from PIL import Image, ImageDraw, ImageFont, ImageFilter, ImageChops
import subprocess, os, math

P8 = "/root/.fonts/Poppins-800.ttf"; P7 = "/root/.fonts/Poppins-700.ttf"
CREME=(252,249,230); MARINE=(15,26,35); BLEU=(0,123,255); ORANGE=(255,165,0)
LOGO_H = "/home/user/Video/studio-video/assets/brand/logo/foodeatup-logo-horizontal.png"
LOGO_M = "/home/user/Video/studio-video/assets/brand/logo/foodeatup-logo-mascot.png"
MARK   = "/home/user/Video/studio-video/assets/brand/logo/foodeatup-mark-eight.png"

def track(d, xy, text, font, fill, sp=0, anchor="mm"):
    """texte avec interlettrage"""
    ws = [d.textlength(c, font=font) for c in text]
    total = sum(ws) + sp*(len(text)-1)
    x = xy[0] - total/2 if anchor[0] == "m" else xy[0]
    asc, desc = font.getmetrics()
    y = xy[1] - (asc+desc)/2 if anchor[1] == "m" else xy[1]
    for c, w in zip(text, ws):
        d.text((x, y), c, font=font, fill=fill); x += w + sp
    return total

def vgrad(size, top_a, bot_a, color, start=0.0):
    w, h = size; g = Image.new("L", (1, h))
    for y in range(h):
        t = max(0.0, (y/h - start) / max(1e-6, 1-start))
        g.putpixel((0, y), int(255*(top_a + (bot_a-top_a)*t)))
    lay = Image.new("RGBA", size, color+(0,)); lay.putalpha(g.resize(size))
    return lay

# ============================ AFFICHE 1080×1620 ============================
W, H = 1080, 1620
subprocess.run(["ffmpeg","-v","error","-y","-ss","9.62","-i","sources/EP142.mp4",
                "-frames:v","1","work/poster-src.png"], check=True)
src = Image.open("work/poster-src.png").convert("RGB")
s = src.resize((W, int(W*src.height/src.width)), Image.LANCZOS)
bg = s.crop((0, 150, W, 150+H)) if s.height >= 150+H else s.resize((W,H), Image.LANCZOS)

# étalonnage : contraste, désaturation légère, virage marine
bg = Image.blend(bg, bg.convert("L").convert("RGB"), 0.22)
bg = Image.eval(bg, lambda v: int(255*((v/255)**1.18)))
tint = Image.new("RGB", (W,H), (18,34,52))
bg = Image.blend(bg, ImageChops.multiply(bg, tint.point(lambda v: v//1)), 0.0)
bg = bg.convert("RGBA")
# vignette
vg = Image.new("L", (W,H), 0); dv = ImageDraw.Draw(vg)
dv.ellipse((-W*0.35, -H*0.22, W*1.35, H*1.22), fill=255)
vg = vg.filter(ImageFilter.GaussianBlur(200))
bg = Image.composite(bg, Image.new("RGBA",(W,H),MARINE+(255,)), vg)
bg.alpha_composite(vgrad((W,H), 0.0, 0.97, MARINE, start=0.40))
bg.alpha_composite(vgrad((W,H), 0.55, 0.0, MARINE, start=0.0).transform(
    (W,H), Image.AFFINE, (1,0,0,0,1,0)))
d = ImageDraw.Draw(bg)

f_pres  = ImageFont.truetype(P7, 30)
f_title = ImageFont.truetype(P8, 196)
f_tag   = ImageFont.truetype(P8, 44)
f_cred  = ImageFont.truetype(P7, 21)
f_cred2 = ImageFont.truetype(P8, 25)

track(d, (W/2, 96), "FOODEATUP PRÉSENTE", f_pres, CREME+(210,), sp=7)
d.line((W/2-190, 128, W/2+190, 128), fill=BLEU+(180,), width=3)

track(d, (W/2, 1010), "LE CLASH", f_title, CREME, sp=6)
d.line((W/2-330, 1112, W/2+330, 1112), fill=ORANGE+(230,), width=4)
track(d, (W/2, 1168), "DEUX CUISINES. UNE RUE.", f_tag, CREME+(235,), sp=9)

y = 1268
track(d, (W/2, y), "UN FILM PRODUIT PAR FOODEATUP", f_cred2, BLEU+(255,), sp=4); y += 52
for l in ["MUSIQUE « LE CLASH » — DRILL FR × R&B · 144 BPM · LA MINEUR",
          "87 PLANS · 221 COUPES · AUCUNE DEUX FOIS",
          "MONTÉ SUR LA GRILLE — CHAQUE COUPE TOMBE SUR UN TEMPS"]:
    track(d, (W/2, y), l, f_cred, CREME+(165,), sp=3); y += 34

logo = Image.open(LOGO_H).convert("RGBA")
lw = 268; logo = logo.resize((lw, int(lw*logo.height/logo.width)), Image.LANCZOS)
bg.alpha_composite(logo, (int(W/2-lw/2), 1432))
track(d, (W/2, 1568), "FOODEATUP.COM", ImageFont.truetype(P7, 23), CREME+(150,), sp=6)

os.makedirs("dist", exist_ok=True)
bg.convert("RGB").save("dist/affiche-le-clash.jpg", quality=88, optimize=True, progressive=True)
bg.convert("RGB").resize((540,810), Image.LANCZOS).save("work/affiche-preview.png")
print("affiche :", os.path.getsize("dist/affiche-le-clash.jpg")//1024, "Ko")

# ============================ STING LOGO 1080×1920 ============================
SW, SH, FPS, NF = 1080, 1920, 30, 132
os.makedirs("work/sting", exist_ok=True)
mark = Image.open(MARK).convert("RGBA")
word = Image.open(LOGO_M).convert("RGBA")
f_small = ImageFont.truetype(P7, 28); f_dom = ImageFont.truetype(P8, 40)

def ease_out_back(t, s=1.70):
    t -= 1; return t*t*((s+1)*t + s) + 1
def ease_out(t): return 1-(1-t)**3
def seg(f, a, b): return min(1.0, max(0.0, (f-a)/(b-a)))

word = Image.open(LOGO_H).convert("RGBA")
for f in range(NF):
    im = Image.new("RGBA", (SW, SH), MARINE+(255,))
    dd = ImageDraw.Draw(im)
    # 1. la mention, en premier
    t0 = seg(f, 4, 22)
    if t0 > 0:
        track(dd, (SW/2, 752), "UN FILM PRODUIT PAR", f_small,
              CREME+(int(190*ease_out(t0)),), sp=8)
    # 2. la marque, avec rebond
    t1 = seg(f, 12, 38)
    if t1 > 0:
        k = 0.6 + 0.4*ease_out_back(t1)
        mw = max(2, int(118*k)); mh = max(2, int(mw*mark.height/mark.width))
        m = mark.resize((mw, mh), Image.LANCZOS)
        m.putalpha(m.getchannel("A").point(lambda v: int(v*min(1, t1*1.7))))
        im.alpha_composite(m, (int(SW/2-mw/2), int(950-mh/2)))
    # 3. le logotype
    t2 = seg(f, 34, 58)
    if t2 > 0:
        ww = 430; wl = word.resize((ww, int(ww*word.height/word.width)), Image.LANCZOS)
        wl.putalpha(wl.getchannel("A").point(lambda v: int(v*ease_out(t2))))
        im.alpha_composite(wl, (int(SW/2-ww/2), int(1136 + 26*(1-ease_out(t2)))))
    # 4. le trait bleu qui s'ouvre
    t3 = seg(f, 54, 76)
    if t3 > 0:
        w = int(420*ease_out(t3))
        dd.line((SW/2-w/2, 1352, SW/2+w/2, 1352), fill=BLEU+(220,), width=3)
    # 5. l'adresse
    t4 = seg(f, 66, 88)
    if t4 > 0:
        track(dd, (SW/2, 1416), "FOODEATUP.COM", f_dom,
              CREME+(int(235*ease_out(t4)),), sp=5)
    # fondu de sortie
    t5 = seg(f, 112, 125)
    if t5 > 0:
        im.alpha_composite(Image.new("RGBA",(SW,SH),(0,0,0,int(255*t5))))
    im.convert("RGB").save(f"work/sting/{f:04d}.png")

subprocess.run(["ffmpeg","-v","error","-y","-framerate",str(FPS),"-i","work/sting/%04d.png",
                "-c:v","libx264","-preset","veryslow","-crf","14","-pix_fmt","yuv420p",
                "work/sting.mp4"], check=True)
print("sting :", NF, "images,", round(NF/FPS,2), "s,", os.path.getsize("work/sting.mp4")//1024, "Ko")
