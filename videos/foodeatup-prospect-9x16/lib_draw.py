"""Primitives de dessin — charte FoodEatUp, format vertical 1080x1920."""
import os, math
from PIL import Image, ImageDraw, ImageFont, ImageFilter

W, H, FPS = 1080, 1920, 30
CREAM = (252, 249, 230); INK = (15, 26, 35); BLUE = (0, 123, 255); BLUE_D = (11, 74, 166)
ORANGE = (255, 165, 0); WHITE = (255, 255, 255); GREY = (140, 150, 160); GREEN = (34, 168, 106)
RED = (219, 68, 55); PAPER = (247, 249, 252)
ROOT = os.path.dirname(os.path.abspath(__file__))
FONTS = "/home/user/Video/videos/rapidocms-presentation-4min/assets/fonts"
BRAND = "/home/user/Video/videos/shared-images/brand"

_AVAILABLE = ("400", "600", "700", "800")
_ALIAS = {"300": "400", "500": "600", "900": "800"}

def F(weight, size):
    w = str(weight)
    w = w if w in _AVAILABLE else _ALIAS.get(w, "600")
    return ImageFont.truetype(f"{FONTS}/Poppins-{w}.ttf", size)

def ease(t):
    """easeOutCubic sur t clampé dans [0,1]."""
    t = max(0.0, min(1.0, t))
    return 1 - (1 - t) ** 3

def ease_back(t):
    t = max(0.0, min(1.0, t))
    c1, c3 = 1.70158, 2.70158
    return 1 + c3 * (t - 1) ** 3 + c1 * (t - 1) ** 2

def canvas(bg=CREAM):
    return Image.new("RGB", (W, H), bg)

def rr(d, box, r, fill, outline=None, width=0):
    d.rounded_rectangle(box, r, fill=fill, outline=outline, width=width)

def shadow_card(im, box, r=36, blur=26, alpha=46, dy=14):
    """Ombre douce sous une carte, dessinée dans un calque séparé."""
    lay = Image.new("RGBA", (W, H), (0, 0, 0, 0))
    ld = ImageDraw.Draw(lay)
    x0, y0, x1, y1 = box
    ld.rounded_rectangle((x0, y0 + dy, x1, y1 + dy), r, fill=(15, 26, 35, alpha))
    im.paste(Image.alpha_composite(im.convert("RGBA"), lay.filter(ImageFilter.GaussianBlur(blur))).convert("RGB"), (0, 0))

def text(d, xy, s, font, fill=INK, anchor=None, spacing=8):
    d.text(xy, s, font=font, fill=fill, anchor=anchor, spacing=spacing)

def text_w(d, s, font):
    return d.textlength(s, font=font)

def center(d, y, s, font, fill=INK):
    d.text((W // 2, y), s, font=font, fill=fill, anchor="ma")

def wrap(d, s, font, maxw):
    words, lines, cur = s.split(), [], ""
    for w_ in words:
        t = (cur + " " + w_).strip()
        if d.textlength(t, font=font) <= maxw:
            cur = t
        else:
            if cur: lines.append(cur)
            cur = w_
    if cur: lines.append(cur)
    return lines

def pill(d, box, label, font, fill=WHITE, fg=INK, r=None):
    x0, y0, x1, y1 = box
    r = r if r is not None else (y1 - y0) // 2
    d.rounded_rectangle(box, r, fill=fill)
    d.text(((x0 + x1) / 2, (y0 + y1) / 2), label, font=font, fill=fg, anchor="mm")

def logo(im, y, h=110, name="foodeatup-logo-mascot.png"):
    m = Image.open(f"{BRAND}/{name}").convert("RGBA")
    r = h / m.height
    m = m.resize((int(m.width * r), h), Image.LANCZOS)
    im.paste(m, ((W - m.width) // 2, y), m)
    return m.width

def mark(im, xy, h=96):
    m = Image.open(f"{BRAND}/foodeatup-mark-eight.png").convert("RGBA")
    r = h / m.height
    m = m.resize((int(m.width * r), h), Image.LANCZOS)
    im.paste(m, xy, m)
    return m.size

def phone_frame(d, box, r=64, body=INK, screen=WHITE, bezel=16):
    """Cadre de téléphone : coque + écran. Retourne la boîte de l'écran."""
    x0, y0, x1, y1 = box
    d.rounded_rectangle(box, r, fill=body)
    s = (x0 + bezel, y0 + bezel, x1 - bezel, y1 - bezel)
    d.rounded_rectangle(s, r - 10, fill=screen)
    # encoche
    nw = 190
    d.rounded_rectangle((W // 2 - nw // 2, y0 + bezel + 8, W // 2 + nw // 2, y0 + bezel + 44), 18, fill=body)
    return s

def fade_layer(im, alpha, color=(0, 0, 0)):
    if alpha <= 0: return im
    lay = Image.new("RGB", (W, H), color)
    return Image.blend(im, lay, min(1.0, alpha))

def dot_grid(d, y0, y1, color=(0, 0, 0), step=54, alpha=14):
    lay = None  # gardé simple : points discrets directement
    for y in range(y0, y1, step):
        for x in range(30, W, step):
            d.ellipse((x, y, x + 3, y + 3), fill=(226, 224, 205))
