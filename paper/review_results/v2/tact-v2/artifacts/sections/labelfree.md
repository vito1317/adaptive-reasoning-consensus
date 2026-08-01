# Label-Free Estimation  (tact.tex lines 173-188, verbatim LaTeX)

\section{Label-Free Estimation}\label{sec:lf}

\subsection{Pipeline}
(i)~\emph{Dedup:} single-linkage duplicate groups on the lexical-similarity channel at $0.95$; each trace gets weight $1/|\text{group}|$ for plurality determination and pair weighting. (ii)~\emph{Pseudo-label:} $g_{q,i}=\mathbf{1}[a_{q,i}=M_q]$ with $M_q$ the dedup-weighted plurality. (iii)~\emph{Margin gate:} keep the top $60\%$ of items by dedup-weighted margin. (iv)~Compute \eqref{eq:pooled} with $\mathrm{lab}=g$, giving $(\Dhat_g,\mathrm{SE}_g,r_g)$.

\subsection{Sign consistency and its boundary}
\begin{proposition}[Attenuation identity]\label{prop:ccn}
Let $\bar\rho$ be the pair-weighted probability that an item's plurality is wrong. If the plurality-error event is independent of $\varphi$ given $y$ (class-conditional noise), then
$\mathbb{E}[\Dhat_g]=(1-2\bar\rho)\,D$.
In particular $\sign\mathbb{E}[\Dhat_g]=\sign D$ whenever $\bar\rho<1/2$: the label-free estimate can only under-trust, never mis-sign.
\end{proposition}
The identity fails when the flip is \emph{caused} by confidence, that is, under a confident echo. There the observable law under $\{$majority right, $D<0\}$ and $\{$majority wrong via confident echo, $D>0\}$ is identical (the two-root ambiguity of \cite{parisi2014ranking} restated for a single channel), so any label-free guarantee is necessarily conditional; it is stated as such rather than papered over.

\subsection{De-attenuation and alarms}
Split-half agreement over $R{=}20$ random half-splits estimates $\alpha=p^2+(1-p)^2/k$ under a one-coin model with $k$ effective wrong alternatives (inverse-Simpson), inverted as $p=[1+\sqrt{1-(k{+}1)(1-k\alpha)}]/(k{+}1)$; $\Dhat_g$ is divided by the \emph{upper} $95\%$ bootstrap bound of $2p-1$ (floored at $0.2$), which can only under-inflate. Four alarms force $\gamma=0$: duplicate collapse (median Kish ratio $<0.5$), sign-aware margin-decoupling, root ambiguity in the split-half quadratic, and insufficient gated items. The margin-decoupling alarm must condition on the estimated trust direction: a sign-naive version (``plurality has the highest mean $\varphi$'') false-alarms on every benign anti-correlated channel---a defect the author hit, diagnosed, and fixed, and which the released tests pin. Finally the significance gate acts on the \emph{raw} $z$ (unbiased sign under Proposition~\ref{prop:ccn}) and temper on the de-attenuated value. A semi-label-free mode takes only the sign from ${\sim}50$ dev labels, routing it into the pipeline and disabling only the proxy-sign alarm; this purchases immunity to the ambiguity above at negligible labeling cost.

