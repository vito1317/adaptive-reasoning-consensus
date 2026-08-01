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