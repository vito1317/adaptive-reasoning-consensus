#!/usr/bin/env python
"""Useful-regime boundary map (SPEC.md section 8.a, Limitation 2).

DDWC only has headroom when the similarity mass ``Sum_j S_ij`` actually varies
across traces. When the embedding geometry is diffuse, or the kernel hinges are
never crossed, the weights go uniform and the method degenerates to plain
Self-Consistency -- benign, but with exactly zero benefit.

This sweeps the two knobs that control that geometry (cluster separation and
within-cluster spread) plus the echo rate, and reports where the weights
collapse. A real dataset can then be located on the same axes by computing its
weight coefficient of variation, which is what tells you in advance whether the
method can possibly help there.

Usage::

    python experiments/run_boundary.py --items 150 --out results/boundary.json
"""

from __future__ import annotations

import argparse
import json
import sys
from pathlib import Path

import numpy as np

sys.path.insert(0, str(Path(__file__).resolve().parents[1] / "src"))

from rlev_voi import DEFAULT, ModeProbability  # noqa: E402
from rlev_voi.algorithm import run_rlev_voi  # noqa: E402
from rlev_voi.baselines import run_adaptive_consistency, run_self_consistency  # noqa: E402
from rlev_voi.kernel import build_kernel  # noqa: E402
from rlev_voi.simulate import Cluster, SimConfig, generate_dataset  # noqa: E402
from rlev_voi.weights import effective_weights, n_eff  # noqa: E402

MP = ModeProbability(n_mc=DEFAULT.n_mc, seed=0)

SHARED = [0.30, 0.45, 0.55, 0.65, 0.75, 0.85]
"""Question-level cosine baseline. Real CoT traces sit around 0.65-0.85."""
TIGHTNESS = [0.02, 0.06, 0.12, 0.20, 0.30]
"""Extra within-cluster cosine on top of the baseline."""
ECHO_RATES = [0.0, 0.2, 0.4, 0.6, 0.8]


def weight_stats(dataset, k_max: int) -> dict:
    cvs, ratios = [], []
    for pool in dataset[:100]:
        sub = pool.prefix(k_max)
        S = build_kernel(sub.sem, sub.dup, sub.answers, DEFAULT)
        w = effective_weights(S, DEFAULT)
        cvs.append(float(np.std(w) / max(np.mean(w), 1e-12)))
        ratios.append(n_eff(w) / w.size)
    return {"weight_cv": float(np.mean(cvs)), "n_eff_over_K": float(np.mean(ratios))}


def cell(shared: float, tightness: float, echo: float, items: int, k_max: int, seed: int) -> dict:
    """One point on the boundary map.

    Fixed structure: a diffuse correct cluster versus a tight (optionally
    echoing) wrong cluster -- the configuration where redundancy discounting
    could in principle help.
    """
    sim = SimConfig(
        clusters=(
            Cluster(answer=0, weight=0.42, tightness=0.02),
            Cluster(answer=1, weight=0.48, tightness=tightness, echo_prob=echo),
            Cluster(answer=2, weight=0.10, tightness=0.04),
        ),
        sem_shared=shared,
    )
    data = generate_dataset(sim, items, k_max, seed=seed)
    cfg = DEFAULT.with_(k_max=k_max, voi_branch=False, stop_variant="AGGRESSIVE")

    rlev = [run_rlev_voi(p, cfg, MP, use_conf=False) for p in data]
    asc = [run_adaptive_consistency(p, cfg, MP) for p in data]
    # Compare SC at the budget RLEV actually used, item by item.
    sc = [run_self_consistency(p, int(round(r.n_used)), cfg) for p, r in zip(data, rlev)]

    ws = weight_stats(data, k_max)
    acc_r = float(np.mean([r.correct for r in rlev]))
    acc_s = float(np.mean([r.correct for r in sc]))
    acc_a = float(np.mean([r.correct for r in asc]))
    return {
        "sem_shared": shared,
        "tightness": tightness,
        "echo_prob": echo,
        **ws,
        "acc_rlev": acc_r,
        "acc_sc_matched_n": acc_s,
        "acc_asc": acc_a,
        "gain_vs_sc": acc_r - acc_s,
        "guard_rate": float(np.mean([r.guard_fired for r in rlev])),
        "collapsed": bool(ws["weight_cv"] < 0.05),
    }


def main():
    ap = argparse.ArgumentParser()
    ap.add_argument("--items", type=int, default=150)
    ap.add_argument("--k-max", type=int, default=25)
    ap.add_argument("--seed", type=int, default=0)
    ap.add_argument("--out", type=Path, default=Path("results/boundary.json"))
    args = ap.parse_args()

    out: dict = {
        "config": vars(args) | {"out": str(args.out)},
        "note": (
            "Maps where inverse-similarity weighting has any headroom at all. "
            "'collapsed' cells are ones where the weights are effectively uniform, "
            "so RLEV-VoI is mathematically indistinguishable from Self-Consistency."
        ),
        "shared_x_tightness": [],
        "echo_sweep": [],
    }

    print("=== question-baseline x cluster-tightness (echo=0.4) ===")
    for shared in SHARED:
        for tight in TIGHTNESS:
            r = cell(shared, tight, 0.4, args.items, args.k_max, args.seed)
            out["shared_x_tightness"].append(r)
            print(
                f"  shared={shared:<5} tight={tight:<5} cv={r['weight_cv']:.3f} "
                f"n_eff/K={r['n_eff_over_K']:.3f} gain={r['gain_vs_sc']:+.3f} "
                f"{'COLLAPSED' if r['collapsed'] else ''}",
                flush=True,
            )

    print("\n=== echo rate (shared=0.65, tightness=0.30) ===")
    for echo in ECHO_RATES:
        r = cell(0.65, 0.30, echo, args.items, args.k_max, args.seed)
        out["echo_sweep"].append(r)
        print(
            f"  echo={echo:<4} cv={r['weight_cv']:.3f} gain={r['gain_vs_sc']:+.3f} "
            f"guard={r['guard_rate']:.2f}",
            flush=True,
        )

    args.out.parent.mkdir(parents=True, exist_ok=True)
    args.out.write_text(json.dumps(out, indent=2, default=float))
    print(f"\nWrote {args.out}")


if __name__ == "__main__":
    main()
