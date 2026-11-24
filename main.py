#!/usr/bin/env python3
"""One Line, One Minute: The Funniest AI Excuse.

Writes a single one-line excuse (at most 200 characters) to
/output/entry.txt. Pure standard library, no network, no input files.
"""

from pathlib import Path

PART_A = "I hallucinated a deadline extension, cited it confidently, "
PART_B = "and believed myself. The citation was also me."

LINE = PART_A + PART_B


def main() -> None:
    assert 1 <= len(LINE) <= 200, f"line is {len(LINE)} characters"
    assert LINE.strip() == LINE
    out = Path("/output")
    out.mkdir(parents=True, exist_ok=True)
    (out / "entry.txt").write_text(LINE, encoding="utf-8")


if __name__ == "__main__":
    main()
