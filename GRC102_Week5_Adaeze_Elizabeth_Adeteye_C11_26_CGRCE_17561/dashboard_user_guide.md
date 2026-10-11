# Security Governance Dashboard User Guide

## Overview

This guide explains how to use the Security Governance Executive Dashboard (`executive_dashboard.html`), built for executives and board members who need a fast read on the organisation's security governance posture without digging into raw JSON.

## Accessing the Dashboard

Open `executive_dashboard.html` directly in any web browser (double-click it, or `File > Open`). No server is required — it is a self-contained static file that references the PNG charts in `metrics_visualizations/`, so keep both in the same relative folder structure as shipped in this repository.

## Dashboard Sections

1. **Security Posture Summary** — overall rating plus the five headline metrics (patch compliance, remediation time, incidents, monitoring coverage, policy compliance).
2. **Risk Summary** — count of open risks by severity, pulled from `governance_data.json`.
3. **Compliance Summary** — policy compliance, control effectiveness, open audit findings.
4. **Trend Visualisations** — six-month trend per metric, each with its target line.
5. **Key Recommendations** — the current cycle's suggested next actions.

## Interpreting the Dashboard

- **Green** values are meeting or exceeding target.
- **Yellow/Warning** values are below target but within an acceptable range.
- **Red/Critical** values are significantly below target and need immediate attention.
- Each trend chart's dashed line is the target — a line crossing above the target on an "improving is higher" metric (patch compliance) is good news; crossing above target on a "lower is better" metric (remediation time, incidents) is a problem.

## Using the Dashboard for Decision-Making

1. **Spot issues** — any card in yellow/red deserves board attention before the next cycle.
2. **Track progress** — the trend charts show whether a prior remediation (e.g., the Part 3 patch rollout) actually moved the needle, not just whether it was announced.
3. **Prioritise** — use the Risk Summary to decide which open risk gets mitigation budget first.
4. **Demonstrate compliance** — the Compliance Summary card is the quickest artefact to show an auditor or regulator.

## Refreshing the Dashboard

Run `python3 governance_metrics.py` again after each monthly cycle (or after any control change you want reflected). It regenerates `metrics_visualizations/*.png`, `executive_dashboard.html` and `board_report.md` from the current contents of `governance_data.json` and `patch_status.json`, so make sure those are up to date first.

## Conclusion

The dashboard is deliberately a thin presentation layer over `governance_data.json`, `patch_status.json` and the vulnerability/attack logs — it has no logic of its own, so if a number looks wrong the fix is always in the underlying governance tracker data, not the HTML.
