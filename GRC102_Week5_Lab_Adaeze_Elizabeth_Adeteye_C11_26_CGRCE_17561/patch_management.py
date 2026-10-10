#!/usr/bin/env python3
"""
Patch Management System
Part 3 - GRC102 Security Governance Simulation
"""

import os
import sys
import json
import argparse


def get_available_patches():
    return [
        {
            "id": "PATCH-001",
            "name": "Apache Struts2 S2-045 Patch",
            "description": "Fixes CVE-2017-5638 in Apache Struts2",
            "severity": "Critical",
            "affected_system": "web_server",
            "status": "Available",
        },
        {
            "id": "PATCH-002",
            "name": "MySQL Security Configuration",
            "description": "Secures MySQL with proper authentication and access controls",
            "severity": "High",
            "affected_system": "database_server",
            "status": "Available",
        },
        {
            "id": "PATCH-003",
            "name": "Network Segmentation Rules",
            "description": "Implements proper network segmentation between servers",
            "severity": "Medium",
            "affected_system": "all",
            "status": "Available",
        },
    ]


def apply_patch(patch_id):
    patches = get_available_patches()
    patch = next((p for p in patches if p["id"] == patch_id), None)
    if not patch:
        print(f"Error: Patch {patch_id} not found")
        return False

    print(f"Applying patch: {patch['name']} ({patch['id']})")
    print(f"Description: {patch['description']}")
    print(f"Affected system: {patch['affected_system']}")

    status_file = "patch_status.json"
    status = {}
    if os.path.exists(status_file):
        with open(status_file) as f:
            status = json.load(f)

    if patch_id == "PATCH-001":
        print("Simulating Struts patch application...")
        status["struts_patched"] = True
    elif patch_id == "PATCH-002":
        print("Simulating MySQL security configuration...")
        status["mysql_secured"] = True
    elif patch_id == "PATCH-003":
        print("Simulating network segmentation implementation...")
        status["network_segmented"] = True
    else:
        print(f"Error: Unknown patch ID {patch_id}")
        return False

    with open(status_file, "w") as f:
        json.dump(status, f, indent=2)
    print(f"{patch['name']} applied successfully")
    return True


def list_patches():
    print("Available patches:")
    print("-----------------")
    for patch in get_available_patches():
        print(f"ID: {patch['id']}")
        print(f"Name: {patch['name']}")
        print(f"Description: {patch['description']}")
        print(f"Severity: {patch['severity']}")
        print(f"Affected System: {patch['affected_system']}")
        print(f"Status: {patch['status']}")
        print()


def main():
    parser = argparse.ArgumentParser(description="Patch Management System")
    parser.add_argument("--list", action="store_true", help="List available patches")
    parser.add_argument("--apply", metavar="PATCH_ID", help="Apply a specific patch")
    args = parser.parse_args()

    if args.list:
        list_patches()
    elif args.apply:
        apply_patch(args.apply)
    else:
        parser.print_help()


if __name__ == "__main__":
    main()
