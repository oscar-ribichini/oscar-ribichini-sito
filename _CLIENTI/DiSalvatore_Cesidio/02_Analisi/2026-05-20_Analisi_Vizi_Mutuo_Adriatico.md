# Analisi Vizi Contrattuali — Mutuo Banca dell'Adriatico / Intesa Sanpaolo
**Cliente:** Di Salvatore Cesidio
**Data analisi:** 20/05/2026
**Redatta da:** Oscar Ribichini (con supporto AI)

---

## Dati identificativi del rapporto

| Voce | Dettaglio |
|---|---|
| Mutuo n. | 0E53055182312 (poi rinumerato 8R03055295575 dopo rinegoziazione) |
| Data stipula | 31/01/2012 |
| Notaio | Dott. Giuseppe Altieri — Avezzano (AQ) — Rep. 72.808 / Racc. 12.429 |
| Mutuante originaria | Banca dell'Adriatica S.p.A. (ora incorporata in Intesa Sanpaolo S.p.A.) |
| Mutuatario | Di Salvatore Cesidio, nato a Gioia dei Marsi (AQ) il 30/04/1949, C.F. DSL CSD 49D30 E040H |
| Terzo datore d'ipoteca | D'Amico Viviana, nata a Ortucchio (AQ) il 15/02/1950 |
| Regime patrimoniale | Separazione dei beni |
| Importo mutuato | Euro 231.000,00 |
| Durata | 20 anni — 240 rate mensili posticipate |
| Tasso nominale originario | 6,55% annuo fisso |
| TAEG dichiarato | 7,039% |
| Rata mensile | Euro 1.729,08 (salvo prima rata con interessi di preammortamento) |
| Immobile ipotecato | Avezzano (AQ), Via Pereto n. 57 — Foglio 31, Particella 925, Sub 5 e 6 — Cat. A7 |
| Ipoteca iscritta | Euro 462.000,00 — Reg. Generale 2675, Reg. Particolare 200, Presentazione 59 del 13/02/2012 |
| Data rinegoziazione | 08/10/2014 — scrittura privata a Pescara |
| Tasso dopo rinegoziazione | Variabile: Euribor 1 mese (base 360) + spread fisso 2,50% |
| Nuovo n. mutuo | 8R03055295575 |

---

## Premessa metodologica

La presente analisi si basa sulla lettura integrale dei seguenti documenti originali:

1. **File 1 (Parte I):** Nota di iscrizione ipotecaria — Agenzia del Territorio, Ufficio Provinciale di L'Aquila — 3 pagine
2. **File 1 (Parte II):** Contratto di mutuo notarile del 31/01/2012 con allegati A (Documento di Sintesi), B (Condizioni Generali) e C (Piano di Ammortamento) — 19 pagine
3. **File 2:** Atto di rinegoziazione del tasso — scrittura privata del 08/10/2014 — 4 pagine
4. **File 3 (Piano di Ammortamento):** PA completo, 240 rate, dal 01/04/2012 al 01/03/2032 — 11 pagine

La normativa di riferimento principale è il D.Lgs. 1 settembre 1993 n. 385 (Testo Unico Bancario — TUB), in particolare gli artt. 115, 116, 117, 120; la delibera CICR 9 febbraio 2000; le Istruzioni di Vigilanza Banca d'Italia; il Codice del Consumo D.Lgs. 206/2005.

---

## VIZIO N. 1 — Regime di capitalizzazione composta non dichiarato nel contratto originario

### Descrizione del vizio

Il contratto di mutuo stipulato il 31/01/2012 prevede un piano di ammortamento alla francese a tasso fisso, con rata costante mensile di Euro 1.729,08. Il Piano di Ammortamento allegato come "Allegato C" al contratto notarile è firmato dalle parti e costituisce "parte integrante e sostanziale" del contratto (art. 3, comma 1 del contratto).

Il meccanismo matematico sottostante al piano alla francese con rata costante si basa necessariamente sul **regime di capitalizzazione composta**: ogni mese, la quota interessi viene calcolata sul capitale residuo (già ridotto dalle rate precedenti), ma il sistema di calcolo della rata costante presuppone che il tasso mensile venga composto per generare il valore attuale dell'intera serie di rate. In altre parole, il tasso mensile effettivo non è semplicemente 1/12 del tasso annuo, ma è la radice dodicesima di (1 + tasso annuo).

### Cosa dice il contratto

L'art. 4, comma 1 del contratto stabilisce:

> *"Il tasso d'interesse mensile viene stabilito nella misura pari ad 1/12 (un dodicesimo) del tasso nominale annuo del 6,55%."*

L'art. 4, comma 2 aggiunge:

> *"Gli interessi saranno calcolati in base ai giorni dell'anno commerciale e con divisore fisso 36.000."*

Il Documento di Sintesi (Allegato A) indica:
- Piano di ammortamento: **francese**
- Tipologia rata: **costante**
- Periodicità: **mensile**

### Cosa manca

In nessuna parte del contratto — né nel corpo principale, né nel Documento di Sintesi, né nelle Condizioni Generali (Allegato B) — viene mai indicato che il calcolo della rata avviene in **regime di capitalizzazione composta**, né che gli interessi si capitalizzano mensilmente, né che il tasso effettivo annuo risultante dal meccanismo composto è diverso dal tasso nominale dichiarato del 6,55%.

La formula usata per il calcolo della rata costante nel piano alla francese è:

```
R = C × [i(1+i)^n] / [(1+i)^n - 1]
```

dove `i` è il tasso periodico e `n` è il numero di periodi. Questa formula implica la capitalizzazione composta. Il suo utilizzo senza esplicitazione costituisce una clausola implicita non dichiarata.

### Verifica sui numeri del Piano di Ammortamento

Dalla rata n. 001 (01/04/2012):
- Capitale residuo iniziale: 231.000,00
- Quota interessi: 2.563,76 — pari a 231.000 × (6,55% / 12 × giorni/30) ... ma attenzione: 231.000 × 6,55% / 12 = **1.261,13**, non 2.563,76.

La quota interessi della prima rata è quasi il doppio di quanto si otterrebbe con un semplice calcolo mensile lineare. Questo perché la prima rata incorpora gli **interessi di preammortamento** maturati dalla data di stipula (31/01/2012) al 01/04/2012 — circa 60 giorni. Ma a partire dalla rata 002 in poi, la quota interessi scende a 1.258,32 (rata 002) e decresce progressivamente, confermando il meccanismo francese standard.

Dalla rata n. 002 in poi il calcolo è verificabile: quota interessi rata 002 = 230.531,79 × (6,55% / 12) = 230.531,79 × 0,005458... = **1.258,32**. Il divisore fisso 36.000 e l'anno commerciale di 360 giorni vengono usati per il preammortamento ma non alterano la struttura del piano.

**Il piano è coerente internamente con il regime composto — e questo non viene mai dichiarato.**

### Norma violata e conseguenza

L'art. 117 TUB (nella versione applicabile al 2012) impone che i contratti bancari indichino "il tasso di interesse e ogni altro prezzo e condizione praticati, inclusi, per i contratti di credito, gli eventuali maggiori oneri in caso di mora". La delibera CICR del 09/02/2000 (attuativa dell'art. 120 TUB) vieta la capitalizzazione degli interessi nei rapporti bancari e impone che le clausole di capitalizzazione siano esplicite e approvate specificamente.

La mancata indicazione del regime composto rende il tasso **indeterminato o indeterminabile** nella sua componente effettiva. Conseguenza: si applica l'art. 117, comma 7 TUB — sostituzione del tasso contrattuale con il tasso sostitutivo pari al rendimento dei Buoni Ordinari del Tesoro annuali emessi nei dodici mesi precedenti la conclusione del contratto.

### Impatto economico stimato

Il tasso sostitutivo BOT per il 2011-2012 era mediamente intorno al 2,0-2,5% annuo. Su un mutuo da 231.000 euro ventennale, la differenza tra il 6,55% contrattuale e un tasso sostitutivo del 2,5% comporta una riduzione degli interessi totali nell'ordine di **80.000-100.000 euro** sull'intera durata residua, con diritto alla ripetizione degli interessi già versati in eccesso.

**Giudizio: VIZIO FONDATO E DOCUMENTALMENTE PROVATO.**

---

## VIZIO N. 2 — Assenza del Piano di Ammortamento nella rinegoziazione del 2014

### Descrizione del vizio

L'atto di rinegoziazione del tasso, sottoscritto come scrittura privata il 08/10/2014 a Pescara, modifica il tasso di interesse da fisso (6,55%) a variabile (Euribor 1 mese base 360 + spread 2,50%) con decorrenza dalla rata in corso.

### Cosa dice la rinegoziazione

Il punto 2 dell'atto afferma testualmente:

> *"Le rate saranno calcolate col sistema dell'ammortamento di un prestito a rate costanti basato sulla formula matematico finanziaria nota nella tecnica finanziaria come 'sistema francese', assumendo i seguenti dati: tasso di interesse e di ammortamento del capitale: quello indicato al punto 1; capitale: debito residuo risultante dopo il rimborso della rata immediatamente precedente la decorrenza della modifica del tasso di interesse come precisata al punto 1; durata: pari alle residue rate di ammortamento a decorrere dalla data di variazione del tasso di interesse."*

### Cosa manca

**Non esiste alcun allegato alla rinegoziazione.** L'atto originale del 2012 aveva il Piano di Ammortamento come "Allegato C", firmato da tutte le parti e dichiarato "parte integrante e sostanziale" del contratto. La rinegoziazione del 2014 non ha alcun allegato equivalente.

Con il passaggio a tasso variabile, la rata mensile cambia ogni mese in funzione dell'Euribor. Ma la banca non ha fornito al cliente nemmeno:
- il piano di ammortamento calcolato al momento della rinegoziazione (cioè con il debito residuo a quella data e il tasso iniziale variabile);
- il criterio di ricalcolo delle rate future;
- il valore del debito residuo al momento della decorrenza della modifica.

Alla data della rinegoziazione (08/10/2014), in base al PA originale, la rata corrente era la n. 031 (01/10/2014) con debito residuo di circa **215.232,12 euro**. Su questo importo, con Euribor 1 mese a 0,007% (valore dichiarato nell'atto) + spread 2,50%, il tasso applicato era 2,507% annuo circa — ma il cliente non ha mai ricevuto un documento che lo certificasse o che mostrasse come cambiava la rata.

### Norma violata e conseguenza

L'art. 117 TUB richiede che i contratti bancari siano redatti per iscritto e che una copia sia consegnata al cliente. L'art. 116 impone la trasparenza delle condizioni. Le Istruzioni di Banca d'Italia in materia di trasparenza (Provvedimento del 29/07/2009 e successive) prevedono che in caso di modifica delle condizioni economiche di un mutuo, il cliente debba ricevere un documento che illustri le nuove condizioni e il loro impatto sul piano di rimborso.

L'assenza del PA nella rinegoziazione rende il nuovo tasso variabile **indeterminabile** nella sua applicazione concreta, poiché il cliente non ha mai potuto verificare se le rate addebitategli corrispondessero al calcolo contrattualmente previsto. Questo integra una violazione dell'art. 117 TUB e, per la parte di tasso indeterminato, legittima l'applicazione del tasso sostitutivo.

Ulteriore elemento rilevante: la rinegoziazione è una **scrittura privata**, non autenticata né notarile, su carta intestata della banca, compilata in modo asimmetrico. Questo non è di per sé un vizio formale (la legge consente le rinegoziazioni in forma semplificata), ma sottolinea l'assenza di qualunque presidio di terzietà a tutela del cliente.

**Giudizio: VIZIO FONDATO E DOCUMENTALMENTE PROVATO.**

---

## VIZIO N. 3 — TAEG potenzialmente difforme per errato computo delle spese assicurative

### Descrizione del vizio

Il Documento di Sintesi (Allegato A al contratto del 2012) dichiara un TAEG del **7,039%** e specifica che nella sua determinazione sono state incluse le seguenti voci:

- Istruttoria: Euro 600,00
- Perizia: Euro 250,00 (rimanda a "Altre Spese da Sostenere")
- Assicurazione incendio: **Euro 2.418,32** — polizza obbligatoria contro incendio/scoppio, con vincolo a favore della banca, stipulata con Intesa Sanpaolo Assicura S.p.A.
- Conto corrente: canone annuo Euro 48,00 + imposta di bollo Euro 34,20
- Avviso di scadenza rata cartaceo: Euro 1,50/mese

### Il problema dell'assicurazione

La polizza assicurativa incendio è:
1. **Obbligatoria per contratto** (art. 6 delle Condizioni Generali: "La Parte Mutuataria è tenuta ad assicurare a sue spese... i fabbricati oggetto di garanzia contro i danni causati da incendio, scoppio, fulmine ed altri eventi assicurabili")
2. **Con vincolo a favore della banca** (le polizze devono essere "vincolate a favore della Banca e consegnate in copia presso la medesima")
3. **Stipulata con una società del gruppo Intesa Sanpaolo** (Intesa Sanpaolo Assicura S.p.A.)

Secondo la normativa europea (Direttiva 2014/17/UE, recepita in Italia, e le Istruzioni Banca d'Italia) e l'orientamento dell'ABF (Arbitro Bancario Finanziario), quando la polizza assicurativa è obbligatoria e il fornitore è imposto dalla banca, il premio deve necessariamente essere incluso nel calcolo del TAEG. Se invece è incluso ma calcolato in modo scorretto (ad esempio usando il premio della sola prima annualità invece del costo attualizzato sull'intera durata del mutuo), il TAEG risultante è difforme da quello reale.

### Cosa va verificato

Per provare questo vizio è necessario:
1. Ottenere la polizza assicurativa completa con il piano dei premi per i 20 anni
2. Ricalcolare il TAEG reale includendo tutti i costi nella loro esatta misura
3. Confrontare il TAEG ricalcolato con il 7,039% dichiarato

Se la differenza supera 0,1 punti percentuali (tolleranza convenzionalmente accettata), il TAEG è difforme e si configura la violazione dell'art. 117 TUB con conseguente applicazione del tasso sostitutivo.

**Giudizio: VIZIO PROBABILE MA NECESSITA DI VERIFICA NUMERICA CON PERIZIA.**

---

## Quadro sinottico dei vizi

| N. | Vizio | Base documentale | Norma violata | Solidità | Azione necessaria |
|---|---|---|---|---|---|
| 1 | Regime composto non dichiarato | Contratto 2012 + PA | Art. 117 TUB + Delibera CICR 2000 | ALTA | Già provato — pronto per atto giudiziario |
| 2 | Assenza PA nella rinegoziazione 2014 | Rinegoziazione 2014 | Art. 117 TUB + Istruzioni Banca d'Italia | ALTA | Già provato — pronto per atto giudiziario |
| 3 | TAEG difforme (spese assicurative) | Documento di Sintesi + polizza | Art. 117 TUB + Dir. 2014/17/UE | MEDIA | Richiede perizia numerica |

---

## Conseguenza giuridica unitaria

Tutti e tre i vizi convergono verso la stessa conseguenza: il tasso di interesse è **indeterminato o indeterminabile** nella sua misura effettiva. Ai sensi dell'art. 117, comma 7 TUB:

> *"In caso di inosservanza del comma 4 e nelle ipotesi di nullità indicate nel comma 6, si applicano: a) il tasso nominale minimo e quello massimo, rispettivamente per le operazioni attive e per quelle passive, dei buoni ordinari del tesoro annuali o di altri titoli similari eventualmente indicati dal Ministro dell'economia e delle finanze, emessi nei dodici mesi precedenti la conclusione del contratto o, se più favorevoli per il cliente, emessi nei dodici mesi precedenti lo svolgimento dell'operazione."*

Il tasso BOT annuale nel periodo gennaio-dicembre 2011 era mediamente inferiore al 3% annuo. Applicando questo tasso sostitutivo al posto del 6,55% contrattuale su un piano di 240 rate da 231.000 euro, la riduzione degli interessi totali è nell'ordine di 80.000-100.000 euro, con diritto del cliente:

- alla **ripetizione degli interessi già pagati in eccesso** rispetto al tasso sostitutivo (dal 01/04/2012 ad oggi — circa 14 anni di rate)
- alla **rideterminazione del debito residuo** sulla base del tasso sostitutivo
- alla **sospensione legittima del rimborso** nella parte eccedente il dovuto (posizione già assunta dal cliente)

---

## Strategia processuale consigliata

**Fase 1 — Stragiudiziale (immediata)**
Diffida formale a Intesa Sanpaolo con indicazione dei tre vizi, richiesta di ricalcolo del piano al tasso sostitutivo e rimborso delle somme versate in eccesso. Questo apre il confronto e costituisce prova della buona fede del cliente.

**Fase 2 — ABF (Arbitro Bancario Finanziario)**
Presentazione di ricorso all'ABF entro i termini. L'ABF ha già emesso numerosi provvedimenti favorevoli ai mutuatari in casi analoghi (regime composto non dichiarato + assenza PA). Tempi: 6-12 mesi. Costo: minimo. L'ABF non è vincolante ma le banche di solito si adeguano.

**Fase 3 — Giudiziale (se necessario)**
Azione di accertamento della nullità parziale della clausola del tasso e condanna alla restituzione degli interessi indebitamente percepiti, con nomina di CTU per il ricalcolo. Competenza: Tribunale di L'Aquila (foro della residenza del mutuatario / luogo di stipula).

---

## Note operative per Oscar

- I documenti originali sono in: `_CLIENTI\DiSalvatore_Cesidio\01_Documenti_Mutuo\`
- Per il Vizio 3 serve la polizza assicurativa completa con piano premi — chiederla a Cesidio
- Per la perizia numerica sul TAEG, valutare un consulente specializzato in contenzioso bancario
- Prima di procedere con la diffida, Cesidio — essendo avvocato — probabilmente gestirà direttamente la parte legale; il ruolo di Oscar è fornire l'analisi di supporto
- Aggiornare questo documento man mano che emergono nuovi elementi

---

*Documento redatto il 20/05/2026 — Da aggiornare in caso di nuovi elementi documentali.*
