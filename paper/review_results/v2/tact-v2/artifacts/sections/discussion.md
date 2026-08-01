# Discussion and Limitations  (tact.tex lines 530-570, verbatim LaTeX)

\section{Discussion and Limitations}\label{sec:limits}

\textbf{What the evidence does and does not show.} The \emph{accuracy} claims are all on a synthetic oracle whose confidence model \eqref{eq:confmodel} is, at the homogeneous cells, the very coupling the estimator measures. Three design choices limit the circularity: the adversarial regimes (distortions, heterogeneity, echo) lie outside the estimator's working model; mechanism-recovery claims (does $\Dhat$ track $\kappa$?) are reported separately from accuracy claims; and the pre-measured baseline landscape (Fig.~\ref{fig:baselines}) fixed the winnable cells before the method existed. The real-trace campaigns of Sections~\ref{sec:real} and~\ref{sec:hard} test the \emph{premise} and the \emph{abstention behaviour}, and both predictions held: the channel is null on saturated benchmarks and positive on competition mathematics, and the dead zone kept the vote bit-identical to \SC{} in each case. They do not test the accuracy claim, because on neither substrate was the addressable stratum large enough for any method to demonstrate a gain (Section~\ref{sec:window}).

\textbf{Narrow margins where labels abound.} When labels are plentiful and the confidence scale is trusted, a dev-picked signed grid captures most of the value; \TACT's case rests on the label-free setting, distorted scales, small dev sets, and the exactness of its anchors.

\textbf{Conditional label-free guarantee, and what happens past the boundary.}
Proposition~\ref{prop:ccn} requires $\bar\rho<1/2$ after deduplication, and the
confident-echo ambiguity is fundamental (Proposition~\ref{prop:twoworld}).
Follow-on work measured the consequence of crossing that boundary, and it is
worse than under-trust. In a \emph{paraphrased} wrong-majority cell (a dominant
wrong cluster that is semantically tight but carries no verbatim signature, so
deduplication has nothing to collapse) the plurality is wrong on most items,
$\bar\rho>1/2$, and \TACT-LF does not merely shrink toward \SC: it
\emph{mis-signs}, saturates at $\gamma=-2.0$, and scores $0.000$ against an
\SC{} floor of $0.340$. None of the four alarms fires, because E1 keys on
verbatim duplication which is absent by construction. This is the method's
sharpest unguarded failure mode: the guarantee is conditional, the condition is
not observable label-free, and the existing diagnostics do not detect its
violation. Where a systematically wrong majority is plausible, the
semi-label-free mode (sign from ${\sim}50$ labels) should be the default rather
than an optional refinement.

\textbf{Global exponent per group.} Within a group, \TACT{} ships one exponent; per-item variation inside a group is unexploitable by Propositions~\ref{prop:selfreinf}--\ref{prop:twoworld} unless further covariates exist.

\textbf{The thin window.} Section~\ref{sec:window} measures the stratum this
whole family of methods can act on at $3$--$7.5\%$ of items on every substrate
tried, in two domains, with no widening as items harden: they pass from
saturated straight to capability-limited. Two consequences follow for the
method proposed here. First, abstention is not a conservative compromise but
the only correct default, and the measured cost of acting anyway was negative
on both real substrates (best-single-confidence loses $4.5$ points in
Table~\ref{tab:hard} where the dead zone holds \TACT{} at the \SC{} floor).
Second, an aggregation gain of the size reported on the synthetic harness is
not measurable on a benchmark of a few hundred items at these window widths,
which is why the real-trace claim in this paper is confined to the premise
(the channel exists and is signed) and to the abstention behaviour, and does
not extend to accuracy. Demonstrating the gain needs a (model, benchmark)
pair whose plurality is wrong on $30$--$60\%$ of items with the correct answer
still reachable, and no pair tried here satisfies both.

