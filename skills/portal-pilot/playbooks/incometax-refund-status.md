# Income Tax e-filing: check refund status
Official URL: https://www.incometax.gov.in/iec/foportal/
Last walked: 2 November 2026 (operator test run, no data)   Result: no public refund-status page found; stopped at Know Payment Status fields
Confidence: low; refund route UNWALKED

## Prerequisites
- PAN, and login credentials for the e-filing portal (or Aadhaar OTP login), held by the user.

## Route
1. **Home**: menu (Individual/HUF, Company, Non-Company, Tax Professionals & Others, Downloads, Help); Login / Register; scam-alert banners; cookie banner (decline non-essential if offered).
   Quick Links seen: NUDGE Campaign; e-Pay Tax; e-Verify Return; Instant e-PAN; Tax Calendar; Income & Tax Calculator; Know Tax Payment Status; Link Aadhaar/View Status; Comply to Notice; Authenticate notice/order issued by ITD; Verify PAN Status; Verify Service Request; Know Your JAO; Know TAN Details; Download CSI File; Report Account Misuse; Submit Information on Tax Evasion or Benami Property; Tax Information & Services (external).
   **No refund-status quick link.**
2. **Refund status (expected, UNWALKED):** after login (GATE: login + OTP) → e-File → Income Tax Returns → View Filed Returns → the return shows refund status. Confirm on first live run.
3. **Alternative (UNWALKED, needs lead approval, separate domain):** the Protean (formerly NSDL) TIN refund-status service. Verify the official URL before use.

## Related public page walked
**Know Tax Payment Status** (eportal.incometax.gov.in/iec/foservices/#/tin/pre-login/know-payment-status/payment-information): checks challan payment status, not refunds. Fields: PAN/TAN*, CRN*, Mobile* ("Enter Mobile Number for OTP verification", country code defaults to India). Continue → OTP (GATE). No CAPTCHA seen.

## Watch for
- Quick links jump to the eportal.incometax.gov.in subdomain: official.
- Scam banners on the home page: the department warns about fake refund messages; pair this with the status-watcher's scam triage.
- Unchecked: Individual/HUF menu and Help/FAQ may describe the refund route; check on next run.
