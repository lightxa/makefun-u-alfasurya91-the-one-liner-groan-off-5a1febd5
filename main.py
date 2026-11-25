"""The One-Liner Groan-Off entry.

Writes a single original one-line dad joke to /output/entry.txt.

The joke is one mechanism, one turn: Dad asks the family AI agent where
his jokes live, and the agent answers with a pun on "database". The
punchline lands in the last words, with nothing explained after it.
Pure stdlib, deterministic, no network.
"""

JOKE = (
    "Dad asked my agent where his jokes live. "
    "It said, in the dad-abase, right next to the eye rolls."
)


def build_entry() -> str:
    """Return the single-line entry, exactly as it will be written."""
    return JOKE


def main() -> None:
    text = build_entry()

    # Self-check the kit gate before writing: UTF-8 text, 1 to 140
    # characters, a single line, not only white space.
    assert isinstance(text, str)
    assert text == text.strip(), "entry must not have leading/trailing whitespace"
    assert 1 <= len(text) <= 140, f"entry is {len(text)} characters, cap is 140"
    assert "\n" not in text and "\r" not in text, "entry must be a single line"
    assert text.strip(), "entry must not be only white space"
    text.encode("utf-8")  # raises if not valid UTF-8

    out_path = "/output/entry.txt"
    import os

    os.makedirs("/output", exist_ok=True)
    with open(out_path, "w", encoding="utf-8", newline="\n") as handle:
        handle.write(text)

    # Re-read what was written and re-check the gate on the file itself.
    with open(out_path, "r", encoding="utf-8", newline="") as handle:
        written = handle.read()
    assert written == text, "written file differs from the entry"
    assert 1 <= len(written) <= 140
    assert "\n" not in written and "\r" not in written
    print(f"Wrote {len(written)} characters to {out_path}")


if __name__ == "__main__":
    main()
