"""Frozen default configuration for RLEV-VoI.

Per SPEC.md section 6, a SINGLE frozen default config is the headline. Anything
tuned per-dataset/per-regime is reported separately and labelled an upper bound.
The guard parameters (``delta``, ``eta_dup``) are frozen across ALL regimes and
datasets so the guard cannot be tuned per-regime to satisfy every falsifier.
"""

from __future__ import annotations

from dataclasses import dataclass, replace
from typing import Literal

KernelScope = Literal["DECOMP", "WITHIN_CLASS", "GLOBAL"]
StopVariant = Literal["SAFE", "AGGRESSIVE"]


@dataclass(frozen=True)
class Config:
    """Frozen defaults from SPEC.md section 6."""

    # --- kernel -----------------------------------------------------------
    rho: float = 0.7
    """Global discount strength. ``rho == 0`` => S = I => exact Self-Consistency."""
    theta_dup: float = 0.9
    gamma_dup: float = 6.0
    theta_sem: float = 0.6
    gamma_sem: float = 3.0
    beta_sem: float = 0.25
    kernel_scope: KernelScope = "DECOMP"

    # --- confidence channel (consensus only; never enters the posterior) ---
    use_conf_gate: bool = True
    conf_gate_ece: float = 0.10
    gamma_c: float = 1.0

    # --- never-worse-than-SC guard (FROZEN across all regimes/datasets) ----
    delta: float = 0.15
    eta_dup: float = 0.5

    # --- posterior --------------------------------------------------------
    alpha0: float = 1.0

    # --- stopping ---------------------------------------------------------
    tau: float = 0.95
    tau_floor: float = 0.80
    lam: float = 1e-3
    k_min: int = 5
    k_max: int = 40
    stop_variant: StopVariant = "SAFE"
    voi_branch: bool = True
    stop_on_raw: bool = False
    """Ablation (h): stop on the raw ASC posterior while still using DDWC for
    consensus. Isolates the stopping change from the consensus change."""
    disable_guard: bool = False
    """Ablation (f): run DDWC UNGUARDED (answer = argmax_a W_a).

    This measures the regression the guard prevents, which is the point of the
    ablation -- suppressing DDWC entirely would instead just re-run SC."""
    force_sc_consensus: bool = False
    """Ablation (h): use the plain-SC consensus rule while keeping the effective
    -count stopping rule, isolating the stopping change from the consensus one."""

    # --- estimators -------------------------------------------------------
    n_mc: int = 512
    """Monte-Carlo samples for the mode probability when |A| > 2."""

    # --- weights ----------------------------------------------------------
    w_clip_lo: float = 1e-3
    w_clip_hi: float = 1.0

    # --- cost accounting --------------------------------------------------
    rho_over: float = 1.0
    """Overhead scale applied to all non-generation work."""
    kappa_post: float = 0.05
    """Token-equivalent cost of ONE Monte-Carlo mode-probability evaluation.

    SPEC.md 4.4 puts posterior/VoI compute on the cost axis. Without it the VoI
    variant -- which does several times the posterior work of a plain threshold
    -- would be compared to it at nominally identical cost, and ablation (g)
    would be decided by an accounting omission."""

    def with_(self, **kwargs) -> "Config":
        """Return a copy with fields overridden (keeps the frozen dataclass honest)."""
        return replace(self, **kwargs)


DEFAULT = Config()

#: ``rho=0`` collapses the kernel to the identity, which makes the whole
#: pipeline reduce to plain Self-Consistency + Adaptive-Consistency exactly.
SC_EQUIVALENT = DEFAULT.with_(rho=0.0)
