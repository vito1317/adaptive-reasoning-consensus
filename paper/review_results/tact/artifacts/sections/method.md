method can act on, where the plurality is wrong and
the correct answer is present in the pool and the signal
is separable, occupied 2–5% of items at every diﬀiculty
level: as items harden, they pass directly from saturated
(plurality right) to capability-limited (the correct answer
never sampled: 0 of 6 plurality-wrong AIME items had it
in 16 draws), and the addressable band between the two
regimes does not widen. Classifying all 16 decisive items by
error shape, 7 were stable-wrong (a tight wrong cluster, the
two-world regime where no label-free signal can help) and
9 were scattered (6–8 distinct answers, a capability wall
that diversity interventions cannot cross, since diversity is
already maximal). Under this accounting, abstention is not
a conservative compromise but the only correct default:
on the confirmatory substrate the largest measured effect
of acting anyway was negative (the best-single-confidence
baseline loses 4.5 points where tact’s dead zone holds it
exactly at the sc floor).
The natural hypothesis is that the window widens
wherever an external anchor is cheap, since a passing
test is a real per-sample signal rather than a model-
relative one. That hypothesis was tested and does not
hold. On 40 LeetCode Medium/Hard problems [28] with 8
candidate solutions each, graded against the benchmark’s
own hidden suites, the window (oracle minus the largest-
behavioural-cluster baseline) measures 3/40 = 7.5% (CI95
2.6–19.9%), against 3.56% recomputed from published
HumanEval+/MBPP+ tables and 2–5% for label-free
QA. The composition is the same shape as well: 75%
saturated, 18% capability wall, 8% rescuable. Raising the
candidate budget does not open it: the seven capability-
wall problems produced zero correct solutions in 224
further attempts (per-problem 95% upper bound on the
pass rate 0.088), and extrapolating oracle@N shows the
window saturating by N=32. Executable ground truth
buys a slightly wider window, not a different regime. One
precaution deserves reporting with that number, since it
nearly inverted it: the grading harness was first validated
against the benchmark’s own reference solutions, of which
178 of 180 pass under the sandbox’s resource limits.
An earlier version of the same harness failed 100% of
executions because the host rejects one of the requested
limits outright, a condition that surfaces as a candidate
failure rather than as an error. Any study that grades
by execution should report its reference-solution pass
rate for the same reason a calibration curve is reported:
without it, a broken harness and a capability wall are
indistinguishable.
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
of thought reasoning in language models,” in Proc. ICLR, 2023.
[2] A. Taubenfeld et al., “Confidence improves self-consistency in
LLMs,” in Findings of ACL, 2025, arXiv:2502.06233.
[3] P. Aggarwal, A. Madaan, Y. Yang, and Mausam, “Let’s sample
step by step: Adaptive-consistency for eﬀicient reasoning and
coding with LLMs,” in Proc. EMNLP, 2023, pp. 12375–12396.
[4] Y.
Li
et
al.,
“Escape
sky-high
cost:
Early-stopping
self-
consistency for multi-step reasoning,” in Proc. ICLR, 2024.
[5] S. Kadavath et al., “Language models (mostly) know what they
know,” arXiv:2207.05221, 2022.
[6] K. Tian et al., “Just ask for calibration: Strategies for eliciting
calibrated confidence scores from language models fine-tuned
with human feedback,” in Proc. EMNLP, 2023.
[7] M. Xiong et al., “Can LLMs express their uncertainty? An
empirical evaluation of confidence elicitation in LLMs,” in Proc.
ICLR, 2024.
[8] X. Huang, S. Li, M. Yu, M. Sesia, H. Hassani, I. Lee, O. Bastani,
and E. Dobriban, “Uncertainty in language models: Assessment
through rank-calibration,” in Proc. EMNLP, 2024, pp. 284–312.
[9] Y. Li et al., “Making language models better reasoners with
step-aware verifier,” in Proc. ACL, 2023.
[10] Z. Kang, X. Zhao, and D. Song, “Scalable best-of-N selection
for large language models via self-certainty,” in Proc. NeurIPS,
2025, arXiv:2502.18581.
[11] J. Kim, N. Yang, K. Min, and K. Jung, “Reliability-aware adap-
tive self-consistency for eﬀicient sampling in LLM reasoning,”
in Findings of ACL, 2026, pp. 21575–21590.
[12] Y. Fu et al., “Deep think with confidence,” arXiv:2508.15260,
2025.
[13] A. P. Dawid and A. M. Skene, “Maximum likelihood estimation
of observer error-rates using the EM algorithm,” J. Roy. Statist.
Soc. C, vol. 28, no. 1, pp. 20–28, 1979.
[14] J. Whitehill et al., “Whose vote should count more: Optimal
integration of labels from labelers of unknown expertise,” in
Proc. NeurIPS, 2009.
[15] D. R. Karger, S. Oh, and D. Shah, “Iterative learning for reliable
crowdsourcing systems,” in Proc. NeurIPS, 2011.
[16] F. Parisi, F. Strino, B. Nadler, and Y. Kluger, “Ranking and
combining multiple predictors without labeled data,” Proc.
Natl. Acad. Sci., vol. 111, no. 4, pp. 1253–1258, 2014.
[17] J. Lee, V. Ma, S. Zhao, Y. Nair, A. Spector, R. Cohen, and E. J.
Candès, “FUSE: Ensembling verifiers with zero labeled data,”
arXiv:2604.18547, 2026.
[18] R. Ai, Y. Pan, D. Simchi-Levi, M. Tambe, and H. Xu, “Beyond
majority voting: LLM aggregation by leveraging higher-order
information,” arXiv:2510.01499, 2025, accepted to ICML 2026.
[19] P. van Elteren, “On the combination of independent two-sample
tests of Wilcoxon,” Bull. Int. Statist. Inst., vol. 37, pp. 351–361,
1960.

[20] W. James and C. Stein, “Estimation with quadratic loss,” in
Proc. 4th Berkeley Symp. Math. Statist. Prob., 1961, pp. 361–
379.
[21] L. Kish, Survey Sampling. New York, NY, USA: Wiley, 1965.
[22] J. N. K. Rao and A. J. Scott, “The analysis of categorical data
from complex sample surveys,” J. Amer. Statist. Assoc., vol. 76,
no. 374, pp. 221–230, 1981.
[23] K. Cobbe et al., “Training verifiers to solve math word prob-
lems,” arXiv:2110.14168, 2021.
[24] L. Kuhn, Y. Gal, and S. Farquhar, “Semantic uncertainty:
Linguistic invariances for uncertainty estimation in natural
language generation,” in Proc. ICLR, 2023.
[25] G. Wan, Y. Wu, J. Chen, and S. Li, “Reasoning aware self-
consistency: Leveraging reasoning paths for eﬀicient LLM sam-
pling,” in Proc. NAACL, 2025, pp. 3613–3635.
[26] D. Hendrycks et al., “Measuring mathematical problem solving
with the MATH dataset,” in Proc. NeurIPS Datasets and
Benchmarks, 2021.
[27] H. Lightman et al., “Let’s verify step by step,” in Proc. ICLR,
2024. (MATH-500 test subset.)
[28] Y. Xia et al., “LeetCodeDataset: A temporal dataset for
robust