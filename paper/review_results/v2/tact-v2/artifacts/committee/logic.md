## Logic Chain Review

### Broken Links (claim -> evidence)

1. **The paper bounds its own motivation and never closes the loop.** Sec. V-I measures the
   addressable stratum at "$2$--$7.5\%$ of items on every substrate" with "no widening as items
   harden". That result bounds the entire method family, TACT included, and the two real-trace
   campaigns duly returned $\gamma=0$ with votes bit-identical to \SC. Every step is stated
   honestly; none is joined to the next. The manuscript never says why a method whose addressable
   stratum it has just measured at a few per cent is worth adopting, nor reframes itself as the
   measurement plus a method that abstains correctly inside it. A reader who follows the argument
   to its end reaches a conclusion the paper never states.

2. **Sec. VII contradicts Secs. V-G and V-H.** "Validation on real LLM traces is the remaining
   step" and "All quantitative claims are on a synthetic oracle" sit in the same section as
   "the measured cost of acting anyway was negative on both real substrates". The limitations
   section was not re-derived after the evidence base changed.

3. **A universal default from five small samples.** "Abstention is therefore the correct default
   rather than a conservative one" rests on window measurements over 100, 89, 30, 40 items and one
   recomputed published table. The paper reports the CI on one of them (2.6--19.9% on 3/40) and
   then states the recommendation without qualification in the abstract.

### Causal Inversions

None found. The chain from Sec. V-G finding (c) ("Saturation is the binding constraint, not the
estimator") to the Sec. V-H confirmatory campaign and then to the Sec. V-I window measurement is
correctly ordered, and the reasoning that H2's failure is a property of the substrate rather than
the estimator is sound: the in-pool oracle tops out at $+4/-0$, so the endpoint was unpassable for
any method.

### Fast Fixes

- Add one paragraph joining Sec. V-I to the contribution claim: state the ceiling, then state what
  TACT is for given that ceiling. Leading with the boundary is a reframing, not new experiments.
- Delete the two stale sentences in Sec. VII para 1.
- Scope "the correct default" to the substrates measured, or attach the interval.
