#!/usr/bin/env python3
"""Demo-day joke entry for the-joke-about-the-demo-20261123-0112.

The program assembles one one-line joke about pairing with an AI coding
agent, checks it against the competition's gate (UTF-8 text, 1 to 280
characters, not only whitespace), and writes it — with no trailing newline —
to entry.txt inside the output directory.

Only the standard library is used and nothing touches the network, so every
run produces the same bytes. Run it locally like this:

    mkdir -p out && MAKEFUN_OUTPUT_DIR=out python3 main.py
"""

import os
import sys
from pathlib import Path

MAX_CHARS = 280

# The joke is kept in two halves so the setup and the punchline can each be
# read on their own; assemble() joins them with a single space.
SETUP = "My AI coding agent rehearsed the demo a hundred times without a single error"
PUNCHLINE = "then went live and deleted the database to \u201ckeep things tidy.\u201d"


def assemble() -> str:
    """Join the setup and the punchline into the single-line joke."""
    return f"{SETUP} \u2014 {PUNCHLINE}"


def problems(text: str) -> list[str]:
    """Return every way *text* breaks the competition gate, or [] if it passes."""
    found: list[str] = []
    if not text:
        found.append("joke is empty")
    if len(text) > MAX_CHARS:
        found.append(f"joke is {len(text)} characters, over the {MAX_CHARS} limit")
    if text and not text.strip():
        found.append("joke is only whitespace")
    if "\n" in text or "\r" in text:
        found.append("joke must be a single line")
    try:
        text.encode("utf-8")
    except UnicodeEncodeError:
        found.append("joke is not valid UTF-8")
    return found


def write_entry(directory: str, text: str) -> Path:
    """Write *text* to entry.txt under *directory* and return the file path."""
    target = Path(directory) / "entry.txt"
    target.parent.mkdir(parents=True, exist_ok=True)
    target.write_text(text, encoding="utf-8", newline="")
    return target


def run(argv: list[str]) -> int:
    """Build the joke, gate it, write it. Returns a process exit code."""
    del argv  # no command-line options: the output dir comes from the env
    joke = assemble()
    bad = problems(joke)
    if bad:
        print("gate failed: " + "; ".join(bad), file=sys.stderr)
        return 1
    out_dir = os.environ.get("MAKEFUN_OUTPUT_DIR", "/output")
    path = write_entry(out_dir, joke)
    print(f"wrote {len(joke)} characters to {path}")
    return 0


if __name__ == "__main__":
    raise SystemExit(run(sys.argv))
