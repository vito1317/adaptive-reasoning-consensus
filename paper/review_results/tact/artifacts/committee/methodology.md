# Committee — Reviewer 2 (methodology transparency)

**Score: 5.5 / 10**

I was able to do something unusual for a review: the author's result files were
available alongside the manuscript, so most of my findings are checks against artifacts
rather than impressions. Where the paper matches its artifacts I say so; the deductions
below are all cases where it does not, or where the artifact reveals something the
manuscript does not report.

## MUST-FIX (submission blockers)

### 1. The clip, not the derived formula, sets γ in every headline cell

This is my principal concern and it goes to the paper's central novelty claim.
Sec. III-D: "no tuned constant anywhere: ν is a significance level and γ_max a clip, and
both are fixed before any data is seen." Contribution C1: γ "is *derived*, not
grid-searched."

From `results/tact_eval.json`:

| cell | γ (TACT-dev) | γ_max dev | γ (TACT-LF) | γ_max LF |
|---|---|---|---|---|
| κ = −0.6 | **−4.00** | 4 | **−2.00** | 2 |
| κ = −0.4 | **−4.00** | 4 | **−2.00** | 2 |
| κ = −0.2 | −2.78 | 4 | **−2.00** | 2 |
| κ = +0.2 | 2.80 | 4 | **+2.00** | 2 |
| κ = +0.4 | **+4.00** | 4 | **+2.00** | 2 |
| κ = +0.6 | **+4.00** | 4 | **+2.00** | 2 |
| monotone compress | **+4.00** | 4 | **+2.00** | 2 |
| monotone overconf | **+4.00** | 4 | **+2.00** | 2 |

and from `results/group_eval.json`, the grouped cell:
`gammas_dev_by_group = {0: 4.0, 1: 0.0135, 2: −4.0}`,
`gammas_lf_by_group = {0: 2.0, 1: 0.0, 2: −2.0}`.

Every cell in which the paper reports 1.000, and both non-null groups in the headline
0.940 result, have γ pinned exactly at the clip. In those cells γ = z√(2 + z²) is
inactive; the number that determines the vote is a hand-chosen constant that differs
between variants (4 vs 2) with no stated derivation for either value.

The paper supplies the mechanism itself, in Sec. VII-C: the LF variant beats the dev
variant "because its lower exponent cap (2 vs. 4) regularizes better when |D| ≈ 1; cap
robustness is left as an ablation." So the best number in the paper is explicitly
attributed to a constant, and the ablation for that constant is deferred.

**Required:** a γ_max ablation (2 / 4 / 8 / ∞) across the sweep, the distortion cells and
the grouped cell; and per-cell reporting of whether the clip binds. If accuracy is
insensitive to γ_max, say so and the concern evaporates. If it is not, the "no tuned
constant" claim has to go.

### 2. The "oracle over the entire raw-value weight family" is the top of a truncated grid

`results/tact_eval.json`, `adversarial.monotone_compress.acc`:

```
CISC(γ=0.25) 0.795   CISC(γ=0.5) 0.795   CISC(γ=1.0) 0.815
CISC(γ=2.0)  0.8825  CISC(γ=4.0) 0.965
oracle = {acc: 0.965, gamma: 4.0}
```

The maximum is the largest grid point, and accuracy is still strictly increasing at that
point. A monotone compression toward 0.5 is by construction undone by a large enough
exponent, so the family supremum is very plausibly at or near 1.000 for γ = 8 or 16 —
i.e. equal to what TACT achieves. The claim "beats the oracle over the *entire*
raw-value weight family" appears five times (abstract, C1, Table II caption, Sec. VII-B,
Fig. 4 caption) and none of them is supported by a max over five points that has not
turned over.

The *mechanism* claim is fine and should be kept — rank scores are exactly invariant
under monotone distortion, c^γ weights are not, and that is a real structural advantage.
It is the quantitative dominance claim that fails.

**Required:** extend the grid until it turns over, then restate.

### 3. No code or data availability statement

Sec. III-F, Sec. VII-E and all twelve rows of Table VI rest on "the released code". There
is no repository URL, DOI, or availability statement anywhere in the manuscript. For a
paper that explicitly substitutes executable tests for written proofs, the substitution
only functions if the tests are reachable. The frozen model is also named without a
version pin, access date, or decoding configuration ("Claude Haiku 4.5").

## SHOULD-FIX

### 4. Reported suite size and runtime do not match the released suite

Sec. VII-E: "the suite is 76 tests for TACT (84 including the follow-on work) and runs in
14 seconds." Running it: **98 passed in 54.69s**. Per-file collection is
components 20, formula 12, isc 10, properties 17, tact 18, tact_group 7, units 14 — no
subset gives 76 or 84 (non-ISC total 88, full total 98). Runtime is machine-dependent and
I would not press it, but the counts are directly checkable and a reviewer who runs
`pytest` will see the mismatch.

I did check Table VI's test names against the suite. They are abbreviated but they all
resolve to real functions (`poisoning_attenuation_linear` →
`test_poisoning_attenuation_is_linear_in_flip_rate`, `frozen_default_breaks_guarantee` →
`test_frozen_default_breaks_the_safe_guarantee`). The table is sound; only the counts are
stale.

### 5. Falsifiers evaluated at ceiling are reported as survived

F1 asks whether TACT-dev is significantly below the best fixed-γ CISC at κ = +0.6. In
that cell CISC-devT, SignGrid-dev, TACT-dev, TACT-LF and the oracle are all exactly
1.000. The falsifier could not have fired. Sec. VII-D reports it as a survival:
"F1 (1.000 vs. 1.000)". The `monotone_overconf` cell has the same shape — every method
reaches 1.000 while the oracle picks γ = 1.0 and TACT picks γ = 4.0, materially different
policies the metric cannot separate. Report these as inconclusive, not passed.

### 6. Between-cell sampling noise is undisclosed

SC ignores confidence, so its accuracy cannot depend on κ. Table I's SC row nonetheless
runs .807 .797 .835 .762 .835 .795 .845 .838 .782 — an 8.3-point spread, i.e. pure
between-cell variation from independently drawn 400-item pools (SE ≈ 0.02). The within-cell
comparisons are properly paired and I have no objection to them, but the reader cannot
tell from the table which comparisons are paired and which are not, and the unexplained
SC row invites the wrong reading of the 0.005–0.015 margins discussed in Sec. VII-D.
Add per-cell CIs or state that cells are independent draws and only within-column
comparisons are paired.

### 7. The batch-size confound is reported but not propagated

Sec. VII-F(e) reports that a 30-problem-per-call probe measured level-5 plurality
accuracy at 0.40 while the 15-problem-per-call run gave 0.888 on the same stratum, and
correctly concludes batch size must be reported as an experimental parameter. That is a
2.2× swing in measured accuracy from a collection knob — far larger than the 2–7.5%
window the paper's second headline contribution claims to bound. The window measurements
were themselves batch-collected and their batch sizes are never stated. Either report
them and argue the effect is absorbed, or widen the stated uncertainty on the window.

## What is done well and should be preserved

- Paired comparisons with exact McNemar throughout, and the p-values are right: +79/−0
  gives 2⁻⁷⁸ = 3.3 × 10⁻²⁴; +4/−0 gives 0.0625. I recomputed both.
- The pre-measurement of the baseline landscape (Fig. 1) *before* the method existed, and
  restricting the win claims to the cells that pre-measurement identified, is exactly the
  right discipline and is rare.
- Sec. VIII's circularity paragraph is the most honest limitations statement I have read
  in this literature. The three named mitigations are real mitigations.
- The reference-solution pass rate precaution (178 of 180) generalizes beyond this paper
  and deserves the prominence it is given.
