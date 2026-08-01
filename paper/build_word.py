#!/usr/bin/env python3
"""Regenerate tact_word.tex (pandoc-friendly) from tact.tex, deterministically."""
import pathlib
import re


def resolve_citations(s: str) -> str:
    """Turn ``\\cite{key}`` into a numbered link and anchor each ``\\bibitem``.

    pandoc's LaTeX reader drops ``\\cite`` when no .bib database is supplied,
    which left the Word export with no in-text citation markers at all, and it
    gives ``\\bibitem`` no anchor, so nothing could be linked to even if the
    markers had survived. Rewriting both to ``\\hyperref``/``\\phantomsection``
    before conversion gives Word real bookmarks and working jumps.
    """
    order = re.findall(r"\\bibitem\{([^}]+)\}", s)
    num = {k: i + 1 for i, k in enumerate(order)}

    def cite(m):
        keys = [k.strip() for k in m.group(1).split(",")]
        parts = [f"\\hyperref[bib:{k}]{{{num[k]}}}" for k in keys if k in num]
        return "[" + ",".join(parts) + "]" if parts else m.group(0)

    s = re.sub(r"\\cite\{([^}]*)\}", cite, s)
    return re.sub(
        r"\\bibitem\{([^}]+)\}",
        lambda m: f"\\bibitem{{{m.group(1)}}}\\phantomsection\\label{{bib:{m.group(1)}}}",
        s,
    )


def hoist_equation_labels(s: str) -> str:
    """Move ``\\label`` out of display equations so Word can bookmark it.

    pandoc renders a display equation as OMML and attaches no bookmark to a
    label sitting inside it, so every ``\\eqref`` in the Word export pointed at
    a target that did not exist and jumped to the top of the document. Placing
    a ``\\phantomsection\\label`` in the surrounding text flow instead gives
    pandoc something it can anchor.
    """
    def hoist(m):
        env, body = m.group(1), m.group(2)
        labels = re.findall(r"\\label\{([^}]+)\}", body)
        if not labels:
            return m.group(0)
        body = re.sub(r"\\label\{[^}]+\}", "", body)
        anchors = "".join(f"\\phantomsection\\label{{{l}}}" for l in labels)
        return f"{anchors}\n\\begin{{{env}}}{body}\\end{{{env}}}"

    return re.sub(r"\\begin\{(equation|align)\}(.*?)\\end\{\1\}", hoist, s, flags=re.S)


def main() -> None:
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
    # pandoc's TeX math reader does not know \smash; strip it generally
    # rather than by matching one hard-coded body, which silently stopped
    # matching when the symbol inside it was renamed.
    s = re.sub(r"\\smash\{([^{}]*(?:\{[^{}]*\}[^{}]*)*)\}", r"\1", s)
    s = s.replace(r"\begin{abstract}", r"\section*{Abstract}").replace(r"\end{abstract}", "")
    s = s.replace("\\begin{thebibliography}{99}", "\\section*{References}\n\\begin{thebibliography}{99}")
    s = hoist_equation_labels(s)
    s = resolve_citations(s)
    pathlib.Path("tact_word.tex").write_text(s)
    print("tact_word.tex regenerated")


if __name__ == "__main__":
    main()
