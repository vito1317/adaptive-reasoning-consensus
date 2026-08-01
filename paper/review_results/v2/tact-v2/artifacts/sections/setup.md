# Problem Setup  (tact.tex lines 68-85, verbatim LaTeX)

\section{Problem Setup}\label{sec:setup}

\subsection{Notation}
Items $q=1,\dots,Q$; item $q$ has $m_q$ sampled traces. Trace $(q,i)$ yields an answer $a_{q,i}$ in a discrete set and a confidence $c_{q,i}\in(0,1)$; correctness is $y_{q,i}=\mathbf{1}[a_{q,i}=a_q^\ast]$, unobserved at test time. Plain \SC{} returns $\arg\max_A n_q(A)$ where $n_q(A)$ counts votes for answer $A$. CISC-power weights votes by $c_{q,i}^{\,\gamma}$ with a fixed $\gamma>0$.

\subsection{The confidence dilemma}
The synthetic oracle draws, per item, traces from a cluster mixture with a latent correct answer and generates confidence as
\begin{equation}\label{eq:confmodel}
c_{q,i}=\operatorname{clip}\!\big(\tfrac12+\kappa\,(y_{q,i}-\tfrac12)+\varepsilon_{q,i},\,0.01,\,0.99\big),
\end{equation}
with noise $\varepsilon\sim\mathcal{N}(0,0.1^2)$ and coupling $\kappa\in[-0.6,0.6]$. Fig.~\ref{fig:baselines} maps the baseline landscape \emph{before} the proposed method existed: unconditional weighting (CISC, $\gamma=1$) collapses on $\kappa<0$; an ECE gate never opens off the well-calibrated diagonal; a sign-corrected AUC gate over dev labels nearly saturates the homogeneous sweep. This pre-measurement fixes where a new method can legitimately claim wins---monotone distortion of the confidence scale, covariate heterogeneity, small dev sets, and label-free operation---and the evaluation holds itself to exactly those cells.

\begin{figure}[t]
\centering
\includegraphics[width=\columnwidth]{figs/kappa_sweep.png}
\caption{The pre-measured problem statement: accuracy of baseline confidence policies at fixed $K{=}15$ as the true coupling $\kappa$ varies. A trivial sign-corrected AUC gate (green) nearly saturates the homogeneous sweep; the headroom for any new method (shaded) concentrates in the mid-range and, off this plot, in distortion, heterogeneity, and label-free cells.}
\label{fig:baselines}
\end{figure}
