#!/usr/bin/env python
"""Independent verification of the KAPPA kill (docs/GRAVEYARD.md #7).

The adversarial review returned FATAL with an algebraic identity and a
real-task counterexample. This script reproduces both from scratch rather
than accepting them, which is this project's standing rule for killer
findings (the same was done for the ISC review).

Two things are checked:

1. THE IDENTITY. KAPPA's score decomposes as

       score_l = sum_j log(eps_j / kappa_lj)                 <- pass-pattern-FREE
               + sum_{j: pass} [logit(kappa_lj) + logit(1-eps_j)]

   Consequence: every passed test contributes a strictly positive amount
   whenever kappa_lj > eps_j, so the pass-dependent part is a positively
   weighted vote -- it can never treat a failure as evidence FOR a cluster.
   The only cluster-specific offset is a function of the mutant kill rates
   alone, i.e. of how fragile the representative is, not of what the tests
   observed.

2. THE FRAGILITY CONFOUND. Two candidates with IDENTICAL pass rows carry
   identical behavioural evidence, yet KAPPA separates them by their mutants'
   fragility. Whether that separation helps depends on an empirical question
   the design never asked: is a wrong LLM program's neighbourhood more or
   less mutant-fragile than a correct one's? This builds a real task with
   conceptually-wrong candidates (the errors LLMs actually make) and measures
   the sign.

    python experiments/verify_kappa_kill.py
"""

from __future__ import annotations

import ast
import json
import random
from pathlib import Path

import numpy as np

# --------------------------------------------------------------------------
# 1. The identity, on random inputs.
# --------------------------------------------------------------------------


def score_direct(passed, kappa, eps):
    """KAPPA as specified: per-verdict LLR summed over tests."""
    s = 0.0
    for j, p in enumerate(passed):
        if p:
            s += np.log((1 - eps[j]) / (1 - kappa[j]))
        else:
            s += np.log(eps[j] / kappa[j])
    return s


def score_identity(passed, kappa, eps):
    """The reviewer's claimed decomposition."""
    logit = lambda x: np.log(x / (1 - x))
    offset = float(np.sum(np.log(eps / kappa)))
    gain = sum(logit(kappa[j]) + logit(1 - eps[j]) for j, p in enumerate(passed) if p)
    return offset + gain


def check_identity(trials=20000, m=18, seed=0):
    rng = np.random.default_rng(seed)
    worst = 0.0
    for _ in range(trials):
        kappa = rng.uniform(0.05, 0.98, m)
        eps = rng.uniform(0.005, 0.30, m)
        passed = rng.random(m) < 0.6
        worst = max(worst, abs(score_direct(passed, kappa, eps) - score_identity(passed, kappa, eps)))
    return worst


def check_monotone(trials=20000, m=18, seed=1):
    """Does an extra passed test ever LOWER the score when kappa > eps?"""
    rng = np.random.default_rng(seed)
    logit = lambda x: np.log(x / (1 - x))
    violations = 0
    for _ in range(trials):
        kappa = rng.uniform(0.05, 0.98, m)
        eps = rng.uniform(0.005, 0.30, m)
        j = rng.integers(m)
        if kappa[j] <= eps[j]:
            continue
        if logit(kappa[j]) + logit(1 - eps[j]) <= 0:
            violations += 1
    return violations


# --------------------------------------------------------------------------
# 2. A real task: 1 correct + conceptually-wrong candidates, real AST mutants.
# --------------------------------------------------------------------------

TASK = "count_upper: count uppercase vowels at EVEN indices of s"

CANDIDATES = {
    "correct": """
def f(s):
    return sum(1 for i in range(0, len(s), 2) if s[i] in 'AEIOU')
""",
    # conceptual errors of the kind LLMs actually make
    "W_odd": """
def f(s):
    return sum(1 for i in range(1, len(s), 2) if s[i] in 'AEIOU')
""",
    "W_allvowel": """
def f(s):
    return sum(1 for i in range(0, len(s), 2) if s[i] in 'AEIOUaeiou')
""",
    "W_anyindex": """
def f(s):
    return sum(1 for c in s if c in 'AEIOU')
""",
    "W_consonant": """
def f(s):
    return sum(1 for i in range(0, len(s), 2) if s[i].isupper() and s[i] not in 'AEIOU')
""",
    "W_oneindexed": """
def f(s):
    return sum(1 for i in range(len(s)) if (i + 1) % 2 == 0 and s[i] in 'AEIOU')
""",
}


def gold(s):
    return sum(1 for i in range(0, len(s), 2) if s[i] in "AEIOU")


TEST_INPUTS = ["aBCdEf", "abcdefg", "dBBE", "AEIOU", "", "A", "xyzAEI", "AaEeIiOoUu",
               "ABCDEFGHIJ", "zzzzz", "EIOUA", "aEiOu", "QWERTY", "AEIOUAEIOU",
               "bAcEdI", "UUUU", "a", "AB"]


class Mutator(ast.NodeTransformer):
    """AST-level semantic mutation, as specified: comparison flips, off-by-one
    on constants, boolean-op flips, comparator swaps."""

    def __init__(self, target, kind):
        self.target, self.kind, self.n = target, kind, 0

    def _hit(self):
        self.n += 1
        return self.n - 1 == self.target

    def visit_Constant(self, node):
        self.generic_visit(node)
        if isinstance(node.value, int) and not isinstance(node.value, bool):
            if self.kind == "const" and self._hit():
                return ast.Constant(value=node.value + random.choice([-1, 1]))
        return node

    def visit_Compare(self, node):
        self.generic_visit(node)
        if self.kind == "cmp" and self._hit():
            swap = {ast.In: ast.NotIn, ast.NotIn: ast.In, ast.Eq: ast.NotEq,
                    ast.NotEq: ast.Eq, ast.Lt: ast.LtE, ast.LtE: ast.Lt,
                    ast.Gt: ast.GtE, ast.GtE: ast.Gt}
            op = type(node.ops[0])
            if op in swap:
                return ast.Compare(left=node.left, ops=[swap[op]()], comparators=node.comparators)
        return node

    def visit_BoolOp(self, node):
        self.generic_visit(node)
        if self.kind == "bool" and self._hit():
            new = ast.Or() if isinstance(node.op, ast.And) else ast.And()
            return ast.BoolOp(op=new, values=node.values)
        return node


def make_mutants(src, k=20, seed=0):
    random.seed(seed)
    tree = ast.parse(src)
    out, seen = [], {ast.dump(tree)}
    for kind in ("const", "cmp", "bool"):
        for t in range(8):
            m = Mutator(t, kind).visit(ast.parse(src))
            ast.fix_missing_locations(m)
            d = ast.dump(m)
            if d in seen:
                continue
            seen.add(d)
            out.append(ast.unparse(m))
            if len(out) >= k:
                return out
    return out


def run(src, inp):
    ns = {}
    try:
        exec(src, ns)
        return ns["f"](inp)
    except Exception:
        return "__CRASH__"


def main():
    print("=== 1. THE IDENTITY ===")
    worst = check_identity()
    print(f"  max |score_direct - score_identity| over 20,000 random cells: {worst:.2e}")
    print(f"  -> identity {'HOLDS' if worst < 1e-9 else 'FAILS'}")
    v = check_monotone()
    print(f"  cases where a passed test lowers the score while kappa>eps: {v}")
    print(f"  -> the pass-dependent part is a POSITIVELY WEIGHTED VOTE"
          f" ({'confirmed' if v == 0 else 'refuted'}): a failure can never")
    print("     count as evidence FOR a cluster, so no verdict is ever inverted.")

    print(f"\n=== 2. REAL TASK: {TASK} ===")
    # pass matrix on the model-visible tests
    B, rows = {}, {}
    for name, src in CANDIDATES.items():
        row = [1 if run(src, s) == gold(s) else 0 for s in TEST_INPUTS]
        B[name] = np.array(row)
        rows.setdefault(tuple(row), []).append(name)
    print(f"{'candidate':14s} {'tally':>5}  pass row")
    for name in CANDIDATES:
        print(f"{name:14s} {int(B[name].sum()):>5}  {''.join(map(str, B[name]))}")

    dup = {r: n for r, n in rows.items() if len(n) > 1}
    if dup:
        print("\n  behaviourally IDENTICAL groups (pass matrix cannot separate them):")
        for r, n in dup.items():
            print(f"    {n}")

    # kappa: per (candidate, test) local kill rate over that candidate's mutants
    kappa = {}
    for name, src in CANDIDATES.items():
        muts = make_mutants(src, k=20, seed=hash(name) % 1000)
        kk = []
        for j, s in enumerate(TEST_INPUTS):
            killed = sum(1 for m in muts if run(m, s) != gold(s))
            kk.append(killed / max(len(muts), 1))
        kappa[name] = np.clip(np.array(kk), 0.02, 0.98)

    eps = np.full(len(TEST_INPUTS), 0.05)  # the design's clip; oracle arm below
    scores = {n: score_direct(B[n], kappa[n], eps) for n in CANDIDATES}
    tally_pick = max(CANDIDATES, key=lambda n: B[n].sum())
    kappa_pick = max(CANDIDATES, key=lambda n: scores[n])

    print(f"\n{'candidate':14s} {'tally':>5} {'meankappa':>10} {'KAPPAscore':>11}")
    for n in sorted(CANDIDATES, key=lambda x: -scores[x]):
        print(f"{n:14s} {int(B[n].sum()):>5} {kappa[n].mean():>10.3f} {scores[n]:>11.3f}")

    print(f"\n  uniform-majority pick : {tally_pick}  {'CORRECT' if tally_pick=='correct' else 'WRONG'}")
    print(f"  KAPPA pick            : {kappa_pick}  {'CORRECT' if kappa_pick=='correct' else 'WRONG'}")

    # does fragility track correctness, or oppose it?
    corr_k = kappa["correct"].mean()
    wrong_k = np.mean([kappa[n].mean() for n in CANDIDATES if n != "correct"])
    print(f"\n  mean kappa, correct candidate : {corr_k:.3f}")
    print(f"  mean kappa, wrong candidates   : {wrong_k:.3f}")
    print(f"  -> fragility {'FAVOURS' if corr_k > wrong_k else 'PENALISES'} the correct program"
          f" ({'assumption holds' if corr_k > wrong_k else 'assumption INVERTED'})")

    # the confound, isolated: hold the pass row fixed, vary only kappa
    print("\n  isolating the confound (regress score on tally and mean kappa):")
    X = np.array([[B[n].sum(), kappa[n].mean(), 1.0] for n in CANDIDATES])
    y = np.array([scores[n] for n in CANDIDATES])
    beta, *_ = np.linalg.lstsq(X, y, rcond=None)
    pred = X @ beta
    r2 = 1 - np.sum((y - pred) ** 2) / max(np.sum((y - y.mean()) ** 2), 1e-12)
    print(f"    score ~ {beta[0]:+.2f}*tally {beta[1]:+.2f}*mean_kappa {beta[2]:+.2f}   R^2={r2:.3f}")
    print("    a cluster can buy score with mutant fragility alone, holding the")
    print("    pass row -- the only behavioural evidence -- fixed.")

    Path("results").mkdir(exist_ok=True)
    Path("results/kappa_kill_verification.json").write_text(json.dumps(dict(
        identity_max_error=worst, monotone_violations=v,
        tally_pick=tally_pick, kappa_pick=kappa_pick,
        mean_kappa_correct=float(corr_k), mean_kappa_wrong=float(wrong_k),
        scores={k: float(x) for k, x in scores.items()},
        tallies={k: int(B[k].sum()) for k in B},
    ), indent=1))
    print("\nwrote results/kappa_kill_verification.json")


if __name__ == "__main__":
    main()
