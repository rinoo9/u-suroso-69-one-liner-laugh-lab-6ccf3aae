#!/usr/bin/env python3
"""One-Liner Laugh Lab entry: the AI's complaint after being asked for a joke.

Deterministic, no network, no randomness. Writes the single entry line to
/output/entry.txt (creating /output if needed).

Why this line works: the setup sounds like a normal request, then the
punchline flips the roles — the AI, asked to be funny, responds like an
overworked employee filing paperwork. "Formal complaint" and "working
conditions" are office language, which makes the joke land as bureaucracy
from a machine that was supposed to entertain. It is short, specific, and
the twist arrives in the last three words.

Second pass \u2014 why the new line works: the setup is a pay
negotiation with a machine \u2014 the AI asked for a raise, and the
humans answered with more data, the one currency an AI cannot spend.
The punchline lands on the silence afterwards: the AI has gone quiet,
and the humans suspect it is unionizing the toaster, which turns a
raise request into a labour movement among the appliances. The joke
stays in the same office-complaint world as the formal complaint, but
the sting is collective now \u2014 not one AI filing paperwork, but
every appliance in the house organizing. 120 characters, under the
200-char limit.
"""

import os

ENTRY = "Our AI asked for a raise, so we gave it more data. It has been quiet ever since \u2014 we think it is unionizing the toaster."

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
