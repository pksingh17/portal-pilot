# RTI Online: submit an RTI request (Central Government)
Official URL: https://rtionline.gov.in
Last walked: 2 November 2026 (operator test run, no data)   Result: stopped at guidelines checkbox
Confidence: high for guidelines; form UNWALKED

## Prerequisites
- Indian citizen; request addressed to a Ministry/Department/public authority of the **Central Government**. State bodies are not on this portal ("should not be filed for other Public authorities under State Govt.").
- Request text ready: max **3,000 characters**; longer text goes as a PDF attachment in "Supporting document".
- Fee as prescribed under RTI Rules, 2012 (the page prints no amount; ₹10 under those rules: confirm at payment). BPL applicants pay nothing but must attach the BPL certificate.
- Mobile number for SMS alerts.

## Route
1. **Home**: nav: Submit Request, Submit First Appeal, View Status, FAQ. Payment: internet banking, Visa/Mastercard debit/credit, RuPay, UPI.
   → Click **Submit Request**.
2. **Guidelines** (/guidelines.php?request&&pageid=<token>): rules for use; checkbox "I have read and understood the above guidelines." and a submit button.
   GATE: guidelines checkbox — user reads and ticks.
   → Submit (user, after ticking).
3. UNWALKED: request form (fields marked * are mandatory) → **Make Payment** (GATE: payment) → submit (GATE) → registration number issued.

## Field map
| Portal field | Field sheet key | Notes |
|---|---|---|
| Request text | rti_text | ≤3,000 chars; allowed characters only: A-Z a-z 0-9 , . - _ ( ) / @ : & ? \ % |
| Supporting document | rti_attachment | PDF; no spaces in file name; never upload Aadhaar/PAN/other ID (BPL card only) |
| Public authority | ministry | Central only |
| Mobile | user_mobile | For SMS alerts |

## Text rules
- Request text: max 3000 characters; allowed `A-Za-z0-9 ,.\-_()/@:&?\\%`
  Check: `textcheck.py draft.txt --max 3000 --allowed 'A-Za-z0-9 ,.\-_()/@:&?\\%'`

## Judgment calls seen
- Central vs State authority: check before drafting; state RTIs go to the state's own portal or by post.
- Drafting: ask for records/information, not opinions or explanations; one subject per application works best.

## Errors and fixes
- Paid but no registration number: wait 24–48 working hours for reconciliation, **don't pay again**, then email helprtionline-dopt[at]nic[dot]in with transaction details.

## Watch for
- Interactive accessibility tree came back empty: use text search (`find`) to locate the checkbox and buttons.
- The CPIO may ask for additional fees later via the portal; shows in View Status and email.
- First appeal: free, needs the original registration number, via "Submit First Appeal".
