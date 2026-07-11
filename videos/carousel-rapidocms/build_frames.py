#!/usr/bin/env python3
"""Compose 8 branded 1080x1920 frames for the RapidoCMS Carousel presentation video."""
from PIL import Image, ImageDraw, ImageFont, ImageFilter
import os

W, H = 1080, 1920
BG      = (255, 255, 255)
ACCENT  = (41, 169, 242)     # sky blue RapidoCMS
NAVY    = (27, 42, 65)
GREYDOT = (201, 212, 224)
WHITE   = (255, 255, 255)

FD = "assets/fonts"
def F(name, size): return ImageFont.truetype(os.path.join(FD, name), size)
P800 = lambda s: F("Poppins-800.ttf", s)
P700 = lambda s: F("Poppins-700.ttf", s)
P600 = lambda s: F("Poppins-600.ttf", s)
P400 = lambda s: F("Poppins-400.ttf", s)

os.makedirs("frames", exist_ok=True)
logo = Image.open("assets/logo/rapidocms-logo-crop.png").convert("RGBA")

def rounded(size, radius, fill):
    im = Image.new("RGBA", size, (0, 0, 0, 0))
    d = ImageDraw.Draw(im)
    d.rounded_rectangle([0, 0, size[0]-1, size[1]-1], radius=radius, fill=fill)
    return im

def paste_card(canvas, img, box, radius=44, shadow=True):
    x, y, w, h = box
    card = img.convert("RGBA").resize((w, h), Image.LANCZOS)
    mask = rounded((w, h), radius, (255, 255, 255, 255)).split()[3]
    if shadow:
        sh = Image.new("RGBA", (w+80, h+80), (0, 0, 0, 0))
        shm = rounded((w, h), radius, (27, 42, 65, 70))
        sh.paste(shm, (40, 52), shm)
        sh = sh.filter(ImageFilter.GaussianBlur(24))
        canvas.alpha_composite(sh, (x-40, y-40))
    canvas.paste(card, (x, y), mask)

def bg_base():
    im = Image.new("RGBA", (W, H), BG + (255,))
    d = ImageDraw.Draw(im)
    # faint sky-blue cloud blobs (corners) — subtle brand cue
    cloud = Image.new("RGBA", (W, H), (0, 0, 0, 0))
    cd = ImageDraw.Draw(cloud)
    for cx, cy, r in [(980, 70, 150), (1080, 150, 120), (120, 1880, 150), (30, 1800, 110)]:
        cd.ellipse([cx-r, cy-r, cx+r, cy+r], fill=ACCENT + (28,))
    cloud = cloud.filter(ImageFilter.GaussianBlur(6))
    im.alpha_composite(cloud)
    return im

def draw_header(d, im, counter):
    lw = 300
    lh = int(logo.height * lw / logo.width)
    lg = logo.resize((lw, lh), Image.LANCZOS)
    im.alpha_composite(lg, (70, 92))
    # counter pill
    txt = counter
    f = P700(40)
    tb = d.textbbox((0, 0), txt, font=f)
    tw = tb[2]-tb[0]
    pw, ph = tw+56, 68
    px, py = W-70-pw, 96
    pill = rounded((pw, ph), 34, ACCENT + (255,))
    im.alpha_composite(pill, (px, py))
    d.text((px+pw/2, py+ph/2), txt, font=f, fill=WHITE, anchor="mm")

def draw_dots(im, active):
    n = 7
    gap = 26
    aw = 46; dw = 16
    total = aw + (n-1)*(dw+gap)  # rough
    # compute total precisely
    widths = [aw if i == active else dw for i in range(n)]
    total = sum(widths) + gap*(n-1)
    x = (W-total)//2
    y = 1548
    d = ImageDraw.Draw(im)
    for i in range(n):
        w = widths[i]
        col = ACCENT if i == active else GREYDOT
        d.rounded_rectangle([x, y, x+w, y+16], radius=8, fill=col+(255,))
        x += w + gap

def wrap(d, text, font, maxw):
    words = text.split()
    lines, cur = [], ""
    for w in words:
        t = (cur+" "+w).strip()
        if d.textbbox((0,0), t, font=font)[2] <= maxw:
            cur = t
        else:
            if cur: lines.append(cur)
            cur = w
    if cur: lines.append(cur)
    return lines

def draw_caption(im, text):
    d = ImageDraw.Draw(im)
    f = P700(46)
    maxw = 900
    lines = wrap(d, text, f, maxw)
    lh = 62
    th = lh*len(lines)
    pad = 40
    tw = max(d.textbbox((0,0), ln, font=f)[2] for ln in lines)
    pw = min(tw+pad*2, W-80)
    ph = th+pad*2-8
    cy = 1660
    px = (W-pw)//2
    pill = rounded((pw, ph), 40, ACCENT + (235,))
    im.alpha_composite(pill, (px, cy))
    y = cy+pad-4
    for ln in lines:
        d.text((W/2, y+lh/2), ln, font=f, fill=WHITE, anchor="mm")
        y += lh

CAPS = {
 0: "Créer du contenu, ça prend un temps fou.",
 1: "Une bibliothèque de posts, générée par l'IA — 100% modifiable",
 2: "Le problème : c'est chronophage",
 3: "La solution : l'IA génère et centralise vos posts",
 4: "100% personnalisable — contrôle total",
 5: "Gain de temps : 2 clics et c'est publié",
 6: "Toujours à jour, un stock toujours prêt",
 7: "Essayez gratuitement — cms.rapidosoftware.com",
}

# ---- Intro frame (0) ----
im = bg_base()
d = ImageDraw.Draw(im)
lw = 640; lh = int(logo.height*lw/logo.width)
lg = logo.resize((lw, lh), Image.LANCZOS)
im.alpha_composite(lg, ((W-lw)//2, 560))
d.text((W/2, 860), "Le Carousel", font=P800(120), fill=ACCENT, anchor="mm")
sub = "Bibliothèque de posts générée par l'IA"
d.text((W/2, 990), sub, font=P600(46), fill=NAVY, anchor="mm")
d.text((W/2, 1075), "— présentation —", font=P400(40), fill=(120,133,150), anchor="mm")
draw_caption(im, CAPS[0])
im.convert("RGB").save("frames/f0.png")
print("f0 intro")

# ---- 7 carousel slide frames ----
slidefiles = {
 1: "slide1-cover.png", 2: "slide2-probleme.png", 3: "slide3-solution.png",
 4: "slide4-personnalisable.png", 5: "slide5-gaindetemps.png",
 6: "slide6-ajour.png", 7: "slide7-cta.png",
}
for i in range(1, 8):
    im = bg_base()
    d = ImageDraw.Draw(im)
    draw_header(d, im, f"{i}/7")
    sl = Image.open("assets/slides/"+slidefiles[i])
    cw = 1000
    ch = int(cw * sl.height / sl.width)  # 4:5 -> 1250
    paste_card(im, sl, (40, 224, cw, ch))
    draw_dots(im, i-1)
    draw_caption(im, CAPS[i])
    im.convert("RGB").save(f"frames/f{i}.png")
    print("f%d" % i, slidefiles[i])
print("done")
