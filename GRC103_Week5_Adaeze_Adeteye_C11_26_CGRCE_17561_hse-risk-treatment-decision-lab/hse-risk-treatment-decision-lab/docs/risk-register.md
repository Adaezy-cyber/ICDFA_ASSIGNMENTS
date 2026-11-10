# Risk register

Likelihood and impact 1-5, multiplied. Low 1-4, Medium 5-9, High 10-16, Critical 17-25 (classroom scales). Critical cannot be accepted; High needs board escalation.

## R1 Service disruption

- **Owner:** Clinical Operations Director
- **Asset:** Booking and patient-record platform used by all three clinics
- **Threat:** Ransomware encrypts the platform, entering through a phishing attachment as at HSE (F1)
- **Weakness:** Recovery has never been tested (X3), so no one can show a backup restores
- **Business impact:** Essential bookings stop; paper fallback is a stopgap; patients are delayed or turned away
- **Initial score:** 4 x 5 = 20 (Critical)
- **Why:** Likelihood 4: the entry route is ordinary and nothing shows a restore working. Impact 5: essential bookings must continue (X5) and there is no proven fallback. Critical, so it cannot be accepted.
- **Proposed residual:** 3 x 4 = 12 (High). Credited only after the witnessed restore passes the 4-hour target. Until then I carry R1 at 20, Critical.

## R2 Sensitive-data loss

- **Owner:** Data Protection Officer
- **Asset:** Patient health and contact records
- **Threat:** Records are copied out before or during encryption, as HSE's were (F2)
- **Weakness:** Account access has never been reviewed and nothing flags bulk copying (my assumption M1)
- **Business impact:** Patient harm, a notification burden that can run for months, regulator and reputational exposure
- **Initial score:** 3 x 5 = 15 (High)
- **Why:** Likelihood 3: needs a foothold plus copying, which my controls would partly hinder once B lands. Impact 5: health data is the worst thing to lose and HSE needed over a year to notify (F2). High, so board escalation.
- **Proposed residual:** 2 x 5 = 10 (High). B, E and A lower likelihood. Without D or F nothing detects copying or limits spread, so it stays High.

## R3 Unnecessary supplier exposure

- **Owner:** IT Manager
- **Asset:** Unused supplier workflow and its connection into Northbridge systems
- **Threat:** Attacker or a compromised supplier uses a pathway nobody is watching
- **Weakness:** The workflow is enabled but unused (X2), so there is no business reason for it to exist
- **Business impact:** An avoidable foothold into the network
- **Initial score:** 4 x 3 = 12 (High)
- **Why:** Likelihood 4: it is open, idle and unwatched, so misuse would blend in. Impact 3: I cannot yet say what it reaches, so I scored the middle until the review answers that. High, so board escalation.
- **Proposed residual:** 2 x 3 = 6 (Medium). Low only once the supplier confirms removal in writing and logs show no unexplained use. Unknown legacy links stay until F's review, so I hold it at Medium.

## R4 Delayed detection

- **Owner:** IT Manager
- **Asset:** Staff mailboxes and the phishing-reporting route
- **Threat:** A phishing email or early malware sits unnoticed, as it did for about two months at HSE (F1)
- **Weakness:** Phishing reports have no escalation owner (X4)
- **Business impact:** A small compromise turns into an encryption event before anyone acts
- **Initial score:** 4 x 4 = 16 (High)
- **Why:** Likelihood 4: reports go nowhere. Impact 4: late detection converts a contained incident into R1 and R2. High, so board escalation.
- **Proposed residual:** 3 x 4 = 12 (High). E gives reports an owner and a route but no 24/7 monitoring. Still High, so I ask the board to accept it for 90 days (AC-1).

