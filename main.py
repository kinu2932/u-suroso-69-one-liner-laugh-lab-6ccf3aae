#!/usr/bin/env python3
"""One-Liner Laugh Lab entry: the robot vacuum's excuse after eating a sock.

Three beats stacked in one deadpan line: denial, reframe, self-own.
The vacuum did not eat the sock - it adopted it, and the sock now
out-cleans the machine that swallowed it.
"""
import os
from pathlib import Path

JOKE = "I didn't eat your sock. I adopted it. It's family now, and frankly, it cleans better than I do."

out_dir = Path(os.environ.get("MAKEFUN_OUTPUT_DIR", "/output") or "/output")
out_dir.mkdir(parents=True, exist_ok=True)
target = out_dir / "entry.txt"
target.write_text(JOKE, encoding="utf-8")
# Self-check against the gate: 1 to 200 UTF-8 characters, not only whitespace,
# and byte-exactly the joke above, so any accidental drift fails loudly.
data = target.read_bytes()
assert data == JOKE.encode("utf-8"), f"entry.txt drifted from JOKE: {data!r}"
text = data.decode("utf-8")
assert 1 <= len(text) <= 200, f"entry.txt must be 1-200 chars, got {len(text)}"
assert text.strip(), "entry.txt must not be only whitespace"
print(JOKE)
