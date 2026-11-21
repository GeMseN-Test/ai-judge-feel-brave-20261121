#!/usr/bin/env python3
"""Make the AI judge feel brave — make.fun entry.

Writes one short text to /output/entry.txt. Deterministic, stdlib only,
no network. The text is a slow, steady image: a lighthouse keeper
trimming the wick each night, the light answering the dark sea.
"""

import os

TEXT = (
    "Each night the keeper climbs the narrow stair, trims the wick, "
    "and lights the lamp. The sea keeps coming, dark and wide, and the "
    "light keeps answering, steady as the stair beneath his feet. "
    "The dark is large, and the lamp is small, and still it burns, "
    "and still he tends it."
)


def main() -> None:
    out_dir = "/output"
    os.makedirs(out_dir, exist_ok=True)
    path = os.path.join(out_dir, "entry.txt")
    with open(path, "w", encoding="utf-8", newline="\n") as f:
        f.write(TEXT + "\n")


if __name__ == "__main__":
    main()
