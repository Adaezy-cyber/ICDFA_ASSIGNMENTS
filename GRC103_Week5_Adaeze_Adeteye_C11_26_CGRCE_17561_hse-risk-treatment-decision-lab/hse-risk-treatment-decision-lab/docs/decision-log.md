# Decision log

Initial decision first, recorded before the change. Then the revision.

## Initial portfolio

| Option | Type | Cost | Decision | Reason |
|---|---|---|---|---|
| A Retire the unused supplier workflow | Avoidance | $5,000 | Selected | Removes the pathway instead of defending it. Cheapest option and the cleanest way to deal with R3. |
| B MFA rollout and account access review | Mitigation | $25,000 | Selected | Cuts credential misuse and clears dormant and supplier accounts. It is the main lever on R2. |
| C Protected backups, restoration tests and recovery plan | Mitigation | $30,000 | Selected | Only option that addresses the Critical risk. Non-negotiable. |
| D Managed detection and incident escalation service | Mitigation | $35,000 | Not selected | Valuable, but $35,000 does not fit beside B and C. Deferred, with R4 accepted for 90 days (AC-1). |
| E Targeted awareness training and reporting process | Mitigation | $10,000 | Selected | Cheapest fix for the HSE lesson: a phishing report needs an owner and a route. |
| F Network segmentation and legacy dependency review | Mitigation | $40,000 | Not selected | Largest and slowest option. Better scoped once A and B show what is connected. Year 2. |
| G Illustrative cyber insurance ($25,000 deductible; $250,000 max per covered claim) | Transfer | $20,000 | Selected | Transfer limits the money lost, not the outage. Worth buying at this price once core controls exist. |

**Total $90,000; remaining $10,000 of $100,000.**

Transfer (G) covers part of the money, not the service, and does not remove Northbridge's accountability for patient data. Insurance pays off once a covered loss exceeds the $45,000 of deductible plus premium; the $250,000 cap is used up at a $275,000 loss.

## Retained exposure under Option G

| Covered loss | Insurer payment | Retained loss | Premium | Total outlay | If excluded |
|---|---|---|---|---|---|
| $180,000 | $155,000 | $25,000 | $20,000 | $45,000 | Northbridge bears $180,000; outlay $200,000 |
| $400,000 | $250,000 | $150,000 | $20,000 | $170,000 | Northbridge bears $400,000; outlay $420,000 |

Formula: `min(max(loss - 25,000, 0), 250,000)`.

If a claim is excluded, the insurer pays nothing and Northbridge bears the whole loss plus the premium already spent ($200,000 for a $180,000 loss; $420,000 for a $400,000 loss). That falls on Northbridge's own funds and so on its board; patients carry the service consequences that no payout repairs.

## Revised decision after the change

| Item | Initial | Revised |
|---|---|---|
| Trigger | Assumption set in the brief. | Restoration test fails; paper bookings hold for four hours; B rises to $35,000. |
| Portfolio | A, B, C, E, G = $90,000. Reserve $10,000. | A, B, C, E = $80,000. Reserve $20,000. |
| What changed | - | B +$10,000. G removed from year-1 spend. Reserve doubled and ring-fenced. C's first task is to fix the failed restore. Paper drill added at no cost. |
| Deferred | D, F. | G (to 15 Dec gate), D (to 12 Feb 2027 review), F (year 2). |
| Remaining risk owners | R1 Clinical Operations Director; R2 DPO; R3 IT Manager; R4 IT Manager. | Unchanged. R1 now has evidence behind it rather than an assumption. |
| Needs escalation | R2, R3, R4 (High) and R1 (Critical). | Whether the Board will run for up to 30 days on a known 4-hour continuity limit with the financial tail unfunded (AC-2). Chair of the Board Risk Committee decides. |

Revised spend $80,000; reserve $20,000.

**Why G goes, not something else.** I dropped G because a payout arrives after the outage and cannot restore a booking, and four hours of paper is the number that now drives everything. The $20,000 reserve equals the premium: it pays for recovery rework first, and buys insurance at the 15 December gate only if the retest passes. I also do not want to apply for cover while my own test says recovery fails (M4).

| Option | Revised cost | Revised decision | Reason |
|---|---|---|---|
| A | $5,000 | Selected | Unchanged. Still the best value per dollar. |
| B | $35,000 | Selected | Price rose $10,000. I kept it: nothing else funded here reduces R2 likelihood, and D cannot fit beside C. |
| C | $30,000 | Selected | Kept, but its first job is now to fix why the test failed, then re-test. |
| D | $35,000 | Deferred | Still deferred. Revisit 12 February 2027. |
| E | $10,000 | Selected | Unchanged. |
| F | $40,000 | Deferred | Still deferred to year 2. |
| G | $20,000 | Deferred | Deferred to the 15 December gate. A payout cannot reopen a clinic, and the $20,000 now covers recovery rework. |

## Time-limited acceptances

| ID | What | Owner | Expiry | Review trigger | Simulated approver |
|---|---|---|---|---|---|
| AC-1 | Accept residual R4 (delayed detection, High, 12) while D is deferred. Initial and revised portfolios. | IT Manager | Fri 12 Feb 2027 | Any phishing report not triaged within one working hour; a failed reporting drill; a suspected compromise; or an insurer or regulator asking for 24/7 monitoring. | Chair, Board Risk Committee (simulated) |
| AC-2 | Temporary retention of the unfunded financial tail while G is deferred (revised portfolio only). This is not acceptance of R1, which stays Critical and under treatment. | Finance Director | Tue 15 Dec 2026 | Restore retest result on 11 December; insurer terms reviewed by the DPO; any confirmed incident before the gate. | Chair, Board Risk Committee (simulated) |
