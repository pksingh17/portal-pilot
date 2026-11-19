# Verifying that a body or portal is legitimate

A route is only as good as its weakest link. Scammers copy government portals, buy search ads for fake helplines, and dress paid middlemen up as official services. Every body and URL on a route card must pass these checks.

## 1. Official domain

Strong signals by country (check the exact domain, not just that the string appears somewhere in the URL):

| Country | Official patterns | Notes |
|---|---|---|
| India | `.gov.in`, `.nic.in`, regulator domains (`rbi.org.in`, `irdai.gov.in`, `sebi.gov.in`, `trai.gov.in`), PSU domains (`irctc.co.in`, `indianrail.gov.in`) | Some official bodies use `.org.in` or `.co.in`; confirm via a second source |
| United States | `.gov`, `.mil` | Only verified US government entities can register `.gov`; state sites also use `.gov` (e.g. `ca.gov`) |
| United Kingdom | `.gov.uk`, `.nhs.uk`, `.police.uk`; regulators like `financial-ombudsman.org.uk` | Independent ombudsmen often use `.org.uk`: confirm via gov.uk |
| EU | `europa.eu`; national domains vary | EU-wide ODR platform closed 20 July 2025: don't route users there |
| Others | Government second-level domains (`.gov.au`, `.gc.ca`/`canada.ca`, `.gov.sg`, `.go.jp`, `.gob.mx`, etc.) | Confirm via the national government directory |

## 2. Second source

Confirm each body through one of:
- The national government directory (india.gov.in, usa.gov agency index, gov.uk organisations list, europa.eu).
- The parent ministry or regulator's own site linking to it.
- The organisation's own official site naming it (e.g. a bank's grievance page naming the RBI Ombudsman).

Aggregators, legal blogs, forums and news articles are leads. They can point to a body; they can't prove it's real or current.

## 3. Red flags (any one = UNCONFIRMED, warn the user)

- Phone numbers found only in search ads or on non-official sites.
- Sites charging a fee for a service the official portal provides free (unless clearly labelled as a private service).
- Look-alike domains: extra words (`-refund`, `-support`, `-helpdesk`), hyphens, misspellings, `.com` versions of `.gov` bodies.
- Requests for OTPs, PINs or passwords outside the official login flow; requests to install remote-access apps.
- Payment to personal UPI IDs or wallets.

## 4. Currency

Bodies merge, rename and close (e-Daakhil became e-Jagriti; NSDL e-Gov became Protean; the EU ODR platform shut down). Prefer pages updated recently, and mark the check date on every route card.
