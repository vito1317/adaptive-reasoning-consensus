#!/usr/bin/env python
"""The Chinese edition must cover the English paper, section for section.

This exists because of a defect that produced no error anywhere. A complete
Chinese retranslation was written and committed as ``tact_zh_complete.md``, but
nothing was ever pointed at it: the README link, the release bundle, the number
checker and the Word link checker all name ``tact_zh.md``. So every reader kept
getting the older, condensed file -- 17 pages against the complete 20, missing
both pseudocode listings entirely -- and no check noticed, because the stale
file was internally consistent and carried all the numbers.

``check_paper_numbers.py`` cannot catch this: a condensed translation can still
quote every headline figure. What distinguishes the two is prose volume per
section, so that is what is asserted here, along with the structural inventory.

Prose volume is compared as Chinese characters per English word. Faithful
technical translation lands between roughly 1.4 and 2.7; the stale edition sat
at 0.49 for the pipeline section and 0.52 for the one-expression section, which
is what dropping a pseudocode listing looks like from the outside. The floor is
set at 1.0 -- comfortably below every healthy section, comfortably above both
condensed ones.

    python experiments/check_zh_coverage.py
"""

from __future__ import annotations

import re
import sys
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
TEX = ROOT / "paper" / "tact.tex"
ZH = ROOT / "paper" / "tact_zh.md"

RATIO_FLOOR = 1.0
MIN_WORDS = 60  # below this a ratio is noise, not signal

# Three sections are exempt, none of them prose. The symbol appendix is a table
# of LaTeX symbols, the availability section is mostly URLs, and the
# bibliography is author names; in each the English word count is inflated by
# material that has no Chinese counterpart by design.
EXEMPT = {"Notation", "Code and Data Availability", "References"}

# Headings the Chinese edition adds because Markdown has no float: each
# pseudocode listing becomes its own heading. They are inventory, not sections,
# and are counted separately below.
ALG_HEADING = re.compile(r"^演算法\s*\d+")

# The header row build_zh_doc.sh keys on when it widens a pseudocode table.
LISTING_HEAD = re.compile(r"^\|\s*行\s*\|\s*完整偽程式碼\s*\|\s*說明\s*\|")


def en_sections() -> list[tuple[str, int]]:
    s = TEX.read_text()
    abstract = s[s.index(r"\begin{abstract}"):s.index(r"\end{abstract}")]
    marks = [(m.start(), m.group(2)) for m in
             re.finditer(r"\\(section|subsection)\*?\{([^}]*)", s)]
    out = [("Abstract", words(abstract))]
    for i, (pos, name) in enumerate(marks):
        end = marks[i + 1][0] if i + 1 < len(marks) else len(s)
        out.append((re.sub(r"\\label\{[^}]*\}", "", name).strip(), words(s[pos:end])))
    # Neither the abstract nor the bibliography is a \section, but the Chinese
    # edition gives both a heading, so both are added here or the lists cannot
    # be paired positionally.
    bib = s[s.index(r"\begin{thebibliography}"):]
    out.append(("References", words(bib)))
    return out


def words(body: str) -> int:
    body = re.sub(r"(?m)^\s*%.*$", "", body)
    body = re.sub(r"\\[a-zA-Z@]+\*?(\[[^\]]*\])?", " ", body)
    body = re.sub(r"[{}$&\\_^~]", " ", body)
    return len(re.findall(r"[A-Za-z][A-Za-z'-]+", body))


def zh_sections() -> tuple[list[tuple[str, int]], list[str]]:
    """Sections of the Chinese edition, with pseudocode headings folded in.

    A listing's heading is inventory rather than structure, but its body is
    still that section's content: in the English source the listing floats
    inside the section that introduces it. Charging it to its own heading would
    subtract it from the section it belongs to and make a complete translation
    read as a condensed one.
    """
    s = ZH.read_text()
    marks = [(m.start(), m.group(2).strip()) for m in
             re.finditer(r"(?m)^(#{2,3}) (.+)$", s)]
    sections: list[list] = []
    algs: list[str] = []
    for i, (pos, name) in enumerate(marks):
        end = marks[i + 1][0] if i + 1 < len(marks) else len(s)
        chars = len(re.findall(r"[\u4e00-\u9fff]", s[pos:end]))
        if ALG_HEADING.match(name):
            algs.append(name)
            if sections:
                sections[-1][1] += chars
            continue
        sections.append([name, chars])
    return [(n, c) for n, c in sections], algs


def en_tables() -> list[int]:
    """Data-row count of each English table, header included."""
    out = []
    for body in re.findall(r"\\begin\{table\*?\}(?:\[[^\]]*\])?(.*?)\\end\{table\*?\}",
                           TEX.read_text(), re.S):
        out.append(len([l for l in body.split(r"\\") if "&" in l]))
    return sorted(out)


def zh_tables() -> tuple[list[int], list[int]]:
    """Heights of the Chinese tables, split into body tables and listings.

    A pseudocode listing is identified by its header row rather than by
    position or height. Position is wrong because the listings sit mid-document
    while the symbol appendix comes last, and height is wrong because the
    symbol table is taller than either listing -- picking "the two tallest"
    silently swapped the appendix for a listing. The header is the same key
    ``build_zh_doc.sh`` uses to widen these tables, so the two agree by
    construction.
    """
    body, listings, cur, head = [], [], 0, ""
    for line in ZH.read_text().split("\n"):
        stripped = line.strip()
        if stripped.startswith("|"):
            if not re.match(r"^\|[\s:|-]+\|$", stripped):
                if cur == 0:
                    head = stripped
                cur += 1
            continue
        if cur:
            (listings if LISTING_HEAD.match(head) else body).append(cur)
            cur, head = 0, ""
    if cur:
        (listings if LISTING_HEAD.match(head) else body).append(cur)
    return sorted(body), sorted(listings)


def en_alg_steps() -> list[int]:
    return sorted(body.count(r"\State") for body in
                  re.findall(r"\\begin\{algorithm\}(.*?)\\end\{algorithm\}",
                             TEX.read_text(), re.S))


def main() -> int:
    bad: list[str] = []
    EN, (CN, algs) = en_sections(), zh_sections()

    if len(EN) != len(CN):
        bad.append(f"section count: tact.tex has {len(EN)}, tact_zh.md has {len(CN)}")
        for i, (a, b) in enumerate(zip(EN, CN)):
            print(f"   {i:2d}  {a[0][:44]:46s} {b[0][:30]}")
    else:
        print(f"   {len(EN)} sections paired, plus {len(algs)} pseudocode listings")
        for (en, w), (cn, c) in zip(EN, CN):
            if w < MIN_WORDS or en in EXEMPT:
                continue
            ratio = c / w
            mark = "" if ratio >= RATIO_FLOOR else "   <-- condensed"
            if ratio < RATIO_FLOOR:
                bad.append(f"{en} -> {cn}: {c} chars for {w} words "
                           f"(ratio {ratio:.2f} < {RATIO_FLOOR})")
            print(f"   {ratio:5.2f}  {en[:40]:42s} -> {cn[:26]}{mark}")

    # Every English table needs a Chinese one of the same height, and each
    # English algorithm needs a Chinese listing at least as long.
    et, steps = en_tables(), en_alg_steps()
    body_rows, listing_rows = zh_tables()
    if body_rows != et:
        bad.append(f"table heights differ: tact.tex {et}, tact_zh.md {body_rows}")
    else:
        print(f"   {len(et)} tables match on height: {et}")

    if len(listing_rows) != len(steps):
        bad.append(f"pseudocode listings: {len(steps)} in tact.tex, "
                   f"{len(listing_rows)} tables in tact_zh.md")
    else:
        for rows, n in zip(listing_rows, steps):
            if rows < n:
                bad.append(f"pseudocode listing truncated: {rows} rows "
                           f"for {n} \\State lines")
        print(f"   {len(steps)} pseudocode listings, rows {listing_rows} "
              f">= \\State counts {steps}")

    n_en = len(re.findall(r"\\bibitem", TEX.read_text()))
    n_zh = len(set(re.findall(r"#ref(\d+)", ZH.read_text())))
    if n_en != n_zh:
        bad.append(f"references: {n_en} bibitems, {n_zh} anchors in tact_zh.md")
    else:
        print(f"   {n_en} references anchored")

    if bad:
        print(f"\n{len(bad)} coverage failure(s):", file=sys.stderr)
        for b in bad:
            print(f"  {b}", file=sys.stderr)
        return 1
    print("\nthe Chinese edition covers the English paper")
    return 0


if __name__ == "__main__":
    sys.exit(main())
