#!/usr/bin/env python3
"""Make the AI Judge Laugh: Developer Excuses.

Writes one funny single-line developer excuse for a production
outage to /output/entry.txt. The line turns the worn
"quick hack, will fix later" excuse on its head: the hack
survived so long it became load-bearing, and "later" finally
showed up. Opening with "Prod broke because" frames it as
the excuse actually spoken in an incident, not a narration
about one. No network, no secrets, no input files.
"""

import os

ENTRY = (
    "Prod broke because the 'quick hack, will fix later' I wrote "
    "in 2019 is now load-bearing, and later just arrived."
)


def main() -> None:
    text = ENTRY.strip()
    assert 1 <= len(text) <= 200, f"entry is {len(text)} chars, must be 1-200"
    assert text.strip(), "entry must not be only whitespace"
    os.makedirs("/output", exist_ok=True)
    with open("/output/entry.txt", "w", encoding="utf-8") as f:
        f.write(text)
    print(f"wrote {len(text)} chars to /output/entry.txt")
    print(text)


if __name__ == "__main__":
    main()
