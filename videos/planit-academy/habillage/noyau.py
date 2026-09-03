#!/usr/bin/env python3
"""Noyau des gabarits d'habillage Plan'It — tokens, primitives, encodage.

Tout ce qui est commun aux trois gabarits (`ouverture`, `presentatrice`, `fin`)
vit ici : les couleurs de marque, les polices, les fonctions de composition et
l'encodage d'une séquence d'images en MP4.

Les couleurs viennent de `lib/core/theme/app_colors.dart` du dépôt
`PrendsTaPart/planit-app`. Ne pas les redéfinir ailleurs : ce fichier est la
seule source.
"""

from __future__ import annotations

import array
import math
import shutil
import subprocess
from pathlib import Path

from PIL import Image, ImageDraw, ImageFilter, ImageFont

RACINE = Path(__file__).resolve().parent.parent
POLICES = RACINE.parent / "_shared" / "fonts"
ASSETS = RACINE / "assets"
AUDIO = ASSETS / "audio"

LOGO_BLANC = ASSETS / "white_logo.png"
LOGO_NOIR = ASSETS / "black_logo.png"
PLAN_AVATAR = ASSETS / "avatar-generique.mp4"
PORTRAIT_AVATAR = ASSETS / "avatar-presentatrice.png"

W, H = 1080, 1920
FPS = 30

# ── Tokens de marque ──────────────────────────────────────────────────────────
BRAND_GRADIENT = [
    (0xFE, 0x64, 0xD5), (0xFB, 0x63, 0xD6), (0xF2, 0x60, 0xD8),
    (0xE2, 0x5B, 0xDB), (0xCB, 0x54, 0xDF), (0xAE, 0x4B, 0xE5),
    (0x8B, 0x40, 0xED), (0x61, 0x33, 0xF5), (0x4F, 0x2D, 0xF9),
]
PRIMARY = (0x4F, 0x2D, 0xF9)
PRIMARY_BUTTON = (0x82, 0x36, 0xF8)
ACCENT = (0xFE, 0x64, 0xD5)
BACKGROUND_PAGE = (0xED, 0xEA, 0xFE)
TEXT_DARK = (0x0B, 0x05, 0x16)
BUBBLE_EDGE = (0xDC, 0xD2, 0xFA)
WHITE = (255, 255, 255)

SAFE_MARGIN = 80

# Couleurs de module, telles que le MCP les renvoie dans `vignette.module`.
MODULES = {
    "Prompts": "#772FF3",
    "Tâches": "#6A2EF5",
    "Connexions API & MCP": "#8236F8",
    "Chat agentique": "#9438F0",
    "Base de connaissance": "#A63FE8",
    "Skills & Plugins": "#B846E0",
    "Profil & Avatar 3D": "#CA4DD8",
    "Accueil & Statistiques": "#5C2DF7",
    "Notifications": "#DC54D0",
    "Crédits & Facturation": "#F45FC4",
    "Automatisations": "#E85AC9",
    "Authentification": "#4F2DF9",
}


# ── Outils ────────────────────────────────────────────────────────────────────
def ffmpeg_bin() -> str:
    return shutil.which("ffmpeg") or __import__("imageio_ffmpeg").get_ffmpeg_exe()


def run(args: list[str]) -> None:
    subprocess.run(args, check=True)


def duration_of(path: Path) -> float:
    proc = subprocess.run([ffmpeg_bin(), "-hide_banner", "-i", str(path)],
                          capture_output=True, text=True)
    for line in proc.stderr.splitlines():
        if "Duration:" in line:
            clock = line.split("Duration:")[1].split(",")[0].strip()
            h, m, s = clock.split(":")
            return int(h) * 3600 + int(m) * 60 + float(s)
    raise RuntimeError(f"durée introuvable pour {path}")


def font(name: str, size: int) -> ImageFont.FreeTypeFont:
    return ImageFont.truetype(str(POLICES / name), size)


def fitted(name: str, size: int, text: str,
           max_width: int = W - 2 * SAFE_MARGIN) -> ImageFont.FreeTypeFont:
    probe = ImageDraw.Draw(Image.new("L", (1, 1)))
    while size > 14 and probe.textlength(text, font=font(name, size)) > max_width:
        size -= 2
    return font(name, size)


def hex_rgb(value: str) -> tuple[int, int, int]:
    value = value.lstrip("#")
    return tuple(int(value[i:i + 2], 16) for i in (0, 2, 4))


# ── Courbes ───────────────────────────────────────────────────────────────────
def ease_out_cubic(t: float) -> float:
    return 1 - (1 - t) ** 3


def ease_out_back(t: float) -> float:
    c1, c3 = 1.70158, 2.70158
    return 1 + c3 * (t - 1) ** 3 + c1 * (t - 1) ** 2


def ramp(now: float, start: float, dur: float, curve=ease_out_cubic) -> float:
    """Avancement 0 → 1 d'une entrée qui démarre à `start` et dure `dur`."""
    if dur <= 0:
        return 1.0
    return curve(min(max((now - start) / dur, 0.0), 1.0))


# ── Composition ───────────────────────────────────────────────────────────────
def vertical_gradient(width: int, height: int, stops) -> Image.Image:
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


def glow(cx: int, cy: int, radius: int, colour, strength: float,
         size: tuple[int, int] = (W, H)) -> Image.Image:
    mask = Image.new("L", size, 0)
    ImageDraw.Draw(mask).ellipse((cx - radius, cy - radius, cx + radius, cy + radius),
                                 fill=int(255 * strength))
    mask = mask.filter(ImageFilter.GaussianBlur(radius * 0.5))
    layer = Image.new("RGB", size, colour)
    layer.putalpha(mask)
    return layer


def blend(base: Image.Image, layer: Image.Image, opacity: float) -> None:
    if opacity <= 0.001:
        return
    if opacity < 0.999:
        layer = layer.copy()
        layer.putalpha(layer.getchannel("A").point(lambda v: int(v * opacity)))
    base.alpha_composite(layer)


def shift(layer: Image.Image, dy: float) -> Image.Image:
    if abs(dy) < 0.5:
        return layer
    moved = Image.new("RGBA", layer.size, (0, 0, 0, 0))
    moved.paste(layer, (0, int(round(dy))))
    return moved


def text_layer(text: str, fnt, colour, cx: int, cy: int,
               shadow: bool = False) -> Image.Image:
    layer = Image.new("RGBA", (W, H), (0, 0, 0, 0))
    if shadow:
        sh = Image.new("RGBA", (W, H), (0, 0, 0, 0))
        ImageDraw.Draw(sh).text((cx, cy + 6), text, font=fnt,
                                fill=(40, 10, 90, 110), anchor="mm")
        layer.alpha_composite(sh.filter(ImageFilter.GaussianBlur(14)))
    ImageDraw.Draw(layer).text((cx, cy), text, font=fnt,
                               fill=tuple(colour) + (255,), anchor="mm")
    return layer


def pill(text: str, fnt, cx: int, cy: int, fill, fg) -> Image.Image:
    layer = Image.new("RGBA", (W, H), (0, 0, 0, 0))
    d = ImageDraw.Draw(layer)
    tw = d.textlength(text, font=fnt)
    box = fnt.getbbox("Hg")
    th = box[3] - box[1]
    pad_x, pad_y = 46, 24
    x0, y0 = cx - tw / 2 - pad_x, cy - th / 2 - pad_y
    x1, y1 = cx + tw / 2 + pad_x, cy + th / 2 + pad_y
    d.rounded_rectangle((x0, y0, x1, y1), radius=(y1 - y0) / 2, fill=fill)
    d.text((cx, cy), text, font=fnt, fill=tuple(fg) + (255,), anchor="mm")
    return layer


def wrap(text: str, fnt, max_width: int) -> list[str]:
    probe = ImageDraw.Draw(Image.new("L", (1, 1)))
    lines, current = [], ""
    for word in text.split():
        trial = f"{current} {word}".strip()
        if probe.textlength(trial, font=fnt) <= max_width:
            current = trial
        else:
            lines.append(current)
            current = word
    if current:
        lines.append(current)
    return lines


def light_sweep(offset: float) -> Image.Image:
    """Bande de lumière oblique qui balaie l'écran de gauche à droite."""
    band = Image.new("L", (W, H), 0)
    d = ImageDraw.Draw(band)
    x = int(-W + offset * (2.2 * W))
    d.polygon([(x, H), (x + 260, H), (x + 260 + 420, 0), (x + 420, 0)], fill=64)
    band = band.filter(ImageFilter.GaussianBlur(90))
    sweep = Image.new("RGB", (W, H), WHITE)
    sweep.putalpha(band)
    return sweep


def bumper_background(kind: str) -> Image.Image:
    """Fond dégradé des cartons. `intro` descend le dégradé, `outro` le remonte."""
    stops = BRAND_GRADIENT if kind == "intro" else list(reversed(BRAND_GRADIENT))
    bg = vertical_gradient(W, H, stops).convert("RGBA")
    bg.alpha_composite(glow(int(W * 0.22), int(H * 0.26), 620, WHITE, 0.16))
    bg.alpha_composite(glow(int(W * 0.86), int(H * 0.74), 520, ACCENT, 0.22))
    noise = Image.effect_noise((W, H), 7).convert("L").point(lambda v: 128 + (v - 128) // 12)
    return Image.blend(bg, Image.merge("RGBA", (noise, noise, noise, bg.getchannel("A"))), 0.045)


def scaled_logo(source: Image.Image, height: int) -> Image.Image:
    ratio = height / source.height
    return source.resize((max(1, int(source.width * ratio)), height), Image.LANCZOS)


def voice_envelope(audio: Path, fps: int = FPS) -> list[float]:
    """Niveau sonore normalisé, une valeur par image."""
    raw = subprocess.run([ffmpeg_bin(), "-v", "error", "-i", str(audio),
                          "-f", "s16le", "-ac", "1", "-ar", "16000", "-"],
                         capture_output=True, check=True).stdout
    samples = array.array("h")
    samples.frombytes(raw[: len(raw) - (len(raw) % 2)])
    per_frame = max(1, 16000 // fps)
    levels = []
    for start in range(0, len(samples), per_frame):
        window = samples[start:start + per_frame]
        if not window:
            break
        levels.append(math.sqrt(sum(float(s) * s for s in window) / len(window)) / 32768.0)
    peak = max(levels) if levels else 1.0
    if peak <= 0:
        return [0.0] * len(levels)
    return [min(1.0, (lvl / peak) ** 0.55) for lvl in levels]


# ── Encodage ──────────────────────────────────────────────────────────────────
def encoder(dossier: Path, motif: str, cible: Path, audio: Path | None = None) -> Path:
    """Encode une séquence d'images en H.264 High / yuv420p, 30 fps."""
    cible.parent.mkdir(parents=True, exist_ok=True)
    args = [ffmpeg_bin(), "-y", "-loglevel", "error",
            "-framerate", str(FPS), "-i", str(dossier / motif)]
    if audio is not None:
        args += ["-i", str(audio)]
    args += ["-c:v", "libx264", "-profile:v", "high", "-pix_fmt", "yuv420p", "-crf", "18"]
    if audio is not None:
        args += ["-c:a", "aac", "-b:a", "192k", "-ar", "48000", "-ac", "2", "-shortest"]
    args += ["-movflags", "+faststart", str(cible)]
    run(args)
    return cible
