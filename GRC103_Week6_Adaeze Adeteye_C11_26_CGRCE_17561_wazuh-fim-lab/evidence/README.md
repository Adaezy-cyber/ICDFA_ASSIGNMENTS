# Evidence

Status note: the Wazuh manager VM could not be brought up (see `../docs/execution_log_and_challenges.md`), so no evidence has been captured yet.

Save screenshots in `screenshots/` using these names. Status stays "Not captured" until a real run is completed. Do not add images that were not taken from your own environment.

| # | File name | What it must show | Status |
| --- | --- | --- | --- |
| 1 | `01_manager_service_running.png` | `systemctl status wazuh-manager` active | Not captured |
| 2 | `02_dashboard_login.png` | Dashboard login at `https://<VM_IP>` | Not captured |
| 3 | `03_agent_active.png` | Agents page with agent Active | Not captured |
| 4 | `04_ossec_conf_syscheck.png` | The added `<directories realtime="yes">` line | Not captured |
| 5 | `05_alert_file_added.png` | Syscheck alert: file added | Not captured |
| 6 | `06_alert_file_modified.png` | Syscheck alert: file modified | Not captured |
| 7 | `07_alert_file_deleted.png` | Syscheck alert: file deleted | Not captured |

The script `scripts/03_simulate_risk_event.ps1` writes `simulation_log.csv` here, so you can match each alert to the action that caused it.

If you update this table after a successful run, also update Sections 1, 5, 6 and 8 of the main `README.md` so it no longer says the deployment was not completed.
