# Evidence files

Raw output files from Lab 1, generated on the Kali machine in `~/lab1` on 20 October 2026.

| File | Produced by |
|---|---|
| [`initial_scan.nmap`](initial_scan.nmap) | `nmap -sV -sC -O -p- -oA initial_scan 192.168.56.10` |
| [`initial_scan.gnmap`](initial_scan.gnmap) | same command |
| [`initial_scan.xml`](initial_scan.xml) | same command |
| [`initial_scan_report.html`](initial_scan_report.html) | `xsltproc -o initial_scan_report.html /usr/share/nmap/nmap.xsl initial_scan.xml` |
| [`nikto_scan.txt`](nikto_scan.txt) | `nikto -h http://192.168.56.10 -o nikto_scan.txt` |
| [`nuclei_web_scan.txt`](nuclei_web_scan.txt) | `nuclei -u http://192.168.56.10 -o nuclei_web_scan.txt` |

The listing that shows these files being collected is screenshot 22 in the main [README](../README.md#saved-evidence-files).
