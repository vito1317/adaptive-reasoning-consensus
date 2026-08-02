#!/usr/bin/env python3
"""Convert tact.tex (IEEEtran, two-column) to the JMLR style, single column.

JMLR reviews single-blind, so there is no anonymous variant here: the author
block stays, and so does the real repository URL in the availability section.
That is the one substantive difference from build_tmlr.py, which has to
produce a blinded submission alongside its named preprint.

    python paper/build_jmlr.py        # writes tact_jmlr.tex
"""

from __future__ import annotations

import pathlib
import re

from cite_convert import convert_citations

HERE = pathlib.Path(__file__).resolve().parent

PREAMBLE = r"""\documentclass[twoside,11pt]{article}

% jmlr2e loads natbib, graphicx, amssymb and hyperref itself, and defines both
% theorem environments this paper uses (proposition, remark) off one shared
% counter, plus its own \proof. Loading amsthm on top of it is a hard clash:
% "Command \proof already defined". Every cross-reference here is symbolic
% (\ref{prop:...}), so the shared counter renumbers without breaking anything.
\usepackage{amsmath}
\usepackage{jmlr2e}
\usepackage{booktabs}
\usepackage{multirow}
\usepackage{algorithm}
\usepackage[noend]{algpseudocode}
\font\zhfont="[/System/Library/Fonts/Supplemental/Arial Unicode.ttf]" at 11pt

% JMLR's measure is narrower than TMLR's at 11pt, and two paragraphs carrying
% long inline math overflowed the right margin. These are typographic knobs,
% not edits to the text: the paragraphs stay byte-identical to the other
% builds. \binoppenalty lets a long inline formula break after an operator
% (the default 700 made TeX prefer a 34pt overflow to a break at \cdot).
\emergencystretch=3em
\binoppenalty=300
\relpenalty=250

\newcommand{\Dhat}{\widehat{D}}
\newcommand{\sign}{\operatorname{sign}}
\newcommand{\SC}{\textsc{sc}}
\newcommand{\TACT}{\textsc{tact}}

\ShortHeadings{Trust-Anchored Confidence Tempering}{Ko}
\firstpageno{1}

\begin{document}

\title{TACT: Trust-Anchored Confidence Tempering for\\
       Self-Consistency Voting in Large Language Models}

\author{\name Wei-Chen Ko ({\zhfont 柯瑋宸}, vito1317) \email service@vito1317.com \\
        \addr Independent Researcher (corresponding author)}

% No action editor exists before submission, and jmlr2e prints the label
% unconditionally, which leaves a dangling "Editor:" on the title page.
% Blanking the label is presentation-only: once an editor is assigned, delete
% this patch and put the name in \editor{}.
\makeatletter
\def\@starteditor{}
\makeatother
\editor{}

\maketitle
"""


def convert(src: str) -> str:
    s = PREAMBLE + src[src.index(r"\begin{abstract}"):]

    # --- strip IEEE-only constructs -----------------------------------
    s = s.replace(r"\begin{IEEEkeywords}", r"\noindent\textbf{Keywords:} ")
    s = s.replace(r"\end{IEEEkeywords}", "")
    s = s.replace("\\balance\n", "")
    s = re.sub(r"\\IEEEauthorblock[NA]\{", "{", s)

    # --- single column: column-relative lengths become text-relative ---
    s = s.replace(r"\includegraphics[width=\columnwidth]",
                  r"\includegraphics[width=0.62\linewidth]")
    s = s.replace(r"\columnwidth", r"\linewidth")
    s = re.sub(r"\\(begin|end)\{(table|figure)\*\}", r"\\\1{\2}", s)
    # the test-suite table's p-columns are hard-coded to a two-column measure
    # (7.8cm); left alone they occupy half of JMLR's 6in block and wrap hard
    s = s.replace(r"\begin{tabular}{p{3.0cm} p{4.8cm}}",
                  r"\begin{tabular}{p{5.2cm} p{9.2cm}}")

    # --- CJK name: CJKutf8 needs a bsmi font this TeX tree lacks, and drops
    # the characters silently rather than failing. Load a Unicode system font
    # directly, the way the IEEE build does.
    s = re.sub(r"\\begin\{CJK\}\{UTF8\}\{bsmi\}(.*?)\\end\{CJK\}",
               lambda m: "{\\zhfont " + m.group(1) + "}", s)

    # --- citation commands --------------------------------------------
    # jmlr2e runs natbib in author-year mode, where plain \cite emits an
    # unbracketed "Wang et al. (2023)" mid-sentence. cite_convert picks the
    # right command per site; see that module for why it is not a one-liner.
    s = convert_citations(s)

    # --- bibliography: a manual numeric thebibliography cannot satisfy
    # author-year natbib. Switch to bibtex; jmlr2e sets its own style, and
    # references.bib carries the same keys, all verified against the
    # literature.
    # NOTE: a lambda, not a template string. re.sub processes escapes in the
    # replacement, and \b there means backspace.
    s = re.sub(r"\\begin\{thebibliography\}.*?\\end\{thebibliography\}",
               lambda _: "\\bibliography{references}", s, flags=re.S)
    return s


def main() -> None:
    src = (HERE / "tact.tex").read_text()
    (HERE / "tact_jmlr.tex").write_text(convert(src))
    print("wrote tact_jmlr.tex (JMLR submission; single-blind, author shown)")


if __name__ == "__main__":
    main()
