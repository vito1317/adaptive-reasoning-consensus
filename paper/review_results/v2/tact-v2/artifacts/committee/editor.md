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
