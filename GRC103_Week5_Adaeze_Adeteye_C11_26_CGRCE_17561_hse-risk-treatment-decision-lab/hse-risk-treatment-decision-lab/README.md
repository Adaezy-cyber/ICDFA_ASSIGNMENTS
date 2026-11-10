# HSE ransomware risk treatment decision lab

GRC103 | Module 3 Risk Treatment Strategies | Lab 2, International Cybersecurity and Digital Forensics Academy (ICDFA).

**Author:** Adaeze Elizabeth Adeteye  
**Registration number:** [ADD REGISTRATION NUMBER]  
**Source:** Health Service Executive, Cyber-attack and HSE response; last reviewed 1 December 2025; accessed 18 October 2026. <https://www2.hse.ie/services/cyber-attack/what-happened/>

## What this is

My advice to Northbridge Community Health, a fictional three-clinic provider, on spending a $100,000 first-year budget after the 2021 HSE ransomware attack. The brief gave me seven treatment options (A to G) and one rule I took seriously: do not count a control as working until it has been tested.

## Where to look

| What | Link |
|---|---|
| Report (PDF, 3 pages) | [report/GRC103_Lab2_HSE_Risk_Treatment_Report.pdf](report/GRC103_Lab2_HSE_Risk_Treatment_Report.pdf) |
| Report (editable Word) | [report/GRC103_Lab2_HSE_Risk_Treatment_Report.docx](report/GRC103_Lab2_HSE_Risk_Treatment_Report.docx) |
| Workbook: register, budget, insurance, decision log, plan | [workbook/Northbridge_Risk_Treatment_Workbook.xlsx](workbook/Northbridge_Risk_Treatment_Workbook.xlsx) |
| Real facts vs assumptions | [docs/facts-vs-assumptions.md](docs/facts-vs-assumptions.md) |
| Risk register | [docs/risk-register.md](docs/risk-register.md) |
| Initial and revised decisions, insurance maths, acceptances | [docs/decision-log.md](docs/decision-log.md) |
| 30-day plan | [docs/30-day-plan.md](docs/30-day-plan.md) |
| Board memo (243 words) | [docs/board-memo.md](docs/board-memo.md) |

## Where I landed

- **Initial portfolio:** A, B, C, E and G for $90,000, with $10,000 unallocated. I put C (protected backups and tested recovery) first because it is the only option that answers the Critical risk, R1 service disruption (20).
- **After the change** (restoration test fails, paper bookings hold four hours, B rises to $35,000): A, B, C and E for $80,000 and a ring-fenced $20,000 reserve. I dropped insurance (G). A payout arrives after the outage and cannot reopen a clinic; the reserve equals the premium, so it fixes recovery first and buys cover at the 15 December gate only if the retest passes.
- **Insurance maths:** a $180,000 covered loss means the insurer pays $155,000 and I retain $25,000, so first-year outlay is $45,000 with the premium. At $400,000 the $250,000 cap bites: retained $150,000, outlay $170,000. The cap is used up at a $275,000 loss.
- **Still High after treatment:** R2 data loss (10) and R4 delayed detection (12). R4 is the one I ask the board to accept for 90 days, to 12 February 2027, with the IT Manager as owner. R1 is not accepted.
- **Escalation:** whether the board will run for up to 30 days on a known four-hour continuity limit with the financial tail unfunded.

## Real vs fictional

Only two facts come from the real incident: the March 2021 phishing email that led to ransomware in May 2021, and the copying of data that led HSE to notify 90,000 people from November 2022. Northbridge, the budget, option prices, policy terms and the changed circumstances are classroom assumptions. The few extra assumptions I had to make myself are labelled M1 to M6 in [docs/facts-vs-assumptions.md](docs/facts-vs-assumptions.md), including that a four-hour recovery target for bookings is mine, not the brief's.

## Limits of this work

- Scores are classroom scales applied by judgement. Nothing here is measured.
- Owners and the approver are role titles, not people.
- The residual scores are proposals. Each is credited only once its test in the 30-day plan passes.
- No technical testing was done, and none was required.
