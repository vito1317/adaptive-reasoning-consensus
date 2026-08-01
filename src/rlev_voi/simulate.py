"""Synthetic trace generator (SPEC.md section 8.a).

.. warning::
   **This simulator cannot establish that RLEV-VoI helps on real traces.** It
   generates data from exactly the block-cluster structure the DDWC weighting
   assumes, so a "win" here is an artifact of the data-generating process. Per
   the spec it is used only to (1) verify implementation correctness and the
   mandatory unit tests, (2) confirm the block-model limits, (3) stress the
   verbatim-echo attack as a unit test of the guard, and (4) map the
   *useful-regime boundary* -- the kernel geometry beyond which the weights
   collapse to uniform and the method degenerates to Self-Consistency.

   Headline evidence must come from the real-API experiment (section 8.b), which
   requires an API key.

Generative model
----------------
An item has a latent correct answer ``a* = 0`` and a set of reasoning
*clusters*. Each cluster ``g`` carries an answer ``a_g``, a sampling weight, an
embedding centroid ``mu_g`` in ``R^d``, a spread ``sigma_g``, and an echo
probability. Drawing a trace::

    g       ~ Categorical(weights)
    echo    ~ Bernoulli(echo_prob_g)      # verbatim copy of an earlier trace in g
    e_i      = normalize(mu_g + sigma_g * N(0, I_d))       (if not an echo)
    a_i      = a_g with prob 1 - slip, else a uniform random answer
    c_i      = clip(0.5 + kappa_c * (1[a_i = a*] - 0.5) + eps, 0, 1)

``sem_ij`` is the clipped cosine of the embeddings. ``dup_ij`` is 1 for verbatim
copies and otherwise a low, semantically-correlated value -- distinct CoT traces
share some surface n-grams but nothing close to ``theta_dup``.
"""

from __future__ import annotations

from dataclasses import dataclass

import numpy as np

from .kernel import cosine_similarity_matrix
from .traces import TracePool


@dataclass
class Cluster:
    """One reasoning mode.

    ``tightness`` is the *extra* pairwise cosine similarity traces in this
    cluster share on top of the question-level baseline, so within-cluster
    similarity is ``sem_shared + tightness`` and cross-cluster similarity is
    ``sem_shared``. Parameterising by the resulting similarity (rather than by a
    Gaussian spread) is what keeps the synthetic kernel in the same numeric range
    as real sentence embeddings, where every trace answering the same question is
    already highly similar.
    """

    answer: int
    weight: float
    tightness: float
    echo_prob: float = 0.0


@dataclass
class SimConfig:
    """Parameters of the synthetic item generator."""

    clusters: tuple[Cluster, ...]
    n_answers: int = 4
    dim: int = 32
    slip: float = 0.05
    """Probability a trace reports an answer other than its cluster's."""
    kappa_c: float = 0.6
    """Confidence-correctness coupling. ``<= 0`` means miscalibrated."""
    kappa_c_sd: float = 0.0
    """Per-item heterogeneity: each item draws ``kappa ~ N(kappa_c, kappa_c_sd)``.

    Nonzero values model corpora where the confidence channel is informative on
    some questions and useless or inverted on others -- the setting where a
    single global trust decision is provably suboptimal. With the latent kappa
    i.i.d. and no observable covariate, per-item label-free adaptation is also
    IMPOSSIBLE (winner's-curse / two-world unidentifiability -- see
    REPORT-TACT section on the hier study), so this regime is a floor for
    every legitimate method."""
    group_kappas: tuple[float, ...] | None = None
    """Observable-covariate heterogeneity: each item is assigned a group id
    (uniform over the tuple, stored in ``meta['group']``) and uses that group's
    kappa. This is the STRUCTURED heterogeneity of real corpora -- the channel
    is informative on one domain and inverted on another -- and unlike the
    i.i.d. case it is exploitable: run the estimator per group. Overrides
    ``kappa_c``/``kappa_c_sd`` when set."""
    conf_transform: str = "none"
    """Strictly monotone distortion applied to confidences AFTER coupling.

    Rank-preserving by construction, so the signal's DISCRIMINATION (AUC) is
    untouched while its CALIBRATION (ECE) is destroyed -- the exact case that
    separates rank-based trust estimators from ECE-style gates.

    * ``none``          -- identity.
    * ``compress``      -- ``0.5 + 0.15*(c-0.5)``: everything huddles near 0.5
      (systematic underconfidence).
    * ``overconfident`` -- steep sigmoid pushing mass toward 0/1.
    * ``power``         -- ``c**4``: systematically low, long left tail.
    """
    echo_conf: float | None = None
    """If set, traces in verbatim-echo components report this confidence
    (plus noise) regardless of correctness -- the 'confident echo' poison that
    corrupts both the vote and any agreement-based reliability proxy."""
    conf_noise: float = 0.10
    dup_base: float = 0.5
    """Scales the semantic-to-lexical leakage for non-identical traces."""
    gen_tokens_mean: float = 250.0
    gen_tokens_sd: float = 40.0
    sem_shared: float = 0.65
    """Pairwise cosine every trace shares by virtue of answering the same question.

    Real sentence embeddings of CoT traces for one problem sit around 0.65-0.85,
    which is *above* the kernel's ``theta_sem = 0.6`` hinge. Setting this to ~0
    (isotropic random embeddings) would put every pair below the hinge and
    silently disable the semantic channel entirely.
    """
    correct_answer: int = 0
    permute_labels: bool = True
    """Relabel answer codes per item so the correct answer is not always 0.

    Off reproduces the pre-fix harness, in which SC's lowest-index tie-break
    coincided with the correct answer on every tied item.
    """


def _monotone_distort(c: np.ndarray, kind: str) -> np.ndarray:
    """Strictly monotone confidence distortions (rank/AUC preserved, ECE wrecked)."""
    if kind == "none":
        return c
    if kind == "compress":
        return 0.5 + 0.15 * (c - 0.5)
    if kind == "overconfident":
        # Range on (0,1) already; clipping would create ties and break ranks.
        return 1.0 / (1.0 + np.exp(-8.0 * (c - 0.5)))
    if kind == "power":
        return c**4
    raise ValueError(f"unknown conf_transform {kind!r}")


def generate_item(cfg: SimConfig, k_max: int, rng: np.random.Generator) -> TracePool:
    """Generate one item's full pool of ``k_max`` cached traces."""
    weights = np.array([c.weight for c in cfg.clusters], dtype=float)
    weights = weights / weights.sum()

    def unit(v: np.ndarray) -> np.ndarray:
        return v / max(float(np.linalg.norm(v)), 1e-12)

    # Orthogonal-ish basis: one shared question direction, one direction per
    # cluster, and per-trace noise. Mixing unit vectors with weights that sum to
    # 1 makes the resulting cosine similarities directly predictable:
    #   same cluster      ~ sem_shared + tightness
    #   different cluster ~ sem_shared
    shared_dir = unit(rng.normal(size=cfg.dim))
    cluster_dirs = np.stack([unit(rng.normal(size=cfg.dim)) for _ in cfg.clusters])

    embeddings = np.zeros((k_max, cfg.dim))
    answers = np.zeros(k_max, dtype=int)
    is_echo_of = -np.ones(k_max, dtype=int)
    members: dict[int, list[int]] = {g: [] for g in range(len(cfg.clusters))}

    for i in range(k_max):
        g = int(rng.choice(len(cfg.clusters), p=weights))
        cl = cfg.clusters[g]
        if members[g] and rng.random() < cl.echo_prob:
            src = int(rng.choice(members[g]))
            embeddings[i] = embeddings[src]
            answers[i] = answers[src]
            is_echo_of[i] = src
        else:
            w_shared = float(np.clip(cfg.sem_shared, 0.0, 1.0))
            w_cluster = float(np.clip(cl.tightness, 0.0, 1.0 - w_shared))
            w_noise = max(1.0 - w_shared - w_cluster, 0.0)
            embeddings[i] = unit(
                np.sqrt(w_shared) * shared_dir
                + np.sqrt(w_cluster) * cluster_dirs[g]
                + np.sqrt(w_noise) * unit(rng.normal(size=cfg.dim))
            )
            a = cl.answer
            if rng.random() < cfg.slip:
                a = int(rng.integers(cfg.n_answers))
            answers[i] = a
        members[g].append(i)

    sem = cosine_similarity_matrix(embeddings)

    # Lexical duplication: 1 for verbatim echoes, otherwise a low value that
    # tracks semantic similarity (shared phrasing) but stays well under theta_dup.
    dup = cfg.dup_base * np.clip(sem, 0.0, 1.0) ** 2
    dup = np.clip(dup + rng.normal(scale=0.02, size=dup.shape), 0.0, 1.0)
    dup = 0.5 * (dup + dup.T)
    # Echo groups must be a CLIQUE, not a chain. `is_echo_of` is a forest: a
    # trace may echo a source that is itself an echo, so two traces can be
    # byte-identical siblings without either being the other's ancestor. Walking
    # only the ancestor chain leaves sibling pairs at the generic leakage value
    # (~0.5), well below theta_dup, which silently under-arms the guard in the
    # very regime meant to test it. Group by root instead.
    root = np.arange(k_max)
    for i in range(k_max):
        r = i
        while is_echo_of[r] >= 0:
            r = is_echo_of[r]
        root[i] = r
    for r in np.unique(root):
        members_of_r = np.flatnonzero(root == r)
        if members_of_r.size > 1:
            idx = np.ix_(members_of_r, members_of_r)
            dup[idx] = 1.0
            sem[idx] = 1.0
    np.fill_diagonal(dup, 1.0)
    np.fill_diagonal(sem, 1.0)

    hit = (answers == cfg.correct_answer).astype(float)
    group = -1
    if cfg.group_kappas is not None:
        group = int(rng.integers(len(cfg.group_kappas)))
        kappa_item = float(cfg.group_kappas[group])
    elif cfg.kappa_c_sd > 0:
        kappa_item = float(rng.normal(cfg.kappa_c, cfg.kappa_c_sd))
    else:
        kappa_item = cfg.kappa_c
    conf = 0.5 + kappa_item * (hit - 0.5) + rng.normal(scale=cfg.conf_noise, size=k_max)
    if cfg.echo_conf is not None:
        # Confident-echo poison: every member of a multi-trace echo component
        # reports high confidence regardless of correctness.
        comp_size = np.bincount(root, minlength=k_max)[root]
        in_echo = comp_size > 1
        conf[in_echo] = cfg.echo_conf + rng.normal(scale=cfg.conf_noise, size=int(in_echo.sum()))
    conf = np.clip(conf, 0.01, 0.99)
    conf = _monotone_distort(conf, cfg.conf_transform)

    gen_tokens = np.clip(
        rng.normal(cfg.gen_tokens_mean, cfg.gen_tokens_sd, size=k_max), 20.0, None
    )

    # Relabel the answer codes by a per-item random permutation. Without this
    # the correct answer is code 0 on every item, and since ``np.argmax``
    # breaks ties toward the lowest index, plain SC wins every tied item for
    # free: measured at 67.7% on near-tied items against 50.4% for a random
    # tie-break. Any method that perturbs the weights off integers loses that
    # artificial advantage and appears to be harmed by the perturbation. The
    # permutation is drawn from the item's own generator, so datasets stay
    # reproducible.
    if cfg.permute_labels:
        perm = rng.permutation(cfg.n_answers)
        answers = perm[answers]
        correct = int(perm[cfg.correct_answer])
    else:
        correct = cfg.correct_answer

    return TracePool(
        answers=answers,
        confidences=conf,
        sem=sem,
        dup=dup,
        gen_tokens=gen_tokens,
        correct=correct,
        n_answers=cfg.n_answers,
        meta={"is_echo_of": is_echo_of, "group": group},
    )


def generate_dataset(cfg: SimConfig, n_items: int, k_max: int, seed: int = 0) -> list[TracePool]:
    """Generate ``n_items`` independent items."""
    rng = np.random.default_rng(seed)
    return [generate_item(cfg, k_max, rng) for _ in range(n_items)]


# --------------------------------------------------------------------------
# Regimes R1-R5 (SPEC.md section 8.a). These exist to exercise the estimator
# and the guard, and to locate the useful-regime boundary -- NOT to argue the
# method works on real data.
# --------------------------------------------------------------------------

REGIMES: dict[str, SimConfig] = {
    # R1: independent reasoning, no duplication and no cluster structure beyond
    # the shared question. RLEV-VoI must match ASC and DDWC must match SC --
    # if they diverge here the reduction is broken.
    "R1_independent": SimConfig(
        clusters=(
            Cluster(answer=0, weight=0.45, tightness=0.02),
            Cluster(answer=1, weight=0.20, tightness=0.02),
            Cluster(answer=2, weight=0.20, tightness=0.02),
            Cluster(answer=3, weight=0.15, tightness=0.02),
        ),
    ),
    # R2: a tight *wrong* cluster out-votes a diffuse correct one. The regime
    # the method is designed for -- and precisely why a win here proves nothing
    # about real traces.
    "R2_correlated_wrong": SimConfig(
        clusters=(
            Cluster(answer=0, weight=0.42, tightness=0.02),
            Cluster(answer=1, weight=0.48, tightness=0.30, echo_prob=0.55),
            Cluster(answer=2, weight=0.10, tightness=0.05),
        ),
    ),
    # R3: the correct answer is itself a tight canonical derivation -- the
    # similarity-correctness confound. DECOMP + guard must not regress below SC,
    # while the GLOBAL semantic-only scope is expected to hurt.
    "R3_easy_correct_cluster": SimConfig(
        clusters=(
            Cluster(answer=0, weight=0.70, tightness=0.30),
            Cluster(answer=1, weight=0.18, tightness=0.02),
            Cluster(answer=2, weight=0.12, tightness=0.02),
        ),
    ),
    # R4: unmixed verbatim echo of a wrong template -- the guard's unit test.
    "R4_verbatim_echo": SimConfig(
        clusters=(
            Cluster(answer=0, weight=0.40, tightness=0.02),
            Cluster(answer=1, weight=0.60, tightness=0.32, echo_prob=0.85),
        ),
        n_answers=3,
    ),
    # R5: confidence is anti-correlated with correctness; the ECE gate must
    # disable the confidence channel and the posterior must be unaffected.
    "R5_miscalibrated_conf": SimConfig(
        clusters=(
            Cluster(answer=0, weight=0.45, tightness=0.02),
            Cluster(answer=1, weight=0.35, tightness=0.12),
            Cluster(answer=2, weight=0.20, tightness=0.05),
        ),
        kappa_c=-0.6,
    ),
}
