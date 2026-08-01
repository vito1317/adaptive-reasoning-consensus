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
cjk = (
    "\n\\usepackage{xeCJK}\n"
    f"\\setCJKmainfont{{{font}}}\n"
    f"\\setCJKsansfont{{{font}}}\n"
    f"\\setCJKmonofont{{{font}}}\n"
    '\\XeTeXlinebreaklocale "zh"\n'
    "\\XeTeXlinebreakskip = 0pt plus 1pt\n"
    # figures are optional in these documents; a missing one should not abort
    "\\usepackage{graphicx}\n\\graphicspath{{./}{figs/}}\n"
)
open(path, "w").write(s.replace("\\begin{document}", cjk + "\n\\begin{document}", 1))
PY

if ! tectonic "$TEX" --outdir "$OUTDIR" --keep-logs >/dev/null 2>"$OUTDIR/err"; then
    echo "PDF build FAILED for ${BASE}:" >&2
    grep -i -m 5 "^error" "$OUTDIR/err" >&2 || tail -20 "$OUTDIR/err" >&2
    exit 1
fi
cp "$OUTDIR/$(basename "$TEX" .tex).pdf" "${BASE}.pdf"
echo "wrote ${BASE}.pdf ($(du -h "${BASE}.pdf" | cut -f1))"
