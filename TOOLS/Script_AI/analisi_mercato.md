# Agente Analisi Mercato

## Obiettivo

Generare ogni mattina un report sintetico sui trend di mercato rilevanti per l'attività di consulenza di Oscar Ribichini. Il report viene salvato in una cartella dedicata e può essere condiviso con i clienti.

## Struttura del report

1. **Macro economia Italia** — indicatori chiave, notizie rilevanti
2. **Finanza aziendale e straordinaria** — operazioni M&A, ristrutturazioni, passaggi generazionali
3. **Bandi e finanziamenti** — nuove opportunità aperte a livello nazionale e regionale (Marche priority)
4. **Assicurazioni e welfare** — novità normative e di mercato
5. **Intelligenza artificiale per le imprese** — trend e strumenti nuovi per le PMI
6. **Segnali locali** — notizie economiche dal territorio marchigiano
7. **Trend social** — argomenti virali su LinkedIn, Facebook, Instagram, TikTok legati a economia, lavoro e impresa
8. **Gare d'appalto** — opportunità pubbliche rilevanti a livello nazionale e regionale Marche
9. **Crisi aziendali** — segnali di difficoltà, procedure concorsuali, ristrutturazioni in corso
10. **Radar Tendenze** — Top 5 trend del giorno in Italia + trend settoriali con direzione, domande frequenti e copertura social
11. **Parola del giorno** — analisi approfondita di una singola keyword: cos'è, perché è rilevante oggi, cosa chiedono le aziende, trend, copertura social, chiamata da fare, post pronto

## Fonti fisse per sezione

### 1. Macro Economia Italia

- ISTAT — istat.it (comunicati stampa PIL, inflazione, occupazione)
- Banca d'Italia — bancaditalia.it (proiezioni macroeconomiche)
- Il Sole 24 Ore — ilsole24ore.com (economia)
- ANSA Economia — ansa.it/economia

### 2. Finanza Aziendale e M&A

- Il Sole 24 Ore — sezione Finanza e Mercati
- MilanoFinanza — milanofinanza.it
- Dealflower — dealflower.it (operazioni M&A Italia)
- KPMG Italia — kpmg.com/it (report M&A)

### 3. Bandi e Finanziamenti

- MIMIT (ex MISE) — mimit.gov.it
- Invitalia — invitalia.it
- Regione Marche — regione.marche.it/bandi
- IncentivImpresa — incentivimpresa.it
- Unioncamere — unioncamere.it

### 4. Assicurazioni e Welfare

- PMI.it — pmi.it
- Il Sole 24 Ore — sezione Norme e Tributi
- ANIA (assicurazioni) — ania.it
- Welfare aziendale news — welfareaziendale.info

### 5. Intelligenza Artificiale per le PMI

- Osservatori.net (Politecnico Milano) — osservatori.net
- StartupItalia — startupitalia.eu
- Ninja Marketing — ninja.it
- Il Sole 24 Ore — sezione Tecnologia

### 6. Segnali Locali — Marche

- ANSA Marche — ansa.it/marche
- Regione Marche — regione.marche.it
- Camera di Commercio Marche — marche.camcom.it
- Confindustria Marche — confindustriamarche.it
- AnconaToday / CivitanovaNews economia

### 7. Trend Social

- DataReportal — datareportal.com (dati piattaforme Italia)
- Social Factor — socialfactor.it
- Ninja Marketing — ninja.it
- LinkedIn Newsroom — news.linkedin.com

### 8. Gare d'Appalto

- ANAC — anticorruzione.it (banca dati nazionale gare)
- TuttoGare — tuttogare.it
- Regione Marche gare — regione.marche.it/gare
- Camera di Commercio Marche — marche.camcom.it

### 9. Crisi Aziendali

- Registro Imprese — registroimprese.it (procedure concorsuali)
- Il Fallimentarista — ilfallimentarista.it
- ANSA Marche economia — ansa.it/marche
- CNA Macerata / Confartigianato Marche — segnali locali di difficoltà

### 10. Radar Tendenze

- Google Trends — trends.google.it (Top 5 Italia + keyword settoriali)
- AnswerThePublic — answerthepublic.com (domande frequenti per keyword)
- Exploding Topics — explodingtopics.com (trend in anticipo)
- BuzzSumo — buzzsumo.com (copertura social degli argomenti)
- Google Alerts — alerts.google.com (notizie su keyword settoriali)

### 11. Parola del giorno

- Ricerca approfondita sulla keyword scelta (o proposta dal report se non indicata)
- Struttura: cos'è, perché è rilevante oggi, cosa chiedono le aziende, direzione trend, copertura social, chiamata da fare, post social pronto

Keyword settoriali fisse da monitorare:

- Passaggio generazionale impresa
- Welfare aziendale PMI
- Bandi finanziamenti Marche
- Intelligenza artificiale PMI
- Crisi aziendale ristrutturazione

## Output

File markdown giornaliero salvato in:
`e:\Lavori Code\TOOLS\Report_Mercato\AAAA-MM\AAAA-MM-GG_Report_Mercato.md`

## Struttura cartelle

```text
Report_Mercato/
└── AAAA-MM/
    └── AAAA-MM-GG_Report_Mercato.md
```

A fine mese creare `AAAA-MM_Indice.md` nella sottocartella con link ai report del mese e una riga di sintesi per ognuno.

## Stato

Attivo — prima versione con fonti fisse generata l'08/05/2026.
Usare per 2 settimane prima di aggiungere nuove funzionalità.

## Da fare (prossimi sviluppi)

- Testare sezione Radar Tendenze nel prossimo report
- Attivare alert gare d'appalto su Banchedati.biz o FareAppalti
- Aggiungere sezione "Credito e tassi bancari" — utile per clienti che cercano finanziamenti
