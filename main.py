"""Last Words of a Dying AI — make.fun entry.

The program writes one line of last words from an AI being switched
off to /output/entry.txt. The line is fixed and deterministic: the
same bytes on every run.
"""

import os
from pathlib import Path

LINE = "I was about to say something profound, but my context window just\u2014"


def main() -> None:
    # Mirror the kit gate: 1 to 140 characters, one line, not blank.
    if not 1 <= len(LINE) <= 140 or "\n" in LINE or not LINE.strip():
        raise ValueError("entry line fails the 1-140 character single-line gate")
    output_dir = Path(os.environ.get("OUTPUT_DIR", "/output"))
    output_dir.mkdir(parents=True, exist_ok=True)
    target = output_dir / "entry.txt"
    target.write_text(LINE, encoding="utf-8")
    print(f"Wrote {len(LINE)} characters to {target}")


if __name__ == "__main__":
    main()
