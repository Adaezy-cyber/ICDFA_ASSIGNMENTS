# Evidence Bundle 01: Policy Hierarchy and Categorisation

## 1. Document Hierarchy

| Document Type | Purpose | Authority | Mandatory or Recommended | Level of Detail |
|---|---|---|---|---|
| **Policy** | Establishes management intent, direction, and broad security requirements. | Highest governance authority within this hierarchy. | Mandatory. | High-level; states what must be achieved and why. |
| **Standard** | Converts policy intent into specific, measurable requirements. | Mandatory organisational requirement under the relevant policy. | Mandatory. | More specific than policy; defines required controls or minimums. |
| **Procedure** | Defines the approved sequence for carrying out a process. | Operational authority under the relevant policy/standard. | Mandatory when the procedure applies. | Detailed enough to support consistent execution. |
| **Guideline** | Provides recommended practices that help users apply security requirements appropriately. | Advisory. | Recommended unless adopted as a mandatory requirement elsewhere. | Practical guidance without the same authority as a policy or standard. |

### Why the separation matters

The old "IT Rules" document mixes governance intent with implementation instructions and recommendations. Separating the layers makes it clearer **what the organisation requires, what minimum control must exist, how a process is performed, and what good practice is recommended**.

## 2. Categorisation of the Eight Statements

| # | Statement | Classification | Justification |
|---|---|---|---|
| 1 | All employees must use MFA when accessing corporate network remotely. | **Policy** | It establishes a mandatory security requirement for a defined activity without prescribing technical implementation steps. |
| 2 | To configure MFA on mobile, download Authenticator app, scan QR, enter 6-digit code. | **Procedure** | It gives sequential implementation instructions for completing a specific task. |
| 3 | Recommended developers use parameterised queries to reduce SQL injection risk. | **Guideline** | The wording is explicitly advisory and recommends a good security practice. |
| 4 | NexusTech committed to protecting confidentiality, integrity, availability of all client data. | **Policy** | It expresses management intent and the organisation's security direction at a high level. |
| 5 | All corporate laptops must have full-disk encryption using BitLocker (Windows) or FileVault (macOS). | **Standard** | It defines a mandatory, specific and measurable technical control requirement. |
| 6 | Employees should avoid public unsecured Wi-Fi when travelling. | **Guideline** | "Should" indicates recommended behaviour rather than a mandatory control requirement. |
| 7 | In suspected security breach, employees must immediately contact IT Helpdesk extension 5555. | **Procedure** | It specifies an immediate operational action and reporting route for a defined incident situation. |
| 8 | Passwords minimum 14 chars with upper/lower/number/special. | **Standard** | It establishes a specific minimum technical requirement that can be measured and enforced. |

> **Governance note:** Statement 7 is classified as a procedure because it gives an immediate operational action. The broader requirement to report suspected incidents would normally be established at policy level, with the reporting workflow documented in a procedure.

## 3. Hierarchy Flow

```text
                    SECURITY POLICY
                           │
                           ▼
                       STANDARDS
                           │
              ┌────────────┴────────────┐
              ▼                         ▼
         PROCEDURES                 GUIDELINES
              │                         │
              └──────────┬──────────────┘
                         ▼
                 Consistent Practice
```

### Governance principle

Policies establish intent and requirements. Standards make requirements specific and measurable. Procedures support consistent execution. Guidelines help users apply security practices appropriately.
