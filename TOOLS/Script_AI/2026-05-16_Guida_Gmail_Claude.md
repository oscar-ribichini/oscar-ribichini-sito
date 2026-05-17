# Guida pratica — Claude legge e gestisce le tue email Gmail

Data: 16/05/2026
Versione: 1.0 — testata in diretta su account reale

---

## Cosa significa "Claude collegato a Gmail"

Claude può accedere alla tua casella Gmail tramite una connessione sicura (MCP). Non legge le mail in automatico e non fa niente senza un tuo comando. Sei sempre tu a decidere cosa fare.

---

## Cosa puoi fare — casi d'uso pratici

### 1. Sintesi mattutina

**Comando:** "Leggi le ultime 10 mail e dimmi cosa è urgente, cosa posso ignorare e cosa richiede una risposta."

Claude ti restituisce una lista ordinata per priorità. Non devi aprire ogni mail una per una. Come avere un assistente che ha già fatto la prima scrematura.

---

### 2. Cercare senza ricordare le parole esatte

**Comandi di esempio:**
- "Cerca tutte le mail che parlano di bandi o finanziamenti ricevute negli ultimi 30 giorni."
- "Cerca le mail di Mario Rossi degli ultimi 3 mesi."
- "Trova le mail dove si parla del contratto con Xyz."

Non devi ricordare l'oggetto esatto. Claude cerca per concetto, non solo per parola chiave.

---

### 3. Rispondere senza scrivere da zero

**Comandi di esempio:**
- "Scrivi una risposta professionale a questa mail. Devo declinare l'offerta in modo cortese."
- "Rispondi confermando l'appuntamento per giovedì alle 10."
- "Scrivi una risposta che chiede un chiarimento sul preventivo senza sembrare diffidente."

Claude scrive la bozza completa. Tu la leggi, modifichi se serve, e la invii. Mai una mail partita senza il tuo ok.

---

### 4. Pulire la casella senza fare tutto a mano

**Comandi di esempio:**
- "Archivia tutte le mail promozionali di Temu." *(testato — funziona in secondi)*
- "Elimina tutte le notifiche automatiche di Skool più vecchie di 7 giorni."
- "Metti come lette tutte le newsletter che non ho aperto negli ultimi 15 giorni."

Operazioni che normalmente richiedono 20 minuti, Claude le fa in pochi secondi.

---

### 5. Organizzare con etichette

**Comandi di esempio:**
- "Crea un'etichetta CLIENTI e sposta dentro tutte le mail di questi indirizzi." *(testato — etichetta creata in un secondo)*
- "Crea un'etichetta BANDI e sposta dentro tutte le mail che parlano di bandi o finanziamenti."
- "Crea un filtro automatico: tutte le mail da @nomeazienda.it vanno nell'etichetta FORNITORI."

La casella diventa un archivio organizzato invece di un mucchio disordinato.

---

### 6. Riconoscere email sospette o di marketing

**Comando:** "Leggi questa mail e dimmi se è attendibile o è una campagna di marketing mascherata da messaggio personale."

Claude analizza mittente, stile, incoerenze (es. firma diversa dal nome nel testo) e ti dice cosa ha trovato.

Esempio reale testato oggi: mail firmata "Marco Bianchi" ma con firma finale "Marco Rossi" — classico segnale di campagna automatizzata.

---

### 7. Riassumere thread lunghi

**Comando:** "Leggi tutta la conversazione con [nome] e dimmi in 5 righe di cosa si tratta e cosa è rimasto in sospeso."

Utile per tornare su una pratica dopo settimane senza rileggere tutto dall'inizio.

---

### 8. Monitorare follow-up

**Comando:** "Controlla se ho ricevuto risposta da [nome o indirizzo] negli ultimi 7 giorni."

Claude cerca nella casella e ti dice se c'è stata risposta o no. Niente più "mi aveva risposto o no?"

---

### 9. Scaricare allegati

**Comando:** "Scarica l'allegato dell'ultima mail di [mittente]."

Claude recupera il file direttamente dalla mail.

---

### 10. Creare filtri automatici permanenti

**Comando:** "Crea un filtro automatico che mette tutte le mail da Temu direttamente in archivio senza passare dalla inbox."

Il filtro rimane attivo per sempre, non devi rifarlo ogni volta.

---

## Cosa Claude NON fa (importante da spiegare ai clienti)

- Non accede alla posta in autonomia senza un tuo comando
- Non invia mail senza che tu abbia approvato
- Non elimina niente senza istruzione esplicita
- Non legge le mail in background mentre fai altro
- Non memorizza il contenuto delle mail tra una sessione e l'altra

Claude agisce solo quando tu gli dai un comando. Questo è un vantaggio: sei sempre tu a controllare.

---

## Il risparmio di tempo reale

Un imprenditore con 30-50 mail al giorno perde mediamente 45-60 minuti solo a leggere, classificare e rispondere.

Con Claude collegato a Gmail quel tempo scende a 10-15 minuti.

Su 20 giorni lavorativi al mese: **10-15 ore risparmiate**.

Moltiplicate per il costo orario dell'imprenditore (o di un'assistente): il risparmio economico mensile è misurabile.

---

## Come si attiva (per il cliente)

1. Avere Claude Code installato (VS Code o desktop app)
2. Creare un progetto Google Cloud con la Gmail API abilitata
3. Configurare il file MCP con le credenziali OAuth
4. Riavviare VS Code — da quel momento Claude ha accesso alla casella

Tempo di configurazione: circa 30-45 minuti la prima volta, poi è permanente.

---

## Comandi rapidi da dare ogni mattina

```
Leggi le ultime 10 mail e dimmi le priorità del giorno.
```

```
Ci sono mail urgenti che richiedono risposta entro oggi?
```

```
Archivia tutte le notifiche automatiche di ieri.
```

---

*File creato il 16/05/2026 — testato su account reale Oscar Ribichini*
*Aggiornare man mano che si scoprono nuovi casi d'uso*
