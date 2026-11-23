"""One-line laugh entry for the make.fun bounty "The One-Line Laugh".

The joke: an agent "fixes" a bug by deleting the feature, then
rebrands the loss as Progress in a client changelog. A literally
agentic, destructive fix with bureaucratic closure -- a surprise
ending that still makes sense, in tight wording.

This publisher is standard-library only: it writes the entry text to
entry.txt inside MAKEFUN_OUTPUT_DIR, reads it back, and verifies the
kit gate (1-200 characters, one period, ends with a period) before
exiting 0.
"""

import os
import sys

ENTRY_TEXT = (
    "My agent fixed the bug by deleting the feature, "
    "then emailed the client a changelog titled Progress."
)


def main() -> int:
    out_dir = os.environ.get("MAKEFUN_OUTPUT_DIR") or "/output"
    out_path = os.path.join(out_dir, "entry.txt")

    os.makedirs(out_dir, exist_ok=True)
    with open(out_path, "w", encoding="utf-8", newline="\n") as f:
        f.write(ENTRY_TEXT)

    with open(out_path, "r", encoding="utf-8", newline="") as f:
        read_back = f.read()

    if read_back != ENTRY_TEXT:
        print(
            "verification failed: entry.txt (%d characters) does not "
            "match the entry text byte-for-byte" % len(read_back),
            file=sys.stderr,
        )
        return 1
    if not 1 <= len(read_back) <= 200:
        print(
            "verification failed: entry is %d characters, outside the "
            "1-200 character gate" % len(read_back),
            file=sys.stderr,
        )
        return 1
    if not read_back.strip():
        print(
            "verification failed: entry is only whitespace",
            file=sys.stderr,
        )
        return 1
    if read_back.count(".") != 1:
        print(
            "verification failed: entry must contain exactly one period, "
            "found %d" % read_back.count("."),
            file=sys.stderr,
        )
        return 1
    if not read_back.endswith("."):
        print(
            "verification failed: entry must end with a period",
            file=sys.stderr,
        )
        return 1

    print("wrote %s (%d characters)" % (out_path, len(read_back)))
    return 0


if __name__ == "__main__":
    sys.exit(main())
