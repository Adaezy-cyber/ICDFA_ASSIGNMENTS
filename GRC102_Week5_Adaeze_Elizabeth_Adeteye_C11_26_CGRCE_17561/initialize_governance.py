#!/usr/bin/env python3
"""
Initializes the governance tracker with baseline policy, control, risk,
incident, metric and audit data for the simulated organisation.
"""

from governance_tracker import GovernanceTracker


def initialize_governance_data():
    tracker = GovernanceTracker()

    patch_policy_id = tracker.add_policy(
        "Patch Management Policy",
        "Policy governing the timely application of security patches",
        "CISO", "2026-01-15", "2027-01-15",
    )
    vuln_policy_id = tracker.add_policy(
        "Vulnerability Management Policy",
        "Policy governing the identification and remediation of security vulnerabilities",
        "Security Director", "2026-02-10", "2027-02-10",
    )
    incident_policy_id = tracker.add_policy(
        "Incident Response Policy",
        "Policy governing the response to security incidents",
        "CISO", "2026-03-05", "2027-03-05",
    )

    tracker.add_control(
        "Patch Management Process",
        "Process for identifying, testing, and applying security patches",
        patch_policy_id, "IT Manager", "2026-01-20",
    )
    tracker.add_control(
        "Vulnerability Scanning",
        "Regular scanning for security vulnerabilities",
        vuln_policy_id, "Security Engineer", "2026-02-15",
    )
    tracker.add_control(
        "Incident Response Team",
        "Team responsible for responding to security incidents",
        incident_policy_id, "Security Director", "2026-03-10",
    )

    tracker.add_risk(
        "Unpatched Vulnerabilities",
        "Risk of exploitation due to unpatched vulnerabilities",
        "High", "High", "Security Engineer",
        "Implement automated patch management system",
    )
    tracker.add_risk(
        "Insufficient Network Segmentation",
        "Risk of lateral movement due to insufficient network segmentation",
        "Medium", "High", "Network Engineer",
        "Implement network segmentation according to least privilege principle",
    )
    tracker.add_risk(
        "Weak Authentication",
        "Risk of unauthorized access due to weak authentication",
        "Medium", "Medium", "Identity Manager",
        "Implement multi-factor authentication",
    )

    tracker.add_incident(
        "Web Server Compromise",
        "Compromise of web server due to unpatched Struts vulnerability",
        "2026-04-15", "High", "Web Server",
        "Unpatched Struts vulnerability (CVE-2017-5638)",
        "Patched vulnerability and restored from backup",
    )

    tracker.add_metric(
        "Patch Compliance",
        "Percentage of systems with all critical patches applied",
        95.0, 85.0, "September 2026", "Improving",
    )
    tracker.add_metric(
        "Vulnerability Remediation Time",
        "Average time to remediate critical vulnerabilities (days)",
        7.0, 12.0, "September 2026", "Declining",
    )
    tracker.add_metric(
        "Security Incidents",
        "Number of security incidents in the period",
        0.0, 1.0, "September 2026", "Stable",
    )

    tracker.add_audit(
        "Annual Security Audit",
        "Comprehensive audit of security controls",
        "2026-05-01", "External Auditor",
        "Several findings related to patch management and network segmentation",
        "Improve patch management process and implement network segmentation",
    )

    print("Governance tracker initialized with sample data")


if __name__ == "__main__":
    initialize_governance_data()
