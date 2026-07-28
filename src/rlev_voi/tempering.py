"""The tempering map: (D_hat, SE) -> vote exponent gamma (SPEC-TACT 4.3).

Two composed pieces with exact anchor behaviour:

* positive-part James-Stein shrinkage with a significance floor -- the dead
  zone ``|D_hat| <= nu*SE`` returns exactly 0 (=> the caller runs plain SC);
* the Bayes-discriminant link with the mixture-variance correction -- the
  exponent is DERIVED, not grid-searched.
"""

from __future__ import annotations

from dataclasses import dataclass

import numpy as np
from scipy.stats import norm

#: One-sided significance floors (SPEC-TACT 6).
NU_DEV = 1.2816
NU_LF = 2.326
GAMMA_MAX_DEV = 4.0
GAMMA_MAX_LF = 2.0


def js_shrink(d_hat: float, se: float, nu: float) -> float:
    """Positive-part James-Stein with significance floor ``nu``.

    ``D~ = sign(D)*max(0, |D| - nu^2 SE^2/|D|)``; dead zone iff ``|D| <= nu*SE``.
    With ``nu = 1`` this IS the empirical-Bayes posterior mean under a
    ``N(0, tau^2)`` prior with the plug-in ``tau^2 = max(0, D^2 - SE^2)``.
    Properties: odd, continuous, ``|D~| <= |D|``, monotone in ``D``,
    anti-monotone in ``SE``.
    """
    if se <= 0:
        return d_hat
    a = abs(d_hat)
    if a <= nu * se:
        return 0.0
    return float(np.sign(d_hat) * (a - nu**2 * se**2 / a))


def lcb_shrink(d_hat: float, se: float, nu: float) -> float:
    """One-sided lower-confidence-bound soft threshold (ablation alternative).

    Same dead zone as :func:`js_shrink`; subtracts ``nu*SE`` linearly, which is
    more conservative for strong signals. Kept for the ablation comparing
    shrinkers; JS is the default because it under-trusts strong channels less.
    """
    a = abs(d_hat)
    return float(np.sign(d_hat) * max(0.0, a - nu * se))


def discriminant_link(d: float, p_bar: float | None = 0.5) -> float:
    """Bayes-optimal exponent under the working model (SPEC-TACT 4.3).

    ``u = sqrt(2)*Phi^{-1}((1+D)/2)``;  ``gamma* = u*sqrt(1 + p(1-p)u^2)``.

    Derivation: within an item let ``phi | y ~ N(mu_y, s^2)`` with the *mixture*
    standardized to unit variance (which is what :func:`vdw_scores` enforces).
    Then ``1 = s^2 + p(1-p)Delta^2`` forces ``s^2 = 1/(1 + p(1-p)u^2)`` where
    ``u = Delta/s = sqrt(2)*Phi^{-1}(AUC)``, and the optimal per-trace log-weight
    coefficient is ``Delta/s^2 = u/s``. Passing ``p_bar=None`` disables the
    correction (``gamma* = u``), which under-weights strong channels by up to
    ~50% at ``D = 0.9`` but is the conservative choice when ``p`` is unknown.
    """
    d = float(np.clip(d, -1.0 + 1e-9, 1.0 - 1e-9))
    u = float(np.sqrt(2.0) * norm.ppf((1.0 + d) / 2.0))
    if p_bar is None:
        return u
    p = float(np.clip(p_bar, 1e-6, 1.0 - 1e-6))
    return u * float(np.sqrt(1.0 + p * (1.0 - p) * u**2))


@dataclass(frozen=True)
class TemperConfig:
    nu: float = NU_DEV
    gamma_max: float = GAMMA_MAX_DEV
    p_bar: float | None = 0.5
    shrinker: str = "js"  # js | lcb


def temper(d_hat: float, se: float, cfg: TemperConfig = TemperConfig()) -> float:
    """The composite map ``g``: continuous, odd, monotone in ``D_hat``,
    anti-monotone in ``SE``, ``g(0, .) = 0``, ``g(D, 0+) = gamma*(D)``."""
    shrink = js_shrink if cfg.shrinker == "js" else lcb_shrink
    d_t = shrink(d_hat, se, cfg.nu)
    if d_t == 0.0:
        return 0.0
    gamma = discriminant_link(d_t, cfg.p_bar)
    return float(np.clip(gamma, -cfg.gamma_max, cfg.gamma_max))
