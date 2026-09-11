# Task 3: Board Reporting

**Prepared by:** Adaeze Adeteye - Director of Information Security Governance, GlobalHealth Connect (GHC)  
**Executive request:** Board member David Miller has asked for meaningful, business-relevant security metrics rather than raw technical data.

---

## Board Executive Summary

**To:** Board of Directors, GlobalHealth Connect  
**From:** Adaeze Adeteye, Director of Information Security Governance  
**Period covered:** September 2025-February 2026 (6 months)

Dear Sir,

I have tracked GHC's security posture over the past 6 months against five metrics chosen specifically because each one connects directly to a business outcome the Board cares about. The headline finding is this: **our exposure to attack is rising faster than our defensive readiness**, and this is the same underlying pattern that produced the recent near-miss.

Phishing attempts against GHC staff have more than doubled (+113%) and malware detections have doubled (+100%) over the period, which tells me GHC is a growing target, consistent with our expansion into new markets and two recent acquisitions increasing our visible footprint. At the same time, patching compliance has declined from 67% to 55%, meaning our exposed surface is growing while our ability to close known vulnerabilities is getting worse. High-risk incidents have risen from 2 to 7 per month, a 250% increase, which I consider the most important single number in this report as it is a lagging indicator confirming that the first two trends are already translating into real risk events, not just theoretical exposure.

The one genuinely positive trend is training completion, which has risen from 45% to 70%. This shows that governance attention does move the needle, which is precisely why I am recommending the Board put the same deliberate push on patching compliance rather than treating it as something that will improve on its own.

**My recommendation to the Board:** approve a formal remediation programme for patch management (Task 5 sets out a 12–18 month roadmap) and treat rising high-risk incidents as the leading business risk for this cycle, not a technical footnote.

---

## Five Selected Security Metrics: Trends and Commentary

| # | Metric | Sep | Oct | Nov | Dec | Jan | Feb | 6-Month Trend |
|---|---|---|---|---|---|---|---|---|
| 1 | Phishing attempts detected/month | 150 | 180 | 210 | 250 | 280 | 320 | **+113.3%** ▲ |
| 2 | Malware detections/month | 25 | 30 | 35 | 40 | 45 | 50 | **+100.0%** ▲ |
| 3 | Patching compliance (%) | 67 | 60 | 60 | 60 | 57 | 55 | **−17.9%** ▼ |
| 4 | Security training completion (%) | 45 | 50 | 55 | 60 | 65 | 70 | **+55.6%** ▲ (positive) |
| 5 | High-risk incidents/month | 2 | 3 | 4 | 5 | 6 | 7 | **+250.0%** ▲ (concerning) |

**Commentary:**

1. **Phishing attempts**: The steady, near-linear rise (150 → 320) does not look like a one-off spike; it looks like GHC has become a consistently more attractive target, most likely tied to our growing profile as we expand. This trend on its own is not alarming, but it raises the stakes on every other metric on this list, since phishing is usually the entry point for the incidents in Metric 5.

2. **Malware detections**: Doubling in six months, in step with the phishing increase, tells me these are likely related: more successful phishing generally precedes more malware footholds. I read this as confirmation rather than a separate problem.

3. **Patching compliance**: This is the metric that most concerns me, because it is the one moving in the *wrong* direction and it is the one most directly within GHC's control. A drop from 67% to 55% means well over a third of our systems now carry unpatched, known vulnerabilities at any given time and this decline is happening at exactly the moment attack volume is rising.

4. **Training completion**: The one bright spot, and I include it deliberately so the Board sees that governance-led intervention works. This is direct evidence for my recommendation elsewhere in this report: apply the same kind of deliberate push to patch management.

5. **High-risk incidents**: I weight this the most heavily of all five, because it is an outcome metric, not an activity metric. Rising phishing and malware volumes are concerning; rising high-risk incidents means those threats are increasingly succeeding. A 250% increase over six months is the number I would not want to have to explain to the Board a second time after another near-miss.

---

## Priority Risks and Recommendations

| Priority | Risk | Recommendation |
|---|---|---|
| **1 (Highest)** | Declining patch compliance (67%→55%) against a rising attack volume creates a widening window of exploitable vulnerability. | Fund a dedicated patch-management remediation effort with a target compliance floor (recommend 90%+) and monthly Board-visible tracking, detailed in the Task 5 roadmap. |
| **2** | High-risk incidents have grown 250% in six months, indicating existing controls are not keeping pace with threat volume. | Commission a focused root-cause review of the last two quarters' high-risk incidents to determine whether they trace back to patching gaps, phishing success, or a third factor not yet visible in these five metrics. |
| **3** | Rising phishing and malware volumes suggest GHC's growth (new markets, acquisitions) is increasing our attack surface faster than our awareness controls account for. | Extend the training programme that successfully lifted completion from 45% to 70% into phishing-specific simulation exercises, and report simulation click-through rates as a future Board metric. |

---

## Rationale for Metric Selection

I chose these five metrics out of everything I could technically measure, because each one passes a test I apply to any number before it goes in front of the Board: does this tell a Board member something about business risk?

- **Phishing and malware volumes**: This were chosen together because they represent inbound pressure on how much the organisation is being targeted. The Board needs to know whether the threat environment itself is changing, independent of how well GHC is defending against it, because that context is what makes the other three metrics meaningful rather than abstract.
- **Patching compliance**: This was chosen because it is the clearest example of a metric that is entirely within GHC's control and directly predicts future incident risk. I deliberately avoided reporting narrower technical patch metrics (e.g., patch cadence by system type) because they would not be actionable for the Board a single compliance percentage is something the Board can hold me accountable to over time.
- **Training completion**: This was included specifically because it is a governance-effectiveness metric, not a threat metric. It shows the Board whether the interventions I am funding and running are actually working, which is the basis on which the Board should judge whether to approve further governance spend.
- **High-risk incidents**: This was chosen as the single outcome metric that ties everything else together. Every other metric on this page is a leading indicator; this is the lagging one that confirms whether the leading indicators actually matter. I included it last in the table but weight it first in my commentary, because a Board member reading only one number on this page should read that one.

I excluded several metrics I do track internally like mean time to detect, vulnerability scan counts, individual system patch levels because they require security expertise to interpret and would not, on their own, change a Board-level decision, which was the specific gap David Miller asked me to close.

i Sincerely do hope you'll find this Metric information useful.

Kind Regards,  
Adaeze Adeteye

