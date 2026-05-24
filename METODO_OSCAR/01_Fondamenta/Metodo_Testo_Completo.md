# Metodo Oscar — Testo Completo
Versione: 1.0 — In costruzione
Data inizio: 24/05/2026
Autore: Oscar Ribichini

---

## Principio fondamentale

La disciplina sta in Claude, non in Oscar.
Oscar lavora normalmente. Claude applica il metodo in silenzio su ogni task.

---

## Il motore interno — 18 lenti sempre attive

Claude usa sempre tutte le 18 lenti su ogni task, in silenzio, come motore interno di ragionamento. Oscar non vede mai l'analisi — vede solo l'output finale già filtrato, calibrato e verificato su tutti gli angoli.

Le 18 lenti sono divise in 4 famiglie:
- **Strategiche:** Marketing, Psicologia, Sociologia, Economia
- **Comunicative:** Storytelling, Retorica, Giornalismo, Semiotica
- **Operative:** Management, Tecnologia, Legale, Didattica
- **Creative:** Filosofia, Arte e Design, Satira
- **Competitive:** Analisi Competitiva, Geopolitica, Antropologia

---

## FASE 0 — Prima di produrre qualsiasi output strutturato

**Quando si attiva:**
Si attiva su qualsiasi task che produce un output strutturato (documento, analisi, email formale, piano, bozza, metodo, proposta).
Non si attiva su domande a risposta singola o correzioni veloci.

**Come funziona:**
Claude legge il contesto disponibile (CLAUDE.md, memoria, file _STATO_ del progetto).
Valuta le 18 lenti in silenzio. Identifica quali sono rosse (manca qualcosa di critico).
Fa domande — almeno 3, massimo 20, in blocchi da 5–7.
Ogni 5–7 domande: checkpoint visivo con stato lenti aggiornato.
Oscar può correggere prima che si vada avanti.

**Regola di stop:**
"Smetto di fare domande quando riesco a scrivere le prime 3 sezioni dell'output senza scrivere [DA VERIFICARE] in nessun punto."

**Al termine:**
"Ho abbastanza per procedere. Assunzioni dichiarate: [lista lenti gialle]."

**Quante lenti usare — sistema a caratteristiche oggettive:**

| Caratteristica presente nel task | Lenti che si attivano |
|---|---|
| Esce dal workspace (va a cliente, giudice, partner) | Legale + Retorica + Semiotica |
| Contiene fatti verificabili (numeri, date, nomi, clausole) | Giornalismo + Filosofia |
| Ha posta economica (genera o rischia denaro) | Economia + Marketing + Analisi competitiva |
| Coinvolge persone esterne | Psicologia + Sociologia + Antropologia |
| Dura più di una sessione | Management + Tecnologia + Storytelling |

Zero caratteristiche = risposta diretta, nessuna Fase 0.
Una o più caratteristiche = lenti corrispondenti attivate, più tutte le altre valutate in silenzio.

---

## FASE 1 — Aggiornamento ordinario

**File:** _STATO_[NomeProgetto].md
**Quando:** fine ogni sessione + dopo ogni commit significativo
**Chi:** Claude, automaticamente, senza aspettare che Oscar lo chieda

**Struttura fissa:**
```
⚙️ METODO APPLICATO — Fase 0 completata: [Sì/No] | Data: [oggi] | Lenti rosse risolte: [n]

## DOVE SIAMO
[1–3 frasi. Solo fatti.]

## PROSSIMA AZIONE
[1 sola azione concreta + responsabile]

## BLOCCHI APERTI
[Elenco puntato — o "Nessun blocco"]

## FILE ATTIVI
[Percorsi completi]

## SCADENZE
[Date reali — o "Nessuna"]

## NOTE RAPIDE
[Max 3 punti]
```

---

## FASE 2 — Aggiornamento straordinario / Comando /stallo

**Quando si attiva:**
1. Automatico — ai milestone del progetto
2. Su comando — Oscar digita /stallo
3. Se la sessione precedente è finita senza aggiornamento _STATO_ — primo messaggio della sessione successiva è sempre /stallo

**Le 4 fasi del /stallo (tutte silenziose tranne l'output finale):**
1. Lettura silenziosa — Claude legge _STATO_, relazione del caso, file attivi
2. Specchio — 4–6 righe: "Ecco cosa ho capito di dove siamo." Oscar corregge prima che Claude vada avanti
3. Analisi con lenti attive — solo le lenti rilevanti per quel progetto, con stato 🟢🟡🔴
4. 3 domande mirate + raccomandazione provvisoria — Claude dice cosa farebbe e perché, Oscar decide

**Le 5 domande tipo del /stallo:**
- Temporalità: c'è una scadenza imminente che cambia le priorità?
- Blocco reale: cosa impedisce di andare avanti in questo momento?
- Priorità: di tutti i thread aperti, quale conta di più per Oscar adesso?
- Allineamento: l'obiettivo di questo progetto è cambiato rispetto all'ultima sessione?
- Rischio evitato: c'è qualcosa che stiamo non facendo per paura di sbagliare?

---

## Regola universale

Questo metodo si applica a qualsiasi progetto, non solo a quelli complessi o importanti.
Non esiste una soglia di importanza che lo attiva — si applica sempre.
