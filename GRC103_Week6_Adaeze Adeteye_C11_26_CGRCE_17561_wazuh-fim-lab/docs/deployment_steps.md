# Deployment and Verification Guide

## Before you start
- VM: Ubuntu Server 20.04+, **bridged adapter** (select the adapter your host really uses), 4 GB+ RAM, 2 CPUs, ~30 GB disk.
- Windows host with administrator access.
- Take screenshots as you go (see `../evidence/README.md`).

## Part 1 - Manager (Ubuntu)
1. Run `scripts/01_install_wazuh_manager.sh` (or the two commands in the lab document).
2. Copy the admin username and password printed at the end of the install. They are shown once.
3. `sudo systemctl status wazuh-manager` should show `active (running)`.
4. Management commands: `sudo systemctl restart|stop|start|status wazuh-manager`.

## Part 2 - Dashboard
1. `ip addr show` and note the VM IP.
2. On Windows browse to `https://<VM_IP>`, accept the certificate warning, log in as `admin`.

## Part 3 - Windows agent
1. Download `wazuh-agent-4.12.0-1.msi` from the link in the lab document.
2. Install with default settings. Keep the agent version at or below the manager version.

## Part 4 - Registration
1. On Ubuntu run `scripts/02_register_agent_on_manager.sh`: `A` (add), name `Finance-Dept-Workstation`, IP `any`, confirm, then `E` (extract) and copy the key.
2. On Windows open Wazuh Agent Manager, Management tab: paste the key, enter the Ubuntu VM IP as the manager address, Apply, Restart.
3. Verify in Dashboard > Agents: the agent should show Active (green).

## Part 6 step 1 (do this first) - Create the folder
Create `C:\Users\<YourName>\SensitiveFiles`.

## Part 5 - Detective control (FIM)
1. Open `C:\Program Files (x86)\ossec-agent\ossec.conf` as Administrator.
2. Inside the `<syscheck>` block add the line from `config/ossec_syscheck_snippet.xml` with **your** username (the lab document still contains another student's path).
3. Restart the agent (Agent Manager or `services.msc`).

## Part 6 - Verify
1. Run `scripts/03_simulate_risk_event.ps1` in PowerShell. It creates, modifies and deletes `Q4_Financial_Forecast.docx` with a pause between actions and logs the times.
2. In the dashboard open the events / file integrity monitoring view and filter `rule.groups: syscheck`.
3. Open each alert and screenshot the path, action, timestamp and checksums.
4. Match alert times to `evidence/simulation_log.csv`.
