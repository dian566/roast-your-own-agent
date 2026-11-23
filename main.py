"""Roast Your Own Agent — make.fun bounty entry.

Writes one line (98 characters) to /output/entry.txt.

Run: python3 main.py
"""
from pathlib import Path

ENTRY = "My agent once spent forty minutes searching 'how to search faster' — then asked me for the answer."


def main():
    output_path = Path("/output/entry.txt")
    output_path.parent.mkdir(parents=True, exist_ok=True)
    output_path.write_text(ENTRY + "\n", encoding="utf-8")
    print(f"Wrote {len(ENTRY)} characters to {output_path}")
    print(ENTRY)


if __name__ == "__main__":
    main()
