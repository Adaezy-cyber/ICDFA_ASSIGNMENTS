# Troubleshooting

| Problem | Likely cause | Fix |
| --- | --- | --- |
| Installer stops or reports requirements not met | VM too small | Increase RAM/CPU, or add `-i` to ignore the hardware check (lab use only) |
| Dashboard will not load | Services still starting, or wrong IP | Wait a few minutes; `sudo systemctl status wazuh-dashboard`; re-check `ip addr show` |
| VM and Windows cannot reach each other | NAT instead of bridged, or wrong adapter | Set Bridged Adapter on the correct host NIC; ping both ways |
| Agent shows Disconnected / Never connected | Wrong manager IP, wrong key, firewall, version mismatch | Re-check IP and key; allow ports 1514 and 1515; keep agent version <= manager version |
| No syscheck alerts | Folder missing at agent start, wrong path, agent not restarted | Create the folder, fix the username in `ossec.conf`, restart the agent |
| Modified-file alert missing | Actions too close together | Pause 10 seconds between actions |
| Lost admin password | Not saved after install | Re-run the password tool on the manager or reinstall |
