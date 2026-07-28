# Contributions

> Paper-ready contribution section for the TACT work. Figures live in
> `results/figures/`; every number is traceable to a JSON artifact in
> `results/` and re-derivable from the committed experiment scripts.

## Problem

Confidence-weighted self-consistency (CISC and its successors) extracts large
gains from a frozen LLM's self-reported confidence — until the confidence
channel is miscalibrated in *direction*, at which point every published
weighting scheme fails catastrophically: their vote weights are structurally
monotone **increasing** in confidence, so an anti-correlated channel poisons
the vote rather than informing it. Binary dev-set gates (e.g. on ECE) survive
by discarding the channel entirely, wasting genuinely discriminative signal.
No published method can *estimate the sign* of the confidence–correctness
association, and none can do so without labels.

## Contributions

**C1 — Signed, analytically-tempered confidence weighting (TACT).**
We replace CISC's fixed exponent with a derived one:
`γ = clip(L(shrink(D̂, SE)))`, where `D̂` is the pooled van Elteren Somers'
`D = 2·WQD − 1` of the confidence channel (a pure within-item rank statistic,
invariant to every strictly monotone distortion of the confidence scale),
`shrink` is positive-part James–Stein with a significance floor, and `L` is the
Bayes-discriminant link with a mixture-variance correction. The map carries
exact anchors: inside the shrinkage dead zone the vote is **bit-identical to
plain self-consistency** (a shared code path, so `P(TACT = SC | D = 0) → 98%`
label-free and no paired test can distinguish them), and with the log-value
feature map the family reproduces CISC-power exactly. Voting with
`w_i = exp(γ·φ_i)`, where `φ_i` is the standardized van der Waerden score of
the trace's within-item confidence midrank, makes the entire method
rank-invariant — under monotone compression of the confidence scale it beats
the *oracle over the whole raw-value weight family* (1.000 vs 0.965; Fig. 2).

**C2 — Label-free estimation of the signed channel reliability.**
The crowdsourcing lineage (Dawid–Skene; spectral meta-learners) estimates
annotator reliability from cross-annotator covariance; a single exchangeable
confidence channel from one model offers no such structure. We estimate the
signed discrimination from *agreement pseudo-labels* (dedup-weighted plurality
per item), and prove a class-conditional-noise attenuation identity
`E[D̂_g] = (1 − 2ρ̄)·D_true`: the estimate can only *under*-trust, never
mis-sign, whenever the pair-weighted plurality-error rate satisfies
`ρ̄ < 1/2`. A split-half agreement inversion de-attenuates conservatively
(dividing by an upper confidence bound), and sign-aware alarms return the
method to plain SC when the identifiability condition is threatened. On the
coupling sweep the label-free variant matches the 200-label variant nearly
point-for-point, including full recovery of *negative* channels
(κ = −0.6: **1.000 label-free** vs the 0.807 floor of every published
protocol; Fig. 1) — and we state the honest boundary: under a confident
verbatim echo the sign is information-theoretically ambiguous
(a Parisi/Hui–Walter two-root situation), the alarms detect the verbatim case
and refuse, and ~50 labels (sign only) restore full operation.

**C3 — An impossibility result for per-item label-free adaptation, and the
covariate-structured escape (TACT-group).**
When the per-item coupling `κ_q` is i.i.d. with no observable covariate, we
show per-item label-free adaptation is closed: (i) *self-reinforcement
identity* — any monotone map from an item's own agreement statistic to an
exponent reweights toward the plurality on both branches, collapsing to
self-consistency (97.5% agreement; residual flips net-harmful); (ii)
*winner's curse* — on exactly the plurality-wrong items where a flip could
win, the observable sign opposes the true sign 96% of the time; (iii)
*two-world unidentifiability* — `{κ>0, minority correct}` and
`{κ<0, plurality correct}` induce identical observable laws. Consequently the
per-item oracle (0.983) is unreachable, and TACT's dead zone makes it degrade
to *exactly* SC there (zero discordant pairs; Fig. 3 right). When
heterogeneity is instead indexed by an observable covariate — the realistic
case of domain-dependent calibration — running the same estimator per group
recovers each group's signed coupling (label-free: {+2.0, 0.0, −2.0}) and
cracks the floor that provably binds every global policy: **0.940 label-free
vs the 0.808 floor, within 0.007 of the per-item oracle, with zero losses to
SC across 600 paired items** (+79/−0, p = 3.3e-24; Fig. 3 left).

**C4 — A pre-registered falsification protocol, with the strongest baselines
included.**
Four falsifiers were fixed before implementation, including the two designed
to kill the method: the *published* dev-calibrated protocol (CISC-devT — whose
tuned temperature already interpolates SC↔CISC) and a trivial dev-picked
signed exponent grid. All four survived (Fig. 1–2), and we report the honest
margins: against the signed grid the net advantage concentrates in exactly
three cells — monotone distortion (+0.035), confident echo (+0.035), and
label-free operation, which no grid can perform. As a matched pair of honest
outcomes, the same protocol applied to our preceding system (RLEV-VoI,
redundancy-discounted voting) *fired* four of five falsifiers, and we report
that system as a negative result whose post-mortem motivated this work.

## Figures

| | |
|---|---|
| **Fig. 1** `tact_sweep.png` | The confidence-usage frontier. Published protocols (CISC-devT, ECE gate) sit at the SC floor on the entire negative half-axis; TACT-dev and the label-free TACT-LF track the oracle across the sweep. |
| **Fig. 2** `tact_adversarial.png` | Adversarial regimes. Rank invariance beats the oracle of the raw-value family under monotone compression; the confident-echo cell shows the labeled variant countering (γ = −1.20) while the label-free variant alarms and refuses. |
| **Fig. 3** `group_eval.png` | Structured vs i.i.d. heterogeneity. Left: per-group TACT (label-free 0.940) approaches the per-item oracle (0.947) from an 0.808 floor. Right: the provably-closed i.i.d. cell — every legitimate method at the floor, the negative control slightly below it. |
| **Fig. 4** `kappa_sweep.png` | The pre-measured problem statement: baseline headroom before TACT existed, isolating where a new method could and could not win. |

## Scope and evidence status

All quantitative claims above are on a synthetic-oracle harness (paired trace
pools, McNemar tests, 400–600 items per cell) whose adversarial regimes
(monotone distortions, heterogeneity, confident echo) lie *outside* the
estimator's working model; mechanism-recovery and accuracy claims are reported
separately to limit circularity. Validation on real LLM traces is the
remaining step; the harness replays cached traces and the runner is committed
(`experiments/run_real_api.py`).
