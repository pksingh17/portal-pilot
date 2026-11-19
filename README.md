# Portal Pilot

**Find the right official body for your problem, and get it done on their portal, with you in charge of every click that matters.**

A plugin for Claude that helps with real-world paperwork on government and company portals: complaints, refunds, RTI requests, applications, status checks and tax forms. It works out *who* handles your problem (most people's first obstacle), verifies every rule against official sources, drafts everything, fills the form in your own browser, and stops at every login, OTP, CAPTCHA, consent box, payment and submit button for you to do yourself.

**Works in any country.** A research agent finds the official bodies for your problem wherever you are, quoting every rule from an official source, in the original language with a translation. Every verified route is saved, so each country gets faster the more people use it. India has a deep built-in pack (consumer complaints, RBI and insurance ombudsmen, IRCTC, RTI, CPGRAMS, TDS).

> **Status: early, field-tested.** Real tasks have been done on live portals: an RTI request filed end to end, and IRCTC refund and TDS forms filled to the submit button (see [`evals/results-field.md`](evals/results-field.md)). The agents also pass controlled tests ([`evals/results-v0.4.md`](evals/results-v0.4.md)). Portals change without notice, so check every value at the review screen.

## Disclaimer

Portal Pilot helps you use official complaint and filing routes. It is **not legal, tax or financial advice**, and it is not affiliated with any government body, regulator or company. Rules, deadlines, fees and portals change: the plugin quotes and dates every rule it relies on, and you should confirm anything important on the official page before acting. For large claims, tax matters or anything going to court, consult a qualified professional. You alone submit, pay and sign; you are responsible for what you file.

## Install

In Claude Code (or any Claude app that supports plugins):

```
/plugin marketplace add pksingh17/portal-pilot
/plugin install portal-pilot@portal-pilot
```

Browser work needs the **Claude in Chrome** extension connected. Without it, Portal Pilot still finds and verifies routes, drafts everything and produces a ready pack you can file from yourself.

Then just say what you need, in your own language:

- *"My bank debited my EMI twice and won't refund it"* (India)
- *"My airline cancelled and only offers a voucher. Who do I complain to?"* (US)
- *"Meine Bank hat eine falsche Gebühr abgebucht"* (Germany: my bank charged a wrong fee)
- *"I bought from a shop in another EU country and the refund never came"*
- *"File an RTI about my stuck passport"*, or *"run my due-check"*

## Everyday commands

| Say | What happens |
|---|---|
| `Set me up` | Three-minute, skippable setup: your country, language, how much help you want, people you act for |
| *Describe your problem* | Task contract, verified route, drafts, ready pack; then the form filled in your browser if you want |
| `Who do I complain to about …?` | Route card only: the right official bodies, in order, each rule with its source |
| `I'm ready, let's file` | The sitting: the plugin fills the form, you do every gate and press submit |
| `They replied` + paste the reply | Reply classified (resolved, partial, stalling, rejected, suspicious) and the next step proposed |
| `Run my due-check` | What's overdue or coming up across all your cases, with the next step already prepared |
| `I moved to Germany` / `Talk to me in Hindi` | Updates your setup |

## What it can do today

See [`docs/use-cases.md`](docs/use-cases.md) for the catalogue of supported jobs, each one's honest status, and the recipe for adding a new one.

## How it works

1. **Intent first.** Asks "What do you want to get done?" and writes a task contract the user confirms: goal, done-when, for whom, where, data needed, gates, deadlines, stakes.
2. **Route.** Finds which legitimate bodies handle the task, in any country, with a quote and link for every rule. Verification scales with the stakes; high-stakes routes get a second, independent check.
3. **Gather.** Pulls only the fields the contract needs from the user's documents, masked.
4. **Prepare.** Drafts every answer and checks it against the portal's text rules before the portal is opened, so sessions don't time out mid-task.
5. **Operate.** Fills the portal in the user's own Chrome, reads back what it filled, and pauses at login, OTP (including "Get OTP"), CAPTCHA, consent, uploads, payment, the first server-side save and submit.
6. **Review.** Shows every value as read from the page before the user clicks submit themselves.
7. **Remember.** Keeps a case file (contract, route, timeline, deadlines, next action) in the user's folder so a task survives across days and sessions, and a playbook for each portal so the next run is faster.

## Getting results

- **Result ladder.** Every run ends on the highest rung it can reach: filed; ready at the submit button; a ready pack the user can file from alone in ten minutes; or an offline letter to the right officer. The ready pack is written before any portal is opened, so a failed portal still leaves a usable result.
- **One sitting.** Everything that doesn't need the user is done first and in parallel. The user's gates are packed into one short, announced sitting.
- **Wake-ups.** A daily due-check reads every case file, prepares the next step, and reports what needs the user and for how long.
- **Scorecard.** Each run's rung is logged, so `scripts/cases.py score` shows which portals complete and where the others stall.

## Components

| Component | Model | Purpose |
|---|---|---|
| `portal-pilot` skill | Session model (best on the strongest available) | Lead: intent, verification, judgment, review, case files, playbooks |
| `setup` skill | Session model | One-time, skippable setup of your personal folder; later edits |
| `due-check` skill | Session model | Daily wake-up: what's due across all cases, next step prepared, short report |
| `grievance-agent` skill | Session model | Indian complaint and refund law: escalation routes, deadline protocol, letter templates |
| `route-finder` agent | Sonnet | Finds and verifies bodies and portals; check mode refutes another card |
| `portal-operator` agent | Sonnet | Browser navigation, form filling, read-back, resumable state |
| `intake-clerk` agent | Haiku | Field extraction from documents, masking |
| `status-watcher` agent | Haiku | Status checks and reply triage |
| `scripts/deadlines.py` | Code | Date arithmetic |
| `scripts/cases.py` | Code | `due`: overdue and upcoming actions across cases; `score`: rungs reached per portal |
| `scripts/textcheck.py` | Code | Checks drafts against a portal's length and character rules |
| `evals/` | | Regression cases and fixtures; run before every release |

## Setup

- Needs the Claude in Chrome extension connected for browser work.
- Say **"set me up"** once (optional). Everything is saved to a `portal-pilot/` folder in your working folder, which you can read, edit or delete at any time:

```
portal-pilot/
├── me.md          country, language, help level, people you act for
├── memory.md      how bodies behaved before; how you like letters written
├── cases/         one folder per task
├── routes/        verified route cards for your country
└── playbooks/     portal maps learned on your runs
```

No passwords, OTPs, PINs or full ID, account or card numbers are ever stored.

## Limits

- Never solves CAPTCHAs, types passwords or OTPs, ticks consent boxes, uploads files, pays, or submits. The user does these.
- The gate rules are instructions to the model, not technical locks. The browser extension's own permission prompts are the backstop.
- Privacy rules follow India's DPDP Act 2023 and DPDP Rules 2025; this is design guidance, not legal advice.
- It maps routes and fills forms. It doesn't give legal or tax advice; high-stakes points are flagged for a CA or lawyer.
- **Coverage:** four portal playbooks in the repo. Real runs so far: RTI Online filed; IRCTC refund and TDS filled to submit (`evals/results-field.md`). Portals without a playbook are learned live, which is slower.

## Contributing

Two contributions matter most, and neither contains personal data:

- A **playbook**: a map of a portal's flow, fields, text rules, gates and traps.
- A **saved route**: a verified route card for a kind of problem in your country. This is how a new country gets covered.

Portals and rules change often, so updates matter as much as new files. See [CONTRIBUTING.md](CONTRIBUTING.md).

## License

[MIT](LICENSE) © 2026 Prabhakar Singh
