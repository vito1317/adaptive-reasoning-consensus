#!/usr/bin/env python
"""Confirmatory TACT evaluation on MATH level 5 (docs/SPEC-TACT-HARD.md).

Pre-registered BEFORE collection. Sign set = 30 items (seed 20260731),
evaluation set = the rest. Falsifiers H1-H5 as registered; every method
replays the same cached pools.

Data notes handled here, honestly:
- No reasoning text was collected, so the lexical-duplication channel is
  inert (dup = identity) and dedup-SC coincides with SC by construction.
- Answer buckets are formed by canonical string, then merged by mathematical
  equivalence (3/4 == 0.75) via union-find, so votes are counted on
  math-equivalence classes, not surface strings.

    python experiments/run_tact_hard_eval.py --traces results/math_confirm_raw.json
"""

from __future__ import annotations

import argparse
import json
import sys
from pathlib import Path

import numpy as np
from scipy.stats import binomtest

sys.path.insert(0, str(Path(__file__).resolve().parents[1] / "src"))

from rlev_voi.math_grade import canon, equivalent  # noqa: E402
from rlev_voi.tact import (  # noqa: E402
    estimate_dev,
    estimate_label_free,
    estimate_semi_lf,
    sc_answer,
    tact_vote,
)
from rlev_voi.traces import TracePool  # noqa: E402


def build_pool(qid: str, samples: list[dict], gold: str) -> TracePool | None:
    """Bucket answers on math-equivalence classes and grade against gold."""
    if len(samples) < 6:
        return None
    raw = [canon(s["answer"]) for s in samples]
    conf = np.clip([float(s.get("confidence", 0.5)) for s in samples], 0.0, 1.0)

    # union-find over distinct canonical strings by mathematical equivalence
    uniq = sorted(set(raw))
    parent = list(range(len(uniq)))

    def find(i):
        while parent[i] != i:
            parent[i] = parent[parent[i]]
            i = parent[i]
        return i

    for i in range(len(uniq)):
        for j in range(i + 1, len(uniq)):
            if find(i) != find(j) and equivalent(uniq[i], uniq[j]):
                parent[find(j)] = find(i)
    roots = sorted({find(i) for i in range(len(uniq))})
    code_of_root = {r: c for c, r in enumerate(roots)}
    code = {u: code_of_root[find(i)] for i, u in enumerate(uniq)}

    answers = np.array([code[r] for r in raw])
    n_answers = len(roots)
    correct = -1
    for u, c in code.items():
        if equivalent(u, gold):
            correct = c
            break

    k = len(samples)
    eye = np.eye(k)
    return TracePool(
        answers=answers,
        confidences=np.asarray(conf),
        sem=eye.copy(),
        dup=eye.copy(),   # no reasoning text -> duplication channel inert
        gen_tokens=np.ones(k),
        correct=correct,
        n_answers=n_answers,
        meta={"qid": qid, "group": 0},
    )


def cisc_vote(pool: TracePool, k: int) -> int:
    a, c = pool.answers[:k], pool.confidences[:k]
    return int(np.argmax(np.bincount(a, weights=c, minlength=pool.n_answers)))


def best_conf_vote(pool: TracePool, k: int) -> int:
    return int(pool.answers[:k][int(np.argmax(pool.confidences[:k]))])


def mcnemar_one_sided(b: int, c: int):
    """P(net corrections this extreme | no difference), exact binomial."""
    n = b + c
    return binomtest(b, n, 0.5, alternative="greater").pvalue if n else 1.0


def main():
    ap = argparse.ArgumentParser()
    ap.add_argument("--traces", type=Path, default=Path("results/math_confirm_raw.json"))
    ap.add_argument("--items", type=Path, default=Path("data/math_confirm_items.json"))
    ap.add_argument("--k", type=int, default=16)
    ap.add_argument("--sign-set", type=int, default=30)
    ap.add_argument("--seed", type=int, default=20260731)
    ap.add_argument("--out", type=Path, default=Path("results/tact_hard_eval.json"))
    args = ap.parse_args()

    traces = json.loads(args.traces.read_text())["traces"]
    gold = {x["qid"]: x["gold"] for x in json.loads(args.items.read_text())}

    pools = []
    for qid, tr in traces.items():
        p = build_pool(qid, tr, gold[qid])
        if p is not None:
            pools.append(p)
    print(f"pools built: {len(pools)}  (dropped {len(traces) - len(pools)} with <6 samples)")

    # Split on the REGISTERED item list (sorted qids), not on whichever pools
    # happen to have data -- the assignment must be invariant to collection
    # dropouts and dict ordering.
    all_qids = sorted(gold)
    rng = np.random.default_rng(args.seed)
    sign_qids = set(np.array(all_qids)[rng.permutation(len(all_qids))[: args.sign_set]])
    sign_pools = [p for p in pools if p.meta["qid"] in sign_qids]
    eval_pools = [p for p in pools if p.meta["qid"] not in sign_qids]
    k = min(args.k, min(p.k_max for p in pools))
    print(f"sign set {len(sign_pools)}, eval set {len(eval_pools)}, k={k}")

    # ---- substrate description (H5) --------------------------------------
    per_sample_acc = float(np.mean([np.mean(p.answers[:k] == p.correct) for p in eval_pools]))
    gold_in_pool = float(np.mean([p.correct >= 0 for p in eval_pools]))
    print(f"\nper-sample accuracy (rho_bar complement): {per_sample_acc:.3f}  "
          f"-> rho_bar = {1 - per_sample_acc:.3f} {'> 1/2 (Prop-4 regime violated)' if per_sample_acc < 0.5 else ''}")
    print(f"gold-in-pool rate: {gold_in_pool:.3f}")

    # ---- H1: does the channel exist? (gold-labelled D on eval set) -------
    dev_eval = estimate_dev(eval_pools, k)
    po = dev_eval.pooled
    print(f"\nH1 pooled D-hat = {po.d_hat:+.4f}  se = {po.se:.4f}  z = {po.z:+.2f}"
          if po else "\nH1: no informative items")
    h1_pass = bool(po and po.d_hat > 0 and po.z >= 2.0)
    print(f"H1 {'PASS' if h1_pass else 'FAIL'} (need D>0, z>=2)")

    # ---- estimators (label-free parts see only eval pools) ---------------
    lf = estimate_label_free(eval_pools, k, min_gated_items=30)
    semi = estimate_semi_lf(sign_pools, eval_pools, k, min_gated_items=30)
    print(f"\nTACT-LF   gamma = {lf.gamma:+.3f}  alarms: {[a for a, v in lf.alarms.items() if v] or 'none'}")
    print(f"TACT-semi gamma = {semi.gamma:+.3f}  sign from dev: {semi.diagnostics.get('semi_sign')}")

    # ---- methods on the eval set ------------------------------------------
    methods = {
        "SC": lambda p: sc_answer(p.answers[:k], p.n_answers),
        "dedup-SC": lambda p: sc_answer(p.answers[:k], p.n_answers),  # dup inert: == SC
        "best-conf": lambda p: best_conf_vote(p, k),
        "CISC-lin": lambda p: cisc_vote(p, k),
        "TACT-LF": lambda p: tact_vote(p.answers[:k], p.confidences[:k], p.n_answers, lf.gamma),
        "TACT-semi-LF": lambda p: tact_vote(p.answers[:k], p.confidences[:k], p.n_answers, semi.gamma),
        "oracle-in-pool": lambda p: p.correct if p.correct >= 0 else -2,
    }
    picks = {m: np.array([f(p) for p in eval_pools]) for m, f in methods.items()}
    right = {m: np.array([int(v == p.correct) for v, p in zip(picks[m], eval_pools)])
             for m in methods}

    print(f"\n{'method':>14}  {'acc':>6}  {'net vs SC':>9}")
    sc_right = right["SC"]
    results = {}
    for m in methods:
        b = int(np.sum((right[m] == 1) & (sc_right == 0)))
        c = int(np.sum((right[m] == 0) & (sc_right == 1)))
        results[m] = dict(acc=float(np.mean(right[m])), plus=b, minus=c)
        print(f"{m:>14}  {np.mean(right[m]):>6.3f}  +{b}/-{c}")

    # ---- H2: decisive-stratum McNemar for the primary endpoint ------------
    b, c = results["TACT-semi-LF"]["plus"], results["TACT-semi-LF"]["minus"]
    p_h2 = mcnemar_one_sided(b, c)
    h2_pass = bool(b - c > 0 and p_h2 < 0.05)
    dec_n = int(np.sum(sc_right == 0))
    print(f"\nH2 decisive stratum n={dec_n}; TACT-semi-LF net = +{b}/-{c}, "
          f"exact one-sided p = {p_h2:.4f} -> {'PASS' if h2_pass else 'FAIL'}")

    # ---- H3: baseline defences --------------------------------------------
    t = results["TACT-semi-LF"]["acc"]
    h3_pass = bool(t >= results["SC"]["acc"] and t >= results["dedup-SC"]["acc"]
                   and t > results["best-conf"]["acc"])
    print(f"H3 (>=SC, >=dedup-SC, >best-conf): {'PASS' if h3_pass else 'FAIL'}")

    # ---- H4: the limitation must show up as predicted ---------------------
    lf_alarms = [a for a, v in lf.alarms.items() if v]
    h4_pass = bool(lf.gamma <= 0 or lf_alarms or results["TACT-LF"]["acc"] <= t)
    print(f"H4 (LF mis-signs/alarms/does not beat semi): {'PASS' if h4_pass else 'FAIL'}"
          f"  [LF gamma {lf.gamma:+.3f}, alarms {lf_alarms or 'none'}, "
          f"LF acc {results['TACT-LF']['acc']:.3f} vs semi {t:.3f}]")

    out = dict(
        config=dict(k=k, sign_set=len(sign_pools), eval_set=len(eval_pools), seed=args.seed),
        substrate=dict(per_sample_acc=per_sample_acc, gold_in_pool=gold_in_pool,
                       decisive_n=dec_n),
        h1=dict(passed=h1_pass, d_hat=po.d_hat if po else None, se=po.se if po else None,
                z=po.z if po else None),
        gammas=dict(lf=lf.gamma, semi=semi.gamma, lf_alarms=lf_alarms,
                    semi_sign=semi.diagnostics.get("semi_sign")),
        methods=results,
        h2=dict(passed=h2_pass, plus=b, minus=c, p=p_h2),
        h3=dict(passed=h3_pass),
        h4=dict(passed=h4_pass),
    )
    args.out.write_text(json.dumps(out, indent=1, default=float))
    print(f"\nwrote {args.out}")


if __name__ == "__main__":
    main()
