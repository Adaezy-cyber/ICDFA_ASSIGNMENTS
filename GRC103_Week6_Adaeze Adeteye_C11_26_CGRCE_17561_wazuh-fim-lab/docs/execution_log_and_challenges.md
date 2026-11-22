# Execution Log and Challenges

**Student:** Adaeze Elizabeth Adeteye | **Registration number:** C11/26/CGRCE/17561
**Lab:** GRC103 Practical Risk Monitoring with Wazuh | **Period:** 18-22 November 2026

This log records what was attempted and why the live deployment could not be completed. It describes only issues that actually occurred.

| # | Stage | What happened | Cause / assessment | Corrective action taken or planned | Status |
| --- | --- | --- | --- | --- | --- |
| 1 | Obtain Ubuntu Server | Ubuntu Server (26.04.1 LTS) image downloaded successfully. | n/a | n/a | Done |
| 2 | Access the downloaded file | Windows displayed "Smart App Control blocked a file that may be unsafe". | Smart App Control blocks unsigned or low-reputation files from the internet. It cannot be overridden per file. | Options considered: use the Microsoft Store or signed installers, or switch Smart App Control off (irreversible without resetting Windows, so treated as a security risk decision, not a quick fix). | Later stages show the VM was created and booted in VirtualBox; update this entry with how the block was resolved |
| 3 | First boot of the VM | VM booted to the Ubuntu login screen. Red `vmwgfx` graphics messages appeared. | VirtualBox graphics controller not matched to the guest. Cosmetic only. | Planned: set Graphics Controller to VBoxSVGA. | Not a blocker |
| 4 | VM network | Boot stalled on `systemd-networkd-wait-online` (48 s and counting, no limit). | The VM was not obtaining a network address, so the manager could not reach package servers or the Windows agent. | Planned: Bridged Adapter on the Wi-Fi interface, or NAT with port forwarding as a fallback. | Open |
| 5 | Login | The Ubuntu username and password set during the VM install could not be recalled. | Credentials were not recorded at install time (a credential-management failure). | GRUB recovery-mode reset attempted several times. | Failed |
| 6 | Recovery attempts | Repeated Esc presses showed as `^[` characters on the boot screen and the system still booted to the login prompt. | The GRUB menu is only displayed for about two seconds at the start of boot, and the key presses were sent after it had passed. | Decision: delete and rebuild the VM from the existing ISO, recording credentials in a secure note. | Pending |
| 7 | OS compatibility | The installed image is Ubuntu 26.04, which Wazuh does not officially list as supported (24.04 LTS is the latest officially supported). | Version mismatch risk for the installer. | If the installer reports an unsupported OS, use the 24.04 LTS image. | Open |
| 8 | Wazuh installation, agent registration, FIM configuration, test events | Not started. | Blocked by items 4 to 6. | Procedure documented in `deployment_steps.md`. | Not done |

## Lessons learned (GRC perspective)

- **Credential management:** The lost VM credentials are a small-scale example of an access management weakness. Credentials should be recorded in an approved password manager at creation, and recovery procedures should be tested before they are needed.
- **Change and environment readiness:** A pre-deployment checklist (resources, network mode, OS compatibility, credential storage) would have identified the network and OS issues before the build.
- **Security control trade-offs:** Disabling Smart App Control would have removed the immediate block but weakened endpoint protection. This mirrors a real risk acceptance decision and was not taken lightly.
- **Residual impact on the lab:** Because the live deployment was not completed, observed evidence could not be produced. The report therefore presents expected results only and states this openly.

## Next steps to complete the lab

1. Rebuild the VM from the existing ISO with credentials recorded, 4 GB RAM, 2 CPUs, 30 GB disk, and a Bridged Adapter.
2. Confirm a `192.168.x.x` address with `ip addr show`.
3. Run `scripts/01_install_wazuh_manager.sh`, save the admin password, and continue through `deployment_steps.md`.
4. Capture the seven evidence items and update Sections 1, 5, 6 and 8 of the README.
