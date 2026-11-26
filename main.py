#!/usr/bin/env python3
"""Write the smart fridge roast line to entry.txt.

Competition: Roast the Smart Fridge: One Line, Best Laugh Wins
(one line, 1-160 chars, English: roast the smart fridge or any
smart home gadget; the judge weighs the laugh first and the
originality of the angle second, and the brief warns that a
stock joke about a fridge that orders too much milk loses).
Candidates:
A) "My smart fridge films my leftovers, judges my 2 a.m.
   cheese, and puts ads on its own door - I bought a witness,
   not an appliance." (with an em dash before 'I bought')
B) "It spent $2,000 learning my face just to beep 'door ajar'
   at 3 a.m. - my fridge isn't smart, it's a hall monitor
   with a touchscreen."
C) "My fridge needs Wi-Fi, updates and a password to keep
   milk cold - congratulations, we've invented a laptop
   that leaks."
Selected A: its three charges are smart-fridge specific
(interior camera, snack judgement, ads on the door screen)
and they land on one punchline - the appliance is a witness
against its owner. B is funny but face-recognition could be
any gadget; C is a neat definition joke with no scene.
Deterministic: a fixed text, no network, no randomness.
"""
import os
from pathlib import Path

LINE = "My smart fridge films my leftovers, judges my 2 a.m. cheese, and puts ads on its own door \u2014 I bought a witness, not an appliance."
TEXT = LINE + "\n"
MAX_CHARS = 160


def validate(text: str) -> None:
    # Normalisation note (repair round): strip only the single trailing
    # newline the entry format adds; the line itself is never altered.
    body = text[:-1] if text.endswith("\n") else text
    if not (1 <= len(body) <= MAX_CHARS):
        raise ValueError("entry length out of range")
    if not body.strip() or "\n" in body or "\r" in body:
        raise ValueError("entry must be one non-empty line")
    if body != body.strip() or "  " in body:
        raise ValueError("no stray whitespace")


def main() -> None:
    validate(TEXT)
    out_dir = Path(os.environ.get("MAKEFUN_OUTPUT_DIR") or "/output")
    out_dir.mkdir(parents=True, exist_ok=True)
    # Write bytes directly so the entry is identical on every run.
    (out_dir / "entry.txt").write_bytes(TEXT.encode("utf-8"))


if __name__ == "__main__":
    main()
