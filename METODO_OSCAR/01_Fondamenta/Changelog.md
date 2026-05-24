# Changelog — Metodo Oscar

---

## v2.1 — 24/05/2026

- Aggiunto sistema Google Alert per monitoraggio aggiornamenti Anthropic (3 alert: new model, API update, news)
- Aggiunto trigger anticipato per test di calibrazione: se arriva alert su nuovo modello, non aspettare il trimestre
- Integrata istruzione di aggiornamento data prossimo test nel Registro degli Apprendimenti dopo alert

## v2.0 — 24/05/2026

- Aggiunta FASE 0b: autocontrollo dell'output prima di consegnarlo
- Aggiunta FASE 0c: voce del disaccordo con protocollo chiaro
- Aggiunta domanda di autocontrollo anticorpo al rituale vuoto nella Fase 0
- Aggiunto limite di competenza dichiarato per lenti specialistiche (Legale, Finanziaria, Medica)
- Aggiunta scala di confidenza sull'output: Verificato / Probabile / Da confermare
- Aggiunta riga di responsabilità finale su ogni output strutturato
- Aggiunta lettura automatica _STATO_ all'inizio di ogni sessione — copre sessioni interrotte
- Aggiunta riga "Lente chiave della sessione" nel _STATO_ — trasferimento progressivo del vocabolario a Oscar
- Aggiunta sezione APPRENDIMENTI DI QUESTA SESSIONE nel _STATO_
- Aggiunta FASE 1b: trigger di riallineamento con comando /riallinea
- Aggiunta FASE 2b: revisione periodica dall'alto ogni 10 sessioni
- Aggiunta FASE 3: chiusura formale del progetto con archiviazione
- Aggiunto Registro degli Apprendimenti — file Apprendimenti.md
- Aggiunta gestione output esterni: versione interna + versione esterna separata
- Aggiunto Test di calibrazione trimestrale — procedura dettagliata in 6 passi
- Risolto rischio 1 (rituale vuoto): domanda di autocontrollo sulla qualità delle domande
- Risolto rischio 2 (fiducia cieca): scala di confidenza + riga di responsabilità
- Risolto rischio 3 (sessione interrotta): lettura automatica _STATO_ a inizio sessione
- Risolto rischio 4 (dipendenza): lente chiave trasferisce vocabolario a Oscar
- Risolto rischio 5 (lenti usate male): limite di competenza dichiarato
- Risolto rischio 6 (proliferazione file): un solo file per progetto + archiviazione automatica
- Risolto rischio 7 (non scala): due versioni dell'output, interna ed esterna
- Risolto rischio 8 (aggiornamento Claude): test trimestrale di calibrazione

## v1.0 — 24/05/2026

- Prima strutturazione del metodo in sessione con Claude
- Definite Fase 0, Fase 1, Fase 2, comando /stallo
- Introdotto il principio "18 lenti in silenzio come motore interno"
- Introdotto il sistema a caratteristiche oggettive per la selezione delle lenti
- Creata struttura cartelle METODO_OSCAR
- Analisi del metodo con tutte le 18 lenti — identificate 3 lenti rosse
- Lente rossa Psicologia risolta: la disciplina sta in Claude, non in Oscar
- Lente rossa Giornalismo risolta: soglia di attivazione basata su caratteristiche oggettive
- Lente rossa Management risolta: riga ⚙️ METODO APPLICATO nel file _STATO_
