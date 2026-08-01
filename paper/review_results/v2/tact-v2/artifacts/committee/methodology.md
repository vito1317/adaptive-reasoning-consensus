## Methodology Transparency Review (SRQR-aware)

### MUST-FIX (submission blockers)
- No methodology blocker was surfaced by the fallback pass.

### SHOULD-FIX (quality improvements)
- (experiment) "Baselines." — Comparative evaluation language was detected. Deep review should verify that baseline tuning, data splits, and reporting conventions are described symmetrically.
- (experiment) "Baselines." — The results section reports comparative performance. Confirm whether the paper states the evaluation scope, variance, and fairness conditions tightly enough for a reviewer.
- (introduction) "On the coupling sweep the label-free variant matches the 200-label variant nearly point-for-point, including full recovery of negative channels (Section~sec:results)." — Multiple sections contain numeric claims. Confirm that the same quantities reconcile across main text, tables, and appendix material.

### SRQR Checklist Deltas
- Sampling rationale: clarify how the evidence base supports the paper's strongest claims.
- Data collection details (time/place/duration): add context when results depend on specific settings.
- Coding process (stages, coders, disagreement resolution): specify if qualitative or hybrid analysis is used.
- Saturation: state whether the evidence scope is exhaustive or bounded.
- Triangulation: explain whether multiple evidence sources were reconciled.
- Reflexivity: acknowledge researcher choices that shape interpretation.
