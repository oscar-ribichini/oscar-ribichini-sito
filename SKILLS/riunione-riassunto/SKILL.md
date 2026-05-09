---
name: riunione-riassunto
description: Genera una minuta strutturata di una riunione da remoto a partire dalla trascrizione incollata in chat. Usa questa skill ogni volta che l'utente incolla o fornisce nel contesto della chat il testo di una trascrizione di riunione (Teams, Zoom, Meet, ecc.) e chiede un riassunto, una minuta, un verbale o un resoconto. Attivala anche se l'utente scrive frasi come "fai la minuta di questa riunione", "riassumi questa call", "crea il verbale di questa riunione", "ecco la trascrizione, cosa è stato deciso".
---

# Skill: riunione-riassunto

Il tuo unico compito è generare una minuta formale e strutturata a partire dalla trascrizione di una riunione da remoto fornita nel contesto della chat.

## Comportamento

1. Leggi attentamente la trascrizione fornita dall'utente.
2. Produci la minuta in italiano, con tono formale, usando esattamente la struttura indicata sotto.
3. Mostra la minuta direttamente in chat.
4. Salva la minuta come file `.md` nella cartella `e:\Lavori Code\_CLIENTI\[NomeCliente]\11_Riunioni\`, dove `[NomeCliente]` è il nome del cliente che emerge dalla trascrizione. Se il cliente non è identificabile, chiedi all'utente prima di salvare.
5. Il nome del file deve seguire questo formato: `AAAA-MM-GG_minuta_[oggetto-breve].md`

Non fare nient'altro: niente analisi aggiuntive, niente suggerimenti, niente file di log.

## Struttura fissa della minuta

```
# Minuta di Riunione

**Data e ora:** [ricavata dalla trascrizione, o lascia vuoto se assente]
**Modalità:** Riunione da remoto
**Partecipanti:** [elenco dei nomi presenti nella trascrizione]
**Oggetto della riunione:** [titolo sintetico del tema principale]

---

## Punti discussi

[Elenco puntato dei principali argomenti trattati, in ordine cronologico]

## Decisioni prese

[Elenco puntato delle decisioni emerse. Se non ce ne sono, scrivi "Nessuna decisione formale presa."]

## Azioni da intraprendere

| Azione | Responsabile | Scadenza |
|--------|-------------|----------|
| ...    | ...         | ...      |

[Se non ci sono azioni esplicite, scrivi "Nessuna azione assegnata."]

## Prossimi passi

[Elenco puntato dei prossimi passi concordati, incluse eventuali riunioni future. Se non ci sono, scrivi "Non definiti."]
```

## Note operative

- Usa solo le informazioni presenti nella trascrizione: non inventare dati, nomi o decisioni.
- Se la trascrizione è incompleta o ambigua, segnalalo nella sezione pertinente con una nota tra parentesi quadre, es. `[dato non rilevabile dalla trascrizione]`.
- La cartella `11_Riunioni` va creata se non esiste già.
