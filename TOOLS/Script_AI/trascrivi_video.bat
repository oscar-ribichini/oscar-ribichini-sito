@echo off
echo.
echo ========================================
echo   TRASCRIZIONE VIDEO CON WHISPER
echo ========================================
echo.

if "%~1"=="" (
    echo Trascina un file video su questo script oppure
    echo digita il percorso del file qui sotto:
    echo.
    set /p FILEPATH="Percorso file video: "
) else (
    set FILEPATH=%~1
)

echo.
echo --- RINOMINA IL FILE ---
echo.
set /p CORSO="Nome del corso (es. CloudCode, CorsoAI): "
set /p LEZIONE="Numero lezione (es. 01, 02, 03): "

for /f "tokens=1-3 delims=/" %%a in ('echo %date%') do (
    set GG=%%a
    set MM=%%b
    set AAAA=%%c
)
set DATAOGGI=%AAAA%-%MM%-%GG%

set NUOVONOME=%DATAOGGI%_%CORSO%_Lezione-%LEZIONE%.mp4
if not "%~dp1"=="" (
    set CARTELLA=%~dp1
) else (
    for %%F in ("%FILEPATH%") do set CARTELLA=%%~dpF
)

echo.
echo Il video verra rinominato in: %NUOVONOME%
echo.

rename "%FILEPATH%" "%NUOVONOME%"

echo.
echo Avvio trascrizione in italiano...
echo Il file di testo verra salvato nella stessa cartella del video.
echo.

py -m whisper "%CARTELLA%%NUOVONOME%" --language Italian --output_dir "%CARTELLA%"

echo.
echo ========================================
echo   FATTO! File salvato come:
echo   %NUOVONOME%
echo ========================================
echo.
pause
