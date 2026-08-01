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
