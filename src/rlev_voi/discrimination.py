"""Signed within-item discrimination of a confidence channel (SPEC-TACT 4.2).

The estimand is the pair-weighted mean of per-item Somers' ``D_q = 2*AUC_q - 1``
(equivalently ``2*WQD_q - 1`` in CISC's notation), pooled across items with van
Elteren weights ``N_q = n1_q * n0_q``. Everything here is a pure rank statistic:
strictly monotone distortions of the confidence scale change nothing.
"""

from __future__ import annotations

from dataclasses import dataclass

import numpy as np
from scipy.stats import norm, rankdata


def midranks(c: np.ndarray) -> np.ndarray:
    """Within-item midranks (ties averaged), 1-based."""
    return rankdata(np.asarray(c, dtype=float), method="average")


def vdw_scores(c: np.ndarray, eps_sd: float = 1e-8) -> np.ndarray:
    """Standardized van der Waerden normal scores of the within-item midranks.

    ``phi_i = (v_i - mean v) / sd(v)`` with ``v_i = Phi^{-1}(R_i/(m+1))``. The
    SD is the *realized* one, not a closed form: the no-tie value is ~0.62 at
    m=4 vs ~0.95 at m=40, and using a closed form would silently rescale the
    exponent across budgets. All-tied confidences give ``phi = 0`` -- the item
    then votes as plain SC regardless of gamma (tie-safe degeneration).
    """
    c = np.asarray(c, dtype=float)
    m = c.shape[0]
    v = norm.ppf(midranks(c) / (m + 1))
    sd = float(np.std(v))
    if sd <= eps_sd:
        return np.zeros(m)
    return (v - float(np.mean(v))) / sd


@dataclass
class ItemStat:
    """Per-item sufficient statistics for the pooled estimator."""

    d: float
    """Somers' D_q = 2*AUC_q - 1."""
    n_pairs: float
    """Pair count N_q = n1*n0 (van Elteren weight)."""
    var0_d: float
    """Exact tie-corrected null variance of D_q."""


def item_discrimination(c: np.ndarray, labels: np.ndarray, pair_weights: np.ndarray | None = None) -> ItemStat | None:
    """Somers' D of confidence vs a binary label within one item.

    Returns ``None`` for non-informative items (all labels equal). With
    ``pair_weights`` (e.g. dedup weights ``1/|group|``), positives and negatives
    contribute weighted counts; the rank statistic itself stays unweighted --
    weighting the Mann-Whitney kernel is possible but muddies the exact null
    variance, so the weights enter only through the pooling weight ``N_q``.
    """
    c = np.asarray(c, dtype=float)
    labels = np.asarray(labels)
    pos = labels == 1
    neg = ~pos
    if pair_weights is None:
        n1, n0 = float(pos.sum()), float(neg.sum())
    else:
        w = np.asarray(pair_weights, dtype=float)
        n1, n0 = float(w[pos].sum()), float(w[neg].sum())
    if n1 <= 0 or n0 <= 0:
        return None

    R = midranks(c)
    n1_raw, n0_raw = int(pos.sum()), int(neg.sum())
    u = float(R[pos].sum()) - n1_raw * (n1_raw + 1) / 2.0
    auc = u / (n1_raw * n0_raw)
    d = 2.0 * auc - 1.0

    m = c.shape[0]
    # Exact null variance of U with tie correction, mapped to D.
    _, counts = np.unique(c, return_counts=True)
    tie_term = float(np.sum(counts.astype(float) ** 3 - counts)) if counts.size else 0.0
    correction = 1.0 - tie_term / max(m**3 - m, 1)
    var0_u = n1_raw * n0_raw * (m + 1) / 12.0 * correction
    var0_d = 4.0 * var0_u / (n1_raw * n0_raw) ** 2

    return ItemStat(d=d, n_pairs=n1 * n0, var0_d=var0_d)


@dataclass
class PooledD:
    """The pooled signed discrimination with its uncertainty."""

    d_hat: float
    se: float
    se0: float
    se_jack: float
    z: float
    n_pairs_total: float
    n_items: int


def pooled_discrimination(stats: list[ItemStat]) -> PooledD | None:
    """Van Elteren pooling with the conservative SE (SPEC-TACT 4.2).

    ``SE = max(SE0, SE_jack, 1/(2*sqrt(N)))`` -- the exact tie-corrected null SE,
    the delete-one-item jackknife (captures between-item heterogeneity of the
    coupling), and a floor that prevents a degenerate SE from manufacturing a
    huge z.
    """
    stats = [s for s in stats if s is not None]
    if not stats:
        return None
    n_q = np.array([s.n_pairs for s in stats], dtype=float)
    d_q = np.array([s.d for s in stats], dtype=float)
    var0_q = np.array([s.var0_d for s in stats], dtype=float)
    n_total = float(n_q.sum())

    d_hat = float(np.sum(n_q * d_q) / n_total)
    se0 = float(np.sqrt(np.sum(n_q**2 * var0_q)) / n_total)

    q = len(stats)
    if q > 1:
        s_sum = float(np.sum(n_q * d_q))
        d_loo = (s_sum - n_q * d_q) / (n_total - n_q)
        d_bar = float(np.mean(d_loo))
        se_jack = float(np.sqrt((q - 1) / q * np.sum((d_loo - d_bar) ** 2)))
    else:
        se_jack = se0

    se = max(se0, se_jack, 1.0 / (2.0 * np.sqrt(n_total)))
    return PooledD(
        d_hat=d_hat,
        se=se,
        se0=se0,
        se_jack=se_jack,
        z=d_hat / se if se > 0 else 0.0,
        n_pairs_total=n_total,
        n_items=q,
    )
