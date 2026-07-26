"""RLEV-VoI: redundancy-discounted consensus with value-of-information stopping.

An inference-time reasoning pipeline for a frozen LLM. See ``docs/SPEC.md`` for
the full specification, honest novelty positioning, and falsification criteria.
"""

from .algorithm import RunResult, run_rlev_voi
from .baselines import (
    run_adaptive_consistency,
    run_cisc,
    run_dedup_sc,
    run_esc,
    run_rasc_lite,
    run_self_consistency,
    run_sprt,
)
from .config import DEFAULT, SC_EQUIVALENT, Config
from .consensus import essratio_dup, guarded_answer
from .kernel import build_kernel, cosine_similarity_matrix, hinge_pow, ngram_jaccard_matrix
from .posterior import ModeProbability, posterior_alpha, value_of_information
from .traces import TracePool, total_cost
from .weights import (
    block_model_effective_count,
    effective_counts,
    effective_weights,
    kish_dispersion,
    n_eff,
    raw_counts,
)

__all__ = [
    "Config",
    "DEFAULT",
    "SC_EQUIVALENT",
    "TracePool",
    "RunResult",
    "run_rlev_voi",
    "run_self_consistency",
    "run_adaptive_consistency",
    "run_cisc",
    "run_dedup_sc",
    "run_esc",
    "run_sprt",
    "run_rasc_lite",
    "build_kernel",
    "hinge_pow",
    "cosine_similarity_matrix",
    "ngram_jaccard_matrix",
    "effective_weights",
    "effective_counts",
    "raw_counts",
    "n_eff",
    "kish_dispersion",
    "block_model_effective_count",
    "ModeProbability",
    "posterior_alpha",
    "value_of_information",
    "essratio_dup",
    "guarded_answer",
    "total_cost",
]
