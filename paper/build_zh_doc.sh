#!/usr/bin/env bash
# Build a Chinese markdown document to .docx and .pdf.
#
# The PDF path needs a detour: pandoc's usual --pdf-engine=xelatex is not
# available here, and tectonic has no CJK setup of its own, so we emit
# standalone LaTeX, inject xeCJK with a system font, and compile that.
#
# The intermediate .tex is written next to the source rather than in a temp
# directory, because relative \includegraphics paths (figs/...) resolve
# against the input file's location. Compiling elsewhere silently loses every
# figure -- which is how this script first failed.
#
# Errors are NOT suppressed. A missing glyph renders as a black box rather
# than an error, so eyeball the result too.
#
#   ./build_zh_doc.sh tact_parameters_zh
set -euo pipefail

BASE="${1:?usage: build_zh_doc.sh <basename-without-extension>}"
CJK_FONT="${CJK_FONT:-Songti SC}"
cd "$(dirname "$0")"

pandoc "${BASE}.md" -o "${BASE}.docx"

# Pandoc gives a three-column Markdown table a 40/30/30 DOCX grid even when
# its first column only contains line numbers.  That left less than 1.7 in for
# the pseudocode and caused long equations to be visually clipped by Word and
# LibreOffice.  Rebalance only the explicitly identified algorithm tables;
# all other document tables retain Pandoc's widths.
python3 - "${BASE}.docx" <<'PY'
import sys

from docx import Document
from docx.oxml import OxmlElement
from docx.oxml.ns import qn
from docx.shared import Inches

path = sys.argv[1]
doc = Document(path)
widths_in = (0.35, 3.90, 1.25)
widths_dxa = tuple(round(width * 1440) for width in widths_in)

for table in doc.tables:
    if not table.rows or len(table.rows[0].cells) != 3:
        continue
    headings = [cell.text.strip() for cell in table.rows[0].cells]
    if headings != ["行", "完整偽程式碼", "說明"]:
        continue

    table.autofit = False
    for grid_col, width in zip(table._tbl.tblGrid.gridCol_lst, widths_dxa):
        grid_col.set(qn("w:w"), str(width))

    for row in table.rows:
        tr_pr = row._tr.get_or_add_trPr()
        if tr_pr.find(qn("w:cantSplit")) is None:
            tr_pr.append(OxmlElement("w:cantSplit"))

        for cell, width_in, width_dxa in zip(row.cells, widths_in, widths_dxa):
            cell.width = Inches(width_in)
            tc_pr = cell._tc.get_or_add_tcPr()
            tc_w = tc_pr.find(qn("w:tcW"))
            if tc_w is None:
                tc_w = OxmlElement("w:tcW")
                tc_pr.append(tc_w)
            tc_w.set(qn("w:w"), str(width_dxa))
            tc_w.set(qn("w:type"), "dxa")

doc.save(path)
PY
echo "wrote ${BASE}.docx"

TEX="._${BASE}_zhbuild.tex"
OUTDIR="$(mktemp -d)"
cleanup() { rm -f "$TEX"; rm -rf "$OUTDIR"; }
trap cleanup EXIT

pandoc "${BASE}.md" -s -o "$TEX" -V geometry:margin=2.2cm -V fontsize=11pt

python3 - "$TEX" "$CJK_FONT" <<'PY'
import sys
path, font = sys.argv[1], sys.argv[2]
s = open(path).read()

# Pandoc infers 40/30/30 widths from the Markdown alignment row used by the
# two pseudocode tables.  In PDF that turns the line-number column into a
# large empty block and squeezes the actual algorithm into 30% of the page.
# Keep both Algorithm 1 and Algorithm 2 as separate blocks, but give their
# line/code/comment columns proportions that match a conventional algorithmic
# layout.  Require exactly two replacements so a future source change cannot
# silently reintroduce the defect.
algorithm_columns = r"""  >{\raggedleft\arraybackslash}p{(\linewidth - 4\tabcolsep) * \real{0.4000}}
  >{\raggedright\arraybackslash}p{(\linewidth - 4\tabcolsep) * \real{0.3000}}
  >{\raggedright\arraybackslash}p{(\linewidth - 4\tabcolsep) * \real{0.3000}}@{}}"""
balanced_algorithm_columns = r"""  >{\raggedleft\arraybackslash}p{(\linewidth - 4\tabcolsep) * \real{0.0600}}
  >{\raggedright\arraybackslash}p{(\linewidth - 4\tabcolsep) * \real{0.6200}}
  >{\raggedright\arraybackslash}p{(\linewidth - 4\tabcolsep) * \real{0.3200}}@{}}"""
algorithm_count = s.count(algorithm_columns)
if algorithm_count != 2:
    raise RuntimeError(
        f"expected two algorithm tables, found {algorithm_count}; "
        "update the PDF column-width transform"
    )
s = s.replace(algorithm_columns, balanced_algorithm_columns)

cjk = (
    "\n\\usepackage{xeCJK}\n"
    f"\\setCJKmainfont{{{font}}}\n"
    f"\\setCJKsansfont{{{font}}}\n"
    f"\\setCJKmonofont{{{font}}}\n"
    '\\XeTeXlinebreaklocale "zh"\n'
    "\\XeTeXlinebreakskip = 0pt plus 1pt\n"
    # figures are optional in these documents; a missing one should not abort
    "\\usepackage{graphicx}\n\\graphicspath{{./}{figs/}}\n"
    # Pin figures where they are written. Markdown has no notion of a float,
    # and letting them float collided with pandoc's longtable output: the
    # page could not be broken, an overfull \\vbox pushed material past the
    # page bottom, and a section heading plus most of a paragraph vanished
    # from the PDF without the build failing.
    "\\usepackage{float}\n\\floatplacement{figure}{H}\n"
)
open(path, "w").write(s.replace("\\begin{document}", cjk + "\n\\begin{document}", 1))
PY

if ! tectonic "$TEX" --outdir "$OUTDIR" --keep-logs >/dev/null 2>"$OUTDIR/err"; then
    echo "PDF build FAILED for ${BASE}:" >&2
    grep -i -m 5 "^error" "$OUTDIR/err" >&2 || tail -20 "$OUTDIR/err" >&2
    exit 1
fi

# An overfull \vbox during \output means material was pushed off the page.
# tectonic exits 0 on it, and the lost text is invisible in the PDF, so this
# has to be checked explicitly rather than left to the eye.
if grep -q 'Overfull \\vbox.*\\output is active' "$OUTDIR/err"; then
    echo "PDF build FAILED for ${BASE}: content pushed off a page" >&2
    grep -m 3 'Overfull \\vbox' "$OUTDIR/err" >&2
    exit 1
fi
cp "$OUTDIR/$(basename "$TEX" .tex).pdf" "${BASE}.pdf"
echo "wrote ${BASE}.pdf ($(du -h "${BASE}.pdf" | cut -f1))"
