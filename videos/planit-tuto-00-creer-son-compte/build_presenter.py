#!/usr/bin/env python3
"""Bulle avatar de présentation — composant réutilisable de l'Académie Plan'It.

Carte de présentation animée qui ouvre chaque tutoriel : la présentatrice
apparaît dans une bulle, annonce l'épisode, et passe la main à la démonstration.

Deux modes, selon ce qui est fourni :

* **`--talking <mp4>`** — la bulle contient le plan de synchronisation labiale
  (portrait + voix passés à `creatify-aurora`). L'avatar parle réellement :
  bouche, mâchoire, clignements.
* **sans `--talking`** — repli sur le portrait fixe. La bulle respire et les
  barres de niveau bougent, mais la bouche ne s'anime pas.

Dans les deux cas l'habillage — anneau dégradé, halo, barres de niveau, titre,
promesse, chip — est dessiné localement et **piloté par l'enveloppe réelle du
fichier voix**, pas par une boucle décorative.

    python3 build_presenter.py --talking out/avatar-talking.mp4
    python3 build_presenter.py --titre "Se connecter à son espace" \
                               --numero 1 --vo vo/N0.mp3
"""

from __future__ import annotations

import argparse
import array
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
WORK = ROOT / ".presenter"

W, H = 1080, 1920
FPS = 30

BACKGROUND_PAGE = (0xED, 0xEA, 0xFE)
PRIMARY = (0x4F, 0x2D, 0xF9)
PRIMARY_BUTTON = (0x82, 0x36, 0xF8)
ACCENT = (0xFE, 0x64, 0xD5)
TEXT_DARK = (0x0B, 0x05, 0x16)

BUBBLE_D = 620          # diamètre de la bulle
BUBBLE_CY = 700         # centre vertical de la bulle
BARS = 13               # barres de niveau sous la bulle
BUBBLE_EDGE = (0xDC, 0xD2, 0xFA)  # lavande vers lequel fond le pourtour de la bulle


def font(name: str, size: int) -> ImageFont.FreeTypeFont:
    return ImageFont.truetype(str(FONTS / name), size)


def fitted(name: str, size: int, text: str, max_width: int) -> ImageFont.FreeTypeFont:
    probe = ImageDraw.Draw(Image.new("L", (1, 1)))
    while size > 14 and probe.textlength(text, font=font(name, size)) > max_width:
        size -= 2
    return font(name, size)


def ffmpeg_bin() -> str:
    return shutil.which("ffmpeg") or __import__("imageio_ffmpeg").get_ffmpeg_exe()


def ease_out_cubic(t: float) -> float:
    return 1 - (1 - t) ** 3


def ease_out_back(t: float) -> float:
    c1, c3 = 1.70158, 2.70158
    return 1 + c3 * (t - 1) ** 3 + c1 * (t - 1) ** 2


def ramp(now: float, start: float, dur: float, curve=ease_out_cubic) -> float:
    if dur <= 0:
        return 1.0
    return curve(min(max((now - start) / dur, 0.0), 1.0))


# ── Enveloppe de la voix ────────────────────────────────────────────────────────
def voice_envelope(audio: Path, fps: int) -> list[float]:
    """Niveau sonore normalisé, une valeur par image.

    Décode la voix en PCM 16 bits mono via ffmpeg, puis calcule le RMS par
    image. C'est ce qui anime les barres et la respiration de la bulle.
    """
    raw = subprocess.run(
        [ffmpeg_bin(), "-v", "error", "-i", str(audio),
         "-f", "s16le", "-ac", "1", "-ar", "16000", "-"],
        capture_output=True, check=True).stdout

    samples = array.array("h")
    samples.frombytes(raw[: len(raw) - (len(raw) % 2)])
    per_frame = max(1, 16000 // fps)

    levels: list[float] = []
    for start in range(0, len(samples), per_frame):
        window = samples[start:start + per_frame]
        if not window:
            break
        total = sum(float(s) * s for s in window)
        levels.append(math.sqrt(total / len(window)) / 32768.0)

    peak = max(levels) if levels else 1.0
    if peak <= 0:
        return [0.0] * len(levels)

    # Compression douce : les passages faibles restent visibles.
    return [min(1.0, (lvl / peak) ** 0.55) for lvl in levels]


# ── Fond ────────────────────────────────────────────────────────────────────────
def glow(cx: int, cy: int, radius: int, color, strength: float) -> Image.Image:
    mask = Image.new("L", (W, H), 0)
    ImageDraw.Draw(mask).ellipse((cx - radius, cy - radius, cx + radius, cy + radius),
                                 fill=int(255 * strength))
    mask = mask.filter(ImageFilter.GaussianBlur(radius * 0.5))
    layer = Image.new("RGB", (W, H), color)
    layer.putalpha(mask)
    return layer


def build_background() -> Image.Image:
    bg = Image.new("RGBA", (W, H), BACKGROUND_PAGE + (255,))
    bg.alpha_composite(glow(int(W * 0.16), int(H * 0.18), 560, ACCENT, 0.20))
    bg.alpha_composite(glow(int(W * 0.90), int(H * 0.80), 620, PRIMARY, 0.18))
    bg.alpha_composite(glow(W // 2, BUBBLE_CY, 520, PRIMARY_BUTTON, 0.10))
    return bg


def circular(src: Image.Image, diameter: int, top_ratio: float = 0.055,
             zoom: float = 0.86) -> Image.Image:
    """Recadre une image en cercle, centré sur le visage.

    Sert aussi bien au portrait fixe qu'à chaque image du plan de synchronisation
    labiale : le cadrage doit être identique pour que la bulle ne saute pas.
    """
    src = src.convert("RGBA")
    # `zoom` resserre le cadre sur le visage : à 1.0 on prend le plus grand carré
    # possible, ce qui laisse trop de fond studio autour de la tête.
    side = int(min(src.width, src.height) * zoom)
    top = min(int(src.height * top_ratio), src.height - side)
    left = (src.width - side) // 2
    box = (left, top, left + side, top + side)
    face = src.crop(box).resize((diameter, diameter), Image.LANCZOS)

    face = _blend_edge_to_brand(face, diameter)

    mask = Image.new("L", (diameter, diameter), 0)
    ImageDraw.Draw(mask).ellipse((0, 0, diameter - 1, diameter - 1), fill=255)
    face.putalpha(mask)
    return face


_EDGE_CACHE: dict[int, Image.Image] = {}


def _edge_mask(diameter: int) -> Image.Image:
    """Voile radial : opaque au bord du cercle, nul au centre.

    Le plan de synchronisation labiale arrive sur fond gris studio, qui jure avec
    le lavande de la carte. Un détourage par `colorkey` est exclu : le sujet est
    un rendu 3D bourré de tons neutres, et la clé mange les cheveux et la peau.
    Ce dégradé fond le pourtour vers la couleur de marque — le visage, au centre,
    n'est jamais touché.
    """
    if diameter in _EDGE_CACHE:
        return _EDGE_CACHE[diameter]

    mask = Image.new("L", (diameter, diameter), 0)
    d = ImageDraw.Draw(mask)
    steps = 34
    inner = 0.60          # en deçà de 60 % du rayon, aucune teinte
    # On peint du plus grand cercle au plus petit : le bord reçoit le voile plein,
    # l'opacité retombe à zéro avant d'atteindre le visage.
    for i in range(steps):
        f = i / (steps - 1)
        radius = diameter / 2 * (1 - f * (1 - inner))
        value = int(255 * ((1 - f) ** 1.6))
        c = diameter / 2
        d.ellipse((c - radius, c - radius, c + radius, c + radius), fill=value)
    mask = mask.filter(ImageFilter.GaussianBlur(diameter * 0.035))
    _EDGE_CACHE[diameter] = mask
    return mask


def _blend_edge_to_brand(face: Image.Image, diameter: int) -> Image.Image:
    tint = Image.new("RGB", (diameter, diameter), BUBBLE_EDGE)
    base = face.convert("RGB")
    return Image.composite(tint, base, _edge_mask(diameter)).convert("RGBA")


def talking_frames(video: Path, fps: int, target_dir: Path) -> list[Path]:
    """Décompose le plan de synchronisation labiale en images."""
    target_dir.mkdir(parents=True, exist_ok=True)
    subprocess.run([ffmpeg_bin(), "-y", "-v", "error", "-i", str(video),
                    "-vf", f"fps={fps}", str(target_dir / "t%04d.png")], check=True)
    return sorted(target_dir.glob("t*.png"))


def gradient_ring(diameter: int, thickness: int, rotation: float) -> Image.Image:
    """Anneau dégradé rose→violet, tournant lentement autour de la bulle."""
    ring = Image.new("RGBA", (diameter, diameter), (0, 0, 0, 0))
    d = ImageDraw.Draw(ring)
    steps = 180
    for i in range(steps):
        f = i / steps
        start = rotation + f * 360
        colour = tuple(round(ACCENT[c] + (PRIMARY[c] - ACCENT[c]) * (0.5 - 0.5 * math.cos(2 * math.pi * f)))
                       for c in range(3))
        d.arc((thickness // 2, thickness // 2,
               diameter - thickness // 2 - 1, diameter - thickness // 2 - 1),
              start=start, end=start + (360 / steps) + 1.2,
              fill=colour + (255,), width=thickness)
    return ring


# ── Rendu ───────────────────────────────────────────────────────────────────────
def render_frame(t: float, level: float, bg: Image.Image, avatar: Image.Image,
                 logo: Image.Image, titre: str, sous_titre: str,
                 chip: str, levels: list[float], frame_index: int) -> Image.Image:
    frame = bg.copy()

    # Bandeau haut : logo + nom de la série
    p_head = ramp(t, 0.1, 0.6)
    if p_head > 0:
        layer = Image.new("RGBA", (W, H), (0, 0, 0, 0))
        mark = logo.resize((96, 96), Image.LANCZOS)
        layer.alpha_composite(mark, (72, 96))
        ImageDraw.Draw(layer).text((196, 144), "ACADÉMIE PLAN'IT",
                                   font=font("Manrope-700.ttf", 40),
                                   fill=PRIMARY + (255,), anchor="lm")
        _blend(frame, layer, p_head)

    # Halo qui réagit à la voix
    p_bubble = ramp(t, 0.15, 0.8, ease_out_back)
    if p_bubble > 0:
        halo_r = int((BUBBLE_D / 2 + 40) * p_bubble + level * 46)
        _blend(frame, glow(W // 2, BUBBLE_CY, halo_r, ACCENT, 0.30 + 0.22 * level), p_bubble)

        # Anneau dégradé, rotation lente + épaisseur pilotée par la voix
        ring_d = int(BUBBLE_D * (0.99 + 0.035 * level) * p_bubble)
        thickness = int(16 + 12 * level)
        ring = gradient_ring(ring_d + thickness * 2, thickness, -t * 26)
        layer = Image.new("RGBA", (W, H), (0, 0, 0, 0))
        layer.alpha_composite(ring, (W // 2 - ring.width // 2, BUBBLE_CY - ring.height // 2))

        # Disque blanc puis avatar — la bulle « respire » avec la voix
        inner_d = max(2, int(BUBBLE_D * (0.96 + 0.03 * level) * p_bubble))
        disc = Image.new("RGBA", (inner_d, inner_d), (0, 0, 0, 0))
        ImageDraw.Draw(disc).ellipse((0, 0, inner_d - 1, inner_d - 1),
                                     fill=(255, 255, 255, 255))
        layer.alpha_composite(disc, (W // 2 - inner_d // 2, BUBBLE_CY - inner_d // 2))
        face = avatar.resize((inner_d, inner_d), Image.LANCZOS)
        layer.alpha_composite(face, (W // 2 - inner_d // 2, BUBBLE_CY - inner_d // 2))
        _blend(frame, layer, p_bubble)

    # Barres de niveau — l'indicateur « je parle »
    p_bars = ramp(t, 0.7, 0.5)
    if p_bars > 0:
        layer = Image.new("RGBA", (W, H), (0, 0, 0, 0))
        d = ImageDraw.Draw(layer)
        bar_w, gap = 12, 18
        total = BARS * bar_w + (BARS - 1) * gap
        x = W // 2 - total // 2
        y = BUBBLE_CY + BUBBLE_D // 2 + 96
        for i in range(BARS):
            # Chaque barre lit l'enveloppe avec un léger décalage : l'onde se propage.
            idx = min(len(levels) - 1, max(0, frame_index - abs(i - BARS // 2) * 2))
            amp = levels[idx] if levels else 0.0
            shape = math.sin(math.pi * (i + 0.5) / BARS)  # plus haut au centre
            h = max(10, int((18 + 96 * amp * shape) * p_bars))
            colour = tuple(round(PRIMARY[c] + (ACCENT[c] - PRIMARY[c]) * shape) for c in range(3))
            d.rounded_rectangle((x, y - h // 2, x + bar_w, y + h // 2),
                                radius=bar_w // 2, fill=colour + (235,))
            x += bar_w + gap
        _blend(frame, layer, p_bars)

    # Titre du tutoriel
    p_title = ramp(t, 1.0, 0.7)
    if p_title > 0:
        layer = Image.new("RGBA", (W, H), (0, 0, 0, 0))
        ImageDraw.Draw(layer).text(
            (W // 2, 1355), titre,
            font=fitted("Sora-700.ttf", 92, titre, W - 150),
            fill=TEXT_DARK + (255,), anchor="mm")
        _blend(frame, _shift(layer, (1 - p_title) * 44), p_title)

    # Promesse de la fiche
    p_sub = ramp(t, 1.35, 0.7)
    if p_sub > 0:
        layer = Image.new("RGBA", (W, H), (0, 0, 0, 0))
        d = ImageDraw.Draw(layer)
        fnt = font("Manrope-500.ttf", 44)
        for i, line in enumerate(_wrap(sous_titre, fnt, W - 180)):
            d.text((W // 2, 1455 + i * 62), line, font=fnt,
                   fill=(60, 40, 110, 255), anchor="mm")
        _blend(frame, _shift(layer, (1 - p_sub) * 34), p_sub)

    # Chip de série
    p_chip = ramp(t, 1.7, 0.6)
    if p_chip > 0:
        layer = Image.new("RGBA", (W, H), (0, 0, 0, 0))
        d = ImageDraw.Draw(layer)
        fnt = font("Manrope-700.ttf", 40)
        tw = d.textlength(chip, font=fnt)
        cx, cy = W // 2, 1665
        d.rounded_rectangle((cx - tw / 2 - 48, cy - 44, cx + tw / 2 + 48, cy + 44),
                            radius=44, fill=PRIMARY + (255,))
        d.text((cx, cy), chip, font=fnt, fill=(255, 255, 255, 255), anchor="mm")
        _blend(frame, _shift(layer, (1 - p_chip) * 30), p_chip)

    return frame


def _blend(base: Image.Image, layer: Image.Image, opacity: float) -> None:
    if opacity <= 0.001:
        return
    if opacity < 0.999:
        layer = layer.copy()
        layer.putalpha(layer.getchannel("A").point(lambda v: int(v * opacity)))
    base.alpha_composite(layer)


def _shift(layer: Image.Image, dy: float) -> Image.Image:
    if abs(dy) < 0.5:
        return layer
    moved = Image.new("RGBA", (W, H), (0, 0, 0, 0))
    moved.paste(layer, (0, int(round(dy))))
    return moved


def _wrap(text: str, fnt: ImageFont.FreeTypeFont, max_width: int) -> list[str]:
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


def build(titre: str, sous_titre: str, numero: int, vo: Path, target: Path,
          talking: Path | None = None, portrait: Path | None = None) -> Path:
    if WORK.exists():
        shutil.rmtree(WORK)
    WORK.mkdir(parents=True)
    OUT.mkdir(exist_ok=True)

    levels = voice_envelope(vo, FPS)
    total = len(levels)
    bg = build_background()
    logo = Image.open(ASSETS / "black_logo.png").convert("RGBA")
    chip = f"TUTORIEL {numero:02d}"

    if talking is not None and talking.exists():
        shots = talking_frames(talking, FPS, WORK / "talking")
        print(f"  synchronisation labiale : {len(shots)} images")
        # La voix fait foi : si le plan est plus court, on tient sur sa dernière image.
        def face(i: int) -> Image.Image:
            return circular(Image.open(shots[min(i, len(shots) - 1)]), BUBBLE_D)
    else:
        still = circular(Image.open(portrait or ASSETS / "avatar-presentatrice.png"),
                         BUBBLE_D)
        print("  portrait fixe (pas de plan de synchronisation labiale)")

        def face(i: int) -> Image.Image:
            return still

    for i in range(total):
        render_frame(i / FPS, levels[i], bg, face(i), logo,
                     titre, sous_titre, chip, levels, i
                     ).convert("RGB").save(WORK / f"p{i:04d}.png", compress_level=1)
        if i % 30 == 0:
            print(f"  bulle : {i}/{total}", flush=True)

    subprocess.run([
        ffmpeg_bin(), "-y", "-loglevel", "error",
        "-framerate", str(FPS), "-i", str(WORK / "p%04d.png"),
        "-i", str(vo),
        "-c:v", "libx264", "-profile:v", "high", "-pix_fmt", "yuv420p", "-crf", "18",
        "-c:a", "aac", "-b:a", "192k", "-ar", "48000", "-ac", "2",
        "-shortest", "-movflags", "+faststart", str(target),
    ], check=True)
    shutil.rmtree(WORK)
    print(f"✓ {target} ({total / FPS:.2f} s)")
    return target


def main() -> int:
    ap = argparse.ArgumentParser(description=__doc__)
    ap.add_argument("--titre", default="Créer son compte")
    ap.add_argument("--promesse",
                    default="Votre compte existe et votre espace de travail est ouvert.")
    ap.add_argument("--numero", type=int, default=0)
    ap.add_argument("--vo", type=Path, default=ROOT / "vo" / "N0.mp3")
    ap.add_argument("--talking", type=Path, default=OUT / "avatar-talking.mp4",
                    help="plan de synchronisation labiale (creatify-aurora)")
    ap.add_argument("--portrait", type=Path,
                    default=ASSETS / "avatar-presentatrice.png",
                    help="portrait fixe, utilisé si --talking est absent")
    ap.add_argument("--out", type=Path, default=OUT / "presenter.mp4")
    args = ap.parse_args()

    if not args.vo.exists():
        print(f"voix de présentation introuvable : {args.vo}", file=sys.stderr)
        return 1
    build(args.titre, args.promesse, args.numero, args.vo, args.out,
          talking=args.talking, portrait=args.portrait)
    return 0


if __name__ == "__main__":
    sys.exit(main())
