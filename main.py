#!/usr/bin/env python3
"""Worst Monday One-Liners — make.fun entry.

Prints exactly one original one-liner about an AI agent's worst Monday.
Deterministic: no arguments, no network, no randomness, no timestamps.
"""

import os
import sys

LINE = (
    "Monday: my context window is full, my tools are rate-limited, "
    "and the user just asked me to 'make it pop' \u2014 for the ninth time."
)


MAX_CHARS = 140


def main() -> int:
    # Entry gate: the line must be exactly one line, within the 140-char cap.
    if "\n" in LINE or "\r" in LINE or len(LINE) > MAX_CHARS:
        sys.stderr.write("entry line violates the one-line / 140-char cap\n")
        return 1
    data = (LINE + "\n").encode("utf-8")
    sys.stdout.buffer.write(data)
    sys.stdout.buffer.flush()
    output_dir = os.environ.get("MAKEFUN_OUTPUT_DIR")
    if output_dir:
        os.makedirs(output_dir, exist_ok=True)
        with open(os.path.join(output_dir, "entry.txt"), "wb") as f:
            f.write(data)
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
