# GlobalHealth Connect (GHC)
## Information Security Governance Assignment

**Prepared by: Adaeze E. Adeteye**  
**Role: Director of Information Security Governance**  

---

## Table of Contents

1. [Executive Overview](#executive-overview)
2. [Task 1 — Governance Blueprint](#task-1--governance-blueprint)
   - [Current-State Governance Gap Assessment](#11-current-state-governance-gap-assessment)
   - [Proposed Security Governance Structure](#12-proposed-security-governance-structure)
3. [Task 2 — Information Security Charter](#task-2--information-security-charter)
   - [Purpose](#21-purpose)
   - [Scope](#22-scope)
   - [Authority](#23-authority)
   - [Roles and Responsibilities](#24-roles-and-responsibilities)
   - [Key Principles](#25-key-principles)
   - [Reporting Structure](#26-reporting-structure)
   - [CFO Justification Memo](#cfo-justification-memo)
4. [Task 3 — Board Reporting](#task-3--board-reporting)
   - [Board Executive Summary](#31-board-executive-summary)
   - [Security Metrics](#32-five-selected-security-metrics)
   - [Priority Risks and Recommendations](#33-priority-risks-and-recommendations)
   - [Metric Selection Rationale](#34-rationale-for-metric-selection)
5. [Task 4 — Security Steering Committee](#task-4--security-steering-committee)
   - [Terms of Reference](#41-terms-of-reference)
   - [Membership](#42-membership)
   - [Decision Authority](#43-decision-authority)
   - [First Meeting Agenda](#44-sample-first-ssc-meeting-agenda)
   - [CEO Briefing Note](#45-ceo-briefing-note)
6. [Task 5 — Governance Maturity Assessment](#task-5--governance-maturity-assessment)
   - [Maturity Assessment](#51-completed-maturity-assessment)
   - [12–18 Month Roadmap](#52-12-18-month-roadmap)
   - [Board Executive Summary](#53-board-executive-summary--governance-maturity)
7. [Key References](#key-references)

---

## 1. Executive Overview

This repository contains the strategic Information Security Governance framework developed for **GlobalHealth Connect (GHC)** following a recent data-leakage near-miss. Rapid growth from organic expansion and two corporate acquisitions created significant security governance gaps across GHC's cloud-based patient management ecosystems.

This documentation establishes a formal, business-aligned security function. It defines governance roles, institutes an executive charter, formalizes Board-level reporting metrics, creates a cross-functional Security Steering Committee (SSC), and outlines a 12–18 month maturity roadmap to transition GHC from a reactive state to a resilient, Level 3 (Defined) security posture.

---

<a id="task-1--governance-blueprint"></a>
## 2. Task 1 — Governance Blueprint

<a id="11-current-state-governance-gap-assessment"></a>
### 1.1 Current-State Governance Gap Assessment

An evaluation across six governance domains revealed a pattern of **"capable people, no system"**—operational security efforts exist in silos without central accountability or Board alignment.

| Governance Domain | Current Gap | Business Risk |
|---|---|---|
| **Policy & Documentation** | Inconsistent, stale policies inherited from acquired entities. | No single source of truth; inability to demonstrate compliance to healthcare clients and regulators. |
| **Roles & Responsibilities** | Ownership and accountability are undefined across teams. | Ambiguity during security events, increasing the likelihood that near-misses become major breaches. |
| **Risk Management** | Reactive posture; lack of standard risk assessments. | Technology and M&A decisions proceed without prior visibility into introduced security liabilities. |
| **Metrics & Reporting** | Technical noise reported without business impact context. | Leadership lacks actionable risk intelligence and early-warning indicators. |
| **Training & Awareness** | Mandatory annual training treated as a checkbox. | Low employee engagement leaves the human perimeter vulnerable to social engineering. |
| **Compliance** | Audit-driven, point-in-time preparation. | Leaves multi-month compliance gaps between annual audit cycles in a highly regulated sector. |

<a id="12-proposed-security-governance-structure"></a>
### 1.2 Proposed Security Governance Structure

The governance model establishes direct Board visibility for security while connecting operations through the cross-functional Security Steering Committee (SSC).

```mermaid
graph TD
    Board["Board of Directors<br/>(David Miller — Board oversight)"]
    CEO["Sarah Chen — CEO"]
    CFO["Marcus Thorne — CFO"]
    CTO["Elena Rodriguez — CTO"]
    DISG["Adaeze E. Adeteye — Director of InfoSec Governance"]
    SSC["Security Steering Committee<br/>(cross-functional)"]
    ITOps["John Smith — IT Manager / IT Operations"]
    Dev["Jane Doe — Senior Developer / Product Dev"]
    Compliance["Mark Johnson — Compliance Officer"]
    HR["Robert Green — HR Manager"]
    Finance["Emily White — Data Analyst / Finance"]

    Board -->|governance oversight, risk appetite| CEO
    CEO -->|mandate & authority| DISG
    DISG -->|reports posture, risk, metrics| Board
    DISG -->|chairs| SSC
    CFO -->|budget sponsor / investment oversight| DISG
    CTO -->|member| SSC
    ITOps -->|member| SSC
    Dev -->|member| SSC
    Compliance -->|member| SSC
    HR -->|member, informed| SSC
    Finance -.->|informed on relevant risk| SSC
