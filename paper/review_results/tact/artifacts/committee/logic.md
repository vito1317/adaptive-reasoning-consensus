# Committee — Reviewer 4 (logic chain)

**Score: 5.5 / 10**

The argument chain in this paper is unusually well-built at the local level — most
paragraphs earn their next paragraph — and it breaks in a specific, repeatable way: the
*scope* of a claim narrows as you move inward from the abstract to the evidence, and the
abstract is never updated to match. Below are the four places where that gap changes what
a reader concludes.

## Breakpoint 1 — the falsification protocol is offered as portable, but its scope
excluded the method's worst failure

The Conclusion's final clause is the boldest in the paper: the falsification protocol,
"having already killed one of the author's own systems, is offered as the more portable
contribution." Contribution C4 says four falsifiers were fixed before implementation and
"All four survived."

F2 reads: "either variant significantly below SC **anywhere on the sweep**."

Now Sec. VIII discloses that in a paraphrased wrong-majority regime, TACT-LF "does not
merely shrink toward SC: it *mis-signs*, saturates at γ = −2.0, and scores 0.000 against
an SC floor of 0.340. None of the four alarms fires." I confirmed this in
`results/isc_eval.json`: `TACT-LF: 0.0`, `TACT-LF_gamma: -2.0`, `TACT-LF_alarms: {}`,
`SC@K: 0.34`, over 400 items.

So the method has a regime where it scores zero against a 0.34 baseline, undetected, and
the protocol reports a clean sweep. The escape is the phrase "on the sweep" — technically
sound, and the paper does disclose the failure honestly and prominently. But the logic
does not close: a falsification protocol whose scope was drawn narrowly enough to exclude
the method's catastrophic failure mode, and which did not find that failure (follow-on
work did), cannot simultaneously be advertised as the portable contribution. Either widen
F2, or state explicitly what the protocol was and was not designed to reach.

Related, and unstated anywhere: `results/tact_hard_eval.json` records
`h2: {passed: false}`. A pre-registered hypothesis of the second real-trace campaign
failed. Sec. VII-F(e) explains correctly *why* the endpoint was unreachable on the
realized substrate — that is a legitimate and well-argued defence — but the paper never
says "a registered endpoint failed", while the abstract says all pre-registered criteria
were survived. Both facts should be in the same voice.

## Breakpoint 2 — the Conclusion promises an anchor the shipped method does not have

Conclusion: "exact fallbacks at both ends, plain self-consistency when the evidence is
absent and CISC when it is at full strength."

The SC end is exact (Prop. 1, shared code path — genuinely nice). The CISC end is not a
property of the shipped method. Prop. 2 obtains it only after replacing the van der
Waerden feature map φ of Eq. (2) with a different log-value map φ^log. Shipped TACT at
large γ is a rank-score vote, which is *not* CISC-power — and that difference is precisely
the source of the monotone-invariance result the paper is proudest of. The method cannot
both reduce to CISC at full strength and beat the entire c^γ family under distortion.

The abstract and C1 both state this correctly ("a log-value feature map reproduces
CISC-power"). Only the Conclusion overstates, and it is the sentence most likely to be
quoted.

## Breakpoint 3 — "two campaigns confirm the premise" inverts what campaign 1 found

Abstract: "Two real-trace campaigns on a frozen model confirm the premise and locate the
binding constraint."

Sec. VII-F(a), campaign 1: D̂ = −0.219, SE = 0.176, z = −1.24, with the paper itself
noting "what little there is points the *wrong way* (math −0.515, commonsense −0.173;
both groups negative)."
Sec. VII-F(e), campaign 2: D̂ = +0.250, z = +2.54.

The abstract quotes only the positive number. If "the premise" means "signed
discrimination is the operative quantity", campaign 1 does support it — and Sec. VII-F(a)
makes that argument well, via the nice ECE mirror-image observation. But a reader of the
abstract alone concludes that verbalized confidence was measured to be positively
discriminative on real traces twice. One clause fixes this.

## Breakpoint 4 — the flagship number's comparator is chosen to maximize the gap

Abstract: the label-free variant "recovers anti-correlated channels that pin every
published protocol to the majority-vote floor (κ = −0.6: 1.000 vs. 0.807)."

In `results/tact_eval.json` at that cell: SignGrid-dev also scores 1.000, TACT-dev γ = −4.0,
SignGrid γ = −4.0, and `paired.TACT-dev_vs_SignGrid = {a_only: 0, b_only: 0, p_value: 1.0}`
— TACT and the trivial signed-exponent grid are the *identical policy on every item*.

The comparison as stated is true: published protocols do sit at 0.807. But choosing that
comparator, in the abstract, for a cell where a trivial baseline ties you bit-for-bit,
reads as a 19-point advance over the state of the art when the honest reading is "a
trivial signed grid also solves this cell; our advantage is elsewhere." Sec. VII-D says
exactly that, clearly and voluntarily. The abstract should not undo it.

## What holds together well

- Sec. V is the best-argued part of the paper: impossibility → why the honest response is
  fallback → the structured escape when a covariate exists → the empirical confirmation
  that the naive control lands *below* the floor. The negative control landing below the
  floor is the right prediction and it came true.
- The Sec. III-setup → Fig. 1 → "the evaluation holds itself to exactly those cells"
  chain is genuinely disciplined reasoning and I want to name it as such.
- Sec. VIII's escalation — window is thin → it does not widen with difficulty → executable
  ground truth buys 7.5% not a different regime → therefore abstention is not conservatism
  — is a real argument with real measurements behind each link.
