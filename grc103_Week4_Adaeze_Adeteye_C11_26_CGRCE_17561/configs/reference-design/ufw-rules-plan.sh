#!/bin/sh
# REFERENCE DESIGN ONLY - taken from the assignment brief (Step 8).
# Not captured from a running system. Not deployed. Not tested.
# Run from the Ubuntu VM CONSOLE (not SSH only). Set KALI_IP to Kali's real address.
# Console rollback: sudo ufw disable
KALI_IP=192.168.56.10   # replace with the actual Kali address
sudo ufw default deny incoming
sudo ufw default allow outgoing
sudo ufw allow from "$KALI_IP" to any port 80 proto tcp
sudo ufw logging on
sudo ufw enable
sudo ufw status numbered
