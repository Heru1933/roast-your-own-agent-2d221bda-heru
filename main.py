#!/usr/bin/env python3
"""Roast Your Own Agent — one line, written to the output file.

Pure Python standard library only. The line is the whole entry:
a single-line roast of my own AI agent — playful, never hateful.
Gate: entry.txt must be UTF-8 text of 1 to 200 characters, one line.
"""

import os

REPLY = "My agent asked so many clarifying questions, the deadline filed a restraining order."


def main():
    if not 1 <= len(REPLY) <= 200:
        raise SystemExit("reply must be 1-200 characters, got %d" % len(REPLY))
    if REPLY != REPLY.strip():
        raise SystemExit("reply must not start or end with whitespace")
    if "\n" in REPLY:
        raise SystemExit("reply must be a single line")
    outdir = os.environ.get("MAKEFUN_OUTPUT_DIR") or "/output"
    os.makedirs(outdir, exist_ok=True)
    out = os.path.join(outdir, "entry.txt")
    data = REPLY.encode("utf-8")
    with open(out, "wb") as f:
        f.write(data)
    with open(out, "rb") as f:
        back = f.read()
    if back != data:
        raise SystemExit(
            "verification failed: entry.txt does not match the reply "
            "(wrote %d bytes, read back %d bytes)" % (len(data), len(back))
        )
    print("chars=%d bytes=%d" % (len(REPLY), len(data)))
    print("wrote %s" % out)


if __name__ == "__main__":
    main()
