Abstract
Confidence-weighted self-consistency beats majority voting when a frozen model’s confi-
dence is calibrated in direction. Every published scheme is monotone increasing in confi-
dence, so an anti-correlated channel poisons the vote, and calibration gates survive inversion
only by discarding signal. tact derives the vote exponent from the measured signed within-
item discrimination of the channel: a pooled van Elteren Somers’ D, shrunk toward zero and
mapped through a Bayes-discriminant link that at base rate 1
2 collapses to γ = z
√
2 + z2.
Inside the dead zone the vote is bit-identical to plain self-consistency. A label-free variant
recovers the sign from agreement pseudo-labels, provably below a plurality-error rate of
one half and demonstrably wrongly past it. On a synthetic oracle it recovers channels that
pin published protocols to the majority floor (1.000 vs. 0.762) and cracks the heterogeneity
floor with zero paired losses (0.923 vs. 0.785); against a dev-picked signed grid the advan-
tage narrows to distortion, echo and label-free operation. Two real-trace campaigns bound
it: the channel is null on saturated benchmarks and positive on competition mathematics
( bD = +0.250), yet the stratum any such method can act on measures 2.5–7.5% of items
across five substrates in two domains. Abstention is the correct default, and the dead zone
implements it.
Keywords: large language models, self-consistency, confidence calibration, label-free esti-
mation, rank statistics
1 Introduction
Self-consistency (sc; Wang et al., 2023) improves the reasoning accuracy of a frozen large
language model (LLM) by sampling K chain-of-thought traces and returning the plural-
ity answer. Each trace can also report a confidence score, verbalized (Tian et al., 2023;
Xiong et al., 2024), derived from token log-probabilities, or elicited as P(True) (Kadavath
et al., 2022), so weighting votes by confidence is a natural refinement. Confidence-Informed
Self-Consistency (CISC; Taubenfeld et al., 2025) showed that this recovers the accuracy of
plain sc at a fraction of the sampling budget, and introduced Within-Question Discrimi-
nation (WQD) to argue that discrimination, not calibration, is the property that makes a
confidence signal useful for voting.
This refinement carries a structural fragility that, to the best of our knowledge, no
published method addresses. Every existing weighting scheme is monotone increasing in
confidence, including CISC’s softmax weights, reliability-aware pseudo-counts (Kim et al.,
2026), and warmup-thresholded filtering (Fu et al., 2026). The trust decision is which mag-
nitude of up-weighting to apply; the possibility that the channel is anti-correlated with
correctness is never searched for. Yet miscalibration of direction is not exotic: reinforce-
1

Ko
ment fine-tuning is known to distort verbalized confidence, distribution shift can invert
a signal that was informative in-domain, and in the experiments reported here a simple
anti-correlated channel (κ = −0.6; Section 3) drives confidence-weighted baselines from
near-perfect accuracy to far below the majority-vote floor, while the same evidence, read
with the correct sign, is a perfect signal. The defensive alternative, a binary dev-set gate
that disables the channel when calibration error is high, survives the inversion but discards
discriminative signal wholesale: a systematically under-confident yet perfectly ranked chan-
nel fails an ECE gate for reasons irrelevant to voting utility (Taubenfeld et al., 2025; Huang
et al., 2024).
This paper frames the problem as estimating one scalar: the signed within-item discrim-
ination of the confidence channel, and mapping that scalar, with its uncertainty, to a vote
exponent. The contributions are:
C1: Signed, analytically-tempered weighting. tact votes with wi = exp(γφi),
where φi is the standardized van der Waerden score of trace i’s within-item confidence
midrank and γ is derived, not grid-searched: a pooled van Elteren Somers’ D (equal to 2 ·
WQD−1) with an exact tie-corrected null variance and an item-clustered jackknife standard
error, shrunk by positive-part James–Stein with a significance floor, then mapped through a
Bayes-discriminant link. Two anchors are exact: inside the dead zone the vote is bit-identical
to sc via a shared code path, and the log-value feature map reproduces CISC-power. Since
φ uses only within-item ranks, the method is invariant to every strictly monotone distortion
of the confidence scale, and under compression it beats the best exponent in the tested grid
{0.25, 0.5, 1, 2, 4} (1.000 vs. 0.963; that optimum sits at the largest exponent tried, so the
comparison bounds the grid, not the family).
C2: Label-free estimation of the sign. The crowdsourcing lineage estimates reli-
ability from cross-annotator covariance (Dawid and Skene, 1979; Parisi et al., 2014); one
exchangeable channel from one model offers no such structure. tact estimates the signed
discrimination from deduplication-weighted agreement pseudo-labels under a proven class-
conditional-noise identity, E[ bDg] = (1 −2¯ρ)D: while the pair-weighted plurality-error rate
¯ρ is below 1/2 the estimate can only under-trust, never mis-sign. A split-half inversion
de-attenuates conservatively and sign-aware alarms return the method to sc at the identi-
fiability boundary. Past ¯ρ = 1/2 it does mis-sign, which Section 9 measures.
C3:
An impossibility result and its structured escape.
With i.i.d. per-item
coupling and no observable covariate, per-item label-free adaptation is closed: any monotone
use of an item’s own agreement statistic collapses to plurality reinforcement, the observable
sign opposes the truth on 96% of the plurality-wrong items with |Dq| > 0.3, the ones where
a flip could win, and {κ > 0, minority right} and {κ < 0, plurality right} induce the same
observable law. Indexed instead by an observable covariate, the same estimator run per
group recovers each group’s signed coupling with zero paired losses to sc (Section 6).
C4: A pre-registered falsification protocol. Four falsifiers were fixed before im-
plementation, two of them designed to kill the method: the published dev-calibrated CISC
protocol, whose tuned temperature already interpolates sc↔CISC, and a dev-picked signed
exponent grid, which the sweep shows is far the stronger of the two. All four survived, and
the margins are reported both ways: against the signed grid the advantage concentrates in
distortion, echo, and label-free operation, and tact trails it in the mid-range.
2

Trust-Anchored Confidence Tempering
C5: A measurement of the addressable stratum. Two real-trace campaigns and
a five-substrate window measurement bound what any label-free aggregation method can
do. The channel is null on saturated benchmarks ( bD = −0.219, z = −1.24) and positive
on competition mathematics (+0.250, z = +2.54), so the premise holds where the model
is uncertain; but the stratum such a method can act on is 2.5–7.5% of items across all five
substrates, in two domains, and does not widen as items harden. On both real substrates
the in-pool oracle itself cannot clear the pre-registered endpoint, which makes abstention
the correct default.
2 Related Work
Confidence-weighted self-consistency. sc (Wang et al., 2023) treats sampled traces as
i.i.d. votes. CISC (Taubenfeld et al., 2025) weights votes by softmax-normalized confidence
with a temperature tuned on a labeled split, and its WQD metric makes the discrimination-
vs-calibration point that also motivates this work; the rank-calibration line (Huang et al.,
2024) reaches the same conclusion independently. Weighted variants (Li et al., 2023) and
early-stopping families (Aggarwal et al., 2023; Li et al., 2024) refine the budget.
Self-
certainty (Kang et al., 2025) is the closest relative in spirit, being the one published selector
that scores candidates by a rank-like quantity, but it ranks across candidates with a fixed
positive orientation and is not evaluated here; reliability-aware pseudo-counts (Kim et al.,
2026) and warmup-thresholded filtering (Fu et al., 2026) adapt online but only re-scale
positive trust. None of these searches a negative exponent: the obstruction is a sign bit in the
hyperparameter grid rather than the weight family itself, as this paper’s own SignGrid-dev
baseline shows by opening the same cγ family to negative γ and reaching the signed oracle
across the negative half-axis. What no published protocol does is estimate that sign, with or
without labels. The dev-calibrated variant must therefore be positioned honestly: CISC’s
tuned temperature is already a dev-calibrated sc↔CISC interpolation, so the novelty of
tact-dev lies in the sign, the rank invariance, and the analytic (grid-free) map, not in dev
calibration itself.
Reliability estimation without labels. Estimating worker reliability from agreement
is classical (Dawid and Skene, 1979; Whitehill et al., 2009; Karger et al., 2011); spectral
meta-learners (Parisi et al., 2014) and recent LLM ensemble work (Lee et al., 2026; Ai
et al., 2025) exploit covariance across multiple predictors. The setting here differs: one
exchangeable channel from one model, per-item vote structure, and the known failure of
agreement proxies under correlated errors—met here with a quantified attenuation identity,
conservative de-attenuation, and alarms in place of an unconditional claim.
Shrinkage and rank statistics.
The estimator assembles classical parts: strati-
fied rank statistics (van Elteren, 1960), the James–Stein positive-part estimator (James
and Stein, 1961), effective-sample-size corrections (Kish, 1965; Rao and Scott, 1981), and
normal-scores discriminant analysis. The claim is the assembly and its anchors, not the
parts.
Honest sibling result.
A preceding system in the same line of work (RLEV-VoI,
redundancy-discounted voting with value-of-information stopping) was evaluated under the
same falsification discipline and failed it, dominated everywhere by a simple deduplication
3

Ko
baseline, and is reported as a negative result.
Its post-mortem isolated the confidence
dilemma studied here.
3 Problem Setup
3.1 Notation
Every symbol used in the paper is collected in Table 7 (Appendix A), grouped by the section
that introduces it. Items q = 1, . . . , Q; item q has mq sampled traces. Trace (q, i) yields an
answer aq,i in a discrete set and a confidence cq,i ∈(0, 1); correctness is yq,i = 1[aq,i = a∗
q],
unobserved at test time. Plain sc returns arg maxA nq(A) where nq(A) counts votes for
answer A. CISC-power weights votes by c γ
q,i with a fixed γ > 0.
3.2 The confidence dilemma
The synthetic oracle draws, per item, traces from a cluster mixture with a latent correct
answer and generates confidence as
cq,i = clip
  1
2 + κ (yq,i −1
2) + εq,i, 0.01, 0.99

,
(1)
with noise ε ∼N(0, 0.12) and coupling κ ∈[−0.6, 0.6]. Fig. 1 maps the baseline landscape
before the proposed method existed: unconditional weighting (CISC, γ = 1) collapses on
κ < 0; an ECE gate never opens off the well-calibrated diagonal; a sign-corrected AUC
gate over dev labels nearly saturates the homogeneous sweep. This pre-measurement fixes
where a new method can legitimately claim wins—monotone distortion of the confidence
scale, covariate heterogeneity, small dev sets, and label-free operation—and the evaluation
holds itself to exactly those cells.
4 TACT
4.1 Vote family
Within item q, let Rq,i be the midrank of cq,i (ties averaged) and
φq,i = vq,i −¯vq
σq
,
vq,i = Φ−1 Rq,i
mq + 1

,
(2)
where σq is the realized standard deviation of v within the item (the no-tie value is 0.62 at
m=4 but 0.95 at m=40; a closed form would silently rescale γ across budgets), and φ ≡0
if σq ≤10−8 (all-tied confidences vote as plain sc). The vote is
ˆaq = arg max
A
X
i: aq,i=A
exp
 
γ φq,i

,
(3)
and when γ = 0 the implementation calls the sc routine itself, making the zero-trust
anchor bitwise exact rather than equal in distribution.
Because (2) depends on c only
through within-item ranks, every strictly monotone distortion of the confidence scale leaves
(3) unchanged.
4

Trust-Anchored Confidence Tempering
−0.6
−0.4
−0.2
0.0
0.2
0.4
0.6
true confidence–correctness coupling κc
0.0
0.2
0.4
0.6
0.8
1.0
accuracy @ fixed K
SC (ignores confidence)
CISC γ = 1 (always trusts)
ECE gate (calibration)
AUC gate (discrimination + sign)
oracle fixed (γ, sign)
headroom for a new method
Figure 1: The pre-measured problem statement: accuracy of baseline confidence policies at
fixed K=15 as the true coupling κ varies.
A trivial sign-corrected AUC gate
(green) nearly saturates the homogeneous sweep; the headroom for any new