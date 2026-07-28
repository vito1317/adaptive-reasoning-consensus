"""Tests for TACT (SPEC-TACT.md): anchors, statistic, tempering map, LF defences.

Each mathematical claim in the spec is pinned numerically here, including the
four §10 pre-implementation checks: the JS-EB identity, the van Elteren null
variance against brute-force permutation, the mixture-variance link derivation,
and the split-half quadratic roots.
"""

from __future__ import annotations

import numpy as np
import pytest
from scipy.stats import norm

from rlev_voi.discrimination import (
    item_discrimination,
    midranks,
    pooled_discrimination,
    vdw_scores,
)
from rlev_voi.simulate import Cluster, SimConfig, generate_dataset
from rlev_voi.tact import (
    estimate_dev,
    estimate_label_free,
    estimate_semi_lf,
    sc_answer,
    tact_vote,
)
from rlev_voi.tempering import (
    GAMMA_MAX_DEV,
    TemperConfig,
    discriminant_link,
    js_shrink,
    lcb_shrink,
    temper,
)

RNG = np.random.default_rng(0)


# ----------------------------------------------------------------- anchors
def test_A1_gamma_zero_is_bitwise_sc():
    """gamma == 0 must route through the SC code path on every input."""
    for _ in range(200):
        m = int(RNG.integers(2, 30))
        n_ans = int(RNG.integers(2, 6))
        a = RNG.integers(0, n_ans, size=m)
        c = RNG.uniform(0.01, 0.99, size=m)
        assert tact_vote(a, c, n_ans, 0.0) == sc_answer(a, n_ans)


def test_A1_dead_zone_probability_under_null():
    """Under D_true = 0, the dev dead zone catches ~80% (nu = 1.2816)."""
    hits = 0
    trials = 300
    for t in range(trials):
        rng = np.random.default_rng(1000 + t)
        stats = []
        for _ in range(60):
            m = 12
            c = rng.uniform(size=m)
            y = rng.integers(0, 2, size=m)  # label independent of c
            s = item_discrimination(c, y)
            if s is not None:
                stats.append(s)
        pooled = pooled_discrimination(stats)
        if pooled is not None and js_shrink(pooled.d_hat, pooled.se, 1.2816) == 0.0:
            hits += 1
    assert hits / trials > 0.70, f"dead-zone rate {hits/trials:.2f} too low under the null"


def test_A2_logval_phi_reproduces_cisc_power():
    """w = exp(gamma*(log c - mean log c)) must rank identically to c^gamma."""
    for _ in range(100):
        m = int(RNG.integers(3, 25))
        n_ans = int(RNG.integers(2, 5))
        a = RNG.integers(0, n_ans, size=m)
        c = RNG.uniform(0.05, 0.99, size=m)
        gamma = float(RNG.uniform(0.2, 4.0))
        phi = np.log(c) - np.mean(np.log(c))
        w_tact = np.exp(gamma * phi)
        w_cisc = c**gamma
        t1 = np.bincount(a, weights=w_tact, minlength=n_ans)
        t2 = np.bincount(a, weights=w_cisc, minlength=n_ans)
        # identical up to a positive per-item constant => identical shares
        assert np.allclose(t1 / t1.sum(), t2 / t2.sum())


def test_monotone_invariance_of_the_whole_vote():
    """Strictly increasing distortions of c must not change any TACT vote."""
    for _ in range(100):
        m = int(RNG.integers(4, 30))
        n_ans = 3
        a = RNG.integers(0, n_ans, size=m)
        c = RNG.uniform(0.01, 0.99, size=m)
        gamma = float(RNG.uniform(-3, 3))
        base = tact_vote(a, c, n_ans, gamma)
        for f in (lambda x: x**4, lambda x: 0.5 + 0.1 * (x - 0.5), lambda x: 1 / (1 + np.exp(-6 * (x - 0.5)))):
            assert tact_vote(a, f(c), n_ans, gamma) == base


# ----------------------------------------------------------------- statistic
def test_null_variance_matches_permutation():
    """Section 10 check: the tie-corrected van Elteren null SE vs brute force."""
    rng = np.random.default_rng(5)
    m, n_items = 10, 40
    # fixed confidences WITH ties to exercise the correction
    base_c = np.round(rng.uniform(size=m), 1)
    d_hats = []
    for _ in range(3000):
        stats = []
        for _ in range(n_items):
            y = np.zeros(m, dtype=int)
            y[rng.choice(m, size=4, replace=False)] = 1
            s = item_discrimination(base_c, y)
            stats.append(s)
        d_hats.append(pooled_discrimination(stats).d_hat)
    empirical_se = float(np.std(d_hats))
    stats = [item_discrimination(base_c, np.array([1] * 4 + [0] * 6))]
    # analytic SE0 for the pooled statistic with identical items:
    one = stats[0]
    se0_pooled = np.sqrt(n_items * (one.n_pairs**2) * one.var0_d) / (n_items * one.n_pairs)
    assert empirical_se == pytest.approx(se0_pooled, rel=0.10)


def test_d_is_monotone_invariant():
    rng = np.random.default_rng(6)
    c = rng.uniform(size=20)
    y = rng.integers(0, 2, size=20)
    if y.sum() in (0, 20):
        y[0] = 1 - y[0]
    d1 = item_discrimination(c, y).d
    d2 = item_discrimination(c**3, y).d
    d3 = item_discrimination(0.5 + 0.2 * (c - 0.5), y).d
    assert d1 == pytest.approx(d2) == pytest.approx(d3)


def test_d_sign_flips_with_anticorrelation():
    rng = np.random.default_rng(7)
    stats_pos, stats_neg = [], []
    for _ in range(50):
        y = rng.integers(0, 2, size=16)
        if y.sum() in (0, 16):
            y[0] = 1 - y[0]
        noise = rng.normal(scale=0.1, size=16)
        c_pos = np.clip(0.5 + 0.3 * (y - 0.5) + noise, 0.01, 0.99)
        stats_pos.append(item_discrimination(c_pos, y))
        stats_neg.append(item_discrimination(1 - c_pos, y))
    assert pooled_discrimination(stats_pos).d_hat > 0.3
    assert pooled_discrimination(stats_neg).d_hat < -0.3
    assert pooled_discrimination(stats_neg).d_hat == pytest.approx(-pooled_discrimination(stats_pos).d_hat)


def test_vdw_scores_standardized_and_tie_safe():
    c = RNG.uniform(size=25)
    phi = vdw_scores(c)
    assert float(np.mean(phi)) == pytest.approx(0.0, abs=1e-12)
    assert float(np.std(phi)) == pytest.approx(1.0, abs=1e-9)
    assert np.allclose(vdw_scores(np.full(10, 0.7)), 0.0)  # all ties -> SC


# ----------------------------------------------------------------- tempering
def test_js_eb_identity():
    """Section 10 check: JS at nu=1 equals the EB posterior mean with plug-in tau."""
    for d, se in [(0.3, 0.1), (0.5, 0.3), (-0.4, 0.15), (0.05, 0.1)]:
        tau2 = max(0.0, d**2 - se**2)
        eb = d * tau2 / (tau2 + se**2) if tau2 > 0 else 0.0
        assert js_shrink(d, se, 1.0) == pytest.approx(eb, abs=1e-12)


def test_shrinkers_share_dead_zone_and_ordering():
    for _ in range(100):
        d = float(RNG.uniform(-1, 1))
        se = float(RNG.uniform(0.01, 0.5))
        nu = 1.2816
        j, l = js_shrink(d, se, nu), lcb_shrink(d, se, nu)
        assert (j == 0.0) == (l == 0.0) == (abs(d) <= nu * se)
        assert abs(j) >= abs(l) - 1e-12  # JS under-trusts strong signals less
        assert abs(j) <= abs(d) + 1e-12


def test_link_values_and_mixture_correction():
    """Section 10 check: gamma* = u*sqrt(1 + p(1-p)u^2) from the unit-mixture model."""
    for d in (0.1, 0.3, 0.5, 0.7, 0.9):
        u = np.sqrt(2) * norm.ppf((1 + d) / 2)
        assert discriminant_link(d, p_bar=None) == pytest.approx(u, rel=1e-9)
        for p in (0.3, 0.5, 0.7):
            want = u * np.sqrt(1 + p * (1 - p) * u**2)
            assert discriminant_link(d, p_bar=p) == pytest.approx(want, rel=1e-9)
    # spot values from the spec: L(0.5)=0.954, L(0.9)=2.326 (uncorrected)
    assert discriminant_link(0.5, None) == pytest.approx(0.954, abs=2e-3)
    assert discriminant_link(0.9, None) == pytest.approx(2.326, abs=2e-3)


def test_temper_is_odd_monotone_and_capped():
    cfg = TemperConfig()
    prev = None
    for d in np.linspace(-0.99, 0.99, 41):
        g = temper(float(d), 0.05, cfg)
        assert g == pytest.approx(-temper(float(-d), 0.05, cfg), abs=1e-12)
        assert abs(g) <= GAMMA_MAX_DEV + 1e-12
        if prev is not None:
            assert g >= prev - 1e-12
        prev = g
    assert temper(0.0, 0.05, cfg) == 0.0
    assert temper(0.3, 1.0, cfg) == 0.0  # huge SE -> dead zone


# ----------------------------------------------------------------- CCN attenuation
def test_poisoning_attenuation_is_linear_in_flip_rate():
    """E[D_g] ~= (1 - 2*rho) * D_true under class-conditional label noise."""
    rng = np.random.default_rng(8)
    d_true_stats = []
    for _ in range(400):
        y = rng.integers(0, 2, size=20)
        if y.sum() in (0, 20):
            y[0] = 1 - y[0]
        c = np.clip(0.5 + 0.3 * (y - 0.5) + rng.normal(scale=0.15, size=20), 0.01, 0.99)
        d_true_stats.append((c, y, item_discrimination(c, y)))
    d_true = pooled_discrimination([s for _, _, s in d_true_stats]).d_hat

    for rho in (0.1, 0.25, 0.4):
        stats = []
        for c, y, _ in d_true_stats:
            flip = rng.random(y.size) < rho  # flip independent of c given y (CCN)
            g = np.where(flip, 1 - y, y)
            if g.sum() in (0, g.size):
                continue
            stats.append(item_discrimination(c, g))
        d_g = pooled_discrimination(stats).d_hat
        assert d_g == pytest.approx((1 - 2 * rho) * d_true, abs=0.06), f"rho={rho}"


def test_split_half_quadratic_roots():
    """Section 10 check: alpha = p^2 + (1-p)^2/k inverts correctly."""
    for k in (1.0, 2.0, 4.0):
        for p in (0.55, 0.7, 0.9):
            alpha = p**2 + (1 - p) ** 2 / k
            disc = 1 - (k + 1) * (1 - k * alpha)
            root = (1 + np.sqrt(disc)) / (k + 1)
            assert root == pytest.approx(p, abs=1e-9)


# ----------------------------------------------------------------- end-to-end
def _pools(kappa: float, n: int = 120, k: int = 16, seed: int = 0, **kw):
    cfg = SimConfig(
        clusters=(
            Cluster(answer=0, weight=0.45, tightness=0.02),
            Cluster(answer=1, weight=0.25, tightness=0.02),
            Cluster(answer=2, weight=0.18, tightness=0.02),
            Cluster(answer=3, weight=0.12, tightness=0.02),
        ),
        kappa_c=kappa,
        **kw,
    )
    return generate_dataset(cfg, n, k, seed=seed)


def test_dev_estimator_recovers_sign_and_deadzones_null():
    k = 16
    pos = estimate_dev(_pools(+0.6, seed=1), k)
    neg = estimate_dev(_pools(-0.6, seed=2), k)
    nul = estimate_dev(_pools(0.0, seed=3), k)
    assert pos.gamma > 0.5
    assert neg.gamma < -0.5
    assert nul.gamma == pytest.approx(0.0, abs=0.3)  # usually exactly 0


def test_dev_gamma_transfers_across_budgets():
    """D is pairwise, so the estimate at m=16 should be close at m=8."""
    big = estimate_dev(_pools(0.6, seed=4, k=16), 16)
    small = estimate_dev(_pools(0.6, seed=5, k=16), 8)
    assert big.pooled.d_hat == pytest.approx(small.pooled.d_hat, abs=0.12)


def test_lf_recovers_positive_channel_and_alarms_on_confident_echo():
    k = 16
    lf = estimate_label_free(_pools(+0.6, n=200, seed=6), k)
    assert lf.gamma > 0.3, f"LF failed to trust a good channel: {lf.diagnostics}"
    assert not any(lf.alarms.values())

    # Confident echo: wrong cluster echoes verbatim with high confidence.
    cfg = SimConfig(
        clusters=(
            Cluster(answer=0, weight=0.40, tightness=0.02),
            Cluster(answer=1, weight=0.60, tightness=0.30, echo_prob=0.85),
        ),
        n_answers=3,
        kappa_c=0.6,
        echo_conf=0.95,
    )
    poisoned = generate_dataset(cfg, 200, k, seed=7)
    lf2 = estimate_label_free(poisoned, k)
    assert any(lf2.alarms.values()) or lf2.gamma <= 0.05, (
        f"confident echo must trigger an alarm or the dead zone: "
        f"gamma={lf2.gamma} alarms={lf2.alarms} diag={lf2.diagnostics}"
    )


def test_semi_lf_uses_dev_sign():
    k = 16
    dev = _pools(-0.6, n=60, seed=8)
    traffic = _pools(-0.6, n=200, seed=9)
    est = estimate_semi_lf(dev, traffic, k)
    assert est.gamma <= 0.0
