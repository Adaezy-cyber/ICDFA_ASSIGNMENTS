#!/usr/bin/env bash
# Run on the Ubuntu manager. This tool is interactive:
#   A  -> add agent, name: Finance-Dept-Workstation, IP: any, confirm
#   E  -> extract key for the agent ID, copy the key
#   Q  -> quit
sudo /var/ossec/bin/manage_agents
