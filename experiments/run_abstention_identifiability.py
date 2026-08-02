#!/usr/bin/env python
"""Is the abstention doing work, or was there simply nothing to find?

On every real-trace campaign TACT returned gamma = 0 and was bit-identical to
SC. A constant rule that never acts produces exactly the same output, so that
observation on its own is evidence for neither of:

  H_safe  the gate is discriminative -- it declines on an uninformative
          channel and would act, correctly, on an informative one;
  H_null  there was no signal to find, so abstaining is trivially right and
          the mechanism is untested.

Validating a detector only on negatives measures specificity and leaves
sensitivity unknown. These three measurements attack the gap from the side
that cached traces can actually reach. All replay data/real_traces_full.json;
no new sampling.

  A  Stability   Bootstrap the items and ask how often the gate opens at all.
                 A decision that flips on resampling is not a reading of the
                 evidence, whichever way it fell.
  B  Specificity Permute confidences within items. This preserves the real
                 marginal confidences, tie structure, pool composition and
                 item difficulty and destroys only the confidence-correctness
                 coupling, so the false-open rate should match nu's nominal
                 level. Stronger than the synthetic D=0 cell, which is drawn
                 from the estimator's own working model.
  C  Cost        Override the gate and vote anyway, and compute the
                 gold-label oracle ceiling. Abstention is only "correct" if
                 an oracle could not have gained either.

What each outcome means is printed with the numbers, because the reading rule
is the point: none of the three is decisive alone.

    python experiments/run_abstention_identifiability.py
"""

from __future__ import annotations

import argparse
import json
import sys
from pathlib import Path

import numpy as np
from scipy.stats import binomtest

ROOT = Path(__file__).resolve().parents[1]
sys.path.insert(0, str(ROOT / "src"))

from rlev_voi.backends import Trace, build_pool  # noqa: E402
from rlev_voi.discrimination import item_discrimination, pooled_discrimination, vdw_scores  # noqa: E402
from rlev_voi.formula import gamma_of  # noqa: E402
from rlev_voi.tempering import GAMMA_MAX_DEV, NU_DEV, NU_LF  # noqa: E402

N_BOOT = 4000
N_PERM = 4000


def load_pools(traces: Path, items: Path, k: int):
    """Rebuild the campaign's pools exactly as run_real_eval.py does."""
    meta = {it["qid"]: it for it in json.loads(items.read_text())}
    raw = json.loads(traces.read_text())
    pools, groups = [], []
    for qid, trs in raw.items():
        if len(trs) < 6:
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
        p = build_pool(tl, meta[qid]["gold"])
        pools.append(p)
        groups.append(meta[qid]["group"])
    return pools, groups


def pooled_z(pools, k, confs=None):
    """(D_hat, SE, z) over a list of pools; ``confs`` overrides the confidences."""
    stats = []
    for i, p in enumerate(pools):
        c = p.confidences[:k] if confs is None else confs[i]
        y = (p.answers[:k] == p.correct).astype(int)
        s = item_discrimination(c, y)
        if s is not None:
            stats.append(s)
    pd = pooled_discrimination(stats)
    return (pd.d_hat, pd.se, pd.z, len(stats)) if pd else (0.0, 1.0, 0.0, 0)


def vote_correct(pool, k, gamma):
    """The shipped vote at exponent ``gamma``; gamma == 0 is the SC routine."""
    a = pool.answers[:k]
    if gamma == 0.0:
        w = np.ones(a.shape[0])
    else:
        w = np.exp(np.clip(gamma * vdw_scores(pool.confidences[:k]), -50.0, 50.0))
    return int(np.argmax(np.bincount(a, weights=w, minlength=pool.n_answers))) == pool.correct


def measure_A(pools, groups, k, rng):
    """Stability of the gate decision under resampling of items."""
    out = {}
    cells = [("pooled", pools), ("math", [p for p, g in zip(pools, groups) if g == "math"]),
             ("commonsense", [p for p, g in zip(pools, groups) if g != "math"])]
    for name, sel in cells:
        d, se, z, n = pooled_z(sel, k)
        zs = np.empty(N_BOOT)
        for b in range(N_BOOT):
            idx = rng.integers(0, len(sel), len(sel))
            zs[b] = pooled_z([sel[i] for i in idx], k)[2]
        out[name] = {
            "n_items": len(sel), "n_informative": n,
            "d_hat": d, "se": se, "z": z,
            "gap_to_nu_dev": NU_DEV - abs(z),
            "gap_to_nu_dev_pct": (NU_DEV - abs(z)) / NU_DEV * 100.0,
            "boot_open_rate_dev": float((np.abs(zs) > NU_DEV).mean()),
            "boot_open_rate_lf": float((np.abs(zs) > NU_LF).mean()),
            "boot_open_negative_dev": float((zs < -NU_DEV).mean()),
        }
    return out


def measure_B(pools, k, rng):
    """False-open rate under a within-item permutation null on the real traces."""
    zs = np.empty(N_PERM)
    for b in range(N_PERM):
        confs = [rng.permutation(p.confidences[:k]) for p in pools]
        zs[b] = pooled_z(pools, k, confs)[2]
    _, _, z_obs, _ = pooled_z(pools, k)
    return {
        "null_z_mean": float(zs.mean()), "null_z_sd": float(zs.std()),
        "false_open_dev": float((np.abs(zs) > NU_DEV).mean()),
        "nominal_dev": float(2 * (1 - 0.8997)),          # 2*(1-Phi(nu_dev))
        "false_open_lf": float((np.abs(zs) > NU_LF).mean()),
        "nominal_lf": float(2 * (1 - 0.98999)),          # 2*(1-Phi(nu_lf))
        "p_obs_under_null": float((np.abs(zs) >= abs(z_obs)).mean()),
        "z_obs": z_obs,
    }


def measure_C(pools, groups, k):
    """What the abstention forfeited, and what an oracle could have taken."""
    # The campaign estimates on all pools and scores on the 60-item test split.
    dev_n = {"math": 0, "commonsense": 0}
    test = []
    for p, g in zip(pools, groups):
        if dev_n[g] < 20:
            dev_n[g] += 1
        else:
            test.append(p)
    d, se, z, _ = pooled_z(pools, k)
    sc = np.array([vote_correct(p, k, 0.0) for p in test])

    def paired(gamma):
        v = np.array([vote_correct(p, k, gamma) for p in test])
        plus = int(np.sum(v & ~sc))
        minus = int(np.sum(sc & ~v))
        pv = binomtest(plus, plus + minus, 0.5).pvalue if plus + minus else 1.0
        return {"gamma": gamma, "acc": float(v.mean()), "plus": plus, "minus": minus, "p": float(pv)}

    derived = gamma_of(d, se, 0.0, GAMMA_MAX_DEV, 0.5)      # ignore the gate entirely
    grid = np.arange(-4.0, 4.001, 0.25)
    accs = [(float(g), float(np.mean([vote_correct(p, k, float(g)) for p in test]))) for g in grid]
    g_best, a_best = max(accs, key=lambda t: t[1])
    return {
        "n_test": len(test),
        "sc_acc": float(sc.mean()),
        "shipped": {"gamma": 0.0, "acc": float(sc.mean()), "plus": 0, "minus": 0, "p": 1.0},
        "forced_derived": paired(derived),
        "forced_wrong_sign": paired(-derived),
        "gold_oracle": {"gamma": g_best, "acc": a_best, "gain_over_sc": a_best - float(sc.mean())},
    }


def main() -> None:
    ap = argparse.ArgumentParser()
    ap.add_argument("--traces", type=Path, default=ROOT / "data/real_traces_full.json")
    ap.add_argument("--items", type=Path, default=ROOT / "data/real_items.json")
    ap.add_argument("--k", type=int, default=12)
    ap.add_argument("--seed", type=int, default=0)
    ap.add_argument("--out", type=Path, default=ROOT / "results/abstention_identifiability.json")
    args = ap.parse_args()

    pools, groups = load_pools(args.traces, args.items, args.k)
    rng = np.random.default_rng(args.seed)
    print(f"pools {len(pools)}  K={args.k}  nu_dev={NU_DEV}  nu_lf={NU_LF}\n")

    A = measure_A(pools, groups, args.k, rng)
    print("A. Is the abstention a stable decision?")
    for name, r in A.items():
        print(f"   {name:12s} z={r['z']:+.3f}  gap to nu_dev {r['gap_to_nu_dev']:+.4f} "
              f"({r['gap_to_nu_dev_pct']:+.1f}%)  gate opens in "
              f"{r['boot_open_rate_dev']*100:5.1f}% of resamples (dev), "
              f"{r['boot_open_rate_lf']*100:4.1f}% (LF)")
    print("   reading: a rate near 50% means the observed abstention was a coin flip, not a\n"
          "   reading of the evidence. It does not by itself favour H_safe or H_null.\n")

    B = measure_B(pools, args.k, rng)
    print("B. Does the gate stay shut when the coupling is destroyed? (real-data null)")
    print(f"   null z ~ mean {B['null_z_mean']:+.3f}, sd {B['null_z_sd']:.3f}  (should be ~N(0,1))")
    print(f"   false-open dev {B['false_open_dev']*100:5.2f}% vs nominal {B['nominal_dev']*100:.0f}%")
    print(f"   false-open LF  {B['false_open_lf']*100:5.2f}% vs nominal {B['nominal_lf']*100:.0f}%")
    print("   reading: at or below nominal is the strongest evidence for H_safe available on\n"
          "   real data -- the gate's null behaviour is correct on the real substrate, not\n"
          "   merely on the generator the estimator was derived from. Above nominal would\n"
          "   mean the dead zone is not protecting anything.\n")

    C = measure_C(pools, groups, args.k)
    print("C. What did abstaining forfeit?")
    print(f"   SC / shipped TACT        acc {C['sc_acc']:.3f}   (+0/-0 by construction)")
    for key, lab in (("forced_derived", "forced, derived gamma"), ("forced_wrong_sign", "forced, sign flipped")):
        r = C[key]
        print(f"   {lab:24s} acc {r['acc']:.3f}  gamma {r['gamma']:+.3f}  "
              f"+{r['plus']}/-{r['minus']}  p={r['p']:.3f}")
    o = C["gold_oracle"]
    print(f"   gold-label oracle        acc {o['acc']:.3f}  gamma {o['gamma']:+.2f}  "
          f"ceiling over SC {o['gain_over_sc']:+.4f}")
    print("   reading: forcing hurts -> abstention protective (H_safe). Neutral -> vacuous\n"
          "   (H_null). Helps -> over-conservative, a third case the paper does not consider.\n"
          "   An oracle ceiling near zero means H_null holds for this substrate whatever the\n"
          "   gate did, and the sign the estimator derived can still be checked against the\n"
          "   sign the oracle wanted.\n")

    payload = {"config": {"k": args.k, "seed": args.seed, "n_boot": N_BOOT, "n_perm": N_PERM,
                          "nu_dev": NU_DEV, "nu_lf": NU_LF},
               "A_stability": A, "B_permutation_null": B, "C_counterfactual": C}
    args.out.write_text(json.dumps(payload, indent=1))
    print(f"wrote {args.out.relative_to(ROOT)}")


if __name__ == "__main__":
    main()
