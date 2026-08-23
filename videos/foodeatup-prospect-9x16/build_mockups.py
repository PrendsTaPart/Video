#!/usr/bin/env python3
"""Mockups d'interface FoodEatUp (S2..S7) — rendus en séquences d'images puis en mp4.

Aucune donnée réelle : tout est écrit ici, donc aucun nom, e-mail ou téléphone
d'employé ne peut fuir dans la vidéo (cf. NOTES-CAPTURES.md).
"""
import os, sys, math, shutil, subprocess
from PIL import Image, ImageDraw
sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
from lib_draw import *

ROOT = os.path.dirname(os.path.abspath(__file__))
WORK = f"{ROOT}/work"
PLATS = "/home/user/Video/videos/shared-images/plats"
os.makedirs(WORK, exist_ok=True)

# ---------------------------------------------------------------- utilitaires

def encode(name, nframes):
    src = f"{WORK}/frames_{name}/f%05d.png"
    out = f"{WORK}/seq-{name}.mp4"
    subprocess.run(["ffmpeg", "-v", "error", "-y", "-framerate", str(FPS), "-i", src,
                    "-c:v", "libx264", "-preset", "medium", "-crf", "18",
                    "-pix_fmt", "yuv420p", "-r", str(FPS), out], check=True)
    print(f"  -> {out} ({nframes/FPS:.1f}s)")
    return out

def render(name, duration, draw_frame):
    d = f"{WORK}/frames_{name}"
    shutil.rmtree(d, ignore_errors=True); os.makedirs(d)
    n = int(round(duration * FPS))
    print(f"[{name}] {duration}s / {n} frames")
    for i in range(n):
        im = draw_frame(i / FPS)
        im.save(f"{d}/f{i:05d}.png")
    return encode(name, n)

def appear(t, t0, dur=0.55):
    """Facteur 0->1 avec rebond, et décalage vertical qui se résorbe."""
    p = ease_back((t - t0) / dur) if t >= t0 else 0.0
    return max(0.0, min(1.0, p))

def fade(t, t0, dur=0.4):
    return ease((t - t0) / dur) if t >= t0 else 0.0

def slide_card(im, box, r, fill, p, dy=70, shadow=True):
    """Dessine une carte qui monte en place selon p (0..1). Retourne la boîte réelle."""
    if p <= 0: return None
    off = int((1 - p) * dy)
    b = (box[0], box[1] + off, box[2], box[3] + off)
    if shadow: shadow_card(im, b, r=r, alpha=int(40 * p))
    d = ImageDraw.Draw(im)
    d.rounded_rectangle(b, r, fill=fill)
    return b

def title_pill(im, t, label, y=170, t0=0.2):
    p = appear(t, t0)
    if p <= 0: return
    d = ImageDraw.Draw(im)
    f = F("700", 46)
    tw = d.textlength(label, font=f)
    w_ = int(tw + 90); x0 = (W - w_) // 2; h_ = 92
    off = int((1 - p) * 40)
    d.rounded_rectangle((x0, y - off, x0 + w_, y + h_ - off), h_ // 2, fill=BLUE)
    d.text((W // 2, y + h_ // 2 - off), label, font=f, fill=WHITE, anchor="mm")

# ------------------------------------------------------------------- icônes

def ico_phone(d, cx, cy, s, col):
    d.rounded_rectangle((cx - s*0.30, cy - s*0.52, cx + s*0.30, cy + s*0.52), int(s*0.16), outline=col, width=int(s*0.11))
    d.line((cx - s*0.10, cy + s*0.34, cx + s*0.10, cy + s*0.34), fill=col, width=int(s*0.10))

def ico_kiosk(d, cx, cy, s, col):
    d.rounded_rectangle((cx - s*0.46, cy - s*0.52, cx + s*0.46, cy + s*0.18), int(s*0.12), outline=col, width=int(s*0.11))
    d.line((cx, cy + s*0.18, cx, cy + s*0.46), fill=col, width=int(s*0.11))
    d.line((cx - s*0.34, cy + s*0.50, cx + s*0.34, cy + s*0.50), fill=col, width=int(s*0.11))

def ico_web(d, cx, cy, s, col):
    r = s*0.48
    d.ellipse((cx - r, cy - r, cx + r, cy + r), outline=col, width=int(s*0.10))
    d.ellipse((cx - r*0.42, cy - r, cx + r*0.42, cy + r), outline=col, width=int(s*0.08))
    d.line((cx - r, cy, cx + r, cy), fill=col, width=int(s*0.08))

def ico_check(d, cx, cy, s, col, width=None):
    w = width or max(4, int(s*0.20))
    d.line((cx - s*0.42, cy + s*0.02, cx - s*0.08, cy + s*0.36), fill=col, width=w)
    d.line((cx - s*0.08, cy + s*0.36, cx + s*0.44, cy - s*0.36), fill=col, width=w)

def ico_alert(d, cx, cy, s, col):
    d.polygon([(cx, cy - s*0.50), (cx + s*0.54, cy + s*0.42), (cx - s*0.54, cy + s*0.42)], outline=col, width=int(s*0.11))
    d.line((cx, cy - s*0.16, cx, cy + s*0.14), fill=col, width=int(s*0.12))
    d.ellipse((cx - s*0.07, cy + s*0.24, cx + s*0.07, cy + s*0.38), fill=col)

# =========================================================== S2 — les 4 IA

IA4 = [("IA Commandes", "Téléphone · Borne · En ligne", ico_phone),
       ("IA Cuisine", "Stocks · DLC · Plannings · RH", ico_kiosk),
       ("IA Pilotage", "Vos réponses sur WhatsApp", ico_web),
       ("IA Réseaux", "De l'alerte à la campagne", ico_check)]

def s2_frame(t):
    im = canvas(CREAM); d = ImageDraw.Draw(im)
    dot_grid(d, 120, H - 120)
    p = appear(t, 0.6, 0.8)
    if p > 0:
        y = 300 - int((1 - p) * 60)
        logo(im, y, h=150)
    if t >= 2.2:
        f = F("800", 62); d2 = ImageDraw.Draw(im)
        a = fade(t, 2.2)
        col = tuple(int(CREAM[i] + (INK[i] - CREAM[i]) * a) for i in range(3))
        d2.text((W // 2, 520), "4 IA. 1 seul objectif :", font=f, fill=col, anchor="ma")
        col2 = tuple(int(CREAM[i] + (BLUE[i] - CREAM[i]) * a) for i in range(3))
        d2.text((W // 2, 600), "votre tranquillité.", font=F("800", 62), fill=col2, anchor="ma")
    # 4 cartes empilées
    for i, (titre, sous, ico) in enumerate(IA4):
        p = appear(t, 4.0 + i * 0.75, 0.6)
        if p <= 0: continue
        y0 = 780 + i * 235
        b = slide_card(im, (90, y0, W - 90, y0 + 195), 40, WHITE, p, dy=60)
        dd = ImageDraw.Draw(im)
        cx, cy = b[0] + 120, (b[1] + b[3]) // 2
        dd.ellipse((cx - 62, cy - 62, cx + 62, cy + 62), fill=(233, 242, 255))
        ico(dd, cx, cy, 86, BLUE)
        dd.text((b[0] + 230, b[1] + 48), titre, font=F("700", 54), fill=INK)
        dd.text((b[0] + 230, b[1] + 118), sous, font=F("400", 38), fill=GREY)
    return im

# =================================================== S3 — IA Commandes

TICKETS = [("#124", "2× Burger maison · Table 7", "Téléphone"),
           ("#125", "1× Poke bowl · À emporter", "Borne"),
           ("#126", "3× Pizza reine · Livraison", "En ligne"),
           ("#127", "2× Salade César · Table 3", "Téléphone")]

def s3_frame(t):
    im = canvas(CREAM); d = ImageDraw.Draw(im)
    dot_grid(d, 120, H - 120)
    title_pill(im, t, "IA Commandes")
    # 3 canaux
    labels = [("Téléphone", ico_phone), ("Borne", ico_kiosk), ("En ligne", ico_web)]
    xs = [180, W // 2, W - 180]
    for i, ((lab, ico), cx) in enumerate(zip(labels, xs)):
        p = appear(t, 1.0 + i * 0.5)
        if p <= 0: continue
        r = int(96 * p); cy = 470
        d.ellipse((cx - r, cy - r, cx + r, cy + r), fill=WHITE)
        if p > 0.5:
            ico(d, cx, cy - 8, 110, BLUE)
            d.text((cx, cy + 130), lab, font=F("600", 40), fill=INK, anchor="ma")
    # flux de points vers l'écran cuisine
    if t > 2.6:
        for i, cx in enumerate(xs):
            for k in range(4):
                ph = ((t - 2.6) * 0.55 + k * 0.25 + i * 0.11) % 1.0
                y = 700 + ph * 250
                x = cx + (W // 2 - cx) * ph
                a = 1 - abs(ph - 0.5) * 1.2
                if a > 0:
                    rr_ = 9
                    d.ellipse((x - rr_, y - rr_, x + rr_, y + rr_), fill=BLUE if i % 2 == 0 else ORANGE)
    # écran cuisine
    p = appear(t, 3.4, 0.7)
    if p > 0:
        b = slide_card(im, (80, 930, W - 80, 1650), 44, INK, p, dy=80)
        dd = ImageDraw.Draw(im)
        dd.text((b[0] + 46, b[1] + 40), "ÉCRAN CUISINE", font=F("700", 40), fill=(120, 200, 255))
        dd.line((b[0] + 46, b[1] + 110, b[2] - 46, b[1] + 110), fill=(40, 58, 74), width=3)
        for i, (num, lib, canal) in enumerate(TICKETS):
            tp = appear(t, 5.0 + i * 1.6, 0.45)
            if tp <= 0: continue
            y0 = b[1] + 145 + i * 148
            off = int((1 - tp) * 30)
            dd.rounded_rectangle((b[0] + 40, y0 + off, b[2] - 40, y0 + 128 + off), 24, fill=(28, 44, 58))
            dd.text((b[0] + 78, y0 + 24 + off), f"{num}  {lib}", font=F("600", 38), fill=WHITE)
            dd.text((b[0] + 78, y0 + 74 + off), canal, font=F("400", 32), fill=(140, 190, 230))
            if t > 5.0 + i * 1.6 + 0.8:
                ico_check(dd, b[2] - 92, y0 + 62 + off, 54, GREEN)
    return im

# ===================================================== S4 — IA Cuisine

PLANNING = [("Lun", "Karim · Léa"), ("Mar", "Karim · Sam"), ("Mer", "Léa · Sam"),
            ("Jeu", "Karim · Léa"), ("Ven", "Équipe complète")]

def s4_frame(t):
    im = canvas(CREAM); d = ImageDraw.Draw(im)
    dot_grid(d, 120, H - 120)
    title_pill(im, t, "IA Cuisine")
    # 1) alerte stock
    p = appear(t, 1.2, 0.6)
    if p > 0:
        shake = int(6 * math.sin((t - 1.2) * 26)) if 1.2 < t < 2.4 else 0
        b = slide_card(im, (80 + shake, 370, W - 80 + shake, 600), 40, (255, 244, 226), p, dy=60)
        dd = ImageDraw.Draw(im)
        ico_alert(dd, b[0] + 110, (b[1] + b[3]) // 2, 96, ORANGE)
        dd.text((b[0] + 196, b[1] + 50), "Tomates : rupture dans 3 j", font=F("700", 46), fill=INK)
        dd.text((b[0] + 196, b[1] + 118), "Stock 4,2 kg · conso. 1,5 kg/jour", font=F("400", 34), fill=GREY)
    # 2) commande fournisseur générée
    p = appear(t, 6.0, 0.6)
    if p > 0:
        b = slide_card(im, (80, 670, W - 80, 1180), 40, WHITE, p, dy=60)
        dd = ImageDraw.Draw(im)
        dd.text((b[0] + 50, b[1] + 40), "Commande fournisseur", font=F("700", 46), fill=INK)
        dd.text((b[0] + 50, b[1] + 104), "Générée automatiquement", font=F("400", 34), fill=BLUE)
        rows = [("Tomates grappe", "12 kg"), ("Mozzarella", "6 kg"), ("Basilic frais", "10 bottes")]
        for i, (lib, qte) in enumerate(rows):
            rp = fade(t, 7.2 + i * 0.7, 0.35)
            if rp <= 0: continue
            y = b[1] + 175 + i * 82
            col = tuple(int(WHITE[k] + (INK[k] - WHITE[k]) * rp) for k in range(3))
            dd.text((b[0] + 50, y), lib, font=F("500", 40), fill=col)
            dd.text((b[2] - 50, y), qte, font=F("700", 40), fill=col, anchor="ra")
        if t > 9.6:
            gp = fade(t, 9.6, 0.4)
            y = b[1] + 452
            dd.rounded_rectangle((b[0] + 50, y, b[0] + 50 + int(560 * gp), y + 76), 38, fill=(226, 246, 235))
            if gp > 0.6:
                ico_check(dd, b[0] + 100, y + 38, 46, GREEN)
                dd.text((b[0] + 146, y + 16), "Envoyée · livraison mer. 7h", font=F("600", 34), fill=(20, 120, 76))
    # 3) planning
    p = appear(t, 13.2, 0.6)
    if p > 0:
        b = slide_card(im, (80, 1180, W - 80, 1670), 40, WHITE, p, dy=60)
        dd = ImageDraw.Draw(im)
        dd.text((b[0] + 50, b[1] + 36), "Planning de la semaine", font=F("700", 46), fill=INK)
        for i, (jour, equipe) in enumerate(PLANNING):
            rp = appear(t, 14.4 + i * 0.55, 0.4)
            if rp <= 0: continue
            y = b[1] + 120 + i * 80
            w_ = int((b[2] - b[0] - 100) * min(1.0, rp))
            dd.rounded_rectangle((b[0] + 50, y, b[0] + 50 + w_, y + 62), 18, fill=(233, 242, 255))
            if rp > 0.55:
                dd.text((b[0] + 74, y + 12), jour, font=F("700", 34), fill=BLUE)
                dd.text((b[0] + 190, y + 12), equipe, font=F("500", 34), fill=INK)
    return im

# ================================================= S5 — Pilotage WhatsApp

CHAT = [
    ("out", "Combien de couverts ce midi ?", 2.0),
    ("in", ["Service du midi : 64 couverts", "Ticket moyen : 23,40 €", "+12 % vs mardi dernier"], 4.6),
    ("out", "Il me reste combien de steaks hachés ?", 10.0),
    ("in", ["18 portions en stock", "Suffisant jusqu'à jeudi", "Livraison prévue mercredi 7h"], 12.6),
]

def draw_chat(im, t, screen):
    d = ImageDraw.Draw(im)
    sx0, sy0, sx1, sy1 = screen
    # en-tête
    d.rounded_rectangle((sx0, sy0, sx1, sy0 + 150), 0, fill=(7, 94, 84))
    d.rectangle((sx0, sy0 + 100, sx1, sy0 + 150), fill=(7, 94, 84))
    mw, mh = mark(im, (sx0 + 34, sy0 + 40), h=72)
    d.text((sx0 + 130, sy0 + 46), "FoodEatUp", font=F("700", 44), fill=WHITE)
    d.text((sx0 + 130, sy0 + 98), "en ligne", font=F("400", 30), fill=(190, 230, 220))
    y = sy0 + 210
    for kind, payload, t0 in CHAT:
        p = appear(t, t0, 0.4)
        if p <= 0: break
        if kind == "out":
            f = F("500", 40)
            lines = wrap(d, payload, f, 690)
            hgt = 44 + len(lines) * 52
            wdt = int(max(d.textlength(l, font=f) for l in lines)) + 60
            x1 = sx1 - 40; x0 = x1 - wdt
            off = int((1 - p) * 24)
            d.rounded_rectangle((x0, y + off, x1, y + hgt + off), 26, fill=(220, 248, 198))
            for i, l in enumerate(lines):
                d.text((x0 + 30, y + 22 + i * 52 + off), l, font=f, fill=(20, 40, 30))
            y += hgt + 34
        else:
            # bulle réponse structurée
            f = F("600", 40)
            hgt = 40 + len(payload) * 66
            wdt = 700
            x0 = sx0 + 40; x1 = x0 + wdt
            off = int((1 - p) * 24)
            d.rounded_rectangle((x0, y + off, x1, y + hgt + off), 26, fill=WHITE)
            d.rounded_rectangle((x0, y + off, x0 + 10, y + hgt + off), 4, fill=BLUE)
            for i, l in enumerate(payload):
                lp = fade(t, t0 + 0.25 + i * 0.45, 0.3)
                if lp <= 0: break
                col = tuple(int(WHITE[k] + (INK[k] - WHITE[k]) * lp) for k in range(3))
                d.text((x0 + 34, y + 22 + i * 66 + off), l, font=f, fill=col)
            y += hgt + 34
        # indicateur de saisie avant la réponse suivante
    # points de saisie
    for kind, payload, t0 in CHAT:
        if kind == "in" and t0 - 1.5 < t < t0:
            x0 = sx0 + 40
            yy = y
            d.rounded_rectangle((x0, yy, x0 + 190, yy + 78), 26, fill=WHITE)
            for k in range(3):
                a = 0.4 + 0.6 * abs(math.sin((t * 3.2) + k * 0.7))
                col = tuple(int(255 + (120 - 255) * a) for _ in range(3))
                d.ellipse((x0 + 40 + k * 46, yy + 30, x0 + 62 + k * 46, yy + 52), fill=col)
            break
    # barre de saisie
    d.rounded_rectangle((sx0 + 30, sy1 - 120, sx1 - 30, sy1 - 34), 42, fill=(238, 240, 242))
    d.text((sx0 + 70, sy1 - 98), "Écrire un message…", font=F("400", 34), fill=(150, 158, 166))

def s5_frame(t):
    im = canvas(CREAM); d = ImageDraw.Draw(im)
    dot_grid(d, 120, H - 120)
    title_pill(im, t, "IA Pilotage")
    p = appear(t, 0.8, 0.8)
    if p > 0:
        top = 330 + int((1 - p) * 80)
        box = (110, top, W - 110, top + 1310)
        screen = phone_frame(d, box, r=72, screen=(236, 229, 221))
        if p > 0.7:
            draw_chat(im, t, screen)
    return im

# ============================================ S6 — IA Réseaux sociaux

def s6_frame(t):
    """Alerte stock -> suggestion validée -> cascade d'actions -> post publié.

    Après la validation, la moitié haute (notification + suggestion) s'efface pour
    laisser le post occuper l'écran : sinon le contenu déborde du cadre du téléphone.
    """
    im = canvas(CREAM); d = ImageDraw.Draw(im)
    dot_grid(d, 120, H - 120)
    title_pill(im, t, "IA Réseaux sociaux")
    p = appear(t, 0.8, 0.8)
    if p <= 0: return im
    top = 330 + int((1 - p) * 80)
    box = (110, top, W - 110, top + 1310)
    screen = phone_frame(d, box, r=72, screen=PAPER)
    sx0, sy0, sx1, sy1 = screen
    # opacité de la moitié haute : 1 jusqu'à 15,0 s puis fondu
    up = 1.0 if t < 15.0 else max(0.0, 1.0 - (t - 15.0) / 0.8)

    def mix(c, f):
        return tuple(int(PAPER[k] + (c[k] - PAPER[k]) * f) for k in range(3))

    # 1) notification push
    np_ = appear(t, 1.6, 0.5) * up
    if np_ > 0.02:
        off = int((1 - min(1.0, appear(t, 1.6, 0.5))) * 60)
        nb = (sx0 + 24, sy0 + 60 - off, sx1 - 24, sy0 + 226 - off)
        dd = ImageDraw.Draw(im)
        dd.rounded_rectangle(nb, 28, fill=mix(WHITE, np_))
        dd.text((nb[0] + 40, nb[1] + 26), "FoodEatUp · maintenant", font=F("600", 30), fill=mix(GREY, np_))
        dd.text((nb[0] + 40, nb[1] + 68), "Stock à écouler", font=F("700", 40), fill=mix(INK, np_))
        dd.text((nb[0] + 40, nb[1] + 116), "Tomates — 3 jours restants", font=F("400", 36), fill=mix(ORANGE, np_))

    # 2) suggestion de recette
    sp = appear(t, 5.0, 0.6)
    if sp * up > 0.02:
        cb = (sx0 + 24, sy0 + 262, sx1 - 24, sy0 + 872)
        off = int((1 - sp) * 60)
        b = (cb[0], cb[1] + off, cb[2], cb[3] + off)
        dd = ImageDraw.Draw(im)
        dd.rounded_rectangle(b, 32, fill=mix(WHITE, up))
        if up > 0.5:
            try:
                ph = Image.open(f"{PLATS}/plat-du-jour.jpg").convert("RGB")
                tw_, th_ = b[2] - b[0] - 48, 260
                r_ = max(tw_ / ph.width, th_ / ph.height)
                ph = ph.resize((int(ph.width * r_), int(ph.height * r_)), Image.LANCZOS)
                ph = ph.crop(((ph.width - tw_) // 2, (ph.height - th_) // 2,
                              (ph.width - tw_) // 2 + tw_, (ph.height - th_) // 2 + th_))
                msk = Image.new("L", (tw_, th_), 0)
                ImageDraw.Draw(msk).rounded_rectangle((0, 0, tw_, th_), 22, fill=255)
                im.paste(ph, (b[0] + 24, b[1] + 24), msk)
            except Exception:
                pass
        dd = ImageDraw.Draw(im)
        dd.text((b[0] + 28, b[1] + 306), "Suggestion du jour", font=F("600", 32), fill=mix(BLUE, up))
        dd.text((b[0] + 28, b[1] + 352), "Tarte fine tomates & burrata", font=F("700", 44), fill=mix(INK, up))
        dd.text((b[0] + 28, b[1] + 412), "Écoule 3,8 kg · marge préservée", font=F("400", 34), fill=mix(GREY, up))
        bx = (b[0] + 28, b[1] + 486, b[2] - 28, b[1] + 578)
        validated = t > 8.6
        dd.rounded_rectangle(bx, 46, fill=mix(GREEN if validated else BLUE, up))
        dd.text(((bx[0] + bx[2]) / 2, (bx[1] + bx[3]) / 2), "Validé" if validated else "Valider la promotion",
                font=F("700", 40), fill=mix(WHITE, up), anchor="mm")
        if 8.2 < t < 9.2:
            rr_ = int((t - 8.2) * 240)
            a = max(0.0, 1 - (t - 8.2))
            dd.ellipse(((bx[0] + bx[2]) / 2 - rr_, (bx[1] + bx[3]) / 2 - rr_,
                        (bx[0] + bx[2]) / 2 + rr_, (bx[1] + bx[3]) / 2 + rr_),
                       outline=WHITE, width=max(1, int(7 * a)))

    # 3) cascade d'actions (reste à l'écran, remonte quand le haut s'efface)
    rise = int((1 - up) * 660)
    for i, (lab, t0) in enumerate([("Carte mise à jour", 11.0), ("Recette en promotion", 12.0), ("Campagne publiée", 13.0)]):
        ap = appear(t, t0, 0.45)
        if ap <= 0: continue
        y = sy0 + 920 + i * 96 - rise
        off = int((1 - ap) * 26)
        dd = ImageDraw.Draw(im)
        dd.rounded_rectangle((sx0 + 24, y + off, sx1 - 24, y + 78 + off), 24, fill=(226, 246, 235))
        ico_check(dd, sx0 + 76, y + 38 + off, 48, (20, 140, 88))
        dd.text((sx0 + 130, y + 16 + off), lab, font=F("600", 40), fill=(16, 92, 60))

    # 4) le post publié prend toute la place libérée
    pp = appear(t, 15.6, 0.7)
    if pp > 0:
        pb = (sx0 + 24, sy0 + 600, sx1 - 24, sy0 + 1348)
        off = int((1 - pp) * 70)
        b = (pb[0], pb[1] + off, pb[2], pb[3] + off)
        dd = ImageDraw.Draw(im)
        dd.rounded_rectangle(b, 30, fill=WHITE)
        mark(im, (b[0] + 24, b[1] + 22), h=56)
        dd = ImageDraw.Draw(im)
        dd.text((b[0] + 100, b[1] + 22), "votre restaurant", font=F("700", 34), fill=INK)
        dd.text((b[0] + 100, b[1] + 64), "publié à l'instant", font=F("400", 28), fill=GREY)
        try:
            ph = Image.open(f"{PLATS}/plat-du-jour.jpg").convert("RGB")
            tw_, th_ = b[2] - b[0] - 48, 330
            r_ = max(tw_ / ph.width, th_ / ph.height)
            ph = ph.resize((int(ph.width * r_), int(ph.height * r_)), Image.LANCZOS)
            ph = ph.crop(((ph.width - tw_) // 2, (ph.height - th_) // 2,
                          (ph.width - tw_) // 2 + tw_, (ph.height - th_) // 2 + th_))
            msk = Image.new("L", (tw_, th_), 0)
            ImageDraw.Draw(msk).rounded_rectangle((0, 0, tw_, th_), 20, fill=255)
            im.paste(ph, (b[0] + 24, b[1] + 118), msk)
        except Exception:
            pass
        dd = ImageDraw.Draw(im)
        dd.text((b[0] + 26, b[1] + 470), "Ce soir : tarte fine", font=F("600", 38), fill=INK)
        dd.text((b[0] + 26, b[1] + 518), "tomates & burrata", font=F("600", 38), fill=INK)
        dd.text((b[0] + 26, b[1] + 576), "-20 % jusqu'à jeudi", font=F("700", 38), fill=ORANGE)
        if t > 17.4:
            n = int(min(148, (t - 17.4) * 52))
            dd.ellipse((b[0] + 26, b[1] + 646, b[0] + 66, b[1] + 686), outline=RED, width=5)
            dd.text((b[0] + 84, b[1] + 646), f"{n} personnes touchées", font=F("600", 34), fill=GREY)
    return im

# ===================================================== S7 — carte CTA

def s7_frame(t):
    im = canvas(CREAM); d = ImageDraw.Draw(im)
    d.ellipse((-260, -260, 620, 620), fill=(246, 241, 214))
    d.ellipse((W - 500, H - 620, W + 380, H + 260), fill=(246, 241, 214))
    p = appear(t, 0.3, 0.8)
    if p > 0:
        logo(im, 560 - int((1 - p) * 60), h=180)
    if t > 1.6:
        a = fade(t, 1.6)
        col = tuple(int(CREAM[i] + (INK[i] - CREAM[i]) * a) for i in range(3))
        d.text((W // 2, 860), "La gestion de votre restaurant,", font=F("700", 56), fill=col, anchor="ma")
        col2 = tuple(int(CREAM[i] + (BLUE[i] - CREAM[i]) * a) for i in range(3))
        d.text((W // 2, 936), "simplifiée par l'IA", font=F("700", 56), fill=col2, anchor="ma")
    p = appear(t, 3.4, 0.6)
    if p > 0:
        y = 1180 - int((1 - p) * 40)
        d.rounded_rectangle((150, y, W - 150, y + 150), 75, fill=ORANGE)
        d.text((W // 2, y + 75), "Réservez votre démo", font=F("800", 56), fill=INK, anchor="mm")
    if t > 5.0:
        a = fade(t, 5.0)
        col = tuple(int(CREAM[i] + (INK[i] - CREAM[i]) * a) for i in range(3))
        d.text((W // 2, 1400), "foodeatup.fr/demo", font=F("600", 46), fill=col, anchor="ma")
        colg = tuple(int(CREAM[i] + (GREY[i] - CREAM[i]) * a) for i in range(3))
        d.text((W // 2, 1470), "[lien de prise de RDV à confirmer]", font=F("400", 30), fill=colg, anchor="ma")
    return im

# ---------------------------------------------------------------- main
SCENES = {"s2": (s2_frame, 13.0), "s3": (s3_frame, 15.0), "s4": (s4_frame, 19.0),
          "s5": (s5_frame, 17.0), "s6": (s6_frame, 22.0), "s7": (s7_frame, 11.0)}

if __name__ == "__main__":
    todo = sys.argv[1:] or list(SCENES)
    for name in todo:
        fn, dur = SCENES[name]
        render(name, dur, fn)
