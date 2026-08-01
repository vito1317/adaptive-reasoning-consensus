#!/usr/bin/env python
"""G1 final piece: do the capability-wall problems have a nonzero pass rate?

The window measured at n=8 saturates at 7.5% under the oracle@N extrapolation,
so the only route to the 15% gate is rescuing problems where no candidate was
correct in 8 draws. Eight draws cannot distinguish p=0 from p=0.05, so this
re-runs those problems at 4x the budget (32 further candidates each) and
grades them against the hidden suites.

    python experiments/run_g1_deepening.py
"""

from __future__ import annotations

import argparse
import json
import sys
from collections import defaultdict
from concurrent.futures import ProcessPoolExecutor
from pathlib import Path

import numpy as np

sys.path.insert(0, str(Path(__file__).resolve().parents[1] / "src"))

from rlev_voi.sandbox import grade_candidate  # noqa: E402


def _grade(job):
    it, code = job
    return grade_candidate(it["preamble"], code, it["test"], it["entry_point"])


def wilson_upper(k, n, z=1.96):
    if n == 0:
        return 1.0
    p, den = k / n, 1 + z * z / n
    c = (p + z * z / (2 * n)) / den
    h = z * np.sqrt(p * (1 - p) / n + z * z / (4 * n * n)) / den
    return min(1.0, c + h)


def main():
    ap = argparse.ArgumentParser()
    ap.add_argument("--raw", type=Path, default=Path("results/leetcode_wall_raw.json"))
    ap.add_argument("--items", type=Path, default=Path("data/leetcode_items.json"))
    ap.add_argument("--g1", type=Path, default=Path("results/g1_window.json"))
    ap.add_argument("--workers", type=int, default=8)
    ap.add_argument("--out", type=Path, default=Path("results/g1_deepening.json"))
    args = ap.parse_args()

    pools = json.loads(args.raw.read_text())["pools"]
    items = {x["task_id"]: x for x in json.loads(args.items.read_text())}

    jobs, idx = [], []
    for tid, cands in pools.items():
        for c in cands:
            jobs.append((items[tid], c["code"]))
            idx.append(tid)
    print(f"grading {len(jobs)} deepening candidates across {len(pools)} problems...")
    with ProcessPoolExecutor(max_workers=args.workers) as ex:
        res = list(ex.map(_grade, jobs, chunksize=1))

    agg = defaultdict(list)
    for tid, ok in zip(idx, res):
        agg[tid].append(bool(ok))

    print(f"\n{'task':50s} {'diff':6s} {'n':>4} {'pass':>5} {'rate':>7} {'p_upper':>8}  verdict")
    rescued, per = 0, {}
    for tid, oks in agg.items():
        k, n = int(sum(oks)), len(oks)
        # pooled with the original 8 draws, all of which failed
        k_tot, n_tot = k, n + 8
        rescued += k > 0
        per[tid] = dict(n=n_tot, n_pass=k_tot, rate=k_tot / n_tot,
                        p_upper=wilson_upper(k_tot, n_tot))
        print(f"{tid[:50]:50s} {items[tid]['difficulty'][:6]:6s} {n_tot:>4} {k_tot:>5} "
              f"{k_tot/n_tot:>7.3f} {wilson_upper(k_tot,n_tot):>8.3f}  "
              f"{'RESCUED -> enters window' if k else 'true capability wall'}")

    g1 = json.loads(args.g1.read_text())
    N, win = g1["N"], g1["window_n"]
    new = win + rescued
    print(f"\n=== G1 FINAL ===")
    print(f"  window at n=8               : {win}/{N} = {win/N:.3f}")
    print(f"  window at n=40 (deepened)   : {new}/{N} = {new/N:.3f}")
    print(f"  gate                        : 0.150")
    print(f"  VERDICT: {'PASS' if new/N >= 0.15 else 'FAIL -- substrate rejected, KAPPA-P not built'}")
    if rescued == 0:
        pu = max(v["p_upper"] for v in per.values())
        print(f"\n  no wall problem produced a single correct solution in {len(jobs)} further")
        print(f"  attempts; the largest per-problem 95% upper bound on the pass rate is")
        print(f"  {pu:.3f}, so these are capability limits, not sampling luck. Raising the")
        print(f"  candidate budget cannot open this window.")

    args.out.write_text(json.dumps(dict(
        per_problem=per, rescued=rescued, window_n8=win / N, window_deepened=new / N,
        gate_passed=bool(new / N >= 0.15)), indent=1))
    print(f"\nwrote {args.out}")


if __name__ == "__main__":
    main()
