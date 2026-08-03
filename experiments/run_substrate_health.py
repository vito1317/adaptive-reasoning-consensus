#!/usr/bin/env python
"""Substrate health: can this (model, benchmark) pair support the experiment at all?

Two campaigns in this project spent their whole budget on substrates that could
not have produced a result, and in both cases the reason was visible before any
method ran. This computes the panel that would have said so, so it can be run at
design time instead of discovered afterwards.

The panel extends the two figures the paper already reports:

  decisive_n     items whose plurality is wrong. Nothing above SC can change an
                 item outside this set.
  gold_in_pool   of those, how many have the correct answer somewhere in the
                 pool. This is the ceiling for any label-free aggregator.
  n_gated        NEW. How many items survive the label-free pipeline's margin
                 gate with a pseudo-label that varies. TACT-LF cannot form an
                 estimate from fewer than min_gated_items of these, so a
                 substrate that cannot supply them has already decided the
                 outcome -- the channel is never consulted. On the GSM8K/CSQA
                 pools this is 0 by construction; on MATH L5 it is 13 against a
                 floor of 50, and relaxing margin_quantile all the way to 0
                 only reaches 40, so the binding constraint is item supply and
                 not the gate threshold.
  sign_set_z     NEW, and separate from the above. The semi-label-free mode
                 takes only a SIGN from a small labelled set, gated at |z|>1. A
                 sign set that misses that threshold blocks semi-LF for a
                 reason that has nothing to do with the label-free pipeline's
                 alarms, and the two failures should not be reported as one.

Bucketing. Each substrate is bucketed the way its own campaign buckets it:
integers and multiple-choice letters through backends.build_pool, LaTeX through
math_grade.build_math_pool, which folds mathematical-equivalence classes. An
earlier version of this panel sent MATH through the former and reported 13
decisive items where the campaign reports 10, because plain string equality
splits 1/2 from 0.5. Two artifacts disagreeing about one substrate is worse than
no panel at all, so the counts here are asserted against the campaign's in
check_paper_numbers.py.

Reading rule. n_gated below min_gated_items means the label-free arm is
untestable on this substrate at any channel strength; sign_set_z below 1 means
the semi-label-free arm is untestable for want of labels. Neither is evidence
about the method.

    python experiments/run_substrate_health.py
"""

from __future__ import annotations

import argparse
import json
import sys
from pathlib import Path

import numpy as np

ROOT = Path(__file__).resolve().parents[1]
sys.path.insert(0, str(ROOT / "src"))

from rlev_voi.backends import Trace, build_pool  # noqa: E402
from rlev_voi.math_grade import build_math_pool  # noqa: E402
from rlev_voi.tact import estimate_dev, estimate_label_free  # noqa: E402

MARGIN_SWEEP = [0.40, 0.30, 0.20, 0.10, 0.0]
SEMI_SIGN_THRESHOLD = 1.0     # estimate_semi_lf gates the sign at |z| > 1


def pools_from(traces: dict, gold: dict, qids: list[str]) -> list:
    out = []
    for q in qids:
        tl = [Trace(text=str(t.get("reasoning", "")), answer=str(t["answer"]),
                    confidence=float(np.clip(t["confidence"], 0.01, 0.99)),
                    gen_tokens=max(len(str(t.get("reasoning", "")).split()), 1))
              for t in traces[q]]
        out.append(build_pool(tl, gold[q]))
    return out


def strata(pools, k: int) -> dict:
    dec = inpool = 0
    for p in pools:
        a = p.answers[:k]
        counts = np.bincount(a, minlength=p.n_answers)
        if int(np.argmax(counts)) != p.correct:
            dec += 1
            if p.correct >= 0 and counts[p.correct] > 0:
                inpool += 1
    return {"n_items": len(pools), "decisive_n": dec, "gold_in_pool_of_decisive": inpool,
            "decisive_pct": 100.0 * dec / len(pools),
            "window_pct": 100.0 * inpool / len(pools)}


def gate_supply(pools, k: int, floor: int) -> dict:
    """n_gated at the shipped threshold, and under every relaxation of it."""
    sweep = {}
    for mq in MARGIN_SWEEP:
        e = estimate_label_free(pools, k, margin_quantile=mq, min_gated_items=1)
        sweep[f"{mq:.2f}"] = e.diagnostics.get("n_gated") or 0
    shipped = sweep[f"{MARGIN_SWEEP[0]:.2f}"]
    best = max(sweep.values())
    return {"min_gated_items": floor, "n_gated_shipped": shipped,
            "n_gated_by_margin_quantile": sweep, "n_gated_best_case": best,
            "label_free_testable": bool(best >= floor)}


def main() -> None:
    ap = argparse.ArgumentParser()
    ap.add_argument("--out", type=Path, default=ROOT / "results/substrate_health.json")
    args = ap.parse_args()
    report = {}

    # --- GSM8K + CommonsenseQA, K=12 ---------------------------------------
    tr = json.loads((ROOT / "data/real_traces_full.json").read_text())
    meta = {it["qid"]: it for it in json.loads((ROOT / "data/real_items.json").read_text())}
    qids = [q for q in tr if q in meta and len(tr[q]) >= 6]
    gold = {q: str(meta[q]["gold"]) for q in qids}
    ps = pools_from(tr, gold, qids)
    report["gsm8k_csqa"] = {"k": 12, **strata(ps, 12), **gate_supply(ps, 12, 50)}

    # --- MATH level-5, K=16, with the pre-registered 30-item sign set -------
    # Bucketing MUST come through build_math_pool, the same equivalence-class
    # builder the campaign uses. Going through backends.build_pool here is what
    # produced a panel that disagreed with the campaign on the same substrate
    # (13 decisive items against 10), because string equality splits 1/2 from
    # 0.5 and over-counts distinct answers.
    raw = json.loads((ROOT / "results/math_confirm_raw.json").read_text())["traces"]
    mi = {it["qid"]: it for it in json.loads((ROOT / "data/math_confirm_items.json").read_text())}
    allq = sorted(q for q in raw if q in mi)
    g = {q: str(mi[q]["gold"]) for q in allq}
    sign_q = set(np.array(allq)[np.random.default_rng(20260731).permutation(len(allq))[:30]])
    ev_q = [q for q in allq if q not in sign_q]
    ev = [p for p in (build_math_pool(q, raw[q], g[q]) for q in ev_q) if p is not None]
    sg = [p for p in (build_math_pool(q, raw[q], g[q]) for q in sorted(sign_q)) if p is not None]

    sp = estimate_dev(sg, 16).pooled
    ep = estimate_dev(ev, 16).pooled
    report["math_l5_eval"] = {
        "k": 16, **strata(ev, 16), **gate_supply(ev, 16, 50),
        "sign_set": {
            "n_items": len(sg),
            "z": sp.z, "d_hat": sp.d_hat, "se": sp.se,
            "threshold": SEMI_SIGN_THRESHOLD,
            "semi_lf_testable": bool(abs(sp.z) > SEMI_SIGN_THRESHOLD),
            "eval_set_z_for_contrast": ep.z,
        },
    }

    for name, r in report.items():
        print(f"=== {name} (K={r['k']}, {r['n_items']} items) ===")
        print(f"  decisive {r['decisive_n']:3d} ({r['decisive_pct']:.1f}%)   "
              f"window {r['gold_in_pool_of_decisive']:3d} ({r['window_pct']:.1f}%)")
        print(f"  n_gated {r['n_gated_shipped']:3d} at the shipped margin gate; "
              f"best case {r['n_gated_best_case']} against a floor of {r['min_gated_items']}"
              f"  -> label-free {'testable' if r['label_free_testable'] else 'UNTESTABLE'}")
        print(f"     by margin_quantile: {r['n_gated_by_margin_quantile']}")
        if "sign_set" in r:
            s = r["sign_set"]
            print(f"  sign set ({s['n_items']} items): z={s['z']:+.3f} against a threshold of "
                  f"{s['threshold']}  -> semi-label-free "
                  f"{'testable' if s['semi_lf_testable'] else 'UNTESTABLE'}")
            print(f"     for contrast, the evaluation set reaches z={s['eval_set_z_for_contrast']:+.3f} "
                  "on the same substrate, so this is a power shortfall in the sign set,\n"
                  "     not the channel being absent")
        print()

    args.out.write_text(json.dumps(report, indent=1))
    print(f"wrote {args.out.relative_to(ROOT)}")


if __name__ == "__main__":
    main()
