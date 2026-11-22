# GRC103 Lab Report: Practical Risk Monitoring with Wazuh

**Course:** GRC103: Risk Assessment and Management Techniques   
**Module:** Practical Risk Assessment Workshop    
**Student:** Adaeze Elizabeth Adeteye    
**Registration number:** C11/26/CGRCE/17561

## Repository contents

| Path | What it is |
| --- | --- |
| `README.md` | This report: scenario, design, procedure, analysis answers |
| `docs/deployment_steps.md` | Step-by-step deployment and verification guide |
| `docs/troubleshooting.md` | Common problems and fixes |
| `docs/execution_log_and_challenges.md` | What was attempted, what blocked the live deployment, and the corrective actions |
| `docs/monitoring_framework.md` | Metrics, thresholds, alert triage runbook and audit-evidence procedure for the control |
| `config/ossec_syscheck_snippet.xml` | The FIM configuration line for the Windows agent |
| `scripts/01_install_wazuh_manager.sh` | Manager install commands (Ubuntu) |
| `scripts/02_register_agent_on_manager.sh` | Agent registration helper (Ubuntu) |
| `scripts/03_simulate_risk_event.ps1` | Creates, modifies and deletes the test file and logs the times |
| `scripts/04_fallback_fim_watcher.ps1` | Fallback watcher, only if Wazuh cannot be installed |
| `evidence/` | Evidence checklist and a folder for screenshots |

## 1. Purpose and Scope

This report documents the design of a detective control for the risk of unauthorised modification or deletion of sensitive financial forecast documents, using the open-source Wazuh platform for file integrity monitoring (FIM). It then answers the GRC workshop questions, linking the control to risk identification, treatment, monitoring and compliance.

> **Statement of limitations.** I was unable to complete the live deployment of this lab because I could not get the Ubuntu Server (Wazuh manager) virtual machine into a usable state. Windows Smart App Control blocked a downloaded file, I could not recover the VM's login credentials, and the VM booted without a network connection despite several attempts to get it done. Another attempt to redownload ends up in low storage (see `docs/execution_log_and_challenges.md`). As a result, Wazuh was **not installed**, no agent was registered, and no alerts were generated. The deployment steps below are the documented implementation procedure, and the results in Section 5 describe what the control is expected to produce. No alerts, screenshots or dashboard outputs are presented as observed results. `evidence/README.md` lists the evidence to capture on a successful run; those items are marked "Not captured". To compensate, I have added a complete control design and monitoring framework (`docs/monitoring_framework.md`) so the GRC content of the lab is still covered.

## 2. Scenario and Risk Statement

A recent risk assessment rated the unauthorised modification or deletion of sensitive financial forecast documents as a medium-to-high risk. The approved Risk Treatment Plan selected a detective control to monitor a designated folder on a key user's workstation.

| Element | Description |
| --- | --- |
| Asset | Financial forecast documents held in a SensitiveFiles folder on a finance workstation |
| Threat | Malicious insider, careless user, or malware altering or deleting files |
| Vulnerability | Files can be changed or removed without any central record |
| Risk | Unauthorised modification or deletion leading to inaccurate forecasts, data loss and compliance failure |
| Treatment | Reduce, through a detective control (FIM) that creates an audit trail and real-time alerts |
| Control owner | IT Security / GRC function |

## 3. Lab Architecture

| Component | Host | GRC role |
| --- | --- | --- |
| Wazuh Manager | Ubuntu Server in VirtualBox (bridged adapter) | Risk monitoring platform: aggregates and analyses events for reporting |
| Wazuh Agent | Windows host machine | Control agent installed on the monitored endpoint |

The Ubuntu VM uses a bridged adapter so it sits on the same network as the Windows host and the agent can reach the manager. Recommended VM sizing for the all-in-one installation: at least 4 GB RAM, 2 CPUs and about 30 GB disk.

## 4. Implementation Procedure (Planned)

Full detail is in [`docs/deployment_steps.md`](docs/deployment_steps.md). Summary:

1. **Deploy the manager** on Ubuntu with `scripts/01_install_wazuh_manager.sh`, and record the admin credentials printed at the end. GRC note: in production the indexer, server and dashboard would be separated, which removes a single point of failure and acts as a compensating control for availability risk.
2. **Open the dashboard** at `https://<VM_IP>` (the certificate warning is expected in a lab). It is the risk and control monitoring console.
3. **Install and register the Windows agent** (version 4.12.x, matching the manager) using `manage_agents` on the manager to generate a key, then pasting the key and manager IP into Wazuh Agent Manager.
4. **Configure the detective control.** Create `C:\Users\<YourName>\SensitiveFiles` first, then add the `<directories realtime="yes">` line from `config/ossec_syscheck_snippet.xml` inside the `<syscheck>` block of `ossec.conf` and restart the agent. Real-time mode makes the agent report changes as they happen instead of waiting for a scheduled scan.
5. **Verify** by running `scripts/03_simulate_risk_event.ps1` (create, modify, delete `Q4_Financial_Forecast.docx`), then filtering the dashboard with `rule.groups: syscheck`.

## 5. Expected Results

These describe what the control is designed to produce. They are expectations, not observations.

| Test action | Expected FIM event | Expected detail |
| --- | --- | --- |
| Create the file | File added | Path, timestamp, initial checksums (MD5, SHA1, SHA256) |
| Modify the file | File modified | Changed attributes, old and new checksums, size change |
| Delete the file | File deleted | Path, timestamp, last known checksums |

Each event is time-stamped, attributed to the agent and assigned a rule level that indicates severity, giving a central, searchable audit trail.

## 6. Evidence

See [`evidence/README.md`](evidence/README.md) for the checklist and screenshot naming. Status at the time of writing: not captured, because the manager VM could not be brought up. The only evidence available is the record of the blocking issues in [`docs/execution_log_and_challenges.md`](docs/execution_log_and_challenges.md).

### 6.1 Control Design and Monitoring Framework

In place of observed results, the control has been fully specified in [`docs/monitoring_framework.md`](docs/monitoring_framework.md): the three effectiveness metrics with formulas and RAG thresholds, an alert triage and escalation runbook, a RACI for the control, and the audit-evidence procedure referenced in Section 7.4.

## 7. GRC Workshop and Analysis Questions

### 7.1 Risk Identification and Analysis

**What is the potential business impact if this risk were realised?**

- **Financial:** Altered forecasts can drive wrong budgeting, investment and reporting decisions. Deleted forecasts mean rework cost and possible data loss, and fraud could go unnoticed.
- **Reputational:** If investors, lenders or regulators learn that financial documents were tampered with, trust in management and the integrity of reporting is damaged.
- **Operational:** Teams lose time reconstructing documents and validating data, and planning cycles are delayed.
- **Compliance and legal:** Weak integrity controls over financial records can breach requirements such as SOX and, where personal data is involved, data protection obligations such as the Nigeria Data Protection Act.

**How does this control help quantify the risk?**

Once operating, the control turns an unmeasured risk into measurable data. The number of FIM alerts over a period gives an event frequency, which feeds the likelihood component of the risk rating. Splitting alerts into authorised changes (for example, scheduled updates) and unauthorised changes shows the real rate of risk events and the false positive rate. Trends over several months show whether likelihood is rising or falling and whether residual risk is within appetite. Impact can then be estimated per event using the value of the affected documents.

### 7.2 Control Evaluation and Treatment

**What would be a complementary preventive control?**

Role-based access control with least privilege on the forecast folder, so only named finance staff can modify or delete files and everyone else has read-only access. Supporting options include data loss prevention rules, versioned or write-once storage, multi-factor authentication for the workstation and file shares, and endpoint protection against malware. Prevention reduces how often the risk event occurs, while FIM detects what gets through.

**A situation where the alert triggers a corrective control**

Suppose Wazuh raises a high-severity alert that `Q4_Financial_Forecast.docx` was deleted at 2 a.m. by an account that does not normally work at that hour. The security team confirms it is not authorised and starts the incident response process: isolate the workstation, disable or reset the account, restore the file from the latest clean backup or version history, investigate the root cause and document lessons learned. The containment and restore actions are the corrective controls, and the alert is what triggers them.

### 7.3 Risk Monitoring and Reporting

**Three key metrics for reporting operational effectiveness to a manager**

1. **Coverage:** The percentage of in-scope endpoints with an active agent and the monitored folder configured. This shows whether the control is actually deployed.
2. **Volume and classification of FIM alerts:** Number of added, modified and deleted events per period, split into authorised and unauthorised changes, with the trend over time.
3. **Time to detect and respond:** Mean time from the file event to the alert, and from the alert to triage and closure. This shows whether the control is timely and whether the team acts on it.

**How does centralisation improve governance and auditability?**

Checking logs on each computer is inconsistent, slow and easy to tamper with, since someone who alters a file may also be able to alter the local log. A central platform gives one consistent, time-stamped record across all endpoints, retained under defined rules and protected from local tampering. It allows correlation across systems, standard reports and dashboards for management, clear accountability and a repeatable process, all of which support governance oversight. For auditors, evidence can be produced from one source on request, which makes the programme verifiable.

### 7.4 Compliance Mapping

**How does Wazuh provide evidence for compliance audits?**

Wazuh records every monitored file event with a timestamp, agent, file path, action and cryptographic checksums. This gives a searchable, retained audit trail showing the file integrity requirement is both implemented and operating. Wazuh also includes compliance mappings for frameworks such as PCI DSS, HIPAA, GDPR and NIST 800-53, so alerts can be filtered and reported by control requirement. Together with agent status data, this shows coverage and continuous operation.

**Demonstrating that a sensitive file was not altered during a defined period**

1. In the dashboard, open the file integrity monitoring view for the relevant agent.
2. Set the time range to the audit period, for example the last quarter.
3. Filter by the file path (`syscheck.path`) of the sensitive file.
4. !t should show that no modified or deleted events exist for that file in the period, or that the only changes match approved change records.
5. It should show that the agent was active throughout the period, so an absence of alerts is not caused by a monitoring gap.
6. Export or screenshot the results and attach them to the audit evidence file, noting the date and who ran the query.

## 8. Conclusion

File integrity monitoring with Wazuh is a suitable detective control for the risk of unauthorised changes to financial forecasts. It provides real-time alerts, a central audit trail and measurable data for risk monitoring. It is most effective when paired with preventive controls such as least-privilege access and corrective controls such as backup restoration and incident response. The practical deployment was not completed in this submission because the Ubuntu Server manager VM could not be made accessible, and the evidence in `evidence/` should be added once the environment can be built. The control design, metrics and runbook in `docs/monitoring_framework.md` show how the control would operate and be governed.
