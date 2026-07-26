"""Dirichlet posterior, leader stability, and the value-of-information signal.

SPEC.md section 4.2. The posterior uses the **redundancy channel only**::

    alpha_a = alpha0 + N_a^eff

Confidence never enters here (it acts only on the consensus argmax), which is
what makes the reduction to Adaptive-Consistency hold unconditionally at
``S = I`` rather than only when ``g(c) == 1``.

Implementation note (deterministic mode probability)
----------------------------------------------------
For ``|A| > 2`` the mode probability ``Pr[argmax_a theta_a = leader]`` has no
closed form. Naive Monte-Carlo with ``B = 512`` has a standard error of about
1e-2 near ``p = 0.95``, which is the same order as the distance to the stopping
threshold ``tau = 0.95`` -- fresh draws each step would make the stopping time
jitter for reasons unrelated to the evidence.

We therefore use **common random numbers via inverse-CDF sampling**: a fixed
matrix of uniforms ``U`` is drawn once, and each Dirichlet sample is built as
``theta_a ∝ Gamma^{-1}(alpha_a, U[b, a])`` using ``scipy.special.gammaincinv``.
This makes ``P_stable`` a deterministic, smooth function of ``alpha``, so
consecutive steps are compared on identical randomness. The estimator is still
unbiased for the mode probability; only the noise between steps is removed.
"""

from __future__ import annotations

import numpy as np
from scipy.special import betainc, gammaincinv

from .config import Config

_MAX_CLASSES = 256


class ModeProbability:
    """Deterministic Monte-Carlo estimator of ``Pr[argmax_a theta_a = leader]``.

    Holds a fixed uniform matrix so that repeated calls with slightly different
    ``alpha`` are evaluated under common random numbers.
    """

    def __init__(self, n_mc: int = 512, seed: int = 0, max_classes: int = _MAX_CLASSES):
        self.n_mc = n_mc
        rng = np.random.default_rng(seed)
        # Open interval (0, 1) -- gammaincinv is undefined at exactly 0 or 1.
        self._u = rng.uniform(1e-9, 1.0 - 1e-9, size=(n_mc, max_classes))

    def __call__(self, alpha: np.ndarray) -> float:
        """Probability that the current posterior leader is the true mode."""
        alpha = np.asarray(alpha, dtype=float)
        alpha = alpha[alpha > 0] if np.any(alpha <= 0) else alpha
        k = alpha.shape[0]
        if k <= 1:
            # Degenerate support: a Dirichlet over one cell puts all mass there.
            # K_min prevents this from being used as a real stopping decision.
            return 1.0
        if k == 2:
            return exact_two_class_stability(alpha)
        if k > self._u.shape[1]:
            raise ValueError(f"answer vocabulary {k} exceeds max_classes {self._u.shape[1]}")

        leader = int(np.argmax(alpha))
        # theta_a ∝ Gamma(alpha_a, 1) sampled by inverse CDF under fixed uniforms.
        g = gammaincinv(alpha[None, :], self._u[:, :k])
        return float(np.mean(np.argmax(g, axis=1) == leader))


def exact_two_class_stability(alpha: np.ndarray) -> float:
    """Exact ``Pr[theta_leader > 1/2]`` for a two-cell Dirichlet (a Beta).

    ``theta_L ~ Beta(alpha_L, alpha_R)`` so
    ``Pr[theta_L > 1/2] = 1 - I_{1/2}(alpha_L, alpha_R) = I_{1/2}(alpha_R, alpha_L)``.
    With two cells this *is* the probability that the leader is the mode.
    """
    alpha = np.asarray(alpha, dtype=float)
    if alpha.shape[0] != 2:
        raise ValueError("exact_two_class_stability requires exactly 2 cells")
    L = int(np.argmax(alpha))
    R = 1 - L
    return float(betainc(alpha[R], alpha[L], 0.5))


def pairwise_beta_screen(alpha: np.ndarray) -> float:
    """Fast screen ``Pr[theta_leader > theta_rival]`` (leader vs. top rival).

    .. warning::
       This is **not** the mode probability when ``|A| > 2`` -- the leader can be
       the mode while ``theta_leader < 1/2``. Provided only as a cheap
       conservative screen, and flagged as approximate wherever it is reported.
    """
    alpha = np.asarray(alpha, dtype=float)
    if alpha.shape[0] < 2:
        return 1.0
    order = np.argsort(alpha)[::-1]
    return float(betainc(alpha[order[1]], alpha[order[0]], 0.5))


def posterior_alpha(counts: np.ndarray, alpha0: float) -> np.ndarray:
    """``alpha_a = alpha0 + counts_a``.

    With ``counts = N_a^eff`` this is the design-effect-corrected posterior; with
    ``counts = n_a`` it is exactly the Adaptive-Consistency posterior.
    """
    return alpha0 + np.asarray(counts, dtype=float)


def value_of_information(
    alpha: np.ndarray,
    w_bar: float,
    mode_prob: ModeProbability,
    alpha0: float,
    include_new_class: bool = True,
) -> float:
    """Expected gain in leader stability from one more trace.

    ``VoI = E_{a ~ pi}[P_stable^{+a}] - P_stable`` where ``pi`` is the posterior
    predictive and each hypothetical trace contributes the mean *actual* weight
    ``w_bar = n_eff / K`` (not 1 -- a new trace is expected to be as redundant as
    the ones already drawn).

    .. note::
       Because the leader is recomputed after each hypothetical vote, this
       quantity is nonnegative essentially by construction. It is **not** the
       exact Howard (1966) value of information / expected Bayes-risk reduction,
       and is used only as a *relative diminishing-returns signal*. The result is
       clamped at 0 to suppress estimator noise.

    Deviation from the spec pseudocode (deliberate): the predictive over
    "observed classes + one new class" is normalised to sum to 1. The spec's
    literal loop leaves it summing to ``1 + alpha0/total``, which biases the
    expectation upward.
    """
    alpha = np.asarray(alpha, dtype=float)
    total = float(np.sum(alpha))
    base = mode_prob(alpha)

    if include_new_class:
        pi = np.concatenate([alpha / total, [alpha0 / total]])
        pi = pi / pi.sum()
        candidates = [
            np.concatenate([alpha, [alpha0]]) + np.eye(alpha.shape[0] + 1)[i] * w_bar
            for i in range(alpha.shape[0] + 1)
        ]
    else:
        pi = alpha / total
        candidates = [alpha + np.eye(alpha.shape[0])[i] * w_bar for i in range(alpha.shape[0])]

    expected = sum(p * mode_prob(a) for p, a in zip(pi, candidates))
    return max(float(expected) - base, 0.0)


def make_mode_prob(cfg: Config, seed: int = 0) -> ModeProbability:
    """Convenience constructor tied to a config."""
    return ModeProbability(n_mc=cfg.n_mc, seed=seed)
