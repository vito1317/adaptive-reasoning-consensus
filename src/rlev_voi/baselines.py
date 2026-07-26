"""Baseline methods, all replaying the identical cached trace pool.

Cost accounting is per-method honest: only methods that actually embed traces
and compute pairwise similarity (dedup-SC, RASC-lite, RLEV-VoI) are charged the
``o_n`` overhead. Vote-counting methods (SC, ASC, ESC, SPRT) and
confidence-weighting methods (CISC -- logprob confidence is free at generation)
are not.

The reimplementations marked "lite" follow the published *criterion* but not
every engineering detail of the original papers; they are labelled as such
wherever results are reported.
"""

from __future__ import annotations

import numpy as np

from .algorithm import RunResult, _mean_conf_per_answer
from .config import Config, DEFAULT
from .consensus import argmax_with_tiebreak
from .kernel import hinge_pow
from .posterior import ModeProbability, posterior_alpha
from .traces import PROFILE_DUP_ONLY, PROFILE_NONE, TracePool, total_cost
from .weights import raw_counts


def _seen(answers: np.ndarray, n_answers: int) -> np.ndarray:
    return np.flatnonzero(np.bincount(answers, minlength=n_answers) > 0)


def run_self_consistency(pool: TracePool, k: int, cfg: Config = DEFAULT) -> RunResult:
    """Plain Self-Consistency (Wang et al. 2022) with a fixed budget ``k``."""
    n = min(k, pool.k_max)
    sub = pool.prefix(n)
    counts = raw_counts(sub.answers, pool.n_answers)
    mean_conf = _mean_conf_per_answer(sub.answers, sub.confidences, pool.n_answers)
    answer = argmax_with_tiebreak(counts, counts, mean_conf)
    return RunResult(
        answer=answer,
        n_used=n,
        cost=total_cost(pool, n, cfg.rho_over, profile=PROFILE_NONE),
        correct=bool(answer == pool.correct),
        stopped_by="fixed_k",
    )


def run_adaptive_consistency(
    pool: TracePool, cfg: Config = DEFAULT, mode_prob: ModeProbability | None = None
) -> RunResult:
    """Adaptive-Consistency (Aggarwal et al. 2023): Dirichlet stopping on raw counts.

    This is exactly RLEV-VoI with ``S = I``, no VoI branch and no guard, and
    shares the same ``P_stable`` estimator -- so the reduction test T1 compares
    two genuinely independent code paths rather than one function with itself.
    """
    mode_prob = mode_prob or ModeProbability(n_mc=cfg.n_mc)
    k_max = min(cfg.k_max, pool.k_max)
    n, stopped_by = k_max, "k_max"
    for t in range(max(cfg.k_min, 1), k_max + 1):
        sub = pool.prefix(t)
        alpha = posterior_alpha(raw_counts(sub.answers, pool.n_answers), cfg.alpha0)
        if mode_prob(alpha[_seen(sub.answers, pool.n_answers)]) >= cfg.tau:
            n, stopped_by = t, "stability"
            break
    sub = pool.prefix(n)
    counts = raw_counts(sub.answers, pool.n_answers)
    mean_conf = _mean_conf_per_answer(sub.answers, sub.confidences, pool.n_answers)
    answer = argmax_with_tiebreak(counts, counts, mean_conf)
    return RunResult(
        answer=answer,
        n_used=n,
        cost=total_cost(pool, n, cfg.rho_over, profile=PROFILE_NONE),
        correct=bool(answer == pool.correct),
        stopped_by=stopped_by,
    )


def run_cisc(pool: TracePool, k: int, cfg: Config = DEFAULT) -> RunResult:
    """Confidence-Informed Self-Consistency: votes weighted by ``c_i^gamma_c``."""
    n = min(k, pool.k_max)
    sub = pool.prefix(n)
    v = sub.confidences**cfg.gamma_c
    W = np.bincount(sub.answers, weights=v, minlength=pool.n_answers).astype(float)
    counts = raw_counts(sub.answers, pool.n_answers)
    mean_conf = _mean_conf_per_answer(sub.answers, sub.confidences, pool.n_answers)
    answer = argmax_with_tiebreak(W, counts, mean_conf)
    return RunResult(
        answer=answer,
        n_used=n,
        cost=total_cost(pool, n, cfg.rho_over, profile=PROFILE_NONE),
        correct=bool(answer == pool.correct),
        stopped_by="fixed_k",
    )


def run_dedup_sc(pool: TracePool, k: int, cfg: Config = DEFAULT) -> RunResult:
    """Plain near-duplicate vote dedup, then majority.

    The direct test of whether the duplication half of the DECOMP kernel buys
    anything over simply throwing away verbatim copies. A trace is dropped if
    its duplication similarity to any already-kept trace exceeds ``theta_dup``.
    """
    n = min(k, pool.k_max)
    sub = pool.prefix(n)
    keep: list[int] = []
    for i in range(n):
        if all(sub.dup[i, j] <= cfg.theta_dup for j in keep):
            keep.append(i)
    kept = np.array(keep, dtype=int)
    counts = np.bincount(sub.answers[kept], minlength=pool.n_answers).astype(float)
    all_counts = raw_counts(sub.answers, pool.n_answers)
    mean_conf = _mean_conf_per_answer(sub.answers, sub.confidences, pool.n_answers)
    answer = argmax_with_tiebreak(counts, all_counts, mean_conf)
    return RunResult(
        answer=answer,
        n_used=n,
        cost=total_cost(pool, n, cfg.rho_over, profile=PROFILE_DUP_ONLY),
        correct=bool(answer == pool.correct),
        stopped_by="fixed_k",
        diagnostics={"n_kept": int(kept.size)},
    )


def run_esc(pool: TracePool, cfg: Config = DEFAULT, window: int = 5) -> RunResult:
    """Early-Stopping Self-Consistency (Li et al. 2024), lite.

    Draw traces in windows of size ``window``; stop as soon as one window is
    unanimous. Answer is the majority over everything sampled.
    """
    k_max = min(cfg.k_max, pool.k_max)
    n, stopped_by = k_max, "k_max"
    for end in range(window, k_max + 1, window):
        w = pool.answers[end - window : end]
        if np.unique(w).size == 1:
            n, stopped_by = end, "unanimous_window"
            break
    sub = pool.prefix(n)
    counts = raw_counts(sub.answers, pool.n_answers)
    mean_conf = _mean_conf_per_answer(sub.answers, sub.confidences, pool.n_answers)
    answer = argmax_with_tiebreak(counts, counts, mean_conf)
    return RunResult(
        answer=answer,
        n_used=n,
        cost=total_cost(pool, n, cfg.rho_over, profile=PROFILE_NONE),
        correct=bool(answer == pool.correct),
        stopped_by=stopped_by,
    )


def run_sprt(pool: TracePool, cfg: Config = DEFAULT, margin: int = 5) -> RunResult:
    """Plain sequential margin test: stop when the leader's lead reaches ``margin``.

    Stands in for the classical SPRT stopping axis -- the ablation that asks
    whether the VoI machinery beats a trivially simple sequential rule.
    """
    k_max = min(cfg.k_max, pool.k_max)
    n, stopped_by = k_max, "k_max"
    for t in range(max(cfg.k_min, 1), k_max + 1):
        counts = np.bincount(pool.answers[:t], minlength=pool.n_answers)
        top = np.sort(counts)[::-1]
        lead = top[0] - (top[1] if top.size > 1 else 0)
        if lead >= margin:
            n, stopped_by = t, "margin"
            break
    sub = pool.prefix(n)
    counts = raw_counts(sub.answers, pool.n_answers)
    mean_conf = _mean_conf_per_answer(sub.answers, sub.confidences, pool.n_answers)
    answer = argmax_with_tiebreak(counts, counts, mean_conf)
    return RunResult(
        answer=answer,
        n_used=n,
        cost=total_cost(pool, n, cfg.rho_over, profile=PROFILE_NONE),
        correct=bool(answer == pool.correct),
        stopped_by=stopped_by,
    )


def run_rasc_lite(
    pool: TracePool, cfg: Config = DEFAULT, mode_prob: ModeProbability | None = None
) -> RunResult:
    """RASC-lite (after Wan et al. 2024) -- the closest single combined competitor.

    Combines the three ingredients RASC uses: drop near-duplicate reasoning,
    weight the survivors by confidence, and stop on posterior stability. This is
    the baseline RLEV-VoI must beat frontier-vs-frontier to justify itself.
    """
    mode_prob = mode_prob or ModeProbability(n_mc=cfg.n_mc)
    k_max = min(cfg.k_max, pool.k_max)
    n, stopped_by = k_max, "k_max"
    for t in range(max(cfg.k_min, 1), k_max + 1):
        sub = pool.prefix(t)
        keep: list[int] = []
        for i in range(t):
            if all(sub.dup[i, j] <= cfg.theta_dup for j in keep):
                keep.append(i)
        kept = np.array(keep, dtype=int)
        v = sub.confidences[kept] ** cfg.gamma_c
        W = np.bincount(sub.answers[kept], weights=v, minlength=pool.n_answers).astype(float)
        alpha = posterior_alpha(W, cfg.alpha0)
        if mode_prob(alpha[_seen(sub.answers[kept], pool.n_answers)]) >= cfg.tau:
            n, stopped_by = t, "stability"
            break

    sub = pool.prefix(n)
    keep = []
    for i in range(n):
        if all(sub.dup[i, j] <= cfg.theta_dup for j in keep):
            keep.append(i)
    kept = np.array(keep, dtype=int)
    v = sub.confidences[kept] ** cfg.gamma_c
    W = np.bincount(sub.answers[kept], weights=v, minlength=pool.n_answers).astype(float)
    counts = raw_counts(sub.answers, pool.n_answers)
    mean_conf = _mean_conf_per_answer(sub.answers, sub.confidences, pool.n_answers)
    answer = argmax_with_tiebreak(W, counts, mean_conf)
    return RunResult(
        answer=answer,
        n_used=n,
        cost=total_cost(pool, n, cfg.rho_over, profile=PROFILE_DUP_ONLY),
        correct=bool(answer == pool.correct),
        stopped_by=stopped_by,
    )
