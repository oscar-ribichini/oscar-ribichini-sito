from reportlab.lib.pagesizes import mm
from reportlab.lib import colors
from reportlab.platypus import SimpleDocTemplate
from reportlab.pdfgen import canvas
from reportlab.lib.units import mm

OUTPUT = r"e:\Lavori Code\QUANTUM\Marketing\Materiale_Grafico\2026-05-07_Biglietto_Visita_Oscar.pdf"

# Dimensioni biglietto standard 85x55mm, 2 copie per pagina A4
W = 85 * mm
H = 55 * mm

BLU = colors.HexColor("#1a1a2e")
ORO = colors.HexColor("#c9a96e")
BIANCO = colors.white
GRIGIO = colors.HexColor("#888888")

def draw_biglietto(c, x, y):
    # Sfondo blu scuro intero
    c.setFillColor(BLU)
    c.rect(x, y, W, H, fill=1, stroke=0)

    # Banda oro in basso
    c.setFillColor(ORO)
    c.rect(x, y, W, 1.2*mm, fill=1, stroke=0)

    # Banda oro in alto
    c.rect(x, y + H - 1.2*mm, W, 1.2*mm, fill=1, stroke=0)

    # Bordo esterno oro sottile
    c.setStrokeColor(ORO)
    c.setLineWidth(0.5)
    c.rect(x + 2*mm, y + 2*mm, W - 4*mm, H - 4*mm, fill=0, stroke=1)

    # Nome grande
    c.setFillColor(BIANCO)
    c.setFont("Helvetica-Bold", 15)
    c.drawString(x + 5*mm, y + 37*mm, "OSCAR RIBICHINI")

    # Titolo in oro
    c.setFillColor(ORO)
    c.setFont("Helvetica", 8)
    c.drawString(x + 5*mm, y + 30*mm, "AI Consultant & Business Advisor")

    # Linea oro separatrice
    c.setStrokeColor(ORO)
    c.setLineWidth(0.4)
    c.line(x + 5*mm, y + 27*mm, x + W - 5*mm, y + 27*mm)

    # Telefono
    c.setFillColor(BIANCO)
    c.setFont("Helvetica", 8)
    c.drawString(x + 5*mm, y + 21*mm, "+39 327 611 3167")

    # Email
    c.setFont("Helvetica", 8)
    c.drawString(x + 5*mm, y + 15*mm, "globalarea@gmail.com")

    # Citta
    c.setFillColor(GRIGIO)
    c.setFont("Helvetica", 7)
    c.drawString(x + 5*mm, y + 9*mm, "Civitanova Marche (MC) - Italia")

def crea_pdf():
    c = canvas.Canvas(OUTPUT, pagesize=(210*mm, 297*mm))

    # 8 biglietti per pagina (2 colonne x 4 righe)
    margin_x = 15*mm
    margin_y = 20*mm
    gap_x = 10*mm
    gap_y = 10*mm

    for row in range(4):
        for col in range(2):
            x = margin_x + col * (W + gap_x)
            y = margin_y + row * (H + gap_y)
            draw_biglietto(c, x, y)

    c.save()
    print(f"PDF generato: {OUTPUT}")

crea_pdf()
