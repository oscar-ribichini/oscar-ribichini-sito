# Guida Google Search Console — Passo per Passo
Data: 2026-05-28

---

## Perché farlo

Senza Search Console, Google non sa che oscar-ribichini.it esiste. Il sito è online ma invisibile nei risultati di ricerca. Configurare Search Console e sottomettere la sitemap risolve il problema in 1-3 settimane.

---

## Passo 1 — Aprire Search Console

1. Vai su search.google.com/search-console
2. Accedi con il tuo account Google (globalarea@gmail.com)
3. Clicca "Aggiungi proprietà"
4. Scegli "Prefisso URL"
5. Inserisci: https://oscar-ribichini.it
6. Clicca "Continua"

---

## Passo 2 — Verificare di essere il proprietario del sito

Google deve verificare che il sito è tuo. Ci sono diversi metodi — usa quello più semplice per GitHub Pages.

### Metodo consigliato: file HTML
1. Google ti fornisce un file HTML da scaricare (es: google1234abcd.html)
2. Carica quel file nella cartella principale del tuo sito su GitHub
3. Torna su Search Console e clicca "Verifica"

### Metodo alternativo: tag meta
1. Google ti fornisce un tag meta tipo: `<meta name="google-site-verification" content="xxx">`
2. Aggiungilo nell'`<head>` del file index.html del sito
3. Torna su Search Console e clicca "Verifica"

Se non sai quale metodo usare: portami il file index.html del sito e lo aggiungo io direttamente.

---

## Passo 3 — Sottomettere la sitemap

La sitemap è un file che dice a Google quali pagine esistono nel sito.

1. Una volta verificato il sito, vai nella sezione "Sitemap" nel menu a sinistra
2. Nel campo "Aggiungi una nuova sitemap" scrivi: sitemap.xml
3. Clicca "Invia"

Se il sito non ha ancora una sitemap.xml, lo creo io nel prossimo aggiornamento del sito.

---

## Passo 4 — Richiedere l'indicizzazione manuale

1. Vai nella sezione "Ispezione URL"
2. Inserisci: https://oscar-ribichini.it
3. Clicca "Richiedi indicizzazione"
4. Fai lo stesso per ogni pagina importante del sito

---

## Cosa aspettarsi

- Settimana 1-2: Google inizia a crawlare il sito
- Settimana 2-4: il sito appare nei risultati cercando "Oscar Ribichini"
- Mese 2-3: il sito scala nelle posizioni se il contenuto è rilevante

---

## Dopo la configurazione — cosa monitorare

Aprire Search Console una volta a settimana e guardare:
- **Copertura**: quante pagine sono indicizzate
- **Rendimento**: quante volte appare il sito nelle ricerche e quanti click riceve
- **Problemi**: errori da risolvere

Annotare i dati ogni settimana in: REPUTAZIONE_SOCIAL\07_Metriche_KPI\

---

## Note importanti

- Il problema HTTPS su GitHub Pages (certificato TLS bloccato) deve essere risolto prima o insieme a Search Console. Se il sito non ha HTTPS funzionante, Google lo penalizza.
- Soluzione certificato: valutare passaggio a Netlify (gratuito, HTTPS automatico). File memoria: project_sito_hosting.md
- Se si passa a Netlify, il dominio resta oscar-ribichini.it — cambia solo l'hosting

---

✅ Verificato — procedura standard Google Search Console, aggiornata 2026.
