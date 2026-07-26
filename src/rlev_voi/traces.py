"""Cached trace pools and honest token-equivalent cost accounting.

Every method under comparison replays the *same* cached pool of ``K_max`` traces
per item (paired, low-variance comparison), and each is charged for exactly the
machinery it uses. Methods that need embeddings and pairwise similarity pay the
overhead ``o_n``; methods that only count votes do not.
"""

from __future__ import annotations

from dataclasses import dataclass, field

import numpy as np


@dataclass
class TracePool:
    """All ``K_max`` cached traces for a single item.

    Attributes:
        answers: ``(K,)`` integer answer codes.
        confidences: ``(K,)`` confidence in ``[0, 1]``.
        sem: ``(K, K)`` semantic similarity, unit diagonal.
        dup: ``(K, K)`` lexical duplication similarity, unit diagonal.
        gen_tokens: ``(K,)`` generation cost of each trace, in tokens.
        correct: ground-truth answer code (oracle / evaluation only).
        n_answers: size of the answer vocabulary for this item.
    """

    answers: np.ndarray
    confidences: np.ndarray
    sem: np.ndarray
    dup: np.ndarray
    gen_tokens: np.ndarray
    correct: int
    n_answers: int
    meta: dict = field(default_factory=dict)

    def __post_init__(self):
        self.answers = np.asarray(self.answers, dtype=int)
        self.confidences = np.asarray(self.confidences, dtype=float)
        self.sem = np.asarray(self.sem, dtype=float)
        self.dup = np.asarray(self.dup, dtype=float)
        self.gen_tokens = np.asarray(self.gen_tokens, dtype=float)
        k = self.answers.shape[0]
        for name, arr, shape in [
            ("confidences", self.confidences, (k,)),
            ("gen_tokens", self.gen_tokens, (k,)),
            ("sem", self.sem, (k, k)),
            ("dup", self.dup, (k, k)),
        ]:
            if arr.shape != shape:
                raise ValueError(f"{name} has shape {arr.shape}, expected {shape}")

    @property
    def k_max(self) -> int:
        return int(self.answers.shape[0])

    def prefix(self, n: int) -> "TracePool":
        """The first ``n`` traces, as a pool in its own right."""
        n = min(n, self.k_max)
        return TracePool(
            answers=self.answers[:n],
            confidences=self.confidences[:n],
            sem=self.sem[:n, :n],
            dup=self.dup[:n, :n],
            gen_tokens=self.gen_tokens[:n],
            correct=self.correct,
            n_answers=self.n_answers,
            meta=self.meta,
        )


def generation_cost(pool: TracePool, n: int) -> float:
    """Tokens spent generating the first ``n`` traces."""
    return float(np.sum(pool.gen_tokens[:n]))


def overhead_cost(n: int, rho_over: float, uses_similarity: bool) -> float:
    """Token-equivalent overhead for a method that ran for ``n`` traces.

    At step ``k`` a similarity-using method embeds the new trace and compares it
    against the ``k-1`` existing ones on two channels, i.e. ``o_k = rho_over *
    (2k + 1)`` token-equivalents. Summing over steps gives the total below.
    Methods that never touch embeddings pay nothing.
    """
    if not uses_similarity or n <= 0:
        return 0.0
    k = np.arange(1, n + 1, dtype=float)
    return float(rho_over * np.sum(2.0 * k + 1.0))


def total_cost(pool: TracePool, n: int, rho_over: float, uses_similarity: bool) -> float:
    """Total token-equivalents: generation + (optional) similarity overhead.

    This is the x-axis for every accuracy-vs-cost frontier. Comparing at matched
    *total cost* rather than matched ``K`` is what keeps the comparison fair to
    methods that buy their savings with extra local computation.
    """
    return generation_cost(pool, n) + overhead_cost(n, rho_over, uses_similarity)
