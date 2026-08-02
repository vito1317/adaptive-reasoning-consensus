#!/usr/bin/env python3
"""Convert tact.tex (IEEEtran, two-column) to the TMLR style, single column.

TMLR anonymises by default: with no package option the title block prints
"Anonymous authors / Paper under double-blind review", which is what a
submission needs. Passing ``preprint`` restores the author block for arXiv.
Both are produced here.

The conversion is mechanical but not trivial, because column-relative lengths
change meaning when the layout goes single-column: ``\\columnwidth`` figures
would span the full text block at roughly twice their intended size.

    python paper/build_tmlr.py            # writes tact_tmlr.tex and _preprint
"""

from __future__ import annotations

import pathlib
import re

from cite_convert import convert_citations

HERE = pathlib.Path(__file__).resolve().parent

PREAMBLE = r"""\documentclass{article}
%(opt)s
\usepackage{amsmath,amssymb,amsthm}
\usepackage{graphicx}
\usepackage{booktabs}
\usepackage{multirow}
\usepackage{algorithm}
\usepackage[noend]{algpseudocode}
\usepackage{url}
\usepackage[hidelinks,breaklinks=true]{hyperref}

\newtheorem{proposition}{Proposition}
\newtheorem{remark}{Remark}

\newcommand{\Dhat}{\widehat{D}}
\newcommand{\sign}{\operatorname{sign}}
\newcommand{\SC}{\textsc{sc}}
\newcommand{\TACT}{\textsc{tact}}

\title{TACT: Trust-Anchored Confidence Tempering for\\ Self-Consistency Voting
in Large Language Models}

\author{\name Wei-Chen Ko (\begin{CJK}{UTF8}{bsmi}柯瑋宸\end{CJK}, vito1317) \email service@vito1317.com \\
        \addr Independent Researcher}

\def\month{08}
\def\year{2026}
\def\openreview{\url{https://openreview.net/forum?id=XXXXXXXXXX}}

\begin{document}
\maketitle
"""


def convert(src: str, preprint: bool) -> str:
    s = src

    # --- preamble and title block -------------------------------------
    body_start = s.index(r"\begin{abstract}")
    body = s[body_start:]
    opt = r"\usepackage[preprint]{tmlr}" if preprint else r"\usepackage{tmlr}"
    if preprint:
        head = PREAMBLE % {"opt": opt}
        head = head.replace(r"\def\openreview{\url{https://openreview.net/forum?id=XXXXXXXXXX}}",
                            r"\def\openreview{}")
    else:
        # anonymous submission: tmlr.sty replaces the author block itself, but
        # the CJK name must not survive into it
        head = PREAMBLE % {"opt": opt}
        head = re.sub(r"\\author\{.*?\\addr Independent Researcher\}",
                      r"\\author{\\name Anonymous \\email anon@example.com \\\\ \\addr Anonymous}",
                      head, flags=re.S)
    s = head + body

    # --- strip IEEE-only constructs -----------------------------------
    s = s.replace(r"\begin{IEEEkeywords}", r"\noindent\textbf{Keywords:} ")
    s = s.replace(r"\end{IEEEkeywords}", "")
    s = s.replace("\\balance\n", "")
    s = re.sub(r"\\IEEEauthorblock[NA]\{", "{", s)

    # --- single column: column-relative lengths become text-relative ---
    # a figure sized to a two-column measure must not grow to the full block
    s = s.replace(r"\includegraphics[width=\columnwidth]",
                  r"\includegraphics[width=0.62\linewidth]")
    s = s.replace(r"\columnwidth", r"\linewidth")
    # table/figure star environments are meaningless outside two-column
    s = re.sub(r"\\(begin|end)\{(table|figure)\*\}", r"\\\1{\2}", s)
    # centre the floats that were column-width by construction
    s = s.replace(r"\begin{figure}[t]" + "\n" + r"\centering",
                  r"\begin{figure}[t]" + "\n" + r"\centering")

    # --- CJK in the author name needs a package when it is shown -------
    if preprint:
        # CJKutf8 needs a bsmi font that this TeX tree does not have, and it
        # DROPS the characters silently rather than failing, which left the
        # first line of the preprint reading "Wei-Chen Ko (, vito1317)". Load a
        # Unicode system font directly instead, the way the IEEE build does.
        s = s.replace(r"\usepackage{graphicx}",
                      "\\usepackage{graphicx}\n"
                      '\\font\\zhfont="[/System/Library/Fonts/Supplemental/Arial Unicode.ttf]" at 11pt')
        s = re.sub(r"\\begin\{CJK\}\{UTF8\}\{bsmi\}(.*?)\\end\{CJK\}",
                   lambda m: "{\\zhfont " + m.group(1) + "}", s)
    else:
        s = re.sub(r"\\begin\{CJK\}\{UTF8\}\{bsmi\}(.*?)\\end\{CJK\}", "", s)

    # --- availability section identifies the author; drop it when blind
    if not preprint:
        s = re.sub(
            r"\\section\*\{Code and Data Availability\}.*?(?=\\section\{Conclusion\}|\\begin\{thebibliography\})",
            "\\\\section*{Code and Data Availability}\n"
            "All code, cached traces, and the JSON artifacts behind every table are\n"
            "provided as anonymized supplementary material; the repository will be\n"
            "de-anonymized on acceptance.\n\n",
            s, flags=re.S)

    # --- citation commands ------------------------------------------
    # tmlr.bst is an author-year style, in which plain \cite emits an
    # unbracketed "Wang et al. (2023)" mid-sentence. cite_convert picks the
    # right command per site; see that module for why it is not a one-liner.
    s = convert_citations(s)

    # --- bibliography: TMLR's natbib runs in author-year mode, which a manual
    # numeric thebibliography cannot satisfy. Switch to bibtex with tmlr.bst;
    # references.bib carries the same 27 keys, all verified against the
    # literature.
    # NOTE: a lambda, not a template string. re.sub processes escapes in the
    # replacement, and \b there means backspace, which silently injected a
    # control character into the .tex and broke the build with an
    # "invalid character" a few hundred lines away from the cause.
    s = re.sub(r"\\begin\{thebibliography\}.*?\\end\{thebibliography\}",
               lambda _: "\\bibliographystyle{tmlr}\n\\bibliography{references}",
               s, flags=re.S)
    return s


def main() -> None:
    src = (HERE / "tact.tex").read_text()
    for name, preprint in (("tact_tmlr.tex", False), ("tact_tmlr_preprint.tex", True)):
        (HERE / name).write_text(convert(src, preprint))
        print(f"wrote {name} ({'preprint, named' if preprint else 'anonymous submission'})")


if __name__ == "__main__":
    main()
