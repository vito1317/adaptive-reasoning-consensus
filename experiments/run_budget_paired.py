#!/usr/bin/env python
"""Paired test: does removing the reasoning budget open the addressable window?

The thin-window scan had only ever moved along item difficulty, where items
pass from saturated straight to capability-limited. Reasoning budget is a
second axis, and a more promising one in principle: constraining it lowers
per-sample accuracy while leaving the correct answer inside the model's
competence, which is the condition the decisive stratum needs.

The design is paired. Same 119 MATH level-5 items, same frozen model, same
K=16; the only difference is whether the model may write working. The
unconstrained arm is the confirmatory campaign already reported, so every
quantity here can be compared item by item.

A first attempt on GSM8K failed its manipulation check -- forbidding scratch
work there RAISED per-sample accuracy, because the model does not need working
for those problems (docs/REPORT-BUDGET.md). The manipulation check is
therefore reported first here, and the window comparison is only meaningful
if it passes.

    python experiments/run_budget_paired.py
"""

from __future__ import annotations

import argparse
import json
import sys
from collections import Counter
from pathlib import Path

import numpy as np
from scipy.stats import binomtest

sys.path.insert(0, str(Path(__file__).resolve().parents[1] / "src"))

from rlev_voi.discrimination import item_discrimination, pooled_discrimination  # noqa: E402
from rlev_voi.math_grade import canon, equivalent  # noqa: E402


def summarise(traces: dict, gold: dict, min_n: int = 6) -> dict:
    rows, stats = [], []
    for qid, tr in traces.items():
        if len(tr) < min_n:
            continue
        raw = [canon(t["answer"]) for t in tr]
        conf = np.array([float(t.get("confidence", 0.5)) for t in tr])
        g = gold[qid]
        buckets = Counter(raw)
        plur = buckets.most_common(1)[0][0]
        correct = np.array([equivalent(a, g) for a in raw], int)
        rows.append(dict(qid=qid, n=len(raw), K=len(buckets),
                         per_sample=float(correct.mean()),
                         plur_ok=bool(equivalent(plur, g)),
                         gold_in=bool(any(equivalent(b, g) for b in buckets))))
        s = item_discrimination(conf, correct)
        if s:
            stats.append(s)
    po = pooled_discrimination(stats)
    dec = [r for r in rows if not r["plur_ok"]]
    win = [r for r in dec if r["gold_in"]]
    return dict(
        n=len(rows),
        per_sample=float(np.mean([r["per_sample"] for r in rows])),
        sc=float(np.mean([r["plur_ok"] for r in rows])),
        oracle=float(np.mean([r["gold_in"] for r in rows])),
        decisive=len(dec) / max(len(rows), 1),
        window=len(win) / max(len(rows), 1),
        window_n=len(win),
        d_hat=po.d_hat if po else None, se=po.se if po else None,
        z=po.z if po else None, d_items=po.n_items if po else 0,
        rows={r["qid"]: r for r in rows},
    )


def main():
    ap = argparse.ArgumentParser()
    ap.add_argument("--constrained", type=Path, default=Path("results/mathl5_budget_raw.json"))
    ap.add_argument("--free", type=Path, default=Path("results/math_confirm_raw.json"))
    ap.add_argument("--items", type=Path, default=Path("data/math_confirm_items.json"))
    ap.add_argument("--out", type=Path, default=Path("results/budget_paired.json"))
    args = ap.parse_args()

    gold = {x["qid"]: x["gold"] for x in json.loads(args.items.read_text())}
    free = summarise(json.loads(args.free.read_text())["traces"], gold)
    con = summarise(json.loads(args.constrained.read_text())["traces"], gold)

    print("=== MANIPULATION CHECK (must pass before the rest means anything) ===")
    print(f"  per-sample accuracy, full reasoning : {free['per_sample']:.3f}  (n={free['n']})")
    print(f"  per-sample accuracy, no working     : {con['per_sample']:.3f}  (n={con['n']})")
    drop = free["per_sample"] - con["per_sample"]
    passed = drop > 0.10
    print(f"  drop: {drop:+.3f}  -> {'PASS, the constraint bites' if passed else 'FAIL, the constraint had no effect'}")

    print(f"\n{'quantity':28s} {'full reasoning':>15s} {'no working':>12s}")
    for k, lbl in [("sc", "SC accuracy"), ("oracle", "oracle (gold in pool)"),
                   ("decisive", "decisive stratum"), ("window", "WINDOW")]:
        print(f"  {lbl:26s} {free[k]:>15.3f} {con[k]:>12.3f}")
    print(f"  {'pooled D-hat':26s} {free['d_hat']:>+15.3f} {con['d_hat']:>+12.3f}"
          if free["d_hat"] is not None and con["d_hat"] is not None else "")
    print(f"  {'z':26s} {free['z']:>+15.2f} {con['z']:>+12.2f}"
          if free["z"] is not None and con["z"] is not None else "")

    # paired McNemar on the window membership of shared items
    shared = set(free["rows"]) & set(con["rows"])
    b = sum(1 for q in shared if con["rows"][q]["gold_in"] and not con["rows"][q]["plur_ok"]
            and not (free["rows"][q]["gold_in"] and not free["rows"][q]["plur_ok"]))
    c = sum(1 for q in shared if free["rows"][q]["gold_in"] and not free["rows"][q]["plur_ok"]
            and not (con["rows"][q]["gold_in"] and not con["rows"][q]["plur_ok"]))
    p = binomtest(b, b + c, 0.5, alternative="greater").pvalue if b + c else 1.0
    print(f"\n  paired items: {len(shared)}")
    print(f"  entered the window under the constraint : {b}")
    print(f"  left the window under the constraint    : {c}")
    print(f"  exact one-sided p = {p:.4f}")

    verdict = ("substrate found: the constraint opens a measurable window"
               if passed and con["window"] >= 0.15
               else "window stays shut: the thin window holds across budget as well as difficulty"
               if passed else "inconclusive: manipulation check failed")
    print(f"\nVERDICT: {verdict}")
    args.out.write_text(json.dumps(dict(free=free, constrained=con, manipulation_passed=bool(passed),
                                        entered=b, left=c, p=p, verdict=verdict), indent=1, default=float))
    print(f"wrote {args.out}")


if __name__ == "__main__":
    main()
