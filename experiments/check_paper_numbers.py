#!/usr/bin/env python
"""Cross-check the numbers in the paper against the artifacts that produced them.

The synthetic data has been regenerated twice (the tie-break fix, then the
seed work), and each time some prose figure was left behind while the tables
moved. Chasing those by hand does not scale, so this asserts the paper's
claims against results/*.json directly.

Reported, not guessed: every entry below names the artifact field it came
from. A mismatch is printed with both values so it can be judged rather than
silently patched.

    python experiments/check_paper_numbers.py
"""

from __future__ import annotations

import json
import re
import sys
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]

# Both the English source and the Chinese edition are checked. The Chinese one
# is here because it silently fell three commits behind while the tables moved
# under it, which is exactly the drift this script exists to catch.
DOCS = {
    "tact.tex": (ROOT / "paper" / "tact.tex").read_text(),
    "tact_zh.md": (ROOT / "paper" / "tact_zh.md").read_text(),
}
TEX = DOCS["tact.tex"]


def load(name):
    return json.loads((ROOT / "results" / name).read_text())


def fmt(x):
    return f"{x:.3f}"


def cell(ev, kappa):
    for r in ev["sweep_dev200"]:
        if abs(r["kappa_c"] - kappa) < 1e-9:
            return r
    raise KeyError(kappa)


def main():
    ev = load("tact_eval.json")
    grp = load("group_eval.json")["cells"]["grouped"]
    disp = load("seed_dispersion.json")["cells"]
    bud = load("budget_paired.json")
    g1 = load("g1_window.json")
    hard = load("tact_hard_eval.json")

    checks: list[tuple[str, str, str]] = []

    def want(label, value, artifact):
        """Assert the formatted value appears in every edition of the paper."""
        s = fmt(value) if isinstance(value, float) else str(value)
        forms = {s}
        if s.startswith("0."):
            forms.add(s.lstrip("0"))
        if isinstance(value, float) and 0 < value < 1:
            # the paper writes rates as per cent in places, e.g. 0.118 -> 11.8
            forms |= {f"{value*100:.1f}", f"{value*100:.2f}", f"{value*100:.0f}"}
        absent = [name for name, text in DOCS.items()
                  if not any(x in text for x in forms)]
        checks.append((label, s, artifact if not absent
                       else f"MISSING in {','.join(absent)} ({artifact})"))
        return not absent

    # headline sweep cells
    for k in (-0.6, -0.2, -0.1, 0.1, 0.2, 0.6):
        r = cell(ev, k)
        want(f"sweep kappa={k:+.1f} TACT-dev", r["acc"]["TACT-dev"], "tact_eval.sweep_dev200")
        want(f"sweep kappa={k:+.1f} SignGrid", r["acc"]["SignGrid-dev"], "tact_eval.sweep_dev200")

    # adversarial
    adv = ev["adversarial"]
    want("echo TACT-dev", adv["confident_echo"]["acc"]["TACT-dev"], "tact_eval.adversarial")
    want("echo SignGrid", adv["confident_echo"]["acc"]["SignGrid-dev"], "tact_eval.adversarial")
    want("echo SC", adv["confident_echo"]["acc"]["SC"], "tact_eval.adversarial")
    want("compress oracle", adv["monotone_compress"]["oracle"]["acc"], "tact_eval.adversarial")

    # group study
    want("group SC", grp["acc"]["SC"], "group_eval.grouped")
    want("group TACT-LF", grp["acc"]["TACT-group-LF"], "group_eval.grouped")

    # dispersion intervals quoted in the seeds subsection
    for k in ("kappa=-0.2", "kappa=-0.1", "kappa=+0.1", "kappa=+0.2",
              "monotone_compress", "confident_echo"):
        d = disp[k]["TACT_minus_SignGrid"]
        want(f"dispersion {k} mean", abs(d["mean"]), "seed_dispersion")

    # budget arm
    want("budget per-sample free", bud["free"]["per_sample"], "budget_paired.free")
    want("budget per-sample capped", bud["constrained"]["per_sample"], "budget_paired.constrained")
    want("budget window capped", bud["constrained"]["window"], "budget_paired.constrained")
    want("budget SC capped", bud["constrained"]["sc"], "budget_paired.constrained")

    # window table
    want("LeetCode window", g1["window"], "g1_window")
    want("hard-campaign D", hard["h1"]["d_hat"], "tact_hard_eval.h1")

    bad = [c for c in checks if c[2].startswith("MISSING")]
    for label, val, src in checks:
        mark = "  " if not src.startswith("MISSING") else "!!"
        print(f"{mark} {label:36s} {val:>8s}  {src}")
    print(f"\n{len(checks) - len(bad)}/{len(checks)} values found in the paper")
    if bad:
        print("\nnot found (either stale in the paper or simply not quoted):")
        for label, val, src in bad:
            print(f"  {label:36s} artifact says {val}")
    return 1 if bad else 0


if __name__ == "__main__":
    sys.exit(main())
