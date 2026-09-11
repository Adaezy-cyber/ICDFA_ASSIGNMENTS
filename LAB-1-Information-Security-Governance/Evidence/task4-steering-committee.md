
# Task 4: Security Steering Committee

**Prepared by:** Adaeze Adeteye, Director of Information Security Governance, GlobalHealth Connect (GHC)  
**Executive request:** The CEO has asked for a formal Security Steering Committee (SSC) to resolve cross-functional security conflicts, prompted by the current dispute between the CTO and IT Manager over the proposed password policy.

**Conflict context:** The IT Manager, John Smith, has proposed a policy requiring 16-character complex passwords changed every 30 days, with no password-manager integration. The CTO, Elena Rodriguez, believes this creates excessive friction for developers and recommends a more balanced approach built around multi-factor authentication (MFA) and secure password management instead.

---

## Security Steering Committee-Terms of Reference

### 1. Purpose
The Security Steering Committee exists to provide cross-functional strategic direction, prioritisation and oversight for GHC's information security programme, and to resolve exactly the kind of disagreement now on the table between IT Operations and the CTO's function- where two legitimate business concerns (security control strength vs. developer productivity) point in different directions and need a structured forum, not an escalation to the CEO, to be resolved.

### 2. Scope
The SSC has oversight of:
- Security policy and control decisions with cross-functional impact such as the password policy currently in dispute.
- Prioritisation of security initiatives and resourcing trade-offs.
- Review of significant security risks and incident learnings before they reach Board reporting.
- Recommendations to the Board on strategic security direction, via me as chair.

Kindlu note that The SSC does not replace the RACI accountabilities set out in Task 1, it is the forum where Consulted and Responsible parties work through a decision before it is finalised by the Accountable owner.

### 3. Membership
| Member | Role on Committee |
|---|---|
| Adaeae Adeteye, Director of Information Security Governance | Chair |
| Elena Rodriguez, CTO | Member - represents technology strategy, developer productivity, innovation |
| John Smith, IT Manager | Member - represents infrastructure operations and control implementation |
| Mark Johnson, Compliance Officer | Member - represents regulatory obligations |
| Jane Doe, Senior Developer | Member - represents front-line product development impact |
| Robert Green, HR Manager | Member - represents workforce and onboarding/offboarding impact |

Membership is by role, not by named individual, so the committee continues to function if any member changes position.

### 4. Responsibilities
- Review and resolve cross-functional security policy conflicts, using documented risk and business-impact reasoning.
- Recommend security investment priorities to the CFO and CEO.
- Monitor the six-month security metrics (Task 3) at a working level between Board reporting cycles.
- Escalate to the CEO only where the committee cannot reach a workable resolution within one meeting cycle.

### 5. Meeting Cadence
- **Standing meetings:** monthly.
- **Ad-hoc meetings:** may be called by the Chair within 5 business days where a cross-functional conflict such as the current password-policy dispute requires timely resolution.

### 6. Decision Authority
- The SSC operates by seeking consensus wherever possible, since durable security decisions need buy-in from the functions that must implement them.
- Where consensus cannot be reached, I hold final decision authority as Chair and Accountable owner under the Task 1 RACI matrix, informed by the committee's discussion.
- Decisions with material budget impact are escalated to the CFO for approval before implementation.
- Decisions that materially change GHC's risk posture are reported to the CEO and, where significant, the Board.

### 7. Reporting
- I report SSC decisions and any escalations as part of my regular Board reporting (Task 3).
- Meeting minutes, including dissenting views, are retained as governance evidence.

---

## Sample First SSC Meeting Agenda

**Meeting:** Security Steering Committee — Inaugural Meeting  
**Chair:** Director of Information Security Governance  
**Attendees:** CTO, IT Manager, Compliance Officer, Senior Developer, HR Manager

| Time | Item | Lead |
|---|---|---|
| 0:00–0:10 | Welcome, purpose of the SSC, review of Terms of Reference | Chair |
| 0:10–0:15 | Confirm membership, decision authority and meeting cadence | Chair |
| 0:15–0:45 | **Key discussion item: Password policy conflict** IT Manager presents the case for 16-character/30-day rotation; CTO presents the case for MFA + secure password management; open discussion on risk vs. friction trade-off | IT Manager, CTO |
| 0:45–0:55 | Decision and next steps on password policy see briefing note below for recommended resolution | Chair |
| 0:55–1:05 | Review of current six-month security metrics on phishing, malware, patching, training, high-risk incidents | Chair |
| 1:05–1:15 | Standing risk register review | Compliance Officer |
| 1:15–1:25 | AOB and confirm next meeting date | Chair |

---

## CEO Briefing Note

**To:** Sarah Chen, CEO  
**From:** Adaeze Adeteye, Director of Information Security Governance  
**Re:** Security Steering Committee and Resolution of the Password Policy Dispute

Dear MS. Sarah, 
The Security Steering Committee gives GHC a standing forum to resolve exactly the kind of disagreement currently on the table between the IT Manager and the CTO, instead of it landing on your desk every time it happens. Rather than treating this as a binary choice between "strict controls" and "developer-friendly," the committee will evaluate it as a proportionality question: does a 16-character password changed every 30 days actually reduce risk more than MFA plus a managed password vault, given the operational friction it creates? My own assessment, which I will bring to the first meeting, is that the CTO's recommendation is the stronger one, frequent forced rotation without password-manager support is widely understood to push users toward weaker, more predictable passwords, while MFA addresses the same credential-theft risk without that side effect. I expect the committee to reach that same conclusion, but I want it decided through the SSC's process, not by me overriding the IT Manager unilaterally, so the resolution has cross-functional buy-in and doesn't resurface as the same argument next quarter.

More broadly, this committee is how I intend to keep security decisions aligned with GHC's strategic goals rather than made in isolation: developer productivity a CTO concern and control strength an IT Operations concern will now be weighed together, with Compliance and HR also at the table for regulatory and workforce impact. This is the structural fix for the accountability gap identified in Task 1 that says cross-functional conflicts get resolved with documented reasoning at the working level, and only escalate to you when they genuinely can't be.

your opinion regarding this will be appreciated. Thanks 

Yours Sincerely, 

Adaeze Adeteye

