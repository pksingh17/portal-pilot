# Case files

Real tasks run for weeks: a complaint, a 30-day wait, an escalation, a refund. Conversations end long before that. The case file is the task's memory. It lives in the user's working folder, so it survives across sessions and the user can read, edit or delete it.

Location: `portal-pilot/cases/<short-name>/case.md` (for example `cases/hdfc-double-debit/case.md`). Keep drafts and letters beside it in the same folder. If no working folder is available, say so and give the user the case file as a downloadable file to keep and re-attach next time.

Template: [`assets/templates/case.md`](../assets/templates/case.md). Create a new case from it with `python3 ${CLAUDE_PLUGIN_ROOT}/scripts/cases.py new <cases folder> <short-name>`, which fills in today's dates.

Rules:
- **Masked identifiers only.** Account, card, policy, Aadhaar, PAN: last four digits. Never passwords, OTPs, PINs, CVVs.
- **Update at every step**, including failed ones. A case file that lags the truth is worse than none.
- **One line per event** in the timeline, with the reference number. This is the evidence chain an ombudsman or commission asks for.
- **On return**, read the case file before asking the user anything. Check today's date against every deadline and the Next action, and lead with whatever is due or overdue.
- **Machine-readable lines.** `Status:`, `By:`, `Act by:` and the Runs lines are read by `scripts/cases.py` for the daily due-check and the scorecard. Keep their format exact and dates in ISO form (`2026-12-01`). Every open case must have a `By:` date; "waiting" is an action too ("check for the bank's reply").
- **Log every run**, including failed ones, with the rung reached (1 filed, 2 ready at submit, 3 ready pack, 4 offline route).
- **Changing dates.** PLAN dates may be moved whenever the plan changes. A LEGAL date changes only after re-checking the official source: log the old and new date and the source in the Timeline, and tell the user in the next message. Once a step is done, delete its PLAN line.
- **On close**, record the outcome (amount recovered, days taken, body that resolved it) and set Status. Offer to delete the folder.
