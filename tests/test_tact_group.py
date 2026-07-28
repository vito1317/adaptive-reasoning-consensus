"""TACT-group and the item-level impossibility results.

Two halves. The first pins the NEGATIVE result: with i.i.d. latent per-item
coupling, any method that maps the item's own agreement statistic monotonically
to an exponent collapses to plurality reinforcement (~SC), and the agreement
statistic's sign OPPOSES the true sign on exactly the plurality-wrong items
where a flip could win (winner's curse). The second shows the positive
counterpart: once heterogeneity is indexed by an observable covariate,
per-group TACT recovers each group's signed coupling and cracks the floor.
"""

from __future__ import annotations

import numpy as np
import pytest

from rlev_voi.discrimination import item_discrimination
from rlev_voi.simulate import Cluster, SimConfig, generate_dataset
from rlev_voi.tact import (
    estimate_dev_by_group,
    estimate_lf_by_group,
    group_vote,
    sc_answer,
    tact_vote,
)
from rlev_voi.tempering import discriminant_link

BASE = (
    Cluster(answer=0, weight=0.45, tightness=0.02),
    Cluster(answer=1, weight=0.25, tightness=0.02),
    Cluster(answer=2, weight=0.18, tightness=0.02),
    Cluster(answer=3, weight=0.12, tightness=0.02),
)
K = 15


def _iid_hetero(n=300, seed=0):
    return generate_dataset(SimConfig(clusters=BASE, kappa_c=0.0, kappa_c_sd=0.6), n, 20, seed=seed)


def _grouped(n=600, seed=0, kappas=(0.6, 0.0, -0.6)):
    return generate_dataset(SimConfig(clusters=BASE, group_kappas=kappas), n, 20, seed=seed)


# ------------------------------------------------------------- impossibility
def test_naive_per_item_hier_is_plurality_reinforcement():
    """gamma from the item's OWN agreement statistic ~= SC, with harmful flips.

    D^g > 0 => trust confident traces => they agree with the plurality;
    D^g < 0 => trust unconfident traces => those are the plurality side too.
    Either way the plurality is reinforced, so the method cannot beat SC.
    """
    data = _iid_hetero(seed=100)
    agree, flips_right, flips_wrong = 0, 0, 0
    for p in data:
        a, c = p.answers[:K], p.confidences[:K]
        plur = sc_answer(a, p.n_answers)
        s = item_discrimination(c, (a == plur).astype(int))
        d = s.d if s is not None else 0.0
        gamma = float(np.clip(discriminant_link(np.clip(d, -0.99, 0.99), 0.5), -4, 4))
        ans = tact_vote(a, c, p.n_answers, gamma)
        if ans == plur:
            agree += 1
        elif ans == p.correct:
            flips_right += 1
        else:
            flips_wrong += 1
    assert agree / len(data) > 0.9, "self-referential hier should track SC"
    assert flips_wrong >= flips_right, "its rare flips should not be net-helpful"


def test_winners_curse_sign_opposition():
    """On plurality-wrong items the agreement sign OPPOSES the true sign."""
    data = _iid_hetero(n=500, seed=101)
    same_sign, n = 0, 0
    for p in data:
        a, c = p.answers[:K], p.confidences[:K]
        plur = sc_answer(a, p.n_answers)
        if plur == p.correct:
            continue
        st = item_discrimination(c, (a == p.correct).astype(int))
        if st is None or abs(st.d) < 0.3:
            continue
        sg = item_discrimination(c, (a == plur).astype(int))
        if sg is None or sg.d == 0:
            continue
        n += 1
        same_sign += int(np.sign(st.d) == np.sign(sg.d))
    assert n > 20
    assert same_sign / n < 0.25, f"sign agreement {same_sign/n:.0%} should be far below chance"


def test_two_world_unidentifiability():
    """{kappa>0, minority correct} and {kappa<0, plurality correct} produce the
    same observable (answers, confidences) law -- shown by construction: one
    sample is literally consistent with both worlds after relabeling truth."""
    rng = np.random.default_rng(9)
    a = np.array([0] * 9 + [1] * 6)
    # world 1: correct = 1 (minority), kappa = +0.6 -> minority confident
    c = np.clip(0.5 + 0.6 * ((a == 1).astype(float) - 0.5) + rng.normal(0, 0.05, 15), 0.01, 0.99)
    d_w1 = item_discrimination(c, (a == 1).astype(int)).d  # truth = 1
    d_w2 = item_discrimination(c, (a == 0).astype(int)).d  # truth = 0
    # identical observables, opposite implied signs: no label-free method can
    # distinguish the worlds from (a, c) alone.
    assert d_w1 == pytest.approx(-d_w2)


# ------------------------------------------------------------- TACT-group
def test_group_dev_recovers_per_group_signs():
    data = _grouped(n=600, seed=1)
    gammas, global_est = estimate_dev_by_group(data, K)
    assert gammas[0] > 1.0  # kappa +0.6
    assert abs(gammas[1]) < 0.6  # kappa 0 (dead zone or tiny)
    assert gammas[2] < -1.0  # kappa -0.6
    # the global estimate over the mixture is comparatively small
    assert abs(global_est.gamma) < max(abs(gammas[0]), abs(gammas[2]))


def test_group_lf_recovers_signs_without_labels():
    data = _grouped(n=600, seed=2)
    gammas, _ = estimate_lf_by_group(data, K)
    assert gammas[0] > 0.5
    assert gammas[2] < -0.5


def test_group_vote_cracks_the_floor():
    dev = _grouped(n=600, seed=3)
    test = _grouped(n=600, seed=4)
    gammas, global_est = estimate_dev_by_group(dev, K)
    sc = float(np.mean([sc_answer(p.answers[:K], p.n_answers) == p.correct for p in test]))
    grp = float(np.mean([group_vote(p, K, gammas, global_est.gamma) == p.correct for p in test]))
    glob = float(
        np.mean(
            [tact_vote(p.answers[:K], p.confidences[:K], p.n_answers, global_est.gamma) == p.correct for p in test]
        )
    )
    assert grp > sc + 0.05, f"group TACT {grp:.3f} must beat the SC floor {sc:.3f}"
    assert grp > glob + 0.05, f"group TACT {grp:.3f} must beat global TACT {glob:.3f}"


def test_small_groups_fall_back_to_global():
    data = _grouped(n=40, seed=5)  # ~13 items per group < min_items
    gammas, global_est = estimate_dev_by_group(data, K, min_items=30)
    assert all(g == global_est.gamma for g in gammas.values())
