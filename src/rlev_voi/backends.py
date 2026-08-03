"""Real-LLM backends for the headline experiment (SPEC.md section 8.b).

Traces are sampled **once** per item up to ``K_max`` and cached to disk; every
method then replays the identical pool, which makes the comparison paired and
low-variance. Only prefix-replayable methods are valid under this protocol --
generation-altering stoppers must be run natively at matched expected budget and
are out of scope here (the spec scopes the claim accordingly).

No API key is required to import this module. ``pip install anthropic`` (or
``openai``) and export the corresponding key to actually sample.
"""

from __future__ import annotations

import hashlib
import json
import os
import re
from dataclasses import asdict, dataclass
from pathlib import Path

import numpy as np

from .kernel import cosine_similarity_matrix, ngram_jaccard_matrix
from .traces import TracePool

COT_PROMPT = (
    "Solve the problem. Think step by step, then end your reply with a final line "
    'formatted exactly as "ANSWER: <answer>" followed by a line '
    '"CONFIDENCE: <a number between 0 and 1>".\n\nProblem: {question}'
)


@dataclass
class Trace:
    """One sampled chain of thought."""

    text: str
    answer: str
    confidence: float
    gen_tokens: int


class LLMBackend:
    """Interface a backend must satisfy."""

    def sample(self, question: str, k: int, temperature: float) -> list[Trace]:
        raise NotImplementedError


class AnthropicBackend(LLMBackend):
    """Claude backend. Requires ``anthropic`` and ``ANTHROPIC_API_KEY``."""

    def __init__(self, model: str = "claude-sonnet-5", max_tokens: int = 1024):
        try:
            import anthropic
        except ImportError as e:  # pragma: no cover - environment dependent
            raise ImportError("pip install anthropic") from e
        if not os.environ.get("ANTHROPIC_API_KEY"):
            raise RuntimeError("ANTHROPIC_API_KEY is not set")
        self._client = anthropic.Anthropic()
        self.model = model
        self.max_tokens = max_tokens

    def sample(self, question: str, k: int, temperature: float) -> list[Trace]:
        out = []
        for _ in range(k):
            msg = self._client.messages.create(
                model=self.model,
                max_tokens=self.max_tokens,
                temperature=temperature,
                messages=[{"role": "user", "content": COT_PROMPT.format(question=question)}],
            )
            text = "".join(b.text for b in msg.content if getattr(b, "type", "") == "text")
            ans, conf = parse_answer_and_confidence(text)
            out.append(Trace(text, ans, conf, int(msg.usage.output_tokens)))
        return out


class OpenAIBackend(LLMBackend):
    """OpenAI backend. Requires ``openai`` and ``OPENAI_API_KEY``.

    When the model returns logprobs the confidence is derived from the mean
    token probability of the answer line, which is the pre-registered primary
    confidence signal; the verbalized number is the secondary one.
    """

    def __init__(self, model: str = "gpt-4o-mini", max_tokens: int = 1024,
                 use_logprobs: bool = True, base_url: str | None = None):
        """``base_url`` points the OpenAI client at any compatible server.

        This is what makes the capability-ladder campaign possible without new
        code: vLLM, OpenRouter and llama.cpp all speak this API, so a 3B and a
        frontier model differ only by ``model`` and ``base_url``. It also
        reaches the open-weight models that actually return logprobs, which is
        the pre-registered primary confidence signal and the one the
        Anthropic-backed campaigns could not collect.

        Falls back to ``OPENAI_BASE_URL`` so a ladder can be swept from the
        environment. The API key requirement is relaxed when a base_url is
        given, because local servers usually do not want one.
        """
        try:
            from openai import OpenAI
        except ImportError as e:  # pragma: no cover - environment dependent
            raise ImportError("pip install openai") from e
        base_url = base_url or os.environ.get("OPENAI_BASE_URL")
        if not base_url and not os.environ.get("OPENAI_API_KEY"):
            raise RuntimeError("OPENAI_API_KEY is not set")
        self._client = OpenAI(base_url=base_url) if base_url else OpenAI()
        self.base_url = base_url
        self.model = model
        self.max_tokens = max_tokens
        self.use_logprobs = use_logprobs

    def sample(self, question: str, k: int, temperature: float) -> list[Trace]:
        out = []
        for _ in range(k):
            r = self._client.chat.completions.create(
                model=self.model,
                max_tokens=self.max_tokens,
                temperature=temperature,
                logprobs=self.use_logprobs,
                messages=[{"role": "user", "content": COT_PROMPT.format(question=question)}],
            )
            choice = r.choices[0]
            text = choice.message.content or ""
            ans, conf = parse_answer_and_confidence(text)
            if self.use_logprobs and getattr(choice, "logprobs", None):
                lp = [t.logprob for t in choice.logprobs.content or []]
                if lp:
                    conf = float(np.exp(np.mean(lp[-24:])))  # mean prob over the tail
            out.append(Trace(text, ans, conf, int(r.usage.completion_tokens)))
        return out


_ANSWER_RE = re.compile(r"ANSWER:\s*(.+)", re.IGNORECASE)
_CONF_RE = re.compile(r"CONFIDENCE:\s*([01](?:\.\d+)?)", re.IGNORECASE)


def parse_answer_and_confidence(text: str) -> tuple[str, float]:
    """Extract the final answer and the verbalized confidence."""
    m = _ANSWER_RE.findall(text)
    answer = m[-1].strip().rstrip(".").strip() if m else ""
    c = _CONF_RE.findall(text)
    conf = float(c[-1]) if c else 0.5
    return answer, min(max(conf, 0.0), 1.0)


def normalise_answer(a: str) -> str:
    """Light exact-match normalisation for answer bucketing."""
    a = a.strip().lower()
    a = re.sub(r"[\s,$]+", "", a)
    a = re.sub(r"\.0+$", "", a)
    return a


def tfidf_embeddings(texts: list[str], max_features: int = 4096) -> np.ndarray:
    """Hashed TF-IDF embeddings -- a dependency-free stand-in for a sentence encoder.

    Swap in a real encoder for the headline experiment; the semantic channel is
    only as good as the embedder, and the spec's kernel-collapse limitation
    applies more strongly to weak embeddings.
    """
    docs = [re.findall(r"[a-z0-9]+", t.lower()) for t in texts]
    n = len(docs)
    X = np.zeros((n, max_features))
    for i, toks in enumerate(docs):
        grams = toks + [f"{a}_{b}" for a, b in zip(toks, toks[1:])]
        for g in grams:
            h = int(hashlib.md5(g.encode()).hexdigest()[:8], 16) % max_features
            X[i, h] += 1.0
    df = np.count_nonzero(X, axis=0)
    idf = np.log((1 + n) / (1 + df)) + 1.0
    X = X * idf
    return X


def build_pool(traces: list[Trace], gold: str, embeddings: np.ndarray | None = None) -> TracePool:
    """Turn sampled traces into a :class:`TracePool` with both similarity channels."""
    texts = [t.text for t in traces]
    codes: dict[str, int] = {}
    answers = []
    for t in traces:
        key = normalise_answer(t.answer)
        answers.append(codes.setdefault(key, len(codes)))
    gold_key = normalise_answer(gold)
    correct = codes.get(gold_key, -1)

    E = tfidf_embeddings(texts) if embeddings is None else np.asarray(embeddings, dtype=float)
    sem = cosine_similarity_matrix(E)
    dup = ngram_jaccard_matrix(texts, n=5)

    return TracePool(
        answers=np.array(answers, dtype=int),
        confidences=np.array([t.confidence for t in traces], dtype=float),
        sem=sem,
        dup=dup,
        gen_tokens=np.array([t.gen_tokens for t in traces], dtype=float),
        correct=correct,
        n_answers=max(len(codes), 1),
        meta={"answer_codes": codes, "gold": gold_key},
    )


def cached_sample(
    backend: LLMBackend,
    question: str,
    k: int,
    temperature: float,
    cache_dir: Path,
    item_id: str,
) -> list[Trace]:
    """Sample once, reuse forever. Keyed by item, K, temperature and prompt."""
    cache_dir.mkdir(parents=True, exist_ok=True)
    # The key must pin everything that changes the traces: the question text
    # itself, the model and provider, K, temperature and the prompt template.
    # Keying on the row index alone silently shares one model's cached traces
    # with another model, and one dataset's with another dataset.
    model = getattr(backend, "model", "unknown")
    provider = type(backend).__name__
    payload = "|".join([provider, str(model), item_id, question, str(k), str(temperature), COT_PROMPT])
    key = hashlib.sha256(payload.encode()).hexdigest()[:32]
    path = cache_dir / f"{key}.json"
    if path.exists():
        return [Trace(**d) for d in json.loads(path.read_text())]
    traces = backend.sample(question, k, temperature)
    path.write_text(json.dumps([asdict(t) for t in traces], ensure_ascii=False))
    return traces
