---
name: setup
description: Set up Portal Pilot for a user once, so every later task starts in the right country, language and legal system without re-asking. A short, skippable interview that writes a personal folder (me.md, memory.md, cases, routes, playbooks). Also edits it later. Use when the user says "set me up", "set up portal pilot", "remember my details", "I moved to another country", "change my language", "add my mother as someone I help", "change how much you do for me", or when the portal-pilot skill offers setup at the end of a first task. Never run it ahead of an urgent task.
---

# Setup: a personal folder for Portal Pilot

Every task needs the same few facts: which country's rules apply, what language to work in, how much the user wants done for them, and who they act for. Setup asks once and writes them down, so the next task starts warm.

## Never block an urgent task

If the user has an emergency (money just stolen, a deadline today or tomorrow, a portal session open now), **don't run setup**. Hand straight to the `portal-pilot` skill. Setup can be offered once the urgent part is done. A user who came for help and got a questionnaire has been failed.

## Where the folder lives

Use the most durable storage the environment offers:
- **A working folder** (Claude Code, Cowork, any agent with files): create `portal-pilot/` there. Suggest a synced folder (Google Drive, iCloud, OneDrive, Dropbox) so it survives a lost laptop.
- **A chat with no file storage:** build the files, give them to the user as downloads, and tell them to attach `me.md` at the start of the next session.

```
portal-pilot/
├── me.md          who I am for this tool: country, language, help level, people I act for
├── memory.md      what has happened: how bodies behaved, letter voice, things not to repeat
├── cases/         one folder per task (references/case-file.md)
├── routes/        verified route cards (references/saved-routes.md)
└── playbooks/     portal maps learned on my runs (references/playbook-format.md)
```

Templates: `assets/templates/` in the portal-pilot skill folder (`${CLAUDE_PLUGIN_ROOT}/skills/portal-pilot/assets/templates/`). Replace every `[...]`; delete lines that don't apply rather than leaving them blank.

If `portal-pilot/me.md` already exists, this is an **edit**: read it first and change only what the user asks.

## The interview: three short rounds, about three minutes

Ask in the user's language. Every question can be skipped; a skipped answer is left out of the file, not guessed. Ask each round in one message.

**Round 1: where and which language.**
- Which country do you live in? And state, province or region, if your problems are often local (electricity, local tax, state RTI)?
- Which language should I talk to you in? And which language should letters and complaints be written in? (Often the same; sometimes the official language is different. Say so if the country's bodies accept other languages.)

**Round 2: how much help, and reminders.**
- Explain the three help levels in one line each and recommend one:
  - `find`: I tell you which official body handles it and how, with sources. You do the rest.
  - `prepare`: I also draft everything and build a ready pack you can file from in ten minutes.
  - `operate`: I also fill the forms in your Chrome browser while you do every login, code, tick box, payment and submit.
  
  Recommend `operate` if Claude in Chrome is connected, otherwise `prepare`. Say this is a default; any task can use a different level.
- Want a daily check for deadlines on your cases? If yes, at what time? (Set it up only once a scheduling tool confirms it exists; see the portal-pilot skill, Step 6.)

**Round 3: optional details that save time later.** Say plainly that each one is optional and stays in their own folder.
- The last four digits of the phone that receives your OTPs, so I can tell you which phone to have ready. Never the full number unless you want it in letters.
- The email address you want replies sent to, if you'd like it pre-filled in letters.
- Anyone you regularly help (a parent, a child, a client)? Their relationship to you, whether they've agreed, and whether they can be present for their own OTPs. Don't record their ID numbers.
- Portals you already have accounts on (for example the income tax portal or IRCTC). Account names only, never passwords. This tells me whether a task needs a registration step.
- Anything I should always ask you about first, or never do?

## Write the files

1. Create the folder and its three sub-folders.
2. Fill `me.md` and `memory.md` from the templates.
3. **Never store** passwords, OTPs, PINs, CVVs or full ID, account or card numbers, even if the user offers them (`references/privacy.md` in the portal-pilot skill). If they paste one, say it's been left out and why.
4. Show a five-line summary: country and region, languages, help level, reminders, people they act for. Ask "Is this right?" and fix what they correct.
5. Tell them where the files live and that they can read, edit or delete them at any time. Deleting `me.md` undoes setup.

## Then offer one useful next step

- If they came with a task: "Shall we start on it?" and hand to `portal-pilot`.
- If not: offer to map the main complaint routes for their country for one problem they're likely to have (a bank charge, a delayed refund, a utility bill). That runs the route-finder once, saves a verified route to `routes/`, and shows them what the tool does. Ask before spending the time.

## Editing later

- **Moved country:** update `country` and `region`. Existing cases keep their own jurisdiction; say so. Saved routes for the old country stay; they're still valid there.
- **Language or help level:** change the line; confirm in one sentence.
- **Someone they help** no longer agrees, or has died: remove them, and ask whether any open case in their name should be closed.
- Update `last_updated` on every edit.
