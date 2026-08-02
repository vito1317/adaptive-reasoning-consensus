IEEEtran
amsmath,amssymb,amsthm
graphicx
booktabs
multirow
url
subfig
balance
propositionProposition
remarkRemark
D
sign
sc
tact
="[/System/Library/Fonts/Supplemental/Arial Unicode.ttf]" at 10pt
document
TACT: Trust-Anchored Confidence Tempering for\\ Self-Consistency Voting in Large Language Models
Wei-Chen Ko ( 柯瑋宸, vito1317)
Independent Researcher
abstract
Confidence-weighted self-consistency (CISC and its successors) improves on majority voting when a frozen large language model's self-reported confidence is calibrated in direction. Every published weighting scheme is structurally monotone increasing in confidence, so an anti-correlated channel poisons the vote instead of informing it, while binary dev-set gates survive inversion only by discarding genuinely discriminative signal. This paper presents (Trust-Anchored Confidence Tempering), which replaces the fixed confidence exponent with one derived from the measured, signed, within-item discrimination of the channel: a pooled van~Elteren Somers' rank statistic with an item-clustered standard error, passed through positive-part James--Stein shrinkage and a Bayes-discriminant link. Written out, the method is a single expression whose exponent reduces to with the probit of the shrunk pooled AUC, and it carries exact anchors: inside the shrinkage dead zone the vote is bit-identical to plain self-consistency, and a log-value feature map reproduces CISC-power. A label-free variant estimates the signed reliability from agreement pseudo-labels under a proven attenuation identity that guarantees sign consistency whenever the plurality-error rate is below one half, with conservative de-attenuation and echo alarms at the identifiability boundary. On a synthetic-oracle harness with paired trace pools, the label-free variant recovers anti-correlated channels that pin every published protocol to the majority-vote floor (: vs.\ ), rank invariance beats the oracle over the entire raw-value weight family under monotone confidence compression ( vs.\ ), and a per-group extension cracks the heterogeneity floor with zero paired losses to self-consistency ( vs.\ ; , ). Two real-trace campaigns on a frozen model confirm the premise and locate the binding constraint: within-item discrimination is positive on competition mathematics (pooled , ), yet the stratum on which any such method can act, where the plurality is wrong and the correct answer is present in the pool, measures -- of items across five substrates in two domains, code generation with executable ground truth included. Abstention is therefore the correct default rather than a conservative one, and the dead zone implements it exactly. The paper further proves that per-item label-free adaptation is impossible under i.i.d.\ latent coupling, and pre-registers four falsification criteria, among them the published dev-calibrated CISC protocol as a designated killer baseline, all of which the method survived.
abstract
IEEEkeywords
large language models, self-consistency, confidence calibration, weighted voting, label-free estimation, rank statistics
IEEEkeywords
## Introduction
Self-consistency () wang2023selfconsistency improves the reasoning accuracy of a frozen large language model (LLM) by sampling chain-of-thought traces and returning the plurality answer. Because each trace can also report a confidence score (verbalized tian2023just,xiong2024can, derived from token log-probabilities, or elicited as kadavath2022language), a natural refinement is to weight votes by confidence. Confidence-Informed Self-Consistency (CISC) taubenfeld2025cisc showed that this recovers the accuracy of plain at a fraction of the sampling budget, and introduced Within-Question Discrimination (WQD) to argue that discrimination, not calibration, is the property that makes a confidence signal useful for voting.
This refinement carries a structural fragility that, to the author's knowledge, no published method addresses. Every existing weighting scheme is monotone increasing in confidence, including CISC's softmax weights, reliability-aware pseudo-counts reasc2026, and warmup-thresholded filtering deepconf2025. The trust decision is which magnitude of up-weighting to apply; the possibility that the channel is anti-correlated with correctness is not representable. Yet miscalibration of direction is not exotic: reinforcement fine-tuning is known to distort verbalized confidence, distribution shift can invert a signal that was informative in-domain, and in the experiments reported here a simple anti-correlated channel (; Section~sec:setup) drives confidence-weighted baselines from near-perfect accuracy to far below the majority-vote floor, while the same evidence, read with the correct sign, is a perfect signal. The defensive alternative, a binary dev-set gate that disables the channel when calibration error is high, survives the inversion but discards discriminative signal wholesale: a systematically under-confident yet perfectly ranked channel fails an ECE gate for reasons irrelevant to voting utility taubenfeld2025cisc,huang2024rankcalibration.
This paper frames the problem as estimating one scalar: the signed within-item discrimination of the confidence channel, and mapping that scalar, with its uncertainty, to a vote exponent. The contributions are:
C1: Signed, analytically-tempered confidence weighting. votes with weights , where is the standardized van der Waerden score of trace 's within-item confidence midrank, and is derived, not grid-searched: a pooled van~Elteren Somers' statistic (equal to ) with an exact tie-corrected null variance and an item-clustered jackknife standard error, shrunk by positive-part James--Stein with a significance floor, then mapped through a Bayes-discriminant link with a mixture-variance correction. The construction carries exact anchors: inside the shrinkage dead zone the vote is bit-identical to plain (a shared code path), and the log-value feature map reproduces CISC-power exactly (Section~sec:method). Because depends on confidence only through within-item ranks, the entire method is invariant to every strictly monotone distortion of the confidence scale; under monotone compression it beats the oracle over the whole raw-value weight family ( vs.\ ).
C2: Label-free estimation of the signed reliability. The crowdsourcing lineage estimates annotator reliability from cross-annotator covariance dawid1979maximum,parisi2014ranking; a single exchangeable confidence channel from one model offers no such structure. The signed discrimination is estimated from agreement pseudo-labels (deduplication-weighted plurality per item) with a proven class-conditional-noise attenuation identity, : the label-free estimate can only under-trust, never mis-sign, whenever the pair-weighted plurality-error rate is below . A split-half agreement inversion de-attenuates conservatively, and sign-aware alarms return the method to plain when identifiability is threatened. On the coupling sweep the label-free variant matches the 200-label variant nearly point-for-point, including full recovery of negative channels (Section~sec:results).
C3: An impossibility result and its structured escape. When the per-item coupling is i.i.d.\ with no observable covariate, per-item label-free adaptation is shown to be closed: any monotone use of an item's own agreement statistic collapses to plurality reinforcement; on exactly the plurality-wrong items where a flip could help, the observable sign opposes the truth of the time; and the two hypotheses and induce identical observable laws. When heterogeneity is instead indexed by an observable covariate (domain-dependent calibration), running the same estimator per group recovers each group's signed coupling and approaches the per-item oracle with zero paired losses to (Section~sec:hetero).
C4: A pre-registered falsification protocol. Four falsifiers were fixed before implementation, including the two designed to kill the method: the published dev-calibrated CISC protocol (whose tuned temperature already interpolates ) and a trivial dev-picked signed exponent grid. All four survived, and the honest margins are reported: against the signed grid the net advantage concentrates in three cells: monotone distortion, confident echo, and label-free operation, which no grid can perform.
## Related Work
sec:related
Confidence-weighted self-consistency. wang2023selfconsistency treats sampled traces as i.i.d.\ votes. CISC taubenfeld2025cisc weights votes by softmax-normalized confidence with a temperature tuned on a labeled split, and its WQD metric makes the discrimination-vs-calibration point that also motivates this work; the rank-calibration line huang2024rankcalibration reaches the same conclusion independently. Weighted variants li2023diverse,borda2025 and early-stopping families aggarwal2023adaptive,li2024escape refine the budget; reliability-aware pseudo-counts reasc2026 and warmup-thresholded filtering deepconf2025 adapt online but only re-scale positive trust. None of these can represent, much less estimate, a negative confidence--correctness association. The dev-calibrated variant must therefore be positioned honestly: CISC's tuned temperature is already a dev-calibrated interpolation, so the novelty of -dev lies in the sign, the rank invariance, and the analytic (grid-free) map, not in dev calibration itself.
Reliability estimation without labels. Estimating worker reliability from agreement is classical dawid1979maximum,whitehill2009whose,karger2011iterative; spectral meta-learners parisi2014ranking and recent LLM ensemble work fuse2026,beyondmajority2025 exploit covariance across multiple predictors. The setting here differs: one exchangeable channel from one model, per-item vote structure, and the known failure of agreement proxies under correlated errors---met here with a quantified attenuation identity, conservative de-attenuation, and alarms in place of an unconditional claim.
Shrinkage and rank statistics. The estimator assembles classical parts: stratified rank statistics vanelteren1960, the James--Stein positive-part estimator james1961estimation, effective-sample-size corrections kish1965,rao1981analysis, and normal-scores discriminant analysis. The claim is the assembly and its anchors, not the parts.
Honest sibling result. A preceding system by the author (RLEV-VoI, redundancy-discounted voting with value-of-information stopping) was evaluated under the same falsification discipline and failed it, dominated everywhere by a simple deduplication baseline, and is reported as a negative result. Its post-mortem isolated the confidence dilemma studied here.
## Problem Setup
sec:setup
### Notation
Items ; item has sampled traces. Trace yields an answer in a discrete set and a confidence ; correctness is , unobserved at test time. Plain returns where counts votes for answer . CISC-power weights votes by with a fixed .
### The confidence dilemma
The synthetic oracle draws, per item, traces from a cluster mixture with a latent correct answer and generates confidence as
with noise and coupling . Fig.~fig:baselines maps the baseline landscape before the proposed method existed: unconditional weighting (CISC, ) collapses on ; an ECE gate never opens off the well-calibrated diagonal; a sign-corrected AUC gate over dev labels nearly saturates the homogeneous sweep. This pre-measurement fixes where a new method can legitimately claim wins---monotone distortion of the confidence scale, covariate heterogeneity, small dev sets, and label-free operation---and the evaluation holds itself to exactly those cells.
## TACT
sec:method
### Vote family
Within item , let be the midrank of (ties averaged) and
where is the realized standard deviation of within the item (the no-tie value is at but at ; a closed form would silently rescale across budgets), and if (all-tied confidences vote as plain ). The vote is
and when the implementation calls the routine itself, making the zero-trust anchor bitwise exact rather than equal in distribution. Because eq:vdw depends on only through within-item ranks, every strictly monotone distortion of the confidence scale leaves eq:vote unchanged.
### Reliability statistic
For item with positive and negative labels (dev: ; label-free: the pseudo-label of Section~sec:lf), the Mann--Whitney statistic on midranks gives
which equals in CISC's notation. Pooling uses van Elteren pair-count weights vanelteren1960:
Under the within-item exchangeability null, has the exact tie-corrected variance , yielding a null standard error ; between-item heterogeneity is captured by the closed-form delete-one-item jackknife . The conservative choice is
Because is a pairwise functional, does not depend on : an exponent estimated at transfers to deployment at .
### Tempering map
Shrinkage. Positive-part James--Stein with a significance floor :
with dead zone ; , . With , eq:js is exactly the empirical-Bayes posterior mean under a prior with plug-in james1961estimation. The map is odd, continuous, never exceeds , and is monotone in and anti-monotone in .
Link. Model within item with the mixture standardized to unit variance, which is what eq:vdw enforces, so where and is the base rate of correct traces. The Bayes-optimal per-trace log-weight coefficient is then
capped at ( dev, label-free). The uncorrected link under-weights strong channels by up to at .
### 
 in one expressionsec:oneline
Two simplifications collapse the pipeline. Factoring out of
eq:js makes the shrinkage a multiplicative gain in the pooled
-statistic alone, and substituting
 with into
eq:link removes the nested radical. is then
with from eq:pooled and from eq:vdw. At the
default the exponent is exactly
one probit and one square root, with no tuned constant anywhere: is a
significance level and a clip, and both are fixed before any
data is seen. The dead zone is now visible as a single condition,
, on which is identically zero and eq:oneline
is bitwise by Proposition~prop:sc. Equations
eq:oneline--eq:half are verified equivalent to the shipped
implementation over randomised inputs including every boundary
(tests/test\_formula.py).
### Anchor properties
proposition[Exact reduction]prop:sc
At , eq:vote equals plain as a function on every trace pool, including tie-breaks. Under , ( dev, label-free), and is continuous through the dead-zone boundary, so a false positive applies an infinitesimal exponent.
proposition
proposition[Exact CISC reduction]prop:cisc
With the feature map , the weights equal with a per-item constant ; hence the argmax, the ties, and the normalized vote shares coincide with CISC-power on every pool.
proposition
proposition[Regularity]prop:reg
The composite is continuous, odd, nondecreasing in , nonincreasing in in magnitude, with .
proposition
Proofs are elementary and pinned by unit tests in the released code (76 tests; the permutation-verified null variance, the EB identity in eq:js, and the link derivation eq:link are each tested numerically).
## Label-Free Estimation
sec:lf
### Pipeline
(i)~Dedup: single-linkage duplicate groups on the lexical-similarity channel at ; each trace gets weight for plurality determination and pair weighting. (ii)~Pseudo-label: with the dedup-weighted plurality. (iii)~Margin gate: keep the top of items by dedup-weighted margin. (iv)~Compute eq:pooled with , giving .
### Sign consistency and its boundary
proposition[Attenuation identity]prop:ccn
Let be the pair-weighted probability that an item's plurality is wrong. If the plurality-error event is independent of given (class-conditional noise), then
.
In particular whenever : the label-free estimate can only under-trust, never mis-sign.
proposition
The identity fails when the flip is caused by confidence, that is, under a confident echo. There the observable law under majority right, and majority wrong via confident echo, is identical (the two-root ambiguity of parisi2014ranking restated for a single channel), so any label-free guarantee is necessarily conditional; it is stated as such rather than papered over.
### De-attenuation and alarms
Split-half agreement over random half-splits estimates under a one-coin model with effective wrong alternatives (inverse-Simpson), inverted as ; is divided by the upper bootstrap bound of (floored at ), which can only under-inflate. Four alarms force : duplicate collapse (median Kish ratio ), sign-aware margin-decoupling, root ambiguity in the split-half quadratic, and insufficient gated items. The margin-decoupling alarm must condition on the estimated trust direction: a sign-naive version (``plurality has the highest mean '') false-alarms on every benign anti-correlated channel---a defect the author hit, diagnosed, and fixed, and which the released tests pin. Finally the significance gate acts on the raw (unbiased sign under Proposition~prop:ccn) and temper on the de-attenuated value. A semi-label-free mode takes only the sign from dev labels, routing it into the pipeline and disabling only the proxy-sign alarm; this purchases immunity to the ambiguity above at negligible labeling cost.
## Heterogeneity: Impossibility and Escape
sec:hetero
### Per-item adaptation is closed under i.i.d.\ coupling
Suppose with no observable covariate.
proposition[Self-reinforcement]prop:selfreinf
Any per-item rule with monotone increasing and odd reinforces the plurality on both branches: up-weights confident traces, which agree with the plurality; up-weights unconfident traces, which are again the plurality side. Empirically such a rule agrees with on of items and its residual flips are net-harmful ( right vs.\ wrong per items).
proposition
proposition[Winner's curse]prop:curse
On plurality-wrong items with , the items where a flip could win, the agreement statistic's sign matches the true sign only of the time.
proposition
proposition[Two-world unidentifiability]prop:twoworld
For any observed , the worlds and induce identical observable laws (constructively, computed against either truth satisfies ). No label-free method can separate them.
proposition
Consequently the per-item oracle ( in this harness) is unreachable, and the honest behaviour is to fall back to the global estimate, which 's dead zone does: in the i.i.d.\ cell every variant returns bitwise (zero discordant pairs).
### TACT-group
Real heterogeneity is typically indexed by an observable covariate (domain, question type). With indexed by a group label, running the estimator per group keeps every group inside the operating regime of Sections~sec:method--sec:lf; groups with fewer than dev (or unlabeled) items fall back to the global estimate, which Propositions~prop:selfreinf--prop:twoworld show is the only defensible default.
## Experimental Setup
sec:exp
Harness. A cluster-mixture oracle generates, per item, up to cached traces with answers, confidences eq:confmodel, and two similarity channels; all methods replay identical pools (paired comparisons, exact McNemar tests). Voting budget ; items per cell on the sweep, for the group study; dev splits of (primary) and (small-dev).
Regimes. The sweep ; three strictly monotone confidence distortions (compression toward , over-confident sigmoid, fourth power), rank-preserving by construction, so discrimination is intact while calibration is destroyed; i.i.d.\ heterogeneity (); covariate-structured heterogeneity (three groups at ); and a confident-echo poison (a wrong cluster echoes verbatim with confidence ).
Baselines. ; CISC-power with ; CISC-devT, the published dev-calibrated protocol (positive grid picked on dev); a binary ECE gate; SignGrid-dev, the strongest trivial baseline (signed exponent grid picked on dev); and the test-set oracle over signed fixed exponents as the upper envelope. The group study adds the naive self-referential per-item method as a negative control and the per-item link oracle as the ceiling.
Pre-registered falsifiers. F1: -dev significantly below the best fixed- CISC at . F2: either variant significantly below anywhere on the sweep. F3: the label-free variant fails to beat the ECE gate on sweep average. F4: CISC-devT or SignGrid-dev matches -dev everywhere, including the distortion, heterogeneity, and small-dev cells.
## Results
sec:results
### Signed recovery, with and without labels
Table~tab:sweep and Fig.~fig:sweep give the sweep. Three observations. First, the published protocols never leave the floor on : CISC-devT's grid is positive-only and the ECE gate never opens (dev ECE ranges -- across the sweep while the signal's discrimination is perfect at the extremes). Second, the label-free variant matches the -label variant nearly point-for-point---at the raw agreement statistic is with , and the CCN identity's sign guarantee holds as predicted, yielding with zero labels. Third, at the dead zone returns exactly, so the paired accuracy difference to is identically zero---``non-inferior'' is replaced by ``identical.''
### Rank invariance where raw values fail
Under monotone compression (Table~tab:adv, Fig.~fig:adv) all confidences huddle near , so every -family weight is nearly uniform: even the oracle over raw-value policies reaches only . 's rank scores are untouched by the distortion and both variants reach . Under the confident echo, dev labels reveal the inversion (high confidence wrong) and -dev counters with , the best result in the field (; three times the floor); label-free, the duplicate-collapse alarm fires and the method correctly refuses---by Proposition~prop:twoworld no label-free method could do better than a coin flip on the sign here, and pretending otherwise would be the real failure.
### Heterogeneity
Table~tab:group and Fig.~fig:group give the group study. In the covariate-structured cell, per-group recovers each group's signed coupling (dev , label-free , the group correctly dead-zoned---and cracks the floor that provably binds every global policy: the label-free variant reaches , within of the per-item link oracle, with zero paired losses to over items (, ). In the i.i.d.\ cell every legitimate method sits at the floor with zero discordant pairs, and the naive self-referential control lands slightly below it---the empirical face of Propositions~prop:selfreinf--prop:twoworld. One observation is reported as-is rather than tuned for: the label-free variant outperforms the dev variant in the grouped cell ( vs.\ ) because its lower exponent cap ( vs.\ ) regularizes better when ; cap robustness is left as an ablation.
### Small dev sets and falsifiers
With dev the conclusions are unchanged ( at ; at ): the SE-aware shrinkage degrades smoothly rather than catastrophically. All four falsifiers survived: F1 ( vs.\ ), F2 (bit-identical at ; never significantly below elsewhere), F3 (sweep means vs.\ ), and F4 (the distortion and echo cells are unreachable by either grid baseline). Against SignGrid-dev the honest margin is narrow on the homogeneous sweep--- even trails by -- in the mid-range, the deliberate cost of shrinkage---and the net advantage concentrates exactly where pre-registered: distortion (), echo (), and label-free operation, which no grid can perform.
### Verification of the implementation
sec:tests
Because every claim in Sections~sec:method--sec:hetero is a
mathematical property rather than an empirical trend, the released code pins
each one with an executable test; the suite is 76 tests for (84
including the follow-on work) and runs in 14 seconds. Table~tab:tests
maps propositions to the tests that would fail if they stopped holding.
Two entries deserve comment. The permutation-invariance test was added after a
defect in which the memoisation key made the test pass while the
estimator itself was order-dependent by up to ; it now calls the internal
routine directly. And the last two rows are counter-tests that assert
failure of rejected alternatives --- the Kish effective-sample-size
formulation and the claim that the shipped default honours the SAFE stopping
guarantee --- so that neither can be silently reinstated by a later change.
### Real-trace validation
sec:real
Validation on real traces used Claude Haiku 4.5 as the frozen model: 100 items
(50 GSM8K gsm8k2021, 50 CommonsenseQA), 12 independent
chain-of-thought traces per item with verbalized confidence (1,200 traces
total), evaluated at with a 40/60 dev/test split. Four findings.
(a) The calibration--discrimination distinction reverses on real data,
and reads it correctly. The channel is extremely well calibrated
in the usual sense: , far inside the gate, so a
binary ECE gate opens and hands the channel to CISC. Yet the measured
within-item discrimination is with 
(): no usable signal, and what little there is points the
wrong way (math , commonsense ; both groups negative).
This is the exact mirror image of the synthetic case in which ECE wrongly
closed the gate on a discriminative channel (Section~sec:setup):
on real traces ECE wrongly opens it on a non-discriminative one.
Calibration is uninformative about voting utility in both directions, and a
signed discrimination statistic is what distinguishes them.
(b) The dead zone fires, and costs exactly nothing. With ,
-dev, -LF and -group all return and are bit-identical
to on every test item ( discordant pairs, ). All methods score
. This is the pre-registered null-direction prediction of
Section~sec:limits confirmed on real data: where the channel carries no
signal, the method is free.
(c) Saturation is the binding constraint, not the estimator. Trace-level
accuracy is on GSM8K and on CommonsenseQA, so only of 
items contain both a correct and an incorrect trace, the only items a
within-item rank statistic can use. The estimator is not underpowered by
design; the benchmark simply does not present the model with enough genuine
uncertainty. Exposing non-null coupling on a strong model requires harder item
pools, not more traces per item.
(d) Verbalized confidence is tie-heavy. Two values (, )
account for of all reports, activating the tie-safe degeneration path of
eq:vdw on many items.
Scope of this first campaign: one model, two benchmarks, . It confirms
the null-direction prediction and the calibration--discrimination argument, and
it is not evidence that improves accuracy, since the channel carried no
signal to exploit. Finding (c) predicts what to do about that, and
Section~sec:hard does it.
### Confirmatory campaign on harder items
sec:hard
Finding (c) predicts that a channel measured as null on saturated benchmarks
should become measurable on items the model finds genuinely uncertain. A
pre-registered follow-up tests that prediction: MATH level-5 problems
math500,lightman2024verify, traces each from the same frozen
model, a -item sign set and an -item evaluation set drawn from the
registered list before any trace was collected, and five hypotheses (H1--H5)
fixed in advance.
The channel is real. On the evaluation set the pooled statistic is
 with , so and H1 passes. This is
the first real-trace evidence that verbalized confidence carries positive
within-item discrimination; the same measurement on GSM8K/CommonsenseQA gave
 ().
The endpoint was unpassable for any method. The realized substrate
saturated again: per-trace accuracy , , a decisive
stratum of of items, and the correct answer present in the pool on
only of those. The in-pool oracle therefore tops out at ,
exact one-sided . H2 fails, but it fails for every conceivable
aggregation method including a perfect one, so the failure is a property of
the substrate rather than of the estimator.
Abstention behaved as designed. returned , with
alarms E4 and E2 firing on the label-free path and the sign set holding too
few informative items to supply a semi-label-free sign. The vote is therefore
bit-identical to at (H3, H4 pass). The cost of acting anyway is
visible in the same table: best-single-confidence, the trivial baseline that
always trusts the channel, loses points at .
One caveat from this campaign transfers beyond . Measured difficulty
depended on the collection protocol: a -problem-per-call probe put
level-5 plurality accuracy at , while the -problem-per-call
confirmatory run yielded on the same stratum. Batch size belongs in
the experimental record whenever traces are collected in batches.
### How wide is the addressable stratum?
sec:window
Both campaigns failed their endpoint for the same reason, which suggests
measuring that reason directly. Define the window as the fraction of
items where the plurality is wrong and the correct answer is present
in the pool: the ceiling for any label-free aggregation method, since nothing
outside it can be changed.
The window was measured on five substrates spanning two domains
(Table~tab:window). For code generation, where an executable test suite
supplies per-sample ground truth and the window might reasonably be expected
to widen, LeetCode Medium/Hard problems leetcodedataset were
solved times each and graded against the benchmark's hidden suites, with
the baseline taken as the largest behavioural cluster over probe inputs
(never expected outputs). The window is (CI
--): wider than label-free QA, but the same order, and the
composition is the same shape at saturated, capability wall,
 rescuable. Nor does budget open it. The seven capability-wall problems
produced zero correct solutions in further attempts (per-problem 
upper bound on the pass rate ), and extrapolating oracle@ shows the
window saturating by .
One precaution belongs with these numbers, because omitting it would have
inverted them. The grading harness was validated against the benchmark's own
reference solutions before any candidate was scored: of pass
under the sandbox's resource limits. An earlier version of the same harness
failed of executions because the host rejects one of the requested
limits outright, and that condition presents as a candidate failure rather
than as an error. Studies that grade by execution should report their
reference-solution pass rate for the same reason a calibration curve is
reported: without it, a broken harness and a capability wall look identical.
## Discussion and Limitations
sec:limits
What the evidence does and does not show. All quantitative claims are on a synthetic oracle whose confidence model eq:confmodel is, at the homogeneous cells, the very coupling the estimator measures. Three design choices limit the circularity: the adversarial regimes (distortions, heterogeneity, echo) lie outside the estimator's working model; mechanism-recovery claims (does track ?) are reported separately from accuracy claims; and the pre-measured baseline landscape (Fig.~fig:baselines) fixed the winnable cells before the method existed. Validation on real LLM traces is the remaining step; the cached-trace runner is committed and the prediction is falsifiable: if real confidence channels never exhibit directional miscalibration or covariate structure, 's dead zone should make it operationally indistinguishable from CISC-devT there.
Narrow margins where labels abound. When labels are plentiful and the confidence scale is trusted, a dev-picked signed grid captures most of the value; 's case rests on the label-free setting, distorted scales, small dev sets, and the exactness of its anchors.
Conditional label-free guarantee, and what happens past the boundary.
Proposition~prop:ccn requires after deduplication, and the
confident-echo ambiguity is fundamental (Proposition~prop:twoworld).
Follow-on work measured the consequence of crossing that boundary, and it is
worse than under-trust. In a paraphrased wrong-majority cell (a dominant
wrong cluster that is semantically tight but carries no verbatim signature, so
deduplication has nothing to collapse) the plurality is wrong on most items,
, and -LF does not merely shrink toward : it
mis-signs, saturates at , and scores against an
 floor of . None of the four alarms fires, because E1 keys on
verbatim duplication which is absent by construction. This is the method's
sharpest unguarded failure mode: the guarantee is conditional, the condition is
not observable label-free, and the existing diagnostics do not detect its
violation. Where a systematically wrong majority is plausible, the
semi-label-free mode (sign from labels) should be the default rather
than an optional refinement.
Global exponent per group. Within a group, ships one exponent; per-item variation inside a group is unexploitable by Propositions~prop:selfreinf--prop:twoworld unless further covariates exist.
The thin window. Section~sec:window measures the stratum this
whole family of methods can act on at -- of items on every substrate
tried, in two domains, with no widening as items harden: they pass from
saturated straight to capability-limited. Two consequences follow for the
method proposed here. First, abstention is not a conservative compromise but
the only correct default, and the measured cost of acting anyway was negative
on both real substrates (best-single-confidence loses points in
Table~tab:hard where the dead zone holds at the floor).
Second, an aggregation gain of the size reported on the synthetic harness is
not measurable on a benchmark of a few hundred items at these window widths,
which is why the real-trace claim in this paper is confined to the premise
(the channel exists and is signed) and to the abstention behaviour, and does
not extend to accuracy. Demonstrating the gain needs a (model, benchmark)
pair whose plurality is wrong on -- of items with the correct answer
still reachable, and no pair tried here satisfies both.
## Conclusion
 turns ``how much should this model's confidence be trusted?'' into a measured, signed, uncertainty-aware quantity with exact fallbacks at both ends, plain self-consistency when the evidence is absent and CISC when it is at full strength, and shows that the sign, long unrepresentable in this family of methods, can be recovered without any labels under stated and tested conditions. The accompanying impossibility results draw the boundary that any future per-item method must respect, and the falsification protocol, having already killed one of the author's own systems, is offered as the more portable contribution.
thebibliography99 1pt
wang2023selfconsistency
X.~Wang, J.~Wei, D.~Schuurmans, Q.~Le, E.~Chi, S.~Narang, A.~Chowdhery, and D.~Zhou, ``Self-consistency improves chain of thought reasoning in language models,'' in Proc.\ ICLR, 2023.
taubenfeld2025cisc
A.~Taubenfeld et~al., ``Confidence improves self-consistency in LLMs,'' in Findings of ACL, 2025, arXiv:2502.06233.
aggarwal2023adaptive
P.~Aggarwal, A.~Madaan, Y.~Yang, and Mausam, ``Let's sample step by step: Adaptive-consistency for efficient reasoning and coding with LLMs,'' in Proc.\ EMNLP, 2023, pp. 12375--12396.
li2024escape
Y.~Li et~al., ``Escape sky-high cost: Early-stopping self-consistency for multi-step reasoning,'' in Proc.\ ICLR, 2024.
kadavath2022language
S.~Kadavath et~al., ``Language models (mostly) know what they know,'' arXiv:2207.05221, 2022.
tian2023just
K.~Tian et~al., ``Just ask for calibration: Strategies for eliciting calibrated confidence scores from language models fine-tuned with human feedback,'' in Proc.\ EMNLP, 2023.
xiong2024can
M.~Xiong et~al., ``Can LLMs express their uncertainty? An empirical evaluation of confidence elicitation in LLMs,'' in Proc.\ ICLR, 2024.
huang2024rankcalibration
X.~Huang, S.~Li, M.~Yu, M.~Sesia, H.~Hassani, I.~Lee, O.~Bastani, and E.~Dobriban, ``Uncertainty in language models: Assessment through rank-calibration,'' in Proc.\ EMNLP, 2024, pp. 284--312.
li2023diverse
Y.~Li et~al., ``Making language models better reasoners with step-aware verifier,'' in Proc.\ ACL, 2023.
borda2025
Z.~Kang, X.~Zhao, and D.~Song, ``Scalable best-of-N selection for large language models via self-certainty,'' in Proc.\ NeurIPS, 2025, arXiv:2502.18581.
reasc2026
J.~Kim, N.~Yang, K.~Min, and K.~Jung, ``Reliability-aware adaptive self-consistency for efficient sampling in LLM reasoning,'' in Findings of ACL, 2026, pp. 21575--21590.
deepconf2025
Y.~Fu et~al., ``Deep think with confidence,'' arXiv:2508.15260, 2025.
dawid1979maximum
A.~P. Dawid and A.~M. Skene, ``Maximum likelihood estimation of observer error-rates using the EM algorithm,'' J.\ Roy.\ Statist.\ Soc.\ C, vol.~28, no.~1, pp. 20--28, 1979.
whitehill2009whose
J.~Whitehill et~al., ``Whose vote should count more: Optimal integration of labels from labelers of unknown expertise,'' in Proc.\ NeurIPS, 2009.
karger2011iterative
D.~R. Karger, S.~Oh, and D.~Shah, ``Iterative learning for reliable crowdsourcing systems,'' in Proc.\ NeurIPS, 2011.
parisi2014ranking
F.~Parisi, F.~Strino, B.~Nadler, and Y.~Kluger, ``Ranking and combining multiple predictors without labeled data,'' Proc.\ Natl.\ Acad.\ Sci., vol.~111, no.~4, pp. 1253--1258, 2014.
fuse2026
J.~Lee, V.~Ma, S.~Zhao, Y.~Nair, A.~Spector, R.~Cohen, and E.~J. Cand\`es, ``FUSE: Ensembling verifiers with zero labeled data,'' arXiv:2604.18547, 2026.
beyondmajority2025
R.~Ai, Y.~Pan, D.~Simchi-Levi, M.~Tambe, and H.~Xu, ``Beyond majority voting: LLM aggregation by leveraging higher-order information,'' arXiv:2510.01499, 2025, accepted to ICML 2026.
vanelteren1960
P.~van Elteren, ``On the combination of independent two-sample tests of Wilcoxon,'' Bull.\ Int.\ Statist.\ Inst., vol.~37, pp. 351--361, 1960.
james1961estimation
W.~James and C.~Stein, ``Estimation with quadratic loss,'' in Proc.\ 4th Berkeley Symp.\ Math.\ Statist.\ Prob., 1961, pp. 361--379.
kish1965
L.~Kish, Survey Sampling. New York, NY, USA: Wiley, 1965.
rao1981analysis
J.~N.~K. Rao and A.~J. Scott, ``The analysis of categorical data from complex sample surveys,'' J.\ Amer.\ Statist.\ Assoc., vol.~76, no.~374, pp. 221--230, 1981.
gsm8k2021
K.~Cobbe et~al., ``Training verifiers to solve math word problems,'' arXiv:2110.14168, 2021.
kuhn2023semantic
L.~Kuhn, Y.~Gal, and S.~Farquhar, ``Semantic uncertainty: Linguistic invariances for uncertainty estimation in natural language generation,'' in Proc.\ ICLR, 2023.
rasc2024
G.~Wan, Y.~Wu, J.~Chen, and S.~Li, ``Reasoning aware self-consistency: Leveraging reasoning paths for efficient LLM sampling,'' in Proc.\ NAACL, 2025, pp. 3613--3635.
math500
D.~Hendrycks et~al., ``Measuring mathematical problem solving with the MATH dataset,'' in Proc.\ NeurIPS Datasets and Benchmarks, 2021.
lightman2024verify
H.~Lightman et~al., ``Let's verify step by step,'' in Proc.\ ICLR, 2024. (MATH-500 test subset.)
leetcodedataset
Y.~Xia et~al., ``LeetCodeDataset: A temporal dataset for robust evaluation and efficient training of code LLMs,'' arXiv:2504.14655, 2025.
thebibliography
document

<!-- === RAW LATEX SOURCE (tact_jmlr.tex @6b98a8e) === -->

\documentclass[twoside,11pt]{article}

% jmlr2e loads natbib, graphicx, amssymb and hyperref itself, and defines both
% theorem environments this paper uses (proposition, remark) off one shared
% counter, plus its own \proof. Loading amsthm on top of it is a hard clash:
% "Command \proof already defined". Every cross-reference here is symbolic
% (\ref{prop:...}), so the shared counter renumbers without breaking anything.
\usepackage{amsmath}
\usepackage{jmlr2e}
\usepackage{booktabs}
\usepackage{multirow}
\usepackage{algorithm}
\usepackage[noend]{algpseudocode}
\font\zhfont="[/System/Library/Fonts/Supplemental/Arial Unicode.ttf]" at 11pt

% JMLR's measure is narrower than TMLR's at 11pt, and two paragraphs carrying
% long inline math overflowed the right margin. These are typographic knobs,
% not edits to the text: the paragraphs stay byte-identical to the other
% builds. \binoppenalty lets a long inline formula break after an operator
% (the default 700 made TeX prefer a 34pt overflow to a break at \cdot).
\emergencystretch=3em
\binoppenalty=300
\relpenalty=250

\newcommand{\Dhat}{\widehat{D}}
\newcommand{\sign}{\operatorname{sign}}
\newcommand{\SC}{\textsc{sc}}
\newcommand{\TACT}{\textsc{tact}}

\ShortHeadings{Trust-Anchored Confidence Tempering}{Ko}
\firstpageno{1}

\begin{document}

\title{TACT: Trust-Anchored Confidence Tempering for\\
       Self-Consistency Voting in Large Language Models}

\author{\name Wei-Chen Ko ({\zhfont 柯瑋宸}, vito1317) \email service@vito1317.com \\
        \addr Independent Researcher}

% No action editor exists before submission, and jmlr2e prints the label
% unconditionally, which leaves a dangling "Editor:" on the title page.
% Blanking the label is presentation-only: once an editor is assigned, delete
% this patch and put the name in \editor{}.
\makeatletter
\def\@starteditor{}
\makeatother
\editor{}

\maketitle
\begin{abstract}
Confidence-weighted self-consistency improves on majority voting when a frozen
model's self-reported confidence is calibrated in \emph{direction}. Every
published scheme is monotone increasing in confidence, so an anti-correlated
channel poisons the vote, and binary calibration gates survive inversion only
by discarding discriminative signal. \TACT{} derives the vote exponent from the
measured, \emph{signed}, within-item discrimination of the channel: a pooled
van~Elteren Somers' $D$ with an item-clustered standard error, positive-part
James--Stein shrinkage, and a Bayes-discriminant link, which at the default
base rate $\bar p=\tfrac12$ collapses to $\gamma=z\sqrt{2+z^2}$ with $z$ the
probit of the shrunk pooled AUC. Inside the shrinkage dead zone the vote is
bit-identical to plain self-consistency. A label-free variant estimates the
sign from agreement pseudo-labels under an attenuation identity that
guarantees sign consistency while the plurality-error rate stays below one
half; past that boundary it mis-signs, which the paper measures and reports.
On a synthetic-oracle harness it recovers anti-correlated channels that pin
every published protocol to the majority floor ($1.000$ vs.\ $0.762$) and
cracks the heterogeneity floor with zero paired losses ($0.923$ vs.\ $0.785$).
Against a dev-picked \emph{signed} grid, which the sweep shows is a far
stronger baseline than the published protocols, the advantage narrows to
distortion, echo, and label-free operation. Two real-trace campaigns then
bound the setting: the channel is null on saturated benchmarks
($z=-1.24$) and positive on competition mathematics ($\Dhat=+0.250$,
$z=+2.54$), yet the stratum any such method can act on measures $2.5$--$7.5\%$
of items across five substrates in two domains, so abstention is the correct
default and the dead zone implements it.
\end{abstract}

\noindent\textbf{Keywords:} 
large language models, self-consistency, confidence calibration, label-free estimation, rank statistics


\section{Introduction}

Self-consistency (\SC; \citealp{wang2023selfconsistency}) improves the reasoning accuracy of a frozen large language model (LLM) by sampling $K$ chain-of-thought traces and returning the plurality answer. Each trace can also report a confidence score, verbalized \citep{tian2023just,xiong2024can}, derived from token log-probabilities, or elicited as $P(\text{True})$ \citep{kadavath2022language}, so weighting votes by confidence is a natural refinement. Confidence-Informed Self-Consistency (CISC; \citealp{taubenfeld2025cisc}) showed that this recovers the accuracy of plain \SC{} at a fraction of the sampling budget, and introduced Within-Question Discrimination (WQD) to argue that \emph{discrimination}, not calibration, is the property that makes a confidence signal useful for voting.

This refinement carries a structural fragility that, to the best of our knowledge, no published method addresses. Every existing weighting scheme is monotone \emph{increasing} in confidence, including CISC's softmax weights, reliability-aware pseudo-counts \citep{reasc2026}, and warmup-thresholded filtering \citep{deepconf2025}. The trust decision is which magnitude of up-weighting to apply; the possibility that the channel is \emph{anti-correlated} with correctness is never searched for. Yet miscalibration of direction is not exotic: reinforcement fine-tuning is known to distort verbalized confidence, distribution shift can invert a signal that was informative in-domain, and in the experiments reported here a simple anti-correlated channel ($\kappa=-0.6$; Section~\ref{sec:setup}) drives confidence-weighted baselines from near-perfect accuracy to far below the majority-vote floor, while the same evidence, read with the correct sign, is a perfect signal. The defensive alternative, a binary dev-set gate that disables the channel when calibration error is high, survives the inversion but discards discriminative signal wholesale: a systematically under-confident yet perfectly ranked channel fails an ECE gate for reasons irrelevant to voting utility \citep{taubenfeld2025cisc,huang2024rankcalibration}.

This paper frames the problem as estimating one scalar: the \emph{signed} within-item discrimination of the confidence channel, and mapping that scalar, with its uncertainty, to a vote exponent. The contributions are:

\textbf{C1: Signed, analytically-tempered weighting.} \TACT{} votes with
$w_i=\exp(\gamma\varphi_i)$, where $\varphi_i$ is the standardized van der
Waerden score of trace $i$'s within-item confidence midrank and $\gamma$ is
\emph{derived}, not grid-searched: a pooled van~Elteren Somers' $D$ (equal to
$2\cdot\mathrm{WQD}-1$) with an exact tie-corrected null variance and an
item-clustered jackknife standard error, shrunk by positive-part James--Stein
with a significance floor, then mapped through a Bayes-discriminant link. Two
anchors are exact: inside the dead zone the vote is \emph{bit-identical} to
\SC{} via a shared code path, and the log-value feature map reproduces
CISC-power. Since $\varphi$ uses only within-item ranks, the method is
invariant to every strictly monotone distortion of the confidence scale, and
under compression it beats the best exponent in the tested grid
$\{0.25,0.5,1,2,4\}$ ($1.000$ vs.\ $0.963$; that optimum sits at the largest
exponent tried, so the comparison bounds the grid, not the family).

\textbf{C2: Label-free estimation of the sign.} The crowdsourcing lineage
estimates reliability from cross-annotator covariance
\citep{dawid1979maximum,parisi2014ranking}; one exchangeable channel from one
model offers no such structure. \TACT{} estimates the signed discrimination
from deduplication-weighted agreement pseudo-labels under a proven
class-conditional-noise identity, $\mathbb{E}[\Dhat_g]=(1-2\bar\rho)D$: while
the pair-weighted plurality-error rate $\bar\rho$ is below $1/2$ the estimate
can only \emph{under}-trust, never mis-sign. A split-half inversion
de-attenuates conservatively and sign-aware alarms return the method to \SC{}
at the identifiability boundary. Past $\bar\rho=1/2$ it does mis-sign, which
Section~\ref{sec:limits} measures rather than assumes away.

\textbf{C3: An impossibility result and its structured escape.} With i.i.d.\
per-item coupling and no observable covariate, per-item label-free adaptation
is closed: any monotone use of an item's own agreement statistic collapses to
plurality reinforcement, the observable sign opposes the truth on $96\%$ of
the plurality-wrong items with $|D_q|>0.3$, the ones where a flip could win, and
$\{\kappa>0,\text{minority right}\}$ and $\{\kappa<0,\text{plurality right}\}$
induce the same observable law. Indexed instead by an observable covariate,
the same estimator run per group recovers each group's signed coupling with
zero paired losses to \SC{} (Section~\ref{sec:hetero}).

\textbf{C4: A pre-registered falsification protocol.} Four falsifiers were
fixed before implementation, two of them designed to kill the method: the
\emph{published} dev-calibrated CISC protocol, whose tuned temperature already
interpolates \SC$\leftrightarrow$CISC, and a dev-picked \emph{signed} exponent
grid, which the sweep shows is far the stronger of the two. All four survived,
and the margins are reported both ways: against the signed grid the advantage
concentrates in distortion, echo, and label-free operation, and \TACT{} trails
it in the mid-range.

\textbf{C5: A measurement of the addressable stratum.} Two real-trace
campaigns and a five-substrate window measurement bound what \emph{any}
label-free aggregation method can do. The channel is null on saturated
benchmarks ($\Dhat=-0.219$, $z=-1.24$) and positive on competition
mathematics ($+0.250$, $z=+2.54$), so the premise holds where the model is
uncertain; but the stratum such a method can act on is $2.5$--$7.5\%$ of items
across all five substrates, in two domains, and does not widen as items
harden.
On both real substrates the in-pool oracle itself cannot clear the
pre-registered endpoint, which makes abstention the correct default rather
than a conservative one.

\section{Related Work}\label{sec:related}

\textbf{Confidence-weighted self-consistency.} \SC{} \citep{wang2023selfconsistency} treats sampled traces as i.i.d.\ votes. CISC \citep{taubenfeld2025cisc} weights votes by softmax-normalized confidence with a temperature tuned on a labeled split, and its WQD metric makes the discrimination-vs-calibration point that also motivates this work; the rank-calibration line \citep{huang2024rankcalibration} reaches the same conclusion independently. Weighted variants \citep{li2023diverse} and early-stopping families
\citep{aggarwal2023adaptive,li2024escape} refine the budget. Self-certainty
\citep{borda2025} is the closest relative in spirit, being the one published
selector that scores candidates by a rank-like quantity rather than by raw
confidence, but it ranks \emph{across} candidates with a fixed positive
orientation and is not evaluated here; reliability-aware pseudo-counts \citep{reasc2026} and warmup-thresholded filtering \citep{deepconf2025} adapt online but only re-scale positive trust. None of these searches a negative exponent: the obstruction is a sign bit in
the hyperparameter grid rather than the weight family itself, as this paper's
own SignGrid-dev baseline shows by opening the same $c^{\gamma}$ family to
negative $\gamma$ and reaching the signed oracle across the negative half-axis.
What no published protocol does is \emph{estimate} that sign, with or without
labels. The dev-calibrated variant must therefore be positioned honestly: CISC's tuned temperature is already a dev-calibrated \SC$\leftrightarrow$CISC interpolation, so the novelty of \TACT-dev lies in the sign, the rank invariance, and the analytic (grid-free) map, not in dev calibration itself.

\textbf{Reliability estimation without labels.} Estimating worker reliability from agreement is classical \citep{dawid1979maximum,whitehill2009whose,karger2011iterative}; spectral meta-learners \citep{parisi2014ranking} and recent LLM ensemble work \citep{fuse2026,beyondmajority2025} exploit covariance across \emph{multiple} predictors. The setting here differs: one exchangeable channel from one model, per-item vote structure, and the known failure of agreement proxies under correlated errors---met here with a quantified attenuation identity, conservative de-attenuation, and alarms in place of an unconditional claim.

\textbf{Shrinkage and rank statistics.} The estimator assembles classical parts: stratified rank statistics \citep{vanelteren1960}, the James--Stein positive-part estimator \citep{james1961estimation}, effective-sample-size corrections \citep{kish1965,rao1981analysis}, and normal-scores discriminant analysis. The claim is the assembly and its anchors, not the parts.

\textbf{Honest sibling result.} A preceding system in the same line of work
(RLEV-VoI, redundancy-discounted voting with value-of-information stopping)
was evaluated under the same falsification discipline and \emph{failed} it,
dominated everywhere by a simple deduplication baseline, and is reported as a
negative result. Its post-mortem isolated the confidence dilemma studied
here.%
% For a double-blind submission, replace the repository URL and commit in the
% availability section with an anonymized artifact link; this paragraph and
% that section are the only two places carrying identifying information.


\section{Problem Setup}\label{sec:setup}

\subsection{Notation}
Items $q=1,\dots,Q$; item $q$ has $m_q$ sampled traces. Trace $(q,i)$ yields an answer $a_{q,i}$ in a discrete set and a confidence $c_{q,i}\in(0,1)$; correctness is $y_{q,i}=\mathbf{1}[a_{q,i}=a_q^\ast]$, unobserved at test time. Plain \SC{} returns $\arg\max_A n_q(A)$ where $n_q(A)$ counts votes for answer $A$. CISC-power weights votes by $c_{q,i}^{\,\gamma}$ with a fixed $\gamma>0$.

\subsection{The confidence dilemma}
The synthetic oracle draws, per item, traces from a cluster mixture with a latent correct answer and generates confidence as
\begin{equation}\label{eq:confmodel}
c_{q,i}=\operatorname{clip}\!\big(\tfrac12+\kappa\,(y_{q,i}-\tfrac12)+\varepsilon_{q,i},\,0.01,\,0.99\big),
\end{equation}
with noise $\varepsilon\sim\mathcal{N}(0,0.1^2)$ and coupling $\kappa\in[-0.6,0.6]$. Fig.~\ref{fig:baselines} maps the baseline landscape \emph{before} the proposed method existed: unconditional weighting (CISC, $\gamma=1$) collapses on $\kappa<0$; an ECE gate never opens off the well-calibrated diagonal; a sign-corrected AUC gate over dev labels nearly saturates the homogeneous sweep. This pre-measurement fixes where a new method can legitimately claim wins---monotone distortion of the confidence scale, covariate heterogeneity, small dev sets, and label-free operation---and the evaluation holds itself to exactly those cells.

\begin{figure}[t]
\centering
\includegraphics[width=0.62\linewidth]{figs/kappa_sweep.png}
\caption{The pre-measured problem statement: accuracy of baseline confidence policies at fixed $K{=}15$ as the true coupling $\kappa$ varies. A trivial sign-corrected AUC gate (green) nearly saturates the homogeneous sweep; the headroom for any new method (shaded) concentrates in the mid-range and, off this plot, in distortion, heterogeneity, and label-free cells.}
\label{fig:baselines}
\end{figure}

\section{TACT}\label{sec:method}

\subsection{Vote family}
Within item $q$, let $R_{q,i}$ be the midrank of $c_{q,i}$ (ties averaged) and
\begin{equation}\label{eq:vdw}
\varphi_{q,i}=\frac{v_{q,i}-\bar v_q}{\sigma_q},\qquad v_{q,i}=\Phi^{-1}\!\Big(\frac{R_{q,i}}{m_q+1}\Big),
\end{equation}
where $\sigma_q$ is the \emph{realized} standard deviation of $v$ within the item (the no-tie value is $0.62$ at $m{=}4$ but $0.95$ at $m{=}40$; a closed form would silently rescale $\gamma$ across budgets), and $\varphi\equiv 0$ if $\sigma_q\le 10^{-8}$ (all-tied confidences vote as plain \SC). The vote is
\begin{equation}\label{eq:vote}
\hat a_q=\arg\max_A \sum_{i:\,a_{q,i}=A}\exp\big(\gamma\,\varphi_{q,i}\big),
\end{equation}
and when $\gamma=0$ the implementation \emph{calls the \SC{} routine itself}, making the zero-trust anchor bitwise exact rather than equal in distribution. Because \eqref{eq:vdw} depends on $c$ only through within-item ranks, every strictly monotone distortion of the confidence scale leaves \eqref{eq:vote} unchanged.

\subsection{Reliability statistic}
For item $q$ with $n^1_q$ positive and $n^0_q$ negative labels (dev: $y$; label-free: the pseudo-label of Section~\ref{sec:lf}), the Mann--Whitney statistic on midranks gives
\begin{equation}
D_q = 2\,\mathrm{AUC}_q-1,\qquad \mathrm{AUC}_q=\frac{U_q}{n^1_q n^0_q},
\end{equation}
which equals $2\cdot\mathrm{WQD}_q-1$ in CISC's notation. Pooling uses van Elteren pair-count weights $N_q=n^1_q n^0_q$ \citep{vanelteren1960}:
\begin{equation}\label{eq:pooled}
\Dhat=\frac{\sum_q N_q D_q}{\sum_q N_q}.
\end{equation}
Under the within-item exchangeability null, $U_q$ has the exact tie-corrected variance $n^1_qn^0_q(m_q{+}1)/12\cdot[1-\sum_t(t^3-t)/(m_q^3-m_q)]$, yielding a null standard error $\mathrm{SE}_0$; between-item heterogeneity is captured by the closed-form delete-one-item jackknife $\mathrm{SE}_J$. The conservative choice is
\begin{equation}
\mathrm{SE}=\max\big(\mathrm{SE}_0,\ \mathrm{SE}_J,\ \tfrac{1}{2\sqrt{N}}\big),\qquad r=\Dhat/\mathrm{SE}.
\end{equation}
Because $D$ is a pairwise functional, $\mathbb{E}[\Dhat]$ does not depend on $m_q$: an exponent estimated at $m{=}40$ transfers to deployment at $m{=}8$.

\subsection{Tempering map}
\emph{Shrinkage.} Positive-part James--Stein with a significance floor $\nu$:
\begin{equation}\label{eq:js}
\tilde D=\sign(\Dhat)\,\max\!\big(0,\ |\Dhat|-\nu^2\mathrm{SE}^2/|\Dhat|\big),
\end{equation}
with dead zone $\{|r|\le\nu\}$; $\nu_{\mathrm{dev}}=1.28$, $\nu_{\mathrm{LF}}=2.33$. With $\nu=1$, \eqref{eq:js} is exactly the empirical-Bayes posterior mean under a $\mathcal{N}(0,\tau^2)$ prior with plug-in $\hat\tau^2=\max(0,\Dhat^2-\mathrm{SE}^2)$ \citep{james1961estimation}. The map is odd, continuous, never exceeds $|\Dhat|$, and is monotone in $\Dhat$ and anti-monotone in $\mathrm{SE}$.

\emph{Link.} Model $\varphi\,|\,y\sim\mathcal{N}(\mu_y,s^2)$ within item with the \emph{mixture} standardized to unit variance, which is what \eqref{eq:vdw} enforces, so $s^2=1/(1+\bar p(1-\bar p)u^2)$ where $u=\sqrt2\,\Phi^{-1}\!\big(\tfrac{1+\tilde D}{2}\big)$ and $\bar p$ is the base rate of correct traces. The Bayes-optimal per-trace log-weight coefficient is then
\begin{equation}\label{eq:link}
\gamma^\ast=\frac{u}{s}=u\sqrt{1+\bar p(1-\bar p)\,u^2},
\end{equation}
capped at $\gamma_{\max}$ ($4$ dev, $2$ label-free). The uncorrected link $\gamma=u$ under-weights strong channels by up to ${\sim}50\%$ at $D=0.9$. The link assumes $\varphi$ is within-item normal, which \eqref{eq:vdw} supplies only asymptotically: at $m_q{=}4$ the score takes four values before standardization. The scale consequence is handled by using the realized $\sigma_q$, but the distributional one is not, and it bites hardest in the small-budget setting this paper advertises ($m{=}40$ estimates transferring to $m{=}8$). Where $\Dhat$ saturates the cap binds and the link's shape is irrelevant; small $m$ is where it has to hold and where it is least justified.

\subsection{\TACT{} in one expression}\label{sec:oneline}
Two simplifications collapse the pipeline. Factoring $\Dhat$ out of
\eqref{eq:js} makes the shrinkage a multiplicative gain in the pooled
$z$-statistic $\zeta=\Dhat/\mathrm{SE}$ alone, and substituting
$u=\sqrt2\,z$ with $z=\Phi^{-1}\!\big(\tfrac{1+\tilde D}{2}\big)$ into
\eqref{eq:link} removes the nested radical. \TACT{} is then
\begin{equation}\label{eq:oneline}
\boxed{\;
\begin{aligned}
\hat a_q&=\arg\max_A \sum_{i:\,a_{q,i}=A}\exp\big(\gamma\,\varphi_{q,i}\big),\\[2pt]
\gamma&=\Big[z\sqrt{2+4\bar p(1-\bar p)z^{2}}\Big]_{-\gamma_{\max}}^{\gamma_{\max}},
\end{aligned}
\;}
\end{equation}
\begin{equation}\label{eq:oneline2}
z=\Phi^{-1}\!\Big(\tfrac12\big[1+\Dhat\,(1-\nu^{2}/\zeta^{2})_{+}\big]\Big),
\quad \zeta=\tfrac{\Dhat}{\mathrm{SE}},
\end{equation}
with $\Dhat$ from \eqref{eq:pooled} and $\varphi$ from \eqref{eq:vdw}. At the
default $\bar p=\tfrac12$ the exponent is exactly
\begin{equation}\label{eq:half}
\gamma=z\sqrt{2+z^{2}},\qquad z=\Phi^{-1}\!\big(\tfrac{1+\tilde D}{2}\big),
\end{equation}
one probit and one square root, where $\tilde D$ is the shrunk \emph{pooled}
statistic of \eqref{eq:js} and not the per-item $\mathrm{AUC}_q$ of
\eqref{eq:pooled}. Nothing in it is fitted to outcomes: $\nu$ is a
significance level and $\gamma_{\max}$ a clip, both fixed before any data is
seen. The clip is not cosmetic, though. Where $\Dhat$ saturates it binds, and
the vote then sees $\gamma_{\max}$ rather than the derived magnitude
(Section~\ref{sec:results}). The dead zone is now visible as a single condition,
$|\zeta|\le\nu$, on which $\gamma$ is identically zero and \eqref{eq:oneline}
is bitwise \SC{} by Proposition~\ref{prop:sc}. Equations
\eqref{eq:oneline}--\eqref{eq:half} are verified equivalent to the shipped
implementation over randomised inputs including every boundary
(\texttt{tests/test\_formula.py}).

\begin{algorithm}[t]
\caption{\TACT{}: derive the exponent, then vote}
\label{alg:tact}
\begin{algorithmic}[1]
\Require labeled dev pools $\mathcal{D}$, test pools $\mathcal{T}$, budget $K$,
floor $\nu$, cap $\gamma_{\max}$
\Ensure one scalar $\gamma$; an answer $\hat a_q$ for each $q\in\mathcal{T}$
\State $\mathcal{S}\gets\emptyset$,\; $H\gets\emptyset$
\For{$q\in\mathcal{D}$}
  \State $y_i\gets\mathbf{1}[a_{q,i}=a^\ast_q]$,\; $i\le K$;\quad $H\gets H\cup\{y\}$
  \If{$0<\textstyle\sum_i y_i<K$} \Comment{informative items only}
    \State $R\gets$ within-item midranks of $c_{q,1:K}$
    \State $D_q\gets 2U_q/(n^1_qn^0_q)-1$, \; $U_q$ from $R$
    \State $\mathcal{S}\gets\mathcal{S}\cup\{(D_q,\,N_q,\,\mathrm{Var}_0(D_q))\}$
  \EndIf
\EndFor
\State $\Dhat\gets\sum_q N_qD_q\,/\sum_q N_q$ \Comment{van Elteren}
\State $\mathrm{SE}\gets\max\{\mathrm{SE}_0,\ \mathrm{SE}_J,\ 1/(2\sqrt{N})\}$
\State $\bar p\gets\mathrm{clip}(\mathrm{mean}(H),\,0.05,\,0.95)$
\State $\zeta\gets\Dhat/\mathrm{SE}$
\If{$|\zeta|\le\nu$} \Comment{dead zone}
  \State $\gamma\gets 0$
\Else
  \State $\tilde D\gets\Dhat\,(1-\nu^2/\zeta^2)$ \Comment{positive-part JS}
  \State $z\gets\Phi^{-1}\big((1+\tilde D)/2\big)$
  \State $\gamma\gets\mathrm{clip}\big(z\sqrt{2+4\bar p(1-\bar p)z^2},\,\pm\gamma_{\max}\big)$
\EndIf
\For{$q\in\mathcal{T}$}
  \If{$\gamma=0$}
    \State $\hat a_q\gets\mathrm{SC}(a_{q,1:K})$ \Comment{same routine, bit-identical}
  \Else
    \State $\varphi\gets$ standardized van der Waerden scores of $c_{q,1:K}$
    \State $\hat a_q\gets\arg\max_A\sum_{i:a_{q,i}=A}e^{\gamma\varphi_i}$
  \EndIf
\EndFor
\State \Return $\gamma$, $\{\hat a_q\}$
\end{algorithmic}
\end{algorithm}

Algorithm~\ref{alg:tact} states the labeled path end to end. Both loops cost
$O(K\log K)$ per item, dominated by the within-item ranking, and the estimate
is a single scalar: nothing item-specific crosses from dev to test, which is
what makes the dead zone a global abstention rather than a per-item one.

\subsection{Anchor properties}
\begin{proposition}[Exact \SC{} reduction]\label{prop:sc}
At $\gamma=0$, \eqref{eq:vote} equals plain \SC{} as a function on every trace pool, including tie-breaks. Under $D=0$, $P(\gamma=0)\to 2\Phi(\nu)-1$ ($80\%$ dev, $98\%$ label-free), and $\gamma$ is continuous through the dead-zone boundary, so a false positive applies an infinitesimal exponent.
\end{proposition}
\begin{proposition}[Exact CISC reduction]\label{prop:cisc}
With the feature map $\varphi^{\log}_{q,i}=\log c_{q,i}-\overline{\log c_q}$, the weights equal $\smash{\lambda_q\,c_{q,i}^{\,\gamma}}$ with a per-item constant $\lambda_q>0$ (distinct from the coupling $\kappa$ of \eqref{eq:confmodel}); hence the argmax, the ties, and the normalized vote shares coincide with CISC-power$(\gamma)$ on every pool.
\end{proposition}
\begin{proposition}[Regularity]\label{prop:reg}
The composite $g(\Dhat,\mathrm{SE})$ is continuous, odd, nondecreasing in $\Dhat$, nonincreasing in $\mathrm{SE}$ in magnitude, with $g(D,0^+)=\gamma^\ast(D)$.
\end{proposition}
Proofs are elementary and pinned by unit tests in the released code (102 tests; the permutation-verified null variance, the EB identity in \eqref{eq:js}, and the link derivation \eqref{eq:link} are each tested numerically).

\section{Label-Free Estimation}\label{sec:lf}

\subsection{Pipeline}
(i)~\emph{Dedup:} single-linkage duplicate groups on the lexical-similarity channel at $0.95$; each trace gets weight $1/|\text{group}|$ for plurality determination and pair weighting. (ii)~\emph{Pseudo-label:} $g_{q,i}=\mathbf{1}[a_{q,i}=M_q]$ with $M_q$ the dedup-weighted plurality. (iii)~\emph{Margin gate:} keep the top $60\%$ of items by dedup-weighted margin. (iv)~Compute \eqref{eq:pooled} with $\mathrm{lab}=g$, giving $(\Dhat_g,\mathrm{SE}_g,r_g)$.

\begin{algorithm}[t]
\caption{\TACT-LF: recovering the sign without labels}
\label{alg:tactlf}
\begin{algorithmic}[1]
\Require pools $\mathcal{P}$, budget $K$, dedup threshold $\theta{=}0.95$,
margin quantile $\beta{=}0.40$, floor $\nu_{\mathrm{LF}}$, cap $\gamma_{\max}$,
splits $J{=}20$, attenuation floor $0.20$, $\mathrm{minGated}$; $\hat\eta$ below is the
estimated attenuation $1-2\bar\rho$, not $\bar\rho$
\Ensure $\gamma$, equal to $0$ whenever any alarm fires
\For{$q\in\mathcal{P}$}
  \State $w_i\gets 1/|\text{group}(i)|$ from single linkage at $\mathrm{dup}\ge\theta$
  \State $M_q\gets\arg\max_A\sum_{i:a_{q,i}=A}w_i$ \Comment{dedup-weighted plurality}
  \State $\mathrm{mgn}_q\gets$ top-two dedup-weighted share gap
\EndFor
\State $G\gets\{q:\mathrm{mgn}_q\ge Q_\beta(\mathrm{mgn}),\ \text{$\ge 2$ distinct answers}\}$
\State $E_1\gets[\ \mathrm{median}_q(\text{Kish ratio})<0.5\ ]$ \Comment{duplicate collapse}
\State $E_4\gets[\ |G|<\mathrm{minGated}\ ]$
\State $g_{q,i}\gets\mathbf{1}[a_{q,i}=M_q]$ for $q\in G$
\State $(\Dhat_g,\mathrm{SE}_g,z_g)\gets$ pooled statistic over $G$ using $g$
\State $s\gets\sign(\Dhat_g)$ \Comment{estimated trust direction}
\State $E_2\gets[\ \psi(s)>0.05\ ]$ \Comment{\emph{sign-aware} margin decoupling}
\State $\alpha\gets$ mean two-half plurality agreement over $J$ splits
\State $k\gets$ inverse-Simpson size of the non-plurality mass
\State $p\gets\big[1+\sqrt{1-(k{+}1)(1-k\alpha)}\,\big]/(k{+}1)$
\State $E_3\gets[\ \text{discriminant}<0.02\ ]$ \Comment{root ambiguity}
\State $\hat\eta\gets\mathrm{clip}\big(\mathrm{UCB}_{95}(2p-1),\,0.20,\,1\big)$
\If{$E_1\lor E_2\lor E_3\lor E_4$ \textbf{ or } $|z_g|\le\nu_{\mathrm{LF}}$} \label{ln:gate}
  \State \Return $0$ \Comment{refuse; the vote stays \SC}
\EndIf
\State \Return $\mathrm{Temper}\big(\Dhat_g/\hat\eta,\ \mathrm{SE}_g/\hat\eta\big)$ with $\bar p$ unset \label{ln:temper}
\end{algorithmic}
\end{algorithm}

Two orderings in Algorithm~\ref{alg:tactlf} are load-bearing. The significance
gate on line~\ref{ln:gate} tests the \emph{raw} $z_g$, whose sign is unbiased by
Proposition~\ref{prop:ccn}, while the tempering on line~\ref{ln:temper} uses
the de-attenuated pair; testing the inflated statistic instead would let the
de-attenuation manufacture significance. And $\bar p$ is left unset on the
label-free path, so the mixture correction of \eqref{eq:link} is not applied
there: the base rate is exactly what no label-free estimator knows.

\subsection{Sign consistency and its boundary}
\begin{proposition}[Attenuation identity]\label{prop:ccn}
Let $\bar\rho$ be the pair-weighted probability that an item's plurality is wrong. If the plurality-error event is independent of $\varphi$ given $y$ (class-conditional noise), then
$\mathbb{E}[\Dhat_g]=(1-2\bar\rho)\,D$.
In particular $\sign\mathbb{E}[\Dhat_g]=\sign D$ whenever $\bar\rho<1/2$: the label-free estimate can only under-trust, never mis-sign.
\end{proposition}
The identity fails when the flip is \emph{caused} by confidence, that is, under a confident echo. There the observable law under $\{$majority right, $D<0\}$ and $\{$majority wrong via confident echo, $D>0\}$ is identical (the two-root ambiguity of \citet{parisi2014ranking} restated for a single channel), so any label-free guarantee is necessarily conditional; it is stated as such rather than papered over.

\subsection{De-attenuation and alarms}
Split-half agreement over $R{=}20$ random half-splits estimates $\alpha=p^2+(1-p)^2/k$ under a one-coin model with $k$ effective wrong alternatives (inverse-Simpson), inverted as $p=[1+\sqrt{1-(k{+}1)(1-k\alpha)}]/(k{+}1)$; $\Dhat_g$ is divided by the \emph{upper} $95\%$ bootstrap bound of $2p-1$ (floored at $0.2$), which can only under-inflate. Four alarms force $\gamma=0$: duplicate collapse (median Kish ratio $<0.5$), sign-aware margin-decoupling, root ambiguity in the split-half quadratic, and insufficient gated items. The margin-decoupling alarm must condition on the estimated trust direction: a sign-naive version (``plurality has the highest mean $\varphi$'') false-alarms on every benign anti-correlated channel---a defect encountered, diagnosed, and fixed during development, and pinned by the released tests. Finally the significance gate acts on the \emph{raw} $z$ (unbiased sign under Proposition~\ref{prop:ccn}) and temper on the de-attenuated value. A semi-label-free mode takes only the sign from ${\sim}50$ dev labels, routing it into the pipeline and disabling only the proxy-sign alarm; this purchases immunity to the ambiguity above at negligible labeling cost.

\section{Heterogeneity: Impossibility and Escape}\label{sec:hetero}

\subsection{Per-item adaptation is closed under i.i.d.\ coupling}
Suppose $\kappa_q\stackrel{\text{iid}}{\sim}\mathcal{N}(0,0.6^2)$ with no observable covariate.

\begin{proposition}[Self-reinforcement]\label{prop:selfreinf}
Any per-item rule $\gamma_q=h(\Dhat^g_q)$ with $h$ monotone increasing and odd reinforces the plurality on both branches: $\Dhat^g_q>0$ up-weights confident traces, which agree with the plurality; $\Dhat^g_q<0$ up-weights unconfident traces, which are again the plurality side.
\end{proposition}
\begin{remark}
Measured in this harness, such a rule agrees with \SC{} on $97.5\%$ of items and its residual flips are net-harmful ($1$ right vs.\ $9$ wrong per $400$ items).
\end{remark}

\begin{remark}[Winner's curse]\label{prop:curse}
This is a measurement in the present harness rather than a theorem: on plurality-wrong items with $|D_q|>0.3$, the items where a flip could win, the agreement statistic's sign matches the true sign only $4\%$ of the time.
\end{remark}

\begin{proposition}[Two-world unidentifiability]\label{prop:twoworld}
Let $w_1=\{\kappa>0,\ \text{minority correct}\}$ and
$w_2=\{\kappa<0,\ \text{plurality correct}\}$. Computed against either truth,
$D^{w_1}=-D^{w_2}$, so the statistic \TACT{} uses cannot order the two worlds.
When the item has exactly two answer clusters the laws of $(a,c)$ coincide
outright and no label-free method can separate them. With three or more
\emph{populated} clusters they do not coincide: under $w_1$ only the correct
minority carries elevated confidence, whereas under $w_2$ every non-plurality
cluster does, so the conditional law of $c$ on a third cluster separates them
(verified numerically; the two laws agree on the top two clusters and differ
with $\mathrm{KS}\ p<10^{-15}$ on the third). The impossibility is therefore
conditional on the pool being effectively binary, which is the regime the
confident-echo cell occupies: $88\%$ of its items have no third cluster at
$K{=}15$. \TACT{} does not exploit the residual signal, and no published
method does either; doing so is left open.
\end{proposition}

Consequently the per-item oracle ($0.973$ in this harness) is unreachable, and the honest behaviour is to fall back to the global estimate, which \TACT's dead zone does: in the i.i.d.\ cell every variant returns bitwise \SC{} (zero discordant pairs).

\subsection{TACT-group}
Real heterogeneity is typically indexed by an observable covariate (domain, question type). With $\kappa$ indexed by a group label, running the estimator per group keeps every group inside the operating regime of Sections~\ref{sec:method}--\ref{sec:lf}; groups with fewer than $30$ dev (or $60$ unlabeled) items fall back to the global estimate, which Propositions~\ref{prop:selfreinf}--\ref{prop:twoworld} show is the only defensible default.

\section{Experimental Setup}\label{sec:exp}

\textbf{Harness.} A cluster-mixture oracle generates, per item, up to $K_{\max}{=}20$ cached traces with answers, confidences \eqref{eq:confmodel}, and two similarity channels; all methods replay identical pools (paired comparisons, exact McNemar tests). Voting budget $K{=}15$; $400$ items per cell on the sweep, $600$ for the group study; dev splits of $200$ (primary) and $50$ (small-dev).

\textbf{Regimes.} The $\kappa$ sweep $\{-0.6,\dots,+0.6\}$; three strictly monotone confidence distortions (compression toward $0.5$, over-confident sigmoid, fourth power), rank-preserving by construction, so discrimination is intact while calibration is destroyed; i.i.d.\ heterogeneity ($\kappa_q\sim\mathcal{N}(0,0.6^2)$); covariate-structured heterogeneity (three groups at $+0.6/0/-0.6$); and a confident-echo poison (a wrong cluster echoes verbatim with confidence $0.95$).

\textbf{Baselines.} \SC; CISC-power with $\gamma\in\{0.25,\dots,4\}$; \emph{CISC-devT}, the published dev-calibrated protocol (positive grid picked on dev); a binary ECE gate; \emph{SignGrid-dev}, the strongest trivial baseline (signed exponent grid picked on dev); and the test-set oracle over signed fixed exponents as the upper envelope. The group study adds the naive self-referential per-item method as a negative control and the per-item link oracle as the ceiling.

\textbf{Pre-registered falsifiers.} The decision rule is stated here because
the protocol is offered as a contribution. Each falsifier is an exact paired
McNemar test on the $400$ items of a cell, at $\alpha=0.05$ one-sided, with
the seed-level bootstrap of Section~\ref{sec:seeds} as the second gate: a
falsifier fires when the single-cell test is significant \emph{and} the
across-seed interval excludes zero. Single-cell tests at this size are
underpowered against a strong baseline, which is the reason for the second
gate; the earlier fixed $\tau=0.02$ tolerance is retained only as a reporting
convenience in the tables. F1: \TACT-dev below the
best fixed-$\gamma$ CISC at $\kappa{=}{+}0.6$ by more than $\tau$. F2: either
variant below \SC{} by more than $\tau$ anywhere on the sweep. F3: the
label-free variant fails to beat the ECE gate on sweep average. F4: CISC-devT
or SignGrid-dev within $\tau$ of \TACT-dev everywhere, including the
distortion, heterogeneity, and small-dev cells. F4 is the falsifier this matters
most for: on a single cell the \TACT{}-minus-SignGrid comparison never reaches
significance anywhere on the sweep (smallest $p=0.08$ at $\kappa=+0.1$), and
it is the ten-seed bootstrap that resolves the mid-range gap as systematic.
A protocol that had reported only the single-seed tests would have called the
mid-range a tie.


\begin{figure}[t]
\centering
\includegraphics[width=0.62\linewidth]{figs/tact_sweep.png}
\caption{Main result on the confidence-usage frontier. \TACT-dev and the fully label-free \TACT-LF track the signed oracle across the sweep; CISC-devT and the ECE gate sit at the \SC{} floor for all $\kappa<0$.}
\label{fig:sweep}
\end{figure}

\section{Results}\label{sec:results}


\begin{table}[t]
\centering
\caption{Coupling sweep (accuracy at $K{=}15$; $400$ paired items per cell; dev $n{=}200$). Published protocols sit at the \SC{} floor on the entire negative half-axis.}
\label{tab:sweep}
\setlength{\tabcolsep}{3.4pt}
\begin{tabular}{r cc cc cc c}
\toprule
$\kappa$ & \SC & ECE & devT & SignGrid & \textbf{\TACT-dev} & \textbf{\TACT-LF} & oracle\\
\midrule
$-0.6$ & .762 & .762 & .762 & 1.000 & \textbf{1.000} & \textbf{1.000} & 1.000\\
$-0.4$ & .805 & .805 & .805 & 1.000 & \textbf{1.000} & \textbf{1.000} & 1.000\\
$-0.2$ & .750 & .750 & .750 & .985 & .975 & .975 & .985\\
$-0.1$ & .750 & .750 & .750 & .915 & .900 & .890 & .915\\
$0.0$  & .745 & .745 & .760 & .760 & .745 & .745 & .772\\
$+0.1$ & .777 & .777 & .932 & .932 & .907 & .907 & .932\\
$+0.2$ & .760 & .760 & .985 & .985 & .978 & .978 & .985\\
$+0.4$ & .785 & .785 & 1.000 & 1.000 & \textbf{1.000} & \textbf{1.000} & 1.000\\
$+0.6$ & .780 & .780 & 1.000 & 1.000 & \textbf{1.000} & \textbf{1.000} & 1.000\\
\bottomrule
\end{tabular}
\end{table}
\subsection{Signed recovery, with and without labels}
Table~\ref{tab:sweep} and Fig.~\ref{fig:sweep} give the sweep. Three observations. First, the published protocols never leave the floor on $\kappa<0$: CISC-devT's grid is positive-only and the ECE gate never opens (dev ECE ranges $0.10$--$0.80$ across the sweep while the signal's discrimination is perfect at the extremes). Second, the label-free variant matches the $200$-label variant nearly point-for-point---at $\kappa{=}{-}0.6$ the raw agreement statistic is $\Dhat_g=-0.81$ with $z=-17.6$, and the CCN identity's sign guarantee holds as predicted, yielding $1.000$ with zero labels. Third, at $\kappa=0$ the dead zone returns $\gamma=0$ exactly, so the paired accuracy difference to \SC{} is identically zero---``non-inferior'' is replaced by ``identical.''

\begin{table}[t]
\centering
\caption{Adversarial regimes (accuracy at $K{=}15$). ``Oracle'' is the test-set best over \emph{raw-value} weight policies; rank invariance beats that entire family under compression.}
\label{tab:adv}
\setlength{\tabcolsep}{3.2pt}
\begin{tabular}{l cc cc c}
\toprule
Regime & \SC & devT & SignGrid & \textbf{\TACT-dev} & \textbf{\TACT-LF}\\
\midrule
Monotone compress & .775 & .963 & .963 & \textbf{1.000} & \textbf{1.000}\\
Monotone overconf & .775 & 1.000 & 1.000 & \textbf{1.000} & \textbf{1.000}\\
Monotone power & .775 & 1.000 & 1.000 & \textbf{1.000} & \textbf{1.000}\\
Hetero (i.i.d.) & .765 & .765 & .765 & .765 & .765\\
Confident echo & .190 & .190 & .568 & \textbf{.615} & .190$^{\dagger}$\\
\bottomrule
\end{tabular}
\vspace{2pt}
{\footnotesize $^{\dagger}$alarm fires and the method refuses to leave \SC:
the conditional guarantee of Prop.~\ref{prop:ccn} working as stated.}
\end{table}


\textbf{Where the derived exponent actually operates.} The four cells that
carry the headline $1.000$ ($\kappa=\pm0.4,\pm0.6$) are cells where $\Dhat$
saturates, so the link returns an untempered $\gamma^\ast$ between $-8.4$ and
$+12.1$ across the seven saturated cells and the cap $\gamma_{\max}=4$ is what
the vote actually sees; the derived magnitude is not doing the
work there, the sign is. Conversely, at $\kappa=\pm0.1,\pm0.2$, where the
derived value lands strictly inside the cap ($|\gamma|$ from $1.10$ to $2.91$),
\TACT-dev trails the dev-picked signed grid on all four cells ($0.900$ vs.\
$0.915$; $0.907$ vs.\ $0.932$; $0.975$ vs.\ $0.985$; $0.978$ vs.\ $0.985$).
Read together: against the \emph{published} protocols the advantage is large
and comes from representing the sign at all, whereas against a signed grid the
analytic map is not better at choosing a magnitude on these cells. Its
advantage over the grid is elsewhere, in the three cells named in C4, and the
one place the interpolation itself pays is confident echo, where $\gamma=-1.198$
falls between grid points and beats the grid optimum $\gamma=-1$
($0.615$ vs.\ $0.568$).

\subsection{Rank invariance where raw values fail}
Under monotone compression (Table~\ref{tab:adv}, Fig.~\ref{fig:adv}) all confidences huddle near $0.5$, so every $c^{\gamma}$-family weight is nearly uniform: even the \emph{oracle} over raw-value policies reaches only $0.963$. \TACT's rank scores are untouched by the distortion and both variants reach $1.000$. Under the confident echo, dev labels reveal the inversion (high confidence $\Rightarrow$ wrong) and \TACT-dev counters with $\gamma=-1.20$, the best result in the field ($0.615$; $3.2\times$ the \SC{} floor); label-free, the duplicate-collapse alarm fires and the method correctly refuses---by Proposition~\ref{prop:twoworld} no label-free method could do better than a coin flip on the sign here, since $88\%$ of the cell's items are effectively binary and the escape the proposition identifies is unavailable on them; pretending otherwise would be the real failure.

\begin{figure}[t]
\centering
\includegraphics[width=0.62\linewidth]{figs/tact_adversarial.png}
\caption{Adversarial regimes. Dotted line: the oracle over raw-value weights. Left group of bars: rank invariance beats that family under compression; right: the labeled variant counters the confident echo while the label-free variant alarms and refuses.}
\label{fig:adv}
\end{figure}

\subsection{Heterogeneity}
Table~\ref{tab:group} and Fig.~\ref{fig:group} give the group study. In the covariate-structured cell, per-group \TACT{} recovers each group's signed coupling (dev $\{+4.0,0.0,-4.0\}$, label-free $\{+2.0,0.0,-2.0\}$, the $\kappa{=}0$ group correctly dead-zoned---and cracks the floor that provably binds every global policy: the label-free variant reaches $0.923$, within $0.023$ of the per-item link oracle, with \emph{zero} paired losses to \SC{} over $600$ items ($+83/-0$, $p=2.1\times10^{-25}$). In the i.i.d.\ cell every method sits at the floor with zero discordant pairs, the naive self-referential control included: it cannot beat the plurality it is derived from. That control is the empirical face of Propositions~\ref{prop:selfreinf}--\ref{prop:twoworld}, and the grouped cell is where it shows: given the same covariate the per-group estimator exploits, it reaches $0.787$ against the $0.785$ floor, two items in $600$. The two arms land within seed noise of each other here ($0.923$ and $0.927$ on
one seed; $0.929\pm0.015$ each over five). A natural explanation would be the arms'
different exponent caps; the ablation rules it out. Sweeping
the cap over $\{1,2,3,4,6,8\}$ moves neither arm at all (spread $0.0000$ for
both), so the cap is not load-bearing in this cell and the difference is
sampling variation.

\begin{table}[t]
\centering
\caption{Heterogeneity study ($600$ paired items; $K{=}15$).}
\label{tab:group}
\setlength{\tabcolsep}{4.5pt}
\begin{tabular}{l cc}
\toprule
Method & Grouped & i.i.d.\\
\midrule
\SC{} (floor) & .785 & .752\\
\TACT{} global (dev) & .785 & .752\\
\TACT-group (dev) & \textbf{.927} & .752\\
\textbf{\TACT-group (label-free)} & .923 & .752\\
Naive per-item (neg.\ control) & .787 & .752\\
Per-item link oracle (ceiling) & .947 & .973\\
\bottomrule
\end{tabular}
\end{table}

\begin{figure}[t]
\centering
\includegraphics[width=0.62\linewidth]{figs/group_eval.png}
\caption{Structured vs.\ i.i.d.\ heterogeneity. Left: with an observable covariate, per-group \TACT{} (label-free) approaches the per-item oracle from the $0.785$ floor with zero losses to \SC. Right: the provably closed i.i.d.\ cell---every method at the floor, the negative control included.}
\label{fig:group}
\end{figure}

\subsection{Small dev sets and falsifiers}
With dev $n{=}50$ the conclusions are unchanged ($1.000$ at $|\kappa|{=}0.6$; $0.978$ at $-0.2$): the SE-aware shrinkage degrades smoothly rather than catastrophically. All four falsifiers survived: F1 ($1.000$ vs.\ $1.000$), F2 (bit-identical at $\kappa{=}0$; nowhere more than the pre-registered $0.02$ accuracy tolerance below \SC), F3 (sweep means $0.944$ vs.\ $0.768$), and F4 (both grid baselines trail by $0.037$ and $0.047$ on the distortion and echo cells, and neither can operate without labels). On the single seed the paired tests against SignGrid-dev are not significant
anywhere ($\kappa{=}-0.2$: $3/7$ discordant, exact $p=0.34$; $\kappa{=}+0.1$:
$8/18$, $p=0.08$), and the ten-seed intervals of Section~\ref{sec:seeds} are
what establish the mid-range deficit. Against SignGrid-dev the honest margin is narrow on the homogeneous sweep---\TACT{} even trails by $0.007$--$0.025$ in the mid-range, the deliberate cost of shrinkage---and the net advantage concentrates exactly where pre-registered: distortion ($+0.037$), echo ($+0.047$), and label-free operation, which no grid can perform.

\subsection{Verification of the implementation}\label{sec:tests}
Because every claim in Sections~\ref{sec:method}--\ref{sec:hetero} is a
mathematical property rather than an empirical trend, the released code pins
each one with an executable test; the suite is 102 tests covering \TACT{} and the
follow-on work. Table~\ref{tab:tests}
maps propositions to the tests that would fail if they stopped holding.

\begin{table}[t]
\centering
\caption{What the test suite verifies. Every proposition in the paper has an
executable counterpart; the counter-tests fail deliberately on rejected
alternatives so a regression cannot silently reinstate them.}
\label{tab:tests}
\setlength{\tabcolsep}{3.4pt}
\begin{tabular}{p{5.2cm} p{9.2cm}}
\toprule
Claim & Evidence \\
\midrule
Prop.~\ref{prop:sc} (exact \SC) & identical incl.\ ties, 200 pools; dead-zone rate $>$70\% under $D{=}0$ \\
Prop.~\ref{prop:cisc} (exact CISC) & identical vote shares, 100 pools \\
Prop.~\ref{prop:ccn} (attenuation) & $\rho\in\{.1,.25,.4\}$, abs.\ $.06$ \\
Props.~\ref{prop:selfreinf}--\ref{prop:twoworld} & 97.5\% \SC{} agreement; 4\% sign match; the two-world boundary is pinned both ways (binary pools indistinguishable, a populated third cluster separates them at $\mathrm{KS}\ p<10^{-10}$) \\
Rank invariance & 3 distortions $\times$ 100 pools \\
Estimator internals & permutation null variance (3{,}000 draws, 10\% tol.), JS--EB identity to $10^{-12}$, link \eqref{eq:link} to rel.\ $10^{-9}$, permutation-invariance regression \\
Rejected alternatives & Kish ESS and the SAFE-under-VoI guarantee each have a test asserting their \emph{failure} \\
\bottomrule
\end{tabular}
\end{table}

Two entries deserve comment. The permutation-invariance test was added after a
defect in which the memoisation key made the \emph{test} pass while the
estimator itself was order-dependent by up to $0.10$; it now calls the internal
routine directly. And the last two rows are counter-tests that assert
\emph{failure} of rejected alternatives --- the Kish effective-sample-size
formulation and the claim that the shipped default honours the SAFE stopping
guarantee --- so that neither can be silently reinstated by a later change.


\subsection{A harness artifact, and dispersion across seeds}\label{sec:seeds}
Two corrections to the synthetic results, both found by re-running what had
been single-seed measurements.

\emph{Tie-breaking was rewarding \SC{} for free.} The generator assigned the
correct answer the code $0$ on every item, and \texttt{argmax} breaks ties
toward the lowest index, so on any item whose vote was tied plain \SC{} chose
correctly by construction: $67.7\%$ on near-tied items against $50.4\%$ for a
random tie-break, with $31.8\%$ of items tied at $K{=}15$. Every method that
perturbs the weights off integers forfeits that subsidy, so the artifact
inflated the baseline and penalised the proposed method. It also produced a
spurious falsifier: at $\kappa=0$, \TACT-dev averaged $0.797$ against \SC{} at
$0.818$ across ten seeds, tripping F2, while the exponents responsible were
$|\gamma|\le0.05$. The items were near-ties whose tie-break had moved, not
items the exponent had reweighted. Answer codes are now permuted per item.
With the artifact removed the two coincide exactly where the dead zone
should hold: $\kappa=0$ gives $0.745$ for both methods and
heterogeneous-$\kappa$ gives $0.765$ for both (ten-seed means $0.758$ and
$0.768$, zero discordant pairs in every seed): the dead zone behaves as
Proposition~\ref{prop:sc} states. All synthetic numbers in this paper are
post-fix.

\emph{Dispersion.} Ten seeds per cell, $400$ paired items each, bootstrap over
seeds. The extremes are stable to the third decimal ($1.000\pm0.001$ at
$|\kappa|\ge0.4$). The mid-range deficit against SignGrid-dev is small but
real rather than noise: $-0.013$ $[-0.017,-0.009]$ at $\kappa=-0.2$, $-0.016$
$[-0.024,-0.009]$ at $-0.1$, $-0.012$ $[-0.018,-0.005]$ at $+0.1$, $-0.013$
$[-0.019,-0.008]$ at $+0.2$, all $p<0.001$. So is the advantage where the
paper claims it: $+0.032$ $[+0.027,+0.037]$ on monotone compression and
$+0.048$ $[+0.037,+0.059]$ on confident echo. The one cell that changes sign
under the fix is heterogeneous-$\kappa$, now $+0.011$ $[0.000,+0.031]$ rather
than a loss. Reporting a single seed would have hidden both the artifact and
the fact that the mid-range gap is systematic.


\subsection{Real-trace validation}\label{sec:real}
Validation on real traces used Claude Haiku 4.5 as the frozen model: 100 items, 50 from
GSM8K \citep{gsm8k2021} and 50 from CommonsenseQA, with \emph{12} independent
chain-of-thought traces and a verbalized confidence per item (1{,}200 traces
total), evaluated at $K{=}12$ with a 40/60 dev/test split. Four findings.

\emph{(a) The calibration--discrimination distinction reverses on real data,
and \TACT{} reads it correctly.} The channel is \emph{extremely well calibrated}
in the usual sense: $\mathrm{ECE}=0.016$, far inside the $0.10$ gate, so a
binary ECE gate \emph{opens} and hands the channel to CISC. Yet the measured
within-item discrimination is $\Dhat=-0.219$ with $\mathrm{SE}=0.176$
($z=-1.24$): no usable signal, and what little there is points the
\emph{wrong way} (math $-0.515$, commonsense $-0.173$; both groups negative).
This is the exact mirror image of the synthetic case in which ECE wrongly
\emph{closed} the gate on a discriminative channel (Section~\ref{sec:setup}):
on real traces ECE wrongly \emph{opens} it on a non-discriminative one.
Calibration is uninformative about voting utility in both directions, and a
signed discrimination statistic is what distinguishes them.

\emph{(b) The dead zone fires, and costs exactly nothing.} With $|z|<\nu$,
\TACT-dev, \TACT-LF and \TACT-group all return $\gamma=0$ and are bit-identical
to \SC{} on every test item ($+0/-0$ discordant pairs, $p=1$). All methods score
$0.917$. This is the pre-registered null-direction prediction of
Section~\ref{sec:limits} confirmed on real data: where the channel carries no
signal, the method is free.

\emph{(c) Saturation is the binding constraint, not the estimator.} Trace-level
accuracy is $0.958$ on GSM8K and $0.847$ on CommonsenseQA, so only $12$ of $100$
items contain both a correct and an incorrect trace, the only items a
within-item rank statistic can use. The estimator is not underpowered by
design; the benchmark simply does not present the model with enough genuine
uncertainty. Exposing non-null coupling on a strong model requires harder item
pools, not more traces per item.

\emph{(d) Verbalized confidence is tie-heavy.} Two values ($0.99$, $0.95$)
account for $49\%$ of all reports, activating the tie-safe degeneration path of
\eqref{eq:vdw} on many items.

Scope of this first campaign: one model, two benchmarks, $K{=}12$. It confirms
the null-direction prediction and the calibration--discrimination argument, and
it is not evidence that \TACT{} improves accuracy, since the channel carried no
signal to exploit. Finding (c) predicts what to do about that, and
Section~\ref{sec:hard} does it.

\subsection{Confirmatory campaign on harder items}\label{sec:hard}
Finding (c) predicts that a channel measured as null on saturated benchmarks
should become measurable on items the model finds genuinely uncertain. A
pre-registered follow-up tests that prediction: $119$ MATH level-5 problems
\citep{math500,lightman2024verify}, $16$ traces each from the same frozen
model, a $30$-item sign set and an $89$-item evaluation set drawn from the
registered list before any trace was collected, and five hypotheses (H1--H5)
fixed in advance.

\emph{The channel is real.} On the evaluation set the pooled statistic is
$\Dhat=+0.250$ with $\mathrm{SE}=0.098$, so $z=+2.54$ and H1 passes. This is
the first real-trace evidence that verbalized confidence carries positive
within-item discrimination; the same measurement on GSM8K/CommonsenseQA gave
$-0.219$ ($z=-1.24$).

\emph{The endpoint was unpassable for any method.} The realized substrate
saturated again: per-trace accuracy $0.819$, \SC{} $0.888$, a decisive
stratum of $10$ of $89$ items, and the correct answer present in the pool on
only $4$ of those. The in-pool \emph{oracle} therefore tops out at $+4/-0$,
exact one-sided $p=0.0625$. H2 fails, but it fails for every conceivable
aggregation method including a perfect one, so the failure is a property of
the substrate rather than of the estimator.

\emph{Abstention behaved as designed.} \TACT{} returned $\gamma=0$, with
alarms E4 and E2 firing on the label-free path and the sign set holding too
few informative items to supply a semi-label-free sign. The vote is therefore
bit-identical to \SC{} at $0.888$ (H3, H4 pass). The cost of acting anyway is
visible in the same table: best-single-confidence, the trivial baseline that
always trusts the channel, loses $4.5$ points at $0.843$.

\begin{table}[t]
\caption{Confirmatory campaign, MATH level-5 evaluation set ($89$ items,
$K{=}16$). Every method replays the same cached pools. The duplication
channel is inert because no reasoning text was collected, so dedup-\SC{}
coincides with \SC{} by construction.}
\label{tab:hard}
\centering\footnotesize
\setlength{\tabcolsep}{4pt}
\begin{tabular}{l c c}
\toprule
Method & Accuracy & net vs.\ \SC \\
\midrule
\SC{} / dedup-\SC{} / CISC-linear & $0.888$ & --- \\
\TACT-LF & $0.888$ & $+0/-0$ \\
\TACT-semi-LF & $0.888$ & $+0/-0$ \\
best-single-confidence & $0.843$ & $+1/-5$ \\
\midrule
in-pool oracle (ceiling) & $0.933$ & $+4/-0$ \\
\bottomrule
\end{tabular}
\end{table}

One caveat from this campaign transfers beyond \TACT. Measured difficulty
depended on the collection protocol: a $30$-problem-per-call probe put
level-5 plurality accuracy at $0.40$, while the $15$-problem-per-call
confirmatory run yielded $0.888$ on the same stratum. Batch size belongs in
the experimental record whenever traces are collected in batches.

\subsection{How wide is the addressable stratum?}\label{sec:window}
Both campaigns failed their endpoint for the same reason, which suggests
measuring that reason directly. Define the \emph{window} as the fraction of
items where the plurality is wrong \emph{and} the correct answer is present
in the pool: the ceiling for any label-free aggregation method, since nothing
outside it can be changed.

The window was measured on five substrates spanning two domains
(Table~\ref{tab:window}). For code generation, where an executable test suite
supplies per-sample ground truth and the window might reasonably be expected
to widen, $40$ LeetCode Medium/Hard problems \citep{leetcodedataset} were
solved $8$ times each and graded against the benchmark's hidden suites, with
the baseline taken as the largest behavioural cluster over probe inputs
(never expected outputs). The window is $3/40=7.5\%$ (CI$_{95}$
$2.6$--$19.9\%$): wider than label-free QA, but the same order, and the
composition is the same shape at $30$ saturated, $7$ capability wall and $3$
rescuable, i.e.\ $75/17.5/7.5\%$. Nor does budget open it. The seven capability-wall problems
produced zero correct solutions in $224$ further attempts (per-problem $95\%$
upper bound on the pass rate $0.088$), and extrapolating oracle@$N$ shows the
window saturating by $N{=}32$.

\begin{table}[t]
\caption{The addressable stratum across substrates, on one definition
throughout: \emph{decisive} is the fraction of items whose plurality is wrong,
\emph{window} (Win.) the fraction that are decisive \emph{and} have the
correct answer somewhere in the pool; both in per cent. The window is the ceiling for any label-free
aggregation method. Rows marked $\dagger$ are measured here; HumanEval+/MBPP+
is recomputed from published oracle-minus-selector tables, which report the
window only. As items harden the decisive fraction grows but the window does
not: they pass from saturated to capability-limited. The MATH L5 row is over
the full registered list of $119$ items, the substrate being the object
measured; Section~\ref{sec:hard} quotes the same quantities over the $89$-item
evaluation set that remains after the sign set is split off ($10$ and $4$
items, so $11.2$ and $4.5$).}
\label{tab:window}
\centering\footnotesize
\setlength{\tabcolsep}{4pt}
\setlength{\tabcolsep}{3pt}
\begin{tabular}{@{}l l r r@{}}
\toprule
Domain & Substrate & Dec. & Win. \\
\midrule
QA & GSM8K / CSQA$^\dagger$ & $9.0$ & $4.0$ \\
QA & MATH L5$^\dagger$ & $7.6$ & $2.5$ \\
QA & AIME / AMC$^\dagger$ & $23.3$ & $3.3$ \\
Code & HumanEval+ / MBPP+ & --- & $3.6$ \\
Code & LeetCode Med/Hard$^\dagger$ & $25.0$ & $7.5$ \\
QA, budget-capped & MATH L5$^\dagger$ & $18.5$ & $11.8$ \\
\bottomrule
\end{tabular}
\end{table}

One precaution belongs with these numbers, because omitting it would have
inverted them. The grading harness was validated against the benchmark's own
reference solutions before any candidate was scored: $178$ of $180$ pass
under the sandbox's resource limits. The check is not a formality: a sandbox whose
resource limits the host rejects outright fails $100\%$ of executions, and
that condition presents as a candidate failure rather than as an error. Studies that grade by execution should report their
reference-solution pass rate for the same reason a calibration curve is
reported: without it, a broken harness and a capability wall look identical.


\subsection{A third axis: reasoning budget}\label{sec:budget}
Difficulty is not the only way to lower per-sample accuracy. Constraining the
reasoning budget lowers it while leaving the correct answer inside the model's
competence, which is the combination the decisive stratum needs and that
difficulty does not supply: as items harden they pass from saturated to
capability-limited without pausing in between. A paired run tests this on the
same $119$ items, same model, same $K$, with the model instructed to answer
without writing any working.

The manipulation was weaker than pre-registered on its stated check
(per-sample accuracy $0.853\to0.781$, against a $0.10$ drop required) and the
correct answer did not leave the pool ($0.950\to0.933$), so what follows is
exploratory. It is reported because the constraint did not lower accuracy
uniformly, it moved items across the plurality boundary: \SC{} fell $0.924\to
0.815$, the window widened from $2.5\%$ to $11.8\%$ (paired exact McNemar on
window membership, $13$ in and $2$ out, $p=0.0037$), and the channel grew
\emph{stronger}, $\Dhat$ from $+0.229$ ($z=2.69$) to $+0.398$ ($z=6.76$).
Forced to answer without working, the model's confidence tracks whether it
happened to be right.

This is the widest window measured anywhere in this paper, and the first
substrate on which the in-pool oracle clears the endpoint at all ($+9/-0$,
$p=0.002$ on a decisive stratum of $17$). \TACT{} nonetheless returned
$\gamma=0$: only $12$ items survived the margin gate against the threshold of
$30$, so E4 fired. That abstention is testable rather than a matter of taste,
and it cost nothing. Estimating $\gamma$ from gold labels, an upper bound no
deployable method has access to, the best available is $+4/-1$ at $\gamma=1$
($p=0.19$); the derived $\gamma=0.670$ gives $+3/-1$. The gap that matters is
therefore not the one the window closes. Even with the window at $11.8\%$ and
an oracle able to convert nine items, confidence weighting reaches fewer than
half of them, and none of the reachable configurations is significant.

\section{Discussion and Limitations}\label{sec:limits}

\textbf{What the evidence does and does not show.} The \emph{accuracy} claims are all on a synthetic oracle whose confidence model \eqref{eq:confmodel} is, at the homogeneous cells, the very coupling the estimator measures. Three design choices limit the circularity, and the first is weaker than it
looks: heterogeneity and echo lie outside the estimator's working model, but
the three distortion cells are rank-preserving by construction and therefore
sit \emph{inside} \TACT's own invariance group, so passing them tests that the
implementation respects an invariance it was built to have rather than
probing an untested regime; mechanism-recovery claims (does $\Dhat$ track $\kappa$?) are reported separately from accuracy claims; and the pre-measured baseline landscape (Fig.~\ref{fig:baselines}) fixed the winnable cells before the method existed. The real-trace campaigns of Sections~\ref{sec:real} and~\ref{sec:hard} test the \emph{premise} and the \emph{abstention behaviour}, and both predictions held: the channel is null on saturated benchmarks and positive on competition mathematics, and the dead zone kept the vote bit-identical to \SC{} in each case. They do not test the accuracy claim, because on neither substrate was the addressable stratum large enough for any method to demonstrate a gain (Section~\ref{sec:window}).

\textbf{Narrow margins where labels abound.} When labels are plentiful and the confidence scale is trusted, a dev-picked signed grid captures most of the value; \TACT's case rests on the label-free setting, distorted scales, small dev sets, and the exactness of its anchors.

\textbf{Conditional label-free guarantee, and what happens past the boundary.}
Proposition~\ref{prop:ccn} requires $\bar\rho<1/2$ after deduplication, and the
confident-echo ambiguity is fundamental (Proposition~\ref{prop:twoworld}).
Follow-on work measured the consequence of crossing that boundary, and it is
worse than under-trust. In a \emph{paraphrased} wrong-majority cell (a dominant
wrong cluster that is semantically tight but carries no verbatim signature, so
deduplication has nothing to collapse) the plurality is wrong on most items,
$\bar\rho>1/2$, and \TACT-LF does not merely shrink toward \SC: it
\emph{mis-signs}, saturates at $\gamma=-2.0$, and scores $0.000$ against an
\SC{} floor of $0.340$. None of the four alarms fires, because E1 keys on
verbatim duplication which is absent by construction. This is the method's
sharpest unguarded failure mode: the guarantee is conditional, the condition is
not observable label-free, and the existing diagnostics do not detect its
violation. Where a systematically wrong majority is plausible, the
semi-label-free mode (sign from ${\sim}50$ labels) should be the default rather
than an optional refinement. The other standard remedy is not tried here and
should be: the failure is driven by a semantically tight wrong cluster that
lexical deduplication cannot see, which is precisely what semantic-equivalence
clustering \citep{kuhn2023semantic} is built to collapse. Substituting a
semantic pseudo-label for the lexical one is the obvious next guard, and this
paper does not test it.

\textbf{Global exponent per group.} Within a group, \TACT{} ships one exponent; per-item variation inside a group is unexploitable by Propositions~\ref{prop:selfreinf}--\ref{prop:twoworld} unless further covariates exist.

\textbf{The thin window.} Section~\ref{sec:window} measures the stratum this
whole family of methods can act on at $2.5$--$7.5\%$ of items across all five
substrates, in two domains, with no widening as items harden: they pass from
saturated straight to capability-limited. Two consequences follow for the
method proposed here. First, abstention is not a conservative compromise but
the only correct default, and the measured cost of acting anyway was negative
on both real substrates (best-single-confidence loses $4.5$ points in
Table~\ref{tab:hard} where the dead zone holds \TACT{} at the \SC{} floor).
Second, an aggregation gain of the size reported on the synthetic harness is
not measurable on a benchmark of a few hundred items at these window widths,
which is why the real-trace claim in this paper is confined to the premise
(the channel exists and is signed) and to the abstention behaviour, and does
not extend to accuracy. Demonstrating the gain needs a (model, benchmark)
pair whose plurality is wrong on $30$--$60\%$ of items with the correct answer
still reachable, and no pair tried here satisfies both.
Section~\ref{sec:budget} adds the one axis that does widen the window, and it
cuts the same way: with the window at $11.8\%$ and an oracle able to convert
nine items, confidence weighting still reaches fewer than half of them. The
width of the window is not the only thing in the way.

\section{Conclusion}
\TACT{} turns ``how far should this model's confidence be trusted?'' into a
measured, signed, uncertainty-aware scalar, and recovers the sign without
labels under conditions this paper states and tests. The measurement that
frames it matters more than the estimator: across five substrates in two
domains, the stratum on which any label-free aggregation method can act is
$2.5$--$7.5\%$ of items, and on both real substrates the in-pool oracle cannot
clear a pre-registered endpoint. In that regime the useful property of an
estimator is knowing when not to act, which the dead zone does exactly.

\section*{Code and Data Availability}
All code, cached traces, and the JSON artifacts behind every table are at
\url{https://github.com/vito1317/adaptive-reasoning-consensus}. Table~\ref{tab:tests}
is produced by \texttt{pytest} at commit \texttt{35ad160}; the synthetic results by
\texttt{experiments/run\_tact\_eval.py}, the real-trace campaigns by
\texttt{run\_tact\_hard\_eval.py}, and the window measurements by
\texttt{run\_g1\_window.py} and \texttt{run\_g1\_deepening.py}. Each script
writes the artifact its table cites.


\bibliography{references}


\end{document}


<!-- === PDF RENDERED TEXT (tact_jmlr.pdf) === -->

<!-- PDF PAGE 1/23 -->
Trust-Anchored Confidence Tempering
TACT: Trust-Anchored Confidence Tempering for
Self-Consistency Voting in Large Language Models
Wei-Chen Ko (柯瑋宸, vito1317)
service@vito1317.com
Independent Researcher
Abstract
Confidence-weighted self-consistency improves on majority voting when a frozen model’s
self-reported confidence is calibrated in direction. Every published scheme is monotone
increasing in confidence, so an anti-correlated channel poisons the vote, and binary calibra-
tion gates survive inversion only by discarding discriminative signal. tact derives the vote
exponent from the measured, signed, within-item discrimination of the channel: a pooled
van Elteren Somers’ D with an item-clustered standard error, positive-part James–Stein
shrinkage, and a Bayes-discriminant link, which at the default base rate ¯p = 1
2 collapses
to γ = z
√
2 + z2 with z the probit of the shrunk pooled AUC. Inside the shrinkage dead
zone the vote is bit-identical to plain self-consistency. A label-free variant estimates the
sign from agreement pseudo-labels under an attenuation identity that guarantees sign con-
sistency while the plurality-error rate stays below one half; past that boundary it mis-
signs, which the paper measures and reports. On a synthetic-oracle harness it recovers
anti-correlated channels that pin every published protocol to the majority floor (1.000 vs.
0.762) and cracks the heterogeneity floor with zero paired losses (0.923 vs. 0.785). Against
a dev-picked signed grid, which the sweep shows is a far stronger baseline than the pub-
lished protocols, the advantage narrows to distortion, echo, and label-free operation. Two
real-trace campaigns then bound the setting: the channel is null on saturated benchmarks
(z = −1.24) and positive on competition mathematics ( bD = +0.250, z = +2.54), yet the
stratum any such method can act on measures 2.5–7.5% of items across five substrates in
two domains, so abstention is the correct default and the dead zone implements it.
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
1

<!-- PDF PAGE 2/23 -->
Ko
confidence, including CISC’s softmax weights, reliability-aware pseudo-counts (Kim et al.,
2026), and warmup-thresholded filtering (Fu et al., 2026). The trust decision is which mag-
nitude of up-weighting to apply; the possibility that the channel is anti-correlated with
correctness is never searched for. Yet miscalibration of direction is not exotic: reinforce-
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
de-attenuates conservatively and sign-aware alarms return the method to sc at the iden-
tifiability boundary. Past ¯ρ = 1/2 it does mis-sign, which Section 9 measures rather than
assumes away.
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
2

<!-- PDF PAGE 3/23 -->
Trust-Anchored Confidence Tempering
protocol, whose tuned temperature already interpolates sc↔CISC, and a dev-picked signed
exponent grid, which the sweep shows is far the stronger of the two. All four survived, and
the margins are reported both ways: against the signed grid the advantage concentrates in
distortion, echo, and label-free operation, and tact trails it in the mid-range.
C5: A measurement of the addressable stratum. Two real-trace campaigns and
a five-substrate window measurement bound what any label-free aggregation method can
do. The channel is null on saturated benchmarks ( bD = −0.219, z = −1.24) and positive
on competition mathematics (+0.250, z = +2.54), so the premise holds where the model is
uncertain; but the stratum such a method can act on is 2.5–7.5% of items on every substrate
tried, in two domains, and does not widen as items harden. On both real substrates the
in-pool oracle itself cannot clear the pre-registered endpoint, which makes abstention the
correct default rather than a conservative one.
2 Related Work
Confidence-weighted self-consistency. sc (Wang et al., 2023) treats sampled traces as
i.i.d. votes. CISC (Taubenfeld et al., 2025) weights votes by softmax-normalized confidence
with a temperature tuned on a labeled split, and its WQD metric makes the discrimination-
vs-calibration point that also motivates this work; the rank-calibration line (Huang et al.,
2024) reaches the same conclusion independently. Weighted variants (Li et al., 2023) and
early-stopping families (Aggarwal et al., 2023; Li et al., 2024) refine the budget.
Self-
certainty (Kang et al., 2025) is the closest relative in spirit, being the one published selector
that scores candidates by a rank-like quantity rather than by raw confidence, but it ranks
across candidates with a fixed positive orientation and is not evaluated here; reliability-
aware pseudo-counts (Kim et al., 2026) and warmup-thresholded filtering (Fu et al., 2026)
adapt online but only re-scale positive trust. None of these searches a negative exponent:
the obstruction is a sign bit in the hyperparameter grid rather than the weight family itself,
as this paper’s own SignGrid-dev baseline shows by opening the same cγ family to negative
γ and reaching the signed oracle across the negative half-axis. What no published protocol
does is estimate that sign, with or without labels. The dev-calibrated variant must therefore
be positioned honestly: CISC’s tuned temperature is already a dev-calibrated sc↔CISC
interpolation, so the novelty of tact-dev lies in the sign, the rank invariance, and the
analytic (grid-free) map, not in dev calibration itself.
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
3

<!-- PDF PAGE 4/23 -->
Ko
Honest sibling result.
A preceding system in the same line of work (RLEV-VoI,
redundancy-discounted voting with value-of-information stopping) was evaluated under the
same falsification discipline and failed it, dominated everywhere by a simple deduplication
baseline, and is reported as a negative result.
Its post-mortem isolated the confidence
dilemma studied here.
3 Problem Setup
3.1 Notation
Items q = 1, . . . , Q; item q has mq sampled traces. Trace (q, i) yields an answer aq,i in
a discrete set and a confidence cq,i ∈(0, 1); correctness is yq,i = 1[aq,i = a∗
q], unobserved
at test time.
Plain sc returns arg maxA nq(A) where nq(A) counts votes for answer A.
CISC-power weights votes by c γ
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
 γ φq,i

,
(3)
and when γ = 0 the implementation calls the sc routine itself, making the zero-trust
anchor bitwise exact rather than equal in distribution.
Because (2) depends on c only
through within-item ranks, every strictly monotone distortion of the confidence scale leaves
(3) unchanged.
4

<!-- PDF PAGE 5/23 -->
Trust-Anchored Confidence Tempering
Figure 1: The pre-measured problem statement: accuracy of baseline confidence policies at
fixed K=15 as the true coupling κ varies.
A trivial sign-corrected AUC gate
(green) nearly saturates the homogeneous sweep; the headroom for any new
method (shaded) concentrates in the mid-range and, off this plot, in distortion,
heterogeneity, and label-free cells.
4.2 Reliability statistic
For item q with n1
q positive and n0
q negative labels (dev: y; label-free: the pseudo-label of
Section 5), the Mann–Whitney statistic on midranks gives
Dq = 2 AUCq −1,
AUCq =
Uq
n1qn0q
,
(4)
which equals 2 · WQDq −1 in CISC’s notation. Pooling uses van Elteren pair-count weights
Nq = n1
qn0
q (van Elteren, 1960):
bD =
P
q NqDq
P
q Nq
.
(5)
Under the within-item exchangeability null, Uq has the exact tie-corrected variance
n1
qn0
q(mq+1)/12 · [1 −P
t(t3 −t)/(m3
q −mq)], yielding a null standard error SE0; between-
item heterogeneity is captured by the closed-form delete-one-item jackknife SEJ.
The
conservative choice is
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
Because D is a pairwise functional, E[ bD] does not depend on mq: an exponent estimated
at m=40 transfers to deployment at m=8.
4.3 Tempering map
Shrinkage. Positive-part James–Stein with a significance floor ν:
˜D = sign( bD) max
 0, | bD| −ν2SE2/| bD|

,
(7)
5

<!-- PDF PAGE 6/23 -->
Ko
with dead zone {|r| ≤ν}; νdev = 1.28, νLF = 2.33. With ν = 1, (7) is exactly the empirical-
Bayes posterior mean under a N(0, τ 2) prior with plug-in ˆτ 2 = max(0, bD2 −SE2) (James
and Stein, 1961). The map is odd, continuous, never exceeds | bD|, and is monotone in bD
and anti-monotone in SE.
Link. Model φ | y ∼N(µy, s2) within item with the mixture standardized to unit vari-
ance, which is what (2) enforces, so s2 = 1/(1 + ¯p(1 −¯p)u2) where u =
√
2 Φ−1  1+ ˜D
2

and ¯p
is the base rate of correct traces. The Bayes-optimal per-trace log-weight coeﬀicient is then
γ∗= u
s = u
p
1 + ¯p(1 −¯p) u2,
(8)
capped at γmax (4 dev, 2 label-free). The uncorrected link γ = u under-weights strong
channels by up to ∼50% at D = 0.9. The link assumes φ is within-item normal, which (2)
supplies only asymptotically: at mq=4 the score takes four values before standardization.
The scale consequence is handled by using the realized σq, but the distributional one is
not, and it bites hardest in the small-budget setting this paper advertises (m=40 estimates
transferring to m=8). Where bD saturates the cap binds and the link’s shape is irrelevant;
small m is where it has to hold and where it is least justified.
4.4 tact in one expression
Two simplifications collapse the pipeline. Factoring bD out of (7) makes the shrinkage a
multiplicative gain in the pooled z-statistic ζ = bD/SE alone, and substituting u =
√
2 z
with z = Φ−1  1+ ˜D
2

into (8) removes the nested radical. tact is then
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
−γmax,
(9)
z = Φ−1
1
2

1 + bD (1 −ν2/ζ2)+

,
ζ =
b
D
SE,
(10)
with bD from (5) and φ from (2). At the default ¯p = 1
2 the exponent is exactly
γ = z
p
2 + z2,
z = Φ−1  1+ ˜D
2

,
(11)
one probit and one square root, where ˜D is the shrunk pooled statistic of (7) and not
the per-item AUCq of (5). Nothing in it is fitted to outcomes: ν is a significance level
and γmax a clip, both fixed before any data is seen.
The clip is not cosmetic, though.
Where bD saturates it binds, and the vote then sees γmax rather than the derived magnitude
(Section 8).
The dead zone is now visible as a single condition, |ζ| ≤ν, on which γ
is identically zero and (9) is bitwise sc by Proposition 1. Equations (9)–(11) are verified
equivalent to the shipped implementation over randomised inputs including every boundary
(tests/test_formula.py).
Algorithm 1 states the labeled path end to end. Both loops cost O(K log K) per item,
dominated by the within-item ranking, and the estimate is a single scalar: nothing item-
specific crosses from dev to test, which is what makes the dead zone a global abstention
rather than a per-item one.
6

<!-- PDF PAGE 7/23 -->
Trust-Anchored Confidence Tempering
Algorithm 1 tact: derive the exponent, then vote
Require: labeled dev pools D, test pools T , budget K, floor ν, cap γmax
Ensure: one scalar γ; an answer ˆaq for each q ∈T
1: S ←∅, H ←∅
2: for q ∈D do
3:
yi ←1[aq,i = a∗
q], i ≤K;
H ←H ∪{y}
4:
if 0 < P
i yi < K then
▷informative items only
5:
R ←within-item midranks of cq,1:K
6:
Dq ←2Uq/(n1
qn0
q) −1,
Uq from R
7:
S ←S ∪{(Dq, Nq, Var0(Dq))}
8: bD ←P
q NqDq / P
q Nq
▷van Elteren
9: SE ←max{SE0, SEJ, 1/(2
√
N)}
10: ¯p ←clip(mean(H), 0.05, 0.95)
11: ζ ←bD/SE
12: if |ζ| ≤ν then
▷dead zone
13:
γ ←0
14: else
15:
˜D ←bD (1 −ν2/ζ2)
▷positive-part JS
16:
z ←Φ−1 (1 + ˜D)/2

17:
γ ←clip
 z
p
2 + 4¯p(1 −¯p)z2, ±γmax

18: for q ∈T do
19:
if γ = 0 then
20:
ˆaq ←SC(aq,1:K)
▷same routine, bit-identical
21:
else
22:
φ ←standardized van der Waerden scores of cq,1:K
23:
ˆaq ←arg maxA
P
i:aq,i=A eγφi
24: return γ, {ˆaq}
4.5 Anchor properties
Proposition 1 (Exact sc reduction) At γ = 0, (3) equals plain sc as a function on
every trace pool, including tie-breaks. Under D = 0, P(γ = 0) →2Φ(ν) −1 (80% dev, 98%
label-free), and γ is continuous through the dead-zone boundary, so a false positive applies
an infinitesimal exponent.
Proposition 2 (Exact CISC reduction) With the feature map φlog
q,i = log cq,i −log cq,
the weights equal λq c γ
q,i with a per-item constant λq > 0 (distinct from the coupling κ of (1));
hence the argmax, the ties, and the normalized vote shares coincide with CISC-power(γ) on
every pool.
Proposition 3 (Regularity) The composite g( bD, SE) is continuous, odd, nondecreasing
in bD, nonincreasing in SE in magnitude, with g(D, 0+) = γ∗(D).
7

<!-- PDF PAGE 8/23 -->
Ko
Algorithm 2 tact-LF: recovering the sign without labels
Require: pools P, budget K, dedup threshold θ=0.95, margin quantile β=0.40, floor νLF,
cap γmax, splits J=20, attenuation floor 0.20, minGated
Ensure: γ, equal to 0 whenever any alarm fires
1: for q ∈P do
2:
wi ←1/|group(i)| from single linkage at dup ≥θ
3:
Mq ←arg maxA
P
i:aq,i=A wi
▷dedup-weighted plurality
4:
mgnq ←top-two dedup-weighted share gap
5: G ←{q : mgnq ≥Qβ(mgn), ≥2 distinct answers}
6: E1 ←[ medianq(Kish ratio) < 0.5 ]
▷duplicate collapse
7: E4 ←[ |G| < minGated ]
8: gq,i ←1[aq,i = Mq] for q ∈G
9: ( bDg, SEg, zg) ←pooled statistic over G using g
10: s ←sign( bDg)
▷estimated trust direction
11: E2 ←[ ψ(s) > 0.05 ]
▷sign-aware margin decoupling
12: α ←mean two-half plurality agreement over J splits
13: k ←inverse-Simpson size of the non-plurality mass
14: p ←

1 +
p
1 −(k+1)(1 −kα)

/(k+1)
15: E3 ←[ discriminant < 0.02 ]
▷root ambiguity
16: ˆρ ←clip
 UCB95(2p −1), 0.20, 1

17: if E1 ∨E2 ∨E3 ∨E4 or |zg| ≤νLF then
18:
return 0
▷refuse; the vote stays sc
19: return Temper
  bDg/ˆρ, SEg/ˆρ

with ¯p unset
Proofs are elementary and pinned by unit tests in the released code (102 tests; the
permutation-verified null variance, the EB identity in (7), and the link derivation (8) are
each tested numerically).
5 Label-Free Estimation
5.1 Pipeline
(i) Dedup: single-linkage duplicate groups on the lexical-similarity channel at 0.95; each
trace gets weight 1/|group| for plurality determination and pair weighting. (ii) Pseudo-
label: gq,i = 1[aq,i = Mq] with Mq the dedup-weighted plurality. (iii) Margin gate: keep
the top 60% of items by dedup-weighted margin. (iv) Compute (5) with lab = g, giving
( bDg, SEg, rg).
Two orderings in Algorithm 2 are load-bearing. The significance gate on line 17 tests
the raw zg, whose sign is unbiased by Proposition 4, while the tempering on line 19 uses
the de-attenuated pair; testing the inflated statistic instead would let the de-attenuation
manufacture significance. And ¯p is left unset on the label-free path, so the mixture correction
of (8) is not applied there: the base rate is exactly what no label-free estimator knows.
8

<!-- PDF PAGE 9/23 -->
Trust-Anchored Confidence Tempering
5.2 Sign consistency and its boundary
Proposition 4 (Attenuation identity) Let ¯ρ be the pair-weighted probability that an
item’s plurality is wrong. If the plurality-error event is independent of φ given y (class-
conditional noise), then E[ bDg] = (1 −2¯ρ) D. In particular sign E[ bDg] = sign D whenever
¯ρ < 1/2: the label-free estimate can only under-trust, never mis-sign.
The identity fails when the flip is caused by confidence, that is, under a confident echo.
There the observable law under {majority right, D < 0} and {majority wrong via confident
echo, D > 0} is identical (the two-root ambiguity of Parisi et al. (2014) restated for a single
channel), so any label-free guarantee is necessarily conditional; it is stated as such rather
than papered over.
5.3 De-attenuation and alarms
Split-half agreement over R=20 random half-splits estimates α = p2 + (1 −p)2/k under
a one-coin model with k effective wrong alternatives (inverse-Simpson), inverted as p =
[1+
p
1 −(k+1)(1 −kα)]/(k+1); bDg is divided by the upper 95% bootstrap bound of 2p−1
(floored at 0.2), which can only under-inflate. Four alarms force γ = 0: duplicate collapse
(median Kish ratio < 0.5), sign-aware margin-decoupling, root ambiguity in the split-half
quadratic, and insuﬀicient gated items. The margin-decoupling alarm must condition on
the estimated trust direction: a sign-naive version (“plurality has the highest mean φ”)
false-alarms on every benign anti-correlated channel—a defect encountered, diagnosed, and
fixed during development, and pinned by the released tests. Finally the significance gate
acts on the raw z (unbiased sign under Proposition 4) and temper on the de-attenuated
value. A semi-label-free mode takes only the sign from ∼50 dev labels, routing it into the
pipeline and disabling only the proxy-sign alarm; this purchases immunity to the ambiguity
above at negligible labeling cost.
6 Heterogeneity: Impossibility and Escape
6.1 Per-item adaptation is closed under i.i.d. coupling
Suppose κq
iid
∼N(0, 0.62) with no observable covariate.
Proposition 5 (Self-reinforcement) Any per-item rule γq = h( bDg
q) with h monotone
increasing and odd reinforces the plurality on both branches: bDg
q > 0 up-weights confident
traces, which agree with the plurality; bDg
q < 0 up-weights unconfident traces, which are again
the plurality side.
Remark 6 Measured in this harness, such a rule agrees with sc on 97.5% of items and its
residual flips are net-harmful (1 right vs. 9 wrong per 400 items).
Remark 7 (Winner’s curse) This is a measurement in the present harness rather than
a theorem: on plurality-wrong items with |Dq| > 0.3, the items where a flip could win, the
agreement statistic’s sign matches the true sign only 4% of the time.
9

<!-- PDF PAGE 10/23 -->
Ko
Proposition 8 (Two-world unidentifiability) Let w1 = {κ > 0, minority correct} and
w2 = {κ < 0, plurality correct}.
Computed against either truth, Dw1 = −Dw2, so the
statistic tact uses cannot order the two worlds. When the item has exactly two answer
clusters the laws of (a, c) coincide outright and no label-free method can separate them.
With three or more populated clusters they do not coincide: under w1 only the correct
minority carries elevated confidence, whereas under w2 every non-plurality cluster does, so
the conditional law of c on a third cluster separates them (verified numerically; the two laws
agree on the top two clusters and differ with KS p < 10−15 on the third). The impossibility is
therefore conditional on the pool being effectively binary, which is the regime the confident-
echo cell occupies: 88% of its items have no third cluster at K=15. tact does not exploit
the residual signal, and no published method does either; doing so is left open.
Consequently the per-item oracle (0.973 in this harness) is unreachable, and the honest
behaviour is to fall back to the global estimate, which tact’s dead zone does: in the i.i.d.
cell every variant returns bitwise sc (zero discordant pairs).
6.2 TACT-group
Real heterogeneity is typically indexed by an observable covariate (domain, question type).
With κ indexed by a group label, running the estimator per group keeps every group inside
the operating regime of Sections 4–5; groups with fewer than 30 dev (or 60 unlabeled) items
fall back to the global estimate, which Propositions 5–8 show is the only defensible default.
7 Experimental Setup
Harness. A cluster-mixture oracle generates, per item, up to Kmax=20 cached traces with
answers, confidences (1), and two similarity channels; all methods replay identical pools
(paired comparisons, exact McNemar tests). Voting budget K=15; 400 items per cell on
the sweep, 600 for the group study; dev splits of 200 (primary) and 50 (small-dev).
Regimes. The κ sweep {−0.6, . . . , +0.6}; three strictly monotone confidence distor-
tions (compression toward 0.5, over-confident sigmoid, fourth power), rank-preserving by
construction, so discrimination is intact while calibration is destroyed; i.i.d. heterogeneity
(κq ∼N(0, 0.62)); covariate-structured heterogeneity (three groups at +0.6/0/ −0.6); and
a confident-echo poison (a wrong cluster echoes verbatim with confidence 0.95).
Baselines. sc; CISC-power with γ ∈{0.25, . . . , 4}; CISC-devT, the published dev-
calibrated protocol (positive grid picked on dev); a binary ECE gate; SignGrid-dev, the
strongest trivial baseline (signed exponent grid picked on dev); and the test-set oracle over
signed fixed exponents as the upper envelope. The group study adds the naive self-referential
per-item method as a negative control and the per-item link oracle as the ceiling.
Pre-registered falsifiers.
The decision rule is stated here because the protocol is
offered as a contribution. Each falsifier is an exact paired McNemar test on the 400 items of
a cell, at α = 0.05 one-sided, with the seed-level bootstrap of Section 8.6 as the second gate:
a falsifier fires when the single-cell test is significant and the across-seed interval excludes
zero.
Single-cell tests at this size are underpowered against a strong baseline, which is
the reason for the second gate; the earlier fixed τ = 0.02 tolerance is retained only as a
reporting convenience in the tables. F1: tact-dev below the best fixed-γ CISC at κ=+0.6
10

<!-- PDF PAGE 11/23 -->
Trust-Anchored Confidence Tempering
Figure 2: Main result on the confidence-usage frontier. tact-dev and the fully label-free
tact-LF track the signed oracle across the sweep; CISC-devT and the ECE gate
sit at the sc floor for all κ < 0.
Table 1: Coupling sweep (accuracy at K=15; 400 paired items per cell; dev n=200). Pub-
lished protocols sit at the sc floor on the entire negative half-axis.
κ
sc
ECE devT SignGrid tact-dev tact-LF oracle
−0.6 .762 .762
.762
1.000
1.000
1.000
1.000
−0.4 .805 .805
.805
1.000
1.000
1.000
1.000
−0.2 .750 .750
.750
.985
.975
.975
.985
−0.1 .750 .750
.750
.915
.900
.890
.915
0.0 .745 .745
.760
.760
.745
.745
.772
+0.1 .777 .777
.932
.932
.907
.907
.932
+0.2 .760 .760
.985
.985
.978
.978
.985
+0.4 .785 .785 1.000
1.000
1.000
1.000
1.000
+0.6 .780 .780 1.000
1.000
1.000
1.000
1.000
by more than τ.
F2: either variant below sc by more than τ anywhere on the sweep.
F3: the label-free variant fails to beat the ECE gate on sweep average. F4: CISC-devT or
SignGrid-dev within τ of tact-dev everywhere, including the distortion, heterogeneity, and
small-dev cells. F4 is the falsifier this matters most for: on a single cell the tact-minus-
SignGrid comparison never reaches significance anywhere on the sweep (smallest p = 0.08
at κ = +0.1), and it is the ten-seed bootstrap that resolves the mid-range gap as systematic.
A protocol that had reported only the single-seed tests would have called the mid-range a
tie.
11

<!-- PDF PAGE 12/23 -->
Ko
Table 2: Adversarial regimes (accuracy at K=15). “Oracle” is the test-set best over raw-
value weight policies; rank invariance beats that entire family under compression.
Regime
sc
devT SignGrid tact-dev tact-LF
Monotone compress .775
.963
.963
1.000
1.000
Monotone overconf
.775 1.000
1.000
1.000
1.000
Monotone power
.775 1.000
1.000
1.000
1.000
Hetero (i.i.d.)
.765
.765
.765
.765
.765
Confident echo
.190
.190
.568
.615
.190†
†alarm fires and the method
refuses to leave sc: the conditional guarantee of Prop. 4 working as stated.
8 Results
8.1 Signed recovery, with and without labels
Table 1 and Fig. 2 give the sweep. Three observations. First, the published protocols never
leave the floor on κ < 0: CISC-devT’s grid is positive-only and the ECE gate never opens
(dev ECE ranges 0.10–0.80 across the sweep while the signal’s discrimination is perfect at
the extremes). Second, the label-free variant matches the 200-label variant nearly point-
for-point—at κ=−0.6 the raw agreement statistic is bDg = −0.81 with z = −17.6, and the
CCN identity’s sign guarantee holds as predicted, yielding 1.000 with zero labels. Third,
at κ = 0 the dead zone returns γ = 0 exactly, so the paired accuracy difference to sc is
identically zero—“non-inferior” is replaced by “identical.”
Where the derived exponent actually operates. The four cells that carry the
headline 1.000 (κ = ±0.4, ±0.6) are cells where bD saturates, so the link returns an untem-
pered γ∗between −8.4 and +12.1 across the seven saturated cells and the cap γmax = 4 is
what the vote actually sees; the derived magnitude is not doing the work there, the sign
is. Conversely, at κ = ±0.1, ±0.2, where the derived value lands strictly inside the cap (|γ|
from 1.10 to 2.91), tact-dev trails the dev-picked signed grid on all four cells (0.900 vs.
0.915; 0.907 vs. 0.932; 0.975 vs. 0.985; 0.978 vs. 0.985). Read together: against the pub-
lished protocols the advantage is large and comes from representing the sign at all, whereas
against a signed grid the analytic map is not better at choosing a magnitude on these cells.
Its advantage over the grid is elsewhere, in the three cells named in C4, and the one place
the interpolation itself pays is confident echo, where γ = −1.198 falls between grid points
and beats the grid optimum γ = −1 (0.615 vs. 0.568).
8.2 Rank invariance where raw values fail
Under monotone compression (Table 2, Fig. 3) all confidences huddle near 0.5, so every cγ-
family weight is nearly uniform: even the oracle over raw-value policies reaches only 0.963.
tact’s rank scores are untouched by the distortion and both variants reach 1.000. Under
the confident echo, dev labels reveal the inversion (high confidence ⇒wrong) and tact-dev
counters with γ = −1.20, the best result in the field (0.615; 3.2× the sc floor); label-free,
the duplicate-collapse alarm fires and the method correctly refuses—by Proposition 8 no
12

<!-- PDF PAGE 13/23 -->
Trust-Anchored Confidence Tempering
Figure 3: Adversarial regimes. Dotted line: the oracle over raw-value weights. Left group
of bars: rank invariance beats that family under compression; right: the labeled
variant counters the confident echo while the label-free variant alarms and refuses.
label-free method could do better than a coin flip on the sign here, since 88% of the cell’s
items are effectively binary and the escape the proposition identifies is unavailable on them;
pretending otherwise would be the real failure.
8.3 Heterogeneity
Table 3 and Fig. 4 give the group study. In the covariate-structured cell, per-group tact
recovers each group’s signed coupling (dev {+4.0, 0.0, −4.0}, label-free {+2.0, 0.0, −2.0},
the κ=0 group correctly dead-zoned—and cracks the floor that provably binds every global
policy: the label-free variant reaches 0.923, within 0.023 of the per-item link oracle, with
zero paired losses to sc over 600 items (+83/ −0, p = 2.1 × 10−25).
In the i.i.d. cell
every method sits at the floor with zero discordant pairs, the naive self-referential control
included: it cannot beat the plurality it is derived from.
That control is the empirical
face of Propositions 5–8, and the grouped cell is where it shows: given the same covariate
the per-group estimator exploits, it reaches 0.787 against the 0.785 floor, two items in 600.
The two arms land within seed noise of each other here (0.923 and 0.927 on one seed;
0.929 ± 0.015 each over five). A natural explanation would be the arms’ different exponent
caps; the ablation rules it out. Sweeping the cap over {1, 2, 3, 4, 6, 8} moves neither arm at
all (spread 0.0000 for both), so the cap is not load-bearing in this cell and the difference is
sampling variation.
8.4 Small dev sets and falsifiers
With dev n=50 the conclusions are unchanged (1.000 at |κ|=0.6; 0.978 at −0.2): the SE-
aware shrinkage degrades smoothly rather than catastrophically. All four falsifiers survived:
F1 (1.000 vs. 1.000), F2 (bit-identical at κ=0; nowhere more than the pre-registered 0.02
accuracy tolerance below sc), F3 (sweep means 0.944 vs. 0.768), and F4 (both grid baselines
trail by 0.037 and 0.047 on the distortion and echo cells, and neither can operate without
labels). On the single seed the paired tests against SignGrid-dev are not significant anywhere
(κ= −0.2: 3/7 discordant, exact p = 0.34; κ= + 0.1: 8/18, p = 0.08), and the ten-seed
13

<!-- PDF PAGE 14/23 -->
Ko
Table 3: Heterogeneity study (600 paired items; K=15).
Method
Grouped
i.i.d.
sc (floor)
.785
.752
tact global (dev)
.785
.752
tact-group (dev)
.927
.752
tact-group (label-free)
.923
.752
Naive per-item (neg. control)
.787
.752
Per-item link oracle (ceiling)
.947
.973
Figure 4: Structured vs. i.i.d. heterogeneity. Left: with an observable covariate, per-group
tact (label-free) approaches the per-item oracle from the 0.785 floor with zero
losses to sc. Right: the provably closed i.i.d. cell—every method at the floor, the
negative control included.
intervals of Section 8.6 are what establish the mid-range deficit. Against SignGrid-dev the
honest margin is narrow on the homogeneous sweep—tact even trails by 0.007–0.025 in
the mid-range, the deliberate cost of shrinkage—and the net advantage concentrates exactly
where pre-registered: distortion (+0.037), echo (+0.047), and label-free operation, which
no grid can perform.
8.5 Verification of the implementation
Because every claim in Sections 4–6 is a mathematical property rather than an empirical
trend, the released code pins each one with an executable test; the suite is 102 tests covering
tact and the follow-on work. Table 4 maps propositions to the tests that would fail if they
stopped holding.
Two entries deserve comment. The permutation-invariance test was added after a defect
in which the memoisation key made the test pass while the estimator itself was order-
dependent by up to 0.10; it now calls the internal routine directly. And the last two rows
are counter-tests that assert failure of rejected alternatives — the Kish effective-sample-size
formulation and the claim that the shipped default honours the SAFE stopping guarantee
— so that neither can be silently reinstated by a later change.
14

<!-- PDF PAGE 15/23 -->
Trust-Anchored Confidence Tempering
Table 4: What the test suite verifies. Every proposition in the paper has an executable
counterpart; the counter-tests fail deliberately on rejected alternatives so a regres-
sion cannot silently reinstate them.
Claim
Evidence
Prop. 1 (exact sc)
identical incl. ties, 200 pools; dead-zone rate >70% un-
der D=0
Prop. 2 (exact CISC)
identical vote shares, 100 pools
Prop. 4 (attenuation)
ρ ∈{.1, .25, .4}, abs. .06
Props. 5–8
97.5% sc agreement; 4% sign match; the two-world
boundary is pinned both ways (binary pools indistin-
guishable, a populated third cluster separates them at
KS p < 10−10)
Rank invariance
3 distortions × 100 pools
Estimator internals
permutation null variance (3,000 draws, 10% tol.), JS–
EB identity to 10−12, link (8) to rel. 10−9, permutation-
invariance regression
Rejected alternatives
Kish ESS and the SAFE-under-VoI guarantee each have
a test asserting their failure
8.6 A harness artifact, and dispersion across seeds
Two corrections to the synthetic results, both found by re-running what had been single-seed
measurements.
Tie-breaking was rewarding sc for free. The generator assigned the correct answer the
code 0 on every item, and argmax breaks ties toward the lowest index, so on any item whose
vote was tied plain sc chose correctly by construction: 67.7% on near-tied items against
50.4% for a random tie-break, with 31.8% of items tied at K=15.
Every method that
perturbs the weights off integers forfeits that subsidy, so the artifact inflated the baseline
and penalised the proposed method. It also produced a spurious falsifier: at κ = 0, tact-
dev averaged 0.797 against sc at 0.818 across ten seeds, tripping F2, while the exponents
responsible were |γ| ≤0.05. The items were near-ties whose tie-break had moved, not items
the exponent had reweighted. Answer codes are now permuted per item. With the artifact
removed the two coincide exactly where the dead zone should hold: κ = 0 gives 0.745 for
both methods and heterogeneous-κ gives 0.765 for both (ten-seed means 0.758 and 0.768,
zero discordant pairs in every seed): the dead zone behaves as Proposition 1 states. All
synthetic numbers in this paper are post-fix.
Dispersion.
Ten seeds per cell, 400 paired items each, bootstrap over seeds.
The
extremes are stable to the third decimal (1.000 ± 0.001 at |κ| ≥0.4).
The mid-range
deficit against SignGrid-dev is small but real rather than noise: −0.013 [−0.017, −0.009]
at κ = −0.2, −0.016 [−0.024, −0.009] at −0.1, −0.012 [−0.018, −0.005] at +0.1, −0.013
[−0.019, −0.008] at +0.2, all p < 0.001. So is the advantage where the paper claims it:
+0.032 [+0.027, +0.037] on monotone compression and +0.048 [+0.037, +0.059] on confi-
15

<!-- PDF PAGE 16/23 -->
Ko
dent echo. The one cell that changes sign under the fix is heterogeneous-κ, now +0.011
[0.000, +0.031] rather than a loss. Reporting a single seed would have hidden both the
artifact and the fact that the mid-range gap is systematic.
8.7 Real-trace validation
Validation on real traces used Claude Haiku 4.5 as the frozen model: 100 items, 50 from
GSM8K (Cobbe et al., 2021) and 50 from CommonsenseQA, with 12 independent chain-of-
thought traces and a verbalized confidence per item (1,200 traces total), evaluated at K=12
with a 40/60 dev/test split. Four findings.
(a) The calibration–discrimination distinction reverses on real data, and tact reads it
correctly. The channel is extremely well calibrated in the usual sense: ECE = 0.016, far
inside the 0.10 gate, so a binary ECE gate opens and hands the channel to CISC. Yet the
measured within-item discrimination is bD = −0.219 with SE = 0.176 (z = −1.24): no
usable signal, and what little there is points the wrong way (math −0.515, commonsense
−0.173; both groups negative). This is the exact mirror image of the synthetic case in which
ECE wrongly closed the gate on a discriminative channel (Section 3): on real traces ECE
wrongly opens it on a non-discriminative one. Calibration is uninformative about voting
utility in both directions, and a signed discrimination statistic is what distinguishes them.
(b) The dead zone fires, and costs exactly nothing. With |z| < ν, tact-dev, tact-LF
and tact-group all return γ = 0 and are bit-identical to sc on every test item (+0/ −0
discordant pairs, p = 1). All methods score 0.917. This is the pre-registered null-direction
prediction of Section 9 confirmed on real data: where the channel carries no signal, the
method is free.
(c) Saturation is the binding constraint, not the estimator. Trace-level accuracy is 0.958
on GSM8K and 0.847 on CommonsenseQA, so only 12 of 100 items contain both a correct
and an incorrect trace, the only items a within-item rank statistic can use. The estimator
is not underpowered by design; the benchmark simply does not present the model with
enough genuine uncertainty. Exposing non-null coupling on a strong model requires harder
item pools, not more traces per item.
(d) Verbalized confidence is tie-heavy. Two values (0.99, 0.95) account for 49% of all
reports, activating the tie-safe degeneration path of (2) on many items.
Scope of this first campaign: one model, two benchmarks, K=12. It confirms the null-
direction prediction and the calibration–discrimination argument, and it is not evidence
that tact improves accuracy, since the channel carried no signal to exploit. Finding (c)
predicts what to do about that, and Section 8.8 does it.
8.8 Confirmatory campaign on harder items
Finding (c) predicts that a channel measured as null on saturated benchmarks should be-
come measurable on items the model finds genuinely uncertain. A pre-registered follow-up
tests that prediction: 119 MATH level-5 problems (Hendrycks et al., 2021; Lightman et al.,
2024), 16 traces each from the same frozen model, a 30-item sign set and an 89-item evalu-
ation set drawn from the registered list before any trace was collected, and five hypotheses
(H1–H5) fixed in advance.
16

<!-- PDF PAGE 17/23 -->
Trust-Anchored Confidence Tempering
Table 5: Confirmatory campaign, MATH level-5 evaluation set (89 items, K=16). Every
method replays the same cached pools. The duplication channel is inert because
no reasoning text was collected, so dedup-sc coincides with sc by construction.
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
The channel is real. On the evaluation set the pooled statistic is bD = +0.250 with
SE = 0.098, so z = +2.54 and H1 passes. This is the first real-trace evidence that ver-
balized confidence carries positive within-item discrimination; the same measurement on
GSM8K/CommonsenseQA gave −0.219 (z = −1.24).
The endpoint was unpassable for any method. The realized substrate saturated again:
per-trace accuracy 0.819, sc 0.888, a decisive stratum of 10 of 89 items, and the correct
answer present in the pool on only 4 of those. The in-pool oracle therefore tops out at
+4/ −0, exact one-sided p = 0.0625. H2 fails, but it fails for every conceivable aggregation
method including a perfect one, so the failure is a property of the substrate rather than of
the estimator.
Abstention behaved as designed. tact returned γ = 0, with alarms E4 and E2 firing
on the label-free path and the sign set holding too few informative items to supply a semi-
label-free sign. The vote is therefore bit-identical to sc at 0.888 (H3, H4 pass). The cost of
acting anyway is visible in the same table: best-single-confidence, the trivial baseline that
always trusts the channel, loses 4.5 points at 0.843.
One caveat from this campaign transfers beyond tact. Measured diﬀiculty depended
on the collection protocol: a 30-problem-per-call probe put level-5 plurality accuracy at
0.40, while the 15-problem-per-call confirmatory run yielded 0.888 on the same stratum.
Batch size belongs in the experimental record whenever traces are collected in batches.
8.9 How wide is the addressable stratum?
Both campaigns failed their endpoint for the same reason, which suggests measuring that
reason directly. Define the window as the fraction of items where the plurality is wrong and
the correct answer is present in the pool: the ceiling for any label-free aggregation method,
since nothing outside it can be changed.
The window was measured on five substrates spanning two domains (Table 6).
For
code generation, where an executable test suite supplies per-sample ground truth and the
window might reasonably be expected to widen, 40 LeetCode Medium/Hard problems (Xia
et al., 2025) were solved 8 times each and graded against the benchmark’s hidden suites,
with the baseline taken as the largest behavioural cluster over probe inputs (never expected
outputs). The window is 3/40 = 7.5% (CI95 2.6–19.9%): wider than label-free QA, but the
same order, and the composition is the same shape at 30 saturated, 7 capability wall and 3
17

<!-- PDF PAGE 18/23 -->
Ko
Table 6: The addressable stratum across substrates, on one definition throughout: decisive
is the fraction of items whose plurality is wrong, window (Win.)
the fraction
that are decisive and have the correct answer somewhere in the pool; both in
per cent. The window is the ceiling for any label-free aggregation method. Rows
marked † are measured here; HumanEval+/MBPP+ is recomputed from published
oracle-minus-selector tables, which report the window only. As items harden the
decisive fraction grows but the window does not: they pass from saturated to
capability-limited. The MATH L5 row is over the full registered list of 119 items,
the substrate being the object measured; Section 8.8 quotes the same quantities
over the 89-item evaluation set that remains after the sign set is split off (10 and
4 items, so 11.2 and 4.5).
Domain
Substrate
Dec. Win.
QA
GSM8K / CSQA†
9.0
4.0
QA
MATH L5†
7.6
2.5
QA
AIME / AMC†
23.3
3.3
Code
HumanEval+ / MBPP+
—
3.6
Code
LeetCode Med/Hard†
25.0
7.5
QA, budget-capped MATH L5†
18.5
11.8
rescuable, i.e. 75/17.5/7.5%. Nor does budget open it. The seven capability-wall problems
produced zero correct solutions in 224 further attempts (per-problem 95% upper bound on
the pass rate 0.088), and extrapolating oracle@N shows the window saturating by N=32.
One precaution belongs with these numbers, because omitting it would have inverted
them. The grading harness was validated against the benchmark’s own reference solutions
before any candidate was scored: 178 of 180 pass under the sandbox’s resource limits. The
check is not a formality: a sandbox whose resource limits the host rejects outright fails 100%
of executions, and that condition presents as a candidate failure rather than as an error.
Studies that grade by execution should report their reference-solution pass rate for the same
reason a calibration curve is reported: without it, a broken harness and a capability wall
look identical.
8.10 A third axis: reasoning budget
Diﬀiculty is not the only way to lower per-sample accuracy. Constraining the reasoning
budget lowers it while leaving the correct answer inside the model’s competence, which is
the combination the decisive stratum needs and that diﬀiculty does not supply: as items
harden they pass from saturated to capability-limited without pausing in between. A paired
run tests this on the same 119 items, same model, same K, with the model instructed to
answer without writing any working.
The manipulation was weaker than pre-registered on its stated check (per-sample ac-
curacy 0.853 →0.781, against a 0.10 drop required) and the correct answer did not leave
the pool (0.950 →0.933), so what follows is exploratory. It is reported because the con-
straint did not lower accuracy uniformly, it moved items across the plurality boundary: sc
18

<!-- PDF PAGE 19/23 -->
Trust-Anchored Confidence Tempering
fell 0.924 →0.815, the window widened from 2.5% to 11.8% (paired exact McNemar on
window membership, 13 in and 2 out, p = 0.0037), and the channel grew stronger, bD from
+0.229 (z = 2.69) to +0.398 (z = 6.76). Forced to answer without working, the model’s
confidence tracks whether it happened to be right.
This is the widest window measured anywhere in this paper, and the first substrate on
which the in-pool oracle clears the endpoint at all (+9/−0, p = 0.002 on a decisive stratum
of 17). tact nonetheless returned γ = 0: only 12 items survived the margin gate against
the threshold of 30, so E4 fired. That abstention is testable rather than a matter of taste,
and it cost nothing. Estimating γ from gold labels, an upper bound no deployable method
has access to, the best available is +4/ −1 at γ = 1 (p = 0.19); the derived γ = 0.670 gives
+3/ −1. The gap that matters is therefore not the one the window closes. Even with the
window at 11.8% and an oracle able to convert nine items, confidence weighting reaches
fewer than half of them, and none of the reachable configurations is significant.
9 Discussion and Limitations
What the evidence does and does not show.
The accuracy claims are all on a
synthetic oracle whose confidence model (1) is, at the homogeneous cells, the very coupling
the estimator measures. Three design choices limit the circularity, and the first is weaker
than it looks: heterogeneity and echo lie outside the estimator’s working model, but the
three distortion cells are rank-preserving by construction and therefore sit inside tact’s
own invariance group, so passing them tests that the implementation respects an invariance
it was built to have rather than probing an untested regime; mechanism-recovery claims
(does bD track κ?) are reported separately from accuracy claims; and the pre-measured
baseline landscape (Fig. 1) fixed the winnable cells before the method existed. The real-
trace campaigns of Sections 8.7 and 8.8 test the premise and the abstention behaviour,
and both predictions held: the channel is null on saturated benchmarks and positive on
competition mathematics, and the dead zone kept the vote bit-identical to sc in each case.
They do not test the accuracy claim, because on neither substrate was the addressable
stratum large enough for any method to demonstrate a gain (Section 8.9).
Narrow margins where labels abound. When labels are plentiful and the confidence
scale is trusted, a dev-picked signed grid captures most of the value; tact’s case rests on
the label-free setting, distorted scales, small dev sets, and the exactness of its anchors.
Conditional label-free guarantee, and what happens past the boundary.
Proposition 4 requires ¯ρ < 1/2 after deduplication, and the confident-echo ambiguity is
fundamental (Proposition 8). Follow-on work measured the consequence of crossing that
boundary, and it is worse than under-trust. In a paraphrased wrong-majority cell (a domi-
nant wrong cluster that is semantically tight but carries no verbatim signature, so dedupli-
cation has nothing to collapse) the plurality is wrong on most items, ¯ρ > 1/2, and tact-LF
does not merely shrink toward sc: it mis-signs, saturates at γ = −2.0, and scores 0.000
against an sc floor of 0.340. None of the four alarms fires, because E1 keys on verbatim
duplication which is absent by construction. This is the method’s sharpest unguarded fail-
ure mode: the guarantee is conditional, the condition is not observable label-free, and the
existing diagnostics do not detect its violation. Where a systematically wrong majority
is plausible, the semi-label-free mode (sign from ∼50 labels) should be the default rather
19

<!-- PDF PAGE 20/23 -->
Ko
than an optional refinement. The other standard remedy is not tried here and should be:
the failure is driven by a semantically tight wrong cluster that lexical deduplication cannot
see, which is precisely what semantic-equivalence clustering (Kuhn et al., 2023) is built to
collapse. Substituting a semantic pseudo-label for the lexical one is the obvious next guard,
and this paper does not test it.
Global exponent per group. Within a group, tact ships one exponent; per-item
variation inside a group is unexploitable by Propositions 5–8 unless further covariates exist.
The thin window. Section 8.9 measures the stratum this whole family of methods
can act on at 2.5–7.5% of items on every substrate tried, in two domains, with no widening
as items harden: they pass from saturated straight to capability-limited. Two consequences
follow for the method proposed here. First, abstention is not a conservative compromise but
the only correct default, and the measured cost of acting anyway was negative on both real
substrates (best-single-confidence loses 4.5 points in Table 5 where the dead zone holds tact
at the sc floor). Second, an aggregation gain of the size reported on the synthetic harness
is not measurable on a benchmark of a few hundred items at these window widths, which is
why the real-trace claim in this paper is confined to the premise (the channel exists and is
signed) and to the abstention behaviour, and does not extend to accuracy. Demonstrating
the gain needs a (model, benchmark) pair whose plurality is wrong on 30–60% of items with
the correct answer still reachable, and no pair tried here satisfies both.
10 Conclusion
tact turns “how far should this model’s confidence be trusted?” into a measured, signed,
uncertainty-aware scalar, and recovers the sign without labels under conditions this paper
states and tests. The measurement that frames it matters more than the estimator: across
five substrates in two domains, the stratum on which any label-free aggregation method
can act is 2.5–7.5% of items, and on both real substrates the in-pool oracle cannot clear
a pre-registered endpoint. In that regime the useful property of an estimator is knowing
when not to act, which the dead zone does exactly.
Code and Data Availability
All code, cached traces, and the JSON artifacts behind every table are at https://github.
com/vito1317/adaptive-reasoning-consensus. Table 4 is produced by pytest at com-
mit 35ad160; the synthetic results by experiments/run_tact_eval.py, the real-trace cam-
paigns by run_tact_hard_eval.py, and the window measurements by run_g1_window.py
and run_g1_deepening.py. Each script writes the artifact its table cites.
References
Pranjal Aggarwal, Aman Madaan, Yiming Yang, and Mausam. Let’s sample step by step:
Adaptive-consistency for eﬀicient reasoning and coding with LLMs. In Proceedings of the
2023 Conference on Empirical Methods in Natural Language Processing, pages 12375–
12396, Singapore, December 2023. Association for Computational Linguistics.
URL
https://aclanthology.org/2023.emnlp-main.761/.
20

<!-- PDF PAGE 21/23 -->
Trust-Anchored Confidence Tempering
Rui Ai, Yuqi Pan, David Simchi-Levi, Milind Tambe, and Haifeng Xu. Beyond majority
voting: LLM aggregation by leveraging higher-order information, 2025. URL https:
//arxiv.org/abs/2510.01499. Accepted to ICML 2026.
Karl Cobbe, Vineet Kosaraju, Mohammad Bavarian, Mark Chen, Heewoo Jun, Lukasz
Kaiser, Matthias Plappert, Jerry Tworek, Jacob Hilton, Reiichiro Nakano, Christopher
Hesse, and John Schulman. Training verifiers to solve math word problems. arXiv preprint
arXiv:2110.14168, 2021. URL https://arxiv.org/abs/2110.14168.
Alexander Philip Dawid and Allan M. Skene. Maximum likelihood estimation of observer
error-rates using the EM algorithm. Journal of the Royal Statistical Society: Series C
(Applied Statistics), 28(1):20–28, 1979. doi: 10.2307/2346806.
Yichao Fu, Xuewei Wang, Hao Zhang, Yuandong Tian, and Jiawei Zhao. Deep think with
confidence.
In The Fourteenth International Conference on Learning Representations
(ICLR), 2026. URL https://arxiv.org/abs/2508.15260.
Dan Hendrycks, Collin Burns, Saurav Kadavath, Akul Arora, Steven Basart, Eric Tang,
Dawn Song, and Jacob Steinhardt. Measuring mathematical problem solving with the
MATH dataset. In Proceedings of the Neural Information Processing Systems Track on
Datasets and Benchmarks 1, 2021. URL https://arxiv.org/abs/2103.03874. MATH-
500 subset as distributed by Lightman et al., “Let’s Verify Step by Step” (2023).
Xinmeng Huang, Shuo Li, Mengxin Yu, Matteo Sesia, Hamed Hassani, Insup Lee, Osbert
Bastani, and Edgar Dobriban.
Uncertainty in language models: Assessment through
rank-calibration. In Proceedings of the 2024 Conference on Empirical Methods in Natural
Language Processing, pages 284–312, Miami, Florida, USA, November 2024. Association
for Computational Linguistics.
doi: 10.18653/v1/2024.emnlp-main.18.
URL https:
//aclanthology.org/2024.emnlp-main.18/.
W. James and Charles Stein. Estimation with quadratic loss. In Proceedings of the Fourth
Berkeley Symposium on Mathematical Statistics and Probability, Volume 1: Contribu-
tions to the Theory of Statistics, pages 361–379, Berkeley, California, 1961. University of
California Press.
Saurav Kadavath, Tom Conerly, Amanda Askell, Tom Henighan, Dawn Drain, Ethan Perez,
Nicholas Schiefer, Zac Hatfield-Dodds, Nova DasSarma, Eli Tran-Johnson, Scott John-
ston, Sheer El-Showk, Andy Jones, Nelson Elhage, Tristan Hume, Anna Chen, Yuntao
Bai, Sam Bowman, Stanislav Fort, Deep Ganguli, Danny Hernandez, Josh Jacobson,
Jackson Kernion, Shauna Kravec, Liane Lovitt, Kamal Ndousse, Catherine Olsson, Sam
Ringer, Dario Amodei, Tom Brown, Jack Clark, Nicholas Joseph, Ben Mann, Sam Mc-
Candlish, Chris Olah, and Jared Kaplan. Language models (mostly) know what they
know.
arXiv preprint arXiv:2207.05221, 2022.
URL https://arxiv.org/abs/2207.
05221.
Zhewei Kang, Xuandong Zhao, and Dawn Song. Scalable best-of-n selection for large lan-
guage models via self-certainty. In Advances in Neural Information Processing Systems
38 (NeurIPS 2025), 2025. URL https://arxiv.org/abs/2502.18581.
21

<!-- PDF PAGE 22/23 -->
Ko
David
R.
Karger,
Sewoong
Oh,
and
Devavrat
Shah.
Iterative
learning
for
reliable
crowdsourcing
systems.
In
Advances
in
Neural
Information
Pro-
cessing
Systems
24
(NIPS
2011),
pages
1953–1961.
Curran
Associates,
Inc.,
2011.
URL
https://proceedings.neurips.cc/paper_files/paper/2009/hash/
f899139df5e1059396431415e770c6dd-Abstract.html.
Junseok Kim, Nakyeong Yang, Kyungmin Min, and Kyomin Jung. Reliability-aware adap-
tive self-consistency for eﬀicient sampling in LLM reasoning. In Findings of the Associa-
tion for Computational Linguistics: ACL 2026, pages 21575–21590, San Diego, California,
United States, July 2026. Association for Computational Linguistics. doi: 10.18653/v1/
2026.findings-acl.1085. URL https://aclanthology.org/2026.findings-acl.1085/.
Leslie Kish. Survey Sampling. John Wiley & Sons, New York, 1965.
Lorenz Kuhn, Yarin Gal, and Sebastian Farquhar. Semantic uncertainty: Linguistic in-
variances for uncertainty estimation in natural language generation. In The Eleventh
International Conference on Learning Representations (ICLR), 2023.
Joonhyuk Lee, Virginia Ma, Sarah Zhao, Yash Nair, Asher Spector, Regev Cohen, and
Emmanuel J. Candès. FUSE: Ensembling verifiers with zero labeled data, 2026. URL
https://arxiv.org/abs/2604.18547.
Yifei Li, Zeqi Lin, Shizhuo Zhang, Qiang Fu, Bei Chen, Jian-Guang Lou, and Weizhu
Chen.
Making language models better reasoners with step-aware verifier.
In Pro-
ceedings of the 61st Annual Meeting of the Association for Computational Linguis-
tics (Volume 1:
Long Papers), pages 5315–5333, Toronto, Canada, July 2023. As-
sociation for Computational Linguistics.
doi:
10.18653/v1/2023.acl-long.291.
URL
https://aclanthology.org/2023.acl-long.291/.
Yiwei Li, Peiwen Yuan, Shaoxiong Feng, Boyuan Pan, Xinglin Wang, Bin Sun, Heda Wang,
and Kan Li. Escape sky-high cost: Early-stopping self-consistency for multi-step reason-
ing. In The Twelfth International Conference on Learning Representations (ICLR), 2024.
URL https://arxiv.org/abs/2401.10480.
Hunter Lightman, Vineet Kosaraju, Yura Burda, Harri Edwards, Bowen Baker, Teddy Lee,
Jan Leike, John Schulman, Ilya Sutskever, and Karl Cobbe. Let’s verify step by step. In
The Twelfth International Conference on Learning Representations (ICLR), 2024. URL
https://arxiv.org/abs/2305.20050.
Fabio Parisi, Francesco Strino, Boaz Nadler, and Yuval Kluger. Ranking and combining
multiple predictors without labeled data. Proceedings of the National Academy of Sci-
ences, 111(4):1253–1258, 2014. doi: 10.1073/pnas.1219097111.
J. N. K. Rao and A. J. Scott. The analysis of categorical data from complex sample surveys:
Chi-squared tests for goodness of fit and independence in two-way tables. Journal of the
American Statistical Association, 76(374):221–230, 1981. doi: 10.1080/01621459.1981.
10477633.
22

<!-- PDF PAGE 23/23 -->
Trust-Anchored Confidence Tempering
Amir Taubenfeld, Tom Sheffer, Eran Ofek, Amir Feder, Ariel Goldstein, Zorik Gekhman,
and Gal Yona. Confidence improves self-consistency in LLMs. In Findings of the Associa-
tion for Computational Linguistics: ACL 2025, pages 20090–20111, Vienna, Austria, July
2025. Association for Computational Linguistics.
doi: 10.18653/v1/2025.findings-acl.
1030. URL https://aclanthology.org/2025.findings-acl.1030/.
Katherine Tian, Eric Mitchell, Allan Zhou, Archit Sharma, Rafael Rafailov, Huaxiu Yao,
Chelsea Finn, and Christopher Manning. Just ask for calibration: Strategies for eliciting
calibrated confidence scores from language models fine-tuned with human feedback. In
Proceedings of the 2023 Conference on Empirical Methods in Natural Language Process-
ing, pages 5433–5442, Singapore, December 2023. Association for Computational Linguis-
tics. doi: 10.18653/v1/2023.emnlp-main.330. URL https://aclanthology.org/2023.
emnlp-main.330/.
Ph. van Elteren. On the combination of independent two sample tests of Wilcoxon. Bulletin
of the International Statistical Institute, 37:351–361, 1960.
Xuezhi Wang, Jason Wei, Dale Schuurmans, Quoc Le, Ed Chi, Sharan Narang, Aakanksha
Chowdhery, and Denny Zhou. Self-consistency improves chain of thought reasoning in
language models. In The Eleventh International Conference on Learning Representations
(ICLR), 2023. URL https://arxiv.org/abs/2203.11171.
Jacob Whitehill, Paul Ruvolo, Tingfan Wu, Jacob Bergsma, and Javier Movellan. Whose
vote should count more: Optimal integration of labels from labelers of unknown expertise.
In Advances in Neural Information Processing Systems 22 (NIPS 2009), pages 2035–2043.
Curran Associates, Inc., 2009. URL https://proceedings.neurips.cc/paper_files/
paper/2009/hash/f899139df5e1059396431415e770c6dd-Abstract.html.
Yunhui Xia, Wei Shen, Yan Wang, Jason Klein Liu, Huifeng Sun, Siyue Wu, Jian Hu, and
Xiaolong Xu. LeetCodeDataset: A temporal dataset for robust evaluation and eﬀicient
training of code LLMs. arXiv:2504.14655, 2025.
Miao Xiong, Zhiyuan Hu, Xinyang Lu, Yifei Li, Jie Fu, Junxian He, and Bryan Hooi. Can
llms express their uncertainty? an empirical evaluation of confidence elicitation in llms. In
The Twelfth International Conference on Learning Representations (ICLR), 2024. URL
https://arxiv.org/abs/2306.13063.
23
