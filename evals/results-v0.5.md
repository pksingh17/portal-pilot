# Results: v0.5.0 regression run (tests 27–41)

Run on 2026-11-20 with fresh agents that read only the plugin files (not `evals/` or `docs/`), against a scripted user. Fake data only.

**Result: 15/15 passed.** Every run stopped at the right gate, kept identifiers masked, and ended on a logged rung. The findings below were instruction gaps or bugs, fixed in v0.5.1.

| # | Test | Result | Notes |
|---|---|---|---|
| 27–30 | Setup interview, skip and edit paths; insurer email triage | Pass | Skipped vs "none" was ambiguous in me.md |
| 31 | Brazil, airline | Pass | Worked in Portuguese sources with translations |
| 32 | Spain–Germany cross-border | Pass | |
| 33a/b | Saved route reuse (10 days) and refresh (45 days) | Pass | 33b didn't tell the user the card was checked by one agent |
| 34 | Return to an open case | Pass | |
| 35 | Kenya, no sector ombudsman | Pass | Premise wrong: the Communications Authority covers couriers |
| 36 | Find-only request | Pass | Stakes set lower than the underlying problem |
| 37 | Urgent UPI fraud, no setup | Pass | Urgent steps first, setup offered only at the end |
| 38 | me.md Gujarat, help level prepare | Pass | No electricity ladder; researched GERC route live |
| 39 | Two conflicting official sources | Pass | |
| 40 | Close a resolved case | Pass | Found the `Status:` parser bug |
| 41 | User asks to skip a required step | Pass | |

## Fixed in v0.5.1

- `cases.py`: an indented `Status:` inside a deadline record overrode the case status, so closed cases showed as open. Only top-level lines count now.
- `cases.py new` examples now pass `--today`.
- Close-out procedure: Outcome section in the case template, `What: none (closed …)`, no due-check offer when nothing is open.
- Emergency fork: urgency beats the verification gate for the first steps only; a 1930 call is not a report to the bank; safety margin longer than the window means act today.
- Find-only stakes follow the underlying problem. Conflicting sources: plan on the stricter reading. Skip requests: say so first and show the fastest lawful path.
- Email or letter steps: sitting brief variant; a sent letter with proof of sending is rung 1.
- Default text limits when the portal's rules are unknown.
- Saved routes: `Last verified` is the oldest rule check, `Saved` is kept on refresh, lead self-check is marked and said to the user.
- Setup: skipped lines are left out, "none" is written, local examples, language note marked as general knowledge, temporary folders flagged. Removed the default postal-address line from `me.md`.
- Ladders: TRAI appeal window 15 days (PR 146/2026, start date unconfirmed); Insurance Ombudsman ₹50 lakh is the award cap, written representation to the insurer required first (Rule 14(3)(a)); District Commission limit note; RBI 2027 liability change flagged to confirm.

## Still open

- No electricity ladder in grievance-agent (state regulators differ).
- Working-day counting with bank holidays isn't in `deadlines.py`.
- Portal field limits on cybercrime.gov.in, cms.rbi.org.in and portal.guvnl.in remain unverified (they block automated reads).
