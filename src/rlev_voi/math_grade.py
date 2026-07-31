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
