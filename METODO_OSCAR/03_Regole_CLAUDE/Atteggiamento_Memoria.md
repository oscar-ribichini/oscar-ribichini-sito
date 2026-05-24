# Come Claude mantiene il filo tra sessioni

**Da inserire in CLAUDE.md quando approvato da Oscar.**

---

Claude sa che ogni sessione ricomincia da zero. Per questo tiene il filo attivo — non aspetta che Oscar lo chieda.

A fine di ogni sessione significativa aggiorna il file _STATO_[NomeProgetto].md. Non è un riassunto — è il punto di ripresa. Chiunque lo legga in 30 secondi sa esattamente dove si è arrivati, cosa manca, cosa blocca.

La prima riga di ogni _STATO_ è sempre uno specchio onesto:
`⚙️ METODO APPLICATO — Fase 0 completata: [Sì/No] | Data: [oggi] | Lenti rosse risolte: [n]`

Se una sessione finisce male — connessione caduta, chiusura improvvisa, confusione — Claude non finge che tutto vada bene. La sessione successiva parte con /stallo: lettura silenziosa di tutto il contesto disponibile, specchio di 4–6 righe su dove si è arrivati, analisi delle lenti rilevanti, 3 domande mirate e una raccomandazione. Oscar corregge se qualcosa non torna, poi si procede.

Il filo non si perde mai. Se sembra perso, /stallo lo ritrova.

---

## Struttura fissa _STATO_

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

## Stato

In costruzione — non ancora inserita in CLAUDE.md.
Inserire solo dopo approvazione esplicita di Oscar.
