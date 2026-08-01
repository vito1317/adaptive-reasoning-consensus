#!/usr/bin/env python
"""Seed dispersion for the synthetic cells (review finding 7).

Every synthetic number in the paper came from a single seed, which leaves the
mid-range comparisons unsupported: a 0.012 gap on 400 paired items is five
items, and without dispersion there is no way to tell it from noise. This
re-runs the sweep and the adversarial cells across seeds and reports, per
cell, the mean and standard deviation of each method plus a paired bootstrap
on the TACT-minus-SignGrid difference.

The paired structure is preserved within a seed: all methods see the same
pools, so the difference is measured on the same items and the seed-to-seed
variation is what the paper was missing.

    python experiments/run_seed_dispersion.py --seeds 10
"""

from __future__ import annotations

import argparse
import importlib.util
import json
from pathlib import Path

import numpy as np

_spec = importlib.util.spec_from_file_location(
    "tact_eval", Path(__file__).resolve().parent / "run_tact_eval.py")
TE = importlib.util.module_from_spec(_spec)
_spec.loader.exec_module(TE)

METHODS = ["SC", "TACT-dev", "TACT-LF", "SignGrid-dev", "CISC-devT", "ECE-gate"]


def main():
    ap = argparse.ArgumentParser()
    ap.add_argument("--seeds", type=int, default=10)
    ap.add_argument("--items", type=int, default=400)
    ap.add_argument("--k", type=int, default=15)
    ap.add_argument("--k-max", type=int, default=20)
    ap.add_argument("--out", type=Path, default=Path("results/seed_dispersion.json"))
    args = ap.parse_args()

    kappas = [-0.6, -0.4, -0.2, -0.1, 0.0, 0.1, 0.2, 0.4, 0.6]
    cells: dict[str, dict[str, list[float]]] = {}
    gammas: dict[str, list[float]] = {}

    def record(name, r):
        c = cells.setdefault(name, {m: [] for m in METHODS})
        for m in METHODS:
            if m in r["acc"]:
                c[m].append(r["acc"][m])
        if "TACT-dev" in r.get("gamma", {}):
            gammas.setdefault(name, []).append(r["gamma"]["TACT-dev"])

    for s in range(args.seeds):
        base = 1000 * (s + 1)
        for i, kap in enumerate(kappas):
            record(f"kappa={kap:+.1f}", TE.evaluate_cell(
                dict(kappa_c=kap), args.items, args.k, args.k_max, base + i, n_dev=200))
        for nm, kw in TE.ADVERSARIAL.items():
            record(nm, TE.evaluate_cell(kw, args.items, args.k, args.k_max, base + 100, n_dev=200))
        record("confident_echo", TE.evaluate_cell(
            TE.ECHO_CFG, args.items, args.k, args.k_max, base + 200, n_dev=200))
        print(f"  seed batch {s+1}/{args.seeds} done", flush=True)

    print(f"\n{'cell':14s} " + " ".join(f"{m:>16s}" for m in ("SC", "TACT-dev", "SignGrid-dev")))
    out = {}
    rng = np.random.default_rng(0)
    for name, c in cells.items():
        row = {m: dict(mean=float(np.mean(v)), sd=float(np.std(v, ddof=1)) if len(v) > 1 else 0.0,
                       n=len(v)) for m, v in c.items() if v}
        d = np.array(c["TACT-dev"]) - np.array(c["SignGrid-dev"])
        boot = [rng.choice(d, len(d), replace=True).mean() for _ in range(10000)]
        row["TACT_minus_SignGrid"] = dict(
            mean=float(d.mean()), sd=float(d.std(ddof=1)) if len(d) > 1 else 0.0,
            ci=[float(np.percentile(boot, 2.5)), float(np.percentile(boot, 97.5))],
            p_two_sided=float(2 * min((np.array(boot) > 0).mean(), (np.array(boot) < 0).mean())))
        if name in gammas:
            row["gamma_TACT_dev"] = dict(mean=float(np.mean(gammas[name])),
                                         sd=float(np.std(gammas[name], ddof=1)))
        out[name] = row
        f = lambda m: f"{row[m]['mean']:.3f}+-{row[m]['sd']:.3f}"
        print(f"{name:14s} {f('SC'):>16s} {f('TACT-dev'):>16s} {f('SignGrid-dev'):>16s}")

    print(f"\n{'cell':14s} {'TACT - SignGrid':>18s} {'CI95':>22s} {'p':>7s}")
    for name, row in out.items():
        d = row["TACT_minus_SignGrid"]
        print(f"{name:14s} {d['mean']:>+18.4f} "
              f"{'['+format(d['ci'][0],'+.4f')+', '+format(d['ci'][1],'+.4f')+']':>22s} {d['p_two_sided']:>7.3f}")

    args.out.write_text(json.dumps(dict(seeds=args.seeds, items=args.items, cells=out), indent=1))
    print(f"\nwrote {args.out}")


if __name__ == "__main__":
    main()
