"""Mandatory unit tests T1-T6 from SPEC.md section 5, plus the Kish counter-test.

These are the load-bearing correctness checks: they pin the estimator's limiting
behaviour analytically, so an implementation bug cannot hide behind a favourable
simulation. T2/T3 in particular are the tests the *previous* (Kish-ratio)
formulation failed -- :func:`test_kish_fails_T2_T3` asserts that failure
explicitly, so the correction cannot be silently reverted.
"""

from __future__ import annotations

import numpy as np
import pytest

from rlev_voi import (
    DEFAULT,
    ModeProbability,
    TracePool,
    block_model_effective_count,
    build_kernel,
    effective_counts,
    effective_weights,
    essratio_dup,
    guarded_answer,
    kish_dispersion,
    n_eff,
    posterior_alpha,
    raw_counts,
    run_adaptive_consistency,
    run_rlev_voi,
    run_self_consistency,
)
from rlev_voi.consensus import consensus_weights

K = 12


def block_kernel(sizes: list[int], rho: float) -> np.ndarray:
    """Block-diagonal kernel: within-block similarity ``rho``, unit diagonal."""
    n = sum(sizes)
    S = np.zeros((n, n))
    off = 0
    for m in sizes:
        S[off : off + m, off : off + m] = rho
        off += m
    np.fill_diagonal(S, 1.0)
    return S


def make_pool(answers, sem, dup, conf=None, n_answers=None, correct=0, tokens=200.0) -> TracePool:
    answers = np.asarray(answers, dtype=int)
    k = answers.size
    return TracePool(
        answers=answers,
        confidences=np.full(k, 0.8) if conf is None else np.asarray(conf, dtype=float),
        sem=sem,
        dup=dup,
        gen_tokens=np.full(k, tokens),
        correct=correct,
        n_answers=n_answers or int(answers.max()) + 1,
    )


# ---------------------------------------------------------------- T1
def test_T1_identity_kernel_reduces_to_raw_counts():
    """S = I  =>  w_i = 1, N_a^eff = n_a, alpha = alpha0 + n_a (exactly ASC)."""
    S = np.eye(K)
    w = effective_weights(S, DEFAULT)
    assert np.allclose(w, 1.0)

    answers = np.array([0, 0, 1, 2, 0, 1, 1, 1, 2, 0, 0, 1])
    N_eff = effective_counts(w, answers, 3)
    n_raw = raw_counts(answers, 3)
    assert np.allclose(N_eff, n_raw)
    assert np.allclose(posterior_alpha(N_eff, DEFAULT.alpha0), posterior_alpha(n_raw, DEFAULT.alpha0))
    assert n_eff(w) == pytest.approx(K)


def test_T1_rlev_voi_matches_adaptive_consistency_at_rho_zero():
    """The whole pipeline at rho=0 must reproduce ASC's answer AND stopping time.

    Answers are drawn from a *skewed* distribution so a clear leader emerges and
    both methods actually stop early. With uniform draws over 4 classes neither
    reaches ``tau`` and the assertion degenerates to ``40 == 40``, which passes
    regardless of whether the reduction holds.
    """
    rng = np.random.default_rng(7)
    cfg = DEFAULT.with_(rho=0.0, voi_branch=False, stop_variant="SAFE")
    mp = ModeProbability(n_mc=cfg.n_mc, seed=1)

    early_stops = 0
    for trial in range(30):
        k = 40
        p = [0.70, 0.15, 0.10, 0.05] if trial % 2 else [0.55, 0.25, 0.12, 0.08]
        answers = rng.choice(4, size=k, p=p)
        sem = np.clip(rng.uniform(0, 1, size=(k, k)), 0, 1)
        sem = 0.5 * (sem + sem.T)
        np.fill_diagonal(sem, 1.0)
        dup = np.clip(sem * 0.5, 0, 1)
        np.fill_diagonal(dup, 1.0)
        pool = make_pool(answers, sem, dup, n_answers=4)

        ours = run_rlev_voi(pool, cfg, mode_prob=mp, use_conf=False)
        asc = run_adaptive_consistency(pool, cfg, mode_prob=mp)
        assert ours.n_used == asc.n_used, f"trial {trial}: stopping time diverged"
        assert ours.answer == asc.answer, f"trial {trial}: answer diverged"
        early_stops += ours.n_used < 40
    assert early_stops >= 25, f"only {early_stops}/30 trials stopped early -- test is vacuous"


# ---------------------------------------------------------------- T2
def test_T2_all_ones_kernel_gives_one_effective_vote():
    """K identical copies must count as ONE effective vote, not K."""
    S = np.ones((K, K))
    w = effective_weights(S, DEFAULT)
    assert np.allclose(w, 1.0 / K)
    assert n_eff(w) == pytest.approx(1.0)


# ---------------------------------------------------------------- T3
def test_T3_two_equal_fully_correlated_blocks_give_two():
    """Two fully-correlated blocks => n_eff = 2, regardless of block size."""
    for m in (3, 5, 20):
        S = block_kernel([m, m], rho=1.0)
        assert n_eff(effective_weights(S, DEFAULT)) == pytest.approx(2.0)


# ---------------------------------------------------------------- T4
def test_T4_block_model_closed_form_and_limits():
    """N_g^eff = m / (1 + (m-1) rho), tending to 1 as rho->1 and m as rho->0."""
    for m in (2, 4, 9):
        for rho in (0.0, 0.25, 0.5, 0.9, 1.0):
            S = block_kernel([m], rho)
            got = n_eff(effective_weights(S, DEFAULT))
            assert got == pytest.approx(block_model_effective_count(m, rho))
        assert block_model_effective_count(m, 1.0) == pytest.approx(1.0)
        assert block_model_effective_count(m, 0.0) == pytest.approx(m)


def test_T4_per_answer_effective_counts_track_blocks():
    """Effective counts split across answers exactly as the block model predicts."""
    m_wrong, m_right = 6, 3
    S = block_kernel([m_wrong, m_right], rho=1.0)
    answers = np.array([1] * m_wrong + [0] * m_right)
    N = effective_counts(effective_weights(S, DEFAULT), answers, 2)
    assert N[1] == pytest.approx(1.0)  # six echoes -> one effective vote
    assert N[0] == pytest.approx(1.0)
    # Raw counts would have said 6 vs 3.
    assert raw_counts(answers, 2).tolist() == [3.0, 6.0]


# ---------------------------------------------------------------- T5
def test_T5_guard_fires_on_verbatim_echo():
    """m verbatim copies of a wrong answer must be overturned by the guard."""
    m, r = 5, 4
    n = m + r
    answers = np.array([1] * m + [0] * r)
    sem = np.full((n, n), 0.1)
    dup = np.full((n, n), 0.05)
    sem[:m, :m] = 1.0
    dup[:m, :m] = 1.0
    np.fill_diagonal(sem, 1.0)
    np.fill_diagonal(dup, 1.0)

    ratio = essratio_dup(1, answers, dup, DEFAULT)
    assert ratio == pytest.approx(1.0 / (1.0 + (m - 1) * DEFAULT.rho))
    assert ratio <= DEFAULT.eta_dup, "guard must be armed by a verbatim echo cluster"

    S = build_kernel(sem, dup, answers, DEFAULT)
    w = effective_weights(S, DEFAULT)
    W = consensus_weights(w, answers, 2, None, DEFAULT, use_conf=False)
    counts = raw_counts(answers, 2)
    assert int(np.argmax(counts)) == 1, "plain SC picks the echoed wrong answer"
    answer, fired = guarded_answer(W, counts, answers, dup, DEFAULT)
    assert fired and answer == 0


def test_T5_essratio_reaches_one_over_m_in_rho_limit():
    """The spec's headline 1/m holds exactly in the rho -> 1 limit."""
    m = 5
    answers = np.zeros(m, dtype=int)
    dup = np.ones((m, m))
    cfg = DEFAULT.with_(rho=1.0)
    assert essratio_dup(0, answers, dup, cfg) == pytest.approx(1.0 / m)


def test_T5_guard_silent_on_lexically_diverse_agreement():
    """A tight but lexically diverse correct cluster must NOT be discounted away."""
    m, r = 5, 4
    n = m + r
    answers = np.array([0] * m + [1] * r)
    sem = np.full((n, n), 0.1)
    dup = np.full((n, n), 0.05)
    sem[:m, :m] = 0.95  # semantically tight...
    dup[:m, :m] = 0.30  # ...but lexically distinct
    np.fill_diagonal(sem, 1.0)
    np.fill_diagonal(dup, 1.0)
    counts = raw_counts(answers, 2)
    S = build_kernel(sem, dup, answers, DEFAULT)
    W = consensus_weights(effective_weights(S, DEFAULT), answers, 2, None, DEFAULT, use_conf=False)
    answer, fired = guarded_answer(W, counts, answers, dup, DEFAULT)
    assert not fired and answer == 0


# ---------------------------------------------------------------- T6
def test_T6_rho_zero_is_plain_self_consistency():
    """rho = 0 must reproduce fixed-K Self-Consistency answer-for-answer."""
    rng = np.random.default_rng(11)
    cfg = DEFAULT.with_(rho=0.0, voi_branch=False)
    mp = ModeProbability(n_mc=cfg.n_mc, seed=2)
    for _ in range(25):
        k = 15
        answers = rng.integers(0, 3, size=k)
        sem = np.clip(rng.uniform(0.2, 1.0, size=(k, k)), 0, 1)
        sem = 0.5 * (sem + sem.T)
        np.fill_diagonal(sem, 1.0)
        dup = np.clip(sem, 0, 1)
        np.fill_diagonal(dup, 1.0)
        pool = make_pool(answers, sem, dup, n_answers=3)
        ours = run_rlev_voi(pool, cfg, mode_prob=mp, use_conf=False, force_n=k)
        sc = run_self_consistency(pool, k, cfg)
        assert ours.answer == sc.answer


# ------------------------------------------------- Kish counter-test (ablation d)
def test_kish_fails_T2_T3():
    """The rejected Kish dispersion ratio must fail exactly where the spec says.

    This is the reason the estimator was corrected: for K identical copies the
    weights are uniform, so Kish reports K independent votes instead of 1.
    """
    S = np.ones((K, K))
    w = effective_weights(S, DEFAULT)
    assert kish_dispersion(w) == pytest.approx(K)  # wrong: should be 1
    assert n_eff(w) == pytest.approx(1.0)  # the corrected estimator

    S2 = block_kernel([6, 6], rho=1.0)
    w2 = effective_weights(S2, DEFAULT)
    assert kish_dispersion(w2) == pytest.approx(12.0)  # wrong: should be 2
    assert n_eff(w2) == pytest.approx(2.0)


# ------------------------------------------------- estimator sanity
def test_weights_bounded():
    """w_i in [1/K, 1] -- removes the old 'huge 1/s_i outlier' failure mode."""
    rng = np.random.default_rng(3)
    for _ in range(20):
        k = int(rng.integers(2, 30))
        A = rng.uniform(0, 1, size=(k, k))
        S = 0.5 * (A + A.T)
        np.fill_diagonal(S, 1.0)
        w = effective_weights(S, DEFAULT)
        assert np.all(w <= 1.0 + 1e-12)
        assert np.all(w >= 1.0 / k - 1e-9)


def test_n_eff_between_one_and_k():
    rng = np.random.default_rng(4)
    for _ in range(20):
        k = int(rng.integers(2, 30))
        A = rng.uniform(0, 1, size=(k, k))
        S = 0.5 * (A + A.T)
        np.fill_diagonal(S, 1.0)
        e = n_eff(effective_weights(S, DEFAULT))
        assert 1.0 - 1e-9 <= e <= k + 1e-9


def test_kernel_symmetric_unit_diagonal():
    rng = np.random.default_rng(5)
    k = 10
    sem = np.clip(rng.uniform(size=(k, k)), 0, 1)
    dup = np.clip(rng.uniform(size=(k, k)), 0, 1)
    answers = rng.integers(0, 3, size=k)
    S = build_kernel(sem, dup, answers, DEFAULT)
    assert np.allclose(S, S.T)
    assert np.allclose(np.diag(S), 1.0)
    off = S[~np.eye(k, dtype=bool)]
    assert off.min() >= 0.0 and off.max() <= DEFAULT.rho + 1e-12
