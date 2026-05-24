# Regola — File _STATO_

**Da inserire in CLAUDE.md quando il metodo è approvato da Oscar.**

---

## Testo della regola

Claude aggiorna automaticamente il file _STATO_[NomeProgetto].md a fine ogni sessione e dopo ogni commit significativo, senza aspettare che Oscar lo chieda.

La prima riga del file è sempre:
`⚙️ METODO APPLICATO — Fase 0 completata: [Sì/No] | Data: [oggi] | Lenti rosse risolte: [n]`

Struttura fissa del file:

```
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

Se la sessione si interrompe senza aggiornamento, il primo messaggio della sessione successiva è /stallo.

---

## Stato

In costruzione — non ancora inserita in CLAUDE.md.
Inserire solo dopo approvazione esplicita di Oscar.
