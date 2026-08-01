Abstract—Confidence-weighted self-consistency (CISC and
its successors) improves on majority voting when a frozen
large language model’s self-reported confidence is calibrated
in direction. Every published weighting scheme is structurally
monotone increasing in confidence, so an anti-correlated chan-
nel poisons the vote instead of informing it, while binary
dev-set gates survive inversion only by discarding genuinely
discriminative signal. This paper presents tact (Trust-Anchored
Confidence Tempering), which replaces the fixed confidence
exponent with one derived from the measured, signed, within-
item discrimination of the channel: a pooled van Elteren
Somers’ D rank statistic with an item-clustered standard error,
passed through positive-part James–Stein shrinkage and a
Bayes-discriminant link. Written out, the method is a single
expression whose exponent reduces to γ = z
√
2 + z2 with z the
probit of the shrunk pooled AUC, and it carries exact anchors:
inside the shrinkage dead zone the vote is bit-identical to plain
self-consistency, and a log-value feature map reproduces CISC-
power. A label-free variant estimates the signed reliability from
agreement pseudo-labels under a proven attenuation identity
that guarantees sign consistency whenever the plurality-error
rate is below one half, with conservative de-attenuation and
echo alarms at the identifiability boundary. On a synthetic-
oracle harness with paired trace pools, the label-free variant
recovers anti-correlated channels that pin every published
protocol to the majority-vote floor (κ = −0.6: 1.000 vs. 0.807),
rank invariance beats the oracle over the entire raw-value
weight family under monotone confidence compression (1.000
vs. 0.965), and a per-group extension cracks the heterogeneity
floor with zero paired losses to self-consistency (0.940 vs. 0.808;
+79/−0, p = 3.3×10−24). Two real-trace campaigns on a frozen
model confirm the premise and locate the binding constraint:
within-item discrimination is positive on competition math-
ematics (pooled bD = +0.250, z = +2.54), yet the stratum
on which any such method can act, where the plurality is
wrong and the correct answer is present in the pool, measures
2–7.5% of items across five substrates in two domains, code
generation with executable ground truth included. Abstention
is therefore the correct default rather than a conservative one,
and the dead zone implements it exactly. The paper further
proves that per-item label-free adaptation is impossible under
i.i.d. latent coupling, and pre-registers four falsification criteria,
among them the published dev-calibrated CISC protocol as a
designated killer baseline, all of which the method survived.
Index Terms—large language models, self-consistency, confi-
dence calibration, weighted voting, label-free estimation, rank
statistics
I. Introduction
Self-consistency (sc) [1] improves the reasoning accuracy
of a frozen large language model (LLM) by sampling K
chain-of-thought traces and returning the plurality answer.
Because each trace can also report a confidence score
(verbalized [6], [7], derived from token log-probabilities, or
elicited as P(True) [5]), a natural refinement is to weight
votes by confidence. Confidence-Informed Self-Consistency
(CISC) [2] showed that this recovers the accuracy of plain
sc at a fraction of the sampling budget, and introduced
Within-Question Discrimination (WQD) to argue that
discrimination, not calibration, is the property that makes
a confidence signal useful for voting.
This refinement carries a structural fragility that, to the
author’s knowledge, no published method addresses. Every
existing weighting scheme is monotone increasing in confi-
dence, including CISC’s softmax weights, reliability-aware
pseudo-counts [11], and warmup-thresholded filtering [12].
The trust decision is which magnitude of up-weighting to
apply; the possibility that the channel is anti-correlated
with correctness is not representable. Yet miscalibration
of direction is not exotic: reinforcement fine-tuning is
known to distort verbalized confidence, distribution shift
can invert a signal that was informative in-domain, and
in the experiments reported here a simple anti-correlated
channel (κ = −0.6; Section III) drives confidence-weighted
baselines from near-perfect accuracy to far below the
majority-vote floor, while the same evidence, read with
the correct sign, is a perfect signal. The defensive alter-
native, a binary dev-set gate that disables the channel
when calibration error is high, survives the inversion but
discards discriminative signal wholesale: a systematically
under-confident yet perfectly ranked channel fails an ECE
gate for reasons irrelevant to voting utility [2], [8].
This paper frames the problem as estimating one scalar:
the signed within-item discrimination of the confidence
channel, and mapping that scalar, with its uncertainty, to
a vote exponent. The contributions are:
C1: Signed, analytically-tempered confidence weighting.
tact votes with weights wi = exp(γ φi), where φi is
the standardized van der Waerden score of trace i’s
within-item confidence midrank, and γ is derived, not
grid-searched: a pooled van Elteren Somers’ D statistic
(equal to 2 · WQD −1) with an exact tie-corrected null
variance and an item-clustered jackknife standard error,
shrunk by positive-part James–Stein with a significance
floor, then mapped through a Bayes-discriminant link with
a mixture-variance correction. The construction carries
exact anchors: inside the shrinkage dead zone the vote
is bit-identical to plain sc (a shared code path), and
the log-value feature map reproduces CISC-power exactly

(Section IV). Because φ depends on confidence only
through within-item ranks, the entire method is invariant
to every strictly monotone distortion of the confidence
scale; under monotone compression it beats the oracle over
the whole raw-value weight family (1.000 vs. 0.965).
C2: Label-free estimation of the signed reliability. The
crowdsourcing lineage estimates annotator reliability from
cross-annotator covariance [13], [16]; a single exchange-
able confidence channel from one model offers no such
structure. The signed discrimination is estimated from
agreement pseudo-labels (deduplication-weighted plurality
per item) with a proven class-conditional-noise attenua-
tion identity, E[ bDg] = (1 −2¯ρ) D: the label-free estimate
can only under-trust, never mis-sign, whenever the pair-
weighted plurality-error rate ¯ρ is below 1/2. A split-
half agreement inversion de-attenuates conservatively, and
sign-aware alarms return the method to plain sc when
identifiability is threatened. On the coupling sweep the
label-free variant matches the 200-label variant nearly
point-for-point, including full recovery of negative chan-
nels (Section VIII).
C3: An impossibility result and its structured escape.
When the per-item coupling is i.i.d. with no observable
covariate, per-item label-free adaptation is shown to be
closed: any monotone use of an item’s own agreement
statistic collapses to plurality reinforcement; on exactly
the plurality-wrong items where a flip could help, the
observable sign opposes the truth 96% of the time;
and the two hypotheses {κ > 0, minority correct} and
{κ < 0, plurality correct} induce identical observable laws.
When heterogeneity is instead indexed by an observable
covariate (domain-dependent calibration), running the
same estimator per group recovers each group’s signed
coupling and approaches the per-item oracle with zero
paired losses to sc (Section VI).
C4: A pre-registered falsification protocol. Four falsi-
fiers were fixed before implementation, including the two
designed to kill the method: the published dev-calibrated
CISC protocol (whose tuned temperature already inter-
polates sc↔CISC) and a trivial dev-picked signed ex-
ponent grid. All four survived, and the honest margins
are reported: against the signed grid the net advantage
concentrates in three cells: monotone distortion, confident
echo, and label-free operation, which no grid can perform.
II. Related Work
Confidence-weighted self-consistency. sc [1] treats sam-
pled traces as i.i.d. votes. CISC [2] weights votes by
softmax-normalized confidence with a temperature tuned
on a labeled split, and its WQD metric makes the
discrimination-vs-calibration point that also motivates
this
work;
the
rank-calibration
line
[8]
reaches
the
same conclusion independently. Weighted variants [9],
[10] and early-stopping families [3], [4] refine the bud-
get; reliability-aware pseudo-counts [11] and warmup-
thresholded filtering [12] adapt online but only re-scale
positive trust. None of these can represent, much less
estimate, a negative confidence–correctness association.
The dev-calibrated variant must therefore be positioned
honestly: CISC’s tuned temperature is already a dev-
calibrated sc↔CISC interpolation, so the novelty of tact-
dev lies in the sign, the rank invariance, and the analytic
(grid-free) map, not in dev calibration itself.
Reliability estimation without labels. Estimating worker
reliability from agreement is classical [13], [14], [15];
spectral meta-learners [16] and recent LLM ensemble work
[17], [18] exploit covariance across multiple predictors. The
setting here differs: one exchangeable channel from one
model, per-item vote structure, and the known failure
of agreement proxies under correlated errors—met here
with a quantified attenuation identity, conservative de-
attenuation, and alarms in place of an unconditional claim.
Shrinkage and rank statistics. The estimator assem-
bles classical parts: stratified rank statistics [19], the
James–Stein positive-part estimator [20], effective-sample-
size corrections [21], [22], and normal-scores discriminant