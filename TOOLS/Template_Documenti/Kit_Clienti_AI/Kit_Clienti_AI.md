# Kit Clienti AI
Procedura completa per configurare l'ambiente di lavoro AI su un nuovo PC cliente.
Aggiornato: 16/05/2026

---

## FASE 1 — Software da installare

### Strumenti AI
- [ ] Claude Code (CLI) — installare da claude.ai/code
- [ ] VS Code — editor principale per lavorare con Claude Code
- [ ] Node.js — necessario per Claude Code

### Strumenti cloud e sincronizzazione
- [ ] Google Drive for Desktop — sincronizzazione file cloud, si monta come unità disco
- [ ] Dropbox (se il cliente lo usa già)

### Browser
- [ ] Google Chrome — browser principale
  - Configurare barra preferiti: Gmail, Drive, Calendar, LinkedIn, Claude, sito personale
  - Spostare tutto il resto in cartella "Altro"

### Screenshot
- [ ] Snipping Tool (già integrato in Windows) — per uso base, salvataggio manuale solo quando serve
- [ ] ShareX (opzionale, gratuito) — aggiunge blur su dati sensibili del cliente e salvataggio automatico con nome data; consigliato quando si lavora con documenti riservati

### Comunicazione e video
- [ ] Loom — registra lo schermo e manda un link video al cliente senza file pesanti; perfetto per spiegare qualcosa a distanza senza fare una call. Provare prima di installare sui clienti.
- [ ] Google Meet — già incluso in Google, per videochiamate e riunioni remote
- [ ] Calendly — prenotazione chiamate automatica, collegare a Google Calendar

### Accesso remoto
- [ ] AnyDesk — per assistenza remota al PC del cliente; permette di prendere il controllo del desktop da remoto per risolvere problemi o fare dimostrazioni

### Automazioni
- [ ] Make.com — per costruire flussi automatici (es. note vocali → .md → Drive); account gratuito sufficiente per iniziare

### Grafica e contenuti
- [ ] Canva — grafica social, presentazioni, documenti professionali; ha AI integrata

---

## FASE 2 — Configurazione Claude Code

- [ ] Installare Claude Code via terminale
- [ ] Creare il file CLAUDE.md nella cartella di lavoro del cliente
  - Nome e ruolo del cliente
  - Settore e attività
  - Tono di voce e lingua
  - Struttura cartelle
  - Regole operative specifiche
- [ ] Testare il primo prompt per verificare che Claude risponda correttamente

---

## FASE 3 — Configurazione VS Code

- [ ] Installare VS Code
- [ ] Installare estensione Claude Code per VS Code
- [ ] Installare estensioni utili:
  - [ ] Markdown Preview — per vedere i file .md formattati
  - [ ] GitLens — per gestire il versionamento
  - [ ] Italian Language Pack — interfaccia in italiano
- [ ] Configurare il tema (scuro consigliato per lavoro lungo)
- [ ] Aprire la cartella di lavoro del cliente come workspace

---

## FASE 4 — Configurazione Google Drive

- [ ] Installare Google Drive for Desktop
- [ ] Collegare l'account Google del cliente
- [ ] Verificare che Drive sia montato come unità (es. H:)
- [ ] Creare struttura cartelle standard:
  - [ ] Clienti\
  - [ ] Lavori\
  - [ ] Note Vocali\
  - [ ] Archivio\
- [ ] Creare README.md in ogni cartella

---

## FASE 5 — Flusso note vocali (opzionale)

- [ ] Verificare se il cliente usa Google Keep sul telefono
- [ ] Configurare Make.com per il flusso: Keep → Whisper → .md → Drive
- [ ] Testare con una nota di prova
- [ ] Cartella di destinazione: Drive\Note Vocali\

---

## FASE 6 — Test finale

- [ ] Aprire VS Code con Claude Code
- [ ] Chiedere a Claude di leggere un file dalla cartella di lavoro
- [ ] Chiedere a Claude di leggere un file da Drive
- [ ] Fare uno screenshot e annotarlo
- [ ] Verificare che tutto sia sincronizzato su Drive
- [ ] Mandare al cliente un video Loom di riepilogo di cosa è stato installato e come usarlo

---

## Note operative

- Tempo medio installazione completa: 2-3 ore
- Portare sempre chiavetta USB con i programmi scaricati (Claude Code, VS Code, Chrome, Drive)
- Prima di iniziare: chiedere al cliente le credenziali Google e i permessi di installazione
- Documentare ogni installazione con screenshot datati
- Lasciare al cliente un foglio con i percorsi chiave (cartella di lavoro, Drive, VS Code)
- Il video Loom finale è il miglior modo per lasciare al cliente un riferimento su come usare tutto
