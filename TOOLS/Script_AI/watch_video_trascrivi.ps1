$cartella = "E:\Lavori Code\VIDEO"
$logFile  = "E:\Lavori Code\TOOLS\Script_AI\watch_log.txt"
$processati = @{}

function Log($msg) {
    $riga = "$(Get-Date -Format 'yyyy-MM-dd HH:mm:ss') - $msg"
    Add-Content -Path $logFile -Value $riga -Encoding UTF8
}

Log "Watcher avviato. In ascolto su: $cartella"

while ($true) {
    $files = Get-ChildItem -Path $cartella -Filter "*.mp4" -File

    foreach ($file in $files) {
        $chiave = $file.FullName
        if ($processati.ContainsKey($chiave)) { continue }

        # Attendi che il file non sia più in scrittura
        $pronto = $false
        for ($i = 0; $i -lt 30; $i++) {
            Start-Sleep -Seconds 2
            try {
                $stream = [System.IO.File]::Open($file.FullName, 'Open', 'Read', 'None')
                $stream.Close()
                $pronto = $true
                break
            } catch { }
        }

        if (-not $pronto) {
            Log "File non accessibile, salto: $($file.Name)"
            continue
        }

        $processati[$chiave] = $true
        Log "Nuovo video rilevato: $($file.Name)"

        $argomenti = "`"$($file.FullName)`" --language Italian --output_format txt --output_dir `"$cartella`""
        Log "Avvio Whisper..."
        Start-Process -FilePath "py" -ArgumentList "-m whisper $argomenti" -Wait -NoNewWindow
        Log "Trascrizione completata: $($file.BaseName).txt"
    }

    Start-Sleep -Seconds 10
}
