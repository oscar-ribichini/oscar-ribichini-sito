from reportlab.lib.pagesizes import A4
from reportlab.lib import colors
from reportlab.lib.units import cm
from reportlab.lib.styles import ParagraphStyle
from reportlab.lib.enums import TA_LEFT, TA_CENTER, TA_RIGHT
from reportlab.platypus import (
    SimpleDocTemplate, Paragraph, Spacer, Table, TableStyle,
    HRFlowable, KeepTogether
)
from reportlab.pdfbase import pdfmetrics
from reportlab.pdfbase.ttfonts import TTFont
import os

OUTPUT = r"e:\Lavori Code\QUANTUM\Marketing\Presentazioni\2026-05-06_Fonti-Acqua-Italiane_Opportunita-Investimento.pdf"

# Colori
VERDE = colors.HexColor("#1a4a2e")
VERDE_LIGHT = colors.HexColor("#f0f4f0")
VERDE_MED = colors.HexColor("#4a7a5e")
ROSSO = colors.HexColor("#8b0000")
ROSSO_LIGHT = colors.HexColor("#fff3f3")
GRIGIO = colors.HexColor("#555555")
GRIGIO_LIGHT = colors.HexColor("#fafafa")
GRIGIO_BORDER = colors.HexColor("#cccccc")
BIANCO = colors.white

W, H = A4

def build_styles():
    return {
        "nome": ParagraphStyle("nome", fontName="Helvetica-Bold", fontSize=18,
                               textColor=VERDE, leading=22),
        "ruolo": ParagraphStyle("ruolo", fontName="Helvetica-Oblique", fontSize=9,
                                textColor=GRIGIO, leading=13),
        "contatti": ParagraphStyle("contatti", fontName="Helvetica", fontSize=8,
                                   textColor=colors.HexColor("#444444"),
                                   leading=13, alignment=TA_RIGHT),
        "doc_titolo": ParagraphStyle("doc_titolo", fontName="Helvetica-Bold", fontSize=14,
                                     textColor=VERDE, alignment=TA_CENTER, leading=18,
                                     spaceAfter=4),
        "doc_sub": ParagraphStyle("doc_sub", fontName="Helvetica-Oblique", fontSize=9,
                                  textColor=GRIGIO, alignment=TA_CENTER, leading=13,
                                  spaceAfter=14),
        "section": ParagraphStyle("section", fontName="Helvetica-Bold", fontSize=10,
                                  textColor=BIANCO, leading=14),
        "card_num": ParagraphStyle("card_num", fontName="Helvetica-Bold", fontSize=10,
                                   textColor=VERDE, leading=14),
        "card_price": ParagraphStyle("card_price", fontName="Helvetica-Bold", fontSize=9,
                                     textColor=ROSSO, leading=12),
        "card_price_nd": ParagraphStyle("card_price_nd", fontName="Helvetica", fontSize=9,
                                        textColor=GRIGIO, leading=12),
        "label": ParagraphStyle("label", fontName="Helvetica-Bold", fontSize=8,
                                textColor=colors.HexColor("#444444"), leading=12),
        "value": ParagraphStyle("value", fontName="Helvetica", fontSize=8,
                                textColor=colors.HexColor("#222222"), leading=12),
        "note": ParagraphStyle("note", fontName="Helvetica-Oblique", fontSize=7.5,
                               textColor=colors.HexColor("#333333"), leading=11),
        "kpi_val": ParagraphStyle("kpi_val", fontName="Helvetica-Bold", fontSize=10,
                                  textColor=VERDE, alignment=TA_CENTER, leading=13),
        "kpi_label": ParagraphStyle("kpi_label", fontName="Helvetica", fontSize=7,
                                    textColor=GRIGIO, alignment=TA_CENTER, leading=10),
        "tag": ParagraphStyle("tag", fontName="Helvetica-Bold", fontSize=7,
                              textColor=BIANCO, leading=10),
        "h3": ParagraphStyle("h3", fontName="Helvetica-Bold", fontSize=11,
                             textColor=VERDE, leading=14),
        "footer": ParagraphStyle("footer", fontName="Helvetica", fontSize=7.5,
                                 textColor=GRIGIO, alignment=TA_CENTER, leading=11),
    }

def section_bar(title, S):
    p = Paragraph(f"  {title}", S["section"])
    t = Table([[p]], colWidths=[W - 4*cm])
    t.setStyle(TableStyle([
        ("BACKGROUND", (0,0), (-1,-1), VERDE),
        ("TOPPADDING", (0,0), (-1,-1), 5),
        ("BOTTOMPADDING", (0,0), (-1,-1), 5),
        ("LEFTPADDING", (0,0), (-1,-1), 8),
    ]))
    return t

def card(numero, zona, prezzo_str, is_nd, rows, nota, S):
    num_p = Paragraph(f"{numero} – {zona}", S["card_num"])
    pr_style = S["card_price_nd"] if is_nd else S["card_price"]
    pr_p = Paragraph(prezzo_str, pr_style)
    header = Table([[num_p, pr_p]],
                   colWidths=[(W-4*cm)*0.62, (W-4*cm)*0.38])
    header.setStyle(TableStyle([
        ("VALIGN", (0,0), (-1,-1), "BOTTOM"),
        ("ALIGN", (1,0), (1,0), "RIGHT"),
        ("BOTTOMPADDING", (0,0), (-1,-1), 4),
    ]))

    info_data = [[Paragraph(l, S["label"]), Paragraph(v, S["value"])]
                 for l, v in rows]
    info_t = Table(info_data, colWidths=[(W-4*cm)*0.36, (W-4*cm)*0.64])
    info_t.setStyle(TableStyle([
        ("TOPPADDING", (0,0), (-1,-1), 2),
        ("BOTTOMPADDING", (0,0), (-1,-1), 2),
        ("VALIGN", (0,0), (-1,-1), "TOP"),
    ]))

    inner = [header, info_t]
    if nota:
        note_p = Paragraph(nota, S["note"])
        note_t = Table([[note_p]], colWidths=[W-4*cm - 16])
        note_t.setStyle(TableStyle([
            ("BACKGROUND", (0,0), (-1,-1), VERDE_LIGHT),
            ("LEFTPADDING", (0,0), (-1,-1), 6),
            ("RIGHTPADDING", (0,0), (-1,-1), 6),
            ("TOPPADDING", (0,0), (-1,-1), 4),
            ("BOTTOMPADDING", (0,0), (-1,-1), 4),
            ("LINEAFTER", (0,0), (0,-1), 1.5, VERDE_MED),
        ]))
        inner.append(Spacer(1, 4))
        inner.append(note_t)

    outer_data = [[item] for item in inner]
    # flatten into single cell
    from reportlab.platypus import KeepTogether
    body_t = Table([[inner[i]] for i in range(len(inner))],
                   colWidths=[W - 4*cm - 16])
    body_t.setStyle(TableStyle([
        ("TOPPADDING", (0,0), (-1,-1), 0),
        ("BOTTOMPADDING", (0,0), (-1,-1), 0),
    ]))

    wrapper = Table([[body_t]], colWidths=[W - 4*cm])
    wrapper.setStyle(TableStyle([
        ("BOX", (0,0), (-1,-1), 0.5, GRIGIO_BORDER),
        ("LINEBEFORE", (0,0), (0,-1), 2.5, VERDE),
        ("BACKGROUND", (0,0), (-1,-1), GRIGIO_LIGHT),
        ("LEFTPADDING", (0,0), (-1,-1), 8),
        ("RIGHTPADDING", (0,0), (-1,-1), 8),
        ("TOPPADDING", (0,0), (-1,-1), 8),
        ("BOTTOMPADDING", (0,0), (-1,-1), 8),
    ]))
    return KeepTogether([wrapper, Spacer(1, 6)])

def card_premium(titolo, prezzo_str, tags, kpi_data, rows, nota, S):
    h3 = Paragraph(titolo, S["h3"])
    pr = Paragraph(prezzo_str, ParagraphStyle("pb", fontName="Helvetica-Bold",
                   fontSize=13, textColor=ROSSO, leading=16, alignment=TA_RIGHT))
    inner_w = W - 4*cm - 24
    header = Table([[h3, pr]], colWidths=[inner_w*0.55, inner_w*0.45])
    header.setStyle(TableStyle([
        ("VALIGN", (0,0), (-1,-1), "BOTTOM"),
        ("BOTTOMPADDING", (0,0), (-1,-1), 4),
    ]))

    # Tags
    tag_cells = []
    for tag in tags:
        tp = Paragraph(f" {tag} ", S["tag"])
        tc = Table([[tp]])
        tc.setStyle(TableStyle([
            ("BACKGROUND", (0,0), (-1,-1), VERDE),
            ("TOPPADDING", (0,0), (-1,-1), 1),
            ("BOTTOMPADDING", (0,0), (-1,-1), 1),
            ("LEFTPADDING", (0,0), (-1,-1), 4),
            ("RIGHTPADDING", (0,0), (-1,-1), 4),
        ]))
        tag_cells.append(tc)
    tag_spacers = []
    for tc in tag_cells:
        tag_spacers.append(tc)
        tag_spacers.append(Spacer(4, 1))
    tag_row = Table([tag_cells], colWidths=[(W-4*cm-16)/len(tags)]*len(tags))
    tag_row.setStyle(TableStyle([
        ("TOPPADDING", (0,0), (-1,-1), 0),
        ("BOTTOMPADDING", (0,0), (-1,-1), 4),
        ("LEFTPADDING", (0,0), (-1,-1), 2),
        ("RIGHTPADDING", (0,0), (-1,-1), 2),
    ]))

    # KPI
    kpi_items = []
    for val, lbl in kpi_data:
        kpi_items.append([Paragraph(val, S["kpi_val"]), Paragraph(lbl, S["kpi_label"])])
    kpi_table_data = [[Table([[kv], [kl]], colWidths=[(W-4*cm-16)/len(kpi_data) - 8])
                       for kv, kl in kpi_items]]

    def make_kpi_box(val, lbl):
        inner = Table([[Paragraph(val, S["kpi_val"])],
                       [Paragraph(lbl, S["kpi_label"])]],
                      colWidths=[(W-4*cm-16)/len(kpi_data) - 10])
        inner.setStyle(TableStyle([
            ("ALIGN", (0,0), (-1,-1), "CENTER"),
            ("TOPPADDING", (0,0), (-1,-1), 3),
            ("BOTTOMPADDING", (0,0), (-1,-1), 3),
        ]))
        box = Table([[inner]])
        box.setStyle(TableStyle([
            ("BOX", (0,0), (-1,-1), 0.5, VERDE_MED),
            ("BACKGROUND", (0,0), (-1,-1), VERDE_LIGHT),
            ("TOPPADDING", (0,0), (-1,-1), 0),
            ("BOTTOMPADDING", (0,0), (-1,-1), 0),
            ("LEFTPADDING", (0,0), (-1,-1), 0),
            ("RIGHTPADDING", (0,0), (-1,-1), 0),
        ]))
        return box

    kpi_boxes = [make_kpi_box(v, l) for v, l in kpi_data]
    if kpi_boxes:
        col_w = (W - 4*cm - 16 - (len(kpi_boxes)-1)*4) / len(kpi_boxes)
        kpi_row = Table([kpi_boxes], colWidths=[col_w]*len(kpi_boxes),
                        spaceBefore=6, spaceAfter=6)
        kpi_row.setStyle(TableStyle([
            ("LEFTPADDING", (0,0), (-1,-1), 2),
            ("RIGHTPADDING", (0,0), (-1,-1), 2),
        ]))
    else:
        kpi_row = None

    info_data = [[Paragraph(l, S["label"]), Paragraph(v, S["value"])]
                 for l, v in rows]
    info_t = Table(info_data, colWidths=[(W-4*cm-16)*0.32, (W-4*cm-16)*0.68])
    info_t.setStyle(TableStyle([
        ("TOPPADDING", (0,0), (-1,-1), 2),
        ("BOTTOMPADDING", (0,0), (-1,-1), 2),
        ("VALIGN", (0,0), (-1,-1), "TOP"),
    ]))

    inner_elements = [header, Spacer(1, 4), tag_row]
    if kpi_data and kpi_row:
        inner_elements += [Spacer(1, 4), kpi_row]
    inner_elements += [Spacer(1, 4), info_t]
    if nota:
        note_p = Paragraph(nota, S["note"])
        note_t = Table([[note_p]], colWidths=[W-4*cm-28])
        note_t.setStyle(TableStyle([
            ("BACKGROUND", (0,0), (-1,-1), VERDE_LIGHT),
            ("LEFTPADDING", (0,0), (-1,-1), 6),
            ("RIGHTPADDING", (0,0), (-1,-1), 6),
            ("TOPPADDING", (0,0), (-1,-1), 4),
            ("BOTTOMPADDING", (0,0), (-1,-1), 4),
            ("LINEBEFORE", (0,0), (0,-1), 1.5, VERDE_MED),
        ]))
        inner_elements += [Spacer(1, 6), note_t]

    body_t = Table([[e] for e in inner_elements], colWidths=[W-4*cm-24])
    body_t.setStyle(TableStyle([
        ("TOPPADDING", (0,0), (-1,-1), 0),
        ("BOTTOMPADDING", (0,0), (-1,-1), 0),
    ]))

    wrapper = Table([[body_t]], colWidths=[W - 4*cm])
    wrapper.setStyle(TableStyle([
        ("BOX", (0,0), (-1,-1), 1, VERDE),
        ("LINEABOVE", (0,0), (-1,0), 4, VERDE),
        ("BACKGROUND", (0,0), (-1,-1), BIANCO),
        ("LEFTPADDING", (0,0), (-1,-1), 12),
        ("RIGHTPADDING", (0,0), (-1,-1), 12),
        ("TOPPADDING", (0,0), (-1,-1), 10),
        ("BOTTOMPADDING", (0,0), (-1,-1), 10),
    ]))
    return KeepTogether([wrapper, Spacer(1, 8)])

class FooterCanvas:
    def __init__(self, *args, **kwargs):
        pass

from reportlab.platypus.doctemplate import PageTemplate, BaseDocTemplate
from reportlab.platypus.frames import Frame
from reportlab.lib.units import cm

class MyDoc(BaseDocTemplate):
    def __init__(self, filename, **kwargs):
        super().__init__(filename, **kwargs)
        frame = Frame(2*cm, 2.5*cm, W - 4*cm, H - 4.5*cm, id="main")
        template = PageTemplate(id="main", frames=frame,
                                onPage=self._draw_footer)
        self.addPageTemplates([template])

    def _draw_footer(self, canvas, doc):
        canvas.saveState()
        canvas.setFont("Helvetica", 7.5)
        canvas.setFillColor(GRIGIO)
        footer_text = ("Oscar Ribichini  –  Via Fontanella 20, 62012 Civitanova Marche (MC)"
                       "  –  P.IVA 01785850437  –  +39 327 611 3167"
                       "  –  globalarea@gmail.com")
        canvas.drawCentredString(W/2, 1.8*cm, footer_text)
        canvas.setStrokeColor(GRIGIO_BORDER)
        canvas.setLineWidth(0.5)
        canvas.line(2*cm, 2.1*cm, W - 2*cm, 2.1*cm)
        canvas.drawRightString(W - 2*cm, 1.8*cm, f"{doc.page}")
        canvas.restoreState()

def build_doc():
    S = build_styles()
    doc = MyDoc(OUTPUT, pagesize=A4, leftMargin=2*cm, rightMargin=2*cm,
                topMargin=2*cm, bottomMargin=2.8*cm)

    story = []

    # INTESTAZIONE
    nome = Paragraph("Oscar Ribichini", S["nome"])
    ruolo = Paragraph("Consulente Indipendente &ndash; Finanza Straordinaria e Consulenza Aziendale", S["ruolo"])
    contatti = Paragraph(
        "Via Fontanella 20 &ndash; 62012 Civitanova Marche (MC)<br/>"
        "P.IVA 01785850437 &ndash; C.F. RBCSCR68M08E783U<br/>"
        "+39 327 611 3167 &ndash; globalarea@gmail.com",
        S["contatti"])

    header_t = Table([[Table([[nome], [ruolo]],
                              colWidths=[(W-4*cm)*0.6]),
                       contatti]],
                     colWidths=[(W-4*cm)*0.6, (W-4*cm)*0.4])
    header_t.setStyle(TableStyle([
        ("VALIGN", (0,0), (-1,-1), "BOTTOM"),
        ("ALIGN", (1,0), (1,0), "RIGHT"),
    ]))
    story.append(header_t)
    story.append(HRFlowable(width="100%", thickness=2, color=VERDE, spaceAfter=10))

    # TITOLO
    story.append(Paragraph("Fonti d’Acqua Italiane – Opportunità di Investimento", S["doc_titolo"]))
    story.append(Paragraph("Panoramica delle opportunità disponibili – Aggiornamento gennaio/febbraio 2026", S["doc_sub"]))

    # --- SEZIONE FERME ---
    story.append(section_bar("STABILIMENTI FERMI E FONTI DA RIAVVIARE", S))
    story.append(Spacer(1, 8))

    opportunita = [
        ("Opportunità 1", "Nord Italia", "Prezzo: da definire", True,
         [("Tipo sorgente", "Acqua sorgiva oligominerale alcalina"),
          ("Portata", "6 litri/sec"),
          ("Impianti esistenti", "Impianto del 2008 mai utilizzato per boccioni PET (5, 10, 12 litri)"),
          ("Area", "~50.000 mq edificabili – capannone ~1.300 mq"),
          ("Stato", "Stabilimento fermo")], None),

        ("Opportunità 2", "Nord Italia", "Prezzo: da definire", True,
         [("Tipo sorgente", "Pozzo artesiano oligominerale"),
          ("Portata", "20 litri/sec"),
          ("Impianti esistenti", "Nessuno"),
          ("Area", "~7.000 mq in area industriale"),
          ("Stato", "Concessione regionale attiva fino al 2047")], None),

        ("Opportunità 3", "Nord Italia", "Prezzo: da definire", True,
         [("Tipo sorgente", "Acqua sorgiva"),
          ("Impianti esistenti", "Nessuno"),
          ("Area", "~10.000 mq in area industriale"),
          ("Stato", "Progetto birrificio 250.000 hl/anno con filiera agricola friulana")], None),

        ("Opportunità 4", "Nord Italia", "~€ 1.200.000", False,
         [("Tipo sorgente", "Acqua sorgiva minerale"),
          ("Portata", "7 litri/sec (2 sorgenti)"),
          ("Impianti esistenti", "Nessuno"),
          ("Stato", "Stabilimento fermo. Include parco termale e albergo 80 camere (chiusi post-COVID)")],
         "Acquisto dal curatore fallimentare. Manifestando interesse si evita l’asta."),

        ("Opportunità 5", "Nord Italia", "Prezzo: da definire con proprietà", True,
         [("Tipo sorgente", "Pozzo artesiano oligominerale"),
          ("Portata", "2 litri/sec (possibilità ulteriore acqua minerale nelle vicinanze)"),
          ("Impianti esistenti", "Linea vetro a rendere e a perdere, ~10.000 bph (necessita manutenzione)"),
          ("Stato", "Stabilimento in funzione")],
         "Investimento stimato ~€ 1.000.000 per manutenzione e nuove macchine. Società con ~€ 1.000.000 di debiti (di cui € 500.000 mutuo)."),

        ("Opportunità 6", "Nord Italia", "€ 7.000.000", False,
         [("Tipo sorgente", "Acqua sorgiva oligominerale minimamente mineralizzata"),
          ("Portata", "68 litri/sec (3 sorgenti)"),
          ("Impianti esistenti", "Birrificio artigianale (cotte 20 hl) + impianto PET 14.000 b/h (mancano palettizzatore e fasciatore)"),
          ("Stato", "Funzionante solo per birra")],
         "Stabilimento ristrutturato da zero. Disponibilità a cedere quote societarie (totale o maggioranza). Alcune trattative in corso."),

        ("Opportunità 7", "Centro Italia", "€ 2.500.000", False,
         [("Tipo sorgente", "Pozzi artesiani medio minerale"),
          ("Portata totale", "~9 l/s (5 fonti, pH 7,5–9,0) + 2 pozzi acqua industriale"),
          ("Impianti esistenti", "Nessuno"),
          ("Area", "21.000 mq totali, di cui 13.000 mq coperti. Alcune utilities presenti."),
          ("Stato", "Fermo da ~6 anni. In funzione produceva 180 milioni bottiglie/anno")], None),

        ("Opportunità 8", "Centro Italia", "~€ 200.000.000", False,
         [("Tipo sorgente", "Multiple sorgenti con buona portata"),
          ("Stabilimenti", "3 stabilimenti funzionanti"),
          ("Produzione", "Acqua minerale e bibite in PET e vetro"),
          ("Stato", "Operativi")],
         "La società venditrice non rilascia informazioni senza manifestazione di interesse formale."),

        ("Opportunità 9", "Centro Italia", "Base d’asta ~€ 600.000", False,
         [("Tipo sorgente", "Pozzi artesiani"),
          ("Portata", "10 l/s in concessione attiva fino al 2054 + altri 10 l/s da richiedere"),
          ("Impianti esistenti", "Nessuno"),
          ("Area", "Capannone 3.000 mq di recente costruzione"),
          ("Stato", "Chiuso da ~12 anni, senza impianti")],
         "Acquisto da Tribunale di Forlì. Prima dell’asta è possibile presentare offerta al curatore a cifra inferiore alla base d’asta."),

        ("Opportunità 10", "Centro Italia", "~€ 500.000 trattabili", False,
         [("Tipo sorgente", "Pozzo artesiano oligominerale alcalina"),
          ("Portata", "2 l/s + possibilità ulteriori 16 l/s"),
          ("Impianti esistenti", "Nessuno"),
          ("Stato", "Stabilimento chiuso in pessimo stato")], None),

        ("Opportunità 11", "Centro Italia", "€ 8.000.000", False,
         [("Tipo sorgente", "Acqua sorgiva oligominerale"),
          ("Portata", "25 litri/sec (1 sorgente)"),
          ("Impianti esistenti", "Nessuno"),
          ("Area", "22.000 mq coperti (comprese baie di carico) + 100.000 mq scoperti"),
          ("Stato", "Stabilimento fermo. Posizione logistica molto favorevole.")],
         "Acquistato dal tribunale per fallimento precedente proprietà. Proprietà disponibile a co-investire. Procedura concessione mineraria già avviata."),

        ("Opportunità 12", "Centro Italia (Lazio)", "~€ 1.500.000", False,
         [("Tipo sorgente", "Pozzo artesiano oligominerale alcalina"),
          ("Portata", "10 litri/sec"),
          ("Concessione mineraria", "Attiva fino al 2037 (Regione Lazio)"),
          ("Impianti esistenti", "Nessuno – terreni ~20.000 mq per costruzione stabilimento")],
         "Prezzo comprende: società con cap. soc. € 810.000, terreni, costi documentabili, concessione ventennale, titolo Acqua Minerale (idonea neonati) da Ministero della Salute, accordo con Comune per iter concessorio. Possibilità agevolazioni fiscali post-terremoto."),

        ("Opportunità 13", "Sud Italia", "Prezzo: da definire", True,
         [("Tipo sorgente", "Acqua sorgiva oligominerale"),
          ("Portata", "6,5 litri/sec (1 sorgente)"),
          ("Impianti esistenti", "Nessuno"),
          ("Stato", "Stabilimento da realizzare – concessione mineraria da richiedere")], None),

        ("Opportunità 14", "Sud Italia", "Prezzo: da definire", True,
         [("Tipo sorgente", "Pozzo artesiano oligominerale"),
          ("Portata", "~4 litri/sec (da verificare)"),
          ("Impianti esistenti", "Nessuno"),
          ("Stato", "Concessione mineraria in scadenza, già rilasciata per 20 anni e pagata da 19 anni")], None),

        ("Opportunità 15", "Lazio (quota 450 m)", "Prezzo: da definire", True,
         [("Classificazione", "Acqua Minerale Naturale Oligominerale Iposodica"),
          ("Impianti esistenti", "Presenti, da aggiornare e pulire"),
          ("Residuo fisso", "179 mg/l – pH 6,34 – T 13,5°C"),
          ("Composizione", "Ca 26,43 – Mg 11,17 – Na 6,6 – K 7 – Bicarbonato 122 – Cl 21,27 (mg/l)"),
          ("Stato", "Stabilimento abbandonato ma con impianti")], None),

        ("Opportunità 16", "Parma", "Prezzo: da definire", True,
         [("Sorgenti", "4 sorgenti"),
          ("Impianti esistenti", "Stabilimento presente, mancano gli impianti"),
          ("Stato", "Marchi già conosciuti sul mercato")], None),

        ("Opportunità 17", "Provincia di Latina", "€ 2.500.000", False,
         [("Classificazione", "Acqua medio minerale, bicarbonato-calcica magnesiaca, leggermente acidula"),
          ("Portata", "4 l/s (prima sorgente) + possibilità 6 pozzi aggiuntivi"),
          ("Impianti esistenti", "Impianto imbottigliamento in vetro funzionante"),
          ("Area", "900 mq coperti + 2.000 mq scoperti + 20.000 mq proprietà + 22.000 mq locazione (fino al 2038)"),
          ("Concessione", "Rinnovata 2007 per 25 anni (rinnovabili)"),
          ("Ubicazione", "20 min da A1 Cassino/Capua – 5 min dalla Via Appia")],
         "Già in portafoglio richieste contrattuali da operatori nei Paesi Arabi (private label, trasporto via nave). Analisi certificate Università Federico II Napoli. Per approfondimenti richiesta LOI su carta intestata."),

        ("Opportunità 18", "Lazio", "Prezzo: da definire", True,
         [("Classificazione", "Acqua Minerale Naturale Medio Minerale Iposodica"),
          ("Impianti esistenti", "Capannone e impianto presenti, da aggiornare"),
          ("Residuo fisso", "525 mg/l – pH 7,03"),
          ("Composizione", "Ca 132,13 – Mg 45,16 – Na 4 – K 2 – Bicarbonato 573,4 – Solfato 42,8 (mg/l)"),
          ("Stato", "Pronta da far ripartire")], None),
    ]

    for num, zona, prezzo, nd, rows, nota in opportunita:
        story.append(card(num, zona, prezzo, nd, rows, nota, S))

    # --- SEZIONE ATTIVE ---
    story.append(Spacer(1, 6))
    story.append(section_bar("AZIENDE ATTIVE – OPPORTUNITÀ DI ACQUISIZIONE", S))
    story.append(Spacer(1, 10))

    story.append(card_premium(
        "Azienda Leader Beverage – Alta Italia (attiva dal 1955)",
        "€ 26.000.000",
        ["Acqua minerale", "Bevande analcoliche", "Low-alcohol <10°",
         "Contract filling", "Private label", "Export 30+ anni"],
        [("€ 11,3 mln", "Ricavi 2022 (+40%)"),
         ("€ 1,6 mln", "EBITDA 2022 (+25%)"),
         ("€ 1,0 mln", "Utile netto (+23%)"),
         ("€ 5,1 mln", "Patrimonio netto (+21%)")],
        [("Stabilimento", "10.000 mq coperti – 35.000 mq totali – contesto ambientale protetto"),
         ("Impianti", "Vetro e alluminio, formati 100 ml – 1 litro, gassate e lisce, soft drink e craft"),
         ("Co-packer autorizzato", "Diageo, Bacardi-Martini, Conserve Italia, primari retailer internazionali"),
         ("Mercati", "UE, USA/Canada, America Latina, Corea, Giappone, Australia, Emirati Arabi"),
         ("Certificazioni", "BRCGS, Biologico UE, USDA Organic, JAS Organic, Halal, Kosher, SEDEX")],
        "Trattativa riservata. Dossier completo disponibile previa manifestazione di interesse qualificata e sottoscrizione di NDA e fondo spese.",
        S))

    story.append(card_premium(
        "Acqua delle Colline Trevigiane – Monte Grappa",
        "€ 4.500.000",
        ["Oligominerale iposodica", "Sorgente carsica 50 m",
         "Soft drinks artigianali", "Acqua ossigenata"],
        [],
        [("Sorgente", "Fiume carsico a 50 m di profondità – falde del Monte Grappa"),
         ("Caratteristiche", "Residuo fisso 386 mg/l – Conducibilità 666 μS/cm – T 14,1°C – pH neutro"),
         ("Composizione", "Ca 92,2 – Mg 32,1 – Na 7,3 – K 1,4 – Cl 6,8 – Solfati 19,5 (mg/l)"),
         ("Analisi", "Università di Padova"),
         ("Gamme", "Naturale – Frizzante – Con ossigeno (+150 mg/l, 3000% vs acque comuni)"),
         ("Soft drinks", "Tonic, Aranciata, Chinotto, Cedrata, Pompelmo Rosa, Limonata, Gazzosa (100% naturali)")],
        None,
        S))

    doc.build(story)
    print(f"PDF generato: {OUTPUT}")

build_doc()
