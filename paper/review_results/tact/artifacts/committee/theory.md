# Committee — Reviewer 1 (theory contribution)

**Score: 6.0 / 10**

## What the theoretical increment actually is

Stated precisely: *reduce the trust decision in confidence-weighted voting to one signed
scalar, estimate that scalar with its uncertainty, and map it analytically to a vote
exponent that is exactly zero when the evidence is absent.*

That framing is new in this family. The prior art estimates *how much* to up-weight
(CISC's tuned temperature, reliability-aware pseudo-counts, warmup thresholding); none
of it estimates *which direction*. Making the sign a first-class estimand, with a dead
zone that is a shared code path rather than a numerical coincidence, is a real
contribution and is well-motivated by the failure mode in Fig. 1.

The assembly is honestly labelled — Sec. II says "The claim is the assembly and its
anchors, not the parts." I have no complaint about novelty.

## Where the theory is thinner than presented

**The propositions are not uniformly propositions.** Props. 1–3 are genuine mathematical
statements and I verified the algebra: factoring D̂ out of Eq. (8) does give the
multiplicative gain (1 − ν²/ζ²)₊ of Eq. (14); substituting u = √2·z into Eq. (11) does
give γ = z√(2 + 4p̄(1−p̄)z²), which at p̄ = ½ is exactly z√(2 + z²); and
2Φ(1.28) − 1 = 0.799, 2Φ(2.33) − 1 = 0.980, matching the quoted 80% and 98%. The
split-half inversion in Sec. IV-C is also correct: solving p² + (1−p)²/k = α gives
exactly the quoted root.

Props. 4 and 5 are different animals. Prop. 4 asserts something universally quantified
("any per-item rule γ_q = h(D̂ᵍ_q) with h monotone increasing and odd reinforces the
plurality on both branches") and supports it with measured frequencies — 97.5%
agreement, 1 right vs. 9 wrong per 400 items. Prop. 5 has no general statement at all;
it *is* a measured frequency (4%). Labelling measurements as propositions inflates the
apparent theoretical content and makes a reader distrust Props. 1–3, which have earned
the label.

**Prop. 6 carries the most weight and the least support.** "No label-free method can
separate them" is contribution C3 and the boundary the paper offers to all future work.
Its entire justification is one parenthetical: D computed against either truth satisfies
D^{w1} = −D^{w2}. That establishes the *statistic* flips sign. Identical observable laws
is much stronger — it requires the joint law of (answers, confidences) to coincide under
both worlds, constraining cluster sizes and the confidence model of Eq. (1). The claim
may well be true under that generative model; it is not shown. For an impossibility
result offered as a contribution, a half-page proof is the right investment.

**"Proofs are elementary and pinned by unit tests" does not discharge the obligation.** A
test can confirm a measured frequency or verify an identity at sampled points. It cannot
establish a universally quantified claim. The substitution of executable tests for
written proofs is an interesting stance and I am sympathetic to it, but it has a domain
of validity and Props. 4–6 sit outside it.

## The dead zone deserves more credit than it gets

The paper undersells its most defensible idea. An estimator whose null behaviour is
*bit-identical* to the baseline — not "statistically indistinguishable", not
"non-inferior", but the same code path returning the same answer including tie-breaks —
is a strong design property, and combined with the thin-window measurement it supports a
genuine normative conclusion: in this regime abstention is not conservatism, it is
correctness. That is the paper's best theoretical moment and it is buried in Sec. VIII.

## Required

1. Demote Props. 4–5 to numbered Observations, or supply general arguments.
2. Give Prop. 6 an actual proof under the stated generative model.
3. Promote the abstention argument from a limitations paragraph to a claim.
