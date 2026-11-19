# Rail Madad: lodge a railway complaint
Official URL: https://railmadad.indianrailways.gov.in (redirects to /madad/final/home.jsp)
Last walked: 2 November 2026 (operator test run, no data)   Result: stopped at mobile number + Get OTP
Confidence: medium for form layout; categories UNWALKED (behind OTP)

## Prerequisites
- Mobile number that can receive an OTP.
- For train complaints: PNR (or UTS ticket number for unreserved).
- Incident date; optional photo/video/PDF evidence (PDF, JPG, JPEG, PNG, MP4, up to 5 MB).

## Route
1. **Home**: complaint panel on the right with tabs (same URL, anchors): TRAIN `#traincomp` (default), STATION `#stationcomp`, APPRECIATION/RAIL ANUBHAV `#railanubh`, TRACK YOUR CONCERN `#track`, SUGGESTIONS `#suggestions`. 24-language dropdown in header. Helpline 139 linked.
2. **TRAIN tab**: Mobile No. + **Get OTP** (GATE: OTP — user enters their number and the OTP). Then Journey Details (PNR / UTS), PNR No, Grievance Description (voice input available), Proceed, Incident Date (calendar; arrives pre-filled — check it), Upload File.
3. **STATION tab**: Mobile No.* + Get OTP (GATE), Complaint Description*, Type* and Sub Type* (dependent dropdowns, not readable before OTP), Incident Date*, Upload File, Submit (GATE: user clicks).
4. UNWALKED: post-OTP category options, confirmation page and reference number format.

## Field map
| Portal field | Field sheet key | Notes |
|---|---|---|
| Mobile No. | user_mobile | User types it; OTP gate follows |
| Journey Details | ticket_type | PNR or UTS |
| PNR No | pnr | 10 digits (standard PNR length; not shown on page) |
| Description | complaint_text | Disallowed characters: ! @ # $ ^ : ; & + = ₹ ÷ , * % " — rewrite to avoid them (e.g. "Rs" not "₹", no commas) |
| Incident Date | incident_date | Pre-filled; always verify the value, may show a wrong year |
| Upload File | evidence | PDF/JPG/JPEG/PNG/MP4, max 5 MB |

## Text rules
- Description: banned `!@#$^:;&+=₹÷,*%"` (length limit not shown on page)
  Check: `textcheck.py draft.txt --banned '!@#$^:;&+=₹÷,*%"'`

## Judgment calls seen
- Train vs Station tab: on-train issues (coach, AC, catering, staff on train) → TRAIN; station facilities → STATION.
- Refund disputes are better routed via IRCTC TDR / eQuery (see grievance-agent railway section); Rail Madad suits service complaints and stalled refunds as a parallel route.

## Errors and fixes
- None seen.

## Watch for
- Clicking the Appreciation or Suggestions tab can pop a "Complainant Login" modal (User Id, Password, CAPTCHA, OTP, Guest User). Close it with X; complaints don't need an account.
- Category dropdowns stay hidden until OTP verification.
- The description's banned characters include the comma — easy to trip on.
