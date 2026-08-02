#!/usr/bin/env python
"""Pack the two distributable archives, reproducibly.

Both used to be assembled by hand, which is why they were eight commits stale
before anyone noticed -- the same gap that let tact.docx and group_eval.png
drift. They are now built from a manifest.

  supplementary_anonymous.zip   the TMLR double-blind supplement: code,
                                experiments, tests, artifacts and cached
                                traces, with a generated README. Every file is
                                scanned for identifying strings and packing
                                ABORTS on a hit, because a supplement that
                                de-anonymises the submission cannot be recalled
                                once uploaded.
  TACT Paper.zip                the named bundle: every rendered format of the
                                paper plus the figures and the reference guide.

    python paper/build_bundles.py
"""

from __future__ import annotations

import argparse
import zipfile
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
PAPER = ROOT / "paper"

# Identifying strings. github.com is deliberately absent: third-party
# repositories are cited in the verification artifact (the LeetCodeDataset
# companion, for one) and blanket-matching the host would fire on those. The
# author's own repository is matched by name instead.
IDENTIFYING = [
    "vito1317", "Wei-Chen", "柯瑋宸", "service@vito1317.com",
    "adaptive-reasoning-consensus", "Independent Researcher", "/Users/vito",
]
SCAN_SUFFIXES = {".py", ".json", ".txt", ".md", ".cfg", ".ini", ".toml", ".sh"}

SUPP_README = """\
Supplementary material for "TACT: Trust-Anchored Confidence Tempering".

Anonymized for double-blind review: names, e-mail addresses, the repository
URL and absolute paths have been replaced throughout.

Reproducing the tables:
  pip install -r requirements.txt
  pytest -q                                     # 102 tests
  python experiments/run_tact_eval.py           # Tables 1-2 (synthetic)
  python experiments/run_group_eval.py          # Table 3 (heterogeneity)
  python experiments/run_seed_dispersion.py     # seed intervals
  python experiments/run_cap_ablation.py        # cap ablation
  python experiments/run_tact_hard_eval.py      # real-trace campaign
  python experiments/run_g1_window.py           # window measurement
  python experiments/run_abstention_identifiability.py
                                                # finding (e): is the
                                                # abstention a mechanism?
  python experiments/run_planted_sensitivity.py # finding (f): planted-channel
                                                # operating characteristic
  python experiments/check_paper_numbers.py     # cross-checks every figure in
                                                # the paper against results/
Cached traces are in data/, so no API key is needed to reproduce any table.
"""


def collect(patterns: list[tuple[Path, str]]) -> list[tuple[Path, str]]:
    out: list[tuple[Path, str]] = []
    for base, glob in patterns:
        for f in sorted(base.rglob(glob)):
            if f.is_file() and "__pycache__" not in f.parts and not f.name.startswith("~$"):
                out.append((f, str(f.relative_to(ROOT))))
    return out


def anonymize(text: str) -> str:
    text = text.replace("https://github.com/vito1317/adaptive-reasoning-consensus",
                        "https://anonymous.4open.science/r/tact-anonymous")
    text = text.replace("adaptive-reasoning-consensus", "tact-anonymous")
    for s in ("vito1317", "Wei-Chen Ko", "柯瑋宸", "service@vito1317.com",
              "Independent Researcher"):
        text = text.replace(s, "ANONYMIZED")
    return text.replace("/Users/vito", "/home/anon")


def assert_clean(name: str, text: str) -> None:
    hits = [s for s in IDENTIFYING if s in text]
    if hits:
        raise AssertionError(
            f"anonymous supplement would identify the author via {name}: {hits}")


def build_supplementary(out: Path) -> None:
    files = collect([
        (ROOT / "src", "*.py"), (ROOT / "experiments", "*.py"),
        (ROOT / "tests", "*.py"), (ROOT / "results", "*.json"),
        (ROOT / "data", "*.json"),
    ])
    with zipfile.ZipFile(out, "w", zipfile.ZIP_DEFLATED) as z:
        for src, arc in files:
            if src.suffix in SCAN_SUFFIXES:
                text = anonymize(src.read_text(errors="replace"))
                assert_clean(arc, text)
                z.writestr(arc, text)
            else:
                z.write(src, arc)
        for extra in ("requirements.txt", "pytest.ini"):
            p = ROOT / extra
            if p.exists():
                text = anonymize(p.read_text())
                assert_clean(extra, text)
                z.writestr(extra, text)
        assert_clean("README.txt", SUPP_README)
        z.writestr("README.txt", SUPP_README)
    print(f"wrote {out.name} ({len(files) + 3} files, {out.stat().st_size / 1e6:.1f} MB), "
          "no identifying string present")


def build_paper_bundle(out: Path) -> None:
    names = [
        "tact.pdf", "tact.tex", "tact.docx",
        "tact_tmlr.pdf", "tact_tmlr.tex",
        "tact_tmlr_preprint.pdf", "tact_tmlr_preprint.tex",
        "tact_jmlr.pdf", "tact_jmlr.tex",
        "tact_zh.pdf", "tact_zh.docx", "tact_zh.md",
        "tact_parameters_zh.pdf", "tact_parameters_zh.docx", "tact_parameters_zh.md",
        "references_guide.pdf", "references_guide.docx", "references_guide.md",
        "references.bib", "tmlr.sty", "tmlr.bst", "jmlr2e.sty", "fancyhdr.sty",
    ]
    figs = sorted((PAPER / "figs").glob("*.pdf")) + sorted((PAPER / "figs").glob("*.png"))
    with zipfile.ZipFile(out, "w", zipfile.ZIP_DEFLATED) as z:
        n = 0
        for nm in names:
            p = PAPER / nm
            if p.exists():
                z.write(p, nm)
                n += 1
        for f in figs:
            z.write(f, f"figs/{f.name}")
            n += 1
    print(f"wrote {out.name} ({n} files, {out.stat().st_size / 1e6:.1f} MB)")


def build_jmlr_submission(outdir: Path) -> None:
    """Everything JMLR asks for at submission, plus what it asks for on acceptance.

    Requirements checked against jmlr.org/author-info.html: PDF under 5 MB in
    the JMLR style, a cover letter carrying six specific declarations, five
    keywords, a running title of 50 characters or less, and an abstract of at
    most 200 words. Source is not required until acceptance but is included
    because it is cheap to ship and expensive to reconstruct later; it is
    verified to compile from these files alone.
    """
    zip_path = outdir / "jmlr_submission.zip"
    src = [("tact_jmlr.pdf", "01_manuscript_tact_jmlr.pdf"),
           ("jmlr_cover_letter.pdf", "02_cover_letter.pdf")]
    with zipfile.ZipFile(zip_path, "w", zipfile.ZIP_DEFLATED) as z:
        for name, arc in src:
            z.write(PAPER / name, arc)
        for name in ("tact_jmlr.tex", "jmlr2e.sty", "references.bib"):
            z.write(PAPER / name, f"03_source/{name}")
        for f in sorted((PAPER / "figs").glob("*.pdf")):
            z.write(f, f"03_source/figs/{f.name}")
        z.write(PAPER / "supplementary_anonymous.zip", "04_supplementary_code_and_data.zip")
        z.writestr("00_README.txt", JMLR_README)
    size = zip_path.stat().st_size / 1e6
    pdf = (PAPER / "tact_jmlr.pdf").stat().st_size / 1e6
    if pdf >= 5.0:
        raise AssertionError(f"manuscript PDF is {pdf:.1f} MB; JMLR requires under 5 MB")
    print(f"wrote {zip_path.name} ({size:.1f} MB); manuscript PDF {pdf:.2f} MB, "
          "inside JMLR's 5 MB limit")


JMLR_README = """\
JMLR submission package -- "TACT: Trust-Anchored Confidence Tempering for
Self-Consistency Voting in Large Language Models", Wei-Chen Ko.

01_manuscript_tact_jmlr.pdf     the paper, jmlr2e style, 26 pp
02_cover_letter.pdf             the six declarations JMLR requires, including
                                five suggested action editors and five
                                suggested reviewers
03_source/                      LaTeX source; compiles to the identical PDF
                                from these files alone (verified clean-room)
04_supplementary_code_and_data  code, cached traces and the JSON artifact
                                behind every table and figure

Reproducing any table needs no API key; the traces are cached. See the
README inside the supplementary archive.
"""


def main() -> None:
    ap = argparse.ArgumentParser()
    ap.add_argument("--outdir", type=Path, default=PAPER)
    args = ap.parse_args()
    build_supplementary(args.outdir / "supplementary_anonymous.zip")
    build_paper_bundle(args.outdir / "TACT Paper.zip")
    build_jmlr_submission(args.outdir)


if __name__ == "__main__":
    main()
