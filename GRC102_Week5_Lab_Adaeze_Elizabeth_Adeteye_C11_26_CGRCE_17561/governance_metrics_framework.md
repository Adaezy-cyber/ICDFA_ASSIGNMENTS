# Security Governance Metrics Framework

## Overview

This document defines the metrics framework implemented by `governance_metrics.py` to support ongoing governance oversight of the simulated organisation.

## Metrics Categories

### 1. Implementation Metrics
Measure the extent to which controls are actually in place.
- **Patch Compliance** — % of systems with all critical patches applied.
- **Security Monitoring Coverage** — % of critical systems covered by monitoring.
- **Policy Compliance** — % of policies fully implemented and enforced.

### 2. Effectiveness Metrics
Measure how well controls perform once implemented.
- **Vulnerability Remediation Time** — average days to remediate a critical vulnerability.
- **Security Incidents** — count per reporting period.
- **Control Effectiveness** — % of controls operating as designed.

### 3. Efficiency Metrics
Measure the resource cost of maintaining the program (tracked qualitatively in this simulation; not plotted, since the lab has no payroll/headcount data source).
- Security cost per employee, security staff ratio, automation level.

### 4. Impact Metrics
Measure business consequences of security events.
- Security incident cost, business disruption hours, customers affected.

## Metric Definitions

Each metric is defined by: Name, Description, Formula, Target, Data Source, Frequency, Owner, Audience. In this simulation:

| Metric | Formula | Target | Data Source | Frequency | Owner |
|---|---|---|---|---|---|
| Patch Compliance | patched systems ÷ total systems × 100 | 95% | `patch_status.json` | Monthly | Security Engineer |
| Vulnerability Remediation Time | mean(days between detection and `patch_status.json` update) | 7 days | `vulnerability_report_*.json` | Monthly | Security Engineer |
| Security Incidents | count of `INC-*` entries in period | 0 | `governance_data.json` | Monthly | CISO |
| Monitoring Coverage | monitored containers ÷ total containers × 100 | 95% | `monitoring/` config | Monthly | Security Engineer |
| Policy Compliance | enforced policies ÷ total policies × 100 | 95% | `governance_data.json` | Monthly | CISO |

## Reporting Framework

1. **Executive Dashboard** (`executive_dashboard.html`) — posture summary, risk summary, compliance summary, trend charts, recommendations, for senior executives.
2. **Board Report** (`board_report.md`) — fuller narrative version for the board, including program improvements and recommendations.
3. **Operational Reports** — the raw `vulnerability_report_*.json`, `governance_failure_report_*.json` and `governance_data.json` files, for the security/IT team.

## Metrics Lifecycle

Define → Collect → Analyze → Report → Act → Review. In this simulation this maps to: define targets in `governance_tracker.add_metric()` → collect from `patch_status.json`/scan output → `governance_metrics.py` analyzes and charts → dashboard/board report publish → `implement_governance_controls.py` acts on gaps → metrics re-run next period.

## Note on the Historical Trend

The five months preceding the current one are generated with a seeded random distribution (per the original lab script), since no real historical telemetry exists for a lab environment created this week. The current month's values are the actual output of `patch_status.json` and `governance_data.json` after Part 3. This is documented here rather than hidden, since an auditor reviewing real metrics should always be able to tell which numbers are measured and which are illustrative baseline.

## Continuous Improvement

Metrics are reviewed for relevance each reporting cycle; new metrics are added as new risks are identified, and targets are revisited as the risk landscape changes — for example, the 7-day remediation target would typically tighten for internet-facing systems relative to internal-only ones.
