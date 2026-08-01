"""The one-formula statement must be the shipped pipeline, not a paraphrase.

Every test here compares ``rlev_voi.formula`` against the modules it claims to
condense, over randomised inputs including the boundaries (dead zone edge,
saturating |D|, zero SE, all-tied confidences, negative channels).
"""

from __future__ import annotations

import numpy as np
import pytest
from scipy.stats import norm

from rlev_voi.formula import gamma_of, tact
from rlev_voi.tact import sc_answer, tact_vote
from rlev_voi.tempering import GAMMA_MAX_DEV, GAMMA_MAX_LF, NU_DEV, NU_LF, TemperConfig, temper


@pytest.mark.parametrize("nu,gmax", [(NU_DEV, GAMMA_MAX_DEV), (NU_LF, GAMMA_MAX_LF)])
@pytest.mark.parametrize("p_bar", [0.5, 0.3, None])
def test_gamma_matches_temper(nu, gmax, p_bar):
    rng = np.random.default_rng(0)
    worst = 0.0
    for _ in range(4000):
        d = float(rng.uniform(-0.99, 0.99))
        se = float(rng.uniform(1e-4, 0.6))
        a = gamma_of(d, se, nu, gmax, p_bar)
        b = temper(d, se, TemperConfig(nu=nu, gamma_max=gmax, p_bar=p_bar))
        worst = max(worst, abs(a - b))
    assert worst < 1e-9, f"closed form deviates from the pipeline by {worst:.2e}"


def test_shrinkage_is_a_gain_in_the_z_statistic():
    """|D_tilde| = |D_hat| * (1 - nu^2/zeta^2)_+ is the same map as the
    original sgn(D)(|D| - nu^2 SE^2/|D|)_+."""
    rng = np.random.default_rng(1)
    for _ in range(4000):
        d = float(rng.uniform(-0.99, 0.99))
        se = float(rng.uniform(1e-4, 0.6))
        zeta = d / se
        gain = max(1.0 - (nu := NU_DEV) ** 2 / zeta**2, 0.0)
        direct = np.sign(d) * max(abs(d) - nu**2 * se**2 / abs(d), 0.0)
        assert abs(d * gain - direct) < 1e-12


def test_link_collapses_to_z_sqrt_2_plus_z_squared():
    """At p = 1/2 the discriminant link is exactly z*sqrt(2 + z^2)."""
    for auc in np.linspace(0.001, 0.999, 999):
        z = norm.ppf(auc)
        u = np.sqrt(2.0) * z
        original = u * np.sqrt(1.0 + 0.25 * u * u)
        collapsed = z * np.sqrt(2.0 + z * z)
        assert abs(original - collapsed) < 1e-12


def test_dead_zone_is_exactly_the_z_statistic_threshold():
    for nu in (NU_DEV, NU_LF):
        assert gamma_of(0.30, 0.30 / nu * 1.0000001, nu, 4.0) == 0.0   # |zeta| < nu
        assert gamma_of(0.30, 0.30 / nu * 0.9999999, nu, 4.0) != 0.0   # |zeta| > nu
        assert gamma_of(0.0, 0.1, nu, 4.0) == 0.0
        assert gamma_of(-0.8, 0.05, nu, 4.0) < 0.0                     # signed


def test_vote_matches_pipeline_and_is_bitwise_sc_in_the_dead_zone():
    rng = np.random.default_rng(2)
    for _ in range(2000):
        m = int(rng.integers(4, 25))
        k = int(rng.integers(2, 6))
        a = rng.integers(0, k, m)
        c = rng.random(m)
        d = float(rng.uniform(-0.9, 0.9))
        se = float(rng.uniform(1e-3, 0.5))
        g = gamma_of(d, se, NU_DEV, GAMMA_MAX_DEV)
        assert tact(a, c, k, d, se, NU_DEV, GAMMA_MAX_DEV) == tact_vote(a, c, k, g)
        if g == 0.0:
            assert tact(a, c, k, d, se, NU_DEV, GAMMA_MAX_DEV) == sc_answer(a, k)


def test_all_tied_confidences_degenerate_to_sc():
    rng = np.random.default_rng(3)
    a = rng.integers(0, 4, 12)
    c = np.full(12, 0.9)
    assert tact(a, c, 4, 0.8, 0.02, NU_DEV, GAMMA_MAX_DEV) == sc_answer(a, 4)


def test_gamma_is_odd_and_monotone():
    rng = np.random.default_rng(4)
    se = 0.05
    for _ in range(500):
        d = float(rng.uniform(0.2, 0.95))
        assert abs(gamma_of(d, se, NU_DEV, 10.0) + gamma_of(-d, se, NU_DEV, 10.0)) < 1e-9
    ds = np.linspace(0.2, 0.95, 60)
    gs = [gamma_of(d, se, NU_DEV, 10.0) for d in ds]
    assert all(b >= a - 1e-12 for a, b in zip(gs, gs[1:]))
    ses = np.linspace(0.01, 0.3, 60)
    gs2 = [gamma_of(0.6, s, NU_DEV, 10.0) for s in ses]
    assert all(b <= a + 1e-12 for a, b in zip(gs2, gs2[1:]))
