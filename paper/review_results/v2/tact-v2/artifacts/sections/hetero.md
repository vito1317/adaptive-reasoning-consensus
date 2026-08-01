# Heterogeneity  (tact.tex lines 233-254, verbatim LaTeX)

\section{Heterogeneity: Impossibility and Escape}\label{sec:hetero}

\subsection{Per-item adaptation is closed under i.i.d.\ coupling}
Suppose $\kappa_q\stackrel{\text{iid}}{\sim}\mathcal{N}(0,0.6^2)$ with no observable covariate.

\begin{proposition}[Self-reinforcement]\label{prop:selfreinf}
Any per-item rule $\gamma_q=h(\Dhat^g_q)$ with $h$ monotone increasing and odd reinforces the plurality on both branches: $\Dhat^g_q>0$ up-weights confident traces, which agree with the plurality; $\Dhat^g_q<0$ up-weights unconfident traces, which are again the plurality side. Empirically such a rule agrees with \SC{} on $97.5\%$ of items and its residual flips are net-harmful ($1$ right vs.\ $9$ wrong per $400$ items).
\end{proposition}

\begin{proposition}[Winner's curse]\label{prop:curse}
On plurality-wrong items with $|D_q|>0.3$, the items where a flip could win, the agreement statistic's sign matches the true sign only $4\%$ of the time.
\end{proposition}

\begin{proposition}[Two-world unidentifiability]\label{prop:twoworld}
For any observed $(a,c)$, the worlds $\{\kappa>0,\ \text{minority correct}\}$ and $\{\kappa<0,\ \text{plurality correct}\}$ induce identical observable laws (constructively, $D$ computed against either truth satisfies $D^{w_1}=-D^{w_2}$). No label-free method can separate them.
\end{proposition}

Consequently the per-item oracle ($0.983$ in this harness) is unreachable, and the honest behaviour is to fall back to the global estimate, which \TACT's dead zone does: in the i.i.d.\ cell every variant returns bitwise \SC{} (zero discordant pairs).

\subsection{TACT-group}
Real heterogeneity is typically indexed by an observable covariate (domain, question type). With $\kappa$ indexed by a group label, running the estimator per group keeps every group inside the operating regime of Sections~\ref{sec:method}--\ref{sec:lf}; groups with fewer than $30$ dev (or $60$ unlabeled) items fall back to the global estimate, which Propositions~\ref{prop:selfreinf}--\ref{prop:twoworld} show is the only defensible default.

