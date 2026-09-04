#!/usr/bin/env python3
"""Thumbnails, 16:9 and 9:16, from the strongest refrain frame.

Frame chosen by scoring saturation and exposure across the three refrains
(t = 115.70 s, EP119 - the mascot, the most legible frame of the clip).
Charter: the logo is never tilted, never framed, FOOD and EATUP never split,
and it keeps a protection zone of half its height.
"""
import os, subprocess
from PIL import Image, ImageDraw, ImageFont

HERE = os.path.dirname(os.path.abspath(__file__))
BRAND = os.path.join(HERE, '..', 'assets', 'brand')
DIST = os.path.join(HERE, '..', 'dist')
T = 115.70
MARINE = (15, 26, 35)
CREME = (252, 249, 230)
BLEU = (0, 123, 255)


def grab(src, t, out):
    subprocess.run(['ffmpeg', '-y', '-v', 'error', '-ss', str(t), '-i', src,
                    '-frames:v', '1', '-q:v', '2', out], check=True)


def scrim(img, side):
    """Readability gradient, marine, on the side that carries the logo."""
    w, h = img.size
    g = Image.new('L', (1, h if side == 'bottom' else 1))
    ov = Image.new('RGB', (w, h), MARINE)
    mask = Image.new('L', (w, h), 0)
    d = ImageDraw.Draw(mask)
    if side == 'bottom':
        for y in range(h):
            a = max(0, min(255, int(255 * (y / h - 0.42) / 0.58 * 1.15)))
            d.line([(0, y), (w, y)], fill=a)
    else:
        for y in range(h):
            a = int(190 * max(0, 1 - y / (h * 0.42)))
            d.line([(0, y), (w, y)], fill=a)
    return Image.composite(ov, img, mask)


def build(src, size, out, logo_w, title_px, sub_px):
    tmp = os.path.join(HERE, 'thumb_src.jpg')
    grab(src, T, tmp)
    img = Image.open(tmp).convert('RGB').resize(size, Image.LANCZOS)
    img = scrim(img, 'top')
    img = scrim(img, 'bottom')

    logo = Image.open(os.path.join(BRAND, 'logo-h-white.png')).convert('RGBA')
    lw = logo_w
    lh = int(logo.height * lw / logo.width)
    logo = logo.resize((lw, lh), Image.LANCZOS)
    pad = max(lh // 2, int(lw * 0.10))      # protection zone
    img.paste(logo, (pad, pad), logo)       # placement à gauche prioritaire

    d = ImageDraw.Draw(img)
    ft = ImageFont.truetype(os.path.join(BRAND, 'Poppins-800.ttf'), title_px)
    fs = ImageFont.truetype(os.path.join(BRAND, 'Poppins-400.ttf'), sub_px)
    W, H = size
    y = H - pad - sub_px - int(title_px * 1.25) - 18
    d.text((pad, y), 'RESTO 2.0', font=ft, fill=CREME)
    d.text((pad, y + int(title_px * 1.25) + 12),
           'Une infinité de solutions pour gérer votre restaurant',
           font=fs, fill=CREME)
    # orange accent, the charter's point of tension
    d.rectangle([pad, y - 26, pad + int(title_px * 1.6), y - 16], fill=(255, 165, 0))
    img.save(out, quality=92)
    print('%s  %dx%d' % (os.path.basename(out), *size))
    os.remove(tmp)


if __name__ == '__main__':
    build(os.path.join(DIST, 'FoodEatUp-Resto-2-0-master-1920x1080.mp4'),
          (1920, 1080), os.path.join(DIST, 'vignette-16x9.jpg'), 420, 96, 38)
    build(os.path.join(DIST, 'FoodEatUp-Resto-2-0-vertical-1080x1920.mp4'),
          (1080, 1920), os.path.join(DIST, 'vignette-9x16.jpg'), 460, 104, 40)
