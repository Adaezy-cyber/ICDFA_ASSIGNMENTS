# Linux Security Monitoring and Auditing Lab

**Author:** Adaeze E. Adeteye
**Focus:** Cybersecurity | GRC | Data Protection | Security Assurance
**Environment:** Authorised virtual machine (Ubuntu/Debian Linux)

---

## Table of Contents

1. [Introduction](#1-introduction)
2. [Objectives](#2-objectives)
3. [Scope, Environment and Methodology](#3-scope-environment-and-methodology)
4. [Task 1: System Auditing with auditd](#4-task-1-system-auditing-with-auditd)
5. [Task 2: Linux Log Management and Analysis](#5-task-2-linux-log-management-and-analysis)
6. [Task 3: Security Assessment with Lynis](#6-task-3-security-assessment-with-lynis)
7. [Task 4: SIEM and Automation](#7-task-4-siem-and-automation)
8. [GRC Analysis](#8-grc-analysis)
9. [Key Findings](#9-key-findings)
10. [Limitations and Challenges](#10-limitations-and-challenges)
11. [Recommendations](#11-recommendations)
12. [Lessons Learned and Conclusion](#12-lessons-learned-and-conclusion)
13. [Evidence Index](#13-evidence-index)
14. [Repository Structure](#14-repository-structure)
15. [Tools Used and References](#15-tools-used-and-references)
16. [Disclaimer](#16-disclaimer)

---

## 1. Introduction

Monitoring and auditing are the controls that allow an organisation to detect, investigate and prove what happened on its systems. Without them, access control, data protection and incident response commitments cannot be demonstrated.

This lab gave me hands-on experience of Linux security monitoring using `auditd`, `journalctl`, `grep` and Lynis. I collected technical evidence from a Linux system, interpreted it from a security perspective, and connected it to SIEM operations, control monitoring and security assurance.

---

## 2. Objectives

* Understand the role of `auditd` in Linux system auditing.
* Configure audit rules for security-sensitive files and system activity.
* Generate and investigate audit events.
* Use `ausearch` and `aureport` to analyse audit records.
* Review Linux system and authentication logs.
* Use `journalctl` and `grep` to identify security-relevant events.
* Perform a security assessment using Lynis.
* Interpret security warnings and recommendations.
* Understand how Linux monitoring data can integrate with a SIEM.
* Understand the role of automation in continuous security monitoring and auditing.

---

## 3. Scope, Environment and Methodology

### 3.1 Lab Environment

| Item                | Details                                   |
| ------------------- | ----------------------------------------- |
| Operating System    | Ubuntu/Debian Linux                       |
| Environment         | Virtual Machine                           |
| Audit Tool          | auditd                                    |
| Log Analysis        | journalctl, grep                          |
| Security Assessment | Lynis                                     |
| SIEM                | Conceptual (no SIEM was deployed)         |
| Purpose             | Security monitoring and auditing practice |

### 3.2 Scope

In scope: the single lab VM, its audit configuration, its system and authentication logs, and a Lynis assessment of its configuration. Out of scope: any other host, network or production system. The SIEM section is conceptual.

### 3.3 Methodology

```text
Configure → Generate activity → Collect evidence → Analyse → Map to controls → Recommend
```

For each task I ran the commands, captured a screenshot as evidence, and recorded what the output means for security monitoring. All screenshots are stored in the `evidence/` folder and indexed in [Section 13](#13-evidence-index).

---

## 4. Task 1: System Auditing with auditd

### 4.1 Verify auditd

I first checked that the Linux Audit daemon was installed and running.

```bash
sudo systemctl status auditd
```

If `auditd` is not installed, it can be installed with:

```bash
sudo apt update
sudo apt install auditd audispd-plugins
sudo systemctl start auditd
sudo systemctl enable auditd
```

![auditd service status](evidence/01-auditd-status.png)

*Figure 1: auditd service status, checked before configuring rules.*

### 4.2 Configure Audit Rules

I created a separate rule file under `/etc/audit/rules.d/`:

```bash
sudo nano /etc/audit/rules.d/custom.rules
```

```text
-w /etc/passwd -p rwxa -k passwd_changes
-w /etc/shadow -p rwxa -k shadow_changes

-a always,exit -F arch=b64 -S execve -k program_execution
-a always,exit -F arch=b32 -S execve -k program_execution

-w /var/log/auth.log -p wa -k auth_failures
```

| Rule                | Purpose                                     |
| ------------------- | ------------------------------------------- |
| `/etc/passwd`       | Monitor access to user account information  |
| `/etc/shadow`       | Monitor access to password hash information |
| `execve`            | Monitor program execution                   |
| `/var/log/auth.log` | Monitor authentication log activity         |

Each rule carries a key (`-k`), which makes the resulting events searchable by purpose rather than by raw path or syscall.

I reloaded the rules and verified them:

```bash
sudo systemctl restart auditd
sudo auditctl -l
```

![Loaded audit rules](evidence/02-audit-rules.png)

*Figure 2: Active audit rules listed by `auditctl -l`.*

### 4.3 Generate Audit Events

I generated controlled activity to trigger the rules.

| Activity                | Command                | Rule triggered      |
| ----------------------- | ---------------------- | ------------------- |
| Sensitive file access   | `sudo nano /etc/passwd` | `passwd_changes`    |
| Program execution       | `ls /tmp`              | `program_execution` |
| Authentication activity | Authorised local login attempt within the VM | `auth_failures` |

The `/etc/passwd` file was opened and exited without making changes.

### 4.4 Search Audit Events

```bash
sudo ausearch -k passwd_changes
sudo ausearch -k program_execution
sudo ausearch -k auth_failures
```

![Password audit events](evidence/03-passwd-audit.png)

*Figure 3: Audit events for the `passwd_changes` key.*

![Program execution audit events](evidence/04-program-execution.png)

*Figure 4: Audit events for the `program_execution` key.*

![Authentication audit events](evidence/05-auth-failures.png)

*Figure 5: Audit events for the `auth_failures` key.*

The `ausearch` records show which user, process and file were involved and when the activity happened. This is the detail an investigator needs to establish accountability.

### 4.5 Generate Audit Reports

```bash
sudo aureport
sudo aureport --failed
sudo aureport --login
```

![Audit report](evidence/06-aureport.png)

*Figure 6: General audit summary report.*

![Failed audit events](evidence/07-aureport-failed.png)

*Figure 7: Failed events report.*

![Login audit report](evidence/08-aureport-login.png)

*Figure 8: Login activity report.*

**`ausearch` vs `aureport`:** `ausearch` returns detailed records for investigating specific events. `aureport` returns summaries that are useful for reviewing overall audit activity and spotting patterns.

---

## 5. Task 2: Linux Log Management and Analysis

### 5.1 Review System Logs with journalctl

```bash
sudo journalctl                      # recent system logs
sudo journalctl -u ssh               # SSH service logs
sudo journalctl --since "today"      # logs from today
sudo journalctl -p err               # error-level events
sudo journalctl -f                   # live monitoring (stop with Ctrl+C)
```

![Journal logs](evidence/09-journalctl.png)

*Figure 9: systemd journal output.*

![SSH logs](evidence/10-ssh-logs.png)

*Figure 10: SSH service logs.*

![System errors](evidence/11-journal-errors.png)

*Figure 11: Error-level journal events.*

### 5.2 Analyse Authentication Logs

```bash
sudo less /var/log/auth.log
sudo grep -i "failed password" /var/log/auth.log
sudo grep "sudo" /var/log/auth.log
```

The search is case-insensitive because the log records the event as "Failed password".

![Authentication log](evidence/12-auth-log.png)

*Figure 12: Authentication log.*

![Failed authentication](evidence/13-failed-password.png)

*Figure 13: Failed password search results.*

![Sudo activity](evidence/14-sudo-activity.png)

*Figure 14: Sudo (privileged) activity.*

Authentication logs provide evidence of unsuccessful login attempts and of administrative activity.

### 5.3 Analyse System Logs

```bash
sudo less /var/log/syslog
sudo grep -i "error" /var/log/syslog
sudo grep -i "warning" /var/log/syslog
```

![System errors](evidence/15-syslog-errors.png)

*Figure 15: Errors in syslog.*

![System warnings](evidence/16-syslog-warnings.png)

*Figure 16: Warnings in syslog.*

### 5.4 Log Analysis

I treated the logs as security evidence rather than raw output, asking what each event could indicate.

| Evidence Source        | Security Monitoring Purpose                   |
| ---------------------- | --------------------------------------------- |
| `journalctl`           | Review system and service activity            |
| SSH logs               | Monitor remote access activity                |
| `auth.log`             | Monitor authentication activity               |
| Sudo activity          | Monitor privileged access                     |
| Failed password events | Identify unsuccessful authentication attempts |
| Syslog errors          | Identify system or service problems           |
| Syslog warnings        | Identify conditions requiring investigation   |

The significance of any single event depends on its context, frequency, source, the user involved, and whether the activity was authorised. A few failed logins may be a mistyped password; many from one source in a short period suggests a brute-force attempt.

---

## 6. Task 3: Security Assessment with Lynis

### 6.1 About Lynis

Lynis is an open-source security auditing tool for Unix-like systems. It checks system configuration, authentication, file permissions, networking, installed software, logging, security controls and hardening, then produces warnings and suggestions.

### 6.2 Installation

Following the lab guide:

```bash
sudo mkdir /opt/lynis
cd /opt/lynis
sudo wget https://downloads.cisofy.com/lynis/lynis-3.0.8.tar.gz
sudo tar -xvf lynis-3.0.8.tar.gz
cd lynis-3.0.8
```

### 6.3 Running the Audit

```bash
./lynis --version
sudo ./lynis audit system
```

![Lynis version](evidence/17-lynis-version.png)

*Figure 17: Lynis version.*

![Lynis audit](evidence/18-lynis-audit.png)

*Figure 18: Lynis system audit output.*

### 6.4 Results

| Item            | Result                       |
| --------------- | ---------------------------- |
| Lynis Version   | **[from Figure 17]**         |
| Hardening Index | **[from Figure 18]**         |
| Warnings        | **[from Figure 18]**         |
| Suggestions     | **[from Figure 18]**         |
| Report File     | `/var/log/lynis-report.dat`  |

### 6.5 Findings

| ID     | Finding                 | Security Significance | Priority       | Recommended Action |
| ------ | ----------------------- | --------------------- | -------------- | ------------------ |
| LYN-01 | **[Finding from scan]** | **[Analysis]**        | **[Priority]** | **[Action]**       |
| LYN-02 | **[Finding from scan]** | **[Analysis]**        | **[Priority]** | **[Action]**       |
| LYN-03 | **[Finding from scan]** | **[Analysis]**        | **[Priority]** | **[Action]**       |

### 6.6 Improvement and Retesting

The improvement lifecycle applied to Lynis findings:

```text
Identify → Assess → Remediate → Verify → Retest
```

An example of a low-risk remediation within the VM, followed by reassessment:

```bash
sudo apt install ufw
sudo ufw enable
sudo ufw status
sudo ./lynis audit system
```

---

## 7. Task 4: SIEM and Automation

### 7.1 SIEM Overview

A Security Information and Event Management (SIEM) system collects and analyses security events from many sources. Core capabilities are log collection, aggregation, normalisation, parsing, correlation, analysis, alerting, dashboards and reporting.

### 7.2 Linux Evidence and SIEM

Evidence from this lab could conceptually flow into a SIEM as follows:

```text
Linux System
     |
     +-- auditd
     +-- journalctl
     +-- auth.log
     +-- syslog
     +-- Lynis
     |
     v
Evidence Collection
     |
     v
SIEM
     |
     v
Normalisation and Parsing
     |
     v
Correlation and Analysis
     |
     v
Security Alert
     |
     v
Investigation
     |
     v
Remediation
     |
     v
Retesting and Reporting
```

### 7.3 Example Monitoring Scenario

A SIEM can correlate events that look minor on their own:

```text
Multiple authentication failures
             +
Sensitive file access
             +
Unusual program execution
             |
             v
      SIEM correlation
             |
             v
       Security alert
             |
             v
      SOC investigation
             |
             v
      GRC escalation
             |
             v
 Remediation and verification
```

### 7.4 Automation

Automation reduces repetitive manual work and improves consistency. Examples:

* Continuous control monitoring
* Automated alerting
* Automated configuration assessment (for example, scheduled Lynis scans)
* Automated control testing
* Automated reporting and trend analysis
* Security scripts and API integrations
* Automated remediation workflows

```text
Collect → Analyse → Detect → Alert → Investigate → Remediate → Retest → Report
```

---

## 8. GRC Analysis

### 8.1 Evidence-to-Control Mapping

| Technical Evidence         | Control Area                 | Monitoring Purpose                      |
| -------------------------- | ---------------------------- | --------------------------------------- |
| `/etc/passwd` audit events | Account Management           | Monitor sensitive account-file activity |
| `/etc/shadow` audit events | Credential Protection        | Monitor access to password information  |
| `execve` audit events      | System Activity Monitoring   | Monitor program execution               |
| Authentication logs        | Access Control               | Identify authentication activity        |
| Sudo logs                  | Privileged Access Management | Monitor administrative activity         |
| System logs                | System Monitoring            | Identify errors and warnings            |
| Lynis findings             | Security Configuration       | Identify configuration weaknesses       |

### 8.2 Framework Alignment

| Lab Activity                      | ISO/IEC 27001:2022 Annex A                    | NIST CSF 2.0              |
| --------------------------------- | --------------------------------------------- | ------------------------- |
| auditd rules and records          | 8.15 Logging                                  | DE.CM Continuous Monitoring |
| Log review (journalctl, auth.log) | 8.15 Logging, 8.16 Monitoring activities      | DE.AE Adverse Event Analysis |
| Sudo and privileged activity      | 8.2 Privileged access rights                  | PR.AA Identity Management, Authentication and Access Control |
| Authentication monitoring         | 8.5 Secure authentication                     | PR.AA, DE.CM              |
| Lynis assessment                  | 8.9 Configuration management, 8.8 Technical vulnerabilities | ID.RA Risk Assessment, PR.PS Platform Security |

### 8.3 Data Protection Relevance

Audit and access logs help an organisation show that it applies appropriate security measures to personal data, which is a core expectation of data protection law, including the Nigeria Data Protection Act (NDPA) 2023. Logs of who accessed which system, and when, also support breach detection, breach assessment and the evidence needed for notification decisions.

---

## 9. Key Findings

### Finding 1: Audit Monitoring

**Evidence:** auditd records (Figures 3 to 8).
**Observation:** Audit rules gave visibility into selected security-sensitive activity.
**Security relevance:** Detailed audit records support investigation and accountability.

### Finding 2: Log Monitoring

**Evidence:** `journalctl`, authentication and system logs (Figures 9 to 16).
**Observation:** Linux logs provide several complementary sources of information about system, authentication and service activity.
**Security relevance:** Targeted, centralised log analysis helps identify events that need investigation.

### Finding 3: Security Configuration

**Evidence:** Lynis audit (Figures 17 and 18).
**Observation:** Lynis identifies configuration weaknesses and recommends improvements.
**Security relevance:** Configuration assessment supports proactive identification and remediation of weaknesses.

---

## 10. Limitations and Challenges

* **Single lab VM.** Results show monitoring capability on one system and do not represent an enterprise environment.
* **No SIEM deployed.** The SIEM and automation sections are conceptual.
* **auth.log rule.** The rule `-w /var/log/auth.log -p wa` records writes to the log file itself, not the authentication failures inside it. Failed logins are best analysed from the log content (Section 5.2).
* **Log availability.** `/var/log/auth.log` and `/var/log/syslog` depend on `rsyslog`; some newer installations rely only on the journal.
* **Rule persistence and volume.** Rules in `/etc/audit/rules.d/` persist across reboots, and the broad `execve` rule can generate a high volume of events. This needs tuning in production.
* **Lynis scope.** Lynis reports on configuration. It does not confirm that a system is secure or compliant.

---

## 11. Recommendations

1. Keep `auditd` enabled and persistent, with rules tuned to reduce noise.
2. Forward audit and authentication logs to a central log platform or SIEM so they are protected from local tampering.
3. Define alert thresholds for repeated failed logins and unexpected sudo or sensitive-file activity.
4. Schedule regular Lynis scans, track findings in a register with owners and due dates, and retest after remediation.
5. Define log retention periods that match legal, regulatory and investigation needs.
6. Restrict and review access to audit logs themselves.

---

## 12. Lessons Learned and Conclusion

Effective Linux security monitoring needs multiple evidence sources. `auditd` gives detailed system-level auditing, `journalctl` and traditional log files give wider visibility into system and authentication activity, and Lynis adds an assessment of security configuration.

```text
Technical Evidence → Security Observation → Risk / Control Assessment
→ Remediation → Verification → Continuous Monitoring
```

For GRC, the value is in connecting technical findings to security controls, risk decisions, responsible owners, remediation actions and evidence of closure. Technical evidence only becomes assurance when it is analysed, owned and acted on.

---

## 13. Evidence Index

| Evidence | Description                 | File                                                |
| -------- | --------------------------- | --------------------------------------------------- |
| E01      | auditd service status       | [01-auditd-status.png](evidence/01-auditd-status.png)         |
| E02      | Loaded audit rules          | [02-audit-rules.png](evidence/02-audit-rules.png)             |
| E03      | passwd audit events         | [03-passwd-audit.png](evidence/03-passwd-audit.png)           |
| E04      | Program execution events    | [04-program-execution.png](evidence/04-program-execution.png) |
| E05      | Authentication audit events | [05-auth-failures.png](evidence/05-auth-failures.png)         |
| E06      | General audit report        | [06-aureport.png](evidence/06-aureport.png)                   |
| E07      | Failed audit report         | [07-aureport-failed.png](evidence/07-aureport-failed.png)     |
| E08      | Login audit report          | [08-aureport-login.png](evidence/08-aureport-login.png)       |
| E09      | journalctl output           | [09-journalctl.png](evidence/09-journalctl.png)               |
| E10      | SSH logs                    | [10-ssh-logs.png](evidence/10-ssh-logs.png)                   |
| E11      | Journal errors              | [11-journal-errors.png](evidence/11-journal-errors.png)       |
| E12      | Authentication log          | [12-auth-log.png](evidence/12-auth-log.png)                   |
| E13      | Failed password search      | [13-failed-password.png](evidence/13-failed-password.png)     |
| E14      | Sudo activity               | [14-sudo-activity.png](evidence/14-sudo-activity.png)         |
| E15      | Syslog errors               | [15-syslog-errors.png](evidence/15-syslog-errors.png)         |
| E16      | Syslog warnings             | [16-syslog-warnings.png](evidence/16-syslog-warnings.png)     |
| E17      | Lynis version               | [17-lynis-version.png](evidence/17-lynis-version.png)         |
| E18      | Lynis audit                 | [18-lynis-audit.png](evidence/18-lynis-audit.png)             |

---

## 14. Repository Structure

```text
linux-security-monitoring-auditing/
│
├── README.md
│
└── evidence/
    ├── 01-auditd-status.png
    ├── 02-audit-rules.png
    ├── 03-passwd-audit.png
    ├── 04-program-execution.png
    ├── 05-auth-failures.png
    ├── 06-aureport.png
    ├── 07-aureport-failed.png
    ├── 08-aureport-login.png
    ├── 09-journalctl.png
    ├── 10-ssh-logs.png
    ├── 11-journal-errors.png
    ├── 12-auth-log.png
    ├── 13-failed-password.png
    ├── 14-sudo-activity.png
    ├── 15-syslog-errors.png
    ├── 16-syslog-warnings.png
    ├── 17-lynis-version.png
    └── 18-lynis-audit.png
```

---

## 15. Tools Used and References

**Tools:** Ubuntu/Debian Linux, Virtual Machine, auditd, auditctl, ausearch, aureport, journalctl, grep, Lynis.

**References:**

* Linux Audit documentation (`man auditd`, `man auditctl`, `man ausearch`, `man aureport`)
* `man journalctl`
* CISOfy Lynis documentation: https://cisofy.com/documentation/lynis/
* ISO/IEC 27001:2022, Annex A
* NIST Cybersecurity Framework 2.0
* Nigeria Data Protection Act 2023

---

## 16. Disclaimer

This project was completed in an authorised laboratory environment for educational and cybersecurity training purposes. No unauthorised systems, accounts or production environments were targeted.
