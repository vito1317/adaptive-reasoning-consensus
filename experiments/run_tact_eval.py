#!/usr/bin/env python
"""TACT vs the confidence-policy baselines (SPEC-TACT sections 7-8).

Cells: the kappa_c sweep (dev n=200), a small-dev replica (n=50), and the
adversarial regimes (three monotone distortions, heterogeneous kappa,
confident echo). Fixed voting budget K; all methods replay identical pools.

Falsifiers evaluated automatically:
  F1  TACT-dev below the best fixed-gamma CISC at kappa=+0.6
  F2  TACT below SC anywhere on the sweep (per variant; LF conditional on alarms)
  F3  TACT-LF fails to beat the binary ECE gate averaged over the sweep
  F4  CISC-devT or the sign-corrected dev grid matches TACT-dev everywhere
      (incl. distortion / heterogeneous / small-dev cells)

TACT-LF estimates from a SEPARATE unlabeled traffic split (never the labeled
dev, never the eval items), mirroring the online protocol without
self-reference.

Usage::

    python experiments/run_tact_eval.py --items 400 --k 15 --out results/tact_eval.json
"""

from __future__ import annotations

import argparse
import json
import sys
from pathlib import Path

import numpy as np

sys.path.insert(0, str(Path(__file__).resolve().parents[1] / "src"))

from rlev_voi.evaluate import expected_calibration_error, mcnemar  # noqa: E402
from rlev_voi.simulate import Cluster, SimConfig, generate_dataset  # noqa: E402
from rlev_voi.tact import estimate_dev, estimate_label_free, estimate_semi_lf, tact_vote  # noqa: E402
from rlev_voi.tempering import NU_LF, TemperConfig  # noqa: E402

KAPPAS = [-0.6, -0.4, -0.2, -0.1, 0.0, 0.1, 0.2, 0.4, 0.6]
CISC_GAMMAS = [0.25, 0.5, 1.0, 2.0, 4.0]
SIGN_GRID = [-4.0, -2.0, -1.0, -0.5, 0.0, 0.5, 1.0, 2.0, 4.0]

BASE_CLUSTERS = (
    Cluster(answer=0, weight=0.45, tightness=0.02),
    Cluster(answer=1, weight=0.25, tightness=0.02),
    Cluster(answer=2, weight=0.18, tightness=0.02),
    Cluster(answer=3, weight=0.12, tightness=0.02),
)

ADVERSARIAL: dict[str, dict] = {
    "monotone_compress": dict(kappa_c=0.6, conf_transform="compress"),
    "monotone_overconf": dict(kappa_c=0.6, conf_transform="overconfident"),
    "monotone_power": dict(kappa_c=0.6, conf_transform="power"),
    "heterogeneous_kappa": dict(kappa_c=0.0, kappa_c_sd=0.6),
}

ECHO_CFG = SimConfig(
    clusters=(
        Cluster(answer=0, weight=0.40, tightness=0.02),
        Cluster(answer=1, weight=0.60, tightness=0.30, echo_prob=0.85),
    ),
    n_answers=3,
    kappa_c=0.6,
    echo_conf=0.95,
)


# ---------------------------------------------------------------- policies
def cisc_weight(gamma: float):
    if gamma == 0.0:
        return lambda c: np.ones_like(c)
    if gamma > 0:
        return lambda c: c**gamma
    return lambda c: (1.0 - c) ** (-gamma)  # sign-flipped trust


def plain_vote(pool, k: int, conf_fn) -> bool:
    a = pool.answers[:k]
    w = conf_fn(pool.confidences[:k])
    return int(np.argmax(np.bincount(a, weights=w, minlength=pool.n_answers))) == pool.correct


def tact_correct(pool, k: int, gamma: float) -> bool:
    return tact_vote(pool.answers[:k], pool.confidences[:k], pool.n_answers, gamma) == pool.correct


def dev_grid_pick(dev, k: int, grid: list[float]) -> float:
    """Pick the (signed) fixed exponent maximizing dev voting accuracy."""
    best_g, best_acc = 0.0, -1.0
    for g in grid:
        acc = float(np.mean([plain_vote(p, k, cisc_weight(g)) for p in dev]))
        if acc > best_acc + 1e-12:
            best_g, best_acc = g, acc
    return best_g


def ece_gate_policy(dev, k: int):
    conf = np.concatenate([p.confidences[:k] for p in dev])
    hit = np.concatenate([(p.answers[:k] == p.correct).astype(float) for p in dev])
    ece = expected_calibration_error(conf, hit)
    return (lambda c: c) if ece <= 0.10 else (lambda c: np.ones_like(c))


def evaluate_cell(sim_kwargs_or_cfg, items, k, k_max, seed, n_dev, n_traffic=200) -> dict:
    if isinstance(sim_kwargs_or_cfg, SimConfig):
        cfg = sim_kwargs_or_cfg
    else:
        cfg = SimConfig(clusters=BASE_CLUSTERS, **sim_kwargs_or_cfg)
    data = generate_dataset(cfg, items + n_dev + n_traffic, k_max, seed=seed)
    dev, traffic, test = data[:n_dev], data[n_dev : n_dev + n_traffic], data[n_dev + n_traffic :]

    # --- estimates -------------------------------------------------------
    tact_dev = estimate_dev(dev, k)
    tact_lf = estimate_label_free(traffic, k)
    tact_semi = estimate_semi_lf(dev[: min(50, n_dev)], traffic, k)
    g_devT = dev_grid_pick(dev, k, [0.0] + CISC_GAMMAS)  # published CISC-devT (positive only)
    g_sign = dev_grid_pick(dev, k, SIGN_GRID)  # strongest trivial dev baseline
    ece_fn = ece_gate_policy(dev, k)

    # --- correctness vectors (paired) --------------------------------------
    res: dict[str, np.ndarray] = {}
    res["SC"] = np.array([plain_vote(p, k, lambda c: np.ones_like(c)) for p in test])
    for g in CISC_GAMMAS:
        res[f"CISC(g={g})"] = np.array([plain_vote(p, k, cisc_weight(g)) for p in test])
    res["ECE-gate"] = np.array([plain_vote(p, k, ece_fn) for p in test])
    res["CISC-devT"] = np.array([plain_vote(p, k, cisc_weight(g_devT)) for p in test])
    res["SignGrid-dev"] = np.array([plain_vote(p, k, cisc_weight(g_sign)) for p in test])
    res["TACT-dev"] = np.array([tact_correct(p, k, tact_dev.gamma) for p in test])
    res["TACT-LF"] = np.array([tact_correct(p, k, tact_lf.gamma) for p in test])
    res["TACT-semi"] = np.array([tact_correct(p, k, tact_semi.gamma) for p in test])

    # oracle over the sign grid on TEST (upper envelope)
    oracle_acc, oracle_g = -1.0, 0.0
    for g in SIGN_GRID:
        acc = float(np.mean([plain_vote(p, k, cisc_weight(g)) for p in test]))
        if acc > oracle_acc:
            oracle_acc, oracle_g = acc, g

    out = {
        "acc": {m: float(v.mean()) for m, v in res.items()},
        "oracle": {"acc": oracle_acc, "gamma": oracle_g},
        "gamma": {
            "TACT-dev": tact_dev.gamma,
            "TACT-LF": tact_lf.gamma,
            "TACT-semi": tact_semi.gamma,
            "CISC-devT": g_devT,
            "SignGrid-dev": g_sign,
        },
        "tact_dev_diag": tact_dev.diagnostics,
        "tact_lf_diag": {"alarms": tact_lf.alarms, **{k_: v for k_, v in tact_lf.diagnostics.items() if isinstance(v, (int, float))}},
        "paired": {
            "TACT-dev_vs_SignGrid": mcnemar(res["TACT-dev"], res["SignGrid-dev"]),
            "TACT-dev_vs_CISC-devT": mcnemar(res["TACT-dev"], res["CISC-devT"]),
            "TACT-dev_vs_SC": mcnemar(res["TACT-dev"], res["SC"]),
            "TACT-LF_vs_SC": mcnemar(res["TACT-LF"], res["SC"]),
            "TACT-LF_vs_ECE-gate": mcnemar(res["TACT-LF"], res["ECE-gate"]),
        },
    }
    return out


def main():
    ap = argparse.ArgumentParser()
    ap.add_argument("--items", type=int, default=400)
    ap.add_argument("--k", type=int, default=15)
    ap.add_argument("--k-max", type=int, default=20)
    ap.add_argument("--seed", type=int, default=0)
    ap.add_argument("--out", type=Path, default=Path("results/tact_eval.json"))
    args = ap.parse_args()

    out = {"config": vars(args) | {"out": str(args.out)}, "sweep_dev200": [], "sweep_dev50": [], "adversarial": {}}

    hdr = f"{'cell':>22} {'SC':>6} {'ECEg':>6} {'devT':>6} {'signG':>6} {'T-dev':>6} {'T-LF':>6} {'T-semi':>7} {'oracle':>7}  gammas(dev/LF/semi)"
    print(hdr)

    def show(name, r):
        a = r["acc"]
        g = r["gamma"]
        print(
            f"{name:>22} {a['SC']:>6.3f} {a['ECE-gate']:>6.3f} {a['CISC-devT']:>6.3f} "
            f"{a['SignGrid-dev']:>6.3f} {a['TACT-dev']:>6.3f} {a['TACT-LF']:>6.3f} {a['TACT-semi']:>7.3f} "
            f"{r['oracle']['acc']:>7.3f}  ({g['TACT-dev']:+.2f}/{g['TACT-LF']:+.2f}/{g['TACT-semi']:+.2f})",
            flush=True,
        )

    for i, kap in enumerate(KAPPAS):
        r = evaluate_cell(dict(kappa_c=kap), args.items, args.k, args.k_max, args.seed + i, n_dev=200)
        r["kappa_c"] = kap
        out["sweep_dev200"].append(r)
        show(f"kappa={kap}", r)

    print()
    for i, kap in enumerate([-0.6, -0.2, 0.2, 0.6]):
        r = evaluate_cell(dict(kappa_c=kap), args.items, args.k, args.k_max, args.seed + 50 + i, n_dev=50)
        r["kappa_c"] = kap
        out["sweep_dev50"].append(r)
        show(f"dev50 kappa={kap}", r)

    print()
    for name, kw in ADVERSARIAL.items():
        r = evaluate_cell(kw, args.items, args.k, args.k_max, args.seed + 100, n_dev=200)
        out["adversarial"][name] = r
        show(name, r)
    r = evaluate_cell(ECHO_CFG, args.items, args.k, args.k_max, args.seed + 200, n_dev=200)
    out["adversarial"]["confident_echo"] = r
    show("confident_echo", r)

    # ------------------------- falsifier verdicts -------------------------
    sweep = out["sweep_dev200"]
    best_cisc_at_06 = max(v for k_, v in sweep[-1]["acc"].items() if k_.startswith("CISC(g="))
    f1 = sweep[-1]["acc"]["TACT-dev"] < best_cisc_at_06 - 0.02
    f2_dev = any(r["acc"]["TACT-dev"] < r["acc"]["SC"] - 0.02 for r in sweep)
    f2_lf = any(r["acc"]["TACT-LF"] < r["acc"]["SC"] - 0.02 for r in sweep)
    f3 = np.mean([r["acc"]["TACT-LF"] for r in sweep]) <= np.mean([r["acc"]["ECE-gate"] for r in sweep])
    hard_cells = out["sweep_dev50"] + list(out["adversarial"].values())
    f4_devT = all(r["acc"]["CISC-devT"] >= r["acc"]["TACT-dev"] - 0.02 for r in sweep + hard_cells)
    f4_sign = all(r["acc"]["SignGrid-dev"] >= r["acc"]["TACT-dev"] - 0.02 for r in sweep + hard_cells)
    out["falsifiers"] = {
        "F1_below_cisc_at_high_kappa": bool(f1),
        "F2_below_SC_dev": bool(f2_dev),
        "F2_below_SC_lf": bool(f2_lf),
        "F3_lf_not_beating_ece_gate": bool(f3),
        "F4_matched_by_CISC-devT": bool(f4_devT),
        "F4_matched_by_SignGrid": bool(f4_sign),
    }
    print("\nfalsifiers:", json.dumps(out["falsifiers"], indent=2))

    args.out.parent.mkdir(parents=True, exist_ok=True)
    args.out.write_text(json.dumps(out, indent=2, default=float))
    print(f"\nWrote {args.out}")


if __name__ == "__main__":
    main()
