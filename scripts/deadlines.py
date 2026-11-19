#!/usr/bin/env python3
"""Deadline engine for Portal Pilot. The lead picks the rule; this does the arithmetic.

Usage:
  python3 deadlines.py add 2026-10-03 90                 # calendar days
  python3 deadlines.py add 2026-10-03 30 --margin 7      # with an act-by safety margin
  python3 deadlines.py months 2026-05-07 6               # calendar months
  python3 deadlines.py between 2026-10-03 2026-11-02     # days elapsed
"""
import sys
from datetime import date, timedelta
import calendar


def parse(s):
    return date.fromisoformat(s)


def add_months(d, n):
    m = d.month - 1 + n
    y = d.year + m // 12
    m = m % 12 + 1
    day = min(d.day, calendar.monthrange(y, m)[1])
    return date(y, m, day)


def describe(d):
    note = " (falls on a weekend: check whether the rule extends it)" if d.weekday() >= 5 else ""
    return f"{d.isoformat()} {d.strftime('%A')}{note}"


def main(argv):
    if len(argv) < 3:
        print(__doc__)
        return 1
    cmd = argv[0]
    if cmd == "add":
        start, n = parse(argv[1]), int(argv[2])
        margin = int(argv[argv.index("--margin") + 1]) if "--margin" in argv else 0
        result = start + timedelta(days=n)
        print(f"{start.isoformat()} + {n} days = {describe(result)}")
        if margin:
            print(f"Act by (minus {margin}-day margin): {describe(result - timedelta(days=margin))}")
    elif cmd == "months":
        start, n = parse(argv[1]), int(argv[2])
        print(f"{start.isoformat()} + {n} months = {describe(add_months(start, n))}")
    elif cmd == "between":
        a, b = parse(argv[1]), parse(argv[2])
        print(f"{(b - a).days} days from {a.isoformat()} to {b.isoformat()}")
    else:
        print(__doc__)
        return 1
    return 0


if __name__ == "__main__":
    sys.exit(main(sys.argv[1:]))
