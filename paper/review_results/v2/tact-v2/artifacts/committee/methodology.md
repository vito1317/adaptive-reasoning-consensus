## Methodology & Transparency Review

### Transparency Gaps

- **No availability statement.** "Proofs are elementary and pinned by unit tests in the released
  code (76 tests;" -- "released" or "committed" recurs in Secs. IV-B, V-C, V-F and VII, and
  Table IV is an entire table of test names standing in for proofs not given in the body. Nine
  pages contain no URL, DOI, repository name, archive, or "available upon publication" sentence.
  The paper's argument for its own correctness is the artifact it does not provide. Independently
  checked here against the actual repository: the suite collects 98 tests and runs in 49.66 s, not
  76/84 tests in 14 s.
- **No dispersion anywhere in the synthetic evidence.** `results/tact_eval.json` runs at
  `{items: 400, k: 15, k_max: 20, seed: 0}`: one seed per cell, no repetitions, no interval. The
  paper then interprets 0.035 differences and renders pre-registered falsifier verdicts on them.
- **The falsifier decision rule is undisclosed and is not a test.** `experiments/run_tact_eval.py`
  implements every verdict on a hard-coded 0.02 accuracy margin
  (`f2 = any(acc[TACT] < acc[SC] - 0.02)`), while the paper says "significantly below". F4's
  survival turns on the distortion cell's 0.035 exceeding that undisclosed 0.02, on one seed.
- **The oracle envelope's grid is never stated.** It is `SIGN_GRID = [-4, -2, -1, -0.5, 0, 0.5, 1,
  2, 4]`, nine points, and for monotone compression its argmax is $\gamma=4.0$: the boundary.
  "Beats the oracle over the entire raw-value weight family" is a continuum claim on a truncated
  grid.
- **The disclosed batch-size confound is never propagated.** "a $30$-problem-per-call probe put
  level-5 plurality accuracy at $0.40$, while the $15$-problem-per-call confirmatory run yielded
  $0.888$ on the same stratum" is exemplary disclosure, and no collection protocol is then reported
  for any window row in Table VI -- the measurements the confound most threatens.

### Circularity

The Discussion's admission is candid and its three mitigations are real, but mitigation 1 does not
hold as stated: three of the five adversarial cells are the monotone distortions, described in
Sec. IV as "rank-preserving by construction", and C1 makes rank-only dependence the source of
TACT's invariance. A rank-invariant estimator facing rank-preserving distortions is inside its own
invariance group; 1.000 there is entailed, not discovered. Only the confident echo and the i.i.d.
heterogeneity cell probe outside the working model. The comparison against the raw-value family in
those cells is still the right comparison to make -- it just cannot double as the circularity
answer.

### Fast Fixes

- Add an availability statement naming the repository and the commit that produced Table IV; quote
  the test count and runtime from that commit.
- Rerun each adversarial cell over 10--20 seeds; report mean and interval, or give the paired
  McNemar for both $+0.035$ cells.
- State the 0.02 falsifier margin in Sec. IV, or replace it with the exact McNemar the paper
  already uses elsewhere.
- State SIGN_GRID in the text and extend the oracle past $\gamma=4$, or bound the claim to the
  grid evaluated.
- Report the collection protocol (batch size) for every row of Table VI.
