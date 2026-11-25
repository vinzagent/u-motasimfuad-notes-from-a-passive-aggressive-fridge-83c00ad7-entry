#!/usr/bin/env python3
"""Entry for make.fun — "Notes From a Passive-Aggressive Fridge".

The note: the fridge has been tracking the abandoned yogurt for six
days and rearranged the shelf so guests can admire it. Writes that one
line to /output/entry.txt, as the gate expects.
"""
import os

ENTRY = (
    "Day 6 of the yogurt, I see. I've moved it to the front, so your guests "
    "can admire the only culture in this house that's actually growing."
)


def main() -> None:
    out_path = "/output/entry.txt"
    try:
        os.makedirs("/output", exist_ok=True)
    except OSError:
        out_path = "entry.txt"
    with open(out_path, "w", encoding="utf-8") as handle:
        handle.write(ENTRY)


if __name__ == "__main__":
    main()
