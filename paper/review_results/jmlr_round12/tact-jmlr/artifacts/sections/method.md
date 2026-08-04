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
gated set is empty for any channel, whereas here the cut is 0.875 and the set is non-empty,
so the alarm reports a genuine shortfall against the floor. Only the first is a defect.
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
rescuable, i.e. 75/17.5/7.5%. Nor does budget open it. The seven capability-wall problems
produced zero correct solutions in 224 further attempts (per-problem 95% upper bound on
the pass rate 0.088), and extrapolating oracle@N shows the window saturating by N=32.
One precaution belongs with these numbers, because omitting it would have inverted
them. The grading harness was validated against the benchmark’s own reference solutions
before any candidate was scored: 178 of 180 pass under the sandbox’s resource limits. The
check is not a formality: a sandbox whose resource limits the host rejects outright fails 100%
of executions, and that condition presents as a candidate failure, not an error. Studies that
grade by execution should report their reference-solution pass rate for the same reason
a calibration curve is reported: without it, a broken harness and a capability wall look
identical.
19

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
over the 89-item evaluation set that remains after the sign set is split off (10 and 4
items, so 11.2 and 4.5). The last row is that same MATH L5 substrate under the
budget manipulation of Section 8.10, not a sixth substrate: the 2.5–7.5% range
quoted throughout is over the five above it.
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
fell 0.924 →0.815, the window widened from 2.5% to 11.8% (paired exact McNemar on
window membership, 13 in and 2 out, p = 0.0037), and the channel grew stronger, bD from
+0.229 (z = 2.69) to +0.398 (z = 6.76). Forced to answer without working, the model’s
confidence tracks whether it happened to be right.
This is the widest window measured anywhere in this paper, and the first substrate
on which the in-pool oracle clears the endpoint at all (+9/ −0, p = 0.002 on a decisive
stratum of 17). tact nonetheless returned γ = 0: only 12 items survived the margin gate
against the threshold of 30, so E4 fired—the same item-supply condition, with the quantile
cut at 0.875 and the gated set again non-empty, and not the degenerate case finding (f)
reports. That abstention is testable, and it cost nothing. Estimating γ from gold labels, an
upper bound no deployable method has access to, the best available is +4/ −1 at γ = 1
20

Trust-Anchored Confidence Tempering
(p = 0.19); the derived γ = 0.670 gives +3/ −1. The gap that matters is therefore not
the one the window closes. Even with the window at 11.8% and an oracle able to convert
nine items, confidence weighting reaches fewer than half of them, and none of the reachable
configurations is significant.
9 Discussion and Limitations
What the evidence does and does not show.
The accuracy claims are all on a
synthetic oracle whose confidence model (1) is, at the homogeneous cells, the very coupling
the estimator measures. Three design choices limit the circularity, and the first is weaker
than it looks: heterogeneity and echo lie outside the estimator’s working model, but the
three distortion cells are rank-preserving by construction and therefore sit inside tact’s
own invariance group, so passing them shows only that the implementation respects an
invariance it was built to have; mechanism-recovery claims (does bD track κ?) are reported
separately from accuracy claims; and the pre-measured baseline landscape (Fig. 1) fixed the
winnable cells before the method existed. The real-trace campaigns of Sections 8.7 and 8.8
test the premise and the abstention behaviour, and both predictions held: the channel is null
on saturated benchmarks and positive on competition mathematics, and the dead zone kept
the vote bit-identical to sc in each case. They do not test the accuracy claim, because on
neither substrate was the addressable stratum large enough for any method to demonstrate
a gain (Section 8.9).
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
is plausible, the semi-label-free mode (sign from ∼50 labels) should be the default, and
treating it as an optional refinement is the mistake. The other standard remedy is not tried
here and should be: the failure is driven by a semantically tight wrong cluster that lexical
deduplication cannot see, which is precisely what semantic-equivalence clustering (Kuhn
et al., 2023) is built to collapse. Substituting a semantic pseudo-label for the lexical one is
the obvious next guard, and this paper does not test it.
Global exponent per group. Within a group, tact ships one exponent; per-item
variation inside a group is unexploitable by Propositions 5–8 unless further covariates exist.
The thin window. Section 8.9 measures the stratum this whole family of methods can
act on at 2.5–7.5% of items across all five substrates, in two domains, with no widening as
21

Ko
items harden: they pass from saturated straight to capability-limited. Two consequences
follow for the method proposed here. First, abstention is not a conservative compromise but
the only correct default, and the measured cost of acting anyway was negative on both real
substrates (best-single-confidence loses 4.5 points in Table 5 where the dead zone holds tact
at the sc floor). Second, an aggregation gain of the size reported on the synthetic harness
is not measurable on a benchmark of a few hundred items at these window widths, which is
why the real-trace claim in this paper is confined to the premise (the channel exists and is
signed) and to the abstention behaviour, and does not extend to accuracy. Demonstrating
the gain needs a (model, benchmark) pair whose plurality is wrong on 30–60% of items
with the correct answer still reachable, and no pair tried here satisfies both. Section 8.10
adds the one axis that does widen the window, and it cuts the same way: with the window
at 11.8% and an oracle able to convert nine items, confidence weighting still reaches fewer
than half of them. The width of the window is not the only thing in the way.
Widening the window on purpose. That result also names the most promising
direction the paper does not pursue.
Diﬀiculty moves items from saturated straight to
capability-limited, but the budget constraint of Section 8.10 moved them across the plurality
boundary while leaving the answer inside the model’s competence, which is the combination
the decisive stratum needs; sampling temperature is a second knob with the same character,
and neither was swept. If the sampling regime is a controllable input, not a fixed property
of the substrate, the question changes from “how wide is the window?” to “what decoding
configuration puts the most items in it, at what accuracy cost, and does the confidence
channel stay signed there?” The budget arm answers the first part once and suggests the
channel gets stronger under the constraint ( bD from +0.229 to +0.398), which would be
worth confirming on more than one substrate before it is believed. A method that chose
its own decoding budget to maximise decisive-stratum mass, then aggregated, would be
a different contribution from this one, and the measurement here is what makes it worth
attempting.
10 Conclusion
tact turns “how far should this model’s confidence be trusted?” into a measured, signed,
uncertainty-aware scalar, and recovers the sign without labels under conditions this paper
states and tests. The measurement that frames it matters more than the estimator: across
five substrates in two domains, the stratum on which any label-free aggregation method
can act is 2.5–7.5% of items, and on both real substrates the in-pool oracle cannot clear
a pre-registered endpoint. In that regime the useful property of an estimator is knowing
when not to act, which the dead zone does exactly.
Code and Data Availability
All code, cached traces, and the JSON artifacts behind every table are at https:
//github.com/vito1317/adaptive-reasoning-consensus.
Table 4 is produced by
pytest at commit 35ad160; the synthetic results by experiments/run_tact_eval.py,
the real-trace campaigns by run_tact_hard_eval.py, and the window measurements by
run_g1_window.py and run_g1_deepening.py; the three abstention replays of finding (e)
22

Trust-Anchored Confidence Tempering
by run_abstention_identifiability.py; the planted-channel operating characteristic
of finding (f) by run_planted_sensitivity.py. Each script writes the artifact its table
cites. Figures 1–4 are vector output from experiments/make_paper_figures.py, which
reads the same JSON.
23

Ko
24

Trust-Anchored Confidence Tempering
Appendix A. Notation
Table 7: Symbols, in order of first use. Quantities carrying a subscript q are per item; the
estimator ships one global scalar unless a group covariate is available (Section 6).
Symbol
Meaning
q, Q
item index; number of items
mq, K
traces available for item q; voting bud-
get
aq,i, a∗
q
answer of trace i; the correct answer
cq,i
self-reported confidence, in (0, 1)
yq,i
1[aq,i = a∗
q]; unobservable at test time
¯p
base rate of correct traces
Rq,i
within-item midrank of cq,i (ties aver-
aged)
φq,i
standardized van der Waerden score of
Rq,i; the vote feature
σq
realized within-item SD of the normal
scores
γ, γmax
vote exponent; its cap (4 dev, 2 label-
free)
ˆaq
the returned answer
Dq
Somers’ D within item q, = 2 AUCq −
1 = 2 WQDq −1
Nq
van Elteren pooling weight, n1
qn0
q
bD
pooled signed discrimination
SE0, SEJ
exact tie-corrected null SE; delete-one-
item jackknife SE
SE
max{SE0, SEJ, 1/(2
√
N)}
ζ
bD/SE; the dead zone is |ζ| ≤ν
ν
significance floor (1.28 dev, 2.33 label-
free)
˜D
shrunk discrimination, bD(1 −ν2/ζ2)+
z
Φ−1 
(1 + ˜D)/2

Mq
dedup-weighted plurality; the pseudo-
label
gq,i
1[aq,i = Mq]
¯ρ
pair-weighted probability the plurality
is wrong
ˆη
estimated attenuation 1 −2¯ρ (not ¯ρ)
α, k
split-half agreement; effective number
of wrong alternatives
E1 . . . E4
the four alarms; any one forces γ = 0
ψ
margin-decoupling statistic behind E2
κc
true confidence–correctness coupling in
the oracle (1)
λq
per-item coupling under i.i.d. hetero-
geneity
25

Ko
References
Pranjal Aggarwal, Aman Madaan, Yiming Yang, and Mausam. Let’s sample step by step:
Adaptive-consistency for eﬀicient reasoning and coding with LLMs. In Proceedings of the
2023 Conference on Empirical Methods in Natural Language Processing, pages 12375–
12396, Singapore, December 2023. Association for Computational Linguistics.
URL
https://aclanthology.org/2023.emnlp-main.761/.
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
26

Trust-Anchored Confidence Tempering
Ringer, Dario Amodei, Tom Brown, Jack Clark, Nicholas Joseph, Ben Mann, Sam Mc-
Candlish, Chris Olah, and Jared Kaplan. Language models (mostly) know what they
know.
arXiv preprint arXiv:2207.05221, 2022.
URL https://arxiv.org/abs/2207.
05221.
Zhewei Kang, Xuandong Zhao, and Dawn Song. Scalable best-of-n selection for large lan-
guage models via self-certainty. In Advances in Neural Information Processing Systems
38 (NeurIPS 2025), 2025. URL https://arxiv.org/abs/2502.18581.
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
27

Ko
Fabio Parisi, Francesco Strino, Boaz Nadler, and Yuval Kluger. Ranking and combining
multiple predictors without labeled data. Proceedings of the National Academy of Sci-
ences, 111(4):1253–1258, 2014. doi: 10.1073/pnas.1219097111.
J. N. K. Rao and A. J. Scott. The analysis of categorical data from complex sample surveys:
Chi-squared tests for goodness of fit and independence in two-way tables. Journal of the
American Statistical Association, 76(374):221–230, 1981. doi: 10.1080/01621459.1981.
10477633.
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
28