# 深度审稿报告

**论文**: `/Users/vito/development/adaptive-reasoning-consensus/paper/tact.tex` | **语言**: EN | **模式**: deep-review
**生成时间**: 2026-08-02 01:13
**工件目录**: `/Users/vito/development/adaptive-reasoning-consensus/paper/review_results/v2/tact-v2`

## 总体评估

Round-2 re-audit of tact.tex at commit 4d75431, against the bundle raised on 62bc7c7. Ten root causes were fully closed and four partially, and in several cases the fix was better than the recommendation: the paper now discloses that the clip rather than the derived link sets the exponent in its headline cells, names the oracle's grid and states that the optimum sits at its boundary, scopes the CISC anchor to the log-value feature map, and has an internally consistent Limitations section. 38 findings remain: 10 major, 23 moderate, 5 minor. One is a mechanical submission blocker (still no code or data availability statement in a paper that delegates its proofs to a named test suite). Two were introduced by the revision itself: the new disclosure paragraph's gamma* = +/-38 recomputes to +/-12.1 with the paper's own gamma_of(), and the F4 sentence in Sec. V-D now contradicts the new paragraph one screen above it about whether the grid baselines reach the distortion and echo cells. Four claim-level residues live only in the abstract, and the honest wording for each already exists elsewhere in the manuscript.

- **主要**: 10
- **中等**: 23
- **次要**: 5

## 学术预审委员会

### 主编（直接拒稿筛查）

## Editor Pre-Screen (1-10)

Score: 5/10
Verdict: Conditional Pass

### Desk-Reject Triggers (if any)

- **No code or data availability statement anywhere in the manuscript, while the verification
  argument is explicitly delegated to code the reader cannot obtain.** Section V-F:
  "Proofs are elementary and pinned by unit tests in the released code (76 tests;". "Released"
  recurs in Sec. IV-B, V-C and VI-C; no URL, DOI, repository name, archive, or even an
  "available upon publication" sentence appears in nine pages. For a single-author submission
  whose propositions are asserted to be *pinned numerically* rather than proved at length in the
  body, this leaves an unauditable verification chain. This is the one item that stops the
  manuscript at my desk rather than at a reviewer's.
- **Page budget against the declared document class.** The source is
  `\documentclass[conference]{IEEEtran}` and renders to 9 pages (body through p. 8, references
  spilling to p. 9) with 6 tables and 4 figures. Most IEEE conference tracks cap at 6 pages
  (+2 at a fee) or hard-cap at 8. Until a track with a >=9-page limit is named, this is a
  mechanical rejection unrelated to merit. Venue-community fit is the deeper problem: the paper's
  own designated killer baseline, CISC, is cited as "Findings of ACL, 2025," and every
  substantive comparator (SC, adaptive consistency, early-stopping SC, rank calibration) is
  ACL/EMNLP/ICLR work. The reviewers who can adjudicate a van Elteren Somers' *D* estimator for
  self-consistency voting sit in that pool, not in a generic IEEE conference track.

### Top 3 Reasons (no hedging)

1. **The abstract's risk profile is not the paper's risk profile.** The abstract closes with
   "pre-registers four falsification criteria, among them the published dev-calibrated CISC
   protocol as a designated killer baseline, all of which the method survived," and earlier
   promises a variant that "guarantees sign consistency whenever the plurality-error rate is
   below one half". The paper's own Discussion then reports that the *headline* variant — TACT-LF,
   the one credited with the 1.000-vs-0.807 recovery in the abstract — in a paraphrased
   wrong-majority cell "mis-signs, saturates at $\gamma=-2.0$, and scores $0.000$ against an
   SC floor of $0.340$," and that "None of the four alarms fires". The survival sentence is
   literally true (F2 was scoped "anywhere on the sweep," and the paraphrase cell is post-hoc
   follow-on work), but a program-committee member who reads only the abstract forms a materially
   wrong belief about the failure envelope and feels misled on reaching Section VII. One clause
   fixes it; omitting it converts the paper's real honesty into apparent concealment.

2. **The pitch advertises the minority of the paper and buries the majority.** The contribution
   list — "This paper frames the problem as estimating one scalar: … The contributions are:" —
   runs C1–C4 and mentions real LLM traces in none of them. The real-trace material (Sec. V-G,
   V-H, V-I) is 1158 of the Results section's 2203 words, more than the entire synthetic sweep
   (1045), and its central number is what the paper itself calls the binding constraint: the
   actionable stratum "measures $2$--$7.5\%$ of items across five substrates in two domains."
   That measurement bounds *every* confidence-weighted voting method, not just TACT, and is the
   most portable empirical result here — yet title, abstract and introduction never tell a reader
   it is the paper's largest experimental block, nor that the real-trace evidence is null on
   accuracy (only Sec. VII says "does not extend to accuracy"). Under-selling the strongest
   transferable finding while foregrounding a synthetic-oracle sweep is a self-inflicted wound.

3. **The manuscript contradicts itself, inside one section, about whether its own central caveat
   has been addressed.** Section VII, first paragraph: "Validation on real LLM traces is the
   remaining step; the cached-trace runner is committed and the prediction is falsifiable".
   Section VII, fourth paragraph: "the measured cost of acting anyway was negative on both real
   substrates". The abstract meanwhile states "Two real-trace campaigns on a frozen model confirm
   the premise and locate the binding constraint". One of these is a stale survivor from a
   pre-real-trace draft. An editor reads a contradiction of that kind as evidence the manuscript
   was not read end-to-end before submission, which lowers prior confidence in every other number
   in it.

### Fast Fixes (within 1-2 days)

- Add an availability statement with a resolvable pointer (repository URL or archival DOI, plus
  the commit or tag that produced the verification table) and state precisely what "76 tests"
  counts; the checked-in suite exposes 93 test functions across 7 files, so the number as written
  invites a reviewer to distrust it.
- Insert one clause in the abstract naming the conditional guarantee and the unguarded failure
  past $\bar\rho>1/2$, and downgrade "all of which the method survived" to "all four
  pre-registered falsifiers survived; a post-hoc paraphrased-majority cell, outside the
  pre-registered sweep, did not."
- Promote the thin-window measurement to a numbered contribution (C5) in the introduction, framed
  as a bound on the whole method family, and state on page 1 that the real-trace claim is confined
  to the premise and to abstention, not to accuracy. This moves the paper's honesty from Sec. VII,
  where reviewers discover it, to where it earns credit.
- Delete or rewrite "Validation on real LLM traces is the remaining step" so Sec. VII stops
  contradicting Sec. V-G–V-I and the abstract.
- Cut the abstract to IEEE's ~200-word norm and strip inline mathematics. As submitted it is 371
  words in one paragraph, consumes the entire first column of page 1, and asks the reader to parse
  "$\gamma=z\sqrt{2+z^2}$", "$\kappa=-0.6$", "$\Dhat=+0.250$" and "$p=3.3\times10^{-24}$" before
  the introduction begins. The 95-word single-paragraph Conclusion is the mirror defect; the
  displaced substance belongs there.
- Name the target track and bring the page count inside its limit. The trim must not come from
  the Method section: at 626 words it is already the thinnest substantive section in a paper named
  after its method, while Results runs 2203 words across 6 tables.

No text in the manuscript, the extracted artifacts, or the repository files inspected for this
screen attempted to address the reviewer, issue instructions, or claim authority over the review.
Nothing to report on that axis.

### 评审 1（理论贡献）

## Theory Contribution Review

### 3 Fatal Theory Holes

1. (Sec. IV-C, Eq. 11) "Model $\varphi\,|\,y\sim\mathcal{N}(\mu_y,s^2)$ within item with the
   \emph{mixture} standardized to unit variance" -- the analytic link that C1 offers *in place of*
   a grid search is derived from a Gaussian model for a statistic that is discrete and bounded by
   construction. At $m_q{=}4$, $\varphi$ takes four values. The paper handles the scale
   consequence (realized $\sigma_q$) and never the distributional one, in exactly the small-budget
   regime it advertises as transferable ("an exponent estimated at $m{=}40$ transfers to deployment
   at $m{=}8$"). And the artifacts show the point is not academic: `results/tact_eval.json` has
   $\gamma$ pinned at $\gamma_{\max}$ in every cell the paper reports as a win, so the derived
   magnitude is never actually the operative one there.

2. (Sec. V-F, Sec. VI) "Proofs are elementary and pinned by unit tests in the released code
   (76 tests;" -- two of the seven propositions carry their content as frequencies measured on one
   400-item synthetic harness at one seed (97.5% SC agreement; a 4% sign match). A proposition
   environment plus a blanket proof sentence grants those measurements the standing of the theorems
   around them. Proposition 7's justification is also weaker than its statement: it establishes
   $D^{w_1}=-D^{w_2}$, a sign flip in one functional, and claims identical observable laws.

3. (Sec. II) "The claim is the assembly and its anchors, not the parts." -- the most honest
   sentence in the paper, and it locates the increment in the wrong place. What survives if TACT is
   superseded is the impossibility triple of Sec. VI and the attenuation identity
   $\mathbb{E}[\Dhat_g]=(1-2\bar\rho)D$: boundary results about what *any* label-free method can
   do. Title, abstract and C1 spend themselves on the tempering map instead.

### What The Paper Is Actually Contributing (1 sentence, no marketing)

A signed, label-free estimate of within-item confidence discrimination, plus the boundary results
showing that per-item label-free adaptation is closed and that the stratum any such method can act
on is a few per cent of items -- with the tempering map itself a competent but grid-equivalent
wrapper whose magnitude is set by a hand-fixed clip wherever it wins.

### How To Fix (2-4 concrete moves)

- State the $m$ at which the Gaussian link is adequate, or add a discreteness correction; report a
  small-$m$ sensitivity run alongside the existing $m{=}40 \to m{=}8$ transfer claim.
- Disclose that $\gamma$ saturates at $\gamma_{\max}$ in the winning cells, and add the
  cap-sensitivity ablation the paper currently defers ("cap robustness is left as an ablation").
- Demote Propositions 5 and 6 to remarks with sample sizes and intervals, and give Proposition 7
  either a real proof of law equality or a weaker statement matched to the sign-flip argument.
- Re-center the theory claim on the impossibility results and the attenuation identity.

### 评审 3（文献对话）

## Literature Dialogue Review

### Gap Derivation Audit

- Claimed gap (quote + location):
  - Abstract (tact.tex L35): "Every published weighting scheme is structurally monotone increasing in confidence, so an anti-correlated channel poisons the vote instead of informing it, while binary dev-set gates survive inversion only by discarding genuinely discriminative signal."
  - Introduction (L48): "Every existing weighting scheme is monotone \emph{increasing} in confidence" ... "the possibility that the channel is \emph{anti-correlated} with correctness is not representable".
  - Related Work (L60): "None of these can represent, much less estimate, a negative confidence--correctness association."
  - Reference class named in support: `taubenfeld2025cisc`, `huang2024rankcalibration`, `li2023diverse`, `borda2025`, `aggarwal2023adaptive`, `li2024escape`, `reasc2026`, `deepconf2025` — nine citation keys in one Related Work paragraph.

- Why the gap is (not) logically established:
  - **The empirical half is real and well shown.** Table `tab:sweep` and `results/tact_eval.json` confirm that CISC-devT and the ECE gate sit exactly at the SC floor for every kappa < 0 (kappa = -0.6: CISC-devT 0.8075 = SC 0.8075), and that fixed-gamma CISC collapses to 0.000 at gamma in {2,4}. The phenomenon — positive-only trust is catastrophic under sign inversion — is demonstrated, not asserted. The paper also earns credit for pre-registering the *published* CISC protocol as a designated killer baseline rather than a strawman fixed-gamma setting, and for the Related Work concession that "CISC's tuned temperature is already a dev-calibrated \SC$\leftrightarrow$CISC interpolation".
  - **The diagnosis is stated one level too strong.** "Cannot represent" / "not representable" is a claim about representational capacity. What is actually established is that published *protocols* restrict their tuning range to non-negative exponents/temperatures — the paper's own baseline is described as "positive grid picked on dev" (L215), a range choice made when instantiating the baseline. The paper then builds `SignGrid-dev`, the same c^gamma family with the sign released, and it reaches the signed test-set oracle across the entire negative half-axis (1.000 at kappa = -0.6 and -0.4, 0.993 at -0.2, 0.892 at -0.1 — the oracle value in every cell). The barrier is therefore one sign bit in a hyperparameter grid, not an expressive limitation of the weight family. That distinction resizes the contribution: from "a capability no published scheme has" to "a capability no published scheme searches for, plus an estimator that finds it without labels" — still a contribution, but a different one.
  - **The universal quantifier has no stated search protocol.** "Every published weighting scheme" and "None of these" are unbounded universals over the literature, supported by eight hand-selected citations, with no venue or date scope, no query record, and no systematic-review claim. The manuscript hedges once ("to the author's knowledge", L48) and then drops the hedge in the abstract and in Related Work. External verification of the reference class was not available to this reviewer; enabling `--literature-search` is recommended specifically to test (a) whether any confidence- or verifier-weighted self-consistency variant admits a signed weight, and (b) whether `parisi2014ranking`'s spectral sign recovery has already been transposed to single-channel voting.
  - **Closest-prior-work test — one comparator does not survive it.** `borda2025` is filed, with `li2023diverse`, into "Weighted variants ... refine the budget". By the paper's own bibliography (L586) that entry is Kang, Zhao & Song, "Scalable best-of-N selection for large language models via self-certainty," NeurIPS 2025 — a selection/aggregation rule over a self-certainty signal, not a budget mechanism; the author's own citation key (`borda2025`) suggests awareness that it aggregates by rank-style voting. It is the only rank-based confidence aggregator in the reference list, and contribution C1's headline is precisely rank-based invariance ("Because $\varphi$ depends on confidence only through within-item ranks..."). Yet the invariance claim is benchmarked against an oracle explicitly restricted to raw-value policies ("``Oracle'' is the test-set best over \emph{raw-value} weight policies"), so no published rank-based method appears anywhere in the baseline set. The one comparator that could contest C1 is cited once, in a dismissive subordinate clause, and never run.

### Pseudo-Innovation / Straw-Man Signals

1. **Comparator substitution in the headline.** The abstract's anti-correlation result is "$\kappa=-0.6$: $1.000$ vs.\ $0.807$" — TACT against the SC/published floor. In that same cell `SignGrid-dev` also scores 1.000, and `results/tact_eval.json` records `TACT-dev_vs_SignGrid` as `{a_only: 0, b_only: 0, p_value: 1.0}` — bit-identical decisions. Across the nine sweep cells SignGrid-dev ties TACT-dev five times and is strictly ahead four times; it is never behind. The abstract names only the weaker of the two designated killer baselines ("among them the published dev-calibrated CISC protocol as a designated killer baseline, all of which the method survived") and drops the stronger one. The delta a reader infers from the abstract is 0.193; the delta over the paper's own trivial baseline on that axis is 0.000.
2. **Asymmetric pre-registration.** F4 reads "CISC-devT or SignGrid-dev **matches** \TACT-dev everywhere". No falsifier can be tripped by SignGrid-dev *beating* TACT-dev. It does, at kappa = -0.2: 0.993 vs 0.978, discordant pairs 0/6, exact p = 0.03125 (`results/tact_eval.json`). The paper reports the magnitude ("trails by $0.005$--$0.015$ in the mid-range") but not the paired test, in a manuscript that otherwise reports McNemar results scrupulously (+79/-0, p = 3.3e-24; +0/-0, p = 1). Selective reporting of the one unfavourable paired test is something a reviewer finds in minutes.
3. **The label-free advantage and the echo advantage do not belong to the same variant.** In the confident-echo cell SignGrid-dev scores 0.550 and TACT-dev 0.585 (the pre-registered "+0.035"), while TACT-LF — the flagship of the abstract — scores 0.200, i.e. 0.350 *below* the trivial baseline. The refusal is principled (Prop. `twoworld`) and honestly footnoted, so this is a positioning defect rather than concealment: "the net advantage concentrates ... echo ($+0.035$)" invites the reader to add advantages that no single configuration realises at once.
4. **Related Work is a ledger, not a synthesis.** 272 words carry 20 of the paper's 26 references. Nine keys sit in the first paragraph; six in one sentence of the second ("Estimating worker reliability from agreement is classical [3 keys]; spectral meta-learners [1] and recent LLM ensemble work [2] exploit covariance across \emph{multiple} predictors"); four in one sentence of the third. Four papers (`li2023diverse`, `borda2025`, `aggarwal2023adaptive`, `li2024escape`) receive no characterization at all. `fuse2026` ("Ensembling verifiers with zero labeled data") and `beyondmajority2025` ("Beyond majority voting: LLM aggregation by leveraging higher-order information") are the two closest published neighbours to contribution C2 — label-free aggregation beyond majority voting — and are separated from it by a single unevidenced clause. No paragraph states what the field collectively believes and where that belief breaks.
5. **The fourth Related Work theme is not literature.** "\textbf{Honest sibling result.} A preceding system by the author (RLEV-VoI...) was evaluated under the same falsification discipline and \emph{failed} it, dominated everywhere by a simple deduplication baseline" carries no `\cite`, no report or arXiv identifier, and no artifact pointer. The claim is unfalsifiable by a reader, and in Related Work it also breaks anonymity in the same sentence.
6. **The bibliography already contains the fix for the paper's self-declared worst failure.** `kuhn2023semantic` (semantic-equivalence clustering) and `rasc2024` (reasoning-aware self-consistency) appear as `\bibitem`s but are cited nowhere in the body. The Discussion's "sharpest unguarded failure mode: the guarantee is conditional" is triggered by a wrong cluster that is "semantically tight but carries no verbatim signature, so deduplication has nothing to collapse" — a consequence of the dedup channel being purely lexical ("single-linkage duplicate groups on the lexical-similarity channel at $0.95$"). Semantic clustering is the standard published response to exactly that, and it sits uncited in the paper's own reference list. "Unguarded" is contingent on a design choice the literature offers an alternative to, and the paper never says so.
7. **Checked and cleared, not a signal.** No prompt-injection text, instruction-like content, or reviewer-directed material was found in `tact.tex`, the section artifacts, or the repo JSON/test files inspected for this lane. The pre-existing `committee/literature.md` and `comments/committee_literature.json` in the workspace were empty automated placeholders and have been replaced.

### Fix Plan (3 concrete edits)

1. **Put SignGrid-dev in the abstract and in C4.** Replace the bare "$\kappa=-0.6$: $1.000$ vs.\ $0.807$" with a two-comparator statement: "...pin every published protocol to the majority-vote floor ($1.000$ vs.\ $0.807$); a trivial dev-tuned *signed* exponent grid also reaches $1.000$ here, so the contribution on this axis is the label-free estimate of the sign, not the recovery itself." In C4, name both designated killers and give F4's outcome quantitatively (parity on 9/9 sweep cells; TACT ahead only in the compression and echo cells). Add the missing paired test at kappa = -0.2 (0/6, p = 0.03) beside the existing margins in Section `sec:results`, and widen F4 to "matches **or beats**".
2. **Downgrade "cannot represent" to "does not search or estimate", and bound the quantifier.** In abstract, introduction and Related Work, replace "structurally monotone increasing" / "not representable" / "None of these can represent" with a scoped claim: "of the confidence-weighted self-consistency protocols surveyed here, all restrict the confidence exponent (or temperature) to non-negative values, so a negative association is never searched for and, being unmeasured, cannot be acted on." Keep "to the author's knowledge" in every instance. If `--literature-search` is enabled, add one sentence recording the search scope that licenses the universal.
3. **Rewrite Related Work as three claims and give the rank axis its own paragraph.** (a) Promote `borda2025` out of the "refine the budget" clause into a named comparator: state what self-certainty Borda selection does, whether its rank aggregation is already invariant to monotone confidence distortion, and either add it to Table `tab:adv` or say explicitly why the raw-value oracle is the right envelope in its absence. (b) Give `fuse2026` and `beyondmajority2025` one sentence each on what structure they require and why a single exchangeable channel does not supply it. (c) Move the RLEV-VoI paragraph out of Related Work into Section `sec:limits` or an appendix with a citable report or repository tag, and cite `kuhn2023semantic` where the paraphrased-wrong-majority failure is discussed — either as the remedy not adopted (with a reason) or as future work.

### 评审 2（方法与透明度）

## Methodology & Transparency Review

### Transparency Gaps

- **No availability statement.** "Proofs are elementary and pinned by unit tests in the released
  code (76 tests;" -- "released" or "committed" recurs in Secs. IV-B, V-C, V-F and VII, and
  Table IV is an entire table of test names standing in for proofs not given in the body. Nine
  pages contain no URL, DOI, repository name, archive, or "available upon publication" sentence.
  The paper's argument for its own correctness is the artifact it does not provide. Independently
  checked here against the actual repository: the suite collects 98 tests and runs in 49.66 s, not
  76/84 tests in 14 s.
- **No dispersion anywhere in the synthetic evidence.** `results/tact_eval.json` runs at
  `{items: 400, k: 15, k_max: 20, seed: 0}`: one seed per cell, no repetitions, no interval. The
  paper then interprets 0.035 differences and renders pre-registered falsifier verdicts on them.
- **The falsifier decision rule is undisclosed and is not a test.** `experiments/run_tact_eval.py`
  implements every verdict on a hard-coded 0.02 accuracy margin
  (`f2 = any(acc[TACT] < acc[SC] - 0.02)`), while the paper says "significantly below". F4's
  survival turns on the distortion cell's 0.035 exceeding that undisclosed 0.02, on one seed.
- **The oracle envelope's grid is never stated.** It is `SIGN_GRID = [-4, -2, -1, -0.5, 0, 0.5, 1,
  2, 4]`, nine points, and for monotone compression its argmax is $\gamma=4.0$: the boundary.
  "Beats the oracle over the entire raw-value weight family" is a continuum claim on a truncated
  grid.
- **The disclosed batch-size confound is never propagated.** "a $30$-problem-per-call probe put
  level-5 plurality accuracy at $0.40$, while the $15$-problem-per-call confirmatory run yielded
  $0.888$ on the same stratum" is exemplary disclosure, and no collection protocol is then reported
  for any window row in Table VI -- the measurements the confound most threatens.

### Circularity

The Discussion's admission is candid and its three mitigations are real, but mitigation 1 does not
hold as stated: three of the five adversarial cells are the monotone distortions, described in
Sec. IV as "rank-preserving by construction", and C1 makes rank-only dependence the source of
TACT's invariance. A rank-invariant estimator facing rank-preserving distortions is inside its own
invariance group; 1.000 there is entailed, not discovered. Only the confident echo and the i.i.d.
heterogeneity cell probe outside the working model. The comparison against the raw-value family in
those cells is still the right comparison to make -- it just cannot double as the circularity
answer.

### Fast Fixes

- Add an availability statement naming the repository and the commit that produced Table IV; quote
  the test count and runtime from that commit.
- Rerun each adversarial cell over 10--20 seeds; report mean and interval, or give the paired
  McNemar for both $+0.035$ cells.
- State the 0.02 falsifier margin in Sec. IV, or replace it with the exact McNemar the paper
  already uses elsewhere.
- State SIGN_GRID in the text and extend the oracle past $\gamma=4$, or bound the claim to the
  grid evaluated.
- Report the collection protocol (batch size) for every row of Table VI.

### 评审 4（逻辑链）

## Logic Chain Review

### Broken Links (claim -> evidence)

1. **The paper bounds its own motivation and never closes the loop.** Sec. V-I measures the
   addressable stratum at "$2$--$7.5\%$ of items on every substrate" with "no widening as items
   harden". That result bounds the entire method family, TACT included, and the two real-trace
   campaigns duly returned $\gamma=0$ with votes bit-identical to \SC. Every step is stated
   honestly; none is joined to the next. The manuscript never says why a method whose addressable
   stratum it has just measured at a few per cent is worth adopting, nor reframes itself as the
   measurement plus a method that abstains correctly inside it. A reader who follows the argument
   to its end reaches a conclusion the paper never states.

2. **Sec. VII contradicts Secs. V-G and V-H.** "Validation on real LLM traces is the remaining
   step" and "All quantitative claims are on a synthetic oracle" sit in the same section as
   "the measured cost of acting anyway was negative on both real substrates". The limitations
   section was not re-derived after the evidence base changed.

3. **A universal default from five small samples.** "Abstention is therefore the correct default
   rather than a conservative one" rests on window measurements over 100, 89, 30, 40 items and one
   recomputed published table. The paper reports the CI on one of them (2.6--19.9% on 3/40) and
   then states the recommendation without qualification in the abstract.

### Causal Inversions

None found. The chain from Sec. V-G finding (c) ("Saturation is the binding constraint, not the
estimator") to the Sec. V-H confirmatory campaign and then to the Sec. V-I window measurement is
correctly ordered, and the reasoning that H2's failure is a property of the substrate rather than
the estimator is sound: the in-pool oracle tops out at $+4/-0$, so the endpoint was unpassable for
any method.

### Fast Fixes

- Add one paragraph joining Sec. V-I to the contribution claim: state the ceiling, then state what
  TACT is for given that ceiling. Leading with the boundary is a reframing, not new experiments.
- Delete the two stale sentences in Sec. VII para 1.
- Scope "the correct default" to the substrates measured, or attach the interval.

### 委员会共识

## Committee Consensus

**Round 2 (re-audit)** — paper at commit `4d75431`, previous bundle raised against `62bc7c7`.

### Score

Formula (`SKILL.md`): start 9.0, subtract `1.5*major + 0.7*moderate + 0.2*minor`
= 9.0 − (1.5·10 + 0.7·23 + 0.2·5) = 9.0 − 32.1 → **floored at 1.0/10**.

The formula saturates on any bundle this size and should not be read as the
committee's judgement. The informative signals are the Editor's independent
pre-screen — **5/10, Conditional Pass, not desk reject** — and the composition of
what remains: 10 majors, of which one is a mechanical blocker (no availability
statement), three are abstract-level wording, and one was introduced by this
revision.

### What round 1 achieved

Ten root causes closed, and the fixes were better than the recommendations in
four cases. In particular the author did not merely soften the
"derived, not grid-searched" claim: a new Results paragraph
("Where the derived exponent actually operates") now states which cells saturate,
that the cap rather than the link sets the exponent there, and reports every cell
where the method trails the trivial signed grid with exact accuracies. The oracle
claim in both abstract and C1 now names its grid and states that the optimum sits
at the boundary. The Conclusion's CISC anchor is now scoped to the log-value
feature map with the shipped default named explicitly. That is the response of an
author reviewing their own work rather than defending it.

### Ordered priorities

1. **Add an availability statement.** One line; the only remaining item that
   stops the paper at an editor's desk. The test count was corrected to 98 against
   the suite, so the reader now has an accurate number for an artifact they still
   cannot fetch.
2. **Fix the two defects this revision introduced.** `γ* ≈ ±38` recomputes to
   ±12.1 (and −8.4/+9.8 at κ=±0.4) with the paper's own `gamma_of`; and the F4
   sentence in §V-D now contradicts the new paragraph one screen above it about
   whether the grid baselines reach the distortion and echo cells.
3. **Bring the abstract in line with the Results the author has now written.**
   Four claim-level residues live only in the abstract: `all of which the method
   survived`, `Two real-trace campaigns … confirm the premise`, the p̄=1/2
   reduction stated as general, and naming only CISC-devT as the killer baseline.
   Each is one clause, and the honest wording already exists elsewhere in the
   manuscript. The abstract is at 378 words, so this needs the length cut first.

### Top 3 to fix first

1. Availability statement with repository + commit that produced Table IV.
2. `±38` → `±12`, and rewrite the F4 clause to "both grid baselines fall 0.035
   short in the distortion and echo cells, and neither can operate label-free".
3. State the 0.02 falsifier tolerance in §IV, or replace it with the exact
   McNemar the paper already reports elsewhere — the pre-registration is offered
   as the paper's most portable contribution, so its decision rule has to be in
   the paper.

## 论文摘要

# Paper Summary: TACT: Trust-Anchored Confidence Tempering for\\ Self-Consistency Voting in Large Language Models

## Research Question
- Confidence-weighted self-consistency (CISC and its successors) improves on majority voting when a frozen large language model's self-reported confidence is calibrated in direction

## Core Thesis
- This paper presents (Trust-Anchored Confidence Tempering), which replaces the fixed confidence exponent with one derived from the measured, signed, within-item discrimination of the channel: a pooled van~Elteren Somers' rank statistic with an item-clustered standard error, passed through positive-part James--Stein shrinkage and a Bayes-discriminant link.

## Headline Claims
- This paper presents (Trust-Anchored Confidence Tempering), which replaces the fixed confidence exponent with one derived from the measured, signed, within-item discrimination of the channel: a pooled van~Elteren Somers' rank statistic with an item-clustered standard error, passed through positive-part James--Stein shrinkage and a Bayes-discriminant link.
- This paper frames the problem as estimating one scalar: the signed within-item discrimination of the confidence channel, and mapping that scalar, with its uncertainty, to a vote exponent.

## Section Map
- abstract (31-33): 371 words
- introduction (39-54): 706 words
- related (55-64): 272 words
- experiment (206-244): 441 words
- result (245-507): 2203 words
- discussion (508-548): 517 words
- conclusion (549-643): 626 words

## Closure Targets
- Second, an aggregation gain of the size reported on the synthetic harness is not measurable on a benchmark of a few hundred items at these window widths, which is why the real-trace claim in this paper is confined to the premise (the channel exists and is signed) and to the abstention behaviour, and does not extend to accuracy.

## 主要问题

### M1: The abstract still ends on 'all of which the method survived' without the unguarded failure
- **类型**: claim_accuracy
- **来源**: [LLM] via `claims_vs_evidence`
- **置信度**: high
- **章节**: abstract
- **关联章节**: abstract
- **根因键**: `abstract-omits-unguarded-failure`
- **原文已核对**: 是
- **原文**: `all of which the method survived`
- **说明**: Unchanged. The claim is true of the four pre-registered falsifiers, which were scoped to the sweep, while the Discussion reports that TACT-LF, the variant the abstract credits with the 1.000-vs-0.807 recovery, 'mis-signs, saturates at $\gamma=-2.0$, and scores $0.000$ against an \SC{} floor of $0.340$' in a paraphrased wrong-majority cell where 'None of the four alarms fires'. Now that the revision has tightened the oracle claim and the CISC anchor in exactly this spirit, this is the largest remaining gap between what the abstract promises and what the paper knows.

### M2: The paper bounds its own motivation and still does not close the argument
- **类型**: claim_accuracy
- **来源**: [LLM] via `committee_logic`
- **置信度**: high
- **章节**: discussion
- **关联章节**: discussion
- **根因键**: `motivation-undercut-by-own-window-measurement`
- **原文已核对**: 是
- **原文**: `whole family of methods can act on at $3$--$7.5\%$ of items on every substrate`
- **说明**: The revision closed part of this: the Discussion now says the real-trace campaigns 'do not test the accuracy claim, because on neither substrate was the addressable stratum large enough for any method to demonstrate a gain'. That joins step three to step two. The remaining gap is the step to the contribution claim. On the paper's own measurement the ceiling for the entire family, TACT included, is 3 to 7.5% of items, and the manuscript still leads with the estimator and never says why a method with that addressable stratum is worth adopting, nor reframes itself as the boundary measurement plus a method that abstains correctly inside it. This is the structural revision left, and it is a reframing rather than new experiments.

### M3: 'Significantly below' in the falsifiers is still a hard-coded 0.02 accuracy margin with no statistical test
- **类型**: methodology
- **来源**: [LLM] via `self_standard_consistency`
- **置信度**: high
- **章节**: experiment
- **关联章节**: experiment
- **根因键**: `falsifier-tolerance-undisclosed`
- **原文已核对**: 是
- **原文**: `F1: \TACT-dev significantly below the best fixed-$\gamma$ CISC at $\kappa{=}{+}0.6$. F2: either variant significantly below \SC{} anywhere on the sweep.`
- **说明**: experiments/run_tact_eval.py still renders every verdict on a fixed tolerance rather than a test: f1 = acc[TACT-dev] < best_cisc - 0.02; f2 = any(acc[TACT] < acc[SC] - 0.02); f4 = all(acc[SignGrid] >= acc[TACT] - 0.02). The constant 0.02 appears nowhere in the manuscript and Sec. V-D still repeats the statistical framing, 'never significantly below \SC{} elsewhere'. F4's survival still turns on the distortion cell's 0.035 exceeding that undisclosed 0.02 on a single seed. A paper that pre-registers falsification has to state the decision rule its falsifiers use; one sentence in Sec. IV does it.

### M4: Still no repository URL, code-availability or data-availability statement, in a paper that delegates its proofs to code
- **类型**: missing_information
- **来源**: [LLM] via `evaluation_fairness_and_reproducibility`
- **置信度**: high
- **章节**: method
- **关联章节**: method
- **根因键**: `no-availability-statement`
- **原文已核对**: 是
- **原文**: `Proofs are elementary and pinned by unit tests in the released code (98 tests;`
- **说明**: The test count in this sentence was corrected from 76 to 98, which confirms the author checked it against the suite, so the reader now has an accurate number for an artifact they still cannot obtain. 'Released' or 'committed' recurs in Secs. IV-B, V-C, V-F and VII, and Table IV is a whole table of test names standing in for proofs not given in the body. Nine pages still contain no URL, DOI, repository name, archive, or 'available upon publication' sentence. This remains the one finding that stops the manuscript at an editor's desk rather than at a reviewer's, and it is a one-line fix: name the repository and the commit or tag that produced Table IV.

### M5: The abstract still names the weaker of the two designated killer baselines
- **类型**: claim_accuracy
- **来源**: [LLM] via `committee_literature`
- **置信度**: high
- **章节**: abstract
- **关联章节**: abstract
- **根因键**: `signgrid-omitted-from-headline`
- **原文已核对**: 是
- **原文**: `pin every published protocol to the majority-vote floor ($\kappa=-0.6$: $1.000$ vs.\ $0.807$)`
- **说明**: The Results section now gives the full honest picture, so this is a positioning residue rather than a concealment. The delta a reader infers from the abstract is 0.193 over the published floor; in that cell results/tact_eval.json records TACT-dev_vs_SignGrid as {a_only: 0, b_only: 0, p_value: 1.0}, bit-identical decisions, and across the nine sweep cells SignGrid-dev ties five times and leads four times, never behind. The falsifier sentence still names only CISC-devT. One clause in the abstract, stating that a trivial dev-tuned signed grid also reaches 1.000 there and that the contribution on this axis is the label-free estimate of the sign, aligns the abstract with the Results the author has already written.

### M6: Every synthetic cell is still a single seed with no dispersion, and the argument now rests on the mid-range comparison too
- **类型**: methodology
- **来源**: [LLM] via `evaluation_fairness_and_reproducibility`
- **置信度**: high
- **章节**: experiment
- **关联章节**: experiment
- **根因键**: `single-seed-no-dispersion`
- **原文已核对**: 是
- **原文**: `the net advantage concentrates exactly where pre-registered: distortion ($+0.035$), echo ($+0.035$), and label-free operation, which no grid can perform`
- **说明**: results/tact_eval.json still runs at config {items: 400, k: 15, k_max: 20, seed: 0}: one seed per cell, no repetitions, no interval. The revision increased the exposure rather than reducing it: the new paragraph now also interprets four mid-range differences of 0.012 to 0.015 as evidence that 'the analytic map is not better at choosing a magnitude on these cells'. On 400 paired items 0.012 is five items. Both the +0.035 advantages and the new negative claim about the map are single-draw quantities. Rerunning each cell over 10-20 seeds, or giving the paired McNemar for each cell the paragraph interprets, would put all of it on the footing the grouped-cell result already has.

### M7: The contribution list still omits the real-trace campaigns and the window measurement
- **类型**: missing_information
- **来源**: [LLM] via `section_intro_related`
- **置信度**: high
- **章节**: introduction
- **关联章节**: introduction
- **根因键**: `contributions-omit-real-trace`
- **原文已核对**: 是
- **原文**: `This paper frames the problem as estimating one scalar: the \emph{signed} within-item discrimination of the confidence channel, and mapping that scalar, with its uncertainty, to a vote exponent. The contributions are:`
- **说明**: Still four contributions, none mentioning real LLM traces, while Secs. V-G to V-I remain the larger part of the Results and Sec. V-I's window measurement bounds every confidence-weighted voting method rather than only TACT. The Discussion was revised to state that neither real substrate could demonstrate a gain, which is the honest framing; page 1 still does not carry it. Promoting the window measurement to C5, framed as a bound on the whole family, moves the paper's strongest transferable result to where it earns credit.

### M8: The Bayes-discriminant link assumes within-item normality of a statistic that is discrete and bounded by construction
- **类型**: methodology
- **来源**: [LLM] via `section_methods`
- **置信度**: high
- **章节**: method
- **关联章节**: method
- **根因键**: `link-assumes-normality-of-discrete-phi`
- **原文已核对**: 是
- **原文**: `Model $\varphi\,|\,y\sim\mathcal{N}(\mu_y,s^2)$ within item with the \emph{mixture} standardized to unit variance`
- **说明**: The link of Eq. (11) is the sole theoretical justification for the magnitude of the exponent, and it is derived from a Gaussian model for phi. By Eq. (2) phi is the standardized van der Waerden score of a midrank, so at $m_q{=}4$ it takes four values before standardization. The paper handles the scale consequence (it standardizes by the realized sigma_q, noting '$0.62$ at $m{=}4$ but $0.95$ at $m{=}40$') and never the distributional one, in exactly the small-budget regime it advertises as transferable ('an exponent estimated at $m{=}40$ transfers to deployment at $m{=}8$'). The revision's new disclosure that the clip binds wherever the statistic saturates narrows where the link is load-bearing, which makes the small-m case the one place it still has to hold. State the m at which the Gaussian link is adequate, or add a discreteness correction.

### M9: 'Cannot represent' still overstates a search-range choice, and the paper's own trivial baseline still refutes it
- **类型**: claim_accuracy
- **来源**: [LLM] via `prior_art_and_novelty_grounding`
- **置信度**: high
- **章节**: related
- **关联章节**: related
- **根因键**: `cannot-represent-vs-not-searched`
- **原文已核对**: 是
- **原文**: `None of these can represent, much less estimate, a negative confidence--correctness association.`
- **说明**: Unchanged, in the abstract ('Every published weighting scheme is structurally monotone increasing'), the Introduction ('is not representable') and Related Work. SignGrid-dev is the same $c^{\gamma}$ family with the sign released and it reaches the signed oracle across the whole negative half-axis (1.000 at kappa=-0.6 and -0.4, 0.993 at -0.2, 0.892 at -0.1), so the barrier is one sign bit in a hyperparameter range, not representational capacity. The revision has already applied exactly this correction to the oracle claim in C1; the same move here would resize the contribution honestly: from a capability no published scheme has, to one no published scheme searches for, plus an estimator that finds it without labels.

### M10: Two paragraphs of the Results section now contradict each other about whether the grid baselines reach the distortion and echo cells
- **类型**: claim_accuracy
- **来源**: [LLM] via `numbers_vs_released_artifacts`
- **置信度**: high
- **章节**: result
- **关联章节**: result
- **根因键**: `f4-unreachable-now-self-contradictory`
- **原文已核对**: 是
- **原文**: `F4 (the distortion and echo cells are unreachable by either grid baseline)`
- **说明**: The revision added a paragraph that reports exactly the opposite, and correctly: SignGrid-dev reaches 0.965 under monotone compression against TACT's 1.000, and in confident echo 'beats the grid optimum $\gamma=-1$ ($0.585$ vs.\ $0.550$)' describes a grid baseline scoring 0.550 in a cell the F4 sentence calls unreachable. Both statements are in Section V, one screen apart. The new paragraph is the accurate one; the F4 wording predates it and should now read that both grid baselines fall 0.035 short in those cells and that neither can operate label-free, which is the claim the artifacts support and is no weaker.

## 中等问题

### M1: A universal operating default is still inferred from five substrates of 30 to 119 items
- **类型**: claim_accuracy
- **来源**: [LLM] via `committee_logic`
- **置信度**: high
- **章节**: abstract
- **关联章节**: abstract
- **根因键**: `universal-default-from-five-small-samples`
- **原文已核对**: 是
- **原文**: `Abstention is therefore the correct default rather than a conservative one, and the dead zone implements it exactly.`
- **说明**: The premises are five window measurements with denominators of 100, 89, 30, an unstated published table, and 40, and the paper reports the interval on one of them (CI95 2.6-19.9% on 3/40). The conclusion is stated in the abstract without qualification. The direction of the evidence supports it; 'the correct default' outruns five small samples in two domains. Scope it to the substrates measured, or attach the interval.

### M2: Abstract is now 378 words in a single math-dense paragraph, against an IEEE norm of roughly 200
- **类型**: presentation
- **来源**: [Script] via `pre_submission_readiness`
- **置信度**: high
- **章节**: abstract
- **关联章节**: abstract
- **根因键**: `abstract-length-and-math`
- **原文已核对**: 是
- **原文**: `Confidence-weighted self-consistency (CISC and its successors) improves on majority voting when a frozen large language model's self-reported confidence is calibrated in \emph{direction}.`
- **说明**: [Script] The revision's added precision on the oracle grid was worth its words, but the abstract grew from 371 to 378 and is still one paragraph filling the whole first column, still asking the reader to parse inline mathematics before the Introduction. The 95-word Conclusion is the mirror defect. Several of the remaining claim-level fixes above also need abstract space, so this is now the binding constraint on making them.

### M3: Nine pages in IEEEtran conference class, still with no named target track
- **类型**: presentation
- **来源**: [Script] via `pre_submission_readiness`
- **置信度**: high
- **章节**: abstract
- **关联章节**: abstract
- **根因键**: `page-budget-and-venue`
- **原文已核对**: 是
- **原文**: `\documentclass[conference]{IEEEtran}`
- **说明**: [Script] The revision left the page count at 9 (body through p. 8, references to p. 9) with 6 tables and 4 figures. Most IEEE conference tracks cap at 6 pages, some at 8 with over-length fees. Until a track with a sufficient limit is named this is a mechanical rejection unrelated to merit. The community question also stands: every substantive comparator cited is ACL/EMNLP/ICLR/NeurIPS work.

### M4: The abstract still credits both real-trace campaigns with confirming the premise
- **类型**: claim_accuracy
- **来源**: [LLM] via `claims_vs_evidence`
- **置信度**: high
- **章节**: abstract
- **关联章节**: abstract
- **根因键**: `both-campaigns-confirm-premise`
- **原文已核对**: 是
- **原文**: `Two real-trace campaigns on a frozen model confirm the premise and locate the binding constraint`
- **说明**: Unchanged in the abstract, although the Discussion was revised to state it correctly ('the channel is null on saturated benchmarks and positive on competition mathematics'). Campaign 1 measured D-hat = -0.219, SE = 0.176, z = -1.24: not significant and pointing the wrong way. What it confirms is the null-direction prediction and the calibration-discrimination argument, not the premise that the channel carries signed discrimination. The Discussion's new sentence is the wording the abstract needs.

### M5: The abstract still states the p-bar=1/2 special case as the method's general reduction
- **类型**: claim_accuracy
- **来源**: [LLM] via `claims_vs_evidence`
- **置信度**: high
- **章节**: abstract
- **关联章节**: abstract
- **根因键**: `pbar-half-special-case-as-general`
- **原文已核对**: 是
- **原文**: `the method is a single expression whose exponent reduces to $\gamma=z\sqrt{2+z^2}$`
- **说明**: Unchanged. Eq. (13) gives the general exponent as gamma = [z*sqrt(2 + 4*p_bar*(1-p_bar)*z^2)] clipped, and Eq. (15) states the two-term form only 'At the default p_bar = 1/2'. The body is precise; the abstract drops the qualifier. Six words fix it.

### M6: The Limitations section still does not state the limitation the paper's own numbers make unavoidable
- **类型**: methodology
- **来源**: [LLM] via `section_discussion_conclusion`
- **置信度**: high
- **章节**: discussion
- **关联章节**: discussion
- **根因键**: `single-seed-no-dispersion`
- **原文已核对**: 是
- **原文**: `Three design choices limit the circularity`
- **说明**: The circularity paragraph was revised and is now accurate about what the real-trace campaigns do and do not test, which was the substance of the earlier contradiction. It still lists no limitation covering statistical dispersion, and the revision widened the exposure by adding four mid-range comparisons of 0.012 to 0.015 to the interpreted set. One sentence stating that every synthetic cell is a single seed at 400 items with no interval would cover it.

### M7: The remedy for the paper's sharpest failure mode has been removed from the bibliography rather than engaged with
- **类型**: missing_information
- **来源**: [LLM] via `prior_art_and_novelty_grounding`
- **置信度**: high
- **章节**: discussion
- **关联章节**: discussion
- **根因键**: `semantic-dedup-remedy-uncited`
- **原文已核对**: 是
- **原文**: `a dominant
wrong cluster that is semantically tight but carries no verbatim signature, so
deduplication has nothing to collapse`
- **说明**: The uncited-reference finding was closed by deleting kuhn2023semantic and rasc2024, which fixes the IEEE hygiene issue and leaves the substantive one worse. The unguarded failure follows from deduplication being purely lexical ('single-linkage duplicate groups on the lexical-similarity channel at $0.95$'), and semantic-equivalence clustering is the standard published response. It is now absent from the manuscript entirely. Calling the mode 'unguarded' reads as a statement about the problem when it is a statement about one design choice; one sentence citing the alternative, either as not adopted with a reason or as future work, would restore the reference and answer the objection at once.

### M8: Three of the five adversarial cells still lie inside the estimator's invariance group by construction
- **类型**: methodology
- **来源**: [LLM] via `evaluation_fairness_and_reproducibility`
- **置信度**: high
- **章节**: discussion
- **关联章节**: discussion
- **根因键**: `distortion-cells-inside-invariance-group`
- **原文已核对**: 是
- **原文**: `the adversarial regimes (distortions, heterogeneity, echo) lie outside the estimator's working model`
- **说明**: The three monotone distortions are 'rank-preserving by construction' (Sec. IV) and C1 makes rank-only dependence the source of TACT's invariance, so 1.000 in those cells is entailed rather than discovered. The comparison against the raw-value family there is still the right comparison, and the revision has now correctly bounded what it shows. What it cannot also be is the circularity mitigation this sentence claims: of the five cells, only confident echo and the i.i.d. heterogeneity cell probe outside the working model.

### M9: F4 as worded still cannot be tripped by the trivial baseline beating the method
- **类型**: methodology
- **来源**: [LLM] via `self_standard_consistency`
- **置信度**: high
- **章节**: experiment
- **关联章节**: experiment
- **根因键**: `f4-asymmetric-falsifier`
- **原文已核对**: 是
- **原文**: `F4: CISC-devT or SignGrid-dev matches \TACT-dev everywhere, including the distortion, heterogeneity, and small-dev cells.`
- **说明**: The falsifier fires only if a grid baseline matches TACT everywhere, so SignGrid-dev strictly beating TACT-dev, which the revision now documents in four of nine sweep cells, cannot falsify anything. The new paragraph makes the asymmetry more visible, not less: the paper now reports the losses and still keeps a pre-registration that could not have registered them. Widening F4 to 'matches or beats' costs nothing and would have been survived anyway on the distortion and echo cells.

### M10: Proposition 7's justification establishes a sign flip, not the identical observable laws it claims
- **类型**: methodology
- **来源**: [LLM] via `section_methods`
- **置信度**: high
- **章节**: hetero
- **关联章节**: hetero
- **根因键**: `prop7-sketch-weaker-than-claim`
- **原文已核对**: 是
- **原文**: `induce identical observable laws (constructively, $D$ computed against either truth satisfies $D^{w_1}=-D^{w_2}$)`
- **说明**: The claim is that two worlds induce identical laws over the observable (a, c); the parenthetical establishes only that one functional of the data is sign-reversed under the two candidate truths. That does not rule out some other functional separating them. The proposition may well be true under the stated i.i.d. coupling, but the paper leans on it twice more, in Sec. V-B and the Discussion, to license 'No label-free method can separate them', so the justification should match the strength of the statement.

### M11: Propositions 5 and 6 are still measured frequencies from one harness inside a proposition environment
- **类型**: methodology
- **来源**: [LLM] via `section_methods`
- **置信度**: high
- **章节**: hetero
- **关联章节**: hetero
- **根因键**: `empirical-frequencies-as-propositions`
- **原文已核对**: 是
- **原文**: `Empirically such a rule agrees with \SC{} on $97.5\%$ of items and its residual flips are net-harmful ($1$ right vs.\ $9$ wrong per $400$ items).`
- **说明**: Proposition 5's opening is a structural claim but its quantitative content is a frequency measured on 400 synthetic items at one seed; Proposition 6 is entirely such a frequency. The blanket 'Proofs are elementary and pinned by unit tests' then extends to both. Restate them as remarks with sample sizes and intervals, or scope the proof sentence so it does not cover them.

### M12: The theoretical increment is still not the one the title and abstract advertise
- **类型**: claim_accuracy
- **来源**: [LLM] via `committee_theory`
- **置信度**: high
- **章节**: hetero
- **关联章节**: hetero
- **根因键**: `theory-increment-mislocated`
- **原文已核对**: 是
- **原文**: `The claim is the assembly and its anchors, not the parts.`
- **说明**: The revision strengthens this reading rather than weakening it. Now that the paper states the clip binds in every saturated cell and that the analytic map is not better at choosing a magnitude in the cells where it is active, what remains as the durable increment is the impossibility triple of Sec. VI and the attenuation identity E[D-hat_g] = (1-2*rho_bar)*D: boundary results about what any label-free method can do, plus the sign recovery. Those survive if TACT is superseded. Title, abstract and C1 still spend themselves on the tempering map.

### M13: C1 still claims the exponent is derived rather than grid-searched, without the clause the Results now supply
- **类型**: claim_accuracy
- **来源**: [LLM] via `claims_vs_evidence`
- **置信度**: high
- **章节**: introduction
- **关联章节**: introduction
- **根因键**: `gamma-max-clip-not-derived`
- **原文已核对**: 是
- **原文**: `$\gamma$ is \emph{derived}, not grid-searched`
- **说明**: The Results section was revised well: it now states that the cap binds where D-hat saturates and that in the four headline cells 'the derived magnitude is not doing the work there, the sign is'. C1 was revised in the same commit for the oracle claim but this phrase was left, so the contribution a reader carries away from page 1 is still the unqualified one, and the honest version is four pages later. Adding 'derived rather than grid-searched, though the clip binds where the statistic saturates (Section V-B)' to C1 closes the last gap on this root cause.

### M14: AUC-hat in the one-line formula is still the shrunken pooled statistic while AUC was defined per-item and raw
- **类型**: presentation
- **来源**: [LLM] via `notation_and_numeric_consistency`
- **置信度**: high
- **章节**: method
- **关联章节**: method
- **根因键**: `auc-hat-overload`
- **原文已核对**: 是
- **原文**: `\gamma=z\sqrt{2+z^{2}},\qquad z=\Phi^{-1}(\widehat{\mathrm{AUC}}),`
- **说明**: Eq. (5) defines $\mathrm{AUC}_q = U_q/(n^1_q n^0_q)$, raw and per-item. Eq. (15) writes $z=\Phi^{-1}(\widehat{\mathrm{AUC}})$, where by Eq. (14) the argument must be the shrunk pooled value. The hat is the only distinguishing mark, and the abstract compounds it with 'the probit of the shrunk pooled AUC', a name the body never defines. Define it where Eq. (15) introduces it.

### M15: kappa still denotes both the confidence coupling and a per-item normalizing constant
- **类型**: presentation
- **来源**: [LLM] via `notation_and_numeric_consistency`
- **置信度**: high
- **章节**: method
- **关联章节**: method
- **根因键**: `kappa-symbol-collision`
- **原文已核对**: 是
- **原文**: `the weights equal $\smash{\kappa_q\,c_{q,i}^{\,\gamma}}$ with a per-item constant $\kappa_q>0$`
- **说明**: kappa indexes the confidence-correctness coupling in Eq. (1), the sweep axis in Table I, the heterogeneity design, and the abstract's headline cell ($\kappa=-0.6$). Proposition 2 reuses it, subscripted by the same item index q, for an unrelated positive normalizer, with no announcement and no symbol table. Any free letter would do.

### M16: Related Work is still a citation ledger: 20 of 26 references in 272 words, four uncharacterized
- **类型**: presentation
- **来源**: [LLM] via `committee_literature`
- **置信度**: high
- **章节**: related
- **关联章节**: related
- **根因键**: `related-work-is-a-ledger`
- **原文已核对**: 是
- **原文**: `Estimating worker reliability from agreement is classical \cite{dawid1979maximum,whitehill2009whose,karger2011iterative}`
- **说明**: Nine keys in the first paragraph, six in one sentence of the second, four in one sentence of the third; li2023diverse, borda2025, aggarwal2023adaptive and li2024escape get no characterization. fuse2026 and beyondmajority2025 are the closest published neighbours to C2 and are separated from it by one unevidenced clause. No paragraph states what the field believes and where that belief breaks. The reordering and URL work in this commit improved the bibliography's mechanics without touching the section's argument.

### M17: The sibling negative result is still uncitable, and still de-anonymizes inside Related Work
- **类型**: missing_information
- **来源**: [LLM] via `prior_art_and_novelty_grounding`
- **置信度**: high
- **章节**: related
- **关联章节**: related
- **根因键**: `rlev-voi-uncitable`
- **原文已核对**: 是
- **原文**: `\textbf{Honest sibling result.} A preceding system by the author (RLEV-VoI, redundancy-discounted voting with value-of-information stopping) was evaluated under the same falsification discipline and \emph{failed} it`
- **说明**: The Conclusion offers the falsification protocol as the paper's most portable contribution on the strength of 'having already killed one of the author's own systems', so this paragraph carries argumentative weight. It has no cite, arXiv id, report, or artifact pointer, so a reader cannot check the killed system or the deduplication baseline that dominated it. It also identifies the author in Related Work, which matters if the target track is double-blind. Move it to Limitations or an appendix with a citable pointer.

### M18: Table VI's single 'Window' column still reports four different quantities across five rows
- **类型**: presentation
- **来源**: [LLM] via `notation_and_numeric_consistency`
- **置信度**: high
- **章节**: result
- **关联章节**: result
- **根因键**: `window-column-heterogeneous`
- **原文已核对**: 是
- **原文**: `Domain & Substrate & Window`
- **说明**: Sec. V-I defines the window as the fraction of items where the plurality is wrong and the correct answer is in the pool. Row 1 gives '$12\%$ informative, $9\%$ decisive', neither of which is that quantity; rows 2 and 3 give decisive and rescuable fractions; rows 4 and 5 give a bare percentage. The abstract's range now correctly bottoms out at the table's minimum, which makes the column's heterogeneity the remaining obstacle to checking it. One column per defined quantity, with the denominator in each cell.

### M19: The exponent cap still differs between the two arms being compared
- **类型**: methodology
- **来源**: [LLM] via `evaluation_fairness_and_reproducibility`
- **置信度**: high
- **章节**: result
- **关联章节**: result
- **根因键**: `asymmetric-cap-across-arms`
- **原文已核对**: 是
- **原文**: `because its lower exponent cap ($2$ vs.\ $4$) regularizes better when $|D|\approx1$; cap robustness is left as an ablation`
- **说明**: TACT-dev and TACT-LF carry different clips (4 vs 2) and different significance floors (1.28 vs 2.33), and in the grouped cell the label-free arm wins 0.940 vs 0.923 with the paper attributing the win to the cap. The revision now states plainly that the cap binds wherever D-hat saturates, which makes this sharper rather than softer: a parameter the paper says decides the headline comparison differs across the arms being compared, and the ablation is still deferred. Running both arms at both caps is a small run.

### M20: The new disclosure paragraph's gamma* = +/-38 does not survive recomputation with the paper's own formula
- **类型**: claim_accuracy
- **来源**: [LLM] via `numbers_vs_released_artifacts`
- **置信度**: high
- **章节**: result
- **关联章节**: result
- **根因键**: `gamma-star-38-miscomputed`
- **原文已核对**: 是
- **原文**: `saturates at $\pm1$, so the link returns $\gamma^\ast\approx\pm38$ and the cap`
- **说明**: Calling src/rlev_voi/formula.py gamma_of(d_hat, se, nu=1.28, gamma_max=inf, p_bar=0.5) on the diagnostics stored in results/tact_eval.json gives the unclipped link value per cell: -12.093 at kappa=-0.6, -8.364 at -0.4, +9.755 at +0.4, +12.112 at +0.6, and +12.115 in each of the three monotone-distortion cells. None is near 38. The paragraph's argument is untouched, since every one of those values is far above gamma_max=4 and the cap does bind, so 'the derived magnitude is not doing the work there, the sign is' stands. But this paragraph exists to hand the reader a checkable number, and the number it hands over is wrong by a factor of three. Replace 38 with 12, or state the range -8.4 to +12.1 across the seven saturated cells.

### M21: The unfavourable paired test is still the one paired test not reported
- **类型**: methodology
- **来源**: [LLM] via `self_standard_consistency`
- **置信度**: high
- **章节**: result
- **关联章节**: result
- **根因键**: `unreported-unfavourable-paired-test`
- **原文已核对**: 是
- **原文**: `Against SignGrid-dev the honest margin is narrow on the homogeneous sweep`
- **说明**: The revision deserves credit here: the new paragraph now names all four cells where TACT-dev trails and gives the exact accuracies, which was the substance of the objection. What is still missing is the test. results/tact_eval.json holds TACT-dev_vs_SignGrid at every sweep point, and at kappa = -0.2 it reads {a_only: 0, b_only: 6, p_value: 0.03125}: significant at 0.05, and the only paired comparison in the paper that favours a baseline. The manuscript reports p=3.3e-24 for the grouped cell and p=1 for the dead-zone cells. Adding '(0/6 discordant, exact p=0.03)' to the new paragraph completes the disclosure and removes the objection entirely.

### M22: Contribution C3 and Proposition 6 still state the winner's-curse frequency under different conditioning
- **类型**: claim_accuracy
- **来源**: [LLM] via `section_methods`
- **置信度**: medium
- **章节**: introduction
- **关联章节**: introduction
- **根因键**: `c3-prop6-conditioning-mismatch`
- **原文已核对**: 是
- **原文**: `the observable sign opposes the truth $96\%$ of the time`
- **说明**: C3 attaches 96% to 'exactly the plurality-wrong items where a flip could help'; Proposition 6 states the complementary 4% but conditions additionally on $|D_q|>0.3$. Arithmetically consistent, different item sets, so the Introduction claims the stronger unconditional version. Add the magnitude condition to C3 or report both.

### M23: The one rank-based comparator is still filed as a budget refinement and never run
- **类型**: claim_accuracy
- **来源**: [LLM] via `prior_art_and_novelty_grounding`
- **置信度**: medium
- **章节**: related
- **关联章节**: related
- **根因键**: `borda2025-miscategorized-not-run`
- **原文已核对**: 是
- **原文**: `Weighted variants \cite{li2023diverse,borda2025} and early-stopping families \cite{aggarwal2023adaptive,li2024escape} refine the budget`
- **说明**: borda2025 is, by the paper's own bibliography, Kang, Zhao and Song, 'Scalable best-of-N selection for large language models via self-certainty', NeurIPS 2025: an aggregation rule over a self-certainty signal, not a budget mechanism. C1's headline property is rank-based invariance and the adversarial envelope is explicitly raw-value, so no published rank-based aggregator appears in the baseline set. The comparator best placed to contest C1 gets one subordinate clause. State why its rank aggregation does not already confer monotone invariance, or add it to Table II.

## 次要问题

### M1: Still six keywords where IEEE asks for three to five
- **类型**: presentation
- **来源**: [Script] via `pre_submission_readiness`
- **置信度**: high
- **章节**: abstract
- **关联章节**: abstract
- **根因键**: `keyword-count`
- **原文已核对**: 是
- **原文**: `large language models, self-consistency, confidence calibration, weighted voting, label-free estimation, rank statistics`
- **说明**: [Script] Unchanged. Drop one or two; 'label-free estimation' and 'rank statistics' are the two that most distinguish this paper from its neighbours.

### M2: Table I is still placed in the Experimental Setup section but interpreted only in Results
- **类型**: presentation
- **来源**: [LLM] via `section_results`
- **置信度**: high
- **章节**: experiment
- **关联章节**: experiment
- **根因键**: `table1-float-before-results`
- **原文已核对**: 是
- **原文**: `\caption{Coupling sweep (accuracy at $K{=}15$; $400$ paired items per cell; dev $n{=}200$). Published protocols sit at the \SC{} floor on the entire negative half-axis.}`
- **说明**: The float is declared before \section{Results} and its caption already states the paper's first result, while the text that reads it begins in Sec. V-A. Moving the float after the Results heading costs nothing.

### M3: Citation stacking is unchanged: nine and six keys in single sentences
- **类型**: presentation
- **来源**: [Script] via `pre_submission_readiness`
- **置信度**: high
- **章节**: related
- **关联章节**: related
- **根因键**: `citation-stacking`
- **原文已核对**: 是
- **原文**: `Weighted variants \cite{li2023diverse,borda2025} and early-stopping families \cite{aggarwal2023adaptive,li2024escape} refine the budget`
- **说明**: [Script] Related Work still carries 20 of 26 references in 272 words with nine keys in one paragraph. The bibliography reordering and URL additions in this commit fixed the reference list's mechanics; the in-text density is a separate edit.

### M4: 'Three times the SC floor' still describes a 2.93x ratio
- **类型**: claim_accuracy
- **来源**: [LLM] via `claims_vs_evidence`
- **置信度**: high
- **章节**: result
- **关联章节**: result
- **根因键**: `three-times-sc-floor-rounding`
- **原文已核对**: 是
- **原文**: `the best result in the field ($0.585$; three times the \SC{} floor)`
- **说明**: 0.585 / 0.200 = 2.925. Trivial in most papers; in this one, which now states its own losses cell by cell, a rounded ratio in the author's favour is the odd one out. 'Nearly three times' costs one word.

### M5: Table II's footnote rows are still typeset inside the tabular after \bottomrule
- **类型**: presentation
- **来源**: [Script] via `pre_submission_readiness`
- **置信度**: high
- **章节**: result
- **关联章节**: result
- **根因键**: `table2-footnote-after-bottomrule`
- **原文已核对**: 是
- **原文**: `\multicolumn{6}{l}{\footnotesize $^{\dagger}$alarm fires and the method refuses to leave \SC---the conditional}\\`
- **说明**: [Script] Two \multicolumn rows still follow \bottomrule inside the tabular, so booktabs' trailing rule is not the last element and the note inherits row spacing. Use a tablenotes environment or place the note after \end{tabular}.

## 决策信号

- **审稿推荐**: 拒稿
- **问题包**: 主要 10 / 中等 23 / 次要 5

## 修订路线图

### 优先级 1 --- 必须处理（阻断）

- [ ] Abstract and conclusion claims need explicit evidence traceability ([LLM]; abstract)

### 优先级 2 --- 强烈建议

- [ ] Abstract five-element check is incomplete; missing background, conclusion, quantitative results ([Script]; abstract)
- [ ] Comparison protocol should make fairness assumptions explicit ([LLM]; experiment)
- [ ] Result claims should identify comparison scope and uncertainty ([LLM]; experiment)
- [ ] Cross-section numeric consistency should be reconciled ([LLM]; introduction)
- [ ] Novelty claim should be grounded against the closest prior work ([LLM]; related_work)

### 优先级 3 --- 可选改进

- [ ] Conclusion should close the loop on the paper's strongest claims ([LLM]; conclusion)
