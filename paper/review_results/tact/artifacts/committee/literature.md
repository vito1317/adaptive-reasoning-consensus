# Committee — Reviewer 3 (literature dialogue / gap)

**Score: 7.0 / 10** — the strongest dimension of this submission.

## Is the gap genuine or manufactured?

Genuine. The claim is narrow, structural, and checkable: every published
confidence-weighted self-consistency scheme is monotone *increasing* in confidence, so a
negative confidence–correctness association cannot be represented, only survived. I
checked this against the cited comparators — CISC's softmax weights [2],
reliability-aware pseudo-counts [11], warmup-thresholded filtering [12], self-certainty
best-of-N [10] — and the characterization holds. This is not a gap constructed by
selective citation.

The paper also does the harder thing and refuses the easy version of its own novelty.
Sec. II: "CISC's tuned temperature is already a dev-calibrated SC↔CISC interpolation, so
the novelty of TACT-dev lies in the sign, the rank invariance, and the analytic
(grid-free) map, not in dev calibration itself." Authors almost never volunteer that
their headline baseline already interpolates to their method. Similarly, designating the
published CISC protocol as a *killer* baseline rather than a strawman, and admitting in
Sec. VII-D that TACT trails SignGrid-dev by 0.005–0.015 in the mid-range, is the
behaviour of someone trying to find out rather than to win.

## Is the literature synthesized or enumerated?

Synthesized. The four Related Work paragraphs are organized by *what each line can and
cannot represent*, not by chronology: weighting schemes (can scale trust, cannot sign
it), label-free reliability estimation (needs multiple predictors; here there is one
exchangeable channel), shrinkage and rank statistics (supplies the parts, not the
assembly), and the author's own failed prior system. The crowdsourcing lineage
[13,14,15,16] is correctly positioned as *structurally inapplicable* rather than merely
"related", and the reason given — one exchangeable channel from one model offers no
cross-annotator covariance — is the right reason.

The two-root ambiguity is credited to Parisi et al. [16] and restated for the
single-channel case rather than presented as new. Correct attribution of an inherited
limitation.

## Where the dialogue breaks down

### Four sources that carry reported numbers are uncited

- **CommonsenseQA** — 50 items and a 0.847 trace accuracy in Sec. VII-F, no citation.
- **AIME/AMC** — the "0 of 6 plurality-wrong items" that anchors the upper edge of the
  window claim, no citation.
- **HumanEval+ / MBPP+** — Sec. VIII reports "3.56% recomputed from published
  HumanEval+/MBPP+ tables". A number recomputed from another group's published table,
  with no pointer to which table, in which paper. This is the one I would insist on: it
  is both uncheckable and uncredited, and it is one of the five substrates the abstract
  counts.
- **Claude Haiku 4.5** — named as the frozen model with no version, date, or decoding
  configuration.

GSM8K [23], MATH [26], MATH-500 [27] and LeetCodeDataset [28] are cited properly, so
this reads as omission rather than practice.

### The motivating sibling result cannot be cited or checked

Sec. II: "A preceding system by the author (RLEV-VoI, redundancy-discounted voting with
value-of-information stopping) was evaluated under the same falsification discipline and
*failed* it... Its post-mortem isolated the confidence dilemma studied here." This is the
stated origin of the entire paper and part of the credibility case for the falsification
protocol, and it has no citation, preprint, or artifact. Either cite it or present it as
unpublished background without leaning on it evidentially.

### Two bibliography entries are never cited

[24] Kuhn et al. (Semantic uncertainty) and [25] Wan et al. (Reasoning aware
self-consistency) appear in the bibliography and nowhere in the text — verified by
differencing `\bibitem` keys against `\cite` keys. Both are topically apt; the fix is
almost certainly to cite them rather than remove them. RASC in particular belongs in the
confidence-weighted self-consistency paragraph, since it is a direct comparator.

### IEEE numbering order

References must be numbered in order of first citation. 17 of 26 cited entries violate
this (e.g. Tian et al. is cited second but numbered [6]; Aggarwal et al. thirteenth but
[3]). With a manual `thebibliography` the fix is to reorder the entries.

## Assessment

The positioning work in this paper is better than the average accepted paper at this
venue. The defects are bibliographic hygiene, not intellectual dishonesty, and all are
fixable in an afternoon — with the exception of the HumanEval+/MBPP+ recomputation,
which needs a real citation and ideally the recomputation script.
