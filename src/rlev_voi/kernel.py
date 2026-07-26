"""Similarity kernels for RLEV-VoI (SPEC.md section 4.1).

The working kernel decomposes redundancy into two channels:

* ``dup_ij`` -- lexical near-duplication (n-gram Jaccard). Near-verbatim echo is
  redundant *regardless of correctness*, so it is safe to discount hard.
* ``sem_ij`` -- semantic similarity (embedding cosine). This is confounded with
  correctness (a correct answer often has one canonical derivation), so it is
  discounted only weakly via ``beta_sem``.

Hinge-power transform::

    phi_{theta,gamma}(x) = ((x - theta)_+ / (1 - theta))^gamma

Working kernel (off-diagonal only; ``S_ii = 1`` always)::

    S~_ij = phi_{theta_dup,gamma_dup}(dup_ij) + beta_sem * phi_{theta_sem,gamma_sem}(sem_ij)
    S_ij  = rho * clip_[0,1](S~_ij)
"""

from __future__ import annotations

import numpy as np

from .config import Config


def hinge_pow(x: np.ndarray | float, theta: float, gamma: float) -> np.ndarray:
    """Hinge-power transform ``((x - theta)_+ / (1 - theta))^gamma``.

    Maps ``[0, 1] -> [0, 1]``, flat-zero below ``theta``. Large ``gamma`` makes the
    onset sharp, so only values very close to 1 contribute meaningfully.
    """
    if not 0.0 <= theta < 1.0:
        raise ValueError(f"theta must be in [0, 1), got {theta}")
    if gamma <= 0.0:
        raise ValueError(f"gamma must be > 0, got {gamma}")
    x = np.asarray(x, dtype=float)
    return (np.maximum(x - theta, 0.0) / (1.0 - theta)) ** gamma


def build_kernel(
    sem: np.ndarray,
    dup: np.ndarray,
    answers: np.ndarray | None = None,
    cfg: Config | None = None,
) -> np.ndarray:
    """Build the working similarity kernel ``S`` with unit diagonal.

    Args:
        sem: ``(n, n)`` semantic similarity in ``[0, 1]``.
        dup: ``(n, n)`` lexical duplication similarity in ``[0, 1]``.
        answers: ``(n,)`` integer answer codes. Required for ``WITHIN_CLASS`` scope.
        cfg: configuration; defaults to the frozen default.

    Returns:
        ``(n, n)`` symmetric matrix with ``S_ii = 1`` and off-diagonal in ``[0, rho]``.
    """
    from .config import DEFAULT

    cfg = cfg or DEFAULT
    sem = np.asarray(sem, dtype=float)
    dup = np.asarray(dup, dtype=float)
    n = sem.shape[0]
    if sem.shape != (n, n) or dup.shape != (n, n):
        raise ValueError(f"sem/dup must be square and same shape, got {sem.shape} {dup.shape}")

    if cfg.kernel_scope == "GLOBAL":
        # Semantic channel only -- predicted to backfire on tight correct clusters.
        base = hinge_pow(sem, cfg.theta_sem, cfg.gamma_sem)
    elif cfg.kernel_scope == "WITHIN_CLASS":
        # Raw semantic similarity, but only among traces that agree on the answer.
        if answers is None:
            raise ValueError("WITHIN_CLASS kernel scope requires `answers`")
        answers = np.asarray(answers)
        base = np.where(answers[:, None] == answers[None, :], sem, 0.0)
    else:  # DECOMP (default)
        base = hinge_pow(dup, cfg.theta_dup, cfg.gamma_dup) + cfg.beta_sem * hinge_pow(
            sem, cfg.theta_sem, cfg.gamma_sem
        )

    S = cfg.rho * np.clip(base, 0.0, 1.0)
    S = 0.5 * (S + S.T)  # enforce exact symmetry against float asymmetry
    np.fill_diagonal(S, 1.0)
    return S


def dup_only_kernel(dup: np.ndarray, cfg: Config | None = None) -> np.ndarray:
    """Duplication-channel-only kernel, used by the never-worse-than-SC guard.

    The guard must fire on *verbatim echo only*, never on semantic tightness, so
    it deliberately ignores the semantic channel.
    """
    from .config import DEFAULT

    cfg = cfg or DEFAULT
    dup = np.asarray(dup, dtype=float)
    S = cfg.rho * np.clip(hinge_pow(dup, cfg.theta_dup, cfg.gamma_dup), 0.0, 1.0)
    S = 0.5 * (S + S.T)
    np.fill_diagonal(S, 1.0)
    return S


def cosine_similarity_matrix(embeddings: np.ndarray) -> np.ndarray:
    """Pairwise cosine similarity clipped to ``[0, 1]``, with unit diagonal."""
    E = np.asarray(embeddings, dtype=float)
    norms = np.linalg.norm(E, axis=1, keepdims=True)
    norms = np.maximum(norms, 1e-12)
    En = E / norms
    S = np.clip(En @ En.T, 0.0, 1.0)
    np.fill_diagonal(S, 1.0)
    return S


def ngram_jaccard_matrix(texts: list[str], n: int = 5) -> np.ndarray:
    """Character n-gram Jaccard similarity -- the ``dup`` channel for real traces."""

    def grams(t: str) -> frozenset[str]:
        t = " ".join(t.split())
        if len(t) < n:
            return frozenset([t])
        return frozenset(t[i : i + n] for i in range(len(t) - n + 1))

    G = [grams(t) for t in texts]
    m = len(G)
    S = np.eye(m)
    for i in range(m):
        for j in range(i + 1, m):
            inter = len(G[i] & G[j])
            union = len(G[i] | G[j])
            S[i, j] = S[j, i] = (inter / union) if union else 0.0
    return S
