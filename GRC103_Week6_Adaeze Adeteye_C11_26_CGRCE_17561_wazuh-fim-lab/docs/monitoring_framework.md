# Control Design and Monitoring Framework

**Control:** File integrity monitoring (FIM) of the financial forecast folder using Wazuh   
**Control type:** Detective |      
**Risk addressed:** Unauthorised modification or deletion of sensitive financial forecast documents

## 1. Control objective and scope

Detect, within minutes, any creation, modification, deletion or renaming of files in the monitored folder on the finance workstation, record the event centrally with tamper-resistant evidence, and trigger investigation when the change is not authorised.

- **In scope:** `C:\Users\<user>\SensitiveFiles` on the finance workstation (agent `Finance-Dept-Workstation`).
- **Out of scope:** Other endpoints, network file shares and cloud storage (future extension).

## 2. RACI

| Activity | Finance user | IT Security | GRC / Risk | Management |
| --- | --- | --- | --- | --- |
| Maintain monitored-folder list and agent | I | R/A | C | I |
| Review and triage FIM alerts | I | R | C | I |
| Approve planned changes to forecast files | R | C | A | I |
| Investigate unauthorised changes | C | R | A | I |
| Report control metrics | I | R | A | I |
| Accept residual risk | I | C | R | A |

R = Responsible, A = Accountable, C = Consulted, I = Informed.

## 3. Metrics (key risk and control indicators)

| Metric | Formula | Green | Amber | Red | Frequency |
| --- | --- | --- | --- | --- | --- |
| Agent coverage | Active in-scope agents / total in-scope agents x 100 | 100% | 95-99% | < 95% | Weekly |
| Unauthorised change rate | Alerts with no matching approved change / total FIM alerts x 100 | 0-5% | 6-15% | > 15% | Monthly |
| Mean time to detect (MTTD) | Alert time minus file event time | < 5 min | 5-15 min | > 15 min | Monthly |
| Mean time to respond (MTTR) | Case closed time minus alert time | < 4 h | 4-24 h | > 24 h | Monthly |
| Alert backlog | Open FIM alerts older than 24 h | 0 | 1-3 | > 3 | Weekly |

Thresholds are proposed starting values to be agreed with management and tuned after the first quarter of data.

## 4. Alert triage and escalation runbook

1. **Receive alert:** Wazuh raises a `syscheck` event (added, modified, deleted) for the monitored path.
2. **Check against the change log:** Does the user, time and file match an approved change?
   - **Yes:** Close as authorised, record the change reference.
   - **No or unknown:** Continue.
3. **Assess severity:**
   - Deletion or modification of a forecast file outside business hours, or by an unusual account: **High**.
   - Modification during business hours by the file owner, no change record: **Medium**.
   - New file added with no sensitive content: **Low**.
4. **Contain (High):** Isolate the workstation from the network, disable or reset the account, preserve the Wazuh alert and checksums as evidence.
5. **Recover:** Restore the file from the latest clean backup or version history and verify the checksum.
6. **Investigate:** Establish root cause (insider, compromised account, malware, process failure).
7. **Report and improve:** Update the risk register, record lessons learned, adjust preventive controls (for example tighter permissions).

## 5. Audit evidence procedure

To show that a sensitive file was not altered during a period:

1. Open the file integrity monitoring view for the agent.
2. Set the audit period and filter by `syscheck.path`.
3. Confirm there are no unapproved modified or deleted events, and that each approved change matches a change record.
4. Confirm the agent was Active for the whole period (so a lack of alerts is meaningful).
5. Export or screenshot the results, add the date and the name of the person who ran the query, and file them in the audit evidence folder.

## 6. Control limitations and residual risk

- FIM detects changes after they happen. It does not prevent them, so it must be paired with least-privilege access and backups.
- It only covers the configured folder and an active agent. If the agent is stopped, there is a monitoring gap, which is why agent coverage is a reported metric.
- Alerts are only useful if someone reviews them, so triage ownership and response times are part of the control.
- A user with administrator rights on the endpoint could stop the agent or change its configuration, so agent tampering should itself be alerted on.
- **Residual risk:** Reduced from medium-high to **low-medium** once preventive controls and a reviewed alert process are in place, subject to management acceptance.
