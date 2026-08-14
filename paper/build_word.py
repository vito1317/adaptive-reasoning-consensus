#!/usr/bin/env python3
"""Regenerate tact_word.tex (pandoc-friendly) from tact.tex, deterministically."""
import pathlib
import subprocess
import re
import os
import tempfile
import zipfile


def resolve_citations(s: str) -> str:
    """Turn ``\\cite{key}`` into a numbered link and anchor each ``\\bibitem``.

    pandoc's LaTeX reader drops ``\\cite`` when no .bib database is supplied,
    which left the Word export with no in-text citation markers at all, and it
    gives ``\\bibitem`` no anchor, so nothing could be linked to even if the
    markers had survived.

    Both sides use \\hypertarget/\\hyperlink rather than
    \\phantomsection/\\label. The label form does produce a bookmark, but an
    EMPTY one: pandoc emits ``<w:bookmarkStart/><w:bookmarkEnd/>`` back to back
    with no run between them, and Word cannot navigate to a zero-length
    bookmark -- every [n] jumped to the first word of the document instead. All
    27 bibliography bookmarks were like that. \\hypertarget wraps visible text,
    so the bookmark has extent and the jump lands.
    """
    order = re.findall(r"\\bibitem\{([^}]+)\}", s)
    num = {k: i + 1 for i, k in enumerate(order)}

    def cite(m):
        keys = [k.strip() for k in m.group(1).split(",")]
        parts = [f"\\hyperlink{{bib:{k}}}{{{num[k]}}}" for k in keys if k in num]
        return "[" + ",".join(parts) + "]" if parts else m.group(0)

    s = re.sub(r"\\cite\{([^}]*)\}", cite, s)
    # The target wraps the entry's own number, which is the shortest piece of
    # visible text guaranteed to exist at the start of every bibitem.
    return re.sub(
        r"\\bibitem\{([^}]+)\}",
        lambda m: f"\\bibitem{{{m.group(1)}}}"
                  f"\\hypertarget{{bib:{m.group(1)}}}{{[{num[m.group(1)]}]}} ",
        s,
    )


def hoist_labels(s: str) -> str:
    """Move ``\\label`` out of environments pandoc cannot anchor, with extent.

    pandoc renders a display equation as OMML and an algorithm as a plain
    block, and attaches no bookmark to a label sitting inside either, so every
    \\eqref and every algorithm-line reference in the Word export pointed at a
    target that did not exist.

    Hoisting alone is not enough. \\phantomsection\\label produces
    ``<w:bookmarkStart/><w:bookmarkEnd/>`` with no run between, and Word cannot
    navigate to a zero-length bookmark -- it silently goes to the top of the
    document instead. \\hypertarget around a thin space gives the bookmark
    something to cover, which is the smallest visible thing that works.
    """
    def anchor(label: str) -> str:
        return f"\\hypertarget{{{label}}}{{\\,}}"

    def hoist_env(m):
        env, body = m.group(1), m.group(2)
        labels = re.findall(r"\\label\{([^}]+)\}", body)
        if not labels:
            return m.group(0)
        body = re.sub(r"\\label\{[^}]+\}", "", body)
        return "".join(anchor(l) for l in labels) + f"\n\\begin{{{env}}}{body}\\end{{{env}}}"

    s = re.sub(r"\\begin\{(equation|align)\}(.*?)\\end\{\1\}", hoist_env, s, flags=re.S)

    # Algorithm-line labels (\State ... \label{ln:x}) sit inside an
    # algorithmic block; pull each out to just before the block.
    def hoist_alg(m):
        body = m.group(1)
        labels = re.findall(r"\\label\{(ln:[^}]+)\}", body)
        alg_labels = re.findall(r"\\label\{(alg:[^}]+)\}", body)
        if not labels and not alg_labels:
            return m.group(0)
        body = re.sub(r"\\label\{(?:ln|alg):[^}]+\}", "", body)
        return ("".join(anchor(l) for l in alg_labels + labels)
                + f"\n\\begin{{algorithm}}{body}\\end{{algorithm}}")

    return re.sub(r"\\begin\{algorithm\}(.*?)\\end\{algorithm\}", hoist_alg, s, flags=re.S)


def repair_pandoc_docx(path: pathlib.Path) -> None:
    """Repair two OOXML defects emitted by the installed pandoc build.

    The package declares each PNG with an Override but omits the required
    extension-level Default.  Pandoc also serializes ``m:nor`` before
    ``m:sty`` in math run properties, whereas the WordprocessingML schema
    requires the style first.  Word is permissive about both defects; the
    package validator is not.
    """
    with zipfile.ZipFile(path, "r") as src:
        members = [(info, src.read(info.filename)) for info in src.infolist()]

    repaired: list[tuple[zipfile.ZipInfo, bytes]] = []
    for info, payload in members:
        if info.filename == "[Content_Types].xml":
            text = payload.decode("utf-8")
            if 'Default Extension="png"' not in text:
                text = text.replace(
                    '<Types xmlns="http://schemas.openxmlformats.org/package/2006/content-types">',
                    '<Types xmlns="http://schemas.openxmlformats.org/package/2006/content-types">'
                    '<Default Extension="png" ContentType="image/png" />',
                    1,
                )
            payload = text.encode("utf-8")
        elif info.filename == "word/document.xml":
            text = payload.decode("utf-8")
            # CT_RPR defines normal-text (nor) and mathematical style (sty) as
            # alternatives, not an ordered pair.  Pandoc emits both for text
            # such as ``P(True)``; retain the explicit normal-text marker.
            text = re.sub(
                r"<m:rPr>\s*(?:"
                r"<m:nor\s*/>\s*<m:sty\s+m:val=\"[^\"]+\"\s*/>"
                r"|<m:sty\s+m:val=\"[^\"]+\"\s*/>\s*<m:nor\s*/>)"
                r"\s*</m:rPr>",
                r"<m:rPr><m:nor/></m:rPr>",
                text,
            )

            def preserve_math_space(match: re.Match[str]) -> str:
                attrs, body = match.group(1), match.group(2)
                if body and (body[0].isspace() or body[-1].isspace()):
                    return f'<m:t{attrs} xml:space="preserve">{body}</m:t>'
                return match.group(0)

            text = re.sub(
                r"<m:t((?![^>]*xml:space)[^>]*)>([^<]*)</m:t>",
                preserve_math_space,
                text,
            )
            payload = text.encode("utf-8")
        repaired.append((info, payload))

    with tempfile.NamedTemporaryFile(
        prefix="tact-docx-", suffix=".docx", dir=path.parent, delete=False
    ) as handle:
        temp_path = pathlib.Path(handle.name)
    try:
        with zipfile.ZipFile(temp_path, "w", zipfile.ZIP_DEFLATED) as dst:
            for info, payload in repaired:
                dst.writestr(info, payload)
        os.replace(temp_path, path)
    finally:
        if temp_path.exists():
            temp_path.unlink()


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
    # pandoc cannot place a PDF figure into .docx; the paper now includes
    # figures without an extension so LaTeX takes the vector version.
    s = re.sub(r"\\includegraphics(\[[^\]]*\])?\{figs/([a-z_]+)\}",
               lambda m: f"\\includegraphics{m.group(1) or ''}{{figs/{m.group(2)}.png}}", s)
    s = hoist_labels(s)
    s = resolve_citations(s)
    pathlib.Path("tact_word.tex").write_text(s)
    print("tact_word.tex regenerated")

    # The pandoc step used to live only in shell history, so tact.docx could
    # silently lag tact.tex. --resource-path lets \includegraphics{figs/...}
    # resolve when pandoc is invoked from anywhere.
    subprocess.run(
        ["pandoc", "tact_word.tex", "-o", "tact.docx", "--resource-path=.:figs"],
        cwd=pathlib.Path(__file__).resolve().parent, check=True,
    )
    repair_pandoc_docx(pathlib.Path(__file__).resolve().parent / "tact.docx")
    print("tact.docx regenerated")


if __name__ == "__main__":
    main()
