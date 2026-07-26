"""Numeric tests for components that a green suite would otherwise let you delete.

An adversarial review of the test suite found that the kernel formula, the
guard's ``(1 + delta)`` overturn margin, ``value_of_information`` and the whole
token-cost model -- the x-axis of every reported claim -- had no coverage at all.
Each could have been replaced by a constant without a single test going red.
"""

from __future__ import annotations

import numpy as np
import pytest

from rlev_voi import DEFAULT, ModeProbability, TracePool
from rlev_voi.algorithm import run_rlev_voi
from rlev_voi.consensus import essratio_dup, guarded_answer
from rlev_voi.kernel import build_kernel, hinge_pow, ngram_jaccard_matrix
from rlev_voi.posterior import value_of_information
from rlev_voi.traces import (
    KAPPA_EMB,
    PROFILE_DUP_ONLY,
    PROFILE_FULL,
    PROFILE_NONE,
    generation_cost,
    overhead_cost,
    total_cost,
)


# ------------------------------------------------------------------ kernel
def test_hinge_pow_numeric():
    """phi(x) = ((x - theta)_+ / (1 - theta))^gamma, checked against hand values."""
    assert hinge_pow(0.9, 0.9, 6.0) == pytest.approx(0.0)
    assert hinge_pow(0.5, 0.9, 6.0) == pytest.approx(0.0)  # below the hinge
    assert hinge_pow(1.0, 0.9, 6.0) == pytest.approx(1.0)
    assert hinge_pow(0.95, 0.9, 6.0) == pytest.approx(0.5**6)
    assert hinge_pow(0.8, 0.6, 3.0) == pytest.approx(0.5**3)
    assert np.allclose(hinge_pow(np.array([0.0, 0.6, 1.0]), 0.6, 3.0), [0.0, 0.0, 1.0])


def test_hinge_pow_rejects_bad_parameters():
    with pytest.raises(ValueError):
        hinge_pow(0.5, 1.0, 3.0)
    with pytest.raises(ValueError):
        hinge_pow(0.5, 0.6, 0.0)


def test_decomp_kernel_numeric():
    """The DECOMP off-diagonal must equal rho*(phi_dup + beta_sem*phi_sem), clipped."""
    cfg = DEFAULT
    sem = np.array([[1.0, 0.8], [0.8, 1.0]])
    dup = np.array([[1.0, 0.95], [0.95, 1.0]])
    S = build_kernel(sem, dup, np.array([0, 1]), cfg)
    expected = cfg.rho * min(
        1.0,
        hinge_pow(0.95, cfg.theta_dup, cfg.gamma_dup)
        + cfg.beta_sem * hinge_pow(0.8, cfg.theta_sem, cfg.gamma_sem),
    )
    assert S[0, 1] == pytest.approx(expected)
    assert expected == pytest.approx(0.7 * (0.5**6 + 0.25 * 0.5**3))


def test_semantic_channel_is_actually_wired():
    """Raising sem alone must raise the kernel -- catches a dropped sem term."""
    dup = np.array([[1.0, 0.1], [0.1, 1.0]])
    low = build_kernel(np.array([[1.0, 0.62], [0.62, 1.0]]), dup, np.array([0, 1]), DEFAULT)
    high = build_kernel(np.array([[1.0, 0.99], [0.99, 1.0]]), dup, np.array([0, 1]), DEFAULT)
    assert high[0, 1] > low[0, 1] > 0.0


def test_within_class_scope_zeroes_cross_class_pairs():
    sem = np.full((3, 3), 0.9)
    np.fill_diagonal(sem, 1.0)
    dup = np.full((3, 3), 0.95)
    np.fill_diagonal(dup, 1.0)
    answers = np.array([0, 0, 1])
    S = build_kernel(sem, dup, answers, DEFAULT.with_(kernel_scope="WITHIN_CLASS"))
    assert S[0, 1] > 0.0
    assert S[0, 2] == pytest.approx(0.0)


def test_global_scope_ignores_duplication():
    sem = np.array([[1.0, 0.1], [0.1, 1.0]])
    dup = np.array([[1.0, 1.0], [1.0, 1.0]])
    S = build_kernel(sem, dup, np.array([0, 1]), DEFAULT.with_(kernel_scope="GLOBAL"))
    assert S[0, 1] == pytest.approx(0.0), "GLOBAL scope must use the semantic channel only"


def test_ngram_jaccard_endpoints():
    m = ngram_jaccard_matrix(["the cat sat on the mat", "the cat sat on the mat", "zzzzzzzzzz"])
    assert m[0, 1] == pytest.approx(1.0)
    assert m[0, 2] == pytest.approx(0.0)
    assert np.allclose(np.diag(m), 1.0)


# ------------------------------------------------------------------ guard margin
def _echo_case(m: int, r: int, n_answers: int = 2):
    n = m + r
    answers = np.array([1] * m + [0] * r)
    sem = np.full((n, n), 0.1)
    dup = np.full((n, n), 0.05)
    sem[:m, :m] = 1.0
    dup[:m, :m] = 1.0
    np.fill_diagonal(sem, 1.0)
    np.fill_diagonal(dup, 1.0)
    return answers, sem, dup


def test_guard_margin_delta_is_load_bearing():
    """A DDWC win smaller than (1 + delta) must NOT overturn the majority.

    Without this the margin clause could be deleted entirely and every other
    guard test would still pass.
    """
    answers, sem, dup = _echo_case(5, 4)
    counts = np.array([4.0, 5.0])
    assert essratio_dup(1, answers, dup, DEFAULT) <= DEFAULT.eta_dup  # guard is armed

    # W favours DDWC by only 10%, below the frozen delta = 0.15.
    W_small = np.array([1.10, 1.00])
    a, fired = guarded_answer(W_small, counts, answers, dup, DEFAULT)
    assert not fired and a == 1, "margin below (1+delta) must not overturn"

    # A 30% win clears the margin.
    W_big = np.array([1.30, 1.00])
    a, fired = guarded_answer(W_big, counts, answers, dup, DEFAULT)
    assert fired and a == 0


def test_guard_requires_all_three_conditions():
    answers, sem, dup = _echo_case(5, 4)
    counts = np.array([4.0, 5.0])
    W = np.array([10.0, 1.0])

    # (i) armed and clearly winning -> fires
    assert guarded_answer(W, counts, answers, dup, DEFAULT)[1]
    # (ii) no verbatim duplication -> disarmed, majority stands
    clean = np.full_like(dup, 0.05)
    np.fill_diagonal(clean, 1.0)
    a, fired = guarded_answer(W, counts, answers, clean, DEFAULT)
    assert not fired and a == 1
    # (iii) DDWC agrees with SC -> nothing to overturn
    a, fired = guarded_answer(np.array([1.0, 10.0]), counts, answers, dup, DEFAULT)
    assert not fired and a == 1


def test_essratio_arms_at_three_copies_under_frozen_defaults():
    """Operative threshold: 1/(1 + (m-1)*rho) <= eta_dup, i.e. m >= 3 at rho=0.7."""
    for m, armed in [(2, False), (3, True), (6, True)]:
        answers = np.zeros(m, dtype=int)
        dup = np.ones((m, m))
        ratio = essratio_dup(0, answers, dup, DEFAULT)
        assert ratio == pytest.approx(1.0 / (1.0 + (m - 1) * DEFAULT.rho))
        assert (ratio <= DEFAULT.eta_dup) is armed


# ------------------------------------------------------------------ VoI
def test_voi_is_nonnegative_and_support_consistent():
    """Baseline and candidates must share a support, else VoI is biased by a phantom cell."""
    mp = ModeProbability(n_mc=2048, seed=0)
    for alpha in ([4.0, 2.0, 2.0], [5.0, 3.0, 2.0], [6.0, 2.0, 1.0], [3.0, 3.0, 3.0]):
        v = value_of_information(np.array(alpha), 0.8, mp, DEFAULT.alpha0)
        assert v >= 0.0
    # A near-tie has more to learn from one more trace than a settled leader.
    tie = value_of_information(np.array([3.0, 3.0, 1.0]), 1.0, mp, DEFAULT.alpha0)
    settled = value_of_information(np.array([30.0, 2.0, 1.0]), 1.0, mp, DEFAULT.alpha0)
    assert tie > settled


def test_voi_shrinks_as_evidence_accumulates():
    """Diminishing returns: the same vote shape at larger n is worth less."""
    mp = ModeProbability(n_mc=2048, seed=0)
    vals = [
        value_of_information(np.array([2.0 * s, 1.0 * s, 1.0 * s]), 1.0, mp, DEFAULT.alpha0)
        for s in (1, 3, 10)
    ]
    assert vals[0] > vals[-1]


def test_voi_zero_weight_trace_carries_no_information():
    mp = ModeProbability(n_mc=1024, seed=0)
    assert value_of_information(np.array([5.0, 3.0, 2.0]), 0.0, mp, DEFAULT.alpha0) == pytest.approx(
        0.0, abs=1e-12
    )


# ------------------------------------------------------------------ cost model
def test_overhead_is_charged_per_channel_not_all_or_nothing():
    """dedup-SC computes one lexical channel and no embedding; it must pay less."""
    n, rho = 20, 1.0
    none = overhead_cost(n, rho, **PROFILE_NONE)
    dup = overhead_cost(n, rho, **PROFILE_DUP_ONLY)
    full = overhead_cost(n, rho, **PROFILE_FULL)
    assert none == 0.0
    assert 0 < dup < full
    pairs = sum(k - 1 for k in range(1, n + 1))
    assert dup == pytest.approx(pairs)
    assert full == pytest.approx(2 * pairs + KAPPA_EMB * n)


def test_overhead_matches_its_documented_derivation():
    """One embedding per trace plus `channels * (k-1)` comparisons at step k."""
    for n in (1, 5, 17):
        pairs = sum(k - 1 for k in range(1, n + 1))
        assert overhead_cost(n, 1.0, channels=2, embeds=True) == pytest.approx(2 * pairs + n)
    assert overhead_cost(0, 1.0, **PROFILE_FULL) == 0.0


def test_posterior_compute_is_on_the_cost_axis():
    """SPEC 4.4 puts posterior/VoI work on the x-axis; ablation (g) depends on it."""
    plain = overhead_cost(10, 1.0, **PROFILE_FULL, posterior_calls_per_step=2.0, kappa_post=0.05)
    with_voi = overhead_cost(10, 1.0, **PROFILE_FULL, posterior_calls_per_step=7.0, kappa_post=0.05)
    assert with_voi > plain


def test_rho_over_scales_only_overhead():
    pool = TracePool(
        answers=np.array([0, 1, 0]),
        confidences=np.full(3, 0.5),
        sem=np.eye(3),
        dup=np.eye(3),
        gen_tokens=np.full(3, 100.0),
        correct=0,
        n_answers=2,
    )
    gen = generation_cost(pool, 3)
    assert gen == pytest.approx(300.0)
    c1 = total_cost(pool, 3, 1.0, profile=PROFILE_FULL)
    c2 = total_cost(pool, 3, 2.0, profile=PROFILE_FULL)
    assert (c2 - gen) == pytest.approx(2.0 * (c1 - gen))


def test_generation_cost_counts_only_consumed_traces():
    pool = TracePool(
        answers=np.arange(5) % 2,
        confidences=np.full(5, 0.5),
        sem=np.eye(5),
        dup=np.eye(5),
        gen_tokens=np.array([10.0, 20.0, 30.0, 40.0, 50.0]),
        correct=0,
        n_answers=2,
    )
    assert generation_cost(pool, 3) == pytest.approx(60.0)
    assert generation_cost(pool, 5) == pytest.approx(150.0)


# ------------------------------------------------------------------ ablation switches
def _pool_with_echo():
    answers, sem, dup = _echo_case(6, 4)
    return TracePool(
        answers=answers,
        confidences=np.full(answers.size, 0.8),
        sem=sem,
        dup=dup,
        gen_tokens=np.full(answers.size, 100.0),
        correct=0,
        n_answers=2,
    )


def test_ablation_switches_change_behaviour():
    """stop_on_raw / force_sc_consensus / disable_guard must not be silent no-ops."""
    pool = _pool_with_echo()
    mp = ModeProbability(n_mc=DEFAULT.n_mc, seed=0)
    base = DEFAULT.with_(k_max=10, k_min=10, voi_branch=False, stop_variant="AGGRESSIVE")

    guarded = run_rlev_voi(pool, base, mp, use_conf=False)
    sc_cons = run_rlev_voi(pool, base.with_(force_sc_consensus=True), mp, use_conf=False)
    assert guarded.answer == 0 and guarded.guard_fired
    assert sc_cons.answer == 1, "force_sc_consensus must fall back to the plain majority"

    # Ablation (f): unguarded DDWC reaches the same answer here but without the
    # guard's protection -- the flag must run DDWC, not re-run SC.
    unguarded = run_rlev_voi(pool, base.with_(disable_guard=True), mp, use_conf=False)
    assert unguarded.answer == 0 and not unguarded.guard_fired


def test_stop_on_raw_uses_the_asc_criterion():
    """With DDWC consensus but raw-count stopping, the stop time must match ASC's."""
    from rlev_voi.baselines import run_adaptive_consistency
    from rlev_voi.simulate import REGIMES, generate_dataset

    mp = ModeProbability(n_mc=DEFAULT.n_mc, seed=2)
    cfg = DEFAULT.with_(k_max=24, voi_branch=False, stop_on_raw=True, tau=0.9)
    for pool in generate_dataset(REGIMES["R2_correlated_wrong"], 15, 24, seed=31):
        ours = run_rlev_voi(pool, cfg, mp, use_conf=False)
        asc = run_adaptive_consistency(pool, cfg, mp)
        assert ours.n_used == asc.n_used
