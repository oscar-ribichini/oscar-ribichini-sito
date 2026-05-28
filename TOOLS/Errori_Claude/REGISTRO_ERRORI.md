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
**Cosa è successo:** La percentuale di accettazione dell'istanza (80-85%) con motivazione era presente nel file MD ma non è stata trasferita nell'HTML.  
**Causa radice:** La conversione da MD a HTML non è stata fatta con una verifica sezione per sezione.  
**Danno:** Contenuto informativo importante mancante nel documento consegnato.  
**Soluzione corretta:** Quando si produce una versione HTML da un MD approvato, leggere il MD sezione per sezione e verificare che ogni blocco di contenuto sia presente nell'HTML.  
**Regola futura:** MD → HTML = verifica sistematica sezione per sezione. Non si dichiara il documento pronto senza aver letto entrambi in parallelo.

---

### ERR-007 — Badge inline nel testo si spezza su più righe e gonfia l'altezza della riga
**Data:** 28/05/2026 | **Progetto:** Mobilcom Scheda 2 HTML  
**Cosa è successo:** I badge ("Giorno prima del pignoramento", "11 giorni dopo il pignoramento", "8 mesi documentati") erano inline nel testo della timeline. In stampa la colonna è stretta e il badge andava a capo, occupando due righe e rendendo la riga della timeline alta il doppio.  
**Causa radice:** Badge con testo medio-lungo posizionato inline (`vertical-align: middle`) in una colonna stretta. In stampa le larghezze cambiano rispetto allo schermo e il badge non trova spazio sulla stessa riga.  
**Danno:** Timeline con righe di altezza irregolare, aspetto non professionale.  
**Soluzione corretta:** I badge vanno sempre su riga propria, preceduti da `<br>`. CSS: `display: inline-block; margin-top: 3px;` — mai `vertical-align: middle` inline nel testo.  
**Regola futura:** In qualsiasi timeline o tabella da stampare, i badge non vanno mai inline nel testo. Sempre `<br>` + badge su riga separata.

---

### ERR-008 — Troppi `page-break-inside: avoid` causano spazio bianco enorme tra sezioni
**Data:** 28/05/2026 | **Progetto:** Mobilcom Scheda 2 HTML  
**Cosa è successo:** Applicando `page-break-inside: avoid` su ogni singola riga della timeline, il browser non riusciva a spezzare la timeline tra le pagine. Quando la timeline non entrava tutta in pagina 1, il browser spostava l'intera sezione in pagina 2 lasciando metà pagina 1 bianca.  
**Causa radice:** `page-break-inside: avoid` su elementi ripetuti (righe di lista, righe di timeline) blocca il flusso naturale. Il browser preferisce lasciare spazio bianco piuttosto che violare il vincolo.  
**Danno:** Pagina 1 per metà bianca, aspetto non professionale, perdita di spazio.  
**Soluzione corretta:** `page-break-inside: avoid` va usato SOLO su blocchi che non devono MAI spezzarsi (box singoli, card, conclusioni). Le righe di timeline e liste possono spezzarsi liberamente tra pagine — è normale e corretto.  
**Regola futura:** `page-break-inside: avoid` = solo su box singoli e card. MAI su righe ripetute di liste o timeline. Il testo lungo fluisce naturalmente — non forzarlo.

---

### ERR-009 — `page-break-before: always` su un titolo lascia spazio bianco nella pagina precedente
**Data:** 28/05/2026 | **Progetto:** Mobilcom Scheda 2 HTML  
**Cosa è successo:** Aggiungendo `page-break-before: always` sul titolo "I tre fatti" per forzarlo in pagina 2, la pagina 1 terminava con grande spazio bianco sotto la timeline.  
**Causa radice:** Il salto forzato consuma tutto lo spazio rimanente della pagina precedente senza riempirlo.  
**Danno:** Pagina 1 con metà inferiore vuota — peggio della situazione iniziale.  
**Soluzione corretta:** Non usare `page-break-before: always` per risolvere problemi di layout. Usarlo solo quando un capitolo deve iniziare su pagina nuova per scelta editoriale precisa (es. pagina 2 che inizia sempre con una sezione specifica). Per problemi di flusso, agire sulla dimensione del contenuto (font, padding, margini) finché entra naturalmente.  
**Regola futura:** `page-break-before: always` = solo per salti pagina editoriali voluti. Per problemi di flusso: ridurre font/padding/margini finché il contenuto entra. Non forzare salti per coprire problemi di dimensionamento.

---

### ERR-010 — L'anteprima stampa di Chrome non rispecchia il risultato reale di Acrobat/Epson
**Data:** 28/05/2026 | **Progetto:** Mobilcom Scheda 2 HTML  
**Cosa è successo:** L'anteprima Chrome mostrava una cosa, Acrobat/la stampa reale mostrava un'altra. Correzioni fatte sull'anteprima Chrome non risolvevano il problema reale.  
**Causa radice:** Chrome e Acrobat calcolano i layout di stampa in modo diverso. Le dimensioni della colonna, i font hinting e il calcolo dei margini differiscono. Un badge che sta su una riga in Chrome può andare a capo in Acrobat.  
**Danno:** Cicli di correzione inutili perché si correggeva il sintomo sbagliato.  
**Soluzione corretta:** Il test definitivo è sempre su Acrobat o stampando fisicamente. Chrome serve solo come anteprima rapida. Ogni modifica va verificata salvando come PDF da Chrome (Ctrl+P → Salva come PDF) e aprendo il PDF risultante.  
**Regola futura:** Per verificare HTML da stampare: salvare sempre come PDF da Chrome e aprire il PDF. Non fidarsi dell'anteprima visiva di Chrome nel pannello stampa.

---

## CATEGORIA: CONTENUTO / FATTI

---

### ERR-005 — Confusione tra BSM (Banca di San Marino) e Banca delle Marche
**Data:** 28/05/2026 | **Progetto:** Mobilcom Panoramica Truffa  
**Cosa è successo:** BSM usato come abbreviazione di "Banca delle Marche" invece di "Banca di San Marino".  
**Causa radice:** Abbreviazione ambigua non verificata sulla fonte.  
**Danno:** Intera sezione Level 0 del documento da riscrivere.  
**Soluzione corretta:** Ogni abbreviazione nuova va verificata sul documento fonte prima di essere usata.  
**Regola futura:** Nel caso Mobilcom: BSM = Banca di San Marino, sempre e solo.

---

### ERR-006 — Frase condiscendente verso il destinatario del documento
**Data:** 28/05/2026 | **Progetto:** Mobilcom Scheda 3 per Avv. Di Salvatore  
**Cosa è successo:** "Aveva ragione — ma non per i motivi che pensava" — percepita come critica verso l'avvocato.  
**Causa radice:** Tono non calibrato sul destinatario professionale.  
**Danno:** Rischio di compromettere il rapporto con l'avvocato.  
**Soluzione corretta:** "Aveva ragione." — punto fermo, nessuna qualificazione.  
**Regola futura:** Rileggere sempre i documenti per professionisti esterni chiedendosi: "C'è qualcosa che suona come critica alla sua competenza?"

---

## RIEPILOGO RAPIDO

| Codice | Categoria | Errore in sintesi | Regola chiave |
|--------|-----------|-------------------|---------------|
| ERR-001 | HTML/Stampa | `overflow:hidden` taglia il testo | Cercare e rimuovere tutti gli `overflow:hidden` |
| ERR-002 | HTML/Stampa | Grid senza `page-break-inside` si spezza | `page-break-inside:avoid` su contenitore E figli |
| ERR-003 | HTML/Stampa | Flex interno a blocco full-width clipping Epson | Blocchi full-width = layout verticale puro dentro |
| ERR-004 | Contenuto | Contenuto MD non trasferito nell'HTML | Verifica sezione per sezione MD→HTML |
| ERR-005 | Fatti | BSM = Banca delle Marche invece di San Marino | BSM = Banca di San Marino, sempre |
| ERR-006 | Tono | Frase condiscendente verso professionista | Rileggere prima di consegnare a esterni |
| ERR-007 | HTML/Stampa | Badge inline si spezza su più righe in stampa | Badge sempre su riga propria con `<br>` prima |
| ERR-008 | HTML/Stampa | Troppi `avoid` causano spazio bianco enorme | `page-break-inside:avoid` solo su box singoli, mai su righe ripetute |
| ERR-009 | HTML/Stampa | `page-break-before:always` lascia pagina bianca | Usarlo solo per salti editoriali voluti, non per problemi di flusso |
| ERR-010 | HTML/Stampa | Anteprima Chrome ≠ risultato Acrobat/Epson | Verificare sempre salvando PDF e aprendo in Acrobat |

---

## ⭐ MODELLO CSS SICURO PER HTML DA STAMPARE
### Da usare come base per ogni nuovo documento — non reinventare da zero

```css
/* REGOLE BASE STAMPA — copiare sempre in ogni nuovo HTML */
@page { margin: 20mm 20mm 18mm 20mm; size: A4; }

/* ❌ MAI usare overflow:hidden su contenitori di testo */
/* ✅ Tutti i contenitori di testo: overflow:visible (default) */

/* GRIGLIE E FLEX: sempre con page-break su contenitore E figli */
.grid-container {
  display: grid;
  page-break-inside: avoid;
  break-inside: avoid;
}
.grid-item {
  page-break-inside: avoid;
  break-inside: avoid;
}

/* BLOCCHI SINGOLI CHE NON DEVONO SPEZZARSI (box, card, conclusioni) */
.box-singolo {
  page-break-inside: avoid;
  break-inside: avoid;
}

/* RIGHE RIPETUTE (timeline, liste, tabelle): NO page-break-inside */
/* Lasciarle fluire liberamente tra le pagine — è corretto */
.riga-timeline { /* nessun page-break */ }

/* BADGE: sempre su riga propria, mai inline nel testo */
.badge {
  display: inline-block;
  margin-top: 3px;
  /* preceduto da <br> nell'HTML */
}

/* SALTI PAGINA EDITORIALI: solo quando voluti esplicitamente */
.nuova-pagina { page-break-before: always; break-before: page; }

/* TITOLO AGGANCIATO AL CONTENUTO SUCCESSIVO */
h2, h3 { page-break-after: avoid; break-after: avoid; }

/* ❌ MAI usare page-break-before:always per risolvere spazi bianchi */
/* ❌ MAI usare page-break-inside:avoid su righe ripetute di liste */
/* ✅ Per problemi di spazio: ridurre font-size e padding finché entra */
```

### Checklist pre-consegna (eseguire SEMPRE prima di dichiarare pronto)
1. ☐ Nessun `overflow: hidden` su contenitori di testo
2. ☐ Ogni grid/flex ha `page-break-inside: avoid` su contenitore E figli diretti
3. ☐ Blocchi full-width con contenuto lungo: layout verticale puro dentro (no flex/grid interni)
4. ☐ Badge sempre preceduti da `<br>`, mai inline nel testo
5. ☐ `page-break-inside: avoid` solo su box singoli — mai su righe ripetute
6. ☐ Nessun `page-break-before: always` usato per coprire problemi di flusso
7. ☐ Contenuto del sorgente (MD o brief) trasferito sezione per sezione
8. ☐ Verificato salvando come PDF da Chrome e aprendo in Acrobat (non solo anteprima)

---

*Ultimo aggiornamento: 28/05/2026*  
*Aggiungere nuovi errori con il formato ERR-NNN appena si verificano.*
