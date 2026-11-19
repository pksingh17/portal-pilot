# Saved routes

Route-finding is the most expensive research Portal Pilot does, and the answer is the same for everyone with the same problem in the same place. So verified route cards are saved and reused, the way playbooks are. A playbook maps a **portal**; a saved route maps **which bodies handle a kind of problem in a country**. Together they let the plugin learn the world as people use it.

## Where

- Bundled: `routes/` in this skill folder (contributed, reviewed).
- The user's own: `portal-pilot/routes/` in their working folder (saved by the lead after each verified card).
- File name: `<country>-<sector>-<problem>.md`, all lowercase, ISO country code: `br-airline-cancelled-flight.md`, `de-bank-wrong-charge.md`, `in-insurance-claim-rejected.md`. Add the state or region after the country when the route is local: `us-ca-utility-billing.md`.

## Format

The route card exactly as `route-finder` returns it, with a header:

```
# ROUTE: [country] / [sector] / [problem in plain words]
Saved: YYYY-MM-DD    Last verified: YYYY-MM-DD    Stakes it was verified for: LOW | MEDIUM | HIGH
Language of sources: [e.g. Portuguese, quotes kept in original with translation]
Check mode run: yes (YYYY-MM-DD) | no

[route card]
```

## No personal data

A saved route holds bodies, rules, URLs and quotes only. Remove the Task line's personal details ("my EMI of ₹14,200" becomes "a duplicate loan debit"), every amount, date and name from the user's case, and every reference number. If in doubt, leave it out.

## Reusing a saved route

Read the `Last verified` date, then scale to the new task's Stakes:

| Stakes | Saved route under 30 days old | Older than 30 days |
|---|---|---|
| LOW | Use it. Check the domains still load | Use as hints; send route-finder to refresh |
| MEDIUM | Use it, but open the official page for every deadline and fee yourself | Send route-finder to refresh |
| HIGH | Always a fresh route-finder and a check-mode pass. The saved card is only a starting list | Same |

A saved route never overrides an official page. If the page says something different, the page wins: update the saved file, note what changed and the date.

After a refresh, overwrite the file and update `Last verified`. Offer the user to contribute it (see CONTRIBUTING.md).
