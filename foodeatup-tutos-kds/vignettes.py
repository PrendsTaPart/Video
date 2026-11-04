#!/usr/bin/env python3
"""Vignettes 16:9 : fond Lovable (chef, sans texte) + vrai écran KDS + accroche + logo officiel."""
import json, os, sys
from PIL import Image, ImageDraw, ImageFont, ImageFilter
from tutos import T
ICI = os.path.dirname(os.path.abspath(__file__))
F = "/home/user/stockvisionai/resources/fonts/print/Manrope-Bold.ttf"
plan = json.load(open(os.path.join(ICI, "plan.json")))["videos"]
num = {v["slug"]: k + 1 for k, v in enumerate(plan)}
hook = {v["slug"]: v["vignette_hook"] for v in plan}
noms = {1: "01-appairer-et-regler", 2: "02-rythme-du-service", 3: "03-gestes-du-poste", 4: "04-ticket-en-grand", 5: "05-filtres-et-retards", 6: "06-vue-production", 7: "07-rappeler-un-ticket", 8: "08-le-pass", 9: "09-fiche-recette", 10: "10-epuise-du-jour", 11: "11-sons-du-poste", 12: "12-mode-ecole", 13: "13-vue-du-chef", 14: "14-hors-ligne"}
ecran_vignette = {"app-kds-appairer-et-regler": "02_pairing_code", "app-kds-mode-ecole": "54_ecole", "app-kds-le-pass": "60_pass", "app-kds-vue-du-chef": "61_chef"}
os.makedirs(os.path.join(ICI, "sortie"), exist_ok=True)

def lignes(d, txt, f, w):
    mots, out, cur = txt.split(), [], ""
    for m in mots:
        t = (cur + " " + m).strip()
        if d.textlength(t, font=f) <= w: cur = t
        else: out.append(cur); cur = m
    return out + [cur]

for v in T:
    n = num[v["cle"]]
    fond = Image.open(os.path.join(ICI, "fonds", noms[n] + ".webp")).convert("RGB")
    im = fond.copy(); d = ImageDraw.Draw(im)
    e = ecran_vignette.get(v["cle"], v["ecrans"][-1] if len(v["ecrans"]) < 3 else v["ecrans"][1])
    scr = Image.open(os.path.join(ICI, "ecrans", e + ".webp")).convert("RGB").resize((960, 600))
    cadre = Image.new("RGB", (1000, 640), "#05090D")
    cadre.paste(scr, (20, 20))
    masque = Image.new("L", cadre.size, 0); ImageDraw.Draw(masque).rounded_rectangle((0, 0, 999, 639), 34, fill=255)
    ombre = Image.new("RGBA", (1100, 740), (0, 0, 0, 0)); ImageDraw.Draw(ombre).rounded_rectangle((50, 60, 1050, 700), 34, fill=(0, 0, 0, 170))
    ombre = ombre.filter(ImageFilter.GaussianBlur(26))
    im.paste(ombre, (30, 330), ombre); im.paste(cadre, (80, 360), masque)
    # accroche surlignée
    fh = ImageFont.truetype(F, 86); y = 70
    for l in lignes(d, hook[v["cle"]], fh, 1150)[:2]:
        w = d.textlength(l, font=fh)
        d.rounded_rectangle((70, y - 6, 70 + w + 40, y + 104), 22, fill="#FFA500")
        d.text((90, y), l, font=fh, fill="#0F1A23"); y += 120
    # badge
    fb = ImageFont.truetype(F, 34)
    t = f"APPLICATION KDS · TUTO {n}/14"; wb = d.textlength(t, font=fb)
    d.rounded_rectangle((1880 - wb - 40, 36, 1880, 96), 30, fill="#007BFF"); d.text((1880 - wb - 20, 44), t, font=fb, fill="#FFFFFF")
    logo = Image.open(os.path.join(ICI, "commun", "logo.png")).convert("RGBA"); logo.thumbnail((300, 80))
    plaque = Image.new("RGBA", (logo.width + 40, logo.height + 24), (255, 255, 255, 255))
    pm = Image.new("L", plaque.size, 0); ImageDraw.Draw(pm).rounded_rectangle((0, 0, plaque.width - 1, plaque.height - 1), 18, fill=255)
    plaque.paste(logo, (20, 12), logo); im.paste(plaque, (1880 - plaque.width, 990 - plaque.height), pm)
    im.save(os.path.join(ICI, "sortie", v["cle"] + "-vignette.jpg"), quality=90)
    print(v["cle"], e)
