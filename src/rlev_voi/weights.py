"""Effective weights and the *coherent* effective count (SPEC.md section 4.1).

This module holds the central corrected estimator. Given a similarity kernel
``S`` with unit diagonal::

    s_i     = sum_j S_ij                 (similarity mass, in [1, K])
    w_i     = 1 / s_i                    (effective weight, in [1/K, 1])
    N_a^eff = sum_{i: a_i = a} w_i       (coherent effective count for answer a)
    n_eff   = sum_i w_i = tr(D^-1 S)     (coherent total effective count, in [1, K])

Block-model sanity (groups of size ``m_g``, within-group similarity ``rho_g``)::

    N_g^eff = m_g / (1 + (m_g - 1) * rho_g)
    rho_g -> 1  =>  N_g^eff -> 1     (perfect echo collapses to ONE effective vote)
    rho_g -> 0  =>  N_g^eff -> m_g   (independent traces keep full weight)

.. warning::
   The Kish dispersion ratio ``(sum w)^2 / sum w^2`` is **not** the effective
   count. For K identical copies the weights are uniform (``w_i = 1/K``) and
   Kish returns ``K`` -- i.e. it reports K independent votes for K verbatim
   echoes, exactly backwards. It is retained here only as a *dispersion
   diagnostic* (:func:`kish_dispersion`) and never enters the posterior.
"""

from __future__ import annotations

import numpy as np

from .config import Config


def similarity_mass(S: np.ndarray) -> np.ndarray:
    """Row sums ``s_i = sum_j S_ij`` (including the unit diagonal)."""
    S = np.asarray(S, dtype=float)
    return S.sum(axis=1)


def effective_weights(S: np.ndarray, cfg: Config | None = None) -> np.ndarray:
    """Inverse-similarity-mass weights ``w_i = 1 / sum_j S_ij``.

    Also known as Goldberg-Richardson fitness sharing / inverse-density
    (``D^-1``) weighting; a cheap ``O(K^2)`` surrogate for ridge leverage.
    """
    from .config import DEFAULT

    cfg = cfg or DEFAULT
    s = similarity_mass(S)
    if np.any(s <= 0):
        raise ValueError("similarity mass must be positive; check that S has a unit diagonal")
    w = 1.0 / s
    return np.clip(w, cfg.w_clip_lo, cfg.w_clip_hi)


def n_eff(w: np.ndarray) -> float:
    """Coherent total effective count ``n_eff = sum_i w_i = tr(D^-1 S)``."""
    return float(np.sum(w))


def effective_counts(w: np.ndarray, answers: np.ndarray, n_answers: int) -> np.ndarray:
    """Per-answer effective counts ``N_a^eff = sum_{i: a_i = a} w_i``.

    Args:
        w: ``(n,)`` effective weights.
        answers: ``(n,)`` integer answer codes in ``[0, n_answers)``.
        n_answers: size of the answer vocabulary observed so far.

    Returns:
        ``(n_answers,)`` array of effective counts summing to ``n_eff``.
    """
    w = np.asarray(w, dtype=float)
    answers = np.asarray(answers, dtype=int)
    return np.bincount(answers, weights=w, minlength=n_answers).astype(float)


def raw_counts(answers: np.ndarray, n_answers: int) -> np.ndarray:
    """Plain vote counts ``n_a`` -- what Self-Consistency and ASC use."""
    answers = np.asarray(answers, dtype=int)
    return np.bincount(answers, minlength=n_answers).astype(float)


def kish_dispersion(w: np.ndarray) -> float:
    """Kish ratio ``(sum w)^2 / sum w^2`` -- a weight-DISPERSION diagnostic only.

    Reported for transparency. It is deliberately *not* used in the posterior:
    for K identical copies it returns K rather than 1 (see module docstring).
    """
    w = np.asarray(w, dtype=float)
    denom = float(np.sum(w**2))
    if denom <= 0:
        return 0.0
    return float(np.sum(w) ** 2) / denom


def block_model_effective_count(m: int, rho: float) -> float:
    """Closed form ``N_g^eff = m / (1 + (m - 1) * rho)`` for one similarity block.

    Used by the mandatory unit tests to check the limiting behaviour analytically.
    """
    if m <= 0:
        return 0.0
    return m / (1.0 + (m - 1) * rho)
