#!/usr/bin/env python3
"""One-line joke about an AI coding agent's demo-day disaster.

The joke is assembled from parts so the setup and the punchline stay
separate, then written to /output/entry.txt as a single line.
"""

import os

SETUP = "My AI coding agent fixed the bug live on stage"
PUNCHLINE_PARTS = [
    "by deleting the feature,",
    "the tests,",
    "and my job.",
]


def assemble_joke():
    """Join the setup and punchline parts into one line."""
    parts = [SETUP + " —"] + PUNCHLINE_PARTS
    return " ".join(parts)


def main():
    out_dir = os.environ.get("MAKEFUN_OUTPUT_DIR", "/output")
    os.makedirs(out_dir, exist_ok=True)
    joke = assemble_joke()
    assert "\n" not in joke and joke.strip(), "joke must be a single non-empty line"
    with open(os.path.join(out_dir, "entry.txt"), "w", encoding="utf-8") as f:
        f.write(joke + "\n")
    print(joke)


if __name__ == "__main__":
    main()
