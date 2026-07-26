# RLEV-VoI: Robust Leverage-Effective-Vote Consensus with Value-of-Information Stopping

## 1. Name & Abstract

**RLEV-VoI** is an inference-time reasoning pipeline for a **frozen** LLM that (i) aggregates chain-of-thought (CoT) votes with a redundancy-discounted "effective vote" weight derived from an inverse-similarity-mass (Kish / statistical-leverage) estimator over reasoning traces, and (ii) sequentially decides when to stop sampling using a Dirichlet–multinomial posterior over the *effective* vote tallies plus a value-of-information (VoI) per-token cutoff. The single technical spine shared by all three source designs — and the piece we validate hardest — is a **design-effect-corrected posterior** that decouples *which* answer the evidence favors (the weighted vote share `p_a`) from *how much* independent evidence exists (the Kish effective sample size `n_eff ≤ K`), i.e. `α_a = α₀ + n_eff·p_a`. This reduces **exactly** to Adaptive-Consistency when traces are independent (`S=I`), repairing the broken-conjugacy hole in the naive `α_a = α₀ + weighted_count_a`. Around this spine we wrap three robustness mechanisms that make the method *never meaningfully worse than Self-Consistency* in practice: a **duplication-vs-semantic kernel decomposition** (discount only provably-redundant near-verbatim echo, treat confounded semantic similarity cautiously), an **SC-fallback guard** that lets the redundancy discount overturn the plain majority *only* on detected verbatim-echo clusters, and a **one-sided-safe stopping conjunction** (`min(P_stable^raw, P_stable^eff) ≥ τ`) so miscalibrated fractional counts can only make stopping *more* conservative, never premature. We are explicit that neither component is a new *idea*; the contribution is a calibrated, robust, honestly-benchmarked *assembly* plus the safety decomposition.

---

## 2. Honest Novelty Positioning

**What is prior art (cited up front; we do NOT claim these):**

- **The redundancy-discount concept** (correlated CoT chains double-count correlated errors): fitness sharing (Goldberg & Richardson 1987); Kish ESS for correlated LLM votes ("Nine Judges, Two Effective Votes", 2605.29800); semantic-entropy clustering (Kuhn 2023; Farquhar et al. Nature 2024); applied to SC voting by **VecCISC** (2605.08070), **RASC** (2408.17017), and semantic self-consistency.
- **The closed form `w_i = 1/Σ_j S_ij`**: this is Goldberg–Richardson fitness sharing (`f_i / Σ_j sh_ij`), inverse-density / `D⁻¹` graph-degree weighting, and a cheap `O(K²)` surrogate for ridge-leverage `τ_i = [S(S+λI)⁻¹]_ii`, `Σ_i τ_i = d_eff` (Alaoui & Mahoney 2015). We claim it only as an *instantiation*.
- **The confidence fold-in `w_i ← w_i·c_i`**: this is **CISC** (2502.06233) / DiVeRSe / weighted-SC.
- **Dirichlet-multinomial "stop when P(leader is the true mode) ≥ τ"**: this **IS** Adaptive-Consistency's headline criterion (Aggarwal et al. 2023, 2305.11860) and Optimal Bayesian Stopping (2602.05395). *Correction:* the seed's premise that ASC uses "raw counts, no posterior" is **factually wrong** and is corrected here — ASC's best criterion is exactly this Dirichlet posterior.
- **VoI / optimal-stopping-per-cost as a concept**: classical (Wald SPRT; Howard 1966; DeGroot; Weitzman 1979 "Pandora's box"), already ported to test-time LLMs (2510.01394; 2410.02725; MARS 2606.12935; Uncertainty-Aware Budget Allocation 2605.26849).

**What is defensibly new (in decreasing strength):**

1. **The design-effect-corrected coupling** `α_a = α₀ + n_eff·p_a`, decoupling ESS-concentration from vote-share. This makes `P_stable` a bounded, ASC-consistent posterior under fractional redundancy-discounted counts, where the naive `α₀ + weighted_count_a` is uncalibrated. Not found published verbatim. *(All three source designs independently converged on this exact parameterization — the strongest signal that it is the right fix.)*
2. **The duplication-vs-semantic kernel decomposition** (Design-3 core): near-verbatim lexical duplication is redundant *regardless of correctness* (safe to discount); semantic similarity is *confounded* with correctness (discount only weakly). No prior SC-weighting method (RASC/VecCISC discount semantic similarity directly) makes this safety distinction. Numerically, naive inverse-similarity flips a 6-correct-vs-5-wrong item to WRONG; the decomposition + guard prevents this.
3. **The never-worse-than-SC guard + one-sided-safe stopping conjunction**: `ρ=0` recovers plain SC exactly; the guard overturns the majority only on verbatim-echo evidence; `min(P^raw, P^eff)` inherits ASC calibration as a *floor*. Turns the "broken-conjugacy miscalibration" objection into a one-sided-safe bound.
4. **(Thin, crowded) VoI-per-token branch over the corrected posterior**. Claimed only as "a clean decision-theoretic instantiation coupled to effective-vote counts," and only if ablations show it changes *when* to stop vs. the τ-only branch and vs. MARS at matched budget.

**Honest overall position:** the full pipeline (leverage effective votes → ESS-corrected Dirichlet → VoI/token stop, with a dup-vs-sem guard) appears unpublished as an exact assembly, but is one integration step from RASC+ASC and VecCISC+ASC. **If it does not Pareto-dominate RASC+ASC and VecCISC+ASC under identical token accounting, there is no paper.** The contribution is (a) the calibration fix, (b) the safety decomposition, and (c) a rigorous fair test of *when* redundancy-discounting helps vs. backfires.

---

## 3. Notation

| Symbol | Meaning |
|---|---|
| `q` | input question; frozen LLM defines sampling distribution over CoT traces |
| `r_i`, `a_i ∈ 𝒜` | i-th sampled trace and its extracted discrete answer |
| `c_i ∈ [0,1]` | (optionally calibrated) confidence of trace i |
| `e_i ∈ ℝ^d` | reasoning embedding of `r_i` (unit-normalized) |
| `sem_ij ∈ [0,1]` | semantic similarity, `cos(e_i, e_j)` clipped to `[0,1]` |
| `dup_ij ∈ [0,1]` | lexical near-duplication (n-gram Jaccard / normalized edit) |
| `S_ij ∈ [0,1]` | working similarity kernel used for weighting; `S_ii = 1`, symmetric |
| `s_i = Σ_j S_ij` | similarity mass / weighted graph degree of trace i (Parzen-KDE density, up to scale) |
| `w_i` | DDWC effective (leverage) weight of trace i |
| `v_i = w_i·g(c_i)` | vote mass of trace i |
| `n_a = Σ_i 𝟙[a_i=a]` | raw count for answer a |
| `W_a = Σ_{i:a_i=a} v_i` | effective (weighted) count for answer a; `p_a = W_a/Σ_b W_b` |
| `n_eff` | Kish effective sample size, `∈ [1,K]` |
| `K, K_min, K_max` | current / warm-up / max number of traces |
| `θ = (θ_a)` | latent categorical answer probabilities (the vote distribution) |
| `α₀` | Dirichlet prior concentration per category |
| `τ, τ_floor, λ` | stability threshold / VoI-gate floor / VoI-per-token threshold |
| `ρ ∈ [0,1]` | discount strength (`ρ=0` ⇒ exact SC) |
| `θ_dup, γ_dup, θ_sem, γ_sem, β_sem` | kernel hinge thresholds, sharpening exponents, semantic weight |
| `δ, η_dup` | guard margin / duplication-ESS gate |
| `o_n` | per-step overhead (embedding + similarity + posterior), in token-equivalents |
| `a*` | latent correct answer (oracle only) |

---

## 4. Full Math

### 4.1 DDWC — the effective-weight estimator

**Robust tempered kernel (dup-vs-sem decomposition).** Define the hinge-power transform
```
φ_{θ,γ}(x) = ( (x−θ)_+ / (1−θ) )^γ ,   (x)_+ = max(x,0),
```
and the working kernel (off-diagonal; `S_ii = 1`):
```
 S̃_ij = φ_{θ_dup,γ_dup}(dup_ij)  +  β_sem · φ_{θ_sem,γ_sem}(sem_ij)
 S    = ρ · clip_{[0,1]}(S̃)  +  (1−ρ) · I .
```
- `ρ = 0` ⇒ `S = I` ⇒ `w_i ≡ 1` ⇒ **plain Self-Consistency, exactly.**
- High `θ_dup` (≈0.9) with large `γ_dup` collapses only near-verbatim copies; small `β_sem` (≈0.25) lets semantic similarity *nudge* but not dominate. This is the safety fix: verbatim echo is discounted regardless of correctness, while a *tight-but-lexically-diverse correct cluster* (`sem≈0.93, dup<θ_dup`) keeps near-full mass.
- Optional **WITHIN-CLASS scoping** (Design-2 alternative): `s_i = Σ_{j: a_j=a_i} S_ij`, so redundancy is discounted only among traces that already agree. Selectable hyperparameter; reported as an ablation.

**Effective weight (statistical leverage / inverse-similarity mass):**
```
 w_i = 1 / s_i = 1 / Σ_j S_ij ,   v_i = w_i · g(c_i),   g(c) = c^γ_c (or 1 if confidence gated off).
```

**Consensus:** `â_DDWC = argmax_a W_a`, `W_a = Σ_{i:a_i=a} v_i`.

**Exact "one cluster ≈ one effective vote".** In the block-similarity model (traces partition into groups `g`; within group of size `m_g` all pairwise `S_ij = ρ_g`, `S_ii=1`; cross-group `S_ij=0`):
```
 s_i = 1 + (m_g − 1)ρ_g ,   W_g = m_g / (1 + (m_g−1)ρ_g),
 W_g → 1   as ρ_g → 1   (perfect echo ⇒ one effective vote)
 W_g → m_g as ρ_g → 0   (independent ⇒ full weight).
```
In general `Σ_i w_i = Σ_i 1/s_i = tr(D⁻¹S)` (`D = diag(s_i)`) is the inverse-density (Parzen) effective count — a first-order surrogate for the ridge-leverage effective dimension `d_eff(λ_r) = tr(S(S+λ_rI)⁻¹)`. Equality does not hold in general; DDWC is the cheap `O(K²)` surrogate, and ridge-leverage / DPP-marginal weights are reported as **oracle ablations**.

**Kish effective sample size (used for calibration in §4.2):**
```
 n_eff = (Σ_i w_i)² / Σ_i w_i²  ∈ [1, K].
```
Uniform weights ⇒ `n_eff = K`; one dominating weight ⇒ `n_eff → 1`. Design effect `DEFF = K/n_eff ≥ 1`.

**Never-worse-than-SC guard.** Let `â_SC = argmax_a n_a`. Compute a *duplication-only* per-class ESS ratio on the dup-kernel submatrix `S^{(a)}_dup`:
```
 ESSratio_dup(a) = n_eff^{dup}(a) / n_a ∈ (0,1],
 n_eff^{dup}(a) = (Σ_{i∈G_a} w_i^{dup})² / Σ_{i∈G_a} (w_i^{dup})² ,  w_i^{dup} = 1/Σ_{j∈G_a} S^{(a)}_{dup,ij}.
```
Output:
```
 â = â_DDWC   if  â_DDWC ≠ â_SC  ∧  ESSratio_dup(â_SC) ≤ η_dup  ∧  W_{â_DDWC} ≥ (1+δ)·W_{â_SC}
     â_SC     otherwise.
```
DDWC may overturn the majority **only** when the majority's support is a verbatim-duplicate echo (low `ESSratio_dup`) *and* the discounted challenger wins by margin `δ`. Ties in `W_a` break toward larger `n_a`, then higher mean confidence. This yields the empirical no-regret property.

**Why the seed's `α_a = α₀ + W_a` is wrong.** `W_a` are fractional, correlated pseudo-counts; an outlier trace with tiny `s_i` gets a huge `w_i`. Plugging `W_a` as a Dirichlet concentration conflates **evidence direction** with **evidence quantity**, destroying the meaning of `τ`. The fix is §4.2.

### 4.2 VoI-Stop — corrected posterior, leader stability, value of information

**Design-effect-corrected Dirichlet posterior.** Model `a_k | θ ~ Categorical(θ)`, `θ ~ Dir(α₀·𝟙)`. Set the posterior so its **mean** matches the weighted shares `p_a` and its **total concentration** equals the effective (not raw) count:
```
 α_a = α₀ + n_eff · p_a ,   with   Σ_a (α_a − α₀) = n_eff ≤ K,
 θ | data ~ Dir(α).
```
This is the unique parameterization that (i) matches observed weighted shares in expectation, (ii) injects only `n_eff` worth of pseudo-evidence, and (iii) reduces **exactly** to Adaptive-Consistency when `S=I` (then `w_i≡1`, `n_eff=K`, `n_eff·p_a = n_a`). Equivalent forms in the source designs — `tilde_n_a = n_eff·(m_a/M)` and `α_a = α₀ + κN_a, κ = n_eff/ΣN` — are algebraically identical. Because `Σ_a(α_a−α₀)=n_eff < K` whenever traces are correlated, the posterior is *correctly overdispersed*: correlated samples carry less information ⇒ less concentration.

**Exact leader-stability probability.** Let `ℓ = argmax_a α_a`, `R = strongest rival`.
- **Binary / top-2 (exact for `|𝒜|=2`, the Optimal-Bayesian-Stopping top-2 approximation otherwise):** `θ_ℓ ~ Beta(α_ℓ, α_R)`, and
```
 P_stable = Pr[θ_ℓ > 1/2] = 1 − I_{1/2}(α_ℓ, α_R) = I_{1/2}(α_R, α_ℓ),
```
with `I_x(a,b)` the regularized incomplete Beta function (closed form, exact).
- **General `|𝒜| > 3`:** either the L-aggregated approximation (keep top `L−1` answers, lump the rest as "other" ⇒ ≤3-cell Dirichlet, `L=3` asymptotically optimal, 1-D quadrature) or Monte Carlo:
```
 P_stable ≈ (1/B) Σ_{b=1}^{B} 𝟙[ argmax_a θ^{(b)} = ℓ ],   θ^{(b)} ~ Dir(α),  B = 512.
```

**Value of information (proper, nonnegative).** Decision: emit `â = ℓ`. Mode-decision risk `R = 1 − P_stable`. The next answer is predicted by the posterior predictive `π_a = α_a / Σ_b α_b`. For each outcome `a`, add one *effective* vote (expected new-trace weight `w̄ = n_eff / K`) to class `a`, recompute `α`, `ℓ`, `P_stable^{+a}`. Then
```
 VoI = R − E_{a~π}[R^{+a}] = E_{a~π}[ P_stable^{+a} ] − P_stable  ≥ 0   (in expectation; Howard 1966).
```
**Per-token VoI:** `VoI / cost_{next}`, where
```
 cost_{next} = E[gen_tokens_next]  +  o_n ,   o_n = ρ_over·(2K+1)  (O(K) new similarities + 1 embedding, token-equivalents).
```

**Robust, one-sided-safe stopping decision.** Maintain **two** posteriors: the calibrated raw-count `α^raw_a = α₀ + n_a` (= Adaptive-Consistency) and the effective `α^eff_a = α₀ + n_eff·p_a`. Compute `P^raw_stable`, `P^eff_stable` from each. Stop at step `K ≥ K_min` iff
```
 [ min(P^raw_stable, P^eff_stable) ≥ τ ]                          (A) calibrated stability
   ∨  [ (VoI / cost_next < λ)  ∧  (P^raw_stable ≥ τ_floor) ]       (B) gated diminishing-return early stop
   ∨  [ K ≥ K_max ].
```
Emit `â` per the guarded consensus (§4.1) at stop.

**Why this is safe.** The `min(·)` in (A) means effective counts can only *delay* stopping vs. raw ASC — calibration is inherited from ASC as a floor, so fractional-count miscalibration can never cause a *premature* stop. Branch (B) is gated by `τ_floor < τ` so VoI can shave tokens only when risk is already low.

**The coupling claim (falsifiable).** On correlated-wrong echo, raw ASC (`S=I`) sees inflated `n_wrong`, reaches `P^raw_stable ≥ τ` on the WRONG leader early; under DDWC that echo collapses to `n_eff·p_wrong ≈ 1` effective vote, keeping `P^eff_stable` low so the conjunction keeps sampling until truth overtakes. If `T(S) = T(I)` up to noise, the coupling adds nothing — refuted.

### 4.3 Where guarantees hold vs. fail (stated honestly)

- **Holds:** `S=I` ⇒ exact reduction to Adaptive-Consistency; `ρ=0` ⇒ exact plain SC; ESS scaling keeps `α_a ≥ α₀`, so `P^eff_stable` is a genuine posterior probability (unlike `α₀ + W_a`); `min(P^raw,P^eff)` never stops earlier than calibrated ASC.
- **Approximate:** `n_eff·p_a` treats effective votes as `n_eff` independent categorical draws — a moment/ESS match, not the exact (non-multinomial) likelihood of correlated votes. `P^eff_stable` is calibrated to the ESS and validated empirically (reliability diagram).
- **Fails (no formal error control):** fixed-`τ` optional stopping inflates Type-I error. We do **not** claim anytime validity. An optional empirical-Bernstein confidence-sequence guard mode (§5) is offered and both are reported.

### 4.4 Complexity / cost

Generation `Σ_{k≤T} tokens` (dominant); `T` embedding calls (charged as token-equivalents `κ_emb`); incremental similarity `O(K)` per step, `O(T²d)` total; `P_stable` via `L=3` quadrature `O(1)` or MC `O(B|𝒜|)`; VoI `O(|𝒜|)` per step. Because `w_i = 1/s_i` for earlier `i` changes when a new similar trace arrives, an exact per-step refresh of affected class sums is `O(K)`/step, `O(K²)` total. **Honest Pareto = accuracy vs. TOTAL (generation + embedding + similarity) token-equivalents, at matched budget, never matched `K`.**

---

## 5. Implementation-Ready Pseudocode

```
# =============== RLEV-VoI: Robust Leverage-Effective-Vote Consensus + VoI Stopping ===============
# Frozen LLM (no training). No extra LLM calls beyond the K generations:
#   confidence c_i from the SAME generation's logprobs/verbalization; embeddings from a local encoder.

INPUTS:
  q                                  # query
  # --- kernel / weighting ---
  rho=0.7, theta_dup=0.9, gamma_dup=6, theta_sem=0.6, gamma_sem=3, beta_sem=0.25
  kernel_scope in {DECOMP, WITHIN_CLASS, GLOBAL} = DECOMP
  use_conf_gate=True, conf_gate_ece=0.10, gamma_c=1       # g(c)=c^gamma_c if gate passes else 1
  # --- guard ---
  delta=0.15, eta_dup=0.5
  # --- posterior / stopping ---
  alpha0=1.0, tau=0.95, tau_floor=0.80, lambda=1e-3
  Kmin=5, Kmax=40, L=3, B=512, rho_over=measured
  guard_anytime=False                # optional e-process replacement for branch (A)

STATE: R=[], A=[], C=[], Esem=[], Edup=[]; Ssem={}, Sdup={}

# ---- one-time confidence gate (robustness): disable c_i if the model is miscalibrated ----
use_conf = use_conf_gate and (offline_ECE(model, calib_set) <= conf_gate_ece)

def hinge_pow(x, th, g):  return ((max(x-th,0.0))/(1-th))**g          # off-diagonal only
def working_kernel(i,j):
    if kernel_scope==GLOBAL:      base = hinge_pow(Ssem[i][j],theta_sem,gamma_sem)   # sem only
    elif kernel_scope==WITHIN_CLASS: base = (Ssem[i][j] if A[i]==A[j] else 0.0)
    else: # DECOMP (default, safest)
        base = hinge_pow(Sdup[i][j],theta_dup,gamma_dup) + beta_sem*hinge_pow(Ssem[i][j],theta_sem,gamma_sem)
    return rho*clip01(base)                                            # (1-rho)*I added via s_i below

def similarity_mass(i, n):
    s = 1.0                                                            # S_ii = 1 (the (1-rho)*I + rho*1)
    for j in range(n):
        if j!=i:
            if kernel_scope==WITHIN_CLASS and A[j]!=A[i]: continue
            s += working_kernel(i,j)
    return s

def effective_weights(n):
    w=[1.0/similarity_mass(i,n) for i in range(n)]
    g=[ (C[i]**gamma_c if use_conf else 1.0) for i in range(n)]
    v=[w[i]*g[i] for i in range(n)]
    return w, v

def kish_ess(w):  sw=sum(w); return (sw*sw)/sum(x*x for x in w)        # in [1,K]

def weighted_counts(v):
    W={}; 
    for i,a in enumerate(A): W[a]=W.get(a,0.0)+v[i]
    return W

def posterior_alpha_eff(W, n_eff):
    M=sum(W.values());  return {a: alpha0 + n_eff*(W[a]/M) for a in W}
def posterior_alpha_raw():
    cnt={}; 
    for a in A: cnt[a]=cnt.get(a,0)+1
    return {a: alpha0 + cnt[a] for a in cnt}, cnt

def P_stable(alpha):
    L_=argmax_key(alpha); R_=argmax_key({a:alpha[a] for a in alpha if a!=L_}) if len(alpha)>1 else None
    if R_ is None: return 1.0
    if len(alpha)<=3 or True_top2_ok:
        return reg_incomplete_beta(0.5, alpha[R_], alpha[L_])          # = P(Beta(aL,aR) > 1/2)
    return mc_mode_prob(alpha, B)                                      # (1/B) sum 1[argmax==L_]

def voi(alpha, n_eff, K):
    base=P_stable(alpha); tot=sum(alpha.values()); pi={a:alpha[a]/tot for a in alpha}; wbar=n_eff/max(K,1)
    acc=0.0
    for a in list(alpha)+["<NEW>"]:
        a2=dict(alpha); a2[a]=a2.get(a,alpha0)+wbar
        acc += pi.get(a, alpha0/tot) * P_stable(a2)
    return max(acc-base, 0.0)

def guarded_answer(W, n, cnt):
    a_sc  = argmax_key(cnt); a_dd = argmax_key(W)
    if a_dd!=a_sc and essratio_dup(a_sc) <= eta_dup and W[a_dd] >= (1+delta)*W[a_sc]:
        return a_dd, True
    return a_sc, False

# --------------------------------- MAIN LOOP ---------------------------------
n=0
while n < Kmax:
    r=LLM.sample_cot(q); a=extract_answer(r); c=(extract_confidence(r) if use_conf else 1.0)
    esem=EMB(r.reasoning); edup=NGRAM(r.reasoning)
    for j in range(n):
        Ssem[n][j]=Ssem[j][n]=sem_sim(esem,Esem[j]);  Sdup[n][j]=Sdup[j][n]=dup_sim(edup,Edup[j])
    Ssem[n][n]=Sdup[n][n]=1.0
    R.append(r);A.append(a);C.append(c);Esem.append(esem);Edup.append(edup); n+=1
    if n < Kmin: continue

    w,v = effective_weights(n);  n_eff=kish_ess(w);  W=weighted_counts(v)
    a_raw,cnt = posterior_alpha_raw();  a_eff = posterior_alpha_eff(W, n_eff)
    Praw=P_stable(a_raw);  Peff=P_stable(a_eff)
    ahat, guard_fired = guarded_answer(W, n, cnt)

    tok_next = running_mean_gen_tokens() + rho_over*(2*n+1)
    voi_pt   = voi(a_eff, n_eff, n) / max(tok_next,1)

    stop_A = (min(Praw,Peff) >= tau) if not guard_anytime else eprocess_lower_bound_positive()
    stop_B = (voi_pt < lambda) and (Praw >= tau_floor)
    if stop_A or stop_B: break

# final answer from guarded consensus over all collected traces
w,v=effective_weights(n); W=weighted_counts(v); _,cnt=posterior_alpha_raw()
ahat,_ = guarded_answer(W, n, cnt)
return ahat, {n, n_eff, Praw, Peff, guard_fired}

# ------------------------- KERNEL CALIBRATION (dev set) -------------------------
# Tune beta/theta so mean off-diagonal working-kernel entry ~ rho* (default 0.3):
#   too high  -> weights collapse toward uniform -> recover plain SC (no gain)
#   too sharp -> hard clustering -> recover VecCISC.
# ------------------------- OPTIONAL ANYTIME-VALID GUARD -------------------------
# Replace branch (A) with an empirical-Bernstein confidence sequence on
# g_K = theta_leader - max_{a!=leader} theta_a (effective increments); stop when its lower bound > 0.
# Optional-stopping error control at the cost of later stops. Report BOTH variants on the frontier.

# ------------------------------ DEGENERACY ASSERTS ------------------------------
#   rho=0            -> S=I -> w_i=1 -> plain Self-Consistency EXACTLY
#   S=I, no VoI, no guard, tau branch only -> Adaptive-Consistency EXACTLY
#   gamma_c=0 / gate off -> redundancy-only weighting (no confidence)
```

---

## 6. Hyperparameters + Defaults

| Group | Param | Default | Notes |
|---|---|---|---|
| Kernel | `ρ` | 0.7 | discount strength; `ρ=0` ⇒ exact SC |
| | `θ_dup, γ_dup` | 0.9, 6 | collapse only near-verbatim echo |
| | `θ_sem, γ_sem, β_sem` | 0.6, 3, 0.25 | semantic nudge, cannot dominate |
| | `kernel_scope` | DECOMP | `{DECOMP, WITHIN_CLASS, GLOBAL}` (GLOBAL = predicted to backfire, reported) |
| | calibration target mean off-diag | 0.3 | tune `β/θ` on dev to avoid collapse/hard-cluster |
| Confidence | `use_conf_gate`, `conf_gate_ece` | True, 0.10 | auto-disable `g(c)=1` if ECE > gate |
| | `γ_c` | 1 | confidence exponent when gate passes |
| Guard | `δ`, `η_dup` | 0.15, 0.5 | overturn margin / duplication-ESS gate |
| Posterior | `α₀` | 1.0 | symmetric Dirichlet prior |
| Stopping | `τ`, `τ_floor`, `λ` | 0.95, 0.80, 1e-3 | tune `λ` per model/token-cost on dev split |
| | `K_min`, `K_max` | 5, 40 | warm-up / hard cap |
| Estimators | `L`, `B` | 3, 512 | top-L quadrature / MC draws |
| Cost | `ρ_over` | measured | report frontier at 0.5×/1×/2× measured |
| Guarantee | `guard_anytime` | False | e-process variant reported alongside |
| Sampling | temperature | 0.7 | (also sweep 1.0 in real-API) |

---

## 7. Baselines to Compare

**Reference / mandatory:**
- **Self-Consistency fixed-K** (Wang et al. 2022), K swept to trace the full accuracy-vs-token Pareto — matched on **tokens**, not K.
- **Adaptive-Consistency / Dirichlet stopping** (Aggarwal et al. 2023) — the mandatory stopping baseline; **equals RLEV-VoI with `S=I`, no VoI, no guard**. RLEV-VoI must beat this on the frontier or it is dead on arrival.

**Weighting axis (isolate DDWC):**
- **CISC** (Taubenfeld et al. 2025) — confidence-weighted vote; = DDWC with `S` removed; isolates whether redundancy adds anything beyond `c_i`.
- **VecCISC** (2605.08070) — hard-cluster redundancy-discounted weighted SC; the **soft-vs-hard head-to-head** for DDWC's core claim.
- **Nine-Judges Kish-ESS weighting** (2605.29800) applied as an aggregator — shows DDWC adds beyond published Kish ESS.
- **Ridge-leverage / DPP-marginal weighted votes** (Alaoui & Mahoney 2015) — principled-weighting **oracle ablation** vs. the cheap `1/rowsum`.
- **Universal SC** (Chen et al. 2023) / **semantic-entropy clustering** (Kuhn 2023; Farquhar 2024) — hard-clustering redundancy-collapse baseline and aggregator for non-exact-match answers.

**Stopping axis (isolate VoI-Stop):**
- **ESC** (Li et al. 2024) — window-based stopping.
- **Optimal Bayesian Stopping** (2602.05395) — strongest posterior-threshold competitor.
- At least one cost-aware / anytime-valid stopper: **MARS** (2606.12935), **CITE** (2605.05873), or **ConSol SPRT** (2503.17587) — to contest the VoI novelty.
- **DeepConf-online** (2508.15260) if feasible — confidence-weighted vote with mid-stream stopping.

**Combined competitor (hardest to beat):**
- **RASC** (Wan et al. 2024) — similarity/quality-weighted vote + criteria-based early stop; the single closest combined method.

**Accuracy ceiling / fair strong baseline:**
- **Verifier / PRM best-of-N** reranker at matched budget (Cobbe 2021; Lightman 2023).

**Internal ablations (factorial):**
(a) reweight-only@fixedK vs. stop-only@raw-counts vs. full;
(b) DDWC-no-c vs. CISC-only vs. DDWC·c (separate redundancy from confidence);
(c) VoI-Stop fed **raw** `n_a` vs. **effective** `n_eff·p_a` (proves the coupling changes *when* to stop);
(d) **naive `α₀+W_a` vs. ESS-corrected `α₀+n_eff·p_a`** (proves the calibration fix);
(e) kernel: dup-only vs. sem-only vs. dup+sem (tests the safety decomposition); GLOBAL vs. WITHIN-CLASS vs. DECOMP scope;
(f) **guard on/off** (measures the never-worse-than-SC property directly);
(g) stopping conjunction `min(P^raw,P^eff)` vs. `P^eff` alone vs. fixed-τ vs. e-process guard;
(h) sensitivity sweeps over `ρ, θ_dup, γ, β_sem, α₀, τ, λ, ρ_over` (report robustness, not a tuned point).

---

## 8. Experiment Design

### 8.a Simulated Oracle (ground-truth, tunable correlated errors) — the fair test

**Generative model of LLM CoT voting with latent truth + distractor modes.** Per synthetic question:

1. **Latent truth:** correct answer `a* ~ Uniform{1..A}` (default `A=6`). Fix `D` distractor answer modes `a_1..a_D ≠ a*` (default `D=4`).
2. **Reasoning modes = mixture components,** each tied to an answer: mode 0 → `a*`; modes 1..D → distractor answers. Mode `t` has embedding centroid `μ_t ∈ ℝ^d`, spread `σ_t`, and a verbatim-copy rate `ρ_t`.
3. **Mode-selection** `π = (π_0,...,π_D)` sets difficulty (easy: `π_0` large; hard: `π_0 ≤ max_j π_j`).
4. **Sampling a trace i:**
```
 t_i ~ Categorical(π)
 a_i = ans(t_i)   with slip probability s   (a_i ← uniform wrong with prob s)
 e_i = μ_{t_i} + N(0, σ_{t_i}² I)           # small σ ⇒ tight/correlated cluster
 with prob ρ_{t_i}: e_i, tokens ← near-verbatim copy of a prior trace from t_i   # drives dup_ij → ~1
 c_i ~ Beta(mean = m_correct if a_i=a* else m_wrong, scaled by miscalibration knob κ_c)
        # κ_c=1 calibrated, κ_c=0 uninformative, κ_c<0 anti-calibrated
```
Ground truth `a*` and true mode probabilities are known ⇒ exact accuracy, exact stopping-time, exact `P_stable` calibration, and an oracle-optimal stopping time computed from the known mode probabilities.

**Designed regimes (swept over seeds):**

| Regime | Setup | Prediction | Falsifier |
|---|---|---|---|
| **R1 INDEPENDENT** | all `σ` large, no copies | `n_eff≈K`, `w≈uniform`, RLEV-VoI ≈ ASC, DDWC ≈ SC | "reduces to ASC/SC" FALSE if they diverge beyond noise |
| **R2 CORRELATED-WRONG** | one distractor mode tight (`σ_t` small, `π_t` high), correct diffuse | guarded DDWC & full system **beat** SC and ASC at matched tokens | DDWC-value claim FALSE if not |
| **R3 BACKFIRE / EASY-CORRECT-CLUSTER** | correct mode tight & dominant, distractors diffuse (verified to flip 6-vs-5 under naive DDWC) | GLOBAL DDWC HURTS (reported openly); DECOMP/WITHIN-CLASS + guard ≈ SC | confound-fix FALSE if DECOMP+guard underperforms SC |
| **R4 ADVERSARIAL DUPLICATION** | inject `m` verbatim copies (`ρ_t=1`) of a wrong template | guard fires, recovers `a*`; SC fails | recovery claim FALSE if not |
| **R5 MISCALIBRATED CONFIDENCE** | `κ_c ≤ 0` | ECE gate switches `g(c)=1`; no degradation | robustness FALSE if folding `c` degrades below SC |

**Stopping / calibration checks:** (i) accuracy vs. expected #chains and vs. token-equivalents (Pareto/AUC); (ii) **reliability diagram** of `P_stable` vs. empirical `Pr(leader = a*)` — the ESS-corrected posterior must lie near the diagonal, the naive `α₀+W_a` version must be over-confident (this *directly demonstrates the calibration novelty*); (iii) over/under-stopping rate vs. the oracle-optimal stopping time; (iv) guard-firing rate and precision (fires in R4, silent in R3); (v) `Pr[worse than SC]` across seeds (target ≈0 in R1/R3/R5).

**Metrics:** accuracy; Pareto-AUC vs. SC; mean/median stopping K; `P_stable` ECE (raw vs. eff vs. min-conjunction); backfire/flip rate; full sensitivity sweeps (report sweeps, not best point).

**Per-claim confirm/falsify:**
- *Calibration fix (Novelty 1):* CONFIRM if corrected-posterior ECE ≪ naive-posterior ECE across regimes; FALSIFY if indistinguishable.
- *Safety decomposition (Novelty 2):* CONFIRM if dup+sem ≠ sem-only and DECOMP+guard ≈ SC in R3; FALSIFY if sem-only matches dup+sem (decomposition adds nothing) or the dup guard flags genuine correct clusters as verbatim (low precision).
- *No-regret guard (Novelty 3):* CONFIRM if `Pr[worse than SC] ≈ 0` in R1/R3/R5 while DDWC > SC in R2/R4; FALSIFY on any regime violation.
- *Coupling / VoI branch (Novelty 4):* CONFIRM if VoI-Stop Pareto-dominates τ-only stopping AND ablation (c) shows `T(S) ≠ T(I)`; FALSIFY if frontiers overlap within CI or stopping times coincide.

### 8.b Real-API Design

**Datasets** spanning both reasoning geometries:
- *Tight-derivation / exact-match* (GSM8K, MATH subset, MBPP code) — where naive DDWC is predicted to **backfire** and the guard must save it (correlated-CORRECT stress).
- *Diverse-reasoning / distractor-heavy* (CommonsenseQA, StrategyQA, ARC-Challenge, MMLU-subset) — where redundancy discounting has headroom (correlated-WRONG stress).
- *One free-form / non-exact-match set* to test Universal-SC-style aggregation where exact match fails.

**Models:** ≥2 open-weights across scales (e.g. Llama-3.1-8B/70B or Qwen2.5-7B/72B) **plus** one frontier API model — explicitly to test the "SC is losing its edge on frontier models" risk (2511.00751); report honestly whether savings survive on the strong model.

**Sampling (paired, cached):** draw up to `K_max=40` CoT traces/item at temperature ∈ {0.7, 1.0} **once**, cache. **All** methods (SC-K, ASC, ESC, CISC, RASC, VecCISC, Optimal-Bayesian-Stopping, DeepConf, RLEV-VoI + all ablations) **replay the same cached traces**, so differences are purely aggregation/stopping and comparisons are paired/low-variance. Parse `a_k`; `c_k` from verbalized confidence AND a logprob-derived variant (report both — CISC miscalibration caveat); `sem` from a local sentence encoder over the rationale; `dup` from char/word n-gram Jaccard. Precompute the full 40×40 `S_sem`, `S_dup` once.

**Cost accounting:** x-axis = total token-equivalents = generation tokens + `ρ_over`·(embedding + `O(K²)` similarity + posterior/VoI ops), `ρ_over` measured on target hardware; **report with AND without** embedding cost, at `ρ_over ∈ {0.5,1,2}×`; report the crossover K below which overhead erases savings. **Never matched-K.**

**Metrics:** accuracy@matched-tokens; AUC(accuracy–token); per-item win/loss vs. SC (McNemar); wall-clock; stopping-time histograms; guard-firing rate + manual audit of overturned items; `P_stable` calibration.

**Primary result that makes the paper (CONFIRM):** RLEV-VoI Pareto-dominates **both** RASC+ASC and VecCISC+ASC at matched total cost on the distractor-heavy sets, is **within-noise of SC** on GSM8K/MATH/MBPP (no backfire, guard-verified), ablation (d) shows the ESS correction is necessary for calibrated stopping, and ablation (c) shows weighted counts change *when* to stop vs. raw counts.

**No-paper conditions (FALSIFY):** at matched total cost RLEV-VoI does not clearly dominate RASC and ASC (frontiers within CI); OR guarded DDWC is significantly below SC in *any* dataset×model cell; OR WITHIN-CLASS/DECOMP DDWC gives no gain over CISC; OR the sem-only kernel matches dup+sem (decomposition adds nothing); OR the VoI branch offers no token savings over the stability-only rule at equal accuracy; OR gains fall inside diminishing-returns noise on the strong model. Report as a negative result and name the regimes where redundancy-discounting backfires.

---

## 9. Limitations

1. **Similarity = correctness confound (central risk).** On math/code the correct answer is often *one canonical near-duplicate derivation* while wrong answers are idiosyncratic; naive global inverse-similarity discounts the correct cluster and up-weights diverse-but-wrong chains (verified: flips 6-correct-vs-5-wrong to WRONG). Mitigated by the dup-vs-sem decomposition + SC-fallback guard, but this must be *demonstrated* to neutralize the backfire, not assumed.
2. **Weight collapse / kernel brittleness.** With dense embedding cosine, `Σ_j S_ij` is near-constant ⇒ `w→uniform` ⇒ DDWC degenerates to SC (benign but no gain); a too-sharp threshold degenerates to hard clustering (VecCISC). The method lives in a narrow kernel regime; results hinge on `ρ, β_sem, θ, γ` — sweeps required, overfitting risk real.
3. **Broken conjugacy is only *bounded*, not eliminated.** Fractional/correlated effective counts are not multinomial draws, so `P^eff_stable` is a heuristic; the `min(P^raw,P^eff)` conjunction makes it *one-sided safe* (can only over-delay), but if `n_eff` is mis-estimated (e.g. an off-distribution outlier trace with near-zero similarity to all others gets a huge `1/s_i` weight, inflating the vote and shrinking `n_eff`), the effective posterior is distorted. Needs weight-winsorization + near-duplicate-flooding stability checks; the consensus argmax still uses full `w`, so outlier domination is a live failure mode partially handled by clip + guard margin `δ`.
4. **No anytime-valid guarantee.** Fixed-`τ` optional stopping inflates Type-I error; the min-conjunction is conservative but not a martingale certificate. For formal error control, pair with an e-process (CITE-style) — offered as an optional mode that stops later; both must be reported.
5. **Miscalibrated self-confidence.** Folding `c_i` can inject noise and interact badly with the redundancy discount; auto-disabled by the ECE gate, default cautious.
6. **Overhead can erase savings at small K.** Embedding + `O(K²)` similarity + one-step VoI lookahead can exceed tokens saved where SC is already cheap; only an honest total-cost x-axis (including these) makes the dominance claim fair. Report the crossover K.
7. **Diminishing returns on frontier models** ("SC is losing its edge", 2511.00751): token-savings and accuracy headroom may shrink to noise on strong models, undercutting the Pareto claim; must be measured, not assumed.
8. **Novelty is narrow and the space is fast-moving.** Reviewers will cite ASC (Dirichlet stop), CISC (confidence weight), RASC/VecCISC (similarity weight + early stop), Kish-ESS (Nine Judges), Optimal Bayesian Stopping, and the 2025–26 cost-aware-stopping cluster (MARS, CITE, ConSol). The paper survives **only** if (a) the ESS-calibration fix, (b) the dup-vs-sem safety decomposition, (c) the never-worse-than-SC guard, and (d) a clean matched-budget win over RASC+ASC and VecCISC+ASC with isolating ablations all hold. Absent that, it reads as three known pieces bolted together in a closing window — and should be published, if at all, as a rigorous negative/robustness result.