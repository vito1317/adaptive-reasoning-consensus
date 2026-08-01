# Results  (tact.tex lines 248-509, verbatim LaTeX)

\section{Results}\label{sec:results}

\subsection{Signed recovery, with and without labels}
Table~\ref{tab:sweep} and Fig.~\ref{fig:sweep} give the sweep. Three observations. First, the published protocols never leave the floor on $\kappa<0$: CISC-devT's grid is positive-only and the ECE gate never opens (dev ECE ranges $0.10$--$0.80$ across the sweep while the signal's discrimination is perfect at the extremes). Second, the label-free variant matches the $200$-label variant nearly point-for-point---at $\kappa{=}{-}0.6$ the raw agreement statistic is $\Dhat_g=-0.81$ with $z=-17.6$, and the CCN identity's sign guarantee holds as predicted, yielding $1.000$ with zero labels. Third, at $\kappa=0$ the dead zone returns $\gamma=0$ exactly, so the paired accuracy difference to \SC{} is identically zero---``non-inferior'' is replaced by ``identical.''

\begin{table}[t]
\centering
\caption{Adversarial regimes (accuracy at $K{=}15$). ``Oracle'' is the test-set best over \emph{raw-value} weight policies; rank invariance beats that entire family under compression.}
\label{tab:adv}
\setlength{\tabcolsep}{3.2pt}
\begin{tabular}{l cc cc c}
\toprule
Regime & \SC & devT & SignGrid & \textbf{\TACT-dev} & \textbf{\TACT-LF}\\
\midrule
Monotone compress & .795 & .965 & .965 & \textbf{1.000} & \textbf{1.000}\\
Monotone overconf & .795 & 1.000 & 1.000 & 1.000 & 1.000\\
Monotone power & .795 & 1.000 & 1.000 & 1.000 & 1.000\\
Hetero (i.i.d.) & .810 & .810 & .810 & .810 & .810\\
Confident echo & .200 & .200 & .550 & \textbf{.585} & .200$^{\dagger}$\\
\bottomrule
\multicolumn{6}{l}{\footnotesize $^{\dagger}$alarm fires and the method refuses to leave \SC---the conditional}\\
\multicolumn{6}{l}{\footnotesize guarantee of Prop.~\ref{prop:ccn} working as stated.}
\end{tabular}
\end{table}

\subsection{Rank invariance where raw values fail}
Under monotone compression (Table~\ref{tab:adv}, Fig.~\ref{fig:adv}) all confidences huddle near $0.5$, so every $c^{\gamma}$-family weight is nearly uniform: even the \emph{oracle} over raw-value policies reaches only $0.965$. \TACT's rank scores are untouched by the distortion and both variants reach $1.000$. Under the confident echo, dev labels reveal the inversion (high confidence $\Rightarrow$ wrong) and \TACT-dev counters with $\gamma=-1.20$, the best result in the field ($0.585$; three times the \SC{} floor); label-free, the duplicate-collapse alarm fires and the method correctly refuses---by Proposition~\ref{prop:twoworld} no label-free method could do better than a coin flip on the sign here, and pretending otherwise would be the real failure.

\begin{figure}[t]
\centering
\includegraphics[width=\columnwidth]{figs/tact_adversarial.png}
\caption{Adversarial regimes. Dotted line: the oracle over raw-value weights. Left group of bars: rank invariance beats that family under compression; right: the labeled variant counters the confident echo while the label-free variant alarms and refuses.}
\label{fig:adv}
\end{figure}

\subsection{Heterogeneity}
Table~\ref{tab:group} and Fig.~\ref{fig:group} give the group study. In the covariate-structured cell, per-group \TACT{} recovers each group's signed coupling (dev $\{+4.0,0.0,-4.0\}$, label-free $\{+2.0,0.0,-2.0\}$, the $\kappa{=}0$ group correctly dead-zoned---and cracks the floor that provably binds every global policy: the label-free variant reaches $0.940$, within $0.007$ of the per-item link oracle, with \emph{zero} paired losses to \SC{} over $600$ items ($+79/-0$, $p=3.3\times10^{-24}$). In the i.i.d.\ cell every legitimate method sits at the floor with zero discordant pairs, and the naive self-referential control lands slightly below it---the empirical face of Propositions~\ref{prop:selfreinf}--\ref{prop:twoworld}. One observation is reported as-is rather than tuned for: the label-free variant outperforms the dev variant in the grouped cell ($0.940$ vs.\ $0.923$) because its lower exponent cap ($2$ vs.\ $4$) regularizes better when $|D|\approx1$; cap robustness is left as an ablation.

\begin{table}[t]
\centering
\caption{Heterogeneity study ($600$ paired items; $K{=}15$).}
\label{tab:group}
\setlength{\tabcolsep}{4.5pt}
\begin{tabular}{l cc}
\toprule
Method & Grouped & i.i.d.\\
\midrule
\SC{} (floor) & .808 & .827\\
\TACT{} global (dev) & .808 & .827\\
\TACT-group (dev) & .923 & .827\\
\textbf{\TACT-group (label-free)} & \textbf{.940} & .827\\
Naive per-item (neg.\ control) & .803 & .820\\
Per-item link oracle (ceiling) & .947 & .983\\
\bottomrule
\end{tabular}
\end{table}

\begin{figure}[t]
\centering
\includegraphics[width=\columnwidth]{figs/group_eval.png}
\caption{Structured vs.\ i.i.d.\ heterogeneity. Left: with an observable covariate, per-group \TACT{} (label-free) approaches the per-item oracle from the $0.808$ floor with zero losses to \SC. Right: the provably closed i.i.d.\ cell---every legitimate method at the floor; the negative control slightly below it.}
\label{fig:group}
\end{figure}

\subsection{Small dev sets and falsifiers}
With dev $n{=}50$ the conclusions are unchanged ($1.000$ at $|\kappa|{=}0.6$; $0.978$ at $-0.2$): the SE-aware shrinkage degrades smoothly rather than catastrophically. All four falsifiers survived: F1 ($1.000$ vs.\ $1.000$), F2 (bit-identical at $\kappa{=}0$; never significantly below \SC{} elsewhere), F3 (sweep means $0.954$ vs.\ $0.811$), and F4 (the distortion and echo cells are unreachable by either grid baseline). Against SignGrid-dev the honest margin is narrow on the homogeneous sweep---\TACT{} even trails by $0.005$--$0.015$ in the mid-range, the deliberate cost of shrinkage---and the net advantage concentrates exactly where pre-registered: distortion ($+0.035$), echo ($+0.035$), and label-free operation, which no grid can perform.

\subsection{Verification of the implementation}\label{sec:tests}
Because every claim in Sections~\ref{sec:method}--\ref{sec:hetero} is a
mathematical property rather than an empirical trend, the released code pins
each one with an executable test; the suite is 76 tests for \TACT{} (84
including the follow-on work) and runs in 14 seconds. Table~\ref{tab:tests}
maps propositions to the tests that would fail if they stopped holding.

\begin{table}[t]
\centering
\caption{What the test suite verifies. Every proposition in the paper has an
executable counterpart; the counter-tests fail deliberately on rejected
alternatives so a regression cannot silently reinstate them.}
\label{tab:tests}
\setlength{\tabcolsep}{3.4pt}
\begin{tabular}{p{2.55cm} p{3.05cm} p{2.35cm}}
\toprule
Claim & Test & Evidence \\
\midrule
Prop.~\ref{prop:sc} (exact \SC) & \texttt{gamma\_zero\_is\_} \texttt{bitwise\_sc} & 200 random pools, identical incl.\ ties \\
Dead-zone rate & \texttt{dead\_zone\_} \texttt{probability} & $>$70\% under $D{=}0$, 300 trials \\
Prop.~\ref{prop:cisc} (exact CISC) & \texttt{logval\_phi\_} \texttt{reproduces\_cisc} & identical vote shares, 100 pools \\
Rank invariance & \texttt{monotone\_} \texttt{invariance} & 3 distortions $\times$ 100 pools \\
Null variance & \texttt{null\_variance\_} \texttt{matches\_permutation} & 3{,}000-draw permutation, 10\% tol.\ \\
JS--EB identity & \texttt{js\_eb\_identity} & exact to $10^{-12}$ \\
Link \eqref{eq:link} & \texttt{link\_values\_and\_} \texttt{mixture\_correction} & closed form, rel.\ $10^{-9}$ \\
Prop.~\ref{prop:ccn} (attenuation) & \texttt{poisoning\_} \texttt{attenuation\_linear} & $\rho\in\{.1,.25,.4\}$, abs.\ $.06$ \\
Props.~\ref{prop:selfreinf}--\ref{prop:twoworld} & \texttt{test\_tact\_group.py} & 97.5\% \SC{} agreement; 4\% sign match \\
Estimator permutation-invariance & \texttt{estimator\_is\_} \texttt{permutation\_invariant} & bypasses the memo (regression test) \\
Rejected: Kish ESS & \texttt{kish\_fails\_T2\_T3} & asserts the failure \\
Rejected: SAFE guarantee under VoI & \texttt{frozen\_default\_} \texttt{breaks\_guarantee} & asserts the violation \\
\bottomrule
\end{tabular}
\end{table}

Two entries deserve comment. The permutation-invariance test was added after a
defect in which the memoisation key made the \emph{test} pass while the
estimator itself was order-dependent by up to $0.10$; it now calls the internal
routine directly. And the last two rows are counter-tests that assert
\emph{failure} of rejected alternatives --- the Kish effective-sample-size
formulation and the claim that the shipped default honours the SAFE stopping
guarantee --- so that neither can be silently reinstated by a later change.

\subsection{Real-trace validation}\label{sec:real}
Validation on real traces used Claude Haiku 4.5 as the frozen model: 100 items
(50 GSM8K \cite{gsm8k2021}, 50 CommonsenseQA), \emph{12} independent
chain-of-thought traces per item with verbalized confidence (1{,}200 traces
total), evaluated at $K{=}12$ with a 40/60 dev/test split. Four findings.

\emph{(a) The calibration--discrimination distinction reverses on real data,
and \TACT{} reads it correctly.} The channel is \emph{extremely well calibrated}
in the usual sense: $\mathrm{ECE}=0.016$, far inside the $0.10$ gate, so a
binary ECE gate \emph{opens} and hands the channel to CISC. Yet the measured
within-item discrimination is $\Dhat=-0.219$ with $\mathrm{SE}=0.176$
($z=-1.24$): no usable signal, and what little there is points the
\emph{wrong way} (math $-0.515$, commonsense $-0.173$; both groups negative).
This is the exact mirror image of the synthetic case in which ECE wrongly
\emph{closed} the gate on a discriminative channel (Section~\ref{sec:setup}):
on real traces ECE wrongly \emph{opens} it on a non-discriminative one.
Calibration is uninformative about voting utility in both directions, and a
signed discrimination statistic is what distinguishes them.

\emph{(b) The dead zone fires, and costs exactly nothing.} With $|z|<\nu$,
\TACT-dev, \TACT-LF and \TACT-group all return $\gamma=0$ and are bit-identical
to \SC{} on every test item ($+0/-0$ discordant pairs, $p=1$). All methods score
$0.917$. This is the pre-registered null-direction prediction of
Section~\ref{sec:limits} confirmed on real data: where the channel carries no
signal, the method is free.

\emph{(c) Saturation is the binding constraint, not the estimator.} Trace-level
accuracy is $0.958$ on GSM8K and $0.847$ on CommonsenseQA, so only $12$ of $100$
items contain both a correct and an incorrect trace, the only items a
within-item rank statistic can use. The estimator is not underpowered by
design; the benchmark simply does not present the model with enough genuine
uncertainty. Exposing non-null coupling on a strong model requires harder item
pools, not more traces per item.

\emph{(d) Verbalized confidence is tie-heavy.} Two values ($0.99$, $0.95$)
account for $49\%$ of all reports, activating the tie-safe degeneration path of
\eqref{eq:vdw} on many items.

Scope of this first campaign: one model, two benchmarks, $K{=}12$. It confirms
the null-direction prediction and the calibration--discrimination argument, and
it is not evidence that \TACT{} improves accuracy, since the channel carried no
signal to exploit. Finding (c) predicts what to do about that, and
Section~\ref{sec:hard} does it.

\subsection{Confirmatory campaign on harder items}\label{sec:hard}
Finding (c) predicts that a channel measured as null on saturated benchmarks
should become measurable on items the model finds genuinely uncertain. A
pre-registered follow-up tests that prediction: $119$ MATH level-5 problems
\cite{math500,lightman2024verify}, $16$ traces each from the same frozen
model, a $30$-item sign set and an $89$-item evaluation set drawn from the
registered list before any trace was collected, and five hypotheses (H1--H5)
fixed in advance.

\emph{The channel is real.} On the evaluation set the pooled statistic is
$\Dhat=+0.250$ with $\mathrm{SE}=0.098$, so $z=+2.54$ and H1 passes. This is
the first real-trace evidence that verbalized confidence carries positive
within-item discrimination; the same measurement on GSM8K/CommonsenseQA gave
$-0.219$ ($z=-1.24$).

\emph{The endpoint was unpassable for any method.} The realized substrate
saturated again: per-trace accuracy $0.819$, \SC{} $0.888$, a decisive
stratum of $10$ of $89$ items, and the correct answer present in the pool on
only $4$ of those. The in-pool \emph{oracle} therefore tops out at $+4/-0$,
exact one-sided $p=0.0625$. H2 fails, but it fails for every conceivable
aggregation method including a perfect one, so the failure is a property of
the substrate rather than of the estimator.

\emph{Abstention behaved as designed.} \TACT{} returned $\gamma=0$, with
alarms E4 and E2 firing on the label-free path and the sign set holding too
few informative items to supply a semi-label-free sign. The vote is therefore
bit-identical to \SC{} at $0.888$ (H3, H4 pass). The cost of acting anyway is
visible in the same table: best-single-confidence, the trivial baseline that
always trusts the channel, loses $4.5$ points at $0.843$.

\begin{table}[t]
\caption{Confirmatory campaign, MATH level-5 evaluation set ($89$ items,
$K{=}16$). Every method replays the same cached pools. The duplication
channel is inert because no reasoning text was collected, so dedup-\SC{}
coincides with \SC{} by construction.}
\label{tab:hard}
\centering\footnotesize
\setlength{\tabcolsep}{4pt}
\begin{tabular}{l c c}
\toprule
Method & Accuracy & net vs.\ \SC \\
\midrule
\SC{} / dedup-\SC{} / CISC-linear & $0.888$ & --- \\
\TACT-LF & $0.888$ & $+0/-0$ \\
\TACT-semi-LF & $0.888$ & $+0/-0$ \\
best-single-confidence & $0.843$ & $+1/-5$ \\
\midrule
in-pool oracle (ceiling) & $0.933$ & $+4/-0$ \\
\bottomrule
\end{tabular}
\end{table}

One caveat from this campaign transfers beyond \TACT. Measured difficulty
depended on the collection protocol: a $30$-problem-per-call probe put
level-5 plurality accuracy at $0.40$, while the $15$-problem-per-call
confirmatory run yielded $0.888$ on the same stratum. Batch size belongs in
the experimental record whenever traces are collected in batches.

\subsection{How wide is the addressable stratum?}\label{sec:window}
Both campaigns failed their endpoint for the same reason, which suggests
measuring that reason directly. Define the \emph{window} as the fraction of
items where the plurality is wrong \emph{and} the correct answer is present
in the pool: the ceiling for any label-free aggregation method, since nothing
outside it can be changed.

The window was measured on five substrates spanning two domains
(Table~\ref{tab:window}). For code generation, where an executable test suite
supplies per-sample ground truth and the window might reasonably be expected
to widen, $40$ LeetCode Medium/Hard problems \cite{leetcodedataset} were
solved $8$ times each and graded against the benchmark's hidden suites, with
the baseline taken as the largest behavioural cluster over probe inputs
(never expected outputs). The window is $3/40=7.5\%$ (CI$_{95}$
$2.6$--$19.9\%$): wider than label-free QA, but the same order, and the
composition is the same shape at $75\%$ saturated, $18\%$ capability wall,
$8\%$ rescuable. Nor does budget open it. The seven capability-wall problems
produced zero correct solutions in $224$ further attempts (per-problem $95\%$
upper bound on the pass rate $0.088$), and extrapolating oracle@$N$ shows the
window saturating by $N{=}32$.

\begin{table}[t]
\caption{The addressable stratum across substrates. Rows marked $\dagger$ are
measured here; HumanEval+/MBPP+ is recomputed from published oracle-minus-
selector tables. As items harden they pass from saturated to
capability-limited without the window widening.}
\label{tab:window}
\centering\footnotesize
\setlength{\tabcolsep}{4pt}
\begin{tabular}{l l c}
\toprule
Domain & Substrate & Window \\
\midrule
QA, label-free & GSM8K / CommonsenseQA$^\dagger$ & $12\%$ informative, $9\%$ decisive \\
QA, label-free & MATH level-5$^\dagger$ & $11\%$ decisive, $4\%$ rescuable \\
QA, label-free & AIME / AMC$^\dagger$ & $23\%$ decisive, $3\%$ rescuable \\
Code, executable & HumanEval+ / MBPP+ & $3.56\%$ \\
Code, executable & LeetCode Med/Hard$^\dagger$ & $7.5\%$ \\
\bottomrule
\end{tabular}
\end{table}

One precaution belongs with these numbers, because omitting it would have
inverted them. The grading harness was validated against the benchmark's own
reference solutions before any candidate was scored: $178$ of $180$ pass
under the sandbox's resource limits. An earlier version of the same harness
failed $100\%$ of executions because the host rejects one of the requested
limits outright, and that condition presents as a candidate failure rather
than as an error. Studies that grade by execution should report their
reference-solution pass rate for the same reason a calibration curve is
reported: without it, a broken harness and a capability wall look identical.
