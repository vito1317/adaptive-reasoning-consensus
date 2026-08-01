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
