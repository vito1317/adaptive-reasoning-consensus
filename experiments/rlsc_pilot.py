#!/usr/bin/env python
"""Pilot experiments behind the RLSC/DEC design decisions (docs/GRAVEYARD.md).

Three pre-implementation measurements, run BEFORE committing to a build:

1. Mode-certification cost (pairwise betting e-process, aGRAPA bets): validity
   holds at exact ties, but certifying delta=0.05 on a (0.6, 0.3, 0.1) item
   costs ~101 samples -- an order of magnitude over typical SC budgets. This,
   plus the MMC/CITE scoops, killed the mode-certification estimand.

2. Finite-horizon certification cost ("current leader == SC@B decision"):
   deterministic layer (lead > remaining) plus an anytime CS + exact binomial
   tail. On synthetic streams the certificates are ~90% deterministic at B=12;
   the probabilistic layer only matters at larger B on skewed streams.

3. Real-trace replay (100 items x 12 Haiku samples, permutation replay):
   99/100 items certify at mean 7.3/12 samples (39% saving), zero mismatches
   at delta=0.05 -- AND the router leg dies: all 9 wrong-plurality items
   certify (stable-wrong), router TP=0 / FN=9. Certification measures
   stability, which is orthogonal to correctness exactly on the decisive
   stratum. This killed "route on non-certification" empirically, matching
   the sufficiency-of-tallies argument from the adversarial review.

KNOWN RIGOR GAPS in this pilot (deliberate -- it prices designs, it is not the
method): the flip check only tests the current runner-up, not all rivals or
unseen-answer mass; the binomial tail takes r'=r future pair-hits, which is
not always the worst case. A real implementation must fix both.

    python experiments/rlsc_pilot.py
"""

from __future__ import annotations

import json
import math
import sys
from pathlib import Path

import numpy as np
from scipy.stats import binom

sys.path.insert(0, str(Path(__file__).resolve().parents[1] / "src"))

from rlev_voi.backends import normalise_answer  # noqa: E402


# ---------------------------------------------------------------- experiment 1
def run_item_mode_cert(p, delta, B_max, rng):
    """Pairwise betting e-process for the POPULATION mode (the scooped design)."""
    K = len(p)
    logE = np.zeros((K, K))
    nab = np.zeros((K, K))
    sab = np.zeros((K, K))
    counts = np.zeros(K, int)
    thresh = np.log((K - 1) / delta)
    for t in range(1, B_max + 1):
        x = rng.choice(K, p=p)
        counts[x] += 1
        for b in range(K):
            if b == x:
                continue
            for (a2, b2, z) in ((x, b, 1.0), (b, x, 0.0)):
                q = (sab[a2, b2] + 0.5) / (nab[a2, b2] + 1.0)  # predictable
                lam = np.clip(2 * (2 * q - 1), 0.0, 1.8)
                logE[a2, b2] += np.log1p(lam * (z - 0.5))
                nab[a2, b2] += 1
                sab[a2, b2] += z
        leader = int(np.argmax(counts))
        if all(logE[leader, b] >= thresh for b in range(K) if b != leader):
            return leader, t, True
    return int(np.argmax(counts)), B_max, False


# ---------------------------------------------------------------- experiment 2
def hoeffding_cs_lo(s, n, delta):
    """Stitched anytime lower confidence bound on a Bernoulli mean."""
    if n == 0:
        return 0.0
    rad = math.sqrt(math.log((2 / delta) * (1 + math.log2(max(n, 2)))) / (2 * n))
    return max(0.0, s / n - rad)


def flip_prob_exact(L, r, q):
    """P(runner-up beats leader by > L among r future pair-hits at P(a)=q).

    PILOT SIMPLIFICATION: assumes all r remaining samples are pair-hits
    (r'=r). Not always the worst case over r' -- see module docstring.
    """
    if L >= r:
        return 0.0
    kmax = int(np.ceil((r - L) / 2.0)) - 1
    return float(binom.cdf(kmax, r, q)) if kmax >= 0 else 0.0


def replay_stream(stream, K, B, delta):
    """Finite-horizon certificate replayed over one ordered stream."""
    counts = np.zeros(K, int)
    for t in range(1, B + 1):
        counts[stream[t - 1]] += 1
        order = np.argsort(counts)[::-1]
        a = int(order[0])
        L = counts[a] - (counts[int(order[1])] if K > 1 else 0)
        r = B - t
        if L > r:
            return a, t, True
        if K > 1:
            b = int(order[1])
            nab, s2 = counts[a] + counts[b], counts[a]
            qlo = hoeffding_cs_lo(s2, nab, delta / 2)
            if qlo > 0.5 and flip_prob_exact(L, r, qlo) <= delta / 2:
                return a, t, True
    return int(np.argmax(counts)), B, False


# ---------------------------------------------------------------- experiment 3
def real_trace_replay(B=12, delta=0.05, R=400, seed=7):
    traces = json.loads(Path("data/real_traces_full.json").read_text())
    items = {x["qid"]: x for x in json.loads(Path("data/real_items.json").read_text())}
    rng = np.random.default_rng(seed)
    rows = []
    for qid, tr in traces.items():
        ans = [normalise_answer(t["answer"]) for t in tr][:B]
        labels = sorted(set(ans))
        idx = {a: i for i, a in enumerate(labels)}
        seq0 = np.array([idx[a] for a in ans])
        K = len(labels)
        scB = int(np.argmax(np.bincount(seq0, minlength=K)))
        plurality_right = labels[scB] == normalise_answer(str(items[qid]["gold"]))
        Ts, certs, mism = [], 0, 0
        for _ in range(R):
            aa, t, ok = replay_stream(seq0[rng.permutation(B)], K, B, delta)
            Ts.append(t)
            if ok:
                certs += 1
                mism += aa != scB
        rows.append(dict(qid=qid, K=K, p_cert=certs / R, mean_T=float(np.mean(Ts)),
                         mismatch=mism / max(certs, 1), plurality_right=bool(plurality_right)))
    return rows


def main():
    rng = np.random.default_rng(0)

    print("=== 1. mode certification (the SCOOPED estimand): validity + cost ===")
    for p in ([0.5, 0.5], [0.4, 0.4, 0.2]):
        cert = sum(run_item_mode_cert(np.array(p), 0.05, 300, rng)[2] for _ in range(2000))
        print(f"  tie {p}: false-cert rate {cert/2000:.4f} (must be <= 0.05)")
    for p in ((0.6, 0.3, 0.1), (0.45, 0.35, 0.2)):
        out = [run_item_mode_cert(np.array(p), 0.05, 400, rng) for _ in range(1000)]
        print(f"  p={p}: mean T={np.mean([t for _, t, _ in out]):6.1f}  "
              f"P(cert)={np.mean([ok for _, _, ok in out]):.3f}")

    print("\n=== 2. finite-horizon certification: cost on synthetic streams ===")
    for B in (16, 40):
        for p in ((0.85, 0.1, 0.05), (0.6, 0.3, 0.1), (0.45, 0.35, 0.2)):
            Ts, certs, mism = [], 0, 0
            for _ in range(2000):
                stream = rng.choice(len(p), size=B, p=np.array(p))
                scB = int(np.argmax(np.bincount(stream, minlength=len(p))))
                a, t, ok = replay_stream(stream, len(p), B, 0.05)
                Ts.append(t)
                if ok:
                    certs += 1
                    mism += a != scB
            print(f"  B={B} p={p}: P(cert)={certs/2000:.3f}  mean T={np.mean(Ts):5.1f} "
                  f"({np.mean(Ts)/B*100:.0f}%)  mismatch={mism/max(certs,1):.4f}")

    print("\n=== 3. real-trace replay (the router-death result) ===")
    rows = real_trace_replay()
    dec = [r for r in rows if not r["plurality_right"]]
    print(f"  certify P>=.5: {sum(r['p_cert'] >= 0.5 for r in rows)}/100  "
          f"mean T={np.mean([r['mean_T'] for r in rows]):.2f}/12  "
          f"mismatch={np.mean([r['mismatch'] for r in rows if r['p_cert'] >= 0.5]):.4f}")
    print(f"  decisive stratum: {len(dec)} items, uncertified {sum(r['p_cert'] < 0.5 for r in dec)} "
          f"-> router TP={sum(r['p_cert'] < 0.5 for r in dec)}, FN={sum(r['p_cert'] >= 0.5 for r in dec)}")
    Path("results/rlsc_real_replay_pilot.json").write_text(json.dumps(rows, indent=1))


if __name__ == "__main__":
    main()
