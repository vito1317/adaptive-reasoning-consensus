#!/usr/bin/env bash
# Build a Chinese markdown document to .docx and .pdf.
#
# The PDF path needs a detour: pandoc's usual --pdf-engine=xelatex is not
# available here, and tectonic has no CJK setup of its own, so we emit
# standalone LaTeX, inject xeCJK with a system font, and compile that.
# Always eyeball the result -- a missing glyph renders as a black box rather
# than an error, which is exactly how this project once shipped unreadable
# Greek letters in a figure.
#
#   ./build_zh_doc.sh tact_parameters_zh
set -euo pipefail

BASE="${1:?usage: build_zh_doc.sh <basename-without-extension>}"
CJK_FONT="${CJK_FONT:-Songti SC}"
cd "$(dirname "$0")"

pandoc "${BASE}.md" -o "${BASE}.docx"
echo "wrote ${BASE}.docx"

TMP="$(mktemp -d)"
trap 'rm -rf "$TMP"' EXIT
pandoc "${BASE}.md" -s -o "$TMP/doc.tex" -V geometry:margin=2.2cm -V fontsize=11pt

python3 - "$TMP/doc.tex" "$CJK_FONT" <<'PY'
import sys
path, font = sys.argv[1], sys.argv[2]
s = open(path).read()
cjk = (
    "\n\\usepackage{xeCJK}\n"
    f"\\setCJKmainfont{{{font}}}\n"
    f"\\setCJKsansfont{{{font}}}\n"
    f"\\setCJKmonofont{{{font}}}\n"
    '\\XeTeXlinebreaklocale "zh"\n'
    "\\XeTeXlinebreakskip = 0pt plus 1pt\n"
)
open(path, "w").write(s.replace("\\begin{document}", cjk + "\n\\begin{document}", 1))
PY

tectonic "$TMP/doc.tex" --outdir "$TMP" >/dev/null 2>&1
cp "$TMP/doc.pdf" "${BASE}.pdf"
echo "wrote ${BASE}.pdf ($(du -h "${BASE}.pdf" | cut -f1))"
