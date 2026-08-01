"""Proposition 7 holds only when the pool is effectively binary.

The proposition originally claimed the two worlds induce identical observable
laws outright. They do for two answer clusters. With three or more populated
clusters they separate: under {kappa>0, minority correct} only the correct
minority carries elevated confidence, while under {kappa<0, plurality correct}
every non-plurality cluster does, so a third cluster's conditional confidence
tells them apart. These tests pin both halves so the boundary cannot be
silently widened again.
"""

from __future__ import annotations

import numpy as np
from scipy.stats import ks_2samp

KAPPA, SD, N = 0.6, 0.10, 200_000


def _world(rng, probs, kappa, correct, n=N):
    a = rng.choice(len(probs), size=n, p=probs)
    c = np.clip(0.5 + kappa * ((a == correct).astype(float) - 0.5)
                + rng.normal(0, SD, n), 0.0, 1.0)
    return a, c


def _per_cluster_ks(probs):
    """KS p-value per answer cluster between world 1 and world 2."""
    rng = np.random.default_rng(0)
    a1, c1 = _world(rng, probs, +KAPPA, 1)   # w1: kappa>0, minority (1) correct
    a2, c2 = _world(rng, probs, -KAPPA, 0)   # w2: kappa<0, plurality (0) correct
    return [ks_2samp(c1[a1 == k][:5000], c2[a2 == k][:5000]).pvalue
            for k in range(len(probs))]


def test_binary_pool_is_genuinely_unidentifiable():
    """Two clusters: the observable laws coincide, so the impossibility binds."""
    for p in _per_cluster_ks([0.6, 0.4]):
        assert p > 1e-3, f"binary worlds should be indistinguishable, got KS p={p:.2e}"


def test_three_clusters_separate_the_worlds():
    """A populated third cluster breaks the tie, and only the third cluster does."""
    ps = _per_cluster_ks([0.55, 0.30, 0.15])
    assert ps[0] > 1e-3 and ps[1] > 1e-3, "the top two clusters must still agree"
    assert ps[2] < 1e-10, f"the third cluster must separate the worlds, got p={ps[2]:.2e}"


def test_signed_statistic_flips_between_the_worlds():
    """The part of the proposition that always holds: D^{w1} = -D^{w2}."""
    from rlev_voi.discrimination import item_discrimination

    rng = np.random.default_rng(1)
    a = np.array([0] * 9 + [1] * 6)
    conf = np.where(a == 1, 0.8, 0.2) + rng.normal(0, 0.01, a.size)
    d1 = item_discrimination(conf, (a == 1).astype(int))   # minority correct
    d2 = item_discrimination(conf, (a == 0).astype(int))   # plurality correct
    assert abs(d1.d + d2.d) < 1e-9, f"expected D^w1 = -D^w2, got {d1.d} and {d2.d}"


def test_echo_cell_is_effectively_binary():
    """The cell the paper applies the proposition to satisfies its precondition."""
    import importlib.util
    from pathlib import Path

    from rlev_voi.simulate import generate_dataset

    spec = importlib.util.spec_from_file_location(
        "tact_eval", Path(__file__).resolve().parents[1] / "experiments" / "run_tact_eval.py")
    TE = importlib.util.module_from_spec(spec)
    spec.loader.exec_module(TE)

    pools, k = generate_dataset(TE.ECHO_CFG, 300, 20, seed=7), 15
    no_third = 0
    for p in pools:
        counts = np.bincount(p.answers[:k], minlength=p.n_answers)
        no_third += int(np.sort(counts)[::-1][2:].sum() == 0)
    frac = no_third / len(pools)
    assert frac > 0.80, f"echo cell should be effectively binary, only {frac:.0%} of items are"
