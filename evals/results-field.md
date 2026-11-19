# Field runs: real tasks, real portals, real users

Controlled tests (`results-v0.4.md`) prove the agents behave. This file proves the plugin works on live portals for real people. One row per real run. **No personal data:** no names, PNRs, PANs, TANs, reference or acknowledgement numbers. Record the rung and what happened, never the identifiers.

Rungs: 1 filed by the user, 2 ready at submit, 3 ready pack, 4 offline route.

| Reported | Portal | Task | Rung | Who submitted | Notes |
|---|---|---|---|---|---|
| 2026-11-19 | RTI Online (rtionline.gov.in) | RTI request to a Central Government authority | **1** | User | Filled via Claude in Chrome; user passed the gates and submitted; registration number received. Run date not recorded |
| 2026-11-19 | IRCTC | Refund claim (TDR) | 2 | (stopped before submit) | Form filled to the submit button. No IRCTC TDR playbook in the repo yet: route learned live |
| 2026-11-19 | Income Tax / TDS | TDS return forms | 2 | (stopped before submit) | Forms filled to the submit button. HIGH stakes: CA review advised before any real submission |

All three were reported by the maintainer from their own use. They weren't run as scripted evals, so the per-gate pass/fail table in `docs/first-real-run.md` wasn't recorded for them. Future runs should record it.

## What these runs leave open

- No playbook was saved from any of them. The next run of each should save one (structure only) so the route stops being learned from scratch each time.
- Rung 2 on TDS and IRCTC is a strong result, but which gates came up, and in what order, isn't recorded. That is the missing piece for those playbooks.
