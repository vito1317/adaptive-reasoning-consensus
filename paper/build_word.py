#!/usr/bin/env python3
"""Regenerate tact_word.tex (pandoc-friendly) from tact.tex, deterministically."""
import pathlib, re

s = pathlib.Path("tact.tex").read_text()
s = s.replace('\\font\\zhfont="[/System/Library/Fonts/Supplemental/Arial Unicode.ttf]" at 10pt', "")
s = s.replace(r"{\zhfont 柯瑋宸}", "柯瑋宸")
s = re.sub(
    r"\\author\{\\IEEEauthorblockN\{([^}]*)\}\s*\\IEEEauthorblockA\{(.*?)\}\}",
    lambda m: "\\author{" + m.group(1) + " \\\\ " + m.group(2) + "}",
    s, flags=re.S,
)
s = s.replace("\\begin{IEEEkeywords}", "\\textbf{Keywords---}").replace("\\end{IEEEkeywords}", "")
for pkg in (r"\usepackage[caption=false]{subfig}", r"\usepackage{balance}", r"\usepackage{multirow}"):
    s = s.replace(pkg + "\n", "")
s = s.replace("\\balance\n", "")
s = s.replace(r"\smash{\kappa_q\,c_{q,i}^{\,\gamma}}", r"\kappa_q\,c_{q,i}^{\,\gamma}")
s = s.replace(r"\begin{abstract}", r"\section*{Abstract}").replace(r"\end{abstract}", "")
s = s.replace("\\begin{thebibliography}{99}", "\\section*{References}\n\\begin{thebibliography}{99}")
pathlib.Path("tact_word.tex").write_text(s)
print("tact_word.tex regenerated")
