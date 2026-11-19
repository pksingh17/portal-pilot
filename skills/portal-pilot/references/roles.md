# Roles and handoffs

| Role | Model | Does | Never does |
|---|---|---|---|
| **Lead** (this skill) | Strongest available (Opus) | Intent contract, route, judgment calls, review summary, playbook writing, escalations | Bulk clicking, bulk extraction |
| **Route finder** (`route-finder` agent) | Sonnet | Finds which legitimate bodies and portals handle the task in any country, with a quote and URL for every rule; in check mode, tries to refute another finder's card | Opens portals, advises on merits |
| **Portal operator** (`portal-operator` agent) | Sonnet | Navigates, reads pages, fills fields from the field sheet, explores new portals, reports gates and errors | Gates, judgment calls outside the field sheet, submit |
| **Intake clerk** (`intake-clerk` agent) | Haiku | Extracts fields from documents, masks sensitive data, sorts and summarises replies | Decides anything, sends data anywhere |
| **Status watcher** (`status-watcher` agent) | Haiku | Checks a status page or inbox reply when asked, reports changes | Takes any action on what it finds |
| **Deadline engine** (`${CLAUDE_PLUGIN_ROOT}/scripts/deadlines.py`) | Code | Date arithmetic | Choosing the rule (the lead picks it) |
| **Text checker** (`${CLAUDE_PLUGIN_ROOT}/scripts/textcheck.py`) | Code | Checks drafts against a portal's length and character rules | Rewriting (the lead does) |

| **Case reader** (`${CLAUDE_PLUGIN_ROOT}/scripts/cases.py`) | Code | Lists what is due across all cases; scores runs by rung per portal | Deciding what to do about it (the due-check skill does) |

## Distribution rules

1. Work that doesn't need the user runs first and in parallel: one route-finder per candidate body or country, one clerk per document, check mode alongside drafting.
2. One operator per form, start to finish. Separate portals get separate tabs and separate operators.
3. A fresh agent checks high-stakes work; the producer never verifies itself.
4. The user's gates are packed into one sitting, announced with a brief, after the ready pack exists.
5. Every agent returns a partial result with honest gaps in preference to nothing; the lead fills gaps or sends a narrower follow-up.
6. Every run ends on a rung of the result ladder and is logged.

Why this split: judgment is rare and expensive, so it goes to the strongest model in a few calls. Navigation is many small steps, so it goes to a fast, capable model. Extraction and checking are high-volume and narrow, so they go to the cheapest. Arithmetic goes to code because code doesn't misremember dates.

## Handoff formats

**Lead → operator**
```
CONTRACT: [paste]
FIELD SHEET: [field: value (source, confirmed y/n)]
PLAYBOOK: [paste or "none: explore mode"]
TAB: [tab id]
STOP AT: every gate, every judgment call, final submit screen
```

**Operator → lead** (one of)
```
GATE: [type] on [page]. What the user must do: [plain words]
QUESTION: [field] offers [options]. Field sheet doesn't settle it.
ERROR: [page] says "[exact message]" after [action]. Tried: [n]
SURPRISE: [what differs from playbook]
READY FOR REVIEW: [every field and value on the final screen]
```

**Lead → intake clerk**
```
EXTRACT: [list of fields from the contract]
FROM: [file]
MASK: account/card numbers to last 4; omit anything not listed
```

## Escalation ladder

1. Operator retries a failed step with a different approach (twice).
2. Third failure: lead looks at the page and gives a new plan.
3. Lead can't resolve: bring in the user with a screenshot and a plain question.
4. Portal is down or blocking: stop, tell the user, offer the offline route (email, post, office visit).
