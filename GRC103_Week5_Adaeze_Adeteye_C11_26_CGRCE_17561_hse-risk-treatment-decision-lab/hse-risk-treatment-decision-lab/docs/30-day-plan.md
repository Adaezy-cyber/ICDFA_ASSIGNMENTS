# 30-day treatment plan

Day 1 is Monday 16 November 2026; Day 30 is Tuesday 15 December 2026. The simulated board decision is Friday 13 November 2026. Option cost is shown once, on the action that starts it.

| # | Action | Option | Owner | Cost | Target | Effectiveness test |
|---|---|---|---|---|---|---|
| 1 | Name the phishing-escalation owner and publish one reporting route | E | IT Manager | $0 | Wed 18 Nov 2026 | Three seeded test reports reach the owner and are triaged within one working hour. |
| 2 | Retire the supplier workflow; supplier confirms removal in writing; review past activity logs | A | IT Manager | $5,000 | Fri 20 Nov 2026 | Outside connection to the old endpoint is refused; log review shows no unexplained use; written confirmation on file. |
| 3 | Targeted training for front-desk, booking and clinical admin staff; reporting process goes live | E | Data Protection Officer | $10,000 | Fri 27 Nov 2026 | Simulated phishing run: baseline report rate recorded, then at least 70% of target staff report within 24 hours (my target). |
| 4 | Paper-booking drill at one clinic; agree what happens after hour four | - | Clinical Operations Director | $0 | Fri 27 Nov 2026 | Timed drill shows how long paper holds and where it breaks; hour-four triage rule signed off. |
| 5 | Root-cause the failed restore, fix it, and set up protected backups | C | IT Manager | $30,000 | Fri 4 Dec 2026 | Negative test: a normal admin account cannot alter or delete the protected copy. |
| 6 | Access review: leavers, shared, dormant and supplier accounts | B | IT Manager (DPO signs off) | $35,000 | Fri 4 Dec 2026 | No dormant account over 90 days, no shared admin account; DPO samples 15 accounts. |
| 7 | Timed full restore of bookings and patient records to a clean environment, witnessed | C | Clinical Operations Director | $0 | Fri 11 Dec 2026 | Bookings usable within 4 hours, records complete to the last backup (24 hours or less), witness signs. A fail keeps R1 Critical. |
| 8 | Enforce MFA on admin, remote and email access | B | IT Manager | $0 | Tue 15 Dec 2026 | Identity report shows 100% enforcement; five sign-in attempts without the second factor all fail. |
| 9 | Board checkpoint: release the reserve and review AC-2 | G / C | Finance Director | $0 | Tue 15 Dec 2026 | Bind G only if the retest passed and the DPO has reviewed the terms; otherwise the reserve stays for recovery rework. |

Total committed $80,000; reserve $20,000 held separately.
