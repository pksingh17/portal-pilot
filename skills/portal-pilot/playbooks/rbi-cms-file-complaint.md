# RBI CMS: file a complaint with the RBI Ombudsman
Official URL: https://cms.rbi.org.in
Last walked: 2 November 2026 (operator test run)   Result: stopped at first gate (no live case)
Confidence: medium for steps 1–2; steps 3+ UNWALKED

## Prerequisites
- Written complaint already made to the bank / NBFC / wallet, with its reference number.
- Either 30 days passed since the entity received it with no reply, or it rejected the complaint wholly or partly, or the reply is unsatisfactory.
- Within 90 days of the later of: expiry of the 30-day period, or the entity's last communication (RB-IOS 2026). Load `grievance-agent` for deadline rules.
- Entity is covered by RB-IOS 2026 (portal home page links both covered and not-covered lists).

## Route
1. **Home** (cms.rbi.org.in/cms/indexpage.html): buttons File a Complaint / Track Your Complaint / File an Appeal / Feedback; language selector top right; helpline 14448.
   → Click **File a Complaint**. Opens a **new tab** ("Customer Digital Journey", path /rbi/vividflow/run/rbi#captchaAuthentication).
2. **Captcha page**: case-sensitive image CAPTCHA with audio and refresh options; notice that a complaint to the regulated entity first is mandatory; data-consent checkbox ("free, specific and informed consent to Reserve Bank of India for the collection, processing, storage, and use of my personal data for the purpose of complaint resolution"); **Next** button.
   GATE: CAPTCHA — user types the code.
   GATE: consent — user reads and ticks the box.
   → Next.
3. UNWALKED. Expected next: mobile number and OTP verification (GATE: OTP).
4. UNWALKED. Expected: complainant details, entity selection, complaint category, facts, relief, uploads, declaration, review, submit (GATE: final submit).

## Field map
UNWALKED.

## Watch for
- First load can be slow: after navigating, wait ~5 seconds and confirm the URL is no longer chrome://newtab/ before reading the page. (Seen 2 November 2026.)
- Home resolves to /cms/indexpage.html#eng.
- "File a Complaint" is a postback link with no accessible name (javascript:__doPostBack('HyperLink3','')): find it by its visible text or click by screenshot position.
- The form opens in a new tab: operator must switch to it.
- Page warns never to share password, PIN, OTP, CVV, UPI PIN or card details.
