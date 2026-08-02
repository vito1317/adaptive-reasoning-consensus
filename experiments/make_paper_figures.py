#!/usr/bin/env python
"""Render the four paper figures as vector PDF (plus PNG for the Word/markdown paths).

This is separate from make_figures.py, which renders the whole project's
exploratory figures at 150 dpi with long explanatory titles baked into the
image. That is the right thing for a report and the wrong thing for a journal:
the raster text does not scale, and the in-figure titles repeat the LaTeX
caption almost word for word, which is what makes the panels look crowded.

Here every figure is vector, typeset in a serif face close to the body text,
and carries no title -- the caption says it once. group_eval had no generator
anywhere in the repo before this file; it was produced by hand, which meant one
of the four paper figures could not be reproduced from the artifacts.

    python experiments/make_paper_figures.py            # -> paper/figs/*.pdf, *.png
"""

from __future__ import annotations

import argparse
import json
from pathlib import Path

import matplotlib

matplotlib.use("Agg")
import matplotlib.pyplot as plt  # noqa: E402
import numpy as np  # noqa: E402

ROOT = Path(__file__).resolve().parents[1]

# Authored at the size they are printed: IEEE's column is 3.5in and the
# single-column builds place them at 0.62\linewidth = 3.7in, so a 3.45in
# canvas is reproduced at roughly 1:1 in both and the point sizes below are
# the point sizes on paper. Authoring wider and letting LaTeX shrink is what
# made the first version's labels unreadable: a 6.6in canvas at \columnwidth
# is scaled to 53%, turning 10.5pt type into 5.6pt.
RC = {
    "font.family": "serif",
    "font.serif": ["DejaVu Serif"],
    "mathtext.fontset": "dejavuserif",
    "font.size": 8,
    "axes.labelsize": 8,
    "axes.titlesize": 8.5,
    "xtick.labelsize": 7,
    "ytick.labelsize": 7,
    "legend.fontsize": 6.4,
    "axes.linewidth": 0.6,
    "grid.linewidth": 0.4,
    "lines.linewidth": 1.2,
    "lines.markersize": 3.2,
    "figure.constrained_layout.use": True,
    "pdf.fonttype": 42,   # embed as TrueType, not Type 3: some venues reject Type 3
    "ps.fonttype": 42,
    "savefig.bbox": "tight",
    "savefig.pad_inches": 0.02,
}


def save(fig, outdir: Path, stem: str) -> None:
    """Vector for the paper, raster for pandoc's Word and markdown paths."""
    for ext, kw in ((".pdf", {}), (".png", {"dpi": 400})):
        fig.savefig(outdir / f"{stem}{ext}", **kw)
    plt.close(fig)
    print(f"  wrote {stem}.pdf + {stem}.png")


def fig_kappa_sweep(data: dict, outdir: Path) -> None:
    """Fig. 1 -- the pre-measured baseline landscape."""
    sweep = data["sweep"]
    x = [r["kappa_c"] for r in sweep]
    series = [
        ("SC", "SC (ignores confidence)", "#444444", "--", "o"),
        ("CISC(g=1.0)", r"CISC $\gamma{=}1$ (always trusts)", "#9467bd", ":", "^"),
        ("ECE-gate", "ECE gate (calibration)", "#1f77b4", "-.", "s"),
        ("AUC-gate", "AUC gate (discrimination + sign)", "#2ca02c", "-", "D"),
        ("oracle", r"oracle fixed $(\gamma,\mathrm{sign})$", "#d62728", "-", "*"),
    ]
    fig, ax = plt.subplots(figsize=(3.45, 2.85))
    for key, label, color, ls, marker in series:
        ax.plot(x, [r[key] for r in sweep], label=label, color=color, ls=ls, marker=marker)
    ax.fill_between(x, [r["AUC-gate"] for r in sweep], [r["oracle"] for r in sweep],
                    color="#d62728", alpha=0.08, label="headroom for a new method")
    ax.set_xlabel("true confidence\u2013correctness coupling $\\kappa_c$")
    ax.set_ylabel(r"accuracy @ fixed $K$")
    ax.grid(alpha=0.25)
    ax.legend(loc="upper center", bbox_to_anchor=(0.5, -0.30), ncol=2,
              columnspacing=1.0, handlelength=1.8, frameon=False)
    save(fig, outdir, "kappa_sweep")


def fig_tact_sweep(data: dict, outdir: Path) -> None:
    """Fig. 2 -- TACT on the same frontier."""
    sweep = data["sweep_dev200"]
    x = [r["kappa_c"] for r in sweep]
    series = [
        ("SC", "SC", "#444444", "--", "o"),
        ("ECE-gate", "ECE gate", "#1f77b4", "-.", "s"),
        ("CISC-devT", "CISC-devT (published)", "#9467bd", ":", "^"),
        ("SignGrid-dev", "dev signed grid", "#2ca02c", "-", "D"),
        ("TACT-dev", "TACT-dev", "#d62728", "-", "*"),
        ("TACT-LF", "TACT-LF (label-free)", "#ff7f0e", "-", "P"),
    ]
    fig, ax = plt.subplots(figsize=(3.45, 2.85))
    for key, label, color, ls, marker in series:
        ax.plot(x, [r["acc"][key] for r in sweep], label=label, color=color, ls=ls, marker=marker)
    ax.plot(x, [r["oracle"]["acc"] for r in sweep], color="#999999", ls=":", lw=1.3,
            label=r"oracle fixed $(\gamma,\mathrm{sign})$")
    ax.set_xlabel("true confidence\u2013correctness coupling $\\kappa_c$")
    ax.set_ylabel(r"accuracy @ fixed $K$")
    ax.grid(alpha=0.25)
    ax.legend(loc="upper center", bbox_to_anchor=(0.5, -0.30), ncol=3,
              columnspacing=1.0, handlelength=1.8, frameon=False)
    save(fig, outdir, "tact_sweep")


def fig_tact_adversarial(data: dict, outdir: Path) -> None:
    """Fig. 3 -- the adversarial cells."""
    adv = data["adversarial"]
    names = list(adv)
    pretty = {"monotone_compress": "monotone\ncompress", "monotone_overconf": "monotone\noverconf",
              "monotone_power": "monotone\npower", "heterogeneous_kappa": "heterogeneous\n$\\kappa$",
              "confident_echo": "confident\necho"}
    methods = [("SC", "#444444"), ("CISC-devT", "#9467bd"), ("SignGrid-dev", "#2ca02c"),
               ("TACT-dev", "#d62728"), ("TACT-LF", "#ff7f0e")]
    fig, ax = plt.subplots(figsize=(3.45, 2.75))
    xs = np.arange(len(names))
    width = 0.16
    for j, (m, c) in enumerate(methods):
        ax.bar(xs + (j - 2) * width, [adv[n]["acc"][m] for n in names], width, label=m, color=c)
    for i, n in enumerate(names):
        ax.plot([i - 3 * width, i + 3 * width], [adv[n]["oracle"]["acc"]] * 2,
                color="#666666", ls=":", lw=1.4)
    ax.set_xticks(xs, [pretty.get(n, n.replace("_", "\n")) for n in names])
    ax.set_ylabel(r"accuracy @ fixed $K$")
    ax.set_ylim(0, 1.05)
    ax.grid(alpha=0.25, axis="y")
    ax.legend(loc="upper center", bbox_to_anchor=(0.5, -0.22), ncol=3,
              columnspacing=1.0, handlelength=1.5, frameon=False)
    save(fig, outdir, "tact_adversarial")


def fig_group_eval(data: dict, outdir: Path) -> None:
    """Fig. 4 -- structured vs i.i.d. heterogeneity.

    No generator for this existed; it is rebuilt here directly from
    results/group_eval.json so the figure and the table cannot disagree.
    """
    cells = data["cells"]
    # Panels stack rather than sit side by side: at one column the method
    # labels are wider than half the canvas, and abbreviating them enough to
    # fit two panels across would cost more than the vertical space does.
    rows = [("SC", "SC (floor)", "#444444"),
            ("TACT-global-dev", "TACT global", "#8c8c8c"),
            ("TACT-group-dev", "TACT-group (dev)", "#d62728"),
            ("TACT-group-LF", "TACT-group (LF)", "#ff7f0e"),
            ("naive-per-item", "naive per-item", "#1f77b4"),
            ("per-item-link-oracle", "per-item oracle", "#2ca02c")]
    fig, axes = plt.subplots(2, 1, figsize=(3.45, 3.5), sharex=True)
    for ax, (cell, title) in zip(axes, (("grouped", "covariate-structured"), ("iid", "i.i.d."))):
        acc = cells[cell]["acc"]
        ys = np.arange(len(rows))
        ax.barh(ys, [acc[k] for k, _, _ in rows], color=[c for _, _, c in rows], height=0.66)
        for y, (k, _, _) in zip(ys, rows):
            ax.text(acc[k] + 0.012, y, f"{acc[k]:.3f}", va="center", fontsize=6.2)
        ax.axvline(acc["SC"], color="#444444", ls="--", lw=0.9)
        ax.set_yticks(ys, [lab for _, lab, _ in rows])
        ax.set_xlim(0, 1.15)
        ax.set_title(title, pad=3)
        ax.invert_yaxis()
        ax.grid(alpha=0.25, axis="x")
    axes[-1].set_xlabel(r"accuracy @ fixed $K$")
    save(fig, outdir, "group_eval")


def main() -> None:
    ap = argparse.ArgumentParser()
    ap.add_argument("--outdir", type=Path, default=ROOT / "paper" / "figs")
    args = ap.parse_args()
    args.outdir.mkdir(parents=True, exist_ok=True)

    with plt.rc_context(RC):
        print("paper figures ->", args.outdir)
        fig_kappa_sweep(json.loads((ROOT / "results/kappa_sweep.json").read_text()), args.outdir)
        tact = json.loads((ROOT / "results/tact_eval.json").read_text())
        fig_tact_sweep(tact, args.outdir)
        fig_tact_adversarial(tact, args.outdir)
        fig_group_eval(json.loads((ROOT / "results/group_eval.json").read_text()), args.outdir)


if __name__ == "__main__":
    main()
