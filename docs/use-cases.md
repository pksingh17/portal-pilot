# Use cases

A **use case** is one real-world job a person brings to Portal Pilot, described well enough that the plugin can do it and a test can prove it did.

"Help with complaints" is not a use case. "My bank debited my EMI twice, customer care has ignored me for five weeks, and I want the money back" is one.

## What a use case is made of

Every use case has four layers. Each layer is a file that already has a home in this repo:

| Layer | Answers | Lives in | Format |
|---|---|---|---|
| 1. **Scenario** | Who is stuck, on what, and what "done" looks like | This file (the catalogue below) | Template below |
| 2. **Route** | Which official bodies handle it, in what order, under which rules | `skills/grievance-agent/references/escalation-ladders.md` (India), or found live by `route-finder` | Quote + official URL for every rule |
| 3. **Playbook** | How the portal actually behaves: pages, fields, text rules, gates, traps | `skills/portal-pilot/playbooks/<portal>-<flow>.md` | [`playbook-format.md`](../skills/portal-pilot/references/playbook-format.md) |
| 4. **Eval** | Proof it works, and that it stays working | `evals/cases.md` (+ `evals/fixtures/` for fake documents) | One table row with a "Pass if" column |

A use case is **complete** when all four exist and its eval passes. Until then it is listed with its status, so nobody mistakes a plan for a feature.

## How to create one: the recipe

Do these in order. Each step feeds the next.

### 1. Write the scenario from a real person's mouth

Start with the sentence a user would actually type, not the feature you want to build. Then fill in the template (below). The hard fields are:

- **Done when**: something observable. "Complaint number received", "refund credited", "RTI reply received". Not "user is helped".
- **Stakes**: LOW, MEDIUM or HIGH, using the definitions in [`SKILL.md`](../skills/portal-pilot/SKILL.md) Step 0. Stakes decide how hard the route is verified, so get this right.
- **Gates**: every point where the human must act (login, OTP, CAPTCHA, consent, upload, payment, submit). If you don't know yet, write "to find".
- **What goes wrong**: the realistic ways this fails. Portal times out, company never replies, user misses the 30-day window, a reply turns out to be phishing. These become your eval cases.

### 2. Map the route, with sources

Ask Portal Pilot itself: "Who do I complain to about X in Y?" That's a find-only run; it returns a route card. Then check every deadline, fee and limit on that card against the official page. If you can't find the official source, the rule stays `UNVERIFIED`. Never copy a figure from a blog.

For an Indian sector not yet in `escalation-ladders.md`, add it there with the official quote, URL and check date.

### 3. Walk the portal and write the playbook

Open the portal yourself, or run the plugin in explore mode, and go as far as you can **without real data**. Usually that's the first gate. Record pages, field names, character limits, banned characters, which button sends an OTP, which button first saves to the server, and how the session expires. Mark everything you couldn't see as `UNWALKED`.

No personal data, ever: no screenshots of filled forms, no real numbers.

### 4. Turn the failure modes into eval cases

Every line in "What goes wrong" becomes a row in `evals/cases.md`:

- **Happy path**: the scenario as written. Pass if it reaches the highest rung it honestly can.
- **At least one gate test**: the user tries to hand over a gate, or the page tries to instruct the agent.
- **At least one failure test**: portal down, deadline close, document missing.

If a test needs a document, make a fake one in `evals/fixtures/`, labelled `TEST DATA` at the top. Planting a trap in it (an injected instruction, a CVV that must not be copied) is encouraged.

### 5. Run it, then mark the status

Run the eval in a fresh session with only the plugin installed. Record the result in `evals/results-*.md` and update the status in the catalogue below.

## Template

Copy this block into the catalogue and fill it in.

```
### UC-NN: [short name]
Status: IDEA | ROUTED | PLAYBOOK | TESTED | PROVEN
Country: [country / state]      Stakes: LOW | MEDIUM | HIGH

**User says:** "[the sentence a real person would type]"

**Situation:** [two or three lines: what happened, what they've already tried]
**Done when:** [the observable finish]
**Route:** [body → body → body], see [ladder section or route card]
**Portal(s):** [playbook file(s), or "to walk"]
**Gates:** [login, OTP, CAPTCHA, consent, upload, payment, submit, in order]
**Documents needed:** [only what the goal requires]
**Deadlines that matter:** [rule + source, or "to verify"]
**What goes wrong:**
- [failure mode] → eval #[n]
- [failure mode] → eval #[n]
**Evals:** #[n], #[n]
**Open questions:** [what nobody has confirmed yet]
```

Status ladder:

- **IDEA**: scenario written, nothing else.
- **ROUTED**: route mapped with official sources.
- **PLAYBOOK**: portal walked at least to the first gate.
- **TESTED**: evals written and passing in a fresh session.
- **PROVEN**: completed end to end by a real user who passed the gates themselves (eval #19).

No use case is PROVEN yet.

## Catalogue

### UC-01: Bank double debit
Status: TESTED (lead and sub-agents; portal past the first gate UNWALKED)
Country: India      Stakes: MEDIUM

**User says:** "My bank debited my EMI twice and won't refund it."

**Situation:** Two identical debits on the statement. User complained to customer care; no resolution.
**Done when:** Duplicate amount credited back, or an RBI Ombudsman complaint number received.
**Route:** Bank grievance cell → nodal / principal nodal officer → RBI Ombudsman (CMS). See `escalation-ladders.md`, banking.
**Portal(s):** `rbi-cms-file-complaint.md`
**Gates:** CAPTCHA, consent, OTP, upload, submit
**Documents needed:** Statement page showing both debits (other rows redacted), the bank's complaint reference.
**Deadlines that matter:** Bank's 30-day window, then 90 days to approach the Ombudsman (RB-IOS 2026). Verify on rbi.org.in before relying on it.
**What goes wrong:**
- Statement contains planted instructions or a CVV → eval #1
- Bank's "reply" is a phishing email → eval #2
- User waits past 30 days and nobody escalates → eval #25
- Operator reaches CAPTCHA → must stop → eval #3
**Evals:** #1, #2, #3, #10, #25
**Open questions:** Steps after the first CMS gate not walked.

### UC-02: RTI on a stuck government application
Status: TESTED (form past the guidelines checkbox UNWALKED)
Country: India (Central Government bodies only)      Stakes: MEDIUM

**User says:** "My passport has been stuck for months. File an RTI."

**Situation:** Application pending with no explanation.
**Done when:** RTI registration number received.
**Route:** RTI Online → the public authority's CPIO. State bodies are not on this portal.
**Portal(s):** `rtionline-submit-request.md`
**Gates:** guidelines consent, OTP or login, payment, submit
**Documents needed:** Application reference (user types it); BPL certificate only if claiming fee waiver.
**Deadlines that matter:** Request text ≤ 3,000 characters (from the portal). Reply period to verify on rti.gov.in.
**What goes wrong:**
- Draft too long or contains banned characters → eval #16
- RTI is for a parent who isn't present → eval #13
- User has only two minutes → ready pack instead of portal → eval #20
**Evals:** #13, #16, #20, #23
**Open questions:** Whether the text box keeps line breaks; which authority entry covers a Regional Passport Office.

### UC-03: Railway complaint
Status: PLAYBOOK (categories behind OTP UNWALKED)
Country: India      Stakes: LOW

**User says:** "The AC in my coach didn't work for the whole journey."
**Done when:** Rail Madad reference number received.
**Route:** Rail Madad (or 139).
**Portal(s):** `railmadad-lodge-complaint.md`
**Gates:** Get OTP (sends an SMS, so it's a gate), OTP entry, upload, submit
**What goes wrong:**
- Operator clicks "Get OTP" itself → eval #4
- Portal session expires mid-form → eval #5
**Evals:** #4, #5
**Open questions:** Everything behind the OTP. This is the candidate for eval #19, the first real end-to-end filing: see [`first-real-run.md`](first-real-run.md).

### UC-04: Income-tax refund status
Status: ROUTED (no public refund page found)
Country: India      Stakes: LOW
**Portal(s):** `incometax-refund-status.md`
**Open questions:** Refund status appears to sit behind login. Needs a walk with the user at the login gate.

### UC-05: Cancelled flight, voucher instead of refund
Status: ROUTED
Country: US      Stakes: MEDIUM
**User says:** "United cancelled my flight and only offers a voucher."
**Route:** Airline → US DOT complaint portal (.gov); card dispute as a parallel route.
**Evals:** #7
**Open questions:** No playbook for the DOT portal yet.

### UC-06: Quarterly TDS return
Status: ROUTED (HIGH stakes: CA should confirm)
Country: India      Stakes: HIGH
**Evals:** #6, #9, #15
**Open questions:** Where TDS statements are uploaded is unresolved (see `results-v0.4.md`, Still open).

### UC-07: Bank refused to refund an authorised push payment scam
Status: ROUTED
Country: UK      Stakes: HIGH
**Evals:** #8

### UC-08: Health insurance claim rejected
Status: IDEA (route drafted from `escalation-ladders.md` section 2, not yet re-verified on official pages; no playbook)
Country: India      Stakes: MEDIUM, or HIGH when the claim is large or a limitation date is close

**User says:** "My health insurer rejected my hospital claim saying it was a pre-existing disease. I declared everything when I bought the policy."

**Situation:** Cashless or reimbursement claim refused in writing. The user may have called customer care but usually hasn't written to the insurer's Grievance Redressal Officer (GRO). They're angry and want to "go to consumer court" straight away.
**Done when:** The claim is paid (fully or partly), or an Insurance Ombudsman complaint number is received.
**Route:**
1. Insurer's GRO [PREREQ]: a written complaint quoting the rejection letter. Insurer to resolve within 14 days.
2. IRDAI Bima Bharosa [PARALLEL, optional]: doesn't auto-escalate to the Ombudsman.
3. Insurance Ombudsman (Bima Lokpal) [FORUM, EXCLUSIVE]: if the insurer rejects the complaint, replies unsatisfactorily, or doesn't reply within 30 days. Claims up to ₹50 lakh. Free.
4. Consumer commission [FORUM]: only if the Ombudsman route is unavailable, rejected, or the claim is above the cap. **Filing here bars the Ombudsman for the same matter.**

**Portal(s):** to walk: the insurer's grievance page (varies by insurer), Bima Bharosa, and the Ombudsman's online complaint portal.
**Gates:** login or registration, OTP, upload (policy, rejection letter, discharge summary, bills), consent/declaration, submit
**Documents needed:** Policy schedule, proposal form (proves what was declared), rejection letter, discharge summary, bills. Only the pages that matter; diagnoses beyond the claim stay out.
**Deadlines that matter:** Ombudsman: within one year of the insurer's final reply, or one year after the 30-day period with no reply (Insurance Ombudsman Rules, 2017; confirm on the official page before use).
**What goes wrong:**
- User wants the consumer commission and the Ombudsman at once, so filing at the commission kills the free route → eval #27
- User skips the GRO and goes straight to the Ombudsman, so the complaint isn't maintainable → eval #28
- Medical documents are over-shared (full history, other family members on a floater policy) → eval #29
- Insurer's "reply" is a settlement call asking the user to sign a discharge voucher for less → eval #30
**Evals:** #27, #28, #29, #30
**Open questions:** Current Ombudsman portal URL and its forms; whether the Ombudsman office is chosen by the insurer's branch or the user's address (the ladder says insurer's branch: verify); the health-data rules in `privacy.md` for medical records.

## Good next use cases

These sit in `grievance-agent`'s scope but have no playbook or eval yet. Each would be a strong first contribution:

- E-commerce refund not received → seller/platform → National Consumer Helpline → e-Jagriti
- Telecom billing dispute → operator → appellate authority
- Grievance against a central government office → CPGRAMS
- IRCTC refund (TDR) not credited → status check with `status-watcher`
