"""TACT as one formula.

The shipped pipeline is five modules (ranks, discrimination, pooling,
tempering, voting). Written out, it is a single expression whose only free
quantity is the scalar exponent gamma:

    a_hat(q) = argmax_a  sum_{i : A_qi = a}  exp( gamma * phi_qi )

    gamma    = clip_{+-gmax} [ z * sqrt(2 + 4 p(1-p) z^2) ]

    z        = Phi^{-1}( (1 + D_tilde) / 2 )

    D_tilde  = D_hat * (1 - nu^2 / zeta^2)_+        zeta = D_hat / SE

    D_hat    = sum_q N_q (2 AUC_q - 1) / sum_q N_q

    phi_qi   = ( Phi^{-1}(R_qi/(m+1)) - mean_i ) / sd_i

Two algebraic simplifications get it there, both verified against the shipped
code in ``tests/test_formula.py``:

1. SHRINKAGE AS A GAIN. Positive-part James-Stein was written as
   ``sgn(D)(|D| - nu^2 SE^2/|D|)_+``. Factoring out ``D_hat`` turns it into a
   pure multiplicative gain ``(1 - nu^2/zeta^2)_+`` in the pooled z-statistic
   ``zeta`` alone, which also makes the dead zone read off directly as
   ``|zeta| <= nu`` rather than as a separate case.

2. THE LINK COLLAPSES. The Bayes-discriminant exponent
   ``u * sqrt(1 + p(1-p) u^2)`` with ``u = sqrt(2) Phi^{-1}(AUC)`` expands to
   ``z * sqrt(2 + 4 p(1-p) z^2)``; at the default ``p = 1/2`` that is exactly

       gamma = z * sqrt(2 + z^2),      z = Phi^{-1}(AUC)

   -- one probit and one square root, with no free parameter. The exponent was
   always derived rather than tuned; this form makes that visible.

The formula also states the program's empirical boundary exactly. ``gamma``
is zero on the whole dead zone ``|zeta| <= nu``, and zero gamma makes the
weighted plurality *identically* the unweighted one, so on every item where
the channel is not significant TACT is bitwise SC. Seven falsified designs and
a 2-5% addressable window (docs/GRAVEYARD.md) are the reason that is the right
default rather than a conservative one.
"""

from __future__ import annotations

import numpy as np
from scipy.stats import norm

from .discrimination import vdw_scores


def gamma_of(d_hat: float, se: float, nu: float, gamma_max: float,
             p_bar: float | None = 0.5) -> float:
    """The whole estimation half of TACT, in closed form.

    ``p_bar=None`` drops the mixture-variance correction, giving the
    conservative ``gamma = sqrt(2) z``.
    """
    if se <= 0:
        zeta = np.inf if d_hat != 0 else 0.0
    else:
        zeta = d_hat / se
    if not np.isfinite(zeta) or abs(zeta) <= nu:
        if not (np.isinf(zeta) and d_hat != 0):
            return 0.0

    gain = 1.0 - (nu / zeta) ** 2 if np.isfinite(zeta) else 1.0
    d_t = float(np.clip(d_hat * max(gain, 0.0), -1.0 + 1e-9, 1.0 - 1e-9))
    z = float(norm.ppf((1.0 + d_t) / 2.0))
    if p_bar is None:
        g = np.sqrt(2.0) * z
    else:
        p = float(np.clip(p_bar, 1e-6, 1.0 - 1e-6))
        g = z * np.sqrt(2.0 + 4.0 * p * (1.0 - p) * z * z)
    return float(np.clip(g, -gamma_max, gamma_max))


def tact(answers: np.ndarray, confidences: np.ndarray, n_answers: int,
         d_hat: float, se: float, nu: float, gamma_max: float,
         p_bar: float | None = 0.5) -> int:
    """TACT end to end: the displayed formula, evaluated.

    ``gamma == 0`` short-circuits to the unweighted plurality so the dead zone
    is bitwise SC including tie-breaks, not merely equal in distribution.
    """
    answers = np.asarray(answers, dtype=int)
    gamma = gamma_of(d_hat, se, nu, gamma_max, p_bar)
    if gamma == 0.0:
        return int(np.argmax(np.bincount(answers, minlength=n_answers)))
    phi = vdw_scores(confidences)
    w = np.exp(np.clip(gamma * phi, -50.0, 50.0))
    return int(np.argmax(np.bincount(answers, weights=w, minlength=n_answers)))
