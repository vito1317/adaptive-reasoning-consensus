#!/usr/bin/env python
"""TACT-group on structured heterogeneity + the item-level impossibility check.

Two cells:

* ``grouped``  -- kappa indexed by an OBSERVABLE covariate (three domains at
  +0.6 / 0 / -0.6). Exploitable: per-group TACT should approach the per-group
  oracle and crack the SC floor that every global policy is stuck on.
* ``iid``      -- kappa i.i.d. per item, no covariate. Information-
  theoretically closed to label-free per-item adaptation (winner's-curse sign
  opposition + two-world unidentifiability); every legitimate method should
  sit at the floor, and the naive self-referential per-item method should
  collapse to plurality reinforcement.

Usage::

    python experiments/run_group_eval.py --items 600 --out results/group_eval.json
"""

from __future__ import annotations

import argparse
import json
import sys
from pathlib import Path

import numpy as np

sys.path.insert(0, str(Path(__file__).resolve().parents[1] / "src"))

from rlev_voi.discrimination import item_discrimination  # noqa: E402
from rlev_voi.evaluate import mcnemar  # noqa: E402
from rlev_voi.simulate import Cluster, SimConfig, generate_dataset  # noqa: E402
from rlev_voi.tact import (  # noqa: E402
    estimate_dev,
    estimate_dev_by_group,
    estimate_lf_by_group,
    group_vote,
    sc_answer,
    tact_vote,
)
from rlev_voi.tempering import discriminant_link  # noqa: E402

BASE = (
    Cluster(answer=0, weight=0.45, tightness=0.02),
    Cluster(answer=1, weight=0.25, tightness=0.02),
    Cluster(answer=2, weight=0.18, tightness=0.02),
    Cluster(answer=3, weight=0.12, tightness=0.02),
)


def per_item_link_oracle(pool, k: int) -> bool:
    """gamma_q = link(true per-item D) -- the ceiling for per-item adaptation."""
    y = (pool.answers[:k] == pool.correct).astype(int)
    s = item_discrimination(pool.confidences[:k], y)
    g = float(np.clip(discriminant_link(np.clip(s.d, -0.99, 0.99), 0.5), -4, 4)) if s else 0.0
    return tact_vote(pool.answers[:k], pool.confidences[:k], pool.n_answers, g) == pool.correct


def naive_self_referential(pool, k: int) -> bool:
    """The provably-useless per-item method (negative control)."""
    a, c = pool.answers[:k], pool.confidences[:k]
    plur = sc_answer(a, pool.n_answers)
    s = item_discrimination(c, (a == plur).astype(int))
    d = s.d if s is not None else 0.0
    g = float(np.clip(discriminant_link(np.clip(d, -0.99, 0.99), 0.5), -4, 4))
    return tact_vote(a, c, pool.n_answers, g) == pool.correct


def run_cell(cfg: SimConfig, items: int, k: int, k_max: int, seed: int, grouped: bool) -> dict:
    dev = generate_dataset(cfg, items, k_max, seed=seed)
    test = generate_dataset(cfg, items, k_max, seed=seed + 7777)

    res: dict[str, np.ndarray] = {}
    res["SC"] = np.array([sc_answer(p.answers[:k], p.n_answers) == p.correct for p in test])
    g_global = estimate_dev(dev, k)
    res["TACT-global-dev"] = np.array(
        [tact_vote(p.answers[:k], p.confidences[:k], p.n_answers, g_global.gamma) == p.correct for p in test]
    )
    gammas_dev, _ = estimate_dev_by_group(dev, k)
    res["TACT-group-dev"] = np.array([group_vote(p, k, gammas_dev, g_global.gamma) == p.correct for p in test])
    gammas_lf, lf_global = estimate_lf_by_group(test, k)  # label-free: uses unlabeled traffic
    res["TACT-group-LF"] = np.array([group_vote(p, k, gammas_lf, lf_global.gamma) == p.correct for p in test])
    res["naive-per-item"] = np.array([naive_self_referential(p, k) for p in test])
    res["per-item-link-oracle"] = np.array([per_item_link_oracle(p, k) for p in test])

    out = {
        "acc": {m: float(v.mean()) for m, v in res.items()},
        "gammas_dev_by_group": gammas_dev if grouped else None,
        "gammas_lf_by_group": gammas_lf if grouped else None,
        "gamma_global": g_global.gamma,
        "paired": {
            "group-dev_vs_SC": mcnemar(res["TACT-group-dev"], res["SC"]),
            "group-dev_vs_global": mcnemar(res["TACT-group-dev"], res["TACT-global-dev"]),
            "group-LF_vs_SC": mcnemar(res["TACT-group-LF"], res["SC"]),
            "naive_vs_SC": mcnemar(res["naive-per-item"], res["SC"]),
        },
    }
    return out


def main():
    ap = argparse.ArgumentParser()
    ap.add_argument("--items", type=int, default=600)
    ap.add_argument("--k", type=int, default=15)
    ap.add_argument("--k-max", type=int, default=20)
    ap.add_argument("--seed", type=int, default=0)
    ap.add_argument("--out", type=Path, default=Path("results/group_eval.json"))
    args = ap.parse_args()

    cells = {
        "grouped": (SimConfig(clusters=BASE, group_kappas=(0.6, 0.0, -0.6)), True),
        "iid": (SimConfig(clusters=BASE, kappa_c=0.0, kappa_c_sd=0.6), False),
    }
    out = {"config": vars(args) | {"out": str(args.out)}, "cells": {}}
    for name, (cfg, grouped) in cells.items():
        r = run_cell(cfg, args.items, args.k, args.k_max, args.seed, grouped)
        out["cells"][name] = r
        print(f"\n=== {name} ===")
        for m, a in r["acc"].items():
            print(f"  {m:22s} {a:.3f}")
        if grouped:
            print(f"  per-group gammas (dev): { {g: round(v,2) for g,v in r['gammas_dev_by_group'].items()} }")
            print(f"  per-group gammas (LF):  { {g: round(v,2) for g,v in r['gammas_lf_by_group'].items()} }")
        for k_, v in r["paired"].items():
            print(f"  {k_:24s} p={v['p_value']:.2e}  (+{v['a_only']}/-{v['b_only']})")

    args.out.parent.mkdir(parents=True, exist_ok=True)
    args.out.write_text(json.dumps(out, indent=2, default=float))
    print(f"\nWrote {args.out}")


if __name__ == "__main__":
    main()
