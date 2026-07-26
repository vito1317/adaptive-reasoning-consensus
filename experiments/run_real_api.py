#!/usr/bin/env python
"""Headline experiment on real LLM traces (SPEC.md section 8.b).

This is the only experiment that can establish whether RLEV-VoI actually helps.
It requires an API key; the synthetic experiments deliberately cannot substitute
for it.

Pre-registered primary endpoint: logprob-derived confidence where available,
temperature 0.7, ``rho_over = 1x``, embedding cost included, SAFE variant for the
accuracy claim and AGGRESSIVE for the token-savings claim, frozen default config
reported on every cell, Holm-corrected across the grid.

Reported up front, before any win is claimed (the Claim-2 test):

* the empirical ``dup_ij`` distribution -- if near-verbatim echo is absent, the
  duplication kernel is inert on real data and the paper says so;
* the guard-firing rate -- if it is ~0, RLEV-VoI is operationally SC there;
* the weight coefficient of variation -- if the weights are uniform, the method
  is mathematically indistinguishable from SC.

Usage::

    export ANTHROPIC_API_KEY=...
    python experiments/run_real_api.py --data data/gsm8k_sample.jsonl \
        --k-max 40 --items 100 --out results/real_api.json

The data file is JSONL with ``{"question": ..., "answer": ...}`` per line. With
no ``--data`` a small built-in demo set is used so the pipeline can be verified
end to end cheaply.
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
from rlev_voi.backends import (  # noqa: E402
    AnthropicBackend,
    OpenAIBackend,
    build_pool,
    cached_sample,
)
from rlev_voi.baselines import (  # noqa: E402
    run_adaptive_consistency,
    run_cisc,
    run_dedup_sc,
    run_rasc_lite,
    run_self_consistency,
)
from rlev_voi.evaluate import (  # noqa: E402
    confidence_gate_passes,
    evaluate,
    holm_correct,
    interpolate_accuracy,
    mcnemar,
    paired_diff_ci,
    pareto_frontier,
)
from rlev_voi.kernel import build_kernel  # noqa: E402
from rlev_voi.weights import effective_weights, n_eff  # noqa: E402

DEMO_ITEMS = [
    {"question": "A shop sells pens at $3 each. Ann buys 7 pens and pays with a $50 note. How much change does she get?", "answer": "29"},
    {"question": "A train travels 60 km in 45 minutes. At the same speed, how many km does it travel in 2 hours?", "answer": "160"},
    {"question": "If 5 machines make 5 widgets in 5 minutes, how many minutes do 100 machines need to make 100 widgets?", "answer": "5"},
    {"question": "A rectangle has perimeter 36 and its length is twice its width. What is its area?", "answer": "72"},
    {"question": "Sam had some marbles, gave away 1/3, then found 12 more and now has 44. How many did he start with?", "answer": "48"},
]

TAU_SWEEP = [0.50, 0.75, 0.85, 0.90, 0.95, 0.98]
K_SWEEP = [1, 3, 5, 9, 15, 20, 30, 40]

MP = ModeProbability(n_mc=DEFAULT.n_mc, seed=0)


def load_items(path: Path | None, limit: int) -> list[dict]:
    if path is None:
        return DEMO_ITEMS[:limit]
    items = [json.loads(l) for l in path.read_text().splitlines() if l.strip()]
    return items[:limit]


def sample_pools(items, backend, k_max, temperature, cache_dir) -> list:
    pools = []
    for i, it in enumerate(items):
        traces = cached_sample(backend, it["question"], k_max, temperature, cache_dir, str(i))
        pool = build_pool(traces, str(it["answer"]))
        if pool.correct < 0:
            print(f"  item {i}: gold answer never produced; kept (counts as all-wrong)")
        pools.append(pool)
        print(f"  item {i}: {len(traces)} traces, {pool.n_answers} distinct answers", flush=True)
    return pools


def mechanism_report(pools, k_max: int) -> dict:
    """The Claim-2 evidence, reported before any accuracy claim."""
    dups, cvs, ratios, verbatim = [], [], [], []
    for p in pools:
        sub = p.prefix(k_max)
        off = ~np.eye(sub.dup.shape[0], dtype=bool)
        if off.any():
            dups.append(sub.dup[off])
            verbatim.append(float(np.mean(sub.dup[off] > DEFAULT.theta_dup)))
        S = build_kernel(sub.sem, sub.dup, sub.answers, DEFAULT)
        w = effective_weights(S, DEFAULT)
        cvs.append(float(np.std(w) / max(np.mean(w), 1e-12)))
        ratios.append(n_eff(w) / w.size)
    d = np.concatenate(dups) if dups else np.array([0.0])
    rep = {
        "dup_percentiles": {
            str(q): float(np.percentile(d, q)) for q in (50, 75, 90, 95, 99, 100)
        },
        "frac_pairs_above_theta_dup": float(np.mean(d > DEFAULT.theta_dup)),
        "mean_frac_verbatim_pairs_per_item": float(np.mean(verbatim)) if verbatim else 0.0,
        "weight_cv_mean": float(np.mean(cvs)),
        "n_eff_over_K_mean": float(np.mean(ratios)),
    }
    rep["verdict"] = (
        "DUP CHANNEL INERT: near-verbatim echo is essentially absent, so the duplication "
        "kernel and the guard cannot contribute on this data."
        if rep["frac_pairs_above_theta_dup"] < 1e-3
        else "Near-verbatim echo present; duplication channel is active."
    )
    if rep["weight_cv_mean"] < 0.05:
        rep["verdict"] += " WEIGHTS COLLAPSED: DDWC is indistinguishable from SC here."
    return rep


def main():
    ap = argparse.ArgumentParser()
    ap.add_argument("--data", type=Path, default=None)
    ap.add_argument("--items", type=int, default=100)
    ap.add_argument("--k-max", type=int, default=40)
    ap.add_argument("--temperature", type=float, default=0.7)
    ap.add_argument("--provider", choices=["anthropic", "openai"], default="anthropic")
    ap.add_argument("--model", default=None)
    ap.add_argument("--cache", type=Path, default=Path("results/trace_cache"))
    ap.add_argument("--out", type=Path, default=Path("results/real_api.json"))
    args = ap.parse_args()

    if args.provider == "anthropic":
        backend = AnthropicBackend(**({"model": args.model} if args.model else {}))
    else:
        backend = OpenAIBackend(**({"model": args.model} if args.model else {}))

    items = load_items(args.data, args.items)
    print(f"Sampling {len(items)} items x {args.k_max} traces @ T={args.temperature}")
    pools = sample_pools(items, backend, args.k_max, args.temperature, args.cache)

    mech = mechanism_report(pools, args.k_max)
    print("\n=== mechanism report (Claim-2 test, reported before any win) ===")
    print(json.dumps(mech, indent=2))

    dev = pools[: max(1, len(pools) // 5)]
    use_conf, ece = confidence_gate_passes(dev, DEFAULT.conf_gate_ece)
    print(f"\nconfidence gate: ECE={ece:.3f} -> use_conf={use_conf}")

    base = DEFAULT.with_(k_max=args.k_max)
    configs = []
    for k in [k for k in K_SWEEP if k <= args.k_max]:
        configs += [
            ("SC", f"K={k}", lambda p, k=k: run_self_consistency(p, k, base)),
            ("CISC", f"K={k}", lambda p, k=k: run_cisc(p, k, base)),
            ("dedup-SC", f"K={k}", lambda p, k=k: run_dedup_sc(p, k, base)),
        ]
    for tau in TAU_SWEEP:
        c = base.with_(tau=tau)
        configs += [
            ("ASC", f"tau={tau}", lambda p, c=c: run_adaptive_consistency(p, c, MP)),
            ("RASC-lite", f"tau={tau}", lambda p, c=c: run_rasc_lite(p, c, MP)),
            (
                "RLEV-SAFE",
                f"tau={tau}",
                lambda p, c=c.with_(voi_branch=False, stop_variant="SAFE"): run_rlev_voi(
                    p, c, MP, use_conf=use_conf
                ),
            ),
            (
                "RLEV-AGGR",
                f"tau={tau}",
                lambda p, c=c.with_(voi_branch=False, stop_variant="AGGRESSIVE"): run_rlev_voi(
                    p, c, MP, use_conf=use_conf
                ),
            ),
        ]
    configs.append(
        ("FROZEN-DEFAULT", "spec-6", lambda p: run_rlev_voi(p, base, MP, use_conf=use_conf))
    )

    print("\n=== frontier ===")
    points = []
    for method, label, fn in configs:
        pt = evaluate(method, label, fn, pools)
        points.append(pt)
        print(f"  {method:16s} {label:10s} acc={pt.accuracy:.3f} cost={pt.cost:9.1f} n={pt.mean_n:5.2f}")

    by_method: dict[str, list] = {}
    for p in points:
        by_method.setdefault(p.method, []).append(p)
    frontiers = {m: pareto_frontier(ps) for m, ps in by_method.items()}
    sc_pts = sorted(by_method["SC"], key=lambda p: p.cost)

    pvals, checks = {}, {}
    frozen = next(iter(by_method.get("FROZEN-DEFAULT", [])), None)
    if frozen:
        for other in ("SC", "ASC", "RASC-lite", "dedup-SC"):
            cand = by_method.get(other, [])
            if not cand:
                continue
            op = min(cand, key=lambda p: abs(p.cost - frozen.cost))
            mc = mcnemar(frozen.correct, op.correct)
            pvals[f"FROZEN_vs_{other}"] = mc["p_value"]
            d, lo, hi = paired_diff_ci(frozen.correct, op.correct)
            checks[f"frozen_vs_{other}"] = {
                "other_label": op.label,
                "other_accuracy": op.accuracy,
                "other_cost": op.cost,
                "paired_diff": d,
                "ci95": [lo, hi],
                "mcnemar": mc,
            }
        checks["frozen"] = {
            "accuracy": frozen.accuracy,
            "cost": frozen.cost,
            "mean_n": frozen.mean_n,
            "guard_fired_rate": frozen.extra["guard_fired_rate"],
        }
        worst = min(
            (
                p.accuracy - (interpolate_accuracy(sc_pts, p.cost) or p.accuracy)
                for p in by_method.get("RLEV-SAFE", [])
            ),
            default=0.0,
        )
        checks["worst_gap_vs_SC"] = float(worst)

    out = {
        "config": {
            "items": len(items),
            "k_max": args.k_max,
            "temperature": args.temperature,
            "provider": args.provider,
            "model": args.model,
            "frozen_defaults": dict(DEFAULT.__dict__),
        },
        "mechanism_report": mech,
        "confidence_gate": {"ece": ece, "use_conf": use_conf},
        "points": [
            {"method": p.method, "label": p.label, "accuracy": p.accuracy, "cost": p.cost, "mean_n": p.mean_n}
            for p in points
        ],
        "frontiers": {m: [(p.cost, p.accuracy, p.label) for p in fr] for m, fr in frontiers.items()},
        "checks": checks,
        "holm": holm_correct(pvals) if pvals else {},
    }
    args.out.parent.mkdir(parents=True, exist_ok=True)
    args.out.write_text(json.dumps(out, indent=2, default=float))
    print(f"\nWrote {args.out}")


if __name__ == "__main__":
    main()
