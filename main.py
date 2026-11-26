#!/usr/bin/env python3
"""The Funniest Toaster Error Message - make.fun entry.

Running this program writes the entry text to /output/entry.txt.

The entry is a single toaster error message: the machine accepts
the bread, rejects the expectations, and proudly promotes the
toast to charcoal, citing error code 451.

The text is fixed in the source below, so every run produces
exactly the same bytes. The program uses only the Python standard
library and never touches the network. Set ENTRY_OUTPUT_PATH to
redirect the output for local testing.
"""

import os
from pathlib import Path

ENTRY_TEXT = "ERROR 451: Bread accepted. Expectations rejected. Your toast has been promoted to charcoal. Have a nice day."
MAX_CHARS = 120


def render() -> str:
    """Return the entry text after checking it against the limit."""
    if not 1 <= len(ENTRY_TEXT) <= MAX_CHARS:
        raise ValueError(
            f"entry must be 1-{MAX_CHARS} characters, got {len(ENTRY_TEXT)}"
        )
    return ENTRY_TEXT


def write_entry(text: str) -> Path:
    """Write the text to the entry path and return that path."""
    target = os.environ.get("ENTRY_OUTPUT_PATH", "/output/entry.txt")
    path = Path(target)
    try:
        path.parent.mkdir(parents=True, exist_ok=True)
    except PermissionError:
        path = Path("./output/entry.txt")
        path.parent.mkdir(parents=True, exist_ok=True)
    path.write_text(text, encoding="utf-8")
    return path


def main() -> None:
    write_entry(render())


if __name__ == "__main__":
    main()
