# 深度审稿报告

**论文**: `/Users/vito/development/adaptive-reasoning-consensus/paper/tact.tex` | **语言**: EN | **模式**: deep-review
**生成时间**: 2026-08-02 14:11
**工件目录**: `/Users/vito/development/adaptive-reasoning-consensus/paper/review_results/v2/tact-v2`

## 总体评估

Round-8 re-audit of the JMLR build at 6b98a8e. Both round-7 items closed and one new minor found; no major, moderate or methodological finding is open. The two citation problems were reworded rather than patched, which is the better fix: the confidence-score sentence no longer nests parentheses and the real-trace one now reads '100 items, 50 from GSM8K and 50 from CommonsenseQA'. A scan for a \citep inside an unclosed author parenthesis returns zero across the file. Two additions this round go beyond the findings. The paper now carries algorithm blocks for both the labeled and the label-free path, and every constant and ordering in them was checked against src/rlev_voi/tact.py and matches, including the two the text singles out as load-bearing: the significance gate gates on the raw pooled z while tempering uses the de-attenuated pair, and p_bar is genuinely left unset on the label-free path so the mixture correction is not applied there. The window range was also tightened from 3-7.5% to 2.5-7.5%, which is now exactly the min and max of Table 5's window column over the five substrates, closing the round-2 objection properly rather than approximately, and the caption reconciles the 119-item and 89-item MATH L5 denominators. The one remaining item is that Table 5 shows six rows against a text that says five substrates, with the budget-capped row's 11.8 outside the quoted range and no caption clause marking it as excluded.

- **主要**: 0
- **中等**: 0
- **次要**: 1

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

**Round 3** — paper at `f8641e8`. Prior rounds: `62bc7c7` (38 findings, Desk Reject) -> `4d75431` (38 findings, Conditional Pass) -> now.

### Score

Formula: 9.0 − (1.5·2 + 0.7·15 + 0.2·5) = 9.0 − 14.5 → **floored at 1.0/10**, which is
still uninformative: the formula cannot distinguish two presentation-and-dispersion
majors from ten claim-accuracy ones. The Editor screen is the calibrated signal, and
the desk-reject trigger it named two rounds ago (no availability statement) is gone.

### Trajectory

| | 62bc7c7 | 4d75431 | f8641e8 |
|---|---|---|---|
| major | 10 | 10 | **2** |
| moderate | 23 | 23 | **15** |
| minor | 5 | 5 | **5** |
| claim-accuracy majors | 5 | 4 | **0** |
| mechanical blocker | yes | yes | **no** |

### What this round achieved

Twelve root causes closed, and three of the fixes are better than what was asked for:

- The normality objection was answered by **stating the defect**, not hedging it: the
  paper now says the link's Gaussian assumption holds "only asymptotically: at
  $m_q{=}4$ the score takes four values before standardization", that the scale
  consequence is handled and "the distributional one is not, and it bites hardest in
  the small-budget setting this paper advertises".
- The falsifier section states the $\tau=0.02$ rule and then criticizes it: "A
  tolerance rather than a test is the weaker instrument, and it matters most for F4,
  which survives on a $0.035$ margin."
- The `±38` miscalculation was corrected to the exact range recomputed from the
  artifacts, $-8.4$ to $+12.1$, and the self-contradictory F4 clause was rewritten to
  what the artifacts support.

The abstract lost 125 words and gained four disclosures at the same time, which is the
harder direction.

### Ordered priorities

1. **Name the target track and get inside its page limit.** 10 pages now. Every
   paragraph added this round earned its place, so the space has to come from
   elsewhere — Table IV is 12 rows of test names that the new availability section
   makes reproducible from the repo, and the 95-word Conclusion restates C1–C5.
2. **Report dispersion.** Every synthetic cell is one draw at `seed: 0`. F4 survives on
   0.035 against a 0.02 tolerance, and the mid-range paragraph interprets four
   differences of 0.012–0.015. Ten to twenty seeds per cell would let the paper drop
   the tolerance for the paired test it says it prefers, and would close the last
   methodology major.
3. **Two one-line closures.** Introduction: "is not representable" → "is never
   searched for", to stop contradicting the revised Related Work. Results: add
   "(0/6 discordant, exact p=0.03)" beside the mid-range margins — the only paired
   test in the paper that favours a baseline, in a paper that now reports its own
   weaker instrument by name.

### Top 3 to fix first

1. Target track + page budget.
2. Seed dispersion on the adversarial and mid-range cells.
3. The two one-line closures above.

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

## 次要问题

### M1: Table 5 has six rows while every claim about it says five substrates, and the sixth sits outside the quoted range
- **类型**: presentation
- **来源**: [LLM] via `notation_and_numeric_consistency`
- **置信度**: high
- **章节**: result
- **关联章节**: result, abstract
- **根因键**: `table5-sixth-row-outside-range`
- **原文已核对**: 是
- **原文**: `QA, budget-capped & MATH L5$^\dagger$ & $18.5$ & $11.8$ \\`
- **说明**: The count is defensible: the five substrates are GSM8K/CSQA, MATH L5, AIME/AMC, HumanEval+/MBPP+ and LeetCode, and the sixth row is MATH L5 again under the budget manipulation rather than a new substrate. The 2.5-7.5% range is exactly the min and max of the Win. column over those five (4.0, 2.5, 3.3, 3.6, 7.5), so it is now fully reconstructible, which closes the original objection. What remains is that a reader checking the table sees six rows and a Win. value of 11.8 that the abstract's range excludes without saying so at the point of reading. The information exists in the row label 'budget-capped' and in Section 8, which calls it 'the widest window measured anywhere in this paper', but not in the caption where the range is checked. One clause in the caption, saying that the last row is the same MATH L5 substrate under the Section 8 manipulation and is not one of the five, removes the only remaining way to misread this table.

## 决策信号

- **审稿推荐**: 录用
- **问题包**: 主要 0 / 中等 0 / 次要 1

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
