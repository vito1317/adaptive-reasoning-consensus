# 深度审稿报告

**论文**: `/Users/vito/development/adaptive-reasoning-consensus/paper/tact_jmlr.pdf` | **语言**: ZH | **模式**: deep-review
**生成时间**: 2026-08-05 04:51 | **目标期刊**: jmlr
**工件目录**: `/Users/vito/development/adaptive-reasoning-consensus/paper/review_results/jmlr_round12/tact-jmlr`

## 总体评估

Deep review found 1 major, 6 moderate, 0 minor issues. The highest-priority concerns are: Abstract and conclusion claims need explicit evidence traceability; Cross-section numeric consistency should be reconciled.

- **主要**: 1
- **中等**: 6
- **次要**: 0

## 学术预审委员会

### 主编（直接拒稿筛查）

## Editor Pre-Screen (1-10)

Score: 4.0/10
Verdict: Desk Reject

### Desk-Reject Triggers (if any)
- Abstract and conclusion claims need explicit evidence traceability

### Top 3 Reasons (no hedging)
1. Abstract and conclusion claims need explicit evidence traceability

### Fast Fixes (within 1-2 days)
- Clarify abstract to address abstract and conclusion claims need explicit evidence traceability.
- Clarify abstract to address cross-section numeric consistency should be reconciled.
- Clarify abstract to address em dash found; replace it with a comma, colon, parenthesis, or sentence boundary unless it is....

### 评审 1（理论贡献）

## Theory Contribution Review

### 3 Fatal Theory Holes
1. (abstract) "The dev-calibrated variant must therefore be positioned honestly: CISC’s tuned temperature is already a dev-calibrated sc↔CISC interpolation, so the novelty of tact-dev lies in the sign, the rank invariance, and the analytic (grid-free) map, not in dev calibration itself." — At least one headline claim was detected. Deep review should check whether experiments and conclusion language trace back to the same bounded evidence base.
2. (abstract) "2 Related Work Confidence-weighted self-consistency." — The paper positions itself against prior work, but the current wording should make the closest comparator and the real novelty delta explicit instead of relying on broad superiority language.

### Concrete Moves
- Tighten the paper's theoretical positioning in abstract to resolve abstract and conclusion claims need explicit evidence traceability.
- Tighten the paper's theoretical positioning in abstract to resolve novelty claim should be grounded against the closest prior work.

### 评审 3（文献对话）

## Literature Dialogue Review

### Closest Prior Work Risks
- (abstract) "2 Related Work Confidence-weighted self-consistency." — The paper positions itself against prior work, but the current wording should make the closest comparator and the real novelty delta explicit instead of relying on broad superiority language.

### Gap Claim Risks
- The claimed gap should be defended more explicitly: Novelty claim should be grounded against the closest prior work.

### Fast Fixes
- Name the closest prior comparator in abstract and explain the real novelty delta.

### 评审 2（方法与透明度）

## Methodology Transparency Review (SRQR-aware)

### MUST-FIX (submission blockers)
- No methodology blocker was surfaced by the fallback pass.

### SHOULD-FIX (quality improvements)
- (abstract) "tact derives the vote exponent from the measured signed within- item discrimination of the channel: a pooled van Elteren Somers’ D, shrunk toward zero and mapped through a Bayes-discriminant link that at base rate 1 2 collapses to γ = z √ 2 + z2." — Multiple sections contain numeric claims. Confirm that the same quantities reconcile across main text, tables, and appendix material.
- (method) "Method Accuracy net vs." — Comparative evaluation language was detected. Deep review should verify that baseline tuning, data splits, and reporting conventions are described symmetrically.

### SRQR Checklist Deltas
- Sampling rationale: clarify how the evidence base supports the paper's strongest claims.
- Data collection details (time/place/duration): add context when results depend on specific settings.
- Coding process (stages, coders, disagreement resolution): specify if qualitative or hybrid analysis is used.
- Saturation: state whether the evidence scope is exhaustive or bounded.
- Triangulation: explain whether multiple evidence sources were reconciled.
- Reflexivity: acknowledge researcher choices that shape interpretation.

### 评审 4（逻辑链）

## Logic Chain Review

### Breakpoints
- (abstract) "The dev-calibrated variant must therefore be positioned honestly: CISC’s tuned temperature is already a dev-calibrated sc↔CISC interpolation, so the novelty of tact-dev lies in the sign, the rank invariance, and the analytic (grid-free) map, not in dev calibration itself." — At least one headline claim was detected. Deep review should check whether experiments and conclusion language trace back to the same bounded evidence base.

### Structural Fix Moves
- Add one explicit bridge sentence in abstract so the argument chain closes cleanly.

### 委员会共识

## Committee Consensus

Overall Score: 3.3/10
Editor Verdict: Desk Reject

### Score Formula
- base 9.0
- minus 1.5 * major (1)
- minus 0.7 * moderate (6)
- minus 0.2 * minor (0)
- floor 1.0
- desk reject cap 4.0

### Top 3 Issues To Fix First
1. Abstract and conclusion claims need explicit evidence traceability
2. Cross-section numeric consistency should be reconciled
3. Em dash found; replace it with a comma, colon, parenthesis, or sentence boundary unless it is...

## 论文摘要

# Paper Summary: tact_jmlr

## Research Question
- Confidence-weighted self-consistency beats majority voting when a frozen model’s confi- dence is calibrated in direction

## Core Thesis
- This paper frames the problem as estimating one scalar: the signed within-item discrim- ination of the confidence channel, and mapping that scalar, with its uncertainty, to a vote exponent.

## Headline Claims
- This paper frames the problem as estimating one scalar: the signed within-item discrim- ination of the confidence channel, and mapping that scalar, with its uncertainty, to a vote exponent.
- None of these searches a negative exponent: the obstruction is a sign bit in the hyperparameter grid rather than the weight family itself, as this paper’s own SignGrid-dev baseline shows by opening the same cγ family to negative γ and reaching the signed oracle across the negative half-axis.

## Section Map
- abstract (6-229): 1960 words
- method (1083-1552): 3409 words

## Closure Targets
- No closure target was extracted automatically.

## 主要问题

### M1: Abstract and conclusion claims need explicit evidence traceability
- **类型**: claim_accuracy
- **来源**: [LLM] via `claims_vs_evidence`
- **置信度**: medium
- **章节**: abstract
- **关联章节**: abstract, results, conclusion
- **根因键**: `abstract-and-conclusion-claims-need-explicit-evidence-traceability`
- **原文已核对**: 否
- **原文**: `The dev-calibrated variant must therefore be positioned honestly: CISC’s tuned temperature is already a dev-calibrated sc↔CISC interpolation, so the novelty of tact-dev lies in the sign, the rank invariance, and the analytic (grid-free) map, not in dev calibration itself.`
- **说明**: At least one headline claim was detected. Deep review should check whether experiments and conclusion language trace back to the same bounded evidence base.

## 中等问题

### M1: Em dash found; replace it with a comma, colon, parenthesis, or sentence boundary unless it is...
- **类型**: presentation
- **来源**: [Script] via `pre_submission_readiness`
- **置信度**: high
- **章节**: abstract
- **关联章节**: abstract
- **根因键**: `presubmission-g1`
- **原文已核对**: 否
- **原文**: —
- **说明**: [G1] Em dash found; replace it with a comma, colon, parenthesis, or sentence boundary unless it is part of a preserved quotation. This is a mechanical pre-submission readiness finding and should be fixed before the final submission package.

### M2: Em dash found; replace it with a comma, colon, parenthesis, or sentence boundary unless it is...
- **类型**: presentation
- **来源**: [Script] via `pre_submission_readiness`
- **置信度**: high
- **章节**: method
- **关联章节**: method
- **根因键**: `presubmission-g1`
- **原文已核对**: 否
- **原文**: —
- **说明**: [G1] Em dash found; replace it with a comma, colon, parenthesis, or sentence boundary unless it is part of a preserved quotation. This is a mechanical pre-submission readiness finding and should be fixed before the final submission package.

### M3: Em dash found; replace it with a comma, colon, parenthesis, or sentence boundary unless it is...
- **类型**: presentation
- **来源**: [Script] via `pre_submission_readiness`
- **置信度**: high
- **章节**: unknown
- **关联章节**: unknown
- **根因键**: `presubmission-g1`
- **原文已核对**: 否
- **原文**: —
- **说明**: [G1] Em dash found; replace it with a comma, colon, parenthesis, or sentence boundary unless it is part of a preserved quotation. This is a mechanical pre-submission readiness finding and should be fixed before the final submission package.

### M4: Cross-section numeric consistency should be reconciled
- **类型**: presentation
- **来源**: [LLM] via `notation_and_numeric_consistency`
- **置信度**: medium
- **章节**: abstract
- **关联章节**: abstract, method
- **根因键**: `cross-section-numeric-consistency-should-be-reconciled`
- **原文已核对**: 否
- **原文**: `tact derives the vote exponent from the measured signed within- item discrimination of the channel: a pooled van Elteren Somers’ D, shrunk toward zero and mapped through a Bayes-discriminant link that at base rate 1 2 collapses to γ = z √ 2 + z2.`
- **说明**: Multiple sections contain numeric claims. Confirm that the same quantities reconcile across main text, tables, and appendix material.

### M5: Novelty claim should be grounded against the closest prior work
- **类型**: claim_accuracy
- **来源**: [LLM] via `prior_art_and_novelty_grounding`
- **置信度**: medium
- **章节**: abstract
- **关联章节**: abstract, results
- **根因键**: `novelty-claim-should-be-grounded-against-the-closest-prior-work`
- **原文已核对**: 否
- **原文**: `2 Related Work Confidence-weighted self-consistency.`
- **说明**: The paper positions itself against prior work, but the current wording should make the closest comparator and the real novelty delta explicit instead of relying on broad superiority language.

### M6: Comparison protocol should make fairness assumptions explicit
- **类型**: methodology
- **来源**: [LLM] via `evaluation_fairness_and_reproducibility`
- **置信度**: medium
- **章节**: method
- **关联章节**: method
- **根因键**: `comparison-protocol-should-make-fairness-assumptions-explicit`
- **原文已核对**: 否
- **原文**: `Method Accuracy net vs.`
- **说明**: Comparative evaluation language was detected. Deep review should verify that baseline tuning, data splits, and reporting conventions are described symmetrically.

## Phase 0 自动审查发现

### [Script] BIB

| 行号 | 严重度 | 问题 |
|------|--------|------|
| --- | Minor | Check: /Users/vito/development/adaptive-reasoning-consensus/paper/tact_jmlr.pdf |
| --- | Minor | WARNING |
| --- | Minor | @-: tact_jmlr.pdf: 编码异常，部分字符无法解码（已替换为 �），结果可能不完整 |
| --- | Minor | 3 entries missing DOI/URL (Use --online-check to export list) |

### [Script] CONSISTENCY

| 行号 | 严重度 | 问题 |
|------|--------|------|
| --- | Minor | Checking 1 files... |
| --- | Minor | ============================================================ |
| --- | Minor | Check Report / 一致性检查报告 |
| --- | Minor | ============================================================ |
| --- | Minor | Term Consistency / 术语一致性 |
| --- | Minor | ✅ No inconsistencies found |
| --- | Minor | Abbreviation Check / 缩略语检查 |
| --- | Minor | ⚠️ 257 issues found |
| --- | Minor | 'LG' used but not defined (first at tact_jmlr.pdf:8) |
| --- | Minor | 'QS' used but not defined (first at tact_jmlr.pdf:10) |
| --- | Minor | 'WY' used but not defined (first at tact_jmlr.pdf:13) |
| --- | Minor | 'VW' used but not defined (first at tact_jmlr.pdf:14) |
| --- | Minor | 'IX' used but not defined (first at tact_jmlr.pdf:17) |
| --- | Minor | 'EW' used but not defined (first at tact_jmlr.pdf:18) |
| --- | Minor | 'XM' used but not defined (first at tact_jmlr.pdf:29) |
| --- | Minor | 'XK' used but not defined (first at tact_jmlr.pdf:31) |
| --- | Minor | 'PV' used but not defined (first at tact_jmlr.pdf:36) |
| --- | Minor | 'HB' used but not defined (first at tact_jmlr.pdf:36) |
| --- | Minor | 'DU' used but not defined (first at tact_jmlr.pdf:38) |
| --- | Minor | 'TF' used but not defined (first at tact_jmlr.pdf:40) |
| --- | Minor | 'MT' used but not defined (first at tact_jmlr.pdf:40) |
| --- | Minor | 'LJ' used but not defined (first at tact_jmlr.pdf:45) |
| --- | Minor | 'BE' used but not defined (first at tact_jmlr.pdf:51) |
| --- | Minor | 'WV' used but not defined (first at tact_jmlr.pdf:52) |
| --- | Minor | 'PW' used but not defined (first at tact_jmlr.pdf:52) |
| --- | Minor | 'EH' used but not defined (first at tact_jmlr.pdf:54) |
| --- | Minor | 'UT' used but not defined (first at tact_jmlr.pdf:62) |
| --- | Minor | 'DK' used but not defined (first at tact_jmlr.pdf:65) |
| --- | Minor | 'MA' used but not defined (first at tact_jmlr.pdf:67) |
| --- | Minor | 'VV' used but not defined (first at tact_jmlr.pdf:67) |
| --- | Minor | 'LZ' used but not defined (first at tact_jmlr.pdf:68) |
| --- | Minor | 'XJ' used but not defined (first at tact_jmlr.pdf:68) |
| --- | Minor | 'IY' used but not defined (first at tact_jmlr.pdf:70) |
| --- | Minor | 'JC' used but not defined (first at tact_jmlr.pdf:71) |
| --- | Minor | 'CJ' used but not defined (first at tact_jmlr.pdf:72) |
| --- | Minor | 'NY' used but not defined (first at tact_jmlr.pdf:85) |
| --- | Minor | 'FV' used but not defined (first at tact_jmlr.pdf:89) |
| --- | Minor | 'YH' used but not defined (first at tact_jmlr.pdf:92) |
| --- | Minor | 'SC' used but not defined (first at tact_jmlr.pdf:92) |
| --- | Minor | 'II' used but not defined (first at tact_jmlr.pdf:95) |
| --- | Minor | 'JW' used but not defined (first at tact_jmlr.pdf:99) |
| --- | Minor | 'ZB' used but not defined (first at tact_jmlr.pdf:100) |
| --- | Minor | 'XA' used but not defined (first at tact_jmlr.pdf:106) |
| --- | Minor | 'YVR' used but not defined (first at tact_jmlr.pdf:107) |
| --- | Minor | 'WG' used but not defined (first at tact_jmlr.pdf:110) |
| --- | Minor | 'XD' used but not defined (first at tact_jmlr.pdf:110) |
| --- | Minor | 'DH' used but not defined (first at tact_jmlr.pdf:112) |
| --- | Minor | 'MW' used but not defined (first at tact_jmlr.pdf:114) |
| --- | Minor | 'YQ' used but not defined (first at tact_jmlr.pdf:114) |
| --- | Minor | 'IA' used but not defined (first at tact_jmlr.pdf:115) |
| --- | Minor | 'WN' used but not defined (first at tact_jmlr.pdf:115) |
| --- | Minor | 'XY' used but not defined (first at tact_jmlr.pdf:137) |
| --- | Minor | 'NB' used but not defined (first at tact_jmlr.pdf:138) |
| --- | Minor | 'FW' used but not defined (first at tact_jmlr.pdf:141) |
| --- | Minor | 'EE' used but not defined (first at tact_jmlr.pdf:142) |
| --- | Minor | 'LV' used but not defined (first at tact_jmlr.pdf:146) |
| --- | Minor | 'WQ' used but not defined (first at tact_jmlr.pdf:146) |
| --- | Minor | 'KQ' used but not defined (first at tact_jmlr.pdf:147) |
| --- | Minor | 'IK' used but not defined (first at tact_jmlr.pdf:147) |
| --- | Minor | 'BN' used but not defined (first at tact_jmlr.pdf:160) |
| --- | Minor | 'BU' used but not defined (first at tact_jmlr.pdf:160) |
| --- | Minor | 'NS' used but not defined (first at tact_jmlr.pdf:171) |
| --- | Minor | 'ZL' used but not defined (first at tact_jmlr.pdf:171) |
| --- | Minor | 'OX' used but not defined (first at tact_jmlr.pdf:172) |
| --- | Minor | 'IM' used but not defined (first at tact_jmlr.pdf:175) |
| --- | Minor | 'TP' used but not defined (first at tact_jmlr.pdf:182) |
| --- | Minor | 'GD' used but not defined (first at tact_jmlr.pdf:201) |
| --- | Minor | 'TT' used but not defined (first at tact_jmlr.pdf:202) |
| --- | Minor | 'CY' used but not defined (first at tact_jmlr.pdf:202) |
| --- | Minor | 'RLEU' used but not defined (first at tact_jmlr.pdf:214) |
| --- | Minor | 'PT' used but not defined (first at tact_jmlr.pdf:220) |
| --- | Minor | 'YX' used but not defined (first at tact_jmlr.pdf:220) |
| --- | Minor | 'DI' used but not defined (first at tact_jmlr.pdf:220) |
| --- | Minor | 'DV' used but not defined (first at tact_jmlr.pdf:221) |
| --- | Minor | 'VA' used but not defined (first at tact_jmlr.pdf:221) |
| --- | Minor | 'FK' used but not defined (first at tact_jmlr.pdf:224) |
| --- | Minor | 'RJ' used but not defined (first at tact_jmlr.pdf:283) |
| --- | Minor | 'OE' used but not defined (first at tact_jmlr.pdf:283) |
| --- | Minor | 'VI' used but not defined (first at tact_jmlr.pdf:283) |
| --- | Minor | 'ZU' used but not defined (first at tact_jmlr.pdf:291) |
| --- | Minor | 'FF' used but not defined (first at tact_jmlr.pdf:292) |
| --- | Minor | 'ZK' used but not defined (first at tact_jmlr.pdf:298) |
| --- | Minor | 'EO' used but not defined (first at tact_jmlr.pdf:299) |
| --- | Minor | 'ZS' used but not defined (first at tact_jmlr.pdf:304) |
| --- | Minor | 'SH' used but not defined (first at tact_jmlr.pdf:314) |
| --- | Minor | 'CL' used but not defined (first at tact_jmlr.pdf:321) |
| --- | Minor | 'YZ' used but not defined (first at tact_jmlr.pdf:323) |
| --- | Minor | 'JP' used but not defined (first at tact_jmlr.pdf:323) |
| --- | Minor | 'ZD' used but not defined (first at tact_jmlr.pdf:324) |
| --- | Minor | 'LL' used but not defined (first at tact_jmlr.pdf:325) |
| --- | Minor | 'IV' used but not defined (first at tact_jmlr.pdf:326) |
| --- | Minor | 'XU' used but not defined (first at tact_jmlr.pdf:329) |
| --- | Minor | 'OP' used but not defined (first at tact_jmlr.pdf:329) |
| --- | Minor | 'OJ' used but not defined (first at tact_jmlr.pdf:335) |
| --- | Minor | 'YK' used but not defined (first at tact_jmlr.pdf:335) |
| --- | Minor | 'UE' used but not defined (first at tact_jmlr.pdf:335) |
| --- | Minor | 'AK' used but not defined (first at tact_jmlr.pdf:338) |
| --- | Minor | 'WP' used but not defined (first at tact_jmlr.pdf:358) |
| --- | Minor | 'YD' used but not defined (first at tact_jmlr.pdf:358) |
| --- | Minor | 'RB' used but not defined (first at tact_jmlr.pdf:360) |
| --- | Minor | 'OW' used but not defined (first at tact_jmlr.pdf:362) |
| --- | Minor | 'BB' used but not defined (first at tact_jmlr.pdf:362) |
| --- | Minor | 'FN' used but not defined (first at tact_jmlr.pdf:367) |
| --- | Minor | 'MO' used but not defined (first at tact_jmlr.pdf:377) |
| --- | Minor | 'BR' used but not defined (first at tact_jmlr.pdf:379) |
| --- | Minor | 'CV' used but not defined (first at tact_jmlr.pdf:381) |
| --- | Minor | 'HO' used but not defined (first at tact_jmlr.pdf:387) |
| --- | Minor | 'ZT' used but not defined (first at tact_jmlr.pdf:390) |
| --- | Minor | 'QE' used but not defined (first at tact_jmlr.pdf:397) |
| --- | Minor | 'QF' used but not defined (first at tact_jmlr.pdf:404) |
| --- | Minor | 'TB' used but not defined (first at tact_jmlr.pdf:409) |
| --- | Minor | 'US' used but not defined (first at tact_jmlr.pdf:411) |
| --- | Minor | 'BX' used but not defined (first at tact_jmlr.pdf:411) |
| --- | Minor | 'RA' used but not defined (first at tact_jmlr.pdf:411) |
| --- | Minor | 'IP' used but not defined (first at tact_jmlr.pdf:414) |
| --- | Minor | 'XG' used but not defined (first at tact_jmlr.pdf:422) |
| --- | Minor | 'AS' used but not defined (first at tact_jmlr.pdf:427) |
| --- | Minor | 'SG' used but not defined (first at tact_jmlr.pdf:437) |
| --- | Minor | 'TZ' used but not defined (first at tact_jmlr.pdf:437) |
| --- | Minor | 'JJ' used but not defined (first at tact_jmlr.pdf:437) |
| --- | Minor | 'UD' used but not defined (first at tact_jmlr.pdf:437) |
| --- | Minor | 'DR' used but not defined (first at tact_jmlr.pdf:440) |
| --- | Minor | 'GI' used but not defined (first at tact_jmlr.pdf:441) |
| --- | Minor | 'ZH' used but not defined (first at tact_jmlr.pdf:449) |
| --- | Minor | 'KP' used but not defined (first at tact_jmlr.pdf:449) |
| --- | Minor | 'UK' used but not defined (first at tact_jmlr.pdf:449) |
| --- | Minor | 'JK' used but not defined (first at tact_jmlr.pdf:450) |
| --- | Minor | 'CP' used but not defined (first at tact_jmlr.pdf:450) |
| --- | Minor | 'MH' used but not defined (first at tact_jmlr.pdf:450) |
| --- | Minor | 'NU' used but not defined (first at tact_jmlr.pdf:450) |
| --- | Minor | 'EQ' used but not defined (first at tact_jmlr.pdf:488) |
| --- | Minor | 'GQ' used but not defined (first at tact_jmlr.pdf:494) |
| --- | Minor | 'QL' used but not defined (first at tact_jmlr.pdf:498) |
| --- | Minor | 'GA' used but not defined (first at tact_jmlr.pdf:502) |
| --- | Minor | 'RS' used but not defined (first at tact_jmlr.pdf:503) |
| --- | Minor | 'EX' used but not defined (first at tact_jmlr.pdf:505) |
| --- | Minor | 'ZE' used but not defined (first at tact_jmlr.pdf:505) |
| --- | Minor | 'RZ' used but not defined (first at tact_jmlr.pdf:505) |
| --- | Minor | 'FB' used but not defined (first at tact_jmlr.pdf:509) |
| --- | Minor | 'KI' used but not defined (first at tact_jmlr.pdf:509) |
| --- | Minor | 'ZC' used but not defined (first at tact_jmlr.pdf:511) |
| --- | Minor | 'QH' used but not defined (first at tact_jmlr.pdf:515) |
| --- | Minor | 'RW' used but not defined (first at tact_jmlr.pdf:515) |
| --- | Minor | 'WZ' used but not defined (first at tact_jmlr.pdf:515) |
| --- | Minor | 'KT' used but not defined (first at tact_jmlr.pdf:515) |
| --- | Minor | 'GN' used but not defined (first at tact_jmlr.pdf:519) |
| --- | Minor | 'MU' used but not defined (first at tact_jmlr.pdf:520) |
| --- | Minor | 'OF' used but not defined (first at tact_jmlr.pdf:612) |
| --- | Minor | 'DY' used but not defined (first at tact_jmlr.pdf:618) |
| --- | Minor | 'TY' used but not defined (first at tact_jmlr.pdf:619) |
| --- | Minor | 'LD' used but not defined (first at tact_jmlr.pdf:622) |
| --- | Minor | 'RP' used but not defined (first at tact_jmlr.pdf:637) |
| --- | Minor | 'TD' used but not defined (first at tact_jmlr.pdf:637) |
| --- | Minor | 'UX' used but not defined (first at tact_jmlr.pdf:645) |
| --- | Minor | 'MK' used but not defined (first at tact_jmlr.pdf:647) |
| --- | Minor | 'WF' used but not defined (first at tact_jmlr.pdf:651) |
| --- | Minor | 'YU' used but not defined (first at tact_jmlr.pdf:651) |
| --- | Minor | 'DJ' used but not defined (first at tact_jmlr.pdf:651) |
| --- | Minor | 'CD' used but not defined (first at tact_jmlr.pdf:652) |
| --- | Minor | 'YF' used but not defined (first at tact_jmlr.pdf:654) |
| --- | Minor | 'KL' used but not defined (first at tact_jmlr.pdf:656) |
| --- | Minor | 'JU' used but not defined (first at tact_jmlr.pdf:661) |
| --- | Minor | 'MB' used but not defined (first at tact_jmlr.pdf:673) |
| --- | Minor | 'XW' used but not defined (first at tact_jmlr.pdf:674) |
| --- | Minor | 'KV' used but not defined (first at tact_jmlr.pdf:691) |
| --- | Minor | 'BT' used but not defined (first at tact_jmlr.pdf:697) |
| --- | Minor | 'HY' used but not defined (first at tact_jmlr.pdf:708) |
| --- | Minor | 'IH' used but not defined (first at tact_jmlr.pdf:715) |
| --- | Minor | 'PK' used but not defined (first at tact_jmlr.pdf:717) |
| --- | Minor | 'VB' used but not defined (first at tact_jmlr.pdf:727) |
| --- | Minor | 'RD' used but not defined (first at tact_jmlr.pdf:730) |
| --- | Minor | 'BJ' used but not defined (first at tact_jmlr.pdf:733) |
| --- | Minor | 'EF' used but not defined (first at tact_jmlr.pdf:733) |
| --- | Minor | 'JF' used but not defined (first at tact_jmlr.pdf:733) |
| --- | Minor | 'WU' used but not defined (first at tact_jmlr.pdf:781) |
| --- | Minor | 'SJ' used but not defined (first at tact_jmlr.pdf:784) |
| --- | Minor | 'OA' used but not defined (first at tact_jmlr.pdf:795) |
| --- | Minor | 'ZG' used but not defined (first at tact_jmlr.pdf:795) |
| --- | Minor | 'QQ' used but not defined (first at tact_jmlr.pdf:795) |
| --- | Minor | 'XL' used but not defined (first at tact_jmlr.pdf:806) |
| --- | Minor | 'OB' used but not defined (first at tact_jmlr.pdf:808) |
| --- | Minor | 'FC' used but not defined (first at tact_jmlr.pdf:829) |
| --- | Minor | 'VZ' used but not defined (first at tact_jmlr.pdf:829) |
| --- | Minor | 'CB' used but not defined (first at tact_jmlr.pdf:830) |
| --- | Minor | 'RL' used but not defined (first at tact_jmlr.pdf:840) |
| --- | Minor | 'MG' used but not defined (first at tact_jmlr.pdf:840) |
| --- | Minor | 'MM' used but not defined (first at tact_jmlr.pdf:847) |
| --- | Minor | 'CO' used but not defined (first at tact_jmlr.pdf:865) |
| --- | Minor | 'XX' used but not defined (first at tact_jmlr.pdf:879) |
| --- | Minor | 'XS' used but not defined (first at tact_jmlr.pdf:879) |
| --- | Minor | 'AQ' used but not defined (first at tact_jmlr.pdf:879) |
| --- | Minor | 'EU' used but not defined (first at tact_jmlr.pdf:896) |
| --- | Minor | 'JN' used but not defined (first at tact_jmlr.pdf:899) |
| --- | Minor | 'IJ' used but not defined (first at tact_jmlr.pdf:908) |
| --- | Minor | 'SD' used but not defined (first at tact_jmlr.pdf:933) |
| --- | Minor | 'PQ' used but not defined (first at tact_jmlr.pdf:937) |
| --- | Minor | 'YM' used but not defined (first at tact_jmlr.pdf:945) |
| --- | Minor | 'BH' used but not defined (first at tact_jmlr.pdf:951) |
| --- | Minor | 'HA' used but not defined (first at tact_jmlr.pdf:951) |
| --- | Minor | 'ZQ' used but not defined (first at tact_jmlr.pdf:967) |
| --- | Minor | 'AA' used but not defined (first at tact_jmlr.pdf:979) |
| --- | Minor | 'SK' used but not defined (first at tact_jmlr.pdf:984) |
| --- | Minor | 'PL' used but not defined (first at tact_jmlr.pdf:1004) |
| --- | Minor | 'NF' used but not defined (first at tact_jmlr.pdf:1005) |
| --- | Minor | 'HN' used but not defined (first at tact_jmlr.pdf:1005) |
| --- | Minor | 'KA' used but not defined (first at tact_jmlr.pdf:1007) |
| --- | Minor | 'UP' used but not defined (first at tact_jmlr.pdf:1008) |
| --- | Minor | 'ZA' used but not defined (first at tact_jmlr.pdf:1011) |
| --- | Minor | 'OI' used but not defined (first at tact_jmlr.pdf:1013) |
| --- | Minor | 'PO' used but not defined (first at tact_jmlr.pdf:1033) |
| --- | Minor | 'YS' used but not defined (first at tact_jmlr.pdf:1040) |
| --- | Minor | 'KC' used but not defined (first at tact_jmlr.pdf:1081) |
| --- | Minor | 'JS' used but not defined (first at tact_jmlr.pdf:1101) |
| --- | Minor | 'YY' used but not defined (first at tact_jmlr.pdf:1101) |
| --- | Minor | 'FO' used but not defined (first at tact_jmlr.pdf:1104) |
| --- | Minor | 'RG' used but not defined (first at tact_jmlr.pdf:1105) |
| --- | Minor | 'BM' used but not defined (first at tact_jmlr.pdf:1129) |
| --- | Minor | 'KE' used but not defined (first at tact_jmlr.pdf:1141) |
| --- | Minor | 'TV' used but not defined (first at tact_jmlr.pdf:1143) |
| --- | Minor | 'FS' used but not defined (first at tact_jmlr.pdf:1163) |
| --- | Minor | 'UY' used but not defined (first at tact_jmlr.pdf:1176) |
| --- | Minor | 'IN' used but not defined (first at tact_jmlr.pdf:1176) |
| --- | Minor | 'NE' used but not defined (first at tact_jmlr.pdf:1178) |
| --- | Minor | 'IO' used but not defined (first at tact_jmlr.pdf:1178) |
| --- | Minor | 'JT' used but not defined (first at tact_jmlr.pdf:1178) |
| --- | Minor | 'ST' used but not defined (first at tact_jmlr.pdf:1192) |
| --- | Minor | 'LO' used but not defined (first at tact_jmlr.pdf:1203) |
| --- | Minor | 'ER' used but not defined (first at tact_jmlr.pdf:1215) |
| --- | Minor | 'TS' used but not defined (first at tact_jmlr.pdf:1250) |
| --- | Minor | 'AM' used but not defined (first at tact_jmlr.pdf:1252) |
| --- | Minor | 'AW' used but not defined (first at tact_jmlr.pdf:1254) |
| --- | Minor | 'DE' used but not defined (first at tact_jmlr.pdf:1274) |
| --- | Minor | 'JD' used but not defined (first at tact_jmlr.pdf:1320) |
| --- | Minor | 'PB' used but not defined (first at tact_jmlr.pdf:1339) |
| --- | Minor | 'FQ' used but not defined (first at tact_jmlr.pdf:1340) |
| --- | Minor | 'OZ' used but not defined (first at tact_jmlr.pdf:1340) |
| --- | Minor | 'UU' used but not defined (first at tact_jmlr.pdf:1341) |
| --- | Minor | 'ZZ' used but not defined (first at tact_jmlr.pdf:1357) |
| --- | Minor | 'PR' used but not defined (first at tact_jmlr.pdf:1392) |
| --- | Minor | 'HQ' used but not defined (first at tact_jmlr.pdf:1394) |
| --- | Minor | 'QT' used but not defined (first at tact_jmlr.pdf:1411) |
| --- | Minor | 'JY' used but not defined (first at tact_jmlr.pdf:1497) |
| --- | Minor | 'RU' used but not defined (first at tact_jmlr.pdf:1520) |
| --- | Minor | 'YT' used but not defined (first at tact_jmlr.pdf:1535) |
| --- | Minor | 'OL' used but not defined (first at tact_jmlr.pdf:1614) |
| --- | Minor | 'BG' used but not defined (first at tact_jmlr.pdf:1614) |
| --- | Minor | 'FI' used but not defined (first at tact_jmlr.pdf:1617) |
| --- | Minor | 'GJ' used but not defined (first at tact_jmlr.pdf:1630) |
| --- | Minor | 'XO' used but not defined (first at tact_jmlr.pdf:1645) |
| --- | Minor | 'FP' used but not defined (first at tact_jmlr.pdf:1665) |
| --- | Minor | 'AC' used but not defined (first at tact_jmlr.pdf:1666) |
| --- | Minor | 'GK' used but not defined (first at tact_jmlr.pdf:1674) |
| --- | Minor | 'WL' used but not defined (first at tact_jmlr.pdf:1676) |
| --- | Minor | 'OH' used but not defined (first at tact_jmlr.pdf:1730) |
| --- | Minor | 'EN' used but not defined (first at tact_jmlr.pdf:1734) |
| --- | Minor | 'EK' used but not defined (first at tact_jmlr.pdf:1758) |
| --- | Minor | 'PS' used but not defined (first at tact_jmlr.pdf:1792) |
| --- | Minor | 'FG' used but not defined (first at tact_jmlr.pdf:1843) |
| --- | Minor | 'RR' used but not defined (first at tact_jmlr.pdf:1895) |
| --- | Minor | 'ID' used but not defined (first at tact_jmlr.pdf:1935) |
| --- | Minor | 'WI' used but not defined (first at tact_jmlr.pdf:1940) |
| --- | Minor | 'DL' used but not defined (first at tact_jmlr.pdf:2006) |
| --- | Minor | 'DM' used but not defined (first at tact_jmlr.pdf:2016) |
| --- | Minor | 'YJ' used but not defined (first at tact_jmlr.pdf:2034) |
| --- | Minor | 'PA' used but not defined (first at tact_jmlr.pdf:2110) |
| --- | Minor | ============================================================ |

### [Script] DEAI

| 行号 | 严重度 | 问题 |
|------|--------|------|
| --- | Minor | 使用 --analyze 进行完整文档分析 |

### [Script] EXPERIMENT

| 行号 | 严重度 | 问题 |
|------|--------|------|
| --- | Minor | ，生成符合中文顶刊与学位论文标准的完美实验分析段落。 |
| --- | Minor | `references/modules/experiment.md` 中的所有约束条件。 |
| --- | Minor | 强制使用 `\paragraph{核心结论概括}` 引导段落。 |
| --- | Minor | 正文中**禁止**任何 `\textbf{}` 等显式加粗。 |
| --- | Minor | **禁止**使用列表环境 (`\begin{itemize}`) 罗列数据，需串联成连贯的论述段落。 |
| --- | Minor | 包含 SOTA 对比、消融结论，并确保具有深度的比较逻辑而不仅是报数字。 |
| --- | Minor | 极致客观、去口语化，严禁出现“碾压、遥遥领先”等夸张词汇及主观代词。 |
| --- | Minor | 1.5 |
| --- | Minor | 0 obj |
| --- | Minor | <</Filter/FlateDecode/Length 4512>> |
| --- | Minor | ɮ$9W[%v8E#p$8!;Z=UUp=ߞ"[.p͗/oO&@ӗuf)f;}lLHg.`eccIπ>ݻ1ޖH+)#]GPF_}CO=&zۗ?~N7t |
| --- | Minor | ,-ݹ|qЀ*[W#fzqǇvzqXzc·'nS |
| --- | Minor | ڶlj73`heu90;Xw+<D#d5LG7<[~/*`㭰d͖M6)b@<}-ҷvh/fauZ&pzgݶ>^$Gr\MW	1pRO \lC_AlA/߿O؇$` C2\Rk76δݽqmf/!n>%Vsm{l%"&øȄ _4 _EL_Z&ޭ+սn8wēf ކJO |
| --- | Minor | !Mez9q#	ٜϖxI} |
| --- | Minor | apC-a%l2i.oKy]t|f-f!|/Y~"BOa9IYa򴎫J6p>ACP\ |
| --- | Minor | /tsWhVm(2<q+YF.3DE'9d:GU|X4b~!(fJ9*(a|c3O^}ض{B{a*vNVvFuIdLYww턕;Q[~ee{ZY |
| --- | Minor | \3Q(d-TƮץYvs*uxp287+k;|4 |
| --- | Minor | l'H)*h( .DV^]:-O0Y6Y |
| --- | Minor | (Z |
| --- | Minor | Xjk9/C ~sI[8*y&b3-ö+ݺmL,KkM% |
| --- | Minor | Pmx&F#9sVd |
| --- | Minor | *DGSwn} |
| --- | Minor | a_ N,橴$fښfxIiQ{h]<0 |
| --- | Minor | + &ĴdRsu?)0T) h9Yt< ~4@XO6x)-)ߤkm.p>F b`b^d"!,ZXp;l̆2vb7V`wj!;-Gz(l'[l?0ߧe'#5'?qOq釖Ӌ۬pR.# |
| --- | Minor | Pn9Js؞Df^ @!QS@~h |
| --- | Minor | !ϵAA~ڐbLtCu࿎L!> |
| --- | Minor | k<OPO䍴fL |
| --- | Minor | $>Dec&<n+1Q9o.7 |
| --- | Minor | Zu.,ֹLhe\nvcHMwh"ќ]Yik***۝Z9NtЮ[J+Mq^!3\ Uƈ[Tױֽ;oiPaO᧒k}k- |
| --- | Minor | ͍FLYϔ7-]1W\!GH#hyCemvV{Օϒ!ݳT$YtJ(# |
| --- | Minor | *itwuioe^E̞rB*NR;oͻ_dn^8F.p+<dwh#Ο(Z#:Lm}rF?->maeg#fsڒd,JV[NV"O:4P<@<4Wd7.`# |
| --- | Minor | ONplMiLhIgq;E{,N	+`G_)!N؂yI秢L}X]AǀHw&bwLDrO~Y,WYsLpZ~vY.Tk0EbG |
| --- | Minor | g6T86fv%,1J2 {;eU5{"sUW^vUy=8e"ZJE[^ǜA#>' |
| --- | Minor | #WA&Bʶkyelݝ鴁Ms7'T0VWO2-ts$H	QuvPLt`Jo	ҽkvi?ẲB:gE<^=0G 6o= |
| --- | Minor | RKNa)Ie"7_^͒{޼zkaL4pQi	' 	kxGBFuy%:_ɛ(C,&T,Q=J%>l= |
| --- | Minor | ;B'u9Kh)&`^ j]pI?7:M	7KHNVD2q*֒nB0sT5f$ses Q,s1Z?ʻt63Z6;nBŻζ5}*{5&~/<QէK꾝ۇ^CRU05o<ڢ`]涅J'gUp\NPS!߆5`S٫e'uqT;jkI/jǳpTqaTYkNWzaTo<7}VySMloHsJҲKX:kK4kFp{0 |
| --- | Minor | l70.ݘKO\@GAh7o?>oHF ѐ=01ŞUKDp#Man)Le3=IX<g̟Um&hNѰjv: +uv{t |
| --- | Minor |  v"D;cyZ/]̬_<QJ	CY:rOp	9},^p{8`bY[{xB/h]Q^Z2EQu&G8>V׉<W[8f7'20sF5wԬL\Oֱ-wz	EWR΋I8*|O@z($4nAU[O挚'ZbÌ1wy5)F@~$Q4`geDv$'1kRsl/(moC4wv?Q#4t*_Eiݓ+N䃂#c1:]sSf.K!yZ>sQIEyC |
| --- | Minor |  |
| --- | Minor | L'm?~q 2~T,?I0;cz 2dlT"IUm֙2;,2Esix#AsEA`?qRׇ%~.z-YA彃QK3}є0,8T+v=}m:g{7s|AՕ^NՌ7o+w*<{U )+;OO#l܄q(I!Vun"ā8y؃D pd$~#5R@_GMOG|kǣ&(&7(cP5-x{tH-GhJM/f%󠥍IcZ:9fՌ*`$Egeu&b8r-sH$N2Eax[ex̺jݛ&R]B>ކݖuYI2XfcM9ȇt~wH+ ovRus?i7c~)QS{ |
| --- | Minor | [u)=+~م2G(5#.y!|j+,z]W]EaOToT2uԯO+Qzaξ0h Wc`DMh,YDZ 'dņw]9ono'XdH<MvОFo*AS1!Eca3,6@AU66uE~#z}m:~JʵU |
| --- | Minor | /\}F0oIBgIM%KKX' |
| --- | Minor | =u;YZ*-cN^ـ,cT(ҾO-GJhY"18wv-D[ѥ5(&E޸rmt5rh\Zz4Ǫ9JBRSV06NP |
| --- | Minor | ', |
| --- | Minor | Ul( |
| --- | Minor | h<g{u_Lrg.)8f܊\4 |
| --- | Minor | <~Qeeqaor`jsˤkM,X{spHOzx^z9R+F7Esx[>;.ݖ5fhJL۾c[z[w[#c8{P]:R'S+ѳ຿-ls?}w|n	I8lih#H-T+yb2)737 |
| --- | Minor | 0 obj |
| --- | Minor | <</Filter/FlateDecode/Length 5275>> |
| --- | Minor | \K$qW&#j`l7akjzaWWUvkEWf$"ȧ=''OVoxk?ӿ| |
| --- | Minor | 	@*B)O_nW˷|XM>Iqxs+ӫ<ս |
| --- | Minor | g^U/NAv%1T|2{(jskl)|)ONK+ضHI(j\Ӻ |
| --- | Minor | " |
| --- | Minor | ,4C1Dz[Pϱ8.>(,5rzc8FUO0PVF~QR/<<g:DCzk!uaf<+-Yg{ U#jVyYDM7q&lh\njRŉAbVmx"n}YlcZe |
| --- | Minor | !Kb;4"m~oVwRZӮ~W 6Ё@WUcC[jA!6 |
| --- | Minor | )XK |
| --- | Minor | #R۴@Q;5/kֵ^L< ^×"Kh:HG酡yPA**jB܉/hXDEL{!Bꦯl0o4W FF~i	vkl+z([%Ioo$&BrR⠚fE Wr,JEK4`<&@<53m|INHQ1SdfV蜝J}LIMhQ^/kYUΚމt3Ly"Thzzڦt\siC-zWYhrmU |
| --- | Minor | {g'ڎkӇW.׋5*ov0HR#Vva%MH0aVu{*?12rՀHԖF5Ns-i;Liizפ^Zl1yb͊uqks`8I5ok5-nKQ0v͹W2IܠTsB[ma"C0e |
| --- | Minor | K,Y\>8ddud0pj'C_6o6&` yӚٖq "eR-ʣRŶY:(Ⴗ&6hHn7G=vs5SnLLzy9Aߥf&x[@4?|W_M>A'x	6]Ff)8}l 9Ά`_8h`nDJ+:+cW6PFtG>2Y Yg`fmh79R`\ͪ+ :w'P[wan]b$UOc~8sHݏ |
| --- | Minor | žCy͙mWByEYٰFi=Yu2eS9突gkDuiq* [j)soS_~ejV|t]6RpA'Az"{!UB=wp4ޱse+ujdQ~"Qb3qdInh]<> |
| --- | Minor | z*:Y9KpH |
| --- | Minor | XM |
| --- | Minor | R] ( MLPV/uE.=doR8\Bu:@,hȆ2<5y;!HB>Rj5IქMAv__6UjTjUAPƂ_yR#^:amC#ڏ&ǣ"#5#2Y-wG-'Yz$p	HԥHn^yOӻ!:Z_nd}D'ZV |
| --- | Minor | ^4xSA^ͭno2|Gwᕥ"!l;8cR9502$1!Ch*s2ˠhiJ |
| --- | Minor | ,'vdDU%B*cNvA$``q囊кDKpCS&G6${THEz1^>M |
| --- | Minor |  |
| --- | Minor | ">r<S=h |
| --- | Minor | h"a[-;a!@*jVFF-F]u+7vn5 DDa[ q,8zq4zMgǟhHax;|1EJܚTFu7}-:F#3-kjW5-o:eksKx-nnq((Bx0*MTNڥ5 |
| --- | Minor | $1/Yiyab-Rx8.SUɌǄ{zK 藛9+9^vBzCʭi[D`S{W&8>`Ҽ51v9$EI	$Czy%$(qy5reAܞ#`D [" |
| --- | Minor | /k܂`PꏢkóJ\4vd0h*%Q-zBrx2g#HiYy(R#҃r%Z( ?I<( }=ARZsI:fRbi53Ae4EIp4=҈w׺R&	4,KX |
| --- | Minor | ok"nEQ\}+ږ>qB2Y2؆~i&r7q#w@o@oZ'WI>9l~`[j9m.8F̣Kq(VwA |
| --- | Minor | ?3GxZ |
| --- | Minor | U%)VIaskpl->pCx6mtF~2j9:R^)`qcJ9<v`䤐05MDz3AP됣]m> |
| --- | Minor | 1#Gi |
| --- | Minor | @r-%Ar}DģN!k2:o	; ¨>"=)tBӖiP_ |
| --- | Minor | <"$ǈ眀)|-2&9m2n},5FZuζe257 8T>x |
| --- | Minor | k^-p'2ryw-z!̡ٹf婘;ñ gAϭ<ۈk+ |
| --- | Minor | dyLJ&58Uek0FQT8gR5C #6Y5a>2Vt*NOmVÙ$F}5 XqZVV,SG-pq#˰<KkqJ6IA! l4x*ֈ:ccG	#' aݓhJ7vF4#kPIb/9$<9M]h`}PDt-h |
| --- | Minor | ?Ϧ!ē­nV!ې?X 3TʌF;MeYEo%&!?QcI}׽%1_^^C_)I!ڜ#=n:tq(K#⫗9| |
| --- | Minor |  ˦.akQ}来@=C ^GMfk׫vm/}{CfF˝	l&[;UR |
| --- | Minor | lU20) 4;>TYu@eg`tp Wσ ި נz V1Ҕ3f%nװr>׫M'/ڏ80rُnP |
| --- | Minor | /i~eQ5Tc7_+tF)VRv |
| --- | Minor | ! |
| --- | Minor | ֵyn4y'LÃ'caVnkF |
| --- | Minor | ΅Nc8'cnvD*A-[R>#I |
| --- | Minor | n_mLC_kr,U&B<!-~ŕkdϝEIm\nTw>\Q1,DGej%M3`Nݥv,=%FnMterůvSKis3a!0 |
| --- | Minor | [`9}WV'uڵ65˳ZPk w.C8K |
| --- | Minor | )%o 𬚊7d:3^"p0Z'tH,KhF`n+N)0[^@5w肾]_|WH'>}ΥyXu2KV)USõ<:ⴋP<:_Q̻)+?5AlճPҔrEDϊSIqB[C |
| --- | Minor | (]YX}ĉP$3/3L!qDA |
| --- | Minor |  |
| --- | Minor | ~cDFh2!5%jP(̭,w\~CE[Q-h1Sv̒TZ&:ZBM>?gɏ!p"\$%(P]*C |
| --- | Minor | ?T?a]_QMGѣ-EHC(az |
| --- | Minor | <saDS|?2g'Y;ynuv(9?i&θT2kJjK5C!A"ygb~%N9OVF^	R+w !dde8>y퓺HD'Vao^CKOp8t54O;1:*#q˺3!8h@8?I<^B.uA&"UGg~y/%GL"gKzɧ5ƪ-`ljcwvq?ŏ08qMMKG$IeP; |
| --- | Minor | **/-|Ke`BRYfdD͠05NW`JC*Q	vg;"hGp:{6Pp5,\x |
| --- | Minor | ztR9 ޮVzd~pg_T |
| --- | Minor | [T,sAiXl |
| --- | Minor | ]YFx+& |
| --- | Minor | Y٬'H][_!̖v8itVJ,tD;DdmY/tuS!QJ i9B'\ tg)_ٵًIJůf4Pmov4ee]+|40hcr:Ͼ"D%Clg*@N5@dܐQh A~lL5G3"au+۶Sebksxa>՘NGת{.v#T>ktt<d&_V._@꘢Fv+C:e|0mۇW/a |
| --- | Minor | 0 obj |
| --- | Minor | <</Filter/FlateDecode/Length 5139>> |
| --- | Minor | \I$;nWaPa6#7}}|59_ojD-KF*#qQ^/닇__//Ɓ6!|U)G}N'*J)}RԖ6a^I-mizCj| |
| --- | Minor | =XNcbmmn?hUT!D{8k|Xsg1 |
| --- | Minor | ??镻ul12Ywv;wx4y1״Ϗx'Q|}'iĴ#9L:'dJkmׇF9b+33 	.֠eԉrk[VF!10営n53+/B80Dmbԥi	r{$ƪ?QfGֺ<@2E^y\0f*ȕeA!qQH)"RW[NĴ1駽u%j38S%7IIՅ')pb>!{$9-Jo`>C֮%\3J |
| --- | Minor | )\ge!,Y杛xgA;x[([m |
| --- | Minor | [ؚhl |
| --- | Minor | ?sIi8*oM?0JUξE-ZnO'cCetm:nh6?Pi#(TI$$I")&u,fBVy(5RU{|-8<OK:?wQQ]hn|ܣYә,6Qު?@Q;TMd!'88Rʚbߐ:U#fß1!VdRuv<n0/AFf}u,cݲ4u_q,YWao}4FLj=ܫU/媌}yHocMaUg,eatE@}eOm4?\iKCN̠<Ӛukиf6Gjնta20Ks[JRLl(xl6jI0`Ell25ܘuwѸmnK]K^6;VqGiC.K{3UG%t-XS9kpYI&o=`"{{Ax-jUՈY7:H<g$N4'*q@C;rQr43,`0NlT#,Mr21ƪ~/AsjWTԡ ȳ >k-F}Ђ6x+0K}(),'吃WN1pcu2Bw,6䷖GALFIW`@)9ٴ_4D঳;&<q$M$*g?LЇѺ	JLqzbųFKq |
| --- | Minor | ~<a%;	Z_3(aeAubhqi9ql迳&!	1ۭj(6Z`$7{"ZyrKh1߆Q(Y.И^$,eBEс42x RF%'&u$# Bk];@vyt3!B(⸽FYU{WhfؔUT:홶+v6`-/\dc/	PF_W!da ŊK>i̮wg%;YnBnuXcRFg~OOpTpsfK_i`K{a2 |
| --- | Minor | ,&؛p_lvPdhN"N]bZQ˰Yq|u^]ЅeN`&UBp"'jӐ"z b~/R+)i<z]3"#:iCESFt~$N;!#f |
| --- | Minor | 4ոW&u8d̵Os;$$נ`JgdR`&3DțEDK&DP=_H`\+.$:-({rG5cfntn=,d[ѧX8:Rq0EVcgddU i:.f~H򸎈QÓ.QV{xe/%Emu8mQ%	tLd%IxkIﶦRjíYy	U(QϾg.%xmf?J}|~ |
| --- | Minor | ?z̋mQ;Z?Ao:9} YY?2u\{hu%eg+	j8&ڊ5Z)HEDG+S8YAWtl-9d~m(e5}H1NLQ8H5ieYSpk:w˞FyÒ |
| --- | Minor | ΅$n s |
| --- | Minor | I<+4e,j2iq(ŧU!slnyvwZ>6q}uX[/biln-,{#ax=!	.<^3FY]e`?T#	A.R"Y<N{?),6TDs@XԲ*ԉ.8M |
| --- | Minor | `C3-u̪6y ^K^2MA^Y$ְǸθo($V |
| --- | Minor | c	ANia6_VBv<x.VV`-◷R}	bPx4 PeMhlNHXHµ+Dܸe}8T7W+0q+W |
| --- | Minor | ?b m+s;. |
| --- | Minor | *)kތZ^hrK y^>qY 53D8Hx |
| --- | Minor | ^*dA |
| --- | Minor | ;͸V(LZhF51G{)oVFŚd}5;V6J"}ek\koz2Im`>wf"`#Wi" |
| --- | Minor | !lBZfsGrpĜE	A`n`uU |
| --- | Minor | .3XJ|	)K:	4oO*j5z;+w7ӯ(3( #8r{هs |
| --- | Minor | LHM8mDHs {=Ag |
| --- | Minor | ߳k.z-JuZ:ЏdobY\*sǮ^Kh49vᥨtjYh*pr%ok<;5{Yy$Fw |
| --- | Minor | w3$.sue |
| --- | Minor | *ڂEB >E֧K]\KuDεuS:4f{B%h;8ZU]eaJԡ->MRaOW#vd^D^cK22"&S5OavF/"n'ْ*]6,HtnekwkjƧ]8Gb&>k6< B.e8L	*8U륐Ovgq߅2IOg|uœ>)+z/(ƽXJnz |
| --- | Minor | ⎖]",$4 570ZO@j\>R&0_Q9 '3.`t4b:OllӀkON	0KƧ2ʓd!a#ܓ,n@-./Ll.FEYŨ4nv[]	͌҇43*aۑqQdRhD!M&,¯gdJ"fIYr)&hB-?& !fL<⒞AAEӨGʍ\L%ض3 |
| --- | Minor | 4H"I(yISQI\1ڧen |
| --- | Minor | +l~ qn.!75k_"0+Ix1Y7Ed9^Q){Q̓z/6A{2оA.CJeSi4EjYҷX;Q$@=urcpW]yKlBP۰6Viq#6@ayMač(Ԡ/E"QrqJ:!5p	8rz;,<};K,ݨ7{%R;ŴHAvV-ic<ZIE~CŬʑr7q@Ë0Xȫ]Od!YWc >Vf$Uݵ$%kJ":,| K,2Q+jAbħ oeE-tw:sܻ/fWRad]BOT#+[1[/ykl.۵;C-{Ax&#>ևML>Fw<$7+tư |
| --- | Minor | <jZ6Gpۋ|Wl9F{^'ײh+tvzC%*/h#D@"΅ |
| --- | Minor | '=Fxh[yHel`cW[_f8)F3據YOS4l |
| --- | Minor | {R_1sn|Cw)\Y_֒\xQR ͙'TL4A[e[v<]h:.=j{z<+rICPJ(&y/͎1O|!A:ʳV*7q3?Wwi^|A\Bs5#L.t21ҷt2yoRtc w\*N*j!pHz7(hqx m3]7N%oiP/otp͏/@>:R('qʆՉx |
| --- | Minor | [jG1ۿ^-W<uwhh-^s!69ʤJr.9JU*e3uS ӍkX;)4\=]ivgomĝu_ސD( |
| --- | Minor | Bi৯v~-B)<aXS81oEhV-,Z߫x/o>&8V2iY/o2o$o!C=B"4BIRRI4 |
| --- | Minor | . |
| --- | Minor | DD |
| --- | Minor | 0 obj |
| --- | Minor | <</Filter/FlateDecode/Length 4314>> |
| --- | Minor | \K#Wx:de!=`1qSE$)iCU~:胢u\"wx@?87Ɓ Eb0OߞB{@><MZ*yTs8Zg1`orÿgx:<>8ɩ<XX맺`\ʘ7lvO<چ1t~^K<+u*O<ʪ|)VV~H:Y! y.rd2Ɯֳu&0eʓ,V.E$Ly-2|kb|!petٲni{\$F[*,)܉PdN$ea[9ʷ$ |
| --- | Minor | #7$\aO0Ӭ/uL#	|*y5ʃ؄m9=orH$pf'bi؀ |
| --- | Minor | }EADKLӗ|\6flaDG]ILb |
| --- | Minor | gRYItXMNY	bctR @t]h| =~\X j˨^ё~5Y+|u=||U?}}j_ |
| --- | Minor | !4`KK@x;=Λ R93%[$zX-x'64Qq> /8co"_FYDF$eu,qG_ w#+a |
| --- | Minor | _M( |
| --- | Minor | $܄(I@Cn!2Mdu3q`pE$lo'C>tE}82jul(Cɔ'm&Od5:9jfD'*뤱Ҩ [<Lb-V#݃H*WS.SlcBhH5&\+)yL{C%0X|L$Ub<p5}}zэva(N"1qnY% ǥ$CyV$ȱzc6S3Ы9P}ܛRw ԰UD{%(đdUn2ۺuvUoF>ٌOܗ!ONVrIA={ey/hѺ$r!y_O'#$]caG	j7ayl:耷|mX֭r .5NB5OC<?UV#/%Y]q0QW}* &O}~\<fHJ._5N!59 |
| --- | Minor |  |
| --- | Minor | ,0AVճ/TbMIPkCW`R |
| --- | Minor | FVhUrTee8Xc*<<_PG#Z&gɈw/dDwŅ55܇l9u/nmj+h	$)H6[(,FN;S&i6&,I6O+η͋(S4u*y\	Y2e1+6({dJTP-oEk`P! |
| --- | Minor | tn/!%1c< |
| --- | Minor | %?e4N9"CSTh؟&8tdho8@)ՖǸPu_d |
| --- | Minor | C.\MBIdE=itϢW8犯"pC'a. >Frk$p9 WO:.^$ɥvDDA ֋_*p{DsLvR^otp->|1YL*@>bXzr$㿜q&\aH䤚BK&K(ɳiў'B<i`ZƏrfG`VH|," |
| --- | Minor | >j1,po8v(<bVw	]3EvcHoшv]`M-u's'`k`АB2T6nMb\)r>p |
| --- | Minor | #@&RԽ |
| --- | Minor | ~:ڛ2VORHȢ=h<Ǳ"tMYJdVm//})Kʰa4T`:Y$ébJ'Lzh6eYHd[@c/h+$A |
| --- | Minor | O3ċaSCSZ4W{)4K\i,ɯfw[`vqҐBUrEBipix!.S |
| --- | Minor | *Ld> |
| --- | Minor | %̬o`+qtO]{LzI!,P`a°*"2ٓ@.䱲xK{  nSɚ>]Ssϕ$4*dM%p*mܳVl2mObE1kpYc rOX&5v01siu2+α~!is7TmEP\%V&x aX:@r$.`֗5V68| |
| --- | Minor | XS>u!U]juFaХ~=1ʹxs'뾮HE~zT=|uDXVY8߃jND#LYI+݆c ]@`+LnRYE |
| --- | Minor | E"uD/^h".Q+v5Q]8gTrNN2G=Wűg= |
| --- | Minor | Wſ |
| --- | Minor | sw?Ǽy^$ƷvSm6߅rlQIf}(P"n{iL.3">	7Fjɇ ]CcQ.X!	S;"WqC[$;"B?ۿ|x|֝;yy8B!~T8wsx@+1V`xwRbC&Frō* |
| --- | Minor | |#Z	jffU0I~1@8ąr4DiƗ61])PNzx&?3 7+,65s6a0)"3Ć|66.ա>>5h RbIIJ'$cv0#0lhm0o&q%p&uX0#.MŽ2*c`Kݶ=#MnТ+2tEF| |
| --- | Minor | `8K>E%x_S7%ӋyI!]np6ܢXy֣˷{ϴ[۫"O`Le̼VLc#R4h}jNpSHv8;7nz$MA	yJba>EiIBֺE* |
| --- | Minor | |f`ww',lZY6rW$y# OAjOөBSvxfa~ZɧjjFI<d0n#=D!?Ş\Wk |
| --- | Minor | <73vqv⓹K5MvF!uiFY'1.LݨqvuRyMOtksm[dzŚRzKBlPƦ!ݡ868oj>ow)a:R2ɯm6i!m% |
| --- | Minor | ;\_q;S1:(Kw84]ԷL	8zD76 ,zofr4Ua/6Hmf|5nTJW	d'esi:oɭhLJ@ls%唞zƁq?5d9ĝ |
| --- | Minor | =deZ׸wWaQY˫4sM@;ֹ.Ҿ-\y	||uI_ɦyT;4f/[/#6n3W7ɕ)jߣ` |
| --- | Minor | \ٮЁ6S/cL/Kړ,o6=ZBV\Η`@FnՀܔ]ެNe4'"/k% #^=Vʤ}C)UUtF99H!::lV:wwKMٌ3^o|Z,*&4)jd%i߾_HNSR8r4MNi͡vHP;ܪQaVhl/fXr ¤{C2GgBw%7'ڵR.ٮVsR5+o#lǡE |
| --- | Minor | 0 obj |
| --- | Minor | <</Length1 3716/Length 2489/Filter/FlateDecode>> |
| --- | Minor | {pTdMB<M&$H͒̓l+	( FJ`ۨF XAtC3NժUg`gn{mp۞38K |
| --- | Minor | #YVRd#R&6ry|cGʪV?t_2㓌g/5m7W׶#16"y |
| --- | Minor | >E7opu<l+/54w{F9Xٞ|rЈ |
| --- | Minor | %ƿcұ5[Y2cOs[mPMoY[[#^q1lUq?'\|lƺȦN߉b/ cmh:)(Y|JJL |
| --- | Minor | hT^O.?\XQkތƽf2S)jFR0F(xf3^E*I<L4}WyJ$dj;ְ4Q+pƢrڢ|:Hh`fFbbAsL17*/rkUnu"aG!׎6^idH#bv7@p}ti?/lFeGtJgُ>g~=!TTTiZC#ʹz3d9D[As-fKU@N*RuĹ4zyɬi5K#5<_e'GtejPJv5f-172UGKC:uT8c|η3]M5Wtiu%NXxUr2j+2eK)*4Wk<o5GzF+׈~9^[?ɚYQҒQ5%ZâXҒ;'Oj#>>ռ)D~wzdk:Q |
| --- | Minor | Igբ>MzZpx5C&M|WG?xXD̩y%Cz^~^)%I.%z˶[|ʪ/^=/Wx	[N})]FQeVN~9>nkanXQ.V^W"ӸD+ΜZ  |
| --- | Minor | ,'K6j\(mJM{?IYyVsgE]g?l^3<v\nk+**ѿn`paj/knU]5%G< |
| --- | Minor | }uz)mvT&2zD88nSN;0Ψk?ՙ~΄y$(a{+.tL}l?-D"Gߕ1B?[l8݆>n=<я6Z-ޢra1ljAw׊5dیs%bX>k:;*qTMb,)EP<(B6p6A/t}÷ |
| --- | Minor | dm92?"j{_&㾎m67L;V&f27^Leÿ7w<lq؏TQ6sxc6,Q}muͧܶ.2gVyi* |
| --- | Minor | # рMݸFx#qg\5^«řW4yƇW4𲎗txL>we_u:8yZC_~3!< |
| --- | Minor | '}xDH>DO'8.{ |
| --- | Minor | <+M><:G8|(^P@<Ɔix[ƣ7 G#^801b>bΉۺÃxX^A=ղg=bnS=Ů.+ |
| --- | Minor | QӅzGd׋{c |
| --- | Minor | 4;=㱽+^n+woKw-?E[ز#\Mf6M@u]FwE."օ֖5hf'E8hMWqPnP--꽲 |
| --- | Minor | QE"Bm꨹3[3wֱw6kKFOt*U!pde'`YQ7biSlK|(S8]G",	cQS.r(V;QE `cX؋"K.ir~͵y\; |
| --- | Minor | .80[G~&u2Og~7|b̊AnN-ANvIA9fIY1!Ջ3493x349C>-WN/4NlZ.21^GV##=QfT!SlI䒞xΉIlEi11pCR*gsc#ى$MIahn4hv#ypt8s#OE<pG |
| --- | Minor | #Al`Nvػ6 |
| --- | Minor | ,'-]l'}Ldv(U ʀڱW[-')	~ |
| --- | Minor | 0 obj |
| --- | Minor | <</Length 35/Filter/FlateDecode>> |
| --- | Minor | `D4q(`Q@`C D  |
| --- | Minor | 0 obj |
| --- | Minor | <</Length 252/Filter/FlateDecode>> |
| --- | Minor | n E{bMb_JeYvy(N*+Ba\3ƑWsf.0ïݭs6^X#~ |
| --- | Minor | ;@[Q9$d99Y  |
| --- | Minor | '%>0 Qcn絯_B	]k[hg^Ąyi۴WSKkP5Z-4VKuI_$W~ex.8P5,PbQcA}&#mkR-1Reܒu |
| --- | Minor | ?]y ` |
| --- | Minor | 0 obj |
| --- | Minor | <</Length1 15136/Length 10170/Filter/FlateDecode>> |
| --- | Minor | {	|TEoթާtgN',t!అM0"D!$,:"\ |
| --- | Minor | Aaf"8|1}p&9_@Fsg{}R]UԩaX?v\>J~83П?џc3~=eԌ	Gxn5wzf"#!\d޲30/XYnz:B(Zl{Ba!}Ep򢒅ut8avkB%KjVkN!TAn<ѹ_Cy,~}yKFC |
| --- | Minor | w˖/\P9XCJp.@^Ӡ ر@+kU1f)r۫/ENV!LG2ӘH?=%j?|O3O?c,'W/ޡkwK7`@	ِ /JB( |
| --- | Minor | >W-гA`pwIpT;wne7s׳I0s.-|S}#F$F*:7E"zmEGnE܊=J\2Ch FFLGɣi{(z~Ҿ{Zi!t<dP4yx |
| --- | Minor | &PDF0έp9ؘ.x2A?^yrLdQ!SGB?}}\iO  ǡ9ᱴ7ߝӯN&hݾ5x8*a4aE Y0VQ@g@wӅ=nq1074*G)?F\(2ZĘ&'1LXI}(X4z3oIa	GW *Uڡ>NBat+!h8Ơqh",ܯ@	f'';n*rIǽQ{K}B{_={W?zn`U	HJNB^]PBEHjD |
| --- | Minor | ? |
| --- | Minor | eL`b21R(m#ņ:AyP >QMe5@(R^O9\kP5$zu*CUhjN9U\I |
| --- | Minor | `hy0~[r{$yYR tcY^(wym=D> |
| --- | Minor | ]c4>	FWc  գFT(A,ր)c>r|~<+>2Xi`<NHYg |
| --- | Minor | |LP[O9*a1gFÁE@(\C-ɝGIB=WH~EÈ¹F4_OKnIX*7ٞnQpV}doo,6Ŵ$U+uܭǍ:h,>HH4j<գI/_eDx-8ݿ |
| --- | Minor | $sl<Lo?)__Y2Ln |
| --- | Minor | ђN ReК`gĖf |
| --- | Minor | ^yS>??#e>yY |
| --- | Minor | $#r5T,1^'u |
| --- | Minor | c&OD3{.\brlϥq3NUIɪU3#:;͹@h;%1Y,Lzh[;~>Ժ2f8{!`Lɭf ټ<1/o@tSk&Z!|-3hpVnބL{OɐSLB%*,h_h.EfUFm{zH |
| --- | Minor | ~zy% ٲo}Y6:qgU~Q~In]⥸KVyu@VK1l1RsSb/UjLhomT |
| --- | Minor | \Sn p( |
| --- | Minor | "<U3c	&"m!!%q:S2\x1T\vR{1++6cݛu |
| --- | Minor | )}*PH)v-JLV΁4v)7$uK܀ku|8F kcO6АGAʯ\WQ:yS{8~kڧ77g&7˗p|p	n{or	ĘRS֨qF5:TmDZSJ#*,^S(yyEg|,Sq	ڭwH[u3ܪ_ |
| --- | Minor | .<O,ؙ`ff<3A#BlR<KQ,]!'zf}Sl{W÷K/IKnM1]&nIhCB#Zh..%5qvm:^EiΝw |
| --- | Minor | :ĊȋIeYA4ɔKO1&ec	YWQOy`Pƽ{v}mDvGI`ѥ_p/w'׿ |
| --- | Minor | qq7ɿ;JWL4BJH"mqƅiqE(Gx z.jk |
| --- | Minor | &BYYoBb9 zA^o~fZR7۲ng7C˙<{ʕ-G<{(YqލxW=G/]:<Pd`#~9p*:@D<`b[2-䙖-P)h4l|SuhDROCYJW |
| --- | Minor | Q:m1c⢇d@rOW02+j=Ikr7D36ag9rҗd2Nv {Eđ~,vcKigs(BzUG֭_ۀg_[uTuKT]ach |
| --- | Minor | ׂiۺn|{ƺd_?Z{5o |
| --- | Minor | o<kEJ:L󑧁p،^C |
| --- | Minor | lbDFyA%`Q%hu^T)oDNEJ~DAU	pFzXՙԨut:Fo韨RtڤHv#2bhdS>Eb<5pɲ'DgcΞ?Ze[lW~뉲2<A>ޫAаX4Dv-EDl0[JIQhL!A'Rg5 |
| --- | Minor | +0TTS/v5oOaksU.ƍ?=Q oypqJ^Fv8WK }UJn4)f1>bZD+גJn>>7TFj(Ѭ11괃AMT2;n;-p<	ghDڴ:s=V3 |
| --- | Minor | ̙2#N⩞Q6$ЦE9UW注QDdH"灐#`@"2Z}ǅIsm^|Lkg0ϔ^H'DiXihunk |
| --- | Minor |  إ>{ص\+JskuXhcHjcSIaX#ur 4J÷ЌT@1"PN/K_QggΪ4%HCi}QGM&UKGj|;Փ0D5 |
| --- | Minor | ❨?=31afvn~{gvBBSЕ+RoN[uZoNKzk:c{8LLy"5XaHRkIH>S͝:{TՉ>< |
| --- | Minor | 3?Ysw_ 7Tug~._xP^7|8(CNh^g7Y*|{`HD3NLxvwtw(chUyu)u!Wnf x1Ԥ::F&p_:ooo[qa<fb-i XʌhY8ܩjxy㚒Zt!'#AwO˹i |
| --- | Minor | >o!wRf'%iiSΥssm\fk9Essaٷ=DU񄽈ͦd~iƚƓ[ʏ |
| --- | Minor | [8g3? |
| --- | Minor | ?kϿO`'!"/%y8]]"U(d(Rm5Go3>HT}r,9!mVFXVqGqnl{~ڸ}{֝eTֳxέ[ŹŇs?9KFRrlɅ9~	Sz+)6d\Ӣeb)rGXeІ)+Q6M[l_\_/r[cOݳ{6yΒQ/ۺ/zM}3W#ܻWJ"pϹKK0,=H1m"a?ʎqi(Cpq$5oFJ |
| --- | Minor | {.`Z彔eέ۶ol,;T<ܺ-fRnw>/F	<h4UcTRtQM)V]QJmsh2PaebŲ+6ĒK\](r=ff<eՁgj5l1oذC| |
| --- | Minor | |oyJ|UT%%vdք fU.dU78鵂 |
| --- | Minor | H:6jT*rׇo]AkÊd0VIUb*"̌4$+YIWeE@R5Ow*_yWƬ9'Oھ22|ݱQNi\*p=")EqTMeQ=#X.'!1PvKȱe;1  |
| --- | Minor | ̬@h8a@ 6)/;K	q8dYJ*2?pUt_59%E5ءryk^c@bR򻬂;iH6i4~O?x38 8d3dB$vw |
| --- | Minor | ]_@G[DbEBgơV\\E롃2<7v}bnfV,}ÞfdW)BtcC%QC 9"ޯL{8iWLa.B!e)L߆v1ƌ^; s迥((9_@j$If>bQhD "(Dhq'_v1	N(ˢgtDXqR'yZN |
| --- | Minor | ~ |
| --- | Minor | twl~ۗO|}D&N:@)A%/2287X|<>P!} K&SȌu..?,:4DPI?YC2RTYHԌg"VImV`Q7[dFeEˤbIx7;R^2XiH,I7QWE\jpw	w;+i |
| --- | Minor | ?gmVĔڳg׮={wRv |
| --- | Minor | ;v`e%{4 |
| --- | Minor | ':EK~LDrCƄ[˺U~Ը?1ޏ.?VD>} v0ĒR7$&p/1/>	BN]|BUP	C~V~Nx"G+y |
| --- | Minor | Q	)ApC&ٷ!~Fd oVt~C{{Hw37 |
| --- | Minor | |[ӔH"#nFD2]HDb%nMK)F<wT#|_eEál|ީ[`^Ynd1]F)؈H*6B{'{pM>N*aaTlLTnV~*֗Ll/y|	>999	׻{'ٝ{(P!oސ~zv~q$lYfOOy;{R{el5ݷnS݇ox}AqEͪ9vYջۆ\pv́/qȟiܗX%?(UƕH |
| --- | Minor | MVVB<Z%&Ws>2_6QVv1uG)	R?mlM,$2 |
| --- | Minor | &gSShd%gzkx|hPն?&$DyO{}}O)9`'>,VH	[u(PT_]"(e* |
| --- | Minor | ;ʝAjg޷WjJS] |
| --- | Minor | ]tXɞ~	zm2Y/Of(?!<Wqאָ{Lʋ'.<~| ğUXqbh+T#1b	4fU*2ju1uS,LT&=OE*,uZZ%匜&2>丷q}g+E{}{`M]$b&Œkr-c$D,ŸTSj/ly$`ɩ5o(B,mJTjƪ-k2JdW&,֡hɌ$#ّH~0T5Lbjɵqxj1Q7A?A```ɷއ |
| --- | Minor | S@ |
| --- | Minor | / |
| --- | Minor | iY晖|bRqE|P*RkY[+j\ԓzkJUTiWVWVWL5UMsՠjl	o!y`r=Y)o) |
| --- | Minor | .lT\`އ,p^ޓAF b">H}Z&16[mVC`j 7=G<jFT#0mN=nMĪ\v(bUȤvڔQ 3j#Flo-; |
| --- | Minor | 'sʯ_TenI3=H46$4x4 z@me[	%[ֶm1X5XͨZ9']ŸSԹ6t٢SP*3~Mҥ}dclJu|ѹH&$D<ސo=ff<<P~LLL2\ƔBDW_lXh\k5d |
| --- | Minor | jJ |
| --- | Minor | ׊hUUIɰ޶޹޵>A!okÕ:fF*glכF$لUrNY!_]u{oA xDl4D0.l4Fl0T`#Vas<# hLQ2Fb6z5ZvXf"QnQGb&i*vv>T !UXj,8ٸƬ`\*I>,<+LLm	.f+*y<p5|znְ¸B\iZZ2&Xڦ/Wkq:NoMdg0T 3ͣWgIAaé]ar3#YXĚ֞nR 8lB17[^?"wi3Lz,6|6wu,F5}~l7)3^& |
| --- | Minor | ;m-¦o"? [xbI=JEYfdc-^oX33k9FMM!LR՟,LJtR͖J{=f~ |
| --- | Minor | ⟒O023}c`ͰY9V;"u'<.UDלhrBh,RAaԝi;Df |
| --- | Minor | #wNN~t3`)Gt9識lNSmd8ꥁBC*6W!ӄ\V/nOGjo|ю7g 2IY3GZLLLlIdD^ҷF#qoܽf>DBu1?	FϿ+7_<pb6oW9~[S_Y! |
| --- | Minor | Ɛ^BU653N~Fn@#1 |8wi	?wП_3ty'v^n1#=Z/?+UޚI}ogbR!E* |
| --- | Minor | *%e3|A% }mV{<()?݈/L>yߎ`xPD{黡A GH	j%6c4 |
| --- | Minor | l2	BpI{|`> |
| --- | Minor | <0ЀhAw"iRB*bv4ӭ`0߲A|p7Wt. G.=^dfxq1/(^ |
| --- | Minor | QP#gw0OX""dGďztKңxt v8x-hmr(#lm~{GeTERQW^Ϡ"-G:^ĞFhms>I)ÄpoЎF$ |
| --- | Minor | aCNv]-Lp)_FZsG`ET#(n2,:ڱ |
| --- | Minor | 9&2;=og_~JRmRy꟪?լ|uhWiv:4.m_ /VS⫦<fEay |
| --- | Minor | (U>~<>}MS@s,}Gn-mLM20&γiȎn1-Ch9*EQ	Q&^R YК#h4APhZpv"Z |
| --- | Minor | @kÍݞZ-z!ܳaV0`<e2 |
| --- | Minor | fY |
| --- | Minor | )syʵ3]yJ)s4Dps\AxzDsއQdEGt*")EF}{,|"xt/*@O39A#'	f1y*:c5+rGG1zl GH=Z鳟my-{%mM=p](&}\!9[ONk)-y5+zf%'UdLhx-:%h /q/Xai[1y>s@1yv{6p-Iy2yF$O 7qeԓ"T,yR$}Id/k {%vܸJewn}"q%;,$ca!;NbIRpdI9k:E=嶙6mVPu)nLl.䶜"[ֲ7%qftmJ"7qdsR/Dcvn򈖬-.ʤBzpȚ:#B$Ԛj |
| --- | Minor | ͭEVVɊR7đj,I2=W%ezLb+%#dRQ*DR-בr-G"%R,.JNEIBXb%0h-R\L|̓I\L ɤP&?L'sd2{,%d2_&Ӌ4+/H |
| --- | Minor | ^#:JMђIdbLD[Hc48';-'cF=Jˍ(I͍IM$dBYI0 |
| --- | Minor | %y;LC暹$w5!&'e=edPd%YA |
| --- | Minor | !j.!|I 3%l\f<pldZ6C]e&t+LaV.i@zZ1IM	pH |
| --- | Minor |  >|2IJQ\R!Iy+	*qGqB7q(>M$~-!q%1FH\ N03@d :dbjljpV+JB0|&P7&f&GdVRN40FSOD%8&sA'	&e4O'H&$.^׈DL	G͋J |
| --- | Minor | 0 obj |
| --- | Minor | <</Length 143/Filter/FlateDecode>> |
| --- | Minor | 0Л " TP* }LaApa\9'I'4^UN'׵v+7CXyÌ2s^IyO3<,gnMI                G |
| --- | Minor | 0 obj |
| --- | Minor | <</Length 405/Filter/FlateDecode>> |
| --- | Minor | n0E |
| --- | Minor | / |
| --- | Minor | 	!UtâvX$E*Nd;R#=3smqۿm7@h;k]$:w6ra:=~7ב.{f#/.^Ls"H?!ٳxaQ,Vj[=Լ·=*|{Cסj{dVlZl_>_i<#O^Rsv$qTQf,dc |
| --- | Minor | l |
| --- | Minor | \b2~HdȂc	,Kk`>FDd	&Mb(sX)9 |
| --- | Minor | a'Ydp |
| --- | Minor | KWeLV(W<ς0\py7Ol0ݝG |
| --- | Minor | 0 obj |
| --- | Minor | <</Length1 3560/Length 2307/Filter/FlateDecode>> |
| --- | Minor | @Ix%&$M0X	yYBI,>#H ۸̴ |
| --- | Minor | ֡3Epu` |
| --- | Minor | 3vZ{η,"rq'[^Zv'#%+Uv/ȸre	tqq]+?ey%k |
| --- | Minor | b㪺./mn5/<3DV&M[77,.kqAdb<.ol~ƙMm]bimV)$dz׶Oc14;Fv*D5<mlxp?hSr<R)ud3jH42rSט/$yoVQB[kڮ& |
| --- | Minor | [TAEqd!TeqNgJ?J()	辨11]|MөJs/&(IaztYjP]bHU5+I,H5b尵MMFlF,bQ<&c^b:7kF?:,һL1i=A_Ē |
| --- | Minor | *XO5Hc?*~<wZs*NtIEsE? |
| --- | Minor | !p:V<z^&2:}<F/*g(L{,ab̴V13ZcF6dÑyre5hPx2Sa2\_t |
| --- | Minor | ㏮Nki"K8Fq |
| --- | Minor | #|L0*"ObbKbinE@9lI |
| --- | Minor | {e{n,G!bB^GD |
| --- | Minor | {ﬞ |
| --- | Minor | oTTruDFE/CYײRUV1k 4̝3e|S(ʹRc}6s%e'NɡylkbVl6Ť$e;Yg8(ɋ:.2]IyEw͙82233R,$-es&y[j%+WɘbIS&;IcFA`xw?l۫}/_O"'}e(V~˿:n-5ޙ01z}jm$&Km	n_>qvBdmӈi_*87F	1zlTch2jN3*"VlWA0BɌ[#cxGZ@͜:j&e*4`n-kx.N:jYֳ~.s{WygniR*u[^MM//{Y}uֲuev[k}Oe׺ک冤e/?GPnYo6|IsUڣ[[n:)OqJ'3xy"Kĉ,WwaXGǫ_#嫈:3/%@<@~Oq:^\o|·MvÏ<;QG;4vPJ!M<ÆxLM@&~ӏ˧u<u-xyЍň@<*-?,!}$Vub&0g.=$Ա{W==bNU]yaN#;G9 ch/EO0({t<`[8An#&ʇؚ-&;{cbc*ب+::tl |
| --- | Minor | Bi=mGkKluGġE*5 |
| --- | Minor | ezDcO6VQ |
| --- | Minor | KZ:jȕ5::uYqեqUCX2GŲDYƲD]`i,hM.B?nBje)(]-XP()%k18Z4^9r]Wv,H1wKέƜBBcYYcV-gye |
| --- | Minor | ݟ1KMyv9ȞK01ÃΩOb|9S9!K,}pJdYbdo\ |
| --- | Minor | $&;,&qINLvk"-	)rB%RkJ>uus I-Gn7\QD?	<#'#^q:bj-= lVy`u"d;`g"TCP=ʌlw$ |
| --- | Minor | 0 obj |
| --- | Minor | <</Length 10/Filter/FlateDecode>> |
| --- | Minor | `    |
| --- | Minor | 0 obj |
| --- | Minor | <</Length 229/Filter/FlateDecode>> |
| --- | Minor | Pj0+tlmA0úlcFqNױ	d!ē乽g/Mp3֛|kFdqL6(+S66  "0ܭ_ݜ2R`'zDUk->/;2ޖpad)iÀs(h?_Z>NhXeLDl*|RLEUt |
| --- | Minor | 0 obj |
| --- | Minor | <</Length1 2956/Length 1931/Filter/FlateDecode>> |
| --- | Minor | {PT.첗5颉\JZYXk6Qؖ$Ni'TN'cGq:әNvᴗ~{6|s}޹s)D(՗)<icKO L.=/ٞ۲_?Qy/DIw&n]O7T@_Xe;{ mls?|Ӟ`|{hDٞ` vpA~{{¢Xm}[Up;b-\gwwq}n:?pҁiJqrzPξ3xɤRbp^RMɎ-ay#a*|MU&8l |
| --- | Minor | <fNbm |
| --- | Minor | `Aڤu W4SS.$(IDVzwVSVAԽSS%X^IU=Vǌ'nUZ򀩻1s豩4&g<&|yw>-xdu]>ښiڦ7ښRQß7o˛A4č|ȉȷ^F0k;p |
| --- | Minor | ^ |
| --- | Minor | ?~`u7=WL:\zc]߉&TyYh*7z.Axi%_ad]_.9/ٸs.yއs;9CĳFŰÆgV3&^8/pStL1q]rTL!c8i	q7"Oy܃8ڱx~h\>obhPT=GqG#>>䑇sp865aLCr VCxn: |
| --- | Minor | e3nLG\rM؛1;vصsܥcLsRL0=M7m=K.,EwWv;*ReN.yD{[lG{T|mʠђfM[dexD-6T_0q7Qz |
| --- | Minor | .ME. |
| --- | Minor | `U+M+p^|6]ffWtaY[.!ݨ2RdF |
| --- | Minor | {Oc(K?%5d5/b˅X0#c;ys59Jo^HLYQY	Qce(Ҕ,FI&KV7QAVȢ*rc(g̔FzqZ^:h2frV#\3O\.AnTؑc<L#x8B>\,fͪ@\t4땚^/>^	7/jqipqeL8 |
| --- | Minor | ;c<IE 9O!LIU;z	%) |
| --- | Minor | >>!b6˻NNh_qa2}bJԸ(&Tr.ClPIK.`RM*X2F(EB`21i	]Ѹ.'iq6K5kr.)(BǨ:ZŽtRe=>Ny˦qN5f+Ez4!4Ue+;Hk=^?_TE@:?JKwrY:JZeKUlIѽT.ز"kw*JₓuoV~|z^SI(T9~Y6c_Sħ="73?+TVBWZiI02۴n|%Q/ivPQ;ZW?UTSxV |
| --- | Minor | w%mc|kU͢WWe9djXd |
| --- | Minor | ̲a43ot+ OUΑ |
| --- | Minor | ^{^TFKcת.+i'?=}oos;teO߯Q |
| --- | Minor | 0 obj |
| --- | Minor | <</Length 40/Filter/FlateDecode>> |
| --- | Minor | 	   	               p@+  |
| --- | Minor | 0 obj |
| --- | Minor | <</Length 228/Filter/FlateDecode>> |
| --- | Minor | n wp"I(Ru]2=5Tu `" yIR-e֏E7z֑a\aɑ0Nǣ*U2öD{^-ȷ\"opz4~ĳ  ? |
| --- | Minor | 8#EDׁA=fYKoR풰?R׻% |
| --- | Minor | .AidEJAkSthySI=eWG9Y+K)Gx[!S hsV |
| --- | Minor | 0 obj |
| --- | Minor | <</Type/XObject/Subtype/Form/BBox[-6.6 -6.6 6.6 6.6]/Length 134/Filter/FlateDecode>> |
| --- | Minor | =0wN3;z.VjR [ |
| --- | Minor | `?()O8Y3I,,=_*W&jnݨP2dŮP5fj߅̈wr2A,-tK' |
| --- | Minor | 0 obj |
| --- | Minor | <</Type/XObject/Subtype/Form/BBox[-6.6 -6.6 6.6 6.6]/Length 35/Filter/FlateDecode>> |
| --- | Minor | bC=3\.]&r\\N\  |
| --- | Minor | 0 obj |
| --- | Minor | <</Type/XObject/Subtype/Form/BBox[-6.6 -6.6 6.6 6.6]/Length 38/Filter/FlateDecode>> |
| --- | Minor |  \pf	a"\\N\ / |
| --- | Minor | 0 obj |
| --- | Minor | <</Type/XObject/Subtype/Form/BBox[-7.2627417 -7.2627417 7.2627417 7.2627417]/Length |
| --- | Minor | /Filter/FlateDecode>> |
| --- | Minor | rpn.T w |
| --- | Minor | 0 obj |
| --- | Minor | <</Type/XObject/Subtype/Form/BBox[-6.52169043 -6.29442719 6.52169043 6.6]/Length |
| --- | Minor | /Filter/FlateDecode>> |
| --- | Minor | @{^ ȵ+\C`3 |
| --- | Minor | L6tiLݰ6LW@!"uN$woXgY& |
| --- | Minor | 0 obj |
| --- | Minor | <</Type/XObject/Subtype/Form/FormType 1/BBox[0 0 246.23206187 205.7448312]/Matrix[1 |
| --- | Minor | 0 1 0 0]/Resources<</Font 114 0 R/XObject 143 0 R/ExtGState 149 0 R/Pattern 150 0 R/Shading |
| --- | Minor | 0 R/ProcSet[/PDF/Text/ImageB/ImageC/ImageI]>>/Filter/FlateDecode/Length 3269>> |
| --- | Minor | [˒%bv+:lRpa^ f̘_*UT["yT(Ofѧ>OOQs:~:ר~.[پVsH|j8A#||Y~$i7&h?>og]ynFζވ C5(B4Bˬ2kdi7T9*8&x*D'ɴol_w)Y&N7R(K(塊?@JXվ/Ѯh;%t7QBZ|b x |
| --- | Minor | :4f%f0bn2*	RJ UX= |
| --- | Minor | i>"An`&@iDY#'#2=I%]>@DB(?S]W;&TUj҇[%&h*4?O/L\Z_7L͞IsR=\ I d@Κ%aEQ2xyPɆ:-S%7[w$tj(D[G4UYsj}{,Ŗq{;I\_`~dt[cѐD`D+HIc{vy]fzKayLh@{ a ܍auQ FK"M7tKp |
| --- | Minor | F\:$C(|M; |
| --- | Minor | M DލRu ߈uB( |
| --- | Minor | RmŮEVWx7* |
| --- | Minor | (઴(F4:.I&hwIVCX<vo={hA\Ꚍ}m2],%-ti+i CZsk)寳<(gVF}1b![/z5Z6_t%-SF}u/V`/k+&_ڨkj׺R%m}M~]~^Y+@k(\_:/WdC |
| --- | Minor | NX |
| --- | Minor | `TtE;[Y(38RJ<$xB²סYZ3A{UQ]&Gv|gkOE$Ge"  :ZˀV 5NĨ]P:ZsEgcN  e@+]krQhA@cshk |
| --- | Minor | sڛ4</MzI_hJjMVIU{-˭ۯUIl |
| --- | Minor | *>lKny6;9=  lr!`ӻ2uW3Yߍ6O"Dƻs]Jwf|/q6 |
| --- | Minor | `(М68AkA:8~lr"!DQKqdf}03vXwh{esDnG	Xt9|4}Nٲ |
| --- | Minor |  ݂d$/=5Wmw^SiʲE}[{	R)l |
| --- | Minor | #qu	0ꌤknR@Y҃VF$[Or>p/4H]tr1 Qk-EЭܴʷOcocP]Yd5ڕhWV; |
| --- | Minor | ;H/l<j+ўFO~Sԑ.ɚ190P@"+\}ot[ HH |
| --- | Minor | ~Pu^ R fZ]T9z?I{<)j=w+Ldu#*V`-=Z{uckOV=ehu@ 9qxZvPk8rߠ`#n/j'l7g4sJ\k&ri`Ң|(|S\/=r,>Z}*ǿ:%ۭ&bwBa<NE[ɘ9D |
| --- | Minor | #v1_?FBt,C1e	y)rB(CQЃZ5d92DYBDʑnƈށ/<D$Two|%VHs,uaA!SKbj6Q6ηFƑKG5gүl}ϻ2^Μ'"_jO'ġoC0~qΑY |
| --- | Minor | oNV#ƳM(Ty Isc.>D@ZJe'A&"v8{:J0Su\΃9ࢆ$^xOlUKA5fbye`0>1=>Vapxj|^@)Ѕ |
| --- | Minor | ':C1fi^?)>D}d+=2;*u2t:T9 _x!*?fCI#{G'tOGBkG?kO	@ͣW [ͺR@jBdZ74|,sj丠s |
| --- | Minor | .GaZ[h}e0Eˢmֳg2"E`'=X>O ˬ.hSoN6_i% Jkڞ9|We7U2jBp9m0}Ok?>8Mzɢ3R,w]¿*hE%#,hW4n&R.fԅV>$jd]szu*^"IXL4ϓdp/gY~57m~\¼Sbڡ'|zZғF|L@v'L5(Bo2rl%vI(Fc[QsخnZ{^U\bJzY~J)t^ΉP]uQqs_ qD?v+	K%JD>p;u+x=Է#7rtY~íʒHi>iU PTL\ |
| --- | Minor | Xv;bk	oō^1B܍@NZB<jԝhgp!xUL'x_h9ݗ|lȦfZU/ |
| --- | Minor | ޮ7F0")3}c4׾FF,K6ࢯz:8XS_cDzv>ɼZ-yXvo!߅/bP/ʈeuB|U`0jLq^Զgy~/V7?sÜl,=XEE\TIr{`"YH6W4Ϗ8O(DsW |
| --- | Minor | 0 obj |
| --- | Minor | <</Filter/FlateDecode/Length 2904>> |
| --- | Minor | Wqd$F%J@*fs|HLHՃ\~Z̢,`Joy>X~zk/<.cr1PihoNZH}$Qkm.M0-= |
| --- | Minor | <6/Li}_U |
| --- | Minor | zz<Xoڥ1XZQyFYU)*گO.|hbJ:i2ICf/U>Z^ߟNkC?Xx)}VB7 |
| --- | Minor | h)ϓV!Ӥ;Jtw7~ |
| --- | Minor | <s?^EO.#1	|#-˦QYEҍ!ih |
| --- | Minor | * |
| --- | Minor | U2)JqB8 |
| --- | Minor | 1 |
| --- | Minor | _e.aYȌ߲7Lb4*pN[ |
| --- | Minor | }c33w+' |
| --- | Minor | 𯗑mbl:ݶ;&&^FJH[k5,	AyXI+Bbs<v֝quX,kRvZ-o |
| --- | Minor | ^[ti6="WL}HH^dmU(W"	Ez0Ӗ+xo3"<ي,Bգ Ӟi'Jy5Ơ^g*#pZ2%QWwxYrx܌?M |
| --- | Minor | )}{kȱ'dļgتߺ42))OEsti}PVGd[, |
| --- | Minor | "=lCHa3 |
| --- | Minor | sK8:K6IԲf9z8-C/:= |
| --- | Minor | ?MP7)0q]覟F(L VJT |
| --- | Minor | =Qya*FRڻW޹ 7<*zJlg}~_,;5yP 7?ę(df((2YԶ*xg%τeM6Pg8dvDN/&JOvMsDhH:ͼن70rsL4pQؒxs'>=$ |
| --- | Minor | [>"ABo<GR%j]jQ^Fs̿n0m	0y|x=IikEpnCCNKإ!h|8EWbC,*Ez,D5?TCB}z'T_N&B'5]aM)I4Qlȇ`H5nVoaBŔBi'J=C_ucꦱ\xJF#)( Lt'T@4qkIWe] |
| --- | Minor | MT<GkyK~VG6]-K<wK[}.(J&1	Pj0\oC EIS&Y|yrכV8xU'vMj:R*4%XѳywH5GyIV(WHahj:hK_辋m$_ٳu" |
| --- | Minor | csN)ɴrϵLrA-+?rC:h29g@ϗZJp̈́(x t@[oJxn-c,ׁF&1C=K*b,mFDCRbU1h,sXA L~.!A |
| --- | Minor | ͢9Xx}(ԁj[VKF-ڋ=Ǹўh |
| --- | Minor |  Y`(HoSޓBPyU48`'8JFofم'.nvA؄ 혧kO?=mGm4Wݒ:"I-cKnAKM^k'bNZj"$:Ow;^'Kݎ<&Rc")}򪋝}\Z|l |
| --- | Minor | ܆؉04fxxbἇ6of1V-kfI=F)YMuB=iBY6>JL5ѕ:lN%bJ|S*ػ'miLkd#־+9dR>I vu-V"BT |3Zu<_fDfA|$+!ۓʣls_ߊMO!@ |
| --- | Minor |  |
| --- | Minor | (Rr1p|XWN$Y^|ve{.+3AXO?/C	d~UfXw? CH2cD8b¿X }JhOCB^)OܢFgŭO;rX>̳@wjj|%B<* Txw<|xIs)Ee9u)=G:-<wf]ǍyRrຼss@U i |
| --- | Minor | Oho*qX#!U\T8m:G |
| --- | Minor | ,Tguicκibrmkmlp;yCﴛew˥&g<$69Ri"xaIH1kiC1!\*\1RlU, 74j\J^ |
| --- | Minor | #SC`hʓmݦo]4[.92}>_+ű-kuJ/}.W:#Q>8g(:cziMv# @-ݍhdPw}5)>*5fzK}NVOޟje{S^8ZH=wuw7wZFa\iHbSJݭ=b-5y4J^I$ |
| --- | Minor | ^"vjSH}x^\q_yֻf2ū_A |
| --- | Minor | 0 obj |
| --- | Minor | <</Filter/FlateDecode/Length 5812>> |
| --- | Minor | [$Gv~DF[= |
| --- | Minor |  |
| --- | Minor | ,1="3jfzljh++"2.[Iɓa;<?{7_}%Oƒէ7'"ګӛBmÿoޤ$DswK6Oº]tBoF<!0#g%+xG|}j&Ʀ<_}ƷTքV+yN4zL2>&8oG3\HiDo'bz,@/@:Jyr^ޣSU7oEuo!iи&2ׂܫ㽲JٺUv'2r3Riw:;IЂoW39f%?ץ<:1 |
| --- | Minor | ~u&~ce7S?z2M4+>wi1wWVSy! |
| --- | Minor | ^,n6m4&&Ei514=2/cҎ#v`]Z2~OɷHf'iV9EJ}x`c/FF~؋ߏb=PB(V.bXOFsңXKvr4$gY:R|Z$¡pz |
| --- | Minor | }$rjX-CLz݆t><H[;/o_| e9G |
| --- | Minor | 7Zy=PCLȯ+~(a}z)-;KR YG=ǳQBBA)\MkXd:DSO |
| --- | Minor | JGYsAEG*"0!V#O[M`7ikclJJ0<){WxW<3QÖuyE"FڧK_F'y,w݋0Y╰YZSz |
| --- | Minor | =ݦ@ge*ǧ}ӈԫ=i.L!V[ yxq?}c҆a4C.'6heZd+5u"/l"	6 |
| --- | Minor | @˯!fk|{tQ617r]@JPbgSH K#&Y;*UGZȨO |
| --- | Minor |  Am,2 6)<+}tH4iʓ"gjF?>	'.~t)I3*ZDYeoҡ|xo+JĶ-9!r_Rx!wC]&m @H%?-$Yk"'*uFܰ\P uB*vЫ:`-@߆0+|0nt-]l |
| --- | Minor | _OU>[3iaicպL$frb$D:8{tՉ{;iҝeKC7)r}NqAU` |
| --- | Minor | Q$JvmjIӊ<VmT |
| --- | Minor | *{~RzG,L+R0-6s9ϤqR^{gVT0vZUio䫞bB,LIVb"l1=fSi_ |
| --- | Minor | ֐,F± [l=JsR% |
| --- | Minor | IOfQQD?x6SM6gR~W}΀Awv8 N枿_UNnΓvCK%f&+B |
| --- | Minor |  jPSnd\rSrg\)4xE6Cu |
| --- | Minor | O?@X), ٞޝXhOo7(=bS.#pOvf|Udm5	[2]K<6QR'#EF=fLׇ 1!VڐA]f򂽴nקqfOx<nlA0A<ih([~DpF~83^؝sUUBNεakʌYrcS-qK[W>_f1t̞G#:TubfB 142@CyIZ|"j*ʷ$E{vOC`8em&i76I5kcHbm''.Ȗc1qfW-28>֫i/9a @`d  ewW"\^KQNs$u!XUW&p*9S_0yQ]sL  |
| --- | Minor | $݄g<BM |
| --- | Minor | $ez5bxkUfs@?r*ukkP&Ŧ08C[[-.BVn $?MCf)n8 (j@nz)JVQQY1)4uRJP:Kן[*͛k@J/#kir:YOP$ǭnQIi:ފoųwRrղnrc'kXUHDg0o.30M.:%!+Q B7rȧXr>uM2p$&tv1!43RnOii'9RMxvgkҺRnkXXwtDBցEru k6g,]ϪIXzR$Z[7,-^|dvۇ*c0lyEqp&x?h_/&t[`i7WikyչTrDoIn-bz$d߅&Vb3N!$WLD|~lSeXAS^ywԾy6O-E2mEw䅿2u |
| --- | Minor | V.R^%3>qmar:Xg]L4^JOt:st(#m"wwjzLНyUUӏRLIH/G-&Tٷ0§h-i|rr{Pe~ |
| --- | Minor | $3bBZQuF#Jx;yI*ǻnsci6 |
| --- | Minor | Z |
| --- | Minor | (wǾɠg]cRᆐW9(vc>Qr |
| --- | Minor | =Mg[F4 |
| --- | Minor | *}~OR2aWoFyfI):;o0hd>]OJqeW+ntSdpH1$#jQ5kUQӐWWEk6ޗ$OT ò+~_3̈Nzt 8;5YKݷLAc̕kNrsej`+j M~aUE.5uɼHl7p50jv˵DbE"'®#Lpx&T'ule䜛8yrhoTGs35iYL2h)OB2>]rK%qN3/eiT&gPGkq(?[f |
| --- | Minor | ̝z(*`2اYFz^V`.`XGJ^s 4WZM:A9Ik,yB(#)5Oa[vܧU[vA㕚*1.y/*hnbO`8cAςg*8qʱ[řS^ӘF |
| --- | Minor |  bNMi*)u'	'=c"HU"8'4ڄ5\lגO)C:=XthT(wH~ G<l\J&/%k	 2uAzIc75'Y⤟˥&]o9Z>H5>4߽:K/&q@>CZ|7jb#8Yoȡh'X8=sf}Q#禃֞>oY/_rxK -w`oJ1&U7F |
| --- | Minor | &$͎U`>(emFvs#,s-4klpVm9E6^s$(|=Ӄ3 YeN9Z;< |
| --- | Minor | R_ٛ	)$cL_y0%|XrE+a鉓3'e%-m1Sϵ5P\O:@󚁫u̚33TǓR=R}4ڨ{x1T+ |
| --- | Minor | 9]fQ،54g`'1<18 -t1WϳgFprBcNF"Wv	%Ksvό׹F3LTN͋[l܄/S, |
| --- | Minor | \}ܵ,7]<9!;K|yIB*5Lr"ZN8RM6+P	qb |
| --- | Minor | "l\"9΢v"<i|14yR)Ov<|]XkEι, Tb]3\iB	y.TLa6N_tPx!M3BFc1M ټ1-!Ն\f-A/uܱy 3=F_OrAKqn֬U=ZlxUc:pm^CtR?"ԃe}H֍/50IҒ*ϷpQR\p~6:-[5XФb,(B$~-G JjUu>"83hb؝?ԂD`bXCZ1%Y;K6JXDεv	aS䗀e|[@.5%JBa%NCZdJu `xNǟCm>c 嘕oZj?JEsQ,yhm4vSN{3.|7bc'шJ>2Ν}c;Gy^B"NOXwǵETŏM1YSOң==_v*pqwnX`Wdd10pcf׀Ba}ǘY Y2b|f0^NeWoDS\S2;ҵ<W`NMEI{cٍ~ZSLSKsJl/}j.]2PMUt_8+g\U*ڣ7wL<:R|2;,4b6E}|#҉we=fا&A1<	6zdVu%iا>`MeqNڔ?v7f?M;c:T(9Uh"  |
| --- | Minor | *HkDpsrѳ>-{fʒS&ĖMvyUuiͳͣR.KOVLrwUi=)ǵe|I躄^^vЙ7r,Cv _tns`{XQ]l܁SARϴYħƢJG-4JFaHz-7cZN2r;6NvXWOw6m]k҅ 6Jy>|}[-nkZ0dA~S |
| --- | Minor | 0 obj |
| --- | Minor | <</Filter/FlateDecode/Length 4670>> |
| --- | Minor | \YdU~W$*D=5%`y$LËHU]͌_oכ7{0Э7gqO򓁓ns7;~o4hyzzm:}1)8yc?~c1/)NmwlgaOj)߆Vm6JߩO[o7Nqqy7qg\-h$eX~w|uls1k=r@U~4KYTU |
| --- | Minor | (tmrDuZSϏ ,ܽ |
| --- | Minor | ` oN"{ |
| --- | Minor | ( |
| --- | Minor | D3x*5x;-bGi0O(#Ұ!6GF |
| --- | Minor | $`<BKN	>/`'g|CDrEڊE_t|Rѯ&$Lfn)Vo0W9pPڈ^0 |(Iy3)&!%smOLhb@z2ylj>URŹ߽e`CY!f#%H,4zӚ[*7RT |
| --- | Minor | |Ҡ=M{JPO[wSPT |
| --- | Minor | !%e3(ov#/RF$K*`䑶'mQz⇎2tY= |
| --- | Minor | +=o\)8)2ӛa)Kۇ`"KV֫K\J8pq{:qܟ,h,Zu-4}MS:H߰JpaӀ!Y(;P=nZBݦA/pV_jEEN}ֹv38&*ڢ"8	%\KPqL@m|WNb~! |
| --- | Minor | &6'0qx~?dR,Ęcd/]`SYїY*V\ql |
| --- | Minor | \db>iSnF  iv! |
| --- | Minor | S*Q簑G)(q=0ֽU$Ff<SR?pl(mZNʅ[+Vfa5qc5MBOKzHbb|xlk=Rq=@$ #+^(idLw6m!	[p%w9y{e4:ú,WL |
| --- | Minor | $V0qtvh*A[hs#e$כJ+O![R)1/a PsƳn9MY5+f{Y]bMu|O8[)C{a)h$&I?-&ٯ{C' |
| --- | Minor | Zw7ۻe A&&jˑo p 06.h#3\`l ή1FOî^/+&^A,6*^i4~~goH 6n(q@$'}< Q f{+0*nQĕ~)+&@^sIDͥz֠Bac\Vq@ZNqW; |
| --- | Minor | &%6.Ns]ްCRj٬(FHTA&X-RݕlT m89B ɔL]-%r?kOV0CEyvv^腎:rICqnj	3	{!mף [CqST%&f3l璄ĐiÉ[|lhUm@MU'0V.e?9ȸaeYZӶ,(38AagajU/ 'X6z}xWNSʁaXgڸ+S0XXSM̩LŤޘϟMX͆%PcKȭЈF{ |
| --- | Minor | BT/0" |
| --- | Minor | 6%nڤiTHEwp&sBn/mT{ĭ7R% |
| --- | Minor | c\XpL7m/	$ӵ-ʜ-:يf[l{RQ%oF;fDPJ |
| --- | Minor | ZY}ϡ~^J |
| --- | Minor | !gm |
| --- | Minor | l*P@,xYi" 0\|i\'ADqX7T\P^jx|h |
| --- | Minor | '?I!e |
| --- | Minor | {󅘤B{ʩݬВ_lVC,'()u;3<U^d&#3:5C?1!<֓"藸FqI>Ӵs\hb'\fՋe6!Qԏkk̥'ibl՞kzfd!ts?LHѾ	̏:"ڴyB=7Z8P->5	9(ԘH܂~7;Q$Ǫ!)g	=u6x4hj'4ߗalL#+rBdռM8w9EL~\7V'!z4Mqḡ+nD::TvUy	2g_.*sLljWPk6kxoMFk"#0"뢿\YD4|%IE(D!<h!K	hh@U]9Z@%"db,!jܲ"3;]<aѾ:>rJ}B^ǀFRpهoM׈PGHNg2tCnrnpTJ#|'Eu{&["%]%6wSfq^MQ\9EwZ'>JMĸN>j,~爛dTP5gSnƂWhԫl\oهbfH}ÄO#$Y&ԙOzmeUjeb:< |
| --- | Minor | GΪ"DO% X	d#1! xHgϚ:t.V-HBTƵؓLvl!KEctdl>EAxFw= ilRnvQ\Fú	rgUM@Ou񠴬Nad4Dx'Z |
| --- | Minor | ff\ |
| --- | Minor | $Ͽvǖ=!Cɣqu,pgC@E NZ7wc~)' |
| --- | Minor | Ay |
| --- | Minor | 9mSƍb$(i |
| --- | Minor | {S胒%u\CG}ƀ$Q}Ћ$ D#Ğk<ôw	X\d+z'Zy$לªBC	4m>J~dN)j<pWKM~F6y/kn=/ψ}#f]놤JRp |
| --- | Minor | ?hBQ;wA(3/5zRCop.(B>h/`@[(d)ΟjRbu>}۰ OB]2jyݗ_;=vt0>ARk1re Gᯏx(W |
| --- | Minor | &6R'*'d,]nUIrLrwAP2n2n<_U@jHS\ |
| --- | Minor | V9-0dc\Hуz2+@REmOWt$/6U!@[הx(d@BB)so |
| --- | Minor | [Ӡ6 |
| --- | Minor | .)W{*V(9k6:JJgC |
| --- | Minor | x&]5 |
| --- | Minor | z |
| --- | Minor | GHc?/I^!.7|8[(꡺ek}BtD`Iuob7!Oğ<%I%6/qrs=x&3@G~~@FiV%t,y ( |
| --- | Minor | ydc!]~Ȟ	{A<*ǅ) ,*DV[`aQFs8&ܸvIz#F~~r|FH-}N&n{/ +:5d@H&sOJy+ |
| --- | Minor | =cHrV~WW9;AUM䌜5q-5pR?eך]JޫGq_a4/ ]'7Ojݛ!]Uaxձ^xBlP^I`3Z-Xř LhxWȅFH޻ÁjK]>6ͬ6)_E-qGp&#Yj&KIT#Q9|NS$zSWwSm$S@KIXs`QKG |
| --- | Minor | /wZe3)?0_.clp0ɹp<34,?pHߒI`'+b}9_ >/g9ǵXߠ ǖ2] |
| --- | Minor | @KQLkFN_ZY:#)tF(xۢ!j.8JZg-fQcQo)nBZ3Pznγ!M=,% |
| --- | Minor | 0 obj |
| --- | Minor | <</Filter/FlateDecode/Length 4646>> |
| --- | Minor | \KW%,U|ZD$@+'	v4ZAeHv)M6veb6,wvr'YY۽xC>ß厾1`@_RwN__ |
| --- | Minor | =y{B;i0NJW}ݗz'΅7OS@,v'ۅ0;xs@44:ihiJo	SpwOvҕUXJS4	,}fE"Z</[VSp=mi\خ:O-8U#z?KÇCOtq4̷U>r^ |
| --- | Minor | #y]z>%*!!ո |
| --- | Minor | ѭ ^)jUnP.l-	 |
| --- | Minor | %c+l4 |
| --- | Minor | mo6dG׍ |
| --- | Minor | ?kÖQ+2OS$;fQ83nn\ u7|,'8x$>efALyb}㖏YT2A2/i@$58G5X'UT`xz(q9=ˎ`6 ? |
| --- | Minor | G_r0Ι([*wM |
| --- | Minor | @H<`<Gb$J+ӑhnFYoz`47l 5FEj%kRñ |
| --- | Minor | e~%T#RB6眖yޏ"wrSDu 5H_p	[/O8nOo̪5!3kйFY@Ĉ yYYb!Pdvf>}zb鼓QHBJ]8 c'P{>wYS(%KG#:x(k6ssAi[ET |
| --- | Minor | TVDچa$DH?	=-aIBR\#T*W# |
| --- | Minor | (] 9m#9 |
| --- | Minor | D`M2K޵FۚS7=g\5<:D/4h=)CVX3%glw:#xbڂ?{ |
| --- | Minor | :~ Ys\a(Ks^m+	5m]5C3()(cw	mTVe1vԷs6:!BM\1-e3UC@YD_jEw\1{j'vb2k$,]LneAÕSU&	[ld*XCJX̖Ձ |
| --- | Minor | @AK-aڄ )oߖy"0;i	μ kM?˃Mi=Yduv{L׼ۡmC9kl753I)v*q.ZGɶhCP~љ>c,	 _ |
| --- | Minor | ?cixah2 |
| --- | Minor | &j,f3~.*<8dl |
| --- | Minor | *v $ |
| --- | Minor | ՛W?0!Ck |
| --- | Minor | ;+Zt |
| --- | Minor | %N9~C0%FQ4(oOsK/*zV:∑nE`e!"ɶ6]w?pFOӜCeGo7_./ĝ,j%{tPvdfŇj9TK. O%]\Z*+*@FZe,Gf Egyc |
| --- | Minor | CyalEHgĀލ"àk3I cve:WS |
| --- | Minor | +Ϲpan;I[0y6޼ϐNv͐ZTh |
| --- | Minor | <	0Nx^=ϫyαS|j?MԜ\Ƅ%6Ғf2jYhb |
| --- | Minor | P+BۜY$xvumHmm< |
| --- | Minor | `مf21 ;HH*D-	+ΘYƑNh1C?rjB4OFS{ODS{ĞS.K_=ac|Ҙ/<Hl5>>)9,^ |
| --- | Minor | j%p\$ߧܲD( (^کPaCH3q	q_|p|HOtKnv>:p2z F3|d!K λumjU)LI^S,&f0[	h@5x@kPm椕%'1(KF]W||Bs,Ruٯs[FC+nOe(*Ė֟j>MB^ |
| --- | Minor | )/APKTc*>fHlѼUz1g(߱K2%PzIPʁ/2%)rehAB^~1g/?ʊ\	.d;+ۤtXd@I/c"ke%,e.@oh1FA. 5"I_W ½#-SUNAwiH>;%V7<IӪbtV4MB e'w-1D>z.-V,٨9(J;f)z6Al/sOH7(ap> ;p*ŏo_b o~.iUdNK݊TP;c"LpTddݼ&Y!F*.2YGЗy/SovN@ϙzwΧlJчabg~0%K/kn |
| --- | Minor | >buXHu>h--n[d8"/ca#w6 |
| --- | Minor | 4c%r?ACH=_+nWcշ+R+j۠$*%~R"8&þM0}`9YfYzION{7GK)hksͭ)r]]"mS0 |
| --- | Minor | '&*Wj`s:2WBqAPHuE&sNI~]9ܿ|60双@2$!Ll| nSlc>t] bC8sP+;AXy{$9V50pր	PP%6y3 Ar |
| --- | Minor | hz[Usͭ}F3U)=`I,J)M8\xJꮘKӾ |
| --- | Minor | (6))4sSw:sZh |
| --- | Minor | .ǐ4>ǽ$GeVl *5umVd=D0I=hYw,~	22-![±6]_'ў`e,,UpbCD\"ۗ6Wf"X",l(LS[jN 2NMX%7<&ٗIş9%h"RPF@E釒OyZF~(nM.2zFi;R$S@A/J^qcS3:U2zB,΋ݶIʪF5^;'|SDC=d)plQZxȅs$#L^g<CpLvͽKG1SC{I |
| --- | Minor | :HXT1z^}V˙`92rIs]O;M5"[)}- gK̔ST],:iL`K̑_P\32I㮪5v]u*t[QnSt5̎GΎ25QEs |
| --- | Minor | ] LQj"{A/ |
| --- | Minor | `l7CiMoew\_t*隐x 0jayP'*blC%/9*Vo^;/qD/Zj'KE8FNEH(+EKK̍okiȼ\ZWzvkmCF/zCQY34/,6-B)@38 R/kp*3bogX[cŮjczcqbN8ksd	Z8Q8$Թ7+/?lMV{^,5RE{0xaHo%;SRp}ϒСC"&ЫwpӎH~~[Kbi|ڒA |
| --- | Minor | >	oB^k5 i탵RGk*	t~Cu%_9sʷb9t3v+)V$檐~G[ic~J~#ߧG	(r?b!#>캈Y{A,hc4Fbz$@'!ܝ鼬PA]Z9Xa`UuvPTnmM͒-*ܻ^ ÖN܈3j@2m7VZcHnɇ^A-[;>j2 :;#9>V'72͟wA'aMXI(w}[Pdٓ6e0hIN=^UF(e^K>uj+TYAF[{m ƽ;AvdU"%.ֿf |
| --- | Minor | 0 obj |
| --- | Minor | <</Filter/FlateDecode/Length 4896>> |
| --- | Minor | \Il7+j*cPbX ."~X >IHݷl_gToN$up*;}|5N?:'9}x;) |
| --- | Minor | iLЧ]tPW/Ji?O&Ui,c嬽Ye$O˨6Pߗ?֔Ӛח/>&^QFB:9ZVtZgMlGx	?=@zU`.}ôEiS+<1.MCika3D@:O;3/h50Q}E7h/e{iktD//|4׆@dxәX]~|iy[i+5"Z'6]=@@y8yseg'r	om?U |
| --- | Minor | _DzQ |
| --- | Minor | +80Z_&>'/ |
| --- | Minor | (Ҁ,N<P&7\ 2P13R˧t@GyGO.lMKRYqQ%EIu=#Q)a2"x(/&ltQ+HyIۓQӛhq2"$Gb7ДrnIzE	EPY/t?.WS3Z)iϾV,T"=WxM!g꘦d|un4 ̻t|Fo̤GTցg)[mPQiXRK w:os הcHI8F^7n>yǘK |
| --- | Minor |  ee._Y) :ں.⬬J*BA7dojmnנ7dHip0&5&zHO |
| --- | Minor | ;6GcwURfVy|RBUTӕ&\Ҟ|; |
| --- | Minor | x{Xx|U6hblLTN%;R8C<:S͠@3$⚔bUc'/ZHWEMp;VoB%kQ#fmy/Z]z:8.W)o.+xd	/AWǗ|<SۨaėxVTZ& |
| --- | Minor | ^h/H5a0	Y'UҬ*V] |
| --- | Minor | !Nު.$Z5獻!!-;2LA(ԛ+jtU5;ߴc$S-ޘ/Fj2~@x{2d3!egY.&"N&y_Cuf:m"2Wu?ڲ\5d0ۮwe&zbnZB[?I;\vUYTBv r ) |
| --- | Minor | $Dh?ټ~0RPBR|^cr( |
| --- | Minor | Fmv;V)FbF! |
| --- | Minor | _'Es'kqWޑB&-^1	nJ+"#ԔV8d6y(^5"'kCԸUS$[c &Me6O)mLwBH$ǯf8@7~p |
| --- | Minor | Q]D |
| --- | Minor | nQֶ$BXF;1Z3xt\WkuOGm0RA3a |
| --- | Minor | e+JsI}7' @U3lqCNp$6}r 3y/e^(J(D5<Cv'H |
| --- | Minor | ~Q2epX-;px"v	cV |
| --- | Minor | $/X`8Tm1r2UaPҔ`A%w`	Lh_BS)En+kx%3X]dt?,MI,N9J:|Nz86+ȟQ{}fP̙Nܺ=Ë^M{EbROrDFWᙿ^t |{L4^R<хg |
| --- | Minor | [Z |
| --- | Minor | i_i"#Q-hU}Q"deI$Rz4%/{33@ߤ뫻kO 85.AI-R^sR-ڷFB-^Ny#qKX2%wC# v~ר#G1gʨd4Ӧ;h+5*oa]6 @0"_- YH/',K݇Cy@̥͒a%zKlo;ttbeC!)oG'O9ay?EI xGe7i0-|Lnm26N:?:5񩄤o. ͼ8JGee	 |
| --- | Minor | Qe@n*,{~]a>AoSz@~p௪ܜ5'[N13cE+GE,ǲ޻0gih쑙\F Ь5{£R>ӆJqf.cl:;-̀d\˽Vx9t/gڱ2ۃ'ؾ=BSt&?c2IPT[nf IPٵq!No],tFz\.q95W.wV"dyiU*M>!z>Q6TYaoFs	QN8ܝSqVMu*+BdO| |
| --- | Minor | i1dZݖ?Zi+E'5H,2eNN'TMՌ^IE%w~A;pC/N1rP^bj9v^]:#ϗhRsr0H^! |
| --- | Minor | {  <vn/Hq9C_;\,3}Nc!mDω~k`5	QAs.%r9^/w)T9p?5*5❘Y_ՍݥL}Qo}#꽫K*+3u6Dap7vUoIW(nᒱPiǏ\Mn$0=2GY	i@2)"mԈXGsS6WSiCJjXY=}/KX1!<Ew |
| --- | Minor | &kg]ZD\ |
| --- | Minor | @+jBs[Wy֥ 7PNfKعH6Mmoc)9P99ʻ5ؠt;z!~ZV%?WF϶N(.g)$Ydfg--l7mYMKsLxkNӡchJV@ |
| --- | Minor | DT |
| --- | Minor | %AáeNhLD%Pp9v:Vk"mjgg(y!]@gC~$Jv49F;Ϊj67{-#x |
| --- | Minor | ,ASbct2NjL΢gB¬d{m4Q֠<aӫˮbs@&a^xoXɉhI_!wKh&F*ΟF' |
| --- | Minor | ިBP0HgQ質GZOӾ)z=Q*SkJyDi^ʊ |
| --- | Minor |  Siζ#k}6<Syχ<3m }|ksX.JY_jɸ1zY|5TDU^Z<$ph+ |
| --- | Minor | 	z; IF$0YAUSX]zS=waX8*4CR+)]6=`cv9S< JiEWugE꫐ȃg=ZyXG0جedXн7[̚Q. |
| --- | Minor | =ޮb{<5N	^]J٭rSׄ 4P1GK>R%EGE9vFD^X+W |
| --- | Minor | 3@	Z&f-e[u |
| --- | Minor | Mt |
| --- | Minor | |ҁKFe~r.u3%dͱslD0oc侊 |
| --- | Minor | =jyn3	}X5ˠxh/n=?f wE4! 0FtNJd(RdSMy*i%>vW/n#L1Q?t>¯n |
| --- | Minor | = |
| --- | Minor | }0Sv~΢*6EjT5Euv(շl!/Gs{|/Ӽ4֊kSQDGUDA~}隵}^zԆ|-bGB!=5 |
| --- | Minor | /ތI[@	C좛`a| |
| --- | Minor | V,w٬{<O߼+r1$NpWZT&LyshXPTo fbB$v.8T3OnoC*K_XP_q%m2J |
| --- | Minor | lZ@~taV{|5EAX^x,X ٗ} |
| --- | Minor | ?v;̮NS֤.g |
| --- | Minor | _R RJ	G/N_N8|&mqJ0)A\tJ#E |
| --- | Minor | ־ʕ7}hF3*bueT6!FjO/wlֳ Nk~^V`۷cuӠ[*gASKd»ʗsHjm(O5B^pNen/ԵGbácĊ`np"a'}/d؅ Ъ*cTIh |
| --- | Minor | tRQAhKg`Kj$gގ׺"Hϰ"(o7Ern+[бC9,D@$0{>{(4\2}\s(q"5	za0@㧓-rRo, |
| --- | Minor | 0 obj |
| --- | Minor | <</Filter/FlateDecode/Length 5099>> |
| --- | Minor | \Kc9+Pv=@BBfѹ4S~]Or{A=79o/^[{y/|7~xE` g!ǿF^XͼH	M5ɨ[CjB(&B7!rR^[1B8b[ayyX-[nB.elX&٬WxOlSyY_c#e@}_L|O3Se6Z!jFVDifҷUel=1=c9VV$Ն{YT`S6NU&}[Z,-'vlB[ |
| --- | Minor | -F>b^X'=J-k)}9	%=r/nNH,pa62^=XyU~3ҁ)_p,8RL,36ڸREctMTqQ$eMh4r?VOt:͹t[SM(0ӑ%y[\0<GyTnHc;ʡgT>M_j7x:ӪBVXuqZ=IRj}:Eq)Q  ut^Az.ңЄ H5[C1b|NwG('$.Ed7_Iriߓ,|RĤ=%x(fnyAV͖[mexPE3ښjWe0wrm-o1ri^MɅ&0@sJ}_ORp¿K}?V\	B6Q7 Nn߄*8JOMK/5%Oͷޢ׻6+pӥumMנ`ӵ |
| --- | Minor | >%Ν_zhHQ'N.ZZ`ߍhTJ8lfD6AvIoUo`AͅQӨ)A4vp? |
| --- | Minor | ?JX+ |
| --- | Minor | t JwO8%^{ms@9-Ame|8Qu n?%eaXhvy?ᒠ<"2Q(<r\y)WR,Rv/T Y%GϨ>qP鉃ь#fCsT͌/l| |
| --- | Minor | ˪{Pk:J`+G3mw6][m'R@sضp-߶d>}X zS|$X%I9~z]`qWH%_@p\-kp\/P̹(*)A\lsP	{F̄fAαp1x6۩Jg|A}"`R |
| --- | Minor | oL0.TF纥mvb6R[bzN+={ٸ<:N~Jt |
| --- | Minor | =L,!GT?wv1̂(Dr ¹rcM/1=q/+'5zM"#SGK)X6@TZ򶶴i;CKv^:"iA&}c-YD,@"L#ZpԂT2@?,4pft=E[d3Q *;&M|KwGLEn JJ=PFEUDev=!6=!'0O.-zW}n;iM! |
| --- | Minor | ]_?ҡ4~ŹJiA |
| --- | Minor | 0TܘA! |
| --- | Minor | !!Lj@ZvI,wiR"1NNV(? |
| --- | Minor | (vGeUǡR#UG""H#GDR%hD1=,jQkw0Z<#UUH^(DnC68u#$X8]Ye9OszlxQbE>q.AUmu83t}eV&08ir_01	,g0H~2G~CcZFGɑ̨QSCM&O퇥V	L!95#Nvm |
| --- | Minor | Z5/9a)S!n3P%7v*1 |
| --- | Minor | @$9hSt}qʈX<jΖ,ӄ<d>޻PY}yFRtA+g<E |
| --- | Minor | )GqMCģh崥$J2\)u=U}ʝL`ؓ?hSo͊NA0cG̓0lRv3uGIRyXث:y=0ۣ,nm{ǐDū:)E~qN|)UE]nNkEJkW |
| --- | Minor | agiI |
| --- | Minor | %jaCoCT(M1@cjx"idzi&v'I;txi|+=yZJUOsսaLJ܁/Z.Ip>'BmX'!0&lkvrwM?(SLYH{dB$6Cid<o^p5yCkGovx52lCNY=b|y |
| --- | Minor | [Mt[CtBN+Wc]NGEhu<4"?bs4j|ET-[L |
| --- | Minor | .}f cV	3kg)'gJī#pΡ5ؚsI+vA !{Mıa*!XFm UbtKzE<3O6¬p u, 4pMygΜb&[.NZxZ[ck+ee/鴝u3aP!s'_6<7"o5c6r֧P3 |
| --- | Minor | |H:wESfLxķlյhQ%VPV XdԣvA9}ú |
| --- | Minor | Lk*ÎXLL` |
| --- | Minor | ,r |
| --- | Minor | /cNÜ'Fy.ʪY`>)Ć0^棓l.x?Sz3 |
| --- | Minor | M~E͕Vj̽Jm-%Q$`#^#HGxt$>% |
| --- | Minor | ً"SVeix	*W(gvH5RcԏA08=gwhZH@"q7XdJZ1:(zH2gnouS#7H6Eh70~HV؜($̉KP孬8Nt7lp`UKLaԹyCH4OhY^t%HBť6`%61s)Ywk,ld?,eBKf)YYuȢa<q Cu:_J3[ČRpk#_e\Bd]AiɴOIbԞ\x)cf}ϱk΀˨UM3-*YS(%P}*܂1!bODT;w.T1B5ߩUDkأwH|ʨWHa|b'+7aM|7_VJ,BMVNeRar#B*x3iQLYvcobrԑ |
| --- | Minor | ͞9=R̸-vwA1IVkǻfQιL/l^Iדkkŵ5䭁]UFJtW]~0w |
| --- | Minor | =<Uyhp̈́vi˩fX,g5ȧY\JFYS,JK,$/KM"ܤtkۄ' .;e!xڂp}UC)Xlu+Zyu |
| --- | Minor | '(i[#ߵjP&wȘٌtMYf1+yXI.g],p*SR=JCPx##[l-ٶi	GP:V@ʔo-{#L8S݆n	k?ue`S`eaa6qoayS |
| --- | Minor | $ׅ'5珨wş>XV{.X&23*][mj7FPX~X՗kkw^N.MH![泗w@^Qu,k$H@ERNcsFWexItu`5S8q<,w1(`5#b=Z ŅzET=8c7NU8~3/%2sjyr}H0Cn͟~#e&g!f?Z1nzó- ԉ޶׻`Vz-@ak>d9!a쁊TH蝉]U~r}Zf}ȡZi0aȏlmZssI%3#MQŐ|'vRNY31ki.ڏouŽT-A"McO=V<GyY |
| --- | Minor | *()y.Y8Mt-lȰ.y<]+3HRJTrF)<\J}"~Ę'<f~,0;bE­ϗp/m+S$ z(5"Nό./#&繶@j5AEƊ>OǰW9!sOhBtdohAS]yf"nJb*1%-YLOdkhTB5lb+kcV8cN:XwZlPsl8ZĴ\Js礵eYnh?+RХ]y(x)w5Rj;gr6WsIGYv;-c"߬:Q:TmU0Al`C*xqnc(jn:fn~N^C.i=XMy%C/#H| 1}~ W`jd!OcYu5ڠ |
| --- | Minor | {zmbZҵrM8'!nrBSIh}|k |
| --- | Minor | /J2lZ	BMz״g |
| --- | Minor | 0 obj |
| --- | Minor | <</Length1 3716/Length 2489/Filter/FlateDecode>> |
| --- | Minor | {pTdMB<M&$H͒̓l+	( FJ`ۨF XAtC3NժUg`gn{mp۞38K |
| --- | Minor | #YVRd#R&6ry|cGʪV?t_2㓌g/5m7W׶#16"y |
| --- | Minor | >E7opu<l+/54w{F9Xٞ|rЈ |
| --- | Minor | %ƿcұ5[Y2cOs[mPMoY[[#^q1lUq?'\|lƺȦN߉b/ cmh:)(Y|JJL |
| --- | Minor | hT^O.?\XQkތƽf2S)jFR0F(xf3^E*I<L4}WyJ$dj;ְ4Q+pƢrڢ|:Hh`fFbbAsL17*/rkUnu"aG!׎6^idH#bv7@p}ti?/lFeGtJgُ>g~=!TTTiZC#ʹz3d9D[As-fKU@N*RuĹ4zyɬi5K#5<_e'GtejPJv5f-172UGKC:uT8c|η3]M5Wtiu%NXxUr2j+2eK)*4Wk<o5GzF+׈~9^[?ɚYQҒQ5%ZâXҒ;'Oj#>>ռ)D~wzdk:Q |
| --- | Minor | Igբ>MzZpx5C&M|WG?xXD̩y%Cz^~^)%I.%z˶[|ʪ/^=/Wx	[N})]FQeVN~9>nkanXQ.V^W"ӸD+ΜZ  |
| --- | Minor | ,'K6j\(mJM{?IYyVsgE]g?l^3<v\nk+**ѿn`paj/knU]5%G< |
| --- | Minor | }uz)mvT&2zD88nSN;0Ψk?ՙ~΄y$(a{+.tL}l?-D"Gߕ1B?[l8݆>n=<я6Z-ޢra1ljAw׊5dیs%bX>k:;*qTMb,)EP<(B6p6A/t}÷ |
| --- | Minor | dm92?"j{_&㾎m67L;V&f27^Leÿ7w<lq؏TQ6sxc6,Q}muͧܶ.2gVyi* |
| --- | Minor | # рMݸFx#qg\5^«řW4yƇW4𲎗txL>we_u:8yZC_~3!< |
| --- | Minor | '}xDH>DO'8.{ |
| --- | Minor | <+M><:G8|(^P@<Ɔix[ƣ7 G#^801b>bΉۺÃxX^A=ղg=bnS=Ů.+ |
| --- | Minor | QӅzGd׋{c |
| --- | Minor | 4;=㱽+^n+woKw-?E[ز#\Mf6M@u]FwE."օ֖5hf'E8hMWqPnP--꽲 |
| --- | Minor | QE"Bm꨹3[3wֱw6kKFOt*U!pde'`YQ7biSlK|(S8]G",	cQS.r(V;QE `cX؋"K.ir~͵y\; |
| --- | Minor | .80[G~&u2Og~7|b̊AnN-ANvIA9fIY1!Ջ3493x349C>-WN/4NlZ.21^GV##=QfT!SlI䒞xΉIlEi11pCR*gsc#ى$MIahn4hv#ypt8s#OE<pG |
| --- | Minor | #Al`Nvػ6 |
| --- | Minor | ,'-]l'}Ldv(U ʀڱW[-')	~ |
| --- | Minor | 0 obj |
| --- | Minor | <</Length 35/Filter/FlateDecode>> |
| --- | Minor | `D4q(`Q@`C D  |
| --- | Minor | 0 obj |
| --- | Minor | <</Length 252/Filter/FlateDecode>> |
| --- | Minor | n E{bMb_JeYvy(N*+Ba\3ƑWsf.0ïݭs6^X#~ |
| --- | Minor | ;@[Q9$d99Y  |
| --- | Minor | '%>0 Qcn絯_B	]k[hg^Ąyi۴WSKkP5Z-4VKuI_$W~ex.8P5,PbQcA}&#mkR-1Reܒu |
| --- | Minor | ?]y ` |
| --- | Minor | 0 obj |
| --- | Minor | <</Length1 15424/Length 10186/Filter/FlateDecode>> |
| --- | Minor | {	tUuk齫t;Iwg,B `@ĉH $`paBdEQ28èd0 |
| --- | Minor | qqpF!.b2nu:3^չ}o_*Bfag1yh2BjةwNq~ w8qWGB0nMFHg[8g1ٶo0-[iU|~Fsj#Ns݂/> S)}r^pP)\0{_;Ǘ.\X瘇PUds |
| --- | Minor | )ZpΊn.+`Y4ga, jLGai |
| --- | Minor | {K/SDyC,6 |
| --- | Minor | 4&@yV"{K*rΒE	<W%.B*:Rk^+ |
| --- | Minor | 2S/}yڔKӽM	6nBhvnw8$OϹ2ꭸmVo?}']FFu"@mJB~0܍_jiv8SpPkicRW:<Stztu=XȄ7V`1ڄ8xQG,)EsQ ӑ0` |
| --- | Minor | 5m1~'(&e|ÇzeʲsAsY蘇]X/SzM!0 \<&lT' |
| --- | Minor | @ơl);{t~BSQ	+< ws\XwٿC!X[n& |
| --- | Minor | (l(LRS6 ԍp? #q\ |
| --- | Minor | *?Bv4&ԓh>cxp<0!)!$!9ubybͼUǄroPB!93Y}"{P2d$>Byh<f2T	ƚA * *$@MGs jP{?szwz޳<OaP~&eP#t`1]a!E*jJr+QCcAAnvhZth3Q+ZeC[m1heaiQ |
| --- | Minor | A5O-8߅$T:>GӬpGaE8hD	>0oBw161d**O4V2eۡ<^A{Q.9V s	?*Ԉjr8r)wZ9oʁu"2 |
| --- | Minor | |kP9[O9G+h`z?L/z؇6  |
| --- | Minor | |1r5*owM&:@z'1>Ud05)"pX`-Lg<ozDӂk=Sg..j!	6!v4ĩ<-ƌ:h4\>tiHHlZi8GQ^##0jw[p I4gxٙ_kO/ė<\/-[.7r%ʫ]N _mКm-Y&eEnc=vur|?.](=V _@AêU3#U;9}83 |
| --- | Minor | [1ؚ V(~exDy.`ڼS O^oNكm[,?uD<dss.҉W;B8LB^ {`&=eJvΤSΞ2Jb]e	4\!N_b.EfUFm${jHR>*rE&e/q]i^E<<O3TE~N~^nwE |
| --- | Minor | Vw0РR[d³TZp[w f1@Adɏ[43f |
| --- | Minor | i{O |
| --- | Minor | Η |
| --- | Minor | [0ZTI |
| --- | Minor | 2M^ì.|_{N&)e,yuVdԣ%L+/7Y:;`;2hDlFW.t\ ~rr@'2:uʝ" y<m.Ϛg@LqfY7pqĸX+.^:yS{~}'nVcMN_|(ýVyBܶ㇇wLz2]J	LZz2PAMaT,LzbԪxB.8ۻs/vl)95ƅG=jc !Nl͸{bg |
| --- | Minor | +6N<,D0IA`XfF(Dؤkdޒrgw=Kgq|;E_|9NXHvk*\^ FK	^,%k	hmb41ΫcL#}Qل,n73E=RtBP0%tS5 |
| --- | Minor | $Fy`TFe2FctFdnؖyJ3IlVM2c`6($w!=3nqy/ZAumOނ |
| --- | Minor | }#=c7x3QL'Ŧ<)V#*+cjJ\eD&&fWsD`IM+}:ĊȋIeYA4ɔKOqOLY#HQqs#춸tyq׮Ʀ^\_0\鑿#q/]{`љyϜ9Wxn2Z|^_VR.h qW&40c4ra.8d|O+'_z]WH?xmq&/`OLZϔ"WյЊ>1O3p)6>%1ƒ@|t\]6y>ohQX6+5pPv:8'}䑽%?~W8!_wo'~.] |
| --- | Minor | >tCȲv߰k9{tmw\#R=?LPGNO	Tk%F,Q38-7GTځ?DXK.7v3nfݜ;v{^w@CPp0FNza'r/_FhbϜOl޹s杻'&N.cN~Z^!O^RXPw΁rѨ'AƓBi1ID?N=X'uꕑuS|If8?B\(s0>*5l 3"t@YХN |
| --- | Minor | .@)MI>Oqxj<c,Pm|}L@sxv8O8m烅ۆ9p|r-3xBeUʝϼ$5kW739'M_M5ݻ]c	]ǫXӘ+YWMWX}5ܷ~_n*['|4*Tym2~h4g1xĈ׍%E`1zQ&3 |
| --- | Minor | abV%-jb$)dйHuK	D$3D-)ahd$>IdR͊?qV&xI |
| --- | Minor | ?˝=dblz>ۿgӪ}L4srr<NnU>h4Xr9!"6te(d4&FݠNg;GDwT<Mn |
| --- | Minor | vYouou_}{ڷ~xxb}H#_?	Kr'j~4)f1oZ_+W*n.7TFj`QYcb4i.s#HS/(v]l	8t 晠qC |
| --- | Minor | }{gR_/ۙQc=M0nـ |
| --- | Minor | [10bVh#!uv!R0>6Xloo0&L+`EْUW沨QxdH<$=%{<.LPh]'z^>q{V |
| --- | Minor | ;Q@rj%RW!>^1>OeخPv3[0s@i.y#9ٟ&c4'+ju7u:de#p"_Dع\+JhuhhcHl⣓IB;sO4E;CglMLR.N]L&X)E	)(/wZIҴ"ٝI&Vhhs91CC<C9kk'ǹ{{k|}'ߛ[Tj+u |
| --- | Minor | [[Wzw[[ݜڒʀg}W4Q7Jt;v꣯^Tm:'o=/-S;4\=tę_SZ|+rGA*%+hH#\jNKzPQyCJgB<#B(ink짊*}PDb&/!Jv#R"St*97Uu'\z<d9{ |
| --- | Minor | .+|ЫhҒ}R˫uY:6UŻ91)qHWg`N#i9glDJF`{_l;}!jCcG.ŋ)U)+NuI)ic۸6f?yq	B!κ,&jn7B/}΢YhfKj[5WzfY83?OlY]?L;ˣkϽ!z(P[A^^4VJr&A1U |
| --- | Minor | CjfYP z&pMgt+"RS	nVM4۬@q(ip٠gۮ_ovmԸeKmT޳xfW|nvrԹ~ozE |
| --- | Minor | ,ɉvۛ~QSz)rtNdu).~A	BAp pF&@+H_ࣻvXى8pgʨmZ_|rUXg.w=v{` "&췉ć(+ʩI |
| --- | Minor | 'Qǆ,Ŗ&H!lFlf_6n۴y˖ųqvW4I.᭲o~G=z&Њ\hèluHkE6͛tEQ*͉\iL+)'NfOMΣ<svQ/./~qv7ȟ㈿f.[7laê-n<PxWOL%>!R |
| --- | Minor | <BR̚:bբΪcPqkd1ūA`q;?qfbFlD+$ΐyaLsDcfǽpnKw.=ϵ⨵#9)[6TtP^NU9|4ҡ9\w#?/e!OQꢓ[TO |
| --- | Minor | &6n|D4uD}(+)dGJǀ4::ک|EX}2BbzCzK:6)Ơa:A_}eWN*2]ΛZK]}ZEw?RZR[M_!o |
| --- | Minor | RU4DdfFŧ@%0]lW/KwMn.F]!Es%"&3g*[ٽVmVEosA5rXv* `ː)xN:P9"ޯ󁮙t |
| --- | Minor | `']~`gCKו2G^GN9$E`4*풙SUhB $(Hh!q3^r1ߤr'=hXJV'K?_Q-~rŰ+*[Tɂt|umiv/&͊;wn߾s6!W`eW=dY~FUy& |
| --- | Minor | Kcd&zvS_gh[79<ĻHp-"7+`o# |
| --- | Minor | 	>𾾨zK"gƕo+K}DJ*XgB\&δGQ1iHU>p|[Lς*oaH_.Ff8%$aJh!٥H}E=7š( |
| --- | Minor | }V_6,FB	ѻܔ뷼6ՖA;o('3^0YrhLFJ1<\F,#B\/)[ffnTlyL2v{WEx*bX_\@[+<ނYqkk=kkcp߽߳߻?v\ڐzzv0`AIIɈ'geޚ+v[O}QM9f^Wg2]tu[wmC/_V7s@[SZdڴQ?KIhrrIJh&+Bu<Z)&Ws>2r>%L߱#?EN6NT6JUGcCShpl |
| --- | Minor | $f}/yq#[>DW	ъuem)'>ցJv[5H0TG]"0!e8iJП:09^6Z\ |
| --- | Minor | *`!MKkSXݏg+u*?^^u"SG/#>0V)GfT{ |
| --- | Minor | 5ӷҩ8dЫUb6jwO@=hIyzd4TuB<taLT*ź8ڦI@)l |
| --- | Minor | 8Տ52,@e2n9BBBBJuwɵSr-ȯ'{4R4EZ`^j m |
| --- | Minor | k*@3xׅcd9kxDm  V匠\${,FQՙ4.My='0̬lj9`QOʨf+UZF)g~E |
| --- | Minor | @X4Xs!06J |
| --- | Minor | 7rɻ8C96p\I(?I&>C1QL4%;>WsC x<֐g*L>aC |
| --- | Minor | gFtttr,JRCqkZW2+JVܰĸD\bZb]a[ԱԹԵm6i767Y::׺i%,k{kC]X̌4ݍe<il[W˕8A~AagVTr<\>	Y 62hpE1Nh4h5zhPT0U |
| --- | Minor | jLVE3F'b"lj0uZvhfЀ@Suu$4B)ǞmC JL	!ׯoj5 |
| --- | Minor | %`*Z"3wqStafC6Zr.ZRRqiskYT˾՞WW[ʘ!>[aʻE[6w}ȼJj^HdgE%Сut̻OtKO7*llD1ך_,w4tMv2LztvzB-&lVCoeE]0pMöyYu/VL"	~n$K$4[&P w7"ba̸1==1e_#4*m)Aa |
| --- | Minor | *`qɄ!qtQGi~k[Ee|?;J~˧@I	iAQHYv,Ԝ_+d7kZɛԱXU犷ęMcu !BߓAB.C~Y4	?*em7]+|ɑ9Tvd3mo(9׾o*C7Je48p"Q(R>mrWG@sXufOGjo|.{ .C/AENPYKj1>#*9M)>7pf̏k}6RW{3M{K)ZG9ϼkb@stPjRΥ:Tm3Q7ﱰjd	40 |
| --- | Minor | ·#~g@cv_ |
| --- | Minor | URݠ'_c0ƃ=WZ.>K!]3i9}o1ε!KT 5C&)!ß |
| --- | Minor | ,_P-<j[u8=sPiPG3OL>yۛ+&MeNXY_]	[y	ׁ[P$`FaLv?HߗP&Az)^_"8rB2&b8.ݥٓ0&[$1u:o5g1ۛՊӲ;[~K=+^$GεݪAw?Rvmr>}|3D@)8<',T{?үmՍ# Ӝm#; m:ޫpQ5׈I2SLde_G97Yh>s |
| --- | Minor | 5)m(waB5$[ͮbDG%.-6AXwfr8p[׾# |
| --- | Minor | 1c< PK;3X~+^SS=^ݬa5Yc.]9qJ-ψ&ko<p}(Fh}voY-RY	;_:E܉~~xL]g9(]CPZދh<=(pfh.@xHYj݋Jxa4UAnUJ/go1@jh |
| --- | Minor | s` |
| --- | Minor | t}~\X<|;Gw:ӕ]@_GTJ |
| --- | Minor | \R |
| --- | Minor | S>C3A"~gFWs#)5<xY$t'pf:p |
| --- | Minor | /з7bX*t |
| --- | Minor | .*fp?&~`+Z |
| --- | Minor | ׋O^ӓ3}ܙbrGNq-9%l^	5H^QV&/LuL^XEs:7Vr@G~$*&Ɛ}A32y<=@Whw"yR$O=c=2y1{<<&ݻv.	CbM |
| --- | Minor | ۖ@ns[-dk+$5 |
| --- | Minor | $gѐGNMUcdZnlF5!66dÅcdj |
| --- | Minor |  xmH י1d}k)]g"k`5 y0<ܯ%2io/HVz#Bꍤn5|[E-y(ZCjdrLj,֓[,Z8[TA':R$ |
| --- | Minor | dR+=FJW'p |
| --- | Minor | @J y62W&sdR4;+trL |
| --- | Minor | @&,\&3d2L;UN#2BI&iɄb2>VōAX"rc-$L0neFWQ#EnFdFh&td8 |
| --- | Minor | IP |
| --- | Minor | %;TC䘹!$g1&'d5ed`h%A |
| --- | Minor | !j.!|I #&6.#dbc4\f\Or$HTMSIrRKA  AI |
| --- | Minor | |N83Xz"9o!M'xNnm"lHlt2W<q:s:q 6$B$6UY*11{M2G#oAp =,$zD4h FJ0q*+Lp$,,ƦX< V\{ |
| --- | Minor | 0 obj |
| --- | Minor | <</Length 145/Filter/FlateDecode>> |
| --- | Minor | Л2 |
| --- | Minor | "8g0a6$URnkF%Jd'馗~'>*5Τ<V}z5<gE^kVY筚g6%.;?                *f |
| --- | Minor | 0 obj |
| --- | Minor | <</Length 394/Filter/FlateDecode>> |
| --- | Minor | Sn0>2¡@!9=6]ux^+/,Tc[º^ |
| --- | Minor | +zD1}8fLAu^hd7E/m΋ZӋ0%Hƞ~N5>M4\>(K&ޚ6yW	˺iu"[v4OMK7 |
| --- | Minor | ~JVt)Hv[|lgG'onJuTx%4*RPwr |
| --- | Minor | M8S=fR3pZ9Y |
| --- | Minor | 'w<嘖i9r聻끓sWmPCs7!Gycsj7#Sp^̲2{g.ɶ])&E6+K.4N&˼ |
| --- | Minor | 0 obj |
| --- | Minor | <</Length1 2956/Length 1931/Filter/FlateDecode>> |
| --- | Minor | {PT.첗5颉\JZYXk6Qؖ$Ni'TN'cGq:әNvᴗ~{6|s}޹s)D(՗)<icKO L.=/ٞ۲_?Qy/DIw&n]O7T@_Xe;{ mls?|Ӟ`|{hDٞ` vpA~{{¢Xm}[Up;b-\gwwq}n:?pҁiJqrzPξ3xɤRbp^RMɎ-ay#a*|MU&8l |
| --- | Minor | <fNbm |
| --- | Minor | `Aڤu W4SS.$(IDVzwVSVAԽSS%X^IU=Vǌ'nUZ򀩻1s豩4&g<&|yw>-xdu]>ښiڦ7ښRQß7o˛A4č|ȉȷ^F0k;p |
| --- | Minor | ^ |
| --- | Minor | ?~`u7=WL:\zc]߉&TyYh*7z.Axi%_ad]_.9/ٸs.yއs;9CĳFŰÆgV3&^8/pStL1q]rTL!c8i	q7"Oy܃8ڱx~h\>obhPT=GqG#>>䑇sp865aLCr VCxn: |
| --- | Minor | e3nLG\rM؛1;vصsܥcLsRL0=M7m=K.,EwWv;*ReN.yD{[lG{T|mʠђfM[dexD-6T_0q7Qz |
| --- | Minor | .ME. |
| --- | Minor | `U+M+p^|6]ffWtaY[.!ݨ2RdF |
| --- | Minor | {Oc(K?%5d5/b˅X0#c;ys59Jo^HLYQY	Qce(Ҕ,FI&KV7QAVȢ*rc(g̔FzqZ^:h2frV#\3O\.AnTؑc<L#x8B>\,fͪ@\t4땚^/>^	7/jqipqeL8 |
| --- | Minor | ;c<IE 9O!LIU;z	%) |
| --- | Minor | >>!b6˻NNh_qa2}bJԸ(&Tr.ClPIK.`RM*X2F(EB`21i	]Ѹ.'iq6K5kr.)(BǨ:ZŽtRe=>Ny˦qN5f+Ez4!4Ue+;Hk=^?_TE@:?JKwrY:JZeKUlIѽT.ز"kw*JₓuoV~|z^SI(T9~Y6c_Sħ="73?+TVBWZiI02۴n|%Q/ivPQ;ZW?UTSxV |
| --- | Minor | w%mc|kU͢WWe9djXd |
| --- | Minor | ̲a43ot+ OUΑ |
| --- | Minor | ^{^TFKcת.+i'?=}oos;teO߯Q |
| --- | Minor | 0 obj |
| --- | Minor | <</Length 40/Filter/FlateDecode>> |
| --- | Minor | 	   	               p@+  |
| --- | Minor | 0 obj |
| --- | Minor | <</Length 228/Filter/FlateDecode>> |
| --- | Minor | n wp"I(Ru]2=5Tu `" yIR-e֏E7z֑a\aɑ0Nǣ*U2öD{^-ȷ\"opz4~ĳ  ? |
| --- | Minor | 8#EDׁA=fYKoR풰?R׻% |
| --- | Minor | .AidEJAkSthySI=eWG9Y+K)Gx[!S hsV |
| --- | Minor | 0 obj |
| --- | Minor | <</Type/XObject/Subtype/Form/BBox[-6.6 -6.6 6.6 6.6]/Length 134/Filter/FlateDecode>> |
| --- | Minor | =0wN3;z.VjR [ |
| --- | Minor | `?()O8Y3I,,=_*W&jnݨP2dŮP5fj߅̈wr2A,-tK' |
| --- | Minor | 0 obj |
| --- | Minor | <</Type/XObject/Subtype/Form/BBox[-6.6 -6.6 6.6 6.6]/Length 38/Filter/FlateDecode>> |
| --- | Minor |  \pf	a"\\N\ / |
| --- | Minor | 0 obj |
| --- | Minor | <</Type/XObject/Subtype/Form/BBox[-6.6 -6.6 6.6 6.6]/Length 35/Filter/FlateDecode>> |
| --- | Minor | bC=3\.]&r\\N\  |
| --- | Minor | 0 obj |
| --- | Minor | <</Type/XObject/Subtype/Form/BBox[-7.2627417 -7.2627417 7.2627417 7.2627417]/Length |
| --- | Minor | /Filter/FlateDecode>> |
| --- | Minor | rpn.T w |
| --- | Minor | 0 obj |
| --- | Minor | <</Type/XObject/Subtype/Form/BBox[-6.52169043 -6.29442719 6.52169043 6.6]/Length |
| --- | Minor | /Filter/FlateDecode>> |
| --- | Minor | @{^ ȵ+\C`3 |
| --- | Minor | L6tiLݰ6LW@!"uN$woXgY& |
| --- | Minor | 0 obj |
| --- | Minor | <</Type/XObject/Subtype/Form/BBox[-6.6 -6.6 6.6 6.6]/Length 71/Filter/FlateDecode>> |
| --- | Minor | ]C=3\.T~Ip&618HztEW2 * |
| --- | Minor | 0 obj |
| --- | Minor | <</Type/XObject/Subtype/Form/FormType 1/BBox[0 0 260.25125 205.6908312]/Matrix[1 |
| --- | Minor | 0 1 0 0]/Resources<</Font 219 0 R/XObject 241 0 R/ExtGState 248 0 R/Pattern 249 0 R/Shading |
| --- | Minor | 0 R/ProcSet[/PDF/Text/ImageB/ImageC/ImageI]>>/Filter/FlateDecode/Length 2987>> |
| --- | Minor | [ˎ]/hd2],$da{aHlY|Wvb}uAf0.Y,:U,y>~ۋ?yTEu5<ݼk]75Ox2A+x<OF{fKwUJ^דZ9 |
| --- | Minor | }ֱZ'֓+whZ8ILR6ie}L)f+WLRБ` |
| --- | Minor | U}Q}V(Ay; |
| --- | Minor | a`"M;TGpқ6Emlu0JSp.2zP=Sgٍ׷՗?BQ{#-Rg!Q"I:fV<{I1 3HzK:*k\xP3@ |
| --- | Minor | *E2h |
| --- | Minor | `o\;EbnsVȟa >Mpq+Y}ܻ :z >M:V?-gand嬛.Wxp7UnH#mg.PhpUn4MwTMw |
| --- | Minor | Y~* sZdK>3ܭ^7l4˝#i ˙ |
| --- | Minor | 7mkJ>kKmШK.?i|{Œg[u/Vxi_'KiwDY" |
| --- | Minor | mڎ(Gk}aɕL,pxh9wnf s	D)QK;xƟa"?e1ԅXG*&m#|FnREp*GW6	K9prnJHҡ=ȏTY=ҸKbnw_cwĲ1i2G],i\;o9>3+밂MNgp*GWN(8Zi߉_U2a_;20[ob2$olK2pD>vrOKe_v%ꃿs͙Y.'e@/k  ['Vqϙ֧ѹ3ii^KX$`G3{#,ɋQre)Ϋ8Jsx8iAD aqW&GS96%!`.X}]c`s݄wJK㕋6Zm4ӐFX|vi*Øl VڑGio]MS\$)&`Aiu7Ɉ8rHh)7W+ &՟?YwzVk=//3^hgxB;N/mpc |
| --- | Minor | c'Hİz(imXzVk=Ɗ+foX)9u`(a,9fBqW6Qg |
| --- | Minor | ٰu |
| --- | Minor | f	0/CC.MB'k05Qr1g VhҜ9$ NP(ZplLm<~vy$;­QؔȏՆpmMLiLD}aE&ra\8O'RxNӈ(NK)^ymmJ9~ |
| --- | Minor | "1z.g7 |
| --- | Minor | !10 |
| --- | Minor | `VTHK;9vqʠ RK=۔^"EI:ųGłl7^y'eZ`~b;58ɯ4ypb`}ծ |
| --- | Minor | Ʌ)3chϋGWbBQwGM#2['Mɫ\? |
| --- | Minor | VW |
| --- | Minor | ; ,'H<DH"c|R l+A*![ms66爝eF:b |
| --- | Minor | 07Uax"ng=#afzM%|砽 EbQFLHSÒ7iiyO{l=)0ln=2rٍmT|7yR#A9XQHPnn䋋|heSGGӓi#_X{xC9ۈg­i?/<uO.䲌L5k|r8=8PˎT; |
| --- | Minor |  ɋoȲeoK eh:irm<;cp{xOEنQ1{Zcb3kOcdj27=u~!6uSiD@vwIc |
| --- | Minor | 6fz<#iS6j4ޯ`F:zCQVkG2B:1 @n-ꢤtmdZ큔&٩_IGL(̍epSڂU@B)lJeP4MAU%t)nE n0z	-98 L.|9R5ϥna1ݼ+qHi֦%Rݙ@aq[=)ǫ{>y)m!h`1~yq촵,&lQ &c |
| --- | Minor | +#Xؔ--WIlMT&`.xx*UX@j:~ǅyIԵrǷ_&zEE(K$U2*Os |
| --- | Minor | )ئ{n$Wc:o4*tbDł݌܍Ht8Z/--+TM{sF"k#<}E^ĳ\rXr̔VqgbSBgCՇq񒏌}GFC!O7FR]'Q79?Xc	5_\h/tـEԘ(Zd!b7<f(rY{hAx5<fUdJ^0x{&lFN$M{; |
| --- | Minor | iۀ^N,jmӄ#1Nr&-3[-$&[k|q2/Ȑg3~2U꿶3S |
| --- | Minor | 0 obj |
| --- | Minor | <</Filter/FlateDecode/Length 2855>> |
| --- | Minor | $ |
| --- | Minor | A"Er30$Ok~}ޞd`TǏTm`6b}?}lġm |
| --- | Minor | _7AZ!6oZ[Hcoo/=˓4xQmLC]/?ỖiN~|xJc_Z |
| --- | Minor | ~]aihJW~mZEuY;)m=AՏqE6su7Ƥ]rZ&Dz˚(i<Ӣ66M=ѮiJl7qd$C]	}]'j߆3^Ѓ |
| --- | Minor | ڭ_{N V^}{}ݲ.vTvHuv>u<IWi4/L.Uby7{RP׸](KGm|r!Uۺ$MZLAne<v!s2[sW(I_յ<Luj@4Կ'cЖ&:y+2[]RWT@ʡXl;9ye8~$Ǧ;chϤorNFv[gHn|FzVhOt,Ud&uD1z;* "ӺnCe F2(b[qr<N-/\:rhoKLkЈxk5ڎy;> |
| --- | Minor | Oñb7+y[ix-X͸i[fK@\$Sɇ!@vKI靉aa[7^+VlxSwr*$Ek	$!lxgW(w:Wy\BplV=,Q~l{+deavrgAKoY?e	K" {<SCR)=5! j |
| --- | Minor | @ _0XG~ґp85?dR$O9=+phۋ:Q(1Оr_=ђҧթiLg$:[ݺ'lY0,{MAsRnX# |
| --- | Minor | 9J9ԒToIp:Vw:  |
| --- | Minor | vkb'$5wc7WfUsItKtwd5˜ʜ`pV-tGNu	:TzфTD̂<nFIxy(84>n`4[ht .KDYe5,Vyn6 |
| --- | Minor | [},s1i! |
| --- | Minor | ~gY_yedc(L\#W"}(Tyĝ+:&H*18"'$3;[jׇj,k%5$	zsWpJ0؟cT9*A*"	nI2ޘo>U`.&PV FC3GO;G9G#y7oZN|KvqAcױD?e+S)9hՂ:H. |
| --- | Minor | *ɵX9N@X;.y\2mFĴשNIU]=ك!oȂkz*7cKu2տ͋o;|0M{Z{.=FLA	2\^g}_=I&(} K-5G2`[;'Хo޵9x*Pz4jѵ^ZLW0 Y ލ,t;[q$Yru:%d jpCYs/`HС.u |
| --- | Minor | rvFzij`Ŕr'cWwoƲ` aW=k'4Yv(RZ֜~edmvߤQk9J4ւ[Nݑb"rٷ%{#*6s*5M$rDC(5@ѲDWI׻;,sMG=JYdj hB;~	z+i|ag: _Nqb߽8gy)!\~Zw"hqٿiwPLkNY|l|XZDR`ob$;4dG+';I3<޺	)1 H'>lCJ8v%w8=/Y1Ny'F Ģ;Os!;MԙlrJB@Т| |
| --- | Minor | g#v6=NR29 |
| --- | Minor | ?FDψ{9%	99%NNg |
| --- | Minor | SHy.gvס/?+r*+Z@azp1VFң#K0@p^Ѣ(_MNj{Qy0-F9l{djv?;gw+{[EQ}]F+RL3o~:mg܏8P55p~'zw[ApJ΀$=m7#ǝvt'܇sK=Qd@XPXYHR[2(`o6*oDMTHd߸ |
| --- | Minor | ()2NEɠe{fTIG8O=R6s7idgm)ѱ㔹ոvڝ)XMy?W:A|;͚Bi,.W/GndÆ'!lT٣CJJvtdӻc;Z9KR.ES\{4ߡVMdiLr0t僘0y覫&A4sAH.p18u*cIe |
| --- | Minor | 0 obj |
| --- | Minor | <</Filter/FlateDecode/Length 3643>> |
| --- | Minor | \K$9+긣U%v8: $8!'a;tu̬QN9O?I}p:n>|OcoOzo8pxz|@E!szRh׿f}j*~SΨ7.\OA)0\PlZ׳U?y"@niW|<1x-ژw"r`"'E|weN1ˢ+ӾV&tddAbA'kb`]941ǘb<i4Qd\a%	t3?_bsՊyBh[QjieVD |
| --- | Minor | "k5YI |
| --- | Minor | ='sQ*V#ܳ&2Ƥ9L ΋dH*!ªSv3֙N-x;ׅٍ:m1YUJxO)#IOٌjS1dv̥G!+"㓙rR=6nB=6^韧`DW!S(F~̆zN9O |
| --- | Minor | wwq`mξdQ3̇b*f7t{]WL@/f!mǸU1UXMSO݄F1Ah!nzdDeV |
| --- | Minor | L"PT ΚtnI+~XVr+ |
| --- | Minor | @MK,>;1x0J /( < <^[[[;9C՟Pdi3Y?ډlNdZ+3!3l2ǜWr.K%	b7a~#Ec)xxc|i14yo:j<J?z&E |
| --- | Minor | Lfźcz;Pwec^2ˇAGE&ۮãޕE>%Ǥ{*62O<+9vI6[shQFExg.p?Fhűy |
| --- | Minor | *p_B-7pdmc\sAu}ÁrQR |
| --- | Minor | *;Iyn |
| --- | Minor | ,~&YuT5-@ 낵9h+he}`z^roMRxg]p;w0$WF<tGƼj({A=c0y߉"0=(8ZAT0̘A)mYU@pL5OO_ʣ>ėUKYZ@P:Ta=ʀÌ߭p3BDvm䄒!DJAJ{2Qqtx>p;!L`:1H,Pș |
| --- | Minor | q|*<Љ |
| --- | Minor | {[>&!c`ꁢ^n?|aF/Q^Fm!7Ǯsw«#BLtH2>W4[CDYI|'qB,O6O<ܼMLѰǰN1m F}\Z2 |
| --- | Minor | \Ή|:HBc5hG |
| --- | Minor | ?if%)Ufg`g!ap]]N]P7gr$lnI"eԠ`uՔY1zs |
| --- | Minor | )<Gp |
| --- | Minor | ;JrA)Rro@tIZU3>Nņ꽷,YF3Ԅ;v`a;[M |
| --- | Minor | %'rY$o~lA okv!+*}	9iRQTVK}gCIK9L{ӡr9	%)25c&&xxF*~679tS;JIZB#ftNVo$ u8kQ}YFF#e;p++OKS,>/VˊĤ+ʅP	kea}a-$3z'"B"SBҎ!Ə| |
| --- | Minor | ?i`,K/Юa !٥N738(jR|m-ƌG(<J_rTe|/~@#*,t"5O/-4Мɾ%mr[4қFW=n.RZ6x	'oob75^D%{%wO{GgW[=#9B%̆::K1`ƙou: h%'Y	v򭊢Baa3 |
| --- | Minor | . |
| --- | Minor | ]fY]f7r_rվojJ(l躜rZ\PZ*IXZ	AuHZN8;R&)	6o}iz\y#Σٿ^ADt=tA8I"k&h8e4Ay뤢(yfaj[Ld;f)KLsΐF\m(=OfcO𚫥6]=P":`^kn?h",i9LW/Kְ:SN0l3Xi_I5K+Z;4;)40TC@5,@"Izk9ёmp,O_NY<T |
| --- | Minor | ^e=]vfEZD+(a'hI\i |
| --- | Minor | ׃a5U@RTOkt|x8f?Lu?EHbRGD+Ϙq |
| --- | Minor | TZΒ^N,e)Ipgd|,_Z{ٝUC3_@HZ!	]OygrY%o,a;i"]J+B :m?~RJ/;	x<ِ< te+]/}t\s_M-˧W%rA?,[<_@aa2hQ"3Dwabjg5 |
| --- | Minor | YFvPZUSe=TURZ㋷~{	ū}P |
| --- | Minor | w6J/(	0ӯo_ڄ1i3桷_笇>x(y.'"鏉:t&Z;A%/4iQ+UvlvȅV㛷&r/;Z.Jv$<%ݱ(ߡ.ߟdy0W |
| --- | Minor | %32%j4:]MGg#TΩ=Ep׃C)2{ST5nduG]qûHfaЧD\	i) |
| --- | Minor | $4+7gY5ދ4.;7vE%Сtp}t+tZ՟b"O_MjWw4!^NN%6<|ai |
| --- | Minor | ;R/HO0 |
| --- | Minor | G-Q |
| --- | Minor | D_x	PMVFcl^ |
| --- | Minor | 	lE}e5PNQ0h6iUC"UgD{TB{JUٝg֑eE<4wFbtȝُMr:?ncGD~X |
| --- | Minor | 0 obj |
| --- | Minor | <</Length1 3352/Length 2202/Filter/FlateDecode>> |
| --- | Minor | {PTŠ".dG+	bJVA5k0_)Ƥ))ij5m'mƦ46L;gLgbå^6f۞3gw9K |
| --- | Minor | 9GtBtRY媪a.zp3W3j7t#g.`WơN~[Dj%^l7~} |
| --- | Minor | FG<I'66T?)ƗSCDRkb=[g7vnI]L>?gcW[3aNͮ5DX?'>yq&&$MYt(2H)Y{<cz/!amMA;(k1?1E99Hd?S2tS%X,	jwǝ |
| --- | Minor | ZДV/:&b+ݬbbAL-L#G0k2/*1чܯ6"بC.[A-vI?mN| ѐvjt*#ǺؾI`ocԜG1>I**4=N |
| --- | Minor |  |
| --- | Minor | ,QQQI)6yki |
| --- | Minor | ?f樬E^h6G?3!WըEw*x;E1g=6/<phQ?@a^j~|B' |
| --- | Minor | nIT,Uv|Q49J4:gB܎ASYY_n=Hʵb\7(ߤ?r{7%%,Zl%g<2>ѫ~egZ$^Y3nmT,uMy:U4h@3^{kDk1_zu7>3DMpw>XaRΨxDuk |
| --- | Minor | .|UB{AM:`ZZ7wLPco=3g^nOӗܸοʴӈ~^V{.sXDD.6M`Qi&E{KW5o[3?bQ^ᾏxoc<^swҔolMK´6Q35Ru߈:cB>6\3;xmzfؾ" |
| --- | Minor | ֳOƯW=r?lQǶ~hZws6 |
| --- | Minor | vno~S8Uffy9|}S|uh]Ϳ|M?㵝EA8R2Wd˫\ŕlҎ˗r .b |
| --- | Minor | ~	Ny |
| --- | Minor | ^e7 |
| --- | Minor | &߸2pv Q0zZ ?/^>/8$yʃ[l߯	^*cG4u/I{v}Iv<HMB. |
| --- | Minor | =8t.phHxqMBz8`Áb{D;N}[{zȞat{<ro |
| --- | Minor | ׵ǃݻrwv_.'vr<Wg'^H@w |
| --- | Minor | <rȧ'c{$In"%˧\ؖb[lx-ˍdtd`c.7E{mKd[K |
| --- | Minor | &ʐnLDP-6e4n5hElT R@x@NXWm`05Pj |
| --- | Minor | *YVF*+bH g^<E̅e)(Umt2JdIKrE	؁"=^%@cxKD\-,^X&iX6,x0E.8)xv30w&s9|^?^zmN|Q8;M`vAEAM[d~/f |
| --- | Minor | q[(˅"I{cOdg*d[V |
| --- | Minor | #4Ytt}QLdӝ-2lŴ,'cj6L.S0N.D{8=&9i25咚M.R.eNnӀ\r/Xdi"@ llc >8Si:a^i@Bp0ڠT(CJ`>euu 2޴ |
| --- | Minor | 0 obj |
| --- | Minor | <</Length 29/Filter/FlateDecode>> |
| --- | Minor | `e0 |
| --- | Minor | (`P "  |
| --- | Minor | 0 obj |
| --- | Minor | <</Length 236/Filter/FlateDecode>> |
| --- | Minor | P=k0+nLh%]<)u:8A-	Y{Zz =ݽMߣW&0鈳_B8ZN |
| --- | Minor | ~58uN8xֶ?h8Y{{ 5FF}^J |
| --- | Minor | _8Kpd] |
| --- | Minor | {MLMd5 4?UKkPGZC1t߼*i |
| --- | Minor | t{G>+̗smHKVj6inq*oy |
| --- | Minor | 0 obj |
| --- | Minor | <</Length1 13984/Length 9417/Filter/FlateDecode>> |
| --- | Minor | `T9evgLle0!@-$HA@"/AK |
| --- | Minor | *ŖEDA@h)mAѪԾRy߹3mm͹s|\B3vBTf 5i_"_6c!n w[о~Ǵ@^BYLrL&hs<<Ӗki>,|_: ~9K#.&/mTTV@;RY1\!cРJxtʅ |
| --- | Minor | wqBhw͛Ӿ~h%,_nʤyYXVI42eWxi2|/AЗҠN߉(ǎ.45WA9 |
| --- | Minor | Q`P5-BZSsЧ1$dQ/|f|.Oܧrz/ߚ#Dω}܎)(n;)8'8F	Ϣ>5M/tw;*_1cI q,Ȋlȅb%$J;5=}4fQl zU|}Q"׫=veˎȉ"/FGuUiDsQ  30d |
| --- | Minor | 5u:ǎ#J}DOA!TkZ0ջQՠuyTl1[oB`BЎR׹THH]Ap> ;!z__W3 |
| --- | Minor | a`fkϻUg#]oM,$;ƏPiಹЌ	=%4<O8chr$xbÏ`HDV,8w3@VhƣIh:@Κ@_t/!` |
| --- | Minor |  3-DKw//|;x6O~!pKR |
| --- | Minor | G:TʂB'.Z(;8\fPFW.oPB80 |
| --- | Minor | 3I ,P."4'\P(PXe1h(#&(^,%@ߣm.@mFh-OQ:Q(N8yݧ ?{Az=N1CV؋,K΅:m4:w \#a	8z?wP+ڌB4A˽^_{ԕi_5o0P?NSIg>@AjT͖S*~!10)u`hw>t\A{	奋{M&z%l8P+3Lh |
| --- | Minor | 1=s,a0{&q|y|,/5=@E&`hwpQ$Q&^~X4qvcFCߴYP-18ހaT3K%Yu%`Feڽ%Rd@F ك@ŞΉ;gaF6?_/92tjN8(;'N7r)sLZ̶u{e+*}Y6-oE׮]1fCf	eٸ{׮ݴU36q"CyVyN阇wER*ʣJ%`y@D( )Ʉg1Wi`tΞ(jZ9Ϝد8Oz |
| --- | Minor | aRO |
| --- | Minor | .L- |
| --- | Minor | <A |
| --- | Minor | 񚹜l׎1\0[]\MF0HS`QhېɀrwWeXfN$b'1袥k^z`׻n	6% |
| --- | Minor | Vhp)7 khco!Iq<׼_y_G蕵LҞa~m[ż?@9wG}q6<u8ˀkr墨E=Zb$nXE |
| --- | Minor | ,Q:s@2h=H:C?z3M(lQ)l+Da9Bx0Yq0 f8' |
| --- | Minor | }Sx |
| --- | Minor | G+73ƉɵFw*hG|	Uckc+"eI1Ax]k][<z%'jZ8ƪ$d$9Eb;3k)M |
| --- | Minor | 9dxUA9'6ڵmǮWF?[GL+WzHxw\tDӧ7e8AeP&|/^^Q,nsX;3QA*ڊSEjULYVB\:#<@  yoفA_]v3pPn^dWy |
| --- | Minor | +Z6nlY	7Wv;y{'"vZ~׮s|w眑>𺃪QuSBy$1	0Y;,	iiS|H~E,a)"M KPW~w	};J4OBx9AT%% ,Ntu |
| --- | Minor | $&g%wPhH#!#gt=Uc[^Ӟ{㲜Z闕[XfJ\|]<g٤)ʫgmIumfjэg-'3WoN*ke&nYǾv=s?[\SVO15x |
| --- | Minor | 3lw"jAr%g13R6ZXF(:=c4a2됤+d2t@bd+8&ūAr+'iT ]XdX |
| --- | Minor | &l2Ll2'~szlԟxI?$(ݽbl?ez?ڻu͜.Xu5UmenhG4,G!"4HYdJ!Q#Q}gKu_$r_pnT }#ݏޘx!~oƶ?~,,ч=_ 'rTy	_=p&8cGy]E긹V\n2Dȳ(" |
| --- | Minor | \*uJ:<:.++7|-p=^{ + |
| --- | Minor | ()ұoR@4lYk3ir]e+Eh$Fgb,%XWlv#u!@8Q\3u@IO?QJKqjAy |
| --- | Minor | "U8<r^<?g'C'PQ6eQ	,AOW+ |
| --- | Minor | dCPfXlXeh74Q-J){<q'')j<(KvevC|F4/`(\*u:aWyQNhQg|CH1x,@Gd%x%^D{$^7YxY^	jXi/w/TR=:7Z4Ҥ؅dbRu>O9tTTC)ΓV8mUGݶܶzlSո)M |
| --- | Minor | O7%n6Ob3͋?^o;3;>X, |
| --- | Minor | \Vk5Zom\U|آkѷ--oK\S|޴4Bnf31uG	lX+o\҉%ܱ/?ƻZ7͇^z'+ξsʗW-q}xzچܡ#NӔOl~9?wk\)09RH0 B 47&hf3Ћ.J~*kJ~g aPBR/Ěq BaD!CDemfT8=o2Z'kWpwjM\mKD~93ҫs9ͮm6wK昶M2}qqțgMȧqU]}3K |
| --- | Minor | #/'Hu˓Oɧ)d;Nt8:697}LC#%ju |
| --- | Minor | ݧo̶Ջf4O܂zɄ{rd|RR>|XGn#ng1?fnn"et|j$_`:_%tk(Z"EmC_Tƾvܱl?VPR޴>bEk!7!/CNr vCvlGBac%~Sh:u>$WT͕(^_φ |
| --- | Minor | ʮAϴt~-z?mӖ[lV]|6νq]ΤTvɷ>? |
| --- | Minor | &І"9؛f7צhC?lҗEiv7nSjuG*DJJIʆ-G&y|9o?QI@ |
| --- | Minor | *vfO=^|f.[׭|Tl+[v {@ҡW_; |
| --- | Minor | Q^N"6kP檗6րӑA' o7gA wXU4|-ji:jd4\!|afxIH@Hv8$s;L)ʥvtt5#9)[<_]M֬~HKW%TE~4_CLd<$5Gljmlv,=t!2PN[u FYի]TtYX| 3*BRʌ!lV~_NjO~>f\:5̲ |
| --- | Minor | *oXYrg-_l |
| --- | Minor | nX4n`"i#-FM2Fy3anއLVE0 άKR,@Ow(#3velG,Żw1pxXIhL߁+ؿOag7Z{g.z3E۫/(nվLw";/;l"gD7>5s#~PKG	Ht9 |
| --- | Minor | .ѣ32G.YU{A~ijkNٓ荰89lwh*=)?9Ó_?)k@]=}/@)eUrӊف# w*^ |
| --- | Minor | ;G |
| --- | Minor | ?f4RAĜ,zf~[V^E~2*(_ZoUv%>AeW5o_UU/nBW4Z,g%a9ˡò&*IV7|5`A4ي|5m}tZWҚ>Cl!rΝ۷ܵz:ו+إ|^eWו+]]_kCQX]ُ9nC).#nmry4I# |
| --- | Minor | >cLHW{b1pHm۴y͛=iNzbU:?j)oݸ]Dքu\G8adj6#αɠm6щ&I~Ƨ\!CJ323I<6,1]rHN)"-#ˌLdVFe#؃=_zKP\ |
| --- | Minor | @B57e⺭2@s<6E~ǔ}b^Wcgv1/PpzQ^<rm>Ǔn[E=tӋӋ£f|>ŗ%}$S-&vgwMܚ;<;;v?>ZN[vv~qy0dIfav3#P{KV<8{-6y캥 |
| --- | Minor | >so/Ͳt? |
| --- | Minor | =ssC>4RvH2X |
| --- | Minor | =A2c	OW!*ASR3^LBjB"r*;'p`$	ILJW%Z!0>OI9=+D?pHff<A9R[vҌ[ls.؉XHR9iZhXwx/n +t{5@dNᕑMIv`!IUks<xS5ُgn>^]wWG/#6{%`aDG<Qh |
| --- | Minor | Fxh/g0FpԌ=hjHk1U3 <4a(FFrv]LDl*MSQ455ޅfJc#-kk |
| --- | Minor | ^hCo(MMq2	Wӛ|PS3r΋pNn]f۵ |
| --- | Minor | :k),avzx׎F#XlVA/Kl1ј |
| --- | Minor | <aM,ڣجɠ׉@O0gUBxzP8)]ԓ~=@2S<(vnkl<L̳ֻ{J6 KDa08EA'yUVb |
| --- | Minor | ;5FZD.BZmI(hx]jN&نx83gsPm8T?02Ěg+Dc-x88iyev'*EL)b"H(iu,3lE1夜-2LS+[KrĴVk⛄fۤmuKFci̼`]f۠]/r,k5y*!!br	K_?hT:w+7o)o,ß<ۍ-	THdϧlV<ҰyYbL6 |
| --- | Minor | (p4%Q{$Qaw>nq;D=Vhbˮ |
| --- | Minor | 8vzAFz |
| --- | Minor | =RD\8cF;4bǢJw	YhPi7FMZFKĹ87nM\:m\.RD]>3&$s+c3yd8B\b4eaYj@U+ |
| --- | Minor |  |
| --- | Minor | S`n-7:FAMMƵ5555wӴWׅaLc޽Y'mTk?bR'*=?Xɬ552%(PFmD.6#7j7:ѶMF |
| --- | Minor | hj |
| --- | Minor | `gɚhFߠVB8HcC(' !𧉳tU 	Rg-BB!HES*Ux9f]JRx0:,13"n_Of3uJX.4ex9s?m&rrCqihnt7F6F%x]j6 |
| --- | Minor | !>wKG5|*d9QHLO%B-Jg:!kPSb~׭ٛֳ	X`$;<ͺHlRh3hnp`y񃎾C	rW	@=<r2fjӯ(9KU<|ZO]8P"(!5kP[IlvkeL>i]vYE:CqQb'D4VPfyFJ		u	{[rj/ |
| --- | Minor | >dÄ9y/inٽy&QS/?H13.hpc^/ݑqiDq($'f}x%,;5Ȣ	!AC.ya#; 6@C'd!^w:bUbJA'[{3xwͷWm |
| --- | Minor | }=}wW0NXD#}g:(F%|sPn@e8k7XیrzJzlh>ۂs<3Z|hӆ&; |
| --- | Minor | *Pr0O. |
| --- | Minor | }eB.ZL4AGώƢua.O!M[|< ;45E8C|IFlVS4U4Ѣ4KRBרs-X	9ZiƉp~mnNȁQ~CU[Ԁ<(̓҃(l	0 |
| --- | Minor | P"?G >j#P-\4\KV<+`L#RDV |
| --- | Minor | b΁Y=0"/0oy`|;G}yT\:Tg	թs`l |
| --- | Minor | ޯ~ß_f~~	Q[$خTKL4 ']&"t'bB*a=A0.*~f#tY%BX	 |
| --- | Minor | 0ӯu9UJN:rLG^}ƽ  yY!GB^T |
| --- | Minor | ;tt%|+yN!蹟=Y<COsO+r#d"ٻ\&	8YQȏE%{۝Hv.#%;aNٹa$;dD,nB=j%GGѣXGDnl=<}D$bZcd:nlP<lxۤJU܆RAfþ'ukܺhdךjXzu9y8<  ȪrnBVJJ FĭiAdH5ze7H(CFC(>/6p |
| --- | Minor | e,ZX-!HmH*FOjdA*qU |
| --- | Minor | \PU#dO$ Tqyv2W!sR6;+SrBJrDrw+)QHh2K!w)d12C!T3@0qE2BI&Ȅr2>NÍAX"qcB0"7EFrkȨ7JFq#%2Br#tDq;|)`ӹdX6|ɗ١"gᆔf.BIRH@VndD.J\@$hIVf5dfعy͈;XŦk˹ğfI f#i2 |
| --- | Minor | ')Y\K">x4$"Roxo!2!^O-%X3 Sl,,k&lt<2veqiHBS!m6^ClV+gZpc5+D4` |
| --- | Minor | bYBtɃk0b+і`46"	8p0&c	LʈO#H!(._C7/v |
| --- | Minor | 0 obj |
| --- | Minor | <</Length 91/Filter/FlateDecode>> |
| --- | Minor |  ,g={B,Q^?*P!Y"rp{-$7tF&fV62 |
| --- | Minor | 0 obj |
| --- | Minor | <</Length 377/Filter/FlateDecode>> |
| --- | Minor | n0E|""<b	!U&>Դ*bR1!}@";10mG^iMkksę.TVSwžxlGe)Oo^Gwgӟ)BΐkEGm~#;MTUP{#xk_$ҠlICBQW%_UDsS>)`LEY |
| --- | Minor | \ K	C 3v3h+Ƌܱc5c |
| --- | Minor | CW%oO$$%>"`WR!sVWXJBhf3=z*TSsiy(f|I}sΏc8a	l--ge臩j  |
| --- | Minor | 0 obj |
| --- | Minor | <</Length1 3560/Length 2307/Filter/FlateDecode>> |
| --- | Minor | @Ix%&$M0X	yYBI,>#H ۸̴ |
| --- | Minor | ֡3Epu` |
| --- | Minor | 3vZ{η,"rq'[^Zv'#%+Uv/ȸre	tqq]+?ey%k |
| --- | Minor | b㪺./mn5/<3DV&M[77,.kqAdb<.ol~ƙMm]bimV)$dz׶Oc14;Fv*D5<mlxp?hSr<R)ud3jH42rSט/$yoVQB[kڮ& |
| --- | Minor | [TAEqd!TeqNgJ?J()	辨11]|MөJs/&(IaztYjP]bHU5+I,H5b尵MMFlF,bQ<&c^b:7kF?:,һL1i=A_Ē |
| --- | Minor | *XO5Hc?*~<wZs*NtIEsE? |
| --- | Minor | !p:V<z^&2:}<F/*g(L{,ab̴V13ZcF6dÑyre5hPx2Sa2\_t |
| --- | Minor | ㏮Nki"K8Fq |
| --- | Minor | #|L0*"ObbKbinE@9lI |
| --- | Minor | {e{n,G!bB^GD |
| --- | Minor | {ﬞ |
| --- | Minor | oTTruDFE/CYײRUV1k 4̝3e|S(ʹRc}6s%e'NɡylkbVl6Ť$e;Yg8(ɋ:.2]IyEw͙82233R,$-es&y[j%+WɘbIS&;IcFA`xw?l۫}/_O"'}e(V~˿:n-5ޙ01z}jm$&Km	n_>qvBdmӈi_*87F	1zlTch2jN3*"VlWA0BɌ[#cxGZ@͜:j&e*4`n-kx.N:jYֳ~.s{WygniR*u[^MM//{Y}uֲuev[k}Oe׺ک冤e/?GPnYo6|IsUڣ[[n:)OqJ'3xy"Kĉ,WwaXGǫ_#嫈:3/%@<@~Oq:^\o|·MvÏ<;QG;4vPJ!M<ÆxLM@&~ӏ˧u<u-xyЍň@<*-?,!}$Vub&0g.=$Ա{W==bNU]yaN#;G9 ch/EO0({t<`[8An#&ʇؚ-&;{cbc*ب+::tl |
| --- | Minor | Bi=mGkKluGġE*5 |
| --- | Minor | ezDcO6VQ |
| --- | Minor | KZ:jȕ5::uYqեqUCX2GŲDYƲD]`i,hM.B?nBje)(]-XP()%k18Z4^9r]Wv,H1wKέƜBBcYYcV-gye |
| --- | Minor | ݟ1KMyv9ȞK01ÃΩOb|9S9!K,}pJdYbdo\ |
| --- | Minor | $&;,&qINLvk"-	)rB%RkJ>uus I-Gn7\QD?	<#'#^q:bj-= lVy`u"d;`g"TCP=ʌlw$ |
| --- | Minor | 0 obj |
| --- | Minor | <</Length 10/Filter/FlateDecode>> |
| --- | Minor | `    |
| --- | Minor | 0 obj |
| --- | Minor | <</Length 229/Filter/FlateDecode>> |
| --- | Minor | Pj0+tlmA0úlcFqNױ	d!ē乽g/Mp3֛|kFdqL6(+S66  "0ܭ_ݜ2R`'zDUk->/;2ޖpad)iÀs(h?_Z>NhXeLDl*|RLEUt |
| --- | Minor | 0 obj |
| --- | Minor | <</Type/XObject/Subtype/Form/FormType 1/BBox[0 0 245.27952 195.76628931]/Matrix[1 |
| --- | Minor | 0 1 0 0]/Resources<</Font 262 0 R/XObject 284 0 R/ExtGState 285 0 R/Pattern 286 0 R/Shading |
| --- | Minor | 0 R/ProcSet[/PDF/Text/ImageB/ImageC/ImageI]>>/Filter/FlateDecode/Length 2312>> |
| --- | Minor | b(VFl<E`/H؞'!o{}%^#b5r?>}4<~_ |
| --- | Minor | |hxwJcKDشzBWze|#WV'[\cQ8>X9L |
| --- | Minor | ]bMar1s4a*Syfr<χ^duNgm6섶3֨5;eYCF %NBRjB=g8T9D,{Ė=U|࿛llFl&h뽵$m9̾ 	Ea3uSo#EîHTȒRfDe7({(E	6%|dFv 9f&l2f1H1 |
| --- | Minor | 1h3 >tddMeIr6eɸ73󮑪C7W* p:/tdFk@b [sӑH[c% |
| --- | Minor | tl& |
| --- | Minor | [ӑBBD&Ԑ588klKN |
| --- | Minor | ~C5kZU,Ε9}Qe&mGF\йLIn*3֬ONѲPN!Q6?ӱBDQShw[CԱBDAc,9,h["BPGfhs@Dtv\$\CPT*<s:M*ֵVz He[Ȍ5+q̜`)\KtgҚ1`:dӲ7$p&&e֎\{L]i`u8 `q౉d@6ǤY@t7עY÷ҍ |
| --- | Minor | Nʻ#E7IjA9UP+\=!okR/'W$!&|p |
| --- | Minor | +#q|p	p |
| --- | Minor | [G娟O;C޹A8U3s|a$Ihc.eR6Es_?U\Jsd]X&WU-,G _o4Sr=W!x3!*Gk祿pH߯wtzl! 6vglG` |
| --- | Minor | [n1hNN |
| --- | Minor | *2s2{LX1ysrAߵg<Ǽ[:o-> |
| --- | Minor | &}vťzSF_<u7{eа'Rnw_ |
| --- | Minor | ՘dM8 Ϟ؍*}t4a|!frYf?oIG6QGEL>ΎfcnUVuC["uCxMqC~ zk-+iwVV=vn[I6Vy]lP7saBm=qaG62fʁ|;z@3Kș7[Y[IZ |
| --- | Minor | 'Ɵ3|36F6/rSJ̟џmXġTXXL܆i)37g#ng#k?&P't+\aÇTT:6UEV7x'+_WKK"h;K}iZggK˧/$qO,{ގ8PZ&-(Jk.ilsFz_RuA\u2W:.kjƾ |
| --- | Minor | {Sg/!'+m:1cITێxi6'$Je~#:@vK8hn |
| --- | Minor | @ p^~)-`eƶ{R[qi:6<j!<] #Gѻ |
| --- | Minor | նf]R,n+z%2R) |
| --- | Minor | )@+4OqFwyn(ώBM}GM7pS#"w	WlSuz~',ql+8|d\oܩ~p0sNs%9B͏j~)Fȹ%M"T{RQ Rl9y˺] |
| --- | Minor | )iY٥7]fgs'?7?F)NETwnY	D$xGXC{3"{^rꔖ"S8&18o53S)\|8۞6{~:^	ۧ*<61Uv{ȡ|9W-xـs։J70 s:p	n; |
| --- | Minor | 0 obj |
| --- | Minor | <</Filter/FlateDecode/Length 3194>> |
| --- | Minor | [Iod |
| --- | Minor | %@(jK>m 29t]s$P\5rH7 |
| --- | Minor | \>ӿO$<Y8Y^g?篧?AI*qh	N^$q ox!P!T!cwGe-͂/M,oӨ2ho{Xhu~Ny9 2GOKN d` |
| --- | Minor | 6 |
| --- | Minor | C0~ӟy'ȓ^8cAC""HD:g̎Rb^OA`EB[j`;:ZG*ְfę4J	~͇ӧ	Ǉ#$Gt82Pmߦyy$U:PJE,3֎.ufY)<QQ4Iuh-S&cTaXT'1!ֺku;XG5BzOq9>ylqKs |
| --- | Minor | &ZlF0O>JQW" |
| --- | Minor | '-{cRj|چj%N91DҊh}kûDZy&_ƫO6} \c;e䙙O] |
| --- | Minor | htwzTv*̥5e0(848hDGިSzu<&m*(!<;wRNⓣ¬dXbW[ۍghbs$:iPѶAs%QizaY|u&K:Yo<"UfnL둦z;3ނgj#!d۬VY)AM8f;Vt($0Cͣ^LB	%(nt!!lPAbM E $ޯ=[!i|uEzKz\tݟ~rO)0tu|l#bc |
| --- | Minor | Ի؀G!6t31F:aP,M5ͯn?E`irdig1|@ZJ<E"p/l@J1*QƆ@ud` |
| --- | Minor | <Uc oF3!SՆt	դj&гv);Y@^L4:[s:i*OF<)k(% gҏΩ	B󘚘QPŠ#WVHgҬsRJ&oUDZ_WdޚY(i՚%tMAٗ啷 ՔY4m:<DSrjOZ#`F٭|H5ai{>vgG1*g揩АG"QAʔ~޻9>%EF |
| --- | Minor | !F;Jx?؉?0H sWiXDoið5T=2sQ=9H~[d+ar)%PfFogԆ<{H%1nT_4v<PbcCxe(cr>ٯ6%)h!8(O*r])Ю6 u-ҸRM%ʤ |
| --- | Minor | bW2ԫ[fhUM-u |
| --- | Minor | ;u]JL\I%Z<38qtwUTaW垆tuoW}xH[݌0cq+c(y\ݪ+u\_Ub7/3]VB9gv/pXll{.$SRu!c	ДKs$/݌	n4#֟Xx+61{JC֓Xv1R@Ǧ(N6łLs91T:= |
| --- | Minor | |j]ꁾ˕H5j:PsjBdj.7RCmi_Cm\בё{N뱎k/u"RE	r%^ѽZGFJ2<-#Fn*hR27rwVX $ |
| --- | Minor | J}fboZU:d!#K,NzG+eGUJA׃.76jRLl{:TdhS.# bO&`u/,O2	(D3*7zo-dy,e{,n҇{J97"ܬeh> 麓.}k&f?H{PsXV+)/+]RycZo#dpH 7lJʧ#W)G>k{y̕;RׂRAmzH|01Ӎ]0n!X(o67b\̛uT3rt̬ɷЎ"pxwrBՈ+͹M	щú? |
| --- | Minor | "vL*'Jʯ%	]nRxK`z |
| --- | Minor | +4z{o/u3:Zm	bJFK} υ5!l6iZhETᴓdv%[l |
| --- | Minor | |kB 3\dMpU%q-+̖fӧܮ(.Atv-Gˁ!RTn3}`-BN2jͽT^[4ւ)&Li7`AvI#ѥ[axM&BLРɗՔy2H뱎n.$*"U(6޿I~ش9dmݯ3~qk+C%o.,0jG2T%M6'&D[uK֔@Q#Ķr͵9(?*1)~%Fի-/*Nzuzimj"+K߿U_4_,b9gIpp23s]y՞K| 7r57@X/"uXCSbhgQ;|L)_ߙi[y%14yܥcT㲋J׉of߶-/"֌j);r|e}R3TAt[u4z)1^+w@p |
| --- | Minor | /ŉ#.Vm>G3]:/7չ閼5D@/8ի@aDB:YݟomF% 'sϕjCsTx"ݱQ1, Jm[cADFÁݥ7_zn`3x+kPx8$WKk*Z󵺑N |
| --- | Minor | |I#ȴT]_۫Qw,uWo]уn |
| --- | Minor | 0 obj |
| --- | Minor | <</Length1 3212/Length 2088/Filter/FlateDecode>> |
| --- | Minor | {PTŀ" |
| --- | Minor | -."bXL%,y+Z<o)3I1mI;MQVvffmtI:-~I4~s~|]R͓ Wid1#%J+VT{ma</Mb)o1>xM][m'MQaWUu=Á,;I׉;o$;uc[7m[wM5׆^ke|g?0mcHzku16m)Ofmse\=YQN-m`6ϑٛX<+OJ%%xj2{F4>~rͭ޸[k)k?1Y9Bsix	nS] !cTWPbI94CS۔<bH*#*dXX;dr"/F'#C(M[FʹvS?K~UDĒi |
| --- | Minor | )YlsF8Nu}~``Ԣ3U |
| --- | Minor | *,~|!0:1,.рQcUt/2WnQRCZie=Zge6eMLͼ\RV |
| --- | Minor | PUY0eX7U#Qu%2cmJP7dyڗb=LYm*P9rmBgB9^נ+ |
| --- | Minor | +Y;=7k{bй;4>^Q%ȵ2eAKMʻ9Uߖ#QKj,bD,fyI0;ŷm#"[5;(mv6{= |
| --- | Minor | +tW?&KT%= |
| --- | Minor | ͒ZZn3y47lntբ{?iQeθ?}/̌cUD_f{193)DG^ɘxg;Rl:e\[h1,]ӳE4#;4y0U~e'^<KJR"/-6R#5Q7L,^T`n[x |
| --- | Minor | }TOF9,-vcZbez^٧[:(\3GXC[آmk9Jeeތ(<wyk-TZY6r8wmlX]wXY\gf>o# |
| --- | Minor | R{;67!tʉkW3fJ5~EM^㢆!?~a=?73?5`|K?GމÅXyA@,~!~q.$0p.}q߇uz%_3.>'OpN.NI |
| --- | Minor | '{E_t=NR O8~#pSؐ<!2qā#WᎰ<<C/CnAÁaj^k{vTnԻBx /OK}x15BK8ӏp/`G<ۇnls`kWn}-)ǋ-)fTtl`SSn2D.:ho[([ж-Յ^]4s4,7hjMh |
| --- | Minor | 4PF |
| --- | Minor | .Y'ks |
| --- | Minor | +wx |a<c2UVQ"^V"ˋb,e}XG)\ԃ	(Q$Elb\AqQ,vHE1У}Oaȕ\PYP77AΫ9n97sܘ,3ghr!wȀ<$YD~^OBy!ۇlM#7![OrOY Ʌe Õϙ$}HOKHc(L&NsKoW4N6͍i"ՁT]LMCJ<crr\d\$qLr!Qdb4Gj4]x<H`an.^\ňǺ8NLSbsZ`G!D2J |
| --- | Minor | [\pPd@RB*Ç |
| --- | Minor | 0 obj |
| --- | Minor | <</Length 13/Filter/FlateDecode>> |
| --- | Minor | `    |
| --- | Minor | 0 obj |
| --- | Minor | <</Length 227/Filter/FlateDecode>> |
| --- | Minor | =k0w |
| --- | Minor | uv*[F63Wv)T`Y#^K_ǎBrs\"8R`󭪷LRZ~3N4+\N~ahǵߞ%o2TۂC/Lz6sy= |
| --- | Minor | ¥͒d,UshBr7j~>U_EQXK@-Tr~ s |
| --- | Minor | 0 obj |
| --- | Minor | <</Length1 15192/Length 10188/Filter/FlateDecode>> |
| --- | Minor | {y|T9ee2efMI2L!UD@J 	d$-	Բ	! hRlq! bd3jq)HjK\h+?J1ysgAlywY|a~X?v\.J>?	Cg5S?xfN}	s1#=P*x./[Ec˖2T-\u Y |
| --- | Minor | .[SV}ֱ%SR<H!4CCJ`^D(	EKVנ/As{a-Bn߷h*vw/8LU5K>=e?Bt?UW\㽈ҊBF/n0MiD)3s~}ȹr䬘d1rS#m)5hBd^!#p˫o'?yh	>o+j/^[~Ah')vO7ޝ{}MW^1?>}CȂȆhP2JA><K5E̽q	jDu%xiAu4Û~eHP*XQ+a%=h@F$"2u |
| --- | Minor | ڄ8Eg݊κu+:h44$FCL	Gɣ;syVZ(]80GO<¢ |
| --- | Minor | ("͂V46yn̍ |
| --- | Minor |  ;әn4ne4C§ |
| --- | Minor | ?^}\j/1Xwsi}=`h3c~lvW0N4Z*{64t:OMUOT7Th!t}< u-:2Ѝ<Z:'1LKi!	xS[e+#,oCB %{>C |
| --- | Minor | A S7J(4)h&Z |
| --- | Minor | C s TY |
| --- | Minor | = |
| --- | Minor | Zw}ｾ}ou%|p73WP_C=W 2U3R,J6Bϓ |
| --- | Minor | PfBzLB(3 |
| --- | Minor |  |
| --- | Minor | P9LJ-A5 m߇T |
| --- | Minor | /P2~UF.pt'<LAax_ V5r!2CAkF+j'Y,[ow<ܣaIB{hjD5`Fa |
| --- | Minor | {t3+>୰SyVIx:)$l]B=V/!|ѻ=Laǻ~4] NP%JT8Sh0a^XcP={(TVTkDSyX~X`smLĢ6yR}?E݆k}}f\^FUml|_ÿ&On;3nlhqcallhTT6<hո'SL#PT"%G|Ga垎 $	I4gxZٙ^aڵ{S< |
| --- | Minor | ^jVXyrvW&\GaKIdaںgݺ=^O+{p~l"+7ˏ^X5g]|,w`s-'A2bja橾m |
| --- | Minor | ~pa=N<1r # |
| --- | Minor | \uN|aYdlV>6&Ԕ쬩S:uh)]d@>bs067ja]b?>@QL"_f]v6pxgir6q%%[G r РR$[֘g1Ǘp |
| --- | Minor | &@A(+pÔmt췂~'if~`Q-j'ȍ h9}'sdzL\f|cñcku]Sda#ʩ e$]ȨGK"g1W_nuvv^eЈج/w:2eggWnK\M6Wk͵q 8#ڬؓ	0d8spBl%A}N^T._߱jvx.];v)7MQG,Kb1i	*N(&w:*6IbydfR g%AiRzbh ``b\zޏon[JU}Hۜ[֭{T_u/y@ٲl}䡍 |
| --- | Minor | x0'HLZEvѡ r5R¨XĨU1f7о'\NW $."P#n[6hLnͼ{rg |
| --- | Minor | $wPRp-vx"fy&Iaj34B*&u?(yL2Cw |
| --- | Minor | _#Ξ/e/"{4ǔ_jksR<V8yqZFz9+tGM4hȸA/A:(BکH4ܦI1[AT!0K3n:)eY#g䍂Qetc13"#v!xtSM*fE7"&9x㬿p>jSۖ |
| --- | Minor | 3_+r?v4馶idb|)Fb#**kc#Jm	nMt6µ	@ |
| --- | Minor | +r"/ |
| --- | Minor | &Egы(&S.I?5=c.f |
| --- | Minor |  qj\?l)PbMGީKyVnP;|}c/RL\8)ɥхpTGx)MG~d |
| --- | Minor | <$+ |
| --- | Minor | ^YWZli%7֯|bqsO\pxWO<Hߵk]mŋlyq`g?@.)9RaX |
| --- | Minor | #>٢xsO%pxQGe)]Xv\n32:ʦ/98Bd* |
| --- | Minor | /b|\$Jwܼy.ɓ$WӣWx6g@JIh4|Sth8W\gʸ𺔬DaB?J"|dtĈAT` fC9݀zP叧&9f,oBzY0Ͳ&s9kHx:;0]D aӁmÛ;L>B~۬>/<煙rS//z` |
| --- | Minor | )SW/qSMum:}ڵ3g9m枞k*ߘ1[ W2%`M}j;my_/gn*]x$2n2`D4*a0dĈ!{E`1zQngxC%u*V4$ |
| --- | Minor | 0[^Ps:s]ZmTUP^+^K |
| --- | Minor | D.O'|b=jpn"!6{'<XضeߪM2Q?Fq-+v%Ω]BCbDcuFƄ(/"naUb ,O,vvF*GͭZ밵:3]ͭQ!t~F%!_Z3YʕLhjRͳJ@vQ |
| --- | Minor | <	Xs]"qc:Nӟ-P;V}8F}H,we*'JQH\ %V-Pԫq%TvW搄t]bѿ'ЂǙtMtgj}H^i4/#juhu:ZÆް[s[<Q**&E%!#v`т= @÷U mb |
| --- | Minor | ;ş2-*eu |
| --- | Minor | #pfUd$aI&IKk+ɝI |
| --- | Minor | ycNLNMOpMtOLity<w'/L]V |
| --- | Minor | "4^Sk |
| --- | Minor | >665-2tLI5NAƅc5Vypj3/m}[?ոbIQ{)/j˅OKV FT/E9-A4Fk |
| --- | Minor | *	ƴ |
| --- | Minor | {oQ!	Lx@HJg(]3D֦ |
| --- | Minor | WDTBם'sieKPnz Wٱo%JTM覄MB]qpȓ9ȫ1aI ݝr/Empl0eR\"d2[xdN;la'',pu`1QuݩxL% nX~IMc^y辀mk?()|q֧_YVWf|e5r5E'%}LXC.Q*/{8\GQPfZz? |
| --- | Minor | ʥwu*"RUjRM4۬ytWv?=DމKmjܺqӶ2N*]T4G~5̜}ex3:Ar) |
| --- | Minor | 7Nݣ&&RaH9'GP39P BM lm_t~]r[Cڹcf'm!!><(/iW_~U!RB+킩 |
| --- | Minor | &/H&2$_9ORX1!-!BLM&dׁ6m޺u3l_u2I*o}'=zЊ"T)Qj7פoB2oF6'Ncr$e6$II))vSY6(rg\O">Ak%׿au}#"T?nXu |
| --- | Minor | ݃)'!DƑZJYSBlZYU"V!#Ȩ?J @0+7PS4V̈ژ(łD /Bi(dEwz.q8I>l[[/Y;sLZuCyeedzCG}ً@uR"&I.*iEkbc;ưE5Sh;E	N!+,95|+6IE_03+"&5ar	#Tzrvy'wސ*\"*r/YIKM7l_)$^'SS]Ɇ&Jv6YYDxO.}tz:)F$|K0|81{ik%\uرiGL	O2uj1^8&H B;  7{tXYY!IoQnE)QKj[PF6ņâU@6ܖKv{|	AہNtp_qH=@Ӯ pNOn	T |
| --- | Minor | );-tm==lɀ ϭBаLgz{Lkae*T3Gf/]~7ʘ~섖e]EfZVU |
| --- | Minor | Yk4k0li%}~s^c!	C |
| --- | Minor | #Z!F4AbdDg*<UѶo̶֮^JEՊo}^z@?n(,@dAM:pⴍU	qRLt@:0To*mVĔl߹sQ_t	;rt`e/˳v]b]#Sѳ۝:cLt[ݺY~!	ZoEȫ]w㔂$pnoim߳I<;UfBiȁXc#C}?=*Ũ#c	qa:SVbR3:҆`"F]|C9BEF$"=Ҳa]OwJH#6)LK6zD'nCܡz@/N^w_:M1X[WB#98&(%cJXFjo$,OV	s#aIE48&Ո|E4aWJ2o76_]|O~ص1kcwvwxv/6JJiH9`=`;v~ D	123n1iIAmwM^Wg2]tu\;_] /w֠T/<ϗ%ӧ395rs>JQZ+$ꛬ |
| --- | Minor | \MاPy'H%hwLϳJ4'p*`S%	tGX"O|e/;a4Qyk/ɱr<I>R[n]sm-9?;R)nuz+FՅ,bf^]4LwƩ@D#̆$;IviAIH%=צX<yyOƓއ̩{z{Ɣ+<s.}c/] XPQ3A/*1Hzb+ f4#^x#Q bi)r<ֱ@tU*x!L |
| --- | Minor | &*JFp6Md.YI6E~qomXJer~jzf>DՃ3u\[/)87-k=cb |
| --- | Minor | Xx/mB[6A5hG\#U*0b%	Pfs8aam*gJ8iuDUgD8lQ`3j=O:Bga@ P?O<Ld*4ST!P<940  |
| --- | Minor | /<l@(1j |
| --- | Minor | 'NIZΩxm.Q5$S#fncmdr#qGxP]Ya"pSF |
| --- | Minor | ]~ظ bZW2+JVܰĸD\bZb]a[ԱԹ4b- lnmo03uu |
| --- | Minor | !33?k»xFٶ+qCf(/Yeex|~ನ@$Ou )0hdh4h5`4ZtU#*`g 1a6z5O:-l~,4 TF|	8e O;V""$1יF_EOEU|K |
| --- | Minor | %*Z,g0wqӸiafA^	r.ZRRqisYĲD 1u>)?57i#PW>?p/5浃̕wƷAuL |
| --- | Minor | @1Z_*7|Cv2~Lzv||<m&lR([a |
| --- | Minor | `,f⚆moaKᛞ_˿r1槐dfdc}R@,2rtO73{wDDd%@X2l(2nC(0~,Wܭd}}|2d2hN7ȗ2k`2DȀ,X<y#<)QNUuqXsmg2DF38J9oP5% |
| --- | Minor | ]ϑoO^9!vt!3}ڂ3r̛RR_h*Yu(@J$DpNb&Wu:٪#`j}HL7 |
| --- | Minor | sG[I!ycI-ƥUƵƱ7XŊ~dCM̼I޿)j7_HYwm]pa^8: (t*NC65}U#7Bqgu^n9h~龜$#+8)n<{SkW;zmM|LRE* |
| --- | Minor | `3m}@` |
| --- | Minor |  wZ4Y2yepA))A EV*TU^_ rZINB4 7gDQR<0dieIp|]Z9~ |
| --- | Minor | 4ujb7t y z?*)]E^~"g:nyG=ǘ?ȥR>|~_~;LHy	(9???С,.FE]I([(8;ZPy(<Mqo]]kD4(| |
| --- | Minor | {-`I4IP;EsЎ@5$ |
| --- | Minor | ,vM5!Pjn.L#Ƭ`Qe	ʷW*9w|[ry5s?BMإUzuw5wjkн_!ks^\/O1Ub`̲ Hw4QK[Dw })7,-m4xMd0&my1UZt*E%W!v Ýy0ÍFÜ%}`t"ZӠ5 |
| --- | Minor | .woԠ*f0c>̝,TfMw* |
| --- | Minor | ̃uKaޯ}*~eR08Je n~[ |
| --- | Minor | ;hN1X$P:آ,kHx?MAwiNtICw{ %汀U$:X#,]\Ǆ걡z\ |
| --- | Minor | ֣3B`ڙo |
| --- | Minor | #{.q5=9}˝."d9ӒZV yJ%ɋ2yA&drm<wiOU9<k qX~m<MSOqO"D<i]ZIdHK#룹fj*]nw<v.	/Cb'd#n[<yd{Biǒfnp[dk;FDvl96U⚎h&Yb8lx$pه7s%v!_gG}'>v_Ca-Y]TĭIC58@VRo$u;HАkdHn,$K%ѤF&ɤJUˤJO$rYh$,I*u\H*V:R.ee5RZr+I()Y.\-, %vA<)IHQo#d2W&sҸBI#ʤ@&L&w"2Kf2u%Ed 0rV;d(i4%7q ȍ\3hq2v[Nƌ12z-Q%H3vl*7v2"ʍLrk+ɑ2, |
| --- | Minor | + CM\5,="V.S&3,`+h	Rs |
| --- | Minor | 3HM,IOq$$l$m5.Rw_M&)DHl2\D\(%*Lx}8_@b\ŚIƨy |
| --- | Minor | }uf.qf5$ZbbID9gpaSLDbZ9[9Z,Jk33%& I&"Thb;dD/:h |
| --- | Minor | ""LJ ǯ"e4 H&i)^5 M |
| --- | Minor | 0 obj |
| --- | Minor | <</Length 101/Filter/FlateDecode>> |
| --- | Minor | PCO( "3"yG.Ӧ2vK͙.W|m_}R<((%7my2Ly/ |
| --- | Minor | 0 obj |
| --- | Minor | <</Length 374/Filter/FlateDecode>> |
| --- | Minor | Sn0>@n$T}(b/R1Ȑ_1 	F3;ux.^݌,4,idu{IFFQT#GWUsq9 |
| --- | Minor | 0 obj |
| --- | Minor | <</Length1 3540/Length 2285/Filter/FlateDecode>> |
| --- | Minor | {pTݳlv7X]		%D4X#	<ؼ$D.Fyh# (̴ |
| --- | Minor | >l4 |
| --- | Minor | Z83)Nk:zބٞo9;|qI""w |
| --- | Minor | *&s$etRE努e1UT.11.dբ3*/S)Dk"ی?f\];<)S~r5uE(D3c{Sy.dN",bb<{sb5Gm㱉Omu#J26^0wƗ9HGW)Qv!ic/ Vvmde'Q*s^F |
| --- | Minor | olM |
| --- | Minor | 4fu7ݲLJ*S{P5.*vKcj&9o}8O%}p-^.$qqәJWHI(Q"d٬6!i7EUX\qFؗJdF,f$Q<&7dc^c֣{zsGd.>;-0m]͔Q]aC,֓ |
| --- | Minor | Yq?7Ip^~dT2WiZ TLh>F/XZIJzޕ~2K&4֋&}L |
| --- | Minor | \)|KET+aIa)ˤ2s}kmlt^_dIǈq|η3]ğl䏏FSZb,qQZųYҨXl?-.rRP KsdPL۵r}8_*c-jeX11ş '{ie/fy٘2UU3k ,̝3e%|SiI˵ONNnIn)^%b~\%Oeϒ)]_	6+:9_u] |
| --- | Minor | @ƒVUG9j:V辣p4LVtgNIӒaA`{(vķ,_-ݢ^_mǳOXRٛ7V^{4?m(u]b?)j^;?9~vyK6[wg>.MM(i0kڍ&B4%5 Jw8_9v/Q2Qؙ? W&xMk:(B[6pͯLY<()z]uRQet1~.s%[zWxl`Ci2a |
| --- | Minor | ֭c/Myÿsawؾ֙s_SeF.eja!bY+уT%[Vdl7oo+xfP.Fǯ8wv89M9;r3Yda%WUZ g:^S?#/*K:NGC/:qj.N|?d '^:^>xޏ6w9⸎g3i8#Nqԏ#wĉ#4>^ω>MO=/axҏÇ%MWCH[r#*Gn<)?طF¾^e[]n;Ge;9ǣ$7:nuS=:жD[lÃ=>ulJ=>lJE7uKGب#@DS:ho[ [ж -vBkbG9d:64 |
| --- | Minor | jD{FhA4J |
| --- | Minor |  |
| --- | Minor | +ju:jtܿߊ>kP:aV72X^bYxU,â *^Al)([e-XX(-I.h$Z<4U]}X`~*/E6QXSa^G̫AQ[yPܮ`* |
| --- | Minor | \M/6Fx%2&d |
| --- | Minor | +6^%'>$r=GK11GMͩa|139!K7HUdL25e|bZ |
| --- | Minor | |nKoX`nd*6kJZ&R1u)UHa)H1N1Ʌ$UI-P^P5녇<Cpsy:\<J'sNvHCS:$h--qnaUE% |
| --- | Minor | " )9` |
| --- | Minor | H4(v6_'_Mد |
| --- | Minor | 0 obj |
| --- | Minor | <</Type/ObjStm/N 200/First 1844/Filter/FlateDecode/Length 5219>> |
| --- | Minor | \[sƒ~_Ǥ<T|Y$d,!}Mʦb v΃!.==}Ѫ62ж!VB;wЩc+,0P*htX[(Ta\|*T JR/[ |
| --- | Minor | /, ؔ |
| --- | Minor | |,NߡkipEW |
| --- | Minor | H),w (F ]pZXx	 @_xRz |
| --- | Minor | B9@T 5'SH.- A@!J[ kx R-@!#G2H]x]uԫPĀ.A, |
| --- | Minor | G|", |
| --- | Minor | لoOĮr%L$SqRGഒZ90\)_*>Khi<P2Z`ʽ.@!&(ͧQ&eJ+,n:b؊,AD;Ӕ(U"+CH.-|X |
| --- | Minor | R''~CĔ |
| --- | Minor | -NGzbٳIc|9&Z\d@ZG@>		} ١bTV2OF4 |
| --- | Minor | ¨8jRY ¨HS'2.	L$a|. x/8zOQrs5)bKq,TRs,,Zc|OU@@p|N(#[|#0Ek4p&c M5/&]@Ps|*8>)ɱgg4 |
| --- | Minor | *bE] |
| --- | Minor | {	Zj9%c8pF1{E/<8Cli@g |
| --- | Minor | =OjE002< 9ⷤŷJ&x!FJOS~/ӆh4L <cDca49QAK; iFBnטiC$"U25I2HW"${IAcc-IZ{ȩìLa^h]pliыl6_߼ZNggb,aTdB7U%ޖsHYVOtfѳt5	˱/d 4fk(L"KH	M匨Y6a0x'R% OA24< |
| --- | Minor | Kc=O)bq ~p`Yg  |
| --- | Minor | ySW;$JDZ3eDֆ |
| --- | Minor | `(X5)`@'|!	AUy󪚽.hNӭ:OCEKC!pSj$EU.Oo%'AGG{F1g ~a}B.U5kR}Kq9{kF |
| --- | Minor | sgϽ |
| --- | Minor | >[NLnٯ[$Е\uNIvݤ&i1?}^ƣ^TV'W˃#2-AkaNSF$	TtXRLpMKxkPHq`br1N ODE!ZAo$.nj.բ$[ՅM_qUJH$EK+Aeo(}z!Yvz-]W7W |
| --- | Minor | ۠B~8x/]a?C=p].)̐|+`>Ƹq c5Tb84Z2mW>1H	b 0LpBI$k:rпa%`Ybs2p畹vb-:X|鯾:*֤#Ǹ3)qaҠaoaJ'=kB]O4LоSCuyd8R>=t ?<75 mj*)lgXR:1m>Gf@\*! P%@|*H!c́7M |
| --- | Minor | s=aiyqQ؀pV܎N=˝PXs`p&<V[De8\`VI8.5v@*'|gkR+a6aHD0Ah*$|>$>eF(5o;,bab)+jn@_L/vez{1o \n ol<()ao*THQ.Ϋ)_tEZDiRL7(Y`ZRy#|^"0 訆ABk |
| --- | Minor | = |
| --- | Minor | &X0laa;q|vvU/;E5K(jK̵[z bVcV4(	fb#n`P:YΪK(j[`]"x:zx<`ukfޔWU\MbDJNu@8SiCk_1~CLY6:'hIQ/ |
| --- | Minor | ;tB{ЋrRT嬼|.[Na,11!1`WlA1{msm5)#M6t|uYHĚP%t]զ+/BWfgwNۚk^ufQ	XcE`%nV]ed# [8+V#pL]@oWc9 9>%Y0l-rVsmf!4{ӆro^.u*7=j?}_MydU^NOG'H>^g,+Isɰ򴚭ӈ}O?zX^PM/Vi}ߟ_V|U]ĕNWekJ>-:=[]bIJc$0v)Ncd3̍<|@*?}x%pz2{=GϪrxѿ()yra/+Z/T%ͯ-x15;c;π֨AkV+>^U-ы/)ޯXu} Ay?ApkvCI))FMN&֌Ya{B7qz/|_M"h=a4FN7f#.n$ |
| --- | Minor | υ|cݦ{ |
| --- | Minor | ~Q묆Ҋey5nClFqy)&RRȼehQܽhg[V. |
| --- | Minor | t	)SMxp2tNK&jecBLU |
| --- | Minor | jX6⾶~̩7.W֩| BcKmԗ{ܗXkݲ9ȚSiy&A}yWh;7СU<>X؍6OzkY/y5czntwLV	ܟθ"}r'H+J>o-vm!wk\Yo->lL-Z(W$iUW |
| --- | Minor | U;O츑om~cGluEkS/zö6-ljsqs._	Ԡb	\4 |
| --- | Minor | J( .pNciA-èc3Gjnh9[5p|3xD4{9wd8q^F\`O'#!Z?Ю&-	SJ`-)ϗ,ElGZai[K~Z^vZک;YSs< 8z2#dnա&n [h{- ڝ:e`rŒNҮ̉31s1@Px0zBx/s񖡚i $F	˚ERg})0{.euQzwD:8UK1ڌv3Y |
| --- | Minor | /mö4s$)EMBBD&}%C59En#/T1LBG7 c%,O%io=1rwWuf̧T	Fu5/76!m{ר09wth9W\0^5ႚn]WԴG᯿?^">`ŭ"ŁۋE |
| --- | Minor | {F& E#PDi9AS#:17b~ ;w]w&=tޞ 4XFvʝq!.ty].)4%)$@7M!A> |
| --- | Minor |  3he@]OrB|AZgXu.ln-"'6`wVRk;P|p]^z'[~01@͘(fŜ7Lϯ[8xNn١N=??{ϓǃ_qYobZܻF#-hŽ>i˯e |
| --- | Minor | .Gy; |
| --- | Minor | $-;]GOqNjf:EnϘe8l®p |
| --- | Minor | {x+Y3V150$Y!c+Dtغ7Ox[cޙ]Ǟ5Qn1ZHk6@¦-*2e>{ӍfGs!IJ<%m9VH݀ |
| --- | Minor | <Ouv?5b<~s@/˾ힷ*%$ |
| --- | Minor | \r^tf``JyȩCjؽo/_|5uh&#};#}}'#uK |
| --- | Minor | ͽ^w}& ύcY:qh_ßALd |
| --- | Minor | 0 obj |
| --- | Minor | <</Length 10/Filter/FlateDecode>> |
| --- | Minor | `    |
| --- | Minor | 0 obj |
| --- | Minor | <</Length 228/Filter/FlateDecode>> |
| --- | Minor | P1n0 |
| --- | Minor | (ɐP&ELEY$ߗ-8Rڗ60Nq&z]}ͨ,)EӀ|gpʴ Y$N)}!N({GY2e/$C%-NI$͎CA8`wUx4hXeLDl*|RLEUjtI |
| --- | Minor | 0 obj |
| --- | Minor | <</Type/XObject/Subtype/Form/FormType 1/BBox[0 0 245.27952 248.87952]/Matrix[1 0 |
| --- | Minor | 1 0 0]/Resources<</Font 299 0 R/XObject 322 0 R/ExtGState 323 0 R/Pattern 324 0 R/Shading |
| --- | Minor | 0 R/ProcSet[/PDF/Text/ImageB/ImageC/ImageI]>>/Filter/FlateDecode/Length 2291>> |
| --- | Minor | GA%'R#V#ұ)N}^ vSUTt̻oͫSCGܵ[jxo:!9ӺxbU̿!Y>i7W/y4A+<,+RZR$Gln%~iǊ)=3S}mkjb_X.ewZGXJ9(gӾ2D߶GlҔ1\=QTZMQՉ*KxD&70'K`< `wd$Y:xKd\rJx]X%|z#m:{ޤ&oџ/"ƋG:ai%W_F7>*h#$ .InVe4)6۴%Yy+/p3pFlyIthIDGT |
| --- | Minor | &[9Z:zr |
| --- | Minor | En*=_{ٞ+w^%]df)ͫE#;XS`g`!;ܿe}k8`5=v._"Ed=v.3A!7`ҿb-q2(c4\?&t*Y}꺹zMmh9} |
| --- | Minor | '?:Cm1|]}Ԙ0<N%9¼tVl+ߛ`9KY؇OM, Q!yAL36 |
| --- | Minor | +,`^769؉LFU;1U5oa&f^Zg(f^xRzՌ0_~GI|e |
| --- | Minor | .p,>JÉ	!uE#޾Xab7Ι?u4{J@~cq'SD!FT%d@bY |
| --- | Minor | =h L߳B5ʀ (	Ut`duVZgy44y~іj4T??WV(NNUSp8g'nEO~)܎hйpJ6nq |
| --- | Minor | ۩Uox(z7Ӿq[FQ+OA[M}5,a,v^2~:8u.	KB^-$e(e鄽`Q\YEy`&)s` |
| --- | Minor | )l0zV+ʂyDґ,7Qƴ}b;|0/Mxj^iGk"Iqsm"˙gE[/:6^.ƨj\혍g>S0瓕7`wcۺsibƬ;QkFcIH}~!`D=T}ĨƧN!n:eBK]ӓ>ɭ8O1KyUS>g \C0iT7ezdt.<JCjxFJNب`ƜPNoJ;5'"0 |
| --- | Minor | )$va^W˃1)TGۻ'"n	mdTJcJƙ;>eV9fJHOa{*4{Wx̂qL:'tၶp壍c,$PP {.a*1TGЦ ك**1h#WecyE~]xL1,:4vސ7;Ȣ-0|L&up@(Ì}B NQ{&upD-D9ﬁI?zl&vpD-D4:L;E4^:%?9ߡ]V;rFt 	CSu |
| --- | Minor | n-w!`+kƪd5OxT܍θX3<PQ!qG|qVri_.J6. |
| --- | Minor | o*o61asl,0{NG1 |
| --- | Minor | ]44_zGQMY\$2)9(5tLAN:ߡ>'&=ڒ@?˭qxb}|e9_?QR&`3x6ݩw>wsZRy{=ϻgXG,.wR3=14oFjL,=jWKAzy	㭋,|I^J	Z3X/(mɵ8̠3 uʏl#FHԍTzkt4bn5H'* |
| --- | Minor | 0 obj |
| --- | Minor | <</Filter/FlateDecode/Length 1628>> |
| --- | Minor | 5+Ʊ |
| --- | Minor | 	N{;;?vGQHd5ۮW;,a&-ϟx#~^~x\޽7! \ xAktg|u/Oa:|ʢ󴜬WZ@}9 _ͳ`y4JO<|weKZGbd&_oksxj['gU)3E[pل7:sot |
| --- | Minor | av&*;6+VvmrʡۙGT}oVQn+$oqg1<ס54ZA _oˇIB,cš2h$^3N|dፌ1YjzS$L |
| --- | Minor | m$,p[?oZ-$$ |
| --- | Minor | ipʗ! |
| --- | Minor | hp?rp>nN׶vqQM>1ju< |
| --- | Minor | *Xرg/s |
| --- | Minor | ^i%)]~j <<0uqo{vi/ɡ.MP}(yRZO\j!uZsi0?;ͥOCNfӭׅ{D231GR<\nT^hes?1;.Op\ͬ$߆ҵq.!/68Ӆ9]A!lIVet]eL~Ќ~M:1(2	9 lȒOvo^u֎|G'vK1 	wQ	F ZBL7YQ]]l}D"<2iQ|750{*SjWAJB_qJzt1ͅT\@AܡB5<L߫G=c2bzfh7xfco~#Re-yBďm#_FWݫ|Wlx$9#Ro	Sg:ۉ.J[m|Lk cCZH\ovׇZJ˰6=BDd |
| --- | Minor | =)CQ]seٖUXҵ |
| --- | Minor | {ѺJS6 ƇWu&N6 |
| --- | Minor | +3*;6ǘUͶAph u/<Lo |
| --- | Minor | =9˝X;tpacipV[9W)gvXMT(Z3pIN |
| --- | Minor | }Mh>t)haOIjf>0-,끖,c.1_)ii}o STLm`3}Sa?[6tb c,o̕TOJFxLs)N/X{$hݿ9NM"0mT6Kݔ9UdI|[Q뾴S1KkQ~`}[Z^q-k+EVv.FL/_a/a |
| --- | Minor | )e-(ݯjgY)BH}t7NHA(z&P=gmٓF2jSԵk9JQRVo#aע7~<tZѭnIiĕ)˪;3pinqCՓ]	n.=*՜䰰`c.s9C |
| --- | Minor | 0 obj |
| --- | Minor | <</Filter/FlateDecode/Length 4145>> |
| --- | Minor | \Ks$ |
| --- | Minor | [ JfuHQ\[*rU*Nŧd7ye{KCI>| uO*''/?g?į?SĂӧF	hSDO~QAį)5~ ~gNmϱ |
| --- | Minor | <?ѹ>ORKt{j!}P9I5^鯧?}k'>/Ş)>B[ǣ]o8o(s'LWԋrX&IpnDSǳÐZ}kg8i~I.I3$eCm^ί/"\/' |
| --- | Minor | ܆,oM"CZciOn?5n=J2yMƪO0[pZpX+++%6&kZXazeԥD	Iq~pJ<?M%T<}_U>k9ۢ |
| --- | Minor | }#bmSC|Y&5)ԣХl[ |
| --- | Minor | #i'Mǃ́VxDD>8ߧNfĺLiECЦU. |
| --- | Minor | ,Gwi |
| --- | Minor | vwnx|̵6qLAi.2v#h x5K!y䆆Q7&P7ވbkmlnB%A(t:!\JOҮ'ˌ7p>:օmmF:iKkaWhmr^xMho&Ml0U(e7Z*0j zshg8{3YM{?kB<8Uu̓zOΦ3Yd.uEE[yp ,%&)ZsjR<%Bm˓ԶAz_o/*f4ܺSǴ|D/f	NޓX݆78+OuqokCp?,ƍ8ck-C4z1XE%?Y[Ejop.PqL6 MS.*65nmĤz?ecVst[D vuKެtF|9*" BI,$81 ]OGUBUQLf} |
| --- | Minor | Ĺ̡̣Q)vAT೑4zS!DUF@Oc9T3&ԣ8l^f-b59>^iki陧ͬ"ZΪGX& Lqo>|OX4-GOIrڷ?[и]+plF<Kſ\ |
| --- | Minor | $*e^Z8՚y05zt+tv`~ gWZF#${9^."esC`~ɝ!mzb6Fkpd9hشfFїz|POL#	q	}{MdP놥d>`.#ʔI«`>L~N&eWGNYN#gn"4	2ۧUfpNuopO<WPzrئ޼z]O,ubT%ʄ̲zc^",' :"<0M=M{y&:a\jB؈ͬ$crb8LQLi;'^nf	'6Heئ7pvQ-9qE 6Ж2W,!?BJ~F56γ0njȱiبH%yynNDآŴyQe"?H[~H~ǂ4bD݉DjF);is5/{%r4Q@y*U<iĎ`B_jSKgv)l@Ĥ08E |
| --- | Minor | (3Rtvh=ERP<F;S" |
| --- | Minor | ܺ1Pœ |
| --- | Minor | jb=S$ZLq| |
| --- | Minor | \ 7Z |
| --- | Minor | #{#cqE5,8{&0IkQlJ`k<<WV6z<Z^d`:䩍fJP2+O5f78h.,'hb&g2Ḩu{](}{N4,ߜ_MKÄho1 |
| --- | Minor | S3_J;iRNS |
| --- | Minor | N	 k&J9d&	Ou>1dy^j |
| --- | Minor | {fSKWYdqڹc|ZYQ6EF/)FfLPIŀڬNMT |
| --- | Minor | (8䗥C[9l{rpQfv➴5پdJs i\l|dj/Eu9'X)@лx]ծ-0H6f鬿0ޕG|m|lGeꛚ֚$*]2zz{Tt^;|ijgfhYV8w35P!➌~r[ |
| --- | Minor | GbmacO`Թ^s(*kM6=k&ÙϷ-2l ^?eWuh_&$-Jiti	cvޞ:Rj[?^$켁2ՑaAŊjRu(-;Tx<,!"%wK_1v/]MS-x |
| --- | Minor | ie@?xsP)Yt)eve\?kk\ѭ2cIH.)ݵDCu@2Ze)V;E*k^俢Vjlܯ90̃*%_20;T[2 |
| --- | Minor | G:[6/YSʏ6(;Q)Y |
| --- | Minor | #8@82?ě+<d-+ّUFp9 |
| --- | Minor | |q)ڷۏfiءI<DOI唊Z^83>]} ZQ<ވ£`E=4Q/ޅFrگGm:ǽCءm&WyŬC7IP\f5O^?5pk5˵_xb&B`= |
| --- | Minor | 7IXu"ʇpn0GV$7De>s"mWxXmags$|3X8pt{ |h~9m@hx~UV/+'gÏ"R(&f>렷cPR |
| --- | Minor | /mk/2JH0V8Ve=dӅ]\O'p2eq/	soϏلUdw÷zÕ]<xÍ ?Qg5(j<S |
| --- | Minor | .q |
| --- | Minor | )]H2i7v|^tD_:-Ǝvׯ47zțrCt^ӠLݣ5̜֯n-\z(4\Ly9ׯ(GjyTjOLz2xʭ@a@eCWڎ&?mh̼Gњ	R]g-\[`T%vxo~Hp:`_CA	j&eޓ΃ugRk/eHWilcɆNɥDܓv+[B<Ԇs9~SR©|3I |
| --- | Minor | =@iͺgoqÆRD^C̎C~g7yiv#壻G%+ZF^#cn\Y&/ⵈSX%01c H| |
| --- | Minor | {tU%~"ə@!96EnDQyjۡMHSF]+(|o<CHe] |
| --- | Minor | {$ |
| --- | Minor | +i'_ovA8\9*E.g6RZ0o	R挖/r_(!#GqFQጎycrc37]i2S2!++x,x2#IЊLх:*ۑj$RY@:(?3?GӲ~Q?!`M;46X}_KicBNn~wޅJ\Q2Nl!A*sD DH |
| --- | Minor | 0 obj |
| --- | Minor | <</Filter/FlateDecode/Length 4826>> |
| --- | Minor | ˎl7qWiМ.?3 A,n !!(lIf$2g}''NN->t_~R=>^9͓_#8L؂8Q	ѡ	asyRBwUO9K=8~Tlآ.m8>S~O喴AAsnGIS$ |`۷O ;[},yKp8#\zFڍ p[.K%lx*_qP;[vZ*#L=U=PTPti:lݘh	(/zh4O/?׭~rE νOc&#t_b:đyz4B}DP{`$*(LRԃ=E6u=+mxBP]f8^	Nc$Pe܂ |
| --- | Minor | qy*xT'ӵ |
| --- | Minor | (g"@B廊>>!gzJw2#nj&. o`>lErX1z3;]ZTJC'fT&e=XX2Smta`Q<_JyՐ w٘DFdFa$SJy{%i˾<E#oTa7dŌ32[.ڹ	7QlOT#iؤB |
| --- | Minor | .)ܹ8DcjuԳ^^AW.$!iGvgPg'E 6# |
| --- | Minor | "6a3!Fx[.A|ߴmAti |
| --- | Minor | \4}2ybl6/_6"pЋ@tzq60љ |
| --- | Minor | HБB[M㏙~KHLÍGy8rAP9xK9WGVVb}$}EpGFE֤WqJ5\ݜz=k+[od |
| --- | Minor | iҏə=>/hLyaT1P|	@}r^Ь[М!Uu&w{.>[a6H8`kD/A6+]-V[}Z&jrg.unB: _(Pt'蠻o۪evզ'Bb |
| --- | Minor | [l[O"/ʡ.M͜ |
| --- | Minor | ~LaL'B	9fg֒A]BPQ5H-\ؓJH|cObj$pqAΪi[OQ4dd3y:՟ |
| --- | Minor | ~uaw7R̠ؿU17/Q۟xSKxdɚP0cZH L&lVeSWMVw Wrs!Z4rLEVYV}dI`HİJ/H?l[CZ*mhta7on\7jHҷq |
| --- | Minor | "3M*sQo^řOf4ѾF |
| --- | Minor | }A |
| --- | Minor | ]{JlV},釅&wV |
| --- | Minor | (%|="qrSx#ӮS&ĉ˅s̿yYkP 7~/g |
| --- | Minor | [R^G[#tXpwߊ'(S |
| --- | Minor | (]AXjWJnܘ涅ΪZ&soA62:8oEXt8}KSƓ	GKP<0VL[VmHZ,H~YvdWv1U6OJTz<y0/&tYHm4agW۔JPNɝ9<br7zK7\R~yQ76۱&s:rҷ>/,?E[^4@)ϧ؇GK;eN1yQE:4p/CD(mPվx\HsITΩ545΃BnC4+A U)7$ii |
| --- | Minor | BAM>Ǭ@v? =-#~4+F6'1Xk>x@hu֞yTJdah<#z)1g73$j`倬P[:0L'GU_ ג~U͈%`S#Sc2i	t5?fꏰ+@I.䁲lx ^h@5*YJ&p)nsR;82ifQOCVdV`JgݙC~ǧ栣MqOqq:GGY7z<xQ2}Ƀ="y4tqdSo^:HG,okh!$|fl7;mr*g@u	f"|a`Am^m ԐC)ҡjr |
| --- | Minor |  IɣcF? |
| --- | Minor | 	J-LW` |
| --- | Minor | /]X?_777L/@K9TFÇF |
| --- | Minor | %l=/4%=܍J7(,,}(	$Bjye0mM_ԣ9]L͢#h%ƴܒJ3NeЌ{f_繂WD'v*)^uFq@@" |
| --- | Minor | ^y+}+^H))ATrtV7C?M{eh'&	JKt`pJ6+-2Z+/d?fJrKﱧ12m/p׾b%r~_U`uIn;WĜUWF@);E"oVы]?Av,7?Bu]e3Jy<3}ˢ}@$aRa0kJu1g׌P`)	-r a=	0Wδ?rv~}Gֹ4mWPlHZf;k*h7}4k |
| --- | Minor | *g.!dD#y9+Þ9Q[SP=|R؞㔟WLTw !굪Oi\U\Jl<_h&ҋ#|LDASe?K2Oq˵`*#GTDBώD%c<{O"TC'Emi^zcd4 vFƬ),R[ԏYB䳖PQk|1Yp"1_ī*eJasǂ⩤iWM%VrE`+} |
| --- | Minor | "G7mW05%RRKdn^枓TRsM"熚.Roؚ³hx8j͋K.W>'TNCxSUWY |
| --- | Minor | *7YL5N2{= |
| --- | Minor | ,\AkċO |
| --- | Minor | u1	[޽p=!{b5sF$:lj9ם=D~VsǞ|t4nק1>U,Ep_^6-hF'Yysak]َёJW5psƳg4y-TKΠU셄>]f. |
| --- | Minor | ̾ +\WbK)ܣz[t>	0^YZ#z~Ԅ^Շd,YK?BwE>S̞{,yK|ՈtU	@Ku\4]zЛiܖu= |
| --- | Minor | H^m 	dnxOYȩR%^o|ܼB7PscU)TIJ9i?\v |
| --- | Minor | ba`ՆFGǕz7uкW½kLV윤7 |
| --- | Minor | ֧Fa:7^wx%Rw[BY+{m|͌*\ԱZRD̓H @S.ȝWL\c'E)#T_\/ޝKiۣDdxJ*c:2 a&ce`⡰Y(vQ#0$ g1}=MEcO~ |
| --- | Minor | wBXZEoǊfo-x?2wnPz|?2jͪu:D+l<VT/y,*m}a~_yk |
| --- | Minor | @OqZQ	M/eoF9쑹>-qdည?9ýbNUv$65dn*W*cKu* A[hhA)|12;cy4af(̐2(L{ά/"wWK	T)?GYTit11fD+CvSVN8roUrvu) IС\EJxGa.CjG^Gz>(wMm}iR1_MHo=jaCCW[& |
| --- | Minor | 0 obj |
| --- | Minor | <</Filter/FlateDecode/Length 5317>> |
| --- | Minor | Kl9 |
| --- | Minor | +z3:$v@btwb4ˉ:U |
| --- | Minor | $]<g;"?bJ˗g	?{_VoE8!rǫƅ |
| --- | Minor | }?~J!owx7	e,eֆZ}&D~osZbiWޗ	O6U)?}b/^Fė|~׋@xoUԟW-K}.k}-oiVR8{Vbi!\6PAml[^k}T瞷]))-`}X<V檹j0 |
| --- | Minor | )}1< |
| --- | Minor | ߮Ӈ(̃S*O߮G&݁PiKɾ= \-g1i^!Kz#Ll̓Z+C+VI5CA#Rݺ_p(fݙd3ʨ |
| --- | Minor | ?4C{upc?	I |
| --- | Minor | @$I믂XIl Vm]'Qy(z |
| --- | Minor | <y豶+h^)!jӖ$YT\h-AVL,?6 |
| --- | Minor | Uԩ '5_׳a |
| --- | Minor | \PLUYkwsuح<P:C%w{Q`Xl |
| --- | Minor | (JӔ5*>2@@MBVe&߈+`)+aZ |
| --- | Minor | #I\ڴ7T컺 |
| --- | Minor | Am[?::≯/7c/hжQӱױDc$#{墨vL/u;v;qk:ʤp\<ݢve&/ƙ ^8q`Hp^ |
| --- | Minor | (<V$) |
| --- | Minor | )l}# )aMBA_^/[mj9˗r+)]T |
| --- | Minor | NF[PK'[{EAQqOvh8D.SU`a=?m&=4tE	2EiLb=HN,=1R*fCwkS;gAww~dXˁFC:n]i	^A%@NCvʺk,Jmy[0xݦsrPm͈,5"Id|GW]73bݡ\45%ѾUx)ubn2$jmyOTmUHY::Y80~GRgGxDm4nόji)#Tu3yA()lVRQjV`Sn}$ک.+"2WrPW^rǞ7=VitaĠso0,BSv&`RAe |
| --- | Minor | @5%x6`~4Ln`8k*e^+"+|QWKf9֔I߆١ |
| --- | Minor | Ҡh(a^ǸB;bk&"fn	vSf\KISmEE_k;rYL}ksJ45B}|%@Eެ+OWگAQC{yov{l,u+t i#Z4ը:*7h)9ҋCHI%{A$Pf2w+R-bὪ櫢?:bxM\&݀I!t5Mu4Yr{Rf0.&HzSUhEAqW%)EA.;w UlR`#{K)wVR;.]Eso4/T  |
| --- | Minor | `n*Ck\3ٺ+S}	إi^]@a ]ie³	bO:۱>h;%)VzZ7{ƁMB[[voh-I |
| --- | Minor | \X*Se-#SX&u6zJRs=VK؋ߕ |
| --- | Minor | ʹ[9w㥣"l#R*0!6о'MYᔺV)eJAԖnȰnT+mi-mEX?v.&Q'isl7UmyF<[ӎfL3IC{J29H^,P%Iu	ةTg.QV&/nۄ[.Ru--;32`ߘmjMABת@@>Oz`Փ M}swʹ	c60WjD2Rkv^P# -({gsӬm;6wI)w~k Vx( uڂ+f_QOӽo|E(0e#\I$k`Wei'fOr:t50H\QH?rJ'C̕κ+ާU0jCcN!#k*C愺b0Is}Fa!ivC3Cڲce ̼O	GbC8 |
| --- | Minor | @V\4ʓ%ikk`@080a*Jn}oBZ<i	V*s}ٔ=QYm'y c"nvm0㟟4ae*hK禎{{REYMVۺRLPvGCRJygǩE |
| --- | Minor | <KAB!FF3j`ƚJ%3hp<$9qh%VhPNa˯HĚ1e`?̣=7uT咖P~v-uY{mLQX rnL57& |
| --- | Minor |  \VRuDme<lᇝXB5UP1T\qCiYt !ߪ߈e7rv.7Cǵ;/|Ic}9`<nɋXSI,l9;m'uˈT-w<hR}hy]&IvtźVޙY2(FVq!c=Ӿfwd3Eu([0!jMUyx& ̎S`D e6~>Ec9މGQWeb}+.Z92jwo凸Ox{/9;Cݬ= x |
| --- | Minor | `%	HPlU$V%;b^~LvϮ|o*W_~G H-FC* |
| --- | Minor | e`>(l/"''^8.eH)aox.g@AJlH<*G# Hy;XyL-Lͽ)<Y)Di)XD嶺.jV<.;[!O./)ZAԜEXcy |
| --- | Minor | %'kKVNr@6_>bfA)ɥXH݅RV[ |
| --- | Minor | `mcɺ؟cl5ZHdﺮʝ4ʏŅXq+Ɗ˄*D13<txD1hN2@ |
| --- | Minor | [	f3Itډ^Uu2\cB@tj?Jxq|ݧhSP"hjdt3	NfU$F\y5E ۖczi\l1Ҕ\gHsh[s%# 3jHmkmFyp]P7-R` GPyJԾ|.ŐW;֚ۍIKg1bM |
| --- | Minor | ҞǔL.^\{*Tj*jJ?Y)avb!b@OTM*{7C1Garv^Jp	7fmE |
| --- | Minor | ;`{bL]sOf>w#+@< |
| --- | Minor | *XΡ*VI26OIr5<Ђ/יi3xQ8{]ߗ_Jil~=z "셹Bnm=~ӖO	r&͂5`%ѬRE&Y؏ڛoإB\ݹ4 |
| --- | Minor | $~|wSŢuvJ,B6-],hehE2vM./]-ަL	Ѧ]|̯},'9P95 |
| --- | Minor | }6˓9Qa9_d|ԠX3 |
| --- | Minor | "`OΨL%a(.Bq x権OF+OLC+ՓVC/<mRP)iR;0xˀ1)U"!EB7xx5$'NgS?X-ONJ8P/"GE_*zPחxW3mN+ODHn<|e,*+d,VQ|q{euՐerc1fVaD.`ӈMp?`|O^י4C3=blh><Ut^']ȰБhW&!&D\fm_[S3N,u!<yAjd8lփWdhӧmfZʰ"`>"bID?^y*]'͔φ] iP|8#eo}mo,\b}R-::fa<G8=|Yurvz(:a?$Ɲ9mT=V9ȀMR.IFaLp |
| --- | Minor | O[s.=2) |
| --- | Minor | 5^hq6t9shIwKEEx4oyۉ[/	=ATSˑs?ɹdH@!Q?,O<-.kƊ*[[DƌrQ%w |
| --- | Minor | |"_wCV5( |
| --- | Minor | , ,ybGI.Z\ƕo{J%y |
| --- | Minor | ):1txltSVTz2?8%WTYVQIE'Xn3o(,aV57,gW=c>#C@SnIdlZq{0K*Hy8gT	VQ"Egq |
| --- | Minor | 0 obj |
| --- | Minor | <</Filter/FlateDecode/Length 4847>> |
| --- | Minor | \I#Wj4CFpdLs( |
| --- | Minor | `}7 [JrU\|?䛅7+o_~?[_ |
| --- | Minor | @"<!rW!~>1>&ߤ8¹IEV<~)aa?|!"|!0oLߨ+}ʿ(r-l%|ql |
| --- | Minor | ~ZRwH3Lw |
| --- | Minor | /pˣz/38eM;G_<_8O!.PHin!_(L?L`Qauh(?@m^%| EU?^< 6G8SX:dxHsI?9 |
| --- | Minor | رlx^rtfꇐIrAh" |
| --- | Minor | !*2ƍUư2+-m) |
| --- | Minor | =` |
| --- | Minor | `oqsWl^WUsLt܅bT{х{Z6$)D&*w%5^z7b2ykח$ٙd4umyZi4>0[cU1VUX5NY4-\@=e<CUMN=z^f~#hVa6	% I|w,⠏yFP9BED6+2w0޶p |
| --- | Minor | ӑܟfH[%#NuHlLdQ^ޚgk[wc%D~2+8#zBV+L{ޙ$ͻ5OEN6 ɞ6L}ŵ6 |
| --- | Minor | *'UcU~+([HIHhԭNRx+pPUSglk |
| --- | Minor | \;==fU# ="44*@	|QtL[x%WvI<DHGw~DfM7,tM$:xwUUW;ݩ#n{|NӖPgjQWa4s0'匒|R3eE;I]T&UHѦEcTyw_o+ |
| --- | Minor | 6.ZXWܤd_?,;C ߡw~<lH	MQ.iLF,6g "+]F"'p`S	HfUƁWȍI:ymWغNpf3)vHd3ܬзP1:@7PS>_֙|mƋ,u흜j^ |
| --- | Minor | }ZCX<6U#JTgx4CdôGFBwu$W&<Y̐V1o< /@gilfI6N[-0,T&1T$JNUK`~C65GT.ȑxD"ojW2ш |
| --- | Minor | *AΘ=~RfUeSY*s)ѣ(4ܽ֐^ECCild""Kܿ*>Փ~xbi0 |
| --- | Minor | ,กfһɚX |
| --- | Minor | WVK9FU]pI(*ȑ3K^,!XUd s-C~K_J0L$[~K<I^K;Դ?EjڟPOG"9{oh:(:!Kcd25# |
| --- | Minor |  'C<AÃnqg}(&-K̷Yevr[G`%c.>µhmZY\yyF?Õϊ<Oemܵ)qFʳg!B~B% mmT}	nBȯI.jX7,Uئf[,J>Զ2C1&T,J-w:{ |
| --- | Minor | 2=ݽf+ē_Oc"𜐣:Wڑ-:s$Hod^KtF::Q3sMm O c06~~f2AS3+K4Vͫù |
| --- | Minor | 8?i"o |
| --- | Minor | {hA.f9ph1|fs%o4vxcQL3f9a??p( ym'6{XVkT{Z!bt~6H9t'U%Ξ~Ȣ)TT=\cneB |
| --- | Minor | ]v5J5Ae~eR(}7X*	>9ZT֌铩!_ꠓuv_A}m&Á&<kҬ~'KL>Ыd%)]L;a |
| --- | Minor | }оJ|ɒ_p^fj'r$ Wkv}z-gW]y>@3VlM |4ҧ$Rf4fHWrbk!$QhG퉸,#%hiXꞪ)O>QGtb:|oP&`P |
| --- | Minor | .J}qؠѤŗ2@yHD#wIM6NE,i>O -Csh,0I1 $7-pt6s]	ӯݏVoTs-SRL~өCʮS'p1ȮrPZ%)>SF60o1!M5[#WD0p޸UR`&!k |
| --- | Minor | ^>b+eG<9|س`%\*cXJ |
| --- | Minor | /䢷ڨ1VK:EA*ݡr;ԺgQMċ;Y1ꁾrAb]MJh	[A=ƣsGn I k2k@P<jvl+IRB1arC"EU.V8a -U[̓,fHlL+lkZJMolpsAv,Sk0^O7D1{={	go(Z |
| --- | Minor | s[N҈Z>N!m"?;	` 𧥽DWaMrXXW5xҦl֕pUb'ǫ(KP~Cnkbƒm>2 A5^bYS1}ٜ}f ŵ[S	kN9-&ᝊ%Xp"}YU;f.)vV$v +:G\;QC|(T%匹[4utUT>){l%o Xս1lcל\zl_[mn2񒡿sa˧Z몆 _!ԥao}r/Uo{լ*z8%w4N,r!W[<ba'ߙ |
| --- | Minor | .~׶c:mb-V3|{d扂|,5];chue2v֤_(aEPy\ks65-5(Z1.۷_%;#7D\/܈1TS`Nj.LFfD8\ּqjuU]E?)0 5L}ɬ>6JJ5W5H6Uy |
| --- | Minor | hkN=;7h\ru$tCTfHm9Vb7k.yk9Lt,-^?8Ǥtd0hUpSG;Fu䣎Et}{o)"`I2hBBT8裳$n	J`uzS:w9rtfgc+!E~ND@P ۯդ2+,RnJ	aA;s䖦۸z3N5T(g-m6"l,WnuW٩am9?qo#TO^7Uҧz;Q<~Brh:LXH*cF2HYz :+[dG@]/{!JJS69+sSيؚQF<yb/Ra7H:zfM>i7M,&xBy09U |
| --- | Minor | 1yHn(ߠ`|J ti{|.Y_	JIƗNetF@R %3qVBg@^v\XxE~tp,w'%Wb;BCRw~vNjdM= |
| --- | Minor | `[dьc, |
| --- | Minor | cA~֕}徊.)Y]H%HzcVtk!E sWߢ;[+.3 >+S |
| --- | Minor | ͗9\MJ,A#'ׇg˪'&cnS=Y)?w<y0yK*z^B	:\sw'r=zI+]}Sn+^^],ƣg}v%)[xL?snOj`eu]`C̃+ǜ75àX0{=:Z%{0TpߥB%)IkwmG7"!ȝUb@Zo;XgB(Pѹ]	пJ |
| --- | Minor | ؽ`з6ZZ+r&]T-jPE# 9-_t_):pB |
| --- | Minor | ܃LQ*[]Ceao\qg5CQ:	8aa.rϰ>̫!gn,ז:<ŤJfY[ݶi |
| --- | Minor | >Gh1R |
| --- | Minor | ?_ |
| --- | Minor | 0 obj |
| --- | Minor | <</Filter/FlateDecode/Length 4123>> |
| --- | Minor | \K |
| --- | Minor | +^ 	 -=)?ԃ]ClJ%E~|Ԝ~>ɓd8Bw^OQO^OR`OWO_??A-W W!c3חrNNw4ѾU8.域|ç<Iq |
| --- | Minor | =kyhte_pASW~//g#@:,>%3DbGQl8E8+ |
| --- | Minor | ;-	gA+Oc |
| --- | Minor | /qD-i'%!֘$B$QGPl}PR6*esqQd< |
| --- | Minor | ,*m->J&ȘcPd6RB-[:+mT+ITQ?^t |
| --- | Minor | ʆBp-sdZ]HyȯQԪ(/E%!J	nPӨHKJI]Zd.Ϧ |
| --- | Minor | /|#L[!eNRLIh瓙YBB 3si!!h(xv)6 |
| --- | Minor |  |
| --- | Minor | PUM=^EѕNf2e>a|]Sŝ(I?$ |
| --- | Minor | |:?'	@f ޞ~:)A:ϯӏ?y*gɋ	@ʣ1#u8!Hu(+hkᢸ|J3n:m!ePjY*-rIwxp;L.r')ejGi;%(?D>(k}:]Y>fHlR%J{Q<	j5ʠ>,gØH?,Y:~xYh3q'/^_Sז`\/I>ʮ!q-/o"3([;({Xʠ ?(?1 |
| --- | Minor | \Ƅtrd|),prL(b-tWj^Zaq vSTZjX?A/Q0i0wm |
| --- | Minor | ְ+5oeVｱ{?'~!"iL(~ lc0	(	ԈC1ttPaz:y.1Hʺ!i8f0~R{]D`L1ULTntҕGlX (F5D\Cg-g17Ilw'wOV"lě&C|GS1 |
| --- | Minor | )Ie-k0hb%\#$YJ7gv!pKĠ]딓E4%ӰfddǶ%,x !%J&W/5φ#r_׌J%q3ϒ!17Yu>d@&RI[a |
| --- | Minor | $ahl͵SLMWPX |
| --- | Minor | <;b7d{Z(7 kt(4+_	<:9'J16MLZӮ;TdT-h\JFD0+gzfRw|QV+{i)7< w9&K7˙[ѝ=@ |
| --- | Minor | ~zR;qF`^&G~> |
| --- | Minor | "e>U |
| --- | Minor | %NMS<;7gJ}PSͬOLGfth|Ϸb}A#@{a<5v J;f;UZY"@RitJ$_ӳEAL3S ⩘%MaEvq>JGqTUS 	1P^9BGO&pM |
| --- | Minor | t]|p%=Q5ax.h1o^)cnk^PN%RnL  O411QWf>oi0?	d0Z!`Sc8V2c,()X6߿Lam2#No3s~g1M~rE?I>Y  }8Ѡ \EֹW*V-<7Ri<! |
| --- | Minor | L",x# |
| --- | Minor | ?fd<&Tmq |
| --- | Minor | @zm$ |
| --- | Minor | Ё"[As,^:۳ƚ |
| --- | Minor | =i]T՝5%g .u<&6\/BjvlR)fܹcmAXֆA)	*r-Ou2SܯjeՅi0Z[C<ij |
| --- | Minor | ZݗwTF-+;^ 5pc)J&EU |
| --- | Minor | 'rum0W |
| --- | Minor | ^p2 Кa	jUA6ֱ(xׇҗB̞ͰнV	U㌀ѣ8SNSwkG-nXyzq18pm[ރF£71ouu'#20Ob,1# |
| --- | Minor | #m |
| --- | Minor | pTRf4]ci.xv<y앁\Wkn |
| --- | Minor | %~sBR+_"F=ե&cٵAcR |
| --- | Minor | -[HBJH%xj<òfAEoOK5*2@sY}d@SΓW*-YT-5B]%O=^z/l(Ywޚ)/$<,.T2}I?S9{Z/,h}4/ZR5qB"qM%_rXex̮bS q>0Q`HH2lhO}\^ EJ5g)Gi"9N uP].lQsxJmIqr}}|ܖXc.ޕ]]3f衻E 0A.3u!1c!Bwc[tn?Cws撡gXr4ߥmp&L~4S2	l[leUTQ89%Sfbq?gƥ{Kb7yӖz.RKjnAb<׀sN( !HՒoc:2-sʃT8a[K?fәT#ݣtCpB(A-7'! wڤ%tc |
| --- | Minor | @˳f EQjoCR; |
| --- | Minor | a)!N{-%snęVڻc5	gh7b7"HD>˧ݢU_}o:bܼ-'A/AB |
| --- | Minor | ^(89e	m83#b/貏MX棂,]Z 0RnuUTA?/Bi|רx<-s:%@)ޱ+3|%jE9ڪfZcۉG^)>R摳ӫ*,FZVwe~uZ-SO_Rҟx17LNo]]>l㯀SThMͶ yi<;L )Z?;'4( |
| --- | Minor | /Oˬ(;3k*.DЋ5SC3uUҨZÊX"Sskx3K#F\̬\ۙ!=`k<(ag |
| --- | Minor | XL#ҫs𤫡26l-Ld+kM |
| --- | Minor | n!ױ|h9Q"{R05w#98[Q;z^y5@058Gm/$4sqOEfwxH9FBwYtY+14߶|όTrƻ.؎9m!Qݴ |
| --- | Minor |  |
| --- | Minor | (c@<Z=WnwCNVVv| |
| --- | Minor | )DpƟfjW;StfH_`d=)!DX]zfKbk[ |
| --- | Minor | 0 obj |
| --- | Minor | <</Filter/FlateDecode/Length 4462>> |
| --- | Minor | M_=QD"YCѦ@{ |
| --- | Minor | 4>(Q>9I`;#QoRsO''O?ҳП?~wDo8sr0C2&oOJ|:Yڢ*4_L]x@OJ1=u~z>_y,{UY/S |
| --- | Minor | ] m,ӈ+0/eo-`1p |
| --- | Minor | K卩PE`\3Y|]ݼ6qKCgrV@q-;ЁjܬPe< |
| --- | Minor | ?1}W2*BϿ"Jb ױ|I]/.َX3T4<)7J4*n~EHg#^wpgpKV=Cǀbpy	3U 0f=B6>ܦ#StY`N^=/UtMAl_K5BKait.uitT^e&L9%ƚ3GGK$YP* &"Fq>ĶoM2?o1A GUigJ<"!)fid(CIZXW |
| --- | Minor | A.g]xo/]/4/ͧiGw)@Ltj.]rlYNoe |
| --- | Minor | $1zʫӨ43pa@tM`Yl#M'6L*8%fj{< |
| --- | Minor | M |
| --- | Minor |  |	cq |
| --- | Minor | :b䨎Iv65Ƹ#iBQ@ |
| --- | Minor | @c{jnd&Ydy<q\J!6}ʐƥFУUd |
| --- | Minor | )(A4f_~X_@o:{R0n`!S+Hgwcw |
| --- | Minor | @F{F<O^y |
| --- | Minor | !9QHkFU1<ouVKldsQ2#楼e*4@rPE9,jErC9{#ҙAR H;@{]8qZ,4/ |
| --- | Minor | /4HkHw |
| --- | Minor | $fOy>v3X*VbgsaJ3'+cY1COydtQKfߵe{AxUDA'n^oe.Fŧ10НFkY/&I&SM$x |
| --- | Minor | { |
| --- | Minor | @jسkDHp0g<$hyǂ?-+YwD7k' |
| --- | Minor | [txN9pp |
| --- | Minor | [,zu|Jp"{))?Gn^H@NS,kz	Crm+M, {߭F%-P3NU\iVvKg?AScTl7m	&6o,pl8iMZuw$)w|^!I0CNX"jHGC<߆H0< |
| --- | Minor | $<جf'Fu ˠg 4,9 |Zi> |
| --- | Minor | ^rmlwI邼*ykߔ)d0xLh7}> 41]Hwirq_CƷ4>@i2^6p14	~N@^;"7RnH29Jj,yS64e_ˌ(7DAp=y̸8уf| |
| --- | Minor | ņF%!ӕ9{Z/f |
| --- | Minor | #OE7;>Nop,'*@883pf=MgHFMC礢t |
| --- | Minor | 925ısW)5-j)-N6z!0R |
| --- | Minor |  %3̹}h^Eʩd |
| --- | Minor | $	xʺ,Nlu[UYobv$䉬i-9t&FՎ-ZOVpxi]wEx@Mqqa&sZtC[OsUU |
| --- | Minor | '$w |
| --- | Minor | pk4	d%w1kV	sVd܏uOizaG5H]&~cQբ|/˪LNT(ӹBY*N=XVpMkϩ" |
| --- | Minor | [}	qcV.s!$ |
| --- | Minor | _̋x,;I[I,{3[ɐߕAj-T)b&(r |
| --- | Minor | 0ۿ˺Eq=Cyg&uAٮQn;tמna 9軚MSyf |
| --- | Minor | f*Mqrn˟eәRp<ּ+e(oza<0')xU>:a'OfV]F~*qsj|y.S;ȁH |
| --- | Minor | r`}#n 7ōbוqR vDp,gWAeĪ-;U!Eb	};<R1NxP |
| --- | Minor | ^Pnl:;U<V)RxۍM;F 5Z[X5:">(8|˥*JSC덢?x02YY]ʎޱ92iFgg'^@;OWu |
| --- | Minor | {:"V䔦;)9`ʈ;y:ʉ*:4 ۯqIྺ1bs< eؑ/%8Ϊq[I)Z+`ρ}aч;k |
| --- | Minor | }_-h |
| --- | Minor | ͜x#xkiWqWʯB#\6FO9ƱxƇu=]"4vXA 4(i. _VWJ1$({v.!ZdqYrY| Gl |
| --- | Minor | .= |
| --- | Minor | ([Exo,,AΒ}O*J̠d,I*AޠwN.ȰW!ȣ#j6ALD2yXm0[<%7	6oL˂g($$n;X&Bq!(&λ.Y)ڍƼndmQ]Ipٛ┥' ױ{;lQYpP11_-)㔯FN#5n嘗|ahս\`q/-G/+=:ݱ0Nut";e j8 =\[2[KAs=j$)zkTk/llkpB>p19dsQ-{?*cwq |
| --- | Minor | .Fhr\,JlݥeXgKj{Y1&"ßP{|8v2ci9/;Z6|	wZ\ǔX0-dfID |
| --- | Minor | ޹:Ʌ;Ng*	i4؍QounH^' |
| --- | Minor | ]tgr]>}3Yd.9Zo4w |
| --- | Minor | *Ȼd(*zawHN;[54N}'тZ; |
| --- | Minor | @уpp#7t&sp4^`ޅ g6oVUcDOp8=Rzîz}kR.FFӏe̛QGs}}	ϐ'z{W_j9b}>e#pZ]ނFڋx|^4fG&9Ay-xq~#՚WfsgK7de!~C3>x}`J0L#`_].;;;nXX/֭\P|3 |
| --- | Minor | ]o#/h |
| --- | Minor |  c9_~`-?CRʏFˮQwL[]^큹MTYJ!LZdAw@` $KW`w__ui,4յjpn̖'͵zw/G׻;a^y%H;5nsֹM%valZdEA8~i6!9d.Hϐ>;_B=/z} |
| --- | Minor | 0 obj |
| --- | Minor | <</Filter/FlateDecode/Length 4980>> |
| --- | Minor | \K$qWJK(Am7s}ؚI/&2ʻT&x|7ÛK۟~Ɓ÷oڨÆ ۏ_Jwҟ*#A|(eunxz/&4>]RrP+oS<&??3^iuDUy7@ݬ9>0Ф߿V8JT2Lm7TR<N42JM][Iptȇ:ICG_WGC]+mO~-Kp^21 |
| --- | Minor | ؈a&gX8N/l&wlGnff@DpdJLrK}9{EA+S$?|3#.S|ڢ2k#!/=S,]4jc&)4G<`!ؼ	ړ.P |
| --- | Minor | /-ܝt'Y[=>/NW^ZE	xh53g7RLcdԠ#ExDH>ڏ<5LD+cJdwn$QĠg.k=MUk&M>Iչ Hzҹ%K-KO$?~I$#?'KYJĦۓLNO>/)yߴg9Jxt|V335_6^kUAcPo?o1YF8W$C".kW>͓Yd~>:_rdzT֛Ia0u4YnȽ|Xڸ(W`tU86ڹzocS>vQ8H`J,i]z5w';gYA"'b`V-{L܆ߓ"3!˧FmJ]gwyT|꣖ŉNG]t]kkb8K&\9K랉C)X{:c;m=,ryJɛݨb4ў8:Ijb$?%e1&2enP+vXGW֥ǳ+ nmJ4	WHI!*GwgY*	YY92I[p`w++WLL% |
| --- | Minor | Idof$Gu+*s~xyiǱ!r4540c)ZL |
| --- | Minor | ~![acpU{(J,@zRuu{D§;9\Z,$#@VxqέV98i(mYOWQ#)Mi4\)Rj߯z`0me_	}LT;_4n㻣8靎!f#2z3͊QpiqUonH4VkjX͂j)PŮd^򻦑a:o26ݟjvm |
| --- | Minor | #~ k)NH=qm3IUl |
| --- | Minor | Dn75F	BD6,moBȵ	G |
| --- | Minor | `"M9Mf6Anh'^'km M$R㓋?N2	7L?z?e |
| --- | Minor | $W%;IO=ex2; X#[?	D4YO*qƼa	Д}>.Ƴg9惄)Gm?jb3KȾ2DڑnW_'hVL&Q(p |
| --- | Minor | = aeĝu'q51E@m<MAk!8̦g#ov<܃4hL&%Éd,v٠R1-~SqTLٛGTSڷN&6ejZHytI	tszT9;X&N{K#5[$}(u!I#Wc.G$@sW*6iSȀ |
| --- | Minor | )K뾼!k1#s |
| --- | Minor | ,?	06ٯirG(+*?aȠb%wgMidYu-wDl^\=JUj%jHYW5(O0 } |
| --- | Minor | (4wY,JmKWDD 3OY,0i' |
| --- | Minor | '  |
| --- | Minor | G7ŠN7 |
| --- | Minor | N餈0i-mLk1:%FT[2\~ɔ1=դx:3ζqhyi2c*js	w-&zpod/ZcX-HwEa)m!gcVÑkq]\z8ԑ1BwA8@X<Nri9l}"m;9뵳"uhtMR*hϽg?<J |
| --- | Minor | EQ9 ~ìŦ&kfV?px]Uq}K`4e<) 'C:cҨ%x{Vl`fNOӓ |
| --- | Minor | (d鰍02!cFofpks.o9 |
| --- | Minor | }w%gٕ\\r|(gKLa]hɨ1K[S.H_z׬ϑs*JHG Bc>in\) |
| --- | Minor | ^}Q1[rp) |
| --- | Minor | \M$,T\9ӱ8xF)~`/{6wgEujd)qA2.T1<y:GU#@͆u,z^y2rocczf2xP{_IG2C8@g׎-9e(,4@q伧;KƦٔZ~CO ^'h3؀DjR!#P9v~(TSj'.5+zFY|ՓAB |
| --- | Minor | #7Խ9-HK\|!ge)X1"I%dFx8muOK|v.͹qKa!(=5`~Y |
| --- | Minor | [vS9C\޿v9eׂZ |
| --- | Minor | ^ACmH8bsT SV{VLNKJ~	<Vqb5g	M/`q5${M	cܒfi02Fϼb*2~Ayt-_=[6=mAm`Lz]˴uD]ADͿfTG5I[H[Qk7ÝAuSչ!*CQjF |
| --- | Minor | @jiyKr_O(ʤG2t]uv7kT %\og:t,/|TTRO}SRj[¶څ7(j8eҵ$!HBGLhU |
| --- | Minor | hn5	V$jeVgG*0Du\XZ	O.i8>an/Qs.zO+G |
| --- | Minor | ָqz7E&I`w5<E.,Zd&u	fZ<=vH?l <vG"t}sF{%wP |
| --- | Minor | -J_i^D:0ece>{$!sqݟ䖙ۚsRz丷 1>t8I"p9euޮqZ/_aE	bt/w(+a&scvoS{im#_TWknZEFo[qc]&¨k1?Mz,A6Y(bdW*0}G { |
| --- | Minor | $\k=?Hb(b*#la@wRÊLMjc }-Oi |
| --- | Minor | "4g˸^U"eFF ETˑ/1wE |
| --- | Minor | z6Bne Ғ^-bKg_ |
| --- | Minor | )H |
| --- | Minor | ܋Ze.?U3p6"_i}.fjZI6,Y:qDҔ	>BM:c$`94(:8M |
| --- | Minor | ^L1'pSӓ7P:D\6^o"R,/chd2Z0T4;FlP>[ xN&3ˎ)p>.C"~.Ԫlyrw 1Ý|%Z[!3N9^<b~s!$,@*9g%qcYȇWȏR(Oi^x1S$CeTg -y0Y |
| --- | Minor | z)c4,F?	}l:{x9M |
| --- | Minor | ;[e$;Khm*d ix~}HjdYRJ&%,u_ئc{ $>B-.Yʋm{~/6Z	"0sQl[=~pd 79/>֛֓k=N;kS11?枺V{ocZ漆;W'Ld	G8yp~^,qC+FF>$t٪Ͽܒ >Vùj66Q_Հ_DTӾ?;"3Ч	'Xy'G[Z_*mb2#J{v5	)I },_hS1#jEZn}NsiK |
| --- | Minor | .iB#)'"Y$ykCyf+\epkW}CxkFym$D~:W]DcH1f{|. |
| --- | Minor | 0 obj |
| --- | Minor | <</Filter/FlateDecode/Length 4100>> |
| --- | Minor | \Ic |
| --- | Minor |  ^$Rk`!oAv;/DQgtP{Z("?./ҏxx]'=wO.7|{\ LRAϫR~BH׷nUT!\銗GpDJ>FHo(Q[oSkj?F4yn۔i$w= |
| --- | Minor | *"Ӎ<'BKk'7Q{ |
| --- | Minor | > |
| --- | Minor | 76|~8(sϐzh5މhu7K]>4iKIU#ohLEq/YLc!63dXS_qKCM5%^()w	43ϝ;$~LMvE&ZO;^g*%)ah;e |
| --- | Minor | $Qk,`9)ZUyy |
| --- | Minor | WԪ҃X!4Ŝ"T'[[fo-i>G|*N} |
| --- | Minor | =+]R*(E,,-,9+"&bBT|*F)Iު)Yf:$KbZTZOaOP?mH8Tpuf:6umo |
| --- | Minor | \TVoMB4u8֒i4e];zY#O*7>-"Ym~}Kۻ:/ӱsVMUl`g&MG`^̖ֶSQTɬ&naRXYW-{to̮̘ŌKE~g4 @tY/E)[63-j #m>~(đhW7(	X~3`vhf;iG6|T4E.(? |
| --- | Minor | ]8K@Tlf..P U4ESC16 Fݻʃ8G=<plͪE$6i70ШZoMI!0`,@I |
| --- | Minor | a:^ތj'Ϟzje*QR;[uf͖{e8>._c8u*?7]dLc0ij|4WY݇I܊K_ ~}]_D |
| --- | Minor | *&nPU#zoE|5IRh>d-zʊ#=پ }Om&輎Ju>W1Vlub~H(ΩߞP:`!7jb |
| --- | Minor | &NͶNYjb=<c{,M?z--uIګ[zh>/Uet_=F'.tfvnR\Ϡx:kS%y.?OtkC;k-rԋ*O$dGjn9 |
| --- | Minor | {UoqEؽ_Lɰ{$S8nn# |
| --- | Minor | =vw6tQVqWvx~ĥЛ>m8A:bAߍ\'|6snukf8˷آ |
| --- | Minor |  j6ڪ١ |
| --- | Minor | &MSu1L |
| --- | Minor | ^;%fRc;3m |
| --- | Minor | 3&>t n1;(ڏvþИ yq>	ѩӡpGDWd5CS-HUa"g$ob LaF)>*7n1W[vr@d&m*;2Ot<x3zgu7)E,@("~2)*^U!0i;sJuo䔨;9Ϛ][گa*y||z5tlO1^{x~lj Ld4Gm`/Go:ʙĔEzZC	}#P0{$sS  ]pv ~Lz:♯vnII,h؜+m~zsxF_lL |
| --- | Minor | .QvHE@YNvvU#F晖BeL[/dg6Nv=b[֍Z^DLiVSX1[Ҏ%3[C_kO/ |
| --- | Minor | zPw~,X6b5}D@uNpYpW&\˾WIX8%-+j+pGƛ]J'׋ۿ~خY ~O	,)tx"P-mLRY,(,9|۾&8!=c=E%IHKdWjvO}/d* |
| --- | Minor | 8fZKU,9%v	DXDokӰXmi!SS=2z'S.e./I=`8YgT0iLކ.z¿yt_t8=t)Dm~Jv	1|3Bg';Q,~8ј/YCYpCaeicrDbgu:◫4H'Dr_ {bfg5;#Q"vaK-Z^D-M: |
| --- | Minor | |MQIvg!*Luj7:uDH6nii:,!߄Ăooc.fX'bZz ݸ/Ueg97/' |
| --- | Minor | P6v6KHh<yVU-0}Bpxv^=WOOX+>gMZC\nJgQYt\_c,ጥ/p8 |
| --- | Minor | G@v0nk"jng$A-hl uӜ\{'P\>̎Yv(nzvzRrT# m`}N=X\%@L[F9*rޭrY@,,\~봺-zdfL5KagMO2+5q1GXJA  |
| --- | Minor | %:d8dzՙXygv` vP |
| --- | Minor | |<*U0P:>sMxn@EF.@]EHL\Q |
| --- | Minor | _iyH7D$(ljڕQOZBp%?sSz?ܔzR=)x<Ew |
| --- | Minor | n>}ǡW}:ۧL-yv"mP//*w*1mOZo{sZsgV>^ܷ)~c)n1?NÞ%$ہ;DRN]Voiynي_[S	E[3 |
| --- | Minor | %.[EuVQoFQ=C[&9 `8N.G._?=}j0]Ô$(Np:4%mr1C>80ui Tn/=1H6IigWǝsRo`tq)A_ƜKj%QpG|E@aRۗn~~6{6FD\ ;Pj~pyN	?\,Q'[ޠy%=ƐGuN>$ڒH!_n_x8.=Y:T8SNn<iY^(yK&ϺHC$s0	CnVVTxN(0࢈[rTd˶ZM:Fs6E;VW(X5BB''R+ |
| --- | Minor | ,gTuj5VD=TP=xF5sH<7~W匲pqkCgo;<'_7H'53G-\nI<Z@gl<<n^	}^)58qWԿ쪤Ol<^ |
| --- | Minor | $Ŷ't*}p`:XP_=6_+#ŊCæK~>#76U V>q |
| --- | Minor | 0 obj |
| --- | Minor | <</Filter/FlateDecode/Length 664>> |
| --- | Minor | 1	8t5$@bbqeX7N<{(ďsvtoq_ŽO) k#ɇjt۷fyR^yykĖy>W=V7uws3 |
| --- | Minor | /_=8j&  |
| --- | Minor | IGܘQuJF^%^aW&pOl3biEbS8i |
| --- | Minor | }Pvqi [;YPBR['DxvhE6Oth"VІ-f-Z Su(T?{@HbYg%qT+8b'F.ZD |
| --- | Minor | [Ŝɶ솊jBxδ)shSwe-_OUgVFmG:IA((GMch&᱕w9Ϣ#m{啀gP\Ҿ~(l%˘kw!f |
| --- | Minor | @F^-4~ WX/7xZzh놡7W__5U)DQPKm<FS;B~;Ɛ}T׊4z=x{}>ڼko;.-$24vCTY<VHaz?Dv |
| --- | Minor | 0 obj |
| --- | Minor | <</Filter/FlateDecode/Length 119>> |
| --- | Minor | ˻ |
| --- | Minor | ݧ_c9'P:*t.*:9#ńV0(Q7pu1p83cbxBDs9jy ~q	BܬboF[ۼ݈:Qo" |
| --- | Minor | 0 obj |
| --- | Minor | <</Filter/FlateDecode/Length 3478>> |
| --- | Minor | [K$9+FPp[iHⰽH]]#D#UY=fԪLIN@pr2t=z駿ݱhe |
| --- | Minor | hzLH@<']CT/ FXNc᠜)gF-O#z]5:}9<Zy%Q&)E0FZĸ9-y*iǲK |
| --- | Minor | ~D1&Żr f |
| --- | Minor | ,4*ϻW|p0 qy񀑓D|aJ,_p,Ȭ&!Vw˿9KW1OO+EZ2Sg\+n(p# QΫe]L+0kNE,C0_bp$IOM~	ƋYg3ɬ&=rZwi;(p$rI' 5̢O)ҧVIZLBzvbHJTS\LY<*m7?˜ٴ[֊R,Hy8mdV,e"2iճ7~D$PY;VN w*I*1?$C=9TRɻ$`äRM_MoTZlriNjwwx8HgX=SbV2ڕ'Mdm^.Wd+3$[&,mj2rJ<g/kU4lo'#R-2[klX٨sj4p9\<j&2]p"4Qw63^'%V,˼!Lenf{Ft |
| --- | Minor | lBO7ai?۴f&UЄ6izsWt+Ng1)dMም1$.A3Ў UDIOׂ |
| --- | Minor | #Bp|{S}-n"a/	@)$JaKc7q rlۻ=,9㔐F)jȲ+)@SPqa/j5Ջm>+?BKA@*FFw]yC |
| --- | Minor | ԝ}֌	Sl=&<({	Ʃy|0إL1tLZ	M2 |
| --- | Minor | :6ܘUgj2lSC_+*d08G@71%gtӊmg;(ɒ:xv |#(p,,;7	@Bt@|\kC"H |
| --- | Minor | ` |
| --- | Minor | ,waHD$I&mu-SyE1:KAHRO9<^o9">bfw1}R |
| --- | Minor | ߿T^24̥=݌}ބ~<'Hg-us|ެQc6I]K'<RYx)u.)4tj/a'AUi=/V+ |
| --- | Minor | +%ׯŭc6Ws/ULsc"7ܜD>4L"~:DtޙL#O( J:]̱d |
| --- | Minor | *AIyUتɓhS't{޴ބ	MlgFRM,t/\Kɗgxd |
| --- | Minor | &D<oh4U? T<#u`g+A`J5(4@"(.+Tfq7M흴mT |
| --- | Minor | ""Ԍ9nY1θ2#㱄MΎpddAJ |
| --- | Minor | ~v &K6٭l!PH6(Ѳ |
| --- | Minor | IĻ?ޣ{;M<!\}ieiL1*%fh3>RI$Z*k]$r-J "wB?T:Jed(:YX6o<$P%Zڊn+m+NNF$0?TExX#KlvO6W_l3}d.a>tPVY/-hrIq2R9yi6d;.9R[$~:9eTjJZ:ؠ:ŃβDJI3רC\t$zA*Z\nON^<*u[e |
| --- | Minor | ԝ8rah	* |
| --- | Minor | *X"RiԒ+1f@>Yu0@Rt+uj۵&WfM@FTCc./¶׎kZM7	nm<꼼LC	-KI^J̈/{5#m4[X&؏i	dxʬ>er<Z"q~TH=qvјZ(AvYbm+H^'ysMJ~2*K |
| --- | Minor | i2i\:dt#9ic[>?몓d	|c<Ӷ |
| --- | Minor | ̢E}UPrQQ?ΰj[qD%^2Mxik@צ]M7g65Ɉ;ũ$l~PBGAvaZg4?껂4:EVyw%o tpfcs{ |
| --- | Minor | HZ e}]VA P<+ $MV]3 tevt) }%-SJ9b9Z`t&t.Qi7	@|sNFTtg;x?*ҪQvPϩ<boͻxJ,]ޠg0q<[OUk\H3v\GѴUn5nɐofr.^w,bO#tX[Z}K)MEc?uAO,|Ր{LPAXaԮ"vչ!@G}GU:tQ qy;^Q/Ũlu |
| --- | Minor | {E}JuiܔeNs9i9#ô |
| --- | Minor | '{2RQz6>K}cT"&4+>޾쑏ՕOm[G)WgP*_<`uJNwԩ=ٱ`Sj˨T$Z^z=.#V'!? |
| --- | Minor | 7vn=MO]X݂plzt\GAk |
| --- | Minor | ?Y^U<¾2w6FaXqG_^Ye STVŵQI.l\/xnw+\j¥t{Y,Zv'}. jI5Iֹ}]"n3&[>?^.!L)܄㷿ld˕\D |
| --- | Minor | s}0>kSwG_X |
| --- | Minor | 0 obj |
| --- | Minor | <</Filter/FlateDecode/Length 3759>> |
| --- | Minor | [ns |
| --- | Minor | )9#QwȢ@@w]E]uTEt{9>(x'{2{JpJlwo}_~ݞ7? |T}v_r߿q/"v'kěA2<܌qP}FCj\LK[{f+"k;Z~zaӾio'xt7+6">e7 ZgsO=y5^ԞM~$oTPOc܋,c}Os DA)8G7>~R=X_^hz'jTm&dkuC,aQ4IwE4Ccxt=>JƮz-Ⲯt{$7Ƒoڔ17v<n2sqV`^Յ>N3`tdo,"]m\il/?!1d8X7Y{󾜅ϭNƃMdmBt0o0|wmѠ |
| --- | Minor | *b8|Fow`֙1YO}ec'__q?MgBB5Ų	]%n 􇌀!a_lrm zҕ	1>@5y>X5OfUs&Gh[L+1~K1ҥ4F,qۧq̅@[r(>=G{Fplۺ:;}1e6=45kZfiq궊;ፁ70C<&h6x'[~78BXi] |
| --- | Minor | .^𽝲۰ |
| --- | Minor | "f\(gjrF %	/c!T}-V7{-U[$DNG|8w$-]հ-'61H`&hӃ|pK@*f;EX9<}DĲ=MZ*ktn'=&UUnŜ		ί+XKv'I1 gj!_㿾eAI@CȎA\ĔNX1-&y:bxRR=x)*O&I  |
| --- | Minor | $i$N3qƫ^6~r\@C{t#Nv'>8$V|BA>#FO! |
| --- | Minor | FC$'({آ9??`#E-߿1+p~ |
| --- | Minor | cnxRY	Q<_h=Z<S4lD"WV'M6z |
| --- | Minor | C[6H׎")#'\8ݳ~gtys¿W. |
| --- | Minor | " f^c^Uo! |
| --- | Minor | ]ϪCcdaȤ9暿B^CjIvr\!B~S 9@{36_F8:'qϵP\?Öϡ_T(@E`,GXnAѮA)/tE{QGUb+ĜiȖ"Zϸ60mwNr	Ҋjw3CF̀0	i7xDߌM}!KI]`/rrl65֩+ME97	e:b/N@רuXQ< |
| --- | Minor | 8ZC	vz*-%*:#~nnl| WBqt#kt\ EJSMJ~@`{ %a`\8|*;ؓ^zJNeմTD=b^%51%:Nߝ,à*s9 )7KtJ}REn#+o0*MB+{L!lQkToPTԽ*bvkHYx2m |
| --- | Minor | ">&{<  '56=qAb4ks	Bgy#Y͙\? |
| --- | Minor | \l7PkG&=	PF9 GJpI+kEYIT$<(0~0	29ćOP:QUVl?5ؽJUiݣ,\UHpjvRc\0uhtsWqW,¾Bt-x*oK[;\۴xݑ+,YRB.z?O A*.ߺP%n)Y;y;eJgxCﺿҶ؂ |
| --- | Minor | !*Kz1`;>WT73=$phP |
| --- | Minor | &r*vwHÔ*:o{y9eYhԎ:ޡ0DڴԬَeBsmά2!{swfl7ϔ.&͍tp=Wlמ/V=Xɛ/sWEρVz> `!~+IV饚O:|iٻ,\O<kY |
| --- | Minor | +av^XB{Ɨ((e9PؾLG32JgP	xf9P:1y~RۣkÐbcLlc9N.[jz?\kk\Wձڨ}eh"n; |
| --- | Minor | '(qbɢ;H*&!Dh(KRdrN*ocjDHoЂ͹8FzEvn^Vu:,#pM߼:E)[c51#ZDVq6nW13E`?L7T0l4{}çOɏ2V.|7`Vd>ͦh˫`kl_bTGuK7]&ST|4G?ϜkCZc|&JhN) >"[[A9Z'w7Vmc6>U՘k%<S\$TAf#Mٳ5_qYUsm!=c ;#ͭk|'OiM)i=Sd1.1QTǳ[/>NwN!6ᮯlu^i~V¹C͊]Q:N0{k&QKWp8h |
| --- | Minor | $׍';Ot[ 5P+kHz_k؞F̳8Ff<讀RMD?*^9QD'HD*(<CfAVs+XB}zZ[,lRn'*Rv(c\('_KfJI^bfatI*Q}\I)+57H$1BYqw{fN[*P>ouLעE׭Fmt\ڭ]Z{/U;zr |
| --- | Minor | VW.P5ae5872'յI |
| --- | Minor | KZ/zDy	Ru-[F6vqJts&X+h|PQ	\53XQj+o Mn@?_ de(LOoS̰xW&=$\CpkJ?i/M |
| --- | Minor | 0 obj |
| --- | Minor | <</Filter/FlateDecode/Length 3580>> |
| --- | Minor | [Ɏc |
| --- | Minor | +uy ZHdwAro"N"u=V |
| --- | Minor | (<>C}O??oJ(rmris)xqѹ˽ƫ;s4ga粇h.o+|72Vw֍oӜ=L:o?xu]k076zxxqk%s_e%ͧ=<=	T=Xp䉞sF 2e-RÉZ2f*vp?1DHo4e|ŀ>(/7'09\7"n,h>GJQ,!Vu:3m2L߀Dz~էQ`㘼EYDaP"gif<fC\ |
| --- | Minor | !+'ҥ=H<^-}-'H>We-$ ,vV1tidw]da$xvW(	w9qnkm*n^F"nObp/Uxy%<cXwWx܍^8s)sM:WBeT-rۯCɌut)ުRiA&+ak2~5;/0 8BFAI@`^S[Bkʦ]o PZ%II1br2:dPG9q jHKK.Bm-61*Rg EM*0x0anS`x>1 	#fH	=~l[+]@Wl.xMe,{ |
| --- | Minor | -lotݭQe |
| --- | Minor | .2	@/GҙBNs߭f a4!hV !ro&X};9 |
| --- | Minor | |E}S#6sO FcSlHqKoY;_JB2/$}s2 |
| --- | Minor | TԻx;YEDIIqoԋn@ƪ9/z!PukǙ9pyF|N~G'ɝ${4,x˿_ |
| --- | Minor | {Fc8l\~KVeftcytP]VQM''Moa1+v$gQNہwJy8أh~r<f!dIk(Td딹?M4tN	vn,9\)`ot͖>l^F[1[ |
| --- | Minor | ^&_6=]'[Hپ+YLUV4*7߮3Jq |
| --- | Minor | cZU9"H}>c|E~P |
| --- | Minor | [B	y[uI	FE'KWakŏoƽV^JONٰ |
| --- | Minor | %L?VG*Eb)>XB#H,E9drEߙH	WEU!VJJ<TL0rJIi|1یL3}ICO`]\3:QHJ,I4ʚO_D2 eb.1-Btte֐"Wx64H(%|RnFH7 ](@:YD	5==$+a |
| --- | Minor | /PTw<  6 3d=0$\I[:$wփ#t¿sZP-]y9ތ'$+yO.98Y$~>bbyl "9˥++3:<M:"7]8w6FBl<^5ڊ(gɱJ3{dۙF[w2fe%9_/ES7#`Q:O+p/cvb nkDFzZc\Lg#BSV7vZuƄt8".+lJT5E?XsBMs"/rm#Ŭ=*L7ؖ>63 |
| --- | Minor | $k'fCI cY'l>3Ԍ\)5'pCn:j.:cJWqX -ipRE=ݞ@g.9}:k[qG5ܢ=9#*I%ӳ<1׊-iΗx4z |
| --- | Minor | 9כrGw4t<kǴVf嗠"c/nOt?\q;[")d~zV헱H8Բ3hɆ=p0T%OCD=3~^O+MwNɨ嵡$rG~?ђ9,ZW |
| --- | Minor | [47KJ=%OځY3Bo |
| --- | Minor | s}_Iė,a@=VucQLQpmGOҬ<kE}ln$*}8P8Ϝ_g:xd<(Z)-%jւPS&n3P䓴mxMbʙ7a^$#%)N1}nr&^*x3\d,Z{T2sܳxW5G@ꢙ')C9	ZtE=r	=1}5?ȲY3Fh񐶼{<4s,H'rL4~0dy*,S+&3H/ѝYeo4PyĖ$۔d}`*{V$IU.UhLg)j+dz&?|nrzHcK=i%drc-0c?d ''/c/eYTﻌR*oOtEz~TM~%sޯҫ]WjҰ_T:_dmh[[&dz:ɉ˙oȸ{/L	jJj/A9?wi`XRӱѶ%׍F#][(#n̋i FaIybXS%Q숢h|\hGMy}<cklF9zU"#Qi<%O	zYҔ	1ѥ$iv2Ĥʑٓ崣P[N>'M1 J	`?랏8e_BI9Er|]ܘDIj-^oJw+J^ |
| --- | Minor | +##C]/k=[g/D1dn2޶گ/ͥ!{9?)m-E2|US`Pu^bQX@CIft8띎,*S6OiDhER$_QA&J t8*rX">zN]?c1QRw(ok޹ܭthqMC$??o6虧v]B5q-1"HKOK,;v-wYh(9ʜџtQK`j4.ŗGٯN/mp`Z˥J/'}eF;2%]k=OԲX^aZ=e|  |
| --- | Minor | 0 obj |
| --- | Minor | <</Filter/FlateDecode/Length 3555>> |
| --- | Minor | [+mj`0gnf8F+GY/V]\hM_SNéS |
| --- | Minor | gzoSSbISY{ǚRӏ?5g_~Hp |
| --- | Minor | UZyZԇbD&#{K놆#V*e%gRqsfLҟKilmfKOVmiXq$MhujuEK5Ml |
| --- | Minor | ^T9TpV?YaqdXrڢT-WZ&t>`K{Y|WF*+o&%]Kukx#C:8L.ej~I!6;`\/.v#콙}Xӧ(@Rq |
| --- | Minor | {ze2\CW'1jQ{#$SVtu_pc7d6]"B!W/qg弆{h8K24]4IT%QKk)2Xo"9mI A~RdݷNF,'~ʓTd l |
| --- | Minor | } |
| --- | Minor | 'Ezcgbb%<%2)0-yxǈ\ؤ0a{i(WbqČ'f4$WgeXЉoU0!()2ѽ觃j7BVoא>vl]䋏rZBkkA~l<BikfqɅNvSRzͅ~ɺZk!jiE=׺GrY*<j(O(O	Ҍ`bhVej[b]b،=S^!c;Zo&vf!o |
| --- | Minor |  ).ym*JҔcnFVzDѩUWU1j'k<@sQH^][ŗ?ZTs;+yYz-cR'd_	w~bGKyqt}Sh#Dc#tT*=Z> 8:qǀH |
| --- | Minor | ~#0]}t&m"(6[}vʵ.s8 ʌ{CVv߿XAZ6a"-X&]=/פ	Ao	6OhALy#^ڒke3qFF#:J`Hgm̫ |
| --- | Minor | ~ |
| --- | Minor | 49D鏱m	-+^K?yŤ_D%g[_YrxA(xa 8"UX9풷\ > |
| --- | Minor | -)-/1-emO%d\e"Oہǅd97|O(iP︷jt m7NT6Cf 5uG#ʫek8vp^ :Յvo[ĺhȐ.lCM\CT@mߦ^s?,KIbƱDJ{% |
| --- | Minor | #cA>c ΚUw­bK)j٩)sY[Se8'rdq0>GkiK3p |
| --- | Minor | $< |
| --- | Minor | "SMRwZ?H<QzDAS+Vr>u<|Kkks$5TuSI4{7FzN>D8e\+vO}Ea&I(<!j_~(}pmԐ |
| --- | Minor | .!5M?P%_z2#ogv3<"HWl:>Y9;'!E9ek4'UbQ%X%]V5Js*<Hs<9/N8Spz,4T3iDY%wEVk[Bye%t[Lҽã/Oxfs&r_a	GiBHXw٩44`eMd"sV$o_Ӓ%nj^=]}?ܵʹ-l?ԝ7XPFM{Xߝ|= |
| --- | Minor | <H>fwE=^ |
| --- | Minor | whշJH |
| --- | Minor | ZR "4md*6EN_|#[\4ë´IQm |
| --- | Minor | \(s>>e"Đ\C2^隦[49g{$ǝ~j4U |
| --- | Minor | v'RVf |
| --- | Minor | ?ohIo|u-R~6*.O(Ybףn<d+-(̽|W@fHg߰^˟dDq3"-#>D~Tϓ%:"o|W-o?RfOfGxA6&o=2kryА |
| --- | Minor | z.X['omKx zp==%.w6Ҭse/P֒;VjKz`2؄~&Y(Pdxv7p<afiw>%2w<6^u/mX4oN*atV7%EIOr8ɣȣw:!iRM|9R\;Gp;45 |
| --- | Minor | &,^2bc=O[m<F$]y^Q-Es$^͛/LG!>>xOB\OƹݍnjzCZ;^[U)8˾<X#>{UqQC8Ch%2Z<#x86İ\;*"z;N-aqn |
| --- | Minor | *(W՟q6b*wSa%+%P*.毴/u5SfI`l,]-Դ=82V'HҳI7*jctuΏ+9ߌVO |
| --- | Minor | ' |
| --- | Minor | /0Ïqy٪&<C#o'g,/;EGHWu)O,Y?(wYw>07k%2|#u%Xtz?*4~kG{lT[.FRgγub2]v' 4JՂ |
| --- | Minor | (Gr#pu3%c>6?z8n݅AڸC& |
| --- | Minor | (qm}utse"z?GCې7=wd^Rj{g}h>84?	~fw!:NJ~W]ݼQ(XYݜ0ʌJZbhc2lOFO	JYpweJT> |
| --- | Minor | " i{j-1߬˙jxN2uo)ƹ ق'#勻;&FZP^<w}:LpR񄝿M3.z>iP|8Пķ?[UbKJS	K,5AINqc/(۶@Be~㞕St=] |
| --- | Minor | znE4(sX6p/[a |
| --- | Minor | 0 obj |
| --- | Minor | <</Type/ObjStm/N 200/First 1905/Filter/FlateDecode/Length 5164>> |
| --- | Minor | \ks9v_ͤښ*x=fw3M6rZTK |
| --- | Minor | sM6x4* @RծV&*[Yc*4(;Cʉ3w*7VWAihUWTZլ	vXi :C!ur,(ϝTF'2V&VaT+2B+$2l2>~*	Fc!*@Ӳٱ+  |
| --- | Minor | ztNAUNO3RЕ# |
| --- | Minor | `+p-)EAd4\,	,H%LH[BRuIUd1wS\}$$ -TEĕ<fV8AA ЁT@!VQPu5qڢY&Ψ*:ȭ*z̰LEβb TdW(>H3	ő!yɳJ:P;CRJ2%H(xJ8q8%ĩDd|H1i>(i͙q?3 vZ{/0@_`<Éuઆ\`<Ȅ6|wGmwy	i:Ϻ:F$a심Ku jpEa0U;Y%r(W,A2B y(Aܵp |
| --- | Minor | %. 550ȏ\\m`Cb.9*׳JYm ,evYp<a	bkw8J	bk,mP`o"iPu%tJ |
| --- | Minor |  |
| --- | Minor | ' V"o |
| --- | Minor | `t(͑uܦwX(q29A	sDuiJSO<8#?r<VS#Rȡ@9iTYH%̛0"&D:tVy..@hBK:*@BqVg)K]`	H\C_ RP2%%X̌L #S;Rnp؏0>rerdӑWkC`] |
| --- | Minor | jtxİǊK<p%$5H2DA	V]Y.s8/?Ew~l5~pw_ |
| --- | Minor | ^|x.Wr޽]1tZ|~r~ю^\v> k&}.'j?"Y߿~=E|?/x?	]6Z_gSoi` lV|.쵬{u]_5ͪY/*54/Ȧ=C7P{ $m]E꺮(պrsw?_o'y;z_b>yӮގjnvy1͇	taBX>{3~|ꦝ/ڻZ 6CךN5Yv>ۇUn:xb2=kHk@p~N6`1.ՊV`}hVvdR>W[DK"X |
| --- | Minor | 5B^䩀2.Ԏ>Y5bD1x<1؁\#iiNv\ܶ%eX5>eAA{sЗ]kL(E/;H{K>3X+ |
| --- | Minor | &bMĉN^FB[_+Ɔ-Nz#^Fpn65'y;0\>c:sUM |
| --- | Minor | ۘALcId?*B|I0$AlF^q~0)y1~0p@:1S#b85s;J4Xfi=c0L{9=lKCWXj&>jA	{~kY @[WӞs֙CҺf |
| --- | Minor | 2zA[do7f>2<`/2c9G"1ե i,,qU8܅Ac򙴀S|qP!p~?=-)KLB:,w-3߶+˗ |
| --- | Minor | v% |
| --- | Minor | $(r<AȎ p !Ń_3z̹},_@T\d~fFh)ѐe瀭EmjSu6"_1Q.Rr4Oe7^-"		▎<uWE wW_BcަQ=e |
| --- | Minor | !VW鼫CTUp/~ |
| --- | Minor | ]Í>_.y |
| --- | Minor | u(r}X{aph |
| --- | Minor | mv'P?<Mj:)-8F6,_`ݣwMώx+tsz*^ΚP'~<g$ڝMl.`t'{duDOHm\PIќ"3f+4d󒋩TS֩K=L1C,wizCr\@`+.m5ݬVz20n.c|6l:~>ϖlR Ԩ~`"C>J'Lm>Ytf(=q2g$|i<J<${9T<xIlSEIOpO، e50{KO2K3,Ieɚdp$ZUU*o#"06}ئmEjEDDpr!yiq9i?iv~/tnv{xXd05<1:ŧǌUsA%=|1wB06 |
| --- | Minor | <6 |
| --- | Minor | {=7o4p뺨g<-NIf |
| --- | Minor | ƫb䳟57B^$I; |
| --- | Minor | NA2F}P^yc:W̕LUf2fR<iSIq[K;L'Kk<_3bTj}&<:>0&p;W*&uَ |
| --- | Minor | ,kf_f,Xyh ŧҶ<зgbz'}s.jz.2XM_Ŕ_^I$( g* |
| --- | Minor | բm,'xx@H7a"B_4.p|K?ft|fĦQ||[0,ۈ).쉀,Y8jg׵I1}mx"'++C#(cXwX|l\)ꑇ̽0F:3>VIU!j=Q\l&Ƙ_kOCvUtHׁ;pr|V]61=za!< |
| --- | Minor | &頺9tjs{.҄[y(%eP~. |
| --- | Minor | $5oKnai"o#l8DP4 BD8oOY5ը  |
| --- | Minor | ՅW~ Ys{=_LW7<cuf̳&T@UNev@fSsx~<]59M |
| --- | Minor | 4yDʝ.:t|=$~h(h2 |
| --- | Minor | ?} |
| --- | Minor | ˶gW=x7\=,[Qv8꺌UW}̮-هIs;X4u{r5[w(xجn0:~$G*{kHGa@mЦo |
| --- | Minor | yjӺ{,߆)?n%ѓ&.'P#	-{\(ƝP{,K yz7[n]6\Ysy9]xwhlXo<\5.X0p5ͤKp/[Ln;äXN0)W+.WlNł孴}ꋃ|-o|w{N'Hw^f6*outV%]3#ޱحe_[nN">AE,~tlHi2D8՝45Vnh0#N |
| --- | Minor | %g-"6Mҝ{xrxU#8ѮUL.ށHgwm.#L]4fs"]J7u6KC] |
| --- | Minor | Y@^D}@[:)/qg+/p!~C5TpTÆ.jpɖdK [s+L+t qXk"Q M |
| --- | Minor |  |
| --- | Minor | fz,mpZr,mUlՀ=oՀnj@[5mDqT,ҘC5(&=M÷Ԟ"n$AW:l |
| --- | Minor |  /rA~*ǐIaě]T{_ |
| --- | Minor | ~u>9bLV>P{h];] |
| --- | Minor | _ |
| --- | Minor | _ |
| --- | Minor | _ |
| --- | Minor | ~ћFapNxxOAou և<甤֧xH<wSgVܣ3*3ԔIkgkiIX8%: {u-]Mo|dfNW)no7XtlYiCgFu" |
| --- | Minor | \?s36_2|n:misf4 =,4Ch3P |
| --- | Minor | 7<\6+w| |
| --- | Minor | <Ё4ouX@ aO;`|ĕ *G!GOYyq+o[l1Xxa;REвCѻJ |
| --- | Minor | -}|,	̒Jd4^lMf(Ϣi䦋 lZ<4Ήe<HIYʱ~kꝁޘrKmkk)ӒfT!f|T0k7ieIԋ6b}of8g:SG<*+8}V6_A1wZ|5tt &YHShP(4tҀ1/݆mm_]x}u0_h |
| --- | Minor | ^?Ź |
| --- | Minor | 0 obj |
| --- | Minor | <</Filter/FlateDecode/Length 368>> |
| --- | Minor | ]k0ů;	6jݥz	5Ӽ$$=9͊]!_JإuELF:~,jrl/ԇhۦ~~VL7csV],ұ$qs'Y;|kҍ)+M9*u<'M;)V]Mi!$޴RJ |~dy+?5ǛڀBtRZ |
| --- | Minor | PAdu1ֆV`^^@oA֋܁^ |
| --- | Minor | x	QQ2hxqDt1ЅȚC)Aci	Z2Mkl&jzjC3DsIIUUf |
| --- | Minor | 0 obj |
| --- | Minor | <</Filter/FlateDecode/Length 463>> |
| --- | Minor | Oo0| |
| --- | Minor | +EH	i$M[5z#dA9zX$~xaj[nĩs+ܹ(횉M_Q\7?]*7W{Kh |
| --- | Minor | }NX"!9e7qn{;e{&DE¥uc}6Z%UnȺ\xj~1O7ydiAR$h |
| --- | Minor | &OAO@;XT$qFB> Ұ K,b*3 jaLjeI Q#HТ7 hJhĘBB'g$TȗCށEa*9',!AD星F9槑Spui#'PbԮLLSb*#QևKsGԘ+_`Yޟm6<Q??qp |
| --- | Minor | 0 obj |
| --- | Minor | <</Filter/FlateDecode/Length 499>> |
| --- | Minor | Kk0FZYRG |
| --- | Minor | lg?oCG{}IĿ$Νk7XqEi&ڮH1wr.Mgt|/S-Z{hEFu}΃X#!9uwi}\~]qw#8~޺I$QQp)ܚױnFd~ |
| --- | Minor | .秈kv:7j,O$".e2i9	BMB̓^/)5	3Hc$=c%@@k5f@3P z@$)mA$xDOM3$xJSp%.SJ@y CgSf)doUR&4dH0S&4	.pFviϐ?(0̇*]1 |
| --- | Minor | Š.*hiΒtrhnG9/Xs4+xJ |
| --- | Minor | 0 obj |
| --- | Minor | <</Filter/FlateDecode/Length 265>> |
| --- | Minor | Pn0+BDEj^`,C}m'ʡ+ҬwfվRrLzy 	#/wo>2M'y?<FK$ꗶ9	oͪ;:/8VR6:|r/#H5-kߩZ_pDdoY3	ʀme2ChtS;Zo<=X˥q-JJwtI<Wc3'>Փv, x |
| --- | Minor | 0 obj |
| --- | Minor | <</Filter/FlateDecode/Length 533>> |
| --- | Minor | j0~ |
| --- | Minor | ;%eI	Cj`NYұqyu)ԐJȊW7sգr.MHM5ՖCJ_w:?ҟ^d\LgS=?riDqEv_'ݹm }^:w"nZM"/'aWeƲ`_"%ofiseL<(H;)V1$viy1(< D7$DWkHIZc$m@@k5.@4ۀhFY03/ {3C#Ѕ{2hHȠBt |
| --- | Minor | ӐpO'K-`!șFMX\4jŒxȒ9(At38MKBׄbtdP |
| --- | Minor | KkbiMb%3YX[Ԅe |
| --- | Minor | "vj}T;Z8EU񗜷y3x8ΏsM,+ |
| --- | Minor | 0 obj |
| --- | Minor | <</Filter/FlateDecode/Length 598>> |
| --- | Minor | ]k@se)kf,`aRۛK |
| --- | Minor | ^߯ |
| --- | Minor | <Ɍ}fgoV9Xm욶x`¾i'qb:ա&~`ˇ?簿K;S_>`f8af>3nkN,[6<{7ܼuڳ&u1cN]Yla2b3˶]uyeb|$'Z@	O] |
| --- | Minor | .!Uȡ52`DTOgc%SJьwR{HEJ |
| --- | Minor | e+H9 39YC88DJJ-⬳5Y;F),YD8/!\,*p,{HYȋ=J=XE8XE9Rn/Ns#:URBjHrɁd^"gu",'q"u#/Kr>=~*5zz2vhf=H8rh<H!t75ͯa |
| --- | Minor | |xM>'|w]?Ő[ |
| --- | Minor | 0 obj |
| --- | Minor | <</Filter/FlateDecode/Length 428>> |
| --- | Minor | MO@=ײhBH |
| --- | Minor | <RV-=߻N0̼_UYfnнx2-텑n{wh'/H˧rs |
| --- | Minor | .D"Us>tnY	Xlb-fz2ދg8Ks:E幓n8V˂ j{C5^J20`/!`%cNH-N3&s	v6 \}~d;eX)QLW%QK+{±	b+諘*Q·cbש0+u*ԙ>8˜>p@HhsT81BIu|Sq"fSܽeu1vܢł |
| --- | Minor | /zњ |
| --- | Minor | 0 obj |
| --- | Minor | <</Subtype/Type1C/Filter/FlateDecode/Length 7132>> |
| --- | Minor | xea`l#Ab@t>I&eҦ3'd2Ф%Y |
| --- | Minor | *wqY/{IUW>Iy{y٬ѣYl6;tU~,IƦocY,f63a&\;!eطN> ?bƬy>|sGŊRS?QyI |
| --- | Minor | Deg&g%ƧFY+%=M8_ 7oyH=3|Ez޼ESEG^AN#?oMNg,Iz*77wnTj3g&·ffƄ& |
| --- | Minor | >ܑolQlf4	 gpTt\Y+ثklgEYQɬTpbkZg6M,̶lvlk"֣{Y49q	L,lrSyYXY/V^dfaeΊd`dfav*gg?É1:N溸xFj*ui\q4>a|o&B\<qŽwY_y`>ooࡥ&s>#hأ;hC9~7ѱW9L'G1?̽+0PEOdsJ/Pgl*VVUwǃxJ0:wJD2R@_JZwyނK@mLLÉZjzص3@} |
| --- | Minor | >\7~Yx3\ήbfH/Hɼex&v0 |
| --- | Minor | b㑸kp |
| --- | Minor | =rhexN7] |
| --- | Minor | . W/m:5Ey26bGЙkL*g!֧2C;>cbԲ7hpB27TkF:)ɕ6{ |
| --- | Minor | X6B\8b |
| --- | Minor | R1Ԣ<`:sFc4}zr@'Ђ |
| --- | Minor | ?ߎ8bĳSdp(`!>vqۼrqhc4-!dnQb!QjR7S#%NjAV<\{)a^L rUo Vkӗ]#Raϯȳn=[W`ɪ>  |
| --- | Minor | \R[9xrB+SPF)9L!jYM~`	ؑj /F.'o-%sQ;DKCVZc3.kU"PSy |
| --- | Minor | `t?[Vh7&G\K,PT+15eј;t\Q.W [EMѵ&tZp=wEisq+ih |
| --- | Minor | /Gy˾wި;~	-4V̚Aɓy}9c#V>TRNÇ4t[k?!w]#w>}Ϝ<M1H9T#XM6U^ZO@4z)(M]ѧMP[kv;%	h^mOr@i\muVcsyS]]Ά.NM`PS(oqhj`Ӯq6gKL.IZ>+q<nq\4#A;<8S&*vBP~L`fKU~Nv^²b*:ݬjV}kI$*HepٝO	K~)xJgCo(.7ϩ4Iث[]ߞ~Zc׊7Jw#T0ZȭVQ(PC^oKvI2zϼ@j>CCVO̖	f#3X :^1%q@qR& dRBe:q@[%݈G&֡G1DE:gјG<30/pr޿Baq4un#5lzM0uz*%eVl<hs? T{Sڋ4lKã^ړI2x6h1xEx+o(݃)G(6@C绯^(i=.Ji{FL5JFh |
| --- | Minor | ؛Tnf>RܙMD0/hK |
| --- | Minor | %Z |
| --- | Minor | Zb^arf˩4ixf9b |
| --- | Minor | )gPmMn5;OWt5O^HIi,N؃ȇH =(R+]L*ݰFMFk-ᣕG\uNX-bʡpIk2`۱(!~ >S\Q9؀9ʮ ڳN09+HI$ڠ+ݥ0l@yJ<%:V᱘z |
| --- | Minor | 2MI[ao׈VUmVjt"QV&MsRL[O_l=*{5-PB6H B*ц~A?d-砥x)OSבB]r |
| --- | Minor | ,79LvKs^Bh.~'4qF|[ WQ`$lYeKYso2?)H>(Do0`6Ѓ|>PWc0⹤j5L]a<^`+Xd/k@T.CkBO@mx3wP_o~ANҲҪx{%zk6ZޕΘt/4 ` `Ѱ<acRTJRJz:',dZ|>èyn.%wHImAre\j ]R37<J#r9.\J:G> *cc&qu{y@>Q	JV?z>)SREtfR?-"J6]>\.AnQ(?6KRy&Hr}f%IUh,/zuLD/ȣT]P076Lz%7(i1N綺%o5G@F W&ztI7\2(ش |
| --- | Minor | u>0Ch*.t	:?qЂwxb	PR#%FqQx,D4~7kr[_jA |
| --- | Minor | V+9Z&"Q~r#|ſ]G-Y'e8*̠5E3-΅ jnaDE<d#'F"NS3Ve'~P-S!'&BLթZ/RGMsi*[>O+Y&=rG MƴE4dN#JmR:.0X>oSC&PCFnn~S{=iA:j?)Vh+#nePQ`|3h\3lrBo^*]//'p6xh!}zm'}>Gfm(dFg:x^Wg,.CMmVТMZQs)!SbJWht< |
| --- | Minor | ?$M j>4-+zk_// |
| --- | Minor | =af"wc6@bv)Z̗<Gyg;tz6=mEZTt(HԶWWsN[k{Im& OC--$]oIuwڃi!t(j:>FŢٚBYr~=PQ?F154t0FY\PPtmfCPKWIFWi)u |
| --- | Minor | <v ?U;Hst2	mil:Ż%֟{ՕO	.cef&M0 |
| --- | Minor | .;@\47)֦dgjcC*$E,ZޯsTJ=4濋aX |
| --- | Minor | ¨gſ?0`9m"hM%<=LDna0RRmLx!TG0{*p̧1z |
| --- | Minor | ^?Ǽl|Yt~bR:bUkZM-m[>brGn{o,@,se13!oǆ^&мf?sx ݬ:r(kxή&6Te7MJL \R;ݧwAxf>`*z:+I+`FSIy9 7~G35| |
| --- | Minor | 2M:HA |
| --- | Minor | m |
| --- | Minor | }`~3LDhqHQX߈4#%	~ɩ4Dx |
| --- | Minor | =CCtԢW3>s*-墩 |
| --- | Minor | <mDOIo4}ĽqZHڿQq) 44$n<tìSt"ϣ"sK>mdxpsٔ& |
| --- | Minor | tj*ku){.| WkԷwٵdxu@E޵\(KR^Q2tutuwWdmPi2dH# C|ڏNnˇf-ZmrV |
| --- | Minor | 4$<?byфsx w|Ϲ_]_7׿Q2gJTG˷&)*2]f70ӕ:e"NƬ/% |
| --- | Minor | (B2~.N |
| --- | Minor | L?Iĸ_Jx'5Uۏ$\G>faSIT|yYGPt?{јf'fdMǄiu	x:~b5>8i=5\#nцzyd$ςlm6yj1 |
| --- | Minor | l;T@8,AdXu4pߕ,RѤ{jb |
| --- | Minor | <^3 |
| --- | Minor | )**(僒*V4Uw۾?ÂKKB۪0NX2^@a-}g{BtU*=g@fڈ |
| --- | Minor | ="g=#_/]&܆@Eu_u.-1_pPBw񦟙g_0=<"-`KB&^ܞPM%Q	Ǐϸi>ǎ9]=?i!&3@$W-x2i0;Y}=#)@<U(3;/G"N#x_r݉n,V@^3zNqltBe\v4\<mN&dh.s[J*?8q{,fgmP$?	'wZuaadm*U48^4G֤/}T(xg{DBa0$Ql(n @bNOVw_Q(s42E~Le'A%8rV_Jڰ{+%U	^«Gy(uXG/Zoi ֐qD$:	HGvPWo9:$}AtbW |
| --- | Minor | ^s%	{a+PTU}ўd7Q֑GE7h1 |
| --- | Minor | \yu |
| --- | Minor | ~A:SD<[HҨZ281H[y7̥ӷT#.Le"5Se\y"Æ? ka9B;lHyF9Sq<;E=ږdK&̇E?Z'oe{Yvֱѷx;;(Ϋ"w?w(ox hh~x8#х^S$ꔄ1kA1W`oniTePlR3OZ}@! |
| --- | Minor | ݇@l{bdgV"TO]luu奭M4lJcű+$5&7}?mLϬ*RO>SLx<f_6yB~X+W+4[T1"Aa?mFAa=ۨ.lowS݇ |
| --- | Minor | )LߺnkpѸCZ.!ßg܂1ۛ_֙=Ǫv[CmB ,λƝp`w^7i0X f\;F	C38x^>7"G_=xxM; ,lP6*CRP4B=UUHٿ/&Z؉@[^-OpۣmK5T_EIei#9@>W88YL/ඡX"/	nC$Dз]O |
| --- | Minor | C"ZcY@<4Tmf/ݼd]v^9PkF/y;}!k%xsnt]ezTi¸9a75jhywf_v^@p(gf |
| --- | Minor | *2דT,vZO	\ݵ |
| --- | Minor | [Z=U |
| --- | Minor | )>}p[Gђ>)A&b!gl	\r/ުP &ΠE ,IyMt5ZKws;)MW% j[/k]U5[p-4p:+,eb̌		N6PoKDpu|>ۈK$UBZ*~)<r |
| --- | Minor | ;GHxz/*;lvcjLY2/zx쥞~%Z;$#3cߔY(q;N[@h |
| --- | Minor | wI%|yJ2LCM[ NCs2dPSdAHJyU$77GmR9h-Fk~*EWԜDjuhuU65A85iޜBOuEA/= [МCKȵThp<(Q񅌳7LPc |
| --- | Minor | #< |
| --- | Minor | 0 obj |
| --- | Minor | <</Filter/FlateDecode/Length 237>> |
| --- | Minor | P sو6ٽău dxW`fxIVi!qFtaPZ:B$@*.b$EOɽms.(/8jn:{*=` $7{*Ma8NNϢn'((8[.q="a2'忿lgxqG%ݐnVg{Eށ |
| --- | Minor | !;X<utޘ56o |
| --- | Minor | 0 obj |
| --- | Minor | <</Subtype/Type1C/Filter/FlateDecode/Length 462>> |
| --- | Minor | `aa`dduv |
| --- | Minor | M~4L?200<A] |
| --- | Minor | $102rT9Teg(h$k*ZZ(X*8e&')&d& 99 |
| --- | Minor | % |
| --- | Minor | 6%%VzzEv |
| --- | Minor |  |
| --- | Minor | ) |
| --- | Minor | % |
| --- | Minor | ~ |
| --- | Minor | '܂Ғ"Ԣ< |
| --- | Minor | Y|wq{%g>?Duyt%us/>}h9ǟIYurls{mX]c!TvkA=~o~h&[Gic@]cs]wm7o//-?'_q|U[䷀~ĶWY?e]ܪKxJ-;w&Ʀ|l|87u|߉s^>l^9.<?DD ïp |
| --- | Minor | 0 obj |
| --- | Minor | <</Filter/FlateDecode/Length 370>> |
| --- | Minor | Mk@=F6M	jtLjٱ9:vVfaP0Si\O4]=/'jlWU~?|}w/:֕[E^ާBcK	YSx&^7;uO46?Ѓc%IrK4V5J]'vX܈C.m]iPLؕNFb^ |
| --- | Minor | FcAd |
| --- | Minor | ҄a4cC |
| --- | Minor | u%ՍXgfe*7r>݇ruE<b`CH!Y!I!3aGF=rsAvڏz7Ǚ%2+ASسq)< |
| --- | Minor | 0 obj |
| --- | Minor | <</Subtype/Type1C/Filter/FlateDecode/Length 5750>> |
| --- | Minor | ׶?1sP֞:8!VyygC %IVfdNA0 UPjZm>kVn}owy9o[u%F߼{7nck_eY(= |
| --- | Minor | (J?|=\{kR 4gμYs]/ |
| --- | Minor | 3a9s휤~ 0^с~Rh'n[O_tݔ#Ϟ;K5+\vAсv[d|VEm |
| --- | Minor | =k<\''#>5E03l	dZOmYR^Tj!QlJN0j5X%MP;ԻGM&RȎPS\j>ZH9P.rjZEQMlNvR{jJ@YP ]d	-,|->	D?h |
| --- | Minor | "dԑVRFُr%3zOLj=Nl%W=[/^vz^a߫y&A346ZLODhA$|X 8G1h(f,1)~%h<3n6LIH8MMbA<5kB{#h1Lπ&ɢX<*7cnY%͆d3V1	z߄3ÚBio6i |
| --- | Minor | #Zl |
| --- | Minor | B9 |
| --- | Minor | {VpѸ;bY0KW8x׋_;YH:w_?B)/G7J[yQZWbbcז+%3]N0k.	?>@,Z"z,g`6!gMBC@39"g4 |
| --- | Minor | )92LXIBp%x9lymϽQ"ټiY)G##K4jT`23% eU/Sy /+hl} `2sH#cWHN:o&g5J@d	n@Rd7F:9bcT?Q2tPUJ PlQm!}ٱ\9{VȪ%!,˱o_zlSp4ބ"<O2\-8[_/4B#\RX뙤[`N10-oo,[hny@$֑k2:@bυw.4t-67ЋO@dF17ؗ]<l{l-fvMkkt3ʪ+g[. bG	|vl#QOꐳL%HMH_1}4 |
| --- | Minor | XbLc{Ѕ/	>L``C\Ig?IՒf`K E%CUQHWe PjY=[!e6e4G¢B=<Z8bnm9Q?/z{;o#;Pʝvm7ttv~IY,4w%%ri$7S PM,Vj98`@o߶>Մw},S+x&2hlh AI"7C"f)bƮؗO*=&%\>h9y-gn0+/F |
| --- | Minor | %+?r83	jUZU10ƚcpr`ƾ@o?#dg~Bm#߇ |
| --- | Minor | @G!IК$C£=>Yw1#%WX_ɛ?c!'_ |
| --- | Minor | 4_g7bfY|'|͆gr8	+IˊL=冠_f38[@Y]D(Җ~^r0?&(}Dď &%>I8QupN{lNu |
| --- | Minor | (yTA>}>-~}Gtkw-`K cHbn9 |
| --- | Minor | 1?`La||':Eۘ^,.S |
| --- | Minor | \\hS?'aC{$}ņ}[ء8/0E$J|לиB) m^cc*tG&><N:-N4ip?1ax_ |
| --- | Minor | [UVU__SSr0mC=}3}l |
| --- | Minor | $c}MIސU_)=&~N$'m`J̬d&~Oaj1M[@ |
| --- | Minor | ?$FtC#Y>Bq"d{_%p:d6b8ƈܔT6O;fYqA?7di"=fZ& prLUj:hl».Wԍv!ܛhAQ |
| --- | Minor | JW@ˆld{lwv<I瀩O` /~&l[ʆoBzqh |
| --- | Minor | =^*cfDķ"Lt8p,,s	u>"@_4#4kDӍZɾ1.#ó2`kt'!%FT)-NQhxX)c	coĪcJ! Iْ6PP&Aќ+WmWJ}HV/YO;{P{OEx`ÓWCvB؄{x*']k|j2wOOX9Amk#!7t*/ 155=_6+YS|1N9;!r!h-[/Ēi2WLS@;`Ky2Fkgd&Rz9C-J`P	4n.`I |
| --- | Minor | ?~ILO@DIZɠElP\H6OJ΂xǢag~BcMg'N |
| --- | Minor | ^gu	e3Jg?*dUrIK	n ;un79u=w֊x5m,=l<{&>^΄L%[%A5T6zPK`])_P:}dQ03+,w`iS[*.UEDQ0 #^(&]^/Vxt9nC |
| --- | Minor | ;Sو |
| --- | Minor | 2ksd(ǐX5P	PgdopCO#VkAʂKRB	Zo$%3	P"}8 |
| --- | Minor | 3?M4L^ |
| --- | Minor | VƠkt#xN,@ |
| --- | Minor | ՘~nNoT |
| --- | Minor | -PjD*}T-Hn>!]m&my07W?WͯJPR+\E	T&7zup^(^cEGؓ*CUҰCd*҉i6x>@̃\vjۼ<`a |
| --- | Minor | ;(|۵!'?rѦiSK)A| |
| --- | Minor | .Cz4ֶ&@ڄ kٶif<i=y}i,~gLA̳lnziֱ<2CD_YiִrC	j?<i9^3gНoC^/ m2'r9FC |
| --- | Minor | =UnkںJ5*&y߹Z|nJ .`?}+Wd[U'˃z7\mg.bA'^T~[#Y%'-C/2JiP'#>UݱRR'ԧXDw	x%3Z\"o$hϹ8͑5~ڭ |
| --- | Minor | ~;jZd=++Fh}60<o |
| --- | Minor | ,rq+UMފL)`"+cjuXzc<f6hN}:; |
| --- | Minor | *(ȬVfZO3s1@2rLo;21UKsZM.4+OIħ J5{ 5lT"ſLA/É#- |
| --- | Minor | 'H]c<FF+C;h.֟ЛZBt$ܙ2ĿZG(ir<4G`w}%8my7hAt<3'1;/!Y@ªtM9Lez${H=s8E	\fJhT[u^Gכ=.#Z·g8n(3k.L&E$KO!3,@uhx |
| --- | Minor | $В"n>Ҝ[IH#*yvRꊔ_.<2GZc	x$C # 	>ۉ:{Mv@o$~N2 XcŞ 7hK/W^?B+M,3Lr]kHnP45){ܣDlLa4 |
| --- | Minor | ȋ^:x_h<l1F'3M |
| --- | Minor | ~OXZKs{Ѝz.^c+OvT;` |
| --- | Minor | mpIKTN_7ߘ]|'nÉPȍB>hx$3 |
| --- | Minor | '1_Ñ؍}Iqp?tSXLg'l?1LG ݍwm;dהPkB*?C"?MLGݚC]ʦ?c.s;v|'ON{-$'K#6dS]\4[+$>োh'"Sw;CX;5um4E5 JMH&\d4lh7!`M' |
| --- | Minor | *FoD|!V",gv, |OUNe3(rA3UǽN$v_ᔃ |
| --- | Minor | ^X)LSm |
| --- | Minor | \{M:7(ԆY(SӲ~uސDo6	a"2N&^ |
| --- | Minor | &H'C& '~&DA&R9Jf31?zzUW |
| --- | Minor | <޴ˎ7ǿkOI6xMa=uCvg7~z&(J4z	A38q\731IpWQJa55uYRJN+a=1@V%6K~M+"BYYn`j2q:¼KP:]bf&er?؆ҵCYcmF	N)$B&%E?Vh(/_?r?a}&Y<h%E'ٽ<FycREʌ |
| --- | Minor | *CWccW<{Mz |
| --- | Minor |  |
| --- | Minor | /_a |
| --- | Minor | 0 obj |
| --- | Minor | <</Filter/FlateDecode/Length 356>> |
| --- | Minor | Ko@ ;b6MCC	mSI%)fafؗYnQ |
| --- | Minor | EӚ] |
| --- | Minor | +Ҟ9okz,|*54r~XzYFrb?b+`ZsKZP[QH/I9U} |
| --- | Minor | +p2!KMS9Ukj9⸚GCv^dMZ659RS\wl4 ={?9K!Go6x]3ژ)%;[ys!эǓj |
| --- | Minor | </-V04 |
| --- | Minor | 0 obj |
| --- | Minor | <</Subtype/Type1C/Filter/FlateDecode/Length 2907>> |
| --- | Minor | 0\elhm;A[E|TVE  @$HB$;	y? "88_XZku[ZvuƃΜ:?+9{TBEt6.X酌5H>'Hn2M'_LϘg(<.:zFH}5'Mʒ[r$Ҋw#]QT["IJ$r9[RP.UHʇҢrDf;d%ORT!)-SEH&-swF'iiRffT{ēg̙>U<3-mxQ* |
| --- | Minor | &Y^DOWP͝>]TSeL+%rIydxL-cƾ2de$6NIP4QӿP3W%Zj΢ޠ]T"<vRTLimYhmmt#mS3ԋvRۨT6"h*]A |
| --- | Minor | (.?^OLL0#ǎ(˨'3%EZPuH |
| --- | Minor | @0ja^ |
| --- | Minor | h%h?ƣKrT.jo#&HN%n>ކ>UZVWl&Fc6>Yz.Z}>(YYg}.WVh4Y+fl=VUcXxunPFFFaxnGݼnkR	!=#D=1w}<bPF@dZ|d17[Ahq	b$VEW|hmz[i!7D:wﵻ Z<t:tu4z+؀|jP1Z!^m/{	}8NpqB~u] |
| --- | Minor |  |
| --- | Minor | `(Aeu`Hָ^d^P J1<:NV_Xq)Ƿm{ |
| --- | Minor | Lqi~xmA}|\S99gf/Q;*%ƮJtwXQ5e0>5*Ŕu/4OЃnG`S[L|#^T0s3@D>&n6m_[ |
| --- | Minor | ,KD-}hDf'8 |
| --- | Minor | gj`tjP^}lyx1Cb:hyE_qep%Dv}&sBX^u<ʝ |
| --- | Minor | JX*0[XK?N'MPDugfocM밲Rv4;kχBߡID/iL~Ol<o|48;5zILCmm_Q`<'UY&R{uXY`܆JD9_TѸ>^ymp}7^w@	(Nj9>4w |
| --- | Minor | Knw]4nçp-p۷ t:*y30"rճ$@r<Dq#?G9Z:Du@fɶauU/14&pCEO8jdްgP,lQzBhq apނdo"oht߲mI<2^ͥJ |^Wox/3gV&hi}ژ&\u@8R	%F߲z<]%HLղnʲtja}w{CX`j*K.)4]MiPjkսō M$݉'c[aI |
| --- | Minor | +~eXb%8Xd3:ɺSmގ(3T} u3gy(	ܖ"X7*Y |
| --- | Minor | *NF ?Z4(=?}3$sܽst_} |
| --- | Minor | $m`0MIt֣hn='(Hw灎[ p=^ժPCaL5FHQvOe9$y"H2T7!Y>7{Bh8HywwAx:B\ |
| --- | Minor | " |
| --- | Minor | /Wffh?E9$ .[:A4W1֚1oh@YZҠ&FڅArxN|AZ0'%=.I*!a{ӟdнćKT4m&abN,rg;9oja=Z`5שkYFOGСF֡W?؜@y`[oըd0!qN`x |
| --- | Minor | {va'*Jlk4aOx3m⪀ŧ$GJjՍ=ugLnO1(?t=!Glߡ>xW*#{1n~uTG'|밵1됦y#AOe"`hF_bTٮPeW~EA6g5:fEɡBKIG70"W{.Y &Hf4z4N^þuCK;fp̻ 4<ۤAWCXZKB׃h7T˽ݰO2tB]P*AX[gkl\yPↃ^euJcՂY(qUS q)D.h{^+KDfzPC><5۲bn3ƋSz |
| --- | Minor | Ws,gL=j#Dᨄ1,cFGGƌ!ދ |
| --- | Minor | 0 obj |
| --- | Minor | <</Subtype/Type1C/Filter/FlateDecode/Length 1242>> |
| --- | Minor | >NiEc͵9ak(J`MPB/PaC[V |
| --- | Minor | ۢcY%fgLeٲ-F -3~/ |
| --- | Minor | jjմڍJ9O*SJ+Tb\ZX 27'P	tT(#@@A(ՠ4 ;,rŷBXsF1/<=zv,m@xaXlngj<6R窙2[lMVa4.1WU;ς\QS1WZQQnV;m\Y9 Zp4x+Zggʕlw8\-o8Mry7-\ |
| --- | Minor | %ӿj..a]m< /u`hV褎CF 0 |
| --- | Minor | 89 |
| --- | Minor | 8&de2"ɫ/FǒQVpK.įEq1*~}O^| @QU%(F;t/'Ąec/$듽79T!%W?i^ |
| --- | Minor | !^|ѯGh8o3k['\[v|HD?(ѝ@ |
| --- | Minor | ؄[(Ljj2@>ESؐ"U4\'Mt4C6teȥa6cF#	o?RfbC	4;-;/bV#Hq\7b((zu=tbP} |
| --- | Minor |  |
| --- | Minor | "x#tnEǻ(~ٓG	_!q߸G"A*y)cPT<oT3a@{"!1-(QXM]]b?[^rExJ3z}yjI |
| --- | Minor | sZ[ވB.sJz״um[WMV Uv=I/BHM^(qf>MƘ5G6DZV9NﱊU<񯴹եH#Xi@z88DYDB{/F%K{=usJC%"H@}gOIo/ |
| --- | Minor | (]㳙 |
| --- | Minor | <F&㸌JJ7fi;rAM-)M<̌=4g^ag/61n:jϡVQ8HLuԟ]J{zؤ s'~xFz#yY٩|uWww; |
| --- | Minor | 0 obj |
| --- | Minor | <</Filter/FlateDecode/Length 311>> |
| --- | Minor | Mk0:nxHfm,eQ'=OK;zlPeO;YU'<:NnWckP[ގaVTOr_*N+Wu\ZdY ~QyWx(鄏|a;>Q6# ]طg*>cEQYURNi-I%I6ɉK+D8)j%x;@f.<^OxyGܔsSY0o<o__p})IxTnXKs6 |
| --- | Minor | ޚp[ |
| --- | Minor | 0 obj |
| --- | Minor | <</Subtype/Type1C/Filter/FlateDecode/Length 2610>> |
| --- | Minor | _P 8y9l "Aj%4E4iK&KiڦBBZ)TXGAQ2{pqι;w~?`@ [V=6s-8VӄTǫSLK	g4wCwY|/NX"P(=p^VւʊjuY\#]<GȒ%Jde-f+dri^F.Sj}ҍ2Z:{\x||N7PQ9O.}r\L#nUZYt\#][IJ7+UZ,yiYR,VbX)V0 |
| --- | Minor | %pb,rjl{+IX*v]P `S	W_Kf\עƫKs[hQ}&3!1EB爐&}1	G@&7Sɥp~$vZv/]Dqq擥G5ZH°Xi4z^?C8=ITSN=ԏ.O |
| --- | Minor |  p zrݮhecp39Wy z=uʋl૶!!Da;4~z |
| --- | Minor | \"ʿN3U}{VMf-~Gv{o1(,&aejrq'k w|w_CK?G7@N MQj7+Vr8Z;.d}BairB0xQ26ޕ[SMͫh#pOK {h:M+6hW[C?$<~_M1<2L๑Z^woc`atҨH(@B.JjÆ<to|Ꮾ	*ʘh#Iu 	PD)2RfDC |
| --- | Minor | =r1mzcb#c'Gb=Quu댠c$]StZ(?f5tZ]LӾf9pKA!)Eِ |
| --- | Minor | zCZH=h'D+7,sВє"}{hMK'a[+.uEk<<sD+cuIu$C_@:b m`2A`cL6ONvz`#oĺ%]ZվUQMe~}ޫn_ .t}>v&AA` |
| --- | Minor | "j2~?@+y@^,5OJ\ zhtRq |
| --- | Minor | ˝_C#ChUVKҩgDr?6GtbQ3tFqij\ZGn>2hQPǒ5xlwEEExx `#K7~$^"§;/fҪ-ikcCNRns66J8^谍UiWUt6]mklk@Q-z,e^Fw0h*3"tZ~i2'X2!8zU>CXZʏћMHn/^>y^=ֺ3'㰿P ?/Ibͦ6lo-\c%Hh	y]ֶč#ЈwFI}~"V9Cڏ:rb9&PʸݼJ;r,+P/0w@uCU]7} |
| --- | Minor | %O@Wq}doaQ |
| --- | Minor | {8:Uo8/A{!\VeNXe"yt!AN&ۭ2KG?5	>}'9"DoUycOgy[Hl$:;O_Fҳ_ |
| --- | Minor | $ඎvJ5K7IFݡŁ^=TI/ u_ߔ]I6|ʹ-I/o+,0^o*aw?Mu=34n	,} cm |
| --- | Minor | @hDq#r:j[j/ny[v^}|N"~_,D*v:(5dxmFR֊tqHoi6Eu~7CMRZۖc55%ICIwG\F$d |
| --- | Minor | ^K5I`Sv:u,2v(;?\t㫊w6+So@+i  |
| --- | Minor | kuɬ-q|Dg``8MQ	Gn|M;QT$`6!s |
| --- | Minor | \9WUW$%^ߐgce!e'&a)ڨr-v--1M~<CI}`(hZsuIwv6KdvB |
| --- | Minor | ܺ޳q7J^Sh%ɷ؋&8< |
| --- | Minor | /-m/m"6ī4 CL |
| --- | Minor | 0 obj |
| --- | Minor | <</Filter/FlateDecode/Length 234>> |
| --- | Minor | Pn >v&H"eSi@ɐ@4agZ5ƚ+8%0Bo89(cImTܲ(=U+[~oű-\ϠR΋Goysqlls@׎SuxϠ1;R_F`,s⺓r'/i$x]W]~d ie2~I9un>Bv;y*?m+ |
| --- | Minor | 0 obj |
| --- | Minor | <</Subtype/Type1C/Filter/FlateDecode/Length 547>> |
| --- | Minor | `aa`ddsv |
| --- | Minor |  TCYr?Yd |
| --- | Minor | {  T LB,e5zFE% |
| --- | Minor | ɚ |
| --- | Minor |  |
| --- | Minor | %@NBp~rfjIMFII~yy^bn^~QByfIBPjqjQYj[~^_bnzʵ4'WS{뾯^qݣuM}^}'Kww+۝S]7cN̹]UU,[T%{:y݋v}>6ѭf6H9WuVY]Y5{(?1a5UUX6{jw̞߭'pLk\^%ZؘQV\}N;D٫U.[NٓΚÜxYΌneߛEw/i񕭡;O%{w&EstO"þzvw5s8wt\Mb^9.<  ~ |
| --- | Minor | 0 obj |
| --- | Minor | <</Filter/FlateDecode/Length 233>> |
| --- | Minor | P=k0+4^)%:@#AWVRCc |
| --- | Minor | ,$=BupiGXycuܳ+YD(o%vM[q]爓tb qNɺWf]B	]:+o;iopJ#)7"8j3j"V=KMnO/D|( |
| --- | Minor | w |
| --- | Minor | $U~}m; |
| --- | Minor | 0 obj |
| --- | Minor | <</Subtype/Type1C/Filter/FlateDecode/Length 350>> |
| --- | Minor | `aa`ddqvu04 aCYr?DXd^  B,e5zFE% |
| --- | Minor | ɚ |
| --- | Minor |  |
| --- | Minor | %@NBp~rfjIMFII~yy^bn^~QByfIBPjqjQYj[~^_bnz9?$H7?%(,FCYtܽGf'r |
| --- | Minor | vA*e1fw961v{;ʮ |
| --- | Minor | | |
| --- | Minor | ~L`4߱wq}g<;r^9.<=<|?E v$ |
| --- | Minor | 0 obj |
| --- | Minor | <</Filter/FlateDecode/Length 249>> |
| --- | Minor | P=o0+ޘ j	!%DHI?R-c}A:غw~w:_RIїռBT'Z"	!ۦpfl@黾>㥩vF=幚GC |
| --- | Minor |  ptvQ<iZz5yj2*1ɲ`82#I8(2J{{[mon&4[o1ߦξG|vz |
| --- | Minor | GF |
| --- | Minor | zt |
| --- | Minor | 0 obj |
| --- | Minor | <</Subtype/Type1C/Filter/FlateDecode/Length 804>> |
| --- | Minor | KLwikEA#Q( |
| --- | Minor | (ֶBimZ2춥/J[K*Mh/xx/3(>vqosGm;SBqTԖBܪW+v"Zyd"kֹGvR!Or9"VWDYNk`874nltxq`h"NdEh5,\Vr |
| --- | Minor | ,8?Mzͥ;'tJYKt%;hl9ze;Dt֕[āes(r^^!ѓOU>2]Q2 |
| --- | Minor | v |
| --- | Minor | {OcE_/Pdj⤸ |
| --- | Minor | bKx͌0+R&O$|2'!C6\ڥ |
| --- | Minor | \.<nl2#CPp/Ɍ?t {`}!~̝f8p0*hCt?6KpH2"}ת' |
| --- | Minor | ^ZEP/X(Hyl:9/­_͚;IgEz&["Xڗ^`A/I-}E!fX3SCYq"9[ |
| --- | Minor | #E(bm~X$עVp3FOӰF |
| --- | Minor | \С; R;o<@FF4]K1ax<v͔NNVHxVvUUGT7,U*96 |
| --- | Minor |  $]_g |
| --- | Minor | 0 obj |
| --- | Minor | <</Filter/FlateDecode/Length 335>> |
| --- | Minor | n0y;M_m!uP&uJ 41QcE]֪ip4h`]i |
| --- | Minor | ^(rro1ž 4x?v\UĨhyL3F948Yi6 |
| --- | Minor | ;	W74wa 5Ӑ乓|Gb0Vi |
| --- | Minor | Ü	(˥\;W!|qle!˛ı5ȱ5מ^K=^ueg<O}릙yr^A[THޑ->ǄۦcvVzԘ |
| --- | Minor | 0 obj |
| --- | Minor | <</Subtype/Type1C/Filter/FlateDecode/Length 2940>> |
| --- | Minor | WDD1VDcڨQ5%Fq%4;4B7;4b7EhYD*Hu	jBF |
| --- | Minor | c$:랇gZ3sN{Ϋ~R$,-	$m6o߶~ݎyk\f^/	Ī_22Cw-8] xKovol.L$,Iqv^h$2>*80H*7Wp򥎢EEQ~>-> q_$~bih 4rłN>NUsE Nq8*F/rDHE[}"3e'Y+	IQ-qTt<j:r3Fd FJ"HvD-boS;KO&ku+Bl%>BNL HF|EN"vq2ǭl⬾ʄ&JFݡ |
| --- | Minor | ?;i^t}F%DW5qj2茰TUU2H%,T |
| --- | Minor | w.*YRJ9į m)kkMzeU |
| --- | Minor | #Bqv5?YF9a:Ww0|K5h,ט`p-y<܄TnQ |
| --- | Minor | s.vX(wcsMG]C"=nctHoO#!.e=ZD(lPE ::BLC(nno//jB2u޾KξJE3J+ԧ9[wzYZk\5'婠(	z0"6}<p$]fo#:r-3/G{v/	@2VFJmAB4GqƁY{;\jk4:CKe٭*H0r둸,H}!l0z"V`dM08æ@VVZ25g |
| --- | Minor | !́RjX3Kt3jw{1\_!GHHD>i@#2TP|7[uXqZNxwR /c*7hT}Wa\y`C@np=)lj^UY |
| --- | Minor | ^[Qv`]gD!OD/}}(_5Yג9^1=.EKg!$&<&W?+r |
| --- | Minor | 	6#%	eYK.xc&<}u,AlarH<PFZE.WY7lxFQޯ4`}v1ஊlhUGG>B4J050[O_'c|d~ |
| --- | Minor | 4JYnV]K3p62+=?XzE->1H@>Bo4Fj%HINo,mw|_A:ъN.0IF[J4$q5gu5kޱ&;)O^?IYP@0a!f\CeO	~>u@ƜN'D+r[J7#PNNj 7|"BmMyvj{A`i%3z_3Pj>6q(giqؒ7$>eP$R8OIؚc|F7Jj	J'Boܠmfh7L*$Ʒ1C=׏Pq	I |
| --- | Minor | h5T9%@Aqʠ(M"#5~ߥM]c/ŁK񸓁tDD=U+AE5A [ ^8,W2Љaw*J)(-Է}1<ÝC͙GQ:ãZ=>"nB/CSsVnXN*5\{zsaźB/MB<q?qvQI1yufsW_@y<iz#Gvi5AB8@*蔧ƝW06MDocZ^p3>\F3Gb%~^ў~͑3\RTܡk+ޝKk@~hB7ƅ(CՐK<Op'`Dֹ\EQ |
| --- | Minor | (*;;*ٵL!ݯn4rlYbS6\[R>~OVdTQ:8	Q3}.NDז*fQdfB"_RQZ^XUҸMώxDU{=gxUʢC!|5ad_>wCYtcbhkHtj9hΫUkʫ:o	ddLIB3>?ath2|{ל.+9s#kD|L2xn-尉 |
| --- | Minor | \sNuImCg1$3'LZ|ԋIvxmNS)8kJ$5.6U;ZOh#kbq\ |
| --- | Minor | (Av3LLh72MB˧Ȏr |
| --- | Minor | Y8ڦV On/.<(U'H6=SXҜM |yBe&e MygQȇ)5'I@PxB\gj>/H(R(8Wl'Nw0zߌ#zgnx\+Hɔ˓7_XλѠ _]c>p㧀n>}o}EQ _YU 9WYДRU^MnpFOE#+H;`ar3a |
| --- | Minor | ).,/Fl88UPVK8TASy4U#IJ!9FlllƱ֖K56cȤmW* |
| --- | Minor | 0 obj |
| --- | Minor | <</Filter/FlateDecode/Length 261>> |
| --- | Minor | Pj0+Ri]:ⶉCv$d$zfv;&*Cїռ	:Qϖ#KEZ̐`B~>E]WR&얉 k]8PN :;q7n>@+UkфN3	bA.Y,q-p4eGB8Z9A%,m%t&8-rB; 4w&;ګqO:!7+c5p v |
| --- | Minor | 0 obj |
| --- | Minor | <</Subtype/Type1C/Filter/FlateDecode/Length 922>> |
| --- | Minor | mL[eYikhtH3qa&ۜt[*h^E=-ZZ1882>k2˾NrEQ5wi::o}8{ſm+=K |
| --- | Minor | \tK*Bߺm7vmBQ$(Q^RTۭ6c5􋭭*U+f3VkYެeˋ>c1Yﰁem47\.PZ7.#kOzƩǭ>5''[Ͷ>VjNX*_EYc4@63BTǇk:\	EJ"ҟB,74@_o/&9oD>D:k8KKD[("!XU?Nbc+307+<{ |
| --- | Minor | `cs@  |
| --- | Minor | }!"Gd62B@$ TwQl9~|M-4.M:{7Xݡ=,?"^K.c*/~4GgOBhB_I'O_ zV+] WV@<F;wVaaQ5TwH}~%GڵUKif[w47?'?%<&Rb"O&R0jnhPg >O^\87α |
| --- | Minor | ;BlșC/7?'Xt#A4ttw?YT@nlsq;u]Atm |
| --- | Minor |   |
| --- | Minor | ;6,>.EM®a |
| --- | Minor | ("|(Bѫe,i`aI 6.<w0:M)`9ŭ- ^*ky=N[J!ITHvެ^y3!Ě^ |
| --- | Minor | 0 obj |
| --- | Minor | <</Filter/FlateDecode/Length 265>> |
| --- | Minor | Qk01@Nu{LNI~&Jvpw?ˢBmB'$780{!n_6P/: TϟJ |
| --- | Minor | $_ڻpmN$ݪhfo\<ZJ)H  53\j׾ROZq@i! |
| --- | Minor | ̏#Lq5eh1H%2HOKdJڎPItGQB2GJ/Fo+my&c;wY+T> | |
| --- | Minor | 0 obj |
| --- | Minor | <</Filter/FlateDecode/Length 273>> |
| --- | Minor | QMO0Wq1|)zhHV	Yv^o?py3y3UQI@'\<!t8I`"A^W}|)}(O8o |
| --- | Minor | !hydEop8;.y"ͪ(I9O&jVHhf@2#('_ՄƯ&3!4ytBac.<.~~q˽D{ĶObdVJN]'KH}r |
| --- | Minor | 0 obj |
| --- | Minor | <</Subtype/Type1C/Filter/FlateDecode/Length 1151>> |
| --- | Minor | kku8/⦯/F94 T[~xRQ@@`jb-:m%mS K,өwa797{s( t96,Iܼ2,#Ms5iHKT2gk!3"~!\4ň |
| --- | Minor | {PTP(v-%%%.I:Y(eFl1JbUd+Eo}uBBYYYRo |
| --- | Minor | ,^ʗfsY(54U䳌3aHb/i3+Bv	2V #rSbL"bQ |
| --- | Minor | [Q |
| --- | Minor | ԗV]OO<9Xd> z2ǵ]u8@8+p8Хcd\[	..Zƥ)U6L.`ė |
| --- | Minor | KXsS.GY#lW5w]<޵ |
| --- | Minor | )2`-mEjn`=}߫1KX h܀k}̳Fz7Tqy&myFF& qٯ`t/HMlVt?*!x㳧]?_!l嫹vxO*;94z0Z?Hy+8%ta/#oǎcrjVˣx$Qr}Z$Wm5XW'rVi`ˣ[D8گ^%/d?V:q><q^-pih'%ڏ9}cm݃qAoGq,ྃOz/i&l	;L&έd_ۿAFY-LX |
| --- | Minor | +QObt~1f |
| --- | Minor | ?Вi&I4D6l|]*Kzƪɋ29")qP);]{ |
| --- | Minor | LQa_]u:ݍ2#\.Ҥƒs8!yx6Z	\jj|s[YΆ@M7PPpht_߽%!YP:# Dȩ֣%:8=\U=M$ztQY~18 |
| --- | Minor | 0 obj |
| --- | Minor | <</Subtype/Type1C/Filter/FlateDecode/Length 300>> |
| --- | Minor | `aa`ddvvu 	|)a9YrL?200|A+)$eX9k'd$g9Teg(h$k*ZZ(X*8e&')&d& 99 |
| --- | Minor | % |
| --- | Minor | 6%%VzzEv |
| --- | Minor |  |
| --- | Minor | ) |
| --- | Minor | % |
| --- | Minor | ~ |
| --- | Minor | `I܂Ғ"Ԣ<D;##~\cˏw}~wrV\7w1W2C jb9 |
| --- | Minor | 0 obj |
| --- | Minor | <</Filter/FlateDecode/Length 529>> |
| --- | Minor | ]k@@e)QGgDKm_$+4*<߯ιP!3_̝}یjgش.u:SQu.`"ߗ/oݹlot,Ǐ<2vGzb]Fw޷NVRiZsz~>·׾tg׎*k\]җU8}kʧoo,_9ãix&S@qL_i6iU |
| --- | Minor | /rA:/n HYF |
| --- | Minor | =1R-! k!1b%!{B⹄S(?ak#$O<ȧAXkLs)LCO+gnS<cYx)CgJC,7r'.VHNU.s0hNӈ;2 |
| --- | Minor | 9B,w'x݊dX\,yXN=#v#7~+EZG-a@Zg-w~saץ:SV4Y)m |
| --- | Minor | 0 obj |
| --- | Minor | <</Filter/FlateDecode/Length 414>> |
| --- | Minor | Mk@=n"$д&lt |
| --- | Minor | .9TPxv>ޙqM,WoU |
| --- | Minor | uEBF9~,oՖ㦇,[bnpT{R/Oǽ/XMW8=r@mc1w |
| --- | Minor | ~Ŧ.6}tnlqJsR}<'IL:U]MHFNMO$vVyJ |
| --- | Minor | 7=l!"H&@+جdX= |
| --- | Minor | zd ڂ Ri2:D>l{8B,IL NbfqM1IT@O`x,[ 1A"d(H[ԥP]2/|	^wV^6^9ʼf |
| --- | Minor | 0 obj |
| --- | Minor | <</Filter/FlateDecode/Length 250>> |
| --- | Minor | Pj0+RЂ1& |
| --- | Minor | v$_K69taYf6*CBFUZf$`4KRJWܲ8q{=BT~_t5=+v~+=Hlm銫C= |
| --- | Minor | JDL |
| --- | Minor | &|IDRͽä}bA<KwH,H\wȲxrEմɳrf~{K+o_H4{	' |
| --- | Minor | )!uEkW/u |
| --- | Minor | 0 obj |
| --- | Minor | <</Filter/FlateDecode/Length 245>> |
| --- | Minor | Pj07b[1 |
| --- | Minor | Ҕ::Ԓ_K6:xwzx2 ٧ 6h'/Z!eغT E1 d'Ʈ|^8nef@y8pY(K}-c3NʶgWkΚ4i&~q@ 'UՒ |
| --- | Minor | '$zaz$eWPuEШu҂Vޯk9͓Ǝj1#_ۤє68.nq |
| --- | Minor | 0 obj |
| --- | Minor | <</Subtype/Type1C/Filter/FlateDecode/Length 714>> |
| --- | Minor | OLp[6B [!!1h0	((b41h؀uÀ+ۯб |
| --- | Minor | `F,F3=x0\I|]v?=-k!UEZ&^zǊ:s's$TBŪP\g16jF6[VGh{gVCDLRTG0&mHo1܉64F[Aɦ1[o771fu`C=8>ԙ0)&]@Cu\ArJY,!9yqVw@sP)˿jvd2VV`bbjer+-^a3(` ±)^ |
| --- | Minor | L&K1Gxwʥ kezJFw!gr{]*^lHj(o? q=`s9ru!X.-Ƕ֖7X:$ |
| --- | Minor | VRK |
| --- | Minor | |$AF0#}EZ͇9r-۾u|7d-v-`	ga2jA>[潦i |
| --- | Minor | Ohs)p"팋6, 'GS4xǬ3Yca+i<A*s`D]F@! |
| --- | Minor | !JzFI>yFU*K4+2RJQ+͕ |
| --- | Minor | =v/ |
| --- | Minor | 0 obj |
| --- | Minor | <</Filter/FlateDecode/Length 346>> |
| --- | Minor | Mn0>	!(*UF!9 !E*2dYtl<de^~AM3zjƛn_Kyw3Ԋ9پV I?ފs?n_Χy	Nw_e^ݧRv#cƹs4~Ӭ|K{ysVٓ g$v%j&U7kynH7oC%n |
| --- | Minor | ")}{x#rfaڳlba9 @#d)SxE3g!iBD36tMwPGMrLhx}8ǔf _)Vz= |
| --- | Minor | 0 obj |
| --- | Minor | <</Subtype/Type1C/Filter/FlateDecode/Length 3596>> |
| --- | Minor | {TSWֿ1{Vk*,U(B"(obMx)!@ [*R[ujXflgWUU7ص5d>#cgd2⏗/]0U\zvRs^g7d0LҘo0lΙEg+yFf\dn陆zOHܕ#:&kJ^35w^Sc"SB.!bGd.)bRSIOOKNH^41^)i۽&ħzrթ^G&S?Gs̟)bZfldBp&0YTl/Ì`\wUf4d^cxznɌe13yLff219<f=!d3^3ibFeǆg#Q~kx8UW`~n>1"ӵm[n7#GJÑV|a}b=7\]%UwvEn:DDL7U;%QzxkLzLn=7WU):#M{,뻷Keѯ |
| --- | Minor | !<&*ohOdի27V,^ yHN$V.z!6&y`rGx(q9?O;xWRb,RΤ-)aLMyWE/q=OF |
| --- | Minor | |X$j̦Oc	aQ.WAkԙ |
| --- | Minor | ܈@DB$gn^r:c> |
| --- | Minor | =6?t<G|,x6$ck,`i@Hc4H#n_fi5vSVّ[XsK.<\݊{XmjRVw|o.~p#*r |
| --- | Minor | [U |
| --- | Minor | \p1]ǰ |
| --- | Minor | 4XΨ]0Jj0&>p*_ne{;P/駷ˤѤp*OO0\ |
| --- | Minor | }V~@VfaRH,U<spg`p,ӮQ뻹G[^w=Q%hA{ |
| --- | Minor | t,pӖ0i#왓zH$GdpB>`݃2<xPħ@;&NpgbiL!|uInԭ"B\aHr*4FO!8ap\%kˢ7x4f`%>9nẃyiT8N~ynU2bHP*\E.֠}6IC`ÑCQ<pRJ+!;Yo'95B9UviW%&kC ,J/2	Cvu}bZBv?|P#?Wp䬇D&@pfL4<KuEaVS[4[!B˷sK` .r3ė.J#4 w0n`Û<V~/m25I6\_DIRDsҌ zW"(@XL_!?xvs |
| --- | Minor | .ۑUp`9!`M*p[AW[e}{r)KzWT,1*hU\b't)JUW~z(T2,&~86BIF\}E{6N$U^ER0gNm.Wv!h KlH嬙OOܽ3&]#@dMts~M/8/izs ->\S_m&8z~SzB\=ՕCuU|&oy5KtD(¦\\]G] |
| --- | Minor | ]q+΄FOLϱ3)ʻSpL}Gtn?]}֥֝%5Q%!pY=>"c͇3j-=SV:E9	kѢ=EV:P+z8* |
| --- | Minor | d@4֕gB&3I읩1h.w6eRcq=JqL--ҁvl:HT_ϋ=\G0'9 |
| --- | Minor | .[vtʫU. |
| --- | Minor | /X{ɴm s,J>L\?7p>#f4Mfg gnf2ۘUJ-"f"[( 0L2Z',M|(sġF6J@HUIB928ET |
| --- | Minor | !h:.<S_mj>'0a>Oıv6n%c?tUդàKу.	dO{)^B J5Ka}bVm/8-xq6Ma |
| --- | Minor | ]lU޵b/mUL8 |
| --- | Minor | .ag5t?lC_ |
| --- | Minor | MSj ǝ, -+̄ HI=ǑjŔqX'OPIψ֦R[	\p"Tj2w&џs?kolπ%z=}[i |
| --- | Minor | /O.?hHGg//L.iiR& Z˝4 |
| --- | Minor | ޹1a~D<Tz-%Qd舂 nY"_a@>5BYp{ ?]$Al:W	&(*2UUfs)OЗv4=7re |
| --- | Minor | %uzW.wXyMh+Bu`uJ&@d2ux$;m	*ZGAI#N\.x<TmqύrG<#eJt&(kV$TB*`WfTd5,bd<O'O> Ց>4Y |
| --- | Minor | '.*.0*(-+ |
| --- | Minor | [8;ł*6hSECSVW_yaR|r{XK)'?!^fH;>M&=|1yJN^M+y"?ק6B%rmmI!AU2$_Kۢ{^.KXh8Q'?K;OnoIG*KFKg[Alm9Qwŝ	/.Qonojqy,۶e[)黂h~F?hޏΏ$*N}[}@2٭9FsщՆ3ʺ" v׳3vv5GTmOؐ}>| ӶrʟdR X$ |
| --- | Minor | RN>5_PEt_^nhx]"Ggk~4sÂ |
| --- | Minor | Lc)O2aS;0<&:i |
| --- | Minor | 3źnmqYM;BJqgct;D@m/]XOn='S5*PB?˔ZQI |
| --- | Minor | ۡyꂦfs󜇺Qߏe |
| --- | Minor | kww׹\57 |
| --- | Minor | 0 obj |
| --- | Minor | <</Filter/FlateDecode/Length 381>> |
| --- | Minor | Mo0;M+B*HUv`:@㪇 k[/VV677uT^~Ǘ{wS=_ZNޗWy8۷ |
| --- | Minor | a 鮁l |
| --- | Minor | xا6gٸHs&P+^;Jv`Zu/<gYU߿(+iVʣ"-đ8Ew	q;=|G&DyG.%rIlbrB >bXC'F'	C˂"":EJ-r	%(\r	̕=,)R=&zTw3-[#๛zx=D |
| --- | Minor | 0 obj |
| --- | Minor | <</Subtype/Type1C/Filter/FlateDecode/Length 4563>> |
| --- | Minor | tTeG%aSJ^DM((e@6RI*Te}}}IFBa5Y"bQe節vvfz99/'{IK1٧w<rr-Ox72Mgryf>&t}ڟ3'p5gjJMW<|ݻ8S	"Ωw͜M͙PAH\,,	kBS*"aY~aLR\QURT&WK/ZhEKVUk$%EҬZ|c,Z<멲I>ayVPZ\P&?DY/T+)d=xT*^#r<[XV]!)zb,y8kKAU`ֳҬ²qUeb@S@Rqs'g2g1"3%g5'L98EN)50fBVF	$\wp,ds,<yŹwqDqc;gdX2.N&vO:x(s䅓ߞlS{n<.c2:Wd%w+orR~ |
| --- | Minor | s^nwvlpԯ3d֪+k,1 |
| --- | Minor | `m=C#O)Pub#y'^ _({.>y@bwgas9icEqf:A|~uZ^6 ٻW`<`=]mHɾL |
| --- | Minor | }H/4Y&Z6nC'Li~<F#Z |
| --- | Minor | @r$Fv{_3x1E3Āl{[/Q J1@G |
| --- | Minor | N/IɣQ@Z :k{5<w,]U.: 	4[M@FtљK^@IqFmW»>LP:Q&ZE=vpM&Ymڇڅ1R9d*ِp6{'Z -n&R6~9}z |
| --- | Minor | "CRפ.1fRKBvklz걹z{:#1q`[-426}E?m k&A; |
| --- | Minor | }p@z[.2yeFP |
| --- | Minor | &{,O-JOwgQ(b^ʢ(AC>DZ8H٭b4(wHYnnMPt1Gj]jGo=={79=YWu':[Е/ȁM |
| --- | Minor | TGc3]`i^e@6gN;b39TAcȖ0o𥯮sUӝ@EIFy<:		!v8Av3S8Ky&ZA-,,:ZIC-C$Ы*}*P]7+ |
| --- | Minor | 2м$:N |
| --- | Minor | gsLي6kn:F mt7 6o,n)4æK%.egh&[UW)f O |
| --- | Minor | =s]"~:1;t^z[eXU%מ4-5adY+Y(~@ގKXa=c"d=1>ɻ-aT.{ |
| --- | Minor | ;Oi&taO}αs(H:Y.;PXu:as4h XD\\|/|i|9|СT܆6*AXu?\ |
| --- | Minor | <6^B^":A.j@P6ZORl6ey9M9g:5#b׋cW'y\ϟ!AGDa |
| --- | Minor | ?=K^CCD3:tXy )a{؉"JjX)qhY^4)I%͒95VA\>XnKc{KCxN\^̶\+4AW-h |CR>81(qࢥEJ jQ J څ^&aP5*4ZXl(=ۏ6< |
| --- | Minor | ؟[mb'ٕdXV,v,Q/x_g\P3W,ڈ{8[܎0*yjF |
| --- | Minor | "/\tmq\!-5ee+(˰zz{lQL~H |
| --- | Minor | 6q%RHf5쬱fIfDSmV+hmxt@ji]A?Aw+LYC/K]V"X=Z`TTX9ǠCP:Ae2Ѵb6Ypav{0+⇨WQ |
| --- | Minor | JqeVҪcGKdjiMB>t@Z& A5PMl2;=4Q}`JʅN9bh |
| --- | Minor | ?5O[qeAbkV[|ٽB73C&P)Ǯ1#V*`;U}46\| |
| --- | Minor | 3ink18$BG n	jʳքiC'5㋱lu6Mfsy$7vVfкMր5lMbd:',kܘ&niy;t)Q2x,âj*kT4c-h6ml3a"&*ٙ=cŀ+WJϘILǾvY->ш۾zMJ2v/',Y *rg!&2Rcћ5%;4P>G;&ђ{QuRe2>-#F<m펮=Íh) ޙW?>)_}4E\<W.ОU?]xXfl |
| --- | Minor | =^aC>87puKԔѨ,i(R/tfJ}Q |
| --- | Minor | G`.+쭪YH\C?]lev$]:8ݸ\F>>qy{ zY=g`O	Ѥ^X\d#e/`i8=_tx3̑[{ѷ]4WԊ=	v<&=Nxsu>irMt@28]o;g2CMΘ' |
| --- | Minor | ;B<ǝ$:c |
| --- | Minor | E{+qC@w97 /`WLpcCw\f.s,ob'znޕD}mХF,Zɷv{kGM-"|Ehmicf2P2VK?dv*Y_\uݝjt*q7y'jiiM~9L#I)3Ж:ŎBc9u-(Bc'Fl3$>z2 |
| --- | Minor | uaX\)kڒИwz( Y$)h$<MS`&Q,y{=OCww[IMV9P5d^O>WdHb~څqeQܢmMnJf. |
| --- | Minor | 0q4u\Ve@ |	ogS"54ttp |
| --- | Minor | .RM6wEuWu	6Bnp﮼:<fj9}Wh3ZO |
| --- | Minor | \~)Ӊm)jJdz}Qsa6|DlhOp֢h>Z?kō[`l?Am[@V^`^ XM6jl3@cjޞym|_u{>^D4݋zJv7?E<g7g@lˣ`O;MdpP^p'46@%^QA8)`yMڸHy{["tn |
| --- | Minor | .G ێUhQU\fx<Fdx*t |
| --- | Minor | |]9>-m> |
| --- | Minor | (ӌJI((5hiJ!"YMu4F=w'~	;vr}̗ɪJ(zYcD}'_yyk͉`ۆ0Q`WU |
| --- | Minor | %O="1t~vt"xZ	݀`Q6lݹWT&߳˜ip9ؙ͒.7#hFWo |
| --- | Minor | 2UXc1YYQE"LJ{,9ѝ9ɚyIL23ѧ3{W |
| --- | Minor | 0 obj |
| --- | Minor | <</Filter/FlateDecode/Length 262>> |
| --- | Minor | Mk0sR,JAW<]-& |
| --- | Minor | $xDC;3ATOXz!I͆!t8I`v|d#$(T_|/ZZG	p췎=ov,dց5 |
| --- | Minor | |q9VZBH܏8iP9 0sK6E׳j8dsr\9IV8ݸr\l\'Κ3l6fpON*y |
| --- | Minor | 0 obj |
| --- | Minor | <</Subtype/Type1C/Filter/FlateDecode/Length 884>> |
| --- | Minor | [Umإl7]\Icje:\]NiDd]Ҽ,iL6ۼӼ47iڦMbk٤ۘ8g@e 8'}R7zS?!T29}f!Rsy$k:xJ?+%NIVtBxf_[eOjH<O#AtSGSM_&]14׿{N:naf-r_7իSohSC&BLL{28VQZzOՙln5Z5Li=F |
| --- | Minor | ud6]p؜vQC1e ]$&S_'hGD;HD7q}>l| |
| --- | Minor | )48jy5/5MSXֈ&A^VPRʸddb0m=ԟDKQ6/"Y_@9 |
| --- | Minor | ׹y5ؚUUP{J;<SUh|QȬ>/ܥ$ |
| --- | Minor | +זʔ.`Ԃv$u<e\,G!g082$X`s<H Y(阦'?Md=1/RKr |
| --- | Minor | )6x߸aX_̫1qjU̱lx>'2n&Yq |
| --- | Minor | ̉_扛; <@133#rcAL1*6'_GX8)yˣ@*E'韱%djۆ*u5$kQUSGaeT6mP%5HE%DA2x\L%>z͗wԙ| D!VW2`INvJ'iFgcoP~t |
| --- | Minor | 0 obj |
| --- | Minor | <</Filter/FlateDecode/Length 234>> |
| --- | Minor | Pj0+tN	)Sڕ:8! |
| --- | Minor | =`='Vb/@#tꀣBh7[F5Q |
| --- | Minor | Z?t~.@cwg\f]so1 ls@c3l>k)aAc0͵j2Lp@JiTpJu]_mUba2|I=ܩ)enAv3y*?_m |
| --- | Minor | 0 obj |
| --- | Minor | <</Subtype/Type1C/Filter/FlateDecode/Length 351>> |
| --- | Minor | `aa`dduvu	aY4L?200OAC$X9J |
| --- | Minor | *23J45--u,sS2|K2RsKԒJ |
| --- | Minor | +}rbt;M̒ԢTs~nAiIjo~JjQQ@	1012{Ϗ=3~o'iyrݝM-vA |
| --- | Minor | w;<ϴQv{ʞߪ|L?t߱p}<;r^9.<=<|?D Vt |
| --- | Minor | 0 obj |
| --- | Minor | <</Subtype/Type1C/Filter/FlateDecode/Length 527>> |
| --- | Minor | ?lQqG |
| --- | Minor | FI_Ÿ4<bzbCk)'`LK]QD4&]4ws`s|7 p KXS+"z~ÖYrФq$ǁ=ڜ=Fl܀qĨEIEtMK\$$g(NEq*cp2(a4T9-`\r(/iYsJZFZO4831Q*R~1X d-hK() |
| --- | Minor | &<b>cJxSC*+ |
| --- | Minor | & U9 AWu[i{S@'񰊋4p߿wD[?uw@(_:[5o$c̬=˒ee+5$ͦ'k]~E]fQ:^~]bCVT	nwf߇^vI07aofƳ{WɆՖw|دըhДš;ok6uP'aέgf`׶nCAح?C |
| --- | Minor | 0 obj |
| --- | Minor | <</Filter/FlateDecode/Length 266>> |
| --- | Minor | Mk09n)Dht-{LFX$:goXe-[Kڠq\qSHTg>ɈmOEDkCnm_Y&c-z	Y z2z+>ܗf`w-ifn80yrT20"9d<@֪D;ӛUGQz=+{:+U1dOG?e9.YkVv+\?}r |
| --- | Minor | 0 obj |
| --- | Minor | <</Subtype/CIDFontType0C/Filter/FlateDecode/Length 3247>> |
| --- | Minor | }WXWڞ&2n3t&ZVRXD-تA!$\[BN10\X*vtuꢭOmmmt[ݮ	w>L3y9{	OH$M겒 |
| --- | Minor | &}o |
| --- | Minor | (XB$O%fAҾ q3%?.$AH[4['u9i"ӉD(1x !%_T]z}Zk0_*]~}FƨZ_TrjCR>]a_*I勽gtZUZҥUޠJr |
| --- | Minor | "T4UNO%>LuAզ*Fze{6Z֨ڔԪpʠV4Fcs#ti7ƅ-|UkbD4^6&ed"~鳒2	b&xOEoD2Hl&b6"H$TBCd{,"[*R,^Dl ~KrUARN>E&d)O"06ԹS~'cJ蒎ՆxS8\4&#[̶La9㟗w/=Iُ9^*^CܛBQNJPUC9l&<ua0*9|Lʅ1X'#>᩸rWo	WÖZS<i{7U?nJTSC{,<qd]~cEKGX=IsxP-B<0#V2uzKg |
| --- | Minor | 8/	8QHzی |
| --- | Minor | 5*<#ޫYXc3ϯOCoLF6Mv55s;/3/'e݇ VZƥ0Q 	~ߛs@){%#vA+𔗰?~"7!o#ڸbFcQGASU*`_[A썹$'/=8Q\?PɅ./T8 |
| --- | Minor | 69˼xo	:w_Q[L#r`9uՕYlelj<0S 'Aȇ#wK`uT |
| --- | Minor | `t<=zٰ˒̍˨J:V=z$BҢ}lnabBfLS9reoo<:O\\x(!A#7FxV$tᣗi&&'7[q<+͏fRe:4XXNT=RaE&pR&,[~]`/#t$R'L UTaVCI,My:X5unKE1+y8zp6(xzo-IEN |
| --- | Minor | >1pY=hD#[a21xIyy/?mg<x!YxfS9 5YQD&%>&PaXu ],Oa	'&HKp,w |
| --- | Minor | '>&悍P7(HrrU'p(ĠRȣFpXD5	Ԁ5+Y2++Wf;cwW5&ya=:viP:	B?ARʚe3șeRglr%=TXQ	7Sl11D/0sTzikѦLruyY{9ZQph |
| --- | Minor | ;p;Y[.2)jT 6'ܴI>V:C} |
| --- | Minor | F6܂QF+*D	_*c4rUS1#ڱJhIҮsj{z('5r7vpUH=Um;M׀FyX(y;SG#/P ˫Q|ڻQR_GꜨiBr |
| --- | Minor | w>E |
| --- | Minor | 6?#F(pLÁ0WA m]]jd"f_~.B*5pU9ΝL:/s㇩Tj~pOQO7)o6(%?V0E1:XSi,%w?8ԗ2F+S89GGyKmhj |
| --- | Minor | -.+Ar&0zST9..1ʫs76XÖkeCQ7ZƢ?i,6#O(Ö"e"W4\k~Û"ra2vXNܺkUL.m<;<CCP89#6LsIkKSgq$=<w~<e_ |
| --- | Minor | K.{UeEU],;P)w<~Kmy'UՙG}mDvw3Va2%ȼ	P(DZ̊].66Et_4K`FoȗRuW |
| --- | Minor | \/KBt$/sq7GȞ,RΡA7{W>`a6Ē |
| --- | Minor | ^	<ұ!^_\qrX2GQXQQ)ٔL!:ǜsjDSm:(r&a-ls"W |
| --- | Minor | /om)sىDy&*Q2ۨOg9>ZQ nj.9z_&v6|=DrX1Μm_#̝BK{=VO7P1;5|sR2.)7UYIi:dY١{/;]*Oej |
| --- | Minor | ⫍:?~}ROprB;lF;tM])ǿ!ςg%K"(=Js/׋"UpM;G>{gm+/6@TmcuvGhz0@iVTX<8Yт5q<5J$O~|ּMdI49jjżu;h?!EgL\DI,.E_74P둱tASPT>Tn;!wP_zt8Aֺ |
| --- | Minor | 0 obj |
| --- | Minor | <</Filter/FlateDecode/Length 23>> |
| --- | Minor | ``p0T\"ѰI F |
| --- | Minor | 0 obj |
| --- | Minor | <</Subtype/CIDFontType0C/Filter/FlateDecode/Length 5385>> |
| --- | Minor | X֞DhC13n |
| --- | Minor | w-A-BXEd-}dA"jk[꽭Z{mtA-3_B73g")H4zug.фۖV	ȁ8JErb'K:[wcxɴQ	%m{y^ wd[0Q"JJ䔂5tU1!1/{zYٝ|s<wj0M6,DWvWsWē&RTj(cZeP&vvrSpVSjm26? Z\gK\+ R9S(cbv䮉${მfz~̵._=&!FVĨCµߟ(R㩉5AS,Ej625zGͧ^RʋZAVSk:j=HP-NJE)?ʟ |
| --- | Minor | * |
| --- | Minor | "( |
| --- | Minor | *J#ГlAgh/|6w=Mb{J"ЋB! |
| --- | Minor | ;<dx[#F#h/F<lvht1<swr̴5Z*orTdEkaG22qUe%f`}tq9(MTI?@MlHW[ Tsј |
| --- | Minor | #=3ɾ^ƶt |
| --- | Minor | < |
| --- | Minor | ,!LFaɱ	D)V^TYpgGȚnIllniΨSQ5{#`/;'H?;C<%uIj |
| --- | Minor | }a|İL	ч8~1$HBM˱JQ |
| --- | Minor | f>80?x~ +I캐L汃Amr[÷+&P@3?Wefa*^֜bxAE]$fT=gc,v>|p[+>?suqYRe|uXC$]rcEKg}V/f~'@4Ё f |
| --- | Minor | V;!SҒ,.!cJ q.鲐^99F+4Դk9b¬ -dP&$;HУ~~'MG;8m5ٗ"ZDdF9<kJ'M |
| --- | Minor | ! |
| --- | Minor | <|o6n{Y,vzMr|_Xn0DۢrO2n'.f,4AWlbSfc%ewL$K33[xnm:3q ue@őfN53߄:Z.KX	KfhVKsP	fVcyoDBE/0d.|uQϔ]%؋292Qⶲx؋<0壆[fOr'cGSO0N%ɚViKZ;ee)·3vB	3[pxX-[趹c &rDP+ǗhLOu_ݱ:Ϗ^Nm{MlJh(d	M_ ͠4- Ap$&,<.?\2;s	&J`v<Yא?$q߷ ^~wyb Ll^yhc-tmte<Zi*1u޴=q]-k[+:9gvXj_0;u48 |
| --- | Minor | .+][8F3ceP5hSu4C9(-cv'm;Շݸ6ޘcaSPw	(PP\ȕv~-E.kn510"4qۜ/HQ.oa/#pH@d'4:Y@kq |
| --- | Minor | ڛ^b,"4=BGH&H>#L^{Z4<ɿH),L'U~qqHma1~~OBbpBUX1Sb6*?^	k{o})ߺfw"C*HiV*Jʸ	]])|Se}A4'+'{"<ɷ#9SHA>>ym:Z;s̲TteTD|yY/r68uO,.R %2F' |
| --- | Minor | ,``xԟ	!\03EpB*æ,"C@ {dg{A |
| --- | Minor | +'j92X#*n;{p-RC<8*<dlOASUOE ^EPz5?FV, I>Z,4~ftOP#{䊭緄_!GBuNY`VY` |
| --- | Minor | (=)Rr<'qqiI',16*Q>ëٙ:W)bAE3?#,id=]YZQV[3`?MO	Wm'v#)HHWFQ.+Y%pE	_boY!OFγ[ǜ$<|~Fn@ݦHV<8KGq<ΰqqM:rkX>*%Bu_c:#Zp@C8@~A`~q |
| --- | Minor | %>t=g#x7B-'-Ѧ97f?<=m+VTaa~k̟w\ѝsO.k2&|Vƃ9#d!Ia5 |
| --- | Minor | hD9|SAL[_4!Q_L8Ġ/cQ~/ܡk |
| --- | Minor | !f+?uB|+zqxyFZ]5e8	s	q8߭#{VqM55-uaQ{v.gr!cʗGuEwJ</0UȈUD6	S |
| --- | Minor | ׀F#<ϝ3;{f,{8rءX |
| --- | Minor | "SKdWu+^{¾׺[s?|*Hr-WHKOjI¸5bTՒe7bY2A |
| --- | Minor | %(749P38Ҕ+u<vqZb |
| --- | Minor | 6oZ`28,V>|2o78o1%>lwfz_څ&:3&< |
| --- | Minor | ^eJU{& |
| --- | Minor | <~|;R|H |
| --- | Minor | ]L1Y	Zt*C3Fpa#??w_>c{++<Nîɸֳθ)VӍ/8XD>:sF-)Q|s]XB8+]}-SrM9x>C+y |
| --- | Minor | }}?hZ{dk!^j[6|f\M0sɩ{~= |
| --- | Minor | ^;/߯{E |
| --- | Minor | \e{~EjMW9tN&n,plV̟=8TW'-פ٢PŽgc(7C91<&.`(*JJ߿'L(aB͢tNl);X䍒E5`<3AqXC{Ԍi&0?n; cbfY<==ZxmY[٫e |
| --- | Minor | { |
| --- | Minor | 󨊽 ϕ8^V'-|lY$xc |
| --- | Minor | +KՒPf	,}*YX%!/)[ꍥVB |
| --- | Minor | \Y%*Tr|7X!.*FF`yqdwU |
| --- | Minor | ]C'M<2~ |
| --- | Minor | Hё󜹶lukNt=٭ji9l:_pJ+ c_ǌAO\}0K6E |
| --- | Minor | }#4*'pDNua<'N4-ԅ_$<]%#D7iT8+"Q~HHOO RaFyڗ^V1dGM]HC	G%.wcnx6߃f:.x; .'ayT |
| --- | Minor | ;?`F?Rqkecyޯu2puiǶp(yEDdoBt}>['Aي=wVhSqrm-EGM~Hxc2p,0aDʉޛ&ؿ eH1}uGP~m͌7-{뎶֜6ׄqۻj؞EKO/NKGDzYn֡'4c^1ze7\gf~4z-iMt^0dJQAg5f	zJjk0Y$( |
| --- | Minor | ^_G㋊le1)JE\W| |
| --- | Minor | $\&.C~KFbMcmVB4XȵcldUiXfu'B!ry𫸢 2+F>^;`9đKQkSߠdrt|ͺ?,w' |
| --- | Minor | ` |
| --- | Minor | ؋F~ݣ!WxO~nF-[[PA |
| --- | Minor | U{'Hɲ@R'.+)*xb |
| --- | Minor | 5ļ|V:s( |
| --- | Minor | 11U |
| --- | Minor | q |
| --- | Minor | 2򏁤fj믑mB,LQm>$Gg>ENN>/| +  |
| --- | Minor | #RZfThh.mS5ڸmyA-.+RL#hdF*dTptS R |
| --- | Minor | Hr79"ߝeôe5|tCR%(>EW |
| --- | Minor | Բ-[mAW*gչa嶭Sk{D%xqY'=	H#KZQ|3O`6jquӑ;ޟ%xFOo |
| --- | Minor | `9ݐ?O/o4Ô	EfWǔRv*.p#7i# ٔk5 |
| --- | Minor | %yK |
| --- | Minor | j |
| --- | Minor | 0 obj |
| --- | Minor | <</Filter/FlateDecode/Length 24>> |
| --- | Minor | ``.x_E㛯\ 2 |
| --- | Minor | 0 obj |
| --- | Minor | <</Subtype/CIDFontType0C/Filter/FlateDecode/Length 6179>> |
| --- | Minor | XW.TDh.j |
| --- | Minor | [Ơ |
| --- | Minor | QMo"("JK%N&jB1nqɼyP&&D"z}N}VXdƉ%Q5H'LI_>e-_amG6$QÍ"2O>Y61lE$)5RPJ |
| --- | Minor | $,	oPD@DiĆGf8:Μj<rZ#08:<0@Z5MzjMp49{*xj*27,\>ij@*:8,PE|wz"||T6lT-P |
| --- | Minor | ۫Tι*~ӂv=6;_vF{w:<-"&B38L;|c?XʚOEMPS){j@MfP39_w<j!ZL-(gj9ZIGP5:j=Hm\)7ʝRSMm|(_ʟ |
| --- | Minor | * |
| --- | Minor | *b_$䵐ZhL	 ݒo.ˤ&IY-zh7t'H14thDf |
| --- | Minor | lËQ<W2fsjK^Eȵ#:n8iTZ+yo/VEKz?)Lq^LV)<$KhSQj96>Dc@HYxɠR~ʦQ'iy|R8FrhjZ0طX`9O(}=*VB hxzl~`gsL}cS1.P{@/d<A$MϾ:Wq)yE! |
| --- | Minor | }an;O 3O8K-P*HF9/</Q>-WSjGs?|c'Z}d;B)WD |
| --- | Minor | ]$+u?6$){Mh[9+ +&D| |
| --- | Minor | c%(:.;=ҲrSMX;yl5R6pۃ<YgsI7ןj8ς9Üy[IJ\{Q-́hEE>n_2qXe̩h3w |
| --- | Minor | @]oβ@3U|A^3xr½e+X$썽C7s5vVB0FL1+}iK{yv]"	Rg6ƧG%+lc*%ƦxSa}LsxsFkp~qӿ˫ٿ&:G.KR04*> |
| --- | Minor | ׎z3M%\bM5iZF`< 3%GI(^'ogd]<+$5p}fۊVɽn-wŴD)>o dY%>)ЫSQ/f:n۲9{38<TѩF~+,	SoE,6G0)t? 7`6,Ga vBzZx5By|% G%^SL̮sJxA4CpR2k4rHG0Q*&<Šx |
| --- | Minor | `˫Q}|Nײ,5ʟ'l |
| --- | Minor | NgW1mk/l`ap'	mMrT |
| --- | Minor | [q7ZO\Tx1<g]OnNKxPnY_?A |
| --- | Minor | +xqx}Y|^pQr޾c~3w~\EaǢI2I\Gxp` #0ƨbDg:viOf44MSH@0z!| _"!Mzåb0ebr5 |
| --- | Minor | Y5mYhaЗyYY(=KHJQz5nCXMw`my>|Sb1x(Or9M*H?ʂc$ju@U.r |
| --- | Minor | ݋y|E22sss#4sf.YybKFCM	׼}m6g=̍%%ZA.3a]%$rwejl |
| --- | Minor | ӷ<U+$6	␁n98@Bn2l`cKǠ .!4PΞpe+u~`RqX7wαg43u&`(8"i>rh[A_GL}i0yԯůr"VTCqfߓcB |
| --- | Minor | +fۛ"`ͮ(eB@n)Ev~1S<1ڰMaC=>Ij-Sg3,؜{C;P.(Л'k̐غNUlC+grŐɓÇh6d}~>HlUT`y#jh6 |
| --- | Minor | <0E:$E;	y^$s(7=9Iwsm%DA|utZ>FEmC!MmvSFr:x"g~>)^_$Zf.2LRp$+̍Rю8('ʉ'!փ!'~ȉQEt[ |
| --- | Minor | #6բ\NF.O+F# |
| --- | Minor | !vf$~TPʪl XXߥǫ |
| --- | Minor | ˗HihN{diPA3&%6F'C'ό\46=lK7#8ڋظF |
| --- | Minor | qڐ02*LH5mJ.I2уf:3OC7TfW`y%Ze2iN8>m9K?JeGO)qx^ڐ$RXx܈2S1"ei?6 ׉ 5j 4_u8n=v0os	䁢+BWVE/|$IOAG|px@EoO/C#'܏ZyT^7hHe$o/c |
| --- | Minor | (rYk9&I0YlhX&Y#ԅ0qgAJ)VbZ=Sו(C0dClA.pjnC5waoJ/$w`aclux??q.Vb0YȹEN'p>q^ۖ~{Bñʣ||C}WYRz߇<I:aTW^vݟBM3	r<Rҡq`v09lU0 =Δ厕f+Fwe(552Ia(actMJG6(VWK/}Ř4É~i*$=@쥽bMrLo`ۏ\)D@7r-5h*x@h`ke$É2^+)bݱ\7wM]}?w |
| --- | Minor | %w_^K*<yjtnTJqIz}q1~6lI*Dz&-q"KUyi_?T30;xPR7y%;D`qJ<$'߯,gs |
| --- | Minor | r3)|8uæ&x,Q쌧+7<R.!AKS&ksK+-,rZ7@@Evk!cW\a;:_Z"0lf`|.=^W<P"mB=a\[oĄ,[)4"9LTA$rk]s?_X!x.Gͯ^pҗDi5(_<(<UU'7gJc4kֿA6ߘ'?"4JSEa&<Ƨ|{ccW)>'<>~ =7nyǟkFL@|?qR"O\9Z]	qb~æd3!1 |
| --- | Minor | <̙D;Dp x?RF-̡ 膆v]N\{$<sv,Fَ |
| --- | Minor | ?RvW=غDl |
| --- | Minor | ~Oyʺ֭s'jpxTF[$aL*`Bm=t[ |
| --- | Minor | PV$4<^EtrY^FFN.% |
| --- | Minor | )w`)Ed,[oBM&F	*Egt!Χ!0{AΜUTEk,.AO{mWfHG1>\Qv!q|^W.v@Bow&riihk$d+vEl#LC`kQb=h"5	FHK2Q|SyEE_Rc#cb#M`!>e8#py+/5w_2*Xi9um50Q m<cVFn@r䕝99\G,s6K |
| --- | Minor | nkk}uYu,	_` |
| --- | Minor | (ylEKl7pMvFuqWI) |
| --- | Minor | QF?[5k |
| --- | Minor | ؞9T.Q{xKʟƖi`C"0DKP|vWCת9h [5:qԏ7^6'/ЬM` |
| --- | Minor | &݂m_o'E0Tz@}VyEW8<t{CZO6;|"gxo>ߞKәץ'r")6qL+uBN$75V%s:6ZPpވ D*Ueg pL)aTjۛjIZYl'v<bʼkJ=~O%4W>]4V,^y=l_"JVL| =%$~D |
| --- | Minor | ;nN8+{iב?BwyooQT/+Hz/H{SC,vRCB_QmNm}8@@"| ?~LCId)ؒ"TSC\Vw%ө4J@n w ]hd |
| --- | Minor | 0us[h,_ai,|(+̹ƚ[ |
| --- | Minor | _cm!6O<PRm6SF0?EH%ggek3Kyp]'K1p[N[B^K6qqB]8;n]V!Q>$Akex^}܂Hy7ʘ@x |
| --- | Minor | }I}Cdq9m+K(|plौYR{Pm/IxY*~3RXFa(;iZSD80~$eĀaZ<,ߤu,&u6:6&+!21g AxG-'2Nf."9Р |
| --- | Minor | $DeZ"_o\=2p2voސeV7+	/߹xB=8`D6-bJIBbTn) kF'Mx@jLHy!i{]a6T'E?>==*_,Kwq(s`[$F-(Arq |
| --- | Minor | d*UsqJЖc |
| --- | Minor | =bhm|`ͳυ_J&ߴ'%=_,lg;?|T"`	&#LhhSo̍?^ZX62@|?Uȹ!&#=b0̄E̌ٰa$8 |
| --- | Minor | 0 obj |
| --- | Minor | <</Filter/FlateDecode/Length 28>> |
| --- | Minor | ``0/|^7__0  |
| --- | Minor | 0 obj |
| --- | Minor | <</Filter/FlateDecode/Length 26>> |
| --- | Minor | ? |
| --- | Minor | (`Q0l > |
| --- | Minor | 0 obj |
| --- | Minor | <</Length1 94333/Filter/FlateDecode/Length 12796>> |
| --- | Minor | |	x2ٓɞ0$y!̐E4"DPH aIbf"ZpjEYTVe26,jjjpJKZ˒Λ |
| --- | Minor | ~x˹{ι;EzR`O@QE"_Ҿt	{" |
| --- | Minor | %ۯ-&JHxoJш_ڌ#P~Q+ׇ.`|hSϊ |
| --- | Minor | )ѓOʆۯz46b7ZV6uDw4Ī1ƨwͤSCt+D>TW",A|T͘yLrwVE,IqOeA		-;X{y |
| --- | Minor | F2߆;i:[{CշowW'sؚ<zh=C9m9z<8-c66~cfe^@'i |
| --- | Minor | #MJ֪ǔ)W,y1zx;YȰYnkifԍggVv7]]<CUI;ͨXI |
| --- | Minor | ѽڄ쾓t BmC듘g]&r=ED#ounV]T |
| --- | Minor | ;ZKnI^]B'	`jEZ/BKh]ӓ]Q^K^ݯC&-%S&''"ZKmaUհcNz^Q(lxa>%T6Qf7s |
| --- | Minor | ck/,!s]}G0HjWACaB{EX`p:Mgl,,SQ 蝴e+Z*ּam9bﲷT{}B%V~_.W^wnvg-|-A{'ͧ0Zگ\Kz-4i=TcR1E4jD,p;uGJI* |
| --- | Minor | +ڷ |
| --- | Minor | ˝Li?v1Z}UTI_06qC<NK* |
| --- | Minor | <I.XWvZ/XW\ |
| --- | Minor | +ɹ2|ۀ.Xw۩F5GuY&ۭLrjj{\p9C#.քn%~j{tű e, F'dp~@;,8ѽYÎ| |
| --- | Minor | |r(1u9YavdkRe+%XEdֶ0?}~-apB&pG{t<ͅVx]/X}OP~)၉	jdW=^y̽U٠r@(a*i/_@Bh82}2~e9v!A8r |
| --- | Minor | ,J |
| --- | Minor | Cu7%pLz[nqσx{`Ax_/ݥ(8etzDq3[{7OH9e-Nm |
| --- | Minor | ^~T&v-fz1~%nF_sa*~|潇^bλ_SVPr|U_u-d.]7i漏Ǖd'×dpG9%`]f6ܕ赾O;=󞯦UJ%=rKe'74F݁2	ށCTM{4M8K-v"D=N)XcC |
| --- | Minor | ۩w1X-a=3'!#eEk(ecvJd8WᄘdھbB=3nzXn>WWmڗ^]"Hm@g8LEJ9G,x<8S,sh5M,XZ2 ?o|c19Gٳ2)I	q֘Ȉ |
| --- | Minor | \K)\K-U+VWu>ecOw(ڗPSM:q>5e&:ϰ>-/khUi6^>嵙6.EhYkPi\꣚ZN=}2Ϊ.~X耚uYR+|MU(,}275ȉ(xKO/*+[`A32f#+TvemwDx)$*;<5Cw(U |
| --- | Minor | ⸺\둱Wjhl;z&B\|0Tg)0Z|m4svcEF{cÂZ nR+FV\*Lo6+D]gT6](sz |
| --- | Minor | <HXma嵷g+}%OljWeJ]]PwHk&O)PҎ0Xi%nxipkc[hY0.LxAO4ec2eF&ԻF |
| --- | Minor | #bյ	pdsffRcWW%WUFà|G\s9PQgVWn.3wBoF1$ۗfsgVV}JyE'Rl'f)?aڨz`4'sW<DMy11U]]Uvo"awuWWwWb3hUU7Ip2Y3UFsCj,e7fs!|uYZ8lF?Wzp |2CZl"\E1&Q+[fA +Zɷ-B`٠E6?p[=o9ߒ8o^oRg'<4bq3_^so|ekUbs\S|ёdnmY>mJaGm댟`)>	824t4*˃!}0*2Yy946H,2V/[P>6΍ƹWͪvC^T>C*4FQc+,Ȍ͌F |jN9'dsAÖ)/R6[X9iiQqI	=j+,7.֣tL@(ah^';II |
| --- | Minor | ^싊 |
| --- | Minor | #-		qfOĤԴ<k^jYNv[{\Ȅ8Rm9`YԣwY!V=$MG'ʊ㒝'b'O(/;(6Ι_[_@!b&;y`ע"H'$^Oad&c3K3CFjNsJK'𸸒LNIɥ-!IjfIfN=5}rlUszׯSή#3[n3N_gv=-7~}ޙd3m/x{jY3oǽ߳Xug;e |
| --- | Minor | ~=wɦ=Zt[w/6F}K.WbHr,?/<,,JMJʈҭc=~r^:!0.1.;5ZQ'E6lԺ(Þ=VSp# |
| --- | Minor | @qI1Ut |
| --- | Minor | ;VðSt.틄󅡹 RTlJrp~	:!{tg><2:'kP<L |
| --- | Minor | {$fX$$)*ն]Kh:S{曪Gk}1.|7_;/;QvWzݙjԳlcoPV^7PT/~SyH{oms')b)e*)Q	e9	|c$MwO)b4mo7ymJ./eGJv?_\^=3R2>42aB5\uǥgbMY,d-!¸IOt` |
| --- | Minor | ĕ_$G-'FG''$);Xo5s$}#<Z~<D1b#X{Iqlp7߱6p{>cOdO};)e^zw,Wm;M}쑇>v?~[fjK޲i[ytc |
| --- | Minor | {kkٶmd[zOYsoYzi$s̔[ȣ?{ٿ~vc̔<t֊g2ZW%A	$H A	$H A	$H A	$H A	$H A	$H A	$H A	$H A	$H A	$H A	$H A5@@	$H A	$H A	$H߂fi	$H A	$H A	$H AeI(QD%J(QD%J(QD%J(QD%J(QD%J(QD%J(QD%J(QD%J(QD%J(QD%J(QD%J('H%J(QD%J(QD%J(Q&QD%J(QD%J(QD%J?#z]G9$O0y+(Us8  |
| --- | Minor | $_5 |
| --- | Minor | /ͼJ6H}3oḣbAi*ƌdyk>yJCxȇ	r^嬙gdhyyJ̼6DFfB#|XkCH6aGs3Nd}f>Jw|$"R3MK |
| --- | Minor | >|z#Z!<G>.UO"(' |
| --- | Minor | }-61Wp̴!2C"?^C:d!-K[-745 |
| --- | Minor | cq[^cLX,_TPP`.i0fy״7mm |
| --- | Minor | <ýb!x&OSǪFTv4xh |
| --- | Minor | [7+0j |
| --- | Minor | ;Z<-'o`ٌ-1YMK;W4tk |
| --- | Minor | 2Ȍsڒ&sXm3ִuf,XٴrϘm| |
| --- | Minor | mM+=+r˚PoLkK `@K:oX <͝ |
| --- | Minor | MkrVhXdLo5Vby3Z=mlo*m涕 |
| --- | Minor | yQtQZAEEQ-C3`jɋ6fxZ ߊr-A:C !#z!"F4plp	/J-u)t(-B_i@M |
| --- | Minor | {~|v)Rː>L\HwEGPC~U@bn0W#jBr^HN`1 |
| --- | Minor | ^|"mq<+hY<WJ7ϡ+X)l|W6g6omF|5Z*f |
| --- | Minor | z G߃us\πg;Wx[x<8Q3Ms35 |
| --- | Minor | +V,Wk´C#FتCFi>*IC1g W!<Zh1cm4gY=x$yQgC>㘇`<g<aVBaY(tk'Fހ|.+@D-_EE}%jf#^6s(ϥ~ |
| --- | Minor | ֋z3C`ԅdg!N>nw<y+?=;6Z5$=?OpwAMx0=j h{Ix<rٚѾJxW921nSԬC{;rXaW.n!<!YxMi5GTj{8pݝHynt |
| --- | Minor | }['8Gυng|n*N~6pb |
| --- | Minor | ;mp}R\bj6jCo{P |
| --- | Minor | 'v |
| --- | Minor | kht+A޳wG+K\xt	UW9>8V#~57*5As~x=*{kk}<n%%m|_ |
| --- | Minor | w&Dqw|Kq.U# ڱ7DMR*SU:]Q εT8ޫDԵgGhZ |
| --- | Minor | o?G*j+E¦Xi~+ĞlljdnSNYXǼGko8=,.f|K{]<y=SPCϴa=%<CbÌj.k~+uy |
| --- | Minor | =<uA[uE&%gcS~k}%,`Zsh |
| --- | Minor | {3!"4iעUfHF3o^DÚ!n$h1$n«=$J6(vc0:ZΉ11R{x< |
| --- | Minor | *n!'P:n l+_La-_P47a_tP..Btx6 |
| --- | Minor | /W8#Ϊ Cr |
| --- | Minor | ~dIk֮[N];sԟWFɊ6$[l3[>ܪu/-ZΖ1mS/H tt H6L&BJv"Yɒ$M	u4ZAhbMI<5s |
| --- | Minor | qX2Rwe$ToD@9ʒ	ʧ44 6ZrЫ	' =s-cqKEiA7@K%կ8\=?2yb$a80z,IO$c^%Œsa(3郢Ű$ |
| --- | Minor | <.`	M)'fIc;R%ݒAhK |
| --- | Minor | ?.鎳(z/iP%LTr2)?Fi )[':'O_OR8I~\0[ t`{q@d4Vs<.N@sE?H'UVEֿԿQ}Hqn?C@5TjYȥ$p?D5H}G 1aOtTOuA?`mfxmN%G?`MpVOC0X;BNAA*DַbbS9}0bis`)׏9hp_QS}KwIwS0#cwT%pHtZ:g3md-m4Z_JT |
| --- | Minor | ~H}εeS	FI]^GtW55eA.GǢ~~-p3Y&;h/@f6ay .F^sޤ_{y^O7h]mQD%nDEi#SFG@" [a Gr h2\BOå_⇎\}~P_O,\hUi.KtzP9T#_|7|}~ |
| --- | Minor | EZV |
| --- | Minor | +)H7#`d:ucQ9zvPod(E8f#݉TgRe>8n,1]PSHyz>쓮gSOz	z	>L;I7h.0F(+A$^DlqC:0bS?}ޕ"2y0$=RuWUzݩSMN10t 	挧=ZBj#5:8?Ԡ`{l;Q |
| --- | Minor | \[ߣ5pO<LE"݁iYR"ORjQHjZEiվƍE/jow\{?*ȌL33V{?[Z{AӺvM/VwH{Uhrhk^:#~BPhS1O!~lzIӡ0vwv4hN=Z72>l2@ACGV-,`# zsi4s@JQ@\NzNFG |
| --- | Minor | S*zX=X=D=:zd.Fiߣ@Ծa >IFpiփtmLp۵{(R{ 5͠ (B{A |
| --- | Minor | =m6kYq>y{MYi5wbZبE2rPK{S 9 |
| --- | Minor | !y7M76,8'c;iN9O@TF;N{2E:ARc7_<ݤeQ |
| --- | Minor | ~?6mn6[Env3qmv-݊e͈qhm\ 	-m |
| --- | Minor | '|-x |
| --- | Minor | &_c |
| --- | Minor | jhZ+\kCrTl@XsV렵 5l |
| --- | Minor | @VrnET刅5jKK{'"7_[KPj-5_\3Ra ͠#0bىt/-1#hz(5`XB,b!,D j,bvڣ]^@ |
| --- | Minor | .yDDu:6?fGcGZx	n><<{lLC,?^,A |
| --- | Minor | *j	SD)"L}p+$Xp>U8*OJ̈8"|y].ڏf7[HUbԿ}+[Ib_D[&Rݣb*ҙ6N^"Ij7yA |
| --- | Minor | }"z#~>`#h?0/cL~@/?X;>珋wR@Qo!dry_$ |
| --- | Minor | ,g;\~J#oK_;#6j"cqYk\}VBay'<1e|t;LBR\!@yzL's@[AB4E8?wG(N{[r?Wd~-.R<'G 38ǑtLŤI)~C$e"Cq*q_(EN|˫M JpRR=oS?,> |
| --- | Minor | <:\0B*?Q£1MR}G@j3zqPH#t"e{w{d^pGjtLg3dF`W |
| --- | Minor | )38e?.WG>(R\sV9\t?s\TSfkQRef2֌_'@	yf&\LAe |
| --- | Minor | G9l<s /h=itCjJ!7")eFӗ/e:?pXJlPR@R |
| --- | Minor | (jk/0}x gsxs=  )\@ 4*aV	E$&!\_fv~MqGk=cc=cGt#<=={hRW9%<tU97iRN |
| --- | Minor | ޫIl)j)W'$pNëD|Z%)H5MH41B+8p^o5yYPOy^򜈜gEYeπMɟT07 |
| --- | Minor | T(hr[h*H! |
| --- | Minor | @ 1NTFm }N#GR!VVW0WrW^j3Yaja |
| --- | Minor | !`7w8nF$9]lw_xݎ8݄fa1e~[>̷kfl&CoVD213ٟfD?Rd&gJȸ(/XWưha9bf?=]++ |
| --- | Minor | ,q+u߸\}[TGO-N	s9Kn	2-%-ۘmc׃õ3-zN< h;wIݖtm+@bd!Zfna3dپN	ΝC%6Zݦn |
| --- | Minor | Cʗrqҟo,4	>88/1cQ6æC#<p1#N;]-Rs+:s]Mg<&;L,ST!otSaPp.a1nkjSp8Wioa@Z?hU٬!#>_WD#W4	He?WqrTͲ%.,\Y1pgc@T)~b#n]q;cR=&. |
| --- | Minor | /?f"v;KDRb+M^΍0 |
| --- | Minor | mrɧb6f&~0d(џ9JlI^J< |
| --- | Minor | ;&>)Aw0 #Ȯ%֎ofqv] !Iud|NZ`/؃1Bw4Rֈ3zy,o˕lLjq6yX$f`&08͟,*~$33afRG<xfT3lfpx3͌ef%y&tVXMs2{`qQGEcSޝ>J͠ (mP(qП@} Z>Ecx< kND(fMtnF8; |
| --- | Minor | `HslL|d}>ࠎP=x74BPhPȂQRcRES3ST#;<p{aabӳGiayͿ3S\TU_d<`}Hu5m`G;Tٴ1q'hq#Z!n*8sW-cܬ9nAr=׹܁oG<ܶAsϭ |
| --- | Minor | mbbJibbIb܄ĘȢİDKAHysČsD:bѣ1FFL;ǢQTNE |
| --- | Minor | $:]\Tԃփ6| ]S4_Ȕ#O V|fֵ"Yg-zJT/$3B+~l&ֱcM1ȨȰHKHh8#F1#,ŕUu4x,;q㰀ưObciQ)!#QqZBTM1USix>{Qݣ|Ej_hnCOOG+z~mKlx2UoT׭4g]˙ZqGv+lͧmMu4_c5DקxfsZ9 O<C:1+}*|C:&xzLog' |
| --- | Minor | ο3hnv |
| --- | Minor | kqpm`'Uq⋼oNn^ c1GTC%yA8¹s?nrN[P&.KQ5.Gc,c5[qMmM>&7Lfu!6_U |
| --- | Minor | :=XX&0';ڗ?>.8SydbNF.K0❎av*zw3FӴ\s@q4♀1[v?1hs[i+ސ{@ě%x>yf!2U|_CL#/	k!l0ૃ.IH |
| --- | Minor | <fta |
| --- | Minor |  |
| --- | Minor | ^ny'ٜr` bAgpgByƞ	C!(V\0Ϥ|LͬMF_V??R<fbS΋{|[y<GX^lہ |
| --- | Minor | ^łv278<<`C*EpUǻ_ݧvW6V4T֣+[| |
| --- | Minor | }W`Jh֢OacbS_̃5O64%QL0^r%zrvm;0rY: 5Mǰ@ՆB3hSrbv:i$h1h픽<33joXP&3̦=,ΗJ?I,zALau&^1s`QL(KEug`<Cw;_5᎝%Y; |
| --- | Minor | $/4vq!¦uдpfcDI*j寧{ԣE8|aFS8SتKςó |
| --- | Minor | 0 obj |
| --- | Minor | <</Subtype/CIDFontType0C/Filter/FlateDecode/Length 8383>> |
| --- | Minor | xSevB8@ |
| --- | Minor | "8lUZ6f=mII;u_ҽB7JE,"ก:n3xW6훜yy3~<>iQg,ښ{r'=~phKg'x??OǒbOr8\08n4پ'r&q<ps'~cӢƉs.^乍i鹙I	AK,Y*hmQ14I0)(JmqˋvIg槉Rgef%dӳ,ڛ$I3R⢲bĢظ̠ĸ |
| --- | Minor | )M#)&NhQPPV\\Pbvvg',NLx&gR)ߺE/ܻh֍;/ΖfŧeeG%d-u}gZfjT |
| --- | Minor | <yYR2r |
| --- | Minor | *j΋u |
| --- | Minor | [889;8/svrB989{8{98psq"8(N4'ˉ$r8!'Is28,N6'#r82N!w:<6MG0'ؗ2k[Zϟ߉9O89wr>c@~>HϣQS=!ziSf'g=HߒQAFfefլه]7y1FޅtCp{yT	J0?7@zS>U$sg#@^qP |
| --- | Minor | FOJXJaK	RmH0zpQ	n)]jLU)/Ңh]#Ta-U$	iLD`r75FN%Tb5#H"2`S |
| --- | Minor | ؚk3Aͳ($KB17=Ktut] |
| --- | Minor | ęRPa!Xu08GkzNMtzÍz<\/ϻ |
| --- | Minor | P@ӻps/gwf՞&GAVF2H/T+7t |
| --- | Minor | }G34{2}*XiKȄq`;&o;7wOŌ#hYMN:0d 7*&Gϐ!qI9$pc	qڤz=+"\/NXv¨RP#$qAD-̢Dfrc'mX^M8wҙɢdqǻEO}z@,뱷"wU hFȈ"f?g#%p*FJdgݾXy=G~y<R	-.F#psѸ(N^`QZ^/24yP E0zwȮ#̝~g豏Vξ()C4ĝze^kӄɩUyV!.& |
| --- | Minor | dWH;<m6Qb}?p<>.h5 |
| --- | Minor | E:EmMl/~8ƯźL*[z=&Oec&@V ꃂB{P+"&d<ন5 =u:lv[3O?ccDk]L!)HozRݒ#HQ\jӧU|HSzN |
| --- | Minor | l^|A+<Kyލ |
| --- | Minor | \EbY+0`W6fܷP3)-?]/PHSRxZ]&cnj!Rjb5"cv_У|iHݔ+HF_̾*#CXI |
| --- | Minor | ~`0TC>YF	a}17MvOsD[4U oWm`|̬L'yܑ. VgruIdpۡ˯Ηb+h+n4-#'xh03ny	eiB`U1~K+rMA~>ς̣ ^+7xLO.~1ek8%A\' |
| --- | Minor | A_Zatྠz=j<N |
| --- | Minor | X]RI\N^FcUGAz6_OTzXY!lXp |
| --- | Minor | l\I_A%0OwKY&(QAZAXfFnީI*Ìö[M9yadbˊhuN`0,PHMrRV_sPK	X=#r:sKT,K |
| --- | Minor | v#p#/T%x?sF ځ\Fġ	:)hgFuR%"b"Ҥ+r|yU |
| --- | Minor | &q^̜ruD8HYԛBtTeC~C8"BO͞{Ee@-Th*741f.FޘeRyZŬW(r(A}!iG݄H̣&y汥ZOE	qn-/ᰝ'j<,,9gu |
| --- | Minor | \LoC+|؃dz]tR]k))I02I(٤ؤz})YK2\RR/Sb#WѲ߈E@4wZ,;E،,'jt#J]Sc/gՄI;Ko |
| --- | Minor | қ#	f<3X~|S}%%dΊꜴ11(Lt^R[WgbcroA> |
| --- | Minor | {}[hbqlñcd}u\şE |
| --- | Minor | ]`//kp6ɚ3}h0^-)4rյ.G-nk8b0V_N3LŐITqќpRr	mtH`ZfD	KtPK/*-ĆȘx/%J(y\ tf:"j,)#Mфh;ZXcidab"m:^zyk |
| --- | Minor | yצ^)ӟE(e. |
| --- | Minor | skq |
| --- | Minor | 񋒘 |
| --- | Minor | ~5L\,H%%SWdqZ>u;z5щwP"W䴴y؈y_.ræb+]PWEٚ)ՌVxltw^":OIFh# |
| --- | Minor | *l̕Df ڇc;~<-A#t]]M`!-P_n ueM{j{$TD%^6s;_I'^8?caP֥WA-%<RgvsW	%<;T |
| --- | Minor | #'kJAegvH:7~|mtUPǪ2Q븫c|1Ŗ|5ri=u:E0)+ |
| --- | Minor | *b+e#[;LN3㖨En7A@3/|(\VO33F.ڹt.ЂF;G{ޏn9| ""'B&DT%F	|RScukp[5D3NP^PSRi^],=	%~C-opAJ+&1EGŭ~]zW8)0ɔBhX zyZg:N	q#ۙP |
| --- | Minor | OJ)JA2Fd{_}	$+teZC+3M%J2 h,?h~TV |
| --- | Minor | 99 |
| --- | Minor | ~e7o[]7w}En U=D zyyhc= cFfHCa/iIBk˔UIW/}s7e(`c$`)nEDp_{8Uq(ѻ}qwx:TVD11鯃tt#1RGW mi:bɞ2t_O?ax:"ϡo=wן}#Hfy G)-{ECvu8J`|`Xj_g0bP[G]vYU"OW^T'3iD	JZBy3?`?6H+ɾ޶]p6ͣ30Hw%{}ȋȀglFM$5	$"@liL_CMwTΪ+p!ohȄ$. |
| --- | Minor | /BX |
| --- | Minor | $	W(X}OUlj15ujtCjk4WGXWgk>M .}];vv;y:c*@ExQ	 4`G;q4<=P$(+3LMkR˙	ϱtlMaᡎU]elwx|!ff䰌Pkj6yv}y0LH z̔Յ&|f~ |
| --- | Minor | ;fF\oΛ|f 5dezf^lF |
| --- | Minor | =U)yBbZ>h)<K_WcS3)Ykzv_!Q:l4FSAGCyE7:B"nS+	_ |
| --- | Minor | )Ta |
| --- | Minor | ?xt?kg;/< |
| --- | Minor | *0=QFZڷ`!/PkD7s[h3mm9t/g῀meÂ\/%3[m-v#1a 	>!,PVC&)f:Vyz@@]E6XТh"f%š1%;_7o^Wi@/~OC^//{7c7$[U\kBtJړiTeK'K[nݑ,M&0X1W1T|2a:pEkN;p49Ku])`w |
| --- | Minor | ]_ݯ_b:~=+tmUYx}. *ܚW_X?ݳtWejpL1؇ﲜ,īKsw'F,J?xHtFP |
| --- | Minor | {c~ͺ#];쀟QZ\mXDi/Ѓ׹h6-y1l5ZHiAMj[ʽȺ!ho.e*4Ygvy97=BT[TiBSITme\f^o	MUG[xQ4u=r|Q |
| --- | Minor | gŞA/+W6:P3"5u׿1xޯsEݮMp4*={(%dճl$3bfY0ET>XAp8#*rZtA$EenUI:Df$pFd|;UЊ6M/ame6cӲO	4dFlC37"ZJWSXbqb?&%B:c:u,u7q)`YO1RDIc.c t@	V^feIJ(UTeb!9,=(el?Ck>W	ƬMÆ3wvg29l2˰c>odzٶF/ǜ?\bRt$Ko/L͓(BP}N};Ne&ϝ<Z59T-55eЙ ex0M$QWWvݘ`BU ?uWsXVaa!dRګā~miW9^!ޯ|"7BmnTF=lUjEn4mW Zek7XG |
| --- | Minor | !/u'yO8Zf*&|9Q]UY	pQE |
| --- | Minor | ՛(O_ynPBiKF	4۫m͒2#%ЄAE2,4op&S)k8243,"v|ᶴY5.QEES1Ѧ蟟yS |
| --- | Minor | =5/qh0iwM3{ZzaFb]rIJԁ |
| --- | Minor | ̀&Ӥ"XZKY5>\W<؛PYtY,>nXtLGkk=WկMr6qy</}N u.9J2SM"8zB_ |
| --- | Minor | $ZY66t@|hJ |
| --- | Minor | }3䅑Lj4h*Eo{tuv-~樂\,;&G+hAgG]hSYU>$3ff>PpۧM7Z@HY.	9/":Dw7|ޏ"Ae	M̳u |
| --- | Minor | ^)VcrMfZ} ,SMMRB+u9Σfu4hM; :0ubZ7i_d7 Yy俰Q[N,v5=$vX$+NÉhً\D;ь̋abaāCy=Y^(Et)JpyWụg|lՖf:HǓIY m$:KOGn%[g{Sr7t즇}ZW5&ZBJ]},.V˓i()E(bziӷq%%| |
| --- | Minor | Twe*v껠=kVwL(B7Q5*cj8B2X,4@2դtf	4}(1FENnT>z |
| --- | Minor | L]Gt=s |
| --- | Minor | ^g׀?"$%]=.kz8aj |
| --- | Minor | OԮR >h$c4TXON-1YE%ض5!Vo̱ff$<Z	vל7ߝBx |
| --- | Minor | {}|@s巩(_h_qL		AO}i)`Vŭ8@u[h3KIS^S-E=a}I}wmW\>ys]^`_TǦZp PR$!ɷ9$dijYBhP!mچf4͚v~-l"`wr&U8dEQ^XHRlK鶷4t5UJ,hwr XϬdVL۳zp@t3-k&vyf)(zoϢI:x< |
| --- | Minor | ^ |
| --- | Minor | l\sᇀ#KȐ>4*xz0BYǏn7ț]gDߑ냙#ɀ=?q=|6z6{N:#"R 'Z<h^Wfkk"[jRN |
| --- | Minor | )mj0Ӆ6Ȁd6w;|磓 |
| --- | Minor | ieYjYX"3`ac;	L+n`H|'[]$OH$R]0,=[,?>7h8Q~y-,p/+okU9]z	S#̭ 5Riu7Va[р3jg}2.XEzw]*%+웚(h>Ne60tp3̌t&3U+	ϏhN3o>*஬oOޯqOɼMP|{M]U1|^&7zS[	\BS:c6_$I,e(\#6T(Oh.w0$?p~{3sPK.\wtQ>  |
| --- | Minor | `bh2k*K` ΣOj # |
| --- | Minor | (=˝;Aa<zwVs4^wYYp:<$n}~?SADe$ywgBY |
| --- | Minor | L7"tn6gO]l3,tC1ﳂ҉ |
| --- | Minor | 0 obj |
| --- | Minor | <</Filter/FlateDecode/Length 32>> |
| --- | Minor | ``0/y߿zƀ	8p&  |
| --- | Minor | 0 obj |
| --- | Minor | <</Subtype/CIDFontType0C/Filter/FlateDecode/Length 8823>> |
| --- | Minor | XW"*,Qc$FEcWTĊRl9Kua)`{X"X&Ĝ^,{Y]=y3#0Hdz͆ iS'm.Á3ϊx^1?0AWa{y`1RkyѦ,>{a"/6  |
| --- | Minor | `IDn=cG`OxS\n=}Msm&[tqv	t^9zdAQqA֮.A=X<BìBdaMfg-|z{y[=Bý=m^n#0z$k0kyS˼&zM	sQ&-]q?_kpkϠPkwp큵A.CclF`#Qxl6MƦ`Ӱcl66>>`E |
| --- | Minor | [}-Ŗa˱*l5[c0;l#fm6c[6l;9aΘ抹ayc>/cX`Xɰ,¢,ER-&M`JgdT3,RDnj/_0,K7.û$!G;7S^,vocTZVVW!vЀA>K3M |
| --- | Minor | 6TM͠ E;,jx;mEvºxڑ#3FYuiѯ>2}̳1cY+w[v&nN\4aY/g'秪3cX".En]?EoqiO |
| --- | Minor | *6Gcp$$\)Tf	}F`$-y |
| --- | Minor | | =jGU}@f&}kvzRe1U5%eUy;lC:i'EjuBN)$bJ-]~{}&%8nsm8z`,;Kelr2,2Xv치n/g;R峵`֟8h |
| --- | Minor | ؍9o/D"8	'}];u0cɚEGd,nL;	f^}M峱.cC%V:Z^p#_1ofX|Kuk8F +Oa՚ zNn<q58[SԸ\Jn |
| --- | Minor | b!2w9H;wzGRhZƣh;Zt8v)S-$Ib@ʺ}<9lVp\(!RLI%CzB* |
| --- | Minor | 艓ik[wsE(xHI;,("N[b{Pg];kȒ<? |
| --- | Minor | )-`3gxs@'WI'/}Cݟr |
| --- | Minor | ^lW%ᥖƄ$d8?X4 ޑ6!Hu8@B^&uHl;A%zVuiur֒?.7og |
| --- | Minor |  %_ |
| --- | Minor | !|gX^!h9O\Jvh$/ᅭ[aߞB);G+T:24Uƕ}	]R-bN5̪4xTU |
| --- | Minor | 2s':%9 3^JDZe7lT4U],L$A\	Ex疣hd+h\g?,4^'7MFJs*ITɁ+<M3Yp5^ |
| --- | Minor | ODTjAghhгqRu"x	^Í6200,,02A7rLZ_ |
| --- | Minor | :iZܼCB2rrݧAk |
| --- | Minor | +nބ)Dw9.HDih~ |
| --- | Minor | 8cF([mLpc1=>!eْ6vߺYnos8xRοJ+səGX7,zU?\eO>#?BRD>%3+r!E<!8ʜiG=alHtդ;W{ԟZw:rlnPg={-=fzJC%hrh |
| --- | Minor | =!$cKB%i0uH%pRFFIJݹIC&d]jZfF{OV]MlaH:Aʟ?A;xH@P\ʮC(Q?ʸcMA*YMghQ:*wOLTylΪ_79N=~zy&G[܄PcYv.?u,J7ofЀ[]/Z^y1S%.Zy:]+@>^u(`C<(a|jd] |
| --- | Minor | $!nyT,K&j?1D	,!!?17!gy' faggig?4Aħ7uQ5JC@"EF~% |
| --- | Minor | ͉ޯ/)L2:> |
| --- | Minor | /-,dQN[ |
| --- | Minor | DVGE<>  |
| --- | Minor | );9¶;z{1p3A+ShʣUz |
| --- | Minor | #܁M+=Ar,  SHcrN|O3b<u[)o`¸ym6?ÒjzM.]_l1y`!.?CҤ`&e"xsX~;Q2bTlutHh[U[K8)RI[vV	"??wTH K1{uCܓ]E 3D&Ds<Ɩ1OZ1\f |
| --- | Minor | K(6DsZ&5kp@EQ	VpƷ@x |
| --- | Minor | IBG	uN |
| --- | Minor | DztgNc3כ"?g7jFC\ۖfzu/-@Eqܢ*|zSlSh1&?L0re<O()ͬ`I5~;C 7z&x^Q+4%y^VE^>^]}K~4fi{뙳{b{Xmsag&CD.:SITދYJ;Q<:?ˀD@p|T |
| --- | Minor | `!< |
| --- | Minor | {:^e_'͡`v=72qeN^"!/f&.\p5S.o`P;=#ʅ%bXmgPzu@ |
| --- | Minor | dL*iUMkUOn7ݚov&mSoVwN!4[Lofy1AF&VUV^zA͒C6Hë|4"d༹2fLf#8h |
| --- | Minor | {tZJ]f H<l1e&XxcyʂXr'Ή%~v\Ft)~R . |
| --- | Minor | ,r1ukOshI&3XIV0. |
| --- | Minor | |*.=bA#Rgw G`Q,.}?L{m zثObSԎ.&@xFRv|"Mm[m=$/ۿmon';,AZO8".5=v\NsUW5A6NT#"Lb@8N |
| --- | Minor | z/K'#Ze<kk5Z!q!##,l4_7ˇ8*,Jȩ=llsrk*p翆D̂LQ*n'In.G |
| --- | Minor | k`W4_4), |
| --- | Minor | ӸA(64`0ڴno=md48TZ*OOOʡsYi;kJޚ+D4	TMRtQnxqA#'&xİ:6k	{4ONZy)L'.j5B*[/l8]/4(}_+),h |
| --- | Minor | EuT&MOz2$![ɤ@f)!LOr~'?g淰\RT61w*.c8͸h!|~\ஷЀo̸:,>f[ZT0~c}nw0?+$/?zJ=SKe7vF7GPyszO~}Ǳ%ͱ<;(\s_^;=c)tFFp%Z&UTȌ.4|	<8櫎pm r#?01-_)4%G"!^Ma_ |
| --- | Minor | ˜GSV٩`0oC{dUl3XAus9$Po1MgJgVh,:v	5Z03e`/~wTUpOڽ 4ҧ~@ |
| --- | Minor | lO@}=`_ #x~(gzyu^?Cf]dL;\T8]oL?S"Moha0Ene-L\9ЖQ0 mpA(:Hѳ3bxH@S̠(hp tz*SW$N[u+gSsQgPsViwʭP/!6B\lg}H+J |
| --- | Minor | ȃB<&8 Y1	@iʌ_A,{AA3@d 77Xpλ 7c;WtJs剩)) |
| --- | Minor | ~%Qoy^; CX/6ߵqiVeixR<H<')'GN-!TGĺKm-[ۼxs|8~E~E#޶k;'IdgqS! D=R{ME8zI(Q8UVJX눂RP&xy)ⲱpN=k NDiȕ'i5%v})%1]8N |
| --- | Minor | Y5dd2H-CB#=?19%;Ue`>1CaOY(EQ4O)$,-o>apY+xu@]hM>-#<5?h0d4ҲeݒEx`fHW::s?xk<h'{\r |
| --- | Minor | ;I?Rz:akda}**L3.]sg |
| --- | Minor | (YY.6::YX6e-(4|]4Ն*LZX]VJ!뮂?\<nz2x1Ȓ,Ar )E,QxGے~coE_VtoP?#4A_1\;_ ZO/Vlj9E(]"?C4l 1̓T<Ԃ2!4S)/_#y(uZ^2ʾu61 =k}]htJB4L%\?<ՈN]\}I+Zg1h)t?qr |
| --- | Minor | q`ZȥAz)wt)MB |
| --- | Minor |  |
| --- | Minor | mƈ9mnʶ+1)Rj<Cr|}%[\~d꒦<GT:Y@ĀL.7w |
| --- | Minor | {z |
| --- | Minor | {	0rQjU?L΁]px<Ʒ=%.wy>_hr%[T5HgT$ʼ중r;j[R:ΜfPގ]Lmv?(&_IK|-nIӵRFRs44$~5vYИת3|Mkee1)ɦn~}&wN(K!R Ku~ |
| --- | Minor | "W(e_3ȼi&Afh:> |
| --- | Minor | 9LqR2VQpoH |
| --- | Minor | -~dEǣ&=zHv	YFe[G2*[>fpi(ڕ|4HBP4_#KӴ`kc#5^pPFJuk8lfu9< m_8ebA |
| --- | Minor | R[g?^邥i/5ae4sEe)BI	XYp]R9l)!}@H4`#AnSsR |
| --- | Minor | ]n5(B_4TFI$LH.!e$_ptFbQr𨘁šQ&;3T`\F]T+ALhZsRx}~`ɏDX ƨrv+73NMv!+3u ;#\{~#rR6-A>ĉ |
| --- | Minor | ՘k)t&EH3A1_riGh@'gنTΰj.s |
| --- | Minor | (=:\/ߟx{h#t)N;͓SV K^TȜ;񜂒i%MnwZ@b8t~o\⓭n\àˁ:		i#4;2R}{Qo@#21 |
| --- | Minor | ?~͑($%Ōd5sL sp;SݽN	rg>^Jܾf1w |
| --- | Minor | ΢|0N<B-3  |
| --- | Minor | ":?Dŝ4!4:)	U |
| --- | Minor | " |
| --- | Minor | RA/Dx<fg+<*3]OY-hJ;T9a?>Ņw߱Uj陦4QTZ3,dpEifP"D*<M`i |
| --- | Minor | |FХi9B]Q]Ur\#gU*Jѣb&ۗ2(JJ68qM:#uTṳjrr>Gl"4&SkBN<IO̧tst8+*?]/+D%ĝv=H52ziF!:R uj<3eRitTu3({pj*R܀̨Y(uDX |
| --- | Minor | ͵kS	Z?t} .C0/WԄӺ1 |
| --- | Minor | /97Tvnw梈\p8a]4 CbݺcY8V$Aj}jVg(ާ5!mcBr Y)q4%H(T<2.`gt;1%T>-3#'qRTQ	gMڛaY=5YZRDՆvsj(Rx4$S!I'YTlb|Y3/xRePeZtTxCcWC3$uj |
| --- | Minor | Uq*'S/H.S)CmYX3XÐaZuFsr瞸3mӈ0(*RW*X40"Nt; |
| --- | Minor | *KRBO6gf~o:VgJ Y!59MQL(Q&0cF`\NK@R-d]uFYU4y=5D\Z* |
| --- | Minor | 8zrt%Um"Av2a(5		?gm&U LF♻sh8M5)rIbA9ûn#? {i>INȜF}$-\S'h]V%kFiECuÓ2Je |
| --- | Minor | :D0C;k[a~1ȅ	-M	0mZf޾kGߕ~&5'O,b&H3ρgK] ToF=z\)c̭	qA@x	dļ{:'e*hLOD"(CcmIC}9-j J |
| --- | Minor | )B8vGj f |
| --- | Minor | vedyWLF&	vٽv5&1jEP,[_ZQQE36f]ʶғP-Hj73]YTd褥ꤰHJ[Mg+R/!i{',xJc5j |
| --- | Minor | ;&B{~+uN>yG^ |
| --- | Minor | \l+#n<ܗ_(5a!!o=$հI*:kgy჎.Ҫ	G!+aYIxR,yv |
| --- | Minor | '"KNeWW0KjWb 45.?ϼ |
| --- | Minor | " |
| --- | Minor |  uAUL^X.5-U>gc[鸯dK\ݳ+Oz.󛮮 '#tZ tqJ/e5LBή;ǴKBygΖuŘ2=/.	lcEo`їsA3-[X[^f c. |
| --- | Minor | 0 obj |
| --- | Minor | <</Filter/FlateDecode/Length 33>> |
| --- | Minor | ``)/ƀX$p) ) |
| --- | Minor | 0 obj |
| --- | Minor | <</Subtype/CIDFontType0C/Filter/FlateDecode/Length 1035>> |
| --- | Minor | LU^fOx :!@m3J`"lnq[z@m镻+c@Y[h(?dB |
| --- | Minor | FȲhF?hb851Q;wU%~}ߗy(Zt |
| --- | Minor | j |
| --- | Minor | ٝ&Dݛ-Q)T9jiZf<P\s7pμv{l/!>rٍ< #CO^qGݴvKLtu~*׭˄88np |
| --- | Minor | ҳPv:	Z3 ,X&*ÁzYG;9 |
| --- | Minor | ~7GNFσ&OhP] |
| --- | Minor |  GӠl|ʰ]N-lsՍꦣ |
| --- | Minor | <:iq%d38}n%H%B<:iaπ\B9QQ!ta3lU+XKD^RIj|l"LcCJ?ڎ'X,Y3qŕJdjs;-r(bhW9)a+	aӅI |
| --- | Minor | V~TQe@!waC(ȰIPld(Ȯ_{S#kTLƦYQ` |
| --- | Minor | 'GȘΝ2uVUhZKZ>$=BmVefJ*cozXV8z9E|HL_X^6}y |
| --- | Minor | ² K!Sዣ1Ӛ]i=R3D,3=̍mJ-"N5Wiʽ*o/&#b|H-D]P#1"<"(f(Ng&"ܫ$~w'`FmSc(WUKeaS#4//s;REt XG4%DX_N,AQ=)-4E"؍I)y |
| --- | Minor | >]YZ:231Z+DQL|kǕEYtZ |
| --- | Minor | 0 obj |
| --- | Minor | <</Filter/FlateDecode/Length 18>> |
| --- | Minor | ````  v  |
| --- | Minor | 0 obj |
| --- | Minor | <</Subtype/CIDFontType0C/Filter/FlateDecode/Length 7047>> |
| --- | Minor | \֟AQߌIj]VTԭ+]fa@Yŝ֭kk'ui}{^}{#˝;?'@0lʵ `k}#d |
| --- | Minor | ~4:cy9/cv&ёѢ/zE i~6vc7gh7! b1M<$@(}{w{/<$F.4sYQ( |
| --- | Minor | {I+Qx_:Q,!}7K#¼aR_<"$-Gz?0i\(ſ2o0o/iDB-uݰnt<8\;8[:uT-ywڴ_Gw6M?)lVZ?ur-uR/pYUrE_e1DL&S	Gb1A$!fsg]b.XH,"K2xp#> V:b=Hl&[]$o# ""BPBAD4C!x#-x.g#޳ "NfƦK |
| --- | Minor | OX?S4GtRL6. |
| --- | Minor | 2h6evz_ڗ%C&i:zo;0j!U3<@2B(dD؈ƑȀQFEbږ>̄4׋9s{YmQ=Je9CQ=(?MĪScS9{/! o/2RT |
| --- | Minor | (R,ZK	eGDhȐUA@(9	4 |
| --- | Minor | "{>Oi: }Mpb7{rSJדJ+b}naf/@V=pUrj3 rzQ.~<iJ(3ZQʘ.В4iQ;90`>\$]oF:Nb{me:[Np?NL) n7ے/ʢ0]\:bǇ-ɂǱhx:Co+J|`j4ANh#Cs$+9)[n3x^r\~C8lOFmdܽ+ø2-Nhض&`GWK&ajt<Ӫ=^I.ȉ)IMIFv1~XNz"N%Ӧ3E >R%,kN`F4Bh7|̀?@J3lWc߁;B8XbTׅnf>p>	'BGV+`:4lҦhd)$k9=lBMRV\4հ5a&<cѢH_LB詓|RrTXB6= |
| --- | Minor | :-3%+pfR,8{~aO +k^[1\ͭ& |
| --- | Minor | \ |GG6Vs?,tHD"@L2cXd-;uRqtMjg$i4S4Da?N8ZV}@R	8r@Pd).wَhOfgeK(ڪ>y [W~ri9]c&sg5vs;8;g: r1uA$}InQ63bxV-&ZLɼI8X#DW7o)B#J$UWJIװg2vWׇss-4lg#cP47=o^BZ1̜9灆k1["=CLc|LyG)XevpqB/C?zfEӼ|+}љXʙ~1'm	v!|*Yzg8W7ҟ|%n?y*\>jm}@.HX3soџ\=:YItc#$%~N!N/A!Y`EarNppKg׼!rܡqНמ` FDoy |
| --- | Minor | `("ڏԘ\uz.CKbL%UlPx-GުrxfcK*p6	l-dR%!W8;=]%; tHá$% bSzCN&R{$ G_X)w<B<57^Rg7X"C"	N_MB.m#5! |
| --- | Minor | dE'h4qI,G$UHr ɸ |
| --- | Minor | 9K |
| --- | Minor | ^,9a~\_dvtT)Fkq:[í =њv(Qzކ\mh7s!r<SEACe٠pś0ڡlppOߔY<ݕ`C |
| --- | Minor | <).6jڿȷ:*7zl{C~9uPaJ&*蒹:(0'5Y1?\r]^_5< |
| --- | Minor | *9-VfEW喱 |
| --- | Minor | p0i:K3j]JtIJ.pRnʷ=SѼKXC^ĀhrQwUf:wddá8t)gO#ܯ7"*x_{8F)8Sz`[qPLQ6GKǘc)B.W6ŏfQ&ÇpA&RrU$yev	a66X!ko&nW |
| --- | Minor | *f]L:Y5ZC.$fwR&wꖞB@Zov)fZF-!_F&z^>yo$r.UN*غ\`ΤKCcBXJ#yKܸ} |
| --- | Minor | 	au]q9mj$2hܬ)1SXt_ZH&Q([WI{B?|a	L~a\X} |
| --- | Minor | ;A'ėa´|9j;7<|Eo5O |
| --- | Minor | |dc5PcLc㓒Y,CIJA |
| --- | Minor | ~"/~F"DU:Ћjꀪ{I'$&(re~)6u?'XjhqrVuR`K;gCژ4vŒ挷tZ_xEl@đ) &CὗP8NTх0ho9[?SmgjԧǪ9j(>Ðdd2rri5˿ˠɼf==L}={YĦRC*#=; |
| --- | Minor | ]3hA sgmA.~p_w-qGbbrwaɡ[wJ7t;ݣ/[	DvNGxG4Q'CO$R!᮵ |
| --- | Minor | ]S*G-?Jc%KN |
| --- | Minor | .&~>5'j+ |
| --- | Minor | \a.Z>I}2UbKȱDMb);D8R?r$>CNv|G΅hNэt8_Uxh7{}o\&꺐o֊*ISd,9Ns8S@LƆsr@K;3hq8t)	*y2{ı SzI`ԉ	a	p.	Oȍ |
| --- | Minor | `yT}(xJ`̲,CM/ |
| --- | Minor | %b7{{gf.?ř{|ݻ@_ |
| --- | Minor | !A՟)ma>7ؒq(:ElোB %I2T,I />tZi`34CJt$n6 |
| --- | Minor | ]rĢ!w/12Y?'Amل(&QJөR6A45hl(چ#Uh.9u |
| --- | Minor | Ve|Z纸{Z+%[=1P/),j"P	"XԌ82`Ɉ߉cAty(+`a3l"KLhqg&dvxg'&JIH c|Jzj};55z6V?w.4 |
| --- | Minor | D;W	偦Jnbq̳2H$h>dGκ1[}v 7qЕZu=cu3@:9O${SC-Eͧ<c'XKݖ,~ ?TRTce8y&1E&PjH&6!)SQVQDcp! |
| --- | Minor | θD$\,:"ղθ,54aKA |
| --- | Minor | ,,7*$;!EIHacr6ٖt|*C*NݖY˿QЮ[9-@\tNf5 3QD(ljYl~qb/Hlg7?>P4A	VOB^KDUGT}؆f,*ZA"kB&hAja_	Zf[.e3hT́\)D҉}=ɦhoz7>6WLádjKYCf^~F6	W/s}Fp4%&pCYDX#Tid4sWI@:VJH:nB>gA_ -2 |
| --- | Minor | g󍶙Y7@}ēB#kVp>N7ˡ,u<+>tAkrn?)6vݣTSih.ri^GIPiGטҶt |
| --- | Minor | :'6:$8l.)()'$BBaڿBp礕l[}X*iZΔfmњ.VMa{E`e[ |
| --- | Minor | "_tc0!+)6]΢X R%Ɣ"C§/9:ڗ9	ae͒(!;)B=\PZ'1%5@k4N)`˚81Y1*ժ9V[ |
| --- | Minor | 849Xc+Nr55`~?r}bbrR3o$ՈрoOKfԘP3>!((SY ~ٵel_|F_ر,()+8V϶T/mgn-Mj[Sj$3IdأNA]}7GOʸ5M~EY"hǌezj'	>{jxp)5I@<9pSOiHN9iKkZNymQCmd,MvV^;<=0esmhHpֶe/j:akRBHɿ˥-Ik=^:P$ |
| --- | Minor | 2'+p9xH~E$2H Z.䜌QJ'jJv,@bX%Re3PZHpN/}%ffrlݾ,ߔ8`<Cث-b@ |
| --- | Minor | }Q#cdXAj袦"(NSq	"J1T|άO'J{RW@RuT<4ߋL:+?+;Jw>=z{EqF&;[W|&\Ыԥ0ƌ̂no6}ѳ>Tjx'^USE'SU)4 E0hA,#àu8l2SE9)0_Ztd$Pl<XA	(!CXr |
| --- | Minor | (>auC2l<-M9A]QJaо~Z+kmtfcSOci?רuY1XR;T΀5Kg:6g$VoYĂW_S |
| --- | Minor | B^/փbRUk1aTIP05ٷTj[1hVaOkF8NMAxWo:LOLOf'$4 Rq*tU=(gZC03zIƈ`W7F'_⨟z*(\s֏Tp9?7%s0&?v煉0 |
| --- | Minor | z/0aѷb%CF(b 1:k+JF `gq0	ށ4	_H.}>عCf°;ei.tZ:~W{9˛,d%Eŉ |
| --- | Minor | &ȥ ď |
| --- | Minor | <-T\4]r,փ+pry띟vwDc/i0|G'kܷuc8$N_UW$I ?Z]ڎnRT5$UXNGU$@#ANtc&Oof؃Z3¾s6$$ը5֨ AF0땞*K*TT;& eY*eWtV`?w'UhɜQ歍e'W0[!~4wX!?u2uj9Ke%/aI ^/0KbQAb |
| --- | Minor | `o.·-z<ViХ&˃VmsǒSJSs9?o	1?8D.`p^f4`n l5RYٙ,ѠbXF |
| --- | Minor | 0 obj |
| --- | Minor | <</Filter/FlateDecode/Length 32>> |
| --- | Minor | ``0/~[݃_^=c8 	M |
| --- | Minor | 0 obj |
| --- | Minor | <</Subtype/CIDFontType0C/Filter/FlateDecode/Length 3816>> |
| --- | Minor | XS׶>!Ii}'NX@EE'∊(a@$	$a 2OF@Fvyuz}۾	{k_k'ښN}}UѪO]+bjn0v@8Vɭ 4;XYJ̿#-;N09ae0ƊPvT}j0"<CTksC |
| --- | Minor | uDXV:n>I"	^i"#!rOg##U`e\*P,jj<LݠETH9V(E<6:DkًȽUZuhB>f\Q(Zcjc\T갱Xe"X˾1̟;cߢY.ZVRC_};SxX>FQ5HS)EySsy/G- jZKP |
| --- | Minor | *STMmԔBkInM%P'< |
| --- | Minor | #,`(ݧi:E<^|d+]f{vv?O?`48FNV#6b>	vÂ'@e4Hvfm8QFqiI9JYtVߛ*QgeQkqC5`](LQ}ELe2/Za |
| --- | Minor | ̌+m4qbƼm(ŝ#C^QU	-9hGNNVSnRdɬ-QR&ϫ㡬>_fƍhq\1;VM2ߵrYnIf!J	w{aj210y	jޑz\yOp\>\Y[5@10{f̚~8&>>C#n̠r qF,]:JЯMqF Ncs*jeUe{}Wd8h8Y	悓 Vns֒HZmi_؈y?}3ԃ\:2\{NB|7zkdD0j4aXf'=Fᤃ]Zg&JEݧ\ʥ+_ |
| --- | Minor | /ܼ M.æ-t,vqJqNUy{~ҟeZ A~C3aTJyEvC=uL5V29619-xInBwvi;+76'N?tzO'h:?Aobzi?~g%{"wm7]~|La' 曟(rg$)W}wcXw/Ip:1G)һThp GzW?8o悐ʚR#xh&}3dUg.<(=v-HקEBlڦܼiwk9ٽ#^>Sf.Kc{t4.1*-Y` |
| --- | Minor | !xEt.6Ap4 |
| --- | Minor | ^{wD %DO!JKY:Fy4^Ü>|=bWiP+#1\ ϳ_^/D]psNo7s̹ |
| --- | Minor | ȎX;(!blL	kҳJMHR>s5*#Sb8l7ڞ\l)o&fZ][KrQֶ6كkWXͣ!mOUِ̱_^(+)Ò9D( |
| --- | Minor | \;{3_\"DfC*Qi]&MoM ͂I6M:BGoNRP% |
| --- | Minor | [ EDt!=mY5{W\84D:pތY褋qs/p^fEC^OI Cat~oǻ2dW-1VT*UuX]mDbgd\ԾzPcXA,jǤL E:Q[RKٶ7I+FǸw;iA݄17Kmk!7ym]I"wzHPt;[~fڸpLq%-jmr |
| --- | Minor | %jXnCd=XV῱C=`aij=ZSHX67~/YM6ȟ17]~_;l̞n|ɚ-<:f=yE%	dy4w'} |
| --- | Minor | *k=ȀFƱyyeZCeZY>A<7`vK}򒯯~Q+EMSH~͞5C%6Xkĉ0GX=~{ß/]	륅+WF(}FJJ&RLXϲIȎRI噻*ZFo&^n/Ec-fA/{JOtbs8)' |
| --- | Minor | ~1Ќg\^RyhՓV}utL~'JIU!8G@?)ɪ+Kw!jr'/DRfsg75>$*f(kUYlA\9)=UaLN |
| --- | Minor | :A۶NihzוnQyY8ӱ42caw$8l>VMo#p |
| --- | Minor | qf\aDPFO2?l V$hʃ^6[H-$ s7fuK׮Faɣ{eJS3TS,kh;	?j#'<؎?'ͤCk֖H;.yOȅ:BRXMOL=_oQzB6$5슯޾kg>om/;32_h,gI9 |
| --- | Minor | |7je:%~dѤ}u9֯`t;:3ݭ:Wۀf<{Fzk"&%UVՔK2 |
| --- | Minor | |"luTbX62Fe9GK-<CGi9w]7X/]WJkjmlbӅ|uxSxTfflԋ{ЫIO>q |
| --- | Minor | jL-V3m;:X㗲{Vb ?Qڦ$7Ƀ4cw{Aۣ;Ճ>QFLۧS"MjI=ʬZhlAȜ*\.َdA8;߃Bn7}9l !2Amo |
| --- | Minor | Q\d5xo˿<5ָ7IP |
| --- | Minor | $ |
| --- | Minor | l@DL4!5mlzs}єV-E᲍|[YgM/G-ֳoWg\ ]"mă |
| --- | Minor | b&ZVKPeA9$ V? |
| --- | Minor | ޫ9d F%^pns/E却?1} |
| --- | Minor | $@ƋLo`"/Rž |
| --- | Minor | X&zXNoXH,B3HDrh!]tfEZUzjaUoRqt@XVb |
| --- | Minor | +)e< |
| --- | Minor | }^AE,jaj |
| --- | Minor | $7'Vz_|+>K_|w!vӦׯ]@p2P5Qsj7:@`Mvf9+27jk3{qGO0{ |
| --- | Minor | 0 obj |
| --- | Minor | <</Filter/FlateDecode/Length 24>> |
| --- | Minor | ``4hZFúU (& |
| --- | Minor | 0 obj |
| --- | Minor | <</Subtype/CIDFontType0C/Filter/FlateDecode/Length 666>> |
| --- | Minor | R[Hagwmr`;.ݨJQ֍t |
| --- | Minor | o3mBJ^ QrI!5zs#uu!?FTfVɔKs!4hZz^JYQ_}Fm?J  *LV2B3q AjgVߙ!<:BbRiɌD%x=|\pda8mtcp? r0a@`JD#N%&10(D)>(El?m/D |
| --- | Minor | JR#","1#zDn;}-VV"0`I\,!o <j|ȀX	6IUʵcUU*Wm{B_bo$7ɷ/2z|ԫtZڠ:^n |
| --- | Minor | ?||ܴX |
| --- | Minor | ˂o.pmLTbW4MN>|va%;=妩]3 |
| --- | Minor | 0 obj |
| --- | Minor | <</Filter/FlateDecode/Length 15>> |
| --- | Minor | ` F   |
| --- | Minor | 0 obj |
| --- | Minor | <</Subtype/CIDFontType0C/Filter/FlateDecode/Length 1137>> |
| --- | Minor | 8Ra1ދЙH!+dTsd^K{i{o|h@+ |
| --- | Minor | ,lĉɒdٟe纻dk{yy~< |
| --- | Minor |  |
| --- | Minor | ~H[X}r>HDȐv%0Z!oEL'+_UU[Dݘα:l{`0<(A1$aݳu |
| --- | Minor | \=Sj`"+h_/]<k4`Oaky/(҂ô93hւr-)rVPϘhK l.-ЙX88Rg,-0`&ҁUe |
| --- | Minor | @``}ͨxcACjF(< |
| --- | Minor | TVJK*JS |
| --- | Minor | HAyD[T#GTJE&KD%ьZtJH	TAM!Q_ u:ZۜeY-.Rski!>s>q-fi",-`5ODgۆvzf~ut |
| --- | Minor | ]ŮXZp%@|3RK:΄Bʽ]A_˚~4vqP:su7ɒc)hj5Wya`?N/#~/U,/>vB_s0'8:Xl~KbFr։:wʎW/rˏ0O |
| --- | Minor | %yMޡg7<,ZԘrfLc%W.>6L/إwSOnz 䕲5kUWꍬ@^4%p񵝥<wSⳤ;2mO+r |
| --- | Minor | }^sylnrcVe%4P<8iz'I̩='9w8ͤpž;ccגS`d uG|?4$ӿ$"}-|gI'U'gw8x人4?3K85{wnq vy#mqxL2K>lC"keCb XÖBX߀@ |
| --- | Minor | 0 obj |
| --- | Minor | <</Filter/FlateDecode/Length 19>> |
| --- | Minor | `  u |
| --- | Minor | 0 obj |
| --- | Minor | <</Type/ObjStm/N 200/First 1816/Filter/FlateDecode/Length 6438>> |
| --- | Minor | \YF~_!cሶCcMj6)=~̪ |
| --- | Minor | &v8b2 *+/*A4A6*6on8Fzm8FiazwTcOk,>o |
| --- | Minor | [p@=T$8qoB54֊вY1.6Ќ|EDM<&:wS |
| --- | Minor | $E+|8	iN"U#$YВPS8!UJ/@w5YA	`1'b$E$d:"bN@p4* |
| --- | Minor | ' |
| --- | Minor | axnB-Q TAjՑ01@ Cl(M\ |
| --- | Minor | )Kv>0'dyIIk8đ~O>8!9ؑzaHxIhV1x!9fFqk`dF09(  @8`ZBf `	+m*i[H )-ȅP	$-D<VBe:ADI%QAD0ItŀgM*b&B&/<mfUEVb$Pt&I4	24_:?#!%KV3§DC}	lZ#QW<9 G<Cu |
| --- | Minor | ^a$86YVK(EqMXc.aP1ޑoGҐ5%4pW |
| --- | Minor | E[*3GgHrX^jM`Jm!'E/tt-T :E`Igh-	Cq>pXēV:40 bNORaA rCY8  z$Ġ3$'xҠ'zrOVD1<{A@J`G̠)QYD	̒Ͼű'#2$Q(҇	!ݣB$%"*IZPz$wI(~ل\777BU @8,@@vȣg_7#;5..:^ɇJSAKҮո ہF@2;^p}5,dg |
| --- | Minor | =kGՍN/\hXoԨFB͈!c QsgE38qfڴ)gTZ87fTdСWƅlVTbӁpbeQQ"a'$UTo.i*6jF(4\(3/1bܼXVzv	A:E2邲OPV}Хכׯ@-FT$9:8t|}A{ߴ^gvw?j}=pG,}u䴖).yF@R)W3ӪiuzŃ}0{U#yM=h$#GME^.sUc<	r6</fiꏷC|>ݽSOԌtO?ëlWY7Y_>Ȍy	y>U'fēkSe%Y).Ћl,g]e1f<3fFN3SP |
| --- | Minor |  |
| --- | Minor | ֜>K2VV3AVpf\lgVfsv99oMh:q=S^\/ׇաL00#W`l&k7s!W@BgCRU,.+бa6(r&'P=K3B*zc*eXvZQ:%*gMfqǥ?EX1W'T@/3ƫMu4X>ܑy |
| --- | Minor | O	2Y7 |
| --- | Minor | #4uE^g}Vs^g*e#yy?kY>]A'7fR m_U~V}gF<-(]@#>}sa&>J̛Gb^):jXxWXjw!T6dj﮷}3kS%êzAǘ<X꿪2eIcPgc݂^Wj귐c慩SrG+:Sr[AJv:4 |
| --- | Minor | (23*bAFk3rV5s:nu7W+%bQR"Ghp<>ĎD$;F^W\('25:&*;n0/l2H{]_?܂tfbq*'6@կ	WZNk[*_Ao,ӄ7GshZpI[f |
| --- | Minor | ) UohudOOTU5W |
| --- | Minor | }8R6{亮2^mY\OZ	Yv>67ͥDeRR&e&&E&&E&Z $5I&ߤih_ow}Shz\o:ytY}<|Eqi&q`&q`$L$ln8'v0dҚ%,m:64KSĹKyٳqs,D'*>QOTOTүqOT|~jBD%$*!Q	JHTBSD%&*1QShDEL&} ͟ LD7|c*g2mi1+K]ʄ;!T	ELg+(u\+3teƮ2WfY1+3heFS'3ۏN2]fu-3eSXIQζ@)?f~I9<f>52Nj?jߏDcNa|LPTv9꒏f%%℉C |
| --- | Minor | [^ZeZe΁r GhI@M@9HS9cɔfsU#INE	cO"G٢[/UjFe d3)GI9frı	+_jN$S):OHΏVbUZs]5˹Rϕ.*'C>ƩJ/	NټRwG)ef%WvLf q<(N.N\ j47*ASl\mxmF.5uN:lsNO{7rj.TwBT4s~rJ~<9_eBs]$zz؝=SI.7t.7t.7t.uu.?t.?t.uuy:!OI4Fs*qFj*#wfJ@ǲrU`O*B*B**)1Ѫ1bKH&JzTJ%FS	EoZ,J7"zȩo\j(.>ymLh0yT(@e.{hrb491MN&'FלlY=3991#']1&R>GLn&g73݌=qv|U#'zf<Q |
| --- | Minor |  |
| --- | Minor | ~*W	tUbs]eI"U&~>}~yy7_]nr_<Ǐy쿰r"-QPYD_mn/x1wbI^6͗7[-LRll~t |
| --- | Minor | >ovׄ#b9lbzЌnv* {҃	ƔdXLS{ϽOTM!³[s |
| --- | Minor | =Ƈy̔S,>#YSi9~-qOw>;WVCNj@ov'}Fy57qdu66()On,7=WCW=KFQrK|eSH;q;t$\PAGMJ#Vbz~:(yI}4 |
| --- | Minor | ?0,$#l?.?hnG?#fF߈%3NvБ~5^=*ct̸Nb͌~bR0$֙ITƛ)UυU  ҁV˿C7𪒾h`S}ШGtԪe(2hkмIV 9oqk j=yWuy|D=yi;mg=eo%D"1ƞ)A2vYRFosPN# [T1L1/JIT?yoK`Ēq^L&iAR$y2zYĀsЋJԃ/zIM*wsJ= |
| --- | Minor | zD @x" OIS5& |
| --- | Minor | ?^ |
| --- | Minor | _zzP6	k)bimXYڭl\:#WN/@sK-E+oi{j_mkqjLK-*%VJ]!x/ޤH9&gڂ?K{:zze2КZlXWą,/%H7}҆1o)= |
| --- | Minor | <f)MҝFCLXYJv7~(^%QI\śGRI) |
| --- | Minor | .8ǐ1!6Y~5IdPiԩYUjU e8CCo&hN#WEf#j. ^{`RPG֥˴YODXΠm:KXgA |
| --- | Minor | ݌3 |
| --- | Minor | `덏Iz +GoyH^{`DM_@?7W~Zmx_ 6?wрz#,rpLtXzӤ)H[!tH3A" |
| --- | Minor | (aޭU$ͥ= |
| --- | Minor | %0{	j63"V|@*GYV@AކTo1 |
| --- | Minor | >njQ^sj] M:I5d;G>䀸N:2mBaDtL=3q)Qi|j$NL8$2iqPlHEooɁvbD-2 |
| --- | Minor | yq ќκkkDv~1d;FW_)zHpI>@DNa'Dv"l4bB+Gp@ue2N)B<yHҬI &rzR,۞d]4gbLtJ!ODFP!iab-8=Fδ4}Cus JDsʩF1Gj>F{zhcxKXܮ"P& |
| --- | Minor | .ժ۽xw{hy;ϟwj[z׻ۧ뻽O\YӐo~6o߾GWWWWcvwwyK9s</w=CJ= %D>#ڋ% |
| --- | Minor | +)\}ׄ؂O77oo(2w'-nVĪ}~Xl//no6h?Y_lW~(Y1,p\Ѳn	;sa'EO>m?]$mu-)j |
| --- | Minor | |n-zo8!ae9?zπC&1jxL['1f gZ5b 1VIB?J<*o;VğmTV5TK72TiVP)7ss@%zV^_v}	桡m'CBQzN߄ |
| --- | Minor | |ӡYF |
| --- | Minor | 6bѺfiMvHP Q@4S`Rnq")?~_> g0 |
| --- | Minor | *Nb\Lf~0o*YhDZ-`3N_/sK'πsK~bu>n.>OUynE=qq8J`JZwVZ}Zh6\Ar=U=5Kt?<}fItO>x9a1.p@ "AAW}01 YUr!?FA`Gͺ}9۷tJݺY}un߾koߵov~{nm7smle{@ VIU{#7߬okk7hk?k____onmei7g=ڟ~u`( 	S_ |
| --- | Minor | 0 obj |
| --- | Minor | <</Type/ObjStm/N 51/First 445/Filter/FlateDecode/Length 2388>> |
| --- | Minor | [oJ}~ϧ*g.ФBC``j6?{ӆJfa.kg=DzؓJz'QOL7	<E}O(A@F2GXzxW2ea |
| --- | Minor | p ̬|ä,0H;S)`Ya'Xz |
| --- | Minor | @aM1s |
| --- | Minor | zHDJ3\ϕ	ms8\Q'R8(mzf	!LU |
| --- | Minor | @1Ҁ33zhW)`2+^oBv2`9M|!&4FX.趣4[0X:1j.&]uWoZkYpQ-$-{?{.u4氞Hϡ0dƘ	EѨ1h- q8s6ÿ'Tz'T&9RtJ?czL'r5jhEMmA#TlQwf-a(5l{:4NjhzVjv2CtlF4}M)(P9*΂%1̬/5P):C%}B |
| --- | Minor | ~@!#&(B19J(C9ZGX[ۜ |
| --- | Minor |   [|izdu!1[+$-'Na,G]	pWhQ26Tl"~,_ a#be+V'ON͢8LQς΢"h|j껎NcsHy,'N&('#$LñdSK/ϫsn9o>`2I]Ko̝2/?RRldhbٷYVhu˦K˖YU~ȷq-Mg4͝L!e`\ߊkb~~hr(}m?T6\o.1v<DGiDf,8Q<-cYbba0-3>ȼÁAtI}{Aw=rP.ş	ȘW54K8( Ap[5)ؾ&^`feic']T[x+9]ʢ̒}j\ԂK\ |
| --- | Minor | ;:emHJ2"ޟK GKDbNr[6@8O{&GIiASa7}Ocbxͫ |
| --- | Minor | <AB+6)첱tn}dVTU.NMJ\oOo\tY8f\ |
| --- | Minor | iv1zeyWc«t6u1G9\bL=pT{;>!_pA^#X1Ba^pPq`vh |
| --- | Minor | c |
| --- | Minor | $oοwcD<EX Ρ[:IɆst6[vm8Tٿdu)|qlK[g]unsgձ\"/6?@j\bCppMZǫAIw	l2	^=T\T1%q0lX؇8eF	xI_[I$o*oKQVtBw\T|{8IxvLr1Q>rzzqvw&v"jEB$JHc!M<J`"ʵ"JP*lpW+ TLV׊VڗFZQ;ZQOUEQG+bXc5K|XG, ]eڮXANCEͼql]^ģъݜ^< -_LipT.A͇Fob`Hrle&6;ߍ^hRz'2oDjJ2rTn]߭kbsi4NEZB摋Ǭh] 8x1TB-\,B8D%J	071,ZW/G>lZw^5x[knYr˩>hwn]B_NǕC2ߵ}y{1B>t}tW5ˋ^( |zWa%W+}/{yHK`⯟| LLw%#b|Eۛ6Z+U	^E	^I`8|A߮N [E8ǖ~hVe7'e?L |
| --- | Minor | 0 obj |
| --- | Minor | <</Type/XRef/ID[<3fa81f769841a402db35795406a36751><3fa81f769841a402db35795406a36751>]/Root |
| --- | Minor | 0 R/Info 2 0 R/Size 807/W[1 3 2]/Filter/FlateDecode/Length 1897>> |
| --- | Minor | "QEqA(nq |
| --- | Minor | PAV |
| --- | Minor | 4"h /(.8ؙNvhiikg2=g{/8_|=uxm>؀x.8a#nwf_079 l0Xܚ3LC-b;lϹðcGF;agqBGQRG`W(ob,aw&b&co)a-pa6TH%NWz |
| --- | Minor | \nah?q8^!ɺ̢0IQNF& |
| --- | Minor | |8Lg_4D{)l|8]Mg2MfLLXk:I8&)kG=홍sp?8s{հ B sq1.\ؑd.?@c0+;<\1_p8u͏Yu7l'̧ބV`7q~lVq]X%"ޯug̲qHx3#Jt}"1w4/2[әVI9R-d75I~28`3zdWj~.8b݅N}'I |
| --- | Minor | )N3P|Qj<U"%MvNLgmY]KxA>G"wL罦' |
| --- | Minor | ֋Oѫx |
| --- | Minor | wE~D^4gϚ4c|(}m>|5i,hGtXFqO;U?	_	WQͱaKl`CڲZu;&nZvv#p숝ĝB{:ӳF`W(&n^ΊfV>a`,qnѹݙ	ud:{a"&a2>S8Pܪ[z!8pq鬷)u*w&jMFŕIW:k48qa:Nh]p |
| --- | Minor | 30pdϩgafls}qIӬ~q/c5=h[y9Fm߭ݨ>%oо9w~{H>a#.EFbƣ}n]}16xO)<,V9<w"^˸b |
| --- | Minor | ^:ǫx |
| --- | Minor | >GoM\ε;v |
| --- | Minor | ;ӹھG>l!hwEIڣݯbH)+R}v !X(+;(a 6C-`{C~7'7Z=1'b/Lޘ8 ` |
| --- | Minor | ~@ Cp(qhwTvW;(5.7xp?tp |
| --- | Minor | BvXE{-BwZ\kpC7&܇Eb	]"7(Ìq0&_*^;IxgjrPz,جIx>$ުo躖T~IhrX#L&mIvx8o=759&^eI2qNk}Bf܏chIj̯3AS]]`ǍN|]~$>xux/hR/s>'ߗj}_7p^|IZ׻_Twg<//o֏uWJ_%Uj_j~Y|5/5XͣuWl}5-ME#"?mN0c0;a,vxLDL߫?Ew%Y |
| --- | Minor | %EOF |
| --- | Minor | ANALYSIS DRAFT |
| --- | Minor | LaTeX paragraph here] |

### [Script] GRAMMAR

| 行号 | 严重度 | 问题 |
|------|--------|------|
| --- | Minor | tact_jmlr.pdf: not UTF-8, decoded as latin-1 (please convert to UTF-8) |
| --- | Minor | [Script]: goal=grammar strength=minimal |
| --- | Minor | No rule-based issues detected in selected scope. |

### [Script] LOGIC

| 行号 | 严重度 | 问题 |
|------|--------|------|
| --- | Minor | tact_jmlr.pdf: 编码异常，部分字符无法解码（已替换为 �），结果可能不完整 |
| --- | Minor | /方法论：未检测到规则级逻辑问题。 |

### [Script] PRESUBMISSION

| 行号 | 严重度 | 问题 |
|------|--------|------|
| 130 | Major | [G1] Em dash found; replace it with a comma, colon, parenthesis, or sentence boundary unless it is part of a preserved quotation. |
| 171 | Major | [G1] Em dash found; replace it with a comma, colon, parenthesis, or sentence boundary unless it is part of a preserved quotation. |
| 172 | Major | [G1] Em dash found; replace it with a comma, colon, parenthesis, or sentence boundary unless it is part of a preserved quotation. |
| 543 | Major | [G1] Em dash found; replace it with a comma, colon, parenthesis, or sentence boundary unless it is part of a preserved quotation. |
| 656 | Major | [G1] Em dash found; replace it with a comma, colon, parenthesis, or sentence boundary unless it is part of a preserved quotation. |
| 753 | Major | [G1] Em dash found; replace it with a comma, colon, parenthesis, or sentence boundary unless it is part of a preserved quotation. |
| 800 | Major | [G1] Em dash found; replace it with a comma, colon, parenthesis, or sentence boundary unless it is part of a preserved quotation. |
| 807 | Major | [G1] Em dash found; replace it with a comma, colon, parenthesis, or sentence boundary unless it is part of a preserved quotation. |
| 877 | Major | [G1] Em dash found; replace it with a comma, colon, parenthesis, or sentence boundary unless it is part of a preserved quotation. |
| 921 | Major | [G1] Em dash found; replace it with a comma, colon, parenthesis, or sentence boundary unless it is part of a preserved quotation. |
| 922 | Major | [G1] Em dash found; replace it with a comma, colon, parenthesis, or sentence boundary unless it is part of a preserved quotation. |
| 932 | Major | [G1] Em dash found; replace it with a comma, colon, parenthesis, or sentence boundary unless it is part of a preserved quotation. |
| 937 | Major | [G1] Em dash found; replace it with a comma, colon, parenthesis, or sentence boundary unless it is part of a preserved quotation. |
| 1003 | Major | [G1] Em dash found; replace it with a comma, colon, parenthesis, or sentence boundary unless it is part of a preserved quotation. |
| 1005 | Major | [G1] Em dash found; replace it with a comma, colon, parenthesis, or sentence boundary unless it is part of a preserved quotation. |
| 1017 | Major | [G1] Em dash found; replace it with a comma, colon, parenthesis, or sentence boundary unless it is part of a preserved quotation. |
| 1025 | Major | [G1] Em dash found; replace it with a comma, colon, parenthesis, or sentence boundary unless it is part of a preserved quotation. |
| 1027 | Major | [G1] Em dash found; replace it with a comma, colon, parenthesis, or sentence boundary unless it is part of a preserved quotation. |
| 1035 | Major | [G1] Em dash found; replace it with a comma, colon, parenthesis, or sentence boundary unless it is part of a preserved quotation. |
| 1036 | Major | [G1] Em dash found; replace it with a comma, colon, parenthesis, or sentence boundary unless it is part of a preserved quotation. |
| 1089 | Major | [G1] Em dash found; replace it with a comma, colon, parenthesis, or sentence boundary unless it is part of a preserved quotation. |
| 1166 | Major | [G1] Em dash found; replace it with a comma, colon, parenthesis, or sentence boundary unless it is part of a preserved quotation. |
| 1193 | Major | [G1] Em dash found; replace it with a comma, colon, parenthesis, or sentence boundary unless it is part of a preserved quotation. |
| --- | Minor | [A1] Abstract five-element check is incomplete; missing background, objective, conclusion. |
| 1 | Minor | [G2] Long paragraph detected (448 words, 17 sentences); split or add a clearer topic sentence. |
| 47 | Minor | [G2] Long paragraph detected (578 words, 21 sentences); split or add a clearer topic sentence. |
| 96 | Minor | [G2] Long paragraph detected (521 words, 21 sentences); split or add a clearer topic sentence. |
| 144 | Minor | [G2] Long paragraph detected (389 words, 18 sentences); split or add a clearer topic sentence. |
| 205 | Minor | [G2] Long paragraph detected (266 words, 8 sentences); split or add a clearer topic sentence. |

### [Script] PSEUDOCODE

| 行号 | 严重度 | 问题 |
|------|--------|------|
| --- | Minor | tact_jmlr.pdf: not UTF-8, decoded as latin-1 (please convert to UTF-8) |

### [Script] SENTENCES

| 行号 | 严重度 | 问题 |
|------|--------|------|
| --- | Minor | tact_jmlr.pdf: not UTF-8, decoded as latin-1 (please convert to UTF-8) |
| --- | Minor | [Script]: goal=grammar strength=minimal |
| --- | Minor | SENTENCE (Line 3, 178 words, 1 clauses)  [Script] |
| --- | Minor | 37 0 obj <</Filter/FlateDecode/Length 4512>> stream xÚ­É® 8!ñõ;ìÌZè=UU¦pìûôï=úß"¢Í[.ÿ¾ýýþþpúÍÓ/oOô&@ÀÓ÷ufó)àf;}¹ýõlLHôg.`Ë÷ýýecÐc¯ôIÏ>Ý»1Þ±ôÆÀûåÍÅH³à+¿)#]¤ÏúGõÙPF§¶_}CO=ò÷²&¶ÑîzùÛ?~÷ÏàN7Áät ¶è,¸Ó-ù±ãÝ¹|qÐ*[Á·²±W#Êf÷zqÇÅå°ñvï z¿qXzcÎ'nS öxÛ7ØBHµqË¢ÃÚ¶lj73`åheu9¢0à;XwÌ+<å°üDÆ#íd¿5¤LG7<Ñ[~/£*ô«`¸ã­°Ôãþò÷þdÍM6)b¿¹@¬<}-Ò·vüh/ÙfaßuZÐ&©pz¦gÝ¶>ñ¾íë^ ¤`ü Cì«2Ã\Rªk7»6Î´ãÙÝ½¯ìqmûf½/!Øn>¢%VsÇm{l%ä"&öÂÃ¸°È _4£ø _ÂÜÃßE§´ÃÉL_°Î²ZÁ·&Þ­+Õ½nÿ8wÄf±Ä ÞJOÍ	¤Íç |
| --- | Minor | ¸!Me²z9¹q¢#	¬ÙÏx×I} AØä©ap¨¼ÊÒûªÍC-a%l2iëëëºà.oõKy]«tÒë|f-f¿µ!§Ì|/¯Yêç~áý"ÌBËOË¼a9I¥Yaò´«JÕ6p>±ïAC­ÑP¬\ |
| --- | Minor | é/t¾¯ÊsåWhVm(ºÁ2<ºéÐ¡ËqóÎ+YF. |
| --- | Minor | 37 0 obj <</Filter/FlateDecode/Length 4512>> stream xÚ­É® 8!ñõ;ìÌZè=UU¦pìûôï=úß"¢Í[.ÿ¾ýýþþpúÍÓ/oOô&@ÀÓ÷ufó)àf;}¹ýõlLHôg.`Ë÷ýýecÐc¯ôIÏ>Ý»1Þ±ôÆÀûåÍÅH³à+¿)#]¤ÏúGõÙPF§¶_}CO=ò÷²&¶ÑîzùÛ?~÷ÏàN7Áät ¶è. ¸Ó-ù±ãÝ¹|qÐ*[Á·²±W#Êf÷zqÇÅå°ñvï z¿qXzcÎ'nS öxÛ7ØBHµqË¢ÃÚ¶lj73`åheu9¢0à;XwÌ+<å°üDÆ#íd¿5¤LG7<Ñ[~/£*ô«`¸ã­°Ôãþò÷þdÍM6)b¿¹@¬<}-Ò·vüh/ÙfaßuZÐ&©pz¦gÝ¶>ñ¾íë^ ¤`ü Cì«2Ã\Rªk7»6Î´ãÙÝ½¯ìqmûf½/!Øn>¢%VsÇm{l%ä"&öÂÃ¸°È _4£ø _ÂÜÃßE§´ÃÉL_°Î²ZÁ·&Þ­+Õ½nÿ8wÄf±Ä ÞJOÍ	¤Íç |
| --- | Minor | ¸!Me²z9¹q¢#	¬ÙÏx×I} AØä©ap¨¼ÊÒûªÍC-a%l2iëëëºà.oõKy]«tÒë|f-f¿µ!§Ì|/¯Yêç~áý"ÌBËOË¼a9I¥Yaò´«JÕ6p>±ïAC­ÑP¬\ |
| --- | Minor | é/t¾¯ÊsåWhVm(ºÁ2<ºéÐ¡ËqóÎ+YF.. |
| --- | Minor | Sentence exceeds complexity threshold, split for readability. Applying the split needs --strength moderate or higher. |
| --- | Minor | none (split proposal only; source not rewritten) |
| --- | Minor | none |
| --- | Minor | Check: NEEDS-LLM |
| --- | Minor | Flags:    not-assessed |
| --- | Minor | SENTENCE (Line 3, 852 words, 21 clauses)  [Script] |
| --- | Minor | Ïâ3DEÈ'9d:GëUõ|º¼ùX4³b~!(f¸J9*(Òða|c3O^ç}Ø¶{¨B{aî*À¢vN£¸V£vFéuIùÍdLðYwwí©;Q[~±Àee{®ZY |
| --- | Minor | \Ø3Qø£Éø(³d¯â-TÆ®Í×¥YvsýÉ*uãxp28ø7+¦k;¸ë|4 |
| --- | Minor | kQl'£»H)äÍ÷*h( .DV^]:-O0Y6Y |
| --- | Minor |  ð¶(Z¼ |
| --- | Minor | ¤XjkÉ9³Áá°Ôù«/óCó ~säÐúIòµ[8É*Èy&b×3ï-oÊÌ+ÝºmL,KkM%» |
| --- | Minor | §P»±ø³ÙmÉx&F#º¨9sVódå |
| --- | Minor | *DGîS¤ÑwÁn}Üñ |
| --- | Minor | Éöaáî_ÇÒÇÂ N²Ö,æ©´·ø$ÛföÚfxIiºQß{­¥Øh¶±]<Í0 |
| --- | Minor | +ì¦ &Ä´dRsu?ýöóÒæ)Õî0Tº)À«¢ hÑ9YtáÒ< Ô~Ô4@­X©O6ãx)-Àî)ß¤ßkè¦m.pë>ÀF ÀbÞÔÍÐ`b^d©"©É!¯,ZXpÄ;lÌ2vübõ7¤²V`wèj!¯;-G°z¾(ºlóÉÑ'[©l?·0üß§Íe§ÿÅ'É#Â5¹´'±Ê?éqÞOÿqúËé÷Ó Û¬ëp±R.°¡# w]P©­n¥9èJsÄØÖDëfúô£±^ À@!QS@~ýùh- |
| --- | Minor | !ÏµAÿA~ÚbLtÄCuà¿ÐL!>ÁÚ |
| --- | Minor | zB3¹Õ4Ñ¬k<OPOä´fL |
| --- | Minor | $>ðéÇçDØe½c&¡¤ÄÀÉ<¢n²+1»Q¥9o.æ7 |
| --- | Minor | ÈZu.,Ö¹¨LhÌÞe\ÑÃéânv¸cHùMwhë¯ê"«ÄÑë]ÃáYi¨k*¢þ*ü*¼ÛZ÷¢9NtÐ®è[J¬­+»Mq^!3\ UÚÆ[T×±Ö½«Òï;o¯i¸PaïÉÓÕOá§kàã¦}ÞkÒ-¯ë ÍFL²æÃY¦Ï7Ü-¦ì]Â1¯W\!öÍGÝH#èhyCÁç¬÷emvV{ÕöµÏØÇ!Ý³üT$¨YtJ(¬ð¬ÍØÎ# *º£åiÏtwuiÂÓàoe^EÌrêB*§NR;ìoÍ»ö_dn^ù8F.þ¡pè¨®ã+<dwh#Î(Z#:¼©ÛLÞm}ÿrF?->maØäeg#fsÚõd,òJV£[NV"O¿:4â°ÅP<@<4Wdþ7.`£¥# áÃ-OýNàÅplMi»LhIgßq;Eö¹ ¡¼{Úó,N	¨»+ã`G_ö¾)îÊ!ù¼ãØN÷ØºyIúº¼èúÓÅåç§¢êL}ÍÜX]AóÇ¼Hðw&bwLDrÿÈO~Åüæ¦ð½Y,ùWYÀs LípZ~vYô¯ËÊ.ÔTk0ãEbGÉ |
| --- | Minor | g6ÂòìT86øfv%´,ðÏ1¶J2ß {Ü;®e­©øU5{Ï"ÅsUÿW^ïvU»y=Ç8e"ZåÉJÁE[^­öÇA#þÃ>' Å6#WA¹&ÖBûÎôÊ¶kyelÝéë¬Âé´¹Ms7'Tò0VW´ûO2¶-tÂÎîsÜ$H	üQíu¥åv§ÀPLtºÍ`¡JoÛ	¸¦Ò½kºv×i?áº²B:g¬ÜEÍ<Õ^Á=§§ëî0GÔÐ é6o«= |
| --- | Minor | ®ÐRKNåËûÛÏÇa³)Ie"þ7â§_«^ÀÍ{ýÕÞ¼®zkÐaLË4õ¤pQ·i	'µ 	kxGèBFu·y%:_É(ÌC­´ª,Ùåó&T´é,Q=J%÷>lè= ²á;ÙB'u¡Ö9Kíh)&`ü^ ýüj]¹pI?7:M	îÆ7çKòHNV±êD2Úq*ª´ÖnB0ºÊsT×5¡fø$³Ásóées ÅQ,«s1ÌÉZ?Ê»t63Z6;ån´BÓÅ»Î¶¾5}åâè*{5½&ïì~/<ÊQÕ§Kê¾Ûé^CRU0ÇÉÇÝ5¥o<¤Ú¢`]Üúæ¶J'gUp\NPS!ß»5­`SìÙ« ºe¨'º¶u³qTâïéá;åËÆjkIù°/ Ã×j§²þÇ³pèTqaTY°ÛkÏÎõNWzaToó<7À¡}VÝySMloHÌåsJÒ²åKX:k¡K4kFâp{Üñ0± X lßé°7î0.¸ÉÝ÷KðÀOñ\ï@GÈA¤Çh7¡o?>oHF Ñ=01·ÄîÜÅUKDpÚ#½Ma®ïn)L­e3¸=IXè<îgÅÌáëÃUÈm&Ûh÷«øN­ö«ªºÑ°jÜàÎûvÞ: +ÅÂuvÄ¾{Ûæt ÜéTj§Ø«AnRI¡¢ v"üD;¢÷µcyZ/]éÌ¬_«<Q·Jð	C´Y:r«O³p	9ñ}þôùàÃ,ìª^Áp°÷îÝÖ¸{8­²`ÓbÛY[{¦x´Bí/Úh]°éQ^Z2E³ßQu×&§´­¹G«8>ÑúVÕ×<W[ÿÜù8fæ7Ú'2Ã0sF± 5wêÔ¬ÔL\¯OàÖ±-³wåz	EWÜä¨R¿ÎI÷8*|O¸@úÌz(ú äQ4á`ÿgÆeçDvÉ$'£ª1kÃRsl/¢(âmÚoôC4¢wv?Q#ÈåÇÇ4t*¿_EÂiçÝ+Nä#c¢÷1ª:]sSf.ºK!yöZ>sëQÕIEº»yC¾ u§Ô¡µ |
| --- | Minor | áèL'ém?~º£Ýq Õ×2~ÒîãT,?Ã¥÷ÃI0ÿãç;¤Íø¨cÞÇz 2ÅdlT"IìöþUºmÖàë2;Û,2ÁEÕÆsix#åAsôþE­A§`?qR×¼%Ó~.ÆèÞ×z-äYúÔAÉå½ÖÓQKú3³}Ñ0,8­T+üüv=­}´m:g{7sÁ| AÕ§^ö¼NÕ7o+âw×*þï<{U )+Ö;OO#®ä¸lÜq©(I!éV°ëu¿¨Úßn"ÜÄ8º´yØñD æpæd Eg¾eïu&Óô¯bç¬Ê8r-þô¤s´ÅHÔ$»ãN³2»EaÄÆx²[exÌºø¨îjð³¢Ýã&R¶]B>²¼ÞýÝuYßI2æÍXæfcöÆM9Èt~ºÇâw²èíÒH³+ê oàvRuës»?Ïiõ7 ³câÑÎÄ~)QÙS{û» |
| --- | Minor | ¤P«dÞô[u)µ=¹±«+~ÒïÙ2òG(¦5#ü².£Óy¾Ë!|ä¦õj¸Ê+«Î,®ÞÖzÉ]W]EîaOTæoTÓñ2Îuø¦Ô¯´Oð+Qzªa×Î¾ú0ùh Wc` DËMhº,öàYÖDÄÃZ 'dÄÅw]ÑÓ9ìoüèno'÷XÖdôHÒøúª<ãÑM¶vÐFòÏo²*Aâ¦ÍS1Ê!ÓE·ùßÁ·cåça£3,«6»@AU66ÁÇuEÓ~#íz}áðm:ïüÏ~÷ßJÊµÊU /¢\Ó}F¹0Á¥o×IBgIÏM²%ÐKKXÇ' |
| --- | Minor | =u;¨³ÕÀñYZ*Ç-cNõ^±Ù,cTá(ä¦Ò¾O-GJhÝáY"¿§Í18wÇvÀ-ÙD[îÑ¥ß5(&EûÞ¸rmt¿5ÎÌ×rh¯\ÝâZÑz½ÿ4Çªé9ÕJB±Rþ×S¹V0µý6NP |
| --- | Minor | 'åßïð, U¦ÿlÜ(â |
| --- | Minor | Åæh<g{úÙuÇ_ÏLÁrg.§)Ïê8ÂÝfÜÆà\4ú z<ò~QeõåÎ² eõqa²¯or`ÿ·øj´°sË¤·kàMá,Xý{àsøpàHÎOÇÏzÖxê^Õz9R+ÞF7Esx[ï>ßÿÇæ;Ðí.ûû³ÝèôùÎ5ÏfÞhJLÌÛ¾c[z[¸ªwÓë©ëÅ[#cÅ8ô{ãP]:R'ªS+þÑ³Êèàº¿üÊ-l¸s³±Ó? |
| --- | Minor | Ïâ3DEÈ'9d:GëUõ|º¼ùX4³b~!(f¸J9*(Òða|c3O^ç}Ø¶{¨B{aî*À¢vN£¸V£vFéuIùÍdLðYwwí©;Q[~±Àee{®ZY |
| --- | Minor | \Ø3Qø£Éø(³d¯â-TÆ®Í×¥YvsýÉ*uãxp28ø7+¦k;¸ë|4 |
| --- | Minor | kQl'£»H)äÍ÷*h( .DV^]:-O0Y6Y |
| --- | Minor |  ð¶(Z¼ |
| --- | Minor | ¤XjkÉ9³Áá°Ôù«/óCó ~säÐúIòµ[8É*Èy&b×3ï-oÊÌ+ÝºmL. KkM%» |
| --- | Minor | §P»±ø³ÙmÉx&F#º¨9sVódå |
| --- | Minor | *DGîS¤ÑwÁn}Üñ |
| --- | Minor | Éöaáî_ÇÒÇÂ N²Ö. æ©´·ø$ÛföÚfxIiºQß{­¥Øh¶±]<Í0 |
| --- | Minor | +ì¦ &Ä´dRsu?ýöóÒæ)Õî0Tº)À«¢ hÑ9YtáÒ< Ô~Ô4@­X©O6ãx)-Àî)ß¤ßkè¦m.pë>ÀF ÀbÞÔÍÐ`b^d©"©É!¯. ZXpÄ;lÌ2vübõ7¤²V`wèj!¯;-G°z¾(ºlóÉÑ'[©l?·0üß§Íe§ÿÅ'É#Â5¹´'±Ê?éqÞOÿqúËé÷Ó Û¬ëp±R.°¡# w]P©­n¥9èJsÄØÖDëfúô£±^ À@!QS@~ýùh- |
| --- | Minor | !ÏµAÿA~ÚbLtÄCuà¿ÐL!>ÁÚ |
| --- | Minor | zB3¹Õ4Ñ¬k<OPOä´fL |
| --- | Minor | $>ðéÇçDØe½c&¡¤ÄÀÉ<¢n²+1»Q¥9o.æ7 |
| --- | Minor | ÈZu.. Ö¹¨LhÌÞe\ÑÃéânv¸cHùMwhë¯ê"«ÄÑë]ÃáYi¨k*¢þ*ü*¼ÛZ÷¢9NtÐ®è[J¬­+»Mq^!3\ UÚÆ[T×±Ö½«Òï;o¯i¸PaïÉÓÕOá§kàã¦}ÞkÒ-¯ë ÍFL²æÃY¦Ï7Ü-¦ì]Â1¯W\!öÍGÝH#èhyCÁç¬÷emvV{ÕöµÏØÇ!Ý³üT$¨YtJ(¬ð¬ÍØÎ# *º£åiÏtwuiÂÓàoe^EÌrêB*§NR;ìoÍ»ö_dn^ù8F.þ¡pè¨®ã+<dwh#Î(Z#:¼©ÛLÞm}ÿrF?->maØäeg#fsÚõd. òJV£[NV"O¿:4â°ÅP<@<4Wdþ7.`£¥# áÃ-OýNàÅplMi»LhIgßq;Eö¹ ¡¼{Úó. N	¨»+ã`G_ö¾)îÊ!ù¼ãØN÷ØºyIúº¼èúÓÅåç§¢êL}ÍÜX]AóÇ¼Hðw&bwLDrÿÈO~Åüæ¦ð½Y. ùWYÀs LípZ~vYô¯ËÊ.ÔTk0ãEbGÉ |
| --- | Minor | g6ÂòìT86øfv%´. ðÏ1¶J2ß {Ü;®e­©øU5{Ï"ÅsUÿW^ïvU»y=Ç8e"ZåÉJÁE[^­öÇA#þÃ>' Å6#WA¹&ÖBûÎôÊ¶kyelÝéë¬Âé´¹Ms7'Tò0VW´ûO2¶-tÂÎîsÜ$H	üQíu¥åv§ÀPLtºÍ`¡JoÛ	¸¦Ò½kºv×i?áº²B:g¬ÜEÍ<Õ^Á=§§ëî0GÔÐ é6o«= |
| --- | Minor | ®ÐRKNåËûÛÏÇa³)Ie"þ7â§_«^ÀÍ{ýÕÞ¼®zkÐaLË4õ¤pQ·i	'µ 	kxGèBFu·y%:_É(ÌC­´ª. Ùåó&T´é. Q=J%÷>lè= ²á;ÙB'u¡Ö9Kíh)&`ü^ ýüj]¹pI?7:M	îÆ7çKòHNV±êD2Úq*ª´ÖnB0ºÊsT×5¡fø$³Ásóées ÅQ. «s1ÌÉZ?Ê»t63Z6;ån´BÓÅ»Î¶¾5}åâè*{5½&ïì~/<ÊQÕ§Kê¾Ûé^CRU0ÇÉÇÝ5¥o<¤Ú¢`]Üúæ¶J'gUp\NPS!ß»5­`SìÙ« ºe¨'º¶u³qTâïéá;åËÆjkIù°/ Ã×j§²þÇ³pèTqaTY°ÛkÏÎõNWzaToó<7À¡}VÝySMloHÌåsJÒ²åKX:k¡K4kFâp{Üñ0± X lßé°7î0.¸ÉÝ÷KðÀOñ\ï@GÈA¤Çh7¡o?>oHF Ñ=01·ÄîÜÅUKDpÚ#½Ma®ïn)L­e3¸=IXè<îgÅÌáëÃUÈm&Ûh÷«øN­ö«ªºÑ°jÜàÎûvÞ: +ÅÂuvÄ¾{Ûæt ÜéTj§Ø«AnRI¡¢ v"üD;¢÷µcyZ/]éÌ¬_«<Q·Jð	C´Y:r«O³p	9ñ}þôùàÃ. ìª^Áp°÷îÝÖ¸{8­²`ÓbÛY[{¦x´Bí/Úh]°éQ^Z2E³ßQu×&§´­¹G«8>ÑúVÕ×<W[ÿÜù8fæ7Ú'2Ã0sF± 5wêÔ¬ÔL\¯OàÖ±-³wåz	EWÜä¨R¿ÎI÷8*|O¸@úÌz(ú äQ4á`ÿgÆeçDvÉ$'£ª1kÃRsl/¢(âmÚoôC4¢wv?Q#ÈåÇÇ4t*¿_EÂiçÝ+Nä#c¢÷1ª:]sSf.ºK!yöZ>sëQÕIEº»yC¾ u§Ô¡µ |
| --- | Minor | áèL'ém?~º£Ýq Õ×2~ÒîãT. ?Ã¥÷ÃI0ÿãç;¤Íø¨cÞÇz 2ÅdlT"IìöþUºmÖàë2;Û. 2ÁEÕÆsix#åAsôþE­A§`?qR×¼%Ó~.ÆèÞ×z-äYúÔAÉå½ÖÓQKú3³}Ñ0. 8­T+üüv=­}´m:g{7sÁ| AÕ§^ö¼NÕ7o+âw×*þï<{U )+Ö;OO#®ä¸lÜq©(I!éV°ëu¿¨Úßn"ÜÄ8º´yØñD æpæd Eg¾eïu&Óô¯bç¬Ê8r-þô¤s´ÅHÔ$»ãN³2»EaÄÆx²[exÌºø¨îjð³¢Ýã&R¶]B>²¼ÞýÝuYßI2æÍXæfcöÆM9Èt~ºÇâw²èíÒH³+ê oàvRuës»?Ïiõ7 ³câÑÎÄ~)QÙS{û» |
| --- | Minor | ¤P«dÞô[u)µ=¹±«+~ÒïÙ2òG(¦5#ü².£Óy¾Ë!|ä¦õj¸Ê+«Î. ®ÞÖzÉ]W]EîaOTæoTÓñ2Îuø¦Ô¯´Oð+Qzªa×Î¾ú0ùh Wc` DËMhº. öàYÖDÄÃZ 'dÄÅw]ÑÓ9ìoüèno'÷XÖdôHÒøúª<ãÑM¶vÐFòÏo²*Aâ¦ÍS1Ê!ÓE·ùßÁ·cåça£3. «6»@AU66ÁÇuEÓ~#íz}áðm:ïüÏ~÷ßJÊµÊU /¢\Ó}F¹0Á¥o×IBgIÏM²%ÐKKXÇ' |
| --- | Minor | =u;¨³ÕÀñYZ*Ç-cNõ^±Ù. cTá(ä¦Ò¾O-GJhÝáY"¿§Í18wÇvÀ-ÙD[îÑ¥ß5(&EûÞ¸rmt¿5ÎÌ×rh¯\ÝâZÑz½ÿ4Çªé9ÕJB±Rþ×S¹V0µý6NP |
| --- | Minor | 'åßïð.  U¦ÿlÜ(â |
| --- | Minor | Åæh<g{úÙuÇ_ÏLÁrg.§)Ïê8ÂÝfÜÆà\4ú z<ò~QeõåÎ² eõqa²¯or`ÿ·øj´°sË¤·kàMá. Xý{àsøpàHÎOÇÏzÖxê^Õz9R+ÞF7Esx[ï>ßÿÇæ;Ðí.ûû³ÝèôùÎ5ÏfÞhJLÌÛ¾c[z[¸ªwÓë©ëÅ[#cÅ8ô{ãP]:R'ªS+þÑ³Êèàº¿üÊ-l¸s³±Ó?. |
| --- | Minor | Sentence exceeds complexity threshold, split for readability. Applying the split needs --strength moderate or higher. |
| --- | Minor | none (split proposal only; source not rewritten) |
| --- | Minor | none |
| --- | Minor | Check: NEEDS-LLM |
| --- | Minor | Flags:    not-assessed |
| --- | Minor | SENTENCE (Line 3, 161 words, 2 clauses)  [Script] |
| --- | Minor | °}w|n	øI¿8lçÊiôÉh#ûØHßå-T+Ùyb2)´7üð³ÿ37¬ð endstream endobj 54 0 obj <</Filter/FlateDecode/Length 5275>> stream xÚµ\K ñø"È§¿=É'þÉ'OVúÃÇÿ¾ýox÷køÿ?þýËÓ¿ý| _õôåý	@*B)O_n¾¡ô¸ðWË·¿|ù¯XM>Iqxás±æ+ªâÓ«ÆÃ­<Õ½ þÞÞÀgãß^ÁðËÞâÛòUÄ/áÿòNAùv¥õ%¿1T|2ù{ (µjsåkl)|)OðNµéKø+Ø¶¹HIü(üj¹\Óºü |
| --- | Minor | v¸æv" |
| --- | Minor | ±,4C1Dz¼[PûÏ±8âø.>çë(Â,5Ñrzc¾á8ÇFêÅUO¯°0PVF~µQR/×<<öúÕg:âÛDCzk!÷ÞÆuaëfÛ<«+Õ-³Yg{¬¹ ÎU#Íj«VyYD¢ÕïèMí§7q&lh\«·×njRÅAùb©øµVmÜÃx"÷òÞn}çYlcZeî å6kÓ¤Ê!¾KÒb;4¿"m~o³Vw£RZÓ®~WË 6¬Ð¾@ÖóWê¥UcÑC[í üé¡ÖjµA!6 |
| --- | Minor | )XK |
| --- | Minor | ê#°¦R¿Û´@Q;5/kÖµ§ß^µL< ËÄ^§­úÃ"KÃhµ¯:HGé¡¦yPÑA **jÍBÜ/hÿXDE¢Là{! |
| --- | Minor | °}w|n	øI¿8lçÊiôÉh#ûØHßå-T+Ùyb2)´7üð³ÿ37¬ð endstream endobj 54 0 obj <</Filter/FlateDecode/Length 5275>> stream xÚµ\K ñø"È§¿=É'þÉ'OVúÃÇÿ¾ýox÷køÿ?þýËÓ¿ý| _õôåý	@*B)O_n¾¡ô¸ðWË·¿|ù¯XM>Iqxás±æ+ªâÓ«ÆÃ­<Õ½ þÞÞÀgãß^ÁðËÞâÛòUÄ/áÿòNAùv¥õ%¿1T|2ù{ (µjsåkl)|)OðNµéKø+Ø¶¹HIü(üj¹\Óºü |
| --- | Minor | v¸æv" |
| --- | Minor | ±. 4C1Dz¼[PûÏ±8âø.>çë(Â. 5Ñrzc¾á8ÇFêÅUO¯°0PVF~µQR/×<<öúÕg:âÛDCzk!÷ÞÆuaëfÛ<«+Õ-³Yg{¬¹ ÎU#Íj«VyYD¢ÕïèMí§7q&lh\«·×njRÅAùb©øµVmÜÃx"÷òÞn}çYlcZeî å6kÓ¤Ê!¾KÒb;4¿"m~o³Vw£RZÓ®~WË 6¬Ð¾@ÖóWê¥UcÑC[í üé¡ÖjµA!6 |
| --- | Minor | )XK |
| --- | Minor | ê#°¦R¿Û´@Q;5/kÖµ§ß^µL< ËÄ^§­úÃ"KÃhµ¯:HGé¡¦yPÑA **jÍBÜ/hÿXDE¢Là{!. |
| --- | Minor | Sentence exceeds complexity threshold, split for readability. Applying the split needs --strength moderate or higher. |
| --- | Minor | none (split proposal only; source not rewritten) |
| --- | Minor | none |
| --- | Minor | Check: NEEDS-LLM |
| --- | Minor | Flags:    not-assessed |
| --- | Minor | SENTENCE (Line 34, 77 words, 1 clauses)  [Script] |
| --- | Minor | ¤·z*:Y°9³KpåH î¥ÕXÔM ø7SàR]®µ ( ðMLìPVÀ/Øuö¨ðE.=ÿûdoå£R8\èBu:@,ûßhÈ2ÒÈÊþô<5ÿüýÿþúõy;!­HB>R¿¼jýüÛ5Iá¥îM¡°Avò²__6¨UjTôj÷UAP°Æ_yïR¹#^:aÊ»m´ÉÔC¦#ûÚè­&Ç£¤"¹#5#ôâ2Y»¡-wáîG-'¡Yñæ¼æz$p	ÏHÔ¥ú¤HõÚÎnÜ^ÒyOÓ»²!:Z_ùnød}D­æ'ôZV­ ôÆÈIµ^4xSAðë^Í­ÇnÑo¬2|÷¬Gó¸²wá¥Ý"å! |
| --- | Minor | ¤·z*:Y°9³KpåH î¥ÕXÔM ø7SàR]®µ ( ðMLìPVÀ/Øuö¨ðE.=ÿûdoå£R8\èBu:@. ûßhÈ2ÒÈÊþô<5ÿüýÿþúõy;!­HB>R¿¼jýüÛ5Iá¥îM¡°Avò²__6¨UjTôj÷UAP°Æ_yïR¹#^:aÊ»m´ÉÔC¦#ûÚè­&Ç£¤"¹#5#ôâ2Y»¡-wáîG-'¡Yñæ¼æz$p	ÏHÔ¥ú¤HõÚÎnÜ^ÒyOÓ»²!:Z_ùnød}D­æ'ôZV­ ôÆÈIµ^4xSAðë^Í­ÇnÑo¬2|÷¬Gó¸²wá¥Ý"å!. |
| --- | Minor | Sentence exceeds complexity threshold, split for readability. Applying the split needs --strength moderate or higher. |
| --- | Minor | none (split proposal only; source not rewritten) |
| --- | Minor | none |
| --- | Minor | Check: NEEDS-LLM |
| --- | Minor | Flags:    not-assessed |
| --- | Minor | SENTENCE (Line 34, 120 words, 2 clauses)  [Script] |
| --- | Minor | l;á½Çù­8c¸Í÷RÑÜ9ÔÄ502$1!Ch*s2Ë êh×iJ¦ù¸ d,'vdéüåDUä%úB*Á¼´cNv¨A {TH¹¢EzÛ1ðó^À>ÿñçMë¡  |
| --- | Minor | ">áár¥ <Sø=h±°ÏòÛ h¶"a[-Ç;a!@*¼jVéFFø-FÆ]ÄÙu+7ävìn5 DDaâÒ[ qã´,8zq¦4zMgÇh¹¯HÎa¶ôx;|1ïùEJÜTFu¤7}-ï:æØF#3-kjãèW5û-oà:¡ekçó¯ÑsK´Üx-nnq(( ï±ÝBxçÇ0¿*MT±Nö­Ú¥ê5 Ùæ ­ýE£éI	 è(qÐyï5reûºÈAÝÜÇ#`D [ÇÊ"âµÆ |
| --- | Minor | Ö/kÜ`Pê¢¬½kÃ³J\§æ4ÐvdÃ0hàä*%Qú-z³B¥¶rx°2gË#HÃièY ù³y(¥RÍæ#íÒr´%Z( ? |
| --- | Minor | l;á½Çù­8c¸Í÷RÑÜ9ÔÄ502$1!Ch*s2Ë êh×iJ¦ù¸ d. 'vdéüåDUä%úB*Á¼´cNv¨A {TH¹¢EzÛ1ðó^À>ÿñçMë¡  |
| --- | Minor | ">áár¥ <Sø=h±°ÏòÛ h¶"a[-Ç;a!@*¼jVéFFø-FÆ]ÄÙu+7ävìn5 DDaâÒ[ qã´. 8zq¦4zMgÇh¹¯HÎa¶ôx;|1ïùEJÜTFu¤7}-ï:æØF#3-kjãèW5û-oà:¡ekçó¯ÑsK´Üx-nnq(( ï±ÝBxçÇ0¿*MT±Nö­Ú¥ê5 Ùæ ­ýE£éI	 è(qÐyï5reûºÈAÝÜÇ#`D [ÇÊ"âµÆ |
| --- | Minor | Ö/kÜ`Pê¢¬½kÃ³J\§æ4ÐvdÃ0hàä*%Qú-z³B¥¶rx°2gË#HÃièY ù³y(¥RÍæ#íÒr´%Z( ?. |
| --- | Minor | Sentence exceeds complexity threshold, split for readability. Applying the split needs --strength moderate or higher. |
| --- | Minor | none (split proposal only; source not rewritten) |
| --- | Minor | none |
| --- | Minor | Check: NEEDS-LLM |
| --- | Minor | Flags:    not-assessed |
| --- | Minor | SENTENCE (Line 34, 135 words, 2 clauses)  [Script] |
| --- | Minor | Iá<(¬ }=AÈRèçZ¤sÈI¥:fR¬b©i5ÖÛç3åAÃe4EIp4=Òwóª¦×ºRÃÖ&ï	ü4þ,KX |
| --- | Minor | Mo©©ÏkÛ"nEQ\§Ô}ÙÉ+Ú>qB2Yëð2Ø~öiÞÖ&r¯ß7öqó#ów@oË@ßoZ'WÏI>ÕÖ9ºäl~`[jã9õmýºØþÐÒæ.îÁõ¡¹8·FÌ£Kq(ÐVw¶A°º |
| --- | Minor | ÒR¹¿?¼ÁÎ3GÜxZ |
| --- | Minor | Uù%)VãIÌaËskpÀÔl-õ>péCxíå6mtF~2jâ¨9:R^)Ò`qc½Jí9Úû<çÕðÀv`ä¤05ØÐMDz3¢APë£]mÛÜ> §GÔ1#GÄÐi G@r¨-%ù° Ar}Dg¦Ì§´êN!k¢2:¢ÒoÝÂ	Õ; Â¨­Í>ï"=)tBÏüÎËÓÌàÀÃi©ö®P_ ç¹Gñ×j§<¿"çç F}éì÷ò5ã ¼XÁþÂq÷ZñV´V,S±G-póÞÓßq#Ë°<áºÃKk­qJ6êIÉÕÎAñÇ! |
| --- | Minor | Iá<(¬ }=AÈRèçZ¤sÈI¥:fR¬b©i5ÖÛç3åAÃe4EIp4=Òwóª¦×ºRÃÖ&ï	ü4þ. KX |
| --- | Minor | Mo©©ÏkÛ"nEQ\§Ô}ÙÉ+Ú>qB2Yëð2Ø~öiÞÖ&r¯ß7öqó#ów@oË@ßoZ'WÏI>ÕÖ9ºäl~`[jã9õmýºØþÐÒæ.îÁõ¡¹8·FÌ£Kq(ÐVw¶A°º |
| --- | Minor | ÒR¹¿?¼ÁÎ3GÜxZ |
| --- | Minor | Uù%)VãIÌaËskpÀÔl-õ>péCxíå6mtF~2jâ¨9:R^)Ò`qc½Jí9Úû<çÕðÀv`ä¤05ØÐMDz3¢APë£]mÛÜ> §GÔ1#GÄÐi G@r¨-%ù° Ar}Dg¦Ì§´êN!k¢2:¢ÒoÝÂ	Õ; Â¨­Í>ï"=)tBÏüÎËÓÌàÀÃi©ö®P_ ç¹Gñ×j§<¿"çç F}éì÷ò5ã ¼XÁþÂq÷ZñV´V. S±G-póÞÓßq#Ë°<áºÃKk­qJ6êIÉÕÎAñÇ!. |
| --- | Minor | Sentence exceeds complexity threshold, split for readability. Applying the split needs --strength moderate or higher. |
| --- | Minor | none (split proposal only; source not rewritten) |
| --- | Minor | none |
| --- | Minor | Check: NEEDS-LLM |
| --- | Minor | Flags:    not-assessed |
| --- | Minor | SENTENCE (Line 34, 83 words, 0 clauses)  [Script] |
| --- | Minor | akôQ}¹æ¥@ªÇÝù=«C³¥ ÞØÚ^¸àGMfk®×«vm/}â{CÇf´ÒF÷Ëµ	l&»[;UR 7Ö¶ÎÃlU20ýÓþÓ)øèÎ 4ÿ;ßÃ>TYu´ü@eg`tp â¡WÑãÏ Þ¨Ö ý× z Vô1Ò3f%÷àn¤×°´r>×«M¬'¯Ü/ãÚÂ8Õ0rä×ÙÈnPð |
| --- | Minor | §q¥Ôù/iØ~þ·eQ5TËàc7_³¨+çát¸F)VRÁýÜê±v !Ó ÌCäæZÖµÓy²ôænÀ 4y'L¯Ãð'caúÆÉVº¥n¨»£¥kF® ÎN¦´³Ûc8'cnvD*ÁA-´ó[´ªÛR>#I§£ªÆ |
| --- | Minor | akôQ}¹æ¥@ªÇÝù=«C³¥ ÞØÚ^¸àGMfk®×«vm/}â{CÇf´ÒF÷Ëµ	l&»[;UR 7Ö¶ÎÃlU20ýÓþÓ)øèÎ 4ÿ;ßÃ>TYu´ü@eg`tp â¡WÑãÏ Þ¨Ö ý× z Vô1Ò3f%÷àn¤×°´r>×«M¬'¯Ü/ãÚÂ8Õ0rä×ÙÈnPð |
| --- | Minor | §q¥Ôù/iØ~þ·eQ5TËàc7_³¨+çát¸F)VRÁýÜê±v !Ó ÌCäæZÖµÓy²ôænÀ 4y'L¯Ãð'caúÆÉVº¥n¨»£¥kF® ÎN¦´³Ûc8'cnvD*ÁA-´ó[´ªÛR>#I§£ªÆ |
| --- | Minor | Sentence exceeds complexity threshold, split for readability. Applying the split needs --strength moderate or higher. |
| --- | Minor | none (split proposal only; source not rewritten) |
| --- | Minor | none |
| --- | Minor | Check: NEEDS-LLM |
| --- | Minor | Flags:    not-assessed |
| --- | Minor | SENTENCE (Line 51, 129 words, 4 clauses)  [Script] |
| --- | Minor | BEÅÖnÅ_ÄmLø÷Cä_kËr,UÂê&B<!-~ÅkçädÒÏEÐáImÐ¨¥§®\nTw>Ìê\óÚáþQãê1î,DðGÁ¨ej¯ù%ÛÁMÂ3ï`NÝ¥ãvð,¹=%æFnÏMtÁ¥erÅ¯vS­Kis3þa®Ïõ!ð¨0¡ [`ã9£}ÓWVö'ÊuÚµ¿ã65Ë³ZPkõ­ ¥w.Çè·ÕC8Kù |
| --- | Minor | )%oÔ ­×ð¬7Êd:3^"pçä­0Z¨'tH,À¿òKhF`nñ+ÏNÌù)0[¹^@½5w¼è¾]î_äÕ|WH'¥Çë>À}Ä×Î¥yÆXu2¡KV)½USÃµê<õ:¢÷â´Pé<±«¿:£Ó_ÜQøÌ»)Î+?Æáë5ëôAlÕ³PÒéÖrEÄDÏ¦SIqéÅB[C ½u5(ö]ìÓYX¬æ}Ä³ÀP ê%(P³]*C £?¶T¿ß?aÉ]_QMGÑ£-EH¯çÂØC(æaz ¶µé<»saD÷áS|¹?Åê2ÅgµË'§Y;ynuçvÔ(9? |
| --- | Minor | BEÅÖnÅ_ÄmLø÷Cä_kËr. UÂê&B<!-~ÅkçädÒÏEÐáImÐ¨¥§®\nTw>Ìê\óÚáþQãê1î. DðGÁ¨ej¯ù%ÛÁMÂ3ï`NÝ¥ãvð. ¹=%æFnÏMtÁ¥erÅ¯vS­Kis3þa®Ïõ!ð¨0¡ [`ã9£}ÓWVö'ÊuÚµ¿ã65Ë³ZPkõ­ ¥w.Çè·ÕC8Kù |
| --- | Minor | )%oÔ ­×ð¬7Êd:3^"pçä­0Z¨'tH. À¿òKhF`nñ+ÏNÌù)0[¹^@½5w¼è¾]î_äÕ|WH'¥Çë>À}Ä×Î¥yÆXu2¡KV)½USÃµê<õ:¢÷â´Pé<±«¿:£Ó_ÜQøÌ»)Î+?Æáë5ëôAlÕ³PÒéÖrEÄDÏ¦SIqéÅB[C ½u5(ö]ìÓYX¬æ}Ä³ÀP ê%(P³]*C £?¶T¿ß?aÉ]_QMGÑ£-EH¯çÂØC(æaz ¶µé<»saD÷áS|¹?Åê2ÅgµË'§Y;ynuçvÔ(9?. |
| --- | Minor | Sentence exceeds complexity threshold, split for readability. Applying the split needs --strength moderate or higher. |
| --- | Minor | none (split proposal only; source not rewritten) |
| --- | Minor | none |
| --- | Minor | Check: NEEDS-LLM |
| --- | Minor | Flags:    not-assessed |
| --- | Minor | SENTENCE (Line 51, 134 words, 3 clauses)  [Script] |
| --- | Minor | i&Î¸ù²çTÞ®2ÄÎkJÚjK5C!A"y°²gbü¨~ÈÃ%ÑN9¶¹OüVÒñFÒ^÷	ãR©é+éw¿ä·÷ °!dd»e8½>¿yíºHD¼ô'Va«Ïûo^æÜC³KOëàÒp8tç54O·;1ß:Ï*éí#÷ýqËº3!8hçì@8±?óI<^B.¢uA&"¤ª·UéíáÐGg~¬y/%æôGL§"g·Kz¼É§Óù5ÆªÍí-ùé`lòÈj¦cwûÜvq?ªÅð×ÓÎ08û¤qMMKG°ä$IÐeP;» |
| --- | Minor | **/ºõ²-ï|Kîe´¢Æö`âýBÎRYñfçdDÍ ¿05ÅNW`JC*Q	àvgö¾;Ò"hGp:{¼À6§®PpÁ5,\xèÖÄ |
| --- | Minor | ¾8¨Tðïzt·R9 ÉÞ®Vzd~póg_T |
| --- | Minor | ·U¯ßÑ[¿T,sAiXlÈ |
| --- | Minor | ÒÝYF®õx+& ©ËÎY¡õø¶Ù¬'H©à][ê_÷!¬´Ìv8iÑt°V½J,ÏÅÈtD;D÷ÆÏdmÂYÁ/tÆùÏßû²u¢S¼å! |
| --- | Minor | i&Î¸ù²çTÞ®2ÄÎkJÚjK5C!A"y°²gbü¨~ÈÃ%ÑN9¶¹OüVÒñFÒ^÷	ãR©é+éw¿ä·÷ °!dd»e8½>¿yíºHD¼ô'Va«Ïûo^æÜC³KOëàÒp8tç54O·;1ß:Ï*éí#÷ýqËº3!8hçì@8±?óI<^B.¢uA&"¤ª·UéíáÐGg~¬y/%æôGL§"g·Kz¼É§Óù5ÆªÍí-ùé`lòÈj¦cwûÜvq?ªÅð×ÓÎ08û¤qMMKG°ä$IÐeP;» |
| --- | Minor | **/ºõ²-ï|Kîe´¢Æö`âýBÎRYñfçdDÍ ¿05ÅNW`JC*Q	àvgö¾;Ò"hGp:{¼À6§®PpÁ5. \xèÖÄ |
| --- | Minor | ¾8¨Tðïzt·R9 ÉÞ®Vzd~póg_T |
| --- | Minor | ·U¯ßÑ[¿T. sAiXlÈ |
| --- | Minor | ÒÝYF®õx+& ©ËÎY¡õø¶Ù¬'H©à][ê_÷!¬´Ìv8iÑt°V½J. ÏÅÈtD;D÷ÆÏdmÂYÁ/tÆùÏßû²u¢S¼å!. |
| --- | Minor | Sentence exceeds complexity threshold, split for readability. Applying the split needs --strength moderate or higher. |
| --- | Minor | none (split proposal only; source not rewritten) |
| --- | Minor | none |
| --- | Minor | Check: NEEDS-LLM |
| --- | Minor | Flags:    not-assessed |
| --- | Minor | SENTENCE (Line 51, 576 words, 10 clauses)  [Script] |
| --- | Minor | Q»J÷ i9ÝB'é\ tg)_ÙµÙIÂJÅ¯f¼4Pmov4ÀeeÈîò]+|¤Ã40hc²ûØÑrçò³:¯ÒÏ¾Òö"¹D%ðCýÛlg*ÑÅË@½N5íã@dîî¥Ü²¿Qh A~lÍL5Gß3"aæÈu+Á²ëÛ¶SïÕe´bÕäÛÃkäö§sx¨a>Õ¿NG×ª{³.v³¼#á×TÍ>üèkËt·µútñ<dÊ&_âVÜØè´Í.¯_@¶ê¢ÈÍFv÷+ÚC:©e°Á|0mÛW²Æÿø/ÿ­a¾ endstream endobj 97 0 obj <</Filter/FlateDecode/Length 5139>> stream xÚ­\I$;n¾ûWäÁúaPa¢6#§À7}³}èì|5§9øê_oj¡D-KÏëF¡*#´ùqQ^þ÷¢/þë×ñéßåç_éÙ_èçß/ÿüýòÿ¦/ôÆÃË÷¯6ê°!ºà¡¹|¿ÿ×U)èG}Nßéè'*J)}£ßôè·ùRÊêÔþ¦6ðõùa¼§^ð£¼I-§ßùmiÕzCjê|ù |
| --- | Minor | =µXþNcbmmnÿóý?hõö¢ÕUT!¤õD{8k´¹|Xsg1Ö¤ù |
| --- | Minor |  ??é»¦uÓl1ý·2þYwvï;àwxÿ4y÷1õ²×´ÏôÄx'QÄ|Õ}ä'iÄ´ËôÃ#ºúß9ÈLÙÔ:¯'õdJºk­Çm×µF9b+3ì3 ýöð	¡.Ö ¹öe¤ÁÓÔrÂÆÄkù[VFä¿!1 0Âå¶n53ò+/òB80DmbÔ¥iâ	r{ª Éç9ï-µJoª`å>C÷ºÿÖ®ï%\ûâ3J |
| --- | Minor | )\gÞÇe!,©ÇÉÓYæxgÕA;xÃ[ú(òíö[m |
| --- | Minor | Ðèþè­ÿ[ãØhl |
| --- | Minor | ¶ÈÅ·?s³Iñi8¬¶¡*oÿM?0JUÎ¾©EÚ-ZnõO'cCetm:þ¶níh¦Ë6Ü?÷ÓúµPü¿i#Ù(TøIü» Ið"ùÙ)&u,fBVyµ(5RU{| »-çÓ8<¢ÇèçóÙOK¬Ç:?¹ñwQQ]Åéh¦n|Íú­Ü£Y²ÑÁêÈýÓ,Ò6¢ïQÞª?@Q;ÿTMdÿü!øö'8Ù8RóÊ·öbß¢¼:U#fÃ1¢Ìí!VdRôu¼v<ônÆ0­/AFf}Ôu,cÝ²4u_ìqóÎ,ö¤YWao}Î4FLjí®=Ü«U/ýåª}´yHocÜæ±ÍM­aUgåá,­ïeatEþ@}eOmëª4í?\iÈÖÊÿKû³CåN´Ì <Óu¹kÐ¸ ºfß6¸GájÕ¶t Éa20Kïs[§ÓJþÊRLl(xÑlð6Åj·Iÿ0Ú`Ellý¤¦25ÌÜÁuwÑ¸mÓÜnK]ÄK^6;VÉqGØëiËC.K{ú3ÔÂUGÕå%t-ì­XS9êk÷pYº§I&­o=÷íÊ`"{{Ax-j¯Uõ¬½ÕøY7:H<g¤ç ¾M¶¾ö äÞêô7÷{"ZyrKh1ßQÄ(YØ.Ð^¨º # Bk];@¸vytÜ3Ç!B(â¸½FYU{WÝï±hfØ°UT¼Å:þí¶+v6½`-/\âdÀcÅèå/	PF_W­!£da ëïæÜÅóÖK»>ÑiÌ®wg¿%¯;YnBnuXcÓRFg~OOÍäp´Tpísf K_i`K{øêæa2 O1­q,&Øp_£»lv¤Pdh N"N]bã¥Zèæ»îQË°Yqäææù|uû^]Ð eNÞ`&ûUBpË"¼'jÓ¾"®z² ¸Ùb~/RÎ+ËÆÓ)i<z]3"º#:iÆºÀÄCE°SññFãtÐ~$ÛN;!#¿çfþ «ÚJíÅðÝ	4Õ¸W¨Ý&uòà8dåÌµºOÎàs¦Þ;ë × Ä`Jëgâd×R`&3æÜÓDÈ×EÈDK&Ò·þDPÁñ±=Á_H`\+°áÍÙ.$ä:-(©{rÌGç5cÕôìæfn³ëÒtn=ü,ªðÌd[Ñ§ýX8:×Rq·0âE²VcgddðU ­i:³.f~ÂHò¸QùµçÃ.²QÌãVÊ{µ¡xeÐ/Ñ%ÂÒEömºu8ÈmÚQô%	tL´Ïçd%IxÙkIï¶¦ìRjÆòÃ­Yy	U(QÏ¾gõ.æ¥Ø%xçmf?ë­J}|~ ?ÐzÌ£³mÐÌQ;Z?ÒúAÐoø:9}ò çYY?2uª\{¾áhôµÑèuì%ëegð+	ðjÅ8&Ú5ZØ)HEDG+S8¨YûAWtlø-°9dÊ~±­¦¤m(ÇÅî½¶¢e5¾Ï}H1 «NÄLQ8H5´iíµeYSp¤¯ák:ÝäwËFy·Ã |
| --- | Minor | ºÎÒÏÞ$Æ£nâ ås |
| --- | Minor | I<+ü4¯¡e,æj2iq¨(Å§U×!ö¾sl¯nyvãÕwZæ¸>6á¨q}uX¬[²¨/æbil¾¬°nñ-,Á{#ax=Û! |
| --- | Minor | Q»J÷ i9ÝB'é\ tg)_ÙµÙIÂJÅ¯f¼4Pmov4ÀeeÈîò]+|¤Ã40hc²ûØÑrçò³:¯ÒÏ¾Òö"¹D%ðCýÛlg*ÑÅË@½N5íã@dîî¥Ü²¿Qh A~lÍL5Gß3"aæÈu+Á²ëÛ¶SïÕe´bÕäÛÃkäö§sx¨a>Õ¿NG×ª{³.v³¼#á×TÍ>üèkËt·µútñ<dÊ&_âVÜØè´Í.¯_@¶ê¢ÈÍFv÷+ÚC:©e°Á|0mÛW²Æÿø/ÿ­a¾ endstream endobj 97 0 obj <</Filter/FlateDecode/Length 5139>> stream xÚ­\I$;n¾ûWäÁúaPa¢6#§À7}³}èì|5§9øê_oj¡D-KÏëF¡*#´ùqQ^þ÷¢/þë×ñéßåç_éÙ_èçß/ÿüýòÿ¦/ôÆÃË÷¯6ê°!ºà¡¹|¿ÿ×U)èG}Nßéè'*J)}£ßôè·ùRÊêÔþ¦6ðõùa¼§^ð£¼I-§ßùmiÕzCjê|ù |
| --- | Minor | =µXþNcbmmnÿóý?hõö¢ÕUT!¤õD{8k´¹|Xsg1Ö¤ù |
| --- | Minor |  ??é»¦uÓl1ý·2þYwvï;àwxÿ4y÷1õ²×´ÏôÄx'QÄ|Õ}ä'iÄ´ËôÃ#ºúß9ÈLÙÔ:¯'õdJºk­Çm×µF9b+3ì3 ýöð	¡.Ö ¹öe¤ÁÓÔrÂÆÄkù[VFä¿!1 0Âå¶n53ò+/òB80DmbÔ¥iâ	r{ª Éç9ï-µJoª`å>C÷ºÿÖ®ï%\ûâ3J |
| --- | Minor | )\gÞÇe!. ©ÇÉÓYæxgÕA;xÃ[ú(òíö[m |
| --- | Minor | Ðèþè­ÿ[ãØhl |
| --- | Minor | ¶ÈÅ·?s³Iñi8¬¶¡*oÿM?0JUÎ¾©EÚ-ZnõO'cCetm:þ¶níh¦Ë6Ü?÷ÓúµPü¿i#Ù(TøIü» Ið"ùÙ)&u. fBVyµ(5RU{| »-çÓ8<¢ÇèçóÙOK¬Ç:?¹ñwQQ]Åéh¦n|Íú­Ü£Y²ÑÁêÈýÓ. Ò6¢ïQÞª?@Q;ÿTMdÿü!øö'8Ù8RóÊ·öbß¢¼:U#fÃ1¢Ìí!VdRôu¼v<ônÆ0­/AFf}Ôu. cÝ²4u_ìqóÎ. ö¤YWao}Î4FLjí®=Ü«U/ýåª}´yHocÜæ±ÍM­aUgåá. ­ïeatEþ@}eOmëª4í?\iÈÖÊÿKû³CåN´Ì <Óu¹kÐ¸ ºfß6¸GájÕ¶t Éa20Kïs[§ÓJþÊRLl(xÑlð6Åj·Iÿ0Ú`Ellý¤¦25ÌÜÁuwÑ¸mÓÜnK]ÄK^6;VÉqGØëiËC.K{ú3ÔÂUGÕå%t-ì­XS9êk÷pYº§I&­o=÷íÊ`"{{Ax-j¯Uõ¬½ÕøY7:H<g¤ç ¾M¶¾ö äÞêô7÷{"ZyrKh1ßQÄ(YØ.Ð^¨º # Bk];@¸vytÜ3Ç!B(â¸½FYU{WÝï±hfØ°UT¼Å:þí¶+v6½`-/\âdÀcÅèå/	PF_W­!£da ëïæÜÅóÖK»>ÑiÌ®wg¿%¯;YnBnuXcÓRFg~OOÍäp´Tpísf K_i`K{øêæa2 O1­q. &Øp_£»lv¤Pdh N"N]bã¥Zèæ»îQË°Yqäææù|uû^]Ð eNÞ`&ûUBpË"¼'jÓ¾"®z² ¸Ùb~/RÎ+ËÆÓ)i<z]3"º#:iÆºÀÄCE°SññFãtÐ~$ÛN;!#¿çfþ «ÚJíÅðÝ	4Õ¸W¨Ý&uòà8dåÌµºOÎàs¦Þ;ë × Ä`Jëgâd×R`&3æÜÓDÈ×EÈDK&Ò·þDPÁñ±=Á_H`\+°áÍÙ.$ä:-(©{rÌGç5cÕôìæfn³ëÒtn=ü. ªðÌd[Ñ§ýX8:×Rq·0âE²VcgddðU ­i:³.f~ÂHò¸QùµçÃ.²QÌãVÊ{µ¡xeÐ/Ñ%ÂÒEömºu8ÈmÚQô%	tL´Ïçd%IxÙkIï¶¦ìRjÆòÃ­Yy	U(QÏ¾gõ.æ¥Ø%xçmf?ë­J}|~ ?ÐzÌ£³mÐÌQ;Z?ÒúAÐoø:9}ò çYY?2uª\{¾áhôµÑèuì%ëegð+	ðjÅ8&Ú5ZØ)HEDG+S8¨YûAWtlø-°9dÊ~±­¦¤m(ÇÅî½¶¢e5¾Ï}H1 «NÄLQ8H5´iíµeYSp¤¯ák:ÝäwËFy·Ã |
| --- | Minor | ºÎÒÏÞ$Æ£nâ ås |
| --- | Minor | I<+ü4¯¡e. æj2iq¨(Å§U×!ö¾sl¯nyvãÕwZæ¸>6á¨q}uX¬[²¨/æbil¾¬°nñ-. Á{#ax=Û!. |
| --- | Minor | Sentence exceeds complexity threshold, split for readability. Applying the split needs --strength moderate or higher. |
| --- | Minor | none (split proposal only; source not rewritten) |
| --- | Minor | none |
| --- | Minor | Check: NEEDS-LLM |
| --- | Minor | Flags:    not-assessed |
| --- | Minor | SENTENCE (Line 51, 553 words, 6 clauses)  [Script] |
| --- | Minor | ñ.É<þ¸«^3ÓÉFY¤Ò]e¹¬`?ÇT#	Aä.R"Y<íN×{?£),6TDs@ìXÔ²Ç*ÉÔö.Í8ÁËM Ý`û¢C3-u÷Ìª´àà6ày« ÿ^õ¯êúK¥Íé^2ñóMA^ûY ÆVî |
| --- | Minor | Dc	AN¯ia6¢_çVBv<xÂ.VVù`´-¶Êäâ·R¯í}È	ÁbàPxÌë4¿¬Þ PeMhðªlüNöHÏØëXHÂµ¥+DÜ¸êeË}8T7W½+·¬0q+ÝW |
| --- | Minor | ?¹b m+súÑÝ;½.°-Ü |
| --- | Minor | ë*ù)kÞ¼Zÿþ^¬hrKá ÖÔy£^>¹³qYÉ 5÷¨3­Dô¯¤¤ù8ØúHx |
| --- | Minor | ^*dóÇAêÔ Oüà´;Í¸V(££LZ«hF5¯é1Gõ{)oÌVÿFÖÅdÕÒ}5;½åVâ6ªJÜ"}Àeæk\koÌØäz2Iµm`î>wÔf"Á`#Wiüä" |
| --- | Minor | !ãç©úlBZfôsG äé³rpÄEÍ	A`åønÞÎ`¿¡à¾u¡U |
| --- | Minor | .3ÄXJ|ó	)K:	4Ôõã¢ËoO*já5ùz­ÿ;+w7×Ó¯êÒ(þÆ3(¬é ÷#ôè8õÙr¹{Ùs² ù½þêÖË6JÓmLÎÝ£HMðÐ8mD§HsæÄ {=Ag:¨ |
| --- | Minor | .Ëåz-JuZ¬:Ðdoè¾¹bÞY\*ºsÇ®Ô^Kh49vá¥¨tjYîhô*pré£ýé%Ýokíã<Ä;5{Yy §.s²uüìeéÆÆ |
| --- | Minor | Ìì*é«ÂÆÚÿúEîëB >EÖ§K]È\³­ÄKöýûÇu¯ýDÎµÊuäS¡û:»4f®{B%Êh;8úZU]ÀeÃñaJÔ¡Ãß-µ>ÒM¨RÂaOW#ð­vûd^D^c¿K2¢2"þº&êSÆ5àOaÁ¬ vFÌ/"n'ÙÛ*¶]æä6,±éHöÊtneíkwkjÆ§ÐåÖ]¶²¢8Gb&úëù>k6áîóÀÆ< ½­BË.eïÑ8L	*8èèUïë¥O®ÙÉÑvgØÀÁíqþ¢ß2° IOég|u£¯«ÅÍ>ÿ)Ô+·z/(Æ½XJ­nz â²Í]´", $þ¬4¾¸Ù Û57è÷0ZO«ç±ï@jÔ\>RÈ&¿Ë0_÷Q9 'Êî¨3©.ÌÃ`Ót4b:ËìOÂllÓkOæN	þþ¤0KÆ§ØÞ2Êd!aí#ÖÜ±®,n@-./LlÁ.ýF±EYÅ¨Õû4äÑnv[Ã]éç	ÍÒÑÚàÛ43*aÛ³qùÜúQüÈdRhD!¾M&Ò,³Â¯gdJ"fáIYár)&¹h­B-?& !­fL<âAÜAÍå¸ªªEìéÓ¨GÊ\L%ÑÚØ¶3 JCÉ4ßH¥"I(yâéëI¶S­ðÜQòìI\Ó1Ú§ªeÃnØ +¾áªl®¹~ ýüqn®¿.æ ôÃ!7æê5îkï÷¾_"¢îï0+Ixð1Yª7EädÃ9·^»£Q){ÊQÌáðÁîzæ/6¨AêÜÌíê{2¹Ð¾A.CJÀeSçi4þEjYÒ·ÖX;¾Q àÉU¨Ýµ èê7â+tºÆ° Ä<jZ6G®pìÛ|Wæl9øæäF{^'×²£ªh+ëtvzCåúô%*§Ö/Ôíhà#Dðë@ã¶«"¢éÎ |
| --- | Minor | ¯õ'õ¨=Fòx¤h[çyæHeó¸öl`×cW[¥_õfþº8ß)ôF3¥æþYÎOS4l¶ Í_«ßà{ÎR_ò1sú´n|ÝÑCîwµ)É\Yº¡ÁÃò_¾ÅÑÀÖÇ\xQRì óÍ¹£'TäL4Aªô[ÙeÉî[²v<ù]¿hÇä:¿.=j{×z<+ärI¬CÜPëîJÆöñ(Á&y/¹Í£1O|!£íA¢ü:Ê³V*¢7q3?Wwi¦å^|A\BsÏî5é#L.ãt21Ò·çt2æyoRtô±¯c w\*ÍNïªó*jóÆÅÄ!öp±HÁzéóÁø¤7(£ñ°hqxäÜ Ùm3]ýÚ7Nú­%oi§Ü¾P/¶o»t¡pÍ§/ý@>ì:ÛR(¿'qýÊÝÕx |
| --- | Minor | ¡[újGÌ1ÁÛ¿^óØ-Wà±<©uwhç¬hï-ïÖ^s!§õ6û­9Ê¤Jr.½­9J÷U*e3uS ÓôkòX;¤)4\Ì=®]iv÷ÞÂÆgomÄ·Õu_®ÞîD(®ïÏ cõãõÙÝ:¾ çBià§¯Ó×Ùv~ùü-ûùB)<aËïÝXÒÁ¸S8Ý1oEhV-½ß,ÁZß«Ûæx/oôÂÅ>&ß8V2iY/ûão2o·×úÕ$±Ûo!C=B"ð4BèIRRIÅ4 ¯ÒMJÉ_. |
| --- | Minor | ñ.É<þ¸«^3ÓÉFY¤Ò]e¹¬`?ÇT#	Aä.R"Y<íN×{?£). 6TDs@ìXÔ²Ç*ÉÔö.Í8ÁËM Ý`û¢C3-u÷Ìª´àà6ày« ÿ^õ¯êúK¥Íé^2ñóMA^ûY ÆVî |
| --- | Minor | Dc	AN¯ia6¢_çVBv<xÂ.VVù`´-¶Êäâ·R¯í}È	ÁbàPxÌë4¿¬Þ PeMhðªlüNöHÏØëXHÂµ¥+DÜ¸êeË}8T7W½+·¬0q+ÝW |
| --- | Minor | ?¹b m+súÑÝ;½.°-Ü |
| --- | Minor | ë*ù)kÞ¼Zÿþ^¬hrKá ÖÔy£^>¹³qYÉ 5÷¨3­Dô¯¤¤ù8ØúHx |
| --- | Minor | ^*dóÇAêÔ Oüà´;Í¸V(££LZ«hF5¯é1Gõ{)oÌVÿFÖÅdÕÒ}5;½åVâ6ªJÜ"}Àeæk\koÌØäz2Iµm`î>wÔf"Á`#Wiüä" |
| --- | Minor | !ãç©úlBZfôsG äé³rpÄEÍ	A`åønÞÎ`¿¡à¾u¡U |
| --- | Minor | .3ÄXJ|ó	)K:	4Ôõã¢ËoO*já5ùz­ÿ;+w7×Ó¯êÒ(þÆ3(¬é ÷#ôè8õÙr¹{Ùs² ù½þêÖË6JÓmLÎÝ£HMðÐ8mD§HsæÄ {=Ag:¨ |
| --- | Minor | .Ëåz-JuZ¬:Ðdoè¾¹bÞY\*ºsÇ®Ô^Kh49vá¥¨tjYîhô*pré£ýé%Ýokíã<Ä;5{Yy §.s²uüìeéÆÆ |
| --- | Minor | Ìì*é«ÂÆÚÿúEîëB >EÖ§K]È\³­ÄKöýûÇu¯ýDÎµÊuäS¡û:»4f®{B%Êh;8úZU]ÀeÃñaJÔ¡Ãß-µ>ÒM¨RÂaOW#ð­vûd^D^c¿K2¢2"þº&êSÆ5àOaÁ¬ vFÌ/"n'ÙÛ*¶]æä6. ±éHöÊtneíkwkjÆ§ÐåÖ]¶²¢8Gb&úëù>k6áîóÀÆ< ½­BË.eïÑ8L	*8èèUïë¥O®ÙÉÑvgØÀÁíqþ¢ß2° IOég|u£¯«ÅÍ>ÿ)Ô+·z/(Æ½XJ­nz â²Í]´". $þ¬4¾¸Ù Û57è÷0ZO«ç±ï@jÔ\>RÈ&¿Ë0_÷Q9 'Êî¨3©.ÌÃ`Ót4b:ËìOÂllÓkOæN	þþ¤0KÆ§ØÞ2Êd!aí#ÖÜ±®. n@-./LlÁ.ýF±EYÅ¨Õû4äÑnv[Ã]éç	ÍÒÑÚàÛ43*aÛ³qùÜúQüÈdRhD!¾M&Ò. ³Â¯gdJ"fáIYár)&¹h­B-?& !­fL<âAÜAÍå¸ªªEìéÓ¨GÊ\L%ÑÚØ¶3 JCÉ4ßH¥"I(yâéëI¶S­ðÜQòìI\Ó1Ú§ªeÃnØ +¾áªl®¹~ ýüqn®¿.æ ôÃ!7æê5îkï÷¾_"¢îï0+Ixð1Yª7EädÃ9·^»£Q){ÊQÌáðÁîzæ/6¨AêÜÌíê{2¹Ð¾A.CJÀeSçi4þEjYÒ·ÖX;¾Q àÉU¨Ýµ èê7â+tºÆ° Ä<jZ6G®pìÛ|Wæl9øæäF{^'×²£ªh+ëtvzCåúô%*§Ö/Ôíhà#Dðë@ã¶«"¢éÎ |
| --- | Minor | ¯õ'õ¨=Fòx¤h[çyæHeó¸öl`×cW[¥_õfþº8ß)ôF3¥æþYÎOS4l¶ Í_«ßà{ÎR_ò1sú´n|ÝÑCîwµ)É\Yº¡ÁÃò_¾ÅÑÀÖÇ\xQRì óÍ¹£'TäL4Aªô[ÙeÉî[²v<ù]¿hÇä:¿.=j{×z<+ärI¬CÜPëîJÆöñ(Á&y/¹Í£1O|!£íA¢ü:Ê³V*¢7q3?Wwi¦å^|A\BsÏî5é#L.ãt21Ò·çt2æyoRtô±¯c w\*ÍNïªó*jóÆÅÄ!öp±HÁzéóÁø¤7(£ñ°hqxäÜ Ùm3]ýÚ7Nú­%oi§Ü¾P/¶o»t¡pÍ§/ý@>ì:ÛR(¿'qýÊÝÕx |
| --- | Minor | ¡[újGÌ1ÁÛ¿^óØ-Wà±<©uwhç¬hï-ïÖ^s!§õ6û­9Ê¤Jr.½­9J÷U*e3uS ÓôkòX;¤)4\Ì=®]iv÷ÞÂÆgomÄ·Õu_®ÞîD(®ïÏ cõãõÙÝ:¾ çBià§¯Ó×Ùv~ùü-ûùB)<aËïÝXÒÁ¸S8Ý1oEhV-½ß. ÁZß«Ûæx/oôÂÅ>&ß8V2iY/ûão2o·×úÕ$±Ûo!C=B"ð4BèIRRIÅ4 ¯ÒMJÉ_.. |
| --- | Minor | Sentence exceeds complexity threshold, split for readability. Applying the split needs --strength moderate or higher. |
| --- | Minor | none (split proposal only; source not rewritten) |
| --- | Minor | none |
| --- | Minor | Check: NEEDS-LLM |
| --- | Minor | Flags:    not-assessed |
| --- | Minor | SENTENCE (Line 51, 1320 words, 16 clauses)  [Script] |
| --- | Minor | éöëíÒâþÝÿDÏÚD endstream endobj 111 0 obj <</Filter/FlateDecode/Length 4314>> stream xÚÝ\K#·¾çW¹x:d±ø²eÈ!=°`´1ðqóïSE²Ø Ly-åù2Ì|kòb|!õp´eátÙ²¨Ýni{\· ©§Õea£[9Ê·ñ$Â I½K÷I#ÀÐ7þ pfñ'bi»Øè |
| --- | Minor | }¦EAÀíDKLÓ|çî¾Ø«¿¾º» ñà¶ËëËõÆÓéÓÎÁ\6fælaD´®G]ILb¤ îr·ÊÃeW6Âg£¢ËRY¨ItX¹¶MºNY¤	èªýÈbctµRÅ ¢â@t]½h| ­¡=üôªÃ~\X j§Ë¨¯^Ñü~5Yý+£¿|uÔÎ=|Á¿|þU?}}ój_ |
| --- | Minor | Ãr¶ìËT!Ý4`KK´£@ëÝx;=ÞÎ ¾îR93%[ ©þeu«,qèG÷ù¬_ ­ÈÃw#+aÆ 3ßNdHsô´¥_M(á Vn ÷lïÁo'·ãC>¯ç´t®E}8±2juµlò(±CÉ¤'mÄ&Odõ5:9õéj²§Üf¡ÅD'Þì*úë¤±Ò¨ [Ò<ÀLÔb-V#óÝH*ÑWS´¿.ÐSÑlÖcBh£H5ø§&\­+ÿÈ)ï«yùÏLú{Cúð%ã0X³|²LÖ ×ÈC¿y½V§º r!Áçy_OÄ'#$Ó]ÇþcaGü	jæû7²aÎùßëy¿l:è·|mXÖ­¾Æræ .5Nøÿ¢B5çOC<¢?¢UV·Ú#ß/î Ä%Yë]øq¦0Q÷ÖWî}*Ñ &Oõ}~ÊØ\<f¤HJÚç._5Ný!± 5æ9  åoäjb©­¦,Óâ0ÈAVÕ³/TÞèbªµM£IêPkCÉW`ÑRñÎø |
| --- | Minor | FV¬£ÄhUrT¬eÅe8òXÍìþ¥¢cÚ*µé <ÿá<_P¤G#Z¦&g¶ÉùÝwá/dÉÕDðwüÅ5ã5ÁÜlÉÈ9u/nÓm¡Åj­¬öªø+¸Èh	É$í)¸Hù6åé[øâ(,FåN; ÛÔS&øi6&óØ,ðõI¢Ð6O+Î·îÍ(½S4uÆ*§yÅ\	YÉ2e÷1Ë+6¬({dò²J¸öTÙPÜ-oEk`P!¢ |
| --- | Minor | tÁèn/!ë÷%1c< K %ãÑ¼ùñí?e4NÆ9û"C STôh÷¢åØ&Ù8ßètùdÃho8üû@áÏÂîÈð)¢Õ¿£Ç¸PíuûøÇÃ_ßdÒ |
| --- | Minor | «C.\MÏüB©IdE=it¶¼Ï¢òüÁW³8÷ç¯õ"pâCÒ'»a. ÙÚ>Frk ÚÜÉ¥v»¸D¢ïDAÒ æÌòõÖ_þõ¸*p{¸DÍsLvR^úotpÅ->|1YªÏL¾*¤ÚÜ@>ÙÁbXz°Árèéæ$¯·ã¿q±ÖÅ&´\aH½ä¤BKÁ&K(É³ÍiÑ'B<­iª`ZÓÃ­ÆrfG`V®£H|£øÓ,¢" |
| --- | Minor | >jô1­÷í,Õpo8v(Æ<bV¬wâ	]Å3üÝÙEv¸cÙíHoÑv]ý´Û`Mö-ó¼u'ìsý'` »k­ÿ½`¹ï§ÐB2ÆTË6nMõÄb\)rª>på ¾m¯#¦@&RÔ½© ~:ÖâÚÝ2ªÂVORHÈ¢=Ôh<Ç±"ºtÌMòY«JàÛdÿV·«m/½Â/})KÊ°éa¨ 4T`:Y A |
| --- | Minor | O3ðÄañØæÏSCSÿZ°4W{Ìù)®4®ÅK\i,É¯Øfwµ[`vô£qÒB¢Ur²EäBÝÃiæ°p¡£ix!ÀµÜ.S d´*­Ld£ù>õ |
| --- | Minor | ©%Ì¬o`+qtÌÕÉüµO]{LzÒÉI!,P¢¢º`¶©aÂ°Ó*"ü­¹2Ù@.ëÉä±²ë¬xÓï¨K{´ ­ nSáÉË>]SºsÏèô  .`Ö5V§6Ý8½|¶çÞæ· |
| --- | Minor | XíåSï>¤¹­uµµ!¼U]µju§F¤aÐ¥ÔØÐâ~ÂÎ=1Í´¯xs'ë¾®áH¶E²~§¹zT=½ÞÄËêæ²|uDßXÕVY¯8ßjN¡D#LËÚÂYÀÅI+ÝcÕ ´]¦@Û`+ÉLnRYE ØW¢EÓÎ"óu¼ìå õD/á^ÐÐh".Q+év5Q]8gTôrNNý¡»2GÍ=ÑWÅ±gÑ=£í CÁ¥WÅ¿ |
| --- | Minor | ÷ºM¨sw?ÊÇ¼äyÓ^ ;"«ÖB?Û¿¬ç¨Ù|x|Ö¸Ð;¤yþy8Bð!~T8wsx½@+1Ëó¤V`xÃwRbðÌCá&FÍà°rÅÉ*ÕÇ |
| --- | Minor | ¡f |ÈÉìå#ZÛ	jffåU0ÆéIý~Û1@8Är4Diþî÷ÐÀ°éÆ61])±PN¨ö»zèx&Ò?î3 ¥ò7+,6ÔÎÓ5sË6äa0ÝÉ)"3Ä|6Ë6.Õ¡>È>5h öRb¸îøÞ÷II³J'$ïÕãºÇcàívìç¹Ü0#0läh§m0·oÚ&²qñ%êpß&uX0¦÷#ÝË.ÀMÂêñöÅ½2©*c`©ßKÝ¶=è¼ßé#MnÐ¢äÕ+±2tEFÖ|Üçú¹ÍÙ÷Õ K`©ëù8KÈ>E¯%xµ÷»ü¤Â_S7­%ÓáÿyÚÉI!ö]ãÓnpÜÂ6Ü¢§±ñÙÃX©y¨Ö£Ë·{ú°Ï´[Û«"ÆO`ÃLeÌ¼Vº«LcÁ#R4h}ïÓjNpSHö¤àv8;7nz$MA	âyÚJÃba>EiÎÎIåBíÖºE*½ n|©àf`òw¨w',lZÁYè6rËW$»y# OííAØjÛOÓ©³BSvx¯Çfòa ~ÿÝØõ³Z¯É§jÞìjòF¹ôI¾¼<d0n#é=DþûË!?Å\Wk ô<èôê»73v¢q·¥µvÌâ¹ÛK®ü5º÷óMvìþ°F!®¶uÐÙi×FóY'î¡1û®.LÝ¨qvuRyíMO·ÙØÚËtks·m[d£­ã¤Äz³ÅRzKB¬ïl±¦PÆ¦Ò!Ý¡86ÜÝ8oãj>Ûþow)a:R2É¯úüm6iöð½Þõ!m%±¤ ¥;\_é·q;ÇÑS¸¨û¦Û1àè:(ÃÎÉÑÿäèþ¯ûK¹úw8Ò4]âÔ·û¢L	å8z¥á´Dã7ï6 ,zofr4Ô´Ua/ß6ÿºHmf|5í÷nTîJW¶ã	d¦ª'ÿeÖ§siÚÎ:ãîêoÉ­¶hL°JÍ@Ýls%²åûÚz£ÎûÆ§èòq?5ñd9Äö |
| --- | Minor | =deZ¥´×¸wWaQ¬YË«è4sM@÷¦Ì;ìÖ¹óñ¤.Ò¾ä¸-ô\y	||uI_£É¦ééÏyT¬½;­4f/[±/#¿èû¶6n3W¨7ÉÕ)©ÊÑjß£`á ¸¾O\§Ù®Ðµ6½ÀSË®/½c»Lð¡/¤ÏK¥¢Ú,o6ó«=§¯ZB©V\ÇÎ`««É@×F£ÂnÕ¿§¡ùÜ¦]Þ¬Neï4'"/kõ% #^=VÊ¤ú´¦}ÿCú)UæUðtº§öF99¼ÞH!é::l¹V:wãÍwK¹MÙ3^oÖýöÅ|·òZ,ÿ*ø&·Æ4)Äjêd»ø%ªiî¿ß¾¡_úHëNSõR8Òrö4ÂýMíNÁi¯Í¡¼ôvÛHÂPÁÊ;ÜªÃæQ÷Öa¡¸¦VÎÑþñhïl/÷ßfXrî öÂ¤{C¹Ã2GgÔBwë¹þ%7'ÚµRø´µ.ÂÙ®ôVsÙþR 5¥+©o#øµÔålßüê¿Ç¡E endstream endobj 118 0 obj <</Length1 3716/Length 2489/Filter/FlateDecode>> stream xÍU{pTÕÿîý³»ÙdÝìMÂB²<ØM×&$HÍÍl+	ñÁð( FJÚ`Û¨£Fâ XA«ÍtªC­3NÕªUgêÎ`g¤än¿{mpÚþÛ3çï÷ß÷8ÏK ¹ø#ÈYVRºÜd#R&°6¹¬ry|ûëcóGÊªV?t_2ãg/¯Êñ5m7ðW×¶#¢1é6"Õà¬ÝÜáyØú ã·s°>ÒÐòE÷7op°u<ÞÓl+/Ç54wÖñæ{ÙF9ÖXÙ|½ÈrÐ×È Çë%Æ¿cÑØÒ±5­[YÎø2cOs[mPMoY[[#¢^ýq1Þl©U¸qá?ÒÖÞñ'\â|lñøÈÆºÈ¦NËßb/ï cmâh¤¨À¹:£Ù)(Y|óJJ­íÜØL© |
| --- | Minor | ëÂÚìh¥T^O.Ñè?\·±ÕX×QkÁÞÞÆ½f2S)±jFRÆ0¤Fâù(ïºxf¼3^ÆñÆE¤*ûØI¿<L³4£â}ªWyJ$d¬jØÞ;Ö°²¾4ÄQ+pÆ¢érÄÚ¢|:ýHÁh`fF´bbAsL17*¨/à×rôèkU×nãïûu"aòG!×6^idáþÌH#«b§v7@ïp}¥©î¢tåÏi©?/lFeÍÒà¾GÊtæªJ¹ËgÙÇ>g~=ãã´Þ¿!³ÁºTT²TiZ§ÌC#Í´zæÓê3d9D½Ì[Aïs-fïKéUú@¹N*¨öR»¹u»¼Ä¹4ÑzyÉ¬iÙÐ5ÉK#5ñ<_eï'GôÊtejP¯¬áªJ°v5®f-1ç72UÝÆñGçKCê:uºÈTú8cý÷Ñ|Î·3]ÂM5òÇWtÆîçi©u©%N±X»xÇUÚ¿rÄ2j¨+ÙÃ2Öí¥eÊûöK) *4ÓãìW½å¡þÀ­k<o­5óGÐã´zú©²ßÑéF+×äÚ~9¡^[¿ð¦ò?ÉYQ¹ÆÓÿÛÒQ¯¥5%¬«ZÃ¢XÍúÒ¬Ì;Ï'Ojô#>>Õ¼Þ)Dé~wzÁdk:³QüÖÉ üVvö»³IjYÒÙVõIÊå¤gÕ¢>Mzøâæ³Z¤pxø5¿CÃþ&õÂðÓM|¦WG?«xÝÓùÂXDúÌ©ùyä÷%Cz^~^æÔô)«%Iì÷Í.À%z´ÿË¶[|Êª/ë^»=/Wxÿ£²´	ù½[Nù}Ï)]FQeVN®~9>nkaà¿nXQ³°ãî.ãV^ÔWó"Ó¸ÞD+ûÎZ  fgNÍ,ð'K6Ôj¯\(mJM{¹¾?IYy»VâsgÅEê]ãìîgÏÓ?l^­¢¡ã3<¾v\õní¢°kîâ¹+óçø**Ñ¿ñÂn`pýøaÙójª/kÇnU]5åí%½GÉ<¬ |
| --- | Minor | }uzî)møvêT¿&2Ãz­òD8¬8ünSòâN;¬Ü0úÎ¨k?Õ~ñÎyßÒ$ù(üa{ü¿ï¿+.tL³}lîêï?-úD"ÇGßÿ£Å1Bü?[lÂ8Ýû>n=<«ÑÅ6Z-Þ¢raôë1Ülj Çé÷£ùØÔAÌwÍÉïñ×5ôæûd¥Ûs%bX>k¾¬ðù:;*«üÂýqTM¥¿Êb,)E±ÊÊP<´Ú(B´6p6ÔAÆ/átî}üÊå·ÊÃ·»¿ÅÌéà×Áì: RÍdm9µ2?¥"jæêáè{_í&ªã¾m6ó7ÄL;°ÔÄVÓ&fÔ27È^L¦eÃ¿½´ò7Âõìwó<lßÆqæØýTQ6ðúsìà¨Íâx®c­6õí,·Q}§ò¯³þmÖu¶ÆÍ§è·Ü¶ó.ý»2ògVyå³i±¢* |
| --- | Minor |  # ÑÚøøMÝ¸ðF¼Âx#¿qàõóòõÎgâ\5^ëÂ«±ÅW4yÆW4øð²t¼¨ãÏëx®¿L>wýeøµ_uá:Çé¾8yZC_~áÃ3!ü< |
| --- | Minor | '}xêDH>¥ãDOöÆË'½8¾Õ.{ñ³ sâl<¾+M>®ãè§<:G8|(^öâóÅãP@<Æix¬[ôÆ£7 õâà¹ò G¸å#^ØïÜ80 1bÿ>»ÜïÀþåbûÎÛºäÃxèÞXùÄ^öâÁAù =Õ²g=ÝbÏn¯ÜS=±óÚíÅ®.¹+ |
| --- | Minor | »¢çQ±ÓzGäâþdÜ×{cÑ Én÷4;å=ã±½+^n÷¡+woKw»±-?íE§[íØ²Ù#·\ÅæMäf6M@u¤¡]ÇFwEò. |
| --- | Minor | éöëíÒâþÝÿDÏÚD endstream endobj 111 0 obj <</Filter/FlateDecode/Length 4314>> stream xÚÝ\K#·¾çW¹x:d±ø²eÈ!=°`´1ðqóïSE²Ø Ly-åù2Ì|kòb|!õp´eátÙ²¨Ýni{\· ©§Õea£[9Ê·ñ$Â I½K÷I#ÀÐ7þ pfñ'bi»Øè |
| --- | Minor | }¦EAÀíDKLÓ|çî¾Ø«¿¾º» ñà¶ËëËõÆÓéÓÎÁ\6fælaD´®G]ILb¤ îr·ÊÃeW6Âg£¢ËRY¨ItX¹¶MºNY¤	èªýÈbctµRÅ ¢â@t]½h| ­¡=üôªÃ~\X j§Ë¨¯^Ñü~5Yý+£¿|uÔÎ=|Á¿|þU?}}ój_ |
| --- | Minor | Ãr¶ìËT!Ý4`KK´£@ëÝx;=ÞÎ ¾îR93%[ ©þeu«. qèG÷ù¬_ ­ÈÃw#+aÆ 3ßNdHsô´¥_M(á Vn ÷lïÁo'·ãC>¯ç´t®E}8±2juµlò(±CÉ¤'mÄ&Odõ5:9õéj²§Üf¡ÅD'Þì*úë¤±Ò¨ [Ò<ÀLÔb-V#óÝH*ÑWS´¿.ÐSÑlÖcBh£H5ø§&\­+ÿÈ)ï«yùÏLú{Cúð%ã0X³|²LÖ ×ÈC¿y½V§º r!Áçy_OÄ'#$Ó]ÇþcaGü	jæû7²aÎùßëy¿l:è·|mXÖ­¾Æræ .5Nøÿ¢B5çOC<¢?¢UV·Ú#ß/î Ä%Yë]øq¦0Q÷ÖWî}*Ñ &Oõ}~ÊØ\<f¤HJÚç._5Ný!± 5æ9  åoäjb©­¦. Óâ0ÈAVÕ³/TÞèbªµM£IêPkCÉW`ÑRñÎø |
| --- | Minor | FV¬£ÄhUrT¬eÅe8òXÍìþ¥¢cÚ*µé <ÿá<_P¤G#Z¦&g¶ÉùÝwá/dÉÕDðwüÅ5ã5ÁÜlÉÈ9u/nÓm¡Åj­¬öªø+¸Èh	É$í)¸Hù6åé[øâ(. FåN; ÛÔS&øi6&óØ. ðõI¢Ð6O+Î·îÍ(½S4uÆ*§yÅ\	YÉ2e÷1Ë+6¬({dò²J¸öTÙPÜ-oEk`P!¢ |
| --- | Minor | tÁèn/!ë÷%1c< K %ãÑ¼ùñí?e4NÆ9û"C STôh÷¢åØ&Ù8ßètùdÃho8üû@áÏÂîÈð)¢Õ¿£Ç¸PíuûøÇÃ_ßdÒ |
| --- | Minor | «C.\MÏüB©IdE=it¶¼Ï¢òüÁW³8÷ç¯õ"pâCÒ'»a. ÙÚ>Frk ÚÜÉ¥v»¸D¢ïDAÒ æÌòõÖ_þõ¸*p{¸DÍsLvR^úotpÅ->|1YªÏL¾*¤ÚÜ@>ÙÁbXz°Árèéæ$¯·ã¿q±ÖÅ&´\aH½ä¤BKÁ&K(É³ÍiÑ'B<­iª`ZÓÃ­ÆrfG`V®£H|£øÓ. ¢" |
| --- | Minor | >jô1­÷í. Õpo8v(Æ<bV¬wâ	]Å3üÝÙEv¸cÙíHoÑv]ý´Û`Mö-ó¼u'ìsý'` »k­ÿ½`¹ï§ÐB2ÆTË6nMõÄb\)rª>på ¾m¯#¦@&RÔ½© ~:ÖâÚÝ2ªÂVORHÈ¢=Ôh<Ç±"ºtÌMòY«JàÛdÿV·«m/½Â/})KÊ°éa¨ 4T`:Y A |
| --- | Minor | O3ðÄañØæÏSCSÿZ°4W{Ìù)®4®ÅK\i. É¯Øfwµ[`vô£qÒB¢Ur²EäBÝÃiæ°p¡£ix!ÀµÜ.S d´*­Ld£ù>õ |
| --- | Minor | ©%Ì¬o`+qtÌÕÉüµO]{LzÒÉI!. P¢¢º`¶©aÂ°Ó*"ü­¹2Ù@.ëÉä±²ë¬xÓï¨K{´ ­ nSáÉË>]SºsÏèô  .`Ö5V§6Ý8½|¶çÞæ· |
| --- | Minor | XíåSï>¤¹­uµµ!¼U]µju§F¤aÐ¥ÔØÐâ~ÂÎ=1Í´¯xs'ë¾®áH¶E²~§¹zT=½ÞÄËêæ²|uDßXÕVY¯8ßjN¡D#LËÚÂYÀÅI+ÝcÕ ´]¦@Û`+ÉLnRYE ØW¢EÓÎ"óu¼ìå õD/á^ÐÐh".Q+év5Q]8gTôrNNý¡»2GÍ=ÑWÅ±gÑ=£í CÁ¥WÅ¿ |
| --- | Minor | ÷ºM¨sw?ÊÇ¼äyÓ^ ;"«ÖB?Û¿¬ç¨Ù|x|Ö¸Ð;¤yþy8Bð!~T8wsx½@+1Ëó¤V`xÃwRbðÌCá&FÍà°rÅÉ*ÕÇ |
| --- | Minor | ¡f |ÈÉìå#ZÛ	jffåU0ÆéIý~Û1@8Är4Diþî÷ÐÀ°éÆ61])±PN¨ö»zèx&Ò?î3 ¥ò7+. 6ÔÎÓ5sË6äa0ÝÉ)"3Ä|6Ë6.Õ¡>È>5h öRb¸îøÞ÷II³J'$ïÕãºÇcàívìç¹Ü0#0läh§m0·oÚ&²qñ%êpß&uX0¦÷#ÝË.ÀMÂêñöÅ½2©*c`©ßKÝ¶=è¼ßé#MnÐ¢äÕ+±2tEFÖ|Üçú¹ÍÙ÷Õ K`©ëù8KÈ>E¯%xµ÷»ü¤Â_S7­%ÓáÿyÚÉI!ö]ãÓnpÜÂ6Ü¢§±ñÙÃX©y¨Ö£Ë·{ú°Ï´[Û«"ÆO`ÃLeÌ¼Vº«LcÁ#R4h}ïÓjNpSHö¤àv8;7nz$MA	âyÚJÃba>EiÎÎIåBíÖºE*½ n|©àf`òw¨w'. lZÁYè6rËW$»y# OííAØjÛOÓ©³BSvx¯Çfòa ~ÿÝØõ³Z¯É§jÞìjòF¹ôI¾¼<d0n#é=DþûË!?Å\Wk ô<èôê»73v¢q·¥µvÌâ¹ÛK®ü5º÷óMvìþ°F!®¶uÐÙi×FóY'î¡1û®.LÝ¨qvuRyíMO·ÙØÚËtks·m[d£­ã¤Äz³ÅRzKB¬ïl±¦PÆ¦Ò!Ý¡86ÜÝ8oãj>Ûþow)a:R2É¯úüm6iöð½Þõ!m%±¤ ¥;\_é·q;ÇÑS¸¨û¦Û1àè:(ÃÎÉÑÿäèþ¯ûK¹úw8Ò4]âÔ·û¢L	å8z¥á´Dã7ï6 . zofr4Ô´Ua/ß6ÿºHmf|5í÷nTîJW¶ã	d¦ª'ÿeÖ§siÚÎ:ãîêoÉ­¶hL°JÍ@Ýls%²åûÚz£ÎûÆ§èòq?5ñd9Äö |
| --- | Minor | =deZ¥´×¸wWaQ¬YË«è4sM@÷¦Ì;ìÖ¹óñ¤.Ò¾ä¸-ô\y	||uI_£É¦ééÏyT¬½;­4f/[±/#¿èû¶6n3W¨7ÉÕ)©ÊÑjß£`á ¸¾O\§Ù®Ðµ6½ÀSË®/½c»Lð¡/¤ÏK¥¢Ú. o6ó«=§¯ZB©V\ÇÎ`««É@×F£ÂnÕ¿§¡ùÜ¦]Þ¬Neï4'"/kõ% #^=VÊ¤ú´¦}ÿCú)UæUðtº§öF99¼ÞH!é::l¹V:wãÍwK¹MÙ3^oÖýöÅ|·òZ. ÿ*ø&·Æ4)Äjêd»ø%ªiî¿ß¾¡_úHëNSõR8Òrö4ÂýMíNÁi¯Í¡¼ôvÛHÂPÁÊ;ÜªÃæQ÷Öa¡¸¦VÎÑþñhïl/÷ßfXrî öÂ¤{C¹Ã2GgÔBwë¹þ%7'ÚµRø´µ.ÂÙ®ôVsÙþR 5¥+©o#øµÔålßüê¿Ç¡E endstream endobj 118 0 obj <</Length1 3716/Length 2489/Filter/FlateDecode>> stream xÍU{pTÕÿîý³»ÙdÝìMÂB²<ØM×&$HÍÍl+	ñÁð( FJÚ`Û¨£Fâ XA«ÍtªC­3NÕªUgêÎ`g¤än¿{mpÚþÛ3çï÷ß÷8ÏK ¹ø#ÈYVRºÜd#R&°6¹¬ry|ûëcóGÊªV?t_2ãg/¯Êñ5m7ðW×¶#¢1é6"Õà¬ÝÜáyØú ã·s°>ÒÐòE÷7op°u<ÞÓl+/Ç54wÖñæ{ÙF9ÖXÙ|½ÈrÐ×È Çë%Æ¿cÑØÒ±5­[YÎø2cOs[mPMoY[[#¢^ýq1Þl©U¸qá?ÒÖÞñ'\â|lñøÈÆºÈ¦NËßb/ï cmâh¤¨À¹:£Ù)(Y|óJJ­íÜØL© |
| --- | Minor | ëÂÚìh¥T^O.Ñè?\·±ÕX×QkÁÞÞÆ½f2S)±jFRÆ0¤Fâù(ïºxf¼3^ÆñÆE¤*ûØI¿<L³4£â}ªWyJ$d¬jØÞ;Ö°²¾4ÄQ+pÆ¢érÄÚ¢|:ýHÁh`fF´bbAsL17*¨/à×rôèkU×nãïûu"aòG!×6^idáþÌH#«b§v7@ïp}¥©î¢tåÏi©?/lFeÍÒà¾GÊtæªJ¹ËgÙÇ>g~=ãã´Þ¿!³ÁºTT²TiZ§ÌC#Í´zæÓê3d9D½Ì[Aïs-fïKéUú@¹N*¨öR»¹u»¼Ä¹4ÑzyÉ¬iÙÐ5ÉK#5ñ<_eï'GôÊtejP¯¬áªJ°v5®f-1ç72UÝÆñGçKCê:uºÈTú8cý÷Ñ|Î·3]ÂM5òÇWtÆîçi©u©%N±X»xÇUÚ¿rÄ2j¨+ÙÃ2Öí¥eÊûöK) *4ÓãìW½å¡þÀ­k<o­5óGÐã´zú©²ßÑéF+×äÚ~9¡^[¿ð¦ò?ÉYQ¹ÆÓÿÛÒQ¯¥5%¬«ZÃ¢XÍúÒ¬Ì;Ï'Ojô#>>Õ¼Þ)Dé~wzÁdk:³QüÖÉ üVvö»³IjYÒÙVõIÊå¤gÕ¢>Mzøâæ³Z¤pxø5¿CÃþ&õÂðÓM|¦WG?«xÝÓùÂXDúÌ©ùyä÷%Cz^~^æÔô)«%Iì÷Í.À%z´ÿË¶[|Êª/ë^»=/Wxÿ£²´	ù½[Nù}Ï)]FQeVN®~9>nkaà¿nXQ³°ãî.ãV^ÔWó"Ó¸ÞD+ûÎZ  fgNÍ. ð'K6Ôj¯\(mJM{¹¾?IYy»VâsgÅEê]ãìîgÏÓ?l^­¢¡ã3<¾v\õní¢°kîâ¹+óçø**Ñ¿ñÂn`pýøaÙójª/kÇnU]5åí%½GÉ<¬ |
| --- | Minor | }uzî)møvêT¿&2Ãz­òD8¬8ünSòâN;¬Ü0úÎ¨k?Õ~ñÎyßÒ$ù(üa{ü¿ï¿+.tL³}lîêï?-úD"ÇGßÿ£Å1Bü?[lÂ8Ýû>n=<«ÑÅ6Z-Þ¢raôë1Ülj Çé÷£ùØÔAÌwÍÉïñ×5ôæûd¥Ûs%bX>k¾¬ðù:;*«üÂýqTM¥¿Êb. )E±ÊÊP<´Ú(B´6p6ÔAÆ/átî}üÊå·ÊÃ·»¿ÅÌéà×Áì: RÍdm9µ2?¥"jæêáè{_í&ªã¾m6ó7ÄL;°ÔÄVÓ&fÔ27È^L¦eÃ¿½´ò7Âõìwó<lßÆqæØýTQ6ðúsìà¨Íâx®c­6õí. ·Q}§ò¯³þmÖu¶ÆÍ§è·Ü¶ó.ý»2ògVyå³i±¢* |
| --- | Minor |  # ÑÚøøMÝ¸ðF¼Âx#¿qàõóòõÎgâ\5^ëÂ«±ÅW4yÆW4øð²t¼¨ãÏëx®¿L>wýeøµ_uá:Çé¾8yZC_~áÃ3!ü< |
| --- | Minor | '}xêDH>¥ãDOöÆË'½8¾Õ.{ñ³ sâl<¾+M>®ãè§<:G8|(^öâóÅãP@<Æix¬[ôÆ£7 õâà¹ò G¸å#^ØïÜ80 1bÿ>»ÜïÀþåbûÎÛºäÃxèÞXùÄ^öâÁAù =Õ²g=ÝbÏn¯ÜS=±óÚíÅ®.¹+ |
| --- | Minor | »¢çQ±ÓzGäâþdÜ×{cÑ Én÷4;å=ã±½+^n÷¡+woKw»±-?íE§[íØ²Ù#·\ÅæMäf6M@u¤¡]ÇFwEò.. |
| --- | Minor | Sentence exceeds complexity threshold, split for readability. Applying the split needs --strength moderate or higher. |
| --- | Minor | none (split proposal only; source not rewritten) |
| --- | Minor | none |
| --- | Minor | Check: NEEDS-LLM |
| --- | Minor | Flags:    not-assessed |
| --- | Minor | SENTENCE (Line 51, 315 words, 6 clauses)  [Script] |
| --- | Minor | "ÑÖÖ²5hÇÉf'»E8áhâMW±¡qPnÐÑØP-ÑØ-ê½²¡ |
| --- | Minor | QïEê®"BmÖëê¨¹3[Öè¸3wè¨Ö±®·wá6kK°FÇOt¬Ä*U!¬Ðp«Ëde'`YQ 7ÇbiåSl²¼K|(S¹±8¥ª]GÉ"·,	cQ±S.r£¸(V;QE±Ä `¬cXØ"K.¸óçir~æÍµËyæÄ\; oJÕ¸iKÞ9.80[G~&óuäùÝ2Oßg~7|³b¤ÏßÈþÌAnNÌ-ANvÌIAÎ9fÙIÈîY1!Õ349³3x34Ì9õC>-WN/Â4NlZ.2¹ËÔ1µ^GôV##=QfT!ÍÒSlìI«áäxÎIlºEi11pCRÇçÊÔ*g¯ãs¢c§#Ù$MIahn·Ô4háv#ypñòºt8¹s#óOèE<Åëp°G §#Al`NvæØ»Íê6 |
| --- | Minor | ,Ò'-]l'}ìLdªv(U ÊÚ±Wñ[èÀ-ü·þ')	~ endstream endobj 120 0 obj <</Length 35/Filter/FlateDecode>> stream xc`Dõ¬4qÅ(£`Q@`Cá± D¾  endstream endobj 121 0 obj <</Length 252/Filter/FlateDecode>> stream x]»nÄ E{¾bÊM±b_JeYvy(N*+ÁBa\øï3ÀÆWsf.0Ã¯Ý­s6^õÀX§#Î~ Aâh;@[îQ9Õ$ãdî×9áÔ9ãYÓ §äâ »'í%>0 à¯Qc´nÝçµ¯¨_BøÆ	]k[Ðhèºg^ÄÀyßiÊÛ´îÉöWñ±SõKÊkP5Z-4VËÐéùKuI³_$Wª~eüx.8ËP5ã³,¸ÈPµbQ±¸cAÿ}&ÿ#mkR-1Re²¥±Üu¸ |
| --- | Minor | ?ø]yÿ `î endstream endobj 125 0 obj <</Length1 15136/Length 10170/Filter/FlateDecode>> stream xÍ{	|TEºoÕ©³ôÞ§÷tgëN'é,Òt!à°M0"àDÈ!$,é:ìÈ"¢Èà\È ²AÇaf"£Î8|1ã}Ãp&9¹_î@F¼sgîï½ß{}R]UçÔ©óÕ÷ý¿­úa¾Xä?v\>JÂ~83¾àÞéÂ®ÑÐÉ?ýþÑêÿc3~®=eÔ	ÞGçÂxn5©¹wzf°"¸#!¾®Ï\°dÞ²ñ3½0®·/XYãnÊzá:Bê(èïZ´lñ¯Öþ{BaüÅóª!¤}ÝâÚEõ¹úpò¢óu¿¿°¡tüà8avk¯B¿ú%KjVk£N!TAÿ³Êón<Ñ¹ú_Cùy«±»¹,²~}÷ÒyKF¿ÍC |
| --- | Minor | ©BhïwË/\¶¢¿Pö9XãCòJÂp. |
| --- | Minor | "ÑÖÖ²5hÇÉf'»E8áhâMW±¡qPnÐÑØP-ÑØ-ê½²¡ |
| --- | Minor | QïEê®"BmÖëê¨¹3[Öè¸3wè¨Ö±®·wá6kK°FÇOt¬Ä*U!¬Ðp«Ëde'`YQ 7ÇbiåSl²¼K|(S¹±8¥ª]GÉ"·. cQ±S.r£¸(V;QE±Ä `¬cXØ"K.¸óçir~æÍµËyæÄ\; oJÕ¸iKÞ9.80[G~&óuäùÝ2Oßg~7|³b¤ÏßÈþÌAnNÌ-ANvÌIAÎ9fÙIÈîY1!Õ349³3x34Ì9õC>-WN/Â4NlZ.2¹ËÔ1µ^GôV##=QfT!ÍÒSlìI«áäxÎIlºEi11pCRÇçÊÔ*g¯ãs¢c§#Ù$MIahn·Ô4háv#ypñòºt8¹s#óOèE<Åëp°G §#Al`NvæØ»Íê6 |
| --- | Minor | . Ò'-]l'}ìLdªv(U ÊÚ±Wñ[èÀ-ü·þ')	~ endstream endobj 120 0 obj <</Length 35/Filter/FlateDecode>> stream xc`Dõ¬4qÅ(£`Q@`Cá± D¾  endstream endobj 121 0 obj <</Length 252/Filter/FlateDecode>> stream x]»nÄ E{¾bÊM±b_JeYvy(N*+ÁBa\øï3ÀÆWsf.0Ã¯Ý­s6^õÀX§#Î~ Aâh;@[îQ9Õ$ãdî×9áÔ9ãYÓ §äâ »'í%>0 à¯Qc´nÝçµ¯¨_BøÆ	]k[Ðhèºg^ÄÀyßiÊÛ´îÉöWñ±SõKÊkP5Z-4VËÐéùKuI³_$Wª~eüx.8ËP5ã³. ¸ÈPµbQ±¸cAÿ}&ÿ#mkR-1Re²¥±Üu¸ |
| --- | Minor | ?ø]yÿ `î endstream endobj 125 0 obj <</Length1 15136/Length 10170/Filter/FlateDecode>> stream xÍ{	|TEºoÕ©³ôÞ§÷tgëN'é. Òt!à°M0"àDÈ!$. é:ìÈ"¢Èà\È ²AÇaf"£Î8|1ã}Ãp&9¹_î@F¼sgîï½ß{}R]UçÔ©óÕ÷ý¿­úa¾Xä?v\>JÂ~83¾àÞéÂ®ÑÐÉ?ýþÑêÿc3~®=eÔ	ÞGçÂxn5©¹wzf°"¸#!¾®Ï\°dÞ²ñ3½0®·/XYãnÊzá:Bê(èïZ´lñ¯Öþ{BaüÅóª!¤}ÝâÚEõ¹úpò¢óu¿¿°¡tüà8avk¯B¿ú%KjVk£N!TAÿ³Êón<Ñ¹ú_Cùy«±»¹. ²~}÷ÒyKF¿ÍC |
| --- | Minor | ©BhïwË/\¶¢¿Pö9XãCòJÂp.. |
| --- | Minor | Sentence exceeds complexity threshold, split for readability. Applying the split needs --strength moderate or higher. |
| --- | Minor | none (split proposal only; source not rewritten) |
| --- | Minor | none |
| --- | Minor | Check: NEEDS-LLM |
| --- | Minor | Flags:    not-assessed |
| --- | Minor | SENTENCE (Line 51, 175 words, 2 clauses)  [Script] |
| --- | Minor | å@^Ó  Ø±ù÷Ì@®µË+kñòåÈU1¯f)ráÓÛ«Åå/EN¥×¥V!LG2Ó½Hè?½ÜÝï=å%¥õjï«?|ßÿ¹Oß3¾OÉ?¸c,çÿ'Ïø¿ûùçWßÿ/Þ¡ïÕÿkwÈßÉßýK7`@¦	ÙÅ /JB©( |
| --- | Minor | ¥>ÀW-Ð³ÁA`p£½ wIp¨à®T¤;Ów§ª³àààneÂ7s×³IÙ0§Ús¨á.-|S}Ñ#F$Fè³*:¾7EÁ"z´mE¢GnEÜ¹=J\2¯¦ÍÝCh FÍçFÇLßãGïÉ£æÐïiá{Æ(z~Ò¾­{áZi!¦¢tñ<dP¾í´ú4¶yx ÂzÑ¥&PD­äFÙ0Î­p9¦ßØ°.Ãx2A?^yrLd¡¯QÊÓ!áSGÁ¶úBÛý?}}\ißÿO Ã ó®üïÇ¡9á±´¾Ýî7ÇßÓ¯¿àN»ý·&hçÝ¾5x¥ØÇ8*øa4aÀE Y0V½Q¦@«®g@©wÓß¼=nàíq»Æ107ã¨4ô*G)À¬?ÏF\·(×ä2ZÄá&'Ï1LXI}(X4®zî3o­øIa	¾ÓGW¸Ä *UÚ¡>NBaátË+£!h8Æ qh"²,Ü¯@µ	fÀ'ø' ;Ænú*Ðr´í½ÚûIïÇ½¿ë½ÒûQïåÞ{ÛûëÞK½¿ê}·÷BïùÞ½Ç{_é=ö{W?zÿûâçnß`Uè	¢HÁJÂüNBã^]¸P¿B¥E­À H¡³jD ÅÔðH1F8? |
| --- | Minor | å@^Ó  Ø±ù÷Ì@®µË+kñòåÈU1¯f)ráÓÛ«Åå/EN¥×¥V!LG2Ó½Hè?½ÜÝï=å%¥õjï«?|ßÿ¹Oß3¾OÉ?¸c. çÿ'Ïø¿ûùçWßÿ/Þ¡ïÕÿkwÈßÉßýK7`@¦	ÙÅ /JB©( |
| --- | Minor | ¥>ÀW-Ð³ÁA`p£½ wIp¨à®T¤;Ów§ª³àààneÂ7s×³IÙ0§Ús¨á.-|S}Ñ#F$Fè³*:¾7EÁ"z´mE¢GnEÜ¹=J\2¯¦ÍÝCh FÍçFÇLßãGïÉ£æÐïiá{Æ(z~Ò¾­{áZi!¦¢tñ<dP¾í´ú4¶yx ÂzÑ¥&PD­äFÙ0Î­p9¦ßØ°.Ãx2A?^yrLd¡¯QÊÓ!áSGÁ¶úBÛý?}}\ißÿO Ã ó®üïÇ¡9á±´¾Ýî7ÇßÓ¯¿àN»ý·&hçÝ¾5x¥ØÇ8*øa4aÀE Y0V½Q¦@«®g@©wÓß¼=nàíq»Æ107ã¨4ô*G)À¬?ÏF\·(×ä2ZÄá&'Ï1LXI}(X4®zî3o­øIa	¾ÓGW¸Ä *UÚ¡>NBaátË+£!h8Æ qh"². Ü¯@µ	fÀ'ø' ;Ænú*Ðr´í½ÚûIïÇ½¿ë½ÒûQïåÞ{ÛûëÞK½¿ê}·÷BïùÞ½Ç{_é=ö{W?zÿûâçnß`Uè	¢HÁJÂüNBã^]¸P¿B¥E­À H¡³jD ÅÔðH1F8?. |
| --- | Minor | Sentence exceeds complexity threshold, split for readability. Applying the split needs --strength moderate or higher. |
| --- | Minor | none (split proposal only; source not rewritten) |
| --- | Minor | none |
| --- | Minor | Check: NEEDS-LLM |
| --- | Minor | Flags:    not-assessed |
| --- | Minor | SENTENCE (Line 51, 532 words, 10 clauses)  [Script] |
| --- | Minor | eL¤`õáb21R(mÓ#ÅÂ:AÕæyP >Q¬Me5@( ¬R^O9\kP5 è$z÷¡u*CUhjö¨N9UÑÎ\áèØ÷ÑI ãhlÀ`hy²àÚ0~ô[ÀrÑë·È{Êñ$yYR ­åtcYò^¸(w½y¦mî=D> |
| --- | Minor | ]c4Ì>	FWðcè þ Õ£FT­(A,Ö)c>÷r|~¤<+ã>à­ð¤2Xçiý`ø<NÅÓHYgÁ |L³ëP[O9Æ*ë¯aêàùõ¢÷1©¬çÐg¼óFÃÞE@é(¥\C-âÀÉGI¼óB=WëH~EE¨Ì¦Â¹F4_§OðKün±IXÜ*Ý7ËýÙÿ÷ºnQp·¢V}­ûdooÁ,6ÝÊÅ´ sl<­LãoÞüóë×?)_¯à¸_Y2¿LnÊ |
| --- | Minor | ·ÃÌõÊÌÑN ReÐÄÄö¶`gßÄìÁfÈø²í´Úþä |
| --- | Minor | ^¿yS>?¿?ñ#eóÈ>y¿ü´ìY¯ |
| --- | Minor | cÁëz$#Èr5æT,Ò1^'¶çµuçµ |
| --- | Minor | íyP°Écó¼&O¶ÇD3{.µô\brlÏ¥´q3N¯á·ÐUàI¤ÉªU3#¢:;Í¹@h;%Ô1ÇY,LzhÖ[ªí;~>îÔº¤þ2f8ß{¿º¦!Çõ`Lî¶É­ûf× ¯Ù¼<1/oö@tÌSéÄëák&Z!|-3hpVÐn³òÞäó÷äæL{OÉ©SäLB%¶¡÷*Û à,h¡_h.ÕEÞfUóFmÌ{²µãz§ØH R~zy% ²ôÙ²oïÞ}´üYþ6ýù:åïòqgà¹U~Q~In]÷â¥¸ïKäíò¹Vyèu @VK1l1øRÌsSÏb/Uáj¤LhomÝT Áëm¦\Sn p(°ß "ûíì<¹U3cÖ°	&Õ"mï¹!¦!³%µ¹q¦:SÃÂ­2¦÷\x1T\vRÈ{1+¿+6c¶ýÝuÞ )¨Û¦}*P¦Hõ¨)v-äJõ«LV½Î4ØÁ«µ±âõ¶öÎvà)7$Ùu£KîèÜ¤Í×äkóuùÖ|8ôFà¬ k³ÒcO6ÐGàìAÉÞóËÊ¯\ÃùWQ:yS¹¢{8~k÷Ú§77íg«°&7ïóËpí¤|p	nÛý·Í{o£r	ô¶½ÄÍRS¬Ö¨q±F£5:TmD®ZSJË#µ*Æ,^ S¤(ÍÝyíyÁEÊgø|,Sqá	·Ú­wH¥[u3Üª§_ÆÍ iæ°¥Å.<OÄ,ÏØÍ`ff<3A#¢BlR÷­<KQ­,æ]!'zf}×SÃl{ÇÊW¿Ã·«ûK/ÃIKÈõnM¹ü1]ç&Àïn¿Ih CüB#Zh¯«õ..µ%»5qvÂm:^ÍEiÎwÝ |
| --- | Minor | ¤Ô:µÞÄÈIeÑYô¢A4¢ÉªKÕOêê1&ec³Ú	²YWQOÐî°y`PæÆ½{vï}mìÀD¾v­GþÆI÷¾ü`îÑ¥Îä_ºpáÒ/ÞøùÌw'É×¿¾ jSÂñËqq7É¿;JW×ÑÎL4BJH"mêqÆi¥qEÄ(óé¸ÄGÛxÞçÑ z°ºöúÔöÃ.jkûèÎ &ýÚB¶YYoBbö Á9 zA^o~üñfZR7¯©Û²¥nÍæÃgä7ÿCþËö<{óÊÏâ½-G¶<{ô(Y¹qïÞöî½èx¯ù·W¯þ¶ù=GôÇ/]:¾ñÔ¼û<«P¬d`#~9«âp*ñ:@D <`Ðb[2-ä-µ÷ÜPñ)h4lô¨Éã|Suhò¸D¢ROCYJW¯ ¥çLõ¥ |
| --- | Minor | ¢ùQ:m1Ççcâ¢d¦@örOW02+¬jÊëê»Úà=©Ikr7Àª¢¢¾äDà¢À36«Ùag9rÒÌd2çNÍv {EÄì~,çÃvùÝïî¶ÿðé±cÊäK¯ÌiùÎgÅsàôù¬(»BîzîUùúGÖ­_Ûg_øÏ[uÏTùuùKÜT]»achù¶Ó n]¼ø×iÛº»n®|{ÆºÆd_¡¼á?¿Z¼ªþ{ò×Õ5àñoÄù |
| --- | Minor | o<´þkäëòEJë:òLó§¯½×ï÷pØ^îCÔ 3ÅâÎlbD°ÇFåØyA%`Q% hu^T©)o¨D¢NEØJ~¾D£A¯U	pFzXÀÕÔ¨äut:íàþÂFûÖ¸oé¨R tÀÚ¤ÁÚHv#2b£ÁhdS¸>EbðÒÍ<µ5ÎÎÂpØÀÉ²á'D¹«gÂcõßÛÎ? |
| --- | Minor | eL¤`õáb21R(mÓ#ÅÂ:AÕæyP >Q¬Me5@( ¬R^O9\kP5 è$z÷¡u*CUhjö¨N9UÑÎ\áèØ÷ÑI ãhlÀ`hy²àÚ0~ô[ÀrÑë·È{Êñ$yYR ­åtcYò^¸(w½y¦mî=D> |
| --- | Minor | ]c4Ì>	FWðcè þ Õ£FT­(A. Ö)c>÷r|~¤<+ã>à­ð¤2Xçiý`ø<NÅÓHYgÁ |L³ëP[O9Æ*ë¯aêàùõ¢÷1©¬çÐg¼óFÃÞE@é(¥\C-âÀÉGI¼óB=WëH~EE¨Ì¦Â¹F4_§OðKün±IXÜ*Ý7ËýÙÿ÷ºnQp·¢V}­ûdooÁ. 6ÝÊÅ´ sl<­LãoÞüóë×?)_¯à¸_Y2¿LnÊ |
| --- | Minor | ·ÃÌõÊÌÑN ReÐÄÄö¶`gßÄìÁfÈø²í´Úþä |
| --- | Minor | ^¿yS>?¿?ñ#eóÈ>y¿ü´ìY¯ |
| --- | Minor | cÁëz$#Èr5æT. Ò1^'¶çµuçµ |
| --- | Minor | íyP°Écó¼&O¶ÇD3{.µô\brlÏ¥´q3N¯á·ÐUàI¤ÉªU3#¢:;Í¹@h;%Ô1ÇY. LzhÖ[ªí;~>îÔº¤þ2f8ß{¿º¦!Çõ`Lî¶É­ûf× ¯Ù¼<1/oö@tÌSéÄëák&Z!|-3hpVÐn³òÞäó÷äæL{OÉ©SäLB%¶¡÷*Û à. h¡_h.ÕEÞfUóFmÌ{²µãz§ØH R~zy% ²ôÙ²oïÞ}´üYþ6ýù:åïòqgà¹U~Q~In]÷â¥¸ïKäíò¹Vyèu @VK1l1øRÌsSÏb/Uáj¤LhomÝT Áëm¦\Sn p(°ß "ûíì<¹U3cÖ°	&Õ"mï¹!¦!³%µ¹q¦:SÃÂ­2¦÷\x1T\vRÈ{1+¿+6c¶ýÝuÞ )¨Û¦}*P¦Hõ¨)v-äJõ«LV½Î4ØÁ«µ±âõ¶öÎvà)7$Ùu£KîèÜ¤Í×äkóuùÖ|8ôFà¬ k³ÒcO6ÐGàìAÉÞóËÊ¯\ÃùWQ:yS¹¢{8~k÷Ú§77íg«°&7ïóËpí¤|p	nÛý·Í{o£r	ô¶½ÄÍRS¬Ö¨q±F£5:TmD®ZSJË#µ*Æ. ^ S¤(ÍÝyíyÁEÊgø|. Sqá	·Ú­wH¥[u3Üª§_ÆÍ iæ°¥Å.<OÄ. ÏØÍ`ff<3A#¢BlR÷­<KQ­. æ]!'zf}×SÃl{ÇÊW¿Ã·«ûK/ÃIKÈõnM¹ü1]ç&Àïn¿Ih CüB#Zh¯«õ..µ%»5qvÂm:^ÍEiÎwÝ |
| --- | Minor | ¤Ô:µÞÄÈIeÑYô¢A4¢ÉªKÕOêê1&ec³Ú	²YWQOÐî°y`PæÆ½{vï}mìÀD¾v­GþÆI÷¾ü`îÑ¥Îä_ºpáÒ/ÞøùÌw'É×¿¾ jSÂñËqq7É¿;JW×ÑÎL4BJH"mêqÆi¥qEÄ(óé¸ÄGÛxÞçÑ z°ºöúÔöÃ.jkûèÎ &ýÚB¶YYoBbö Á9 zA^o~üñfZR7¯©Û²¥nÍæÃgä7ÿCþËö<{óÊÏâ½-G¶<{ô(Y¹qïÞöî½èx¯ù·W¯þ¶ù=GôÇ/]:¾ñÔ¼û<«P¬d`#~9«âp*ñ:@D <`Ðb[2-ä-µ÷ÜPñ)h4lô¨Éã|Suhò¸D¢ROCYJW¯ ¥çLõ¥ |
| --- | Minor | ¢ùQ:m1Ççcâ¢d¦@örOW02+¬jÊëê»Úà=©Ikr7Àª¢¢¾äDà¢À36«Ùag9rÒÌd2çNÍv {EÄì~. çÃvùÝïî¶ÿðé±cÊäK¯ÌiùÎgÅsàôù¬(»BîzîUùúGÖ­_Ûg_øÏ[uÏTùuùKÜT]»achù¶Ó n]¼ø×iÛº»n®|{ÆºÆd_¡¼á?¿Z¼ªþ{ò×Õ5àñoÄù |
| --- | Minor | o<´þkäëòEJë:òLó§¯½×ï÷pØ^îCÔ 3ÅâÎlbD°ÇFåØyA%`Q% hu^T©)o¨D¢NEØJ~¾D£A¯U	pFzXÀÕÔ¨äut:íàþÂFûÖ¸oé¨R tÀÚ¤ÁÚHv#2b£ÁhdS¸>EbðÒÍ<µ5ÎÎÂpØÀÉ²á'D¹«gÂcõßÛÎ?. |
| --- | Minor | Sentence exceeds complexity threshold, split for readability. Applying the split needs --strength moderate or higher. |
| --- | Minor | none (split proposal only; source not rewritten) |
| --- | Minor | none |
| --- | Minor | Check: NEEDS-LLM |
| --- | Minor | Flags:    not-assessed |
| --- | Minor | SENTENCE (Line 51, 811 words, 10 clauses)  [Script] |
| --- | Minor | ªïÙZeÞþ[lW~ë²2<A>©ØõêÞ«ÜAÐ°X4Dv-EDl0[êJIQÉhLõ!A'Rêg5Þî ã+ã0áTäÉTäÔ°SØ¤à/ví¸5oÙ¼OaksUÒ.þéÆ?=ÿQ oùÍåâyËpìqJ^FÉÿvú8ÊWåòKÍÏ }UJnöèÿ4)Íf1>bZ«D+¨×Jn>®´¬Õ>7TFÞj´³(Ñ¬11ê´AªMíT¯2;©Ñën;ä±-p<à¼×	g½àûhñDÚ´®:s=V×3 |
| --- | Minor | ««Ìº2ËÇ#ëNÉâ©¦ßÈÇQ6æ$Ð¦E9UÃWªæ³¨QãDdH"ç¤#ØÝ»ìÎ`@Òôú"ý2ýZ}³ÇIÔèsm^|ëLÏkgÎ0ãÏÑçÃ^û÷H'û¤ÑÀÓD¨ÕiãâX·¨Ói§hunkÇ |
| --- | Minor |  Ø¥>{­ØµÔ\ê+JskuXÃhcHjcSI£¶±½ìaXåûì#ur 4JÃ·ÐT@1"PëN¤¤/K_ÎQ§g§g¡þÎªø»4%êHCi}QGM&UKGj|ª;Õ0D«ªªªÏ5äÆ |
| --- | Minor | êêÉMâ¨¨¤¨?Ñ=Ñ31a¶f¶v¶n¶~¶{¶gvBºBS¡­ÐëËã+ÜRo¦N[§«Ó×êâëÜuºZoNKzk:úc{¥8©LLy"5XaHRãkïIH>SÍ:{ìTÕ·>< |
| --- | Minor | ×Knn­2ýÙ3?Ysñµw_¿¿­ë ±Ûáç7TÔäuá§g~._x¦ñºòP^Îð7¯|¤8(ê½ÊCNh©¤ã¤^g7éY*Ì|{À`HÔÅD3NäLÈãxv´wtwòÀ(c¥ÜÀñøè¢hªU·yìu)ìu!W½Çnf x¢À1Ô¤:û:ÈãF&pöÔ_:ooÉoÃñ®¬¼¼»[þüóÏqa¡ýµüÓ<fbµ-Íi XÊöh Y8äÜ©j²x¶yã·Zt!ãä'#AïwOË¹ìi© ´:Á>oÙÕ!wÝøRÐfÊ'%ii«SÎ¥±¡søs´±m\ßfk³·9ÎEsséaíÙ·=ÅDUä¶óñ½àÍ¦±d~»iýÆêÆåÃ[Êþºë fv®[ú¨8·èg3?ý OýãÊPå£ÛðéßUOÊ?Ýòk×Ï¿ªÄOÃ`Õ'!²"/%y8 ¸]ª¨]"U(d(Rm5G»´ÙÆo3±>H Æ¬µúT}rÇ¼ ,9!¡mVÚFXVqGqéàçëÚnÞl«{~°¼îÜÚ¸}{ãÖeTÖ³¤x®üÎ­[òÅ¹ÅÊðs?ÿäÓÏÞ9K±F¥Rr¡lÉö9~î	Sz+)6dè\ÈêâÓ¢©¹þe»b®»)rGàXeÐ)+Q6M[ú«µÔl¬ï÷­_\_/üÅÂr[ãcOìÝ³{Õ6yøÎQ/¿Ûºö«/¿üzM}3W#Ü»WJ¶³"pÏ¹K¿K0,À=¡H¿1ûm"ña?ÊqiÒ(û®Cp×qû +YIÄWeE¢@R5O¿wñ*_îìy±µµõµWÆ¬Í9'O­Ú¾©¼ûå²22­|Ý±QNªiä\ö*p=ùÑ")ËEqTMÝeQ=#èXï.'ØöéØýê!Îï1úPv²KÈ±§e;í¼¶1 ÎÎ ß¬Ì¬@h8 a@ë 6)¿/;Kñ	Ãq8µìd³YÝ×JÏÍ*2¯¯?°çªp¼·Uät÷_ü59ù%E¯¶5ÝØ¡ryk^çÂc»@b±¨Rò»¬;ÖiH«6i¶È4Üãç~O?õ»xò38ºÀ 8dðÔ3dB If>¤ªbQ£âhÂDÈ "´ýÐ(Dhàq'ìÂ_î¹v¬1¹¤²¾	Nè§Ò(·Ë¢gùtDXqñR÷'y¢¬ZN |
| --- | Minor | ~· 8Âtwúl~ËÈÛèO|}D¬&³äN:@)A%»º/2287X|<Øäî>P!} K¦&SéÈº¤¹¤½ä¸u.¨.Ä?,ð»:4DP²IÙ?YúüÁC2ÓRTY÷H¬Ôg×"³V¬ºôIÏmV`QÆø7[dFéeËêúÐüEË¤ÞêbIïûÿçx7;þ¸Ûþ¸ÕR¸Þèöí§^ ú2XÝiH,¨IÇ7QWE\¶±jpwö©Õ	w;+i Ñ?ÄÑgðmVÄìÚ³g×®={wRê¼v |
| --- | Minor | ;å¯ò¿éè¸v­£ã`åe%Ëò{4 g²'áé:äE÷K~L±DÏîréCÆ¸[³ËºÕUä~Ô¸?1ÞØ.?VD>} ñv0¢Ä£¼íR7$µ&ÑpÒÖ/þðõ1­/>	³ìBNþ]|BUP	C~V~èNx"G+y õQïýQè	)A¥¶pC&ÄÙ·êÕ!Ó~­FÅd ÑoVùt~CÀ{{§Hw3»À7½ |
| --- | Minor | ®I|[ÙÓHÄ"#nFÙD»è£2]°ÄHDb%n¬M²K)ÊF<¤ÝØÍðwâTâ#Üé|_ÈûeÜÔÉ·ÐóEËàÃ¡lª|ãÞ©§[û`^YndÊä¬1]F)¹ØH*6B{'{µpM>û³¶àçN*aaTùlùLûáT¬»nVÝø~*Ö¹Ll/Þçöy|	>ïÍíÝýø9î99	³¼ëã×»×{Ö'¬÷îßíÞíÙ°Û{(þûçPÂ!o¬Þ~ÄzÄvÄ~Äq «2 |
| --- | Minor | &g³SShðÅÞdí§%gzàÀkx|hPþÑÌÕ¶íÍ?&§Ëñ$ùDyOá{î»}}ãO)Í9`'>,ÀVH	¯Ó[uê(PT´_]Ä"¿(öã¡¿èÓe* |
| --- | Minor | ;ÂÊAjïgÞ·Wj×ÝJS»] ]tXÉ~	âëÃzmò2àY/ËOf(?úü!<Wqï¬¯{LÙé²ÊÜò'.<~ú|æó ÄUXqô ¶ÙbµhÕ+T#´¸®1b	Ã4Óí®fU*Á2ÂjÑéu¢1ÐëuS,LT&=OEûµ*«Å,êuZZ%ÐåÁ&¶ÿ2¼íá>ä¸·q}g+¼ÑE{}{`··¾ìî½àM°]ã² ÍDË,Å¸TSj©/²lÖØy #ÙÜH~¤0T5L«¦¢bjÉµæ£qxjþ1Q7A?A```É·Þ pS@ Ø®/ TêiÚYæéÖû|®bRÌqE|P¤*RÏ×kYæ[ì+Ðj\ËÔz¶«åkJ¯U¯ÔTiWèVêWVW«L«Ì5UÖÍêMsöÕ ¶jl	o!yÕØÞ°`rß=Y)·íoÉÝ)¿µ ÿñÅ.lT\`Þô,îþp^ÞAF Åb"ð>H}Z¥Å&16[mVC³Þ`jÑ 7=G¨¨ÜÌ<jFT#0²ÙmN=Ân·M±Äª\v(²ßbÔUÈ¤vÚÍQ ¢3³j³#Floû¤-²; éþ'òýsÊ¯_ºTeènI¢3ô=¦HÌô46 ÐD<Þo=ÏffÙ<<Pÿá~ãLûLçL×Ìè2\ÆÅB¶DW¢_lXh\½­Ák5d |
| --- | Minor | «_e¨1Ö5¦ëjÛJû ç ×èõh°U»U·I¿É°Á¸ÁºÞ¶Þ¹Þµ>úAª! |
| --- | Minor | ªïÙZeÞþ[lW~ë²2<A>©ØõêÞ«ÜAÐ°X4Dv-EDl0[êJIQÉhLõ!A'Rêg5Þî ã+ã0áTäÉTäÔ°SØ¤à/ví¸5oÙ¼OaksUÒ.þéÆ?=ÿQ oùÍåâyËpìqJ^FÉÿvú8ÊWåòKÍÏ }UJnöèÿ4)Íf1>bZ«D+¨×Jn>®´¬Õ>7TFÞj´³(Ñ¬11ê´AªMíT¯2;©Ñën;ä±-p<à¼×	g½àûhñDÚ´®:s=V×3 |
| --- | Minor | ««Ìº2ËÇ#ëNÉâ©¦ßÈÇQ6æ$Ð¦E9UÃWªæ³¨QãDdH"ç¤#ØÝ»ìÎ`@Òôú"ý2ýZ}³ÇIÔèsm^|ëLÏkgÎ0ãÏÑçÃ^û÷H'û¤ÑÀÓD¨ÕiãâX·¨Ói§hunkÇ |
| --- | Minor |  Ø¥>{­ØµÔ\ê+JskuXÃhcHjcSI£¶±½ìaXåûì#ur 4JÃ·ÐT@1"PëN¤¤/K_ÎQ§g§g¡þÎªø»4%êHCi}QGM&UKGj|ª;Õ0D«ªªªÏ5äÆ |
| --- | Minor | êêÉMâ¨¨¤¨?Ñ=Ñ31a¶f¶v¶n¶~¶{¶gvBºBS¡­ÐëËã+ÜRo¦N[§«Ó×êâëÜuºZoNKzk:úc{¥8©LLy"5XaHRãkïIH>SÍ:{ìTÕ·>< |
| --- | Minor | ×Knn­2ýÙ3?Ysñµw_¿¿­ë ±Ûáç7TÔäuá§g~._x¦ñºòP^Îð7¯|¤8(ê½ÊCNh©¤ã¤^g7éY*Ì|{À`HÔÅD3NäLÈãxv´wtwòÀ(c¥ÜÀñøè¢hªU·yìu)ìu!W½Çnf x¢À1Ô¤:û:ÈãF&pöÔ_:ooÉoÃñ®¬¼¼»[þüóÏqa¡ýµüÓ<fbµ-Íi XÊöh Y8äÜ©j²x¶yã·Zt!ãä'#AïwOË¹ìi© ´:Á>oÙÕ!wÝøRÐfÊ'%ii«SÎ¥±¡søs´±m\ßfk³·9ÎEsséaíÙ·=ÅDUä¶óñ½àÍ¦±d~»iýÆêÆåÃ[Êþºë fv®[ú¨8·èg3?ý OýãÊPå£ÛðéßUOÊ?Ýòk×Ï¿ªÄOÃ`Õ'!²"/%y8 ¸]ª¨]"U(d(Rm5G»´ÙÆo3±>H Æ¬µúT}rÇ¼. 9!¡mVÚFXVqGqéàçëÚnÞl«{~°¼îÜÚ¸}{ãÖeTÖ³¤x®üÎ­[òÅ¹ÅÊðs?ÿäÓÏÞ9K±F¥Rr¡lÉö9~î	Sz+)6dè\ÈêâÓ¢©¹þe»b®»)rGàXeÐ)+Q6M[ú«µÔl¬ï÷­_\_/üÅÂr[ãcOìÝ³{Õ6yøÎQ/¿Ûºö«/¿üzM}3W#Ü»WJ¶³"pÏ¹K¿K0. À=¡H¿1ûm"ña?ÊqiÒ(û®Cp×qû +YIÄWeE¢@R5O¿wñ*_îìy±µµõµWÆ¬Í9'O­Ú¾©¼ûå²22­|Ý±QNªiä\ö*p=ùÑ")ËEqTMÝeQ=#èXï.'ØöéØýê!Îï1úPv²KÈ±§e;í¼¶1 ÎÎ ß¬Ì¬@h8 a@ë 6)¿/;Kñ	Ãq8µìd³YÝ×JÏÍ*2¯¯?°çªp¼·Uät÷_ü59ù%E¯¶5ÝØ¡ryk^çÂc»@b±¨Rò»¬;ÖiH«6i¶È4Üãç~O?õ»xò38ºÀ 8dðÔ3dB If>¤ªbQ£âhÂDÈ "´ýÐ(Dhàq'ìÂ_î¹v¬1¹¤²¾	Nè§Ò(·Ë¢gùtDXqñR÷'y¢¬ZN |
| --- | Minor | ~· 8Âtwúl~ËÈÛèO|}D¬&³äN:@)A%»º/2287X|<Øäî>P!} K¦&SéÈº¤¹¤½ä¸u.¨.Ä?. ð»:4DP²IÙ?YúüÁC2ÓRTY÷H¬Ôg×"³V¬ºôIÏmV`QÆø7[dFéeËêúÐüEË¤ÞêbIïûÿçx7;þ¸Ûþ¸ÕR¸Þèöí§^ ú2XÝiH. ¨IÇ7QWE\¶±jpwö©Õ	w;+i Ñ?ÄÑgðmVÄìÚ³g×®={wRê¼v |
| --- | Minor | ;å¯ò¿éè¸v­£ã`åe%Ëò{4 g²'áé:äE÷K~L±DÏîréCÆ¸[³ËºÕUä~Ô¸?1ÞØ.?VD>} ñv0¢Ä£¼íR7$µ&ÑpÒÖ/þðõ1­/>	³ìBNþ]|BUP	C~V~èNx"G+y õQïýQè	)A¥¶pC&ÄÙ·êÕ!Ó~­FÅd ÑoVùt~CÀ{{§Hw3»À7½ |
| --- | Minor | ®I|[ÙÓHÄ"#nFÙD»è£2]°ÄHDb%n¬M²K)ÊF<¤ÝØÍðwâTâ#Üé|_ÈûeÜÔÉ·ÐóEËàÃ¡lª|ãÞ©§[û`^YndÊä¬1]F)¹ØH*6B{'{µpM>û³¶àçN*aaTùlùLûáT¬»nVÝø~*Ö¹Ll/Þçöy|	>ïÍíÝýø9î99	³¼ëã×»×{Ö'¬÷îßíÞíÙ°Û{(þûçPÂ!o¬Þ~ÄzÄvÄ~Äq «2 |
| --- | Minor | &g³SShðÅÞdí§%gzàÀkx|hPþÑÌÕ¶íÍ?&§Ëñ$ùDyOá{î»}}ãO)Í9`'>. ÀVH	¯Ó[uê(PT´_]Ä"¿(öã¡¿èÓe* |
| --- | Minor | ;ÂÊAjïgÞ·Wj×ÝJS»] ]tXÉ~	âëÃzmò2àY/ËOf(?úü!<Wqï¬¯{LÙé²ÊÜò'.<~ú|æó ÄUXqô ¶ÙbµhÕ+T#´¸®1b	Ã4Óí®fU*Á2ÂjÑéu¢1ÐëuS. LT&=OEûµ*«Å. êuZZ%ÐåÁ&¶ÿ2¼íá>ä¸·q}g+¼ÑE{}{`··¾ìî½àM°]ã² ÍDË. Å¸TSj©/²lÖØy #ÙÜH~¤0T5L«¦¢bjÉµæ£qxjþ1Q7A?A```É·Þ pS@ Ø®/ TêiÚYæéÖû|®bRÌqE|P¤*RÏ×kYæ[ì+Ðj\ËÔz¶«åkJ¯U¯ÔTiWèVêWVW«L«Ì5UÖÍêMsöÕ ¶jl	o!yÕØÞ°`rß=Y)·íoÉÝ)¿µ ÿñÅ.lT\`Þô. îþp^ÞAF Åb"ð>H}Z¥Å&16[mVC³Þ`jÑ 7=G¨¨ÜÌ<jFT#0²ÙmN=Ân·M±Äª\v(²ßbÔUÈ¤vÚÍQ ¢3³j³#Floû¤-²; éþ'òýsÊ¯_ºTeènI¢3ô=¦HÌô46 ÐD<Þo=ÏffÙ<<Pÿá~ãLûLçL×Ìè2\ÆÅB¶DW¢_lXh\½­Ák5d |
| --- | Minor | «_e¨1Ö5¦ëjÛJû ç ×èõh°U»U·I¿É°Á¸ÁºÞ¶Þ¹Þµ>úAª!. |
| --- | Minor | Sentence exceeds complexity threshold, split for readability. Applying the split needs --strength moderate or higher. |
| --- | Minor | none (split proposal only; source not rewritten) |
| --- | Minor | none |
| --- | Minor | Check: NEEDS-LLM |
| --- | Minor | Flags:    not-assessed |
| --- | Minor | SENTENCE (Line 51, 101 words, 4 clauses)  [Script] |
| --- | Minor | okÃ:fÆð¾Fù*¾glÛðÕ×åF$¿ñþ¸Ù³ÊËåUrNY!_ï]ø¸u{oAÎÖ xÁDl4DÇ0.Ôl4´FÝl0T`# «¡Vas<# hLQÅ2Fbì6ðz5µZv¿ùéXÆf "QnQGbí&i²*vv·Ã>Tâù !ìUÔXj,æ8ÄÙ¸¯Æ¬`´©\*¦IÓú>Ñ,<¹+àîçøéÂLÍLm	.f¨+Ñ*¼y<ÌÖp5|­zµnµ¾Ö°Â¸B\iZéZ½2&XÌåàÃÚ¦á¾ä¿/W×âkq:NoÆM«dg0T¹ ø3æÍ£äW gIÌÇåå±æAÑøîØaÃ©Î]ar3ï#¬YX¬¨Ä÷ÀèÖnR ì8¢ÅlÉB1áê7[^?Ô"wÏièéþìÁ3Lzþ,¯ïéêþ6|®6Ñwu,ÿ´¾ù¦°éF5}~«l7)3Úè^&ÌÆÕ |
| --- | Minor | ;ßmùõã-Â¦oº"? |
| --- | Minor | okÃ:fÆð¾Fù*¾glÛðÕ×åF$¿ñþ¸Ù³ÊËåUrNY!_ï]ø¸u{oAÎÖ xÁDl4DÇ0.Ôl4´FÝl0T`# «¡Vas<# hLQÅ2Fbì6ðz5µZv¿ùéXÆf "QnQGbí&i²*vv·Ã>Tâù !ìUÔXj. æ8ÄÙ¸¯Æ¬`´©\*¦IÓú>Ñ. <¹+àîçøéÂLÍLm	.f¨+Ñ*¼y<ÌÖp5|­zµnµ¾Ö°Â¸B\iZéZ½2&XÌåàÃÚ¦á¾ä¿/W×âkq:NoÆM«dg0T¹ ø3æÍ£äW gIÌÇåå±æAÑøîØaÃ©Î]ar3ï#¬YX¬¨Ä÷ÀèÖnR ì8¢ÅlÉB1áê7[^?Ô"wÏièéþìÁ3Lzþ. ¯ïéêþ6|®6Ñwu. ÿ´¾ù¦°éF5}~«l7)3Úè^&ÌÆÕ |
| --- | Minor | ;ßmùõã-Â¦oº"?. |
| --- | Minor | Sentence exceeds complexity threshold, split for readability. Applying the split needs --strength moderate or higher. |
| --- | Minor | none (split proposal only; source not rewritten) |
| --- | Minor | none |
| --- | Minor | Check: NEEDS-LLM |
| --- | Minor | Flags:    not-assessed |
| --- | Minor | SENTENCE (Line 51, 64 words, 1 clauses)  [Script] |
| --- | Minor | U¡èD×âhr«ÙBÚhÿþ,R ¸AýaÞÛÔi®îÚ±ÝÞ;¹ëDßf 9Þ#wNN½~t3­`Ñé×Á)òGt9ûï§¼£l±üøNSÙmd¯8ê¥BC*À6ÅWÙ!Ó\ªýVÝ/n´ø£OëGj§Ío|Ñ7gÛÛ 2¥IY3ÕÛÛGZLÌL¬LlIdïDÜ^ÅæÒ·F#q¯o±ÆÜ½Äf>DBuû¶1?§	FÏ¿+©ë7_<pb6Çã÷oÛWÑ¬9²ò¢·~áî[£SÙ_Y! |
| --- | Minor | U¡èD×âhr«ÙBÚhÿþ. R ¸AýaÞÛÔi®îÚ±ÝÞ;¹ëDßf 9Þ#wNN½~t3­`Ñé×Á)òGt9ûï§¼£l±üøNSÙmd¯8ê¥BC*À6ÅWÙ!Ó\ªýVÝ/n´ø£OëGj§Ío|Ñ7gÛÛ 2¥IY3ÕÛÛGZLÌL¬LlIdïDÜ^ÅæÒ·F#q¯o±ÆÜ½Äf>DBuû¶1?§	FÏ¿+©ë7_<pb6Çã÷oÛWÑ¬9²ò¢·~áî[£SÙ_Y!. |
| --- | Minor | Sentence exceeds complexity threshold, split for readability. Applying the split needs --strength moderate or higher. |
| --- | Minor | none (split proposal only; source not rewritten) |
| --- | Minor | none |
| --- | Minor | Check: NEEDS-LLM |
| --- | Minor | Flags:    not-assessed |
| --- | Minor | SENTENCE (Line 51, 675 words, 17 clauses)  [Script] |
| --- | Minor | ÐE«Æ^BU653Ný~«Fn¸@#1³ß ê|8ÊêwÙiÆ	²§?ñwÐ_3û¥âty'ÄøÌøvÞ^Ón1âÆ#=×Z/?·ûä+áUý·ÞI·}º¸og¬èbRÞ!E* |
| --- | Minor | ¬fÚ*%eú3|ÁAãÏö%ý ç}ÀmVÝþÃÎþ{È<áÂ(Ë)û?ãÃãÆéâïØÝþ/L>íy¿ß`xÉPD{·ÌÉé»¡­ÈúÊ÷A ÜÊGH¸	Üj%ñ6c4 crú1FÒýý¾là2	BpIåõ{|É`>É |
| --- | Minor | <0áøÐhÍþ¤AwØ"¬iRB*Îbv4«üÓ­`0ðß²æñA®ô|p7WÒÿtý.¼ü G.¶ý=ú^Çdfïäxq®1ï/(^¥¼ù |
| --- | Minor | ì«ÿúQÏPñ#Õgw0Ã¸OX"Ç"dýëGÝËÄîztKßÒ£Ó²òûxt Êvþ8x¬-hómrÊ(#¡l¢mà~Þ{GÕÜeTERQW^äÏ "ö-´GÃØ:¥^ÄFhms>»I)ÃÝpúìoÂãÉûÐFÕ$ |
| --- | Minor | ó9üäaCNv]ï-úLp)­_FZsG`á¢ÊET#(n2Ð,ô:Ú± |
| --- | Minor | àsÌ æ9¢&éä2;=ÈþoÎËÝàgóí_¨~¥JRmRÉêyêª?Õ¬Ð|¤uhWi¯évè:õ÷4.m¢_ Þ/VâSâ«¦<ÓËfùEðÓay |
| --- | Minor | (íUÞÑ>ú~<«Å>}MS@sèû,}Göòn-mÓÔöL¤Mß2ü0Ò&ýÎ³ýÚ´ióÈn 1¨-Cµh9*EQ	ªQÞ&^R¡¢ YÐ#Üh4©AÕP£hZüpv"Z ã@kªÃ¦Ý«Zé-z!Ü³¾a¤VÌ0­`ì<e±2Ò |
| --- | Minor | ¿fY ßôMçù0o)sÃýðÜyÊµïÏ3]yJ)às4ªDåp©sÊ\AxzDýï»sêûÞ÷ÔïþQdEÿGtÊÿ*"ÿ§à)àEÒFà}{,¶|"x§Éèt/*@÷OèÙ3Ñ°9èAô#ô'	f1y©*:Îc5Ö+³rGGê1zl¤©óÃõ¨ ­óGúê¬H=¡ÌZé³Ëämy«-{«¼%±mäM=¹pÞÇ](&ç}ä\!9[ONkÉ)-yý5+÷z¼f%'äUÉÏdòLÉähëxîè-Ò:ÉËõä%¼h /Öq/XÉaùiü[1y>çsÏÉä@1yv·{6´¬Öp-I¤y2yF ûö¸}Id/Ûk {%vÜ¸ÇJö¬ewÈn}"ìúqÛ%;,ÜÎ ´ÔÈj |
| --- | Minor | ­ºEV®áVºÉR7ÕÄj,IÕ2=W%ez²Lb+ëÉÒ%#¸¥ådÉRQ®ã*DR±-×r-GÝ"¥%§¸R,.äJNµìâEIÜâB²Xb%0há-R\LØÈ|ÌIÑÜ\Læ É¤P&?L¬'sd2{,%d2ó¹_&ÓÉ4+¹/H î5rõä^#:JMîÑIÅdb¸LñDäÆ[H¾c4Ü8';ÆÂ-'cFÜ=JËÉ(IÍÒIM wË5!&£'e=ÈÊeËdPd%YA |
| --- | Minor | e!Áj.¨!Á°|ªI 3%l\fÉ<ÇÓpldÀZ6C]Ìeì&þt+çLÒaéV.±i@zZ1IM	p©£H  >¨|2IJôQ\R!Iô¹ÄéÄ·yÍÄ+±	*âqGqBâ7qî(â>ÇÆÃÃâM .^×Óÿ¿ý ÿ×üÃDLÿ	GÍJ endstream endobj 127 0 obj <</Length 143/Filter/FlateDecode>> stream xíÏËN0Ð "ø TP* ÿÿ}LaApa\¸9'¹Óé¤IÛä'û4«^¦UõªÒN'×µv+7Þñäí¾Þå¾êC¥ÎÜòXyúáÃ2Îs^òI¦yÛOß3Ë<,«ÿÈg¾²ªnM¾ÿI                øGÛ©Ü endstream endobj 128 0 obj <</Length 405/Filter/FlateDecode>> stream x]ËnÂ0E÷ù /Û yØ	!UtÃ¢vX :w6Éra:=²~õ¥Ô7î×.{ÛöÉf#Ò/¼î.^LßÐs"H?!×Ù³xúÙ·aø¥ÙQ,íVj½Ý[=¼×éÔ¼ØïÆûÂ·=*¾ï|Ò¶¤{C×¡Öäj{¦d³ôÏVlZÿl²æ_>_¢­içú<Ô#O^¯ÏÙRsvÈ$q¬TäÀQf¢¨,¹¨d¬cÅÛ ál |
| --- | Minor | \bÅ2~HdÈ³c	,KÆk`>FÂD²d	É&Mþ»b(sX)Â9¨ aûa§'Yñ§d©p Eµ±fj©°VÅKWeL¢V¼Û(Wú¢<ÏÂñæ0\Épæy×7çü¨Olñ0Ý¥ùýºÂû³GïÚ endstream endobj 132 0 obj <</Length1 3560/Length 2307/Filter/FlateDecode>> stream xÍUypUÕÿîýóÞËËö¶@Ix¼%ïð&$M0X¢	yYÈBI,>#¬ÚH Û¸Ì´ |
| --- | Minor | >»Øh¬ |
| --- | Minor | ÔÖ¡3Ep¦u` Óê8N-3Üô»÷vZÿ¬ç{Î÷ûÎ·ï,"rq'È[^Zv'¹#%¥ãÊ+Uv/ÝÈ¸±·¼re	½t¥qqÑ]Å+ÆÜá?À¸ñeyþ÷%©¯ªk« |
| --- | Minor | büãªºî.ï¾À±/°mn5¶ý½çóü/<¿»±¶3DV&Mã[77Ùô,ã.Æêkq½ÙAd©b<».olñ~ÆMm]«ÈÀ¿bìim¯«åÑÐÇð×V») ÍyoÝæVÞØQßBÓ[k»ÖÓô¶Ú®&þ |
| --- | Minor | »[¶çéTAEqdý«!TåeqNg¢J?¶ÝÀJÓ(¿¾µ)	ì·ûÛõè¾¨®1ÞäÇøøü¾1¸î¯]ÛÇ|ÑMÓ©¼JûÍs/&(ûIò²aztÄYjP]ìÁb´HU5+¦I¯¢¡,HÚ5åbñèå°µMùÛM¯FÃèÇûlF,b¤ïQ<&Æ×c^bÔ:º÷©7kÌF?:ù,Ò»Lï1·i=AýÌ_¢­¦ü°Ä¥¡û |
| --- | Minor | *ÓXO5HÉc?*½Á~<wõ÷ÓZsþ*Nt§ÕIEs¦E? |
| --- | Minor | ÐE«Æ^BU653Ný~«Fn¸@#1³ß ê|8ÊêwÙiÆ	²§?ñwÐ_3û¥âty'ÄøÌøvÞ^Ón1âÆ#=×Z/?·ûä+áUý·ÞI·}º¸og¬èbRÞ!E* |
| --- | Minor | ¬fÚ*%eú3|ÁAãÏö%ý ç}ÀmVÝþÃÎþ{È<áÂ(Ë)û?ãÃãÆéâïØÝþ/L>íy¿ß`xÉPD{·ÌÉé»¡­ÈúÊ÷A ÜÊGH¸	Üj%ñ6c4 crú1FÒýý¾là2	BpIåõ{|É`>É |
| --- | Minor | <0áøÐhÍþ¤AwØ"¬iRB*Îbv4«üÓ­`0ðß²æñA®ô|p7WÒÿtý.¼ü G.¶ý=ú^Çdfïäxq®1ï/(^¥¼ù |
| --- | Minor | ì«ÿúQÏPñ#Õgw0Ã¸OX"Ç"dýëGÝËÄîztKßÒ£Ó²òûxt Êvþ8x¬-hómrÊ(#¡l¢mà~Þ{GÕÜeTERQW^äÏ "ö-´GÃØ:¥^ÄFhms>»I)ÃÝpúìoÂãÉûÐFÕ$ |
| --- | Minor | ó9üäaCNv]ï-úLp)­_FZsG`á¢ÊET#(n2Ð. ô:Ú± |
| --- | Minor | àsÌ æ9¢&éä2;=ÈþoÎËÝàgóí_¨~¥JRmRÉêyêª?Õ¬Ð|¤uhWi¯évè:õ÷4.m¢_ Þ/VâSâ«¦<ÓËfùEðÓay |
| --- | Minor | (íUÞÑ>ú~<«Å>}MS@sèû. }Göòn-mÓÔöL¤Mß2ü0Ò&ýÎ³ýÚ´ióÈn 1¨-Cµh9*EQ	ªQÞ&^R¡¢ YÐ#Üh4©AÕP£hZüpv"Z ã@kªÃ¦Ý«Zé-z!Ü³¾a¤VÌ0­`ì<e±2Ò |
| --- | Minor | ¿fY ßôMçù0o)sÃýðÜyÊµïÏ3]yJ)às4ªDåp©sÊ\AxzDýï»sêûÞ÷ÔïþQdEÿGtÊÿ*"ÿ§à)àEÒFà}{. ¶|"x§Éèt/*@÷OèÙ3Ñ°9èAô#ô'	f1y©*:Îc5Ö+³rGGê1zl¤©óÃõ¨ ­óGúê¬H=¡ÌZé³Ëämy«-{«¼%±mäM=¹pÞÇ](&ç}ä\!9[ONkÉ)-yý5+÷z¼f%'äUÉÏdòLÉähëxîè-Ò:ÉËõä%¼h /Öq/XÉaùiü[1y>çsÏÉä@1yv·{6´¬Öp-I¤y2yF ûö¸}Id/Ûk {%vÜ¸ÇJö¬ewÈn}"ìúqÛ%;. ÜÎ ´ÔÈj |
| --- | Minor | ­ºEV®áVºÉR7ÕÄj. IÕ2=W%ez²Lb+ëÉÒ%#¸¥ådÉRQ®ã*DR±-×r-GÝ"¥%§¸R. .äJNµìâEIÜâB²Xb%0há-R\LØÈ|ÌIÑÜ\Læ É¤P&?L¬'sd2{. %d2ó¹_&ÓÉ4+¹/H î5rõä^#:JMîÑIÅdb¸LñDäÆ[H¾c4Ü8';ÆÂ-'cFÜ=JËÉ(IÍÒIM wË5!&£'e=ÈÊeËdPd%YA |
| --- | Minor | e!Áj.¨!Á°|ªI 3%l\fÉ<ÇÓpldÀZ6C]Ìeì&þt+çLÒaéV.±i@zZ1IM	p©£H  >¨|2IJôQ\R!Iô¹ÄéÄ·yÍÄ+±	*âqGqBâ7qî(â>ÇÆÃÃâM .^×Óÿ¿ý ÿ×üÃDLÿ	GÍJ endstream endobj 127 0 obj <</Length 143/Filter/FlateDecode>> stream xíÏËN0Ð "ø TP* ÿÿ}LaApa\¸9'¹Óé¤IÛä'û4«^¦UõªÒN'×µv+7Þñäí¾Þå¾êC¥ÎÜòXyúáÃ2Îs^òI¦yÛOß3Ë<. «ÿÈg¾²ªnM¾ÿI                øGÛ©Ü endstream endobj 128 0 obj <</Length 405/Filter/FlateDecode>> stream x]ËnÂ0E÷ù /Û yØ	!UtÃ¢vX :w6Éra:=²~õ¥Ô7î×.{ÛöÉf#Ò/¼î.^LßÐs"H?!×Ù³xúÙ·aø¥ÙQ. íVj½Ý[=¼×éÔ¼ØïÆûÂ·=*¾ï|Ò¶¤{C×¡Öäj{¦d³ôÏVlZÿl²æ_>_¢­içú<Ô#O^¯ÏÙRsvÈ$q¬TäÀQf¢¨. ¹¨d¬cÅÛ ál |
| --- | Minor | \bÅ2~HdÈ³c. KÆk`>FÂD²d	É&Mþ»b(sX)Â9¨ aûa§'Yñ§d©p Eµ±fj©°VÅKWeL¢V¼Û(Wú¢<ÏÂñæ0\Épæy×7çü¨Olñ0Ý¥ùýºÂû³GïÚ endstream endobj 132 0 obj <</Length1 3560/Length 2307/Filter/FlateDecode>> stream xÍUypUÕÿîýóÞËËö¶@Ix¼%ïð&$M0X¢	yYÈBI. >#¬ÚH Û¸Ì´ |
| --- | Minor | >»Øh¬ |
| --- | Minor | ÔÖ¡3Ep¦u` Óê8N-3Üô»÷vZÿ¬ç{Î÷ûÎ·ï. "rq'È[^Zv'¹#%¥ãÊ+Uv/ÝÈ¸±·¼re	½t¥qqÑ]Å+ÆÜá?À¸ñeyþ÷%©¯ªk« |
| --- | Minor | büãªºî.ï¾À±/°mn5¶ý½çóü/<¿»±¶3DV&Mã[77Ùô. ã.Æêkq½ÙAd©b<».olñ~ÆMm]«ÈÀ¿bìim¯«åÑÐÇð×V») ÍyoÝæVÞØQßBÓ[k»ÖÓô¶Ú®&þ |
| --- | Minor | »[¶çéTAEqdý«!TåeqNg¢J?¶ÝÀJÓ(¿¾µ)	ì·ûÛõè¾¨®1ÞäÇøøü¾1¸î¯]ÛÇ|ÑMÓ©¼JûÍs/&(ûIò²aztÄYjP]ìÁb´HU5+¦I¯¢¡. HÚ5åbñèå°µMùÛM¯FÃèÇûlF. b¤ïQ<&Æ×c^bÔ:º÷©7kÌF?:ù. Ò»Lï1·i=AýÌ_¢­¦ü°Ä¥¡û |
| --- | Minor | *ÓXO5HÉc?*½Á~<wõ÷ÓZsþ*Nt§ÕIEs¦E?. |
| --- | Minor | Sentence exceeds complexity threshold, split for readability. Applying the split needs --strength moderate or higher. |
| --- | Minor | none (split proposal only; source not rewritten) |
| --- | Minor | none |
| --- | Minor | Check: NEEDS-LLM |
| --- | Minor | Flags:    not-assessed |
| --- | Minor | SENTENCE (Line 51, 490 words, 4 clauses)  [Script] |
| --- | Minor | âv!p:úVïÒ<z^&¾±´Î2°÷Åô:}¨<F/*g(L{¨Ó,abçÓÔÌ´V1é3ZcF6dÍòÅÃy¯³÷£re²5hPªxª2À÷º¶S³¨aÊ2©Ô\_t |
| --- | Minor | ã®N«kÔi"Kà8FÓìæq¾ |
| --- | Minor | éBþT#|Lý0*"OÐbëbKb±iÏnE@9lI£ c{¸e{ènå,G!½bªBÙ^GDõ- F´{ª¼ï¬ý |
| --- | Minor | ªÄoöTTruD¦Fà³E/ãÂ¼½¤¢ÊùCYé¨×²RUV1k ³¼¬4Ìâç3e¦Å|®³¸¢S(¬Í´¦R²c¦}6s%À¾eí¨'NÉ¡øyîlkbVl6Å¤ ­¨ú-esô&­Ðy[áj%+WÉbIS&;IÎcFA `ÖìÜxw?¶líÛ«¾}üúÇ/_ÿüøõO"È'î}eµ´(«Vîí~µ ¹Ë¿:nô-5§Þ01zßÔÕ}jæm Vîub¯&ö0·g.Ü= §ô&Ã;,&q°INLêév¤k"-©	)ùrB%RØkJ>uç ãus ÉãI-ð¸ÝÒãGn7\¬çËëÔáàÁQDÎ?±	< #Ä'#^q:bÄj-°³= lV§´y`uÂ"ýÒd;é`g"ìTµC©éPàö=Êïl£ÿwÿ³ñßôß$¸¸´ endstream endobj 134 0 obj <</Length 10/Filter/FlateDecode>> stream xc`    endstream endobj 135 0 obj <</Length 229/Filter/FlateDecode>> stream x]PÁjÃ0½û+tlÅmA0öÃº±l§±cËÁ°ØFqùûÉN×±	d!¿÷Ää¹½´Ág/Mp3ÄáÖ|ëêkFdq·LÇ6¸(ä+S¦66ö¸  É"ù0ÀæýÜ­_ÝÒ2ìR`Ññ¸'®zDU¼k-ã>/;ý2Þp¬ýaµd¢Å)i¤Ã¢Ùs(hì?ü¦êÝ_úZ>¸Nê³hXeLÙùîÑÌDl¯¦ú*|ÀûíRLEUòòt endstream endobj 139 0 obj <</Length1 2956/Length 1931/Filter/FlateDecode>> stream xÍV{PT×ÿîý³À.»ì²À5°äé¢ï\ê³JÄZ´YX·¬¢k6QÆñØ$NØ±iº'ÅTûN'còG§q:¶ÓNÇvÚþá´~{6ôßö|sîù¿ï÷}çÞ¹s)Dä¢(ÖÕûî¦·)<icKO L.=Äö/ÙÛ²«_?Qyù/DI÷Øw&nëù]ôO7TÁñ¡¶@_XÈe;µ­{ ùôm¢l¶·sîüõ?ð|¬ËÓ`®|¶óÛ{ú÷hDÙ`ÛÝÝÛ vpþA~Ø{{Â¢X÷³m}[ §Uÿpá;±ïb¸·¯§-\Çgw´wØþÆýq}ùÅ÷ªn:?påÒ­iÿJ¹ÉqrzçPÎ¾¯3þñûýäx¿É¤Rbp^RMäÉî÷-¦ay#aÙ*¹é|üMU&8l |
| --- | Minor | ÜG¥<ÏfNbÅm ©é`³AÚ¤ªèÔu¡Ú ºW÷Ú4SS.$õ(¿IôDV­ÂzwV×à©ñS±VAº¶ºÔ½SSç¯ï%X^·IU¡Ý=¦úVÇ'ônUZò©»ô1ªsè±©©ºñÜ4&gÁ<&|yw>-x§´du]>ö³ÚiÖÚ¦öÕ7°·ØÍþÚR©QãÃø±7oäËAÜ4Ä|üÈ·®È·¸^Fü0k;põ |
| --- | Minor | ^õã |
| --- | Minor | ?~`âuß7ñ=WL¼:¶\¾zcËñ]ßàÛ&¾åÂåÑTyYÃh*¾éÇ7øz.ùñÊËAùxiØ%_òad]øðÕÕø_.ÃÅÃ9ò¢/¸åÙ¸àÆùs.yÞs;çÂ9CåÄ³ÎFÅ°ÃøgVÈ3&^8í/øpúSöâtL1qê¤]râTL!c¥8iÇÉ	q¢7"Oãø³yÜã8ÆÚ±x~h\>obèh£ÇPT=âGqÔG¸¯#>>äsp865aLCréÁ VàÀCxnÏ: |
| --- | Minor | eÔÄ3ÝnùLöG\r¿öíMû¼Ø§1àÁ;vïÒåîûØµs¦Ü¥cçLôsRúLì0±=ìÛM¢7m=Kå¶.ô,EwWªìv£;*ºRÑeN.Ùyíã²ÃD{[£lG{T´|²­mùÐÊ ÖûÑfM[Ëd­exÊD£-«ñÅ6ØT_0±q7QÄz |
| --- | Minor | ·.MÖE°. |
| --- | Minor | âv!p:úVïÒ<z^&¾±´Î2°÷Åô:}¨<F/*g(L{¨Ó. abçÓÔÌ´V1é3ZcF6dÍòÅÃy¯³÷£re²5hPªxª2À÷º¶S³¨aÊ2©Ô\_t |
| --- | Minor | ã®N«kÔi"Kà8FÓìæq¾ |
| --- | Minor | éBþT#|Lý0*"OÐbëbKb±iÏnE@9lI£ c{¸e{ènå. G!½bªBÙ^GDõ- F´{ª¼ï¬ý |
| --- | Minor | ªÄoöTTruD¦Fà³E/ãÂ¼½¤¢ÊùCYé¨×²RUV1k ³¼¬4Ìâç3e¦Å|®³¸¢S(¬Í´¦R²c¦}6s%À¾eí¨'NÉ¡øyîlkbVl6Å¤ ­¨ú-esô&­Ðy[áj%+WÉbIS&;IÎcFA `ÖìÜxw?¶líÛ«¾}üúÇ/_ÿüøõO"È'î}eµ´(«Vîí~µ ¹Ë¿:nô-5§Þ01zßÔÕ}jæm Vîub¯&ö0·g.Ü= §ô&Ã;. &q°INLêév¤k"-©	)ùrB%RØkJ>uç ãus ÉãI-ð¸ÝÒãGn7\¬çËëÔáàÁQDÎ?±	< #Ä'#^q:bÄj-°³= lV§´y`uÂ"ýÒd;é`g"ìTµC©éPàö=Êïl£ÿwÿ³ñßôß$¸¸´ endstream endobj 134 0 obj <</Length 10/Filter/FlateDecode>> stream xc`    endstream endobj 135 0 obj <</Length 229/Filter/FlateDecode>> stream x]PÁjÃ0½û+tlÅmA0öÃº±l§±cËÁ°ØFqùûÉN×±	d!¿÷Ää¹½´Ág/Mp3ÄáÖ|ëêkFdq·LÇ6¸(ä+S¦66ö¸  É"ù0ÀæýÜ­_ÝÒ2ìR`Ññ¸'®zDU¼k-ã>/;ý2Þp¬ýaµd¢Å)i¤Ã¢Ùs(hì?ü¦êÝ_úZ>¸Nê³hXeLÙùîÑÌDl¯¦ú*|ÀûíRLEUòòt endstream endobj 139 0 obj <</Length1 2956/Length 1931/Filter/FlateDecode>> stream xÍV{PT×ÿîý³À.»ì²À5°äé¢ï\ê³JÄZ´YX·¬¢k6QÆñØ$NØ±iº'ÅTûN'còG§q:¶ÓNÇvÚþá´~{6ôßö|sîù¿ï÷}çÞ¹s)Dä¢(ÖÕûî¦·)<icKO L.=Äö/ÙÛ²«_?Qyù/DI÷Øw&nëù]ôO7TÁñ¡¶@_XÈe;µ­{ ùôm¢l¶·sîüõ?ð|¬ËÓ`®|¶óÛ{ú÷hDÙ`ÛÝÝÛ vpþA~Ø{{Â¢X÷³m}[ §Uÿpá;±ïb¸·¯§-\Çgw´wØþÆýq}ùÅ÷ªn:?påÒ­iÿJ¹ÉqrzçPÎ¾¯3þñûýäx¿É¤Rbp^RMäÉî÷-¦ay#aÙ*¹é|üMU&8l |
| --- | Minor | ÜG¥<ÏfNbÅm ©é`³AÚ¤ªèÔu¡Ú ºW÷Ú4SS.$õ(¿IôDV­ÂzwV×à©ñS±VAº¶ºÔ½SSç¯ï%X^·IU¡Ý=¦úVÇ'ônUZò©»ô1ªsè±©©ºñÜ4&gÁ<&|yw>-x§´du]>ö³ÚiÖÚ¦öÕ7°·ØÍþÚR©QãÃø±7oäËAÜ4Ä|üÈ·®È·¸^Fü0k;põ |
| --- | Minor | ^õã |
| --- | Minor | ?~`âuß7ñ=WL¼:¶\¾zcËñ]ßàÛ&¾åÂåÑTyYÃh*¾éÇ7øz.ùñÊËAùxiØ%_òad]øðÕÕø_.ÃÅÃ9ò¢/¸åÙ¸àÆùs.yÞs;çÂ9CåÄ³ÎFÅ°ÃøgVÈ3&^8í/øpúSöâtL1qê¤]râTL!c¥8iÇÉ	q¢7"Oãø³yÜã8ÆÚ±x~h\>obèh£ÇPT=âGqÔG¸¯#>>äsp865aLCréÁ VàÀCxnÏ: |
| --- | Minor | eÔÄ3ÝnùLöG\r¿öíMû¼Ø§1àÁ;vïÒåîûØµs¦Ü¥cçLôsRúLì0±=ìÛM¢7m=Kå¶.ô. EwWªìv£;*ºRÑeN.Ùyíã²ÃD{[£lG{T´|²­mùÐÊ ÖûÑfM[Ëd­exÊD£-«ñÅ6ØT_0±q7QÄz |
| --- | Minor | ·.MÖE°.. |
| --- | Minor | Sentence exceeds complexity threshold, split for readability. Applying the split needs --strength moderate or higher. |
| --- | Minor | none (split proposal only; source not rewritten) |
| --- | Minor | none |
| --- | Minor | Check: NEEDS-LLM |
| --- | Minor | Flags:    not-assessed |
| --- | Minor | SENTENCE (Line 51, 278 words, 2 clauses)  [Script] |
| --- | Minor | k«j¬q`U+M+±ÂåpËå^|6µª]Öf¡fWÖtaYµ[.ó¢ºÊ!«Ý¨2RdF ø{¬Oc©(K?%5¹d5/²ËÅb¤ËX0ß#¤c¾;ñys59ÏÄÜJ¯«¡Òo^øç¤H¿þÄ÷òLYQò²Yò	Qce(Ò ,FI±&KV£7Q¬¡Ø³¹õÙAVÈ¢*rc(à¥ÀÄgÂçÌ¾Fäç¥ËüzäqZ^:òñh2férV#ô\Ô3¡O\.ëAnTäØcì<ÌLÃ#ùx8«B>\,fÍª@¦\tÜÈÐ4ÑÍëÍ^/Ò>¿^	7/îj¤qÿiÃpqÌeÂÉÎL8 |
| --- | Minor | jÂÁÃß;cì¤äÉ<°I¿´E 9Oú!LIU;z	%¦)Åÿ·þ× |
| --- | Minor | ×Á§b§>>!bô6Ë»¬­¡NÚNhõ»´×ò_ÉqaÏ2}bJãÔ¸(åÖó&óTrì.ãClP³¿IK.`RÝM*êX«³2F(EB`21­¬·i	]¥Ñ¸.'iqëé6K5³¯¢kôr.)·(BÇ¨Ï:Z³»¼Å½tR³¼eÉ=>ñãã¾NyË¦q¥NÞç5f¿ð+EÊz4!¤4ðUe+Ø;H¢¥Àk=¨ê^®?½_T·¨E¢@å:ñÌ?JK¸ßwº§ï¿§¤rYò:­JZeKUlIÚÀÑ½¨T.Ø²©"ØÀkÙwÖ*·¹Jâu®oV~¯©Í|z»^SI(Tþ9ä~ïçÞY³6cÍß_SÄ§=ð"õ7­3?®+TÈVBWùZðÛiIÖÅÇ02Û´n£|%Q/ivPµQ;õóí¡Z¨W?U°T²ÖÌ¿SÇûxî V P°w%mc|kUÔÍ¢óWýWeµòÚÊ9»ød¤jXëd´- |
| --- | Minor | ÔYóëÌ²aÆ43oãtÎïåº+ö O½U¥¿Îæ s^{¯æ¬^êúTüFKëc½×ªéç.+iÞ'ð¡?É=}oÚoÝÇþsë;«teú®ÈßÉðOß¯Q endstream endobj 141 0 obj <</Length 40/Filter/FlateDecode>> stream xíÁ	     ÿÛ¨	               p¢@+  endstream endobj 142 0 obj <</Length 228/Filter/FlateDecode>> stream x]±nÄ wÂãÝp"I×(Ru]2´=5íTu `"¤Æ yûI¯R-eüÖåµêÉE7özÀÖa\üÊaÄÉ¨0NÇ£*·U2ÁÃ¶D{²^´-È·Ô\"opz4~Ä³  ùÊÙÑ§ë°? |
| --- | Minor | k«j¬q`U+M+±ÂåpËå^|6µª]Öf¡fWÖtaYµ[.ó¢ºÊ!«Ý¨2RdF ø{¬Oc©(K?%5¹d5/²ËÅb¤ËX0ß#¤c¾;ñys59ÏÄÜJ¯«¡Òo^øç¤H¿þÄ÷òLYQò²Yò	Qce(Ò. FI±&KV£7Q¬¡Ø³¹õÙAVÈ¢*rc(à¥ÀÄgÂçÌ¾Fäç¥ËüzäqZ^:òñh2férV#ô\Ô3¡O\.ëAnTäØcì<ÌLÃ#ùx8«B>\. fÍª@¦\tÜÈÐ4ÑÍëÍ^/Ò>¿^	7/îj¤qÿiÃpqÌeÂÉÎL8 |
| --- | Minor | jÂÁÃß;cì¤äÉ<°I¿´E 9Oú!LIU;z	%¦)Åÿ·þ× |
| --- | Minor | ×Á§b§>>!bô6Ë»¬­¡NÚNhõ»´×ò_ÉqaÏ2}bJãÔ¸(åÖó&óTrì.ãClP³¿IK.`RÝM*êX«³2F(EB`21­¬·i	]¥Ñ¸.'iqëé6K5³¯¢kôr.)·(BÇ¨Ï:Z³»¼Å½tR³¼eÉ=>ñãã¾NyË¦q¥NÞç5f¿ð+EÊz4!¤4ðUe+Ø;H¢¥Àk=¨ê^®?½_T·¨E¢@å:ñÌ?JK¸ßwº§ï¿§¤rYò:­JZeKUlIÚÀÑ½¨T.Ø²©"ØÀkÙwÖ*·¹Jâu®oV~¯©Í|z»^SI(Tþ9ä~ïçÞY³6cÍß_SÄ§=ð"õ7­3?®+TÈVBWùZðÛiIÖÅÇ02Û´n£|%Q/ivPµQ;õóí¡Z¨W?U°T²ÖÌ¿SÇûxî V P°w%mc|kUÔÍ¢óWýWeµòÚÊ9»ød¤jXëd´- |
| --- | Minor | ÔYóëÌ²aÆ43oãtÎïåº+ö O½U¥¿Îæ s^{¯æ¬^êúTüFKëc½×ªéç.+iÞ'ð¡?É=}oÚoÝÇþsë;«teú®ÈßÉðOß¯Q endstream endobj 141 0 obj <</Length 40/Filter/FlateDecode>> stream xíÁ	     ÿÛ¨	               p¢@+  endstream endobj 142 0 obj <</Length 228/Filter/FlateDecode>> stream x]±nÄ wÂãÝp"I×(Ru]2´=5íTu `"¤Æ yûI¯R-eüÖåµêÉE7özÀÖa\üÊaÄÉ¨0NÇ£*·U2ÁÃ¶D{²^´-È·Ô\"opz4~Ä³  ùÊÙÑ§ë°?. |
| --- | Minor | Sentence exceeds complexity threshold, split for readability. Applying the split needs --strength moderate or higher. |
| --- | Minor | none (split proposal only; source not rewritten) |
| --- | Minor | none |
| --- | Minor | Check: NEEDS-LLM |
| --- | Minor | Flags:    not-assessed |
| --- | Minor | SENTENCE (Line 51, 1286 words, 17 clauses)  [Script] |
| --- | Minor | kß8#E¨D×AÆ=«ð¢fYàKoRßÅí°?ÅûR×»%í |
| --- | Minor | .AidE¶JÑAkStÉüëÔhySÕI¾§Ï=eîWGäÿÞýé9Y+K)²Gxß[ð!Sùü hÃsV endstream endobj 144 0 obj <</Type/XObject/Subtype/Form/BBox[-6.6 -6.6 6.6 6.6]/Length 134/Filter/FlateDecode>> stream xm=0wNÑ¼¦´ø3;z.ÆÄû¯VÒjR¼¯ »[é `?º()Oü8ÅY3I,,=_ÒÄ*W&«ÂjÑnØÝ¨P«2dÅ®ÖÞP5fjÿÂßÿÐÌwr´¡³2º·Açøòñ,±-t¥«K' endstream endobj 145 0 obj <</Type/XObject/Subtype/Form/BBox[-6.6 -6.6 6.6 6.6]/Length 35/Filter/FlateDecode>> stream x3PÈâ2PðbC=3\.]&r¸\\N\ ´åô endstream endobj 146 0 obj <</Type/XObject/Subtype/Form/BBox[-6.6 -6.6 6.6 6.6]/Length 38/Filter/FlateDecode>> stream x3PÈâ2PðâÒ5Ô3S ¹\pf	aé"\\N\ /× f endstream endobj 147 0 obj <</Type/XObject/Subtype/Form/BBox[-7.2627417 -7.2627417 7.2627417 7.2627417]/Length 49/Filter/FlateDecode>> stream x3PÈâ2PðâÒ5PÐ5Ò323271RÈå3 |
| --- | Minor | ròpn.T ·w­ endstream endobj 148 0 obj <</Type/XObject/Subtype/Form/BBox[-6.52169043 -6.29442719 6.52169043 6.6]/Length 100/Filter/FlateDecode>> stream xm1@{^Á Èµ¾Äý+ÆÂ\C`3ì®âÔ ¼ 1uªL6ÌtÁ«ÄøiL¢Ý°6ÉL·WÆæõ£û@!"uN©Ý$wÖoXágY&Ü endstream endobj 152 0 obj <</Type/XObject/Subtype/Form/FormType 1/BBox[0 0 246.23206187 205.7448312]/Matrix[1 0 0 1 0 0]/Resources<</Font 114 0 R/XObject 143 0 R/ExtGState 149 0 R/Pattern 150 0 R/Shading 151 0 R/ProcSet[/PDF/Text/ImageB/ImageC/ImageI]>>/Filter/FlateDecode/Length 3269>> stream xÚÕ[Ë¹%bvµ´ Â+:lÔRê½pa^ íðîfÌïòÎ_ç*UT[· ¡"¸y¥Tê(OfêÑ§ß>ýÏOçOÞûºýæQs:~:×¨ö~.[Ù¾ÀÏûVµ÷ðsÙH|ºjÈ8A¤#||Y~$i7&h¹¬?>ogÍé]¨yn÷F°Î¶Þ C5«(´ÞÄBü²4BË¬2k¨di7íT9µ*8á£ñ&xÛ*ÂD'É´o¶ÿl_µ§w)Y&¤¬N7R(KÑ(å¡?@JÞXÕ¾½/ðó¾êÑ®öhÞ;²%t7QBZë|«b¦ x ©Î:4fì%fµ0ÎÏbnâ¤2¸Þ*¥	R¥J UX= |
| --- | Minor | iö>"ÇðAn`Ò&@ióDY#È'#ôèÑ2Þ=ÑðI¥%Äì]>@îDÀB(?S]WúÚ;ç&öTòÂþ ÑUjÒæ[à%&Äh*4ñ?òÖO/L\Z»ä_7ÚòLÍIíýäsRö=\à I d@Î¾%·aEæQ2êô®éxyÇìÙPÉ:¯ -S%7ø[¶w$t¥Ùj(Dï[G4Æ²íùUóõYsú½j}{ö,Å³æq{û¿;I\ñÒ_`~ûdtÑ[cÑDé`D+HÜIûc{v¿ùî¬yð¹] ÄfîÆzKáa´y¬Lø´h@{ aÍ ÜõauQ FKçñÓ"M7tKp ñn´·UF\:ÆàÆ$Cü(|åMà;¦« Q¼ßMø ¼DÞRu ßuBÆ(Þð¦Ê |
| --- | Minor | ½Rm´¨Å®àÅEVWðx7ÀÛ*ÌÛ |
| --- | Minor | ÿ¶(ò®àª´(F4:Ç.I&hw£IVCÇX<và±oßúù¤={ÑhAà\ê¹}ëm2]·,ÿ%É-ïtÙþiá+i¤ð CÑZÎsk¤)å¯³<(g°ä¯VF}õÃ1b!þ©Ö[Ê/z5Z6_tÍø%-§ßSFºý}÷u/V`/k+³&_ÜÚ¨kþðj×º¿ËR%m¥}M~]~²æÿ^Yø+²æ@k(\®è_×é÷:/þWÿËÉd¾£øÃCßØ WúÊç­ýNX |
| --- | Minor | `¤TtE;[éY(ç38¶±RJ´ù«¬< ©ÞGe¾À"ª ¥³ :Ê÷ZéËVºÖ 5NÄ¨]P:ZsEÓgc°ÖN åû ­ôe@+]krÅêQÈçh¸A@ËcèÐòs ¾h¥k |
| --- | Minor | ·sÚÞ4<Ê/¤ÑùMÅÍzþI_¹hµ¢ÍJjM¾VI­U{Çý-Ë­ªÛ¯UIò°Õlçà×Á °c³f¾øÀ*ïÖß>ºlKn®yÁ·Âà6²½;Ëü9Å=  Èl¨rùÞ!`ëËè£÷Ó»2ØuW3Yß êó6»O"Dê¯ÛÆ»sá]Jwü®f|î¿/q6É©ù `´Ì(Åûòöôï²ýöõÐ6ñ8AkA:8¯¬~³ñlr"Ø´Ð!DÁë×QõKqdÕfë}ª03vXwêhÉ{eÑÛsDäán³õ×G	þX×tÉ9½ÈþÂ|ºì4°¦}¸NÀéÙ²¦ b1æ«d¨¸¢Á° Ýd± [Or>p/ó¶4ãúH]ÞÉt¢ür1 ÃQ°k¤-EÐ­¹Ü´Ê·OcocÏæPÏ]Yöd5ÚÕhWV;ÔÚ ­QUaYmÜl­4;H/¥Ýl<Ïj´+«Ñ¬FO¸~SÔ.áÉ´1¤§90P¶úæ@"+Þè\}Ùot[ çHH ~òæPu^õ R fÝZë]T9Ôz?ôªÌI{¨õ<)j=w½+éLïÉdúúuÔ#¸Ä*ÎVÞ`-=×Z{Úu­ª§ckOÍV¦­=ehuä«@ 9qxðâZõvPìk8³îr³ß `#nÒÞ/´ÞÜj­«'¨·Êl7g4sJÆóôÞ\åk&riéò`Ò¢»|(¶|óS\/=rë,>½Z}*Ç¿·:ê%ÇÛ­&bwBa<ÖÛôNE[É9ÔD¶ë¢Ô #Âv1_?FBt,C1âe	ày)rB(ÔCÊQÐZ½È5²d9ú2D©øYB¡äDÊ¹Á«näÞÆÞ/<D Ì^óxOÙlöU»½KºÉA5÷ÉÊfbåyêe½¶¦ÁÚÉ`0èÇæì>ð1=>VaÃpüxjñ­|®^@Ê)ÓÐç |
| --- | Minor | '³:¾C1Ófió^?ä)¤Ãà>D}èÉÕd+=2Ð;*u2õÏt:T9 _äxª!*õ?éöfCI×#ª{¯GòÚ'ÊtOGBôkG¾?ÆÿkO	ã@ÿÍ£ÜW [ÿÍº¶þR@jBØdÅñZ 7æ«ÿæ4Ò|óÅÀÍ,þsjä¸ s ÛÑ.GðaZ[£§hÐ}e0EÂÈûúË¢øm Ö³g2"E`'=Xð>O Ë¬ø.hSÙoù§¤ÖN£6­_iÉØ% JkÚÎÏý¢9ÔÓ|We¦7U2ííéújµBpÁ9·mÀú0ë}ëýµOÏôk?>8Mû´zÉ¢õè3R,w]Â¿*hE%ó#,hW4°Ân&ÔïRòã.fÔVóôµ>$Æþßjd]î÷szuþ*^©"IXLàí4ÏÍdùÉp/gY~÷ÿ57ümªª~Ô\æÊçõÂ¼¦¨SbÚ¡'²|è±²ðzZÒFÀÔï|L@v¡¨ÿÄ'L5(üØÏBþýoù¹2rl²%vI(Fc¶[QsØ®ónZåèÅÒ{^¯¤Uö\b½åJzÓY¨â~J)t^ÎµPâÎ]u£ñù¨Qüqsç_ íq¼ÆÍDõ¥?v+§£ä	KÞ%JD>p¯°Îë;u+x=Ô·#7úr¶àtYá~âÃ­Ê¾¾Hi>iU ÓPTúL\® j1òXÍv;æËbk	ÅoÅµ^×1B°ÝÜ@©NZ£Bô<jÔhËgp!xUL'õ£x_h9®Ý|lÈ¦õfí¶ZUç/àÄ Ûã Õvñú4÷Áþ1òÞ®7ûF0"þ)3}c4ç×¾âFF,KÜ6à¢¯ì£ØzÿýÂ:º8ìXªùS_ÔcDz­Ãv¹»>ÿËÕÉ¼Z-ÅËâyá÷áXvoý!ï¾ß/bP®/¯ÊeuB|U°`0ñjúLq^ÇÔ¶Ïgy~±/ºÌV³ü7Ï?sÉU§©Ìóló,=ÄX¨EEåè\ÑÂTææIrÉ{`·¤"Y½H¦6W4ÏãÏ8O»(ææÿDsW endstream endobj 156 0 obj <</Filter/FlateDecode/Length 2904>> stream xÚÝZK·¾çWôqÁÐd±øÇ ­Qkm.ôMï¾íÖÎ0-= |
| --- | Minor | <6ïÊ/Li}ç_U |
| --- | Minor | ëzùzë°<óX©íåüãëo¯Ú¥Ò1ÄXöZQyëÜFY¼ëU)*Ú¯OË.|ñõ½¼øûòþhÌb´J:i¥ªà£2ICªò±¾ðf/U>ºîÆZúÕñ^ßNkÙÛCù?ÄX¢x)Ïæ}ôýV¢B7¥ F5	h)ÏV!Ó¤Â;JÖtûwÁ7~ |
| --- | Minor | Ó<sìôê²ê?Üïë^öEO±.#1	Ö|#-Ë¦QYEÒ±Ê!i´h× ØdÇ¤¤XØ* ÆhKÖA£ßÞU2ô¯É)úJöqB8 y1± £Ä6:_e.°¾aYûûþ­Èß²¶7½Löb4*pNÊå[ |
| --- | Minor | ò}c3è³3w+'âù |
| --- | Minor | ¯m¦õÇbl°:³ÍæÝ¶¥;³¾¬&Ê&^FÓJÅHÙßÉ[k5é,£	Ay´XþIÅ+ëBbs¬Ù<vÅÖqu²XïÂ,kµRvZ-o |
| --- | Minor | ±nØ^Öõù[tÛÍÁ²iá6û¹=½¯"ü³WLè}èÒHH^ÞdmU(W"	Eºzª0Ó+xoªÜ3"<¬Ùù,ûBÕ£ì Ó´i'ñ§Jy5Æ ^g*¾#pZß2%ðQWÁwãüØxÓêY¤©½r§Ê¬xÜ?÷M÷ûâ |
| --- | Minor | )è}{Êk¤¦ÌÈ±'ód·û¸Ä¼gÝØª¾ßºØÊê42¤))OEsÔt³ i}PVGd[, ã"¡Ñ=lCHa®3¶ |
| --- | Minor | ­ÕFØ	s½¨Kì8ïã:KÉ6IÔ²fÍ9«üÄz8ÉÊ-ÀîC/:¥=º ¼?MP7)0q]è¦F(§L ¹ÿVçJîT Ú=Qy²¨a±*¹ó¦FØRÚ»WÞ¹ 7¥<*zJlg¡}Ç~_,;³5¼ýÍyP èÌó7§?ÿæÄú(³¿¯©ûdÈfÃ((ÈÇ2­YÔ¶*xg%·øÏe§MÉ6ãáÀPìg8³d£vDN/¨&¹¯¸JOá¡vMsDhH:Í¼Ùü70rµs¯L4pQÆûØïxs '>=¼è¼àã$ >¾[>é"AêB¥oó<GR%Êj]Äê£újQÊ^FsÌ¿n0Úm¥¤	¤0yÌ|x±ï=IikÈÁEpnëCCNKÎØ¥§ýêî! |
| --- | Minor | kß8#E¨D×AÆ=«ð¢fYàKoRßÅí°?ÅûR×»%í |
| --- | Minor | .AidE¶JÑAkStÉüëÔhySÕI¾§Ï=eîWGäÿÞýé9Y+K)²Gxß[ð!Sùü hÃsV endstream endobj 144 0 obj <</Type/XObject/Subtype/Form/BBox[-6.6 -6.6 6.6 6.6]/Length 134/Filter/FlateDecode>> stream xm=0wNÑ¼¦´ø3;z.ÆÄû¯VÒjR¼¯ »[é `?º()Oü8ÅY3I. =_ÒÄ*W&«ÂjÑnØÝ¨P«2dÅ®ÖÞP5fjÿÂßÿÐÌwr´¡³2º·Açøòñ. ±-t¥«K' endstream endobj 145 0 obj <</Type/XObject/Subtype/Form/BBox[-6.6 -6.6 6.6 6.6]/Length 35/Filter/FlateDecode>> stream x3PÈâ2PðbC=3\.]&r¸\\N\ ´åô endstream endobj 146 0 obj <</Type/XObject/Subtype/Form/BBox[-6.6 -6.6 6.6 6.6]/Length 38/Filter/FlateDecode>> stream x3PÈâ2PðâÒ5Ô3S ¹\pf	aé"\\N\ /× f endstream endobj 147 0 obj <</Type/XObject/Subtype/Form/BBox[-7.2627417 -7.2627417 7.2627417 7.2627417]/Length 49/Filter/FlateDecode>> stream x3PÈâ2PðâÒ5PÐ5Ò323271RÈå3 |
| --- | Minor | ròpn.T ·w­ endstream endobj 148 0 obj <</Type/XObject/Subtype/Form/BBox[-6.52169043 -6.29442719 6.52169043 6.6]/Length 100/Filter/FlateDecode>> stream xm1@{^Á Èµ¾Äý+ÆÂ\C`3ì®âÔ ¼ 1uªL6ÌtÁ«ÄøiL¢Ý°6ÉL·WÆæõ£û@!"uN©Ý$wÖoXágY&Ü endstream endobj 152 0 obj <</Type/XObject/Subtype/Form/FormType 1/BBox[0 0 246.23206187 205.7448312]/Matrix[1 0 0 1 0 0]/Resources<</Font 114 0 R/XObject 143 0 R/ExtGState 149 0 R/Pattern 150 0 R/Shading 151 0 R/ProcSet[/PDF/Text/ImageB/ImageC/ImageI]>>/Filter/FlateDecode/Length 3269>> stream xÚÕ[Ë¹%bvµ´ Â+:lÔRê½pa^ íðîfÌïòÎ_ç*UT[· ¡"¸y¥Tê(OfêÑ§ß>ýÏOçOÞûºýæQs:~:×¨ö~.[Ù¾ÀÏûVµ÷ðsÙH|ºjÈ8A¤#||Y~$i7&h¹¬?>ogÍé]¨yn÷F°Î¶Þ C5«(´ÞÄBü²4BË¬2k¨di7íT9µ*8á£ñ&xÛ*ÂD'É´o¶ÿl_µ§w)Y&¤¬N7R(KÑ(å¡?@JÞXÕ¾½/ðó¾êÑ®öhÞ;²%t7QBZë|«b¦ x ©Î:4fì%fµ0ÎÏbnâ¤2¸Þ*¥	R¥J UX= |
| --- | Minor | iö>"ÇðAn`Ò&@ióDY#È'#ôèÑ2Þ=ÑðI¥%Äì]>@îDÀB(?S]WúÚ;ç&öTòÂþ ÑUjÒæ[à%&Äh*4ñ?òÖO/L\Z»ä_7ÚòLÍIíýäsRö=\à I d@Î¾%·aEæQ2êô®éxyÇìÙPÉ:¯ -S%7ø[¶w$t¥Ùj(Dï[G4Æ²íùUóõYsú½j}{ö. Å³æq{û¿;I\ñÒ_`~ûdtÑ[cÑDé`D+HÜIûc{v¿ùî¬yð¹] ÄfîÆzKáa´y¬Lø´h@{ aÍ ÜõauQ FKçñÓ"M7tKp ñn´·UF\:ÆàÆ$Cü(|åMà;¦« Q¼ßMø ¼DÞRu ßuBÆ(Þð¦Ê |
| --- | Minor | ½Rm´¨Å®àÅEVWðx7ÀÛ*ÌÛ |
| --- | Minor | ÿ¶(ò®àª´(F4:Ç.I&hw£IVCÇX<và±oßúù¤={ÑhAà\ê¹}ëm2]·. ÿ%É-ïtÙþiá+i¤ð CÑZÎsk¤)å¯³<(g°ä¯VF}õÃ1b!þ©Ö[Ê/z5Z6_tÍø%-§ßSFºý}÷u/V`/k+³&_ÜÚ¨kþðj×º¿ËR%m¥}M~]~²æÿ^Yø+²æ@k(\®è_×é÷:/þWÿËÉd¾£øÃCßØ WúÊç­ýNX |
| --- | Minor | `¤TtE;[éY(ç38¶±RJ´ù«¬< ©ÞGe¾À"ª ¥³ :Ê÷ZéËVºÖ 5NÄ¨]P:ZsEÓgc°ÖN åû ­ôe@+]krÅêQÈçh¸A@ËcèÐòs ¾h¥k |
| --- | Minor | ·sÚÞ4<Ê/¤ÑùMÅÍzþI_¹hµ¢ÍJjM¾VI­U{Çý-Ë­ªÛ¯UIò°Õlçà×Á °c³f¾øÀ*ïÖß>ºlKn®yÁ·Âà6²½;Ëü9Å=  Èl¨rùÞ!`ëËè£÷Ó»2ØuW3Yß êó6»O"Dê¯ÛÆ»sá]Jwü®f|î¿/q6É©ù `´Ì(Åûòöôï²ýöõÐ6ñ8AkA:8¯¬~³ñlr"Ø´Ð!DÁë×QõKqdÕfë}ª03vXwêhÉ{eÑÛsDäán³õ×G	þX×tÉ9½ÈþÂ|ºì4°¦}¸NÀéÙ²¦ b1æ«d¨¸¢Á° Ýd± [Or>p/ó¶4ãúH]ÞÉt¢ür1 ÃQ°k¤-EÐ­¹Ü´Ê·OcocÏæPÏ]Yöd5ÚÕhWV;ÔÚ ­QUaYmÜl­4;H/¥Ýl<Ïj´+«Ñ¬FO¸~SÔ.áÉ´1¤§90P¶úæ@"+Þè\}Ùot[ çHH ~òæPu^õ R fÝZë]T9Ôz?ôªÌI{¨õ<)j=w½+éLïÉdúúuÔ#¸Ä*ÎVÞ`-=×Z{Úu­ª§ckOÍV¦­=ehuä«@ 9qxðâZõvPìk8³îr³ß `#nÒÞ/´ÞÜj­«'¨·Êl7g4sJÆóôÞ\åk&riéò`Ò¢»|(¶|óS\/=rë. >½Z}*Ç¿·:ê%ÇÛ­&bwBa<ÖÛôNE[É9ÔD¶ë¢Ô #Âv1_?FBt. C1âe	ày)rB(ÔCÊQÐZ½È5²d9ú2D©øYB¡äDÊ¹Á«näÞÆÞ/<D Ì^óxOÙlöU»½KºÉA5÷ÉÊfbåyêe½¶¦ÁÚÉ`0èÇæì>ð1=>VaÃpüxjñ­|®^@Ê)ÓÐç |
| --- | Minor | '³:¾C1Ófió^?ä)¤Ãà>D}èÉÕd+=2Ð;*u2õÏt:T9 _äxª!*õ?éöfCI×#ª{¯GòÚ'ÊtOGBôkG¾?ÆÿkO	ã@ÿÍ£ÜW [ÿÍº¶þR@jBØdÅñZ 7æ«ÿæ4Ò|óÅÀÍ. þsjä¸ s ÛÑ.GðaZ[£§hÐ}e0EÂÈûúË¢øm Ö³g2"E`'=Xð>O Ë¬ø.hSÙoù§¤ÖN£6­_iÉØ% JkÚÎÏý¢9ÔÓ|We¦7U2ííéújµBpÁ9·mÀú0ë}ëýµOÏôk?>8Mû´zÉ¢õè3R. w]Â¿*hE%ó#. hW4°Ân&ÔïRòã.fÔVóôµ>$Æþßjd]î÷szuþ*^©"IXLàí4ÏÍdùÉp/gY~÷ÿ57ümªª~Ô\æÊçõÂ¼¦¨SbÚ¡'²|è±²ðzZÒFÀÔï|L@v¡¨ÿÄ'L5(üØÏBþýoù¹2rl²%vI(Fc¶[QsØ®ónZåèÅÒ{^¯¤Uö\b½åJzÓY¨â~J)t^ÎµPâÎ]u£ñù¨Qüqsç_ íq¼ÆÍDõ¥?v+§£ä	KÞ%JD>p¯°Îë;u+x=Ô·#7úr¶àtYá~âÃ­Ê¾¾Hi>iU ÓPTúL\® j1òXÍv;æËbk	ÅoÅµ^×1B°ÝÜ@©NZ£Bô<jÔhËgp!xUL'õ£x_h9®Ý|lÈ¦õfí¶ZUç/àÄ Ûã Õvñú4÷Áþ1òÞ®7ûF0"þ)3}c4ç×¾âFF. KÜ6à¢¯ì£ØzÿýÂ:º8ìXªùS_ÔcDz­Ãv¹»>ÿËÕÉ¼Z-ÅËâyá÷áXvoý!ï¾ß/bP®/¯ÊeuB|U°`0ñjúLq^ÇÔ¶Ïgy~±/ºÌV³ü7Ï?sÉU§©Ìóló. =ÄX¨EEåè\ÑÂTææIrÉ{`·¤"Y½H¦6W4ÏãÏ8O»(ææÿDsW endstream endobj 156 0 obj <</Filter/FlateDecode/Length 2904>> stream xÚÝZK·¾çWôqÁÐd±øÇ ­Qkm.ôMï¾íÖÎ0-= |
| --- | Minor | <6ïÊ/Li}ç_U |
| --- | Minor | ëzùzë°<óX©íåüãëo¯Ú¥Ò1ÄXöZQyëÜFY¼ëU)*Ú¯OË.|ñõ½¼øûòþhÌb´J:i¥ªà£2ICªò±¾ðf/U>ºîÆZúÕñ^ßNkÙÛCù?ÄX¢x)Ïæ}ôýV¢B7¥ F5	h)ÏV!Ó¤Â;JÖtûwÁ7~ |
| --- | Minor | Ó<sìôê²ê?Üïë^öEO±.#1	Ö|#-Ë¦QYEÒ±Ê!i´h× ØdÇ¤¤XØ* ÆhKÖA£ßÞU2ô¯É)úJöqB8 y1± £Ä6:_e.°¾aYûûþ­Èß²¶7½Löb4*pNÊå[ |
| --- | Minor | ò}c3è³3w+'âù |
| --- | Minor | ¯m¦õÇbl°:³ÍæÝ¶¥;³¾¬&Ê&^FÓJÅHÙßÉ[k5é. £	Ay´XþIÅ+ëBbs¬Ù<vÅÖqu²XïÂ. kµRvZ-o |
| --- | Minor | ±nØ^Öõù[tÛÍÁ²iá6û¹=½¯"ü³WLè}èÒHH^ÞdmU(W"	Eºzª0Ó+xoªÜ3"<¬Ùù. ûBÕ£ì Ó´i'ñ§Jy5Æ ^g*¾#pZß2%ðQWÁwãüØxÓêY¤©½r§Ê¬xÜ?÷M÷ûâ |
| --- | Minor | )è}{Êk¤¦ÌÈ±'ód·û¸Ä¼gÝØª¾ßºØÊê42¤))OEsÔt³ i}PVGd[. ã"¡Ñ=lCHa®3¶ |
| --- | Minor | ­ÕFØ	s½¨Kì8ïã:KÉ6IÔ²fÍ9«üÄz8ÉÊ-ÀîC/:¥=º ¼?MP7)0q]è¦F(§L ¹ÿVçJîT Ú=Qy²¨a±*¹ó¦FØRÚ»WÞ¹ 7¥<*zJlg¡}Ç~_. ;³5¼ýÍyP èÌó7§?ÿæÄú(³¿¯©ûdÈfÃ((ÈÇ2­YÔ¶*xg%·øÏe§MÉ6ãáÀPìg8³d£vDN/¨&¹¯¸JOá¡vMsDhH:Í¼Ùü70rµs¯L4pQÆûØïxs '>=¼è¼àã$ >¾[>é"AêB¥oó<GR%Êj]Äê£újQÊ^FsÌ¿n0Úm¥¤	¤0yÌ|x±ï=IikÈÁEpnëCCNKÎØ¥§ýêî!. |
| --- | Minor | Sentence exceeds complexity threshold, split for readability. Applying the split needs --strength moderate or higher. |
| --- | Minor | none (split proposal only; source not rewritten) |
| --- | Minor | none |
| --- | Minor | Check: NEEDS-LLM |
| --- | Minor | Flags:    not-assessed |
| --- | Minor | SENTENCE (Line 51, 161 words, 5 clauses)  [Script] |
| --- | Minor | àîh|8üöÂáßï¯EõWÈÚþbC,ñ*EzÞ,öD5Ï×ù?¡úTCB}z'T_N&Bú'5ÂÍ]aMø)À­I4Q»lÈö`H5È¹nVÈoaù×BÅBãi'J½Ë=àCì_ÿuù¾Çcê¦±¤ª\x JFÍ#ÑÊ)Ú­(Ç LèÖtþµõ'­íT@õ½4qkIWeª] |
| --- | Minor | rb±MTÑ<Gk¡y±K~ VG6·]-ÝKÖÀáÚî<¡²wKÈ[÷}.(ÄJ«&µØ1	ÉPþÄþñj0\oC EIS&Y|ÄëÁyrö¶×ÀV8xýUð'vMj:Rªí*4%XÑ³yðÒwH5G¤¿yIä¹VÆñ¶è(WHahjÔ:þhK_è¾»m©¾$_Ù³u¾"° |
| --- | Minor | Ïc¤s¦·ýµÊãéëN)ÙÉ´rÏµLr£¨¬A½-¾ßí+?r¢C:þüàhû2üâ9òg@ÏÂZJ²pÈÏÝÍ(xÒ Ãt@ò[ðoÇØJáxÃØn-cº,Æ®×ÇFü¹&1Cº=K*bÒÎ,¾¥âm´F§DCRbU1h,ÈsXA L~.¸!ÅA XqªÍ¢ýå9îXÕxÿÇ}©æÏß(Ôj[VKF-¹¬¥Ú¬òã=öÊÇ¸ÍÑh  Y`(ÚHoSÞBÿºÏPyU4»8`'Àÿ8JF«ÚáofÙ'ç¸Í.ânvAØ í§kO? |
| --- | Minor | àîh|8üöÂáßï¯EõWÈÚþbC. ñ*EzÞ. öD5Ï×ù?¡úTCB}z'T_N&Bú'5ÂÍ]aMø)À­I4Q»lÈö`H5È¹nVÈoaù×BÅBãi'J½Ë=àCì_ÿuù¾Çcê¦±¤ª\x JFÍ#ÑÊ)Ú­(Ç LèÖtþµõ'­íT@õ½4qkIWeª] |
| --- | Minor | rb±MTÑ<Gk¡y±K~ VG6·]-ÝKÖÀáÚî<¡²wKÈ[÷}.(ÄJ«&µØ1	ÉPþÄþñj0\oC EIS&Y|ÄëÁyrö¶×ÀV8xýUð'vMj:Rªí*4%XÑ³yðÒwH5G¤¿yIä¹VÆñ¶è(WHahjÔ:þhK_è¾»m©¾$_Ù³u¾"° |
| --- | Minor | Ïc¤s¦·ýµÊãéëN)ÙÉ´rÏµLr£¨¬A½-¾ßí+?r¢C:þüàhû2üâ9òg@ÏÂZJ²pÈÏÝÍ(xÒ Ãt@ò[ðoÇØJáxÃØn-cº. Æ®×ÇFü¹&1Cº=K*bÒÎ. ¾¥âm´F§DCRbU1h. ÈsXA L~.¸!ÅA XqªÍ¢ýå9îXÕxÿÇ}©æÏß(Ôj[VKF-¹¬¥Ú¬òã=öÊÇ¸ÍÑh  Y`(ÚHoSÞBÿºÏPyU4»8`'Àÿ8JF«ÚáofÙ'ç¸Í.ânvAØ í§kO?. |
| --- | Minor | Sentence exceeds complexity threshold, split for readability. Applying the split needs --strength moderate or higher. |
| --- | Minor | none (split proposal only; source not rewritten) |
| --- | Minor | none |
| --- | Minor | Check: NEEDS-LLM |
| --- | Minor | Flags:    not-assessed |
| --- | Minor | SENTENCE (Line 51, 490 words, 5 clauses)  [Script] |
| --- | Minor | =mGþªm±4ÔWÝ:"IØç-cKnÚñÉAK¬ÂM^÷k'ªbÊNZjµ"£$:ÏOw;ç^'·KÝ<Ìå&RcÀåÉ"äè)}òª¾}ëº\Z|´l ©BÜîÿÏØ®ýö0å¦4ífxæ¨xbá¼¿6oïf¹ýã1ðV-kfI=éÚFññ¬Þ)§YìðM¨ùÙÅuB=iBY6>ðJLÛàï5úó¾Ñ:ÞlÎN%àbJ¶¸ÜÙ|S*Ø»'mçiæñLkd#Ö¾+§9ä®·ùdùýR>ùöîÇI v©u-ÎæV"BTÇõ ¨|¨3ZËÓu<_úf¢DfAù|©$+!Û´ÓÊ£lsüï_îëð¡ßMO!@º |
| --- | Minor | ¹5xºÅí Îím¹CÉP(Rrý«Óü1±pÆ|üùXíWN$YÀ¹®ï^¸|ve{.+3µÓAXO?¥/¡½ìCÎ	Ådúý îîÎÀ~UfÀXþ¸w?÷Õ CHµ2cDåÞ8bôÂ¿XÄ }JhO¥CBÚ^)ºOÜ¢íFÝ÷gÅ­O¢ä§;¬rXØ>éÌ³@wçÈÂj¢ðªj£|Ùñ%B<*Í TîxçÆw<|x÷ïIðsûè)øEëëe9¥u)=ýG:-<ê´ÓÞw¤fð¨]´õÇy¶ãRràº¼s¬¹s@U i ¼H±ÊDGèÜOho»*qX­#!U\T8m:¤ ·G ,T guiÿ£cÎºèibrmkmÊlpá£;yÝ±Cï´eÃÞwË¥&Åg­ö<Áæ¾$Ë6Þþ9ËRªi"x¬¡aIH1çÜkä¹ò±iC1!\*\1RlUß,¦ù¦ ë7µ4÷öjé¨\J^Ð Ö-#SC­Ùå`hß³ÊmÝ¦o]®¤ äÁí4[½.÷92}>¾_+Å±-§kuÇJì¤/§}Ü.W:¼Á#QÑÖ>Å8ögÁ(ËÏ:cÜziúMv#æõ @Ä-±»ÝhdPwÈ}½²´¡5)>*5f³§zô¡ïòK¨}íõËûñNVOÞjãe{S«^ö8ZòH²=wÊuw7wÝÓZFa\iµH£bÎòS°JÝ­´=b÷-5ªy4ôØêí§õJ^Ií$ |
| --- | Minor | ^¬"ªvñj¾SH}xÞ^ã¸\ìq½üÔ_ô¦È¨yýÖ»fí2Å«_ýAà endstream endobj 174 0 obj <</Filter/FlateDecode/Length 5812>> stream xÚå][ ÅDÞswéòKÎ6OÂºÜ]tõBØoÎF<±þ!þ0ø#¾Õg%ó+ð¿xÂçG|áÕ}j&ßÆ¦<_}Æ·Ó«TÖüV+ÑýyNÛ4zL¯2>&å8ÑúãoG3ê\ÜHiDÒo'ÒöÄÕbz¿Ù,@/@¥§:¿£ÈØJ¦yr^²ëÞ£ËSù¶üUæÁ««ã¹à7å­ÒùoEuÄoã!óiòËÐ¸¤õ&2íÀÝ×Ü«ã½²ðJÙºUôv ©'2Ñr3Riw:;¹IÐoøWÇ39Óf´%â?Á¿Øú×¥õ<:1 |
| --- | Minor | Y¿~u&çî~úþ»ÿøú®ô°ce7¯ÙS?üãz2¤·Mô¨4·ðÕ+>»wßüi1òôøwòWVSÞy!ã |
| --- | Minor | ìLß^,¦n6m4&&óEi51±ß4=ÓýÝ2/±cæÒýã#v`]Z·2~O¥É·£HõfÀ'i´ØV½9EJÎ}ãßýæx`©°cÚ/F¦F~½ØñÀþßbÁ=PBí(V.ðb¿XOÂú°®ÆFsÖÒ£XKÄvÎëÜr4¦ç £Â¡ãípzÓÁ:÷ãùÅ }$rjX-­óCLzõÎÝ³t><Hã»ï[;Ð«µÐà/o¾Ê_í| eËÍ9Gñî¾ý¯¶ñ Ð7ÏÒZ®y=ØP¨áî¯CL­È¯+~ª©­§õ(aè}¶ÀzÐÏÝßµÚ½)-;õ­óÐKîR·î ÐÐYGæäÀ=Ç³QBÌÑBØéA)²\MkXd:³ÙDSOÖÍáíçà µúJGÌÐY¼sîAEGÜ*"Ë0!V#®¶O[ÀM`7ikáclJJ0ô<){W¢xW<3åâéÞQÃåuö¡yÕE"FäÚ§K_þF'ôy,w¤öÂü¨øÝÍ0ëªYâ°ÙÐÐÊYZSz¡Åæ |
| --- | Minor | íã=Ý¦ßûÆ@gÇôeÉ*ÐïÓñïå¯Ç§ñ¸}ÚÓÔ«=ò°à±i¨²Â.ÿºÒæÐL! |
| --- | Minor | =mGþªm±4ÔWÝ:"IØç-cKnÚñÉAK¬ÂM^÷k'ªbÊNZjµ"£$:ÏOw;ç^'·KÝ<Ìå&RcÀåÉ"äè)}òª¾}ëº\Z|´l ©BÜîÿÏØ®ýö0å¦4ífxæ¨xbá¼¿6oïf¹ýã1ðV-kfI=éÚFññ¬Þ)§YìðM¨ùÙÅuB=iBY6>ðJLÛàï5úó¾Ñ:ÞlÎN%àbJ¶¸ÜÙ|S*Ø»'mçiæñLkd#Ö¾+§9ä®·ùdùýR>ùöîÇI v©u-ÎæV"BTÇõ ¨|¨3ZËÓu<_úf¢DfAù|©$+!Û´ÓÊ£lsüï_îëð¡ßMO!@º |
| --- | Minor | ¹5xºÅí Îím¹CÉP(Rrý«Óü1±pÆ|üùXíWN$YÀ¹®ï^¸|ve{.+3µÓAXO?¥/¡½ìCÎ	Ådúý îîÎÀ~UfÀXþ¸w?÷Õ CHµ2cDåÞ8bôÂ¿XÄ }JhO¥CBÚ^)ºOÜ¢íFÝ÷gÅ­O¢ä§;¬rXØ>éÌ³@wçÈÂj¢ðªj£|Ùñ%B<*Í TîxçÆw<|x÷ïIðsûè)øEëëe9¥u)=ýG:-<ê´ÓÞw¤fð¨]´õÇy¶ãRràº¼s¬¹s@U i ¼H±ÊDGèÜOho»*qX­#!U\T8m:¤ ·G. T guiÿ£cÎºèibrmkmÊlpá£;yÝ±Cï´eÃÞwË¥&Åg­ö<Áæ¾$Ë6Þþ9ËRªi"x¬¡aIH1çÜkä¹ò±iC1!\*\1RlUß. ¦ù¦ ë7µ4÷öjé¨\J^Ð Ö-#SC­Ùå`hß³ÊmÝ¦o]®¤ äÁí4[½.÷92}>¾_+Å±-§kuÇJì¤/§}Ü.W:¼Á#QÑÖ>Å8ögÁ(ËÏ:cÜziúMv#æõ @Ä-±»ÝhdPwÈ}½²´¡5)>*5f³§zô¡ïòK¨}íõËûñNVOÞjãe{S«^ö8ZòH²=wÊuw7wÝÓZFa\iµH£bÎòS°JÝ­´=b÷-5ªy4ôØêí§õJ^Ií$ |
| --- | Minor | ^¬"ªvñj¾SH}xÞ^ã¸\ìq½üÔ_ô¦È¨yýÖ»fí2Å«_ýAà endstream endobj 174 0 obj <</Filter/FlateDecode/Length 5812>> stream xÚå][ ÅDÞswéòKÎ6OÂºÜ]tõBØoÎF<±þ!þ0ø#¾Õg%ó+ð¿xÂçG|áÕ}j&ßÆ¦<_}Æ·Ó«TÖüV+ÑýyNÛ4zL¯2>&å8ÑúãoG3ê\ÜHiDÒo'ÒöÄÕbz¿Ù. @/@¥§:¿£ÈØJ¦yr^²ëÞ£ËSù¶üUæÁ««ã¹à7å­ÒùoEuÄoã!óiòËÐ¸¤õ&2íÀÝ×Ü«ã½²ðJÙºUôv ©'2Ñr3Riw:;¹IÐoøWÇ39Óf´%â?Á¿Øú×¥õ<:1 |
| --- | Minor | Y¿~u&çî~úþ»ÿøú®ô°ce7¯ÙS?üãz2¤·Mô¨4·ðÕ+>»wßüi1òôøwòWVSÞy!ã |
| --- | Minor | ìLß^. ¦n6m4&&óEi51±ß4=ÓýÝ2/±cæÒýã#v`]Z·2~O¥É·£HõfÀ'i´ØV½9EJÎ}ãßýæx`©°cÚ/F¦F~½ØñÀþßbÁ=PBí(V.ðb¿XOÂú°®ÆFsÖÒ£XKÄvÎëÜr4¦ç £Â¡ãípzÓÁ:÷ãùÅ }$rjX-­óCLzõÎÝ³t><Hã»ï[;Ð«µÐà/o¾Ê_í| eËÍ9Gñî¾ý¯¶ñ Ð7ÏÒZ®y=ØP¨áî¯CL­È¯+~ª©­§õ(aè}¶ÀzÐÏÝßµÚ½)-;õ­óÐKîR·î ÐÐYGæäÀ=Ç³QBÌÑBØéA)²\MkXd:³ÙDSOÖÍáíçà µúJGÌÐY¼sîAEGÜ*"Ë0!V#®¶O[ÀM`7ikáclJJ0ô<){W¢xW<3åâéÞQÃåuö¡yÕE"FäÚ§K_þF'ôy. w¤öÂü¨øÝÍ0ëªYâ°ÙÐÐÊYZSz¡Åæ |
| --- | Minor | íã=Ý¦ßûÆ@gÇôeÉ*ÐïÓñïå¯Ç§ñ¸}ÚÓÔ«=ò°à±i¨²Â.ÿºÒæÐL!. |
| --- | Minor | Sentence exceeds complexity threshold, split for readability. Applying the split needs --strength moderate or higher. |
| --- | Minor | none (split proposal only; source not rewritten) |
| --- | Minor | none |
| --- | Minor | Check: NEEDS-LLM |
| --- | Minor | Flags:    not-assessed |
| --- | Minor | SENTENCE (Line 51, 191 words, 5 clauses)  [Script] |
| --- | Minor | ûV[ yËÎxÖqÌ?}cð«Òaëú°4Cïå.'´à6ûheZd+5ù¦uÓ"/ l°"	ª6Å |
| --- | Minor | @Ë¯!fk|{tQº6Æ17Þr]äÙÞÍ@JPìbgSíH¦ç ïíÕK±°#¡&³¼Y;*ÜUGZÈ¨O§ß KÖþûâ Am,2ýÁ 6)<+}tH4iÙùÊ"gã§jF³?ÿ>	ô' .~þì³tã)IèÔ3*§¬ZDêYeoÒ¡|xüÃo¶+ÌJÄ¶-9ý³!ä¼r_öÃRßxú±!wé²Cò]&mí¬ @Hê%?-ì$±Yk"'®Ù*»uFÜ°Ää\º¤P¤ uºBØ*ÁvÐ«°:ÛÎ`é-@ß¸0+ |0nt·-]l jN®ïÒßLL_O¼Uùªþ>[º3iÿaicÕºØLÿ½ µD:8{ãtÕÍµ{;iÒeKC7)r¥á¢}ÁNq²»A¡U` |
| --- | Minor | ÷m3úi¥BQø$JÂvmjÄI×Óûîù©<ÂV±m²éT 	ä5*{Ì~RzG,L¯+RÅÞ0-6s9Ï¤±qóøR^{îgËVT0vZUiÉoä«ëbB,LÌ¤IVÑb"·­l1=f¥Â®¦ñSi_Íñ Ö,FÂ± °Ä[§lÒãåØ¥÷=ÙêJsR%à Øn«´u¥2IOðfÓÒQQD?­x6SõMà6gÉØR~Æë¥W·÷û}áÎAwóàv´8Ê Næ¿_ï½UÝøNnÎ©îëvCïµK£%æýføê&Áù+ó´ùB |
| --- | Minor |  jPSÏÍÔnÂdÖ\rSröÞgÐ\)öõú4xEØ6CuÛ ¾ûñéO§?@ØX)â¸, ÙÞÀXÙìùhOÿýô»Óo7ý(=ÓbS³. |
| --- | Minor | ûV[ yËÎxÖqÌ?}cð«Òaëú°4Cïå.'´à6ûheZd+5ù¦uÓ"/ l°"	ª6Å |
| --- | Minor | @Ë¯!fk|{tQº6Æ17Þr]äÙÞÍ@JPìbgSíH¦ç ïíÕK±°#¡&³¼Y;*ÜUGZÈ¨O§ß KÖþûâ Am. 2ýÁ 6)<+}tH4iÙùÊ"gã§jF³?ÿ>	ô' .~þì³tã)IèÔ3*§¬ZDêYeoÒ¡|xüÃo¶+ÌJÄ¶-9ý³!ä¼r_öÃRßxú±!wé²Cò]&mí¬ @Hê%?-ì$±Yk"'®Ù*»uFÜ°Ää\º¤P¤ uºBØ*ÁvÐ«°:ÛÎ`é-@ß¸0+ |0nt·-]l jN®ïÒßLL_O¼Uùªþ>[º3iÿaicÕºØLÿ½ µD:8{ãtÕÍµ{;iÒeKC7)r¥á¢}ÁNq²»A¡U` |
| --- | Minor | ÷m3úi¥BQø$JÂvmjÄI×Óûîù©<ÂV±m²éT 	ä5*{Ì~RzG. L¯+RÅÞ0-6s9Ï¤±qóøR^{îgËVT0vZUiÉoä«ëbB. LÌ¤IVÑb"·­l1=f¥Â®¦ñSi_Íñ Ö. FÂ± °Ä[§lÒãåØ¥÷=ÙêJsR%à Øn«´u¥2IOðfÓÒQQD?­x6SõMà6gÉØR~Æë¥W·÷û}áÎAwóàv´8Ê Næ¿_ï½UÝøNnÎ©îëvCïµK£%æýføê&Áù+ó´ùB |
| --- | Minor |  jPSÏÍÔnÂdÖ\rSröÞgÐ\)öõú4xEØ6CuÛ ¾ûñéO§?@ØX)â¸.  ÙÞÀXÙìùhOÿýô»Óo7ý(=ÓbS³.. |
| --- | Minor | Sentence exceeds complexity threshold, split for readability. Applying the split needs --strength moderate or higher. |
| --- | Minor | none (split proposal only; source not rewritten) |
| --- | Minor | none |
| --- | Minor | Check: NEEDS-LLM |
| --- | Minor | Flags:    not-assessed |
| --- | Minor | SENTENCE (Line 51, 776 words, 8 clauses)  [Script] |
| --- | Minor | Í#pOõ´°ºvÇf|ãÈUÀdm5	[øê2£¢ó]K ü<6ä¬QR'#¡E¤F=ý´fßLßø× ¨1!VÚAØ]ìô»fò½´Ýãn×§³qfOÍx<èäænl÷A0©A<øÃôÄàßih£(½[~D©­pF~8ãï3^ÂØsUUBNÎµô²ak©ÊÔYÿrµçcS-qK¯[©W>É_ªfó1ºtÔå±Ì¤õ«G½#¯:ïÄÑTÊub£fB 142@CyIZ|÷"÷j*Ê· u!ëXU°W&Ùp¬*9ÏSê_ÐÝ0ãyËÖ QÂ]ÀÎsLï  |
| --- | Minor |  ez5ØÌöbßxkUfs@?rµ*uk£ùàkP¢ºÊ&©Å¦Öâ¾Ú 0Ô8ìC[·» [í-à.Bî´°VºÞnÍ  éæßÇ­nQIi:ËÞÎÍöíoÅ³wRí¢rÕ²n©¸rcè'úé¢kXUHDg0ûo.30Mé.àªÄ:Ó%!ñ+Q B7r»È§X´rÞ>½¥uõ¦±MìÍ2p íZ[Ü7¶,ñöô´³-Ê^|ådvÚÒÛ³á*í¿·²õ»cÛ0lÆyE£úqépÀ&x?øh_/Õ¿&tþòÁ[`iíÝ7ÅWi»¸kyáÕ¹öT¢ÙròDÖøõÐoÐI½nÒ-Òb¤ z WLD|~lêSeÓXASÿ^²ÇywÎÝÔ¾ìy6O-E·ä2§Ñú£ËmEáwä¿ÏÁ 2Áu A­BÐÏV.ÈR^%Ë3>Úqma½r¶½:Xûg]Lß4^ßJOt«:÷´st²(¥#m"ÜwwòjzLÛÐy¡UU×ÓRìLèIæ°H/»G-&ô½TÙ·0åÂ§hó-içã |rçØr{í­ðPÞe~­ MîØ$3ÐbB¢ïZÔQuÓûFº#JxÌÃÂ;ÉÐyI*Ç»nÉsÞc¯iÉ6 ºë÷[³_Z º	óÜu(éwÇ¾äÉ gËú]cRáW9¤(vÒícå±>Qír Cî=ð«ãØMÈg[F¨üó¼ãòÊ4º Î*}Ð~O¥ ²R2ÃÁÒaçWÒÛoFyéfÚI)£:;äoªª0«ß×hdý>]¿OJèÜú¾qeW+¼nítSµæ©å¶dpµäH1ì ùO÷ÉÍõT Ã²+å©ù¡~_Î3ëÌNztãÃ Î8;Ã5©YKÝ·LÔAcôÌk¤ÎNrseÓôû¤×jÐ`+j  MÞ~a´êUE³¡.5ûüuÊÉ¼Hl7ïÈp 50ðjvËµDbE"'Â®#´ÓLªp°x&áT'ÎÖuleä8¢yr²ho§ÒTGs3½5ÀÀiYLÊ2÷h)îçOÃB2>©É]²¾r¥¦îÝÏKãß%áÎüèqN3/eiTû&±ÎgæóP³GkÉqøÓú(ê?[f |
| --- | Minor | úzã(*`2Ø§YçÍFz±Ý^V`¤Á.`ÁÑXGúJ¬Á^s 4WÃàZ¹M:­A9ÞÍèñÝIkÚ,yð´ÇBÝ(#«¾)Ð5ò¡O­a²Åô[v§Ü§UÁææó[vAã*1.íy/ðïÏ*hï±°n¨b¸O`ä8ß¯cöA±Ïýg*8®qÊ±¯Ù[Å½SÈ^ÓFÞ |
| --- | Minor |  bÇNMi*ý)u¥'	'ö=c"×ààHé¬ÙU"¦8Ïî'ø4Ú5«®\lÛÙÉ×Oç)CÂ:«¨ó¦=XthTÍ(wÐóH~© óG¼<l\ÞÁòJÁ&/%ýÆù´¡Èkì	 ÇÐù¼£¯2ÔuAzIc7¥5'Yèâ¤Ë¥&Ð]¡Èêo9ÓZ·¸>ÜH5º>4úæß½:K/ûÀÞø&Åq@>C²Z­¯|¹7jóäbÍ#éÿ´8YoÙ×È¡âh'·þþX8Ñæ=sÌ»f}Q¦Í#Âç×Éç¦¢Ö>oÞY»/¾_åërÚÛõx½ÌîäòKÝ -w`ÓæäoÿôûÀJ1&³¬U¿¥ò7F c2ÀgÇ3& (|=Ó3Ë Y¿ÁeNá9ö°Z;<¾éÑ |
| --- | Minor | RÍôà_úÕÙ	¬)£óÏ$ÝcL_ýyòò0áÃ%|XôàrEñ÷+aé ¼»Ä3'e%Ü-ðm1SÞÅÏµ5¸PÆøÝ\O:ê@ó«uÌ33ô¨TûÇR=Rå}4Ú¨Êëã{æx²1±ØTó­+ z§ËÁáJ·9]fÖQØ5¬¶4g¥`ü'1¦<¼18® -t1WÏ³Æ÷gÒFõØÀpröBcNéF"Wv×ð½Å	¢È%KÞÏsvÏÞ×¹æF3LTNÍ[lÜ/S¨¶, |
| --- | Minor | \¢ÒÑÕÂ}Üµ,7]²¦Î<¤¿ó¥î9!;Kî|¾®yöÚêI¡ÚB*ú5Lr"ÈZÀN8»RöýÒMÅÅ6+P	ÙqËb "l\"9ØÎ¢v"Ä<«ið|14yR)ÍèÔOv£<Ù|]û´XkEÎ¹, TbÓ]3\iìB	y.TLa6N_tÑÌÌåïPêxÀ!M­3­B­¤F¯Þc1M¯ø ¼Ù¼1- !ÌÕ¢¿\f-A/uåÜ±y öÅ3ú¼=F_O¥rõýAK©qínÊ×êÖ¬UÁÔ=ZlâêxUÆc:¿pm¼^CtR?¿ü"Ôe¬è®}øH¬ÊÖ/÷Ü5±0IÒ*Ï·pQÒRû\pÏ~6ð:Áò-[Ýã5§£XÐ¤÷îbÚ,(ÇB$÷~¸Ý-×G JjUµÝu>¸óå"83hÇôbØí?Ô¼ôÍäDº`bßXèC·¸¸Z1%Yåë;ÛãK¾¥6J¿X ÍåDÿ±ßýüÎµv	aáS¼ä¡°ßeôó÷|Í[@.°5%ÅJBañ%N÷øCáZðdJ©ÆuÍç ÿ¸«æ`xôNýÇCõ¼mî>cÍÙî þ¦åo°Zj?àJEsÎQ,yhmü4v×SN{3.£î|7bc'ÑJ>ð2Î}cÕ;Gy^B"NOºXw­·ÇµýâEÈ¯éTÅM1ùYSOÒ£=æ¸=_v*úpÀõÀqwnX`Òõ°Wdd10Âêpcf×Ba¸}ÇY° ªY2æb|f0^N¹èÇe¤®ÂüËWäîþñoÅ¥D¸ÛSß Ã\ÎS2;Òµ<W`NÚ§MEI{Äåø´ÇÿæcÙ~Ûø±Ïåé¿ZöõSº¯®LÜSKsJl/}jù.]2PMÂÛU©±tý_Æ8+¿gæ\áU§ö×·*£ùÚ£7wæ»ùL<öõ:Ëë¬RÁ|²2¤ãØ;,É4¬b6E°}Æ|#ÒwÑe=f«®¥Ø§&ýÅA1ù<Íá¹	¯6³zdVuÆ%iØ§î>µþ`Meq¼NÚé?v7f?¶´æ§M;c:T(9Uhµ"  |
| --- | Minor | *HkDps¦¬rÑ³á>í-ü{fÊëS&ÉæÄûMvy±ñÉî¾¤ÚUôuiíÍ³êÍ£îóR. |
| --- | Minor | Í#pOõ´°ºvÇf|ãÈUÀdm5	[øê2£¢ó]K ü<6ä¬QR'#¡E¤F=ý´fßLßø× ¨1!VÚAØ]ìô»fò½´Ýãn×§³qfOÍx<èäænl÷A0©A<øÃôÄàßih£(½[~D©­pF~8ãï3^ÂØsUUBNÎµô²ak©ÊÔYÿrµçcS-qK¯[©W>É_ªfó1ºtÔå±Ì¤õ«G½#¯:ïÄÑTÊub£fB 142@CyIZ|÷"÷j*Ê· u!ëXU°W&Ùp¬*9ÏSê_ÐÝ0ãyËÖ QÂ]ÀÎsLï  |
| --- | Minor |  ez5ØÌöbßxkUfs@?rµ*uk£ùàkP¢ºÊ&©Å¦Öâ¾Ú 0Ô8ìC[·» [í-à.Bî´°VºÞnÍ  éæßÇ­nQIi:ËÞÎÍöíoÅ³wRí¢rÕ²n©¸rcè'úé¢kXUHDg0ûo.30Mé.àªÄ:Ó%!ñ+Q B7r»È§X´rÞ>½¥uõ¦±MìÍ2p íZ[Ü7¶. ñöô´³-Ê^|ådvÚÒÛ³á*í¿·²õ»cÛ0lÆyE£úqépÀ&x?øh_/Õ¿&tþòÁ[`iíÝ7ÅWi»¸kyáÕ¹öT¢ÙròDÖøõÐoÐI½nÒ-Òb¤ z WLD|~lêSeÓXASÿ^²ÇywÎÝÔ¾ìy6O-E·ä2§Ñú£ËmEáwä¿ÏÁ 2Áu A­BÐÏV.ÈR^%Ë3>Úqma½r¶½:Xûg]Lß4^ßJOt«:÷´st²(¥#m"ÜwwòjzLÛÐy¡UU×ÓRìLèIæ°H/»G-&ô½TÙ·0åÂ§hó-içã |rçØr{í­ðPÞe~­ MîØ$3ÐbB¢ïZÔQuÓûFº#JxÌÃÂ;ÉÐyI*Ç»nÉsÞc¯iÉ6 ºë÷[³_Z º	óÜu(éwÇ¾äÉ gËú]cRáW9¤(vÒícå±>Qír Cî=ð«ãØMÈg[F¨üó¼ãòÊ4º Î*}Ð~O¥ ²R2ÃÁÒaçWÒÛoFyéfÚI)£:;äoªª0«ß×hdý>]¿OJèÜú¾qeW+¼nítSµæ©å¶dpµäH1ì ùO÷ÉÍõT Ã²+å©ù¡~_Î3ëÌNztãÃ Î8;Ã5©YKÝ·LÔAcôÌk¤ÎNrseÓôû¤×jÐ`+j  MÞ~a´êUE³¡.5ûüuÊÉ¼Hl7ïÈp 50ðjvËµDbE"'Â®#´ÓLªp°x&áT'ÎÖuleä8¢yr²ho§ÒTGs3½5ÀÀiYLÊ2÷h)îçOÃB2>©É]²¾r¥¦îÝÏKãß%áÎüèqN3/eiTû&±ÎgæóP³GkÉqøÓú(ê?[f |
| --- | Minor | úzã(*`2Ø§YçÍFz±Ý^V`¤Á.`ÁÑXGúJ¬Á^s 4WÃàZ¹M:­A9ÞÍèñÝIkÚ. yð´ÇBÝ(#«¾)Ð5ò¡O­a²Åô[v§Ü§UÁææó[vAã*1.íy/ðïÏ*hï±°n¨b¸O`ä8ß¯cöA±Ïýg*8®qÊ±¯Ù[Å½SÈ^ÓFÞ |
| --- | Minor |  bÇNMi*ý)u¥'	'ö=c"×ààHé¬ÙU"¦8Ïî'ø4Ú5«®\lÛÙÉ×Oç)CÂ:«¨ó¦=XthTÍ(wÐóH~© óG¼<l\ÞÁòJÁ&/%ýÆù´¡Èkì	 ÇÐù¼£¯2ÔuAzIc7¥5'Yèâ¤Ë¥&Ð]¡Èêo9ÓZ·¸>ÜH5º>4úæß½:K/ûÀÞø&Åq@>C²Z­¯|¹7jóäbÍ#éÿ´8YoÙ×È¡âh'·þþX8Ñæ=sÌ»f}Q¦Í#Âç×Éç¦¢Ö>oÞY»/¾_åërÚÛõx½ÌîäòKÝ -w`ÓæäoÿôûÀJ1&³¬U¿¥ò7F c2ÀgÇ3& (|=Ó3Ë Y¿ÁeNá9ö°Z;<¾éÑ |
| --- | Minor | RÍôà_úÕÙ	¬)£óÏ$ÝcL_ýyòò0áÃ%|XôàrEñ÷+aé ¼»Ä3'e%Ü-ðm1SÞÅÏµ5¸PÆøÝ\O:ê@ó«uÌ33ô¨TûÇR=Rå}4Ú¨Êëã{æx²1±ØTó­+ z§ËÁáJ·9]fÖQØ5¬¶4g¥`ü'1¦<¼18® -t1WÏ³Æ÷gÒFõØÀpröBcNéF"Wv×ð½Å	¢È%KÞÏsvÏÞ×¹æF3LTNÍ[lÜ/S¨¶. >\¢ÒÑÕÂ}Üµ. 7]²¦Î<¤¿ó¥î9!;Kî|¾®yöÚêI¡ÚB*ú5Lr"ÈZÀN8»RöýÒMÅÅ6+P	ÙqËb "l\"9ØÎ¢v"Ä<«ið|14yR)ÍèÔOv£<Ù|]û´XkEÎ¹.  TbÓ]3\iìB	y.TLa6N_tÑÌÌåïPêxÀ!M­3­B­¤F¯Þc1M¯ø ¼Ù¼1- !ÌÕ¢¿\f-A/uåÜ±y öÅ3ú¼=F_O¥rõýAK©qínÊ×êÖ¬UÁÔ=ZlâêxUÆc:¿pm¼^CtR?¿ü"Ôe¬è®}øH¬ÊÖ/÷Ü5±0IÒ*Ï·pQÒRû\pÏ~6ð:Áò-[Ýã5§£XÐ¤÷îbÚ. (ÇB$÷~¸Ý-×G JjUµÝu>¸óå"83hÇôbØí?Ô¼ôÍäDº`bßXèC·¸¸Z1%Yåë;ÛãK¾¥6J¿X ÍåDÿ±ßýüÎµv	aáS¼ä¡°ßeôó÷|Í[@.°5%ÅJBañ%N÷øCáZðdJ©ÆuÍç ÿ¸«æ`xôNýÇCõ¼mî>cÍÙî þ¦åo°Zj?àJEsÎQ. yhmü4v×SN{3.£î|7bc'ÑJ>ð2Î}cÕ;Gy^B"NOºXw­·ÇµýâEÈ¯éTÅM1ùYSOÒ£=æ¸=_v*úpÀõÀqwnX`Òõ°Wdd10Âêpcf×Ba¸}ÇY° ªY2æb|f0^N¹èÇe¤®ÂüËWäîþñoÅ¥D¸ÛSß Ã\ÎS2;Òµ<W`NÚ§MEI{Äåø´ÇÿæcÙ~Ûø±Ïåé¿ZöõSº¯®LÜSKsJl/}jù.]2PMÂÛU©±tý_Æ8+¿gæ\áU§ö×·*£ùÚ£7wæ»ùL<öõ:Ëë¬RÁ|²2¤ãØ;. É4¬b6E°}Æ|#ÒwÑe=f«®¥Ø§&ýÅA1ù<Íá¹	¯6³zdVuÆ%iØ§î>µþ`Meq¼NÚé?v7f?¶´æ§M;c:T(9Uhµ"  |
| --- | Minor | *HkDps¦¬rÑ³á>í-ü{fÊëS&ÉæÄûMvy±ñÉî¾¤ÚUôuiíÍ³êÍ£îóR.. |
| --- | Minor | Sentence exceeds complexity threshold, split for readability. Applying the split needs --strength moderate or higher. |
| --- | Minor | none (split proposal only; source not rewritten) |
| --- | Minor | none |
| --- | Minor | Check: NEEDS-LLM |
| --- | Minor | Flags:    not-assessed |
| --- | Minor | SENTENCE (Line 51, 327 words, 6 clauses)  [Script] |
| --- | Minor | ÛêKõOö¦Vþ¥¹Lrí·wUi¾=±)ÚåÇµe|Iûèº¼^^³£v¹Ð7ïÊÿâ­Är,£C·ãÌâv« _­tö¶¤ËnsÇ`{îX´QØ]lÜSÎýAÛÖRÏ´åYÒÄ§éÆ¢JG-¾£¼ã4JFaHz-7c½úZN2¥À¶rÛùæ;6N¸vó×XWØûOw6óm¶]ØkëÒÍ 6Jyã>àú|Æðªº}[Ôó-nãkZö¹Ãÿòö0d²Ñð÷®AÂ¤~ûÿú¼Sÿ endstream endobj 188 0 obj <</Filter/FlateDecode/Length 4670>> stream xÚÝ\YdÉU~çW ÀLÃÛHU]­±¦Í_ÀóÀoçØ×7»{0Ð­îª¼7gùÎqúáÄOÿòánsôçôü½Çú7§¿þ;~Âo4hyzózâmÊ:}¹1)­8½yùÍcÚâ?ö~Áÿc1Æ/øþ¯)Nmñwl¯ga¾Oáj)þôßVùm Ö6ç¿Á§Jß©O[Ëãoßüêô7§Nqqyú7qg\-höôá$eX¹­~wúæôë°|uâlsÌ1k=r@U~4«KY¡T UËÎÝ l©ÀÏ(Ûtm´Âr¤DuZS×Ï ø,¾Ü½ |
| --- | Minor | ßçÇ³4` ããÙoNÁÍ"²{ x( |
| --- | Minor | ªDàÇ3Õóþx*è5x;ñ-bGi0Oç(»#Ò°Þ!6­íÞä§GöF Lfn)Vo¨0øÝW÷ó9ÚÍpPö¼Ú°ß^0 |þèÙ(½I£³y³3)&!%ÍàÉsËÌmO¸Lhÿõb@üÀ¤z2¤ylj>àURÅ¹ß½e`CêY!f#Â%H,4zÓ[â*¨7RTø |ÓÒ =óM{JPóOÿ[wSPTø ¾À7Ç!ë%eÖ3ÁË¾¥(ov#õ¨/RF´Ô$KÚ*ü`ñã¸ä¶ºý'mQzÚâË2tY= |
| --- | Minor | +¶øßîç³=o\)8ý)µ2Ýæ­ÓÍùa)ÜKÛ`â"KVÚÖ«K\ÍëJ8øpäq{²ã:qÜÁ,ºhã,Zu-ö«4}ÆMüºS:Hß°J¯paÓ!ñÍýY(¸;ÑPöî=ÐnZ¶¡ùBÝ¦AÐû/ïpVØ_ÝäÑûjE¬E¿N}©Ö¹»Ìvóæ3ç8&*Ú¢¯æ"8	%\KðPêq±L@m³õË|ª·³WNØª¨Üîþ¸b~!­êÿÛÅ Ñp ÔAÍü¸C±­ë&6'0qx~?dÔR£ß,Äìª¾cdâ»/¾]¼`S®YÑY *V\qè¦l |
| --- | Minor | \¾²¢db>i ´¬ÕÍSnF  ¹Æiçþv! |
| --- | Minor | ­ËãzËµÊS*Qç°G³°è)(q=¬0Ö½Uì¸Óº  #ûñÊ®+¯ ¤¿^(i¨d©óLáÐw³6m! |
| --- | Minor | ÛêKõOö¦Vþ¥¹Lrí·wUi¾=±)ÚåÇµe|Iûèº¼^^³£v¹Ð7ïÊÿâ­Är. £C·ãÌâv« _­tö¶¤ËnsÇ`{îX´QØ]lÜSÎýAÛÖRÏ´åYÒÄ§éÆ¢JG-¾£¼ã4JFaHz-7c½úZN2¥À¶rÛùæ;6N¸vó×XWØûOw6óm¶]ØkëÒÍ 6Jyã>àú|Æðªº}[Ôó-nãkZö¹Ãÿòö0d²Ñð÷®AÂ¤~ûÿú¼Sÿ endstream endobj 188 0 obj <</Filter/FlateDecode/Length 4670>> stream xÚÝ\YdÉU~çW ÀLÃÛHU]­±¦Í_ÀóÀoçØ×7»{0Ð­îª¼7gùÎqúáÄOÿòánsôçôü½Çú7§¿þ;~Âo4hyzózâmÊ:}¹1)­8½yùÍcÚâ?ö~Áÿc1Æ/øþ¯)Nmñwl¯ga¾Oáj)þôßVùm Ö6ç¿Á§Jß©O[Ëãoßüêô7§Nqqyú7qg\-höôá$eX¹­~wúæôë°|uâlsÌ1k=r@U~4«KY¡T UËÎÝ l©ÀÏ(Ûtm´Âr¤DuZS×Ï ø. ¾Ü½ |
| --- | Minor | ßçÇ³4` ããÙoNÁÍ"²{ x( |
| --- | Minor | ªDàÇ3Õóþx*è5x;ñ-bGi0Oç(»#Ò°Þ!6­íÞä§GöF Lfn)Vo¨0øÝW÷ó9ÚÍpPö¼Ú°ß^0 |þèÙ(½I£³y³3)&!%ÍàÉsËÌmO¸Lhÿõb@üÀ¤z2¤ylj>àURÅ¹ß½e`CêY!f#Â%H. 4zÓ[â*¨7RTø |ÓÒ =óM{JPóOÿ[wSPTø ¾À7Ç!ë%eÖ3ÁË¾¥(ov#õ¨/RF´Ô$KÚ*ü`ñã¸ä¶ºý'mQzÚâË2tY= |
| --- | Minor | +¶øßîç³=o\)8ý)µ2Ýæ­ÓÍùa)ÜKÛ`â"KVÚÖ«K\ÍëJ8øpäq{²ã:qÜÁ. ºhã. Zu-ö«4}ÆMüºS:Hß°J¯paÓ!ñÍýY(¸;ÑPöî=ÐnZ¶¡ùBÝ¦AÐû/ïpVØ_ÝäÑûjE¬E¿N}©Ö¹»Ìvóæ3ç8&*Ú¢¯æ"8	%\KðPêq±L@m³õË|ª·³WNØª¨Üîþ¸b~!­êÿÛÅ Ñp ÔAÍü¸C±­ë&6'0qx~?dÔR£ß. Äìª¾cdâ»/¾]¼`S®YÑY *V\qè¦l |
| --- | Minor | \¾²¢db>i ´¬ÕÍSnF  ¹Æiçþv! |
| --- | Minor | ­ËãzËµÊS*Qç°G³°è)(q=¬0Ö½Uì¸Óº  #ûñÊ®+¯ ¤¿^(i¨d©óLáÐw³6m!. |
| --- | Minor | Sentence exceeds complexity threshold, split for readability. Applying the split needs --strength moderate or higher. |
| --- | Minor | none (split proposal only; source not rewritten) |
| --- | Minor | none |
| --- | Minor | Check: NEEDS-LLM |
| --- | Minor | Flags:    not-assessed |
| --- | Minor | SENTENCE (Line 51, 708 words, 9 clauses)  [Script] |
| --- | Minor | [pÍÎ%w9»yç{êçe§4ºÏ:ÃºôÒ½°,ÌWL |
| --- | Minor | DÂãÖ ë×ÖJ+O!¢[ÂR÷)²1è/Âa þóåPsÆ³n²©­Ìûß9íàÏæýêMY5É×+Áðf{Y²]bMu|¿¾OÙ8¸Û[³)§¸C¹«{a)øh²©ùù$Í&I?-&Ù¯{C' Zw¹7úÛ»e A&&ùýjËÚÀo p Ü06ûÜàãíý.hü#3\`lÅáÃ ùÎ®ì¡ä1F©OáÃ®©¯^/+ì&½ä^Aâ,6*ÒÀ^îøi4·~~gàÒo©ÛH á6nÿ(½q@$¿¸'}÷ø< ¸QÒÿÊ÷ fû×{+îþ0*nÚÑÙQ©ÛþÄ×ÿö~)¬ê+¸ÑÝ&µÑÐ@^sIDÍ¥z°êÖ ©Bµaþõc\Vq@ZNqøªõW; ½ØÊÓ ¢&«óñõ%è6¢.¸áNõ÷s]ïÔêÞ°Cÿ¨RjÝÙ¬ï(ìFH­TA&X-RÝlTú m89¶B ÉL¸þ]-%r?æöËkOêç÷V0÷ýCÙü¾Eyv½v^èë:r¥¡ICqnêõøÿj	3	å{!ËmÏ×£ [CqÿSTØóÐÝ÷÷%¿&fà3lÙçÄÇiÜéÃ[|lhª§Um@MU'Ü0¥V.e?9È¸aeYZÓ¶´,(38AagajãöÄµU/  'XøýÒ¢³ö6ézþîÛïßÞ}x÷ôû¥Wþ¢NSªÊª»áªaXög®Ú¸+S«0XX¥øSMÌ©L²Å¤ÞÏMX¬Í¢á%PcKæÑÈ­×ÐF{ JB¿T/·Ðå0èê" ÅÜ6%ÈnÚ¤¡ÇiTëHãïEõw¬pÆ&sÎïBÌn/mð¥íÿT­áÙÛâ{¡óÄ­Ò7Æ÷R%Ï æúcì\X´pÀL7m/	$°¹¯¸Óµ-ÀÊ-:¨ÙÉôf[øl¾{áìÉRQ%äÉoÍF³;fD PJ |
| --- | Minor | ÊÿZ¥ÂÆðY}Ï¡±~^J vçÉ!gmê |
| --- | Minor | l*¡P¡¦¢@Á,x®Y©i"È 0ï\è|i\Ñ'A¿Dq£X7åTº\·ñú½¦â¶P^jx|ýh½Êý TØÎr7åîÝ¨o'û?®±ÍI£Íó!µ¼Ï²e´² {ó¤¤Ñ×B{ñÊ©Ý¬ÐÐøØ_ù·lVCð,'()u;æ3À<©U³^d´&Ü#ÜÉ3à¡:¶5CÉ?1!<½Ö½"è¸FøqI>¥Ó´síº\Ühb'\ÞfÕÏe6!QÔk§kÐÌ¥'iïbàúòþlÕkz×fd!ts?ÅLÈHñÑ¾×þ	Ì«:»°"æå¯ÚÚ´ºñ»yB½=7Z8áPØ->Ñï5	9¾(ÈÔHÜÀ~Êê¨7;ÕQ øY¾»ò&Ô®Oézme¥UæjÐôeb¨ý:< |
| --- | Minor | ËâLGÎªâò"©¦DO»á½¸ß% X½	d#1! ì¿éøxÞÎHgÏ§:t².VùØÁ-HBT·öæÆµ¡ØLvåïùúÐÆlÜÙÙØ!K·ÿ¶EctdÃüËêÈl>EûAxF××w= ÌþôiÝlRnvQ\ýFÃººñ	rgUÔM@Ouâñ ´¬N÷ad4Dàxöû'§ÉZè kfóf\ |
| --- | Minor | $«ãÞÏ¿vÇÆ=!ßæCºÉ£équ,pgC@E ØNZ¶®7ðîêÉówc¾~)' |
| --- | Minor | ´È÷òA¯¿y RBí9¹mSÆéêçÑ÷Äb·$ (i MÒ1äüÙøÝ{µSè%uò\CG­}³ñ¤§ùÆü  ªóé¯õD#Äkó<³Ã´wü	Xý\ºþd+ýz'æZy¬ßýûûõ$ú ¯õ×ÂªBC	4mõìÊ>©ßòþJ~dN)j<p¯WäKËM~³ÃF6Öyà/kn=/âßèÏ}#øf¬]ë¤ËJR«pâ |
| --- | Minor | ©?hÇBQ;ÌwA(å3/5·zµ¹ÚÉæRCop.Å(B>hã/­`@[èêã×(d)ÎjR©¬buº>þ}Û°õá OB]2jäëyÝ¤_²ê;=Õõvt0>õARËËk1¢reèê £ªÀÀù®Gá¯x­©û(WÔ |
| --- | Minor | ¯2Ô1&ù6ëR'*'Åd,]nUI¿©rLêãÞÚrwAþï¡Pã2¡n2Ìn<¶_U@j«H¦SÂ\Ï ÐI8´®¤¤V9-0Ìdc\HøÑzÆÅÙ2ã+@ ÚRòEúmÒOWÞt$Ãã/èé6øÉU!Ý@ÍÚ[×¾x(ÖÓd@úBBØÀ)soÏ |
| --- | Minor | ¬ÉhÑe[Ó 6 °4.)®W{Æ­*úúV(9ók¬6Ê:JJæg­øC |
| --- | Minor | PHxø&]çâ5¢: ªËhIÉz |
| --- | Minor | G§ýHc?/IÐ^ÄÑÃ!.ÑÁ7|8[(÷ê¡º¼eûk}BÇÑðtùD`ÊIuob7çøÅÐ!OÕÄ<%I%6ëä/q¬rå¹sÅÍÞÁ=Üx&Ü3¼@G~¿~@¿F÷iV¤%«t,ûy (:ö |
| --- | Minor | ¨ÙCydc!¥Êî]ô~È	{A®<Å*Ç) ,¾*ÝÏDþVË[¹`a¹QÈF¶sáÕ÷8&Ü¸vIz#F~ª~©rù|FH-ü}Nþ&·n{/ +:ì5d@H&ø¦÷ÑsOäJy+ ý=ºòc±ÅHý·úrV~W·W9;ÓA³U¨MÔè¬ä²ö5q-5ÀÎpþRá?eÛË×]JÞ«GÃqÆ_aù4¥/Ç ]å'©7¶OjÝ!]UßaxíÁ¡Õ±^xBlP³^I`3Z¦-XÞÝÅÝ Lºá¬ähxWÎÈF¥¬üHÞ»ßÃjKÉæ]>£6Í¬ñâ6)_E°ãá Ó-qG²³ËËp&#Yªj&KÐÕÂIàTÊó#Q9å|úNS áS@òõKïÇ®IXí¢s¼`QKG 5/w­Ze3)½§?þ0èóª_. |
| --- | Minor | [pÍÎ%w9»yç{êçe§4ºÏ:ÃºôÒ½°. ÌWL |
| --- | Minor | DÂãÖ ë×ÖJ+O!¢[ÂR÷)²1è/Âa þóåPsÆ³n²©­Ìûß9íàÏæýêMY5É×+Áðf{Y²]bMu|¿¾OÙ8¸Û[³)§¸C¹«{a)øh²©ùù$Í&I?-&Ù¯{C' Zw¹7úÛ»e A&&ùýjËÚÀo p Ü06ûÜàãíý.hü#3\`lÅáÃ ùÎ®ì¡ä1F©OáÃ®©¯^/+ì&½ä^Aâ. 6*ÒÀ^îøi4·~~gàÒo©ÛH á6nÿ(½q@$¿¸'}÷ø< ¸QÒÿÊ÷ fû×{+îþ0*nÚÑÙQ©ÛþÄ×ÿö~)¬ê+¸ÑÝ&µÑÐ@^sIDÍ¥z°êÖ ©Bµaþõc\Vq@ZNqøªõW; ½ØÊÓ ¢&«óñõ%è6¢.¸áNõ÷s]ïÔêÞ°Cÿ¨RjÝÙ¬ï(ìFH­TA&X-RÝlTú m89¶B ÉL¸þ]-%r?æöËkOêç÷V0÷ýCÙü¾Eyv½v^èë:r¥¡ICqnêõøÿj	3	å{!ËmÏ×£ [CqÿSTØóÐÝ÷÷%¿&fà3lÙçÄÇiÜéÃ[|lhª§Um@MU'Ü0¥V.e?9È¸aeYZÓ¶´. (38AagajãöÄµU/  'XøýÒ¢³ö6ézþîÛïßÞ}x÷ôû¥Wþ¢NSªÊª»áªaXög®Ú¸+S«0XX¥øSMÌ©L²Å¤ÞÏMX¬Í¢á%PcKæÑÈ­×ÐF{ JB¿T/·Ðå0èê" ÅÜ6%ÈnÚ¤¡ÇiTëHãïEõw¬pÆ&sÎïBÌn/mð¥íÿT­áÙÛâ{¡óÄ­Ò7Æ÷R%Ï æúcì\X´pÀL7m/	$°¹¯¸Óµ-ÀÊ-:¨ÙÉôf[øl¾{áìÉRQ%äÉoÍF³;fD PJ |
| --- | Minor | ÊÿZ¥ÂÆðY}Ï¡±~^J vçÉ!gmê |
| --- | Minor | l*¡P¡¦¢@Á. x®Y©i"È 0ï\è|i\Ñ'A¿Dq£X7åTº\·ñú½¦â¶P^jx|ýh½Êý TØÎr7åîÝ¨o'û?®±ÍI£Íó!µ¼Ï²e´² {ó¤¤Ñ×B{ñÊ©Ý¬ÐÐøØ_ù·lVCð. '()u;æ3À<©U³^d´&Ü#ÜÉ3à¡:¶5CÉ?1!<½Ö½"è¸FøqI>¥Ó´síº\Ühb'\ÞfÕÏe6!QÔk§kÐÌ¥'iïbàúòþlÕkz×fd!ts?ÅLÈHñÑ¾×þ	Ì«:»°"æå¯ÚÚ´ºñ»yB½=7Z8áPØ->Ñï5	9¾(ÈÔHÜÀ~Êê¨7;ÕQ øY¾»ò&Ô®Oézme¥UæjÐôeb¨ý:< |
| --- | Minor | ËâLGÎªâò"©¦DO»á½¸ß% X½	d#1! ì¿éøxÞÎHgÏ§:t².VùØÁ-HBT·öæÆµ¡ØLvåïùúÐÆlÜÙÙØ!K·ÿ¶EctdÃüËêÈl>EûAxF××w= ÌþôiÝlRnvQ\ýFÃººñ	rgUÔM@Ouâñ ´¬N÷ad4Dàxöû'§ÉZè kfóf\ |
| --- | Minor | $«ãÞÏ¿vÇÆ=!ßæCºÉ£équ. pgC@E ØNZ¶®7ðîêÉówc¾~)' |
| --- | Minor | ´È÷òA¯¿y RBí9¹mSÆéêçÑ÷Äb·$ (i MÒ1äüÙøÝ{µSè%uò\CG­}³ñ¤§ùÆü  ªóé¯õD#Äkó<³Ã´wü	Xý\ºþd+ýz'æZy¬ßýûûõ$ú ¯õ×ÂªBC	4mõìÊ>©ßòþJ~dN)j<p¯WäKËM~³ÃF6Öyà/kn=/âßèÏ}#øf¬]ë¤ËJR«pâ |
| --- | Minor | ©?hÇBQ;ÌwA(å3/5·zµ¹ÚÉæRCop.Å(B>hã/­`@[èêã×(d)ÎjR©¬buº>þ}Û°õá OB]2jäëyÝ¤_²ê;=Õõvt0>õARËËk1¢reèê £ªÀÀù®Gá¯x­©û(WÔ |
| --- | Minor | ¯2Ô1&ù6ëR'*'Åd. ]nUI¿©rLêãÞÚrwAþï¡Pã2¡n2Ìn<¶_U@j«H¦SÂ\Ï ÐI8´®¤¤V9-0Ìdc\HøÑzÆÅÙ2ã+@ ÚRòEúmÒOWÞt$Ãã/èé6øÉU!Ý@ÍÚ[×¾x(ÖÓd@úBBØÀ)soÏ |
| --- | Minor | ¬ÉhÑe[Ó 6 °4.)®W{Æ­*úúV(9ók¬6Ê:JJæg­øC |
| --- | Minor | PHxø&]çâ5¢: ªËhIÉz |
| --- | Minor | G§ýHc?/IÐ^ÄÑÃ!.ÑÁ7|8[(÷ê¡º¼eûk}BÇÑðtùD`ÊIuob7çøÅÐ!OÕÄ<%I%6ëä/q¬rå¹sÅÍÞÁ=Üx&Ü3¼@G~¿~@¿F÷iV¤%«t. ûy (:ö |
| --- | Minor | ¨ÙCydc!¥Êî]ô~È	{A®<Å*Ç) . ¾*ÝÏDþVË[¹`a¹QÈF¶sáÕ÷8&Ü¸vIz#F~ª~©rù|FH-ü}Nþ&·n{/ +:ì5d@H&ø¦÷ÑsOäJy+ ý=ºòc±ÅHý·úrV~W·W9;ÓA³U¨MÔè¬ä²ö5q-5ÀÎpþRá?eÛË×]JÞ«GÃqÆ_aù4¥/Ç ]å'©7¶OjÝ!]UßaxíÁ¡Õ±^xBlP³^I`3Z¦-XÞÝÅÝ Lºá¬ähxWÎÈF¥¬üHÞ»ßÃjKÉæ]>£6Í¬ñâ6)_E°ãá Ó-qG²³ËËp&#Yªj&KÐÕÂIàTÊó#Q9å|úNS áS@òõKïÇ®IXí¢s¼`QKG 5/w­Ze3)½§?þ0èóª_.. |
| --- | Minor | Sentence exceeds complexity threshold, split for readability. Applying the split needs --strength moderate or higher. |
| --- | Minor | none (split proposal only; source not rewritten) |
| --- | Minor | none |
| --- | Minor | Check: NEEDS-LLM |
| --- | Minor | Flags:    not-assessed |
| --- | Minor | SENTENCE (Line 51, 388 words, 9 clauses)  [Script] |
| --- | Minor | cþl p0É¹p»<ï3è4,?p­HûßÖÌÁúI`'¯+ØÕb¬}9_¯ >/±g9ÿÇµXß ´ Ç2]¶ «þ@ÔKQä÷LkëÕFN®é¨_ZYÝÈ:¡#ÕÊÚ)ÎÇtF(xòÛ¢!j.8èêJZýg-ØfQ¹ècQo) nòæÂõ¹BåZ«æÆÝ3àÚPznÎ³¦ºò!Më×öß=Á,% endstream endobj 194 0 obj <</Filter/FlateDecode/Length 4646>> stream xÚí\K·¾çWÌ%À,éU|Z«ìDà$@+'Ë	v4ZA¶eHvþõ)M6ÉîêévebÁØÝ6,Öã«wïvr'èÜYØYéþÛ½xC½¢ÿî>¶ûÃå¾1`ÔîÙÝ@Ñ _RwÏN__¡ô |
| --- | Minor | ©åÍ7Ï¾Ø=y¶{·¬·BªÝÏ;iÇÉô0ÜîÍN©ôJW}úýî«Ýé½z'ÅàÎ7OS@¬ß,ôv'ÃÛ0þúéé³;úýxs@4ÒãÚÂ©­4:ihÏiJão	S¿¸ pwOvÒ§UX¥ÓJà½ãËéS4	,}fE"Zø</[ÂVÂSp=m¡Ìi\Ø®:åO-´8ÅU#äz?ÞÊKÃªCOt­Ïq°4Ì·çU>Ýr^ í¬¶#yô]z·>¦%*¨ó!²!ý¬Õ¸ |
| --- | Minor | ¢eþ¥ÙÍÑ­Ü ^)æØÿýjùUnP.l-¿	¥ ¿aZ1Ü%òÇc+lí4 m­Ïoûó6údG¥× ?ÃkÃQø+2ÙOäS ¢ã>efÃA ÀL¯ybÐ¡}ãYT2A2/ôi®@$5ò8G5X'U¡TÌÌ`xz(q9=ìËõ`¶¤ÚÈéÈíø6 Å? |
| --- | Minor | Gç_r0Î(®û¿þ[Í*¦wM£ÓÃø¢Á @éHü<`<Gbæåå$J+ÐÓhn½FYoâzÑ`4û7·ÿål 5´«FÕE¯jØ%kRÃ± |
| --- | Minor | 	Òe¢~Á³%¥åT¶ÇÀ³§#RB6çyÞ"w¦ïÂr£èÓSDéuîèèÍ ÀÀñ5©­H_ÂÖp	[/Oè§Å8nÿæõOoÿýòÄÌªìÊå5!3kÐ¹ÄFYÿÉìù@ªÜÄ yYÎYöÓÛØbð!Pd±øvf>}ÕzÑbÇé¼QHBJ¡µ½ ]È8 cèÎ'P {>wÖYS(%ÄKùðGæ#¸:x(k6±ÝsÚsAi[ET ¥À3ûTù×VDÚèça¾$ÝDHú±?	äÅÓ=-aIBRÕ\#öT*®W# ±do(]Á¾ ÷9m#9Ð z |
| --- | Minor | D`M2KÞµïæµÕFÛæS7ýãÖ=ÕÈg\5ù<:D¨/4©h=£¾®)ÝCVX3é%´gl«¤wÕÈ:â#xÊbëÁÚ?{ d8©ñ®:~ ùYs\a(ÂÞKÈòús^µmì+	5m]¶öõ5³C3()(cw	m¯TVeÿ1óâvÔ·s6é:!ÈÀBÙMÐÈ\1 ¤-eÙÛ3UC@ËYD_³öÑjEw\1{j'ûvbÑ2kÞÓ$,Ù]LneAÃS¿U&	[òlòd*XCJ°XÌöáô·ÌÕ j@ËAK-aî¡ô¬Ú )í÷o·óþßy¡"Û0ÿ;Öüi¯	Î¼óßþøêê ¨k»´ÃMË?ËM¯iö=Yd¡uëèv{LÑÂ×¼Û¡mC9ókl75þ¾Í3I)v*q·ò.éZ¸´ÔûGÌËÉ¶hCP¿~âñòÑÑ>c¸,	 éÞ_ |
| --- | Minor | ?âcixaØh2ç &j,f3~ð. |
| --- | Minor | cþl p0É¹p»<ï3è4. ?p­HûßÖÌÁúI`'¯+ØÕb¬}9_¯ >/±g9ÿÇµXß ´ Ç2]¶ «þ@ÔKQä÷LkëÕFN®é¨_ZYÝÈ:¡#ÕÊÚ)ÎÇtF(xòÛ¢!j.8èêJZýg-ØfQ¹ècQo) nòæÂõ¹BåZ«æÆÝ3àÚPznÎ³¦ºò!Më×öß=Á. % endstream endobj 194 0 obj <</Filter/FlateDecode/Length 4646>> stream xÚí\K·¾çWÌ%À. éU|Z«ìDà$@+'Ë	v4ZA¶eHvþõ)M6ÉîêévebÁØÝ6. Öã«wïvr'èÜYØYéþÛ½xC½¢ÿî>¶ûÃå¾1`ÔîÙÝ@Ñ _RwÏN__¡ô |
| --- | Minor | ©åÍ7Ï¾Ø=y¶{·¬·BªÝÏ;iÇÉô0ÜîÍN©ôJW}úýî«Ýé½z'ÅàÎ7OS@¬ß. ôv'ÃÛ0þúéé³;úýxs@4ÒãÚÂ©­4:ihÏiJão	S¿¸ pwOvÒ§UX¥ÓJà½ãËéS4. }fE"Zø</[ÂVÂSp=m¡Ìi\Ø®:åO-´8ÅU#äz?ÞÊKÃªCOt­Ïq°4Ì·çU>Ýr^ í¬¶#yô]z·>¦%*¨ó!²!ý¬Õ¸ |
| --- | Minor | ¢eþ¥ÙÍÑ­Ü ^)æØÿýjùUnP.l-¿	¥ ¿aZ1Ü%òÇc+lí4 m­Ïoûó6údG¥× ?ÃkÃQø+2ÙOäS ¢ã>efÃA ÀL¯ybÐ¡}ãYT2A2/ôi®@$5ò8G5X'U¡TÌÌ`xz(q9=ìËõ`¶¤ÚÈéÈíø6 Å? |
| --- | Minor | Gç_r0Î(®û¿þ[Í*¦wM£ÓÃø¢Á @éHü<`<Gbæåå$J+ÐÓhn½FYoâzÑ`4û7·ÿål 5´«FÕE¯jØ%kRÃ± |
| --- | Minor | 	Òe¢~Á³%¥åT¶ÇÀ³§#RB6çyÞ"w¦ïÂr£èÓSDéuîèèÍ ÀÀñ5©­H_ÂÖp	[/Oè§Å8nÿæõOoÿýòÄÌªìÊå5!3kÐ¹ÄFYÿÉìù@ªÜÄ yYÎYöÓÛØbð!Pd±øvf>}ÕzÑbÇé¼QHBJ¡µ½ ]È8 cèÎ'P {>wÖYS(%ÄKùðGæ#¸:x(k6±ÝsÚsAi[ET ¥À3ûTù×VDÚèça¾$ÝDHú±?	äÅÓ=-aIBRÕ\#öT*®W# ±do(]Á¾ ÷9m#9Ð z |
| --- | Minor | D`M2KÞµïæµÕFÛæS7ýãÖ=ÕÈg\5ù<:D¨/4©h=£¾®)ÝCVX3é%´gl«¤wÕÈ:â#xÊbëÁÚ?{ d8©ñ®:~ ùYs\a(ÂÞKÈòús^µmì+	5m]¶öõ5³C3()(cw	m¯TVeÿ1óâvÔ·s6é:!ÈÀBÙMÐÈ\1 ¤-eÙÛ3UC@ËYD_³öÑjEw\1{j'ûvbÑ2kÞÓ$. Ù]LneAÃS¿U&	[òlòd*XCJ°XÌöáô·ÌÕ j@ËAK-aî¡ô¬Ú )í÷o·óþßy¡"Û0ÿ;Öüi¯	Î¼óßþøêê ¨k»´ÃMË?ËM¯iö=Yd¡uëèv{LÑÂ×¼Û¡mC9ókl75þ¾Í3I)v*q·ò.éZ¸´ÔûGÌËÉ¶hCP¿~âñòÑÑ>c¸. 	 éÞ_ |
| --- | Minor | ?âcixaØh2ç &j. f3~ð.. |
| --- | Minor | Sentence exceeds complexity threshold, split for readability. Applying the split needs --strength moderate or higher. |
| --- | Minor | none (split proposal only; source not rewritten) |
| --- | Minor | none |
| --- | Minor | Check: NEEDS-LLM |
| --- | Minor | Flags:    not-assessed |
| --- | Minor | SENTENCE (Line 51, 898 words, 13 clauses)  [Script] |
| --- | Minor | *<8ÎìÄdl |
| --- | Minor | ]*v $ ÎP¯J­ ÕW?0ü!Ck 1¼ÁHOòµE¬ê±;+Z¬tª á%MiXv%N9Òë~¨C0%FQ4(öoOsK/*zÌV:âænEµ`eÿ!"É¶6]wû?þõpF­ÁOÓü¡CeG½ï¡o7_./Ä,jÀ%¡Î{tPèvÍð°ÃÉd÷fÅø¤Ïjý9TÜìK­î.Ð ª÷O%]ÙôìÔ\øZ¢î*óÆ+Î*·¢@F³ÒZe½,Gf EgyÔïc¿¾ B½CyÿòôúalEæHgÄÞ"Ã kÖ3ÁI¹ cve:W¼«S ­+Ï¹paÙnâ;I÷[0yØõ6Þ¼ÏNÿv£ÒÍùäÃZTûh ¡	¨dÂq¢gï3<	Ïù¨¢0NÍx^=Ï«àyÎ±«¼ÉµS|Êj?MêÔËÄØÚ\Æ%6ØðÏÌÒåçf±2ÄíçôjYhb¯ P+çáBûåãòÛæY ø¾Àß§Ü²D( (^Ú©PñaÒ×ÂCHÐ¤°3q	q_ë×Ô|p|§HßO¬tKnv>ëÆõ§×ä:p2z ýF3|d!¼Kûã §Î»uºmÈjU)èäLIñ^SÔ,&³f0ØÁ¢[Ê	hØÎ@5x@¨kPmÇæ¤·%'½1 ýë(KF]æWÜ||¿Bs,RuùÙ¯³s[ÂFCî+n´¸®ËOú´e(¢Ã*ãÄ¹ÖjÈæ>M£Bç^ ©³)¬¿/êØÿ¹ÈAÚPÍäåÅæKÕTc*°è>fHãlÑ¼ÙãUz1gÆ(ß±Kû2÷%ÆPzIPÊ/ø2%)r®ehAB^éÅã¼Ý~ß1gîà/?Ê\¾	.¿ËÉd;±´©+Û¤¬Âtè¸Xd@ËI/c"k¹e%í,¸åññ÷e.@o£àh1FA.½ Þ5"½IÂ_W ØÂ½#¤þ-®SU«Nå¢AwiØý¼óHöÂ>;¤%V»7ô<±¸IøéÓªbtV4MBâó e'Þw¬-¨1úD>¿zÎ.Â-¬V×ø,Ù¨Ú9(J;³½f)¢z6Alò/­Ësî¬OìHê7°(îap> ;¨úp¬*ÅÕo_íb o~½ø.i§UdN¬ÅKÝTöP;¶¹c"L¨ßÎp­TûdÑù¨öd¦Ý¼Ä&ÚY½!F*Å.¯2YGËÐy/¾ýSîäÂo¡×vúN@«þñÇÏz¦ÃwÎ§×lJÑaábg~0%ÔðK/k²nµ |
| --- | Minor | ubê·>buXHu>h--¬ÕÒn[d8"/¬cÉéa²éÄ#wò¬6² |
| --- | Minor | ×èá4¨cÅ%àr?A©CH=ö_+n¼ºWÇÿc¼Õ·«+®¾R+èjðÛ » °!ôLl| ¤nS¿¡lÑc>¶tü] ÁbCäÏ8îÁsP÷¾+Îì;AÂXýy{$9æV50pÖÊÕ	êPP%ô6Áºy3­ AÖr ªæL®µUÓh¬ìz[ËÇU¨ÂsÍ­}F3UË)þ=`éI,J)úMø8 ¬Êí¸ø\ÎxäJ«ªê®KªËÓ¾ ¥Æ6(6ÛâÒ)×)Î4sSõw:ÒsZ¶Õh r8»¼¡å ñ |
| --- | Minor | Ê.¿ÇÞ4§>ÛÇ½ Sâ´@¹A/úäJ^äqÊc©S3:U©Â2zÙBÃ,¯ÎÝ¶IÊªF½ëç5¥^;°Ê'|óµSDâC=d)ºplQZÊxÈîsÑõ$#ÐL^ÕgÙò<C±¿pLëvÍ½¬êKG1S±÷C{I å:HÌÌXT1Öèz¶ÑÆ^·}äÿV½ÏËÕé`ã¦92rIsÄä]îO;M5"é[À)}§ã- Æg«KÌS¿ÉòT»«÷]®¼,îÝ:i L`³KÌ_Pò\3í2ÂIã®ªîò±5¶´v÷Å]u*téº[Q¾nÅStþ×úº5ñåÌ¾ñ¾GÎÏÿ2×5ßÙQEåóª²æs¬ |
| --- | Minor | ]Éãô L¬ôQ¤j­©"{ýA/ |
| --- | Minor | 4»µ©÷Ö`l7CöiMoew\è_Ót¹ôù½*éïxæÁ 0ja«yP'Ü*blCÉ%Ü/9ï*Vo«¼^;¶Ú/qDÎ/ø°×ZñjÔä'ëÒKE8ÆFN²ÓEH(+EKKÌ¯okÇiÕÈ¼\éZWzvkmC¦«F/þzCQãÆY34/,íôñ6-B»)@3ê 8ÀÍ RÕõ/kp*3bogÂX[cøÅ®ãñj¬czc»qïb÷ã·åN8ksÇd	Zà8Qíâ8Ý$Ô¹7Åþ+/ü?él·M£V{ªÉê^ºÏ,Òö5RE{Ô0x©aæÃæÊÍôÐHo%¯ë;³ÆSRp}®ÏÐ¡öC"þ&ïÐ«wpóÓH¥~~[KÒèbi|ÚÙíA :ë>	oB^Ïùk5 iíµ¢RGk*	t~Cu%_ 9ÖsÊ·b9ïÁñt¥ð3v¬î½+á)µV ¤Æ@'¤«Ø!Üé¼¬P·Aí¼]«âËZ9Xaì`ÔUu´vPTn¼mÎMÍ-*¨Ü»æ^ ÎþúÁÈÐÃNÜß3Çj@2m7V¦úìZ»·cHÜ÷nëøÉ^Aà-[;>j2 :;#Ê÷9Ä>V'72ÍwA'êaMXI(w}¢[PÁ dÙÓò6e0h¢IN¿¿=^UF(e^ÉK>Îu¡ªâj+TYñAÐFþü[Þ{·åýÈm Æ½ô;ÉíA´êvdÒU"àâ%Å.Ö¿õ¾ø¿ûø¬f endstream endobj 207 0 obj <</Filter/FlateDecode/Length 4896>> stream xÚå\Il7Þó+jè*cÏPébX Þ.É"~X øõÇ>öµ«ªIHôÔÝ·l_ÛgúÎT§oNê ÔæOË¨6ÒèPß?Á§ÖßÓ¦Ö×/>ü&í^QFB:À9Zá¬Vút¶ZgMlGx	?=¼@zUø²`.}Ã´ñEé°i¤»ÐSú+<1´©.ÂMþòC½èi«Êka¬§3D@:O;½3/h¡ð5á0Q}E7¶h/e{ikét¼D/Ð/ç|é¬4×³@dx£ÓáÓX]~÷|i­y®ä[i+¬Ðî5°ÀÍÓ"Z'Õáô6]½¹=@@y8Üy¬´¯ôsegóÓä'¥rð	om»?ùU¨ Z _¬ÌDzQ |
| --- | Minor | +Ã80ÎZ_&>ýë¹ó'/¢ Çã(»Ò, ÓNÛ<öëçµPöÄÆ&Äë7²\ 2Å¹ÓÓPÅÀõ1¯ù3ÈR®Ë§àÀt@GyGO¬.ìÞlMåKÚÉRúYùåqQ%áEÚÅàêIu¼=Ñ#Q)Áaâñ2á"Àx©(/&l«tQï+´±HÐyßIÌÇÛQÓhìq2é÷"$G»b7Ðºìrßn¤²IzE×	EÊì¤ì³©×åPYãÊ/¥t¹ã?.ÞWæÔÕèS3½®óZô)iÏ¾V²,ø÷µ²ÌTæ"=öWxïÝM!gê¦ûÜd|ó¾¯uý×n4 Ì»t|±Fo¤ØÌ¤G¥TÍö¹÷¼ÖgÁ)[þm£ÖPâQ¡iXRK Ýw:oºs ×cðHãIë8F¾^¾7n>³´ÊúyÊÇKê 3C eéñe®._»Y) :Úº.Ùâ¬¬J*B¤AÚ7dojmn× Â7dH´¾­i¤pá0É& 5·&å¯×z®HOÒ |
| --- | Minor | ¦LÿH;6»GôûcwñURfVÐy|²RÝBµUäT»Ó&\Ò|; |
| --- | Minor | ²Òxªö×{X©¿xÐ|U6h»öºblëLTN%;ÑêRè8C<¢­Ì:SÍ @3$éâübü°UcÔ'¦£/Z¯HWª¯EMpÅå;V¼õøoBý%käQ÷£#ýfmÒy/Z]z:¯µÑÓ8.³ûÓW)o.+xÅd	/AÚüWÇÆ|<SÛ¨aÄÞxüý¾VTìúZÃóë&È ¨^h/H5Úºa0	¡ÕYÛÂÃÝÚ'þ÷U¼ÃÒ¬*V] ·ØÌéI!ªN·Þª. |
| --- | Minor | *<8ÎìÄdl |
| --- | Minor | ]*v $ ÎP¯J­ ÕW?0ü!Ck 1¼ÁHOòµE¬ê±;+Z¬tª á%MiXv%N9Òë~¨C0%FQ4(öoOsK/*zÌV:âænEµ`eÿ!"É¶6]wû?þõpF­ÁOÓü¡CeG½ï¡o7_./Ä. jÀ%¡Î{tPèvÍð°ÃÉd÷fÅø¤Ïjý9TÜìK­î.Ð ª÷O%]ÙôìÔ\øZ¢î*óÆ+Î*·¢@F³ÒZe½. Gf EgyÔïc¿¾ B½CyÿòôúalEæHgÄÞ"Ã kÖ3ÁI¹ cve:W¼«S ­+Ï¹paÙnâ;I÷[0yØõ6Þ¼ÏNÿv£ÒÍùäÃZTûh ¡	¨dÂq¢gï3<	Ïù¨¢0NÍx^=Ï«àyÎ±«¼ÉµS|Êj?MêÔËÄØÚ\Æ%6ØðÏÌÒåçf±2ÄíçôjYhb¯ P+çáBûåãòÛæY ø¾Àß§Ü²D( (^Ú©PñaÒ×ÂCHÐ¤°3q	q_ë×Ô|p|§HßO¬tKnv>ëÆõ§×ä:p2z ýF3|d!¼Kûã §Î»uºmÈjU)èäLIñ^SÔ. &³f0ØÁ¢[Ê	hØÎ@5x@¨kPmÇæ¤·%'½1 ýë(KF]æWÜ||¿Bs. RuùÙ¯³s[ÂFCî+n´¸®ËOú´e(¢Ã*ãÄ¹ÖjÈæ>M£Bç^ ©³)¬¿/êØÿ¹ÈAÚPÍäåÅæKÕTc*°è>fHãlÑ¼ÙãUz1gÆ(ß±Kû2÷%ÆPzIPÊ/ø2%)r®ehAB^éÅã¼Ý~ß1gîà/?Ê\¾	.¿ËÉd;±´©+Û¤¬Âtè¸Xd@ËI/c"k¹e%í. ¸åññ÷e.@o£àh1FA.½ Þ5"½IÂ_W ØÂ½#¤þ-®SU«Nå¢AwiØý¼óHöÂ>;¤%V»7ô<±¸IøéÓªbtV4MBâó e'Þw¬-¨1úD>¿zÎ.Â-¬V×ø. Ù¨Ú9(J;³½f)¢z6Alò/­Ësî¬OìHê7°(îap> ;¨úp¬*ÅÕo_íb o~½ø.i§UdN¬ÅKÝTöP;¶¹c"L¨ßÎp­TûdÑù¨öd¦Ý¼Ä&ÚY½!F*Å.¯2YGËÐy/¾ýSîäÂo¡×vúN@«þñÇÏz¦ÃwÎ§×lJÑaábg~0%ÔðK/k²nµ |
| --- | Minor | ubê·>buXHu>h--¬ÕÒn[d8"/¬cÉéa²éÄ#wò¬6² |
| --- | Minor | ×èá4¨cÅ%àr?A©CH=ö_+n¼ºWÇÿc¼Õ·«+®¾R+èjðÛ » °!ôLl| ¤nS¿¡lÑc>¶tü] ÁbCäÏ8îÁsP÷¾+Îì;AÂXýy{$9æV50pÖÊÕ	êPP%ô6Áºy3­ AÖr ªæL®µUÓh¬ìz[ËÇU¨ÂsÍ­}F3UË)þ=`éI. J)úMø8 ¬Êí¸ø\ÎxäJ«ªê®KªËÓ¾ ¥Æ6(6ÛâÒ)×)Î4sSõw:ÒsZ¶Õh r8»¼¡å ñ |
| --- | Minor | Ê.¿ÇÞ4§>ÛÇ½ Sâ´@¹A/úäJ^äqÊc©S3:U©Â2zÙBÃ. ¯ÎÝ¶IÊªF½ëç5¥^;°Ê'|óµSDâC=d)ºplQZÊxÈîsÑõ$#ÐL^ÕgÙò<C±¿pLëvÍ½¬êKG1S±÷C{I å:HÌÌXT1Öèz¶ÑÆ^·}äÿV½ÏËÕé`ã¦92rIsÄä]îO;M5"é[À)}§ã- Æg«KÌS¿ÉòT»«÷]®¼. îÝ:i L`³KÌ_Pò\3í2ÂIã®ªîò±5¶´v÷Å]u*téº[Q¾nÅStþ×úº5ñåÌ¾ñ¾GÎÏÿ2×5ßÙQEåóª²æs¬ |
| --- | Minor | ]Éãô L¬ôQ¤j­©"{ýA/ |
| --- | Minor | 4»µ©÷Ö`l7CöiMoew\è_Ót¹ôù½*éïxæÁ 0ja«yP'Ü*blCÉ%Ü/9ï*Vo«¼^;¶Ú/qDÎ/ø°×ZñjÔä'ëÒKE8ÆFN²ÓEH(+EKKÌ¯okÇiÕÈ¼\éZWzvkmC¦«F/þzCQãÆY34/. íôñ6-B»)@3ê 8ÀÍ RÕõ/kp*3bogÂX[cøÅ®ãñj¬czc»qïb÷ã·åN8ksÇd	Zà8Qíâ8Ý$Ô¹7Åþ+/ü?él·M£V{ªÉê^ºÏ. Òö5RE{Ô0x©aæÃæÊÍôÐHo%¯ë;³ÆSRp}®ÏÐ¡öC"þ&ïÐ«wpóÓH¥~~[KÒèbi|ÚÙíA :ë>	oB^Ïùk5 iíµ¢RGk*	t~Cu%_ 9ÖsÊ·b9ïÁñt¥ð3v¬î½+á)µV ¤Æ@'¤«Ø!Üé¼¬P·Aí¼]«âËZ9Xaì`ÔUu´vPTn¼mÎMÍ-*¨Ü»æ^ ÎþúÁÈÐÃNÜß3Çj@2m7V¦úìZ»·cHÜ÷nëøÉ^Aà-[;>j2 :;#Ê÷9Ä>V'72ÍwA'êaMXI(w}¢[PÁ dÙÓò6e0h¢IN¿¿=^UF(e^ÉK>Îu¡ªâj+TYñAÐFþü[Þ{·åýÈm Æ½ô;ÉíA´êvdÒU"àâ%Å.Ö¿õ¾ø¿ûø¬f endstream endobj 207 0 obj <</Filter/FlateDecode/Length 4896>> stream xÚå\Il7Þó+jè*cÏPébX Þ.É"~X øõÇ>öµ«ªIHôÔÝ·l_ÛgúÎT§oNê ÔæOË¨6ÒèPß?Á§ÖßÓ¦Ö×/>ü&í^QFB:À9Zá¬Vút¶ZgMlGx	?=¼@zUø²`.}Ã´ñEé°i¤»ÐSú+<1´©.ÂMþòC½èi«Êka¬§3D@:O;½3/h¡ð5á0Q}E7¶h/e{ikét¼D/Ð/ç|é¬4×³@dx£ÓáÓX]~÷|i­y®ä[i+¬Ðî5°ÀÍÓ"Z'Õáô6]½¹=@@y8Üy¬´¯ôsegóÓä'¥rð	om»?ùU¨ Z _¬ÌDzQ |
| --- | Minor | +Ã80ÎZ_&>ýë¹ó'/¢ Çã(»Ò. ÓNÛ<öëçµPöÄÆ&Äë7²\ 2Å¹ÓÓPÅÀõ1¯ù3ÈR®Ë§àÀt@GyGO¬.ìÞlMåKÚÉRúYùåqQ%áEÚÅàêIu¼=Ñ#Q)Áaâñ2á"Àx©(/&l«tQï+´±HÐyßIÌÇÛQÓhìq2é÷"$G»b7Ðºìrßn¤²IzE×	EÊì¤ì³©×åPYãÊ/¥t¹ã?.ÞWæÔÕèS3½®óZô)iÏ¾V². ø÷µ²ÌTæ"=öWxïÝM!gê¦ûÜd|ó¾¯uý×n4 Ì»t|±Fo¤ØÌ¤G¥TÍö¹÷¼ÖgÁ)[þm£ÖPâQ¡iXRK Ýw:oºs ×cðHãIë8F¾^¾7n>³´ÊúyÊÇKê 3C eéñe®._»Y) :Úº.Ùâ¬¬J*B¤AÚ7dojmn× Â7dH´¾­i¤pá0É& 5·&å¯×z®HOÒ |
| --- | Minor | ¦LÿH;6»GôûcwñURfVÐy|²RÝBµUäT»Ó&\Ò|; |
| --- | Minor | ²Òxªö×{X©¿xÐ|U6h»öºblëLTN%;ÑêRè8C<¢­Ì:SÍ @3$éâübü°UcÔ'¦£/Z¯HWª¯EMpÅå;V¼õøoBý%käQ÷£#ýfmÒy/Z]z:¯µÑÓ8.³ûÓW)o.+xÅd	/AÚüWÇÆ|<SÛ¨aÄÞxüý¾VTìúZÃóë&È ¨^h/H5Úºa0	¡ÕYÛÂÃÝÚ'þ÷U¼ÃÒ¬*V] ·ØÌéI!ªN·Þª.. |
| --- | Minor | Sentence exceeds complexity threshold, split for readability. Applying the split needs --strength moderate or higher. |
| --- | Minor | none (split proposal only; source not rewritten) |
| --- | Minor | none |
| --- | Minor | Check: NEEDS-LLM |
| --- | Minor | Flags:    not-assessed |
| --- | Minor | SENTENCE (Line 51, 239 words, 3 clauses)  [Script] |
| --- | Minor | S-ÆÂä§áÞ/F¡jë2~@ïx{Õ2¯d¹3Ò!egYÍÉ.·³ö¬&"N&êéy_Cu«³f:m"2WÄu?Ú²\´Ê5Ód0Û®wîúe&zbÿnÂZ«B[?I;\»êvU»Y²TBv r )¼­Ô ¯$³¤Dóåºêh?Ù¼~Ø0ßR½PBR¿|^ëªcõrã(´ÿ |
| --- | Minor | ¨Fmv®;ÕV)¶ÁFÿbíËF!µ °ñeÍ]_öéç³öîéòãó'Es'k qWÞB&åæ-È^ý1	Ïç¨n©J+"#ÔóÂV8d6ðy³(^ÿ5"'kC´½Ô¸óUS ÿþÇ¯ÿú¼f8@¬þûâ7~p¾ºÙÏ |
| --- | Minor | Q]D |
| --- | Minor | ±¤nQ®Ö¶ 6}rí¦ ¯3yèÛ/ÂáÚe^Ð(J(D5<¢ßàCvû'H ~¤ÙQÉà2öºeÐÑÖùp¥ûX- á;p»xªÂ"»vÀË	ÒcV |
| --- | Minor | $®/Xä`8Tm1Ér2îÈø×U¢ÚaãPÒ`A%w`	«¾¢óïßLÔh·_BSù)En+kx%3§X]Ýdt?ã,MåIÁÓ,N9Jåø:Ð×ä|Nzº8öÚ6+ÈQÍ{Û}fPµúÑÆÌNÜºÉ=Îä°Ã^©¤±Mµ´{©EbROrDFå·Ûá¢Wá¿¼^t |ý÷{ºçLØÂ4^Rô<ÀÑg£Á |
| --- | Minor | ceÅè[Zâ £iõò_¢iÇ"#ÜQ­-ªÒhU}Q"¿×d«eI$Rà¨z4%/{33@ß¤Õë«»k¶O³ 85.A­úI-¤R^ÅsÅRÑò-âÚ·©ÊFB-^¼ñNÄÂy#ýq¦K¨X2%wÒCÙ# vñ~×¨#G1gÊ¨d4ÉÓ¦;h+À­Ú5Ö*oaå]6Ñ õ@0"_-ù YÔÙHîèÖ/'ºÞ,KÝCä£y@µÌ¥Ía%¿zÈKÚàlo;Óttbe¥öC!û)oG¯ÈÛ'O9ay¤Öý­?¦E÷I xGe7i¿¤0-|¼LÒênò ¥mä¹2Ä6N:?ú¨Ý:5ñ©¤±o¨. |
| --- | Minor | S-ÆÂä§áÞ/F¡jë2~@ïx{Õ2¯d¹3Ò!egYÍÉ.·³ö¬&"N&êéy_Cu«³f:m"2WÄu?Ú²\´Ê5Ód0Û®wîúe&zbÿnÂZ«B[?I;\»êvU»Y²TBv r )¼­Ô ¯$³¤Dóåºêh?Ù¼~Ø0ßR½PBR¿|^ëªcõrã(´ÿ |
| --- | Minor | ¨Fmv®;ÕV)¶ÁFÿbíËF!µ °ñeÍ]_öéç³öîéòãó'Es'k qWÞB&åæ-È^ý1	Ïç¨n©J+"#ÔóÂV8d6ðy³(^ÿ5"'kC´½Ô¸óUS ÿþÇ¯ÿú¼f8@¬þûâ7~p¾ºÙÏ |
| --- | Minor | Q]D |
| --- | Minor | ±¤nQ®Ö¶ 6}rí¦ ¯3yèÛ/ÂáÚe^Ð(J(D5<¢ßàCvû'H ~¤ÙQÉà2öºeÐÑÖùp¥ûX- á;p»xªÂ"»vÀË	ÒcV |
| --- | Minor | $®/Xä`8Tm1Ér2îÈø×U¢ÚaãPÒ`A%w`	«¾¢óïßLÔh·_BSù)En+kx%3§X]Ýdt?ã. MåIÁÓ. N9Jåø:Ð×ä|Nzº8öÚ6+ÈQÍ{Û}fPµúÑÆÌNÜºÉ=Îä°Ã^©¤±Mµ´{©EbROrDFå·Ûá¢Wá¿¼^t |ý÷{ºçLØÂ4^Rô<ÀÑg£Á |
| --- | Minor | ceÅè[Zâ £iõò_¢iÇ"#ÜQ­-ªÒhU}Q"¿×d«eI$Rà¨z4%/{33@ß¤Õë«»k¶O³ 85.A­úI-¤R^ÅsÅRÑò-âÚ·©ÊFB-^¼ñNÄÂy#ýq¦K¨X2%wÒCÙ# vñ~×¨#G1gÊ¨d4ÉÓ¦;h+À­Ú5Ö*oaå]6Ñ õ@0"_-ù YÔÙHîèÖ/'ºÞ. KÝCä£y@µÌ¥Ía%¿zÈKÚàlo;Óttbe¥öC!û)oG¯ÈÛ'O9ay¤Öý­?¦E÷I xGe7i¿¤0-|¼LÒênò ¥mä¹2Ä6N:?ú¨Ý:5ñ©¤±o¨.. |
| --- | Minor | Sentence exceeds complexity threshold, split for readability. Applying the split needs --strength moderate or higher. |
| --- | Minor | none (split proposal only; source not rewritten) |
| --- | Minor | none |
| --- | Minor | Check: NEEDS-LLM |
| --- | Minor | Flags:    not-assessed |
| --- | Minor | SENTENCE (Line 51, 134 words, 4 clauses)  [Script] |
| --- | Minor | Í¼Õ8®¼ðJGeeùÂ	·¶ zfÁZÿÝÆF¡Qòe@nÔ*à,Ëöóë«{¥½çí~¾ªí]a>©AÜo¼µÍÍSzô@Û~pÜàà¯ªàÜ5Õ'î[NÞ1Àâ´3ücôE¾ÌÁ+GÚØE,Ç²Þ»0gihìé\F Ð¬Ï5{ÿÂ£íRã¹>ùÓJqÿf®.ècl:;-ÂÚÌd\²Ë½Växê9ðt/gÚ±2Û'Ø¾=BS£t×&?÷ËcÚ2I¯¿PT[nàfÙ IPÙµÿq½!NoÛ],tF÷z²\ª.q9ãÀ5W.wVä¦¹­Û" dyiU*âðàM>¢°Êâà!ôz>ãÆQ´Öñ6TÖèYàµaoFsôÍ	QÓNÿ8ÜSqVMuú*+ð²BdOÿ|úýéÓ «æÀZ_Èi1¬dZÂïÝ?Zõi+E'Æ5H,¤ò¯2êÇêóçñeÖNËðN÷ø'ôTÔMÕ^¨IEÚéÍÂ%²ú®ØÛw~A;Ðp¨ÐC/N¿¬1ãêËÿrä÷P^âb©j®9v^]:#Ï´hü¦øRs¯r0H´^êÁÙÜ! |
| --- | Minor | Í¼Õ8®¼ðJGeeùÂ	·¶ zfÁZÿÝÆF¡Qòe@nÔ*à. Ëöóë«{¥½çí~¾ªí]a>©AÜo¼µÍÍSzô@Û~pÜàà¯ªàÜ5Õ'î[NÞ1Àâ´3ücôE¾ÌÁ+GÚØE. Ç²Þ»0gihìé\F Ð¬Ï5{ÿÂ£íRã¹>ùÓJqÿf®.ècl:;-ÂÚÌd\²Ë½Växê9ðt/gÚ±2Û'Ø¾=BS£t×&?÷ËcÚ2I¯¿PT[nàfÙ IPÙµÿq½!NoÛ]. tF÷z²\ª.q9ãÀ5W.wVä¦¹­Û" dyiU*âðàM>¢°Êâà!ôz>ãÆQ´Öñ6TÖèYàµaoFsôÍ	QÓNÿ8ÜSqVMuú*+ð²BdOÿ|úýéÓ «æÀZ_Èi1¬dZÂïÝ?Zõi+E'Æ5H. ¤ò¯2êÇêóçñeÖNËðN÷ø'ôTÔMÕ^¨IEÚéÍÂ%²ú®ØÛw~A;Ðp¨ÐC/N¿¬1ãêËÿrä÷P^âb©j®9v^]:#Ï´hü¦øRs¯r0H´^êÁÙÜ!. |
| --- | Minor | Sentence exceeds complexity threshold, split for readability. Applying the split needs --strength moderate or higher. |
| --- | Minor | none (split proposal only; source not rewritten) |
| --- | Minor | none |
| --- | Minor | Check: NEEDS-LLM |
| --- | Minor | Flags:    not-assessed |
| --- | Minor | SENTENCE (Line 51, 871 words, 14 clauses)  [Script] |
| --- | Minor | ï{ê Úî è¼ô<vn±½/²¢HÉÀq9¿æC_;\,3}ÓNcò¿ÁÏ!àÛáä¿mDÏ~ïk`À5	QËA§©s.±%r9^/w¶·)øT£À¸9òpóä?Ý5*5ßâY®_æÕÝ¥LÂ×}ÑéQo}#ê½«ÂKù*+3ºu¥6¸¨D¾aïpÔ7vºUoì©IWê(ØnÄá±©PÔÌêiûÑÓÇ\Mn$0=2GúY	iô@2ÎÁÁÉ)"mÔÐXGÎõøsµSñü6WSiC»À§JjXYó=°´}/KX1Ê!<Ew¨÷À &óÓkg]ÃÚZåÝD\ Ü@+j¡¹ÀBsåúß«[£Þ¯çüWyùÖ¥ ý7±PNfàKàºªØ¹H6üµMÀÂmoÁ£c)°9ÚPÛÙ99ç¯Ê»¿5íÈØ tú;z!­~û±ZãVÁî%ÓîÇ?ßW«´FÛÏ¶N´(.g)$Yæ­d¨×fg-ÏÜ-¨l7 mÑYêMÏKs±LxkNÓ¡ácýöhéJVìµ@¾ -ð£-DT |
| --- | Minor |  Ro¦Uì%A¯ÆÃ¡è¶eNÃèhîLDÞ%PþÒp¼ëÅ9vû:Vkæ­"¼¬¸mjgûág¥(³y!]@gC~$J±v49F;Îªj67{-#®x vÇ,ÚASÊç¢bÖüÐÂc÷t2Nj½ÊLÎ¢¡g«BÂ¬¨Æûd{ám4QÍÖ <a´Ó«Ë®§ªbsº@»¾&aÿ^xoXÉhI¡_!wKh&FÜ*ÎFÿ' |
| --- | Minor | ¨¹ëßBäôP0øHgQ°è³ªGZÕäO¾Ó¾)z=Q*S¦×õßkJy±D¤i^Ê  ¡SiÝÕÎ¶#k}ò6<³SyÏ<3¯m Ô}|kósX.ôæûJú­Y_ÛjÉ¸1zY|¢÷5TDUó^óZ<õº« ¯»÷ê0Y÷µ½Aª£©¥U¹SX]¨ÚûzËSÊ=waX8*4CR+)ã]§6=ü`ÖäècÝßv9Sµ<ê Jç¬iE±¦WuÏg»Eê«°È²·¼g=ZyÖXG0åðØ¬edXÐ½Ï7Ú[Ìò©Q.« |
| --- | Minor | =õÞ®Æb§{<5÷îÉÆN	^]JÙ­rS× 4ïP¶©ö1GK>R%EGE9ÒvF©DÖ^ÈX+×W |
| --- | Minor | ¬3Ä@Çö	Z&¹f-e[u |
| --- | Minor | ©uÒ¶Mt |ÒKFÛe´­~Ñêr.u£Â3×Ô%dÍ±ÅslêéýÌD0oc³ÞØä¾ |
| --- | Minor | ¹=jãyn3è	}X«5Ë ³xðhø·á/ÂÇÃn=?f wE4! ÿ¦Õ0õÂF«tNßJÃdÜ(RÆÆdSMy*Íi%>ývW¬/¡÷n#L1ÍÕQ?Û×t£Õú>Â¯n |
| --- | Minor | = |
| --- | Minor | ·Iã}0SÒvÙ~øÚÎ¢*ó6EjÝTå5Euv«¨(Õ·lÈ¼!/Gs{|/Ó¼¸ê4´Ö·k½SQD®GU­DÎAî~}¼Ìéµ¶Â}^zÔ|-bGúB!=5Ã |
| --- | Minor | ¸µ/¢ÝÞI®[è@µ È¶	Á¢Cæì¢`Ñaú|¥-Æ -½V,ÇwÎéÙ¬{<ÒOß¼+r1àÍÍ õ¯¯¹v®.8ù¿T3OÐnoøC¢¢*K_XPú_q%mµ2ÿJíÕæ Ðël¥ÔÑóïÐÈðZ@è~tÛaV{|5ö½EA´æX^xÁþïð,ÌÞX ÞçÙ}ÆÇøÙ 8ÛÇpÈDßêÓusë£?vÖÜ;±Ì®NªÀ¢áSÖ¤.gò |
| --- | Minor | _ÒR¨ RJ	G/N_N8|¹ð&ÛmqòíJçÿ0)ãA\tÙ×¦J#¸ÍE© Ö¾Ê7È}hF3*bue»T6!Fj­OÔ/¢wÌÏÕÖlÖ³ Nk±~^¹V`Û·c½u¤Ó [û*g·ASKºùù²dÂ»ëÊsH·Ôjm(O5ûBò^§¦«p¯NenÊ/ÔµGÅÜüµèÓäÎbÃ¡cÄ`£ïéþâïnp"a'}/èd±Ø ¡Ðª©*úcTIùh ýtRQAÃóÂhµÌÀöKg`Kß¼j 0{áøù>{(4\¬³2}á\sÜ(q¨á"ó5	z·êçaß0®­@ã§-rR óáÈÜ÷o,ûôÿðÞ endstream endobj 216 0 obj <</Filter/FlateDecode/Length 5099>> stream xÚµ\K¯c9Þó+î©¯Pvù=Éñ@BBôfÑ¹4¬àçS~]ö±Or{ºA=79Ço«¾úªÿ¼Èÿ/^[ÿ{yûýÿþôò»/¿ý£|Á7¬~ùxÐøE`ü ´öêåãíg!´¹Ç¿F^þùñÏXÍ¼H±÷±â	M5ÕËÉ¨Í[£C©jîB(À&®BÈ7!¬ÀÏörR^á[«é1B8ïbÙ[þëayyÇÿX -Ù[nÉB.elXè&Ù¬WÆãóx¬Ç÷ÜOlSyæßàÇY_cû#Îeô@}_L|O3SeÔ6ðõZ´!÷ªjFçVDifÒ·ëÔU»µñÄÖel=¾1êµô=c9VéÔVå$Õ{´Y²T`SÎÚò6NÉU& }[Z¢ø,-'vìlìÿB[²Ü ¶-Á¹¦ãFä>b½úö^¶XÂ'=J­-óø×k)}9µ	%ú=r/nNH,pa6«¬2©ì^ç=ëÍXyÙUï~3Ò)½_¨æ¢p,8¡RL,36Ú¸Rê»EcýÕëôtM³TÍÛq¼Q .Eód 7Ö_I¢r©õ³Îißú,¥|RÅÄ¤=%õx»(ÉfçnyAÙVÍ[ÚmexPE3¨ÚjWe0wrmÜïÑç-ûoÙ1rÇiÉ^MÉÀÂîÔÔ&±0@sJ} _OàíR¯ÜpèÂ¿K¯}?V\	Bµ½6Q7» ÙNÏnÁóß*ÂÂÄ8µJþOóMK/ÛÀ5¼%©OÍ·Þ¢ë×»6+pÓ¥uÏmºÂM× ¾`Óµ |
| --- | Minor | «M7>¯±éø%Î©¨§à©õ_¶ûz ØïþhHQ'¼N.ZéZ`ßÌhTÔJ8lf¯ÒDÈ6AvIo©Uoå`A¨Í¢±QÓ¨ð)¥½A4÷vpÎøä?Ø |
| --- | Minor | ?¢JìÿX+ |
| --- | Minor | t JªwïÐO8Ç%ÎÒ^{÷mçs@9Ñ­-AªÔm²e|·8Qu nß?%eaXãhv¶y?á <"2QîÙ(<r\ í­y)ÉWR,Rv/¢ÄàT Y%GÏ¨>q´PéÑ¥Ä#fCÔîÑsTÍ/Ûîl| ÜËªåâ{§ù¿ÎPk:J`+Gæ Î3m­ô§Ñïw6¶]µ[öm'RÔ@¬ûsÀËØ¶p-ØÐß¶dÄ>}X ½zSä|þþõ$­ýð¶òX%ãI9~z]ÚÆ`ÎõqÅ÷WÇH%_@ª p\¦©-kåp\/PÌ¹õ(*··ª®)A\ÚlsPÚý	¨{FÌfìAéÎ±ìp1¾xê6©Û©¢Jg|ÒAåã}"Ú`ïóÄR |
| --- | Minor | ÇoºL0.TFçº¥å×m£ÈvÑb6Ìè¢R[bzæN+={Ù¸<:®N~Jt g¡=ÃùLñ,Øô!µGô÷³T?°wÝv1èÌ(ÇDðràØÂ Â¹«rÐÈcµÀMÚ/1¾=ª»q/+¿'5­£²zM"´#SGòô®ÆóÇçKÜ)X¹6@ì§ÛTZò¶¶´òiËÅ;«CK¨v^:"±­iA&±ÇÞáîàËÙÂ}æÓÀc-ÙY¥øDí,Ò@Þ"L¢#÷¶ZpÔÃT2@·?Ñ,4p¼Ñft°=ÖØEå[½ÒÓÄd3Q *¡;&·M¢|íKwÅGúõLêEöÜnÛÔ JJ=PÈFEUD¨ÏÓe¸ÀÖv¸¤=!6§=¡!å'0O.Å-z©WöÖ}n;ÉÏiâÑM! |
| --- | Minor | ï{ê Úî è¼ô<vn±½/²¢HÉÀq9¿æC_;\. 3}ÓNcò¿ÁÏ!àÛáä¿mDÏ~ïk`À5	QËA§©s.±%r9^/w¶·)øT£À¸9òpóä?Ý5*5ßâY®_æÕÝ¥LÂ×}ÑéQo}#ê½«ÂKù*+3ºu¥6¸¨D¾aïpÔ7vºUoì©IWê(ØnÄá±©PÔÌêiûÑÓÇ\Mn$0=2GúY	iô@2ÎÁÁÉ)"mÔÐXGÎõøsµSñü6WSiC»À§JjXYó=°´}/KX1Ê!<Ew¨÷À &óÓkg]ÃÚZåÝD\ Ü@+j¡¹ÀBsåúß«[£Þ¯çüWyùÖ¥ ý7±PNfàKàºªØ¹H6üµMÀÂmoÁ£c)°9ÚPÛÙ99ç¯Ê»¿5íÈØ tú;z!­~û±ZãVÁî%ÓîÇ?ßW«´FÛÏ¶N´(.g)$Yæ­d¨×fg-ÏÜ-¨l7 mÑYêMÏKs±LxkNÓ¡ácýöhéJVìµ@¾ -ð£-DT |
| --- | Minor |  Ro¦Uì%A¯ÆÃ¡è¶eNÃèhîLDÞ%PþÒp¼ëÅ9vû:Vkæ­"¼¬¸mjgûág¥(³y!]@gC~$J±v49F;Îªj67{-#®x vÇ. ÚASÊç¢bÖüÐÂc÷t2Nj½ÊLÎ¢¡g«BÂ¬¨Æûd{ám4QÍÖ <a´Ó«Ë®§ªbsº@»¾&aÿ^xoXÉhI¡_!wKh&FÜ*ÎFÿ' |
| --- | Minor | ¨¹ëßBäôP0øHgQ°è³ªGZÕäO¾Ó¾)z=Q*S¦×õßkJy±D¤i^Ê  ¡SiÝÕÎ¶#k}ò6<³SyÏ<3¯m Ô}|kósX.ôæûJú­Y_ÛjÉ¸1zY|¢÷5TDUó^óZ<õº« ¯»÷ê0Y÷µ½Aª£©¥U¹SX]¨ÚûzËSÊ=waX8*4CR+)ã]§6=ü`ÖäècÝßv9Sµ<ê Jç¬iE±¦WuÏg»Eê«°È²·¼g=ZyÖXG0åðØ¬edXÐ½Ï7Ú[Ìò©Q.« |
| --- | Minor | =õÞ®Æb§{<5÷îÉÆN	^]JÙ­rS× 4ïP¶©ö1GK>R%EGE9ÒvF©DÖ^ÈX+×W |
| --- | Minor | ¬3Ä@Çö	Z&¹f-e[u |
| --- | Minor | ©uÒ¶Mt |ÒKFÛe´­~Ñêr.u£Â3×Ô%dÍ±ÅslêéýÌD0oc³ÞØä¾ |
| --- | Minor | ¹=jãyn3è	}X«5Ë ³xðhø·á/ÂÇÃn=?f wE4! ÿ¦Õ0õÂF«tNßJÃdÜ(RÆÆdSMy*Íi%>ývW¬/¡÷n#L1ÍÕQ?Û×t£Õú>Â¯n |
| --- | Minor | = |
| --- | Minor | ·Iã}0SÒvÙ~øÚÎ¢*ó6EjÝTå5Euv«¨(Õ·lÈ¼!/Gs{|/Ó¼¸ê4´Ö·k½SQD®GU­DÎAî~}¼Ìéµ¶Â}^zÔ|-bGúB!=5Ã |
| --- | Minor | ¸µ/¢ÝÞI®[è@µ È¶	Á¢Cæì¢`Ñaú|¥-Æ -½V. ÇwÎéÙ¬{<ÒOß¼+r1àÍÍ õ¯¯¹v®.8ù¿T3OÐnoøC¢¢*K_XPú_q%mµ2ÿJíÕæ Ðël¥ÔÑóïÐÈðZ@è~tÛaV{|5ö½EA´æX^xÁþïð. ÌÞX ÞçÙ}ÆÇøÙ 8ÛÇpÈDßêÓusë£?vÖÜ;±Ì®NªÀ¢áSÖ¤.gò |
| --- | Minor | _ÒR¨ RJ	G/N_N8|¹ð&ÛmqòíJçÿ0)ãA\tÙ×¦J#¸ÍE© Ö¾Ê7È}hF3*bue»T6!Fj­OÔ/¢wÌÏÕÖlÖ³ Nk±~^¹V`Û·c½u¤Ó [û*g·ASKºùù²dÂ»ëÊsH·Ôjm(O5ûBò^§¦«p¯NenÊ/ÔµGÅÜüµèÓäÎbÃ¡cÄ`£ïéþâïnp"a'}/èd±Ø ¡Ðª©*úcTIùh ýtRQAÃóÂhµÌÀöKg`Kß¼j 0{áøù>{(4\¬³2}á\sÜ(q¨á"ó5	z·êçaß0®­@ã§-rR óáÈÜ÷o. ûôÿðÞ endstream endobj 216 0 obj <</Filter/FlateDecode/Length 5099>> stream xÚµ\K¯c9Þó+î©¯Pvù=Éñ@BBôfÑ¹4¬àçS~]ö±Or{ºA=79Ço«¾úªÿ¼Èÿ/^[ÿ{yûýÿþôò»/¿ý£|Á7¬~ùxÐøE`ü ´öêåãíg!´¹Ç¿F^þùñÏXÍ¼H±÷±â	M5ÕËÉ¨Í[£C©jîB(À&®BÈ7!¬ÀÏörR^á[«é1B8ïbÙ[þëayyÇÿX -Ù[nÉB.elXè&Ù¬WÆãóx¬Ç÷ÜOlSyæßàÇY_cû#Îeô@}_L|O3SeÔ6ðõZ´!÷ªjFçVDifÒ·ëÔU»µñÄÖel=¾1êµô=c9VéÔVå$Õ{´Y²T`SÎÚò6NÉU& }[Z¢ø. -'vìlìÿB[²Ü ¶-Á¹¦ãFä>b½úö^¶XÂ'=J­-óø×k)}9µ	%ú=r/nNH. pa6«¬2©ì^ç=ëÍXyÙUï~3Ò)½_¨æ¢p. 8¡RL. 36Ú¸Rê»EcýÕëôtM³TÍÛq¼Q .Eód 7Ö_I¢r©õ³Îißú. ¥|RÅÄ¤=%õx»(ÉfçnyAÙVÍ[ÚmexPE3¨ÚjWe0wrmÜïÑç-ûoÙ1rÇiÉ^MÉÀÂîÔÔ&±0@sJ} _OàíR¯ÜpèÂ¿K¯}?V\	Bµ½6Q7» ÙNÏnÁóß*ÂÂÄ8µJþOóMK/ÛÀ5¼%©OÍ·Þ¢ë×»6+pÓ¥uÏmºÂM× ¾`Óµ |
| --- | Minor | «M7>¯±éø%Î©¨§à©õ_¶ûz ØïþhHQ'¼N.ZéZ`ßÌhTÔJ8lf¯ÒDÈ6AvIo©Uoå`A¨Í¢±QÓ¨ð)¥½A4÷vpÎøä?Ø |
| --- | Minor | ?¢JìÿX+ |
| --- | Minor | t JªwïÐO8Ç%ÎÒ^{÷mçs@9Ñ­-AªÔm²e|·8Qu nß?%eaXãhv¶y?á <"2QîÙ(<r\ í­y)ÉWR. Rv/¢ÄàT Y%GÏ¨>q´PéÑ¥Ä#fCÔîÑsTÍ/Ûîl| ÜËªåâ{§ù¿ÎPk:J`+Gæ Î3m­ô§Ñïw6¶]µ[öm'RÔ@¬ûsÀËØ¶p-ØÐß¶dÄ>}X ½zSä|þþõ$­ýð¶òX%ãI9~z]ÚÆ`ÎõqÅ÷WÇH%_@ª p\¦©-kåp\/PÌ¹õ(*··ª®)A\ÚlsPÚý	¨{FÌfìAéÎ±ìp1¾xê6©Û©¢Jg|ÒAåã}"Ú`ïóÄR |
| --- | Minor | ÇoºL0.TFçº¥å×m£ÈvÑb6Ìè¢R[bzæN+={Ù¸<:®N~Jt g¡=ÃùLñ. Øô!µGô÷³T?°wÝv1èÌ(ÇDðràØÂ Â¹«rÐÈcµÀMÚ/1¾=ª»q/+¿'5­£²zM"´#SGòô®ÆóÇçKÜ)X¹6@ì§ÛTZò¶¶´òiËÅ;«CK¨v^:"±­iA&±ÇÞáîàËÙÂ}æÓÀc-ÙY¥øDí. Ò@Þ"L¢#÷¶ZpÔÃT2@·?Ñ. 4p¼Ñft°=ÖØEå[½ÒÓÄd3Q *¡;&·M¢|íKwÅGúõLêEöÜnÛÔ JJ=PÈFEUD¨ÏÓe¸ÀÖv¸¤=!6§=¡!å'0O.Å-z©WöÖ}n;ÉÏiâÑM!. |
| --- | Minor | Sentence exceeds complexity threshold, split for readability. Applying the split needs --strength moderate or higher. |
| --- | Minor | none (split proposal only; source not rewritten) |
| --- | Minor | none |
| --- | Minor | Check: NEEDS-LLM |
| --- | Minor | Flags:    not-assessed |
| --- | Minor | SENTENCE (Line 51, 1201 words, 18 clauses)  [Script] |
| --- | Minor | ]Í_þ¾À?Ò¡¯4ùÿ~Å¹»µ¨JiA F_¢Ó0¹TËÁÜA!Ù |
| --- | Minor | !!ÏLÈðj@ýßZívI,wiR"1µN»NV(? (ävGeUÇ¡úÔR©#UÔG""H#GDRõ%ªÊh®DÙ1ºÃ=,jQkw0Z<#¿UUHËÒ^§(ÍôDn¯µC68u¨# 9hS¨tÜ}ãqÊX¤þ<ÏÂjÎ,½Ó<d>üÞ»PY}yFRtA+ÿÉg<E ÔC)GÚqMCÄ£hå´¥$J2É\)Ôu=U}ÊúîLøãÌ`Ø?¥hñêÉS¬oÍNA0c¯¼õ×ÕGÁÚÝâÍ0ílRvÔ3uGIÆR©¾yX¶Ø«¼:y¨=ãêÅÉ0é¦Û£î, ànà Ñm{ÇÇãD³ôÅ«:)­ù´­à¾E®~§§qN|®)UE]ínN¹½kÓEÔJkW |
| --- | Minor | -×õÓagéiÅI %jaCoCøçTð(M1@cjxøÌ"ÛiÆdíÓzÜi&Îó½«ëv'î¬ôI;ÁÅt±xiû|û+ø¨Ì=yZ¼¸ÒJUO¼¬÷ÆsÌÕ½aLJÜ/Z.IpÀ­´>©'BmX'Ë!0ó&l¤kvÏrwÞM?(SLÞYH¥{dB$½÷6C×ÍÐèi¢dªâ<ÍÇéo^·p¾5yóìØCÍËkGov½¶àx5è2lòCNY=bÂ|y [MÙt[CtªBäÃNïö+Wc]NGEhu<4"«±?bs¤4j|Eô¢ÚT-ÕÏ[L ðbìD¨c.}fõ cVß	î3kg)ÂîÖ'²gJÄ«ò#pÖÆÎ¡5Ø¢Ìs¹I+Á®vA» !{ÞMÄ±¼a±¦Þ*ðËË!XFÉm UbtÂKzE<3OØ6õ­Â¬p  ËÛu«, Íâ4p»MygÌÞçÎbÝóÀ&­[.NZxôZ[cÑk+eeÙðëÞû/Äé´u3ÑaPÚ!°sè'_6<¨é7"¼±¦oÇ5c6ÑrÖ§P3ÄÌ »ï3|H:w¿EÛSføÔLÄ¸xÄ·ÜlÕµÀÅh¼÷¼Q%VPV¡ Xd¶×Ô£°ÍvÃA9¢êìÓ}ÕÃº:Û £ÁLâk*øàÃ¦XLÑL±Íâ` ÷,Àr |
| --- | Minor | /cNøÃ¼'¬Fy.ÊªY`Ö>)åàÄ0^Á®æ£Îl.x?ëS×ôz3Á µ¯Iz5ºÕ°6è°·ÂM~EîÍV£jíÌ½J§m-í%¡é×QÅ >% É¹F´DÙ"SVeÏi¦x	*W(gvHð»5RcÔ®éA08=ågwå hZH@±"q®×7XµdÒÛJZ1:(µ·Ûz¢H2gnouÓ«À¦ÞÐS#é7ÄÂÖH×6þü¿Eh70~HVØ($ÌÀKP£å­¬Ðó8Ntä7ålp³`UK·éáL½aÔ¹yCóH4OhñYÚ^t%HBÅ¥6¶ö`%6Åý¤¦¥ñê1¥¹ªsè¶)Yãü¾w¸£k,¿lÎd¡?÷,eBKf)ÏYYuÈ¢aÏ<¨q Cêuãö:_J3[ÄRpkÆõÝâ#_·e\B®­d]AèiÉ´OÕäöIbÔþ\´ÇÛxù)¨¡cf²ï}ÂÏ±Äýâk¶ÎË¨U¡ïM3-£*YS(ß%P}ÀªË*ÿÜ1!Õb©ODT;ÚwÝ.èäTµ1B5ß©àUDkØ£wH|Ê¨WHa|b'+ëÁê7aÁMê|7©_VJÆ,BM¨´¡êVNeèRêa¡érÍ#B*x¨3Ñiû´ùQäøLY±Þvc°¬obr´àëÔû« Í9¶ä¬=ÐR½¯úÌ¸-ÒvwA±1ãIVèkÇ»üâ½fQÎ¹L/ÒÞl£^áI×kk¨¾Åµ5ûä­¤ú]üãòúíûUæFJt­W]~³õ0¹wÛ |
| --- | Minor | §ÅÆw	=¶<ÔUyhp¸ÍviË©fX,gó5È§µÇYçÆ\µ«¦JÝÉ¦ÌÐàF¢YµÄS¹ñ,JK¤,¸ÓÁ Ä×¢êî'5ç¨wÅ²>XV{².ÿÒX&23*]Ç[ãùmjµ»Ñè7Fø¶áPX~X´Õïkkw^N.ÛíÈþMH!á[â¾æ³ÊÁw@ë^¯óöìQu,k¥$H@¯E£RNc£sF¢£ªWexItuéë`©5½S8q<,w1ø(`ÐÂ5#b=Z »ÿÅz«ô«æEµ£³«¹T¬=8c7¦NU8~ö3/%2sjºyr}³­H½ìü0¯CnÍê~þ#¡e&ÕÓgñ!Òf?Z1n´zºÃ³ÿ- Ô´ÄÛÞ¶Ý×»¼âø`Vz¶Û÷¯áê¯í·-®´@ak>ÀdÏ9!aìTHè]U~r}ZèfíÎ}×äÈ¡ZØÐi0aÈlmZ©ssïIìñµ%Ùëª3#MÇQÅ|ß'vê×RäN´Y31Úkúi¥.ÿ«ÏÚou©Å½T®-¤A"Mcô²²O=Vù<GyYÈ *()y.Y8øÉMt-âlÈ°ºÞ¯.ó¤ÿÝyÐ<]+3êH×R©JÙñÙTèrÁ¹ÞåÓÀF)Ý<\·ÚôJ}"~Äãï±'<fÏ~Í,Âåí0;b«EÜÂ­ÏpÏ/mÉ+©SÏßÆ$ò¤ îßz¤ù¬(ï¡Ï5ª"NýØÏ./#ØÑåô&ç¹¶@Öj5ùÐA­ýEâÊÆ>ÖOßÇ°W9!sOú©ö¤hBtdoh±ASÚ]®«ÆyfÜØ"ÁnJ©ñbþ*´ñ1%¡-YLOÉdªûîkÐhTB×5lÆb»+öùkcV8cN:XwëãÚëZl PÑsËl8ZîÄ´\ßÑÓJ«ÆÔøsç¤µÐeYnh?+RæÐ¥]yø(ËïºÍx)ôìwÛ5R¦öjÌ;gÊùr6ò§ÄWÔsÛóIGåØôÉYv¼ëÔ;-cºâéü"ß¬âÞù:ïQ:×ïÍTmUòÞô0AóÎl`C½¡¦Â*xqnc(ÊÈjnÖ:ífn~N^ìCÃü÷.×i³=X°Mª£Ày¨á²òµá%C/#ÊH|Òæ ¿1Ãù}ë~ ãÎW`j§¹»dÚí!áOcYu5ËÚ  |
| --- | Minor | -û{zmbÚú®ÂZÖÒµÀrMá8Ñ'æÿ!n×rßBSÇëÄIhÇ}ÌÌ|k ý/J2lZÆðí	BüMÀ¦¾âz×´ä¿ýêÿÅgÛÔ endstream endobj 223 0 obj <</Length1 3716/Length 2489/Filter/FlateDecode>> stream xÍU{pTÕÿîý³»ÙdÝìMÂB²<ØM×&$HÍÍl+	ñÁð( FJÚ`Û¨£Fâ XA«ÍtªC­3NÕªUgêÎ`g¤än¿{mpÚþÛ3çï÷ß÷8ÏK ¹ø#ÈYVRºÜd#R&°6¹¬ry|ûëcóGÊªV?t_2ãg/¯Êñ5m7ðW×¶#¢1é6"Õà¬ÝÜáyØú ã·s°>ÒÐòE÷7op°u<ÞÓl+/Ç54wÖñæ{ÙF9ÖXÙ|½ÈrÐ×È Çë%Æ¿cÑØÒ±5­[YÎø2cOs[mPMoY[[#¢^ýq1Þl©U¸qá?ÒÖÞñ'\â|lñøÈÆºÈ¦NËßb/ï cmâh¤¨À¹:£Ù)(Y|óJJ­íÜØL© |
| --- | Minor | ëÂÚìh¥T^O.Ñè?\·±ÕX×QkÁÞÞÆ½f2S)±jFRÆ0¤Fâù(ïºxf¼3^ÆñÆE¤*ûØI¿<L³4£â}ªWyJ$d¬jØÞ;Ö°²¾4ÄQ+pÆ¢érÄÚ¢|:ýHÁh`fF´bbAsL17*¨/à×rôèkU×nãïûu"aòG!×6^idáþÌH#«b§v7@ïp}¥©î¢tåÏi©?/lFeÍÒà¾GÊtæªJ¹ËgÙÇ>g~=ãã´Þ¿!³ÁºTT²TiZ§ÌC#Í´zæÓê3d9D½Ì[Aïs-fïKéUú@¹N*¨öR»¹u»¼Ä¹4ÑzyÉ¬iÙÐ5ÉK#5ñ<_eï'GôÊtejP¯¬áªJ°v5®f-1ç72UÝÆñGçKCê:uºÈTú8cý÷Ñ|Î·3]ÂM5òÇWtÆîçi©u©%N±X»xÇUÚ¿rÄ2j¨+ÙÃ2Öí¥eÊûöK) *4ÓãìW½å¡þÀ­k<o­5óGÐã´zú©²ßÑéF+×äÚ~9¡^[¿ð¦ò?ÉYQ¹ÆÓÿÛÒQ¯¥5%¬«ZÃ¢XÍúÒ¬Ì;Ï'Ojô#>>Õ¼Þ)Dé~wzÁdk:³QüÖÉ üVvö»³IjYÒÙVõIÊå¤gÕ¢>Mzøâæ³Z¤pxø5¿CÃþ&õÂðÓM|¦WG?«xÝÓùÂXDúÌ©ùyä÷%Cz^~^æÔô)«%Iì÷Í.À%z´ÿË¶[|Êª/ë^»=/Wxÿ£²´	ù½[Nù}Ï)]FQeVN®~9>nkaà¿nXQ³°ãî.ãV^ÔWó"Ó¸ÞD+ûÎZ  fgNÍ,ð'K6Ôj¯\(mJM{¹¾?IYy»VâsgÅEê]ãìîgÏÓ?l^­¢¡ã3<¾v\õní¢°kîâ¹+óçø**Ñ¿ñÂn`pýøaÙójª/kÇnU]5åí%½GÉ<¬ |
| --- | Minor | }uzî)møvêT¿&2Ãz­òD8¬8ünSòâN;¬Ü0úÎ¨k?Õ~ñÎyßÒ$ù(üa{ü¿ï¿+.tL³}lîêï?-úD"ÇGßÿ£Å1Bü?[lÂ8Ýû>n=<«ÑÅ6Z-Þ¢raôë1Ülj Çé÷£ùØÔAÌwÍÉïñ×5ôæûd¥Ûs%bX>k¾¬ðù:;*«üÂýqTM¥¿Êb,)E±ÊÊP<´Ú(B´6p6ÔAÆ/átî}üÊå·ÊÃ·»¿ÅÌéà×Áì: RÍdm9µ2?¥"jæêáè{_í&ªã¾m6ó7ÄL;°ÔÄVÓ&fÔ27È^L¦eÃ¿½´ò7Âõìwó<lßÆqæØýTQ6ðúsìà¨Íâx®c­6õí,·Q}§ò¯³þmÖu¶ÆÍ§è·Ü¶ó.ý»2ògVyå³i±¢* |
| --- | Minor |  # ÑÚøøMÝ¸ðF¼Âx#¿qàõóòõÎgâ\5^ëÂ«±ÅW4yÆW4øð²t¼¨ãÏëx®¿L>wýeøµ_uá:Çé¾8yZC_~áÃ3!ü< |
| --- | Minor | '}xêDH>¥ãDOöÆË'½8¾Õ.{ñ³ sâl<¾+M>®ãè§<:G8|(^öâóÅãP@<Æix¬[ôÆ£7 õâà¹ò G¸å#^ØïÜ80 1bÿ>»ÜïÀþåbûÎÛºäÃxèÞXùÄ^öâÁAù =Õ²g=ÝbÏn¯ÜS=±óÚíÅ®.¹+ |
| --- | Minor | »¢çQ±ÓzGäâþdÜ×{cÑ Én÷4;å=ã±½+^n÷¡+woKw»±-?íE§[íØ²Ù#·\ÅæMäf6M@u¤¡]ÇFwEò. |
| --- | Minor | ]Í_þ¾À?Ò¡¯4ùÿ~Å¹»µ¨JiA F_¢Ó0¹TËÁÜA!Ù |
| --- | Minor | !!ÏLÈðj@ýßZívI. wiR"1µN»NV(? (ävGeUÇ¡úÔR©#UÔG""H#GDRõ%ªÊh®DÙ1ºÃ=. jQkw0Z<#¿UUHËÒ^§(ÍôDn¯µC68u¨# 9hS¨tÜ}ãqÊX¤þ<ÏÂjÎ. ½Ó<d>üÞ»PY}yFRtA+ÿÉg<E ÔC)GÚqMCÄ£hå´¥$J2É\)Ôu=U}ÊúîLøãÌ`Ø?¥hñêÉS¬oÍNA0c¯¼õ×ÕGÁÚÝâÍ0ílRvÔ3uGIÆR©¾yX¶Ø«¼:y¨=ãêÅÉ0é¦Û£î.  ànà Ñm{ÇÇãD³ôÅ«:)­ù´­à¾E®~§§qN|®)UE]ínN¹½kÓEÔJkW |
| --- | Minor | -×õÓagéiÅI %jaCoCøçTð(M1@cjxøÌ"ÛiÆdíÓzÜi&Îó½«ëv'î¬ôI;ÁÅt±xiû|û+ø¨Ì=yZ¼¸ÒJUO¼¬÷ÆsÌÕ½aLJÜ/Z.IpÀ­´>©'BmX'Ë!0ó&l¤kvÏrwÞM?(SLÞYH¥{dB$½÷6C×ÍÐèi¢dªâ<ÍÇéo^·p¾5yóìØCÍËkGov½¶àx5è2lòCNY=bÂ|y [MÙt[CtªBäÃNïö+Wc]NGEhu<4"«±?bs¤4j|Eô¢ÚT-ÕÏ[L ðbìD¨c.}fõ cVß	î3kg)ÂîÖ'²gJÄ«ò#pÖÆÎ¡5Ø¢Ìs¹I+Á®vA» !{ÞMÄ±¼a±¦Þ*ðËË!XFÉm UbtÂKzE<3OØ6õ­Â¬p  ËÛu«. Íâ4p»MygÌÞçÎbÝóÀ&­[.NZxôZ[cÑk+eeÙðëÞû/Äé´u3ÑaPÚ!°sè'_6<¨é7"¼±¦oÇ5c6ÑrÖ§P3ÄÌ »ï3|H:w¿EÛSføÔLÄ¸xÄ·ÜlÕµÀÅh¼÷¼Q%VPV¡ Xd¶×Ô£°ÍvÃA9¢êìÓ}ÕÃº:Û £ÁLâk*øàÃ¦XLÑL±Íâ` ÷. Àr |
| --- | Minor | /cNøÃ¼'¬Fy.ÊªY`Ö>)åàÄ0^Á®æ£Îl.x?ëS×ôz3Á µ¯Iz5ºÕ°6è°·ÂM~EîÍV£jíÌ½J§m-í%¡é×QÅ >% É¹F´DÙ"SVeÏi¦x	*W(gvHð»5RcÔ®éA08=ågwå hZH@±"q®×7XµdÒÛJZ1:(µ·Ûz¢H2gnouÓ«À¦ÞÐS#é7ÄÂÖH×6þü¿Eh70~HVØ($ÌÀKP£å­¬Ðó8Ntä7ålp³`UK·éáL½aÔ¹yCóH4OhñYÚ^t%HBÅ¥6¶ö`%6Åý¤¦¥ñê1¥¹ªsè¶)Yãü¾w¸£k. ¿lÎd¡?÷. eBKf)ÏYYuÈ¢aÏ<¨q Cêuãö:_J3[ÄRpkÆõÝâ#_·e\B®­d]AèiÉ´OÕäöIbÔþ\´ÇÛxù)¨¡cf²ï}ÂÏ±Äýâk¶ÎË¨U¡ïM3-£*YS(ß%P}ÀªË*ÿÜ1!Õb©ODT;ÚwÝ.èäTµ1B5ß©àUDkØ£wH|Ê¨WHa|b'+ëÁê7aÁMê|7©_VJÆ. BM¨´¡êVNeèRêa¡érÍ#B*x¨3Ñiû´ùQäøLY±Þvc°¬obr´àëÔû« Í9¶ä¬=ÐR½¯úÌ¸-ÒvwA±1ãIVèkÇ»üâ½fQÎ¹L/ÒÞl£^áI×kk¨¾Åµ5ûä­¤ú]üãòúíûUæFJt­W]~³õ0¹wÛ |
| --- | Minor | §ÅÆw	=¶<ÔUyhp¸ÍviË©fX. gó5È§µÇYçÆ\µ«¦JÝÉ¦ÌÐàF¢YµÄS¹ñ. JK¤. ¸ÓÁ Ä×¢êî'5ç¨wÅ²>XV{².ÿÒX&23*]Ç[ãùmjµ»Ñè7Fø¶áPX~X´Õïkkw^N.ÛíÈþMH!á[â¾æ³ÊÁw@ë^¯óöìQu. k¥$H@¯E£RNc£sF¢£ªWexItuéë`©5½S8q<. w1ø(`ÐÂ5#b=Z »ÿÅz«ô«æEµ£³«¹T¬=8c7¦NU8~ö3/%2sjºyr}³­H½ìü0¯CnÍê~þ#¡e&ÕÓgñ!Òf?Z1n´zºÃ³ÿ- Ô´ÄÛÞ¶Ý×»¼âø`Vz¶Û÷¯áê¯í·-®´@ak>ÀdÏ9!aìTHè]U~r}ZèfíÎ}×äÈ¡ZØÐi0aÈlmZ©ssïIìñµ%Ùëª3#MÇQÅ|ß'vê×RäN´Y31Úkúi¥.ÿ«ÏÚou©Å½T®-¤A"Mcô²²O=Vù<GyYÈ *()y.Y8øÉMt-âlÈ°ºÞ¯.ó¤ÿÝyÐ<]+3êH×R©JÙñÙTèrÁ¹ÞåÓÀF)Ý<\·ÚôJ}"~Äãï±'<fÏ~Í. Âåí0;b«EÜÂ­ÏpÏ/mÉ+©SÏßÆ$ò¤ îßz¤ù¬(ï¡Ï5ª"NýØÏ./#ØÑåô&ç¹¶@Öj5ùÐA­ýEâÊÆ>ÖOßÇ°W9!sOú©ö¤hBtdoh±ASÚ]®«ÆyfÜØ"ÁnJ©ñbþ*´ñ1%¡-YLOÉdªûîkÐhTB×5lÆb»+öùkcV8cN:XwëãÚëZl PÑsËl8ZîÄ´\ßÑÓJ«ÆÔøsç¤µÐeYnh?+RæÐ¥]yø(ËïºÍx)ôìwÛ5R¦öjÌ;gÊùr6ò§ÄWÔsÛóIGåØôÉYv¼ëÔ;-cºâéü"ß¬âÞù:ïQ:×ïÍTmUòÞô0AóÎl`C½¡¦Â*xqnc(ÊÈjnÖ:ífn~N^ìCÃü÷.×i³=X°Mª£Ày¨á²òµá%C/#ÊH|Òæ ¿1Ãù}ë~ ãÎW`j§¹»dÚí!áOcYu5ËÚ  |
| --- | Minor | -û{zmbÚú®ÂZÖÒµÀrMá8Ñ'æÿ!n×rßBSÇëÄIhÇ}ÌÌ|k ý/J2lZÆðí	BüMÀ¦¾âz×´ä¿ýêÿÅgÛÔ endstream endobj 223 0 obj <</Length1 3716/Length 2489/Filter/FlateDecode>> stream xÍU{pTÕÿîý³»ÙdÝìMÂB²<ØM×&$HÍÍl+	ñÁð( FJÚ`Û¨£Fâ XA«ÍtªC­3NÕªUgêÎ`g¤än¿{mpÚþÛ3çï÷ß÷8ÏK ¹ø#ÈYVRºÜd#R&°6¹¬ry|ûëcóGÊªV?t_2ãg/¯Êñ5m7ðW×¶#¢1é6"Õà¬ÝÜáyØú ã·s°>ÒÐòE÷7op°u<ÞÓl+/Ç54wÖñæ{ÙF9ÖXÙ|½ÈrÐ×È Çë%Æ¿cÑØÒ±5­[YÎø2cOs[mPMoY[[#¢^ýq1Þl©U¸qá?ÒÖÞñ'\â|lñøÈÆºÈ¦NËßb/ï cmâh¤¨À¹:£Ù)(Y|óJJ­íÜØL© |
| --- | Minor | ëÂÚìh¥T^O.Ñè?\·±ÕX×QkÁÞÞÆ½f2S)±jFRÆ0¤Fâù(ïºxf¼3^ÆñÆE¤*ûØI¿<L³4£â}ªWyJ$d¬jØÞ;Ö°²¾4ÄQ+pÆ¢érÄÚ¢|:ýHÁh`fF´bbAsL17*¨/à×rôèkU×nãïûu"aòG!×6^idáþÌH#«b§v7@ïp}¥©î¢tåÏi©?/lFeÍÒà¾GÊtæªJ¹ËgÙÇ>g~=ãã´Þ¿!³ÁºTT²TiZ§ÌC#Í´zæÓê3d9D½Ì[Aïs-fïKéUú@¹N*¨öR»¹u»¼Ä¹4ÑzyÉ¬iÙÐ5ÉK#5ñ<_eï'GôÊtejP¯¬áªJ°v5®f-1ç72UÝÆñGçKCê:uºÈTú8cý÷Ñ|Î·3]ÂM5òÇWtÆîçi©u©%N±X»xÇUÚ¿rÄ2j¨+ÙÃ2Öí¥eÊûöK) *4ÓãìW½å¡þÀ­k<o­5óGÐã´zú©²ßÑéF+×äÚ~9¡^[¿ð¦ò?ÉYQ¹ÆÓÿÛÒQ¯¥5%¬«ZÃ¢XÍúÒ¬Ì;Ï'Ojô#>>Õ¼Þ)Dé~wzÁdk:³QüÖÉ üVvö»³IjYÒÙVõIÊå¤gÕ¢>Mzøâæ³Z¤pxø5¿CÃþ&õÂðÓM|¦WG?«xÝÓùÂXDúÌ©ùyä÷%Cz^~^æÔô)«%Iì÷Í.À%z´ÿË¶[|Êª/ë^»=/Wxÿ£²´	ù½[Nù}Ï)]FQeVN®~9>nkaà¿nXQ³°ãî.ãV^ÔWó"Ó¸ÞD+ûÎZ  fgNÍ. ð'K6Ôj¯\(mJM{¹¾?IYy»VâsgÅEê]ãìîgÏÓ?l^­¢¡ã3<¾v\õní¢°kîâ¹+óçø**Ñ¿ñÂn`pýøaÙójª/kÇnU]5åí%½GÉ<¬ |
| --- | Minor | }uzî)møvêT¿&2Ãz­òD8¬8ünSòâN;¬Ü0úÎ¨k?Õ~ñÎyßÒ$ù(üa{ü¿ï¿+.tL³}lîêï?-úD"ÇGßÿ£Å1Bü?[lÂ8Ýû>n=<«ÑÅ6Z-Þ¢raôë1Ülj Çé÷£ùØÔAÌwÍÉïñ×5ôæûd¥Ûs%bX>k¾¬ðù:;*«üÂýqTM¥¿Êb. )E±ÊÊP<´Ú(B´6p6ÔAÆ/átî}üÊå·ÊÃ·»¿ÅÌéà×Áì: RÍdm9µ2?¥"jæêáè{_í&ªã¾m6ó7ÄL;°ÔÄVÓ&fÔ27È^L¦eÃ¿½´ò7Âõìwó<lßÆqæØýTQ6ðúsìà¨Íâx®c­6õí. ·Q}§ò¯³þmÖu¶ÆÍ§è·Ü¶ó.ý»2ògVyå³i±¢* |
| --- | Minor |  # ÑÚøøMÝ¸ðF¼Âx#¿qàõóòõÎgâ\5^ëÂ«±ÅW4yÆW4øð²t¼¨ãÏëx®¿L>wýeøµ_uá:Çé¾8yZC_~áÃ3!ü< |
| --- | Minor | '}xêDH>¥ãDOöÆË'½8¾Õ.{ñ³ sâl<¾+M>®ãè§<:G8|(^öâóÅãP@<Æix¬[ôÆ£7 õâà¹ò G¸å#^ØïÜ80 1bÿ>»ÜïÀþåbûÎÛºäÃxèÞXùÄ^öâÁAù =Õ²g=ÝbÏn¯ÜS=±óÚíÅ®.¹+ |
| --- | Minor | »¢çQ±ÓzGäâþdÜ×{cÑ Én÷4;å=ã±½+^n÷¡+woKw»±-?íE§[íØ²Ù#·\ÅæMäf6M@u¤¡]ÇFwEò.. |
| --- | Minor | Sentence exceeds complexity threshold, split for readability. Applying the split needs --strength moderate or higher. |
| --- | Minor | none (split proposal only; source not rewritten) |
| --- | Minor | none |
| --- | Minor | Check: NEEDS-LLM |
| --- | Minor | Flags:    not-assessed |
| --- | Minor | SENTENCE (Line 51, 465 words, 7 clauses)  [Script] |
| --- | Minor | "ÑÖÖ²5hÇÉf'»E8áhâMW±¡qPnÐÑØP-ÑØ-ê½²¡ |
| --- | Minor | QïEê®"BmÖëê¨¹3[Öè¸3wè¨Ö±®·wá6kK°FÇOt¬Ä*U!¬Ðp«Ëde'`YQ 7ÇbiåSl²¼K|(S¹±8¥ª]GÉ"·,	cQ±S.r£¸(V;QE±Ä `¬cXØ"K.¸óçir~æÍµËyæÄ\; oJÕ¸iKÞ9.80[G~&óuäùÝ2Oßg~7|³b¤ÏßÈþÌAnNÌ-ANvÌIAÎ9fÙIÈîY1!Õ349³3x34Ì9õC>-WN/Â4NlZ.2¹ËÔ1µ^GôV##=QfT!ÍÒSlìI«áäxÎIlºEi11pCRÇçÊÔ*g¯ãs¢c§#Ù$MIahn·Ô4háv#ypñòºt8¹s#óOèE<Åëp°G §#Al`NvæØ»Íê6 |
| --- | Minor | ,Ò'-]l'}ìLdªv(U ÊÚ±Wñ[èÀ-ü·þ')	~ endstream endobj 225 0 obj <</Length 35/Filter/FlateDecode>> stream xc`Dõ¬4qÅ(£`Q@`Cá± D¾  endstream endobj 226 0 obj <</Length 252/Filter/FlateDecode>> stream x]»nÄ E{¾bÊM±b_JeYvy(N*+ÁBa\øï3ÀÆWsf.0Ã¯Ý­s6^õÀX§#Î~ Aâh;@[îQ9Õ$ãdî×9áÔ9ãYÓ §äâ »'í%>0 à¯Qc´nÝçµ¯¨_BøÆ	]k[Ðhèºg^ÄÀyßiÊÛ´îÉöWñ±SõKÊkP5Z-4VËÐéùKuI³_$Wª~eüx.8ËP5ã³,¸ÈPµbQ±¸cAÿ}&ÿ#mkR-1Re²¥±Üu¸ |
| --- | Minor | ?ø]yÿ `î endstream endobj 230 0 obj <</Length1 15424/Length 10186/Filter/FlateDecode>> stream xÍ{	tUÚè½uké½«·tº;Iwgë,¤éB `±@ÄH ¶$`paBdEQ¢28Ã¨d0 ²qÐqpFÑ!.øbô2Êûnu:3ÿüç¼ó^Õ¹}ï­úêÞo_*Bføagìè1yh2ªBûájÔØ©wNqÇ~ ÃØéwü8ñïÍq³àþWGÌÿB¼0Óî¬nMFHØ÷gÎ[8g1Ù¶ìo0ïû»æ-[âiÊüÍUÔÁ|ûüÅ~¹ú¿ÚÒFüÆsj#N¤ÝsÝÊÚù/>Þý· äSÌ)Ö}ræ^­pP)\0{´_Àü;Ç.\²ÂXçP¦æUóædÝs |
| --- | Minor | )Z±pÎÅìn.æ+`îY4gaëÍ,æ» ù«jLúÛGai ÿéâ{K/­å¯ÁüS ùDy¥C¡ ,¸6 |
| --- | Minor | 1½§A4±£ó&Í@Îyµ÷V"ç{K*³rÎEÈ	<£·WÅ%÷.B*:RkÐ^æ+ I4d2ÀS·½/¡ÿøè}äÆè£ÛîÀ¼÷yÚÑKÿ£õÿÓäÓ½û M	ã°ô6ùé§n½ùÿB¡h¢çvºÿnïÊ×åwÃ8$öÎéOÏ¹±®2ê­¸m·èùßÝáVÿo?Õëµÿè}¨ý'ü]¨ýFF°u²"@ÈºîmJB~ÒÁ®0Ü_jiÔv8ÄSïpãPõk iÃcR£ÛñWÁ:<Ê¯öSë÷tººÖÕÂztu=X£ÈÌ7°¶£ÈÛVÑÂþ`1Ú8ÅxàQüGññç,)EsQ Ó0¢` |
| --- | Minor | 5mü1~'( ¿Ó&Âïôúe|ÃzeÊ²sAù sÔçYè]Xò/SzMØ!0ò \<¬ÎÀì&lTÈ'Á £@Æ¡lÇ);{Ât~¾BSQ®	+È< ìôÀÞ³Öw«Ãs\ßõ¹åÀXwÙ¿C!XÚß÷[ãëýæónÁýÐãÜ&ý Wh¤¢ET_(õl(LRS6 àÔp? #¤Þq\Ö |
| --- | Minor | ¸7à2oÀ*¬?BµËävÃ4&Ôh>cìxp<Ç0!)! |
| --- | Minor | "ÑÖÖ²5hÇÉf'»E8áhâMW±¡qPnÐÑØP-ÑØ-ê½²¡ |
| --- | Minor | QïEê®"BmÖëê¨¹3[Öè¸3wè¨Ö±®·wá6kK°FÇOt¬Ä*U!¬Ðp«Ëde'`YQ 7ÇbiåSl²¼K|(S¹±8¥ª]GÉ"·. cQ±S.r£¸(V;QE±Ä `¬cXØ"K.¸óçir~æÍµËyæÄ\; oJÕ¸iKÞ9.80[G~&óuäùÝ2Oßg~7|³b¤ÏßÈþÌAnNÌ-ANvÌIAÎ9fÙIÈîY1!Õ349³3x34Ì9õC>-WN/Â4NlZ.2¹ËÔ1µ^GôV##=QfT!ÍÒSlìI«áäxÎIlºEi11pCRÇçÊÔ*g¯ãs¢c§#Ù$MIahn·Ô4háv#ypñòºt8¹s#óOèE<Åëp°G §#Al`NvæØ»Íê6 |
| --- | Minor | . Ò'-]l'}ìLdªv(U ÊÚ±Wñ[èÀ-ü·þ')	~ endstream endobj 225 0 obj <</Length 35/Filter/FlateDecode>> stream xc`Dõ¬4qÅ(£`Q@`Cá± D¾  endstream endobj 226 0 obj <</Length 252/Filter/FlateDecode>> stream x]»nÄ E{¾bÊM±b_JeYvy(N*+ÁBa\øï3ÀÆWsf.0Ã¯Ý­s6^õÀX§#Î~ Aâh;@[îQ9Õ$ãdî×9áÔ9ãYÓ §äâ »'í%>0 à¯Qc´nÝçµ¯¨_BøÆ	]k[Ðhèºg^ÄÀyßiÊÛ´îÉöWñ±SõKÊkP5Z-4VËÐéùKuI³_$Wª~eüx.8ËP5ã³. ¸ÈPµbQ±¸cAÿ}&ÿ#mkR-1Re²¥±Üu¸ |
| --- | Minor | ?ø]yÿ `î endstream endobj 230 0 obj <</Length1 15424/Length 10186/Filter/FlateDecode>> stream xÍ{	tUÚè½uké½«·tº;Iwgë. ¤éB `±@ÄH ¶$`paBdEQ¢28Ã¨d0 ²qÐqpFÑ!.øbô2Êûnu:3ÿüç¼ó^Õ¹}ï­úêÞo_*Bføagìè1yh2ªBûájÔØ©wNqÇ~ ÃØéwü8ñïÍq³àþWGÌÿB¼0Óî¬nMFHØ÷gÎ[8g1Ù¶ìo0ïû»æ-[âiÊüÍUÔÁ|ûüÅ~¹ú¿ÚÒFüÆsj#N¤ÝsÝÊÚù/>Þý· äSÌ)Ö}ræ^­pP)\0{´_Àü;Ç.\²ÂXçP¦æUóædÝs |
| --- | Minor | )Z±pÎÅìn.æ+`îY4gaëÍ. æ» ù«jLúÛGai ÿéâ{K/­å¯ÁüS ùDy¥C¡. ¸6 |
| --- | Minor | 1½§A4±£ó&Í@Îyµ÷V"ç{K*³rÎEÈ	<£·WÅ%÷.B*:RkÐ^æ+ I4d2ÀS·½/¡ÿøè}äÆè£ÛîÀ¼÷yÚÑKÿ£õÿÓäÓ½û M	ã°ô6ùé§n½ùÿB¡h¢çvºÿnïÊ×åwÃ8$öÎéOÏ¹±®2ê­¸m·èùßÝáVÿo?Õëµÿè}¨ý'ü]¨ýFF°u²"@ÈºîmJB~ÒÁ®0Ü_jiÔv8ÄSïpãPõk iÃcR£ÛñWÁ:<Ê¯öSë÷tººÖÕÂztu=X£ÈÌ7°¶£ÈÛVÑÂþ`1Ú8ÅxàQüGññç. )EsQ Ó0¢` |
| --- | Minor | 5mü1~'( ¿Ó&Âïôúe|ÃzeÊ²sAù sÔçYè]Xò/SzMØ!0ò \<¬ÎÀì&lTÈ'Á £@Æ¡lÇ);{Ât~¾BSQ®	+È< ìôÀÞ³Öw«Ãs\ßõ¹åÀXwÙ¿C!XÚß÷[ãëýæónÁýÐãÜ&ý Wh¤¢ET_(õl(LRS6 àÔp? #¤Þq\Ö |
| --- | Minor | ¸7à2oÀ*¬?BµËävÃ4&Ôh>cìxp<Ç0!)!. |
| --- | Minor | Sentence exceeds complexity threshold, split for readability. Applying the split needs --strength moderate or higher. |
| --- | Minor | none (split proposal only; source not rewritten) |
| --- | Minor | none |
| --- | Minor | Check: NEEDS-LLM |
| --- | Minor | Flags:    not-assessed |
| --- | Minor | SENTENCE (Line 51, 84 words, 0 clauses)  [Script] |
| --- | Minor | >Byh<f 2T	½ÕÆAó *¶ * TªÑ:>GõÊõÓ¬påGaßE­8àhÂàD­ü¬	÷>øù0oïBïw·ó1ò6³1d*¦*O4£V2eÉÛ¡¦<õ^Aè{Q.Â9V s	?öá÷Ð*Ôj¥Æ°ôr8çrï)çwèÊÎôZ9÷oÊÎã°ú¾Ðu§"2Ï |«kP9[§O9G+ôh`zØ?L/zùÌúðØîñ6¬  |
| --- | Minor | |ç¦ã 1r5*owM&ð:Ì«@zª'ø1>¡Ud¬0®5¢)ø"ìªpçXÂ`ä÷-LÂøâég³<¿Ë÷¦ùozDÁÓ¦¶èk=­½½Sg±..¿j! |
| --- | Minor | >Byh<f 2T	½ÕÆAó *¶ * TªÑ:>GõÊõÓ¬påGaßE­8àhÂàD­ü¬	÷>øù0oïBïw·ó1ò6³1d*¦*O4£V2eÉÛ¡¦<õ^Aè{Q.Â9V s	?öá÷Ð*Ôj¥Æ°ôr8çrï)çwèÊÎôZ9÷oÊÎã°ú¾Ðu§"2Ï |«kP9[§O9G+ôh`zØ?L/zùÌúðØîñ6¬  |
| --- | Minor | |ç¦ã 1r5*owM&ð:Ì«@zª'ø1>¡Ud¬0®5¢)ø"ìªpçXÂ`ä÷-LÂøâég³<¿Ë÷¦ùozDÁÓ¦¶èk=­½½Sg±..¿j! |
| --- | Minor | Sentence exceeds complexity threshold, split for readability. Applying the split needs --strength moderate or higher. |
| --- | Minor | none (split proposal only; source not rewritten) |
| --- | Minor | none |
| --- | Minor | Check: NEEDS-LLM |
| --- | Minor | Flags:    not-assessed |
| --- | Minor | SENTENCE (Line 51, 567 words, 8 clauses)  [Script] |
| --- | Minor | ª6!î³vó³4ÿÄ©³<-çÆ¯:¦h4\>táúÑiHHlZëÓòi¦8ªGQ^Ð#¾ÚÀ#0ñjw[p »ÀI4gÛxÚÙÆï¯_ÿþ±µkO/Äð<\/-[.7ÈÏÈûärê%¶ÀÊ«]N ¿_mÐÈüÅmÁ¾-YÌ&ñeEÐnËcëÖ=võúuùôÜr|?þ.Ä÷Ï](ûä=ò²V _Á¯£Ë@A¤ ÃªU3#¢U;Ì9°ìº¬}83 |
| --- | Minor | pÏ¬×U[¶¾1æØßü­ V(À¦¨~exDy.`ñÚ¼S³ O÷^Æo¡NÙèÁèÄÝm[,?uD<dssÅÜÜüè£.ÒW;B÷8L´Bè^ {à Ì`ÍÊÇÅ&=eJvÎ¤ÒÁS¦Î2Jb]ïe¶	4\!N² _b.ÓEÞfUóFm$¬{²«ýjØHR>ÅÅ*rE&eé/³q÷®]»iû^þ¾¿Eù»<<OÇ3ðT¹E~N~^nwáE¸ ïKå-òV¹¨ì§w0Ð R[±óÜdÂ³ãËT¸©Zàp[wÛ Ñ¼ÚfÊ1å@¿öAd¿ÉÅ[43f½ H°¨i{O |
| --- | Minor | ÎÔäÁê |
| --- | Minor | [0Z¦÷TI 7Ëkâ²2M^Ã¬ü.®|³åì_{°£«NÑ&¨£Ø)e,yuVdÔ£%L±³+Ó/7Yõ:;Ò`;¯2hDlÖFWÛ.t\ ~rr@'2:¯uÊ" ´y<m.Ïgã@¿âLÃqfµYÁ±7pÈÂÃqÖÀÄ¸Xó+.^Áù:ySµ´{~}Çê'nÚÃVcMNî_Ï|(·Ã½VyßBÜ¶ãwØLåzàÛø2]öJ	L±Z£ÆÅz2ÖèPA¹MaT,LzbÔª³xõB.°8ðÛ»s/ävÃl)9àóá5ÆG=jÞc !NlÑÍ¸{bþgÜ |
| --- | Minor | +6Ãâ°©ÅN<Ç,ÏD0IAÌ`ÍXfF(DØ¤î£ÀkÊdÞr´gÖw=KÍgq´|ù;ÜEÝ_È|9NXH®vk*ä©\^ ý­íFÏK	^á,áÅ%Æk	¸Çåh®®Èmb41ÈÎ«cL#ã}á´QÙµú,Ün73±E=RtB¨P0%tSÑ5 Qh w!ÎÄò=3nù¿q¤üy/ZðAuµúmOøõÞ |
| --- | Minor | ÷öÉ3âãå«_}#ÿ=c7ïxçµ3ç¥QL'ýàÉÅ¦Ð<)Vø#*±¹+cjãJ\e¶¢D&&ðfWsÚD`IÇM+ï½}¸Ô:µÞÄÈIeÑYô¢A4¢É¬KÖOqOñLñúð¶Y#HQqsð#ì¶¸ty²q×®Æ¦»^ý\å_0¯\é¿Ã#qÂ/Ü]­{`ÑyçÏ9ÿ»Wßxùnâ î2¸Z|^_¹VR.ÿØýhö qºW&40c4ÜÞra.8õñ¬°Ãd§º|µ£O¹°+ªùªáì'_z]­ÞW®±ãHÂªÁ?xmq&/û`Oë£LZÏ¥ä"WÕµÐ>ò¾1ìO3Ðp)6>ØÔ%1Æ²¢@|¤ÎÌùt\â]6÷yµæÕ>oÑçhßï¤Q¯« ¤ßXÁ6+5pPv:8°'¯ì}ä½´%?¼²~ãÆúW8!_»þwùo'~³ó©ë.] ïj>t¨ù©CÈ²õ»v­ß°k×9ûÛ{ÿtùòö¾mw\äüù#ëR=º?Lô¨PGNO	±Tkí%Fâ,Q­3âã8-7GðTÚÀ?DX¢K.7v3nâfÝ;Æív{Ü^wìËë¾@CPÖÀp0¡¥÷ÑFNzaá'r/¶_éÁFùühÎbýÏOlÞ¹sóæ»'&NÀº¯.c¼N~Z^!O¹^RØXP®wÎrÑ¨'ïª¸§AÆÑBièÈÇø¦ÄëÐÄ1IñD?¦N=±ÎX'ñu©êu©ÙS|IfÃ8?B\(sô0>*Æ5l 3ö"÷t@§YàÐ¥ÜN ½ |
| --- | Minor | ®ÑËá.@)MIÌ>Oqõ¾Äxjõ<c³í,Pmç©|}LÖ@sö xvº8ÕO8ÃÐmÿüçÛî9p|ô¨rùü-3ßü´xöBúüýeUÊÏ¼$¿¸êþ5kW7àü3ïã9Ë'M_¿ÀM5µëÖ×Ý»ùú´©]çÎýcê´ÍÝÝ	]Ç«ÎÎXÓè+×ýýYùËËWMWX¸¦¾}µç5Ü·~ÿ¹_¬¯Êçn*[õøÁ'÷|4¦÷*Tym2àø~h4g1ÔxÙÄ×Ê%ÈE`¦Õ1zQ¥&3¼¡ :a«ø¹b½V%Àé-jb 3D-)ºa£Áhd¸$>IdðRÍ?öªqV&Ó¡xI¦ |
| --- | Minor | ?ÆÄË=ãd¬¿blÛz>Û¿ªgÓª}L4söèr®¢ëÑòr<NnUòÞËÜ>°h4Xr9!"6­te¤(Æd4&FûÝ N©¥÷ó´g;GDwT<úMÖn ùMH´¨BpûFÊç:·vÍY¼oÅãë°uouÂ_Î}{íÚ·Ï~Àÿx±xÎb}ÖßH#ä_? |
| --- | Minor | ª6!î³vó³4ÿÄ©³<-çÆ¯:¦h4\>táúÑiHHlZëÓòi¦8ªGQ^Ð#¾ÚÀ#0ñjw[p »ÀI4gÛxÚÙÆï¯_ÿþ±µkO/Äð<\/-[.7ÈÏÈûärê%¶ÀÊ«]N ¿_mÐÈüÅmÁ¾-YÌ&ñeEÐnËcëÖ=võúuùôÜr|?þ.Ä÷Ï](ûä=ò²V _Á¯£Ë@A¤ ÃªU3#¢U;Ì9°ìº¬}83 |
| --- | Minor | pÏ¬×U[¶¾1æØßü­ V(À¦¨~exDy.`ñÚ¼S³ O÷^Æo¡NÙèÁèÄÝm[. ?uD<dssÅÜÜüè£.ÒW;B÷8L´Bè^ {à Ì`ÍÊÇÅ&=eJvÎ¤ÒÁS¦Î2Jb]ïe¶	4\!N² _b.ÓEÞfUóFm$¬{²«ýjØHR>ÅÅ*rE&eé/³q÷®]»iû^þ¾¿Eù»<<OÇ3ðT¹E~N~^nwáE¸ ïKå-òV¹¨ì§w0Ð R[±óÜdÂ³ãËT¸©Zàp[wÛ Ñ¼ÚfÊ1å@¿öAd¿ÉÅ[43f½ H°¨i{O |
| --- | Minor | ÎÔäÁê |
| --- | Minor | [0Z¦÷TI 7Ëkâ²2M^Ã¬ü.®|³åì_{°£«NÑ&¨£Ø)e. yuVdÔ£%L±³+Ó/7Yõ:;Ò`;¯2hDlÖFWÛ.t\ ~rr@'2:¯uÊ" ´y<m.Ïgã@¿âLÃqfµYÁ±7pÈÂÃqÖÀÄ¸Xó+.^Áù:ySµ´{~}Çê'nÚÃVcMNî_Ï|(·Ã½VyßBÜ¶ãwØLåzàÛø2]öJ	L±Z£ÆÅz2ÖèPA¹MaT. LzbÔª³xõB.°8ðÛ»s/ävÃl)9àóá5ÆG=jÞc !NlÑÍ¸{bþgÜ |
| --- | Minor | +6Ãâ°©ÅN<Ç. ÏD0IAÌ`ÍXfF(DØ¤î£ÀkÊdÞr´gÖw=KÍgq´|ù;ÜEÝ_È|9NXH®vk*ä©\^ ý­íFÏK	^á. áÅ%Æk	¸Çåh®®Èmb41ÈÎ«cL#ã}á´QÙµú. Ün73±E=RtB¨P0%tSÑ5 Qh w!ÎÄò=3nù¿q¤üy/ZðAuµúmOøõÞ |
| --- | Minor | ÷öÉ3âãå«_}#ÿ=c7ïxçµ3ç¥QL'ýàÉÅ¦Ð<)Vø#*±¹+cjãJ\e¶¢D&&ðfWsÚD`IÇM+ï½}¸Ô:µÞÄÈIeÑYô¢A4¢É¬KÖOqOñLñúð¶Y#HQqsð#ì¶¸ty²q×®Æ¦»^ý\å_0¯\é¿Ã#qÂ/Ü]­{`ÑyçÏ9ÿ»Wßxùnâ î2¸Z|^_¹VR.ÿØýhö qºW&40c4ÜÞra.8õñ¬°Ãd§º|µ£O¹°+ªùªáì'_z]­ÞW®±ãHÂªÁ?xmq&/û`Oë£LZÏ¥ä"WÕµÐ>ò¾1ìO3Ðp)6>ØÔ%1Æ²¢@|¤ÎÌùt\â]6÷yµæÕ>oÑçhßï¤Q¯« ¤ßXÁ6+5pPv:8°'¯ì}ä½´%?¼²~ãÆúW8!_»þwùo'~³ó©ë.] ïj>t¨ù©CÈ²õ»v­ß°k×9ûÛ{ÿtùòö¾mw\äüù#ëR=º?Lô¨PGNO	±Tkí%Fâ. Q­3âã8-7GðTÚÀ?DX¢K.7v3nâfÝ;Æív{Ü^wìËë¾@CPÖÀp0¡¥÷ÑFNzaá'r/¶_éÁFùühÎbýÏOlÞ¹sóæ»'&NÀº¯.c¼N~Z^!O¹^RØXP®wÎrÑ¨'ïª¸§AÆÑBièÈÇø¦ÄëÐÄ1IñD?¦N=±ÎX'ñu©êu©ÙS|IfÃ8?B\(sô0>*Æ5l 3ö"÷t@§YàÐ¥ÜN ½ |
| --- | Minor | ®ÑËá.@)MIÌ>Oqõ¾Äxjõ<c³í. Pmç©|}LÖ@sö xvº8ÕO8ÃÐmÿüçÛî9p|ô¨rùü-3ßü´xöBúüýeUÊÏ¼$¿¸êþ5kW7àü3ïã9Ë'M_¿ÀM5µëÖ×Ý»ùú´©]çÎýcê´ÍÝÝ	]Ç«ÎÎXÓè+×ýýYùËËWMWX¸¦¾}µç5Ü·~ÿ¹_¬¯Êçn*[õøÁ'÷|4¦÷*Tym2àø~h4g1ÔxÙÄ×Ê%ÈE`¦Õ1zQ¥&3¼¡ :a«ø¹b½V%Àé-jb 3D-)ºa£Áhd¸$>IdðRÍ?öªqV&Ó¡xI¦ |
| --- | Minor | ?ÆÄË=ãd¬¿blÛz>Û¿ªgÓª}L4söèr®¢ëÑòr<NnUòÞËÜ>°h4Xr9!"6­te¤(Æd4&FûÝ N©¥÷ó´g;GDwT<úMÖn ùMH´¨BpûFÊç:·vÍY¼oÅãë°uouÂ_Î}{íÚ·Ï~Àÿx±xÎb}ÖßH#ä_?. |
| --- | Minor | Sentence exceeds complexity threshold, split for readability. Applying the split needs --strength moderate or higher. |
| --- | Minor | none (split proposal only; source not rewritten) |
| --- | Minor | none |
| --- | Minor | Check: NEEDS-LLM |
| --- | Minor | Flags:    not-assessed |
| --- | Minor | SENTENCE (Line 51, 371 words, 3 clauses)  [Script] |
| --- | Minor | ×Kr«üüÞ'¿j¥þ~¼Ò4)Åf1ÞoZ­¿_+¨W*n.®²¬ÖÞ7TFÞj`Q¼Ycb¼4ù¶i.s¡#HS/(ºÛÄv¹]l	8ît æ ÈqCÑæ |
| --- | Minor | i_}â{¸¾g¾R_/ÛõåªüQÖÅc=M 0nÙ |
| --- | Minor | [1³àª0bVÊhàû#ÖÖ!¡uv!ÉR0ü>6ÍÙúáXlooÅå¾ò0&L+`¢EÙUÃW©æ²¨QãxdH<ç$»=ØÝ%¡Á¤è§êôõ«õ{õ<.LPôîhÃ]'z^>q{¢¼îV¦Õ |
| --- | Minor | ;èQ@rjÕ%R½W!>^¥1ê>ÅOe»Ø®Pv­3ÜÎì[··°0s@áiÅ¦.y#¥à9ðÙ&c4´'Þ+juÚ7íu:íd­Îãe#pæ"_D­Ø¹È\æ+JñhuÞhÝhcHlâ£I¡±éB;øósëO4E;ÁCægøálML¥¶¦õ¤R§¦.N]ÊÞL&¶XÜ)E	°)(¥/wZ¤IÖÒ´"ÙìIö&ÇVçhhèès91CÜC<C¼9±ãÆkÆk'èÆëÇ¹Ç{Æ{ÇÇækòµùº|}¾'ß[®®ÔTj+uú w¥§Ò[[W¯©×Öëêõµzw½§Þ[[ÝÚÊågì}©W¦Á4ºæñQ7ëÆJ´t¢;vòð±ê£¯¿®^ßTm:ôÛ'¹òÜËo=/-Sß;ªÏ4®«\=tÄ_øSZª|æÉÆûë+êr³½º÷ÒGA*%+hÁHÐ#ª\jNKª¹zPQÅyC¼JgBñ<#B(iïnk§ì§¼*ç¶}¹¨°PDbÝ&Ü/!§Jv#RÈµ¦"S©ÙtÒÄ*97U§°àu'åñõ\z½<þd9{õ .¯ü +§¹À|Ð«ìh¨ÒÐ}RË«uYâ:Ç6UÅ»9®1¦)q¥HWg`ò¦ÅêýN#òi9glDJ²¢FÁ`{_Ìèl;¯}!jCÒcÊG.Å)U)+N¥°uI§ð)æicÛ¸6¾ÍÖÑf?yÊqÊ	©B!Îºÿ,&jn7Bª·/}Î¢YhÉøfÃÚõKj[÷Éû5Wz§óf¶­Yô8»è·3?þOùlY]Õññ?×LÈ;ÞüË£ãk×Ï½ü!¥z(PÝÊ[A^^4VJðr&A1ÛUÛ |
| --- | Minor | ¸T£:CjÙåÔfY¿ÍÄúP z&pMÔÇgt´+¦"RSÉ	nÃÈV¸M4Û¬õø@îËq(ipÙ gëÛ®_o«v¼mÛÔ¸eKã¦måTÞ³°x¶üfW|nvñþr¼ôÔ¹¿~ôñ§o¤zE¥ |
| --- | Minor | ¢,ÉvÛ~§îQSz)rÒtNduò).~A	BÝAp«¢ ·pFúþ&@ãíû¤å+H_ü®¤ÂÖøà£»vîX¾Ùï8pgÊ¨ÈÈßmZýå_|µrUXg.¹w§ÁÀ=Çv½{»`ª³ ÷"ý&Æì·Äý(+Ê©I¡ì» ¥gnûØ'©Q××Çý,Å&H!l³¼·äFlf¼²ñ×_6¾ç·nÛ´yËÍÀÆòýÅ³qvW4»I.ÿá­²o~úñG=Æz&ðÐ\hÃ¨luHµkÒE6¡ÇÍtEQ*µÍ\ØiL¢ÂØøû+)'ÅNªËfO´ÝMÎ£óø<sÞvÞÅQÍõÙ/ß. |
| --- | Minor | ×Kr«üüÞ'¿j¥þ~¼Ò4)Åf1ÞoZ­¿_+¨W*n.®²¬ÖÞ7TFÞj`Q¼Ycb¼4ù¶i.s¡#HS/(ºÛÄv¹]l	8ît æ ÈqCÑæ |
| --- | Minor | i_}â{¸¾g¾R_/ÛõåªüQÖÅc=M 0nÙ |
| --- | Minor | [1³àª0bVÊhàû#ÖÖ!¡uv!ÉR0ü>6ÍÙúáXlooÅå¾ò0&L+`¢EÙUÃW©æ²¨QãxdH<ç$»=ØÝ%¡Á¤è§êôõ«õ{õ<.LPôîhÃ]'z^>q{¢¼îV¦Õ |
| --- | Minor | ;èQ@rjÕ%R½W!>^¥1ê>ÅOe»Ø®Pv­3ÜÎì[··°0s@áiÅ¦.y#¥à9ðÙ&c4´'Þ+juÚ7íu:íd­Îãe#pæ"_D­Ø¹È\æ+JñhuÞhÝhcHlâ£I¡±éB;øósëO4E;ÁCægøálML¥¶¦õ¤R§¦.N]ÊÞL&¶XÜ)E	°)(¥/wZ¤IÖÒ´"ÙìIö&ÇVçhhèès91CÜC<C¼9±ãÆkÆk'èÆëÇ¹Ç{Æ{ÇÇækòµùº|}¾'ß[®®ÔTj+uú w¥§Ò[[W¯©×Öëêõµzw½§Þ[[ÝÚÊågì}©W¦Á4ºæñQ7ëÆJ´t¢;vòð±ê£¯¿®^ßTm:ôÛ'¹òÜËo=/-Sß;ªÏ4®«\=tÄ_øSZª|æÉÆûë+êr³½º÷ÒGA*%+hÁHÐ#ª\jNKª¹zPQÅyC¼JgBñ<#B(iïnk§ì§¼*ç¶}¹¨°PDbÝ&Ü/!§Jv#RÈµ¦"S©ÙtÒÄ*97U§°àu'åñõ\z½<þd9{õ .¯ü +§¹À|Ð«ìh¨ÒÐ}RË«uYâ:Ç6UÅ»9®1¦)q¥HWg`ò¦ÅêýN#òi9glDJ²¢FÁ`{_Ìèl;¯}!jCÒcÊG.Å)U)+N¥°uI§ð)æicÛ¸6¾ÍÖÑf?yÊqÊ	©B!Îºÿ. &jn7Bª·/}Î¢YhÉøfÃÚõKj[÷Éû5Wz§óf¶­Yô8»è·3?þOùlY]Õññ?×LÈ;ÞüË£ãk×Ï½ü!¥z(PÝÊ[A^^4VJðr&A1ÛUÛ |
| --- | Minor | ¸T£:CjÙåÔfY¿ÍÄúP z&pMÔÇgt´+¦"RSÉ	nÃÈV¸M4Û¬õø@îËq(ipÙ gëÛ®_o«v¼mÛÔ¸eKã¦måTÞ³°x¶üfW|nvñþr¼ôÔ¹¿~ôñ§o¤zE¥ |
| --- | Minor | ¢. ÉvÛ~§îQSz)rÒtNduò).~A	BÝAp«¢ ·pFúþ&@ãíû¤å+H_ü®¤ÂÖøà£»vîX¾Ùï8pgÊ¨ÈÈßmZýå_|µrUXg.¹w§ÁÀ=Çv½{»`ª³ ÷"ý&Æì·Äý(+Ê©I¡ì» ¥gnûØ'©Q××Çý. Å&H!l³¼·äFlf¼²ñ×_6¾ç·nÛ´yËÍÀÆòýÅ³qvW4»I.ÿá­²o~úñG=Æz&ðÐ\hÃ¨luHµkÒE6¡ÇÍtEQ*µÍ\ØiL¢ÂØøû+)'ÅNªËfO´ÝMÎ£óø<sÞvÞÅQÍõÙ/ß.. |
| --- | Minor | Sentence exceeds complexity threshold, split for readability. Applying the split needs --strength moderate or higher. |
| --- | Minor | none (split proposal only; source not rewritten) |
| --- | Minor | none |
| --- | Minor | Check: NEEDS-LLM |
| --- | Minor | Flags:    not-assessed |
| --- | Minor | SENTENCE (Line 51, 151 words, 0 clauses)  [Script] |
| --- | Minor | qf¨b°âFlÔÇD+$Îy©aæLs¦Dc¥fÇ½ÌpnKªçàéw.å=Ïµ´´¼üâ¨µ#9ÇÄ)Õ[6Tt¿P^N¦U¬9|4Ò¡ø9½\w#?/eú!O³Qê¢·[TO º&6n»|ûDô4uã÷D}(+Ñ)dG¤¤JÅÇ4::Ú©ê|òEX}2³¢BébzCzK:¨6)¯ÅÂÆ a¸¿:Aí_}e±ÝWÊNÍ*2¯]õôÎZKå]}ZEwßýù?ÿRZôR[ÓMÛ_!o «×©ÄØNX4ªüN« Çö5RÇU»Ìë4DdfòóF¿Å§Âú¼ù@%0Á·]lWò¨/ìÁîÎÐK¦ÀÑw»ÅMnÊ.F]!Ùõ¥Es´%"&3ö·àÒÌg*[öïÙ½³ëV¯mVÜÍÌÊEo¾ßs¶¼A¯5½rXv*ñ ¨`¸Ë)ÙÐxÉNÔæ:ëP9"¼Þ¯ó®¡téâ Ý`' ]ö~Ú¡`gCK¿×Ô£2ÒGÌÈõ¿^èùº°äªÓGNÏ9ò ´ýÐ(Hhà!q3Ãû^è¹r¼1Íß¤rÔ'=ÐÓh´XJôV'KÂòÛó?ÙþÏöß_Q-°æÕ~ÒÛrìÅ°ô¨+*è[TÉt|umÄi­Çvó­/µ¢À£&úýßôØûÍÒí;wnß¾s×6! |
| --- | Minor | qf¨b°âFlÔÇD+$Îy©aæLs¦Dc¥fÇ½ÌpnKªçàéw.å=Ïµ´´¼üâ¨µ#9ÇÄ)Õ[6Tt¿P^N¦U¬9|4Ò¡ø9½\w#?/eú!O³Qê¢·[TO º&6n»|ûDô4uã÷D}(+Ñ)dG¤¤JÅÇ4::Ú©ê|òEX}2³¢BébzCzK:¨6)¯ÅÂÆ a¸¿:Aí_}e±ÝWÊNÍ*2¯]õôÎZKå]}ZEwßýù?ÿRZôR[ÓMÛ_!o «×©ÄØNX4ªüN« Çö5RÇU»Ìë4DdfòóF¿Å§Âú¼ù@%0Á·]lWò¨/ìÁîÎÐK¦ÀÑw»ÅMnÊ.F]!Ùõ¥Es´%"&3ö·àÒÌg*[öïÙ½³ëV¯mVÜÍÌÊEo¾ßs¶¼A¯5½rXv*ñ ¨`¸Ë)ÙÐxÉNÔæ:ëP9"¼Þ¯ó®¡téâ Ý`' ]ö~Ú¡`gCK¿×Ô£2ÒGÌÈõ¿^èùº°äªÓGNÏ9ò ´ýÐ(Hhà!q3Ãû^è¹r¼1Íß¤rÔ'=ÐÓh´XJôV'KÂòÛó?ÙþÏöß_Q-°æÕ~ÒÛrìÅ°ô¨+*è[TÉt|umÄi­Çvó­/µ¢À£&úýßôØûÍÒí;wnß¾s×6! |
| --- | Minor | Sentence exceeds complexity threshold, split for readability. Applying the split needs --strength moderate or higher. |
| --- | Minor | none (split proposal only; source not rewritten) |
| --- | Minor | none |
| --- | Minor | Check: NEEDS-LLM |
| --- | Minor | Flags:    not-assessed |
| --- | Minor | SENTENCE (Line 51, 1238 words, 14 clauses)  [Script] |
| --- | Minor | W®`üeÞ×ííW®´·=¼òdY~FUy&Û »ëPºKòcd&zv»S_g©óh¶[79<÷Ä»ýHp-üÑ"òéñ7+å`o# |
| --- | Minor | 	´²õ§¾>¦õÅÛëð¾¾¨ÚzK¼¥"gÆÃêo+öß·²KÉá©Ï}ðDJ±*µÃÈXgB\Ä&½ºÎ´G«Q1iHôU>ßpäÉ|[¨LÏ«Ï*o°¥ÁaH_³ÙÄÑ.Ff8%$aÄJÜh!Ù¥H}ÕE=ØÃð7Å¡( ýK}øV_ä6Ý,FB	Ñ»åÜë·¼×ó6ÕAêÒæ±Éòµ;§oÍ('3Ê^­ª0ëYrhLF¤J1<\F×Þ,#BÍ\/â)[³ôçffnTùlyñLùé2¢»¾èºv{ÑWEx*bÏíóø¼¾X_\¦@[ +Ð¸<ÞØYqkÝk=k½kc×ÆípïðìðîÝ·ß½ß³ß»?v\´ÚzÐzÐv0â ý`äAÇIëIÛÉö'ùgeÞù+Ëv[æO}QM9ÛøðÊfï^³¡þýWg¼2¯]¿tÉòu[w®ùò­mC¯/_V7s@ÿ¡ù[÷ûS¾Z°dÚ´Q?KIËh¬Úù¼rrIâãªÁâJ¥h»ú&+«Bu<³ÇZ)&ìWs>2Àör©Âü>Ä%·²ò·Lß±À#Ä?EöÕN6NàT6Á¦JUGc¯CShpl ½Rïw$f}üôÓ/ãyÿÀ¼q#ªÍ[ö>DWà	òÑÂuî½emã¯)ÎÙà'>¬ÖJ±v¯Ó[5êH0T´G]Ä"¿0öã!¿èÓe8iÕJ·öÐ:À0¡àÔ÷§¹9û^«6¸Z\Ì |
| --- | Minor | *ì¤`!MööKðØ²kSóõüXæÓÝg+áõu*?^^uî"SÑóèG¿/#ÜÛ>»¨0 V)G£fT{õ½°Ð |
| --- | Minor | ô5áÓ·ÈÒ©8êÆÉdÐ«UÏb¤6jãwO@=hêÿæIyÍzÕdêª4TuÇñBà<Âta°LT*ÚÅº8Ú¦I@)l ¢NÑ¤£8Õ5üÍ2,@¥eì2n9¿BµB½B³BªêÅJå¯uwÉµµøÊS÷â¦år-È¯¢'ù°¢¢{4R¼ï4µEZ`ã^«Íj ÂmÐ |
| --- | Minor | Ðk·á*@3x´×ècd°9kxDm²Í  Vå \ 4àB)Ç£üm­CÑ JëLæ¡	!×¯¢oj5»Ëð Ì FÌ%ó`*ZÁ"§3wqS¹»ø©üta¦f¦¶C6ZÄËÐr¼¹ÜÇ.áðµêºúZÃRãRqiskYT°Ë¾ÕÓWàWòä[¬Ë¬«Ê¼ÏÉÍõÚ!ò>[ûaÆÊ»Eã[££6wÀ}È¼²Jjæ^ÄâHdgE%ºÐ¡üuÿÇtÉÌ»OtKO7*l¥ßù¢ÅlÉD1á×_Ùß,w4ôtMvâ¿2Lz¾×ötvz×èBí-¯½&l¸VC÷o­°âeE]0³pMÃ¶·ßy¤YØðu÷/åËV¹ÁL"	~nÃ Î4[Ì&ÓØP w7ï¥"baÌ¸1È==ïÈ1Ýe_#Ì4*Ïm ß)AÊa © *Ê`ýqÉ!qtQ¦ñµæGÞi~k[Eæíe³|?;ð¯ÉÝJ~ÝÛË§@I´	iñü¾øAýQH°¦Yvú,Ô_+õ«dÅ¹í7kZÉíÔ±ñXUç·ÄìMcu !BÖåßÉAúB.Cÿ~îYª4Ç	?*em7êÜ]è+|É9Tå¶¹vd3mêüÓoä(9û×¾o*åðC7Je®48p"­Q(RÊ>mrWG@¡¡©sªöXu´¶f´ø£OëGjÍo|.{ .C/´AÖEN¥àP¾YêKj1>#¾*¾9½MÆ)>7ÎpöõfÌk}6ãRW¿{3óM{þK)ÓZ¾þüçGó9Ï¼kóîbÌ@sò¢×çtõÑèPjá¥RºÎ¥²ëôª:Tm3Q7ãÐï±°jdà	4Ë0û |
| --- | Minor | ¢Î#­~g­¦@öôcvúÊ_ùËé |
| --- | Minor | ÃäÝîæURÝ é'_c0ãÆ=WZ.>³ûäK!ª¾å­]3i9øÀÅ}o1Îµ!åKT¤Ò 5CÑ&)!Ãæ¦ |
| --- | Minor | ÁÙþ,_üPàÜÛ¸-<j§¥ªÒá¬[u8=sÐPiñPã¢ÇG3¹¸øìÇýOL>îy·ßÛÐ+&MíeNÿXµY_º]	[y	×[P­ 1Õu¤:o5g1ÛÕþÓ²;ü[Öü´~K=ïý+©ß^ý¾ü [¹Í®éíbDÚóGÐ%.-·6¦öÜAXwf¨©rÐ8Õpå[×¾# |
| --- | Minor | 1c<Ìâ ¥äìPöK®;Â3üX~ÿ+¡^¸ ºSõ¬ªS=^Ý¬a5µ´ñÚYÚcÚ.]î÷ú¥úó á9ãq¾¸JÜ-îÏ&©ÑÔkoî±<¤p}(£F©hò}¹vÓoûY-þæô³RÐïYúíî	å;_:¦EÜð~ù~xLú]gû9ó(]C£PZÞÊhòó<¨Û=(pfÂh.@xÐHYj ÝJÐ´ùáêx´àÓa4UÂéAÓn¬U£ÌJ /gÁo1@jÐhÃ 3ÑR°s` ¤Æt}¬²~Ì\X·à<ð|ì;G¹wû:Ó]Ê@_GTªëôJ |
| --- | Minor | \«RÖ ÂîôîæS¡ÿ£÷>åÛ÷C¡ÿ3Aÿ"ôÿ¡ÿ~°ÿgÃµFWþs#øþ)öÚ5<üxYÑ$t'úpf:ºp² |
| --- | Minor | £»Ñ/Ð·7ÌbóXÀ*t Æj¬.*fæ÷£Âýèp?&ÜçúÚçôõá~`+³Zúô |
| --- | Minor | µ×Ûâ¹×ÉëÛO^Ó3§}ÜbrÚGN«Èq-9¦%¯¼lå^	­¤5H^ÉQüV&/Êä°Lµåu±ä L^XEÉsò:î7Vr@G~ O¤=ëc¸=2yü1{<<&Ý»Üî²àvÈ.Ý	î´«Ù²CbM Û pÛe²m«Û@¶nÑs[-dk+ gÑGN±MU«¸¦cdóýZn³lØF5!6ã6ÉdãÃÜÆcdãjöá |
| --- | Minor | äaÝ xmH ë×¸õ1d}kï)©]g"k`ë5Åä¡ y0<°Ü¯%«¹Õ2i¨¹¹o»/HVÈÊz#·ÒBê¤n©5²|[ÞE-âyÈÒ(²ZCjdr¯Lªë¹j,ÖÅ[µ,Z8[TA':®R$«Ù ©ØrØ²¼ãÊdRº +=FJW³æ'p É@J ¨¤y62W&sdR4;+ÉìtrL eòäîU¤@&ù£É,ü\&3»d2½L³ÉÔ;ÜÔUäN#2BI&iÉb2>VÅßAÆÉX"rc- g°Ë1Á&­'d5ÐÊeÉd`¦h%A |
| --- | Minor | i!Áj.¨!Á|¨I #&é6.#dbÓc4\º¤¯fÓÔÅ\ÚâOµrþ$HµTMÔSIrRKA ±¤ ñAçIâ ä I|Nâà±83ØXñz"9o!ñ¸M'xN±nØÌm"îÕlÄHlt2W<q:s:qÀª 6µË 6«³U«ÅÂY­Ä*±1ù1{M2¡G#àoÜApÏ =,  ,,Æ¦XÑ< àV\¼¦§þ{ ÿ×üË²¨ÿõíé endstream endobj 232 0 obj <</Length 145/Filter/FlateDecode>> stream xíÏÉNBAÐ2 "8òÿgçí0a6ç$U·»RîänþÜk¹­²F%ïÒJ»d'÷é¦~'û>*5Î¤<V}z²5ËÓÙ<gE^²ÌkVYç­¾úÈg6%·ùÊ.ûÊù;?ý                ®åø*f endstream endobj 233 0 obj <</Length 394/Filter/FlateDecode>> stream x]SËn0¼ó>¶ð2ªôÂ¡öå@ð!9ð÷µ=6£Ù]ïuxª^+Ù/,üTc[ÓÂº^ EóxW-±+ÝzD1}»8f¿íÐLA¨ëu^h¨d7EÁÂ/mÎZÙÓ¯ô0ÆÂ%HõòÆ~N5¤ú>M¿4\Ø>(K&¨ÓåÞé½6yW	í÷ËºÓiïu"[¡¥v4OMKª7 ½~JVtú)âåH»v[|lâgàÅÊÈG'onJÎuTxÕ%¨Äò4ò*RPw§rÀÁÚÌõÒ 7M8SîäÂ=ºfRÆ3pZ9ÃY ùA­Ë1'wµ<å£i9¦årè»¸ës÷÷åWmPCs7´§è!GyæcÓs×ýj7#Sp^Ì²ù­2{g.É¶Ôí])½Ïö&ÙE6+ÜKÚ.Û4N&Ë¼:³é° endstream endobj 237 0 obj <</Length1 2956/Length 1931/Filter/FlateDecode>> stream xÍV{PT×ÿîý³À.»ì²À5°äé¢ï\ê³JÄZ´YX·¬¢k6QÆñØ$NØ±iº'ÅTûN'còG§q:¶ÓNÇvÚþá´~{6ôßö|sîù¿ï÷}çÞ¹s)Dä¢(ÖÕûî¦·)<icKO L.=Äö/ÙÛ²«_?Qyù/DI÷Øw&nëù]ôO7TÁñ¡¶@_XÈe;µ­{ ùôm¢l¶·sîüõ?ð|¬ËÓ`®|¶óÛ{ú÷hDÙ`ÛÝÝÛ vpþA~Ø{{Â¢X÷³m}[ §Uÿpá;±ïb¸·¯§-\Çgw´wØþÆýq}ùÅ÷ªn:?påÒ­iÿJ¹ÉqrzçPÎ¾¯3þñûýäx¿É¤Rbp^RMäÉî÷-¦ay#aÙ*¹é|üMU&8l |
| --- | Minor | ÜG¥<ÏfNbÅm ©é`³AÚ¤ªèÔu¡Ú ºW÷Ú4SS.$õ(¿IôDV­ÂzwV×à©ñS±VAº¶ºÔ½SSç¯ï%X^·IU¡Ý=¦úVÇ'ônUZò©»ô1ªsè±©©ºñÜ4&gÁ<&|yw>-x§´du]>ö³ÚiÖÚ¦öÕ7°·ØÍþÚR©QãÃø±7oäËAÜ4Ä|üÈ·®È·¸^Fü0k;põ |
| --- | Minor | ^õã |
| --- | Minor | ?~`âuß7ñ=WL¼:¶\¾zcËñ]ßàÛ&¾åÂåÑTyYÃh*¾éÇ7øz.ùñÊËAùxiØ%_òad]øðÕÕø_.ÃÅÃ9ò¢/¸åÙ¸àÆùs.yÞs;çÂ9CåÄ³ÎFÅ°ÃøgVÈ3&^8í/øpúSöâtL1qê¤]râTL!c¥8iÇÉ	q¢7"Oãø³yÜã8ÆÚ±x~h\>obèh£ÇPT=âGqÔG¸¯#>>äsp865aLCréÁ VàÀCxnÏ: |
| --- | Minor | eÔÄ3ÝnùLöG\r¿öíMû¼Ø§1àÁ;vïÒåîûØµs¦Ü¥cçLôsRúLì0±=ìÛM¢7m=Kå¶.ô,EwWªìv£;*ºRÑeN.Ùyíã²ÃD{[£lG{T´|²­mùÐÊ ÖûÑfM[Ëd­exÊD£-«ñÅ6ØT_0±q7QÄz |
| --- | Minor | ·.MÖE°. |
| --- | Minor | W®`üeÞ×ííW®´·=¼òdY~FUy&Û »ëPºKòcd&zv»S_g©óh¶[79<÷Ä»ýHp-üÑ"òéñ7+å`o# |
| --- | Minor | 	´²õ§¾>¦õÅÛëð¾¾¨ÚzK¼¥"gÆÃêo+öß·²KÉá©Ï}ðDJ±*µÃÈXgB\Ä&½ºÎ´G«Q1iHôU>ßpäÉ|[¨LÏ«Ï*o°¥ÁaH_³ÙÄÑ.Ff8%$aÄJÜh!Ù¥H}ÕE=ØÃð7Å¡( ýK}øV_ä6Ý. FB	Ñ»åÜë·¼×ó6ÕAêÒæ±Éòµ;§oÍ('3Ê^­ª0ëYrhLF¤J1<\F×Þ. #BÍ\/â)[³ôçffnTùlyñLùé2¢»¾èºv{ÑWEx*bÏíóø¼¾X_\¦@[ +Ð¸<ÞØYqkÝk=k½kc×ÆípïðìðîÝ·ß½ß³ß»?v\´ÚzÐzÐv0â ý`äAÇIëIÛÉö'ùgeÞù+Ëv[æO}QM9ÛøðÊfï^³¡þýWg¼2¯]¿tÉòu[w®ùò­mC¯/_V7s@ÿ¡ù[÷ûS¾Z°dÚ´Q?KIËh¬Úù¼rrIâãªÁâJ¥h»ú&+«Bu<³ÇZ)&ìWs>2Àör©Âü>Ä%·²ò·Lß±À#Ä?EöÕN6NàT6Á¦JUGc¯CShpl ½Rïw$f}üôÓ/ãyÿÀ¼q#ªÍ[ö>DWà	òÑÂuî½emã¯)ÎÙà'>¬ÖJ±v¯Ó[5êH0T´G]Ä"¿0öã!¿èÓe8iÕJ·öÐ:À0¡àÔ÷§¹9û^«6¸Z\Ì |
| --- | Minor | *ì¤`!MööKðØ²kSóõüXæÓÝg+áõu*?^^uî"SÑóèG¿/#ÜÛ>»¨0 V)G£fT{õ½°Ð |
| --- | Minor | ô5áÓ·ÈÒ©8êÆÉdÐ«UÏb¤6jãwO@=hêÿæIyÍzÕdêª4TuÇñBà<Âta°LT*ÚÅº8Ú¦I@)l ¢NÑ¤£8Õ5üÍ2. @¥eì2n9¿BµB½B³BªêÅJå¯uwÉµµøÊS÷â¦år-È¯¢'ù°¢¢{4R¼ï4µEZ`ã^«Íj ÂmÐ |
| --- | Minor | Ðk·á*@3x´×ècd°9kxDm²Í  Vå \ 4àB)Ç£üm­CÑ JëLæ¡	!×¯¢oj5»Ëð Ì FÌ%ó`*ZÁ"§3wqS¹»ø©üta¦f¦¶C6ZÄËÐr¼¹ÜÇ.áðµêºúZÃRãRqiskYT°Ë¾ÕÓWàWòä[¬Ë¬«Ê¼ÏÉÍõÚ!ò>[ûaÆÊ»Eã[££6wÀ}È¼²Jjæ^ÄâHdgE%ºÐ¡üuÿÇtÉÌ»OtKO7*l¥ßù¢ÅlÉD1á×_Ùß. w4ôtMvâ¿2Lz¾×ötvz×èBí-¯½&l¸VC÷o­°âeE]0³pMÃ¶·ßy¤YØðu÷/åËV¹ÁL"	~nÃ Î4[Ì&ÓØP w7ï¥"baÌ¸1È==ïÈ1Ýe_#Ì4*Ïm ß)AÊa © *Ê`ýqÉ!qtQ¦ñµæGÞi~k[Eæíe³|?;ð¯ÉÝJ~ÝÛË§@I´	iñü¾øAýQH°¦Yvú. Ô_+õ«dÅ¹í7kZÉíÔ±ñXUç·ÄìMcu !BÖåßÉAúB.Cÿ~îYª4Ç	?*em7êÜ]è+|É9Tå¶¹vd3mêüÓoä(9û×¾o*åðC7Je®48p"­Q(RÊ>mrWG@¡¡©sªöXu´¶f´ø£OëGjÍo|.{ .C/´AÖEN¥àP¾YêKj1>#¾*¾9½MÆ)>7ÎpöõfÌk}6ãRW¿{3óM{þK)ÓZ¾þüçGó9Ï¼kóîbÌ@sò¢×çtõÑèPjá¥RºÎ¥²ëôª:Tm3Q7ãÐï±°jdà	4Ë0û |
| --- | Minor | ¢Î#­~g­¦@öôcvúÊ_ùËé |
| --- | Minor | ÃäÝîæURÝ é'_c0ãÆ=WZ.>³ûäK!ª¾å­]3i9øÀÅ}o1Îµ!åKT¤Ò 5CÑ&)!Ãæ¦ |
| --- | Minor | ÁÙþ. _üPàÜÛ¸-<j§¥ªÒá¬[u8=sÐPiñPã¢ÇG3¹¸øìÇýOL>îy·ßÛÐ+&MíeNÿXµY_º]	[y	×[P­ 1Õu¤:o5g1ÛÕþÓ²;ü[Öü´~K=ïý+©ß^ý¾ü [¹Í®éíbDÚóGÐ%.-·6¦öÜAXwf¨©rÐ8Õpå[×¾# |
| --- | Minor | 1c<Ìâ ¥äìPöK®;Â3üX~ÿ+¡^¸ ºSõ¬ªS=^Ý¬a5µ´ñÚYÚcÚ.]î÷ú¥úó á9ãq¾¸JÜ-îÏ&©ÑÔkoî±<¤p}(£F©hò}¹vÓoûY-þæô³RÐïYúíî	å;_:¦EÜð~ù~xLú]gû9ó(]C£PZÞÊhòó<¨Û=(pfÂh.@xÐHYj ÝJÐ´ùáêx´àÓa4UÂéAÓn¬U£ÌJ /gÁo1@jÐhÃ 3ÑR°s` ¤Æt}¬²~Ì\X·à<ð|ì;G¹wû:Ó]Ê@_GTªëôJ |
| --- | Minor | \«RÖ ÂîôîæS¡ÿ£÷>åÛ÷C¡ÿ3Aÿ"ôÿ¡ÿ~°ÿgÃµFWþs#øþ)öÚ5<üxYÑ$t'úpf:ºp² |
| --- | Minor | £»Ñ/Ð·7ÌbóXÀ*t Æj¬.*fæ÷£Âýèp?&ÜçúÚçôõá~`+³Zúô |
| --- | Minor | µ×Ûâ¹×ÉëÛO^Ó3§}ÜbrÚGN«Èq-9¦%¯¼lå^	­¤5H^ÉQüV&/Êä°Lµåu±ä L^XEÉsò:î7Vr@G~ O¤=ëc¸=2yü1{<<&Ý»Üî²àvÈ.Ý	î´«Ù²CbM Û pÛe²m«Û@¶nÑs[-dk+ gÑGN±MU«¸¦cdóýZn³lØF5!6ã6ÉdãÃÜÆcdãjöá |
| --- | Minor | äaÝ xmH ë×¸õ1d}kï)©]g"k`ë5Åä¡ y0<°Ü¯%«¹Õ2i¨¹¹o»/HVÈÊz#·ÒBê¤n©5²|[ÞE-âyÈÒ(²ZCjdr¯Lªë¹j. ÖÅ[µ. Z8[TA':®R$«Ù ©ØrØ²¼ãÊdRº +=FJW³æ'p É@J ¨¤y62W&sdR4;+ÉìtrL eòäîU¤@&ù£É. ü\&3»d2½L³ÉÔ;ÜÔUäN#2BI&iÉb2>VÅßAÆÉX"rc- g°Ë1Á&­'d5ÐÊeÉd`¦h%A |
| --- | Minor | i!Áj.¨!Á|¨I #&é6.#dbÓc4\º¤¯fÓÔÅ\ÚâOµrþ$HµTMÔSIrRKA ±¤ ñAçIâ ä I|Nâà±83ØXñz"9o!ñ¸M'xN±nØÌm"îÕlÄHlt2W<q:s:qÀª 6µË 6«³U«ÅÂY­Ä*±1ù1{M2¡G#àoÜApÏ =. . Æ¦XÑ< àV\¼¦§þ{ ÿ×üË²¨ÿõíé endstream endobj 232 0 obj <</Length 145/Filter/FlateDecode>> stream xíÏÉNBAÐ2 "8òÿgçí0a6ç$U·»RîänþÜk¹­²F%ïÒJ»d'÷é¦~'û>*5Î¤<V}z²5ËÓÙ<gE^²ÌkVYç­¾úÈg6%·ùÊ.ûÊù;?ý                ®åø*f endstream endobj 233 0 obj <</Length 394/Filter/FlateDecode>> stream x]SËn0¼ó>¶ð2ªôÂ¡öå@ð!9ð÷µ=6£Ù]ïuxª^+Ù/. üTc[ÓÂº^ EóxW-±+ÝzD1}»8f¿íÐLA¨ëu^h¨d7EÁÂ/mÎZÙÓ¯ô0ÆÂ%HõòÆ~N5¤ú>M¿4\Ø>(K&¨ÓåÞé½6yW	í÷ËºÓiïu"[¡¥v4OMKª7 ½~JVtú)âåH»v[|lâgàÅÊÈG'onJÎuTxÕ%¨Äò4ò*RPw§rÀÁÚÌõÒ 7M8SîäÂ=ºfRÆ3pZ9ÃY ùA­Ë1'wµ<å£i9¦årè»¸ës÷÷åWmPCs7´§è!GyæcÓs×ýj7#Sp^Ì²ù­2{g.É¶Ôí])½Ïö&ÙE6+ÜKÚ.Û4N&Ë¼:³é° endstream endobj 237 0 obj <</Length1 2956/Length 1931/Filter/FlateDecode>> stream xÍV{PT×ÿîý³À.»ì²À5°äé¢ï\ê³JÄZ´YX·¬¢k6QÆñØ$NØ±iº'ÅTûN'còG§q:¶ÓNÇvÚþá´~{6ôßö|sîù¿ï÷}çÞ¹s)Dä¢(ÖÕûî¦·)<icKO L.=Äö/ÙÛ²«_?Qyù/DI÷Øw&nëù]ôO7TÁñ¡¶@_XÈe;µ­{ ùôm¢l¶·sîüõ?ð|¬ËÓ`®|¶óÛ{ú÷hDÙ`ÛÝÝÛ vpþA~Ø{{Â¢X÷³m}[ §Uÿpá;±ïb¸·¯§-\Çgw´wØþÆýq}ùÅ÷ªn:?påÒ­iÿJ¹ÉqrzçPÎ¾¯3þñûýäx¿É¤Rbp^RMäÉî÷-¦ay#aÙ*¹é|üMU&8l |
| --- | Minor | ÜG¥<ÏfNbÅm ©é`³AÚ¤ªèÔu¡Ú ºW÷Ú4SS.$õ(¿IôDV­ÂzwV×à©ñS±VAº¶ºÔ½SSç¯ï%X^·IU¡Ý=¦úVÇ'ônUZò©»ô1ªsè±©©ºñÜ4&gÁ<&|yw>-x§´du]>ö³ÚiÖÚ¦öÕ7°·ØÍþÚR©QãÃø±7oäËAÜ4Ä|üÈ·®È·¸^Fü0k;põ |
| --- | Minor | ^õã |
| --- | Minor | ?~`âuß7ñ=WL¼:¶\¾zcËñ]ßàÛ&¾åÂåÑTyYÃh*¾éÇ7øz.ùñÊËAùxiØ%_òad]øðÕÕø_.ÃÅÃ9ò¢/¸åÙ¸àÆùs.yÞs;çÂ9CåÄ³ÎFÅ°ÃøgVÈ3&^8í/øpúSöâtL1qê¤]râTL!c¥8iÇÉ	q¢7"Oãø³yÜã8ÆÚ±x~h\>obèh£ÇPT=âGqÔG¸¯#>>äsp865aLCréÁ VàÀCxnÏ: |
| --- | Minor | eÔÄ3ÝnùLöG\r¿öíMû¼Ø§1àÁ;vïÒåîûØµs¦Ü¥cçLôsRúLì0±=ìÛM¢7m=Kå¶.ô. EwWªìv£;*ºRÑeN.Ùyíã²ÃD{[£lG{T´|²­mùÐÊ ÖûÑfM[Ëd­exÊD£-«ñÅ6ØT_0±q7QÄz |
| --- | Minor | ·.MÖE°.. |
| --- | Minor | Sentence exceeds complexity threshold, split for readability. Applying the split needs --strength moderate or higher. |
| --- | Minor | none (split proposal only; source not rewritten) |
| --- | Minor | none |
| --- | Minor | Check: NEEDS-LLM |
| --- | Minor | Flags:    not-assessed |
| --- | Minor | SENTENCE (Line 51, 278 words, 2 clauses)  [Script] |
| --- | Minor | k«j¬q`U+M+±ÂåpËå^|6µª]Öf¡fWÖtaYµ[.ó¢ºÊ!«Ý¨2RdF ø{¬Oc©(K?%5¹d5/²ËÅb¤ËX0ß#¤c¾;ñys59ÏÄÜJ¯«¡Òo^øç¤H¿þÄ÷òLYQò²Yò	Qce(Ò ,FI±&KV£7Q¬¡Ø³¹õÙAVÈ¢*rc(à¥ÀÄgÂçÌ¾Fäç¥ËüzäqZ^:òñh2férV#ô\Ô3¡O\.ëAnTäØcì<ÌLÃ#ùx8«B>\,fÍª@¦\tÜÈÐ4ÑÍëÍ^/Ò>¿^	7/îj¤qÿiÃpqÌeÂÉÎL8 |
| --- | Minor | jÂÁÃß;cì¤äÉ<°I¿´E 9Oú!LIU;z	%¦)Åÿ·þ× |
| --- | Minor | ×Á§b§>>!bô6Ë»¬­¡NÚNhõ»´×ò_ÉqaÏ2}bJãÔ¸(åÖó&óTrì.ãClP³¿IK.`RÝM*êX«³2F(EB`21­¬·i	]¥Ñ¸.'iqëé6K5³¯¢kôr.)·(BÇ¨Ï:Z³»¼Å½tR³¼eÉ=>ñãã¾NyË¦q¥NÞç5f¿ð+EÊz4!¤4ðUe+Ø;H¢¥Àk=¨ê^®?½_T·¨E¢@å:ñÌ?JK¸ßwº§ï¿§¤rYò:­JZeKUlIÚÀÑ½¨T.Ø²©"ØÀkÙwÖ*·¹Jâu®oV~¯©Í|z»^SI(Tþ9ä~ïçÞY³6cÍß_SÄ§=ð"õ7­3?®+TÈVBWùZðÛiIÖÅÇ02Û´n£|%Q/ivPµQ;õóí¡Z¨W?U°T²ÖÌ¿SÇûxî V P°w%mc|kUÔÍ¢óWýWeµòÚÊ9»ød¤jXëd´- |
| --- | Minor | ÔYóëÌ²aÆ43oãtÎïåº+ö O½U¥¿Îæ s^{¯æ¬^êúTüFKëc½×ªéç.+iÞ'ð¡?É=}oÚoÝÇþsë;«teú®ÈßÉðOß¯Q endstream endobj 239 0 obj <</Length 40/Filter/FlateDecode>> stream xíÁ	     ÿÛ¨	               p¢@+  endstream endobj 240 0 obj <</Length 228/Filter/FlateDecode>> stream x]±nÄ wÂãÝp"I×(Ru]2´=5íTu `"¤Æ yûI¯R-eüÖåµêÉE7özÀÖa\üÊaÄÉ¨0NÇ£*·U2ÁÃ¶D{²^´-È·Ô\"opz4~Ä³  ùÊÙÑ§ë°? |
| --- | Minor | k«j¬q`U+M+±ÂåpËå^|6µª]Öf¡fWÖtaYµ[.ó¢ºÊ!«Ý¨2RdF ø{¬Oc©(K?%5¹d5/²ËÅb¤ËX0ß#¤c¾;ñys59ÏÄÜJ¯«¡Òo^øç¤H¿þÄ÷òLYQò²Yò	Qce(Ò. FI±&KV£7Q¬¡Ø³¹õÙAVÈ¢*rc(à¥ÀÄgÂçÌ¾Fäç¥ËüzäqZ^:òñh2férV#ô\Ô3¡O\.ëAnTäØcì<ÌLÃ#ùx8«B>\. fÍª@¦\tÜÈÐ4ÑÍëÍ^/Ò>¿^	7/îj¤qÿiÃpqÌeÂÉÎL8 |
| --- | Minor | jÂÁÃß;cì¤äÉ<°I¿´E 9Oú!LIU;z	%¦)Åÿ·þ× |
| --- | Minor | ×Á§b§>>!bô6Ë»¬­¡NÚNhõ»´×ò_ÉqaÏ2}bJãÔ¸(åÖó&óTrì.ãClP³¿IK.`RÝM*êX«³2F(EB`21­¬·i	]¥Ñ¸.'iqëé6K5³¯¢kôr.)·(BÇ¨Ï:Z³»¼Å½tR³¼eÉ=>ñãã¾NyË¦q¥NÞç5f¿ð+EÊz4!¤4ðUe+Ø;H¢¥Àk=¨ê^®?½_T·¨E¢@å:ñÌ?JK¸ßwº§ï¿§¤rYò:­JZeKUlIÚÀÑ½¨T.Ø²©"ØÀkÙwÖ*·¹Jâu®oV~¯©Í|z»^SI(Tþ9ä~ïçÞY³6cÍß_SÄ§=ð"õ7­3?®+TÈVBWùZðÛiIÖÅÇ02Û´n£|%Q/ivPµQ;õóí¡Z¨W?U°T²ÖÌ¿SÇûxî V P°w%mc|kUÔÍ¢óWýWeµòÚÊ9»ød¤jXëd´- |
| --- | Minor | ÔYóëÌ²aÆ43oãtÎïåº+ö O½U¥¿Îæ s^{¯æ¬^êúTüFKëc½×ªéç.+iÞ'ð¡?É=}oÚoÝÇþsë;«teú®ÈßÉðOß¯Q endstream endobj 239 0 obj <</Length 40/Filter/FlateDecode>> stream xíÁ	     ÿÛ¨	               p¢@+  endstream endobj 240 0 obj <</Length 228/Filter/FlateDecode>> stream x]±nÄ wÂãÝp"I×(Ru]2´=5íTu `"¤Æ yûI¯R-eüÖåµêÉE7özÀÖa\üÊaÄÉ¨0NÇ£*·U2ÁÃ¶D{²^´-È·Ô\"opz4~Ä³  ùÊÙÑ§ë°?. |
| --- | Minor | Sentence exceeds complexity threshold, split for readability. Applying the split needs --strength moderate or higher. |
| --- | Minor | none (split proposal only; source not rewritten) |
| --- | Minor | none |
| --- | Minor | Check: NEEDS-LLM |
| --- | Minor | Flags:    not-assessed |
| --- | Minor | SENTENCE (Line 51, 582 words, 9 clauses)  [Script] |
| --- | Minor | kß8#E¨D×AÆ=«ð¢fYàKoRßÅí°?ÅûR×»%í |
| --- | Minor | .AidE¶JÑAkStÉüëÔhySÕI¾§Ï=eîWGäÿÞýé9Y+K)²Gxß[ð!Sùü hÃsV endstream endobj 242 0 obj <</Type/XObject/Subtype/Form/BBox[-6.6 -6.6 6.6 6.6]/Length 134/Filter/FlateDecode>> stream xm=0wNÑ¼¦´ø3;z.ÆÄû¯VÒjR¼¯ »[é `?º()Oü8ÅY3I,,=_ÒÄ*W&«ÂjÑnØÝ¨P«2dÅ®ÖÞP5fjÿÂßÿÐÌwr´¡³2º·Açøòñ,±-t¥«K' endstream endobj 243 0 obj <</Type/XObject/Subtype/Form/BBox[-6.6 -6.6 6.6 6.6]/Length 38/Filter/FlateDecode>> stream x3PÈâ2PðâÒ5Ô3S ¹\pf	aé"\\N\ /× f endstream endobj 244 0 obj <</Type/XObject/Subtype/Form/BBox[-6.6 -6.6 6.6 6.6]/Length 35/Filter/FlateDecode>> stream x3PÈâ2PðbC=3\.]&r¸\\N\ ´åô endstream endobj 245 0 obj <</Type/XObject/Subtype/Form/BBox[-7.2627417 -7.2627417 7.2627417 7.2627417]/Length 49/Filter/FlateDecode>> stream x3PÈâ2PðâÒ5PÐ5Ò323271RÈå3 |
| --- | Minor | ròpn.T ·w­ endstream endobj 246 0 obj <</Type/XObject/Subtype/Form/BBox[-6.52169043 -6.29442719 6.52169043 6.6]/Length 100/Filter/FlateDecode>> stream xm1@{^Á Èµ¾Äý+ÆÂ\C`3ì®âÔ ¼ 1uªL6ÌtÁ«ÄøiL¢Ý°6ÉL·WÆæõ£û@!"uN©Ý$wÖoXágY&Ü endstream endobj 247 0 obj <</Type/XObject/Subtype/Form/BBox[-6.6 -6.6 6.6 6.6]/Length 71/Filter/FlateDecode>> stream x3PÈâ2PðââÒ5Ð35]C=3\.T~ÎÊáI¡ó¸p&61±º8ùHztÑÌÕE·W«ë2¸¸¸ Þþ*¨ endstream endobj 251 0 obj <</Type/XObject/Subtype/Form/FormType 1/BBox[0 0 260.25125 205.6908312]/Matrix[1 0 0 1 0 0]/Resources<</Font 219 0 R/XObject 241 0 R/ExtGState 248 0 R/Pattern 249 0 R/Shading 250 0 R/ProcSet[/PDF/Text/ImageB/ImageC/ImageI]>>/Filter/FlateDecode/Length 2987>> stream xÚÝ[Ë·à]/hd¥2Å],Ûâ$Ûda{aÏH²±lY¶å|Wvùºb¿Ø}ûu¥«¹Af0º.Y,:U,²y¯>~úÛ§?yTôEu5<Ý¼®¨þÏk]¿75ÕOð÷¼Òxú¡2A+ãÉx<ÝOF{fKëñãwUõ¬ºúJ^£×ªòZ9 ¤}²Ö±¢Z'ÅÖ+Åw¥ØháZ­8öªÂÔä¤I»LR6®þùiýÏúe}õ¡ûLý)f+W¿©´LRÐ`å£ Á83Å U}Q}V¿Â(¶Aáy; a`"MÍ;TªGpÒêþÕõ¥6Emlôu0JSp.2zÝüP=º®®SëëgÙ×·ÕõÃ?ýáB°Q{ë#¹úá-RôÎg!Q"I:°fVúëúúÓêëê³<§{I1 3HzKá:ÔÑ*k\xïP»3@ |
| --- | Minor | *E2h ñÑ`o«\;EåbÒïns¸­VÈaÍ >îMëpqÊ+Y}Ü»ÀÕç ×:ÖzÄ >ÜMà:V¢?-¸gandå¬.Wøxp7UnâHé´à#mg.Pøhp·Un4¬M°§wTMÕwÉ uMq3ËY~øàúúûÊ* s²ZdK>ø¹3ª¨Ü­ÿå^7¶lÿ4Ë#i¥ Ë -7mkèJù­ÓÁôò£>kõ©¿èõìKùm§ÆÐ¨ý¼ñK.?§åê±i®ÿØ|ÜÉ{Ågäó[u/òûëVxi_'KìüiÁñwDY"Ð ÏôÏÏëê±mÿÁÚ¨¤(áG¹k}aÉûLªÃ,pxÄhÛ9wnØfº ¥s	ÕD)Q×¤KìÒ;æÓxÐÆaù"?e¢1ÔüX¬G*°ÇÑ&m¬ñ¿#Ü|ÐFnÃREÇ¸ùÑp*¸GWà6	K9·pr¸ÏÌnJHÒ¡À=È»TYÀ=Ò¸·KØ÷bnïwú_cwÄ²Ä1i2äGÃ]ª,ài\;oØ9ÜÉá>3»+ë°MNgùÑp*¸GWàN(8Ø±ZÚ¸ißÄ»_U2ô¥a¨_;´2É0¶[oºb2 Ú`G3ç{#Ö,ÉQØãrÈe)Î«8J¦sÁx8iADÆ aqW¤ ×À&òGÈS9Ãó6%¢!`à. |
| --- | Minor | kß8#E¨D×AÆ=«ð¢fYàKoRßÅí°?ÅûR×»%í |
| --- | Minor | .AidE¶JÑAkStÉüëÔhySÕI¾§Ï=eîWGäÿÞýé9Y+K)²Gxß[ð!Sùü hÃsV endstream endobj 242 0 obj <</Type/XObject/Subtype/Form/BBox[-6.6 -6.6 6.6 6.6]/Length 134/Filter/FlateDecode>> stream xm=0wNÑ¼¦´ø3;z.ÆÄû¯VÒjR¼¯ »[é `?º()Oü8ÅY3I. =_ÒÄ*W&«ÂjÑnØÝ¨P«2dÅ®ÖÞP5fjÿÂßÿÐÌwr´¡³2º·Açøòñ. ±-t¥«K' endstream endobj 243 0 obj <</Type/XObject/Subtype/Form/BBox[-6.6 -6.6 6.6 6.6]/Length 38/Filter/FlateDecode>> stream x3PÈâ2PðâÒ5Ô3S ¹\pf	aé"\\N\ /× f endstream endobj 244 0 obj <</Type/XObject/Subtype/Form/BBox[-6.6 -6.6 6.6 6.6]/Length 35/Filter/FlateDecode>> stream x3PÈâ2PðbC=3\.]&r¸\\N\ ´åô endstream endobj 245 0 obj <</Type/XObject/Subtype/Form/BBox[-7.2627417 -7.2627417 7.2627417 7.2627417]/Length 49/Filter/FlateDecode>> stream x3PÈâ2PðâÒ5PÐ5Ò323271RÈå3 |
| --- | Minor | ròpn.T ·w­ endstream endobj 246 0 obj <</Type/XObject/Subtype/Form/BBox[-6.52169043 -6.29442719 6.52169043 6.6]/Length 100/Filter/FlateDecode>> stream xm1@{^Á Èµ¾Äý+ÆÂ\C`3ì®âÔ ¼ 1uªL6ÌtÁ«ÄøiL¢Ý°6ÉL·WÆæõ£û@!"uN©Ý$wÖoXágY&Ü endstream endobj 247 0 obj <</Type/XObject/Subtype/Form/BBox[-6.6 -6.6 6.6 6.6]/Length 71/Filter/FlateDecode>> stream x3PÈâ2PðââÒ5Ð35]C=3\.T~ÎÊáI¡ó¸p&61±º8ùHztÑÌÕE·W«ë2¸¸¸ Þþ*¨ endstream endobj 251 0 obj <</Type/XObject/Subtype/Form/FormType 1/BBox[0 0 260.25125 205.6908312]/Matrix[1 0 0 1 0 0]/Resources<</Font 219 0 R/XObject 241 0 R/ExtGState 248 0 R/Pattern 249 0 R/Shading 250 0 R/ProcSet[/PDF/Text/ImageB/ImageC/ImageI]>>/Filter/FlateDecode/Length 2987>> stream xÚÝ[Ë·à]/hd¥2Å]. Ûâ$Ûda{aÏH²±lY¶å|Wvùºb¿Ø}ûu¥«¹Af0º.Y. :U. ²y¯>~úÛ§?yTôEu5<Ý¼®¨þÏk]¿75ÕOð÷¼Òxú¡2A+ãÉx<ÝOF{fKëñãwUõ¬ºúJ^£×ªòZ9 ¤}²Ö±¢Z'ÅÖ+Åw¥ØháZ­8öªÂÔä¤I»LR6®þùiýÏúe}õ¡ûLý)f+W¿©´LRÐ`å£ Á83Å U}Q}V¿Â(¶Aáy; a`"MÍ;TªGpÒêþÕõ¥6Emlôu0JSp.2zÝüP=º®®SëëgÙ×·ÕõÃ?ýáB°Q{ë#¹úá-RôÎg!Q"I:°fVúëúúÓêëê³<§{I1 3HzKá:ÔÑ*k\xïP»3@ |
| --- | Minor | *E2h ñÑ`o«\;EåbÒïns¸­VÈaÍ >îMëpqÊ+Y}Ü»ÀÕç ×:ÖzÄ >ÜMà:V¢?-¸gandå¬.Wøxp7UnâHé´à#mg.Pøhp·Un4¬M°§wTMÕwÉ uMq3ËY~øàúúûÊ* s²ZdK>ø¹3ª¨Ü­ÿå^7¶lÿ4Ë#i¥ Ë -7mkèJù­ÓÁôò£>kõ©¿èõìKùm§ÆÐ¨ý¼ñK.?§åê±i®ÿØ|ÜÉ{Ågäó[u/òûëVxi_'KìüiÁñwDY"Ð ÏôÏÏëê±mÿÁÚ¨¤(áG¹k}aÉûLªÃ. pxÄhÛ9wnØfº ¥s	ÕD)Q×¤KìÒ;æÓxÐÆaù"?e¢1ÔüX¬G*°ÇÑ&m¬ñ¿#Ü|ÐFnÃREÇ¸ùÑp*¸GWà6	K9·pr¸ÏÌnJHÒ¡À=È»TYÀ=Ò¸·KØ÷bnïwú_cwÄ²Ä1i2äGÃ]ª. ài\;oØ9ÜÉá>3»+ë°MNgùÑp*¸GWàN(8Ø±ZÚ¸ißÄ»_U2ô¥a¨_;´2É0¶[oºb2 Ú`G3ç{#Ö. ÉQØãrÈe)Î«8J¦sÁx8iADÆ aqW¤ ×À&òGÈS9Ãó6%¢!`à.. |
| --- | Minor | Sentence exceeds complexity threshold, split for readability. Applying the split needs --strength moderate or higher. |
| --- | Minor | none (split proposal only; source not rewritten) |
| --- | Minor | none |
| --- | Minor | Check: NEEDS-LLM |
| --- | Minor | Flags:    not-assessed |
| --- | Minor | SENTENCE (Line 51, 157 words, 1 clauses)  [Script] |
| --- | Minor | X}õ]ücßÒ`såÝ w²­ÀïJ»Kã6ZÉm4Ó°F¸X¯|vi*Ãl VÚGioÖÚ]²ìMS\$)&`AÔiuóöÑð7ÉÚ8rÁHh)7øW+ õ&Õ?©þßY¿w¨ã zVk=÷ÆíÚ/´/´3^hg¼ÐÎx¡ñB;ãN/mpïc #°£ý?ö>ð1êÄ\[>?×ÚP Qic'HÙÄ°z(£­im¸ÙXzVk=÷ÆÙ+fo¬XýÌ)9u`(a·Ò,9fBqêWÚÁ6Qg­ |
| --- | Minor | °u fm¥áïÝf£	0/ïò®CêC.M¨BëÑ'kñ0Ú5Qr­1g VhÒ9 ;Â­QØÈçÕäpmMLi¥áLDØ}a÷EÄ&§îrïaÉÏùÌç\8O'R×xNÓ(N¶K)ò^ymm³¦JÆ9~§Ø "Âô1ô¨Özì·ÂÙÏ.gª7² |
| --- | Minor | áµ3!1Û0¢¬ |
| --- | Minor | `ûVÚÍÄâìTHK;É9vÂqÊ  ©R»âK=¬Û¦ù^"ÁEIê:Å³GÂÅ°Þl7çýý^ÎûyÎ'eZ`~×b¡;58É¯4á¼ßÉy¿ópbß`Û}­Õ®à |
| --- | Minor |  d Éû)3c³hÏ£GWbç¯þBíìâï£ÇQwGíM«#è2ÏÕ['«MÉ«ä\Õ? |
| --- | Minor | X}õ]ücßÒ`såÝ w²­ÀïJ»Kã6ZÉm4Ó°F¸X¯|vi*Ãl VÚGioÖÚ]²ìMS\$)&`AÔiuóöÑð7ÉÚ8rÁHh)7øW+ õ&Õ?©þßY¿w¨ã zVk=÷ÆíÚ/´/´3^hg¼ÐÎx¡ñB;ãN/mpïc #°£ý?ö>ð1êÄ\[>?×ÚP Qic'HÙÄ°z(£­im¸ÙXzVk=÷ÆÙ+fo¬XýÌ)9u`(a·Ò. 9fBqêWÚÁ6Qg­ |
| --- | Minor | °u fm¥áïÝf£	0/ïò®CêC.M¨BëÑ'kñ0Ú5Qr­1g VhÒ9 ;Â­QØÈçÕäpmMLi¥áLDØ}a÷EÄ&§îrïaÉÏùÌç\8O'R×xNÓ(N¶K)ò^ymm³¦JÆ9~§Ø "Âô1ô¨Özì·ÂÙÏ.gª7² |
| --- | Minor | áµ3!1Û0¢¬ |
| --- | Minor | `ûVÚÍÄâìTHK;É9vÂqÊ  ©R»âK=¬Û¦ù^"ÁEIê:Å³GÂÅ°Þl7çýý^ÎûyÎ'eZ`~×b¡;58É¯4á¼ßÉy¿ópbß`Û}­Õ®à |
| --- | Minor |  d Éû)3c³hÏ£GWbç¯þBíìâï£ÇQwGíM«#è2ÏÕ['«MÉ«ä\Õ?. |
| --- | Minor | Sentence exceeds complexity threshold, split for readability. Applying the split needs --strength moderate or higher. |
| --- | Minor | none (split proposal only; source not rewritten) |
| --- | Minor | none |
| --- | Minor | Check: NEEDS-LLM |
| --- | Minor | Flags:    not-assessed |
| --- | Minor | SENTENCE (Line 51, 460 words, 6 clauses)  [Script] |
| --- | Minor | þÊâù¨¸VW¶Ñ |
| --- | Minor | ;¹ÎÓÉ ñ,Ö'H<¶DÈ²H"cÀìú|R £l+A*ì!²±Þ[mÝs66÷çeF:¢b |
| --- | Minor | p90ã7Uax¦Ñ"ng=#afzíÃM%·|Ãç ½á Eb¯QF£LH£ÑÀSÃ7³ðiiyóØO¬{lç=ôï¡Æ)0ìéÁln=2rÙÜmTé|7¿y±R¾#A9ÉXQ¥áÍHPnònä|he¼S­ä£ò½GGÓÂi±#_X÷Ø{x¾§C¶ì9ÛÈíïºgîÂ­iÞ?öÞÈ/¼<u´æìO.ä²Lù5k|r8«=¡8ñó­êÌPËØÇTçë;è Ä É®o²È²eoé÷K¾ eh£:¿iùºràm¶<;³ãcpö{ÿxOçEÙÔQ1{¡Zú¼ÜçcÌbÓÅ3þükëOc¤¥dÍjÚï27Âú¯=Ìu~!6uúSiDØâÊÙ@ÿvwIÚÀåë¦ c¤¢ü mB¨¯6fz<£#iõS6j4Þ¯`FÅÖ:zïÛC£îQVkG2¦Bò:·1½ ôúî@õáän-úê¢¤tÞmdZ¿í¼üµ&Ù©_ IG¥L(âÌe÷pìSÚU@¸ÂÙB)¼lJeáP4M²¿A¥U%£t)nE nÔÍ0ØÉÔzÂÔ	-«9¼8 ×L.|9æR5Ï¥na1ÕÝ¼+­qHÐiÖ¦Û%R¾ÝÐ@Êaq¼[¬°=)Ç«ì{>y)má!h°ÄÙ`1ùÂ~³yq¨¡©ì´µ¦,&æÐlQ &§cÂ +#XíØ÷ùÖç--W×IÒÿ´±l®ØMT£ôÑ&¹`³Ó.xxì*½UÆÀX@júæ¥:ç±~ÇÒàú¢yI£ÔµrÇ·_&æzÔùE«°E§Ê(Kî$U²2*Os ·¦rwb¹õ)Ø¦{¶½ðn ÉM¯®ó{; ¼óiÛÛö^N,jmÓÝù#¬1¨»NrÁ­ý÷&ÄÐð-Þ3î¾£Öòø[-ø$&É[k¶çÿ|q2/»ïÈg¥3~2ÅU¼ê¿¶3óS endstream endobj 254 0 obj <</Filter/FlateDecode/Length 2855>> stream xÚÅZK ííOk~}¨õªªÞdÙÅ`¦ªTÅÇÇTmÿÚ`Óü6¨bú·}ùïýÂ?Ùþüº}÷lüÄ¡£íõm£ |
| --- | Minor | ³½Þþö¬µü£_Òß7þAþZÖ®üï!ÿ6oZ[Hcùoo/ã=¿Ë4ÒxþQímL£C]/?á»ÊßiNª£Íõå¯Ý~|ÝxJc_öZÿ¾ Î°9åÑ¢I»îúAñ~]äai¿ÖhJ¾ûéWØ~ømûÿÕÀZEuY;¾êðÖ)m=AÕqE6s­úÑu7Æ¤Ýð]üòr±Zó±&àìÇDzîËå(i<ÊÓ¢¹66Mçò¤=Ñ®¿i¶ØJlÖ7×qd$C]	}]'ïªjß¬õä3^Ð ¬ÃÚ­þ_{Në¼ Vùø^}{}Ý².övTvàµHuv«>u¢¼ª½ôã<IWi4/L.UÊb²y7{¼ÉRPÄ×¸]À(KüÇGm|r!UÛº­ Ç¦Â;cÛhÿÏ¤ÔêoÅ²rò¸ùNÖFv[çé­gHnÂ|ú»Fzº ÷ê´¸VÁhOõýt,¶UdÉú&uòDÎ1z;* "ÕìèÓºnCeû F2¿øÖî¢(¿b[qr<Næ-¸/\ë:rhoÄK£ÌLÓêkÐäxÇ¬æk³µ5Úy;>£¤ |
| --- | Minor | ÷ªOÃ±b7ö+y[ix-XÍ¸i[f¯´Kê@à\á §Ek	Î °O§é9Â=+p£×ÑhÍÛ:ãìÍQó(1Ðr·½_Õ¤ë=ÑÒ§¬Õ© ¸´iLg ï5w²Ã¡c7¶äWfUs¤°IùtKÔtwdÕ5õËÊ`pV-ðtGNu	:T·zÐ¡Ñ£TDÌ¥<näFØùIx®y(¼çÇÂ8Ê4>Ènâ`ê4ñ[h¾®Ùtá .¬KDYeÄ5ô,Vynï6Â |
| --- | Minor | ¬[},ôs1i! |
| --- | Minor | þÊâù¨¸VW¶Ñ |
| --- | Minor | ;¹ÎÓÉ ñ. Ö'H<¶DÈ²H"cÀìú|R £l+A*ì!²±Þ[mÝs66÷çeF:¢b |
| --- | Minor | p90ã7Uax¦Ñ"ng=#afzíÃM%·|Ãç ½á Eb¯QF£LH£ÑÀSÃ7³ðiiyóØO¬{lç=ôï¡Æ)0ìéÁln=2rÙÜmTé|7¿y±R¾#A9ÉXQ¥áÍHPnònä|he¼S­ä£ò½GGÓÂi±#_X÷Ø{x¾§C¶ì9ÛÈíïºgîÂ­iÞ?öÞÈ/¼<u´æìO.ä²Lù5k|r8«=¡8ñó­êÌPËØÇTçë;è Ä É®o²È²eoé÷K¾ eh£:¿iùºràm¶<;³ãcpö{ÿxOçEÙÔQ1{¡Zú¼ÜçcÌbÓÅ3þükëOc¤¥dÍjÚï27Âú¯=Ìu~!6uúSiDØâÊÙ@ÿvwIÚÀåë¦ c¤¢ü mB¨¯6fz<£#iõS6j4Þ¯`FÅÖ:zïÛC£îQVkG2¦Bò:·1½ ôúî@õáän-úê¢¤tÞmdZ¿í¼üµ&Ù©_ IG¥L(âÌe÷pìSÚU@¸ÂÙB)¼lJeáP4M²¿A¥U%£t)nE nÔÍ0ØÉÔzÂÔ	-«9¼8 ×L.|9æR5Ï¥na1ÕÝ¼+­qHÐiÖ¦Û%R¾ÝÐ@Êaq¼[¬°=)Ç«ì{>y)má!h°ÄÙ`1ùÂ~³yq¨¡©ì´µ¦. &æÐlQ &§cÂ +#XíØ÷ùÖç--W×IÒÿ´±l®ØMT£ôÑ&¹`³Ó.xxì*½UÆÀX@júæ¥:ç±~ÇÒàú¢yI£ÔµrÇ·_&æzÔùE«°E§Ê(Kî$U²2*Os ·¦rwb¹õ)Ø¦{¶½ðn ÉM¯®ó{; ¼óiÛÛö^N. jmÓÝù#¬1¨»NrÁ­ý÷&ÄÐð-Þ3î¾£Öòø[-ø$&É[k¶çÿ|q2/»ïÈg¥3~2ÅU¼ê¿¶3óS endstream endobj 254 0 obj <</Filter/FlateDecode/Length 2855>> stream xÚÅZK ííOk~}¨õªªÞdÙÅ`¦ªTÅÇÇTmÿÚ`Óü6¨bú·}ùïýÂ?Ùþüº}÷lüÄ¡£íõm£ |
| --- | Minor | ³½Þþö¬µü£_Òß7þAþZÖ®üï!ÿ6oZ[Hcùoo/ã=¿Ë4ÒxþQímL£C]/?á»ÊßiNª£Íõå¯Ý~|ÝxJc_öZÿ¾ Î°9åÑ¢I»îúAñ~]äai¿ÖhJ¾ûéWØ~ømûÿÕÀZEuY;¾êðÖ)m=AÕqE6s­úÑu7Æ¤Ýð]üòr±Zó±&àìÇDzîËå(i<ÊÓ¢¹66Mçò¤=Ñ®¿i¶ØJlÖ7×qd$C]	}]'ïªjß¬õä3^Ð ¬ÃÚ­þ_{Në¼ Vùø^}{}Ý².övTvàµHuv«>u¢¼ª½ôã<IWi4/L.UÊb²y7{¼ÉRPÄ×¸]À(KüÇGm|r!UÛº­ Ç¦Â;cÛhÿÏ¤ÔêoÅ²rò¸ùNÖFv[çé­gHnÂ|ú»Fzº ÷ê´¸VÁhOõýt. ¶UdÉú&uòDÎ1z;* "ÕìèÓºnCeû F2¿øÖî¢(¿b[qr<Næ-¸/\ë:rhoÄK£ÌLÓêkÐäxÇ¬æk³µ5Úy;>£¤ |
| --- | Minor | ÷ªOÃ±b7ö+y[ix-XÍ¸i[f¯´Kê@à\á §Ek	Î °O§é9Â=+p£×ÑhÍÛ:ãìÍQó(1Ðr·½_Õ¤ë=ÑÒ§¬Õ© ¸´iLg ï5w²Ã¡c7¶äWfUs¤°IùtKÔtwdÕ5õËÊ`pV-ðtGNu	:T·zÐ¡Ñ£TDÌ¥<näFØùIx®y(¼çÇÂ8Ê4>Ènâ`ê4ñ[h¾®Ùtá .¬KDYeÄ5ô. Vynï6Â |
| --- | Minor | ¬[}. ôs1i!. |
| --- | Minor | Sentence exceeds complexity threshold, split for readability. Applying the split needs --strength moderate or higher. |
| --- | Minor | none (split proposal only; source not rewritten) |
| --- | Minor | none |
| --- | Minor | Check: NEEDS-LLM |
| --- | Minor | Flags:    not-assessed |
| --- | Minor | SENTENCE (Line 51, 947 words, 16 clauses)  [Script] |
| --- | Minor | ¡:*ÉµÙX·9Nõ@íX;¸­ú§ù±.öyèã\Õ2mFÿ½Ä´×©N¾IU]=ºÜÙ÷!oÉÁÈk³zì±ä*£Å7ç§c¹ÖK¿¡u2Õ¿çÍo;|0M¹»´¸º¥{Z{.Ó=FLA±·	Ãüý2\²ø^Ï´çõgÖê£}_=ÎI&(}Ô ¾K´-5¾G£2`[ïûÒÜ;'Ð¥oçÞµ9x´è*Pz»4jÑµ^ZLW0 Y¹ Þý¸ìª,t;[¦qî« rÞDC(5ëÅ@Ñ²Á¾DWI×»;,sMG=ùÎJ§ÅÂÙYó±djÖòæÅØ ÈhÐB;·~	þz+iÒìÏ|a¨g:£ ¬÷_´Nqþb ß½8ágËyñâ)»!ò\ÁÓ~Zw½û"h¯qºÙ¿iª«wPL­kõNY|¡l|Xÿ¶°Z¸DR»Ãù`¢µÃo¾bïª$§;4dG+';I3<Þº¡	Ï)çú1 ­H'>¡lµCÌJÞÕ8Çøäv%w8=/¤ÐYÙ1NyÒ©'FãùÉ ¨Ä¢Ü;Os!î;äÕðæ¤ªËMÔ¦¨lrJB@Ð¢|Òéü 4´ïÅø]g#v6Â=¦NÀ¦ÕR29 |
| --- | Minor | ?ÊF«DÏ{9å%	«9ñ9%úNN·³g |
| --- | Minor | ¬ýÂSáHy²§.áágv×¡/ê?+r*+Z@azïp¦1ÇVFÒ£#K0¶@p^¹¦¬Ñ¢(_MNéj{Qyá0-ì£F9ôlÍ{çdáãÂjßvÂ±?;¬gw+à{[¥E¨äÆÈQ}]Fí+RL3¤o÷ß~:mgüÜ8Þá±ÛþP5÷ã5®pº~'Ðzàw¦[A¤ïÏpýJìÎøî$µÐÜÀ=×ömº®º7ð#ÑÇvt§¿òÈ'øÜsÂéKîÞ=²¯Qdá@XPÁáXYÊHR[2(`o6*oùÞÚõDMTHÒÃèd´ß¸øðì |
| --- | Minor | (­)2¡NE¥±¿É áªe{fûTIÅä¨ÿGã8O=ãðÏR6sÀ´ãÕ7¿id­ðgm´)ÕÿÑ±ã¹Õ¸vÌÚ)XØMÀíy?W:ÓA|¾;ÍBiö,â.W§/G¥Ïãndç¯Ã'Ï!µléTÔÙ£ºCåJJvÐßt¿³dþèÓ»ác°;Z9KR.ES\{àþú4ß¡VMdÏü¿ªiþLrú¥0tå0yè¦«&ÐðAû4sAH.p1§8Ñu*cIÿóþ±»e endstream endobj 259 0 obj <</Filter/FlateDecode/Length 3643>> stream xÚí\K 8!æº§·´'àßa;üÊtuõÒÃÌ¬Q©»N§ãñ9²O?ôIÑ}òpò:nÿ>|Oc¥ÏoO¿zúùoô®8pxzÿ|@ú¢èúE!szÿô§Rh¯è§Õ×¿¼ÿÝéÛ÷åf}Òj*ªø~íËSÎ¨7Ëí.\ÐOýA)0´\PÊÀõlZ Ñ×³U¾Á?îy¢ç"Í@únùäiÄÃüWÊ|Õð¶<ë1x-§Úw²¸"r`"'àæöØE|õûweNó1Ë¢+Ó¾ÑV&Îü¨tÈdëñìdAâÂbA 'kb`]9Æ41Çbæ<µi4æQd¾\aÞ%	t£3³Òä?´_ºbùÊs¾âÕy¤Bh¼[QjieÞÁVÜ­D |
| --- | Minor | ×3"k5YÎI¿ò¦ÎÆÂæéÄé¬ |
| --- | Minor | ='èsQ*V#óÜ³É&2óÆ¤õ9ÌL¬ ÎdÎÊHÑ*¹å!ÂªSv3ÖN-x;×ÙØØ:Û×m1íYUJx³O)#I¶OÙøjS1ÎdvÌ¥G!+Ï"¹ã¼rR=6nÏBÈß=6^¸ÿøá´Þàé§`ÈëD§³Wóÿû!ãS(èFÿ~úãéÅõÌê¦ÌÑzNË9«¬O õgøîíÖw¤wq`Óm¬³Î¾ÊçÝdÉãQ§3ùÌÀÄÌÌbÌ*f§­Ñ7t¶{³]¼WLðì@/f!mÇ¸U1UXëMéÑSOÝFÓ1¸Ah!nÁÑzÌd°ÙDeð¬öVÐ Èß EdÍLÎ"PTÁ þ¸ÎtÁn´I+³~±XËðVÅè¾r+ |
| --- | Minor | @ÔMK,Û>;1â÷x0J» /ù( ù< ®¶§ïï<^[î[ÖÚ[;§ýÁ9úÀCÕPdøi3¡Y?Úlþ¿ÈÞNdðZ+3!3l´2¬¬ÇWrÿ.K%	Áb7ï aéë~#EÂçÀcý)xÌúxÀcÑ÷ÇÌÈ|iÇã²È14yóçÇoÉ:õjÖí<J?z&ÖõÃëúE:Ö |
| --- | Minor | uiLfÅºcõüzÅ;©PÁ«wù³ e´c^2ËAG½á½ãE&Û®Ã£ÞE>%óàÇ¤{£­*62O<à+£9væÇøI¯6[sh¶ãèQØFóEåxg.ð¶âp?FhýÒÅ±¬y Q Tf* Úp_B-7pdmïÜÜc¹éÇ\ËsAÉu}ÃrQêþR²æ Öñ©¸U |
| --- | Minor | *¥;ùIÞßÅy÷Ên b÷Ñ 8A,«~&YuTÓ5-ã@ê ¯¤ëµ9hõ¸+heÂÒ}`zì­^roM¥Rxg]p¤;Æw0ºÚ$ßWF<tÈ©¿GÆ¼j({êA«ñ¬÷±=­cð0Ïyß"0=Ð(8ZÂAúT0ÌA)ÙmYU@pL­5¶ªO¯¤O_Ê£>ÄñUðìKYZ±®ô@±P´:¯úT¶òÜa«=øØÇÊÂÃß­p3ÍBDvÑmä!ÁDJ¡½áAìJ{2³Qqt·x>²í©póÆÇ;!LÐ¹¾Ð`ë:³1üHè,PÎÃÝÈ |
| --- | Minor | ñFÑYqä|¾õ¶à*<ýÐ¾ÐÆ x{[²>¯æì&!©c`ê¢^n?|ÈaÐFò/Qå^FÏmÙ!7¹Ç®²ãÏö×swÀÂ«#BLt¯H2>Wî4·[ØCD¡YüIñÅ|'q¶é´B,Oìø§Í6O<Ü¼Óö¸öM©íL© ýÑ°Ç°N1ºm ÑF¢×Ì}\Z ª2Ù |
| --- | Minor | \Î|:H¤Bc5ýhG |
| --- | Minor | ?if%â°)íUfg`g!apÃ]Ýò] Nì]¦ÌPÒ7gÑr$álïßïnI"eÔ `òÕu¸óÕYàé©À1zs )Û<¬G»î´½p Ð;JÛrA)øRro¶@üÈtIZU3>ÍNÅê½·Ö,æYF3Ô;vòÏ`a;[³íMÍ |
| --- | Minor | ÷%'ùñròY » ¦ÓÙuÝ8kQ»£Ö}YFF#eÙ;¢p+¬ÓÐ+O§¨ KSÎö,£>±/VË­üÄ¤ò+ºøøÊP	keäa¨}a-¦$§Ô3×©z'"B"S¶ÆBÒ!«Æ|õ¥ ¼15í?´i`,¥ÚóK/Ð®Èa !ÞÝÎ¯Ù¥¨NÞ7ç38à(êµjR|m-ÆèGË(<æJ_r§TeªÎÀ|/~Ï@Ê#*,t"5O/-4­½êÐÉ¾òî¤Å%mâær[4ÒFW=n½.RÁZ6åx	'ooô¥bé´75^Á¥·½DÑ%ÉÓ{%wO{åGgW[=ô¬ë#9B%Ì:×:K1¡ÔëÒ`ÆoÝu:¥ùñ hó%¢ð'Y	ûvò­¢BðaÖa3ø°©Ó |
| --- | Minor | . ¬Úî]ÞâôëfYÐ]f7rò_rÕ¾ºoÞ«jJº(lèºr®ÉàæZ¿\PZÖ*ùIX¡ñÃZ	ÿäôAuHZNôÂ8ò;§Rç&)ü	6o}iÎz\ÐyÖ#Î£úÙ¿^A¹D°®²t=¾÷tìA8²æÜI"k&hÌ8õe4ËAæyë¤¢Ì(yfajÆ[Ld;f)ÜÙÙKLÕsÎ¥F°Ï\¦Êm(=ÔO¤fÁcÒOð«¥6]Ç=´P"ÁÂ:`Ó^kßÌã¾nð?h"¢,£i9LW/KÁÉ¿Ö°:SNþËÃõ¼Í0l3ÅXi_­ùIØ5ÆK+ûZ;§4;)ç4«ð0T±C@5ÐßÍó,®¨@"I³æ ×zÐk»9ôÑmÎp,Oÿþá_«ü³NY<¿T |
| --- | Minor | ^e=]vfEZDåå+öô©¬Íðä(a'üh³¼ªI\iá ×aï5Î÷U@R®§TOõktÇ|ªxÞ8f«?Lu®ä ?EHbRGåDÉ+Ïq ±ÃÊÂg©ÖL©Ör¡q³lTñÄZÞÞÎ¶^N,eð)³ý¥§IpgÔd|ú,ûì_´´¼¢ºZ{Ù¿ÒUÉC3_@H©Z¹Ø! |
| --- | Minor | ¡:*ÉµÙX·9Nõ@íX;¸­ú§ù±.öyèã\Õ2mFÿ½Ä´×©N¾IU]=ºÜÙ÷!oÉÁÈk³zì±ä*£Å7ç§c¹ÖK¿¡u2Õ¿çÍo;|0M¹»´¸º¥{Z{.Ó=FLA±·	Ãüý2\²ø^Ï´çõgÖê£}_=ÎI&(}Ô ¾K´-5¾G£2`[ïûÒÜ;'Ð¥oçÞµ9x´è*Pz»4jÑµ^ZLW0 Y¹ Þý¸ìª. t;[¦qî« rÞDC(5ëÅ@Ñ²Á¾DWI×»;. sMG=ùÎJ§ÅÂÙYó±djÖòæÅØ ÈhÐB;·~	þz+iÒìÏ|a¨g:£ ¬÷_´Nqþb ß½8ágËyñâ)»!ò\ÁÓ~Zw½û"h¯qºÙ¿iª«wPL­kõNY|¡l|Xÿ¶°Z¸DR»Ãù`¢µÃo¾bïª$§;4dG+';I3<Þº¡	Ï)çú1 ­H'>¡lµCÌJÞÕ8Çøäv%w8=/¤ÐYÙ1NyÒ©'FãùÉ ¨Ä¢Ü;Os!î;äÕðæ¤ªËMÔ¦¨lrJB@Ð¢|Òéü 4´ïÅø]g#v6Â=¦NÀ¦ÕR29 |
| --- | Minor | ?ÊF«DÏ{9å%	«9ñ9%úNN·³g |
| --- | Minor | ¬ýÂSáHy²§.áágv×¡/ê?+r*+Z@azïp¦1ÇVFÒ£#K0¶@p^¹¦¬Ñ¢(_MNéj{Qyá0-ì£F9ôlÍ{çdáãÂjßvÂ±?;¬gw+à{[¥E¨äÆÈQ}]Fí+RL3¤o÷ß~:mgüÜ8Þá±ÛþP5÷ã5®pº~'Ðzàw¦[A¤ïÏpýJìÎøî$µÐÜÀ=×ömº®º7ð#ÑÇvt§¿òÈ'øÜsÂéKîÞ=²¯Qdá@XPÁáXYÊHR[2(`o6*oùÞÚõDMTHÒÃèd´ß¸øðì |
| --- | Minor | (­)2¡NE¥±¿É áªe{fûTIÅä¨ÿGã8O=ãðÏR6sÀ´ãÕ7¿id­ðgm´)ÕÿÑ±ã¹Õ¸vÌÚ)XØMÀíy?W:ÓA|¾;ÍBiö. â.W§/G¥Ïãndç¯Ã'Ï!µléTÔÙ£ºCåJJvÐßt¿³dþèÓ»ác°;Z9KR.ES\{àþú4ß¡VMdÏü¿ªiþLrú¥0tå0yè¦«&ÐðAû4sAH.p1§8Ñu*cIÿóþ±»e endstream endobj 259 0 obj <</Filter/FlateDecode/Length 3643>> stream xÚí\K 8!æº§·´'àßa;üÊtuõÒÃÌ¬Q©»N§ãñ9²O?ôIÑ}òpò:nÿ>|Oc¥ÏoO¿zúùoô®8pxzÿ|@ú¢èúE!szÿô§Rh¯è§Õ×¿¼ÿÝéÛ÷åf}Òj*ªø~íËSÎ¨7Ëí.\ÐOýA)0´\PÊÀõlZ Ñ×³U¾Á?îy¢ç"Í@únùäiÄÃüWÊ|Õð¶<ë1x-§Úw²¸"r`"'àæöØE|õûweNó1Ë¢+Ó¾ÑV&Îü¨tÈdëñìdAâÂbA 'kb`]9Æ41Çbæ<µi4æQd¾\aÞ%	t£3³Òä?´_ºbùÊs¾âÕy¤Bh¼[QjieÞÁVÜ­D |
| --- | Minor | ×3"k5YÎI¿ò¦ÎÆÂæéÄé¬ |
| --- | Minor | ='èsQ*V#óÜ³É&2óÆ¤õ9ÌL¬ ÎdÎÊHÑ*¹å!ÂªSv3ÖN-x;×ÙØØ:Û×m1íYUJx³O)#I¶OÙøjS1ÎdvÌ¥G!+Ï"¹ã¼rR=6nÏBÈß=6^¸ÿøá´Þàé§`ÈëD§³Wóÿû!ãS(èFÿ~úãéÅõÌê¦ÌÑzNË9«¬O õgøîíÖw¤wq`Óm¬³Î¾ÊçÝdÉãQ§3ùÌÀÄÌÌbÌ*f§­Ñ7t¶{³]¼WLðì@/f!mÇ¸U1UXëMéÑSOÝFÓ1¸Ah!nÁÑzÌd°ÙDeð¬öVÐ Èß EdÍLÎ"PTÁ þ¸ÎtÁn´I+³~±XËðVÅè¾r+ |
| --- | Minor | @ÔMK. Û>;1â÷x0J» /ù( ù< ®¶§ïï<^[î[ÖÚ[;§ýÁ9úÀCÕPdøi3¡Y?Úlþ¿ÈÞNdðZ+3!3l´2¬¬ÇWrÿ.K%	Áb7ï aéë~#EÂçÀcý)xÌúxÀcÑ÷ÇÌÈ|iÇã²È14yóçÇoÉ:õjÖí<J?z&ÖõÃëúE:Ö |
| --- | Minor | uiLfÅºcõüzÅ;©PÁ«wù³ e´c^2ËAG½á½ãE&Û®Ã£ÞE>%óàÇ¤{£­*62O<à+£9væÇøI¯6[sh¶ãèQØFóEåxg.ð¶âp?FhýÒÅ±¬y Q Tf* Úp_B-7pdmïÜÜc¹éÇ\ËsAÉu}ÃrQêþR²æ Öñ©¸U |
| --- | Minor | *¥;ùIÞßÅy÷Ên b÷Ñ 8A. «~&YuTÓ5-ã@ê ¯¤ëµ9hõ¸+heÂÒ}`zì­^roM¥Rxg]p¤;Æw0ºÚ$ßWF<tÈ©¿GÆ¼j({êA«ñ¬÷±=­cð0Ïyß"0=Ð(8ZÂAúT0ÌA)ÙmYU@pL­5¶ªO¯¤O_Ê£>ÄñUðìKYZ±®ô@±P´:¯úT¶òÜa«=øØÇÊÂÃß­p3ÍBDvÑmä!ÁDJ¡½áAìJ{2³Qqt·x>²í©póÆÇ;!LÐ¹¾Ð`ë:³1üHè. PÎÃÝÈ |
| --- | Minor | ñFÑYqä|¾õ¶à*<ýÐ¾ÐÆ x{[²>¯æì&!©c`ê¢^n?|ÈaÐFò/Qå^FÏmÙ!7¹Ç®²ãÏö×swÀÂ«#BLt¯H2>Wî4·[ØCD¡YüIñÅ|'q¶é´B. Oìø§Í6O<Ü¼Óö¸öM©íL© ýÑ°Ç°N1ºm ÑF¢×Ì}\Z ª2Ù |
| --- | Minor | \Î|:H¤Bc5ýhG |
| --- | Minor | ?if%â°)íUfg`g!apÃ]Ýò] Nì]¦ÌPÒ7gÑr$álïßïnI"eÔ `òÕu¸óÕYàé©À1zs )Û<¬G»î´½p Ð;JÛrA)øRro¶@üÈtIZU3>ÍNÅê½·Ö. æYF3Ô;vòÏ`a;[³íMÍ |
| --- | Minor | ÷%'ùñròY » ¦ÓÙuÝ8kQ»£Ö}YFF#eÙ;¢p+¬ÓÐ+O§¨ KSÎö. £>±/VË­üÄ¤ò+ºøøÊP	keäa¨}a-¦$§Ô3×©z'"B"S¶ÆBÒ!«Æ|õ¥ ¼15í?´i`. ¥ÚóK/Ð®Èa !ÞÝÎ¯Ù¥¨NÞ7ç38à(êµjR|m-ÆèGË(<æJ_r§TeªÎÀ|/~Ï@Ê#*. t"5O/-4­½êÐÉ¾òî¤Å%mâær[4ÒFW=n½.RÁZ6åx	'ooô¥bé´75^Á¥·½DÑ%ÉÓ{%wO{åGgW[=ô¬ë#9B%Ì:×:K1¡ÔëÒ`ÆoÝu:¥ùñ hó%¢ð'Y	ûvò­¢BðaÖa3ø°©Ó |
| --- | Minor | . ¬Úî]ÞâôëfYÐ]f7rò_rÕ¾ºoÞ«jJº(lèºr®ÉàæZ¿\PZÖ*ùIX¡ñÃZ	ÿäôAuHZNôÂ8ò;§Rç&)ü	6o}iÎz\ÐyÖ#Î£úÙ¿^A¹D°®²t=¾÷tìA8²æÜI"k&hÌ8õe4ËAæyë¤¢Ì(yfajÆ[Ld;f)ÜÙÙKLÕsÎ¥F°Ï\¦Êm(=ÔO¤fÁcÒOð«¥6]Ç=´P"ÁÂ:`Ó^kßÌã¾nð?h"¢. £i9LW/KÁÉ¿Ö°:SNþËÃõ¼Í0l3ÅXi_­ùIØ5ÆK+ûZ;§4;)ç4«ð0T±C@5ÐßÍó. ®¨@"I³æ ×zÐk»9ôÑmÎp. Oÿþá_«ü³NY<¿T |
| --- | Minor | ^e=]vfEZDåå+öô©¬Íðä(a'üh³¼ªI\iá ×aï5Î÷U@R®§TOõktÇ|ªxÞ8f«?Lu®ä ?EHbRGåDÉ+Ïq ±ÃÊÂg©ÖL©Ör¡q³lTñÄZÞÞÎ¶^N. eð)³ý¥§IpgÔd|ú. ûì_´´¼¢ºZ{Ù¿ÒUÉC3_@H©Z¹Ø!. |
| --- | Minor | Sentence exceeds complexity threshold, split for readability. Applying the split needs --strength moderate or higher. |
| --- | Minor | none (split proposal only; source not rewritten) |
| --- | Minor | none |
| --- | Minor | Check: NEEDS-LLM |
| --- | Minor | Flags:    not-assessed |
| --- | Minor | SENTENCE (Line 51, 209 words, 2 clauses)  [Script] |
| --- | Minor | ]©OÍày½grÍÙÀY%ÁïoÁ,ïa;¿³i¹¶"ÇÆ]ÞíJ+ßB ®:»Àm?~RJ/;	íÔx<Ù< Øte+¼áã²]/}é»t\Òúãs_MË-ü«Ë§ñW%r«Ó°¸ÝA?ÓÙ,©À¥©¶À[µ<_@aýa2¯hQÌ"êÊ3D¦wab¾j£gÝÊë5 |
| --- | Minor | YFvPZUSe=»TURôZ¿©ã·ª~®{	Å«}ÌPþ 8äÛîwÝÒã6JáüË/×ù(	ú£0Ó¯ÉoôûÉý_Úð1¶ià3æ¡·_Ãç¬>ü´x(Ýy.'"ÓéþÒ:Ìt&Z;A¸áÑÂ%/4öiQ+UvïlÎÍvÈ£Vã·óû§È&¢r/¿;õº ÷¸ZåÆÇÝõê.Jv$ô<%Ý±¨ð(ß¡ûò.Ýßd·y0Wü ¦N%3¬2%j4:£ô]MGg#µTúÎ©üëö¤=Eîà«pà×ÖÜC)2{S»Tæ5ÿændùêuä»G]Çq¡Ã»þìHfaÐ§DÝ\°§	Þëi)Ã |
| --- | Minor | »VKÃ¡Fi¹Ê»AÜ$¯4+7ÐÏÛgYÕÇíËÝ5ÖÞ»­£4¶ê.;7v²Eì%õõìÐ¡tp}t­+¶¬´¢ÔÖ¹Çø¾¹tZÕb"O¸_Mj»»Ww4ô©!^NN%6¬åÜÔ<ô|a§Õi |
| --- | Minor | ;R/HºOØåè¶0É |
| --- | Minor | ¸sSÊ²9ËÙÃæ¬ÂÀôÆÃúheG-×QÊàËí qD_x	PMîµ¸üVÐñFclì^¸¨ |
| --- | Minor | ÷ã	ÇlEî}Çú¤e5P©NúïÂQ0hð÷í6ôÕi·Uÿ´C"¥¦ÇUgá·DÀÅ{TBíÊ{öøJUÙg¨à»ÖeE<4¿éé­wFbt¯ÈÝæÙ°MëÂërç:¹û?ín¸çßÔÁ·cG¨ïD~ûþôýXó |
| --- | Minor | ]©OÍày½grÍÙÀY%ÁïoÁ. ïa;¿³i¹¶"ÇÆ]ÞíJ+ßB ®:»Àm?~RJ/;	íÔx<Ù< Øte+¼áã²]/}é»t\Òúãs_MË-ü«Ë§ñW%r«Ó°¸ÝA?ÓÙ. ©À¥©¶À[µ<_@aýa2¯hQÌ"êÊ3D¦wab¾j£gÝÊë5 |
| --- | Minor | YFvPZUSe=»TURôZ¿©ã·ª~®{	Å«}ÌPþ 8äÛîwÝÒã6JáüË/×ù(	ú£0Ó¯ÉoôûÉý_Úð1¶ià3æ¡·_Ãç¬>ü´x(Ýy.'"ÓéþÒ:Ìt&Z;A¸áÑÂ%/4öiQ+UvïlÎÍvÈ£Vã·óû§È&¢r/¿;õº ÷¸ZåÆÇÝõê.Jv$ô<%Ý±¨ð(ß¡ûò.Ýßd·y0Wü ¦N%3¬2%j4:£ô]MGg#µTúÎ©üëö¤=Eîà«pà×ÖÜC)2{S»Tæ5ÿændùêuä»G]Çq¡Ã»þìHfaÐ§DÝ\°§	Þëi)Ã |
| --- | Minor | »VKÃ¡Fi¹Ê»AÜ$¯4+7ÐÏÛgYÕÇíËÝ5ÖÞ»­£4¶ê.;7v²Eì%õõìÐ¡tp}t­+¶¬´¢ÔÖ¹Çø¾¹tZÕb"O¸_Mj»»Ww4ô©!^NN%6¬åÜÔ<ô|a§Õi |
| --- | Minor | ;R/HºOØåè¶0É |
| --- | Minor | ¸sSÊ²9ËÙÃæ¬ÂÀôÆÃúheG-×QÊàËí qD_x	PMîµ¸üVÐñFclì^¸¨ |
| --- | Minor | ÷ã	ÇlEî}Çú¤e5P©NúïÂQ0hð÷í6ôÕi·Uÿ´C"¥¦ÇUgá·DÀÅ{TBíÊ{öøJUÙg¨à»ÖeE<4¿éé­wFbt¯ÈÝæÙ°MëÂërç:¹û?ín¸çßÔÁ·cG¨ïD~ûþôýXó. |
| --- | Minor | Sentence exceeds complexity threshold, split for readability. Applying the split needs --strength moderate or higher. |
| --- | Minor | none (split proposal only; source not rewritten) |
| --- | Minor | none |
| --- | Minor | Check: NEEDS-LLM |
| --- | Minor | Flags:    not-assessed |
| --- | Minor | SENTENCE (Line 663, 276 words, 5 clauses)  [Script] |
| --- | Minor | endstream endobj 266 0 obj <</Length1 3352/Length 2202/Filter/FlateDecode>> stream xÍU{PT×ÿîý³»ìÅ ".Âd×Gâ+	b±JÂÊòÜVA¢5k0ã_)«Æ¤)¶)i¡j5m'ÃmÆ¦é4Ú6ÉL;gLgbÃ¥ß^6©fþÛ3g¿ï÷½ÏwÏ9K 9ùG£¬¤t¹ÈB¤¤³tRYåªª®Ïaì.«z´øpê3W3·ªj¶7t¬#g¼¦®Õ¶.`üWÆ¡º®N÷~ßÙ[Dj%Ë^l7¶~Ü}ó ¢úFG¬<I'6¶6T?»ÐÍø)Æêý¸SCDRækbýõ=Æ[g7µvnI]L>ÆÇ§Úëüä§Æ?gÔêßõcÆW¢õ·ù[ë3óìaÌùáöNÿÍ®5DÖçX?'¼©>¼y«åØæqö&&Ê$MYtÙ(2H)Y¶¢â¸{<ÆÇc¶z/Í!aê§ÔmÝ¢ìÆMõAÊù;Û(ûk1?1E9À9Húd?ÍS2¢t¼ïSÂ%X,	jÔwÇ |
| --- | Minor | ¥ÎZÍÐ£ÖVå/±:&b+Ý¬¨bbA¹L-LÞ#G0k2éøù/*¾1ÑÜ¯ºÁ6±ÅÕàÂÄ"©Ø¨µCô.Ï÷[A-´vÑIæ?¢m¦üN| £¶ïÑÇvjt*³Íø#ÇÇºØ¾ñIÚ`êocÔG1ª>I**«4=NÒ Ñez½Ké |
| --- | Minor | ·ÞçYÌÑÓÛôò,Q®QöQùI¦)6yki¡ |
| --- | Minor | 9?¥õfæ¨¬E^³h©÷ù6G?3!WòÕ¨E²w¨*x¥;©EÔòÌ1g¹¿=¨ê6ÎÛ/ªëÕ<£phQ?@¹Þ®ôa^j´~|B'ý å%Zn]nIT,ÖU³v|ÊQË4ª¥ª9ÂJí£Êû4:gªB³ÜAÕSÔYëþõºÌüY_nÕ=Hö­î¡ññÊµbª\7(Óá¬ß¤¼?«¢r­{ð7¥%±¨¥µ%,«ZËl±å¥%ùg¿<2>ãòÑ«á~§eÍ÷¹²ægZ³ $^ñY3ø¬nmäóTµ,u¤M½y:Uù4õµ±µh@3^{§kDk½«ÎåßÑ1_zuìý7>3DMåpwÔù>XaRÎ¨¾¥xDuökÊ |
| --- | Minor | Ñ£äôkc·´¾OÎ.|UûB{õÕAMä:å¥`ÐøãØïZZ7wLPÝ»cêºþ×ãÚo=¼è3g^ßnOúÓôóò±öÜ¸ëæÎ¿ºëüÊ´Óì~^þÏV{.øí½sXDôDÃðêáÝÜ¿. |
| --- | Minor | endstream endobj 266 0 obj <</Length1 3352/Length 2202/Filter/FlateDecode>> stream xÍU{PT×ÿîý³»ìÅ ".Âd×Gâ+	b±JÂÊòÜVA¢5k0ã_)«Æ¤)¶)i¡j5m'ÃmÆ¦é4Ú6ÉL;gLgbÃ¥ß^6©fþÛ3g¿ï÷½ÏwÏ9K 9ùG£¬¤t¹ÈB¤¤³tRYåªª®Ïaì.«z´øpê3W3·ªj¶7t¬#g¼¦®Õ¶.`üWÆ¡º®N÷~ßÙ[Dj%Ë^l7¶~Ü}ó ¢úFG¬<I'6¶6T?»ÐÍø)Æêý¸SCDRækbýõ=Æ[g7µvnI]L>ÆÇ§Úëüä§Æ?gÔêßõcÆW¢õ·ù[ë3óìaÌùáöNÿÍ®5DÖçX?'¼©>¼y«åØæqö&&Ê$MYtÙ(2H)Y¶¢â¸{<ÆÇc¶z/Í!aê§ÔmÝ¢ìÆMõAÊù;Û(ûk1?1E9À9Húd?ÍS2¢t¼ïSÂ%X. 	jÔwÇ |
| --- | Minor | ¥ÎZÍÐ£ÖVå/±:&b+Ý¬¨bbA¹L-LÞ#G0k2éøù/*¾1ÑÜ¯ºÁ6±ÅÕàÂÄ"©Ø¨µCô.Ï÷[A-´vÑIæ?¢m¦üN| £¶ïÑÇvjt*³Íø#ÇÇºØ¾ñIÚ`êocÔG1ª>I**«4=NÒ Ñez½Ké |
| --- | Minor | ·ÞçYÌÑÓÛôò. Q®QöQùI¦)6yki¡ |
| --- | Minor | 9?¥õfæ¨¬E^³h©÷ù6G?3!WòÕ¨E²w¨*x¥;©EÔòÌ1g¹¿=¨ê6ÎÛ/ªëÕ<£phQ?@¹Þ®ôa^j´~|B'ý å%Zn]nIT. ÖU³v|ÊQË4ª¥ª9ÂJí£Êû4:gªB³ÜAÕSÔYëþõºÌüY_nÕ=Hö­î¡ññÊµbª\7(Óá¬ß¤¼?«¢r­{ð7¥%±¨¥µ%. «ZËl±å¥%ùg¿<2>ãòÑ«á~§eÍ÷¹²ægZ³ $^ñY3ø¬nmäóTµ. u¤M½y:Uù4õµ±µh@3^{§kDk½«ÎåßÑ1_zuìý7>3DMåpwÔù>XaRÎ¨¾¥xDuökÊ |
| --- | Minor | Ñ£äôkc·´¾OÎ.|UûB{õÕAMä:å¥`ÐøãØïZZ7wLPÝ»cêºþ×ãÚo=¼è3g^ßnOúÓôóò±öÜ¸ëæÎ¿ºëüÊ´Óì~^þÏV{.øí½sXDôDÃðêáÝÜ¿.. |
| --- | Minor | Sentence exceeds complexity threshold, split for readability. Applying the split needs --strength moderate or higher. |
| --- | Minor | none (split proposal only; source not rewritten) |
| --- | Minor | none |
| --- | Minor | Check: NEEDS-LLM |
| --- | Minor | Flags:    not-assessed |
| --- | Minor | SENTENCE (Line 663, 254 words, 3 clauses)  [Script] |
| --- | Minor | ÿû6üÞMÔ`Qãi&õE{KÒÍW5åoö[Ä3?b¾Q^á¾Äxoøïc<è^úswðÒ¸o¡lÅMK©Â´6Q35Ruß:Êcê¥B>æ6°ï\3ë;xm¢z®»f±´ÚØ¾¹" ñtó |
| --- | Minor | êÖ³OÿØÒÆ¯W=r?­¡ÍlQÇ¶~ÒhZºÆws6þ |
| --- | Minor | ÛÌvnöoç¼~S÷õ8Uffîy9çöÇ|¾ÉÆ}ÕSÞÁ|»ÕËuúhî]ÞÿöÍ¿Ë×|MÇ?ãµ¿Òó«ÜùEA8ìR»õë¿2ðW¯dË«\ÕÅlüÒËräå .åàb |
| --- | Minor | ~ÁÛ	NÀó¼àÅy |
| --- | Minor | ^¼eà7 |
| --- | Minor | &ß¸Á2üÄÀëüØÀpv QÕ0zñZ ?ÈÀ/^>/8À©Þ In÷"§¶%Ë§\Øïöb«[lx²Ë-¼®Íé²ËÍéèd§ÎtØd`cØ.7ÛÖE{m­Kd[­K &Ê¡nLDP-²å6e³¦ÆÙ4¦nÑØà5hÔEõlT êR±Áß@í²ÖÀxÜ@õøNXWµ¾m`Í05PÀj |
| --- | Minor | xQ¹*YVF°*+ôb¬HÀò ÊgÄÉò^<ìE²Ìe)(Um²t2JºdIKr©ÅE	²Ø"=^%@ícx¨KD¾\ò-,^¤ÉÅX´Ð&iX¤6,x0E.¨Á8å)xÀùvÌ30w&çãsÉ9|^ô¹à½?^zmðN|ûãQ8;M`vAªÙEAM¤¢ [äÇd~/fÍÔä¬ ÌäMÌÔ0S÷qé÷[(óËå"I{ÀcOdg¥Èì*d±[V ²t1#î4Y÷t§t§Á}QLçdÓÞ-2lÈÐÅ´,¤'cj6¦L.Sª0£N.D{8é=&9ªi25ÍåM.RØ.eNn¯Ó£É\r/XdÀÎìi°ë"Ñ@ý llc >8«SÆi°:a^i@²ôBp0ªÚ T(CJ`ç>eæÿí ÿuÿuð¿ò¿ 2Þ´² endstream endobj 268 0 obj <</Length 29/Filter/FlateDecode>> stream xc`e 0 FÁ(£`P° "÷  |
| --- | Minor | ÿû6üÞMÔ`Qãi&õE{KÒÍW5åoö[Ä3?b¾Q^á¾Äxoøïc<è^úswðÒ¸o¡lÅMK©Â´6Q35Ruß:Êcê¥B>æ6°ï\3ë;xm¢z®»f±´ÚØ¾¹" ñtó |
| --- | Minor | êÖ³OÿØÒÆ¯W=r?­¡ÍlQÇ¶~ÒhZºÆws6þ |
| --- | Minor | ÛÌvnöoç¼~S÷õ8Uffîy9çöÇ|¾ÉÆ}ÕSÞÁ|»ÕËuúhî]ÞÿöÍ¿Ë×|MÇ?ãµ¿Òó«ÜùEA8ìR»õë¿2ðW¯dË«\ÕÅlüÒËräå .åàb |
| --- | Minor | ~ÁÛ	NÀó¼àÅy |
| --- | Minor | ^¼eà7 |
| --- | Minor | &ß¸Á2üÄÀëüØÀpv QÕ0zñZ ?ÈÀ/^>/8À©Þ In÷"§¶%Ë§\Øïöb«[lx²Ë-¼®Íé²ËÍéèd§ÎtØd`cØ.7ÛÖE{m­Kd[­K &Ê¡nLDP-²å6e³¦ÆÙ4¦nÑØà5hÔEõlT êR±Áß@í²ÖÀxÜ@õøNXWµ¾m`Í05PÀj |
| --- | Minor | xQ¹*YVF°*+ôb¬HÀò ÊgÄÉò^<ìE²Ìe)(Um²t2JºdIKr©ÅE	²Ø"=^%@ícx¨KD¾\ò-. ^¤ÉÅX´Ð&iX¤6. x0E.¨Á8å)xÀùvÌ30w&çãsÉ9|^ô¹à½?^zmðN|ûãQ8;M`vAªÙEAM¤¢ [äÇd~/fÍÔä¬ ÌäMÌÔ0S÷qé÷[(óËå"I{ÀcOdg¥Èì*d±[V ²t1#î4Y÷t§t§Á}QLçdÓÞ-2lÈÐÅ´. ¤'cj6¦L.Sª0£N.D{8é=&9ªi25ÍåM.RØ.eNn¯Ó£É\r/XdÀÎìi°ë"Ñ@ý llc >8«SÆi°:a^i@²ôBp0ªÚ T(CJ`ç>eæÿí ÿuÿuð¿ò¿ 2Þ´² endstream endobj 268 0 obj <</Length 29/Filter/FlateDecode>> stream xc`e 0 FÁ(£`P° "÷ . |
| --- | Minor | Sentence exceeds complexity threshold, split for readability. Applying the split needs --strength moderate or higher. |
| --- | Minor | none (split proposal only; source not rewritten) |
| --- | Minor | none |
| --- | Minor | Check: NEEDS-LLM |
| --- | Minor | Flags:    not-assessed |
| --- | Minor | SENTENCE (Line 685, 208 words, 4 clauses)  [Script] |
| --- | Minor | endstream endobj 269 0 obj <</Length 236/Filter/FlateDecode>> stream x]P=kÃ0Ýõ+nL ÄÍh%]<´)u:ú8A-	Yüï{Zz =îÝ½ãñø¥éMÀß£W&0Öé³_¢B8ZÇN |
| --- | Minor | «ÒOW~5À8uN8õÎxÖ¶À?h8§¸ÂîY{{ ü5FëFØ}^J |
| --- | Minor | _8¡Kpd] |
| --- | Minor | {áML¼½¦¹Mëd·5 4¥?UKÊkPµGªZCÕ1túß¼©*i¶õ³¤õ ÷¢¤Èt{ÅG>÷+ÌsmµÄHKVÅj6inq²*¿o±yÉ endstream endobj 273 0 obj <</Length1 13984/Length 9417/Filter/FlateDecode>> stream xÍzy`TÕùè9÷ÜeæÎvgÏL¶le²0!@-ìÙ dQ·ý/£ÿø|äfíÃÛú¡|.¸O½øßÍÜ§¼r³µ´ÿz·ÖýÞ/é¿Á¢ßÅÿ#DÏ}ëÜ÷¿ú)ß(nî;)8'8FÏ	Ï¢>5áÖM/ÿtû·wô;*û_1üçc¯ÿÃI çqÔ,ÈlÈb%¢ ¡;ëÆPià²¹ÝÐ	=É%4±À<O8cöæð¯hþr$ýxbÃñåÛ`H¸D¡VÛ,ÚÏ8wÜ3@V÷£hÆ£Ih:ª@Î@À_¡tð/!` Ui 3-D÷ÁËÁKÁwï//|;x6øËàà©àáàÁàÁÛ÷þO~!ÿöpKR× |
| --- | Minor | G:¢òT©ÊBåü'.Z(Ââ;8\¨fÊPFW.oPÆB80 3Iá ,P."4'\ìP(« P­Xe1h(# &(^,¢%@ß£èm¸.@mªFõh-ÚõOQÚÿ:«¡ô¼ÏQØè(N8êã¨y²áÝ§ ? |
| --- | Minor | endstream endobj 269 0 obj <</Length 236/Filter/FlateDecode>> stream x]P=kÃ0Ýõ+nL ÄÍh%]<´)u:ú8A-	Yüï{Zz =îÝ½ãñø¥éMÀß£W&0Öé³_¢B8ZÇN |
| --- | Minor | «ÒOW~5À8uN8õÎxÖ¶À?h8§¸ÂîY{{ ü5FëFØ}^J |
| --- | Minor | _8¡Kpd] |
| --- | Minor | {áML¼½¦¹Mëd·5 4¥?UKÊkPµGªZCÕ1túß¼©*i¶õ³¤õ ÷¢¤Èt{ÅG>÷+ÌsmµÄHKVÅj6inq²*¿o±yÉ endstream endobj 273 0 obj <</Length1 13984/Length 9417/Filter/FlateDecode>> stream xÍzy`TÕùè9÷ÜeæÎvgÏL¶le²0!@-ìÙ dQ·ý/£ÿø|äfíÃÛú¡|.¸O½øßÍÜ§¼r³µ´ÿz·ÖýÞ/é¿Á¢ßÅÿ#DÏ}ëÜ÷¿ú)ß(nî;)8'8FÏ	Ï¢>5áÖM/ÿtû·wô;*û_1üçc¯ÿÃI çqÔ. ÈlÈb%¢ ¡;ëÆPià²¹ÝÐ	=É%4±À<O8cöæð¯hþr$ýxbÃñåÛ`H¸D¡VÛ. ÚÏ8wÜ3@V÷£hÆ£Ih:ª@Î@À_¡tð/!` Ui 3-D÷ÁËÁKÁwï//|;x6øËàà©àáàÁàÁÛ÷þO~!ÿöpKR× |
| --- | Minor | G:¢òT©ÊBåü'.Z(Ââ;8\¨fÊPFW.oPÆB80 3Iá . P."4'\ìP(« P­Xe1h(# &(^. ¢%@ß£èm¸.@mªFõh-ÚõOQÚÿ:«¡ô¼ÏQØè(N8êã¨y²áÝ§ ?. |
| --- | Minor | Sentence exceeds complexity threshold, split for readability. Applying the split needs --strength moderate or higher. |
| --- | Minor | none (split proposal only; source not rewritten) |
| --- | Minor | none |
| --- | Minor | Check: NEEDS-LLM |
| --- | Minor | Flags:    not-assessed |
| --- | Minor | SENTENCE (Line 685, 474 words, 11 clauses)  [Script] |
| --- | Minor | ¦ÖãÎ1÷0)¬uèç`þhìw>ìtî\A{	å¥{M&ðzÌ­À%µlü8ÊP+3L¾Íh ¾«1=Âs,a0ò{¤&q|y|ç,Ï/½éþï5=àé@E&ÏÑ`°hÉwpQ$QÓÁ&ÆòÏ^~îX4ËÓqvÌèð¬cÊFCß´YP¥-èþ1£©8ÃÞó aT3Kð%¦Yué%±`F¥¿àeõÚ½%R³d@¾¼ßFÝ Ù@ôÒÅÎÖ;gaF6?_ÊÏ/9Ú2½tíjèN½ËÊ8(;à°Ûøø¸¤×'ååN7©rð)s§L¦ûZ¼Ì¶¿uà{âe+ªÐó*}Yáí6-oÒEÀ¼×®Âþº®]º³³ÄÄÇ1fÉâCf	eèÙ¸{×®Ý´üUù36ÿõ¯q§ã"¥CyVyNéwáE¸ïR*­Ê£J%`yÔþì@DËå(¶¬ )ç¹Ég1ÇWið¤Ì`ÀtÒÅÎÎÎ(ójàZ§9ÏÔØ¯ýª8Oì§Ïz |
| --- | Minor | aRÒO |
| --- | Minor | .µäÁÚL- <A² ãÍñ¹Äl³×ã1«\Àµ0[Íþþ]½Ñ\M­íF0HS`Qh²ìÕÛÉrwWeXf¶ôN$b'¯1¶è¢¥k¯^zóòò`ÇÝ×»n	6%ë ÅB]¡¾ÐVhçp)7àì k·hcoì!àIñq<æ×¼_y_GèµLÝÒaø«~¼¡m[Å¼ü?þ@9ïwG}qçï6ì<°òu8ì·öËkr­¨Åå¢¨E=Zb Î}Â»zò/æ_ |
| --- | Minor | É,Q:s@ç2µñh=H:±C?ýîz3M¿(lQ)l+Da9BÝx0Yq0Éâ f°8' ¥¨µ}SxÍÙÌÛ CôÎúº·ÙrG+¿Æ7»ç3¯ÆÉµ±Fùâ¹äw*¿h§G|	UØckcâ+"«ìeI1ÆAx]Ïk¹]óÕ[Ý<z¸%'jõZ8³Æª· ³9Eb;Å3Åk)M ñÆnsÊ9d·¡xU¼ÓA9'6ïÚµ¹mÇ®WF?[ûGL+Wz¯ñHxÇów×ë\túDáùÓ§Ïÿòµ7ße¾8A¹öÅeP&|/^¹^Q­ü,ÅnsX;3QA*ìÚSEjULYVBÞÂùô\:â#í<ïóê²@ô »°ìõ©í»Ý y¸oßÙA¤_]Áv3pPn^ØdWÛy¤ |
| --- | Minor | +Z6nlY±¡öÀ	åú7Wþvâç;üæý÷¿yïÚ{èÐÞ'"ëvíZ·~×®³Îsí¿»|ùwíç×>þðºª¥QöuÜS ÑByèÈÇø¦$èÑÄ1É	Ä0¦Y;±ÙÔ,	ÍiÚÍi¹S|Éã¸H~E£,ÑÃø¨Èa)"ðMéí KæÅPW~w·ÔÝ	}´;üÈJ4OBx9AÎTõò%% ±Û,NtÈuò ¾$&g %wPh¥H#!äô#gº­ôàï°tÛÐ=U­±¤cæ[Ï^Ó{àã²Z¥ûé[X½fÕJ\|ú]<gÙ¤)Ê«Êg¸mIÓÚuÍ÷mùfjÑ³g¿-º¥§'ñÆñº3ÓWoNò*kÿþòùe­&®nYÇ¾v®¼Ýþ=s?[¡\SÎÜVÕú£O´ü1Ð5x |
| --- | Minor | À3 lÏÉw"jAr%g13ØRÚ6ZÐXÒF(:=c4a2Ãë¤×¶+³d2t@bdÕ+8&³ü®«ÎÀÅ«°Aà¾rî+ú'iTã ¨]áXdX ÙaB&l2Ll2Ì'~s§zïÕâlÔxI¶?Î Êrª¿¬ÓÒ_pnT ¸}#³ÝÞ³x!~oÆ¶öúÄ?ýóõë~æ½,¼ñ·Êç,ÆÑñ=øçòå§Ç_ '÷²rTy®ý	Ø_=p&8cG²Ïôyá ]Eê¸¹V\§»Èn2ÚDÉÈ³(Á"¯öè \ì¼*uJÝê:ºà<:¥.¥++7|-Þp=Û^â{¦¥· +-- óçjÕ(«è)Ò±ÞûoRê@©4l¤Yk¨3iÙÐÊèr²È]e+E¦h£Þ$ñFgb,%XWlàv#uÄãÉòÜá!@8 QÝÿ \3u @IOÈ¹Øø?QóJý¯KÏq×jåÜAåy¥ "âUØü8ë<ö¢rçÆÔô^<?gã¹ø'Có'PÌQ  åÊ6¯ÓÌeQ£Å	È,ÎAOW §+ |
| --- | Minor | ¦ÖãÎ1÷0)¬uèç`þhìw>ìtî\A{	å¥{M&ðzÌ­À%µlü8ÊP+3L¾Íh ¾«1=Âs. a0ò{¤&q|y|ç. Ï/½éþï5=àé@E&ÏÑ`°hÉwpQ$QÓÁ&ÆòÏ^~îX4ËÓqvÌèð¬cÊFCß´YP¥-èþ1£©8ÃÞó aT3Kð%¦Yué%±`F¥¿àeõÚ½%R³d@¾¼ßFÝ Ù@ôÒÅÎÖ;gaF6?_ÊÏ/9Ú2½tíjèN½ËÊ8(;à°Ûøø¸¤×'ååN7©rð)s§L¦ûZ¼Ì¶¿uà{âe+ªÐó*}Yáí6-oÒEÀ¼×®Âþº®]º³³ÄÄÇ1fÉâCf	eèÙ¸{×®Ý´üUù36ÿõ¯q§ã"¥CyVyNéwáE¸ïR*­Ê£J%`yÔþì@DËå(¶¬ )ç¹Ég1ÇWið¤Ì`ÀtÒÅÎÎÎ(ójàZ§9ÏÔØ¯ýª8Oì§Ïz |
| --- | Minor | aRÒO |
| --- | Minor | .µäÁÚL- <A² ãÍñ¹Äl³×ã1«\Àµ0[Íþþ]½Ñ\M­íF0HS`Qh²ìÕÛÉrwWeXf¶ôN$b'¯1¶è¢¥k¯^zóòò`ÇÝ×»n	6%ë ÅB]¡¾ÐVhçp)7àì k·hcoì!àIñq<æ×¼_y_GèµLÝÒaø«~¼¡m[Å¼ü?þ@9ïwG}qçï6ì<°òu8ì·öËkr­¨Åå¢¨E=Zb Î}Â»zò/æ_ |
| --- | Minor | É. Q:s@ç2µñh=H:±C?ýîz3M¿(lQ)l+Da9BÝx0Yq0Éâ f°8' ¥¨µ}SxÍÙÌÛ CôÎúº·ÙrG+¿Æ7»ç3¯ÆÉµ±Fùâ¹äw*¿h§G|	UØckcâ+"«ìeI1ÆAx]Ïk¹]óÕ[Ý<z¸%'jõZ8³Æª· ³9Eb;Å3Åk)M ñÆnsÊ9d·¡xU¼ÓA9'6ïÚµ¹mÇ®WF?[ûGL+Wz¯ñHxÇów×ë\túDáùÓ§Ïÿòµ7ße¾8A¹öÅeP&|/^¹^Q­ü. ÅnsX;3QA*ìÚSEjULYVBÞÂùô\:â#í<ïóê²@ô »°ìõ©í»Ý y¸oßÙA¤_]Áv3pPn^ØdWÛy¤ |
| --- | Minor | +Z6nlY±¡öÀ	åú7Wþvâç;üæý÷¿yïÚ{èÐÞ'"ëvíZ·~×®³Îsí¿»|ùwíç×>þðºª¥QöuÜS ÑByèÈÇø¦$èÑÄ1É	Ä0¦Y;±ÙÔ. 	ÍiÚÍi¹S|Éã¸H~E£. ÑÃø¨Èa)"ðMéí KæÅPW~w·ÔÝ	}´;üÈJ4OBx9AÎTõò%% ±Û. NtÈuò ¾$&g %wPh¥H#!äô#gº­ôàï°tÛÐ=U­±¤cæ[Ï^Ó{àã²Z¥ûé[X½fÕJ\|ú]<gÙ¤)Ê«Êg¸mIÓÚuÍ÷mùfjÑ³g¿-º¥§'ñÆñº3ÓWoNò*kÿþòùe­&®nYÇ¾v®¼Ýþ=s?[¡\SÎÜVÕú£O´ü1Ð5x |
| --- | Minor | À3 lÏÉw"jAr%g13ØRÚ6ZÐXÒF(:=c4a2Ãë¤×¶+³d2t@bdÕ+8&³ü®«ÎÀÅ«°Aà¾rî+ú'iTã ¨]áXdX ÙaB&l2Ll2Ì'~s§zïÕâlÔxI¶?Î Êrª¿¬ÓÒ_pnT ¸}#³ÝÞ³x!~oÆ¶öúÄ?ýóõë~æ½. ¼ñ·Êç. ÆÑñ=øçòå§Ç_ '÷²rTy®ý	Ø_=p&8cG²Ïôyá ]Eê¸¹V\§»Èn2ÚDÉÈ³(Á"¯öè \ì¼*uJÝê:ºà<:¥.¥++7|-Þp=Û^â{¦¥· +-- óçjÕ(«è)Ò±ÞûoRê@©4l¤Yk¨3iÙÐÊèr²È]e+E¦h£Þ$ñFgb. %XWlàv#uÄãÉòÜá!@8 QÝÿ \3u @IOÈ¹Øø?QóJý¯KÏq×jåÜAåy¥ "âUØü8ë<ö¢rçÆÔô^<?gã¹ø'Có'PÌQ  åÊ6¯ÓÌeQ£Å	È. ÎAOW §+. |
| --- | Minor | Sentence exceeds complexity threshold, split for readability. Applying the split needs --strength moderate or higher. |
| --- | Minor | none (split proposal only; source not rewritten) |
| --- | Minor | none |
| --- | Minor | Check: NEEDS-LLM |
| --- | Minor | Flags:    not-assessed |
| --- | Minor | SENTENCE (Line 713, 105 words, 1 clauses)  [Script] |
| --- | Minor | ®²dC¡ÈPfXlXeh7ð¸4Q-J){<¾q¢÷'±'ª«)jÂ<(Kvë´ev®C|F4é/`(\¹*u©¹Þ:û¸aWyQ¯NÌhQgþÎ|CÙH1x,ø§@ùìGd%x%^ËD{ µ_¿º¨üª`:_¨%Àtk(Z­þ"EmíûCÇà Ý_Tü²¢Æ¾ù¡ÇvíÜ±l?ðÎVPÈÌR¾Þ´êóÏ>ûbEk!7¶!/ºCNr° ×vCìvÁÜl­GÍBacñÛ%âÃ~åSãh:¡u>µ$W»TÍ¨æÁµ(^_ßÏíÝ |
| --- | Minor | »ÍñÞ°ÙÊ®AÏ´t~ûÍ-ÏzÏ?ºmÓ­[·lÚV]½¿|6Î½q]Î¤T÷vÕÉ·>þèÃ? |
| --- | Minor | &ÐÐ"Ñ9ÑØf7×¦hC?²lÒEi´v7ÄnSjuGÉü*DJJI©ÊÅ-G¯&çÑy|9o? |
| --- | Minor | ®²dC¡ÈPfXlXeh7ð¸4Q-J){<¾q¢÷'±'ª«)jÂ<(Kvë´ev®C|F4é/`(\¹*u©¹Þ:û¸aWyQ¯NÌhQgþÎ|CÙH1x. ø§@ùìGd%x%^ËD{ µ_¿º¨üª`:_¨%Àtk(Z­þ"EmíûCÇà Ý_Tü²¢Æ¾ù¡ÇvíÜ±l?ðÎVPÈÌR¾Þ´êóÏ>ûbEk!7¶!/ºCNr° ×vCìvÁÜl­GÍBacñÛ%âÃ~åSãh:¡u>µ$W»TÍ¨æÁµ(^_ßÏíÝ |
| --- | Minor | »ÍñÞ°ÙÊ®AÏ´t~ûÍ-ÏzÏ?ºmÓ­[·lÚV]½¿|6Î½q]Î¤T÷vÕÉ·>þèÃ? |
| --- | Minor | &ÐÐ"Ñ9ÑØf7×¦hC?²lÒEi´v7ÄnSjuGÉü*DJJI©ÊÅ-G¯&çÑy|9o?. |
| --- | Minor | Sentence exceeds complexity threshold, split for readability. Applying the split needs --strength moderate or higher. |
| --- | Minor | none (split proposal only; source not rewritten) |
| --- | Minor | none |
| --- | Minor | Check: NEEDS-LLM |
| --- | Minor | Flags:    not-assessed |
| --- | Minor | SENTENCE (Line 713, 268 words, 6 clauses)  [Script] |
| --- | Minor | ÉQIð¢ó@ *vfÏçO=Ñô£Øíþ¯^¿¢|úf.ò[×­|TlöÒ+[v ¡{ð@åÒ¡W_;ñ åøÈëÆQ¨^NÈ"6kPÛæªôÍ6Í£ÖÓA'øÐ «Éo7gAòß wÒXUÓîÒýîð§4|¡-«ji§:­jd4\!|¹afx¦ñIH@¢±ýHv8 5G§l·jômlüvè,ûãè=éÚt!Æï2ùPN[Èu¤¦« FÕYàÆÕ«]TtþðYX| 3*BRÆÊ!lVÓ~_N¶jOáþâ~«>Ãf÷\©:5«Ì²¦õ©·¤ W*»ú¤ï¹ûÓoþXYörgÛ-Û_£l ×©ÇØnàX4ªýn`ÀÎÕ"iæê#-FÅM2³Fùyßê3aýnÞüLVE0 Î¬KêRý,ÄòÎ@Ow(Ø#3velG,¹Å»w1px×©ÆÆæXIhLßß+³®íØ¿OaÛg7¯Z³·«{gÖ.zëÝÞ3ÕÕúEÛ«/(nÕ¾Lw";/;ÖÒlÛ"gD7øõ>5s#~PKñGè	H³t9Ô:à íÐÚï8Æz32ysTfÆ¨£þ×ó½_vÀ.¹úÑ£32Gü.Y¢U{A~²ÐÏä·ÕÀòiÑÒjâkNÙè°é8¡9lwhË*ÓÇù=Ø)?Ü9Ìå³û­Ãý©_?)k@Ô]=}ä/@)ºâeUrÒÓáÙºÀ# w¯*^à û1k¦©ËtfFÏëÎ;ÏG hKñ?fÄ4RAÙÄ,zfß~Ù[V×òÀ^E~2*ï(_±ÌZºìüoUv%>½AeW5ão_ªéU¯U/néB W4Z,g%a9ÜóßË¡Åù¡ýßÃ²&*Àâ×úIáVÝ7½|5`Aóÿ4ÙÚô|5ÑÄm­}ëtZ¬ÃWÒþ§Î>Cl·!¦rûÎÛ·ïÜµz:×+Ø¥|^øeW×+]]_Îë«àòkÜÏÁêCìQX]âÑÙ9ØínC³).¦Ù#n·mry4íIõ#Á |
| --- | Minor | Ï © BrJÁ>c¸éê¯LìH¤éWØú¨{õõÍb·1ÔpH÷mÛ´yëÖÍ¶=«¨iúæNêðz¯bÆU:û§?úø­jÀå)oÝ¸¡]®DÖu\ýG Çä8ÖÊadj6#Î±É m6ïÑ&I~Æ§÷³\!¾CßJ»3à2¤3êI£<6,1è]rHN)"Ó-#ËLdVæFÛeì#ìôØ=_zKP\ª ¸à |
| --- | Minor | ÉQIð¢ó@ *vfÏçO=Ñô£Øíþ¯^¿¢|úf.ò[×­|TlöÒ+[v ¡{ð@åÒ¡W_;ñ åøÈëÆQ¨^NÈ"6kPÛæªôÍ6Í£ÖÓA'øÐ «Éo7gAòß wÒXUÓîÒýîð§4|¡-«ji§:­jd4\!|¹afx¦ñIH@¢±ýHv8 5G§l·jômlüvè. ûãè=éÚt!Æï2ùPN[Èu¤¦« FÕYàÆÕ«]TtþðYX| 3*BRÆÊ!lVÓ~_N¶jOáþâ~«>Ãf÷\©:5«Ì²¦õ©·¤ W*»ú¤ï¹ûÓoþXYörgÛ-Û_£l ×©ÇØnàX4ªýn`ÀÎÕ"iæê#-FÅM2³Fùyßê3aýnÞüLVE0 Î¬KêRý. ÄòÎ@Ow(Ø#3velG. ¹Å»w1px×©ÆÆæXIhLßß+³®íØ¿OaÛg7¯Z³·«{gÖ.zëÝÞ3ÕÕúEÛ«/(nÕ¾Lw";/;ÖÒlÛ"gD7øõ>5s#~PKñGè	H³t9Ô:à íÐÚï8Æz32ysTfÆ¨£þ×ó½_vÀ.¹úÑ£32Gü.Y¢U{A~²ÐÏä·ÕÀòiÑÒjâkNÙè°é8¡9lwhË*ÓÇù=Ø)?Ü9Ìå³û­Ãý©_?)k@Ô]=}ä/@)ºâeUrÒÓáÙºÀ# w¯*^à û1k¦©ËtfFÏëÎ;ÏG hKñ?fÄ4RAÙÄ. zfß~Ù[V×òÀ^E~2*ï(_±ÌZºìüoUv%>½AeW5ão_ªéU¯U/néB W4Z. g%a9ÜóßË¡Åù¡ýßÃ²&*Àâ×úIáVÝ7½|5`Aóÿ4ÙÚô|5ÑÄm­}ëtZ¬ÃWÒþ§Î>Cl·!¦rûÎÛ·ïÜµz:×+Ø¥|^øeW×+]]_Îë«àòkÜÏÁêCìQX]âÑÙ9ØínC³).¦Ù#n·mry4íIõ#Á |
| --- | Minor | Ï © BrJÁ>c¸éê¯LìH¤éWØú¨{õõÍb·1ÔpH÷mÛ´yëÖÍ¶=«¨iúæNêðz¯bÆU:û§?úø­jÀå)oÝ¸¡]®DÖu\ýG Çä8ÖÊadj6#Î±É m6ïÑ&I~Æ§÷³\!¾CßJ»3à2¤3êI£<6. 1è]rHN)"Ó-#ËLdVæFÛeì#ìôØ=_zKP\ª ¸à. |
| --- | Minor | Sentence exceeds complexity threshold, split for readability. Applying the split needs --strength moderate or higher. |
| --- | Minor | none (split proposal only; source not rewritten) |
| --- | Minor | none |
| --- | Minor | Check: NEEDS-LLM |
| --- | Minor | Flags:    not-assessed |
| --- | Minor | SENTENCE (Line 723, 499 words, 7 clauses)  [Script] |
| --- | Minor | î@¾¯äB57eâº­ïô£Ò2è@sú<6E¹~Çã}b^WcgväÀ1½/PópzQ »^<örm>Çö½n[éEº=ºÀ¤ñÙtóÓ«ôéú÷Ó¾ìÂ£f³|±>ÏëóÅ%º}¡ 	IL×JW«Ý%Z!¬0>ûÅOI9=õÔ+¸DÙ?°pÜHf£fËÖöÉñ<A9RÓ[ºvÒÙ[×lþÝs.ØXHÖR9Îiæõ³ZöhËXäwÂýxÑ/ùônÍÒ ´+tÌ{5@í½êdûNÈÝêÎÝÈÞùáÌMIv«ì¦`!IööüUÒks<óõ¼òxöS5Ùg«nõõª>^]wöWÓûØéG¿/#¼6{%`aDGå<QËhÚ |
| --- | Minor | ÐÎFxhú/gá0F¤×pÔ=ÈhÐjÅHkÒ1¦çUóæñõ­£©Ðñ3 ¢«©èãà<Â4aÐ(FÉFrv­]LD©l*ªMSQ455Þf Jc#ÛÈ-ãkkË |
| --- | Minor | ª^¬hCo(MMøÊÓÚqÛ2¥	øWÓÈ|PSÓ3rÎp¶áNùn]»ÕfÛµ¢ |
| --- | Minor | :Þk)¶,avzx×°F#XlV½A/KÁ l1Ñ |
| --- | Minor | <aM,Ú£ÓØ¬É ×@úO0g´UBxzP²8ÿ)]Ô¼~=@§2¥S<(vnköÉÖl<LÌ³ÆÄñÖ»Ä{­å¸J¬²6 K­D¬aà08 åEA'êyUµ¢Vb |
| --- | Minor | ´;5FÒZD.Bï°ZmI(§hÄx]ªjN´&Ù ¡x83gsÃùáÂÍPm8T?Ø0Ø2Äg+DcðÍ-ý¯Êxý8Ã8iyeµÐv'*ÂEL)b¸"¾H(Òi§Óu³,3­ÓlE¹é1å¤-ãÊø2¡LS¦+ëæ[çÚÊKÑrÜÄ´V¶kâfÛ¤mëuKõFc£i´Ì¼ÌÒ`]fÛ ]/r,þk±5Äy*!!°br	K_?hT:w+7o·)o,Ã<Û- 	§THdÏ§ªl¤úV<¿Ò°yYbLí6»Í aGÉ(p4Å%áQ{$àQÝaw¹ÈÃ>Ùn«q;¨¶D=VhÍb¤Ë®õ z«µ8£¤vÏzAFzþ |
| --- | Minor | ¡RazÖAÍ=ïRíD\á8ñcF;4bÇ¢ñ Jw	ÅÆYöùh¾Pi¬´7ì«ÑF£MÄZFK´ÞÄ¹87éÆnÆM\:Þm°\.ÛR°ñD]¢>Ùà3&¤$s+ÅíÌc3yd8Æã±ÆBÓØÈ\Ìb4ÜeaéééY«j²@¨ÔUê+ |
| --- | Minor | ¦ùËÑ ¼YAVðMeÆSÔ`n°-·7:ººF®AëMºMúõõÆµ¦µ¶5ö5®5î5wÓ´Ñ¶ªW×aÀLÿcÞ½Y¹'mTìk?ÿbR»'*¯=?XÉ¬ÇÙ55Ê2%·º(§á¾PÚFÈ©mÂD.Æí6#£7j7:Ñ¶MF |
| --- | Minor | hj ´Ì`gÉhÆäFÃ¾ß ¥VBÇî±ü8±©¨HcÒC( 'Ñ ¯!ð§³tU 	Rg-ÿBB!ÁHES*ÆUx9f]JáRx0¡:Ñ,§13¸"n_ÄOf3u¸¡JX.4¢ex9s?¹màø&írýrCq©i©Ôhnt7F6F%¹ÜÛí¬êxú]üj¡²ä6«ë 4×eÎÜËçåçúÅ!òë>üÝôwK¦·G¦5|*d®9¨Qö¤HLOàÏô%èB-ÝJ°Ûg¤åü:!kP¿Séb~×­óÙíÖ³	XÓ`·$;Û<¦ú¬ÍºHÿlRhÁóÝü3ÔýhnpÌ`¿yñ¾C	r¸W	@=<rÍÈ2fjÑüéÓ¯÷(9ûK¼¥U<|«ªZO]8P"µÊ(!5kPÛ[ïäIlvköØôôÜeÉêL>i]v¿YðE:³âCqQàb'D4êV¨PfyóFÖJ		u	{Ø[r¼j/âá Ç¾>dÃùá9y/inÙ½y&½QSè/?½ëH1Çã3¶ì.hpc^öÆ/ÝÇqiDÀq(Ú$'fúÓ}ôxëÏñ%ù,ÏÿË;Ã5È¢ë	!®çÜÎõìAC.Ä÷yaÿ#ÎÉ; 6@³Ê¢øCø'd! |
| --- | Minor | î@¾¯äB57eâº­ïô£Ò2è@sú<6E¹~Çã}b^WcgväÀ1½/PópzQ »^<örm>Çö½n[éEº=ºÀ¤ñÙtóÓ«ôéú÷Ó¾ìÂ£f³|±>ÏëóÅ%º}¡ 	IL×JW«Ý%Z!¬0>ûÅOI9=õÔ+¸DÙ?°pÜHf£fËÖöÉñ<A9RÓ[ºvÒÙ[×lþÝs.ØXHÖR9Îiæõ³ZöhËXäwÂýxÑ/ùônÍÒ ´+tÌ{5@í½êdûNÈÝêÎÝÈÞùáÌMIv«ì¦`!IööüUÒks<óõ¼òxöS5Ùg«nõõª>^]wöWÓûØéG¿/#¼6{%`aDGå<QËhÚ |
| --- | Minor | ÐÎFxhú/gá0F¤×pÔ=ÈhÐjÅHkÒ1¦çUóæñõ­£©Ðñ3 ¢«©èãà<Â4aÐ(FÉFrv­]LD©l*ªMSQ455Þf Jc#ÛÈ-ãkkË |
| --- | Minor | ª^¬hCo(MMøÊÓÚqÛ2¥	øWÓÈ|PSÓ3rÎp¶áNùn]»ÕfÛµ¢ |
| --- | Minor | :Þk)¶. avzx×°F#XlV½A/KÁ l1Ñ |
| --- | Minor | <aM. Ú£ÓØ¬É ×@úO0g´UBxzP²8ÿ)]Ô¼~=@§2¥S<(vnköÉÖl<LÌ³ÆÄñÖ»Ä{­å¸J¬²6 K­D¬aà08 åEA'êyUµ¢Vb |
| --- | Minor | ´;5FÒZD.Bï°ZmI(§hÄx]ªjN´&Ù ¡x83gsÃùáÂÍPm8T?Ø0Ø2Äg+DcðÍ-ý¯Êxý8Ã8iyeµÐv'*ÂEL)b¸"¾H(Òi§Óu³. 3­ÓlE¹é1å¤-ãÊø2¡LS¦+ëæ[çÚÊKÑrÜÄ´V¶kâfÛ¤mëuKõFc£i´Ì¼ÌÒ`]fÛ ]/r. þk±5Äy*!!°br	K_?hT:w+7o·)o. Ã<Û- 	§THdÏ§ªl¤úV<¿Ò°yYbLí6»Í aGÉ(p4Å%áQ{$àQÝaw¹ÈÃ>Ùn«q;¨¶D=VhÍb¤Ë®õ z«µ8£¤vÏzAFzþ |
| --- | Minor | ¡RazÖAÍ=ïRíD\á8ñcF;4bÇ¢ñ Jw	ÅÆYöùh¾Pi¬´7ì«ÑF£MÄZFK´ÞÄ¹87éÆnÆM\:Þm°\.ÛR°ñD]¢>Ùà3&¤$s+ÅíÌc3yd8Æã±ÆBÓØÈ\Ìb4ÜeaéééY«j²@¨ÔUê+ |
| --- | Minor | ¦ùËÑ ¼YAVðMeÆSÔ`n°-·7:ººF®AëMºMúõõÆµ¦µ¶5ö5®5î5wÓ´Ñ¶ªW×aÀLÿcÞ½Y¹'mTìk?ÿbR»'*¯=?XÉ¬ÇÙ55Ê2%·º(§á¾PÚFÈ©mÂD.Æí6#£7j7:Ñ¶MF |
| --- | Minor | hj ´Ì`gÉhÆäFÃ¾ß ¥VBÇî±ü8±©¨HcÒC( 'Ñ ¯!ð§³tU 	Rg-ÿBB!ÁHES*ÆUx9f]JáRx0¡:Ñ. §13¸"n_ÄOf3u¸¡JX.4¢ex9s?¹màø&írýrCq©i©Ôhnt7F6F%¹ÜÛí¬êxú]üj¡²ä6«ë 4×eÎÜËçåçúÅ!òë>üÝôwK¦·G¦5|*d®9¨Qö¤HLOàÏô%èB-ÝJ°Ûg¤åü:!kP¿Séb~×­óÙíÖ³	XÓ`·$;Û<¦ú¬ÍºHÿlRhÁóÝü3ÔýhnpÌ`¿yñ¾C	r¸W	@=<rÍÈ2fjÑüéÓ¯÷(9ûK¼¥U<|«ªZO]8P"µÊ(!5kPÛ[ïäIlvköØôôÜeÉêL>i]v¿YðE:³âCqQàb'D4êV¨PfyóFÖJ		u	{Ø[r¼j/âá Ç¾>dÃùá9y/inÙ½y&½QSè/?½ëH1Çã3¶ì.hpc^öÆ/ÝÇqiDÀq(Ú$'fúÓ}ôxëÏñ%ù. ÏÿË;Ã5È¢ë	!®çÜÎõìAC.Ä÷yaÿ#ÎÉ; 6@³Ê¢øCø'd!. |
| --- | Minor | Sentence exceeds complexity threshold, split for readability. Applying the split needs --strength moderate or higher. |
| --- | Minor | none (split proposal only; source not rewritten) |
| --- | Minor | none |
| --- | Minor | Check: NEEDS-LLM |
| --- | Minor | Flags:    not-assessed |
| --- | Minor | SENTENCE (Line 723, 250 words, 1 clauses)  [Script] |
| --- | Minor | õ^èw: bÒUbüJäøA¥Îûß'[ø{3¦xwÍ·WmÊÿ |
| --- | Minor | }ùÛûô=¿}¯wôýîºßW0NX¨D#È¿}¯g±ôÞ¾ó³ô«:ý(¡F%ð|s¢µPn@Ùe8õ´Àäk¹7×øX´Ûêùr´¤ z®Jzlìh>Ûæs±ð<æ3×ÑZç|hÓ&; |
| --- | Minor | ·*ÌPrê0O. ý¹ìêà |
| --- | Minor | }äeB.ZçüL4AGåææÏÆ¢uèaà.ÉOÈßØ!ìöMöïÜ[|<ÿÿ© ;ï45´ÚE8C|IçÓýFªßlVS¤é4Uê4ß¦³Ñ¢4´KýRB»é×¨¬ÿÚôs-ÐïXúÜ	õ9Z§iÆp~môn¸Núõ³ýêÔÿ®óÈ®£Q¨~îCU[Ô<(ÍÌÒ(®l¨Í	0 |
| --- | Minor | ûP"?ôG >j#P-\4õæ\KÔV<+`L#ÜËRD£¡V |
| --- | Minor | bÀÎY¨¨Óù=0Ë"¸/¹0oÀy`|¬;G}÷ýy¦©«T\¨:Tý´g	ôÕ©s`õl°ôýÇÝú¾æ |
| --- | Minor | ¯~ãùÃ_åýf~Áú~×	Q[$Ø®TKL4åÂ ']&¡"t'Ðb«B*a»Ñ=A§0.ª*~f#tY%ü¦BÎXÉ	Üåä |
| --- | Minor | íL ¿0Ó¯û¸Óåäu9UJN¶ã:rLG^}ÅÆ½ ¯ØÈÑ yY!GòB^TÈ 9Ô1;tt%ò|+yN!ÏÉÏè¹ÛÈ=ùYü´<CöÈÓOsO+ä©ròä#÷d"Ù»\äö&öä	ü8ìYÃíQÈ¸EÇ%²{ÛHvÜ.#Ù%³;aàNÙ¹Ýa bÛêZ¹¶cdË:nlÙÍPÛ<lÚxÛ¤J¹ÇÈÆUìõÜR²Af×Ã¾Ö'ukÍÜº²îhðd×ÉjXzu9y8<ä î èÈªòrnBVÖJÜJ¹¿ÕÈÝ ­F²¢ÅÄ­°iÞAÌd¹H5z¸e7HãÒ(®ÑCFÔC(ä>Ô/6põ Yl e¶®,ZXÀ-ª! |
| --- | Minor | õ^èw: bÒUbüJäøA¥Îûß'[ø{3¦xwÍ·WmÊÿ |
| --- | Minor | }ùÛûô=¿}¯wôýîºßW0NX¨D#È¿}¯g±ôÞ¾ó³ô«:ý(¡F%ð|s¢µPn@Ùe8õ´Àäk¹7×øX´Ûêùr´¤ z®Jzlìh>Ûæs±ð<æ3×ÑZç|hÓ&; |
| --- | Minor | ·*ÌPrê0O. ý¹ìêà |
| --- | Minor | }äeB.ZçüL4AGåææÏÆ¢uèaà.ÉOÈßØ!ìöMöïÜ[|<ÿÿ© ;ï45´ÚE8C|IçÓýFªßlVS¤é4Uê4ß¦³Ñ¢4´KýRB»é×¨¬ÿÚôs-ÐïXúÜ	õ9Z§iÆp~môn¸Núõ³ýêÔÿ®óÈ®£Q¨~îCU[Ô<(ÍÌÒ(®l¨Í	0 |
| --- | Minor | ûP"?ôG >j#P-\4õæ\KÔV<+`L#ÜËRD£¡V |
| --- | Minor | bÀÎY¨¨Óù=0Ë"¸/¹0oÀy`|¬;G}÷ýy¦©«T\¨:Tý´g	ôÕ©s`õl°ôýÇÝú¾æ |
| --- | Minor | ¯~ãùÃ_åýf~Áú~×	Q[$Ø®TKL4åÂ ']&¡"t'Ðb«B*a»Ñ=A§0.ª*~f#tY%ü¦BÎXÉ	Üåä |
| --- | Minor | íL ¿0Ó¯û¸Óåäu9UJN¶ã:rLG^}ÅÆ½ ¯ØÈÑ yY!GòB^TÈ 9Ô1;tt%ò|+yN!ÏÉÏè¹ÛÈ=ùYü´<CöÈÓOsO+ä©ròä#÷d"Ù»\äö&öä	ü8ìYÃíQÈ¸EÇ%²{ÛHvÜ.#Ù%³;aàNÙ¹Ýa bÛêZ¹¶cdË:nlÙÍPÛ<lÚxÛ¤J¹ÇÈÆUìõÜR²Af×Ã¾Ö'ukÍÜº²îhðd×ÉjXzu9y8<ä î èÈªòrnBVÖJÜJ¹¿ÕÈÝ ­F²¢ÅÄ­°iÞAÌd¹H5z¸e7HãÒ(®ÑCFÔC(ä>Ô/6põ Yl e¶®. ZXÀ-ª!. |
| --- | Minor | Sentence exceeds complexity threshold, split for readability. Applying the split needs --strength moderate or higher. |
| --- | Minor | none (split proposal only; source not rewritten) |
| --- | Minor | none |
| --- | Minor | Check: NEEDS-LLM |
| --- | Minor | Flags:    not-assessed |
| --- | Minor | SENTENCE (Line 723, 360 words, 10 clauses)  [Script] |
| --- | Minor | Hm«Hí*¶FOjd¶¬¾Aª*qU ©\PÊU#«Øó¹¥dÌÎO hIVf5dfØ¹ÌyÍ¹;ÉXÅ¦kË¹ôÄfãüI f#i2 [O-')ÉY\ÊKÎ">xø4$"¸ÄRoá¦xo!ñ2§!^Oç-%X3ç Sl,,k&±«ØÄÈlt<2ÈâveqîiÄ³º²HB°¨S!Øm6Î^ClV+g³ÌZ­ÄpcÄä5+D4`ÿ¦Äï 1ÀbY½BtÐÐÉk0b+Ñ`æ46"	Ï8¾p0&cÓ	LÊO#H!ø(._½§ýûCÿ¯7ð/üõv endstream endobj 275 0 obj <</Length 91/Filter/FlateDecode>> stream x¥×  ,g={ïÝÿÿBø¢à,ÉÂÂÇQ^?*Pç!ÛY"ûrpÿÓ{øÂàôá-¿ö$¢úº7´tôâF&fV6ö2 endstream endobj 276 0 obj <</Length 377/Filter/FlateDecode>> stream x]Ën0E÷|é""<b	!Ué&>Ô´«*bR1È!ü}ï@¤"Áè;ã10÷mG¸^iMk£ksÄ.­TV¬ÂSwõÅ¾øx¿ÔlÓGe)âOo^Gw«gÓé)BÄïÎkíE¬¾÷G ãm~©#;MTUÂPã{­·º#âõÁx¿ïk_öÈøº$Ò lI÷®C­ÉÕöBQ¹ñW%ÊÆ_UDÖüó²s³ä§S>Ââ)`LÜEY wÉLCæ3À±d\ àKç	ðCÂÍ 3v3Æh+Æ»Ü±»c¬5c |
| --- | Minor | -¿ÅCWâ%oOò¾ ·%>Ü"`WR!sÀ÷VüWXJBhf3äªÍ=z*ôTè©ÐSsáiy(¦±f|I}sÎc8a§	l--geè©jºÿ ÌÑÜ endstream endobj 280 0 obj <</Length1 3560/Length 2307/Filter/FlateDecode>> stream xÍUypUÕÿîýóÞËËö¶@Ix¼%ïð&$M0X¢	yYÈBI,>#¬ÚH Û¸Ì´ |
| --- | Minor | >»Øh¬ |
| --- | Minor | ÔÖ¡3Ep¦u` Óê8N-3Üô»÷vZÿ¬ç{Î÷ûÎ·ï,"rq'È[^Zv'¹#%¥ãÊ+Uv/ÝÈ¸±·¼re	½t¥qqÑ]Å+ÆÜá?À¸ñeyþ÷%©¯ªk« |
| --- | Minor | büãªºî.ï¾À±/°mn5¶ý½çóü/<¿»±¶3DV&Mã[77Ùô,ã.Æêkq½ÙAd©b<».olñ~ÆMm]«ÈÀ¿bìim¯«åÑÐÇð×V») ÍyoÝæVÞØQßBÓ[k»ÖÓô¶Ú®&þ |
| --- | Minor | »[¶çéTAEqdý«!TåeqNg¢J?¶ÝÀJÓ(¿¾µ)	ì·ûÛõè¾¨®1ÞäÇøøü¾1¸î¯]ÛÇ|ÑMÓ©¼JûÍs/&(ûIò²aztÄYjP]ìÁb´HU5+¦I¯¢¡,HÚ5åbñèå°µMùÛM¯FÃèÇûlF,b¤ïQ<&Æ×c^bÔ:º÷©7kÌF?:ù,Ò»Lï1·i=AýÌ_¢­¦ü°Ä¥¡û |
| --- | Minor | *ÓXO5HÉc?*½Á~<wõ÷ÓZsþ*Nt§ÕIEs¦E? |
| --- | Minor | Hm«Hí*¶FOjd¶¬¾Aª*qU ©\PÊU#«Øó¹¥dÌÎO hIVf5dfØ¹ÌyÍ¹;ÉXÅ¦kË¹ôÄfãüI f#i2 [O-')ÉY\ÊKÎ">xø4$"¸ÄRoá¦xo!ñ2§!^Oç-%X3ç Sl. k&±«ØÄÈlt<2ÈâveqîiÄ³º²HB°¨S!Øm6Î^ClV+g³ÌZ­ÄpcÄä5+D4`ÿ¦Äï 1ÀbY½BtÐÐÉk0b+Ñ`æ46"	Ï8¾p0&cÓ	LÊO#H!ø(._½§ýûCÿ¯7ð/üõv endstream endobj 275 0 obj <</Length 91/Filter/FlateDecode>> stream x¥×  . g={ïÝÿÿBø¢à. ÉÂÂÇQ^?*Pç!ÛY"ûrpÿÓ{øÂàôá-¿ö$¢úº7´tôâF&fV6ö2 endstream endobj 276 0 obj <</Length 377/Filter/FlateDecode>> stream x]Ën0E÷|é""<b	!Ué&>Ô´«*bR1È!ü}ï@¤"Áè;ã10÷mG¸^iMk£ksÄ.­TV¬ÂSwõÅ¾øx¿ÔlÓGe)âOo^Gw«gÓé)BÄïÎkíE¬¾÷G ãm~©#;MTUÂPã{­·º#âõÁx¿ïk_öÈøº$Ò lI÷®C­ÉÕöBQ¹ñW%ÊÆ_UDÖüó²s³ä§S>Ââ)`LÜEY wÉLCæ3À±d\ àKç	ðCÂÍ 3v3Æh+Æ»Ü±»c¬5c |
| --- | Minor | -¿ÅCWâ%oOò¾ ·%>Ü"`WR!sÀ÷VüWXJBhf3äªÍ=z*ôTè©ÐSsáiy(¦±f|I}sÎc8a§	l--geè©jºÿ ÌÑÜ endstream endobj 280 0 obj <</Length1 3560/Length 2307/Filter/FlateDecode>> stream xÍUypUÕÿîýóÞËËö¶@Ix¼%ïð&$M0X¢	yYÈBI. >#¬ÚH Û¸Ì´ |
| --- | Minor | >»Øh¬ |
| --- | Minor | ÔÖ¡3Ep¦u` Óê8N-3Üô»÷vZÿ¬ç{Î÷ûÎ·ï. "rq'È[^Zv'¹#%¥ãÊ+Uv/ÝÈ¸±·¼re	½t¥qqÑ]Å+ÆÜá?À¸ñeyþ÷%©¯ªk« |
| --- | Minor | büãªºî.ï¾À±/°mn5¶ý½çóü/<¿»±¶3DV&Mã[77Ùô. ã.Æêkq½ÙAd©b<».olñ~ÆMm]«ÈÀ¿bìim¯«åÑÐÇð×V») ÍyoÝæVÞØQßBÓ[k»ÖÓô¶Ú®&þ |
| --- | Minor | »[¶çéTAEqdý«!TåeqNg¢J?¶ÝÀJÓ(¿¾µ)	ì·ûÛõè¾¨®1ÞäÇøøü¾1¸î¯]ÛÇ|ÑMÓ©¼JûÍs/&(ûIò²aztÄYjP]ìÁb´HU5+¦I¯¢¡. HÚ5åbñèå°µMùÛM¯FÃèÇûlF. b¤ïQ<&Æ×c^bÔ:º÷©7kÌF?:ù. Ò»Lï1·i=AýÌ_¢­¦ü°Ä¥¡û |
| --- | Minor | *ÓXO5HÉc?*½Á~<wõ÷ÓZsþ*Nt§ÕIEs¦E?. |
| --- | Minor | Sentence exceeds complexity threshold, split for readability. Applying the split needs --strength moderate or higher. |
| --- | Minor | none (split proposal only; source not rewritten) |
| --- | Minor | none |
| --- | Minor | Check: NEEDS-LLM |
| --- | Minor | Flags:    not-assessed |
| --- | Minor | SENTENCE (Line 723, 549 words, 8 clauses)  [Script] |
| --- | Minor | âv!p:úVïÒ<z^&¾±´Î2°÷Åô:}¨<F/*g(L{¨Ó,abçÓÔÌ´V1é3ZcF6dÍòÅÃy¯³÷£re²5hPªxª2À÷º¶S³¨aÊ2©Ô\_t |
| --- | Minor | ã®N«kÔi"Kà8FÓìæq¾ |
| --- | Minor | éBþT#|Lý0*"OÐbëbKb±iÏnE@9lI£ c{¸e{ènå,G!½bªBÙ^GDõ- F´{ª¼ï¬ý |
| --- | Minor | ªÄoöTTruD¦Fà³E/ãÂ¼½¤¢ÊùCYé¨×²RUV1k ³¼¬4Ìâç3e¦Å|®³¸¢S(¬Í´¦R²c¦}6s%À¾eí¨'NÉ¡øyîlkbVl6Å¤ ­¨ú-esô&­Ðy[áj%+WÉbIS&;IÎcFA `ÖìÜxw?¶líÛ«¾}üúÇ/_ÿüøõO"È'î}eµ´(«Vîí~µ ¹Ë¿:nô-5§Þ01zßÔÕ}jæm Vîub¯&ö0·g.Ü= §ô&Ã;,&q°INLêév¤k"-©	)ùrB%RØkJ>uç ãus ÉãI-ð¸ÝÒãGn7\¬çËëÔáàÁQDÎ?±	< #Ä'#^q:bÄj-°³= lV§´y`uÂ"ýÒd;é`g"ìTµC©éPàö=Êïl£ÿwÿ³ñßôß$¸¸´ endstream endobj 282 0 obj <</Length 10/Filter/FlateDecode>> stream xc`    endstream endobj 283 0 obj <</Length 229/Filter/FlateDecode>> stream x]PÁjÃ0½û+tlÅmA0öÃº±l§±cËÁ°ØFqùûÉN×±	d!¿÷Ää¹½´Ág/Mp3ÄáÖ|ëêkFdq·LÇ6¸(ä+S¦66ö¸  É"ù0ÀæýÜ­_ÝÒ2ìR`Ññ¸'®zDU¼k-ã>/;ý2Þp¬ýaµd¢Å)i¤Ã¢Ùs(hì?ü¦êÝ_úZ>¸Nê³hXeLÙùîÑÌDl¯¦ú*|ÀûíRLEUòòt endstream endobj 288 0 obj <</Type/XObject/Subtype/Form/FormType 1/BBox[0 0 245.27952 195.76628931]/Matrix[1 0 0 1 0 0]/Resources<</Font 262 0 R/XObject 284 0 R/ExtGState 285 0 R/Pattern 286 0 R/Shading 287 0 R/ProcSet[/PDF/Text/ImageB/ImageC/ImageI]>>/Filter/FlateDecode/Length 2312>> stream xÚÝZËn¹¿¢Öb(Vñ½íÄFl<áE`Ë/HÎØ'¿¯Ë!o«»ØÍ{}%Íè^Ùî#²º¬Ãb5Ïþrñë×?>}4<~¡Îæ§×_ |
| --- | Minor | |hxwÊàéJ±ócö§KñDÙë§Ø´ïz«ÎBÈWÌzªeí|Ðä#W©V'[ä\c£ì´åQØ8·Áê>XÊ9L |
| --- | Minor | ]b¦MÊaør1üsø4Íaüí£*ÆÁï¦´SÎy¼Ãfrð<½«²Ïß^ÝduNÙg¡m6·ì¶3Ö¨5Í¾eYCFæ Ô%NB°áRjBÂ=©g8T9D,¤{©òÐÄ=U|Ðà¿Êll¨Fl&hë½µ$³m9Ì¾Â 	ßEaÍû3ÔuãÿSÀo¢#ÁEÑïÃ®ªHTÀÇÈRfëDÛüð¹Îeä7Èø(ó{Â(E	Éä6í%|dFv 9f½&ãl¶2Çf°1HÒÅ1ºæ |
| --- | Minor | ±å1hÃ3¸ >É¡¶tóddM¶Ôe¦»I»r6Ìe ÉÉ¸æ73Åó®ªC7W* pÞ:/±úÌtdF®ékÖ@µb» [êsÓÙáØéH[c%× °%¡-ätl®ù&£ |
| --- | Minor | [¶Á¶ÓÚáBB©D&æÔÐ588klKN |
| --- | Minor | ~CÓ5kZUª,Î9}Q¿ e&mG»Fªå\©Ð¹LIn*3Ö¬OÉN¿Ñ²ýìPNá!Qç¦Á6?·ðÓ±ºæBDQ»ìShw[C·Ô±ºæBDAc,9,h["ÚBPGfhs@Dìtvâ\ÑÚ Àôéåp&­¹&eÖ\{L°]ôiä`u8 Ä`qà±d@6Ç¤Y@÷tö7ý×¢ËÇÂYÃ·Ò- 8¶yïÀ¸NÊ»Õ#EÃ7õáIÎjäAÖ9UPàûµÃë+õè\=¡!çokùüR/'W§À$Ï!&Ì|pòï +#üq|pò	pÌ |
| --- | Minor | [G©å¨O;CÞ¹ëAûº8U¯Ôù3õ×sõ|aæ$ªIÖéh¡c.¾ØeÒëúR6Es_á?U\Jsð¥d]X&WU-¾,G _×o4ÛSã«rÖª·=£ÛW¬!x3ÿ!â*Gökç¥¿ÖpHß¯´¢Úwtz»l! |
| --- | Minor | âv!p:úVïÒ<z^&¾±´Î2°÷Åô:}¨<F/*g(L{¨Ó. abçÓÔÌ´V1é3ZcF6dÍòÅÃy¯³÷£re²5hPªxª2À÷º¶S³¨aÊ2©Ô\_t |
| --- | Minor | ã®N«kÔi"Kà8FÓìæq¾ |
| --- | Minor | éBþT#|Lý0*"OÐbëbKb±iÏnE@9lI£ c{¸e{ènå. G!½bªBÙ^GDõ- F´{ª¼ï¬ý |
| --- | Minor | ªÄoöTTruD¦Fà³E/ãÂ¼½¤¢ÊùCYé¨×²RUV1k ³¼¬4Ìâç3e¦Å|®³¸¢S(¬Í´¦R²c¦}6s%À¾eí¨'NÉ¡øyîlkbVl6Å¤ ­¨ú-esô&­Ðy[áj%+WÉbIS&;IÎcFA `ÖìÜxw?¶líÛ«¾}üúÇ/_ÿüøõO"È'î}eµ´(«Vîí~µ ¹Ë¿:nô-5§Þ01zßÔÕ}jæm Vîub¯&ö0·g.Ü= §ô&Ã;. &q°INLêév¤k"-©	)ùrB%RØkJ>uç ãus ÉãI-ð¸ÝÒãGn7\¬çËëÔáàÁQDÎ?±	< #Ä'#^q:bÄj-°³= lV§´y`uÂ"ýÒd;é`g"ìTµC©éPàö=Êïl£ÿwÿ³ñßôß$¸¸´ endstream endobj 282 0 obj <</Length 10/Filter/FlateDecode>> stream xc`    endstream endobj 283 0 obj <</Length 229/Filter/FlateDecode>> stream x]PÁjÃ0½û+tlÅmA0öÃº±l§±cËÁ°ØFqùûÉN×±	d!¿÷Ää¹½´Ág/Mp3ÄáÖ|ëêkFdq·LÇ6¸(ä+S¦66ö¸  É"ù0ÀæýÜ­_ÝÒ2ìR`Ññ¸'®zDU¼k-ã>/;ý2Þp¬ýaµd¢Å)i¤Ã¢Ùs(hì?ü¦êÝ_úZ>¸Nê³hXeLÙùîÑÌDl¯¦ú*|ÀûíRLEUòòt endstream endobj 288 0 obj <</Type/XObject/Subtype/Form/FormType 1/BBox[0 0 245.27952 195.76628931]/Matrix[1 0 0 1 0 0]/Resources<</Font 262 0 R/XObject 284 0 R/ExtGState 285 0 R/Pattern 286 0 R/Shading 287 0 R/ProcSet[/PDF/Text/ImageB/ImageC/ImageI]>>/Filter/FlateDecode/Length 2312>> stream xÚÝZËn¹¿¢Öb(Vñ½íÄFl<áE`Ë/HÎØ'¿¯Ë!o«»ØÍ{}%Íè^Ùî#²º¬Ãb5Ïþrñë×?>}4<~¡Îæ§×_ |
| --- | Minor | |hxwÊàéJ±ócö§KñDÙë§Ø´ïz«ÎBÈWÌzªeí|Ðä#W©V'[ä\c£ì´åQØ8·Áê>XÊ9L |
| --- | Minor | ]b¦MÊaør1üsø4Íaüí£*ÆÁï¦´SÎy¼Ãfrð<½«²Ïß^ÝduNÙg¡m6·ì¶3Ö¨5Í¾eYCFæ Ô%NB°áRjBÂ=©g8T9D. ¤{©òÐÄ=U|Ðà¿Êll¨Fl&hë½µ$³m9Ì¾Â 	ßEaÍû3ÔuãÿSÀo¢#ÁEÑïÃ®ªHTÀÇÈRfëDÛüð¹Îeä7Èø(ó{Â(E	Éä6í%|dFv 9f½&ãl¶2Çf°1HÒÅ1ºæ |
| --- | Minor | ±å1hÃ3¸ >É¡¶tóddM¶Ôe¦»I»r6Ìe ÉÉ¸æ73Åó®ªC7W* pÞ:/±úÌtdF®ékÖ@µb» [êsÓÙáØéH[c%× °%¡-ätl®ù&£ |
| --- | Minor | [¶Á¶ÓÚáBB©D&æÔÐ588klKN |
| --- | Minor | ~CÓ5kZUª. Î9}Q¿ e&mG»Fªå\©Ð¹LIn*3Ö¬OÉN¿Ñ²ýìPNá!Qç¦Á6?·ðÓ±ºæBDQ»ìShw[C·Ô±ºæBDAc. 9. h["ÚBPGfhs@Dìtvâ\ÑÚ Àôéåp&­¹&eÖ\{L°]ôiä`u8 Ä`qà±d@6Ç¤Y@÷tö7ý×¢ËÇÂYÃ·Ò- 8¶yïÀ¸NÊ»Õ#EÃ7õáIÎjäAÖ9UPàûµÃë+õè\=¡!çokùüR/'W§À$Ï!&Ì|pòï +#üq|pò	pÌ |
| --- | Minor | [G©å¨O;CÞ¹ëAûº8U¯Ôù3õ×sõ|aæ$ªIÖéh¡c.¾ØeÒëúR6Es_á?U\Jsð¥d]X&WU-¾. G _×o4ÛSã«rÖª·=£ÛW¬!x3ÿ!â*Gökç¥¿ÖpHß¯´¢Úwtz»l!. |
| --- | Minor | Sentence exceeds complexity threshold, split for readability. Applying the split needs --strength moderate or higher. |
| --- | Minor | none (split proposal only; source not rewritten) |
| --- | Minor | none |
| --- | Minor | Check: NEEDS-LLM |
| --- | Minor | Flags:    not-assessed |
| --- | Minor | SENTENCE (Line 723, 485 words, 5 clauses)  [Script] |
| --- | Minor | 6ÜvÏglG` |
| --- | Minor | õ¨¢´[ènïþ´1hN¹ßN MU |
| --- | Minor | *2¨s2{ßîLÜØX£1Òþñyßs×rA®ßµgÁ<Ç¼[:o-çÓ> uDÿ²§¬&}vÅ¥¾úªzSñÙF_<uö7{ð§ÿçeÐ°'ëàRnw_î ÕdMðî´ý·8òÕ ëÏØ*¸}´tóÉ4a|¥Ó!¢fóÓrYfòï³?oIG6Q³GEïLñÆ>ù²ûÎÞ÷fcnUãVuÛÙC[ê"uCxMqCÔ~ ßëëµzñýªk-+©iwVV=vn[I6ßáV³Êy]lP¿£­ñ7saBm=qëÄ½aG6¶¸2fÊ§|£;ºçÊzèÌÖ@3éKßÈ­¸7[Y[ÜI¶Z |
| --- | Minor | ÂýéèÏÒÁ'ñßÆ3|36âF6²¶ù/¬èÉðýèÏrõSJ±õçßÌ¸Ñ¬mþôXÄ¡TXX¤éþLôçÜiü)»37ñg#nôg#k?×&ÅÀPñìð'Ýt+ú\®aÃTÞT:6U²E¹V7µÀÃ¯x'ÿª+«_WKµ¨¨¸K¨"¦¢h;þKÅ}iéZggüKÅË§/Ç$Æßô½ÿqOíø¡âã,Çÿ¹âé{ÃÞ8PZ¸îø&-(Jk.®­ilsí¦Fz_RuAùû\uß2Wê:.kj¼¬ÿ²Æ¾ý o{SÓg/!'Ùåõ+mß:í÷ö1cîIµTÌÛxi6'$J eÿø~#Ê:à@Úv·Kß8hÔónÙ ¾gí@ã pÛ^~)-`e¸Æ¶¯{ÏÚåR´ò[qiç:Í6 <j¿!·<]öì #GçèÑ» |
| --- | Minor | ÉÕ¶û´½ïfý²]R§¿Ï·ë­âºÿ,n+z¥%2R)  |
| --- | Minor | ) ²@+4O ñÎq³óØ÷ÄFçwùyn»½(¥ÏB¸ËMëÚè}ïGM·¬7þØóþpûÂS#"wé¨	º£ÆWlóSuÔãz~',ql+8úÛæü|´d\íoôÜ©ó~¨p0ÞsNsÏÂ%æ9ÅëB©¦ËÍàj¶~¶Å)ÙF¼È¹ì%M¡ÚóÉ"T{ÞRQ RlÄ9yËºÜ]ö |
| --- | Minor | )±i¹·YÙ¥7]¼fgÈÖÁø°ñs'?7ÿ¤ç?ÕF)NÙETwØénY	D$xÓGìXÕÚÜ¾«ºCì{Þó3ý"Ò{^²rê"ÎS8ß&1ç8ïÈo53S)\|ú°8Ûó6ùèúé{~:^®õ	êÄÛ§æ*<»¿61Ùý­UÕv{È¡|ã9W-xÙsÖé·J»70 ÿ¨sÄ:Ép	ÈÏÕÿ«n; endstream endobj 296 0 obj <</Filter/FlateDecode/Length 3194>> stream xÚí[Iod¹ |
| --- | Minor | %@¿(jKÜ>ÉÈm ß29tÙ]s$ùÿPµ«\5ÓrH7 ¶ßÓBR\>ªÓ¿Oò qôÏ Ãïoôúx!P!ÏôýT!´céwçGe-Í/éM©,ýoÓ¨2Âh÷oè©Æô{Xóhu~þÇËßNy9ð 2¯ù÷GOäK¥N d`» Ä»6þô CØ0àû~Óÿyúþ'ÙÈ^8Åc³A»C""HD:gÌRb^µOA`ÏEBì[j`¯Ùð;:ZGû§*Ö°fñÄôÑ4J	ë~ÍàÓ§	Ç®# U¡:P¸JëEî,¤Ññà3êÖ¼.uàÃfYØð)òò· <QQÐ4ÎÑÁIuhô-S&cØT¾aÑXýTÇ'1!ÖºÃku;ïòüXäGÞø5BzÃOq9>yølq£Ks i³s6»lH¬A&ÂZlF0O>éJÁQW" |
| --- | Minor | ¢¨'-{èúc£üÔôRj|ì´ÚÄj%©N9ª1DÒh®}ký¯Ã»DZ³y&_Æ«Oª¤Õçý¶¢6õí¸} \c;eä÷OÊ] y¢±ìºÝhtwzçíT¢ñv*Ì¥5ÎìÓôe0§ª(84ø8hDÍGÞ¨êSÒzu<­¬&¯m*(ÖÏ!ò<;wRNâ£ÞëÂ¬dXbW[¢ð¨Ûghbßs ò0èCµÍ£þð°^LB	%ó(ý°ÖÎn­ît¢!ËÂ!¤lPAbM E $ãóÞ¯¼·=é[!i|uEzKzí\tÝ~rO)¹0tu|læ#ÅbcÕ ¶Ô»ØG! |
| --- | Minor | 6ÜvÏglG` |
| --- | Minor | õ¨¢´[ènïþ´1hN¹ßN MU |
| --- | Minor | *2¨s2{ßîLÜØX£1Òþñyßs×rA®ßµgÁ<Ç¼[:o-çÓ> uDÿ²§¬&}vÅ¥¾úªzSñÙF_<uö7{ð§ÿçeÐ°'ëàRnw_î ÕdMðî´ý·8òÕ ëÏØ*¸}´tóÉ4a|¥Ó!¢fóÓrYfòï³?oIG6Q³GEïLñÆ>ù²ûÎÞ÷fcnUãVuÛÙC[ê"uCxMqCÔ~ ßëëµzñýªk-+©iwVV=vn[I6ßáV³Êy]lP¿£­ñ7saBm=qëÄ½aG6¶¸2fÊ§|£;ºçÊzèÌÖ@3éKßÈ­¸7[Y[ÜI¶Z |
| --- | Minor | ÂýéèÏÒÁ'ñßÆ3|36âF6²¶ù/¬èÉðýèÏrõSJ±õçßÌ¸Ñ¬mþôXÄ¡TXX¤éþLôçÜiü)»37ñg#nôg#k?×&ÅÀPñìð'Ýt+ú\®aÃTÞT:6U²E¹V7µÀÃ¯x'ÿª+«_WKµ¨¨¸K¨"¦¢h;þKÅ}iéZggüKÅË§/Ç$Æßô½ÿqOíø¡âã. Çÿ¹âé{ÃÞ8PZ¸îø&-(Jk.®­ilsí¦Fz_RuAùû\uß2Wê:.kj¼¬ÿ²Æ¾ý o{SÓg/!'Ùåõ+mß:í÷ö1cîIµTÌÛxi6'$J eÿø~#Ê:à@Úv·Kß8hÔónÙ ¾gí@ã pÛ^~)-`e¸Æ¶¯{ÏÚåR´ò[qiç:Í6 <j¿!·<]öì #GçèÑ» |
| --- | Minor | ÉÕ¶û´½ïfý²]R§¿Ï·ë­âºÿ. n+z¥%2R)  |
| --- | Minor | ) ²@+4O ñÎq³óØ÷ÄFçwùyn»½(¥ÏB¸ËMëÚè}ïGM·¬7þØóþpûÂS#"wé¨	º£ÆWlóSuÔãz~'. ql+8úÛæü|´d\íoôÜ©ó~¨p0ÞsNsÏÂ%æ9ÅëB©¦ËÍàj¶~¶Å)ÙF¼È¹ì%M¡ÚóÉ"T{ÞRQ RlÄ9yËºÜ]ö |
| --- | Minor | )±i¹·YÙ¥7]¼fgÈÖÁø°ñs'?7ÿ¤ç?ÕF)NÙETwØénY	D$xÓGìXÕÚÜ¾«ºCì{Þó3ý"Ò{^²rê"ÎS8ß&1ç8ïÈo53S)\|ú°8Ûó6ùèúé{~:^®õ	êÄÛ§æ*<»¿61Ùý­UÕv{È¡|ã9W-xÙsÖé·J»70 ÿ¨sÄ:Ép	ÈÏÕÿ«n; endstream endobj 296 0 obj <</Filter/FlateDecode/Length 3194>> stream xÚí[Iod¹ |
| --- | Minor | %@¿(jKÜ>ÉÈm ß29tÙ]s$ùÿPµ«\5ÓrH7 ¶ßÓBR\>ªÓ¿Oò qôÏ Ãïoôúx!P!ÏôýT!´céwçGe-Í/éM©. ýoÓ¨2Âh÷oè©Æô{Xóhu~þÇËßNy9ð 2¯ù÷GOäK¥N d`» Ä»6þô CØ0àû~Óÿyúþ'ÙÈ^8Åc³A»C""HD:gÌRb^µOA`ÏEBì[j`¯Ùð;:ZGû§*Ö°fñÄôÑ4J	ë~ÍàÓ§	Ç®# U¡:P¸JëEî. ¤Ññà3êÖ¼.uàÃfYØð)òò· <QQÐ4ÎÑÁIuhô-S&cØT¾aÑXýTÇ'1!ÖºÃku;ïòüXäGÞø5BzÃOq9>yølq£Ks i³s6»lH¬A&ÂZlF0O>éJÁQW" |
| --- | Minor | ¢¨'-{èúc£üÔôRj|ì´ÚÄj%©N9ª1DÒh®}ký¯Ã»DZ³y&_Æ«Oª¤Õçý¶¢6õí¸} \c;eä÷OÊ] y¢±ìºÝhtwzçíT¢ñv*Ì¥5ÎìÓôe0§ª(84ø8hDÍGÞ¨êSÒzu<­¬&¯m*(ÖÏ!ò<;wRNâ£ÞëÂ¬dXbW[¢ð¨Ûghbßs ò0èCµÍ£þð°^LB	%ó(ý°ÖÎn­ît¢!ËÂ!¤lPAbM E $ãóÞ¯¼·=é[!i|uEzKzí\tÝ~rO)¹0tu|læ#ÅbcÕ ¶Ô»ØG!. |
| --- | Minor | Sentence exceeds complexity threshold, split for readability. Applying the split needs --strength moderate or higher. |
| --- | Minor | none (split proposal only; source not rewritten) |
| --- | Minor | none |
| --- | Minor | Check: NEEDS-LLM |
| --- | Minor | Flags:    not-assessed |
| --- | Minor | SENTENCE (Line 723, 194 words, 1 clauses)  [Script] |
| --- | Minor | 6àtã31ûFÆ:aÿçP,ÄM5Í¯n?ÉÁE`iÓrdig1àë³|ê@ÕZJ<EÍ"Ðp/èl@J1*QÆÏ@uòd÷Ð` |
| --- | Minor | u<UcÌÒÞÂåÊÙ° oÔF3¥!ÍSÕt	ý¸¨£äÕ¤¤¤j&ÉòØûÐ³õv É);Y@^LÁ¦4:[sÁ:¢®iá*OF<Ä)k(% ðgÒ¸§¿Î©	BÍóóµQ«PÅ #ÏWV¥åùÕûHgÒ¬s­R¨J°&Èo¨UDÇíZõ¨_ãèWdÕÞY½(ií­ÐÕ%tMAçÙå· ÕÍYø­ä4m:<äDSrÛjOZ#`FÖÙ­¿Ë|ùHôè5õai{>¼vgG1¢¨*g¡æ©ÐàG"¨Qô¥ãÐö AÊå~¿Þ»9¸>%EF |
| --- | Minor | 2s!ÛåÚF;×J±x?Ø?0±ÐçõH s²º®WíiXÏè°DoiÃ°5áøT=º2sQÆü=9H~Õüë[dü+óÂö­ar¥)%ØÅPÃ¡fîFogÔ<{H¥%§¾å1nT¬_4v<øPÂbc¦ò«Cx§«e¦(½±cr>ÊùøÙ¯¹à6¹âà%¨)h!ýµ8ýªõ(ëO*Åâr]¥)¦®Ð®6× Âu¸-ÍøÒ¸ÂRËôMé%°Ê¤ ó9£îÓbW2Ô«[fhUMã-àu- |
| --- | Minor | ;uÁ]»ÃJáL©\I%ZïÝ<38qØtðwUTÄaWåt¡ÅuoòüWç}xH[Ý¾0cÁq«â+cê(Êy\ Ýª+Óäu\_Ub7/ñ3´]VB§9gvî÷/êp¥íò¿XlÞÐÌål{. |
| --- | Minor | 6àtã31ûFÆ:aÿçP. ÄM5Í¯n?ÉÁE`iÓrdig1àë³|ê@ÕZJ<EÍ"Ðp/èl@J1*QÆÏ@uòd÷Ð` |
| --- | Minor | u<UcÌÒÞÂåÊÙ° oÔF3¥!ÍSÕt	ý¸¨£äÕ¤¤¤j&ÉòØûÐ³õv É);Y@^LÁ¦4:[sÁ:¢®iá*OF<Ä)k(% ðgÒ¸§¿Î©	BÍóóµQ«PÅ #ÏWV¥åùÕûHgÒ¬s­R¨J°&Èo¨UDÇíZõ¨_ãèWdÕÞY½(ií­ÐÕ%tMAçÙå· ÕÍYø­ä4m:<äDSrÛjOZ#`FÖÙ­¿Ë|ùHôè5õai{>¼vgG1¢¨*g¡æ©ÐàG"¨Qô¥ãÐö AÊå~¿Þ»9¸>%EF |
| --- | Minor | 2s!ÛåÚF;×J±x?Ø?0±ÐçõH s²º®WíiXÏè°DoiÃ°5áøT=º2sQÆü=9H~Õüë[dü+óÂö­ar¥)%ØÅPÃ¡fîFogÔ<{H¥%§¾å1nT¬_4v<øPÂbc¦ò«Cx§«e¦(½±cr>ÊùøÙ¯¹à6¹âà%¨)h!ýµ8ýªõ(ëO*Åâr]¥)¦®Ð®6× Âu¸-ÍøÒ¸ÂRËôMé%°Ê¤ ó9£îÓbW2Ô«[fhUMã-àu- |
| --- | Minor | ;uÁ]»ÃJáL©\I%ZïÝ<38qØtðwUTÄaWåt¡ÅuoòüWç}xH[Ý¾0cÁq«â+cê(Êy\ Ýª+Óäu\_Ub7/ñ3´]VB§9gvî÷/êp¥íò¿XlÞÐÌål{.. |
| --- | Minor | Sentence exceeds complexity threshold, split for readability. Applying the split needs --strength moderate or higher. |
| --- | Minor | none (split proposal only; source not rewritten) |
| --- | Minor | none |
| --- | Minor | Check: NEEDS-LLM |
| --- | Minor | Flags:    not-assessed |
| --- | Minor | SENTENCE (Line 723, 118 words, 4 clauses)  [Script] |
| --- | Minor | â/Ý	n¶£4#Ö²Xx½ú¶+6º1¨{ÆÙÛJCÖ¸Xv«1æúR@Ç¦(N6ÅLÄs9×ó¹1Täò:= |
| --- | Minor | |j]ùîê¾Áµ®ËH5jª:Ps´ÚjâBÉd¯jÀ.¥7Õê¡RCÎmñi_Cm»\·×Ñ{ÓNë±üëÈêk/Öu®"RE	r%ØÜ^Ñ½¿¶ZGFJ2<-Üá¥#Fn*hR2à7rØçËwVX¥ $ |
| --- | Minor | ®ò×gRêòÎÅÌóè	J}¡©fÝbËo¸ZÀÕU:dÎ!#ÆKÝÀ,×NîÿzG­+eGÁUJA×.«76¹ÿØÎj¼RÞLl{:TdÙhS¿.í# bOá&×`uÝ/,ÔOË2	¿©µ(D3Ë*7zo-dÖyü­Î¬,éÝeø{,ÿnÒ¿{ÄûJ97å"Ü¬e§h> éº.}®ókü®&f?ßÑáHÍæ{PísXäïV¥ÿ+Ý)ü/+]éRycµ¼Zo´#dpH 7læJÊ§ÏÛÚ#ñWàù±º)G«ºä>k{ØñyÌ;´Rö©×R´AîmézH|²¨01Ó]0Ãn! |
| --- | Minor | â/Ý	n¶£4#Ö²Xx½ú¶+6º1¨{ÆÙÛJCÖ¸Xv«1æúR@Ç¦(N6ÅLÄs9×ó¹1Täò:= |
| --- | Minor | |j]ùîê¾Áµ®ËH5jª:Ps´ÚjâBÉd¯jÀ.¥7Õê¡RCÎmñi_Cm»\·×Ñ{ÓNë±üëÈêk/Öu®"RE	r%ØÜ^Ñ½¿¶ZGFJ2<-Üá¥#Fn*hR2à7rØçËwVX¥ $ |
| --- | Minor | ®ò×gRêòÎÅÌóè	J}¡©fÝbËo¸ZÀÕU:dÎ!#ÆKÝÀ. ×NîÿzG­+eGÁUJA×.«76¹ÿØÎj¼RÞLl{:TdÙhS¿.í# bOá&×`uÝ/. ÔOË2	¿©µ(D3Ë*7zo-dÖyü­Î¬. éÝeø{. ÿnÒ¿{ÄûJ97å"Ü¬e§h> éº.}®ókü®&f?ßÑáHÍæ{PísXäïV¥ÿ+Ý)ü/+]éRycµ¼Zo´#dpH 7læJÊ§ÏÛÚ#ñWàù±º)G«ºä>k{ØñyÌ;´Rö©×R´AîmézH|²¨01Ó]0Ãn!. |
| --- | Minor | Sentence exceeds complexity threshold, split for readability. Applying the split needs --strength moderate or higher. |
| --- | Minor | none (split proposal only; source not rewritten) |
| --- | Minor | none |
| --- | Minor | Check: NEEDS-LLM |
| --- | Minor | Flags:    not-assessed |
| --- | Minor | SENTENCE (Line 723, 74 words, 0 clauses)  [Script] |
| --- | Minor | ·¶á"óvªL*ÀÆ'JÊ¯½û¸%Ò	­]äônRûxK`Ùçì­z° §+4z{o/´u3:´Zm	b¼åJFçK}Öñ À¶Ï5!l±6¾Å»iZÉhEéT®á´dv%¼¾[l |
| --- | Minor | |éßk¯ÏB 3\£ùd¶M¾pÔ¨UÝ%q¾-Ø+ÚÌfÓ§ïÜ®(.ýAø¢t¯v-GË¿!øRÞçÐÉTn3}îÐ`-÷¯ý®BôùN½üÄ2jÍ½¯íT^[4Ö)½&îLiõ7`¼AvÃI#Ñ¥[±ë¤aôxM&´B¾LÐ É«Õ¢y²2Hþë±Ç÷ùn. |
| --- | Minor | ·¶á"óvªL*ÀÆ'JÊ¯½û¸%Ò	­]äônRûxK`Ùçì­z° §+4z{o/´u3:´Zm	b¼åJFçK}Öñ À¶Ï5!l±6¾Å»iZÉhEéT®á´dv%¼¾[l |
| --- | Minor | |éßk¯ÏB 3\£ùd¶M¾pÔ¨UÝ%q¾-Ø+ÚÌfÓ§ïÜ®(.ýAø¢t¯v-GË¿!øRÞçÐÉTn3}îÐ`-÷¯ý®BôùN½üÄ2jÍ½¯íT^[4Ö)½&îLiõ7`¼AvÃI#Ñ¥[±ë¤aôxM&´B¾LÐ É«Õ¢y²2Hþë±Ç÷ùn. |
| --- | Minor | Sentence exceeds complexity threshold, split for readability. Applying the split needs --strength moderate or higher. |
| --- | Minor | none (split proposal only; source not rewritten) |
| --- | Minor | none |
| --- | Minor | Check: NEEDS-LLM |
| --- | Minor | Flags:    not-assessed |
| --- | Minor | SENTENCE (Line 723, 366 words, 11 clauses)  [Script] |
| --- | Minor | þWóÿK¡k*ZóµºN |
| --- | Minor | |Iï#È´×ÉT]®_·ýºÇê¸Û«QÝw,¥öu¢WÓoÎÖÒ´]Å÷Ñn endstream endobj 303 0 obj <</Length1 3212/Length 2088/Filter/FlateDecode>> stream xÍU{PT×ÿîý³»ìÅ"® |
| --- | Minor | Ùõ-."bÅXL%,y+Z³<ßo¤)3I1mI;MQªVÓvfÚf¬mÉtúI:£-~÷²I4Óôßö~sÎù~ßû|ç]RÈÍ Wi°d1¹#%¥J+VT{ma<±·´òâã/Mb¼ñ¬ùþÖ)o1>ÀxM][m'MQÞaüWÆUu=ÝÞÃ©,;ÑÐÙØöIï§×ð;Öïo¬íê$;uc[·7Üm[ùwÆM×5Õ×¢Î^ke|ÝÌ×Äçgö?0þãô¦¶îmñc´Hzk­uµ¼æ16ëm«ÝÖ)êÔOëfýíµmõÓsçíe\Ãõ¼ÞÙÑÕ=¾öYQNçæúÎ-Ûmÿ`Ã6ÏÙXø©<+Oä J%%¸xÙj2{F4>þ¥­©÷Ó~rÝöÍ­Þ¸¹¾Ò[k»Û)ýk?1Y9Bsäi¥¤ëx	nSÀ]´Ù !cTÉñåWÑPbI9Û4CSÎØÛ¿<bÈH±*#*d¤XXÙ;Ádâr«"Ç/F¼'öòÐÎÊ#C(êâÑM¦[FÍ´vS?óÓK~UDÄ¥iû |
| --- | Minor | )Yl§¤äsF8Nu³}ã~Ú`é`Ô¢3U· æ*,~Â|!0:1,¯´.ÑÉËQêc»Ut©£/¥Ëô¡ò2WnQRÕþ©CÞâZi¼eÑ=Zge6eÍòMãLÍ¼ÏËýü\ÉRV¡ |
| --- | Minor | ïPU°¥»¨YÔ0eX´ö7±UÝÁù#û¥Qu%2Îcæåø´ëmàJðPÍúñ7êÙùdyÚÚb=L«Y»åm*ÕP«9Âr¤åÊmÎB½gªB9^× ê+ |
| --- | Minor | +«¼¿Y;=7çkÐë²{©bÐ¹Ý;4>^Q%¦Èµ2e¾¨AáK»ûMÊ»¹9åUÞÁß#QKj,«¬bÖD,fyI0¬âç;Å·mü#"[5÷;(mvÀ6{º= |
| --- | Minor | µD+ût»W¹?¨&´«KTî%¾=  |
| --- | Minor | cï÷hÍZZÆnª3y4«7ÆÞl¶n¥ºöt×Õ¢{ëã?§iQÖeýýÎ¸?}±Þ/çÌºcUD_Ýf{1ÈùÑý²¶93)DG^¤æÉáxìgÁñ;éó¬ÜR¦l:eî\¤[¿h1,ø]°Ó³æþE4ó#Ö;4yû0áU~eð 'èÏ^<ÄKJR¢"¼Ò/-¢ê¤í´6R#5Q7¿äLª£,^ýTÀ`n[xù |
| --- | Minor | }ÍTOµÔF9,-£v¶Ïc®Z¼üb¾Õe¡z^ëÙ§ç[:(È\3GXC[Ø¢mk9J£eéeÞïå(í<w²Í»í¼ìßÁyk-Ý×ãTZY6r¯Ë8wmÄçl¼X­±ä]ÌwXYý\gf>âýoî#¾æ |
| --- | Minor | ¥ñÏyìäSúO´îÊÏR{õ;¿6ð¾7®§Ë!ÜÐÅõtüÊkW3äµ®fàJ5~ÆåÇàÒEM^òã¢!?~aà=?7ð3?5ðî`©|÷Kñ?ãGÞÃXyAÃ@,~èÇÛ!¼ó~¼q.$ß0p.³}qò¬ýÛ²ßãu¾×ö¤Ê×¼zÆ%_3.>'OûpíNÅá.N²ãI |
| --- | Minor | '{E_útñ=N¼R O8~Ì#ûpì¨SóàØ¢ëÑâè<êÄÑ! |
| --- | Minor | þWóÿK¡k*ZóµºN |
| --- | Minor | |Iï#È´×ÉT]®_·ýºÇê¸Û«QÝw. ¥öu¢WÓoÎÖÒ´]Å÷Ñn endstream endobj 303 0 obj <</Length1 3212/Length 2088/Filter/FlateDecode>> stream xÍU{PT×ÿîý³»ìÅ"® |
| --- | Minor | Ùõ-."bÅXL%. y+Z³<ßo¤)3I1mI;MQªVÓvfÚf¬mÉtúI:£-~÷²I4Óôßö~sÎù~ßû|ç]RÈÍ Wi°d1¹#%¥J+VT{ma<±·´òâã/Mb¼ñ¬ùþÖ)o1>ÀxM][m'MQÞaüWÆUu=ÝÞÃ©. ;ÑÐÙØöIï§×ð;Öïo¬íê$;uc[·7Üm[ùwÆM×5Õ×¢Î^ke|ÝÌ×Äçgö?0þãô¦¶îmñc´Hzk­uµ¼æ16ëm«ÝÖ)êÔOëfýíµmõÓsçíe\Ãõ¼ÞÙÑÕ=¾öYQNçæúÎ-Ûmÿ`Ã6ÏÙXø©<+Oä J%%¸xÙj2{F4>þ¥­©÷Ó~rÝöÍ­Þ¸¹¾Ò[k»Û)ýk?1Y9Bsäi¥¤ëx	nSÀ]´Ù !cTÉñåWÑPbI9Û4CSÎØÛ¿<bÈH±*#*d¤XXÙ;Ádâr«"Ç/F¼'öòÐÎÊ#C(êâÑM¦[FÍ´vS?óÓK~UDÄ¥iû |
| --- | Minor | )Yl§¤äsF8Nu³}ã~Ú`é`Ô¢3U· æ*. ~Â|!0:1. ¯´.ÑÉËQêc»Ut©£/¥Ëô¡ò2WnQRÕþ©CÞâZi¼eÑ=Zge6eÍòMãLÍ¼ÏËýü\ÉRV¡ |
| --- | Minor | ïPU°¥»¨YÔ0eX´ö7±UÝÁù#û¥Qu%2Îcæåø´ëmàJðPÍúñ7êÙùdyÚÚb=L«Y»åm*ÕP«9Âr¤åÊmÎB½gªB9^× ê+ |
| --- | Minor | +«¼¿Y;=7çkÐë²{©bÐ¹Ý;4>^Q%¦Èµ2e¾¨AáK»ûMÊ»¹9åUÞÁß#QKj. «¬bÖD. fyI0¬âç;Å·mü#"[5÷;(mvÀ6{º= |
| --- | Minor | µD+ût»W¹?¨&´«KTî%¾=  |
| --- | Minor | cï÷hÍZZÆnª3y4«7ÆÞl¶n¥ºöt×Õ¢{ëã?§iQÖeýýÎ¸?}±Þ/çÌºcUD_Ýf{1ÈùÑý²¶93)DG^¤æÉáxìgÁñ;éó¬ÜR¦l:eî\¤[¿h1. ø]°Ó³æþE4ó#Ö;4yû0áU~eð 'èÏ^<ÄKJR¢"¼Ò/-¢ê¤í´6R#5Q7¿äLª£. ^ýTÀ`n[xù |
| --- | Minor | }ÍTOµÔF9. -£v¶Ïc®Z¼üb¾Õe¡z^ëÙ§ç[:(È\3GXC[Ø¢mk9J£eéeÞïå(í<w²Í»í¼ìßÁyk-Ý×ãTZY6r¯Ë8wmÄçl¼X­±ä]ÌwXYý\gf>âýoî#¾æ |
| --- | Minor | ¥ñÏyìäSúO´îÊÏR{õ;¿6ð¾7®§Ë!ÜÐÅõtüÊkW3äµ®fàJ5~ÆåÇàÒEM^òã¢!?~aà=?7ð3?5ðî`©|÷Kñ?ãGÞÃXyAÃ@. ~èÇÛ!¼ó~¼q.$ß0p.³}qò¬ýÛ²ßãu¾×ö¤Ê×¼zÆ%_3.>'OûpíNÅá.N²ãI |
| --- | Minor | '{E_útñ=N¼R O8~Ì#ûpì¨SóàØ¢ëÑâè<êÄÑ!. |
| --- | Minor | Sentence exceeds complexity threshold, split for readability. Applying the split needs --strength moderate or higher. |
| --- | Minor | none (split proposal only; source not rewritten) |
| --- | Minor | none |
| --- | Minor | Check: NEEDS-LLM |
| --- | Minor | Flags:    not-assessed |
| --- | Minor | SENTENCE (Line 723, 299 words, 3 clauses)  [Script] |
| --- | Minor | ô2qÄ#WÄá°<<C/ÆÈCnÒÅAæÎÃýÃòýûªåþaìïûöúä¾jìÓÅ^®k¯{v»åTì¿¢ÝnìâÔ»Bx¥ /OÂK}x1½¡ì5ðB«K¾á8¹Ópß/÷`G<¾Ûínls`kWn}-)²Ç-)èf§îTtØl`S§Sn2ÐéD§.:Âho[(Û[Ð¶­-±²ÕÖ^Ñ]4sÊæØØ4,7hj¬MÃhê |
| --- | Minor | F]4øPÏFõ ¡.Ô¨Y'k¬ÏÃsª |
| --- | Minor | ¬+ÇwÂxÖÀÚ ª|ÛÀa<c 2UVúQ±"^V±"Ëôb,ÁÒÊe}XâG)\²ÔÅ	(Q² YD~^¢ÌOBþêyÈë¹Ñ!ÛlMæ#7­![OréOY ³Ée OÌÏ qÒÇLr!QÓdb4Gj4]x<H`»a¸¹½n.^\ÅçúãûÇº8NàLS±bÄèsZà`GÑ!DÙÝ2JÝ |
| --- | Minor | ôK[ý¤\pPÕ¥d@RB»*Ùÿ·ý¯ø¯ÿÿïÃÙ endstream endobj 305 0 obj <</Length 13/Filter/FlateDecode>> stream xc`    endstream endobj 306 0 obj <</Length 227/Filter/FlateDecode>> stream x]=kÄ0wÿ ×áðÝÑ1ÊuÉÐv*[F63äßWv®)T`Yï#^K_»ÇBýÊÑöÁrs\Ø"8Rç¸`ó­ª·LRZà~3Nù¨ô4çÌ+\ðN~ahÃÇµßú%¥o2TÛC/ãLz6®ð±sÒy= ö§x_Â¥ÖçÍçd,²¡Ush¡ñ­Brÿú7jð»ü~ù>·üU¸_EQþ»û³³X«K©@¸ï-ÅT¨r~ Êsæ endstream endobj 310 0 obj <</Length1 15192/Length 10188/Filter/FlateDecode>> stream xÍ{y|TÕýè9÷Üeö¹³e2ef²MI2L!ð²UD@J¢ 	d "2uà¥ÈÃ élÚ8EgÝÎºu+:·hî4ô¡4$ÊçFCÆL	¿ãGßÉ£òéïôÉð;s©´¯ëy°VZ©(]8ß0ÚGýÚOÛ<ìÂ¢ |
| --- | Minor | R("ÌÍV4Ð6æyÒônÌÚ |
| --- | Minor |  ;Ón4úneçè£¯Ñ4£CÂ§ 0÷?¶^ý}\jßõ/¸1àÂXwÙòsi}½=`Æóôçßh3àc~lvÎõWÿ0ªN4Z*{64 t:OMíUÌOT7ÂóTh!õæ®Ït}ÿú< uâ-°:â2¸ÝÐÖä<ZÀ:'Ï1LK®iÆ! |
| --- | Minor | ô2qÄ#WÄá°<<C/ÆÈCnÒÅAæÎÃýÃòýûªåþaìïûöúä¾jìÓÅ^®k¯{v»åTì¿¢ÝnìâÔ»Bx¥ /OÂK}x1½¡ì5ðB«K¾á8¹Ópß/÷`G<¾Ûínls`kWn}-)²Ç-)èf§îTtØl`S§Sn2ÐéD§.:Âho[(Û[Ð¶­-±²ÕÖ^Ñ]4sÊæØØ4. 7hj¬MÃhê |
| --- | Minor | F]4øPÏFõ ¡.Ô¨Y'k¬ÏÃsª |
| --- | Minor | ¬+ÇwÂxÖÀÚ ª|ÛÀa<c 2UVúQ±"^V±"Ëôb. ÁÒÊe}XâG)\²ÔÅ	(Q² YD~^¢ÌOBþêyÈë¹Ñ!ÛlMæ#7­![OréOY ³Ée OÌÏ qÒÇLr!QÓdb4Gj4]x<H`»a¸¹½n.^\ÅçúãûÇº8NàLS±bÄèsZà`GÑ!DÙÝ2JÝ |
| --- | Minor | ôK[ý¤\pPÕ¥d@RB»*Ùÿ·ý¯ø¯ÿÿïÃÙ endstream endobj 305 0 obj <</Length 13/Filter/FlateDecode>> stream xc`    endstream endobj 306 0 obj <</Length 227/Filter/FlateDecode>> stream x]=kÄ0wÿ ×áðÝÑ1ÊuÉÐv*[F63äßWv®)T`Yï#^K_»ÇBýÊÑöÁrs\Ø"8Rç¸`ó­ª·LRZà~3Nù¨ô4çÌ+\ðN~ahÃÇµßú%¥o2TÛC/ãLz6®ð±sÒy= ö§x_Â¥ÖçÍçd. ²¡Ush¡ñ­Brÿú7jð»ü~ù>·üU¸_EQþ»û³³X«K©@¸ï-ÅT¨r~ Êsæ endstream endobj 310 0 obj <</Length1 15192/Length 10188/Filter/FlateDecode>> stream xÍ{y|TÕýè9÷Üeö¹³e2ef²MI2L!ð²UD@J¢ 	d "2uà¥ÈÃ élÚ8EgÝÎºu+:·hî4ô¡4$ÊçFCÆL	¿ãGßÉ£òéïôÉð;s©´¯ëy°VZ©(]8ß0ÚGýÚOÛ<ìÂ¢ |
| --- | Minor | R("ÌÍV4Ð6æyÒônÌÚ |
| --- | Minor |  ;Ón4úneçè£¯Ñ4£CÂ§ 0÷?¶^ý}\jßõ/¸1àÂXwÙòsi}½=`Æóôçßh3àc~lvÎõWÿ0ªN4Z*{64 t:OMíUÌOT7ÂóTh!õæ®Ït}ÿú< uâ-°:â2¸ÝÐÖä<ZÀ:'Ï1LK®iÆ!. |
| --- | Minor | Sentence exceeds complexity threshold, split for readability. Applying the split needs --strength moderate or higher. |
| --- | Minor | none (split proposal only; source not rewritten) |
| --- | Minor | none |
| --- | Minor | Check: NEEDS-LLM |
| --- | Minor | Flags:    not-assessed |
| --- | Minor | SENTENCE (Line 835, 349 words, 3 clauses)  [Script] |
| --- | Minor | ÕPfB¡zL­øB(Ô3 Ý» Ä àë¡P9L²J-¬A5 íèm¸ßÖTªÑ:Ô í/P½2~UÑF.ptîû¨'Á<êïL¥AÇaxöÌ_ ýV°ôù5ò®rï!ï2ËC¦AkòF+j'ÃY¼,Ê[o£è´¶¹wªéè<Ü£aõIèºB{ñhjD5`Fa |
| --- | Minor | Üó¸û{t²3+ã>à­°SàyVßÇIx:) ö¼íÇ	I4gÙxZÙÆ®^ýaÏÚµ{äSð<áæÉ |
| --- | Minor | ^¹¡júVXy²r¤ÀvW´&±ñ\G «aKæ³Id¼a´ÚºgÝº=¯^OÍ+Ãà{p~ lÞ"Ù+7ËÉ^X5gò]|,â¹w`±sïø-'A2bjaæ©¾ømÔ |
| --- | Minor | ~pèa=¨¦N<×Ó1¹ÍrçìÃ  #æää |
| --- | Minor | É\u¡N¼Ü|Æa¢ÏüYdÂlV>6&áÔì¬©S³²§:uhÖÔÛ)×õ]d@>µ ³±ëøbs©®0ð6«7jÃaÝËÙÎË]b·?>@±Q¨L"ÊÐ_fãî]»vÓòü6ýpò÷¹xgâirü¬üÜ6ïÂq%Þ%È[åGäÀò r Ð R º]òè¬È¨GK"g1Wª_n²êuv¤Áv^eÐØ¬/wë:ô2eggÄÝWºånÎöKÚ\M®6WkÍµq ±¦8#ÀÚ¬ Ø	0dâ8spBlùªò%°Aþ}¸N^ÇT.í_ß±ú±Ùj¬ÉÎùëéå³vxÖ.ï];vüøðÎý)¼ÍÀ×7àMQG»,KÌÅöb1i	*N(&¥ÆÂw´:*6IbyÞÉë¬dfR ò® gùÞÓ%¾Aèi§ÐR¢±ÍÊzb¼¦h §àÌ``bß\zþÞ¯ìon[þJ¾ºô³ÅUçß}ðHÛÀ[Ö­{T_Åíð¥½úu/ºçyï³@Ù²ýà¶l}ä¡«ïù¼ |
| --- | Minor | x0'¶HñLZ£ÆEúv¬Ñ¡ r5RÂ¨XôÄ¨U1fñò¹ 7Ð¾³'ç\NW  ÅwPR¤p-vâ¡x"fy&IÔajÆ34B*À&u?©(yLÌÛ2CôÎþ¾w	³ù |
| --- | Minor | _#Î/e¾Ç/"{4åòÇ_Ï¿jÁk¸ÐsR<á£V8yq±ØZFz9§+tGM4²óêhÆÈ¸A/AÈ:(£BÚ©ðHî4±Ü¦I1º[AT!Ì0ÃKð¡¢3n:)eY#gäQetÆc¤1Ê­3"#v!xØtÌSM*ÈfE7"&ï9xã¬¿ãpù>´ð£êjõSÛßÿÛü |
| --- | Minor | ³¸öÊ3ãâäË_+ÿró?¼vú¬4é¦¶iÐdbâÑ|)Føb#*¶¹*¢kc#Jm	nMtáÍ6¯æÂµ	@®Ö ¤¶ûC _WëÔz+r"/ &EgÑÑ(&S.I?Õ5Õ=Õc.ïÛf |
| --- | Minor | ÕPfB¡zL­øB(Ô3 Ý» Ä àë¡P9L²J-¬A5 íèm¸ßÖTªÑ:Ô í/P½2~UÑF.ptîû¨'Á<êïL¥AÇaxöÌ_ ýV°ôù5ò®rï!ï2ËC¦AkòF+j'ÃY¼. Ê[o£è´¶¹wªéè<Ü£aõIèºB{ñhjD5`Fa |
| --- | Minor | Üó¸û{t²3+ã>à­°SàyVßÇIx:) ö¼íÇ	I4gÙxZÙÆ®^ýaÏÚµ{äSð<áæÉ |
| --- | Minor | ^¹¡júVXy²r¤ÀvW´&±ñ\G «aKæ³Id¼a´ÚºgÝº=¯^OÍ+Ãà{p~ lÞ"Ù+7ËÉ^X5gò]|. â¹w`±sïø-'A2bjaæ©¾ømÔ |
| --- | Minor | ~pèa=¨¦N<×Ó1¹ÍrçìÃ  #æää |
| --- | Minor | É\u¡N¼Ü|Æa¢ÏüYdÂlV>6&áÔì¬©S³²§:uhÖÔÛ)×õ]d@>µ ³±ëøbs©®0ð6«7jÃaÝËÙÎË]b·?>@±Q¨L"ÊÐ_fãî]»vÓòü6ýpò÷¹xgâirü¬üÜ6ïÂq%Þ%È[åGäÀò r Ð R º]òè¬È¨GK"g1Wª_n²êuv¤Áv^eÐØ¬/wë:ô2eggÄÝWºånÎöKÚ\M®6WkÍµq ±¦8#ÀÚ¬ Ø	0dâ8spBlùªò%°Aþ}¸N^ÇT.í_ß±ú±Ùj¬ÉÎùëéå³vxÖ.ï];vüøðÎý)¼ÍÀ×7àMQG». KÌÅöb1i	*N(&¥ÆÂw´:*6IbyÞÉë¬dfR ò® gùÞÓ%¾Aèi§ÐR¢±ÍÊzb¼¦h §àÌ``bß\zþÞ¯ìon[þJ¾ºô³ÅUçß}ðHÛÀ[Ö­{T_Åíð¥½úu/ºçyï³@Ù²ýà¶l}ä¡«ïù¼ |
| --- | Minor | x0'¶HñLZ£ÆEúv¬Ñ¡ r5RÂ¨XôÄ¨U1fñò¹ 7Ð¾³'ç\NW  ÅwPR¤p-vâ¡x"fy&IÔajÆ34B*À&u?©(yLÌÛ2CôÎþ¾w	³ù |
| --- | Minor | _#Î/e¾Ç/"{4åòÇ_Ï¿jÁk¸ÐsR<á£V8yq±ØZFz9§+tGM4²óêhÆÈ¸A/AÈ:(£BÚ©ðHî4±Ü¦I1º[AT!Ì0ÃKð¡¢3n:)eY#gäQetÆc¤1Ê­3"#v!xØtÌSM*ÈfE7"&ï9xã¬¿ãpù>´ð£êjõSÛßÿÛü |
| --- | Minor | ³¸öÊ3ãâäË_+ÿró?¼vú¬4é¦¶iÐdbâÑ|)Føb#*¶¹*¢kc#Jm	nMtáÍ6¯æÂµ	@®Ö ¤¶ûC _WëÔz+r"/ &EgÑÑ(&S.I?Õ5Õ=Õc.ïÛf |
| --- | Minor | Sentence exceeds complexity threshold, split for readability. Applying the split needs --strength moderate or higher. |
| --- | Minor | none (split proposal only; source not rewritten) |
| --- | Minor | none |
| --- | Minor | Check: NEEDS-LLM |
| --- | Minor | Flags:    not-assessed |
| --- | Minor | SENTENCE (Line 835, 548 words, 5 clauses)  [Script] |
| --- | Minor | }¥¸LþûYìã*tE¨'cÆèv0ßËy¼-äOÄ3jª&;åË]ýbÌÄXá4°P­ðW |
| --- | Minor | ÷ þÒqµjú\?lÇá)PóØbMö¡ÞöGÔÞ©KÉy®òÚVnP;¾|¥}cÈ/¤£RL\8)¶©£ÅÉ¥Ñþ¸póê¸TÄGØxÞëÑú)ûMG¿Ãø°úÞ~ªdí |
| --- | Minor | Ë<$+ |
| --- | Minor | ^ÈYWZ¶li¡%éáõ7Ö¯|¸bÿqùÊÕÈÿsüO\½páêxWëÁ­O<H­ßµký]»ÎØßmùãÅly×q`ýá³g¯?@åè.£)9ÝÅÄRa®µ³X |
| --- | Minor | ¦0Áª1#>ÓÙ¢xsO%©pøxQóGe)Â]¸Xçv¹\nÇ3Ê2Ê:Ê¦/À98ä©Bd* aÆý8ãc_ôg¹Û/õb£|\þ ¯WÈÓ££¯Wàx6ëg@¸¨÷JîIàñíh4|ô¨Éã¼Sãthò¸Ä8¢W§\g¬ÈÊ¸ºõÊðº¬©ÞD³aB?J"æ¨|dtÄAÌT`èÜÛ fçC9ÝzÑáPå§&9f§¸,oBÕz±YÍö0°Í²ó¿Þ&s°9kHx:;0]DÉ aø¶úÓmÃ÷;¦L>ûB~Û¬·>/³§<÷Àçr÷S/É/¬z`ÍÚÕ |
| --- | Minor | xîò)SåWä/qSMíºõu÷m¾:}Úµ3gþ9múæøkÇ*ß¹¦1Á[ ¯ûÇÓòW¯2%· `M}ÿj;Îm¸ý¾æy_®/Ëgn*]õ«·x  |
| --- | Minor | ­J0Ò[ÔÄÁ^P¡s:»ìs]æëZm ÚT»UÊP¨^+Ñ^K £fØh0ÙD.OÔ'|¦³b=jpÂn¸"â!6¼»{'<ÄXÃØ¶õþeßªÞM«ö2QÌ?Fqå×-+Ãäv%Î©é»Èí]BC¥çbDÄcu±®FÆ(/²ÔñÑ"ÕôönÿaÑUéb ¤¡,O ,§vµvF*ÜÞÑòîG®Í­ZÁë°µ¥:þ³3ß]¹òÝÓùñÆ÷ÎÍ­ÂQ!t~F%ÿæØ!_ÛåçZøª3YÀÊ¼ÆL«õhõjRÉÍ³àJíý@v£ÁªQ |
| --- | Minor | <âÌã	Xs]"èqcÝÈ:ÄN¹ÓÂñ-P;ÃV}ü8ûF}ïH,××ËÌwe*¿'ëÊâÑÞûJQH\ ù%§V-PÔ«q%âãT£vWÁætÁÞ]b§²ïîØÑ¿'µ¿Ð½ñÇýõtòM×ätýgÁj}HÂ^i4Ð/Î#juÚhåu:ííZÛÃáÎÅÞ°[s±¹Ô[ìÖê<Q*»ÑÆ*É&ÄE%!#¬v`Ñê= ´ÓÂ@Ã·ÐU mb 6­;Å2-¥*eu Wp#pÜfU¢dÅÅ$£äþèaI¢&IKk+ÉäIªÎÖÓÓ |
| --- | Minor | ²£¹¹y²cÆNÔLÔNÒMÔOpMtOôLÉÓäiótyú<w'/¦L]¡©ÐVèÊõå® w§"¦4¶^S¯­×Õëk |
| --- | Minor | ®zw½§>¦66«5¥-ÙÏ2ÙûtLÝI5NAñ£ÆûcÖã5ÜÑVyýÃØp¹äê¦jÓÁÿõÊ3/¿ýüüm}ßÈ[ö?Õ¸®bIÖðQ§{ü©)òéÇ¨/¯ËÉñjËOKVÑ FT/E¨9-©æéA4Fkä |
| --- | Minor | *	ÅñÆ´³§£ Bà²Óð÷{oQ!¡Ä	¹Lx@HJg(þ]¤3DÖ¦ MM¦VÓ	W DTBâ×'ÖsiõòÄeìåK¸Pn½ô£®zÃ WÙ±o%¢û¥ôÖJëÛTMÏæØÆè¦MB]qpÈ£÷9È«å1aÉIÁü èì÷éÝr÷/Empû¦l0eR\¼"ñd2[xdN¶ëà;laöá''à,pæu`1QuÝ©xúÈL%ß éßnX»~IMcû^yïÖòè¾mk?(Î)|qÖ§_á©YVWùàf|¬÷e5rµþúÈÄÚ5EóÎ'%}L±X·C.Q*/Å{8 èíªðí\GªQ¡PµÉáÔfZÍÄz?Ú |
| --- | Minor | ÔÊ¥wu*ª"RUÉöjÅÈR¨M4Û¬µyî÷òµ®¸tÈÓõW¯vÔ?=DÞK·mjÜºµqÓ¶2N*ë]T4G~ëÚ5ùÌ¢}exéÉ3ýäÓÏß:Aår) ¸äDí¶7ýNÝ£¦&õ&RaHÕ9ÕÉ'GP3üÎ9Å÷P Á ªØBMÏª µÀl÷Ïm_Ût~]ü»âr[ãCîÚ¹cùf'¾mÿ!!£><(Ý/¿iõW_~ùõÊU!¹¢ÞRB+õÛõ®í©ÎÔ õ³Ï&/ö¡ÌH§&ï2 e6 ^'SàSÈ]É&Jv¢6×YYDx½Oç.ü}tz:Ï)F pÝno§imçöö­ß³I÷öûïö<;UfBiÈ¿X¾ïc#ÊËCÖý}? |
| --- | Minor | }¥¸LþûYìã*tE¨'cÆèv0ßËy¼-äOÄ3jª&;åË]ýbÌÄXá4°P­ðW |
| --- | Minor | ÷ þÒqµjú\?lÇá)PóØbMö¡ÞöGÔÞ©KÉy®òÚVnP;¾|¥}cÈ/¤£RL\8)¶©£ÅÉ¥Ñþ¸póê¸TÄGØxÞëÑú)ûMG¿Ãø°úÞ~ªdí |
| --- | Minor | Ë<$+ |
| --- | Minor | ^ÈYWZ¶li¡%éáõ7Ö¯|¸bÿqùÊÕÈÿsüO\½páêxWëÁ­O<H­ßµký]»ÎØßmùãÅly×q`ýá³g¯?@åè.£)9ÝÅÄRa®µ³X |
| --- | Minor | ¦0Áª1#>ÓÙ¢xsO%©pøxQóGe)Â]¸Xçv¹\nÇ3Ê2Ê:Ê¦/À98ä©Bd* aÆý8ãc_ôg¹Û/õb£|\þ ¯WÈÓ££¯Wàx6ëg@¸¨÷JîIàñíh4|ô¨Éã¼Sãthò¸Ä8¢W§\g¬ÈÊ¸ºõÊðº¬©ÞD³aB?J"æ¨|dtÄAÌT`èÜÛ fçC9ÝzÑáPå§&9f§¸. oBÕz±YÍö0°Í²ó¿Þ&s°9kHx:;0]DÉ aø¶úÓmÃ÷;¦L>ûB~Û¬·>/³§<÷Àçr÷S/É/¬z`ÍÚÕ |
| --- | Minor | xîò)SåWä/qSMíºõu÷m¾:}Úµ3gþ9múæøkÇ*ß¹¦1Á[ ¯ûÇÓòW¯2%· `M}ÿj;Îm¸ý¾æy_®/Ëgn*]õ«·x  |
| --- | Minor | ­J0Ò[ÔÄÁ^P¡s:»ìs]æëZm ÚT»UÊP¨^+Ñ^K £fØh0ÙD.OÔ'|¦³b=jpÂn¸"â!6¼»{'<ÄXÃØ¶õþeßªÞM«ö2QÌ?Fqå×-+Ãäv%Î©é»Èí]BC¥çbDÄcu±®FÆ(/²ÔñÑ"ÕôönÿaÑUéb ¤¡. O. §vµvF*ÜÞÑòîG®Í­ZÁë°µ¥:þ³3ß]¹òÝÓùñÆ÷ÎÍ­ÂQ!t~F%ÿæØ!_ÛåçZøª3YÀÊ¼ÆL«õhõjRÉÍ³àJíý@v£ÁªQ |
| --- | Minor | <âÌã	Xs]"èqcÝÈ:ÄN¹ÓÂñ-P;ÃV}ü8ûF}ïH. ××ËÌwe*¿'ëÊâÑÞûJQH\ ù%§V-PÔ«q%âãT£vWÁætÁÞ]b§²ïîØÑ¿'µ¿Ð½ñÇýõtòM×ätýgÁj}HÂ^i4Ð/Î#juÚhåu:ííZÛÃáÎÅÞ°[s±¹Ô[ìÖê<Q*»ÑÆ*É&ÄE%!#¬v`Ñê= ´ÓÂ@Ã·ÐU mb 6­;Å2-¥*eu Wp#pÜfU¢dÅÅ$£äþèaI¢&IKk+ÉäIªÎÖÓÓ |
| --- | Minor | ²£¹¹y²cÆNÔLÔNÒMÔOpMtOôLÉÓäiótyú<w'/¦L]¡©ÐVèÊõå® w§"¦4¶^S¯­×Õëk |
| --- | Minor | ®zw½§>¦66«5¥-ÙÏ2ÙûtLÝI5NAñ£ÆûcÖã5ÜÑVyýÃØp¹äê¦jÓÁÿõÊ3/¿ýüüm}ßÈ[ö?Õ¸®bIÖðQ§{ü©)òéÇ¨/¯ËÉñjËOKVÑ FT/E¨9-©æéA4Fkä |
| --- | Minor | *	ÅñÆ´³§£ Bà²Óð÷{oQ!¡Ä	¹Lx@HJg(þ]¤3DÖ¦ MM¦VÓ	W DTBâ×'ÖsiõòÄeìåK¸Pn½ô£®zÃ WÙ±o%¢û¥ôÖJëÛTMÏæØÆè¦MB]qpÈ£÷9È«å1aÉIÁü èì÷éÝr÷/Empû¦l0eR\¼"ñd2[xdN¶ëà;laöá''à. pæu`1QuÝ©xúÈL%ß éßnX»~IMcû^yïÖòè¾mk?(Î)|qÖ§_á©YVWùàf|¬÷e5rµþúÈÄÚ5EóÎ'%}L±X·C.Q*/Å{8 èíªðí\GªQ¡PµÉáÔfZÍÄz?Ú |
| --- | Minor | ÔÊ¥wu*ª"RUÉöjÅÈR¨M4Û¬µyî÷òµ®¸tÈÓõW¯vÔ?=DÞK·mjÜºµqÓ¶2N*ë]T4G~ëÚ5ùÌ¢}exéÉ3ýäÓÏß:Aår) ¸äDí¶7ýNÝ£¦&õ&RaHÕ9ÕÉ'GP3üÎ9Å÷P Á ªØBMÏª µÀl÷Ïm_Ût~]ü»âr[ãCîÚ¹cùf'¾mÿ!!£><(Ý/¿iõW_~ùõÊU!¹¢ÞRB+õÛõ®í©ÎÔ õ³Ï&/ö¡ÌH§&ï2 e6 ^'SàSÈ]É&Jv¢6×YYDx½Oç.ü}tz:Ï)F pÝno§imçöö­ß³I÷öûïö<;UfBiÈ¿X¾ïc#ÊËCÖý}?. |
| --- | Minor | Sentence exceeds complexity threshold, split for readability. Applying the split needs --strength moderate or higher. |
| --- | Minor | none (split proposal only; source not rewritten) |
| --- | Minor | none |
| --- | Minor | Check: NEEDS-LLM |
| --- | Minor | Flags:    not-assessed |
| --- | Minor | SENTENCE (Line 835, 244 words, 2 clauses)  [Script] |
| --- | Minor | =*Å¨Ô#c	qaôê:S³V£bRè3«¼:ÁïòÒ`º"¿F]|C9õBEF ,O V®Éö­Õ	òs#aIµE4ª¼¶Ü8&ÕÆý|ÂÒÓE®ü4aéÏWÜJ¾2Ûëòº½o76_¯Í×åëó]ùî|O~ÌìØµ®µîµµ1kcw¸v¸wxvÄìÝçÚçÞçÙ³/6JJiH9`=`;vÀ~ üãõíDØ	ûðÍ123nÎ1iûIAmwMÛøðÊçì^³¡þÃWg¾2¿]¿tÉòüuì\óÕÛ;_]¾¬ /wÖ Tß/<²ÏüõÂ%Ó§¹395½±rçs>JQZ«+¢ì$ê¬¬ ÕñL³µ0\MØ§æ¼¥îåPy'H%hw²ò÷LÏ³ááJÂû³4'p*`S%	ªtG£ÉÑâÐXÀñÇ×"ÌO|òe/ï;a4³QµykË/É±r<I>RÞ[°nÊ]s¶®mü-9ìÄÇ?;ÐR)Ænâuz+³FÕ,òÙbfð^]ºæÇ4LìÕw¨½§ìö÷ÿµÆ©@îDÎþ#Ì¶æº$;IvÒiAIöH%=¨×¦Xæ<ûyyOÆåÞçÌ©{Çz{Æ+«<sÉ.ï}ôôc/à÷]Ý XP»­Q3ª½A/´ðª*úñË1üHzb+ £f4#^­x#µQË¯ó böià)r¤<Ö±@tU*ºx!Lð na0_X&*JÁFp6µMÙd.Y¬I6E~q¯oømXJËØeÜr~jzf>DÕ3u°Âø\[/íÇ)8¥7-kå½ñÌÇåå=cb |
| --- | Minor | Xx/ÄmÒBÈ[¬6«·A5ÒhG\#U*0bð¨%	PÄÈfs8aa¶Ûm±*g¥J8i¶uDUgÒD8lÊQÀ`¤3³j³=òâO:Bga@¢ ìÿP?O<L³d*4STä!îP<ð940  |
| --- | Minor | Ù/<ÃlÛ´@(1Øj |
| --- | Minor | ¶5h£ÁªÁjFMÔzÞÈ98'áÄNÆIZÎ©·Ó°ñxm¼.Qï5$ÄS#ÉéÈfnc²ÉmdÇrã#òqGòxØPÿÃ]ÆYa³³³"ÊpSF |
| --- | Minor | =*Å¨Ô#c	qaôê:S³V£bRè3«¼:ÁïòÒ`º"¿F]|C9õBEF. O V®Éö­Õ	òs#aIµE4ª¼¶Ü8&ÕÆý|ÂÒÓE®ü4aéÏWÜJ¾2Ûëòº½o76_¯Í×åëó]ùî|O~ÌìØµ®µîµµ1kcw¸v¸wxvÄìÝçÚçÞçÙ³/6JJiH9`=`;vÀ~ üãõíDØ	ûðÍ123nÎ1iûIAmwMÛøðÊçì^³¡þÃWg¾2¿]¿tÉòüuì\óÕÛ;_]¾¬ /wÖ Tß/<²ÏüõÂ%Ó§¹395½±rçs>JQZ«+¢ì$ê¬¬ ÕñL³µ0\MØ§æ¼¥îåPy'H%hw²ò÷LÏ³ááJÂû³4'p*`S%	ªtG£ÉÑâÐXÀñÇ×"ÌO|òe/ï;a4³QµykË/É±r<I>RÞ[°nÊ]s¶®mü-9ìÄÇ?;ÐR)Ænâuz+³FÕ. òÙbfð^]ºæÇ4LìÕw¨½§ìö÷ÿµÆ©@îDÎþ#Ì¶æº$;IvÒiAIöH%=¨×¦Xæ<ûyyOÆåÞçÌ©{Çz{Æ+«<sÉ.ï}ôôc/à÷]Ý XP»­Q3ª½A/´ðª*úñË1üHzb+ £f4#^­x#µQË¯ó böià)r¤<Ö±@tU*ºx!Lð na0_X&*JÁFp6µMÙd.Y¬I6E~q¯oømXJËØeÜr~jzf>DÕ3u°Âø\[/íÇ)8¥7-kå½ñÌÇåå=cb |
| --- | Minor | Xx/ÄmÒBÈ[¬6«·A5ÒhG\#U*0bð¨%	PÄÈfs8aa¶Ûm±*g¥J8i¶uDUgÒD8lÊQÀ`¤3³j³=òâO:Bga@¢ ìÿP?O<L³d*4STä!îP<ð940  |
| --- | Minor | Ù/<ÃlÛ´@(1Øj |
| --- | Minor | ¶5h£ÁªÁjFMÔzÞÈ98'áÄNÆIZÎ©·Ó°ñxm¼.Qï5$ÄS#ÉéÈfnc²ÉmdÇrã#òqGòxØPÿÃ]ÆYa³³³"ÊpSF. |
| --- | Minor | Sentence exceeds complexity threshold, split for readability. Applying the split needs --strength moderate or higher. |
| --- | Minor | none (split proposal only; source not rewritten) |
| --- | Minor | none |
| --- | Minor | Check: NEEDS-LLM |
| --- | Minor | Flags:    not-assessed |
| --- | Minor | SENTENCE (Line 853, 530 words, 12 clauses)  [Script] |
| --- | Minor | Ì FÄ%ñ *Z¯Á,g0wqÓ¸»øiüaf¶Aô^È	ËÐr¼¹ÜÏ.áðµêºúZÃRãRqisYÄ²ÈD 1u³>)¦?åÀ¯äÊ57i#PW>?p/5æµä÷ýºöãÌwÆ·ÇAu®­·L¨ Áº¢ÅlÉ@1á×Z_Ù×*÷ä7ôö|Cvâ¿2~Lz×öv÷||×è<ðÖm¯½&l¸R£¬([aÅ |
| --- | Minor | 6º`,fâmo·þaK«°á_Ë¿­r1»øæ§dÁfÙdcòåÖ}¯´R@,×2¹·÷rtOé73Ê{èwDDüdò%Ö@X2l°(¥2¯µnùCëÛÛ(0ïö~,å£øW¸ÿÜ­d}}|2d2häN7Èî2Økª`§×2DÍù´È,X<Óy#<)QNUuqXs¢½Ém¬ög2D¨ÓFø38¨Jõ9oPç 5¿% |
| --- | Minor | ¶]ÏoèOÉá^9!·½vt!3}Ú3 åèrÌßRRé_Þh*Yu(×â¼@´J ½#¢+ÝÕúï¤ë8ýìó)n<Ð{©íüSk±W¾Äê;ÞzmM|¬¨ÿ¤ðLR¾E* |
| --- | Minor | `3mâÓ}©Þ@ê`åËôÆ |
| --- | Minor | Îù wZ4Yâ2y³§eÎpA)Í)ÙòÏÉñô®A® EþVÝ*ÑÿÉäÓÞ÷üTµ·ò»U´^_ø© µr®µ ZI¼NB¬4ß 7èg¡DQRÅú<Þ0dieIÉp|]Z¦9~ð |
| --- | Minor | ¢«ë4ujÎb¶7«ù§t àÿ¤ùyù z?¸*)ß]¾E^~"g:n Ð÷Åy»Gäî=Çó?È¥R>Ü|ï~Ã_úë~Ô;LüHõyèûÌàï	ä(9ñ??ê©?ºåËÐ¡,ý.¿ÊFÈE]èI([Ã(ú§8;ZåP¡Üåy( <ªM×qoö]æ]¨kDÕÜ4(õð|²²¯£ |
| --- | Minor | z{-`® I´Í4¡IP; ïEØ÷sÉûÐ@5$ |
| --- | Minor | ñ,vMß5ö!äPjÚn.L#­¹°Æ¬`Qe£	ªÊ·¨ýW*¡ô9ÎÀñwÌ|æ[ry5±÷sÉÜÓÜ?ø¾B¸MØ¥²¨ÊUÔzuúw5µwjkÐÍÐ½®_¬ÿ!Åðkãsâ±^\/îO¿¿1Uþb`þÌ² Hw4Q£´Kù®[D»éwî¬ÿ }ú)¨òé7,ýþ¸òÝ-mÓ4ìx¨M¿dü0Ô&ÆÙmÚµy® 1¨U¡Zt*Eü£%ÊWÄó!óv£ òÃ­y0ÃFÃ%¨Ê}¨ÍÚø`t"ZóÓ 5 UÀíFÓ¯¯U£ô¡.wÁoÌÔ ±Ð*f¡¥0c>Ì«,Tfº¡M×wÃ*á· æÌuKaÞ¯}ç*Ï~ºÎeRÏÑ0«Ã8©±Je­ ì±ÀÀ÷n¼úÿÿ ï~åó[¯¡ ¯è;hNùÿáÌ1²Xå :ÕX#,]\ÈÈªÇê±¡z\¨Î |
| --- | Minor | £ü´Îíï¯3Bõ`ÚÕÒçoÊä |
| --- | Minor | #{½¼.±qä5=9}ÊË."§¼äd9±Ó£ZòÊËVî yÙJÚä%É2yA&dr°m<wðiOÈäùUä9<k Ïì×qÏXÉ~ùmü¦<MöÈSOqOÉäÉ"òÄ÷D<i]¡áZãIËdò¸HK#Íë£¹füjÈý*ìÉî]nw<ÙóvÈ.Ý	/î´«Ù²Cb'Ûéç¶ËdÛ#n[<yd«{ÄBiÇ¤f·nÑp[õdk;FÒDvl9É6U®âÍh¹Í&²Yb¡Õ8lÚxÛ u;H­¬ÐåËÜÜòkdÙÒHn, ¶rY¼h ý m5ª.âRw_óM&)D¤Hl2\Dý\Ò(%ú*¯Lx}8_@âbÍ\Ü¯ÅI¬ÄÆ¨ÇÎy ÛeâÜáÄ}uÁf.q­f£5$Zb£bI¤DÄ§ÃÏ9g¬êðpØaS»LÂDb³Z9[9±Z,ÕJ¬k±3Ì3%& ¯I&"Tâhbø;d¢ôáD/±:h¡£ |
| --- | Minor | ¬"ê"¢LÊJá¹ Ç¯"¼Ç±©e4Ï H&¸­iÄ)ÿß^èÿ5 ÿöé¯MÉ- endstream endobj 312 0 obj <</Length 101/Filter/FlateDecode>> stream x¥ÉPCO( "3"üÿ÷yóÂÂGâÊ.Ó¦Â2vù¹ÑKüÍ. |
| --- | Minor | Ì FÄ%ñ *Z¯Á. g0wqÓ¸»øiüaf¶Aô^È	ËÐr¼¹ÜÏ.áðµêºúZÃRãRqisYÄ²ÈD 1u³>)¦?åÀ¯äÊ57i#PW>?p/5æµä÷ýºöãÌwÆ·ÇAu®­·L¨ Áº¢ÅlÉ@1á×Z_Ù×*÷ä7ôö|Cvâ¿2~Lz×öv÷||×è<ðÖm¯½&l¸R£¬([aÅ |
| --- | Minor | 6º`. fâmo·þaK«°á_Ë¿­r1»øæ§dÁfÙdcòåÖ}¯´R@. ×2¹·÷rtOé73Ê{èwDDüdò%Ö@X2l°(¥2¯µnùCëÛÛ(0ïö~. å£øW¸ÿÜ­d}}|2d2häN7Èî2Økª`§×2DÍù´È. X<Óy#<)QNUuqXs¢½Ém¬ög2D¨ÓFø38¨Jõ9oPç 5¿% |
| --- | Minor | ¶]ÏoèOÉá^9!·½vt!3}Ú3 åèrÌßRRé_Þh*Yu(×â¼@´J ½#¢+ÝÕúï¤ë8ýìó)n<Ð{©íüSk±W¾Äê;ÞzmM|¬¨ÿ¤ðLR¾E* |
| --- | Minor | `3mâÓ}©Þ@ê`åËôÆ |
| --- | Minor | Îù wZ4Yâ2y³§eÎpA)Í)ÙòÏÉñô®A® EþVÝ*ÑÿÉäÓÞ÷üTµ·ò»U´^_ø© µr®µ ZI¼NB¬4ß 7èg¡DQRÅú<Þ0dieIÉp|]Z¦9~ð |
| --- | Minor | ¢«ë4ujÎb¶7«ù§t àÿ¤ùyù z?¸*)ß]¾E^~"g:n Ð÷Åy»Gäî=Çó?È¥R>Ü|ï~Ã_úë~Ô;LüHõyèûÌàï	ä(9ñ??ê©?ºåËÐ¡. ý.¿ÊFÈE]èI([Ã(ú§8;ZåP¡Üåy( <ªM×qoö]æ]¨kDÕÜ4(õð|²²¯£ |
| --- | Minor | z{-`® I´Í4¡IP; ïEØ÷sÉûÐ@5$ |
| --- | Minor | ñ. vMß5ö!äPjÚn.L#­¹°Æ¬`Qe£	ªÊ·¨ýW*¡ô9ÎÀñwÌ|æ[ry5±÷sÉÜÓÜ?ø¾B¸MØ¥²¨ÊUÔzuúw5µwjkÐÍÐ½®_¬ÿ!Åðkãsâ±^\/îO¿¿1Uþb`þÌ² Hw4Q£´Kù®[D»éwî¬ÿ }ú)¨òé7. ýþ¸òÝ-mÓ4ìx¨M¿dü0Ô&ÆÙmÚµy® 1¨U¡Zt*Eü£%ÊWÄó!óv£ òÃ­y0ÃFÃ%¨Ê}¨ÍÚø`t"ZóÓ 5 UÀíFÓ¯¯U£ô¡.wÁoÌÔ ±Ð*f¡¥0c>Ì«. Tfº¡M×wÃ*á· æÌuKaÞ¯}ç*Ï~ºÎeRÏÑ0«Ã8©±Je­ ì±ÀÀ÷n¼úÿÿ ï~åó[¯¡ ¯è;hNùÿáÌ1²Xå :ÕX#. ]\ÈÈªÇê±¡z\¨Î |
| --- | Minor | £ü´Îíï¯3Bõ`ÚÕÒçoÊä |
| --- | Minor | #{½¼.±qä5=9}ÊË."§¼äd9±Ó£ZòÊËVî yÙJÚä%É2yA&dr°m<wðiOÈäùUä9<k Ïì×qÏXÉ~ùmü¦<MöÈSOqOÉäÉ"òÄ÷D<i]¡áZãIËdò¸HK#Íë£¹füjÈý*ìÉî]nw<ÙóvÈ.Ý	/î´«Ù²Cb'Ûéç¶ËdÛ#n[<yd«{ÄBiÇ¤f·nÑp[õdk;FÒDvl9É6U®âÍh¹Í&²Yb¡Õ8lÚxÛ u;H­¬ÐåËÜÜòkdÙÒHn.  ¶rY¼h ý m5ª.âRw_óM&)D¤Hl2\Dý\Ò(%ú*¯Lx}8_@âbÍ\Ü¯ÅI¬ÄÆ¨ÇÎy ÛeâÜáÄ}uÁf.q­f£5$Zb£bI¤DÄ§ÃÏ9g¬êðpØaS»LÂDb³Z9[9±Z. ÕJ¬k±3Ì3%& ¯I&"Tâhbø;d¢ôáD/±:h¡£ |
| --- | Minor | ¬"ê"¢LÊJá¹ Ç¯"¼Ç±©e4Ï H&¸­iÄ)ÿß^èÿ5 ÿöé¯MÉ- endstream endobj 312 0 obj <</Length 101/Filter/FlateDecode>> stream x¥ÉPCO( "3"üÿ÷yóÂÂGâÊ.Ó¦Â2vù¹ÑKüÍ.. |
| --- | Minor | Sentence exceeds complexity threshold, split for readability. Applying the split needs --strength moderate or higher. |
| --- | Minor | none (split proposal only; source not rewritten) |
| --- | Minor | none |
| --- | Minor | Check: NEEDS-LLM |
| --- | Minor | Flags:    not-assessed |
| --- | Minor | SENTENCE (Line 853, 453 words, 16 clauses)  [Script] |
| --- | Minor | W|mßÇ_}¢­R²îä<((©¨%7ªméèy2L¼y/¬ÈÜ endstream endobj 313 0 obj <</Length 374/Filter/FlateDecode>> stream x]SËn0¼ó>¦@Àn$T¥}¨´§(b/R1È_ì1 	F3»;öux.^Ý,ü4,idu£¡¡{IìF÷FQÌT#GÏÜW¶Usq9 |
| --- | Minor | ×>l4¶ |
| --- | Minor | ÚZÎ83ÕÁ)Nkÿ :µÌzÓïÞí´þÙoî9ßï;ßë|çqI""w ù*ÊÊï&s ºqùâqÓ¼JÛø¹W¦HIðâ(ÃôÑ©Qö°Â"dÙ¬6!½ÊÆòi7ä²EÕUéX\ôçq¯FÃØJdF,f  7½:nuS°=êÛ:ñÐ¶DñÛ±µ[ÜØlÃ=>ñàuôlJ=>lJE7u§£KG§Ø¨#â@DS:¢ho[ Ú[Ð¶ ­-vÑêBk¯ÒbG¦9dø:64 |
| --- | Minor | jDó{¦F¿hªA¦4úÑÀJ |
| --- | Minor | × ¡>	ëuÔé¨]+ju¬ËÅ:jtÜ¿ßâ>kËP­ã:ÖaµªVª¸7Ê¢2X^¢bY°xºU,îÃ¢ *à^ÜíA¹lå)([èe-XXê½(-I¥.hñ¢$Z<4£UÊ]}X ä÷`~±*æ/Eñ6Q¬¢XSî´a^GÌ«AQ¡[yPèÆÜ®£`®* tÌ |
| --- | Minor | \ÁM½Ü/6F÷ç¶xäç%ü2äå&¼dä |
| --- | Minor | +¹é6Ü^%'> UI-P½^¡ªP5Åëõ<CpsyÝ:\<¸JÈù'öÁÉsNvàHCSì:$h-°±-ø¬qnaUçE% Áv" )9`§² |
| --- | Minor | H4(vîæüß6ú_'ð_ÿMÿÈØ¯¸ endstream endobj 22 0 obj <</Type/ObjStm/N 200/First 1844/Filter/FlateDecode/Length 5219>> stream xÚÝ\[sÛÆ~ß_Ç¤¶<û¥êTª|ïYç$¶ãdÃâ,ÁÔ!©Øþ÷û}MÊ¦b vÎ!.Ó=Ý=}Ñª62±Ð¶Ð!ÚVºBûÂ;w¾Ð©Ïc+,´¡0ªP*êÂhtÀûèÈÚX[(Ta\¡|ÂÕ*ªT JøÎ¦R¶°ªÐ/[ |
| --- | Minor | /, Ø ¸Z |,ðNß¡kipEW ÷H),Þw ñÃø(F ëð]ò©pèZÉXx	 ê@_xR¸Âz§ B9@ÉT 5'S¿ÚH¼.- ÂAúß@!J[ kÀ§xè R¨í-ð@Éá!»À #îG ð2HðÈ]x]ÉèÑuÄûøÔ«PÄ.A,Ü G|", ÄNøTÙ®­ÄoOÁ¤Ä®rèß%Lü· ña|¤.ÿ Ñx/å±ä÷8zOêäQrsóÿ5)¤bKq,TRs, ¦,ZcÑ|½OU@®@p| N­(#[|#0¥¦¬Ekù4p¤¥&ßc M5å/&Ð]ê@ºPs|*²8>ô )É±gÇgù4 O À8*bE] Ç{à	Zj9%cÀ±8pFç1{E¥Ç/<8 ùùCÕÐlñi@g |
| --- | Minor | ìó£ç=OµjÇ£äE¯0´02Á<´ 9©£â·¤Å·JÙ&x! |
| --- | Minor | W|mßÇ_}¢­R²îä<((©¨%7ªméèy2L¼y/¬ÈÜ endstream endobj 313 0 obj <</Length 374/Filter/FlateDecode>> stream x]SËn0¼ó>¦@Àn$T¥}¨´§(b/R1È_ì1 	F3»;öux.^Ý. ü4. idu£¡¡{IìF÷FQÌT#GÏÜW¶Usq9 |
| --- | Minor | ×>l4¶ |
| --- | Minor | ÚZÎ83ÕÁ)Nkÿ :µÌzÓïÞí´þÙoî9ßï;ßë|çqI""w ù*ÊÊï&s ºqùâqÓ¼JÛø¹W¦HIðâ(ÃôÑ©Qö°Â"dÙ¬6!½ÊÆòi7ä²EÕUéX\ôçq¯FÃØJdF. f  7½:nuS°=êÛ:ñÐ¶DñÛ±µ[ÜØlÃ=>ñàuôlJ=>lJE7u§£KG§Ø¨#â@DS:¢ho[ Ú[Ð¶ ­-vÑêBk¯ÒbG¦9dø:64 |
| --- | Minor | jDó{¦F¿hªA¦4úÑÀJ |
| --- | Minor | × ¡>	ëuÔé¨]+ju¬ËÅ:jtÜ¿ßâ>kËP­ã:ÖaµªVª¸7Ê¢2X^¢bY°xºU. îÃ¢ *à^ÜíA¹lå)([èe-XXê½(-I¥.hñ¢$Z<4£UÊ]}X ä÷`~±*æ/Eñ6Q¬¢XSî´a^GÌ«AQ¡[yPèÆÜ®£`®* tÌ |
| --- | Minor | \ÁM½Ü/6F÷ç¶xäç%ü2äå&¼dä |
| --- | Minor | +¹é6Ü^%'> UI-P½^¡ªP5Åëõ<CpsyÝ:\<¸JÈù'öÁÉsNvàHCSì:$h-°±-ø¬qnaUçE% Áv" )9`§² |
| --- | Minor | H4(vîæüß6ú_'ð_ÿMÿÈØ¯¸ endstream endobj 22 0 obj <</Type/ObjStm/N 200/First 1844/Filter/FlateDecode/Length 5219>> stream xÚÝ\[sÛÆ~ß_Ç¤¶<û¥êTª|ïYç$¶ãdÃâ. ÁÔ!©Øþ÷û}MÊ¦b vÎ!.Ó=Ý=}Ñª62±Ð¶Ð!ÚVºBûÂ;w¾Ð©Ïc+. ´¡0ªP*êÂhtÀûèÈÚX[(Ta\¡|ÂÕ*ªT JøÎ¦R¶°ªÐ/[ |
| --- | Minor | /. Ø ¸Z |. ðNß¡kipEW ÷H). Þw ñÃø(F ëð]ò©pèZÉXx	 ê@_xR¸Âz§ B9@ÉT 5'S¿ÚH¼.- ÂAúß@!J[ kÀ§xè R¨í-ð@Éá!»À #îG ð2HðÈ]x]ÉèÑuÄûøÔ«PÄ.A. Ü G|".  ÄNøTÙ®­ÄoOÁ¤Ä®rèß%Lü· ña|¤.ÿ Ñx/å±ä÷8zOêäQrsóÿ5)¤bKq. TRs. ¦. ZcÑ|½OU@®@p| N­(#[|#0¥¦¬Ekù4p¤¥&ßc M5å/&Ð]ê@ºPs|*²8>ô )É±gÇgù4 O À8*bE] Ç{à	Zj9%cÀ±8pFç1{E¥Ç/<8 ùùCÕÐlñi@g |
| --- | Minor | ìó£ç=OµjÇ£äE¯0´02Á<´ 9©£â·¤Å·JÙ&x!. |
| --- | Minor | Sentence exceeds complexity threshold, split for readability. Applying the split needs --strength moderate or higher. |
| --- | Minor | none (split proposal only; source not rewritten) |
| --- | Minor | none |
| --- | Minor | Check: NEEDS-LLM |
| --- | Minor | Flags:    not-assessed |
| --- | Minor | SENTENCE (Line 853, 84 words, 1 clauses)  [Script] |
| --- | Minor | ÈFJOS~/Ó÷h4L¶ <cDca49ÈQAKã;Èè iFBn¡×iC {I¤µ¬Ac¦È®àáÖc¶õ-IZç{´ÆÈ©µÃ¬Á½LaÏ^h]¶p¤µ÷lñiÄØþñÑ÷×Õèþl6_ß¼Zñ×ÿNgÌgÕb,aTÕdôÃèÉèáBÃ÷ñÙóÑãùùèÑ7§ÓU%Þ³sHYV¯Oç³åt¹ªf§ï¿ýî»Ñ³êt5ü	Ë±/d 4¢fìä»ïþk(L´³"KH	¯äM÷¨¬¦å¨¼¹Y®6ða¤ç0x'R %÷½° ýÃOAÐ24ðÂéþ»é<óÂ³ |
| --- | Minor | Kµc=®O)bô½q ëÝ~p`½éþåYùg¹º  úySW;$ÐJDZ3eDÖ cÂ`(X½Öô5)`@'|! |
| --- | Minor | ÈFJOS~/Ó÷h4L¶ <cDca49ÈQAKã;Èè iFBn¡×iC {I¤µ¬Ac¦È®àáÖc¶õ-IZç{´ÆÈ©µÃ¬Á½LaÏ^h]¶p¤µ÷lñiÄØþñÑ÷×Õèþl6_ß¼Zñ×ÿNgÌgÕb. aTÕdôÃèÉèáBÃ÷ñÙóÑãùùèÑ7§ÓU%Þ³sHYV¯Oç³åt¹ªf§ï¿ýî»Ñ³êt5ü	Ë±/d 4¢fìä»ïþk(L´³"KH	¯äM÷¨¬¦å¨¼¹Y®6ða¤ç0x'R %÷½° ýÃOAÐ24ðÂéþ»é<óÂ³ |
| --- | Minor | Kµc=®O)bô½q ëÝ~p`½éþåYùg¹º  úySW;$ÐJDZ3eDÖ cÂ`(X½Öô5)`@'|!. |
| --- | Minor | Sentence exceeds complexity threshold, split for readability. Applying the split needs --strength moderate or higher. |
| --- | Minor | none (split proposal only; source not rewritten) |
| --- | Minor | none |
| --- | Minor | Check: NEEDS-LLM |
| --- | Minor | Flags:    not-assessed |
| --- | Minor | SENTENCE (Line 853, 265 words, 3 clauses)  [Script] |
| --- | Minor | ·¡ÅÕöAUyóª½®.ÏhÁN§ËÓ­:âO£CE¤ÐàKC!pSj ×Ð\½ëuNâºIvÝ¤ÓÇ&üi1?}^­Æ£^TïV£'W»ëËúò¤#2-Aèka¶äNÀSF .njÏÉ.ÊÙ§ååôÕ¢ E»ÞëKÆ+Aeo(}z!ÉYùvz-]ï¦W7W-æ³ |
| --- | Minor | °Û B~8Áx/]Áàa?ÉC= p].¦Ë)âëÌéì|+`>£ú¸±Æ¸q éc­5ÉÇTb§84Z2mÉW>1H	b ý0LpBI |¸¡àõ¦Ü>$>åeìîáßF(5øo¸;,¹Ðbßab)+ójÂnú@áíþ_L/¡vez{1o úñ\ên o¸l<(Æ)ao*THüQ.Î«â)_tEZæÇDi¸ÅÂRL¹7(Yº­`ZúÀâöØRy#|^Íó"æ¤0øÃ ¸è¨ABk- ¼Ø= ¯oÕ®M ¬¥YÃ&¸X0laÊã­a;©³qìö«êý|vvU¾/¦«÷;«EÖä5K(jKÌµ[ø¨z bVcËþ¼V4(	fb#né`P¡:üYÎªK(j¦[â`]"x:ÚzÁµxæ<¢`Àuk«fÖ±®ÞWÕÀUµ\M¯öbDåÈåJN¤u@8SiCk_¥¢1²~CºLY6:'ÄÓåh¯ë©IQ/ |
| --- | Minor | Ú;Á²tB²ú«{Ðr®RTå¬¼|¿.[ùNa,«1°°1Ú!1`¢W²lA¢1úü{Ïmsm­Ö5)Ì#ò¢õ¿M6tè¼çª|uYÐHØçÄP%t®]ÅÕ¦Â+/BWö¡¼¾®fgÓwâþNîÛ°k¥^u÷õôüfQ	ÕÊXcE`%näêÉá²V]eëªßd# î[ÑãÀ8ýÖ+ÆV#pL]¯·@oWc9í 9Öú>%áëòY0àlÿþ¢õ-rÞÊð·V¥s¹mÝf!£4{Óro^Ñ.Èu¹*7üåùÂÑ=ª§éõj¾È?}üþòï_þ÷£êMùòæyµ¾¾÷dU^NOG'åù²H>¿ûàÁüÝø^´²¸g,+IsÉ° ýò´­¤Óý³}O?zX^ÿPMÏ/Vý¶iÕ}ß_Vøõ|U]½ÄN¦WekJ>-ßý:=[]ÁbÜ­IJcçå #zÅäpÖ×Ä¬CÝö¬Õr¢d¢²H¬}àî¨<(ea¹lÂïYÜKãÙÁ's JFín¾Ï·îE\ÛFÄµ? |
| --- | Minor | ·¡ÅÕöAUyóª½®.ÏhÁN§ËÓ­:âO£CE¤ÐàKC!pSj ×Ð\½ëuNâºIvÝ¤ÓÇ&üi1?}^­Æ£^TïV£'W»ëËúò¤#2-Aèka¶äNÀSF .njÏÉ.ÊÙ§ååôÕ¢ E»ÞëKÆ+Aeo(}z!ÉYùvz-]ï¦W7W-æ³ |
| --- | Minor | °Û B~8Áx/]Áàa?ÉC= p].¦Ë)âëÌéì|+`>£ú¸±Æ¸q éc­5ÉÇTb§84Z2mÉW>1H	b ý0LpBI |¸¡àõ¦Ü>$>åeìîáßF(5øo¸;. ¹Ðbßab)+ójÂnú@áíþ_L/¡vez{1o úñ\ên o¸l<(Æ)ao*THüQ.Î«â)_tEZæÇDi¸ÅÂRL¹7(Yº­`ZúÀâöØRy#|^Íó"æ¤0øÃ ¸è¨ABk- ¼Ø= ¯oÕ®M ¬¥YÃ&¸X0laÊã­a;©³qìö«êý|vvU¾/¦«÷;«EÖä5K(jKÌµ[ø¨z bVcËþ¼V4(	fb#né`P¡:üYÎªK(j¦[â`]"x:ÚzÁµxæ<¢`Àuk«fÖ±®ÞWÕÀUµ\M¯öbDåÈåJN¤u@8SiCk_¥¢1²~CºLY6:'ÄÓåh¯ë©IQ/ |
| --- | Minor | Ú;Á²tB²ú«{Ðr®RTå¬¼|¿.[ùNa. «1°°1Ú!1`¢W²lA¢1úü{Ïmsm­Ö5)Ì#ò¢õ¿M6tè¼çª|uYÐHØçÄP%t®]ÅÕ¦Â+/BWö¡¼¾®fgÓwâþNîÛ°k¥^u÷õôüfQ	ÕÊXcE`%näêÉá²V]eëªßd# î[ÑãÀ8ýÖ+ÆV#pL]¯·@oWc9í 9Öú>%áëòY0àlÿþ¢õ-rÞÊð·V¥s¹mÝf!£4{Óro^Ñ.Èu¹*7üåùÂÑ=ª§éõj¾È?}üþòï_þ÷£êMùòæyµ¾¾÷dU^NOG'åù²H>¿ûàÁüÝø^´²¸g. +IsÉ° ýò´­¤Óý³}O?zX^ÿPMÏ/Vý¶iÕ}ß_Vøõ|U]½ÄN¦WekJ>-ßý:=[]ÁbÜ­IJcçå #zÅäpÖ×Ä¬CÝö¬Õr¢d¢²H¬}àî¨<(ea¹lÂïYÜKãÙÁ's JFín¾Ï·îE\ÛFÄµ?. |
| --- | Minor | Sentence exceeds complexity threshold, split for readability. Applying the split needs --strength moderate or higher. |
| --- | Minor | none (split proposal only; source not rewritten) |
| --- | Minor | none |
| --- | Minor | Check: NEEDS-LLM |
| --- | Minor | Flags:    not-assessed |
| --- | Minor | SENTENCE (Line 853, 783 words, 8 clauses)  [Script] |
| --- | Minor | âá."¾ïQ²­Í¾lÇ#eûñãÇ''¿Ù6zW¶½ÏOÑ¸Û©{¶Õ°Ý}¶{¶À÷(¶¹ÇvãdûÃÿïN~iÃ|4]^_ïpÖø^.ÍÏ¼AuÏû´Ë{W«µ¨£}7öß>´¤ 6R`å¾Xu)¸íã!ì	Õ[ð'&ïpªÝ®¼)7ë}Jµ·"m>xÊ=µj{J?pmyX%U«¹§ÜÛS÷§Lç´Î}Õøûw«ÇÏWå ¼ºïëÏ|¾c¿£Ý¦{ð |
| --- | Minor | ~QÙþë¬¦Ò¹ÁÀ­÷Üe y5n½C¤´lFqy£àæ)&ÕàÞÒRRÈ¼ehQ¦ôÜ½hg´[¢VÑ. # úÛ¿^½¶DáÉ/ý%ÂîV\Ö½boÖ?ª(¸È"$SÜ	Y Nt	áÆ)SMxé¹p2tNÐKÚ&jäÒ¤º¡³eºcBL¨ÄU U8Ìç¼Ù0yÖHÃõFñºOÐNiÁ]j¬ÜX¬Ï6â¾¶ýÊ~Ì©7.WÖ©õá| B÷ cKm±Ô{´Üé§XkÀºÝ²9ïÈSiy&©ÃA}òòyWë´Æh¹;·7Ð¡Uóâ<ü¤º>XØ¼±6³OzkY/y5»cÈznítwLãÄV	Ü½Î¸±"ÈËð©ÛÆì}r'H+çÖJ>o­â-v³m!w²k\Yo-á>l¿°L-Z(Á¼ëW$®Ãå ÏËiUW juQÍÕU;Oì¸ËoÀÏm~ªc¸GluEákÐÖÀåS/z­¶Ã¶6ë-ljsÿq§°ËËs._´	®ëÔ b²õå	\4 |
| --- | Minor | 7J( .pN¢cî²iÙA¶-Ã¨µc3ËGj¶nh9Ä[5±£¦éóÚp|¾¥3xÆD4{9ûÏËÓwîd8®qò^¹·F\ý`óµO'#ï!¡¦Z¶µ¾?Ð®µ£&æ-±	SJó`­-®)êÏ«,µElGZÁÚaùi[K~Z·^vZ¶Ú©å;YSÆÂsÍ<Â 8Éz2Û#dnÕ¡&n [hâ{Ø-äÆ Ú:Çeà`rÅ¡ÃNûÙÒ®×¼Ì3Ð1äsª1@PxëÂ0zBx·/äãªsñ¡²i $¸Fì	ËEîêRg}Þ)¥0{.euQzwD:©å8·ÔUKÈ1Úv«3½Y gKº/môÈÃ¶4÷sû$)EMBBD&}%C59»µê´Eên#/»ÕT1åÍ÷LÅBG®7Å ¯c¨±%¥ÁÀ,O%áio=è1rwW®u®fÌ§T	ÞÄíöFu5/7¯6!m{×¨ò09wÕúÇæ¯µ½ÓtÇÁh©9÷·ºW¶ò\0¢ëÅßÿ½^ú5öáÖn°]W´Ô´öG®®þðäá¯¿?úòêº^">ª`Äò Å­Õ"Å¿ÛE lS0üØ{»®áÒþF& ÎøE#¹PDi9þ¼¢¼ëAÌS#æë:17úb~ ßãä;îÉw]Éðw«Ð&ü=«t½Þ¥ 4Xõ®ëFvÁÊê½qó!ëÝ.tyÊ].º)ÐÖ4%º) -¾Ê;]GOqNÓøjf:£E»ùn¢¼Ïîe8lÂ®p ì w	»à{ðýx+ø¿Y3Vÿ1óí5Ûã0 |
| --- | Minor | \ÀÃrÛò­·^t«fá`ø`Jy§È©íC·jëØ½oýüá/_|5¾µÍßÍ¹uh&#ÄÈ}ÄÈ;ù#·¢}}âØ'#uKüöÏþ ÒÀF¾Í½þØßí^ö¿ð©Ýø»÷¿wë}&õ Ï£ÅcöäYÝÅÑ:ïq¼çhÁØë_üøûÃ¿Aõ¯ÿLÛd endstream endobj 319 0 obj <</Length 10/Filter/FlateDecode>> stream xc`    endstream endobj 321 0 obj <</Length 228/Filter/FlateDecode>> stream x]P1nÃ0Üõ é(ÉÉP¤&ELEY¢µ ØÜNÝúÕÍ)}á!ÃN({Õé¬GYÅÛÖ2îó²eÙ/ãº ÍCAã8À`ÿáwUïþÒ×òÁõxä4ê³hXeLÙùáÑÌDl¯¦ú*|ÀÇíRLEUòjtI endstream endobj 326 0 obj <</Type/XObject/Subtype/Form/FormType 1/BBox[0 0 245.27952 248.87952]/Matrix[1 0 0 1 0 0]/Resources<</Font 299 0 R/XObject 322 0 R/ExtGState 323 0 R/Pattern 324 0 R/Shading 325 0 R/ProcSet[/PDF/Text/ImageB/ImageC/ImageI]>>/Filter/FlateDecode/Length 2291>> stream xÚíYMsÜÆÕ¿GíAÃéï%'R#Vùàøà#ÕÒ±)ËNþ}^° î®v×SUTþt÷Ì»úËíoÞÝþãÍ«öë·ÍÕðôîSCíGüÜµºýß[jßàç®ÑxºoØ:Å!9ÆÓºxbUÌ¿­!Y>ý»iÞ7W/¡âÞyÓ4A+<»,+²R£¢ñZ R Y:ªÒxKüd\rJx]ÂX%|¥z¬#m:{à¨Þ¤&oõÛÑË/"ÆG:ai£¹×%òÙW_F7â>êîØáËÐ*h#$¨ËÛ Ù.InV£eÊ4)Ò6Û´×%ìYöÑÖy+Ñ/p3p¸÷F¢lõÞÍáyI²tÓÇh³I°DGÒTâë ·Ai&[9Z¢Ç:zõ¥þrû |
| --- | Minor | »8¼©E¾nÓ*=_{·Ù«¦+ðwý­å^%]df)øÍ«ËøEû#;XS`ûö¾Ëûg`³!¤Â;Ü¿e}÷Ïk8`µ5=v¸Ëú.ï_"Ed=v¸Ëú.î3A!»ÀÅü7`û÷¾Ò¿bø-q2ö(¯c4\ùÿëöÆÂà?&t*Y¢ÉÆöÝ}óêº¹zMmh¯ßç9ùú¦ù¾}þìí ¯¢º'ö½?ú:Cm1Ö|þ¬]Á¡¤}Ô0<öÏç«ööú¨äN%9´Â¼t¯ºVñl+ß`9KY¼§èØøO¶M, Q!úyèAL36À |
| --- | Minor | ¨i+,Õ`©¿^7ß69åØ­L±êÎFU¦;1U5oÐïa&fù æ¨^¯Zgò(f^ÂxRùäñÙÎúzÕÃ0ýÝø­õªªê_ã·~·ª¼¯GIö|õeà t.p¤,º>JÃ£	!øó°ñµuÁE¬#Þ¾XåaÃb7µÑÎÚçéú?ïõu4µÌÍø¥ÛýÐ{J@~äcq'SD!FÛT%d@çbÓY ã=h ùçLÉß³B5¯³Êå îØÕ(	Utö£`dÙuV¡Zgñy¥4ü4õyúù~Ñjæ¶Ý4T??¾WVÍ(NÓìNÍùUíSp8àg'nEO¥ù~)ÜhõÐ¹pçÖJ6¡ªnq KÞËùvÙùf_çÛ©óUùoæÒóxî(z7íóÓ¾q[Fÿ¨Q+OAÝï[£éÁóM}£5,a,¯³v^2ÝÁ~è:ú8¹å»ßuËá½. |
| --- | Minor | âá."¾ïQ²­Í¾lÇ#eûñãÇ''¿Ù6zW¶½ÏOÑ¸Û©{¶Õ°Ý}¶{¶À÷(¶¹ÇvãdûÃÿïN~iÃ|4]^_ïpÖø^.ÍÏ¼AuÏû´Ë{W«µ¨£}7öß>´¤ 6R`å¾Xu)¸íã!ì	Õ[ð'&ïpªÝ®¼)7ë}Jµ·"m>xÊ=µj{J?pmyX%U«¹§ÜÛS÷§Lç´Î}Õøûw«ÇÏWå ¼ºïëÏ|¾c¿£Ý¦{ð |
| --- | Minor | ~QÙþë¬¦Ò¹ÁÀ­÷Üe y5n½C¤´lFqy£àæ)&ÕàÞÒRRÈ¼ehQ¦ôÜ½hg´[¢VÑ. # úÛ¿^½¶DáÉ/ý%ÂîV\Ö½boÖ?ª(¸È"$SÜ	Y Nt	áÆ)SMxé¹p2tNÐKÚ&jäÒ¤º¡³eºcBL¨ÄU U8Ìç¼Ù0yÖHÃõFñºOÐNiÁ]j¬ÜX¬Ï6â¾¶ýÊ~Ì©7.WÖ©õá| B÷ cKm±Ô{´Üé§XkÀºÝ²9ïÈSiy&©ÃA}òòyWë´Æh¹;·7Ð¡Uóâ<ü¤º>XØ¼±6³OzkY/y5»cÈznítwLãÄV	Ü½Î¸±"ÈËð©ÛÆì}r'H+çÖJ>o­â-v³m!w²k\Yo-á>l¿°L-Z(Á¼ëW$®Ãå ÏËiUW juQÍÕU;Oì¸ËoÀÏm~ªc¸GluEákÐÖÀåS/z­¶Ã¶6ë-ljsÿq§°ËËs._´	®ëÔ b²õå	\4 |
| --- | Minor | 7J( .pN¢cî²iÙA¶-Ã¨µc3ËGj¶nh9Ä[5±£¦éóÚp|¾¥3xÆD4{9ûÏËÓwîd8®qò^¹·F\ý`óµO'#ï!¡¦Z¶µ¾?Ð®µ£&æ-±	SJó`­-®)êÏ«. µElGZÁÚaùi[K~Z·^vZ¶Ú©å;YSÆÂsÍ<Â 8Éz2Û#dnÕ¡&n [hâ{Ø-äÆ Ú:Çeà`rÅ¡ÃNûÙÒ®×¼Ì3Ð1äsª1@PxëÂ0zBx·/äãªsñ¡²i $¸Fì	ËEîêRg}Þ)¥0{.euQzwD:©å8·ÔUKÈ1Úv«3½Y gKº/môÈÃ¶4÷sû$)EMBBD&}%C59»µê´Eên#/»ÕT1åÍ÷LÅBG®7Å ¯c¨±%¥ÁÀ. O%áio=è1rwW®u®fÌ§T	ÞÄíöFu5/7¯6!m{×¨ò09wÕúÇæ¯µ½ÓtÇÁh©9÷·ºW¶ò\0¢ëÅßÿ½^ú5öáÖn°]W´Ô´öG®®þðäá¯¿?úòêº^">ª`Äò Å­Õ"Å¿ÛE lS0üØ{»®áÒþF& ÎøE#¹PDi9þ¼¢¼ëAÌS#æë:17úb~ ßãä;îÉw]Éðw«Ð&ü=«t½Þ¥ 4Xõ®ëFvÁÊê½qó!ëÝ.tyÊ].º)ÐÖ4%º) -¾Ê;]GOqNÓøjf:£E»ùn¢¼Ïîe8lÂ®p ì w	»à{ðýx+ø¿Y3Vÿ1óí5Ûã0 |
| --- | Minor | \ÀÃrÛò­·^t«fá`ø`Jy§È©íC·jëØ½oýüá/_|5¾µÍßÍ¹uh&#ÄÈ}ÄÈ;ù#·¢}}âØ'#uKüöÏþ ÒÀF¾Í½þØßí^ö¿ð©Ýø»÷¿wë}&õ Ï£ÅcöäYÝÅÑ:ïq¼çhÁØë_üøûÃ¿Aõ¯ÿLÛd endstream endobj 319 0 obj <</Length 10/Filter/FlateDecode>> stream xc`    endstream endobj 321 0 obj <</Length 228/Filter/FlateDecode>> stream x]P1nÃ0Üõ é(ÉÉP¤&ELEY¢µ ØÜNÝúÕÍ)}á!ÃN({Õé¬GYÅÛÖ2îó²eÙ/ãº ÍCAã8À`ÿáwUïþÒ×òÁõxä4ê³hXeLÙùáÑÌDl¯¦ú*|ÀÇíRLEUòjtI endstream endobj 326 0 obj <</Type/XObject/Subtype/Form/FormType 1/BBox[0 0 245.27952 248.87952]/Matrix[1 0 0 1 0 0]/Resources<</Font 299 0 R/XObject 322 0 R/ExtGState 323 0 R/Pattern 324 0 R/Shading 325 0 R/ProcSet[/PDF/Text/ImageB/ImageC/ImageI]>>/Filter/FlateDecode/Length 2291>> stream xÚíYMsÜÆÕ¿GíAÃéï%'R#Vùàøà#ÕÒ±)ËNþ}^° î®v×SUTþt÷Ì»úËíoÞÝþãÍ«öë·ÍÕðôîSCíGüÜµºýß[jßàç®ÑxºoØ:Å!9ÆÓºxbUÌ¿­!Y>ý»iÞ7W/¡âÞyÓ4A+<». +²R£¢ñZ R Y:ªÒxKüd\rJx]ÂX%|¥z¬#m:{à¨Þ¤&oõÛÑË/"ÆG:ai£¹×%òÙW_F7â>êîØáËÐ*h#$¨ËÛ Ù.InV£eÊ4)Ò6Û´×%ìYöÑÖy+Ñ/p3p¸÷F¢lõÞÍáyI²tÓÇh³I°DGÒTâë ·Ai&[9Z¢Ç:zõ¥þrû |
| --- | Minor | »8¼©E¾nÓ*=_{·Ù«¦+ðwý­å^%]df)øÍ«ËøEû#;XS`ûö¾Ëûg`³!¤Â;Ü¿e}÷Ïk8`µ5=v¸Ëú.ï_"Ed=v¸Ëú.î3A!»ÀÅü7`û÷¾Ò¿bø-q2ö(¯c4\ùÿëöÆÂà?&t*Y¢ÉÆöÝ}óêº¹zMmh¯ßç9ùú¦ù¾}þìí ¯¢º'ö½?ú:Cm1Ö|þ¬]Á¡¤}Ô0<öÏç«ööú¨äN%9´Â¼t¯ºVñl+ß`9KY¼§èØøO¶M. Q!úyèAL36À |
| --- | Minor | ¨i+. Õ`©¿^7ß69åØ­L±êÎFU¦;1U5oÐïa&fù æ¨^¯Zgò(f^ÂxRùäñÙÎúzÕÃ0ýÝø­õªªê_ã·~·ª¼¯GIö|õeà t.p¤. º>JÃ£	!øó°ñµuÁE¬#Þ¾XåaÃb7µÑÎÚçéú?ïõu4µÌÍø¥ÛýÐ{J@~äcq'SD!FÛT%d@çbÓY ã=h ùçLÉß³B5¯³Êå îØÕ(	Utö£`dÙuV¡Zgñy¥4ü4õyúù~Ñjæ¶Ý4T??¾WVÍ(NÓìNÍùUíSp8àg'nEO¥ù~)ÜhõÐ¹pçÖJ6¡ªnq KÞËùvÙùf_çÛ©óUùoæÒóxî(z7íóÓ¾q[Fÿ¨Q+OAÝï[£éÁóM}£5. a. ¯³v^2ÝÁ~è:ú8¹å»ßuËá½.. |
| --- | Minor | Sentence exceeds complexity threshold, split for readability. Applying the split needs --strength moderate or higher. |
| --- | Minor | none (split proposal only; source not rewritten) |
| --- | Minor | none |
| --- | Minor | Check: NEEDS-LLM |
| --- | Minor | Flags:    not-assessed |
| --- | Minor | SENTENCE (Line 853, 173 words, 2 clauses)  [Script] |
| --- | Minor | K¹BÁ^-¾ô$eîªà(Âá£eé½ôà`QÈ\YE¼âñîÖy`&)ásý­ºã` )lÌ0¹zV+÷ÊyDÒÁ,Ïá7QµÆ´§}ÈbÈ;|§0/M¥xj^Øi¡Gk´"Iqsm"ØËg­E[/§:Ò6^.·»çÆ¨jªå\åä®íg>Sðìþæá0­ç£Õý7ëç`ÎwcÛºÒíµ¡ siÛbÆ¬·Í¾úQºkäF¡cIH}~!Ã`DÅ÷º=T¯ý}Ä¨¢½Æ§»N!n:eBßK]ÌÓõ>É­8 O¹1KãyUS£>g \êçC0£iúÞT÷á7e¾z¨dtÏ.<JC«jxFJNØ¨`ÆPNoJ;5'"0õè |
| --- | Minor | ) PPÌÎ {¼.aÃ*1TGúøÐ¦ Ï×Ùø*¶*Íå1þh#Wäecy«E~÷]«Õäx§ûÒéìL1,¥Þõ:4ËêvÇÞ7;È¢-0 |ñLÖ&up@Õí(±¸Ã}B NQ{ñÜÙ&ýupDÕ-DÔ9ï¬ÜI?zñlÝ&ávpDÕ-D4:åÂL;ÓE4^:¢%?¸9ß¡]V·;¢rFt 	é¾¥CSuª ÃAÄÐn-¯w!Åù`+kæÓåõÇÆªªdä5Ox·TüÜÎ¸ÛX3àÇ<PQ!èºÿëqGµ|qVri_ÊñøØûÇ.JÕ6â.ºÿïÖ |
| --- | Minor | K¹BÁ^-¾ô$eîªà(Âá£eé½ôà`QÈ\YE¼âñîÖy`&)ásý­ºã` )lÌ0¹zV+÷ÊyDÒÁ. Ïá7QµÆ´§}ÈbÈ;|§0/M¥xj^Øi¡Gk´"Iqsm"ØËg­E[/§:Ò6^.·»çÆ¨jªå\åä®íg>Sðìþæá0­ç£Õý7ëç`ÎwcÛºÒíµ¡ siÛbÆ¬·Í¾úQºkäF¡cIH}~!Ã`DÅ÷º=T¯ý}Ä¨¢½Æ§»N!n:eBßK]ÌÓõ>É­8 O¹1KãyUS£>g \êçC0£iúÞT÷á7e¾z¨dtÏ.<JC«jxFJNØ¨`ÆPNoJ;5'"0õè |
| --- | Minor | ) PPÌÎ {¼.aÃ*1TGúøÐ¦ Ï×Ùø*¶*Íå1þh#Wäecy«E~÷]«Õäx§ûÒéìL1. ¥Þõ:4ËêvÇÞ7;È¢-0 |ñLÖ&up@Õí(±¸Ã}B NQ{ñÜÙ&ýupDÕ-DÔ9ï¬ÜI?zñlÝ&ávpDÕ-D4:åÂL;ÓE4^:¢%?¸9ß¡]V·;¢rFt 	é¾¥CSuª ÃAÄÐn-¯w!Åù`+kæÓåõÇÆªªdä5Ox·TüÜÎ¸ÛX3àÇ<PQ!èºÿëqGµ|qVri_ÊñøØûÇ.JÕ6â.ºÿïÖ. |
| --- | Minor | Sentence exceeds complexity threshold, split for readability. Applying the split needs --strength moderate or higher. |
| --- | Minor | none (split proposal only; source not rewritten) |
| --- | Minor | none |
| --- | Minor | Check: NEEDS-LLM |
| --- | Minor | Flags:    not-assessed |
| --- | Minor | SENTENCE (Line 939, 104 words, 5 clauses)  [Script] |
| --- | Minor | ¥7·o*ßo61aª´ÏsõÚlò·,0{çNGú1 |
| --- | Minor | ] Ë44Éí_z¢¡GQMÂYè\$¡åÂ2þ)9è(5tLAàN:ß¡>Ð'& =ÚóÏ¸@?Ë­qxb¿}Ðð|Àeî9_?QÏûRÏ&` 3Ï¸x6Ý©öw>wÞsZÿRÚy{·=¾×Ï»g÷½XçGï¦Æ,Âý.¡âwR3=¼¾¤õ1ÆÇ4oFjã£Lü,=÷¼³òj¼W«ÍKAzÐy	çã­,ú|óI­ó^JÚ	éæZç¡3ÓÍXÊ/÷¿(mÆÉµ8Ì 3³Íá ªÞ¹uÊïÝ÷ßûãló#ÜÙFH¶»¤±ÔTzkt4Èbn5ªªôÍÿH'ù* endstream endobj 327 0 obj <</Filter/FlateDecode/Length 1628>> stream xÚÍYM5½ó+úÆ±Ëå² |
| --- | Minor | 	N{Û;;¹¡øû?Êv÷´GQ´Hd5ê·Û®W¯;ËçÅ,ÿÌâañ&ªþ-Ïxì#~^~x\Þ½7ß! |
| --- | Minor | ¥7·o*ßo61aª´ÏsõÚlò·. 0{çNGú1 |
| --- | Minor | ] Ë44Éí_z¢¡GQMÂYè\$¡åÂ2þ)9è(5tLAàN:ß¡>Ð'& =ÚóÏ¸@?Ë­qxb¿}Ðð|Àeî9_?QÏûRÏ&` 3Ï¸x6Ý©öw>wÞsZÿRÚy{·=¾×Ï»g÷½XçGï¦Æ. Âý.¡âwR3=¼¾¤õ1ÆÇ4oFjã£Lü. =÷¼³òj¼W«ÍKAzÐy	çã­. ú|óI­ó^JÚ	éæZç¡3ÓÍXÊ/÷¿(mÆÉµ8Ì 3³Íá ªÞ¹uÊïÝ÷ßûãló#ÜÙFH¶»¤±ÔTzkt4Èbn5ªªôÍÿH'ù* endstream endobj 327 0 obj <</Filter/FlateDecode/Length 1628>> stream xÚÍYM5½ó+úÆ±Ëå² |
| --- | Minor | 	N{Û;;¹¡øû?Êv÷´GQ´Hd5ê·Û®W¯;ËçÅ. ÿÌâañ&ªþ-Ïxì#~^~x\Þ½7ß!. |
| --- | Minor | Sentence exceeds complexity threshold, split for readability. Applying the split needs --strength moderate or higher. |
| --- | Minor | none (split proposal only; source not rewritten) |
| --- | Minor | none |
| --- | Minor | Check: NEEDS-LLM |
| --- | Minor | Flags:    not-assessed |
| --- | Minor | SENTENCE (Line 939, 61 words, 1 clauses)  [Script] |
| --- | Minor | \¯ òÍðìòxùýAktg|uæüçã/ËOõa³­¢:ô|Ê¢ó´¬WZ@}Â9 _Í³Ö`y½ µóÉÚ4JO<ú|we È¹¥íKZGb½êd&_Ëo¼ÔksÏÏxj[×'gÁUîØäªË±)¸3E[åÁpÙ7¼áÛ:sot :aÖÄ¬v&»à*;âà®Õ6+VÀvmrÊ¡ñ±ñëÛ±GT§}oÜÜVQn+è ^3æN|©dá1¡YjzÖSÖ ­,p[ÛèèàÔ?oñèZ |
| --- | Minor | ­ëipÊ! |
| --- | Minor | \¯ òÍðìòxùýAktg|uæüçã/ËOõa³­¢:ô|Ê¢ó´¬WZ@}Â9 _Í³Ö`y½ µóÉÚ4JO<ú|we È¹¥íKZGb½êd&_Ëo¼ÔksÏÏxj[×'gÁUîØäªË±)¸3E[åÁpÙ7¼áÛ:sot :aÖÄ¬v&»à*;âà®Õ6+VÀvmrÊ¡ñ±ñëÛ±GT§}oÜÜVQn+è ^3æN|©dá1¡YjzÖSÖ ­. p[ÛèèàÔ?oñèZ |
| --- | Minor | ­ëipÊ!. |
| --- | Minor | Sentence exceeds complexity threshold, split for readability. Applying the split needs --strength moderate or higher. |
| --- | Minor | none (split proposal only; source not rewritten) |
| --- | Minor | none |
| --- | Minor | Check: NEEDS-LLM |
| --- | Minor | Flags:    not-assessed |
| --- | Minor | SENTENCE (Line 939, 313 words, 4 clauses)  [Script] |
| --- | Minor | ÙËä-Õhpô§¦?Á¾ÍrÙp>nN×¶ýv÷qQMØ>Ë1æju<å >C*XóØ±g/ö­¥äí©üs |
| --- | Minor | ^i%)]~ðÌj¶ <ü¯<ãü¸0uqoÀ»®½{ïvi·ÀÂøÛø/É¡äÜÄ.´à³ôMÆP¸}(¦yÚ¢RôZ¾Oâ\Êj!uZsi0?ê;Í¥OóþõC÷î¥úNfñ¹Ó­×ú{×ÙÐD23¼åà1ÒGR<\ÃnT^Êò¹ÔheÄs?1õ½Ñ;.éOëï¼ÂÊpÉ\ìÍ¬ 9Ê#RoèÝ	SÇõÌg:ëÛ.µJ[m«Ú|ãÃLk c×CZH\¸Áov×±ZJË°6Ú=BD¤dé |
| --- | Minor | =)CQ]âs º¡÷eáÙÆÆÍUXÚÒµó |
| --- | Minor | {ÑºJ®S 6 ÆW·u&N6Å |
| --- | Minor | · +»3*;µ6òÇUÄÍ¶AõÝpËùºh¡ ùµu/<Lôoæ M·Ð=9ËXï;tpacip¿«·V[9Wâ)gÈÏv¸¸ÿ©XMÁ«T(óöZ3pIñ¡°Nü |
| --- | Minor | ÉvÐ}Móô½hð>t)haOIjfÔà>0£Üõ-,ëË,c.1_î)iÔí¢i}¥oé ãS¹TLm`3}¥Sa¨?[6tÙbÃ÷ c,oÌäTðO½ÞJÿ´ÊFÝð¡xLèÓsÙ)þN¸/X{«¯$äåÉh´Ý¿ß9NM"0m¯T6¿«ÖKåÝ9´UdI|[«ÅQ±Îíë¾´SÀ1KkôQ°~`}[æêæ»ÉZ¨ö^q-ûká+®E¯¸Vàv­.â³FÐýLë/_æa/Áa§Ç )e-(¯Ý¯«jègY)ÂBHÒ}t£½÷7¼Nº·ÅHAÿÍõô(ðz&P=ägÓmÙFÎ2jÏS²£¦ýÚÔµ¾©k9JQ»òRVo#aá×¢¦7ª~<£tZÑ­ïïÙn¸ÕIiåïÄ)»Ëª;3pç®inqCÕ]Üíã	n.ëô=*í°Õä°°`cíåÛö.ñs÷¾ù9ùC² endstream endobj 340 0 obj <</Filter/FlateDecode/Length 4145>> stream xÚÅ\Ks ÁeáCmú^ÄÎ¯/"\/' |
| --- | Minor | Ü,oæM"­Cú­Z»ºciO³¶ÄÓîn´?5nÔ=J½ò2ò¸yõMÆªO0ý[û§pZøpÃX¤æý+++½æÕ%ù6&k­¯Z Xaz£´eÔ¥ïD	Iq~pJ<?Mû©¿%«T<}_UÐè>ÿÄïÅkÿ9ëÊÛ¢æ |
| --- | Minor | }âÙ#bmÙúòÅøSîC|ðY&åÐ5)Ô£ÍÛÐ¥ØÆlÛ[ |
| --- | Minor | g#ðÓióÒé'ÀMÇ§³ÇÍVxúñDD·>8ñôß§ïNßÛ°ÑõéìfÄºù¹L¿iE±CÚÐ¦U. |
| --- | Minor | ÙËä-Õhpô§¦?Á¾ÍrÙp>nN×¶ýv÷qQMØ>Ë1æju<å >C*XóØ±g/ö­¥äí©üs |
| --- | Minor | ^i%)]~ðÌj¶ <ü¯<ãü¸0uqoÀ»®½{ïvi·ÀÂøÛø/É¡äÜÄ.´à³ôMÆP¸}(¦yÚ¢RôZ¾Oâ\Êj!uZsi0?ê;Í¥OóþõC÷î¥úNfñ¹Ó­×ú{×ÙÐD23¼åà1ÒGR<\ÃnT^Êò¹ÔheÄs?1õ½Ñ;.éOëï¼ÂÊpÉ\ìÍ¬ 9Ê#RoèÝ	SÇõÌg:ëÛ.µJ[m«Ú|ãÃLk c×CZH\¸Áov×±ZJË°6Ú=BD¤dé |
| --- | Minor | =)CQ]âs º¡÷eáÙÆÆÍUXÚÒµó |
| --- | Minor | {ÑºJ®S 6 ÆW·u&N6Å |
| --- | Minor | · +»3*;µ6òÇUÄÍ¶AõÝpËùºh¡ ùµu/<Lôoæ M·Ð=9ËXï;tpacip¿«·V[9Wâ)gÈÏv¸¸ÿ©XMÁ«T(óöZ3pIñ¡°Nü |
| --- | Minor | ÉvÐ}Móô½hð>t)haOIjfÔà>0£Üõ-. ëË. c.1_î)iÔí¢i}¥oé ãS¹TLm`3}¥Sa¨?[6tÙbÃ÷ c. oÌäTðO½ÞJÿ´ÊFÝð¡xLèÓsÙ)þN¸/X{«¯$äåÉh´Ý¿ß9NM"0m¯T6¿«ÖKåÝ9´UdI|[«ÅQ±Îíë¾´SÀ1KkôQ°~`}[æêæ»ÉZ¨ö^q-ûká+®E¯¸Vàv­.â³FÐýLë/_æa/Áa§Ç )e-(¯Ý¯«jègY)ÂBHÒ}t£½÷7¼Nº·ÅHAÿÍõô(ðz&P=ägÓmÙFÎ2jÏS²£¦ýÚÔµ¾©k9JQ»òRVo#aá×¢¦7ª~<£tZÑ­ïïÙn¸ÕIiåïÄ)»Ëª;3pç®inqCÕ]Üíã	n.ëô=*í°Õä°°`cíåÛö.ñs÷¾ù9ùC² endstream endobj 340 0 obj <</Filter/FlateDecode/Length 4145>> stream xÚÅ\Ks ÁeáCmú^ÄÎ¯/"\/' |
| --- | Minor | Ü. oæM"­Cú­Z»ºciO³¶ÄÓîn´?5nÔ=J½ò2ò¸yõMÆªO0ý[û§pZøpÃX¤æý+++½æÕ%ù6&k­¯Z Xaz£´eÔ¥ïD	Iq~pJ<?Mû©¿%«T<}_UÐè>ÿÄïÅkÿ9ëÊÛ¢æ |
| --- | Minor | }âÙ#bmÙúòÅøSîC|ðY&åÐ5)Ô£ÍÛÐ¥ØÆlÛ[ |
| --- | Minor | g#ðÓióÒé'ÀMÇ§³ÇÍVxúñDD·>8ñôß§ïNßÛ°ÑõéìfÄºù¹L¿iE±CÚÐ¦U.. |
| --- | Minor | Sentence exceeds complexity threshold, split for readability. Applying the split needs --strength moderate or higher. |
| --- | Minor | none (split proposal only; source not rewritten) |
| --- | Minor | none |
| --- | Minor | Check: NEEDS-LLM |
| --- | Minor | Flags:    not-assessed |
| --- | Minor | SENTENCE (Line 939, 835 words, 12 clauses)  [Script] |
| --- | Minor | ¯4,Gwiæú¼ |
| --- | Minor | òvwüß´Õnx|ÓÌµ6q¡LAi.¤ô2v#àh x±£5Kþ £éæ!¬ïy°äQ7Úë&P7í½ÞÐbkmlnéÔæâøù¸B%A(t:é!\ºJ¦OÒ®'ËÙ7p>:²éØÖôÅmmF:i¨ÖKkaW²hmr^xMhoË&Ml0U(eç7òä»æZ*0®½®ðjÎ zshg¸³8ö{êëþÈ3¢±YØÉ×M{ø¨?kBÐ<8ðÏUuÍë°çz«ªOªÎ¦3Yd.uÅEE[ÓyÑÁùp·ºâ ,%À&)ZsÜjRÛ<%BmËÔ¶èA·z_oâ/*Íf4ÜºSÇ´|D/f	NÞXÝ½7æáû8+¥OuqokCøpç?,ÆöÑ8ckëß-ÎC4ßðz1XEô%õ?üþÃY[»ÒEé¿ÌjùoçùÃâp­.¬©PqL6ØàòÂ MSüå.é*»²65Ì½nmÄ¤zý?ecôVs¯t´[D vuËKÞ¬¶tôF|9ò*" B·ïIÿ,ÞÂ *Úêe^Zùï¡ú8Õë¡y0¼5zt+µætv`~ê ²ÓgWZF# ücÖÃrb8LQL³¶Þi;'^nf	'6ðµHðùe³Ø¦7pÇvÄQ®±¶Õü¤-9·ÙqÇE ºä6Ð2W,ÚÀ!?¼BJ~¨FÂÙ÷÷5î§¡Ñ6Î³0nê±jÈ±iÊØ¨¯Hä%º¨yy¡áõn´NDØ¢Å´«yóª½QñÔe"?H[~íåH~öÇü4«¬bDÝDj¦¦F);iséÚ5/{%År4QÕä@y*U¨<iËöý´Ä`BïÐ_j¤ØÀ¥ÔSK¥ñ­gv)l@Ä¤éÃ°0«8E¶Í ÁÅM¡¸(ÁÁ3R§tívhÐ=üERP<F;S" cáâUÜººýª1PÐÜÅÜÈ ¨¥ÔÑÑjù³bû=S$ÿZLq|ù÷ V\Ý Â7÷âZ: »Éß#{#cñqEÅ5õ÷,8ÿ{&0ÀüþIÿªk¥QlJ`k<<®ÉêWVü6zØ<Z^d`:ä©fJPÊ2+O¶³5¥¥fç78h.­,'õôÀhÃâb£¥¶&¥gôµÛî2H²ÀÌ§äu{ú](}{öNâ4í,ß_MÀÀ´¾KÃhâo1ú¥ |
| --- | Minor | ó éS3_J;÷iRÌóNSÛ |
| --- | Minor | N	 «k&J9ÎÛéªd®¸&åæÄ	ÑîüOëu>ô¬1½dy«ÑÎ^j ÐèçÑ{fæS§KWYdqÚ¹c|ZÚYQ6E£F/)þÞFfèLPIÞÅ¯Ú¬£ýN»ÚêMT |
| --- | Minor | (8ä¥Cè[9l{rÌpQÃfðô vâ´5§Ù¾dÊJs Ði\l|dj¡/çEu¼9'X)@Ð»x]¢Õ®-íàï0HÑ6Äáfé¬¿Ó0Þ¹G|m|íþ²lGe²®±ÜêÖÖ$£*¨]É2zzãÒ{Tt·î¹à²ö^;|iÒjgÒf³h÷YV°åìÌ8w3ÌýÖÁ5P!â~r[¸ mðÐïGbméacO`Ô¹^»s(ï*÷ÕkÜÑMÃ6ÚË=§k&ÃÏ·- 2lÔËµ ¹^¡Ù?eÃWuh_®&Ç ú¸ì¼à2ÐÕaA«ØÅjRu¦ÜÞ(-;TÏxâ<»ì,Ë!"ò%wKì_1v/Ë]ÏôàMSû¸ÚØÊ-xå |
| --- | Minor | ie@?xÞsP)Yt)ev¹eÞ\?áãk k\íÑ­2æcIH.)»ÿÝµ¸DCuÊ@2À¬¬¤íýZe§¾)ßV;Eö¶*·k¥^ä¿¢Vj«¼«®ÉlÜ¯¦9êæ0Ì°óÓÞï*Ë%_20;ÏT[­®2 |
| --- | Minor | ¥G:ÛèÚ[ô6/ËÜYÐíøSªÊ6(;Qáöå´)¿Y >ìG¼¡ª£Ï#Ã8@82?²Ä+<dÖ-ìè+®ÙUFpÌ9 æsf|q) ëÚ·×÷ßéÛfèiÊÇØ¡Iõ<ïDéOIÖå³ÆZàÕÒ^Ìå8Í3«>¯]§ÐËã¯} ª´¾ÆZQ<·ÞÂ£µ`ËìôÎE=4ýâÄÇQ/»ÞFrÚ¯GÖm:Ç½CØ¡Üm±&W¬ì³yÅ¬C7§IÑP\äíf5ÏO^?5ÖpØÿk5­Ëµ_xb»&BÉ`= åaE7Ñ×I©§ßìXu"ôÊÚpn0­GV¸ |3X8pòt{ |h~9m@hx~óUV/+ê'gÃ"õR(±&þÃf½û>ë ·­cPèR¶ ÞF¤ÜI/¼mk/2ïÛßËJH0V8Vâe=ódÓ³]á\ÓO'p¯»2ìe½q/	s¹oåÏÁÜÙë¢ô­UdãwÃ·¼zÃü®²¹]Ð<xÃ ?æQ©ògÊ5¿èµ(÷Ýj¿æ<¼S |
| --- | Minor | «.qè¼ |
| --- | Minor | B)·]þHé2i7v|­^ûtßD«ý_Å:Ø-Æv×¯Á4Ï7ªzÈrCtÕÅÞ^«Ó LÝ£Á5Ö¯îÌòòÎn-\z(4\L­y9×¯(·æGjyT©jÛOÖLz±°2xÊ­@¦a@ÁÛöô°ÊÒe¼CWÚ¤&?mühï»Ì¼¨GÄÃèÑÅíðò	«R]g-\µ×å[`×T%vxo~ÓHÔûp:ø`ÍÍ_CêAù	Ûj&¸eÞ ÎugR¹Éãký/eHWiÄÃlcëÉÛìNßæÉ¥DôÜÏv¹Ä+½ó¢¾ìÚê[B<Ôà¦s9âÜ~ãS»©R¼»ïûäØíçÐÂ©|3I² ó=@iÍºgoq¨ïÃêÂÿåþRD^þ¢C¿Ì¾Cè~g7µyiv¦úÃÖêÚ#å£»G%¿ü+ZFß^ÔÛÉ#cÝnê\öY&Ñ/ÿðâµSX%Ä01c¿ ÓH|ù¦üÔ {tþU%ú~Õ"É@!9ÿ6EnßDÏÛQ×yÁjÛ¡M¾ÊäHSFè]¡+(Ú|ºo<ÔCÂHeìàÅ] Y{$ ö+»iÕ'¯_ú¨ËovA8\×ß9*EÌ.ôg¾â6íÃêî÷ ì²RZæ«0o	Ræ/çr«_»(ü!#½GqÀòFÓQ¾áyæc¯rcæõô3Ô7]Öi2S2!++x,x2#IÐêLÑ«­:ú*æÛãååj$RÉY@:(?3þ¬?äGÎÐÓ²~Qä?!`¸§ÈýÇM;4â6X£ûñ¿Óæ}ÿ_ÁK¦iëcB®Nä§Ùn~Þw«ºÞ³JÔ\úQ2âïNl¤!A*÷®sD ïDûÿªH endstream endobj 347 0 obj <</Filter/FlateDecode/Length 4826>> stream xÚåËl7qÏWôi®ÐØ.?¡3 Aâî,nßÎ !!Á¯§ü(»lîIf ù å°×|`«ÖÛ·ØOâ ;ä[}ã,yKåp8#\êz¼FÚ pà²[.K%lx*_qPç¼;¯[vZÓÚ*ï£#®L=âU=PTPÖÉËti:¶áØælÝhÆÅ	(/õzh©4O/?×­û~ßrEÇÍ Î½O ûêc&Ó#»tà_®b:Ä¸yz4BÄ}DP{`« ÂPèôeð»Ü÷à ¬òqy§*ÏxTà' ¦Óµ |
| --- | Minor | (g"ü¥Å@Bå»·> >!gïz÷JÂùw®2#nÚj&¨¬ìÚ. |
| --- | Minor | ¯4. Gwiæú¼ |
| --- | Minor | òvwüß´Õnx|ÓÌµ6q¡LAi.¤ô2v#àh x±£5Kþ £éæ!¬ïy°äQ7Úë&P7í½ÞÐbkmlnéÔæâøù¸B%A(t:é!\ºJ¦OÒ®'ËÙ7p>:²éØÖôÅmmF:i¨ÖKkaW²hmr^xMhoË&Ml0U(eç7òä»æZ*0®½®ðjÎ zshg¸³8ö{êëþÈ3¢±YØÉ×M{ø¨?kBÐ<8ðÏUuÍë°çz«ªOªÎ¦3Yd.uÅEE[ÓyÑÁùp·ºâ . %À&)ZsÜjRÛ<%BmËÔ¶èA·z_oâ/*Íf4ÜºSÇ´|D/f	NÞXÝ½7æáû8+¥OuqokCøpç?. ÆöÑ8ckëß-ÎC4ßðz1XEô%õ?üþÃY[»ÒEé¿ÌjùoçùÃâp­.¬©PqL6ØàòÂ MSüå.é*»²65Ì½nmÄ¤zý?ecôVs¯t´[D vuËKÞ¬¶tôF|9ò*" B·ïIÿ. ÞÂ *Úêe^Zùï¡ú8Õë¡y0¼5zt+µætv`~ê ²ÓgWZF# ücÖÃrb8LQL³¶Þi;'^nf	'6ðµHðùe³Ø¦7pÇvÄQ®±¶Õü¤-9·ÙqÇE ºä6Ð2W. ÚÀ!?¼BJ~¨FÂÙ÷÷5î§¡Ñ6Î³0nê±jÈ±iÊØ¨¯Hä%º¨yy¡áõn´NDØ¢Å´«yóª½QñÔe"?H[~íåH~öÇü4«¬bDÝDj¦¦F);iséÚ5/{%År4QÕä@y*U¨<iËöý´Ä`BïÐ_j¤ØÀ¥ÔSK¥ñ­gv)l@Ä¤éÃ°0«8E¶Í ÁÅM¡¸(ÁÁ3R§tívhÐ=üERP<F;S" cáâUÜººýª1PÐÜÅÜÈ ¨¥ÔÑÑjù³bû=S$ÿZLq|ù÷ V\Ý Â7÷âZ: »Éß#{#cñqEÅ5õ÷. 8ÿ{&0ÀüþIÿªk¥QlJ`k<<®ÉêWVü6zØ<Z^d`:ä©fJPÊ2+O¶³5¥¥fç78h.­. 'õôÀhÃâb£¥¶&¥gôµÛî2H²ÀÌ§äu{ú](}{öNâ4í. ß_MÀÀ´¾KÃhâo1ú¥ |
| --- | Minor | ó éS3_J;÷iRÌóNSÛ |
| --- | Minor | N	 «k&J9ÎÛéªd®¸&åæÄ	ÑîüOëu>ô¬1½dy«ÑÎ^j ÐèçÑ{fæS§KWYdqÚ¹c|ZÚYQ6E£F/)þÞFfèLPIÞÅ¯Ú¬£ýN»ÚêMT |
| --- | Minor | (8ä¥Cè[9l{rÌpQÃfðô vâ´5§Ù¾dÊJs Ði\l|dj¡/çEu¼9'X)@Ð»x]¢Õ®-íàï0HÑ6Äáfé¬¿Ó0Þ¹G|m|íþ²lGe²®±ÜêÖÖ$£*¨]É2zzãÒ{Tt·î¹à²ö^;|iÒjgÒf³h÷YV°åìÌ8w3ÌýÖÁ5P!â~r[¸ mðÐïGbméacO`Ô¹^»s(ï*÷ÕkÜÑMÃ6ÚË=§k&ÃÏ·- 2lÔËµ ¹^¡Ù?eÃWuh_®&Ç ú¸ì¼à2ÐÕaA«ØÅjRu¦ÜÞ(-;TÏxâ<»ì. Ë!"ò%wKì_1v/Ë]ÏôàMSû¸ÚØÊ-xå |
| --- | Minor | ie@?xÞsP)Yt)ev¹eÞ\?áãk k\íÑ­2æcIH.)»ÿÝµ¸DCuÊ@2À¬¬¤íýZe§¾)ßV;Eö¶*·k¥^ä¿¢Vj«¼«®ÉlÜ¯¦9êæ0Ì°óÓÞï*Ë%_20;ÏT[­®2 |
| --- | Minor | ¥G:ÛèÚ[ô6/ËÜYÐíøSªÊ6(;Qáöå´)¿Y >ìG¼¡ª£Ï#Ã8@82?²Ä+<dÖ-ìè+®ÙUFpÌ9 æsf|q) ëÚ·×÷ßéÛfèiÊÇØ¡Iõ<ïDéOIÖå³ÆZàÕÒ^Ìå8Í3«>¯]§ÐËã¯} ª´¾ÆZQ<·ÞÂ£µ`ËìôÎE=4ýâÄÇQ/»ÞFrÚ¯GÖm:Ç½CØ¡Üm±&W¬ì³yÅ¬C7§IÑP\äíf5ÏO^?5ÖpØÿk5­Ëµ_xb»&BÉ`= åaE7Ñ×I©§ßìXu"ôÊÚpn0­GV¸ |3X8pòt{ |h~9m@hx~óUV/+ê'gÃ"õR(±&þÃf½û>ë ·­cPèR¶ ÞF¤ÜI/¼mk/2ïÛßËJH0V8Vâe=ódÓ³]á\ÓO'p¯»2ìe½q/	s¹oåÏÁÜÙë¢ô­UdãwÃ·¼zÃü®²¹]Ð<xÃ ?æQ©ògÊ5¿èµ(÷Ýj¿æ<¼S |
| --- | Minor | «.qè¼ |
| --- | Minor | B)·]þHé2i7v|­^ûtßD«ý_Å:Ø-Æv×¯Á4Ï7ªzÈrCtÕÅÞ^«Ó LÝ£Á5Ö¯îÌòòÎn-\z(4\L­y9×¯(·æGjyT©jÛOÖLz±°2xÊ­@¦a@ÁÛöô°ÊÒe¼CWÚ¤&?mühï»Ì¼¨GÄÃèÑÅíðò	«R]g-\µ×å[`×T%vxo~ÓHÔûp:ø`ÍÍ_CêAù	Ûj&¸eÞ ÎugR¹Éãký/eHWiÄÃlcëÉÛìNßæÉ¥DôÜÏv¹Ä+½ó¢¾ìÚê[B<Ôà¦s9âÜ~ãS»©R¼»ïûäØíçÐÂ©|3I² ó=@iÍºgoq¨ïÃêÂÿåþRD^þ¢C¿Ì¾Cè~g7µyiv¦úÃÖêÚ#å£»G%¿ü+ZFß^ÔÛÉ#cÝnê\öY&Ñ/ÿðâµSX%Ä01c¿ ÓH|ù¦üÔ {tþU%ú~Õ"É@!9ÿ6EnßDÏÛQ×yÁjÛ¡M¾ÊäHSFè]¡+(Ú|ºo<ÔCÂHeìàÅ] Y{$ ö+»iÕ'¯_ú¨ËovA8\×ß9*EÌ.ôg¾â6íÃêî÷ ì²RZæ«0o	Ræ/çr«_»(ü!#½GqÀòFÓQ¾áyæc¯rcæõô3Ô7]Öi2S2!++x. x2#IÐêLÑ«­:ú*æÛãååj$RÉY@:(?3þ¬?äGÎÐÓ²~Qä?!`¸§ÈýÇM;4â6X£ûñ¿Óæ}ÿ_ÁK¦iëcB®Nä§Ùn~Þw«ºÞ³JÔ\úQ2âïNl¤!A*÷®sD ïDûÿªH endstream endobj 347 0 obj <</Filter/FlateDecode/Length 4826>> stream xÚåËl7qÏWôi®ÐØ.?¡3 Aâî. nßÎ !!Á¯§ü(»lîIf ù å°×|`«ÖÛ·ØOâ ;ä[}ã. yKåp8#\êz¼FÚ pà²[.K%lx*_qPç¼;¯[vZÓÚ*ï£#®L=âU=PTPÖÉËti:¶áØælÝhÆÅ	(/õzh©4O/?×­û~ßrEÇÍ Î½O ûêc&Ó#»tà_®b:Ä¸yz4BÄ}DP{`« ÂPèôeð»Ü÷à ¬òqy§*ÏxTà' ¦Óµ |
| --- | Minor | (g"ü¥Å@Bå»·> >!gïz÷JÂùw®2#nÚj&¨¬ìÚ.. |
| --- | Minor | Sentence exceeds complexity threshold, split for readability. Applying the split needs --strength moderate or higher. |
| --- | Minor | none (split proposal only; source not rewritten) |
| --- | Minor | none |
| --- | Minor | Check: NEEDS-LLM |
| --- | Minor | Flags:    not-assessed |
| --- | Minor | SENTENCE (Line 939, 933 words, 11 clauses)  [Script] |
| --- | Minor | o£`>lEárXþ1zÎ3;ÕÓ]ZTÝ£ªJCÅ'fT&ÆëÜeÈ=ó÷´ÕXXã2S¬mtòÅ×a `Q<â_JyÕ£ wÙDFdFa Ü!iòGÒvgÆPµíg'E¾ 6í´#¦åÅ "«6a3Üª!Fx[.çA|Ø¡ß´mAâtÊiÂ |
| --- | Minor | \è4}­2­ ybÞöl6/¢_6Í"pê²ÄÁÐ@tzqíà60Á´Ñ |
| --- | Minor | HÐîB[Mãõ~K»HLÃªGyÃ8®rÆÀAP¨9xýK±9WGV ¦Vb}$}¤EpÔGô¡»¬ü¥F±ÐE äÖ¤WqåñJ5\²Ýµz=üÁk+[o®d°ý Ä¢i¡ùÒåêÉ=¡ª>/hL°yaTÁÄëÊÔÐ1ýPúýöÃþ|°	@}¶ôr¿^Ð¬ô[Ðíåë!¦Uu&±w{Ü.>¿âáû[a6H°à8÷`ÄkD/A6+]é¢-ÅV[}æZ&Ð¾õã jr¶g.u°n¿ÂBÝá:å _(þPt'àè »·oõÙÛªe×ûvîÕ¦'BøËbãø |
| --- | Minor | [ l[÷O"»¹/Ê¡.MÍ£ K~ÁLaLª'B	9fgÖAú]B¤PùQ5H-\ØJH¢|ÕcObÈîÓjÇ$½p³ÆqAüóÎªi[¦OQ4þçÌdd«É3yµ:ç±ýÕ çÿ~Çuawæ¸7RÌ Ø¿U1Ý7Òÿ/QÛ¦²ëxÓSKxdíÕÉPâ0c±öñ¨ZH L&ºlVeSêWMV»®w¥ ³Wr©øs»!Z4örLEVYV}dIõ`ÅH°Ä°¾J/H?lÆ[CÿåZ*¥Òmhßta7o½n\7j³þù¤HÒ·Íäq |
| --- | Minor | "3­üÖM¼ *sQo·®¬ã^ÅOf4Î±Ñ¾³àF |
| --- | Minor | }±A |
| --- | Minor | ]²{¯êÜ´Jlà¤Væ},éü&¤w·V§ |
| --- | Minor | £ÓdQn(%|à=¿"»îËùqråÉáSx§#Ó®ÒáSÒ&ÄËsÌ¿ýÝyYkªÇÎñP 7~²/¹g­ h[R^G«[¥ÿÏ#°tØÿXÜpwß¦'(SÕ |
| --- | Minor | ÷]BA±ÎùM«Ñ>Ç¬ì@¦§v?× ¿¸=-ÐÊ#¨~4Ï+£F6©¤'1Xk>x@huÞÖy¿TJdah<#z)1À¡ÏgÝÓ73 |øfÂÊlÖ7ß;mrç*ïÃïg@u	·fßõ"|÷aÇ`¾²Am^m úÔC)Ò¡j§ÿrÅÇ |
| --- | Minor | » IÝÉ£ÖcF? N»÷ÅU¥	J÷¥ú-¿L¾Wæãê` |
| --- | Minor | /ñÕ]ÿ¾XÓÂ?_Ä77ßÜ­íÿ7ËL/@K9TçÿFÃâF |
| --- | Minor | ÷­%¢æÁ»l=üüñÜ/ñÍ4%=ÜçJÙ7Áò(,ÅÂ,ý}(»	¯$éÛÿBjÝÃye0âmèMü_ÚÔ£9»]L±Í¢ß#»hªÍ%Æ´Ü·ÉJ3¥N»·eáÐ{¿âf_ºóç¹§WD'­v*)^uFqØ@×@Þë" XóðÍr^ÑËõÒyÕ­+}Ä+^ûÌîHØ)¼©)AT¸ÞÇr¯¾´t½VÖå7C?ÒØM©{eh'¨ú§&¼	JÜK t`÷«pJ6+«òà-2Z³+¶/dÈé?fJÿçÃrKï±§Ö1£ú®ë2m±/pª­×¾b%rº~­¶§¡_ºýUã`u¼IïnÇ;WéÄU³¡¨¾ïWF@);E"oV«õÚÑ]í?Av,¿»7ã?¥BÔ£ÎÍ÷uÙ]©e·æ3JÓyÏó<3}»Ë¢}¥@Õ$ÎaÊýRþµËa0¼kJÊu»1gþü×P`)	-rú åaÀ=	þ0WìÎ´?r¿v~}GðÖ¹4í­mWPïlÃóè·HõýåìZÃf;´k*h7Ï}²4éöªÈñkÑ |
| --- | Minor | *¨çÝgî®.Î!dD#y¾9+îÃù¯9Q[§SP=|ÍRäØãØWºÆÀ÷L±·Tw !ÃêêµªÙOÉÑi¥\U\Jl<£Ô_ïåh&Ò#|LDÿÕAS»¥Ïûòåõe?K2 â÷Oq´²Ëµ`í*©#GTÕâDñBÏDøÆ%c<ª{O"ÏT­C²Ù'å¬Emi^îzcd4 vFÆ¬÷Ýøß),RÍ[ÔçYíÎBä³ûPÁÏ÷Qú¸ô¥×ükÝûÛ|Ê1YÃp«"À1_Ä«ÍÉ*ÚâeÝJaÅsÆÇâ©¤iWM%VÈÒérE`+} |
| --- | Minor | "¥G7mW05%RRK­d²º¨în«Ì^ëàæTRsM"ç.ðRòõë¥ÂoÓØ·Â³·hÂxÄÃ8jÃÉÍK.W>'TNCñxSÚýÞUÚWY GNm óè*¦Ê×ÐË7YL5å´N2ò{=¥±½ |
| --- | Minor | ,\ÛúAÏkÄO CÌÏu¢ü1	[Þ½épª=Ã!Ï{b5ÿÏsF$¥:£¯lÇj¸â9ª×ó§=D~Vsê¹Çñ|´Ëtª4n×§1>¦U,EÖp_¥^6-hFú¼Ï'Éó¶Yysak¯]ëÙÏó´èÑòJW5p®ÇsÆ³g4º¼©¶y-TñÔKóîÎ ôUì>÷¬]¹f.« |
| --- | Minor | ±ÒHÌ¾ ¯+\WbK)Ü£ôz[t¼>	×0íÐ^YZþ²#z~ÓôÔ¬^ï¯þðÕ¸d,ÿY±ÚÄÜûK¿?Bwõ£ÎEë®>°SõÌ¸«µ{î,Çþy§ÒKûþ|¹¬ÖÕüÚtU	@K¨ãuäÌ\4ÕñÁ×]Ìzõ³ôÐi£Ü¶Áu®=Û éÒHãå^Æþàm 	d÷nxø³OYeÌ§R%^o|õÜ¼ÓBà7PsçÑcU)TûIæ÷Jã¨9iÎ?\ÈåÑãvô |
| --- | Minor | ÕxÈ]ba`ÂÇË·ÕFøGëýÇz¤7íu·²ÐºWÂ½kLVµì¤ª7 |
| --- | Minor | DÙMÖ§Fþ¦a:¹Ü7¸Í^Ëwöxãì%³Rwã¥Ò[BÿY+»Ö{ßmÚðÒÛ|Íè£*¯¡\¸Ô±äZâÍÎRDÍ«ÞHªÙåæ @SÜ.ÈWöòL\c'E)¯#ÇêÁ¿T_\¥/ÞKÖiÛ£ðÕDdxJ*c:2 Åa&ÏÍc«e`¯â¡°Y(vñQ#Íê0¢ÀýºÆ Ý×Ê 65d¢õn*©W*¦«cKu´* A[hhA)|º12Æ;cyØ4¤aÎf°ò(Ì¾2ä(L{Î¬ ÆçÉõ/µ"¡wãæºWÞíKÔ	þT)Ü?GòüYT×it11f¡¦D+ÏCòvïßÚSVN8¯½ràoUïÑÆ¤rvuÐÎ) ¹îI÷Ð¡ó¾¾º\¬ÜE´¹JËüªÍÍëxGa.¼C¡jG^Gz>½(ñwM°m}i¤R1_ÊMHo=jaC¥½½¹§ÒCà±üõWÿ[¼& endstream endobj 353 0 obj <</Filter/FlateDecode/Length 5317>> stream xÚå]Kl9 |
| --- | Minor | +z3Ò¡: æªÕ]§<çóg;óòÏù"Â?ùbáÅJøøßË¿g	?¿{ùõç_üV¾oõòùíE¢8´óæÔ!røòùþÇ«Æñ 2þ}?~¼J!oáwxá7¾	¡e,þeàíõÖZð}þ&D~§os©ZbiWÞ¾	OµÊÇ6U)·×?þ}è½âðÂçbÿ/^F£ÄÆÃ­|Öá~×@ïxËoU¯ÔW-ÂßòKî}.kë}-oïiVRùÔÃ8¦{øVbi!¬¶·\6ÍPAômlÁªòæ[ßð^kè}±µT×ç·ÙÏ])û)-`}Xò<Væª¹ª¦jî0 QçZþúm)}1< ¥Ôß®ÓÖ(Ì¶Ìá¤SÔÖõÛ*ûéO¡ëß®G&ÝÚP¯iîKÉ¾ = \-gü«1i^!¯Kz¶¿#L®lµ£ÌäZ±+ØC£þ+¾V÷¡I5©CAðÄ#üRÉÝº_òp(¿f·¢üÅÝd3Ê¨ ûØyê?ô4Cý{ÙÕupêðÖc? |
| --- | Minor | o£`>lEárXþ1zÎ3;ÕÓ]ZTÝ£ªJCÅ'fT&ÆëÜeÈ=ó÷´ÕXXã2S¬mtòÅ×a `Q<â_JyÕ£ wÙDFdFa Ü!iòGÒvgÆPµíg'E¾ 6í´#¦åÅ "«6a3Üª!Fx[.çA|Ø¡ß´mAâtÊiÂ |
| --- | Minor | \è4}­2­ ybÞöl6/¢_6Í"pê²ÄÁÐ@tzqíà60Á´Ñ |
| --- | Minor | HÐîB[Mãõ~K»HLÃªGyÃ8®rÆÀAP¨9xýK±9WGV ¦Vb}$}¤EpÔGô¡»¬ü¥F±ÐE äÖ¤WqåñJ5\²Ýµz=üÁk+[o®d°ý Ä¢i¡ùÒåêÉ=¡ª>/hL°yaTÁÄëÊÔÐ1ýPúýöÃþ|°	@}¶ôr¿^Ð¬ô[Ðíåë!¦Uu&±w{Ü.>¿âáû[a6H°à8÷`ÄkD/A6+]é¢-ÅV[}æZ&Ð¾õã jr¶g.u°n¿ÂBÝá:å _(þPt'àè »·oõÙÛªe×ûvîÕ¦'BøËbãø |
| --- | Minor | [ l[÷O"»¹/Ê¡.MÍ£ K~ÁLaLª'B	9fgÖAú]B¤PùQ5H-\ØJH¢|ÕcObÈîÓjÇ$½p³ÆqAüóÎªi[¦OQ4þçÌdd«É3yµ:ç±ýÕ çÿ~Çuawæ¸7RÌ Ø¿U1Ý7Òÿ/QÛ¦²ëxÓSKxdíÕÉPâ0c±öñ¨ZH L&ºlVeSêWMV»®w¥ ³Wr©øs»!Z4örLEVYV}dIõ`ÅH°Ä°¾J/H?lÆ[CÿåZ*¥Òmhßta7o½n\7j³þù¤HÒ·Íäq |
| --- | Minor | "3­üÖM¼ *sQo·®¬ã^ÅOf4Î±Ñ¾³àF |
| --- | Minor | }±A |
| --- | Minor | ]²{¯êÜ´Jlà¤Væ}. éü&¤w·V§ |
| --- | Minor | £ÓdQn(%|à=¿"»îËùqråÉáSx§#Ó®ÒáSÒ&ÄËsÌ¿ýÝyYkªÇÎñP 7~²/¹g­ h[R^G«[¥ÿÏ#°tØÿXÜpwß¦'(SÕ |
| --- | Minor | ÷]BA±ÎùM«Ñ>Ç¬ì@¦§v?× ¿¸=-ÐÊ#¨~4Ï+£F6©¤'1Xk>x@huÞÖy¿TJdah<#z)1À¡ÏgÝÓ73 |øfÂÊlÖ7ß;mrç*ïÃïg@u	·fßõ"|÷aÇ`¾²Am^m úÔC)Ò¡j§ÿrÅÇ |
| --- | Minor | » IÝÉ£ÖcF? N»÷ÅU¥	J÷¥ú-¿L¾Wæãê` |
| --- | Minor | /ñÕ]ÿ¾XÓÂ?_Ä77ßÜ­íÿ7ËL/@K9TçÿFÃâF |
| --- | Minor | ÷­%¢æÁ»l=üüñÜ/ñÍ4%=ÜçJÙ7Áò(. ÅÂ. ý}(»	¯$éÛÿBjÝÃye0âmèMü_ÚÔ£9»]L±Í¢ß#»hªÍ%Æ´Ü·ÉJ3¥N»·eáÐ{¿âf_ºóç¹§WD'­v*)^uFqØ@×@Þë" XóðÍr^ÑËõÒyÕ­+}Ä+^ûÌîHØ)¼©)AT¸ÞÇr¯¾´t½VÖå7C?ÒØM©{eh'¨ú§&¼	JÜK t`÷«pJ6+«òà-2Z³+¶/dÈé?fJÿçÃrKï±§Ö1£ú®ë2m±/pª­×¾b%rº~­¶§¡_ºýUã`u¼IïnÇ;WéÄU³¡¨¾ïWF@);E"oV«õÚÑ]í?Av. ¿»7ã?¥BÔ£ÎÍ÷uÙ]©e·æ3JÓyÏó<3}»Ë¢}¥@Õ$ÎaÊýRþµËa0¼kJÊu»1gþü×P`)	-rú åaÀ=	þ0WìÎ´?r¿v~}GðÖ¹4í­mWPïlÃóè·HõýåìZÃf;´k*h7Ï}²4éöªÈñkÑ |
| --- | Minor | *¨çÝgî®.Î!dD#y¾9+îÃù¯9Q[§SP=|ÍRäØãØWºÆÀ÷L±·Tw !ÃêêµªÙOÉÑi¥\U\Jl<£Ô_ïåh&Ò#|LDÿÕAS»¥Ïûòåõe?K2 â÷Oq´²Ëµ`í*©#GTÕâDñBÏDøÆ%c<ª{O"ÏT­C²Ù'å¬Emi^îzcd4 vFÆ¬÷Ýøß). RÍ[ÔçYíÎBä³ûPÁÏ÷Qú¸ô¥×ükÝûÛ|Ê1YÃp«"À1_Ä«ÍÉ*ÚâeÝJaÅsÆÇâ©¤iWM%VÈÒérE`+} |
| --- | Minor | "¥G7mW05%RRK­d²º¨în«Ì^ëàæTRsM"ç.ðRòõë¥ÂoÓØ·Â³·hÂxÄÃ8jÃÉÍK.W>'TNCñxSÚýÞUÚWY GNm óè*¦Ê×ÐË7YL5å´N2ò{=¥±½ |
| --- | Minor | . \ÛúAÏkÄO CÌÏu¢ü1	[Þ½épª=Ã!Ï{b5ÿÏsF$¥:£¯lÇj¸â9ª×ó§=D~Vsê¹Çñ|´Ëtª4n×§1>¦U. EÖp_¥^6-hFú¼Ï'Éó¶Yysak¯]ëÙÏó´èÑòJW5p®ÇsÆ³g4º¼©¶y-TñÔKóîÎ ôUì>÷¬]¹f.« |
| --- | Minor | ±ÒHÌ¾ ¯+\WbK)Ü£ôz[t¼>	×0íÐ^YZþ²#z~ÓôÔ¬^ï¯þðÕ¸d. ÿY±ÚÄÜûK¿?Bwõ£ÎEë®>°SõÌ¸«µ{î. Çþy§ÒKûþ|¹¬ÖÕüÚtU	@K¨ãuäÌ\4ÕñÁ×]Ìzõ³ôÐi£Ü¶Áu®=Û éÒHãå^Æþàm 	d÷nxø³OYeÌ§R%^o|õÜ¼ÓBà7PsçÑcU)TûIæ÷Jã¨9iÎ?\ÈåÑãvô |
| --- | Minor | ÕxÈ]ba`ÂÇË·ÕFøGëýÇz¤7íu·²ÐºWÂ½kLVµì¤ª7 |
| --- | Minor | DÙMÖ§Fþ¦a:¹Ü7¸Í^Ëwöxãì%³Rwã¥Ò[BÿY+»Ö{ßmÚðÒÛ|Íè£*¯¡\¸Ô±äZâÍÎRDÍ«ÞHªÙåæ @SÜ.ÈWöòL\c'E)¯#ÇêÁ¿T_\¥/ÞKÖiÛ£ðÕDdxJ*c:2 Åa&ÏÍc«e`¯â¡°Y(vñQ#Íê0¢ÀýºÆ Ý×Ê 65d¢õn*©W*¦«cKu´* A[hhA)|º12Æ;cyØ4¤aÎf°ò(Ì¾2ä(L{Î¬ ÆçÉõ/µ"¡wãæºWÞíKÔ	þT)Ü?GòüYT×it11f¡¦D+ÏCòvïßÚSVN8¯½ràoUïÑÆ¤rvuÐÎ) ¹îI÷Ð¡ó¾¾º\¬ÜE´¹JËüªÍÍëxGa.¼C¡jG^Gz>½(ñwM°m}i¤R1_ÊMHo=jaC¥½½¹§ÒCà±üõWÿ[¼& endstream endobj 353 0 obj <</Filter/FlateDecode/Length 5317>> stream xÚå]Kl9 |
| --- | Minor | +z3Ò¡: æªÕ]§<çóg;óòÏù"Â?ùbáÅJøøßË¿g	?¿{ùõç_üV¾oõòùíE¢8´óæÔ!røòùþÇ«Æñ 2þ}?~¼J!oáwxá7¾	¡e. þeàíõÖZð}þ&D~§os©ZbiWÞ¾	OµÊÇ6U)·×?þ}è½âðÂçbÿ/^F£ÄÆÃ­|Öá~×@ïxËoU¯ÔW-ÂßòKî}.kë}-oïiVRùÔÃ8¦{øVbi!¬¶·\6ÍPAômlÁªòæ[ßð^kè}±µT×ç·ÙÏ])û)-`}Xò<Væª¹ª¦jî0 QçZþúm)}1< ¥Ôß®ÓÖ(Ì¶Ìá¤SÔÖõÛ*ûéO¡ëß®G&ÝÚP¯iîKÉ¾ = \-gü«1i^!¯Kz¶¿#L®lµ£ÌäZ±+ØC£þ+¾V÷¡I5©CAðÄ#üRÉÝº_òp(¿f·¢üÅÝd3Ê¨ ûØyê?ô4Cý{ÙÕupêðÖc?. |
| --- | Minor | Sentence exceeds complexity threshold, split for readability. Applying the split needs --strength moderate or higher. |
| --- | Minor | none (split proposal only; source not rewritten) |
| --- | Minor | none |
| --- | Minor | Check: NEEDS-LLM |
| --- | Minor | Flags:    not-assessed |
| --- | Minor | SENTENCE (Line 939, 1474 words, 23 clauses)  [Script] |
| --- | Minor | ©IÔ â@á$Ië¯ìXùIlà¸Ñê øVmÏ]¥'Qy(¦özö öZ¾<yè±¶+ßh¹^)Í!ÁjÓ$µ±YT\h­-AVLÔÏ,¹?¤6£ iý U¹Ô©Ú ©ÜðÔ'5¥_×³íÍa |
| --- | Minor | ¡\úPLÕUYkwsuØ­²<P:C%wË{Q`ÂXl |
| --- | Minor | (JÓ5¢£*>Ï2@ëæ@ÅM¡BVe&ß+`´)+óéa¸ÃZ |
| --- | Minor | §äò# ­¶IÊþ¢\Ú´7¶ÁTì»ºµ |
| --- | Minor | ã×¸2øxÚäbãAßm­°[?Î::>Ì¸¶¥Ô/7cïÏ/·ºÝhÐ¶Q×Ó±×±ºûDcÇú ) ÔF¿µ)l}Ï#á§ )Éü¶aMBA_^/ã¢[ mj9·Ëº´r+Êï­)öÛè]îÚT´ |
| --- | Minor | ¢ÜNF[µÇPÊ´K'[Â{ú¤EAQÇqÑOvh8D.ÎéSÄËU`a=?m&©=4tEï	ûÞ2öEiìÐLbé=÷HN,=¡ã1£R§ý*fCÄwËkS³é;gAw¸wÿ~dXËFC:n]iíø	ì^A%@NºC¹vÊºk,ðêÚJ§myï[ç0xÝ¦s§rýàÂP¹ÚmÍ,Ö5"IÀdé|åGßW]Ó73òºbÝ¡\45¿þ¸Ú%Ñ¾UÚÏx)uº¦·bn2ñ »¡ÃÚ©.õ+ªï"ÆÕ2WrPëWã^ër¹Ç7éË=ViÄtÑa©Ä ¢ósoÛÑ0,ÊBS¡vå&`åRAe |
| --- | Minor | §±Á8@5â%¹x6ª©Å`ª¯¡æ~ª4LnÙø`8Âk*¥e²º^+©"Ý+|Q³­WÆKf9ÞÊÖIßÎÜÙ¡ |
| --- | Minor | ®â­-Ò h(©§a^Ç¸¯B;ÖbkÏ&¸"Éf¯n	vS·êf¿·êÛ\ÑKIÛSòmEE_k;ó¥rYL}ksÖJø4ïÄ5B}|¯´%±@EòÞ¬+OWÚ¯AÌú¶ÒQC²{yovÍ{ëíÕ¶åÃölð¯,£u+t iï#üZ4Õ¨:*¿Ù7h«îµ)9ÒCHïüI%{A$P­fÃ2w¦+R-½bäá½ªÈæ«¢?¿éÄ:b¸Ãx´Mí\&ñÝ¶I!tê5Mu4 ØY¶r{ RÿfÇª0.­&HÆzSUæhE¤AØqËW%Ò)EA.¾¿;w ôUÏlR`#©{K¾)¦wVöR;Ú.]Es´o±°4/èTõ·  ³äÕáÂ4·`n*ÚCkïõ\3Ùºµ+­»êÖS}	Ø¥iÝ^ß]@Áa ]ÙÚieÂ³£	«ÐbO:ÕÛ±>h;%æÊ)VßzõZ»7{ÆM¶åèB[[voh-I |
| --- | Minor | \X®×ºêÛ*SæÐe³¹å-î#S¶úX&Éu6zJRÚsÞÔß=ÅÞVKØÂ½ß |
| --- | Minor | ÎÍ´¹[µ9wã¥£"íl#¹íêõöáþÖóÐôR©*ÞÚ0!6Ð¾'¨MåôYªáº×ÏV)eºJAûÔnÉÈ°n´T¢+¢Àými-mñ¹EX?Ñöáv.±&óèÛQÕó'ÕiùsµÑl7¢®¾U¬myFÊ<[àÓfLë3IC{J2Âç²9ÞáHÞö^Ú,Pï§%Ióu®Ñí­	Ø©Tg®.¼ÂQV&¢Çé/í¢Ân¸Û[Á­ø.­ÊRu¢-§-º;32¥`åßàmjMÂÐAòÌBñ×ª@ðô@>ÚOzëë`Õ M}sâwÊ¹	¹c60WjD¦ç2RkÃvö^PÉ# -ú(É{g¬sÌÓ¬¥mÞ;¸6í¬µwI)Áw~k Vßx(Ñ ´uÕ×Ú+f_«­QOÓ½oî|E(0eÍ#ü\I$k·`«÷×WÀe¹«êð¸Öiêç'üfO¸ÚÐr:tªØê50òH¶¢³ô÷\ñÄQH?úrJ'´¬C³Úö¬¦ãµûöÌÎº+®ÓÞ§U»0jCcNµ¡Ñµ!ª#ªÒâæk*Cøæºb0Is×ü}Faïç!ivC3CÚ²²c¦»·e© Ì¼OË	ÛÒGòbÅ´C8 |
| --- | Minor | ·æ@íVÚÔâ\4Ê%ÃöÎiìkk¶È`@080a¹*¶J¡n}oBZàµ<Ði	«V*s´ÚÁê}±Ù®=ôíåQYmí'y ÌÈc§Ð"nvm0ÜÂãî4aeÍ*ÆhßÈKï©{ÛÑ·¡Üè{REYæáMåV²ÛºÜÛRLÌÞPvíG§úÛÃCR¼ÿ§Jyg¢Ç©E <àKAüÑB!×FFÓÁ3j£¢`®ÆJ÷ß¬%â3hªÌp²<·Õ$´»9qháÐ%÷VïhâPNaõ¥Ë¯HÄ¯1eÅ`?¯Ì£ô¢¤=7uúTåP~v-uY{mà´ÌLQñôÑøX råòënL5Þ7&Ã «1ÊÙ èÃ\îVRuDme<láXB¡5âUPï1T£\qÄCiYtú´ !ßªßµÆe7ã±rv.7ÚCÇµö;/|Iðc÷}ã9·è¹Í`æ<ç­¸©åánÉXSIÆ,ùµlÛ9ö;mÝ¼'Öu³°î§ªËT-õÄw<hÕR}hâéy]÷þ&íIvtÅºïVÜíÞYË2(FVq!ìc«ÝÓðè=Ó¾·fÞwd3Eu(â[0Ä!jMU¹Ãyx&Ù ÌS`DµË ³eµ6~­ÄÞ>EcÛ9ÞGQWeªbîÑá¤ð}Ø+.Zß92jwoå¸¼Ox£¼{/Ôú¹üÏò°ºæ9å;CáªùÝ¬= åx Ë`%Ïä	H»Pl±U¡¥$×V%ºÀ;bêªÍ^~LvÏ®|oÌË*¼Wú§Ö_â~G HÑÊ-ªFCÃ*ô F ÒªCe`>û(Àl¼«½/"ó¿´×÷'Ö'^ü8ä.ÜÈe¨¡ßÅHå)ÉaÜäÂÍoíx.g@¹¤ª½ÙAÇÜÏJôlÞH<*æG# Hy;XyLê-®¡LÍ½À)£<ÁY½)÷Døi)ùàX¥ºD §ûåå¶º.Ïjå¼V<µ.öê;[æ!µO.§/»)ãZAÖÔEXcºy |
| --- | Minor | %ÜÑ'ÕkKóV£Nr@6_>bfA¿©Øþ÷â)çÉ¥XÙÄÕÔèHµÞÝRVÈ[å­¦â æ#.P/é¸p®Ü;JE!É |
| --- | Minor | ¦Ou`mc¤ÉºØclô5ZHüdÌïº®üÊ4ÊÅXq+Æ®ÎË*ÂD13<þ³µñtxD¿õª1hN2@ |
| --- | Minor | ±[ù	§f3¹I¥tèÚÀ^UÍuÎ2á\´cÍB@tj?¥J´©xÄÙq¹|óÝ§hS³áúP"åhjdt3	NféUð$F£\y®»5EÎ åÛé¯czi\æl1Ò÷\gÞHshõ[¥sº°Ø%#¹ Ç3jÄHóÃm¦kô±mFyp]àPÁ7Ú-R` GPúóÐyJ¦¼îÔ¾õç|í.ÅW×;þÖÛ¾IKîg1ëbMÙë |
| --- | Minor | f2±YBs]ù±ÒÇL.^\Ë{ç*Tjµ*jÂJ?Y)ËÒÓaçv²b!bÖâé@OT¼¯Mì*ò{7üC©Ìâ1G²arv^Jìýp°	7èfmØE f;`{÷°bLï±Ã]çsçOÿf>w#À¬+åäá@<Ñ |
| --- | Minor | *XÁÎ¡*V¯I2åªÖÒß6¯OI£r£°5<¾ÒÐ/×i¥3ÁxQ8Ñ{ù]ß_J¸il~å=z ÊÜ"ì¹ÜBnm=~ª´§ÓÈíO	rÕ&³Íí5`µïè%Ñ¬RîE ú&YØúÚóáÜoú¡Ø¥B\Ý¹å4· r¢¿t³hjCày$Ââ~¨é Äå|wâ°SÅ¢Æu¯ñ÷vJÙ,Bðé6-],hÁehÖEÞ2¦vM.äç/ñÜé]Þ-Þ¦½LÎ	Ñ¦Ï]|Ì¯ó},'9»PÓ9§¬5ä ¥£}ß6Ë9QàÓaÚ9_¢dùÇ|Ô Xè©í3 ¥PI÷Þ "`OÎ¨L%«a(Á¯.§·BÊñæÉÿÖÆq xîª¢Áæ¨©OF¯æ+OLC¨Á+ÕïöV­C°/Ø<mýRöP)æiR;0xâóËì1)ªêUñá"Ü!ÀEB7xÉùÀx5 ¶ÆÄ9m·ìTå©Äè=ãV9²ÈåMRñ.IFaþÇLpù çz»®ÊO[òÓsÎ.=ìÚ2)Ì |
| --- | Minor | »Á¡é5^°hq¦6t9sÙÅùÔh¤I»wKæÁE³ÜÂEx4oyÛ[/	Î=AÉä¾TSËs?É¹áÖödHÅ@!Q¯¼ýÿîÒ?,O£<ï-¨Å.åk¶Æ®Ñ*Ò[ÜÒ[DìÓÓÆrQØëäÞÝ%õw¿Ó |
| --- | Minor | gü0éi|"_³wCV5¿(® ²w, È»,¡ôáybÃýGÄÆIæ¿ñ.Z\Æ±o{JÇ%èîyä |
| --- | Minor | ):1tûxÎl¯»tSVTz2Å?8Ü%©éWè§TY§VQI®»ÖáÉE'Xn ï3ão¬(¶,aÍÍV¾È·57Ø,g®éW=cÈ>#óØC@¶SnIìdÈlZìÿq{¸0K*ÞHy8gTÄ	VäQûÃÏþ"Egq endstream endobj 362 0 obj <</Filter/FlateDecode/Length 4847>> stream xÚ½\I¯#¹¾ûW¼j4CFp¨ßÁûdLÝÆs(ú |
| --- | Minor | `À}õ¯7· [Jê®rU\±|±åÛ?Þää7+ýáão_ÿ¾ûÿðÿÞ~÷ùí?þ[¾_õöùã |
| --- | Minor | @"<þ!røöùþ¿W!~þÖòýÿ>ÿ1>&ß¤8¼ðÂ¹øäIâÛEãáV¾<ø~)aîa²ð?|!¿Ï"|!0üoàý¯íLß¨+}Ê¿(ærï-lü%|Âql× Tø·¼~ZûçR÷wH3øöLüwü |
| --- | Minor | /pË£ðÍz/38eM;GÜ_<_8O!î.PHin!èÓ_(ÃL?L`Q¿ÁauøÞh(ä?@¡ôñmôý°^ßÊéºü%|ú EãU?^ºð±²< 6ÐG8SX:úÏÍdxHsI?¬9 ÄØ±lxÂ½Ñ^rtéæ¡Ýf¾áð÷­ÜêòçI·rAhÿ"ñì e!­*¿2ÆUÆ°2+ô-m)ý íßÂHHrÁ=¯` |
| --- | Minor | ¹`¤oÊqâsëWËl^W¹µU¸°µsùL×ÔôtÜbÌT¨{ì­ÑË{ ßÝéZ6· Ùd4£umÆÈy¬Zi«4>0Á[c¸¯¨â¿ãüU1VU¬èX5NÕY4-\@=eÓ<ðCUMâ÷ãN=z¥^f~#ÌÒhÐVa6	ãõ% ÖI|wç×ç«å,â  yFP9¨BE×D6+2¦w0×Þ¶p |
| --- | Minor | ­Ó«ÜfîHÆà[%úÖ#N¡uH¤ãlûLdQá^ÆÞÈgk[wcý%õ¤D~ª2+8å#ÕzBÐV´+Lë{Þ$Í»5OÄEàN6 É6LÄ}Åµ¸6:Á× |
| --- | Minor | ±*'UcU~+(®[ùÍÄHIîHhÔ­NRx+§¤pPñ´USg©ªª©lkèÛ n\¹ö;==®Öfª÷Uû#Ù º="4·4Ù*Ðè@	|Qtãøå´ÒüLµ[Ïx%ÍWvIÿ<ëDHGw~ÊDfM7®,t»ÎM$ôò:Üxµ¬wºùUU¬WðÓ;Ý©°í#ãÞÐn¦·²ð{|¥¶¦NÛÓPg¹ÞjQ°¼WaéþÀãá4s¯àü0'Æëå£|Râ·û3eE³;I]Ýò®¹üT&U¯HÑ¦óEc«T¹÷îyw²_o+À |
| --- | Minor | ß6ï.µëZXWÙÑÜ¤³d_?¥ô È,Ú;C¥ùÙõ¯©ôá £ß¡w~<lèÿôH	MÖQ.ÑiLF,6güªâ "+]F"'p¿Ó`SíØ	¿Hf¡U¿Æ¹«WÈI:ÖùymèÚWºØºNpfæ3)vHdÂ3ÞÜ¬Ð·ÉP©1:@7PS>_ÖÃ|m·çÆÉ,©ÐuíÐj^÷þÇÑ L°9}óZCX¡Êô<6ï¯U©#§¶ÌJÏÖTgåæàx4ÊéCÇßdÃ´GFòBwu ðJÞúÓNUK´`±æ~°CþÀ6ß5GÒT.ÈxD"ojòW2Ñïî |
| --- | Minor | *AÎ=ñ~RfUe®SY*sâÀâ)«Ñ£¥Ô(4ªç×Ü½åÖÅ×^½§ECCÜiÚïld"Ñ"ÙK¿Ü¿*ÜÍ>ÕûÖ~Ïx¿ëób¢Ài0¥Û ,©à¸fÒ»Éñ úXÿ ü¡ô°´ÄWV±Kø9FU¿ö]p²I(í¾*ÇóÈÄ3îK^ÿ,ç!XUÖdõ æsä±-ðC~Kç_Jô0ìL­Ëó$[~K¶<I^ÇK; æâÔ´?E¹jüµÚ¤ïPOûÔùÆÕGð£é"9{oh:£(·:! |
| --- | Minor | ©IÔ â@á$Ië¯ìXùIlà¸Ñê øVmÏ]¥'Qy(¦özö öZ¾<yè±¶+ßh¹^)Í!ÁjÓ$µ±YT\h­-AVLÔÏ. ¹?¤6£ iý U¹Ô©Ú ©ÜðÔ'5¥_×³íÍa |
| --- | Minor | ¡\úPLÕUYkwsuØ­²<P:C%wË{Q`ÂXl |
| --- | Minor | (JÓ5¢£*>Ï2@ëæ@ÅM¡BVe&ß+`´)+óéa¸ÃZ |
| --- | Minor | §äò# ­¶IÊþ¢\Ú´7¶ÁTì»ºµ |
| --- | Minor | ã×¸2øxÚäbãAßm­°[?Î::>Ì¸¶¥Ô/7cïÏ/·ºÝhÐ¶Q×Ó±×±ºûDcÇú ) ÔF¿µ)l}Ï#á§ )Éü¶aMBA_^/ã¢[ mj9·Ëº´r+Êï­)öÛè]îÚT´ |
| --- | Minor | ¢ÜNF[µÇPÊ´K'[Â{ú¤EAQÇqÑOvh8D.ÎéSÄËU`a=?m&©=4tEï	ûÞ2öEiìÐLbé=÷HN. =¡ã1£R§ý*fCÄwËkS³é;gAw¸wÿ~dXËFC:n]iíø	ì^A%@NºC¹vÊºk. ðêÚJ§myï[ç0xÝ¦s§rýàÂP¹ÚmÍ. Ö5"IÀdé|åGßW]Ó73òºbÝ¡\45¿þ¸Ú%Ñ¾UÚÏx)uº¦·bn2ñ »¡ÃÚ©.õ+ªï"ÆÕ2WrPëWã^ër¹Ç7éË=ViÄtÑa©Ä ¢ósoÛÑ0. ÊBS¡vå&`åRAe |
| --- | Minor | §±Á8@5â%¹x6ª©Å`ª¯¡æ~ª4LnÙø`8Âk*¥e²º^+©"Ý+|Q³­WÆKf9ÞÊÖIßÎÜÙ¡ |
| --- | Minor | ®â­-Ò h(©§a^Ç¸¯B;ÖbkÏ&¸"Éf¯n	vS·êf¿·êÛ\ÑKIÛSòmEE_k;ó¥rYL}ksÖJø4ïÄ5B}|¯´%±@EòÞ¬+OWÚ¯AÌú¶ÒQC²{yovÍ{ëíÕ¶åÃölð¯. £u+t iï#üZ4Õ¨:*¿Ù7h«îµ)9ÒCHïüI%{A$P­fÃ2w¦+R-½bäá½ªÈæ«¢?¿éÄ:b¸Ãx´Mí\&ñÝ¶I!tê5Mu4 ØY¶r{ RÿfÇª0.­&HÆzSUæhE¤AØqËW%Ò)EA.¾¿;w ôUÏlR`#©{K¾)¦wVöR;Ú.]Es´o±°4/èTõ·  ³äÕáÂ4·`n*ÚCkïõ\3Ùºµ+­»êÖS}	Ø¥iÝ^ß]@Áa ]ÙÚieÂ³£	«ÐbO:ÕÛ±>h;%æÊ)VßzõZ»7{ÆM¶åèB[[voh-I |
| --- | Minor | \X®×ºêÛ*SæÐe³¹å-î#S¶úX&Éu6zJRÚsÞÔß=ÅÞVKØÂ½ß |
| --- | Minor | ÎÍ´¹[µ9wã¥£"íl#¹íêõöáþÖóÐôR©*ÞÚ0!6Ð¾'¨MåôYªáº×ÏV)eºJAûÔnÉÈ°n´T¢+¢Àými-mñ¹EX?Ñöáv.±&óèÛQÕó'ÕiùsµÑl7¢®¾U¬myFÊ<[àÓfLë3IC{J2Âç²9ÞáHÞö^Ú. Pï§%Ióu®Ñí­	Ø©Tg®.¼ÂQV&¢Çé/í¢Ân¸Û[Á­ø.­ÊRu¢-§-º;32¥`åßàmjMÂÐAòÌBñ×ª@ðô@>ÚOzëë`Õ M}sâwÊ¹	¹c60WjD¦ç2RkÃvö^PÉ# -ú(É{g¬sÌÓ¬¥mÞ;¸6í¬µwI)Áw~k Vßx(Ñ ´uÕ×Ú+f_«­QOÓ½oî|E(0eÍ#ü\I$k·`«÷×WÀe¹«êð¸Öiêç'üfO¸ÚÐr:tªØê50òH¶¢³ô÷\ñÄQH?úrJ'´¬C³Úö¬¦ãµûöÌÎº+®ÓÞ§U»0jCcNµ¡Ñµ!ª#ªÒâæk*Cøæºb0Is×ü}Faïç!ivC3CÚ²²c¦»·e© Ì¼OË	ÛÒGòbÅ´C8 |
| --- | Minor | ·æ@íVÚÔâ\4Ê%ÃöÎiìkk¶È`@080a¹*¶J¡n}oBZàµ<Ði	«V*s´ÚÁê}±Ù®=ôíåQYmí'y ÌÈc§Ð"nvm0ÜÂãî4aeÍ*ÆhßÈKï©{ÛÑ·¡Üè{REYæáMåV²ÛºÜÛRLÌÞPvíG§úÛÃCR¼ÿ§Jyg¢Ç©E <àKAüÑB!×FFÓÁ3j£¢`®ÆJ÷ß¬%â3hªÌp²<·Õ$´»9qháÐ%÷VïhâPNaõ¥Ë¯HÄ¯1eÅ`?¯Ì£ô¢¤=7uúTåP~v-uY{mà´ÌLQñôÑøX råòënL5Þ7&Ã «1ÊÙ èÃ\îVRuDme<láXB¡5âUPï1T£\qÄCiYtú´ !ßªßµÆe7ã±rv.7ÚCÇµö;/|Iðc÷}ã9·è¹Í`æ<ç­¸©åánÉXSIÆ. ùµlÛ9ö;mÝ¼'Öu³°î§ªËT-õÄw<hÕR}hâéy]÷þ&íIvtÅºïVÜíÞYË2(FVq!ìc«ÝÓðè=Ó¾·fÞwd3Eu(â[0Ä!jMU¹Ãyx&Ù ÌS`DµË ³eµ6~­ÄÞ>EcÛ9ÞGQWeªbîÑá¤ð}Ø+.Zß92jwoå¸¼Ox£¼{/Ôú¹üÏò°ºæ9å;CáªùÝ¬= åx Ë`%Ïä	H»Pl±U¡¥$×V%ºÀ;bêªÍ^~LvÏ®|oÌË*¼Wú§Ö_â~G HÑÊ-ªFCÃ*ô F ÒªCe`>û(Àl¼«½/"ó¿´×÷'Ö'^ü8ä.ÜÈe¨¡ßÅHå)ÉaÜäÂÍoíx.g@¹¤ª½ÙAÇÜÏJôlÞH<*æG# Hy;XyLê-®¡LÍ½À)£<ÁY½)÷Døi)ùàX¥ºD §ûåå¶º.Ïjå¼V<µ.öê;[æ!µO.§/»)ãZAÖÔEXcºy |
| --- | Minor | %ÜÑ'ÕkKóV£Nr@6_>bfA¿©Øþ÷â)çÉ¥XÙÄÕÔèHµÞÝRVÈ[å­¦â æ#.P/é¸p®Ü;JE!É |
| --- | Minor | ¦Ou`mc¤ÉºØclô5ZHüdÌïº®üÊ4ÊÅXq+Æ®ÎË*ÂD13<þ³µñtxD¿õª1hN2@ |
| --- | Minor | ±[ù	§f3¹I¥tèÚÀ^UÍuÎ2á\´cÍB@tj?¥J´©xÄÙq¹|óÝ§hS³áúP"åhjdt3	NféUð$F£\y®»5EÎ åÛé¯czi\æl1Ò÷\gÞHshõ[¥sº°Ø%#¹ Ç3jÄHóÃm¦kô±mFyp]àPÁ7Ú-R` GPúóÐyJ¦¼îÔ¾õç|í.ÅW×;þÖÛ¾IKîg1ëbMÙë |
| --- | Minor | f2±YBs]ù±ÒÇL.^\Ë{ç*Tjµ*jÂJ?Y)ËÒÓaçv²b!bÖâé@OT¼¯Mì*ò{7üC©Ìâ1G²arv^Jìýp°	7èfmØE f;`{÷°bLï±Ã]çsçOÿf>w#À¬+åäá@<Ñ |
| --- | Minor | *XÁÎ¡*V¯I2åªÖÒß6¯OI£r£°5<¾ÒÐ/×i¥3ÁxQ8Ñ{ù]ß_J¸il~å=z ÊÜ"ì¹ÜBnm=~ª´§ÓÈíO	rÕ&³Íí5`µïè%Ñ¬RîE ú&YØúÚóáÜoú¡Ø¥B\Ý¹å4· r¢¿t³hjCày$Ââ~¨é Äå|wâ°SÅ¢Æu¯ñ÷vJÙ. Bðé6-]. hÁehÖEÞ2¦vM.äç/ñÜé]Þ-Þ¦½LÎ	Ñ¦Ï]|Ì¯ó}. '9»PÓ9§¬5ä ¥£}ß6Ë9QàÓaÚ9_¢dùÇ|Ô Xè©í3 ¥PI÷Þ "`OÎ¨L%«a(Á¯.§·BÊñæÉÿÖÆq xîª¢Áæ¨©OF¯æ+OLC¨Á+ÕïöV­C°/Ø<mýRöP)æiR;0xâóËì1)ªêUñá"Ü!ÀEB7xÉùÀx5 ¶ÆÄ9m·ìTå©Äè=ãV9²ÈåMRñ.IFaþÇLpù çz»®ÊO[òÓsÎ.=ìÚ2)Ì |
| --- | Minor | »Á¡é5^°hq¦6t9sÙÅùÔh¤I»wKæÁE³ÜÂEx4oyÛ[/	Î=AÉä¾TSËs?É¹áÖödHÅ@!Q¯¼ýÿîÒ?. O£<ï-¨Å.åk¶Æ®Ñ*Ò[ÜÒ[DìÓÓÆrQØëäÞÝ%õw¿Ó |
| --- | Minor | gü0éi|"_³wCV5¿(® ²w.  È». ¡ôáybÃýGÄÆIæ¿ñ.Z\Æ±o{JÇ%èîyä |
| --- | Minor | ):1tûxÎl¯»tSVTz2Å?8Ü%©éWè§TY§VQI®»ÖáÉE'Xn ï3ão¬(¶. aÍÍV¾È·57Ø. g®éW=cÈ>#óØC@¶SnIìdÈlZìÿq{¸0K*ÞHy8gTÄ	VäQûÃÏþ"Egq endstream endobj 362 0 obj <</Filter/FlateDecode/Length 4847>> stream xÚ½\I¯#¹¾ûW¼j4CFp¨ßÁûdLÝÆs(ú |
| --- | Minor | `À}õ¯7· [Jê®rU\±|±åÛ?Þää7+ýáão_ÿ¾ûÿðÿÞ~÷ùí?þ[¾_õöùã |
| --- | Minor | @"<þ!røöùþ¿W!~þÖòýÿ>ÿ1>&ß¤8¼ðÂ¹øäIâÛEãáV¾<ø~)aîa²ð?|!¿Ï"|!0üoàý¯íLß¨+}Ê¿(ærï-lü%|Âql× Tø·¼~ZûçR÷wH3øöLüwü |
| --- | Minor | /pË£ðÍz/38eM;GÜ_<_8O!î.PHin!èÓ_(ÃL?L`Q¿ÁauøÞh(ä?@¡ôñmôý°^ßÊéºü%|ú EãU?^ºð±²< 6ÐG8SX:úÏÍdxHsI?¬9 ÄØ±lxÂ½Ñ^rtéæ¡Ýf¾áð÷­ÜêòçI·rAhÿ"ñì e!­*¿2ÆUÆ°2+ô-m)ý íßÂHHrÁ=¯` |
| --- | Minor | ¹`¤oÊqâsëWËl^W¹µU¸°µsùL×ÔôtÜbÌT¨{ì­ÑË{ ßÝéZ6· Ùd4£umÆÈy¬Zi«4>0Á[c¸¯¨â¿ãüU1VU¬èX5NÕY4-\@=eÓ<ðCUMâ÷ãN=z¥^f~#ÌÒhÐVa6	ãõ% ÖI|wç×ç«å. â  yFP9¨BE×D6+2¦w0×Þ¶p |
| --- | Minor | ­Ó«ÜfîHÆà[%úÖ#N¡uH¤ãlûLdQá^ÆÞÈgk[wcý%õ¤D~ª2+8å#ÕzBÐV´+Lë{Þ$Í»5OÄEàN6 É6LÄ}Åµ¸6:Á× |
| --- | Minor | ±*'UcU~+(®[ùÍÄHIîHhÔ­NRx+§¤pPñ´USg©ªª©lkèÛ n\¹ö;==®Öfª÷Uû#Ù º="4·4Ù*Ðè@	|Qtãøå´ÒüLµ[Ïx%ÍWvIÿ<ëDHGw~ÊDfM7®. t»ÎM$ôò:Üxµ¬wºùUU¬WðÓ;Ý©°í#ãÞÐn¦·²ð{|¥¶¦NÛÓPg¹ÞjQ°¼WaéþÀãá4s¯àü0'Æëå£|Râ·û3eE³;I]Ýò®¹üT&U¯HÑ¦óEc«T¹÷îyw²_o+À |
| --- | Minor | ß6ï.µëZXWÙÑÜ¤³d_?¥ô È. Ú;C¥ùÙõ¯©ôá £ß¡w~<lèÿôH	MÖQ.ÑiLF. 6güªâ "+]F"'p¿Ó`SíØ	¿Hf¡U¿Æ¹«WÈI:ÖùymèÚWºØºNpfæ3)vHdÂ3ÞÜ¬Ð·ÉP©1:@7PS>_ÖÃ|m·çÆÉ. ©ÐuíÐj^÷þÇÑ L°9}óZCX¡Êô<6ï¯U©#§¶ÌJÏÖTgåæàx4ÊéCÇßdÃ´GFòBwu ðJÞúÓNUK´`±æ~°CþÀ6ß5GÒT.ÈxD"ojòW2Ñïî |
| --- | Minor | *AÎ=ñ~RfUe®SY*sâÀâ)«Ñ£¥Ô(4ªç×Ü½åÖÅ×^½§ECCÜiÚïld"Ñ"ÙK¿Ü¿*ÜÍ>ÕûÖ~Ïx¿ëób¢Ài0¥Û. ©à¸fÒ»Éñ úXÿ ü¡ô°´ÄWV±Kø9FU¿ö]p²I(í¾*ÇóÈÄ3îK^ÿ. ç!XUÖdõ æsä±-ðC~Kç_Jô0ìL­Ëó$[~K¶<I^ÇK; æâÔ´?E¹jüµÚ¤ïPOûÔùÆÕGð£é"9{oh:£(·:!. |
| --- | Minor | Sentence exceeds complexity threshold, split for readability. Applying the split needs --strength moderate or higher. |
| --- | Minor | none (split proposal only; source not rewritten) |
| --- | Minor | none |
| --- | Minor | Check: NEEDS-LLM |
| --- | Minor | Flags:    not-assessed |
| --- | Minor | SENTENCE (Line 939, 633 words, 15 clauses)  [Script] |
| --- | Minor | í÷Kcd25ì#» IÙ 'C<AùÃnÛqg±¡}(&°-¹KÌ·¯Y¶·Îìöe­v»rÈç±Í[G`%c¯.>ÃüÂµhmÁZY§\ÔìyµïyõF?ÃÚÏª<¡OemÜµ)àqF©ÈÌÓÊ³«g!¢¦§B~é¹ÑB%´ m¦mºT¬Õ}µñ·	n¨BÈ¯¡IÕÔ.jX7°,UØ¦ÁÑfÞ[ñ,JÖ÷>åÔ¶çÿ2´¿ÕC1&T,ÌJÞ-w³:É{´ |
| --- | Minor | ÷¨2Û=Ý½f+Ä_²¼Oc"ð£:WÚ-ý:ós¬¾$åHodã^KätñF::Q3ù±ãäêsMm ÐO ícá06¸¤~~f2õA²ÉÉSÞ3§+K4­ðµVÍ«Ã¹ >Äa8?i"ñùo |
| --- | Minor | {hïA.f9·ph1|½ ²Ífàs%oÍü4ÂvxcQ¾L3f9éa´¡??¸p( ¢ym¸'6{XV¨k³T{Z!¤bþt~ýÅ6éH9©§t'ÑU%Î~¿È¢¢)TµT=\Êcn×e´ÂB |
| --- | Minor | ]v5J5Ae~ºÊeR(}³½7X*	>9ÿë·ZTÖé©!_×ê ¬u£v_æéAç}m«&Ã¸&îÈß<k¹Ò¬ä~'KLÑ>Ð«d¨%ëÓø)º]ÌÁ±ÇL;a içYïÜäTR}Ð¾J|É_Âp^fj´'r Rf4fHå¬ÄWrb ¤k!$Q¢hG×í¸,#%hiXÍêªÓ)O>QGª®tb¨Æù:|oP¥&`P ã§.JË}qØ Ñ¤Å2 ·@yHD#wIM6NE,i¯ä>ýÏïÃî¥O ±-CshöÅï,0I1 $7©-ptïÉ6üs]àØýþûû	Ó¯ÝVûüoT®®s-SRLôÜ~Ó©µCÊ®ëèù¹þS'pé1È®rýÑP©ÄZï%µÉÕ)ë>SFÖ60o1ë¨Â¬åº!M5¹[ª#W¿D0pêÞ¸UR`&!kîè u¨Ñ^>çb+eG<Ï9Ç|Ø³¸È´¦§Îò`ø%ó¢ËÃ\*ØcXëÖJ ÔÕ±ë/ä¢·Ú¨1V¼K:ëô ÿE´ºA*Ý¡rö;ÔºÂgí½QMÄÏ;¯«¢Y1ê¾rA·b]÷§M°Jh	¯Òä[æáA=Æ£s¶G ån I­ Àk2«k¹±§@ÍßP<ãjvÕl+IRB1õarC"EâÌU.Vû8a ¥­Ò-ÒUÂ[½ÒÍ,£fãHólLÓÌë+lkê±òZJ¡·×MÃolpsA¢°v¸øòí¤,Skö0^»ÑO7 D1{ò=ªò{	goî(ÜúZÚÎ w]s[NÒóZ·À>NÇ»í!máÉºÈ"¾Ã?;ëüî	Ä` ð§¥½DWaMrXXW5xÒ¦lÖÛpÏÜUbÂþÄé¢'Ç«(KP~CnkbÆm>±2 A5^bÙYS1}Ù}àf ÅµÇ[ÛS­ñø	kÿN«9-&áÂ%Xáp"ã}YU;f.)v©²¬ªV·$üè»v ø +:ßíGõ\;ÀQØC£|(ÂTú%å¹¯¢äÊ[¡4õutÝUòTµ>£ð)½ñéï{l%o X»Õ½1lcÂ×\zï©l_¼ä[mn±Ìôº¦2ñ¡¿s¢©aµË§ù¼µÀZÚëª½ åè_ÕÊô!Ô¥¥aào}ür/Ê Uo¬»{×äÕ¬Ê*z´8%w4N,ºr¨!W[<b«a'âß À.~×¶c:mÚb-V3|{³údæÄ|,5Öõó];cÑì¢Êáåèhðueø®2vÇêÖ¤_(aE¶Py\kÞs65-5(ÏZ1¸ÕÀ½ê.ÓÌÛ·_ª%¯;#7¥DÙ\½/ÝÜ1TS`NüÒj.L·FfÈD8â\Ö¼µqju±UË]E¸?À)0í»è 5ÆõéªL}É¬½>èÁÜ6öJãJÝÉ5WØÿ5Hè6U¦yî½¦ Õ |
| --- | Minor | hÚöükÅNª=;7ýh¢ñí¦î\ruÝë n°	JÔ`¶Ðuçz×S:w9ÂÅ×rýtf¼ßgc+È!EèÛ~êéNõ¾¿òDË@PÕ Û¯Õ¤2+ª,RªnJ	ÐaA;sÿä¦¶ß÷ÉÛ¸¡Ãz3¼N5T(g-m§»6"l,úWn¹uWæ¢Ù©aê¼m9?qïo#¨¹TO^Íê­7ÕóUû®Ò§z;Q<~ýB©´Ýñrh:LÁ©XÜH*cF2Á¹ìHYz÷ÇúñÑ ÿ:+[ÃÑ¼dG¨£Ð@]/ý{!J·JËSû³6ÿäÞëÚ9÷+Ësê»òSÙØñ½££QîÅÄFÂû<y×b¸/ìRÂÛåa7æ¤àHÒ:zfÇMÊ>i7¾ÎöûÏM,&xBy09ÂU ½ï1y¦Hn(¶ß É`|J ÷t½i{|.Yë_	ñJIãÖÆë×Net¿æF@þR¾çã ¬ù¾%ßëç3q®ÖV¸ÁBg¦@^Ùûv\ÒXxö¾E~t×p,w'¯ÅöÐâ%Wbª;ËBCÑR¤ÂÈÒwüñÆô~ÏvNÞÄjï¼µ¸dêÉM=§º |
| --- | Minor | zBy`¦[dÑû°c,÷õËî |
| --- | Minor | cA¨Ü~¸Ö÷}å¾.Ë)Y]Hõã»×%å×À³½ËåH¬zcªVéÍtk!¬¯Eêã sãWß¢öÇ;ã[°¶+«á»Ô.ì3 >+S |
| --- | Minor | í÷Kcd25ì#» IÙ 'C<AùÃnÛqg±¡}(&°-¹KÌ·¯Y¶·Îìöe­v»rÈç±Í[G`%c¯.>ÃüÂµhmÁZY§\ÔìyµïyõF?ÃÚÏª<¡OemÜµ)àqF©ÈÌÓÊ³«g!¢¦§B~é¹ÑB%´ m¦mºT¬Õ}µñ·	n¨BÈ¯¡IÕÔ.jX7°. UØ¦ÁÑfÞ[ñ. JÖ÷>åÔ¶çÿ2´¿ÕC1&T. ÌJÞ-w³:É{´ |
| --- | Minor | ÷¨2Û=Ý½f+Ä_²¼Oc"ð£:WÚ-ý:ós¬¾$åHodã^KätñF::Q3ù±ãäêsMm ÐO ícá06¸¤~~f2õA²ÉÉSÞ3§+K4­ðµVÍ«Ã¹ >Äa8?i"ñùo |
| --- | Minor | {hïA.f9·ph1|½ ²Ífàs%oÍü4ÂvxcQ¾L3f9éa´¡??¸p( ¢ym¸'6{XV¨k³T{Z!¤bþt~ýÅ6éH9©§t'ÑU%Î~¿È¢¢)TµT=\Êcn×e´ÂB |
| --- | Minor | ]v5J5Ae~ºÊeR(}³½7X*	>9ÿë·ZTÖé©!_×ê ¬u£v_æéAç}m«&Ã¸&îÈß<k¹Ò¬ä~'KLÑ>Ð«d¨%ëÓø)º]ÌÁ±ÇL;a içYïÜäTR}Ð¾J|É_Âp^fj´'r Rf4fHå¬ÄWrb ¤k!$Q¢hG×í¸. #%hiXÍêªÓ)O>QGª®tb¨Æù:|oP¥&`P ã§.JË}qØ Ñ¤Å2 ·@yHD#wIM6NE. i¯ä>ýÏïÃî¥O ±-CshöÅï. 0I1 $7©-ptïÉ6üs]àØýþûû	Ó¯ÝVûüoT®®s-SRLôÜ~Ó©µCÊ®ëèù¹þS'pé1È®rýÑP©ÄZï%µÉÕ)ë>SFÖ60o1ë¨Â¬åº!M5¹[ª#W¿D0pêÞ¸UR`&!kîè u¨Ñ^>çb+eG<Ï9Ç|Ø³¸È´¦§Îò`ø%ó¢ËÃ\*ØcXëÖJ ÔÕ±ë/ä¢·Ú¨1V¼K:ëô ÿE´ºA*Ý¡rö;ÔºÂgí½QMÄÏ;¯«¢Y1ê¾rA·b]÷§M°Jh	¯Òä[æáA=Æ£s¶G ån I­ Àk2«k¹±§@ÍßP<ãjvÕl+IRB1õarC"EâÌU.Vû8a ¥­Ò-ÒUÂ[½ÒÍ. £fãHólLÓÌë+lkê±òZJ¡·×MÃolpsA¢°v¸øòí¤. Skö0^»ÑO7 D1{ò=ªò{	goî(ÜúZÚÎ w]s[NÒóZ·À>NÇ»í!máÉºÈ"¾Ã?;ëüî	Ä` ð§¥½DWaMrXXW5xÒ¦lÖÛpÏÜUbÂþÄé¢'Ç«(KP~CnkbÆm>±2 A5^bÙYS1}Ù}àf ÅµÇ[ÛS­ñø	kÿN«9-&áÂ%Xáp"ã}YU;f.)v©²¬ªV·$üè»v ø +:ßíGõ\;ÀQØC£|(ÂTú%å¹¯¢äÊ[¡4õutÝUòTµ>£ð)½ñéï{l%o X»Õ½1lcÂ×\zï©l_¼ä[mn±Ìôº¦2ñ¡¿s¢©aµË§ù¼µÀZÚëª½ åè_ÕÊô!Ô¥¥aào}ür/Ê Uo¬»{×äÕ¬Ê*z´8%w4N. ºr¨!W[<b«a'âß À.~×¶c:mÚb-V3|{³údæÄ|. 5Öõó];cÑì¢Êáåèhðueø®2vÇêÖ¤_(aE¶Py\kÞs65-5(ÏZ1¸ÕÀ½ê.ÓÌÛ·_ª%¯;#7¥DÙ\½/ÝÜ1TS`NüÒj.L·FfÈD8â\Ö¼µqju±UË]E¸?À)0í»è 5ÆõéªL}É¬½>èÁÜ6öJãJÝÉ5WØÿ5Hè6U¦yî½¦ Õ |
| --- | Minor | hÚöükÅNª=;7ýh¢ñí¦î\ruÝë n°	JÔ`¶Ðuçz×S:w9ÂÅ×rýtf¼ßgc+È!EèÛ~êéNõ¾¿òDË@PÕ Û¯Õ¤2+ª. RªnJ	ÐaA;sÿä¦¶ß÷ÉÛ¸¡Ãz3¼N5T(g-m§»6"l. úWn¹uWæ¢Ù©aê¼m9?qïo#¨¹TO^Íê­7ÕóUû®Ò§z;Q<~ýB©´Ýñrh:LÁ©XÜH*cF2Á¹ìHYz÷ÇúñÑ ÿ:+[ÃÑ¼dG¨£Ð@]/ý{!J·JËSû³6ÿäÞëÚ9÷+Ësê»òSÙØñ½££QîÅÄFÂû<y×b¸/ìRÂÛåa7æ¤àHÒ:zfÇMÊ>i7¾ÎöûÏM. &xBy09ÂU ½ï1y¦Hn(¶ß É`|J ÷t½i{|.Yë_	ñJIãÖÆë×Net¿æF@þR¾çã ¬ù¾%ßëç3q®ÖV¸ÁBg¦@^Ùûv\ÒXxö¾E~t×p. w'¯ÅöÐâ%Wbª;ËBCÑR¤ÂÈÒwüñÆô~ÏvNÞÄjï¼µ¸dêÉM=§º |
| --- | Minor | zBy`¦[dÑû°c. ÷õËî |
| --- | Minor | cA¨Ü~¸Ö÷}å¾.Ë)Y]Hõã»×%å×À³½ËåH¬zcªVéÍtk!¬¯Eêã sãWß¢öÇ;ã[°¶+«á»Ô.ì3 >+S. |
| --- | Minor | Sentence exceeds complexity threshold, split for readability. Applying the split needs --strength moderate or higher. |
| --- | Minor | none (split proposal only; source not rewritten) |
| --- | Minor | none |
| --- | Minor | Check: NEEDS-LLM |
| --- | Minor | Flags:    not-assessed |
| --- | Minor | SENTENCE (Line 1044, 190 words, 2 clauses)  [Script] |
| --- | Minor | öÊÜKÀ>Gh1R |
| --- | Minor | m |
| --- | Minor | ?ÿæ_Ó endstream endobj 372 0 obj <</Filter/FlateDecode/Length 4123>> stream xÚå\K¹ |
| --- | Minor |  +õ^´ç 	 ñ-ÉÁíöä=ì)?Ôõêî]Cl¦»J%E~|Ô~>ÉÀÿòäàäd8Büwúò^ûþüéôûO§ßýQð«O^ORÃø`O ¡µW§O·¿_°ÄÈøù??A-Wü× «W!cñ3×³rÏùN©þNwó¨ú4ÄÑ¾¬îàU£óç8§.£Õõåþ|úÃ§Â<Iq÷ |
| --- | Minor | =kyhteãÅþ_pASù²¨W~//g#Ä@°»å¯ùÙÈ:±é,>ô%³ïÑé3Db·³GêÏQlÄê×8ºE8+ ;-	ÁgA+O£Êc /qDÜ¢-®i§'â%!¢Ö Ú¯QGPlï}øPR6*»äeãò´sqQdº< |
| --- | Minor | ,Ñ*ù°¦¿m´-Ã>J»£&È»cPd6RöB-[ç:+méñ§³TÑ¡+ITûåQ?^Ût¦Ç |
| --- | Minor | Û ¿ä5ü×Qe¤lÊ²´«¤Bp-¾²sd£Z]H¨´¤öyÆÈ¯QÔª®(/ù´E%!JÓ	¼n¦PÓ¨H´ÞÊéKJIó¦]¯ÔZd.Ï¦ Á/|#ÝL[!¦¸eNRLØéIhçYÔÐéBBºê 3§si!!Òù×h(¸xvËÌÀ)×6¦ WÊ÷ PÆUMäú²=^¨EÊÔÑNf2¹Íe>Ùa|]SãðÅùµÄ(ÒóIÌ?$ |
| --- | Minor | ¸5qj¶i¨«Åÿ|:¼§ôé?'	ö@£fàìõ Þ~:)´ãA:Ï¯þûô·ÓÙþ?yäÆ*gÉ	ë@ÎÁÊ£1#uú¼8Ð! |
| --- | Minor | öÊÜKÀ>Gh1R |
| --- | Minor | m |
| --- | Minor | ?ÿæ_Ó endstream endobj 372 0 obj <</Filter/FlateDecode/Length 4123>> stream xÚå\K¹ |
| --- | Minor |  +õ^´ç 	 ñ-ÉÁíöä=ì)?Ôõêî]Cl¦»J%E~|Ô~>ÉÀÿòäàäd8Büwúò^ûþüéôûO§ßýQð«O^ORÃø`O ¡µW§O·¿_°ÄÈøù??A-Wü× «W!cñ3×³rÏùN©þNwó¨ú4ÄÑ¾¬îàU£óç8§.£Õõåþ|úÃ§Â<Iq÷ |
| --- | Minor | =kyhteãÅþ_pASù²¨W~//g#Ä@°»å¯ùÙÈ:±é. >ô%³ïÑé3Db·³GêÏQlÄê×8ºE8+ ;-	ÁgA+O£Êc /qDÜ¢-®i§'â%!¢Ö Ú¯QGPlï}øPR6*»äeãò´sqQdº< |
| --- | Minor | . Ñ*ù°¦¿m´-Ã>J»£&È»cPd6RöB-[ç:+méñ§³TÑ¡+ITûåQ?^Ût¦Ç |
| --- | Minor | Û ¿ä5ü×Qe¤lÊ²´«¤Bp-¾²sd£Z]H¨´¤öyÆÈ¯QÔª®(/ù´E%!JÓ	¼n¦PÓ¨H´ÞÊéKJIó¦]¯ÔZd.Ï¦ Á/|#ÝL[!¦¸eNRLØéIhçYÔÐéBBºê 3§si!!Òù×h(¸xvËÌÀ)×6¦ WÊ÷ PÆUMäú²=^¨EÊÔÑNf2¹Íe>Ùa|]SãðÅùµÄ(ÒóIÌ?$ |
| --- | Minor | ¸5qj¶i¨«Åÿ|:¼§ôé?'	ö@£fàìõ Þ~:)´ãA:Ï¯þûô·ÓÙþ?yäÆ*gÉ	ë@ÎÁÊ£1#uú¼8Ð!. |
| --- | Minor | Sentence exceeds complexity threshold, split for readability. Applying the split needs --strength moderate or higher. |
| --- | Minor | none (split proposal only; source not rewritten) |
| --- | Minor | none |
| --- | Minor | Check: NEEDS-LLM |
| --- | Minor | Flags:    not-assessed |
| --- | Minor | SENTENCE (Line 1044, 330 words, 5 clauses)  [Script] |
| --- | Minor | èHu(+h¦óká¢¸|J3ÿÞûÓú¨n:m¨§¶éÌ!ePjµY*-rÚI¥wxpèÓ;±´ËL.r')eíåjïGi¢;ðé%þ(?Dá>(kÖÊöü¸}:ú]Y>fÊHüél¨RÄ%JÎß{Q<	j5¤»Ê >,gÃà¹Hï?,YÑ:~±xòºÏYúhö¼3q'/Ö^²_¡S×«·`\³/I>¨Ê®å!q-/½o"3àÔï»Ñ([;²Ý({XÿÊ  ?ëÕÃÒ(?ð1 9Ã:ëÞ\Æ®t±Èÿïrd¶|),p§ÞÜr¼ÇýLæ(b-tîWjÞ^èZÐå÷ºùðÀaq Ûvð£íòSTZ£jX?A/Q0i¸0wám ÈgÖ°+ß5´oeVßï½±ß{?Ñ'Ó~êÿÕ!ÚÃ"iíáLÄ(ý~ÖË lcî0	(	ÔC1tÁúÆãtÓPaz:ÆúyÿË.1¾³HÊº!®i8»Á¢f0ú~RÀ{Ê]D`L1ULTnº»tµßÒG©lÂX (­F5DÅæÀ\Ê Cg-gö1±7ÊÉI¶lw'ÎíwÉÚéßì¿OíV"lÄ&ñC|×GS1é e72ª± )âä¡úôòI¹e-k0h¡Ïb%\#$YµJÇ7gvÜ×!pKÄ ]ëE¬«Í4%éÓ°fddÇ¶%,x Õ!Ð%J &¼Wà/5Ï#rä_²ì×J%q3ãÏ!17Yu>d@&RI[a Bì$ÄîÂÉahlÍµÄSLÂÃÂMÊWPðX |
| --- | Minor | ¬§ý<;b¦7¦ïdÕù{Z(7ðò kÂtÞ(Á£4+_¹á	¢<:ù²Ó9'Jù16ML©ZÓ®;ëþTÑd÷Ø´ôíTÕ-h\ÒJFD0Å+gzf©Rw»ý|åQ¾V+{i)7< Ãw9&´K7äË[Ñ=@ |
| --- | Minor | ~zRÞ;qFî`^¬´½&®G~¼³ä>¥ùþ "Íe>îU g%NMºSÃ<éïÌ;à7gÑJ}ðPS´Í¬ÑÑOèLGftÈh·«Ü|§Ï·bð}Aàðø#ü@{¦a<î©ÙôÜ5v J·®Ü;f½÷°;UZY "@ªRiÍtJ$_Ó³E­£A¬Lóþø«ÁÅ3ªÔS©ìµ â©%Ýâò«MaÙE±vq>Å÷JÅGq¡¯TUS ©Æ	1P¾^9ÚèB·GØO¹ù×&pM» WñËÆ¿t§]|pé%¹¼¤Ö=QþË5axØ.½ÒÝÆh¨Ï1oßÁ^Ý)cnûÐkº^ÊPþN%Rn´äÝÑL¢ ¬ ÷µOï41Ð1ÑQWÍéèf>oª­iùÉ0?	Ód¤´0áðìÿZå­!`°òSc8þV²2¤c©,(®)Xãé6Äß¿Lam2#NËÏÅoÊÑ3sîÌáñ~åg1M~ÎrþæE­?I´>Y » º}8¬Ñ  \ùE¸ôÖ¹WÁ*V-<7Ri<! |
| --- | Minor | èHu(+h¦óká¢¸|J3ÿÞûÓú¨n:m¨§¶éÌ!ePjµY*-rÚI¥wxpèÓ;±´ËL.r')eíåjïGi¢;ðé%þ(?Dá>(kÖÊöü¸}:ú]Y>fÊHüél¨RÄ%JÎß{Q<	j5¤»Ê >. gÃà¹Hï?. YÑ:~±xòºÏYúhö¼3q'/Ö^²_¡S×«·`\³/I>¨Ê®å!q-/½o"3àÔï»Ñ([;²Ý({XÿÊ  ?ëÕÃÒ(?ð1 9Ã:ëÞ\Æ®t±Èÿïrd¶|). p§ÞÜr¼ÇýLæ(b-tîWjÞ^èZÐå÷ºùðÀaq Ûvð£íòSTZ£jX?A/Q0i¸0wám ÈgÖ°+ß5´oeVßï½±ß{?Ñ'Ó~êÿÕ!ÚÃ"iíáLÄ(ý~ÖË lcî0	(	ÔC1tÁúÆãtÓPaz:ÆúyÿË.1¾³HÊº!®i8»Á¢f0ú~RÀ{Ê]D`L1ULTnº»tµßÒG©lÂX (­F5DÅæÀ\Ê Cg-gö1±7ÊÉI¶lw'ÎíwÉÚéßì¿OíV"lÄ&ñC|×GS1é e72ª± )âä¡úôòI¹e-k0h¡Ïb%\#$YµJÇ7gvÜ×!pKÄ ]ëE¬«Í4%éÓ°fddÇ¶%. x Õ!Ð%J &¼Wà/5Ï#rä_²ì×J%q3ãÏ!17Yu>d@&RI[a Bì$ÄîÂÉahlÍµÄSLÂÃÂMÊWPðX |
| --- | Minor | ¬§ý<;b¦7¦ïdÕù{Z(7ðò kÂtÞ(Á£4+_¹á	¢<:ù²Ó9'Jù16ML©ZÓ®;ëþTÑd÷Ø´ôíTÕ-h\ÒJFD0Å+gzf©Rw»ý|åQ¾V+{i)7< Ãw9&´K7äË[Ñ=@ |
| --- | Minor | ~zRÞ;qFî`^¬´½&®G~¼³ä>¥ùþ "Íe>îU g%NMºSÃ<éïÌ;à7gÑJ}ðPS´Í¬ÑÑOèLGftÈh·«Ü|§Ï·bð}Aàðø#ü@{¦a<î©ÙôÜ5v J·®Ü;f½÷°;UZY "@ªRiÍtJ$_Ó³E­£A¬Lóþø«ÁÅ3ªÔS©ìµ â©%Ýâò«MaÙE±vq>Å÷JÅGq¡¯TUS ©Æ	1P¾^9ÚèB·GØO¹ù×&pM» WñËÆ¿t§]|pé%¹¼¤Ö=QþË5axØ.½ÒÝÆh¨Ï1oßÁ^Ý)cnûÐkº^ÊPþN%Rn´äÝÑL¢ ¬ ÷µOï41Ð1ÑQWÍéèf>oª­iùÉ0?	Ód¤´0áðìÿZå­!`°òSc8þV²2¤c©. (®)Xãé6Äß¿Lam2#NËÏÅoÊÑ3sîÌáñ~åg1M~ÎrþæE­?I´>Y » º}8¬Ñ  \ùE¸ôÖ¹WÁ*V-<7Ri<!. |
| --- | Minor | Sentence exceeds complexity threshold, split for readability. Applying the split needs --strength moderate or higher. |
| --- | Minor | none (split proposal only; source not rewritten) |
| --- | Minor | none |
| --- | Minor | Check: NEEDS-LLM |
| --- | Minor | Flags:    not-assessed |
| --- | Minor | SENTENCE (Line 1044, 413 words, 7 clauses)  [Script] |
| --- | Minor | Rx5ÌúL²½",éÚ×x#Ö ¶Ü¬sh4¢3?fdú<ÐÁ&Tëmq ¥»»ârîØ×ÖkÞ@¬ÒzìÉþìÆmòª$îÞÈ |
| --- | Minor | §ÐûÒ"[´Asê,^:íÛ³Æ £[Ú²=i]T±óÕ5%çg¯ .¯uãÀ®ÒÓÑ®<&6ºº»Û\/£Bå¢jv¦l¢R)f³íÜ¹×¤cmAXÌá¼¶æÁîðÖùAê)ñ	Û*r-¿Oô¬ÀìuÐñÖõÑ2SÍôÎÜ¯ØjeÕi¬å0¶Z¶[C«<²¼i¢¦j§ åÊò:ZÝwTF-£+;èÑ^ 5¯pc)ËJ&EU |
| --- | Minor | ©1½iÕì¯'rï´Ïum0Wª¦¼à |
| --- | Minor | Î^p2 ¶ÆÙóÐa	jÂÌUA6¤Ö±÷(x×ºáíÈÒààóB¬øÜÌ¬­Í°¢ÆÐ½¸ÜV	U©ãÑ£8¼SN«SwkªG-¨énïXÎyz¦q1À¯§Ü8pm£[ÂãÞFÂ£7´1Ãòouu'#2ò0Ob,1Ò# ì©ªï#Ïm ÂºÃpT°ÞåRòfÁ4]½ciã.xðv<Äyì\ÞW·k÷n Ý%¸õ~¼æs¢­²B¾R+_"¯F=¯üìÕ¥&cÙµAcÑRº -[HÝôBJ×H%xjÂ<ÉÃ²´äf­AEoOóK¾5*ü2ö¡ª@sY}d@S·¤ÎWÌ*ù®º¢-´Y´T-ç5B]Æ%Oÿ=^z/ûÅl(YwÞ)õ/¤$<,.ÆTÄ2}I?ü¸Éö£ÐSÁ9¿ü{·Zå/¿,÷hÞí¼}Ö4/ZRï5åÈqB"q¼M%Ø_rXe³xÌ®§bS ¢q>Þ0©ºëQîæÝ`»HH2lhë³ÝOÞí}\´ï Î§^ EJ5¤g)úGi"ó9¿N uP].ÝlìQÑsöxJmIqáÙØæÛr}}|êÜçX¯cñð.Þ]]å´3¹£ãfè¡»E 0þÐA×.3uô!²ëÎäùÑ1úc!úBwc[t¤n³¨?¼òCwsæ¡gXçrÇÁµ4ß¥m¶p& ¦àL~4S2	lê[»l£eUTQÏ89%S®¶fàbïúÖÔqÿÐ?gÆ¥{KbÞÐÁ¸7´»æyÓz.RÞäK¥Ýjnõ¸²ÀAébÒ<×ÒsëN( !H×Õoc:êñùÈ2-sãÊ°«àT8ðÒíaÚ[K?fÓòT¾ØÔã#Ý£¤«tCpB(§A²µ-ºñò7'!å ÐwÚ¤¤÷Í%ïtc |
| --- | Minor | @Ë³fÃØ EôQæjþØoÁ¶CÂR; ó¶ª a)ó¡é!Nª{-%snËÄVÚ»©õªc5	¼g«ùÔhÍ7éÛb7"HD®>·®íÆË§íÝ¢ÆU_ó}o:bñ³Ü¼-'Añû×¸/ÞAÿ¢êB þêÓ¢µì^(¢à89eï	m83#b/õÈÙè²ûMXæ£§ß,]Z ä0RËûnÁuîUµéåÊðTÏA?/ÕÙBÃi|×¨xÍÖ<-Ås:%¹@í)Þ±+3|%j¦­Ëë×÷E9ÚªfÂóZýcÛG^î£ú)®>³RÉÆÆÔæ³¶Ó«*,F½ZV¯±¥ÝëÑËwýe~ë¢©uZù-¢SñO_RþÒñx17LNo]«ðã]¦>úlã¯SãõTh¬MÔÍ¶®¤Ù·Ý yiè»å<­;L )Z§?;Àú ºö'å¶4( |
| --- | Minor | »K/îOË¬Óè(ë;ö¼¯3¹kâÑ*.DæÐ¼5SCôÂ3uUÒ¨ZäÃþäåXõ"¾Ssñkx¹3K#Fó\Ì¬Õ\ºÛ! |
| --- | Minor | Rx5ÌúL²½". éÚ×x#Ö ¶Ü¬sh4¢3?fdú<ÐÁ&Tëmq ¥»»ârîØ×ÖkÞ@¬ÒzìÉþìÆmòª$îÞÈ |
| --- | Minor | §ÐûÒ"[´Asê. ^:íÛ³Æ £[Ú²=i]T±óÕ5%çg¯ .¯uãÀ®ÒÓÑ®<&6ºº»Û\/£Bå¢jv¦l¢R)f³íÜ¹×¤cmAXÌá¼¶æÁîðÖùAê)ñ	Û*r-¿Oô¬ÀìuÐñÖõÑ2SÍôÎÜ¯ØjeÕi¬å0¶Z¶[C«<²¼i¢¦j§ åÊò:ZÝwTF-£+;èÑ^ 5¯pc)ËJ&EU |
| --- | Minor | ©1½iÕì¯'rï´Ïum0Wª¦¼à |
| --- | Minor | Î^p2 ¶ÆÙóÐa	jÂÌUA6¤Ö±÷(x×ºáíÈÒààóB¬øÜÌ¬­Í°¢ÆÐ½¸ÜV	U©ãÑ£8¼SN«SwkªG-¨énïXÎyz¦q1À¯§Ü8pm£[ÂãÞFÂ£7´1Ãòouu'#2ò0Ob. 1Ò# ì©ªï#Ïm ÂºÃpT°ÞåRòfÁ4]½ciã.xðv<Äyì\ÞW·k÷n Ý%¸õ~¼æs¢­²B¾R+_"¯F=¯üìÕ¥&cÙµAcÑRº -[HÝôBJ×H%xjÂ<ÉÃ²´äf­AEoOóK¾5*ü2ö¡ª@sY}d@S·¤ÎWÌ*ù®º¢-´Y´T-ç5B]Æ%Oÿ=^z/ûÅl(YwÞ)õ/¤$<. .ÆTÄ2}I?ü¸Éö£ÐSÁ9¿ü{·Zå/¿. ÷hÞí¼}Ö4/ZRï5åÈqB"q¼M%Ø_rXe³xÌ®§bS ¢q>Þ0©ºëQîæÝ`»HH2lhë³ÝOÞí}\´ï Î§^ EJ5¤g)úGi"ó9¿N uP].ÝlìQÑsöxJmIqáÙØæÛr}}|êÜçX¯cñð.Þ]]å´3¹£ãfè¡»E 0þÐA×.3uô!²ëÎäùÑ1úc!úBwc[t¤n³¨?¼òCwsæ¡gXçrÇÁµ4ß¥m¶p& ¦àL~4S2	lê[»l£eUTQÏ89%S®¶fàbïúÖÔqÿÐ?gÆ¥{KbÞÐÁ¸7´»æyÓz.RÞäK¥Ýjnõ¸²ÀAébÒ<×ÒsëN( !H×Õoc:êñùÈ2-sãÊ°«àT8ðÒíaÚ[K?fÓòT¾ØÔã#Ý£¤«tCpB(§A²µ-ºñò7'!å ÐwÚ¤¤÷Í%ïtc |
| --- | Minor | @Ë³fÃØ EôQæjþØoÁ¶CÂR; ó¶ª a)ó¡é!Nª{-%snËÄVÚ»©õªc5	¼g«ùÔhÍ7éÛb7"HD®>·®íÆË§íÝ¢ÆU_ó}o:bñ³Ü¼-'Añû×¸/ÞAÿ¢êB þêÓ¢µì^(¢à89eï	m83#b/õÈÙè²ûMXæ£§ß. ]Z ä0RËûnÁuîUµéåÊðTÏA?/ÕÙBÃi|×¨xÍÖ<-Ås:%¹@í)Þ±+3|%j¦­Ëë×÷E9ÚªfÂóZýcÛG^î£ú)®>³RÉÆÆÔæ³¶Ó«*. F½ZV¯±¥ÝëÑËwýe~ë¢©uZù-¢SñO_RþÒñx17LNo]«ðã]¦>úlã¯SãõTh¬MÔÍ¶®¤Ù·Ý yiè»å<­;L )Z§?;Àú ºö'å¶4( |
| --- | Minor | »K/îOË¬Óè(ë;ö¼¯3¹kâÑ*.DæÐ¼5SCôÂ3uUÒ¨ZäÃþäåXõ"¾Ssñkx¹3K#Fó\Ì¬Õ\ºÛ!. |
| --- | Minor | Sentence exceeds complexity threshold, split for readability. Applying the split needs --strength moderate or higher. |
| --- | Minor | none (split proposal only; source not rewritten) |
| --- | Minor | none |
| --- | Minor | Check: NEEDS-LLM |
| --- | Minor | Flags:    not-assessed |
| --- | Minor | SENTENCE (Line 1044, 808 words, 15 clauses)  [Script] |
| --- | Minor | =®`úºk<(aºg |
| --- | Minor | ¼XÏLÊ#éåç×Ò«sð¤«¡¼2­Ù6l-­ûLd©+kM­ª ·móZä¨-®ðn!×±|hì9Qî"{óR0×Ãã5w«¼#³¦õ°9Ú8[Q;ézÖ^¥¬y5¾õ@05§µ8ÅÕGám/ÊÂ®®$¶4ÞsqçOEfþw¾òxãH9¾FÁÐB¹»w£YtÁõïýY+1ï½±4Úß¶ßÔ|÷ÏTrÆ».Øæ¡9m¹!QÝ´æ |
| --- | Minor | ¢ |
| --- | Minor | O¨Kß2Þ5vhVD(cï¾@Ã<éÙZ=¡WnwºéC£NVV¨Á´v| |
| --- | Minor | )­åDçà®pÆÍfjWÙÃÂ;¯ìæStå÷fHø_Ö`äd=ÙÛ)! ãDXà]³zfKý÷Çßübk[ endstream endobj 377 0 obj <</Filter/FlateDecode/Length 4462>> stream xÚÅM¯·íÞ_±=°QìD"õY¼¼CÑ¦@{ ê[Ó×ë×K4§¢ýõ¥>(QÑî>÷9I`Ø;#QÅoRsúé¤Oþ×''¯ãÓ§O?Ò³Ð?~ÿáôÍwúDo8súðr0ôCÑú2&àéÃõoOJûþ¶úùïþ|úã:Y´Ú¢*4_ûºÊÙÐãL¬ó]x@ëOJ¼ Âó1=u~z>Ó_y,½{©ïUäY/åSé |
| --- | Minor | ÿì æùm,£Óüï+º0/eÕo-`1p¥ såùåWÅH§]ÁKå¯å©PÓßãÜÿE`à\Ê3þÆÅÒY|ó]£Ý¼éôñËÒÏ6£q©KCùÛgrV@óqÑê-;ÐjÜ¬ÀüP©e< 1?1ô}§W¦ò´Ó2*ýBÏ¿"JæÂðÓb÷ ×±¦|¦I]/ý.°Á§ÙñìX3T¦±©4¦ó<¤)¸©Ê7¢úJÀ4*n~EHgö#±Äê^wp¶gpîKèV=CÇ»Ãbpy	¤3U 0ñfÑ=B6>Ü¦#ÒàÝåSÈtYÐ`´ãN^=/UtMAlÇ_ÕKåÕ5B¡Kait.uitÊô»TÉ^e&L9%¼ÇÆç3«GþGåK$­YðP¼* &ðùµ"Fóàq>Ä¶oM¬À2?o1A¶ GUi¿gÛJô<"!)ãåf±id(¡CÃÏIÌZÃèâXW ¬¾ÅÖ2HÕ9A.g]xo/]/Ú4/Í§ËiGw)Õ÷@Ltj§ø.]rëlÕYÝNÚØoÞe «¿ûÏûcð1$ê1z±üºÊ««Ó¨ð43pa@ðtøM`ÔYÜl¤©£éæ#ÁMäÄú'6L*¥ø±8%µÌfjÂÏ¥{á§< |
| --- | Minor | ÞM¥îÙØ |
| --- | Minor |  |Ø	Õcq #K°"!U)¤wÅôñ¬Z÷ZÑÍÆßa LQ¹â¥Í¯j¢j® èYÌº'¨yÛ­	Uö¯C[H6DWZÆÙÖ²r3ª,=3^âðÉ CxTØ<²A+ì]«·³z*OnÑ­BZ yB¦k×ÏÉ!uq4ÇÕÈ%m²Øù»¢	£:»ðÂî[»J.¯ùÊù¬/#4Ígvîvf$ùúR*¿ýÜÞÐî0ð¯ñ ÒS+íGÓÞ7£^%fSa|ÕR	÷a%VõÌfÍ |
| --- | Minor | :°bä¨Iv6«ú5Æ¸Ùè#«i­ãBQ§@ @cÓÔ{ÑjndÿÍ&®Y¹dyãÁ<qðÈÑ\Jëì!è´ó6}ðÊÛÆ¥£³FÐ£ª¼ÐUd ) (A¾4f_ºú~Xü_ÄÛ@o: µ{öR0n®³`¡ì!­³¹»ðS+ HgwÈcw |
| --- | Minor | @F{··FÇ<Oú^¥îyÑè |
| --- | Minor | ¡ º°bXrbþ!9QÍÜHkFU1í<ouVÄKÞldsQªÎù2°ÛÍ#²Ëæ¥¼Î±eóåü*¸4¤½ç@ÐãrPö±ý²EÌÎ9´,ýjErCÎ9{#ÒA«ÇR ÷«H;ÀæúÃ@{¯]8qÍZðÝ,Ø4/ |
| --- | Minor | ·ØèÝïÞ/4ä¦HkÄöûHÁwð ú Ýx  |
| --- | Minor | »DÌ{Ùì ï@jØ³·kDHÿpþ0g<£Ä$hÂÔyÇÕÅïç­?-+Ywú·Dí7k' ¡ÉpËýq®´r6E1[txN9p²øp Gw¡Ç[ï,zu|JËp©ò"{¾))Êé?¶òGæôïÖn¨È^H@NÓéÇSÊêÒ,käãþzú¾È	ÙCrm±+²MÄÎï¸, {Ìß­F%-P¼Õ3NßU\iVvKê¯g¯?ü©AS¤còTlÌ7m	&²ÂãæÛãÇ6oü¦µ÷Íë,ûp³ø±l8iõ¤Mù¨ÌZÿuóÍw <Ø¬½õþ¬­f'Fðu Ë àg 4,9Æý ÁÙ|Zi> |
| --- | Minor | ^rµm´ÄlwÉëÉI é¼þÍÈë*yáíÈkß¼)dõóû0üxLhë7Ä}>¬ 4à1]Hwirq_C¬Æ·£4>@i2^6p14	~N@Å^;Ö"7R¶nHÙ2³÷9Jßj,yS6ã¶4úÍêÀe¾¿_ËÓ(7ôÿÑDAÐp¼=õyÌ¸¸Ðëø8Ñþûf|Ë Øÿò¢ ÅF%!Ó9õ{­¤Zñ/ÓÚÜf þþ©8 ìA9#OE7;û>ÅN¡×op,»µ'*Å@883ý±pfìª=M²gHèFMµCç¤¢t |
| --- | Minor | ©oÒ	§ø®9ªÑ25Ä±s«W)Ë5-jÇ)-N6zá!æ0ìRÉ |
| --- | Minor |  %3Ì¹ú}hå^ÈíEúÊ©dÚ ¾çïy0 ä¬ñÀi-9tþ&¸FÕ-ÛZ×OVpäxiâ¶]wEx« @¾ÕMÐqäéqa·&sZt­CêÇ[÷OsUUò '¯½$õ²w· NpÏkÀ4ª§	dÜ%w1êkØºËî­«ôV	sÞVÇúdÜuOiô»zaG5H]¬&~Ñc½QÕ¢ã|¸°/ÌËªLNT(ËÓ¹BYî*ðN=X¡VÎäpêMkÏ© " ¸½a£ç[¦}	qcVî.ÔÑsÁ¬!$´ |
| --- | Minor | _Ì±Ôx,;³®I[íI,óÁ{3[Ôö´ÉßòüAåj-T)¯¡ÃÝb&(r¤ |
| --- | Minor | ÷«º774YhhÏ0ØìÛ¿ûËºîEq=CÔyg&uAÙ®Qn;½½t×¥nÉÂ¾a 9Äè»àMSy·ø¾f ÙEÉfÚú¬*äòMqrnËeÓRp<¦Ö¼+e¾(õo¯©zaÊ<ÔÈ0Ýä')x×U½×çÑ>:»a'ÛOfV¡]§F~ÛÍ*µ·qsjò|§¬ðïªÕy.S;Èÿ·H¬Û |
| --- | Minor | ²ôÁr¢`î}#õ¢n½ §ÍæãþÑ7Åb×qR v D¸Çp,gWAôeÄª³-ò;¹U!ÂEb¿ª¥¸	};<R÷1ïNxP ô^ÿíåPáånlöÀú:;Uì<úV)²RºµxÛÅMºíýª;ÀÍF û5Zµ[æµèX÷5:">(8©|Ë¥*ôJSCºë¢?¸ôxíý0¥ô2§YY]ÊÏÞ±9À2i¹öõFg¦°òg'½^ö@;íù®OW¡Òuê÷ |
| --- | Minor | {Ç:÷"¥V¶ä¦;)9`î¤Ê;y:Êû*½±»:ð¢ó4ëÏÞ Û¯ËqI´à¾º÷1b¸»£sÐ<øÛ eôØ/%8Îªq[I)Z+åÀ`ÑßÓÇÏ}ïaåÑÍ;íðk:µ |
| --- | Minor | =®`úºk<(aºg |
| --- | Minor | ¼XÏLÊ#éåç×Ò«sð¤«¡¼2­Ù6l-­ûLd©+kM­ª ·móZä¨-®ðn!×±|hì9Qî"{óR0×Ãã5w«¼#³¦õ°9Ú8[Q;ézÖ^¥¬y5¾õ@05§µ8ÅÕGám/ÊÂ®®$¶4ÞsqçOEfþw¾òxãH9¾FÁÐB¹»w£YtÁõïýY+1ï½±4Úß¶ßÔ|÷ÏTrÆ».Øæ¡9m¹!QÝ´æ |
| --- | Minor | ¢ |
| --- | Minor | O¨Kß2Þ5vhVD(cï¾@Ã<éÙZ=¡WnwºéC£NVV¨Á´v| |
| --- | Minor | )­åDçà®pÆÍfjWÙÃÂ;¯ìæStå÷fHø_Ö`äd=ÙÛ)! ãDXà]³zfKý÷Çßübk[ endstream endobj 377 0 obj <</Filter/FlateDecode/Length 4462>> stream xÚÅM¯·íÞ_±=°QìD"õY¼¼CÑ¦@{ ê[Ó×ë×K4§¢ýõ¥>(QÑî>÷9I`Ø;#QÅoRsúé¤Oþ×''¯ãÓ§O?Ò³Ð?~ÿáôÍwúDo8súðr0ôCÑú2&àéÃõoOJûþ¶úùïþ|úã:Y´Ú¢*4_ûºÊÙÐãL¬ó]x@ëOJ¼ Âó1=u~z>Ó_y. ½{©ïUäY/åSé |
| --- | Minor | ÿì æùm. £Óüï+º0/eÕo-`1p¥ såùåWÅH§]ÁKå¯å©PÓßãÜÿE`à\Ê3þÆÅÒY|ó]£Ý¼éôñËÒÏ6£q©KCùÛgrV@óqÑê-;ÐjÜ¬ÀüP©e< 1?1ô}§W¦ò´Ó2*ýBÏ¿"JæÂðÓb÷ ×±¦|¦I]/ý.°Á§ÙñìX3T¦±©4¦ó<¤)¸©Ê7¢úJÀ4*n~EHgö#±Äê^wp¶gpîKèV=CÇ»Ãbpy	¤3U 0ñfÑ=B6>Ü¦#ÒàÝåSÈtYÐ`´ãN^=/UtMAlÇ_ÕKåÕ5B¡Kait.uitÊô»TÉ^e&L9%¼ÇÆç3«GþGåK$­YðP¼* &ðùµ"Fóàq>Ä¶oM¬À2?o1A¶ GUi¿gÛJô<"!)ãåf±id(¡CÃÏIÌZÃèâXW ¬¾ÅÖ2HÕ9A.g]xo/]/Ú4/Í§ËiGw)Õ÷@Ltj§ø.]rëlÕYÝNÚØoÞe «¿ûÏûcð1$ê1z±üºÊ««Ó¨ð43pa@ðtøM`ÔYÜl¤©£éæ#ÁMäÄú'6L*¥ø±8%µÌfjÂÏ¥{á§< |
| --- | Minor | ÞM¥îÙØ |
| --- | Minor |  |Ø	Õcq #K°"!U)¤wÅôñ¬Z÷ZÑÍÆßa LQ¹â¥Í¯j¢j® èYÌº'¨yÛ­	Uö¯C[H6DWZÆÙÖ²r3ª. =3^âðÉ CxTØ<²A+ì]«·³z*OnÑ­BZ yB¦k×ÏÉ!uq4ÇÕÈ%m²Øù»¢	£:»ðÂî[»J.¯ùÊù¬/#4Ígvîvf$ùúR*¿ýÜÞÐî0ð¯ñ ÒS+íGÓÞ7£^%fSa|ÕR	÷a%VõÌfÍ |
| --- | Minor | :°bä¨Iv6«ú5Æ¸Ùè#«i­ãBQ§@ @cÓÔ{ÑjndÿÍ&®Y¹dyãÁ<qðÈÑ\Jëì!è´ó6}ðÊÛÆ¥£³FÐ£ª¼ÐUd ) (A¾4f_ºú~Xü_ÄÛ@o: µ{öR0n®³`¡ì!­³¹»ðS+ HgwÈcw |
| --- | Minor | @F{··FÇ<Oú^¥îyÑè |
| --- | Minor | ¡ º°bXrbþ!9QÍÜHkFU1í<ouVÄKÞldsQªÎù2°ÛÍ#²Ëæ¥¼Î±eóåü*¸4¤½ç@ÐãrPö±ý²EÌÎ9´. ýjErCÎ9{#ÒA«ÇR ÷«H;ÀæúÃ@{¯]8qÍZðÝ. Ø4/ |
| --- | Minor | ·ØèÝïÞ/4ä¦HkÄöûHÁwð ú Ýx  |
| --- | Minor | »DÌ{Ùì ï@jØ³·kDHÿpþ0g<£Ä$hÂÔyÇÕÅïç­?-+Ywú·Dí7k' ¡ÉpËýq®´r6E1[txN9p²øp Gw¡Ç[ï. zu|JËp©ò"{¾))Êé?¶òGæôïÖn¨È^H@NÓéÇSÊêÒ. käãþzú¾È	ÙCrm±+²MÄÎï¸.  {Ìß­F%-P¼Õ3NßU\iVvKê¯g¯?ü©AS¤còTlÌ7m	&²ÂãæÛãÇ6oü¦µ÷Íë. ûp³ø±l8iõ¤Mù¨ÌZÿuóÍw <Ø¬½õþ¬­f'Fðu Ë àg 4. 9Æý ÁÙ|Zi> |
| --- | Minor | ^rµm´ÄlwÉëÉI é¼þÍÈë*yáíÈkß¼)dõóû0üxLhë7Ä}>¬ 4à1]Hwirq_C¬Æ·£4>@i2^6p14	~N@Å^;Ö"7R¶nHÙ2³÷9Jßj. yS6ã¶4úÍêÀe¾¿_ËÓ(7ôÿÑDAÐp¼=õyÌ¸¸Ðëø8Ñþûf|Ë Øÿò¢ ÅF%!Ó9õ{­¤Zñ/ÓÚÜf þþ©8 ìA9#OE7;û>ÅN¡×op. »µ'*Å@883ý±pfìª=M²gHèFMµCç¤¢t |
| --- | Minor | ©oÒ	§ø®9ªÑ25Ä±s«W)Ë5-jÇ)-N6zá!æ0ìRÉ |
| --- | Minor |  %3Ì¹ú}hå^ÈíEúÊ©dÚ ¾çïy0 ä¬ñÀi-9tþ&¸FÕ-ÛZ×OVpäxiâ¶]wEx« @¾ÕMÐqäéqa·&sZt­CêÇ[÷OsUUò '¯½$õ²w· NpÏkÀ4ª§	dÜ%w1êkØºËî­«ôV	sÞVÇúdÜuOiô»zaG5H]¬&~Ñc½QÕ¢ã|¸°/ÌËªLNT(ËÓ¹BYî*ðN=X¡VÎäpêMkÏ© " ¸½a£ç[¦}	qcVî.ÔÑsÁ¬!$´ |
| --- | Minor | _Ì±Ôx. ;³®I[íI. óÁ{3[Ôö´ÉßòüAåj-T)¯¡ÃÝb&(r¤ |
| --- | Minor | ÷«º774YhhÏ0ØìÛ¿ûËºîEq=CÔyg&uAÙ®Qn;½½t×¥nÉÂ¾a 9Äè»àMSy·ø¾f ÙEÉfÚú¬*äòMqrnËeÓRp<¦Ö¼+e¾(õo¯©zaÊ<ÔÈ0Ýä')x×U½×çÑ>:»a'ÛOfV¡]§F~ÛÍ*µ·qsjò|§¬ðïªÕy.S;Èÿ·H¬Û |
| --- | Minor | ²ôÁr¢`î}#õ¢n½ §ÍæãþÑ7Åb×qR v D¸Çp. gWAôeÄª³-ò;¹U!ÂEb¿ª¥¸	};<R÷1ïNxP ô^ÿíåPáånlöÀú:;Uì<úV)²RºµxÛÅMºíýª;ÀÍF û5Zµ[æµèX÷5:">(8©|Ë¥*ôJSCºë¢?¸ôxíý0¥ô2§YY]ÊÏÞ±9À2i¹öõFg¦°òg'½^ö@;íù®OW¡Òuê÷ |
| --- | Minor | {Ç:÷"¥V¶ä¦;)9`î¤Ê;y:Êû*½±»:ð¢ó4ëÏÞ Û¯ËqI´à¾º÷1b¸»£sÐ<øÛ eôØ/%8Îªq[I)Z+åÀ`ÑßÓÇÏ}ïaåÑÍ;íðk:µ. |
| --- | Minor | Sentence exceeds complexity threshold, split for readability. Applying the split needs --strength moderate or higher. |
| --- | Minor | none (split proposal only; source not rewritten) |
| --- | Minor | none |
| --- | Minor | Check: NEEDS-LLM |
| --- | Minor | Flags:    not-assessed |
| --- | Minor | SENTENCE (Line 1103, 960 words, 20 clauses)  [Script] |
| --- | Minor | »Ù_VôÄö¼WºJ1$({vÓ.í¨®!¡Zd«qíËYrYãç| ºGºéÐl RGê½.= |
| --- | Minor | (ºô[×Ex°o,ö¿,AÎÁ¾}O*JÌ d ÇØ,Iã*AÞ °wNýìÙâ.È°®¸W!È£äý#¿¸j6äÂALD±îå2¦¼yXmóñ¾0í[ê<%7¯Â	6oéÿL°ËúgØ( n;ËÑXñ&Bq­ô!úá(&ÂéÎÎ»ß.Y)ÚÆ¼®nd¸mQðº]ð·IÄp¼îëÆÍ´ÐÙâ¥¢'³­ Æ×±·{¸ß;lQßÓùYpP¼1å1_òî-)ïÝã¯FN#ÇÕ5nåé|¦ÅahÕ½\`q/§-G¶/ÄÜ+=ÕÈ:Ý±0ÒN¬¸üutà";e ÃjÕ8Ù =\¹òöâÐ[Ù2 ¬[KA»s=jáÌ$Ç)zkT¿k/ÃíÙÃl¨²¡­lôÓükpB>p19¡dÜsQó-­{·?Ë*cþwq¥ÙÈ IY.Fhì¡ír¹\,êJlýÚÝ¥²eýXûÍìgKÞj{£ÞYÂ1&°"Ã²±ëÄP{|¹ßÊë¦8ºöv¿2Êci9Ô/¨·;ûZ6|	äwZ\úâ«¶ßÆÇþ·X0û-dùö¸õfIDÂ |
| --- | Minor | ±ô:ýæÉÂ;Ng*	i4ØQoíuÒnH á^'¬ |
| --- | Minor | ] ¨ÏîtgÍr]À>þ}3ÒÑY²ïdº¸÷.9Z¢o½ö¯4w |
| --- | Minor | #×Q8¹ñÙ¹ÚO-z[Ð.lÁ;- WùñÑ*È»×âªd­(ÌÁ*¾ü×Íü zªaçwØHN¿ð;[ò54àNßû}'ÑçZíÕ; |
| --- | Minor | @Ñ×p£pÛè#¬7Ät«&sñ­ùµ¼p4¿^`Þ ¦Ûg6oVUô®cDëéOpò8£®Õ=¾×ÚRzÃ®zñËç}¬ÌkçåR.FFÓeµ¾ÌQGÅs}ÔÿÁåÁ}	Ïþ'Çz«Ä{W_úÖå×jð9bÅ}>¥e#§pªéZ]¸Þ¾FÖÐÛÚx|ð^4fG&9Ay-µïxäq~#ÕWfs»g¦K7dÎeâ!~CËâÆò3>x}ãù`ßJ0äL¯#µîÀ`³å_ñ].;;ÜÈî;nÖX²XÞ/»Ö­\¤P|3Ì |
| --- | Minor | ]o#ö/h |
| --- | Minor | ¥£Þ: c9_~Ê®ò`-?¤ðCÉRÊFàË®µ¢æ¥QwL[Æ]å^ì¤×í¹Úåö¬M÷TYJ!¼LZ´ìdõAw@¦ê«` °û$KW`ów__øu¡iüÂ,4Õµj«ÈîpÁÝþònÌ'ÍÍµ¯zw/G×»·;a^y%ªØýþHºïöÐ;5²½nsÖ¹æäÿ×ÉM%ßvòal»Z¾dEçÛÕîA8Àà~i6!9d.HÄ÷Ï>;ù²_ÜBð=/òzð÷¿ú£} endstream endobj 393 0 obj <</Filter/FlateDecode/Length 4980>> stream xÚ½\K ¢²ªûÖ?³|ð±3#ä§.òS|ðÚ¢2k#!ð/=°Sã,±]®ÛÈÏú4jßÀøc&)4G<`í!ÔØ¼¦	Úµ.ïPô ¯/-Ütºà'ªY[=ò>¹/NóîW^ZE¥ö	¿Ùxh53Ög7ÈøRþùLcdÆÔ #åEÒx«ôDH>ÜüÉÚ¢<5óÓL¬Dú+÷¢c­JdwÁnÌ ©½?~I­ì C"û.økÒW>üÊóÓÍ¹ÚìØYdÊ¬~>:_ìÄr² ³ÁdôzTØÖé¨èIa0uî4Y÷¦nº¬È½|ÚX¨õÚ¸(Wê`tUõ86Ú¹ÃzocS>ÂvQ8õH`´¶J,iÕ]z·úÞ5w'ó£;gÕY¡AÓ"'b`íÍV-Æ{LÜùß"3ÉÚ!¹Ë§åFæm£²JÚ]gw¥yæT|óê£ÅNG]t]kòkßýb«å8µK¶Ä&¶\9§KëÙC)úX{:½Éc;mº=­,ryÂäÀJ¢ÉÝ¨¤b£Ø4ÑéÏ8ß:ÃàIªÂjb Guú+©*s³~¦£xyiÇ±!r45¦40·åc)ZLñ Ä~àð![acÿþpU{ª(ËJ,Ó@zRuu{D§Â§;9´\Z,ïò Rãü·éÿü?N2	7ÈùLó?zë?e  }(u!I#Wü¾c.Gèù$@ô¨ÒïsW*6iÇî¸SÃÈ ¤kµö0)»Kë¾¼´!àk1#âsõ |
| --- | Minor | ¶d6ìé¶C,?é	§¢06Ù¯ï¶irG©(ÊÒÓ+©*ÙÙ?aÔÚÃÈ ãb´%Ìàw¾À³gMÀid£Yu¬-wD¹l^µ\=ÖJU¯ª­j%çj«HíéY÷ÔWÛâ5ÅÑ(O0 } |
| --- | Minor | «(¥4 ¯wYÈ,ÌãçJÌmKWDD 3OYð,ÌÜÚù0åÅi®' 'Åë  ZäG¶7Å ø¨íN7 Ã[2pVw¯uNé¤0èØ÷i-mÂºñLk¾¿íà1:%¡¤FTý[2\~É1=Õ¤x:Ðô3«Î¶q± ¯¡hyi¤2cÌä®Þ»*j²¦Ãás	ÎÍ°wÍ-Í&z¸pod/Zéc¾X-HwE¬a·è)mæ!gcÍÁêºVÂêÈÝÃ«kqã]\z8Ô1úBàwùA¾­8¦@®¸ðÝX»<ÍNë¹×rië£9´l}"ômê;9øëµ³ ü¡"ÚuÔh©tóæMRÚ*ÞhÏ½ðg?<J¸î |
| --- | Minor | ¿ªÝäEQ9èù ~Ã¬Å¦Øé¥&ÃkfV?­ü¨px°]Uq}Kï`Ì4·e<¿Á) ¤'C:cÒ¨%x{Vël`¶fNOÓ (dÃÁÎé°0»2¯ÆÅ!­îcFoöôóù»´ç¿ªfp¼k»s.¥o9« |
| --- | Minor | ¥î2}ówñÞ%¶gÙ\\róª¦|¬(§¹gK¾ìó­ðLÄa]ßhÞÚÉ¨1éÝÛK[S.H_z×¬Ïs­*ÓJà¬HG Båc>Éi·nã\) ^½èþ}â¼íêQú1[rpË½ìï) |
| --- | Minor | \ÓÞÌM$åû,«T\ý9Ó±ÚÑ8xÄFÜ)~`/Íå{ª6wgë¨Eujdþ)qÑÂA2ª.ÎT¥1<yß:òGÜì÷U#@Íuë,êz^y2üÐrªûoÒc¤czfí2èxÁP{_I×G2÷Á±¡C8@g×-Ñøè9e¡÷(,4@«qä¼§;KÆ¦ÙÐZø~C¿ÝO ^É'høÄ3´ØìèD¼jçèRðÞû!#Pø9v×~(êTÇSj'.Î5+¥zFY|ÕöAB ¬ZÃ2#7ÖÔ½ã9±õ-ÑþH´K\Ð|!ge)X­ìþ 1ù"I%dFx8­m®êuOK|¿v¬.êÍ¹Øqï¡K¡¹¡a!(=®5`~óY [êÐvSò9C\¨Þ¿ðv¥9e×Z |
| --- | Minor | ¡ÒbêÇlÔ^AºôCmËH8¿¡bsTß êS±÷V{³¤¢µ£¢VL±N¾¼KJý¥Å~	<VèÏêÃõqb5²g£í	M/`ìq5 þ§!HÈÐBGLµhUÎæË |
| --- | Minor | ±g4Ñ6ËÄåðbrZÆ	hnÊéû5	ô¡£V$je¨VÕâÎêgäÉÓGÀ*0Du¿\÷XÕÅZ	éO.i8>¿aþ¿¥×n¨/ÈQs.zOÃ+G Ö¸äqz±ì7íEí&I`ò­wÆ5ó<çE.,ÂZdÄ&ÊÂËõØÂuè×	fZ<Ýé=ÙvH?lôÿ <£¡vG"àt}­ sF{¸ô%wP |
| --- | Minor | #*Uø¡ª,©-qÄ­*oý.\©^+QDÜJý%«ÞÉÚmösG¨EÖzmvþµ:§jPd¦(h°SYsJ#| |
| --- | Minor | Ê¨-JãÆ_Ãi^D:¬0eÌce>{ Ý\Ìkî=µ°É?Hb(âób*#la@wRÏÃÎLMjö£c ùÄ}-Oi £nà2"4îgË¸^ÂU"eF¿F E¿TË/×1wE ¾¨3z	êz¬6B¢n½áe Ò¿^-bKg_ï 0Ñ÷i´)ÍHè Y»löû¼ÜÌïÔãZõç¤e.µ?Äþ¢·£çU3¿Ôp6Á©ÅÁ"_iÛ}ä¢Ø.fíîÖÔÅþjZ­IÇ6­æ,øY:qD¶Ò	Ù>ñõåBM:c$`ø9µ¡Ü4³(:¿á8äM ¼^L1Â'õåÌpSÓ7P:DÔ\Ïä6Ð^®oÎ"ÃèR¾Ý,æ/chd2ÚZÍøè0T¶4÷;ÊFlàP>æ[ ¹x³NÞ&3ÔÃôË)pÔ>æ.Cò"ýí~¹.Ôªl¦òyrówú Þé1Ã|%åZ[!ì3N¯9^ÏÕà<¡çÖÀb~÷s¤! |
| --- | Minor | »Ù_VôÄö¼WºJ1$({vÓ.í¨®!¡Zd«qíËYrYãç| ºGºéÐl RGê½.= |
| --- | Minor | (ºô[×Ex°o. ö¿. AÎÁ¾}O*JÌ d ÇØ. Iã*AÞ °wNýìÙâ.È°®¸W!È£äý#¿¸j6äÂALD±îå2¦¼yXmóñ¾0í[ê<%7¯Â	6oéÿL°ËúgØ( n;ËÑXñ&Bq­ô!úá(&ÂéÎÎ»ß.Y)ÚÆ¼®nd¸mQðº]ð·IÄp¼îëÆÍ´ÐÙâ¥¢'³­ Æ×±·{¸ß;lQßÓùYpP¼1å1_òî-)ïÝã¯FN#ÇÕ5nåé|¦ÅahÕ½\`q/§-G¶/ÄÜ+=ÕÈ:Ý±0ÒN¬¸üutà";e ÃjÕ8Ù =\¹òöâÐ[Ù2 ¬[KA»s=jáÌ$Ç)zkT¿k/ÃíÙÃl¨²¡­lôÓükpB>p19¡dÜsQó-­{·?Ë*cþwq¥ÙÈ IY.Fhì¡ír¹\. êJlýÚÝ¥²eýXûÍìgKÞj{£ÞYÂ1&°"Ã²±ëÄP{|¹ßÊë¦8ºöv¿2Êci9Ô/¨·;ûZ6|	äwZ\úâ«¶ßÆÇþ·X0û-dùö¸õfIDÂ |
| --- | Minor | ±ô:ýæÉÂ;Ng*	i4ØQoíuÒnH á^'¬ |
| --- | Minor | ] ¨ÏîtgÍr]À>þ}3ÒÑY²ïdº¸÷.9Z¢o½ö¯4w |
| --- | Minor | #×Q8¹ñÙ¹ÚO-z[Ð.lÁ;- WùñÑ*È»×âªd­(ÌÁ*¾ü×Íü zªaçwØHN¿ð;[ò54àNßû}'ÑçZíÕ; |
| --- | Minor | @Ñ×p£pÛè#¬7Ät«&sñ­ùµ¼p4¿^`Þ ¦Ûg6oVUô®cDëéOpò8£®Õ=¾×ÚRzÃ®zñËç}¬ÌkçåR.FFÓeµ¾ÌQGÅs}ÔÿÁåÁ}	Ïþ'Çz«Ä{W_úÖå×jð9bÅ}>¥e#§pªéZ]¸Þ¾FÖÐÛÚx|ð^4fG&9Ay-µïxäq~#ÕWfs»g¦K7dÎeâ!~CËâÆò3>x}ãù`ßJ0äL¯#µîÀ`³å_ñ].;;ÜÈî;nÖX²XÞ/»Ö­\¤P|3Ì |
| --- | Minor | ]o#ö/h |
| --- | Minor | ¥£Þ: c9_~Ê®ò`-?¤ðCÉRÊFàË®µ¢æ¥QwL[Æ]å^ì¤×í¹Úåö¬M÷TYJ!¼LZ´ìdõAw@¦ê«` °û$KW`ów__øu¡iüÂ. 4Õµj«ÈîpÁÝþònÌ'ÍÍµ¯zw/G×»·;a^y%ªØýþHºïöÐ;5²½nsÖ¹æäÿ×ÉM%ßvòal»Z¾dEçÛÕîA8Àà~i6!9d.HÄ÷Ï>;ù²_ÜBð=/òzð÷¿ú£} endstream endobj 393 0 obj <</Filter/FlateDecode/Length 4980>> stream xÚ½\K ¢²ªûÖ?³|ð±3#ä§.òS|ðÚ¢2k#!ð/=°Sã. ±]®ÛÈÏú4jßÀøc&)4G<`í!ÔØ¼¦	Úµ.ïPô ¯/-Ütºà'ªY[=ò>¹/NóîW^ZE¥ö	¿Ùxh53Ög7ÈøRþùLcdÆÔ #åEÒx«ôDH>ÜüÉÚ¢<5óÓL¬Dú+÷¢c­JdwÁnÌ ©½?~I­ì C"û.økÒW>üÊóÓÍ¹ÚìØYdÊ¬~>:_ìÄr² ³ÁdôzTØÖé¨èIa0uî4Y÷¦nº¬È½|ÚX¨õÚ¸(Wê`tUõ86Ú¹ÃzocS>ÂvQ8õH`´¶J. iÕ]z·úÞ5w'ó£;gÕY¡AÓ"'b`íÍV-Æ{LÜùß"3ÉÚ!¹Ë§åFæm£²JÚ]gw¥yæT|óê£ÅNG]t]kòkßýb«å8µK¶Ä&¶\9§KëÙC)úX{:½Éc;mº=­. ryÂäÀJ¢ÉÝ¨¤b£Ø4ÑéÏ8ß:ÃàIªÂjb Guú+©*s³~¦£xyiÇ±!r45¦40·åc)ZLñ Ä~àð![acÿþpU{ª(ËJ. Ó@zRuu{D§Â§;9´\Z. ïò Rãü·éÿü?N2	7ÈùLó?zë?e  }(u!I#Wü¾c.Gèù$@ô¨ÒïsW*6iÇî¸SÃÈ ¤kµö0)»Kë¾¼´!àk1#âsõ |
| --- | Minor | ¶d6ìé¶C. ?é	§¢06Ù¯ï¶irG©(ÊÒÓ+©*ÙÙ?aÔÚÃÈ ãb´%Ìàw¾À³gMÀid£Yu¬-wD¹l^µ\=ÖJU¯ª­j%çj«HíéY÷ÔWÛâ5ÅÑ(O0 } |
| --- | Minor | «(¥4 ¯wYÈ. ÌãçJÌmKWDD 3OYð. ÌÜÚù0åÅi®' 'Åë  ZäG¶7Å ø¨íN7 Ã[2pVw¯uNé¤0èØ÷i-mÂºñLk¾¿íà1:%¡¤FTý[2\~É1=Õ¤x:Ðô3«Î¶q± ¯¡hyi¤2cÌä®Þ»*j²¦Ãás	ÎÍ°wÍ-Í&z¸pod/Zéc¾X-HwE¬a·è)mæ!gcÍÁêºVÂêÈÝÃ«kqã]\z8Ô1úBàwùA¾­8¦@®¸ðÝX»<ÍNë¹×rië£9´l}"ômê;9øëµ³ ü¡"ÚuÔh©tóæMRÚ*ÞhÏ½ðg?<J¸î |
| --- | Minor | ¿ªÝäEQ9èù ~Ã¬Å¦Øé¥&ÃkfV?­ü¨px°]Uq}Kï`Ì4·e<¿Á) ¤'C:cÒ¨%x{Vël`¶fNOÓ (dÃÁÎé°0»2¯ÆÅ!­îcFoöôóù»´ç¿ªfp¼k»s.¥o9« |
| --- | Minor | ¥î2}ówñÞ%¶gÙ\\róª¦|¬(§¹gK¾ìó­ðLÄa]ßhÞÚÉ¨1éÝÛK[S.H_z×¬Ïs­*ÓJà¬HG Båc>Éi·nã\) ^½èþ}â¼íêQú1[rpË½ìï) |
| --- | Minor | \ÓÞÌM$åû. «T\ý9Ó±ÚÑ8xÄFÜ)~`/Íå{ª6wgë¨Eujdþ)qÑÂA2ª.ÎT¥1<yß:òGÜì÷U#@Íuë. êz^y2üÐrªûoÒc¤czfí2èxÁP{_I×G2÷Á±¡C8@g×-Ñøè9e¡÷(. 4@«qä¼§;KÆ¦ÙÐZø~C¿ÝO ^É'høÄ3´ØìèD¼jçèRðÞû!#Pø9v×~(êTÇSj'.Î5+¥zFY|ÕöAB ¬ZÃ2#7ÖÔ½ã9±õ-ÑþH´K\Ð|!ge)X­ìþ 1ù"I%dFx8­m®êuOK|¿v¬.êÍ¹Øqï¡K¡¹¡a!(=®5`~óY [êÐvSò9C\¨Þ¿ðv¥9e×Z |
| --- | Minor | ¡ÒbêÇlÔ^AºôCmËH8¿¡bsTß êS±÷V{³¤¢µ£¢VL±N¾¼KJý¥Å~	<VèÏêÃõqb5²g£í	M/`ìq5 þ§!HÈÐBGLµhUÎæË |
| --- | Minor | ±g4Ñ6ËÄåðbrZÆ	hnÊéû5	ô¡£V$je¨VÕâÎêgäÉÓGÀ*0Du¿\÷XÕÅZ	éO.i8>¿aþ¿¥×n¨/ÈQs.zOÃ+G Ö¸äqz±ì7íEí&I`ò­wÆ5ó<çE.. ÂZdÄ&ÊÂËõØÂuè×	fZ<Ýé=ÙvH?lôÿ <£¡vG"àt}­ sF{¸ô%wP |
| --- | Minor | #*Uø¡ª. ©-qÄ­*oý.\©^+QDÜJý%«ÞÉÚmösG¨EÖzmvþµ:§jPd¦(h°SYsJ#| |
| --- | Minor | Ê¨-JãÆ_Ãi^D:¬0eÌce>{ Ý\Ìkî=µ°É?Hb(âób*#la@wRÏÃÎLMjö£c ùÄ}-Oi £nà2"4îgË¸^ÂU"eF¿F E¿TË/×1wE ¾¨3z	êz¬6B¢n½áe Ò¿^-bKg_ï 0Ñ÷i´)ÍHè Y»löû¼ÜÌïÔãZõç¤e.µ?Äþ¢·£çU3¿Ôp6Á©ÅÁ"_iÛ}ä¢Ø.fíîÖÔÅþjZ­IÇ6­æ. øY:qD¶Ò	Ù>ñõåBM:c$`ø9µ¡Ü4³(:¿á8äM ¼^L1Â'õåÌpSÓ7P:DÔ\Ïä6Ð^®oÎ"ÃèR¾Ý. æ/chd2ÚZÍøè0T¶4÷;ÊFlàP>æ[ ¹x³NÞ&3ÔÃôË)pÔ>æ.Cò"ýí~¹.Ôªl¦òyrówú Þé1Ã|%åZ[!ì3N¯9^ÏÕà<¡çÖÀb~÷s¤!. |
| --- | Minor | Sentence exceeds complexity threshold, split for readability. Applying the split needs --strength moderate or higher. |
| --- | Minor | none (split proposal only; source not rewritten) |
| --- | Minor | none |
| --- | Minor | Check: NEEDS-LLM |
| --- | Minor | Flags:    not-assessed |
| --- | Minor | SENTENCE (Line 1103, 64 words, 2 clauses)  [Script] |
| --- | Minor | CëeTÒgáà -y0âY éáà¾z)c4,F?	ùÈÍí}lú:²¹{x¸Ð9M |
| --- | Minor | ;[e >B£-.Y¶Êëm{~/6½­ªÿZ	ßÈ"0µsÏQ¼Øl[=~pd 7¹9´¶/Â>½ÖÖÎÒåk=Nå;¾ÊkS1ß1Ì?æºVÏ{æocZæ¼;åòWíò·'æLd	ëGÀ8®îyp÷~ÿóê^«,Ðqì§Àà´îC+×FFØÚæ>Ø$ìôtóÙªÏ¿Üá ß>VuÿÍjÖï66Q_ûäÕõ_DTöÓ¾®? |
| --- | Minor | CëeTÒgáà -y0âY éáà¾z)c4. F?	ùÈÍí}lú:²¹{x¸Ð9M |
| --- | Minor | ;[e >B£-.Y¶Êëm{~/6½­ªÿZ	ßÈ"0µsÏQ¼Øl[=~pd 7¹9´¶/Â>½ÖÖÎÒåk=Nå;¾ÊkS1ß1Ì?æºVÏ{æocZæ¼;åòWíò·'æLd	ëGÀ8®îyp÷~ÿóê^«. Ðqì§Àà´îC+×FFØÚæ>Ø$ìôtóÙªÏ¿Üá ß>VuÿÍjÖï66Q_ûäÕõ_DTöÓ¾®?. |
| --- | Minor | Sentence exceeds complexity threshold, split for readability. Applying the split needs --strength moderate or higher. |
| --- | Minor | none (split proposal only; source not rewritten) |
| --- | Minor | none |
| --- | Minor | Check: NEEDS-LLM |
| --- | Minor | Flags:    not-assessed |
| --- | Minor | SENTENCE (Line 1103, 1842 words, 36 clauses)  [Script] |
| --- | Minor | ÁÆ;"þ3ÌüÐ§	¥÷Ó'XÐy'£G÷[èZ¨ß_*m¯b2ñá#J{év5	Î)I ÿ²},_hS1þ#jEöµZn°}·¢N¾ùßsiKÓÑ KÃ¢â¶Z.i¼Bº#)á'í"«¸YÕÝÌëë D~ç:¥Wù]ÑDcHÁ1fÓ{à»ú·ÿëþü|.ß endstream endobj 402 0 obj <</Filter/FlateDecode/Length 4100>> stream xÚ½\Ic¹ |
| --- | Minor |   ^ w§ü= îï*Ü"Ó·<ÿ'øBKk'ê7¸Q{¦ úÀk§þ> |
| --- | Minor | ´ç76|~8(sÏÿzhó5ÞæÜ×Þhu7ú¸÷K]>4iK îIæU#ÐohLÜ§E§òq/øáYêLc!63d¦ð¦XS_q¡óKCMÕ5%^(´¸Ê)Õw	î©Ï43Ï³;ïõ ÿQk§,ï`9å)ÏZ¸Uyù¥ÓyË êÌWÔª®­ÈÒûX!í4ÞÅ"Tä'èù[ÙÅ[çfoò-ïi>G|*ÒN¿}õù |
| --- | Minor | ëc=Ïóù+¯¯]R*å(E¶,ÎË,¤-«,â9+ "&¹µbBÞÅT¹ï|¡ý*®F)õ÷IÞª)è¬YÖçfÔç:$KÑbZTZËïÌOµíìa¬±¾¶úãOûÑðP»º¶²?ímH8Tp¨ÕuÒf:ÕÄ6umoê Yo6M\øTVùoÕäMóB4³u¯ã8Öái¿4ú¡e];zÕY#O*Ñò7«üà§>ô-¥¶¬"Ymç~}û¦ÝKæÛ»:/Ó±s®VMUÑl¹ÉÆÜè`g&ÁMG`^ÌµÖ¶SQTÑÉ¬Ú&n¢ï­ýaRX£YW-Ï{ït×oÌ®Ì¢ÅÐéKE±é·~gÐ4 ±üÖÑ@ÚtY/ÆE¿á)[63-j #m>Ý~(ÄhW7Þ(	´Xº~ü3`v»ÙÉhf;iÿéìÕþÍGË6¶|T©¬ª4E£Üå.(Ø? |
| --- | Minor | mÒÞî]8¤ªKÛ@Tlf.³ñ.í¼PÏð U4¢E¡ SÎC16 ´FÝ»ÊÆ8G=Ù<¦ñpl«ÍªEØ$6Ôªiâã7í0Ð¨±ÓíZoÃMØIÊ!Ü0´`,¤å@´I ¦Äa:^Þ¯j»ë'ÏÌzje*íÞôQÙÑR«;ì[ôufÍ{e¼8¬>.«_ÄÀÔc8u´ø*?ª7ç]d´L½øcÛÕ0ijÌ|ì4îWY±Ý®²·I»Ü K_¬ËÖ ~ôý¨}]_¾DÚâÆ ÐÓ*¡ãú&ÓnPU©#zoÄÂE|5¿¦IRh>d¦-zÊ¤#=Ù¾ }ÁËÕOmë¹&Â©è¼Juý¬>¢W1VôêþÑlÿubâ~H(üÎ©ßPè:¢`»!7jýb |
| --- | Minor | &¼ªÂNÍ¶NYjýb=¼òÀ<cä {,M?z-¢-uÇIÏÚ«[Ýzh­ï>/¥¨¯ËUeÐt±_=õF'¬¬í.tñfõ¨èÛvnR\Ï x:kSèò%yó.?ñÇO¿øtíkìC; kòËî-¸²rÔ*O S8éØÏÆÛnn# |
| --- | Minor | ³Na=vw6ìtÏQÕVqWv¸´x~ªÚÐúÄ¥õÐ>m8ÓA: bÓAß\'|6s¦¹nukëÓf8Ë·¦Ø¢  Æ«j Ã6ÚªÙ¡×÷ |
| --- | Minor | Ç&MSÃuæ1öLéÑ O^;%fÂÿR¥c;3öm vnOBuôPú3¾®&>âtº nÑÿ«1ç;Ï(èÚ¹vÃ¾Ð y³£q>í	Ñ©°Ó¡pGDWÎdË5¤CS-¬ÕÜHUa"Àª¸gêÊ sS©ÅæÊöæ  ë]pvÉ º~Lz®Ùùí:â¯¬vnI­I­×,hù Øò+m~z¶sxßF_ÆÀÉlL [æ¦¨å.Qv¼íÐH¿E@üÕYöNvv¬U«Ú#âFæBeL·è[/×Õdg6þÁNüv¾=b¦[Ö¢Z§^DLiÁVSX1[Ò%ø3[C_ékèO/È ÞØ²ÚJ¤2XñÓzÀPwÏ~,Xü6bÙ5Ó}DÂ@u³ðéNîpîÂYpW¤&\¶Ë¾ÁÂWIX8·%-+j+¤Òã©pGÆê]Jî«Øê'´×Û¿~Ø®øY À~Oó	,)âÊtx"´ó«Pêì-âmL¸×ØRÈY,(ø,®Çí9|Û¾±ä&8!²=cµ=E%üIHº¶Kd¤WjÚvOüû}²/òdó*¹ |
| --- | Minor | 8ùfÍZä·Kú³UÒ,9ðÒ%vþ	¶DÇXªDoÜþkÔÓ°Xmêç¥ùi«!SÃS=2ÅzÙ'¹ÉS.e.¬ùñ/ïIÏ=`ÜÒ8YgTë0¨ðiLÞ¨È.zäÂ¿²ytáÔ_t8=Ât¸)D¾ù¤áüm~Jív³û	1è­ÿ|3Bgú'µ¼ø;ÓæQÄï÷ê,~8Ñ/ÅâYCÊYp¢CÖaeicrþºDbgu:ìâ«4HåÙ'¨DÏró_Â {b¬fgâÄ5;#ÆQ"ÌvaKÒ-Z^D-Mç:¢Þ |
| --- | Minor | ¡ÝKìÁ-Ç|¬ßMÚâóQI°vg!*LuÑj7¹ÆÓ:ÎuÁDH6niÏi£:,!«ìßÜôÄæoàå¢oc.f®X'ßûb½ïÌ£ZÎz Ý¸¹¤/ûUeßg¿97/' |
| --- | Minor | ¸ÔÖðÇP6vÌ6Àã°¤ÑÌKåHhÇÅ¥µ<yVÊïÖU-éÌ0¨³Á}¾BpxÜv^=WOOòX³+>gMZC\¬æ­ÕnJgôQYt\_ÃcÆùçø´,á¥Ä/p8 |
| --- | Minor | JCG@°v0n¼k"jngï$µ¬A¹-âhôlÙ uæ­ÀÓ\{þ'PÌ\öþ>êÅÌYvÊ(»ÇÕnâóâëzv¬zRrT# mæ`Õ}ºN Ø=Xð\Ëò%ò@­L[®Fµ9ÎÐ*ìrÞ­rÀY@»,,\à§~ë´º§È-zd²±®½Éôf®L5KagMO2+ç5çq­1GXJA ®² |
| --- | Minor | OéÙmø%:¶ød8dÎzÕX¶yg½Øv`Õ vP |
| --- | Minor |  Iy2wä|<*U0ÄóPÿ¾:ó>sM©¿x÷n@¢EF.@]EHL\¢QáÑãâý ²Ô_iÎ¡yH7¢¶D$âÊ§ç(«lõjêõÚQO°ìÓäZBÁp%?Á±sS¦£âzø?ÜÆz¿RÎÿ¤=)x<®Ew ôýnÁ±á>}ÛÞÇ¡WÓ}:ÝÛ§L-yv"ÒmÔP¶//¦´¹Î*w*é·1ÈÓÞímOÂõªÀäZoÑ{sá³ZsgÈÊ÷ÔV>^Ü·)~c)n1Í?ÅNÃ%$êÛÍêÚ;¿Úøí»éDRN]åÙVoiynÙ_é[ËS	õEì[ÞêÕ3ûú Âãt®§%Îôí.[EuéVQo»©àFQ¯=ÜÎCíõ[µ&9 `8ÃN.G.ó»ä_éÉ?ùÑ÷¨È=µ»}j0]¬Ã¶« ¸ÚÿúÅH´!_Õn_×x8.®=Y¯:ºÖT»8SNÖn<¸iY^(yK&ÏºHC$»¦£«s¢0Á¢	CÁnVÖVáTxÒë«N(²î0à¢Ýç[èrTdË¶Z¥M:Fés¯ÎÅ6¬Eø;VW(ÒÞXõÃ5BB'¦'Rª½°¦+ |
| --- | Minor | ÝÉ,gTußÙýj5ÖVD=TPê»Ì=ÀxÎFØÎ5sHí<ø§7~è®ûWå²ÜÝÆÛpq½åk¦æCg où;<þ'_Æ7H'53G°-±\n½ºI<ýZè@ó×gl<À¹¥<næ^	}^)®5¯8ÂõqWÔ¿§ôìª¤«ýÿÐOÒl<^ï¦ GÐA»Aw$Å¶Ü'tÁ±Õ*¿}µpºæÌ`¬§:X¯Pãµ_ú=ô6_¢+#Åÿ¶æCÃ¦Kö¾ï~>#76UÿøÍÿ ®V>q endstream endobj 407 0 obj <</Filter/FlateDecode/Length 664>> stream xÚUË®1Ýóù	±8t5$@bÔbq§eX±àÿ7ØN<{¯ Õ(ÓÄãs×ývàÁtoòq×_¼÷ÏîÃÅ½ÿO)¹Ëê k#ÉjtÛ·§¨òfy¿ñü´R^yykÄßÙ×y¥°>÷±W=íV7uùôwsêï3 |
| --- | Minor | ¸Ìß/_=8¾j& Ô ÀM9úJ9µQÆI¡áÃÙGÜQuèÕJFúÁ^%Ê^½aW&p¯Olïë3«ÝbiEµ¯bS8i®½ê |
| --- | Minor | }P«ªv¨qèi [;YPBR¦['ÁàDxñìvh·E6OÝth"æVÝÐÍñ©- f-Z Suë(T?©{Â@ªHbY£g%qT+8b'F.¬ZËD 9w[ÅÉ¶ßìjBx±Î´)s©hSwe-á_OUígVÒF«ÑmÌ²G:IAÍ((GúM´Ócõh&á±w9ÍÏ¢#mí®{ÈÁçîågP£\Ò¾£~³(lÐ%ìÇËkwÖæ!f ä´@Fãë^-É4É~ ×WýX ð/¶7üx§ZèÁÑØïzhë¡7îWª_³Ð_£5Uû)¥DQÇÖòÒPìKÍm¿®¤¿Ìåå<íôFSß×;BÃ~ÜÙ;Æ}Úþ×TÄ×4z=®Ûx±{¢}ùÅû>´ìÚ¼koéãÝå;Ã.-ÇÝ$ÿ24£«vñýð·ËCÎ¨TYõ<VHaâÙzæë»?Dv®£ endstream endobj 410 0 obj <</Filter/FlateDecode/Length 119>> stream xÚ]Ë» ÂPàÝ§ø_Àc¦9'P:*t².*:9ôý#ÔÅV0(Q½ø7pçíuÁ1p83òcbxBDs¡9jëy Ò~½çq	§ØðöBÜ¬boF¥ª[Û¼Ý:ÿÙëîQo" endstream endobj 419 0 obj <</Filter/FlateDecode/Length 3478>> stream xÚÝ[K$9¾ó+òF·Ppø½[ÓiHÃâ°½H]]Û#ØÓÂøíDØéô#ÓUY=fÔªªL§çÎé»IN@ÿåäpr2Àÿ¦çtí=ýýzúù»é§¿Ý±hõôîe ñÁN¨híÕôîüõÀzúüýLH@<Ñ']CúT/ FòXúNcðåá £§ð)ÝáÊÑg¼F-O#öózñ]5:}ç9õ<Z¾y÷%Q¯&)E0FZÏô¤Ä¸9Þæ-Èy*£iÞÇ²òK×ñ |
| --- | Minor | ~÷DûÏó¾1ï&ÒñÅ»r ðéf¦ ­,àÂÏÇ4*ÇÏ»W|Õøüp0 üÖqyñêá¿D|éaÍÛJ,â_p,ÂÈ¬&!VwË¿Ü9KÍW³¨ùÉÈË1OéO+EZ2Sòg\+n(p#ë ýÅíQÎ«Éçe]L+0kâîNEü,C¢0_bËp¥Ï rãI' 5Ì¢O)Ò§¢VIZLBæz©vùÎbHñJTæSÒ¾Ã\²ñõLY<*m7?ËæÙ´¯¨[ÖRßÔ,Håy¶¤8ÏmdÒÆV,eêóþ"½2êiÕ³7~ÃDâóÆ ¼C§ôô=9TRÈàÉ» [&ËÄÆ,»mj2r±J<g/ßÎkU4ílão·'#R-ëÅ2[kºl¶êXø¤ÓÙ¨ãÝsâj4âp¨9\<jü©Úò¸½&2]pÌ"¤4Q®wò63^'·%¥÷¤V,Ë¼¨!Leänþf{FtÂ CyláÑBOÏ7a¶i?Û´»fÓ&òÓUÐµÈ6i§z¶sùWt+ÊØÎNg1Å)çÀdMÍá1 JaKcÅ7q røÐ®l­Û»´=,9³´ÍãF)×jÈ²ÎÚç+)à@SÂPqa/ÛjÁÈ5Ðú®Õçm>+?Á¨ôBKAû@Õ*FFwÑ]ôyC DfS¨¾áïÔ·}¦Å×æýëÖ	ÇSlõ¹=ÞÁý&£È©Í<ìóûÍÙ({	Æ©y|¼¿0Ý Ø¥ÖLÿ×Èòæ¢1þtLZÒÐê	¹M2 |
| --- | Minor | È:úõ6ÁÜàUg¯·ûóäj2ßlSCó_÷+*édã0î¾8G­Ï@7ä¬ü1%© gtÎÓmg;(É:¶¾x¢v Âì|ÿ# (¨pÎÉ,ï,;7Í	@ÚßBt@|¶\÷k C"H ¤` |
| --- | Minor | ,waHD$ÈI&ñûmu²ôÍ-SyáÈEÖ1:¬àÇKAÖHR«°O¥ª9°<Â^oÛ9"ÏÞ>­Ûç¨bùfw1}êRõ´ ¶Eß¿T^2îü4¤Ì¥Æ=¼Ý}ÆÞ~<'HgÝ-âÂâuË÷sº|Þ¬îóQc6I]K'¼É<À¶âRËYx)åu.)4þtj¿/a'ïÈÀAUi¾=/ÜV+ÉäªÞ |
| --- | Minor | 0°k½+ï¡%­Üíªì×¯Å­cÝí6Wsößæç³/ïUL÷sìö´c" 7§µ²ÜD>4ÛL"~:éðÆD»ÏtñÞàL#Oÿ( JØ:»¡]Ì±då |
| --- | Minor | ¯*AIyµ²UÞÝØªÉhÕS³¢'Ùt{Þ´ÞÞ¨	MæòÔÜlgFRM¤,t/Í\àKÉçíg¸¾xd ¨tQU&êêD<o ÔÇh4¡U? T¤<¯ #uü`g°+÷³Aå`²äJÚ5(4è@" (åò.¢è+ÁTfíøÛÌqÂ°7MÀí´màT¢ |
| --- | Minor | "®"óÔ ¥Ê÷9ªÔnÛ½ÞY1¬îÎ¸Ûê2#ã±MÎÞpdÓdAJ î~vîî¿ &Kç6Ù­l·!ÔPóØÎH6(Ñ² |
| --- | Minor | Þ0üIÄ»?Þ£¿{;ÐMëï<!\²}iüeiËÁLõÐ1*%fh3Ï>RI ¿rõ-ªJ "w³BÑê?¥T¥:ø¾ÁJeûäÆæd´¼Â(âÅò:YX6¿o<ò èñ0?TExXº#²ÊKÇl¸­¶vñ®÷Áéó°O»ú6ÓW_l3}d.ÿa>ÊtPÕVY/-hýràÎI¬q§2²R9yi½õÇ6d¸;.Ô9Rè[ zðA¾*Z\nO½Nã^¤¹«<ú*u[e  m¨Ômgiv´9oöpðqÔ8rÁa®êh	*ç |
| --- | Minor | êû	­á>çÐ*X"RiîÔ+÷õå1¬fÑ@>ÚYu0íö@RÜt¸+ujÛµ&Wâ½ùfM@Fí¥TCc./Â¶÷×k¥ZMµ7¿ÑõÌ	©°èÖnm<£íê¼¼L¾Äç»C¥	»äÌ-KI¬^JÌò/{êí5#m¯4[X&Øëíi	dxíÊ¬î>er¤<Z­Ë"óýë¶±Ìq®Î~T­H=qßvÑZéÖ(Av´YíÀÞbÁm+HË^ôÃ¦'ys²MJµè~2*Kê ÿÄOi2i\:dt÷ï#9icÍëÀ[>Á¹¶?Õâëªd	|Úàc<Ó¶ö oÌ¢¼E}»UPr±QQ?¬Î°j[íq»D%ë^â2òMåxºi¹k@ÿ¶¦Õ×¦]¢M7g65äøÉõÔÞ;Å©£$ålÊ~PÑB¨G°ÝA´Âú×vaÄZg¬4½?ê»4Ò:EVyw%oÖ ëtpfcs{ wHÙZ e}é]VÑAïºÅ» PÀ<¨Ù+ëýåÅ $MÛVÌÊå]3í¥ teývtî) Ú}%Ë-SèJ9bÄÞÜ9§ä¤ãZ`éøt&t.Q«ÏiÉÜ7³	¿«û@Ç|sNæFTt£g;ÜÔx?*Òª QßvÁÿ×ã¯P¿µíÝÍÇÏ©Ç<boëÍ»xJ»«,å°]êÜÞ çÊgö0q<[úÎOU¿k¿½\Hõ3v×ÐÇ\GÑ´©Un5²nÉo÷ýÎfµÁr§.ò^w,bO#t­ÊX¤[ÚZ}ìKÇ)¦ÂMEc¼?uAO»,|¨§Õ{LPAX¢aâ½Ô®üÑÆ"vÕ¹ÿá!@ÄG}GU:ªtÊÜØQýë ±qÙyÎØ;®^½Q/Å¨¸ñl«u {E}¿ÔJÌuÁ§õiúÜeNsï9½iÏí9#ÅÃ´û¼º |
| --- | Minor | '¬{â2R´ÖÃËQ¥ËzÛ6>K}¨öcTÐ"ò©&4¹¡+­Ñåàô¹>Þ¾ì¡×ÕüOöãåm[G)³Wg¾ÖÐñPòúÐÀæ*¹¸£¹_£<`¢ôéuJÓNw¬«Ô©=Ù±`ÃSýjË¨±T$Z^zª=.#ÄV'!ß?¨ ¡p7v®â¬n=MOÕËå]XÝ¥ìplöÆzt\GAík ÏÃî?åY^¯U<×Â¾ÃÆ2w6F½ÜaXÞqÒò¸GôÐ_^×Ye¦ STVÅµüªQI.l¥ã\Ô/¯áåéÜxnéw½¥Ñ+\jÂ¥t{ïY,Zv'}. |
| --- | Minor | ÁÆ;"þ3ÌüÐ§	¥÷Ó'XÐy'£G÷[èZ¨ß_*m¯b2ñá#J{év5	Î)I ÿ²}. _hS1þ#jEöµZn°}·¢N¾ùßsiKÓÑ KÃ¢â¶Z.i¼Bº#)á'í"«¸YÕÝÌëë D~ç:¥Wù]ÑDcHÁ1fÓ{à»ú·ÿëþü|.ß endstream endobj 402 0 obj <</Filter/FlateDecode/Length 4100>> stream xÚ½\Ic¹ |
| --- | Minor |   ^ w§ü= îï*Ü"Ó·<ÿ'øBKk'ê7¸Q{¦ úÀk§þ> |
| --- | Minor | ´ç76|~8(sÏÿzhó5ÞæÜ×Þhu7ú¸÷K]>4iK îIæU#ÐohLÜ§E§òq/øáYêLc!63d¦ð¦XS_q¡óKCMÕ5%^(´¸Ê)Õw	î©Ï43Ï³;ïõ ÿQk§. ï`9å)ÏZ¸Uyù¥ÓyË êÌWÔª®­ÈÒûX!í4ÞÅ"Tä'èù[ÙÅ[çfoò-ïi>G|*ÒN¿}õù |
| --- | Minor | ëc=Ïóù+¯¯]R*å(E¶. ÎË. ¤-«. â9+ "&¹µbBÞÅT¹ï|¡ý*®F)õ÷IÞª)è¬YÖçfÔç:$KÑbZTZËïÌOµíìa¬±¾¶úãOûÑðP»º¶²?ímH8Tp¨ÕuÒf:ÕÄ6umoê Yo6M\øTVùoÕäMóB4³u¯ã8Öái¿4ú¡e];zÕY#O*Ñò7«üà§>ô-¥¶¬"Ymç~}û¦ÝKæÛ»:/Ó±s®VMUÑl¹ÉÆÜè`g&ÁMG`^ÌµÖ¶SQTÑÉ¬Ú&n¢ï­ýaRX£YW-Ï{ït×oÌ®Ì¢ÅÐéKE±é·~gÐ4 ±üÖÑ@ÚtY/ÆE¿á)[63-j #m>Ý~(ÄhW7Þ(	´Xº~ü3`v»ÙÉhf;iÿéìÕþÍGË6¶|T©¬ª4E£Üå.(Ø? |
| --- | Minor | mÒÞî]8¤ªKÛ@Tlf.³ñ.í¼PÏð U4¢E¡ SÎC16 ´FÝ»ÊÆ8G=Ù<¦ñpl«ÍªEØ$6Ôªiâã7í0Ð¨±ÓíZoÃMØIÊ!Ü0´`. ¤å@´I ¦Äa:^Þ¯j»ë'ÏÌzje*íÞôQÙÑR«;ì[ôufÍ{e¼8¬>.«_ÄÀÔc8u´ø*?ª7ç]d´L½øcÛÕ0ijÌ|ì4îWY±Ý®²·I»Ü K_¬ËÖ ~ôý¨}]_¾DÚâÆ ÐÓ*¡ãú&ÓnPU©#zoÄÂE|5¿¦IRh>d¦-zÊ¤#=Ù¾ }ÁËÕOmë¹&Â©è¼Juý¬>¢W1VôêþÑlÿubâ~H(üÎ©ßPè:¢`»!7jýb |
| --- | Minor | &¼ªÂNÍ¶NYjýb=¼òÀ<cä {. M?z-¢-uÇIÏÚ«[Ýzh­ï>/¥¨¯ËUeÐt±_=õF'¬¬í.tñfõ¨èÛvnR\Ï x:kSèò%yó.?ñÇO¿øtíkìC; kòËî-¸²rÔ*O S8éØÏÆÛnn# |
| --- | Minor | ³Na=vw6ìtÏQÕVqWv¸´x~ªÚÐúÄ¥õÐ>m8ÓA: bÓAß\'|6s¦¹nukëÓf8Ë·¦Ø¢  Æ«j Ã6ÚªÙ¡×÷ |
| --- | Minor | Ç&MSÃuæ1öLéÑ O^;%fÂÿR¥c;3öm vnOBuôPú3¾®&>âtº nÑÿ«1ç;Ï(èÚ¹vÃ¾Ð y³£q>í	Ñ©°Ó¡pGDWÎdË5¤CS-¬ÕÜHUa"Àª¸gêÊ sS©ÅæÊöæ  ë]pvÉ º~Lz®Ùùí:â¯¬vnI­I­×. hù Øò+m~z¶sxßF_ÆÀÉlL [æ¦¨å.Qv¼íÐH¿E@üÕYöNvv¬U«Ú#âFæBeL·è[/×Õdg6þÁNüv¾=b¦[Ö¢Z§^DLiÁVSX1[Ò%ø3[C_ékèO/È ÞØ²ÚJ¤2XñÓzÀPwÏ~. Xü6bÙ5Ó}DÂ@u³ðéNîpîÂYpW¤&\¶Ë¾ÁÂWIX8·%-+j+¤Òã©pGÆê]Jî«Øê'´×Û¿~Ø®øY À~Oó. )âÊtx"´ó«Pêì-âmL¸×ØRÈY. (ø. ®Çí9|Û¾±ä&8!²=cµ=E%üIHº¶Kd¤WjÚvOüû}²/òdó*¹ |
| --- | Minor | 8ùfÍZä·Kú³UÒ. 9ðÒ%vþ	¶DÇXªDoÜþkÔÓ°Xmêç¥ùi«!SÃS=2ÅzÙ'¹ÉS.e.¬ùñ/ïIÏ=`ÜÒ8YgTë0¨ðiLÞ¨È.zäÂ¿²ytáÔ_t8=Ât¸)D¾ù¤áüm~Jív³û	1è­ÿ|3Bgú'µ¼ø;ÓæQÄï÷ê. ~8Ñ/ÅâYCÊYp¢CÖaeicrþºDbgu:ìâ«4HåÙ'¨DÏró_Â {b¬fgâÄ5;#ÆQ"ÌvaKÒ-Z^D-Mç:¢Þ |
| --- | Minor | ¡ÝKìÁ-Ç|¬ßMÚâóQI°vg!*LuÑj7¹ÆÓ:ÎuÁDH6niÏi£:. !«ìßÜôÄæoàå¢oc.f®X'ßûb½ïÌ£ZÎz Ý¸¹¤/ûUeßg¿97/' |
| --- | Minor | ¸ÔÖðÇP6vÌ6Àã°¤ÑÌKåHhÇÅ¥µ<yVÊïÖU-éÌ0¨³Á}¾BpxÜv^=WOOòX³+>gMZC\¬æ­ÕnJgôQYt\_ÃcÆùçø´. á¥Ä/p8 |
| --- | Minor | JCG@°v0n¼k"jngï$µ¬A¹-âhôlÙ uæ­ÀÓ\{þ'PÌ\öþ>êÅÌYvÊ(»ÇÕnâóâëzv¬zRrT# mæ`Õ}ºN Ø=Xð\Ëò%ò@­L[®Fµ9ÎÐ*ìrÞ­rÀY@». \à§~ë´º§È-zd²±®½Éôf®L5KagMO2+ç5çq­1GXJA ®² |
| --- | Minor | OéÙmø%:¶ød8dÎzÕX¶yg½Øv`Õ vP |
| --- | Minor |  Iy2wä|<*U0ÄóPÿ¾:ó>sM©¿x÷n@¢EF.@]EHL\¢QáÑãâý ²Ô_iÎ¡yH7¢¶D$âÊ§ç(«lõjêõÚQO°ìÓäZBÁp%?Á±sS¦£âzø?ÜÆz¿RÎÿ¤=)x<®Ew ôýnÁ±á>}ÛÞÇ¡WÓ}:ÝÛ§L-yv"ÒmÔP¶//¦´¹Î*w*é·1ÈÓÞímOÂõªÀäZoÑ{sá³ZsgÈÊ÷ÔV>^Ü·)~c)n1Í?ÅNÃ%$êÛÍêÚ;¿Úøí»éDRN]åÙVoiynÙ_é[ËS	õEì[ÞêÕ3ûú Âãt®§%Îôí.[EuéVQo»©àFQ¯=ÜÎCíõ[µ&9 `8ÃN.G.ó»ä_éÉ?ùÑ÷¨È=µ»}j0]¬Ã¶« ¸ÚÿúÅH´!_Õn_×x8.®=Y¯:ºÖT»8SNÖn<¸iY^(yK&ÏºHC$»¦£«s¢0Á¢	CÁnVÖVáTxÒë«N(²î0à¢Ýç[èrTdË¶Z¥M:Fés¯ÎÅ6¬Eø;VW(ÒÞXõÃ5BB'¦'Rª½°¦+ |
| --- | Minor | ÝÉ. gTußÙýj5ÖVD=TPê»Ì=ÀxÎFØÎ5sHí<ø§7~è®ûWå²ÜÝÆÛpq½åk¦æCg où;<þ'_Æ7H'53G°-±\n½ºI<ýZè@ó×gl<À¹¥<næ^	}^)®5¯8ÂõqWÔ¿§ôìª¤«ýÿÐOÒl<^ï¦ GÐA»Aw$Å¶Ü'tÁ±Õ*¿}µpºæÌ`¬§:X¯Pãµ_ú=ô6_¢+#Åÿ¶æCÃ¦Kö¾ï~>#76UÿøÍÿ ®V>q endstream endobj 407 0 obj <</Filter/FlateDecode/Length 664>> stream xÚUË®1Ýóù	±8t5$@bÔbq§eX±àÿ7ØN<{¯ Õ(ÓÄãs×ývàÁtoòq×_¼÷ÏîÃÅ½ÿO)¹Ëê k#ÉjtÛ·§¨òfy¿ñü´R^yykÄßÙ×y¥°>÷±W=íV7uùôwsêï3 |
| --- | Minor | ¸Ìß/_=8¾j& Ô ÀM9úJ9µQÆI¡áÃÙGÜQuèÕJFúÁ^%Ê^½aW&p¯Olïë3«ÝbiEµ¯bS8i®½ê |
| --- | Minor | }P«ªv¨qèi [;YPBR¦['ÁàDxñìvh·E6OÝth"æVÝÐÍñ©- f-Z Suë(T?©{Â@ªHbY£g%qT+8b'F.¬ZËD 9w[ÅÉ¶ßìjBx±Î´)s©hSwe-á_OUígVÒF«ÑmÌ²G:IAÍ((GúM´Ócõh&á±w9ÍÏ¢#mí®{ÈÁçîågP£\Ò¾£~³(lÐ%ìÇËkwÖæ!f ä´@Fãë^-É4É~ ×WýX ð/¶7üx§ZèÁÑØïzhë¡7îWª_³Ð_£5Uû)¥DQÇÖòÒPìKÍm¿®¤¿Ìåå<íôFSß×;BÃ~ÜÙ;Æ}Úþ×TÄ×4z=®Ûx±{¢}ùÅû>´ìÚ¼koéãÝå;Ã.-ÇÝ$ÿ24£«vñýð·ËCÎ¨TYõ<VHaâÙzæë»?Dv®£ endstream endobj 410 0 obj <</Filter/FlateDecode/Length 119>> stream xÚ]Ë» ÂPàÝ§ø_Àc¦9'P:*t².*:9ôý#ÔÅV0(Q½ø7pçíuÁ1p83òcbxBDs¡9jëy Ò~½çq	§ØðöBÜ¬boF¥ª[Û¼Ý:ÿÙëîQo" endstream endobj 419 0 obj <</Filter/FlateDecode/Length 3478>> stream xÚÝ[K$9¾ó+òF·Ppø½[ÓiHÃâ°½H]]Û#ØÓÂøíDØéô#ÓUY=fÔªªL§çÎé»IN@ÿåäpr2Àÿ¦çtí=ýýzúù»é§¿Ý±hõôîe ñÁN¨híÕôîüõÀzúüýLH@<Ñ']CúT/ FòXúNcðåá £§ð)ÝáÊÑg¼F-O#öózñ]5:}ç9õ<Z¾y÷%Q¯&)E0FZÏô¤Ä¸9Þæ-Èy*£iÞÇ²òK×ñ |
| --- | Minor | ~÷DûÏó¾1ï&ÒñÅ»r ðéf¦ ­. àÂÏÇ4*ÇÏ»W|Õøüp0 üÖqyñêá¿D|éaÍÛJ. â_p. ÂÈ¬&!VwË¿Ü9KÍW³¨ùÉÈË1OéO+EZ2Sòg\+n(p#ë ýÅíQÎ«Éçe]L+0kâîNEü. C¢0_bËp¥Ï rãI' 5Ì¢O)Ò§¢VIZLBæz©vùÎbHñJTæSÒ¾Ã\²ñõLY<*m7?ËæÙ´¯¨[ÖRßÔ. Håy¶¤8ÏmdÒÆV. eêóþ"½2êiÕ³7~ÃDâóÆ ¼C§ôô=9TRÈàÉ» [&ËÄÆ. »mj2r±J<g/ßÎkU4ílão·'#R-ëÅ2[kºl¶êXø¤ÓÙ¨ãÝsâj4âp¨9\<jü©Úò¸½&2]pÌ"¤4Q®wò63^'·%¥÷¤V. Ë¼¨!Leänþf{FtÂ CyláÑBOÏ7a¶i?Û´»fÓ&òÓUÐµÈ6i§z¶sùWt+ÊØÎNg1Å)çÀdMÍá1 JaKcÅ7q røÐ®l­Û»´=. 9³´ÍãF)×jÈ²ÎÚç+)à@SÂPqa/ÛjÁÈ5Ðú®Õçm>+?Á¨ôBKAû@Õ*FFwÑ]ôyC DfS¨¾áïÔ·}¦Å×æýëÖ	ÇSlõ¹=ÞÁý&£È©Í<ìóûÍÙ({	Æ©y|¼¿0Ý Ø¥ÖLÿ×Èòæ¢1þtLZÒÐê	¹M2 |
| --- | Minor | È:úõ6ÁÜàUg¯·ûóäj2ßlSCó_÷+*édã0î¾8G­Ï@7ä¬ü1%© gtÎÓmg;(É:¶¾x¢v Âì|ÿ# (¨pÎÉ. ï. ;7Í	@ÚßBt@|¶\÷k C"H ¤` |
| --- | Minor | . waHD$ÈI&ñûmu²ôÍ-SyáÈEÖ1:¬àÇKAÖHR«°O¥ª9°<Â^oÛ9"ÏÞ>­Ûç¨bùfw1}êRõ´ ¶Eß¿T^2îü4¤Ì¥Æ=¼Ý}ÆÞ~<'HgÝ-âÂâuË÷sº|Þ¬îóQc6I]K'¼É<À¶âRËYx)åu.)4þtj¿/a'ïÈÀAUi¾=/ÜV+ÉäªÞ |
| --- | Minor | 0°k½+ï¡%­Üíªì×¯Å­cÝí6Wsößæç³/ïUL÷sìö´c" 7§µ²ÜD>4ÛL"~:éðÆD»ÏtñÞàL#Oÿ( JØ:»¡]Ì±då |
| --- | Minor | ¯*AIyµ²UÞÝØªÉhÕS³¢'Ùt{Þ´ÞÞ¨	MæòÔÜlgFRM¤. t/Í\àKÉçíg¸¾xd ¨tQU&êêD<o ÔÇh4¡U? T¤<¯ #uü`g°+÷³Aå`²äJÚ5(4è@" (åò.¢è+ÁTfíøÛÌqÂ°7MÀí´màT¢ |
| --- | Minor | "®"óÔ ¥Ê÷9ªÔnÛ½ÞY1¬îÎ¸Ûê2#ã±MÎÞpdÓdAJ î~vîî¿ &Kç6Ù­l·!ÔPóØÎH6(Ñ² |
| --- | Minor | Þ0üIÄ»?Þ£¿{;ÐMëï<!\²}iüeiËÁLõÐ1*%fh3Ï>RI ¿rõ-ªJ "w³BÑê?¥T¥:ø¾ÁJeûäÆæd´¼Â(âÅò:YX6¿o<ò èñ0?TExXº#²ÊKÇl¸­¶vñ®÷Áéó°O»ú6ÓW_l3}d.ÿa>ÊtPÕVY/-hýràÎI¬q§2²R9yi½õÇ6d¸;.Ô9Rè[ zðA¾*Z\nO½Nã^¤¹«<ú*u[e  m¨Ômgiv´9oöpðqÔ8rÁa®êh	*ç |
| --- | Minor | êû	­á>çÐ*X"RiîÔ+÷õå1¬fÑ@>ÚYu0íö@RÜt¸+ujÛµ&Wâ½ùfM@Fí¥TCc./Â¶÷×k¥ZMµ7¿ÑõÌ	©°èÖnm<£íê¼¼L¾Äç»C¥	»äÌ-KI¬^JÌò/{êí5#m¯4[X&Øëíi	dxíÊ¬î>er¤<Z­Ë"óýë¶±Ìq®Î~T­H=qßvÑZéÖ(Av´YíÀÞbÁm+HË^ôÃ¦'ys²MJµè~2*Kê ÿÄOi2i\:dt÷ï#9icÍëÀ[>Á¹¶?Õâëªd	|Úàc<Ó¶ö oÌ¢¼E}»UPr±QQ?¬Î°j[íq»D%ë^â2òMåxºi¹k@ÿ¶¦Õ×¦]¢M7g65äøÉõÔÞ;Å©£$ålÊ~PÑB¨G°ÝA´Âú×vaÄZg¬4½?ê»4Ò:EVyw%oÖ ëtpfcs{ wHÙZ e}é]VÑAïºÅ» PÀ<¨Ù+ëýåÅ $MÛVÌÊå]3í¥ teývtî) Ú}%Ë-SèJ9bÄÞÜ9§ä¤ãZ`éøt&t.Q«ÏiÉÜ7³	¿«û@Ç|sNæFTt£g;ÜÔx?*Òª QßvÁÿ×ã¯P¿µíÝÍÇÏ©Ç<boëÍ»xJ»«. å°]êÜÞ çÊgö0q<[úÎOU¿k¿½\Hõ3v×ÐÇ\GÑ´©Un5²nÉo÷ýÎfµÁr§.ò^w. bO#t­ÊX¤[ÚZ}ìKÇ)¦ÂMEc¼?uAO». |¨§Õ{LPAX¢aâ½Ô®üÑÆ"vÕ¹ÿá!@ÄG}GU:ªtÊÜØQýë ±qÙyÎØ;®^½Q/Å¨¸ñl«u {E}¿ÔJÌuÁ§õiúÜeNsï9½iÏí9#ÅÃ´û¼º |
| --- | Minor | '¬{â2R´ÖÃËQ¥ËzÛ6>K}¨öcTÐ"ò©&4¹¡+­Ñåàô¹>Þ¾ì¡×ÕüOöãåm[G)³Wg¾ÖÐñPòúÐÀæ*¹¸£¹_£<`¢ôéuJÓNw¬«Ô©=Ù±`ÃSýjË¨±T$Z^zª=.#ÄV'!ß?¨ ¡p7v®â¬n=MOÕËå]XÝ¥ìplöÆzt\GAík ÏÃî?åY^¯U<×Â¾ÃÆ2w6F½ÜaXÞqÒò¸GôÐ_^×Ye¦ STVÅµüªQI.l¥ã\Ô/¯áåéÜxnéw½¥Ñ+\jÂ¥t{ïY. Zv'}.. |
| --- | Minor | Sentence exceeds complexity threshold, split for readability. Applying the split needs --strength moderate or higher. |
| --- | Minor | none (split proposal only; source not rewritten) |
| --- | Minor | none |
| --- | Minor | Check: NEEDS-LLM |
| --- | Minor | Flags:    not-assessed |
| --- | Minor | SENTENCE (Line 1103, 522 words, 4 clauses)  [Script] |
| --- | Minor | ª jßÙIéÓ5¹ÌIÖ¹}] çò"nòå3&[>?§^Ú.Ô!L¾)Ü±ã·¿lìòódËÊæ\D Òs}0å°>kS´¼wööGÿ_X endstream endobj 430 0 obj <</Filter/FlateDecode/Length 3759>> stream xÚ½[Ëns¹ |
| --- | Minor | ÷)ü9#QwÀÈ¢@§@wþ]ÑEÇ]uÑ÷ßTâE¢t{Ìÿ9>(üxÍé'{2õ{JpJ¶l¥ýwúüo}öúó÷Ó_~ûÝê7¢?ýº |ýÅTúã}v§_×ñárýöýß¿þqúÛ/"v'k·¹ÛÄ¼AÙ2<ÜqP}FCþj\øLK[{²f+¦¼¬Ì"k;ZÏ~ÒzÞó¿óûó¶¾aÛüÓ¾io'xt7+×ö6ðÛþ"ëÉþÀ>e7¢óõê ZÏgs¡Oá=ÃyÐ5^Ô²ÚMÈ~ñÚ Ì7ÆÐòåàÏoÚ17v<n¢üí÷2ë¸sq«ê §Vî÷`Èö^Õ>ëN3¬`ÏtdÚoî,"]ãâmìº\ilò/ô?ªÞ!ð1d8ìX7×Y{ó¾¢­Ï­ÒNÆöÙèúMd¡mBt0o0|àØw £Ëm´Ñ |
| --- | Minor | Ãz*b»ÒïÿÁºÐ¯8æ|Fo²íwÜ` ÖÄ1¶æÃYÜäêO}Ëecí'ß__q¹?Mä¿êg ÍBB5°³ºÅ²®¡¾ø	óçÅæ]%ënö ìô¾±!±a_lÆrmÚ zÒ	¯º­1®>@ùÚ5y>§X¯5¶ÅOòfUs&Ghæ[L¿Ô+1~K1ÕÒ¥4F¥,ÌqÛ§qéÌ@[Ôr(>=G{Fpl¼©Ûºð:;ÁË}1ôe6=ÓÌå¬ü¤45kZúfÈi³Õºýq«èóê¶Ìæ;áüþÄ70C<·¬&h6x'â[Û~78åå¯BX«Ïôið]²¶ |
| --- | Minor | .ì¹^Íð½²¯Û° ßÊCm]Î"f\(¤gjrFä ¿Æ%	ð/¢åc!T}äÖÙ-V7{-UéêÙ[ì -³]Õ°á-æÙ'6­1H`&hÓ´|pKÂ@å*ÞµµÇfçÃ;ßE»X9<Ü¯}¤DÄ²³ç=ÚàMZ*ktn'=&U³¶èêÿUîÞnÉÅ¢	û·	òÎ¯+¨ÁXØKv'I¡1ª ¬Ñàgj!_ã¿¾±û´e­¯¼°A®IÇ@êCÊÈA\ÄNìÕ¿ùçXÍ1 -&y:bxRÞR=xê¹Ð)*OÔ&Iè  |
| --- | Minor | ±ºÁØ3±qÆ«^Ðóî6~r\@CÝ{t#×à¬NvðØ×ùöâ'>Ü×8 ì'(Ã{öØ¢¹9¨?Û«?²`#¥E-óß¿1+å¤p½~ |
| --- | Minor | Ú¹cn¸xRY£	Q<é³Ü_²h=Z<S4l¸DÀ"WôëV¯'ÚÑÆÎMñ6Ìz |
| --- | Minor | C[ÂêÀÀÉýº6H§§Í×ü")#'\¨8¡¤Ý³~Øgtàâyïå®ê¡sÁÂ¿Á¶Æ²ªW.ÊõÓ |
| --- | Minor | "ß f^c^§ÁU°o!¤ ±]Ïª«´Cßcda²§È¤â9¾æ¿ïæ¸ôBÀ®Á^CÃjÎÝIvrÝÂ§\!ûB~S 9@¿{Þ3Ú6_ãêFÀÍñ8û:¿'åqÏµ¸Pèö\?íÀÃÏ¡_T(äµõ@ÆE`Ðë±,G©XnAÅÅÑ®A)¾/ûtEöññÑ{QGUb+ÄÐiÈä±à"ô¸Z¯ÅÏ¸60Üm·¤wþN¨Ér¢	Òíjw3£ËC¥ÝFÍ0	iÐ7x¿©âDßúM}¤ò!ßKIÓ]Ö`/þrrl65Ö©è+ ME9ö è7Í²	e¬:°b¬û/NÕË@ªü×¨ÚuXQ< |
| --- | Minor | ®B¡åÁâ8÷ZC	vz*-%·*ú:#~¼Ånõnl| ÎWBqt#kùßí¢t\Âú§Ï³ EJêS¡MJÓ~@`{Ö à¿%ªâ¶ú½äaÔ`\Ö¬¹8Ò|*;óêØ¤^z·÷JïNeÕ´¾TD=½ïbÙ^í%ÿ÷ñ5­1û%´ô:NßÄ,aÍ¢*s£¨ç9òÅ )Ê7KÕútéJ}RE÷n#¾+o§¸Ä0*MB+Éâ{LÄ!l¥ÖQkT±oªPTáÔ½* ÇüåbvºkHYxìÓ2ím |
| --- | Minor | "²>áÿÜ&{ëÂ< ¬ '¢îÂ5Ì6=±q¿AÚbÀ4¿ksÀý	ñãB¥Ägy#ÇñYûÍìö\? |
| --- | Minor | ª jßÙIéÓ5¹ÌIÖ¹}] çò"nòå3&[>?§^Ú.Ô!L¾)Ü±ã·¿lìòódËÊæ\D Òs}0å°>kS´¼wööGÿ_X endstream endobj 430 0 obj <</Filter/FlateDecode/Length 3759>> stream xÚ½[Ëns¹ |
| --- | Minor | ÷)ü9#QwÀÈ¢@§@wþ]ÑEÇ]uÑ÷ßTâE¢t{Ìÿ9>(üxÍé'{2õ{JpJ¶l¥ýwúüo}öúó÷Ó_~ûÝê7¢?ýº |ýÅTúã}v§_×ñárýöýß¿þqúÛ/"v'k·¹ÛÄ¼AÙ2<ÜqP}FCþj\øLK[{²f+¦¼¬Ì"k;ZÏ~ÒzÞó¿óûó¶¾aÛüÓ¾io'xt7+×ö6ðÛþ"ëÉþÀ>e7¢óõê ZÏgs¡Oá=ÃyÐ5^Ô²ÚMÈ~ñÚ Ì7ÆÐòåàÏoÚ17v<n¢üí÷2ë¸sq«ê §Vî÷`Èö^Õ>ëN3¬`ÏtdÚoî. "]ãâmìº\ilò/ô?ªÞ!ð1d8ìX7×Y{ó¾¢­Ï­ÒNÆöÙèúMd¡mBt0o0|àØw £Ëm´Ñ |
| --- | Minor | Ãz*b»ÒïÿÁºÐ¯8æ|Fo²íwÜ` ÖÄ1¶æÃYÜäêO}Ëecí'ß__q¹?Mä¿êg ÍBB5°³ºÅ²®¡¾ø	óçÅæ]%ënö ìô¾±!±a_lÆrmÚ zÒ	¯º­1®>@ùÚ5y>§X¯5¶ÅOòfUs&Ghæ[L¿Ô+1~K1ÕÒ¥4F¥. ÌqÛ§qéÌ@[Ôr(>=G{Fpl¼©Ûºð:;ÁË}1ôe6=ÓÌå¬ü¤45kZúfÈi³Õºýq«èóê¶Ìæ;áüþÄ70C<·¬&h6x'â[Û~78åå¯BX«Ïôið]²¶ |
| --- | Minor | .ì¹^Íð½²¯Û° ßÊCm]Î"f\(¤gjrFä ¿Æ%	ð/¢åc!T}äÖÙ-V7{-UéêÙ[ì -³]Õ°á-æÙ'6­1H`&hÓ´|pKÂ@å*ÞµµÇfçÃ;ßE»X9<Ü¯}¤DÄ²³ç=ÚàMZ*ktn'=&U³¶èêÿUîÞnÉÅ¢	û·	òÎ¯+¨ÁXØKv'I¡1ª ¬Ñàgj!_ã¿¾±û´e­¯¼°A®IÇ@êCÊÈA\ÄNìÕ¿ùçXÍ1 -&y:bxRÞR=xê¹Ð)*OÔ&Iè  |
| --- | Minor | ±ºÁØ3±qÆ«^Ðóî6~r\@CÝ{t#×à¬NvðØ×ùöâ'>Ü×8 ì'(Ã{öØ¢¹9¨?Û«?²`#¥E-óß¿1+å¤p½~ |
| --- | Minor | Ú¹cn¸xRY£	Q<é³Ü_²h=Z<S4l¸DÀ"WôëV¯'ÚÑÆÎMñ6Ìz |
| --- | Minor | C[ÂêÀÀÉýº6H§§Í×ü")#'\¨8¡¤Ý³~Øgtàâyïå®ê¡sÁÂ¿Á¶Æ²ªW.ÊõÓ |
| --- | Minor | "ß f^c^§ÁU°o!¤ ±]Ïª«´Cßcda²§È¤â9¾æ¿ïæ¸ôBÀ®Á^CÃjÎÝIvrÝÂ§\!ûB~S 9@¿{Þ3Ú6_ãêFÀÍñ8û:¿'åqÏµ¸Pèö\?íÀÃÏ¡_T(äµõ@ÆE`Ðë±. G©XnAÅÅÑ®A)¾/ûtEöññÑ{QGUb+ÄÐiÈä±à"ô¸Z¯ÅÏ¸60Üm·¤wþN¨Ér¢	Òíjw3£ËC¥ÝFÍ0	iÐ7x¿©âDßúM}¤ò!ßKIÓ]Ö`/þrrl65Ö©è+ ME9ö è7Í²	e¬:°b¬û/NÕË@ªü×¨ÚuXQ< |
| --- | Minor | ®B¡åÁâ8÷ZC	vz*-%·*ú:#~¼Ånõnl| ÎWBqt#kùßí¢t\Âú§Ï³ EJêS¡MJÓ~@`{Ö à¿%ªâ¶ú½äaÔ`\Ö¬¹8Ò|*;óêØ¤^z·÷JïNeÕ´¾TD=½ïbÙ^í%ÿ÷ñ5­1û%´ô:NßÄ. aÍ¢*s£¨ç9òÅ )Ê7KÕútéJ}RE÷n#¾+o§¸Ä0*MB+Éâ{LÄ!l¥ÖQkT±oªPTáÔ½* ÇüåbvºkHYxìÓ2ím |
| --- | Minor | "²>áÿÜ&{ëÂ< ¬ '¢îÂ5Ì6=±q¿AÚbÀ4¿ksÀý	ñãB¥Ägy#ÇñYûÍìö\?. |
| --- | Minor | Sentence exceeds complexity threshold, split for readability. Applying the split needs --strength moderate or higher. |
| --- | Minor | none (split proposal only; source not rewritten) |
| --- | Minor | none |
| --- | Minor | Check: NEEDS-LLM |
| --- | Minor | Flags:    not-assessed |
| --- | Minor | SENTENCE (Line 1103, 379 words, 5 clauses)  [Script] |
| --- | Minor | o\¶l¡7PákÄGÞ&=	PF9 ÐGJ£pI+kÖõEY¯¥ùÚIÚÂ©÷ÍTà£ phØÿ£¢P |
| --- | Minor | &r*vw×âH«Ã*:ëû÷o{yÕ9eY¢³ÝhÔ:þÚÞ¡0DÚ´Ô¬ÙeBßÜsmÎ¬2!{swæfèl7Ï.&Ít³ïp=¿W÷éï¶ðl×/ìV=XÉï/sWÐEÏÎVz>ÓÇ º`¯!~¼+ÞIVé¥«Ðèìèà¨²OÐ:|iìÙ»¥,ý\ÝOª<káY |
| --- | Minor | áù¼ì+à¦÷aÛv»^ÀãXB{í²çÆµ(î©(e9¥êPØ¾ñ´½ì¤LGÄ3©Ûç2JgóP	»§ôÐÝxþf9öëPÔà¸ùøÌ:ã1y®Ë~RÛ£Çk·ûÃbúc®Ll¿c9N¥ý.¸[Ájz?\¢k×àÂµk\ä½WóÕ±Ú¨}eøh¿¾"n; Ø'¯(¼±®qbÉ¢¹;ªHõ¶Ê*©&Â!¸Døh(KRdrÑN*ocæjÐËDHoÐ®Í¹8FzúEÜvÇn^ÊV©u´:,ÁÛÍ#pMß¼:E)¢[c5¬å1©ú#ÃZDùê°Vqù º¨´´6nW13×EÞ`?LåÊ7ÃTñÎ0l4{}öÃ§úOø±É2ûV.á¹|7`æÓVóì¦d>Í¦hË«`kl_bÂÄTGuK7]&STß|¬4G?Ï´kêCáZ»c|&JõhNýûÉò)û >"[[ñÙAü9·¦®Zð«ÛÃ'wÀ7Vmc6ü>UÕkÁ%<ýÆS\ ×ñ';Oât[¾È ð£Ê5àPè+kHz¢¶_kØ¸ñô±ìþF¨ïÌ³8Fífò÷<è®RÕMD¢?*^ó9¾ö³QD'á¿HD*(<CäfAÍßVÑýç¾s+XÓB}¬zZ[ÿ,lR·n'*R½vªô(c\(Ô'_KfJI«^bfÖatIÁ*Q}\ÇIÖÙî)+5ëÔÛü7Hã°$1BYqÔôwáæ{å¦fN[*P>ouéL³¢×¢íEó×­Fämt\ê£Ú­÷]ÜôZªæ{í/Uâò;zár Ù÷hÞ×¬V¡Èç±ÿñ£¹WúÌ.P¸á5éaîe¾5°87¯ò2'ÕµI |
| --- | Minor | K§ÖZÇ÷±/óôzÉDÛy¸ª±ûõì§	RÓu-§[F±6ÎvÖqÜJêts§´ë&XÍ+h×á|PãÓQë	\´53æºûXQj+èoâ Mn@ÂÈ?Æ_¯¶ Éde(LOÛòßo§Sã°óÌ°ÆxW&¬¹=Ò$\CpkJà?óÍiúÁÄÏÿó/ÿM endstream endobj 443 0 obj <</Filter/FlateDecode/Length 3580>> stream xÚÅ[Éc» |
| --- | Minor | +üu£y ZHd wAårû­²Èÿo"N"u=Vå¥Ó |
| --- | Minor | £ìk¢(ñ<ÿ>øÿý¡Cõ}ëðïðù¯ñì·ñúëáO?ü?oJ(éðãrðÑm¹õris)µxøqþÇÑ¹ÒÆË½ïÏãÆ«;sþ4þgaüç²¶ãýh.ïo±ÖÑ+|Ð7Ð2Öñ¿¥V³wÖÇÃoÆÓè=ÈLÜ:Þÿùão ½?x·u×]k07ïü6zçxxËqk%§ÎsÈÛ_eóµ%ÐñçÍ§=è<Ç=	 àT=X¥½·pä¤sàFç ¦¨2eì-R¤ÃZ¤2û³¥fÔ*v¼ôÉp?1ÿìDHo4êe|Å>(ý¤®ª/ÎÓó7'Û09\7"nÃö,°h£>¬GJ²Qà,Ì! |
| --- | Minor | o\¶l¡7PákÄGÞ&=	PF9 ÐGJ£pI+kÖõEY¯¥ùÚIÚÂ©÷ÍTà£ phØÿ£¢P |
| --- | Minor | &r*vw×âH«Ã*:ëû÷o{yÕ9eY¢³ÝhÔ:þÚÞ¡0DÚ´Ô¬ÙeBßÜsmÎ¬2!{swæfèl7Ï.&Ít³ïp=¿W÷éï¶ðl×/ìV=XÉï/sWÐEÏÎVz>ÓÇ º`¯!~¼+ÞIVé¥«Ðèìèà¨²OÐ:|iìÙ»¥. ý\ÝOª<káY |
| --- | Minor | áù¼ì+à¦÷aÛv»^ÀãXB{í²çÆµ(î©(e9¥êPØ¾ñ´½ì¤LGÄ3©Ûç2JgóP	»§ôÐÝxþf9öëPÔà¸ùøÌ:ã1y®Ë~RÛ£Çk·ûÃbúc®Ll¿c9N¥ý.¸[Ájz?\¢k×àÂµk\ä½WóÕ±Ú¨}eøh¿¾"n; Ø'¯(¼±®qbÉ¢¹;ªHõ¶Ê*©&Â!¸Døh(KRdrÑN*ocæjÐËDHoÐ®Í¹8FzúEÜvÇn^ÊV©u´:. ÁÛÍ#pMß¼:E)¢[c5¬å1©ú#ÃZDùê°Vqù º¨´´6nW13×EÞ`?LåÊ7ÃTñÎ0l4{}öÃ§úOø±É2ûV.á¹|7`æÓVóì¦d>Í¦hË«`kl_bÂÄTGuK7]&STß|¬4G?Ï´kêCáZ»c|&JõhNýûÉò)û >"[[ñÙAü9·¦®Zð«ÛÃ'wÀ7Vmc6ü>UÕkÁ%<ýÆS\ ×ñ';Oât[¾È ð£Ê5àPè+kHz¢¶_kØ¸ñô±ìþF¨ïÌ³8Fífò÷<è®RÕMD¢?*^ó9¾ö³QD'á¿HD*(<CäfAÍßVÑýç¾s+XÓB}¬zZ[ÿ. lR·n'*R½vªô(c\(Ô'_KfJI«^bfÖatIÁ*Q}\ÇIÖÙî)+5ëÔÛü7Hã°$1BYqÔôwáæ{å¦fN[*P>ouéL³¢×¢íEó×­Fämt\ê£Ú­÷]ÜôZªæ{í/Uâò;zár Ù÷hÞ×¬V¡Èç±ÿñ£¹WúÌ.P¸á5éaîe¾5°87¯ò2'ÕµI |
| --- | Minor | K§ÖZÇ÷±/óôzÉDÛy¸ª±ûõì§	RÓu-§[F±6ÎvÖqÜJêts§´ë&XÍ+h×á|PãÓQë	\´53æºûXQj+èoâ Mn@ÂÈ?Æ_¯¶ Éde(LOÛòßo§Sã°óÌ°ÆxW&¬¹=Ò$\CpkJà?óÍiúÁÄÏÿó/ÿM endstream endobj 443 0 obj <</Filter/FlateDecode/Length 3580>> stream xÚÅ[Éc» |
| --- | Minor | +üu£y ZHd wAårû­²Èÿo"N"u=Vå¥Ó |
| --- | Minor | £ìk¢(ñ<ÿ>øÿý¡Cõ}ëðïðù¯ñì·ñúëáO?ü?oJ(éðãrðÑm¹õris)µxøqþÇÑ¹ÒÆË½ïÏãÆ«;sþ4þgaüç²¶ãýh.ïo±ÖÑ+|Ð7Ð2Öñ¿¥V³wÖÇÃoÆÓè=ÈLÜ:Þÿùão ½?x·u×]k07ïü6zçxxËqk%§ÎsÈÛ_eóµ%ÐñçÍ§=è<Ç=	 àT=X¥½·pä¤sàFç ¦¨2eì-R¤ÃZ¤2û³¥fÔ*v¼ôÉp?1ÿìDHo4êe|Å>(ý¤®ª/ÎÓó7'Û09\7"nÃö. °h£>¬GJ²Qà. Ì!. |
| --- | Minor | Sentence exceeds complexity threshold, split for readability. Applying the split needs --strength moderate or higher. |
| --- | Minor | none (split proposal only; source not rewritten) |
| --- | Minor | none |
| --- | Minor | Check: NEEDS-LLM |
| --- | Minor | Flags:    not-assessed |
| --- | Minor | SENTENCE (Line 1103, 1180 words, 14 clauses)  [Script] |
| --- | Minor | Vu:3í«¡¡m2µ¤¤LßDôÍíý­z´~Õ§°Q`Ãã¼EYÎÍíÐDaP"gif<f´¨C«\¦ Â Ìí!ý+'Ò¥=H<^-·Í}-'H>ÓWeë- xv¢W(	¢÷±éw9ÜqnÛÖkmª*n^F¨ËÙ"nÖOöýbÿüp/ºUxèy%<cXÄwWxÜ^8ãÀs)ôsM:W×Â¶·B¹eTð-²¥rÛ¯êCÉöæÊutÎ)ÞªÛRiA&ÄÝëç+·a×kÎ2~5;/0ä ÈÉ8¸BFíAI@`ÆÍè ^úûS[Bk©¢ÀÊ¦½]ão ¦PZÓ%I£IìÖ1¬¡bðr2:dPçG¬9q jHKèK»À¶µØ.øBm-61ªò*õý¾¸R±úg EM*ûï0åxöóáÙ0anþS¼`x>1 	#fH¸	=~lÌ[+ö]@WÐl.ûxîçMe,{ï |
| --- | Minor | ¢-ôloñÎtÝ­ÊÌQe |
| --- | Minor | ¢«.ô2	÷­@/ûGÒBNû¦sß­f a4!ËÄh¨Vý !r¹¡ÝoÙ&X}¨î;9 |
| --- | Minor | |E}ÛS#¼ù6ßsO¿ FcS½±láHÏáï¤qKoèY;­_ÆJÊÖB2/ðä$á}ë¡s2 ÆíÑØTÐÔÔ»æx;YÜE¯®ÇDIäIqoÔÔÜn@ÕÆª§9µÆÑ/zê!P¦åukÇ9pyFÎ|ö¼úN~ÅÉG¸'É${4,õÈx¼Ë¿_ {»¸æ¯Fñc8¼íÈlá\ð~K­Vÿeó®ftãcytÒäPÇ]V¬QçMµß'õ'MoaÏí1Ñ+vù$gQNÛwãëÊùæ¶ÖJÊÌy8Ø£ôh¿Í~rõá<f!ü¬d³Ik(Tdë¹ò­?©M4t£N	v²n,9\Ì)í`otÍ¿Ù>là^F©[ª¡1[ ì5Eì^¶Ö&_áÏ6³=±»]'[ÿÊH¸Ù¾¨à+YLUÅV¡4*Í7ß®3¬JqúÃ |
| --- | Minor | ÞcZU9Öð"H¦ã}è>c|âE~PÀú¢ |
| --- | Minor | [B	y[Íà×uãIÎ	FE'KÃWèakÅÎoÀ¯Æ½òV²^JONôÓÙ° |
| --- | Minor | 9 |
| --- | Minor | %L?VG*EÎâb)°>¯X«B#H,E¸9ë·édrEß¯H	WEÆÔU´!VÇJª»ùJ±¼ÄøáÉ<¼çTL0è¯r¢J¹ãI¼i²÷Ò|1¸ ùÛL3}ICO`´]\Ë3:QHJÅ,I4Ê¦¦O_òD2 ñeÑÝb.1-Btteó£æÖÙ"Wx64Hå(%¡|RnFH 7± û](@«:ÜYD	Ø«5==$+a¶ß ú/PÏTw<¯¤®Å  ­6ùÀ 3dÕ=ïè0 wÖ#tÂ¿¥ísÀZÄP×-]y9ýÊÞ'å¨ý Ë~Ý>µ¸bbyñëêØl "¯9±¥±Ë¥+ª+Ó3:<M:"7]Ñ8Äw6ÉúÊFBÏl£<Ù^¥5Ú£(ågÉ±J3»{éËdçÛF[¬©©ÚãwËã2âfeý¡ö­%¨9_/ES7Âù#`¾Q:ÿOÁ+p/cvÚbî nû©¿kDFzZc\£ª×LgèÑääÝ#ÀÛBÊSV7v¡ZüÃÀuíÆtÚ8Ó"±.+lôJT¿ú5ÏEð?ÛX¦sBMþsò"/ëáÔrmí#þõú¾ù±øÅ¬=Õ*L7ÊéØ¦Ê>¼6«Ó3é |
| --- | Minor | r²G~?ÏÑ9,ßZW |
| --- | Minor | é0íC[47®þðKJï=ü¥­Å%ÃOþúÚ÷Y3ÏB¹o¡ä |
| --- | Minor | Þsö}£_IÄ,a¶î@=´ÆV­ucQËLQpý¶mGOõÒ¬Ä<kÃE}ln #¬·%)N1÷}¦nró&^éâ*¨¢ø±èëx3\d,¹Z£ô{T2sÜ³çx°W5ãÁG³@Êê¢ò«')CÆèá±9	Zït¯EÊ=rÊÂ	ÛÃ=µÄ1}öÂÃ5?È²êY3ÛFµôhþÞñ¶¼{<4s,Hµ'ÓríLËÍïÈ4~Â0dy*,ÜS+&3ÊH/ÀÑY¯eo4÷Âè¯PyûÄ IÎU.ïUhLÜàgÒ)j+¦dz¬&?´¬|nrzH´±³cKÝ=¨Ëi%²drcä-0cØþ?d ''Ä/c/eÊYäí¨ÉÂTï»ÁRí*oOÊåtEz~ðTM~%þ¢sÞ¯Ò«¬]ÎWjÒ°_ÞTä:_dí¼ëþm×ðòî×h»[¦[É&d ä²Ôz¯:ÉÑìËÍÐo®ý¿È¸{ÓÎ/Lû	ñjÞJííj/§A9¤?ÕÐwiÐþ`XRäÓ±ÎÑ¶Óà%×F#©][(#în ÌiÝÓ FaIybXS%Qì¢h|­\hGMy¿}<©ckûlèF9zU"µ½#ûQª´iåæ<Ãä%£³ËÂÅO	zYÒÒ	1­èÑ¥$°×iv÷±¾2Ä¤ÊÙïå´£PÁÿúôµ[N>È'M½1 Jªàö	ÙÔäÞä`¼?äë8§´e_B¾I9Er|]ÜD²Ijñ-^ÉùoðJ¡wË+Ñè¯òJú^µø ¯4Vb+#¼¯·#Cíû]/k÷Ï=ô[g/D 1d®nä2Þ¶ÔÚ¯¸/ÙÍ¥!{Ãç9µ?)±m-E¸»º×úõ 2|òU¦ûS`Pu©§^ñbQþý´õX@C»IÅ¹ft8ë,ÑÆ×*SÒ6º¼O³i¯ò¹DhòER ?Õýª?o6Üè§v]Bê5qÛå-Ñ1ìïâ"àHKéO·K,û;ðÂäv¸ÇÒ-w¼YhÐ(9Êä ÑÕò×õ tçÿQü¨á»ñ£ïKÔ`ãþjüÀß4ü.ç¤ÅâGñÙ¯×N¯/mpü`ZïË¥J/íýß'}èeF©;ä2%]ºÝk=OãýúÔ²µXà^aßZ«Ë=e|ÿþÿ ¢¨ endstream endobj 453 0 obj <</Filter/FlateDecode/Length 3555>> stream xÚÅ[»+¹Íýúém²øj`0¯gnf8F+GüÿY/V±ÕÒÕÌì]\hÔM_ÅS§©ÓNá´öÿÃ©ÆS |
| --- | Minor | §Ï÷gÿêÿþzúóÓo¿SSbI§·S©Y{þÇRÓë?Þ×5åØúgÿüñ·Ó_~Håp ë²­ÛÚÖUZyÛÒâZªÔòÑbÿ¡Dè&#{Këá#V*°®eå·%òg¼öRqsf°L×þöÒKiüÛlÐÿmfKçàíÅÈOÐVmýiXq°ü SßVùt·u_pc¼7dºö6æ]"éB !÷ÁúÝW¹/qüägýýå¼°{ Öh8¼K2é4]¸àø4I«T¾Ùß%QKk)â2Á¸óµ¶é®Xo"çù9ÕmIÊ Aà~ÇRdÉÝ·ì¿éNF,â'~çÊËT²­ÁdÆ Èý¹ßlÝ |
| --- | Minor | RêTü |
| --- | Minor | «Ë¢ÀÅv°îju_©1mB} UpQÈYç'EzÏÒcûgb©òb%<%¢ú2²î)Ï0-yxÇ\Ø¤0a{·i(WbqòÄ'f4$òWgeXÐçoU0î!()2ää¡Ñ½°è§àªj¨7BóV£oýÞ×>vl]äárZBkkøA~lí<BòÐi¥kfq·¢ÉNvSÃRzªÍ~Éº²Zkõ!jiE=â×ºGø°rY*ä<ãj¢(O(O	ÍÒ«`b©ôýÌhÆVÛeÓÞj[ð´íb]ÂÕbØ=SÅ^!c;Zo×&­v·f£!o |
| --- | Minor |  ).y«møû­*îÊJÒc²û¥¨nßàFVz³DÑ©UWU1j'Ùkõ<ó@®ÁsQíH^][Å?î¸²ZåTs;+Ôáy£îYz-cR'èd´_ëñ	w~­bGûKÀyqÐt}µSh#çDc#tÐT*=ö¼ZªÖú¦> 8¶¢:qëÇH xÔ¬~#0]}t&m"(º6¯ã[ç}Øvò°Êµ.­sÑ8 Êô{Þ·ìCöVv¼ß¿XÊ­»ÜAZ6aö"-ÞX&]ë=Èî/×¤	ó¼Aòìo	6OÏhAû¥Lyæ#^ÚkÊeàÈÛ3q÷FF¤#:ÓJûç`HýgöÊÍmÌ« |
| --- | Minor | a9~±Ú YI49Dâé±ì×m	áÔ-+^K?yÅ¤_òDÀó%g[_YrìxÛêAðªé(xa Â8"©°UX9Ùÿ÷í·¤\¦ª µ> l-)Ìþ»¿úÐëì-/1§ºá­Ï-em¸¿åOº%d\eî"¯O¯©ÛÇd97|ë¯ÌO¾û¹(åiPï¸·j¸úËt mé¡7¡N¹Tæ6óCfä 5u¸¨¡°¦ÔGË#Ê«ek8vp±§¼^ á:Õvo[ÄºàhÈÆ.lCÓM\CúT@mïß¦¨^¢±s?,KªIúbãÈÆ±DJ{% |
| --- | Minor | Ù#¸cAÂ>c Î×UwÂ­bK¯ÖÓÙ)j×Ù©³)sà¡Y[Se8÷Õ'ôÄrdq0>¸Gki§Kî3p |
| --- | Minor | $<´ N"SMRÞwZ?ëíHÉí<QzDÊÄA£S+V×r½>Àu<|KÌáâ·kºìòks òo_Ó%njè^=]}¨Ü?ÒùÍÜµÊ¹-·ló?Ô7X¶P ÒFM{ÒXß|=¨ |
| --- | Minor | Ô<HÛ>fwæE=^ ¡òwÄhÈÕ·çJH¸ |
| --- | Minor | ûÖïãZëÁ¡R "4mÿ³d*6EþðN_|#ÀôâÊ[¤\4Ã«Â´IQmì ¯ |
| --- | Minor | \(Às>¥Ó>e"Äµ¸û\C2^íðé¦[ìÝ4«×9ÁÒÙg{$Ç¹~j4U»À pòv'RVfÛ |
| --- | Minor | ?÷oü¤hÆIoÊ|u-²ûR~6ö*Ð.®åó«O·Öâ(çYb³×£än<d½¡ñ+-·þª(Ì½ñ¶Å|ëW¶¼¿·@ìífHÉÞgïÜÝß°^°ËdDqÏ3"-¬#>ÉD¶¶ô~TðàÏ%ÃîÄÖ¯:ñü"oå|þÁ­W-oÚ?óR÷fÖÙOfÞïGxÔ¹Añ6&o=2ÏkÕÌÖryÐ -ôzÏÀ¿¤.X['o°mKë¦ëx ízÉêàp==%.üþw6Ò¬ÿøÆse¿ÁÚà¾×/P¤Ö;VjKz`2Ø~Ö&YþÍ(ÉPöèdxºvÕôµ7Óp<afÕiºÁwµ>Ù%2«w<½¾6ø¥ê´^¬u/¤mX4õoN«*atV7%EIOr8èÉ£È£w:ô! |
| --- | Minor | Vu:3í«¡¡m2µ¤¤LßDôÍíý­z´~Õ§°Q`Ãã¼EYÎÍíÐDaP"gif<f´¨C«\¦ Â Ìí!ý+'Ò¥=H<^-·Í}-'H>ÓWeë- xv¢W(	¢÷±éw9ÜqnÛÖkmª*n^F¨ËÙ"nÖOöýbÿüp/ºUxèy%<cXÄwWxÜ^8ãÀs)ôsM:W×Â¶·B¹eTð-²¥rÛ¯êCÉöæÊutÎ)ÞªÛRiA&ÄÝëç+·a×kÎ2~5;/0ä ÈÉ8¸BFíAI@`ÆÍè ^úûS[Bk©¢ÀÊ¦½]ão ¦PZÓ%I£IìÖ1¬¡bðr2:dPçG¬9q jHKèK»À¶µØ.øBm-61ªò*õý¾¸R±úg EM*ûï0åxöóáÙ0anþS¼`x>1 	#fH¸	=~lÌ[+ö]@WÐl.ûxîçMe. {ï |
| --- | Minor | ¢-ôloñÎtÝ­ÊÌQe |
| --- | Minor | ¢«.ô2	÷­@/ûGÒBNû¦sß­f a4!ËÄh¨Vý !r¹¡ÝoÙ&X}¨î;9 |
| --- | Minor | |E}ÛS#¼ù6ßsO¿ FcS½±láHÏáï¤qKoèY;­_ÆJÊÖB2/ðä$á}ë¡s2 ÆíÑØTÐÔÔ»æx;YÜE¯®ÇDIäIqoÔÔÜn@ÕÆª§9µÆÑ/zê!P¦åukÇ9pyFÎ|ö¼úN~ÅÉG¸'É${4. õÈx¼Ë¿_ {»¸æ¯Fñc8¼íÈlá\ð~K­Vÿeó®ftãcytÒäPÇ]V¬QçMµß'õ'MoaÏí1Ñ+vù$gQNÛwãëÊùæ¶ÖJÊÌy8Ø£ôh¿Í~rõá<f!ü¬d³Ik(Tdë¹ò­?©M4t£N	v²n. 9\Ì)í`otÍ¿Ù>là^F©[ª¡1[ ì5Eì^¶Ö&_áÏ6³=±»]'[ÿÊH¸Ù¾¨à+YLUÅV¡4*Í7ß®3¬JqúÃ |
| --- | Minor | ÞcZU9Öð"H¦ã}è>c|âE~PÀú¢ |
| --- | Minor | [B	y[Íà×uãIÎ	FE'KÃWèakÅÎoÀ¯Æ½òV²^JONôÓÙ° |
| --- | Minor | 9 |
| --- | Minor | %L?VG*EÎâb)°>¯X«B#H. E¸9ë·édrEß¯H	WEÆÔU´!VÇJª»ùJ±¼ÄøáÉ<¼çTL0è¯r¢J¹ãI¼i²÷Ò|1¸ ùÛL3}ICO`´]\Ë3:QHJÅ. I4Ê¦¦O_òD2 ñeÑÝb.1-Btteó£æÖÙ"Wx64Hå(%¡|RnFH 7± û](@«:ÜYD	Ø«5==$+a¶ß ú/PÏTw<¯¤®Å  ­6ùÀ 3dÕ=ïè0 wÖ#tÂ¿¥ísÀZÄP×-]y9ýÊÞ'å¨ý Ë~Ý>µ¸bbyñëêØl "¯9±¥±Ë¥+ª+Ó3:<M:"7]Ñ8Äw6ÉúÊFBÏl£<Ù^¥5Ú£(ågÉ±J3»{éËdçÛF[¬©©ÚãwËã2âfeý¡ö­%¨9_/ES7Âù#`¾Q:ÿOÁ+p/cvÚbî nû©¿kDFzZc\£ª×LgèÑääÝ#ÀÛBÊSV7v¡ZüÃÀuíÆtÚ8Ó"±.+lôJT¿ú5ÏEð?ÛX¦sBMþsò"/ëáÔrmí#þõú¾ù±øÅ¬=Õ*L7ÊéØ¦Ê>¼6«Ó3é |
| --- | Minor | r²G~?ÏÑ9. ßZW |
| --- | Minor | é0íC[47®þðKJï=ü¥­Å%ÃOþúÚ÷Y3ÏB¹o¡ä |
| --- | Minor | Þsö}£_IÄ. a¶î@=´ÆV­ucQËLQpý¶mGOõÒ¬Ä<kÃE}ln #¬·%)N1÷}¦nró&^éâ*¨¢ø±èëx3\d. ¹Z£ô{T2sÜ³çx°W5ãÁG³@Êê¢ò«')CÆèá±9	Zït¯EÊ=rÊÂ	ÛÃ=µÄ1}öÂÃ5?È²êY3ÛFµôhþÞñ¶¼{<4s. Hµ'ÓríLËÍïÈ4~Â0dy*. ÜS+&3ÊH/ÀÑY¯eo4÷Âè¯PyûÄ IÎU.ïUhLÜàgÒ)j+¦dz¬&?´¬|nrzH´±³cKÝ=¨Ëi%²drcä-0cØþ?d ''Ä/c/eÊYäí¨ÉÂTï»ÁRí*oOÊåtEz~ðTM~%þ¢sÞ¯Ò«¬]ÎWjÒ°_ÞTä:_dí¼ëþm×ðòî×h»[¦[É&d ä²Ôz¯:ÉÑìËÍÐo®ý¿È¸{ÓÎ/Lû	ñjÞJííj/§A9¤?ÕÐwiÐþ`XRäÓ±ÎÑ¶Óà%×F#©][(#în ÌiÝÓ FaIybXS%Qì¢h|­\hGMy¿}<©ckûlèF9zU"µ½#ûQª´iåæ<Ãä%£³ËÂÅO	zYÒÒ	1­èÑ¥$°×iv÷±¾2Ä¤ÊÙïå´£PÁÿúôµ[N>È'M½1 Jªàö	ÙÔäÞä`¼?äë8§´e_B¾I9Er|]ÜD²Ijñ-^ÉùoðJ¡wË+Ñè¯òJú^µø ¯4Vb+#¼¯·#Cíû]/k÷Ï=ô[g/D 1d®nä2Þ¶ÔÚ¯¸/ÙÍ¥!{Ãç9µ?)±m-E¸»º×úõ 2|òU¦ûS`Pu©§^ñbQþý´õX@C»IÅ¹ft8ë. ÑÆ×*SÒ6º¼O³i¯ò¹DhòER ?Õýª?o6Üè§v]Bê5qÛå-Ñ1ìïâ"àHKéO·K. û;ðÂäv¸ÇÒ-w¼YhÐ(9Êä ÑÕò×õ tçÿQü¨á»ñ£ïKÔ`ãþjüÀß4ü.ç¤ÅâGñÙ¯×N¯/mpü`ZïË¥J/íýß'}èeF©;ä2%]ºÝk=OãýúÔ²µXà^aßZ«Ë=e|ÿþÿ ¢¨ endstream endobj 453 0 obj <</Filter/FlateDecode/Length 3555>> stream xÚÅ[»+¹Íýúém²øj`0¯gnf8F+GüÿY/V±ÕÒÕÌì]\hÔM_ÅS§©ÓNá´öÿÃ©ÆS |
| --- | Minor | §Ï÷gÿêÿþzúóÓo¿SSbI§·S©Y{þÇRÓë?Þ×5åØúgÿüñ·Ó_~Håp ë²­ÛÚÖUZyÛÒâZªÔòÑbÿ¡Dè&#{Këá#V*°®eå·%òg¼öRqsf°L×þöÒKiüÛlÐÿmfKçàíÅÈOÐVmýiXq°ü SßVùt·u_pc¼7dºö6æ]"éB !÷ÁúÝW¹/qüägýýå¼°{ Öh8¼K2é4]¸àø4I«T¾Ùß%QKk)â2Á¸óµ¶é®Xo"çù9ÕmIÊ Aà~ÇRdÉÝ·ì¿éNF. â'~çÊËT²­ÁdÆ Èý¹ßlÝ |
| --- | Minor | RêTü |
| --- | Minor | «Ë¢ÀÅv°îju_©1mB} UpQÈYç'EzÏÒcûgb©òb%<%¢ú2²î)Ï0-yxÇ\Ø¤0a{·i(WbqòÄ'f4$òWgeXÐçoU0î!()2ää¡Ñ½°è§àªj¨7BóV£oýÞ×>vl]äárZBkkøA~lí<BòÐi¥kfq·¢ÉNvSÃRzªÍ~Éº²Zkõ!jiE=â×ºGø°rY*ä<ãj¢(O(O	ÍÒ«`b©ôýÌhÆVÛeÓÞj[ð´íb]ÂÕbØ=SÅ^!c;Zo×&­v·f£!o |
| --- | Minor |  ).y«møû­*îÊJÒc²û¥¨nßàFVz³DÑ©UWU1j'Ùkõ<ó@®ÁsQíH^][Å?î¸²ZåTs;+Ôáy£îYz-cR'èd´_ëñ	w~­bGûKÀyqÐt}µSh#çDc#tÐT*=ö¼ZªÖú¦> 8¶¢:qëÇH xÔ¬~#0]}t&m"(º6¯ã[ç}Øvò°Êµ.­sÑ8 Êô{Þ·ìCöVv¼ß¿XÊ­»ÜAZ6aö"-ÞX&]ë=Èî/×¤	ó¼Aòìo	6OÏhAû¥Lyæ#^ÚkÊeàÈÛ3q÷FF¤#:ÓJûç`HýgöÊÍmÌ« |
| --- | Minor | a9~±Ú YI49Dâé±ì×m	áÔ-+^K?yÅ¤_òDÀó%g[_YrìxÛêAðªé(xa Â8"©°UX9Ùÿ÷í·¤\¦ª µ> l-)Ìþ»¿úÐëì-/1§ºá­Ï-em¸¿åOº%d\eî"¯O¯©ÛÇd97|ë¯ÌO¾û¹(åiPï¸·j¸úËt mé¡7¡N¹Tæ6óCfä 5u¸¨¡°¦ÔGË#Ê«ek8vp±§¼^ á:Õvo[ÄºàhÈÆ.lCÓM\CúT@mïß¦¨^¢±s?. KªIúbãÈÆ±DJ{% |
| --- | Minor | Ù#¸cAÂ>c Î×UwÂ­bK¯ÖÓÙ)j×Ù©³)sà¡Y[Se8÷Õ'ôÄrdq0>¸Gki§Kî3p |
| --- | Minor | $<´ N"SMRÞwZ?ëíHÉí<QzDÊÄA£S+V×r½>Àu<|KÌáâ·kºìòks òo_Ó%njè^=]}¨Ü?ÒùÍÜµÊ¹-·ló?Ô7X¶P ÒFM{ÒXß|=¨ |
| --- | Minor | Ô<HÛ>fwæE=^ ¡òwÄhÈÕ·çJH¸ |
| --- | Minor | ûÖïãZëÁ¡R "4mÿ³d*6EþðN_|#ÀôâÊ[¤\4Ã«Â´IQmì ¯ |
| --- | Minor | \(Às>¥Ó>e"Äµ¸û\C2^íðé¦[ìÝ4«×9ÁÒÙg{$Ç¹~j4U»À pòv'RVfÛ |
| --- | Minor | ?÷oü¤hÆIoÊ|u-²ûR~6ö*Ð.®åó«O·Öâ(çYb³×£än<d½¡ñ+-·þª(Ì½ñ¶Å|ëW¶¼¿·@ìífHÉÞgïÜÝß°^°ËdDqÏ3"-¬#>ÉD¶¶ô~TðàÏ%ÃîÄÖ¯:ñü"oå|þÁ­W-oÚ?óR÷fÖÙOfÞïGxÔ¹Añ6&o=2ÏkÕÌÖryÐ -ôzÏÀ¿¤.X['o°mKë¦ëx ízÉêàp==%.üþw6Ò¬ÿøÆse¿ÁÚà¾×/P¤Ö;VjKz`2Ø~Ö&YþÍ(ÉPöèdxºvÕôµ7Óp<afÕiºÁwµ>Ù%2«w<½¾6ø¥ê´^¬u/¤mX4õoN«*atV7%EIOr8èÉ£È£w:ô!. |
| --- | Minor | Sentence exceeds complexity threshold, split for readability. Applying the split needs --strength moderate or higher. |
| --- | Minor | none (split proposal only; source not rewritten) |
| --- | Minor | none |
| --- | Minor | Check: NEEDS-LLM |
| --- | Minor | Flags:    not-assessed |
| --- | Minor | SENTENCE (Line 1103, 453 words, 11 clauses)  [Script] |
| --- | Minor | £ièRÌåM|»9R\®;ÎÊGp;4·5 Ù&ß,^Ô2¹»bÑ¹c=O[m<ºÍF ·^òÍý/ëLG!>>ðxOB\°÷OÆ¹ÝÝËnjzÌÕCZ;^Õ[Uõ)ïâÆ8Ë¾<X#>ð{U÷qQCÝ8üCh«ª%å2ZÊ<ì#µôØx´ø86Ä°Ä\;½*"Õ÷z;N-aÓq´¬¹nõ |
| --- | Minor | *È(ÔWÕqªù´6®b*å¿wSa%¨å+û%öP¼æ*.æ¯´ú/ìõ¸×u5¡SífI`ãÅl³,çöÙîÍ]¬ã-Ô´´Ðâ=¯82Vî'¯HÒ³ÊÂ¡Iìø7ÑÇ*jct×uäÎ+Ù9ÞßVO¯öÐ |
| --- | Minor | ¥'±üæ |
| --- | Minor | /0¸Ãqy¸Ùª&ô<äC#oí'ÕÒg,/Ë;©³¾EGHW¸ùôuÎ)O,Y¬?º(wY¨õwÆùÏ>Û¶åÀôö0æ7Ùk¨èà%Ó2µ®Ç|ú«»#uÑ%Xt±zª?*êÑê4~kG{l®úT[.FRÒgÎ³¬Ñuºb§2±]v®' »4JÕø (G¹r#Íøp§Á§ÂÁýu3­%¦c>6¯ø´?¬z8©ÍÝnÝA¨û´øÚ¸ïÀC&à÷îÁ |
| --- | Minor | (qm}utse"z?GCÛç7ç¡Ý=w÷d^ÚRj¶{gï}h>84?ô	~ÓØfw!:NJ»~W¾]Ý¼ÛÔQß(XYÝ0ÊØÁßJºZbhc2lOÞFO¢	J±¾YpwªeJÉT> OË"ùÉ i{þúj-1ß¬³ËòæºûÑj»xNô2uoÓ)Æ¹ ÙøèÈÔ'#å»;ò&FZP^<¼w}:¸LpÜRñ¿M3.Ô¾z>iP|ÒÙ8ñúàÐ¨Ä·ô§¿£?Õéü[UbêþëúöâKJS	Kò,5¥ýAïøINûÊqcã/(Û¶@ìÎÿBeÒó¿ì~õãóSt=] |
| --- | Minor | ÔzßëìnºE²4(øs °¤X6p×/´±¿ÿé¿ÈÛ[a endstream endobj 320 0 obj <</Type/ObjStm/N 200/First 1905/Filter/FlateDecode/Length 5164>> stream xÚÕ\ks9vý_ÑÍ¤ÜÄëâÚ*Ïx=ëÊfw3M6ër¥ZTK¢- IyìsÐM6øòx²¤4ã*¹Ñ ÷û@«¥RÕ®ÒÑV&¥Ê*[Yc*ë4(;§«CÊÃ3âw«*á7VWAóiªhù´UÊíWTZ§¯´Õ¬	vãÛXiñ µ:CÖ!¡ur,¸Ê(ÏTF'±2V³&VÆaT+ª2B¢+Ø$¦2 l2>~*²	Fc!*@Ó²Ù±Ú+¾  |
| --- | Minor | ¿L¨ztNíAUNO3äRÐ# 6X°TðÊ`ðù+p-)ÔàEA d4¢©\´É,®	,H%L¾HÖÅ®[BåRåuIU³d1ºwS\å}  À-ÐTEÄâ<þàfV8íàAAª ÐT@!VQP©u5ÈqÚ¢Y&Î¨*:È­*zÌ°LEÎ²ûbâÈ TdÁWÉ(>Häº3	Å!yÉ³ÌJ£:P;Cè´RJ2%H²Ò(xJ8q8%£Ä©Dd|ªH1ði>(iÍq?­3 vZ{Ã/0¥@ÙÎ_`<Ãuàª\`<È6|wGm¼wy	iÉ:ÏºÞ:øåF±$Ôa¶´õì¬K©Äu£ ¶jpEµa0U;Y%¶r¨(W,A2­Bü y(AÜµp¾Åë¼ |
| --- | Minor | %Ö.Îõ 5í50Èö\È\mÚ¦`µ÷ Cb.9Ê*×³ÎØÚ×JYm°ê Ê,e¡vYp<a	øbkw8J	ÿbk²,ÍàømP`Ço"ÿiPu%Àt J |
| --- | Minor | ú¢  G'Â VÁ"Ïo |
| --- | Minor | `t(ÍuÜ¦¡wX°(qÁ§2Å9A	sDu©iJSËñØO<8ñ#? |
| --- | Minor | £ièRÌåM|»9R\®;ÎÊGp;4·5 Ù&ß. ^Ô2¹»bÑ¹c=O[m<ºÍF ·^òÍý/ëLG!>>ðxOB\°÷OÆ¹ÝÝËnjzÌÕCZ;^Õ[Uõ)ïâÆ8Ë¾<X#>ð{U÷qQCÝ8üCh«ª%å2ZÊ<ì#µôØx´ø86Ä°Ä\;½*"Õ÷z;N-aÓq´¬¹nõ |
| --- | Minor | *È(ÔWÕqªù´6®b*å¿wSa%¨å+û%öP¼æ*.æ¯´ú/ìõ¸×u5¡SífI`ãÅl³. çöÙîÍ]¬ã-Ô´´Ðâ=¯82Vî'¯HÒ³ÊÂ¡Iìø7ÑÇ*jct×uäÎ+Ù9ÞßVO¯öÐ |
| --- | Minor | ¥'±üæ |
| --- | Minor | /0¸Ãqy¸Ùª&ô<äC#oí'ÕÒg. /Ë;©³¾EGHW¸ùôuÎ)O. Y¬?º(wY¨õwÆùÏ>Û¶åÀôö0æ7Ùk¨èà%Ó2µ®Ç|ú«»#uÑ%Xt±zª?*êÑê4~kG{l®úT[.FRÒgÎ³¬Ñuºb§2±]v®' »4JÕø (G¹r#Íøp§Á§ÂÁýu3­%¦c>6¯ø´?¬z8©ÍÝnÝA¨û´øÚ¸ïÀC&à÷îÁ |
| --- | Minor | (qm}utse"z?GCÛç7ç¡Ý=w÷d^ÚRj¶{gï}h>84?ô	~ÓØfw!:NJ»~W¾]Ý¼ÛÔQß(XYÝ0ÊØÁßJºZbhc2lOÞFO¢	J±¾YpwªeJÉT> OË"ùÉ i{þúj-1ß¬³ËòæºûÑj»xNô2uoÓ)Æ¹ ÙøèÈÔ'#å»;ò&FZP^<¼w}:¸LpÜRñ¿M3.Ô¾z>iP|ÒÙ8ñúàÐ¨Ä·ô§¿£?Õéü[UbêþëúöâKJS	Kò. 5¥ýAïøINûÊqcã/(Û¶@ìÎÿBeÒó¿ì~õãóSt=] |
| --- | Minor | ÔzßëìnºE²4(øs °¤X6p×/´±¿ÿé¿ÈÛ[a endstream endobj 320 0 obj <</Type/ObjStm/N 200/First 1905/Filter/FlateDecode/Length 5164>> stream xÚÕ\ks9vý_ÑÍ¤ÜÄëâÚ*Ïx=ëÊfw3M6ër¥ZTK¢- IyìsÐM6øòx²¤4ã*¹Ñ ÷û@«¥RÕ®ÒÑV&¥Ê*[Yc*ë4(;§«CÊÃ3âw«*á7VWAóiªhù´UÊíWTZ§¯´Õ¬	vãÛXiñ µ:CÖ!¡ur. ¸Ê(ÏTF'±2V³&VÆaT+ª2B¢+Ø$¦2 l2>~*²	Fc!*@Ó²Ù±Ú+¾  |
| --- | Minor | ¿L¨ztNíAUNO3äRÐ# 6X°TðÊ`ðù+p-)ÔàEA d4¢©\´É. ®. H%L¾HÖÅ®[BåRåuIU³d1ºwS\å}  À-ÐTEÄâ<þàfV8íàAAª ÐT@!VQP©u5ÈqÚ¢Y&Î¨*:È­*zÌ°LEÎ²ûbâÈ TdÁWÉ(>Häº3	Å!yÉ³ÌJ£:P;Cè´RJ2%H²Ò(xJ8q8%£Ä©Dd|ªH1ði>(iÍq?­3 vZ{Ã/0¥@ÙÎ_`<Ãuàª\`<È6|wGm¼wy	iÉ:ÏºÞ:øåF±$Ôa¶´õì¬K©Äu£ ¶jpEµa0U;Y%¶r¨(W. A2­Bü y(AÜµp¾Åë¼ |
| --- | Minor | %Ö.Îõ 5í50Èö\È\mÚ¦`µ÷ Cb.9Ê*×³ÎØÚ×JYm°ê Ê. e¡vYp<a	øbkw8J	ÿbk². ÍàømP`Ço"ÿiPu%Àt J |
| --- | Minor | ú¢  G'Â VÁ"Ïo |
| --- | Minor | `t(ÍuÜ¦¡wX°(qÁ§2Å9A	sDu©iJSËñØO<8ñ#?. |
| --- | Minor | Sentence exceeds complexity threshold, split for readability. Applying the split needs --strength moderate or higher. |
| --- | Minor | none (split proposal only; source not rewritten) |
| --- | Minor | none |
| --- | Minor | Check: NEEDS-LLM |
| --- | Minor | Flags:    not-assessed |
| --- | Minor | SENTENCE (Line 1103, 226 words, 2 clauses)  [Script] |
| --- | Minor | r<VââÐÃS#äñRÈ¡@¬9iTY»°HÈ%ÌË0"&ÜD:tVµy..@«hBKØ:*¨@ÉBqVµg)K]`	H­\C_ óR§ûP2à%Ê¤%ðXûÌLÛ #Sé;R©nÅp§Ø0¸>reÒrdòÓWkC¸¦£`] ×tä:Îj¤tâxÄ°ÇK¬<p®%º m]¤õEêº®(ÕºrÕswü·?_¼o'y¤;z_¾¯ÿËb>yÓ®ÞÿòòÕøÇöÓjüú®¹n¿ëßv×ïùy1Í	úãtöaüíBñÔïÆ¿÷Xòå>{3þ~þã|üòÙê¦/Ú»Z ù ó6ªC×ÖÚ¶®¯¡µN×ìÁ¶«5Y¥v>®ÛëUõõn:éxb¸2Àµ¦ÿ=åkHkø@ÃÔp~N6`­1°.ÕVä¤`Ûÿ}hVÓù¬vdRè>½W©é¢Ã[öDKÀ"èXû |
| --- | Minor | ¥ÕDGY¶5­B^ä©÷Ù2.Ô>Y5bêDÇ1x<1Ø\#i½êiNvÕ\Ü¶%­Þe·XÓë5>eA§A{÷ªsÐ¥]kL(E·¾/ã;ÕHÿ{KÏ>½3X+:ÎÔ n ¥n&bMÄÀN¦«¶¾^ÞÅFB[_+¸¥ÆÚÓ-N¶z#¶Ó^àFp»n65'¾y;0\>c·:µðsÀUÃMü éÛèALÎcìIdö?í¾Ì*£B×|I0$©àAlFý^q~0)y1þôú~0èpåá@:1ýS#ô¨±b8·5s;ÆJ­4ÓXºfiö=¸c¢0L{©9=¬l¦KCWØXåj&>jA	{ú÷~þkÿ®YÝ @[WÓsÖCÒºf f 2×zéA[dþ o§×7«»fç>2Øù<`áà/2§Ócø¸Î9GÅ"1Õ¥ i,,q¦°ôU8ÜAícò´SÇ|qP»Ì!pÖ~ñ? |
| --- | Minor | r<VââÐÃS#äñRÈ¡@¬9iTY»°HÈ%ÌË0"&ÜD:tVµy..@«hBKØ:*¨@ÉBqVµg)K]`	H­\C_ óR§ûP2à%Ê¤%ðXûÌLÛ #Sé;R©nÅp§Ø0¸>reÒrdòÓWkC¸¦£`] ×tä:Îj¤tâxÄ°ÇK¬<p®%º m]¤õEêº®(ÕºrÕswü·?_¼o'y¤;z_¾¯ÿËb>yÓ®ÞÿòòÕøÇöÓjüú®¹n¿ëßv×ïùy1Í	úãtöaüíBñÔïÆ¿÷Xòå>{3þ~þã|üòÙê¦/Ú»Z ù ó6ªC×ÖÚ¶®¯¡µN×ìÁ¶«5Y¥v>®ÛëUõõn:éxb¸2Àµ¦ÿ=åkHkø@ÃÔp~N6`­1°.ÕVä¤`Ûÿ}hVÓù¬vdRè>½W©é¢Ã[öDKÀ"èXû |
| --- | Minor | ¥ÕDGY¶5­B^ä©÷Ù2.Ô>Y5bêDÇ1x<1Ø\#i½êiNvÕ\Ü¶%­Þe·XÓë5>eA§A{÷ªsÐ¥]kL(E·¾/ã;ÕHÿ{KÏ>½3X+:ÎÔ n ¥n&bMÄÀN¦«¶¾^ÞÅFB[_+¸¥ÆÚÓ-N¶z#¶Ó^àFp»n65'¾y;0\>c·:µðsÀUÃMü éÛèALÎcìIdö?í¾Ì*£B×|I0$©àAlFý^q~0)y1þôú~0èpåá@:1ýS#ô¨±b8·5s;ÆJ­4ÓXºfiö=¸c¢0L{©9=¬l¦KCWØXåj&>jA	{ú÷~þkÿ®YÝ @[WÓsÖCÒºf f 2×zéA[dþ o§×7«»fç>2Øù<`áà/2§Ócø¸Î9GÅ"1Õ¥ i. q¦°ôU8ÜAícò´SÇ|qP»Ì!pÖ~ñ?. |
| --- | Minor | Sentence exceeds complexity threshold, split for readability. Applying the split needs --strength moderate or higher. |
| --- | Minor | none (split proposal only; source not rewritten) |
| --- | Minor | none |
| --- | Minor | Check: NEEDS-LLM |
| --- | Minor | Flags:    not-assessed |
| --- | Minor | SENTENCE (Line 1103, 1100 words, 24 clauses)  [Script] |
| --- | Minor | =-º§·÷Ùõ)ÜKºLèBÕÐò:,Ñç¼w-æ¤3ß¶+ËÍ øªv¡ßÈ% |
| --- | Minor | §Û$æ¾ëº(øòðr<ä³öAÈ°ÍèÇ ¯¡ìÅÝp !N³µÍ_µ3ùzûÏÌ¹¾èÅ÷}¸áÃ¹,ÝÔ_@T«\d~³fÛFh)¿Ñeç­EmªóãëÀ­jSu¦6"_1Q.ÆÏÏRùr4OeÓ7^-"		â<ïÖÓçu²§²çWÓëE»¾ ¶ÜwW­_BcÎ×ÔÞ¦óÚQ=µeò Å!VWé¼«CT¬Uû¼p/á¡æ~ÆÊû |
| --- | Minor | ÉÝ-]Ã>_î.y¢ ïu(rî}êÚX{¶ap¦h±î |
| --- | Minor | DmÜv¨'P?<ÜÐM²ËþÒj:)-¦8Fä6,¦á_Ðð`Ý£w°M¶Ïx+ýÞtszòµ*æ^ÎPÁ»'åÁ~ÖÓÂ¦Ë<gâ º|iÝøîÞ<°JÅ< £ZUóU*o#"0éë6}Ø¦mEjEDÆå­üÏDp¡rë!yøiq9ié¾?çèÇÝißÕÍä¾ØÍüv~ý¹/®ÇtÐêönv{ÿü®ÎêàõxXd0·ã5ÓØ<ñ°1×ÔÕ:¹Å§éÇUs±A®%¤=|1wB0ËÈíòâ£ã³6 <6¹¯ |
| --- | Minor | {É=7o4pÑ¦¸½Ýëº¨g±<ó©-NIçf |
| --- | Minor | Æ«bï±ä³57Bãá^$ðöI; 1¡Ø N®æA2F}ùP^ycÆ:WûËÌËLÇýUf2f¦R¶<ÆÁiSáIq[K¸;L'áºðKîàk<_ñ3ÂbT¨èÒûj} &ð¢½çæ<:>0&p;WÄó*&ÁîôÈÙ×uÞÙ |
| --- | Minor | ,kâf_àÙf,èXyh øÅ§ÆçÒ¶<Ð·¬gíÃbz¿¬'ñ}sß.þçjzÛ.»2X¥ñM³¼_Åà¥_^I«$( g¡*¥ |
| --- | Minor | ËÕ¢¬êÕÝí¾mÑÂÀ,'xx@ H7¿aÂ"B_4«.p|K?fñõÕtÉ|fÄ¦QÆÅÎ|ëî¨|¸[Þó²0èÏ,ÛÈ)Û.ì,ûîÀÜYãñý8®jßÎg×µI1£}mxÇ"'++C#ÎÍ(cºXwXª|l\³)°êÌ½0F:3>VIU!j=Qè\l&ÕÆ_´µók°OCvUtHàÏÂ×;pr|V]®61=za·ëçÛùü!< &é º9æÇt¾ÿjÞsÉ{.úÒ³[y(­Þ÷±Æó%°Þe¶ÚP~û.¤â |
| --- | Minor | ~h×íÂ(­ñ¶h2ð |
| --- | Minor | ±?ä}¥ |
| --- | Minor | ¶½ÌgW=x7´\=,[úQ¨¡v8üêºUW}óÐÌ®Ï-ÙIs;½Xä4ÚÈuù¨®×{¢¥×ír5½[w(xùüØ¬n0:½~À$£G*{ìÓËkHG¸öaº¼@m¢ÛæÐ¦o¯ |
| --- | Minor | vwyßjÓº{,×ßÆ)?¼n%Ñ&×.'P#î	-{çÛ\(·ÆçP{ß,¦K Ðy z²ºÁÿ7ÓÛ[ªnæË]ÙÿÌ6 Í\§¨Ysûy9]xéwhlå¤X°oÕ<\´³«öö¢5.ÁÀX0p5Í¤Ú÷Kp/ÜûØÌÚ[Ln;Ã¤ÞX°ï§NÌ0)·WÜ+.WílNÅÈå­´}¦íê|ú·éåò-o¯âû|wµ{¦îNÆ'Hw^f6*»æout©ãûVÚ%½]É3Æ#Þ±Ø­e_»[Ün¥ñöèN¥ñ"é>AE,¥~ËÂtlµÓÆîÙHi·2D©ÝÊ8âÕÊ4â5Vnöh¤»±®0#éN |
| --- | Minor | >%íg÷Ð-¯"6MÒï{xrxU#Þ8ÞÑ®UñL´.ÞHgàúw¯mñ.#éLá¢]«ïñ4fÀsÝ"]J¿7u6©K¼ÁC]à |
| --- | Minor | ¶Y¦@ú^ÅðÎþöëD}@¸[:)£/qçg·+/p!ÛØ~»C5ÄTpÓTÃñöìð.jpÉdK¶ Ã[s+ÈL¿+õÏõît ëqáXØk"Q M 1Q¶Cy |
| --- | Minor | áÔvæÃòÖûfz,ÀmpZÅÙrÀ,×ÎmUlÕ=ÎoÕn¶j@º[5 ÞmDúòqT,ØÒC³5(ø&=MÃ·Ô"n¿Äõþß$ööûÕìö«ÁÞÜAW:÷ïlï ½ /×ÙþrA~ú¼*ÇÑÎIaÛýÄ]T{»_ |
| --- | Minor | ¯Õ~u>â÷«9Èëbî¿LV>P²{hñ]¹£µÀ;½] Ù¯Æ¼»_ |
| --- | Minor | ¦·_ |
| --- | Minor | ±²_ |
| --- | Minor | ~¿òÂÏÑFýapNÈxçxôýÀÅÞOëÞAoïuï ´÷ÉÖ<¤÷ÁÖç¤÷¼Ö§û¥÷¶ÖxH<äwÿSgVéÜ£ââ3*£¬½Ç3ÔÞÝÒIïê¬kgïæ¬kiïãI¯X8%Ý:ìâü ù{¶åu¶-ö]MoÓ|¿dÓf®ßêNÆûï¿W)ÿ¯§Înoßí7ÂX·tlY·iöCãÖg÷ãF°óu¤±¸Õ" öm¦sy6ð\¬á­?ìüÜè÷s3¨6_÷§2|n:m·æóëiïsììf4 Ç=,4Cãh3Püé ÅK7<\ñ6í+wì| |
| --- | Minor | <Ð4ou®àX@ a¡ÛO;`ì|Ä Ê¼Ø*ÃßÐG¦Îä«!GæéO½×YøÜèy¶²Áq+¤o·æ[l1¯ÁÿXx×aÃ;×ùRE»·Ð²C»Ñ»íJ àûãóÆK_ø©Ë |
| --- | Minor | òü-}|ð ,Ç	äÌ§Jdí4^ÌÙàlMÚf(Ï¢iä¦Ý lÙZ<4òÎe<H¥IYÍÊ±~kêÓ³ÞrêKîmkÄk)ø¶Óf·T÷Ü!fî|T0k·åè7ói»eIÔáí6¦b}of8g:§SGñ<*û+8}V 6_Aûñ1wZ|5 §¯ttã &YHàåÛãSh¡PÞö(4îtìÒì´È1±/ÝÂmØmñ_Í]x}u0_hý |
| --- | Minor | ^ý?Å¹ endstream endobj 678 0 obj <</Filter/FlateDecode/Length 368>> stream xÚ]]k0ïý¹ìÅ¯;¡µ	ë6j»Ý¥zÚ	5¨ý÷Ó¼¡ ç=9ÇÍ]!¹_º«JØ¥µ¦¾uEìL×F:~Àê¦,³jrÜl/Ôh¹ÅÛ¦øù~~ßºVÈL¨Þ÷º7¡§cîsVÓã],»òÞÔòÒ± Þ´RäÓJõ¿÷ ì|©~Íýídîy+?5â ÀÇÚBtÜRZ PAdu1ÈêÖV¡`²^^@¢oAÖµÜ^ |
| --- | Minor | ç x	QQ´2£¢hxÐqDt1êãÐÈC¡Ú)Aci	¿Z2ñ±ÀMklæ&Íö°jÔzjµC3Ds¿IIUUfÿüÿ» endstream endobj 679 0 obj <</Filter/FlateDecode/Length 463>> stream xÚ]Oo£0Åï| »ZU |
| --- | Minor | +EH	i ~xþ¼aËj[¹nñ«Ä©s­·áê+öÜ¹(¢íM_Q\îëñ¹î­7Õßýçï?û·¡¯]*ï7ÃW{ÿñ¾Kµhí	¦ï·Ñ I®¶Ûe²}åNX­"!â·9òeò7q·n£ýµ¼{ñ­õ;»òÞ®ãøe{ë&DEÂ¥ÐÖ­½uc}íÎ6Z%óUÕn¾Èºö¿ó\ÂíxjþÕ~1O7³ydi¨¤AR qFB>õ Ò°Ô KÒ,é÷b*3 jaLjeI ¹QÙ#ÊHÐ¢7 hÉJ´h»ÄÔBB²'Ðg$èTÈCÞ Ea*9º' ,!ADÌÕæFµ9æ§ÁS¡ópÆ¡ui#´'øP»bÔ®ÕLLSb*#Q²ÖÌÁ KsGíýÔÚüñó+_Ö`YÞÝm®ÞÏË6<¬é²Q³??q¯pý½ endstream endobj 680 0 obj <</Filter/FlateDecode/Length 499>> stream xÚ]Kkã0F÷þZ¶ÅYRÁG |
| --- | Minor | éÌÐ4L·­dµlg?¶¾oºCG{ïµïª}åºIÄ¿üÐì QQp)Ü¡µ×±n¬¯ÝÅFëd~ ±.ç§¬kÿ×Üv:7j¿,O·óò =c%÷­@Ì@k¢5fÌ@3Pàö z®@ô xæ¨DOM¢3 ùÔ$xJäSpÑ%.ýS¨J@y Cg÷SðÌfò)ÆdoURø&4ªdH0Sø&4Ì	.×pèFviôÏÐ?É(0Ì*ô]Ó1 |
| --- | Minor | «ºÔÅ .ß*hØý¯÷i¹¬ÎtÏØr«ãëæhnÞÏG9Ü/áXÎsçì×4ã²+üþx§J endstream endobj 681 0 obj <</Filter/FlateDecode/Length 265>> stream xÚ]PËn0¼û+öªªBDEjúðÆ^¨¥`,Cü}m'Ê¡+ÙÒ¬wfÇÕ¾RràÛL¼Æz©ÁyºÐá 	#/wäo>2MòÄô'æ§y?<çF²K«$ê¶9	ìo£Íª¢;®öõ:/8VªR­ò¼6¹:|r½/#ÐH5À¦-kß©¯Z_pDµÀdoÞÜÚY3©	ÝÚÊmeø÷¾»±ºÿ2ChtS;ýZo¡»<=X¤Ë¥q²Ï-Jã¸ðJwÓtI<àWc¬3ÿ³³'>Õv,þ  ·x endstream endobj 682 0 obj <</Filter/FlateDecode/Length 533>> stream xÚ]Íjã0÷~ -;%eI	CjÇ`N¦YÌÒ±¡þÁqyû±u)ÔÀ§¿ûéêJ«´È®ÄêÏØW7sÓÕ£»ö·±râä.MÈHÔM5üÕC°J_ËáwÙ:±ú»? |
| --- | Minor | =-º§·÷Ùõ)ÜKºLèBÕÐò:. Ñç¼w-æ¤3ß¶+ËÍ øªv¡ßÈ% |
| --- | Minor | §Û$æ¾ëº(øòðr<ä³öAÈ°ÍèÇ ¯¡ìÅÝp !N³µÍ_µ3ùzûÏÌ¹¾èÅ÷}¸áÃ¹. ÝÔ_@T«\d~³fÛFh)¿Ñeç­EmªóãëÀ­jSu¦6"_1Q.ÆÏÏRùr4OeÓ7^-"		â<ïÖÓçu²§²çWÓëE»¾ ¶ÜwW­_BcÎ×ÔÞ¦óÚQ=µeò Å!VWé¼«CT¬Uû¼p/á¡æ~ÆÊû |
| --- | Minor | ÉÝ-]Ã>_î.y¢ ïu(rî}êÚX{¶ap¦h±î |
| --- | Minor | DmÜv¨'P?<ÜÐM²ËþÒj:)-¦8Fä6. ¦á_Ðð`Ý£w°M¶Ïx+ýÞtszòµ*æ^ÎPÁ»'åÁ~ÖÓÂ¦Ë<gâ º|iÝøîÞ<°JÅ< £ZUóU*o#"0éë6}Ø¦mEjEDÆå­üÏDp¡rë!yøiq9ié¾?çèÇÝißÕÍä¾ØÍüv~ý¹/®ÇtÐêönv{ÿü®ÎêàõxXd0·ã5ÓØ<ñ°1×ÔÕ:¹Å§éÇUs±A®%¤=|1wB0ËÈíòâ£ã³6 <6¹¯ |
| --- | Minor | {É=7o4pÑ¦¸½Ýëº¨g±<ó©-NIçf |
| --- | Minor | Æ«bï±ä³57Bãá^$ðöI; 1¡Ø N®æA2F}ùP^ycÆ:WûËÌËLÇýUf2f¦R¶<ÆÁiSáIq[K¸;L'áºðKîàk<_ñ3ÂbT¨èÒûj} &ð¢½çæ<:>0&p;WÄó*&ÁîôÈÙ×uÞÙ |
| --- | Minor | . kâf_àÙf. èXyh øÅ§ÆçÒ¶<Ð·¬gíÃbz¿¬'ñ}sß.þçjzÛ.»2X¥ñM³¼_Åà¥_^I«$( g¡*¥ |
| --- | Minor | ËÕ¢¬êÕÝí¾mÑÂÀ. 'xx@ H7¿aÂ"B_4«.p|K?fñõÕtÉ|fÄ¦QÆÅÎ|ëî¨|¸[Þó²0èÏ. ÛÈ)Û.ì. ûîÀÜYãñý8®jßÎg×µI1£}mxÇ"'++C#ÎÍ(cºXwXª|l\³)°êÌ½0F:3>VIU!j=Qè\l&ÕÆ_´µók°OCvUtHàÏÂ×;pr|V]®61=za·ëçÛùü!< &é º9æÇt¾ÿjÞsÉ{.úÒ³[y(­Þ÷±Æó%°Þe¶ÚP~û.¤â |
| --- | Minor | ~h×íÂ(­ñ¶h2ð |
| --- | Minor | ±?ä}¥ |
| --- | Minor | ¶½ÌgW=x7´\=. [úQ¨¡v8üêºUW}óÐÌ®Ï-ÙIs;½Xä4ÚÈuù¨®×{¢¥×ír5½[w(xùüØ¬n0:½~À$£G*{ìÓËkHG¸öaº¼@m¢ÛæÐ¦o¯ |
| --- | Minor | vwyßjÓº{. ×ßÆ)?¼n%Ñ&×.'P#î	-{çÛ\(·ÆçP{ß. ¦K Ðy z²ºÁÿ7ÓÛ[ªnæË]ÙÿÌ6 Í\§¨Ysûy9]xéwhlå¤X°oÕ<\´³«öö¢5.ÁÀX0p5Í¤Ú÷Kp/ÜûØÌÚ[Ln;Ã¤ÞX°ï§NÌ0)·WÜ+.WílNÅÈå­´}¦íê|ú·éåò-o¯âû|wµ{¦îNÆ'Hw^f6*»æout©ãûVÚ%½]É3Æ#Þ±Ø­e_»[Ün¥ñöèN¥ñ"é>AE. ¥~ËÂtlµÓÆîÙHi·2D©ÝÊ8âÕÊ4â5Vnöh¤»±®0#éN |
| --- | Minor | >%íg÷Ð-¯"6MÒï{xrxU#Þ8ÞÑ®UñL´.ÞHgàúw¯mñ.#éLá¢]«ïñ4fÀsÝ"]J¿7u6©K¼ÁC]à |
| --- | Minor | ¶Y¦@ú^ÅðÎþöëD}@¸[:)£/qçg·+/p!ÛØ~»C5ÄTpÓTÃñöìð.jpÉdK¶ Ã[s+ÈL¿+õÏõît ëqáXØk"Q M 1Q¶Cy |
| --- | Minor | áÔvæÃòÖûfz. ÀmpZÅÙrÀ. ×ÎmUlÕ=ÎoÕn¶j@º[5 ÞmDúòqT. ØÒC³5(ø&=MÃ·Ô"n¿Äõþß$ööûÕìö«ÁÞÜAW:÷ïlï ½ /×ÙþrA~ú¼*ÇÑÎIaÛýÄ]T{»_ |
| --- | Minor | ¯Õ~u>â÷«9Èëbî¿LV>P²{hñ]¹£µÀ;½] Ù¯Æ¼»_ |
| --- | Minor | ¦·_ |
| --- | Minor | ±²_ |
| --- | Minor | ~¿òÂÏÑFýapNÈxçxôýÀÅÞOëÞAoïuï ´÷ÉÖ<¤÷ÁÖç¤÷¼Ö§û¥÷¶ÖxH<äwÿSgVéÜ£ââ3*£¬½Ç3ÔÞÝÒIïê¬kgïæ¬kiïãI¯X8%Ý:ìâü ù{¶åu¶-ö]MoÓ|¿dÓf®ßêNÆûï¿W)ÿ¯§Înoßí7ÂX·tlY·iöCãÖg÷ãF°óu¤±¸Õ" öm¦sy6ð\¬á­?ìüÜè÷s3¨6_÷§2|n:m·æóëiïsììf4 Ç=. 4Cãh3Püé ÅK7<\ñ6í+wì| |
| --- | Minor | <Ð4ou®àX@ a¡ÛO;`ì|Ä Ê¼Ø*ÃßÐG¦Îä«!GæéO½×YøÜèy¶²Áq+¤o·æ[l1¯ÁÿXx×aÃ;×ùRE»·Ð²C»Ñ»íJ àûãóÆK_ø©Ë |
| --- | Minor | òü-}|ð. Ç	äÌ§Jdí4^ÌÙàlMÚf(Ï¢iä¦Ý lÙZ<4òÎe<H¥IYÍÊ±~kêÓ³ÞrêKîmkÄk)ø¶Óf·T÷Ü!fî|T0k·åè7ói»eIÔáí6¦b}of8g:§SGñ<*û+8}V 6_Aûñ1wZ|5 §¯ttã &YHàåÛãSh¡PÞö(4îtìÒì´È1±/ÝÂmØmñ_Í]x}u0_hý |
| --- | Minor | ^ý?Å¹ endstream endobj 678 0 obj <</Filter/FlateDecode/Length 368>> stream xÚ]]k0ïý¹ìÅ¯;¡µ	ë6j»Ý¥zÚ	5¨ý÷Ó¼¡ ç=9ÇÍ]!¹_º«JØ¥µ¦¾uEìL×F:~Àê¦. ³jrÜl/Ôh¹ÅÛ¦øù~~ßºVÈL¨Þ÷º7¡§cîsVÓã]. »òÞÔòÒ± Þ´RäÓJõ¿÷ ì|©~Íýídîy+?5â ÀÇÚBtÜRZ PAdu1ÈêÖV¡`²^^@¢oAÖµÜ^ |
| --- | Minor | ç x	QQ´2£¢hxÐqDt1êãÐÈC¡Ú)Aci	¿Z2ñ±ÀMklæ&Íö°jÔzjµC3Ds¿IIUUfÿüÿ» endstream endobj 679 0 obj <</Filter/FlateDecode/Length 463>> stream xÚ]Oo£0Åï| »ZU |
| --- | Minor | +EH	i ~xþ¼aËj[¹nñ«Ä©s­·áê+öÜ¹(¢íM_Q\îëñ¹î­7Õßýçï?û·¡¯]*ï7ÃW{ÿñ¾Kµhí	¦ï·Ñ I®¶Ûe²}åNX­"!â·9òeò7q·n£ýµ¼{ñ­õ;»òÞ®ãøe{ë&DEÂ¥ÐÖ­½uc}íÎ6Z%óUÕn¾Èºö¿ó\ÂíxjþÕ~1O7³ydi¨¤AR qFB>õ Ò°Ô KÒ. é÷b*3 jaLjeI ¹QÙ#ÊHÐ¢7 hÉJ´h»ÄÔBB²'Ðg$èTÈCÞ Ea*9º'. !ADÌÕæFµ9æ§ÁS¡ópÆ¡ui#´'øP»bÔ®ÕLLSb*#Q²ÖÌÁ KsGíýÔÚüñó+_Ö`YÞÝm®ÞÏË6<¬é²Q³??q¯pý½ endstream endobj 680 0 obj <</Filter/FlateDecode/Length 499>> stream xÚ]Kkã0F÷þZ¶ÅYRÁG |
| --- | Minor | éÌÐ4L·­dµlg?¶¾oºCG{ïµïª}åºIÄ¿üÐì QQp)Ü¡µ×±n¬¯ÝÅFëd~ ±.ç§¬kÿ×Üv:7j¿. O·óò =c%÷­@Ì@k¢5fÌ@3Pàö z®@ô xæ¨DOM¢3 ùÔ$xJäSpÑ%.ýS¨J@y Cg÷SðÌfò)ÆdoURø&4ªdH0Sø&4Ì	.×pèFviôÏÐ?É(0Ì*ô]Ó1 |
| --- | Minor | «ºÔÅ .ß*hØý¯÷i¹¬ÎtÏØr«ãëæhnÞÏG9Ü/áXÎsçì×4ã²+üþx§J endstream endobj 681 0 obj <</Filter/FlateDecode/Length 265>> stream xÚ]PËn0¼û+öªªBDEjúðÆ^¨¥`. Cü}m'Ê¡+ÙÒ¬wfÇÕ¾RràÛL¼Æz©ÁyºÐá 	#/wäo>2MòÄô'æ§y?<çF²K«$ê¶9	ìo£Íª¢;®öõ:/8VªR­ò¼6¹:|r½/#ÐH5À¦-kß©¯Z_pDµÀdoÞÜÚY3©	ÝÚÊmeø÷¾»±ºÿ2ChtS;ýZo¡»<=X¤Ë¥q²Ï-Jã¸ðJwÓtI<àWc¬3ÿ³³'>Õv. þ  ·x endstream endobj 682 0 obj <</Filter/FlateDecode/Length 533>> stream xÚ]Íjã0÷~ -;%eI	CjÇ`N¦YÌÒ±¡þÁqyû±u)ÔÀ§¿ûéêJ«´È®ÄêÏØW7sÓÕ£»ö·±râä.MÈHÔM5üÕC°J_ËáwÙ:±ú»?. |
| --- | Minor | Sentence exceeds complexity threshold, split for readability. Applying the split needs --strength moderate or higher. |
| --- | Minor | none (split proposal only; source not rewritten) |
| --- | Minor | none |
| --- | Minor | Check: NEEDS-LLM |
| --- | Minor | Flags:    not-assessed |
| --- | Minor | SENTENCE (Line 1103, 135 words, 2 clauses)  [Script] |
| --- | Minor | ßÒ¿^ßû¶ìdø\LågS=?riDíÎüqÈEv¸_'×Ý¹Ûm Äê}^û:wñ´«ûû±´½µî"éÁ·nÃðéZ×M"Ä/'aWõµ»eåÆ²»¸`Î_"¶ùü%ëêoýfi§sõ¯áòe±L<¥(ÐúH;ô)V1 DWkÁH²IZc$çm@@k¢5.°Î@4ÛhFYÝÆ03/ ÅØ{3C¢#ÐÆ{2hHÈ Bt |
| --- | Minor | ÁÓà©póO±'KÒØ-ö®±`!º§åÈFM¸X\4jÂÀÅxÈÂ9¸(¦Ató38MKB×btdP£ 2hI´FKk­ábiMb%Ë3YX[Ôe |
| --- | Minor | "×vÇj}T¬Í¾Z8ÿÕâ«EúÒïUæ´ñ·y¹îË3õx¥ªÛ8ÎËüs´¼MçÏÝÐË,ÿû+ý endstream endobj 683 0 obj <</Filter/FlateDecode/Length 598>> stream xÚ]]kâ@ïýsÙe)ækf,`£a¥ÛíRÛ½KÑ |
| --- | Minor | ¢^ôß¯ÉóÒÂ -<Éç}fgoV¶9éïþXmÃÙì¶îÃéxé«`ÞÂ¾i'qbê¦:ÆÿÕ¡ì&Óü±ì~`¦Ëùï? |
| --- | Minor | ßÒ¿^ßû¶ìdø\LågS=?riDíÎüqÈEv¸_'×Ý¹Ûm Äê}^û:wñ´«ûû±´½µî"éÁ·nÃðéZ×M"Ä/'aWõµ»eåÆ²»¸`Î_"¶ùü%ëêoýfi§sõ¯áòe±L<¥(ÐúH;ô)V1 DWkÁH²IZc$çm@@k¢5.°Î@4ÛhFYÝÆ03/ ÅØ{3C¢#ÐÆ{2hHÈ Bt |
| --- | Minor | ÁÓà©póO±'KÒØ-ö®±`!º§åÈFM¸X\4jÂÀÅxÈÂ9¸(¦Ató38MKB×btdP£ 2hI´FKk­ábiMb%Ë3YX[Ôe |
| --- | Minor | "×vÇj}T¬Í¾Z8ÿÕâ«EúÒïUæ´ñ·y¹îË3õx¥ªÛ8ÎËüs´¼MçÏÝÐË. ÿû+ý endstream endobj 683 0 obj <</Filter/FlateDecode/Length 598>> stream xÚ]]kâ@ïýsÙe)ækf. `£a¥ÛíRÛ½KÑ |
| --- | Minor | ¢^ôß¯ÉóÒÂ -<Éç}fgoV¶9éïþXmÃÙì¶îÃéxé«`ÞÂ¾i'qbê¦:ÆÿÕ¡ì&Óü±ì~`¦Ëùï?. |
| --- | Minor | Sentence exceeds complexity threshold, split for readability. Applying the split needs --strength moderate or higher. |
| --- | Minor | none (split proposal only; source not rewritten) |
| --- | Minor | none |
| --- | Minor | Check: NEEDS-LLM |
| --- | Minor | Flags:    not-assessed |
| --- | Minor | SENTENCE (Line 1103, 450 words, 10 clauses)  [Script] |
| --- | Minor | ²£Ûç°¿¼ýíëK;S«_>º`ñfµý8ÃaÓîf>3½nkNçþÃÜ,ëã[ø6<{êëÐ7íÞÜ¼æÛñÉöÒuïáÚ³&Åøu1ñªcN]Y¾l÷a2®×ÏbÚú¿÷3Ë¶·]õ·ìåñýuyeñb¤|$'Z¸@	²O´ä] QÁ¨.!UÈ¡5û2¨`ªº¨îDTOgc%©SÏJÑÚw©R{H©EJ¦ Je+H9ï å3Ãýª9¾YÞÝC88§áàDJ­êJ-â¬³5ÄY;F)É,YáàD8¤ôÅÁÒ/Â!á\,*àpò,{H°µYÕÃÈÔ=JÆ=XºÎáàE8XºÎáàEêê9RnÚáÒ/NÔs¤¶ô#µ:UR§ÊBj»ã¼HÔórÉd^"Ýgíu",'ïqð"îÁÒu#/ÒïÛôKýr>=~°*î£ö«¯5z²þz2vhf=ïH¢8rh<µ¸H!ö´t75Í¯aÀ |
| --- | Minor | ùs0W¾¿Éq|xM>'|wì]ãß?Å[ó endstream endobj 684 0 obj <</Filter/FlateDecode/Length 428>> stream xÚ]MO@ïü=ÖÃ×²hBH X¦j¤<RV»-=ôß»ïNíÁð0Ì¼ó±_ÖU­YøïfìÅnÐ½¡ãx2-ííèn¾¼¹{wh'Ï/×íôÚHøÏË§¯Ûr½®Ãàîs³ èiÇ.óD"º¼×Us>Ît¨õnYæ	áXÅãlÎb±ìÇ-ÝÀöfz2ÞÅgÙ8Ks¦:Eàå¹¹¦nìé8µVïÉË Ùj{¤ûßâC¶»î»5^JëÄÅ2·0`²½/!¸`Á%³´Ì÷àc¡±N©À£¤H-ÇN3°&Ës	v6 \±}~d;üeèX¢)QLW¦ÌÈ%ïQä¼½KÎ+Ñ{Â±	bë+è«ý*öQÎcb×©0+Åu*Ô>8¶Ë×>p@HþÎåïhÅÓsÓÆTÃË81BIÄu»|èSq"fS¤Ü½eÎÆúØìðu»1v·Ü¢»­Å |
| --- | Minor | ®ÿÂ4Nr×/zÑ endstream endobj 686 0 obj <</Subtype/Type1C/Filter/FlateDecode/Length 7132>> stream xÚ¥Yxe¶a`øl#ÔùAîâb@t½ô>I&eÒ¦×3½'d2éôÐ¤%Y |
| --- | Minor | *®wqYµëê÷Ç/»{¿IÐUW÷º÷>IæûÎyÏ{ÎyÏùÙ¬Ñ£Yl6;tíòUëÖí±~ýùóï,IÆ¦oåcY,f63Ëa&Ü\;ú!£e±Ø·ï¾æN¾®º¼²¦Ç>»õ Í?ñbÆ¬y>·|Ãös®G¥¢Å¢â£RS£òÉÈ?QyI £R¢RÅD¥eg&¤g%Æ§F¢²Y±ä+%=M8_ 7oÁÜyóH=3|þ¢EÏÌzÞ¼EáËSÉßEG¥¯^AN#?¤oMNÃg,Iz*77wnTjÖÜôÌø¥3gç&Â·ÄfÅfæÄÆ¿& ß>ÌÜoé©ÂlQlføúôØÌ4âþ¤	£îõ gò¨pÖTÖtÖ\ÖâÑËY+Ø«ØkÙëÇlgE±¢Y±¬øQÉ¬T¶p¬ÍbkØZ¶­gÛÀ6²M,ÛÌ¶°­lÛÎv°lk"ëÖ£¬{Y49që	ÖÖLÖ,ÖlröS¬y¬ù¬§YXY/°V°^d­f­a­e½ÄÚÀÚÈÚÌÚÂÚÊÚÆÚÎdí`ídífíaývÍÍ*gg°?ÕÃã¼1Ú:éäNæº¸xìFj*ui\ü¸q¯4>a|íøo&èBÁ÷\½<qÅ½«ïÜwéþY÷_yÀò`>ooà¡¥&­çsø®°ÜÉâ>üå#ðhØ£åûèÕá¿;ÅÉhCú9~öá7Ñ±W9LòÐü¹'ãG1?§Ì½°ìÁ+0PõöEOdsJ/P§gËl*VV«UwÇ¨x§J0:ÝwÐøJD2êíR@«_JZ¶wµúyÞ¥K¥Ñ@mLí½LÃZÄjzùØµ3­@} xÒs4ÄÁfc>Ê\Âè7~ôYüìx£÷3À\á½µíÒbÁfH/HÈØ½íÉ¼exÁß&òõÊv0 |
| --- | Minor | ¦×Q¿bã¸kp |
| --- | Minor | =rühÓexâNÅ×ô7÷] ¯ÆyÅj©. |
| --- | Minor | ²£Ûç°¿¼ýíëK;S«_>º`ñfµý8ÃaÓîf>3½nkNçþÃÜ. ëã[ø6<{êëÐ7íÞÜ¼æÛñÉöÒuïáÚ³&Åøu1ñªcN]Y¾l÷a2®×ÏbÚú¿÷3Ë¶·]õ·ìåñýuyeñb¤|$'Z¸@	²O´ä] QÁ¨.!UÈ¡5û2¨`ªº¨îDTOgc%©SÏJÑÚw©R{H©EJ¦ Je+H9ï å3Ãýª9¾YÞÝC88§áàDJ­êJ-â¬³5ÄY;F)É. YáàD8¤ôÅÁÒ/Â!á\. *àpò. {H°µYÕÃÈÔ=JÆ=XºÎáàE8XºÎáàEêê9RnÚáÒ/NÔs¤¶ô#µ:UR§ÊBj»ã¼HÔórÉd^"Ýgíu". 'ïqð"îÁÒu#/ÒïÛôKýr>=~°*î£ö«¯5z²þz2vhf=ïH¢8rh<µ¸H!ö´t75Í¯aÀ |
| --- | Minor | ùs0W¾¿Éq|xM>'|wì]ãß?Å[ó endstream endobj 684 0 obj <</Filter/FlateDecode/Length 428>> stream xÚ]MO@ïü=ÖÃ×²hBH X¦j¤<RV»-=ôß»ïNíÁð0Ì¼ó±_ÖU­YøïfìÅnÐ½¡ãx2-ííèn¾¼¹{wh'Ï/×íôÚHøÏË§¯Ûr½®Ãàîs³ èiÇ.óD"º¼×Us>Ît¨õnYæ	áXÅãlÎb±ìÇ-ÝÀöfz2ÞÅgÙ8Ks¦:Eàå¹¹¦nìé8µVïÉË Ùj{¤ûßâC¶»î»5^JëÄÅ2·0`²½/!¸`Á%³´Ì÷àc¡±N©À£¤H-ÇN3°&Ës	v6 \±}~d;üeèX¢)QLW¦ÌÈ%ïQä¼½KÎ+Ñ{Â±	bë+è«ý*öQÎcb×©0+Åu*Ô>8¶Ë×>p@HþÎåïhÅÓsÓÆTÃË81BIÄu»|èSq"fS¤Ü½eÎÆúØìðu»1v·Ü¢»­Å |
| --- | Minor | ®ÿÂ4Nr×/zÑ endstream endobj 686 0 obj <</Subtype/Type1C/Filter/FlateDecode/Length 7132>> stream xÚ¥Yxe¶a`øl#ÔùAîâb@t½ô>I&eÒ¦×3½'d2éôÐ¤%Y |
| --- | Minor | *®wqYµëê÷Ç/»{¿IÐUW÷º÷>IæûÎyÏ{ÎyÏùÙ¬Ñ£Yl6;tíòUëÖí±~ýùóï. IÆ¦oåcY. f63Ëa&Ü\;ú!£e±Ø·ï¾æN¾®º¼²¦Ç>»õ Í?ñbÆ¬y>·|Ãös®G¥¢Å¢â£RS£òÉÈ?QyI £R¢RÅD¥eg&¤g%Æ§F¢²Y±ä+%=M8_ 7oÁÜyóH=3|þ¢EÏÌzÞ¼EáËSÉßEG¥¯^AN#?¤oMNÃg. Iz*77wnTjÖÜôÌø¥3gç&Â·ÄfÅfæÄÆ¿& ß>ÌÜoé©ÂlQlføúôØÌ4âþ¤	£îõ gò¨pÖTÖtÖ\ÖâÑËY+Ø«ØkÙëÇlgE±¢Y±¬øQÉ¬T¶p¬ÍbkØZ¶­gÛÀ6²M. ÛÌ¶°­lÛÎv°lk"ëÖ£¬{Y49që	ÖÖLÖ. ÖlröS¬y¬ù¬§YXY/°V°^d­f­a­e½ÄÚÀÚÈÚÌÚÂÚÊÚÆÚÎdí`ídífíaývÍÍ*gg°?ÕÃã¼1Ú:éäNæº¸xìFj*ui\ü¸q¯4>a|íøo&èBÁ÷\½<qÅ½«ïÜwéþY÷_yÀò`>ooà¡¥&­çsø®°ÜÉâ>üå#ðhØ£åûèÕá¿;ÅÉhCú9~öá7Ñ±W9LòÐü¹'ãG1?§Ì½°ìÁ+0PõöEOdsJ/P§gËl*VV«UwÇ¨x§J0:ÝwÐøJD2êíR@«_JZ¶wµúyÞ¥K¥Ñ@mLí½LÃZÄjzùØµ3­@} xÒs4ÄÁfc>Ê\Âè7~ôYüìx£÷3À\á½µíÒbÁfH/HÈØ½íÉ¼exÁß&òõÊv0 |
| --- | Minor | ¦×Q¿bã¸kp |
| --- | Minor | =rühÓexâNÅ×ô7÷] ¯ÆyÅj©.. |
| --- | Minor | Sentence exceeds complexity threshold, split for readability. Applying the split needs --strength moderate or higher. |
| --- | Minor | none (split proposal only; source not rewritten) |
| --- | Minor | none |
| --- | Minor | Check: NEEDS-LLM |
| --- | Minor | Flags:    not-assessed |
| --- | Minor | SENTENCE (Line 1103, 659 words, 6 clauses)  [Script] |
| --- | Minor |  W/³m:ñÁ5îEy°26bGÐkL*g«!Ö§2C;ÝñÃ>ãæ¬çÓcb¶¯ßÔ²Øþ7hpB©¥â2²òý7ÐTkÊF:)ÁÉÌÅ6ú{ |
| --- | Minor | ÑXÄ6¸B³\8b |
| --- | Minor | ÔùÊÜìR1Ô¢´<`÷»:ªÞsöFÑcö4}zÍìú½ÍíörÊ@'Ð ´Ê³£§G?¡èßù8ëbôÂ÷­Ä³SdpÛ×à(ÿ`!³ßÇ>ví¬qæ ëÌÛ¼rqøª¹hc4-!dÈÔn Qb!Q¥ìjRû´È7íS#ñÓø%À§ÜNÈj¡AV©<\{)a^L îr¥UoÐ ¥Vk²ØÓ]î£¡#¯RaÏ¯È³nò=[W`Éªê>¨ ô E¡ª\¼R[9x ÌúrµB+SPÔF¡Ä)ö³9L!jäYÊM¨£~Ýý¼`	ìØ îjÜû /F.'o-%sQàÁê÷¾á;Þ·DKCVZ¼c3.àkU"PSây©À |
| --- | Minor | Ï`t³Öø?à[ýV¿¥Êhµ7¬&Gà\K¿,PÑT+15eÑ;t¯\ÐQ.W [ÉEìMúÑµ&tÍÏî¾Z®p=wEèiÆsq+ÏiÀÛh ºH/àGyÞË¾w»Þ¨;Ñ~¤Ü	ëº-4ìVìÌAÉyÒ}9c#VÅî>TRNÃ4t[ûk?!w]#w½÷>}úýÏó<M1H9âT#X«íMÎ6U^ZòöOù°@ªÖÉ4z)(¨M]Ñ§MP[îk©év÷ ;å %	¬×hò^mÛOr@êi¥¡Ô\möuÜÁÛVcsyS]]ÕÑÎê.¯NM`PS(Ðäo¨qhjã`Ó®q«6gÆKL.÷I×Zë>Ê+qæú¦<ÿnqåà\û4#ç AÔË;<õ8S&*ËvBP~®L`ÒµfKUªôáÌ~NÿvÏ^Â²b*ì:Ý¬²©jV}kø¸×I$*åHÊeàpÙä¦O	ÐK~æ) ¯xJgÇÌÑËðãCoÿ( à.7ÌÏ©4·IØ«ñÁëÐÙ[]ïØß~Z¡ªª¬ÉÛæ¹øcäò×7J¨­õÑàw³·Ö#ßTêì0ZªÈ­Vª¼ÈQ(PC^¸oäKvI£´2½zÏ¼Å@íÊj>CC­ÞVOÌ	íf#Á3³X :^ª1%q@éq£R& ¥d¯R¸ëøBe:q@êÔ[%Ü×ÝÝùåG&Ö¡GÀ1â¯DEÚ:gãÑGÕ<¤30/pñrÞ¿Baq4¡Éuån#5lâÏüzMßô0uz*%eÇòV¼ë Álñ<õh´³ÍßÕsí¤? T{SÚ4lKÃ£»^Úäî×ÿÞÏî¸êI2ãx6h©Î1ó¸xæàExÂó+o£ñ(ÝæÒàã)G(ÿÎÛÝ6@C£û­ç»¯^(iê=ûöæ.JÜ³i{FLð5JÕÏFÇÈñh	÷î |
| --- | Minor | Ø¾Tänf«ýÄõ>R©ÜøMD0©­À/hK½© ¤qT%Z |
| --- | Minor | Z¾b¹^¾Ãarçñf£ðË©4¨¼ÐiÄxñßfò9bÛá )¾µgP¸ÙmóêMnß5;OW²²º¿t5Oì^H¦IiÎ,NØïÈÙïúH¥ =¸(R+Í]L*Ý°ÉF°£MFk©¤Íä·Ã-¸óÍá£G\ÿàuNX-b«Ê¡pIk2`¬Û±(!~ÁÓë >S\öQ´9Ø9Ê®«­©á çò ¨Ú³¨N0ÅÒ9 Ë¹ó+H¾øIÛ$ÏÚ +Ý¥0êl@yJ<%:Vá±µz |
| --- | Minor | Û2ÍÚMIÉ[aµ¶oÃ×îV©UmVÐjtÚ"QV&MsÃÂRÒL[êO_l¤=¼*{¥Á5Ã-¡P©ÓÇB6H ÏBÓ*Ñ~ôA?ûd-ã®ç ¥x)OS¬×B]¡r ,à79«LvKsêÐÛô^BØÅh.~'æÂó4qäF¼³|[ÏÁ ÔW¡Q®Ú`$ùlÖYeéKñ´Ysåo2©?à)H>(Do0Ñ`ôÞ6Ðï|ô>PWë¶ïÁc0â¹¤ïj5L¼]×Åaö¢<^Ã`+Xõ¶ÇÐdÍ/¶k@T.äÒCkÇBO@¸múxø3¼wóøØPÔ_³o~ÍAÛNó²ªÓÒ²²ÒÒª³ª«ä·x{%zþk6Zãç ÞÌÎ¤ÜÌt¡/£´4Ùé ÒÈ` Ê`ÐÑ°<acRTJÜÐRJÆâz÷:',©dZ|ìâ>Ã¨yn«Í.Ê%wHImÔA±rèe\Âªj ]íR3Á7<J#±r9.\JÄ:äG> *¿Ýêcc&qu{y@>Q	J­V?ûûz>)àÐSRÜEtÉfõR?±Àç²Ø-à·Â"µ½JøÅ6]>©\.¥AnQ(?6ðÈKR­yØð&HÑr }f%IÑUh,/zuLÑ­D/È£Tµ]P0Õ7·6Lµz Â%7(i1ËNç¶ºì%o£ùÈÌ5æàG@F¥îÐæÉ Wê&Éz¸Çt¸æòI7ø\2(¦×Ø´ |
| --- | Minor | Çðu>0çCh*óÖðÐ.t£	ß:øÙöàÁ?qÐwx²b	PùRÈ#%½FïqQùëx¦,D£ñ4~7òkír½[_¦³jA ½V+¡þ ç9Z&"Q¾á~r#ó|ÈÅ¿]G¥Å-Y'e8Ô*Ì 5E3-åÎ jnaîDE<£Åd#ü'½F"N¥S­Å3âVãeä'~æ×P-ÿSî!'&âB¢LÕ©õZÂ/ÝRGMsi*æ[>O+ÉY&=Ôî¤r´ÌG Má¢ÐÆ´E4dN#èJmR:.0X>´oªSC&PCFnn~S{=iA:µójù? |
| --- | Minor |  W/³m:ñÁ5îEy°26bGÐkL*g«!Ö§2C;ÝñÃ>ãæ¬çÓcb¶¯ßÔ²Øþ7hpB©¥â2²òý7ÐTkÊF:)ÁÉÌÅ6ú{ |
| --- | Minor | ÑXÄ6¸B³\8b |
| --- | Minor | ÔùÊÜìR1Ô¢´<`÷»:ªÞsöFÑcö4}zÍìú½ÍíörÊ@'Ð ´Ê³£§G?¡èßù8ëbôÂ÷­Ä³SdpÛ×à(ÿ`!³ßÇ>ví¬qæ ëÌÛ¼rqøª¹hc4-!dÈÔn Qb!Q¥ìjRû´È7íS#ñÓø%À§ÜNÈj¡AV©<\{)a^L îr¥UoÐ ¥Vk²ØÓ]î£¡#¯RaÏ¯È³nò=[W`Éªê>¨ ô E¡ª\¼R[9x ÌúrµB+SPÔF¡Ä)ö³9L!jäYÊM¨£~Ýý¼`	ìØ îjÜû /F.'o-%sQàÁê÷¾á;Þ·DKCVZ¼c3.àkU"PSây©À |
| --- | Minor | Ï`t³Öø?à[ýV¿¥Êhµ7¬&Gà\K¿. PÑT+15eÑ;t¯\ÐQ.W [ÉEìMúÑµ&tÍÏî¾Z®p=wEèiÆsq+ÏiÀÛh ºH/àGyÞË¾w»Þ¨;Ñ~¤Ü	ëº-4ìVìÌAÉyÒ}9c#VÅî>TRNÃ4t[ûk?!w]#w½÷>}úýÏó<M1H9âT#X«íMÎ6U^ZòöOù°@ªÖÉ4z)(¨M]Ñ§MP[îk©év÷ ;å %	¬×hò^mÛOr@êi¥¡Ô\möuÜÁÛVcsyS]]ÕÑÎê.¯NM`PS(Ðäo¨qhjã`Ó®q«6gÆKL.÷I×Zë>Ê+qæú¦<ÿnqåà\û4#ç AÔË;<õ8S&*ËvBP~®L`ÒµfKUªôáÌ~NÿvÏ^Â²b*ì:Ý¬²©jV}kø¸×I$*åHÊeàpÙä¦O	ÐK~æ) ¯xJgÇÌÑËðãCoÿ( à.7ÌÏ©4·IØ«ñÁëÐÙ[]ïØß~Z¡ªª¬ÉÛæ¹øcäò×7J¨­õÑàw³·Ö#ßTêì0ZªÈ­Vª¼ÈQ(PC^¸oäKvI£´2½zÏ¼Å@íÊj>CC­ÞVOÌ	íf#Á3³X :^ª1%q@éq£R& ¥d¯R¸ëøBe:q@êÔ[%Ü×ÝÝùåG&Ö¡GÀ1â¯DEÚ:gãÑGÕ<¤30/pñrÞ¿Baq4¡Éuån#5lâÏüzMßô0uz*%eÇòV¼ë Álñ<õh´³ÍßÕsí¤? T{SÚ4lKÃ£»^Úäî×ÿÞÏî¸êI2ãx6h©Î1ó¸xæàExÂó+o£ñ(ÝæÒàã)G(ÿÎÛÝ6@C£û­ç»¯^(iê=ûöæ.JÜ³i{FLð5JÕÏFÇÈñh	÷î |
| --- | Minor | Ø¾Tänf«ýÄõ>R©ÜøMD0©­À/hK½© ¤qT%Z |
| --- | Minor | Z¾b¹^¾Ãarçñf£ðË©4¨¼ÐiÄxñßfò9bÛá )¾µgP¸ÙmóêMnß5;OW²²º¿t5Oì^H¦IiÎ. NØïÈÙïúH¥ =¸(R+Í]L*Ý°ÉF°£MFk©¤Íä·Ã-¸óÍá£G\ÿàuNX-b«Ê¡pIk2`¬Û±(!~ÁÓë >S\öQ´9Ø9Ê®«­©á çò ¨Ú³¨N0ÅÒ9 Ë¹ó+H¾øIÛ$ÏÚ +Ý¥0êl@yJ<%:Vá±µz |
| --- | Minor | Û2ÍÚMIÉ[aµ¶oÃ×îV©UmVÐjtÚ"QV&MsÃÂRÒL[êO_l¤=¼*{¥Á5Ã-¡P©ÓÇB6H ÏBÓ*Ñ~ôA?ûd-ã®ç ¥x)OS¬×B]¡r. à79«LvKsêÐÛô^BØÅh.~'æÂó4qäF¼³|[ÏÁ ÔW¡Q®Ú`$ùlÖYeéKñ´Ysåo2©?à)H>(Do0Ñ`ôÞ6Ðï|ô>PWë¶ïÁc0â¹¤ïj5L¼]×Åaö¢<^Ã`+Xõ¶ÇÐdÍ/¶k@T.äÒCkÇBO@¸múxø3¼wóøØPÔ_³o~ÍAÛNó²ªÓÒ²²ÒÒª³ª«ä·x{%zþk6Zãç ÞÌÎ¤ÜÌt¡/£´4Ùé ÒÈ` Ê`ÐÑ°<acRTJÜÐRJÆâz÷:'. ©dZ|ìâ>Ã¨yn«Í.Ê%wHImÔA±rèe\Âªj ]íR3Á7<J#±r9.\JÄ:äG> *¿Ýêcc&qu{y@>Q	J­V?ûûz>)àÐSRÜEtÉfõR?±Àç²Ø-à·Â"µ½JøÅ6]>©\.¥AnQ(?6ðÈKR­yØð&HÑr }f%IÑUh. /zuLÑ­D/È£Tµ]P0Õ7·6Lµz Â%7(i1ËNç¶ºì%o£ùÈÌ5æàG@F¥îÐæÉ Wê&Éz¸Çt¸æòI7ø\2(¦×Ø´ |
| --- | Minor | Çðu>0çCh*óÖðÐ.t£	ß:øÙöàÁ?qÐwx²b	PùRÈ#%½FïqQùëx¦. D£ñ4~7òkír½[_¦³jA ½V+¡þ ç9Z&"Q¾á~r#ó|ÈÅ¿]G¥Å-Y'e8Ô*Ì 5E3-åÎ jnaîDE<£Åd#ü'½F"N¥S­Å3âVãeä'~æ×P-ÿSî!'&âB¢LÕ©õZÂ/ÝRGMsi*æ[>O+ÉY&=Ôî¤r´ÌG Má¢ÐÆ´E4dN#èJmR:.0X>´oªSC&PCFnn~S{=iA:µójù?. |
| --- | Minor | Sentence exceeds complexity threshold, split for readability. Applying the split needs --strength moderate or higher. |
| --- | Minor | none (split proposal only; source not rewritten) |
| --- | Minor | none |
| --- | Minor | Check: NEEDS-LLM |
| --- | Minor | Flags:    not-assessed |
| --- | Minor | SENTENCE (Line 1103, 356 words, 5 clauses)  [Script] |
| --- | Minor | ]oêIÇôëÉøu¤wÚi!¼¸t(§Áj´¬¯¡:>êçFáÅ¢ÙBYr~=PÿÙ¤Q½í?F1ùö54Ãt0ßðìÍFÇY Ê\PáPtæmfÒâ¤ïCPKWI­FW­µiÉ¨Ò)u <vè ?ëÉU;Hst2é	ýê¬mil:óÅ»%«ÖÞû{úÏðÕO	ö¤.cefðô&M0 |
| --- | Minor | %.;@óï\í47ì§Ê)³Ö¦dgj³âcâC¦*$E,ZÞ¯s¨âTJ=4æ¿ÞaX |
| --- | Minor | Â¨úgÅ¿õ?Â0éÝ`ú9m"h³úM¥%§<§=§ÐLDñýna0±ÃRêåRéÝÚÖÕmêòñLµx!§­Tè·ûG0øöé»ä{¨*ÇpÌ§1zä |
| --- | Minor | ±^å?Ç¼¢­ÒlÃð£ÿ®á¬|Yt~òbR:õb¹Uk§ZMÍ-mÍß[ ¤·¤>¨Ábr¡Gn¾{óo,£Ä@,sÕe±13ï!oãÇ^&ìÐ¼fª?Üsx¸Îÿ óÝ¬:r·(k·xÎ®òÀ»&Êâ6Te7 MJL \R¹ä;Ý§wåA¢ÕêµxôÐf>Î`*åzø:+IË+¸` FSIõy¤÷þÄ9§Ü ¥7~¢Gã35|³ t2ÝäÛòM:¾HA |
| --- | Minor | jÊ®üm |
| --- | Minor | ù}Î`³~3±ðLD×áÅhôèq²HQ­àÍXùß4#%è	Òø¯~õÉ©ßõ¶â4Dñ¼xâ |
| --- | Minor | 6=CààC¤ÄtÔ¢W3>ä sè*-å¢©þ ¾¾æM<Æ×ÿmDÿOäIo4éý®}Ä½qZHÜßÄÄïÚ¿Qqé)ÜÐÁ üø­4ÑÏ4 ¼<¸?byûÑ×ásêæüËx w|Ï¹_]°_7Õ×¿Q2õgJìTÎG¸·Ë·&«)*2]¹f¡ðü±õó7ñ0ØÓ:eæòù" þNÒÆ¬/%Æ (ë«B2~.ÍN °_»ÎL¯Ãå?I¯ÄÄ¸_J¯ùx'ã±ÿ5¨UÛÜ ÏÂlm6µ»yj1è ól;T@8²«è,AôdXu4p¾·½¨ß,RÑ¤{©ôjbç 2<·Üê^è¦þ3÷ò Hs)**(ÔåÊ*V4ÔUwØÛ¾?ÃKÞùýK¾B½÷µÛª²0N¥X2³º§^¸@ÃaßÇ-}g{ÎBtÉU±ä*¡=ëg@ÞfÚ x |
| --- | Minor | ¦ñdåëóPB=ü"Ög=#¦_òÉ/]ñü½&Ü@éEÊêçu¢Ù_Öu¬.-ñ1ü_pPBåwÿñ¦êg_à0ÉÌ=<"-`ÁKB¥&^ÜPM¢Â%Q	ÇÏ¸¸i>Ç9]=?çiÉ!¢&å3¦@ ?¨½­	Çî´£'ìwZuaadòm¤Ò*U4Ô8ªþ²^4úGÖ¤/Á¸}T(úxÄêÞg¿{¡çµáùÊDBa0¯ :	HGvPWæo¯9â:ûã$Í}A´t¼bW |
| --- | Minor | ^s¹Ìì%ªÀ	¿{©a¡+PÞÔTU}üôÑd7QïÖñGEõ 7êöhå1 ¡ \yuµ |
| --- | Minor | ~A:ìSD<[HäÒ¨Z281H[çyÿëæÙìµ7Ì¥Ó·ÿT¯#.Leº"5SüÜe\y"¨Ã? |
| --- | Minor | ]oêIÇôëÉøu¤wÚi!¼¸t(§Áj´¬¯¡:>êçFáÅ¢ÙBYr~=PÿÙ¤Q½í?F1ùö54Ãt0ßðìÍFÇY Ê\PáPtæmfÒâ¤ïCPKWI­FW­µiÉ¨Ò)u <vè ?ëÉU;Hst2é	ýê¬mil:óÅ»%«ÖÞû{úÏðÕO	ö¤.cefðô&M0 |
| --- | Minor | %.;@óï\í47ì§Ê)³Ö¦dgj³âcâC¦*$E. ZÞ¯s¨âTJ=4æ¿ÞaX |
| --- | Minor | Â¨úgÅ¿õ?Â0éÝ`ú9m"h³úM¥%§<§=§ÐLDñýna0±ÃRêåRéÝÚÖÕmêòñLµx!§­Tè·ûG0øöé»ä{¨*ÇpÌ§1zä |
| --- | Minor | ±^å?Ç¼¢­ÒlÃð£ÿ®á¬|Yt~òbR:õb¹Uk§ZMÍ-mÍß[ ¤·¤>¨Ábr¡Gn¾{óo. £Ä@. sÕe±13ï!oãÇ^&ìÐ¼fª?Üsx¸Îÿ óÝ¬:r·(k·xÎ®òÀ»&Êâ6Te7 MJL \R¹ä;Ý§wåA¢ÕêµxôÐf>Î`*åzø:+IË+¸` FSIõy¤÷þÄ9§Ü ¥7~¢Gã35|³ t2ÝäÛòM:¾HA |
| --- | Minor | jÊ®üm |
| --- | Minor | ù}Î`³~3±ðLD×áÅhôèq²HQ­àÍXùß4#%è	Òø¯~õÉ©ßõ¶â4Dñ¼xâ |
| --- | Minor | 6=CààC¤ÄtÔ¢W3>ä sè*-å¢©þ ¾¾æM<Æ×ÿmDÿOäIo4éý®}Ä½qZHÜßÄÄïÚ¿Qqé)ÜÐÁ üø­4ÑÏ4 ¼<¸?byûÑ×ásêæüËx w|Ï¹_]°_7Õ×¿Q2õgJìTÎG¸·Ë·&«)*2]¹f¡ðü±õó7ñ0ØÓ:eæòù" þNÒÆ¬/%Æ (ë«B2~.ÍN °_»ÎL¯Ãå?I¯ÄÄ¸_J¯ùx'ã±ÿ5¨UÛÜ ÏÂlm6µ»yj1è ól;T@8²«è. AôdXu4p¾·½¨ß. RÑ¤{©ôjbç 2<·Üê^è¦þ3÷ò Hs)**(ÔåÊ*V4ÔUwØÛ¾?ÃKÞùýK¾B½÷µÛª²0N¥X2³º§^¸@ÃaßÇ-}g{ÎBtÉU±ä*¡=ëg@ÞfÚ x |
| --- | Minor | ¦ñdåëóPB=ü"Ög=#¦_òÉ/]ñü½&Ü@éEÊêçu¢Ù_Öu¬.-ñ1ü_pPBåwÿñ¦êg_à0ÉÌ=<"-`ÁKB¥&^ÜPM¢Â%Q	ÇÏ¸¸i>Ç9]=?çiÉ!¢&å3¦@ ?¨½­	Çî´£'ìwZuaadòm¤Ò*U4Ô8ªþ²^4úGÖ¤/Á¸}T(úxÄêÞg¿{¡çµáùÊDBa0¯ :	HGvPWæo¯9â:ûã$Í}A´t¼bW |
| --- | Minor | ^s¹Ìì%ªÀ	¿{©a¡+PÞÔTU}üôÑd7QïÖñGEõ 7êöhå1 ¡ \yuµ |
| --- | Minor | ~A:ìSD<[HäÒ¨Z281H[çyÿëæÙìµ7Ì¥Ó·ÿT¯#.Leº"5SüÜe\y"¨Ã?. |
| --- | Minor | Sentence exceeds complexity threshold, split for readability. Applying the split needs --strength moderate or higher. |
| --- | Minor | none (split proposal only; source not rewritten) |
| --- | Minor | none |
| --- | Minor | Check: NEEDS-LLM |
| --- | Minor | Flags:    not-assessed |
| --- | Minor | SENTENCE (Line 1103, 674 words, 5 clauses)  [Script] |
| --- | Minor | Ý@Óïl¹²Þ{âbdgVÆýºÇ"­TO]òluuõå¥­¨®êM4lJÂcÅ±+÷ DþÐ·¸¸]O åöØ3_ô³C"ÑôZµôàcY@åÈ<Í4Tmf/ñûêÝ¼d]v^ðå9ëPkFÏ/ª¢­y«¢¾;ã}´÷Â!Ôk¢%²x¬·sõ¿¯½ênü¾©ütï]ó§ö ezÒT²¤iªÂ¸9ëa75ûjæÁhëõúÝywíf_v^@îpâÉ(gf |
| --- | Minor | ·-*´2×ñTÔ,ÆãvZO	à\ÝµÀ |
| --- | Minor | ÷[ZÃç=U |
| --- | Minor | ´LP)>©â}p¨Þ[GÑ>ôÞ)Aèàï®ÿãÂÑ&bÀ!ôgÅïlÿ	Ê\­r/ÞªÌP¦êÄ &Î E¦¦Ä õ,¼Iò¤ÉÒyMt5ZKÏÚwÿËs;­ßá)MWæÀã%û ÷jÂ[/®×k×]U5Â[päÚ-ï4¡Ép:+,ýebÚÌ		¤Nî6öÑPoK¢ÅDpußêþ|æ>¹ÛK »£#3cÓö»ßßY(q;N[@h vï:wIð%|y»§¯ÚýÈí·¿J2øïLCM[ N·µýåCÿñàs2ªd¢PËS÷ädAHJ½yUù¾$ ß77GmR9h-FkÅÑ~ªÊ*EW¡ÔøÏDäÌ¿juÂ¢«½²ÑhuUµ6Ö5A8å5iÞòB¡OûÑuEA/=¢µëò ÄÖ[¢§ÐC¤KÈµTh¶p¹<(ÕÏÅQ®±ñ£ñ³7LPc |
| --- | Minor | ü#þ< endstream endobj 687 0 obj <</Filter/FlateDecode/Length 237>> stream xÚ]PÁ ½ósì¦Ù6Ù½ÆÆÄu£í dxðïWÐô°`fxïå½IêViå!ùqFtèaPZ:ÍâB£Ò EÍíOÉ½©¯ms.êöûóù(Ó/8ìÇj²£¯nÝ:{*=` $í¦7{·Âé*MaÖ8NéNÏ¢n±ö'Ô(Éó(î8[.Ðq="aæÀÊ2'¨å¿¿lgôxqGØ%ÝnÏVg{EÞ !é;¨XÛ<ÄuÄtÁÒøÞ56°âù±o endstream endobj 689 0 obj <</Subtype/Type1C/Filter/FlateDecode/Length 462>> stream xÚcd`aa`ddäñó÷uò×vö |
| --- | Minor | ñM~÷ýúö³õ4ÃÆ²L?ä³È200<ùAä]© k*ZZë(X*8æ¦e&'æ)ø&d¤æ& 99 ÁùÉ©% 6%%Vúúåååz¹ÅzùEév: å% A©Å©Ee©) nùy% ~¹© 'ëçüÜÒÔ"ßüÔ¢<  |
| --- | Minor | Y|wÿèàûq¶{ý%ë·Ïgü>éó÷Ç?DuöäËyût%us¤³/î>Û}h9ÇIìYÝuêr©éls{¾ó÷mXõ]¨c!ÊúTvõîkäA=øþæëõ§¾~o~Ãü£÷»h&[Gic@]cs«]wm7Ço¶//Ö-?¾ëê±'»_q|çU¼ú[ä·¹~Ä¶¶©WÌY?·e]¸ÜªKçîêæx¿ßÖJ¾ÛÄ×-;ýwëï&Æ¦îÎî|l|åó8Ïú7uÊ|¶ßÓØ×sÝâ^>çÖl^9.óù<?DD ÚÃ¯p endstream endobj 690 0 obj <</Filter/FlateDecode/Length 370>> stream xÚ]Mk@ïþ=¶â÷F6M	ôjtLºÊjù÷Ù±9ô óìøÎ×:vVäêfaôP0¶Si¸éÄ®²\O4]=/'ó®ûj´ìlWUÂ~?|}ìw/Ùîè:¯çÓÖ¢§ûÂ[ÎE^Þ§úBµcKû	§YßÅSÚx&ß^7 ;uOç¬4ò6?Ðc%IçrKõÐÀ4V5èJ]Á'ñvX ßÜC.mý]i®Pêø©L¬ØÄN±F¼b^¯×Äæ |
| --- | Minor | FcÅAd |
| --- | Minor | Ò®a4ÈìcC |
| --- | Minor | ½úGRÉu%Õ¸úXgfØe*ù7ãr>ÝruE<b`ÚñC®õH!Y!I!3äÈaGF=r°ËsAºvÚÇzÔ7­ñÇ%2+A¯SðØ³q)Ê<¿¥°À endstream endobj 692 0 obj <</Subtype/Type1C/Filter/FlateDecode/Length 5750>> stream xÚ­XyXS×¶?1sP§ÖàÐ:8!¶VÁyÄygC %ÌIVfdNA0 UPÑj«ÞÒÖZm«­>§k­¶V»nî}oôö¾wï÷þyïûòïË9ûìµÖo¯õ[¿u%F®ß¼{ËÆéË7nµc¾±Àk_eö¥Yòã(þ=Ï |
| --- | Minor | %Bþm÷(J?Æ|=\©{£Í×÷ÉåkÊR °¬Þ4gÎ¼YsæÌ]/ ¶â3ÕÎÞÑÑaÝÜ9sí¤~² ¯0»^Ñ~R¯hò'Ôn[¸O_t¼Ý££#Ï;ËK5+\ðñÔv±AÑv[ý¢üdûý|íVEÛmòúÙ |
| --- | Minor | =kàº<\í'³Ûîë'#²õõ>5E03l	åd±ZOm¡¶Y¸Rû^Tj!ÆQÈâlJN¨¡Ô0j5²¦ÄÔX%ï¿MÙP¶Ô;Ô»GM &RÈPS¨Ô\j>µZH9P¨¨É.ÎÔrjµZE­¡ÖQ©MµÙlÚNí vR{¨jÁJ@YPê ]ðãd	-ëç,|->±	Dþ¢?h |
| --- | Minor | ¡ÙC |
| --- | Minor | n1Ü4"däÔ¥V£¬RFÙr%3zÎèOÆLÓj=Nl%öWÝ=öëÌö¾õñ[/Þ^üvÍz^aÕç¦ß«yêç&AÏ34ÿ6ZüLÈODï²höA$|¿ÂïXô Ï8ÈôÐG ô1×h(f·÷,1)´~%Ûh<3Én6LIH8MMb¶ÑA<5kB{û#h1ÉLÏ&É¢ïX<¡*þ7øº¦cn«YÄ%ÖÍ¥àd§Ç3V¼ï1	zÑß¼3ßÃðßBi«¾o¶6i |
| --- | Minor | ÏÐV#Zl¾ ûúÜØ¼Bòâ´B9 Y{V¯p°Ñ¸½;®bY0KW8à¡xä×¯_;YH :÷w_ñ?ÕßB)/G­²éßñ7û´J[yQZWbÆÈÏbc× ÅèÃ+%ú3]N0µkù. |
| --- | Minor | Ý@Óïl¹²Þ{âbdgVÆýºÇ"­TO]òluuõå¥­¨®êM4lJÂcÅ±+÷ DþÐ·¸¸]O åöØ3_ô³C"ÑôZµôàcY@åÈ<Í4Tmf/ñûêÝ¼d]v^ðå9ëPkFÏ/ª¢­y«¢¾;ã}´÷Â!Ôk¢%²x¬·sõ¿¯½ênü¾©ütï]ó§ö ezÒT²¤iªÂ¸9ëa75ûjæÁhëõúÝywíf_v^@îpâÉ(gf |
| --- | Minor | ·-*´2×ñTÔ. ÆãvZO	à\ÝµÀ |
| --- | Minor | ÷[ZÃç=U |
| --- | Minor | ´LP)>©â}p¨Þ[GÑ>ôÞ)Aèàï®ÿãÂÑ&bÀ!ôgÅïlÿ	Ê\­r/ÞªÌP¦êÄ &Î E¦¦Ä õ. ¼Iò¤ÉÒyMt5ZKÏÚwÿËs;­ßá)MWæÀã%û ÷jÂ[/®×k×]U5Â[päÚ-ï4¡Ép:+. ýebÚÌ		¤Nî6öÑPoK¢ÅDpußêþ|æ>¹ÛK »£#3cÓö»ßßY(q;N[@h vï:wIð%|y»§¯ÚýÈí·¿J2øïLCM[ N·µýåCÿñàs2ªd¢PËS÷ädAHJ½yUù¾$ ß77GmR9h-FkÅÑ~ªÊ*EW¡ÔøÏDäÌ¿juÂ¢«½²ÑhuUµ6Ö5A8å5iÞòB¡OûÑuEA/=¢µëò ÄÖ[¢§ÐC¤KÈµTh¶p¹<(ÕÏÅQ®±ñ£ñ³7LPc |
| --- | Minor | ü#þ< endstream endobj 687 0 obj <</Filter/FlateDecode/Length 237>> stream xÚ]PÁ ½ósì¦Ù6Ù½ÆÆÄu£í dxðïWÐô°`fxïå½IêViå!ùqFtèaPZ:ÍâB£Ò EÍíOÉ½©¯ms.êöûóù(Ó/8ìÇj²£¯nÝ:{*=` $í¦7{·Âé*MaÖ8NéNÏ¢n±ö'Ô(Éó(î8[.Ðq="aæÀÊ2'¨å¿¿lgôxqGØ%ÝnÏVg{EÞ !é;¨XÛ<ÄuÄtÁÒøÞ56°âù±o endstream endobj 689 0 obj <</Subtype/Type1C/Filter/FlateDecode/Length 462>> stream xÚcd`aa`ddäñó÷uò×vö |
| --- | Minor | ñM~÷ýúö³õ4ÃÆ²L?ä³È200<ùAä]© k*ZZë(X*8æ¦e&'æ)ø&d¤æ& 99 ÁùÉ©% 6%%Vúúåååz¹ÅzùEév: å% A©Å©Ee©) nùy% ~¹© 'ëçüÜÒÔ"ßüÔ¢<  |
| --- | Minor | Y|wÿèàûq¶{ý%ë·Ïgü>éó÷Ç?DuöäËyût%us¤³/î>Û}h9ÇIìYÝuêr©éls{¾ó÷mXõ]¨c!ÊúTvõîkäA=øþæëõ§¾~o~Ãü£÷»h&[Gic@]cs«]wm7Ço¶//Ö-?¾ëê±'»_q|çU¼ú[ä·¹~Ä¶¶©WÌY?·e]¸ÜªKçîêæx¿ßÖJ¾ÛÄ×-;ýwëï&Æ¦îÎî|l|åó8Ïú7uÊ|¶ßÓØ×sÝâ^>çÖl^9.óù<?DD ÚÃ¯p endstream endobj 690 0 obj <</Filter/FlateDecode/Length 370>> stream xÚ]Mk@ïþ=¶â÷F6M	ôjtLºÊjù÷Ù±9ô óìøÎ×:vVäêfaôP0¶Si¸éÄ®²\O4]=/'ó®ûj´ìlWUÂ~?|}ìw/Ùîè:¯çÓÖ¢§ûÂ[ÎE^Þ§úBµcKû	§YßÅSÚx&ß^7 ;uOç¬4ò6?Ðc%IçrKõÐÀ4V5èJ]Á'ñvX ßÜC.mý]i®Pêø©L¬ØÄN±F¼b^¯×Äæ |
| --- | Minor | FcÅAd |
| --- | Minor | Ò®a4ÈìcC |
| --- | Minor | ½úGRÉu%Õ¸úXgfØe*ù7ãr>ÝruE<b`ÚñC®õH!Y!I!3äÈaGF=r°ËsAºvÚÇzÔ7­ñÇ%2+A¯SðØ³q)Ê<¿¥°À endstream endobj 692 0 obj <</Subtype/Type1C/Filter/FlateDecode/Length 5750>> stream xÚ­XyXS×¶?1sP§ÖàÐ:8!¶VÁyÄygC %ÌIVfdNA0 UPÑj«ÞÒÖZm«­>§k­¶V»nî}oôö¾wï÷þyïûòïË9ûìµÖo¯õ[¿u%F®ß¼{ËÆéË7nµc¾±Àk_eö¥Yòã(þ=Ï |
| --- | Minor | %Bþm÷(J?Æ|=\©{£Í×÷ÉåkÊR °¬Þ4gÎ¼YsæÌ]/ ¶â3ÕÎÞÑÑaÝÜ9sí¤~² ¯0»^Ñ~R¯hò'Ôn[¸O_t¼Ý££#Ï;ËK5+\ðñÔv±AÑv[ý¢üdûý|íVEÛmòúÙ |
| --- | Minor | =kàº<\í'³Ûîë'#²õõ>5E03l	åd±ZOm¡¶Y¸Rû^Tj!ÆQÈâlJN¨¡Ô0j5²¦ÄÔX%ï¿MÙP¶Ô;Ô»GM &RÈPS¨Ô\j>µZH9P¨¨É.ÎÔrjµZE­¡ÖQ©MµÙlÚNí vR{¨jÁJ@YPê ]ðãd	-ëç. |->±	Dþ¢?h |
| --- | Minor | ¡ÙC |
| --- | Minor | n1Ü4"däÔ¥V£¬RFÙr%3zÎèOÆLÓj=Nl%öWÝ=öëÌö¾õñ[/Þ^üvÍz^aÕç¦ß«yêç&AÏ34ÿ6ZüLÈODï²höA$|¿ÂïXô Ï8ÈôÐG ô1×h(f·÷. 1)´~%Ûh<3Én6LIH8MMb¶ÑA<5kB{û#h1ÉLÏ&É¢ïX<¡*þ7øº¦cn«YÄ%ÖÍ¥àd§Ç3V¼ï1	zÑß¼3ßÃðßBi«¾o¶6i |
| --- | Minor | ÏÐV#Zl¾ ûúÜØ¼Bòâ´B9 Y{V¯p°Ñ¸½;®bY0KW8à¡xä×¯_;YH :÷w_ñ?ÕßB)/G­²éßñ7û´J[yQZWbÆÈÏbc× ÅèÃ+%ú3]N0µkù.. |
| --- | Minor | Sentence exceeds complexity threshold, split for readability. Applying the split needs --strength moderate or higher. |
| --- | Minor | none (split proposal only; source not rewritten) |
| --- | Minor | none |
| --- | Minor | Check: NEEDS-LLM |
| --- | Minor | Flags:    not-assessed |
| --- | Minor | SENTENCE (Line 1103, 378 words, 9 clauses)  [Script] |
| --- | Minor | ïÒ?ùß>@,ZÍ"zóÝÿÃ,gÅÛ`­þÕ6àé!úg° MB¬CÐ@39·"g4 )9Ð2ùÙÚLýêÍX¼IÁBp%Åxä9lyº³®¼m¾äÏ½Q"Ù¼iY¸)G#·#K4jÁT`2³³3%  eUü/SÎãyý /õÇ+ðhl}  `2s²óHä÷¿ø»Ðð#cÕW¹HN´¡:oÙ&äg¢5J«@§d	n@¢R¨¸d7âF:9bc« TÈ?Q2ÄétPUJ PÄúl£·QÁm!ï®±ð}Ö÷ßìûÙ±Ü\À9Ò{VÈª¬%ð!,Ë±o_zlñµØSp¾ÕÌ4ôæÞï¯±¾°Ùÿ³ü"<Oá2\-8[_/4B#\¯R´¤ÖX«åë¤[¥î`N10ñ-¦ã¥o¨³o,[hnãúy@ò 7ÓSðÅþ PM,Vj98òÚ`@oß¶>ýÔÕâîÿàw },îøS+x&2h­ËlÌh úòAI"7C¢"¨f)bÓöÆ®Øï¦O×*É=&Ò%øé¥\>h´9yÅå-gn0î+/÷×øÂFü Á%Ê+Ê×?r8ÃÖ3	jUZU10Æcpr`Æ¾½Ó³ÿ@Ìo?#±dÀg~Bõímä î#ßëîû |
| --- | Minor | ­¡QÝÜÅÕ@G¦!Iò÷Ð$CùáÂ£=>YÇâw1#%âWXðñ_Éâ¹?c!'î_ |
| --- | Minor | »c]4_g7ôbfY|'|ÌÍg÷¹r8	¦þ°ö+ìIºìËL=å Çøø¡à_²fÑ38[­@Y]ÅÈDÁØÛÒ(Ò~^r0?ï&(}DòÄ° &Ø¿%ð>ÎýäI8QÄuÑpN{®àlNuéã |
| --- | Minor | (úËyTA¢>}Õ>-~ø}ì¾ÃÙG ¹t¥ã«kw-ç`«¯«K cHb¿n9Õ |
| --- | Minor | sÏÏ¼Øiñ÷·â1?ß¶`LaÆÿ¶æ²||ûå'ü:âôEëÛÉ^,µ¤.®S lír\°ü³Û\h¸üSç ?Í¬æ'aÝCä{ JÓ|×õþÐ¸BÈ) ¦¿Ëm½ñîÞîÑ^°Ácþc*¡tñ ½£úGÌ&Â>ý<¾N±:õ-N·4iªp?³ö1¦Íã¬ÐaxÂ_ î¼¢í¼[UVU__SSÏáÿrð0²mC³Ú=}3}ËÑ÷lÙ îÿYôrË ä'ôm`³JùÌ¬dìÓÿØ&~·OÒaÃjõ1M³©[Ù@ Þ#3ÖJ@«.RkN¢·mÎàêlM&dÛJ·AJ7k¿Öc'Ud}<íÉùòFø"Yâ8FdÕ·8pÕ¬ä6ºðÄù!O?E*ºQßÉ¡Ñ¢'Mw®ßëiìªÞËð |
| --- | Minor | ü×?$´FtC#ô×ÐâY>æ¢Bùq"d{ÿÞ_%p×ñ:d6b¢8ÆÜùT6ÓO;f­Y±ËqAÀ?ÆÔ7ÓdÝói"Ìý¨=f±ZíÑ&äð ¦òprLUj:hçÀlÂ» .øWÔv¹Ä!Ü£ÃhAQ L9hõJW@¾ËlÂd{lüwøvÁð<ìIìç©O` î/~&lê[ÊÖÐoBzÐúqh Ú¶âw=^*ÁcÿfÇDÄ·"õLôôÆt­8¶¹p,,s	Ø±uË¤Úû>"@_4¡Æ#4îÚkDÓZ£»É¾1ò¨.#Ã³¢ñ2`°íkÈt÷é'Å! |
| --- | Minor | ïÒ?ùß>@. ZÍ"zóÝÿÃ. gÅÛ`­þÕ6àé!úg° MB¬CÐ@39·"g4 )9Ð2ùÙÚLýêÍX¼IÁBp%Åxä9lyº³®¼m¾äÏ½Q"Ù¼iY¸)G#·#K4jÁT`2³³3%  eUü/SÎãyý /õÇ+ðhl}  `2s²óHä÷¿ø»Ðð#cÕW¹HN´¡:oÙ&äg¢5J«@§d	n@¢R¨¸d7âF:9bc« TÈ?Q2ÄétPUJ PÄúl£·QÁm!ï®±ð}Ö÷ßìûÙ±Ü\À9Ò{VÈª¬%ð!. Ë±o_zlñµØSp¾ÕÌ4ôæÞï¯±¾°Ùÿ³ü"<Oá2\-8[_/4B#\¯R´¤ÖX«åë¤[¥î`N10ñ-¦ã¥o¨³o. [hnãúy@ò 7ÓSðÅþ PM. Vj98òÚ`@oß¶>ýÔÕâîÿàw }. îøS+x&2h­ËlÌh úòAI"7C¢"¨f)bÓöÆ®Øï¦O×*É=&Ò%øé¥\>h´9yÅå-gn0î+/÷×øÂFü Á%Ê+Ê×?r8ÃÖ3	jUZU10Æcpr`Æ¾½Ó³ÿ@Ìo?#±dÀg~Bõímä î#ßëîû |
| --- | Minor | ­¡QÝÜÅÕ@G¦!Iò÷Ð$CùáÂ£=>YÇâw1#%âWXðñ_Éâ¹?c!'î_ |
| --- | Minor | »c]4_g7ôbfY|'|ÌÍg÷¹r8	¦þ°ö+ìIºìËL=å Çøø¡à_²fÑ38[­@Y]ÅÈDÁØÛÒ(Ò~^r0?ï&(}DòÄ° &Ø¿%ð>ÎýäI8QÄuÑpN{®àlNuéã |
| --- | Minor | (úËyTA¢>}Õ>-~ø}ì¾ÃÙG ¹t¥ã«kw-ç`«¯«K cHb¿n9Õ |
| --- | Minor | sÏÏ¼Øiñ÷·â1?ß¶`LaÆÿ¶æ²||ûå'ü:âôEëÛÉ^. µ¤.®S lír\°ü³Û\h¸üSç ?Í¬æ'aÝCä{ JÓ|×õþÐ¸BÈ) ¦¿Ëm½ñîÞîÑ^°Ácþc*¡tñ ½£úGÌ&Â>ý<¾N±:õ-N·4iªp?³ö1¦Íã¬ÐaxÂ_ î¼¢í¼[UVU__SSÏáÿrð0²mC³Ú=}3}ËÑ÷lÙ îÿYôrË ä'ôm`³JùÌ¬dìÓÿØ&~·OÒaÃjõ1M³©[Ù@ Þ#3ÖJ@«.RkN¢·mÎàêlM&dÛJ·AJ7k¿Öc'Ud}<íÉùòFø"Yâ8FdÕ·8pÕ¬ä6ºðÄù!O?E*ºQßÉ¡Ñ¢'Mw®ßëiìªÞËð |
| --- | Minor | ü×?$´FtC#ô×ÐâY>æ¢Bùq"d{ÿÞ_%p×ñ:d6b¢8ÆÜùT6ÓO;f­Y±ËqAÀ?ÆÔ7ÓdÝói"Ìý¨=f±ZíÑ&äð ¦òprLUj:hçÀlÂ» .øWÔv¹Ä!Ü£ÃhAQ L9hõJW@¾ËlÂd{lüwøvÁð<ìIìç©O` î/~&lê[ÊÖÐoBzÐúqh Ú¶âw=^*ÁcÿfÇDÄ·"õLôôÆt­8¶¹p. . s	Ø±uË¤Úû>"@_4¡Æ#4îÚkDÓZ£»É¾1ò¨.#Ã³¢ñ2`°íkÈt÷é'Å!. |
| --- | Minor | Sentence exceeds complexity threshold, split for readability. Applying the split needs --strength moderate or higher. |
| --- | Minor | none (split proposal only; source not rewritten) |
| --- | Minor | none |
| --- | Minor | Check: NEEDS-LLM |
| --- | Minor | Flags:    not-assessed |
| --- | Minor | SENTENCE (Line 1103, 733 words, 7 clauses)  [Script] |
| --- | Minor | %FT)-NãìQhðxXÑ)¶c	c£ËþoÎÄªÏcJÓ! á÷ÄIüýÏÙ6ÂPP&AÎôÑÜ+öWmWJ}HËú¾Vî/YO;±§¯Ã{P{OãEîx`¯ÃÿW´CvB¢Øâ¹Ø{¡ùxÚ*']ïk|j2¯ÁwOÈOâX´9éúAmk¢#!°7t*/Ò 155=_ÅÝ6è+ºYS|«1Nàç·ÉÂ9;¢¾ÖÖë!þØÜæÐrôí!h-Öç¥[©/Äi2WLSë@ÅÐ;`ô¸ÙK¼óy¯2ðõFk¢ÓgÐäöçÏd&ñRèz9»C-®J`P	²ûáá4n.à`I ?~ILOÈéÍÀìõô@DIZÉ ÙElP\H6»ÓOÕëJÎÁ«xÓÇ¢ag~BcMg'N a^gâùØ»£éÁu	òêñßåe3Jg?æ·*dÛUÅrI¹ÃKê	n ;un7©±9uÖ=µÑwÖ¯¡ßx5m,ó=l¿<{é&>^ç®ÎL%[%Aû5TªÀ­6Òzïö¹äPóÆK`ÑçÅÙ])_ÆðèPÆá:}dQ03+ö,wàÂ`iîÎS[Î*.«UEéDQ0 #^ÝèÈ(&]^­É/µVÛxÆt9àénC¿ÿ |
| --- | Minor | ¯Á³µ·tÌÀÄ;êS Ù î¡2kÌêsdû(ÇîX5¢éP	µP¤Ôg¢dÀùÎopòäó¡ãCOÒ#¾VækAÊKñRB	Zo$%ê3	ùïP"¦}8Ã |
| --- | Minor | 3¢­?æM¼4L^ç |
| --- | Minor | ÷U VÐÆ kt#xNê,@åª tÕë~næN£ïoTõ¹ ûü-¶´åPýjÆD*}TÒ-Hóân>¢!]©ÌÄëû÷Ûàm¼&³èmýy07W¬?WÏÁÍ¯àJýPRÿ+ü¸\E	T&7·±zupÐ^å«(á«ñÄ^åùcEGØ*CUÒ°õöþ¢ÒCd*Ò½iýÞ6x>@£Ì\ÛÃ vÀÞj§ÆÛ¼þ<èá`a¥ |
| --- | Minor | ô;á¼(³|ÐþÛµ×!'ë ?rëï³Ñ¦iSKÈ¨ÉÏ)A|® |
| --- | Minor | 7xÓvð.Cz4Ö¶½Ñ&@ÃÚ¨ kÙ¶i¯f<iÃïý=þ§§ÃÉÓy}i,~ÏçÉßgLóAïÌ³lþn©ziûÖ±ø<®2¨CD¿_YiÖ´rC	jïÛ?<i°î¸áú9ô^3¥gÐoÙC^Àè/þ ém£·È2åÁÙ'r9äFC |
| --- | Minor | =º§ÜÇUnk¥ºÚºJéÏ³÷©5*&øÔyß¹Z|ìÌnÅJÅé² Ù.ð`?}Î+Wád[U'±éËÜ÷z7æà\Çmäg.b¹A®ç'õË^T~[ñ#Yô%'É-Cé/2öJúiµº ôP'#>UÝ±çRRÃÿè'ñÔ§XDØw	xº%Æ3Z\Î"o Üâ2Ä¿ZªGÎëºÛ(íêÀirÙ<4õGã`áw}%8m¿y7hAÿtÇ<3³'á1ô;/¦!Y@Âª¢tM9èLezà KO÷!á3¾,ä@uîhx»¢ G½½7 ÅC #î£ ´ÄÏëâ	>Ìò§Û:ö{×M»v×í¬Û@¡ÉÙoû$ÜË~°ªëN¶¶×2î X°cÅ©³ 7ñhäKëë/W^?B+ùM,¶3ëÂLr¬Ú]kHnPÕÔ45){ôÚìÜ£Dæð­lLa4Õõ |
| --- | Minor | ªÈ^¢æ¢ÿ§:©x³_£úÆh<¥l1ï·F'3àMÁ |
| --- | Minor | ~æøÑOX¬óZºKs¨¶{Ð×Ðú÷¯z.^¼c+ÿOëvìT´;` mN®ÖmðpIðK¾ëTìN_7Ïðø¤ß£Í÷]|âÿÃñïÐ'nüÃ¯PÈüÊáÛB>³hìäx â'KÀË#6ðd¢èú®Sõ]À\»4[â+ vúä_¾ÀéáÁ |
| --- | Minor | ^äX·¯)LSmû |
| --- | Minor | \{M¨:­¸7(ÔY¤(²SÓ²~uÞD¸ÇÊoÍ6	aÄ÷"ë2¿N&^Û ¬Cá&´H'ø½½C& '~&ðD´A&R9Jí¦f31?ázzÒüUÝW¹ó²í´ÔÏ |
| --- | Minor | <¨àÞ´Ë7Ç¿ûkO£I6ÑxòMa=ßuµ³Cvg7~zýä&(æJð4z	ÌA38q\¯«73©1¤IpWQJa·¶ª©55·uY¤RJÙNÍ³Ñ+a=1õ@VæÆ%6K~M+"øäÙBYY¡n`µj­2q¿:Â¼úKP«:]bÖf&îºe³r?ØÒµº¶¾CYcÎÊmF	¡¾ñÒ×ßN¶)$B&¤¥%E?V÷hª(ñèú/õ_?r?a}ÝÿÄÏïÏ&YªüÜ<¸h%EÇç'òÙ½­<ÉFÝÚy«cREê¡ÄÊ h*CWccàW °â<{¤MÃz GèÕÉ |
| --- | Minor | îý/_aé« endstream endobj 693 0 obj <</Filter/FlateDecode/Length 356>> stream xÚ]ÒKo@ à;¿b6MÃîÊCC¢ 	mS´I%)ËfÁÿ¾ÌñÐäÛafØæYnÚQø®¯ EÓÚÁÐß]â ·ÖxJº­ÆyDïª+­ç§ÇÒÊ9oÓÓ×kz,¾|»*54r~XzçYñFèrÓôb³ñð?§Ãèb±­û+¼`ìÝÕàZsKZP¤¸[ûQH/I¨â9U} |
| --- | Minor | -+p¥¹·2Ã!ñÀÔÿ¾éK®MõSº9Uk¥Éj²»­É9â¸¬åGä Cv^édMýÕZ¢ÿ¥6Öê59ÃøRS­\¡wlì4 ó={?9äûKöÍù!æÜGoÑ6öx]ñ³3ôóçýÁÚæ)§%áÆÎ;[áyª»sÓ!Ñ¡ãÇj |
| --- | Minor | </í-VÑó0ª¨4 endstream endobj 695 0 obj <</Subtype/Type1C/Filter/FlateDecode/Length 2907>> stream xÚ­VkTSW¾0\ÅÚelhm;ÓA[E|´T«VE­ïÑêø ± @ ¹;	y?ä "88_¨­XµZ©í´µk¦uú[íÌZvuµçÆÎÑ:?ú¯+ÉÉÉÍ9{ûÛßÞçÐTBEÓtÒ6.ÊX»é5¶ÎH>'½¿ñîHÓn2ÅM¡¹çã¸â¹'_¬LøÏ¸g(¾<.:zÆFÇâÇÉHý}ò5¦Çð'MñÊõ[r r9ù[RP.ÉUHÊçò¢Ò¢ÜòÜòr²D¯Æf;dÂáÉÎ%ÃORT!)-S¨äE´H&-ååÈÊËswF'ii³RÓÒffÈÊTÃ{Äó¦gÌ>U<3-mxQ©¤¬×ä* |
| --- | Minor | %FT)-NãìQhðxXÑ)¶c	c£ËþoÎÄªÏcJÓ! á÷ÄIüýÏÙ6ÂPP&AÎôÑÜ+öWmWJ}HËú¾Vî/YO;±§¯Ã{P{OãEîx`¯ÃÿW´CvB¢Øâ¹Ø{¡ùxÚ*']ïk|j2¯ÁwOÈOâX´9éúAmk¢#!°7t*/Ò 155=_ÅÝ6è+ºYS|«1Nàç·ÉÂ9;¢¾ÖÖë!þØÜæÐrôí!h-Öç¥[©/Äi2WLSë@ÅÐ;`ô¸ÙK¼óy¯2ðõFk¢ÓgÐäöçÏd&ñRèz9»C-®J`P	²ûáá4n.à`I ?~ILOÈéÍÀìõô@DIZÉ ÙElP\H6»ÓOÕëJÎÁ«xÓÇ¢ag~BcMg'N a^gâùØ»£éÁu	òêñßåe3Jg?æ·*dÛUÅrI¹ÃKê	n ;un7©±9uÖ=µÑwÖ¯¡ßx5m. ó=l¿<{é&>^ç®ÎL%[%Aû5TªÀ­6Òzïö¹äPóÆK`ÑçÅÙ])_ÆðèPÆá:}dQ03+ö. wàÂ`iîÎS[Î*.«UEéDQ0 #^ÝèÈ(&]^­É/µVÛxÆt9àénC¿ÿ |
| --- | Minor | ¯Á³µ·tÌÀÄ;êS Ù î¡2kÌêsdû(ÇîX5¢éP	µP¤Ôg¢dÀùÎopòäó¡ãCOÒ#¾VækAÊKñRB	Zo$%ê3	ùïP"¦}8Ã |
| --- | Minor | 3¢­?æM¼4L^ç |
| --- | Minor | ÷U VÐÆ kt#xNê. @åª tÕë~næN£ïoTõ¹ ûü-¶´åPýjÆD*}TÒ-Hóân>¢!]©ÌÄëû÷Ûàm¼&³èmýy07W¬?WÏÁÍ¯àJýPRÿ+ü¸\E	T&7·±zupÐ^å«(á«ñÄ^åùcEGØ*CUÒ°õöþ¢ÒCd*Ò½iýÞ6x>@£Ì\ÛÃ vÀÞj§ÆÛ¼þ<èá`a¥ |
| --- | Minor | ô;á¼(³|ÐþÛµ×!'ë ?rëï³Ñ¦iSKÈ¨ÉÏ)A|® |
| --- | Minor | 7xÓvð.Cz4Ö¶½Ñ&@ÃÚ¨ kÙ¶i¯f<iÃïý=þ§§ÃÉÓy}i. ~ÏçÉßgLóAïÌ³lþn©ziûÖ±ø<®2¨CD¿_YiÖ´rC	jïÛ?<i°î¸áú9ô^3¥gÐoÙC^Àè/þ ém£·È2åÁÙ'r9äFC |
| --- | Minor | =º§ÜÇUnk¥ºÚºJéÏ³÷©5*&øÔyß¹Z|ìÌnÅJÅé² Ù.ð`?}Î+Wád[U'±éËÜ÷z7æà\Çmäg.b¹A®ç'õË^T~[ñ#Yô%'É-Cé/2öJúiµº ôP'#>UÝ±çRRÃÿè'ñÔ§XDØw	xº%Æ3Z\Î"o Üâ2Ä¿ZªGÎëºÛ(íêÀirÙ<4õGã`áw}%8m¿y7hAÿtÇ<3³'á1ô;/¦!Y@Âª¢tM9èLezà KO÷!á3¾. ä@uîhx»¢ G½½7 ÅC #î£ ´ÄÏëâ	>Ìò§Û:ö{×M»v×í¬Û@¡ÉÙoû$ÜË~°ªëN¶¶×2î X°cÅ©³ 7ñhäKëë/W^?B+ùM. ¶3ëÂLr¬Ú]kHnPÕÔ45){ôÚìÜ£Dæð­lLa4Õõ |
| --- | Minor | ªÈ^¢æ¢ÿ§:©x³_£úÆh<¥l1ï·F'3àMÁ |
| --- | Minor | ~æøÑOX¬óZºKs¨¶{Ð×Ðú÷¯z.^¼c+ÿOëvìT´;` mN®ÖmðpIðK¾ëTìN_7Ïðø¤ß£Í÷]|âÿÃñïÐ'nüÃ¯PÈüÊáÛB>³hìäx â'KÀË#6ðd¢èú®Sõ]À\»4[â+ vúä_¾ÀéáÁ |
| --- | Minor | ^äX·¯)LSmû |
| --- | Minor | \{M¨:­¸7(ÔY¤(²SÓ²~uÞD¸ÇÊoÍ6	aÄ÷"ë2¿N&^Û ¬Cá&´H'ø½½C& '~&ðD´A&R9Jí¦f31?ázzÒüUÝW¹ó²í´ÔÏ |
| --- | Minor | <¨àÞ´Ë7Ç¿ûkO£I6ÑxòMa=ßuµ³Cvg7~zýä&(æJð4z	ÌA38q\¯«73©1¤IpWQJa·¶ª©55·uY¤RJÙNÍ³Ñ+a=1õ@VæÆ%6K~M+"øäÙBYY¡n`µj­2q¿:Â¼úKP«:]bÖf&îºe³r?ØÒµº¶¾CYcÎÊmF	¡¾ñÒ×ßN¶)$B&¤¥%E?V÷hª(ñèú/õ_?r?a}ÝÿÄÏïÏ&YªüÜ<¸h%EÇç'òÙ½­<ÉFÝÚy«cREê¡ÄÊ h*CWccàW °â<{¤MÃz GèÕÉ |
| --- | Minor | îý/_aé« endstream endobj 693 0 obj <</Filter/FlateDecode/Length 356>> stream xÚ]ÒKo@ à;¿b6MÃîÊCC¢ 	mS´I%)ËfÁÿ¾ÌñÐäÛafØæYnÚQø®¯ EÓÚÁÐß]â ·ÖxJº­ÆyDïª+­ç§ÇÒÊ9oÓÓ×kz. ¾|»*54r~XzçYñFèrÓôb³ñð?§Ãèb±­û+¼`ìÝÕàZsKZP¤¸[ûQH/I¨â9U} |
| --- | Minor | -+p¥¹·2Ã!ñÀÔÿ¾éK®MõSº9Uk¥Éj²»­É9â¸¬åGä Cv^édMýÕZ¢ÿ¥6Öê59ÃøRS­\¡wlì4 ó={?9äûKöÍù!æÜGoÑ6öx]ñ³3ôóçýÁÚæ)§%áÆÎ;[áyª»sÓ!Ñ¡ãÇj |
| --- | Minor | </í-VÑó0ª¨4 endstream endobj 695 0 obj <</Subtype/Type1C/Filter/FlateDecode/Length 2907>> stream xÚ­VkTSW¾0\ÅÚelhm;ÓA[E|´T«VE­ïÑêø ± @ ¹;	y?ä "88_¨­XµZ©í´µk¦uú[íÌZvuµçÆÎÑ:?ú¯+ÉÉÉÍ9{ûÛßÞçÐTBEÓtÒ6.ÊX»é5¶ÎH>'½¿ñîHÓn2ÅM¡¹çã¸â¹'_¬LøÏ¸g(¾<.:zÆFÇâÇÉHý}ò5¦Çð'MñÊõ[r r9ù[RP.ÉUHÊçò¢Ò¢ÜòÜòr²D¯Æf;dÂáÉÎ%ÃORT!)-S¨äE´H&-ååÈÊËswF'ii³RÓÒffÈÊTÃ{Äó¦gÌ>U<3-mxQ©¤¬×ä*. |
| --- | Minor | Sentence exceeds complexity threshold, split for readability. Applying the split needs --strength moderate or higher. |
| --- | Minor | none (split proposal only; source not rewritten) |
| --- | Minor | none |
| --- | Minor | Check: NEEDS-LLM |
| --- | Minor | Flags:    not-assessed |
| --- | Minor | SENTENCE (Line 1413, 196 words, 1 clauses)  [Script] |
| --- | Minor | ªæ7·@0¨jÑÐa^µ Êh%¡hëô?Æ£ÈÆï·K¥r¹TÚ.ïêjoï#î·&H£NÏ%£n>Þ²Ô>³UÉõõZôV³W¶ál&Fc6>YãÑz.°Z}>²(çYYg}.·WVh4ÙY+fl=V¡U»c¯ßî°XÁÉxunµPF£FÃFaÔ¤¹áxnºÊGÝ¼ánÔÅkR	ª!îÁ=#D=¸÷ü1wëÑ}<bûP¥Fßô@dZ|d17ßÜúª[±Ahqß	b$VEÿùW£|hmzÞ[ÐiÁÏÛ!®7ËD:wïµ»ìàØ Z£Ñ<tÕ:t uèî4öüz+Øñº£|¹j×P±Î1¤¹«ZÑÐ!^må/º{	}Â8NpÇè¨qB~Á§ÌÀ¨uÑì©] |
| --- | Minor | ® |
| --- | Minor | `(A©eu`HÖ¸µ^¡äÈïd¸^ýîPò J1¾ä·<:NÏV_X±q)¬¬ãÇ·ômî{ |
| --- | Minor | L¯ÃqiÅ~°xmA¨Å}|â\S9ý9g²Ïf¿¢/ ¸¢¤»µQñ¿;*þ®·%Æ®Jt¯wîXçQÿä5×e°0>5èÕÀ*Åu/ãÛ4OÐÞnöÈÿG`S[LÍÀ¸|à#ÂÓ^ÎTöæô0ÿs3@ÜD>&n6æíÐÕm_¦[ |
| --- | Minor | ,£öKØD-ûþ}áhD¯Ñf'8 |
| --- | Minor | füØi	gò±¶j`tjPÀì^}ly°´«ðx1Cªb:hyöñEø¼_qeòp%Dv¡¿óÙ}°¶ &s÷BæÞX^uÕ½ÅËÊÞ<ê¤ÊÐè Þÿæ»o_»4Øyvo³Ãb±Z­J¼X«É*0[XK? |
| --- | Minor | ªæ7·@0¨jÑÐa^µ Êh%¡hëô?Æ£ÈÆï·K¥r¹TÚ.ïêjoï#î·&H£NÏ%£n>Þ²Ô>³UÉõõZôV³W¶ál&Fc6>YãÑz.°Z}>²(çYYg}.·WVh4ÙY+fl=V¡U»c¯ßî°XÁÉxunµPF£FÃFaÔ¤¹áxnºÊGÝ¼ánÔÅkR	ª!îÁ=#D=¸÷ü1wëÑ}<bûP¥Fßô@dZ|d17ßÜúª[±Ahqß	b$VEÿùW£|hmzÞ[ÐiÁÏÛ!®7ËD:wïµ»ìàØ Z£Ñ<tÕ:t uèî4öüz+Øñº£|¹j×P±Î1¤¹«ZÑÐ!^må/º{	}Â8NpÇè¨qB~Á§ÌÀ¨uÑì©] |
| --- | Minor | ® |
| --- | Minor | `(A©eu`HÖ¸µ^¡äÈïd¸^ýîPò J1¾ä·<:NÏV_X±q)¬¬ãÇ·ômî{ |
| --- | Minor | L¯ÃqiÅ~°xmA¨Å}|â\S9ý9g²Ïf¿¢/ ¸¢¤»µQñ¿;*þ®·%Æ®Jt¯wîXçQÿä5×e°0>5èÕÀ*Åu/ãÛ4OÐÞnöÈÿG`S[LÍÀ¸|à#ÂÓ^ÎTöæô0ÿs3@ÜD>&n6æíÐÕm_¦[. £öKØD-ûþ}áhD¯Ñf'8 |
| --- | Minor | füØi	gò±¶j`tjPÀì^}ly°´«ðx1Cªb:hyöñEø¼_qeòp%Dv¡¿óÙ}°¶ &s÷BæÞX^uÕ½ÅËÊÞ<ê¤ÊÐè Þÿæ»o_»4Øyvo³Ãb±Z­J¼X«É*0[XK?. |
| --- | Minor | Sentence exceeds complexity threshold, split for readability. Applying the split needs --strength moderate or higher. |
| --- | Minor | none (split proposal only; source not rewritten) |
| --- | Minor | none |
| --- | Minor | Check: NEEDS-LLM |
| --- | Minor | Flags:    not-assessed |
| --- | Minor | SENTENCE (Line 1413, 1808 words, 24 clauses)  [Script] |
| --- | Minor | N¹¹á'MµìÆPDugf÷oc¾ÕMë°²RóÂ±áv4;ùýkÏBß¡ID/ióL~OÄðl<oôªÍ|äÿ48ñ;5zIâLóC½mmô_Qû`<'èùÃUY&¡RçéÕä©Å{óáuXY¿`çÜJD9_±TÑ¸´>á^°ym¾p}¡7Ü^w@×	(NÜj9Õñ¾íü>4wö |
| --- | Minor | Knów]4nÃ§p-p¥õÛ· t:*yüë30Ã"õrÕ³ ¬Ý¼Ê'¿¶c[aI æ_¤H+~eéXb¨%8XÆd3:ÉºSmÞ³(é3T} u3gy(	Ü"X7*Y |
| --- | Minor | *µNFï ?Z4(Ô=?}3Â$îûsÜ½stËç_} ¤D y"Hÿ2ïTåÅ7³!Y§>7çê{Bh±·8Hyw¸wAºëx®:BóÑ\¾î·­ |
| --- | Minor | " |
| --- | Minor | ®/Wéf¨fh?Eâ9 GJ¯j£ßäè÷¥Õ=ugLnÒO1(?útÍÅ=!©Gæúlß¡>xûªÂW¡*Á#ù·{¦õ1Æná¿àÛ~ËuTG '|°·ë°µÍÃó¶¢1ë¦ßäy#¨AOÖá¼îe"`´h×FÙØ_ìßbÓÆÐTÙ®êâPeWý~ÝEA6¬gÈ º»5:fE¶ÿÍû³É¡BKIÒG÷7¯û0"WÍ{ßññ.YßÔ &Hf¡4º©ºzòÓÄ4ØN¡^Ã¾×ëu¡­CKÎ;¹éfìp¸Ì»Î 4ñè<ÑÛ¤¾AWCXZKBÜ×h7´°TË½ÌÝ°O2tëBÀôØÛÝ]P*ÒA¹X[¨­gkÍÐléô\´ÿÙyPâ» ¸^îµeîuJ¨ÚcÕÂYé(qUSÜ ×îq)»D.hµö¸{ÝË^+KDýfÍzPCà><ß5Û²ÇbðÀnõ3ö¾ÆÖSz PôWs¾þ,ëgL¼=òjé#ÞDá¨ôàÎ1£,cFGGÆ!ÇÐãÿÛßÞ endstream endobj 697 0 obj <</Subtype/Type1C/Filter/FlateDecode/Length 1242>> stream xÚURmLSW>§NiEcÍµ½º9ak°(J`ºMØèP¢©³B/´¥µ½PúaÛÛC[Vü |
| --- | Minor | ¢cY¹Ô%fgLÔeÙ²-ÑF÷Ç ËÎ-§3òã¾÷ý~Þó¼/ jjö¼·Õ´ãÍêÚ»J9O¹ýÇÉ*¿ÊSJ+T¥bô\Z¨X ¼27'¿P	tT(#ó@@ A(Õ 4 ;à,àr§ÙÅ·µòÍB£­åî²µXsF£ËÜô1/<=·þ¾¨ªz¹îv»Ý,Øm@xaXlng«¹Ój<6ÿRçª©é2[lMæVa4®.1WU;Ï\QS1WZQQnàVÜ;ï¢©m\­Y°ò9 ZÇíp4Ùx¡+ZggåÊ§Älw8\-o8M°rÛy7ïêà-\ |
| --- | Minor | Ûj¶óÜ4Û%Ó¿jÝÙ.ð.®Öaá]mØ< /u`hVè¤CF ý0 c0À8Ô9ÎÀ n	8&d³eí2"×É«äÍò/¤°FÚÇÎQVØpK.²Ä¯Eq1*Æ~Øô÷}ÑO^Çïã|¼ @QU%ý(¤ëF;·õt/'êÍÄec¤/$ë½7Þ9Tñ!ÔÏÀè»%ÇW²?i^æÂ |
| --- | Minor | !^ïÞ|§©Ñ¯G¡h8¾øÁÊoÉê3ÆÄk¨½î[¾¿'\Ý[»vø|HD¢Ê?(Ñ@¯ |
| --- | Minor | ÀêØ°[¥Ê(Ljj2ñ¾ç@µ¸>ESØ"õÌËU4ã£\«'õMØðtò4ÒC6³teþ¢³îÈ¥a6cÐF#	o?RfbCý	ý4;-ã;/×bV#HªÃóðq\7Æb(£(zu=tbßPÁ} |
| --- | Minor |  d |
| --- | Minor | "x¿#£¸tnùºE½Ç»ªø(~ÙG«	_!»qû¡Íß¸G"êA*¯y)cñPT<o½Tÿ3a@è{"­!ùä1-¢(QXåM ¤î]]bèï?ÿÅú[¸å^r¯ExJ3zÚ}yjI JÙsZ³[üÞBúè.s¹£Jãz×´um[W°ÆMV Uv=IÑ/BñHÿáùMÚ^(qf>¸M¶©Æ5¸Gùä6ãDZõV9ÆNï±U<¦º«ñ¯´¹åÕ¥H½#X¼ÔÓîi@z88D»YDÙæÌÜBé{/F÷%ÄKþ{ß=ÖusßùJCÔø¼%"ðáH@}ÒgO¬ÙÙIo/ ¢Èô4ÒÒÕÑ«0(]ã³ |
| --- | Minor | <Fæ&ã¸²£íJÔJ7f³i;ÒrÜAM-ö¤ú°)M<Ì=4g©ÓÓ^ìaóòg/61©n ×Ò:ªjÏ¡þþä§ÒVÑQ8ÛHLuÔÈ]JÈìË{z­Ø¤ Ñs'º~¹¤ÔxFz¨#yéYéÙ©Áü|ú©u³üWðÝùÿww; endstream endobj 698 0 obj <</Filter/FlateDecode/Length 311>> stream xÚ]MkÃ0ïù:nxHfÑm,íe·ÔQºÀâ'=ôßO²K;Øzl¿ßPÖe­ÂO;©èÝY§U'<:èµÜNnWckPî[óÞaùýúVTOr¿¯_*N¡ÃÞ+WÜÎuÙ\çÇZ÷dY ~QÁy±Wx(ºé|÷a;´>ÃÃQ6î¦¹ó#ê¢ Ï]¹Ø·¤¦gÓ*´­>cEQYUåêîßõåRN½úi-I%I£Õ6ÉKÏ+âD8)ñjË%x;¦@¼ö¼f.<Ì^OxçyGúÜsSáY0o<o×Ö__p}áõõÂë)ð·IxTöänºXKås6ð |
| --- | Minor | ïÞÉp[ûª² endstream endobj 700 0 obj <</Subtype/Type1C/Filter/FlateDecode/Length 2610>> stream xÚytSuÇ_Pêú õ8y9l¡Â "èØÒAÈjËÚ%4EÒ4i¤K&ÍòòîKÒìiÚ¦éBÓBZÄ)«¨TªX±GAQÑã2³ø{øp×âÌqæüÎ¹ç¼ß;çw¿÷~?¿û`©©@ [ðôìËóòV=6º±¬sÿÅ-Ë8V±¤¦°ÓìÔTÉÇ«SLKù	½g4wñCwÆY|¤º/NX¡"¦°´P¡(¬=µp^VÖåÊjuY©\#]<GúÈ%çJde-f+dê²âÂri^¡F.Sjø}ÒÊâ2¦Z:{\£©x|þ|N7¯PQ9O©.}rÎ\©®L#nUÊÔZYt²\#][¨IÇJ7+UZ§,©ËyÕéiYØR,ËÅVÖbX)V©0 |
| --- | Minor | ¦Ãªùß%pb±éØ,ÍÇr°Øjl¶{+ÀîIÁX*v]P `S¤	W_Kýf\è×¢Æ«ðñÀÂK¥³s[âhQ}&3!ø1EúBçý&þ}ü1	G@&7SÉ¥p~ <þ~_óMß1<2LÄÐøàà¹§Z^üwoÎÝÇáÜc¤`aðtôÒ¨çÙH(@ëB´.JÀjÃ¼<åtoðÛ|á®¡	*íëÊòÎh#I¿u¨ Éæ´	PDìÈ)2RfÚDC |
| --- | Minor | ×=r±£1mzcb#c'µÖíõGb=QuâÜãÕuÛë §c³ ²Cì_@¿Ëð¦Ä:b m`¤2AÅ`cLÌ6Æ¸­ONýÐåìvz`º#ÃoËÄº%«]ZØèÕ¾¸UQMe¡~}Þ«Ûn_ Â.t}§ÿÒÙ>v&A»ìA`ÀÕú® |
| --- | Minor | "ìj2~úàñã?ÓÄ@+í³y­@²^,ª5OJ\ü§Õ zhÆ¥ýt³R««qÒ |
| --- | Minor | µÃNÝË_C#C®ÀÈhUVKê¡Ò©§ñgD róçØëþ««Ü·ûÄ?³Äá6GÈtºbQ3tFçqi ´j\ZåâG××ån>2ÅhÂQPÇá5xÅºÞløwEEExx `#K£¯¶¿7~Â$É^"Â§Ú;/»ñ ßñÚýfÒª§²-iÓk©úcCN¨àµØÁî¨åRn¯s66ÖÐêJÈà¦ü8é^è°UiÊWU­tâ6]mkl÷åkÑ@ÚôQ-áz,e^èFw0h*3"tàö¾ZÆ~Óãiá2'X2!8zUÈ>ÈÞCXZÊ®åÑÄMåHnö/ß^÷>y^=ÝÚÖºâ¢3' ã°¿¥íPÓ ?/¼Ib§Í¦6lÒo-\c%Hh	ôy»¼]ÑóÖ¶÷Ä¡#ÐwèýFI¨Íö}øÓÜ~"ÅVíóïÐ9CÂÉîïÚõ:rð·b9&ÞPõÊ¸æÝ¼J·;r,¼Ç+µ²ã¾P/0wÕ@uµCÛU]7¦} ÁÍä°Kß%OÀ@W²§êq}¡µ¼doa©Q |
| --- | Minor | Lec{8¼³:¢UïÓo¸ê8/AÓáÒ{Ñ!\¶VeN«·Xe"âòäyt!A÷éçN&øÛ­Ù2KG?5	>}'9"D§o¥íµÍUy¥¢ª¹¶cOg¯y[Hlæ Øà¶vÑJ5K7»IèôµF»Ý¡î×Åð^ìËÅýÏ=TÈIÃ/ ãu_èæß¦ ]I6|ÇÊ¹-Iù/o+Ø,ñ0^Þ¯ÃoáóÔ*ëÛÇóþÃía §w?MíãîuÔÔ=ô34nâ	Ã,®} ­cÓóù¦mà |
| --- | Minor | ü@hôDq#r: jô[×îjÐþ/ßnyÂÊ[ì´Òv^ê}|÷îN"~Ò_º,D*v:ñµ(Ë5dèºxm°FRÖúû¸tq¦HoüiîÞ­ã¬6µEu§ÊÎ~7¦CMR´ÃZ§ÛËc­55%I¹CîIÝwÐG® ß\Fÿ$dèÂÛ: ^¼Kç5Iä`Sv·:ôu,2Óv(;ÓÀ?\tÅã«w6¿+So¼Üï@+þê®Þ³¸i¦³ÿ£ý Ì´ |
| --- | Minor | kuÉ¬ê-°q£|DÒg``8±ùMÓQ¸	Gn´ö|«M×ñ«;ÁQ©T©$`ð6øì!s¯ \9W¹U¿Wø®²$ì÷%^ãØÎßägc½ñeò!e'&þa÷Ý)ÆÚ¨rÚ-¥v-ß-1Mí~<ðCÇIìû}Ç`°ëÿ(£hZÍs°ó®êuÉIèwv6KdÛö«vB |
| --- | Minor | Ïq¾£7¬J^S°ýhñ%É·ÆØ&ãéÚ8»< ¡¸Û/º¸-m/m"6éàÄ«´4ôñýÿ CL endstream endobj 701 0 obj <</Filter/FlateDecode/Length 234>> stream xÚ]PÁnÃ ½ó>v&Hµí"µ©²eS¶i´@ÀÉ@ò÷4êaüüígZ5§Æô+8%0Bo¬8¹9(cI±mTÜ²Õ(=¡U+ýèË[ûú~¼oÅ±-ØÃå\Ï ±¿RÎGØoysËqllïs@¿×SìÚux°Ï 1;ÀîRÙû_ÑF`¤,s»âºr'/i$±x]­þWÛ]¯~d üñie2¶~»¡IüÝì©9un>Bv·;yç*¿?Óm+ endstream endobj 703 0 obj <</Subtype/Type1C/Filter/FlateDecode/Length 547>> stream xÚcd`aa`ddäs÷òõðvÒö |
| --- | Minor |  ü±áTÿ¥ÃúCáãY¦rÌ?ÄYd È{ü ò T L¬B,e5ÆzFÎùEé% É æ: F ¹©EÉy ¾%©¹%@NBp~rfjI¥MFII¾~yy¹^bn±^~Qº¦ByfIBPjqjQYj[~^_bnªÄÕzÊµ4'µèW ³Ô®ùÑÁ÷S¯{Ý÷ë¾¯^ÇøqÝ£ußMÖ}^Çü}ú÷'¢Kºww¯+ÛÓÚÝÚSÛ]7§cN÷Ì¹òß³Ïî]UÕUÓ,×ú[Tµ%¼ã{:û¹yÝåv³}î>ç6Ñ­§¹§f6HÃì9òßÅØWuöæÈýÂVYÝ]Y5¯{òþæ(ù?ì1a5UÝU³»çÊýXÆ6¯{jwßÌåß­»'pLkÔ\Û^×%×ZØèQÒÍÂV\Ñ}Nþûþ;D£Ù«æUÌ.Áñ[î÷NÑÙÎ»Ã½xYÎ®nßeßE»§w/iËñ­¡¤;«»ãO%{wú¤òþ&E¶És»tOçøÁ"ÚÃ¾zö²óçvµ·Äw5sðÏÿé8íwÒtöÍ\¹×Màáb^9.óù<ß  ~Ò endstream endobj 704 0 obj <</Filter/FlateDecode/Length 233>> stream xÚ]P=kÄ0Ýý+4^)%Î:@ë#àá®ÉAWÇVRCcÅòïûÂ |
| --- | Minor | ,£§÷$=B¤³òºÅupöiGëXycuÜ³õ¤+ÄYìDûù(Îoß%ºvMù¥[ÂqÏå©]çtªb Å×Öq´ÂáÕøöNÉºWÑf¤]BøÅ	]Îê:·+o;iopJ#)7"«8¯¡j¡3ÿj»¢ô"V=óíKÜMªäïnO/DÛÜ|ì( |
| --- | Minor | ·ïw >$U~«}m; endstream endobj 706 0 obj <</Subtype/Type1C/Filter/FlateDecode/Length 350>> stream xÚcd`aa`ddäóóqÔvöu04 ÿîaéùÙÄúCáãY¦rÌ?DXd^Èü ò ÔÖB,e5ÝÆzFÎùEé% É æ: F ¹©EÉy ¾%©¹%@NBp~rfjI¥MFII¾~yy¹^bn±^~Qº¦ByfIBPjqjQYj[~^_bnªÄÕzÊ9?· ´$µHÁ7?%µ(è,FC Y¼tðý¸Ü½ëGë®íó¿×çfþþí'³èÂî©r |
| --- | Minor | ÝM-vA*ÝeÝå1óÙfwê96ãÏÌßò1ìÛû¾vïÙóµ{;Ê®ß ì| |
| --- | Minor | ~Lù·`ê4¶ß±Øwq}gãÞ<ç;Ûr^9.óù<=<|?E ²ìv$ endstream endobj 707 0 obj <</Filter/FlateDecode/Length 249>> stream xÚ]P=o0Üý+Þªª ·j	!%DHI?¡£±ÄR°-cþ}±A:Øºw~w:_çRIÑÕ¼BTÂâ¨'ËZì¥"	!¹Û¦póåf®l@Óé»¾>çê÷ã¥©ävëF=ºÍå¹GC© |
| --- | Minor |  ¢ÅptvÝQè<÷iZ©zØ5yj2æ*1É²`¬¸8ÆÑ2Õ#Iã8´(2Jü{{[mÇoÌn&4[ðë÷ÞoüÑãÇ1ß¦ôÎ¾G|²vÉz ¿ö¥ÂGF¯ ç¥zt endstream endobj 709 0 obj <</Subtype/Type1C/Filter/FlateDecode/Length 804>> stream xÚKLwikE±øØîA#¦Q(Æ |
| --- | Minor | (¾¸Ö¶Bim×ZèÝ2ì¶¥/J[ÊK*Mh¢/xÏîõµx/Éü3ÿ(¢¯>ÝÚvqosËåGÖÇm;S¥B¹¸qTÔBÜªÄWÏ+ÿªÊv"Z³yd"¿kÖ¹G¢vR!O¬ÝÎr9"VWÍDY¦Nk©Û`8¨74Ûn§Õl¡ÑØÔtxqÀ`h"NÙdE©h5¤,\íVr |
| --- | Minor | ,å8º?MÓzÍ¥·;Í'tûÚJYK¤tÞ%;³ö¸h²ÄÿôÿÙl·9ze;D½töÈÖ²[Ä¸eçs(²r^^ Ñ!ÑèOU>ô2ú­´]Q2 t]v ¦§{¡OûëcE_/PÔdµjñÁâ¤¸­ ob£ ©KxÍåµ0áô+ºRí¡êµ&ÎO$â|2Æ'!¥C6\Ú¥Ë |
| --- | Minor | \.<Ûõnðôól 2#é¤úïþCPßçñºµp/É?tÏ¾¤¥ª« {Ï`}!Ö~Ìñfñ8p0*¿hú¥CåtÎ?6KpH2ÓÌ"û}©×ªþ'×Ú è§ÒB4ü^­ZEÍP ð°/¸ûÆã÷²X(Hàyl:9/çÒÂ­_Í;IÈgEzí¸&["XÚòâ^`A/¦»¥®IñëÐ-¦}E!êfX3SCYÀq"©¡9³[Àº |
| --- | Minor | _H¾#E(bãÌÂmÌ~X°$Ûâ×¢VÎìâÃp3ÝéöÖ¾ÍFO´Ó°ÏÇîÆF \ØÁÐ¡;Þàë óR;oç<Ì@FF¹4]¼çóK1aüxüà«ð<¦vÍNNVHxº¯V¤vÿUUªªGT«7,çU*96 «µÿ $]_g endstream endobj 710 0 obj <</Filter/FlateDecode/Length 335>> stream xÚ]Ín0Çïy;M_mà!uP&¤uíJû 41ÒQ ¾ýâí°øcÿíØE]Öªip4£h`¦]¯¤i¼ô ·^(¦²órro1´Å¾Õí 4x? |
| --- | Minor | N¹¹á'MµìÆPDugf÷oc¾ÕMë°²RóÂ±áv4;ùýkÏBß¡ID/ióL~OÄðl<oôªÍ|äÿ48ñ;5zIâLóC½mmô_Qû`<'èùÃUY&¡RçéÕä©Å{óáuXY¿`çÜJD9_±TÑ¸´>á^°ym¾p}¡7Ü^w@×	(NÜj9Õñ¾íü>4wö |
| --- | Minor | Knów]4nÃ§p-p¥õÛ· t:*yüë30Ã"õrÕ³ ¬Ý¼Ê'¿¶c[aI æ_¤H+~eéXb¨%8XÆd3:ÉºSmÞ³(é3T} u3gy(	Ü"X7*Y |
| --- | Minor | *µNFï ?Z4(Ô=?}3Â$îûsÜ½stËç_} ¤D y"Hÿ2ïTåÅ7³!Y§>7çê{Bh±·8Hyw¸wAºëx®:BóÑ\¾î·­ |
| --- | Minor | " |
| --- | Minor | ®/Wéf¨fh?Eâ9 GJ¯j£ßäè÷¥Õ=ugLnÒO1(?útÍÅ=!©Gæúlß¡>xûªÂW¡*Á#ù·{¦õ1Æná¿àÛ~ËuTG '|°·ë°µÍÃó¶¢1ë¦ßäy#¨AOÖá¼îe"`´h×FÙØ_ìßbÓÆÐTÙ®êâPeWý~ÝEA6¬gÈ º»5:fE¶ÿÍû³É¡BKIÒG÷7¯û0"WÍ{ßññ.YßÔ &Hf¡4º©ºzòÓÄ4ØN¡^Ã¾×ëu¡­CKÎ;¹éfìp¸Ì»Î 4ñè<ÑÛ¤¾AWCXZKBÜ×h7´°TË½ÌÝ°O2tëBÀôØÛÝ]P*ÒA¹X[¨­gkÍÐléô\´ÿÙyPâ» ¸^îµeîuJ¨ÚcÕÂYé(qUSÜ ×îq)»D.hµö¸{ÝË^+KDýfÍzPCà><ß5Û²ÇbðÀnõ3ö¾ÆÖSz PôWs¾þ. ëgL¼=òjé#ÞDá¨ôàÎ1£. cFGGÆ!ÇÐãÿÛßÞ endstream endobj 697 0 obj <</Subtype/Type1C/Filter/FlateDecode/Length 1242>> stream xÚURmLSW>§NiEcÍµ½º9ak°(J`ºMØèP¢©³B/´¥µ½PúaÛÛC[Vü |
| --- | Minor | ¢cY¹Ô%fgLÔeÙ²-ÑF÷Ç ËÎ-§3òã¾÷ý~Þó¼/ jjö¼·Õ´ãÍêÚ»J9O¹ýÇÉ*¿ÊSJ+T¥bô\Z¨X ¼27'¿P	tT(#ó@@ A(Õ 4 ;à. àr§ÙÅ·µòÍB£­åî²µXsF£ËÜô1/<=·þ¾¨ªz¹îv»Ý. Øm@xaXlng«¹Ój<6ÿRçª©é2[lMæVa4®.1WU;Ï\QS1WZQQnàVÜ;ï¢©m\­Y°ò9 ZÇíp4Ùx¡+ZggåÊ§Älw8\-o8M°rÛy7ïêà-\ |
| --- | Minor | Ûj¶óÜ4Û%Ó¿jÝÙ.ð.®Öaá]mØ< /u`hVè¤CF ý0 c0À8Ô9ÎÀ n	8&d³eí2"×É«äÍò/¤°FÚÇÎQVØpK.²Ä¯Eq1*Æ~Øô÷}ÑO^Çïã|¼ @QU%ý(¤ëF;·õt/'êÍÄec¤/$ë½7Þ9Tñ!ÔÏÀè»%ÇW²?i^æÂ |
| --- | Minor | !^ïÞ|§©Ñ¯G¡h8¾øÁÊoÉê3ÆÄk¨½î[¾¿'\Ý[»vø|HD¢Ê?(Ñ@¯ |
| --- | Minor | ÀêØ°[¥Ê(Ljj2ñ¾ç@µ¸>ESØ"õÌËU4ã£\«'õMØðtò4ÒC6³teþ¢³îÈ¥a6cÐF#	o?RfbCý	ý4;-ã;/×bV#HªÃóðq\7Æb(£(zu=tbßPÁ} |
| --- | Minor |  d |
| --- | Minor | "x¿#£¸tnùºE½Ç»ªø(~ÙG«	_!»qû¡Íß¸G"êA*¯y)cñPT<o½Tÿ3a@è{"­!ùä1-¢(QXåM ¤î]]bèï?ÿÅú[¸å^r¯ExJ3zÚ}yjI JÙsZ³[üÞBúè.s¹£Jãz×´um[W°ÆMV Uv=IÑ/BñHÿáùMÚ^(qf>¸M¶©Æ5¸Gùä6ãDZõV9ÆNï±U<¦º«ñ¯´¹åÕ¥H½#X¼ÔÓîi@z88D»YDÙæÌÜBé{/F÷%ÄKþ{ß=ÖusßùJCÔø¼%"ðáH@}ÒgO¬ÙÙIo/ ¢Èô4ÒÒÕÑ«0(]ã³ |
| --- | Minor | <Fæ&ã¸²£íJÔJ7f³i;ÒrÜAM-ö¤ú°)M<Ì=4g©ÓÓ^ìaóòg/61©n ×Ò:ªjÏ¡þþä§ÒVÑQ8ÛHLuÔÈ]JÈìË{z­Ø¤ Ñs'º~¹¤ÔxFz¨#yéYéÙ©Áü|ú©u³üWðÝùÿww; endstream endobj 698 0 obj <</Filter/FlateDecode/Length 311>> stream xÚ]MkÃ0ïù:nxHfÑm. íe·ÔQºÀâ'=ôßO²K;Øzl¿ßPÖe­ÂO;©èÝY§U'<:èµÜNnWckPî[óÞaùýúVTOr¿¯_*N¡ÃÞ+WÜÎuÙ\çÇZ÷dY ~QÁy±Wx(ºé|÷a;´>ÃÃQ6î¦¹ó#ê¢ Ï]¹Ø·¤¦gÓ*´­>cEQYUåêîßõåRN½úi-I%I£Õ6ÉKÏ+âD8)ñjË%x;¦@¼ö¼f.<Ì^OxçyGúÜsSáY0o<o×Ö__p}áõõÂë)ð·IxTöänºXKås6ð |
| --- | Minor | ïÞÉp[ûª² endstream endobj 700 0 obj <</Subtype/Type1C/Filter/FlateDecode/Length 2610>> stream xÚytSuÇ_Pêú õ8y9l¡Â "èØÒAÈjËÚ%4EÒ4i¤K&ÍòòîKÒìiÚ¦éBÓBZÄ)«¨TªX±GAQÑã2³ø{øp×âÌqæüÎ¹ç¼ß;çw¿÷~?¿û`©©@ [ðôìËóòV=6º±¬sÿÅ-Ë8V±¤¦°ÓìÔTÉÇ«SLKù	½g4wñCwÆY|¤º/NX¡"¦°´P¡(¬=µp^VÖåÊjuY©\#]<GúÈ%çJde-f+dê²âÂri^¡F.Sjø}ÒÊâ2¦Z:{\£©x|þ|N7¯PQ9O©.}rÎ\©®L#nUÊÔZYt²\#][¨IÇJ7+UZ§. ©ËyÕéiYØR. ËÅVÖbX)V©0 |
| --- | Minor | ¦Ãªùß%pb±éØ. ÍÇr°Øjl¶{+ÀîIÁX*v]P `S¤	W_Kýf\è×¢Æ«ðñÀÂK¥³s[âhQ}&3!ø1EúBçý&þ}ü1	G@&7SÉ¥p~ <þ~_óMß1<2LÄÐøàà¹§Z^üwoÎÝÇáÜc¤`aðtôÒ¨çÙH(@ëB´.JÀjÃ¼<åtoðÛ|á®¡	*íëÊòÎh#I¿u¨ Éæ´	PDìÈ)2RfÚDC |
| --- | Minor | ×=r±£1mzcb#c'µÖíõGb=QuâÜãÕuÛë §c³ ²Cì_@¿Ëð¦Ä:b m`¤2AÅ`cLÌ6Æ¸­ONýÐåìvz`º#ÃoËÄº%«]ZØèÕ¾¸UQMe¡~}Þ«Ûn_ Â.t}§ÿÒÙ>v&A»ìA`ÀÕú® |
| --- | Minor | "ìj2~úàñã?ÓÄ@+í³y­@²^. ª5OJ\ü§Õ zhÆ¥ýt³R««qÒ |
| --- | Minor | µÃNÝË_C#C®ÀÈhUVKê¡Ò©§ñgD róçØëþ««Ü·ûÄ?³Äá6GÈtºbQ3tFçqi ´j\ZåâG××ån>2ÅhÂQPÇá5xÅºÞløwEEExx `#K£¯¶¿7~Â$É^"Â§Ú;/»ñ ßñÚýfÒª§²-iÓk©úcCN¨àµØÁî¨åRn¯s66ÖÐêJÈà¦ü8é^è°UiÊWU­tâ6]mkl÷åkÑ@ÚôQ-áz. e^èFw0h*3"tàö¾ZÆ~Óãiá2'X2!8zUÈ>ÈÞCXZÊ®åÑÄMåHnö/ß^÷>y^=ÝÚÖºâ¢3' ã°¿¥íPÓ ?/¼Ib§Í¦6lÒo-\c%Hh	ôy»¼]ÑóÖ¶÷Ä¡#ÐwèýFI¨Íö}øÓÜ~"ÅVíóïÐ9CÂÉîïÚõ:rð·b9&ÞPõÊ¸æÝ¼J·;r. ¼Ç+µ²ã¾P/0wÕ@uµCÛU]7¦} ÁÍä°Kß%OÀ@W²§êq}¡µ¼doa©Q |
| --- | Minor | Lec{8¼³:¢UïÓo¸ê8/AÓáÒ{Ñ!\¶VeN«·Xe"âòäyt!A÷éçN&øÛ­Ù2KG?5	>}'9"D§o¥íµÍUy¥¢ª¹¶cOg¯y[Hlæ Øà¶vÑJ5K7»IèôµF»Ý¡î×Åð^ìËÅýÏ=TÈIÃ/ ãu_èæß¦ ]I6|ÇÊ¹-Iù/o+Ø. ñ0^Þ¯ÃoáóÔ*ëÛÇóþÃía §w?MíãîuÔÔ=ô34nâ	Ã. ®} ­cÓóù¦mà |
| --- | Minor | ü@hôDq#r: jô[×îjÐþ/ßnyÂÊ[ì´Òv^ê}|÷îN"~Ò_º. D*v:ñµ(Ë5dèºxm°FRÖúû¸tq¦HoüiîÞ­ã¬6µEu§ÊÎ~7¦CMR´ÃZ§ÛËc­55%I¹CîIÝwÐG® ß\Fÿ$dèÂÛ: ^¼Kç5Iä`Sv·:ôu. 2Óv(;ÓÀ?\tÅã«w6¿+So¼Üï@+þê®Þ³¸i¦³ÿ£ý Ì´ |
| --- | Minor | kuÉ¬ê-°q£|DÒg``8±ùMÓQ¸	Gn´ö|«M×ñ«;ÁQ©T©$`ð6øì!s¯ \9W¹U¿Wø®²$ì÷%^ãØÎßägc½ñeò!e'&þa÷Ý)ÆÚ¨rÚ-¥v-ß-1Mí~<ðCÇIìû}Ç`°ëÿ(£hZÍs°ó®êuÉIèwv6KdÛö«vB |
| --- | Minor | Ïq¾£7¬J^S°ýhñ%É·ÆØ&ãéÚ8»< ¡¸Û/º¸-m/m"6éàÄ«´4ôñýÿ CL endstream endobj 701 0 obj <</Filter/FlateDecode/Length 234>> stream xÚ]PÁnÃ ½ó>v&Hµí"µ©²eS¶i´@ÀÉ@ò÷4êaüüígZ5§Æô+8%0Bo¬8¹9(cI±mTÜ²Õ(=¡U+ýèË[ûú~¼oÅ±-ØÃå\Ï ±¿RÎGØoysËqllïs@¿×SìÚux°Ï 1;ÀîRÙû_ÑF`¤. s»âºr'/i$±x]­þWÛ]¯~d üñie2¶~»¡IüÝì©9un>Bv·;yç*¿?Óm+ endstream endobj 703 0 obj <</Subtype/Type1C/Filter/FlateDecode/Length 547>> stream xÚcd`aa`ddäs÷òõðvÒö |
| --- | Minor |  ü±áTÿ¥ÃúCáãY¦rÌ?ÄYd È{ü ò T L¬B. e5ÆzFÎùEé% É æ: F ¹©EÉy ¾%©¹%@NBp~rfjI¥MFII¾~yy¹^bn±^~Qº¦ByfIBPjqjQYj[~^_bnªÄÕzÊµ4'µèW ³Ô®ùÑÁ÷S¯{Ý÷ë¾¯^ÇøqÝ£ußMÖ}^Çü}ú÷'¢Kºww¯+ÛÓÚÝÚSÛ]7§cN÷Ì¹òß³Ïî]UÕUÓ. ×ú[Tµ%¼ã{:û¹yÝåv³}î>ç6Ñ­§¹§f6HÃì9òßÅØWuöæÈýÂVYÝ]Y5¯{òþæ(ù?ì1a5UÝU³»çÊýXÆ6¯{jwßÌåß­»'pLkÔ\Û^×%×ZØèQÒÍÂV\Ñ}Nþûþ;D£Ù«æUÌ.Áñ[î÷NÑÙÎ»Ã½xYÎ®nßeßE»§w/iËñ­¡¤;«»ãO%{wú¤òþ&E¶És»tOçøÁ"ÚÃ¾zö²óçvµ·Äw5sðÏÿé8íwÒtöÍ\¹×Màáb^9.óù<ß  ~Ò endstream endobj 704 0 obj <</Filter/FlateDecode/Length 233>> stream xÚ]P=kÄ0Ýý+4^)%Î:@ë#àá®ÉAWÇVRCcÅòïûÂ. £§÷$=B¤³òºÅupöiGëXycuÜ³õ¤+ÄYìDûù(Îoß%ºvMù¥[ÂqÏå©]çtªb Å×Öq´ÂáÕøöNÉºWÑf¤]BøÅ	]Îê:·+o;iopJ#)7"«8¯¡j¡3ÿj»¢ô"V=óíKÜMªäïnO/DÛÜ|ì( |
| --- | Minor | ·ïw >$U~«}m; endstream endobj 706 0 obj <</Subtype/Type1C/Filter/FlateDecode/Length 350>> stream xÚcd`aa`ddäóóqÔvöu04 ÿîaéùÙÄúCáãY¦rÌ?DXd^Èü ò ÔÖB. e5ÝÆzFÎùEé% É æ: F ¹©EÉy ¾%©¹%@NBp~rfjI¥MFII¾~yy¹^bn±^~Qº¦ByfIBPjqjQYj[~^_bnªÄÕzÊ9?· ´$µHÁ7?%µ(è. FC Y¼tðý¸Ü½ëGë®íó¿×çfþþí'³èÂî©r |
| --- | Minor | ÝM-vA*ÝeÝå1óÙfwê96ãÏÌßò1ìÛû¾vïÙóµ{;Ê®ß ì| |
| --- | Minor | ~Lù·`ê4¶ß±Øwq}gãÞ<ç;Ûr^9.óù<=<|?E ²ìv$ endstream endobj 707 0 obj <</Filter/FlateDecode/Length 249>> stream xÚ]P=o0Üý+Þªª ·j	!%DHI?¡£±ÄR°-cþ}±A:Øºw~w:_çRIÑÕ¼BTÂâ¨'ËZì¥"	!¹Û¦póåf®l@Óé»¾>çê÷ã¥©ävëF=ºÍå¹GC© |
| --- | Minor |  ¢ÅptvÝQè<÷iZ©zØ5yj2æ*1É²`¬¸8ÆÑ2Õ#Iã8´(2Jü{{[mÇoÌn&4[ðë÷ÞoüÑãÇ1ß¦ôÎ¾G|²vÉz ¿ö¥ÂGF¯ ç¥zt endstream endobj 709 0 obj <</Subtype/Type1C/Filter/FlateDecode/Length 804>> stream xÚKLwikE±øØîA#¦Q(Æ |
| --- | Minor | (¾¸Ö¶Bim×ZèÝ2ì¶¥/J[ÊK*Mh¢/xÏîõµx/Éü3ÿ(¢¯>ÝÚvqosËåGÖÇm;S¥B¹¸qTÔBÜªÄWÏ+ÿªÊv"Z³yd"¿kÖ¹G¢vR!O¬ÝÎr9"VWÍDY¦Nk©Û`8¨74Ûn§Õl¡ÑØÔtxqÀ`h"NÙdE©h5¤. \íVr |
| --- | Minor | . å8º?MÓzÍ¥·;Í'tûÚJYK¤tÞ%;³ö¸h²ÄÿôÿÙl·9ze;D½töÈÖ²[Ä¸eçs(²r^^ Ñ!ÑèOU>ô2ú­´]Q2 t]v ¦§{¡OûëcE_/PÔdµjñÁâ¤¸­ ob£ ©KxÍåµ0áô+ºRí¡êµ&ÎO$â|2Æ'!¥C6\Ú¥Ë |
| --- | Minor | \.<Ûõnðôól 2#é¤úïþCPßçñºµp/É?tÏ¾¤¥ª« {Ï`}!Ö~Ìñfñ8p0*¿hú¥CåtÎ?6KpH2ÓÌ"û}©×ªþ'×Ú è§ÒB4ü^­ZEÍP ð°/¸ûÆã÷²X(Hàyl:9/çÒÂ­_Í;IÈgEzí¸&["XÚòâ^`A/¦»¥®IñëÐ-¦}E!êfX3SCYÀq"©¡9³[Àº |
| --- | Minor | _H¾#E(bãÌÂmÌ~X°$Ûâ×¢VÎìâÃp3ÝéöÖ¾ÍFO´Ó°ÏÇîÆF \ØÁÐ¡;Þàë óR;oç<Ì@FF¹4]¼çóK1aüxüà«ð<¦vÍNNVHxº¯V¤vÿUUªªGT«7. çU*96 «µÿ $]_g endstream endobj 710 0 obj <</Filter/FlateDecode/Length 335>> stream xÚ]Ín0Çïy;M_mà!uP&¤uíJû 41ÒQ ¾ýâí°øcÿíØE]Öªip4£h`¦]¯¤i¼ô ·^(¦²órro1´Å¾Õí 4x?. |
| --- | Minor | Sentence exceeds complexity threshold, split for readability. Applying the split needs --strength moderate or higher. |
| --- | Minor | none (split proposal only; source not rewritten) |
| --- | Minor | none |
| --- | Minor | Check: NEEDS-LLM |
| --- | Minor | Flags:    not-assessed |
| --- | Minor | SENTENCE (Line 1413, 326 words, 5 clauses)  [Script] |
| --- | Minor | ÞvÏÅþ½\ÎUÄ¨Îh¼ë²yL3µêFÊ9¡48Y½i6ºÚÊñ Oè;	¦W7ººó4w­¿a 5Óä¹|Gb0éViÕ |
| --- | Minor | ÃòªÊ	(ùïíË¥\;ñÕÂãWÖ­!|½qleæ!ËÄ±5³È±5××È^¡K=§È^¡óuÖegÛ<O}Ýë¦çy»àrø÷^ËAâ«[¶TH¶Þ-©>ÇëüÛ¦¸cívîVÓîüýzÔå « endstream endobj 712 0 obj <</Subtype/Type1C/Filter/FlateDecode/Length 2940>> stream xÚ¥ViTW®¢¡«DD1VDcªÚ¨Q5Æ%F¢¨q%²4;4B7;4b7EhÀ¦YºDÃ*Hu¢	jBF |
| --- | Minor | c¢ ,-	 ,IÆqv^ìäì¼h­ ~Ábi¼hÎÊ ©4rÅ±±±N>áÑN¨ÀUsE±ÁÒ ÑNq´8*Fì/rDHE[}ÂÅ"3e'³Y+	IÅQ¢-qTÏtü<ÂÙjÅÇÄ:r3áFøþd FJ"HáÛvÄDâ-bÁoS©Ä;K¼OÌ&æku+±ØBl%¶îÄ>BNLµ HÂØF|EN"vþq2ËÇ­l­â¬¾Ê&JFÝ¡ |
| --- | Minor | ?Çä±ö;iì^£ÂÖt}F%êïDW5¤qj§À¸Å2è°TUU2HæðÔ%,­T ²dwá.*YR©J9Ä¯É «ªm)kkÔÇèMÖz²eU |
| --- | Minor | Éè#©×B®îÿqvàà5?Y¸F9Üa£êý®:WwºàúÜ0Ý|K5×h,Å×`p-yÚá<Ü¿»TùìnQ |
| --- | Minor | sñ.øÖÃvX(w£cÞsMGñ¡]C"ù=ºn²ctÊìHÖ×oO´#Ð!.Âe=ZD(älP°Eõ ::BÍLCå¨(næÌnÑo/È/ôjB2u«¡¬ôËÞ¾KðÆÎ¾í°ÍJçE§3J+Ô§Îï9[wûzÍY îZ¹k\°5'â·íå© (ÚÈ	ëÐz«0¡"6}<îpº$]fáêo#:õür-ùÍ3äû/ÊG{çv¼íþ°ã/¬	º@¬©2VFJümAB4åçG¿qðÃÆYÚ{ú¾ðýÝÂÞ¢;\jk4Ú:CKeÙ­î¨*®HÉÁºäÄð0©rë¸¬ô,H¡¡}­!l0zó"ÞúV`dMï08Ã¦@VVZ2¾5êgñ ¦®b¥!ÂûªèíÍû¼RjâX3÷ÃKÃtê£3j¨×w{1\õ¹_¬!GHùHDÆ>¦äÈçi­@#»ÕÇ2TéP¦|7[uXqZ²NÔxwRñ /c*7ïh±úT÷}èWa\y`øC@ÖnÉþ¸p¿°=ð)lj^£UYù |
| --- | Minor | ´^[ÑÐQv`á]gD!»OÐD/}­¹}à(¦_5Y×í½èò9º^1=ºçà.ýÃE§éKÖÌg! |
| --- | Minor | ÞvÏÅþ½\ÎUÄ¨Îh¼ë²yL3µêFÊ9¡48Y½i6ºÚÊñ Oè;	¦W7ººó4w­¿a 5Óä¹|Gb0éViÕ |
| --- | Minor | ÃòªÊ	(ùïíË¥\;ñÕÂãWÖ­!|½qleæ!ËÄ±5³È±5××È^¡K=§È^¡óuÖegÛ<O}Ýë¦çy»àrø÷^ËAâ«[¶TH¶Þ-©>ÇëüÛ¦¸cívîVÓîüýzÔå « endstream endobj 712 0 obj <</Subtype/Type1C/Filter/FlateDecode/Length 2940>> stream xÚ¥ViTW®¢¡«DD1VDcªÚ¨Q5Æ%F¢¨q%²4;4B7;4b7EhÀ¦YºDÃ*Hu¢	jBF |
| --- | Minor | c¢. -	. IÆqv^ìäì¼h­ ~Ábi¼hÎÊ ©4rÅ±±±N>áÑN¨ÀUsE±ÁÒ ÑNq´8*Fì/rDHE[}ÂÅ"3e'³Y+	IÅQ¢-qTÏtü<ÂÙjÅÇÄ:r3áFøþd FJ"HáÛvÄDâ-bÁoS©Ä;K¼OÌ&æku+±ØBl%¶îÄ>BNLµ HÂØF|EN"vþq2ËÇ­l­â¬¾Ê&JFÝ¡ |
| --- | Minor | ?Çä±ö;iì^£ÂÖt}F%êïDW5¤qj§À¸Å2è°TUU2HæðÔ%. ­T ²dwá.*YR©J9Ä¯É «ªm)kkÔÇèMÖz²eU |
| --- | Minor | Éè#©×B®îÿqvàà5?Y¸F9Üa£êý®:WwºàúÜ0Ý|K5×h. Å×`p-yÚá<Ü¿»TùìnQ |
| --- | Minor | sñ.øÖÃvX(w£cÞsMGñ¡]C"ù=ºn²ctÊìHÖ×oO´#Ð!.Âe=ZD(älP°Eõ ::BÍLCå¨(næÌnÑo/È/ôjB2u«¡¬ôËÞ¾KðÆÎ¾í°ÍJçE§3J+Ô§Îï9[wûzÍY îZ¹k\°5'â·íå© (ÚÈ	ëÐz«0¡"6}<îpº$]fáêo#:õür-ùÍ3äû/ÊG{çv¼íþ°ã/¬	º@¬©2VFJümAB4åçG¿qðÃÆYÚ{ú¾ðýÝÂÞ¢;\jk4Ú:CKeÙ­î¨*®HÉÁºäÄð0©rë¸¬ô. H¡¡}­!l0zó"ÞúV`dMï08Ã¦@VVZ2¾5êgñ ¦®b¥!ÂûªèíÍû¼RjâX3÷ÃKÃtê£3j¨×w{1\õ¹_¬!GHùHDÆ>¦äÈçi­@#»ÕÇ2TéP¦|7[uXqZ²NÔxwRñ /c*7ïh±úT÷}èWa\y`øC@ÖnÉþ¸p¿°=ð)lj^£UYù |
| --- | Minor | ´^[ÑÐQv`á]gD!»OÐD/}­¹}à(¦_5Y×í½èò9º^1=ºçà.ýÃE§éKÖÌg!. |
| --- | Minor | Sentence exceeds complexity threshold, split for readability. Applying the split needs --strength moderate or higher. |
| --- | Minor | none (split proposal only; source not rewritten) |
| --- | Minor | none |
| --- | Minor | Check: NEEDS-LLM |
| --- | Minor | Flags:    not-assessed |
| --- | Minor | SENTENCE (Line 1413, 551 words, 5 clauses)  [Script] |
| --- | Minor | q¯Æ¢ù¢5gu5¿kÞ±&Åò;Õü­)OÆ^ª?I¢YP@À´0aÂØ!fÞÀ×Î\¡² CeO¨áÒð¸¤	~>u@©ÂÆN½'D+ r[J7#P¬ÕèÃ­ðNNj 7ª¦|"ËB¿mMy¼vj{·¿A`üi%3zë¯Ç_çýõ3·¡ÏûPj>6q(ógêiqØ7 ¦ÑR8¾¹OæIØæñ­êÁÃc¼¾|F7íôæJÆjª	J³'BoÅðÜ mfh©7L*þ$ÞÆ·1C=Ù×öP²q	³IíÙ |
| --- | Minor | û²h5TáóÄ9©Ù%@AÁqí¥Ê (M¥"#5ÈÍ~ß¥Mê]¼¢c/ÅKÏñ¸tDD=U+AE©5ÁàA»îáË [ ^8¸,ÞW2ÐÇaw*ÒJøòÌÎ)(ÊÍÏ-Ô·ö»}ò¹Âÿ1<ÂÁÃC³ªÍ¦GQ:Ã£Z=Ù>"nóB/CÝÌSÇsÎËVn¯¯Õ×èX¨N*å5×\ {züsaÔÅÅºÅâB/ùýàMBöó<q­¸è¢û¹?qÂvQ¾I1ÐyuéfôsßßÔÅÂW_Þ@Îy<iz#§Gâv²i5Þ ABÝ8áÁá@*è§ÆWÃ0Çÿ6Mäúà¬ÞÐDo¦cZ^p3>£\F¯3Gb%~^Ñà~ÕÑÍ§3ÏÂ¸\ØRÕTÝÜ¡ïæk­+ºÞÇKk@~µh¬B7Æ(ÑæCÕÇK<Op'`³ÑDôÖ¹ª\EQ ÇÿB2(âÁ¼*Ã;Ã;á*ÔÓÙµL!Ý¯n4rñôl©YbìS6\»[RëÈú>~¯±OVßdÂTQ:8	Õù­Q§3«¾}ó.§ND×*ÏfQdfB"_RQZ^XUÒ¸MÏxùDUø{=gëÇxÖUÆÊ¢ÒC!|5aÚ÷d_ð¢×>wCöÈYtßcábhkHùötÁã¿j9hÎ«UkÊ«ôÅ:þo	óddLIB3â>?ath2|´{×Ù.+Ëú9s#âk¦DÖ|´ÜL2xnªÕ-¡¼å° |
| --- | Minor | ¡N«z \sNóuImCgûï1üô õ«ÏúÓ5.ûë6U;èêZ¡íO×h#õâÞÙþkÇöîbqüÿÎ\ |
| --- | Minor | ¯ó¢ (Av3í±ýLLðéh72MBÌË§ÈÅr¼Ù |
| --- | Minor | ¦¨ÅY8§à¶Ú¦V¾¶¨ª Oönð/å.éç¿ß<(õ¦U'Hã6ô=SÝÓXÒM¨ |yBße¨&e¡ Myäg­QõáÈ)5'ùIÁ@PxB\Ìgj>ò«¶/HÊÏ(R(8WlÆâÅ'ùNw¥0ú¦ºÆz¡©©¶ßèÏ#zgnx\+HÉË7¯¶_ùXÎ»àÑ  _]c>í§pã§½n>}²³Îo}íìEQ _åªYU ­9WàYÐÔ¨âRU^M½®¾¶np®½FÊOE#ÐÇ+º¡ÞüÁHË;Ø`®ãÍar½3¾Þa R).,/òFlÌîí8û8UPV¢K©8T§ASy±¶©4®U#IÑÑJ!ö9F¬ÆêóllÊlÆ±ÖK56cÐÈ¤ÿmW* endstream endobj 713 0 obj <</Filter/FlateDecode/Length 261>> stream xÚ]PËjÃ0¼ë+öRi]Â:¸â¶C²´vµ zfvµ;&*ªC¥äÑÕ¼Á	:©ÅQÏ#´ØKEäÓZÌ¨¨ù`Bô~ú>E]WÙÓõR&ìËÍ ¤k]Û8áP©N¥ :;Áq²7ØìnñÁ÷>­@+UkÑN3óª	bçA.Y,q-p4£eªGBã8Z9A%þ½½,mÇ%tûæ&ã8-rB÷; 4ÛîÀñÝÂw¿&;ðÚ«ÿÅÇqOÏÖ:!³7+Þc5Úø­pþ ¨îv endstream endobj 715 0 obj <</Subtype/Type1C/Filter/FlateDecode/Length 922>> stream xÚÎmL[eÀñçÒÂYi¨kÜhïtËH©3q aÊè&Ût[â*íh¾Þ^úíEº¶´=´å¥-èZZÜÂ188Æ2>ÌÈçk2Ë¾üNÎùrþEQ5¯wi:»:´«Õo¾¼}8â{Å¿mù+ù=ßKñ |
| --- | Minor | ¼\ÄïËtK*BÞößºm7vmûBQà$¦(Ü×Q©^RªTÛ­6cì5°ô¾ýô­­è*U+ÝfÖ3Æ­VkYÞ¬eË>cí1êY½ï°em¯47»\.¥ÖìPZÞ×ö7Ñ.#k OëzÆ©×ÑÇ­>©5ëé'íÊ'¶[Í¶>VÏÐj«NÏX¢*_E¨½Y cåý4ªª@£6ô3ÕBýTÑÇkù:á\´	EJ"ÒBæ,Ó74@ûþÌ_¿ºoí·/è&9oúD>D:k·8KKDÌ[("!X´UÃ?Nbc+§307ð+<à{À |
| --- | Minor | ¨ì`ûcÄs@  F9Ç}ð!à"Gd62B@$ TýwQæl9~¶| Ù¿M-Á4. |
| --- | Minor | q¯Æ¢ù¢5gu5¿kÞ±&Åò;Õü­)OÆ^ª?I¢YP@À´0aÂØ!fÞÀ×Î\¡² CeO¨áÒð¸¤	~>u@©ÂÆN½'D+ r[J7#P¬ÕèÃ­ðNNj 7ª¦|"ËB¿mMy¼vj{·¿A`üi%3zë¯Ç_çýõ3·¡ÏûPj>6q(ógêiqØ7 ¦ÑR8¾¹OæIØæñ­êÁÃc¼¾|F7íôæJÆjª	J³'BoÅðÜ mfh©7L*þ$ÞÆ·1C=Ù×öP²q	³IíÙ |
| --- | Minor | û²h5TáóÄ9©Ù%@AÁqí¥Ê (M¥"#5ÈÍ~ß¥Mê]¼¢c/ÅKÏñ¸tDD=U+AE©5ÁàA»îáË [ ^8¸. ÞW2ÐÇaw*ÒJøòÌÎ)(ÊÍÏ-Ô·ö»}ò¹Âÿ1<ÂÁÃC³ªÍ¦GQ:Ã£Z=Ù>"nóB/CÝÌSÇsÎËVn¯¯Õ×èX¨N*å5×\ {züsaÔÅÅºÅâB/ùýàMBöó<q­¸è¢û¹?qÂvQ¾I1ÐyuéfôsßßÔÅÂW_Þ@Îy<iz#§Gâv²i5Þ ABÝ8áÁá@*è§ÆWÃ0Çÿ6Mäúà¬ÞÐDo¦cZ^p3>£\F¯3Gb%~^Ñà~ÕÑÍ§3ÏÂ¸\ØRÕTÝÜ¡ïæk­+ºÞÇKk@~µh¬B7Æ(ÑæCÕÇK<Op'`³ÑDôÖ¹ª\EQ ÇÿB2(âÁ¼*Ã;Ã;á*ÔÓÙµL!Ý¯n4rñôl©YbìS6\»[RëÈú>~¯±OVßdÂTQ:8	Õù­Q§3«¾}ó.§ND×*ÏfQdfB"_RQZ^XUÒ¸MÏxùDUø{=gëÇxÖUÆÊ¢ÒC!|5aÚ÷d_ð¢×>wCöÈYtßcábhkHùötÁã¿j9hÎ«UkÊ«ôÅ:þo	óddLIB3â>?ath2|´{×Ù.+Ëú9s#âk¦DÖ|´ÜL2xnªÕ-¡¼å° |
| --- | Minor | ¡N«z \sNóuImCgûï1üô õ«ÏúÓ5.ûë6U;èêZ¡íO×h#õâÞÙþkÇöîbqüÿÎ\ |
| --- | Minor | ¯ó¢ (Av3í±ýLLðéh72MBÌË§ÈÅr¼Ù |
| --- | Minor | ¦¨ÅY8§à¶Ú¦V¾¶¨ª Oönð/å.éç¿ß<(õ¦U'Hã6ô=SÝÓXÒM¨ |yBße¨&e¡ Myäg­QõáÈ)5'ùIÁ@PxB\Ìgj>ò«¶/HÊÏ(R(8WlÆâÅ'ùNw¥0ú¦ºÆz¡©©¶ßèÏ#zgnx\+HÉË7¯¶_ùXÎ»àÑ  _]c>í§pã§½n>}²³Îo}íìEQ _åªYU ­9WàYÐÔ¨âRU^M½®¾¶np®½FÊOE#ÐÇ+º¡ÞüÁHË;Ø`®ãÍar½3¾Þa R).. /òFlÌîí8û8UPV¢K©8T§ASy±¶©4®U#IÑÑJ!ö9F¬ÆêóllÊlÆ±ÖK56cÐÈ¤ÿmW* endstream endobj 713 0 obj <</Filter/FlateDecode/Length 261>> stream xÚ]PËjÃ0¼ë+öRi]Â:¸â¶C²´vµ zfvµ;&*ªC¥äÑÕ¼Á	:©ÅQÏ#´ØKEäÓZÌ¨¨ù`Bô~ú>E]WÙÓõR&ìËÍ ¤k]Û8áP©N¥ :;Áq²7ØìnñÁ÷>­@+UkÑN3óª	bçA.Y. q-p4£eªGBã8Z9A%þ½½. mÇ%tûæ&ã8-rB÷; 4ÛîÀñÝÂw¿&;ðÚ«ÿÅÇqOÏÖ:!³7+Þc5Úø­pþ ¨îv endstream endobj 715 0 obj <</Subtype/Type1C/Filter/FlateDecode/Length 922>> stream xÚÎmL[eÀñçÒÂYi¨kÜhïtËH©3q aÊè&Ût[â*íh¾Þ^úíEº¶´=´å¥-èZZÜÂ188Æ2>ÌÈçk2Ë¾üNÎùrþEQ5¯wi:»:´«Õo¾¼}8â{Å¿mù+ù=ßKñ |
| --- | Minor | ¼\ÄïËtK*BÞößºm7vmûBQà$¦(Ü×Q©^RªTÛ­6cì5°ô¾ýô­­è*U+ÝfÖ3Æ­VkYÞ¬eË>cí1êY½ï°em¯47»\.¥ÖìPZÞ×ö7Ñ.#k OëzÆ©×ÑÇ­>©5ëé'íÊ'¶[Í¶>VÏÐj«NÏX¢*_E¨½Y cåý4ªª@£6ô3ÕBýTÑÇkù:á\´	EJ"ÒBæ. Ó74@ûþÌ_¿ºoí·/è&9oúD>D:k·8KKDÌ[("!X´UÃ?Nbc+§307ð+<à{À |
| --- | Minor | ¨ì`ûcÄs@  F9Ç}ð!à"Gd62B@$ TýwQæl9~¶| Ù¿M-Á4.. |
| --- | Minor | Sentence exceeds complexity threshold, split for readability. Applying the split needs --strength moderate or higher. |
| --- | Minor | none (split proposal only; source not rewritten) |
| --- | Minor | none |
| --- | Minor | Check: NEEDS-LLM |
| --- | Minor | Flags:    not-assessed |
| --- | Minor | SENTENCE (Line 1413, 155 words, 3 clauses)  [Script] |
| --- | Minor | äM:³éÂ{7äýXØÀµüÝ¡É=,¨Õ?Éøß"^Ç×K¹°±.cæ*/~4óÙ÷GgOÍB£ð hºßB¤ä­_þI'ßO_ õzßV+]Ç ·W¾V@<Fðýõ©;wVaaÞQþÒ5TâwH}~%GÙÚµUÙÜKiÖf±[¬w¶47?'?%<&RÉb"O&R0ïjnhÏ²¾PÂg >O^¸\¸87Î± p½À;B½lÐÎÈCôãî¥Þ/7?'²ÙXtÒ#÷A4tt¿wª°Ç?YT@nlêå°s¤q;úu]ÄÊÆÂòA¸tÙmæ Å7 Ï ÂáyZ;ùâ6,>.EMÂ®a× |
| --- | Minor | (öúñ"|(B²Ñ«eóá,à±iâ`ÀaIÄ 6Å.<éwëÞÕ0:ÀçM·î)`±°9ÿÅ­ï¯- ^Ë¾¢û*ky¾=N[¾J¸Ú!¯ÊITHvÞ¬^ßy3!õÿ¹Ä^ endstream endobj 716 0 obj <</Filter/FlateDecode/Length 265>> stream xÚ]Qk0Çßý÷Ø1ÆÇ@NéÖu¨í{LN¨Iãß~&JvpßåþwÇ?ÌË¢ÂBøm«ÑB' Ú_Ú»øpmN$Ýªhfo\õ<ZJÙ)HÓ  ¬£53ì\µøäjÃÑÙÃî×¾ROZßq@i! |
| --- | Minor | äM:³éÂ{7äýXØÀµüÝ¡É=. ¨Õ?Éøß"^Ç×K¹°±.cæ*/~4óÙ÷GgOÍB£ð hºßB¤ä­_þI'ßO_ õzßV+]Ç ·W¾V@<Fðýõ©;wVaaÞQþÒ5TâwH}~%GÙÚµUÙÜKiÖf±[¬w¶47?'?%<&RÉb"O&R0ïjnhÏ²¾PÂg >O^¸\¸87Î± p½À;B½lÐÎÈCôãî¥Þ/7?'²ÙXtÒ#÷A4tt¿wª°Ç?YT@nlêå°s¤q;úu]ÄÊÆÂòA¸tÙmæ Å7 Ï ÂáyZ;ùâ6. >.EMÂ®a× |
| --- | Minor | (öúñ"|(B²Ñ«eóá. à±iâ`ÀaIÄ 6Å.<éwëÞÕ0:ÀçM·î)`±°9ÿÅ­ï¯- ^Ë¾¢û*ky¾=N[¾J¸Ú!¯ÊITHvÞ¬^ßy3!õÿ¹Ä^ endstream endobj 716 0 obj <</Filter/FlateDecode/Length 265>> stream xÚ]Qk0Çßý÷Ø1ÆÇ@NéÖu¨í{LN¨Iãß~&JvpßåþwÇ?ÌË¢ÂBøm«ÑB' Ú_Ú»øpmN$Ýªhfo\õ<ZJÙ)HÓ  ¬£53ì\µøäjÃÑÙÃî×¾ROZßq@i!. |
| --- | Minor | Sentence exceeds complexity threshold, split for readability. Applying the split needs --strength moderate or higher. |
| --- | Minor | none (split proposal only; source not rewritten) |
| --- | Minor | none |
| --- | Minor | Check: NEEDS-LLM |
| --- | Minor | Flags:    not-assessed |
| --- | Minor | SENTENCE (Line 1413, 83 words, 0 clauses)  [Script] |
| --- | Minor | ²Ì#ëLq5eh¨ì1H£%2HOKdJþïÿ°ªÚýPãºI¾tGQB2GñûJ/ØÓëFo+üÜmÛàìy¸Ã&c;½Þw¬ø°Y+íT>ÿ Çð|¼ endstream endobj 717 0 obj <</Filter/FlateDecode/Length 273>> stream xÚ]QMO0½÷WÌq1|)zhHV	¨Yv³^¡°¦Ào?pÚy3y3óäUQI±@ð©'Öà½\ã<­!t8I¢¸`Ëî¹­"A^·ê½ëW}|»Þçõ)}¸Ë(½O8o !Þýªh¶yÁ±ýàdøæEop8ò©Ã;ûÐµ.yã"ÍªÔ(I9ºÈOÄ&³jêVHhf@Ë2#(ù¿·'_Ñõì»ÕÆ¯&3!4ytØBÓÈac.<. |
| --- | Minor | ²Ì#ëLq5eh¨ì1H£%2HOKdJþïÿ°ªÚýPãºI¾tGQB2GñûJ/ØÓëFo+üÜmÛàìy¸Ã&c;½Þw¬ø°Y+íT>ÿ Çð|¼ endstream endobj 717 0 obj <</Filter/FlateDecode/Length 273>> stream xÚ]QMO0½÷WÌq1|)zhHV	¨Yv³^¡°¦Ào?pÚy3y3óäUQI±@ð©'Öà½\ã<­!t8I¢¸`Ëî¹­"A^·ê½ëW}|»Þçõ)}¸Ë(½O8o !Þýªh¶yÁ±ýàdøæEop8ò©Ã;ûÐµ.yã"ÍªÔ(I9ºÈOÄ&³jêVHhf@Ë2#(ù¿·'_Ñõì»ÕÆ¯&3!4ytØBÓÈac.<. |
| --- | Minor | Sentence exceeds complexity threshold, split for readability. Applying the split needs --strength moderate or higher. |
| --- | Minor | none (split proposal only; source not rewritten) |
| --- | Minor | none |
| --- | Minor | Check: NEEDS-LLM |
| --- | Minor | Flags:    not-assessed |
| --- | Minor | SENTENCE (Line 1413, 587 words, 13 clauses)  [Script] |
| --- | Minor | ~~qØË½³D{ûÄ¶ObÏîþÍd»éÆV­ÍJN]'ÝKH¼}­rç®î endstream endobj 719 0 obj <</Subtype/Type1C/Filter/FlateDecode/Length 1151>> stream xÚ­OSWÇïkkßÃu8/â¦¯/FÕ9Ù4ÃÝ ÝT[~¨ýõxüRùQ@íëáÀ@`jÁ´b-:m¸%m²§S Kº,Ó©ìw»¯Ëöº¿aÉÍ797ß{Îçs(¤Ñ ¢t9¹ë6æ,IÍÜ¼2¯,#Ms5þ©ÚiòËHKÉóT2§gkæ!þèÏ3"~!¢Ñ\4Åå |
| --- | Minor | ×â |
| --- | Minor | å©6{PTP(òv-æ%%%.åIü:Y(Úe´òF±Ðl1J°ßbÛUd+øEo¢}uBBYYY¼ÑRo Ö,^Êüfs±Y(5ø4Uä³3aHªÍb/Íi3+Bv	2¨V #² rSbÐLô"bQ ÊB[Q QHÞA¡ìÔªV]ÑO¾Oã<9¬Xdñ¶Ë> z2Çµ]àu8@¨äÈ8£+p8¼Ð¥Çcd\[	ÏÞ..ZÆ¥)Uº6¯LªåÏðö.`Ä ¤KXÜsS.GY#lð÷¿ÀWð5w]õÞë<ÂÞµÝÙ |
| --- | Minor | )°2`á¾-mEjÕn`=Á}ß«1ÁúKÏX ÀhÜk}Ì³Fz7TÅqy&m¨yFF& ¤æÑqÐÙ¯¤¹`t/HÝÁ·ÿ®ÏáMl¾Vªt¦¨©?¸*!´xÖã³§î]?ãã÷_Û!Óî»lå«¹vxOÿ¸·*°;94zá0¼¹Zë?Hy+8%Öét»a/#oÐþÇcr®ÒjVË£x Wm5ùíÙöX¾¬ðW'rVÖÓð¨i`àË£ð[éD8Ú¯ÿ^%/dÉ?¤V²:ØêÇqêú¸><q^-ÛðûpihÞ'Ó%Ú9}¢×ÇÁñºcmýÝÐÌíq­ÞAo¥Gº¸q¼Í,âà¾ÁOz/´æôçiþ&õ¡ülÚ	;L&¸ÜÎ­d_Û¿ç½ÜþAF®ÞÅY-LôÓÊX´ Ï+ÊQObÿØt~1ïfÅ |
| --- | Minor | °ek±q?Ði&úë·éIç4ÎD·6Ülº|ù«]ù*æKz¼ÆªÉ£·ºó29"üÆè©ÙÊ)qûëãáÁPó)¤«Ü;]{ ²êâLôQ©­ªa_]u÷¶ÜØ×:ÛÝÐ2§û£#\.Ò¤âò¬Æ÷s8!yíx6ÛZßà	\Ëjjö|s[YÉÎ¦@×M©7ÂPÕPßpìhç¿ït_ß½%±åÑ!ÆYë¬PûÇÛÎ»:#þ­ ÝÏDöÈ©ÝØÖÞÖ£%Æ:8=ü\ U§Ó=ÏM×$ztQòYÿ~18æ endstream endobj 721 0 obj <</Subtype/Type1C/Filter/FlateDecode/Length 300>> stream xÚcd`aa`ddäðvöñÓvöu° 	È|)aãú9õÃYÆrL?ä³È200|ïøAä+) g¦¤ë9çTe¦g(h$k*ZZë(X*8æ¦e&'æ)ø&d¤æ& 99 ÁùÉ©% 6%%Vúúåååz¹ÅzùEév: å% A©Å©Ee©) nùy% ~¹© `×ëIçüÜÒÔ"ßüÔ¢< ãD;##ú¾~\ðþcË÷Ìßwÿ¬ý}è·ÑÌüï¿ó~ßòwærV¾\7¸w®âá¹1W¥2óûC j¤b9 endstream endobj 722 0 obj <</Filter/FlateDecode/Length 529>> stream xÚ]]k£@@ßýóØe)QGgÔD´»Km_öÍè$+4*Æ<äß¯Î¹¤P!3_÷Ì»ÈöÛ}ÛjñgèªÂêØ´õà.Ýu¨:¸SÓQ¬ê¦üu.û`½ý¯òìÔ"ÛäÅß/¯oÝ¹loîtý,Ç÷<2ªvG¿ßz§báý¶¸]FwÞ·ÇN­VRiZszØÔÝÁýÛ~µö¤>²Â·×¾ÿtg×*Ök¿\]ÕÕîÒÊöäU8}kµÊ§o¸¶þÖo,ÓÇê_9ÌÃ£çix&ÑÚSæÉ@qL_iú6ôiU«è |
| --- | Minor | ´õ45zÚ1/ræA:¢/n® ÃHYF =1Ræ-! Ök!1b%!{ØBâ¹ÄS(Øû´?òÂÚak#$O<È§ÙAXk¢§ÂLs)LCO+gÌnS<cY³x)ùÙCgJC,7Äàr'.VHNU.s0¸hNÓ;2¸¤¦ÁÅ á¢%9ÓâBÎ,wÂ'¬xÝ§d¼X\,y±¸XNÚÊ=#v#7ò~+íö«Eæï¾Zü©Gþ-Æa@ä÷åZúg-ïw~àsaº×¥ê:SðÕË ¹V4­»¸¾ëçYþ÷è)m endstream endobj 723 0 obj <</Filter/FlateDecode/Length 414>> stream xÚ]Mk@ïþ=¦àÇên"$Ð´¥&ält qòï«û.9TPxv>ÞqÖMó,WÍÀÜoÝU |
| --- | Minor | ¨ZÓ£uEìB·F9~Àê¦,oÕ½ã¦²ÿ,[bnå»óùýãpèTç{Ëº÷R/OÇ½/XMW8=±ÀrÏÇ@m®®c1w k~²Å¦î.ô6}ét£nlqJsR}§ÔÀ<'IL:ÕU]M¾¬HêFNìMOÂâýô$©ú¯v¹V¿¥Ýýíäîy¡J |
| --- | Minor | àÉ7 =l¡! |
| --- | Minor | ~~qØË½³D{ûÄ¶ObÏîþÍd»éÆV­ÍJN]'ÝKH¼}­rç®î endstream endobj 719 0 obj <</Subtype/Type1C/Filter/FlateDecode/Length 1151>> stream xÚ­OSWÇïkkßÃu8/â¦¯/FÕ9Ù4ÃÝ ÝT[~¨ýõxüRùQ@íëáÀ@`jÁ´b-:m¸%m²§S Kº. Ó©ìw»¯Ëöº¿aÉÍ797ß{Îçs(¤Ñ ¢t9¹ë6æ. IÍÜ¼2¯. #Ms5þ©ÚiòËHKÉóT2§gkæ!þèÏ3"~!¢Ñ\4Åå |
| --- | Minor | ×â |
| --- | Minor | å©6{PTP(òv-æ%%%.åIü:Y(Úe´òF±Ðl1J°ßbÛUd+øEo¢}uBBYYY¼ÑRo Ö. ^Êüfs±Y(5ø4Uä³3aHªÍb/Íi3+Bv	2¨V #² rSbÐLô"bQ ÊB[Q QHÞA¡ìÔªV]ÑO¾Oã<9¬Xdñ¶Ë> z2Çµ]àu8@¨äÈ8£+p8¼Ð¥Çcd\[	ÏÞ..ZÆ¥)Uº6¯LªåÏðö.`Ä ¤KXÜsS.GY#lð÷¿ÀWð5w]õÞë<ÂÞµÝÙ |
| --- | Minor | )°2`á¾-mEjÕn`=Á}ß«1ÁúKÏX ÀhÜk}Ì³Fz7TÅqy&m¨yFF& ¤æÑqÐÙ¯¤¹`t/HÝÁ·ÿ®ÏáMl¾Vªt¦¨©?¸*!´xÖã³§î]?ãã÷_Û!Óî»lå«¹vxOÿ¸·*°;94zá0¼¹Zë?Hy+8%Öét»a/#oÐþÇcr®ÒjVË£x Wm5ùíÙöX¾¬ðW'rVÖÓð¨i`àË£ð[éD8Ú¯ÿ^%/dÉ?¤V²:ØêÇqêú¸><q^-ÛðûpihÞ'Ó%Ú9}¢×ÇÁñºcmýÝÐÌíq­ÞAo¥Gº¸q¼Í. âà¾ÁOz/´æôçiþ&õ¡ülÚ	;L&¸ÜÎ­d_Û¿ç½ÜþAF®ÞÅY-LôÓÊX´ Ï+ÊQObÿØt~1ïfÅ |
| --- | Minor | °ek±q?Ði&úë·éIç4ÎD·6Ülº|ù«]ù*æKz¼ÆªÉ£·ºó29"üÆè©ÙÊ)qûëãáÁPó)¤«Ü;]{ ²êâLôQ©­ªa_]u÷¶ÜØ×:ÛÝÐ2§û£#\.Ò¤âò¬Æ÷s8!yíx6ÛZßà	\Ëjjö|s[YÉÎ¦@×M©7ÂPÕPßpìhç¿ït_ß½%±åÑ!ÆYë¬PûÇÛÎ»:#þ­ ÝÏDöÈ©ÝØÖÞÖ£%Æ:8=ü\ U§Ó=ÏM×$ztQòYÿ~18æ endstream endobj 721 0 obj <</Subtype/Type1C/Filter/FlateDecode/Length 300>> stream xÚcd`aa`ddäðvöñÓvöu° 	È|)aãú9õÃYÆrL?ä³È200|ïøAä+) g¦¤ë9çTe¦g(h$k*ZZë(X*8æ¦e&'æ)ø&d¤æ& 99 ÁùÉ©% 6%%Vúúåååz¹ÅzùEév: å% A©Å©Ee©) nùy% ~¹© `×ëIçüÜÒÔ"ßüÔ¢< ãD;##ú¾~\ðþcË÷Ìßwÿ¬ý}è·ÑÌüï¿ó~ßòwærV¾\7¸w®âá¹1W¥2óûC j¤b9 endstream endobj 722 0 obj <</Filter/FlateDecode/Length 529>> stream xÚ]]k£@@ßýóØe)QGgÔD´»Km_öÍè$+4*Æ<äß¯Î¹¤P!3_÷Ì»ÈöÛ}ÛjñgèªÂêØ´õà.Ýu¨:¸SÓQ¬ê¦üu.û`½ý¯òìÔ"ÛäÅß/¯oÝ¹loîtý. Ç÷<2ªvG¿ßz§báý¶¸]FwÞ·ÇN­VRiZszØÔÝÁýÛ~µö¤>²Â·×¾ÿtg×*Ök¿\]ÕÕîÒÊöäU8}kµÊ§o¸¶þÖo. ÓÇê_9ÌÃ£çix&ÑÚSæÉ@qL_iú6ôiU«è |
| --- | Minor | ´õ45zÚ1/ræA:¢/n® ÃHYF =1Ræ-! Ök!1b%!{ØBâ¹ÄS(Øû´?òÂÚak#$O<È§ÙAXk¢§ÂLs)LCO+gÌnS<cY³x)ùÙCgJC. 7Äàr'.VHNU.s0¸hNÓ;2¸¤¦ÁÅ á¢%9ÓâBÎ. wÂ'¬xÝ§d¼X\. y±¸XNÚÊ=#v#7ò~+íö«Eæï¾Zü©Gþ-Æa@ä÷åZúg-ïw~àsaº×¥ê:SðÕË ¹V4­»¸¾ëçYþ÷è)m endstream endobj 723 0 obj <</Filter/FlateDecode/Length 414>> stream xÚ]Mk@ïþ=¦àÇên"$Ð´¥&ält qòï«û.9TPxv>ÞqÖMó. WÍÀÜoÝU |
| --- | Minor | ¨ZÓ£uEìB·F9~Àê¦. oÕ½ã¦²ÿ. [bnå»óùýãpèTç{Ëº÷R/OÇ½/XMW8=±ÀrÏÇ@m®®c1w k~²Å¦î.ô6}ét£nlqJsR}§ÔÀ<'IL:ÕU]M¾¬HêFNìMOÂâýô$©ú¯v¹V¿¥Ýýíäîy¡J |
| --- | Minor | àÉ7 =l¡!. |
| --- | Minor | Sentence exceeds complexity threshold, split for readability. Applying the split needs --strength moderate or higher. |
| --- | Minor | none (split proposal only; source not rewritten) |
| --- | Minor | none |
| --- | Minor | Check: NEEDS-LLM |
| --- | Minor | Flags:    not-assessed |
| --- | Minor | SENTENCE (Line 1413, 741 words, 13 clauses)  [Script] |
| --- | Minor | "²ðHÂ&@+Ø¬çd³X=	² ÈzdõÖ Ú  RÍiã2Ð´:²D>l{8æ¤B,IÌL NbfqMã1IT@O`xÚ,è[ô 1A"d¶(H[Ô¥íóPè]Úÿà²»2/Ó|	^w µVÒÜ³ìó^6^©ïú9Ê¼©«Úf endstream endobj 724 0 obj <</Filter/FlateDecode/Length 250>> stream xÚ]PËjÃ0¼ë+öRÐ1Ó& |
| --- | Minor | ²´v± Ð`§4KRJ¸WôÜ²¨8q{æ=BT~_õùýçt5=×Û+vãÓö~+=Hlòm²é«C= |
| --- | Minor | ûJ·²D³L |
| --- | Minor | &Ø|IÓàýDRºÍ½¨Ã¤­}bÚAÌò<¬KwÂH,H\wÈ²x®²r®¡ÿþÓEÕ´âÁÉ³ÓrfÇñ~{´Kô´+Ëoñé_áÅH4{	' )½!¥ñuEk¬Wþ/ûu endstream endobj 725 0 obj <</Filter/FlateDecode/Length 245>> stream xÚ]P±jÃ0Ýõ7¦b[1¤ ¦Ò::ÊÒÙÔåÁ_K6:èxwz÷xï2ÆÏÜè Ù§·²Á 6Êãh'/Zìµ!¥eØºTå ÉØE¸1 d'þÆ®ïÏìÒ|^î·º8ÂneÜf@·y8pÓY(K}-cð3ìNÊ¶øgW¯ÐkÓÃîÎ4i&ç~q@ 'UäÕ´ G' eWPÖuEÐ¨ûu£íäðÒVÞ¯ø¸àãkÄ9ÍÆÆj1ö#µ¼_ü¤Û¤¤Ñ6ø8³.n¥÷q endstream endobj 727 0 obj <</Subtype/Type1C/Filter/FlateDecode/Length 714>> stream xÚOLÓpÇ[6°ÂB [!!1Ðh0þ	( (b41ËhØ±±u«ûÃý+Û¯£Ð± |
| --- | Minor | `ÓþF,FãÕ3=x0í\÷IÞË÷½|ÉåÃå]îv?ê¹ÜÝ×ÿüÚÉàù¯§¶¸=-k!±UE¢Z&^«zåÇ¢:å¡£s'üsþ |
| --- | Minor | ©ëåVRK P¾ÃÈ|$AîF¥ø³0÷÷#}ðE¼ZÍ9r-ÀÛ¾u|¤7dð-¦v±-`	¸gÝa£2ñ¯ôjüØA>[æ½¦iû ãOhsü)å¢p"ê¢í6,Ú ¢'GSã»ê4xÇ¬3Yc£a+iÙ<÷AÂ¾ð*ê¡üs`D]FÐö@ÌûÃ÷! ¯!JÛzþÎFI¡>yFU*K4+Î2RJQ+ÍåÒ TåÂAÕ=v/¯ endstream endobj 728 0 obj <</Filter/FlateDecode/Length 346>> stream xÚ]Mn0÷>©ª¿	!(*UÓF!9 !E*Æ2dÛ×ã¡YtþlÞ<½ñàde^Ê~æÎAM3ïzÙjÆn_àÚKæù¼íyÙÙw3Ô9Ù¾Võ ÜI?Þ÷Ãs¶?n_Î§Ây	NwÜ_öe^Ý§Rv#cÆ¹s4~Ó¬ï|¶ãðìK· {yå«sVÙê¦Ô gî²$±v%jÆ&U7 ky»nÂã¢HÈöß7oC%®ù®µnÔ |
| --- | Minor | ±"»©)}{îÅðx¼#ÞrËfañÚ³lba9 ±@#dòè)ÈS §xEö3Ìg!iBÔD3ÂéóÌ6¾tèÿõ»ÜMwPGMrL¸¦h©Äx}8æÇÖf ö_°£Å)ô¿VÙç­z¥= endstream endobj 730 0 obj <</Subtype/Type1C/Filter/FlateDecode/Length 3596>> stream xÚW{TSWÖ¿1{ÄÖôè´÷¢Vk«Ú*Úú,ã³UÅ(BÞ"(obMxä)!@ [¬Ï*R[ujëXflíègWU´UºÜ7ÆõØµæûþø¾5ëd³ÏÞûüö>û·#cgd2ûâ/]0ÕUà\çzÖvRüÜâÈs^g¤7d0LåÒáo0lé«ÎEgæÖ+ÎyFåf\d²áné¾¾ïzûúÎôOHÜ¼#:&ÕkJÄÛ^3æÎõæ5Ó×w®×â¸Èäáñ^«ÂSc"ãÂSéBåµ.!bGdê.¯)óbRSß÷ñIOO÷KñNH^ðö4¯ô©1^)ÉiÛ½&Ä§z­ôrºííüâÕ©É^«¶G&ÇS?GsÌ)²©ïùÌbÆØZfÄldB­²p&Ñ0YTl/Ã`\wæUf4£d^cxznãÉeÆ13yÄLff2ï1³9Ì<f=÷!³ÙÌd3^Ã3ibÊFËâeÇÍ¶gØ#¹Q~kxË8UìWÜ`ÃØ~n>×1"ÂÕÓµÀm[¨Ûn7³û÷Ç#»GJÎÃö§V|a}bõ=Ä7Ñÿ¡\òñ]%UwvEn:DDL÷7UØ;%ÙQâzÌÏxkL·zãLn=µ7ÛWU):ïÁ#÷ ÓýM{,ë»·ªKìeÑ¯ å÷á!<&»ä½*ÎohOdÕ«Ï2ðèô7èVËÝ,âïç^ßä åëÍyHû¤ÞNÙß þjÌ¦ºOc	ÿÌÆaQ£¼¿Ï.W¯AkÔ ¾ÜÃÈë@DBÈ$òg½nï^Ðr:cþ>¡ n_=²¿6?tç<G|,x¦Ï6È$¹cîâk,`iÔ@¦Hc·¢Ìê4HÛ#nÒÍî¡_Õf¨® i¤Â5vSö©­ÑVÙ[XsK.Åá÷<\ÖÝùû¶{×ÂX²mjìRíû°Vßéw|öÇà¯Ðoûì.×~¹ìïp#*rÿ |
| --- | Minor | [ÐßÂU½ |
| --- | Minor | ¿\ªïÃp1Ýì]¹æÃÇ° ür¸4¢XÎ¨]ê²Ë0ýûJÞj0&«>òp*Ö_ÃÙn¨Òe{;âPñ/ðé§·áÐË¤ðÖÑ¤p*¹Oí²ÓO0ö®\úð }V~@VfaÞRH,U<¼spÂ×g`p,²Ó®Qïë»¹G[ÑØ^w¨=­Q%hA{ |
| --- | Minor | »tà,pÓ0iÁä#ìzHå U^ÃER0gNm.î¯Wº¿¹v!h KÖlHå¬ü©æïOÁOÜ½é½3&Ì]ä#@dMtsü~MÙÞ/£8å/ï¬¹Üø§Ëizsþ ¿->\S_mâ&ñ8z~ÓîS±°zì¼Bæ½÷á\=õÕC¸Óu÷¦UïÁÊ»£|&Âoy5KtD(¤Â¦¤\¢\ß]G¸] |
| --- | Minor | ]q+ÎÝFOLÏ±¸3°¼)Ê»SáÙ÷päL}Gø¿ðéØÃ÷t²n?Ý]}ÖÖ¥%¹5Q%«!ûpçÄé­¨ìÁY=²>Ç"¹cÍ3­jØ-=SìV:­ªEé9	ãk¡Ñ¢=âÐEV:­P+z8*é ±KËd@¹4Ýñ¯­ÖgB&è3IìÐÏì©1´h.¦Ðw6ÎÑçÅeØÁÆRcéqä=±JqL-É-ÒvlÜ:HTìçÅ_À±Ïá=Á®\Gü0'9 tÅë.[ÕvÇtÊ«¶U. |
| --- | Minor | "²ðHÂ&@+Ø¬çd³X=	² ÈzdõÖ Ú  RÍiã2Ð´:²D>l{8æ¤B. IÌL NbfqMã1IT@O`xÚ. è[ô 1A"d¶(H[Ô¥íóPè]Úÿà²»2/Ó|	^w µVÒÜ³ìó^6^©ïú9Ê¼©«Úf endstream endobj 724 0 obj <</Filter/FlateDecode/Length 250>> stream xÚ]PËjÃ0¼ë+öRÐ1Ó& |
| --- | Minor | ²´v± Ð`§4KRJ¸WôÜ²¨8q{æ=BT~_õùýçt5=×Û+vãÓö~+=Hlòm²é«C= |
| --- | Minor | ûJ·²D³L |
| --- | Minor | &Ø|IÓàýDRºÍ½¨Ã¤­}bÚAÌò<¬KwÂH. H\wÈ²x®²r®¡ÿþÓEÕ´âÁÉ³ÓrfÇñ~{´Kô´+Ëoñé_áÅH4{	' )½!¥ñuEk¬Wþ/ûu endstream endobj 725 0 obj <</Filter/FlateDecode/Length 245>> stream xÚ]P±jÃ0Ýõ7¦b[1¤ ¦Ò::ÊÒÙÔåÁ_K6:èxwz÷xï2ÆÏÜè Ù§·²Á 6Êãh'/Zìµ!¥eØºTå ÉØE¸1 d'þÆ®ïÏìÒ|^î·º8ÂneÜf@·y8pÓY(K}-cð3ìNÊ¶øgW¯ÐkÓÃîÎ4i&ç~q@ 'UäÕ´ G' eWPÖuEÐ¨ûu£íäðÒVÞ¯ø¸àãkÄ9ÍÆÆj1ö#µ¼_ü¤Û¤¤Ñ6ø8³.n¥÷q endstream endobj 727 0 obj <</Subtype/Type1C/Filter/FlateDecode/Length 714>> stream xÚOLÓpÇ[6°ÂB [!!1Ðh0þ	( (b41ËhØ±±u«ûÃý+Û¯£Ð± |
| --- | Minor | `ÓþF. FãÕ3=x0í\÷IÞË÷½|ÉåÃå]îv?ê¹ÜÝ×ÿüÚÉàù¯§¶¸=-k!±UE¢Z&^«zåÇ¢:å¡£s'üsþ |
| --- | Minor | ©ëåVRK P¾ÃÈ|$AîF¥ø³0÷÷#}ðE¼ZÍ9r-ÀÛ¾u|¤7dð-¦v±-`	¸gÝa£2ñ¯ôjüØA>[æ½¦iû ãOhsü)å¢p"ê¢í6. Ú ¢'GSã»ê4xÇ¬3Yc£a+iÙ<÷AÂ¾ð*ê¡üs`D]FÐö@ÌûÃ÷! ¯!JÛzþÎFI¡>yFU*K4+Î2RJQ+ÍåÒ TåÂAÕ=v/¯ endstream endobj 728 0 obj <</Filter/FlateDecode/Length 346>> stream xÚ]Mn0÷>©ª¿	!(*UÓF!9 !E*Æ2dÛ×ã¡YtþlÞ<½ñàde^Ê~æÎAM3ïzÙjÆn_àÚKæù¼íyÙÙw3Ô9Ù¾Võ ÜI?Þ÷Ãs¶?n_Î§Ây	NwÜ_öe^Ý§Rv#cÆ¹s4~Ó¬ï|¶ãðìK· {yå«sVÙê¦Ô gî²$±v%jÆ&U7 ky»nÂã¢HÈöß7oC%®ù®µnÔ |
| --- | Minor | ±"»©)}{îÅðx¼#ÞrËfañÚ³lba9 ±@#dòè)ÈS §xEö3Ìg!iBÔD3ÂéóÌ6¾tèÿõ»ÜMwPGMrL¸¦h©Äx}8æÇÖf ö_°£Å)ô¿VÙç­z¥= endstream endobj 730 0 obj <</Subtype/Type1C/Filter/FlateDecode/Length 3596>> stream xÚW{TSWÖ¿1{ÄÖôè´÷¢Vk«Ú*Úú. ã³UÅ(BÞ"(obMxä)!@ [¬Ï*R[ujëXflíègWU´UºÜ7ÆõØµæûþø¾5ëd³ÏÞûüö>û·#cgd2ûâ/]0ÕUà\çzÖvRüÜâÈs^g¤7d0LåÒáo0lé«ÎEgæÖ+ÎyFåf\d²áné¾¾ïzûúÎôOHÜ¼#:&ÕkJÄÛ^3æÎõæ5Ó×w®×â¸Èäáñ^«ÂSc"ãÂSéBåµ.!bGdê.¯)óbRSß÷ñIOO÷KñNH^ðö4¯ô©1^)ÉiÛ½&Ä§z­ôrºííüâÕ©É^«¶G&ÇS?GsÌ)²©ïùÌbÆØZfÄldB­²p&Ñ0YTl/Ã`\wæUf4£d^cxznãÉeÆ13yÄLff2ï1³9Ì<f=÷!³ÙÌd3^Ã3ibÊFËâeÇÍ¶gØ#¹Q~kxË8UìWÜ`ÃØ~n>×1"ÂÕÓµÀm[¨Ûn7³û÷Ç#»GJÎÃö§V|a}bõ=Ä7Ñÿ¡\òñ]%UwvEn:DDL÷7UØ;%ÙQâzÌÏxkL·zãLn=µ7ÛWU):ïÁ#÷ ÓýM{. ë»·ªKìeÑ¯ å÷á!<&»ä½*ÎohOdÕ«Ï2ðèô7èVËÝ. âïç^ßä åëÍyHû¤ÞNÙß þjÌ¦ºOc	ÿÌÆaQ£¼¿Ï.W¯AkÔ ¾ÜÃÈë@DBÈ$òg½nï^Ðr:cþ>¡ n_=²¿6?tç<G|. x¦Ï6È$¹cîâk. `iÔ@¦Hc·¢Ìê4HÛ#nÒÍî¡_Õf¨® i¤Â5vSö©­ÑVÙ[XsK.Åá÷<\ÖÝùû¶{×ÂX²mjìRíû°Vßéw|öÇà¯Ðoûì.×~¹ìïp#*rÿ |
| --- | Minor | [ÐßÂU½ |
| --- | Minor | ¿\ªïÃp1Ýì]¹æÃÇ° ür¸4¢XÎ¨]ê²Ë0ýûJÞj0&«>òp*Ö_ÃÙn¨Òe{;âPñ/ðé§·áÐË¤ðÖÑ¤p*¹Oí²ÓO0ö®\úð }V~@VfaÞRH. U<¼spÂ×g`p. ²Ó®Qïë»¹G[ÑØ^w¨=­Q%hA{ |
| --- | Minor | »tà. pÓ0iÁä#ìzHå U^ÃER0gNm.î¯Wº¿¹v!h KÖlHå¬ü©æïOÁOÜ½é½3&Ì]ä#@dMtsü~MÙÞ/£8å/ï¬¹Üø§Ëizsþ ¿->\S_mâ&ñ8z~ÓîS±°zì¼Bæ½÷á\=õÕC¸Óu÷¦UïÁÊ»£|&Âoy5KtD(¤Â¦¤\¢\ß]G¸] |
| --- | Minor | ]q+ÎÝFOLÏ±¸3°¼)Ê»SáÙ÷päL}Gø¿ðéØÃ÷t²n?Ý]}ÖÖ¥%¹5Q%«!ûpçÄé­¨ìÁY=²>Ç"¹cÍ3­jØ-=SìV:­ªEé9	ãk¡Ñ¢=âÐEV:­P+z8*é ±KËd@¹4Ýñ¯­ÖgB&è3IìÐÏì©1´h.¦Ðw6ÎÑçÅeØÁÆRcéqä=±JqL-É-ÒvlÜ:HTìçÅ_À±Ïá=Á®\Gü0'9 tÅë.[ÕvÇtÊ«¶U.. |
| --- | Minor | Sentence exceeds complexity threshold, split for readability. Applying the split needs --strength moderate or higher. |
| --- | Minor | none (split proposal only; source not rewritten) |
| --- | Minor | none |
| --- | Minor | Check: NEEDS-LLM |
| --- | Minor | Flags:    not-assessed |
| --- | Minor | SENTENCE (Line 1413, 949 words, 16 clauses)  [Script] |
| --- | Minor | dâäOÒû{)^Bó û J5K´a}bV¶êmÁó/ã8ú-¨xq6M²að |
| --- | Minor | ]­ÕælUÞµb/mUÚLü³£8 p.aÄg5tø?²lC_ ïj¡MõSjß îÇ®ª,± ö´ùï-+Ì HëI=Çðjþ®Å²qXâí'OPIÏñ³Ö¦R[	\pôö­"¤TjÎ2ññ»w&Ñs?«kolïÏ%¼z=}[i øR/áOä.Íæ?hHºG¹Ëg/Ý/¦ÖL.ÖiiR&Ï ZÐËñ4 ²³ví«Þ¹1£aã©éµ~¾D<¤Tûù¶z-º%ü¤©ÐÜQdè nYð"_añ@>Î5ÔBYp{ ?] àÛÇ;¤ßm	Î*ZG¥ÙAIÉ#¼þöì·ÖN\.x<ÿTmq·ËÌÏrG²<#eJt&(kïVª$T·B×À*§Ó`ÖWfTd5,§bÐåôdüÐ<Oâ'í¦OÂÅÿç©>Ê Õ>4äYº§´° Ê¡ÜXfÆùR'.*.Ë0ÔÀØ*(-+­Á |
| --- | Minor | [­ç8;«ÒÅ*6¡h­SÏECS¤V¿W_ÀyàaRÜó|rÝ{äXKù)Ï'?ì!^ìfÿ×îHº;î>ßM&=|1yJ¥NËõ^º¡Mû+y"?×§¡ûïè6¹ÞâB%r¬émm»×Ió!øAÿU2 ®Æ*N}Õ[¿}@2Ù­9°ÊãFsÑÕ3ÎÊº"¸ý v×³ð3Øvv¥5GTmOØ}>â| ÁÓ¶rÊdRý¶¢ X$ |
| --- | Minor | ¿a©û¥ç²©RN>5_PEt¸_^nïèhþÚòx]"ÄGîgÈkõÕù´ÍÌËÑ~4ÏsþÃ ½Lc¡ª²ªÉ)©O2êa»Sú;0ê<&¼§:iÃ uòæ5ú4gSÜFù¥íÀÃ§3ÉÅºý°¡¦¶¾ÙÞÒnmÿq²§YM;¥BÈÉÍJqÒgÆæ¢ct;D@¨m/ÿ]±XOÉná='¡ÍàS5*P¦Bµ?ËZQ I ¨Ïðlmm2Û¡Ìyöê¦¬fèsÃÙóºQòßñe òIkwíw³¹»÷×¹\û5¸Àû¯ý7À endstream endobj 731 0 obj <</Filter/FlateDecode/Length 381>> stream xÚ]Mo0ïü;Má+¬B*¡HºU£v¥`:¤¢@ý÷ãª æÍk[¶/ë²VãÊü£»V6ª7°Ì7Ó»ÀuT^²~ìÖÇ{wS«=_ZýÑNÀüªøÞÇWy8ÔÛ·ó© ëa Åé®ïºlîË S­eÇÿe |
| --- | Minor | ÕÜÙf×ÏxÁØ§éÁêÊ6gÙ¸HsÓú&P+ã^;»JêæÝv`Zu/ã<gYUå¨þß¿(¤+¡ûiVÊ£"È-Äåä8EwÈ	qÈ;Ç=òè§|G&½DÿÈéy¸G.%rIlÉbÛÃrB >ÆbÒÇXC¼'FÏÄÕÏ¬'	CËâã""Æ:EJý-ñr	Ì%(À\r	Ìº¹=,þ)ù¤èR¿öÀ=&£Âz®Tw3ÆÛ-[#ø¨à¹zÖxË=¼D· endstream endobj 733 0 obj <</Subtype/Type1C/Filter/FlateDecode/Length 4563>> stream xÚµX	tTe®G%ñaSJé¦^DM´­((e©@6RI*ªTe«}}·ö}I¥ªÊFBa5Y"b¢èQÛìÅ§ÕÓçñe¦ç¯Óvvfzæô99/'¯òÞ¿{¿ûÝïÁIKã1ùÙ§w<³úù«rrÖ-OÝx¼µ72ªMgæryóàf>&øt}Ú3'ÌæpûôÔ5gjêJMÃWÎ<|¹çÝ»8S	"ãÎ©wÍMÍ÷PöÒæöA¡H\,,	k¤BüS*"aYþ~a¹LR\QURT&WK/Zôhö¢EKVUk \©©wpàÌå,ädsá,á<Êy³³³³³³³³ËÙÅ¹wà¤qâDqc»;ö³´¾ôÉé¯gdX2.ÞÁ½ÃNê&vO:x§(sáäß²lÊS§­¾ù®{îúônûõ<.c2:Wdæ%ÁwÑ+orRñÐüÅ~ÎþÍ ØûïsÍ^nwvòl÷pÔ¯3¥ÚdÖªË+ëk,1 `óúãm=­C#¯´O)Pubé#y'©^±ö _(ì{Á¦¯.·>y®@bwg«as9icEqfä:ÁÌA|ùíú·Ê~uàZ^û6 Ù»W±ó¨ý`§<`·Ù=]¿ým¤H´ÔÉ¾øL |
| --- | Minor | ÊGÅ÷ÔC}Hà/4¾Úú÷Y×«ýü&ZÓØ6°n£C'°Li~Õöê<£F#ZÏßÆ £UÉ@r$F¼v¶{Îâ¢_3×x1E3Äl{º[ì/Qõ J1@GÁ |
| --- | Minor | N/¸I§É£Q@¾Z :¨öÉÙékØ{Ù5À®<w,·§ ]û¯¢ëúU°¬¨.: Ø	­Ûà4[M@F½êtÑK§^»@ÁIq÷F½mW¤Â»>þLP: Q&ZñõE²=À¹ÂvpÒM&­YmÚ£±Ú1øR9d³é*ÔÁóÉëâÛÙ»®®Úp6¿{'¡ZÔ ®-nØ&Rë6»~°9±¦÷ã}ìÒz ªu"C¥¾R³×¤ÚÇ.ãë«ð1fRé­KBöºv§Ëk¾Á÷lzÛê±¹§z{:Úú#1q`[-¸426}ìE¾©?m kª&A¸;ìï |
| --- | Minor | }p@zËý[.2ye°FP ºr&{,O-üÔÎôÐJOwÝgîQ(Üb^³Ê¢µ(AC>Dø Z£ÉþÐ8H§Ù­¨Áb4Ö(wHÖæYnnMPt·Íæ¶1G¶Æj]jGo«=Ü=Ö{¬§³¹79¯=YëW´u':[Ð/ÈM¹» ß%ï­Ç¾TÆG³c3å]`ç÷³i^e¬Ò@6g¸­N;¦Ób39TAcÐÐÈ0oð¥¯®s©UöÓÆ@E¸ð¶Ïö°IFy<«:ª		!v8ðAv3S8Ky&³ôZA-,ÓÉ,:ZIC-©ôCä ÊþêÊ:ùNø fïxÖE g÷°sØL¿Ùù6k³án»÷Ã:F äómt³É7 6o¸¬«ä,nÍ)è4ÍýÃ¦«K©%.egh&Ï[UûWò÷Ð)´ñ÷¡f O´ _ à´wUUþîü=Ïþs]"~:1;t^°z[e  XU»%ÙÅìô¹×ÿö4-¤à5ña³d«YÄ+ÜÿìÃèYôÀé²§(¨í~î@ÞÒÝøå£KXa=êc"ßdîø=1>É»-a´ÑTÇ.û÷ø«¼{ºá |
| --- | Minor | Û;O¡iî½&òtaOî}ìÕíÎ±ºÁøÛ§s(åHõÕ:Y.;ÝPXu:ÍÔîasø4h XíÎDè\ø\ð|/|ÿ¦i|9ú³·µ|³Ð¡T¥¨÷êÜ6·*AXñÄÚu?¾Î\ ÿQ¶<6^B^":ØA.jÓò¼´@P6ZòÑÞORl6¬eåyì9M9gà:´5#bäª×écWëÒ'ÙyÙ\ Ï»!ç°AGÖDÔa |
| --- | Minor | ?é¿æ=K^åÙC®C¶÷Dð3¿:tìXÏy Ï)ÈaÓØ{Øì"JjÐXÉ)¨øq¸hÇY^4)I%ååÍü9»5VâÿAë\´>Â°ü©ÕÐXôn£Ëÿë÷ÐÄK²c{Kä±ÊC¬xN\áìñï^çû¸Ì¶Ñ\+4®ëAW-h ¶°úõ|C¦RéÓú>ð8Ü1¶Ïáà(qÜà¢¥ïò´EíJ j¨Qú J¡è ÚÍ^&aPì5*ü±â¢±4ZÜXlÁ§¡üÄÂóöÚì¸î(=ãÛ6³< 6KØýòÁÝ[mb'àÙÄdÕXÍV,v,³Q¢¨û® /x_g\«P 3Wê,Ú{Õ8[Üð0*äßîyÁ©ÃjF ùã"å/\¾tmq\!·-5çe éíe+(Ë°zézïø{lQL~H ÁX ã6ìïq%RHf¬5ì¬±þßfIfDS´±ÛmV«+hûmï­xt@Óji¿]A?ü÷Aw+ÿLYÊC/¡îKý­]³ÜV¿"X©=ZÎ`ÞTTX9Ç ÆCÑP:²Ae2Ñ´Ùb6YpÍaø ·¼ývÏ{0+â¨WïÐQ ¨²È¡JqeV¹µÒªÀc¶áGKÉþd¬÷Õj¤µÉÚiMµBÊ>tâ@Zé& ÝA5PM êl2;íÀÃã=4àQ}Í`»Jô³Ê´N9¤ñb­h |
| --- | Minor | ? |
| --- | Minor | dâäOÒû{)^Bó û J5K´a}bV¶êmÁó/ã8ú-¨xq6M²að |
| --- | Minor | ]­ÕælUÞµb/mUÚLü³£8 p.aÄg5tø?²lC_ ïj¡MõSjß îÇ®ª. ± ö´ùï-+Ì HëI=Çðjþ®Å²qXâí'OPIÏñ³Ö¦R[	\pôö­"¤TjÎ2ññ»w&Ñs?«kolïÏ%¼z=}[i øR/áOä.Íæ?hHºG¹Ëg/Ý/¦ÖL.ÖiiR&Ï ZÐËñ4 ²³ví«Þ¹1£aã©éµ~¾D<¤Tûù¶z-º%ü¤©ÐÜQdè nYð"_añ@>Î5ÔBYp{ ?] àÛÇ;¤ßm	Î*ZG¥ÙAIÉ#¼þöì·ÖN\.x<ÿTmq·ËÌÏrG²<#eJt&(kïVª$T·B×À*§Ó`ÖWfTd5. §bÐåôdüÐ<Oâ'í¦OÂÅÿç©>Ê Õ>4äYº§´° Ê¡ÜXfÆùR'.*.Ë0ÔÀØ*(-+­Á |
| --- | Minor | [­ç8;«ÒÅ*6¡h­SÏECS¤V¿W_ÀyàaRÜó|rÝ{äXKù)Ï'?ì!^ìfÿ×îHº;î>ßM&=|1yJ¥NËõ^º¡Mû+y"?×§¡ûïè6¹ÞâB%r¬émm»×Ió!øAÿU2 ®Æ*N}Õ[¿}@2Ù­9°ÊãFsÑÕ3ÎÊº"¸ý v×³ð3Øvv¥5GTmOØ}>â| ÁÓ¶rÊdRý¶¢ X$ |
| --- | Minor | ¿a©û¥ç²©RN>5_PEt¸_^nïèhþÚòx]"ÄGîgÈkõÕù´ÍÌËÑ~4ÏsþÃ ½Lc¡ª²ªÉ)©O2êa»Sú;0ê<&¼§:iÃ uòæ5ú4gSÜFù¥íÀÃ§3ÉÅºý°¡¦¶¾ÙÞÒnmÿq²§YM;¥BÈÉÍJqÒgÆæ¢ct;D@¨m/ÿ]±XOÉná='¡ÍàS5*P¦Bµ?ËZQ I ¨Ïðlmm2Û¡Ìyöê¦¬fèsÃÙóºQòßñe òIkwíw³¹»÷×¹\û5¸Àû¯ý7À endstream endobj 731 0 obj <</Filter/FlateDecode/Length 381>> stream xÚ]Mo0ïü;Má+¬B*¡HºU£v¥`:¤¢@ý÷ãª æÍk[¶/ë²VãÊü£»V6ª7°Ì7Ó»ÀuT^²~ìÖÇ{wS«=_ZýÑNÀüªøÞÇWy8ÔÛ·ó© ëa Åé®ïºlîË S­eÇÿe |
| --- | Minor | ÕÜÙf×ÏxÁØ§éÁêÊ6gÙ¸HsÓú&P+ã^;»JêæÝv`Zu/ã<gYUå¨þß¿(¤+¡ûiVÊ£"È-Äåä8EwÈ	qÈ;Ç=òè§|G&½DÿÈéy¸G.%rIlÉbÛÃrB >ÆbÒÇXC¼'FÏÄÕÏ¬'	CËâã""Æ:EJý-ñr	Ì%(À\r	Ìº¹=. þ)ù¤èR¿öÀ=&£Âz®Tw3ÆÛ-[#ø¨à¹zÖxË=¼D· endstream endobj 733 0 obj <</Subtype/Type1C/Filter/FlateDecode/Length 4563>> stream xÚµX	tTe®G%ñaSJé¦^DM´­((e©@6RI*ªTe«}}·ö}I¥ªÊFBa5Y"b¢èQÛìÅ§ÕÓçñe¦ç¯Óvvfzæô99/'¯òÞ¿{¿ûÝïÁIKã1ùÙ§w<³úù«rrÖ-OÝx¼µ72ªMgæryóàf>&øt}Ú3'ÌæpûôÔ5gjêJMÃWÎ<|¹çÝ»8S	"ãÎ©wÍMÍ÷PöÒæöA¡H\. 	k¤BüS*"aYþ~a¹LR\QURT&WK/Zôhö¢EKVUk \©©wpàÌå. ädsá. á<Êy³³³³³³³³ËÙÅ¹wà¤qâDqc»;ö³´¾ôÉé¯gdX2.ÞÁ½ÃNê&vO:x§(sáäß²lÊS§­¾ù®{îúônûõ<.c2:Wdæ%ÁwÑ+orRñÐüÅ~ÎþÍ ØûïsÍ^nwvòl÷pÔ¯3¥ÚdÖªË+ëk. 1 `óúãm=­C#¯´O)Pubé#y'©^±ö _(ì{Á¦¯.·>y®@bwg«as9icEqfä:ÁÌA|ùíú·Ê~uàZ^û6 Ù»W±ó¨ý`§<`·Ù=]¿ým¤H´ÔÉ¾øL |
| --- | Minor | ÊGÅ÷ÔC}Hà/4¾Úú÷Y×«ýü&ZÓØ6°n£C'°Li~Õöê<£F#ZÏßÆ £UÉ@r$F¼v¶{Îâ¢_3×x1E3Äl{º[ì/Qõ J1@GÁ |
| --- | Minor | N/¸I§É£Q@¾Z :¨öÉÙékØ{Ù5À®<w. ·§ ]û¯¢ëúU°¬¨.: Ø	­Ûà4[M@F½êtÑK§^»@ÁIq÷F½mW¤Â»>þLP: Q&ZñõE²=À¹ÂvpÒM&­YmÚ£±Ú1øR9d³é*ÔÁóÉëâÛÙ»®®Úp6¿{'¡ZÔ ®-nØ&Rë6»~°9±¦÷ã}ìÒz ªu"C¥¾R³×¤ÚÇ.ãë«ð1fRé­KBöºv§Ëk¾Á÷lzÛê±¹§z{:Úú#1q`[-¸426}ìE¾©?m kª&A¸;ìï |
| --- | Minor | }p@zËý[.2ye°FP ºr&{. O-üÔÎôÐJOwÝgîQ(Üb^³Ê¢µ(AC>Dø Z£ÉþÐ8H§Ù­¨Áb4Ö(wHÖæYnnMPt·Íæ¶1G¶Æj]jGo«=Ü=Ö{¬§³¹79¯=YëW´u':[Ð/ÈM¹» ß%ï­Ç¾TÆG³c3å]`ç÷³i^e¬Ò@6g¸­N;¦Ób39TAcÐÐÈ0oð¥¯®s©UöÓÆ@E¸ð¶Ïö°IFy<«:ª		!v8ðAv3S8Ky&³ôZA-. ÓÉ. :ZIC-©ôCä ÊþêÊ:ùNø fïxÖE g÷°sØL¿Ùù6k³án»÷Ã:F äómt³É7 6o¸¬«ä. nÍ)è4ÍýÃ¦«K©%.egh&Ï[UûWò÷Ð)´ñ÷¡f O´ _ à´wUUþîü=Ïþs]"~:1;t^°z[e  XU»%ÙÅìô¹×ÿö4-¤à5ña³d«YÄ+ÜÿìÃèYôÀé²§(¨í~î@ÞÒÝøå£KXa=êc"ßdîø=1>É»-a´ÑTÇ.û÷ø«¼{ºá |
| --- | Minor | Û;O¡iî½&òtaOî}ìÕíÎ±ºÁøÛ§s(åHõÕ:Y.;ÝPXu:ÍÔîasø4h XíÎDè\ø\ð|/|ÿ¦i|9ú³·µ|³Ð¡T¥¨÷êÜ6·*AXñÄÚu?¾Î\ ÿQ¶<6^B^":ØA.jÓò¼´@P6ZòÑÞORl6¬eåyì9M9gà:´5#bäª×écWëÒ'ÙyÙ\ Ï»!ç°AGÖDÔa |
| --- | Minor | ?é¿æ=K^åÙC®C¶÷Dð3¿:tìXÏy Ï)ÈaÓØ{Øì"JjÐXÉ)¨øq¸hÇY^4)I%ååÍü9»5VâÿAë\´>Â°ü©ÕÐXôn£Ëÿë÷ÐÄK²c{Kä±ÊC¬xN\áìñï^çû¸Ì¶Ñ\+4®ëAW-h ¶°úõ|C¦RéÓú>ð8Ü1¶Ïáà(qÜà¢¥ïò´EíJ j¨Qú J¡è ÚÍ^&aPì5*ü±â¢±4ZÜXlÁ§¡üÄÂóöÚì¸î(=ãÛ6³< 6KØýòÁÝ[mb'àÙÄdÕXÍV. v. ³Q¢¨û® /x_g\«P 3Wê. Ú{Õ8[Üð0*äßîyÁ©ÃjF ùã"å/\¾tmq\!·-5çe éíe+(Ë°zézïø{lQL~H ÁX ã6ìïq%RHf¬5ì¬±þßfIfDS´±ÛmV«+hûmï­xt@Óji¿]A?ü÷Aw+ÿLYÊC/¡îKý­]³ÜV¿"X©=ZÎ`ÞTTX9Ç ÆCÑP:²Ae2Ñ´Ùb6YpÍaø ·¼ývÏ{0+â¨WïÐQ ¨²È¡JqeV¹µÒªÀc¶áGKÉþd¬÷Õj¤µÉÚiMµBÊ>tâ@Zé& ÝA5PM êl2;íÀÃã=4àQ}Í`»Jô³Ê´N9¤ñb­h |
| --- | Minor | ?. |
| --- | Minor | Sentence exceeds complexity threshold, split for readability. Applying the split needs --strength moderate or higher. |
| --- | Minor | none (split proposal only; source not rewritten) |
| --- | Minor | none |
| --- | Minor | Check: NEEDS-LLM |
| --- | Minor | Flags:    not-assessed |
| --- | Minor | SENTENCE (Line 1413, 653 words, 11 clauses)  [Script] |
| --- | Minor | ¸5ÖØîÌûO[Òqe£A¨bk­£¶òôV¢¾[Ã|ÃóöÙ½ïBÄâ73C&P)ÆÒÇ®ð1#¦V*`;ûU}»¯Éâ4æ6¾»Ç\|åö ù:3in k1ðÀøÖÈ8¾ ¾ÍÞ7võVþf¥ÂÐºMüþÃÖ5lMb÷d:',¿ëïæÏkóØÜ&n·iyç;ÒÔýt¬)¦Q2xÁ,Ã¢j*kTÛê4¥ªc¡úé-Ö£¹h6ml3­a"Ú&Ú*ÅÙõ=ácú Å+ÞÇWåJ¤ÏIòÿLÅÇ¾v×Y->«ÃÑ±Û¾z»MJ2Évâå/'ÉÌþË,ÊçYÔÐ *rgÍûèÎ!´&ì2ºRýcÑõÒ5%°ê;4×Pùï>G;Í&Ñ{QuR¶­eì2>-#ÞF<ëmåí®=Ãh)â ÞW?>÷)_}ð4EÁ¼\<W.ÐU?]xîXfl |
| --- | Minor | =öÏ^aC>Ê8Ò×7pì¢uëKÔÑ¨,õi(RÝúÕñ/¹ÌtfçJÚ}Q»×Ú |
| --- | Minor | ßG`.õ+·ì­ªÛYêûH\ÏC?íùø]øüláevüï :c	¹õó ëE{ó+q¹µCî@w´ê9Ñ7 äð/ô`WLpÏcÔùCãìw\f.s¯,oÕb½'·zöûýnÞÕD}ümÐ¥÷èF,ÚZõ¦§É·ÿÕvÖÜ{æÌkÐGM-"|ïEhmùi¸þ©cfß2éµP­2VÈúK?ìdv*¶Y_\÷uÝÊëÖêjê¢Çæ¦tØ*q7y'µ¡jiiM~î9ÕLÛë×#I)ÚÉ3ÕÐ:ÅÍBc¯9uÃ-(­óBëÉc'¼Üø¤öºFl3¾¯âÝ )hñ$<MÑS`&ÎûÚÝQ¼,yÉó{Úö=´½OýCww­è¾¥[IM¥Vºû9½ÂP5d^OáÐúÑý>Á¦Wdø³Hb«~úÚßqÑÀèeØàQÜ¢¡ÕmØMã÷¾±·n­Jf².¨ ºñªäDùW |
| --- | Minor | 0ëqç4úÙu\­VÍe@ Þ|ºí	ogS"ÞÕ54ttpß âÁ»Ç¤.RªM6wEuWuç	6Bn®pï®¼ªªÂ:<fßjÑ9}W¹h3ZÌûÑÅO |
| --- | Minor | \é~)ËÓÀømóØ)jJdÂóÜz¤ìøÑ}þÔQòsa6ÂúèÂØ|­DlhàOpîÖ¢»¶¯®h>ZÂ?kéÅñç[Ù`Òÿçlü?ýAØmÑÂ[@V^ç`§óôåí^ ÕX´M6­´¥»¬Íjl¤3ï@cjÞàµyàöâmÎÝæô¡ù|_u{>^ÐD4ÝúzÃÈJªv7®©?·»±ä½®·èÈ×E<g7g¸íÐñþã@lÊË£`O;M´­d°ëãúº÷ÝøpÓêÄP^úpÿ²'46@%òâº^Q÷¿òA8èë)`³ùÊ´yM¦üÚ¸HÀy{ºñ["tn§Ü .GÔ øÛUµÿæñhQúUçë\fx<«ÓæÔFdx*Ôèt Ú¤É7Èv²y|]9Ö>-m>¾ Èx­ãÁÓ(ÍÓ ÙJ¯ÂÛI((¨5Õh«òØiJ!ì"YîMuà4ô´F£Êê=ûwíÛ'~	;É¾vrØ}Ì¨ÉªJ»·(zúñYc¨¯¡Ë×D}Â'_yy°÷úkÍ`èÃ÷Û¾ÿ0õQ§÷`ñWú¥­U­ %Oä="1Ût~ÊvÕÞtê"x Zô	Ý²`Qñ»6lÝ¹WT&îß³ËÞiòðÊêpºô9üØêÍ.ä7#hFWo×ã |
| --- | Minor | ¢·ÄO­VWäÎ2ÜUå®ÆXc1ÑäYYå÷ûQE"úïLJ{,9Ñ9ÉyçÁI×ïLº23Ñ§3þÍ{WÄ endstream endobj 734 0 obj <</Filter/FlateDecode/Length 262>> stream xÚ]Mk0ïùsÜR,JAW<ì¶Ô]Øí-&£ |
| --- | Minor | (ÏT_è|ß/÷úôZÛÇûÛíZG	pì·ë¢â=oªv,ìd¾Ö5 ®:|qµÃÑ9ÀáV¶¾ÒÎZÿâÒBHòÜ¶â8iÊÐP9 ÉÂ0¬®sÿûK6E×³jöÎ8âdÑÑsr\9IVÃôä8Ý¸r\l\®îÚÂïÙ'ºÎ§3l6f½ÙûçÝpOµÒNåßÝ*y endstream endobj 736 0 obj <</Subtype/Type1C/Filter/FlateDecode/Length 884>> stream xÚEmh[UÆÏm²äØ¥Ñél7]\Icje:\]ÃNiD¶¬dé]Ò¼,¹iL6Û¼¿ýÓ¼47iÚ¦MbkÙ¤Û8gÁ@e 8Ù'¿õúÁ}R¸7½±zS?ÃáùÿßÃ!Tè29}fðø!ÃÙþöÃöáRsyñ &S_'âhG£DÉ;¤HÊD7qø­ã}>¡lÞæ| |
| --- | Minor | «)4û8jyê5/ø5­MßSXÖ&A×à^­ñßVÿµäÿP±ÙRÊ¸ddb0m=ÖÔD¢â¦KQ6Î/¬ª"Y¼_Ó@9 |
| --- | Minor | ×¹y5¿ØUUªP«{àJ;î<SU¨h|QÈ¬ñ>ã/¬Ü¥$Üþ ¾O7®U+×¾ÊÒ.`Ôv X°`Ãßs<H Y(é¦'?ùMd=1/RÞÄÜKr¸ )6xß¸aXâðü_âÿÌ«ÿ1qjUúúÕþÌ±élòx>'2çnï&Yq× |
| --- | Minor | _Àæ®¿; <é@1Óüýüì33#rcAL´1*6'î_ðÂGX8)÷°yý¶Ë£@*ÀÓE'Ãã»é±»%djÛ*Áu5$ÜkÍQUªSøØGîôÊýà­ÕaeT6ß®mP%5ïHøçÿúE%âDãéA2¾x\ÆãÁñL%Å>¹zÍ¥w¾õ¶ºàÏÍøÛÇÔ|¶ ÞýýDâ! |
| --- | Minor | ¸5ÖØîÌûO[Òqe£A¨bk­£¶òôV¢¾[Ã|ÃóöÙ½ïBÄâ73C&P)ÆÒÇ®ð1#¦V*`;ûU}»¯Éâ4æ6¾»Ç\|åö ù:3in k1ðÀøÖÈ8¾ ¾ÍÞ7võVþf¥ÂÐºMüþÃÖ5lMb÷d:'. ¿ëïæÏkóØÜ&n·iyç;ÒÔýt¬)¦Q2xÁ. Ã¢j*kTÛê4¥ªc¡úé-Ö£¹h6ml3­a"Ú&Ú*ÅÙõ=ácú Å+ÞÇWåJ¤ÏIòÿLÅÇ¾v×Y->«ÃÑ±Û¾z»MJ2Évâå/'ÉÌþË. ÊçYÔÐ *rgÍûèÎ!´&ì2ºRýcÑõÒ5%°ê;4×Pùï>G;Í&Ñ{QuR¶­eì2>-#ÞF<ëmåí®=Ãh)â ÞW?>÷)_}ð4EÁ¼\<W.ÐU?]xîXfl |
| --- | Minor | =öÏ^aC>Ê8Ò×7pì¢uëKÔÑ¨. õi(RÝúÕñ/¹ÌtfçJÚ}Q»×Ú |
| --- | Minor | ßG`.õ+·ì­ªÛYêûH\ÏC?íùø]øüláevüï :c	¹õó ëE{ó+q¹µCî@w´ê9Ñ7 äð/ô`WLpÏcÔùCãìw\f.s¯. oÕb½'·zöûýnÞÕD}ümÐ¥÷èF. ÚZõ¦§É·ÿÕvÖÜ{æÌkÐGM-"|ïEhmùi¸þ©cfß2éµP­2VÈúK?ìdv*¶Y_\÷uÝÊëÖêjê¢Çæ¦tØ*q7y'µ¡jiiM~î9ÕLÛë×#I)ÚÉ3ÕÐ:ÅÍBc¯9uÃ-(­óBëÉc'¼Üø¤öºFl3¾¯âÝ )hñ$<MÑS`&ÎûÚÝQ¼. yÉó{Úö=´½OýCww­è¾¥[IM¥Vºû9½ÂP5d^OáÐúÑý>Á¦Wdø³Hb«~úÚßqÑÀèeØàQÜ¢¡ÕmØMã÷¾±·n­Jf².¨ ºñªäDùW |
| --- | Minor | 0ëqç4úÙu\­VÍe@ Þ|ºí	ogS"ÞÕ54ttpß âÁ»Ç¤.RªM6wEuWuç	6Bn®pï®¼ªªÂ:<fßjÑ9}W¹h3ZÌûÑÅO |
| --- | Minor | \é~)ËÓÀømóØ)jJdÂóÜz¤ìøÑ}þÔQòsa6ÂúèÂØ|­DlhàOpîÖ¢»¶¯®h>ZÂ?kéÅñç[Ù`Òÿçlü?ýAØmÑÂ[@V^ç`§óôåí^ ÕX´M6­´¥»¬Íjl¤3ï@cjÞàµyàöâmÎÝæô¡ù|_u{>^ÐD4ÝúzÃÈJªv7®©?·»±ä½®·èÈ×E<g7g¸íÐñþã@lÊË£`O;M´­d°ëãúº÷ÝøpÓêÄP^úpÿ²'46@%òâº^Q÷¿òA8èë)`³ùÊ´yM¦üÚ¸HÀy{ºñ["tn§Ü .GÔ øÛUµÿæñhQúUçë\fx<«ÓæÔFdx*Ôèt Ú¤É7Èv²y|]9Ö>-m>¾ Èx­ãÁÓ(ÍÓ ÙJ¯ÂÛI((¨5Õh«òØiJ!ì"YîMuà4ô´F£Êê=ûwíÛ'~	;É¾vrØ}Ì¨ÉªJ»·(zúñYc¨¯¡Ë×D}Â'_yy°÷úkÍ`èÃ÷Û¾ÿ0õQ§÷`ñWú¥­U­ %Oä="1Ût~ÊvÕÞtê"x Zô	Ý²`Qñ»6lÝ¹WT&îß³ËÞiòðÊêpºô9üØêÍ.ä7#hFWo×ã |
| --- | Minor | ¢·ÄO­VWäÎ2ÜUå®ÆXc1ÑäYYå÷ûQE"úïLJ{. 9Ñ9ÉyçÁI×ïLº23Ñ§3þÍ{WÄ endstream endobj 734 0 obj <</Filter/FlateDecode/Length 262>> stream xÚ]Mk0ïùsÜR. JAW<ì¶Ô]Øí-&£ |
| --- | Minor | (ÏT_è|ß/÷úôZÛÇûÛíZG	pì·ë¢â=oªv. ìd¾Ö5 ®:|qµÃÑ9ÀáV¶¾ÒÎZÿâÒBHòÜ¶â8iÊÐP9 ÉÂ0¬®sÿûK6E×³jöÎ8âdÑÑsr\9IVÃôä8Ý¸r\l\®îÚÂïÙ'ºÎ§3l6f½ÙûçÝpOµÒNåßÝ*y endstream endobj 736 0 obj <</Subtype/Type1C/Filter/FlateDecode/Length 884>> stream xÚEmh[UÆÏm²äØ¥Ñél7]\Icje:\]ÃNiD¶¬dé]Ò¼. ¹iL6Û¼¿ýÓ¼47iÚ¦MbkÙ¤Û8gÁ@e 8Ù'¿õúÁ}R¸7½±zS?ÃáùÿßÃ!Tè29}fðø!ÃÙþöÃöáRsyñ &S_'âhG£DÉ;¤HÊD7qø­ã}>¡lÞæ| |
| --- | Minor | «)4û8jyê5/ø5­MßSXÖ&A×à^­ñßVÿµäÿP±ÙRÊ¸ddb0m=ÖÔD¢â¦KQ6Î/¬ª"Y¼_Ó@9 |
| --- | Minor | ×¹y5¿ØUUªP«{àJ;î<SU¨h|QÈ¬ñ>ã/¬Ü¥$Üþ ¾O7®U+×¾ÊÒ.`Ôv X°`Ãßs<H Y(é¦'?ùMd=1/RÞÄÜKr¸ )6xß¸aXâðü_âÿÌ«ÿ1qjUúúÕþÌ±élòx>'2çnï&Yq× |
| --- | Minor | _Àæ®¿; <é@1Óüýüì33#rcAL´1*6'î_ðÂGX8)÷°yý¶Ë£@*ÀÓE'Ãã»é±»%djÛ*Áu5$ÜkÍQUªSøØGîôÊýà­ÕaeT6ß®mP%5ïHøçÿúE%âDãéA2¾x\ÆãÁñL%Å>¹zÍ¥w¾õ¶ºàÏÍøÛÇÔ|¶ ÞýýDâ!. |
| --- | Minor | Sentence exceeds complexity threshold, split for readability. Applying the split needs --strength moderate or higher. |
| --- | Minor | none (split proposal only; source not rewritten) |
| --- | Minor | none |
| --- | Minor | Check: NEEDS-LLM |
| --- | Minor | Flags:    not-assessed |
| --- | Minor | SENTENCE (Line 1413, 715 words, 9 clauses)  [Script] |
| --- | Minor | VºWÇê2á`INvJûª'æiÅÞFgco£¢P§ÛÚÿû~t endstream endobj 737 0 obj <</Filter/FlateDecode/Length 234>> stream xÚ]PÁjÃ0½û+tìÃN	¬)SÚ¥»:¶Û8Î!¿Ø |
| --- | Minor | =ì`=½'éVb/¬@ÏÁ©#tÆê£Bh±7[ÐFÅ5ËQ |
| --- | Minor | Z¥?Éîâtþ~®»÷ë¥.Þ@cwg\f°]s±oæ1â lçs@¿c3l>´kñ)aAc0¶Íµj2ÒLÞßp@²ÌíûJÊi½T¤ípÆJàu]´ú_mU´úð×ba2¶|»¢Iì=Ü©)en¾Av3yç*¿?_m endstream endobj 739 0 obj <</Subtype/Type1C/Filter/FlateDecode/Length 351>> stream xÚcd`aa`ddäuòöôÓvöu°	þîaYý³õ4ÃÆ²L?ä°È200¼OùAäC©$­X9J« |
| --- | Minor | õó*2Ó3J45--Íu,sS2ó|K2RsKàüäÌÔJ |
| --- | Minor | +}ýòòr½ÄÜb½ü¢t;MòÌ ÔâÔ¢²Ô·ü¼¿ÄÜT°£õÀ¤s~nAiIjo~JjQÐQ@ç	1012²øþèàûñ¸{Ï¦=Ûç3~oûÎÇüá'³èÂîiyrõÝÝM-vA ÝåÝåQóÙwì;<ãÏ´ßÊQìû¾óvïØõ«{Êßªì|õÓLù?êt¶ß±Ø÷p}çäÞ<ç;çr^9.óù<=<|?äD Vtý endstream endobj 741 0 obj <</Subtype/Type1C/Filter/FlateDecode/Length 527>> stream xÚU?lQÇïqG 6RAxÝh¤ôÚFIñ_ÄÒÅ¸4<ábáðzbCk)Ï'`LÚÈà¢K]¤QíD4&]Ý4wÍsð`sù|ßß7ùýò p ¡KXüÂåS±øÙ+áÞ"¤z~«óÃY÷rºèÐ¤òúqá ­$g(NEq*¦ËýúÓcp2à(a4T9-`\Òr(/iYsJZFZúOç4­831Q*R~1¨¨ÙÈX d-h©K(Ï) |
| --- | Minor | &¤<ýbÁ>cJ¾xSC*+¤ &¤Ù U9 AÞÿ¥Wúu[i{ÊS@'»¼ñ°4pß¿úöâwDáÒ×[?uºw@Ã(_¯:©[Í5o Í¦ï¿'k]~úûÎEèü]fQ:^~É]b¹CV±T	n¬wfß^²väI07aofØÆ³{WÉÕw|Ø¯Õ¨º÷hÐÅ¡Ö;íÁºþ§¯o»Øk6½uîP'ÝaÎ­gfÇî`×¶ûÂnï¶ìCÞA¡¬Ø­ôàØ?í¢ÙC endstream endobj 742 0 obj <</Filter/FlateDecode/Length 266>> stream xÚ]Mk0ïþ9n)íºDhµt·-«Û{LFXãÁß$Ê:gòÎoXÔe-¸ð[KÚ ¦q³¦\qS³¿éHTg¢>É¶ú§mO§óED¼ìkCnî¯m§À°_µí¢ë²Y&c-z	Y Ûz2zÝ+>¸Üf¨¹`w-if¥n8¢0yîÛÅërT2¡¨0È"9d<@ÁþýÖª®§¿D;õÓUGQzÌ=+½{:Ä+UÒÈÓ1ñdOG?eëçæ9î.ÑYk»µ÷ÒûáVçïv+©\?²ø}r endstream endobj 744 0 obj <</Subtype/CIDFontType0C/Filter/FlateDecode/Length 3247>> stream xÚ}WXWÚ&Ñ2n3t&ZëV¤¶ºµõõR¯XD-ØªÜA! M·ê²´«² |
| --- | Minor | oU§çf&é}oÖ ¡Â(XBà AH¦ûÚ[4[ü'÷Íñuü9èi"ÀÓD(1x !%Á_ý§±èT]²z}ªZkÌ0î_ùü*]ö~}FºÆ¨ZùÜ_»TõrjCRÊ>]¾a_*IªÚ¡Ú¡Ñå½ªgtZU²Z¦Ò¥©¶©ãU¹µÞ J×ër³ |
| --- | Minor | "TÛ4U¾N¿O%>õêLuAªÊÕ¦ªõ*£F­ze{Ü6ÕZÖ¨Ú¢ÖÔªðpÊ V«4FcösÓ#túôiâ7úÆ¯Ý³-|ÓúUkbâÖDª4^ª6&ed"~âÿèÑé³2	ñb&xOEÄoDñ2±ØHl&b­Ä6"H$TBCd{,"[*R,^¡D¨l¢ ÉÛ~Kýº¤r©UúÿARN>E&ÊÂd©Ôêï±º)Où"06ðÂÔ¹Sû~Ô'åcÞðJèÕx÷SËê»Ê8\4&#[Ì¶Laµ¥¤Ã9ãw/²=IÙõ9ú°^*ÞØÑ^®CÜBÂQÙNºJPµU©C9l&å<ua0Ø*9|LÊ1XÎÃ'ùØ#>á©¸rWo	£WÉÃÊZS<i{ñø³¦ì»7U?¡§n»ùØJòTÃÚS¯¬C{,¤È<qd]~cE©KGX=õÈIö­¶µsxìPà-²ÏÁBÊÇî<0Å#°¾V2Âuz®ÅKÇÁg 0âhWã8/Æ	8ÂQ ¹õ áHØÞÆöºz¥Û ÙrYQ5²Z¸Â4L¼ç0â5ð*<#Þ«áYX§cã3¥Ï¯OC¿oäÀLµÙìF6Mv55®s;ýç/À3ð/ÿ¡ã'¸øú¹¿eî´Ý «£ÈVZÀÆ¥Åç§0Qëï 	þ¾û~ß¯æsµ@)ëÌõ{%#ÿÜâvA±Â¥ÌÆâ§+ð°?ó~õ"7!éÌõo¾#Ú¸bÝÚÈFÎcQGÐASU*­`_[Aöì¹$®'/ÃÏã=8Q\Çó°?PÊÉÿ.æ/ä¼T8 |
| --- | Minor | õÿ69Ë¼xËoÖ	:ÐÃÂöÁw_ÃôQÎì°[ÜL#rå`9uÕYlÕelj<éÉÛÙÅà0¬ÀSñ¼ Ä'AÈßüù#þw¼ÊK`Êu¸ò±T¸µ `çÀt<Å=zÙ°ËÌË¨äJË:V=Ìzð tá£ái¯ã&&'Í7¨[ò×q<¼®­+Íf×ÀRÙÄäeô:4XÒÀñ²XNÇþTú=RaE&¹pR´¬õý&,Ãþ[~æ]ú`/#×þt$R'L÷¥ ýUTºÀÁ²aêVCÞúI,ëMyÑì:X5åøuïÃþnKE1+y8ÏÂÀè®zµp6(xªzo-IEN |
| --- | Minor | §o¥>¨1¥pY=hD#[aÖ21xÎIÈýÖyþæyþç/úµ?mgçáÃñ<xË!²÷ëÒY®¸þxfSê9 ©³5µYQD&ð æ%>&ÐÈÌPaXuµý £ú]µÃ,OaÂ	'©§&HÁKp,ùåwÿ |
| --- | Minor | VºWÇê2á`INvJûª'æiÅÞFgco£¢P§ÛÚÿû~t endstream endobj 737 0 obj <</Filter/FlateDecode/Length 234>> stream xÚ]PÁjÃ0½û+tìÃN	¬)SÚ¥»:¶Û8Î!¿Ø |
| --- | Minor | =ì`=½'éVb/¬@ÏÁ©#tÆê£Bh±7[ÐFÅ5ËQ |
| --- | Minor | Z¥?Éîâtþ~®»÷ë¥.Þ@cwg\f°]s±oæ1â lçs@¿c3l>´kñ)aAc0¶Íµj2ÒLÞßp@²ÌíûJÊi½T¤ípÆJàu]´ú_mU´úð×ba2¶|»¢Iì=Ü©)en¾Av3yç*¿?_m endstream endobj 739 0 obj <</Subtype/Type1C/Filter/FlateDecode/Length 351>> stream xÚcd`aa`ddäuòöôÓvöu°	þîaYý³õ4ÃÆ²L?ä°È200¼OùAäC©$­X9J« |
| --- | Minor | õó*2Ó3J45--Íu. sS2ó|K2RsKàüäÌÔJ |
| --- | Minor | +}ýòòr½ÄÜb½ü¢t;MòÌ ÔâÔ¢²Ô·ü¼¿ÄÜT°£õÀ¤s~nAiIjo~JjQÐQ@ç	1012²øþèàûñ¸{Ï¦=Ûç3~oûÎÇüá'³èÂîiyrõÝÝM-vA ÝåÝåQóÙwì;<ãÏ´ßÊQìû¾óvïØõ«{Êßªì|õÓLù?êt¶ß±Ø÷p}çäÞ<ç;çr^9.óù<=<|?äD Vtý endstream endobj 741 0 obj <</Subtype/Type1C/Filter/FlateDecode/Length 527>> stream xÚU?lQÇïqG 6RAxÝh¤ôÚFIñ_ÄÒÅ¸4<ábáðzbCk)Ï'`LÚÈà¢K]¤QíD4&]Ý4wÍsð`sù|ßß7ùýò p ¡KXüÂåS±øÙ+áÞ"¤z~«óÃY÷rºèÐ¤òúqá ­$g(NEq*¦ËýúÓcp2à(a4T9-`\Òr(/iYsJZFZúOç4­831Q*R~1¨¨ÙÈX d-h©K(Ï) |
| --- | Minor | &¤<ýbÁ>cJ¾xSC*+¤ &¤Ù U9 AÞÿ¥Wúu[i{ÊS@'»¼ñ°4pß¿úöâwDáÒ×[?uºw@Ã(_¯:©[Í5o Í¦ï¿'k]~úûÎEèü]fQ:^~É]b¹CV±T	n¬wfß^²väI07aofØÆ³{WÉÕw|Ø¯Õ¨º÷hÐÅ¡Ö;íÁºþ§¯o»Øk6½uîP'ÝaÎ­gfÇî`×¶ûÂnï¶ìCÞA¡¬Ø­ôàØ?í¢ÙC endstream endobj 742 0 obj <</Filter/FlateDecode/Length 266>> stream xÚ]Mk0ïþ9n)íºDhµt·-«Û{LFXãÁß$Ê:gòÎoXÔe-¸ð[KÚ ¦q³¦\qS³¿éHTg¢>É¶ú§mO§óED¼ìkCnî¯m§À°_µí¢ë²Y&c-z	Y Ûz2zÝ+>¸Üf¨¹`w-if¥n8¢0yîÛÅërT2¡¨0È"9d<@ÁþýÖª®§¿D;õÓUGQzÌ=+½{:Ä+UÒÈÓ1ñdOG?eëçæ9î.ÑYk»µ÷ÒûáVçïv+©\?²ø}r endstream endobj 744 0 obj <</Subtype/CIDFontType0C/Filter/FlateDecode/Length 3247>> stream xÚ}WXWÚ&Ñ2n3t&ZëV¤¶ºµõõR¯XD-ØªÜA! M·ê²´«² |
| --- | Minor | oU§çf&é}oÖ ¡Â(XBà AH¦ûÚ[4[ü'÷Íñuü9èi"ÀÓD(1x !%Á_ý§±èT]²z}ªZkÌ0î_ùü*]ö~}FºÆ¨ZùÜ_»TõrjCRÊ>]¾a_*IªÚ¡Ú¡Ñå½ªgtZU²Z¦Ò¥©¶©ãU¹µÞ J×ër³ |
| --- | Minor | "TÛ4U¾N¿O%>õêLuAªÊÕ¦ªõ*£F­ze{Ü6ÕZÖ¨Ú¢ÖÔªðpÊ V«4FcösÓ#túôiâ7úÆ¯Ý³-|ÓúUkbâÖDª4^ª6&ed"~âÿèÑé³2	ñb&xOEÄoDñ2±ØHl&b­Ä6"H$TBCd{. "[*R. ^¡D¨l¢ ÉÛ~Kýº¤r©UúÿARN>E&ÊÂd©Ôêï±º)Où"06ðÂÔ¹Sû~Ô'åcÞðJèÕx÷SËê»Ê8\4&#[Ì¶Laµ¥¤Ã9ãw/²=IÙõ9ú°^*ÞØÑ^®CÜBÂQÙNºJPµU©C9l&å<ua0Ø*9|LÊ1XÎÃ'ùØ#>á©¸rWo	£WÉÃÊZS<i{ñø³¦ì»7U?¡§n»ùØJòTÃÚS¯¬C{. ¤È<qd]~cE©KGX=õÈIö­¶µsxìPà-²ÏÁBÊÇî<0Å#°¾V2Âuz®ÅKÇÁg 0âhWã8/Æ	8ÂQ ¹õ áHØÞÆöºz¥Û ÙrYQ5²Z¸Â4L¼ç0â5ð*<#Þ«áYX§cã3¥Ï¯OC¿oäÀLµÙìF6Mv55®s;ýç/À3ð/ÿ¡ã'¸øú¹¿eî´Ý «£ÈVZÀÆ¥Åç§0Qëï 	þ¾û~ß¯æsµ@)ëÌõ{%#ÿÜâvA±Â¥ÌÆâ§+ð°?ó~õ"7!éÌõo¾#Ú¸bÝÚÈFÎcQGÐASU*­`_[Aöì¹$®'/ÃÏã=8Q\Çó°?PÊÉÿ.æ/ä¼T8 |
| --- | Minor | õÿ69Ë¼xËoÖ	:ÐÃÂöÁw_ÃôQÎì°[ÜL#rå`9uÕYlÕelj<éÉÛÙÅà0¬ÀSñ¼ Ä'AÈßüù#þw¼ÊK`Êu¸ò±T¸µ `çÀt<Å=zÙ°ËÌË¨äJË:V=Ìzð tá£ái¯ã&&'Í7¨[ò×q<¼®­+Íf×ÀRÙÄäeô:4XÒÀñ²XNÇþTú=RaE&¹pR´¬õý&. Ãþ[~æ]ú`/#×þt$R'L÷¥ ýUTºÀÁ²aêVCÞúI. ëMyÑì:X5åøuïÃþnKE1+y8ÏÂÀè®zµp6(xªzo-IEN |
| --- | Minor | §o¥>¨1¥pY=hD#[aÖ21xÎIÈýÖyþæyþç/úµ?mgçáÃñ<xË!²÷ëÒY®¸þxfSê9 ©³5µYQD&ð æ%>&ÐÈÌPaXuµý £ú]µÃ. OaÂ	'©§&HÁKp. ùåwÿ. |
| --- | Minor | Sentence exceeds complexity threshold, split for readability. Applying the split needs --strength moderate or higher. |
| --- | Minor | none (split proposal only; source not rewritten) |
| --- | Minor | none |
| --- | Minor | Check: NEEDS-LLM |
| --- | Minor | Flags:    not-assessed |
| --- | Minor | SENTENCE (Line 1736, 515 words, 6 clauses)  [Script] |
| --- | Minor | '>Â&æP7þè(HrØrUÒ'¤p¶(®â±Ä RÅÈ£F¤pXD²ºÒ5À	þÔËõ5+ö÷Yû«2÷§++Wûf;åcwW×5&éÒyaÑ=¸¼õ:Öâ¥viÑP:Íð	ÄBÔé°?AÏôR´Ê³e3ôÌô­ÈÁeRgl®Ür%=¿¼ÒTXÄâQü	7©SÛl»11DÔ¯ò¹/³ºí0¥sãíTzµikÑ¦LröÞu¶yY{9¯ZQÝph A;p;Y[á.2)µjT Ê6ý²³×'Ü´I>V:ÁCðï¾Ö} |
| --- | Minor | ¿F6öêÏÜ§QF+*¨àðÊñD	_*Êcð4½rÒUSô1#Ú±J¤hÔIÒ®æs¶j£¸{z«(»¶'å5®r7ãvÕ××p°UH·ÛÈñÈüõì=Um;ÉM××F±ÃyX(Ãy±¤×í²;ô¢SGÐ#/Pø¸  Ë«Q|¸Ú»¹ìÿßQîR_Gê¨iBrÂã½º |
| --- | Minor | w¥>Eÿ Aæ6?#F (òópLÃ0W¼§A ±¢Âúm]½û]±jÈÎ¿dÞ"fÂ_ì§½×òÁ~.B¼*5õpÂUª9ìÎ¢L¿:/sã©TÆj~pö©OQ¿è»þOõ7)oê6(â%?¤V0E1²ò:¦XÜþSýiÂ,%õõw?à¤¢8ÅÔë2F+S89 GG¤ yKÑmh×j |
| --- | Minor | ­¶ÝÐÝÝÞÞ-.é+Ar&Ü0zST9á÷.ä.1ÙÊ«ØsºÍÌä76X¸Ã®k½eCQÝ7ZÞü£òÆ¢?ái,6ÿê#ç·ÿôåO(¾Ãéåå"ÃeÚ"ÝßÒW4È\k~§Ãà"µraµ2Þáv»XçÁNÔÂÜºkULí.æm<øñ°ÀÓÈÉ;<ÁCCP8¤¢9³ï¦ö#6íL¡sIkKSgq$´=®<×w~è<e_ |
| --- | Minor | KÃ÷Õ.ô{U´å±eEUÓê]Èõ¯,;±÷P)w<«µê~ÞïKÜÕmy´'ÊUÕ½Gº}mÎöÞDvw¯õ¼­3 ÎVa·2%È¼££	ÌP´(DîZ»ÝÓÌ].»¹¦66Eåt_4þùòÛKº`ËFoÈÀ®ûR¡uìW \/K®BÎtîµÛÚ íÅÉ$/sq7Õ¸ÞGÍäÈÆ,ÂÛÎR¡ÝçÎ¡A7{äW>`a6Äõ |
| --- | Minor | WÀ^	<¸íÍÒ±!^¬_¹ä¿à\qrXÖÔÚÏ2G»QµóXQ©Q)·³ÙL³ÿ!:Çû²ösÞjöD°·SmèÇÉ:ÜÝè(Çrð²&ßñ¹a·û-ðúìlsä"ÜWû f©¬/÷®om)sÙDy&¨*QóÄÑû2äìÛ¨¡Oö½¬g9>ZQÕ njÀ.á9éz_&ævÁ6|ðü·=D÷éïrX©øë±ß1üÎúðmå_#¯ÌóBÜK{=ÝÞVO÷7P1;Ø5|äsþRö2´.)ËÒè«7Uì·YIi:°dÛüY£Ù¡¯{/;]ÙÅ÷*Oe·j |
| --- | Minor | ÷°´9â«¢:?~ÿ³¯}R¬ßOòpýÇrBïªõ;lF§µ;t¢àMÊ])Ç¿õô!Ïçg%ò½K"³(=Js°/Öÿ×"UpíáM;G©>{gmºó+/6@T´mËc²uvG¶h­×z0¯@i²VTX<çÃ8YÑ5ÊÎq<5ÛJæ$O~|©Ö¼·ñMdI­ÃÜÈ49jjÅ¼u¾;èh¶?!÷EgLÐ\ñDI,ö.E_74ÛPë±þÛtASPÐT>ðÞTÓn·;ì®!wP_Ûz¬ÁétÖÔ8AÓþÖºÕè endstream endobj 746 0 obj <</Filter/FlateDecode/Length 23>> stream xÚk``p0T\"Ñ°âI Fè endstream endobj 748 0 obj <</Subtype/CIDFontType0C/Filter/FlateDecode/Length 5385>> stream xÚY	XçÖÉDÅhC1£3¡n Xm­µÖw¢ÅÖ-Aö-BXEd-ù}dA¢àÒ"jk[­ÚÖê½­Z{m½tA½-Õ3ø¥ÿóþÛí_BòÍ73ç¼ç÷¼g"¢ìí)H4zíºuä¬g.ÑûÛVã	È8JàEràb'µÇKì®:Ø[wcóxÉ´ñöQâ	%m{íy^ ï¿wd[¸ç0¢Q"JJ¢äú5tÅþ¿Uþ1!1/º{zÎYªÙ£|ÑÓsöÛë<åwåjõ®0M¼6,D©ôW®vW®sW®×ÄÕ¥«&Ré¬Tj¶(cµÑZeP´&v·v»rSpV¯SÿÑájm¿26Ò? |
| --- | Minor | '>Â&æP7þè(HrØrUÒ'¤p¶(®â±Ä RÅÈ£F¤pXD²ºÒ5À	þÔËõ5+ö÷Yû«2÷§++Wûf;åcwW×5&éÒyaÑ=¸¼õ:Öâ¥viÑP:Íð	ÄBÔé°?AÏôR´Ê³e3ôÌô­ÈÁeRgl®Ür%=¿¼ÒTXÄâQü	7©SÛl»11DÔ¯ò¹/³ºí0¥sãíTzµikÑ¦LröÞu¶yY{9¯ZQÝph A;p;Y[á.2)µjT Ê6ý²³×'Ü´I>V:ÁCðï¾Ö} |
| --- | Minor | ¿F6öêÏÜ§QF+*¨àðÊñD	_*Êcð4½rÒUSô1#Ú±J¤hÔIÒ®æs¶j£¸{z«(»¶'å5®r7ãvÕ××p°UH·ÛÈñÈüõì=Um;ÉM××F±ÃyX(Ãy±¤×í²;ô¢SGÐ#/Pø¸  Ë«Q|¸Ú»¹ìÿßQîR_Gê¨iBrÂã½º |
| --- | Minor | w¥>Eÿ Aæ6?#F (òópLÃ0W¼§A ±¢Âúm]½û]±jÈÎ¿dÞ"fÂ_ì§½×òÁ~.B¼*5õpÂUª9ìÎ¢L¿:/sã©TÆj~pö©OQ¿è»þOõ7)oê6(â%?¤V0E1²ò:¦XÜþSýiÂ. %õõw?à¤¢8ÅÔë2F+S89 GG¤ yKÑmh×j |
| --- | Minor | ­¶ÝÐÝÝÞÞ-.é+Ar&Ü0zST9á÷.ä.1ÙÊ«ØsºÍÌä76X¸Ã®k½eCQÝ7ZÞü£òÆ¢?ái. 6ÿê#ç·ÿôåO(¾Ãéåå"ÃeÚ"ÝßÒW4È\k~§Ãà"µraµ2Þáv»XçÁNÔÂÜºkULí.æm<øñ°ÀÓÈÉ;<ÁCCP8¤¢9³ï¦ö#6íL¡sIkKSgq$´=®<×w~è<e_ |
| --- | Minor | KÃ÷Õ.ô{U´å±eEUÓê]Èõ¯. ;±÷P)w<«µê~ÞïKÜÕmy´'ÊUÕ½Gº}mÎöÞDvw¯õ¼­3 ÎVa·2%È¼££	ÌP´(DîZ»ÝÓÌ].»¹¦66Eåt_4þùòÛKº`ËFoÈÀ®ûR¡uìW \/K®BÎtîµÛÚ íÅÉ$/sq7Õ¸ÞGÍäÈÆ. ÂÛÎR¡ÝçÎ¡A7{äW>`a6Äõ |
| --- | Minor | WÀ^	<¸íÍÒ±!^¬_¹ä¿à\qrXÖÔÚÏ2G»QµóXQ©Q)·³ÙL³ÿ!:Çû²ösÞjöD°·SmèÇÉ:ÜÝè(Çrð²&ßñ¹a·û-ðúìlsä"ÜWû f©¬/÷®om)sÙDy&¨*QóÄÑû2äìÛ¨¡Oö½¬g9>ZQÕ njÀ.á9éz_&ævÁ6|ðü·=D÷éïrX©øë±ß1üÎúðmå_#¯ÌóBÜK{=ÝÞVO÷7P1;Ø5|äsþRö2´.)ËÒè«7Uì·YIi:°dÛüY£Ù¡¯{/;]ÙÅ÷*Oe·j |
| --- | Minor | ÷°´9â«¢:?~ÿ³¯}R¬ßOòpýÇrBïªõ;lF§µ;t¢àMÊ])Ç¿õô!Ïçg%ò½K"³(=Js°/Öÿ×"UpíáM;G©>{gmºó+/6@T´mËc²uvG¶h­×z0¯@i²VTX<çÃ8YÑ5ÊÎq<5ÛJæ$O~|©Ö¼·ñMdI­ÃÜÈ49jjÅ¼u¾;èh¶?!÷EgLÐ\ñDI. ö.E_74ÛPë±þÛtASPÐT>ðÞTÓn·;ì®!wP_Ûz¬ÁétÖÔ8AÓþÖºÕè endstream endobj 746 0 obj <</Filter/FlateDecode/Length 23>> stream xÚk``p0T\"Ñ°âI Fè endstream endobj 748 0 obj <</Subtype/CIDFontType0C/Filter/FlateDecode/Length 5385>> stream xÚY	XçÖÉDÅhC1£3¡n Xm­µÖw¢ÅÖ-Aö-BXEd-ù}dA¢àÒ"jk[­ÚÖê½­Z{m½tA½-Õ3ø¥ÿóþÛí_BòÍ73ç¼ç÷¼g"¢ìí)H4zíºuä¬g.ÑûÛVã	È8JàEràb'µÇKì®:Ø[wcóxÉ´ñöQâ	%m{íy^ ï¿wd[¸ç0¢Q"JJ¢äú5tÅþ¿Uþ1!1/º{zÎYªÙ£|ÑÓsöÛë<åwåjõ®0M¼6. D©ôW®vW®sW®×ÄÕ¥«&Ré¬Tj¶(cµÑZeP´&v·v»rSpV¯SÿÑájm¿26Ò?. |
| --- | Minor | Sentence exceeds complexity threshold, split for readability. Applying the split needs --strength moderate or higher. |
| --- | Minor | none (split proposal only; source not rewritten) |
| --- | Minor | none |
| --- | Minor | Check: NEEDS-LLM |
| --- | Minor | Flags:    not-assessed |
| --- | Minor | SENTENCE (Line 1736, 80 words, 1 clauses)  [Script] |
| --- | Minor | ¾;<dxÍð[#FÒ#Ëh/F<ê¾l¬v´htÛß1<÷Æs¥ÏÝwÌrüÙÌ´5¶Zî*oréTdE²kÈaG¼¨¿ËÉ2ÆÅý2qUîÖe%fðØ`}tq9ÑÙ(MTI?@MlãçHWÇ[èØ T¢ásÑ× |
| --- | Minor | #¹=Å3É¾^ÔÆ¶üt |
| --- | Minor | <¾ Yr,áÐ!áÔLÓîFaÉ±	ìÀDÌ)¡­V^¹µTY§pºgÉGØÅÈ«nIllnªi«Î¨ÚSÂêQ5{½#`¿Æ/âÙ;±'Hã?ùû;æÎC<³%©þÅuIj Q-}a¸|æÜÄ°·ýL§ÿ	ÔÑ8~1Ó$H»BM°¹Ë±¯JÀQ _Vf>À8æ÷¶0? |
| --- | Minor | ¾;<dxÍð[#FÒ#Ëh/F<ê¾l¬v´htÛß1<÷Æs¥ÏÝwÌrüÙÌ´5¶Zî*oréTdE²kÈaG¼¨¿ËÉ2ÆÅý2qUîÖe%fðØ`}tq9ÑÙ(MTI?@MlãçHWÇ[èØ T¢ásÑ× |
| --- | Minor | #¹=Å3É¾^ÔÆ¶üt |
| --- | Minor | <¾ Yr. áÐ!áÔLÓîFaÉ±	ìÀDÌ)¡­V^¹µTY§pºgÉGØÅÈ«nIllnªi«Î¨ÚSÂêQ5{½#`¿Æ/âÙ;±'Hã?ùû;æÎC<³%©þÅuIj Q-}a¸|æÜÄ°·ýL§ÿ	ÔÑ8~1Ó$H»BM°¹Ë±¯JÀQ _Vf>À8æ÷¶0?. |
| --- | Minor | Sentence exceeds complexity threshold, split for readability. Applying the split needs --strength moderate or higher. |
| --- | Minor | none (split proposal only; source not rewritten) |
| --- | Minor | none |
| --- | Minor | Check: NEEDS-LLM |
| --- | Minor | Flags:    not-assessed |
| --- | Minor | SENTENCE (Line 1736, 815 words, 18 clauses)  [Script] |
| --- | Minor | ÎÒxñ~±þ¨ ùóÖéÕ«+IßìºÚÎ÷äLæ±A¾mÔr[Ã·¥±+ÏÖ&óP@3Î?WefaÂÌ*^Öb°xÐÆA¼Eô¸³] ]rc¹EKÅg}VÖ/fñ~ì'ã@ìÓð4ÐÐ ¼·f¶ Ï·ÚÀVÀ;!ÀSÒôú,.!c÷J» qêç.é²^§Óó99ûöF+ÔÇö4Ô´¹éüÍØk9bÿÁ¦Â¬£ -àdÖPÀ&îÁ$;H¤òÐ£þþ¡á~~¦ð'MG;8Ümÿ5ÙÈ"ôZDädFãíúÛáâð½9ë<Õk¯J'Mà £!Çã |
| --- | Minor | <|¯oð6n{ðÊÐY,vzÁMrÿÓß|_õÛX®ön0DÛ¢êr´¹O2nµð'½.äf,¿4ÞAWÇîlòbñSfc%øèewáLµé Æ& ,øèÄ<.Ð?î\2îý;§s 	&J`vÃ<ªY×?³Ö$qß· µ^~wyb» Ll^¬ºy©hcÝ-tmºtõ¼e<üî»Zi*1êuùÜÞ´ô=q]-k[+:9×gðÜÚvXÐjú_0õÅ;u4àÌ8¦ FØ.Ù+÷ñ][÷©8F3öÔþc¨eì¨ú÷PÇ5þhõ¹Su¨4C9(-c®v'm;ÕÝ¸µäà6ÞcÌaSPÚwÒ	(õP±ÑP\È¶v~Íö ¯-EñèÀµåïðê.k¯ånª5ª10"4qÛ/çÂHQ.÷Þoa/#pHú@d'4:YÜ@ÒkqÓ |
| --- | Minor | ÚÂá^ëbÀ,"Ø4=B­ì±GH×ÈÒÙ&ÇH>#L¿½^ì¹Õ{Z4ÇÞÝø<É¿ËH)Á,L×'¶¨U~qqãHÕûùma1·éõåáÅ~æ~OBbpBUXÄ1Sµëb6*¼?^	káÕ{ço}³¡)º«ßºÍf£w"C¯*Hi«V*JÊ¸¨³	À]øû§]­)Å|Se}ÞA£4'+'{"®<áðáòê¸É·#¯9SHÍA>>¹ymçÁÞ:Z¼;sÌ²Tìt±íÊeTÁDòù§û|yY/Áêªrò68Ûõßu²¸½O,´.RØ %2Fòª'¸ ßª¿,Ûø`÷`×úéxÛøÔ	!\¢0Ò3E°pØB¯Å*éüÞÁÃ¦¼½,"ÓÃCÉØÌúþ@öÞ Ù{d°g{A |
| --- | Minor | +'j´9Üø§ã2ëXÖ#*n;øÉ{p·-³RCü<8*<ïdÁölíOASUOEÆ ^EPëÅöäz­5?FºVÞÖ, ËÿIÇÄÒ>¦Z,ëé4ó~Ýfë¥æýtÀOP#{ä­Òç·_ä!GüÂBýý·u´N¾Yüº`VY`« |
| --- | Minor | ¾>¦D¸A(=)RùäÜìÜÔr<ÂÁñ'qqiIÑ',16*²Q>ÈÃ«èÒúýÙÙ:Wã)bAE3ú?#Ç,´©iüd=]YZQV[£°§3³¨`?©MOäËÀ	õWm'¤v#)ÿÝØHHWFQ.+Y%pE	_bÉoY!¼O FÎ³Å[ÜÇ$Ôý<Í|ò×Ø~Fn×øÙ@ìàÄÐÝ¦úHV<8KGqé<Î°ÇÂqqM:ùÌârËkX½>*Ó%ÆëÙB¤u_ØòáËcèÝ:«å#óôZpÁ@Cõ©8õ@~ÚAö`~qÉû |
| --- | Minor | %ÆÆ>t=Ög#xÐ7B-'-Ñ¦ÁÄÝ9ø7f®?<¾=þç°ým+Â¸¯VT¬a§û®ÛÇëaéÄ~kÌþw©Ì\ÑsOÔÆ.øk2&ûÿ|ÜVÆÑ9#d!Üÿ¼¤IÌ¤a5¯ |
| --- | Minor | ¤IÝhD9õ|S¶A«°¾L[_´â4½!ÅQÿ_ôL´°ßú8¥Ä /cëQ~/Ü¡k |
| --- | Minor | Ãy±ê¡¬öÆß!f+õ¢?úÒuÁB¸|¾û¿ñùü+öözqÁÿÑêx±yFZü]ù5e8	sÓæã	ÿq8ß­ø¬¤#¼{VÆqMù55-ÖÝuaQ¡{v.¿°ågr!÷¯ ÃcÊGºÎuEwþîèJÝÆÔ<±/0®UÈUD6	S ¤×F¬Ç#<Ï3;áç{fÂ,{ÿ8rØ¡Xþ "S¿KdWu+×^{ªÊÂ¾×º[s?|·*Hr-WHK±Oj¸IÂ¸5±bTÕãÝùeí¼µ7bY2A½¢ |
| --- | Minor | %(»þ749P3¾Æó8ëÁÒü°+àuæ÷õÏ<vqZæbóÐ |
| --- | Minor | äþ¼6òÆoZ`28,VÇ>Ï|2o78÷o1ë½%>lwfz_Úå&:¶¡3ú&<ý ¦ÁÃ	O^ºeJU{&³ |
| --- | Minor | è®<É~|É;óR|Hßø« ]L1ÅYà	Zt*C3FpaªûÿÖ#?¸?w_>c{++<NÃ®É¸Ö³ÏìÎ¸)ØVÓóÇ/ÜÃë8«XõDÂµ³>:¿¡sFÒí-)Qµ|s]©XüºB8¦+øÜ]}-ûSér·îòMú9x>C+ÀÜÜyÞ¸¿ |
| --- | Minor | ´ |
| --- | Minor | }}?hZÞå{dëk!^j[§³6|åÏéÿ¶f\M0sÉ©{~¦= |
| --- | Minor | ¦¶1Ìc-àÛ^í¢÷ó;áÑ/ß¯{E |
| --- | Minor | pTìZs£\ÑeºÔÛ{~¾ËEúj¶åÖñàMW£½9ú´tNõ¶¸&ú­n,¸p­lÝVÌó=Ùó8¶TW'-Û×¤Ù¢PÅ½ígc¾¦ìçªô(7C91<ö&.£¢À`(*æJJÊ¤Ûß¿»Ûóê'L(aBóÇÍ¢¶ëtÝN¼ül)¾ó;¿¹Xº¦ä³¿E5`¿<ÚÈí3AqÀÜX©Cé{¹ìÔ¬i¥&0?Àn;½ cbfñY¦Ì<¶=½=Z­xÝÅmY[Ù«áeê |
| --- | Minor | {¥ |
| --- | Minor | ¢ÊCÜájqð©ó¨½ ÏÂ8^V'-¤ü|l¦¹ßY$xÚc §+ÑKÕPÄf	ª,æ}*YX%!Åí²/)Ü[ê¥é³ÞV¬ìB |
| --- | Minor | \Y%*íTÀÌr°¿|7X!.*FFð`Óyqd¿wU |
| --- | Minor | Cæ'¥ÛM<2~ |
| --- | Minor | ×HûÑó¹¶ëäÇlukNt=¤Ù­ji9l:ØùÁ®_ÀÏápùJ+ cÞç_ÇAîæO\}¾0K6¡ÛE Ý}îÒ#4*'ÓÚùpÇDN·uúa­<'¿NÄã4â-Ô_Ã$öõ<]%#DØæéÂ7·iT8+"Q~HH¶O¼ãO RaéFÀy·Ú^þºVÇÁ1dÁÀGMë]·ººæHC	ÑßÁG%.wcnÜì¼xÓ6ß±f:.x; .'ayçÂàTÐ ù;Ñ?`FîÆ?úRqkéeÌcûyÞ¯¾u2épÓñêÓuiÇ¶pæë(ýyEDdoóã£B¢tº}¼>['ÍÌAÙ=ùèwVöhâÖÈSq«rmå-EGM~±H©öx¼Ìïó¾üçc2pÀ¸ãº,¢0¼a¬ÂDÊËðÞ&ÍØ¿ íe±ÔH1Ø}u½ëGP~±ØmÍ7-{ë¶Ö6×çq§Û»ójØÎEK¼¹ÔOÅã/NKGºDÅázèYÀý­µn²µÖ¡'ö4cÂ^¿1Êzáõe7\àgøf~4z-òiýMtÇÂ^0d×JãúQÿÕA¾íg5ËÕfí	zÏJÆjk0ÒÄßY \&Û. |
| --- | Minor | ÎÒxñ~±þ¨ ùóÖéÕ«+IßìºÚÎ÷äLæ±A¾mÔr[Ã·¥±+ÏÖ&óP@3Î?WefaÂÌ*^Öb°xÐÆA¼Eô¸³] ]rc¹EKÅg}VÖ/fñ~ì'ã@ìÓð4ÐÐ ¼·f¶ Ï·ÚÀVÀ;!ÀSÒôú. .!c÷J» qêç.é²^§Óó99ûöF+ÔÇö4Ô´¹éüÍØk9bÿÁ¦Â¬£ -àdÖPÀ&îÁ$;H¤òÐ£þþ¡á~~¦ð'MG;8Ümÿ5ÙÈ"ôZDädFãíúÛáâð½9ë<Õk¯J'Mà £!Çã |
| --- | Minor | <|¯oð6n{ðÊÐY. vzÁMrÿÓß|_õÛX®ön0DÛ¢êr´¹O2nµð'½.äf. ¿4ÞAWÇîlòbñSfc%øèewáLµé Æ& . øèÄ<.Ð?î\2îý;§s 	&J`vÃ<ªY×?³Ö$qß· µ^~wyb» Ll^¬ºy©hcÝ-tmºtõ¼e<üî»Zi*1êuùÜÞ´ô=q]-k[+:9×gðÜÚvXÐjú_0õÅ;u4àÌ8¦ FØ.Ù+÷ñ][÷©8F3öÔþc¨eì¨ú÷PÇ5þhõ¹Su¨4C9(-c®v'm;ÕÝ¸µäà6ÞcÌaSPÚwÒ	(õP±ÑP\È¶v~Íö ¯-EñèÀµåïðê.k¯ånª5ª10"4qÛ/çÂHQ.÷Þoa/#pHú@d'4:YÜ@ÒkqÓ |
| --- | Minor | ÚÂá^ëbÀ. "Ø4=B­ì±GH×ÈÒÙ&ÇH>#L¿½^ì¹Õ{Z4ÇÞÝø<É¿ËH)Á. L×'¶¨U~qqãHÕûùma1·éõåáÅ~æ~OBbpBUXÄ1Sµëb6*¼?^	káÕ{ço}³¡)º«ßºÍf£w"C¯*Hi«V*JÊ¸¨³	À]øû§]­)Å|Se}ÞA£4'+'{"®<áðáòê¸É·#¯9SHÍA>>¹ymçÁÞ:Z¼;sÌ²Tìt±íÊeTÁDòù§û|yY/Áêªrò68Ûõßu²¸½O. ´.RØ %2Fòª'¸ ßª¿. Ûø`÷`×úéxÛøÔ	!\¢0Ò3E°pØB¯Å*éüÞÁÃ¦¼½. "ÓÃCÉØÌúþ@öÞ Ù{d°g{A |
| --- | Minor | +'j´9Üø§ã2ëXÖ#*n;øÉ{p·-³RCü<8*<ïdÁölíOASUOEÆ ^EPëÅöäz­5?FºVÞÖ. ËÿIÇÄÒ>¦Z. ëé4ó~Ýfë¥æýtÀOP#{ä­Òç·_ä!GüÂBýý·u´N¾Yüº`VY`« |
| --- | Minor | ¾>¦D¸A(=)RùäÜìÜÔr<ÂÁñ'qqiIÑ'. 16*²Q>ÈÃ«èÒúýÙÙ:Wã)bAE3ú?#Ç. ´©iüd=]YZQV[£°§3³¨`?©MOäËÀ	õWm'¤v#)ÿÝØHHWFQ.+Y%pE	_bÉoY!¼O FÎ³Å[ÜÇ$Ôý<Í|ò×Ø~Fn×øÙ@ìàÄÐÝ¦úHV<8KGqé<Î°ÇÂqqM:ùÌârËkX½>*Ó%ÆëÙB¤u_ØòáËcèÝ:«å#óôZpÁ@Cõ©8õ@~ÚAö`~qÉû |
| --- | Minor | %ÆÆ>t=Ög#xÐ7B-'-Ñ¦ÁÄÝ9ø7f®?<¾=þç°ým+Â¸¯VT¬a§û®ÛÇëaéÄ~kÌþw©Ì\ÑsOÔÆ.øk2&ûÿ|ÜVÆÑ9#d!Üÿ¼¤IÌ¤a5¯ |
| --- | Minor | ¤IÝhD9õ|S¶A«°¾L[_´â4½!ÅQÿ_ôL´°ßú8¥Ä /cëQ~/Ü¡k |
| --- | Minor | Ãy±ê¡¬öÆß!f+õ¢?úÒuÁB¸|¾û¿ñùü+öözqÁÿÑêx±yFZü]ù5e8	sÓæã	ÿq8ß­ø¬¤#¼{VÆqMù55-ÖÝuaQ¡{v.¿°ågr!÷¯ ÃcÊGºÎuEwþîèJÝÆÔ<±/0®UÈUD6	S ¤×F¬Ç#<Ï3;áç{fÂ. {ÿ8rØ¡Xþ "S¿KdWu+×^{ªÊÂ¾×º[s?|·*Hr-WHK±Oj¸IÂ¸5±bTÕãÝùeí¼µ7bY2A½¢ |
| --- | Minor | %(»þ749P3¾Æó8ëÁÒü°+àuæ÷õÏ<vqZæbóÐ |
| --- | Minor | äþ¼6òÆoZ`28. VÇ>Ï|2o78÷o1ë½%>lwfz_Úå&:¶¡3ú&<ý ¦ÁÃ	O^ºeJU{&³ |
| --- | Minor | è®<É~|É;óR|Hßø« ]L1ÅYà	Zt*C3FpaªûÿÖ#?¸?w_>c{++<NÃ®É¸Ö³ÏìÎ¸)ØVÓóÇ/ÜÃë8«XõDÂµ³>:¿¡sFÒí-)Qµ|s]©XüºB8¦+øÜ]}-ûSér·îòMú9x>C+ÀÜÜyÞ¸¿ |
| --- | Minor | ´ |
| --- | Minor | }}?hZÞå{dëk!^j[§³6|åÏéÿ¶f\M0sÉ©{~¦= |
| --- | Minor | ¦¶1Ìc-àÛ^í¢÷ó;áÑ/ß¯{E |
| --- | Minor | pTìZs£\ÑeºÔÛ{~¾ËEúj¶åÖñàMW£½9ú´tNõ¶¸&ú­n. ¸p­lÝVÌó=Ùó8¶TW'-Û×¤Ù¢PÅ½ígc¾¦ìçªô(7C91<ö&.£¢À`(*æJJÊ¤Ûß¿»Ûóê'L(aBóÇÍ¢¶ëtÝN¼ül)¾ó;¿¹Xº¦ä³¿E5`¿<ÚÈí3AqÀÜX©Cé{¹ìÔ¬i¥&0?Àn;½ cbfñY¦Ì<¶=½=Z­xÝÅmY[Ù«áeê |
| --- | Minor | {¥ |
| --- | Minor | ¢ÊCÜájqð©ó¨½ ÏÂ8^V'-¤ü|l¦¹ßY$xÚc §+ÑKÕPÄf	ª. æ}*YX%!Åí²/)Ü[ê¥é³ÞV¬ìB |
| --- | Minor | \Y%*íTÀÌr°¿|7X!.*FFð`Óyqd¿wU |
| --- | Minor | Cæ'¥ÛM<2~ |
| --- | Minor | ×HûÑó¹¶ëäÇlukNt=¤Ù­ji9l:ØùÁ®_ÀÏápùJ+ cÞç_ÇAîæO\}¾0K6¡ÛE Ý}îÒ#4*'ÓÚùpÇDN·uúa­<'¿NÄã4â-Ô_Ã$öõ<]%#DØæéÂ7·iT8+"Q~HH¶O¼ãO RaéFÀy·Ú^þºVÇÁ1dÁÀGMë]·ººæHC	ÑßÁG%.wcnÜì¼xÓ6ß±f:.x; .'ayçÂàTÐ ù;Ñ?`FîÆ?úRqkéeÌcûyÞ¯¾u2épÓñêÓuiÇ¶pæë(ýyEDdoóã£B¢tº}¼>['ÍÌAÙ=ùèwVöhâÖÈSq«rmå-EGM~±H©öx¼Ìïó¾üçc2pÀ¸ãº. ¢0¼a¬ÂDÊËðÞ&ÍØ¿ íe±ÔH1Ø}u½ëGP~±ØmÍ7-{ë¶Ö6×çq§Û»ójØÎEK¼¹ÔOÅã/NKGºDÅázèYÀý­µn²µÖ¡'ö4cÂ^¿1Êzáõe7\àgøf~4z-òiýMtÇÂ^0d×JãúQÿÕA¾íg5ËÕfí	zÏJÆjk0ÒÄßY \&Û.. |
| --- | Minor | Sentence exceeds complexity threshold, split for readability. Applying the split needs --strength moderate or higher. |
| --- | Minor | none (split proposal only; source not rewritten) |
| --- | Minor | none |
| --- | Minor | Check: NEEDS-LLM |
| --- | Minor | Flags:    not-assessed |
| --- | Minor | SENTENCE (Line 1736, 565 words, 9 clauses)  [Script] |
| --- | Minor | ¤C~ìKFbMcmVBº¬4ÇÅXÇÄÈµc£ÝlädâUiXfu'³êØÊBã!ríyð«¸¢ ¯ð2+F>Þ^;`9éÄKQkSÉß dr²t|Íº¯ÂÅ?Ø,w'» |
| --- | Minor | ` O°RØýF°~Ý£!ýW©xO~nF-[[PÏÃA |
| --- | Minor | ­jqÒÀbõ¼êÄUÆü{ìÀ'¹HøÜÉ²Æ@R'.+)*üèxb 5Ä¼êâ|V:ñs¦¹Â(±Ùæù âyÄæ |
| --- | Minor | Ñà711Uñ «¢¿3ÌHw·Ð	q 2ò¤fÅjÒâë¯ÒÜmÛB,ÁÛLÂÇQ­mÂ>$û¿°GgÑ>ENN¦>´/| æðµ+ô ÿ ë¬³R#³RÆíóZÎf§ üTÞhh.mS´5áÚ¸mêî¿ÙyA-.ÏÏ+¼ÂÊRLÂ#¨h¤dF*òdâTpÛtS R |
| --- | Minor | °÷ÑH¥rº79"ß¦eÃ´e5ñ|tCR%¤(>EW ÏqÊoÔ²-í[ÎmA¯®W*ÎgÕ¹ÏÁa²å¶­áSk{Dæ%¸ÓxqY'=¦	H#ÛKZQ|3¶O¥`Æ6jqÌuÓº¶;Þ%xFÅOùíÑÉo Q1Ï`9Ý¯æñ­?O/¶o4Æ¬Ã	E½fûâWÇRÁ»v*.p#ì7i# ÙkÈÍ5 |
| --- | Minor | %·Ìy§K rEy£Æö×Ëÿj¦ endstream endobj 750 0 obj <</Filter/FlateDecode/Length 24>> stream xÚk``°.¾üx_Eã¯§\ 2³ endstream endobj 752 0 obj <</Subtype/CIDFontType0C/Filter/FlateDecode/Length 6179>> stream xÚY	XW¶®¶é.TD¤h.¬j |
| --- | Minor | [¸¢Æ Æ |
| --- | Minor | Qö¾M³o²¯"(È"JKÔÄÄ%N£&jB1§ðò¾÷nqÉ¼y¯¿ê¦î­®³üçÿ¯P&&D"î²z}ðï éöNÁ»}§VÖâXdÆ%òQ5H'­L°­ô²I_>e-_am²G6¢ )5RPJê $Ôë,ñ	Þîû®oPD@Dìi³ÄøùG¨f8:Îj<¾£r¦Zå½#08:<0@åä£Z5MµzjMp49 ¤Úîëï½{§*x§j£¯*2Ü7,\å>ij£@¸*:8,PEÞÃ|wûzûú¨"||ÃTþ¾ª6lT-P¹ìð ÷UÙÛ«Tá¾¾*ÿ¹~ÓÃüv=á»6;¯³_¾vÍF{w:¯Ùà<-"&Bµ38Låãá°;|Úcúæ?¼XÊO½EM¦¦PS){jå@M§fP3©·©9Ô_¨w¨¹Ô<j!µZL-¡(gj9µZI½G¹P«©5Ô:j=µÚHm¢\)7ÊRSåMm§|(_Ê vQÔ* ¡B©0*¢b©½_¥ KÐhS±Qj96ÈÚ>DÚc¼@£¨HYxÉ R~ÛÊ¦ªåÖQ'Ûþiy|R8FrhjZö°ö0Ø·XÖÃ`ð9£O×(ª÷¡}Ü=*ªVB ýhÙÇxÒzl~`¦gsL}cSåñÃ1¥Ú.ûP¾ý¢Ù{@/Óâd<AÉ$MØÏ¾:WqÌâÝÈãïÜ)yE!ªá±Ð æÈ}an;O 3O8óÞKÄå-P*HÀFÁ9/íÕÀÅÓÙ×ñÐ<¨ò/ßQ>õÍõ-WÕ÷SjÑGsï?|Îc'øZ±Ð}õd;B)¬÷Í÷àëñWD­° |
| --- | Minor | ]à )Í{MhÕëÎ[¾9+° +&D|á cÿà´%(:.;§ÈÔôäÃ÷=èòÒ²rSæãÜîMXôâ;àyl5R6úpÛ<Ygs÷óI7×j8Ï9ÂÃyóÞ[IøJ\{QÛ-íÍhEEª>n_2ÓqX­±eÌ©ùh3¯¾øÅwÊ |
| --- | Minor | @]ýûäãoÎ²@ý¸3U|A^ÍÖé3êxrÂ½û¾ìôêe+Xíñ Ñ5p·Â}füÛÀVþÉ½çn¾Ù-wÅ´ÄìD)Á >o dY%>)Ð«SQ/þf:¼nÛ²9{ùºñ3ñ8<úñTøÑ©ÚF~+Í,	S»oûÆE,6G0ìÆ)t®®?Þ ä7²Úª`´¤6È,Gãa¶ vBÀ¼êõzZ¹Èàx5§BóyùÓ|¯%¼ GÕò%É^¹SåLÌ®sÂÃJxA¾4²ÿCp ×RÎ2k4íàræ¶HÀªæG0ûQ*&<Å ´¸ô´x |
| --- | Minor | µ>pÇé`ÌÎË«òQ}£æöÓ|ËN×²å,5ËÀÊ'ÃlÑù² JNg´éW1m¯k/l`apå¯'¼Ô	m¢²MrêÁÇÀáT¬µ æ[q7ZO\TþâxË1ï<gË]OnÎNÏõKxPn Y_?A n+¶xqxò}Y|^péQåïrÚïÞ¾«ìªc¿~Òú3wï~ÐÙ\ÁÁØE²aÇ¢ÜI2ýI\«¨êGÊxp`¬ í#¾§0Æ¨ïßbDúg:ÁviOðf¡ú4ý4ïMSH·@¨ä0»z! |
| --- | Minor | ¤C~ìKFbMcmVBº¬4ÇÅXÇÄÈµc£ÝlädâUiXfu'³êØÊBã!ríyð«¸¢ ¯ð2+F>Þ^;`9éÄKQkSÉß dr²t|Íº¯ÂÅ?Ø. w'» |
| --- | Minor | ` O°RØýF°~Ý£!ýW©xO~nF-[[PÏÃA |
| --- | Minor | ­jqÒÀbõ¼êÄUÆü{ìÀ'¹HøÜÉ²Æ@R'.+)*üèxb 5Ä¼êâ|V:ñs¦¹Â(±Ùæù âyÄæ |
| --- | Minor | Ñà711Uñ «¢¿3ÌHw·Ð	q 2ò¤fÅjÒâë¯ÒÜmÛB. ÁÛLÂÇQ­mÂ>$û¿°GgÑ>ENN¦>´/| æðµ+ô ÿ ë¬³R#³RÆíóZÎf§ üTÞhh.mS´5áÚ¸mêî¿ÙyA-.ÏÏ+¼ÂÊRLÂ#¨h¤dF*òdâTpÛtS R |
| --- | Minor | °÷ÑH¥rº79"ß¦eÃ´e5ñ|tCR%¤(>EW ÏqÊoÔ²-í[ÎmA¯®W*ÎgÕ¹ÏÁa²å¶­áSk{Dæ%¸ÓxqY'=¦	H#ÛKZQ|3¶O¥`Æ6jqÌuÓº¶;Þ%xFÅOùíÑÉo Q1Ï`9Ý¯æñ­?O/¶o4Æ¬Ã	E½fûâWÇRÁ»v*.p#ì7i# ÙkÈÍ5 |
| --- | Minor | %·Ìy§K rEy£Æö×Ëÿj¦ endstream endobj 750 0 obj <</Filter/FlateDecode/Length 24>> stream xÚk``°.¾üx_Eã¯§\ 2³ endstream endobj 752 0 obj <</Subtype/CIDFontType0C/Filter/FlateDecode/Length 6179>> stream xÚY	XW¶®¶é.TD¤h.¬j |
| --- | Minor | [¸¢Æ Æ |
| --- | Minor | Qö¾M³o²¯"(È"JKÔÄÄ%N£&jB1§ðò¾÷nqÉ¼y¯¿ê¦î­®³üçÿ¯P&&D"î²z}ðï éöNÁ»}§VÖâXdÆ%òQ5H'­L°­ô²I_>e-_am²G6¢ )5RPJê $Ôë. ñ	Þîû®oPD@Dìi³ÄøùG¨f8:Îj<¾£r¦Zå½#08:<0@åä£Z5MµzjMp49 ¤Úîëï½{§*x§j£¯*2Ü7. \å>ij£@¸*:8. PEÞÃ|wûzûú¨"||ÃTþ¾ª6lT-P¹ìð ÷UÙÛ«Tá¾¾*ÿ¹~ÓÃüv=á»6;¯³_¾vÍF{w:¯Ùà<-"&Bµ38Låãá°;|Úcúæ?¼XÊO½EM¦¦PS){jå@M§fP3©·©9Ô_¨w¨¹Ô<j!µZL-¡(gj9µZI½G¹P«©5Ô:j=µÚHm¢\)7ÊRSåMm§|(_Ê vQÔ* ¡B©0*¢b©½_¥ KÐhS±Qj96ÈÚ>DÚc¼@£¨HYxÉ R~ÛÊ¦ªåÖQ'Ûþiy|R8FrhjZö°ö0Ø·XÖÃ`ð9£O×(ª÷¡}Ü=*ªVB ýhÙÇxÒzl~`¦gsL}cSåñÃ1¥Ú.ûP¾ý¢Ù{@/Óâd<AÉ$MØÏ¾:WqÌâÝÈãïÜ)yE!ªá±Ð æÈ}an;O 3O8óÞKÄå-P*HÀFÁ9/íÕÀÅÓÙ×ñÐ<¨ò/ßQ>õÍõ-WÕ÷SjÑGsï?|Îc'øZ±Ð}õd;B)¬÷Í÷àëñWD­° |
| --- | Minor | ]à )Í{MhÕëÎ[¾9+° +&D|á cÿà´%(:.;§ÈÔôäÃ÷=èòÒ²rSæãÜîMXôâ;àyl5R6úpÛ<Ygs÷óI7×j8Ï9ÂÃyóÞ[IøJ\{QÛ-íÍhEEª>n_2ÓqX­±eÌ©ùh3¯¾øÅwÊ |
| --- | Minor | @]ýûäãoÎ²@ý¸3U|A^ÍÖé3êxrÂ½û¾ìôêe+Xíñ Ñ5p·Â}füÛÀVþÉ½çn¾Ù-wÅ´ÄìD)Á >o dY%>)Ð«SQ/þf:¼nÛ²9{ùºñ3ñ8<úñTøÑ©ÚF~+Í. 	S»oûÆE. 6G0ìÆ)t®®?Þ ä7²Úª`´¤6È. Gãa¶ vBÀ¼êõzZ¹Èàx5§BóyùÓ|¯%¼ GÕò%É^¹SåLÌ®sÂÃJxA¾4²ÿCp ×RÎ2k4íàræ¶HÀªæG0ûQ*&<Å ´¸ô´x |
| --- | Minor | µ>pÇé`ÌÎË«òQ}£æöÓ|ËN×²å. 5ËÀÊ'ÃlÑù² JNg´éW1m¯k/l`apå¯'¼Ô	m¢²MrêÁÇÀáT¬µ æ[q7ZO\TþâxË1ï<gË]OnÎNÏõKxPn Y_?A n+¶xqxò}Y|^péQåïrÚïÞ¾«ìªc¿~Òú3wï~ÐÙ\ÁÁØE²aÇ¢ÜI2ýI\«¨êGÊxp`¬ í#¾§0Æ¨ïßbDúg:ÁviOðf¡ú4ý4ïMSH·@¨ä0»z!. |
| --- | Minor | Sentence exceeds complexity threshold, split for readability. Applying the split needs --strength moderate or higher. |
| --- | Minor | none (split proposal only; source not rewritten) |
| --- | Minor | none |
| --- | Minor | Check: NEEDS-LLM |
| --- | Minor | Flags:    not-assessed |
| --- | Minor | SENTENCE (Line 1736, 735 words, 13 clauses)  [Script] |
| --- | Minor | | ÿïä»_Ò"!MzÃ¥â»b¯â¸ßÉ0åeíbõøÅr5 |
| --- | Minor | Yë5¤máYðhë¡aÐyµYY(=KHJQz5ÇÔnªìàúC÷XMËw`Ñmy> |ãSb1x(ÿOrÕª9M§*H?ÊícÕæ¤ rø¾wejèÀl¢¦ |
| --- | Minor | ­ß§Ó·ýÓÉ<ÉÁUù+ë$6	ân9Ù8@¬B µþ³»n2lâÕ`cKÇ  .!4PÈÎÝpe+ïu~ßÍï`RqñX7wºýÎ±§ì¯ÿgë¼è´43uØÛáØ&`(8ò"ãÊi>¤ñrh[òàA_±GL}ºìiøÓÐ0yêùÔ¯Å¯Ãr"¢VTCõçÅqê¸fµÖßcêB c½+°ØfãçíÛ"ø`Í®(eBæÖö@nÖ)ÊEév~1¨Áùî¥S®®<Ê1ïÚ°MaC=>÷ÌIj-SægÌÎå³ð®3éµ,Ø¿{C;PÂ.©Ì(Ð¦§¥'kÌ°ÒØººÒòNUlC+grÌÅèúÉèúÃhå6d}Ã~>ðHl¶µ«ëòUTÌÁ`y#ÈÐjÞüÕhÕ6 _ÊçÆ<ô0E: Âøs(ü7ý=¤û9Iwçs¤m%µDA|ÛþutZôÏ>F¶âEímC!ýMmvSÜÖùFr:x"gý~>¨)°ÔÊÈ^_ £+ßÌñRÑ8('ÊÛ'!Öø±ø!'~È¹ÏQÛEÌíètô[ÿ ß#6©ÿÕ¢Í\ÀNFû.õO+F#Ì |
| --- | Minor | ç¡ù«1¿3£÷ÉH!vÕf$ò¸~TPËÊª£Ãl© ×îXÒXß¥ÈàÇ«é¢ VËHÔçiûäøÊh¸ýÿÎÂNúç{°×diPºA3&%6ù³F'¿C'ÙöÏäÒ\46µÇç=ØlÌÊKÂÞÖ7«Åû#8ÚØ¸ÇÀFöÈ ór®³qÚ0Ê2*LH5ÕmJ.×áI2Ñfòþ:3ëOC7TçfW÷`ËÑy%ÑZe2iNÎ8ü­>m9ªK?Jò»¬ÁeÒÀGõOÅå)qx^ÁÚ² ë¯IOA¼G|pøx@EoO/Cú#£Òú®'±ôÞÜÚZy«¬T^Æ7hõºHeß$ºo¼è/cÜ tú(ÇrY©Ók9&IÙ0µYlh½ÚX&õøY#Ô0qÓgÄòA¾J)VÐbZß=S¯×°õ(¯¿ «ôúC±0Ôd ClAÿ.pÆjnøC5»®wåaºóÃôoÄJÑÝ/Û è¹Ð=@¡ì¥½¾b¢MüËõÍþ­äÿÚrÁLoÁ`Û\â)D@7°r-5öhì*À¸x@èh`ûke üÃô'ß¯,gsó |
| --- | Minor | ¿ÿrÍ3)|ØÔ÷8 ßu¼Ã¦ì×&¥¡ôÒx,±ÕQì§+ñ7<ÂR.!A§KS&åksK+-ã,r¨ÊôZÝý7ã@üû@EvÉkÁ!cW°\üa;í:_Öí¿áðZ"0lf`ë|÷Éâö.¢=^W<PÄ"mB÷þ·¤=ìêµaÿ\¸üå©ù[oíÄï£ ,[ÕÑ)Ü4"9LüTA$Ór´ók]Þs?_ÛÔXÕ!x¥ë¹òºÂ.ö±ÞGíÍ¯^¼pÒDiÕ5(»«§_<ù¨µ«(<UU'ôíÿ7ÞõgJc4ökÖ¿A6ö´Õß'½?ý¨¨"4J·S§Eîa×&ß<Æ§¤|¦ËÚ{cc£W)>óñ'Ê<è>~ë³ =ë×7¨ny³Ç÷³kêFL@|?qR¾¶Þà"O\9ÐÁþZô]	qbú~Ã¦dûÂé3¬!1 ú­¹À<ÌâÑDñÁ¦ÍÎ;¶¸Dp £Ûxîº×?éýRúF-ÿÌ¡¸ åö¦è¦Êv]¯Nî\{ôÞ üaL©¶*Êô`Bm¨Ò=tù[ðÔ ÂéPV ý¶åd £­+vEl#LC`kùQb=h"5º	FHÅó½£ØKí²2÷òQº¼ô|SµÜçÈyþEE¦Ù_£RÈc#c¢b#M§`¥ÅÎ¢ì!ë®>e8#py×+/5w¬_2ö*XÌi9um§50QÙã­ ím<cVFn@¼ùrä99¡æ\ËG,s¦ì¨6¢÷K |
| --- | Minor | £¨nk«©k½â}u¶ÆïÌÆYóóæu,ç	_ß`ú |
| --- | Minor | (yl¡°EKl7´¤pñMèvFÎÿÛuqWI) ¥ËQF½?[5Äkåå |
| --- | Minor | ¾»ØÇ9¢T.±ÈQ{½x÷KÞÊåùÆ§iÿ`C´å«"0ÏDK°P| v£W¯C×ª9h [ÛÂ5­³Û:q¢ÖÔÁ7¸^®ú6òæ'/ÜÐ¬M`¿¨ |
| --- | Minor | &·Ý±­m_o¼'E0á­Tz@ÀÎ}VyûÂåEWð8<tÁ{ó¼CZOÖ6»¸©à;Ô|"·½gxo×>õß®KÓî×¥ï'rÇ")6qL+uBNû ©½~¬DÑø½ö |
| --- | Minor | ;n®Nµµç8øá+{iÕ×?ÕÝBw»¸´yooQT/+Hêz/H{ïõSC,ÓÊvRèCÈBÞ_QâmNËãm}î8@ý@¸²ï"|æ ?¯~LCÃId±¹)Ø"TSÀC¹ø\Vw%Ó©4J@n wÖèô° ]ëhdûå |
| --- | Minor | ÒÓöóØ0u²s[h±,_£ai,¬°±¥ùÊ|æ(+ÎÎÌ¹Æ[Ô |
| --- | Minor | _cm!µ6Ñ÷¯ñOßÆú®<µ§PR÷mÀÎâ6ÙS£ñöFãç÷ÿî0ÖÓ?þEH%Åggî¯ek3óK²yp]Á©Ïõ'ãÅ²Kõ1¨pÙ[ýN[ÖB^K6À®q°Á®ñ°qîíBÄ]8;Å¼n]V«!Qó°È>  eíÄaZ<,ß¤¬uÁ£°,&Î¹uøØðð6:6&+!21øg Ax¤ÌG-'2Nfä.êñ"¹9Ð ú |
| --- | Minor | ÷ü F-¼(©ñAðrq itdØî¹üþ§­*ÓöUsq¸JÐc |
| --- | Minor | g=¯bhm|ð`ÎîÍ³ÀáÞÏ_ÀJº&ùóøÓß´'Ü%¿=_,lñÅg;?|óT¼ª"÷`	§Á&Î#ãLhhSûäo âÌ?^Z¬íX¢Þ6þùÄ2©@|?¶UæÈ¹!&Í#³¡Â=b0èõú£ÍÌìãEÙÜÌÙ°ÿa$ô8 endstream endobj 754 0 obj <</Filter/FlateDecode/Length 28>> stream xÚk``0°/þü|^ÝÌ7__¹0 ² endstream endobj 756 0 obj <</Filter/FlateDecode/Length 26>> stream xÚ«ÿ? |
| --- | Minor | | ÿïä»_Ò"!MzÃ¥â»b¯â¸ßÉ0åeíbõøÅr5 |
| --- | Minor | Yë5¤máYðhë¡aÐyµYY(=KHJQz5ÇÔnªìàúC÷XMËw`Ñmy> |ãSb1x(ÿOrÕª9M§*H?ÊícÕæ¤ rø¾wejèÀl¢¦ |
| --- | Minor | ­ß§Ó·ýÓÉ<ÉÁUù+ë$6	ân9Ù8@¬B µþ³»n2lâÕ`cKÇ  .!4PÈÎÝpe+ïu~ßÍï`RqñX7wºýÎ±§ì¯ÿgë¼è´43uØÛáØ&`(8ò"ãÊi>¤ñrh[òàA_±GL}ºìiøÓÐ0yêùÔ¯Å¯Ãr"¢VTCõçÅqê¸fµÖßcêB c½+°ØfãçíÛ"ø`Í®(eBæÖö@nÖ)ÊEév~1¨Áùî¥S®®<Ê1ïÚ°MaC=>÷ÌIj-SægÌÎå³ð®3éµ. Ø¿{C;PÂ.©Ì(Ð¦§¥'kÌ°ÒØººÒòNUlC+grÌÅèúÉèúÃhå6d}Ã~>ðHl¶µ«ëòUTÌÁ`y#ÈÐjÞüÕhÕ6 _ÊçÆ<ô0E: Âøs(ü7ý=¤û9Iwçs¤m%µDA|ÛþutZôÏ>F¶âEímC!ýMmvSÜÖùFr:x"gý~>¨)°ÔÊÈ^_ £+ßÌñRÑ8('ÊÛ'!Öø±ø!'~È¹ÏQÛEÌíètô[ÿ ß#6©ÿÕ¢Í\ÀNFû.õO+F#Ì |
| --- | Minor | ç¡ù«1¿3£÷ÉH!vÕf$ò¸~TPËÊª£Ãl© ×îXÒXß¥ÈàÇ«é¢ VËHÔçiûäøÊh¸ýÿÎÂNúç{°×diPºA3&%6ù³F'¿C'ÙöÏäÒ\46µÇç=ØlÌÊKÂÞÖ7«Åû#8ÚØ¸ÇÀFöÈ ór®³qÚ0Ê2*LH5ÕmJ.×áI2Ñfòþ:3ëOC7TçfW÷`ËÑy%ÑZe2iNÎ8ü­>m9ªK?Jò»¬ÁeÒÀGõOÅå)qx^ÁÚ² ë¯IOA¼G|pøx@EoO/Cú#£Òú®'±ôÞÜÚZy«¬T^Æ7hõºHeß$ºo¼è/cÜ tú(ÇrY©Ók9&IÙ0µYlh½ÚX&õøY#Ô0qÓgÄòA¾J)VÐbZß=S¯×°õ(¯¿ «ôúC±0Ôd ClAÿ.pÆjnøC5»®wåaºóÃôoÄJÑÝ/Û è¹Ð=@¡ì¥½¾b¢MüËõÍþ­äÿÚrÁLoÁ`Û\â)D@7°r-5öhì*À¸x@èh`ûke üÃô'ß¯. gsó |
| --- | Minor | ¿ÿrÍ3)|ØÔ÷8 ßu¼Ã¦ì×&¥¡ôÒx. ±ÕQì§+ñ7<ÂR.!A§KS&åksK+-ã. r¨ÊôZÝý7ã@üû@EvÉkÁ!cW°\üa;í:_Öí¿áðZ"0lf`ë|÷Éâö.¢=^W<PÄ"mB÷þ·¤=ìêµaÿ\¸üå©ù[oíÄï£ . [ÕÑ)Ü4"9LüTA$Ór´ók]Þs?_ÛÔXÕ!x¥ë¹òºÂ.ö±ÞGíÍ¯^¼pÒDiÕ5(»«§_<ù¨µ«(<UU'ôíÿ7ÞõgJc4ökÖ¿A6ö´Õß'½?ý¨¨"4J·S§Eîa×&ß<Æ§¤|¦ËÚ{cc£W)>óñ'Ê<è>~ë³ =ë×7¨ny³Ç÷³kêFL@|?qR¾¶Þà"O\9ÐÁþZô]	qbú~Ã¦dûÂé3¬!1 ú­¹À<ÌâÑDñÁ¦ÍÎ;¶¸Dp £Ûxîº×?éýRúF-ÿÌ¡¸ åö¦è¦Êv]¯Nî\{ôÞ üaL©¶*Êô`Bm¨Ò=tù[ðÔ ÂéPV ý¶åd £­+vEl#LC`kùQb=h"5º	FHÅó½£ØKí²2÷òQº¼ô|SµÜçÈyþEE¦Ù_£RÈc#c¢b#M§`¥ÅÎ¢ì!ë®>e8#py×+/5w¬_2ö*XÌi9um§50QÙã­ ím<cVFn@¼ùrä99¡æ\ËG. s¦ì¨6¢÷K |
| --- | Minor | £¨nk«©k½â}u¶ÆïÌÆYóóæu. ç	_ß`ú |
| --- | Minor | (yl¡°EKl7´¤pñMèvFÎÿÛuqWI) ¥ËQF½?[5Äkåå |
| --- | Minor | ¾»ØÇ9¢T.±ÈQ{½x÷KÞÊåùÆ§iÿ`C´å«"0ÏDK°P| v£W¯C×ª9h [ÛÂ5­³Û:q¢ÖÔÁ7¸^®ú6òæ'/ÜÐ¬M`¿¨ |
| --- | Minor | &·Ý±­m_o¼'E0á­Tz@ÀÎ}VyûÂåEWð8<tÁ{ó¼CZOÖ6»¸©à;Ô|"·½gxo×>õß®KÓî×¥ï'rÇ")6qL+uBNû ©½~¬DÑø½ö |
| --- | Minor | ;n®Nµµç8øá+{iÕ×?ÕÝBw»¸´yooQT/+Hêz/H{ïõSC. ÓÊvRèCÈBÞ_QâmNËãm}î8@ý@¸²ï"|æ ?¯~LCÃId±¹)Ø"TSÀC¹ø\Vw%Ó©4J@n wÖèô° ]ëhdûå |
| --- | Minor | ÒÓöóØ0u²s[h±. _£ai. ¬°±¥ùÊ|æ(+ÎÎÌ¹Æ[Ô |
| --- | Minor | _cm!µ6Ñ÷¯ñOßÆú®<µ§PR÷mÀÎâ6ÙS£ñöFãç÷ÿî0ÖÓ?þEH%Åggî¯ek3óK²yp]Á©Ïõ'ãÅ²Kõ1¨pÙ[ýN[ÖB^K6À®q°Á®ñ°qîíBÄ]8;Å¼n]V«!Qó°È>  eíÄaZ<. ß¤¬uÁ£°. &Î¹uøØðð6:6&+!21øg Ax¤ÌG-'2Nfä.êñ"¹9Ð ú |
| --- | Minor | ÷ü F-¼(©ñAðrq itdØî¹üþ§­*ÓöUsq¸JÐc |
| --- | Minor | g=¯bhm|ð`ÎîÍ³ÀáÞÏ_ÀJº&ùóøÓß´'Ü%¿=_. lñÅg;?|óT¼ª"÷`	§Á&Î#ãLhhSûäo âÌ?^Z¬íX¢Þ6þùÄ2©@|?¶UæÈ¹!&Í#³¡Â=b0èõú£ÍÌìãEÙÜÌÙ°ÿa$ô8 endstream endobj 754 0 obj <</Filter/FlateDecode/Length 28>> stream xÚk``0°/þü|^ÝÌ7__¹0 ² endstream endobj 756 0 obj <</Filter/FlateDecode/Length 26>> stream xÚ«ÿ?. |
| --- | Minor | Sentence exceeds complexity threshold, split for readability. Applying the split needs --strength moderate or higher. |
| --- | Minor | none (split proposal only; source not rewritten) |
| --- | Minor | none |
| --- | Minor | Check: NEEDS-LLM |
| --- | Minor | Flags:    not-assessed |
| --- | Minor | SENTENCE (Line 1736, 1121 words, 24 clauses)  [Script] |
| --- | Minor | FÁ(£`Q0lÀ >Òþ endstream endobj 757 0 obj <</Length1 94333/Filter/FlateDecode/Length 12796>> stream xÚí|	xÕÕÿ¹ï2ÙÉ0$y! ÌE4"ÍDPH aIbf"Zp¡jEYT VÅe26,¶Újj¿ÚÅjýpë÷·JKµZËü÷Î |
| --- | Minor | ¿~Ï÷ïÿùï¹çxî¹Ë¹÷{Î¹Ë;áEÐzR©`æìü¢öO½@ó¯òÍQEÄ"¯_Ò¾tåÞ	­{¢î" Y¶tÅ%Û¯-&JøHßÕÜÔÐxìoJÑ­è_Ú¸»Ã#P~åQÍ+½×.`¯¡|hSÏ¶Å |
| --- | Minor | ­ý)ÑOòòÊëÛ¯z4ì6b¥õ7ZV6uÏ±åõD´w4µöñÄª1Æ¨©w°Í¤S¨¾Ct+á´D¹>TW",ÂAë|ÌTÍyÅLrÑwVÿEï,ºIqÔOeA	ôô	-;XÓ÷Ãë{y |
| --- | Minor | ¥¼Ü÷F¢ÿ2ôß;i:è[Ý×Ó÷{ÚCõÕ· owßWì'sØ<ôí¡×éýzh=À¢íCòð¼²­»é9·Ð¢mè9z<8»-c±66¹ÏÑ~¤cÀfºe^@ß'»i |
| --- | Minor | #ðMJ÷Ð¥Öª¡«Ç¾ªï)ÁWÒ,y ëúîÄ1zxÔÝí;YÈ°Yn§kifºÔ¥ggVv7]«¬§]ì½©<C§§©UI;Í¨XI©Ê ÷Ñ½ôÚ ì¾t åBú¥mCëg]&róì=ÚEáD#¨±oõý®¸è¹í®£uên¥V]§Tý¥ |
| --- | Minor | ÕvÜÞ;ZÈKó´nI°ìéû¦·^]ÉðÅBÉ' Ó	ò`ýÒj§»EéØÀZ/Bí¤Kh]¦ÆÓì]Q¿^K¢Ü¼^Ý¯íÖüCêè&¤¿-È%S&''ÕÐ"ZKmÃaUÑÕ°øcðúNz^Qõ(lµxaø> »Ô%T£¡6ºQf7ÃsÕ jgOP5]Ïõckè/,ô!sÜ]×ô}Ø÷Gå0ÅHj¥WACa´ßB÷µ´Á{EXõ`p:MgÑÀ±l,,S¤îQ· ÷è´eÐê+Z*Ö¼·amý9bï²·T¿ú{ý}B%¸¤V~¬¼_Â.W^wn¦vßâgõë-|-A{'Í§0ÒíZÚ¯\K·²z-4µÈi=T­¶³êï´cÊRÜ1E4jD,p¯íþ;uèG¨JIÑ*õ |
| --- | Minor | +Ú· ¹ÛaËôøêL¾¹çi?vÃ1Z}ºUTI_³06qC<NÁºKÿ*¸ |
| --- | Minor | §Ë<I.XWvZ¸º²ç/XWë\ |
| --- | Minor | +ôó¹°É¹2|ÍçÛ.Xw¡¾ªÛ©´ÚF5¨G¯ÑuY°ß& ½Û­L§Íû§ír°jáÍj¬¤óÝ{\ápÍ´9·C#ú.£ÖØn%~jóí{t·öÅ± eÓ,î F÷³'d¦¡p¯~@ þ;,8Ñ½§õYô¬Ã|û¨Ú |
| --- | Minor | ¿C÷Ó­t|r(1u9YéaôvÑdÌøkúµRüÀò¢e+%XâôEdÕÖ¶¨Ë0óé¾?÷}~öÃùþè÷-ôa»pBí&ûpG±{ÙÓtø<¹ëÉýÍVxåÜ]ÿ/ ´ï§XùÕ}OP¯~)Ùáù	jdØW»ÏþØ=»^yùÌ½½ïUÙ ÝrÜ@×(a*i/«_@»ÝBÓ÷Ùê¢h¼§¦ªê8ßöÓ2}2»~e9À¢ßÅv©!°A8ýö­¥r- ù¯hµò,éJ [øXOéCu7%±«pÿüL¡zÔ[Ô½nºqÏ³èöûëô¥Åx{`Aþx_ý¯Ûá÷ù¨å/Ý¥(8µÓeÊtåzDÄ¥qð3[Ø{7OH´9ÓØe-NÒm¸ |
| --- | Minor | £^øè~¶Tû´&³v-fú¢«±ûz1~®%n·ÑFÊ_sa*ú·á~ø|©Ìæ½^bÎ»_SåVPr×â|ËU_u-d.Ü]Ô7iæ¼°Çdò°'éßá×ÃdÑpññ°Gáå9%`¼]Ðfö6üÜèµ¾O;ÞÝû=ó¯¦UJ%=ÊrÙK°eý'Þ7­ï4FÝû2	ëÞÍCäTÃM{4¡ö¶óÃM³Ò8¡K-ìv"ùDûä¯Å=ª¾N)XÛcêå¬íÿ C |
| --- | Minor | kÛ©þwÝ1ÄÐÍXÃ-èía=ê3ì'!#éeöüßÿE°ã·k(eÀ·c°®v×Jídµ÷¿8WádÚ¾bí·B§=°ú3¥¤nøèzXðØínú>öÌWWþmÇÚà^]"H§¿Äm@ßgÉ8£L¨EJº9GÆÞÊ,xÜ­<8ïS¿Æ,sh½÷«Ë5ëÒéMä,XZ2¡¸¨° ?o|®cÜØ19£³GÙ³2ô´¶©)ÉI	ñq±Öè¨Èð°Ð®© £\âK)¯­\æK-¯÷UÙ+ìVÃWuÅÉù>³eÚcâüºñ¦Owø(¾ÚPSÛM®²:Åq®È>5Ûúe&:Ï°>-ÿÙ/khôUi·þÊ6Ð^>¾åµ6ÿ.Eþ»¬ÁhôYkPiÖ\ê£ZN=}¡Ê2ëÎªõ¥÷ëê.¤ä~XôèÅ¹uY»«RË+|ÐMUù(,Ã}2Å7Æ5¬È±(ßÇ¾ô±xKOÀ»/»*Ù+[`ÏÆúAÚ3Óè2ºfÕÆ#+T®ö½vemwDx¹½¼)$*¨;<5¼C´w³ªÈ(Uº ñâ¸ºù\ë±WÀjhléé;z×Ð&B·þ\|0TÂg)÷0Z|®m4ºsvÝÕc¥EõÈF{cÃZÚ nR³+çøFV×\*Lªo6¸³+DÂ]gT6](sÙz¤ö îòaõÍMõ<HX½½maåµ·gµùâÀ+}±ß%»äOljWeJÁ]]·¾ÝPwHk&O)P½«ÒÙ0Xå²iÜ%ùn±xi£pkcá[¿hY0òîêþÌ.«¯êLxþAOÑÑ4ecý2®ò²¾ÌÊeF×Æ&±Ô»ÄÒ­Få² N¼#bæ¢÷ÕµÍöÊÁ	±pdÔìsûffúR¼cWW%W±¡ÚUFÃ þ|GØúû\s£9ÂÑÕPQgVWón¼¥¾¢®.3èwúB²o×óìF1$Ûà°f¾¶£ãs«gÕVVØÄê}JyíE'Rl'¯®¨f)éÊ?aÚ¨z¶½úÊ`4÷'õsÛWð<DMy1ê±Û1ä«ìUõ]]Uv£ª«¾«¡§oý"»aµwuWWwµWÖbß3ÔØhóUÝUç³Ö7³Ip2·ªYÜ3UFsCðjÏ,³eÆÖõ7×ü½fs!Øò|uY¿Z8lF?Wzp Ø|Ö2¾C¡ÄÜZlÅ"\E­1Ûø&Që²+[f¶A ±Â¼+ÍZÉ·ÏÆ-BÁ·þÊÚ`Ù E6?¹òp[=o9Úß8·¬ïoè^oRªgÿ'á<4»bíq3_^³¾£s°ÆoË|¡e¦§ãËkUbæÊsá\S|ÉÑÛdÕn¼m÷Y>½¼ö¨mJaÅÉÆâÀG¨õmûë`õ±)>Äë	ç©8ÔÕä24t4*»êÍãËï!}â0éþ*ê2ÏY¹y946¿üH,2V»/ò[P>6ÎÎð¦ØçÆ¹ÚWÏÈÍª½ÉvC^T¤ð>CßÕ*ÍÂ4Fº¦Q¨õcøòå+,ÈÍÍFÂ |j½N§9'dÐsAßêÃ§)/R6Ò[X9ééiiQ©qIñ¡	=j©+,Þ7.ÖÖ£tçL@(aúh^²'è;II OL²äÄkH^©ì Wù#-		q¹¹ãÆfO¤Ä¤¤Ô´â<k^þ¸jYûNv[Ã{Ô\È8ÎRm9`ÝYÒôü´±ÙÔ£wëY©!V=±´ Á^¢Oa³d&Úc3K3ãCFjÍNÖsJK'ÆÚð¸¸ØÌÄLNIÉ¥-!IjfIfÈôN½ø=5}rlUsïz×¯û­SÎ®º#ª3®÷ÄÆ[nÌÐ3N_¯g½¹vÁ=-7Õî~}Þdõ3mÃË/³«ßxãÔø{jYî3oÇ½ß³ÄXØë½ug;¯e ~=³©wÉ¦=óªZt[Ëw/6FÍ}·ì¶ìÁK.ßùôWbHr¶,?/<,,JMJÊÒ­cá=~r^:!0.1.;5ZÏÌèQ'ºÂòÇE6ëlÔº¬£ì(Ã=VÒÃSÇpÇäæ# |
| --- | Minor | eV¼Ç½@qI1ÜUût KEä¾;V·ÛÃ°S»ÃÂá¸Èét.íÑó¡¹­á üRTlJrÿpâ~	:!{Òtg><2:'Ök·äP<L |
| --- | Minor | âD{âÄ ¸¤ ÀàñMÆwO)b½4mÍÎáæo7ymJ./eÜGJßv?¯æ_\^Ì=3R2>»4Ä2aB¨5\çuääÄ¢Ç¥g±bMÉ­§«Y,§¸d-!ÕñÂ¸IOt` ÃCb¹Õñ¨÷çÄ£Ò_É÷µ ©£ö«ã);£Xo5s þsÌ¯Éü[È£§ýó?{ðÙ¿~vö¸ÄÐÝâcÌå<tÿÖÿëg§2ãZúW%A	 H A	 H A	 H A	 H A	 H A	 H A	 Hðßfi	 H A	 ¬O³¬0Òy+(Us8  æ$_5ó Ð/Í¼J6HóÚ¢è}3o¡húÌÌÐbºÊÌ÷Aâ¯i*Æd¿ykÅ>y¨ÿJäCx½ò²Èü	r^å¬gdh·y¢µïyJµëÌ¼6DF§ÚfÞB#µ·Ì|ýXÝkæC©H­6óaôGís3Nd}f>JõwÍ|$µä£"þåR3MKâ E>|Èz#øZâîùÈ!õÑ<ÔßÊ×÷G>.îUO"(ìÌ' |
| --- | Minor | ©O}-ò61WpÌ´!2Cò£ü§"?^äýCè:düÈ!õ¦þ-K[¼-745 |
| --- | Minor | cq[û¥Í^cLùX£Ðé,_TPP`¸.i0f´µ¶y×´7åmím |
| --- | Minor | ¶Ö<Ã½b!ºx&OSÇª¦FTv´4¬xÒhñ |
| --- | Minor | ·£¡±ieCÇr£m1§¹éã«[7+Ö0ÐÒ·©jµ´:¼ |
| --- | Minor | ;Z<-¹¼'o`ñÁÙ¹­-Û1üìYMK;W4tÌkêðð¡ó |
| --- | Minor | FÁ(£`Q0lÀ >Òþ endstream endobj 757 0 obj <</Length1 94333/Filter/FlateDecode/Length 12796>> stream xÚí|	xÕÕÿ¹ï2ÙÉ0$y! ÌE4"ÍDPH aIbf"Zp¡jEYT VÅe26. ¶Újj¿ÚÅjýpë÷·JKµZËü÷Î |
| --- | Minor | ¿~Ï÷ïÿùï¹çxî¹Ë¹÷{Î¹Ë;áEÐzR©`æìü¢öO½@ó¯òÍQEÄ"¯_Ò¾tåÞ	­{¢î" Y¶tÅ%Û¯-&JøHßÕÜÔÐxìoJÑ­è_Ú¸»Ã#P~åQÍ+½×.`¯¡|hSÏ¶Å |
| --- | Minor | ­ý)ÑOòòÊëÛ¯z4ì6b¥õ7ZV6uÏ±åõD´w4µöñÄª1Æ¨©w°Í¤S¨¾Ct+á´D¹>TW". ÂAë|ÌTÍyÅLrÑwVÿEï. ºIqÔOeA	ôô	-;XÓ÷Ãë{y |
| --- | Minor | ¥¼Ü÷F¢ÿ2ôß;i:è[Ý×Ó÷{ÚCõÕ· owßWì'sØ<ôí¡×éýzh=À¢íCòð¼²­»é9·Ð¢mè9z<8»-c±66¹ÏÑ~¤cÀfºe^@ß'»i |
| --- | Minor | #ðMJ÷Ð¥Öª¡«Ç¾ªï)ÁWÒ. y ëúîÄ1zxÔÝí;YÈ°Yn§kifºÔ¥ggVv7]«¬§]ì½©<C§§©UI;Í¨XI©Ê ÷Ñ½ôÚ ì¾t åBú¥mCëg]&róì=ÚEáD#¨±oõý®¸è¹í®£uên¥V]§Tý¥ |
| --- | Minor | ÕvÜÞ;ZÈKó´nI°ìéû¦·^]ÉðÅBÉ' Ó	ò`ýÒj§»EéØÀZ/Bí¤Kh]¦ÆÓì]Q¿^K¢Ü¼^Ý¯íÖüCêè&¤¿-È%S&''ÕÐ"ZKmÃaUÑÕ°øcðúNz^Qõ(lµxaø> »Ô%T£¡6ºQf7ÃsÕ jgOP5]Ïõckè/. ô!sÜ]×ô}Ø÷Gå0ÅHj¥WACa´ßB÷µ´Á{EXõ`p:MgÑÀ±l. S¤îQ· ÷è´eÐê+Z*Ö¼·amý9bï²·T¿ú{ý}B%¸¤V~¬¼_Â.W^wn¦vßâgõë-|-A{'Í§0ÒíZÚ¯\K·²z-4µÈi=T­¶³êï´cÊRÜ1E4jD. p¯íþ;uèG¨JIÑ*õ |
| --- | Minor | +Ú· ¹ÛaËôøêL¾¹çi?vÃ1Z}ºUTI_³06qC<NÁºKÿ*¸ |
| --- | Minor | §Ë<I.XWvZ¸º²ç/XWë\ |
| --- | Minor | +ôó¹°É¹2|ÍçÛ.Xw¡¾ªÛ©´ÚF5¨G¯ÑuY°ß& ½Û­L§Íû§ír°jáÍj¬¤óÝ{\ápÍ´9·C#ú.£ÖØn%~jóí{t·öÅ± eÓ. î F÷³'d¦¡p¯~@ þ;. 8Ñ½§õYô¬Ã|û¨Ú |
| --- | Minor | ¿C÷Ó­t|r(1u9YéaôvÑdÌøkúµRüÀò¢e+%XâôEdÕÖ¶¨Ë0óé¾?÷}~öÃùþè÷-ôa»pBí&ûpG±{ÙÓtø<¹ëÉýÍVxåÜ]ÿ/ ´ï§XùÕ}OP¯~)Ùáù	jdØW»ÏþØ=»^yùÌ½½ïUÙ ÝrÜ@×(a*i/«_@»ÝBÓ÷Ùê¢h¼§¦ªê8ßöÓ2}2»~e9À¢ßÅv©!°A8ýö­¥r- ù¯hµò. éJ [øXOéCu7%±«pÿüL¡zÔ[Ô½nºqÏ³èöûëô¥Åx{`Aþx_ý¯Ûá÷ù¨å/Ý¥(8µÓeÊtåzDÄ¥qð3[Ø{7OH´9ÓØe-NÒm¸ |
| --- | Minor | £^øè~¶Tû´&³v-fú¢«±ûz1~®%n·ÑFÊ_sa*ú·á~ø|©Ìæ½^bÎ»_SåVPr×â|ËU_u-d.Ü]Ô7iæ¼°Çdò°'éßá×ÃdÑpññ°Gáå9%`¼]Ðfö6üÜèµ¾O;ÞÝû=ó¯¦UJ%=ÊrÙK°eý'Þ7­ï4FÝû2	ëÞÍCäTÃM{4¡ö¶óÃM³Ò8¡K-ìv"ùDûä¯Å=ª¾N)XÛcêå¬íÿ C |
| --- | Minor | kÛ©þwÝ1ÄÐÍXÃ-èía=ê3ì'!#éeöüßÿE°ã·k(eÀ·c°®v×Jídµ÷¿8WádÚ¾bí·B§=°ú3¥¤nøèzXðØínú>öÌWWþmÇÚà^]"H§¿Äm@ßgÉ8£L¨EJº9GÆÞÊ. xÜ­<8ïS¿Æ. sh½÷«Ë5ëÒéMä. XZ2¡¸¨° ?o|®cÜØ19£³GÙ³2ô´¶©)ÉI	ñq±Öè¨Èð°Ð®© £\âK)¯­\æK-¯÷UÙ+ìVÃWuÅÉù>³eÚcâüºñ¦Owø(¾ÚPSÛM®²:Åq®È>5Ûúe&:Ï°>-ÿÙ/khôUi·þÊ6Ð^>¾åµ6ÿ.Eþ»¬ÁhôYkPiÖ\ê£ZN=}¡Ê2ëÎªõ¥÷ëê.¤ä~XôèÅ¹uY»«RË+|ÐMUù(. Ã}2Å7Æ5¬È±(ßÇ¾ô±xKOÀ»/»*Ù+[`ÏÆúAÚ3Óè2ºfÕÆ#+T®ö½vemwDx¹½¼)$*¨;<5¼C´w³ªÈ(Uº ñâ¸ºù\ë±WÀjhléé;z×Ð&B·þ\|0TÂg)÷0Z|®m4ºsvÝÕc¥EõÈF{cÃZÚ nR³+çøFV×\*Lªo6¸³+DÂ]gT6](sÙz¤ö îòaõÍMõ<HX½½maåµ·gµùâÀ+}±ß%»äOljWeJÁ]]·¾ÝPwHk&O)P½«ÒÙ0Xå²iÜ%ùn±xi£pkcá[¿hY0òîêþÌ.«¯êLxþAOÑÑ4ecý2®ò²¾ÌÊeF×Æ&±Ô»ÄÒ­Få² N¼#bæ¢÷ÕµÍöÊÁ	±pdÔìsûffúR¼cWW%W±¡ÚUFÃ þ|GØúû\s£9ÂÑÕPQgVWón¼¥¾¢®.3èwúB²o×óìF1$Ûà°f¾¶£ãs«gÕVVØÄê}JyíE'Rl'¯®¨f)éÊ?aÚ¨z¶½úÊ`4÷'õsÛWð<DMy1ê±Û1ä«ìUõ]]Uv£ª«¾«¡§oý"»aµwuWWwµWÖbß3ÔØhóUÝUç³Ö7³Ip2·ªYÜ3UFsCðjÏ. ³eÆÖõ7×ü½fs!Øò|uY¿Z8lF?Wzp Ø|Ö2¾C¡ÄÜZlÅ"\E­1Ûø&Që²+[f¶A ±Â¼+ÍZÉ·ÏÆ-BÁ·þÊÚ`Ù E6?¹òp[=o9Úß8·¬ïoè^oRªgÿ'á<4»bíq3_^³¾£s°ÆoË|¡e¦§ãËkUbæÊsá\S|ÉÑÛdÕn¼m÷Y>½¼ö¨mJaÅÉÆâÀG¨õmûë`õ±)>Äë	ç©8ÔÕä24t4*»êÍãËï!}â0éþ*ê2ÏY¹y946¿üH. 2V»/ò[P>6ÎÎð¦ØçÆ¹ÚWÏÈÍª½ÉvC^T¤ð>CßÕ*ÍÂ4Fº¦Q¨õcøòå+. ÈÍÍFÂ |j½N§9'dÐsAßêÃ§)/R6Ò[X9ééiiQ©qIñ¡	=j©+. Þ7.ÖÖ£tçL@(aúh^²'è;II OL²äÄkH^©ì Wù#-		q¹¹ãÆfO¤Ä¤¤Ô´â<k^þ¸jYûNv[Ã{Ô\È8ÎRm9`ÝYÒôü´±ÙÔ£wëY©!V=±´ Á^¢Oa³d&Úc3K3ãCFjÍNÖsJK'ÆÚð¸¸ØÌÄLNIÉ¥-!IjfIfÈôN½ø=5}rlUsïz×¯û­SÎ®º#ª3®÷ÄÆ[nÌÐ3N_¯g½¹vÁ=-7Õî~}Þdõ3mÃË/³«ßxãÔø{jYî3oÇ½ß³ÄXØë½ug;¯e ~=³©wÉ¦=óªZt[Ëw/6FÍ}·ì¶ìÁK.ßùôWbHr¶. ?/<. JMJÊÒ­cá=~r^:!0.1.;5ZÏÌèQ'ºÂòÇE6ëlÔº¬£ì(Ã=VÒÃSÇpÇäæ# |
| --- | Minor | eV¼Ç½@qI1ÜUût KEä¾;V·ÛÃ°S»ÃÂá¸Èét.íÑó¡¹­á üRTlJrÿpâ~	:!{Òtg><2:'Ök·äP<L |
| --- | Minor | âD{âÄ ¸¤ ÀàñMÆwO)b½4mÍÎáæo7ymJ./eÜGJßv?¯æ_\^Ì=3R2>»4Ä2aB¨5\çuääÄ¢Ç¥g±bMÉ­§«Y. §¸d-!ÕñÂ¸IOt` ÃCb¹Õñ¨÷çÄ£Ò_É÷µ ©£ö«ã);£Xo5s þsÌ¯Éü[È£§ýó?{ðÙ¿~vö¸ÄÐÝâcÌå<tÿÖÿëg§2ãZúW%A	 H A	 H A	 H A	 H A	 H A	 H A	 Hðßfi	 H A	 ¬O³¬0Òy+(Us8  æ$_5ó Ð/Í¼J6HóÚ¢è}3o¡húÌÌÐbºÊÌ÷Aâ¯i*Æd¿ykÅ>y¨ÿJäCx½ò²Èü	r^å¬gdh·y¢µïyJµëÌ¼6DF§ÚfÞB#µ·Ì|ýXÝkæC©H­6óaôGís3Nd}f>JõwÍ|$µä£"þåR3MKâ E>|Èz#øZâîùÈ!õÑ<ÔßÊ×÷G>.îUO"(ìÌ' |
| --- | Minor | ©O}-ò61WpÌ´!2Cò£ü§"?^äýCè:düÈ!õ¦þ-K[¼-745 |
| --- | Minor | cq[û¥Í^cLùX£Ðé. _TPP`¸.i0f´µ¶y×´7åmím |
| --- | Minor | ¶Ö<Ã½b!ºx&OSÇª¦FTv´4¬xÒhñ |
| --- | Minor | ·£¡±ieCÇr£m1§¹éã«[7+Ö0ÐÒ·©jµ´:¼ |
| --- | Minor | ;Z<-¹¼'o`ñÁÙ¹­-Û1üìYMK;W4tÌkêðð¡ó. |
| --- | Minor | Sentence exceeds complexity threshold, split for readability. Applying the split needs --strength moderate or higher. |
| --- | Minor | none (split proposal only; source not rewritten) |
| --- | Minor | none |
| --- | Minor | Check: NEEDS-LLM |
| --- | Minor | Flags:    not-assessed |
| --- | Minor | SENTENCE (Line 1848, 482 words, 5 clauses)  [Script] |
| --- | Minor | ¯2¦ÈÙs¡ÚÖ&£½£­±s±×XÔÑÖÉ×ím3Ö´uÖÞf,ÇXÙ´rÆáº÷Ï®m­Þþ®| oSÃÊIÆ4ÌÑÊ |
| --- | Minor | kT®ÚÆ´mM+=+rËPoLkK ÒØ`@ÛK:oXÙ ñËÚ<Í |
| --- | Minor | ÆMkr«V¬hXÜdLoË5ªVby3Z=m¹ÆloÓ*¬²Áëmò´¡çæ¶ |
| --- | Minor | ­MyQtµQ­¤ZA­´¥E´EQ-Cù3Ð`ûj¦òÖëÉ´6¢fxÚZ ßr-A:CÚ »Ú!#z»!Ù"F4plp	/J-à¼u)ê¹t³(-óBº_Ïi@¢Môñ ¹ÕÈ{~|v®)RË>³ÅL\ëÚH¹¨wæEG§îP»ÕCêÐ~õúU@b©¥n0WÍÇá#õjÞBªµ¡r^HN`1ÇØ¹ |
| --- | Minor | bm |
| --- | Minor | °^|Íí"móq<Ñ+hÁY<¢ÔÎW±Jè7ÌÆÏ¡ôÍ+ÆäÖX)l°|ÀWý6ûgõá6oÖmF¶|èÁ5Z*fõ ½Ö úf±¨é÷¸8ëºz ÃGëßu¯Ëøsâç\ÏgÙ;ÑÎWx®á[x <8ÎðQø3Ms35 +óºVò,±Wk¸Â´CÓ#âªFØªC´´ÛÏFÚiî±>*ÏÛICãÒý1g W!<²Zh±åðä1cÐáïõm4ïÉgY=x ú=?¨Opw¬òAMx¬0=ØjÞ ´h{¶Ix<rêÌÙÑ¾JÈñxìßWÁ9½ÿÀ21£n£óS½ÅÔ¬CÄ{¨ç;rXßa½´W¹.n±¦!£ôË¯Ñ<!øYµxM­i5G¾T±ªáj{êü¨8æÁópØÝH­í£yÿntäçÎ 1£gç}ôÓð³['8«GÃÏànýg|n±Ø*NÈà~ïèæÝÔ6pb |
| --- | Minor | %r¤;Ämp}ÞÿÔR\»büþ¸j6ÞjáÿåÂCoþÛ{P² |
| --- | Minor | ­b'v óñÖÔkht÷ß+AûÞ³ýw¡úG+KÅÚÏ÷\xtêÄØý«	¾U÷Wë9>è8ïVîÙ#î~57ã*È5A£Ásàñ~ÿxÁ=É÷ê*Ó{¬¼óý´Öàkk±óü}<øÞnë%ÿ%m­|þû_ Ã5 ®GÐ¤æâüw£¶&ÐDÜÿqw |Kq.U# Ú±7×DÔM¤R*ÁSÿ¨Uæ:Ï]ËÐ¹ÿ´çQÙ Îµó÷T»8ÌÞ«DÔµgGÿÞhÂZ |
| --- | Minor | æíoË?Gçá·*§ËÍj+ÒEÂ¦ÁXíi°~§¹¶+Ä¹ÁlóÑÕljºdàönïSÿN¦æYX©Ç¼Gþ¥k¬°o»8¿=â,Èú.øf|K»{Ì]<Ãyßñ=á©SôPCÏ´¦aýÎ=%<CbºÃj.±Âìk~+u±yÝ |
| --- | Minor | =<âðuA[uûùÿEÆýï&ó%gcS~k}%,Ñ`Zs±èÕh |
| --- | Minor | {ã3!ß"4ôiï×¢ÿU¼fH¯F3oéÁ^âDË¶Ãú­ß!n nÂ«Ì=Ø$ÞîÿJ6§ÊàÙÖ(vc0:ZÎ¯1®1ðRè{µöx<ß |
| --- | Minor | ¦ZÄ*n¶!'Pð:ÇÜÓÁn ¶ýËlò¾+þ_ÿùL¿a-Ù_þPü¦Ñ4ì7¦a¿_´t­P«Ö.Ñ.Bêtx6 Íø7b8éx/W8#Îª±´ öCr± |
| --- | Minor | 8ÓÕÃ6¸f9ÿýxRòÈw~díI¶kÛÖ®[«N];s­²öÆÔÿêW­F²²É6 MÍ	¶uÍ÷4¿ÕüïÍZAËhbMÍ®êIº¡<5s |
| --- | Minor | qôX2±ñÎRwe añ8¿ê0z,IþÔO´ ò èH3<.Áé`	M)'fIÀÀc;ÕR%ÝAhKÅ >Ö2ÎâÀ²ìQlrEÂü÷lCÿ£?.Õé³(z/iP%LÿTrè2ù)Ö?ÅFþi Éæ¼ô þ)ÿ[ïó'§:é'õOÔ_ôORøÇ8ÝI~\¬0[ Çtú`{ßqý£@d4V¨Øs<.ÙáN×ÿ@·©ÿýsýýEêïë¿Ó? |
| --- | Minor | ¯2¦ÈÙs¡ÚÖ&£½£­±s±×XÔÑÖÉ×ím3Ö´uÖÞf. ÇXÙ´rÆáº÷Ï®m­Þþ®| oSÃÊIÆ4ÌÑÊ |
| --- | Minor | kT®ÚÆ´mM+=+rËPoLkK ÒØ`@ÛK:oXÙ ñËÚ<Í |
| --- | Minor | ÆMkr«V¬hXÜdLoË5ªVby3Z=m¹ÆloÓ*¬²Áëmò´¡çæ¶ |
| --- | Minor | ­MyQtµQ­¤ZA­´¥E´EQ-Cù3Ð`ûj¦òÖëÉ´6¢fxÚZ ßr-A:CÚ »Ú!#z»!Ù"F4plp	/J-à¼u)ê¹t³(-óBº_Ïi@¢Môñ ¹ÕÈ{~|v®)RË>³ÅL\ëÚH¹¨wæEG§îP»ÕCêÐ~õúU@b©¥n0WÍÇá#õjÞBªµ¡r^HN`1ÇØ¹ |
| --- | Minor | bm |
| --- | Minor | °^|Íí"móq<Ñ+hÁY<¢ÔÎW±Jè7ÌÆÏ¡ôÍ+ÆäÖX)l°|ÀWý6ûgõá6oÖmF¶|èÁ5Z*fõ ½Ö úf±¨é÷¸8ëºz ÃGëßu¯Ëøsâç\ÏgÙ;ÑÎWx®á[x <8ÎðQø3Ms35 +óºVò. ±Wk¸Â´CÓ#âªFØªC´´ÛÏFÚiî±>*ÏÛICãÒý1g W!<²Zh±åðä1cÐáïõm4ïÉgY=x ú=?¨Opw¬òAMx¬0=ØjÞ ´h{¶Ix<rêÌÙÑ¾JÈñxìßWÁ9½ÿÀ21£n£óS½ÅÔ¬CÄ{¨ç;rXßa½´W¹.n±¦!£ôË¯Ñ<!øYµxM­i5G¾T±ªáj{êü¨8æÁópØÝH­í£yÿntäçÎ 1£gç}ôÓð³['8«GÃÏànýg|n±Ø*NÈà~ïèæÝÔ6pb |
| --- | Minor | %r¤;Ämp}ÞÿÔR\»büþ¸j6ÞjáÿåÂCoþÛ{P² |
| --- | Minor | ­b'v óñÖÔkht÷ß+AûÞ³ýw¡úG+KÅÚÏ÷\xtêÄØý«	¾U÷Wë9>è8ïVîÙ#î~57ã*È5A£Ásàñ~ÿxÁ=É÷ê*Ó{¬¼óý´Öàkk±óü}<øÞnë%ÿ%m­|þû_ Ã5 ®GÐ¤æâüw£¶&ÐDÜÿqw |Kq.U# Ú±7×DÔM¤R*ÁSÿ¨Uæ:Ï]ËÐ¹ÿ´çQÙ Îµó÷T»8ÌÞ«DÔµgGÿÞhÂZ |
| --- | Minor | æíoË?Gçá·*§ËÍj+ÒEÂ¦ÁXíi°~§¹¶+Ä¹ÁlóÑÕljºdàönïSÿN¦æYX©Ç¼Gþ¥k¬°o»8¿=â. Èú.øf|K»{Ì]<Ãyßñ=á©SôPCÏ´¦aýÎ=%<CbºÃj.±Âìk~+u±yÝ |
| --- | Minor | =<âðuA[uûùÿEÆýï&ó%gcS~k}%. Ñ`Zs±èÕh |
| --- | Minor | {ã3!ß"4ôiï×¢ÿU¼fH¯F3oéÁ^âDË¶Ãú­ß!n nÂ«Ì=Ø$ÞîÿJ6§ÊàÙÖ(vc0:ZÎ¯1®1ðRè{µöx<ß |
| --- | Minor | ¦ZÄ*n¶!'Pð:ÇÜÓÁn ¶ýËlò¾+þ_ÿùL¿a-Ù_þPü¦Ñ4ì7¦a¿_´t­P«Ö.Ñ.Bêtx6 Íø7b8éx/W8#Îª±´ öCr± |
| --- | Minor | 8ÓÕÃ6¸f9ÿýxRòÈw~díI¶kÛÖ®[«N];s­²öÆÔÿêW­F²²É6 MÍ	¶uÍ÷4¿ÕüïÍZAËhbMÍ®êIº¡<5s |
| --- | Minor | qôX2±ñÎRwe añ8¿ê0z. IþÔO´ ò èH3<.Áé`	M)'fIÀÀc;ÕR%ÝAhKÅ >Ö2ÎâÀ²ìQlrEÂü÷lCÿ£?.Õé³(z/iP%LÿTrè2ù)Ö?ÅFþi Éæ¼ô þ)ÿ[ïó'§:é'õOÔ_ôORøÇ8ÝI~\¬0[ Çtú`{ßqý£@d4V¨Øs<.ÙáN×ÿ@·©ÿýsýýEêïë¿Ó?. |
| --- | Minor | Sentence exceeds complexity threshold, split for readability. Applying the split needs --strength moderate or higher. |
| --- | Minor | none (split proposal only; source not rewritten) |
| --- | Minor | none |
| --- | Minor | Check: NEEDS-LLM |
| --- | Minor | Flags:    not-assessed |
| --- | Minor | SENTENCE (Line 1848, 808 words, 14 clauses)  [Script] |
| --- | Minor | HÊ×ß'¦ÿUÿVÿEéÖ¿Ô¿Qßç×¯¸ãõ}ôH¡qún¥?C@5úÃTjYÈ¥ï$pÚÜáúª?Dûô½ô5H£}G 1a£ïñOtÁTºOßÆuÖ÷üA?`òmúfx¶ømN¾%ÀG¸?`MpVÖïíÖèOCé§õí0Xµ;BßNóAËA*íDÊúÞÖ·bb¨º¾ËSý9}³0àãbØis`¢Ó)¸Åç¸×9ø¤÷òhpÐ_àQÎS}§¾Kÿw¾I¿Ðw¢öûúúS0Ø#ú£úcÕwT¿%ãpêîHýtýZ¤á:g¢·èúÓ3mîd½®-­mé4Z_JõT |
| --- | Minor | ~H}ëÎµõe°S¯	FI] ¨ë^çGtÒWè5Â5úeA.ôGÇ¢~¡~-Æpè3õYØ&;é³h/ïò@f6ay .óF^s¿Þ¤_¾{y^ëOÚËô7¥¬h­Ó]¦·êm­·ë×Q¡DÔÏó´%nDêEi#øSFG@¶" [a Üÿ¢Gr h2×\BOèÍÃ¥_âîú\}~¼P¥_¢O,ú\h©éUèÇi.æKtzé¯Pû9¸ÑæÈTæ#_¾|¯ ¹¦7èôÅðç|}~ |
| --- | Minor | ¶»MÐONÐtíàÂúEØZÑV +ûçûõ)ºû¶H7°#`d:§ÑÇÀucõQÂ9zvP¨Èod£Ó(E8f¹#²ýÝíT¨gReê¼>8¤Ân§,1]»P·SHÑÇëyz>ì®gè¸S¤OÆzõ	z	¿õñÐ>L;I7h¡.Ðïõ0úFç(+A©´ô =RuþW«UzÝ©ó¿SMÒNÀ10tý 	Çæ§=ZûBÄjÉ#Áù¾5¹Åä:8?èÔ ö§`½öö{l;Q· uÎÐ\¢[µß£ìÐ5pÞOçò<ÁL£Eû"Ýôi¢ýYûRû"µ´µORjQHÑÎj½ZEiÕ¾ÕþÆ§½E/joÒw\{Ó?*ÈL33V§{ö¾ö?®µ÷´þ[íçÿZ{AðÓº¹vÚÏMþÍ/VwH{UðhüÄrh¯¡kï×^ð:ÂÝ#µßÓ~BPû®öhýöS1ÊO!àÒ~lözIüÕÓ¡½0ìvw´v4¼hN¿ßä=Z7«Ì2ÓÚ>¦¼l2@ÓAªöCíGØëV-,`íÔÜñÚ# zôèsÐi4¤s@JßQí@\ÓêNÔ¥ÐzÐNFG¾ |
| --- | Minor | HÕvkS*æzX=íÎXç¡=D÷=:zdÌ.Ôî©Fiß£Û@ïÔ¾·µaÑÎùèú ª>ÐIFÚ²pèiÛÉªµÖtmâ¯ÎLpÛµ{(ÔR±Ð{ 5 õ Í Ý (ÙB{A =¡má6kYþqîí>Ìy{MííYÕi¨¹5wbùZÆØ¨EûÓ2þrP»Kü¹{S 9Í×Ý |
| --- | Minor | »!y7úÞM76,°òð8'¹c´;øi¨ÝN 9 ­ O@ºöö¤TF»;N{2E:A»R·´´¤cÁ7ù§_é<¤Ý¤eQ ~¶Ø?6£ÑmÕnèÐó6¤[En«v3¬q³°ímþèv-ºÝeÍqçh«Ðmæ\¯¢ã ±Õ	-ñm |
| --- | Minor | '´ÕÂÿ|-x:ø |
| --- | Minor | &_còëµÕþô ßjh¾Z¨²+ù\kCÔrTlÉö@Xs¹»Vë µ ª5læ¡ Ó |
| --- | Minor | ìÁ@¬ÃÏ×VÐr¨nETó´ååÈ5jK®K{é'"7_[KP¿ýj-üÁ 5Ó_\3µïRèa® ¤ù Í # é0ÀbôÙt/-1#¹Çhá¡z(½ª5`ªXÊB,b!º,D jÚ,bvÃÚ£]^å@ù°Ê E _-â¨.éÜyD«ÃDu½:Øè¨6Æ?f¬GcºÆÿGZx¸	îÏn><<{lLCý,?^´,A |
| --- | Minor | *j	æá¨áSDó)"ÁÀ£Lþ}p+ø$ðXp>U8*OÀJÌ8"Ã|yü].Ú£f¿ú7õ[H»UýbÔ¿¾¥äó}ú+è[êûðá÷ñIb¨§©_«¡Dõ[´&RÚÝ£òb*Ò  6ÐNÐ^"µíIj7yA }é"÷ z#~¬>ËÏ`õ#õ·h?0ù/Õçø¯¾cò·L~@ý¡à/å«¯¾?Xî;®>çwRÃ@Qñ¿ÄÉo!d²ry_ý e"¶Cq*q_ô(EN|Ë«Môô ÇJpRÆR=oSö©?,ÖÙÃ> |
| --- | Minor | <¯:\î0ö¶éB*?ïQÂ£1þMáRöù±âý}GÙø@jº3ßËÆÓzÐqPH#©t¤"e®ÑÌÕÇê{w÷¾Ý{¼÷d¯^p¶þìæ³GÏjt¦àLýÍg´3ÓÆdF`¹W |
| --- | Minor | ´´¤)³åã3î8e?.WøGÀ>åç(³ÉÚR\sV»ü9¢\t?ôs¢\©TòøSfkÂÜQRe°f2Ö_'@¡	yf&®\¤LÁ»ìôAe ¬T¬ùG9lî<¥sé¤Õ /h=ÈÒi·ûtC©jµÓJ!ú7"õö)üe¹ÔFÓ¦/ýðe:?pXJäÿlÊPR@©ðR (jÀkÀëÁëÁÛÁÛÁÃé/ìÌó0ûû}èËxø ûgÙsx£Þs= â )\ý@ 4ó*aV	ûE$ô¸&!\_fv~¹MqÐGÌõkóñ=cýcì±=ªcý£ìÑGtÇ#<»í£=Ö=õ{Ú÷hîR¥W9%<tU9Î7ÜiRN Þ«üIlÞ)j)W'óò$p´«NÃ«êD|Z%)îêH5MHÚÔ41B¼+8p^o5yY­Æâ¸PÜéOy^èò¼òçgEùYe¯àÏóú§MþÉTö07¹£ |
| --- | Minor |  T²(·¶hr»[h*H!«: @õ 1N·öT¤ü÷«¤ FÐm }ÁNð#G½R!VVÎW0ÓäWürW«^j§«ü3Yéaü÷jÖãßÂÙaÿ­ Ø!ÿÎú×é`ûý7éw8ÛÄnF$9Ø]l½àw°Ûñ_xÝ8ºÝfüa1§£e~[>ÙÖÌ·kf¸¶l&ïÁCoV«Dÿü2ø13ÙåfâD¦Ì?­Rd&ögJÈ¸(/¢ãXÃWÄÆ°hãêa9¢bþãf?=Ç]+Áúê+ã |
| --- | Minor | ,q+Èuß¸\ç}[TGOßÑÀ½-NÁë®	òs9ÿÁ½îK÷n	ç2®¼-%¥Î-Ûãîmºc×ºÃµ3-ÃézÉNÔ<ºô h;wIÝïtmË+@bd!ÁZfna3d¸Ù¾§îNØ	Î²CÝ%6ZÝ¦nîÜ Î[î3ù½êî®CÊæù³r«ÅÅqÒoð,åØ4¼á	å>ò88/ï1ùcàåQï6ùÃ¦üCÊ#<p1â#þN§;]-RsÅö+ç:s]òMgòñà<&§æòÕìï;L,¿þSÔT!¬¦oãÔÀt§âSÃÔaPp.a1¹nÖkjSåÖÀp8Wiâ÷oÛa¥îù@ªZï?hUÙ¬À!þ#ûß>_ìWDç¨#ìW4ô	He?W²q¢rT²±©²±Í²ÅÖ%.,\÷YâÖ1pügc¤£@·Tö)~»bïÂ#nþ¯]q;±cÔRè=ö&. |
| --- | Minor | HÊ×ß'¦ÿUÿVÿEéÖ¿Ô¿Qßç×¯¸ãõ}ôH¡qún¥?C@5úÃTjYÈ¥ï$pÚÜáúª?Dûô½ô5H£}G 1a£ïñOtÁTºOßÆuÖ÷üA?`òmúfx¶ømN¾%ÀG¸?`MpVÖïíÖèOCé§õí0Xµ;BßNóAËA*íDÊúÞÖ·bb¨º¾ËSý9}³0àãbØis`¢Ó)¸Åç¸×9ø¤÷òhpÐ_àQÎS}§¾Kÿw¾I¿Ðw¢öûúúS0Ø#ú£úcÕwT¿%ãpêîHýtýZ¤á:g¢·èúÓ3mîd½®-­mé4Z_JõT |
| --- | Minor | ~H}ëÎµõe°S¯	FI] ¨ë^çGtÒWè5Â5úeA.ôGÇ¢~¡~-Æpè3õYØ&;é³h/ïò@f6ay .óF^s¿Þ¤_¾{y^ëOÚËô7¥¬h­Ó]¦·êm­·ë×Q¡DÔÏó´%nDêEi#øSFG@¶" [a Üÿ¢Gr h2×\BOèÍÃ¥_âîú\}~¼P¥_¢O. ú\h©éUèÇi.æKtzé¯Pû9¸ÑæÈTæ#_¾|¯ ¹¦7èôÅðç|}~ |
| --- | Minor | ¶»MÐONÐtíàÂúEØZÑV +ûçûõ)ºû¶H7°#`d:§ÑÇÀucõQÂ9zvP¨Èod£Ó(E8f¹#²ýÝíT¨gReê¼>8¤Ân§. 1]»P·SHÑÇëyz>ì®gè¸S¤OÆzõ	z	¿õñÐ>L;I7h¡.Ðïõ0úFç(+A©´ô =RuþW«UzÝ©ó¿SMÒNÀ10tý 	Çæ§=ZûBÄjÉ#Áù¾5¹Åä:8?èÔ ö§`½öö{l;Q· uÎÐ\¢[µß£ìÐ5pÞOçò<ÁL£Eû"Ýôi¢ýYûRû"µ´µORjQHÑÎj½ZEiÕ¾ÕþÆ§½E/joÒw\{Ó?*ÈL33V§{ö¾ö?®µ÷´þ[íçÿZ{AðÓº¹vÚÏMþÍ/VwH{UðhüÄrh¯¡kï×^ð:ÂÝ#µßÓ~BPû®öhýöS1ÊO!àÒ~lözIüÕÓ¡½0ìvw´v4¼hN¿ßä=Z7«Ì2ÓÚ>¦¼l2@ÓAªöCíGØëV-. `íÔÜñÚ# zôèsÐi4¤s@JßQí@\ÓêNÔ¥ÐzÐNFG¾ |
| --- | Minor | HÕvkS*æzX=íÎXç¡=D÷=:zdÌ.Ôî©Fiß£Û@ïÔ¾·µaÑÎùèú ª>ÐIFÚ²pèiÛÉªµÖtmâ¯ÎLpÛµ{(ÔR±Ð{ 5 õ Í Ý (ÙB{A =¡má6kYþqîí>Ìy{MííYÕi¨¹5wbùZÆØ¨EûÓ2þrP»Kü¹{S 9Í×Ý |
| --- | Minor | »!y7úÞM76. °òð8'¹c´;øi¨ÝN 9 ­ O@ºöö¤TF»;N{2E:A»R·´´¤cÁ7ù§_é<¤Ý¤eQ ~¶Ø?6£ÑmÕnèÐó6¤[En«v3¬q³°ímþèv-ºÝeÍqçh«Ðmæ\¯¢ã ±Õ	-ñm |
| --- | Minor | '´ÕÂÿ|-x:ø |
| --- | Minor | &_còëµÕþô ßjh¾Z¨²+ù\kCÔrTlÉö@Xs¹»Vë µ ª5læ¡ Ó |
| --- | Minor | ìÁ@¬ÃÏ×VÐr¨nETó´ååÈ5jK®K{é'"7_[KP¿ýj-üÁ 5Ó_\3µïRèa® ¤ù Í # é0ÀbôÙt/-1#¹Çhá¡z(½ª5`ªXÊB. b!º. D jÚ. bvÃÚ£]^å@ù°Ê E _-â¨.éÜyD«ÃDu½:Øè¨6Æ?f¬GcºÆÿGZx¸	îÏn><<{lLCý. ?^´. A |
| --- | Minor | *j	æá¨áSDó)"ÁÀ£Lþ}p+ø$ðXp>U8*OÀJÌ8"Ã|yü].Ú£f¿ú7õ[H»UýbÔ¿¾¥äó}ú+è[êûðá÷ñIb¨§©_«¡Dõ[´&RÚÝ£òb*Ò  6ÐNÐ^"µíIj7yA }é"÷ z#~¬>ËÏ`õ#õ·h?0ù/Õçø¯¾cò·L~@ý¡à/å«¯¾?Xî;®>çwRÃ@Qñ¿ÄÉo!d²ry_ý e"¶Cq*q_ô(EN|Ë«Môô ÇJpRÆR=oSö©?. ÖÙÃ> |
| --- | Minor | <¯:\î0ö¶éB*?ïQÂ£1þMáRöù±âý}GÙø@jº3ßËÆÓzÐqPH#©t¤"e®ÑÌÕÇê{w÷¾Ý{¼÷d¯^p¶þìæ³GÏjt¦àLýÍg´3ÓÆdF`¹W |
| --- | Minor | ´´¤)³åã3î8e?.WøGÀ>åç(³ÉÚR\sV»ü9¢\t?ôs¢\©TòøSfkÂÜQRe°f2Ö_'@¡	yf&®\¤LÁ»ìôAe ¬T¬ùG9lî<¥sé¤Õ /h=ÈÒi·ûtC©jµÓJ!ú7"õö)üe¹ÔFÓ¦/ýðe:?pXJäÿlÊPR@©ðR (jÀkÀëÁëÁÛÁÛÁÃé/ìÌó0ûû}èËxø ûgÙsx£Þs= â )\ý@ 4ó*aV	ûE$ô¸&!\_fv~¹MqÐGÌõkóñ=cýcì±=ªcý£ìÑGtÇ#<»í£=Ö=õ{Ú÷hîR¥W9%<tU9Î7ÜiRN Þ«üIlÞ)j)W'óò$p´«NÃ«êD|Z%)îêH5MHÚÔ41B¼+8p^o5yY­Æâ¸PÜéOy^èò¼òçgEùYe¯àÏóú§MþÉTö07¹£ |
| --- | Minor |  T²(·¶hr»[h*H!«: @õ 1N·öT¤ü÷«¤ FÐm }ÁNð#G½R!VVÎW0ÓäWürW«^j§«ü3Yéaü÷jÖãßÂÙaÿ­ Ø!ÿÎú×é`ûý7éw8ÛÄnF$9Ø]l½àw°Ûñ_xÝ8ºÝfüa1§£e~[>ÙÖÌ·kf¸¶l&ïÁCoV«Dÿü2ø13ÙåfâD¦Ì?­Rd&ögJÈ¸(/¢ãXÃWÄÆ°hãêa9¢bþãf?=Ç]+Áúê+ã. q+Èuß¸\ç}[TGOßÑÀ½-NÁë®	òs9ÿÁ½îK÷n	ç2®¼-%¥Î-Ûãîmºc×ºÃµ3-ÃézÉNÔ<ºô h;wIÝïtmË+@bd!ÁZfna3d¸Ù¾§îNØ	Î²CÝ%6ZÝ¦nîÜ Î[î3ù½êî®CÊæù³r«ÅÅqÒoð. åØ4¼á	å>ò88/ï1ùcàåQï6ùÃ¦üCÊ#<p1â#þN§;]-RsÅö+ç:s]òMgòñà<&§æòÕìï;L. ¿þSÔT!¬¦oãÔÀt§âSÃÔaPp.a1¹nÖkjSåÖÀp8Wiâ÷oÛa¥îù@ªZï?hUÙ¬À!þ#ûß>_ìWDç¨#ìW4ô	He?W²q¢rT²±©²±Í²ÅÖ%.. \÷YâÖ1pügc¤£@·Tö)~»bïÂ#nþ¯]q;±cÔRè=ö&.. |
| --- | Minor | Sentence exceeds complexity threshold, split for readability. Applying the split needs --strength moderate or higher. |
| --- | Minor | none (split proposal only; source not rewritten) |
| --- | Minor | none |
| --- | Minor | Check: NEEDS-LLM |
| --- | Minor | Flags:    not-assessed |
| --- | Minor | SENTENCE (Line 1848, 1442 words, 24 clauses)  [Script] |
| --- | Minor | b½42Øçìöõ/±?Ðf"v;K½D­«RËÅb+M^Î0 |
| --- | Minor | ÞmrÉ§übµÜÏ6áìf&~0dëÁùÃë(»Ñ9JlýñIÎýì^ÆJ< ÙÍPµ§ì;ì&>»)°Aw÷0¿ ¬#È®ãì%Öofßqv] !ÉIØudáõÏÚý±|äN¶Z`ã/ØøØøØõ1çBw4«·RÖ3Ïzy,ðo§ËlL±ÙjäÏq6ÉyXÃ 33ÖafRG<¥xfªêT3ãlfpx3ãóÍef¸%y&îtVüXM³s2{`Åqä úÿQóGEêcüS¦Þ¯>Jí õ Í Ý è(èmP(îÇÑïqÜÓÐ@} Zöðô®>ÆÇEûcx< ¥ÑkÜN­¨D(fMtnF8ò; |
| --- | Minor | ®²áufCÜÙ`óH¹slþ£LùØ|ødñÈÅã}>ñ´äà §P=¨ý©x7©4éBPhèPÈQRcó¹«RüESáþ3ST#;<p{¸ÃêaabâÓ³¤GiÓayÍ¿§3S\ÕTÇéUÇÃ_±·×Õd<âØ`}¯°þHuÿû5m`»¹»¨G;áTÙ´1Üq'hãq#¬Z!nõ°*ç·à8¼¼sWû-cò·Ü¬9nëAßÝr­=×¹£ÜéoG<Ü¶AsÜÊÏ­ |
| --- | Minor | ªõmbbJibbIbÜÄâÄÈ¢Ä°ÂDKA¢Hy£s¢ÇäÄsDç:b²ìÑ£ì1éÑFFL;Ç¢ùQT¤ìNÖE£Äé û3ªÿÈþôB´+~lÐ&Ö±cMòµ±ã1ÖØÈÈ¨èÈ°ðHKHh¤ªé8#ÛF1#ëí,ÅUu4ëxÖÉ,÷;q´ã°¦Æ°õOªbciQ)!#¢­ÉQqZBTM1óÅUSõi¾x>{¯ØQÝ£³|Ej_hÍüÚnÆî®C­O¹£§°O»£G+¿z~mKåÍlxÁ2òU×oØT×­Ð4»Ãg]ËëÊZqGæÔv+lÍ§mª««óM¬®©åu4_c5D×§ÕùxfsZ9 O¼<CÔ:úî1£+}ã*|¹õCÙð¾à:&òx¼ÁzLog' ¢ÅÎ¿3hö¨n×îÇvºÿé |
| --- | Minor | kó»ûq¥pm`'Uqâ¼ÜoN£n^® ×Ècë1GTC%y·Àè±A8Â¹s?nr±N[P&.ÉùKQç5.¯µ¹G«cÕ,ñØcò5[Üq£MmÖÛM>Êä&7L¡fu³!6¨ë_±UÍ |
| --- | Minor | :­=àX±àX&çþÐ0'³ ÛùÇ;¸âòÚðùö?ð>ïäï£Í.8ÿSyd¬±bN¾F.KÏ0åâav*ázØâÏËw3F¦Ó´Ñ\¢s@q4îïâ1[v?1hs[i+Þ{@ûÄ§¯Þ%¸³àx>y½f¸æã¢í!õ2U|_CþôL¡Ï¿#/	àkú»!±lî0²à«Ù.öÏIH |
| --- | Minor | <ft×í÷aö ì |
| --- | Minor | Ëïí·ü^nyéö'ÙÁ·r`°ýÞÀ¸Ü úb¯éAgpÄg¸ByÆí¡ð¾	C!(V\0Ï¤È|LÍ¬MF_V©??è²Rþ<fbSÎ¾{¼|[yû÷<·»GX ß^lÛ½æ |
| --- | Minor | >^Åv27¸8¡Ç<<Èã`C*EÕpUÇ»_Ý§vW6÷¨ÏV¶4TÖ£ú+[|® |
| --- | Minor | }°W`JõhÑÖ¢íÃO¡acbÍS_ÌÏðÿ5O6ó4%QäL0^r%z¹rýÚvm;0¯rY:òá ì5MçÅÜÇ°@÷ÕB¼3hSrbv:ÄÜÞýÚií$ê÷Âõhÿ1hí½<Á3Ñ3¸joðX÷P§é&3½æÌ¦=,ÎíJ¾ï?¸I,z¨¹AL±a×uÜ&ÜÅ^1·s`QL(ÁçKñàEu§g`»ñ¹<Cw¿£;_¯5³¦á%îYß; ¯¡PB$/4Îòévq!£¾¶ÛÂ¦uÐ´îpðfcÝDIÖî*jï¦ª{´Ô£¬ôE8|áèaFS§¦8¬SØªü²K¤ÏÚû´ºÿ«Ã³ endstream endobj 759 0 obj <</Subtype/CIDFontType0C/Filter/FlateDecode/Length 8383>> stream xÚ­z	xSeÚvB8¡@­ Fé9ø²"8¬¢lUZ6Ëf÷=mº¦I´I³äÍ¾u_Ò½éB7JE,»"¢à¸:n£3óóxúÍ÷´ è¥óóÍÿ·WÓ6í÷yîç¾ïçy3~<Ëå>ºãåÝi©Q¢g,Úã{r'=~úphK£gðèãÁ'ÛxÑÿí?ëÏëõ?ÎôOÇôbOr8\ø0û8nú£4ôÉþôÔÿÙ¾'óÃñÇár&qæ<ÁÎùÃpÇs'ýô~ëcÓ¢ã¶ÆÆ²²s.^²ä¹ié¹I	ÙAK,Y¶Ð÷¸*hÃâ mQ1Â4I0)(J´mqÐËv¦IØgæ§¢ã£RâÒâöÆígÅef%d¦Ó³,Ú$IË±ß3ãRâ¢²âbÄ¢Ø¸Ì ìÄ¸ Íûöì |
| --- | Minor | )M´#)&N´hQPPV\\PbvvúêgÉ',NËLx&ý¬gRÆþ)ëßºE/ìÜ»hÇÖÁ;÷/ÎfÅ§eÅÆeG%¥d-þuú}gZfjT ý Ø¸ÌäÌâ<Åy³³³óçYÎRÎ2ÎrÎ ÎJÎ*ÎjÎÎuõ |
| --- | Minor | 89[8Û8Û9;8/svrB9»8»9{8{9û8¯pösq"8(N4'Ëã sgä£È#µº@¹^qÊPì |
| --- | Minor | ¦FOÕJXJaµK	RmH0zp¥ÄQ	n )ò]ÌjLU)/Ò¢h]½¦îÎ#Ta-U ôKBá1ÌÜåÁ7«=ÙKtuåt]µ |
| --- | Minor | r²ª»äÄÍRPùòê½ÄaåùÖ!Xu¼Ø08ÔGkzNMt²zÃz<\/þÏ» ¥	>Þ2¸ÑP@Ó»¼ß½Âps/gwfÕ&GAVF2ÄH/¤T+7£tÀ }ÌG3Ñ4á{2}*XþÂiüKÈqØ`;&ño;7§»wO­ÅÌ#üh²YMN¼:0´ÿõd 7*&¼ÒßäÑ¨GðÏ!qI9Â ¦§Ñqø£ßAãÑDô-Ì¢ÈàýDfríÍcÎÄ'mõÐX^ã×ÛÒÝÑM8w£ÒÉ¢ídÀq±Ç»ÈÃEO}Êóò®Ì«z§@,ë±·"wU hFÈ"få?g#Â%p* F­JdÖîgÝ¾X±ìy©=ûG~yíËÁ÷<ý¡R¸Â	-.¡ÒF#ºßpsÑ¸ë(êNü^`QºZ½^¡Ö/Õæû2Ï4ý£ñyõÈPç áÐEÔ0âù®üº¦zw÷ÉÈ®íÌ#ÉÌ~ëgè±ÿVÎ¾þ¿à(í)CÜ4Äze^¸ókÓÉ©ÉUyöVð!ú£ .¿& |
| --- | Minor | ¦dWH;<m6QÿbÖå }?pÙõ<Ê>.h5 c2EÂ:EmMËl/Ø~8Æ¯Åº§L*[z=&O ÇËe¸åc·Þ&@³Vÿ æêîíB{P+»¡"&dù<°ûà¦¨5Äìû° =u:lvâ[þï3O?ÃÖcÛïÖc¹µD³èk·]L!æ)Hoz°RÝ#HQî\ó¥j¯Ó§UÎ|§HSz­N |
| --- | Minor | lÉ^ð|âA+<ÜKÞyÞ \EbY+»0`Wâ6fÁÜ·õ·P3ö)ÿ-?]¥/PH¨SRxZ]&c¼Òïn¬¤j!£¤Rñjb5ÿ"Òcív_ÐÐ£|ÄiHÝ®+¤²H½F_Ì¾Ëæ*#¨CÁX£I |
| --- | Minor | ~æÚ`Í0TC¨Ô>ÒþëÄÑYü¡ÜFþ	¥a£}ÿ1¤§»Ñêü·¦û7¡¾MþvO·sÀÖDöð[ß4U ßoWmø`|ÏöÌ¬¹Lð³'ÿyÜÈ.Á¬É Vögr½uéId¸Ùûp÷Û¡Ë¯¡Îðèb+h+n4µ-¶#»Æï¯'ßx¿µýh03nÞìy	eiÎB`Uô1~ÌÏKã+®¿rMA~>ÒåèÏÌ£Õ ê Ê^¼å+Üõø7ßxïLOò.°~ä1ÁekÙÑåóýõ8øè%¬A\' |
| --- | Minor | òÙÄ÷ A_Zñ¼atà¾ z º ì=jê<N |
| --- | Minor | X]RóI´¡Ñ\N^FìcþUGAz6_OêTzíXY¦©¶!Ál°Xp¢ õT®lÊÍÏ\I¬å_A%÷0ÿOwÊKYÊ&õùØÏ(ðQA»úZêAþXëæfÞFnóèýÞ©þèºèÌãI*ÃÃ¶úÊ[ÂM9y¿adbÑËhuN`²0,PHMår²ÕRV_»sùÄðþ®ïûPüKüö¿Ò	«X=Ï#×òÛÐr¬Ëî:s°×êòKÉT,K« |
| --- | Minor | Í5òûív#pË#áÒ/ÜàÑT%x?âÖs¯FçâÁ Ú\FÄ¡	:) ª®ÓÕhÜgÛÔFÒêuR®%"b"Ò¤Öµ+¢r|yU½â Îj3l6páÔk¢¯&qß^ÑÌruD¨8HØYó­ÔÐBtT·ÔÕe©Cú·~C8"ÐBO×ç Íý{ÞÀ£Eeº¤@-Th*7­4ä1ôf.FÞe RÕyZÅ¬ÞÐØW(rºâó (ÒA}!êi½GÝH®ÉÌ£ÿ&Æïyæ±¥ÁZÊOE	óòq­­Ðn-/±»Ýá°'ªj ¼<Ï,À´,ã9gu©«Î ºÐ\LoµC+Ñ|µ´øØdzÎ]t R]k))I02ÜI(Ù¤»Ø¤Ûù¥z})YKÙõ2\ËRR/ÕÉSÓüb#÷ÅW½ëÑ²ïßãE¤Å@ÿðý4óËw»ZÈ,;ÁEØ,û'Ð¬Îjt#J]¬ScùÅ/Úî¦gú´ÕI;Ko |
| --- | Minor | ´ÈÒ#	f<3ÏÌX~|óÍSý}%%dÎ¢ê´¤ÀÃ11°(L®t²Æ^R[Wgä¦ÈbcºroÿãÖ·ªA> cMÚÎµ{}º[®­hbíqòlÃ±âc¤dØ}uç\ÕÅEªê ´ ]¾`£//kp6ÚëÉ3}hü0þÑ^÷Á-©)à4ð¢ÅÌùÓëôrËÕµ¥.èGë-nk­Åè8b0VµùµÕô_¾N3ç¼ÁLÅITqÑpâ«´ÀÂRÀrû	²òÐmtH`´ZÝfÜÇD	ãKt°PKêÔ©/´Ã*öò«-°ÄÄþÈxå¡/ª%J(yÚ\ÚÌå tÖf·:Þ"j,³) ¢¢£#MÑªh;ZX£ cid¦ôaÉÊbå"§æÊm:ûúú©^ÂÆzyk |
| --- | Minor | ¬íyìÜñ×¦¾Ç^îý¡)ÓÞE(e¦ÆÒöÒ.ò zs¶íÕøkq |
| --- | Minor |  K |
| --- | Minor | ~5L¸\ì,¹H%%SWÆÏÇdqZ¹­>ýu;zÊ¦5ÑÚwªP"Wä´´µyÚØÍ»¯þy¸_Çóó.ør¨¤ðÃ¦¢¸è®bð+]PWEºÙ)ðÕV¿xltwð^":±¡OIêFh#ºÝ |
| --- | Minor | Ò*¾°ùlÌ¯¿¼ùDé¬Ùf³å®Ñ øôöÚ¥c;~å<ë-¥¿°Aû¥#t]]M­Ù`!-µÐP_nÚá ueµµM¿ó§{j{$£TD%^è6º«ºs;Â_I»·æç'æý^8í?c«­Ùa§PÖ¥¹³WA-%Ú<¨Ràgvs·W»»»ì¢	ÃÑ%ú<Ï;é¬©¡ôT #?f	kkî³Óé>ÖZN_x«Kä,´ÂS¯FGbuáxPzßm0TZÉ[H<+w{G¹__à¡ö»ÁÔ¨¡L,8OöÙJæÑ Ók5ü#ñ'ºkJAegÙvÓH:¶ë7~|çýmtUP²ÚÚÇª§­»ý2Që¸«Ìc|1ÅÉ|5ri=¹u:E0¿å»)í+ ×*åúÜb+e#[;L¶NÊ3Úã¨Eän£®±7A«¹ @º3ð/|å¡ª(µØ\Vèå²O33F.ÿÚ¹tõº»û¨.ÂæëÐ±FÙ;ÕG{Þönïª9| ""¼¥«'B&¿DT%µF	ìÔ|RS¸âcukp[Àõªê¢äù5Dë3N­×P¸Ü^PSRi«¶^ôÜ],=	%µ~C-ýÃopAºJ¤+&·1¥ÿE¿GïÞÅ­×Ãó~å]zW8)¡0ÉBhX ÊzyZgäàÅ:N	q#Ûº«Pë |
| --- | Minor | óèO¹³J)JA2ÓFd{ã_}ðÜ	è$ù+°teËÌZCÑ+®3µM%J2 h,?ôh~èTV ÿ99 |
| --- | Minor | -~õe7oý[]7w}ðÝÀE«n óU=D zyyÊöÄóÃñhÂc½Ç= cFfHÄ¿Ca/iI¶BòÙÔkÁËUI¹¢WÓ/}sûÃ7¿¡e(ø¾í`c 5	 . |
| --- | Minor | b½42Øçìöõ/±?Ðf"v;K½D­«RËÅb+M^Î0 |
| --- | Minor | ÞmrÉ§übµÜÏ6áìf&~0dëÁùÃë(»Ñ9JlýñIÎýì^ÆJ< ÙÍPµ§ì;ì&>»)°Aw÷0¿ ¬#È®ãì%Öofßqv] !ÉIØudáõÏÚý±|äN¶Z`ã/ØøØøØõ1çBw4«·RÖ3Ïzy. ðo§ËlL±ÙjäÏq6ÉyXÃ 33ÖafRG<¥xfªêT3ãlfpx3ãóÍef¸%y&îtVüXM³s2{`Åqä úÿQóGEêcüS¦Þ¯>Jí õ Í Ý è(èmP(îÇÑïqÜÓÐ@} Zöðô®>ÆÇEûcx< ¥ÑkÜN­¨D(fMtnF8ò; |
| --- | Minor | ®²áufCÜÙ`óH¹slþ£LùØ|ødñÈÅã}>ñ´äà §P=¨ý©x7©4éBPhèPÈQRcó¹«RüESáþ3ST#;<p{¸ÃêaabâÓ³¤GiÓayÍ¿§3S\ÕTÇéUÇÃ_±·×Õd<âØ`}¯°þHuÿû5m`»¹»¨G;áTÙ´1Üq'hãq#¬Z!nõ°*ç·à8¼¼sWû-cò·Ü¬9nëAßÝr­=×¹£ÜéoG<Ü¶AsÜÊÏ­ |
| --- | Minor | ªõmbbJibbIbÜÄâÄÈ¢Ä°ÂDKA¢Hy£s¢ÇäÄsDç:b²ìÑ£ì1éÑFFL;Ç¢ùQT¤ìNÖE£Äé û3ªÿÈþôB´+~lÐ&Ö±cMòµ±ã1ÖØÈÈ¨èÈ°ðHKHh¤ªé8#ÛF1#ëí. ÅUu4ëxÖÉ. ÷;q´ã°¦Æ°õOªbciQ)!#¢­ÉQqZBTM1óÅUSõi¾x>{¯ØQÝ£³|Ej_hÍüÚnÆî®C­O¹£§°O»£G+¿z~mKåÍlxÁ2òU×oØT×­Ð4»Ãg]ËëÊZqGæÔv+lÍ§mª««óM¬®©åu4_c5D×§ÕùxfsZ9 O¼<CÔ:úî1£+}ã*|¹õCÙð¾à:&òx¼ÁzLog' ¢ÅÎ¿3hö¨n×îÇvºÿé |
| --- | Minor | kó»ûq¥pm`'Uqâ¼ÜoN£n^® ×Ècë1GTC%y·Àè±A8Â¹s?nr±N[P&.ÉùKQç5.¯µ¹G«cÕ. ñØcò5[Üq£MmÖÛM>Êä&7L¡fu³!6¨ë_±UÍ |
| --- | Minor | :­=àX±àX&çþÐ0'³ ÛùÇ;¸âòÚðùö?ð>ïäï£Í.8ÿSyd¬±bN¾F.KÏ0åâav*ázØâÏËw3F¦Ó´Ñ\¢s@q4îïâ1[v?1hs[i+Þ{@ûÄ§¯Þ%¸³àx>y½f¸æã¢í!õ2U|_CþôL¡Ï¿#/	àkú»!±lî0²à«Ù.öÏIH |
| --- | Minor | <ft×í÷aö ì |
| --- | Minor | Ëïí·ü^nyéö'ÙÁ·r`°ýÞÀ¸Ü úb¯éAgpÄg¸ByÆí¡ð¾	C!(V\0Ï¤È|LÍ¬MF_V©??è²Rþ<fbSÎ¾{¼|[yû÷<·»GX ß^lÛ½æ |
| --- | Minor | >^Åv27¸8¡Ç<<Èã`C*EÕpUÇ»_Ý§vW6÷¨ÏV¶4TÖ£ú+[|® |
| --- | Minor | }°W`JõhÑÖ¢íÃO¡acbÍS_ÌÏðÿ5O6ó4%QäL0^r%z¹rýÚvm;0¯rY:òá ì5MçÅÜÇ°@÷ÕB¼3hSrbv:ÄÜÞýÚií$ê÷Âõhÿ1hí½<Á3Ñ3¸joðX÷P§é&3½æÌ¦=. ÎíJ¾ï?¸I. z¨¹AL±a×uÜ&ÜÅ^1·s`QL(ÁçKñàEu§g`»ñ¹<Cw¿£;_¯5³¦á%îYß; ¯¡PB$/4Îòévq!£¾¶ÛÂ¦uÐ´îpðfcÝDIÖî*jï¦ª{´Ô£¬ôE8|áèaFS§¦8¬SØªü²K¤ÏÚû´ºÿ«Ã³ endstream endobj 759 0 obj <</Subtype/CIDFontType0C/Filter/FlateDecode/Length 8383>> stream xÚ­z	xSeÚvB8¡@­ Fé9ø²"8¬¢lUZ6Ëf÷=mº¦I´I³äÍ¾u_Ò½éB7JE. »"¢à¸:n£3óóxúÍ÷´ è¥óóÍÿ·WÓ6í÷yîç¾ïçy3~<Ëå>ºãåÝi©Q¢g. Úã{r'=~úphK£gðèãÁ'ÛxÑÿí?ëÏëõ?ÎôOÇôbOr8\ø0û8nú£4ôÉþôÔÿÙ¾'óÃñÇár&qæ<ÁÎùÃpÇs'ýô~ëcÓ¢ã¶ÆÆ²²s.^²ä¹ié¹I	ÙAK. Y¶Ð÷¸*hÃâ mQ1Â4I0)(J´mqÐËv¦IØgæ§¢ã£RâÒâöÆígÅef%d¦Ó³. Ú$IË±ß3ãRâ¢²âbÄ¢Ø¸Ì ìÄ¸ Íûöì |
| --- | Minor | )M´#)&N´hQPPV\\PbvvúêgÉ'. NËLx&ý¬gRÆþ)ëßºE/ìÜ»hÇÖÁ;÷/ÎfÅ§eÅÆeG%¥d-þuú}gZfjT ý Ø¸ÌäÌâ<Åy³³³óçYÎRÎ2ÎrÎ ÎJÎ*ÎjÎÎuõ |
| --- | Minor | 89[8Û8Û9;8/svrB9»8»9{8{9û8¯pösq"8(N4'Ëã sgä£È#µº@¹^qÊPì |
| --- | Minor | ¦FOÕJXJaµK	RmH0zp¥ÄQ	n )ò]ÌjLU)/Ò¢h]½¦îÎ#Ta-U ôKBá1ÌÜåÁ7«=ÙKtuåt]µ |
| --- | Minor | r²ª»äÄÍRPùòê½ÄaåùÖ!Xu¼Ø08ÔGkzNMt²zÃz<\/þÏ» ¥	>Þ2¸ÑP@Ó»¼ß½Âps/gwfÕ&GAVF2ÄH/¤T+7£tÀ }ÌG3Ñ4á{2}*XþÂiüKÈqØ`;&ño;7§»wO­ÅÌ#üh²YMN¼:0´ÿõd 7*&¼ÒßäÑ¨GðÏ!qI9Â ¦§Ñqø£ßAãÑDô-Ì¢ÈàýDfríÍcÎÄ'mõÐX^ã×ÛÒÝÑM8w£ÒÉ¢ídÀq±Ç»ÈÃEO}Êóò®Ì«z§@. ë±·"wU hFÈ"få?g#Â%p* F­JdÖîgÝ¾X±ìy©=ûG~yíËÁ÷<ý¡R¸Â	-.¡ÒF#ºßpsÑ¸ë(êNü^`QºZ½^¡Ö/Õæû2Ï4ý£ñyõÈPç áÐEÔ0âù®üº¦zw÷ÉÈ®íÌ#ÉÌ~ëgè±ÿVÎ¾þ¿à(í)CÜ4Äze^¸ókÓÉ©ÉUyöVð!ú£ .¿& |
| --- | Minor | ¦dWH;<m6QÿbÖå }?pÙõ<Ê>.h5 c2EÂ:EmMËl/Ø~8Æ¯Åº§L*[z=&O ÇËe¸åc·Þ&@³Vÿ æêîíB{P+»¡"&dù<°ûà¦¨5Äìû° =u:lvâ[þï3O?ÃÖcÛïÖc¹µD³èk·]L!æ)Hoz°RÝ#HQî\ó¥j¯Ó§UÎ|§HSz­N |
| --- | Minor | lÉ^ð|âA+<ÜKÞyÞ \EbY+»0`Wâ6fÁÜ·õ·P3ö)ÿ-?]¥/PH¨SRxZ]&c¼Òïn¬¤j!£¤Rñjb5ÿ"Òcív_ÐÐ£|ÄiHÝ®+¤²H½F_Ì¾Ëæ*#¨CÁX£I |
| --- | Minor | ~æÚ`Í0TC¨Ô>ÒþëÄÑYü¡ÜFþ	¥a£}ÿ1¤§»Ñêü·¦û7¡¾MþvO·sÀÖDöð[ß4U ßoWmø`|ÏöÌ¬¹Lð³'ÿyÜÈ.Á¬É Vögr½uéId¸Ùûp÷Û¡Ë¯¡Îðèb+h+n4µ-¶#»Æï¯'ßx¿µýh03nÞìy	eiÎB`Uô1~ÌÏKã+®¿rMA~>ÒåèÏÌ£Õ ê Ê^¼å+Üõø7ßxïLOò.°~ä1ÁekÙÑåóýõ8øè%¬A\' |
| --- | Minor | òÙÄ÷ A_Zñ¼atà¾ z º ì=jê<N |
| --- | Minor | X]RóI´¡Ñ\N^FìcþUGAz6_OêTzíXY¦©¶!Ál°Xp¢ õT®lÊÍÏ\I¬å_A%÷0ÿOwÊKYÊ&õùØÏ(ðQA»úZêAþXëæfÞFnóèýÞ©þèºèÌãI*ÃÃ¶úÊ[ÂM9y¿adbÑËhuN`²0. PHMår²ÕRV_»sùÄðþ®ïûPüKüö¿Ò	«X=Ï#×òÛÐr¬Ëî:s°×êòKÉT. K« |
| --- | Minor | Í5òûív#pË#áÒ/ÜàÑT%x?âÖs¯FçâÁ Ú\FÄ¡	:) ª®ÓÕhÜgÛÔFÒêuR®%"b"Ò¤Öµ+¢r|yU½â Îj3l6páÔk¢¯&qß^ÑÌruD¨8HØYó­ÔÐBtT·ÔÕe©Cú·~C8"ÐBO×ç Íý{ÞÀ£Eeº¤@-Th*7­4ä1ôf.FÞe RÕyZÅ¬ÞÐØW(rºâó (ÒA}!êi½GÝH®ÉÌ£ÿ&Æïyæ±¥ÁZÊOE	óòq­­Ðn-/±»Ýá°'ªj ¼<Ï. À´. ã9gu©«Î ºÐ\LoµC+Ñ|µ´øØdzÎ]t R]k))I02ÜI(Ù¤»Ø¤Ûù¥z})YKÙõ2\ËRR/ÕÉSÓüb#÷ÅW½ëÑ²ïßãE¤Å@ÿðý4óËw»ZÈ. ;ÁEØ. û'Ð¬Îjt#J]¬ScùÅ/Úî¦gú´ÕI;Ko |
| --- | Minor | ´ÈÒ#	f<3ÏÌX~|óÍSý}%%dÎ¢ê´¤ÀÃ11°(L®t²Æ^R[Wgä¦ÈbcºroÿãÖ·ªA> cMÚÎµ{}º[®­hbíqòlÃ±âc¤dØ}uç\ÕÅEªê ´ ]¾`£//kp6ÚëÉ3}hü0þÑ^÷Á-©)à4ð¢ÅÌùÓëôrËÕµ¥.èGë-nk­Åè8b0VµùµÕô_¾N3ç¼ÁLÅITqÑpâ«´ÀÂRÀrû	²òÐmtH`´ZÝfÜÇD	ãKt°PKêÔ©/´Ã*öò«-°ÄÄþÈxå¡/ª%J(yÚ\ÚÌå tÖf·:Þ"j. ³) ¢¢£#MÑªh;ZX£ cid¦ôaÉÊbå"§æÊm:ûúú©^ÂÆzyk |
| --- | Minor | ¬íyìÜñ×¦¾Ç^îý¡)ÓÞE(e¦ÆÒöÒ.ò zs¶íÕøkq |
| --- | Minor |  K |
| --- | Minor | ~5L¸\ì. ¹H%%SWÆÏÇdqZ¹­>ýu;zÊ¦5ÑÚwªP"Wä´´µyÚØÍ»¯þy¸_Çóó.ør¨¤ðÃ¦¢¸è®bð+]PWEºÙ)ðÕV¿xltwð^":±¡OIêFh#ºÝ |
| --- | Minor | Ò*¾°ùlÌ¯¿¼ùDé¬Ùf³å®Ñ øôöÚ¥c;~å<ë-¥¿°Aû¥#t]]M­Ù`!-µÐP_nÚá ueµµM¿ó§{j{$£TD%^è6º«ºs;Â_I»·æç'æý^8í?c«­Ùa§PÖ¥¹³WA-%Ú<¨Ràgvs·W»»»ì¢	ÃÑ%ú<Ï;é¬©¡ôT #?f	kkî³Óé>ÖZN_x«Kä. ´ÂS¯FGbuáxPzßm0TZÉ[H<+w{G¹__à¡ö»ÁÔ¨¡L. 8OöÙJæÑ Ók5ü#ñ'ºkJAegÙvÓH:¶ë7~|çýmtUP²ÚÚÇª§­»ý2Që¸«Ìc|1ÅÉ|5ri=¹u:E0¿å»)í+ ×*åúÜb+e#[;L¶NÊ3Úã¨Eän£®±7A«¹ @º3ð/|å¡ª(µØ\Vèå²O33F.ÿÚ¹tõº»û¨.ÂæëÐ±FÙ;ÕG{Þönïª9| ""¼¥«'B&¿DT%µF	ìÔ|RS¸âcukp[Àõªê¢äù5Dë3N­×P¸Ü^PSRi«¶^ôÜ]. =	%µ~C-ýÃopAºJ¤+&·1¥ÿE¿GïÞÅ­×Ãó~å]zW8)¡0ÉBhX ÊzyZgäàÅ:N	q#Ûº«Pë |
| --- | Minor | óèO¹³J)JA2ÓFd{ã_}ðÜ	è$ù+°teËÌZCÑ+®3µM%J2 h. ?ôh~èTV ÿ99 |
| --- | Minor | -~õe7oý[]7w}ðÝÀE«n óU=D zyyÊöÄóÃñhÂc½Ç= cFfHÄ¿Ca/iI¶BòÙÔkÁËUI¹¢WÓ/}sûÃ7¿¡e(ø¾í`c 5	 .. |
| --- | Minor | Sentence exceeds complexity threshold, split for readability. Applying the split needs --strength moderate or higher. |
| --- | Minor | none (split proposal only; source not rewritten) |
| --- | Minor | none |
| --- | Minor | Check: NEEDS-LLM |
| --- | Minor | Flags:    not-assessed |
| --- | Minor | SENTENCE (Line 1848, 87 words, 0 clauses)  [Script] |
| --- | Minor | /Éü¿BX |
| --- | Minor | (+3L¸MkRË	«Ï±tÂlMaöá¡UÀþ]eÕl¶Þÿ¢wxôúà|ñåÜ!ðffä°Pkµjµ6yv}y0ÎLÀ¨H ±z«ÌÕ&|f~ Ð8´Õöþ;ùfF\ÞoÎ|fü§ Î5deýøzf£à^°lFÁ Ðtÿ=U)yBbZ>h)Êè<ôéK_WcS3)Ykçåzív½_!Q:lë4µ·¡ÚFSA®GCÿyÌ±Eí7:íBç"nÇçS+½	_ ØN°°P¯)¢À¼Ta J5µ5êM¤©Îr¬?xt?kg¹öé;øû/¾Å< ÊßCùÔÄ_ã¼×ÔÝóÛ8¿*0Äá=¿QFËöòÃZÚ·þ¢ðòíÖì`! |
| --- | Minor | /Éü¿BX |
| --- | Minor | (+3L¸MkRË	«Ï±tÂlMaöá¡UÀþ]eÕl¶Þÿ¢wxôúà|ñåÜ!ðffä°Pkµjµ6yv}y0ÎLÀ¨H ±z«ÌÕ&|f~ Ð8´Õöþ;ùfF\ÞoÎ|fü§ Î5deýøzf£à^°lFÁ Ðtÿ=U)yBbZ>h)Êè<ôéK_WcS3)Ykçåzív½_!Q:lë4µ·¡ÚFSA®GCÿyÌ±Eí7:íBç"nÇçS+½	_ ØN°°P¯)¢À¼Ta J5µ5êM¤©Îr¬?xt?kg¹öé;øû/¾Å< ÊßCùÔÄ_ã¼×ÔÝóÛ8¿*0Äá=¿QFËöòÃZÚ·þ¢ðòíÖì`! |
| --- | Minor | Sentence exceeds complexity threshold, split for readability. Applying the split needs --strength moderate or higher. |
| --- | Minor | none (split proposal only; source not rewritten) |
| --- | Minor | none |
| --- | Minor | Check: NEEDS-LLM |
| --- | Minor | Flags:    not-assessed |
| --- | Minor | SENTENCE (Line 1848, 75 words, 2 clauses)  [Script] |
| --- | Minor | /PkïÛD©²7sùì[«Ýh3mm°¸ò¸Í9tæ Ïß/gá¿mâeôÃÓÛ\É/%ç3òØêäÿÁ[m-v#¸Ê1a 	>!,ÍPVC&Ê)¡fÔ:VyÊz@@Øã]ÒÌE®¡6ñ¨XÐ¢êËh"ÓÂf©%Å¡1ú%çµõá½÷§;_7o^¡WiÅ@/Ã~îO£ûúC^//á{°7c7$[U\ökBûátÒJ¹ÕåÚ²i§ìTe®Kæ'àKÖÎ[ºnÝïë,M&0X1W1Té|2ÆÄa:¢pµEkµN;p4¶9Kýöu])`Ëw â±]ý_ýÈÝ¯_b±¼øò:~=+øtmU´¤Yìýx}íµº±. |
| --- | Minor | /PkïÛD©²7sùì[«Ýh3mm°¸ò¸Í9tæ Ïß/gá¿mâeôÃÓÛ\É/%ç3òØêäÿÁ[m-v#¸Ê1a 	>!. ÍPVC&Ê)¡fÔ:VyÊz@@Øã]ÒÌE®¡6ñ¨XÐ¢êËh"ÓÂf©%Å¡1ú%çµõá½÷§;_7o^¡WiÅ@/Ã~îO£ûúC^//á{°7c7$[U\ökBûátÒJ¹ÕåÚ²i§ìTe®Kæ'àKÖÎ[ºnÝïë. M&0X1W1Té|2ÆÄa:¢pµEkµN;p4¶9Kýöu])`Ëw â±]ý_ýÈÝ¯_b±¼øò:~=+øtmU´¤Yìýx}íµº±.. |
| --- | Minor | Sentence exceeds complexity threshold, split for readability. Applying the split needs --strength moderate or higher. |
| --- | Minor | none (split proposal only; source not rewritten) |
| --- | Minor | none |
| --- | Minor | Check: NEEDS-LLM |
| --- | Minor | Flags:    not-assessed |
| --- | Minor | SENTENCE (Line 1848, 225 words, 5 clauses)  [Script] |
| --- | Minor | Ô*Ó¸ÜW_ÙXÒ?Ý³ýtØWeÍjpL1 ØÓ×Ìï²Ê§,ðÄ«Ks²ÓòÂw'¼êFà§Á,JóÕÙ?xHtFP {c~Íºì#È]³;ìÒQZ\mÖX«ÐDöÂýÁôÙèÀ÷þi/ÐçÐîã×¹h6-æy1ïlî«5ZHiAÛM©òìÖj[£ôÊ½»Èº!h¸o.×ëe*ð4©YgÎâÆÎvy97¿¬=BT[Ti¤¨¢BSITmeä\fµ^¼Õo	³M¤ÅÅUòÊG[xÿQ4u=r|«¹ßÏQ ÍgÅíàÿüA/+¶þWé6£:ÁPú¶3"5u×¿1xÞ¯ÇsæÄEÂÝ®Mp4Ñ*=·±£ª¹{(¾%dÕ³»çl EenUI:üÕDfº K³×o¸/LÍÓÙ(BP­}çÅNð}çð·ð;ÛN®e&Ï¹<±ZÔÕ5Ø9T-÷©55eÐÔ Úex0M$QWW½ÿÅ×ßvÈÝ¯`BU ?uWsXVÍüêaÝêÜâùa!dRÚ«áÄ­ïêÈ~miW9^!¯ÈÞ¯ÉÝ|"Ä7òò¶BÄ×mnTâF=lU¯jEþn4ëmëWÜë óµ Z»ek7çöXG !/ÖéuäÐ'ïôyªüÐâO¿¸8°öìZfþ*&|Ä9ðþQäß]UÜYèÛ	«­°pQüE KóÕ(ôO_ÉÌynÅüPæ¼B¾iKF	4Û«´mÍ¼2·Ñ#î%ÐA´ÁE¼Ë2ì,4ÃoÞ×p¤&S)Âäßk824Æ3,"Âöv|á¶´YÜäßè¹÷5.QEÆES±1Ñ¦ØßèyS ¡X3þ·7ÍÖ=Æ5/èq¿h0iwMí3ËÏñèá{ZzõaF«ÁbÂ]ÊrIªJ¤Ô |
| --- | Minor | &êÓ¤¢Ô"¼øXûÅöÏ®öZKY5>ì\ÈÌWÿ<ÇñØþìãPYtY,±>nXtöLGkk=ØWÕ¯®þÅéMÀ»úïr6qÞy</í}N u.9ÈJ§2SM"å8©Üíz²B_¯ÊÂå­ 0GG ÌÁÓ3ffÂ>ùPûpÛ§M7¥ÂZþ@HY. |
| --- | Minor | Ô*Ó¸ÜW_ÙXÒ?Ý³ýtØWeÍjpL1 ØÓ×Ìï²Ê§. ðÄ«Ks²ÓòÂw'¼êFà§Á. JóÕÙ?xHtFP {c~Íºì#È]³;ìÒQZ\mÖX«ÐDöÂýÁôÙèÀ÷þi/ÐçÐîã×¹h6-æy1ïlî«5ZHiAÛM©òìÖj[£ôÊ½»Èº!h¸o.×ëe*ð4©YgÎâÆÎvy97¿¬=BT[Ti¤¨¢BSITmeä\fµ^¼Õo	³M¤ÅÅUòÊG[xÿQ4u=r|«¹ßÏQ ÍgÅíàÿüA/+¶þWé6£:ÁPú¶3"5u×¿1xÞ¯ÇsæÄEÂÝ®Mp4Ñ*=·±£ª¹{(¾%dÕ³»çl EenUI:üÕDfº K³×o¸/LÍÓÙ(BP­}çÅNð}çð·ð;ÛN®e&Ï¹<±ZÔÕ5Ø9T-÷©55eÐÔ Úex0M$QWW½ÿÅ×ßvÈÝ¯`BU ?uWsXVÍüêaÝêÜâùa!dRÚ«áÄ­ïêÈ~miW9^!¯ÈÞ¯ÉÝ|"Ä7òò¶BÄ×mnTâF=lU¯jEþn4ëmëWÜë óµ Z»ek7çöXG !/ÖéuäÐ'ïôyªüÐâO¿¸8°öìZfþ*&|Ä9ðþQäß]UÜYèÛ	«­°pQüE KóÕ(ôO_ÉÌynÅüPæ¼B¾iKF	4Û«´mÍ¼2·Ñ#î%ÐA´ÁE¼Ë2ì. 4ÃoÞ×p¤&S)Âäßk824Æ3. "Âöv|á¶´YÜäßè¹÷5.QEÆES±1Ñ¦ØßèyS ¡X3þ·7ÍÖ=Æ5/èq¿h0iwMí3ËÏñèá{ZzõaF«ÁbÂ]ÊrIªJ¤Ô |
| --- | Minor | &êÓ¤¢Ô"¼øXûÅöÏ®öZKY5>ì\ÈÌWÿ<ÇñØþìãPYtY. ±>nXtöLGkk=ØWÕ¯®þÅéMÀ»úïr6qÞy</í}N u.9ÈJ§2SM"å8©Üíz²B_¯ÊÂå­ 0GG ÌÁÓ3ffÂ>ùPûpÛ§M7¥ÂZþ@HY.. |
| --- | Minor | Sentence exceeds complexity threshold, split for readability. Applying the split needs --strength moderate or higher. |
| --- | Minor | none (split proposal only; source not rewritten) |
| --- | Minor | none |
| --- | Minor | Check: NEEDS-LLM |
| --- | Minor | Flags:    not-assessed |
| --- | Minor | SENTENCE (Line 1848, 584 words, 18 clauses)  [Script] |
| --- | Minor | 9/¹":DÿÕÐÇw7ûã|Þ£®"Ae	MÂÑÌ³ø±úu ^¤)VËcÓrêMf¼ÒZ}Õ ì,S±ÆMMÆÇRñìÊB+u9Î£fu4hM; ®:µ0²ubZ¦¯Õ7¼i¼¸_­d7 Y²yä¿°Q[N,åv5ÓÐ=¢Á¤¨® ÑôÛê+N³ÃhîÆòÙ¥çî\DÿÄó¾ü;ÑÎÌabaô«Äü¾£C½ëy=YÝÎ^ó(Eªt»)¦JÓçÈpyÊÊWá»¥gßõ|lÕÿf:ÌHÇìIY ­mª é%§ë]ýö²=.kzí8aj² 2FãàOÖóÔ®ÑÞäR¸ >hÏ ÇÍ<ÑÞÝZ	v×7ßBx |
| --- | Minor | {½Û}Çë|@ò×så·©ßÒË(Á_h¬Æ_±ØqL¤		ýã¯AO}i)`VÅ­8@u[ Áh3KIS^ïÊS-E±ê=a}I¯}ÿÅwmõ¬W\>ys]á^¢çòè`_TÇ¦©Zp ÷PR dijYBhP¯!möÚæf4Ív~øÄ-îól"Ô`wr¡&ÈU8¥dEQ^X¹HRlÓÙKÆé¶·4t5UJ,hwÁr¢ ¯XÏ¬dVLÛ³÷Ðz®p@«½t3¨-kè&Üvyf)©(zoÏ¢ÇëIÖ:x§±<ñ ºzG§£¾¯ºÑÒñ^ |
| --- | Minor | l\sá#KñÈãë>4ç*xz«à°øÀþ0BYóÇn¢7È]gÝDßÔíë#É=?q¾ç=ã|ú6zê6{çÕûN:#ê"£¢Rã¥ 'ZÉ<îÇÈøíh£Â^áWfkk"Ê[¨jRN RF)êÜmÇÃjö0Ó6Èd6¶Õwà;æ|ç£ ·ieYjYX"3`aøåùèácÒÎ;è	ôL+¸n`HÆßÌ|'[·]¨Ð æ²²ÎR]Ý0º,=[,Ü?ßýÖðù>7h8Q~Æyæ-ôý´Ç,µp/ð+okäU·ý9]§z	S#Ì­ ³5Riæèu×7Va[µÑ¼3jg}Ð2¯.¾óóXð·EûzÝwÄ]*%¿ê+ìÒË(h>Ne6Å0þtp3¿õ±Ìt»Ûö³¼Äñ&3ó°Uá+	¿ Ï¡¹hN3¸ÞÄÐáû§o >*ëà®¬¯¾oOÞ¯qOÉ¼M»P|{êMÿÛ]¡ôU1|ÈÏü½^ª&±©7åz¾Sß[	\BS:Á¬Îc6É_ì ÝÉÔ?p~{3sPðK.\ÞçwªêtÙQÂ> ¥ |
| --- | Minor | `béh2k*K`à »ûÎ£O j¯ #ù (=®§òËÐå;A£»ï§a<z¢w² Vs4ò^wYYåp:< ÃyÞwógä±ÞèBYÆ 7L¿7Í"ôìtn²ÛÄ6ñìgO¥Ùêïß]Éþl3,Õt­ÿC´ý1ï³ÿÒ¤¶ endstream endobj 761 0 obj <</Filter/FlateDecode/Length 32>> stream xÚk``0°/þøyß¿þþzÆ	8p& úä	 endstream endobj 763 0 obj <</Subtype/CIDFontType0C/Filter/FlateDecode/Length 8823>> stream xÚµzXWÛö¬Ëì "*ãÑ,Qc¯± kë0kïððàyS¦Ë¼&zMñ®	âßsQØÓ÷&-µ]»qÒê?_k÷ùäð¨pkÏ Pkwpÿ°ÉöíµA¡.þðCcÃlF`#±QØxl6MÆ¦`Ó°éØìcl66ÍÃ>Á>Ã`±E |
| --- | Minor | ¶[}-ÅaË±Ø*l5¶[­ÃÖc0;l#fmÂ6c[°­Ø6l;æ9aÎæ¹aîæyc>/æùcX`¡XÉ°,Â¢±,ÃâER-&úMô»è±`Jág¶ÉdT3,RDn÷j/_0ûÔ,ßìK¼7.Ã»$!ïGâ;óù½ñÞ½ô¹Ù7¼ïS^ë,võÚo§åËcý÷·ïÿÙTZ±VÁVWÈ!¤vÐA>K3¥MÒ |
| --- | Minor | ø¹6TMÍ  õE·;,jxáÃ;mÌEvûÂºxÄÚ#3FYuiôâÑ¯>¼2Æ}Ì³±1cÓÆÇY+wÖ[v&nåø¢NÁ\4aY/g'ç§ª3céX".En]?EoqÛi¯êOüª ç­¡Æ*½6G«cÂp \«Ô)Tfü	}ã°F`¶É ôbûÁ½JÒÆ-­Úå]~¾à{}Ò&%µû8nsm8z²µÎÍ`,;Kelå®r2,2Xµvì¹nüÝ/ÉgÇ;ýøÑR¯Âå³µº`Ö8h MLMÑ¨Øã9o/D"8Ü	æ'Î}õ];u0¶cÉEG¸d,nÎL;î	¶§fÞ^ýìîÙ}õMíå³±éï.¾§cC%ªVù:ÒöÛöø±ïýêàÍæöòZó®^p¼#_1ofX|Ku£îì­k8F ¦²+OºaÕ zNøßïn<q58ì[SÔ¸¹ÉÓ\ÐJn½ |
| --- | Minor | éÓêb!¸¼ñ2w9ËH¶;wzÀGRÀ¡hZÆ£h;Zôt8v)³ðS-¨Ë$IbÕ@Êº}<9lV¢Áp\íà(ø!Ã¨RLI¶%Cïz¶B* 6Äj´ öâÍîôè²úiòk[w±sEí¡(xñHI;,(ã"ÕN[ôbÛ{PÅgï]«;k×È<? |
| --- | Minor | 9/¹":DÿÕÐÇw7ûã|Þ£®"Ae	MÂÑÌ³ø±úu ^¤)VËcÓrêMf¼ÒZ}Õ ì. S±ÆMMÆÇRñìÊB+u9Î£fu4hM; ®:µ0²ubZ¦¯Õ7¼i¼¸_­d7 Y²yä¿°Q[N. åv5ÓÐ=¢Á¤¨® ÑôÛê+N³ÃhîÆòÙ¥çî\DÿÄó¾ü;ÑÎÌabaô«Äü¾£C½ëy=YÝÎ^ó(Eªt»)¦JÓçÈpyÊÊWá»¥gßõ|lÕÿf:ÌHÇìIY ­mª é%§ë]ýö²=.kzí8aj² 2FãàOÖóÔ®ÑÞäR¸ >hÏ ÇÍ<ÑÞÝZ	v×7ßBx |
| --- | Minor | {½Û}Çë|@ò×så·©ßÒË(Á_h¬Æ_±ØqL¤		ýã¯AO}i)`VÅ­8@u[ Áh3KIS^ïÊS-E±ê=a}I¯}ÿÅwmõ¬W\>ys]á^¢çòè`_TÇ¦©Zp ÷PR dijYBhP¯!möÚæf4Ív~øÄ-îól"Ô`wr¡&ÈU8¥dEQ^X¹HRlÓÙKÆé¶·4t5UJ. hwÁr¢ ¯XÏ¬dVLÛ³÷Ðz®p@«½t3¨-kè&Üvyf)©(zoÏ¢ÇëIÖ:x§±<ñ ºzG§£¾¯ºÑÒñ^ |
| --- | Minor | l\sá#KñÈãë>4ç*xz«à°øÀþ0BYóÇn¢7È]gÝDßÔíë#É=?q¾ç=ã|ú6zê6{çÕûN:#ê"£¢Rã¥ 'ZÉ<îÇÈøíh£Â^áWfkk"Ê[¨jRN RF)êÜmÇÃjö0Ó6Èd6¶Õwà;æ|ç£ ·ieYjYX"3`aøåùèácÒÎ;è	ôL+¸n`HÆßÌ|'[·]¨Ð æ²²ÎR]Ý0º. =[. Ü?ßýÖðù>7h8Q~Æyæ-ôý´Ç. µp/ð+okäU·ý9]§z	S#Ì­ ³5Riæèu×7Va[µÑ¼3jg}Ð2¯.¾óóXð·EûzÝwÄ]*%¿ê+ìÒË(h>Ne6Å0þtp3¿õ±Ìt»Ûö³¼Äñ&3ó°Uá+	¿ Ï¡¹hN3¸ÞÄÐáû§o >*ëà®¬¯¾oOÞ¯qOÉ¼M»P|{êMÿÛ]¡ôU1|ÈÏü½^ª&±©7åz¾Sß[	\BS:Á¬Îc6É_ì ÝÉÔ?p~{3sPðK.\ÞçwªêtÙQÂ> ¥ |
| --- | Minor | `béh2k*K`à »ûÎ£O j¯ #ù (=®§òËÐå;A£»ï§a<z¢w² Vs4ò^wYYåp:< ÃyÞwógä±ÞèBYÆ 7L¿7Í"ôìtn²ÛÄ6ñìgO¥Ùêïß]Éþl3. Õt­ÿC´ý1ï³ÿÒ¤¶ endstream endobj 761 0 obj <</Filter/FlateDecode/Length 32>> stream xÚk``0°/þøyß¿þþzÆ	8p& úä	 endstream endobj 763 0 obj <</Subtype/CIDFontType0C/Filter/FlateDecode/Length 8823>> stream xÚµzXWÛö¬Ëì "*ãÑ. Qc¯± kë0kïððàyS¦Ë¼&zMñ®	âßsQØÓ÷&-µ]»qÒê?_k÷ùäð¨pkÏ Pkwpÿ°ÉöíµA¡.þðCcÃlF`#±QØxl6MÆ¦`Ó°éØìcl66ÍÃ>Á>Ã`±E |
| --- | Minor | ¶[}-ÅaË±Ø*l5¶[­ÃÖc0;l#fmÂ6c[°­Ø6l;æ9aÎæ¹aîæyc>/æùcX`¡XÉ°. Â¢±. ÃâER-&úMô»è±`Jág¶ÉdT3. RDn÷j/_0ûÔ. ßìK¼7.Ã»$!ïGâ;óù½ñÞ½ô¹Ù7¼ïS^ë. võÚo§åËcý÷·ïÿÙTZ±VÁVWÈ!¤vÐA>K3¥MÒ |
| --- | Minor | ø¹6TMÍ  õE·;. jxáÃ;mÌEvûÂºxÄÚ#3FYuiôâÑ¯>¼2Æ}Ì³±1cÓÆÇY+wÖ[v&nåø¢NÁ\4aY/g'ç§ª3céX".En]?EoqÛi¯êOüª ç­¡Æ*½6G«cÂp \«Ô)Tfü	}ã°F`¶É ôbûÁ½JÒÆ-­Úå]~¾à{}Ò&%µû8nsm8z²µÎÍ`. ;Kelå®r2. 2Xµvì¹nüÝ/ÉgÇ;ýøÑR¯Âå³µº`Ö8h MLMÑ¨Øã9o/D"8Ü	æ'Î}õ];u0¶cÉEG¸d. nÎL;î	¶§fÞ^ýìîÙ}õMíå³±éï.¾§cC%ªVù:ÒöÛöø±ïýêàÍæöòZó®^p¼#_1ofX|Ku£îì­k8F ¦²+OºaÕ zNøßïn<q58ì[SÔ¸¹ÉÓ\ÐJn½ |
| --- | Minor | éÓêb!¸¼ñ2w9ËH¶;wzÀGRÀ¡hZÆ£h;Zôt8v)³ðS-¨Ë$IbÕ@Êº}<9lV¢Áp\íà(ø!Ã¨RLI¶%Cïz¶B* 6Äj´ öâÍîôè²úiòk[w±sEí¡(xñHI;. (ã"ÕN[ôbÛ{PÅgï]«;k×È<?. |
| --- | Minor | Sentence exceeds complexity threshold, split for readability. Applying the split needs --strength moderate or higher. |
| --- | Minor | none (split proposal only; source not rewritten) |
| --- | Minor | none |
| --- | Minor | Check: NEEDS-LLM |
| --- | Minor | Flags:    not-assessed |
| --- | Minor | SENTENCE (Line 1848, 370 words, 8 clauses)  [Script] |
| --- | Minor | ,4^'7ÂúÇMFÑî¸ù±ûJs*I­T¨É+<éM3öÁYpöíÖãÙ5^ |
| --- | Minor | ¬«JODÖTïújAóghà¡hÐ³qÐRuÐ"±x	^î½Ã¼¥´6¬200,,0°2¬¶¶²²A7ÌþrLøZí_à :i¥ÂZÜ¼£CB2rrÝ§AkÌ FI¥¤+ÓónÞÒ×)âD¹wä9.îÜHáDÃihÁû§~ 8®cÇFâ([¯mLpäõcè1=>Âï!ºÝè¹äÂeÙ6vßºìYó©nos§8xRðÎ¿ÕJÀ¯´ôà+sÄçÉGXþ7,zÇU?Ñè\eO£>#?BRD>%ì®3²+r!Eµ<!·8ÊiG¯ª=alHêtÕ¤;W{áÊ÷Ô Zw:rlnP¢g¾=ç¸{-è=ìÜfz£¸ÓæJC%hrh¸ |
| --- | Minor | £¡¯=¾ì!ñ !µú nyT,çK&üjî?ç¼1ÀìDß	Ì,!!?ê17Ú!¦µgÇãy'Ë fíïaggigý¦Ï?Þ4AÄ§þ7ÑuÂQ5JôøÞC@µå"EêÜF~%ê |
| --- | Minor | Þ¯/)L2:> /¬®-,«dºQ½Nè[ |
| --- | Minor | ÏÕDôVGE<øø>  |
| --- | Minor | )ì;÷9Â¶;Çz{1p3A+ÊêSêhØÿÊ£üUz KöÆ ¤ª¤ÈmËi²æ¶#³ÜMÖ+ È=ãAr,Ñ ¹ S§ÏHcrN|O3îÎb<uî[)o`æÂ¸yì m6?ÃjôzM.]_l¬¬1úÆy§ì`Éò!³.ù¯?CÒ¤`&ãe"xüª÷s¥ÜX~;Q2bT¦lÎuùàþ°t¦ÉH¾åh¥[UË[ÐîK8)RI ï[vV	¤"ã?ìÎÊ?wÁTH Kîö1Ð{±þuÄC½Ü]E 3D&­DÛºóóÖús<Æ1ëüìO£ÑZô1\fÀ |
| --- | Minor | ×nUÝÍÊò÷ºåÒÙ K(Á6DsZú&5kÜpæ@EQ	VpÆ·@x |
| --- | Minor | ËIBÎGóã¤Å	uîN WDòz½¼tégNc¿3Ú×òÏ÷à"Û?g7jñ³Ðöù­íFC\Û¦fÓz°uÚÖ/-«£Ò@EqÔÜ¢*¥¼|ùzSlSh»»±1½&?L ×0reª<ÉO(Ê)Í¬`ÐI5~;Cäð 7z&x^Q­­+4²ä%y^VEÍ^ú>ÎÂ^]}¥öK¶~4fiÛñ{öë³{ÐÌb{XíîîÉmÇøsaÄg&CñD£.÷:SÉITÞí±è½YÿJ¢;Q<:ãÿö?ËDßð@p÷|T |
| --- | Minor |  |
| --- | Minor | `!< ß{þàú:õÃ^¡Çeò_'äþÍ¡`vÄ=Àù72Åq¾eëéÙN¶^±¬þ"!¼Ëß/®f&.¾\°p5ñÛÕS.æÚo`PÜ;×àð´=#Ê%bXm¥gPÉzÂþóuáö@ï |
| --- | Minor | OU¯ÒçÞdªLê*¨ïþi·úUÄMýkõUòOn7Ýovë&ÔmSâño¢Vwÿ×N!4[¡Lofy1AFÖ&¾ÈVUÍðV¼^z¼¡A­ÙÍC6ò¿H«Ã«|®4¸"d×î²£à¼¹2föÐLfà#8«h¶ ýrÜÊ{tZ¢JªÂ]f ½ëßH<ñÞl1e«Ý&©XÎx±äècy»ªÊXrÌ'Î%Á¢«¶~½våÛ\Ft»)~ÑR . |
| --- | Minor | 4^'7ÂúÇMFÑî¸ù±ûJs*I­T¨É+<éM3öÁYpöíÖãÙ5^ |
| --- | Minor | ¬«JODÖTïújAóghà¡hÐ³qÐRuÐ"±x	^î½Ã¼¥´6¬200. 0°2¬¶¶²²A7ÌþrLøZí_à :i¥ÂZÜ¼£CB2rrÝ§AkÌ FI¥¤+ÓónÞÒ×)âD¹wä9.îÜHáDÃihÁû§~ 8®cÇFâ([¯mLpäõcè1=>Âï!ºÝè¹äÂeÙ6vßºìYó©nos§8xRðÎ¿ÕJÀ¯´ôà+sÄçÉGXþ7. zÇU?Ñè\eO£>#?BRD>%ì®3²+r!Eµ<!·8ÊiG¯ª=alHêtÕ¤;W{áÊ÷Ô Zw:rlnP¢g¾=ç¸{-è=ìÜfz£¸ÓæJC%hrh¸ |
| --- | Minor | £¡¯=¾ì!ñ !µú nyT. çK&üjî?ç¼1ÀìDß	Ì. !!?ê17Ú!¦µgÇãy'Ë fíïaggigý¦Ï?Þ4AÄ§þ7ÑuÂQ5JôøÞC@µå"EêÜF~%ê |
| --- | Minor | Þ¯/)L2:> /¬®-. «dºQ½Nè[ |
| --- | Minor | ÏÕDôVGE<øø>  |
| --- | Minor | )ì;÷9Â¶;Çz{1p3A+ÊêSêhØÿÊ£üUz KöÆ ¤ª¤ÈmËi²æ¶#³ÜMÖ+ È=ãAr. Ñ ¹ S§ÏHcrN|O3îÎb<uî[)o`æÂ¸yì m6?ÃjôzM.]_l¬¬1úÆy§ì`Éò!³.ù¯?CÒ¤`&ãe"xüª÷s¥ÜX~;Q2bT¦lÎuùàþ°t¦ÉH¾åh¥[UË[ÐîK8)RI ï[vV	¤"ã?ìÎÊ?wÁTH Kîö1Ð{±þuÄC½Ü]E 3D&­DÛºóóÖús<Æ1ëüìO£ÑZô1\fÀ |
| --- | Minor | ×nUÝÍÊò÷ºåÒÙ K(Á6DsZú&5kÜpæ@EQ	VpÆ·@x |
| --- | Minor | ËIBÎGóã¤Å	uîN WDòz½¼tégNc¿3Ú×òÏ÷à"Û?g7jñ³Ðöù­íFC\Û¦fÓz°uÚÖ/-«£Ò@EqÔÜ¢*¥¼|ùzSlSh»»±1½&?L ×0reª<ÉO(Ê)Í¬`ÐI5~;Cäð 7z&x^Q­­+4²ä%y^VEÍ^ú>ÎÂ^]}¥öK¶~4fiÛñ{öë³{ÐÌb{XíîîÉmÇøsaÄg&CñD£.÷:SÉITÞí±è½YÿJ¢;Q<:ãÿö?ËDßð@p÷|T |
| --- | Minor |  |
| --- | Minor | `!< ß{þàú:õÃ^¡Çeò_'äþÍ¡`vÄ=Àù72Åq¾eëéÙN¶^±¬þ"!¼Ëß/®f&.¾\°p5ñÛÕS.æÚo`PÜ;×àð´=#Ê%bXm¥gPÉzÂþóuáö@ï |
| --- | Minor | OU¯ÒçÞdªLê*¨ïþi·úUÄMýkõUòOn7Ýovë&ÔmSâño¢Vwÿ×N!4[¡Lofy1AFÖ&¾ÈVUÍðV¼^z¼¡A­ÙÍC6ò¿H«Ã«|®4¸"d×î²£à¼¹2föÐLfà#8«h¶ ýrÜÊ{tZ¢JªÂ]f ½ëßH<ñÞl1e«Ý&©XÎx±äècy»ªÊXrÌ'Î%Á¢«¶~½våÛ\Ft»)~ÑR .. |
| --- | Minor | Sentence exceeds complexity threshold, split for readability. Applying the split needs --strength moderate or higher. |
| --- | Minor | none (split proposal only; source not rewritten) |
| --- | Minor | none |
| --- | Minor | Check: NEEDS-LLM |
| --- | Minor | Flags:    not-assessed |
| --- | Minor | SENTENCE (Line 1848, 256 words, 7 clauses)  [Script] |
| --- | Minor | Ù|*èô·.=bÈA#ÍþªRgéÈw ÙG¤í`Q,ü.²²·}¯Êª?L{m z¡÷Ø«ÉO¢bSÔáðêÿ£.&ÖÕ®@åxFRv|à"Mm[©m³ä=$Ää¬/Û¿mon';ø,AZO8îÁ".Ã5ºÔ=võ\Ns±­UW®5ÄA´×6N»T#§"ãLb@8N |
| --- | Minor | ÷gözëÏ/K'ñë#Zí¢©¨eé<¦Çkk5êZ!Èq!È##ùé¯,l4_ð7»éËò8*,¡çJÈ©=ll±üÄÔsrÊk*p¥Ýç¿¼öïä®DÒíÌLQ*n' Iënøäå÷Ë.âìÕG¯ |
| --- | Minor | k`â÷âWâ÷¤4_4Ñ), ê:øÓ¸A(6á4ÿ¨`à0Ú´no=ìmÂd48TÍòZ*þÙOOOÊ¡sõY¹i;èìk»®JÞ»é+D4	TMRßtÛQnxqßAÃÈ#'þ&íxÄ°÷ãå:Ò6ÎkØß	ò{4âONZþyäý)è¦L»'.jø¹5BÚîïÞ*Ô[/lþ8³]ô/Âó4Ú(}æ_+),Óh Ù VEuþàôT­&MÁOìz2 ¹/?ázJ=ú±SKçøÁe7v¸èÏF7£G¨àPys´zO~}°ÞÇ±%Í±<¿´Õ;(Ó\¤ªsÑÄ_^;=àc)tFFp%Z&¡ÈUàÑT¸®àèÈ.¢4|ö	úÀ<8æ«ûpÔmâ r#?µûïê01-_)4ö%êG"!^¥¿M½a¿_ ÄlNÔØËGSàVÚÙ©ü`0ºo¤ÁÊýÌÁêCå{éýûdÎUl3XïAus9¾» N[ÈuÌÔ+gSósQ¿gPÿs÷VæÐiúÌw±ÂÊ­P/½!ý6B\èlg}H+J ¨K£Ù§ãN£ÈB<&8 Y1ñ	@­¢iÊ_Aò,Ó{åAñÁA¿±3@d ¨7Ü7XºpÞøÎ» 7ÉcÇ;WtJs²å©)) fÙÖåÁ6ôçkÇ6²ÅQ~ô%³QoÔïëyß^;ý CÇXÏ/¦6Òßµqi¬VÓeÿÏixR<H<')'GÅðúN-ô!TGÄºûKþm-¦Ë[àÓÛ¼xsä|8~òE~ùñ¶E#Þ¶kì;'¡Iùód÷ä£gìqü¯S! |
| --- | Minor | Ù|*èô·.=bÈA#ÍþªRgéÈw ÙG¤í`Q. ü.²²·}¯Êª?L{m z¡÷Ø«ÉO¢bSÔáðêÿ£.&ÖÕ®@åxFRv|à"Mm[©m³ä=$Ää¬/Û¿mon';ø. AZO8îÁ".Ã5ºÔ=võ\Ns±­UW®5ÄA´×6N»T#§"ãLb@8N |
| --- | Minor | ÷gözëÏ/K'ñë#Zí¢©¨eé<¦Çkk5êZ!Èq!È##ùé¯. l4_ð7»éËò8*. ¡çJÈ©=ll±üÄÔsrÊk*p¥Ýç¿¼öïä®DÒíÌLQ*n' Iënøäå÷Ë.âìÕG¯ |
| --- | Minor | k`â÷âWâ÷¤4_4Ñ). ê:øÓ¸A(6á4ÿ¨`à0Ú´no=ìmÂd48TÍòZ*þÙOOOÊ¡sõY¹i;èìk»®JÞ»é+D4	TMRßtÛQnxqßAÃÈ#'þ&íxÄ°÷ãå:Ò6ÎkØß	ò{4âONZþyäý)è¦L»'.jø¹5BÚîïÞ*Ô[/lþ8³]ô/Âó4Ú(}æ_+). Óh Ù VEuþàôT­&MÁOìz2 ¹/?ázJ=ú±SKçøÁe7v¸èÏF7£G¨àPys´zO~}°ÞÇ±%Í±<¿´Õ;(Ó\¤ªsÑÄ_^;=àc)tFFp%Z&¡ÈUàÑT¸®àèÈ.¢4|ö	úÀ<8æ«ûpÔmâ r#?µûïê01-_)4ö%êG"!^¥¿M½a¿_ ÄlNÔØËGSàVÚÙ©ü`0ºo¤ÁÊýÌÁêCå{éýûdÎUl3XïAus9¾» N[ÈuÌÔ+gSósQ¿gPÿs÷VæÐiúÌw±ÂÊ­P/½!ý6B\èlg}H+J ¨K£Ù§ãN£ÈB<&8 Y1ñ	@­¢iÊ_Aò. Ó{åAñÁA¿±3@d ¨7Ü7XºpÞøÎ» 7ÉcÇ;WtJs²å©)) fÙÖåÁ6ôçkÇ6²ÅQ~ô%³QoÔïëyß^;ý CÇXÏ/¦6Òßµqi¬VÓeÿÏixR<H<')'GÅðúN-ô!TGÄºûKþm-¦Ë[àÓÛ¼xsä|8~òE~ùñ¶E#Þ¶kì;'¡Iùód÷ä£gìqü¯S!. |
| --- | Minor | Sentence exceeds complexity threshold, split for readability. Applying the split needs --strength moderate or higher. |
| --- | Minor | none (split proposal only; source not rewritten) |
| --- | Minor | none |
| --- | Minor | Check: NEEDS-LLM |
| --- | Minor | Flags:    not-assessed |
| --- | Minor | SENTENCE (Line 1848, 366 words, 3 clauses)  [Script] |
| --- | Minor | ×DÀö½°=RÄã{M©E8ÕÁzI(QÂõ¨¥ Â8UVJXëRP&xy)Úôâ²±ÙpÁÀ×­N=¼îk åòN¿DiÈ'i5½Â%ÀvÝ})%Û1Øçø]8N þ |
| --- | Minor | ¡YÉ5dd×2¦üHÉ-CÛØB#=?19%ó;ºÞâïì¥U³öeÈì¡`>´þþ1CaOà°Y(E£Q»4ÊÇO)£·$,¬-¯o>apY+xñu¸ï@]óhôM>-#<¦â5ñ®?¡ùÈñh0ød4¿Ò²¯ÖÀ¢eïÐØÝúEÉÂ¸x¿`ÚfíHÀ¾W:¾¹Õ:s°?xùk<ôhû£¯'{\þrÛË |
| --- | Minor | ½;ÈI?ÿRzÆí:úak­dÈa}*â*L3ê.]sg [i(ËÜYÒY¾.6::Y±X6e-å(4³¼|]Â4ÐêÉÕ*LZX]VÞØJ!ë®÷Ù?\ Á<nÇz2x1È,íþArãå )EÃ,QxGÒÛÛ~cãoE_ÚV¿±tèÊçoP?#É4A_¾½ÈÀ·ù«ñª1\í;¼É_ ZO»Çø/§V·lój9©ØEß(¾]Ã"?Cº4lÇ 1ÌT<ÑåÔ2ú!4S¢½)¬/Û_Þ#­y(­ó¯u¶ñZîÇÀ^¦2Ê¾¯þu61 Ç=k}ð]¦htJBï4óêL%\è»?çàî<çÕN]úò\}IÌ+áZéó·g1h¯)t?qºrâü |
| --- | Minor | ÍqÌ`Z È¥óAz)wt÷Ú)MB ã½¯ |
| --- | Minor | NÙmÆ9Çmn³¹Ê¶+1Õ)»Rj<ÍËCr|}©%[Ï\~d³þê¦Ñ<GT´:¢Yä@ÄÜL­.7ú´úãwÉë |
| --- | Minor | {ßz {	ð0r®QjUº?LÎ]pôxÀ®<Æ·Î=Ë%ËÜ.wyþª¡ªåì>Í_Çhr º%þ¥[àT5HgTÊÄ ~ù5ûvÈú·ãY½Ð×ª¿±3|M×k©ÍÕeeù«1)É¦nÀæ~}¨&¿w½N(KùèÎ!R¤ Ku~© |
| --- | Minor | ø"WÜ(Ñe_ÌÏ3ÏÈ¼òiè&Afh:> |
| --- | Minor | ýJ9LqR2ëVQpoÿHÃ |
| --- | Minor | jUNu-~dEÇ£½&=zHv	ËY¨±ÓFâe[¶G2àõÛ*[>f§pô¯Üi(ÚÝ|Îéð4ÑHBP4_ò#Kâþ°Ó´Òí`kc°#5^p®PÁF·J¨uÏk8¦ÄlÙfãu9<Å æm_©8eb¢Aÿø |
| --- | Minor | R[£gà?^Ùàé¥iÖ/ÒÚ¸5aÖe4¬s¿Ee)BI	XÁYõp]RÔ9l¹ÈÃ)!Ü}@ÜHÆÍ4Àú¤¾è`¹#AÁnSsR JÒ]n5(¥áB_4«ÀT½åFøI _Á»pôtèFbQçrð¨Å¡Q&²;3T¢`ýÒ\FÜ]T+AýLh¼ZsõRÏèðªÐx®}~¹`ÁÉðD¶X ½½úÆ¨rævõ+7©Û3NM³Àv¯!ª+3Ôu ;#\{~#ÝrR6-A½>Ä |
| --- | Minor | £ ÕkÃÔ)t²&EHÉ3A1³_r»iÙGhØÒ@'çÅg½ÙTÎ°j. |
| --- | Minor | ×DÀö½°=RÄã{M©E8ÕÁzI(QÂõ¨¥ Â8UVJXëRP&xy)Úôâ²±ÙpÁÀ×­N=¼îk åòN¿DiÈ'i5½Â%ÀvÝ})%Û1Øçø]8N þ |
| --- | Minor | ¡YÉ5dd×2¦üHÉ-CÛØB#=?19%ó;ºÞâïì¥U³öeÈì¡`>´þþ1CaOà°Y(E£Q»4ÊÇO)£·$. ¬-¯o>apY+xñu¸ï@]óhôM>-#<¦â5ñ®?¡ùÈñh0ød4¿Ò²¯ÖÀ¢eïÐØÝúEÉÂ¸x¿`ÚfíHÀ¾W:¾¹Õ:s°?xùk<ôhû£¯'{\þrÛË |
| --- | Minor | ½;ÈI?ÿRzÆí:úak­dÈa}*â*L3ê.]sg [i(ËÜYÒY¾.6::Y±X6e-å(4³¼|]Â4ÐêÉÕ*LZX]VÞØJ!ë®÷Ù?\ Á<nÇz2x1È. íþArãå )EÃ. QxGÒÛÛ~cãoE_ÚV¿±tèÊçoP?#É4A_¾½ÈÀ·ù«ñª1\í;¼É_ ZO»Çø/§V·lój9©ØEß(¾]Ã"?Cº4lÇ 1ÌT<ÑåÔ2ú!4S¢½)¬/Û_Þ#­y(­ó¯u¶ñZîÇÀ^¦2Ê¾¯þu61 Ç=k}ð]¦htJBï4óêL%\è»?çàî<çÕN]úò\}IÌ+áZéó·g1h¯)t?qºrâü |
| --- | Minor | ÍqÌ`Z È¥óAz)wt÷Ú)MB ã½¯ |
| --- | Minor | NÙmÆ9Çmn³¹Ê¶+1Õ)»Rj<ÍËCr|}©%[Ï\~d³þê¦Ñ<GT´:¢Yä@ÄÜL­.7ú´úãwÉë |
| --- | Minor | {ßz {	ð0r®QjUº?LÎ]pôxÀ®<Æ·Î=Ë%ËÜ.wyþª¡ªåì>Í_Çhr º%þ¥[àT5HgTÊÄ ~ù5ûvÈú·ãY½Ð×ª¿±3|M×k©ÍÕeeù«1)É¦nÀæ~}¨&¿w½N(KùèÎ!R¤ Ku~© |
| --- | Minor | ø"WÜ(Ñe_ÌÏ3ÏÈ¼òiè&Afh:> |
| --- | Minor | ýJ9LqR2ëVQpoÿHÃ |
| --- | Minor | jUNu-~dEÇ£½&=zHv	ËY¨±ÓFâe[¶G2àõÛ*[>f§pô¯Üi(ÚÝ|Îéð4ÑHBP4_ò#Kâþ°Ó´Òí`kc°#5^p®PÁF·J¨uÏk8¦ÄlÙfãu9<Å æm_©8eb¢Aÿø |
| --- | Minor | R[£gà?^Ùàé¥iÖ/ÒÚ¸5aÖe4¬s¿Ee)BI	XÁYõp]RÔ9l¹ÈÃ)!Ü}@ÜHÆÍ4Àú¤¾è`¹#AÁnSsR JÒ]n5(¥áB_4«ÀT½åFøI _Á»pôtèFbQçrð¨Å¡Q&²;3T¢`ýÒ\FÜ]T+AýLh¼ZsõRÏèðªÐx®}~¹`ÁÉðD¶X ½½úÆ¨rævõ+7©Û3NM³Àv¯!ª+3Ôu ;#\{~#ÝrR6-A½>Ä |
| --- | Minor | £ ÕkÃÔ)t²&EHÉ3A1³_r»iÙGhØÒ@'çÅg½ÙTÎ°j.. |
| --- | Minor | Sentence exceeds complexity threshold, split for readability. Applying the split needs --strength moderate or higher. |
| --- | Minor | none (split proposal only; source not rewritten) |
| --- | Minor | none |
| --- | Minor | Check: NEEDS-LLM |
| --- | Minor | Flags:    not-assessed |
| --- | Minor | SENTENCE (Line 1848, 508 words, 5 clauses)  [Script] |
| --- | Minor | ósúã (ýÚ=¼þä:\úû/ÕÑßþ¯x{h#t©)N;ÍSV K^¾ÀáTÈ;ñi·%ÂMnwèòZª¢«¼Õ@£b¾¨8Ñt~´oÞ\üâ­n\Ã ÈË:â		i#4;2¿ÀêRÍ}ð{ÛðôQ¡¾oô@#Ç2Ñõ1Â |
| --- | Minor | ?ðïþ~Í°($þ%Å¾dï¥à5¢èîsL÷ spß;S¨Ý½N÷	rûg>^JÌÜ¾Ìf¶òÐ1´w	²¥çì |
| --- | Minor | Î¢ñÄ|0N<µ¿æB-3  i":?æD¥ÛÅÝ©ýÝ4!4:¦)	§U µA«º"¯Ã |
| --- | Minor | §á×RA/D®þ¢x<fg×+<*3]OëÒÒYÆß-hª®ýJ;T 9üa?>NÌ§wß±UjÂé¦4¹áQTZ©3¢,dëpE¾i·ªfP"ìD*<ØM«`ýi ÿ|FËÐ¥æÓùiÙ9Bý¼]Q¼¯]ØíU¾¬r¡\#gUò*ÜòJÑ£b¿&î±Û2ß(J¡J6©8¾ËÍäãqM:#ÚuTu«¸Ì¤¢¥éjrÎéràÇ>Gl×"4ã½&SÿÞkêÇB®N<I¯OÌ§tùsùt8¯+ã¿*?]²/§+äD%Äv=HÉ52z²iíF!:R uj<3eRæitéTu3(ä¥Â{pj*RÇç°éÜÌ¨Y(uÈDX§ y6íÍµ¨ÝkÍSù	ÒZ¡?ð¸t}² ¨.C0ß/°ñWÔËÓºé»1î |
| --- | Minor | ¿/9Êå7¿Tvnwúæ¢Íé\¼à×p8Üa¨Û]÷À4 Cbî¶èÝºÇcY8¨V§È S!°I§'­ËÕYñ±Tlb|ªY3þ/xRÐePÙeZÌtÅTxCÏcW´ÛCì3$u°j |
| --- | Minor | ×o_§×UqÚ*ú'S/H.éSò)Cmýù¯ïÆâYòüX´3XÃªaZu³F½ýsîrç¸3âmÄÓ0±¥(*R®W*X4£ð0"NÓt;¨ |
| --- | Minor | µø*KRÄBOô6ïåáÄgªfÚÐ~o:Vg¹Jî ïÄYÞ!ü59MQL(¨Q§&0cF`\£NK£ª@é¿ÅòáRà-dñ]¢ÐuøFYÐÒU4y=5D±\Z¡ª* Å8¶z½Ørút%ððUmÚ"Avóÿâ2­ó§aé¶(5	­¡Ñ	?gæm&U¤ L×F¼§ôâ»¾sh8MÒ5´á)r I¦bÒA9Ã»n#?È ªá{ù¡­iÕ>INÈF}$ã-ðì\Så'h]V%¬úkFiìECÕuõÃ2JÅe :Ã©¤:DÍ0«CÌ;ÃkÒ[©·¼¿a~Þ1·È¶µ	ìÊú-Mÿ	µ0mZËfÞ¾kGèßÿ´­»~ã&5'Oº,¯b&îÜàH»¯3þÍÊÏÇg©K ] T°oé·ÙFº¾=z\)c¬¨Ì­	qºAõí@x	dÄ¼³¿´Ñ{·Ý:'e*ÓhLODæÆ"É½õ(ÖCñcëÏüýmIC} 9ñàð¡ï½-j¥±ªÈø J¡ |
| --- | Minor | ­NbTñ )Bò8ñävëGj¢ óf ÉÇõÑËvèeúdÙyàíWL¸«F&ãµÄ	v¸äÙ½½v5&1®jEP,å[_ZQQ´ëìÆÖE36¸ífÂ]Ê¶ÒPï-Hôßjêõ7ç¦3ã]YTñîdè¤¥îê¤°HJ[ÊM­¯ ÕóûÍg+RªßÎ/!ù ÑÔiÁ{'»,x£²JÂc5j |
| --- | Minor | ìú;å&£¾BÌ§Ð{~+uäÕN>yG ^ \©Ñêl+Ó#ÈnÔÿ<Ü_(5a!!üøÝÁoÒ=»$Õ°IÊØÄ*:kg±yçá¸.Òªû	òÑÿGÈ!+a­YÀIxR»úþè,yv '"KÜòÕNeW±âW±0KjøW¬b¸û ¯45«ÂÁ.¥é ?Ï¼ö¢¯ |
| --- | Minor | ¡ÁÔpÙI«bª½"ã F°¡ uAUùõÅL^ÏX.5-U>gêc[é¸¯¡¤ºÿï¿dÚûîK\Ý³³+Oz.ìó®®¬ '#ÑêtZ tqJÊ/eñê5LBÂÛÎ®ã;ØÇ´óÿþKBÉÏìygõÿõÎ¦§uð´ÅáÍ2=û½ÌÀ/.¹	ÓÇlcEo`Ñës¹¯A«3-©ÓéÏ[X[ôº½^fÑïÿ c. |
| --- | Minor | ósúã (ýÚ=¼þä:\úû/ÕÑßþ¯x{h#t©)N;ÍSV K^¾ÀáTÈ;ñi·%ÂMnwèòZª¢«¼Õ@£b¾¨8Ñt~´oÞ\üâ­n\Ã ÈË:â		i#4;2¿ÀêRÍ}ð{ÛðôQ¡¾oô@#Ç2Ñõ1Â |
| --- | Minor | ?ðïþ~Í°($þ%Å¾dï¥à5¢èîsL÷ spß;S¨Ý½N÷	rûg>^JÌÜ¾Ìf¶òÐ1´w	²¥çì |
| --- | Minor | Î¢ñÄ|0N<µ¿æB-3  i":?æD¥ÛÅÝ©ýÝ4!4:¦)	§U µA«º"¯Ã |
| --- | Minor | §á×RA/D®þ¢x<fg×+<*3]OëÒÒYÆß-hª®ýJ;T 9üa?>NÌ§wß±UjÂé¦4¹áQTZ©3¢. dëpE¾i·ªfP"ìD*<ØM«`ýi ÿ|FËÐ¥æÓùiÙ9Bý¼]Q¼¯]ØíU¾¬r¡\#gUò*ÜòJÑ£b¿&î±Û2ß(J¡J6©8¾ËÍäãqM:#ÚuTu«¸Ì¤¢¥éjrÎéràÇ>Gl×"4ã½&SÿÞkêÇB®N<I¯OÌ§tùsùt8¯+ã¿*?]²/§+äD%Äv=HÉ52z²iíF!:R uj<3eRæitéTu3(ä¥Â{pj*RÇç°éÜÌ¨Y(uÈDX§ y6íÍµ¨ÝkÍSù	ÒZ¡?ð¸t}² ¨.C0ß/°ñWÔËÓºé»1î |
| --- | Minor | ¿/9Êå7¿Tvnwúæ¢Íé\¼à×p8Üa¨Û]÷À4 Cbî¶èÝºÇcY8¨V§È S!°I§'­ËÕYñ±Tlb|ªY3þ/xRÐePÙeZÌtÅTxCÏcW´ÛCì3$u°j |
| --- | Minor | ×o_§×UqÚ*ú'S/H.éSò)Cmýù¯ïÆâYòüX´3XÃªaZu³F½ýsîrç¸3âmÄÓ0±¥(*R®W*X4£ð0"NÓt;¨ |
| --- | Minor | µø*KRÄBOô6ïåáÄgªfÚÐ~o:Vg¹Jî ïÄYÞ!ü59MQL(¨Q§&0cF`\£NK£ª@é¿ÅòáRà-dñ]¢ÐuøFYÐÒU4y=5D±\Z¡ª* Å8¶z½Ørút%ððUmÚ"Avóÿâ2­ó§aé¶(5	­¡Ñ	?gæm&U¤ L×F¼§ôâ»¾sh8MÒ5´á)r I¦bÒA9Ã»n#?È ªá{ù¡­iÕ>INÈF}$ã-ðì\Så'h]V%¬úkFiìECÕuõÃ2JÅe :Ã©¤:DÍ0«CÌ;ÃkÒ[©·¼¿a~Þ1·È¶µ	ìÊú-Mÿ	µ0mZËfÞ¾kGèßÿ´­»~ã&5'Oº. ¯b&îÜàH»¯3þÍÊÏÇg©K ] T°oé·ÙFº¾=z\)c¬¨Ì­	qºAõí@x	dÄ¼³¿´Ñ{·Ý:'e*ÓhLODæÆ"É½õ(ÖCñcëÏüýmIC} 9ñàð¡ï½-j¥±ªÈø J¡ |
| --- | Minor | ­NbTñ )Bò8ñävëGj¢ óf ÉÇõÑËvèeúdÙyàíWL¸«F&ãµÄ	v¸äÙ½½v5&1®jEP. å[_ZQQ´ëìÆÖE36¸ífÂ]Ê¶ÒPï-Hôßjêõ7ç¦3ã]YTñîdè¤¥îê¤°HJ[ÊM­¯ ÕóûÍg+RªßÎ/!ù ÑÔiÁ{'». x£²JÂc5j |
| --- | Minor | ìú;å&£¾BÌ§Ð{~+uäÕN>yG ^ \©Ñêl+Ó#ÈnÔÿ<Ü_(5a!!üøÝÁoÒ=»$Õ°IÊØÄ*:kg±yçá¸.Òªû	òÑÿGÈ!+a­YÀIxR»úþè. yv '"KÜòÕNeW±âW±0KjøW¬b¸û ¯45«ÂÁ.¥é ?Ï¼ö¢¯ |
| --- | Minor | ¡ÁÔpÙI«bª½"ã F°¡ uAUùõÅL^ÏX.5-U>gêc[é¸¯¡¤ºÿï¿dÚûîK\Ý³³+Oz.ìó®®¬ '#ÑêtZ tqJÊ/eñê5LBÂÛÎ®ã;ØÇ´óÿþKBÉÏìygõÿõÎ¦§uð´ÅáÍ2=û½ÌÀ/.¹	ÓÇlcEo`Ñës¹¯A«3-©ÓéÏ[X[ôº½^fÑïÿ c.. |
| --- | Minor | Sentence exceeds complexity threshold, split for readability. Applying the split needs --strength moderate or higher. |
| --- | Minor | none (split proposal only; source not rewritten) |
| --- | Minor | none |
| --- | Minor | Check: NEEDS-LLM |
| --- | Minor | Flags:    not-assessed |
| --- | Minor | SENTENCE (Line 1848, 167 words, 2 clauses)  [Script] |
| --- | Minor | endstream endobj 765 0 obj <</Filter/FlateDecode/Length 33>> stream xÚk``)°/þüßÿÿþþÿÆX$p) )£  endstream endobj 767 0 obj <</Subtype/CIDFontType0C/Filter/FlateDecode/Length 1035>> stream xÚmSLU¿^ÓÁÉfOx¬÷ :!@Ûm3J`ÙÆè"lnq[z@mé»+c@Y[h¯×ã(?dB 7FÈ²hF¶?hbÌþÁ851QÑÅý±Äè;wüáU%~÷ý¾÷}ß÷y÷ý Á (ZÔtâ |
| --- | Minor | ¦Çé¯w¸ýöjËçé |
| --- | Minor | &µDÝÄ-ªQ)T9ji®Zf°<P\£íÃs7pÃÎ¼v£{üøl/ ïíÎú§ÿÀËô!>»¾¿rÙ< ¥È#CÍè³O^ùqÑGÝ´÷ðý¬vûKõL õtuóàÝ~°*ë×­à³ÃË8¯8ýnpÌ NXA3Ò³PÎøîvú:Ó	Zé3 ÈÑ,ºX&à*¬ µÛÃÃzYÚG;9Ú |
| --- | Minor | ~7Í¾GNµ´FÆÏ&OíçhP] |
| --- | Minor |  GÓ ç¯Úl|°ËÊ°]¶N½³ùþ-âlÙsÕæÖê¦£õ |
| --- | Minor | <:¸iÞéñqÖÿ%úd3Ãö8}n%H%âB<¹:iºa¥Ï\Bè·9øQú¬QàÏ!tÚa3lÏUï+XKD^RêIìj|l"LÆcCJëßÙ?àÚ'ÇX,Y3ä÷ñqÅJ­¤¦ÅÉdjsÛ;³-r(íbÅÌhWò9Æþ)a+ë	aÒÃÓÃIÃ ÔûVÌ~TQe@! |
| --- | Minor | endstream endobj 765 0 obj <</Filter/FlateDecode/Length 33>> stream xÚk``)°/þüßÿÿþþÿÆX$p) )£  endstream endobj 767 0 obj <</Subtype/CIDFontType0C/Filter/FlateDecode/Length 1035>> stream xÚmSLU¿^ÓÁÉfOx¬÷ :!@Ûm3J`ÙÆè"lnq[z@mé»+c@Y[h¯×ã(?dB 7FÈ²hF¶?hbÌþÁ851QÑÅý±Äè;wüáU%~÷ý¾÷}ß÷y÷ý Á (ZÔtâ |
| --- | Minor | ¦Çé¯w¸ýöjËçé |
| --- | Minor | &µDÝÄ-ªQ)T9ji®Zf°<P\£íÃs7pÃÎ¼v£{üøl/ ïíÎú§ÿÀËô!>»¾¿rÙ< ¥È#CÍè³O^ùqÑGÝ´÷ðý¬vûKõL õtuóàÝ~°*ë×­à³ÃË8¯8ýnpÌ NXA3Ò³PÎøîvú:Ó	Zé3 ÈÑ. ºX&à*¬ µÛÃÃzYÚG;9Ú |
| --- | Minor | ~7Í¾GNµ´FÆÏ&OíçhP] |
| --- | Minor |  GÓ ç¯Úl|°ËÊ°]¶N½³ùþ-âlÙsÕæÖê¦£õ |
| --- | Minor | <:¸iÞéñqÖÿ%úd3Ãö8}n%H%âB<¹:iºa¥Ï\Bè·9øQú¬QàÏ!tÚa3lÏUï+XKD^RêIìj|l"LÆcCJëßÙ?àÚ'ÇX. Y3ä÷ñqÅJ­¤¦ÅÉdjsÛ;³-r(íbÅÌhWò9Æþ)a+ë	aÒÃÓÃIÃ ÔûVÌ~TQe@!. |
| --- | Minor | Sentence exceeds complexity threshold, split for readability. Applying the split needs --strength moderate or higher. |
| --- | Minor | none (split proposal only; source not rewritten) |
| --- | Minor | none |
| --- | Minor | Check: NEEDS-LLM |
| --- | Minor | Flags:    not-assessed |
| --- | Minor | SENTENCE (Line 1848, 245 words, 4 clauses)  [Script] |
| --- | Minor | ©waCá(¦È°IP¥l¥ãò¬öâdÖ(È®Á_Ý{S#ñkTLÆ¦ÉYQ¨` |
| --- | Minor | 'GÈ¡ÎÁ2ýÎëu¤V©UhùZKé¢Z>¬$=°è·ßºB¨m ÀVefJ*co·ÕzXV8ý÷zò9ßúEéÐ|HöL¦ÎÍ_úX^6}¾¹y íò TTÍüÂ² Kþ!ÏS±Ñá£1Ó·ý]i¯=R3D´,½3=¬ôÌm÷ÝJÌ÷-"í¦³·N5½§ÇWiÊ½*o/&#b|HöÇ-D]P#1"<"Óä(fæ(¢Ng¯È&"Ü«Üä¿$~ýÍw³úî'`FmSÌðÚÖðc(WUøKáe¡a£S«Á#4//¼sÉ;RòíEtì XG4®%ûDXÿ_¢NÚø,¹AQ=Ä×)½-úµ4E®"ØI)yÈÜ¦ ²Zß£ø>]«ÈËYÝZÌ:ËÐ231Zò­¾+ç·DQLé|kÇ©EY¤tZÂú¹½ endstream endobj 769 0 obj <</Filter/FlateDecode/Length 18>> stream xÚk``à``  v ù endstream endobj 771 0 obj <</Subtype/CIDFontType0C/Filter/FlateDecode/Length 7047>> stream xÚ¥Z	\×ÖA¥¨QßIÝj]µV©»T©Ô­î+ì]Âäfaì@YÅÖ­ÕkkµµÚ'ui­}ÞÁË{¿ïìò^}ï{ßï#Ë;çþïÿó?'@0lÅÊµò `ç©k½}#d ëà2~4ÿ:°cyà9/µáßòc vÂ&»½«ÑÑ¢/zE¯ i~¶6vcð«7¾´gh7°µ!Ä b1M< Fáïë.áä4sõÙYºÄQêæá( ôz{IÝ¥+¥«äQxÔ_:Q,Ýííç!óÊ}¤ë½7K#Â¼aR_<" Þ!fsgâ]b.±XH,"K÷¥Ä2Âxp#> V«µÄ:b=±ØHl&¶[]±ð$¼oÂð#ü ""BPBAD4Cì!âx#-x.Äg¿Þ#Þ³Ö "Nð ÐfÆ¦KÈ 7	OX? |
| --- | Minor | ©waCá(¦È°IP¥l¥ãò¬öâdÖ(È®Á_Ý{S#ñkTLÆ¦ÉYQ¨` |
| --- | Minor | 'GÈ¡ÎÁ2ýÎëu¤V©UhùZKé¢Z>¬$=°è·ßºB¨m ÀVefJ*co·ÕzXV8ý÷zò9ßúEéÐ|HöL¦ÎÍ_úX^6}¾¹y íò TTÍüÂ² Kþ!ÏS±Ñá£1Ó·ý]i¯=R3D´. ½3=¬ôÌm÷ÝJÌ÷-"í¦³·N5½§ÇWiÊ½*o/&#b|HöÇ-D]P#1"<"Óä(fæ(¢Ng¯È&"Ü«Üä¿$~ýÍw³úî'`FmSÌðÚÖðc(WUøKáe¡a£S«Á#4//¼sÉ;RòíEtì XG4®%ûDXÿ_¢NÚø. ¹AQ=Ä×)½-úµ4E®"ØI)yÈÜ¦ ²Zß£ø>]«ÈËYÝZÌ:ËÐ231Zò­¾+ç·DQLé|kÇ©EY¤tZÂú¹½ endstream endobj 769 0 obj <</Filter/FlateDecode/Length 18>> stream xÚk``à``  v ù endstream endobj 771 0 obj <</Subtype/CIDFontType0C/Filter/FlateDecode/Length 7047>> stream xÚ¥Z	\×ÖA¥¨QßIÝj]µV©»T©Ô­î+ì]Âäfaì@YÅÖ­ÕkkµµÚ'ui­}ÞÁË{¿ïìò^}ï{ßï#Ë;çþïÿó?'@0lÅÊµò `ç©k½}#d ëà2~4ÿ:°cyà9/µáßòc vÂ&»½«ÑÑ¢/zE¯ i~¶6vcð«7¾´gh7°µ!Ä b1M< Fáïë.áä4sõÙYºÄQêæá( ôz{IÝ¥+¥«äQxÔ_:Q. Ýííç!óÊ}¤ë½7K#Â¼aR_<" Þ!fsgâ]b.±XH. "K÷¥Ä2Âxp#> V«µÄ:b=±ØHl&¶[]±ð$¼oÂð#ü ""BPBAD4Cì!âx#-x.Äg¿Þ#Þ³Ö "Nð ÐfÆ¦KÈ 7	OX?. |
| --- | Minor | Sentence exceeds complexity threshold, split for readability. Applying the split needs --strength moderate or higher. |
| --- | Minor | none (split proposal only; source not rewritten) |
| --- | Minor | none |
| --- | Minor | Check: NEEDS-LLM |
| --- | Minor | Flags:    not-assessed |
| --- | Minor | SENTENCE (Line 1848, 363 words, 3 clauses)  [Script] |
| --- | Minor | Üoæ/2RßT |
| --- | Minor | (R,äZíK	£ËÐe°G¡DâÓh²È¨U¥ÑAë@(ç9	Ú4 æIRÁ"{>Oi: }MpÉáb7{íªrçSïJÎÊ×J°Å×+b¡ÙêÝ±û}¶naf/õø@V¶§ªº¤´ªÕ=pUÕÇrjÞ3¹ rzQÚû¶.~<iJéü(äò­¦3æZâQãÛÊ.ÞäÐÊ4iQÐÎí;ëÚñ9ÉÚ÷È0`£Åýª>\ú²íÝ ¨ÉÈ+9)[¹Þn3Ùx^´Ór\~¡ÍC8¥lOÝêÉFìmdÜ½+Ã¸¸2 -¡áN²hóØ¶úö¢&¦õ`GWµK·&¶ïÙaéjt<åÓª=à^I.È)IMIFvÇ1ï å§à~XÝNÝzòË"ôN%¯Ó¦å3E £ñä>¢R%¥²,kÏN`ÐF4ÍBîh7|Íëá»?Ã×á@¼ßJ3l¸WcÔß;»üB8XbT¨÷¤²ËÂ×nf>p>	'B§GÏåV+¹Èô¨¸`:´4ªªªlåÂÒ¦hød) µiÍüÉÌ4÷Só4Dú a?N¿8ÒZVÌ}@R	8r@Píd)ý.wÙhOfgeK(Úªþ¸>yªê [W~Èri9é]Íc&sg5v£s;8;´«»«Ô§ú²g: r1¦uA ¨¹UWú¨JI×°ãýg¨÷2ÛvW×sís-4lg²×ý#»©cÑP4ò7¡=´o^Á¹BZÒÅÐ1§«ÈÌ9çk1[ó"Ì=CLÎcÐ|LÈÀyG)XevpqBíñÊ/C?zfúçEÓ¼|+Ù}ÑéùØÎôX³Ê~ã÷1'm	v!|*Yºzg8ì¿W7Ò|Þüéõ²å½Ã%óæn÷ö·®?÷yæ*ö\¡¡>jm}@.HáX3õsÉoôõÑë\À±øà= :ÀYI§tc#Õ % bçæSÙzCN&×R{¬ò U³HrÏåâç É¸ T9K¹È Òr±E^,²ï9añ~\_dvíö¤ÃtT¹)ÁFÆkÐûq²:²[àÃ­ =âÑvØøÇ(Íþ÷QzÞ\mh7s!ûür<SÄÁEäACÆeëÙ ÝÕpÅÅÕ0¥Ú¡ælØõø³pôõú³ÔpOçßÄY<Ýø`ÊC¼ <).®ó6×úíåÔj¹ßÚ¿È·:¥*7Çzúl§ß{²C~9uýPôaJöÀºÁ&*è¹àÌèê:º(£0'5Yö¶1?\½r£]^_À5< L*9-VfEWå±È |
| --- | Minor | p0i:Kå3Àãòj]ý¾J®´°ºÐÌtIáöÚJÖ.pÊRnÊ·=Sûéî¾¸Ñ¼ËõK£XC¹´^Ä°Ôøhør²Qw­°UîëÀfÇ: wçddÃ¡8tÆýÇ)¿Çìg±O¶ª#Ü¯7ð"*xå÷Û_Æ{8àô¹F)ùÃ8ÚSÀ¢áàzò¨`ÍáÞù[÷·ú­qøPLµþQ6ýæ¢GK´Çcùõ)ÎB.W6ºûòäÅó·®fQì«&ÚÃpåA¬Â&¸RrU¯$íyòev	a×«66X!kÐo²&ÇnW°Ùå ô»9¼©Kðµâá«NË*ðf]­Lë :ÄY¸5âÈZCÂá. |
| --- | Minor | Üoæ/2RßT |
| --- | Minor | (R. äZíK	£ËÐe°G¡DâÓh²È¨U¥ÑAë@(ç9	Ú4 æIRÁ"{>Oi: }MpÉáb7{íªrçSïJÎÊ×J°Å×+b¡ÙêÝ±û}¶naf/õø@V¶§ªº¤´ªÕ=pUÕÇrjÞ3¹ rzQÚû¶.~<iJéü(äò­¦3æZâQãÛÊ.ÞäÐÊ4iQÐÎí;ëÚñ9ÉÚ÷È0`£Åýª>\ú²íÝ ¨ÉÈ+9)[¹Þn3Ùx^´Ór\~¡ÍC8¥lOÝêÉFìmdÜ½+Ã¸¸2 -¡áN²hóØ¶úö¢&¦õ`GWµK·&¶ïÙaéjt<åÓª=à^I.È)IMIFvÇ1ï å§à~XÝNÝzòË"ôN%¯Ó¦å3E £ñä>¢R%¥². kÏN`ÐF4ÍBîh7|Íëá»?Ã×á@¼ßJ3l¸WcÔß;»üB8XbT¨÷¤²ËÂ×nf>p>	'B§GÏåV+¹Èô¨¸`:´4ªªªlåÂÒ¦hød) µiÍüÉÌ4÷Só4Dú a?N¿8ÒZVÌ}@R	8r@Píd)ý.wÙhOfgeK(Úªþ¸>yªê [W~Èri9é]Íc&sg5v£s;8;´«»«Ô§ú²g: r1¦uA ¨¹UWú¨JI×°ãýg¨÷2ÛvW×sís-4lg²×ý#»©cÑP4ò7¡=´o^Á¹BZÒÅÐ1§«ÈÌ9çk1[ó"Ì=CLÎcÐ|LÈÀyG)XevpqBíñÊ/C?zfúçEÓ¼|+Ù}ÑéùØÎôX³Ê~ã÷1'm	v!|*Yºzg8ì¿W7Ò|Þüéõ²å½Ã%óæn÷ö·®?÷yæ*ö\¡¡>jm}@.HáX3õsÉoôõÑë\À±øà= :ÀYI§tc#Õ % bçæSÙzCN&×R{¬ò U³HrÏåâç É¸ T9K¹È Òr±E^. ²ï9añ~\_dvíö¤ÃtT¹)ÁFÆkÐûq²:²[àÃ­ =âÑvØøÇ(Íþ÷QzÞ\mh7s!ûür<SÄÁEäACÆeëÙ ÝÕpÅÅÕ0¥Ú¡ælØõø³pôõú³ÔpOçßÄY<Ýø`ÊC¼ <).®ó6×úíåÔj¹ßÚ¿È·:¥*7Çzúl§ß{²C~9uýPôaJöÀºÁ&*è¹àÌèê:º(£0'5Yö¶1?\½r£]^_À5< L*9-VfEWå±È |
| --- | Minor | p0i:Kå3Àãòj]ý¾J®´°ºÐÌtIáöÚJÖ.pÊRnÊ·=Sûéî¾¸Ñ¼ËõK£XC¹´^Ä°Ôøhør²Qw­°UîëÀfÇ: wçddÃ¡8tÆýÇ)¿Çìg±O¶ª#Ü¯7ð"*xå÷Û_Æ{8àô¹F)ùÃ8ÚSÀ¢áàzò¨`ÍáÞù[÷·ú­qøPLµþQ6ýæ¢GK´Çcùõ)ÎB.W6ºûòäÅó·®fQì«&ÚÃpåA¬Â&¸RrU¯$íyòev	a×«66X!kÐo²&ÇnW°Ùå ô»9¼©Kðµâá«NË*ðf]­Lë :ÄY¸5âÈZCÂá.. |
| --- | Minor | Sentence exceeds complexity threshold, split for readability. Applying the split needs --strength moderate or higher. |
| --- | Minor | none (split proposal only; source not rewritten) |
| --- | Minor | none |
| --- | Minor | Check: NEEDS-LLM |
| --- | Minor | Flags:    not-assessed |
| --- | Minor | SENTENCE (Line 1848, 134 words, 2 clauses)  [Script] |
| --- | Minor | r².ûUNþ¦«*ÃØº\`Î¤«¢KCc¢BXJµé#yKÙÜ¸øÉ}×Ã |
| --- | Minor | zþ	¼au]¼q9m·áj¸øâÇ´û´Áþ¼$2h¨ßÜ¬)¦1³SXtÁÏþ_¤ZHâÔ&«Q([³WI{«B?|aªÕ	L¯~Äa¨\X} ;A'ÄaÂ´Ç|9j;7<¾ÝÖ|Eo5ØO |
| --- | Minor | |dc5¸PcL¥£cãYô,âCIÊòJÆA¡ ­%DÙ~"/~F"²âèDUÌ:Ðjêª{ãßIÅÿÐ' R!á®µá |
| --- | Minor | úyQ¶º9û ]S*GÇ-?µ«Jðc³÷%KÆNÝ .²ÔëÊè&Ð~>5±'jó+ÕË |
| --- | Minor | \aÕ.ÚZ>ùI}2·áUbøKàÈ±ÏÐDMb);ìÙD8R?ý°³r$>àCÅNv|G³ÅÃÔÎ¶hNµÑ Ãt¯¼°é8è_ÊUxh7{Ð}o´\Â&êºoÖ*¬ù³¤I£S°¬d,9ªNs½8S©Ù@LÆ»às¨¨¸¾r@K;3¼hq8øt§Ãí)÷	*y2î{Ä±ý© SzI­ê`Ô	a	p. |
| --- | Minor | r².ûUNþ¦«*ÃØº\`Î¤«¢KCc¢BXJµé#yKÙÜ¸øÉ}×Ã |
| --- | Minor | zþ	¼au]¼q9m·áj¸øâÇ´û´Áþ¼$2h¨ßÜ¬)¦1³SXtÁÏþ_¤ZHâÔ&«Q([³WI{«B?|aªÕ	L¯~Äa¨\X} ;A'ÄaÂ´Ç|9j;7<¾ÝÖ|Eo5ØO |
| --- | Minor | |dc5¸PcL¥£cãYô. âCIÊòJÆA¡ ­%DÙ~"/~F"²âèDUÌ:Ðjêª{ãßIÅÿÐ' R!á®µá |
| --- | Minor | úyQ¶º9û ]S*GÇ-?µ«Jðc³÷%KÆNÝ .²ÔëÊè&Ð~>5±'jó+ÕË |
| --- | Minor | \aÕ.ÚZ>ùI}2·áUbøKàÈ±ÏÐDMb);ìÙD8R?ý°³r$>àCÅNv|G³ÅÃÔÎ¶hNµÑ Ãt¯¼°é8è_ÊUxh7{Ð}o´\Â&êºoÖ*¬ù³¤I£S°¬d. 9ªNs½8S©Ù@LÆ»às¨¨¸¾r@K;3¼hq8øt§Ãí)÷	*y2î{Ä±ý© SzI­ê`Ô	a	p.. |
| --- | Minor | Sentence exceeds complexity threshold, split for readability. Applying the split needs --strength moderate or higher. |
| --- | Minor | none (split proposal only; source not rewritten) |
| --- | Minor | none |
| --- | Minor | Check: NEEDS-LLM |
| --- | Minor | Flags:    not-assessed |
| --- | Minor | SENTENCE (Line 1848, 87 words, 2 clauses)  [Script] |
| --- | Minor | w/12Y¬?¬ðÂ' Aòm´Ùµ(²Æñ&Q¬JÓ©²R¸6A45Ñhl(ÚÆ#U«ÒÓÓh.9×Øu N³ÇVþíèþùe±|Zòçº¸çà{ðZ+¼%àí[=1P/)±,jÍâ"P	"ãXÔÉ8ü2¢`ÉßcAty(+`a3l"ðKLhãÓÏÍqæg&Þdvèxgà'Ñ&J©ìIHä c|Jzj};Ù55ÙÙz6£VÏ?Åw¦á.4 |
| --- | Minor | VãÇ44íD;¡W±Ô	å¦¬¬JnbqáÛÝÌ³2HàÆÀ {ýSC­-EµåµÍ§Ê<Öçcü'XKÝÒþ,ùü¯Ô~ ?TRTë¾ÚÃce8«y&¦¡1¯E®&òàPÌjHµ&6!)ÛSQVQç¯Då¸Öcp! |
| --- | Minor | w/12Y¬?¬ðÂ' Aòm´Ùµ(²Æñ&Q¬JÓ©²R¸6A45Ñhl(ÚÆ#U«ÒÓÓh.9×Øu N³ÇVþíèþùe±|Zòçº¸çà{ðZ+¼%àí[=1P/)±. jÍâ"P	"ãXÔÉ8ü2¢`ÉßcAty(+`a3l"ðKLhãÓÏÍqæg&Þdvèxgà'Ñ&J©ìIHä c|Jzj};Ù55ÙÙz6£VÏ?Åw¦á.4 |
| --- | Minor | VãÇ44íD;¡W±Ô	å¦¬¬JnbqáÛÝÌ³2HàÆÀ {ýSC­-EµåµÍ§Ê<Öçcü'XKÝÒþ. ùü¯Ô~ ?TRTë¾ÚÃce8«y&¦¡1¯E®&òàPÌjHµ&6!)ÛSQVQç¯Då¸Öcp!. |
| --- | Minor | Sentence exceeds complexity threshold, split for readability. Applying the split needs --strength moderate or higher. |
| --- | Minor | none (split proposal only; source not rewritten) |
| --- | Minor | none |
| --- | Minor | Check: NEEDS-LLM |
| --- | Minor | Flags:    not-assessed |
| --- | Minor | SENTENCE (Line 1848, 369 words, 10 clauses)  [Script] |
| --- | Minor | 1Lþv	Î¸D$ø\,»:"Õ²»Î¸ç¹Î,5·4ôÒaúòéKßAÉÉÉ Øh½6ÍÈ,,ù7à*$;!E£IHaãcró6ÙîÙt|*C*ÑÀÙNãçÝÆÙYË¿ÎQï÷·¼×Ð®[9-@\tNf5 3ÉQ¤DÈ(lÌÒjYl~qbüþ¶«/ÜHlg ý7?>ÇP½¥4A±	VêOÀøB^KDUGT°þû}³Øf,Éï ë*ZîA"kBÇ&hAj¾Õèîa_¦	ñ¬Zf[.eú3hTÀÍ¡\½¬)åDÒÄ}ªò=¶¹É¦hozæ7>ôöé6W¥ÉL°Ã¡áädÌÔjKYCf^~Fíî6	­W/s¿÷}úFpéß4ô½%&pãCYDXµ#TiÈÈdÃ4sW¸°ÉI@Þ×Êùò:´³VJHþÖÍ:ì¬nÝB>½géÄÈA_¢âäâ ä-2 |
| --- | Minor | Ùgó¶Y7@}Ä±B#k½V÷¶£àp>ÛNÂ7Ë¡í©«,Âu¢< +£û²ü>üÎtëþAkrênÀ?)ÝÞ÷6v»Ý£æáTµS©ihõ.¿Õröi^GõIöPiûG×Ò¶tß :Ô'6: ÁBBa¨Ú¿ÿ¥ÙBáÝpç¤l[£}X*iÑZÙÎfmÀÑ.úæVM½a{ÙEí`e[â |
| --- | Minor | ¶n³b"_ìtðcüö¤0!+)6]Î¢§ÿX R%©ÓÓé½Æ"CÑÀÂ§/ô9:ÁÚÄ9	aÍeÐëùÍ(!ú;)B=è\PZ'1%5@Ë§k4N)þ`ïÖË µ¨ÀÏ81Y¼È1 °Þ*Õª´9¥V[ |
| --- | Minor | 8©49Xc+N¯®røÛ5¹ùÜ5`¦~?À¡ùr±Ì×÷}ð×bÖbýÆÃrR3ÛoÜ 3IdÏûØ£âïNAÃ]}7GOÊ¸æÎ5¤Mõô~EY°"h¯ÇîeÐëîzj¥'¸	>{jxïùÝp)Øêøä5ñ±¶I©Ë@<Á9pÌùSOiHN¹Å9ßÉiKkZNymQCmd¹,MÏvV^ª;Í<=0eÙøs¶mâÐh«H©êp§ÄÖ¶e/jô«:a¨ëkRBH¢É¿Ë¥ä-¸ÌIk=ÍÂï^þå:PÍàÐ 2Hµ Z.Óêä¬QïÛJ'jÔéJv,Ê@bX%Reª3³èªPÂZHõ®pÍNÆ/è}ñô£%À§Åff«rlÝ¾,ß8`< ýýCØ««-ßbê@ |
| --- | Minor | }QÖ#µ¶cdX¡AÖjè¢¦"(NS§«qùæÔëæð	"Jª1¨²´¥T³Ô|ûàÎ¬Oúø¾'JÔ{ò¸øRW@R£ÆuTï<4ß¯LË:ýË+?û×+;Jw>=z{Eq©F&;[WÉÁù|&\Ð«íÉÔ¥0ÆÌnäo©6}·Ñ³§µï>ÔTjÀxÇ½'^´USE'ªSU)ì4¤ «EØ½®²èª0hª»A,#Ã âÙu¥8l¼2ßSE§Å9£)0_Ztºº¹d VoY«ÄW_S |
| --- | Minor | º:ºëB^µ/ÖÂb¶ÒRUkª½1aTIP§ÒÊÄø05Ù·Tj[ð1hVaOkF¦¯´8ÞN¾MÕðûúAxæWª¶©o:­LOLOf' $4 Rq*tU=(³¢gÕZ ÷Â¨C03zIÅÑÆ`W7F±'_§â¨²µæìzº*º(\âÞâsòÖÎT²p9?7¯ªøÐ%s0óö&? |
| --- | Minor | 1Lþv	Î¸D$ø\. »:"Õ²»Î¸ç¹Î. 5·4ôÒaúòéKßAÉÉÉ Øh½6ÍÈ. ù7à*$;!E£IHaãcró6ÙîÙt|*C*ÑÀÙNãçÝÆÙYË¿ÎQï÷·¼×Ð®[9-@\tNf5 3ÉQ¤DÈ(lÌÒjYl~qbüþ¶«/ÜHlg ý7?>ÇP½¥4A±	VêOÀøB^KDUGT°þû}³Øf. Éï ë*ZîA"kBÇ&hAj¾Õèîa_¦	ñ¬Zf[.eú3hTÀÍ¡\½¬)åDÒÄ}ªò=¶¹É¦hozæ7>ôöé6W¥ÉL°Ã¡áädÌÔjKYCf^~Fíî6	­W/s¿÷}úFpéß4ô½%&pãCYDXµ#TiÈÈdÃ4sW¸°ÉI@Þ×Êùò:´³VJHþÖÍ:ì¬nÝB>½géÄÈA_¢âäâ ä-2 |
| --- | Minor | Ùgó¶Y7@}Ä±B#k½V÷¶£àp>ÛNÂ7Ë¡í©«. Âu¢< +£û²ü>üÎtëþAkrênÀ?)ÝÞ÷6v»Ý£æáTµS©ihõ.¿Õröi^GõIöPiûG×Ò¶tß :Ô'6: ÁBBa¨Ú¿ÿ¥ÙBáÝpç¤l[£}X*iÑZÙÎfmÀÑ.úæVM½a{ÙEí`e[â |
| --- | Minor | ¶n³b"_ìtðcüö¤0!+)6]Î¢§ÿX R%©ÓÓé½Æ"CÑÀÂ§/ô9:ÁÚÄ9	aÍeÐëùÍ(!ú;)B=è\PZ'1%5@Ë§k4N)þ`ïÖË µ¨ÀÏ81Y¼È1 °Þ*Õª´9¥V[ |
| --- | Minor | 8©49Xc+N¯®røÛ5¹ùÜ5`¦~?À¡ùr±Ì×÷}ð×bÖbýÆÃrR3ÛoÜ 3IdÏûØ£âïNAÃ]}7GOÊ¸æÎ5¤Mõô~EY°"h¯ÇîeÐëîzj¥'¸	>{jxïùÝp)Øêøä5ñ±¶I©Ë@<Á9pÌùSOiHN¹Å9ßÉiKkZNymQCmd¹. MÏvV^ª;Í<=0eÙøs¶mâÐh«H©êp§ÄÖ¶e/jô«:a¨ëkRBH¢É¿Ë¥ä-¸ÌIk=ÍÂï^þå:PÍàÐ 2Hµ Z.Óêä¬QïÛJ'jÔéJv. Ê@bX%Reª3³èªPÂZHõ®pÍNÆ/è}ñô£%À§Åff«rlÝ¾. ß8`< ýýCØ««-ßbê@ |
| --- | Minor | }QÖ#µ¶cdX¡AÖjè¢¦"(NS§«qùæÔëæð	"Jª1¨²´¥T³Ô|ûàÎ¬Oúø¾'JÔ{ò¸øRW@R£ÆuTï<4ß¯LË:ýË+?û×+;Jw>=z{Eq©F&;[WÉÁù|&\Ð«íÉÔ¥0ÆÌnäo©6}·Ñ³§µï>ÔTjÀxÇ½'^´USE'ªSU)ì4¤ «EØ½®²èª0hª»A. #Ã âÙu¥8l¼2ßSE§Å9£)0_Ztºº¹d VoY«ÄW_S |
| --- | Minor | º:ºëB^µ/ÖÂb¶ÒRUkª½1aTIP§ÒÊÄø05Ù·Tj[ð1hVaOkF¦¯´8ÞN¾MÕðûúAxæWª¶©o:­LOLOf' $4 Rq*tU=(³¢gÕZ ÷Â¨C03zIÅÑÆ`W7F±'_§â¨²µæìzº*º(\âÞâsòÖÎT²p9?7¯ªøÐ%s0óö&?. |
| --- | Minor | Sentence exceeds complexity threshold, split for readability. Applying the split needs --strength moderate or higher. |
| --- | Minor | none (split proposal only; source not rewritten) |
| --- | Minor | none |
| --- | Minor | Check: NEEDS-LLM |
| --- | Minor | Flags:    not-assessed |
| --- | Minor | SENTENCE (Line 1848, 115 words, 2 clauses)  [Script] |
| --- | Minor | ®µvçñÑ0 |
| --- | Minor | ÃzìË/º0ìaÑ·b%CíÓÌâF(bà 1:Ðk+JÂFÇæ »ÅÖ`gêq0	Þ¸4	_H.«îø}É>Ø¹°òCfõÂ°É;¹Àeiï.¤ÝtZç±ïý:¶ùäù~W{9óËô,£d%¸EâÈÅ &È¥ ¢¹ÄÁú ¸a<ÃÞ-½T\Ï4]r,áòÖù+pryôÞôóÎëv»w©ÇDÝc/iô­ÿ0|Gª¯'kôÜ·Èuc8 ÕIÀ ôø?µ³Z]ÇÚ°Ôn¥ÞRÿµT5 ²ª@#ANüt§éc½&¶OôõofØZ 3Â¾sú»6 Õ¨5Ö¨Õ AöÐFüìÁ¦Ô0ë*K *÷TT;Öû&²Û eÿýÂYäÑÌøÝ*eïãWÓtVÃ`À?ÙõwÒ'U¤ÒhõÉQæ­e«'üW0[!~Õ4wX!?¾uèó²2uj9KÇeÅ%±ö/òaI ^/0KbúQAbö |
| --- | Minor | ¬ñ`o. |
| --- | Minor | ®µvçñÑ0 |
| --- | Minor | ÃzìË/º0ìaÑ·b%CíÓÌâF(bà 1:Ðk+JÂFÇæ »ÅÖ`gêq0	Þ¸4	_H.«îø}É>Ø¹°òCfõÂ°É;¹Àeiï.¤ÝtZç±ïý:¶ùäù~W{9óËô. £d%¸EâÈÅ &È¥ ¢¹ÄÁú ¸a<ÃÞ-½T\Ï4]r. áòÖù+pryôÞôóÎëv»w©ÇDÝc/iô­ÿ0|Gª¯'kôÜ·Èuc8 ÕIÀ ôø?µ³Z]ÇÚ°Ôn¥ÞRÿµT5 ²ª@#ANüt§éc½&¶OôõofØZ 3Â¾sú»6 Õ¨5Ö¨Õ AöÐFüìÁ¦Ô0ë*K *÷TT;Öû&²Û eÿýÂYäÑÌøÝ*eïãWÓtVÃ`À?ÙõwÒ'U¤ÒhõÉQæ­e«'üW0[!~Õ4wX!?¾uèó²2uj9KÇeÅ%±ö/òaI ^/0KbúQAbö |
| --- | Minor | ¬ñ`o.. |
| --- | Minor | Sentence exceeds complexity threshold, split for readability. Applying the split needs --strength moderate or higher. |
| --- | Minor | none (split proposal only; source not rewritten) |
| --- | Minor | none |
| --- | Minor | Check: NEEDS-LLM |
| --- | Minor | Flags:    not-assessed |
| --- | Minor | SENTENCE (Line 1848, 1550 words, 17 clauses)  [Script] |
| --- | Minor | Íüê­ÄÂÎ¿-¹Úâñë§zùù<V§ÓiÐ¥&ÑËVmsÇS¥JëSs¹·¿´ª9ë?oå»	¯1Ëúï?8Dó.û`p^f¹4`½Ün °lÔ5¸R«ÃYÙÙõ¦ì,½Ñ ÇbÑîµÿXÇF endstream endobj 773 0 obj <</Filter/FlateDecode/Length 32>> stream xÚk``0°/þü~[Ý_^=cÀ8 ë¨	M endstream endobj 775 0 obj <</Subtype/CIDFontType0C/Filter/FlateDecode/Length 3816>> stream xÚX	XS×¶>!äIi}Ý'µN­«âX@EEÁ'â(a@ aÊ 2OF@¹¨Ô§â¬¯F«vÖyºõ½uz·ï}÷°ØÛÛ¾ß	{³÷Ùkýë_ký'ÊÚNó}}UÑªO]Çø+ÂbÁjËän0÷v@¢8VÀÉ­¸Üëâ 4;X¿YJÌ¿ªþ#ú¢éý-÷;Nàè0ÿË9Ëa¨eâªÃ0ÊÆPvTê}j0õ"¡Àö·<CTksCÑÚ­ÁÍÅÕõ³ª |
| --- | Minor | uDX¸Vîæê:n´å>Iîå"÷	^©Òi"#äÁÑ!r¹¯ÜO¥ãg#ä#UÑòµð`e¨\*P,Çjj<L­Ý ùØE¡ëTêH9ÿ©V(ÁE<6:D¡kÃòÙÈ½UÑZùüuhB>f\®Q(äáZíÉcÇjcÃ\Tê°±¡üÍXeÏ"ÍXË¾1ÞüÆÌ;cß¢Y.Z½VªRËCÚà¥Æå_¡};öS©£ÉxX>¢FQ£©±5H¹S¨)ÔçåEySs¨y/åG-¤ü© jµZKP * ÖSTMm Ô£BkþI´ nM%Pÿ'<¶ ±:#,¬´`(Ý§i:þE<^|ÇÆßÆd+¶]f{Õöïvv?ÚO´?`ÿ£Ã4ý¼úµö»é8ÕñFÿèNV§#6ýbâ>Ô	vÃ'°@Èe4Hvf¦ä¡m±8QFúq¢ýiI9JYtV¤±¤ß*Qge°©¥Qõ¸½¢ËkqC£±5¿`]ó(LQµ¸}EÕãLe2þ/øZäa 0A§ÉùÌ+m4¨qbðÆ¼m(Å¿#C×Ã^QU	µ»-9hGNNåVS²ÈnRÎdÉ¬-¤ÿòQR&Õû¢Ï«íÇã¡¬>½_f¬Æühq\1;ãÃVãM2ßµû´ýÐÃrYÞ¸nIðÔùf!J	ôw{öaàj2¸1£0yÑ	jÞz\ÂyOëp\ó>\Y[¥5É@ðô10¬÷{£fùÌ~ÿ8º&>îôÅëç¼>C#n×Ì ér¡ £qFÂÆ,]:JÎÐ¯ôMqåçãF¬ê NcÃs*jeµUe{®}Wdð8âðh8»ïYëÁ	æ VnsÖ¨úHZ©miÚ_×ØÈyë?ÌõÀ}Ùâ­3Ô·Ù\:2É\{NB«¹|úî7zÏúµ¥kdD0j4aXfðÓ'ÿÝþÅî=FÄøá¤è]ZgÚ&JæE«Ý§Ï\ÐÙõäÊ¥+_µ- °/Ü¼ MÎÌ.¤Ã¦-út´,vqJæáqâNÒU¸èyÏÈ{Ä~ÔÒeZãËá AÇ~ªC3aTÐ×JÎyEvªC=´uL5ÁV¬296¡¿1£9-xInø÷¬Bwvi;+½7á6±'§Nö?ºüÄtzÄÍûOé'Çñh:?¸ÿ¹ÃA¿obözùi?Õ~üÛg²%äÄ{î"wÄø»Ïm7Î]üùÁÙù~|LÐa' æþ(äærg$¦à)ÓW}wcXw±/IÇp:1G)ëùÔÒ»øThÁìpè GzW?Ôà8£oÐææÊR#²x×hñ&Á}3dóU¿äåôgÄ.<(=v-H÷í¯¦×§§E²¤BlÀÚ¦òÜ¼Â¨iwkù9Ù½#^>Sf.¨·ãK·c{¥t¶4.1*-Äý»Y` |
| --- | Minor | !²xE¸t¸ÞÞÑ.ä6A Äòp4 |
| --- | Minor | ^Ó{ÓwD ­ÉÌÖ%³DOþ!JKÆY:éúôFyò¥4½^Ã>Ç|ºÝ=bW£¨iPÃ+#1\ Ï³_^Ï/D]pÞsNoö7ÃsÌ¹ÍæçÏ |
| --- | Minor | Ôè§®ÈX;ª(!¼blÌL	kÊÖïÒ³JMH¨R>Às5*ÿÚÂÀ×ß#ÆSÞb8±l7Ú\ý©l½)oÝÄ&fàZ]¥¹[KrQÖ¶ýÚ6ÙkW»XÆÍ£!mO¼U×æîÌ±Ù_^(+«)ÞÃ9D(ñ Zº8øØiÄ\Ê;{øð©3_¬\"Dä±fÄCË*Qi]¾&ëßMËoËM ÍI£Ç6éËM³:B¯Gà÷oªNRPßÆÑ% ñ[Ù E¿¸¾ÿäéÕDt!=´ÛmY5¦{ëµW\84ãD:épÞYè¤qs/¯¿p^fÆÄòñECà^OI CÞa°t~oÍáÇÇ»Í2®dW-1ÆV«T±±*Uu¬ÑX]mD½bÏgÊd\Ô¾æòzPÒäcXýA,jîËâÒÇ¤L £Eðº:QÍ[RKÙ¶7I+úFàÒÇ¸wé;×ÁíiAÝ´ë17KâmÑókè!7yïmíãë]Îï½I"wÆ÷zHÜãPÉùt;Ø[~fÚ¸ü³âpLq%Ú-jmr íKT¯EF%ÅjXænCd=XVá¿±¤C×°û=îóÏ`a¶iëj=ÖZSïHXÿ6ª7~·è/ôYÙM6æÈ°17á]ë~_ó;þlÌÿn|ÉÔ-<:f¨½=³yÍEÂ%	d¡y4w'ý}ß |
| --- | Minor | ¬N*k=ÈÓF¥åÆ±¹yyùeÒZCeZY>ÏâA<7`vK°Øß}ò¯¯ÿØÙ~õQ«+EMSH~¦´·Í5C%¬6îäòXkÄ0GX=~ÎÈ{»ÄÅ×ÃÓÓ÷ÆÃ/]ê¼ú«¢£	ù²Éï÷ë¥+WFâº(}FJJ&RLXªÏ²IÈËRIÕå»*Zó÷Fo&»ûª^n/EÚc-éÞÃfAÿª/ç{²J¿Otãb¿þs½Á8÷)Ü':þ¨ |
| --- | Minor | ~£1Ð¿g\¹Î^Ròû²yùh¹ÕV}ÉutL~'ÕJÞIU!8ÑÌÐGç@?¤É)ÓÕÉª+Kw³½!¹jr'É/DRf¢sgÖ75>þ¶$*fÏÙß(kÆU¬YlA\³9)=Ua½LÑN û:þAÛ¶éNòihèz×n«Qyææ¢Y8Ó±°º¡ 4§¥µÎ2ÊÀ­éÛã¬cawÎ ¼¾¹¬¬hÊ^¦ó6å[·H- 5ì¯¬Þ¾kg>oõm/ÍÁ;º3ã2_îøh»ñ,gI9® _|³ý7jeÓñ©:ÒÀý%á~®ÀÕdÑ¤Ïú´Ì}²u9ìÚõ»ººÕÉÖ¯`¯½ºtíì;ó:3Ý­¾:WÛÚÿf<{FzÝëk"&³½××%UVÕK2 ·lC¼¿|"luTbøX62Feã¿9GK-<CGi¦ðùÉ9ýÍw]7½èX/]¶çWJkõjmlb¤ÛÓ|uxÿû»SxÉùT¨ÍÑff§lÔ{Ð«I£çO>¹qè |
| --- | Minor | ¯îHÁaø |
| --- | Minor | ¦NjL-³V¹3m;:ºëXã²{·VµbáÜ Ä?QÚ¦Ì$©²7É4c³w{AÛ£«;ÞÕÄ>Qý¶þ®ÀFÐLÛ§S"§â½MjþØïI=Ê¬¹ÖÚZhlAÌÊÈ*\.ëÕÙd¥¡AÑÐËâ8; ßåBn7´ö¶}9l¤Ü ¸!2¾£Amûo |
| --- | Minor | Q\«d5xoË¿¦<5ôÖ¸Í7á¤IP  PÈåqÃ$ |
| --- | Minor | l@DL4ü!5¸m£¢lzs}òÑV-Eá²|¶¥²[Ò×´YgM/¢¶·G-Ö³o÷Wñg\ ]"mî¶Ä²Û LålÝýmÕ69tÞÒb»É&¾¸ËZ¶Vç² KÔPeA¨»Æ9ï$ Væ?æÃ æÞ«9ÖÑd FÒ%»ß²^pªñnÖsøç/Eõü¤å´û?1½}î |
| --- | Minor | $@ÆÖÑLÝoó`Û"ßÍÙ é/RÅ¾í ¶Ý§ðÓüÀ9X&çzXNæÜoXÎHÿ,B3HDrh!]ùÙtfEZUz¤ªû÷áj¤aùU»oÁR¬¬æqt@XVb¶ |
| --- | Minor | +Ø)e<êåüä¡ |
| --- | Minor | à}ëÚ^AE¹,åjªÛaðïäøj |
| --- | Minor | $à7Þ'VÄz_«|ß+ò>ßK­_|wô!vÓ¦ùáæç×¯]ù@ïp2áP5ÙòýQ¹sj7£¦åÑÈÎ:@å`ìMvfûý¥ù9+¯27ßÁ¡¹jkîöÂ3{úqÕÿGòO0ïÑ{ endstream endobj 777 0 obj <</Filter/FlateDecode/Length 24>> stream xÚk``4¼¸hZFÃº²U (&ò endstream endobj 779 0 obj <</Subtype/CIDFontType0C/Filter/FlateDecode/Length 666>> stream xÚ]R[Haþgwmr¼ì`«;ÑÎ.Ý¨JQÑÖtÃ |
| --- | Minor | o®ó¯3³mBJ¥Áè²^ Qr»I ¤øÒí!¨è5z¢©é¡¢ú¾sáÎÇá#Í¨òuuã!?îîFTÌf«V«ÕÉKs!4hÑöZµz^JYQ¶_}úFmÉû?Jê  Æ*LÎV½¡êÄ2Bí3ëqªì´ ØAØjÁg V¢ôßÓ!<:BbRæëõiÁÉD%xÈë=|Ðä°\p§ÅÁäøìdaý8mtcp?æá r0Äa@`JD#N%Å&¢1¦±0( âD)>(El?ßm /D¼ Û |
| --- | Minor | ¡JRò¤Ç#¥","°1#zD¹çn;ë¸}-­þVVº"Á0`I\,!²ÿÿõoíÇÂ < Ùj|ÈX	Â6þIUÊµcù¢UæU¤Ä×*WÌém{·B¶_Ùb´o$½®7ÄÉ·³×/2z|í»ÓëÔ«të½Z¯øÚ :^nå ã#éSj-#O¤]ôJ÷}ÎþàòªÈ$×Æ·Ö¼{²Tp­.oä·bï}¦\Ýy]-ç¿«VÇFQP-Çô9uÞPÐ9[c4@Ò!½ÑTðzî¡à6yéª|ÆEÆÉìÚ3yÁ9ÿJ¾Y`h{·ö¥Z^âùa)Î/ |
| --- | Minor | ?|°|÷«Ü´X¥æ¤ |
| --- | Minor | §£¦krËZËoÍ.îpÙmLÊTbW4ËMNÍ>§¨|va%;=Êå¦©]¿¨3 endstream endobj 781 0 obj <</Filter/FlateDecode/Length 15>> stream xÚk` F ­ ¢ endstream endobj 783 0 obj <</Subtype/CIDFontType0C/Filter/FlateDecode/Length 1137>> stream xÚTmLSW¾å¶8ñR÷a1Þ÷ÝÐH!î+ºdTsd^ÚK{ié{o¿ä£|h´¥¥¬@+ dÓéæ²éÔ,lÄÉÍþÌdÙeçº»dkçü³{¼ïy¼ç¼çy~< D©D ÅóeåïsM´uo~©H[X}«r¥­>HD¢È¶¡Òv%ùð0Zÿ!oÆÐELù'+_ÎUùþU[DáÝÎ±à:l{ê¤ô`¯¤0<(õÉAä1ò$µaÝ³uû |
| --- | Minor | \=Sj`¬"+ºöh_/æ]<k4`Oaák»Óy/(ÒÃ´ÞÌ93h«Ör-¨à)¯rVPÏhKàù ØçlÍÂ.-ÐX88ÞRg,-0`³&¬®ÒUe¬± ÈÏ@``Åæ}¢Í¨åxcACjF(°< Ò÷òTVèòËJK*ªJ´¢S |
| --- | Minor | H³AûyµßD[T¼#Gã¦TJE&ÖKD%ÑÍ÷á¼Z²ÈtJH¹	TÞA¥M¥!©Q_ u·:ZÛò»e¶Y-ò.°Rski!>s²¿å>êqÙ-fÎÒi",-¡`5àODÏãgÛ®¦v¾ØzfÞû~utÂ |
| --- | Minor | ¾¿Ðõ®Å®èXZ½p%¹@|3ô¦··¿·¯RK÷:ÒÎBÊ½]A¥_áË·½¿×~4vqûªÿôäÈÜP:su¢7ðïôÉâcæòóî)häj5µWyñaß`Ì?N/Ì§#Ýû©~/U,/«¼í¾>îvÅæB_ñs0'8:óÅääXl~þKbñ£FóãrÖ:ÊÝØwÊW/rËàÎ0©âOÿ Ñ58¶JgàæqåÝù%y³¼MÞ¡ýºèg7Á<¸,ZÔrfÝò¨¹ÖL¦c÷¿%W¨ó×æ.>6LÑ/Ø¥wSOnz é¨ä²5kÏUWê¬@^î4%êÿ½èøàì¹£ªpàÜøñµ¥º<wÄÜãSçâ³¤úÉ;ÿ2ÚómøöO+Ðr |
| --- | Minor | }ò¡´^s½y´ÕÞlç»¡nr¸cÜVe´%ÍíÖÊ÷²ÞÛñóáð4ªP<²8i´µºz¬'IÌ©ú='9wô8Í¤pÂé¶Å¾;cc×¿S©`dÿ¯ÛÝ çu»G|¡¨?4 "Ã}-|gÓI'U'gwéõ8xäºº4?ñÉ©¾Ù3Kü°´úé85{wn¿«ÿq Àv¤¼y#í±mq©xþÓñL2K©ã°õ>lC"keCb à÷þàâXÃüãþÈBXöß@Ü endstream endobj 785 0 obj <</Filter/FlateDecode/Length 19>> stream xÚk`  u endstream endobj 599 0 obj <</Type/ObjStm/N 200/First 1816/Filter/FlateDecode/Length 6438>> stream xÚå\YÛF~ß_·Â!¢îcÃá¶äCcËöØòÉáÕMµÓjö6)=¿~¿Ìª h&×v8b×2 ª*+/*°A4¢±A6*6ÖâÕo¶Òâ«n¤Ñ8Fz£m8ºFiÑçaÆázÄwï­TcÐO¢ñ®Ñèk,>ý¬oñ ïôñÝ Ð§©5è[pâ@æ=ëTã$úÛ8¾ðqèoBãÁ5±ñ4ÖÆÐ²ÆYÝ1.6üÐ|EÙDM<¨&:ôwS Ò ú £YÐÊPSô8!UJð/@wÂ5ÒYºÊA	`1'b£¤ Ìd:ãª"bN@÷pÒ4* |
| --- | Minor | 'É Ía­x¸n´B¯-Q TAjÕ01@ Cl(MÅ\ ª É)Kv¢>0Ò'dõyIIk¼8Ä~¦O >8! |
| --- | Minor | Íüê­ÄÂÎ¿-¹Úâñë§zùù<V§ÓiÐ¥&ÑËVmsÇS¥JëSs¹·¿´ª9ë?oå»	¯1Ëúï?8Dó.û`p^f¹4`½Ün °lÔ5¸R«ÃYÙÙõ¦ì. ½Ñ ÇbÑîµÿXÇF endstream endobj 773 0 obj <</Filter/FlateDecode/Length 32>> stream xÚk``0°/þü~[Ý_^=cÀ8 ë¨	M endstream endobj 775 0 obj <</Subtype/CIDFontType0C/Filter/FlateDecode/Length 3816>> stream xÚX	XS×¶>!äIi}Ý'µN­«âX@EEÁ'â(a@ aÊ 2OF@¹¨Ô§â¬¯F«vÖyºõ½uz·ï}÷°ØÛÛ¾ß	{³÷Ùkýë_ký'ÊÚNó}}UÑªO]Çø+ÂbÁjËän0÷v@¢8VÀÉ­¸Üëâ 4;X¿YJÌ¿ªþ#ú¢éý-÷;Nàè0ÿË9Ëa¨eâªÃ0ÊÆPvTê}j0õ"¡Àö·<CTksCÑÚ­ÁÍÅÕõ³ª |
| --- | Minor | uDX¸Vîæê:n´å>Iîå"÷	^©Òi"#äÁÑ!r¹¯ÜO¥ãg#ä#UÑòµð`e¨\*P. Çjj<L­Ý ùØE¡ëTêH9ÿ©V(ÁE<6:D¡kÃòÙÈ½UÑZùüuhB>f\®Q(äáZíÉcÇjcÃ\Tê°±¡üÍXeÏ"ÍXË¾1ÞüÆÌ;cß¢Y.Z½VªRËCÚà¥Æå_¡};öS©£ÉxX>¢FQ£©±5H¹S¨)ÔçåEySs¨y/åG-¤ü© jµZKP * ÖSTMm Ô£BkþI´ nM%Pÿ'<¶ ±:#. ¬´`(Ý§i:þE<^|ÇÆßÆd+¶]f{Õöïvv?ÚO´?`ÿ£Ã4ý¼úµö»é8ÕñFÿèNV§#6ýbâ>Ô	vÃ'°@Èe4Hvf¦ä¡m±8QFúq¢ýiI9JYtV¤±¤ß*Qge°©¥Qõ¸½¢ËkqC£±5¿`]ó(LQµ¸}EÕãLe2þ/øZäa 0A§ÉùÌ+m4¨qbðÆ¼m(Å¿#C×Ã^QU	µ»-9hGNNåVS²ÈnRÎdÉ¬-¤ÿòQR&Õû¢Ï«íÇã¡¬>½_f¬Æühq\1;ãÃVãM2ßµû´ýÐÃrYÞ¸nIðÔùf!J	ôw{öaàj2¸1£0yÑ	jÞz\ÂyOëp\ó>\Y[¥5É@ðô10¬÷{£fùÌ~ÿ8º&>îôÅëç¼>C#n×Ì ér¡ £qFÂÆ. ]:JÎÐ¯ôMqåçãF¬ê NcÃs*jeµUe{®}Wdð8âðh8»ïYëÁ	æ VnsÖ¨úHZ©miÚ_×ØÈyë?ÌõÀ}Ùâ­3Ô·Ù\:2É\{NB«¹|úî7zÏúµ¥kdD0j4aXfðÓ'ÿÝþÅî=FÄøá¤è]ZgÚ&JæE«Ý§Ï\ÐÙõäÊ¥+_µ- °/Ü¼ MÎÌ.¤Ã¦-út´. vqJæáqâNÒU¸èyÏÈ{Ä~ÔÒeZãËá AÇ~ªC3aTÐ×JÎyEvªC=´uL5ÁV¬296¡¿1£9-xInø÷¬Bwvi;+½7á6±'§Nö?ºüÄtzÄÍûOé'Çñh:?¸ÿ¹ÃA¿obözùi?Õ~üÛg²%äÄ{î"wÄø»Ïm7Î]üùÁÙù~|LÐa' æþ(äærg$¦à)ÓW}wcXw±/IÇp:1G)ëùÔÒ»øThÁìpè GzW?Ôà8£oÐææÊR#²x×hñ&Á}3dóU¿äåôgÄ.<(=v-H÷í¯¦×§§E²¤BlÀÚ¦òÜ¼Â¨iwkù9Ù½#^>Sf.¨·ãK·c{¥t¶4.1*-Äý»Y` |
| --- | Minor | !²xE¸t¸ÞÞÑ.ä6A Äòp4 |
| --- | Minor | ^Ó{ÓwD ­ÉÌÖ%³DOþ!JKÆY:éúôFyò¥4½^Ã>Ç|ºÝ=bW£¨iPÃ+#1\ Ï³_^Ï/D]pÞsNoö7ÃsÌ¹ÍæçÏ |
| --- | Minor | Ôè§®ÈX;ª(!¼blÌL	kÊÖïÒ³JMH¨R>Às5*ÿÚÂÀ×ß#ÆSÞb8±l7Ú\ý©l½)oÝÄ&fàZ]¥¹[KrQÖ¶ýÚ6ÙkW»XÆÍ£!mO¼U×æîÌ±Ù_^(+«)ÞÃ9D(ñ Zº8øØiÄ\Ê;{øð©3_¬\"Dä±fÄCË*Qi]¾&ëßMËoËM ÍI£Ç6éËM³:B¯Gà÷oªNRPßÆÑ% ñ[Ù E¿¸¾ÿäéÕDt!=´ÛmY5¦{ëµW\84ãD:épÞYè¤qs/¯¿p^fÆÄòñECà^OI CÞa°t~oÍáÇÇ»Í2®dW-1ÆV«T±±*Uu¬ÑX]mD½bÏgÊd\Ô¾æòzPÒäcXýA. jîËâÒÇ¤L £Eðº:QÍ[RKÙ¶7I+úFàÒÇ¸wé;×ÁíiAÝ´ë17KâmÑókè!7yïmíãë]Îï½I"wÆ÷zHÜãPÉùt;Ø[~fÚ¸ü³âpLq%Ú-jmr íKT¯EF%ÅjXænCd=XVá¿±¤C×°û=îóÏ`a¶iëj=ÖZSïHXÿ6ª7~·è/ôYÙM6æÈ°17á]ë~_ó;þlÌÿn|ÉÔ-<:f¨½=³yÍEÂ%	d¡y4w'ý}ß |
| --- | Minor | ¬N*k=ÈÓF¥åÆ±¹yyùeÒZCeZY>ÏâA<7`vK°Øß}ò¯¯ÿØÙ~õQ«+EMSH~¦´·Í5C%¬6îäòXkÄ0GX=~ÎÈ{»ÄÅ×ÃÓÓ÷ÆÃ/]ê¼ú«¢£	ù²Éï÷ë¥+WFâº(}FJJ&RLXªÏ²IÈËRIÕå»*Zó÷Fo&»ûª^n/EÚc-éÞÃfAÿª/ç{²J¿Otãb¿þs½Á8÷)Ü':þ¨ |
| --- | Minor | ~£1Ð¿g\¹Î^Ròû²yùh¹ÕV}ÉutL~'ÕJÞIU!8ÑÌÐGç@?¤É)ÓÕÉª+Kw³½!¹jr'É/DRf¢sgÖ75>þ¶$*fÏÙß(kÆU¬YlA\³9)=Ua½LÑN û:þAÛ¶éNòihèz×n«Qyææ¢Y8Ó±°º¡ 4§¥µÎ2ÊÀ­éÛã¬cawÎ ¼¾¹¬¬hÊ^¦ó6å[·H- 5ì¯¬Þ¾kg>oõm/ÍÁ;º3ã2_îøh»ñ. gI9® _|³ý7jeÓñ©:ÒÀý%á~®ÀÕdÑ¤Ïú´Ì}²u9ìÚõ»ººÕÉÖ¯`¯½ºtíì;ó:3Ý­¾:WÛÚÿf<{FzÝëk"&³½××%UVÕK2 ·lC¼¿|"luTbøX62Feã¿9GK-<CGi¦ðùÉ9ýÍw]7½èX/]¶çWJkõjmlb¤ÛÓ|uxÿû»SxÉùT¨ÍÑff§lÔ{Ð«I£çO>¹qè |
| --- | Minor | ¯îHÁaø |
| --- | Minor | ¦NjL-³V¹3m;:ºëXã²{·VµbáÜ Ä?QÚ¦Ì$©²7É4c³w{AÛ£«;ÞÕÄ>Qý¶þ®ÀFÐLÛ§S"§â½MjþØïI=Ê¬¹ÖÚZhlAÌÊÈ*\.ëÕÙd¥¡AÑÐËâ8; ßåBn7´ö¶}9l¤Ü ¸!2¾£Amûo |
| --- | Minor | Q\«d5xoË¿¦<5ôÖ¸Í7á¤IP  PÈåqÃ$ |
| --- | Minor | l@DL4ü!5¸m£¢lzs}òÑV-Eá²|¶¥²[Ò×´YgM/¢¶·G-Ö³o÷Wñg\ ]"mî¶Ä²Û LålÝýmÕ69tÞÒb»É&¾¸ËZ¶Vç² KÔPeA¨»Æ9ï$ Væ?æÃ æÞ«9ÖÑd FÒ%»ß²^pªñnÖsøç/Eõü¤å´û?1½}î |
| --- | Minor | $@ÆÖÑLÝoó`Û"ßÍÙ é/RÅ¾í ¶Ý§ðÓüÀ9X&çzXNæÜoXÎHÿ. B3HDrh!]ùÙtfEZUz¤ªû÷áj¤aùU»oÁR¬¬æqt@XVb¶ |
| --- | Minor | +Ø)e<êåüä¡ |
| --- | Minor | à}ëÚ^AE¹. åjªÛaðïäøj |
| --- | Minor | $à7Þ'VÄz_«|ß+ò>ßK­_|wô!vÓ¦ùáæç×¯]ù@ïp2áP5ÙòýQ¹sj7£¦åÑÈÎ:@å`ìMvfûý¥ù9+¯27ßÁ¡¹jkîöÂ3{úqÕÿGòO0ïÑ{ endstream endobj 777 0 obj <</Filter/FlateDecode/Length 24>> stream xÚk``4¼¸hZFÃº²U (&ò endstream endobj 779 0 obj <</Subtype/CIDFontType0C/Filter/FlateDecode/Length 666>> stream xÚ]R[Haþgwmr¼ì`«;ÑÎ.Ý¨JQÑÖtÃ |
| --- | Minor | o®ó¯3³mBJ¥Áè²^ Qr»I ¤øÒí!¨è5z¢©é¡¢ú¾sáÎÇá#Í¨òuuã!?îîFTÌf«V«ÕÉKs!4hÑöZµz^JYQ¶_}úFmÉû?Jê  Æ*LÎV½¡êÄ2Bí3ëqªì´ ØAØjÁg V¢ôßÓ!<:BbRæëõiÁÉD%xÈë=|Ðä°\p§ÅÁäøìdaý8mtcp?æá r0Äa@`JD#N%Å&¢1¦±0( âD)>(El?ßm /D¼ Û |
| --- | Minor | ¡JRò¤Ç#¥". "°1#zD¹çn;ë¸}-­þVVº"Á0`I\. !²ÿÿõoíÇÂ < Ùj|ÈX	Â6þIUÊµcù¢UæU¤Ä×*WÌém{·B¶_Ùb´o$½®7ÄÉ·³×/2z|í»ÓëÔ«të½Z¯øÚ :^nå ã#éSj-#O¤]ôJ÷}ÎþàòªÈ$×Æ·Ö¼{²Tp­.oä·bï}¦\Ýy]-ç¿«VÇFQP-Çô9uÞPÐ9[c4@Ò!½ÑTðzî¡à6yéª|ÆEÆÉìÚ3yÁ9ÿJ¾Y`h{·ö¥Z^âùa)Î/ |
| --- | Minor | ?|°|÷«Ü´X¥æ¤ |
| --- | Minor | §£¦krËZËoÍ.îpÙmLÊTbW4ËMNÍ>§¨|va%;=Êå¦©]¿¨3 endstream endobj 781 0 obj <</Filter/FlateDecode/Length 15>> stream xÚk` F ­ ¢ endstream endobj 783 0 obj <</Subtype/CIDFontType0C/Filter/FlateDecode/Length 1137>> stream xÚTmLSW¾å¶8ñR÷a1Þ÷ÝÐH!î+ºdTsd^ÚK{ié{o¿ä£|h´¥¥¬@+ dÓéæ²éÔ. lÄÉÍþÌdÙeçº»dkçü³{¼ïy¼ç¼çy~< D©D ÅóeåïsM´uo~©H[X}«r¥­>HD¢È¶¡Òv%ùð0Zÿ!oÆÐELù'+_ÎUùþU[DáÝÎ±à:l{ê¤ô`¯¤0<(õÉAä1ò$µaÝ³uû |
| --- | Minor | \=Sj`¬"+ºöh_/æ]<k4`Oaák»Óy/(ÒÃ´ÞÌ93h«Ör-¨à)¯rVPÏhKàù ØçlÍÂ.-ÐX88ÞRg. -0`³&¬®ÒUe¬± ÈÏ@``Åæ}¢Í¨åxcACjF(°< Ò÷òTVèòËJK*ªJ´¢S |
| --- | Minor | H³AûyµßD[T¼#Gã¦TJE&ÖKD%ÑÍ÷á¼Z²ÈtJH¹	TÞA¥M¥!©Q_ u·:ZÛò»e¶Y-ò.°Rski!>s²¿å>êqÙ-fÎÒi". -¡`5àODÏãgÛ®¦v¾ØzfÞû~utÂ |
| --- | Minor | ¾¿Ðõ®Å®èXZ½p%¹@|3ô¦··¿·¯RK÷:ÒÎBÊ½]A¥_áË·½¿×~4vqûªÿôäÈÜP:su¢7ðïôÉâcæòóî)häj5µWyñaß`Ì?N/Ì§#Ýû©~/U. /«¼í¾>îvÅæB_ñs0'8:óÅääXl~þKbñ£FóãrÖ:ÊÝØwÊW/rËàÎ0©âOÿ Ñ58¶JgàæqåÝù%y³¼MÞ¡ýºèg7Á<¸. ZÔrfÝò¨¹ÖL¦c÷¿%W¨ó×æ.>6LÑ/Ø¥wSOnz é¨ä²5kÏUWê¬@^î4%êÿ½èøàì¹£ªpàÜøñµ¥º<wÄÜãSçâ³¤úÉ;ÿ2ÚómøöO+Ðr |
| --- | Minor | }ò¡´^s½y´ÕÞlç»¡nr¸cÜVe´%ÍíÖÊ÷²ÞÛñóáð4ªP<²8i´µºz¬'IÌ©ú='9wô8Í¤pÂé¶Å¾;cc×¿S©`dÿ¯ÛÝ çu»G|¡¨?4 "Ã}-|gÓI'U'gwéõ8xäºº4?ñÉ©¾Ù3Kü°´úé85{wn¿«ÿq Àv¤¼y#í±mq©xþÓñL2K©ã°õ>lC"keCb à÷þàâXÃüãþÈBXöß@Ü endstream endobj 785 0 obj <</Filter/FlateDecode/Length 19>> stream xÚk`  u endstream endobj 599 0 obj <</Type/ObjStm/N 200/First 1816/Filter/FlateDecode/Length 6438>> stream xÚå\YÛF~ß_·Â!¢îcÃá¶äCcËöØòÉáÕMµÓjö6)=¿~¿Ìª h&×v8b×2 ª*+/*°A4¢±A6*6ÖâÕo¶Òâ«n¤Ñ8Fz£m8ºFiÑçaÆázÄwï­TcÐO¢ñ®Ñèk. >ý¬oñ ïôñÝ Ð§©5è[pâ@æ=ëTã$úÛ8¾ðqèoBãÁ5±ñ4ÖÆÐ²ÆYÝ1.6üÐ|EÙDM<¨&:ôwS Ò ú £YÐÊPSô8!UJð/@wÂ5ÒYºÊA	`1'b£¤ Ìd:ãª"bN@÷pÒ4* |
| --- | Minor | 'É Ía­x¸n´B¯-Q TAjÕ01@ Cl(MÅ\ ª É)Kv¢>0Ò'dõyIIk¼8Ä~¦O >8!. |
| --- | Minor | Sentence exceeds complexity threshold, split for readability. Applying the split needs --strength moderate or higher. |
| --- | Minor | none (split proposal only; source not rewritten) |
| --- | Minor | none |
| --- | Minor | Check: NEEDS-LLM |
| --- | Minor | Flags:    not-assessed |
| --- | Minor | SENTENCE (Line 1848, 508 words, 6 clauses)  [Script] |
| --- | Minor | 9ØØÁÑ¦zaHÙxIâhØV1Ýx!9fóF§£qk`d«ÉF0¶â9µ( æ è@8`ZBfÄ `¥ 	+mÀ*¤§¾iõÄ®Ð»[H )-ÈPÄô	 ÀPä¶t&I4ö	¨2à4_ÃÄ:?â#!%øÐKæÁ¢V3Â§öDÙC}	ÂlÔZ#QÔÉW<9 G<Càu¯³Ô  è^a$¼86£Y§VK(EqüM×Xc .aP1í©ÓóÞoGÒÆ5%4ìäpÐW G¨EÃ[à*é ¦3GgàHrX^jM¾`Jm!'E/°¿òtÐt-ðáT :»E`IghÚÉ- 	CÁÂÃq>pXÄV:ò4Î0ÖÒìÎ bNORÃaAÐ rC¡Y8 æ z ¿'xÒ 'ÍzrOõVÂD1<{A@JÌ`GÌ )ÂQÀÑÂ¡ÅàµÐYÀ¼ °¼DÎ	ÌñÏ¾Å±'#2â %¹"±è*à­IZPzðÒ$wI®(¯Û~ü©¡Ù\ ÿí»Õ777BÁU³ àË@8ï,Õá@@vèÛÈ£g_Î7ú#ä;5³..:^ÉJSàAKµÀÒ®Õ¸Ýâ çÛáîçöíF@2;^°p}Ð5ïÁ,dg ÍãÆi=kéÀGÕN/\ßhXoÔ¨­FBÎÍ!c QsãgÖûEÔ38³q¡fÚ´ö)gT·Z8ß7fTd±Ð¡WÈÆéä lVTb ÓpäbeQæQ"aËà' ®9:·8êtÝÅ|}óA{ñß´ì^îÚgöËÃvw»?ø ýj}¿¹=péG,}±ùåÀuòä´¦¢).ñy¦F@Rã)¥W3Óªi¿ºßüÌuzÅ}ç0³¢¾{U¦Õ#yM=h$#ÉGªMóàãò¼EÜ^ú¾.sûUþÈc<ª	³rì¢ÎÇ6É<ù/fì¢iê·÷ûC¬ý|½ï´Ó>Ý½SOÔít­O?Ã««lWôäY7Y_>ÎëÈìèëyã	¸y>UÙ'fýÄÄ×ñåk·ÒÇøSüe%Y).Ðl¼Â,ÌgÅ]eÅ1fô<3±fFN3S´P Oáóâ |
| --- | Minor | ÄlHû¬uÖ>ÍKÍÂÌ2VV3áAV®úpÄf­\¥ÖlgVfösv99oMâÉh:q=S»^¨\/×ÙõìëÕ¡Lêù0Á0#W`ãÍËlî&k7s!©ÛW@©BgCçRUø,.è+Ð±êü½ØÑöýØÔñðaîåÉ6(r&'»®úøPÁ=ÈK3BÉ*ªìòúózùcË*ÞeÃïX¼vZ¼×ØQ»:%Çæ*gMfòqÇ¥?âì´êªEïXÖ1W'T Ò@/3¨ô°®ÌöÆ«Mu4éX>åÜÃùy»Ã |
| --- | Minor | O	2Y7¾ vöxp#§¶¹4ôuE¢^g§·}V¨s«^gÅ*½½e#yyì?¯¬kYÛ>]ÏA'Ô7À§fR·©²ß m_UñÁô~V}ægëæF<-(ð]â@Á¬«#é>óê}åsaÚ&ã>þJÌGÇb^úª×)êØ:¥ðõjXµxWÅÛXõ«jw!T6´djçï®·¥·}µ3¨kËÇäSò%ÃªzA¤ÌåÇÑóÌ<àXê¿ª2Ûeµ²Ic¥ÂîP¯g²c­Ý^Wjê·cæ©S½rG+µÉõò:õS¢r[AðªJv:4º¤ |
| --- | Minor | ( ­ôóÅ23*Ø«öbA¡ìF«ËÖk§ºàÖ3µ®rV5sÌ:nu7¯W+%üÆbQöÅR·Ï"G¢h·pý<³¨>ùÍÄD©$;F^W\ôðí ('ÊõÚ25:&* º;n0/l½2ÖâH¤{]_?Ütü¯fbq*Û'õ6@öËÕ¯	ç­WÝZ÷ËNØk¿óÇÐ[ê*_A××Èo¨,éÓ7Gs°hÎZ¶ÖpIôÎ[f© ´ùRÔT 4)¦« UohudõûªÑOîOÌTU5çW³ÆÙ nPÕh}¯ë¾ê8¾·R6{Åìäº®2ô±íº¾»ÛÜ^mY\ÌOZ	Yv>67Í¥DÇeRRê&eð&å¹&Eö&ÅÌ&E&ùZ Ú LÀ *!Q	JHTB¢ôS¨ÄD%&*1QSháDEÇL&Ëè}¸ê³í Íø ÁñøL¾D7|äcê*Óég·2mäi¶1+®K]Ê;º! |
| --- | Minor | 9ØØÁÑ¦zaHÙxIâhØV1Ýx!9fóF§£qk`d«ÉF0¶â9µ( æ è@8`ZBfÄ `¥ 	+mÀ*¤§¾iõÄ®Ð»[H )-ÈPÄô	 ÀPä¶t&I4ö	¨2à4_ÃÄ:?â#!%øÐKæÁ¢V3Â§öDÙC}	ÂlÔZ#QÔÉW<9 G<Càu¯³Ô  è^a$¼86£Y§VK(EqüM×Xc .aP1í©ÓóÞoGÒÆ5%4ìäpÐW G¨EÃ[à*é ¦3GgàHrX^jM¾`Jm!'E/°¿òtÐt-ðáT :»E`IghÚÉ- 	CÁÂÃq>pXÄV:ò4Î0ÖÒìÎ bNORÃaAÐ rC¡Y8 æ z ¿'xÒ 'ÍzrOõVÂD1<{A@JÌ`GÌ )ÂQÀÑÂ¡ÅàµÐYÀ¼ °¼DÎ	ÌñÏ¾Å±'#2â %¹"±è*à­IZPzðÒ$wI®(¯Û~ü©¡Ù\ ÿí»Õ777BÁU³ àË@8ï. Õá@@vèÛÈ£g_Î7ú#ä;5³..:^ÉJSàAKµÀÒ®Õ¸Ýâ çÛáîçöíF@2;^°p}Ð5ïÁ. dg ÍãÆi=kéÀGÕN/\ßhXoÔ¨­FBÎÍ!c QsãgÖûEÔ38³q¡fÚ´ö)gT·Z8ß7fTd±Ð¡WÈÆéä lVTb ÓpäbeQæQ"aËà' ®9:·8êtÝÅ|}óA{ñß´ì^îÚgöËÃvw»?ø ýj}¿¹=péG. }±ùåÀuòä´¦¢).ñy¦F@Rã)¥W3Óªi¿ºßüÌuzÅ}ç0³¢¾{U¦Õ#yM=h$#ÉGªMóàãò¼EÜ^ú¾.sûUþÈc<ª	³rì¢ÎÇ6É<ù/fì¢iê·÷ûC¬ý|½ï´Ó>Ý½SOÔít­O?Ã««lWôäY7Y_>ÎëÈìèëyã	¸y>UÙ'fýÄÄ×ñåk·ÒÇøSüe%Y).Ðl¼Â. ÌgÅ]eÅ1fô<3±fFN3S´P Oáóâ |
| --- | Minor | ÄlHû¬uÖ>ÍKÍÂÌ2VV3áAV®úpÄf­\¥ÖlgVfösv99oMâÉh:q=S»^¨\/×ÙõìëÕ¡Lêù0Á0#W`ãÍËlî&k7s!©ÛW@©BgCçRUø. .è+Ð±êü½ØÑöýØÔñðaîåÉ6(r&'»®úøPÁ=ÈK3BÉ*ªìòúózùcË*ÞeÃïX¼vZ¼×ØQ»:%Çæ*gMfòqÇ¥?âì´êªEïXÖ1W'T Ò@/3¨ô°®ÌöÆ«Mu4éX>åÜÃùy»Ã |
| --- | Minor | O	2Y7¾ vöxp#§¶¹4ôuE¢^g§·}V¨s«^gÅ*½½e#yyì?¯¬kYÛ>]ÏA'Ô7À§fR·©²ß m_UñÁô~V}ægëæF<-(ð]â@Á¬«#é>óê}åsaÚ&ã>þJÌGÇb^úª×)êØ:¥ðõjXµxWÅÛXõ«jw!T6´djçï®·¥·}µ3¨kËÇäSò%ÃªzA¤ÌåÇÑóÌ<àXê¿ª2Ûeµ²Ic¥ÂîP¯g²c­Ý^Wjê·cæ©S½rG+µÉõò:õS¢r[AðªJv:4º¤ |
| --- | Minor | ( ­ôóÅ23*Ø«öbA¡ìF«ËÖk§ºàÖ3µ®rV5sÌ:nu7¯W+%üÆbQöÅR·Ï"G¢h·pý<³¨>ùÍÄD©$;F^W\ôðí ('ÊõÚ25:&* º;n0/l½2ÖâH¤{]_?Ütü¯fbq*Û'õ6@öËÕ¯	ç­WÝZ÷ËNØk¿óÇÐ[ê*_A××Èo¨. éÓ7Gs°hÎZ¶ÖpIôÎ[f© ´ùRÔT 4)¦« UohudõûªÑOîOÌTU5çW³ÆÙ nPÕh}¯ë¾ê8¾·R6{Åìäº®2ô±íº¾»ÛÜ^mY\ÌOZ	Yv>67Í¥DÇeRRê&eð&å¹&Eö&ÅÌ&E&ùZ Ú LÀ *!Q	JHTB¢ôS¨ÄD%&*1QSháDEÇL&Ëè}¸ê³í Íø ÁñøL¾D7|äcê*Óég·2mäi¶1+®K]Ê;º!. |
| --- | Minor | Sentence exceeds complexity threshold, split for readability. Applying the split needs --strength moderate or higher. |
| --- | Minor | none (split proposal only; source not rewritten) |
| --- | Minor | none |
| --- | Minor | Check: NEEDS-LLM |
| --- | Minor | Flags:    not-assessed |
| --- | Minor | SENTENCE (Line 1848, 520 words, 7 clauses)  [Script] |
| --- | Minor | íÔT	E§LÅê§Òg+(©u¯¡\+3teÆ®Ìà½2ÃWfüÊY1+3heF­ôSî'ýÿ3ÛÐØNÃç2]f¤ËuÑ-3¼eÂ÷óSXIQ±âÎ¶@þ)³É?£¯fû~°­ð£I9<f>5³Êì§2Nj?ÎjßDcíNûÉaé|LÖPÙåTv9ÒÝêf%%æâC [^Zæ©eZæ©eÎrÊô§² G®håI@ÈÚM@9§HÄÖS9c©É¥fsU#þÆIËêNE	cÒÉùO"G¤ÍÙ¢ç[/Uj³ÊéFe «d3Ê)GÅIÆ9fÝõrÄ±	+_®jN züzÜØý=®SI.7t.7t.7t.­u®­u.?t.?t.¯u®¯uy:û±Î!OÇI4Fs*ëqF¾jó*#ßwf¢J@ÊÇ²rU`ÊéOç*Bç*Bç*Âä*Â)1³ÑªÂ1Îb¿ÈÌKHá&§JòzT¼J%FÊS	æEÉoZ,ËJ7"¯«zÂäºÇÈ©¤oÔ\Ò÷jÌÐ(éû.>çyÁäm÷LÞh0y§Áä­£¦ÑòTô(¡øÓâÇ@e²ð.{åÄhrb491MN&'F×¦lY=3åÄÆÌ9±9±1#'ö]ü1&³Rö>ÊæG®LÎn&g73Ý=qvóþ|Uçº#ß'zf<ÉûÙQ  §³~Òð¼þ*W	tÁUûbsµ]¸ûeIäé"U&úô~³>ìî}¾~¹ù¡ù×öð¦yyîï7¯·_Ýï®Þ]nîýrõóöîêõÛ_<ùÇÓÀíîöÙú°yôì¿°r"-QPYûDÿÄÿÓ_Þmn/xÓ1ßwýñö°bI^ì®6í·ûÍï7Û[öÅú-LçRllËå~§¤ïtÇ yº>¬ov×§Ó#b×9¡lbzÐnÖvüèí*Î {Ò	ô¬ÆádX®îÇÑLÿSÞóÇ{Ï½¼OT½Mí!Â³[Ñs |
| --- | Minor | C=â×ÆùyôÌàÇçÎÀSÿ,>Ãéï#YS¹i9~è-qOw>;öãWVÂCN÷¼j¤Çñ@ov'}Fy57ÿqd¹uÒ6Õ©6()£Où¨¢Ín,éÕó7ô=ðÃWC±W=KùFQrÆK¡|e¾ô·ÄSó³H¦;q;t$©½ô\êPA£ù¹GMåJ#ÅVbzÌ~:úª(ÿøyIþÓ}4ÿ¹ èÇÌé9å?0,ËÅ ºÖñÙIÜTÆ)UÏµU  Ò§ó ÒìVË¿ÔÈæ¿ìC7ðª¾h`êS·Öã²}éáÐ¨«G®tÔªe¦(2hkÐ¼I±¬ëÿV´º 9oqkã õj=yWÔýuºy»|Dþûçü§=¯yÑi;mÿùg=eo%òÀD«ñ´"÷1Æò)A2vYÿRñFosPN#¬ïÇ [ßTì1ô·L1/J°ÓIÐTñ?yoÍêì¶§K`ÛÄÈq^úL&ýiAR$yÆ2zYÄûÀsÐJÔ/zIM*ws¼Jû=: ïèµ¨oÊzåD @Åx" OïùºIS5È&À |
| --- | Minor | ¸Ö?^þ _zº×zP6µ¤å	küÒ)³²bimXY»´Ú­l\:#WN/ùÅ@sK-ÔÊE×+oiüÊ{j_ÉËmkqjLK-ã*º%V«¨J]!x/©¦ÌÞ¤ïÉH©ø9&gÄÚ?KÓ{¨:ÆzzeÜ2ÐZâlX§WÄç½,/Å%HÁ7}Ò1ío)®è= ´<¤¯f)óMÍÒFCÈLXäYJ½v°Êæ7~(^%QóìI\ÅGýµÈRI) ô é.8âÇ§Å1©!ë¡6®´Y~5IdýPiÔ©Y°îUj¬ã¥U¤ e8ÐCèCo¡&hßN¢#W´ýEfÑ#½£j¥¢. ^ä{Ó`RP¦GÖ¥Ë´YOàDÐÛXÎ ªm¹£Í:KXgAô îZ¤Ý¤3²ðü Ú4`½áë¹IzÃ +³ôGoy¦H^²ã{­ `DMð_Þ@½ ?ç7ÑWè~Z¥¤múxÀ_Ø 6ðþ?wÑ°z#,ÄÈrÌpLtXz×Ó¤)éH[»ø°!tH3Aô" |
| --- | Minor | ¥ñÔ©b(aÞ­£UÏ ÕNLÒ8¤$2ïiæ¤qö¥¤P¡Ûl¡åHEoÖoÉ¤vbD-ô2½ ³yqÌö ÑÉ©ÑÎºðkùk¶½ôDv~1d;¡F¢W_)zÇHpIû>¹@ÜDÈNaÐ'ÔDv"ÒÔl4ÿbB+GÀp@uíåÑe2N)õB<y¢HÉÒ¬¼IÁÌ½ &r¡ßzRË,Û©dÔÕ]4gb«LtJ¡! |
| --- | Minor | íÔT	E§LÅê§Òg+(©u¯¡\+3teÆ®Ìà½2ÃWfüÊY1+3heF­ôSî'ýÿ3ÛÐØNÃç2]f¤ËuÑ-3¼eÂ÷óSXIQ±âÎ¶@þ)³É?£¯fû~°­ð£I9<f>5³Êì§2Nj?ÎjßDcíNûÉaé|LÖPÙåTv9ÒÝêf%%æâC [^Zæ©eZæ©eÎrÊô§² G®håI@ÈÚM@9§HÄÖS9c©É¥fsU#þÆIËêNE	cÒÉùO"G¤ÍÙ¢ç[/Uj³ÊéFe «d3Ê)GÅIÆ9fÝõrÄ±	+_®jN züzÜØý=®SI.7t.7t.7t.­u®­u.?t.?t.¯u®¯uy:û±Î!OÇI4Fs*ëqF¾jó*#ßwf¢J@ÊÇ²rU`ÊéOç*Bç*Bç*Âä*Â)1³ÑªÂ1Îb¿ÈÌKHá&§JòzT¼J%FÊS	æEÉoZ. ËJ7"¯«zÂäºÇÈ©¤oÔ\Ò÷jÌÐ(éû.>çyÁäm÷LÞh0y§Áä­£¦ÑòTô(¡øÓâÇ@e²ð.{åÄhrb491MN&'F×¦lY=3åÄÆÌ9±9±1#'ö]ü1&³Rö>ÊæG®LÎn&g73Ý=qvóþ|Uçº#ß'zf<ÉûÙQ  §³~Òð¼þ*W	tÁUûbsµ]¸ûeIäé"U&úô~³>ìî}¾~¹ù¡ù×öð¦yyîï7¯·_Ýï®Þ]nîýrõóöîêõÛ_<ùÇÓÀíîöÙú°yôì¿°r"-QPYûDÿÄÿÓ_Þmn/xÓ1ßwýñö°bI^ì®6í·ûÍï7Û[öÅú-LçRllËå~§¤ïtÇ yº>¬ov×§Ó#b×9¡lbzÐnÖvüèí*Î {Ò	ô¬ÆádX®îÇÑLÿSÞóÇ{Ï½¼OT½Mí!Â³[Ñs |
| --- | Minor | C=â×ÆùyôÌàÇçÎÀSÿ. >Ãéï#YS¹i9~è-qOw>;öãWVÂCN÷¼j¤Çñ@ov'}Fy57ÿqd¹uÒ6Õ©6()£Où¨¢Ín. éÕó7ô=ðÃWC±W=KùFQrÆK¡|e¾ô·ÄSó³H¦;q;t$©½ô\êPA£ù¹GMåJ#ÅVbzÌ~:úª(ÿøyIþÓ}4ÿ¹ èÇÌé9å?0. ËÅ ºÖñÙIÜTÆ)UÏµU  Ò§ó ÒìVË¿ÔÈæ¿ìC7ðª¾h`êS·Öã²}éáÐ¨«G®tÔªe¦(2hkÐ¼I±¬ëÿV´º 9oqkã õj=yWÔýuºy»|Dþûçü§=¯yÑi;mÿùg=eo%òÀD«ñ´"÷1Æò)A2vYÿRñFosPN#¬ïÇ [ßTì1ô·L1/J°ÓIÐTñ?yoÍêì¶§K`ÛÄÈq^úL&ýiAR$yÆ2zYÄûÀsÐJÔ/zIM*ws¼Jû=: ïèµ¨oÊzåD @Åx" OïùºIS5È&À |
| --- | Minor | ¸Ö?^þ _zº×zP6µ¤å	küÒ)³²bimXY»´Ú­l\:#WN/ùÅ@sK-ÔÊE×+oiüÊ{j_ÉËmkqjLK-ã*º%V«¨J]!x/©¦ÌÞ¤ïÉH©ø9&gÄÚ?KÓ{¨:ÆzzeÜ2ÐZâlX§WÄç½. /Å%HÁ7}Ò1ío)®è= ´<¤¯f)óMÍÒFCÈLXäYJ½v°Êæ7~(^%QóìI\ÅGýµÈRI) ô é.8âÇ§Å1©!ë¡6®´Y~5IdýPiÔ©Y°îUj¬ã¥U¤ e8ÐCèCo¡&hßN¢#W´ýEfÑ#½£j¥¢. ^ä{Ó`RP¦GÖ¥Ë´YOàDÐÛXÎ ªm¹£Í:KXgAô îZ¤Ý¤3²ðü Ú4`½áë¹IzÃ +³ôGoy¦H^²ã{­ `DMð_Þ@½ ?ç7ÑWè~Z¥¤múxÀ_Ø 6ðþ?wÑ°z#. ÄÈrÌpLtXz×Ó¤)éH[»ø°!tH3Aô" |
| --- | Minor | ¥ñÔ©b(aÞ­£UÏ ÕNLÒ8¤$2ïiæ¤qö¥¤P¡Ûl¡åHEoÖoÉ¤vbD-ô2½ ³yqÌö ÑÉ©ÑÎºðkùk¶½ôDv~1d;¡F¢W_)zÇHpIû>¹@ÜDÈNaÐ'ÔDv"ÒÔl4ÿbB+GÀp@uíåÑe2N)õB<y¢HÉÒ¬¼IÁÌ½ &r¡ßzRË. Û©dÔÕ]4gb«LtJ¡!. |
| --- | Minor | Sentence exceeds complexity threshold, split for readability. Applying the split needs --strength moderate or higher. |
| --- | Minor | none (split proposal only; source not rewritten) |
| --- | Minor | none |
| --- | Minor | Check: NEEDS-LLM |
| --- | Minor | Flags:    not-assessed |
| --- | Minor | SENTENCE (Line 1848, 118 words, 1 clauses)  [Script] |
| --- | Minor | ÉÀ´ODËFP!iab-å8=òÈùáFÎ´ùµå4}ÜÁõCus áJDÙ÷sÂÊ©áFè1éGØj>FÄà{ìè°zøhòÑåc¦¥xÎK¼ð¯XÜ®¸"P&úÌ |
| --- | Minor | .¨ÕªÛ½ÿxw{h¿y÷êÀ;×ÏÑwjíëý[zñü§ïÞûüÅ×»·ëÛ§ë»½O¾Þ\¿»YßÓo~Ý6oß¾Þñ¯×Ûýáþ×GW»WÇí÷Wûííõ£çWÛÃöðëcÌvww³yK¿9ºs<Ûì/ï·wÝ=CÚJö= %ÚïùDÃß>#Úý%Ñ ÂÑ+)øü¦ý\}×ØåO7Ûë7©ÏÅÏ×ßo¯o(´2©éw'´-ÿnVðû¥Äª}~Xßl//n¯o6h?¾Y_ïº¿ÞlÀËWëÛÝ~ó¾(ÿY1øï,ýp\ÔëãíÍÑ²Üÿ­nô³	Ñ;sa§'EýO>m?º½Ü]Á$mu-)îj |
| --- | Minor | |núæåîÛÛ-zo8! |
| --- | Minor | ÉÀ´ODËFP!iab-å8=òÈùáFÎ´ùµå4}ÜÁõCus áJDÙ÷sÂÊ©áFè1éGØj>FÄà{ìè°zøhòÑåc¦¥xÎK¼ð¯XÜ®¸"P&úÌ |
| --- | Minor | .¨ÕªÛ½ÿxw{h¿y÷êÀ;×ÏÑwjíëý[zñü§ïÞûüÅ×»·ëÛ§ë»½O¾Þ\¿»YßÓo~Ý6oß¾Þñ¯×Ûýáþ×GW»WÇí÷Wûííõ£çWÛÃöðëcÌvww³yK¿9ºs<Ûì/ï·wÝ=CÚJö= %ÚïùDÃß>#Úý%Ñ ÂÑ+)øü¦ý\}×ØåO7Ûë7©ÏÅÏ×ßo¯o(´2©éw'´-ÿnVðû¥Äª}~Xßl//n¯o6h?¾Y_ïº¿ÞlÀËWëÛÝ~ó¾(ÿY1øï. ýp\ÔëãíÍÑ²Üÿ­nô³	Ñ;sa§'EýO>m?º½Ü]Á$mu-)îj |
| --- | Minor | |núæåîÛÛ-zo8!. |
| --- | Minor | Sentence exceeds complexity threshold, split for readability. Applying the split needs --strength moderate or higher. |
| --- | Minor | none (split proposal only; source not rewritten) |
| --- | Minor | none |
| --- | Minor | Check: NEEDS-LLM |
| --- | Minor | Flags:    not-assessed |
| --- | Minor | SENTENCE (Line 1848, 804 words, 6 clauses)  [Script] |
| --- | Minor | ae9þôü»?¤zòáîæêÏC&þÈÀç1jÌxÂL Ãñ[Âß'1£ªf gZ5bÂ 1VIâçBÅ?J<*Ïøøâûo;VÄôm«T¤V5TK7ý2TôiVP)7¨sËñs¡@%¡¢zV^þýå§_þÞÅýv}	½øæ¡¡m'ìïC BQz¹ûäù³ë»NÆß |
| --- | Minor | »6J|êÓ¡ÆY¡F Ô¥OèBE÷J s6æbò¯¨ÑºfiMvøH÷P QÑìÏ@Ì4ñS`Rnð¯q"Ï)?~ôí·_>­ ÷g0 *Nü bÝ\L±f~0o*Yh½ÑÁñDÀZ-ê`3N¼ø_/sª¬K'ÏÊùsÃK~Äbu>n.>ûôéOUÜüyµn¾E³ù=Àqq8±J¡`JåÿÈZwVZò}²Zìh£6\¹AÿrÐ=Uë¬â=¿ç5ÝKt¿?<}³¾fùIÁt®ªö·O>ûìÇ÷¾xñ9aà ·1.p@Á "AAW}0è1¡ Á·ÞYUær!?FA`¯GíúæîÍº}µ9¬ÛëõÛ·ëößtJÃúûÏõÝÝº½Y¿}uµnß¾koßµ÷oví~{¾õ»ön¿m7øs³»mïÞle{@ VïI®öÇÝU{¹#Ú7ý¾Ýß¬÷oÚkºÅk7hµµ´¶k?k_´_´_¶_µo¿n¿m×íe»i¯Û7í¶ýgû¶Åí·÷í¾=´ïÚÛµ¿¶ÿ~ÜÃu`(ý 	S_ endstream endobj 788 0 obj <</Type/ObjStm/N 51/First 445/Filter/FlateDecode/Length 2388>> stream xÚµY[oÚJ}ÿ~Ï§*g.¥ªÐ¤BCäô¨¦`Õ`j6é¯?{°ÓJfa.k­½gï=DzØJzÄ'QOL7ð£	<E}OØ¸ð(A@F2øÀGÌX±zxÀWø¥2ð¦eÌaå Æaø¾pª ÆÌ¬Êàð|êÃ¤,0óHÏÔÌ;S°)`Ya'Xz P@a³Må1îsø |
| --- | Minor | %à V]z£HDJ3ÆàÈÌã\ÁÌÃÏï	³mûðsá8æà\ÂQ¤'RÁ8¡(mÂzf	!ÂáL°UÉàÈ @1ÒÉà33ÀzÐðhãæWÐÃé)¥`2+ÀÂ^àÃç·oÑÍãB£v2ÏÑ`9ÌMÇ|!è&ù4FÉXÃöÅ×è.çÓºªè¶£4Ë[Ó0õX:áºÍ1j.&ì]u×WoZÝkY¬pª³Q-ò$-¼{÷?{Û¨.Îu4æ°ÙHÏ¡0dÆö	ÎEÆÑ¨1ÄÚÃhëÙ- Úq8s6ÉÃ¿'Tz'ëT&9þRü­Å¸ýtþJæå?ÿczáLÛ'ÙÙr5jÀhÞEMmA#TlQ»ìßw®ºf-÷a(á5l{°Ñ:°õ§£4£NÍjh¦zë¯ëVjvñ2C¿tlFù4Õ}M)úýÐ(P¦è9*Îæ%1Ì¬¿/Ã5PµÐ):CïÑ%úè}B·è |
| --- | Minor | ëöjÕQ³¯±~@!¢#&(B1¡9JÐ¥(C9Z¢GñX[üÛÔï í Û [|ºi´z·°Øà¬du ðÿØ!ÿ°¿1[+áµ ½úýLÃ±Æád¢SK/Ï«àsñçn9o>í`î³û2ÎI]ÎñKoÌÉ2/ÉÀÜ²Ü?RRléýdÜÃhbÙ·éYVhuþüôË¦óKÓË³YU¹~È·½q-âðMÃüg4ÖöÍLÍ!¬eñç`\ßkÅÁ£Àb¹~~ÙhÃrÝµÏ(}m?î²T¥¦Ì6 Ñ\o.1vÙê<DðGiDÀýf,ê¸Ü8Qã<¿Ãü-íc×YbbaÐÈÂ0 ýñûÝóËæî Ù-3¿>È¼¶áàÃ¨ïAtI}æ{ÝAÖw=³ÐrP.æÂÅ	ÈWïâ¦5øÜ4K½«8(¶ ­Ap[¬5)Ø¾&Å^`feöiêc']ìTÝ[¹ÙüxÓ+¼9ó£]Ê¢Ì}Ëjï¥\Ô²K\ö |
| --- | Minor | ;Î:emHéJ²é2¿"Ôíô¯Þ¯K GKDûb¹ïÉN¤ûr[·¡6ê@8®£O{&èGIÄiASßåa7àä}øýøOçc§ðÙbßËÔxÍ« <ï¾ÀAB+6¨)ì²±t®n¦ÒÃ}dûVëTU¶.NMßüÁJ\oOoßß\¿ét¯Y8f\ |
| --- | Minor | iv1ÿÀ¤×zeyúøWcÂ«t6üu1ÓG9\åb±L=pT{;½ó¨Âè>¨ç!_¬°pA^#X1B¦a»^êpPæ¾qÀ`vh þf %ÙR4Èc |
| --- | Minor | ó ýoà*oÅ³KQ¬ðVtBò¬¾ìð²¡ãw\T|{8ÞIúx§évLrß1QúÜ>ÊÅrzzqvwÛé&óüäÅÂvÅ"jEBû$Jé¶H¹³¶ãcÆ!ðMÁÊ<J`"Êµ"ÑJP©*ôl­pW+ò ­TL°VÛ×¸VÚýÞFºêZQ;ZQøOùUEQG+bãXÌc¡ü5K|¶XG, é]eÚ®XØAåNÄCEÍ¼ºqÑl]ç^Ä£ðÑÝåÕ^¦<âÓ îí-_L«÷ÒiûpõT.AÍ£Fç¼ý¡ob«`Hr´leÓÁ&6¯;¡£«ß^ñ½hóR´z'2oDj¿ÍJ2rÞÚTún]Óß­kbsi¿4ïÏNûEîZBæÇ¬êh] áûî8Ãx1ÝTB²ùÿ-\,B³á8Dó%J§	071æ,ZW/Gë>ÃlZwº¨^5£¢îü­x´[ ïèý²künõYrË©>¯ùhóù¾wßnÖ]B´ _ùNÇ©µÌCºü2ßµ}y{é1ÌBØ>t}ÝtØW5ÖÍË^ÿ¶(ñ |Äzµ¬¬W«§¤¸ÄçêÕöaê%¿W+ÑÎ}/{­îy¿HK`â¯ûù| Lî«LÅw%#µ÷Óbû|E¯ýÛÎå6ñZæÁ«¢»Á+ûàUðê¬Ø	^E°	^I`¼ü²ï8|Aß®³þN [¤E±òÝ8ÇÏ~hËVe7'eËò?õêL endstream endobj 806 0 obj <</Type/XRef/ID[<3fa81f769841a402db35795406a36751><3fa81f769841a402db35795406a36751>]/Root 1 0 R/Info 2 0 R/Size 807/W[1 3 2]/Filter/FlateDecode/Length 1897>> stream xÚ5ØyPV×ÇñûÜû"QEqA(nq |
| --- | Minor | ÄPAV |
| --- | Minor | 4"hÜ ¸/(.¸ï8±íØNvh¦i§í´ikg2¶ö=ßóðÏgùç{¹ï½ç½/ã8¯_»é|ð=¼ux¯ám¼÷ð>ÄûØðëx¡.ú°ë8a#nèwfÔ_ºè¡0í¬7°9¶À l­0X§µ®Ü3LÝC°-b;lÏ¹ÙõÃ°cGFí;agqBþ¥GéÂQ¦RG`WÄ(ìÑob,ÆawìñØ°&b&coì)Øûañ-pÅaø6ÇTïàH%NÜWzÞå dPÆ1\±öú¥nah? |
| --- | Minor | ae9þôü»?¤zòáîæêÏC&þÈÀç1jÌxÂL Ãñ[Âß'1£ªf gZ5bÂ 1VIâçBÅ?J<*Ïøøâûo;VÄôm«T¤V5TK7ý2TôiVP)7¨sËñs¡@%¡¢zV^þýå§_þÞÅýv}	½øæ¡¡m'ìïC BQz¹ûäù³ë»NÆß |
| --- | Minor | »6J|êÓ¡ÆY¡F Ô¥OèBE÷J s6æbò¯¨ÑºfiMvøH÷P QÑìÏ@Ì4ñS`Rnð¯q"Ï)?~ôí·_>­ ÷g0 *Nü bÝ\L±f~0o*Yh½ÑÁñDÀZ-ê`3N¼ø_/sª¬K'ÏÊùsÃK~Äbu>n.>ûôéOUÜüyµn¾E³ù=Àqq8±J¡`JåÿÈZwVZò}²Zìh£6\¹AÿrÐ=Uë¬â=¿ç5ÝKt¿?<}³¾fùIÁt®ªö·O>ûìÇ÷¾xñ9aà ·1.p@Á "AAW}0è1¡ Á·ÞYUær!?FA`¯GíúæîÍº}µ9¬ÛëõÛ·ëößtJÃúûÏõÝÝº½Y¿}uµnß¾koßµ÷oví~{¾õ»ön¿m7øs³»mïÞle{@ VïI®öÇÝU{¹#Ú7ý¾Ýß¬÷oÚkºÅk7hµµ´¶k?k_´_´_¶_µo¿n¿m×íe»i¯Û7í¶ýgû¶Åí·÷í¾=´ïÚÛµ¿¶ÿ~ÜÃu`(ý 	S_ endstream endobj 788 0 obj <</Type/ObjStm/N 51/First 445/Filter/FlateDecode/Length 2388>> stream xÚµY[oÚJ}ÿ~Ï§*g.¥ªÐ¤BCäô¨¦`Õ`j6é¯?{°ÓJfa.k­½gï=DzØJzÄ'QOL7ð£	<E}OØ¸ð(A@F2øÀGÌX±zxÀWø¥2ð¦eÌaå Æaø¾pª ÆÌ¬Êàð|êÃ¤. 0óHÏÔÌ;S°)`Ya'Xz P@a³Må1îsø |
| --- | Minor | %à V]z£HDJ3ÆàÈÌã\ÁÌÃÏï	³mûðsá8æà\ÂQ¤'RÁ8¡(mÂzf	!ÂáL°UÉàÈ @1ÒÉà33ÀzÐðhãæWÐÃé)¥`2+ÀÂ^àÃç·oÑÍãB£v2ÏÑ`9ÌMÇ|!è&ù4FÉXÃöÅ×è.çÓºªè¶£4Ë[Ó0õX:áºÍ1j.&ì]u×WoZÝkY¬pª³Q-ò$-¼{÷?{Û¨.Îu4æ°ÙHÏ¡0dÆö	ÎEÆÑ¨1ÄÚÃhëÙ- Úq8s6ÉÃ¿'Tz'ëT&9þRü­Å¸ýtþJæå?ÿczáLÛ'ÙÙr5jÀhÞEMmA#TlQ»ìßw®ºf-÷a(á5l{°Ñ:°õ§£4£NÍjh¦zë¯ëVjvñ2C¿tlFù4Õ}M)úýÐ(P¦è9*Îæ%1Ì¬¿/Ã5PµÐ):CïÑ%úè}B·è |
| --- | Minor | ëöjÕQ³¯±~@!¢#&(B1¡9JÐ¥(C9Z¢GñX[üÛÔï í Û [|ºi´z·°Øà¬du ðÿØ!ÿ°¿1[+áµ ½úýLÃ±Æád¢SK/Ï«àsñçn9o>í`î³û2ÎI]ÎñKoÌÉ2/ÉÀÜ²Ü?RRléýdÜÃhbÙ·éYVhuþüôË¦óKÓË³YU¹~È·½q-âðMÃüg4ÖöÍLÍ!¬eñç`\ßkÅÁ£Àb¹~~ÙhÃrÝµÏ(}m?î²T¥¦Ì6 Ñ\o.1vÙê<DðGiDÀýf. ê¸Ü8Qã<¿Ãü-íc×YbbaÐÈÂ0 ýñûÝóËæî Ù-3¿>È¼¶áàÃ¨ïAtI}æ{ÝAÖw=³ÐrP.æÂÅ	ÈWïâ¦5øÜ4K½«8(¶ ­Ap[¬5)Ø¾&Å^`feöiêc']ìTÝ[¹ÙüxÓ+¼9ó£]Ê¢Ì}Ëjï¥\Ô²K\ö |
| --- | Minor | ;Î:emHéJ²é2¿"Ôíô¯Þ¯K GKDûb¹ïÉN¤ûr[·¡6ê@8®£O{&èGIÄiASßåa7àä}øýøOçc§ðÙbßËÔxÍ« <ï¾ÀAB+6¨)ì²±t®n¦ÒÃ}dûVëTU¶.NMßüÁJ\oOoßß\¿ét¯Y8f\ |
| --- | Minor | iv1ÿÀ¤×zeyúøWcÂ«t6üu1ÓG9\åb±L=pT{;½ó¨Âè>¨ç!_¬°pA^#X1B¦a»^êpPæ¾qÀ`vh þf %ÙR4Èc |
| --- | Minor | ó ýoà*oÅ³KQ¬ðVtBò¬¾ìð²¡ãw\T|{8ÞIúx§évLrß1QúÜ>ÊÅrzzqvwÛé&óüäÅÂvÅ"jEBû$Jé¶H¹³¶ãcÆ!ðMÁÊ<J`"Êµ"ÑJP©*ôl­pW+ò ­TL°VÛ×¸VÚýÞFºêZQ;ZQøOùUEQG+bãXÌc¡ü5K|¶XG.  é]eÚ®XØAåNÄCEÍ¼ºqÑl]ç^Ä£ðÑÝåÕ^¦<âÓ îí-_L«÷ÒiûpõT.AÍ£Fç¼ý¡ob«`Hr´leÓÁ&6¯;¡£«ß^ñ½hóR´z'2oDj¿ÍJ2rÞÚTún]Óß­kbsi¿4ïÏNûEîZBæÇ¬êh] áûî8Ãx1ÝTB²ùÿ-\. B³á8Dó%J§	071æ. ZW/Gë>ÃlZwº¨^5£¢îü­x´[ ïèý²künõYrË©>¯ùhóù¾wßnÖ]B´ _ùNÇ©µÌCºü2ßµ}y{é1ÌBØ>t}ÝtØW5ÖÍË^ÿ¶(ñ |Äzµ¬¬W«§¤¸ÄçêÕöaê%¿W+ÑÎ}/{­îy¿HK`â¯ûù| Lî«LÅw%#µ÷Óbû|E¯ýÛÎå6ñZæÁ«¢»Á+ûàUðê¬Ø	^E°	^I`¼ü²ï8|Aß®³þN [¤E±òÝ8ÇÏ~hËVe7'eËò?õêL endstream endobj 806 0 obj <</Type/XRef/ID[<3fa81f769841a402db35795406a36751><3fa81f769841a402db35795406a36751>]/Root 1 0 R/Info 2 0 R/Size 807/W[1 3 2]/Filter/FlateDecode/Length 1897>> stream xÚ5ØyPV×ÇñûÜû"QEqA(nq |
| --- | Minor | ÄPAV |
| --- | Minor | 4"hÜ ¸/(.¸ï8±íØNvh¦i§í´ikg2¶ö=ßóðÏgùç{¹ï½ç½/ã8¯_»é|ð=¼ux¯ám¼÷ð>ÄûØðëx¡.ú°ë8a#nèwfÔ_ºè¡0í¬7°9¶À l­0X§µ®Ü3LÝC°-b;lÏ¹ÙõÃ°cGFí;agqBþ¥GéÂQ¦RG`WÄ(ìÑob. ÆawìñØ°&b&coì)Øûañ-pÅaø6ÇTïàH%NÜWzÞå dPÆ1\±öú¥nah?. |
| --- | Minor | Sentence exceeds complexity threshold, split for readability. Applying the split needs --strength moderate or higher. |
| --- | Minor | none (split proposal only; source not rewritten) |
| --- | Minor | none |
| --- | Minor | Check: NEEDS-LLM |
| --- | Minor | Flags:    not-assessed |
| --- | Minor | SENTENCE (Line 1848, 379 words, 5 clauses)  [Script] |
| --- | Minor | q8^!ÉºæÖÌ¢ÎÆ÷0ÓÄI¤ÅÉÈñßQNF&ö³ÄÉ Ô|²8LgÁ_4ÉD{æÓÄ)lÔ|º8Å]Mgñ2MfáLÌ§¤LóâXk:ü I8¥Á&)k§GË=ísp®?¥ùû8çsö{ÍÆÕ°ç° áBü sq1.Á¥\áØd.Ç¸?§®@µcå0+;¯Æ<\1ö_ëp½8ÏòuÍYÓþuù¸7ãßlÏ'ôÌ§Þ¸±·àVü£Ç`7q~lú¼¶±½VÛqîÄ]X%"Þ¯uÖgÌ²×óîÅÏq·Hx3íÜ#ÝÎÿJtÓßøÀ}"1w4ß/2á[ÓV§I9ÄRô-dÌ7Ï5©Éü·I²~2Î8`3Îz©±dWj~ä.×ä8ãb®ÝNä}££'µ÷I |
| --- | Minor | Å3xJ¤h¶v)N3çP|Qj<U"%MçvNäÊÿLgmÓY]ÆKxA¤>Gó"wëLç½¦'å ÖbÖÜOÒÑ«x |
| --- | Minor | ¯ã |
| --- | Minor | ·ð¶ÈÙÚo¿³ü÷¿¤ê7Î¼wE~¡÷D^4gòâÏ4àc|(ò}¨æÄm>À|£5çiõ¯,hGtXëFqãOú;½U¦?þÚï¡°¸	¦§_í	äÌWQ¿Í±aKlÁØÛ`¸C¾ÒÕÚ²Zu;Åö&nZºvv ó#êpìÄ³B{:Ó³ºF`WÄ(ì&n^¾ÎfV>÷aöÀÆ`,¾qân«Ñ¹Ýû	u·¬öd´:{a"&a2öÆ>ØS°öÇ8PÜª§ºþ[¬¿zÆ!8âpqïé¬·õ)u*÷¿ÔÑwÝ&îójMFì¤ÅéIöüß÷W¹:k4³©Çà8ãq¦a:N÷Åh]Á¾î¦p NÃ©830³p¸ª«ÍdµÏ©gafãlsð}qÿ³IçÎÃÓ¬öÎ~âûq/Úõçc5=±h[Ôöy9FmïÌ´ß­Ý¨¯ã>¬%oöùºÐ¾9w§~{HâÐ>a#.ÄEFbÆ£½çíµí}ònÃí¸í]±í}¾1ð6ÁãxOâ)<ñ,Vá9<wð"^ÂË¸b |
| --- | Minor | ^Á:¬Ç«x |
| --- | Minor | ÷ñ>ÄGøoàM\Îµ²;ýÍv ÇØ	;Ó¹Ú¾¥G >l!hwE»®ÄIÚ£Ý¯bÐîHö)+ÁR´û³}vÊð ã!¬ÀÃX«ñ(+;(èa 6Cû-`÷»{¯C»÷~ù¸7¢Ý'7á´ûùZñ=ÿ1'b/LÄÞÉ8 û` öÅ~Øã@´»å Cp(ÇqhwÈTvW´;á(´¿5ì.7Çâx´¿Òp?ÎÁtp ÎÀé³ÑîZÙ¸çâBvßXö¹ÎE{¿-ÅB´wÑZ\kp®Cû¼7â&ÜE¸·b	îÀ]¸íìñ"7(óèÅø±ÃqÅÆ0&é§_*^â;£Ixãg´ÿjrP¼ôz,Ø¬I¹x´> ß>Õä¬xßý¤ux/«ÍèïÛhR/Þsµ>'Þßj}Ý_7­p^|IZßò×»´®_TÖwýµ®ßg<ßÔ­//oÖýu¥ÖÅWºJÿÓÞ_­ù%ñU¤jÞÅ_j~Y|×ó5ô×/5¯ßÓXÍ£ýu¡æWÄ÷læ}üõÏ5¯õï-ME#£"¾?mÐN0c¶ÂÖí0;a,vÇxLÀDLß«Çù?Ew%Y endstream endobj startxref 324658 |
| --- | Minor | q8^!ÉºæÖÌ¢ÎÆ÷0ÓÄI¤ÅÉÈñßQNF&ö³ÄÉ Ô|²8LgÁ_4ÉD{æÓÄ)lÔ|º8Å]Mgñ2MfáLÌ§¤LóâXk:ü I8¥Á&)k§GË=ísp®?¥ùû8çsö{ÍÆÕ°ç° áBü sq1.Á¥\áØd.Ç¸?§®@µcå0+;¯Æ<\1ö_ëp½8ÏòuÍYÓþuù¸7ãßlÏ'ôÌ§Þ¸±·àVü£Ç`7q~lú¼¶±½VÛqîÄ]X%"Þ¯uÖgÌ²×óîÅÏq·Hx3íÜ#ÝÎÿJtÓßøÀ}"1w4ß/2á[ÓV§I9ÄRô-dÌ7Ï5©Éü·I²~2Î8`3Îz©±dWj~ä.×ä8ãb®ÝNä}££'µ÷I |
| --- | Minor | Å3xJ¤h¶v)N3çP|Qj<U"%MçvNäÊÿLgmÓY]ÆKxA¤>Gó"wëLç½¦'å ÖbÖÜOÒÑ«x |
| --- | Minor | ¯ã |
| --- | Minor | ·ð¶ÈÙÚo¿³ü÷¿¤ê7Î¼wE~¡÷D^4gòâÏ4àc|(ò}¨æÄm>À|£5çiõ¯. hGtXëFqãOú;½U¦?þÚï¡°¸	¦§_í	äÌWQ¿Í±aKlÁØÛ`¸C¾ÒÕÚ²Zu;Åö&nZºvv ó#êpìÄ³B{:Ó³ºF`WÄ(ì&n^¾ÎfV>÷aöÀÆ`. ¾qân«Ñ¹Ýû	u·¬öd´:{a"&a2öÆ>ØS°öÇ8PÜª§ºþ[¬¿zÆ!8âpqïé¬·õ)u*÷¿ÔÑwÝ&îójMFì¤ÅéIöüß÷W¹:k4³©Çà8ãq¦a:N÷Åh]Á¾î¦p NÃ©830³p¸ª«ÍdµÏ©gafãlsð}qÿ³IçÎÃÓ¬öÎ~âûq/Úõçc5=±h[Ôöy9FmïÌ´ß­Ý¨¯ã>¬%oöùºÐ¾9w§~{HâÐ>a#.ÄEFbÆ£½çíµí}ònÃí¸í]±í}¾1ð6ÁãxOâ)<ñ. Vá9<wð"^ÂË¸b |
| --- | Minor | ^Á:¬Ç«x |
| --- | Minor | ÷ñ>ÄGøoàM\Îµ²;ýÍv ÇØ	;Ó¹Ú¾¥G >l!hwE»®ÄIÚ£Ý¯bÐîHö)+ÁR´û³}vÊð ã!¬ÀÃX«ñ(+;(èa 6Cû-`÷»{¯C»÷~ù¸7¢Ý'7á´ûùZñ=ÿ1'b/LÄÞÉ8 û` öÅ~Øã@´»å Cp(ÇqhwÈTvW´;á(´¿5ì.7Çâx´¿Òp?ÎÁtp ÎÀé³ÑîZÙ¸çâBvßXö¹ÎE{¿-ÅB´wÑZ\kp®Cû¼7â&ÜE¸·b	îÀ]¸íìñ"7(óèÅø±ÃqÅÆ0&é§_*^â;£Ixãg´ÿjrP¼ôz. Ø¬I¹x´> ß>Õä¬xßý¤ux/«ÍèïÛhR/Þsµ>'Þßj}Ý_7­p^|IZßò×»´®_TÖwýµ®ßg<ßÔ­//oÖýu¥ÖÅWºJÿÓÞ_­ù%ñU¤jÞÅ_j~Y|×ó5ô×/5¯ßÓXÍ£ýu¡æWÄ÷læ}üõÏ5¯õï-ME#£"¾?mÐN0c¶ÂÖí0;a. vÇxLÀDLß«Çù?Ew%Y endstream endobj startxref 324658. |
| --- | Minor | Sentence exceeds complexity threshold, split for readability. Applying the split needs --strength moderate or higher. |
| --- | Minor | none (split proposal only; source not rewritten) |
| --- | Minor | none |
| --- | Minor | Check: NEEDS-LLM |
| --- | Minor | Flags:    not-assessed |

### [Script] VISUAL

| 行号 | 严重度 | 问题 |
|------|--------|------|
| --- | Major | (Page 1) : Content overflows top margin (y=39.9pt, margin=72.0pt) |
| --- | Major | (Page 1) : Content overflows bottom margin (y=734.7pt, page_height=792.0pt) |
| --- | Major | (Page 2) : Content overflows top margin (y=39.9pt, margin=72.0pt) |
| --- | Major | (Page 2) : Content overflows bottom margin (y=734.7pt, page_height=792.0pt) |
| --- | Major | (Page 3) : Content overflows top margin (y=39.9pt, margin=72.0pt) |
| --- | Major | (Page 3) : Content overflows bottom margin (y=734.7pt, page_height=792.0pt) |
| --- | Major | (Page 4) : Content overflows top margin (y=39.9pt, margin=72.0pt) |
| --- | Major | (Page 4) : Content overflows bottom margin (y=734.7pt, page_height=792.0pt) |
| --- | Major | (Page 5) : Content overflows top margin (y=39.9pt, margin=72.0pt) |
| --- | Major | (Page 5) : Content overflows bottom margin (y=734.7pt, page_height=792.0pt) |
| --- | Major | (Page 6) : Content overflows top margin (y=39.9pt, margin=72.0pt) |
| --- | Major | (Page 6) : Content overflows bottom margin (y=734.7pt, page_height=792.0pt) |
| --- | Major | (Page 7) : Content overflows top margin (y=39.9pt, margin=72.0pt) |
| --- | Major | (Page 7) : Content overflows bottom margin (y=734.7pt, page_height=792.0pt) |
| --- | Major | (Page 8) : Content overflows top margin (y=39.9pt, margin=72.0pt) |
| --- | Major | (Page 8) : Content overflows bottom margin (y=734.7pt, page_height=792.0pt) |
| --- | Major | (Page 9) : Content overflows top margin (y=39.9pt, margin=72.0pt) |
| --- | Major | (Page 9) : Content overflows bottom margin (y=734.7pt, page_height=792.0pt) |
| --- | Major | (Page 10) : Content overflows top margin (y=39.9pt, margin=72.0pt) |
| --- | Major | (Page 10) : Content overflows bottom margin (y=734.7pt, page_height=792.0pt) |
| --- | Major | (Page 11) : Content overflows top margin (y=39.9pt, margin=72.0pt) |
| --- | Major | (Page 11) : Content overflows bottom margin (y=734.7pt, page_height=792.0pt) |
| --- | Major | (Page 12) : Content overflows top margin (y=39.9pt, margin=72.0pt) |
| --- | Major | (Page 12) : Content overflows bottom margin (y=734.7pt, page_height=792.0pt) |
| --- | Major | (Page 13) : Content overflows top margin (y=39.9pt, margin=72.0pt) |
| --- | Major | (Page 13) : Content overflows bottom margin (y=734.7pt, page_height=792.0pt) |
| --- | Major | (Page 14) : Content overflows top margin (y=39.9pt, margin=72.0pt) |
| --- | Major | (Page 14) : Content overflows bottom margin (y=734.7pt, page_height=792.0pt) |
| --- | Major | (Page 15) : Content overflows top margin (y=39.9pt, margin=72.0pt) |
| --- | Major | (Page 15) : Content overflows bottom margin (y=734.7pt, page_height=792.0pt) |
| --- | Major | (Page 16) : Content overflows top margin (y=39.9pt, margin=72.0pt) |
| --- | Major | (Page 16) : Content overflows bottom margin (y=734.7pt, page_height=792.0pt) |
| --- | Major | (Page 17) : Content overflows top margin (y=39.9pt, margin=72.0pt) |
| --- | Major | (Page 17) : Content overflows bottom margin (y=734.7pt, page_height=792.0pt) |
| --- | Major | (Page 18) : Content overflows top margin (y=39.9pt, margin=72.0pt) |
| --- | Major | (Page 18) : Content overflows bottom margin (y=734.7pt, page_height=792.0pt) |
| --- | Major | (Page 19) : Content overflows top margin (y=39.9pt, margin=72.0pt) |
| --- | Major | (Page 19) : Content overflows bottom margin (y=734.7pt, page_height=792.0pt) |
| --- | Major | (Page 20) : Content overflows top margin (y=39.9pt, margin=72.0pt) |
| --- | Major | (Page 20) : Content overflows bottom margin (y=734.7pt, page_height=792.0pt) |
| --- | Major | (Page 21) : Content overflows top margin (y=39.9pt, margin=72.0pt) |
| --- | Major | (Page 21) : Content overflows bottom margin (y=734.7pt, page_height=792.0pt) |
| --- | Major | (Page 22) : Content overflows top margin (y=39.9pt, margin=72.0pt) |
| --- | Major | (Page 22) : Content overflows bottom margin (y=734.7pt, page_height=792.0pt) |
| --- | Major | (Page 23) : Content overflows top margin (y=39.9pt, margin=72.0pt) |
| --- | Major | (Page 23) : Content overflows bottom margin (y=734.7pt, page_height=792.0pt) |
| --- | Major | (Page 24) : Content overflows top margin (y=39.9pt, margin=72.0pt) |
| --- | Major | (Page 24) : Content overflows bottom margin (y=734.7pt, page_height=792.0pt) |
| --- | Major | (Page 25) : Content overflows top margin (y=39.9pt, margin=72.0pt) |
| --- | Major | (Page 25) : Content overflows bottom margin (y=734.7pt, page_height=792.0pt) |
| --- | Major | (Page 26) : Content overflows top margin (y=39.9pt, margin=72.0pt) |
| --- | Major | (Page 26) : Content overflows bottom margin (y=734.7pt, page_height=792.0pt) |
| --- | Major | (Page 27) : Content overflows top margin (y=39.9pt, margin=72.0pt) |
| --- | Major | (Page 27) : Content overflows bottom margin (y=734.7pt, page_height=792.0pt) |
| --- | Major | (Page 28) : Content overflows top margin (y=39.9pt, margin=72.0pt) |
| --- | Major | (Page 28) : Content overflows bottom margin (y=734.7pt, page_height=792.0pt) |
| --- | Critical | (Page 1) : Block overlap detected: 4024 sq pt |
| --- | Critical | (Page 1) : Block overlap detected: 1298 sq pt |
| --- | Critical | (Page 1) : Block overlap detected: 1725 sq pt |
| --- | Critical | (Page 4) : Block overlap detected: 5535 sq pt |
| --- | Critical | (Page 4) : Block overlap detected: 1151 sq pt |
| --- | Critical | (Page 4) : Block overlap detected: 127 sq pt |
| --- | Critical | (Page 5) : Block overlap detected: 1008 sq pt |
| --- | Critical | (Page 5) : Block overlap detected: 1111 sq pt |
| --- | Critical | (Page 5) : Block overlap detected: 220 sq pt |
| --- | Critical | (Page 5) : Block overlap detected: 1325 sq pt |
| --- | Critical | (Page 5) : Block overlap detected: 4828 sq pt |
| --- | Critical | (Page 5) : Block overlap detected: 195 sq pt |
| --- | Critical | (Page 5) : Block overlap detected: 1912 sq pt |
| --- | Critical | (Page 5) : Block overlap detected: 928 sq pt |
| --- | Critical | (Page 5) : Block overlap detected: 205 sq pt |
| --- | Critical | (Page 5) : Block overlap detected: 1311 sq pt |
| --- | Critical | (Page 5) : Block overlap detected: 848 sq pt |
| --- | Critical | (Page 6) : Block overlap detected: 4828 sq pt |
| --- | Critical | (Page 6) : Block overlap detected: 1098 sq pt |
| --- | Critical | (Page 6) : Block overlap detected: 4707 sq pt |
| --- | Critical | (Page 6) : Block overlap detected: 345 sq pt |
| --- | Critical | (Page 6) : Block overlap detected: 2563 sq pt |
| --- | Critical | (Page 6) : Block overlap detected: 787 sq pt |
| --- | Critical | (Page 6) : Block overlap detected: 217 sq pt |
| --- | Critical | (Page 6) : Block overlap detected: 195 sq pt |
| --- | Critical | (Page 7) : Block overlap detected: 3815 sq pt |
| --- | Critical | (Page 7) : Block overlap detected: 4273 sq pt |
| --- | Critical | (Page 7) : Block overlap detected: 126 sq pt |
| --- | Critical | (Page 7) : Block overlap detected: 730 sq pt |
| --- | Critical | (Page 7) : Block overlap detected: 514 sq pt |
| --- | Critical | (Page 7) : Block overlap detected: 122 sq pt |
| --- | Critical | (Page 7) : Block overlap detected: 217 sq pt |
| --- | Critical | (Page 7) : Block overlap detected: 1145 sq pt |
| --- | Critical | (Page 7) : Block overlap detected: 803 sq pt |
| --- | Critical | (Page 7) : Block overlap detected: 371 sq pt |
| --- | Critical | (Page 7) : Block overlap detected: 375 sq pt |
| --- | Critical | (Page 7) : Block overlap detected: 534 sq pt |
| --- | Critical | (Page 7) : Block overlap detected: 159 sq pt |
| --- | Critical | (Page 8) : Block overlap detected: 485 sq pt |
| --- | Critical | (Page 8) : Block overlap detected: 669 sq pt |
| --- | Critical | (Page 8) : Block overlap detected: 283 sq pt |
| --- | Critical | (Page 8) : Block overlap detected: 205 sq pt |
| --- | Critical | (Page 8) : Block overlap detected: 601 sq pt |
| --- | Critical | (Page 8) : Block overlap detected: 115 sq pt |
| --- | Critical | (Page 8) : Block overlap detected: 103 sq pt |
| --- | Critical | (Page 9) : Block overlap detected: 4828 sq pt |
| --- | Critical | (Page 9) : Block overlap detected: 4828 sq pt |
| --- | Critical | (Page 9) : Block overlap detected: 4338 sq pt |
| --- | Critical | (Page 9) : Block overlap detected: 5991 sq pt |
| --- | Critical | (Page 9) : Block overlap detected: 119 sq pt |
| --- | Critical | (Page 25) : Block overlap detected: 1900 sq pt |
| --- | Critical | (Page 25) : Block overlap detected: 1095 sq pt |
| --- | Critical | (Page 25) : Block overlap detected: 1923 sq pt |
| --- | Critical | (Page 25) : Block overlap detected: 144 sq pt |
| --- | Critical | (Page 25) : Block overlap detected: 450 sq pt |
| --- | Minor | (Page 1) : Inconsistent body fonts (10 detected): LMRomanCaps10-Regular, LMRoman10-Bold, LMRoman10-Italic, LMRoman12-Bold, LMRoman10-Regular (+5 more) |

## 决策信号

- **委员会评分**: 3.3/10
- **主编裁定**: Desk Reject
- **审稿推荐**: 大修
- **问题包**: 主要 1 / 中等 6 / 次要 0

## 修订路线图

### 优先级 1 --- 必须处理（阻断）

- [ ] Abstract and conclusion claims need explicit evidence traceability ([LLM]; abstract)

### 优先级 2 --- 强烈建议

- [ ] Cross-section numeric consistency should be reconciled ([LLM]; abstract)
- [ ] Em dash found; replace it with a comma, colon, parenthesis, or sentence boundary unless it is... ([Script]; abstract)
- [ ] Novelty claim should be grounded against the closest prior work ([LLM]; abstract)
- [ ] Comparison protocol should make fairness assumptions explicit ([LLM]; method)
- [ ] Em dash found; replace it with a comma, colon, parenthesis, or sentence boundary unless it is... ([Script]; method)
- [ ] Em dash found; replace it with a comma, colon, parenthesis, or sentence boundary unless it is... ([Script]; unknown)
