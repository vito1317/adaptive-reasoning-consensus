# Committee — Editor (desk-reject screen)

**Verdict: NOT a desk reject. Send for review.**
**Screening score: 7.0 / 10**

*(The Phase 0 script returned "Desk Reject". That heuristic ran in PDF mode with format,
citation, figure and reference checks all skipped, and keyed on abstract length and term
density. Having read the manuscript I overrule it; the position below is the editor
record.)*

## Pitch quality

The hook lands inside the first two paragraphs and it is a good one: every published
confidence-weighted self-consistency method is *structurally* monotone increasing in
confidence, so the possibility that the channel is anti-correlated with correctness is
not merely unhandled — it is not representable. Clean, checkable, and genuinely
unaddressed.

The second pitch — that the stratum on which *any* such method can act is 2–7.5% wide
and does not widen with difficulty — is, if it holds, more valuable than the method
itself. A boundary result that explains why a whole family of interventions
underdelivers is the kind of thing a program committee remembers.

## Venue fit

Good for an IEEE conference on ML/NLP systems. Right length (8 pages, `\balance`d),
correct IEEEtran conference class. The statistical machinery (van Elteren stratified
rank statistics, positive-part James–Stein, a Bayes-discriminant link) is heavier than
the median paper at such a venue but is deployed for a purpose rather than for
decoration, and the paper collapses it into a two-symbol formula before asking the
reader to carry anything.

## Fatal flaws

None. Specifically, I checked the three that would end it:

- **Fabricated or unreproducible numbers.** No. I traced the headline numbers to the
  author's released result files and they match: the +79/−0 with p = 3.3 × 10⁻²⁴ is
  `group-LF_vs_SC` in `results/group_eval.json`; D̂ = +0.250, SE = 0.098, z = +2.54 is
  `results/tact_hard_eval.json`; the LeetCode window 3/40 with CI₉₅ 2.6–19.9% is
  `results/g1_window.json`. The arithmetic in this paper is unusually trustworthy.
- **Hidden negative results.** No — the opposite. The paper volunteers that its
  label-free variant scores 0.000 against an SC floor of 0.340 in a wrong-majority
  regime with none of its four alarms firing, and calls it "the method's sharpest
  unguarded failure mode". Very few submissions do this.
- **Manufactured gap.** No. The claim that no published weighting scheme can represent a
  negative confidence–correctness association holds up against the cited literature.

## Presentation baseline

Meets it, with one prominent exception: the abstract is ~480 words in a single
paragraph and front-loads eight numbers and four estimator components before the reader
knows what problem is being solved. It is the first thing a reviewer sees, it currently
works against the paper, and it is the cheapest fix in the revision.

## Editor's note to reviewers

The concerns worth reviewer attention are not about honesty or competence — both are
above the bar. They are about the distance between what the evidence supports and what
the abstract and section headings assert. Three claims need checking against the
released artifacts rather than against the prose: that the exponent is "derived, not
grid-searched"; that the method "beats the oracle over the entire raw-value weight
family"; and that all pre-registered falsifiers were survived. Each is narrower than
stated.
