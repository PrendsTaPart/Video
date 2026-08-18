#!/usr/bin/env python3
"""Génère l'animation d'ouverture et l'animation de fin de l'Académie Plan'It.

Aucune génération Higgsfield : tout est dessiné ici (Pillow) puis encodé par ffmpeg.
Les couleurs et les polices reprennent exactement les tokens de `planit-app` :
`AppColors.brandGradient`, `AppColors.primary`, `AppColors.accent`, Sora + Manrope.

    python3 build_bumpers.py            # rend out/intro.mp4 et out/outro.mp4
"""

from __future__ import annotations

import math
import shutil
import subprocess
import sys
from pathlib import Path

from PIL import Image, ImageDraw, ImageFilter, ImageFont

# ── Réglages ────────────────────────────────────────────────────────────────────
ROOT = Path(__file__).resolve().parent
FONTS = ROOT.parent / "_shared" / "fonts"
ASSETS = ROOT / "assets"
OUT = ROOT / "out"
WORK = ROOT / ".frames"

W, H = 1080, 1920
FPS = 30
INTRO_SECONDS = 3.6
OUTRO_SECONDS = 5.2

# Tokens de marque — lib/core/theme/app_colors.dart
BRAND_GRADIENT = [
    (0xFE, 0x64, 0xD5),
    (0xFB, 0x63, 0xD6),
    (0xF2, 0x60, 0xD8),
    (0xE2, 0x5B, 0xDB),
    (0xCB, 0x54, 0xDF),
    (0xAE, 0x4B, 0xE5),
    (0x8B, 0x40, 0xED),
    (0x61, 0x33, 0xF5),
    (0x4F, 0x2D, 0xF9),
]
PRIMARY = (0x4F, 0x2D, 0xF9)
ACCENT = (0xFE, 0x64, 0xD5)
BACKGROUND_PAGE = (0xED, 0xEA, 0xFE)

MODULE_COLOR = PRIMARY  # module 1 « Authentification » côté MCP Plan'It Video


SAFE_MARGIN = 80  # marge latérale minimale, en pixels


def font(name: str, size: int) -> ImageFont.FreeTypeFont:
    return ImageFont.truetype(str(FONTS / name), size)


def fitted_font(name: str, size: int, text: str,
                max_width: int = W - 2 * SAFE_MARGIN) -> ImageFont.FreeTypeFont:
    """Même police, réduite juste assez pour que `text` tienne dans le cadre.

    Les libellés viennent des fiches du MCP et changent d'un tutoriel à l'autre :
    on ne peut pas fixer une taille au pixel près pour tous.
    """
    probe = ImageDraw.Draw(Image.new("L", (1, 1)))
    while size > 12 and probe.textlength(text, font=font(name, size)) > max_width:
        size -= 2
    return font(name, size)


# ── Courbes d'animation ─────────────────────────────────────────────────────────
def ease_out_cubic(t: float) -> float:
    return 1 - (1 - t) ** 3


def ease_out_back(t: float) -> float:
    c1, c3 = 1.70158, 2.70158
    return 1 + c3 * (t - 1) ** 3 + c1 * (t - 1) ** 2


def ramp(now: float, start: float, duration: float, curve=ease_out_cubic) -> float:
    """Progression 0→1 d'un élément démarrant à `start` et durant `duration`."""
    if duration <= 0:
        return 1.0
    return curve(min(max((now - start) / duration, 0.0), 1.0))


# ── Fabrique de fonds ───────────────────────────────────────────────────────────
def vertical_gradient(width: int, height: int, stops: list[tuple[int, int, int]]) -> Image.Image:
    """Dégradé vertical interpolé linéairement entre les arrêts fournis."""
    grad = Image.new("RGB", (1, height))
    px = grad.load()
    span = len(stops) - 1
    for y in range(height):
        pos = (y / max(height - 1, 1)) * span
        i = min(int(pos), span - 1)
        f = pos - i
        a, b = stops[i], stops[i + 1]
        px[0, y] = tuple(round(a[c] + (b[c] - a[c]) * f) for c in range(3))
    return grad.resize((width, height), Image.BILINEAR)


def glow(width: int, height: int, cx: int, cy: int, radius: int,
         color: tuple[int, int, int], strength: float) -> Image.Image:
    """Halo radial doux, utilisé pour donner de la profondeur au fond."""
    layer = Image.new("L", (width, height), 0)
    d = ImageDraw.Draw(layer)
    d.ellipse((cx - radius, cy - radius, cx + radius, cy + radius),
              fill=int(255 * strength))
    layer = layer.filter(ImageFilter.GaussianBlur(radius * 0.55))
    tinted = Image.new("RGB", (width, height), color)
    tinted.putalpha(layer)
    return tinted


def build_background(kind: str) -> Image.Image:
    """Fond fixe pré-calculé — seuls les calques de texte bougent ensuite."""
    stops = BRAND_GRADIENT if kind == "intro" else list(reversed(BRAND_GRADIENT))
    bg = vertical_gradient(W, H, stops).convert("RGBA")
    bg.alpha_composite(glow(W, H, int(W * 0.22), int(H * 0.26), 620, (255, 255, 255), 0.16))
    bg.alpha_composite(glow(W, H, int(W * 0.86), int(H * 0.74), 520, ACCENT, 0.22))
    # grain très léger : casse le banding du dégradé sur les grands aplats
    noise = Image.effect_noise((W, H), 7).convert("L").point(lambda v: 128 + (v - 128) // 12)
    bg = Image.blend(bg, Image.merge("RGBA", (noise, noise, noise, bg.getchannel("A"))), 0.045)
    return bg


def light_sweep(offset: float) -> Image.Image:
    """Bande lumineuse diagonale qui traverse le cadre — accent de mouvement."""
    band = Image.new("L", (W, H), 0)
    d = ImageDraw.Draw(band)
    x = int(-W + offset * (2.2 * W))
    d.polygon([(x, H), (x + 260, H), (x + 260 + 420, 0), (x + 420, 0)], fill=64)
    band = band.filter(ImageFilter.GaussianBlur(90))
    sweep = Image.new("RGB", (W, H), (255, 255, 255))
    sweep.putalpha(band)
    return sweep


# ── Primitives de composition ───────────────────────────────────────────────────
def paste_alpha(base: Image.Image, layer: Image.Image, opacity: float) -> None:
    if opacity <= 0.001:
        return
    if opacity < 0.999:
        alpha = layer.getchannel("A").point(lambda v: int(v * opacity))
        layer = layer.copy()
        layer.putalpha(alpha)
    base.alpha_composite(layer)


def text_layer(text: str, fnt: ImageFont.FreeTypeFont, color: tuple[int, int, int],
               cx: int, cy: int, tracking: int = 0,
               shadow: bool = False) -> Image.Image:
    """Rend un texte centré sur (cx, cy) dans son propre calque transparent."""
    layer = Image.new("RGBA", (W, H), (0, 0, 0, 0))
    d = ImageDraw.Draw(layer)

    if tracking:
        widths = [d.textlength(ch, font=fnt) + tracking for ch in text]
        total = sum(widths) - tracking
        x = cx - total / 2
        box = fnt.getbbox("Hg")
        y = cy - (box[3] - box[1]) / 2 - box[1]
        for ch, adv in zip(text, widths):
            d.text((x, y), ch, font=fnt, fill=color + (255,))
            x += adv
    else:
        if shadow:
            sh = Image.new("RGBA", (W, H), (0, 0, 0, 0))
            ImageDraw.Draw(sh).text((cx, cy + 6), text, font=fnt,
                                    fill=(40, 10, 90, 110), anchor="mm")
            layer.alpha_composite(sh.filter(ImageFilter.GaussianBlur(14)))
            d = ImageDraw.Draw(layer)
        d.text((cx, cy), text, font=fnt, fill=color + (255,), anchor="mm")
    return layer


def shift(layer: Image.Image, dy: float) -> Image.Image:
    if abs(dy) < 0.5:
        return layer
    moved = Image.new("RGBA", (W, H), (0, 0, 0, 0))
    moved.paste(layer, (0, int(round(dy))))
    return moved


def scaled_logo(source: Image.Image, height: int) -> Image.Image:
    ratio = height / source.height
    return source.resize((max(1, int(source.width * ratio)), height), Image.LANCZOS)


def place(layer: Image.Image, sprite: Image.Image, cx: int, cy: int) -> None:
    layer.alpha_composite(sprite, (cx - sprite.width // 2, cy - sprite.height // 2))


def pill(text: str, fnt: ImageFont.FreeTypeFont, cx: int, cy: int,
         fill: tuple[int, int, int, int], fg: tuple[int, int, int]) -> Image.Image:
    """Étiquette arrondie type « chip » du design system."""
    layer = Image.new("RGBA", (W, H), (0, 0, 0, 0))
    d = ImageDraw.Draw(layer)
    tw = d.textlength(text, font=fnt)
    pad_x, pad_y = 46, 24
    box = fnt.getbbox("Hg")
    th = box[3] - box[1]
    x0, y0 = cx - tw / 2 - pad_x, cy - th / 2 - pad_y
    x1, y1 = cx + tw / 2 + pad_x, cy + th / 2 + pad_y
    d.rounded_rectangle((x0, y0, x1, y1), radius=(y1 - y0) / 2, fill=fill)
    d.text((cx, cy), text, font=fnt, fill=fg + (255,), anchor="mm")
    return layer


# ── Ouverture ───────────────────────────────────────────────────────────────────
def render_intro_frame(t: float, bg: Image.Image, logo: Image.Image) -> Image.Image:
    frame = bg.copy()
    paste_alpha(frame, light_sweep(ramp(t, 0.15, 2.4, ease_out_cubic)), 0.5)

    # Logo : reprend le geste du splash natif (translation -200 → 0, easeOut).
    p_logo = ramp(t, 0.25, 1.0)
    if p_logo > 0:
        sprite = scaled_logo(logo, int(300 * (0.86 + 0.14 * ease_out_back(p_logo))))
        layer = Image.new("RGBA", (W, H), (0, 0, 0, 0))
        place(layer, sprite, W // 2, int(H * 0.34))
        paste_alpha(frame, shift(layer, (1 - p_logo) * 190), p_logo)

    # Nom de marque
    p_word = ramp(t, 0.85, 0.8)
    if p_word > 0:
        layer = text_layer("Plan'It", font("Sora-800.ttf", 168), (255, 255, 255),
                           W // 2, int(H * 0.50), shadow=True)
        paste_alpha(frame, shift(layer, (1 - p_word) * 52), p_word)

    # Filet de séparation qui s'ouvre depuis le centre
    p_rule = ramp(t, 1.25, 0.65)
    if p_rule > 0:
        layer = Image.new("RGBA", (W, H), (0, 0, 0, 0))
        half = int(150 * p_rule)
        y = int(H * 0.565)
        ImageDraw.Draw(layer).rounded_rectangle(
            (W // 2 - half, y - 4, W // 2 + half, y + 4), radius=4,
            fill=(255, 255, 255, 200))
        paste_alpha(frame, layer, p_rule)

    # Titre du tutoriel
    p_title = ramp(t, 1.5, 0.8)
    if p_title > 0:
        layer = text_layer("Créer son compte", fitted_font("Sora-700.ttf", 88, "Créer son compte"),
                           (255, 255, 255), W // 2, int(H * 0.635))
        paste_alpha(frame, shift(layer, (1 - p_title) * 44), p_title)

    # Chip de série
    p_chip = ramp(t, 1.95, 0.7)
    if p_chip > 0:
        layer = pill("ACADÉMIE PLAN'IT · TUTORIEL 00", font("Manrope-700.ttf", 40),
                     W // 2, int(H * 0.735), (255, 255, 255, 56), (255, 255, 255))
        paste_alpha(frame, shift(layer, (1 - p_chip) * 34), p_chip)

    # Respiration finale : très léger fondu au blanc pour le raccord au screencast
    p_out = ramp(t, INTRO_SECONDS - 0.45, 0.45, lambda x: x)
    if p_out > 0:
        veil = Image.new("RGBA", (W, H), BACKGROUND_PAGE + (255,))
        paste_alpha(frame, veil, p_out * 0.92)
    return frame


# ── Fin ─────────────────────────────────────────────────────────────────────────
PUNCHLINE_TOP = "Vous planifiez une fois."
PUNCHLINE_BOTTOM = "Vos agents s'occupent du reste."


def render_outro_frame(t: float, bg: Image.Image, logo: Image.Image) -> Image.Image:
    frame = bg.copy()
    paste_alpha(frame, light_sweep(ramp(t, 0.3, 3.0, ease_out_cubic)), 0.42)

    # Entrée depuis le blanc, pour raccorder proprement la fin du screencast
    p_in = ramp(t, 0.0, 0.4, lambda x: x)
    p_logo = ramp(t, 0.15, 0.85)
    if p_logo > 0:
        sprite = scaled_logo(logo, int(210 * (0.9 + 0.1 * ease_out_back(p_logo))))
        layer = Image.new("RGBA", (W, H), (0, 0, 0, 0))
        place(layer, sprite, W // 2, int(H * 0.30))
        paste_alpha(frame, layer, p_logo)

    p_top = ramp(t, 0.65, 0.8)
    if p_top > 0:
        layer = text_layer(PUNCHLINE_TOP, fitted_font("Sora-700.ttf", 82, PUNCHLINE_TOP),
                           (255, 255, 255), W // 2, int(H * 0.455), shadow=True)
        paste_alpha(frame, shift(layer, (1 - p_top) * 46), p_top)

    p_bottom = ramp(t, 1.05, 0.8)
    if p_bottom > 0:
        layer = text_layer(PUNCHLINE_BOTTOM, fitted_font("Sora-800.ttf", 82, PUNCHLINE_BOTTOM),
                           (255, 255, 255), W // 2, int(H * 0.535), shadow=True)
        paste_alpha(frame, shift(layer, (1 - p_bottom) * 46), p_bottom)

    p_rule = ramp(t, 1.5, 0.6)
    if p_rule > 0:
        layer = Image.new("RGBA", (W, H), (0, 0, 0, 0))
        half = int(190 * p_rule)
        y = int(H * 0.605)
        ImageDraw.Draw(layer).rounded_rectangle(
            (W // 2 - half, y - 4, W // 2 + half, y + 4), radius=4,
            fill=(255, 255, 255, 190))
        paste_alpha(frame, layer, p_rule)

    p_cta = ramp(t, 1.85, 0.75)
    if p_cta > 0:
        layer = pill("Commencez à planifier intelligemment",
                     fitted_font("Manrope-700.ttf", 44,
                                 "Commencez à planifier intelligemment",
                                 W - 2 * SAFE_MARGIN - 92),
                     W // 2, int(H * 0.685),
                     (255, 255, 255, 235), MODULE_COLOR)
        paste_alpha(frame, shift(layer, (1 - p_cta) * 36), p_cta)

    p_next = ramp(t, 2.35, 0.7)
    if p_next > 0:
        layer = text_layer("Tutoriel suivant · Se connecter à son espace",
                           fitted_font("Manrope-600.ttf", 40,
                                       "Tutoriel suivant · Se connecter à son espace"),
                           (255, 255, 255),
                           W // 2, int(H * 0.775))
        paste_alpha(frame, layer, p_next * 0.88)

    if p_in < 1:
        veil = Image.new("RGBA", (W, H), BACKGROUND_PAGE + (255,))
        paste_alpha(frame, veil, 1 - p_in)
    return frame


# ── Encodage ────────────────────────────────────────────────────────────────────
def ffmpeg_bin() -> str:
    found = shutil.which("ffmpeg")
    if found:
        return found
    import imageio_ffmpeg

    return imageio_ffmpeg.get_ffmpeg_exe()


def render(kind: str, seconds: float, renderer) -> Path:
    frames_dir = WORK / kind
    if frames_dir.exists():
        shutil.rmtree(frames_dir)
    frames_dir.mkdir(parents=True)

    bg = build_background(kind)
    logo = Image.open(ASSETS / "white_logo.png").convert("RGBA")

    total = int(round(seconds * FPS))
    for i in range(total):
        renderer(i / FPS, bg, logo).convert("RGB").save(
            frames_dir / f"f{i:04d}.png", compress_level=1)
        if i % 20 == 0:
            print(f"  {kind}: {i}/{total}", flush=True)

    OUT.mkdir(exist_ok=True)
    target = OUT / f"{kind}.mp4"
    subprocess.run([
        ffmpeg_bin(), "-y", "-loglevel", "error",
        "-framerate", str(FPS), "-i", str(frames_dir / "f%04d.png"),
        "-c:v", "libx264", "-profile:v", "high", "-pix_fmt", "yuv420p",
        "-crf", "18", "-movflags", "+faststart", str(target),
    ], check=True)
    shutil.rmtree(frames_dir)
    print(f"✓ {target} ({total} images, {seconds:.2f} s)")
    return target


def main() -> int:
    render("intro", INTRO_SECONDS, render_intro_frame)
    render("outro", OUTRO_SECONDS, render_outro_frame)
    if WORK.exists() and not any(WORK.iterdir()):
        WORK.rmdir()
    return 0


if __name__ == "__main__":
    sys.exit(main())
