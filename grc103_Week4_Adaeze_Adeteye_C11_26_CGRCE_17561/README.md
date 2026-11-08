# GRC103 Module 3: Technical Risk Treatment Lab

**Course:** International Cybersecurity and Digital Forensics Academy (ICDFA), GRC103 Risk Assessment and Management Techniques   
**Scenario:** Northbridge Services (fictional organisation)   
**Author:** Adaeze Elizabeth Adeteye     
**Status as of 8 November 2026:** Partially complete. The hands-on server tasks were **not performed**

---

## Important: limitation affecting this submission

I was unable to download the Ubuntu Server 24.04 LTS image because the free storage on my device is limited and could not hold the ISO and the virtual machine disks the lab requires. As a result, I could not build the Ubuntu and Kali lab environment, and **I have not run any of the lab commands**.

Because of this:

- **No command outputs, screenshots, logs, hashes or timestamps are included**, and none have been created or simulated. The brief states that marks depend on evidenced results, and I do not want to present anything as evidence that I did not actually collect.
- Every technical step (Steps 1 to 10) is marked **Not performed** in the evidence map below.
- Controls are described as **designed but untested**. Nothing in this repository claims that a control works, blocks traffic, logs events or restores service.
- The analysis that does not depend on running the VMs (risk register design, treatment decisions, monitoring proposal, cost comparison and the illustrative ALE calculation) is included, and its assumptions are stated.

I am requesting guidance from my course contact on whether an alternative is available (for example a pre-built VM image, a lab machine, or additional time). If the environment becomes available, I will complete the technical steps and add real evidence to this repository, updating the status table as each step is done.

---

## What this lab asks for

The brief asks me to act as a GRC analyst and technical control implementer, to:

1. Build a local two-VM lab (Ubuntu Server 24.04 LTS and Kali Linux) on an isolated network.
2. Collect baseline evidence, and create a risk register (R1 to R4).
3. Apply **avoidance** by retiring an unnecessary legacy service.
4. Apply **mitigation** by removing archive publication and restricting access with UFW.
5. Validate **detection** (log correlation) and **correction** (backup and restore of a deleted dummy file).
6. Model **transfer** and **acceptance**, and compare costs and remaining risk.

---

## Baseline risk register (proposed, not evidence-based)

The brief's scale is used: likelihood 1 to 5, impact 1 to 5, score = likelihood x impact. Bands: 1 to 4 Low, 5 to 9 Medium, 10 to 16 High, 17 to 25 Critical. These are classroom thresholds, not an external standard. Scores are ordinal and are not monetary values or probabilities.

The values below are my **analyst estimates based on the lab design described in the brief**. They have **not** been confirmed by baseline scans, because the baseline was not collected.

| ID | Asset | Threat event | Observed weakness | Impact | Likelihood | Score | Band | Evidence reference | Owner (simulated) |
|---|---|---|---|---|---|---|---|---|---|
| R1 | Legacy HTTP endpoint (port 8080) | Unauthorised access to an unneeded service | Unnecessary service listening on all interfaces (expected from design; not observed) | 3 | 4 | 12 | High | Pending: `baseline-ports.txt`, `baseline-legacy.txt` | Service owner |
| R2 | Archive of dummy records | Unauthorised retrieval of files | Directory listing and direct file access enabled (expected from design; not observed) | 4 | 4 | 16 | High | Pending: `baseline-listing.txt`, `baseline-file.txt` | Application owner |
| R3 | Document server network exposure | Unauthorised network access | No source restriction on inbound traffic (expected from design; not observed) | 4 | 3 | 12 | High | Pending: `ufw status verbose`, `ss -lntp` output | Infrastructure owner |
| R4 | Approved portal content | Loss or deletion of content | No tested backup or restore process | 3 | 3 | 9 | Medium | Pending: recovery test evidence | Service owner |

**Residual risk (R1 to R4):** Not assessed. Residual likelihood, impact and score depend on tested control outcomes, and no tests were run. Every control is therefore marked **untested**, not effective.

---

## Treatment decisions

### Avoidance: retire the unused legacy endpoint (R1)

- **Proposed change:** Disable the `grc-legacy` service and retain the approved portal.
- **Business impact:** None expected, since the endpoint is unused and holds only dummy data. To be confirmed by test.
- **Approval role:** Service owner. Approval is simulated.
- **Test:** Rescan ports 80 and 8080 from Kali; port 8080 should no longer respond while port 80 still serves the portal.
- **Rollback:** `sudo systemctl enable --now grc-legacy`, then reapply the treatment and leave the endpoint disabled.
- **Why this does not eliminate all risk:** Retiring the legacy workflow removes the exposure created by that service only. The remaining web service, its configuration, access controls and data still carry risk (R2, R3, R4).
- **Result:** Not performed.

### Mitigation: archive hardening and firewall restriction (R2, R3)

- **Design:** Move the archive outside the web root, restrict permissions, deny the old URL in Nginx, and use UFW to allow only the approved Kali address to reach port 80.
- **Note on listing versus file access:** Turning directory listing off only stops people from browsing a directory. If the file is still inside the web root, anyone who knows or guesses its path can still request it directly. Moving the file out of the web root and denying the path is what removes publication.
- **Result:** Not performed. Expected outcomes (200 for `/public/`, 403 for `/`, `/archive/` and the file, and a timeout for an unapproved source) are what the brief predicts. They are **not observed results**.

### Detection: log correlation

- **Design:** Compare Nginx access logs with UFW kernel block events.
- **Expected behaviour:** Requests permitted by the firewall appear in the Nginx log. Requests blocked by UFW are dropped before reaching Nginx and should therefore not appear there, but may appear as `UFW BLOCK` entries (firewall logging can be rate-limited).
- **Result:** Not performed. Any control I cannot verify would be recorded as **unverified**, not as failed.

### Correction: backup and restore (R4)

- **Design:** Create a protected archive of the portal directory and a SHA-256 hash, delete the file, confirm the service check fails, restore, verify the hash and confirm the service again.
- **Limitation of a same-host backup:** It helps with accidental deletion in this exercise, but it does not protect against loss of the whole host, disk failure or compromise of the server.
- **Recovery time:** Not measured.

### Transfer (fictional managed-backup offer)

Comparison: $120 setup plus $20 per month, against local-only backup.

| Item | Position |
|---|---|
| Provider duties | Store backups offsite, keep the service available, retain backup data for the agreed period, report failed backups |
| Retained customer duties | Decide what is backed up, protect credentials, perform restoration tests, keep evidence, remain responsible for the data |
| Restoration-test requirement | A restore is tested at least quarterly and after any significant change, with the result recorded |
| Evidence retention | Backup job logs and restoration-test records kept for a defined period (proposed: 12 months) |
| Service limitation | The provider is not responsible for data that was never backed up or for errors caused by the customer |

**Draft service clause (proposed):** *"The Provider shall perform scheduled backups of the Customer's designated portal content, store them offsite and notify the Customer of any failed job within one business day. The Customer remains responsible for selecting the content to be backed up, safeguarding access credentials and verifying restoration at least quarterly. The Provider's obligations apply only to content included in the backup scope."*

A contract or service does not remove the technical risk. The customer must still test restoration and keep control of the data.

### Acceptance (plain HTTP on the isolated lab network, dummy data only)

| Field | Entry |
|---|---|
| Owner | Service owner (simulated) |
| Proposed residual risk score | Likelihood 2 x Impact 2 = 4 (Low). *Analyst estimate, not tested.* |
| Rationale | Isolated host-only network, fictional data, no external connectivity |
| Proposed expiry | 14 days from approval |
| Review date | Day 14, or earlier if a trigger occurs |
| Triggers for re-evaluation | Any real data, any external connectivity or bridged networking, wider user access, or use beyond the lab |
| Approval | **Simulated** |

If any trigger occurs, the acceptance lapses and the matter should be escalated or treated (for example by deploying TLS) rather than accepted.

---

## Monitoring plan (proposed; no measured results)

These are **proposals for ongoing operation**, not results from the lab.

| Check | Owner (simulated) | Frequency | Threshold | Escalation |
|---|---|---|---|---|
| Approved portal availability | Service owner | Every 5 minutes (automated) | Any failed check for more than 15 minutes | Notify service owner, then infrastructure lead if unresolved after 1 hour |
| Unexpected open ports | Infrastructure owner | Daily scan | Any port open other than 80 | Treat as an incident and review within 4 hours |
| Recovery-test success | Service owner | Quarterly | Restore fails or hash does not match | Fix the backup process and retest within 5 working days |
| Configuration drift: retired legacy service | Infrastructure owner | Daily | `grc-legacy` active, enabled or listening on 8080 | Disable it, record the change and investigate how it returned |

---

## Cost comparison (fictional figures from the brief)

First-year cost = setup + labour + annual recurring cost.

| Option | Calculation | First-year cost |
|---|---|---|
| A: Hardening work | 4 hours x $25 + $50 annual maintenance | **$150** |
| B: Managed backup | $120 setup + ($20 x 12 months) | **$360** |
| C: TLS deployment | 3 hours x $25 + $25 annual maintenance | **$100** |

**Excluded costs:** staff time beyond the stated hours, training, hardware or hosting, monitoring tools, incident costs, downtime, and later contract renewal.

**Provisional recommendation:** Options A and C address the technical weaknesses identified (exposure and plain-text transport) at a combined first-year cost of **$250**. Option B is justified by the illustrative ALE below and by the limitations of a same-host backup, giving **$610** if all three are adopted. This recommendation is provisional because the technical results needed to confirm it were not collected.

### Illustrative ALE for option B (separate scenario, all figures are assumptions)

| Item | Calculation | Value |
|---|---|---|
| Annual rate of occurrence (assumption) | 0.2 | 0.2 per year |
| Loss per event, baseline (assumption) | $5,000 | $5,000 |
| Baseline ALE | 0.2 x $5,000 | **$1,000** |
| Loss per event with tested recovery (assumption) | $1,000 | $1,000 |
| Residual ALE | 0.2 x $1,000 | **$200** |
| Annual benefit | $1,000 - $200 | **$800** |
| First-year net benefit of option B | $800 - $360 | **$440** |

These figures are assumptions given in the brief. A recovery test, had it been run, would not establish them. Benefits from the options are not summed, and the ordinal risk scores above are not converted into dollars.

---

## Completion plan (if a lab environment becomes available)

1. Obtain Ubuntu Server 24.04 LTS and Kali Linux, using external storage if needed, and take a clean checkpoint of each VM.
2. Run Steps 1 to 10 in order, saving every output with its timestamp.
3. Update the status table, replace "pending" evidence references with real file names, and add a residual risk reassessment based on the actual results.
4. Add the evidence table (test ID, source IP, service, expected outcome, actual outcome, timestamp, log reference).

```

The `evidence/` and `screenshots/` folders hold no results because none exist. Files from the `reference-design/` folder are the intended design only and must not be read as proof that any control works.

---

## Honesty and scope notes

- All data in the lab design is fictional. No real data, passwords or private keys are used or included.
- The approvals referred to above are **simulated** for the exercise.
- Estimated scores and costs are classroom values and assumptions, not measurements.
