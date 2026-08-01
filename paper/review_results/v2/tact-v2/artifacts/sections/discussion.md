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