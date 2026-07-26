#!/usr/bin/env python
"""Render figures from the experiment JSON outputs.

    python experiments/make_figures.py --frontier results/frontier.json \
        --boundary results/boundary.json --outdir results/figures
"""

from __future__ import annotations

import argparse
import json
import sys
from pathlib import Path

import matplotlib

matplotlib.use("Agg")
import matplotlib.pyplot as plt  # noqa: E402
import numpy as np  # noqa: E402

sys.path.insert(0, str(Path(__file__).resolve().parents[1] / "src"))

from rlev_voi.weights import block_model_effective_count  # noqa: E402

STYLE = {
    "SC": dict(color="#444444", marker="o", ls="--", label="Self-Consistency"),
    "ASC": dict(color="#1f77b4", marker="s", ls="-", label="Adaptive-Consistency"),
    "CISC": dict(color="#9467bd", marker="^", ls=":", label="CISC (conf-weighted)"),
    "dedup-SC": dict(color="#8c564b", marker="v", ls=":", label="dedup-SC"),
    "RASC-lite": dict(color="#2ca02c", marker="D", ls="-", label="RASC-lite"),
    "ESC": dict(color="#bcbd22", marker="P", ls=":", label="ESC"),
    "SPRT": dict(color="#7f7f7f", marker="X", ls=":", label="SPRT"),
    "RLEV-SAFE": dict(color="#ff7f0e", marker="o", ls="-", label="RLEV SAFE"),
    "RLEV-AGGR": dict(color="#d62728", marker="*", ls="-", label="RLEV AGGRESSIVE"),
    "RLEV-VoI": dict(color="#e377c2", marker="h", ls="-.", label="RLEV VoI-stop"),
}


def plot_frontiers(data: dict, outdir: Path) -> None:
    regimes = data["regimes"]
    n = len(regimes)
    ncols = 3
    nrows = (n + ncols - 1) // ncols
    fig, axes = plt.subplots(nrows, ncols, figsize=(6.2 * ncols, 4.9 * nrows), squeeze=False)
    flat = [ax for row in axes for ax in row]
    for ax in flat[n:]:
        ax.axis("off")
    for ax, (name, r) in zip(flat, regimes.items()):
        for method, pts in r["frontiers"].items():
            if method not in STYLE or not pts:
                continue
            pts = sorted(pts, key=lambda p: p[0])
            xs = [p[0] for p in pts]
            ys = [p[1] for p in pts]
            st = dict(STYLE[method])
            lbl = st.pop("label")
            ax.plot(xs, ys, **st, label=lbl, ms=5, lw=1.6, alpha=0.9)
        ax.set_title(name.replace("_", " "), fontsize=11)
        ax.set_xlabel("total cost (token-equivalents)")
        ax.set_ylabel("accuracy")
        ax.grid(alpha=0.25)
        kd = r.get("kernel_diagnostic", {})
        if kd:
            ax.text(
                0.02,
                0.02,
                f"weight CV={kd['weight_cv_mean']:.3f}\n"
                f"n_eff/K={kd['n_eff_over_K_mean']:.2f}"
                + ("\nCOLLAPSED -> = SC" if kd.get("collapsed_to_SC") else ""),
                transform=ax.transAxes,
                fontsize=8,
                va="bottom",
                bbox=dict(boxstyle="round", fc="#fffbe6", ec="#ccc", alpha=0.9),
            )
    handles, labels = flat[0].get_legend_handles_labels()
    legend_ax = flat[n] if n < len(flat) else flat[-1]
    if n < len(flat):
        legend_ax.legend(handles, labels, fontsize=11, loc="center", frameon=False)
    else:
        flat[-1].legend(fontsize=8, loc="lower right", framealpha=0.9)
    fig.suptitle(
        "Accuracy vs total cost -- Pareto frontiers\n"
        "SYNTHETIC data: implementation-correctness, no-regret and boundary checks only. "
        "NOT evidence of benefit on real LLM traces.",
        fontsize=12,
    )
    fig.tight_layout(rect=(0, 0, 1, 0.94))
    fig.savefig(outdir / "frontiers.png", dpi=150)
    plt.close(fig)


def plot_block_model(outdir: Path) -> None:
    """Analytic verification: one echo cluster collapses to one effective vote."""
    fig, ax = plt.subplots(figsize=(6.2, 4.2))
    ms = np.arange(1, 21)
    for rho in (0.0, 0.25, 0.5, 0.75, 1.0):
        ax.plot(
            ms,
            [block_model_effective_count(int(m), rho) for m in ms],
            marker="o",
            ms=3,
            label=f"rho={rho}",
        )
    ax.plot(ms, ms, color="#999", ls=":", lw=1, label="raw count (SC)")
    ax.set_xlabel("cluster size m (near-identical traces)")
    ax.set_ylabel("effective votes  $N_g^{eff}$")
    ax.set_title("Redundancy discount: $N^{eff}_g = m / (1 + (m-1)\\rho)$")
    ax.legend(fontsize=8)
    ax.grid(alpha=0.25)
    fig.tight_layout()
    fig.savefig(outdir / "block_model.png", dpi=150)
    plt.close(fig)


def plot_boundary(data: dict, outdir: Path) -> None:
    cells = data["shared_x_tightness"]
    seps = sorted({c["sem_shared"] for c in cells})
    sprs = sorted({c["tightness"] for c in cells})
    cv = np.full((len(sprs), len(seps)), np.nan)
    gain = np.full((len(sprs), len(seps)), np.nan)
    for c in cells:
        i, j = sprs.index(c["tightness"]), seps.index(c["sem_shared"])
        cv[i, j] = c["weight_cv"]
        gain[i, j] = c["gain_vs_sc"]

    fig, axes = plt.subplots(1, 2, figsize=(11.5, 4.4))
    for ax, M, title, cmap in [
        (axes[0], cv, "weight coefficient of variation\n(<0.05 = collapsed to SC)", "viridis"),
        (axes[1], gain, "accuracy gain vs SC at matched K", "RdBu_r"),
    ]:
        vmax = np.nanmax(np.abs(M)) if "gain" in title else None
        im = ax.imshow(
            M,
            origin="lower",
            aspect="auto",
            cmap=cmap,
            **({"vmin": -vmax, "vmax": vmax} if vmax else {}),
        )
        ax.set_xticks(range(len(seps)), [str(s) for s in seps])
        ax.set_yticks(range(len(sprs)), [str(s) for s in sprs])
        ax.set_xlabel("question-level cosine baseline (real CoT ~0.65-0.85)")
        ax.set_ylabel("extra within-cluster cosine")
        ax.set_title(title, fontsize=10)
        fig.colorbar(im, ax=ax)
    fig.suptitle("Useful-regime boundary: where redundancy weighting has any headroom", fontsize=11)
    fig.tight_layout()
    fig.savefig(outdir / "boundary.png", dpi=150)
    plt.close(fig)

    echo = data.get("echo_sweep", [])
    if echo:
        fig, ax = plt.subplots(figsize=(6.2, 4.2))
        x = [c["echo_prob"] for c in echo]
        ax.plot(x, [c["acc_rlev"] for c in echo], marker="o", label="RLEV-VoI")
        ax.plot(x, [c["acc_sc_matched_n"] for c in echo], marker="s", ls="--", label="SC @ matched K")
        ax.plot(x, [c["guard_rate"] for c in echo], marker="^", ls=":", label="guard firing rate")
        ax.set_xlabel("verbatim echo probability in the wrong cluster")
        ax.set_ylabel("accuracy / rate")
        ax.set_title("Effect of verbatim echo (the mechanism the guard targets)")
        ax.legend(fontsize=8)
        ax.grid(alpha=0.25)
        fig.tight_layout()
        fig.savefig(outdir / "echo_sweep.png", dpi=150)
        plt.close(fig)


def plot_voi_scale(data: dict, outdir: Path) -> None:
    """Show that the spec's default lambda sits far above the observed VoI range."""
    regimes = data["regimes"]
    rows = [(n, r["voi_scale"]) for n, r in regimes.items() if r.get("voi_scale")]
    if not rows:
        return
    fig, ax = plt.subplots(figsize=(7.2, 4.2))
    names = [n for n, _ in rows]
    med = [v["median"] for _, v in rows]
    p90 = [v["p90"] for _, v in rows]
    mx = [v["max"] for _, v in rows]
    x = np.arange(len(names))
    ax.bar(x - 0.25, med, 0.25, label="median VoI/token")
    ax.bar(x, p90, 0.25, label="p90")
    ax.bar(x + 0.25, mx, 0.25, label="max")
    ax.axhline(1e-3, color="crimson", ls="--", lw=1.5, label="spec default $\\lambda=10^{-3}$")
    ax.set_yscale("log")
    ax.set_xticks(x, [n.replace("_", "\n") for n in names], fontsize=8)
    ax.set_ylabel("VoI per token")
    ax.set_title("The default $\\lambda$ sits above every observed value\n=> the VoI branch fires unconditionally")
    ax.legend(fontsize=8)
    ax.grid(alpha=0.25, axis="y")
    fig.tight_layout()
    fig.savefig(outdir / "voi_scale.png", dpi=150)
    plt.close(fig)


def plot_kappa_sweep(data: dict, outdir: Path) -> None:
    """The confidence-usage frontier: who wins at each true coupling strength."""
    sweep = data["sweep"]
    x = [r["kappa_c"] for r in sweep]
    series = [
        ("SC", "SC (ignore confidence)", "#444444", "--", "o"),
        ("CISC(g=1.0)", "CISC g=1 (always trust)", "#9467bd", ":", "^"),
        ("ECE-gate", "ECE gate (binary, calibration)", "#1f77b4", "-.", "s"),
        ("AUC-gate", "AUC gate (binary, discrimination+sign)", "#2ca02c", "-", "D"),
        ("oracle", "oracle fixed (gamma, sign) on test", "#d62728", "-", "*"),
    ]
    fig, ax = plt.subplots(figsize=(8.4, 5.2))
    for key, label, color, ls, marker in series:
        ax.plot(x, [r[key] for r in sweep], label=label, color=color, ls=ls, marker=marker, ms=5, lw=1.8)
    ax.fill_between(
        x,
        [r["AUC-gate"] for r in sweep],
        [r["oracle"] for r in sweep],
        color="#d62728",
        alpha=0.08,
        label="headroom left for a new method",
    )
    ax.set_xlabel("true confidence-correctness coupling  $\\kappa_c$")
    ax.set_ylabel("accuracy @ fixed K")
    ax.set_title(
        "Confidence-usage frontier (baselines only)\n"
        "A trivial sign-corrected AUC gate nearly saturates the homogeneous sweep;\n"
        "the open ground is monotone distortion, per-item heterogeneity, small dev sets, label-free"
    )
    ax.grid(alpha=0.25)
    ax.legend(fontsize=8, loc="lower left")
    fig.tight_layout()
    fig.savefig(outdir / "kappa_sweep.png", dpi=150)
    plt.close(fig)

    adv = data.get("adversarial", {})
    if adv:
        names = list(adv)
        methods = ["SC", "CISC(g=1.0)", "ECE-gate", "AUC-gate", "oracle"]
        fig, ax = plt.subplots(figsize=(8.4, 4.4))
        width = 0.15
        xs = np.arange(len(names))
        for j, m in enumerate(methods):
            ax.bar(xs + (j - 2) * width, [adv[n][m] for n in names], width, label=m)
        ax.set_xticks(xs, [n.replace("_", "\n") for n in names], fontsize=8)
        ax.set_ylabel("accuracy @ fixed K")
        ax.set_title("Adversarial confidence regimes -- where every existing policy leaves headroom")
        ax.legend(fontsize=8)
        ax.grid(alpha=0.25, axis="y")
        fig.tight_layout()
        fig.savefig(outdir / "kappa_adversarial.png", dpi=150)
        plt.close(fig)


def main():
    ap = argparse.ArgumentParser()
    ap.add_argument("--frontier", type=Path, default=Path("results/frontier.json"))
    ap.add_argument("--boundary", type=Path, default=Path("results/boundary.json"))
    ap.add_argument("--kappa", type=Path, default=Path("results/kappa_sweep.json"))
    ap.add_argument("--outdir", type=Path, default=Path("results/figures"))
    args = ap.parse_args()
    args.outdir.mkdir(parents=True, exist_ok=True)

    plot_block_model(args.outdir)
    print("wrote block_model.png")
    if args.frontier.exists():
        d = json.loads(args.frontier.read_text())
        plot_frontiers(d, args.outdir)
        plot_voi_scale(d, args.outdir)
        print("wrote frontiers.png, voi_scale.png")
    if args.boundary.exists():
        plot_boundary(json.loads(args.boundary.read_text()), args.outdir)
        print("wrote boundary.png, echo_sweep.png")
    if args.kappa.exists():
        plot_kappa_sweep(json.loads(args.kappa.read_text()), args.outdir)
        print("wrote kappa_sweep.png, kappa_adversarial.png")


if __name__ == "__main__":
    main()
