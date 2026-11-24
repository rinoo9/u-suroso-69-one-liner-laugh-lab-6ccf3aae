#!/usr/bin/env python3
"""One-Liner Laugh Lab entry: the robot vacuum's excuse after eating a sock.

Deterministic, no network, no randomness. Writes the single entry line to
/output/entry.txt (creating /output if needed).
"""

import os

ENTRY = "In my defence, the sock was on the floor, it smelled of feet, and my job description literally says 'eat the floor'."

def main():
    line = ENTRY
    assert 1 <= len(line) <= 200, f"entry must be 1-200 chars, got {len(line)}"
    assert "\n" not in line and "\r" not in line, "entry must be a single line"
    assert line == line.strip(), "entry must have no leading/trailing whitespace"
    os.makedirs("/output", exist_ok=True)
    # No trailing newline: the gate counts every character in entry.txt.
    with open("/output/entry.txt", "w", encoding="utf-8") as f:
        f.write(line)

if __name__ == "__main__":
    main()
