## Theory Contribution Review

### 3 Fatal Theory Holes

1. (Sec. IV-C, Eq. 11) "Model $\varphi\,|\,y\sim\mathcal{N}(\mu_y,s^2)$ within item with the
   \emph{mixture} standardized to unit variance" -- the analytic link that C1 offers *in place of*
   a grid search is derived from a Gaussian model for a statistic that is discrete and bounded by
   construction. At $m_q{=}4$, $\varphi$ takes four values. The paper handles the scale
   consequence (realized $\sigma_q$) and never the distributional one, in exactly the small-budget
   regime it advertises as transferable ("an exponent estimated at $m{=}40$ transfers to deployment
   at $m{=}8$"). And the artifacts show the point is not academic: `results/tact_eval.json` has
   $\gamma$ pinned at $\gamma_{\max}$ in every cell the paper reports as a win, so the derived
   magnitude is never actually the operative one there.

2. (Sec. V-F, Sec. VI) "Proofs are elementary and pinned by unit tests in the released code
   (76 tests;" -- two of the seven propositions carry their content as frequencies measured on one
   400-item synthetic harness at one seed (97.5% SC agreement; a 4% sign match). A proposition
   environment plus a blanket proof sentence grants those measurements the standing of the theorems
   around them. Proposition 7's justification is also weaker than its statement: it establishes
   $D^{w_1}=-D^{w_2}$, a sign flip in one functional, and claims identical observable laws.

3. (Sec. II) "The claim is the assembly and its anchors, not the parts." -- the most honest
   sentence in the paper, and it locates the increment in the wrong place. What survives if TACT is
   superseded is the impossibility triple of Sec. VI and the attenuation identity
   $\mathbb{E}[\Dhat_g]=(1-2\bar\rho)D$: boundary results about what *any* label-free method can
   do. Title, abstract and C1 spend themselves on the tempering map instead.

### What The Paper Is Actually Contributing (1 sentence, no marketing)

A signed, label-free estimate of within-item confidence discrimination, plus the boundary results
showing that per-item label-free adaptation is closed and that the stratum any such method can act
on is a few per cent of items -- with the tempering map itself a competent but grid-equivalent
wrapper whose magnitude is set by a hand-fixed clip wherever it wins.

### How To Fix (2-4 concrete moves)

- State the $m$ at which the Gaussian link is adequate, or add a discreteness correction; report a
  small-$m$ sensitivity run alongside the existing $m{=}40 \to m{=}8$ transfer claim.
- Disclose that $\gamma$ saturates at $\gamma_{\max}$ in the winning cells, and add the
  cap-sensitivity ablation the paper currently defers ("cap robustness is left as an ablation").
- Demote Propositions 5 and 6 to remarks with sample sizes and intervals, and give Proposition 7
  either a real proof of law equality or a weaker statement matched to the sign-flip argument.
- Re-center the theory claim on the impossibility results and the attenuation identity.
