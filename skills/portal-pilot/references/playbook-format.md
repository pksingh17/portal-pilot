# Playbook format

One file per portal flow: `playbooks/<portal>-<flow>.md`. A playbook maps the portal. It never holds personal data.

```
# [Portal name]: [flow, e.g. "file a complaint"]
Official URL: [verified start URL]
Last walked: [date]   Result: [reached review screen / filed / blocked at …]
Confidence: high | medium | low

## Prerequisites
- [what must exist before starting]

## Route
1. [page name]: [what's on it] → [action] → [next page]
   GATE: [CAPTCHA / OTP / consent / login] — user does: [plain words]
2. ...

## Field map
| Portal field | Field sheet key | Notes (format, length limit, validation quirks) |

## Text rules
- [field]: max [n] characters; allowed `[class]` or banned `[chars]`  (feeds scripts/textcheck.py)

## Session
- [timeout length if known; what the expiry looks like; whether drafts are saved]

## Judgment calls seen
- [field]: [options] → [how to choose]

## Errors and fixes
- "[exact message]" → [cause] → [fix]

## Watch for
- [session timeouts, opens in new tab, uploads size limit, etc.]
```

Rules:
- Update after every run, even a failed one. Note what changed and the date.
- If a page differs from the playbook, trust the page, explore, then rewrite that step.
- Mark steps not walked yet as UNWALKED.
- Staleness: a playbook walked within 60 days is followed; older than that it is a set of hints, and the operator explores. Portals change without notice.
- Record which button first saves to the server, and every button that sends an OTP or message: these are gates.
