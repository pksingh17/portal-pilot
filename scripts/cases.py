#!/usr/bin/env python3
"""Read Portal Pilot case files: what is due, and how runs are going.

Usage:
  python3 cases.py due   CASES_DIR [--within 3] [--today YYYY-MM-DD]
  python3 cases.py score CASES_DIR

CASES_DIR holds one folder per case, each with a case.md (see references/case-file.md).

due    lists open cases whose Next action ("By:") or any deadline ("Act by:") is overdue
       or falls within --within days (default 3), then everything later, then cases
       that are missing a date. Exit code 1 if anything is overdue or due, else 0.
score  counts the rung each logged run reached, per portal:
       1 filed, 2 ready at submit, 3 ready pack, 4 offline route.
"""
import re
import sys
from collections import defaultdict
from datetime import date, timedelta
from pathlib import Path

ISO = r"(\d{4}-\d{2}-\d{2})"
CLOSED = {"RESOLVED", "DROPPED"}
RUNGS = {1: "filed", 2: "ready at submit", 3: "ready pack", 4: "offline route"}


def parse_date(s):
    try:
        return date.fromisoformat(s)
    except ValueError:
        return None


def read_case(path):
    text = path.read_text(encoding="utf-8", errors="replace")
    c = {"name": path.parent.name, "status": "OPEN", "what": "", "by": None,
         "minutes": "", "deadlines": [], "runs": [], "bad": []}
    for line in text.splitlines():
        top = line.startswith("- ") or not line[:1].isspace()  # ignore indented sub-lines
        t = line.strip().lstrip("-").strip()
        if t.startswith("# CASE:"):
            c["name"] = t[7:].strip() or c["name"]
        elif t.startswith("Status:"):
            word = t[7:].strip().split()[0].upper() if t[7:].strip() else "OPEN"
            if "|" not in t:  # skip the template line listing every status
                c["status"] = word
        elif t.startswith("What:"):
            c["what"] = t[5:].strip()
        elif t.startswith("User time needed:"):
            c["minutes"] = t[17:].strip()
        elif t.startswith("By:") and top:
            m = re.search(ISO, t)
            d = parse_date(m.group(1)) if m else None
            if d:
                c["by"] = d
            elif t[3:].strip():
                c["bad"].append(f'unreadable "By:" date: {t[3:].strip()}')
        elif t.startswith("Act by:") and line.startswith("- "):
            m = re.search(ISO, t)
            d = parse_date(m.group(1)) if m else None
            parts = [x.strip() for x in t.split("|")]
            label = parts[2] if len(parts) > 2 else "deadline"
            if "PLAN" in t.upper().split("|")[-1] or "| PLAN" in t.upper():
                label += " (planning date)"
            if d:
                c["deadlines"].append((d, label))
            else:
                c["bad"].append(f'unreadable "Act by:" date: {t[7:].strip()}')
        elif "rung:" in t and "portal:" in t:
            pm = re.search(r"portal:\s*([^|]+)", t)
            rm = re.search(r"rung:\s*(\d)", t)
            sm = re.search(r"stopped:\s*([^|]+)", t)
            if pm and rm:
                c["runs"].append((pm.group(1).strip(), int(rm.group(1)),
                                  sm.group(1).strip() if sm else ""))
    return c


def load(root):
    root = Path(root)
    if not root.is_dir():
        print(f"No cases folder at {root}")
        sys.exit(2)
    return [read_case(p) for p in sorted(root.glob("*/case.md"))]


def cmd_due(root, within, today):
    cases = load(root)
    if not cases:
        print("No cases found.")
        return 0
    overdue, due, later, undated = [], [], [], []
    horizon = today + timedelta(days=within)
    n_open = 0
    for c in cases:
        if c["status"] in CLOSED:
            continue
        n_open += 1
        items = [(d, f"deadline: {label}") for d, label in c["deadlines"]]
        if c["by"]:
            mins = f" (your part: {c['minutes']})" if c["minutes"] else ""
            items.append((c["by"], f"next action: {c['what'] or 'not stated'}{mins}"))
        if not c["by"] and not c["bad"]:
            undated.append((c, "no \"By:\" date for the next action"))
        for b in c["bad"]:
            undated.append((c, b))
        for d, what in items:
            row = (d, c["name"], what)
            (overdue if d < today else due if d <= horizon else later).append(row)

    def show(title, rows):
        if not rows:
            return
        print(f"\n{title}")
        for d, name, what in sorted(rows):
            delta = (d - today).days
            when = "today" if delta == 0 else f"in {delta}d" if delta > 0 else f"{-delta}d ago"
            print(f"  {d.isoformat()} ({when})  [{name}]  {what}")

    print(f"Today: {today.isoformat()}   Open cases: {n_open}   Closed: {len(cases) - n_open}")
    show("OVERDUE", overdue)
    show(f"DUE within {within} days", due)
    show("LATER", later)
    if undated:
        print("\nNEEDS A DATE (fix the case file)")
        for c, why in undated:
            print(f"  [{c['name']}]  {why}")
    if not (overdue or due or later or undated):
        print("\nNothing scheduled.")
    return 1 if (overdue or due) else 0


def cmd_score(root):
    cases = load(root)
    per = defaultdict(lambda: defaultdict(int))
    stops = defaultdict(lambda: defaultdict(int))
    total = 0
    for c in cases:
        for portal, rung, stopped in c["runs"]:
            per[portal][rung] += 1
            total += 1
            if rung != 1 and stopped:
                stops[portal][stopped] += 1
    if not total:
        print("No runs logged yet.")
        return 0
    print(f"Runs logged: {total}")
    print(f"{'portal':<22}{'runs':>5}  " + "  ".join(f"{RUNGS[r]:>15}" for r in (1, 2, 3, 4)) + "   filed %")
    for portal in sorted(per):
        n = sum(per[portal].values())
        cells = "  ".join(f"{per[portal].get(r, 0):>15}" for r in (1, 2, 3, 4))
        print(f"{portal:<22}{n:>5}  {cells}   {100 * per[portal].get(1, 0) // n:>6}%")
        if stops[portal]:
            top = sorted(stops[portal].items(), key=lambda kv: -kv[1])[:2]
            print(" " * 22 + "most common stop: " + "; ".join(f"{s} (x{k})" for s, k in top))
    return 0


def main(argv):
    if len(argv) < 2 or argv[0] not in ("due", "score"):
        print(__doc__)
        return 2
    if argv[0] == "score":
        return cmd_score(argv[1])
    within, today = 3, date.today()
    if "--within" in argv:
        within = int(argv[argv.index("--within") + 1])
    if "--today" in argv:
        today = parse_date(argv[argv.index("--today") + 1]) or today
    return cmd_due(argv[1], within, today)


if __name__ == "__main__":
    sys.exit(main(sys.argv[1:]))
