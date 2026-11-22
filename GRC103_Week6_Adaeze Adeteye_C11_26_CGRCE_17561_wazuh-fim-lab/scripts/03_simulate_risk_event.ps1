<#
 Simulates the unauthorised activity from Part 6 of the lab:
   create -> modify -> delete  Q4_Financial_Forecast.docx
 Writes the exact action times to evidence\simulation_log.csv so alerts in
 the Wazuh dashboard can be matched to what was done.
 Placeholder content is plain text; FIM only cares that the file changed.
#>
param(
  [string]$Folder = "$env:USERPROFILE\SensitiveFiles",
  [int]$PauseSeconds = 10
)
$file   = Join-Path $Folder "Q4_Financial_Forecast.docx"
$evid   = Join-Path (Split-Path $PSScriptRoot -Parent) "evidence"
$log    = Join-Path $evid "simulation_log.csv"
if (-not (Test-Path $Folder)) { New-Item -ItemType Directory -Path $Folder | Out-Null }
if (-not (Test-Path $evid))   { New-Item -ItemType Directory -Path $evid | Out-Null }
if (-not (Test-Path $log))    { "timestamp,action,path" | Out-File $log -Encoding utf8 }

function Log($a) { "{0},{1},{2}" -f (Get-Date -Format "yyyy-MM-dd HH:mm:ss"), $a, $file | Add-Content $log }

Set-Content -Path $file -Value "Q4 financial forecast - draft";                     Log "created";  Start-Sleep $PauseSeconds
Add-Content -Path $file -Value "Revenue revised upward by 12% (unauthorised edit)"; Log "modified"; Start-Sleep $PauseSeconds
Remove-Item -Path $file -Force;                                                     Log "deleted"
Write-Host "Done. Check the Wazuh dashboard (rule.groups: syscheck). Log: $log"
