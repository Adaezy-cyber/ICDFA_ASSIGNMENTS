# Reproduction Steps — Completing the Live Docker Evidence

Everything in this repository that does **not** require a live Docker daemon has already been run for real and its actual output is committed (see `governance_data.json`, `patch_status.json`, `baseline_dashboard.json`, `executive_dashboard.html`, `board_report.md`, `metrics_visualizations/*.png`).

Three pieces of evidence can only be produced on your own machine, because they require the three containers (`web_server`, `database_server`, `monitoring_server`) to actually be running:

1. `vulnerability_report_*.json` (a fresh one, post-fix)
2. `attack_log.json`
3. A second vulnerability scan after Part 3's patches, proving the Struts endpoint no longer responds to the exploit header

This is intentional rather than an oversight: fabricating the contents of those files instead of running them against a live target would not be your own evidence, and this is an individually assessed lab. The good news is that the one real bug blocking you (`vulhub/struts2:s2-045` is not a valid tag) is already fixed in this repo's `docker-compose.yml`, which now pulls `vulhub/struts2:2.3.30` instead — the actual pre-patch Struts version vulnerable to S2-045 / CVE-2017-5638.

## Steps

```bash
cd ~/security_governance_lab

# You already fixed the permission issue in your screenshots via:
#   sudo usermod -aG docker $USER
# then logging out/in (or `newgrp docker`) so it takes effect — the
# earlier `newgrp docker` attempt failed because it was chained onto the
# same line as usermod with no re-login in between. Log out and back in,
# or open a fresh terminal, then confirm:
docker ps

# Bring the (now-corrected) environment up
docker compose up -d
docker ps -a   # all three containers should show "Up"

# Part 1 evidence
python3 vulnerability_scanner.py
python3 governance_tracker.py --dashboard

# Part 2 evidence
python3 simulate_attack.py
python3 analyze_governance_failures.py

# Part 3 evidence — apply controls, then re-scan to prove remediation
python3 implement_governance_controls.py --all
python3 vulnerability_scanner.py   # should now show struts "vulnerable": false
python3 simulate_attack.py         # should now show "System is not vulnerable"

# Part 4 — already generated, but you can re-run after the above:
python3 governance_metrics.py
```

Take a screenshot of each command above and its output, save them into `evidence/part1_environment/`, `evidence/part2_attack/`, and `evidence/part3_controls/` respectively (folders already created), and reference them in `README.md` and in your PDF evidence report. The eight screenshots already in `evidence/part1_environment/` cover your environment setup and troubleshooting; the corrected `docker-compose up -d` run, the three `docker ps -a` containers showing "Up", the vulnerability scan, and the attack simulation are the ones to add.

## Why this is a legitimate gap to disclose, not hide

Your screenshots show you did the right troubleshooting sequence: you hit `permission denied` on the Docker socket, correctly diagnosed it as a group-membership issue, ran `sudo usermod -aG docker $USER`, and then hit a second, unrelated blocker — the image pull itself failing with `manifest for vulhub/struts2:s2-045 not found`. That second error is not something `usermod` or `sudo` can fix, because it isn't a permissions problem — it's that the tag named in the official lab instructions does not exist in the `vulhub/struts2` registry (confirmed against Docker Hub's tag list: the maintainers only ever published this image under version tags such as `2.3.30`, not CVE/advisory IDs like `s2-045`). State this plainly in your evidence report rather than hiding it — "the Docker tag specified in the LAB_INSTRUCTIONS.md does not exist upstream; I diagnosed this from the `manifest unknown` error, corrected `docker-compose.yml` to pull `vulhub/struts2:2.3.30` (the version actually vulnerable to CVE-2017-5638), and completed the remaining evidence after that fix" is a stronger, more GRC-appropriate answer than no explanation at all, since it demonstrates exactly the kind of root-cause diagnosis this course is teaching.
