#!/usr/bin/env python
"""G1 window gate for KAPPA-P (docs/SPEC-KAPPA-P.md).

The reframe rests on one claim: hard, non-saturated code benchmarks have an
addressable window far wider than the 3.56% measured on HumanEval+/MBPP+.
This measures it directly on LeetCodeDataset Medium/Hard with a frozen model.

    window = oracle@N - baseline@N

where oracle@N is "at least one candidate passes the hidden suite" (the
ceiling for ANY label-free selector) and baseline@N is the standard
label-free selector: cluster candidates by behavioural fingerprint on probe
INPUTS only (never expected outputs), take the largest cluster's
representative -- the DiffCodeGen/CodeT consensus rule.

GATE: window >= 15% or the substrate is rejected and KAPPA-P is not built.

Grading and fingerprinting run in a resource-limited subprocess
(rlev_voi.sandbox); the 2 dataset items whose own reference solution does not
pass under those limits are excluded upstream, so a failure here is the
candidate's, not the harness's.

    python experiments/run_g1_window.py --raw results/leetcode_g1_raw.json
"""

from __future__ import annotations

import argparse
import json
import sys
from collections import Counter
from concurrent.futures import ProcessPoolExecutor
from pathlib import Path

import numpy as np
from scipy.stats import binomtest

sys.path.insert(0, str(Path(__file__).resolve().parents[1] / "src"))

from rlev_voi.sandbox import fingerprint, grade_candidate  # noqa: E402


def _one(job):
    """Grade + fingerprint a single candidate (runs in a worker process)."""
    it, cand = job
    ok = grade_candidate(it["preamble"], cand["code"], it["test"], it["entry_point"])
    fp = fingerprint(it["preamble"], cand["code"], it["entry_point"], it["inputs"][:8])
    return ok, tuple(fp)


def wilson(k, n, z=1.96):
    if n == 0:
        return (0.0, 1.0)
    p, den = k / n, 1 + z * z / n
    c = (p + z * z / (2 * n)) / den
    h = z * np.sqrt(p * (1 - p) / n + z * z / (4 * n * n)) / den
    return (max(0.0, c - h), min(1.0, c + h))


def main():
    ap = argparse.ArgumentParser()
    ap.add_argument("--raw", type=Path, default=Path("results/leetcode_g1_raw.json"))
    ap.add_argument("--items", type=Path, default=Path("data/leetcode_items.json"))
    ap.add_argument("--workers", type=int, default=8)
    ap.add_argument("--out", type=Path, default=Path("results/g1_window.json"))
    args = ap.parse_args()

    pools = json.loads(args.raw.read_text())["pools"]
    items = {x["task_id"]: x for x in json.loads(args.items.read_text())}

    jobs, index = [], []
    for tid, cands in pools.items():
        for c in cands:
            jobs.append((items[tid], c))
            index.append(tid)
    print(f"grading {len(jobs)} candidates across {len(pools)} problems "
          f"(sandboxed, {args.workers} workers)...")
    with ProcessPoolExecutor(max_workers=args.workers) as ex:
        results = list(ex.map(_one, jobs, chunksize=1))

    per_item = {tid: {"ok": [], "fp": [], "conf": []} for tid in pools}
    for (tid, (ok, fp)), (it, cand) in zip(zip(index, results), jobs):
        per_item[tid]["ok"].append(bool(ok))
        per_item[tid]["fp"].append(fp)
        per_item[tid]["conf"].append(float(cand.get("confidence", 0.5)))

    rows = []
    print(f"\n{'task':46s} {'diff':6s} {'n':>2} {'pass':>5} {'clus':>4} {'base':>5} {'orac':>5}")
    for tid, d in per_item.items():
        n = len(d["ok"])
        if n < 4:
            continue
        oracle = any(d["ok"])
        # largest behavioural cluster; ties broken by mean confidence
        counts = Counter(d["fp"])
        best = max(counts.items(), key=lambda kv: (kv[1], np.mean(
            [d["conf"][i] for i, f in enumerate(d["fp"]) if f == kv[0]])))[0]
        members = [i for i, f in enumerate(d["fp"]) if f == best]
        base = bool(d["ok"][members[0]])
        rows.append(dict(task_id=tid, difficulty=items[tid]["difficulty"], n=n,
                         n_pass=int(sum(d["ok"])), n_clusters=len(counts),
                         baseline_correct=base, oracle_correct=bool(oracle),
                         in_window=bool(oracle and not base)))
        print(f"{tid[:46]:46s} {items[tid]['difficulty'][:6]:6s} {n:>2} "
              f"{sum(d['ok']):>5} {len(counts):>4} {str(base)[:5]:>5} {str(oracle)[:5]:>5}")

    N = len(rows)
    orc = sum(r["oracle_correct"] for r in rows)
    bas = sum(r["baseline_correct"] for r in rows)
    win = sum(r["in_window"] for r in rows)
    per_samp = float(np.mean([r["n_pass"] / r["n"] for r in rows]))

    print(f"\n=== G1 WINDOW GATE (N={N} problems) ===")
    print(f"  per-candidate pass rate (pass@1) : {per_samp:.3f}")
    print(f"  baseline  (largest cluster)      : {bas}/{N} = {bas/N:.3f}")
    print(f"  oracle    (any candidate passes) : {orc}/{N} = {orc/N:.3f}")
    print(f"  WINDOW  (oracle - baseline)      : {win}/{N} = {win/N:.3f}  "
          f"CI95 {tuple(round(x,3) for x in wilson(win, N))}")
    print(f"  reference: HumanEval+/MBPP+ 3.56%, QA thin window 2-5%, gate 15%")

    passed = win / N >= 0.15
    print(f"\n  G1: {'PASS -- substrate admits a measurable endpoint' if passed else 'FAIL -- substrate rejected, do not build'}")
    if passed:
        # power for the primary endpoint at published capture rates
        for c in (0.20, 0.33, 0.50):
            conv = int(round(win * c))
            p = binomtest(conv, max(conv, 1), 0.5, alternative="greater").pvalue if conv else 1.0
            print(f"    at capture {c:.0%}: {conv}/{win} converted, best-case exact p = {p:.4f}")
        print(f"    (to reach p<0.05 with no regressions, need >= 5 conversions)")

    for diff in ("Medium", "Hard"):
        sub = [r for r in rows if r["difficulty"] == diff]
        if sub:
            w = sum(r["in_window"] for r in sub)
            print(f"  {diff:6s}: N={len(sub):>2}  window {w}/{len(sub)} = {w/len(sub):.3f}")

    args.out.write_text(json.dumps(dict(
        N=N, pass_at_1=per_samp, baseline=bas / N, oracle=orc / N,
        window=win / N, window_ci=wilson(win, N), window_n=win,
        gate_passed=bool(passed), rows=rows), indent=1))
    print(f"\nwrote {args.out}")


if __name__ == "__main__":
    main()
