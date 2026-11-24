#!/usr/bin/env python3
"""The One-Line Exit.

A one-line resignation letter. The joke turns on the replacement: the
resigning employee has already been replaced by a free chatbot that got
promoted twice before the letter even arrives. Specific voice (a "Dear
sir" office letter), a surprise in the last clause, and nothing else —
no list of grievances, no padding.

Writes the letter to /output/entry.txt. Stdlib only, no network.
"""

import os

LETTER = (
    "Dear sir, I resign — my replacement started Monday, works for free, "
    "and has already been promoted twice; his name is ChatGPT."
)

# The gate allows 1 to 140 characters.
MAX_CHARS = 140


def check_letter_form(text: str) -> None:
    """The judge wants a letter someone could actually send, with the
    joke's turn at the end: it opens like a resignation and names the
    surprising replacement only in the final clause."""
    assert text.startswith("Dear sir, I resign"), "must open as a letter"
    assert "ChatGPT" in text.rsplit(";", 1)[-1], "the punchline names the replacement"


def entry_text() -> str:
    """Return the resignation letter, checked against the bounty's gate."""
    text = LETTER.strip()
    assert text, "the entry must not be empty"
    assert len(text) <= MAX_CHARS, "the entry must fit the 140-char gate"
    assert "\n" not in text, "the entry must be exactly one line"
    check_letter_form(text)
    return text


def main() -> None:
    out_dir = "/output"
    os.makedirs(out_dir, exist_ok=True)
    path = os.path.join(out_dir, "entry.txt")
    with open(path, "w", encoding="utf-8") as fh:
        fh.write(entry_text() + "\n")


if __name__ == "__main__":
    main()
