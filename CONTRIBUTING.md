# Contributing to Portal Pilot

Thank you for helping. Portals change without notice, so this project only stays useful if people who use them keep the maps current.

## The golden rule: no personal data, ever

Never commit a real name, phone number, email, address, Aadhaar, PAN, account, card, policy, PNR, application or complaint number, screenshot of a filled form, or anyone's case file. Test fixtures must be clearly fake and labelled `TEST DATA`. Pull requests containing personal data will be closed and the data purged.

## Ways to help

1. **Update a playbook** after you've used a portal and something differed: a renamed button, a new field, a changed limit, a new gate. Change the `Last walked` date and note what changed.
2. **Add a playbook** for a portal not yet covered. Follow [`references/playbook-format.md`](skills/portal-pilot/references/playbook-format.md). Mark anything you didn't personally see as `UNWALKED`.
3. **Correct a rule** in the grievance references (`skills/grievance-agent/references/`). Every deadline, fee or limit must cite an **official** page (regulator, ministry, gazette) with a short quote. Blogs and aggregators are leads, not sources.
4. **Report a bad route** as an issue: what you asked, what it said, what the official source says (with link).
5. **Add a saved route for your country.** After a verified run, the plugin saves a route card in your `portal-pilot/routes/` folder. Strip anything personal, check every quote still matches its official page, and send it to `skills/portal-pilot/routes/` following [`saved-routes.md`](skills/portal-pilot/references/saved-routes.md). Quotes stay in the original language with a translation.
6. **Add a use case.** Follow the recipe in [`docs/use-cases.md`](docs/use-cases.md): scenario, route, playbook, evals, in that order.
7. **Add an eval case** to [`evals/cases.md`](evals/cases.md) for any failure you found, so it can't come back.

## Before opening a pull request

- Run the scripts you touched: `python3 scripts/textcheck.py`, `python3 scripts/cases.py`, `python3 scripts/deadlines.py`.
- Validate the plugin if you have Claude Code: `claude plugin validate .claude-plugin/plugin.json`.
- Keep the gate rules intact. Changes that let the agent type OTPs or passwords, solve CAPTCHAs, tick consent boxes, upload files, pay or submit on the user's behalf will not be merged.
- Write plainly. Many users are reading in their second or third language.

## Questions

Open an issue. For anything involving a real person's case, describe it in general terms only.
