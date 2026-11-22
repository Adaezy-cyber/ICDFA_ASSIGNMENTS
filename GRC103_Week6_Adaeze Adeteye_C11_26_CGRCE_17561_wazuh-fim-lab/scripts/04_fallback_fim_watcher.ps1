<#
 FALLBACK ONLY - use if Wazuh cannot be installed, and only with your
 instructor's agreement. A PowerShell file-system watcher that records
 created/changed/deleted/renamed events to evidence\fallback_fim_log.csv.
 It demonstrates the same detective control with a different tool; it is
 not Wazuh and must be reported as such.
 Leave this window running while you run 03_simulate_risk_event.ps1.
#>
param([string]$Folder = "$env:USERPROFILE\SensitiveFiles")
$evid = Join-Path (Split-Path $PSScriptRoot -Parent) "evidence"
$log  = Join-Path $evid "fallback_fim_log.csv"
if (-not (Test-Path $Folder)) { New-Item -ItemType Directory -Path $Folder | Out-Null }
if (-not (Test-Path $evid))   { New-Item -ItemType Directory -Path $evid | Out-Null }
if (-not (Test-Path $log))    { "timestamp,event,path,sha256" | Out-File $log -Encoding utf8 }

$w = New-Object System.IO.FileSystemWatcher $Folder
$w.IncludeSubdirectories = $true
$w.EnableRaisingEvents = $true
$action = {
  $p = $Event.SourceEventArgs.FullPath
  $h = ""
  if (Test-Path $p -PathType Leaf) { try { $h = (Get-FileHash $p -Algorithm SHA256).Hash } catch {} }
  "{0},{1},{2},{3}" -f (Get-Date -Format "yyyy-MM-dd HH:mm:ss"), $Event.SourceEventArgs.ChangeType, $p, $h |
    Add-Content $Event.MessageData
}
foreach ($e in "Created","Changed","Deleted","Renamed") {
  Register-ObjectEvent $w $e -Action $action -MessageData $log | Out-Null
}
Write-Host "Watching $Folder. Press Ctrl+C to stop. Log: $log"
while ($true) { Start-Sleep 1 }
