# TACT: Trust-Anchored Confidence Tempering

### Final specification (synthesized from three independent designs + prior-art survey; self-red-teamed — see §10)

---

## 1. Name & abstract

**TACT** replaces CISC's fixed confidence exponent with an exponent **derived** from the measured, *signed*, within-item discrimination of the confidence channel. One scalar estimand — pooled Somers' `D = 2·WQD − 1`, a pure rank statistic — is estimated with an item-clustered standard error, pushed through positive-part James–Stein shrinkage (no evidence ⇒ `γ = 0` **exactly**, bit-identical to plain SC), then through the closed-form Bayes-discriminant link to the exponent of the vote weight `w_i = exp(γ·φ_i)`, where `φ_i` is the within-item van der Waerden normal score of the trace's confidence midrank.

Two variants: **TACT-dev** (a small labeled dev split estimates `(D, SE)` once) and **TACT-LF** (label-free: agreement pseudo-labels + dedup + margin gating + split-half de-attenuation + echo alarms). A **semi-LF** mode takes the *sign* from ~50 labels and the *magnitude* from unlabeled traffic.

## 2. Honest novelty positioning

What is **not** new (cite, don't claim):

- The discrimination-not-calibration insight **is CISC's own WQD metric** (arXiv:2502.06233); Rank-Calibration (2404.03163) makes the ECE-vs-AUROC point independently.
- A dev-calibrated SC↔CISC interpolation **already exists as CISC's standard protocol** (softmax temperature `T` tuned on a labeled split; `T→∞` is SC). TACT-dev must therefore beat/match **CISC-devT**, not merely a binary ECE gate.
- Rank-based confidence voting with a power exponent exists (self-certainty Borda voting, 2502.18581).
- ReASC (2601.02970) is the closest by name; its GMM calibrates *per-response evidence strength*, never the confidence–correctness association — it would collapse on anti-correlated confidence exactly like CISC.
- Agreement-based reliability estimation and its correlated-error failure are the crowdsourcing lineage (Dawid–Skene; Parisi et al. PNAS 2014; label-free verifier work FUSE 2604.18547, "Beyond Majority Voting" 2510.01499).

The defensible contributions:

1. **Signed** trust: every published confidence-weighting scheme can only up-weight high confidence; an anti-correlated channel poisons them all. TACT estimates the sign and can *exploit* negative coupling.
2. The **analytic** estimate→exponent pipeline (statistic → shrinkage → discriminant link) with **exact anchors**: dead-zone ⇒ bitwise SC; `φ = log c − mean(log c)` ⇒ exactly CISC-power at the same `γ`; the link is the Bayes-optimal exponent under the working model, not a grid search.
3. The **label-free signed-reliability estimator for a single exchangeable confidence channel** (no cross-classifier covariance available), with a quantified poisoning theorem, a conservative de-attenuation, and pre-registered alarms — its guarantee is *conditional* and stated as such.

## 3. Notation

| symbol | meaning |
|---|---|
| `q = 1..Q`, `m_q` | items; traces per item |
| `a_{q,i}`, `c_{q,i}` | answer (cluster id) and confidence of trace `i` |
| `y_{q,i}` | correctness (dev only) |
| `R_{q,i}` | within-item midrank of `c_{q,i}` (ties averaged) |
| `φ_{q,i}` | standardized van der Waerden score of `R_{q,i}` |
| `n1_q, n0_q` | positives / negatives under the label in use; `N_q = n1_q·n0_q` |
| `D_q`, `D̂` | per-item and pooled signed discrimination |
| `ν` | significance floor of the shrinkage dead zone |
| `γ̂` | the shipped exponent; `w = exp(γ̂·φ)` |
| `p̄` | fraction of correct traces (base rate), for the link correction |
| `ρ̄` | pair-weighted P(item plurality is wrong) — the LF poisoning rate |

## 4. Math

### 4.1 Vote family

```
φ_{q,i} = (v_{q,i} − v̄_q)/σ_q,   v_{q,i} = Φ⁻¹(R_{q,i}/(m_q+1))
σ_q = realized SD of v within the item (NOT a closed form — the no-tie value
      is 0.62 at m=4 vs 0.95 at m=40; a closed form silently rescales γ)
σ_q ≤ 1e-8  ⇒  φ ≡ 0 for the item (all-tied confidences vote as plain SC)

w_{q,i} = exp(clip(γ̂·φ_{q,i}, ±50)),   answer = argmax_A Σ_{i∈A} w_{q,i}
γ̂ == 0  ⇒  CALL THE SC ROUTINE ITSELF (bitwise-identical output, not just equal in distribution)
```

Monotone-invariance: `φ` depends on `c` only through within-item ranks, so any strictly increasing distortion of the confidence scale (compression, over-confidence, powers) leaves the entire method unchanged.

### 4.2 The statistic

Per informative item (`n1_q·n0_q > 0`), Mann–Whitney on midranks:

```
U_q = Σ_{i: lab=1} R_{q,i} − n1_q(n1_q+1)/2
AUC_q = U_q/(n1_q·n0_q),      D_q = 2·AUC_q − 1        (= 2·WQD_q − 1)
D̂ = Σ_q N_q D_q / Σ_q N_q                              (van Elteren pooling)
```

Null variance (exact, tie-corrected): `Var₀(U_q) = n1n0(m+1)/12·[1 − Σ(t³−t)/(m³−m)]`; items independent ⇒ `SE₀`. Heterogeneity-robust: delete-one-**item** jackknife `SE_J` (closed form, O(Q)). Use `SE = max(SE₀, SE_J, 1/(2√N))`. Score-test z: `r = D̂/SE`.

Budget invariance: `D` is a pairwise functional — `E[D̂]` does not depend on `m_q`, so a `γ̂` estimated at `m=40` transfers to deployment at `m=8`.

### 4.3 Tempering map

**Shrinkage** (positive-part James–Stein with a significance floor):

```
D̃ = sign(D̂)·max(0, |D̂| − ν²·SE²/|D̂|)        dead zone ⇔ |r| ≤ ν
ν_dev = 1.2816 (one-sided 10%),  ν_LF = 2.326 (one-sided 1%)
```

Empirical-Bayes identity: with prior `D ~ N(0,τ²)` and plug-in `τ̂² = max(0, D̂²−SE²)`, the posterior mean is exactly this shrinker at `ν = 1`. Properties: dead zone; `|D̃| ≤ |D̂|` (never trusts more than the point estimate); odd; continuous; monotone in `D̂`, anti-monotone in `SE`.

**Link** (Bayes discriminant under the working model, with the mixture-variance correction):

```
u  = √2·Φ⁻¹((1+D̃)/2)
γ* = u·√(1 + p̄(1−p̄)·u²)          [exact under the model; reduces to u if the
                                    correction is disabled]
γ̂  = clip(γ*, ±γ_max),  γ_max_dev = 4, γ_max_LF = 2
```

Derivation: `φ|y ~ N(μ_y, s²)` within item with the *mixture* standardized to unit variance forces `s² = 1/(1+p̄(1−p̄)u²)`; `AUC = Φ(Δ/(s√2))` gives `Δ/s = u`; the Nitzan–Paroush optimal per-trace log-weight is `(Δ/s²)·φ`, i.e. `γ* = u/s`. The uncorrected `L(D) = u` (set `p̄` term to 0) under-weights strong channels by up to ~50% at `D = 0.9`.

`p̄`: estimated on dev; fixed at 0.5 in TACT-LF (the cap `γ_max_LF = 2` binds first anyway).

### 4.4 TACT-dev

Labeled dev split (default 200 items, min 50): compute `(D̂, SE, r)` with `lab = y`, ship `γ̂ = g(D̂, SE)`. Report `(D̂, SE, r)` and dev ECE as diagnostics — **ECE never gates**. Dev-set accuracy, when reported, uses 5-fold cross-fitting.

### 4.5 TACT-LF (label-free)

1. **Dedup first**: single-linkage duplicate groups at `dup ≥ 0.95` (the harness's lexical channel); dedup weight `d_i = 1/|group|` for plurality determination and pair weighting.
2. **Pseudo-label**: `g_{q,i} = 1[a_{q,i} = dedup-weighted plurality]`; margin `mgn_q`.
3. **Margin gate**: keep the top 60% of items by margin (τ_M = 0.40 quantile), `|K_q| ≥ 2`.
4. **Raw statistic**: `(D_g, SE_g, r_g)` with `lab = g` on the gated set.
5. **Poisoning theorem** (class-conditional noise): with `ρ̄` = pair-weighted P(plurality wrong), if the flip is independent of `φ` given `y` then `E[D_g] = (1−2ρ̄)·D_true` — attenuation only, **sign preserved** whenever `ρ̄ < 1/2`. The theorem **fails** exactly under confident echo (flip caused by confidence): the observable law under {majority right, D<0} and {majority wrong via confident echo, D>0} is *identical* (Parisi/Hui–Walter sign ambiguity), so the LF guarantee is conditional on `ρ̄ < 1/2` after dedup, and the paper says so.
6. **De-attenuation** (conservative): split-half agreement rate `α` over R=20 random half-splits; one-coin model `α = p² + (1−p)²/k` with `k = Keff−1` ⇒ `p = [1+√(1−(k+1)(1−kα))]/(k+1)` (larger root under majority-competence); `att = clip(UCB₉₅(2p−1), 0.20, 1)`; `D_LF = D_g/att` (dividing by the **upper** bound minimizes inflation).
7. **Echo alarms** (any ⇒ `γ̂ = 0`): E1 duplicate collapse (`median m_eff/m < 0.5`); E2 margin-decoupling (`ψ = f_low − f_high > 0.05`, where `f_·` = fraction of bottom/top-margin-tercile items whose plurality also has the highest mean `φ`); E3 root ambiguity (`Disc < 0.02`); E4 `< 50` informative gated items.
8. **Gate on the raw z, temper on the de-attenuated value**: `γ̂ = 0` if any alarm or `|r_g| ≤ ν_LF`, else `g(D_LF, SE_g/att)` capped at `±γ_max_LF`.
9. **Online**: warmup W=200 items at `γ = 0`; recompute every 50 items from the trailing window only (cross-fitting).

### 4.6 Semi-LF (recommended deployment)

Sign from dev (`s = sign(D̂_dev)` if `|r_dev| > 1`, else 0); magnitude from unlabeled traffic. Buys immunity to the §4.5 sign-ambiguity theorem with ~50 labels.

### 4.7 Scope: heterogeneity

TACT ships one global exponent; under per-item `κ_q`, `D̂` estimates the pair-weighted mean and `SE_J` inflates honestly. **TACT-hier** (ablation): two-level shrinkage `γ_q = link(D̃ + shrink_q·(D_q − D̂))`, `shrink_q = τ_b²/(τ_b²+SE_q²)`, `τ_b² = max(0, Var_q(D_q) − mean SE_q²)`. Per-item `D_q` at `m = 40` has `SE ≈ 0.15`, so expectations are modest and stated up front.

## 5. Anchors (proved in the designs, pinned by tests)

- **A1** `γ = 0` ⇒ bitwise SC (`w ≡ 1` + shared code path). Under the null, `P(dead zone) → 2Φ(ν)−1` (80% dev / 98% LF); outside it `γ̂` is continuous through 0, so a false positive applies an infinitesimal exponent.
- **A2** `φ = log c − mean_q(log c)` makes `w = κ_q·c^γ` ⇒ argmax and normalized vote shares **identical to CISC-power(γ)** for every pool.
- **A3** `g` is continuous, odd, monotone in `D̂`, anti-monotone in `|SE|`, `g(D̂, 0⁺) = γ*(D̂)` (oracle exponent at zero noise).

## 6. Defaults

| param | value | note |
|---|---|---|
| `φ` | standardized vdW normal scores | realized σ_q, tie-safe |
| `ν_dev / ν_LF` | 1.2816 / 2.326 | dead-zone floors |
| `γ_max_dev / γ_max_LF` | 4 / 2 | |
| link correction | ON (dev, `p̄` from dev); OFF→`p̄=0.5` (LF) | |
| dev size | 200 (min 50) | |
| `s_dup / τ_M` | 0.95 / 0.40 | LF dedup & margin gate |
| split-half R / bootstrap B | 20 / 200 | |
| alarms | ξ_min=0.5, ψ_max=0.05, Disc≥0.02, Q_gate≥50 | frozen |
| warmup / refresh | 200 / 50 items | online LF |

## 7. Baselines

SC; CISC fixed-γ sweep {0.25,0.5,1,2,4}; **CISC-devT (the published dev-tuned protocol — the baseline that must not silently win)**; binary ECE gate; binary **discrimination** gate (dev WQD, no continuity) — isolates "right metric" from "continuous tempering"; sign-corrected binary gate γ∈{−1,0,+1} picked on dev; Borda-rank voting with fixed p; dedup-SC; ReASC-lite (GMM z-scores, positive-only) if feasible; Dawid–Skene one-coin EM control; oracle-tempered CISC (test-set best (γ, sign)) as the upper envelope.

## 8. Experiments & pre-registered falsifiers

Primary axis: the `κ_c` sweep (−0.6…+0.6) on the existing harness; adversarial regimes: three monotone distortions, heterogeneous `κ` (σ=0.6), confident echo (`echo_conf=0.9`), tail-only informativeness. Paired pools, McNemar + Holm across cells; dev/test split with dev also swept at n ∈ {50, 200}.

- **F1** TACT-dev significantly below the CISC frontier at `κ = +0.6` ⇒ G1 fails.
- **F2** TACT (either variant) significantly below SC anywhere on the sweep ⇒ G2 fails. For TACT-LF this claim is *conditional* on no alarm; alarm rates are reported per regime.
- **F3** TACT-LF fails to beat the binary ECE gate's frontier averaged over the sweep ⇒ the label-free machinery adds nothing over a crude gate.
- **F4** If **CISC-devT** or the sign-corrected binary dev gate matches TACT-dev's whole frontier (incl. distorted + heterogeneous + small-dev cells) ⇒ continuous analytic tempering adds nothing beyond published/dev-picked protocols ⇒ negative result, reported as such.
- Empirically pre-measured headroom (results/kappa_sweep.json): the AUC-style binary gate already reaches 0.994 at `κ=−0.6`; TACT's room to win is **monotone distortion (0.834 vs 0.956 oracle)**, **heterogeneous κ (all global policies at the SC floor 0.828)**, **small dev**, and **label-free operation**. If TACT only ties the binary gates on the homogeneous sweep, that is the expected outcome, not a win — the paper's claims live in the four gap cells.

## 9. Limitations

1. Global exponent: heterogeneous channels get the pair-weighted mean (hier variant is an ablation, expected modest).
2. TACT-LF's sign guarantee is conditional (`ρ̄ < 1/2` after dedup); confident echo defeats any label-free method — semi-LF is the honest fix.
3. The link is model-based (Gaussian normal-score discriminant); misspecification (tail-only signal) degrades toward — not below — the dead zone.
4. Dead zones sacrifice small true signals (`|D| ≲ ν·SE`), by design.
5. The working model's independence assumption across traces is violated by echo; dedup mitigates within the LF path only.

## 10. Self-red-team notes (in lieu of the budget-limited red-team stage)

- Verified numerically before implementation: the JS–EB identity; the van Elteren null variance against brute-force permutation; the mixture-variance link derivation (`s² = 1/(1+p̄(1−p̄)u²)`); the split-half quadratic roots. Each is pinned by a unit test.
- The known dangers: (a) **CISC-devT is the real competitor** — F4 includes it; (b) the sim generates exactly the coupling TACT estimates — circularity is limited by evaluating on *distorted/heterogeneous/echo* regimes the estimator was not told about, and the report separates "estimator recovers κ" (mechanism check) from "accuracy vs baselines" (the claim); (c) margin gating induces easy-item selection bias in `|D|` — attenuating, hence safe, but stated; (d) the de-attenuation UCB is anti-conservative if the one-coin model is wrong — alarms E2/E3 exist for exactly that, and `att_floor = 0.2` bounds the inflation at 5×.
