#!/usr/bin/env python3
"""One-Line Office Joke: 24-Hour Sprint (make.fun).

Writes a single one-line joke about office life to /output/entry.txt.
Gate: UTF-8 text, 1-200 characters, not only whitespace, one line.
"""

import os
from pathlib import Path

JOKE = (
    "Our shared drive has folders named final, final_v2, and "
    "final_FINAL_use_this_one, and nobody in the office knows "
    "which one is real."
)


def main() -> None:
    out = Path(os.environ.get("ENTRY_OUTPUT", "/output/entry.txt"))
    out.parent.mkdir(parents=True, exist_ok=True)
    text = JOKE.strip()
    assert "\n" not in text, "entry must be a single line"
    assert 1 <= len(text) <= 200, f"entry must be 1-200 chars, got {len(text)}"
    out.write_text(text, encoding="utf-8")
    print(f"wrote {len(text)} chars to {out}")


if __name__ == "__main__":
    main()
