# Evidence Bundle 03 — User Access Request Procedure

## Document Control

| Field | Detail |
|---|---|
| **Document Title** | User Access Request Procedure |
| **Document ID** | NTS-ISP-PRO-001 |
| **Version** | 1.0 |
| **Owner** | Information Security Manager |
| **Status** | Approved |
| **Effective Date** | 18 September 2026 |
| **Review Date** | 18 September 2027 |

## 1. Purpose

This procedure establishes a consistent process for requesting, approving, provisioning, reviewing, and recording user access to NexusTech systems and information.

The objective is to support least privilege, role-based access, accountability, and an auditable record of access decisions.

## 2. Scope

This procedure applies to employees, contractors, consultants, interns, and other authorised users requiring access to NexusTech systems or information.

## 3. Prerequisites

Before access is provisioned, the request should identify:

- the user and relevant employment/engagement status;
- the requested system or resource;
- the business purpose;
- the required role or access level;
- the user's manager;
- the relevant system or data owner;
- any additional approval required for sensitive resources.

## 4. Procedure

### Step 1 — Receive the Request

Access requests must be submitted through the approved service-management ticket or workflow.

Requests submitted through informal channels should be redirected to the approved workflow before access is granted, except where the emergency process applies.

### Step 2 — Verify the User

The responsible IT/service desk function verifies that the requester is an authorised NexusTech user and that the request relates to an active engagement.

### Step 3 — Verify Approvals

The request must contain the required manager approval and, where applicable, system/data-owner approval.

Requests lacking required approval are returned for completion rather than provisioned.

### Step 4 — Determine the Appropriate Role

The responsible team determines the minimum access required for the user's job function.

Access should follow:

- **role-based access control** where applicable;
- **least privilege**;
- separation of incompatible duties where relevant; and
- relevant security/classification requirements.

### Step 5 — Provision Access

IT provisions the approved access using the organisation's authorised identity and access-management mechanisms.

The procedure does not prescribe vendor-specific configuration steps; those belong in technical procedures or standards where required.

### Step 6 — Perform a Post-Provisioning Check

The responsible team confirms that the access granted matches the approved request and that no unnecessary permissions were introduced.

### Step 7 — Notify the User and Manager

The user and relevant manager are notified that access has been provisioned and, where appropriate, reminded of their responsibilities for protecting the account and information.

### Step 8 — Capture Evidence

The access record should retain appropriate evidence, such as:

- request details;
- approval evidence;
- system/resource requested;
- role or permission level;
- provisioning date;
- responsible approver/provisioner;
- relevant completion notes.

### Step 9 — Close the Request

Once provisioning and verification are complete, the ticket/workflow is updated and closed with sufficient evidence to support future review or audit.

## 5. Emergency Access

Emergency access may be granted where delay could create significant operational, safety, security, or business impact.

Emergency access must:

1. be justified and recorded;
2. use the minimum necessary privilege;
3. be time-limited where technically possible;
4. receive retrospective review/approval where prior approval was not possible; and
5. be removed when the emergency requirement ends.

## 6. Exceptions

Any non-standard access request should be documented and risk-assessed. The exception should identify the business justification, scope, owner, approval authority, compensating controls where applicable, and expiry/review date.

## 7. Records and Audit Trail

Access requests and approval evidence must be retained according to NexusTech's applicable records-retention requirements.

Records should be sufficiently complete to demonstrate who requested access, who approved it, what access was granted, and when it was granted.

## 8. Process Flow

```text
Access Request
      │
      ▼
Verify User
      │
      ▼
Check Required Approvals
      │
      ├── Missing ──► Return for Approval
      │
      ▼
Determine Role / Least Privilege
      │
      ▼
Provision Approved Access
      │
      ▼
Post-Provisioning Check
      │
      ▼
Notify User + Manager
      │
      ▼
Capture Evidence
      │
      ▼
Close Ticket / Workflow
```
