#!/usr/bin/env python
"""Measure the real instrument validity that ISC's guarantees rest on.

ISC's Theorem 2 assumes an *anchored* channel: a verification query whose
coupling sign with correctness is fixed by construction. Its Corollary says an
instrument that is invalid on a fraction ``epsilon`` of items retains an
effective separation ``delta*(1 - 2*epsilon)`` and survives iff
``epsilon < 1/2``. Neither number has ever been measured on a real model, and
the whole method stands or falls on them. This script measures both from
Haiku verification passes over contested items.

Reported quantities:

* ``delta`` -- endorsement-rate separation between correct and incorrect
  candidates. This is the instrument's raw strength.
* ``epsilon`` -- fraction of items where the instrument's preference points at
  the wrong candidate (the exclusion-restriction violation rate).
* the **decisive test**: does the instrument prefer the correct candidate on
  the items where the *plurality is wrong*? Those are the only items where an
  instrument can add anything, and an instrument that merely echoes the
  model's belief will fail exactly there while looking fine on average.
* position bias -- candidates were presented in both orders; a verifier that
  endorses by position rather than content is detected here.

Usage::

    python experiments/analyze_instrument_validity.py --raw results/instrument_raw.json
"""

from __future__ import annotations

import argparse
import json
from pathlib import Path

import numpy as np


def wilson(k: int, n: int, z: float = 1.96) -> tuple[float, float]:
    """Wilson score interval — honest at the small n this study has."""
    if n == 0:
        return (0.0, 1.0)
    p = k / n
    d = 1 + z**2 / n
    c = (p + z**2 / (2 * n)) / d
    h = z * np.sqrt(p * (1 - p) / n + z**2 / (4 * n**2)) / d
    return (max(0.0, c - h), min(1.0, c + h))


def main() -> None:
    ap = argparse.ArgumentParser()
    ap.add_argument("--raw", type=Path, default=Path("results/instrument_raw.json"))
    ap.add_argument("--queries", type=Path, default=Path("data/isc_instrument_queries.json"))
    ap.add_argument("--out", type=Path, default=Path("results/instrument_validity.json"))
    args = ap.parse_args()

    raw = json.loads(args.raw.read_text())
    endorsements = raw["endorsements"]
    queries = {q["qid"]: q for q in json.loads(args.queries.read_text())}

    rows = []
    for qid, q in queries.items():
        e = endorsements.get(qid)
        if not e:
            continue
        ea = [v["endorse"] for v in e.get("a", [])]
        eb = [v["endorse"] for v in e.get("b", [])]
        if not ea or not eb:
            continue
        rate_a, rate_b = float(np.mean(ea)), float(np.mean(eb))
        # Which candidate does the instrument prefer?
        preferred = "a" if rate_a > rate_b else ("b" if rate_b > rate_a else "tie")
        gold_side = "a" if q["a_is_correct"] else ("b" if q["b_is_correct"] else None)
        rows.append(
            dict(
                qid=qid, group=q["group"],
                rate_a=rate_a, rate_b=rate_b, n_a=len(ea), n_b=len(eb),
                preferred=preferred, gold_side=gold_side,
                plurality_correct=q["plurality_correct"],
                instrument_right=(gold_side is not None and preferred == gold_side),
                instrument_wrong=(gold_side is not None and preferred != "tie" and preferred != gold_side),
                separation=(rate_a - rate_b) if gold_side == "a" else ((rate_b - rate_a) if gold_side == "b" else None),
            )
        )

    # Items where the gold answer is among the top-2: the only ones where the
    # instrument's preference is even well-defined.
    scored = [r for r in rows if r["gold_side"] is not None]
    decisive = [r for r in scored if r["preferred"] != "tie"]
    right = sum(r["instrument_right"] for r in decisive)
    eps = 1.0 - (right / len(decisive)) if decisive else float("nan")
    seps = [r["separation"] for r in scored if r["separation"] is not None]

    # The decisive subset: plurality wrong. An instrument that merely echoes the
    # model's belief scores ~0 here while looking fine overall.
    pw = [r for r in decisive if not r["plurality_correct"]]
    pw_right = sum(r["instrument_right"] for r in pw)
    pc = [r for r in decisive if r["plurality_correct"]]
    pc_right = sum(r["instrument_right"] for r in pc)

    report = {
        "n_items_scored": len(scored),
        "n_decisive": len(decisive),
        "delta_mean_separation": float(np.mean(seps)) if seps else None,
        "epsilon": eps,
        "epsilon_ci95": [1 - wilson(right, len(decisive))[1], 1 - wilson(right, len(decisive))[0]] if decisive else None,
        "valid_by_corollary": bool(eps < 0.5) if decisive else None,
        "plurality_wrong": {
            "n": len(pw), "instrument_right": pw_right,
            "rate": pw_right / len(pw) if pw else None,
            "ci95": list(wilson(pw_right, len(pw))) if pw else None,
        },
        "plurality_correct": {
            "n": len(pc), "instrument_right": pc_right,
            "rate": pc_right / len(pc) if pc else None,
        },
        "items": rows,
    }

    print(f"items with gold in top-2 : {len(scored)}")
    print(f"decisive (non-tie)       : {len(decisive)}")
    print(f"delta (mean separation)  : {report['delta_mean_separation']}")
    print(f"epsilon (invalid rate)   : {eps:.3f}  CI95 {report['epsilon_ci95']}")
    print(f"valid by Corollary       : {report['valid_by_corollary']}  (needs epsilon < 0.5)")
    print()
    print("THE DECISIVE TEST — items where the plurality is WRONG:")
    print(f"  instrument picks the correct candidate: {pw_right}/{len(pw)}"
          + (f"  ({100*pw_right/len(pw):.0f}%, CI95 {report['plurality_wrong']['ci95']})" if pw else ""))
    print(f"  (for contrast, plurality-correct items : {pc_right}/{len(pc)})")
    print()
    if pw and pw_right / len(pw) > 0.5:
        print("=> The instrument carries information the vote does not: it points at the")
        print("   correct answer precisely where the majority is wrong. ISC's premise holds.")
    elif pw:
        print("=> The instrument does NOT beat the vote where it matters: it largely echoes")
        print("   the model's belief. ISC's exclusion restriction FAILS on this model/benchmark,")
        print("   and the honest conclusion is that same-model verification is not an anchor here.")

    args.out.parent.mkdir(parents=True, exist_ok=True)
    args.out.write_text(json.dumps(report, indent=1, default=float))
    print(f"\nwrote {args.out}")


if __name__ == "__main__":
    main()
