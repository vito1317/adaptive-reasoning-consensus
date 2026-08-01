# PDF rendered text (tact.pdf)

<!-- PDF PAGE 1/9 -->
TACT: Trust-Anchored Confidence Tempering for
Self-Consistency Voting in Large Language Models
Wei-Chen Ko (柯瑋宸, vito1317)
Independent Researcher
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
protocol to the majority-vote floor (κ = −0.6: 1.000 vs.
0.807), rank invariance beats the best exponent in the tested
raw-value grid {0.25, 0.5, 1, 2, 4} under monotone confidence
compression (1.000 vs. 0.965, the grid optimum sitting at
its upper endpoint), and a per-group extension cracks the
heterogeneity floor with zero paired losses to self-consistency
(0.940 vs. 0.808; +79/ −0, p = 3.3 × 10−24). Two real-trace
campaigns on a frozen model confirm the premise and locate
the binding constraint: within-item discrimination is positive
on competition mathematics (pooled bD = +0.250, z = +2.54),
yet the stratum on which any such method can act, where
the plurality is wrong and the correct answer is present in
the pool, measures 3–7.5% of items across five substrates in
two domains, code generation with executable ground truth
included. Abstention is therefore the correct default rather than
a conservative one, and the dead zone implements it exactly.
The paper further proves that per-item label-free adaptation
is impossible under i.i.d. latent coupling, and pre-registers four
falsification criteria, among them the published dev-calibrated
CISC protocol as a designated killer baseline, all of which the
method survived.
Index Terms—large language models, self-consistency, confi-
dence calibration, weighted voting, label-free estimation, rank
statistics
I. Introduction
Self-consistency (sc) [1] improves the reasoning accuracy
of a frozen large language model (LLM) by sampling K
chain-of-thought traces and returning the plurality answer.
Because each trace can also report a confidence score
(verbalized [2], [3], derived from token log-probabilities, or
elicited as P(True) [4]), a natural refinement is to weight
votes by confidence. Confidence-Informed Self-Consistency
(CISC) [5] showed that this recovers the accuracy of plain
sc at a fraction of the sampling budget, and introduced
Within-Question Discrimination (WQD) to argue that
discrimination, not calibration, is the property that makes
a confidence signal useful for voting.
This refinement carries a structural fragility that, to
the author’s knowledge, no published method addresses.
Every existing weighting scheme is monotone increasing in
confidence, including CISC’s softmax weights, reliability-
aware pseudo-counts [6], and warmup-thresholded filtering
[7]. The trust decision is which magnitude of up-weighting
to apply; the possibility that the channel is anti-correlated
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
gate for reasons irrelevant to voting utility [5], [8].
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

<!-- PDF PAGE 2/9 -->
the log-value feature map reproduces CISC-power exactly
(Section IV). Because φ depends on confidence only
through within-item ranks, the entire method is invariant
to every strictly monotone distortion of the confidence
scale; under monotone compression it beats the best
exponent in the tested raw-value grid {0.25, 0.5, 1, 2, 4}
(1.000 vs. 0.965); that grid optimum lies at the largest
exponent tried, so the comparison bounds the grid, not
the whole family.
C2: Label-free estimation of the signed reliability. The
crowdsourcing lineage estimates annotator reliability from
cross-annotator covariance [9], [10]; a single exchange-
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
pled traces as i.i.d. votes. CISC [5] weights votes by
softmax-normalized confidence with a temperature tuned
on a labeled split, and its WQD metric makes the
discrimination-vs-calibration point that also motivates
this work; the rank-calibration line [8] reaches the same
conclusion independently. Weighted variants [11], [12]
and early-stopping families [13], [14] refine the bud-
get; reliability-aware pseudo-counts [6] and warmup-
thresholded filtering [7] adapt online but only re-scale
positive trust. None of these can represent, much less
estimate, a negative confidence–correctness association.
The dev-calibrated variant must therefore be positioned
honestly: CISC’s tuned temperature is already a dev-
calibrated sc↔CISC interpolation, so the novelty of tact-
dev lies in the sign, the rank invariance, and the analytic
(grid-free) map, not in dev calibration itself.
Reliability estimation without labels. Estimating worker
reliability from agreement is classical [9], [15], [16]; spectral
meta-learners [10] and recent LLM ensemble work [17],
[18] exploit covariance across multiple predictors. The
setting here differs: one exchangeable channel from one
model, per-item vote structure, and the known failure
of agreement proxies under correlated errors—met here
with a quantified attenuation identity, conservative de-
attenuation, and alarms in place of an unconditional claim.
Shrinkage and rank statistics. The estimator assem-
bles classical parts: stratified rank statistics [19], the
James–Stein positive-part estimator [20], effective-sample-
size corrections [21], [22], and normal-scores discriminant
analysis. The claim is the assembly and its anchors, not
the parts.
Honest sibling result. A preceding system by the author
(RLEV-VoI, redundancy-discounted voting with value-
of-information stopping) was evaluated under the same
falsification discipline and failed it, dominated everywhere
by a simple deduplication baseline, and is reported as a
negative result. Its post-mortem isolated the confidence
dilemma studied here.
III. Problem Setup
A. Notation
Items q = 1, . . . , Q; item q has mq sampled traces. Trace
(q, i) yields an answer aq,i in a discrete set and a confidence
cq,i ∈(0, 1); correctness is yq,i = 1[aq,i = a∗
q], unobserved
at test time. Plain sc returns arg maxA nq(A) where nq(A)
counts votes for answer A. CISC-power weights votes by
c γ
q,i with a fixed γ > 0.
B. The confidence dilemma
The synthetic oracle draws, per item, traces from a
cluster mixture with a latent correct answer and generates
confidence as
cq,i = clip
  1
2 + κ (yq,i −1
2) + εq,i, 0.01, 0.99

,
(1)
with noise ε ∼N(0, 0.12) and coupling κ ∈[−0.6, 0.6].
Fig. 1 maps the baseline landscape before the proposed
method existed: unconditional weighting (CISC, γ = 1)
collapses on κ < 0; an ECE gate never opens off the well-
calibrated diagonal; a sign-corrected AUC gate over dev
labels nearly saturates the homogeneous sweep. This pre-
measurement fixes where a new method can legitimately

<!-- PDF PAGE 3/9 -->
Fig. 1.
The pre-measured problem statement: accuracy of baseline
confidence policies at fixed K=15 as the true coupling κ varies.
A trivial sign-corrected AUC gate (green) nearly saturates the
homogeneous sweep; the headroom for any new method (shaded)
concentrates in the mid-range and, off this plot, in distortion,
heterogeneity, and label-free cells.
claim wins—monotone distortion of the confidence scale,
covariate heterogeneity, small dev sets, and label-free
operation—and the evaluation holds itself to exactly those
cells.
IV. TACT
A. Vote family
Within item q, let Rq,i be the midrank of cq,i (ties
averaged) and
φq,i = vq,i −¯vq
σq
,
vq,i = Φ−1 Rq,i
mq + 1

,
(2)
where σq is the realized standard deviation of v within the
item (the no-tie value is 0.62 at m=4 but 0.95 at m=40; a
closed form would silently rescale γ across budgets), and
φ ≡0 if σq ≤10−8 (all-tied confidences vote as plain sc).
The vote is
ˆaq = arg max
A
X
i: aq,i=A
exp
 γ φq,i

,
(3)
and when γ = 0 the implementation calls the sc routine
itself, making the zero-trust anchor bitwise exact rather
than equal in distribution. Because (2) depends on c
only through within-item ranks, every strictly monotone
distortion of the confidence scale leaves (3) unchanged.
B. Reliability statistic
For item q with n1
q positive and n0
q negative labels (dev:
y; label-free: the pseudo-label of Section V), the Mann–
Whitney statistic on midranks gives
Dq = 2 AUCq −1,
AUCq =
Uq
n1qn0q
,
(4)
which equals 2 · WQDq −1 in CISC’s notation. Pooling
uses van Elteren pair-count weights Nq = n1
qn0
q [19]:
bD =
P
q NqDq
P
q Nq
.
(5)
Under the within-item exchangeability null, Uq has the
exact tie-corrected variance n1
qn0
q(mq+1)/12·[1−P
t(t3 −
t)/(m3
q−mq)], yielding a null standard error SE0; between-
item heterogeneity is captured by the closed-form delete-
one-item jackknife SEJ. The conservative choice is
SE = max
 SE0, SEJ,
1
2
√
N

,
r = bD/SE.
(6)
Because D is a pairwise functional, E[ bD] does not depend
on mq: an exponent estimated at m=40 transfers to
deployment at m=8.
C. Tempering map
Shrinkage. Positive-part James–Stein with a significance
floor ν:
˜D = sign( bD) max
 0, | bD| −ν2SE2/| bD|

,
(7)
with dead zone {|r| ≤ν}; νdev = 1.28, νLF = 2.33. With
ν = 1, (7) is exactly the empirical-Bayes posterior mean
under a N(0, τ 2) prior with plug-in ˆτ 2 = max(0, bD2−SE2)
[20]. The map is odd, continuous, never exceeds | bD|, and
is monotone in bD and anti-monotone in SE.
Link. Model φ | y ∼N(µy, s2) within item with the
mixture standardized to unit variance, which is what
(2) enforces, so s2 = 1/(1 + ¯p(1 −¯p)u2) where u =
√
2 Φ−1  1+ ˜
D
2

and ¯p is the base rate of correct traces.
The Bayes-optimal per-trace log-weight coeﬀicient is then
γ∗= u
s = u
p
1 + ¯p(1 −¯p) u2,
(8)
capped at γmax (4 dev, 2 label-free). The uncorrected link
γ = u under-weights strong channels by up to ∼50% at
D = 0.9.
D. tact in one expression
Two simplifications collapse the pipeline. Factoring bD
out of (7) makes the shrinkage a multiplicative gain in
the pooled z-statistic ζ = bD/SE alone, and substituting
u =
√
2 z with z = Φ−1  1+ ˜
D
2

into (8) removes the nested
radical. tact is then
ˆaq = arg max
A
X
i: aq,i=A
exp
 γ φq,i

,
γ =
h
z
p
2 + 4¯p(1 −¯p)z2
iγmax
−γmax
,
(9)
z = Φ−1
1
2

1 + bD (1 −ν2/ζ2)+

,
ζ = bD/SE,
(10)
with bD from (5) and φ from (2). At the default ¯p = 1
2 the
exponent is exactly
γ = z
p
2 + z2,
z = Φ−1( [
AUC),
(11)
one probit and one square root. Nothing in it is fitted to
outcomes: ν is a significance level and γmax a clip, both
fixed before any data is seen. The clip is not cosmetic,
though. Where bD saturates it binds, and the vote then sees
γmax rather than the derived magnitude (Section VIII).
The dead zone is now visible as a single condition, |ζ| ≤ν,
on which γ is identically zero and (9) is bitwise sc by

<!-- PDF PAGE 4/9 -->
Proposition 1. Equations (9)–(11) are verified equivalent
to the shipped implementation over randomised inputs
including every boundary (tests/test_formula.py).
E. Anchor properties
Proposition 1 (Exact sc reduction). At γ = 0, (3) equals
plain sc as a function on every trace pool, including tie-
breaks. Under D = 0, P(γ = 0) →2Φ(ν) −1 (80% dev,
98% label-free), and γ is continuous through the dead-
zone boundary, so a false positive applies an infinitesimal
exponent.
Proposition 2 (Exact CISC reduction). With the feature
map φlog
q,i = log cq,i−log cq, the weights equal κq c γ
q,i with a
per-item constant κq > 0; hence the argmax, the ties, and
the normalized vote shares coincide with CISC-power(γ)
on every pool.
Proposition 3 (Regularity). The composite g( bD, SE) is
continuous, odd, nondecreasing in bD, nonincreasing in SE
in magnitude, with g(D, 0+) = γ∗(D).
Proofs are elementary and pinned by unit tests in
the released code (98 tests; the permutation-verified null
variance, the EB identity in (7), and the link derivation
(8) are each tested numerically).
V. Label-Free Estimation
A. Pipeline
(i) Dedup: single-linkage duplicate groups on the
lexical-similarity channel at 0.95; each trace gets weight
1/|group| for plurality determination and pair weighting.
(ii) Pseudo-label: gq,i = 1[aq,i = Mq] with Mq the dedup-
weighted plurality. (iii) Margin gate: keep the top 60% of
items by dedup-weighted margin. (iv) Compute (5) with
lab = g, giving ( bDg, SEg, rg).
B. Sign consistency and its boundary
Proposition 4 (Attenuation identity). Let ¯ρ be the pair-
weighted probability that an item’s plurality is wrong. If
the plurality-error event is independent of φ given y (class-
conditional noise), then E[ bDg] = (1 −2¯ρ) D. In particular
sign E[ bDg] = sign D whenever ¯ρ < 1/2: the label-free
estimate can only under-trust, never mis-sign.
The identity fails when the flip is caused by confidence,
that is, under a confident echo. There the observable law
under {majority right, D < 0} and {majority wrong via
confident echo, D > 0} is identical (the two-root ambiguity
of [10] restated for a single channel), so any label-free
guarantee is necessarily conditional; it is stated as such
rather than papered over.
C. De-attenuation and alarms
Split-half agreement over R=20 random half-splits es-
timates α = p2 + (1 −p)2/k under a one-coin model with
k effective wrong alternatives (inverse-Simpson), inverted
as p = [1 +
p
1 −(k+1)(1 −kα)]/(k+1); bDg is divided
by the upper 95% bootstrap bound of 2p −1 (floored
at 0.2), which can only under-inflate. Four alarms force
γ = 0: duplicate collapse (median Kish ratio < 0.5),
sign-aware margin-decoupling, root ambiguity in the split-
half quadratic, and insuﬀicient gated items. The margin-
decoupling alarm must condition on the estimated trust
direction: a sign-naive version (“plurality has the highest
mean φ”) false-alarms on every benign anti-correlated
channel—a defect the author hit, diagnosed, and fixed, and
which the released tests pin. Finally the significance gate
acts on the raw z (unbiased sign under Proposition 4) and
temper on the de-attenuated value. A semi-label-free mode
takes only the sign from ∼50 dev labels, routing it into
the pipeline and disabling only the proxy-sign alarm; this
purchases immunity to the ambiguity above at negligible
labeling cost.
VI. Heterogeneity: Impossibility and Escape
A. Per-item adaptation is closed under i.i.d. coupling
Suppose κq
iid
∼N(0, 0.62) with no observable covariate.
Proposition 5 (Self-reinforcement). Any per-item rule
γq = h( bDg
q) with h monotone increasing and odd reinforces
the plurality on both branches: bDg
q > 0 up-weights confi-
dent traces, which agree with the plurality; bDg
q < 0 up-
weights unconfident traces, which are again the plurality
side. Empirically such a rule agrees with sc on 97.5% of
items and its residual flips are net-harmful (1 right vs. 9
wrong per 400 items).
Proposition 6 (Winner’s curse). On plurality-wrong items
with |Dq| > 0.3, the items where a flip could win, the
agreement statistic’s sign matches the true sign only 4%
of the time.
Proposition 7 (Two-world unidentifiability). For any ob-
served (a, c), the worlds {κ > 0, minority correct} and
{κ < 0, plurality correct} induce identical observable laws
(constructively, D computed against either truth satisfies
Dw1 = −Dw2). No label-free method can separate them.
Consequently the per-item oracle (0.983 in this harness)
is unreachable, and the honest behaviour is to fall back to
the global estimate, which tact’s dead zone does: in the
i.i.d. cell every variant returns bitwise sc (zero discordant
pairs).
B. TACT-group
Real heterogeneity is typically indexed by an observable
covariate (domain, question type). With κ indexed by a
group label, running the estimator per group keeps every
group inside the operating regime of Sections IV–V; groups
with fewer than 30 dev (or 60 unlabeled) items fall back
to the global estimate, which Propositions 5–7 show is the
only defensible default.

<!-- PDF PAGE 5/9 -->
TABLE I
Coupling sweep (accuracy at K=15; 400 paired items per cell; dev
n=200). Published protocols sit at the sc floor on the entire
negative half-axis.
κ
sc
ECE
devT
SignGrid
tact-dev
tact-LF
oracle
−0.6
.807
.807
.807
1.000
1.000
1.000
1.000
−0.4
.797
.797
.797
1.000
1.000
1.000
1.000
−0.2
.835
.835
.835
.993
.978
.978
.993
−0.1
.762
.762
.762
.892
.880
.885
.892
0.0
.835
.835
.835
.835
.835
.835
.835
+0.1
.795
.795
.917
.917
.902
.902
.917
+0.2
.845
.845
.993
.993
.988
.988
.993
+0.4
.838
.838
1.000
1.000
1.000
1.000
1.000
+0.6
.782
.782
1.000
1.000
1.000
1.000
1.000
VII. Experimental Setup
Harness. A cluster-mixture oracle generates, per item,
up to Kmax=20 cached traces with answers, confidences
(1), and two similarity channels; all methods replay iden-
tical pools (paired comparisons, exact McNemar tests).
Voting budget K=15; 400 items per cell on the sweep,
600 for the group study; dev splits of 200 (primary) and
50 (small-dev).
Regimes. The κ sweep {−0.6, . . . , +0.6}; three strictly
monotone confidence distortions (compression toward 0.5,
over-confident sigmoid, fourth power), rank-preserving by
construction, so discrimination is intact while calibra-
tion is destroyed; i.i.d. heterogeneity (κq ∼N(0, 0.62));
covariate-structured
heterogeneity
(three
groups
at
+0.6/0/ −0.6); and a confident-echo poison (a wrong
cluster echoes verbatim with confidence 0.95).
Baselines. sc; CISC-power with γ ∈{0.25, . . . , 4}; CISC-
devT, the published dev-calibrated protocol (positive grid
picked on dev); a binary ECE gate; SignGrid-dev, the
strongest trivial baseline (signed exponent grid picked on
dev); and the test-set oracle over signed fixed exponents
as the upper envelope. The group study adds the naive
self-referential per-item method as a negative control and
the per-item link oracle as the ceiling.
Pre-registered falsifiers. F1: tact-dev significantly below
the best fixed-γ CISC at κ=+0.6. F2: either variant
significantly below sc anywhere on the sweep. F3: the
label-free variant fails to beat the ECE gate on sweep
average. F4: CISC-devT or SignGrid-dev matches tact-
dev everywhere, including the distortion, heterogeneity,
and small-dev cells.
VIII. Results
A. Signed recovery, with and without labels
Table I and Fig. 2 give the sweep. Three observations.
First, the published protocols never leave the floor on
κ < 0: CISC-devT’s grid is positive-only and the ECE
gate never opens (dev ECE ranges 0.10–0.80 across the
sweep while the signal’s discrimination is perfect at the
extremes). Second, the label-free variant matches the 200-
label variant nearly point-for-point—at κ=−0.6 the raw
Fig. 2.
Main result on the confidence-usage frontier. tact-dev and
the fully label-free tact-LF track the signed oracle across the sweep;
CISC-devT and the ECE gate sit at the sc floor for all κ < 0.
TABLE II
Adversarial regimes (accuracy at K=15). “Oracle” is the test-set
best over raw-value weight policies; rank invariance beats that
entire family under compression.
Regime
sc
devT
SignGrid
tact-dev
tact-LF
Monotone compress
.795
.965
.965
1.000
1.000
Monotone overconf
.795
1.000
1.000
1.000
1.000
Monotone power
.795
1.000
1.000
1.000
1.000
Hetero (i.i.d.)
.810
.810
.810
.810
.810
Confident echo
.200
.200
.550
.585
.200†
†alarm fires and the method refuses to leave sc—the conditional
guarantee of Prop. 4 working as stated.
agreement statistic is bDg = −0.81 with z = −17.6, and the
CCN identity’s sign guarantee holds as predicted, yielding
1.000 with zero labels. Third, at κ = 0 the dead zone
returns γ = 0 exactly, so the paired accuracy difference
to sc is identically zero—“non-inferior” is replaced by
“identical.”
Where the derived exponent actually operates. The
four cells that carry the headline 1.000 (κ = ±0.4, ±0.6)
are cells where bD saturates at ±1, so the link returns
γ∗≈±38 and the cap γmax is what the vote sees; the
derived magnitude is not doing the work there, the sign
is. Conversely, at κ = ±0.1, ±0.2, where the derived
value lands strictly inside the cap (±1.06 to ±2.80), tact-
dev trails the dev-picked signed grid on all four cells
(0.880 vs. 0.892; 0.902 vs. 0.917; 0.978 vs. 0.993; 0.988
vs. 0.993). Read together: against the published protocols
the advantage is large and comes from representing the
sign at all, whereas against a signed grid the analytic map
is not better at choosing a magnitude on these cells. Its
advantage over the grid is elsewhere, in the three cells
named in C4, and the one place the interpolation itself
pays is confident echo, where γ = −1.198 falls between
grid points and beats the grid optimum γ = −1 (0.585 vs.
0.550).

<!-- PDF PAGE 6/9 -->
Fig. 3.
Adversarial regimes. Dotted line: the oracle over raw-value
weights. Left group of bars: rank invariance beats that family under
compression; right: the labeled variant counters the confident echo
while the label-free variant alarms and refuses.
B. Rank invariance where raw values fail
Under monotone compression (Table II, Fig. 3) all
confidences huddle near 0.5, so every cγ-family weight
is nearly uniform: even the oracle over raw-value policies
reaches only 0.965. tact’s rank scores are untouched by the
distortion and both variants reach 1.000. Under the confi-
dent echo, dev labels reveal the inversion (high confidence
⇒wrong) and tact-dev counters with γ = −1.20, the best
result in the field (0.585; three times the sc floor); label-
free, the duplicate-collapse alarm fires and the method
correctly refuses—by Proposition 7 no label-free method
could do better than a coin flip on the sign here, and
pretending otherwise would be the real failure.
C. Heterogeneity
Table III and Fig. 4 give the group study. In the
covariate-structured cell, per-group tact recovers each
group’s signed coupling (dev {+4.0, 0.0, −4.0}, label-free
{+2.0, 0.0, −2.0}, the κ=0 group correctly dead-zoned—
and cracks the floor that provably binds every global
policy: the label-free variant reaches 0.940, within 0.007 of
the per-item link oracle, with zero paired losses to sc over
600 items (+79/−0, p = 3.3×10−24). In the i.i.d. cell every
legitimate method sits at the floor with zero discordant
pairs, and the naive self-referential control lands slightly
below it—the empirical face of Propositions 5–7. One
observation is reported as-is rather than tuned for: the
label-free variant outperforms the dev variant in the
grouped cell (0.940 vs. 0.923) because its lower exponent
cap (2 vs. 4) regularizes better when |D| ≈1; cap
robustness is left as an ablation.
D. Small dev sets and falsifiers
With dev n=50 the conclusions are unchanged (1.000 at
|κ|=0.6; 0.978 at −0.2): the SE-aware shrinkage degrades
smoothly rather than catastrophically. All four falsifiers
survived: F1 (1.000 vs. 1.000), F2 (bit-identical at κ=0;
never significantly below sc elsewhere), F3 (sweep means
0.954 vs. 0.811), and F4 (the distortion and echo cells are
TABLE III
Heterogeneity study (600 paired items; K=15).
Method
Grouped
i.i.d.
sc (floor)
.808
.827
tact global (dev)
.808
.827
tact-group (dev)
.923
.827
tact-group (label-free)
.940
.827
Naive per-item (neg. control)
.803
.820
Per-item link oracle (ceiling)
.947
.983
Fig. 4. Structured vs. i.i.d. heterogeneity. Left: with an observable
covariate, per-group tact (label-free) approaches the per-item oracle
from the 0.808 floor with zero losses to sc. Right: the provably closed
i.i.d. cell—every legitimate method at the floor; the negative control
slightly below it.
unreachable by either grid baseline). Against SignGrid-
dev the honest margin is narrow on the homogeneous
sweep—tact even trails by 0.005–0.015 in the mid-range,
the deliberate cost of shrinkage—and the net advan-
tage concentrates exactly where pre-registered: distortion
(+0.035), echo (+0.035), and label-free operation, which
no grid can perform.
E. Verification of the implementation
Because every claim in Sections IV–VI is a mathemat-
ical property rather than an empirical trend, the released
code pins each one with an executable test; the suite is
98 tests covering tact and the follow-on work, and runs in
82 seconds. Table IV maps propositions to the tests that
would fail if they stopped holding.
Two
entries
deserve
comment.
The
permutation-
invariance test was added after a defect in which the
memoisation key made the test pass while the estimator
itself was order-dependent by up to 0.10; it now calls
the internal routine directly. And the last two rows are
counter-tests that assert failure of rejected alternatives —
the Kish effective-sample-size formulation and the claim
that the shipped default honours the SAFE stopping
guarantee — so that neither can be silently reinstated
by a later change.
F. Real-trace validation
Validation on real traces used Claude Haiku 4.5 as
the frozen model: 100 items (50 GSM8K [23], 50 Com-
monsenseQA), 12 independent chain-of-thought traces
per item with verbalized confidence (1,200 traces total),

<!-- PDF PAGE 7/9 -->
TABLE IV
What the test suite verifies. Every proposition in the paper has an
executable counterpart; the counter-tests fail deliberately on
rejected alternatives so a regression cannot silently reinstate them.
Claim
Test
Evidence
Prop. 1 (exact sc)
gamma_zero_is_
bit-
wise_sc
200 random pools,
identical incl. ties
Dead-zone rate
dead_zone_
probabil-
ity
>70%
under
D=0, 300 trials
Prop.
2
(exact
CISC)
logval_phi_
reproduces_cisc
identical
vote
shares, 100 pools
Rank invariance
monotone_ invariance
3
distortions
×
100 pools
Null variance
null_variance_
matches_permutation
3,000-draw
permutation,
10% tol.
JS–EB identity
js_eb_identity
exact to 10−12
Link (8)
link_values_and_
mixture_correction
closed
form,
rel.
10−9
Prop.
4
(attenua-
tion)
poisoning_
attenuation_linear
ρ
∈
{.1, .25, .4},
abs. .06
Props. 5–7
test_tact_group.py
97.5%
sc
agreement;
4%
sign match
Estimator
permutation-
invariance
estimator_is_
permu-
tation_invariant
bypasses
the
memo (regression
test)
Rejected: Kish ESS
kish_fails_T2_T3
asserts the failure
Rejected:
SAFE
guarantee
under
VoI
frozen_default_
breaks_guarantee
asserts the viola-
tion
evaluated at K=12 with a 40/60 dev/test split. Four
findings.
(a) The calibration–discrimination distinction reverses
on real data, and tact reads it correctly. The channel is
extremely well calibrated in the usual sense: ECE = 0.016,
far inside the 0.10 gate, so a binary ECE gate opens and
hands the channel to CISC. Yet the measured within-
item discrimination is bD = −0.219 with SE = 0.176 (z =
−1.24): no usable signal, and what little there is points
the wrong way (math −0.515, commonsense −0.173; both
groups negative). This is the exact mirror image of the
synthetic case in which ECE wrongly closed the gate on
a discriminative channel (Section III): on real traces ECE
wrongly opens it on a non-discriminative one. Calibration
is uninformative about voting utility in both directions,
and a signed discrimination statistic is what distinguishes
them.
(b) The dead zone fires, and costs exactly nothing. With
|z| < ν, tact-dev, tact-LF and tact-group all return γ = 0
and are bit-identical to sc on every test item (+0/ −0
discordant pairs, p = 1). All methods score 0.917. This is
the pre-registered null-direction prediction of Section IX
confirmed on real data: where the channel carries no signal,
the method is free.
(c) Saturation is the binding constraint, not the estima-
tor. Trace-level accuracy is 0.958 on GSM8K and 0.847 on
CommonsenseQA, so only 12 of 100 items contain both a
correct and an incorrect trace, the only items a within-item
rank statistic can use. The estimator is not underpowered
by design; the benchmark simply does not present the
model with enough genuine uncertainty. Exposing non-
null coupling on a strong model requires harder item pools,
not more traces per item.
(d) Verbalized confidence is tie-heavy. Two values (0.99,
0.95) account for 49% of all reports, activating the tie-safe
degeneration path of (2) on many items.
Scope of this first campaign: one model, two bench-
marks, K=12. It confirms the null-direction prediction
and the calibration–discrimination argument, and it is not
evidence that tact improves accuracy, since the channel
carried no signal to exploit. Finding (c) predicts what to
do about that, and Section VIII-G does it.
G. Confirmatory campaign on harder items
Finding (c) predicts that a channel measured as null on
saturated benchmarks should become measurable on items
the model finds genuinely uncertain. A pre-registered
follow-up tests that prediction: 119 MATH level-5 prob-
lems [24], [25], 16 traces each from the same frozen model,
a 30-item sign set and an 89-item evaluation set drawn
from the registered list before any trace was collected, and
five hypotheses (H1–H5) fixed in advance.
The channel is real. On the evaluation set the pooled
statistic is bD = +0.250 with SE = 0.098, so z = +2.54 and
H1 passes. This is the first real-trace evidence that verbal-
ized confidence carries positive within-item discrimination;
the same measurement on GSM8K/CommonsenseQA gave
−0.219 (z = −1.24).
The endpoint was unpassable for any method. The
realized substrate saturated again: per-trace accuracy
0.819, sc 0.888, a decisive stratum of 10 of 89 items, and
the correct answer present in the pool on only 4 of those.
The in-pool oracle therefore tops out at +4/−0, exact one-
sided p = 0.0625. H2 fails, but it fails for every conceivable
aggregation method including a perfect one, so the failure
is a property of the substrate rather than of the estimator.
Abstention behaved as designed. tact returned γ = 0,
with alarms E4 and E2 firing on the label-free path and
the sign set holding too few informative items to supply a
semi-label-free sign. The vote is therefore bit-identical to
sc at 0.888 (H3, H4 pass). The cost of acting anyway is
visible in the same table: best-single-confidence, the trivial
baseline that always trusts the channel, loses 4.5 points
at 0.843.
One caveat from this campaign transfers beyond tact.
Measured diﬀiculty depended on the collection protocol:
a 30-problem-per-call probe put level-5 plurality accuracy
at 0.40, while the 15-problem-per-call confirmatory run
yielded 0.888 on the same stratum. Batch size belongs in
the experimental record whenever traces are collected in
batches.
H. How wide is the addressable stratum?
Both campaigns failed their endpoint for the same
reason, which suggests measuring that reason directly.

<!-- PDF PAGE 8/9 -->
TABLE V
Confirmatory campaign, MATH level-5 evaluation set (89 items,
K=16). Every method replays the same cached pools. The
duplication channel is inert because no reasoning text was
collected, so dedup-sc coincides with sc by construction.
Method
Accuracy
net vs. sc
sc / dedup-sc / CISC-linear
0.888
—
tact-LF
0.888
+0/ −0
tact-semi-LF
0.888
+0/ −0
best-single-confidence
0.843
+1/ −5
in-pool oracle (ceiling)
0.933
+4/ −0
TABLE VI
The addressable stratum across substrates. Rows marked † are
measured here; HumanEval+/MBPP+ is recomputed from
published oracle-minus- selector tables. As items harden they pass
from saturated to capability-limited without the window widening.
Domain
Substrate
Window
QA, label-free
GSM8K / CommonsenseQA†
12% informative, 9% decisive
QA, label-free
MATH level-5†
11% decisive, 4% rescuable
QA, label-free
AIME / AMC†
23% decisive, 3% rescuable
Code, executable
HumanEval+ / MBPP+
3.56%
Code, executable
LeetCode Med/Hard†
7.5%
Define the window as the fraction of items where the
plurality is wrong and the correct answer is present in the
pool: the ceiling for any label-free aggregation method,
since nothing outside it can be changed.
The window was measured on five substrates spanning
two domains (Table VI). For code generation, where an
executable test suite supplies per-sample ground truth and
the window might reasonably be expected to widen, 40
LeetCode Medium/Hard problems [26] were solved 8 times
each and graded against the benchmark’s hidden suites,
with the baseline taken as the largest behavioural cluster
over probe inputs (never expected outputs). The window
is 3/40 = 7.5% (CI95 2.6–19.9%): wider than label-free
QA, but the same order, and the composition is the same
shape at 30 saturated, 7 capability wall and 3 rescuable,
i.e. 75/17.5/7.5%. Nor does budget open it. The seven
capability-wall problems produced zero correct solutions
in 224 further attempts (per-problem 95% upper bound on
the pass rate 0.088), and extrapolating oracle@N shows
the window saturating by N=32.
One precaution belongs with these numbers, because
omitting it would have inverted them. The grading harness
was validated against the benchmark’s own reference
solutions before any candidate was scored: 178 of 180 pass
under the sandbox’s resource limits. An earlier version of
the same harness failed 100% of executions because the
host rejects one of the requested limits outright, and that
condition presents as a candidate failure rather than as
an error. Studies that grade by execution should report
their reference-solution pass rate for the same reason a
calibration curve is reported: without it, a broken harness
and a capability wall look identical.
IX. Discussion and Limitations
What the evidence does and does not show. The
accuracy claims are all on a synthetic oracle whose
confidence model (1) is, at the homogeneous cells, the very
coupling the estimator measures. Three design choices
limit the circularity: the adversarial regimes (distortions,
heterogeneity, echo) lie outside the estimator’s working
model; mechanism-recovery claims (does bD track κ?) are
reported separately from accuracy claims; and the pre-
measured baseline landscape (Fig. 1) fixed the winnable
cells before the method existed. The real-trace campaigns
of Sections VIII-F and VIII-G test the premise and
the abstention behaviour, and both predictions held: the
channel is null on saturated benchmarks and positive on
competition mathematics, and the dead zone kept the
vote bit-identical to sc in each case. They do not test
the accuracy claim, because on neither substrate was
the addressable stratum large enough for any method to
demonstrate a gain (Section VIII-H).
Narrow margins where labels abound. When labels are
plentiful and the confidence scale is trusted, a dev-picked
signed grid captures most of the value; tact’s case rests
on the label-free setting, distorted scales, small dev sets,
and the exactness of its anchors.
Conditional label-free guarantee, and what happens
past the boundary. Proposition 4 requires ¯ρ
<
1/2
after deduplication, and the confident-echo ambiguity is
fundamental (Proposition 7). Follow-on work measured
the consequence of crossing that boundary, and it is
worse than under-trust. In a paraphrased wrong-majority
cell (a dominant wrong cluster that is semantically tight
but carries no verbatim signature, so deduplication has
nothing to collapse) the plurality is wrong on most items,
¯ρ > 1/2, and tact-LF does not merely shrink toward
sc: it mis-signs, saturates at γ = −2.0, and scores 0.000
against an sc floor of 0.340. None of the four alarms fires,
because E1 keys on verbatim duplication which is absent
by construction. This is the method’s sharpest unguarded
failure mode: the guarantee is conditional, the condition
is not observable label-free, and the existing diagnostics
do not detect its violation. Where a systematically wrong
majority is plausible, the semi-label-free mode (sign from
∼50 labels) should be the default rather than an optional
refinement.
Global exponent per group. Within a group, tact ships
one exponent; per-item variation inside a group is un-
exploitable by Propositions 5–7 unless further covariates
exist.
The thin window. Section VIII-H measures the stratum
this whole family of methods can act on at 3–7.5% of
items on every substrate tried, in two domains, with
no widening as items harden: they pass from saturated
straight to capability-limited. Two consequences follow
for the method proposed here. First, abstention is not
a conservative compromise but the only correct default,

<!-- PDF PAGE 9/9 -->
and the measured cost of acting anyway was negative
on both real substrates (best-single-confidence loses 4.5
points in Table V where the dead zone holds tact at the sc
floor). Second, an aggregation gain of the size reported on
the synthetic harness is not measurable on a benchmark
of a few hundred items at these window widths, which
is why the real-trace claim in this paper is confined to
the premise (the channel exists and is signed) and to the
abstention behaviour, and does not extend to accuracy.
Demonstrating the gain needs a (model, benchmark) pair
whose plurality is wrong on 30–60% of items with the
correct answer still reachable, and no pair tried here
satisfies both.
X. Conclusion
tact turns “how much should this model’s confidence
be trusted?” into a measured, signed, uncertainty-aware
quantity with an exact fallback at one end, plain self-
consistency whenever the evidence is absent, and an exact
correspondence to CISC-power at the other under the
log-value feature map (the shipped default uses van der
Waerden scores, so that correspondence is a property
of the family, not of the shipped configuration), and
shows that the sign, long unrepresentable in this family of
methods, can be recovered without any labels under stated
and tested conditions. The accompanying impossibility
results draw the boundary that any future per-item
method must respect, and the falsification protocol, having
already killed one of the author’s own systems, is offered
as the more portable contribution.
References
[1] X. Wang, J. Wei, D. Schuurmans, Q. Le, E. Chi, S. Narang,
A. Chowdhery, and D. Zhou, “Self-consistency improves chain
of thought reasoning in language models,” in Proc. ICLR, 2023.
https://arxiv.org/pdf/2203.11171
[2] K. Tian et al., “Just ask for calibration: Strategies for elic-
iting calibrated confidence scores from language models fine-
tuned with human feedback,” in Proc. EMNLP, 2023. https:
//aclanthology.org/2023.emnlp-main.330.pdf
[3] M. Xiong et al., “Can LLMs express their uncertainty? An
empirical evaluation of confidence elicitation in LLMs,” in Proc.
ICLR, 2024. https://openreview.net/pdf?id=gjeQKFxFpZ
[4] S. Kadavath et al., “Language models (mostly) know what
they know,” arXiv:2207.05221, 2022. https://arxiv.org/pdf/
2207.05221
[5] A. Taubenfeld et al., “Confidence improves self-consistency in
LLMs,” in Findings of ACL, 2025, arXiv:2502.06233. https://
aclanthology.org/2025.findings-acl.1030.pdf
[6] J. Kim, N. Yang, K. Min, and K. Jung, “Reliability-aware
adaptive self-consistency for eﬀicient sampling in LLM rea-
soning,” in Findings of ACL, 2026, pp. 21575–21590. https:
//aclanthology.org/2026.findings-acl.1085.pdf
[7] Y. Fu et al., “Deep think with confidence,” arXiv:2508.15260,
2025. https://arxiv.org/pdf/2508.15260
[8] X. Huang, S. Li, M. Yu, M. Sesia, H. Hassani, I. Lee, O. Bastani,
and E. Dobriban, “Uncertainty in language models: Assessment
through rank-calibration,” in Proc. EMNLP, 2024, pp. 284–312.
https://aclanthology.org/2024.emnlp-main.18.pdf
[9] A. P. Dawid and A. M. Skene, “Maximum likelihood estimation
of observer error-rates using the EM algorithm,” J. Roy. Statist.
Soc. C, vol. 28, no. 1, pp. 20–28, 1979. https://doi.org/10.2307/
2346806
[10] F. Parisi, F. Strino, B. Nadler, and Y. Kluger, “Ranking
and combining multiple predictors without labeled data,”
Proc. Natl. Acad. Sci., vol. 111, no. 4, pp. 1253–1258, 2014.
https://pmc.ncbi.nlm.nih.gov/articles/PMC3910607/pdf/
pnas.201219097.pdf
[11] Y. Li et al., “Making language models better reasoners with
step-aware verifier,” in Proc. ACL, 2023. https://aclanthology.
org/2023.acl-long.291.pdf
[12] Z.
Kang,
X.
Zhao,
and
D.
Song,
“Scalable
best-
of-N
selection
for
large
language
models
via
self-
certainty,”
in
Proc.
NeurIPS,
2025,
arXiv:2502.18581.
https://proceedings.neurips.cc/paper_files/paper/2025/file/
1c7eff166a8e345f664f0faa8f4e4d2e-Paper-Conference.pdf
[13] P. Aggarwal, A. Madaan, Y. Yang, and Mausam, “Let’s sample
step by step: Adaptive-consistency for eﬀicient reasoning and
coding with LLMs,” in Proc. EMNLP, 2023, pp. 12375–12396.
https://aclanthology.org/2023.emnlp-main.761.pdf
[14] Y.
Li
et
al.,
“Escape
sky-high
cost:
Early-stopping self-
consistency for multi-step reasoning,” in Proc. ICLR, 2024.
https://arxiv.org/pdf/2401.10480
[15] J.
Whitehill
et
al.,
“Whose
vote
should
count
more:
Optimal
integration
of
labels
from
labelers
of
unknown
expertise,”
in
Proc.
NeurIPS,
2009.
https://proceedings.neurips.cc/paper_files/paper/2009/file/
f899139df5e1059396431415e770c6dd-Paper.pdf
[16] D.
R.
Karger,
S.
Oh,
and
D.
Shah,
“Iterative
learn-
ing for reliable crowdsourcing systems,” in Proc. NeurIPS,
2011. https://proceedings.neurips.cc/paper_files/paper/2011/
file/c667d53acd899a97a85de0c201ba99be-Paper.pdf
[17] J. Lee, V. Ma, S. Zhao, Y. Nair, A. Spector, R. Cohen, and E. J.
Candès, “FUSE: Ensembling verifiers with zero labeled data,”
arXiv:2604.18547, 2026. https://arxiv.org/pdf/2604.18547
[18] R. Ai, Y. Pan, D. Simchi-Levi, M. Tambe, and H. Xu, “Beyond
majority voting: LLM aggregation by leveraging higher-order
information,” arXiv:2510.01499, 2025, accepted to ICML 2026.
https://arxiv.org/pdf/2510.01499
[19] P. van Elteren, “On the combination of independent two-sample
tests of Wilcoxon,” Bull. Int. Statist. Inst., vol. 37, pp. 351–361,
1960. https://catalog.hathitrust.org/Record/008896012
[20] W. James and C. Stein, “Estimation with quadratic loss,”
in Proc. 4th Berkeley Symp. Math. Statist. Prob., 1961,
pp. 361–379. https://digitalassets.lib.berkeley.edu/math/ucb/
text/math_s4_v1_article-19.pdf
[21] L.
Kish,
Survey
Sampling.
New
York,
NY,
USA:
Wiley,
1965.
https://www.wiley.com/en-us/Survey+
Sampling-p-9780471109495
[22] J. N. K. Rao and A. J. Scott, “The analysis of categorical data
from complex sample surveys,” J. Amer. Statist. Assoc., vol. 76,
no. 374, pp. 221–230, 1981. https://doi.org/10.1080/01621459.
1981.10477633
[23] K. Cobbe et al., “Training verifiers to solve math word prob-
lems,” arXiv:2110.14168, 2021.
[24] D.
Hendrycks
et
al.,
“Measuring
mathematical
problem
solving
with
the
MATH
dataset,”
in
Proc.
NeurIPS
Datasets
and
Benchmarks,
2021.
https:
//datasets-benchmarks-proceedings.neurips.cc/paper/2021/
file/be83ab3ecd0db773eb2dc1b0a17836a1-Paper-round2.pdf
[25] H. Lightman et al., “Let’s verify step by step,” in Proc. ICLR,
2024. (MATH-500 test subset.)
[26] Y. Xia et al., “LeetCodeDataset: A temporal dataset for
robust
evaluation
and
eﬀicient
training
of
code
LLMs,”
arXiv:2504.14655, 2025. https://arxiv.org/pdf/2504.14655
