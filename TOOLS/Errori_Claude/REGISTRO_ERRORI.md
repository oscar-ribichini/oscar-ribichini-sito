# REGISTRO ERRORI DI CLAUDE
## Scopo: raccogliere tutti gli errori ricorrenti per trovare soluzioni strutturali

Ogni errore include: contesto, causa radice, danno prodotto, soluzione corretta, regola da applicare in futuro.

---

## CATEGORIA: HTML / STAMPA / PDF

---

### ERR-001 — `overflow: hidden` taglia il contenuto in stampa
**Data:** 28/05/2026 | **Progetto:** Mobilcom Scheda 3 HTML  
**Cosa è successo:** Il Passo 5 (blocco full-width) era completamente tagliato nella stampa PDF. Tre tentativi consecutivi prima di trovare la causa radice.  
**Causa radice:** La classe `.passo` aveva `overflow: hidden`. Il blocco `.passo-full` lo ereditava E aveva anche il proprio `overflow: hidden`. Quando il contenuto superava l'altezza calcolata dal browser in modalità stampa, veniva silenziosamente tagliato.  
**Danno:** Tre versioni del file prodotte, tre errori consecutivi, tempo perso.  
**Soluzione corretta:** Rimuovere `overflow: hidden` da qualsiasi classe che contenga testo stampabile. Aggiungere `overflow: visible` esplicito sui blocchi full-width. Usare `border-radius` senza `overflow: hidden` — funziona ugualmente in screen, non taglia in stampa.  
**Regola futura:** Prima di produrre qualsiasi HTML per stampa, cercare TUTTE le occorrenze di `overflow: hidden` nel CSS e verificare che nessuna sia su un contenitore di testo.

---

### ERR-002 — Griglia CSS si spezza tra pagine senza `page-break-inside`
**Data:** 28/05/2026 | **Progetto:** Mobilcom Scheda 3 HTML  
**Cosa è successo:** Le "mosse parallele" (3 box in griglia) si spezzavano tra pagina 2 e 3. Gli header dei box rimanevano su una pagina, i body sull'altra.  
**Causa radice:** La griglia `.parallele` e le singole `.mossa` non avevano `page-break-inside: avoid`. Il browser in stampa spezza liberamente le griglie a cavallo pagina.  
**Danno:** Documento visivamente rotto, contenuto illeggibile in stampa.  
**Soluzione corretta:** Su ogni griglia e su ogni cella della griglia che non deve spezzarsi aggiungere sia `page-break-inside: avoid` che `break-inside: avoid` (la versione moderna). Usarli in coppia perché Acrobat/Chrome li gestiscono diversamente.  
**Regola futura:** Ogni `display: grid` o `display: flex` usato in un documento da stampare deve avere `page-break-inside: avoid; break-inside: avoid;` sulla griglia E su ogni figlio diretto.

---

### ERR-003 — Layout flex interno a un blocco full-width causa clipping in stampa
**Data:** 28/05/2026 | **Progetto:** Mobilcom Scheda 3 HTML  
**Cosa è successo:** Il Passo 5 usava un layout flex a due colonne internamente. Anche dopo aver tolto `overflow: hidden`, il flex causava overflow invisibile che la stampante Epson tagliava nell'area non stampabile.  
**Causa radice:** I browser calcolano l'altezza dei flex container in modo diverso in modalità stampa rispetto allo schermo. Un contenitore flex con due colonne di altezza diversa può superare l'altezza attesa dal layout di pagina.  
**Danno:** Terzo errore consecutivo sullo stesso blocco.  
**Soluzione corretta:** Nei documenti da stampare, evitare flex/grid INTERNI ai blocchi full-width. Usare layout verticale puro (blocchi impilati) dentro i contenitori che devono stare su una sola pagina.  
**Regola futura:** Blocco full-width + contenuto lungo + stampa = layout verticale puro dentro. Niente flex, niente grid interni se il blocco deve stare intero su una pagina.

---

### ERR-004 — Contenuto presente nel file MD omesso nella versione HTML
**Data:** 28/05/2026 | **Progetto:** Mobilcom Scheda 3 HTML  
**Cosa è successo:** La percentuale di accettazione dell'istanza (80-85%) con motivazione era presente nel file MD ma non è stata trasferita nell'HTML. Oscar l'ha notato dopo aver letto il documento.  
**Causa radice:** La conversione da MD a HTML non è stata fatta con una verifica sezione per sezione. Alcuni contenuti sono stati riscritti liberamente invece di essere trasferiti sistematicamente.  
**Danno:** Contenuto informativo importante mancante nel documento consegnato.  
**Soluzione corretta:** Quando si produce una versione HTML da un MD approvato, leggere il MD sezione per sezione e verificare che ogni blocco di contenuto sia presente nell'HTML prima di dichiararlo pronto.  
**Regola futura:** MD → HTML = verifica sistematica sezione per sezione. Non si dichiara il documento pronto senza aver letto entrambi in parallelo.

---

## CATEGORIA: CONTENUTO / FATTI

---

### ERR-005 — Confusione tra BSM (Banca di San Marino) e Banca delle Marche
**Data:** 28/05/2026 | **Progetto:** Mobilcom Panoramica Truffa  
**Cosa è successo:** In una versione del documento BSM è stato interpretato/usato come abbreviazione di "Banca delle Marche" invece di "Banca di San Marino". Il mutuo Mobilcom nasce da BSM = Banca di San Marino. Banca delle Marche non c'entra nulla.  
**Causa radice:** Abbreviazione ambigua non verificata sulla fonte. Assunzione fatta senza leggere il documento originale.  
**Danno:** Intera sezione Level 0 del documento da riscrivere. Catena securitizzazione errata.  
**Soluzione corretta:** Ogni abbreviazione nuova va verificata sul documento fonte prima di essere usata. Nel caso Mobilcom: BSM = Banca di San Marino, sempre e solo.  
**Regola futura:** Nel caso Mobilcom, prima di usare qualsiasi sigla o nome di istituto, verificare che corrisponda al soggetto corretto nella catena: BSM → CRSM/BAC/BSI → Veicolo di Sistema → S3 → DEX.

---

### ERR-006 — Frase offensiva verso il destinatario del documento
**Data:** 28/05/2026 | **Progetto:** Mobilcom Scheda 3 per Avv. Di Salvatore  
**Cosa è successo:** Il documento conteneva la frase "Aveva ragione — ma non per i motivi che pensava" rivolta all'avvocato. Oscar ha segnalato che poteva essere percepita come offensiva o condiscendente verso il professionista destinatario.  
**Causa radice:** Tono non calibrato sul destinatario. La frase era pensata come introduzione narrativa ma suonava come una correzione del professionista.  
**Danno:** Rischio di compromettere il rapporto con l'avvocato al primo contatto con il documento.  
**Soluzione corretta:** Sostituita con "Aveva ragione." — punto fermo, nessuna qualificazione.  
**Regola futura:** Qualsiasi documento destinato a un professionista esterno (avvocato, commercialista, consulente) va riletto con la domanda: "C'è qualcosa che potrebbe suonare come una critica alla sua competenza?" Se sì, riscrivere prima di consegnare.

---

## RIEPILOGO RAPIDO

| Codice | Categoria | Errore in sintesi | Regola chiave |
|--------|-----------|-------------------|---------------|
| ERR-001 | HTML/Stampa | `overflow:hidden` taglia il testo in stampa | Cercare e rimuovere tutti gli `overflow:hidden` prima di stampare |
| ERR-002 | HTML/Stampa | Griglia senza `page-break-inside` si spezza | Ogni grid/flex in stampa vuole `page-break-inside:avoid` su contenitore E figli |
| ERR-003 | HTML/Stampa | Flex interno a blocco full-width causa clipping Epson | Blocchi full-width da stampare = layout verticale puro dentro |
| ERR-004 | Contenuto | Contenuto del MD non trasferito nell'HTML | MD→HTML = verifica sezione per sezione prima di dichiarare pronto |
| ERR-005 | Fatti | BSM = Banca delle Marche invece di Banca di San Marino | Nel caso Mobilcom verificare sempre la catena: BSM=Banca di San Marino |
| ERR-006 | Tono | Frase condiscendente verso professionista esterno | Rileggere sempre i documenti esterni chiedendosi se c'è qualcosa che suona come critica |

---

*Ultimo aggiornamento: 28/05/2026*  
*Aggiungere nuovi errori con il formato ERR-NNN appena si verificano.*
