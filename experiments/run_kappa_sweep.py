#!/usr/bin/env python
"""The confidence-usage frontier: baseline behaviour along the kappa_c sweep.

This is the problem-statement experiment for the reliability-tempered
confidence study. It quantifies, before any new method exists, exactly how much
accuracy each existing confidence policy gains or loses as the true
confidence-correctness coupling ``kappa_c`` moves from strongly negative
(anti-correlated / poisoned) to strongly positive (informative):

* ``SC``           -- ignore confidence entirely (the floor everyone must beat).
* ``CISC(gamma)``  -- trust it unconditionally at a fixed exponent.
* ``ECE-gate``     -- the prior project's binary dev-set gate (all-or-nothing).
* ``AUC-gate``     -- same gate driven by dev-set *discrimination* + sign
  instead of calibration; still binary, but gates on the right quantity.
* ``oracle``       -- per-regime best (gamma, sign) chosen with TEST ground
  truth: the upper envelope no legitimate method can exceed.

The gap between the best binary gate and the oracle envelope is the room the
continuous tempering method has to claim; if that gap is negligible, the
follow-up method is dead on arrival and we say so.

Voting only, fixed K: confidence weighting concerns the consensus rule, so
adaptive stopping is deliberately out of scope here.

Usage::

    python experiments/run_kappa_sweep.py --items 400 --k 15 --out results/kappa_sweep.json
"""

from __future__ import annotations

import argparse
import json
import sys
from pathlib import Path

import numpy as np

sys.path.insert(0, str(Path(__file__).resolve().parents[1] / "src"))

from rlev_voi.evaluate import expected_calibration_error  # noqa: E402
from rlev_voi.simulate import Cluster, SimConfig, generate_dataset  # noqa: E402

KAPPAS = [-0.6, -0.4, -0.2, -0.1, 0.0, 0.1, 0.2, 0.4, 0.6]
GAMMAS = [0.5, 1.0, 2.0, 4.0]

#: Independent, diffuse clusters -- no echo, no similarity structure, so the
#: ONLY signal separating methods is how they use confidence.
BASE_CLUSTERS = (
    Cluster(answer=0, weight=0.45, tightness=0.02),
    Cluster(answer=1, weight=0.25, tightness=0.02),
    Cluster(answer=2, weight=0.18, tightness=0.02),
    Cluster(answer=3, weight=0.12, tightness=0.02),
)

ADVERSARIAL = {
    "monotone_compress": dict(kappa_c=0.6, conf_transform="compress"),
    "monotone_overconf": dict(kappa_c=0.6, conf_transform="overconfident"),
    "monotone_power": dict(kappa_c=0.6, conf_transform="power"),
    "heterogeneous_kappa": dict(kappa_c=0.0, kappa_c_sd=0.6),
}


def vote(pool, k: int, conf_fn) -> bool:
    """Weighted plurality over the first k traces; conf_fn maps c -> weight."""
    a = pool.answers[:k]
    w = conf_fn(pool.confidences[:k])
    tally = np.bincount(a, weights=w, minlength=pool.n_answers)
    return int(np.argmax(tally)) == pool.correct


def accuracy(dataset, k: int, conf_fn) -> float:
    return float(np.mean([vote(p, k, conf_fn) for p in dataset]))


def dev_stats(dev, k: int) -> dict:
    """Dev-split statistics available to any legitimate gate."""
    conf = np.concatenate([p.confidences[:k] for p in dev])
    hit = np.concatenate([(p.answers[:k] == p.correct).astype(float) for p in dev])
    ece = expected_calibration_error(conf, hit)
    # AUC via the rank-sum identity (label-efficient, threshold-free).
    order = np.argsort(conf)
    ranks = np.empty_like(order, dtype=float)
    ranks[order] = np.arange(1, conf.size + 1)
    n_pos, n_neg = float(hit.sum()), float((1 - hit).sum())
    auc = 0.5 if n_pos == 0 or n_neg == 0 else (ranks[hit == 1].sum() - n_pos * (n_pos + 1) / 2) / (n_pos * n_neg)
    return {"ece": float(ece), "auc": float(auc)}


def make_policies(dev, k: int) -> dict:
    """Every baseline policy as a name -> conf_fn map (oracle handled separately)."""
    stats = dev_stats(dev, k)
    policies: dict = {"SC": lambda c: np.ones_like(c)}
    for g in GAMMAS:
        policies[f"CISC(g={g})"] = lambda c, g=g: c**g
    # Prior project's gate: binary on calibration.
    if stats["ece"] <= 0.10:
        policies["ECE-gate"] = lambda c: c
    else:
        policies["ECE-gate"] = lambda c: np.ones_like(c)
    # Discrimination-driven binary gate with sign correction: trust when the
    # dev AUC is far from 0.5, flipping the signal when it is anti-correlated.
    auc = stats["auc"]
    if auc >= 0.55:
        policies["AUC-gate"] = lambda c: c
    elif auc <= 0.45:
        policies["AUC-gate"] = lambda c: 1.0 - c
    else:
        policies["AUC-gate"] = lambda c: np.ones_like(c)
    return policies, stats


def oracle_envelope(test, k: int) -> tuple[float, str]:
    """Best fixed (gamma, sign) on the TEST split -- the upper reference line."""
    best, label = -1.0, "SC"
    for g in [0.0] + GAMMAS:
        for name, fn in [
            (f"g={g}", lambda c, g=g: np.ones_like(c) if g == 0 else c**g),
            (f"g={g},flip", lambda c, g=g: np.ones_like(c) if g == 0 else (1.0 - c) ** g),
        ]:
            acc = accuracy(test, k, fn)
            if acc > best:
                best, label = acc, name
    return best, label


def run_cell(sim_kwargs: dict, items: int, k: int, k_max: int, seed: int) -> dict:
    cfg = SimConfig(clusters=BASE_CLUSTERS, **sim_kwargs)
    data = generate_dataset(cfg, items, k_max, seed=seed)
    n_dev = max(20, items // 5)
    dev, test = data[:n_dev], data[n_dev:]
    policies, stats = make_policies(dev, k)
    row = {"dev": stats}
    for name, fn in policies.items():
        row[name] = accuracy(test, k, fn)
    row["oracle"], row["oracle_choice"] = oracle_envelope(test, k)
    return row


def main():
    ap = argparse.ArgumentParser()
    ap.add_argument("--items", type=int, default=400)
    ap.add_argument("--k", type=int, default=15)
    ap.add_argument("--k-max", type=int, default=20)
    ap.add_argument("--seed", type=int, default=0)
    ap.add_argument("--out", type=Path, default=Path("results/kappa_sweep.json"))
    args = ap.parse_args()

    out = {"config": vars(args) | {"out": str(args.out)}, "sweep": [], "adversarial": {}}

    print(f"{'kappa':>6} {'SC':>6} {'CISC1':>6} {'ECEg':>6} {'AUCg':>6} {'oracle':>7}  (dev ece/auc)")
    for i, kap in enumerate(KAPPAS):
        row = run_cell(dict(kappa_c=kap), args.items, args.k, args.k_max, args.seed + i)
        row["kappa_c"] = kap
        out["sweep"].append(row)
        print(
            f"{kap:>6} {row['SC']:>6.3f} {row['CISC(g=1.0)']:>6.3f} {row['ECE-gate']:>6.3f} "
            f"{row['AUC-gate']:>6.3f} {row['oracle']:>7.3f}  "
            f"({row['dev']['ece']:.2f}/{row['dev']['auc']:.2f}) {row['oracle_choice']}",
            flush=True,
        )

    print("\nadversarial regimes:")
    for name, kw in ADVERSARIAL.items():
        row = run_cell(kw, args.items, args.k, args.k_max, args.seed + 100)
        out["adversarial"][name] = row
        print(
            f"  {name:22s} SC={row['SC']:.3f} CISC1={row['CISC(g=1.0)']:.3f} "
            f"ECEg={row['ECE-gate']:.3f} AUCg={row['AUC-gate']:.3f} oracle={row['oracle']:.3f} "
            f"(dev ece={row['dev']['ece']:.2f} auc={row['dev']['auc']:.2f})",
            flush=True,
        )

    args.out.parent.mkdir(parents=True, exist_ok=True)
    args.out.write_text(json.dumps(out, indent=2, default=float))
    print(f"\nWrote {args.out}")


if __name__ == "__main__":
    main()
