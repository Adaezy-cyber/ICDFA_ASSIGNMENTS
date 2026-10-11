#!/usr/bin/env python3
"""
Governance Control Implementation
Part 3 - GRC102 Security Governance Simulation
"""

import os
import json
import datetime
import subprocess
import argparse
from governance_tracker import GovernanceTracker


def implement_patch_management():
    print("Implementing patch management controls...")
    subprocess.run(["python3", "patch_management.py", "--apply", "PATCH-001"], check=True)

    tracker = GovernanceTracker()
    control_id = tracker.add_control(
        "Automated Patch Management",
        "Automated system for identifying, testing, and applying security patches",
        "POL-001", "Security Engineer",
        datetime.datetime.now().strftime("%Y-%m-%d"),
    )
    metric_id = tracker.add_metric(
        "Critical Patch Compliance",
        "Percentage of systems with critical patches applied within 7 days",
        100.0, 100.0, datetime.datetime.now().strftime("%B %Y"), "Improved",
    )
    print(f"Patch management controls implemented. Control ID: {control_id}, Metric ID: {metric_id}")
    return True


def implement_network_segmentation():
    print("Implementing network segmentation controls...")
    subprocess.run(["python3", "patch_management.py", "--apply", "PATCH-003"], check=True)

    tracker = GovernanceTracker()
    control_id = tracker.add_control(
        "Network Segmentation",
        "Implementation of network segmentation according to least privilege principle",
        "POL-001", "Network Engineer",
        datetime.datetime.now().strftime("%Y-%m-%d"),
    )
    print(f"Network segmentation controls implemented. Control ID: {control_id}")
    return True


def implement_database_security():
    print("Implementing database security controls...")
    subprocess.run(["python3", "patch_management.py", "--apply", "PATCH-002"], check=True)

    tracker = GovernanceTracker()
    control_id = tracker.add_control(
        "Database Security",
        "Implementation of strong authentication and access controls for databases",
        "POL-001", "Database Administrator",
        datetime.datetime.now().strftime("%Y-%m-%d"),
    )
    print(f"Database security controls implemented. Control ID: {control_id}")
    return True


def implement_security_monitoring():
    print("Implementing security monitoring controls...")
    os.makedirs("monitoring", exist_ok=True)

    monitoring_script = """#!/bin/bash
# Security Monitoring Script - polls for suspicious activity every 5 minutes via cron

grep -i "Content-Type.*multipart/form-data" /var/log/nginx/access.log > /tmp/suspicious_requests.log 2>/dev/null

mysql -u root -ppassword -e "SHOW PROCESSLIST" > /tmp/database_access.log 2>/dev/null

find /var/www -type f -mtime -1 > /tmp/recent_file_changes.log 2>/dev/null

if [ -s /tmp/suspicious_requests.log ]; then
    echo "ALERT: Suspicious HTTP requests detected" >> /tmp/security_alerts.log
fi

if grep -q "customer_data" /tmp/database_access.log 2>/dev/null; then
    echo "ALERT: Access to customer_data database detected" >> /tmp/security_alerts.log
fi

if [ -s /tmp/recent_file_changes.log ]; then
    echo "ALERT: Recent file changes detected" >> /tmp/security_alerts.log
fi
"""
    with open("monitoring/security_monitor.sh", "w") as f:
        f.write(monitoring_script)
    os.chmod("monitoring/security_monitor.sh", 0o755)

    with open("monitoring/security_cron", "w") as f:
        f.write("*/5 * * * * /monitoring/security_monitor.sh\n")

    tracker = GovernanceTracker()
    control_id = tracker.add_control(
        "Real-time Security Monitoring",
        "Implementation of real-time security monitoring and alerting",
        "POL-001", "Security Engineer",
        datetime.datetime.now().strftime("%Y-%m-%d"),
    )
    metric_id = tracker.add_metric(
        "Security Monitoring Coverage",
        "Percentage of critical systems covered by security monitoring",
        100.0, 100.0, datetime.datetime.now().strftime("%B %Y"), "Improved",
    )
    print(f"Security monitoring controls implemented. Control ID: {control_id}, Metric ID: {metric_id}")
    return True


def implement_governance_oversight():
    print("Implementing governance oversight controls...")
    oversight_doc = """# Security Governance Oversight

## Executive Responsibilities

- CEO: Ultimate accountability for security governance
- CISO: Day-to-day responsibility for the security program
- CIO: Responsibility for IT infrastructure security
- CFO: Responsibility for security budget

## Board Oversight

- Quarterly security briefings to the board
- Annual security program review by the board
- Security committee of the board established

## Reporting Structure

- CISO reports to CEO with a dotted line to CIO
- Security team reports to CISO
- Clear escalation paths for security issues, with named owners and SLAs

## Accountability

- Performance metrics tied to named individual responsibilities (addresses the
  Equifax finding that no single person was accountable for confirming the
  Struts patch was applied)
- Regular security performance reviews
- Defined consequences for missed patch/remediation SLAs
"""
    with open("governance_oversight.md", "w") as f:
        f.write(oversight_doc)

    tracker = GovernanceTracker()
    policy_id = tracker.add_policy(
        "Security Governance Oversight",
        "Policy defining security governance roles, responsibilities, and oversight",
        "CEO", datetime.datetime.now().strftime("%Y-%m-%d"),
        (datetime.datetime.now() + datetime.timedelta(days=365)).strftime("%Y-%m-%d"),
    )
    control_id = tracker.add_control(
        "Executive Security Oversight",
        "Implementation of executive and board oversight of the security program",
        policy_id, "CEO", datetime.datetime.now().strftime("%Y-%m-%d"),
    )
    print(f"Governance oversight controls implemented. Policy ID: {policy_id}, Control ID: {control_id}")
    return True


def verify_controls():
    print("Verifying security controls...")

    if os.path.exists("patch_status.json"):
        with open("patch_status.json", "r") as f:
            patch_status = json.load(f)
        print(f"Struts patched: {patch_status.get('struts_patched', False)}")
        print(f"MySQL secured: {patch_status.get('mysql_secured', False)}")
        print(f"Network segmented: {patch_status.get('network_segmented', False)}")
    else:
        print("Patch status not available")

    print("Security monitoring script implemented"
          if os.path.exists("monitoring/security_monitor.sh")
          else "Security monitoring script not implemented")
    print("Governance oversight document implemented"
          if os.path.exists("governance_oversight.md")
          else "Governance oversight document not implemented")

    tracker = GovernanceTracker()
    print(f"Policies: {len(tracker.list_policies())}")
    print(f"Controls: {len(tracker.list_controls())}")
    print(f"Metrics: {len(tracker.list_metrics())}")

    # Re-running the live vulnerability scan here requires the Docker
    # containers to be up (see REPRODUCTION.md). It is intentionally not
    # invoked automatically so this script can be reviewed/run without Docker.
    print("NOTE: run ./vulnerability_scanner.py separately against the live "
          "containers to produce post-control verification evidence.")

    return True


def main():
    parser = argparse.ArgumentParser(description="Implement Security Governance Controls")
    parser.add_argument("--all", action="store_true")
    parser.add_argument("--patch", action="store_true")
    parser.add_argument("--network", action="store_true")
    parser.add_argument("--database", action="store_true")
    parser.add_argument("--monitoring", action="store_true")
    parser.add_argument("--oversight", action="store_true")
    parser.add_argument("--verify", action="store_true")
    args = parser.parse_args()

    if args.all or args.patch:
        implement_patch_management()
    if args.all or args.network:
        implement_network_segmentation()
    if args.all or args.database:
        implement_database_security()
    if args.all or args.monitoring:
        implement_security_monitoring()
    if args.all or args.oversight:
        implement_governance_oversight()
    if args.all or args.verify:
        verify_controls()


if __name__ == "__main__":
    main()
