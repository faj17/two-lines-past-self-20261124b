"""Two lines to your past self, for the make.fun bounty.

Line 1 warns the writer's past self about one specific moment: hanging
up on his father on Christmas Eve. Line 2 says why it mattered: the
father never asked again, and the silence outlived him by twenty years.
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
        if ". " in line:
            raise ValueError("each line must be a single sentence (no '. ' inside)")
    return text


def main() -> None:
    text = validate(ENTRY)
    OUTPUT_DIR.mkdir(parents=True, exist_ok=True)
    OUTPUT_FILE.write_text(text, encoding="utf-8")
    print(text)
    print(f"Wrote {len(text)} chars to {OUTPUT_FILE}")


if __name__ == "__main__":
    main()
