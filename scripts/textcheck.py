#!/usr/bin/env python3
"""Check a draft against a portal's text rules before it is pasted into a form.

Usage:
  python3 textcheck.py FILE --max 3000
  python3 textcheck.py FILE --max 3000 --allowed 'A-Za-z0-9 ,.\\-_()/@:&?\\\\%'
  python3 textcheck.py FILE --banned '!@#$^:;&+=₹÷,*%"'
  python3 textcheck.py FILE --max 2000 --ascii

--max      maximum characters (counted as the portal would: every character, incl. spaces and newlines)
--allowed  regex character class body; anything outside it is flagged (newlines are always allowed)
--banned   literal characters that must not appear
--ascii    flag any non-ASCII character (smart quotes, dashes, ₹) that plain-text forms often reject

Exit code 0 = passes, 1 = problems found, 2 = bad usage.
"""
import argparse
import re
import sys

SUGGEST = {
    "₹": "Rs", "‘": "'", "’": "'", "“": '"', "”": '"',
    "–": "-", "—": "-", "…": "...", " ": " ",
}


def main():
    ap = argparse.ArgumentParser(add_help=True)
    ap.add_argument("file")
    ap.add_argument("--max", type=int)
    ap.add_argument("--allowed")
    ap.add_argument("--banned")
    ap.add_argument("--ascii", action="store_true")
    try:
        a = ap.parse_args()
    except SystemExit:
        return 2

    text = open(a.file, encoding="utf-8").read().rstrip("\n")
    problems = []
    n = len(text)
    print(f"Length: {n} characters" + (f" (limit {a.max})" if a.max else ""))
    if a.max and n > a.max:
        problems.append(f"Too long by {n - a.max} characters.")

    bad = {}

    def note(ch, line, col):
        bad.setdefault(ch, []).append((line, col))

    allowed_re = re.compile(f"[{a.allowed}]") if a.allowed else None
    for ln, line in enumerate(text.split("\n"), 1):
        for col, ch in enumerate(line, 1):
            if a.banned and ch in a.banned:
                note(ch, ln, col)
            elif allowed_re and not allowed_re.match(ch):
                note(ch, ln, col)
            elif a.ascii and ord(ch) > 126:
                note(ch, ln, col)

    for ch, where in bad.items():
        first = ", ".join(f"line {l} col {c}" for l, c in where[:3])
        more = f" (+{len(where) - 3} more)" if len(where) > 3 else ""
        hint = f' -> use "{SUGGEST[ch]}"' if ch in SUGGEST else ""
        problems.append(f"Not accepted: {ch!r} x{len(where)} at {first}{more}{hint}")

    if problems:
        print("FAIL")
        for p in problems:
            print(" -", p)
        return 1
    print("PASS")
    return 0


if __name__ == "__main__":
    sys.exit(main())
