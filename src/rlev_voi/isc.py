"""ISC: Instrumented Self-Consistency (docs/SPEC-ISC.md).

The instrument decides the *world* (Theorem 2's one-sided Mann-Whitney on
anchored verification scores), the base channel is then measured against
instrument-anchored pseudo-labels with TACT's machinery, and TACT's tempering
map produces the vote weights. One rank statistic, used twice.
"""

from __future__ import annotations

import zlib
from dataclasses import dataclass, field
from typing import Callable

import numpy as np
from scipy.stats import mannwhitneyu

from .discrimination import item_discrimination, pooled_discrimination
from .tact import _dedup_weights, sc_answer, tact_vote
from .tempering import NU_LF, GAMMA_MAX_LF, TemperConfig, temper
from .traces import TracePool

#: An instrument is a callable (pool, candidate_answer, n_queries, rng) -> scores.
#: Scores are anchored: higher means "more likely correct", with the SIGN of
#: that relationship guaranteed by construction (Theorem 2's premise).
InstrumentFn = Callable[[TracePool, int, int, np.random.Generator], np.ndarray]


@dataclass
class ItemInstrumentation:
    """Outcome of instrumenting one item."""

    candidates: tuple[int, int]
    anchored: int | None
    """The Mann-Whitney winner among the top-2 candidates, or None (undecided)."""
    p_value: float
    margin: float
    """Rank-biserial effect of the winning side, in [0, 1]."""
    n_queries: int


def instrument_item(
    pool: TracePool,
    k: int,
    instrument: InstrumentFn,
    n_v: int,
    rng: np.random.Generator,
    alpha_v: float = 0.10,
) -> ItemInstrumentation | None:
    """Decide the world for one item via anchored verification (Theorem 2).

    Queries are split evenly across the top-2 dedup-weighted candidates; the
    one-sided Mann-Whitney test on the anchored scores names the winner. Items
    with a single observed answer are not instrumented (nothing to decide).
    """
    a = pool.answers[:k]
    _, dw = _dedup_weights(pool.dup[:k, :k])
    tally = np.bincount(a, weights=dw, minlength=pool.n_answers)
    order = np.argsort(tally)[::-1]
    if tally[order[1]] <= 0:
        return None
    top2 = (int(order[0]), int(order[1]))

    n_each = max(n_v // 2, 1)
    s0 = instrument(pool, top2[0], n_each, rng)
    s1 = instrument(pool, top2[1], n_each, rng)

    try:
        u_stat, p_greater = mannwhitneyu(s0, s1, alternative="greater")
        _, p_less = mannwhitneyu(s0, s1, alternative="less")
    except ValueError:  # all scores identical
        return ItemInstrumentation(top2, None, 1.0, 0.0, 2 * n_each)

    # rank-biserial effect r = 2U/(n0*n1) - 1 for candidate 0 over candidate 1
    r = 2.0 * float(u_stat) / (len(s0) * len(s1)) - 1.0
    # Two one-sided tests are run, so the family-wise level is 2*alpha_v unless
    # each is held to alpha_v/2. The uncorrected version measured a 0.17-0.22
    # false-decision rate at a nominal 0.10.
    half = alpha_v / 2.0
    if p_greater <= half:
        return ItemInstrumentation(top2, top2[0], float(p_greater), abs(r), 2 * n_each)
    if p_less <= half:
        return ItemInstrumentation(top2, top2[1], float(p_less), abs(r), 2 * n_each)
    return ItemInstrumentation(top2, None, min(float(p_greater), float(p_less)), abs(r), 2 * n_each)


@dataclass
class ISCEstimate:
    gamma: float
    anchored_answers: dict
    """qid-index -> anchored answer for decisively instrumented items."""
    diagnostics: dict = field(default_factory=dict)


def estimate_isc(
    pools: list[TracePool],
    k: int,
    instrument: InstrumentFn,
    n_v: int = 6,
    instrument_fraction: float = 0.3,
    alpha_v: float = 0.10,
    nu: float = NU_LF,
    gamma_max: float = GAMMA_MAX_LF,
    min_decided: int = 8,
    seed: int = 0,
) -> ISCEstimate:
    """The two-phase ISC estimator (SPEC-ISC section 4). Label-free throughout.

    Phase A instruments the lowest-margin ``instrument_fraction`` of items and
    decides their worlds. Phase B measures the base channel against pseudo-labels
    that use the anchored answer where decided (plurality elsewhere) and tempers
    with TACT's map. Diagnostics I1-I3 guard against weak/invalid instruments;
    any alarm returns gamma = 0 with no anchored overrides beyond the decisive
    items themselves.
    """
    rng = np.random.default_rng(seed)

    # ---- Phase A: choose and instrument the least-trustworthy items ----------
    margins = []
    for idx, pool in enumerate(pools):
        a = pool.answers[:k]
        _, dw = _dedup_weights(pool.dup[:k, :k])
        tally = np.bincount(a, weights=dw, minlength=pool.n_answers)
        share = tally / max(tally.sum(), 1e-12)
        srt = np.sort(share)[::-1]
        margins.append(float(srt[0] - (srt[1] if srt.size > 1 else 0.0)))
    margins = np.array(margins)
    n_instr = max(int(round(instrument_fraction * len(pools))), 1)
    chosen = np.argsort(margins)[:n_instr]

    anchored: dict[int, int] = {}
    # Keep (index, result) paired: instrument_item returns None for
    # single-answer items, so zipping `chosen` against a filtered result list
    # silently misaligns every later item's margin.
    paired: list[tuple[int, ItemInstrumentation]] = []
    for idx in chosen:
        res = instrument_item(pools[idx], k, instrument, n_v, rng, alpha_v)
        if res is None:
            continue
        paired.append((int(idx), res))
        if res.anchored is not None:
            anchored[int(idx)] = res.anchored
    results = [r for _, r in paired]

    decided = [r for r in results if r.anchored is not None]
    # I1: instrument decisiveness
    median_margin = float(np.median([r.margin for r in results])) if results else 0.0
    i1_weak = median_margin < 0.30 or len(decided) < min_decided
    # I2: agreement with the plurality among decided items
    agree_plu = [
        1.0 if r.anchored == r.candidates[0] else 0.0 for r in decided
    ]
    agree_rate = float(np.mean(agree_plu)) if agree_plu else 1.0
    # I3: where do disagreements live? Uniform-in-margin disagreement suggests a
    # broken instrument; low-margin-concentrated disagreement is the poisoned-
    # vote pattern the instrument exists to catch. Compare mean margins.
    dis_idx = [i for i, r in paired if r.anchored is not None and r.anchored != r.candidates[0]]
    agr_idx = [i for i, r in paired if r.anchored is not None and r.anchored == r.candidates[0]]
    i3_suspicious = False
    if len(dis_idx) >= 3 and len(agr_idx) >= 3:
        i3_suspicious = float(np.mean(margins[dis_idx])) > float(np.mean(margins[agr_idx])) + 0.10

    # ---- Phase B: anchored pseudo-labels -> TACT statistic -> temper ---------
    stats = []
    for idx, pool in enumerate(pools):
        a = pool.answers[:k]
        c = pool.confidences[:k]
        if int(idx) in anchored:
            ref = anchored[int(idx)]
        else:
            _, dw = _dedup_weights(pool.dup[:k, :k])
            ref = int(np.argmax(np.bincount(a, weights=dw, minlength=pool.n_answers)))
        g = (a == ref).astype(int)
        s = item_discrimination(c, g)
        if s is not None:
            stats.append(s)
    pooled = pooled_discrimination(stats)

    diagnostics = {
        "n_instrumented": len(results),
        "n_decided": len(decided),
        "median_instrument_margin": median_margin,
        "agreement_with_plurality": agree_rate,
        "I1_weak_instrument": bool(i1_weak),
        "I3_margin_pattern_suspicious": bool(i3_suspicious),
        "d_anchored": pooled.d_hat if pooled else 0.0,
        "se": pooled.se if pooled else 0.0,
        "z": pooled.z if pooled else 0.0,
    }

    if pooled is None or i1_weak or i3_suspicious:
        # Weak or suspicious instrument: keep only the decisive per-item
        # overrides (they carry their own significance test) but do not trust
        # the channel measurement.
        return ISCEstimate(gamma=0.0, anchored_answers=anchored, diagnostics=diagnostics)

    gamma = temper(pooled.d_hat, pooled.se, TemperConfig(nu=nu, gamma_max=gamma_max, p_bar=None))
    return ISCEstimate(gamma=gamma, anchored_answers=anchored, diagnostics=diagnostics)


def isc_vote(pool: TracePool, idx: int, k: int, est: ISCEstimate) -> int:
    """Vote: anchored override where the instrument was decisive, tempered
    weighted vote elsewhere."""
    if idx in est.anchored_answers:
        return est.anchored_answers[idx]
    return tact_vote(pool.answers[:k], pool.confidences[:k], pool.n_answers, est.gamma)


# --------------------------------------------------------------------------
# Simulated instruments (SPEC-ISC section 3) with the validity knob epsilon.
# --------------------------------------------------------------------------


def make_sim_verifier(p_v: float = 0.85, epsilon_sys: float = 0.0) -> InstrumentFn:
    """A simulated verification channel.

    With probability ``1 - epsilon_sys`` the item is 'checkable': each query
    endorses a correct candidate w.p. ``p_v`` and an incorrect one w.p.
    ``1 - p_v`` (anchored, Theorem 2). With probability ``epsilon_sys`` the
    verifier shares the model's systematic belief: it endorses the POOL'S
    plurality answer as if it were correct — the exclusion-restriction
    violation of the Corollary, which turns a poisoned vote into a poisoned
    instrument.
    """

    def verify(pool: TracePool, candidate: int, n: int, rng: np.random.Generator, k: int | None = None) -> np.ndarray:
        # Item-level systematic failure is a property of the item, not the
        # query: draw it once per pool from a deterministically seeded
        # generator. Python's hash() is salted per process, so using it here
        # made every 0 < epsilon_sys < 1 experiment irreproducible.
        item_rng = np.random.default_rng(
            zlib.crc32(str(pool.meta.get("qid", "")).encode()) ^ 0x5EED
        )
        systematic = item_rng.random() < epsilon_sys
        if systematic:
            # Read the plurality at the SAME budget the caller votes at, not
            # over the whole cached pool -- they differ often enough to matter.
            kk = k if k is not None else pool.k_max
            believed = sc_answer(pool.answers[:kk], pool.n_answers)
            p_endorse = p_v if candidate == believed else 1.0 - p_v
        else:
            p_endorse = p_v if candidate == pool.correct else 1.0 - p_v
        return (rng.random(n) < p_endorse).astype(float)

    return verify
