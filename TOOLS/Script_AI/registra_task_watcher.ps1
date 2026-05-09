$taskName = "WatcherTrascrizione_VideoOscar"
$scriptPath = "E:\Lavori Code\TOOLS\Script_AI\watch_video_trascrivi.ps1"

$action = New-ScheduledTaskAction `
    -Execute "powershell.exe" `
    -Argument "-ExecutionPolicy Bypass -WindowStyle Hidden -File `"$scriptPath`""

$trigger = New-ScheduledTaskTrigger -AtLogOn

$settings = New-ScheduledTaskSettingsSet `
    -ExecutionTimeLimit (New-TimeSpan -Hours 0) `
    -RestartCount 3 `
    -RestartInterval (New-TimeSpan -Minutes 1) `
    -StartWhenAvailable

Register-ScheduledTask `
    -TaskName $taskName `
    -Action $action `
    -Trigger $trigger `
    -Settings $settings `
    -Description "Avvia il watcher Whisper per trascrizione automatica video in E:\Lavori Code\VIDEO" `
    -RunLevel Highest `
    -Force

Write-Host "Task registrato: $taskName"
Write-Host "Il watcher partira in automatico ad ogni accesso a Windows."
