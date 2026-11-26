#!/usr/bin/env python3
"""Entry for make.fun: The Funniest Toaster Error.

The entry is a single toaster error message, written the way a
household appliance with a legal department would phrase it.
The machine happily accepts the bread, rejects the very idea
of expectations, and proudly promotes the toast to charcoal,
citing error code 451, which in this kitchen is the temperature
at which breakfast becomes a fire-safety announcement and
the smoke alarm joins the conversation uninvited.

Running this program writes the entry to /output/entry.txt,
falling back to ./output/entry.txt when /output is not
writable, and prints it to stdout as well.
"""

from pathlib import Path

ENTRY_TEXT = (
    "ERROR 451: Bread accepted, expectations rejected. "
    "Your toast has been promoted to charcoal."
)

# The toaster reports problems the way old printers did: a short
# code, a colon, and then far more honesty than the user wanted.
ERROR_CODE = 451


def render_entry() -> str:
    """Return the entry text exactly as the toaster displays it."""
    return ENTRY_TEXT


def check_length(text: str) -> bool:
    """Confirm the message stays within the competition limit."""
    return len(text) < 120


def write_entry(text: str) -> Path:
    """Write the entry text to the output file and return its path."""
    out_dir = Path("/output")
    try:
        out_dir.mkdir(parents=True, exist_ok=True)
        target = out_dir / "entry.txt"
        target.write_text(text + "\n", encoding="utf-8")
        return target
    except OSError:
        out_dir = Path("output")
        out_dir.mkdir(parents=True, exist_ok=True)
        target = out_dir / "entry.txt"
        target.write_text(text + "\n", encoding="utf-8")
        return target


def main() -> None:
    text = render_entry()
    assert check_length(text), "entry exceeds the character limit"
    write_entry(text)
    print(text)


if __name__ == "__main__":
    main()
