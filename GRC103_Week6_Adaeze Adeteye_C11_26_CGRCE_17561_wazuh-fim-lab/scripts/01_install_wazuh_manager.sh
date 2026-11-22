#!/usr/bin/env bash
# Run on the Ubuntu Server VM (bridged adapter, >= 4 GB RAM, 2 CPUs, ~30 GB disk).
# Commands taken from the lab document (Part 1).
set -e

# 1. Add the Wazuh GPG key
curl -s https://packages.wazuh.com/key/GPG-KEY-WAZUH | sudo gpg --dearmor -o /usr/share/keyrings/wazuh-archive-keyring.gpg

# 2. Download and run the all-in-one installer (-a = all components)
#    NOTE: -i means "ignore minimum hardware checks" (it is NOT "interactive").
#    Only add -i if the VM is under-sized.
curl -sO https://packages.wazuh.com/4.12/wazuh-install.sh
sudo bash ./wazuh-install.sh -a

# 3. Save the admin credentials printed at the end - they are shown once.
sudo systemctl status wazuh-manager --no-pager
ip addr show
