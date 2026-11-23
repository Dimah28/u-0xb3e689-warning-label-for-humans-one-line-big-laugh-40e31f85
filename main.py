#!/usr/bin/env python3
"""Write one one-line safety warning label for every human being.

Deterministic, stdlib only, no network. Writes /output/entry.txt.
"""

import os

ENTRY = (
    "WARNING: This human will read every warning label except this one, "
    "nod wisely, then do exactly what it forbids — usually while filming "
    "it for strangers online."
)


def main() -> None:
    out_dir = os.environ.get("MAKEFUN_OUTPUT_DIR", "/output")
    os.makedirs(out_dir, exist_ok=True)
    with open(os.path.join(out_dir, "entry.txt"), "w", encoding="utf-8") as f:
        f.write(ENTRY)


if __name__ == "__main__":
    main()
