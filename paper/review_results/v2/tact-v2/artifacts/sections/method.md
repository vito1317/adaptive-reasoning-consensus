# TACT (method)  (tact.tex lines 87-172, verbatim LaTeX)

\section{TACT}\label{sec:method}

\subsection{Vote family}
Within item $q$, let $R_{q,i}$ be the midrank of $c_{q,i}$ (ties averaged) and
\begin{equation}\label{eq:vdw}
\varphi_{q,i}=\frac{v_{q,i}-\bar v_q}{\sigma_q},\qquad v_{q,i}=\Phi^{-1}\!\Big(\frac{R_{q,i}}{m_q+1}\Big),
\end{equation}
where $\sigma_q$ is the \emph{realized} standard deviation of $v$ within the item (the no-tie value is $0.62$ at $m{=}4$ but $0.95$ at $m{=}40$; a closed form would silently rescale $\gamma$ across budgets), and $\varphi\equiv 0$ if $\sigma_q\le 10^{-8}$ (all-tied confidences vote as plain \SC). The vote is
\begin{equation}\label{eq:vote}
\hat a_q=\arg\max_A \sum_{i:\,a_{q,i}=A}\exp\big(\gamma\,\varphi_{q,i}\big),
\end{equation}
and when $\gamma=0$ the implementation \emph{calls the \SC{} routine itself}, making the zero-trust anchor bitwise exact rather than equal in distribution. Because \eqref{eq:vdw} depends on $c$ only through within-item ranks, every strictly monotone distortion of the confidence scale leaves \eqref{eq:vote} unchanged.

\subsection{Reliability statistic}
For item $q$ with $n^1_q$ positive and $n^0_q$ negative labels (dev: $y$; label-free: the pseudo-label of Section~\ref{sec:lf}), the Mann--Whitney statistic on midranks gives
\begin{equation}
D_q = 2\,\mathrm{AUC}_q-1,\qquad \mathrm{AUC}_q=\frac{U_q}{n^1_q n^0_q},
\end{equation}
which equals $2\cdot\mathrm{WQD}_q-1$ in CISC's notation. Pooling uses van Elteren pair-count weights $N_q=n^1_q n^0_q$ \cite{vanelteren1960}:
\begin{equation}\label{eq:pooled}
\Dhat=\frac{\sum_q N_q D_q}{\sum_q N_q}.
\end{equation}
Under the within-item exchangeability null, $U_q$ has the exact tie-corrected variance $n^1_qn^0_q(m_q{+}1)/12\cdot[1-\sum_t(t^3-t)/(m_q^3-m_q)]$, yielding a null standard error $\mathrm{SE}_0$; between-item heterogeneity is captured by the closed-form delete-one-item jackknife $\mathrm{SE}_J$. The conservative choice is
\begin{equation}
\mathrm{SE}=\max\big(\mathrm{SE}_0,\ \mathrm{SE}_J,\ \tfrac{1}{2\sqrt{N}}\big),\qquad r=\Dhat/\mathrm{SE}.
\end{equation}
Because $D$ is a pairwise functional, $\mathbb{E}[\Dhat]$ does not depend on $m_q$: an exponent estimated at $m{=}40$ transfers to deployment at $m{=}8$.

\subsection{Tempering map}
\emph{Shrinkage.} Positive-part James--Stein with a significance floor $\nu$:
\begin{equation}\label{eq:js}
\tilde D=\sign(\Dhat)\,\max\!\big(0,\ |\Dhat|-\nu^2\mathrm{SE}^2/|\Dhat|\big),
\end{equation}
with dead zone $\{|r|\le\nu\}$; $\nu_{\mathrm{dev}}=1.28$, $\nu_{\mathrm{LF}}=2.33$. With $\nu=1$, \eqref{eq:js} is exactly the empirical-Bayes posterior mean under a $\mathcal{N}(0,\tau^2)$ prior with plug-in $\hat\tau^2=\max(0,\Dhat^2-\mathrm{SE}^2)$ \cite{james1961estimation}. The map is odd, continuous, never exceeds $|\Dhat|$, and is monotone in $\Dhat$ and anti-monotone in $\mathrm{SE}$.

\emph{Link.} Model $\varphi\,|\,y\sim\mathcal{N}(\mu_y,s^2)$ within item with the \emph{mixture} standardized to unit variance, which is what \eqref{eq:vdw} enforces, so $s^2=1/(1+\bar p(1-\bar p)u^2)$ where $u=\sqrt2\,\Phi^{-1}\!\big(\tfrac{1+\tilde D}{2}\big)$ and $\bar p$ is the base rate of correct traces. The Bayes-optimal per-trace log-weight coefficient is then
\begin{equation}\label{eq:link}
\gamma^\ast=\frac{u}{s}=u\sqrt{1+\bar p(1-\bar p)\,u^2},
\end{equation}
capped at $\gamma_{\max}$ ($4$ dev, $2$ label-free). The uncorrected link $\gamma=u$ under-weights strong channels by up to ${\sim}50\%$ at $D=0.9$.

\subsection{\TACT{} in one expression}\label{sec:oneline}
Two simplifications collapse the pipeline. Factoring $\Dhat$ out of
\eqref{eq:js} makes the shrinkage a multiplicative gain in the pooled
$z$-statistic $\zeta=\Dhat/\mathrm{SE}$ alone, and substituting
$u=\sqrt2\,z$ with $z=\Phi^{-1}\!\big(\tfrac{1+\tilde D}{2}\big)$ into
\eqref{eq:link} removes the nested radical. \TACT{} is then
\begin{equation}\label{eq:oneline}
\boxed{\;
\hat a_q=\arg\max_A \sum_{i:\,a_{q,i}=A}\exp\big(\gamma\,\varphi_{q,i}\big),
\quad
\gamma=\Big[z\sqrt{2+4\bar p(1-\bar p)z^{2}}\Big]_{-\gamma_{\max}}^{\gamma_{\max}},
\;}
\end{equation}
\begin{equation}\label{eq:oneline2}
z=\Phi^{-1}\!\Big(\tfrac12\big[1+\Dhat\,(1-\nu^{2}/\zeta^{2})_{+}\big]\Big),
\qquad \zeta=\Dhat/\mathrm{SE},
\end{equation}
with $\Dhat$ from \eqref{eq:pooled} and $\varphi$ from \eqref{eq:vdw}. At the
default $\bar p=\tfrac12$ the exponent is exactly
\begin{equation}\label{eq:half}
\gamma=z\sqrt{2+z^{2}},\qquad z=\Phi^{-1}(\widehat{\mathrm{AUC}}),
\end{equation}
one probit and one square root. Nothing in it is fitted to outcomes: $\nu$ is a
significance level and $\gamma_{\max}$ a clip, both fixed before any data is
seen. The clip is not cosmetic, though. Where $\Dhat$ saturates it binds, and
the vote then sees $\gamma_{\max}$ rather than the derived magnitude
(Section~\ref{sec:results}). The dead zone is now visible as a single condition,
$|\zeta|\le\nu$, on which $\gamma$ is identically zero and \eqref{eq:oneline}
is bitwise \SC{} by Proposition~\ref{prop:sc}. Equations
\eqref{eq:oneline}--\eqref{eq:half} are verified equivalent to the shipped
implementation over randomised inputs including every boundary
(\texttt{tests/test\_formula.py}).

\subsection{Anchor properties}
\begin{proposition}[Exact \SC{} reduction]\label{prop:sc}
At $\gamma=0$, \eqref{eq:vote} equals plain \SC{} as a function on every trace pool, including tie-breaks. Under $D=0$, $P(\gamma=0)\to 2\Phi(\nu)-1$ ($80\%$ dev, $98\%$ label-free), and $\gamma$ is continuous through the dead-zone boundary, so a false positive applies an infinitesimal exponent.
\end{proposition}
\begin{proposition}[Exact CISC reduction]\label{prop:cisc}
With the feature map $\varphi^{\log}_{q,i}=\log c_{q,i}-\overline{\log c_q}$, the weights equal $\smash{\kappa_q\,c_{q,i}^{\,\gamma}}$ with a per-item constant $\kappa_q>0$; hence the argmax, the ties, and the normalized vote shares coincide with CISC-power$(\gamma)$ on every pool.
\end{proposition}
\begin{proposition}[Regularity]\label{prop:reg}
The composite $g(\Dhat,\mathrm{SE})$ is continuous, odd, nondecreasing in $\Dhat$, nonincreasing in $\mathrm{SE}$ in magnitude, with $g(D,0^+)=\gamma^\ast(D)$.
\end{proposition}
Proofs are elementary and pinned by unit tests in the released code (98 tests; the permutation-verified null variance, the EB identity in \eqref{eq:js}, and the link derivation \eqref{eq:link} are each tested numerically).

