# SPEC — Next campaign: a decisive G1 and a capability ladder

Written before collection, as the other SPECs were. Two campaigns, one shared
reason: every real-trace result so far was decided by the substrate rather than
by the method, and both designs below fix that at the design stage instead of
discovering it afterwards.

Run `experiments/run_substrate_health.py` on any candidate pair before spending
budget. It reports `decisive_n`, the window, `n_gated` against the label-free
floor, and the sign-set `z` against the semi-label-free gate. Three of the four
already say "untestable" on the substrates used so far.

---

## Campaign A — G1 at N≈120 by two-stage sampling

### Why the present result is not decisive

The window is measured as a binomial proportion, so its interval depends on the
item count and not at all on how many candidates each item gets. At the
measured `3/40 = 7.5%` the exact 95% interval is `(0.016, 0.204)`. The KAPPA-P
gate was 15%. The upper bound sits above the gate, so "did not pass" is
currently indistinguishable from "not measured precisely enough".

| N | window | 95% CI (Clopper–Pearson) | vs the 15% gate |
|---:|---:|---|---|
| 40 | 3/40 | (0.016, 0.204) | upper bound above the gate |
| 80 | 6/80 | (0.028, 0.156) | still above |
| **120** | **9/120** | **(0.035, 0.138)** | **below — decisive** |
| 160 | 12/160 | (0.039, 0.127) | below |

N≈120 is where the conclusion becomes a conclusion. That is the target.

### The design

Deepening every item to 32 candidates costs 32 samples per item. But the window
is defined only over items whose baseline is *wrong*, and the baseline needs far
fewer samples to establish than the window does to resolve.

```
stage 1   k1 = 4 candidates, score the baseline (largest behavioural cluster
          over probe inputs, never expected outputs)
stage 2   only for items whose stage-1 baseline is wrong (~25% historically),
          deepen to 32
```

Cost per item becomes `4 + 0.25 × 28 = 11` against 32, so the same budget buys
**2.91× the items**: the 40-item budget reaches ~116, and N≈120 is affordable.

### The assumption, stated because it is load-bearing

Stage 1 must classify the baseline the same way a 32-candidate run would. This
is not a new assumption — the extrapolated `oracle@N` table in REPORT-G1
already relies on the baseline being stable in the number of candidates, and it
found the window saturating by N=32. It should still be checked rather than
assumed: on the existing 40 LeetCode problems the stage-1 and stage-2 baseline
verdicts can be compared directly from cached candidates, at zero new cost.
**Do that first.** If they disagree on more than a couple of items the two-stage
design is void and the honest answer is that G1 needs the full budget.

### Falsifiers, fixed here

- **A1** the two-stage baseline disagrees with the full-depth baseline on more
  than 3 of 40 cached problems → design void, do not run
- **A2** the window at N≈120 has a CI upper bound still above 15% → report the
  interval and stop claiming anything about the gate
- **A3** stage-2 deepening rate exceeds 40% → the cost model fails and the
  budget must be recomputed before continuing

---

## Campaign B — Capability ladder on one benchmark

### What it fixes, and why the existing corpora cannot

Every real-trace result so far failed for want of substrate, and the failures
were different each time:

| substrate | what blocked it |
|---|---|
| GSM8K / CSQA | SC 0.917, 12 informative items; label-free gate empty by construction |
| MATH L5 | SC 0.888, `n_gated` 13 against a floor of 50; sign set z=+0.73 against a gate of 1 |
| MATH L5, budget-capped | widest window measured (11.8%) but only 12 items past the margin gate |

TACT-group has never been tested on real traces at all: the only grouped corpus
has 3 informative items in the math group and 9 in commonsense.

Holding the benchmark fixed and sweeping **model capability** attacks all of it
at once. On one MATH-500 slice, a 3B model's plurality is wrong far more often
than a frontier model's, so:

- **SC lands in 0.4–0.7** on the weak rungs, which is where H2 can pass at all
- **disagreement is plentiful**, so `n_gated` clears its floor and the
  label-free and grouped arms actually run
- **difficulty and capability separate**: the benchmark is constant, so any
  change in the window is attributable to the model
- **model identity is the group covariate** TACT-group needs, and it is
  observable by construction rather than inferred
- **logprob confidence becomes available**. Open-weight rungs return logprobs,
  which SPEC-TACT registers as the *primary* confidence signal; the
  Anthropic-backed campaigns could only collect the verbalized number, so the
  registered primary channel has never been measured. This is the comparison
  the paper currently cannot make.

### Rungs

3B → 7B → 14B → frontier, one MATH-500 slice, same K, same prompt, same grader.
Sweep temperature at one rung to separate decoding entropy from capability.

### Infrastructure

Already in place after this commit. `OpenAIBackend` takes `base_url`, so vLLM,
OpenRouter and llama.cpp are reachable without new code, and the API-key
requirement relaxes when a base_url is given because local servers do not want
one. `OPENAI_BASE_URL` works too, so a ladder can be swept from the environment:

```bash
export OPENAI_BASE_URL=http://localhost:8000/v1
python experiments/run_real_api.py --model Qwen/Qwen2.5-3B-Instruct ...
```

### Falsifiers, fixed here

- **B1** no rung puts SC in 0.4–0.7 on this slice → the ladder does not span
  the regime and the window claim stays where it is
- **B2** `n_gated` stays below `min_gated_items` on every rung → the label-free
  arm is untestable on MATH at any capability, which is a finding about the
  pipeline's item appetite and should be reported as one
- **B3** the window does not vary across rungs → capability is not the axis
  either, and the thin-window phenomenon is stronger than currently claimed
- **B4** logprob and verbalized confidence give the same signed `D` to within
  the seed interval → the primary/secondary distinction in SPEC-TACT is
  decoration and should be dropped

### Order

B4 and the group arm are the two that reach claims the paper currently cannot
support. Run the cheapest rung first and check B1 before buying the rest: if no
rung reaches SC∈0.4–0.7, nothing downstream is worth collecting.
