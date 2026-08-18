#!/usr/bin/env python3
"""Vignette du tutoriel, composée d'après `vignette_spec` du MCP Plan'It Video.

Le MCP ne stocke pas d'image (`urlProduite: null`) : il fournit la **spécification**
(titre court, module et sa couleur, pose d'avatar, écran, variante, gabarit) et une
route de rendu côté Studio. Ce script applique cette spécification localement.

Spécification appliquée pour le tutoriel 00 :

    titreCourt « Ouvrir Plani't » · module 1 « Authentification » #4F2DF9
    avatar « accueil » · écran « ecran-splash » · variante A
    règle : « Concept ou découverte : pose d'accueil ou d'explication, l'avatar domine. »
    gabarit 1280 × 720, export 2560 × 1440 (facteur 2)

    python3 build_thumbnail.py
"""

from __future__ import annotations

import argparse
import math
import shutil
import subprocess
import sys
from pathlib import Path

from PIL import Image, ImageDraw, ImageFilter, ImageFont

ROOT = Path(__file__).resolve().parent
FONTS = ROOT.parent / "_shared" / "fonts"
ASSETS = ROOT / "assets"
OUT = ROOT / "out"

# Gabarit du MCP : 1280 × 720 exporté au facteur 2.
BASE_W, BASE_H = 1280, 720
SCALE = 2
W, H = BASE_W * SCALE, BASE_H * SCALE

ACCENT = (0xFE, 0x64, 0xD5)
WHITE = (255, 255, 255)


def font(name: str, size: int) -> ImageFont.FreeTypeFont:
    return ImageFont.truetype(str(FONTS / name), size)


def fitted(name: str, size: int, text: str, max_width: int) -> ImageFont.FreeTypeFont:
    probe = ImageDraw.Draw(Image.new("L", (1, 1)))
    while size > 16 and probe.textlength(text, font=font(name, size)) > max_width:
        size -= 2
    return font(name, size)


def ffmpeg_bin() -> str:
    return shutil.which("ffmpeg") or __import__("imageio_ffmpeg").get_ffmpeg_exe()


def hex_rgb(value: str) -> tuple[int, int, int]:
    value = value.lstrip("#")
    return tuple(int(value[i:i + 2], 16) for i in (0, 2, 4))


def gradient(size: tuple[int, int], top: tuple[int, int, int],
             bottom: tuple[int, int, int]) -> Image.Image:
    w, h = size
    strip = Image.new("RGB", (1, h))
    px = strip.load()
    for y in range(h):
        f = y / max(h - 1, 1)
        px[0, y] = tuple(round(top[c] + (bottom[c] - top[c]) * f) for c in range(3))
    return strip.resize((w, h), Image.BILINEAR)


def glow(cx: int, cy: int, radius: int, colour, strength: float) -> Image.Image:
    mask = Image.new("L", (W, H), 0)
    ImageDraw.Draw(mask).ellipse((cx - radius, cy - radius, cx + radius, cy + radius),
                                 fill=int(255 * strength))
    mask = mask.filter(ImageFilter.GaussianBlur(radius * 0.5))
    layer = Image.new("RGB", (W, H), colour)
    layer.putalpha(mask)
    return layer


def cutout_avatar(path: Path) -> Image.Image:
    """Détoure l'avatar officiel, fourni sur fond blanc opaque."""
    src = Image.open(path).convert("RGBA")
    px = src.load()
    for y in range(src.height):
        for x in range(src.width):
            r, g, b, _ = px[x, y]
            brightness = min(r, g, b)
            if brightness > 246:
                px[x, y] = (r, g, b, 0)
            elif brightness > 232:
                px[x, y] = (r, g, b, int((brightness - 232) / 14 * 0 + (246 - brightness) / 14 * 255))
    return src


def splash_frame() -> Image.Image | None:
    """Extrait l'écran splash depuis l'animation d'ouverture déjà rendue."""
    intro = OUT / "intro.mp4"
    if not intro.exists():
        return None
    tmp = OUT / ".splash.png"
    subprocess.run([ffmpeg_bin(), "-y", "-loglevel", "error", "-ss", "2.6",
                    "-i", str(intro), "-frames:v", "1", str(tmp)], check=True)
    frame = Image.open(tmp).convert("RGBA")
    tmp.unlink()
    return frame


def rounded(image: Image.Image, radius: int) -> Image.Image:
    mask = Image.new("L", image.size, 0)
    ImageDraw.Draw(mask).rounded_rectangle((0, 0, image.width - 1, image.height - 1),
                                           radius=radius, fill=255)
    out = image.copy()
    out.putalpha(mask)
    return out


def build(titre_court: str, sous_titre: str, module_nom: str, module_hex: str,
          numero: int, target: Path) -> Path:
    module = hex_rgb(module_hex)
    lighter = tuple(min(255, round(c + (255 - c) * 0.34)) for c in module)

    canvas = gradient((W, H), lighter, module).convert("RGBA")
    canvas.alpha_composite(glow(int(W * 0.12), int(H * 0.16), 760, WHITE, 0.15))
    canvas.alpha_composite(glow(int(W * 0.78), int(H * 0.88), 820, ACCENT, 0.30))

    # ── Écran splash, incliné, en retrait derrière l'avatar ─────────────────────
    splash = splash_frame()
    if splash is not None:
        phone_h = int(H * 0.82)
        phone_w = int(phone_h * 9 / 16)
        phone = rounded(splash.resize((phone_w, phone_h), Image.LANCZOS), 46)

        shadow = Image.new("RGBA", (phone_w + 120, phone_h + 120), (0, 0, 0, 0))
        ImageDraw.Draw(shadow).rounded_rectangle(
            (60, 70, phone_w + 60, phone_h + 70), radius=46, fill=(20, 5, 60, 150))
        shadow = shadow.filter(ImageFilter.GaussianBlur(38))

        tilted = phone.rotate(-8, expand=True, resample=Image.BICUBIC)
        tilted_shadow = shadow.rotate(-8, expand=True, resample=Image.BICUBIC)

        px = int(W * 0.545)
        py = int(H * 0.10)
        canvas.alpha_composite(tilted_shadow, (px - 60, py - 60))
        canvas.alpha_composite(tilted, (px, py))

    # ── Avatar : il domine, comme l'exige la variante A ─────────────────────────
    avatar = cutout_avatar(ASSETS / "avatar-planit.png")
    av_h = int(H * 0.95)
    avatar = avatar.resize((int(avatar.width * av_h / avatar.height), av_h), Image.LANCZOS)
    canvas.alpha_composite(
        glow(int(W * 0.855), int(H * 0.58), 430, WHITE, 0.20))
    canvas.alpha_composite(avatar, (int(W * 0.855) - avatar.width // 2, int(H * 0.09)))

    d = ImageDraw.Draw(canvas)

    # ── Bandeau de série ────────────────────────────────────────────────────────
    logo = Image.open(ASSETS / "white_logo.png").convert("RGBA")
    logo = logo.resize((110, 110), Image.LANCZOS)
    canvas.alpha_composite(logo, (110, 96))
    d.text((250, 152), "ACADÉMIE PLAN'IT", font=font("Manrope-700.ttf", 46),
           fill=WHITE + (235,), anchor="lm")

    # ── Titre court ─────────────────────────────────────────────────────────────
    text_width = int(W * 0.54)
    title_font = fitted("Sora-800.ttf", 190, titre_court, text_width)

    shadow = Image.new("RGBA", (W, H), (0, 0, 0, 0))
    ImageDraw.Draw(shadow).text((110, 620), titre_court, font=title_font,
                                fill=(25, 5, 70, 130), anchor="lm")
    canvas.alpha_composite(shadow.filter(ImageFilter.GaussianBlur(20)))
    d = ImageDraw.Draw(canvas)
    d.text((110, 612), titre_court, font=title_font, fill=WHITE + (255,), anchor="lm")

    # ── Sous-titre ──────────────────────────────────────────────────────────────
    d.text((110, 790), sous_titre,
           font=fitted("Manrope-600.ttf", 74, sous_titre, text_width),
           fill=(255, 255, 255, 225), anchor="lm")

    # ── Chip module + numéro ────────────────────────────────────────────────────
    chip = f"TUTORIEL {numero:02d} · {module_nom.upper()}"
    chip_font = fitted("Manrope-700.ttf", 52, chip, text_width)
    cw = d.textlength(chip, font=chip_font)
    x0, y0 = 110, 940
    d.rounded_rectangle((x0, y0, x0 + cw + 110, y0 + 116), radius=58,
                        fill=(255, 255, 255, 240))
    d.text((x0 + 55 + cw / 2, y0 + 58), chip, font=chip_font,
           fill=module + (255,), anchor="mm")

    OUT.mkdir(exist_ok=True)
    canvas.convert("RGB").save(target, "PNG")
    print(f"✓ {target} — {W} × {H}")
    return target


def main() -> int:
    ap = argparse.ArgumentParser(description=__doc__)
    ap.add_argument("--titre-court", default="Ouvrir Plani't")
    ap.add_argument("--sous-titre", default="Créer son compte Plan'It")
    ap.add_argument("--module", default="Authentification")
    ap.add_argument("--couleur", default="#4F2DF9")
    ap.add_argument("--numero", type=int, default=0)
    ap.add_argument("--out", type=Path, default=OUT / "vignette-tuto-00.png")
    args = ap.parse_args()

    build(args.titre_court, args.sous_titre, args.module, args.couleur,
          args.numero, args.out)
    return 0


if __name__ == "__main__":
    sys.exit(main())
