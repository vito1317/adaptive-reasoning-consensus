# Abstract  (tact.tex lines 34-65, verbatim LaTeX)

\begin{abstract}
Confidence-weighted self-consistency improves on majority voting when a frozen
model's self-reported confidence is calibrated in \emph{direction}. Every
published scheme is monotone increasing in confidence, so an anti-correlated
channel poisons the vote, and binary calibration gates survive inversion only
by discarding discriminative signal. \TACT{} derives the vote exponent from the
measured, \emph{signed}, within-item discrimination of the channel: a pooled
van~Elteren Somers' $D$ with an item-clustered standard error, positive-part
James--Stein shrinkage, and a Bayes-discriminant link, which at the default
base rate $\bar p=\tfrac12$ collapses to $\gamma=z\sqrt{2+z^2}$ with $z$ the
probit of the shrunk pooled AUC. Inside the shrinkage dead zone the vote is
bit-identical to plain self-consistency. A label-free variant estimates the
sign from agreement pseudo-labels under an attenuation identity that
guarantees sign consistency while the plurality-error rate stays below one
half; past that boundary it mis-signs, which the paper measures and reports.
On a synthetic-oracle harness it recovers anti-correlated channels that pin
every published protocol to the majority floor ($1.000$ vs.\ $0.807$) and
cracks the heterogeneity floor with zero paired losses ($0.940$ vs.\ $0.808$).
Against a dev-picked \emph{signed} grid, which the sweep shows is a far
stronger baseline than the published protocols, the advantage narrows to
distortion, echo, and label-free operation. Two real-trace campaigns then
bound the setting: the channel is null on saturated benchmarks
($z=-1.24$) and positive on competition mathematics ($\Dhat=+0.250$,
$z=+2.54$), yet the stratum any such method can act on measures $3$--$7.5\%$
of items across five substrates in two domains, so abstention is the correct
default and the dead zone implements it.
\end{abstract}

\begin{IEEEkeywords}
large language models, self-consistency, confidence calibration, weighted voting, label-free estimation, rank statistics
\end{IEEEkeywords}

