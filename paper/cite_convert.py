"""Convert IEEEtran's numeric ``\\cite`` into natbib author-year commands.

Shared by build_tmlr.py and build_jmlr.py. It lives in its own module because
the rule is no longer a one-liner: most sites take ``\\citep``, but a handful
take ``\\citealp`` or ``\\citet``, and which one is right depends on the
sentence rather than on the key. ``parisi2014ranking`` is the proof: it wants
``\\citep`` where it attributes a noun phrase ("spectral meta-learners") and
``\\citet`` where it is the object of a preposition ("the ambiguity of ...").
Duplicating that across two build scripts would guarantee they drift.

Every special case is matched on its surrounding text and asserted, so a
reworded sentence fails the build instead of silently reverting to ``\\citep``.
"""

from __future__ import annotations

import re

# Three sites used to sit inside parentheses the author had already written,
# which \citep renders as bracket-inside-bracket. \citealp fixes the brackets
# but leaves the citation running into the surrounding list with no delimiter
# at all ("verbalized Tian et al., 2023; Xiong et al., 2024, derived from..."),
# which is no easier to read. Both sentences were reworded instead so nothing
# is nested and plain \citep is correct; nothing is needed here.
CITEALP_SITES: list[tuple[str, str]] = []

# The citation is the object of a preposition, so it has to read as a noun:
# "the ambiguity of Parisi et al. (2014)", not "the ambiguity of (Parisi ...)".
CITET_SITES = [
    (r"the two-root ambiguity of \cite{parisi2014ranking}",
     r"the two-root ambiguity of \citet{parisi2014ranking}"),
]


def convert_citations(s: str) -> str:
    """Rewrite every ``\\cite`` in ``s`` to the right author-year command."""
    # An abbreviation already occupies the parentheses: fold the citation in.
    s = re.sub(r"\((\\SC|CISC)\)\s*\\cite\{([^}]*)\}",
               lambda m: f"({m.group(1)}; \\citealp{{{m.group(2)}}})", s)

    for old, new in CITEALP_SITES + CITET_SITES:
        if old not in s:
            raise AssertionError(
                f"citation site no longer present, so its command would "
                f"silently fall back to \\citep:\n  {old}")
        s = s.replace(old, new)

    # Everything else is a parenthetical attribution to a preceding noun
    # phrase, which is what \citep is for.
    s = s.replace(r"\cite{", r"\citep{")
    return s
