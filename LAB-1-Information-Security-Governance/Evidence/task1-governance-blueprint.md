# Task 1: Governance Blueprint
2
 
3
## 1.0 Executive Summary
4
 
5
Following a review of GlobalHealth Connect's current operating environment, recent acquisitions, and the reported data leakage near-miss, I assessed the organization's information security governance posture to determine whether its existing structure adequately supports business growth, regulatory obligations, and protection of sensitive healthcare information.
6
 
7
My assessment found that GHC currently operates with an informal and reactive governance model. While individual departments perform certain security-related activities, there is no dedicated governance function responsible for providing strategic oversight, risk ownership, policy coordination, or board-level reporting. As a result, accountability is fragmented, security decisions are inconsistent, and management lacks sufficient visibility into enterprise security risks.
8
 
9
To address these issues, I recommend establishing a formal Information Security Governance structure led by a Director of Information Security Governance reporting to the Chief Executive Officer. This structure introduces clear accountability, strengthens oversight, improves cross-functional collaboration, and aligns security activities with GHC's strategic business objectives.
10
 
11
---
12
 
13
# 1.1 Current-State Governance Gap Assessment
14
 
15
## Governance Gap Analysis
16
 
17
| Ref | Governance Domain | Current Observation | Root Cause | Business Impact | Risk Rating | Recommended Action |
18
|------|------------------|-------------------|------------|----------------|------------|-------------------|
19
| G-01 | Security Leadership | No dedicated security governance function exists. Security responsibilities are spread across operational teams. | Historical focus on operational IT rather than enterprise governance. | Security priorities may not receive adequate executive attention, increasing organizational risk exposure. | High | Establish a Director of Information Security Governance role reporting directly to the CEO. |
20
| G-02 | Accountability & Ownership | Security responsibilities and decision-making authority are unclear across departments. | Absence of a formal governance framework and RACI model. | Risk of duplicated efforts, unassigned tasks, and delayed decision-making. | High | Implement an enterprise-wide accountability framework supported by a documented RACI matrix. |
21
| G-03 | Policy Management | Security policies inherited from acquisitions are inconsistent and not uniformly applied. | Lack of centralized policy ownership and review process. | Increased likelihood of compliance violations and operational confusion. | High | Develop a standardized enterprise policy management framework. |
22
| G-04 | Risk Management | Security risk management activities are largely reactive. | No formal risk assessment methodology or risk register. | Emerging risks may remain unidentified until incidents occur. | High | Implement a formal risk management program and governance review cycle. |
23
| G-05 | Executive & Board Reporting | Security reporting is informal and lacks consistent key performance indicators. | Governance reporting requirements have not been defined. | Executive leadership may make decisions without a complete understanding of cyber risk exposure. | Medium-High | Establish quarterly risk and security governance reporting to the Board. |
24
| G-06 | Incident Governance | Incident response planning exists at an operational level but lacks governance oversight. | Limited executive participation in incident preparedness activities. | Delayed escalation and ineffective crisis decision-making during major incidents. | Medium-High | Introduce executive-level incident governance and escalation procedures. |
25
| G-07 | Cross-Functional Coordination | Security-related decisions are often made independently by departments. | No formal cross-functional decision-making body exists. | Conflicting priorities can create inefficiencies and increase organizational risk. | Medium | Establish a Security Steering Committee (SSC). |
26
 
27
---
28
 
29
## Business Impact Assessment
30
 
31
| Governance Gap | Regulatory Impact | Financial Impact | Operational Impact | Reputational Impact |
32
|---------------|------------------|-----------------|-------------------|--------------------|
33
| Lack of Security Leadership | Increased compliance exposure | Increased remediation costs | Delayed security decisions | Reduced stakeholder confidence |
34
| Unclear Accountability | Audit observations and governance findings | Resource inefficiencies | Inconsistent execution of controls | Perception of weak governance |
35
| Weak Risk Management | Potential regulatory breaches | Higher likelihood of financial loss from incidents | Reactive crisis management | Loss of customer trust |
36
| Inadequate Board Reporting | Reduced oversight effectiveness | Poor investment prioritization | Limited strategic visibility | Negative investor perception |
37
| Policy Inconsistency | Compliance failures | Potential penalties and legal costs | Employee confusion and inconsistent practices | Damage to organizational credibility |
38
 
39
---
40
 
41
## Governance Risk Summary
42
 
43
Based on the evidence reviewed, the most significant governance risks facing GHC are:
44
 
45
1. **Lack of clear security accountability** resulting in governance gaps and inconsistent decision-making.
46
2. **Absence of proactive risk management processes** leading to unmanaged enterprise risks.
47
3. **Insufficient Board oversight and reporting mechanisms** limiting strategic visibility into cybersecurity threats.
48
4. **Policy fragmentation caused by acquisitions** increasing compliance and operational risks.
49
 
50
Overall, I assess the current governance maturity as operating between **Level 1 (Ad Hoc)** and **Level 2 (Initial)**. The organization has some security-related activities in place; however, governance processes remain largely informal and inconsistently applied.
51
 
52
---
53
 
54
# 1.2 Proposed Information Security Governance Structure
55
 
56
## Future-State Governance Model
57
 
58
```text
59
BOARD OF DIRECTORS
60
│
61
▼
62
Chief Executive Officer (CEO)
63
│
64
▼
65
Director of Information Security Governance
66
│
67
┌──────┼───────────┬──────────┬──────────┐
68
▼ ▼ ▼ ▼ ▼
69
 
70
IT Legal & Human Finance Development
71
Operations Compliance Resources Department Department
72
Manager Officer Manager Analyst Senior Developer
73
 
74
│
75
▼
76
 
77
Security Steering Committee (SSC)
78
 
79
Members:
80
• CEO (Executive Sponsor)
81
• Director of Information Security Governance
82
• CTO
83
• IT Manager
84
• Compliance Officer
85
• HR Manager
86
• Finance Representative
87
```
88
 
89
---
90
 
91
## Governance Structure Justification
92
 
93
| Governance Principle | How the Proposed Structure Supports the Principle |
94
|---------------------|--------------------------------------------------|
95
| Accountability | Assigns clear ownership of governance activities to a dedicated security governance leader. |
96
| Transparency | Establishes formal reporting relationships between management and the Board. |
97
| Strategic Alignment | Aligns security initiatives with business objectives, growth plans, and regulatory obligations. |
98
| Risk-Based Decision Making | Provides structured oversight of enterprise security risks and mitigation activities. |
99
| Separation of Duties | Distinguishes governance oversight from day-to-day IT operations. |
100
| Cross-Functional Collaboration | Enables coordinated decision-making through the Security Steering Committee. |
101
| Continuous Improvement | Supports ongoing governance reviews, performance measurement, and maturity growth. |
102
 
103
### Governance Rationale
104
 
105
I recommend positioning the Director of Information Security Governance as an independent governance function reporting directly to the CEO. This reporting structure provides visibility at the executive level while maintaining sufficient independence from operational IT functions.
106
 
107
The establishment of a Security Steering Committee will ensure that major security decisions are reviewed from business, technical, compliance, financial, and operational perspectives. This structure reduces decision-making silos and enables balanced security investments that support GHC's strategic objectives.
108
 
109
---
110
 
111
# 1.3 RACI Matrix
112
 
113
## Governance Responsibility Matrix
114
 
115
| Governance Activity | Board | CEO | Director of Information Security Governance | IT Manager | Compliance Officer | HR Manager | CTO |
116
|-------------------|-------|-----|---------------------------------------------|------------|-------------------|-----------|-----|
117
| Security Policy Development | I | C | A/R | C | C | C | C |
118
| Security Policy Approval | A | C | R | I | C | I | I |
119
| Enterprise Risk Assessment | I | A | R | C | C | I | C |
120
| Risk Review & Acceptance | A | C | R | C | C | I | C |
121
| Compliance Monitoring | I | C | C | I | A/R | I | I |
122
| Security Awareness Programme | I | A | R | C | C | R | I |
123
| Incident Response Planning | I | A | R | R | C | C | C |
124
| Board Security Reporting | A | C | R | I | I | I | I |
125
| Third-Party Security Reviews | I | C | A/R | C | C | I | C |
126
| Governance Maturity Reviews | I | C | A/R | C | C | C | C |
127
 
128
### Key
129
 
130
- **R** = Responsible
131
- **A** = Accountable
132
- **C** = Consulted
133
- **I** = Informed
134
 
135
---
136
 
137
## RACI Analysis
138
 
139
The proposed RACI model addresses one of the most significant governance weaknesses identified during the assessment, namely the lack of clearly defined accountability. Each governance activity has a designated accountable owner, ensuring ownership cannot be transferred or ignored.
140
 
141
The model also promotes transparency by identifying stakeholders who must be consulted before major governance decisions are made. This approach reduces ambiguity, improves auditability, and strengthens organizational accountability across all business functions.
142
 
143
---
144
 
145
# 1.4 Conclusion
146
 
147
The assessment confirms that GlobalHealth Connect's current information security governance arrangements are insufficient to support the organization's ongoing growth, regulatory obligations, and risk management requirements. The primary governance challenges relate to fragmented ownership, inconsistent policies, limited executive oversight, and the absence of a formal security governance framework.
148
 
149
The proposed governance structure addresses these weaknesses by establishing dedicated governance leadership, defining accountability through a RACI model, introducing Board-level reporting, and creating a Security Steering Committee to support cross-functional decision-making. Collectively, these measures will improve accountability, transparency, business alignment, and enterprise risk management while providing a foundation for future governance maturity improvements.
