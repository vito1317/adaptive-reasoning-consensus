#!/usr/bin/env python
"""Is a cross-model verifier a valid instrument, or just a stronger solver?

The ISC negative result (docs/REPORT-ISC.md) left one diagnosis untested: the
same-model verifier fails because it shares the model's errors, so a *different*
model should work. This measures that -- but with the confound control the
claim needs.

Arm A: the other model does forced-choice verification between the two
candidates (the instrument).
Arm B: the other model solves the item from scratch, never seeing the
candidates (the control).

If A and B agree item-for-item, "cross-model verification" is not an
instrument-validity result: it is outsourcing the item to a stronger model,
which needs no identification theory and no ISC.

    python experiments/analyze_cross_model.py --raw results/cross_model_raw.json
"""

from __future__ import annotations

import argparse
import json
import sys
from pathlib import Path

import numpy as np

sys.path.insert(0, str(Path(__file__).resolve().parents[1] / "src"))

from rlev_voi.backends import normalise_answer  # noqa: E402


def wilson(k: int, n: int, z: float = 1.96) -> tuple[float, float]:
    if n == 0:
        return (0.0, 1.0)
    p = k / n
    den = 1 + z * z / n
    centre = (p + z * z / (2 * n)) / den
    half = z * np.sqrt(p * (1 - p) / n + z * z / (4 * n * n)) / den
    return (max(0.0, centre - half), min(1.0, centre + half))


def main():
    ap = argparse.ArgumentParser()
    ap.add_argument("--raw", type=Path, default=Path("results/cross_model_raw.json"))
    ap.add_argument("--queries", type=Path, default=Path("data/isc_instrument_queries.json"))
    ap.add_argument("--out", type=Path, default=Path("results/cross_model_validity.json"))
    args = ap.parse_args()

    raw = json.loads(args.raw.read_text())
    Q = {q["qid"]: q for q in json.loads(args.queries.read_text())}
    verify, solve = raw["verify"], raw["solve"]

    print(f"{'qid':11s} {'plur':>5} {'gold':>5} | {'A:P(a)':>7} {'A pick':>7} | {'B solve':>9} | verdict")
    rows = []
    for qid in Q:
        q = Q[qid]
        gs = "a" if q["a_is_correct"] else ("b" if q["b_is_correct"] else None)
        v = verify.get(qid, [])
        s = solve.get(qid, [])
        if not v:
            continue
        pa = float(np.mean([c["chose"] == "a" for c in v]))
        pick = "a" if pa > 0.5 else ("b" if pa < 0.5 else "tie")

        # Arm B: majority of the other model's independent solves, mapped onto
        # the candidate pair when it lands there.
        gold_norm = normalise_answer(str(q.get("gold", "")))
        norm = [normalise_answer(x) for x in s]
        b_major = max(set(norm), key=norm.count) if norm else ""
        cand_a, cand_b = normalise_answer(q["cand_a"]), normalise_answer(q["cand_b"])
        b_pick = "a" if b_major == cand_a else ("b" if b_major == cand_b else "other")
        b_right = (gs is not None) and (b_pick == gs)

        v_ok = "n/a" if gs is None else ("tie" if pick == "tie" else ("RIGHT" if pick == gs else "WRONG"))
        print(f"{qid:11s} {str(q['plurality_correct']):>5} {str(gs):>5} | {pa:>7.2f} {pick:>7s} | "
              f"{b_major[:9]:>9s} | A:{v_ok} B:{'RIGHT' if b_right else ('n/a' if gs is None else 'WRONG')}")
        rows.append(dict(qid=qid, gold=gs, a_pick=pick, a_p=pa, b_major=b_major, b_pick=b_pick,
                         plurality_correct=q["plurality_correct"],
                         a_right=(gs is not None and pick == gs),
                         b_right=bool(b_right), scorable=gs is not None))

    scorable = [r for r in rows if r["scorable"]]
    dec = [r for r in scorable if r["a_pick"] != "tie"]
    pw = [r for r in dec if not r["plurality_correct"]]
    pwB = [r for r in scorable if not r["plurality_correct"]]

    a_right = sum(r["a_right"] for r in dec)
    pw_right = sum(r["a_right"] for r in pw)
    pwB_right = sum(r["b_right"] for r in pwB)
    agree = sum(r["a_pick"] == r["b_pick"] for r in scorable)

    out = {
        "n_scorable": len(scorable),
        "arm_A": {
            "decisive": len(dec),
            "right": a_right,
            "decisive_subset_right": pw_right,
            "decisive_subset_n": len(pw),
            "decisive_subset_ci": wilson(pw_right, len(pw)),
        },
        "arm_B_control": {
            "decisive_subset_right": pwB_right,
            "decisive_subset_n": len(pwB),
        },
        "A_B_agreement": agree / max(len(scorable), 1),
        "rows": rows,
    }

    print("\n=== ARM A: cross-model verification (the instrument) ===")
    print(f"  overall right on decisive items : {a_right}/{len(dec)}")
    print(f"  DECISIVE SUBSET (plurality wrong): {pw_right}/{len(pw)}"
          + (f"  CI95 {tuple(round(x,3) for x in out['arm_A']['decisive_subset_ci'])}" if pw else ""))
    print("  [same-model endorsement was 1/5; same-model forced-choice was 2/4]")

    print("\n=== ARM B: cross-model SOLVE (the confound control) ===")
    print(f"  DECISIVE SUBSET (plurality wrong): {pwB_right}/{len(pwB)}")
    print(f"  A/B agreement over all scorable items: {out['A_B_agreement']:.2f}")
    if out["A_B_agreement"] > 0.85:
        print("\n  => The 'instrument' tracks the other model's own answer almost exactly.")
        print("     This is OUTSOURCING to a stronger solver, not instrument validity:")
        print("     no identification theory is needed to justify 'ask a better model'.")

    args.out.write_text(json.dumps(out, indent=1, default=float))
    print(f"\nwrote {args.out}")


if __name__ == "__main__":
    main()
