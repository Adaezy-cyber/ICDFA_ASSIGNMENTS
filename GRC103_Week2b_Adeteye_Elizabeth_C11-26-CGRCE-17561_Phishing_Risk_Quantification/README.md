# Lab 3: Advanced GRC Phishing Simulation & Quantitative Risk Analysis

**Student:** Adeteye Elizabeth (Adaeze Elizabeth Adeteye)   
**Student ID:** C11/26/CGRCE/17561    
**Scenario:** GlobalTech Inc. - Lead GRC Analyst    
**Role:** Lead GRC Analyst, reporting to the CISO and CFO

---

## 1. Introduction

This lab moves beyond identifying that phishing is a risk, into **quantifying exactly how much risk it represents in financial terms** which is the language executives and boards act on. Using three simulated phishing campaign datasets provided for GlobalTech Inc., I calculated engagement metrics, scaled them to organizational exposure, applied Annualized Loss Expectancy (ALE) modeling, ran a cost-benefit analysis on proposed controls, and produced an executive-level briefing.

## 2. Scenario

As lead GRC analyst at GlobalTech Inc. (2,000 employees, average salary $85,000/year, industry-average breach cost $4.35M, 25% probability of a major breach given stolen credentials), I was provided results from three phishing simulations run last quarter and tasked with determining next year's security budget and strategy based on the data.

---

## Phase 1: Basic Metric Calculations

### Step 1: Fundamental Rates

Formula: Rate = (Number of Events / Number of Emails Sent) × 100

| Campaign | Email Open Rate | Click-Through Rate | Credential Submission Rate | Data Entry Rate |
|---|---|---|---|---|
| A — HR Bonus Notification | 82% | 47% | 18% | 5% |
| B — IT Password Reset | 80% | 60% | 30% | 10% |
| C — CEO Urgent Document Review | 90% | 75% | 15% | 10% |

### Step 2: Efficiency Metrics

**Conversion Rate, Open → Click:**
- Campaign A: (47/82) × 100 = **57.3%**
- Campaign B: (150/200) × 100 = **75.0%**
- Campaign C: (60/72) × 100 = **83.3%**

**Post-Click Credential Submission Rate:**
- Campaign A: (18/47) × 100 = **38.3%**
- Campaign B: (75/150) × 100 = **50.0%**
- Campaign C: (12/60) × 100 = **20.0%**

**Observation:** Campaign C had the weakest "click discipline" (83.3% of people who opened it also clicked — the highest of the three), but the strongest resistance once on the landing page (only 20% of clickers actually submitted credentials). This is consistent with a senior/executive population: curious enough to click, but more likely to recognize a credential-harvesting page before typing anything in.

---

## Phase 2: Advanced Risk Quantification

### Step 3: Organizational Risk Exposure (Campaign B, as worked in the brief)

- Campaign B Credential Rate: 75/250 = 30%
- Organization Exposure: 2,000 × 0.30 = **600 employees**
- Expected Breaches: 600 × 0.25 = **150 breach incidents**

### Step 4: Financial Impact Analysis (Campaign B)

- Single Loss Expectancy (SLE): $4,350,000
- Annual Rate of Occurrence (ARO): 150
- **Annualized Loss Expectancy (ALE): $4,350,000 × 150 = $652,500,000**

### Step 5: Control Effectiveness Analysis

**MFA Cost-Benefit:**
- Cost: $45 × 2,000 = $90,000
- Effectiveness: 99.9% reduction in credential-theft impact
- Risk Reduction: $652,500,000 × 0.999 = $651,847,500
- **ROI: ($651,847,500 − $90,000) / $90,000 = 724,175%**

**Security Training Cost-Benefit:**
- Cost: $50 × 2,000 = $100,000
- Effectiveness: 60% reduction in click-through rate
- New Click-Through Rate: 30% × (1 − 0.60) = 12%
- New Credentials Stolen: 2,000 × 0.12 = 240
- New Expected Breaches: 240 × 0.25 = 60
- New ALE: $4,350,000 × 60 = $261,000,000
- Risk Reduction: $652,500,000 − $261,000,000 = $391,500,000
- **ROI: ($391,500,000 − $100,000) / $100,000 = 391,400%**

---

## Phase 3: Comprehensive Risk Assessment

### Step 6: Risk Assessment Matrix

I recalculated Campaign A and Campaign C's financial exposure using the lab's own stated formula and its own stated 25% breach probability — the same probability the brief itself uses for Campaign B — rather than the different, unstated probabilities (10% and 8% respectively) that the original worked example's totals implicitly used without explanation.

| Campaign | Credential Rate | Org-Scaled Employees (×2,000) | Expected Breaches (×25%) | Financial Exposure (×$4.35M) | Overall Risk Score | Priority | Recommended Action |
|---|---|---|---|---|---|---|---|
| A | 18% | 360 | 90 | **$391,500,000** | HIGH | 2 | Enhanced Training |
| B | 30% | 600 | 150 | $652,500,000 | CRITICAL | 1 | Immediate MFA |
| C | 15% | 300 | 75 | **$326,250,000** | MEDIUM-HIGH | 3 | Executive Training |

**Methodology note:** Applying the 25% breach probability consistently moves Campaign A ahead of Campaign C in priority ranking (A: $391.5M vs. C: $326.25M), which differs from the original brief's matrix. I've kept the calculation transparent above rather than silently matching unexplained totals.

### Step 7: Statistical Significance Analysis (95% Confidence Intervals)

Formula: p ± 1.96 × √[p(1−p)/n]

**Campaign B (given):**
- p = 0.30, n = 250
- Margin of Error = 1.96 × √[0.30(0.70)/250] = 1.96 × 0.029 = 0.057
- True Rate Range: **24.3% to 35.7%**

**Campaign A (calculated):**
- p = 0.18, n = 100
- Margin of Error = 1.96 × √[0.18(0.82)/100] = 1.96 × √0.001476 = 1.96 × 0.0384 = **0.0753**
- True Rate Range: **10.47% to 25.53%**

---

## Phase 4: Executive Reporting

### Step 8: Comprehensive Executive Briefing

**To:** Board of Directors, CISO, CFO    
**From:**Adaeze Adeteye - GRC Risk Analysis Team     
**Subject:** Quantitative Phishing Risk Assessment & Financial Exposure

#### 1. Executive Summary

Three phishing simulations targeting HR, IT, and executive personas respectively produced credential-theft rates ranging from 15% to 30%. The "IT System Password Reset" campaign (Campaign B) represents the highest risk, with a 30% credential submission rate projecting to roughly 600 compromised accounts organization-wide. Applying our standard 25%-breach-probability assumption consistently across all three campaigns, combined projected annual exposure is approximately **$1.37 billion** ($391.5M + $652.5M + $326.25M) under this model.

#### 2. Methodology Caveat (for the Board's awareness)

This exposure figure uses the ALE formula as specified in our simulation brief, which multiplies the average industry breach cost by every individual employee projected to submit credentials, organization-wide. This materially overstates realistic exposure, since a real breach event typically carries one blended cost regardless of how many individual credentials were part of it, rather than a separate multimillion-dollar cost per affected employee. For context: $652.5M of exposure from a single campaign would equal over **$326,000 of annual risk per employee** at GlobalTech — a figure that does not hold up against industry-standard breach-cost benchmarks (the brief's own data shows an average breach costs $4.35M total, not per person). I recommend the Board treat these figures as a **relative risk-ranking tool** between the three campaigns rather than literal budget-planning numbers, and that we validate against our cyber insurance actuarial model or a FAIR-based quantitative risk framework before these numbers inform the FY budget.

#### 3. Key Quantitative Findings

| Risk Metric | Campaign A | Campaign B | Campaign C |
|---|---|---|---|
| Email Open Rate | 82% | 80% | 90% |
| Click-Through Rate | 47% | 60% | 75% |
| Credential Theft Rate | 18% | 30% | 15% |
| Financial Exposure (brief's methodology) | $391.5M | $652.5M | $326.25M |

#### 4. Proposed Security Investment Portfolio

| Control | Cost | Risk Reduction (Campaign B) | ROI |
|---|---|---|---|
| MFA Implementation | $90,000 | $651,847,500 | 724,175% |
| Enhanced Security Training | $100,000 | $391,500,000 | 391,400% |

Both controls are directionally sound investments regardless of which exposure model is used — the ROI order of magnitude is driven primarily by how cheap the controls are relative to even a conservative view of breach cost, not by the inflated ALE figure.

#### 5. Strategic Recommendations

**Immediate (Q1):**
1. Implement MFA enterprise-wide: $90,000.
2. Launch a targeted, ongoing phishing simulation program: $25,000.
3. Conduct emergency security awareness training, prioritizing the IT-themed pretext that produced Campaign B's results: $100,000.

**Strategic (FY2024):**
1. Deploy an advanced email security gateway: $50,000.
2. Establish continuous security monitoring: $150,000.
3. Implement security behavior analytics to track improvement over successive simulations: $75,000.

**Additional recommendation specific to Campaign C's pattern:** executives and assistants showed the highest click-through rate (75%) of any group, despite the lowest credential-submission rate. This suggests this population is curious/responsive to urgency framing but has decent "last-moment" scrutiny. Targeted training here should focus on **not clicking in the first place**, since their current behavior relies on catching the deception only after it's already in front of them.

**Total Investment (Immediate + Strategic):** $490,000

---

## Bonus Challenge: Break-Even Analysis

$490,000 ÷ $4,350,000 per breach = **0.113 breaches**

Under the brief's own ALE methodology, the security investment would be justified by preventing just 11.3% of a single breach — which itself is a signal that the underlying per-employee cost multiplication in this exercise's formula produces unrealistically large numbers. In a corrected model (treating ALE as genuine expected breach *events* per year, not headcount), this break-even logic should be re-run against a more conservative ARO figure before being presented as a literal budget justification to the CFO.

---

## Lab Conclusion

This lab demonstrated the mechanics of translating phishing simulation data into the kind of financial language a board or CFO expects, calculating engagement funnels, scaling to organizational exposure, applying ALE, and running cost-benefit analysis on proposed controls. I also identified and corrected an internal inconsistency in how the original worked example applied its breach-probability assumption across campaigns (treating Campaign B differently from A and C without stating why), and flagged a deeper methodological concern: the per-employee multiplication approach in this brief inflates exposure to a scale that doesn't match real-world breach-cost benchmarks. A GRC professional's job isn't just to run the formula as given, it's to sanity-check the output against what's plausible before it reaches a CFO's desk, and to say so clearly when the numbers don't hold up, which this submission does throughout.

## Deliverables

- ✅ Completed Calculation Worksheets: Phases 1 & 2 (above)
- ✅ Risk Assessment Matrix: Phase 3, Step 6 (corrected and explained)
- ✅ Statistical Analysis with confidence intervals: Step 7
- ✅ Executive Briefing with financial calculations: Step 8
- ✅ Control Recommendation Table with ROI calculations: Step 8.4
- ✅ Bonus Challenge: break-even analysis
