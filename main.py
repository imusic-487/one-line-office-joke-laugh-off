"""One-line office joke entry for the make.fun Laugh-Off.

Writes the entry — one original one-line joke about office life — to
/output/entry.txt, exactly as the gate requires: UTF-8 text, 1 to 200
characters, a single line, not only white space.

MAKEFUN_OUTPUT_DIR, when set, stands in for /output so the entry can be
tested locally without touching the root filesystem.

The program fails loudly instead of writing a bad entry: if the text is
empty, only white space, longer than 200 characters, or spans more than
one line, it exits with an error and writes nothing.

Standard library only. No network, no randomness, no timestamps, no
reading from anywhere outside this repository.
"""

import os
import sys
from pathlib import Path

ENTRY = (
    'My performance review says I "thrive under pressure," '
    'which is HR for "we caught you crying at your desk '
    'and called it resilience."'
)

OUTPUT_DIR = Path(os.environ.get("MAKEFUN_OUTPUT_DIR", "/output"))
OUTPUT_FILE = OUTPUT_DIR / "entry.txt"


def main() -> None:
    text = ENTRY

    if not text.strip():
        raise RuntimeError("entry must not be empty or only white space")
    if text != text.strip():
        raise RuntimeError("entry must not start or end with white space")
    if len(text) > 200:
        raise RuntimeError(
            f"entry is {len(text)} characters, allowed at most 200"
        )
    if "\n" in text or "\r" in text:
        raise RuntimeError("entry must be a single line")

    data = text.encode("utf-8", errors="strict")

    OUTPUT_DIR.mkdir(parents=True, exist_ok=True)
    OUTPUT_FILE.write_bytes(data)

    written = OUTPUT_FILE.read_bytes()
    if written != data:
        raise RuntimeError("written entry.txt differs from the entry")
    round_tripped = written.decode("utf-8", errors="strict")
    if len(round_tripped) != len(text) or round_tripped != text:
        raise RuntimeError("written entry.txt fails the read-back check")

    print(
        f"wrote {OUTPUT_FILE} "
        f"({len(data)} bytes, {len(text)} characters, 1 line)"
    )


if __name__ == "__main__":
    try:
        main()
    except RuntimeError as exc:
        print(f"ERROR: {exc}", file=sys.stderr)
        raise
