# Experimental Setup  (tact.tex lines 211-249, verbatim LaTeX)

\section{Experimental Setup}\label{sec:exp}

\textbf{Harness.} A cluster-mixture oracle generates, per item, up to $K_{\max}{=}20$ cached traces with answers, confidences \eqref{eq:confmodel}, and two similarity channels; all methods replay identical pools (paired comparisons, exact McNemar tests). Voting budget $K{=}15$; $400$ items per cell on the sweep, $600$ for the group study; dev splits of $200$ (primary) and $50$ (small-dev).

\textbf{Regimes.} The $\kappa$ sweep $\{-0.6,\dots,+0.6\}$; three strictly monotone confidence distortions (compression toward $0.5$, over-confident sigmoid, fourth power), rank-preserving by construction, so discrimination is intact while calibration is destroyed; i.i.d.\ heterogeneity ($\kappa_q\sim\mathcal{N}(0,0.6^2)$); covariate-structured heterogeneity (three groups at $+0.6/0/-0.6$); and a confident-echo poison (a wrong cluster echoes verbatim with confidence $0.95$).

\textbf{Baselines.} \SC; CISC-power with $\gamma\in\{0.25,\dots,4\}$; \emph{CISC-devT}, the published dev-calibrated protocol (positive grid picked on dev); a binary ECE gate; \emph{SignGrid-dev}, the strongest trivial baseline (signed exponent grid picked on dev); and the test-set oracle over signed fixed exponents as the upper envelope. The group study adds the naive self-referential per-item method as a negative control and the per-item link oracle as the ceiling.

\textbf{Pre-registered falsifiers.} F1: \TACT-dev significantly below the best fixed-$\gamma$ CISC at $\kappa{=}{+}0.6$. F2: either variant significantly below \SC{} anywhere on the sweep. F3: the label-free variant fails to beat the ECE gate on sweep average. F4: CISC-devT or SignGrid-dev matches \TACT-dev everywhere, including the distortion, heterogeneity, and small-dev cells.

\begin{table}[t]
\centering
\caption{Coupling sweep (accuracy at $K{=}15$; $400$ paired items per cell; dev $n{=}200$). Published protocols sit at the \SC{} floor on the entire negative half-axis.}
\label{tab:sweep}
\setlength{\tabcolsep}{3.4pt}
\begin{tabular}{r cc cc cc c}
\toprule
$\kappa$ & \SC & ECE & devT & SignGrid & \textbf{\TACT-dev} & \textbf{\TACT-LF} & oracle\\
\midrule
$-0.6$ & .807 & .807 & .807 & 1.000 & \textbf{1.000} & \textbf{1.000} & 1.000\\
$-0.4$ & .797 & .797 & .797 & 1.000 & \textbf{1.000} & \textbf{1.000} & 1.000\\
$-0.2$ & .835 & .835 & .835 & .993 & .978 & .978 & .993\\
$-0.1$ & .762 & .762 & .762 & .892 & .880 & .885 & .892\\
$0.0$  & .835 & .835 & .835 & .835 & .835 & .835 & .835\\
$+0.1$ & .795 & .795 & .917 & .917 & .902 & .902 & .917\\
$+0.2$ & .845 & .845 & .993 & .993 & .988 & .988 & .993\\
$+0.4$ & .838 & .838 & 1.000 & 1.000 & \textbf{1.000} & \textbf{1.000} & 1.000\\
$+0.6$ & .782 & .782 & 1.000 & 1.000 & \textbf{1.000} & \textbf{1.000} & 1.000\\
\bottomrule
\end{tabular}
\end{table}

\begin{figure}[t]
\centering
\includegraphics[width=\columnwidth]{figs/tact_sweep.png}
\caption{Main result on the confidence-usage frontier. \TACT-dev and the fully label-free \TACT-LF track the signed oracle across the sweep; CISC-devT and the ECE gate sit at the \SC{} floor for all $\kappa<0$.}
\label{fig:sweep}
\end{figure}

