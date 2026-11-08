# Lab runbook (for completing the lab once an environment is available)

This runbook condenses the assignment brief into an ordered checklist. It is a plan, not a record of work done. **No step below has been performed yet** because the Ubuntu Server VM could not be built because my device storage limited.

Rules: use only fictional data and your own VMs; keep the lab on an isolated or host-only network; do not use bridged networking; save every output with its timestamp; never fabricate or edit evidence. If a control cannot be verified, record it as **unverified**, not failed.

## 0. Prepare

- Ubuntu Server 24.04 LTS ISO (about 2.5 GB). Check its SHA256 against the value on the download page.
- Kali Linux VM. Both VMs: 2 vCPUs, 2 to 4 GB RAM, 25 GB disk.
- Two adapters per VM: a temporary NAT adapter (package installs only) and a host-only/internal adapter (the lab network).
- **Take a clean snapshot of both VMs before starting.**

## 1. Build the baseline (Steps 1 to 3, Ubuntu console)

1. With NAT on: `sudo apt update && sudo apt install -y nginx ufw python3 curl`
2. Disconnect NAT. Record both addresses: `ip -br addr` (save as `ip-addresses.txt`).
3. Create content and the legacy service, then the Nginx site, using the commands in the brief (Steps 2 and 3).
4. `sudo nginx -t && sudo systemctl reload nginx`

## 2. Baseline evidence (Step 4, from Kali)

```
mkdir -p ~/grc-treatment-evidence && cd ~/grc-treatment-evidence
SERVER_IP=<ubuntu address>        # no angle brackets
date -Is | tee baseline-time.txt
nmap -sT -p 80,8080 "$SERVER_IP" -oN baseline-ports.txt
curl -i "http://$SERVER_IP/" | tee baseline-web.txt
curl -i "http://$SERVER_IP/archive/" | tee baseline-listing.txt
curl -i "http://$SERVER_IP/archive/dummy-records.txt" | tee baseline-file.txt
curl -i "http://$SERVER_IP:8080/" | tee baseline-legacy.txt
```
On Ubuntu also save `sudo ufw status verbose` and `sudo ss -lntp`. Then confirm the register's R1 to R4 (update scores if the evidence differs from the estimates).

## 3. Avoidance (Step 6)

Record the change first (business impact, approval role *simulated*, test, rollback). Then:
```
sudo systemctl disable --now grc-legacy
sudo systemctl is-active grc-legacy
sudo ss -lntp
```
From Kali repeat the scan and the legacy request as `avoidance-ports.txt` and `avoidance-legacy.txt`. Expected: 8080 closed, 80 still works. Rollback: `sudo systemctl enable --now grc-legacy`, test, then re-disable.

## 4. Archive hardening (Step 7)

Apply the commands and Nginx config in the brief (see `configs/reference-design/nginx-grc-lab.conf`). From Kali check and save: `/public/` = 200; `/`, `/archive/`, `/archive/dummy-records.txt` = 403.

## 5. Firewall (Step 8, Ubuntu console only)

Use `configs/reference-design/ufw-rules-plan.sh` after setting `KALI_IP`. Save `ufw status numbered`. Test from the approved address (expect 200). For the blocked source use a second VM or a second address on Kali (`ip addr add ... dev <iface>`, then remove it). Expect a timeout. Record source address and timestamp. Console rollback: `sudo ufw disable`, then reapply.

## 6. Correlate logs (Step 9)

From Kali request `/public/` then `/archive/`, noting timestamps. On Ubuntu:
```
sudo tail -n 30 /var/log/nginx/grc_access.log
sudo journalctl -k --since '15 minutes ago' | grep 'UFW BLOCK'
```
Check `/var/log/ufw.log` if the journal is empty. Repeat the blocked request and allow time (logging can be rate-limited). Fill the `Evidence_Log` sheet. Do not invent missing events.

## 7. Backup and restore (Step 10)

Follow the brief: create `/srv/grc-backups` (mode 700), tar the `public` directory, record `sha256sum` and `date -Is`, delete `index.html`, confirm from Kali the page is gone, restore, run `sha256sum -c`, `date -Is`, and confirm 200 with the original content. Enter the two timestamps in the `Recovery_Timing` sheet.

## 8. Finish

- Reassess R1 to R4 in `Residual_Register` from actual results (mark anything untested as untested).
- Update README status table, report and management summary.
- Package: one PDF report, one ZIP of outputs, configs, redacted logs, screenshots, workbook and README. No passwords, private keys or VM images.
