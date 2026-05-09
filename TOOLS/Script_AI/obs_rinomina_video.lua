local obs = obslua
local cartella = "E:\\Lavori Code\\VIDEO\\"

function script_description()
    return "Chiede il nome del file appena finisce la registrazione e rinomina il video."
end

function on_event(event)
    if event == obs.OBS_FRONTEND_EVENT_RECORDING_STOPPED then
        obs.timer_add(rinomina_video, 2000)
    end
end

function rinomina_video()
    obs.timer_remove(rinomina_video)

    -- Trova l'ultimo file mp4 nella cartella
    local handle = io.popen('dir "' .. cartella .. '" /b /od /a-d')
    local ultimo_file = ""
    if handle then
        for line in handle:lines() do
            if line:match("%.mp4$") then
                ultimo_file = line
            end
        end
        handle:close()
    end

    if ultimo_file == "" then
        obs.script_log(obs.LOG_INFO, "Nessun file mp4 trovato")
        return
    end

    -- Mostra input dialog tramite PowerShell
    local data = os.date("%Y-%m-%d")
    local cmd = 'powershell -Command "Add-Type -AssemblyName Microsoft.VisualBasic; $n = [Microsoft.VisualBasic.Interaction]::InputBox(\'Inserisci il nome del video (es. CloudCode_Lezione-01):\', \'Rinomina video\', \'\'); Write-Output $n"'

    local handle2 = io.popen(cmd)
    local nome = ""
    if handle2 then
        nome = handle2:read("*l") or ""
        handle2:close()
    end

    nome = nome:gsub("%s+$", ""):gsub("^%s+", "")

    if nome ~= "" then
        local vecchio = cartella .. ultimo_file
        local nuovo = cartella .. nome .. "_" .. data .. ".mp4"
        os.rename(vecchio, nuovo)
        obs.script_log(obs.LOG_INFO, "Rinominato in: " .. nome .. "_" .. data .. ".mp4")
    else
        obs.script_log(obs.LOG_INFO, "Rinomina saltata, nome non inserito")
    end
end

obs.obs_frontend_add_event_callback(on_event)
