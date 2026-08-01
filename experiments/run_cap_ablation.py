#!/usr/bin/env python
"""Is the exponent cap load-bearing in the grouped cell? (review finding 11)

The paper attributed a difference between the two arms in the covariate-
structured cell to their different caps (4 for dev, 2 for label-free) and
deferred the check. This runs it: sweep the cap for both arms over several
seeds and report accuracy as a function of it, so the attribution is either
supported or dropped.

    python experiments/run_cap_ablation.py --seeds 5
"""

from __future__ import annotations

import argparse
import importlib.util
import json
from pathlib import Path

import numpy as np

_spec = importlib.util.spec_from_file_location(
    "group_eval", Path(__file__).resolve().parent / "run_group_eval.py")
GE = importlib.util.module_from_spec(_spec)
_spec.loader.exec_module(GE)

import sys  # noqa: E402

sys.path.insert(0, str(Path(__file__).resolve().parents[1] / "src"))

from rlev_voi.simulate import SimConfig, generate_dataset  # noqa: E402
from rlev_voi.tact import (  # noqa: E402
    estimate_dev_by_group,
    estimate_label_free,
    estimate_lf_by_group,
    group_vote,
    sc_answer,
    tact_vote,
)
from rlev_voi.tempering import NU_DEV, NU_LF  # noqa: E402

CAPS = [1.0, 2.0, 3.0, 4.0, 6.0, 8.0]


def one_seed(seed: int, items: int, k: int, k_max: int, n_dev: int):
    cfg = SimConfig(clusters=GE.BASE, group_kappas=(0.6, 0.0, -0.6))
    data = generate_dataset(cfg, items + n_dev, k_max, seed=seed)
    dev, test = data[:n_dev], data[n_dev:]
    sc = float(np.mean([sc_answer(p.answers[:k], p.n_answers) == p.correct for p in test]))
    row = {"SC": sc, "dev": {}, "lf": {}}
    from rlev_voi.tempering import TemperConfig
    for cap in CAPS:
        gmap, _ = estimate_dev_by_group(
            dev, k, cfg=TemperConfig(nu=NU_DEV, gamma_max=cap, p_bar=None))
        row["dev"][cap] = float(np.mean(
            [group_vote(p, k, gmap, 0.0) == p.correct for p in test]))

        # the paper's comparison is per-group dev vs per-GROUP label-free, not
        # the global label-free arm
        gmap_lf, lf_glob = estimate_lf_by_group(test, k, gamma_max=cap)
        row["lf"][cap] = float(np.mean(
            [group_vote(p, k, gmap_lf, lf_glob.gamma) == p.correct for p in test]))
    return row


def main():
    ap = argparse.ArgumentParser()
    ap.add_argument("--seeds", type=int, default=5)
    ap.add_argument("--items", type=int, default=600)
    ap.add_argument("--k", type=int, default=15)
    ap.add_argument("--k-max", type=int, default=20)
    ap.add_argument("--n-dev", type=int, default=200)
    ap.add_argument("--out", type=Path, default=Path("results/cap_ablation.json"))
    args = ap.parse_args()

    rows = [one_seed(4000 + s, args.items, args.k, args.k_max, args.n_dev)
            for s in range(args.seeds)]
    sc = np.mean([r["SC"] for r in rows])
    print(f"grouped cell, {args.seeds} seeds, SC floor {sc:.3f}\n")
    print(f"{'cap':>6} {'per-group dev':>18} {'per-group label-free':>22}")
    out = {"seeds": args.seeds, "sc": float(sc), "caps": {}}
    for cap in CAPS:
        d = np.array([r["dev"][cap] for r in rows])
        l = np.array([r["lf"][cap] for r in rows])
        out["caps"][cap] = dict(dev_mean=float(d.mean()), dev_sd=float(d.std(ddof=1)),
                                lf_mean=float(l.mean()), lf_sd=float(l.std(ddof=1)))
        print(f"{cap:>6.1f} {d.mean():>11.3f}+-{d.std(ddof=1):.3f} {l.mean():>13.3f}+-{l.std(ddof=1):.3f}")

    devs = np.array([out["caps"][c]["dev_mean"] for c in CAPS])
    lfs = np.array([out["caps"][c]["lf_mean"] for c in CAPS])
    print(f"\nspread across caps: per-group dev {devs.max()-devs.min():.4f}, "
          f"label-free {lfs.max()-lfs.min():.4f}")
    verdict = ("the cap is load-bearing" if max(devs.max() - devs.min(), lfs.max() - lfs.min()) > 0.02
               else "the cap is NOT load-bearing in this cell; the arms differ for another reason")
    out["verdict"] = verdict
    print(f"VERDICT: {verdict}")
    args.out.write_text(json.dumps(out, indent=1))
    print(f"wrote {args.out}")


if __name__ == "__main__":
    main()
