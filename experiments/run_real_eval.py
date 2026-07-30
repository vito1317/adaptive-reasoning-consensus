#!/usr/bin/env python
"""Evaluate TACT on real Claude Haiku traces (GSM8K + CommonsenseQA).

Input: a traces JSON produced by the sampling workflow, mapping qid ->
[{reasoning, answer, confidence}, ...], plus data/real_items.json with gold
answers and group labels.

Protocol (fixed before looking at the traces):
  * dev = the first 20 items of each group (40 items), test = the rest (60).
  * The label-free estimator sees all items UNLABELED; accuracy is reported on
    the test split only. Its transductive character is noted in the paper.
  * Voting budget K = min(12, available traces). Paired McNemar on test.
  * Primary readouts, in order: (1) where the real channel sits -- pooled and
    per-group signed discrimination with CIs; (2) whether TACT's behaviour
    matches its own falsifiable prediction (dead zone if the channel is null,
    CISC-devT-equivalence if positive, signed recovery if negative);
    (3) accuracy vs the baselines.

    ./.venv/bin/python experiments/run_real_eval.py --traces results/real_traces.json
"""

from __future__ import annotations

import argparse
import json
import sys
from pathlib import Path

import numpy as np

sys.path.insert(0, str(Path(__file__).resolve().parents[1] / "src"))

from rlev_voi.backends import Trace, build_pool  # noqa: E402
from rlev_voi.evaluate import expected_calibration_error, mcnemar  # noqa: E402
from rlev_voi.tact import (  # noqa: E402
    estimate_dev,
    estimate_dev_by_group,
    estimate_label_free,
    estimate_lf_by_group,
    group_vote,
    sc_answer,
    tact_vote,
)

CISC_GAMMAS = [0.25, 0.5, 1.0, 2.0, 4.0]
SIGN_GRID = [-4.0, -2.0, -1.0, -0.5, 0.0, 0.5, 1.0, 2.0, 4.0]


def cisc_weight(gamma: float):
    if gamma == 0.0:
        return lambda c: np.ones_like(c)
    if gamma > 0:
        return lambda c: c**gamma
    return lambda c: (1.0 - c) ** (-gamma)


def plain_vote(pool, k, fn):
    a = pool.answers[:k]
    w = fn(pool.confidences[:k])
    return int(np.argmax(np.bincount(a, weights=w, minlength=pool.n_answers))) == pool.correct


def main():
    ap = argparse.ArgumentParser()
    ap.add_argument("--traces", type=Path, default=Path("results/real_traces.json"))
    ap.add_argument("--items", type=Path, default=Path("data/real_items.json"))
    ap.add_argument("--k", type=int, default=12)
    ap.add_argument("--out", type=Path, default=Path("results/real_eval.json"))
    args = ap.parse_args()

    items = {it["qid"]: it for it in json.load(open(args.items))}
    traces = json.load(open(args.traces))

    pools, groups, qids = [], [], []
    for qid, trs in traces.items():
        it = items[qid]
        if len(trs) < 6:
            print(f"  skip {qid}: only {len(trs)} traces")
            continue
        tl = [
            Trace(
                text=t["reasoning"],
                answer=str(t["answer"]),
                confidence=float(np.clip(t["confidence"], 0.01, 0.99)),
                gen_tokens=max(len(t["reasoning"].split()), 1),
            )
            for t in trs
        ]
        pool = build_pool(tl, it["gold"])
        pool.meta["group"] = 0 if it["group"] == "math" else 1
        pool.meta["qid"] = qid
        pools.append(pool)
        groups.append(it["group"])
        qids.append(qid)

    k = args.k
    print(f"pools: {len(pools)}; traces/item median = {int(np.median([p.k_max for p in pools]))}; K = {k}")

    # ---- fixed split: first 20 per group -> dev --------------------------
    dev, test = [], []
    seen = {"math": 0, "commonsense": 0}
    for pool, g in zip(pools, groups):
        if seen[g] < 20:
            dev.append(pool)
            seen[g] += 1
        else:
            test.append(pool)
    print(f"dev {len(dev)} / test {len(test)}")

    # ---- readout 1: where does the real channel sit? ---------------------
    est_all = estimate_dev(pools, k)
    gammas_dev, est_global = estimate_dev_by_group(dev, k, min_items=15)
    per_group_full = {}
    for gname, gid in (("math", 0), ("commonsense", 1)):
        sub = [p for p in pools if p.meta["group"] == gid]
        e = estimate_dev(sub, k)
        per_group_full[gname] = {
            "d_hat": e.pooled.d_hat if e.pooled else None,
            "se": e.pooled.se if e.pooled else None,
            "z": e.pooled.z if e.pooled else None,
            "gamma": e.gamma,
            "n_items": e.pooled.n_items if e.pooled else 0,
        }
    lf_all = estimate_label_free(pools, k, min_gated_items=30)
    gammas_lf, lf_global = estimate_lf_by_group(pools, k, min_items=30, min_gated_items=15)

    conf = np.concatenate([p.confidences[:k] for p in pools])
    hit = np.concatenate([(p.answers[:k] == p.correct).astype(float) for p in pools])
    ece = expected_calibration_error(conf, hit)

    print("\n=== channel diagnosis (all 100 items, labeled) ===")
    print(f"  pooled D = {est_all.pooled.d_hat:+.3f} (SE {est_all.pooled.se:.3f}, z {est_all.pooled.z:+.1f}) -> gamma_dev {est_all.gamma:+.2f}")
    for gname, v in per_group_full.items():
        print(f"  {gname:12s} D = {v['d_hat']:+.3f} (z {v['z']:+.1f}) -> gamma {v['gamma']:+.2f}")
    print(f"  ECE = {ece:.3f}  (the binary gate opens iff <= 0.10)")
    print(f"  label-free: gamma {lf_all.gamma:+.2f}, alarms {[a for a,v in lf_all.alarms.items() if v] or 'none'}, d_raw {lf_all.diagnostics.get('d_raw', float('nan')):+.3f}")
    print(f"  per-group gammas: dev {gammas_dev} | LF {gammas_lf}")

    # ---- readout 2+3: accuracy on test -----------------------------------
    dev_est = estimate_dev(dev, k)

    def dev_pick(grid):
        best_g, best_acc = 0.0, -1.0
        for g in grid:
            acc = float(np.mean([plain_vote(p, k, cisc_weight(g)) for p in dev]))
            if acc > best_acc + 1e-12:
                best_g, best_acc = g, acc
        return best_g

    g_devT = dev_pick([0.0] + CISC_GAMMAS)
    g_sign = dev_pick(SIGN_GRID)
    conf_dev = np.concatenate([p.confidences[:k] for p in dev])
    hit_dev = np.concatenate([(p.answers[:k] == p.correct).astype(float) for p in dev])
    ece_gate_open = expected_calibration_error(conf_dev, hit_dev) <= 0.10

    res = {}
    res["SC"] = np.array([sc_answer(p.answers[:k], p.n_answers) == p.correct for p in test])
    for g in CISC_GAMMAS:
        res[f"CISC(g={g})"] = np.array([plain_vote(p, k, cisc_weight(g)) for p in test])
    res["ECE-gate"] = np.array([plain_vote(p, k, (lambda c: c) if ece_gate_open else (lambda c: np.ones_like(c))) for p in test])
    res["CISC-devT"] = np.array([plain_vote(p, k, cisc_weight(g_devT)) for p in test])
    res["SignGrid-dev"] = np.array([plain_vote(p, k, cisc_weight(g_sign)) for p in test])
    res["TACT-dev"] = np.array([tact_vote(p.answers[:k], p.confidences[:k], p.n_answers, dev_est.gamma) == p.correct for p in test])
    res["TACT-LF"] = np.array([tact_vote(p.answers[:k], p.confidences[:k], p.n_answers, lf_all.gamma) == p.correct for p in test])
    res["TACT-group-dev"] = np.array([group_vote(p, k, gammas_dev, est_global.gamma) == p.correct for p in test])
    res["TACT-group-LF"] = np.array([group_vote(p, k, gammas_lf, lf_global.gamma) == p.correct for p in test])
    oracle_acc = max(float(np.mean([plain_vote(p, k, cisc_weight(g)) for p in test])) for g in SIGN_GRID)

    print("\n=== test accuracy (n = %d, K = %d) ===" % (len(test), k))
    for m, v in res.items():
        print(f"  {m:16s} {v.mean():.3f}")
    print(f"  {'oracle(sign)':16s} {oracle_acc:.3f}")
    print(f"  gammas: TACT-dev {dev_est.gamma:+.2f} | devT {g_devT:+.2f} | signgrid {g_sign:+.2f}")

    paired = {
        "TACT-dev_vs_SC": mcnemar(res["TACT-dev"], res["SC"]),
        "TACT-dev_vs_CISC-devT": mcnemar(res["TACT-dev"], res["CISC-devT"]),
        "TACT-LF_vs_SC": mcnemar(res["TACT-LF"], res["SC"]),
        "TACT-group-dev_vs_TACT-dev": mcnemar(res["TACT-group-dev"], res["TACT-dev"]),
    }
    print("\npaired (McNemar):")
    for kk, v in paired.items():
        print(f"  {kk:30s} +{v['a_only']}/-{v['b_only']} p={v['p_value']:.3f}")

    out = {
        "n_pools": len(pools), "k": k,
        "channel": {
            "pooled": {"d_hat": est_all.pooled.d_hat, "se": est_all.pooled.se, "z": est_all.pooled.z, "gamma": est_all.gamma},
            "per_group": per_group_full,
            "ece": float(ece),
            "lf": {"gamma": lf_all.gamma, "alarms": lf_all.alarms,
                   "diag": {kk: vv for kk, vv in lf_all.diagnostics.items() if isinstance(vv, (int, float))}},
            "group_gammas_dev": {str(kk): vv for kk, vv in gammas_dev.items()},
            "group_gammas_lf": {str(kk): vv for kk, vv in gammas_lf.items()},
        },
        "test_acc": {m: float(v.mean()) for m, v in res.items()},
        "oracle_sign": oracle_acc,
        "gammas": {"TACT-dev": dev_est.gamma, "CISC-devT": g_devT, "SignGrid": g_sign, "TACT-LF": lf_all.gamma},
        "paired": paired,
    }
    args.out.parent.mkdir(parents=True, exist_ok=True)
    args.out.write_text(json.dumps(out, indent=2, default=float))
    print(f"\nWrote {args.out}")


if __name__ == "__main__":
    main()
