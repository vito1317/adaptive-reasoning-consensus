# Deep Review Report

**Paper**: `/Users/vito/development/adaptive-reasoning-consensus/paper/tact.tex` | **Language**: EN | **Mode**: deep-review
**Generated**: 2026-08-01 22:03 | **Venue**: ieee
**Artifacts**: `/Users/vito/development/adaptive-reasoning-consensus/paper/review_results/v2/tact-v2`

## Overall Assessment

Deep review found 1 major, 5 moderate, 1 minor issues. The highest-priority concerns are: Abstract and conclusion claims need explicit evidence traceability; Abstract five-element check is incomplete; missing background, conclusion, quantitative results.

- **Major**: 1
- **Moderate**: 5
- **Minor**: 1

## Academic Pre-Review Committee

### Editor (Desk Reject Screen)

## Editor Pre-Screen (1-10)

Score: 4.0/10
Verdict: Desk Reject

### Desk-Reject Triggers (if any)
- Abstract and conclusion claims need explicit evidence traceability

### Top 3 Reasons (no hedging)
1. Abstract and conclusion claims need explicit evidence traceability

### Fast Fixes (within 1-2 days)
- Clarify abstract to address abstract and conclusion claims need explicit evidence traceability.
- Clarify abstract to address abstract five-element check is incomplete; missing background, conclusion, quantitative results.
- Clarify introduction to address cross-section numeric consistency should be reconciled.

### Reviewer 1 (Theory Contribution)

## Theory Contribution Review

### 3 Fatal Theory Holes
1. (abstract) Abstract and conclusion claims need explicit evidence traceability — At least one headline claim was detected. Deep review should check whether experiments and conclusion language trace back to the same bounded evidence base.
2. (related_work) Novelty claim should be grounded against the closest prior work — The paper positions itself against prior work, but the current wording should make the closest comparator and the real novelty delta explicit instead of relying on broad superiority language.

### Concrete Moves
- Tighten the paper's theoretical positioning in abstract to resolve abstract and conclusion claims need explicit evidence traceability.
- Tighten the paper's theoretical positioning in related_work to resolve novelty claim should be grounded against the closest prior work.

### Reviewer 3 (Literature Dialogue)

## Literature Dialogue Review

### Closest Prior Work Risks
- (related_work) Novelty claim should be grounded against the closest prior work — The paper positions itself against prior work, but the current wording should make the closest comparator and the real novelty delta explicit instead of relying on broad superiority language.

### Gap Claim Risks
- The claimed gap should be defended more explicitly: Novelty claim should be grounded against the closest prior work.

### Fast Fixes
- Name the closest prior comparator in related_work and explain the real novelty delta.

### Reviewer 2 (Methodology & Transparency)

## Methodology Transparency Review (SRQR-aware)

### MUST-FIX (submission blockers)
- No methodology blocker was surfaced by the fallback pass.

### SHOULD-FIX (quality improvements)
- (experiment) "Baselines." — Comparative evaluation language was detected. Deep review should verify that baseline tuning, data splits, and reporting conventions are described symmetrically.
- (experiment) "Baselines." — The results section reports comparative performance. Confirm whether the paper states the evaluation scope, variance, and fairness conditions tightly enough for a reviewer.
- (introduction) "On the coupling sweep the label-free variant matches the 200-label variant nearly point-for-point, including full recovery of negative channels (Section~sec:results)." — Multiple sections contain numeric claims. Confirm that the same quantities reconcile across main text, tables, and appendix material.

### SRQR Checklist Deltas
- Sampling rationale: clarify how the evidence base supports the paper's strongest claims.
- Data collection details (time/place/duration): add context when results depend on specific settings.
- Coding process (stages, coders, disagreement resolution): specify if qualitative or hybrid analysis is used.
- Saturation: state whether the evidence scope is exhaustive or bounded.
- Triangulation: explain whether multiple evidence sources were reconciled.
- Reflexivity: acknowledge researcher choices that shape interpretation.

### Reviewer 4 (Logic Chain)

## Logic Chain Review

### Breakpoints
- (abstract) Abstract and conclusion claims need explicit evidence traceability — At least one headline claim was detected. Deep review should check whether experiments and conclusion language trace back to the same bounded evidence base.
- (abstract) Abstract five-element check is incomplete; missing background, conclusion, quantitative results — [A1] Abstract five-element check is incomplete; missing background, conclusion, quantitative results. This is a mechanical pre-submission readiness finding and should be fixed before the final submission package.
- (conclusion) Conclusion should close the loop on the paper's strongest claims — A closure claim appears in the discussion/conclusion. Verify that it matches the limitations, experimental scope, and prior-art positioning established earlier in the paper.

### Structural Fix Moves
- Add one explicit bridge sentence in abstract so the argument chain closes cleanly.
- Add one explicit bridge sentence in abstract so the argument chain closes cleanly.
- Add one explicit bridge sentence in conclusion so the argument chain closes cleanly.

### Committee Consensus

## Committee Consensus

Overall Score: 3.8/10
Editor Verdict: Desk Reject

### Score Formula
- base 9.0
- minus 1.5 * major (1)
- minus 0.7 * moderate (5)
- minus 0.2 * minor (1)
- floor 1.0
- desk reject cap 4.0

### Top 3 Issues To Fix First
1. Abstract and conclusion claims need explicit evidence traceability
2. Abstract five-element check is incomplete; missing background, conclusion, quantitative results
3. Comparison protocol should make fairness assumptions explicit

## Paper Summary

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

## Major Issues

### M1: Abstract and conclusion claims need explicit evidence traceability
- **Type**: claim_accuracy
- **Source**: [LLM] via `claims_vs_evidence`
- **Confidence**: low
- **Section**: abstract
- **Related Sections**: abstract, results, conclusion
- **Root Cause Key**: `abstract-and-conclusion-claims-need-explicit-evidence-traceability`
- **Quote Verified**: no
- **Quote**: —
- **Explanation**: At least one headline claim was detected. Deep review should check whether experiments and conclusion language trace back to the same bounded evidence base.

## Moderate Issues

### M1: Abstract five-element check is incomplete; missing background, conclusion, quantitative results
- **Type**: missing_information
- **Source**: [Script] via `pre_submission_readiness`
- **Confidence**: high
- **Section**: abstract
- **Related Sections**: abstract
- **Root Cause Key**: `presubmission-a1`
- **Quote Verified**: no
- **Quote**: —
- **Explanation**: [A1] Abstract five-element check is incomplete; missing background, conclusion, quantitative results. This is a mechanical pre-submission readiness finding and should be fixed before the final submission package.

### M2: Cross-section numeric consistency should be reconciled
- **Type**: presentation
- **Source**: [LLM] via `notation_and_numeric_consistency`
- **Confidence**: medium
- **Section**: introduction
- **Related Sections**: introduction, result, conclusion
- **Root Cause Key**: `cross-section-numeric-consistency-should-be-reconciled`
- **Quote Verified**: yes
- **Quote**: `On the coupling sweep the label-free variant matches the 200-label variant nearly point-for-point, including full recovery of negative channels (Section~sec:results).`
- **Explanation**: Multiple sections contain numeric claims. Confirm that the same quantities reconcile across main text, tables, and appendix material.

### M3: Result claims should identify comparison scope and uncertainty
- **Type**: methodology
- **Source**: [LLM] via `evaluation_fairness_and_reproducibility`
- **Confidence**: medium
- **Section**: experiment
- **Related Sections**: experiment, methods
- **Root Cause Key**: `result-claims-should-identify-comparison-scope-and-uncertainty`
- **Quote Verified**: yes
- **Quote**: `Baselines.`
- **Explanation**: The results section reports comparative performance. Confirm whether the paper states the evaluation scope, variance, and fairness conditions tightly enough for a reviewer.

### M4: Comparison protocol should make fairness assumptions explicit
- **Type**: methodology
- **Source**: [LLM] via `evaluation_fairness_and_reproducibility`
- **Confidence**: medium
- **Section**: experiment
- **Related Sections**: experiment
- **Root Cause Key**: `comparison-protocol-should-make-fairness-assumptions-explicit`
- **Quote Verified**: yes
- **Quote**: `Baselines.`
- **Explanation**: Comparative evaluation language was detected. Deep review should verify that baseline tuning, data splits, and reporting conventions are described symmetrically.

### M5: Novelty claim should be grounded against the closest prior work
- **Type**: claim_accuracy
- **Source**: [LLM] via `prior_art_and_novelty_grounding`
- **Confidence**: low
- **Section**: related_work
- **Related Sections**: related_work, results
- **Root Cause Key**: `novelty-claim-should-be-grounded-against-the-closest-prior-work`
- **Quote Verified**: no
- **Quote**: —
- **Explanation**: The paper positions itself against prior work, but the current wording should make the closest comparator and the real novelty delta explicit instead of relying on broad superiority language.

## Minor Issues

### M1: Conclusion should close the loop on the paper's strongest claims
- **Type**: missing_information
- **Source**: [LLM] via `self_standard_consistency`
- **Confidence**: low
- **Section**: conclusion
- **Related Sections**: conclusion, introduction, results
- **Root Cause Key**: `conclusion-should-close-the-loop-on-the-paper-s-strongest-claims`
- **Quote Verified**: no
- **Quote**: —
- **Explanation**: A closure claim appears in the discussion/conclusion. Verify that it matches the limitations, experimental scope, and prior-art positioning established earlier in the paper.

## Phase 0 Automated Findings

### [Script] BIB

| Line | Severity | Issue |
|------|----------|-------|
| --- | Minor | Check: /Users/vito/development/adaptive-reasoning-consensus/paper/tact.tex |
| --- | Minor | PASS |
| --- | Minor | entries: 0 |
| --- | Minor | entries: 0 |

### [Script] CITATIONS

| Line | Severity | Issue |
|------|----------|-------|
| 44 | Critical | Citation stacking: 5 citations clustered in one sentence without individual discussion (section: introduction). Max 2 clustered citations allowed. |
| 46 | Major | Citation stacking: 4 citations clustered in one sentence without individual discussion (section: introduction). Max 2 clustered citations allowed. |
| 60 | Critical | Citation stacking: 9 citations clustered in one sentence without individual discussion (section: related). Max 2 clustered citations allowed. |
| 62 | Critical | Citation stacking: 6 citations clustered in one sentence without individual discussion (section: related). Max 2 clustered citations allowed. |
| 64 | Major | Citation stacking: 4 citations clustered in one sentence without individual discussion (section: related). Max 2 clustered citations allowed. |

### [Script] DEAI

| Line | Severity | Issue |
|------|----------|-------|
| --- | Minor | Use --analyze for full analysis |

### [Script] EXPERIMENT

| Line | Severity | Issue |
|------|----------|-------|
| 209 | Minor | No ablation or component-level evidence is mentioned; verify that contribution attribution is covered. |
| 209 | Minor | No statistical significance, variance, or confidence information is mentioned. |
| 209 | Minor | No efficiency comparison is mentioned; verify whether runtime, memory, or parameter cost should be reported. |
| 251 | Critical | Conclusion overreaches the reported evidence; avoid universal or guarantee-style claims. |
| 269 | Critical | Conclusion overreaches the reported evidence; avoid universal or guarantee-style claims. |
| 344 | Critical | Conclusion overreaches the reported evidence; avoid universal or guarantee-style claims. |
| 355 | Critical | Conclusion overreaches the reported evidence; avoid universal or guarantee-style claims. |
| 397 | Major | Performance claim lacks an explicit baseline or comparator. |
| 417 | Major | Performance claim lacks an explicit baseline or comparator. |
| 429 | Critical | Conclusion overreaches the reported evidence; avoid universal or guarantee-style claims. |
| 502 | Major | Performance claim is not tied to a concrete metric or numeric result. |
| 248 | Minor | No efficiency comparison is mentioned; verify whether runtime, memory, or parameter cost should be reported. |
| 511 | Major | Discussion may lack depth: low ratio of explanatory/attribution language (2/35 lines). Add causal analysis explaining why results occur. |
| 511 | Major | No citations from Related Work reappear in Discussion. Compare your findings with prior work to strengthen the narrative. |
| 552 | Major | Conclusion lacks limitations or future work discussion. |
| 552 | Minor | Conclusion lacks implications or broader impact statement. |
| 552 | Minor | Conclusion lacks explicit summary of core findings. |

### [Script] FIGURES

| Line | Severity | Issue |
|------|----------|-------|
| --- | Minor | figures in /Users/vito/development/adaptive-reasoning-consensus/paper/tact.tex... |
| --- | Minor | 4 figures. |
| --- | Minor | Line 82: figs/kappa_sweep.png |
| --- | Minor | Raster format (.png) used. Prefer Vector (PDF/EPS). |
| --- | Minor | Low DPI: 150x150 (Min: 300) |
| --- | Minor | Line 243: figs/tact_sweep.png |
| --- | Minor | Raster format (.png) used. Prefer Vector (PDF/EPS). |
| --- | Minor | Low DPI: 150x150 (Min: 300) |
| --- | Minor | Line 278: figs/tact_adversarial.png |
| --- | Minor | Raster format (.png) used. Prefer Vector (PDF/EPS). |
| --- | Minor | Low DPI: 150x150 (Min: 300) |
| --- | Minor | Line 307: figs/group_eval.png |
| --- | Minor | Raster format (.png) used. Prefer Vector (PDF/EPS). |
| --- | Minor | Low DPI: 150x150 (Min: 300) |
| --- | Minor | Found 4 potential issues. |

### [Script] FORMAT

| Line | Severity | Issue |
|------|----------|-------|
| --- | Minor | ============================================================ |
| --- | Minor | Format Check Report |
| --- | Minor | ============================================================ |
| --- | Minor | /Users/vito/development/adaptive-reasoning-consensus/paper/tact.tex |
| --- | Minor | UNAVAILABLE |
| --- | Minor | chktex not found. Install with: apt-get install chktex (Linux) or via TeX Live/MiKTeX |
| --- | Minor | MODE] chktex not available |
| --- | Minor | chktex for detailed format checking |

### [Script] GRAMMAR

| Line | Severity | Issue |
|------|----------|-------|
| --- | Minor | [Script]: goal=grammar strength=minimal |
| --- | Minor | No rule-based issues detected in selected scope. |

### [Script] LOGIC

| Line | Severity | Issue |
|------|----------|-------|
| --- | Major | REVIEW (Line 58-67) : No research gap derivation found at end of Related Work |
| --- | Minor | Add explicit gap statement connecting literature to your contribution. |
| --- | Minor | Related Work should conclude by identifying gaps that motivate the study. |
| --- | Major | Abstract, contribution claims, and conclusion may be misaligned. |
| --- | Minor | abstract missing contribution, problem, result; abstract missing contribution claim. |
| --- | Minor | Make sure all three sections consistently state the problem, method, key results, and contribution. |
| --- | Minor | These sections should tell the same core story with different emphasis, not diverge. |

### [Script] PRESUBMISSION

| Line | Severity | Issue |
|------|----------|-------|
| --- | Major | [A1] Abstract five-element check is incomplete; missing background, conclusion, quantitative results. |
| 34 | Minor | [G2] Long paragraph detected (363 words, 10 sentences); split or add a clearer topic sentence. |
| 128 | Minor | [G2] Long paragraph detected (197 words, 6 sentences); split or add a clearer topic sentence. |
| 44 | Minor | [L1] LaTeX citation should use a non-breaking tie before citation, e.g. `Method~\cite{key}`. |
| 44 | Minor | [L1] LaTeX citation should use a non-breaking tie before citation, e.g. `Method~\cite{key}`. |
| 44 | Minor | [L1] LaTeX citation should use a non-breaking tie before citation, e.g. `Method~\cite{key}`. |
| 46 | Minor | [L1] LaTeX citation should use a non-breaking tie before citation, e.g. `Method~\cite{key}`. |
| 46 | Minor | [L1] LaTeX citation should use a non-breaking tie before citation, e.g. `Method~\cite{key}`. |
| 46 | Minor | [L1] LaTeX citation should use a non-breaking tie before citation, e.g. `Method~\cite{key}`. |
| 52 | Minor | [L1] LaTeX citation should use a non-breaking tie before citation, e.g. `Method~\cite{key}`. |
| 60 | Minor | [L1] LaTeX citation should use a non-breaking tie before citation, e.g. `Method~\cite{key}`. |
| 60 | Minor | [L1] LaTeX citation should use a non-breaking tie before citation, e.g. `Method~\cite{key}`. |
| 60 | Minor | [L1] LaTeX citation should use a non-breaking tie before citation, e.g. `Method~\cite{key}`. |
| 60 | Minor | [L1] LaTeX citation should use a non-breaking tie before citation, e.g. `Method~\cite{key}`. |
| 60 | Minor | [L1] LaTeX citation should use a non-breaking tie before citation, e.g. `Method~\cite{key}`. |
| 60 | Minor | [L1] LaTeX citation should use a non-breaking tie before citation, e.g. `Method~\cite{key}`. |
| 60 | Minor | [L1] LaTeX citation should use a non-breaking tie before citation, e.g. `Method~\cite{key}`. |
| 62 | Minor | [L1] LaTeX citation should use a non-breaking tie before citation, e.g. `Method~\cite{key}`. |
| 62 | Minor | [L1] LaTeX citation should use a non-breaking tie before citation, e.g. `Method~\cite{key}`. |
| 62 | Minor | [L1] LaTeX citation should use a non-breaking tie before citation, e.g. `Method~\cite{key}`. |
| 64 | Minor | [L1] LaTeX citation should use a non-breaking tie before citation, e.g. `Method~\cite{key}`. |
| 64 | Minor | [L1] LaTeX citation should use a non-breaking tie before citation, e.g. `Method~\cite{key}`. |
| 64 | Minor | [L1] LaTeX citation should use a non-breaking tie before citation, e.g. `Method~\cite{key}`. |
| 182 | Minor | [L1] LaTeX citation should use a non-breaking tie before citation, e.g. `Method~\cite{key}`. |
| 359 | Minor | [L1] LaTeX citation should use a non-breaking tie before citation, e.g. `Method~\cite{key}`. |
| 405 | Minor | [L1] LaTeX citation should use a non-breaking tie before citation, e.g. `Method~\cite{key}`. |
| 469 | Minor | [L1] LaTeX citation should use a non-breaking tie before citation, e.g. `Method~\cite{key}`. |
| 102 | Minor | [L4] Numbered equation environment has no label for later reference. |
| 110 | Minor | [L4] Numbered equation environment has no label for later reference. |
| 141 | Minor | [L5] Numbered equation label `eq:oneline2` is never referenced in text. |

### [Script] REFERENCES

| Line | Severity | Issue |
|------|----------|-------|
| 78 | Minor | Reference before definition: \ref{fig:baselines} at line 78 appears before label definition at line 84 |
| 141 | Minor | Unreferenced label: \label{eq:oneline2} is never cited in text |
| 274 | Minor | Reference before definition: \ref{fig:adv} at line 274 appears before label definition at line 280 |
| 284 | Minor | Reference before definition: \ref{tab:group} at line 284 appears before label definition at line 289 |
| 284 | Minor | Reference before definition: \ref{fig:group} at line 284 appears before label definition at line 309 |
| 319 | Minor | Reference before definition: \ref{tab:tests} at line 319 appears before label definition at line 327 |
| 467 | Minor | Reference before definition: \ref{tab:window} at line 467 appears before label definition at line 485 |

### [Script] SENTENCES

| Line | Severity | Issue |
|------|----------|-------|
| --- | Minor | [Script]: goal=grammar strength=minimal |
| --- | Minor | SENTENCE (Line 44, 26 words, 4 clauses)  [Script] |
| --- | Minor | Because each trace can also report a confidence score (verbalized  , derived from token log-probabilities, or elicited as    ), a natural refinement is to weight votes by confidence. |
| --- | Minor | Because each trace can also report a confidence score (verbalized. derived from token log-probabilities. or elicited as    ). a natural refinement is to weight votes by confidence.. |
| --- | Minor | Sentence exceeds complexity threshold, split for readability. Applying the split needs --strength moderate or higher. |
| --- | Minor | none (split proposal only; source not rewritten) |
| --- | Minor | none |
| --- | Minor | Check: NEEDS-LLM |
| --- | Minor | Flags:    not-assessed |
| --- | Minor | SENTENCE (Line 44, 42 words, 4 clauses)  [Script] |
| --- | Minor | Confidence-Informed Self-Consistency (CISC)   showed that this recovers the accuracy of plain \SC{} at a fraction of the sampling budget, and introduced Within-Question Discrimination (WQD) to argue that \emph{discrimination}, not calibration, is the property that makes a confidence signal useful for voting. |
| --- | Minor | Confidence-Informed Self-Consistency (CISC)   showed that this recovers the accuracy of plain \SC{} at a fraction of the sampling budget. and introduced Within-Question Discrimination (WQD) to argue that \emph{discrimination}. not calibration. is the property that makes a confidence signal useful for voting.. |
| --- | Minor | Sentence exceeds complexity threshold, split for readability. Applying the split needs --strength moderate or higher. |
| --- | Minor | none (split proposal only; source not rewritten) |
| --- | Minor | none |
| --- | Minor | Check: NEEDS-LLM |
| --- | Minor | Flags:    not-assessed |
| --- | Minor | SENTENCE (Line 46, 61 words, 7 clauses)  [Script] |
| --- | Minor | Yet miscalibration of direction is not exotic: reinforcement fine-tuning is known to distort verbalized confidence, distribution shift can invert a signal that was informative in-domain, and in the experiments reported here a simple anti-correlated channel ( ; Section~ ) drives confidence-weighted baselines from near-perfect accuracy to far below the majority-vote floor, while the same evidence, read with the correct sign, is a perfect signal. |
| --- | Minor | Yet miscalibration of direction is not exotic: reinforcement fine-tuning is known to distort verbalized confidence. distribution shift can invert a signal that was informative in-domain. and in the experiments reported here a simple anti-correlated channel ( ; Section~ ) drives confidence-weighted baselines from near-perfect accuracy to far below the majority-vote floor. while the same evidence. read with the correct sign. is a perfect signal.. |
| --- | Minor | Sentence exceeds complexity threshold, split for readability. Applying the split needs --strength moderate or higher. |
| --- | Minor | none (split proposal only; source not rewritten) |
| --- | Minor | none |
| --- | Minor | Check: NEEDS-LLM |
| --- | Minor | Flags:    not-assessed |
| --- | Minor | SENTENCE (Line 46, 41 words, 4 clauses)  [Script] |
| --- | Minor | The defensive alternative, a binary dev-set gate that disables the channel when calibration error is high, survives the inversion but discards discriminative signal wholesale: a systematically under-confident yet perfectly ranked channel fails an ECE gate for reasons irrelevant to voting utility  . |
| --- | Minor | The defensive alternative. a binary dev-set gate that disables the channel when calibration error is high. survives the inversion but discards discriminative signal wholesale: a systematically under-confident yet perfectly ranked channel fails an ECE gate for reasons irrelevant to voting utility  .. |
| --- | Minor | Sentence exceeds complexity threshold, split for readability. Applying the split needs --strength moderate or higher. |
| --- | Minor | none (split proposal only; source not rewritten) |
| --- | Minor | none |
| --- | Minor | Check: NEEDS-LLM |
| --- | Minor | Flags:    not-assessed |
| --- | Minor | SENTENCE (Line 48, 29 words, 4 clauses)  [Script] |
| --- | Minor | This paper frames the problem as estimating one scalar: the \emph{signed} within-item discrimination of the confidence channel, and mapping that scalar, with its uncertainty, to a vote exponent. |
| --- | Minor | This paper frames the problem as estimating one scalar: the \emph{signed} within-item discrimination of the confidence channel. and mapping that scalar. with its uncertainty. to a vote exponent.. |
| --- | Minor | Sentence exceeds complexity threshold, split for readability. Applying the split needs --strength moderate or higher. |
| --- | Minor | none (split proposal only; source not rewritten) |
| --- | Minor | none |
| --- | Minor | Check: NEEDS-LLM |
| --- | Minor | Flags:    not-assessed |
| --- | Minor | SENTENCE (Line 50, 68 words, 6 clauses)  [Script] |
| --- | Minor | \textbf{C1: Signed, analytically-tempered confidence weighting.} \TACT{} votes with weights  , where   is the standardized van der Waerden score of trace  's within-item confidence midrank, and   is \emph{derived}, not grid-searched: a pooled van~Elteren Somers'   statistic (equal to  ) with an exact tie-corrected null variance and an item-clustered jackknife standard error, shrunk by positive-part James--Stein with a significance floor, then mapped through a Bayes-discriminant link with a mixture-variance correction. |
| --- | Minor | \textbf{C1: Signed. analytically-tempered confidence weighting.} \TACT{} votes with weights. where   is the standardized van der Waerden score of trace  's within-item confidence midrank. and   is \emph{derived}. not grid-searched: a pooled van~Elteren Somers'   statistic (equal to  ) with an exact tie-corrected null variance and an item-clustered jackknife standard error. shrunk by positive-part James--Stein with a significance floor. then mapped through a Bayes-discriminant link with a mixture-variance correction.. |
| --- | Minor | Sentence exceeds complexity threshold, split for readability. Applying the split needs --strength moderate or higher. |
| --- | Minor | none (split proposal only; source not rewritten) |
| --- | Minor | none |
| --- | Minor | Check: NEEDS-LLM |
| --- | Minor | Flags:    not-assessed |
| --- | Minor | SENTENCE (Line 54, 70 words, 3 clauses)  [Script] |
| --- | Minor | \textbf{C3: An impossibility result and its structured escape.} When the per-item coupling is i.i.d.\ with no observable covariate, per-item label-free adaptation is shown to be closed: any monotone use of an item's own agreement statistic collapses to plurality reinforcement; on exactly the plurality-wrong items where a flip could help, the observable sign opposes the truth   of the time; and the two hypotheses   and   induce identical observable laws. |
| --- | Minor | \textbf{C3: An impossibility result and its structured escape.} When the per-item coupling is i.i.d.\ with no observable covariate. per-item label-free adaptation is shown to be closed: any monotone use of an item's own agreement statistic collapses to plurality reinforcement; on exactly the plurality-wrong items where a flip could help. the observable sign opposes the truth   of the time; and the two hypotheses   and   induce identical observable laws.. |
| --- | Minor | Sentence exceeds complexity threshold, split for readability. Applying the split needs --strength moderate or higher. |
| --- | Minor | none (split proposal only; source not rewritten) |
| --- | Minor | none |
| --- | Minor | Check: NEEDS-LLM |
| --- | Minor | Flags:    not-assessed |
| --- | Minor | SENTENCE (Line 56, 32 words, 5 clauses)  [Script] |
| --- | Minor | All four survived, and the honest margins are reported: against the signed grid the net advantage concentrates in three cells: monotone distortion, confident echo, and label-free operation, which no grid can perform. |
| --- | Minor | All four survived. and the honest margins are reported: against the signed grid the net advantage concentrates in three cells: monotone distortion. confident echo. and label-free operation. which no grid can perform.. |
| --- | Minor | Sentence exceeds complexity threshold, split for readability. Applying the split needs --strength moderate or higher. |
| --- | Minor | none (split proposal only; source not rewritten) |
| --- | Minor | none |
| --- | Minor | Check: NEEDS-LLM |
| --- | Minor | Flags:    not-assessed |
| --- | Minor | SENTENCE (Line 60, 40 words, 4 clauses)  [Script] |
| --- | Minor | The dev-calibrated variant must therefore be positioned honestly: CISC's tuned temperature is already a dev-calibrated \SC CISC interpolation, so the novelty of \TACT-dev lies in the sign, the rank invariance, and the analytic (grid-free) map, not in dev calibration itself. |
| --- | Minor | The dev-calibrated variant must therefore be positioned honestly: CISC's tuned temperature is already a dev-calibrated \SC CISC interpolation. so the novelty of \TACT-dev lies in the sign. the rank invariance. and the analytic (grid-free) map. not in dev calibration itself.. |
| --- | Minor | Sentence exceeds complexity threshold, split for readability. Applying the split needs --strength moderate or higher. |
| --- | Minor | none (split proposal only; source not rewritten) |
| --- | Minor | none |
| --- | Minor | Check: NEEDS-LLM |
| --- | Minor | Flags:    not-assessed |
| --- | Minor | SENTENCE (Line 62, 39 words, 4 clauses)  [Script] |
| --- | Minor | The setting here differs: one exchangeable channel from one model, per-item vote structure, and the known failure of agreement proxies under correlated errors---met here with a quantified attenuation identity, conservative de-attenuation, and alarms in place of an unconditional claim. |
| --- | Minor | The setting here differs: one exchangeable channel from one model. per-item vote structure. and the known failure of agreement proxies under correlated errors---met here with a quantified attenuation identity. conservative de-attenuation. and alarms in place of an unconditional claim.. |
| --- | Minor | Sentence exceeds complexity threshold, split for readability. Applying the split needs --strength moderate or higher. |
| --- | Minor | none (split proposal only; source not rewritten) |
| --- | Minor | none |
| --- | Minor | Check: NEEDS-LLM |
| --- | Minor | Flags:    not-assessed |
| --- | Minor | SENTENCE (Line 211, 29 words, 5 clauses)  [Script] |
| --- | Minor | \textbf{Harness.} A cluster-mixture oracle generates, per item, up to   cached traces with answers, confidences  , and two similarity channels; all methods replay identical pools (paired comparisons, exact McNemar tests). |
| --- | Minor | \textbf{Harness.} A cluster-mixture oracle generates. per item. up to   cached traces with answers. confidences. and two similarity channels; all methods replay identical pools (paired comparisons. exact McNemar tests).. |
| --- | Minor | Sentence exceeds complexity threshold, split for readability. Applying the split needs --strength moderate or higher. |
| --- | Minor | none (split proposal only; source not rewritten) |
| --- | Minor | none |
| --- | Minor | Check: NEEDS-LLM |
| --- | Minor | Flags:    not-assessed |
| --- | Minor | SENTENCE (Line 213, 46 words, 5 clauses)  [Script] |
| --- | Minor | \textbf{Regimes.} The   sweep  ; three strictly monotone confidence distortions (compression toward  , over-confident sigmoid, fourth power), rank-preserving by construction, so discrimination is intact while calibration is destroyed; i.i.d.\ heterogeneity ( ); covariate-structured heterogeneity (three groups at  ); and a confident-echo poison (a wrong cluster echoes verbatim with confidence  ). |
| --- | Minor | \textbf{Regimes.} The   sweep  ; three strictly monotone confidence distortions (compression toward. over-confident sigmoid. fourth power). rank-preserving by construction. so discrimination is intact while calibration is destroyed; i.i.d.\ heterogeneity ( ); covariate-structured heterogeneity (three groups at  ); and a confident-echo poison (a wrong cluster echoes verbatim with confidence  ).. |
| --- | Minor | Sentence exceeds complexity threshold, split for readability. Applying the split needs --strength moderate or higher. |
| --- | Minor | none (split proposal only; source not rewritten) |
| --- | Minor | none |
| --- | Minor | Check: NEEDS-LLM |
| --- | Minor | Flags:    not-assessed |
| --- | Minor | SENTENCE (Line 223, 116 words, 0 clauses)  [Script] |
| --- | Minor | \setlength{\tabcolsep}{3.4pt} \begin{tabular}{r cc cc cc c} \toprule & \SC & ECE & devT & SignGrid & \textbf{\TACT-dev} & \textbf{\TACT-LF} & oracle\\ \midrule & .807 & .807 & .807 & 1.000 & \textbf{1.000} & \textbf{1.000} & 1.000\\ & .797 & .797 & .797 & 1.000 & \textbf{1.000} & \textbf{1.000} & 1.000\\ & .835 & .835 & .835 & .993 & .978 & .978 & .993\\ & .762 & .762 & .762 & .892 & .880 & .885 & .892\\ & .835 & .835 & .835 & .835 & .835 & .835 & .835\\ & .795 & .795 & .917 & .917 & .902 & .902 & .917\\ & .845 & .845 & .993 & .993 & .988 & .988 & .993\\ & .838 & .838 & 1.000 & 1.000 & \textbf{1.000} & \textbf{1.000} & 1.000\\ & .782 & .782 & 1.000 & 1.000 & \textbf{1.000} & \textbf{1.000} & 1.000\\ \bottomrule \end{tabular} \end{table} |
| --- | Minor | \setlength{\tabcolsep}{3.4pt} \begin{tabular}{r cc cc cc c} \toprule & \SC & ECE & devT & SignGrid & \textbf{\TACT-dev} & \textbf{\TACT-LF} & oracle\\ \midrule & .807 & .807 & .807 & 1.000 & \textbf{1.000} & \textbf{1.000} & 1.000\\ & .797 & .797 & .797 & 1.000 & \textbf{1.000} & \textbf{1.000} & 1.000\\ & .835 & .835 & .835 & .993 & .978 & .978 & .993\\ & .762 & .762 & .762 & .892 & .880 & .885 & .892\\ & .835 & .835 & .835 & .835 & .835 & .835 & .835\\ & .795 & .795 & .917 & .917 & .902 & .902 & .917\\ & .845 & .845 & .993 & .993 & .988 & .988 & .993\\ & .838 & .838 & 1.000 & 1.000 & \textbf{1.000} & \textbf{1.000} & 1.000\\ & .782 & .782 & 1.000 & 1.000 & \textbf{1.000} & \textbf{1.000} & 1.000\\ \bottomrule \end{tabular} \end{table} |
| --- | Minor | Sentence exceeds complexity threshold, split for readability. Applying the split needs --strength moderate or higher. |
| --- | Minor | none (split proposal only; source not rewritten) |
| --- | Minor | none |
| --- | Minor | Check: NEEDS-LLM |
| --- | Minor | Flags:    not-assessed |
| --- | Minor | SENTENCE (Line 257, 99 words, 0 clauses)  [Script] |
| --- | Minor | \setlength{\tabcolsep}{3.2pt} \begin{tabular}{l cc cc c} \toprule Regime & \SC & devT & SignGrid & \textbf{\TACT-dev} & \textbf{\TACT-LF}\\ \midrule Monotone compress & .795 & .965 & .965 & \textbf{1.000} & \textbf{1.000}\\ Monotone overconf & .795 & 1.000 & 1.000 & 1.000 & 1.000\\ Monotone power & .795 & 1.000 & 1.000 & 1.000 & 1.000\\ Hetero (i.i.d.) & .810 & .810 & .810 & .810 & .810\\ Confident echo & .200 & .200 & .550 & \textbf{.585} & .200 \\ \bottomrule \multicolumn{6}{l}{\footnotesize  alarm fires and the method refuses to leave \SC---the conditional}\\ \multicolumn{6}{l}{\footnotesize guarantee of Prop.~  working as stated.} \end{tabular} \end{table} |
| --- | Minor | \setlength{\tabcolsep}{3.2pt} \begin{tabular}{l cc cc c} \toprule Regime & \SC & devT & SignGrid & \textbf{\TACT-dev} & \textbf{\TACT-LF}\\ \midrule Monotone compress & .795 & .965 & .965 & \textbf{1.000} & \textbf{1.000}\\ Monotone overconf & .795 & 1.000 & 1.000 & 1.000 & 1.000\\ Monotone power & .795 & 1.000 & 1.000 & 1.000 & 1.000\\ Hetero (i.i.d.) & .810 & .810 & .810 & .810 & .810\\ Confident echo & .200 & .200 & .550 & \textbf{.585} & .200 \\ \bottomrule \multicolumn{6}{l}{\footnotesize  alarm fires and the method refuses to leave \SC---the conditional}\\ \multicolumn{6}{l}{\footnotesize guarantee of Prop.~  working as stated.} \end{tabular} \end{table} |
| --- | Minor | Sentence exceeds complexity threshold, split for readability. Applying the split needs --strength moderate or higher. |
| --- | Minor | none (split proposal only; source not rewritten) |
| --- | Minor | none |
| --- | Minor | Check: NEEDS-LLM |
| --- | Minor | Flags:    not-assessed |
| --- | Minor | SENTENCE (Line 273, 60 words, 4 clauses)  [Script] |
| --- | Minor | Under the confident echo, dev labels reveal the inversion (high confidence   wrong) and \TACT-dev counters with  , the best result in the field ( ; three times the \SC{} floor); label-free, the duplicate-collapse alarm fires and the method correctly refuses---by Proposition~  no label-free method could do better than a coin flip on the sign here, and pretending otherwise would be the real failure. |
| --- | Minor | Under the confident echo. dev labels reveal the inversion (high confidence   wrong) and \TACT-dev counters with. the best result in the field ( ; three times the \SC{} floor); label-free. the duplicate-collapse alarm fires and the method correctly refuses---by Proposition~  no label-free method could do better than a coin flip on the sign here. and pretending otherwise would be the real failure.. |
| --- | Minor | Sentence exceeds complexity threshold, split for readability. Applying the split needs --strength moderate or higher. |
| --- | Minor | none (split proposal only; source not rewritten) |
| --- | Minor | none |
| --- | Minor | Check: NEEDS-LLM |
| --- | Minor | Flags:    not-assessed |
| --- | Minor | SENTENCE (Line 283, 45 words, 7 clauses)  [Script] |
| --- | Minor | In the covariate-structured cell, per-group \TACT{} recovers each group's signed coupling (dev  , label-free  , the   group correctly dead-zoned---and cracks the floor that provably binds every global policy: the label-free variant reaches  , within   of the per-item link oracle, with \emph{zero} paired losses to \SC{} over   items ( ,  ). |
| --- | Minor | In the covariate-structured cell. per-group \TACT{} recovers each group's signed coupling (dev. label-free. the   group correctly dead-zoned---and cracks the floor that provably binds every global policy: the label-free variant reaches. within   of the per-item link oracle. with \emph{zero} paired losses to \SC{} over   items (. ).. |
| --- | Minor | Sentence exceeds complexity threshold, split for readability. Applying the split needs --strength moderate or higher. |
| --- | Minor | none (split proposal only; source not rewritten) |
| --- | Minor | none |
| --- | Minor | Check: NEEDS-LLM |
| --- | Minor | Flags:    not-assessed |
| --- | Minor | SENTENCE (Line 312, 40 words, 5 clauses)  [Script] |
| --- | Minor | Against SignGrid-dev the honest margin is narrow on the homogeneous sweep---\TACT{} even trails by  --  in the mid-range, the deliberate cost of shrinkage---and the net advantage concentrates exactly where pre-registered: distortion ( ), echo ( ), and label-free operation, which no grid can perform. |
| --- | Minor | Against SignGrid-dev the honest margin is narrow on the homogeneous sweep---\TACT{} even trails by  --  in the mid-range. the deliberate cost of shrinkage---and the net advantage concentrates exactly where pre-registered: distortion ( ). echo ( ). and label-free operation. which no grid can perform.. |
| --- | Minor | Sentence exceeds complexity threshold, split for readability. Applying the split needs --strength moderate or higher. |
| --- | Minor | none (split proposal only; source not rewritten) |
| --- | Minor | none |
| --- | Minor | Check: NEEDS-LLM |
| --- | Minor | Flags:    not-assessed |
| --- | Minor | SENTENCE (Line 328, 176 words, 7 clauses)  [Script] |
| --- | Minor | \setlength{\tabcolsep}{3.4pt} \begin{tabular}{p{2.55cm} p{3.05cm} p{2.35cm}} \toprule Claim & Test & Evidence \\ \midrule Prop.~  (exact \SC) & \texttt{gamma\_zero\_is\_} \texttt{bitwise\_sc} & 200 random pools, identical incl.\ ties \\ Dead-zone rate & \texttt{dead\_zone\_} \texttt{probability} &  70\% under  , 300 trials \\ Prop.~  (exact CISC) & \texttt{logval\_phi\_} \texttt{reproduces\_cisc} & identical vote shares, 100 pools \\ Rank invariance & \texttt{monotone\_} \texttt{invariance} & 3 distortions   100 pools \\ Null variance & \texttt{null\_variance\_} \texttt{matches\_permutation} & 3{,}000-draw permutation, 10\% tol.\ \\ JS--EB identity & \texttt{js\_eb\_identity} & exact to   \\ Link   & \texttt{link\_values\_and\_} \texttt{mixture\_correction} & closed form, rel.\   \\ Prop.~  (attenuation) & \texttt{poisoning\_} \texttt{attenuation\_linear} &  , abs.\   \\ Props.~ --  & \texttt{test\_tact\_group.py} & 97.5\% \SC{} agreement; 4\% sign match \\ Estimator permutation-invariance & \texttt{estimator\_is\_} \texttt{permutation\_invariant} & bypasses the memo (regression test) \\ Rejected: Kish ESS & \texttt{kish\_fails\_T2\_T3} & asserts the failure \\ Rejected: SAFE guarantee under VoI & \texttt{frozen\_default\_} \texttt{breaks\_guarantee} & asserts the violation \\ \bottomrule \end{tabular} \end{table} |
| --- | Minor | \setlength{\tabcolsep}{3.4pt} \begin{tabular}{p{2.55cm} p{3.05cm} p{2.35cm}} \toprule Claim & Test & Evidence \\ \midrule Prop.~  (exact \SC) & \texttt{gamma\_zero\_is\_} \texttt{bitwise\_sc} & 200 random pools. identical incl.\ ties \\ Dead-zone rate & \texttt{dead\_zone\_} \texttt{probability} &  70\% under. 300 trials \\ Prop.~  (exact CISC) & \texttt{logval\_phi\_} \texttt{reproduces\_cisc} & identical vote shares. 100 pools \\ Rank invariance & \texttt{monotone\_} \texttt{invariance} & 3 distortions   100 pools \\ Null variance & \texttt{null\_variance\_} \texttt{matches\_permutation} & 3{. }000-draw permutation. 10\% tol.\ \\ JS--EB identity & \texttt{js\_eb\_identity} & exact to   \\ Link   & \texttt{link\_values\_and\_} \texttt{mixture\_correction} & closed form. rel.\   \\ Prop.~  (attenuation) & \texttt{poisoning\_} \texttt{attenuation\_linear} &. abs.\   \\ Props.~ --  & \texttt{test\_tact\_group.py} & 97.5\% \SC{} agreement; 4\% sign match \\ Estimator permutation-invariance & \texttt{estimator\_is\_} \texttt{permutation\_invariant} & bypasses the memo (regression test) \\ Rejected: Kish ESS & \texttt{kish\_fails\_T2\_T3} & asserts the failure \\ Rejected: SAFE guarantee under VoI & \texttt{frozen\_default\_} \texttt{breaks\_guarantee} & asserts the violation \\ \bottomrule \end{tabular} \end{table}. |
| --- | Minor | Sentence exceeds complexity threshold, split for readability. Applying the split needs --strength moderate or higher. |
| --- | Minor | none (split proposal only; source not rewritten) |
| --- | Minor | none |
| --- | Minor | Check: NEEDS-LLM |
| --- | Minor | Flags:    not-assessed |
| --- | Minor | SENTENCE (Line 357, 45 words, 4 clauses)  [Script] |
| --- | Minor | \subsection{Real-trace validation} Validation on real traces used Claude Haiku 4.5 as the frozen model: 100 items (50 GSM8K  , 50 CommonsenseQA), \emph{12} independent chain-of-thought traces per item with verbalized confidence (1{,}200 traces total), evaluated at   with a 40/60 dev/test split. |
| --- | Minor | \subsection{Real-trace validation} Validation on real traces used Claude Haiku 4.5 as the frozen model: 100 items (50 GSM8K. 50 CommonsenseQA). \emph{12} independent chain-of-thought traces per item with verbalized confidence (1{. }200 traces total). evaluated at   with a 40/60 dev/test split.. |
| --- | Minor | Sentence exceeds complexity threshold, split for readability. Applying the split needs --strength moderate or higher. |
| --- | Minor | none (split proposal only; source not rewritten) |
| --- | Minor | none |
| --- | Minor | Check: NEEDS-LLM |
| --- | Minor | Flags:    not-assessed |
| --- | Minor | SENTENCE (Line 376, 28 words, 4 clauses)  [Script] |
| --- | Minor | \emph{(b) The dead zone fires, and costs exactly nothing.} With  , \TACT-dev, \TACT-LF and \TACT-group all return   and are bit-identical to \SC{} on every test item (  discordant pairs,  ). |
| --- | Minor | \emph{(b) The dead zone fires. and costs exactly nothing.} With. \TACT-dev. \TACT-LF and \TACT-group all return   and are bit-identical to \SC{} on every test item (  discordant pairs. ).. |
| --- | Minor | Sentence exceeds complexity threshold, split for readability. Applying the split needs --strength moderate or higher. |
| --- | Minor | none (split proposal only; source not rewritten) |
| --- | Minor | none |
| --- | Minor | Check: NEEDS-LLM |
| --- | Minor | Flags:    not-assessed |
| --- | Minor | SENTENCE (Line 401, 42 words, 4 clauses)  [Script] |
| --- | Minor | A pre-registered follow-up tests that prediction:   MATH level-5 problems ,   traces each from the same frozen model, a  -item sign set and an  -item evaluation set drawn from the registered list before any trace was collected, and five hypotheses (H1--H5) fixed in advance. |
| --- | Minor | A pre-registered follow-up tests that prediction:   MATH level-5 problems. traces each from the same frozen model. a  -item sign set and an  -item evaluation set drawn from the registered list before any trace was collected. and five hypotheses (H1--H5) fixed in advance.. |
| --- | Minor | Sentence exceeds complexity threshold, split for readability. Applying the split needs --strength moderate or higher. |
| --- | Minor | none (split proposal only; source not rewritten) |
| --- | Minor | none |
| --- | Minor | Check: NEEDS-LLM |
| --- | Minor | Flags:    not-assessed |
| --- | Minor | SENTENCE (Line 466, 24 words, 4 clauses)  [Script] |
| --- | Minor | The window is   (CI -- ): wider than label-free QA, but the same order, and the composition is the same shape at   saturated,   capability wall, rescuable. |
| --- | Minor | The window is   (CI -- ): wider than label-free QA. but the same order. and the composition is the same shape at   saturated. capability wall. rescuable.. |
| --- | Minor | Sentence exceeds complexity threshold, split for readability. Applying the split needs --strength moderate or higher. |
| --- | Minor | none (split proposal only; source not rewritten) |
| --- | Minor | none |
| --- | Minor | Check: NEEDS-LLM |
| --- | Minor | Flags:    not-assessed |
| --- | Minor | SENTENCE (Line 486, 47 words, 8 clauses)  [Script] |
| --- | Minor | \centering\footnotesize \setlength{\tabcolsep}{4pt} \begin{tabular}{l l c} \toprule Domain & Substrate & Window \\ \midrule QA, label-free & GSM8K / CommonsenseQA  &   informative,   decisive \\ QA, label-free & MATH level-5  &   decisive,   rescuable \\ QA, label-free & AIME / AMC  &   decisive,   rescuable \\ Code, executable & HumanEval+ / MBPP+ &   \\ Code, executable & LeetCode Med/Hard  &   \\ \bottomrule \end{tabular} \end{table} |
| --- | Minor | \centering\footnotesize \setlength{\tabcolsep}{4pt} \begin{tabular}{l l c} \toprule Domain & Substrate & Window \\ \midrule QA. label-free & GSM8K / CommonsenseQA  &   informative. decisive \\ QA. label-free & MATH level-5  &   decisive. rescuable \\ QA. label-free & AIME / AMC  &   decisive. rescuable \\ Code. executable & HumanEval+ / MBPP+ &   \\ Code. executable & LeetCode Med/Hard  &   \\ \bottomrule \end{tabular} \end{table}. |
| --- | Minor | Sentence exceeds complexity threshold, split for readability. Applying the split needs --strength moderate or higher. |
| --- | Minor | none (split proposal only; source not rewritten) |
| --- | Minor | none |
| --- | Minor | Check: NEEDS-LLM |
| --- | Minor | Flags:    not-assessed |
| --- | Minor | SENTENCE (Line 515, 43 words, 5 clauses)  [Script] |
| --- | Minor | \textbf{Narrow margins where labels abound.} When labels are plentiful and the confidence scale is trusted, a dev-picked signed grid captures most of the value; \TACT's case rests on the label-free setting, distorted scales, small dev sets, and the exactness of its anchors. |
| --- | Minor | \textbf{Narrow margins where labels abound.} When labels are plentiful and the confidence scale is trusted. a dev-picked signed grid captures most of the value; \TACT's case rests on the label-free setting. distorted scales. small dev sets. and the exactness of its anchors.. |
| --- | Minor | Sentence exceeds complexity threshold, split for readability. Applying the split needs --strength moderate or higher. |
| --- | Minor | none (split proposal only; source not rewritten) |
| --- | Minor | none |
| --- | Minor | Check: NEEDS-LLM |
| --- | Minor | Flags:    not-assessed |
| --- | Minor | SENTENCE (Line 517, 52 words, 6 clauses)  [Script] |
| --- | Minor | In a \emph{paraphrased} wrong-majority cell (a dominant wrong cluster that is semantically tight but carries no verbatim signature, so deduplication has nothing to collapse) the plurality is wrong on most items, , and \TACT-LF does not merely shrink toward \SC: it \emph{mis-signs}, saturates at  , and scores   against an \SC{} floor of  . |
| --- | Minor | In a \emph{paraphrased} wrong-majority cell (a dominant wrong cluster that is semantically tight but carries no verbatim signature. so deduplication has nothing to collapse) the plurality is wrong on most items. and \TACT-LF does not merely shrink toward \SC: it \emph{mis-signs}. saturates at. and scores   against an \SC{} floor of  .. |
| --- | Minor | Sentence exceeds complexity threshold, split for readability. Applying the split needs --strength moderate or higher. |
| --- | Minor | none (split proposal only; source not rewritten) |
| --- | Minor | none |
| --- | Minor | Check: NEEDS-LLM |
| --- | Minor | Flags:    not-assessed |
| --- | Minor | SENTENCE (Line 536, 58 words, 4 clauses)  [Script] |
| --- | Minor | Second, an aggregation gain of the size reported on the synthetic harness is not measurable on a benchmark of a few hundred items at these window widths, which is why the real-trace claim in this paper is confined to the premise (the channel exists and is signed) and to the abstention behaviour, and does not extend to accuracy. |
| --- | Minor | Second. an aggregation gain of the size reported on the synthetic harness is not measurable on a benchmark of a few hundred items at these window widths. which is why the real-trace claim in this paper is confined to the premise (the channel exists and is signed) and to the abstention behaviour. and does not extend to accuracy.. |
| --- | Minor | Sentence exceeds complexity threshold, split for readability. Applying the split needs --strength moderate or higher. |
| --- | Minor | none (split proposal only; source not rewritten) |
| --- | Minor | none |
| --- | Minor | Check: NEEDS-LLM |
| --- | Minor | Flags:    not-assessed |
| --- | Minor | SENTENCE (Line 552, 62 words, 8 clauses)  [Script] |
| --- | Minor | \section{Conclusion} \TACT{} turns ``how much should this model's confidence be trusted?'' into a measured, signed, uncertainty-aware quantity with exact fallbacks at both ends, plain self-consistency when the evidence is absent and CISC when it is at full strength, and shows that the sign, long unrepresentable in this family of methods, can be recovered without any labels under stated and tested conditions. |
| --- | Minor | \section{Conclusion} \TACT{} turns ``how much should this model's confidence be trusted?'' into a measured. signed. uncertainty-aware quantity with exact fallbacks at both ends. plain self-consistency when the evidence is absent and CISC when it is at full strength. and shows that the sign. long unrepresentable in this family of methods. can be recovered without any labels under stated and tested conditions.. |
| --- | Minor | Sentence exceeds complexity threshold, split for readability. Applying the split needs --strength moderate or higher. |
| --- | Minor | none (split proposal only; source not rewritten) |
| --- | Minor | none |
| --- | Minor | Check: NEEDS-LLM |
| --- | Minor | Flags:    not-assessed |
| --- | Minor | SENTENCE (Line 552, 34 words, 4 clauses)  [Script] |
| --- | Minor | The accompanying impossibility results draw the boundary that any future per-item method must respect, and the falsification protocol, having already killed one of the author's own systems, is offered as the more portable contribution. |
| --- | Minor | The accompanying impossibility results draw the boundary that any future per-item method must respect. and the falsification protocol. having already killed one of the author's own systems. is offered as the more portable contribution.. |
| --- | Minor | Sentence exceeds complexity threshold, split for readability. Applying the split needs --strength moderate or higher. |
| --- | Minor | none (split proposal only; source not rewritten) |
| --- | Minor | none |
| --- | Minor | Check: NEEDS-LLM |
| --- | Minor | Flags:    not-assessed |
| --- | Minor | SENTENCE (Line 559, 40 words, 10 clauses)  [Script] |
| --- | Minor | \bibitem{wang2023selfconsistency} X.~Wang, J.~Wei, D.~Schuurmans, Q.~Le, E.~Chi, S.~Narang, A.~Chowdhery, and D.~Zhou, ``Self-consistency improves chain of thought reasoning in language models,'' in \emph{Proc.\ ICLR}, 2023.\ \url{https://arxiv.org/pdf/2203.11171} |
| --- | Minor | \bibitem{wang2023selfconsistency} X.~Wang. J.~Wei. D.~Schuurmans. Q.~Le. E.~Chi. S.~Narang. A.~Chowdhery. and D.~Zhou. ``Self-consistency improves chain of thought reasoning in language models. '' in \emph{Proc.\ ICLR}. 2023.\ \url{https://arxiv.org/pdf/2203.11171}. |
| --- | Minor | Sentence exceeds complexity threshold, split for readability. Applying the split needs --strength moderate or higher. |
| --- | Minor | none (split proposal only; source not rewritten) |
| --- | Minor | none |
| --- | Minor | Check: NEEDS-LLM |
| --- | Minor | Flags:    not-assessed |
| --- | Minor | SENTENCE (Line 562, 29 words, 4 clauses)  [Script] |
| --- | Minor | \bibitem{taubenfeld2025cisc} A.~Taubenfeld \emph{et~al.}, ``Confidence improves self-consistency in LLMs,'' in \emph{Findings of ACL}, 2025, arXiv:2502.06233.\ \url{https://aclanthology.org/2025.findings-acl.1030.pdf} |
| --- | Minor | \bibitem{taubenfeld2025cisc} A.~Taubenfeld \emph{et~al.}. ``Confidence improves self-consistency in LLMs. '' in \emph{Findings of ACL}. 2025. arXiv:2502.06233.\ \url{https://aclanthology.org/2025.findings-acl.1030.pdf}. |
| --- | Minor | Sentence exceeds complexity threshold, split for readability. Applying the split needs --strength moderate or higher. |
| --- | Minor | none (split proposal only; source not rewritten) |
| --- | Minor | none |
| --- | Minor | Check: NEEDS-LLM |
| --- | Minor | Flags:    not-assessed |
| --- | Minor | SENTENCE (Line 565, 29 words, 7 clauses)  [Script] |
| --- | Minor | \bibitem{aggarwal2023adaptive} P.~Aggarwal, A.~Madaan, Y.~Yang, and Mausam, ``Let's sample step by step: Adaptive-consistency for efficient reasoning and coding with {LLMs},'' in \emph{Proc.\ EMNLP}, 2023, pp. |
| --- | Minor | \bibitem{aggarwal2023adaptive} P.~Aggarwal. A.~Madaan. Y.~Yang. and Mausam. ``Let's sample step by step: Adaptive-consistency for efficient reasoning and coding with {LLMs}. '' in \emph{Proc.\ EMNLP}. 2023. pp.. |
| --- | Minor | Sentence exceeds complexity threshold, split for readability. Applying the split needs --strength moderate or higher. |
| --- | Minor | none (split proposal only; source not rewritten) |
| --- | Minor | none |
| --- | Minor | Check: NEEDS-LLM |
| --- | Minor | Flags:    not-assessed |
| --- | Minor | SENTENCE (Line 580, 32 words, 11 clauses)  [Script] |
| --- | Minor | \bibitem{huang2024rankcalibration} X.~Huang, S.~Li, M.~Yu, M.~Sesia, H.~Hassani, I.~Lee, O.~Bastani, and E.~Dobriban, ``Uncertainty in language models: Assessment through rank-calibration,'' in \emph{Proc.\ EMNLP}, 2024, pp. |
| --- | Minor | \bibitem{huang2024rankcalibration} X.~Huang. S.~Li. M.~Yu. M.~Sesia. H.~Hassani. I.~Lee. O.~Bastani. and E.~Dobriban. ``Uncertainty in language models: Assessment through rank-calibration. '' in \emph{Proc.\ EMNLP}. 2024. pp.. |
| --- | Minor | Sentence exceeds complexity threshold, split for readability. Applying the split needs --strength moderate or higher. |
| --- | Minor | none (split proposal only; source not rewritten) |
| --- | Minor | none |
| --- | Minor | Check: NEEDS-LLM |
| --- | Minor | Flags:    not-assessed |
| --- | Minor | SENTENCE (Line 586, 37 words, 6 clauses)  [Script] |
| --- | Minor | \bibitem{borda2025} Z.~Kang, X.~Zhao, and D.~Song, ``Scalable best-of-N selection for large language models via self-certainty,'' in \emph{Proc.\ NeurIPS}, 2025, arXiv:2502.18581.\ \url{https://proceedings.neurips.cc/paper_files/paper/2025/file/1c7eff166a8e345f664f0faa8f4e4d2e-Paper-Conference.pdf} |
| --- | Minor | \bibitem{borda2025} Z.~Kang. X.~Zhao. and D.~Song. ``Scalable best-of-N selection for large language models via self-certainty. '' in \emph{Proc.\ NeurIPS}. 2025. arXiv:2502.18581.\ \url{https://proceedings.neurips.cc/paper_files/paper/2025/file/1c7eff166a8e345f664f0faa8f4e4d2e-Paper-Conference.pdf}. |
| --- | Minor | Sentence exceeds complexity threshold, split for readability. Applying the split needs --strength moderate or higher. |
| --- | Minor | none (split proposal only; source not rewritten) |
| --- | Minor | none |
| --- | Minor | Check: NEEDS-LLM |
| --- | Minor | Flags:    not-assessed |
| --- | Minor | SENTENCE (Line 589, 27 words, 7 clauses)  [Script] |
| --- | Minor | \bibitem{reasc2026} J.~Kim, N.~Yang, K.~Min, and K.~Jung, ``Reliability-aware adaptive self-consistency for efficient sampling in LLM reasoning,'' in \emph{Findings of ACL}, 2026, pp. |
| --- | Minor | \bibitem{reasc2026} J.~Kim. N.~Yang. K.~Min. and K.~Jung. ``Reliability-aware adaptive self-consistency for efficient sampling in LLM reasoning. '' in \emph{Findings of ACL}. 2026. pp.. |
| --- | Minor | Sentence exceeds complexity threshold, split for readability. Applying the split needs --strength moderate or higher. |
| --- | Minor | none (split proposal only; source not rewritten) |
| --- | Minor | none |
| --- | Minor | Check: NEEDS-LLM |
| --- | Minor | Flags:    not-assessed |
| --- | Minor | SENTENCE (Line 595, 22 words, 5 clauses)  [Script] |
| --- | Minor | Skene, ``Maximum likelihood estimation of observer error-rates using the EM algorithm,'' \emph{J.\ Roy.\ Statist.\ Soc.\ C}, vol.~28, no.~1, pp. |
| --- | Minor | Skene. ``Maximum likelihood estimation of observer error-rates using the EM algorithm. '' \emph{J.\ Roy.\ Statist.\ Soc.\ C}. vol.~28. no.~1. pp.. |
| --- | Minor | Sentence exceeds complexity threshold, split for readability. Applying the split needs --strength moderate or higher. |
| --- | Minor | none (split proposal only; source not rewritten) |
| --- | Minor | none |
| --- | Minor | Check: NEEDS-LLM |
| --- | Minor | Flags:    not-assessed |
| --- | Minor | SENTENCE (Line 601, 28 words, 5 clauses)  [Script] |
| --- | Minor | Karger, S.~Oh, and D.~Shah, ``Iterative learning for reliable crowdsourcing systems,'' in \emph{Proc.\ NeurIPS}, 2011.\ \url{https://proceedings.neurips.cc/paper_files/paper/2011/file/c667d53acd899a97a85de0c201ba99be-Paper.pdf} |
| --- | Minor | Karger. S.~Oh. and D.~Shah. ``Iterative learning for reliable crowdsourcing systems. '' in \emph{Proc.\ NeurIPS}. 2011.\ \url{https://proceedings.neurips.cc/paper_files/paper/2011/file/c667d53acd899a97a85de0c201ba99be-Paper.pdf}. |
| --- | Minor | Sentence exceeds complexity threshold, split for readability. Applying the split needs --strength moderate or higher. |
| --- | Minor | none (split proposal only; source not rewritten) |
| --- | Minor | none |
| --- | Minor | Check: NEEDS-LLM |
| --- | Minor | Flags:    not-assessed |
| --- | Minor | SENTENCE (Line 604, 29 words, 8 clauses)  [Script] |
| --- | Minor | \bibitem{parisi2014ranking} F.~Parisi, F.~Strino, B.~Nadler, and Y.~Kluger, ``Ranking and combining multiple predictors without labeled data,'' \emph{Proc.\ Natl.\ Acad.\ Sci.}, vol.~111, no.~4, pp. |
| --- | Minor | \bibitem{parisi2014ranking} F.~Parisi. F.~Strino. B.~Nadler. and Y.~Kluger. ``Ranking and combining multiple predictors without labeled data. '' \emph{Proc.\ Natl.\ Acad.\ Sci.}. vol.~111. no.~4. pp.. |
| --- | Minor | Sentence exceeds complexity threshold, split for readability. Applying the split needs --strength moderate or higher. |
| --- | Minor | none (split proposal only; source not rewritten) |
| --- | Minor | none |
| --- | Minor | Check: NEEDS-LLM |
| --- | Minor | Flags:    not-assessed |
| --- | Minor | SENTENCE (Line 607, 17 words, 6 clauses)  [Script] |
| --- | Minor | \bibitem{fuse2026} J.~Lee, V.~Ma, S.~Zhao, Y.~Nair, A.~Spector, R.~Cohen, and E.~J. |
| --- | Minor | \bibitem{fuse2026} J.~Lee. V.~Ma. S.~Zhao. Y.~Nair. A.~Spector. R.~Cohen. and E.~J.. |
| --- | Minor | Sentence exceeds complexity threshold, split for readability. Applying the split needs --strength moderate or higher. |
| --- | Minor | none (split proposal only; source not rewritten) |
| --- | Minor | none |
| --- | Minor | Check: NEEDS-LLM |
| --- | Minor | Flags:    not-assessed |
| --- | Minor | SENTENCE (Line 610, 37 words, 8 clauses)  [Script] |
| --- | Minor | \bibitem{beyondmajority2025} R.~Ai, Y.~Pan, D.~Simchi-Levi, M.~Tambe, and H.~Xu, ``Beyond majority voting: LLM aggregation by leveraging higher-order information,'' arXiv:2510.01499, 2025, accepted to ICML 2026.\ \url{https://arxiv.org/pdf/2510.01499} |
| --- | Minor | \bibitem{beyondmajority2025} R.~Ai. Y.~Pan. D.~Simchi-Levi. M.~Tambe. and H.~Xu. ``Beyond majority voting: LLM aggregation by leveraging higher-order information. '' arXiv:2510.01499. 2025. accepted to ICML 2026.\ \url{https://arxiv.org/pdf/2510.01499}. |
| --- | Minor | Sentence exceeds complexity threshold, split for readability. Applying the split needs --strength moderate or higher. |
| --- | Minor | none (split proposal only; source not rewritten) |
| --- | Minor | none |
| --- | Minor | Check: NEEDS-LLM |
| --- | Minor | Flags:    not-assessed |
| --- | Minor | SENTENCE (Line 613, 22 words, 4 clauses)  [Script] |
| --- | Minor | \bibitem{vanelteren1960} P.~van Elteren, ``On the combination of independent two-sample tests of Wilcoxon,'' \emph{Bull.\ Int.\ Statist.\ Inst.}, vol.~37, pp. |
| --- | Minor | \bibitem{vanelteren1960} P.~van Elteren. ``On the combination of independent two-sample tests of Wilcoxon. '' \emph{Bull.\ Int.\ Statist.\ Inst.}. vol.~37. pp.. |
| --- | Minor | Sentence exceeds complexity threshold, split for readability. Applying the split needs --strength moderate or higher. |
| --- | Minor | none (split proposal only; source not rewritten) |
| --- | Minor | none |
| --- | Minor | Check: NEEDS-LLM |
| --- | Minor | Flags:    not-assessed |
| --- | Minor | SENTENCE (Line 616, 22 words, 4 clauses)  [Script] |
| --- | Minor | \bibitem{james1961estimation} W.~James and C.~Stein, ``Estimation with quadratic loss,'' in \emph{Proc.\ 4th Berkeley Symp.\ Math.\ Statist.\ Prob.}, 1961, pp. |
| --- | Minor | \bibitem{james1961estimation} W.~James and C.~Stein. ``Estimation with quadratic loss. '' in \emph{Proc.\ 4th Berkeley Symp.\ Math.\ Statist.\ Prob.}. 1961. pp.. |
| --- | Minor | Sentence exceeds complexity threshold, split for readability. Applying the split needs --strength moderate or higher. |
| --- | Minor | none (split proposal only; source not rewritten) |
| --- | Minor | none |
| --- | Minor | Check: NEEDS-LLM |
| --- | Minor | Flags:    not-assessed |
| --- | Minor | SENTENCE (Line 622, 20 words, 5 clauses)  [Script] |
| --- | Minor | Scott, ``The analysis of categorical data from complex sample surveys,'' \emph{J.\ Amer.\ Statist.\ Assoc.}, vol.~76, no.~374, pp. |
| --- | Minor | Scott. ``The analysis of categorical data from complex sample surveys. '' \emph{J.\ Amer.\ Statist.\ Assoc.}. vol.~76. no.~374. pp.. |
| --- | Minor | Sentence exceeds complexity threshold, split for readability. Applying the split needs --strength moderate or higher. |
| --- | Minor | none (split proposal only; source not rewritten) |
| --- | Minor | none |
| --- | Minor | Check: NEEDS-LLM |
| --- | Minor | Flags:    not-assessed |
| --- | Minor | SENTENCE (Line 628, 32 words, 5 clauses)  [Script] |
| --- | Minor | \bibitem{kuhn2023semantic} L.~Kuhn, Y.~Gal, and S.~Farquhar, ``Semantic uncertainty: Linguistic invariances for uncertainty estimation in natural language generation,'' in \emph{Proc.\ ICLR}, 2023.\ \url{https://arxiv.org/pdf/2302.09664} |
| --- | Minor | \bibitem{kuhn2023semantic} L.~Kuhn. Y.~Gal. and S.~Farquhar. ``Semantic uncertainty: Linguistic invariances for uncertainty estimation in natural language generation. '' in \emph{Proc.\ ICLR}. 2023.\ \url{https://arxiv.org/pdf/2302.09664}. |
| --- | Minor | Sentence exceeds complexity threshold, split for readability. Applying the split needs --strength moderate or higher. |
| --- | Minor | none (split proposal only; source not rewritten) |
| --- | Minor | none |
| --- | Minor | Check: NEEDS-LLM |
| --- | Minor | Flags:    not-assessed |
| --- | Minor | SENTENCE (Line 631, 27 words, 7 clauses)  [Script] |
| --- | Minor | \bibitem{rasc2024} G.~Wan, Y.~Wu, J.~Chen, and S.~Li, ``Reasoning aware self-consistency: Leveraging reasoning paths for efficient LLM sampling,'' in \emph{Proc.\ NAACL}, 2025, pp. |
| --- | Minor | \bibitem{rasc2024} G.~Wan. Y.~Wu. J.~Chen. and S.~Li. ``Reasoning aware self-consistency: Leveraging reasoning paths for efficient LLM sampling. '' in \emph{Proc.\ NAACL}. 2025. pp.. |
| --- | Minor | Sentence exceeds complexity threshold, split for readability. Applying the split needs --strength moderate or higher. |
| --- | Minor | none (split proposal only; source not rewritten) |
| --- | Minor | none |
| --- | Minor | Check: NEEDS-LLM |
| --- | Minor | Flags:    not-assessed |
| --- | Minor | SENTENCE (Line 34, 47 words, 5 clauses)  [Script] |
| --- | Minor | This paper presents \TACT{} (Trust-Anchored Confidence Tempering), which replaces the fixed confidence exponent with one \emph{derived} from the measured, signed, within-item discrimination of the channel: a pooled van~Elteren Somers'   rank statistic with an item-clustered standard error, passed through positive-part James--Stein shrinkage and a Bayes-discriminant link. |
| --- | Minor | This paper presents \TACT{} (Trust-Anchored Confidence Tempering). which replaces the fixed confidence exponent with one \emph{derived} from the measured. signed. within-item discrimination of the channel: a pooled van~Elteren Somers'   rank statistic with an item-clustered standard error. passed through positive-part James--Stein shrinkage and a Bayes-discriminant link.. |
| --- | Minor | Sentence exceeds complexity threshold, split for readability. Applying the split needs --strength moderate or higher. |
| --- | Minor | none (split proposal only; source not rewritten) |
| --- | Minor | none |
| --- | Minor | Check: NEEDS-LLM |
| --- | Minor | Flags:    not-assessed |
| --- | Minor | SENTENCE (Line 34, 55 words, 5 clauses)  [Script] |
| --- | Minor | On a synthetic-oracle harness with paired trace pools, the label-free variant recovers anti-correlated channels that pin every published protocol to the majority-vote floor ( :   vs.\  ), rank invariance beats the oracle over the entire raw-value weight family under monotone confidence compression (  vs.\  ), and a per-group extension cracks the heterogeneity floor with zero paired losses to self-consistency (  vs.\  ;  ,  ). |
| --- | Minor | On a synthetic-oracle harness with paired trace pools. the label-free variant recovers anti-correlated channels that pin every published protocol to the majority-vote floor ( :   vs.\  ). rank invariance beats the oracle over the entire raw-value weight family under monotone confidence compression (  vs.\  ). and a per-group extension cracks the heterogeneity floor with zero paired losses to self-consistency (  vs.\  ;. ).. |
| --- | Minor | Sentence exceeds complexity threshold, split for readability. Applying the split needs --strength moderate or higher. |
| --- | Minor | none (split proposal only; source not rewritten) |
| --- | Minor | none |
| --- | Minor | Check: NEEDS-LLM |
| --- | Minor | Flags:    not-assessed |
| --- | Minor | SENTENCE (Line 34, 63 words, 6 clauses)  [Script] |
| --- | Minor | Two real-trace campaigns on a frozen model confirm the premise and locate the binding constraint: within-item discrimination is positive on competition mathematics (pooled  ,  ), yet the stratum on which any such method can act, where the plurality is wrong and the correct answer is present in the pool, measures  --  of items across five substrates in two domains, code generation with executable ground truth included. |
| --- | Minor | Two real-trace campaigns on a frozen model confirm the premise and locate the binding constraint: within-item discrimination is positive on competition mathematics (pooled. ). yet the stratum on which any such method can act. where the plurality is wrong and the correct answer is present in the pool. measures  --  of items across five substrates in two domains. code generation with executable ground truth included.. |
| --- | Minor | Sentence exceeds complexity threshold, split for readability. Applying the split needs --strength moderate or higher. |
| --- | Minor | none (split proposal only; source not rewritten) |
| --- | Minor | none |
| --- | Minor | Check: NEEDS-LLM |
| --- | Minor | Flags:    not-assessed |
| --- | Minor | SENTENCE (Line 34, 39 words, 5 clauses)  [Script] |
| --- | Minor | The paper further proves that per-item label-free adaptation is impossible under i.i.d.\ latent coupling, and pre-registers four falsification criteria, among them the published dev-calibrated CISC protocol as a designated killer baseline, all of which the method survived. |
| --- | Minor | The paper further proves that per-item label-free adaptation is impossible under i.i.d.\ latent coupling. and pre-registers four falsification criteria. among them the published dev-calibrated CISC protocol as a designated killer baseline. all of which the method survived.. |
| --- | Minor | Sentence exceeds complexity threshold, split for readability. Applying the split needs --strength moderate or higher. |
| --- | Minor | none (split proposal only; source not rewritten) |
| --- | Minor | none |
| --- | Minor | Check: NEEDS-LLM |
| --- | Minor | Flags:    not-assessed |

## Decision Signals

- **Committee Score**: 3.8/10
- **Editor Verdict**: Desk Reject
- **Reviewer Recommendation**: Major Revision
- **Issue Bundle**: 1 major / 5 moderate / 1 minor

## Revision Roadmap

### Priority 1 --- Must Address (Blocking)

- [ ] Abstract and conclusion claims need explicit evidence traceability ([LLM]; abstract)

### Priority 2 --- Strongly Recommended

- [ ] Abstract five-element check is incomplete; missing background, conclusion, quantitative results ([Script]; abstract)
- [ ] Comparison protocol should make fairness assumptions explicit ([LLM]; experiment)
- [ ] Result claims should identify comparison scope and uncertainty ([LLM]; experiment)
- [ ] Cross-section numeric consistency should be reconciled ([LLM]; introduction)
- [ ] Novelty claim should be grounded against the closest prior work ([LLM]; related_work)

### Priority 3 --- Optional Improvements

- [ ] Conclusion should close the loop on the paper's strongest claims ([LLM]; conclusion)
