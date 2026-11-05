#!/usr/bin/env python3
"""Vignettes 16:9 communes : vrai écran de l'app dans son appareil + accroche surlignée + chef + logo officiel."""
import os
from PIL import Image, ImageDraw, ImageFont, ImageFilter

ICI = os.path.dirname(os.path.abspath(__file__))
F = "/home/user/stockvisionai/resources/fonts/print/Manrope-Bold.ttf"
LOGO = os.path.join(ICI, "..", "foodeatup-tutos-kds", "commun", "logo.png")
CHEFS = "/home/user/stockvisionai/public/images/illustrations/chef-video"

def _lignes(d, txt, f, w):
    mots, out, cur = txt.split(), [], ""
    for m in mots:
        t = (cur + " " + m).strip()
        if d.textlength(t, font=f) <= w: cur = t
        else: out.append(cur); cur = m
    return out + [cur]

def _fond():
    im = Image.new("RGB", (1920, 1080), "#0F1A23")
    halo = Image.new("RGB", (1920, 1080), "#0F1A23"); d = ImageDraw.Draw(halo)
    d.ellipse((1050, 80, 1950, 980), fill="#3a2a10"); d.ellipse((-300, 600, 700, 1400), fill="#0d2a4a")
    return Image.blend(im, halo.filter(ImageFilter.GaussianBlur(160)), 0.9)

def vignette(sortie, ecran, hook, badge, chef, appareil="telephone"):
    im = _fond(); d = ImageDraw.Draw(im)
    fh = ImageFont.truetype(F, 84); y = 150
    for l in _lignes(d, hook, fh, 860)[:3]:
        w = d.textlength(l, font=fh)
        d.rounded_rectangle((90, y - 6, 90 + w + 40, y + 104), 22, fill="#FFA500")
        d.text((110, y), l, font=fh, fill="#0F1A23"); y += 122
    fb = ImageFont.truetype(F, 34); wb = d.textlength(badge, font=fb)
    d.rounded_rectangle((90, 60, 90 + wb + 40, 120), 30, fill="#007BFF"); d.text((110, 68), badge, font=fb, fill="#FFFFFF")
    scr = Image.open(ecran).convert("RGB")
    if appareil == "telephone":
        sw, sh, bord, ray, x0, y0 = 450, 800, 16, 54, 1060, 140
    else:
        sw, sh, bord, ray, x0, y0 = 900, 560, 18, 30, 960, 260
    scr = scr.resize((sw, sh))
    cadre = Image.new("RGB", (sw + 2 * bord, sh + 2 * bord), "#05090D"); cadre.paste(scr, (bord, bord))
    m = Image.new("L", cadre.size, 0); ImageDraw.Draw(m).rounded_rectangle((0, 0, cadre.width - 1, cadre.height - 1), ray, fill=255)
    om = Image.new("RGBA", (cadre.width + 120, cadre.height + 120), (0, 0, 0, 0))
    ImageDraw.Draw(om).rounded_rectangle((60, 70, cadre.width + 60, cadre.height + 70), ray, fill=(0, 0, 0, 170))
    om = om.filter(ImageFilter.GaussianBlur(26)); im.paste(om, (x0 - 60, y0 - 60), om); im.paste(cadre, (x0, y0), m)
    c = Image.open(os.path.join(CHEFS, chef)).convert("RGB"); t = 330; c = c.resize((t, t))
    cm = Image.new("L", (t, t), 0); ImageDraw.Draw(cm).ellipse((0, 0, t - 1, t - 1), fill=255)
    rond = Image.new("RGB", (t + 20, t + 20), "#FFA500"); rm = Image.new("L", rond.size, 0); ImageDraw.Draw(rm).ellipse((0, 0, t + 19, t + 19), fill=255)
    cx, cy = (1530, 650) if appareil == "telephone" else (1560, 690)
    im.paste(rond, (cx, cy), rm); im.paste(c, (cx + 10, cy + 10), cm)
    logo = Image.open(LOGO).convert("RGBA"); logo.thumbnail((320, 86))
    pl = Image.new("RGBA", (logo.width + 44, logo.height + 28), (255, 255, 255, 255))
    pm = Image.new("L", pl.size, 0); ImageDraw.Draw(pm).rounded_rectangle((0, 0, pl.width - 1, pl.height - 1), 20, fill=255)
    pl.paste(logo, (22, 14), logo); im.paste(pl, (90, 1000 - pl.height), pm)
    im.save(sortie, quality=90)
