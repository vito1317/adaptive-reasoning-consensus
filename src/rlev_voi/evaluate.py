"""Evaluation harness: matched-budget frontiers and paired statistics.

Dominance is judged **frontier-vs-frontier** over swept thresholds, never
point-vs-point: every adaptive method gets its own sweep and traces its own
accuracy-vs-total-cost curve, and each is charged only for the machinery it
actually uses (see :mod:`rlev_voi.traces`).
"""

from __future__ import annotations

from dataclasses import dataclass, field
from typing import Callable, Sequence

import numpy as np
from scipy.stats import binomtest

from .traces import TracePool

MethodFn = Callable[[TracePool], "object"]


@dataclass
class Point:
    """One (method, hyperparameter) configuration evaluated over a dataset."""

    method: str
    label: str
    accuracy: float
    cost: float
    mean_n: float
    correct: np.ndarray = field(repr=False)
    n_used: np.ndarray = field(repr=False)
    costs: np.ndarray = field(repr=False)
    extra: dict = field(default_factory=dict)


def evaluate(method: str, label: str, fn: MethodFn, dataset: Sequence[TracePool]) -> Point:
    """Run one configuration over every item and aggregate."""
    results = [fn(p) for p in dataset]
    correct = np.array([r.correct for r in results], dtype=bool)
    costs = np.array([r.cost for r in results], dtype=float)
    n_used = np.array([r.n_used for r in results], dtype=float)
    extra = {
        "guard_fired_rate": float(np.mean([getattr(r, "guard_fired", False) for r in results])),
        "stopped_by": {
            k: int(sum(1 for r in results if r.stopped_by == k))
            for k in {r.stopped_by for r in results}
        },
    }
    return Point(
        method=method,
        label=label,
        accuracy=float(correct.mean()),
        cost=float(costs.mean()),
        mean_n=float(n_used.mean()),
        correct=correct,
        n_used=n_used,
        costs=costs,
        extra=extra,
    )


def pareto_frontier(points: Sequence[Point]) -> list[Point]:
    """Points not dominated on (lower cost, higher accuracy)."""
    out: list[Point] = []
    for p in points:
        dominated = any(
            (q.cost <= p.cost and q.accuracy >= p.accuracy) and (q.cost < p.cost or q.accuracy > p.accuracy)
            for q in points
        )
        if not dominated:
            out.append(p)
    return sorted(out, key=lambda p: p.cost)


def interpolate_accuracy(frontier: Sequence[Point], cost: float) -> float | None:
    """Linear interpolation of a method's frontier at a given budget.

    Returns ``None`` outside the method's achievable cost range, so that
    comparisons are never extrapolated.
    """
    fr = sorted(frontier, key=lambda p: p.cost)
    if not fr or cost < fr[0].cost or cost > fr[-1].cost:
        return None
    for a, b in zip(fr, fr[1:]):
        if a.cost <= cost <= b.cost:
            if b.cost == a.cost:
                return max(a.accuracy, b.accuracy)
            t = (cost - a.cost) / (b.cost - a.cost)
            return a.accuracy + t * (b.accuracy - a.accuracy)
    return fr[-1].accuracy


def mcnemar(a: np.ndarray, b: np.ndarray) -> dict:
    """Exact McNemar test on paired correctness vectors ``a`` vs ``b``."""
    a = np.asarray(a, dtype=bool)
    b = np.asarray(b, dtype=bool)
    n01 = int(np.sum(~a & b))  # b right, a wrong
    n10 = int(np.sum(a & ~b))  # a right, b wrong
    n = n01 + n10
    p = 1.0 if n == 0 else float(binomtest(n10, n, 0.5).pvalue)
    return {"a_only": n10, "b_only": n01, "p_value": p}


def holm_correct(pvalues: dict[str, float], alpha: float = 0.05) -> dict[str, dict]:
    """Holm-Bonferroni correction across a family of tests."""
    items = sorted(pvalues.items(), key=lambda kv: kv[1])
    m = len(items)
    out: dict[str, dict] = {}
    prev = 0.0
    for i, (k, p) in enumerate(items):
        adj = min(1.0, max(prev, (m - i) * p))
        prev = adj
        out[k] = {"p_raw": p, "p_holm": adj, "significant": adj < alpha}
    return out


def bootstrap_ci(
    values: np.ndarray, n_boot: int = 10_000, alpha: float = 0.05, seed: int = 0
) -> tuple[float, float]:
    """Percentile bootstrap CI for the mean."""
    rng = np.random.default_rng(seed)
    v = np.asarray(values, dtype=float)
    idx = rng.integers(0, v.size, size=(n_boot, v.size))
    means = v[idx].mean(axis=1)
    lo, hi = np.percentile(means, [100 * alpha / 2, 100 * (1 - alpha / 2)])
    return float(lo), float(hi)


def paired_diff_ci(
    a: np.ndarray, b: np.ndarray, n_boot: int = 10_000, alpha: float = 0.05, seed: int = 0
) -> tuple[float, float, float]:
    """Bootstrap CI for the paired accuracy difference ``mean(a) - mean(b)``."""
    d = np.asarray(a, dtype=float) - np.asarray(b, dtype=float)
    lo, hi = bootstrap_ci(d, n_boot=n_boot, alpha=alpha, seed=seed)
    return float(d.mean()), lo, hi


def expected_calibration_error(
    confidences: np.ndarray, correct: np.ndarray, n_bins: int = 10
) -> float:
    """Standard binned ECE, used to drive the confidence gate.

    The gate exists because the confidence channel is only safe when it tracks
    correctness; on an anti-correlated model it must be switched off rather than
    trusted. Note ECE is a *magnitude*, so it flags miscalibration in either
    direction.
    """
    c = np.asarray(confidences, dtype=float).ravel()
    y = np.asarray(correct, dtype=float).ravel()
    edges = np.linspace(0.0, 1.0, n_bins + 1)
    idx = np.clip(np.digitize(c, edges[1:-1], right=False), 0, n_bins - 1)
    ece = 0.0
    for b in range(n_bins):
        m = idx == b
        if not np.any(m):
            continue
        ece += (m.sum() / c.size) * abs(y[m].mean() - c[m].mean())
    return float(ece)


def confidence_gate_passes(dataset: Sequence[TracePool], threshold: float) -> tuple[bool, float]:
    """Decide whether the consensus channel may use self-reported confidence.

    Computed on a dev split of trace-level (confidence, correctness) pairs. The
    posterior never uses confidence regardless of this decision.
    """
    conf = np.concatenate([p.confidences for p in dataset])
    corr = np.concatenate([(p.answers == p.correct).astype(float) for p in dataset])
    ece = expected_calibration_error(conf, corr)
    return bool(ece <= threshold), ece


def achievable_oracle(dataset: Sequence[TracePool], k_max: int) -> tuple[float, float]:
    """Retrospective oracle: smallest K whose running majority equals the K_max answer.

    The metric reviewers trust, computed on the traces themselves rather than on
    the simulator's own latent probabilities. Returns (mean K, accuracy of the
    K_max majority).
    """
    ks, acc = [], []
    for pool in dataset:
        n = min(k_max, pool.k_max)
        final = int(np.argmax(np.bincount(pool.answers[:n], minlength=pool.n_answers)))
        k_star = n
        for t in range(1, n + 1):
            running = int(np.argmax(np.bincount(pool.answers[:t], minlength=pool.n_answers)))
            if running == final and all(
                int(np.argmax(np.bincount(pool.answers[:u], minlength=pool.n_answers))) == final
                for u in range(t, n + 1)
            ):
                k_star = t
                break
        ks.append(k_star)
        acc.append(final == pool.correct)
    return float(np.mean(ks)), float(np.mean(acc))
