#!/usr/bin/env python
"""Planted-signal sensitivity on real pools: at what channel strength does the gate open?

The abstention replays (run_abstention_identifiability.py) measured specificity
on the real substrate and left sensitivity unmeasured, because the real channel
carried no signal to detect. This plants one of known strength into the same
pools and sweeps it.

AVOIDING THE CIRCULARITY. Planting a channel drawn from the estimator's own
working model and then detecting it proves nothing; this paper already shipped
three "adversarial" distortion cells that turned out to sit inside TACT's own
invariance group. The way out is to be precise about which claim is at risk.

The estimator's target, D, is a distribution-free rank functional. Detecting a
planted D is therefore NOT circular as long as families with different
generative shapes but the same realized D behave the same -- that is the
detector measuring D rather than the family, which is exactly what it claims.
What genuinely depends on the working model is the LINK: gamma is derived
assuming phi | y is normal with equal variances, and nothing guarantees that
outside the oracle's location-shift model. So the design separates them:

  * detection  swept across four families, compared at matched |D|. If the
               curves coincide, detection is a property of D and the plant
               family is not doing the work.
  * magnitude  the accuracy the derived gamma achieves against the accuracy a
               gold-label oracle gamma achieves, per family. A gap that opens
               only off the Gaussian family convicts the link, not the gate.

Families (real answers, pools, item difficulty and duplication all untouched;
only the confidence vector is replaced):
  location    c = 1/2 + s(y - 1/2) + N(0, 0.1^2)   -- the oracle's own model,
              included as the reference, labelled as circular by construction
  heavy_tail  the same location shift with Laplace noise, so phi | y is not
              normal and the link's assumption is violated while D survives
  rank_local  iid uniform confidence, then with probability s the top-confidence
              slot is forced onto a correct trace: real D, but concentrated in
              one rank position instead of spread as a location shift
  variance    no location shift at all; wrong traces merely get a wider spread.
              D is 0 by construction although the channel is informative, so
              the correct behaviour is to abstain. This is the scope test: it
              shows what the method cannot see, and that it does not pretend to.

    python experiments/run_planted_sensitivity.py
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
from rlev_voi.discrimination import item_discrimination, pooled_discrimination, vdw_scores  # noqa: E402
from rlev_voi.formula import gamma_of  # noqa: E402
from rlev_voi.tact import estimate_label_free  # noqa: E402
from rlev_voi.tempering import GAMMA_MAX_DEV, NU_DEV  # noqa: E402

LADDER = [0.0, 0.03, 0.05, 0.07, 0.10, 0.20, 0.30, 0.45, 0.60, 0.80]
FAMILIES = ["location", "heavy_tail", "rank_local", "variance"]
GAMMA_GRID = np.arange(-4.0, 4.001, 0.25)


def load_pools(traces: Path, items: Path):
    meta = {it["qid"]: it for it in json.loads(items.read_text())}
    raw = json.loads(traces.read_text())
    pools, groups = [], []
    for qid, trs in raw.items():
        if len(trs) < 6:
            continue
        tl = [Trace(text=t["reasoning"], answer=str(t["answer"]),
                    confidence=float(np.clip(t["confidence"], 0.01, 0.99)),
                    gen_tokens=max(len(t["reasoning"].split()), 1)) for t in trs]
        pools.append(build_pool(tl, meta[qid]["gold"]))
        groups.append(meta[qid]["group"])
    return pools, groups


def plant(y: np.ndarray, family: str, s: float, rng) -> np.ndarray:
    """A confidence vector for one item, conditioned on the real correctness y."""
    m = y.shape[0]
    if family == "location":
        c = 0.5 + s * (y - 0.5) + rng.normal(0.0, 0.1, m)
    elif family == "heavy_tail":
        c = 0.5 + s * (y - 0.5) + rng.laplace(0.0, 0.1 / np.sqrt(2.0), m)
    elif family == "rank_local":
        c = rng.random(m)
        ok = np.flatnonzero(y == 1)
        if ok.size and rng.random() < s:
            top = int(np.argmax(c))
            pick = int(rng.choice(ok))
            c[top], c[pick] = c[pick], c[top]
    elif family == "variance":
        sd = np.where(y == 1, 0.05, 0.05 + 0.30 * s)
        c = 0.5 + rng.normal(0.0, 1.0, m) * sd
    else:
        raise ValueError(family)
    return np.clip(c, 0.01, 0.99)


def pooled(pools, k, confs):
    stats = []
    for p, c in zip(pools, confs):
        y = (p.answers[:k] == p.correct).astype(int)
        st = item_discrimination(c, y)
        if st is not None:
            stats.append(st)
    pd = pooled_discrimination(stats)
    return (pd.d_hat, pd.se, pd.z) if pd else (0.0, 1.0, 0.0)


def vote_correct(pool, k, c, gamma):
    a = pool.answers[:k]
    w = np.ones(a.shape[0]) if gamma == 0.0 else np.exp(np.clip(gamma * vdw_scores(c), -50, 50))
    return int(np.argmax(np.bincount(a, weights=w, minlength=pool.n_answers))) == pool.correct


def run_cell(pools, test_idx, k, family, s, seed):
    rng = np.random.default_rng(seed)
    confs = [plant((p.answers[:k] == p.correct).astype(int), family, s, rng) for p in pools]
    d, se, z = pooled(pools, k, confs)

    tp = [pools[i] for i in test_idx]
    tc = [confs[i] for i in test_idx]
    sc = np.array([vote_correct(p, k, c, 0.0) for p, c in zip(tp, tc)])

    def acc(g):
        return float(np.mean([vote_correct(p, k, c, g) for p, c in zip(tp, tc)]))

    gate_open = abs(z) > NU_DEV
    g_derived = gamma_of(d, se, NU_DEV, GAMMA_MAX_DEV, 0.5)   # 0 inside the dead zone
    g_oracle = max(((float(g), acc(float(g))) for g in GAMMA_GRID), key=lambda t: t[1])

    # The label-free arm is asked the same question; on this substrate it never
    # reaches the channel, which the aggregate below makes explicit.
    lf = estimate_label_free([_swap_conf(p, c, k) for p, c in zip(pools, confs)], k, seed=seed)

    return {
        "d_true": d, "se": se, "z": z,
        "gate_open": bool(gate_open),
        "sign_correct": bool(gate_open and np.sign(d) == np.sign(g_derived) and g_derived != 0.0),
        "gamma_derived": g_derived,
        "acc_sc": float(sc.mean()),
        "acc_derived": acc(g_derived),
        "acc_oracle": g_oracle[1],
        "gamma_oracle": g_oracle[0],
        "lf_gamma": lf.gamma,
        "lf_alarms": [a for a, v in lf.alarms.items() if v],
    }


def _swap_conf(pool, c, k):
    """A shallow copy of the pool carrying the planted confidences."""
    import copy
    q = copy.copy(pool)
    conf = pool.confidences.copy()
    conf[:k] = c
    q.confidences = conf
    return q


def margin_diagnostics(k: int) -> dict:
    """Why E4 fires, per substrate: the quantile cut and what survives it.

    Finding (f) turns on the cut degenerating to 1.0 on the saturated pools,
    and the paper contrasts that against MATH L5 where it does not. Both
    numbers belong in an artifact rather than in prose only.
    """
    import collections
    out = {}

    def cut_of(answer_lists, budget):
        margins, ndist = [], []
        for ans in answer_lists:
            a = [str(x) for x in ans][:budget]
            cnt = collections.Counter(a)
            top = cnt.most_common(2)
            margins.append((top[0][1] - (top[1][1] if len(top) > 1 else 0)) / len(a))
            ndist.append(len(cnt))
        margins, ndist = np.array(margins), np.array(ndist)
        cut = float(np.quantile(margins, 0.40))
        return {"n_items": len(margins),
                "n_unanimous": int((margins == 1.0).sum()),
                "quantile_cut": cut,
                "n_two_or_more_answers": int((ndist >= 2).sum()),
                "n_gated": int(np.sum((margins >= cut) & (ndist >= 2)))}

    raw = json.loads((ROOT / "data/real_traces_full.json").read_text())
    out["gsm8k_csqa"] = cut_of([[t["answer"] for t in v] for v in raw.values()], 12)

    for label, fname, budget, split in (("math_l5_eval", "math_confirm_raw.json", 16, True),
                                        ("math_l5_budget_capped", "mathl5_budget_raw.json", 16, False)):
        tr = json.loads((ROOT / "results" / fname).read_text())["traces"]
        qids = list(tr)
        if split:   # reproduce the pre-registered 30-item sign set
            sign = set(np.array(qids)[np.random.default_rng(20260731)
                                      .permutation(len(qids))[:30]])
            qids = [q for q in qids if q not in sign]
        out[label] = cut_of([[t["answer"] for t in tr[q]] for q in qids], budget)
    return out


def main() -> None:
    ap = argparse.ArgumentParser()
    ap.add_argument("--traces", type=Path, default=ROOT / "data/real_traces_full.json")
    ap.add_argument("--items", type=Path, default=ROOT / "data/real_items.json")
    ap.add_argument("--k", type=int, default=12)
    ap.add_argument("--seeds", type=int, default=40)
    ap.add_argument("--out", type=Path, default=ROOT / "results/planted_sensitivity.json")
    args = ap.parse_args()

    pools, groups = load_pools(args.traces, args.items)
    seen = {"math": 0, "commonsense": 0}
    test_idx = []
    for i, g in enumerate(groups):
        if seen[g] < 20:
            seen[g] += 1
        else:
            test_idx.append(i)
    print(f"pools {len(pools)}  test {len(test_idx)}  K={args.k}  nu_dev={NU_DEV}  "
          f"seeds={args.seeds}\n")

    cells = {}
    for fam in FAMILIES:
        for s in LADDER:
            runs = [run_cell(pools, test_idx, args.k, fam, s, 1000 * FAMILIES.index(fam) + i)
                    for i in range(args.seeds)]
            gain_d = np.array([r["acc_derived"] - r["acc_sc"] for r in runs])
            gain_o = np.array([r["acc_oracle"] - r["acc_sc"] for r in runs])
            cells[f"{fam}@{s}"] = {
                "family": fam, "strength": s,
                "abs_d_true": float(np.mean([abs(r["d_true"]) for r in runs])),
                "abs_z": float(np.mean([abs(r["z"]) for r in runs])),
                "p_gate_open": float(np.mean([r["gate_open"] for r in runs])),
                "p_sign_correct": float(np.mean([r["sign_correct"] for r in runs])),
                "gain_derived": float(gain_d.mean()),
                "gain_oracle": float(gain_o.mean()),
                "capture": float(gain_d.mean() / gain_o.mean()) if gain_o.mean() > 1e-9 else None,
                "p_lf_acts": float(np.mean([r["lf_gamma"] != 0.0 for r in runs])),
                "lf_alarms": sorted({a for r in runs for a in r["lf_alarms"]}),
            }

    print(f"{'family':11s} {'s':>5s} {'|D|':>6s} {'|z|':>6s} {'P(open)':>8s} {'P(sign)':>8s} "
          f"{'gain':>7s} {'oracle':>7s} {'capture':>8s} {'LF acts':>8s}")
    for key, c in cells.items():
        cap = f"{c['capture']:.2f}" if c["capture"] is not None else "  --"
        print(f"{c['family']:11s} {c['strength']:5.2f} {c['abs_d_true']:6.3f} {c['abs_z']:6.2f} "
              f"{c['p_gate_open']*100:7.0f}% {c['p_sign_correct']*100:7.0f}% "
              f"{c['gain_derived']:+7.4f} {c['gain_oracle']:+7.4f} {cap:>8s} "
              f"{c['p_lf_acts']*100:7.0f}%")

    # minimum detectable |D| per family, by linear interpolation on the ladder
    mdd = {}
    for fam in FAMILIES:
        pts = sorted(((cells[f"{fam}@{s}"]["abs_d_true"], cells[f"{fam}@{s}"]["p_gate_open"])
                      for s in LADDER))
        for target in (0.5, 0.8):
            hit = next((d for d, p in pts if p >= target), None)
            mdd[f"{fam}@{int(target*100)}"] = hit
    print("\nminimum |D| at which the dev gate opens on this substrate:")
    for kk, v in mdd.items():
        print(f"   {kk:22s} {'not reached' if v is None else f'{v:.3f}'}")

    diag = margin_diagnostics(args.k)
    print("\nwhy E4 fires, per substrate (margin gate at the 40% quantile):")
    for name, r in diag.items():
        print(f"   {name:22s} unanimous {r['n_unanimous']:3d}/{r['n_items']:3d}  "
              f"cut {r['quantile_cut']:.3f}  gated {r['n_gated']:2d}")

    payload = {"config": {"k": args.k, "seeds": args.seeds, "ladder": LADDER,
                          "families": FAMILIES, "nu_dev": NU_DEV, "n_test": len(test_idx)},
               "cells": cells, "min_detectable_D": mdd,
               "margin_diagnostics": diag}
    args.out.write_text(json.dumps(payload, indent=1))
    print(f"\nwrote {args.out.relative_to(ROOT)}")


if __name__ == "__main__":
    main()
