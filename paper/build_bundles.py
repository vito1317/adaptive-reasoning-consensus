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
import re
import subprocess
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


SUPP_README_NAMED = """\
Supplementary material for "TACT: Trust-Anchored Confidence Tempering for
Self-Consistency Voting in Large Language Models", Wei-Chen Ko.

Repository: https://github.com/vito1317/adaptive-reasoning-consensus

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


def build_supplementary_named(out: Path) -> None:
    """The single-blind version: real names, real repository URL, no rewriting.

    JMLR reviews single-blind, so the anonymised supplement is not merely
    unnecessary there -- it is wrong. Its anonymiser substitutes a placeholder
    anonymous.4open.science URL that does not exist, which would ship a dead
    link to the editors.
    """
    files = collect([
        (ROOT / "src", "*.py"), (ROOT / "experiments", "*.py"),
        (ROOT / "tests", "*.py"), (ROOT / "results", "*.json"),
        (ROOT / "data", "*.json"),
    ])
    with zipfile.ZipFile(out, "w", zipfile.ZIP_DEFLATED) as z:
        for src, arc in files:
            z.write(src, arc)
        for extra in ("requirements.txt", "pytest.ini"):
            pth = ROOT / extra
            if pth.exists():
                z.write(pth, extra)
        z.writestr("README.txt", SUPP_README_NAMED)
    print(f"wrote {out.name} ({len(files) + 3} files, {out.stat().st_size / 1e6:.1f} MB), named")


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


TMLR_UPLOAD_README = """\
TMLR submission -- "TACT: Trust-Anchored Confidence Tempering for
Self-Consistency Voting in Large Language Models".

*** DO NOT SUBMIT WHILE THE JMLR SUBMISSION IS LIVE ***

TMLR's editorial policy: "There should not be any reuse of written text,
figures or results between the submitted paper and any paper which has been
published, accepted for publication, or submitted in parallel at another
archival, peer-reviewed venue."

This manuscript is under review at JMLR (26-2518, submitted 2 August 2026).
JMLR is an archival peer-reviewed venue, so submitting this to TMLR before
JMLR renders a decision would breach TMLR's policy and would also falsify the
declaration in the JMLR cover letter that the work is not under review
elsewhere. Submit only after a JMLR decision, or after withdrawing from JMLR.

Everything below is ready for that moment.

  row1_Manuscript_ANONYMOUS.pdf   the paper, tmlr.sty, 21 pp, double-blind.
                                  Verified: no author name, handle, e-mail,
                                  affiliation, repository URL or commit hash in
                                  the text, and no Author/Title fields in the
                                  PDF metadata.

  row2_Supplementary_ANONYMOUS.zip  code, cached traces and the JSON artifact
                                  behind every table. Anonymised and scanned;
                                  packing aborts on any identifying string.

OpenReview form fields
  Title      TACT: Trust-Anchored Confidence Tempering for Self-Consistency
             Voting in Large Language Models
  Abstract   as printed in the PDF (200 words; TMLR sets no cap, this is the
             JMLR limit and it is kept for a single source of truth)
  Keywords   large language models; self-consistency; confidence calibration;
             label-free estimation; rank statistics

Broader Impact Statement
  TMLR requires one only where the work "carries a significant risk of harm".
  This paper aggregates a frozen model's own outputs at inference time and its
  headline recommendation is to abstain; it introduces no new capability, no
  training, and no data collection about people. No statement is included on
  that reading. The action editor may take a different view, so be ready to add
  one rather than surprised to be asked.

Which upload slot
  PDF                 row1_Manuscript_ANONYMOUS.pdf
  Supplementary       row2_Supplementary_ANONYMOUS.zip
  Beyond PDF          NOTHING. That slot is for interactive webpage code, not
                      supplementary material. Putting the supplement there
                      submits it as an alternative rendering of the paper.

Declared in the OpenReview PROFILE, not in the paper
  affiliations, conflicts of interest, publication history, funding, IRB.
  TMLR takes these from the profile, which is why the paper carries none of
  them. Check the profile is current before submitting.
"""


def openreview_abstract() -> str:
    """The abstract as OpenReview wants it pasted, derived from tact.tex.

    Not hand-copied: the abstract has been rewritten several times and a stale
    copy in a text file is exactly the drift this project keeps catching. Three
    conversions matter. OpenReview renders $...$ inline, so real math stays;
    LaTeX's -- becomes an en-dash because the form is plain text; and the per
    cent sign moves OUT of math mode, since $7.5\\%$ either breaks the formula
    or starts a comment depending on the renderer.
    """
    src = (PAPER / "tact.tex").read_text()
    t = re.search(r"\\begin\{abstract\}(.*?)\\end\{abstract\}", src, re.S).group(1)
    t = t.replace("\\TACT{}", "TACT").replace("\\TACT", "TACT")
    t = t.replace("\\Dhat", "\\widehat{D}").replace("\\tfrac12", "\\frac{1}{2}")
    t = re.sub(r"\\emph\{([^}]*)\}", r"\1", t)
    t = t.replace("$2.5$--$7.5\\%$", "2.5\u20137.5%")
    t = t.replace("--", "\u2013").replace("\\%", "%")
    t = t.replace("\\ ", " ").replace("~", " ")
    t = re.sub(r"\s+", " ", t).strip()
    if "--" in t or "\\%" in t:
        raise AssertionError("abstract still carries LaTeX-only markup")
    if any("%" in m for m in re.findall(r"\$[^$]*\$", t)):
        raise AssertionError("a per cent sign is inside math mode; OpenReview will mangle it")
    words = len([w for w in re.sub(r"\$[^$]*\$", " X ", t).split()
                 if re.search(r"[A-Za-z0-9]", w)])
    return t, words


def build_tmlr_submission(outdir: Path) -> None:
    """The double-blind package, with the dual-submission block stated up front.

    Named after the form rows for the same reason the JMLR set is: a combined
    archive sitting beside the per-row files is how the wrong file got uploaded
    once already.
    """
    up = outdir / "tmlr_upload"
    up.mkdir(exist_ok=True)
    for f in up.glob("*"):
        f.unlink()

    pdf = PAPER / "tact_tmlr.pdf"
    text = subprocess.run(["pdftotext", str(pdf), "-"],
                          capture_output=True, text=True).stdout
    # "Ko" is not scanned: it appears inside cited authors such as Kosaraju.
    leaks = [k for k in ("vito1317", "Wei-Chen", "柯瑋宸", "service@vito1317.com",
                         "adaptive-reasoning-consensus", "Independent Researcher")
             if k in text]
    if leaks:
        raise AssertionError(f"anonymous TMLR manuscript would identify the author: {leaks}")
    meta = subprocess.run(["pdfinfo", str(pdf)], capture_output=True, text=True).stdout
    for field in ("Author:", "Title:", "Subject:", "Keywords:"):
        if field in meta:
            raise AssertionError(f"PDF metadata carries {field} in a double-blind submission")

    (up / "row1_Manuscript_ANONYMOUS.pdf").write_bytes(pdf.read_bytes())
    (up / "row2_Supplementary_ANONYMOUS.zip").write_bytes(
        (PAPER / "supplementary_anonymous.zip").read_bytes())
    (up / "00_READ_THIS_FIRST.txt").write_text(TMLR_UPLOAD_README)
    abstract, words = openreview_abstract()
    (up / "field_Title.txt").write_text(
        "TACT: Trust-Anchored Confidence Tempering for Self-Consistency "
        "Voting in Large Language Models\n")
    (up / "field_Abstract.txt").write_text(abstract + "\n")
    (up / "field_Keywords.txt").write_text(
        "large language models; self-consistency; confidence calibration; "
        "label-free estimation; rank statistics\n")
    print(f"wrote {up.name}/ -- manuscript, supplement and the three paste-ready\n      form fields (abstract {words} words), all scanned anonymous; README states\n      the JMLR dual-submission block")


def build_jmlr_submission(outdir: Path) -> None:
    """Emit exactly the files the JMLR form asks for, named after its rows.

    This used to produce a single jmlr_submission.zip containing the manuscript,
    the cover letter, the source and the supplement. That archive was for the
    author's records, but it sat in the same directory under a name one letter
    away from the supplement's, and it got uploaded into the form's "Other"
    slot -- which is marked viewable by reviewers. The cover letter inside it,
    separately and deliberately marked NOT viewable, was therefore exposed
    along with its list of suggested reviewers.

    A combined archive has no use the per-row files do not serve, so it is no
    longer produced. What is emitted instead is one file per form row, prefixed
    with the row number and carrying the viewability setting in the name, so
    picking the wrong file requires ignoring the filename.

    Requirements checked against jmlr.org/author-info.html: PDF under 5 MB in
    the JMLR style, a cover letter carrying six declarations, five keywords, a
    running title of at most 50 characters, an abstract of at most 200 words.
    """
    up = outdir / "jmlr_upload"
    up.mkdir(exist_ok=True)
    for f in up.glob("*"):
        f.unlink()

    pdf_mb = (PAPER / "tact_jmlr.pdf").stat().st_size / 1e6
    if pdf_mb >= 5.0:
        raise AssertionError(f"manuscript PDF is {pdf_mb:.1f} MB; JMLR requires under 5 MB")

    named = PAPER / "supplementary_named.zip"
    build_supplementary_named(named)

    rows = [
        ("tact_jmlr.pdf",          "row1_Manuscript__viewable_YES.pdf"),
        ("jmlr_cover_letter.pdf",  "row2_CoverLetter__viewable_NO.pdf"),
        (named.name,               "row3_Other_supplementary__viewable_YES.zip"),
    ]
    for src, dst in rows:
        (up / dst).write_bytes((PAPER / src).read_bytes())
    (up / "00_HOW_TO_UPLOAD.txt").write_text(JMLR_UPLOAD_README)

    # The combined archive is the hazard this function exists to remove.
    stale = outdir / "jmlr_submission.zip"
    if stale.exists():
        stale.unlink()
        print(f"removed {stale.name} (contained the cover letter; see docstring)")
    print(f"wrote {up.name}/ -- 3 upload files named after the form rows, "
          f"manuscript {pdf_mb:.2f} MB")


JMLR_UPLOAD_README = """\
JMLR submission form -- upload exactly these three files, one per row.

  row1_Manuscript__viewable_YES.pdf            File Type: Manuscript
                                               Viewable by reviewers: yes (fixed)

  row2_CoverLetter__viewable_NO.pdf            File Type: Cover Letter
                                               Viewable by reviewers: NO
                                               It names five suggested reviewers.
                                               A reviewer who is one of them must
                                               not see that they were suggested.

  row3_Other_supplementary__viewable_YES.zip   File Type: Other
                                               Viewable by reviewers: yes
                                               Code, cached traces, and the JSON
                                               artifacts behind every table, so
                                               reviewers can verify the claims.

Title:  TACT: Trust-Anchored Confidence Tempering for Self-Consistency Voting
        in Large Language Models
Special issue: No

Notes added to the manuscript record must have "viewable by: reviewers"
UNCHECKED; the form checks it by default.
"""


def main() -> None:
    ap = argparse.ArgumentParser()
    ap.add_argument("--outdir", type=Path, default=PAPER)
    args = ap.parse_args()
    build_supplementary(args.outdir / "supplementary_anonymous.zip")
    build_paper_bundle(args.outdir / "TACT Paper.zip")
    build_jmlr_submission(args.outdir)
    build_tmlr_submission(args.outdir)


if __name__ == "__main__":
    main()
