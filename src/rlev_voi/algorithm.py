"""RLEV-VoI: the full streaming algorithm (SPEC.md sections 4-5).

Per trace drawn, the loop maintains two Dirichlet posteriors -- the raw one
(``alpha0 + n_a``, which is exactly Adaptive-Consistency) and the design-effect
corrected one (``alpha0 + N_a^eff``) -- and stops on whichever variant is
configured:

* ``SAFE``       -- ``min(P_raw, P_eff) >= tau``. Cannot stop earlier than ASC by
  construction, so it trades tokens for accuracy; it can never deliver a
  token-side win over ASC and the spec is explicit about that.
* ``AGGRESSIVE`` -- ``P_eff >= tau``. Can stop earlier, but only when the
  *rival* cluster is the redundant one.

Both are reported; "Pareto dominance" is judged frontier-vs-frontier over swept
thresholds, never point-vs-point.
"""

from __future__ import annotations

from dataclasses import dataclass, field

import numpy as np

from .config import Config, DEFAULT
from .consensus import consensus_weights, guarded_answer
from .kernel import build_kernel
from .posterior import ModeProbability, posterior_alpha, value_of_information
from .traces import TracePool, total_cost
from .weights import effective_counts, effective_weights, kish_dispersion, n_eff, raw_counts


@dataclass
class RunResult:
    """Outcome of one method on one item."""

    answer: int
    n_used: int
    cost: float
    correct: bool
    stopped_by: str = "k_max"
    guard_fired: bool = False
    diagnostics: dict = field(default_factory=dict)


def _mean_conf_per_answer(
    answers: np.ndarray, conf: np.ndarray, n_answers: int
) -> np.ndarray:
    sums = np.bincount(answers, weights=conf, minlength=n_answers).astype(float)
    counts = np.bincount(answers, minlength=n_answers).astype(float)
    return np.divide(sums, counts, out=np.zeros_like(sums), where=counts > 0)


def run_rlev_voi(
    pool: TracePool,
    cfg: Config = DEFAULT,
    mode_prob: ModeProbability | None = None,
    use_conf: bool = True,
    force_n: int | None = None,
) -> RunResult:
    """Run RLEV-VoI over a cached trace pool.

    Args:
        pool: cached traces for one item.
        cfg: configuration (frozen defaults unless explicitly overridden).
        mode_prob: shared deterministic mode-probability estimator.
        use_conf: whether the confidence gate passes. When ``False`` the
            consensus channel uses ``g(c) = 1``. The posterior never uses ``c``.
        force_n: if given, skip the stopping rule and use exactly this many
            traces (used for the fixed-K ablations).

    Returns:
        :class:`RunResult` with the answer, traces consumed, and total cost.
    """
    mode_prob = mode_prob or ModeProbability(n_mc=cfg.n_mc)
    k_max = min(cfg.k_max, pool.k_max)

    # Every kernel scope is an element-wise function of (sem, dup, answers), so
    # the kernel over the first t traces is exactly the leading t x t submatrix
    # of the full kernel. Building it once turns the streaming loop from
    # O(K^3) into O(K^2) without changing a single number.
    S_full = build_kernel(pool.sem, pool.dup, pool.answers, cfg)
    stopped_by = "k_max"
    p_raw = p_eff = float("nan")
    voi_per_token = float("nan")
    voi_trace: list[float] = []

    if force_n is not None:
        n = min(force_n, pool.k_max)
    else:
        n = k_max
        for t in range(max(cfg.k_min, 1), k_max + 1):
            sub = pool.prefix(t)
            w = effective_weights(S_full[:t, :t], cfg)
            a_eff = posterior_alpha(effective_counts(w, sub.answers, pool.n_answers), cfg.alpha0)
            a_raw = posterior_alpha(raw_counts(sub.answers, pool.n_answers), cfg.alpha0)
            # Unobserved answers carry only the prior; drop them so the support
            # matches Adaptive-Consistency's (observed answers only).
            seen = np.flatnonzero(np.bincount(sub.answers, minlength=pool.n_answers) > 0)
            p_eff = mode_prob(a_eff[seen])
            p_raw = mode_prob(a_raw[seen])

            if cfg.stop_on_raw:
                stop_a = p_raw >= cfg.tau  # ablation (h): ASC stopping, DDWC consensus
            elif cfg.stop_variant == "SAFE":
                stop_a = min(p_raw, p_eff) >= cfg.tau
            else:
                stop_a = p_eff >= cfg.tau

            stop_b = False
            if cfg.voi_branch:
                gen_mean = float(np.mean(sub.gen_tokens))
                cost_next = max(gen_mean + cfg.rho_over * (2 * t + 1), 1.0)
                voi = value_of_information(
                    a_eff[seen], w_bar=n_eff(w) / t, mode_prob=mode_prob, alpha0=cfg.alpha0
                )
                voi_per_token = voi / cost_next
                voi_trace.append(voi_per_token)
                stop_b = (voi_per_token < cfg.lam) and (p_eff >= cfg.tau_floor)

            if stop_a or stop_b:
                n = t
                stopped_by = "stability" if stop_a else "voi"
                break

    sub = pool.prefix(n)
    S = build_kernel(sub.sem, sub.dup, sub.answers, cfg)
    w = effective_weights(S, cfg)
    n_counts = raw_counts(sub.answers, pool.n_answers)
    W = consensus_weights(w, sub.answers, pool.n_answers, sub.confidences, cfg, use_conf)
    mean_conf = _mean_conf_per_answer(sub.answers, sub.confidences, pool.n_answers)
    if cfg.disable_guard:
        from .consensus import argmax_with_tiebreak

        answer, guard_fired = argmax_with_tiebreak(n_counts, n_counts, mean_conf), False
    else:
        answer, guard_fired = guarded_answer(W, n_counts, sub.answers, sub.dup, cfg, mean_conf)

    return RunResult(
        answer=answer,
        n_used=n,
        cost=total_cost(pool, n, cfg.rho_over, uses_similarity=True),
        correct=bool(answer == pool.correct),
        stopped_by=stopped_by,
        guard_fired=guard_fired,
        diagnostics={
            "n_eff": n_eff(w),
            "kish_dispersion": kish_dispersion(w),
            "p_raw": p_raw,
            "p_eff": p_eff,
            "voi_per_token": voi_per_token,
            "voi_trace": voi_trace,
        },
    )
