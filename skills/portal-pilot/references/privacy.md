# Privacy rules

These rules are a **global baseline**: purpose limitation, data minimisation, consent, security and deletion, the principles shared by the EU GDPR, India's DPDP Act 2023 and DPDP Rules 2025, and most modern data-protection laws. Follow them in every country. Where a local law is stricter (for example on health data, children's data or national ID numbers), follow the local law as well; when unsure, take the stricter reading. This is design guidance, not legal advice; a product handling user data at scale needs a lawyer's review.

## Purpose limitation

- The task contract's **Goal** is the purpose. Collect only data that serves it.
- New need mid-task: say what and why, ask first.
- Never reuse a user's data for another task, another person, or "improving" anything without fresh, specific consent.

## Never collect, never type

Passwords, OTPs, PINs, UPI PINs, CVVs, full card numbers, net-banking credentials. These go from the user's hand into the portal, never through you. If the user pastes one: don't use it, and keep it out of every file and note. For a password or PIN, advise changing it. For an OTP, ask whose account it belongs to and whether they requested it just now; if they didn't, or if anyone asked them for it, treat it as a scam attempt and tell them not to share it with anyone. Some OTPs stay valid until used.

## Minimise what you do handle

- National ID numbers (Aadhaar in India, Social Security Number in the US, National Insurance number in the UK, CPF in Brazil, and their equivalents): masked (last 4 characters) everywhere except a portal field that requires the full number, which the user types themselves or confirms on screen.
- Tax IDs (PAN and equivalents), account numbers, policy numbers: mask in notes and summaries (last 4).
- Documents: ask for only the pages that prove the point; suggest redacting unrelated transactions and addresses.
- Health, caste, religion, and other sensitive details: only when a form legally requires them and the user agrees.

## Consent on the portal

Portal consent checkboxes (like RBI CMS's data-consent box) are the user's own consent to that organisation. The user reads and ticks them. Point them out; never tick them.

## Other people's data

Acting for someone else requires their knowledge and agreement, and their presence for their own OTPs and consent. For a child, a parent or guardian consents. Never look up, compile, or enter data about a person who isn't part of the agreed task.

## Retention and deletion

- Working notes and extracted fields exist only for the task.
- At the end: tell the user what was handled; delete working copies; keep only what the user asks to keep (the acknowledgement, the case file).
- Playbooks hold portal structure only. Before saving one, strip names, numbers, dates of birth, addresses, reference numbers, screenshots containing personal data.

## Suspected scams

Flag look-alike URLs, unofficial helpline numbers, pages asking for OTPs outside the official flow, payment requests to personal UPI IDs, and remote-access app requests (AnyDesk, TeamViewer). Stop and tell the user.
