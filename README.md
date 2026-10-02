# Linux Security Monitoring and Auditing Lab

## Overview

This lab provided hands-on experience with Linux security monitoring, system auditing, log analysis, and security configuration assessment.

The practical work focused on using `auditd`, `journalctl`, `grep`, and Lynis to collect and interpret security-relevant evidence from a Linux system. The lab also introduced how these technical monitoring activities support SIEM operations, security investigations, continuous control monitoring, and security assurance.

---

## Objectives

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

## Lab Environment

| Item                | Details                                   |
| ------------------- | ----------------------------------------- |
| Operating System    | Ubuntu/Debian Linux                       |
| Environment         | Virtual Machine                           |
| Audit Tool          | auditd                                    |
| Log Analysis        | journalctl, grep                          |
| Security Assessment | Lynis                                     |
| SIEM                | Conceptual                                |
| Purpose             | Security monitoring and auditing practice |

All activities were performed within an authorised laboratory environment.

---

# Module 1: System Auditing with auditd

## 1.1 Verify auditd

I first checked whether the Linux Audit daemon was installed and running.

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

The service status was checked before configuring the audit rules.

---

## 1.2 Configure Audit Rules

A separate audit rule file was created under `/etc/audit/rules.d/`:

```bash
sudo nano /etc/audit/rules.d/custom.rules
```

The following rules were added:

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

The rules were reloaded:

```bash
sudo systemctl restart auditd
```

I verified the active rules with:

```bash
sudo auditctl -l
```

![Loaded audit rules](evidence/02-audit-rules.png)

---

## 1.3 Generate Audit Events

I generated controlled activity to trigger the configured audit rules.

**Sensitive file access**

```bash
sudo nano /etc/passwd
```

The file was opened and exited without making changes.

**Program execution**

```bash
ls /tmp
```

This generated activity relevant to the `program_execution` audit rule.

**Authentication monitoring**

An authentication event was generated using an authorised local mechanism within the VM.

---

## 1.4 Search Audit Events

The audit records were searched using the keys configured in the audit rules.

```bash
sudo ausearch -k passwd_changes
sudo ausearch -k program_execution
sudo ausearch -k auth_failures
```

![Password audit events](evidence/03-passwd-audit.png)

![Program execution audit events](evidence/04-program-execution.png)

![Authentication audit events](evidence/05-auth-failures.png)

The `ausearch` results provided detailed audit records showing what activity occurred and when.

---

## 1.5 Generate Audit Reports

I used `aureport` to obtain higher-level summaries.

```bash
sudo aureport
sudo aureport --failed
sudo aureport --login
```

![Audit report](evidence/06-aureport.png)

![Failed audit events](evidence/07-aureport-failed.png)

![Login audit report](evidence/08-aureport-login.png)

**`ausearch` vs `aureport`:** `ausearch` provides detailed records for investigating specific events, while `aureport` provides summarised information that is useful for reviewing overall audit activity.

---

# Module 2: Linux Log Management and Analysis

## 2.1 Review System Logs with journalctl

I used `journalctl` to review the systemd journal.

```bash
sudo journalctl                      # recent system logs
sudo journalctl -u ssh               # SSH service logs
sudo journalctl --since "today"      # logs from today
sudo journalctl -p err               # error-level events
sudo journalctl -f                   # live monitoring (stop with Ctrl+C)
```

![Journal logs](evidence/09-journalctl.png)

![SSH logs](evidence/10-ssh-logs.png)

![System errors](evidence/11-journal-errors.png)

---

## 2.2 Analyse Authentication Logs

I reviewed the authentication log:

```bash
sudo less /var/log/auth.log
```

I searched for failed authentication attempts (case-insensitive, since the log records them as "Failed password"):

```bash
sudo grep -i "failed password" /var/log/auth.log
```

I also searched for privileged activity:

```bash
sudo grep "sudo" /var/log/auth.log
```

![Authentication log](evidence/12-auth-log.png)

![Failed authentication](evidence/13-failed-password.png)

![Sudo activity](evidence/14-sudo-activity.png)

Authentication logs provide useful evidence for identifying unsuccessful login attempts and monitoring privileged activity.

---

## 2.3 Analyse System Logs

I reviewed the system log and searched for errors and warnings:

```bash
sudo less /var/log/syslog
sudo grep -i "error" /var/log/syslog
sudo grep -i "warning" /var/log/syslog
```

![System errors](evidence/15-syslog-errors.png)

![System warnings](evidence/16-syslog-warnings.png)

---

## 2.4 Log Analysis

The logs were not treated simply as raw technical output. I considered what each event could indicate from a security monitoring perspective.

| Evidence Source        | Security Monitoring Purpose                   |
| ---------------------- | --------------------------------------------- |
| `journalctl`           | Review system and service activity            |
| SSH logs               | Monitor remote access activity                |
| `auth.log`             | Monitor authentication activity               |
| Sudo activity          | Monitor privileged access                     |
| Failed password events | Identify unsuccessful authentication attempts |
| Syslog errors          | Identify system or service problems           |
| Syslog warnings        | Identify conditions requiring investigation   |

The significance of an individual event depends on its context, frequency, source, user, and whether the activity was authorised.

---

# Module 3: Security Assessment with Lynis

## 3.1 About Lynis

Lynis is an open-source security auditing tool for Unix-like systems. It examines system configuration, authentication, file permissions, networking, installed software, logging, security controls, and system hardening. The purpose of the assessment was to identify security weaknesses and configuration areas that may require attention.

---

## 3.2 Install Lynis

Following the lab guide:

```bash
sudo mkdir /opt/lynis
cd /opt/lynis
sudo wget https://downloads.cisofy.com/lynis/lynis-3.0.8.tar.gz
sudo tar -xvf lynis-3.0.8.tar.gz
cd lynis-3.0.8
```

---

## 3.3 Run Lynis Audit

```bash
./lynis --version
sudo ./lynis audit system
```

![Lynis version](evidence/17-lynis-version.png)

![Lynis audit](evidence/18-lynis-audit.png)

---

## 3.4 Lynis Results

| Item            | Result                  |
| --------------- | ----------------------- |
| Lynis Version   | **[Add from your scan]** |
| Hardening Index | **[Add from your scan]** |
| Warnings        | **[Add from your scan]** |
| Suggestions     | **[Add from your scan]** |
| Report File     | `/var/log/lynis-report.dat` |

---

## 3.5 Lynis Findings

| ID     | Finding                     | Security Significance | Priority        | Recommended Action |
| ------ | --------------------------- | --------------------- | --------------- | ------------------ |
| LYN-01 | **[Finding from scan]**     | **[Analysis]**        | **[Priority]**  | **[Action]**       |
| LYN-02 | **[Finding from scan]**     | **[Analysis]**        | **[Priority]**  | **[Action]**       |
| LYN-03 | **[Finding from scan]**     | **[Analysis]**        | **[Priority]**  | **[Action]**       |

---

## 3.6 Security Improvement and Retesting

The security improvement lifecycle followed in this lab:

```text
Identify → Assess → Remediate → Verify → Retest
```

An example of a low-risk remediation within the VM, followed by a reassessment:

```bash
sudo apt install ufw
sudo ufw enable
sudo ufw status
sudo ./lynis audit system
```

---

# Module 4: SIEM and Automation

## 4.1 SIEM Overview

A Security Information and Event Management (SIEM) system collects and analyses security events from multiple sources. Key capabilities include log collection, aggregation, normalisation, parsing, correlation, analysis, alerting, dashboards, and reporting.

## 4.2 Linux Evidence and SIEM

Evidence collected during this lab could conceptually flow into a SIEM as follows:

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

## 4.3 Example Monitoring Scenario

A SIEM can correlate several events rather than treating each independently:

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

The combination of events provides more useful security context than a single log entry.

## 4.4 Automation

Automation improves monitoring and auditing by reducing repetitive manual work and increasing consistency. Examples include:

* Continuous control monitoring
* Automated alerting
* Automated configuration assessment
* Automated control testing
* Automated reporting
* Trend analysis
* Security scripts and API integrations
* Automated remediation workflows

```text
Collect → Analyse → Detect → Alert → Investigate → Remediate → Retest → Report
```

---

# Evidence-to-Control Mapping

| Technical Evidence         | Control Area                 | Monitoring Purpose                      |
| -------------------------- | ---------------------------- | --------------------------------------- |
| `/etc/passwd` audit events | Account Management           | Monitor sensitive account-file activity |
| `/etc/shadow` audit events | Credential Protection        | Monitor access to password information  |
| `execve` audit events      | System Activity Monitoring   | Monitor program execution               |
| Authentication logs        | Access Control               | Identify authentication activity        |
| Sudo logs                  | Privileged Access Management | Monitor administrative activity         |
| System logs                | System Monitoring            | Identify errors and warnings            |
| Lynis findings             | Security Configuration       | Identify configuration weaknesses       |

---

# Key Findings

## Finding 1: Audit Monitoring

**Evidence:** Auditd records generated during the exercise.
**Observation:** Audit rules provided visibility into selected security-sensitive activities.
**Security relevance:** Detailed audit records support investigation and accountability for system activity.

## Finding 2: Log Monitoring

**Evidence:** `journalctl`, authentication logs, and system logs.
**Observation:** Linux logs provide multiple sources of information about system, authentication, and service activity.
**Security relevance:** Centralised and targeted log analysis helps identify events requiring investigation.

## Finding 3: Security Configuration

**Evidence:** Lynis system audit.
**Observation:** Lynis identifies configuration weaknesses and provides recommendations for improving security posture.
**Security relevance:** Configuration assessment supports proactive identification and remediation of weaknesses.

---

# Lessons Learned

Effective Linux security monitoring requires multiple sources of evidence. `auditd` provides detailed system-level auditing, `journalctl` and traditional log files provide broader visibility into system and authentication activity, and Lynis adds an assessment of the system's security configuration.

```text
Technical Evidence → Security Observation → Risk / Control Assessment
→ Remediation → Verification → Continuous Monitoring
```

In a GRC environment, technical findings should ultimately be connected to security controls, risk decisions, responsible owners, remediation activities, and evidence of closure.

---

# Evidence Index

| Evidence | Description                 | File                       |
| -------- | --------------------------- | -------------------------- |
| E01      | auditd service status       | `01-auditd-status.png`     |
| E02      | Loaded audit rules          | `02-audit-rules.png`       |
| E03      | passwd audit events         | `03-passwd-audit.png`      |
| E04      | Program execution events    | `04-program-execution.png` |
| E05      | Authentication audit events | `05-auth-failures.png`     |
| E06      | General audit report        | `06-aureport.png`          |
| E07      | Failed audit report         | `07-aureport-failed.png`   |
| E08      | Login audit report          | `08-aureport-login.png`    |
| E09      | journalctl output           | `09-journalctl.png`        |
| E10      | SSH logs                    | `10-ssh-logs.png`          |
| E11      | Journal errors              | `11-journal-errors.png`    |
| E12      | Authentication log          | `12-auth-log.png`          |
| E13      | Failed password search      | `13-failed-password.png`   |
| E14      | Sudo activity               | `14-sudo-activity.png`     |
| E15      | Syslog errors               | `15-syslog-errors.png`     |
| E16      | Syslog warnings             | `16-syslog-warnings.png`   |
| E17      | Lynis version               | `17-lynis-version.png`     |
| E18      | Lynis audit                 | `18-lynis-audit.png`       |

---

# Repository Structure

```text
linux-security-monitoring-auditing/
├── README.md
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

# Tools Used

Ubuntu/Debian Linux, Virtual Machine, auditd, auditctl, ausearch, aureport, journalctl, grep, Lynis

---

# Author

**Adaeze E. Adeteye**
Cybersecurity | GRC | Data Protection | Security Assurance

---

## Disclaimer

This project was completed in an authorised laboratory environment for educational and cybersecurity training purposes. No unauthorised systems, accounts, or production environments were targeted.
