"""Answer equivalence for MATH-style LaTeX answers.

Two-stage: a deterministic string canonicalisation (used for BUCKETING samples
into answer clusters -- must be fast and total), then a sympy-backed
equivalence check (used for GRADING a cluster against gold -- may be slow,
falls back to string equality when parsing fails).

Bucketing and grading are deliberately separate: clustering only needs
within-model consistency, grading needs mathematical truth. A canonicalisation
too aggressive for grading (e.g. numeric evaluation at 4 decimals) is fine for
bucketing, and vice versa.
"""

from __future__ import annotations

import re
from functools import lru_cache

import numpy as np

from .traces import TracePool

_LATEX_JUNK = [
    (r"\\boxed\{(.*)\}", r"\1"),
    (r"\\left|\\right|\\!|\\,|\\;|\\ ", ""),
    (r"\\text\{([^}]*)\}", r"\1"),
    (r"\\mbox\{([^}]*)\}", r"\1"),
    (r"\\\$|\$", ""),
    (r"\\%|%", ""),
    (r"\\dfrac|\\tfrac", r"\\frac"),
    (r"\\cdot", "*"),
    (r"\\times", "*"),
    (r"\^\{?\\circ\}?", ""),
    (r"\\(?:degrees?|circ)", ""),
    (r"\\pi", "pi"),
    (r"\\sqrt\s*(\d)", r"\\sqrt{\1}"),
    (r"\s+", ""),
]


def canon(a: str) -> str:
    """Deterministic canonical form for answer bucketing."""
    a = str(a).strip()
    for pat, rep in _LATEX_JUNK:
        a = re.sub(pat, rep, a)
    a = a.strip("$. ").lower().rstrip("^")
    a = re.sub(r"^[a-z](?:\([a-z]\))?=", "", a)  # 'x=5' / 'f(x)=...' -> value
    # sqrt BEFORE frac, both iterated, so \frac{5\sqrt{53}}{53} loses its
    # inner braces before the frac pattern (which forbids nested braces) runs
    prev = None
    while prev != a:
        prev = a
        a = re.sub(r"\\sqrt\{([^{}]*)\}", r"sqrt(\1)", a)
        a = re.sub(r"\\frac\{([^{}]*)\}\{([^{}]*)\}", r"(\1)/(\2)", a)
    a = a.replace("{", "(").replace("}", ")")
    a = re.sub(r"\.0+$", "", a)
    # (a)/(b) with plain ints -> a/b
    a = re.sub(r"^\((\-?\d+)\)/\((\d+)\)$", r"\1/\2", a)
    a = re.sub(r"^\((.+)\)$", r"\1", a) if a.count("(") == 1 and a.count(")") == 1 and a.startswith("(") and a.endswith(")") and "," not in a else a
    return a


@lru_cache(maxsize=8192)
def _sympy_val(expr: str):
    """Parse a canonicalised answer into a sympy object, or None."""
    try:
        import sympy
        from sympy.parsing.sympy_parser import (
            implicit_multiplication_application,
            parse_expr,
            standard_transformations,
        )

        e = parse_expr(
            expr.replace("^", "**"),
            transformations=standard_transformations + (implicit_multiplication_application,),
            evaluate=True,
        )
        return sympy.simplify(e)
    except Exception:
        return None


def equivalent(pred: str, gold: str) -> bool:
    """Is a predicted answer mathematically equal to gold?"""
    cp, cg = canon(pred), canon(gold)
    if cp == cg:
        return True
    # interval / tuple / set answers: compare element-wise canonical forms
    if ("," in cp) != ("," in cg):
        return False
    if "," in cp:
        sp = [x.strip() for x in re.split(r"[,;]", cp)]
        sg = [x.strip() for x in re.split(r"[,;]", cg)]
        if len(sp) != len(sg):
            return False
        return all(equivalent(x, y) for x, y in zip(sp, sg))
    vp, vg = _sympy_val(cp), _sympy_val(cg)
    if vp is None or vg is None:
        return False
    try:
        import sympy

        diff = sympy.simplify(vp - vg)
        if diff == 0:
            return True
        return bool(abs(complex(diff)) < 1e-9)
    except Exception:
        return False

def build_math_pool(qid: str, samples: list[dict], gold: str) -> TracePool | None:
    """Bucket answers into mathematical-equivalence classes and grade against gold.

    Lives here rather than in a script because two scripts bucketing the same
    substrate differently is a defect that already happened: a screening panel
    used backends.build_pool, whose normalise_answer only folds case and
    whitespace, and reported 13 decisive items on a MATH L5 evaluation set where
    the campaign reports 10. Plain string equality splits 1/2 from 0.5, which
    inflates the answer count, deflates margins, and can hand the plurality to a
    wrong answer that merely happens to be spelled one way.

    backends.build_pool stays correct for the QA campaigns, where answers are
    integers or multiple-choice letters and normalise_answer is sufficient.
    Anything grading LaTeX must come through here.
    """
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
