"""Sandboxed execution of model-generated code.

Candidate solutions come from an LLM and are executed to grade them. Two real
risks are handled: non-termination (competitive-programming code loops on bad
inputs routinely) and resource exhaustion. Each execution runs in a separate
process with a wall-clock timeout, a CPU-time limit, and an address-space cap,
in a scratch working directory.

This is containment for accidents, not a security boundary against deliberately
hostile code. Only run this on code you generated yourself from a benchmark.
"""

from __future__ import annotations

import json
import subprocess
import sys
import tempfile
from pathlib import Path

#: Prelude installed inside the child process before any candidate code runs.
#: Each limit is applied independently and never above the inherited hard
#: limit -- macOS refuses RLIMIT_AS outright in some configurations, and a
#: failure to set one limit must not disable the others (or the whole harness).
_LIMITS = """
import resource, sys
for _name, _val in (("RLIMIT_CPU", {cpu}), ("RLIMIT_AS", {mem}), ("RLIMIT_NPROC", 64)):
    _r = getattr(resource, _name, None)
    if _r is None:
        continue
    try:
        _soft, _hard = resource.getrlimit(_r)
        _want = _val if _hard == resource.RLIM_INFINITY else min(_val, _hard)
        resource.setrlimit(_r, (_want, _hard))
    except (ValueError, OSError):
        pass
sys.setrecursionlimit(20000)
"""


def run_script(body: str, timeout: float = 12.0, cpu: int = 10,
               mem_mb: int = 2048) -> tuple[bool, str]:
    """Run ``body`` in a limited subprocess. Returns (ok, stdout-or-error)."""
    script = _LIMITS.format(cpu=cpu, mem=mem_mb * 1024 * 1024) + body
    with tempfile.TemporaryDirectory() as td:
        f = Path(td) / "run.py"
        f.write_text(script)
        try:
            p = subprocess.run([sys.executable, str(f)], capture_output=True,
                               text=True, timeout=timeout, cwd=td)
        except subprocess.TimeoutExpired:
            return False, "__TIMEOUT__"
        except Exception as e:  # pragma: no cover - environment failure
            return False, f"__SPAWN_ERROR__ {e}"
        if p.returncode != 0:
            return False, (p.stderr or "")[-400:]
        return True, p.stdout


def grade_candidate(preamble: str, code: str, test_src: str, entry_point: str,
                    timeout: float = 12.0) -> bool:
    """Does ``code`` pass the benchmark's hidden ``check(candidate)`` suite?"""
    body = (
        f"{preamble}\n\n{code}\n\n{test_src}\n\n"
        f"check({entry_point})\nprint('__PASS__')\n"
    )
    ok, out = run_script(body, timeout=timeout)
    return bool(ok and "__PASS__" in out)


def fingerprint(preamble: str, code: str, entry_point: str, inputs: list[str],
                timeout: float = 12.0) -> list[str]:
    """Behavioural fingerprint: the candidate's output on each probe input.

    Label-free -- only the INPUTS from the benchmark are used, never the
    expected outputs. Errors and timeouts become distinct fingerprint values,
    which is correct: they are observable behaviour that separates candidates.
    """
    calls = "\n".join(
        f"try:\n"
        f"    __r = {entry_point}({inp})\n"
        f"    __o.append(repr(__r))\n"
        f"except Exception as __e:\n"
        f"    __o.append('ERR:' + type(__e).__name__)\n"
        for inp in inputs
    )
    body = f"{preamble}\n\n{code}\n\n__o = []\n{calls}\nimport json; print(json.dumps(__o))\n"
    ok, out = run_script(body, timeout=timeout)
    if not ok:
        return ["__DEAD__"] * len(inputs)
    try:
        vals = json.loads(out.strip().splitlines()[-1])
        return vals if len(vals) == len(inputs) else ["__DEAD__"] * len(inputs)
    except Exception:
        return ["__DEAD__"] * len(inputs)
