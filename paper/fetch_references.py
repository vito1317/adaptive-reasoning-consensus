#!/usr/bin/env python
"""Download the open-access PDFs for every verified reference.

Sources are arXiv, the ACL Anthology, PubMed Central and the NeurIPS
proceedings -- all of which publish these papers openly. Paywalled entries
(Kish's book, the 1979 JRSS-C and 1981 JASA articles, van Elteren 1960) have
no legitimate open copy and are recorded as such rather than sourced from
scan-hosting sites.

    python paper/fetch_references.py            # download missing only
    python paper/fetch_references.py --force    # re-download everything
"""

from __future__ import annotations

import argparse
import json
import time
import urllib.error
import urllib.request
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
VERIF = ROOT / "results" / "reference_verification.json"
OUT = ROOT / "paper" / "refs_pdf"
UA = "Mozilla/5.0 (compatible; academic-reference-archiver/1.0)"

#: Where the canonical open-access link does not serve a PDF to a script.
#: PMC returns an interstitial HTML page for direct /pdf/ requests, and
#: OpenReview answers 403; both works are on arXiv, so use that instead.
FALLBACK = {
    "parisi2014ranking": "https://arxiv.org/pdf/1303.3257",
    "xiong2024can": "https://arxiv.org/pdf/2306.13063",
}


def fetch(url: str, dest: Path, timeout: int = 60) -> tuple[bool, str]:
    req = urllib.request.Request(url, headers={"User-Agent": UA})
    try:
        with urllib.request.urlopen(req, timeout=timeout) as r:
            data = r.read()
    except urllib.error.HTTPError as e:
        return False, f"HTTP {e.code}"
    except Exception as e:  # network, TLS, timeout
        return False, type(e).__name__
    if not data.startswith(b"%PDF"):
        return False, f"not a PDF ({data[:16]!r})"
    dest.write_bytes(data)
    return True, f"{len(data)/1024:.0f} KB"


def main():
    ap = argparse.ArgumentParser()
    ap.add_argument("--force", action="store_true")
    args = ap.parse_args()

    refs = json.loads(VERIF.read_text())
    OUT.mkdir(exist_ok=True)
    have, miss, failed = [], [], []

    for r in sorted(refs, key=lambda x: x["key"]):
        key, url = r["key"], (r.get("pdf_url") or "").strip()
        dest = OUT / f"{key}.pdf"
        if not url:
            miss.append(key)
            print(f"  --   {key:26s} no open-access copy")
            continue
        if dest.exists() and not args.force:
            have.append(key)
            print(f"  ok   {key:26s} cached ({dest.stat().st_size/1024:.0f} KB)")
            continue
        ok, info = fetch(url, dest)
        if not ok and key in FALLBACK:
            time.sleep(1.0)
            ok, info2 = fetch(FALLBACK[key], dest)
            info = f"{info2} (via arXiv fallback)" if ok else f"{info}; fallback {info2}"
        if ok:
            have.append(key)
            print(f"  ok   {key:26s} {info}")
        else:
            failed.append((key, url, info))
            print(f"  FAIL {key:26s} {info}  {url}")
        time.sleep(1.0)  # be polite to the hosts

    print(f"\ndownloaded/cached: {len(have)}  |  no open copy: {len(miss)}  |  failed: {len(failed)}")
    if failed:
        print("failed (retry or source manually):")
        for k, u, i in failed:
            print(f"  {k}: {i}  {u}")
    (OUT / "MANIFEST.json").write_text(json.dumps(
        {"downloaded": have, "no_open_access": miss,
         "failed": [{"key": k, "url": u, "reason": i} for k, u, i in failed]},
        indent=1))


if __name__ == "__main__":
    main()
