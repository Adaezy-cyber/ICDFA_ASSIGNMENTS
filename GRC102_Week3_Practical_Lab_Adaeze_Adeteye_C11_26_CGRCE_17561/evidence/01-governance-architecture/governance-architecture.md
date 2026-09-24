# Evidence Bundle 1 — Governance Architecture and Stakeholder Map

## 1. Governance Gap Assessment

TechGlobal currently operates through **security by informal decision**. The IT Director is effectively acting as security owner, risk approver and operational decision-maker. Business-unit leaders make local security choices, while formal governance forums and reliable escalation paths are absent.

| ID | Current weakness | Business / risk consequence | Governance response |
|---|---|---|---|
| G1 | Security decisions are concentrated with the IT Director. | Bottleneck and concentration-of-authority risk. | Establish CISO-led security governance with executive and Board oversight. |
| G2 | IT combines security ownership, risk approval and operational execution. | Weak independent challenge and potential self-approval. | Separate security leadership, enterprise-risk challenge, risk ownership and technical execution. |
| G3 | No formal governance committee structure. | Cross-functional issues are resolved inconsistently. | Establish Executive Security Council, Security Governance Committee and specialist Working Group. |
| G4 | Business units make local security choices inconsistently. | Uneven control maturity and risk exposure across offices. | Retain BU ownership while establishing enterprise requirements and a common escalation path. |
| G5 | CEO and Board have limited cyber-risk visibility. | Material risks may not receive timely senior attention. | Establish executive and Board cyber-risk reporting. |
| G6 | No reliable escalation path. | Material issues can remain operational too long. | Define three escalation levels and trigger criteria. |
| G7 | Accountability is implicit rather than documented. | Delays and disputes during incidents and decisions. | Implement role profiles and RACI with one Accountable role wherever practicable. |
| G8 | Decisions lack a formal governance trail. | Weak evidence of who decided what, why and whether actions closed. | Maintain decision logs linked to risks, actions and evidence. |

## 2. Stakeholder Map

| Stakeholder | Authority / Influence | Primary Interest | Information Needed | Governance Contribution |
|---|---|---|---|---|
| Board | Highest oversight | Resilience, material risk, accountability | Material risks, incidents, trends, assurance | Oversight, risk-appetite challenge and material-risk decisions |
| CEO | Executive authority | Growth, strategy and acceptable risk | Executive risk exposure, investment needs, major incidents | Executive accountability and Board escalation |
| CISO | Security governance leader | Security strategy, policy, control effectiveness | Metrics, incidents, vulnerabilities, architecture, third parties | Security strategy, policy, analysis and reporting |
| CRO / Risk | Enterprise-risk authority/challenge | Consistent risk methodology | Ratings, treatment, accepted risks | Independent challenge and enterprise aggregation |
| Legal / Compliance | Legal/regulatory adviser | Regulatory, privacy and contractual duties | Incident facts, obligations, evidence | Legal advice, notification analysis and compliance challenge |
| Finance | Financial governance | Budget, loss exposure and investment | Business cases, financial exposure | Investment challenge and prioritisation |
| HR | People governance | Workforce controls and conduct | JML status, training, policy breaches | Awareness, workforce controls and disciplinary support |
| IT / Technology | Technical delivery | Secure and reliable technology | Architecture, vulnerabilities, incidents | Technical implementation, operations and continuity |
| Business Unit Leaders | Business ownership | Business outcomes and local risk | Business impact, dependencies and controls | Business ownership, local implementation and risk input |

## 3. Security Governance Organisation Chart

```text
                         BOARD OF DIRECTORS
                                  │
                    Oversight / material-risk challenge
                                  │
                                  ▼
                                CEO
                                  │
                  Executive accountability for security
                                  │
                    EXECUTIVE SECURITY COUNCIL
                                  │
                                  ▼
                    SECURITY GOVERNANCE COMMITTEE
              ┌──────────┬────────┬─────────┬─────────┐
              ▼          ▼        ▼         ▼         ▼
            CISO       CRO/Risk   IT      Legal     Finance/HR
              │
              ▼
      Business Unit Leaders
              │
              ▼
      Operational Teams
              │
              ▼
Cloud & Technology Security Working Group
```

## 4. Consultant Justification

TechGlobal has 2,500 employees across five offices. A model centred on one IT executive is difficult to scale because security decisions increasingly involve business priorities, financial investment, people processes, legal obligations and enterprise risk.

The proposed model uses **central governance with distributed execution**. Enterprise security direction remains consistent while Business Units retain ownership of business outcomes and local implementation. This avoids creating separate security silos in each office.

The CISO becomes the central security governance leader rather than the sole risk owner. CRO/Risk provides enterprise-risk challenge and aggregation. Legal/Compliance, Finance, HR and IT contribute specialist authority within their domains. The CEO provides executive decision authority and connects material security matters to the Board.

The committee ecosystem creates repeatable decision forums. The RACI matrix converts the structure into explicit decision rights. The escalation model ensures that risk moves beyond operational management when authority, impact or materiality requires it.

The design also improves auditability: a material decision can be traced from identification through assessment, decision authority, treatment, review and closure rather than relying on informal conversations or individual memory.
