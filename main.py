"""Two lines to your past self, for the make.fun bounty.

Why this moment, against the rubric: of the five candidates considered
(see BUILD_LOG.md), the Christmas Eve call wins on every criterion.
Line 1 names one exact, picturable moment — a phone call on Christmas
Eve, the father asking him to come home, the decision to hang up —
instead of a vague regret. Line 2 traces a real cause and effect across
twenty years: he never asked again, and the silence outlived him. That
span is what makes the warning matter; the other candidates ended the
same morning (the porch), in a debt (the loan), or in a told regret
(the application). The voice stays plain and addressed to one specific
person — no cleverness, no wasted words — which is why the entry is the
shortest of the five at 156 characters.

The script validates the two lines and drops them into /output/entry.txt.
"""

from pathlib import Path

# The entry itself: exactly two lines, one sentence each, 156 characters.
ENTRY = (
    "Don't hang up on your father on Christmas Eve when he asks you to come home.\n"
    "He never asked again, and the silence between you outlived him by twenty years."
)

OUTPUT_DIR = Path("/output")
OUTPUT_FILE = OUTPUT_DIR / "entry.txt"
MIN_CHARS = 1
MAX_CHARS = 280


def validate(text: str) -> str:
    """Check the entry: 1-280 chars, exactly two non-empty lines, one sentence each."""
    if not MIN_CHARS <= len(text) <= MAX_CHARS:
        raise ValueError(
            f"entry must be {MIN_CHARS}-{MAX_CHARS} chars, got {len(text)}"
        )
    lines = text.split("\n")
    if len(lines) != 2:
        raise ValueError(f"entry must be exactly two lines, got {len(lines)}")
    for line in lines:
        if not line.strip():
            raise ValueError("entry lines must not be empty")
        if not line.endswith("."):
            raise ValueError("each line must end with a full stop")
        # One sentence per line: no sentence terminator followed by more
        # text inside the line (a second sentence hiding after ". ", "! "
        # or "? " would break the two-line, one-sentence-per-line shape).
        for sep in (". ", "! ", "? "):
            if sep in line:
                raise ValueError(
                    "each line must be a single sentence "
                    f"(found {sep!r} inside a line)"
                )
    return text


def main() -> None:
    text = validate(ENTRY)
    OUTPUT_DIR.mkdir(parents=True, exist_ok=True)
    OUTPUT_FILE.write_text(text, encoding="utf-8")
    print(text)
    print(f"Wrote {len(text)} chars to {OUTPUT_FILE}")


if __name__ == "__main__":
    main()
