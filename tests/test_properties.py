"""Property tests for the architectural guarantees claimed in SPEC.md section 4.3.

These are the claims the spec makes *unconditionally*, so they are tested as
properties over randomised inputs rather than on hand-picked examples.
"""

from __future__ import annotations

import numpy as np
import pytest

from rlev_voi import DEFAULT, ModeProbability, TracePool, effective_counts, effective_weights, n_eff
from rlev_voi.algorithm import run_rlev_voi
from rlev_voi.baselines import run_adaptive_consistency
from rlev_voi.consensus import essratio_dup
from rlev_voi.kernel import build_kernel
from rlev_voi.posterior import exact_two_class_stability, posterior_alpha
from rlev_voi.simulate import REGIMES, generate_dataset


@pytest.fixture(scope="module")
def pools() -> list[TracePool]:
    """A mixed dataset spanning every regime."""
    out: list[TracePool] = []
    for i, cfg in enumerate(REGIMES.values()):
        out.extend(generate_dataset(cfg, 12, 24, seed=100 + i))
    return out


def test_safe_never_stops_earlier_than_asc(pools):
    """SAFE uses min(P_raw, P_eff) <= P_raw, so it can never stop before ASC.

    This is the honest architectural consequence the spec insists on stating:
    SAFE trades tokens for safety and cannot deliver a token-side win over ASC.
    """
    mp = ModeProbability(n_mc=DEFAULT.n_mc, seed=3)
    cfg = DEFAULT.with_(k_max=24, voi_branch=False, stop_variant="SAFE")
    for pool in pools:
        safe = run_rlev_voi(pool, cfg, mp, use_conf=False)
        asc = run_adaptive_consistency(pool, cfg, mp)
        assert safe.n_used >= asc.n_used


def test_posterior_never_uses_confidence(pools):
    """Scrambling confidence must not move the stopping time.

    The posterior sees only the redundancy channel; confidence acts on the
    consensus argmax alone. This is what makes the ASC reduction unconditional.
    """
    rng = np.random.default_rng(0)
    mp = ModeProbability(n_mc=DEFAULT.n_mc, seed=4)
    cfg = DEFAULT.with_(k_max=24, voi_branch=True, stop_variant="AGGRESSIVE")
    for pool in pools[:20]:
        scrambled = TracePool(
            answers=pool.answers,
            confidences=rng.permutation(pool.confidences),
            sem=pool.sem,
            dup=pool.dup,
            gen_tokens=pool.gen_tokens,
            correct=pool.correct,
            n_answers=pool.n_answers,
        )
        a = run_rlev_voi(pool, cfg, mp, use_conf=False)
        b = run_rlev_voi(scrambled, cfg, mp, use_conf=False)
        assert a.n_used == b.n_used


def test_effective_counts_sum_to_n_eff(pools):
    for pool in pools[:30]:
        S = build_kernel(pool.sem, pool.dup, pool.answers, DEFAULT)
        w = effective_weights(S, DEFAULT)
        N = effective_counts(w, pool.answers, pool.n_answers)
        assert float(N.sum()) == pytest.approx(n_eff(w))


def test_guard_silent_without_verbatim_duplication(pools):
    """No pair above theta_dup => the guard cannot arm, whatever the embeddings say."""
    for pool in pools:
        off = ~np.eye(pool.k_max, dtype=bool)
        if np.any(pool.dup[off] > DEFAULT.theta_dup):
            continue
        for a in range(pool.n_answers):
            if np.any(pool.answers == a):
                assert essratio_dup(a, pool.answers, pool.dup, DEFAULT) > DEFAULT.eta_dup


def test_aggressive_equals_safe_when_effective_is_less_concentrated(pools):
    """When P_eff <= P_raw the min() is P_eff, so the two variants must coincide."""
    mp = ModeProbability(n_mc=DEFAULT.n_mc, seed=5)
    base = DEFAULT.with_(k_max=24, voi_branch=False)
    for pool in pools[:25]:
        s = run_rlev_voi(pool, base.with_(stop_variant="SAFE"), mp, use_conf=False)
        a = run_rlev_voi(pool, base.with_(stop_variant="AGGRESSIVE"), mp, use_conf=False)
        if s.diagnostics["p_eff"] <= s.diagnostics["p_raw"]:
            assert s.n_used == a.n_used


def test_two_class_stability_is_a_probability_and_monotone():
    """Exact Beta stability: in [0,1], increases with the leader's lead."""
    prev = -1.0
    for lead in range(0, 12):
        p = exact_two_class_stability(np.array([1.0 + lead, 1.0]))
        assert 0.0 <= p <= 1.0
        assert p >= prev
        prev = p
    assert exact_two_class_stability(np.array([1.0, 1.0])) == pytest.approx(0.5)


def test_mode_probability_matches_exact_beta_on_two_classes():
    """The MC path and the closed form must agree where both apply."""
    mp = ModeProbability(n_mc=20000, seed=6)
    for alpha in ([3.0, 1.0], [8.0, 5.0], [2.5, 2.0], [20.0, 3.0]):
        a = np.array(alpha)
        assert mp(a) == pytest.approx(exact_two_class_stability(a), abs=1e-9)


def test_mode_probability_three_class_against_fresh_monte_carlo():
    """The deterministic common-random-numbers estimator must be unbiased.

    Checked against an independent, freshly-seeded Dirichlet sampler.
    """
    rng = np.random.default_rng(7)
    mp = ModeProbability(n_mc=40000, seed=8)
    for alpha in ([5.0, 3.0, 2.0], [10.0, 2.0, 1.0], [4.0, 4.0, 3.0]):
        a = np.array(alpha)
        ref = float(np.mean(np.argmax(rng.dirichlet(a, size=200000), axis=1) == int(np.argmax(a))))
        assert mp(a) == pytest.approx(ref, abs=0.01)


def test_mode_probability_is_permutation_invariant():
    """Load-bearing for the memoisation: a Dirichlet is exchangeable.

    ``P[argmax theta = argmax alpha]`` depends only on the multiset of alpha
    values, which is why the estimator can be cached on the sorted vector.
    """
    rng = np.random.default_rng(9)
    mp = ModeProbability(n_mc=512, seed=0, cache_decimals=12)
    for _ in range(60):
        k = int(rng.integers(2, 7))
        a = rng.uniform(0.5, 30.0, size=k)
        base = mp(a)
        for _ in range(3):
            assert mp(rng.permutation(a)) == pytest.approx(base, abs=1e-12)


def test_cache_rounding_does_not_change_results():
    """Rounding the cache key to 1e-3 must not perturb the estimate."""
    rng = np.random.default_rng(10)
    coarse = ModeProbability(n_mc=512, seed=0, cache_decimals=3)
    exact = ModeProbability(n_mc=512, seed=0, cache_decimals=12)
    for _ in range(300):
        a = rng.uniform(0.5, 30.0, size=int(rng.integers(2, 6)))
        assert coarse(a) == pytest.approx(exact(a), abs=1e-3)


def test_posterior_alpha_reduces_to_asc_at_identity():
    counts = np.array([4.0, 2.0, 1.0])
    assert np.allclose(posterior_alpha(counts, 1.0), np.array([5.0, 3.0, 2.0]))


def test_rho_zero_leaves_kernel_identity(pools):
    cfg = DEFAULT.with_(rho=0.0)
    for pool in pools[:10]:
        S = build_kernel(pool.sem, pool.dup, pool.answers, cfg)
        assert np.allclose(S, np.eye(pool.k_max))
        assert np.allclose(effective_weights(S, cfg), 1.0)
