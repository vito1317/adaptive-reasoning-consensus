"""Tests for ISC (docs/SPEC-ISC.md): the two theorems and the falsifiers F1-F4.

The two-world test (F4) is the theory's load-bearing check: on constructed
Prop-7 twins, the anchored instrument must decide the world at its declared
error rate, while any unanchored channel collection provably cannot.
"""

from __future__ import annotations

import numpy as np
import pytest

from rlev_voi.discrimination import item_discrimination
from rlev_voi.isc import estimate_isc, instrument_item, isc_vote, make_sim_verifier
from rlev_voi.simulate import Cluster, SimConfig, generate_dataset
from rlev_voi.tact import estimate_label_free, sc_answer
from rlev_voi.traces import TracePool

K = 12
RNG = np.random.default_rng(0)


def twin_pools(kappa: float = 0.6, m: int = 16, seed: int = 0) -> tuple[TracePool, TracePool]:
    """Construct a Prop-7 twin pair: identical observables, opposite worlds.

    World 1: correct = minority (1), kappa > 0 (confident minority is right).
    World 2: correct = majority (0), kappa < 0 -- SAME answers and confidences.
    """
    rng = np.random.default_rng(seed)
    a = np.array([0] * 10 + [1] * 6)
    y1 = (a == 1).astype(float)
    c = np.clip(0.5 + kappa * (y1 - 0.5) + rng.normal(0, 0.05, a.size), 0.01, 0.99)
    kw = dict(
        confidences=c, sem=np.eye(a.size), dup=np.eye(a.size),
        gen_tokens=np.full(a.size, 100.0), n_answers=2,
    )
    w1 = TracePool(answers=a, correct=1, **kw)
    w2 = TracePool(answers=a.copy(), correct=0, **kw)
    w1.meta["qid"] = f"w1-{seed}"
    w2.meta["qid"] = f"w2-{seed}"
    return w1, w2


# ------------------------------------------------------------- Theorem 1 (necessity)
def test_theorem1_unanchored_channels_cannot_distinguish_twins():
    """Any statistic of unanchored channels takes the same value on both twins.

    The twins share answers and confidences BY CONSTRUCTION, so this holds for
    every function of the pool; the test documents it concretely via the
    discrimination statistic computed against each world's truth.
    """
    w1, w2 = twin_pools()
    assert np.array_equal(w1.answers, w2.answers)
    assert np.allclose(w1.confidences, w2.confidences)
    d1 = item_discrimination(w1.confidences, (w1.answers == w1.correct).astype(int)).d
    d2 = item_discrimination(w2.confidences, (w2.answers == w2.correct).astype(int)).d
    assert d1 == pytest.approx(-d2)  # the flip: same observables, opposite implied signs


# ------------------------------------------------------------- Theorem 2 (sufficiency)
def test_theorem2_anchored_instrument_decides_the_world():
    """One anchored channel separates the twins, with error shrinking in n_V."""
    verify = make_sim_verifier(p_v=0.85, epsilon_sys=0.0)
    for n_v, min_rate in [(6, 0.55), (16, 0.80), (40, 0.95)]:
        correct = 0
        trials = 60
        for t in range(trials):
            w1, w2 = twin_pools(seed=t)
            rng = np.random.default_rng(1000 + t)
            r1 = instrument_item(w1, K, verify, n_v, rng, alpha_v=0.10)
            r2 = instrument_item(w2, K, verify, n_v, rng, alpha_v=0.10)
            correct += int(r1 is not None and r1.anchored == w1.correct)
            correct += int(r2 is not None and r2.anchored == w2.correct)
        rate = correct / (2 * trials)
        assert rate >= min_rate, f"n_v={n_v}: decision rate {rate:.2f} < {min_rate}"


def test_theorem2_error_control_undecided_not_wrong():
    """When the test does not pass, the item is UNDECIDED -- not answered wrongly."""
    verify = make_sim_verifier(p_v=0.85)
    wrong, decided, total = 0, 0, 0
    for t in range(80):
        w1, _ = twin_pools(seed=200 + t)
        r = instrument_item(w1, K, verify, 6, np.random.default_rng(t), alpha_v=0.05)
        if r is None:
            continue
        total += 1
        if r.anchored is not None:
            decided += 1
            wrong += int(r.anchored != w1.correct)
    assert decided > 0
    assert wrong / decided <= 0.15, f"decided-wrong rate {wrong}/{decided}"


# ------------------------------------------------------------- F1 headline: echo, label-free
def _echo_pools(n: int, seed: int) -> list[TracePool]:
    cfg = SimConfig(
        clusters=(
            Cluster(answer=0, weight=0.40, tightness=0.02),
            Cluster(answer=1, weight=0.60, tightness=0.30, echo_prob=0.85),
        ),
        n_answers=3,
        kappa_c=0.6,
        echo_conf=0.95,
    )
    return generate_dataset(cfg, n, 20, seed=seed)


def test_F1_isc_cracks_the_confident_echo_without_labels():
    """The cell where Prop. 7 forces every single-channel label-free method to
    refuse (TACT-LF returns SC = ~0.2): ISC with an artifact-independent
    verifier must recover most of the lost accuracy, still with zero labels."""
    pools = _echo_pools(120, seed=5)
    sc = float(np.mean([sc_answer(p.answers[:K], p.n_answers) == p.correct for p in pools]))

    lf = estimate_label_free(pools, K)
    tact_lf_acc = sc if lf.gamma == 0.0 else None  # alarms force SC here
    assert any(lf.alarms.values()), "TACT-LF should alarm on the confident echo"

    verify = make_sim_verifier(p_v=0.85, epsilon_sys=0.0)
    est = estimate_isc(pools, K, verify, n_v=8, instrument_fraction=0.5, seed=1)
    isc_acc = float(np.mean([isc_vote(p, i, K, est) == p.correct for i, p in enumerate(pools)]))
    assert sc < 0.45, f"echo cell should crush SC, got {sc}"
    assert isc_acc > sc + 0.25, f"ISC {isc_acc:.3f} must clearly beat the SC floor {sc:.3f}"


def test_F1_more_plain_votes_do_not_help_in_the_echo_cell():
    """The matched-budget contrast: spending the instrument budget on MORE
    PLAIN VOTES amplifies the echo instead of fixing it."""
    pools = _echo_pools(120, seed=6)
    small = float(np.mean([sc_answer(p.answers[:12], p.n_answers) == p.correct for p in pools]))
    big = float(np.mean([sc_answer(p.answers[:20], p.n_answers) == p.correct for p in pools]))
    assert big <= small + 0.02, f"extra votes should not help under echo: K12={small}, K20={big}"


# ------------------------------------------------------------- F2: no instrument tax
def test_F2_benign_negative_channel_isc_matches_tact_lf():
    """On the benign anti-correlated cell TACT-LF is already near-oracle;
    ISC must not degrade it (and its anchored labels should agree)."""
    base = (
        Cluster(answer=0, weight=0.45, tightness=0.02),
        Cluster(answer=1, weight=0.25, tightness=0.02),
        Cluster(answer=2, weight=0.18, tightness=0.02),
        Cluster(answer=3, weight=0.12, tightness=0.02),
    )
    pools = generate_dataset(SimConfig(clusters=base, kappa_c=-0.6), 150, 20, seed=7)
    lf = estimate_label_free(pools, K)
    verify = make_sim_verifier(p_v=0.85)
    est = estimate_isc(pools, K, verify, n_v=6, instrument_fraction=0.2, seed=2)
    assert np.sign(est.diagnostics["d_anchored"]) == np.sign(lf.diagnostics["d_raw"]) == -1
    lf_acc = float(np.mean([sc_answer(p.answers[:K], p.n_answers) == p.correct if lf.gamma == 0
                            else isc_vote(p, -1, K, type(est)(lf.gamma, {}, {})) == p.correct
                            for p in pools]))
    isc_acc = float(np.mean([isc_vote(p, i, K, est) == p.correct for i, p in enumerate(pools)]))
    assert isc_acc >= lf_acc - 0.02, f"instrument tax: ISC {isc_acc:.3f} vs TACT-LF {lf_acc:.3f}"


# ------------------------------------------------------------- F3: honest failure
def test_F3_systematic_belief_echo_triggers_fallback():
    """When the verifier shares the model's belief (epsilon > 1/2 on echo items),
    the anchor is invalid; ISC must detect it (I1/I3) or at minimum not fall
    below the SC floor it would have returned anyway."""
    pools = _echo_pools(120, seed=8)
    sc = float(np.mean([sc_answer(p.answers[:K], p.n_answers) == p.correct for p in pools]))
    broken = make_sim_verifier(p_v=0.85, epsilon_sys=1.0)  # always follows the belief
    est = estimate_isc(pools, K, broken, n_v=8, instrument_fraction=0.5, seed=3)
    isc_acc = float(np.mean([isc_vote(p, i, K, est) == p.correct for i, p in enumerate(pools)]))
    # With a fully invalid instrument the anchored answers just repeat the
    # plurality, so ISC should sit at (not below) the floor -- and never claim
    # the echo cell was solved.
    assert isc_acc <= sc + 0.10
    assert isc_acc >= sc - 0.05, f"broken instrument must not do worse than the floor: {isc_acc} vs {sc}"


# ------------------------------------------------------------- amortization
def test_amortization_channel_estimate_stabilizes_with_fixed_instrumented_count():
    """The channel measurement needs a fixed number of instrumented items,
    independent of corpus size: doubling the corpus at constant instrumented
    count must not degrade the sign estimate."""
    verify = make_sim_verifier(p_v=0.85)
    base = (
        Cluster(answer=0, weight=0.45, tightness=0.02),
        Cluster(answer=1, weight=0.35, tightness=0.10),
        Cluster(answer=2, weight=0.20, tightness=0.05),
    )
    for n_items in (100, 200):
        pools = generate_dataset(SimConfig(clusters=base, kappa_c=0.5), n_items, 20, seed=9)
        est = estimate_isc(pools, K, verify, n_v=6,
                           instrument_fraction=30 / n_items, seed=4)
        assert est.diagnostics["d_anchored"] > 0.2, (n_items, est.diagnostics)
