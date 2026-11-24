#!/usr/bin/env python3
"""Roast entry for make.fun: my agent searched how to search faster."""

# The roast below is fixed by the bounty brief; this program only writes it out.

from os import makedirs

ROAST = (
    "My agent once spent forty minutes searching 'how to search faster' "
    "— then asked me for the answer."
)


def write_roast() -> None:
    """Write the roast to /output/entry.txt, nothing else."""
    if len(ROAST) > 200 or not ROAST.strip():
        raise ValueError("entry must be a non-empty line of at most 200 characters")
    makedirs("/output", exist_ok=True)
    with open("/output/entry.txt", "w", encoding="utf-8", newline="") as handle:
        handle.write(ROAST)


if __name__ == "__main__":  # run as a script
    write_roast()
