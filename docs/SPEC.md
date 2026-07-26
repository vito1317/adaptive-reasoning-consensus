# RLEV-VoI: Robust Leverage-Effective-Vote Consensus with Value-of-Information Stopping
### (Final, red-team-revised specification)

---

## 1. Name & Abstract

**RLEV-VoI** is an inference-time reasoning pipeline for a **frozen** LLM that (i) aggregates chain-of-thought (CoT) votes with a redundancy-discounted "effective vote" weight `w_i = 1/Σ_j S_ij` (inverse-similarity-mass / inverse-density weighting), and (ii) sequentially decides when to stop sampling using a **design-effect-corrected Dirichlet–multinomial posterior** over *effective* vote counts, optionally combined with a value-of-information (VoI) per-token cutoff.

The shared technical spine is a **Rao–Scott design-effect correction** applied to CoT voting: replace the raw category count `n_a` by the *coherent effective count*
```
N_a^eff = Σ_{i: a_i = a} w_i ,   w_i = 1 / Σ_j S_ij ,
α_a = α₀ + N_a^eff ,   with total effective count  n_eff = Σ_i w_i = tr(D⁻¹S) ∈ [1, K].
```
This reduces **exactly** to Adaptive-Consistency when traces are independent (`S = I ⇒ w_i = 1 ⇒ N_a^eff = n_a`), and, in the block-similarity limit, correctly collapses a cluster of `m` fully-correlated echoes to **one** effective vote.

We are explicit and honest about positioning (see §2 and §10): **the coupling itself is not new** — it is the classical effective-sample-size / design-effect correction (Rao & Scott 1981/1984) composed with Adaptive-Consistency's Dirichlet posterior (Aggarwal 2023) using Kish/inverse-density effective counts. The contribution is therefore **not** a new estimator but an **engineered, honestly-benchmarked assembly** with three defensible robustness pieces: a **duplication-vs-semantic kernel decomposition**, a **never-worse-than-SC guard**, and a **safe/aggressive stopping pair**; plus a **fair, non-circular empirical protocol** that measures *when redundancy-discounting helps vs. backfires* on real LLM traces. If the assembly does not Pareto-dominate RASC+ASC and VecCISC+ASC under identical token accounting on real data, the honest outcome is a rigorous negative/robustness result.

> **Prior-version correction (critical).** Earlier drafts set `n_eff` to the **Kish dispersion ratio** `(Σw)²/Σw²` and declared `α₀ + W_a` "wrong." That was backwards. The Kish ratio measures weight *dispersion*, not independent-vote count, and returns `K` for `K` identical copies (uniform weights). The **correct** effective count is the weight sum `Σ_i w_i = tr(D⁻¹S)`, which — with redundancy-only weights — makes `α_a = α₀ + N_a^eff` the right form. This is now the spine, and the S→all-ones and equal-block limits are mandatory unit tests (§5, §8.a).

---

## 2. Honest Novelty Positioning

**Prior art we explicitly build on and do NOT claim as new:**

- **Redundancy discounting for correlated CoT:** fitness sharing (Goldberg & Richardson 1987); Kish ESS for correlated LLM votes ("Nine Judges, Two Effective Votes", 2605.29800); semantic-entropy clustering (Kuhn 2023; Farquhar et al. 2024); VecCISC (2605.08070), RASC (2408.17017).
- **The closed form `w_i = 1/Σ_j S_ij`:** by our own admission this is Goldberg–Richardson fitness sharing, inverse-density / `D⁻¹` graph-degree weighting, and a cheap `O(K²)` surrogate for ridge-leverage `τ_i = [S(S+λI)⁻¹]_ii` (Alaoui & Mahoney 2015). Claimed only as an *instantiation*.
- **The design-effect / effective-sample-size correction `n_eff = n/DEFF`:** this is **Rao & Scott (JASA 1981; Ann. Statist. 1984)**, standard in complex-survey statistics for 40+ years. Feeding effective counts into a Dirichlet posterior is the Bayesian analog and a one-line composition of Kish-ESS (2605.29800) + Adaptive-Consistency (2305.11860).
- **Confidence fold-in:** CISC (2502.06233) / DiVeRSe / weighted-SC.
- **Dirichlet "stop when leader is the mode ≥ τ":** IS Adaptive-Consistency's criterion, and Optimal Bayesian Stopping (2602.05395).
- **VoI / cost-normalized optimal stopping:** classical (Raiffa & Schlaifer 1961; Wald SPRT; Howard 1966; Weitzman 1979), already ported to test-time LLMs (2510.01394; 2410.02725; MARS 2606.12935; 2605.26849).

**Weakened, honest claims (novel *combination / engineering*, not novel ideas):**

1. **[Weakened from "novel spine" to "application"] Rao–Scott design-effect correction for CoT voting.** `α_a = α₀ + N_a^eff` with the **coherent** effective count `N_a^eff = Σ_{i:a_i=a} 1/s_i`. We claim only that (a) applying the effective-count correction to CoT self-consistency stopping, with the inverse-similarity-mass estimator, and (b) getting the estimator *right* (weight-sum, not Kish dispersion), is a useful, correctly-calibrated engineering choice. We cite Rao–Scott, Kish-ESS, and ASC as the composed components.
2. **[Engineering safety distinction] Duplication-vs-semantic kernel decomposition.** Near-verbatim lexical duplication is redundant regardless of correctness (safe to discount); semantic similarity is confounded with correctness (discount weakly). This is standard surface-vs-semantic dedup (MinHash/n-gram Jaccard vs. embedding), applied as a *safety gate* in SC weighting. **We concede up front (§8.b) that if near-verbatim CoT echoes are vanishingly rare on real temperature-0.7 traces, this mechanism is inert on real data and only active in adversarial/synthetic settings** — we measure and report the empirical `dup_ij` distribution and compare to plain near-duplicate vote dedup.
3. **[Engineering safeguard] Never-worse-than-SC guard + stopping-variant pair.** `ρ=0` recovers SC exactly; the guard (with the *corrected* weight-sum ESS ratio) overturns the majority only on detected verbatim-echo clusters; we offer both a **SAFE** stopping rule (`min(P^raw,P^eff) ≥ τ`, never premature vs. ASC) and an **AGGRESSIVE** rule (`P^eff ≥ τ`, can save tokens when the *rival* is the redundant cluster). We concede the guard fires ≈never on real data outside adversarial regimes and therefore reduces to SC there; we quantify its firing rate rather than claiming a general "no-regret" theorem.
4. **[Implementation detail, not a contribution] VoI-per-token branch.** Textbook EVSI-per-cost (Raiffa & Schlaifer 1961). Demoted. Reported only if a pre-committed ablation shows it beats a plain patience threshold and a plain SPRT at matched budget; otherwise reported as a **negative result**, not silently dropped.

**Overall honest position.** The full pipeline is one integration step from RASC+ASC and VecCISC+ASC. **If it does not Pareto-dominate them (frontier-vs-frontier) under identical total-cost accounting on real data, there is no positive paper — only a robustness/negative result.** The value is: (a) getting the effective-count estimator correct where prior seeds got it wrong, (b) the safety decomposition + guard as measured engineering, (c) a fair, non-circular test of when redundancy-discounting helps.

---

## 3. Notation

| Symbol | Meaning |
|---|---|
| `q` | input question; frozen LLM defines the CoT sampling distribution |
| `r_i`, `a_i ∈ 𝒜` | i-th trace and its extracted discrete answer |
| `c_i ∈ [0,1]` | (optionally calibrated) confidence of trace i |
| `e_i ∈ ℝ^d` | unit-normalized reasoning embedding of `r_i` |
| `sem_ij ∈ [0,1]` | semantic similarity `clip(cos(e_i,e_j),0,1)` |
| `dup_ij ∈ [0,1]` | lexical near-duplication (n-gram Jaccard / normalized edit) |
| `S_ij ∈ [0,1]` | working kernel; `S_ii = 1`, symmetric |
| `s_i = Σ_j S_ij` | similarity mass (row sum incl. diagonal), `∈ [1,K]` |
| `w_i = 1/s_i` | effective (inverse-density) weight, `∈ [1/K, 1]` |
| `N_a^eff = Σ_{i:a_i=a} w_i` | **coherent** effective count for answer `a` |
| `n_eff = Σ_i w_i = tr(D⁻¹S)` | coherent total effective count, `∈ [1,K]`; `D=diag(s_i)` |
| `p_a^eff = N_a^eff / n_eff` | effective vote share |
| `n_a = Σ_i 𝟙[a_i=a]` | raw count |
| `v_i = w_i·g(c_i)` | **consensus-only** vote mass (confidence channel, kept out of posterior) |
| `θ = (θ_a)` | latent categorical answer probabilities |
| `α₀` | symmetric Dirichlet prior concentration |
| `τ, τ_floor, λ` | stability threshold / VoI-gate floor / VoI-per-token threshold |
| `ρ ∈ [0,1]` | discount strength (`ρ=0 ⇒ S=I ⇒ exact SC`) |
| `θ_dup,γ_dup,θ_sem,γ_sem,β_sem` | kernel hinge thresholds / exponents / semantic weight |
| `δ, η_dup` | guard overturn margin / duplication-ESS-ratio gate |
| `o_n` | per-step overhead (embedding+similarity+posterior), token-equivalents |
| `a*` | latent correct answer (oracle only) |

---

## 4. Full Math (corrected)

### 4.1 DDWC — the effective-weight estimator

**Robust tempered kernel (dup-vs-sem decomposition).** Hinge-power transform
```
φ_{θ,γ}(x) = ((x − θ)_+ / (1 − θ))^γ ,   (x)_+ = max(x,0),   for x,θ ∈ [0,1), γ>0.
```
Working kernel (off-diagonal; `S_ii = 1`):
```
S̃_ij = φ_{θ_dup,γ_dup}(dup_ij) + β_sem · φ_{θ_sem,γ_sem}(sem_ij)
S_ij  = ρ · clip_{[0,1]}(S̃_ij)                 (i≠j),      S_ii = 1.
```
- `ρ = 0 ⇒ S = I ⇒ s_i = 1 ⇒ w_i = 1 ⇒` **plain Self-Consistency, exactly.**
- High `θ_dup≈0.9`, large `γ_dup` collapse only near-verbatim copies; small `β_sem≈0.25` lets semantic similarity nudge but not dominate. **Safety intent:** verbatim echo discounted regardless of correctness; a tight-but-lexically-diverse correct cluster keeps near-full mass.
- Optional **WITHIN-CLASS scoping** (ablation): `s_i = 1 + Σ_{j≠i, a_j=a_i} S_ij` (discount only among agreeing traces).

**Effective weight and coherent effective count.**
```
w_i = 1 / s_i = 1 / Σ_j S_ij ,          w_i ∈ [1/K, 1]
N_a^eff = Σ_{i:a_i=a} w_i ,              n_eff = Σ_i w_i = tr(D⁻¹S) ∈ [1, K].
```

**Exact "one cluster ≈ one effective vote" (block model).** Traces partition into groups `g` of size `m_g`; within group all pairwise `S_ij = ρ_g`, `S_ii=1`; cross-group `0`. Then `s_i = 1 + (m_g−1)ρ_g` and
```
N_g^eff = m_g / (1 + (m_g−1)ρ_g),
N_g^eff → 1   as ρ_g → 1   (perfect echo ⇒ ONE effective vote),
N_g^eff → m_g as ρ_g → 0   (independent ⇒ full weight).
```
**Mandatory limit checks (were previously failing under Kish):**
- All-ones `S` (K identical copies): one group `m=K, ρ=1 ⇒ n_eff = 1`. ✅ (Kish gave `K` — the bug.)
- Two equal fully-correlated blocks: `n_eff = 2`. ✅
- `S = I`: `n_eff = K`, `N_a^eff = n_a`. ✅ (exact ASC reduction).

`Σ_i w_i = tr(D⁻¹S)` is the inverse-density (Parzen) effective count and a first-order surrogate for ridge-leverage `d_eff(λ_r)=tr(S(S+λ_rI)⁻¹)`; ridge-leverage / DPP-marginal weights are reported as **oracle ablations**. The Kish ratio `(Σw)²/Σw²` is retained only as a **dispersion diagnostic**, never in the posterior.

> **Note (removed misleading claim).** `n_eff ∈ [1,K]` is a trivial Cauchy–Schwarz-type bound on any nonneg weights and is **not** evidence of correct discounting; we do not present it as such. Correctness rests on the block-model limits above.

**Consensus (with optional confidence channel, kept separate from the posterior).**
```
v_i = w_i · g(c_i),   g(c) = c^{γ_c} if confidence gate passes, else 1.
â_DDWC = argmax_a W_a ,   W_a = Σ_{i:a_i=a} v_i.
```

**Never-worse-than-SC guard (corrected ESS ratio — weight SUM, not Kish).** Let `â_SC = argmax_a n_a`. On the duplication-only within-class submatrix `S^{(a)}_dup` (entries `ρ·φ_{θ_dup,γ_dup}(dup_ij)`, diagonal 1), define
```
w_i^dup = 1 / Σ_{j∈G_a} S^{(a)}_{dup,ij},
ESSratio_dup(a) = ( Σ_{i∈G_a} w_i^dup ) / n_a   ∈ (0, 1].
```
For `m` mutually-verbatim copies (`S_dup ≈ all-ones`): `w_i^dup = 1/m`, `Σ = 1`, `ESSratio = 1/m → 0` ⇒ **fires**. (The old Kish version gave `m/m = 1` and never fired — the R4 contradiction; now fixed.)
Output:
```
â = â_DDWC  if  â_DDWC ≠ â_SC  ∧  ESSratio_dup(â_SC) ≤ η_dup  ∧  W_{â_DDWC} ≥ (1+δ)·W_{â_SC}
    â_SC    otherwise.
```
Ties in `W_a` break toward larger `n_a`, then higher mean confidence. **`δ, η_dup` are frozen on dev and held constant across all regimes/datasets** (§8), so the guard cannot be per-regime tuned to satisfy every falsifier.

### 4.2 VoI-Stop — corrected posterior, leader stability, value of information

**Design-effect-corrected posterior (redundancy channel only).**
```
α_a = α₀ + N_a^eff = α₀ + Σ_{i:a_i=a} w_i ,   θ | data ~ Dir(α).
```
- **Reduces exactly to Adaptive-Consistency iff `S = I`** (then `w_i=1`, `N_a^eff = n_a`, `α_a = α₀ + n_a`). This reduction requires nothing about confidence because **the posterior does not use the confidence channel** (`v_i`); confidence enters only the consensus argmax (§4.1). This resolves the previous w-vs-v inconsistency.
- **Corrected calibration statement (previous "matches shares in expectation / unique" was false).** The Dirichlet posterior mean is `E[θ_a] = (α₀ + N_a^eff)/(α₀|𝒜| + n_eff)`, which is *shrunk toward uniform* by `α₀` and equals `p_a^eff` only as `α₀→0` or `n_eff→∞`. We therefore claim only the correct, weaker property: **the pseudo-count increment `α_a − α₀ = N_a^eff` is the effective count**, i.e. correlated samples inject `n_eff ≤ K` pseudo-evidence, so the posterior is correctly overdispersed. We drop all "unique parameterization" and "matches shares in expectation" language.
- **Optional confidence-tempered variant (heuristic ablation only):** `α_a^conf = α₀ + Σ_{i:a_i=a} w_i g(c_i)`. We flag explicitly that its total concentration `Σ w_i g(c_i)` is *not* the coherent effective count and this variant loses the clean ASC reduction; reported as ablation (b).

**Leader-stability probability (correctly labeled).** Let `ℓ = argmax_a α_a`.
- **`|𝒜| = 2` (exact):** `θ_ℓ ~ Beta(α_ℓ, α_R)` (`R` = the other cell), and
```
P_stable = Pr[θ_ℓ > 1/2] = I_{1/2}(α_R, α_ℓ)      # scipy.special.betainc(α_R, α_ℓ, 0.5)
```
This *is* `P(leader is the mode)` when `|𝒜|=2`.
- **`|𝒜| > 2` (primary definition = the genuine mode probability):**
```
P_stable = Pr[ argmax_a θ_a = ℓ ] ≈ (1/B) Σ_{b=1}^B 𝟙[ argmax_a θ_a^{(b)} = ℓ ],   θ^{(b)} ~ Dir(α),  B=512,
```
or the L-aggregation quadrature (top `L−1` cells + lumped "other", 1-D integral). **The pairwise Beta form for `|𝒜|>2` is an approximation to `Pr[θ_ℓ > θ_R]` (leader-vs-single-rival), NOT to `Pr(leader is mode)`, and is used only as a fast screen** (`θ_ℓ` can be the mode at `θ_ℓ<1/2`, so the pairwise-`>1/2` test under-reports). Default: MC/L-aggregation is the reported `P_stable`; pairwise Beta is an optional fast path flagged as approximate.

**Value of information (labeled as approximate, not exact Howard EVSI).** Decision: emit `â = ℓ`. Predictive `π_a = α_a / Σ_b α_b`. Expected next-trace weight `w̄ = n_eff / K = (Σ_i w_i)/K` (**mean actual weight — consistent with `n_eff`, was previously mis-scaled**). For each hypothetical outcome `a`, add `w̄` to class `a`, recompute `ℓ` and `P_stable^{+a}`; then
```
VoI = E_{a~π}[ P_stable^{+a} ] − P_stable .
```
**Honest caveat (was over-claimed).** With the leader *recomputed* after each hypothetical vote, `P_stable^{+a} = Pr(new argmax is stable)` and this quantity is nonnegative essentially by construction — it is **not** the exact Howard-1966 value of information / expected Bayes-risk reduction, and under MC estimation it carries a Jensen/estimation-noise gap. We therefore treat `VoI` as a **relative diminishing-returns signal** for the stopping decision only, apply `max(·,0)` to suppress MC noise, and do **not** claim decision-theoretic optimality. Per-token: `VoI / cost_next`, `cost_next = E[gen_tokens_next] + o_n`, `o_n = ρ_over·(2K+1)`.

**Stopping decision — two explicitly-different variants (report both frontiers).**
Maintain the calibrated raw posterior `α^raw_a = α₀ + n_a` (= ASC) and the effective posterior `α^eff_a = α₀ + N_a^eff`. Stop at `K ≥ K_min` iff:

- **SAFE variant** (safety-first; **cannot stop earlier than ASC**):
```
[ min(P^raw_stable, P^eff_stable) ≥ τ ]  ∨  [ (VoI/cost_next < λ) ∧ (P^eff_stable ≥ τ_floor) ]  ∨  [ K ≥ K_max ].
```
- **AGGRESSIVE variant** (can save tokens when the *rival* is the redundant echo):
```
[ P^eff_stable ≥ τ ]  ∨  [ (VoI/cost_next < λ) ∧ (P^eff_stable ≥ τ_floor) ]  ∨  [ K ≥ K_max ].
```

**Honest architectural statement (was a contradiction in the headline).** Because `min(P^raw,P^eff) ≤ P^raw`, the SAFE rule can **never** stop earlier than ASC — it trades tokens for accuracy/safety and can only match-or-exceed ASC's token spend. **Therefore the SAFE rule cannot deliver a token-side win over ASC; its value is accuracy at matched-or-higher tokens.** Any *token savings* over ASC must come from (a) the AGGRESSIVE rule's `P^eff`-driven early stops (valid only when the effective posterior concentrates faster than raw — i.e. the *rival* cluster is redundant), or (b) the VoI branch, which is load-bearing for the savings story and must independently beat ASC/MARS on tokens (ablation (g), §7). We report both variants; "Pareto dominance" is judged frontier-vs-frontier over the swept thresholds, not point-vs-point.

**The coupling claim (falsifiable).** On a correlated-wrong *rival* echo, raw ASC sees inflated `n_wrong` and a tight race, keeping `P^raw` low or stopping on the wrong leader; the effective posterior collapses the echo to `N_wrong^eff ≈ 1`, so `P^eff` concentrates on the correct leader — enabling both a correct answer and (AGGRESSIVE) an earlier correct stop. If `T(S) = T(I)` up to noise **and** frontiers coincide, the coupling adds nothing — refuted.

### 4.3 Where guarantees hold vs. fail (honest)

- **Holds exactly:** `S=I ⇒` exact ASC (posterior); `ρ=0 ⇒` exact SC (consensus); block-model one-cluster-one-vote limits; SAFE `min(·)` never stops earlier than ASC.
- **Approximate:** treating `N_a^eff` effective votes as `n_eff` independent categorical draws is a moment/ESS match (Rao–Scott spirit), not the exact non-multinomial likelihood of correlated votes; `P^eff_stable` and `VoI` are calibrated/validated empirically against real ground truth (§8), not proven exact.
- **Fails (no formal control):** fixed-`τ` optional stopping inflates Type-I error; we do **not** claim anytime validity. An empirical-Bernstein e-process guard mode is offered (§5) and both are reported. Outlier trace with near-zero similarity to all others gets `w_i ≈ 1` (bounded, since `w_i ≤ 1`) — **note the corrected bound `w_i ∈ [1/K,1]` removes the old "huge `1/s_i`" failure mode**; nonetheless winsorization is applied as defense (§5).

### 4.4 Complexity / cost

Generation `Σ_{k≤T} tokens` dominant; `T` embeddings (token-equivalents `κ_emb`); incremental similarity `O(K)`/step, `O(T²d)` total; `P_stable` via `L=3` quadrature `O(1)` or MC `O(B|𝒜|)`; VoI `O(|𝒜|)`/step; weight refresh `O(K)`/step (`O(K²)` total). **Cost x-axis = TOTAL token-equivalents (generation + embedding + similarity + posterior/VoI), at matched budget, never matched K, with identical `o_n` charged to every method that uses embeddings/similarity/confidence.**

---

## 5. Implementation-Ready Pseudocode

```python
# ============ RLEV-VoI (corrected): effective-count posterior + guard + stopping ============
# Frozen LLM. No extra LLM calls beyond K generations. c_i from same-generation logprobs;
# embeddings from a local encoder.  numpy + scipy.special.betainc.

import numpy as np
from scipy.special import betainc

# ---------------- config (frozen defaults; see §6) ----------------
CFG = dict(
  rho=0.7, theta_dup=0.9, gamma_dup=6.0, theta_sem=0.6, gamma_sem=3.0, beta_sem=0.25,
  kernel_scope="DECOMP",                       # {DECOMP, WITHIN_CLASS, GLOBAL}
  use_conf_gate=True, conf_gate_ece=0.10, gamma_c=1.0,
  delta=0.15, eta_dup=0.5,                      # guard (FROZEN across all regimes/datasets)
  alpha0=1.0, tau=0.95, tau_floor=0.80, lam=1e-3,
  Kmin=5, Kmax=40, B=512, rho_over=1.0,        # rho_over measured on hardware; 1x is primary
  stop_variant="SAFE",                          # {"SAFE","AGGRESSIVE"} — report BOTH frontiers
  w_clip=(1e-3, 1.0),                           # winsorize weights (w_i in [1/K,1] already)
  voi_branch=True, guard_anytime=False)

def hinge_pow(x, th, g):                         # off-diagonal only
    return (max(x - th, 0.0) / (1.0 - th))**g

def working_kernel_offdiag(i, j, A, Ssem, Sdup, cfg):
    if cfg["kernel_scope"] == "GLOBAL":
        base = hinge_pow(Ssem[i][j], cfg["theta_sem"], cfg["gamma_sem"])
    elif cfg["kernel_scope"] == "WITHIN_CLASS":
        base = (Ssem[i][j] if A[i] == A[j] else 0.0)
    else:  # DECOMP (default)
        base = (hinge_pow(Sdup[i][j], cfg["theta_dup"], cfg["gamma_dup"])
                + cfg["beta_sem"] * hinge_pow(Ssem[i][j], cfg["theta_sem"], cfg["gamma_sem"]))
    return cfg["rho"] * min(max(base, 0.0), 1.0)

def similarity_mass(i, n, A, Ssem, Sdup, cfg):
    s = 1.0                                       # S_ii = 1
    for j in range(n):
        if j == i: continue
        if cfg["kernel_scope"] == "WITHIN_CLASS" and A[j] != A[i]: continue
        s += working_kernel_offdiag(i, j, A, Ssem, Sdup, cfg)
    return s

def effective_weights(n, A, Ssem, Sdup, cfg):
    w = np.array([1.0 / similarity_mass(i, n, A, Ssem, Sdup, cfg) for i in range(n)])
    lo, hi = cfg["w_clip"]; w = np.clip(w, lo, hi)
    return w                                       # w_i in [1/K, 1]

def eff_counts(w, A):                              # coherent effective count per class
    N = {}
    for i, a in enumerate(A): N[a] = N.get(a, 0.0) + w[i]
    return N                                        # n_eff = sum(N.values()) = tr(D^-1 S)

def raw_counts(A):
    n = {}
    for a in A: n[a] = n.get(a, 0) + 1
    return n

def posterior_alpha(counts, alpha0):
    return {a: alpha0 + counts[a] for a in counts}

def consensus_W(w, A, C, cfg, use_conf):          # confidence channel (consensus only)
    W = {}
    for i, a in enumerate(A):
        g = (C[i]**cfg["gamma_c"] if use_conf else 1.0)
        W[a] = W.get(a, 0.0) + w[i] * g
    return W

# ---- P_stable: MC mode-probability (primary for |A|>2); exact Beta for |A|=2 ----
def P_stable(alpha, B, rng):
    keys = list(alpha); a = np.array([alpha[k] for k in keys])
    if len(keys) == 1: return 1.0
    if len(keys) == 2:
        # leader = larger; P[theta_leader > 1/2] = I_{1/2}(a_R, a_L)
        L = int(np.argmax(a)); R = 1 - L
        return float(betainc(a[R], a[L], 0.5))
    theta = rng.dirichlet(a, size=B)              # (B, |A|)
    L = int(np.argmax(a))
    return float(np.mean(np.argmax(theta, axis=1) == L))

def voi(alpha, w, n, K, B, rng, alpha0):
    keys = list(alpha)
    tot = sum(alpha.values()); pi = {k: alpha[k] / tot for k in keys}
    wbar = (float(np.sum(w)) / max(K, 1))          # = n_eff / K  (mean ACTUAL weight)
    base = P_stable(alpha, B, rng); acc = 0.0
    for a in keys + ["<NEW>"]:
        a2 = dict(alpha); a2[a] = a2.get(a, alpha0) + wbar
        pr = pi.get(a, alpha0 / tot)
        acc += pr * P_stable(a2, B, rng)
    return max(acc - base, 0.0)                     # relative diminishing-returns signal only

# ---- guard: ESS ratio from weight SUM (NOT Kish) ----
def essratio_dup(a_class, A, Sdup, cfg):
    idx = [i for i, a in enumerate(A) if a == a_class]
    m = len(idx)
    if m == 0: return 1.0
    wsum = 0.0
    for i in idx:
        s = 1.0
        for j in idx:
            if j == i: continue
            s += cfg["rho"] * hinge_pow(Sdup[i][j], cfg["theta_dup"], cfg["gamma_dup"])
        wsum += 1.0 / s
    return wsum / m                                 # = 1/m for m verbatim copies -> fires

def guarded_answer(W, ncnt, A, Sdup, cfg):
    a_sc = max(ncnt, key=ncnt.get); a_dd = max(W, key=W.get)
    if (a_dd != a_sc and essratio_dup(a_sc, A, Sdup, cfg) <= cfg["eta_dup"]
            and W[a_dd] >= (1.0 + cfg["delta"]) * W[a_sc]):
        return a_dd, True
    return a_sc, False

# ------------------------------- MAIN LOOP -------------------------------
def rlev_voi(q, LLM, EMB, NGRAM, cfg, offline_ECE=None, calib_set=None, seed=0):
    rng = np.random.default_rng(seed)
    use_conf = cfg["use_conf_gate"] and (offline_ECE is None or
               offline_ECE(calib_set) <= cfg["conf_gate_ece"])
    A, C, Esem, Edup = [], [], [], []
    Ssem = {}; Sdup = {}
    n = 0
    while n < cfg["Kmax"]:
        r = LLM.sample_cot(q); a = extract_answer(r)
        c = (extract_confidence(r) if use_conf else 1.0)
        es = EMB(r.reasoning); ed = NGRAM(r.reasoning)
        Ssem[n] = {}; Sdup[n] = {}
        for j in range(n):
            sij = sem_sim(es, Esem[j]); dij = dup_sim(ed, Edup[j])
            Ssem[n][j] = Ssem[j][n] = sij; Sdup[n][j] = Sdup[j][n] = dij
        Ssem[n][n] = Sdup[n][n] = 1.0
        A.append(a); C.append(c); Esem.append(es); Edup.append(ed); n += 1
        if n < cfg["Kmin"]: continue

        w   = effective_weights(n, A, Ssem, Sdup, cfg)
        Neff = eff_counts(w, A)                      # coherent effective counts
        ncnt = raw_counts(A)
        a_eff = posterior_alpha(Neff, cfg["alpha0"])
        a_raw = posterior_alpha(ncnt, cfg["alpha0"])
        Peff = P_stable(a_eff, cfg["B"], rng)
        Praw = P_stable(a_raw, cfg["B"], rng)

        cost_next = running_mean_gen_tokens() + cfg["rho_over"] * (2*n + 1)
        voi_pt = (voi(a_eff, w, n, n, cfg["B"], rng, cfg["alpha0"]) / max(cost_next, 1.0)
                  if cfg["voi_branch"] else 0.0)

        if cfg["stop_variant"] == "SAFE":
            stop_A = (min(Praw, Peff) >= cfg["tau"]) if not cfg["guard_anytime"] \
                     else eprocess_lower_bound_positive()
        else:  # AGGRESSIVE
            stop_A = (Peff >= cfg["tau"])
        stop_B = cfg["voi_branch"] and (voi_pt < cfg["lam"]) and (Peff >= cfg["tau_floor"])
        if stop_A or stop_B: break

    # final answer: guarded consensus over all collected traces
    w = effective_weights(n, A, Ssem, Sdup, cfg)
    W = consensus_W(w, A, C, cfg, use_conf); ncnt = raw_counts(A)
    ahat, guard_fired = guarded_answer(W, ncnt, A, Sdup, cfg)
    return ahat, dict(n=n, n_eff=float(np.sum(w)), Praw=Praw, Peff=Peff, guard_fired=guard_fired)

# -------------------- MANDATORY UNIT TESTS (must pass) --------------------
# T1  S = I                         -> w_i = 1, N_a^eff = n_a, alpha = alpha0 + n_a   (== ASC)
# T2  S = all-ones (K copies)       -> n_eff = 1                (NOT K; the old Kish bug)
# T3  two equal rho=1 blocks        -> n_eff = 2
# T4  block ρ_g -> 1                 -> N_g^eff -> 1 ; ρ_g -> 0 -> N_g^eff -> m_g
# T5  m verbatim copies, one class   -> essratio_dup = 1/m <= eta_dup -> guard FIRES (pure echo)
# T6  rho = 0                        -> plain Self-Consistency exactly
# -------------------- OPTIONAL ANYTIME-VALID GUARD --------------------
# Replace SAFE stop_A with an empirical-Bernstein confidence sequence on the effective
# leader-margin increments; stop when its lower bound > 0. Reports later stops; both on frontier.
```

---

## 6. Hyperparameters + Defaults

**Pre-registration rule (§8): one FROZEN default config below is chosen on the dev split and reported on ALL test cells as the headline. Per-cell-tuned results are reported separately and labeled as an upper bound, never as the claim.**

| Group | Param | Frozen default | Notes |
|---|---|---|---|
| Kernel | `ρ` | 0.7 | `ρ=0 ⇒` exact SC |
| | `θ_dup, γ_dup` | 0.9, 6 | collapse only near-verbatim echo |
| | `θ_sem, γ_sem, β_sem` | 0.6, 3, 0.25 | semantic nudge, cannot dominate |
| | `kernel_scope` | DECOMP | GLOBAL predicted to backfire (reported) |
| | calib. target mean off-diag | 0.3 | tune `β/θ` on dev to avoid collapse/hard-cluster |
| Confidence | `use_conf_gate`, `conf_gate_ece` | True, 0.10 | auto-disable `g(c)=1` if ECE > gate; **posterior never uses `c`** |
| | `γ_c` | 1 | consensus channel only |
| Guard | `δ`, `η_dup` | 0.15, 0.5 | **frozen across ALL regimes/datasets** |
| Posterior | `α₀` | 1.0 | pseudo-count increment `=N_a^eff`; mean is shrunk (not `p_a`) |
| Stopping | `τ, τ_floor, λ` | 0.95, 0.80, 1e-3 | tune `λ` per model on dev |
| | `stop_variant` | report BOTH | SAFE (safety) + AGGRESSIVE (savings) |
| | `K_min, K_max` | 5, 40 | |
| Estimators | `B` | 512 | MC mode-probability |
| Cost | `ρ_over` | 1× (primary) | also 0.5×/2× as robustness |
| Guarantee | `guard_anytime` | False | e-process variant reported alongside |
| Sampling | temperature | 0.7 (primary) | 1.0 as robustness |

**Effective-count estimator uses the WEIGHT SUM (`n_eff = Σw_i`), never the Kish ratio.**

---

## 7. Baselines to Compare

**Every adaptive baseline gets its OWN hyperparameter sweep on the identical dev split, traces its OWN accuracy-vs-total-cost frontier, and is charged identical `o_n` accounting for any embeddings/similarity/confidence it uses. Pareto-dominance is judged frontier-vs-frontier. Tuning budget (number of dev configs) pre-registered equal across methods.**

**Reference / mandatory:**
- **Self-Consistency fixed-K** (Wang 2022), K swept for the full frontier — matched on tokens.
- **Adaptive-Consistency / Dirichlet stopping** (Aggarwal 2023) = RLEV-VoI with `S=I`, no VoI, no guard; `τ` swept for its frontier. RLEV-VoI must beat this frontier-vs-frontier.

**Weighting axis:** CISC (2502.06233); VecCISC (2605.08070, soft-vs-hard head-to-head); Nine-Judges Kish-ESS aggregator (2605.29800); **plain near-duplicate vote dedup** (n-gram/MinHash surface dedup — the direct test of whether Claim 2's dup half adds anything); ridge-leverage / DPP-marginal oracle ablation (Alaoui & Mahoney 2015); Universal-SC (Chen 2023) / semantic-entropy clustering (Kuhn 2023; Farquhar 2024).

**Stopping axis:** ESC (Li 2024); Optimal Bayesian Stopping (2602.05395); a plain **SPRT** and at least one cost-aware/anytime stopper — MARS (2606.12935), CITE (2605.05873), or ConSol SPRT (2503.17587); DeepConf-online (2508.15260) if feasible. (Generation-altering stoppers handled per §8.b.)

**Combined competitor (hardest):** RASC (Wan 2024) — the closest single combined method.

**Accuracy ceiling:** Verifier / PRM best-of-N at matched budget (Cobbe 2021; Lightman 2023).

**Internal ablations (factorial):**
(a) reweight-only@fixedK vs. stop-only vs. full;
(b) redundancy-only posterior vs. confidence-tempered posterior `α₀+Σw_i g(c_i)` (tests the separated-channel choice); DDWC-no-c vs. CISC-only vs. DDWC·c for consensus;
(c) **stopping fed raw `n_a` vs. effective `N_a^eff` at the SAME consensus rule** — coupling isolation;
(d) **coherent effective-count `α₀+N_a^eff` vs. the old Kish-ratio `α₀+n_eff^{Kish}·p_a`** (demonstrates the corrected estimator; the Kish version must fail T2/T3);
(e) kernel: dup-only vs. sem-only vs. dup+sem; GLOBAL vs. WITHIN-CLASS vs. DECOMP;
(f) **guard on/off** with the FROZEN `δ,η_dup`;
(g) **stopping: SAFE `min(P^raw,P^eff)` vs. AGGRESSIVE `P^eff` vs. fixed-τ vs. e-process; and VoI branch vs. a plain patience threshold `P^eff∈[τ_floor,τ)` for fixed patience (VoI computation removed)** — attributes savings to VoI vs. the gate;
(h) **2×2 factorial** `{SC-consensus, guarded-DDWC-consensus} × {ASC-stop, VoI-eff-stop}` — isolates the marginal contribution of the stopping change from the consensus change;
(i) sensitivity sweeps over `ρ,θ_dup,γ,β_sem,α₀,τ,λ,ρ_over` (report sweeps, not a tuned point).

---

## 8. Experiment Design

### 8.a Simulated Oracle — **demoted to implementation sanity check (NOT the fair test)**

**Purpose (narrowed to avoid circularity).** The synthetic mixture generates data from exactly the block-cluster structure DDWC's math assumes, so it **cannot falsify whether DDWC helps on real traces** — a "win" there is an artifact of the data-generating process. It is used **only** to:
1. verify implementation-correctness / the mandatory unit tests T1–T6 (`S=I ⇒ ASC`; all-ones `⇒ n_eff=1`; equal-block `⇒ n_eff=2`; pure-echo guard firing; `ρ=0 ⇒ SC`);
2. confirm the code reproduces the block-model limits;
3. stress the pure-verbatim-echo attack (R4) as a **unit test of the guard**, not as evidence of real-world benefit.

**Empirical-kernel resampling (the honest synthetic).** For any synthetic claim beyond unit tests, the generative process is **fit to real cached traces** (the §8.b corpus): the `S_ij` distribution, the `dup_ij`–`sem_ij` joint, and the cluster-correctness coupling are estimated from real data and **bootstrap-resampled** — not hand-specified. Synthetic `sem_ij`/`dup_ij` marginals and joints are validated against the empirical kernels via a two-sample KS test (reported); the mixture centroids/spreads/`d` are fit so the synthetic sem-distribution matches the real one. We sweep `μ/σ/d` and **report the useful-regime boundary** (where `Σ_j S_ij` collapses to near-constant → DDWC degenerates to SC) and **where each real dataset falls relative to it.** If real traces fall in the collapse regime, headroom is nil and we report that.

**Regimes (for the guard/estimator unit tests and the boundary map only):**

| Regime | Setup | Role | Falsifier |
|---|---|---|---|
| **R1 INDEPENDENT** | large `σ`, no copies | code check: RLEV-VoI ≈ ASC, DDWC ≈ SC | reduction FALSE if they diverge beyond noise |
| **R2 CORRELATED-WRONG** | one distractor tight, correct diffuse | boundary map only (NOT headline evidence) | — (cannot establish real benefit) |
| **R3 EASY-CORRECT-CLUSTER** | correct tight & dominant | check GLOBAL hurts; DECOMP+guard ≈ SC | confound-fix FALSE if DECOMP+guard < SC |
| **R4 PURE VERBATIM ECHO** | `m` verbatim copies of a wrong template, **unmixed** | guard unit test: `essratio_dup=1/m` fires | recovery FALSE if guard silent (old Kish bug) |
| **R5 MISCALIBRATED CONF** | `κ_c ≤ 0` | ECE gate switches `g(c)=1`; posterior unaffected | robustness FALSE if degradation below SC |

**Checks:** unit-test pass/fail (T1–T6); guard firing on pure echo (R4); GLOBAL-vs-DECOMP flip behavior (R3); useful-regime boundary map with real datasets located on it.

### 8.b Real-API Design — **the headline evidence**

**Datasets:** tight-derivation/exact-match (GSM8K, MATH subset, MBPP) where naive DDWC is predicted to backfire and the guard must save it; diverse/distractor-heavy (CommonsenseQA, StrategyQA, ARC-Challenge, MMLU-subset) where discounting has headroom; one free-form/non-exact-match set for Universal-SC-style aggregation.

**Models:** ≥2 open-weights across scales (Llama-3.1-8B/70B or Qwen2.5-7B/72B) **plus** one frontier API model — explicitly to test whether savings survive on strong models ("SC losing its edge", 2511.00751).

**Sampling (paired, cached):** draw up to `K_max=40` CoT traces/item at temperature ∈ {0.7, 1.0} once, cache. **Prefix-replayable** methods (SC-K, ASC, ESC, CISC, RASC, VecCISC, OBS, RLEV-VoI + ablations) replay identical cached traces (paired, low-variance). **Generation-altering** methods (DeepConf-online, SPRT variants that abort mid-generation or adapt temperature) are declared as such and either (a) run **natively with fresh sampling at matched expected budget** (pairing lost, noted), or (b) the dominance claim is explicitly scoped to "aggregation-and-prefix-stopping methods over a fixed trace pool" and generation-altering methods excluded. Precompute `40×40` `S_sem`, `S_dup`. Parse `a_k`; `c_k` from verbalized AND logprob-derived confidence (both reported).

**Empirical dup/sem reporting (Claim-2 test, up front).** Report the full `dup_ij` distribution on real cached traces per dataset. **If near-verbatim clusters (`dup_ij` above `θ_dup`) are vanishingly rare, we concede the dup decomposition is inert on real data**, active only in adversarial/synthetic settings, and cannot carry the paper. Compare DDWC directly to plain near-duplicate vote dedup; if they match, Claim 2 is refuted. Report the **guard-firing rate** per dataset; if ≈0 outside R4, we state that RLEV-VoI is operationally SC on those benchmarks and reframe the guard as an engineering safeguard, not a result.

**Calibration test against a genuine competitor on real ground truth (fixes the rigged-by-construction issue).** The reliability diagram is **NOT** computed against the sim's own `n_eff`. Instead: estimate real `Pr(leader = a*)` from **held-out large-K sampling** (e.g. K=200 majority as the empirical mode-truth proxy). Then compare ECE of: (i) `α₀+N_a^eff` (ours), (ii) the naive strawman `α₀+W_a` with unbounded weights, **(iii) a genuinely competitive third parameterization** — temperature-scaled ASC (a scalar `T` fit on dev so ASC's `P_stable` is calibrated) — on the same real held-out ground truth. **We pre-commit to the falsifier: if `α₀+N_a^eff` is over/under-confident on real data (ECE not within CI of the temperature-scaled competitor), Novelty-1's calibration claim FAILS** — beating the unbounded strawman is not sufficient and not claimed as evidence.

**Matched-budget protocol (fully specified).** Each adaptive baseline's threshold(s) (`ASC τ`, `ESC window`, `MARS cost param`, `OBS threshold`, `RASC criteria`) are **independently swept on the identical dev split** to trace its own accuracy-vs-total-cost frontier. `o_n = ρ_over·(2K+1)` is charged **identically** to every method using embeddings/similarity/confidence (RASC, VecCISC, DeepConf included). Dominance is **frontier-vs-frontier**, never point-vs-point. Tuning budget (# dev configs) pre-registered **equal** across methods.

**Multiple-comparisons discipline (fixes garden-of-forking-paths).** (1) A **single frozen default config** (§6) chosen on dev is reported on **all** test cells as the headline. (2) **Holm correction** across the dataset×model grid for all McNemar tests. (3) The headline claim must hold for the **frozen default**, not per-cell-tuned configs; per-cell-tuned results are reported separately and labeled "upper bound." (4) `δ,η_dup` frozen across all regimes/datasets (guard cannot be per-regime tuned).

**Pre-registered PRIMARY endpoint (fixes the multiplied grid).** **Logprob-derived confidence, temperature 0.7, `ρ_over=1×`, embedding cost included, SAFE variant for the accuracy claim / AGGRESSIVE variant for the token-savings claim.** All of {verbalized confidence, temp 1.0, `ρ_over∈{0.5,2}×`, without-embedding-cost, raw/eff/min calibration} are **secondary/robustness**, labeled as such.

**Real-data achievable oracle (replaces the sim-oracle-optimal metric).** Retrospective oracle = smallest `K` whose running majority already equals the `K_max=40` answer. Report each method's gap to this achievable oracle on real data — the metric reviewers trust — instead of the sim's own-mode-probability oracle (dropped as headline).

**Metrics:** accuracy@matched-tokens; AUC(accuracy–token); per-item win/loss vs. SC (McNemar, Holm-corrected); wall-clock; stopping-time histograms; guard-firing rate + manual audit of overturned items; `dup_ij` distribution; `P_stable` ECE (ours vs. strawman vs. temperature-scaled ASC on real ground truth).

**Primary result that makes the paper (CONFIRM, on the frozen default, Holm-corrected):**
1. RLEV-VoI's frontier Pareto-dominates **both** RASC+ASC and VecCISC+ASC at matched total cost on distractor-heavy sets;
2. within-noise of SC on GSM8K/MATH/MBPP (guard-verified no backfire);
3. ablation (d) shows the coherent effective count is necessary (Kish version fails T2/T3 and is miscalibrated);
4. ablation (c)/(h) shows effective-count stopping changes the frontier **at the same consensus rule** (not just stopping *time*);
5. calibration: `α₀+N_a^eff` ECE within CI of temperature-scaled ASC on real held-out ground truth.

**No-paper conditions (FALSIFY → report as negative/robustness result):** at matched total cost the frontier does not clearly dominate RASC and ASC; OR guarded DDWC is significantly below SC in any dataset×model cell; OR DECOMP/WITHIN-CLASS gives no gain over CISC; OR sem-only matches dup+sem AND plain dedup matches DDWC (decomposition inert); OR real-data `dup_ij` shows near-verbatim echo is absent AND guard-firing ≈0 (mechanism inactive on real data); OR AGGRESSIVE/VoI offers no token savings over ASC/MARS at equal accuracy AND the VoI-vs-patience ablation (g) shows VoI adds nothing; OR `α₀+N_a^eff` is miscalibrated vs. the temperature-scaled competitor on real ground truth; OR gains fall inside diminishing-returns noise on the strong model. **We pre-commit to reporting the VoI-branch outcome (positive or negative) either way — it is never silently dropped.**

---

## 9. Limitations

1. **Similarity = correctness confound (central risk).** On math/code the correct answer is often one canonical near-duplicate derivation; global inverse-similarity discounts the correct cluster. Mitigated by dup-vs-sem decomposition + guard, but this must be *demonstrated* on real data, not assumed — and the demonstration hinges on near-verbatim echo actually occurring (see Lim. 8).
2. **Weight collapse / kernel brittleness.** With dense embedding cosine, `Σ_j S_ij` is near-constant ⇒ `w→uniform` ⇒ DDWC degenerates to SC (benign, no gain). The method lives in a narrow kernel regime; the useful-regime boundary is mapped and real datasets located on it (§8.a). If real traces fall in the collapse regime, headroom is nil — reported.
3. **Effective count is a moment/ESS match, not the exact correlated likelihood.** `α₀+N_a^eff` is Rao–Scott-style, not the exact non-multinomial likelihood of correlated votes; `P^eff_stable` and `VoI` are heuristics validated empirically against real ground truth. The corrected `w_i ∈ [1/K,1]` bound removes the old "huge `1/s_i` outlier" failure; winsorization is a further defense.
4. **SAFE stopping cannot save tokens over ASC — by design.** `min(P^raw,P^eff) ≤ P^raw` means SAFE never stops earlier than ASC; it trades tokens for accuracy/safety. Any token-side win must come from the AGGRESSIVE variant (valid only when the rival cluster is redundant) or the VoI branch, both of which are independently tested. This is stated honestly rather than being papered over by a "Pareto-dominates ASC" headline.
5. **No anytime-valid guarantee.** Fixed-`τ` optional stopping inflates Type-I error; an e-process mode is offered (later stops); both reported.
6. **VoI is not exact Howard EVSI.** With leader recomputation it is nonnegative by construction and measures a different quantity than Bayes-risk reduction; used only as a relative diminishing-returns signal, and demoted from a contribution to an implementation detail unless ablation (g) shows it beats a plain patience threshold and a plain SPRT.
7. **Miscalibrated self-confidence.** The posterior deliberately excludes the confidence channel (only consensus uses it) to keep the effective count coherent; confidence is ECE-gated and cautious.
8. **Mechanisms may be inert on real data.** If near-verbatim CoT echoes essentially never occur at temperature 0.7, the "safe" dup kernel discounts nothing, the guard fires ≈never, and the method collapses to lightly-down-weighted semantic similarity ≈ SC. We measure and report the `dup_ij` distribution and guard-firing rate up front; if inactive, we say so and reframe as an engineering safeguard.
9. **Overhead can erase savings at small K.** Embedding + `O(K²)` similarity + VoI lookahead can exceed tokens saved; only the honest total-cost x-axis (with the crossover K) makes the claim fair.
10. **Diminishing returns on frontier models.** Savings and headroom may shrink to noise on strong models; measured, not assumed.
11. **Novelty is narrow and the space is fast-moving.** The coupling is Rao–Scott + ASC + Kish-ESS; DDWC's weighting is fitness-sharing/inverse-density; the dup-sem split is surface-vs-semantic dedup; VoI/token is textbook EVSI-per-cost. The paper survives **only** as (a) a corrected, correctly-calibrated estimator where prior seeds got it wrong, (b) a measured safety decomposition + guard, and (c) a rigorous, non-circular matched-budget win over RASC+ASC / VecCISC+ASC. Absent (c), it should be published, if at all, as a rigorous negative/robustness result.

---

## 10. Red-Team Resolutions

**[critical/math] Kish ESS measures dispersion, not independent votes (S→all-ones returns K).** Fixed. The posterior now uses the **coherent effective count `n_eff = Σ_i w_i = tr(D⁻¹S)`** and per-category `N_a^eff = Σ_{i:a_i=a} w_i`, giving `n_eff=1` for K identical copies and `2` for equal fully-correlated blocks (mandatory unit tests T2/T3). Kish is retained only as a dispersion diagnostic, never in the posterior. We explicitly own the resulting form `α_a = α₀ + N_a^eff` (justified via Rao–Scott + the block-model one-cluster-one-vote limit), rather than the previously-rejected-then-reintroduced framing.

**[critical/experiment] Guard uses broken Kish, fails pure echo (R4).** Fixed. `ESSratio_dup(a) = (Σ_{i∈G_a} w_i^dup)/n_a` (weight sum, not Kish) `= 1/m` for `m` verbatim copies ⇒ fires. R4 redefined as a **pure, unmixed** verbatim-echo stress test (unit test T5).

**[major/math] "Matches shares in expectation / unique parameterization" false for α₀>0.** Fixed. We state only the correct property — the **pseudo-count increment `α_a−α₀=N_a^eff`** is the effective count; the posterior mean is explicitly noted as shrunk toward uniform by `α₀`. All "unique" and "matches shares" language dropped.

**[major/math] n_eff from w, p_a from v=w·g(c) inconsistent; ASC reduction only at g=1; w̄ mis-scaled.** Fixed. The posterior uses the **redundancy channel only** (`w`); confidence enters only the consensus argmax. ASC reduction now holds unconditionally (posterior never sees `c`). `w̄ = Σw_i/K = n_eff/K` (mean actual weight), consistent with the coherent `n_eff`.

**[major/math] Top-2 Beta mislabeled as P(leader is mode).** Fixed. Primary `P_stable` for `|𝒜|>2` is the MC/L-aggregation **mode probability**; the pairwise Beta is relabeled as an approximation to `Pr[θ_ℓ>θ_R]` and used only as a fast screen. Exact-VoI/Howard claim dropped; VoI labeled an approximate diminishing-returns signal with the `max(·,0)` clamp acknowledged.

**[minor/claim] [1,K] bound presented as correctness evidence.** Removed as a correctness argument; noted as a trivial property. Correctness now rests on the block-model limits and unit tests.

**[critical/novelty] Claim 1 = Rao–Scott, not new.** Weakened to "application of the Rao–Scott / effective-sample-size design-effect correction to CoT voting," citing Rao & Scott (1981/1984), Kish-ESS, and ASC as the composed components. The contribution is repositioned as a corrected estimator + measured robustness assembly, not a novel spine.

**[critical/claim] min-conjunction can't stop earlier than ASC — contradicts "Pareto-dominates ASC."** Fixed and stated honestly (§4.2, Lim. 4). SAFE trades tokens for accuracy and cannot beat ASC on tokens; token savings come only from the AGGRESSIVE `P^eff` variant or the VoI branch, both independently tested. "Pareto dominance" redefined as frontier-vs-frontier.

**[major/novelty] DDWC weighting is admitted fitness-sharing/inverse-density; dup-sem may be inert.** Conceded. We report the empirical `dup_ij` distribution up front, add a plain near-duplicate dedup baseline, and pre-commit to conceding inertness if near-verbatim echo is rare on real traces.

**[major/novelty] VoI is textbook, nonnegativity misapplied.** Demoted to an implementation detail; nonnegativity caveat added; ablation (g) requires VoI to beat a plain patience threshold and a plain SPRT, else reported as a negative result.

**[minor/novelty] Guard + min-conjunction are generic conservative combinations reducing to SC.** Conceded; guard-firing rate quantified on real data; reframed as an engineering safeguard, not a novel result.

**[critical/experiment] Simulation is circular.** Fixed. The synthetic oracle is **demoted to an implementation sanity check + unit tests**; it cannot establish real-world benefit. Empirical kernels (`S_ij` dist., dup-sem joint, cluster-correctness coupling) are **fit to and bootstrap-resampled from real cached traces**, KS-validated. Headline claims rest on the real-API experiment.

**[critical/experiment] Calibration demo rigged by construction.** Fixed. Reliability tested against a **third, genuinely competitive parameterization (temperature-scaled ASC)** on **real held-out large-K ground truth**, not the sim's own `n_eff`. Falsifier added: beating the unbounded strawman is insufficient.

**[critical/experiment] Matched-budget under-specified / exploitable.** Fixed. Every baseline gets its own dev sweep and full frontier; identical `o_n` charged to all embedding/similarity users; frontier-vs-frontier dominance; equal pre-registered tuning budget.

**[major/experiment] ~12 hyperparameters / forking paths.** Fixed. Single **frozen default** config reported on all cells; Holm correction across the grid; per-cell-tuned results labeled as upper bounds; `δ,η_dup` frozen across regimes.

**[major/experiment] "Never-worse-than-SC" trivially tunable.** Fixed. `δ,η_dup` frozen on dev and held constant across R1–R5 and all datasets; falsifier: no single frozen guard setting achieves both no-regret (R1/R3/R5) and gains (R2/R4).

**[major/experiment] Consensus-vs-stopping confound.** Fixed. Added the **2×2 factorial** `{SC, guarded-DDWC} × {ASC-stop, VoI-eff-stop}` (ablation h); coupling falsifier strengthened to require VoI-eff-stop to Pareto-dominate raw-count-stop **at the same consensus rule**.

**[major/experiment] Slip/embedding geometry are free parameters.** Fixed. Synthetic `sem_ij`/`dup_ij` marginals+joints fit to and KS-validated against real kernels; `μ/σ/d` swept; useful-regime boundary mapped with real datasets located on it.

**[major/claim] VoI branch non-falsifiable / could be tau_floor doing the work.** Fixed. Branch B gated by `P^eff` (not `P^raw`); ablation (g) replaces VoI with a plain patience threshold to attribute savings; outcome pre-committed to be reported either way.

**[major/experiment] Oracle-optimal from sim's own probabilities.** Fixed. Dropped as headline; replaced by the **real-data achievable oracle** (smallest K whose running majority equals the K_max answer).

**[minor/experiment] Paired cache can't fairly test generation-altering stoppers.** Fixed. Such methods are declared and either run natively at matched expected budget (pairing loss noted) or excluded, with the claim scoped to aggregation-and-prefix-stopping over a fixed pool.

**[minor/experiment] Confidence/temperature grid, no primary endpoint.** Fixed. Pre-registered primary endpoint: logprob confidence, temp 0.7, `ρ_over=1×`, embedding cost included; all others secondary/robustness.