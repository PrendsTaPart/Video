#!/usr/bin/env python3
"""Dessine le bloc contact incrusté sur le carton de fin.

« Demander une démo », le numéro, et la pastille WhatsApp. Dessiné en vectoriel
plutôt que posé comme image : le numéro change en une ligne, et le rendu reste
net à 1080 px de large.
"""
import pathlib
from PIL import Image, ImageDraw, ImageFont

ROOT = pathlib.Path(__file__).resolve().parent.parent
POLICE = ROOT / "templates" / "Poppins-800.ttf"

NUMERO = "06 14 18 92 25"
ACCROCHE = "Demander une démo"

W, H = 1080, 300
ENCRE = (20, 32, 43, 255)
VERT = (37, 211, 102, 255)      # vert WhatsApp
BLANC = (255, 255, 255, 255)

img = Image.new("RGBA", (W, H), (0, 0, 0, 0))
d = ImageDraw.Draw(img)

f_accroche = ImageFont.truetype(str(POLICE), 52)
f_num = ImageFont.truetype(str(POLICE), 62)

# accroche centrée
a_w = d.textbbox((0, 0), ACCROCHE, font=f_accroche)[2]
d.text(((W - a_w) / 2, 0), ACCROCHE, font=f_accroche, fill=ENCRE)

# pastille verte : icône + numéro, dimensionnée sur le texte
n_w = d.textbbox((0, 0), NUMERO, font=f_num)[2]
ICONE = 76
ESPACE = 26
PAD_X, PAD_Y = 40, 26
pill_w = PAD_X * 2 + ICONE + ESPACE + n_w
pill_h = PAD_Y * 2 + ICONE
x0 = (W - pill_w) / 2
y0 = 108
d.rounded_rectangle([x0, y0, x0 + pill_w, y0 + pill_h], pill_h / 2, fill=VERT)

# combiné téléphone stylisé, dans une bulle — le repère WhatsApp
cx, cy = x0 + PAD_X + ICONE / 2, y0 + PAD_Y + ICONE / 2
r = ICONE / 2
d.ellipse([cx - r, cy - r, cx + r, cy + r], fill=BLANC)
d.polygon([(cx - r * 0.72, cy + r * 0.30), (cx - r * 0.30, cy + r * 0.72),
           (cx - r * 0.86, cy + r * 0.86)], fill=BLANC)
# le combiné, deux pavés reliés par une diagonale
d.rounded_rectangle([cx - r * 0.46, cy - r * 0.52, cx - r * 0.10, cy - r * 0.14],
                    6, fill=VERT)
d.rounded_rectangle([cx + r * 0.08, cy + r * 0.06, cx + r * 0.46, cy + r * 0.44],
                    6, fill=VERT)
d.line([(cx - r * 0.24, cy - r * 0.26), (cx + r * 0.24, cy + r * 0.20)],
       fill=VERT, width=13)

d.text((x0 + PAD_X + ICONE + ESPACE, y0 + PAD_Y + 2), NUMERO, font=f_num, fill=BLANC)

chemin = ROOT / "templates" / "cta-contact.png"
img.save(chemin)
print(f"{chemin.name}  {W}x{H}  numéro {NUMERO}")
