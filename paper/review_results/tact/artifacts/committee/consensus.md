# Committee Consensus

**Recommendation: Major Revision**
**Editor verdict: not a desk reject — send for review**
**Confidence in this assessment: High** (most findings are verified against the author's
own released result files, not inferred from prose)

## Scores

| Lane | Score |
|---|---|
| Editor (desk-reject screen) | 7.0 |
| Reviewer 1 — theory contribution | 6.0 |
| Reviewer 2 — methodology transparency | 5.5 |
| Reviewer 3 — literature dialogue / gap | 7.0 |
| Reviewer 4 — logic chain | 5.5 |
| **Mean** | **6.2** |

No lane pair diverges by more than 1.5, so no arbitration was required. The spread is
worth noting though: the two lanes that read the paper's *positioning* (editor,
literature) score it a point and a half above the two that check its *claims against its
evidence* (methodology, logic). That gap is the paper's diagnosis in miniature — the
work is stronger than its claims are calibrated.

## Mechanical score

The skill's count-based formula gives:
base 9.0 − 1.5 × 4 major − 0.7 × 12 moderate − 0.2 × 9 minor = 9.0 − 16.4 → **floor 1.0**.

That number should not be reported as this paper's quality. The formula is calibrated for
bundles of five to eight findings and saturates here because this manuscript is dense
with checkable claims — which is a virtue, not a defect: a vaguer paper would score
higher by offering less to check. The calibrated committee mean of **6.2/10** and the
Major Revision recommendation are the operative signals.

## Consensus classification

`[CONSENSUS-MAJORITY]` on the three blocking issues:

| Issue | Lanes flagging |
|---|---|
| γ_max clip is load-bearing, contradicting "no tuned constant anywhere" | methodology, logic, theory (3/5) |
| "Beats the oracle over the entire raw-value weight family" is a truncated grid | methodology, logic (2/5) |
| No code/data availability statement | methodology, editor (2/5) |
| Falsifier scope excludes the known catastrophic failure; H2 failure undisclosed | logic, methodology (2/5) |

With mean 6.2 and CONSENSUS-MAJORITY, the decision matrix in
`editorial_decision_standards.md` maps to **Major Revision**.

## Top 3 issues to fix first

1. **Reconcile "no tuned constant anywhere" with the fact that γ sits exactly on the clip
   in every cell that carries the paper.** Run the γ_max ablation the paper already
   promises (Sec. VII-C defers it), report where the clip binds, and rewrite C1 and
   Sec. III-D to whichever claim survives. This is the one finding that touches the
   central novelty claim, and the fix is a day of compute plus two paragraphs.

2. **Retire or requalify "beats the oracle over the entire raw-value weight family."**
   The measured "oracle" is a max over γ ∈ {0.25, 0.5, 1, 2, 4} whose maximum is the
   boundary point and is still rising. Extend the grid until it turns over. The
   *mechanism* claim — exact rank invariance under monotone distortion — is sound and
   should be kept; only the dominance claim needs to go. Appears in five places.

3. **Add a code/data availability statement and fix the falsifier framing.** The paper
   substitutes executable tests for written proofs, which only works if the tests are
   reachable; there is currently no URL anywhere. In the same pass, state F2's scope
   boundary explicitly and report that the second real-trace campaign's H2 endpoint
   failed — the paper's honesty elsewhere is its strongest asset and these two omissions
   are the only places that asset is undersold.

## Committee note

Four of the five lanes independently observed that this manuscript is more candid than
the norm in its literature — it designates the published baseline as a *killer* baseline,
reports trailing a trivial grid by 0.005–0.015, volunteers a regime where its own method
scores 0.000, and reports a prior system by the same author that failed the same
protocol. The findings above should be read against that background. They are almost all
of one kind: claims stated at a scope the evidence does not quite reach, in a paper whose
evidence is otherwise unusually well kept.
