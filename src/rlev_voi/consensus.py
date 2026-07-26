"""Diversity-discounted consensus and the never-worse-than-SC guard.

SPEC.md section 4.1. The consensus channel (unlike the posterior) may use
confidence::

    v_i = w_i * g(c_i),   g(c) = c^gamma_c  if the ECE gate passes else 1
    a_DDWC = argmax_a  W_a,   W_a = sum_{i: a_i = a} v_i

The guard exists because inverse-similarity weighting is confounded with
correctness on tight-derivation tasks (the correct answer is often one canonical
near-duplicate derivation). It only allows DDWC to overturn the plain majority
when the majority is a *verbatim echo cluster* -- measured on the duplication
channel alone -- and then only by a clear margin.
"""

from __future__ import annotations

import numpy as np

from .config import Config
from .kernel import hinge_pow


def confidence_gain(c: np.ndarray, cfg: Config, use_conf: bool) -> np.ndarray:
    """``g(c) = c^gamma_c`` when the confidence gate passes, else all-ones."""
    if not use_conf:
        return np.ones_like(np.asarray(c, dtype=float))
    return np.asarray(c, dtype=float) ** cfg.gamma_c


def consensus_weights(
    w: np.ndarray, answers: np.ndarray, n_answers: int, c: np.ndarray | None, cfg: Config, use_conf: bool
) -> np.ndarray:
    """Per-answer consensus mass ``W_a = sum_{i: a_i = a} w_i * g(c_i)``."""
    w = np.asarray(w, dtype=float)
    answers = np.asarray(answers, dtype=int)
    if c is None:
        v = w
    else:
        v = w * confidence_gain(c, cfg, use_conf)
    return np.bincount(answers, weights=v, minlength=n_answers).astype(float)


def argmax_with_tiebreak(
    W: np.ndarray, n_counts: np.ndarray, mean_conf: np.ndarray | None = None, atol: float = 1e-12
) -> int:
    """Argmax of ``W``, breaking ties by raw count then by mean confidence."""
    W = np.asarray(W, dtype=float)
    best = float(np.max(W))
    tied = np.flatnonzero(W >= best - atol)
    if tied.size == 1:
        return int(tied[0])
    counts = np.asarray(n_counts, dtype=float)[tied]
    best_count = counts.max()
    tied = tied[counts >= best_count - atol]
    if tied.size == 1 or mean_conf is None:
        return int(tied[0])
    conf = np.asarray(mean_conf, dtype=float)[tied]
    return int(tied[int(np.argmax(conf))])


def essratio_dup(answer: int, answers: np.ndarray, dup: np.ndarray, cfg: Config) -> float:
    """Duplication-only effective-sample-size ratio *within* one answer class.

    ``ESSratio(a) = (sum_{i in G_a} w_i^dup) / n_a``  with the weights computed
    on the duplication channel restricted to ``G_a``.

    For ``m`` mutually verbatim copies the closed form is
    ``1 / (1 + (m - 1) * rho)`` -- it reaches the spec's headline ``1/m`` only in
    the ``rho -> 1`` limit, since the operative kernel carries the ``rho`` factor.
    At the frozen defaults (``rho = 0.7``, ``eta_dup = 0.5``) the guard therefore
    arms at ``m >= 3`` verbatim copies.

    Returns 1.0 (no redundancy detected) for an empty or singleton class.
    """
    answers = np.asarray(answers, dtype=int)
    idx = np.flatnonzero(answers == answer)
    m = idx.size
    if m <= 1:
        return 1.0
    D = np.asarray(dup, dtype=float)[np.ix_(idx, idx)]
    off = cfg.rho * np.clip(hinge_pow(D, cfg.theta_dup, cfg.gamma_dup), 0.0, 1.0)
    np.fill_diagonal(off, 0.0)
    s = 1.0 + off.sum(axis=1)
    return float(np.sum(1.0 / s) / m)


def guarded_answer(
    W: np.ndarray,
    n_counts: np.ndarray,
    answers: np.ndarray,
    dup: np.ndarray,
    cfg: Config,
    mean_conf: np.ndarray | None = None,
) -> tuple[int, bool]:
    """Return ``(answer, guard_fired)``.

    DDWC is allowed to overturn the plain-majority answer only when all three
    hold: it disagrees with SC, the SC majority is a detected verbatim-echo
    cluster (``ESSratio_dup <= eta_dup``), and DDWC wins by the margin
    ``(1 + delta)``. Otherwise the SC answer stands, which is what makes the
    method reduce to Self-Consistency rather than risk a regression.
    """
    a_sc = argmax_with_tiebreak(np.asarray(n_counts, dtype=float), n_counts, mean_conf)
    a_dd = argmax_with_tiebreak(W, n_counts, mean_conf)
    if a_dd == a_sc:
        return a_sc, False
    ratio = essratio_dup(a_sc, answers, dup, cfg)
    if ratio <= cfg.eta_dup and W[a_dd] >= (1.0 + cfg.delta) * W[a_sc]:
        return a_dd, True
    return a_sc, False
