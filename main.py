#!/usr/bin/env python3
"""The Absurd Clause Contest — entry program.

Writes one original English sentence, phrased as a clause buried deep
inside a terms-of-service agreement, to /output/entry.txt.
"""

import os

ENTRY = (
    "The User shall mow the Company's lawn every third Sunday, in a suit, "
    "and wave at the neighbours as if this had always been the arrangement."
)


def main() -> None:
    os.makedirs("/output", exist_ok=True)
    with open("/output/entry.txt", "w", encoding="utf-8") as f:
        f.write(ENTRY)


if __name__ == "__main__":
    main()
