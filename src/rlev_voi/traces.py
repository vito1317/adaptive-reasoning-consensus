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


#: Token-equivalent cost of embedding one trace with a local encoder
#: (SPEC.md 4.4's ``kappa_emb``). Charged only to methods that need embeddings.
KAPPA_EMB = 1.0


def overhead_cost(
    n: int,
    rho_over: float,
    *,
    channels: int = 0,
    embeds: bool = False,
    posterior_calls_per_step: float = 0.0,
    kappa_post: float = 0.0,
) -> float:
    """Token-equivalent overhead for a method that ran for ``n`` traces.

    Charged per the machinery a method actually uses, not as an all-or-nothing
    flag -- a boolean would bill plain duplicate-dedup for a semantic embedding
    and a second similarity channel it never computes, roughly doubling its
    honest overhead and flattering anything compared against it.

    * ``channels``: how many pairwise similarity channels are maintained. At step
      ``k`` a channel compares the new trace against the ``k-1`` existing ones,
      so the total is ``channels * sum_k (k-1)``.
    * ``embeds``: whether a neural embedding is computed per trace
      (``kappa_emb`` each). Lexical n-gram methods set this False.
    * ``posterior_calls_per_step`` / ``kappa_post``: Monte-Carlo posterior and
      VoI work, which SPEC.md 4.4 explicitly puts on the cost axis. Charging it
      matters for ablation (g), where the VoI variant does several times the
      posterior work of a plain threshold at otherwise identical cost.
    """
    if n <= 0:
        return 0.0
    k = np.arange(1, n + 1, dtype=float)
    pairs = float(np.sum(k - 1.0))
    total = channels * pairs
    if embeds:
        total += KAPPA_EMB * n
    total += posterior_calls_per_step * kappa_post * n
    return float(rho_over * total)


#: Overhead profiles per method family, so every method is billed for exactly
#: the machinery it runs. ``posterior`` counts mode-probability evaluations per
#: step (RLEV evaluates P_raw and P_eff; the VoI branch adds |A|+1 more).
PROFILE_NONE = dict(channels=0, embeds=False)
PROFILE_DUP_ONLY = dict(channels=1, embeds=False)
PROFILE_FULL = dict(channels=2, embeds=True)


def total_cost(
    pool: TracePool,
    n: int,
    rho_over: float,
    uses_similarity: bool | None = None,
    *,
    profile: dict | None = None,
    posterior_calls_per_step: float = 0.0,
    kappa_post: float = 0.0,
) -> float:
    """Total token-equivalents: generation + the overhead the method incurs.

    This is the x-axis for every accuracy-vs-cost frontier. Comparing at matched
    *total cost* rather than matched ``K`` is what keeps the comparison fair to
    methods that buy their savings with extra local computation.

    ``uses_similarity`` is retained as a coarse shorthand (True -> full profile)
    for callers that have not been given an explicit profile.
    """
    if profile is None:
        profile = PROFILE_FULL if uses_similarity else PROFILE_NONE
    return generation_cost(pool, n) + overhead_cost(
        n,
        rho_over,
        posterior_calls_per_step=posterior_calls_per_step,
        kappa_post=kappa_post,
        **profile,
    )
