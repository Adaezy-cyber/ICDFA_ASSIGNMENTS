# Comparison of Simulated Environment to the Equifax Data Breach

## Overview

This report compares the security governance failures identified in the simulated environment (`security_governance_lab`) to the failures that contributed to the Equifax data breach disclosed in September 2017.

## Key Governance Failures in the Equifax Breach

1. **Patch Management Failure** — Equifax did not patch a known, publicly disclosed vulnerability in Apache Struts (CVE-2017-5638 / S2-045) for roughly two months after Apache released a fix and the US-CERT advisory was issued.
2. **Security Monitoring Failure** — The intrusion was not detected for approximately 76 days, in part because an SSL inspection device had an expired certificate that silently stopped decrypting monitored traffic.
3. **Network Segmentation Failure** — Once inside, attackers moved laterally across roughly 51 unrelated databases, indicating the environment was not segmented along data-sensitivity lines.
4. **Leadership and Accountability Failure** — A US House Oversight Committee investigation found unclear ownership of the patch, and no single named individual was accountable for confirming remediation.
5. **Policy Implementation Failure** — Equifax had a documented patch management policy with a 48-hour SLA for critical vulnerabilities, but the policy was not enforced against the affected system.

## Comparison with the Simulated Environment

| Governance Failure | Equifax | Simulated Environment | Similarity |
|---|---|---|---|
| Patch Management | Known Struts CVE unpatched for ~2 months | `docker-compose.yml` deploys a deliberately unpatched `vulhub/struts2` image; `patch_status.json` shows `struts_patched: false` until Part 3 | High |
| Security Monitoring | Breach undetected for 76 days (failed SSL inspection) | No monitoring container is configured to alert by default; `monitoring_server` only runs `tail -f /dev/null` until Part 3 adds `security_monitor.sh` | High |
| Network Segmentation | Lateral movement across ~51 databases | `web_server` and `database_server` share a single flat `secgov_network` bridge with no access-control rules | High |
| Authentication | Some internal systems used default/weak credentials | `database_server` is seeded with `MYSQL_ROOT_PASSWORD: password` and an `app_user`/`app_password` pair | Medium |
| Policy Implementation | 48-hour patch SLA existed but was not enforced | `governance_tracker.py` baseline shows a Patch Management Policy (`POL-001`) and a Patch Compliance metric sitting at 85% against a 95% target — the policy exists but is not yet met | High |
| Metrics and Measurement | Vulnerability scan results were reportedly not escalated to the people who could act on them | Baseline governance dashboard metrics are recorded but, before Part 3, are not tied to an enforcement or escalation workflow | Medium |

## Lessons Learned

Both cases show that having a patch management **policy** is not the same as having a patch management **control**. Equifax's 48-hour SLA and the lab's `POL-001` both existed on paper; neither prevented the underlying system from staying vulnerable, because nothing in the process verified compliance and escalated when it was missed. The second shared lesson is about monitoring: a vulnerability that is never detected being exploited produces no incident record and no pressure to fix it, which is why both environments show "quiet" systems with no incident history before the compromise is simulated. Finally, flat networking turns a single compromised component into full data exposure — in Equifax's case, dozens of databases; in the simulated case, the entire `customer_data` table is reachable the moment the web tier is compromised, because nothing stands between the two containers on `secgov_network`.

## Conclusion

The simulated environment reproduces the structural governance conditions behind the Equifax breach — an unpatched known CVE, a flat network, weak database authentication, and metrics/policies that exist without enforcement — rather than merely reproducing the technical exploit. Part 3 of this assessment implements controls against each of these specific gaps and Part 4 builds the metrics and reporting layer that was functionally absent in both cases.
