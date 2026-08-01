#!/usr/bin/env python
"""Build a clickable reference guide (Word + PDF) from the verified bibliography.

Reads results/reference_verification.json -- the output of the verification
pass, which checked every entry against the live literature and recorded the
canonical landing page plus an open-access PDF where one exists -- and emits a
navigable document: one row per citation, grouped by role in the paper, with
the key, the full reference, and live links.

    python paper/build_references_doc.py
"""

from __future__ import annotations

import json
import re
import subprocess
import sys
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
VERIF = ROOT / "results" / "reference_verification.json"
BIB = ROOT / "paper" / "references.bib"
TEX = ROOT / "paper" / "tact.tex"
OUT_MD = ROOT / "paper" / "references_guide.md"

#: Where each citation does its work in the paper. Keys not listed fall into
#: "其他"; the grouping is for navigation, not a claim about the literature.
GROUPS = [
    ("自我一致性與信心加權", [
        "wang2023selfconsistency", "taubenfeld2025cisc", "li2023diverse", "borda2025",
        "deepconf2025", "reasc2026", "rasc2024", "beyondmajority2025",
    ]),
    ("自適應取樣與提早停止", ["aggarwal2023adaptive", "li2024escape"]),
    ("信心引出與校準", [
        "kadavath2022language", "tian2023just", "xiong2024can",
        "huang2024rankcalibration", "kuhn2023semantic",
    ]),
    ("無標籤可靠度估計", [
        "dawid1979maximum", "whitehill2009whose", "karger2011iterative",
        "parisi2014ranking", "fuse2026",
    ]),
    ("統計方法（收縮、秩統計、抽樣設計）", [
        "vanelteren1960", "james1961estimation", "kish1965", "rao1981analysis",
    ]),
    ("資料集", ["math500", "leetcodedataset"]),
]


def cite_counts() -> dict[str, int]:
    """How many times each key is cited in the paper."""
    txt = TEX.read_text()
    keys = [k.strip() for grp in re.findall(r"\\cite\{([^}]*)\}", txt) for k in grp.split(",")]
    return {k: keys.count(k) for k in set(keys)}


def fmt_authors(a: str, limit: int = 4) -> str:
    parts = [p.strip() for p in re.split(r"\s+and\s+", a) if p.strip()]
    if len(parts) > limit:
        return ", ".join(parts[:limit]) + " 等"
    return ", ".join(parts)


def main():
    if not VERIF.exists():
        sys.exit(f"missing {VERIF} -- run the verification pass first")
    refs = {r["key"]: r for r in json.loads(VERIF.read_text())}
    counts = cite_counts()

    listed = {k for _, ks in GROUPS for k in ks}
    extra = sorted(set(refs) - listed)
    groups = GROUPS + ([("其他", extra)] if extra else [])

    L: list[str] = []
    L.append("# TACT 論文參考文獻導覽\n")
    L.append("**作者：柯瑋宸（vito1317）**\n")
    L.append(
        f"全部 {len(refs)} 筆文獻皆已對照實際文獻查證：確認存在、核對標題與作者、"
        "更正出處，並附上正式頁面與（若為開放取用）PDF 直連。\n"
    )
    n_pdf = sum(1 for r in refs.values() if r.get("pdf_url"))
    n_bad = sum(1 for r in refs.values() if r.get("status") != "VERIFIED")
    L.append(
        f"- 可直接下載 PDF：**{n_pdf}/{len(refs)}**\n"
        f"- 原始 BibTeX 有誤需更正：**{n_bad}** 筆（詳見各條目的「更正」）\n"
        f"- 論文中的引用次數標示於每筆之後\n"
    )

    for title, keys in groups:
        keys = [k for k in keys if k in refs]
        if not keys:
            continue
        L.append(f"\n## {title}\n")
        for k in keys:
            r = refs[k]
            n = counts.get(k, 0)
            cited = f"（引用 {n} 次）" if n else "（未引用）"
            L.append(f"### `{k}` {cited}\n")
            L.append(f"**{r['correct_title']}**  ")
            L.append(f"{fmt_authors(r['correct_authors'])}  ")
            L.append(f"*{r['correct_venue']}*, {r['correct_year']}  ")
            links = []
            if r.get("canonical_url"):
                links.append(f"[正式頁面]({r['canonical_url']})")
            if r.get("pdf_url"):
                links.append(f"[PDF 直連]({r['pdf_url']})")
            if r.get("doi"):
                links.append(f"[DOI](https://doi.org/{r['doi']})")
            if links:
                L.append(" · ".join(links) + "  ")
            if r.get("status") != "VERIFIED" or r.get("problems") not in ("none", "", None):
                L.append(f"\n> **更正**：{r['problems']}  ")
            L.append("")

    OUT_MD.write_text("\n".join(L))
    print(f"wrote {OUT_MD}")
    subprocess.run(["bash", str(ROOT / "paper" / "build_zh_doc.sh"), "references_guide"], check=True)


if __name__ == "__main__":
    main()
