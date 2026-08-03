#!/usr/bin/env python
"""Every internal link in the Word exports must land somewhere.

This defect came back twice, so it gets a check. pandoc turns
\\phantomsection\\label into an EMPTY Word bookmark --
``<w:bookmarkStart/><w:bookmarkEnd/>`` with no run between them -- and Word
cannot navigate to a zero-length bookmark. It silently scrolls to the first word
of the document instead, which is what "every [n] jumps to the top" means. There
is no error, no warning, and the .docx opens fine, so nothing but an explicit
check finds it.

Two failure modes are asserted:
  dangling  a hyperlink whose anchor has no bookmark at all
  empty     a bookmark whose start and end are adjacent

    python experiments/check_docx_links.py
"""

from __future__ import annotations

import re
import sys
import zipfile
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
DOCX = ["paper/tact.docx", "paper/tact_zh.docx",
        "paper/tact_parameters_zh.docx", "paper/references_guide.docx"]

START_END = re.compile(r'<w:bookmarkStart w:id="(\d+)" w:name="([^"]+)"\s*/>\s*'
                       r'<w:bookmarkEnd w:id="\1"\s*/>')


def check(path: Path) -> tuple[int, int, int]:
    xml = zipfile.ZipFile(path).read("word/document.xml").decode("utf-8", "replace")
    marks = set(re.findall(r'<w:bookmarkStart[^>]*w:name="([^"]+)"', xml))
    links = re.findall(r'<w:hyperlink[^>]*w:anchor="([^"]*)"', xml)
    empty = [m.group(2) for m in START_END.finditer(xml)]
    dangling = sorted({l for l in links if l not in marks})
    return len(links), len(dangling), len(empty), dangling, empty


def main() -> int:
    bad = 0
    for rel in DOCX:
        p = ROOT / rel
        if not p.exists():
            print(f"  skip {rel} (not built)")
            continue
        n, nd, ne, dangling, empty = check(p)
        ok = nd == 0 and ne == 0
        print(f"{'  ' if ok else '!!'} {rel:34s} {n:4d} links, "
              f"{nd} dangling, {ne} zero-length")
        if dangling:
            print(f"     dangling: {dangling[:8]}")
        if empty:
            print(f"     zero-length: {empty[:8]}")
        bad += 0 if ok else 1
    print(f"\n{len(DOCX) - bad}/{len(DOCX)} Word exports have every internal link landing")
    return 1 if bad else 0


if __name__ == "__main__":
    sys.exit(main())
