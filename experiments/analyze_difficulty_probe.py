#!/usr/bin/env python
"""Difficulty probe: is MATH level 4-5 the right substrate for the TACT redo?

The GSM8K/CSQA real-trace experiment was uninformative because the benchmark
was saturated for the model: plurality right on 91/100 items, so the decisive
stratum (the only place any SC-improving method can act) had n=9. This probe
measures, on a 30-item stratified sample of MATH level 4-5:

  - plurality accuracy       (want ~0.4-0.7: a decisive stratum worth 30-60%)
  - gold-in-pool rate        (TACT can only help when the right answer exists
                              in the pool at all; want > 0.8)
  - within-item answer spread (K of dedup clusters; all-unique pools carry no
                              vote signal and would favour nothing)

    python experiments/analyze_difficulty_probe.py --raw results/math_probe_raw.json
"""

from __future__ import annotations

import argparse
import json
import sys
from collections import Counter
from pathlib import Path

import numpy as np

sys.path.insert(0, str(Path(__file__).resolve().parents[1] / "src"))

from rlev_voi.math_grade import canon, equivalent  # noqa: E402


def main():
    ap = argparse.ArgumentParser()
    ap.add_argument("--raw", type=Path, default=Path("results/math_probe_raw.json"))
    ap.add_argument("--items", type=Path, default=Path("data/math_pilot_items.json"))
    args = ap.parse_args()

    traces = json.loads(args.raw.read_text())["traces"]
    items = {x["qid"]: x for x in json.loads(args.items.read_text())}

    rows = []
    print(f"{'qid':10s} {'lvl':>3} {'n':>2} {'K':>2} {'plur_share':>10} {'plur_ok':>7} {'gold_in_pool':>12} {'conf_r':>6}")
    for qid, tr in traces.items():
        if not tr:
            continue
        gold = items[qid]["gold"]
        level = items[qid]["group"][-1]
        buckets = Counter(canon(t["answer"]) for t in tr)
        plur, cnt = buckets.most_common(1)[0]
        plur_ok = equivalent(plur, gold)
        gold_in = any(equivalent(b, gold) for b in buckets)
        # confidence-correctness alignment within the item (the WQD raw signal)
        confs = np.array([t.get("confidence", 0.5) for t in tr], float)
        right = np.array([equivalent(canon(t["answer"]), gold) for t in tr], float)
        conf_r = float(np.corrcoef(confs, right)[0, 1]) if 0 < right.sum() < len(right) and np.std(confs) > 0 else float("nan")
        rows.append(dict(qid=qid, level=level, n=len(tr), K=len(buckets),
                         plur_share=cnt / len(tr), plur_ok=bool(plur_ok),
                         gold_in_pool=bool(gold_in), conf_r=conf_r))
        print(f"{qid:10s} {level:>3} {len(tr):>2} {len(buckets):>2} {cnt/len(tr):>10.2f} "
              f"{str(plur_ok):>7} {str(gold_in):>12} {conf_r:>6.2f}")

    for lvl in ("4", "5"):
        sub = [r for r in rows if r["level"] == lvl]
        if not sub:
            continue
        print(f"\nlevel {lvl}: n={len(sub)}  plurality acc={np.mean([r['plur_ok'] for r in sub]):.2f}  "
              f"gold-in-pool={np.mean([r['gold_in_pool'] for r in sub]):.2f}  "
              f"mean K={np.mean([r['K'] for r in sub]):.1f}")
    dec = [r for r in rows if not r["plur_ok"]]
    rescuable = [r for r in dec if r["gold_in_pool"]]
    print(f"\nDECISIVE stratum: {len(dec)}/{len(rows)} items; of those, gold in pool "
          f"(rescuable): {len(rescuable)}/{len(dec)}")
    cr = [r["conf_r"] for r in rows if np.isfinite(r["conf_r"])]
    print(f"within-item conf-correctness corr: mean {np.mean(cr):+.3f} over {len(cr)} mixed items"
          if cr else "no mixed items with confidence variance")
    verdict = ("GO: decisive stratum >= 30% and most of it rescuable"
               if len(dec) >= 0.3 * len(rows) and len(rescuable) >= 0.5 * max(len(dec), 1)
               else "ADJUST: wrong difficulty mix -- reweight levels or change model")
    print("\n" + verdict)


if __name__ == "__main__":
    main()
