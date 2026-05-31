"""
Genera le 3 copertine social per Quantum S.r.l.
- LinkedIn: 1128x191px
- Facebook: 1920x711px
- YouTube: 2560x1440px
"""

from PIL import Image, ImageDraw, ImageFont
import os

BLU = (26, 58, 110)
ORO = (201, 169, 110)
BIANCO = (255, 255, 255)

LOGO_SCRITTA = r"QUANTUM\Marketing\Materiale_Grafico\logo quantum scritta.png"
LOGO_ICONA   = r"QUANTUM\Marketing\Materiale_Grafico\logo quantum logo.png"
OUT_DIR      = r"QUANTUM\Marketing\Materiale_Grafico\Copertine_Social"

os.makedirs(OUT_DIR, exist_ok=True)

def fit_font(draw, text, font_path, max_w, start_size):
    size = start_size
    while size > 8:
        try:
            f = ImageFont.truetype(font_path, size)
        except:
            f = ImageFont.load_default()
            return f
        bb = draw.textbbox((0, 0), text, font=f)
        if (bb[2] - bb[0]) <= max_w:
            return f
        size -= 2
    return f

def crea_copertina(larghezza, altezza, nome_file, riga1, riga2, logo_h):
    img = Image.new("RGB", (larghezza, altezza), BLU)
    draw = ImageDraw.Draw(img)

    # Bordi oro
    draw.rectangle([(0, 0), (larghezza, 3)], fill=ORO)
    draw.rectangle([(0, altezza - 4), (larghezza, altezza)], fill=ORO)

    margin_x = int(larghezza * 0.05)

    # Icona
    icona = Image.open(LOGO_ICONA).convert("RGBA")
    ratio = logo_h / icona.height
    icona_w = int(icona.width * ratio)
    icona = icona.resize((icona_w, logo_h), Image.LANCZOS)
    margin_y = (altezza - logo_h) // 2
    img.paste(icona, (margin_x, margin_y), icona)

    # Scritta QUANTUM
    scritta = Image.open(LOGO_SCRITTA).convert("RGBA")
    scritta_h = int(logo_h * 0.50)
    scritta_w = int(scritta.width * scritta_h / scritta.height)
    scritta = scritta.resize((scritta_w, scritta_h), Image.LANCZOS)
    scritta_x = margin_x + icona_w + int(larghezza * 0.015)
    scritta_y = margin_y + (logo_h - scritta_h) // 2
    img.paste(scritta, (scritta_x, scritta_y), scritta)

    # Separatore verticale al 50%
    sep_x = int(larghezza * 0.50)
    draw.rectangle([(sep_x, altezza // 5), (sep_x + 2, altezza * 4 // 5)], fill=ORO)

    # Area testo: dalla sep_x+3% al 97% larghezza
    text_x = sep_x + int(larghezza * 0.03)
    max_text_w = int(larghezza * 0.97) - text_x

    font_path_b = "C:/Windows/Fonts/georgiab.ttf"
    font_path_r = "C:/Windows/Fonts/georgia.ttf"

    start1 = int(altezza * 0.18)
    start2 = int(altezza * 0.12)

    f1 = fit_font(draw, riga1, font_path_b, max_text_w, start1)
    f2 = fit_font(draw, riga2, font_path_r, max_text_w, start2)

    bb1 = draw.textbbox((0, 0), riga1, font=f1)
    h1 = bb1[3] - bb1[1]
    bb2 = draw.textbbox((0, 0), riga2, font=f2)
    h2 = bb2[3] - bb2[1]
    gap = int(altezza * 0.04)
    total_h = h1 + gap + h2
    start_y = (altezza - total_h) // 2

    draw.text((text_x, start_y), riga1, font=f1, fill=ORO)
    draw.text((text_x, start_y + h1 + gap), riga2, font=f2, fill=BIANCO)

    out_path = os.path.join(OUT_DIR, nome_file)
    img.save(out_path, quality=95)
    print(f"Salvato: {out_path} ({larghezza}x{altezza})")

R1 = "L'Advisor che affianca le imprese"
R2 = "Finanza  ·  Strategia  ·  Crescita"

crea_copertina(1128, 191,  "quantum_linkedin_cover.jpg",  R1, R2, logo_h=90)
crea_copertina(1920, 711,  "quantum_facebook_cover.jpg",  R1, R2, logo_h=200)
crea_copertina(2560, 1440, "quantum_youtube_banner.jpg",  R1, R2, logo_h=340)

print("\nDone.")
