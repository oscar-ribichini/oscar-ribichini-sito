# Newsletter modello — Francesco AI
Data ricezione: 15 maggio 2026
Mittente: Francesco (creator AI italiano)
Piattaforma: Brevo/Sendinblue

---

## Oggetto
*(non riportato nello screenshot)*

## Testo completo

Ciao Ribichini,

l'ultima cosa che ho costruito mi ha divertito un sacco. È una piccola web UI locale per testare un modello di text-to-speech che gira tutto sul tuo PC Windows, senza cloud, senza API, senza costi. Apri, scrivi una frase, ascolti la voce. Te la metto subito in mano così la provi al volo.

Poi ti racconto tre progetti open-source che mi hanno colpito molto in questi giorni. Messi insieme raccontano benissimo una cosa: il focus AI si sta spostando dai chatbot generici ai sistemi che agiscono. Multimodalità, memoria persistente, integrazione nei workflow, AI operative. E il mondo open-source sta recuperando terreno in fretta.

Ah, e se ti sei perso il mio ultimo video su Cowork 3P di Claude Desktop, te lo rimetto in fondo: spiega come usare Claude con modelli alternativi spendendo molto meno.

---

**In questa edizione**
- Supertonic TTS in locale su Windows: la web UI che ho costruito
- Ti ricordi di OpenClaw? I tre progetti open-source che lo stanno superando
- [Video] Cowork 3P di Claude Desktop con DeepSeek, MiniMax e GLM

---

### Ho messo un text-to-speech locale su Windows: zero cloud, zero costi, 5 minuti di setup

Mi serviva un modo veloce per testare un modello TTS senza spendere niente in API e senza mandare in giro la mia voce. Quindi ho preso Supertonic, un modello text-to-speech molto leggero, e ci ho costruito sopra una mini web UI in Python + Gradio che gira tutta in locale sul mio PC Windows.

Il bello è che non serve un PC mostruoso. Apri la web UI nel browser, scrivi una frase, premi un pulsante, e ascolti la voce generata. Tutto sul tuo computer, niente che esce. La latenza onestamente è ottima.

Ho messo tutto in una repo pubblica con guida passo passo per Windows, fix per i problemi tipici di PowerShell, e link alle risorse. Se vuoi provarlo ti serve solo Python e cinque minuti.

Cosa trovi nella repo: app.py (la web UI), requirements.txt (dipendenze), .gitignore e un README completo con la guida per Windows.

[Vai alla repo su GitHub]

---

### Ti ricordi di OpenClaw? Ecco i tre progetti che lo stanno superando

Te l'avevo già raccontato qualche tempo fa: OpenClaw era quel runtime agentico che girava da terminale, con memorie persistenti, skill che si accumulavano, automazioni che lavoravano in background. Per molti è stato il primo assaggio vero di cosa volesse dire "agente AI" e non solo "chatbot".

In queste settimane sono comparsi tre progetti open-source che provano a fare cose simili, ma partendo da angoli diversi. Tutti e tre sono molto attivi su GitHub, e secondo me messi insieme spiegano dove sta andando il mondo degli agenti meglio di qualsiasi articolo che ho letto. Te li racconto in fila.

**OpenHuman** prova a essere il "sistema operativo personale" basato su AI. Lo installi sul tuo computer, gli colleghi Gmail, GitHub, Slack, Calendar e Drive, e ogni venti minuti lui va a leggere cosa è successo. Tutto viene compresso in piccoli file Markdown salvati in una cartella stile Obsidian, che puoi aprire e modificare a mano. Per te, l'agente non parte mai "vuoto": sa già chi sei e su cosa stai lavorando.

**Multica** va in un'altra direzione. Non è un agente singolo, è una piattaforma per gestire più agenti come se fossero colleghi di lavoro. Praticamente un Jira per AI: crei i task, li assegni a Claude Code, Codex, Gemini, Cursor o OpenCode, e la piattaforma si occupa di farli girare e monitorarli. È il primo che porta dentro l'AI il concetto di team management vero, con board, runtime e squad di agenti assegnabili.

**Hermes Agent**, di Nous Research, è quello che più di tutti raccoglie l'eredità di OpenClaw. Tant'è vero che hanno messo dentro un comando (hermes claw migrate) che importa al volo memoria, skill e configurazioni da una vecchia installazione OpenClaw. Lo installi su un VPS da 5 euro al mese, lo controlli da Telegram, WhatsApp, Slack o Discord, e l'agente continua a lavorare anche quando hai chiuso il computer. Ha pure una cosa che si chiama closed learning loop: si crea da solo nuove skill dalle esperienze passate e le riusa. 151k stelle su GitHub, non poco.

Una cosa che voglio dirti subito, così non perdi tempo: sono tutti e tre in early beta. OpenHuman lo scrive proprio nel README. E quando colleghi Gmail, Slack, Calendar, GitHub o Drive, stai dando accesso a tutta la tua vita digitale. Quindi: divertiti, sperimenta, ma non li metterei domani su un cliente in ambiente regolamentato (ISO 27001, GDPR, NIS2). Per l'uso personale invece sono perfetti per capire dove sta andando il mondo.

OpenHuman è il "cervello digitale personale", Multica è il "team di colleghi AI", Hermes è "l'agente che vive sul cloud e ti risponde anche da Telegram". Tre pezzi diversi dello stesso puzzle, e il puzzle è chiaro: il focus si sta spostando dai chatbot generici verso agenti, realtime, multimodalità, memoria persistente, integrazione nei workflow aziendali, AI operative. E l'open-source sta recuperando terreno in fretta sul mondo chiuso.

Se dovessi sceglierne uno solo da provare questo weekend, partirei da OpenHuman: ha l'onboarding più semplice, l'effetto "wow" arriva in pochi minuti, e ti fa capire al volo cosa significa avere un'AI che ti conosce davvero. Hermes lo terrei per quando vuoi smanettare di brutto, Multica per quando hai un workflow di team da automatizzare.

[Vedi OpenHuman su GitHub] [Vedi Hermes Agent su GitHub]

---

### Nuovo video YouTube

**Cowork 3P: usa Claude Desktop con DeepSeek, MiniMax e GLM spendendo una frazione**

Ti ricordi che la settimana scorsa ti avevo parlato della third-party inference dentro Claude Desktop? Nel video ti faccio vedere come funziona davvero, passo passo, con la finestra dei modelli aperta e i provider attivi sotto gli occhi.

Tutto testato dal vivo, con demo reali:
- Cos'è la 3P: cosa fa la modalità third-party e perché cambia il gioco
- DeepSeek, MiniMax, GLM: come li colleghi e quali girano direttamente senza proxy
- Il proxy open-source che ho costruito io per far girare anche Ollama e altri modelli compatibili
- Demo live di configurazione vera dentro Claude Desktop, niente slide
- Costi reali: quanto risparmi davvero rispetto al solo Claude

[Guarda il video su YouTube]

---

### Prova una cosa oggi e raccontami!

1. Clona la mia repo supertonic-local-demo, segui il README, e prova il TTS in locale. Bastano cinque minuti.
2. Apri il README di OpenHuman o di Hermes Agent e leggi le prime venti righe: capisci subito di che stiamo parlando.
3. Se hai un VPS che dorme da qualche parte, prova ad installare Hermes e lascialo lavorare. Lo controlli da Telegram.

Mandami uno screenshot o la tua esperienza → li metto in evidenza nella prossima edizione con commenti pratici!

**Domanda della settimana:** se potessi avere un agente AI che lavora per te in background tutto il giorno, cosa gli faresti fare per primo?

---

A presto,
Francesco
L'AI che ti fa lavorare meglio.

---

## Note di analisi

- Formato: newsletter lunga, scannable, tono da amico esperto
- Struttura: apertura personale → indice → sezione tecnica → sezione editoriale narrativa → video → CTA numerata → domanda della settimana
- Punto di forza: filo narrativo tra i tool ("tre pezzi dello stesso puzzle")
- Onestà sui limiti: segnala early beta e rischi GDPR prima di entusiasmarsi
- Piattaforma invio: Brevo (Sendinblue)
