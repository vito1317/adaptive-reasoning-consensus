"""TACT: Trust-Anchored Confidence Tempering (SPEC-TACT.md).

The vote is ``w_i = exp(gamma * phi_i)`` with ``phi`` the standardized van der
Waerden normal score of the trace's within-item confidence midrank; ``gamma``
comes from the measured signed discrimination of the channel via
:mod:`rlev_voi.tempering`. ``gamma == 0`` routes through the plain-SC code path,
making the zero-trust anchor bitwise exact.
"""

from __future__ import annotations

from dataclasses import dataclass, field

import numpy as np

from .discrimination import ItemStat, PooledD, item_discrimination, pooled_discrimination, vdw_scores
from .tempering import NU_LF, GAMMA_MAX_LF, TemperConfig, temper
from .traces import TracePool

# --------------------------------------------------------------------------
# Voting
# --------------------------------------------------------------------------


def sc_answer(answers: np.ndarray, n_answers: int) -> int:
    """Plain SC plurality with the canonical tie-break (lowest cluster id)."""
    counts = np.bincount(np.asarray(answers, dtype=int), minlength=n_answers)
    return int(np.argmax(counts))


def tact_vote(answers: np.ndarray, confidences: np.ndarray, n_answers: int, gamma: float) -> int:
    """Weighted plurality ``argmax_A sum_{i in A} exp(gamma * phi_i)``.

    At ``gamma == 0`` this CALLS the SC routine itself, so the zero-trust anchor
    is bitwise-identical to the SC baseline (ties included), not merely equal in
    distribution.
    """
    if gamma == 0.0:
        return sc_answer(answers, n_answers)
    phi = vdw_scores(confidences)
    w = np.exp(np.clip(gamma * phi, -50.0, 50.0))
    tally = np.bincount(np.asarray(answers, dtype=int), weights=w, minlength=n_answers)
    return int(np.argmax(tally))


# --------------------------------------------------------------------------
# TACT-dev
# --------------------------------------------------------------------------


@dataclass
class DevEstimate:
    gamma: float
    pooled: PooledD | None
    p_bar: float
    diagnostics: dict = field(default_factory=dict)


def estimate_dev(dev: list[TracePool], k: int, cfg: TemperConfig | None = None) -> DevEstimate:
    """TACT-dev: estimate (D, SE) on a labeled dev split, ship one scalar."""
    cfg = cfg or TemperConfig()
    stats: list[ItemStat] = []
    hits = []
    for pool in dev:
        c = pool.confidences[:k]
        y = (pool.answers[:k] == pool.correct).astype(int)
        hits.append(y)
        s = item_discrimination(c, y)
        if s is not None:
            stats.append(s)
    pooled = pooled_discrimination(stats)
    p_bar = float(np.clip(np.concatenate(hits).mean(), 0.05, 0.95)) if hits else 0.5
    if pooled is None:
        return DevEstimate(gamma=0.0, pooled=None, p_bar=p_bar, diagnostics={"reason": "no informative items"})
    gamma = temper(pooled.d_hat, pooled.se, TemperConfig(nu=cfg.nu, gamma_max=cfg.gamma_max, p_bar=p_bar, shrinker=cfg.shrinker))
    return DevEstimate(
        gamma=gamma,
        pooled=pooled,
        p_bar=p_bar,
        diagnostics={"d_hat": pooled.d_hat, "se": pooled.se, "z": pooled.z, "n_items": pooled.n_items},
    )


# --------------------------------------------------------------------------
# TACT-LF (label-free)
# --------------------------------------------------------------------------


def _dedup_weights(dup: np.ndarray, threshold: float = 0.95) -> tuple[np.ndarray, np.ndarray]:
    """Single-linkage duplicate groups at ``dup >= threshold``.

    Returns ``(group_id, weight)`` with ``weight_i = 1/|group(i)|``. Union-find
    keeps it O(m^2 alpha) on the cached similarity matrix.
    """
    m = dup.shape[0]
    parent = np.arange(m)

    def find(x: int) -> int:
        while parent[x] != x:
            parent[x] = parent[parent[x]]
            x = parent[x]
        return x

    for i in range(m):
        for j in range(i + 1, m):
            if dup[i, j] >= threshold:
                ri, rj = find(i), find(j)
                if ri != rj:
                    parent[ri] = rj
    roots = np.array([find(i) for i in range(m)])
    sizes = np.bincount(roots, minlength=m)[roots]
    return roots, 1.0 / sizes


@dataclass
class LFEstimate:
    gamma: float
    alarms: dict
    diagnostics: dict = field(default_factory=dict)


def estimate_label_free(
    pools: list[TracePool],
    k: int,
    dup_threshold: float = 0.95,
    margin_quantile: float = 0.40,
    nu: float = NU_LF,
    gamma_max: float = GAMMA_MAX_LF,
    n_splits: int = 20,
    n_boot: int = 200,
    att_floor: float = 0.20,
    min_gated_items: int = 50,
    seed: int = 0,
    trusted_sign: float | None = None,
) -> LFEstimate:
    """TACT-LF (SPEC-TACT 4.5): agreement pseudo-labels with poisoning defences.

    Pipeline: dedup -> dedup-weighted plurality pseudo-label -> margin gate ->
    pooled raw statistic (unbiased SIGN whenever the pair-weighted
    plurality-wrong rate is < 1/2) -> split-half de-attenuation (conservative:
    divide by the UPPER confidence bound of the attenuation) -> echo alarms.
    Any alarm, or an insignificant raw z, returns ``gamma = 0`` (pure SC).
    """
    rng = np.random.default_rng(seed)

    per_item = []
    for pool in pools:
        a = pool.answers[:k]
        c = pool.confidences[:k]
        dup = pool.dup[:k, :k]
        groups, dw = _dedup_weights(dup, dup_threshold)
        tally = np.bincount(a, weights=dw, minlength=pool.n_answers)
        order = np.argsort(tally)[::-1]
        plurality = int(order[0])
        share = tally / max(tally.sum(), 1e-12)
        margin = float(share[order[0]] - (share[order[1]] if order.size > 1 else 0.0))
        # Kish effective size of the dedup partition (E1 diagnostic input).
        gsizes = np.bincount(groups).astype(float)
        gsizes = gsizes[gsizes > 0]
        m_eff = float(gsizes.sum() ** 2 / np.sum(gsizes**2))
        per_item.append(
            dict(
                answers=a,
                conf=c,
                dedup_w=dw,
                plurality=plurality,
                margin=margin,
                m_eff_ratio=m_eff / k,
                n_distinct=int(np.unique(a).size),
                share=share,
            )
        )

    # ---- margin gate -----------------------------------------------------
    margins = np.array([it["margin"] for it in per_item])
    cut = float(np.quantile(margins, margin_quantile))
    gated = [it for it in per_item if it["margin"] >= cut and it["n_distinct"] >= 2]

    alarms: dict = {}
    # E1: duplicate collapse
    alarms["E1_duplicate_collapse"] = bool(np.median([it["m_eff_ratio"] for it in per_item]) < 0.5)
    # E4: too few gated informative items
    alarms["E4_too_few_items"] = bool(len(gated) < min_gated_items)

    # ---- raw agreement statistic ------------------------------------------
    stats = []
    for it in gated:
        g = (it["answers"] == it["plurality"]).astype(int)
        s = item_discrimination(it["conf"], g, pair_weights=it["dedup_w"])
        if s is not None:
            stats.append(s)
    pooled = pooled_discrimination(stats)
    if pooled is None:
        return LFEstimate(gamma=0.0, alarms=alarms, diagnostics={"reason": "no informative gated items"})

    # E2: SIGN-AWARE margin-decoupling. Let s = the trust direction (the sign
    # of the raw statistic, or the externally supplied one). On a benign
    # channel of EITHER sign, the plurality sits at the s-extreme of mean phi
    # on easy (high-margin) items and decouples on hard (low-margin) items, so
    # psi = f_low - f_high <= 0. An echo that would be AMPLIFIED by trusting
    # direction s keeps the coupling on hard items too (psi ~ 0 or > 0).
    # A sign-naive version of this test ("plurality has the highest mean phi")
    # false-alarms on every benign anti-correlated channel -- the plurality is
    # then the LOW-confidence cluster by construction.
    terciles = np.quantile(margins, [1 / 3, 2 / 3])
    trust_dir = float(np.sign(trusted_sign if trusted_sign is not None else pooled.d_hat)) or 1.0

    def plurality_at_trusted_extreme(it) -> bool:
        phi = vdw_scores(it["conf"])
        labels = [aa for aa in range(it["share"].size) if np.any(it["answers"] == aa)]
        means = [trust_dir * phi[it["answers"] == aa].mean() for aa in labels]
        return labels[int(np.argmax(means))] == it["plurality"]

    low = [it for it in per_item if it["margin"] <= terciles[0] and it["n_distinct"] >= 2]
    high = [it for it in per_item if it["margin"] >= terciles[1] and it["n_distinct"] >= 2]
    f_low = float(np.mean([plurality_at_trusted_extreme(it) for it in low])) if low else 0.0
    f_high = float(np.mean([plurality_at_trusted_extreme(it) for it in high])) if high else 0.0
    psi = f_low - f_high
    # With an externally trusted sign (semi-LF), the proxy-sign poisoning E2
    # guards against is moot -- the sign does not come from the proxy.
    alarms["E2_margin_decoupling"] = bool(psi > 0.05) and trusted_sign is None

    # ---- split-half de-attenuation ----------------------------------------
    agree = []
    for it in gated:
        a = it["answers"]
        m = a.shape[0]
        if m < 4:
            continue
        for _ in range(n_splits):
            perm = rng.permutation(m)
            h1, h2 = perm[: m // 2], perm[m // 2 :]
            p1 = np.argmax(np.bincount(a[h1], weights=it["dedup_w"][h1], minlength=it["share"].size))
            p2 = np.argmax(np.bincount(a[h2], weights=it["dedup_w"][h2], minlength=it["share"].size))
            agree.append(1.0 if p1 == p2 else 0.0)
    alpha = float(np.mean(agree)) if agree else 0.0

    # Effective number of wrong alternatives k = Keff - 1 via inverse Simpson
    # of the non-plurality mass, pooled over gated items.
    simpson = []
    for it in gated:
        rest = np.delete(it["share"], it["plurality"])
        mass = rest.sum()
        if mass > 1e-9:
            p = rest / mass
            simpson.append(1.0 / np.sum(p**2))
    k_eff = float(np.mean(simpson)) if simpson else 1.0
    k_wrong = max(k_eff, 1.0)

    def solve_p(alpha_val: float) -> tuple[float, float]:
        disc = 1.0 - (k_wrong + 1.0) * (1.0 - k_wrong * alpha_val)
        if disc <= 0:
            return 0.5, disc
        p = (1.0 + np.sqrt(disc)) / (k_wrong + 1.0)  # larger root: majority competence
        return float(np.clip(p, 0.5, 1.0)), float(disc)

    p_hat, disc = solve_p(alpha)
    alarms["E3_root_ambiguity"] = bool(disc < 0.02)

    # Bootstrap the UCB of the attenuation over gated items.
    if gated and agree:
        per_item_agree = np.array(agree).reshape(len([it for it in gated if it["answers"].shape[0] >= 4]), -1).mean(axis=1)
        boots = []
        for _ in range(n_boot):
            idx = rng.integers(0, per_item_agree.size, size=per_item_agree.size)
            boots.append(solve_p(float(per_item_agree[idx].mean()))[0])
        att_ucb = float(np.percentile([2 * b - 1 for b in boots], 95))
    else:
        att_ucb = 1.0
    att = float(np.clip(att_ucb, att_floor, 1.0))

    diagnostics = {
        "d_raw": pooled.d_hat,
        "se_raw": pooled.se,
        "z_raw": pooled.z,
        "alpha_split_half": alpha,
        "k_eff_wrong": k_wrong,
        "p_hat": p_hat,
        "attenuation_used": att,
        "psi_margin_decoupling": psi,
        "n_gated": len(gated),
    }

    if any(alarms.values()) or abs(pooled.z) <= nu:
        return LFEstimate(gamma=0.0, alarms=alarms, diagnostics=diagnostics)

    d_lf = float(np.clip(pooled.d_hat / att, -0.999, 0.999))
    if trusted_sign is not None and trusted_sign != 0:
        d_lf = float(np.sign(trusted_sign)) * abs(d_lf)
    se_lf = pooled.se / att
    gamma = temper(d_lf, se_lf, TemperConfig(nu=nu, gamma_max=gamma_max, p_bar=None))
    return LFEstimate(gamma=gamma, alarms=alarms, diagnostics=diagnostics)


def estimate_semi_lf(dev: list[TracePool], pools: list[TracePool], k: int, **lf_kwargs) -> LFEstimate:
    """Semi-label-free: SIGN from >=50 dev labels, MAGNITUDE from unlabeled traffic.

    The dev sign is passed INTO the label-free pipeline, which then (a) skips
    the proxy-sign-poisoning alarm E2 (moot when the sign is not taken from
    the proxy) and (b) reports |D_LF| with the trusted sign attached. Buys
    immunity to the label-free sign-ambiguity theorem with ~50 labels
    (SPEC-TACT 4.6). E1/E3/E4 still apply.
    """
    dev_est = estimate_dev(dev, k)
    sign = 0.0
    if dev_est.pooled is not None and abs(dev_est.pooled.z) > 1.0:
        sign = float(np.sign(dev_est.pooled.d_hat))
    if sign == 0.0:
        lf = estimate_label_free(pools, k, **lf_kwargs)
        return LFEstimate(gamma=0.0, alarms=lf.alarms, diagnostics=lf.diagnostics | {"semi_sign": 0.0})
    lf = estimate_label_free(pools, k, trusted_sign=sign, **lf_kwargs)
    return LFEstimate(gamma=lf.gamma, alarms=lf.alarms, diagnostics=lf.diagnostics | {"semi_sign": sign})
