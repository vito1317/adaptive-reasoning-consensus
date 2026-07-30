#!/usr/bin/env python
"""ISC evaluation with the baselines that falsified it (SPEC-ISC section 6).

This script exists because the original ISC headline numbers were committed as
JSON with no generating script and no recorded seeds -- a reproducibility
failure that an adversarial review had to brute-force to reproduce. Every
number in docs/REPORT-ISC.md comes from here.

The baseline list deliberately includes every existing method in this repo.
Both RLEV-VoI and ISC v1 were falsified by ``dedup-SC``, which was missing from
their headline tables; it is mandatory here.

    python experiments/run_isc_eval.py --out results/isc_eval.json
"""

from __future__ import annotations

import argparse
import json
import sys
from pathlib import Path

import numpy as np

sys.path.insert(0, str(Path(__file__).resolve().parents[1] / "src"))

from rlev_voi import DEFAULT  # noqa: E402
from rlev_voi.baselines import run_dedup_sc, run_self_consistency  # noqa: E402
from rlev_voi.discrimination import item_discrimination, pooled_discrimination  # noqa: E402
from rlev_voi.isc import (  # noqa: E402
    ISCEstimate,
    estimate_isc,
    instrument_item,
    isc_vote,
    make_sim_verifier,
)
from rlev_voi.simulate import Cluster, SimConfig, generate_dataset  # noqa: E402
from rlev_voi.tact import _dedup_weights, estimate_label_free, sc_answer, tact_vote  # noqa: E402
from rlev_voi.tempering import GAMMA_MAX_LF, NU_LF, TemperConfig, temper  # noqa: E402

ECHO = SimConfig(
    clusters=(
        Cluster(answer=0, weight=0.40, tightness=0.02),
        Cluster(answer=1, weight=0.60, tightness=0.30, echo_prob=0.85),
    ),
    n_answers=3,
    kappa_c=0.6,
    echo_conf=0.95,
)

#: The cell where deduplication CANNOT help: the wrong cluster is tight but not
#: verbatim, so there is no lexical signature to collapse. This is the honest
#: hard case; the echo cell is not.
PARAPHRASED = SimConfig(
    clusters=(
        Cluster(answer=0, weight=0.40, tightness=0.02),
        Cluster(answer=1, weight=0.60, tightness=0.30, echo_prob=0.0),
    ),
    n_answers=3,
    kappa_c=0.6,
)


def no_instrument_arm(pools, k):
    """Phase B with ZERO instrument queries: dedup-plurality pseudo-labels only.

    This is the ablation that falsified ISC. The earlier 'channel ablation'
    zeroed gamma while KEEPING the anchored answers, which flattered the method
    by attributing to the instrument work the pseudo-labels were doing.
    """
    stats = []
    for p in pools:
        a, c = p.answers[:k], p.confidences[:k]
        _, dw = _dedup_weights(p.dup[:k, :k])
        ref = int(np.argmax(np.bincount(a, weights=dw, minlength=p.n_answers)))
        s = item_discrimination(c, (a == ref).astype(int))
        if s:
            stats.append(s)
    po = pooled_discrimination(stats)
    if po is None:
        return 0.0, 0.0
    g = temper(po.d_hat, po.se, TemperConfig(nu=NU_LF, gamma_max=GAMMA_MAX_LF, p_bar=None))
    acc = float(np.mean([tact_vote(p.answers[:k], p.confidences[:k], p.n_answers, g) == p.correct
                         for p in pools]))
    return g, acc


def instrument_oracle_check(pools, k, verify, n_v, seed):
    """Is the simulated instrument actually noisy, or is it an oracle?"""
    rng = np.random.default_rng(seed)
    dec = right = 0
    for p in pools:
        r = instrument_item(p, k, verify, n_v, rng)
        if r and r.anchored is not None:
            dec += 1
            right += r.anchored == p.correct
    return dec, (right / dec if dec else float("nan"))


def evaluate(cfg, name, items, k, k_max, data_seed, est_seed, p_v, out):
    pools = generate_dataset(cfg, items, k_max, seed=data_seed)
    base = DEFAULT.with_(k_max=k_max)
    verify = make_sim_verifier(p_v=p_v)

    sc = float(np.mean([sc_answer(p.answers[:k], p.n_answers) == p.correct for p in pools]))
    row = {
        "cell": name,
        "SC@K": sc,
        "SC@K+8": float(np.mean([sc_answer(p.answers[: k + 8], p.n_answers) == p.correct for p in pools])),
        "dedup-SC@K": float(np.mean([run_dedup_sc(p, k, base).correct for p in pools])),
        "dedup-SC@K+8": float(np.mean([run_dedup_sc(p, k + 8, base).correct for p in pools])),
    }
    lf = estimate_label_free(pools, k)
    row["TACT-LF"] = float(np.mean([tact_vote(p.answers[:k], p.confidences[:k], p.n_answers, lf.gamma) == p.correct
                                    for p in pools]))
    row["TACT-LF_gamma"] = lf.gamma
    row["TACT-LF_alarms"] = {a: bool(v) for a, v in lf.alarms.items() if v}

    g0, acc0 = no_instrument_arm(pools, k)
    row["NO-INSTRUMENT_gamma"] = g0
    row["NO-INSTRUMENT_acc"] = acc0

    for frac, n_v in [(0.1, 4), (0.5, 8), (1.0, 8)]:
        est = estimate_isc(pools, k, verify, n_v=n_v, instrument_fraction=frac, seed=est_seed)
        acc = float(np.mean([isc_vote(p, i, k, est) == p.correct for i, p in enumerate(pools)]))
        row[f"ISC(f={frac},nv={n_v})"] = acc
        row[f"ISC(f={frac},nv={n_v})_gamma"] = est.gamma
        row[f"ISC(f={frac},nv={n_v})_extra_traces"] = est.diagnostics["n_instrumented"] * n_v / len(pools)

    dec, acc_dec = instrument_oracle_check(pools[:200], k, verify, 8, est_seed)
    row["instrument_decided"] = dec
    row["instrument_decided_accuracy"] = acc_dec

    out["cells"].append(row)
    print(f"\n=== {name} ===")
    for key in ["SC@K", "SC@K+8", "dedup-SC@K", "dedup-SC@K+8", "TACT-LF", "NO-INSTRUMENT_acc",
                "ISC(f=0.1,nv=4)", "ISC(f=0.5,nv=8)", "ISC(f=1.0,nv=8)"]:
        print(f"  {key:22s} {row[key]:.4f}")
    print(f"  instrument decided {dec} items at accuracy {acc_dec:.4f}"
          + ("   <- ORACLE, not a noisy instrument" if acc_dec > 0.99 else ""))
    return row


def instrument_quality_curve(items=400, k=12, k_max=20, data_seed=42, est_seed=7):
    """At what instrument quality does ISC stop working?

    The theory's Corollary says the anchor survives while epsilon < 1/2, i.e.
    p_v > 0.5. That is the *identification* threshold; this measures the
    *usefulness* threshold, which is what a practitioner needs and which the
    real-trace measurement (delta = 0.115, endorsement of 87% of known-wrong
    answers) has to clear.
    """
    pools = generate_dataset(PARAPHRASED, items, k_max, seed=data_seed)
    sc = float(np.mean([sc_answer(p.answers[:k], p.n_answers) == p.correct for p in pools]))
    rows = []
    print(f"\n=== INSTRUMENT QUALITY CURVE (paraphrased cell; SC floor {sc:.4f}) ===")
    print(f"{'p_v':>6} {'delta':>7} {'decided':>8} {'dec.acc':>8} {'ISC acc':>8}  verdict")
    for p_v in (1.00, 0.90, 0.80, 0.70, 0.60, 0.55, 0.52, 0.50):
        verify = make_sim_verifier(p_v=p_v)
        est = estimate_isc(pools, k, verify, n_v=8, instrument_fraction=1.0, seed=est_seed)
        acc = float(np.mean([isc_vote(p, i, k, est) == p.correct for i, p in enumerate(pools)]))
        dec, dacc = instrument_oracle_check(pools[:200], k, verify, 8, est_seed)
        v = "beats SC" if acc > sc + 0.02 else ("= SC" if acc > sc - 0.02 else "BELOW SC")
        print(f"{p_v:>6.2f} {2*p_v-1:>7.2f} {dec:>8d} {dacc:>8.3f} {acc:>8.4f}  {v}")
        rows.append(dict(p_v=p_v, delta=2 * p_v - 1, decided=dec, decided_acc=dacc,
                         isc_acc=acc, beats_sc=bool(acc > sc + 0.02)))
    return {"sc_floor": sc, "curve": rows}


def main():
    ap = argparse.ArgumentParser()
    ap.add_argument("--items", type=int, default=400)
    ap.add_argument("--k", type=int, default=12)
    ap.add_argument("--k-max", type=int, default=20)
    ap.add_argument("--data-seed", type=int, default=42)
    ap.add_argument("--est-seed", type=int, default=7)
    ap.add_argument("--p-v", type=float, default=0.85)
    ap.add_argument("--out", type=Path, default=Path("results/isc_eval.json"))
    args = ap.parse_args()

    out = {"config": vars(args) | {"out": str(args.out)}, "cells": []}
    evaluate(ECHO, "confident_echo (dedup CAN help)", args.items, args.k, args.k_max,
             args.data_seed, args.est_seed, args.p_v, out)
    evaluate(PARAPHRASED, "paraphrased_wrong_majority (dedup CANNOT help)", args.items, args.k,
             args.k_max, args.data_seed, args.est_seed, args.p_v, out)

    echo, para = out["cells"][0], out["cells"][1]
    # Matched budget: ISC at f=1.0,nv=8 spends ~8 extra traces per item, so the
    # honest rivals are SC and dedup-SC given the SAME 8 extra traces.
    out["verdict"] = {
        "echo_cell": {
            "isc_at_+8": echo["ISC(f=1.0,nv=8)"],
            "dedup_sc_at_+8": echo["dedup-SC@K+8"],
            "dedup_sc_at_zero_cost": echo["dedup-SC@K"],
            "F1_falsified": bool(echo["dedup-SC@K+8"] > echo["ISC(f=1.0,nv=8)"]),
            "note": "dedup-SC wins at matched budget AND nearly matches ISC at zero cost",
        },
        "paraphrased_cell": {
            "isc_at_+8": para["ISC(f=1.0,nv=8)"],
            "dedup_sc_at_+8": para["dedup-SC@K+8"],
            "best_non_instrument": max(para["SC@K"], para["dedup-SC@K"],
                                       para["dedup-SC@K+8"], para["TACT-LF"],
                                       para["NO-INSTRUMENT_acc"]),
            "isc_wins": bool(para["ISC(f=1.0,nv=8)"] > max(
                para["SC@K"], para["dedup-SC@K+8"], para["NO-INSTRUMENT_acc"]) + 0.05),
            "note": "the only cell where the instrument is load-bearing -- and it is an oracle here",
        },
        "instrument_is_oracle": bool(echo["instrument_decided_accuracy"] > 0.99),
    }
    print("\n=== VERDICT ===")
    print(json.dumps(out["verdict"], indent=2))
    out["quality_curve"] = instrument_quality_curve(
        args.items, args.k, args.k_max, args.data_seed, args.est_seed)
    args.out.parent.mkdir(parents=True, exist_ok=True)
    args.out.write_text(json.dumps(out, indent=1, default=float))
    print(f"\nWrote {args.out}")


if __name__ == "__main__":
    main()

