import sys
sys.stdout.reconfigure(encoding='utf-8')

with open(r'e:\Lavori Code\QUANTUM\Marketing\Materiale_Grafico\icona_b64.txt', 'r') as f:
    icona = f.read().strip()
with open(r'e:\Lavori Code\QUANTUM\Marketing\Materiale_Grafico\scritta_b64.txt', 'r') as f:
    scritta = f.read().strip()

CSS = """
* { margin: 0; padding: 0; box-sizing: border-box; }
body { font-family: Georgia, serif; font-size: 11pt; color: #1a1a1a; background: #fff; }
.pagina { width: 210mm; min-height: 297mm; margin: 0 auto; padding: 14mm 16mm 16mm 16mm; }
.intestazione { display: flex; align-items: center; justify-content: space-between; border-bottom: 2px solid #B8962E; padding-bottom: 8px; margin-bottom: 14px; }
.logo-wrap { display: flex; align-items: center; gap: 10px; }
.logo-wrap img.icona { height: 42px; }
.logo-wrap img.scritta { height: 28px; }
.intestazione-destra { text-align: right; font-size: 8.5pt; color: #666; line-height: 1.6; }
.intestazione-destra strong { color: #B8962E; font-size: 9pt; }
.titolo-doc { text-align: center; margin-bottom: 12px; }
.titolo-doc h1 { font-size: 14pt; font-weight: bold; color: #1a1a1a; letter-spacing: 0.5px; margin-bottom: 2px; }
.titolo-doc .sottotitolo { font-size: 9.5pt; color: #666; font-style: italic; }
.titolo-doc .tipo-documento { display: inline-block; font-size: 16pt; font-weight: 900; color: #1a1a1a; letter-spacing: 2px; text-transform: uppercase; border-bottom: 3px solid #B8962E; padding-bottom: 2px; margin-bottom: 4px; font-style: normal; }
.dati-cliente { display: grid; grid-template-columns: 1fr 1fr; gap: 6px 20px; background: #faf8f3; border: 1px solid #ddd; border-left: 3px solid #B8962E; padding: 10px 14px; margin-bottom: 16px; border-radius: 2px; }
.campo { display: flex; flex-direction: column; gap: 2px; }
.campo label { font-size: 7.5pt; color: #888; text-transform: uppercase; letter-spacing: 0.5px; }
.campo .linea { border-bottom: 1px solid #bbb; height: 18px; width: 100%; }
.campo-largo { grid-column: span 2; }
.sezione { margin-bottom: 14px; page-break-inside: avoid; }
.sezione-titolo { background: #B8962E; color: #fff; font-size: 10.5pt; font-weight: bold; padding: 5px 12px; letter-spacing: 0.8px; border-radius: 2px 2px 0 0; }
.sezione-corpo { border: 1px solid #ddd; border-top: none; border-radius: 0 0 2px 2px; overflow: hidden; }
.sezione-opzionale { opacity: 0.38; }
.sezione-opzionale .sezione-titolo { background: #999; }
.sezione-opzionale.attiva { opacity: 1; }
.sezione-opzionale.attiva .sezione-titolo { background: #1a1a1a; font-size: 11.5pt; letter-spacing: 1.2px; text-transform: uppercase; border-left: 6px solid #B8962E; padding-left: 10px; }
.sezione-opzionale.attiva .sezione-corpo { border: 2.5px solid #1a1a1a; border-top: none; }
.sezione-opzionale.attiva .voce .testo { font-weight: bold; font-size: 10pt; color: #000; }
.sezione-opzionale.attiva .voce .testo .nota { font-weight: normal; font-size: 8pt; }
.voce { display: flex; align-items: flex-start; gap: 10px; padding: 5px 12px; border-top: 1px solid #f0f0f0; line-height: 1.4; }
.voce:first-child { border-top: none; }
.voce:nth-child(even) { background: #fdfcfa; }
.voce input[type=checkbox] { margin-top: 2px; width: 14px; height: 14px; flex-shrink: 0; accent-color: #B8962E; }
.voce .testo { font-size: 9.5pt; color: #1a1a1a; }
.voce .testo .nota { display: block; font-size: 8pt; color: #888; font-style: italic; margin-top: 1px; }
.istruzione-opzionali { margin-bottom: 12px; background: #fff8e6; border: 1px solid #e8c840; border-left: 4px solid #B8962E; padding: 8px 14px; font-size: 8.5pt; color: #555; border-radius: 2px; }
.istruzione-opzionali strong { color: #B8962E; }
.note-finali { margin-top: 16px; background: #faf8f3; border: 1px solid #ddd; border-left: 3px solid #B8962E; padding: 10px 14px; font-size: 8.5pt; color: #555; line-height: 1.6; border-radius: 2px; }
.note-finali strong { color: #B8962E; }
.pie-pagina { margin-top: 18px; padding-top: 8px; border-top: 1px solid #ddd; display: flex; justify-content: space-between; font-size: 7.5pt; color: #aaa; }
.pie-pagina span { color: #B8962E; font-weight: bold; }
@media print { .pagina { margin: 0; padding: 12mm 14mm 14mm 14mm; } }
"""

def intestazione():
    return f"""  <div class="intestazione">
    <div class="logo-wrap">
      <img class="icona" src="data:image/png;base64,{icona}" alt="">
      <img class="scritta" src="data:image/png;base64,{scritta}" alt="QUANTUM">
    </div>
    <div class="intestazione-destra">
      <strong>Quantum S.r.l.</strong><br>
      Via Castelletta 8 &mdash; 63831 Rapagnano (FM)<br>
      Tel. +39 0734 63831 &middot; quantum@pec.cloud
    </div>
  </div>"""

DATI = """  <div class="dati-cliente">
    <div class="campo campo-largo"><label>Ragione Sociale / Nome e Cognome del Titolare</label><div class="linea"></div></div>
    <div class="campo"><label>P.IVA / Codice Fiscale</label><div class="linea"></div></div>
    <div class="campo"><label>Data di compilazione</label><div class="linea"></div></div>
    <div class="campo"><label>Consulente Quantum di riferimento</label><div class="linea"></div></div>
    <div class="campo campo-largo"><label>Tipo di operazione richiesta</label><div class="linea"></div></div>
  </div>"""

ISTRUZIONE = """  <div class="istruzione-opzionali">
    <strong>Sezioni aggiuntive:</strong> le sezioni in grigio si applicano solo se pertinenti all&rsquo;operazione. Quella relativa all&rsquo;operazione in corso viene evidenziata prima della stampa.
  </div>"""

NOTE = """  <div class="note-finali">
    <strong>Note operative:</strong> Tutti i documenti devono essere forniti in formato digitale (PDF scansionato o file originale). Per qualsiasi chiarimento contattare il proprio consulente Quantum di riferimento prima di procedere alla raccolta.
  </div>"""

def voce(testo, nota=None):
    n = f'<span class="nota">{nota}</span>' if nota else ''
    return f'    <div class="voce"><input type="checkbox"><div class="testo">{testo}{n}</div></div>'

def sezione(num, titolo, voci):
    corpo = "\n".join(voci)
    return f"""  <div class="sezione"><div class="sezione-titolo">{num} &middot; {titolo}</div><div class="sezione-corpo">
{corpo}
  </div></div>"""

def sezione_opz(titolo, voci, attiva=False):
    cls = "sezione sezione-opzionale attiva" if attiva else "sezione sezione-opzionale"
    corpo = "\n".join(voci)
    return f"""  <div class="{cls}"><div class="sezione-titolo">+ SE L&rsquo;OPERAZIONE &Egrave; {titolo}</div><div class="sezione-corpo">
{corpo}
  </div></div>"""

def pagina(titolo_h1, tipo_doc, sottotitolo, sezioni_std, sezioni_extra, label_pie):
    return f"""<!DOCTYPE html>
<html lang="it">
<head><meta charset="UTF-8"><title>Checklist Affidamento &mdash; {label_pie}</title>
<style>{CSS}</style></head>
<body><div class="pagina">
{intestazione()}
  <div class="titolo-doc">
    <h1>{titolo_h1}</h1>
    <div class="sottotitolo"><span class="tipo-documento">{tipo_doc}</span><br>{sottotitolo}</div>
  </div>
{DATI}
{chr(10).join(sezioni_std)}
{ISTRUZIONE}
{chr(10).join(sezioni_extra)}
{NOTE}
  <div class="pie-pagina"><div><span>{label_pie}</span></div><div>Quantum S.r.l. &middot; documento riservato uso interno</div></div>
</div></body></html>"""

# ── Sezioni standard comuni ──────────────────────────────────────────────
s_identificativi_di = sezione("1", "DOCUMENTI IDENTIFICATIVI", [
    voce("Documento di riconoscimento in corso di validit&agrave; del Titolare", "Carta d&rsquo;identit&agrave; o patente di guida"),
    voce("Codice fiscale del Titolare"),
    voce("Documento di riconoscimento e codice fiscale di ogni Garante"),
    voce("E-mail personale del Titolare e di ogni Garante"),
    voce("Numero di cellulare del Titolare e di ogni Garante", "Necessario per firma digitale a distanza e identificazione tramite SPID"),
])
s_aziendali = sezione("2", "DOCUMENTI AZIENDALI", [
    voce("Visura camerale / C.C.I.A.A. aggiornata"),
    voce("Relazione / Presentazione aziendale"),
])
s_fiscali_di = sezione("3", "DOCUMENTI FISCALI E REDDITUALI", [
    voce("Modello UNICO 2024 completo di quadro IVA/IRAP e ricevuta di presentazione"),
    voce("Modello UNICO 2025 completo di quadro IVA/IRAP e ricevuta di presentazione"),
    voce("Dichiarazione IVA 2024 e relativa ricevuta di presentazione"),
    voce("Dichiarazione IVA 2025 e relativa ricevuta di presentazione"),
    voce("Documentazione reddituale 2025 di ogni Garante", "Modello UNICO 2025, Mod. 730/2025 o CU"),
    voce("Bilancio provvisorio aggiornato a data recente"),
])
s_finanziaria = sezione("4", "POSIZIONE FINANZIARIA E TRIBUTARIA", [
    voce("Sintesi degli affidamenti bancari in essere", "Mutui, prestiti, leasing, fidi in c/c, conto anticipi"),
    voce("Dettaglio debiti tributari"),
    voce("Estratto conto fiscale &mdash; Agenzia delle Entrate", "Posizione fiscale, versamenti, deleghe F24, eventuali irregolarit&agrave;"),
    voce("Estratto conto &mdash; Agenzia della Riscossione (ex Equitalia)", "Carichi iscritti a ruolo, rateizzazioni, sospensioni, avvisi, pignoramenti"),
    voce("Estratto contributivo INPS", "Posizione contributiva, versamenti, eventuali omissioni, rateizzazioni"),
    voce("DURC in corso di validit&agrave;"),
])

# ── Sezioni opzionali ────────────────────────────────────────────────────
opz_investimento = sezione_opz("UN INVESTIMENTO", [
    voce("Business Plan"),
    voce("Fatture e/o preventivi a supporto dell&rsquo;investimento"),
])
opz_fideiussione = sezione_opz("UNA FIDEIUSSIONE", [
    voce("Contratto da cui sorge la richiesta di fideiussione"),
    voce("Testo della fideiussione", "In alternativa: pro-forma interno Quantum"),
])
opz_simest = sezione_opz("UNA GARANZIA SIMEST", [
    voce("Pre-delibera SIMEST"),
    voce("Contratto di finanziamento"),
])
opz_mutuo = sezione_opz("UN MUTUO IPOTECARIO", [
    voce("Atto di propriet&agrave; del bene immobile da ipotecare"),
    voce("Contratto preliminare tra le parti", "Solo nel caso di acquisto di un bene immobile"),
    voce("Computo metrico e atto di propriet&agrave; del terreno", "Solo nel caso di costruzione di un bene immobile"),
    voce("Perizia tecnica sull&rsquo;immobile da ipotecare", "Redatta da un tecnico di fiducia della Banca"),
])

# ── DITTA INDIVIDUALE ────────────────────────────────────────────────────
html_di = pagina(
    "DOCUMENTAZIONE PER PRATICA DI AFFIDAMENTO BANCARIO",
    "DITTA INDIVIDUALE",
    "da consegnare a Quantum prima dell&rsquo;avvio della pratica",
    [s_identificativi_di, s_aziendali, s_fiscali_di, s_finanziaria],
    [opz_investimento, opz_fideiussione, opz_simest],
    "DITTA INDIVIDUALE"
)

# ── SOCIETARIA ───────────────────────────────────────────────────────────
s_societari = sezione("1", "DOCUMENTI SOCIETARI", [
    voce("Atto costitutivo e statuto societario"),
    voce("Eventuali atti di modifica successivi alla costituzione"),
    voce("Visura camerale / C.C.I.A.A. aggiornata"),
    voce("Relazione / Presentazione aziendale"),
])
s_identificativi_soc = sezione("2", "DOCUMENTI IDENTIFICATIVI SOCI E GARANTI", [
    voce("Documento di riconoscimento in corso di validit&agrave; di ogni Socio", "Carta d&rsquo;identit&agrave; o patente di guida"),
    voce("Ultime dichiarazioni dei redditi di ogni Socio", "Mod. UNICO 2025 con ricevuta, Mod. 730/2025 o CU"),
    voce("E-mail personale del Titolare / Soci / Garanti"),
    voce("Numero di cellulare del Titolare / Soci / Garanti", "Necessario per firma digitale a distanza e identificazione tramite SPID"),
])
s_bilanci = sezione("3", "BILANCI E DICHIARAZIONI FISCALI", [
    voce("Modello UNICO Societ&agrave; 2024 completo di quadro IVA/IRAP e ricevuta"),
    voce("Modello UNICO Societ&agrave; 2025 completo di quadro IVA/IRAP e ricevuta"),
    voce("Bilancio 2024 con nota integrativa, verbale approvazione e ricevuta di deposito"),
    voce("Bilancio 2025 con nota integrativa, verbale approvazione e ricevuta di deposito"),
    voce("Bilancio Analitico 2023"),
    voce("Bilancio Analitico 2024"),
    voce("Bilancio Analitico 2025"),
    voce("Bilancio provvisorio aggiornato a data recente"),
])

html_soc = pagina(
    "DOCUMENTAZIONE PER PRATICA DI AFFIDAMENTO BANCARIO",
    "SOCIET&Agrave;",
    "da consegnare a Quantum prima dell&rsquo;avvio della pratica",
    [s_societari, s_identificativi_soc, s_bilanci, s_finanziaria],
    [opz_investimento, opz_mutuo, opz_fideiussione, opz_simest],
    "SOCIET&Agrave;"
)

base = r"e:\Lavori Code\QUANTUM\Servizi\Affidamenti_Bancari\Proposta_Miglioramento"
with open(base + r"\Checklist_DittaIndividuale.html", "w", encoding="utf-8") as f:
    f.write(html_di)
with open(base + r"\Checklist_Societa.html", "w", encoding="utf-8") as f:
    f.write(html_soc)
print("OK — due file creati")
