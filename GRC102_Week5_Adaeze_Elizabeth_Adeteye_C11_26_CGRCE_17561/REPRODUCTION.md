# Completing the live Docker evidence

Three pieces of evidence need the containers running: the vulnerability scan, the attack-simulation log and the post-patch re-scan. I will not substitute invented output for them. This is the exact sequence I run on my Kali host.

## Why the first run failed

`docker compose up -d` failed with `manifest for vulhub/struts2:s2-045 not found`. That tag is not published on [Docker Hub](https://hub.docker.com/r/vulhub/struts2/tags). My [docker-compose.yml](docker-compose.yml) uses `vulhub/struts2:2.3.30` instead. The scripts now target `http://localhost:8080` (override with `TARGET_URL`).

## Steps

```bash
cd ~/security_governance_lab

# Docker group change needs a fresh login; confirm it worked
docker ps

# The compose file expects the external network
docker network create secgov_network   # skip if it already exists

docker compose up -d
docker ps -a                           # screenshot: all three containers "Up"

# Part 1 evidence
python3 vulnerability_scanner.py       # screenshot + keep vulnerability_report_*.json
python3 governance_tracker.py --dashboard

# Part 2 evidence
python3 simulate_attack.py             # screenshot + keep attack_log.json
python3 analyze_governance_failures.py

# Part 3 evidence: apply controls, then prove remediation
python3 implement_governance_controls.py --all
python3 vulnerability_scanner.py       # expect Struts "vulnerable": false
python3 simulate_attack.py             # expect "not vulnerable"
```

Note: the `--all` step only updates state files. To make the re-scan genuinely change, I also need to switch the web service to a patched Struts image (for example a 2.5.x tag) and recreate the container; otherwise the re-scan will still report vulnerable, and I will report that honestly.

## Where the screenshots go

- `evidence/part1_environment/` — compose run, `docker ps -a`, scan
- `evidence/part2_attack/` — attack simulation and failure analysis
- `evidence/part3_controls/` — controls run, post-patch re-scan

Then I add them to [README.md](README.md) and replace the red boxes in the PDF report.
