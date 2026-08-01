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