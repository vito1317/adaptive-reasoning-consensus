# ISC: Instrumented Self-Consistency

### Design specification v1 (theory drafted inline; novelty check and red team pending — see §9)

---

## 1. Abstract

Every published self-consistency method treats the trace pool as given: i.i.d.
samples from one fixed prompt. ISC treats the sampling protocol itself as a
design variable. The key move is to add **anchored instrument channels** —
sampling procedures whose coupling *sign* with correctness is fixed by
construction rather than estimated — and to show that this minimal
instrumentation converts the per-item identification problem from provably
impossible (TACT's Proposition 7) to solvable at a vanishing amortized cost.
ISC composes with TACT: the instrument decides the *world* (which answer group
is the correct one), the same rank machinery then measures the base channel
against instrument-anchored pseudo-labels, and TACT's tempering map turns the
measurement into vote weights. The construction is deliberately economical:
one Mann–Whitney statistic used twice.

## 2. The identification problem, restated

Setup as in TACT: item $q$, traces $i$ with answers $a_{q,i}$ and confidences
$c_{q,i}$; correctness $y_{q,i}$ unobserved. TACT's Prop. 7 (two-world
unidentifiability): for items whose traces take two values $A, B$, the worlds

$$w_1=\{a^*=A,\ \kappa>0\} \qquad w_2=\{a^*=B,\ \kappa<0\}$$

induce identical observable laws under the symmetric confidence model
$c = \mathrm{clip}(1/2+\kappa(y-1/2)+\varepsilon)$. No function of the pool
distinguishes them.

**Theorem 1 (necessity of an anchor).** Let the pool carry any finite number
$M$ of confidence channels $c^{(1)},\dots,c^{(M)}$, each following the
symmetric model with unknown couplings $\kappa_1,\dots,\kappa_M$. Then the
two-world ambiguity persists: the swap $(a^*\!: A\leftrightarrow B,\
\kappa_m \to -\kappa_m\ \forall m)$ leaves the joint law of all observables
invariant. *Proof sketch.* Swapping $a^*$ between the two present values flips
$y_i$ for every trace; each channel's conditional law is symmetric under
$(y,\kappa)\to(1-y,-\kappa)$; independence across channels given $y$ completes
the invariance. $\square$

Unanchored channels, no matter how many, all flip together. Identification
requires at least one channel whose sign cannot flip.

**Theorem 2 (sufficiency of one anchored channel).** Add an instrument
channel $V$: for a candidate answer $A$, an instrument query returns a score
$v$ with $\mathbb{E}[v \mid A=a^*] - \mathbb{E}[v \mid A\neq a^*] = \delta > 0$,
where the *sign* of $\delta$ is known by construction (magnitude unknown).
Then with $n_V$ instrument queries split across the two candidate groups, the
one-sided Mann–Whitney test of $v$(candidate $A$) vs $v$(candidate $B$)
decides between $w_1$ and $w_2$ with error probability decaying exponentially
in $n_V$; consequently the base channel's per-item sign, and TACT's pooled
$D$, become identified. *Proof sketch.* Under $w_1$ the $A$-queries
stochastically dominate; under $w_2$ they are dominated. The rank test's
error is controlled by the Mann–Whitney tail bound at effect $\delta$;
posterior consistency follows from the likelihood ratio of the two orderings.
$\square$

**Corollary (instrument attenuation).** If the instrument is invalid on a
fraction $\varepsilon$ of items (its judgment follows the model's systematic
error rather than the truth), the effective separation is $\delta(1-2\varepsilon)$:
the same class-conditional-noise attenuation as TACT's Prop. 4. The anchor
survives iff $\varepsilon < 1/2$, and $\varepsilon$ is the honest sensitivity
parameter of the whole method.

## 3. Instrument constructions

* **Verification channel $V_\text{ver}$** (default): sample a fresh trace that
  is shown candidate $A$ and asked to check it (recompute, test, refute);
  score = endorsement. Sign-positive by construction *to the extent that
  checking shares no error with the original solve* — the exclusion
  restriction. Independent re-derivations, unit-test execution (for code), or
  substitution checks (for math) approach $\varepsilon\to 0$; "does this look
  right" paraphrases do not.
* **Refutation channel $V_\text{ref}$**: ask for a concrete counterexample or
  error in the candidate's derivation; score = refutation *failure*.
  Sign-positive; complements $V_\text{ver}$ because its failure modes differ.
* What does **not** qualify: re-asking for confidence, paraphrased re-solves
  under the same prompt (these are the base channel again, and flip with it).

## 4. The ISC estimator

Two phases over a corpus of items, no labels anywhere.

**Phase A (identification, on a budgeted subset).** Select items to
instrument — lowest dedup-weighted margin first (where the plurality
pseudo-label is least trustworthy and the anchored label differs most).
On each, run $n_V$ instrument queries against the top-2 candidates; the
anchored answer $\hat a^{IV}_q$ is the Mann–Whitney winner if the one-sided
test passes at level $\alpha_V$, else undecided.

**Phase B (measurement + voting, everywhere).** Build pseudo-labels
$g_{q,i}=\mathbf 1[a_{q,i}=\hat a_q]$ using the anchored answer where decided
and the dedup-weighted plurality elsewhere; feed them to TACT's pooled
statistic, shrinkage and link unchanged (this replaces the plurality
pseudo-label of TACT-LF, whose poisoning rate $\bar\rho$ is now driven by the
*instrument's* error, not the vote's). Vote with $w=\exp(\gamma\varphi)$ on
all items; on instrumented items where the instrument margin is decisive,
the anchored answer overrides the weighted vote.

**Amortization.** The channel parameter $D$ is shared across items, so the
number of instrumented items needed for a given precision is $O(1/\text{SE}^2)$
— independent of corpus size $Q$. The identification tax per item is
$O(n_V \cdot m_{\text{instr}} / Q) \to 0$: asymptotically free.

**Diagnostics (all label-free).** I1: instrument decisiveness — median
Mann–Whitney margin across instrumented items; below floor ⇒ weak instrument,
fall back to TACT-LF. I2: instrument–plurality agreement rate; if ≈ 1 the
instrument adds nothing (benign corpus), if very low, flag either a poisoned
vote (good: that is the point) or an invalid instrument — disambiguated by I3:
anchored-vs-plurality label disagreement should concentrate on low-margin
items when the vote is poisoned, but be margin-uniform when the instrument is
broken.

## 5. Adaptive allocation (v2, sketched)

State: posterior over per-item answers and the shared channel coupling.
Action: next unit of budget → {base trace on item q, instrument query on
(item q, candidate A)}. Objective: corpus accuracy at fixed total traces.
Structure worth exploiting: instrument queries update a *shared* parameter —
a shared-parameter bandit whose exploration cost amortizes. v1 ships the
margin-stratified static rule; the bandit is future work.

## 6. Pre-registered falsifiers

* **F1 (the headline).** In the artifact-echo cell — where Prop. 7 makes every
  single-channel label-free method refuse or fail, and TACT-LF scores the SC
  floor 0.200 — ISC-LF at *matched total trace budget* must beat both TACT-LF
  and plain SC given the same extra budget as additional votes. The
  comparison against "just take more votes" is mandatory: extra plain votes
  *amplify* an echo, so this is the cell where instruments are provably the
  only use of budget that helps.
* **F2 (no instrument tax).** On benign cells ($\kappa$ sweep), adaptive ISC
  at matched budget within noise of TACT-LF (which is near-oracle there).
* **F3 (honest failure).** Under systematic-belief echo (verifier shares the
  error, $\varepsilon > 1/2$), ISC must *detect* instrument weakness via I1–I3
  and fall back, not answer confidently wrong.
* **F4 (theory check).** On constructed Prop-7 twin pools, the anchored test
  decides the world at its declared error rate, and an unanchored multi-channel
  variant provably cannot (empirical type-I ≈ chance).

## 7. Relation to prior art (to be verified by the survey — §9)

Verification/critique channels exist (self-verification, chain-of-verification,
generative verifiers, debate); they are used to *rescore answers*. The claimed
novelty here is different and threefold: (i) framing prompt selection as
**instrumental design for identification**, with necessity/sufficiency
theorems; (ii) using instruments to identify the *confidence channel's signed
reliability* label-free — not just to rescore the instrumented items; (iii)
the amortization result: a vanishing per-item identification tax, which
rescoring approaches (that must pay per item) do not have. If the survey finds
prior work on any of the three, the claim narrows accordingly.

## 8. Cost accounting

Instrument queries are traces and are charged as such. All comparisons at
matched *total* trace budget; the allocation between votes and instruments is
part of the method under test, never a hidden subsidy.

## 9. Status

Theory and this spec drafted inline (subagent budget exhausted until 23:40).
Pending before any strong claim: (a) an adversarial novelty sweep on
instrumental-variable framings of LLM inference and on verifier-based
aggregation; (b) a red team on Theorems 1–2 and the exclusion restriction;
(c) real-trace instrument validity measurement ($\varepsilon$ for Haiku
verification on GSM8K/CSQA).
