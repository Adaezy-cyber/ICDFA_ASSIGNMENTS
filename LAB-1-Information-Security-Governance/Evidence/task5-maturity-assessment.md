# Task 5: Governance Maturity Assessment

**Prepared by:** Adaeze Adeteye Director of Information Security Governance, GlobalHealth Connect (GHC) 
**Executive request:** The Board wants evidence that GHC's new governance arrangements will improve measurably over time, not just exist on paper.

**Note on method:** I assessed each domain against the simplified 1–5 maturity scale using the current-state evidence gathered during my governance review the same evidence base underlying the Task 1 gap assessment, since this reflects what stakeholders across GHC actually described when I asked them how these processes work today.

---

## Completed Maturity Assessment

| Governance Domain | Current-State Evidence | Maturity Level | Rationale |
|---|---|---|---|
| Policy & Documentation | Policies are inconsistent, inherited from acquisitions, and not always current. | **2 - Initial** | Documentation exists (it isn't absent), but it is inconsistently applied and not standardised — this matches "some processes exist but are inconsistently documented or applied" rather than a total absence of process. |
| Roles & Responsibilities | Security ownership and accountability are unclear. | **1 - Ad Hoc** | There is no defined, communicated responsibility model in place at all — this is the domain furthest from a defined state, which is why Task 1's RACI matrix was the first artefact I built. |
| Risk Management | The organisation is reactive and lacks a formal, proactive assessment process. | **1 - Ad Hoc** | No structured process exists; risk is discovered after the fact, which is the defining characteristic of Level 1. |
| Metrics & Reporting | Technical metrics exist but are not consistently translated into business impact. | **2 - Initial** | Data collection itself is happening (the six-month dataset in Task 3 proves this), but it isn't standardised into a repeatable, business-facing reporting process. |
| Training & Awareness | Annual training is mandatory, but engagement is low. | **2 - Initial** | A process exists and is applied (mandatory annual training), but low engagement means it is not consistently effective — this is Level 2, not Level 3, because "supported by clear responsibilities" and genuine communication are missing. |
| Compliance | Preparation is audit-driven rather than continuously monitored. | **2 - Initial** | A compliance process clearly exists (audits happen), but it is applied inconsistently over time rather than continuously monitored, so it does not yet meet the Level 3 bar of being standardised and ongoing. |

**Overall current maturity: GHC sits mostly at Level 2 (Initial), with Roles & Responsibilities and Risk Management still at Level 1 (Ad Hoc)** the two domains where I found the least structure at all, and not coincidentally, the two domains most directly implicated in how the recent near-miss was able to develop without earlier detection.

---

## 12–18 Month Maturity Roadmap

I have proposed five priority initiatives — enough to cover all six domains without spreading effort so thin that nothing reaches Level 3 within the window. Two domains are paired where the work is genuinely shared.

| # | Initiative | Domain(s) | Objective | Key Activities | Measurable Expected Outcome | Timeframe |
|---|---|---|---|---|---|---|
| 1 | Policy Harmonisation Programme | Policy & Documentation | Consolidate GHC's inconsistent, acquisition-inherited policies into a single, standardised, currently-maintained policy suite. | Audit all existing policies across GHC and its two acquired entities; identify conflicts, gaps and duplication; rewrite into a unified policy set under my authority as defined in the Task 2 Charter; publish with a version-control and annual review cycle; communicate to all staff. | 100% of GHC's information security policies harmonised, published and under a documented annual review cycle - moving this domain to Level 3 (Defined). | 6 months |
| 2 | Accountability & Security Awareness Programme | Roles & Responsibilities; Training & Awareness | Give every governance activity a clear, communicated owner, and make security training something staff genuinely engage with rather than complete as a compliance formality. | Formally roll out the Task 1 RACI matrix across all departments; embed security responsibilities into job descriptions and performance reviews (working with Robert Green, HR); redesign training from a single annual module into shorter, role-specific, recurring sessions; track completion and engagement, not completion alone. | Documented, communicated ownership in place for 100% of governance activities, and training engagement sustained above 85% (against the current 70% trend from Task 3) - moving both domains to Level 3. | 9 months |
| 3 | Proactive Risk Management Programme | Risk Management | Replace GHC's reactive risk posture with a standing, proactive risk assessment process. | Establish a quarterly enterprise risk assessment cycle owned by me; build a formal risk register with a standard scoring methodology; route significant risks through the Security Steering Committee (Task 4) before they reach the Board. | Four consecutive quarterly risk assessments completed, documented and reviewed by the SSC, with a live, maintained risk register - reaching Level 3. | 12 months |
| 4 | Board-Aligned Security Metrics Programme | Metrics & Reporting | Turn the ad-hoc technical metrics GHC already collects into the standardised, business-facing reporting model demonstrated in Task 3. | Formalise the five-metric Board reporting set into a recurring quarterly cadence; define RAG (Red/Amber/Green) thresholds in advance so status assessments are consistent rather than subjective; where practical, automate metric collection to reduce manual reporting effort. | Four consecutive quarters of on-time, standardised Board security reporting delivered - reaching Level 3. | 12 months |
| 5 | Continuous Compliance & Patch Management Programme | Compliance | Shift GHC from audit-driven, point-in-time compliance to continuous monitoring, and directly reverse the patching decline identified in Task 3 (67% → 55% over six months). | Deploy continuous vulnerability scanning and patch tracking; set a firm patch-compliance target with monthly tracking visible to the SSC; move regulatory compliance checks from an annual audit event to an ongoing monitoring process owned jointly with Mark Johnson (Compliance Officer). | Patch compliance restored to 90%+ and continuous compliance monitoring operating in place of audit-only checks - reaching Level 3. | 12 months |

---

## Board Executive Summary - Governance Maturity

GHC's information security governance is currently concentrated at Level 2 (Initial) across most domains, with Roles & Responsibilities and Risk Management still at Level 1 (Ad Hoc) - meaning that, in those two areas specifically, GHC has been operating without any defined, repeatable process at all. This is not a criticism of any individual; it is the predictable result of rapid growth and two acquisitions outpacing governance investment, and it is the same underlying condition that allowed the recent data-leakage near-miss to develop without earlier warning.

The roadmap I am proposing is deliberately structured around five initiatives that map to all six governance domains, each with a measurable target and a 6–12 month delivery window, so that GHC reaches at least Level 3 (Defined) - documented, standardised and supported by clear responsibilities - across every domain within the Board's 12–18 month expectation. I want to be direct with the Board about why this matters commercially, not just procedurally: GHC's 2026 strategic goals - 25% client growth, two new regional markets, AI-driven diagnostics - all depend on customers and regulators trusting that our governance is more than a policy binder. This roadmap is how that trust becomes demonstrable rather than assumed.
