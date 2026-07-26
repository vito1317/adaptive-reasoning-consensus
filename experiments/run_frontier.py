#!/usr/bin/env python
"""Matched-budget accuracy-vs-cost frontiers across regimes R1-R5.

.. warning::
   Synthetic data. Per SPEC.md section 8.a this establishes **implementation
   correctness, no-regret behaviour, ablation attribution and the useful-regime
   boundary** -- it does NOT establish that RLEV-VoI helps on real LLM traces,
   because the generator produces exactly the block-cluster structure the DDWC
   weighting assumes. R2/R4 gains are mechanism checks, not evidence.

Sweep design
------------
Each stopping mechanism is swept on *its own* parameter so the frontiers are
real curves rather than a single collapsed point:

* stability frontier -- ``voi_branch=False``, sweep ``tau`` (this doubles as the
  "plain patience threshold" comparator required by ablation (g));
* VoI frontier -- ``tau=0.999``, ``tau_floor=0.0`` so the stability branch and
  the floor are both out of the way, sweep ``lambda`` on a log grid.

Comparing those two frontiers is ablation (g): if they coincide, the VoI
machinery adds nothing over a plain threshold and is reported as a negative
result.

Usage::

    python experiments/run_frontier.py --items 400 --out results/frontier.json
    python experiments/run_frontier.py --quick
"""

from __future__ import annotations

import argparse
import json
import sys
import time
from pathlib import Path

import numpy as np

sys.path.insert(0, str(Path(__file__).resolve().parents[1] / "src"))

from rlev_voi import DEFAULT, ModeProbability  # noqa: E402
from rlev_voi.algorithm import run_rlev_voi  # noqa: E402
from rlev_voi.baselines import (  # noqa: E402
    run_adaptive_consistency,
    run_cisc,
    run_dedup_sc,
    run_esc,
    run_rasc_lite,
    run_self_consistency,
    run_sprt,
)
from rlev_voi.evaluate import (  # noqa: E402
    achievable_oracle,
    confidence_gate_passes,
    evaluate,
    holm_correct,
    interpolate_accuracy,
    mcnemar,
    paired_diff_ci,
    pareto_frontier,
)
from rlev_voi.simulate import REGIMES, generate_dataset  # noqa: E402

TAU_SWEEP = [0.50, 0.65, 0.75, 0.85, 0.90, 0.95, 0.98, 0.995]
LAMBDA_SWEEP = [1e-8, 3e-8, 1e-7, 3e-7, 1e-6, 3e-6, 1e-5, 3e-5, 1e-4, 1e-3]
K_SWEEP = [1, 3, 5, 7, 9, 12, 15, 20, 25, 30, 35, 40]
WINDOW_SWEEP = [2, 3, 4, 5, 6, 8]
MARGIN_SWEEP = [2, 3, 4, 5, 6, 8, 10]

MP = ModeProbability(n_mc=DEFAULT.n_mc, seed=0)


def build_configs(k_max: int, quick: bool, use_conf: bool):
    """Every (method, label, factory). Each adaptive method gets its own sweep."""
    taus = TAU_SWEEP[::2] if quick else TAU_SWEEP
    lams = LAMBDA_SWEEP[::2] if quick else LAMBDA_SWEEP
    ks = [k for k in (K_SWEEP[::2] if quick else K_SWEEP) if k <= k_max]
    windows = WINDOW_SWEEP[::2] if quick else WINDOW_SWEEP
    margins = MARGIN_SWEEP[::2] if quick else MARGIN_SWEEP
    base = DEFAULT.with_(k_max=k_max)
    out = []

    # ---- fixed-budget baselines -----------------------------------------
    for k in ks:
        out.append(("SC", f"K={k}", lambda p, k=k: run_self_consistency(p, k, base)))
        out.append(("CISC", f"K={k}", lambda p, k=k: run_cisc(p, k, base)))
        out.append(("dedup-SC", f"K={k}", lambda p, k=k: run_dedup_sc(p, k, base)))

    # ---- adaptive baselines ---------------------------------------------
    for tau in taus:
        cfg = base.with_(tau=tau)
        out.append(("ASC", f"tau={tau}", lambda p, c=cfg: run_adaptive_consistency(p, c, MP)))
        out.append(("RASC-lite", f"tau={tau}", lambda p, c=cfg: run_rasc_lite(p, c, MP)))
    for w in windows:
        out.append(("ESC", f"w={w}", lambda p, w=w: run_esc(p, base, window=w)))
    for m in margins:
        out.append(("SPRT", f"margin={m}", lambda p, m=m: run_sprt(p, base, margin=m)))

    # ---- RLEV-VoI: stability frontier (VoI off) -------------------------
    for tau in taus:
        safe = base.with_(tau=tau, voi_branch=False, stop_variant="SAFE")
        aggr = base.with_(tau=tau, voi_branch=False, stop_variant="AGGRESSIVE")
        out.append(
            ("RLEV-SAFE", f"tau={tau}", lambda p, c=safe: run_rlev_voi(p, c, MP, use_conf=use_conf))
        )
        out.append(
            ("RLEV-AGGR", f"tau={tau}", lambda p, c=aggr: run_rlev_voi(p, c, MP, use_conf=use_conf))
        )
        # Ablation (h) 2x2 cells:
        #   SC-consensus x eff-stop, and DDWC-consensus x raw(ASC)-stop.
        h_sc = base.with_(tau=tau, voi_branch=False, stop_variant="AGGRESSIVE", disable_guard=True)
        h_raw = base.with_(tau=tau, voi_branch=False, stop_on_raw=True)
        out.append(
            ("abl-h_SCcons_effstop", f"tau={tau}", lambda p, c=h_sc: run_rlev_voi(p, c, MP, use_conf=use_conf))
        )
        out.append(
            ("abl-h_DDWCcons_rawstop", f"tau={tau}", lambda p, c=h_raw: run_rlev_voi(p, c, MP, use_conf=use_conf))
        )
        # Ablation (e): GLOBAL semantic-only kernel -- predicted to backfire.
        g = base.with_(tau=tau, voi_branch=False, stop_variant="AGGRESSIVE", kernel_scope="GLOBAL")
        out.append(
            ("abl-e_GLOBAL", f"tau={tau}", lambda p, c=g: run_rlev_voi(p, c, MP, use_conf=use_conf))
        )
        # Ablation (b'): what the ECE confidence gate costs. ECE measures
        # calibration, not discriminativeness -- a signal can be highly
        # informative yet systematically under/over-confident, and the gate
        # would discard it. This variant forces the channel on regardless.
        out.append(
            ("abl-b_forceconf", f"tau={tau}", lambda p, c=aggr: run_rlev_voi(p, c, MP, use_conf=True))
        )

    # ---- RLEV-VoI: VoI frontier (stability + floor disabled) ------------
    for lam in lams:
        cfg = base.with_(tau=0.999, tau_floor=0.0, lam=lam, voi_branch=True, stop_variant="AGGRESSIVE")
        out.append(
            ("RLEV-VoI", f"lam={lam:g}", lambda p, c=cfg: run_rlev_voi(p, c, MP, use_conf=use_conf))
        )

    # ---- the frozen default config, exactly as specified ----------------
    frozen = base.with_(stop_variant="SAFE")
    out.append(("FROZEN-DEFAULT", "spec-6", lambda p, c=frozen: run_rlev_voi(p, c, MP, use_conf=use_conf)))
    return out


def voi_scale_diagnostic(dataset, k_max: int, use_conf: bool) -> dict:
    """Record the actual distribution of VoI-per-token.

    The spec's default ``lambda = 1e-3`` is compared against these values to show
    whether the VoI branch is a real criterion or fires unconditionally.
    """
    cfg = DEFAULT.with_(k_max=k_max, tau=0.999, tau_floor=0.0, lam=0.0, voi_branch=True)
    vals: list[float] = []
    for pool in dataset[:60]:
        r = run_rlev_voi(pool, cfg, MP, use_conf=use_conf)
        vals.extend(r.diagnostics.get("voi_trace", []))
    if not vals:
        return {}
    v = np.asarray(vals, dtype=float)
    return {
        "n_samples": int(v.size),
        "median": float(np.median(v)),
        "p90": float(np.percentile(v, 90)),
        "max": float(v.max()),
        "frac_below_default_lambda_1e-3": float(np.mean(v < 1e-3)),
    }


def kernel_diagnostic(dataset, k_max: int) -> dict:
    """Weight-collapse diagnostic -- where the method lives on the useful-regime map.

    When ``Sum_j S_ij`` is near-constant across traces the weights go uniform and
    DDWC degenerates to Self-Consistency (benign, but zero headroom). The
    coefficient of variation of ``w`` and the realised ``n_eff / K`` say how much
    redundancy structure the kernel actually sees.
    """
    from rlev_voi.kernel import build_kernel
    from rlev_voi.weights import effective_weights, n_eff

    cvs, ratios, dup_max, sem_mean = [], [], [], []
    for pool in dataset[:120]:
        sub = pool.prefix(k_max)
        S = build_kernel(sub.sem, sub.dup, sub.answers, DEFAULT)
        w = effective_weights(S, DEFAULT)
        cvs.append(float(np.std(w) / max(np.mean(w), 1e-12)))
        ratios.append(n_eff(w) / w.size)
        off = ~np.eye(sub.dup.shape[0], dtype=bool)
        dup_max.append(float(sub.dup[off].max()))
        sem_mean.append(float(sub.sem[off].mean()))
    return {
        "weight_cv_mean": float(np.mean(cvs)),
        "n_eff_over_K_mean": float(np.mean(ratios)),
        "frac_items_with_verbatim_dup": float(np.mean([d > DEFAULT.theta_dup for d in dup_max])),
        "mean_offdiag_sem": float(np.mean(sem_mean)),
        "collapsed_to_SC": bool(np.mean(cvs) < 0.05),
    }


def analyse_regime(name: str, dataset, k_max: int, quick: bool) -> dict:
    # Confidence gate on a dev split -- the posterior never uses confidence,
    # only the consensus channel is affected.
    dev = dataset[: max(1, len(dataset) // 5)]
    use_conf, ece = confidence_gate_passes(dev, DEFAULT.conf_gate_ece)
    print(f"  confidence gate: ECE={ece:.3f} -> use_conf={use_conf}", flush=True)

    points = []
    for method, label, fn in build_configs(k_max, quick, use_conf):
        t0 = time.time()
        pt = evaluate(method, label, fn, dataset)
        points.append(pt)
        print(
            f"  {method:24s} {label:12s} acc={pt.accuracy:.3f} "
            f"cost={pt.cost:8.1f} n={pt.mean_n:5.2f}  ({time.time()-t0:.1f}s)",
            flush=True,
        )

    by_method: dict[str, list] = {}
    for p in points:
        by_method.setdefault(p.method, []).append(p)
    frontiers = {m: pareto_frontier(ps) for m, ps in by_method.items()}

    sc_points = sorted(by_method["SC"], key=lambda p: p.cost)
    checks: dict = {}
    pvals: dict[str, float] = {}

    # --- no-regret: worst gap vs SC interpolated to the SAME total cost ---
    for method in sorted(by_method):
        if method == "SC":
            continue
        worst = None
        for p in by_method[method]:
            sc_acc = interpolate_accuracy(sc_points, p.cost)
            if sc_acc is None:
                continue
            gap = p.accuracy - sc_acc
            if worst is None or gap < worst["gap"]:
                worst = {
                    "gap": gap,
                    "label": p.label,
                    "cost": p.cost,
                    "sc_accuracy": sc_acc,
                    "accuracy": p.accuracy,
                }
        if worst:
            checks.setdefault("worst_gap_vs_SC", {})[method] = worst

    # --- frontier dominance at shared budgets -----------------------------
    def frontier_compare(a: str, b: str) -> dict | None:
        if a not in frontiers or b not in frontiers:
            return None
        fa, fb = frontiers[a], frontiers[b]
        lo = max(min(p.cost for p in fa), min(p.cost for p in fb))
        hi = min(max(p.cost for p in fa), max(p.cost for p in fb))
        if hi <= lo:
            return None
        grid = np.linspace(lo, hi, 40)
        diffs = []
        for c in grid:
            xa, xb = interpolate_accuracy(fa, c), interpolate_accuracy(fb, c)
            if xa is not None and xb is not None:
                diffs.append(xa - xb)
        if not diffs:
            return None
        d = np.asarray(diffs)
        return {
            "shared_cost_range": [float(lo), float(hi)],
            "mean_acc_diff": float(d.mean()),
            "min_acc_diff": float(d.min()),
            "max_acc_diff": float(d.max()),
            "dominates": bool(d.min() >= -1e-9),
        }

    for a, b in [
        ("RLEV-AGGR", "ASC"),
        ("RLEV-SAFE", "ASC"),
        ("RLEV-AGGR", "RASC-lite"),
        ("RLEV-AGGR", "dedup-SC"),
        ("RLEV-AGGR", "SC"),
        ("RLEV-VoI", "RLEV-AGGR"),  # ablation (g): VoI vs plain patience
        ("RLEV-AGGR", "abl-h_SCcons_effstop"),  # consensus contribution
        ("RLEV-AGGR", "abl-h_DDWCcons_rawstop"),  # stopping contribution
        ("RLEV-AGGR", "abl-e_GLOBAL"),  # kernel scope
        ("abl-b_forceconf", "RLEV-AGGR"),  # what the ECE gate costs
        ("RASC-lite", "RLEV-AGGR"),  # does the simple competitor already win?
    ]:
        cmp = frontier_compare(a, b)
        if cmp:
            checks.setdefault("frontier_vs", {})[f"{a}_vs_{b}"] = cmp

    # --- frozen default, paired tests ------------------------------------
    frozen = next((p for p in by_method.get("FROZEN-DEFAULT", [])), None)
    if frozen is not None:
        nearest_sc = min(sc_points, key=lambda p: abs(p.cost - frozen.cost))
        d, lo_, hi_ = paired_diff_ci(frozen.correct, nearest_sc.correct)
        mc = mcnemar(frozen.correct, nearest_sc.correct)
        pvals["FROZEN_vs_SC"] = mc["p_value"]
        entry = {
            "accuracy": frozen.accuracy,
            "cost": frozen.cost,
            "mean_n": frozen.mean_n,
            "guard_fired_rate": frozen.extra["guard_fired_rate"],
            "stopped_by": frozen.extra["stopped_by"],
            "vs_SC": {
                "sc_label": nearest_sc.label,
                "sc_accuracy": nearest_sc.accuracy,
                "sc_cost": nearest_sc.cost,
                "paired_diff": d,
                "ci95": [lo_, hi_],
                "mcnemar": mc,
            },
        }
        for other in ("ASC", "RASC-lite", "dedup-SC"):
            cand = by_method.get(other, [])
            if not cand:
                continue
            op = min(cand, key=lambda p: abs(p.cost - frozen.cost))
            m2 = mcnemar(frozen.correct, op.correct)
            pvals[f"FROZEN_vs_{other}"] = m2["p_value"]
            d2, l2, h2 = paired_diff_ci(frozen.correct, op.correct)
            entry[f"vs_{other}"] = {
                "label": op.label,
                "accuracy": op.accuracy,
                "cost": op.cost,
                "paired_diff": d2,
                "ci95": [l2, h2],
                "mcnemar": m2,
            }
        checks["frozen_default"] = entry

    oracle_k, oracle_acc = achievable_oracle(dataset, k_max)

    return {
        "regime": name,
        "confidence_gate": {"ece": ece, "use_conf": use_conf},
        "kernel_diagnostic": kernel_diagnostic(dataset, k_max),
        "voi_scale": voi_scale_diagnostic(dataset, k_max, use_conf),
        "points": [
            {
                "method": p.method,
                "label": p.label,
                "accuracy": p.accuracy,
                "cost": p.cost,
                "mean_n": p.mean_n,
                "guard_fired_rate": p.extra["guard_fired_rate"],
                "stopped_by": p.extra["stopped_by"],
            }
            for p in points
        ],
        "frontiers": {m: [(p.cost, p.accuracy, p.label) for p in fr] for m, fr in frontiers.items()},
        "checks": checks,
        "holm": holm_correct(pvals) if pvals else {},
        "achievable_oracle": {"mean_k": oracle_k, "accuracy_at_k_max": oracle_acc},
    }


def main():
    ap = argparse.ArgumentParser()
    ap.add_argument("--items", type=int, default=400)
    ap.add_argument("--k-max", type=int, default=40)
    ap.add_argument("--seed", type=int, default=0)
    ap.add_argument("--quick", action="store_true")
    ap.add_argument("--out", type=Path, default=Path("results/frontier.json"))
    args = ap.parse_args()

    if args.quick:
        args.items = min(args.items, 80)
        args.k_max = min(args.k_max, 20)

    out: dict = {
        "config": {
            "items": args.items,
            "k_max": args.k_max,
            "seed": args.seed,
            "quick": args.quick,
            "frozen_defaults": dict(DEFAULT.__dict__),
        },
        "caveat": (
            "SYNTHETIC DATA. Establishes implementation correctness, no-regret behaviour, "
            "ablation attribution and the useful-regime boundary only. The generator produces "
            "the block-cluster structure DDWC assumes, so R2/R4 gains are NOT evidence of "
            "benefit on real LLM traces."
        ),
        "regimes": {},
    }

    for i, (name, sim_cfg) in enumerate(REGIMES.items()):
        print(f"\n=== {name} ===", flush=True)
        dataset = generate_dataset(sim_cfg, args.items, args.k_max, seed=args.seed + 1000 * i)
        out["regimes"][name] = analyse_regime(name, dataset, args.k_max, args.quick)

    args.out.parent.mkdir(parents=True, exist_ok=True)
    args.out.write_text(json.dumps(out, indent=2, default=float))
    print(f"\nWrote {args.out}")


if __name__ == "__main__":
    main()
