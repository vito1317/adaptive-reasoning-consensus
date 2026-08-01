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

<!-- === RAW LATEX SOURCE (tact.tex, verbatim) === -->

\documentclass[conference]{IEEEtran}
\usepackage{amsmath,amssymb,amsthm}
\usepackage{graphicx}
\usepackage{booktabs}
\usepackage{multirow}
\usepackage{url}
\usepackage[caption=false]{subfig}
\usepackage{balance}

\usepackage[hidelinks,breaklinks=true]{hyperref}
\usepackage{cleveref}

\newtheorem{proposition}{Proposition}
\newtheorem{remark}{Remark}

\newcommand{\Dhat}{\widehat{D}}
\newcommand{\sign}{\operatorname{sign}}
\newcommand{\SC}{\textsc{sc}}
\newcommand{\TACT}{\textsc{tact}}

% CJK author name: load a Unicode font directly (XeTeX/tectonic), keeping
% IEEEtran's Latin fonts untouched.
\font\zhfont="[/System/Library/Fonts/Supplemental/Arial Unicode.ttf]" at 10pt

\begin{document}

\title{TACT: Trust-Anchored Confidence Tempering for\\ Self-Consistency Voting in Large Language Models}

\author{\IEEEauthorblockN{Wei-Chen Ko ({\zhfont 柯瑋宸}, vito1317)}
\IEEEauthorblockA{Independent Researcher}}

\maketitle

\begin{abstract}
Confidence-weighted self-consistency (CISC and its successors) improves on majority voting when a frozen large language model's self-reported confidence is calibrated in \emph{direction}. Every published weighting scheme is structurally monotone increasing in confidence, so an anti-correlated channel poisons the vote instead of informing it, while binary dev-set gates survive inversion only by discarding genuinely discriminative signal. This paper presents \TACT{} (Trust-Anchored Confidence Tempering), which replaces the fixed confidence exponent with one \emph{derived} from the measured, signed, within-item discrimination of the channel: a pooled van~Elteren Somers' $D$ rank statistic with an item-clustered standard error, passed through positive-part James--Stein shrinkage and a Bayes-discriminant link. Written out, the method is a single expression whose exponent reduces to $\gamma=z\sqrt{2+z^2}$ with $z$ the probit of the shrunk pooled AUC, and it carries exact anchors: inside the shrinkage dead zone the vote is bit-identical to plain self-consistency, and a log-value feature map reproduces CISC-power. A label-free variant estimates the signed reliability from agreement pseudo-labels under a proven attenuation identity that guarantees sign consistency whenever the plurality-error rate is below one half, with conservative de-attenuation and echo alarms at the identifiability boundary. On a synthetic-oracle harness with paired trace pools, the label-free variant recovers anti-correlated channels that pin every published protocol to the majority-vote floor ($\kappa=-0.6$: $1.000$ vs.\ $0.807$), rank invariance beats the oracle over the entire raw-value weight family under monotone confidence compression ($1.000$ vs.\ $0.965$), and a per-group extension cracks the heterogeneity floor with zero paired losses to self-consistency ($0.940$ vs.\ $0.808$; $+79/-0$, $p=3.3\times10^{-24}$). Two real-trace campaigns on a frozen model confirm the premise and locate the binding constraint: within-item discrimination is positive on competition mathematics (pooled $\Dhat=+0.250$, $z=+2.54$), yet the stratum on which any such method can act, where the plurality is wrong and the correct answer is present in the pool, measures $2$--$7.5\%$ of items across five substrates in two domains, code generation with executable ground truth included. Abstention is therefore the correct default rather than a conservative one, and the dead zone implements it exactly. The paper further proves that per-item label-free adaptation is impossible under i.i.d.\ latent coupling, and pre-registers four falsification criteria, among them the published dev-calibrated CISC protocol as a designated killer baseline, all of which the method survived.
\end{abstract}

\begin{IEEEkeywords}
large language models, self-consistency, confidence calibration, weighted voting, label-free estimation, rank statistics
\end{IEEEkeywords}

\section{Introduction}

Self-consistency (\SC) \cite{wang2023selfconsistency} improves the reasoning accuracy of a frozen large language model (LLM) by sampling $K$ chain-of-thought traces and returning the plurality answer. Because each trace can also report a confidence score (verbalized \cite{tian2023just,xiong2024can}, derived from token log-probabilities, or elicited as $P(\text{True})$ \cite{kadavath2022language}), a natural refinement is to weight votes by confidence. Confidence-Informed Self-Consistency (CISC) \cite{taubenfeld2025cisc} showed that this recovers the accuracy of plain \SC{} at a fraction of the sampling budget, and introduced Within-Question Discrimination (WQD) to argue that \emph{discrimination}, not calibration, is the property that makes a confidence signal useful for voting.

This refinement carries a structural fragility that, to the author's knowledge, no published method addresses. Every existing weighting scheme is monotone \emph{increasing} in confidence, including CISC's softmax weights, reliability-aware pseudo-counts \cite{reasc2026}, and warmup-thresholded filtering \cite{deepconf2025}. The trust decision is which magnitude of up-weighting to apply; the possibility that the channel is \emph{anti-correlated} with correctness is not representable. Yet miscalibration of direction is not exotic: reinforcement fine-tuning is known to distort verbalized confidence, distribution shift can invert a signal that was informative in-domain, and in the experiments reported here a simple anti-correlated channel ($\kappa=-0.6$; Section~\ref{sec:setup}) drives confidence-weighted baselines from near-perfect accuracy to far below the majority-vote floor, while the same evidence, read with the correct sign, is a perfect signal. The defensive alternative, a binary dev-set gate that disables the channel when calibration error is high, survives the inversion but discards discriminative signal wholesale: a systematically under-confident yet perfectly ranked channel fails an ECE gate for reasons irrelevant to voting utility \cite{taubenfeld2025cisc,huang2024rankcalibration}.

This paper frames the problem as estimating one scalar: the \emph{signed} within-item discrimination of the confidence channel, and mapping that scalar, with its uncertainty, to a vote exponent. The contributions are:

\textbf{C1: Signed, analytically-tempered confidence weighting.} \TACT{} votes with weights $w_i=\exp(\gamma\,\varphi_i)$, where $\varphi_i$ is the standardized van der Waerden score of trace $i$'s within-item confidence midrank, and $\gamma$ is \emph{derived}, not grid-searched: a pooled van~Elteren Somers' $D$ statistic (equal to $2\cdot\mathrm{WQD}-1$) with an exact tie-corrected null variance and an item-clustered jackknife standard error, shrunk by positive-part James--Stein with a significance floor, then mapped through a Bayes-discriminant link with a mixture-variance correction. The construction carries exact anchors: inside the shrinkage dead zone the vote is \emph{bit-identical} to plain \SC{} (a shared code path), and the log-value feature map reproduces CISC-power exactly (Section~\ref{sec:method}). Because $\varphi$ depends on confidence only through within-item ranks, the entire method is invariant to every strictly monotone distortion of the confidence scale; under monotone compression it beats the oracle over the whole raw-value weight family ($1.000$ vs.\ $0.965$).

\textbf{C2: Label-free estimation of the signed reliability.} The crowdsourcing lineage estimates annotator reliability from cross-annotator covariance \cite{dawid1979maximum,parisi2014ranking}; a single exchangeable confidence channel from one model offers no such structure. The signed discrimination is estimated from \emph{agreement pseudo-labels} (deduplication-weighted plurality per item) with a proven class-conditional-noise attenuation identity, $\mathbb{E}[\Dhat_g]=(1-2\bar{\rho})\,D$: the label-free estimate can only \emph{under}-trust, never mis-sign, whenever the pair-weighted plurality-error rate $\bar{\rho}$ is below $1/2$. A split-half agreement inversion de-attenuates conservatively, and sign-aware alarms return the method to plain \SC{} when identifiability is threatened. On the coupling sweep the label-free variant matches the 200-label variant nearly point-for-point, including full recovery of negative channels (Section~\ref{sec:results}).

\textbf{C3: An impossibility result and its structured escape.} When the per-item coupling is i.i.d.\ with no observable covariate, per-item label-free adaptation is shown to be closed: any monotone use of an item's own agreement statistic collapses to plurality reinforcement; on exactly the plurality-wrong items where a flip could help, the observable sign opposes the truth $96\%$ of the time; and the two hypotheses $\{\kappa>0,\text{minority correct}\}$ and $\{\kappa<0,\text{plurality correct}\}$ induce identical observable laws. When heterogeneity is instead indexed by an observable covariate (domain-dependent calibration), running the same estimator per group recovers each group's signed coupling and approaches the per-item oracle with zero paired losses to \SC{} (Section~\ref{sec:hetero}).

\textbf{C4: A pre-registered falsification protocol.} Four falsifiers were fixed before implementation, including the two designed to kill the method: the \emph{published} dev-calibrated CISC protocol (whose tuned temperature already interpolates \SC$\leftrightarrow$CISC) and a trivial dev-picked signed exponent grid. All four survived, and the honest margins are reported: against the signed grid the net advantage concentrates in three cells: monotone distortion, confident echo, and label-free operation, which no grid can perform.

\section{Related Work}\label{sec:related}

\textbf{Confidence-weighted self-consistency.} \SC{} \cite{wang2023selfconsistency} treats sampled traces as i.i.d.\ votes. CISC \cite{taubenfeld2025cisc} weights votes by softmax-normalized confidence with a temperature tuned on a labeled split, and its WQD metric makes the discrimination-vs-calibration point that also motivates this work; the rank-calibration line \cite{huang2024rankcalibration} reaches the same conclusion independently. Weighted variants \cite{li2023diverse,borda2025} and early-stopping families \cite{aggarwal2023adaptive,li2024escape} refine the budget; reliability-aware pseudo-counts \cite{reasc2026} and warmup-thresholded filtering \cite{deepconf2025} adapt online but only re-scale positive trust. None of these can represent, much less estimate, a negative confidence--correctness association. The dev-calibrated variant must therefore be positioned honestly: CISC's tuned temperature is already a dev-calibrated \SC$\leftrightarrow$CISC interpolation, so the novelty of \TACT-dev lies in the sign, the rank invariance, and the analytic (grid-free) map, not in dev calibration itself.

\textbf{Reliability estimation without labels.} Estimating worker reliability from agreement is classical \cite{dawid1979maximum,whitehill2009whose,karger2011iterative}; spectral meta-learners \cite{parisi2014ranking} and recent LLM ensemble work \cite{fuse2026,beyondmajority2025} exploit covariance across \emph{multiple} predictors. The setting here differs: one exchangeable channel from one model, per-item vote structure, and the known failure of agreement proxies under correlated errors---met here with a quantified attenuation identity, conservative de-attenuation, and alarms in place of an unconditional claim.

\textbf{Shrinkage and rank statistics.} The estimator assembles classical parts: stratified rank statistics \cite{vanelteren1960}, the James--Stein positive-part estimator \cite{james1961estimation}, effective-sample-size corrections \cite{kish1965,rao1981analysis}, and normal-scores discriminant analysis. The claim is the assembly and its anchors, not the parts.

\textbf{Honest sibling result.} A preceding system by the author (RLEV-VoI, redundancy-discounted voting with value-of-information stopping) was evaluated under the same falsification discipline and \emph{failed} it, dominated everywhere by a simple deduplication baseline, and is reported as a negative result. Its post-mortem isolated the confidence dilemma studied here.

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
\includegraphics[width=\columnwidth]{figs/kappa_sweep.png}
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
which equals $2\cdot\mathrm{WQD}_q-1$ in CISC's notation. Pooling uses van Elteren pair-count weights $N_q=n^1_q n^0_q$ \cite{vanelteren1960}:
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
with dead zone $\{|r|\le\nu\}$; $\nu_{\mathrm{dev}}=1.28$, $\nu_{\mathrm{LF}}=2.33$. With $\nu=1$, \eqref{eq:js} is exactly the empirical-Bayes posterior mean under a $\mathcal{N}(0,\tau^2)$ prior with plug-in $\hat\tau^2=\max(0,\Dhat^2-\mathrm{SE}^2)$ \cite{james1961estimation}. The map is odd, continuous, never exceeds $|\Dhat|$, and is monotone in $\Dhat$ and anti-monotone in $\mathrm{SE}$.

\emph{Link.} Model $\varphi\,|\,y\sim\mathcal{N}(\mu_y,s^2)$ within item with the \emph{mixture} standardized to unit variance, which is what \eqref{eq:vdw} enforces, so $s^2=1/(1+\bar p(1-\bar p)u^2)$ where $u=\sqrt2\,\Phi^{-1}\!\big(\tfrac{1+\tilde D}{2}\big)$ and $\bar p$ is the base rate of correct traces. The Bayes-optimal per-trace log-weight coefficient is then
\begin{equation}\label{eq:link}
\gamma^\ast=\frac{u}{s}=u\sqrt{1+\bar p(1-\bar p)\,u^2},
\end{equation}
capped at $\gamma_{\max}$ ($4$ dev, $2$ label-free). The uncorrected link $\gamma=u$ under-weights strong channels by up to ${\sim}50\%$ at $D=0.9$.

\subsection{\TACT{} in one expression}\label{sec:oneline}
Two simplifications collapse the pipeline. Factoring $\Dhat$ out of
\eqref{eq:js} makes the shrinkage a multiplicative gain in the pooled
$z$-statistic $\zeta=\Dhat/\mathrm{SE}$ alone, and substituting
$u=\sqrt2\,z$ with $z=\Phi^{-1}\!\big(\tfrac{1+\tilde D}{2}\big)$ into
\eqref{eq:link} removes the nested radical. \TACT{} is then
\begin{equation}\label{eq:oneline}
\boxed{\;
\hat a_q=\arg\max_A \sum_{i:\,a_{q,i}=A}\exp\big(\gamma\,\varphi_{q,i}\big),
\quad
\gamma=\Big[z\sqrt{2+4\bar p(1-\bar p)z^{2}}\Big]_{-\gamma_{\max}}^{\gamma_{\max}},
\;}
\end{equation}
\begin{equation}\label{eq:oneline2}
z=\Phi^{-1}\!\Big(\tfrac12\big[1+\Dhat\,(1-\nu^{2}/\zeta^{2})_{+}\big]\Big),
\qquad \zeta=\Dhat/\mathrm{SE},
\end{equation}
with $\Dhat$ from \eqref{eq:pooled} and $\varphi$ from \eqref{eq:vdw}. At the
default $\bar p=\tfrac12$ the exponent is exactly
\begin{equation}\label{eq:half}
\gamma=z\sqrt{2+z^{2}},\qquad z=\Phi^{-1}(\widehat{\mathrm{AUC}}),
\end{equation}
one probit and one square root, with no tuned constant anywhere: $\nu$ is a
significance level and $\gamma_{\max}$ a clip, and both are fixed before any
data is seen. The dead zone is now visible as a single condition,
$|\zeta|\le\nu$, on which $\gamma$ is identically zero and \eqref{eq:oneline}
is bitwise \SC{} by Proposition~\ref{prop:sc}. Equations
\eqref{eq:oneline}--\eqref{eq:half} are verified equivalent to the shipped
implementation over randomised inputs including every boundary
(\texttt{tests/test\_formula.py}).

\subsection{Anchor properties}
\begin{proposition}[Exact \SC{} reduction]\label{prop:sc}
At $\gamma=0$, \eqref{eq:vote} equals plain \SC{} as a function on every trace pool, including tie-breaks. Under $D=0$, $P(\gamma=0)\to 2\Phi(\nu)-1$ ($80\%$ dev, $98\%$ label-free), and $\gamma$ is continuous through the dead-zone boundary, so a false positive applies an infinitesimal exponent.
\end{proposition}
\begin{proposition}[Exact CISC reduction]\label{prop:cisc}
With the feature map $\varphi^{\log}_{q,i}=\log c_{q,i}-\overline{\log c_q}$, the weights equal $\smash{\kappa_q\,c_{q,i}^{\,\gamma}}$ with a per-item constant $\kappa_q>0$; hence the argmax, the ties, and the normalized vote shares coincide with CISC-power$(\gamma)$ on every pool.
\end{proposition}
\begin{proposition}[Regularity]\label{prop:reg}
The composite $g(\Dhat,\mathrm{SE})$ is continuous, odd, nondecreasing in $\Dhat$, nonincreasing in $\mathrm{SE}$ in magnitude, with $g(D,0^+)=\gamma^\ast(D)$.
\end{proposition}
Proofs are elementary and pinned by unit tests in the released code (76 tests; the permutation-verified null variance, the EB identity in \eqref{eq:js}, and the link derivation \eqref{eq:link} are each tested numerically).

\section{Label-Free Estimation}\label{sec:lf}

\subsection{Pipeline}
(i)~\emph{Dedup:} single-linkage duplicate groups on the lexical-similarity channel at $0.95$; each trace gets weight $1/|\text{group}|$ for plurality determination and pair weighting. (ii)~\emph{Pseudo-label:} $g_{q,i}=\mathbf{1}[a_{q,i}=M_q]$ with $M_q$ the dedup-weighted plurality. (iii)~\emph{Margin gate:} keep the top $60\%$ of items by dedup-weighted margin. (iv)~Compute \eqref{eq:pooled} with $\mathrm{lab}=g$, giving $(\Dhat_g,\mathrm{SE}_g,r_g)$.

\subsection{Sign consistency and its boundary}
\begin{proposition}[Attenuation identity]\label{prop:ccn}
Let $\bar\rho$ be the pair-weighted probability that an item's plurality is wrong. If the plurality-error event is independent of $\varphi$ given $y$ (class-conditional noise), then
$\mathbb{E}[\Dhat_g]=(1-2\bar\rho)\,D$.
In particular $\sign\mathbb{E}[\Dhat_g]=\sign D$ whenever $\bar\rho<1/2$: the label-free estimate can only under-trust, never mis-sign.
\end{proposition}
The identity fails when the flip is \emph{caused} by confidence, that is, under a confident echo. There the observable law under $\{$majority right, $D<0\}$ and $\{$majority wrong via confident echo, $D>0\}$ is identical (the two-root ambiguity of \cite{parisi2014ranking} restated for a single channel), so any label-free guarantee is necessarily conditional; it is stated as such rather than papered over.

\subsection{De-attenuation and alarms}
Split-half agreement over $R{=}20$ random half-splits estimates $\alpha=p^2+(1-p)^2/k$ under a one-coin model with $k$ effective wrong alternatives (inverse-Simpson), inverted as $p=[1+\sqrt{1-(k{+}1)(1-k\alpha)}]/(k{+}1)$; $\Dhat_g$ is divided by the \emph{upper} $95\%$ bootstrap bound of $2p-1$ (floored at $0.2$), which can only under-inflate. Four alarms force $\gamma=0$: duplicate collapse (median Kish ratio $<0.5$), sign-aware margin-decoupling, root ambiguity in the split-half quadratic, and insufficient gated items. The margin-decoupling alarm must condition on the estimated trust direction: a sign-naive version (``plurality has the highest mean $\varphi$'') false-alarms on every benign anti-correlated channel---a defect the author hit, diagnosed, and fixed, and which the released tests pin. Finally the significance gate acts on the \emph{raw} $z$ (unbiased sign under Proposition~\ref{prop:ccn}) and temper on the de-attenuated value. A semi-label-free mode takes only the sign from ${\sim}50$ dev labels, routing it into the pipeline and disabling only the proxy-sign alarm; this purchases immunity to the ambiguity above at negligible labeling cost.

\section{Heterogeneity: Impossibility and Escape}\label{sec:hetero}

\subsection{Per-item adaptation is closed under i.i.d.\ coupling}
Suppose $\kappa_q\stackrel{\text{iid}}{\sim}\mathcal{N}(0,0.6^2)$ with no observable covariate.

\begin{proposition}[Self-reinforcement]\label{prop:selfreinf}
Any per-item rule $\gamma_q=h(\Dhat^g_q)$ with $h$ monotone increasing and odd reinforces the plurality on both branches: $\Dhat^g_q>0$ up-weights confident traces, which agree with the plurality; $\Dhat^g_q<0$ up-weights unconfident traces, which are again the plurality side. Empirically such a rule agrees with \SC{} on $97.5\%$ of items and its residual flips are net-harmful ($1$ right vs.\ $9$ wrong per $400$ items).
\end{proposition}

\begin{proposition}[Winner's curse]\label{prop:curse}
On plurality-wrong items with $|D_q|>0.3$, the items where a flip could win, the agreement statistic's sign matches the true sign only $4\%$ of the time.
\end{proposition}

\begin{proposition}[Two-world unidentifiability]\label{prop:twoworld}
For any observed $(a,c)$, the worlds $\{\kappa>0,\ \text{minority correct}\}$ and $\{\kappa<0,\ \text{plurality correct}\}$ induce identical observable laws (constructively, $D$ computed against either truth satisfies $D^{w_1}=-D^{w_2}$). No label-free method can separate them.
\end{proposition}

Consequently the per-item oracle ($0.983$ in this harness) is unreachable, and the honest behaviour is to fall back to the global estimate, which \TACT's dead zone does: in the i.i.d.\ cell every variant returns bitwise \SC{} (zero discordant pairs).

\subsection{TACT-group}
Real heterogeneity is typically indexed by an observable covariate (domain, question type). With $\kappa$ indexed by a group label, running the estimator per group keeps every group inside the operating regime of Sections~\ref{sec:method}--\ref{sec:lf}; groups with fewer than $30$ dev (or $60$ unlabeled) items fall back to the global estimate, which Propositions~\ref{prop:selfreinf}--\ref{prop:twoworld} show is the only defensible default.

\section{Experimental Setup}\label{sec:exp}

\textbf{Harness.} A cluster-mixture oracle generates, per item, up to $K_{\max}{=}20$ cached traces with answers, confidences \eqref{eq:confmodel}, and two similarity channels; all methods replay identical pools (paired comparisons, exact McNemar tests). Voting budget $K{=}15$; $400$ items per cell on the sweep, $600$ for the group study; dev splits of $200$ (primary) and $50$ (small-dev).

\textbf{Regimes.} The $\kappa$ sweep $\{-0.6,\dots,+0.6\}$; three strictly monotone confidence distortions (compression toward $0.5$, over-confident sigmoid, fourth power), rank-preserving by construction, so discrimination is intact while calibration is destroyed; i.i.d.\ heterogeneity ($\kappa_q\sim\mathcal{N}(0,0.6^2)$); covariate-structured heterogeneity (three groups at $+0.6/0/-0.6$); and a confident-echo poison (a wrong cluster echoes verbatim with confidence $0.95$).

\textbf{Baselines.} \SC; CISC-power with $\gamma\in\{0.25,\dots,4\}$; \emph{CISC-devT}, the published dev-calibrated protocol (positive grid picked on dev); a binary ECE gate; \emph{SignGrid-dev}, the strongest trivial baseline (signed exponent grid picked on dev); and the test-set oracle over signed fixed exponents as the upper envelope. The group study adds the naive self-referential per-item method as a negative control and the per-item link oracle as the ceiling.

\textbf{Pre-registered falsifiers.} F1: \TACT-dev significantly below the best fixed-$\gamma$ CISC at $\kappa{=}{+}0.6$. F2: either variant significantly below \SC{} anywhere on the sweep. F3: the label-free variant fails to beat the ECE gate on sweep average. F4: CISC-devT or SignGrid-dev matches \TACT-dev everywhere, including the distortion, heterogeneity, and small-dev cells.

\begin{table}[t]
\centering
\caption{Coupling sweep (accuracy at $K{=}15$; $400$ paired items per cell; dev $n{=}200$). Published protocols sit at the \SC{} floor on the entire negative half-axis.}
\label{tab:sweep}
\setlength{\tabcolsep}{3.4pt}
\begin{tabular}{r cc cc cc c}
\toprule
$\kappa$ & \SC & ECE & devT & SignGrid & \textbf{\TACT-dev} & \textbf{\TACT-LF} & oracle\\
\midrule
$-0.6$ & .807 & .807 & .807 & 1.000 & \textbf{1.000} & \textbf{1.000} & 1.000\\
$-0.4$ & .797 & .797 & .797 & 1.000 & \textbf{1.000} & \textbf{1.000} & 1.000\\
$-0.2$ & .835 & .835 & .835 & .993 & .978 & .978 & .993\\
$-0.1$ & .762 & .762 & .762 & .892 & .880 & .885 & .892\\
$0.0$  & .835 & .835 & .835 & .835 & .835 & .835 & .835\\
$+0.1$ & .795 & .795 & .917 & .917 & .902 & .902 & .917\\
$+0.2$ & .845 & .845 & .993 & .993 & .988 & .988 & .993\\
$+0.4$ & .838 & .838 & 1.000 & 1.000 & \textbf{1.000} & \textbf{1.000} & 1.000\\
$+0.6$ & .782 & .782 & 1.000 & 1.000 & \textbf{1.000} & \textbf{1.000} & 1.000\\
\bottomrule
\end{tabular}
\end{table}

\begin{figure}[t]
\centering
\includegraphics[width=\columnwidth]{figs/tact_sweep.png}
\caption{Main result on the confidence-usage frontier. \TACT-dev and the fully label-free \TACT-LF track the signed oracle across the sweep; CISC-devT and the ECE gate sit at the \SC{} floor for all $\kappa<0$.}
\label{fig:sweep}
\end{figure}

\section{Results}\label{sec:results}

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
Monotone compress & .795 & .965 & .965 & \textbf{1.000} & \textbf{1.000}\\
Monotone overconf & .795 & 1.000 & 1.000 & 1.000 & 1.000\\
Monotone power & .795 & 1.000 & 1.000 & 1.000 & 1.000\\
Hetero (i.i.d.) & .810 & .810 & .810 & .810 & .810\\
Confident echo & .200 & .200 & .550 & \textbf{.585} & .200$^{\dagger}$\\
\bottomrule
\multicolumn{6}{l}{\footnotesize $^{\dagger}$alarm fires and the method refuses to leave \SC---the conditional}\\
\multicolumn{6}{l}{\footnotesize guarantee of Prop.~\ref{prop:ccn} working as stated.}
\end{tabular}
\end{table}

\subsection{Rank invariance where raw values fail}
Under monotone compression (Table~\ref{tab:adv}, Fig.~\ref{fig:adv}) all confidences huddle near $0.5$, so every $c^{\gamma}$-family weight is nearly uniform: even the \emph{oracle} over raw-value policies reaches only $0.965$. \TACT's rank scores are untouched by the distortion and both variants reach $1.000$. Under the confident echo, dev labels reveal the inversion (high confidence $\Rightarrow$ wrong) and \TACT-dev counters with $\gamma=-1.20$, the best result in the field ($0.585$; three times the \SC{} floor); label-free, the duplicate-collapse alarm fires and the method correctly refuses---by Proposition~\ref{prop:twoworld} no label-free method could do better than a coin flip on the sign here, and pretending otherwise would be the real failure.

\begin{figure}[t]
\centering
\includegraphics[width=\columnwidth]{figs/tact_adversarial.png}
\caption{Adversarial regimes. Dotted line: the oracle over raw-value weights. Left group of bars: rank invariance beats that family under compression; right: the labeled variant counters the confident echo while the label-free variant alarms and refuses.}
\label{fig:adv}
\end{figure}

\subsection{Heterogeneity}
Table~\ref{tab:group} and Fig.~\ref{fig:group} give the group study. In the covariate-structured cell, per-group \TACT{} recovers each group's signed coupling (dev $\{+4.0,0.0,-4.0\}$, label-free $\{+2.0,0.0,-2.0\}$, the $\kappa{=}0$ group correctly dead-zoned---and cracks the floor that provably binds every global policy: the label-free variant reaches $0.940$, within $0.007$ of the per-item link oracle, with \emph{zero} paired losses to \SC{} over $600$ items ($+79/-0$, $p=3.3\times10^{-24}$). In the i.i.d.\ cell every legitimate method sits at the floor with zero discordant pairs, and the naive self-referential control lands slightly below it---the empirical face of Propositions~\ref{prop:selfreinf}--\ref{prop:twoworld}. One observation is reported as-is rather than tuned for: the label-free variant outperforms the dev variant in the grouped cell ($0.940$ vs.\ $0.923$) because its lower exponent cap ($2$ vs.\ $4$) regularizes better when $|D|\approx1$; cap robustness is left as an ablation.

\begin{table}[t]
\centering
\caption{Heterogeneity study ($600$ paired items; $K{=}15$).}
\label{tab:group}
\setlength{\tabcolsep}{4.5pt}
\begin{tabular}{l cc}
\toprule
Method & Grouped & i.i.d.\\
\midrule
\SC{} (floor) & .808 & .827\\
\TACT{} global (dev) & .808 & .827\\
\TACT-group (dev) & .923 & .827\\
\textbf{\TACT-group (label-free)} & \textbf{.940} & .827\\
Naive per-item (neg.\ control) & .803 & .820\\
Per-item link oracle (ceiling) & .947 & .983\\
\bottomrule
\end{tabular}
\end{table}

\begin{figure}[t]
\centering
\includegraphics[width=\columnwidth]{figs/group_eval.png}
\caption{Structured vs.\ i.i.d.\ heterogeneity. Left: with an observable covariate, per-group \TACT{} (label-free) approaches the per-item oracle from the $0.808$ floor with zero losses to \SC. Right: the provably closed i.i.d.\ cell---every legitimate method at the floor; the negative control slightly below it.}
\label{fig:group}
\end{figure}

\subsection{Small dev sets and falsifiers}
With dev $n{=}50$ the conclusions are unchanged ($1.000$ at $|\kappa|{=}0.6$; $0.978$ at $-0.2$): the SE-aware shrinkage degrades smoothly rather than catastrophically. All four falsifiers survived: F1 ($1.000$ vs.\ $1.000$), F2 (bit-identical at $\kappa{=}0$; never significantly below \SC{} elsewhere), F3 (sweep means $0.954$ vs.\ $0.811$), and F4 (the distortion and echo cells are unreachable by either grid baseline). Against SignGrid-dev the honest margin is narrow on the homogeneous sweep---\TACT{} even trails by $0.005$--$0.015$ in the mid-range, the deliberate cost of shrinkage---and the net advantage concentrates exactly where pre-registered: distortion ($+0.035$), echo ($+0.035$), and label-free operation, which no grid can perform.

\subsection{Verification of the implementation}\label{sec:tests}
Because every claim in Sections~\ref{sec:method}--\ref{sec:hetero} is a
mathematical property rather than an empirical trend, the released code pins
each one with an executable test; the suite is 76 tests for \TACT{} (84
including the follow-on work) and runs in 14 seconds. Table~\ref{tab:tests}
maps propositions to the tests that would fail if they stopped holding.

\begin{table}[t]
\centering
\caption{What the test suite verifies. Every proposition in the paper has an
executable counterpart; the counter-tests fail deliberately on rejected
alternatives so a regression cannot silently reinstate them.}
\label{tab:tests}
\setlength{\tabcolsep}{3.4pt}
\begin{tabular}{p{2.55cm} p{3.05cm} p{2.35cm}}
\toprule
Claim & Test & Evidence \\
\midrule
Prop.~\ref{prop:sc} (exact \SC) & \texttt{gamma\_zero\_is\_} \texttt{bitwise\_sc} & 200 random pools, identical incl.\ ties \\
Dead-zone rate & \texttt{dead\_zone\_} \texttt{probability} & $>$70\% under $D{=}0$, 300 trials \\
Prop.~\ref{prop:cisc} (exact CISC) & \texttt{logval\_phi\_} \texttt{reproduces\_cisc} & identical vote shares, 100 pools \\
Rank invariance & \texttt{monotone\_} \texttt{invariance} & 3 distortions $\times$ 100 pools \\
Null variance & \texttt{null\_variance\_} \texttt{matches\_permutation} & 3{,}000-draw permutation, 10\% tol.\ \\
JS--EB identity & \texttt{js\_eb\_identity} & exact to $10^{-12}$ \\
Link \eqref{eq:link} & \texttt{link\_values\_and\_} \texttt{mixture\_correction} & closed form, rel.\ $10^{-9}$ \\
Prop.~\ref{prop:ccn} (attenuation) & \texttt{poisoning\_} \texttt{attenuation\_linear} & $\rho\in\{.1,.25,.4\}$, abs.\ $.06$ \\
Props.~\ref{prop:selfreinf}--\ref{prop:twoworld} & \texttt{test\_tact\_group.py} & 97.5\% \SC{} agreement; 4\% sign match \\
Estimator permutation-invariance & \texttt{estimator\_is\_} \texttt{permutation\_invariant} & bypasses the memo (regression test) \\
Rejected: Kish ESS & \texttt{kish\_fails\_T2\_T3} & asserts the failure \\
Rejected: SAFE guarantee under VoI & \texttt{frozen\_default\_} \texttt{breaks\_guarantee} & asserts the violation \\
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

\subsection{Real-trace validation}\label{sec:real}
Validation on real traces used Claude Haiku 4.5 as the frozen model: 100 items
(50 GSM8K \cite{gsm8k2021}, 50 CommonsenseQA), \emph{12} independent
chain-of-thought traces per item with verbalized confidence (1{,}200 traces
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
\cite{math500,lightman2024verify}, $16$ traces each from the same frozen
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
to widen, $40$ LeetCode Medium/Hard problems \cite{leetcodedataset} were
solved $8$ times each and graded against the benchmark's hidden suites, with
the baseline taken as the largest behavioural cluster over probe inputs
(never expected outputs). The window is $3/40=7.5\%$ (CI$_{95}$
$2.6$--$19.9\%$): wider than label-free QA, but the same order, and the
composition is the same shape at $75\%$ saturated, $18\%$ capability wall,
$8\%$ rescuable. Nor does budget open it. The seven capability-wall problems
produced zero correct solutions in $224$ further attempts (per-problem $95\%$
upper bound on the pass rate $0.088$), and extrapolating oracle@$N$ shows the
window saturating by $N{=}32$.

\begin{table}[t]
\caption{The addressable stratum across substrates. Rows marked $\dagger$ are
measured here; HumanEval+/MBPP+ is recomputed from published oracle-minus-
selector tables. As items harden they pass from saturated to
capability-limited without the window widening.}
\label{tab:window}
\centering\footnotesize
\setlength{\tabcolsep}{4pt}
\begin{tabular}{l l c}
\toprule
Domain & Substrate & Window \\
\midrule
QA, label-free & GSM8K / CommonsenseQA$^\dagger$ & $12\%$ informative, $9\%$ decisive \\
QA, label-free & MATH level-5$^\dagger$ & $11\%$ decisive, $4\%$ rescuable \\
QA, label-free & AIME / AMC$^\dagger$ & $23\%$ decisive, $3\%$ rescuable \\
Code, executable & HumanEval+ / MBPP+ & $3.56\%$ \\
Code, executable & LeetCode Med/Hard$^\dagger$ & $7.5\%$ \\
\bottomrule
\end{tabular}
\end{table}

One precaution belongs with these numbers, because omitting it would have
inverted them. The grading harness was validated against the benchmark's own
reference solutions before any candidate was scored: $178$ of $180$ pass
under the sandbox's resource limits. An earlier version of the same harness
failed $100\%$ of executions because the host rejects one of the requested
limits outright, and that condition presents as a candidate failure rather
than as an error. Studies that grade by execution should report their
reference-solution pass rate for the same reason a calibration curve is
reported: without it, a broken harness and a capability wall look identical.

\section{Discussion and Limitations}\label{sec:limits}

\textbf{What the evidence does and does not show.} All quantitative claims are on a synthetic oracle whose confidence model \eqref{eq:confmodel} is, at the homogeneous cells, the very coupling the estimator measures. Three design choices limit the circularity: the adversarial regimes (distortions, heterogeneity, echo) lie outside the estimator's working model; mechanism-recovery claims (does $\Dhat$ track $\kappa$?) are reported separately from accuracy claims; and the pre-measured baseline landscape (Fig.~\ref{fig:baselines}) fixed the winnable cells before the method existed. Validation on real LLM traces is the remaining step; the cached-trace runner is committed and the prediction is falsifiable: if real confidence channels never exhibit directional miscalibration or covariate structure, \TACT's dead zone should make it operationally indistinguishable from CISC-devT there.

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
than an optional refinement.

\textbf{Global exponent per group.} Within a group, \TACT{} ships one exponent; per-item variation inside a group is unexploitable by Propositions~\ref{prop:selfreinf}--\ref{prop:twoworld} unless further covariates exist.

\textbf{The thin window.} Section~\ref{sec:window} measures the stratum this
whole family of methods can act on at $2$--$7.5\%$ of items on every substrate
tried, in two domains, with no widening as items harden: they pass from
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

\section{Conclusion}
\TACT{} turns ``how much should this model's confidence be trusted?'' into a measured, signed, uncertainty-aware quantity with exact fallbacks at both ends, plain self-consistency when the evidence is absent and CISC when it is at full strength, and shows that the sign, long unrepresentable in this family of methods, can be recovered without any labels under stated and tested conditions. The accompanying impossibility results draw the boundary that any future per-item method must respect, and the falsification protocol, having already killed one of the author's own systems, is offered as the more portable contribution.

\balance

\begin{thebibliography}{99}\itemsep 1pt

\bibitem{wang2023selfconsistency}
X.~Wang, J.~Wei, D.~Schuurmans, Q.~Le, E.~Chi, S.~Narang, A.~Chowdhery, and D.~Zhou, ``Self-consistency improves chain of thought reasoning in language models,'' in \emph{Proc.\ ICLR}, 2023.\ \url{https://arxiv.org/pdf/2203.11171}

\bibitem{taubenfeld2025cisc}
A.~Taubenfeld \emph{et~al.}, ``Confidence improves self-consistency in LLMs,'' in \emph{Findings of ACL}, 2025, arXiv:2502.06233.\ \url{https://aclanthology.org/2025.findings-acl.1030.pdf}

\bibitem{aggarwal2023adaptive}
P.~Aggarwal, A.~Madaan, Y.~Yang, and Mausam, ``Let's sample step by step: Adaptive-consistency for efficient reasoning and coding with {LLMs},'' in \emph{Proc.\ EMNLP}, 2023, pp. 12375--12396.\ \url{https://aclanthology.org/2023.emnlp-main.761.pdf}

\bibitem{li2024escape}
Y.~Li \emph{et~al.}, ``Escape sky-high cost: Early-stopping self-consistency for multi-step reasoning,'' in \emph{Proc.\ ICLR}, 2024.\ \url{https://arxiv.org/pdf/2401.10480}

\bibitem{kadavath2022language}
S.~Kadavath \emph{et~al.}, ``Language models (mostly) know what they know,'' arXiv:2207.05221, 2022.\ \url{https://arxiv.org/pdf/2207.05221}

\bibitem{tian2023just}
K.~Tian \emph{et~al.}, ``Just ask for calibration: Strategies for eliciting calibrated confidence scores from language models fine-tuned with human feedback,'' in \emph{Proc.\ EMNLP}, 2023.\ \url{https://aclanthology.org/2023.emnlp-main.330.pdf}

\bibitem{xiong2024can}
M.~Xiong \emph{et~al.}, ``Can LLMs express their uncertainty? An empirical evaluation of confidence elicitation in LLMs,'' in \emph{Proc.\ ICLR}, 2024.\ \url{https://openreview.net/pdf?id=gjeQKFxFpZ}

\bibitem{huang2024rankcalibration}
X.~Huang, S.~Li, M.~Yu, M.~Sesia, H.~Hassani, I.~Lee, O.~Bastani, and E.~Dobriban, ``Uncertainty in language models: Assessment through rank-calibration,'' in \emph{Proc.\ EMNLP}, 2024, pp. 284--312.\ \url{https://aclanthology.org/2024.emnlp-main.18.pdf}

\bibitem{li2023diverse}
Y.~Li \emph{et~al.}, ``Making language models better reasoners with step-aware verifier,'' in \emph{Proc.\ ACL}, 2023.\ \url{https://aclanthology.org/2023.acl-long.291.pdf}

\bibitem{borda2025}
Z.~Kang, X.~Zhao, and D.~Song, ``Scalable best-of-N selection for large language models via self-certainty,'' in \emph{Proc.\ NeurIPS}, 2025, arXiv:2502.18581.\ \url{https://proceedings.neurips.cc/paper_files/paper/2025/file/1c7eff166a8e345f664f0faa8f4e4d2e-Paper-Conference.pdf}

\bibitem{reasc2026}
J.~Kim, N.~Yang, K.~Min, and K.~Jung, ``Reliability-aware adaptive self-consistency for efficient sampling in LLM reasoning,'' in \emph{Findings of ACL}, 2026, pp. 21575--21590.\ \url{https://aclanthology.org/2026.findings-acl.1085.pdf}

\bibitem{deepconf2025}
Y.~Fu \emph{et~al.}, ``Deep think with confidence,'' arXiv:2508.15260, 2025.\ \url{https://arxiv.org/pdf/2508.15260}

\bibitem{dawid1979maximum}
A.~P. Dawid and A.~M. Skene, ``Maximum likelihood estimation of observer error-rates using the EM algorithm,'' \emph{J.\ Roy.\ Statist.\ Soc.\ C}, vol.~28, no.~1, pp. 20--28, 1979.\ \url{https://doi.org/10.2307/2346806}

\bibitem{whitehill2009whose}
J.~Whitehill \emph{et~al.}, ``Whose vote should count more: Optimal integration of labels from labelers of unknown expertise,'' in \emph{Proc.\ NeurIPS}, 2009.\ \url{https://proceedings.neurips.cc/paper_files/paper/2009/file/f899139df5e1059396431415e770c6dd-Paper.pdf}

\bibitem{karger2011iterative}
D.~R. Karger, S.~Oh, and D.~Shah, ``Iterative learning for reliable crowdsourcing systems,'' in \emph{Proc.\ NeurIPS}, 2011.\ \url{https://proceedings.neurips.cc/paper_files/paper/2011/file/c667d53acd899a97a85de0c201ba99be-Paper.pdf}

\bibitem{parisi2014ranking}
F.~Parisi, F.~Strino, B.~Nadler, and Y.~Kluger, ``Ranking and combining multiple predictors without labeled data,'' \emph{Proc.\ Natl.\ Acad.\ Sci.}, vol.~111, no.~4, pp. 1253--1258, 2014.\ \url{https://pmc.ncbi.nlm.nih.gov/articles/PMC3910607/pdf/pnas.201219097.pdf}

\bibitem{fuse2026}
J.~Lee, V.~Ma, S.~Zhao, Y.~Nair, A.~Spector, R.~Cohen, and E.~J. Cand\`es, ``FUSE: Ensembling verifiers with zero labeled data,'' arXiv:2604.18547, 2026.\ \url{https://arxiv.org/pdf/2604.18547}

\bibitem{beyondmajority2025}
R.~Ai, Y.~Pan, D.~Simchi-Levi, M.~Tambe, and H.~Xu, ``Beyond majority voting: LLM aggregation by leveraging higher-order information,'' arXiv:2510.01499, 2025, accepted to ICML 2026.\ \url{https://arxiv.org/pdf/2510.01499}

\bibitem{vanelteren1960}
P.~van Elteren, ``On the combination of independent two-sample tests of Wilcoxon,'' \emph{Bull.\ Int.\ Statist.\ Inst.}, vol.~37, pp. 351--361, 1960.\ \url{https://catalog.hathitrust.org/Record/008896012}

\bibitem{james1961estimation}
W.~James and C.~Stein, ``Estimation with quadratic loss,'' in \emph{Proc.\ 4th Berkeley Symp.\ Math.\ Statist.\ Prob.}, 1961, pp. 361--379.\ \url{https://digitalassets.lib.berkeley.edu/math/ucb/text/math_s4_v1_article-19.pdf}

\bibitem{kish1965}
L.~Kish, \emph{Survey Sampling}. New York, NY, USA: Wiley, 1965.\ \url{https://www.wiley.com/en-us/Survey+Sampling-p-9780471109495}

\bibitem{rao1981analysis}
J.~N.~K. Rao and A.~J. Scott, ``The analysis of categorical data from complex sample surveys,'' \emph{J.\ Amer.\ Statist.\ Assoc.}, vol.~76, no.~374, pp. 221--230, 1981.\ \url{https://doi.org/10.1080/01621459.1981.10477633}

\bibitem{gsm8k2021}
K.~Cobbe \emph{et~al.}, ``Training verifiers to solve math word problems,'' arXiv:2110.14168, 2021.

\bibitem{kuhn2023semantic}
L.~Kuhn, Y.~Gal, and S.~Farquhar, ``Semantic uncertainty: Linguistic invariances for uncertainty estimation in natural language generation,'' in \emph{Proc.\ ICLR}, 2023.\ \url{https://arxiv.org/pdf/2302.09664}

\bibitem{rasc2024}
G.~Wan, Y.~Wu, J.~Chen, and S.~Li, ``Reasoning aware self-consistency: Leveraging reasoning paths for efficient LLM sampling,'' in \emph{Proc.\ NAACL}, 2025, pp. 3613--3635.\ \url{https://aclanthology.org/2025.naacl-long.184.pdf}

\bibitem{math500}
D.~Hendrycks \emph{et~al.}, ``Measuring mathematical problem solving with the MATH dataset,'' in \emph{Proc.\ NeurIPS Datasets and Benchmarks}, 2021.\ \url{https://datasets-benchmarks-proceedings.neurips.cc/paper/2021/file/be83ab3ecd0db773eb2dc1b0a17836a1-Paper-round2.pdf}

\bibitem{lightman2024verify}
H.~Lightman \emph{et~al.}, ``Let's verify step by step,'' in \emph{Proc.\ ICLR}, 2024. (MATH-500 test subset.)

\bibitem{leetcodedataset}
Y.~Xia \emph{et~al.}, ``LeetCodeDataset: A temporal dataset for robust evaluation and efficient training of code LLMs,'' arXiv:2504.14655, 2025.\ \url{https://arxiv.org/pdf/2504.14655}

\end{thebibliography}

\end{document}


<!-- === PDF RENDERED TEXT (tact.pdf) === -->

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

<!-- PDF PAGE 2/9 -->
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
claim wins—monotone distortion of the confidence scale,
covariate heterogeneity, small dev sets, and label-free
operation—and the evaluation holds itself to exactly those
cells.

<!-- PDF PAGE 3/9 -->
Fig. 1.
The pre-measured problem statement: accuracy of baseline
confidence policies at fixed K=15 as the true coupling κ varies.
A trivial sign-corrected AUC gate (green) nearly saturates the
homogeneous sweep; the headroom for any new method (shaded)
concentrates in the mid-range and, off this plot, in distortion,
heterogeneity, and label-free cells.
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
one probit and one square root, with no tuned constant
anywhere: ν is a significance level and γmax a clip, and
both are fixed before any data is seen. The dead zone
is now visible as a single condition, |ζ| ≤ν, on which γ
is identically zero and (9) is bitwise sc by Proposition 1.
Equations (9)–(11) are verified equivalent to the shipped
implementation over randomised inputs including every
boundary (tests/test_formula.py).

<!-- PDF PAGE 4/9 -->
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
the released code (76 tests; the permutation-verified null
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
of [16] restated for a single channel), so any label-free
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
VII. Experimental Setup
Harness. A cluster-mixture oracle generates, per item,
up to Kmax=20 cached traces with answers, confidences
(1), and two similarity channels; all methods replay iden-
tical pools (paired comparisons, exact McNemar tests).

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
agreement statistic is bDg = −0.81 with z = −17.6, and the
CCN identity’s sign guarantee holds as predicted, yielding
1.000 with zero labels. Third, at κ = 0 the dead zone
returns γ = 0 exactly, so the paired accuracy difference
to sc is identically zero—“non-inferior” is replaced by
“identical.”
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

<!-- PDF PAGE 6/9 -->
Fig. 3.
Adversarial regimes. Dotted line: the oracle over raw-value
weights. Left group of bars: rank invariance beats that family under
compression; right: the labeled variant counters the confident echo
while the label-free variant alarms and refuses.
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
code pins each one with an executable test; the suite is 76
tests for tact (84 including the follow-on work) and runs
in 14 seconds. Table IV maps propositions to the tests
that would fail if they stopped holding.
Two
entries
deserve
comment.
The
permutation-
invariance test was added after a defect in which the
Fig. 4. Structured vs. i.i.d. heterogeneity. Left: with an observable
covariate, per-group tact (label-free) approaches the per-item oracle
from the 0.808 floor with zero losses to sc. Right: the provably closed
i.i.d. cell—every legitimate method at the floor; the negative control
slightly below it.
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
lems [26], [27], 16 traces each from the same frozen model,
a 30-item sign set and an 89-item evaluation set drawn
from the registered list before any trace was collected, and
five hypotheses (H1–H5) fixed in advance.
The channel is real. On the evaluation set the pooled
statistic is bD = +0.250 with SE = 0.098, so z = +2.54 and
H1 passes. This is the first real-trace evidence that verbal-
ized confidence carries positive within-item discrimination;
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
Define the window as the fraction of items where the
plurality is wrong and the correct answer is present in the
pool: the ceiling for any label-free aggregation method,
since nothing outside it can be changed.
The window was measured on five substrates spanning
two domains (Table VI). For code generation, where an
executable test suite supplies per-sample ground truth and
the window might reasonably be expected to widen, 40
LeetCode Medium/Hard problems [28] were solved 8 times
each and graded against the benchmark’s hidden suites,
with the baseline taken as the largest behavioural cluster
over probe inputs (never expected outputs). The window is
3/40 = 7.5% (CI95 2.6–19.9%): wider than label-free QA,
but the same order, and the composition is the same shape
at 75% saturated, 18% capability wall, 8% rescuable. Nor

<!-- PDF PAGE 8/9 -->
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
does budget open it. The seven capability-wall problems
produced zero correct solutions in 224 further attempts
(per-problem 95% upper bound on the pass rate 0.088),
and extrapolating oracle@N shows the window saturating
by N=32.
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
What the evidence does and does not show. All quan-
titative claims are on a synthetic oracle whose confidence
model (1) is, at the homogeneous cells, the very coupling
the estimator measures. Three design choices limit the
circularity: the adversarial regimes (distortions, hetero-
geneity, echo) lie outside the estimator’s working model;
mechanism-recovery claims (does bD track κ?) are reported
separately from accuracy claims; and the pre-measured
baseline landscape (Fig. 1) fixed the winnable cells before
the method existed. Validation on real LLM traces is
the remaining step; the cached-trace runner is committed
and the prediction is falsifiable: if real confidence chan-
nels never exhibit directional miscalibration or covariate
structure, tact’s dead zone should make it operationally
indistinguishable from CISC-devT there.
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
this whole family of methods can act on at 2–7.5% of
items on every substrate tried, in two domains, with
no widening as items harden: they pass from saturated
straight to capability-limited. Two consequences follow
for the method proposed here. First, abstention is not
a conservative compromise but the only correct default,
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
quantity with exact fallbacks at both ends, plain self-
consistency when the evidence is absent and CISC when
it is at full strength, and shows that the sign, long un-
representable in this family of methods, can be recovered
without any labels under stated and tested conditions. The
accompanying impossibility results draw the boundary
that any future per-item method must respect, and the
falsification protocol, having already killed one of the
author’s own systems, is offered as the more portable
contribution.
References
[1] X. Wang, J. Wei, D. Schuurmans, Q. Le, E. Chi, S. Narang,
A. Chowdhery, and D. Zhou, “Self-consistency improves chain

<!-- PDF PAGE 9/9 -->
of thought reasoning in language models,” in Proc. ICLR, 2023.
https://arxiv.org/pdf/2203.11171
[2] A. Taubenfeld et al., “Confidence improves self-consistency in
LLMs,” in Findings of ACL, 2025, arXiv:2502.06233. https://
aclanthology.org/2025.findings-acl.1030.pdf
[3] P. Aggarwal, A. Madaan, Y. Yang, and Mausam, “Let’s sample
step by step: Adaptive-consistency for eﬀicient reasoning and
coding with LLMs,” in Proc. EMNLP, 2023, pp. 12375–12396.
https://aclanthology.org/2023.emnlp-main.761.pdf
[4] Y.
Li
et
al.,
“Escape
sky-high
cost: Early-stopping
self-
consistency for multi-step reasoning,” in Proc. ICLR, 2024.
https://arxiv.org/pdf/2401.10480
[5] S. Kadavath et al., “Language models (mostly) know what
they know,” arXiv:2207.05221, 2022. https://arxiv.org/pdf/
2207.05221
[6] K. Tian et al., “Just ask for calibration: Strategies for elic-
iting calibrated confidence scores from language models fine-
tuned with human feedback,” in Proc. EMNLP, 2023. https:
//aclanthology.org/2023.emnlp-main.330.pdf
[7] M. Xiong et al., “Can LLMs express their uncertainty? An
empirical evaluation of confidence elicitation in LLMs,” in Proc.
ICLR, 2024. https://openreview.net/pdf?id=gjeQKFxFpZ
[8] X. Huang, S. Li, M. Yu, M. Sesia, H. Hassani, I. Lee, O. Bastani,
and E. Dobriban, “Uncertainty in language models: Assessment
through rank-calibration,” in Proc. EMNLP, 2024, pp. 284–312.
https://aclanthology.org/2024.emnlp-main.18.pdf
[9] Y. Li et al., “Making language models better reasoners with
step-aware verifier,” in Proc. ACL, 2023. https://aclanthology.
org/2023.acl-long.291.pdf
[10] Z.
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
[11] J. Kim, N. Yang, K. Min, and K. Jung, “Reliability-aware
adaptive self-consistency for eﬀicient sampling in LLM rea-
soning,” in Findings of ACL, 2026, pp. 21575–21590. https:
//aclanthology.org/2026.findings-acl.1085.pdf
[12] Y. Fu et al., “Deep think with confidence,” arXiv:2508.15260,
2025. https://arxiv.org/pdf/2508.15260
[13] A. P. Dawid and A. M. Skene, “Maximum likelihood estimation
of observer error-rates using the EM algorithm,” J. Roy. Statist.
Soc. C, vol. 28, no. 1, pp. 20–28, 1979. https://doi.org/10.2307/
2346806
[14] J.
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
[15] D.
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
[16] F. Parisi, F. Strino, B. Nadler, and Y. Kluger, “Ranking
and combining multiple predictors without labeled data,”
Proc. Natl. Acad. Sci., vol. 111, no. 4, pp. 1253–1258, 2014.
https://pmc.ncbi.nlm.nih.gov/articles/PMC3910607/pdf/
pnas.201219097.pdf
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
[24] L. Kuhn, Y. Gal, and S. Farquhar, “Semantic uncertainty:
Linguistic invariances for uncertainty estimation in natural
language generation,” in Proc. ICLR, 2023. https://arxiv.org/
pdf/2302.09664
[25] G. Wan, Y. Wu, J. Chen, and S. Li, “Reasoning aware
self-consistency: Leveraging reasoning paths for eﬀicient LLM
sampling,” in Proc. NAACL, 2025, pp. 3613–3635. https://
aclanthology.org/2025.naacl-long.184.pdf
[26] D.
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
[27] H. Lightman et al., “Let’s verify step by step,” in Proc. ICLR,
2024. (MATH-500 test subset.)
[28] Y. Xia et al., “LeetCodeDataset: A temporal dataset for
robust
evaluation
and
eﬀicient
training
of
code
LLMs,”
arXiv:2504.14655, 2025. https://arxiv.org/pdf/2504.14655
