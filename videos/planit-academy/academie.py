#!/usr/bin/env python3
"""Moteur de fabrication de l'Académie Plan'It — commun aux 43 tutoriels.

Chaque épisode se réduit à une fiche de configuration (`Episode`) : le reste —
ouverture, bulle de présentation, montage de la démonstration, mixage sonore,
vignette — est produit ici, à l'identique d'un épisode à l'autre.

Ce qui est **généré une seule fois puis réutilisé** (`assets/`) :

* `avatar-generique.mp4` — le plan de synchronisation labiale de la présentatrice.
  Un seul rendu `creatify-aurora` pour toute la série. Il est bouclé en
  aller-retour pour couvrir la durée de la voix de chaque épisode.
* `sting-intro.mp3`, `musique-produit.mp3`, `signature-outro.mp3` — l'identité
  sonore.
* Le portrait, les logos, les polices.

Ce qui change à chaque épisode : **les lignes de voix off**, et elles seules.

Règle de calage : chaque plan dure exactement la longueur de sa ligne de voix.
La vitesse du plan en découle — jamais l'inverse.
"""

from __future__ import annotations

import array
import math
import shutil
import subprocess
from dataclasses import dataclass, field
from pathlib import Path

from PIL import Image, ImageDraw, ImageFilter, ImageFont

ACADEMIE = Path(__file__).resolve().parent
FONTS = ACADEMIE.parent / "_shared" / "fonts"
SHARED = ACADEMIE / "assets"
SHARED_AUDIO = SHARED / "audio"

W, H = 1080, 1920
FPS = 30

# ── Tokens de marque — lib/core/theme/app_colors.dart du dépôt planit-app ──────
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
INTRO_SECONDS = 3.6
OUTRO_SECONDS = 5.2

BUBBLE_D = 620
BUBBLE_CY = 700
BARS = 13

MUSIC_DB = -21
STING_DB = -7
SIGNATURE_DB = -5

PUNCHLINE_TOP = "Vous planifiez une fois."
PUNCHLINE_BOTTOM = "Vos agents s'occupent du reste."
BASELINE = "Commencez à planifier intelligemment"


# ── Description d'un épisode ───────────────────────────────────────────────────
@dataclass
class Segment:
    """Un plan de la démonstration : une plage source, une ligne de voix off."""

    vo: str
    src_in: float
    src_out: float
    banner: str

    @property
    def source_span(self) -> float:
        return self.src_out - self.src_in


@dataclass
class Episode:
    numero: int
    slug: str
    titre: str              # fiche.titre
    titre_court: str        # fiche.titreVignette
    promesse: str
    presentation: str       # ce que dit l'avatar
    module_nom: str
    module_couleur: str
    variante: str           # « A » avatar dominant · « B » écran dominant
    suivant: str            # titre du tutoriel suivant
    crop: str               # recadrage du screencast
    segments: list[Segment]
    racine: Path
    ecran_vignette: float = 0.5   # instant du screencast utilisé pour la vignette
    chapitres: list = field(default_factory=list)

    @property
    def out(self) -> Path:
        return self.racine / "out"

    @property
    def vo(self) -> Path:
        return self.racine / "vo"

    @property
    def screencast(self) -> Path:
        return self.racine / "assets" / "screencast.mp4"

    @property
    def final(self) -> Path:
        return self.out / f"tuto-{self.numero:02d}-{self.slug}.mp4"


# ── Utilitaires ────────────────────────────────────────────────────────────────
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
    return ImageFont.truetype(str(FONTS / name), size)


def fitted(name: str, size: int, text: str,
           max_width: int = W - 2 * SAFE_MARGIN) -> ImageFont.FreeTypeFont:
    probe = ImageDraw.Draw(Image.new("L", (1, 1)))
    while size > 14 and probe.textlength(text, font=font(name, size)) > max_width:
        size -= 2
    return font(name, size)


def hex_rgb(value: str) -> tuple[int, int, int]:
    value = value.lstrip("#")
    return tuple(int(value[i:i + 2], 16) for i in (0, 2, 4))


def ease_out_cubic(t: float) -> float:
    return 1 - (1 - t) ** 3


def ease_out_back(t: float) -> float:
    c1, c3 = 1.70158, 2.70158
    return 1 + c3 * (t - 1) ** 3 + c1 * (t - 1) ** 2


def ramp(now: float, start: float, dur: float, curve=ease_out_cubic) -> float:
    if dur <= 0:
        return 1.0
    return curve(min(max((now - start) / dur, 0.0), 1.0))


# ── Composition ────────────────────────────────────────────────────────────────
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
    band = Image.new("L", (W, H), 0)
    d = ImageDraw.Draw(band)
    x = int(-W + offset * (2.2 * W))
    d.polygon([(x, H), (x + 260, H), (x + 260 + 420, 0), (x + 420, 0)], fill=64)
    band = band.filter(ImageFilter.GaussianBlur(90))
    sweep = Image.new("RGB", (W, H), WHITE)
    sweep.putalpha(band)
    return sweep


def bumper_background(kind: str) -> Image.Image:
    stops = BRAND_GRADIENT if kind == "intro" else list(reversed(BRAND_GRADIENT))
    bg = vertical_gradient(W, H, stops).convert("RGBA")
    bg.alpha_composite(glow(int(W * 0.22), int(H * 0.26), 620, WHITE, 0.16))
    bg.alpha_composite(glow(int(W * 0.86), int(H * 0.74), 520, ACCENT, 0.22))
    noise = Image.effect_noise((W, H), 7).convert("L").point(lambda v: 128 + (v - 128) // 12)
    return Image.blend(bg, Image.merge("RGBA", (noise, noise, noise, bg.getchannel("A"))), 0.045)


def scaled_logo(source: Image.Image, height: int) -> Image.Image:
    ratio = height / source.height
    return source.resize((max(1, int(source.width * ratio)), height), Image.LANCZOS)


# ── Ouverture et fin ───────────────────────────────────────────────────────────
def render_intro_frame(t: float, bg, logo, ep: Episode) -> Image.Image:
    frame = bg.copy()
    blend(frame, light_sweep(ramp(t, 0.15, 2.4)), 0.5)

    p = ramp(t, 0.25, 1.0)
    if p > 0:
        sprite = scaled_logo(logo, int(300 * (0.86 + 0.14 * ease_out_back(p))))
        layer = Image.new("RGBA", (W, H), (0, 0, 0, 0))
        layer.alpha_composite(sprite, (W // 2 - sprite.width // 2,
                                       int(H * 0.34) - sprite.height // 2))
        blend(frame, shift(layer, (1 - p) * 190), p)

    p = ramp(t, 0.85, 0.8)
    if p > 0:
        blend(frame, shift(text_layer("Plan'It", font("Sora-800.ttf", 168), WHITE,
                                      W // 2, int(H * 0.50), shadow=True),
                           (1 - p) * 52), p)

    p = ramp(t, 1.25, 0.65)
    if p > 0:
        layer = Image.new("RGBA", (W, H), (0, 0, 0, 0))
        half, y = int(150 * p), int(H * 0.565)
        ImageDraw.Draw(layer).rounded_rectangle(
            (W // 2 - half, y - 4, W // 2 + half, y + 4), radius=4, fill=(255, 255, 255, 200))
        blend(frame, layer, p)

    p = ramp(t, 1.5, 0.8)
    if p > 0:
        blend(frame, shift(text_layer(ep.titre_court,
                                      fitted("Sora-700.ttf", 88, ep.titre_court),
                                      WHITE, W // 2, int(H * 0.635)), (1 - p) * 44), p)

    p = ramp(t, 1.95, 0.7)
    if p > 0:
        chip = f"ACADÉMIE PLAN'IT · TUTORIEL {ep.numero:02d}"
        blend(frame, shift(pill(chip, fitted("Manrope-700.ttf", 40, chip, W - 320),
                                W // 2, int(H * 0.735), (255, 255, 255, 56), WHITE),
                           (1 - p) * 34), p)

    p = ramp(t, INTRO_SECONDS - 0.45, 0.45, lambda x: x)
    if p > 0:
        blend(frame, Image.new("RGBA", (W, H), BACKGROUND_PAGE + (255,)), p * 0.92)
    return frame


def render_outro_frame(t: float, bg, logo, ep: Episode) -> Image.Image:
    frame = bg.copy()
    blend(frame, light_sweep(ramp(t, 0.3, 3.0)), 0.42)

    p_in = ramp(t, 0.0, 0.4, lambda x: x)
    p = ramp(t, 0.15, 0.85)
    if p > 0:
        sprite = scaled_logo(logo, int(210 * (0.9 + 0.1 * ease_out_back(p))))
        layer = Image.new("RGBA", (W, H), (0, 0, 0, 0))
        layer.alpha_composite(sprite, (W // 2 - sprite.width // 2,
                                       int(H * 0.30) - sprite.height // 2))
        blend(frame, layer, p)

    p = ramp(t, 0.65, 0.8)
    if p > 0:
        blend(frame, shift(text_layer(PUNCHLINE_TOP,
                                      fitted("Sora-700.ttf", 82, PUNCHLINE_TOP),
                                      WHITE, W // 2, int(H * 0.455), shadow=True),
                           (1 - p) * 46), p)

    p = ramp(t, 1.05, 0.8)
    if p > 0:
        blend(frame, shift(text_layer(PUNCHLINE_BOTTOM,
                                      fitted("Sora-800.ttf", 82, PUNCHLINE_BOTTOM),
                                      WHITE, W // 2, int(H * 0.535), shadow=True),
                           (1 - p) * 46), p)

    p = ramp(t, 1.5, 0.6)
    if p > 0:
        layer = Image.new("RGBA", (W, H), (0, 0, 0, 0))
        half, y = int(190 * p), int(H * 0.605)
        ImageDraw.Draw(layer).rounded_rectangle(
            (W // 2 - half, y - 4, W // 2 + half, y + 4), radius=4, fill=(255, 255, 255, 190))
        blend(frame, layer, p)

    p = ramp(t, 1.85, 0.75)
    if p > 0:
        blend(frame, shift(pill(BASELINE,
                                fitted("Manrope-700.ttf", 44, BASELINE, W - 252),
                                W // 2, int(H * 0.685), (255, 255, 255, 235),
                                hex_rgb(ep.module_couleur)), (1 - p) * 36), p)

    p = ramp(t, 2.35, 0.7)
    if p > 0:
        suite = f"Tutoriel suivant · {ep.suivant}"
        blend(frame, text_layer(suite, fitted("Manrope-600.ttf", 40, suite),
                                WHITE, W // 2, int(H * 0.775)), p * 0.88)

    if p_in < 1:
        blend(frame, Image.new("RGBA", (W, H), BACKGROUND_PAGE + (255,)), 1 - p_in)
    return frame


def build_bumpers(ep: Episode) -> tuple[Path, Path]:
    logo = Image.open(SHARED / "white_logo.png").convert("RGBA")
    work = ep.racine / ".frames"
    ep.out.mkdir(parents=True, exist_ok=True)
    made = []
    for kind, seconds, renderer in (("intro", INTRO_SECONDS, render_intro_frame),
                                    ("outro", OUTRO_SECONDS, render_outro_frame)):
        if work.exists():
            shutil.rmtree(work)
        work.mkdir(parents=True)
        bg = bumper_background(kind)
        total = int(round(seconds * FPS))
        for i in range(total):
            renderer(i / FPS, bg, logo, ep).convert("RGB").save(
                work / f"f{i:04d}.png", compress_level=1)
        target = ep.out / f"{kind}.mp4"
        run([ffmpeg_bin(), "-y", "-loglevel", "error", "-framerate", str(FPS),
             "-i", str(work / "f%04d.png"), "-c:v", "libx264", "-profile:v", "high",
             "-pix_fmt", "yuv420p", "-crf", "18", "-movflags", "+faststart", str(target)])
        shutil.rmtree(work)
        made.append(target)
        print(f"  {kind} — {seconds:.2f} s")
    return made[0], made[1]


# ── Bulle de présentation ──────────────────────────────────────────────────────
def voice_envelope(audio: Path, fps: int) -> list[float]:
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


_EDGE_CACHE: dict[int, Image.Image] = {}


def edge_mask(diameter: int) -> Image.Image:
    """Voile radial : opaque au bord du cercle, nul au centre.

    Le plan de la présentatrice arrive sur fond gris studio, qui jure avec le
    lavande de la carte. Un détourage par `colorkey` est exclu — le sujet est un
    rendu 3D plein de tons neutres et la clé mange cheveux, peau et col. Ce
    dégradé fond le pourtour vers la marque sans jamais toucher le visage.
    """
    if diameter in _EDGE_CACHE:
        return _EDGE_CACHE[diameter]
    mask = Image.new("L", (diameter, diameter), 0)
    d = ImageDraw.Draw(mask)
    steps, inner = 34, 0.60
    for i in range(steps):
        f = i / (steps - 1)
        radius = diameter / 2 * (1 - f * (1 - inner))
        c = diameter / 2
        d.ellipse((c - radius, c - radius, c + radius, c + radius),
                  fill=int(255 * ((1 - f) ** 1.6)))
    mask = mask.filter(ImageFilter.GaussianBlur(diameter * 0.035))
    _EDGE_CACHE[diameter] = mask
    return mask


def circular(src: Image.Image, diameter: int, top_ratio: float = 0.055,
             zoom: float = 0.86) -> Image.Image:
    src = src.convert("RGBA")
    side = int(min(src.width, src.height) * zoom)
    top = min(int(src.height * top_ratio), src.height - side)
    left = (src.width - side) // 2
    face = src.crop((left, top, left + side, top + side)).resize(
        (diameter, diameter), Image.LANCZOS)
    tint = Image.new("RGB", (diameter, diameter), BUBBLE_EDGE)
    face = Image.composite(tint, face.convert("RGB"), edge_mask(diameter)).convert("RGBA")
    mask = Image.new("L", (diameter, diameter), 0)
    ImageDraw.Draw(mask).ellipse((0, 0, diameter - 1, diameter - 1), fill=255)
    face.putalpha(mask)
    return face


def gradient_ring(diameter: int, thickness: int, rotation: float) -> Image.Image:
    ring = Image.new("RGBA", (diameter, diameter), (0, 0, 0, 0))
    d = ImageDraw.Draw(ring)
    steps = 180
    for i in range(steps):
        f = i / steps
        colour = tuple(round(ACCENT[c] + (PRIMARY[c] - ACCENT[c]) *
                             (0.5 - 0.5 * math.cos(2 * math.pi * f))) for c in range(3))
        d.arc((thickness // 2, thickness // 2,
               diameter - thickness // 2 - 1, diameter - thickness // 2 - 1),
              start=rotation + f * 360, end=rotation + f * 360 + (360 / steps) + 1.2,
              fill=colour + (255,), width=thickness)
    return ring


def talking_sequence(video: Path, needed: int, work: Path) -> list[Path]:
    """Images du plan générique, bouclées en aller-retour sur `needed` images.

    Le plan de la présentatrice est rendu **une seule fois** pour toute la série.
    Comme les textes de présentation n'ont pas tous la même longueur, on le
    boucle : aller, puis retour, ce qui évite le saut d'un raccord bout-à-bout.
    """
    work.mkdir(parents=True, exist_ok=True)
    run([ffmpeg_bin(), "-y", "-v", "error", "-i", str(video),
         "-vf", f"fps={FPS}", str(work / "t%04d.png")])
    shots = sorted(work.glob("t*.png"))
    if not shots:
        raise RuntimeError(f"aucune image extraite de {video}")
    cycle = shots + shots[-2:0:-1]          # aller-retour
    return [cycle[i % len(cycle)] for i in range(needed)]


def render_presenter_frame(t: float, level: float, bg, face, logo, ep: Episode,
                           levels: list[float], index: int) -> Image.Image:
    frame = bg.copy()

    p = ramp(t, 0.1, 0.6)
    if p > 0:
        layer = Image.new("RGBA", (W, H), (0, 0, 0, 0))
        layer.alpha_composite(logo.resize((96, 96), Image.LANCZOS), (72, 96))
        ImageDraw.Draw(layer).text((196, 144), "ACADÉMIE PLAN'IT",
                                   font=font("Manrope-700.ttf", 40),
                                   fill=PRIMARY + (255,), anchor="lm")
        blend(frame, layer, p)

    p = ramp(t, 0.15, 0.8, ease_out_back)
    if p > 0:
        halo_r = int((BUBBLE_D / 2 + 40) * p + level * 46)
        blend(frame, glow(W // 2, BUBBLE_CY, halo_r, ACCENT, 0.30 + 0.22 * level), p)

        ring_d = int(BUBBLE_D * (0.99 + 0.035 * level) * p)
        thickness = int(16 + 12 * level)
        ring = gradient_ring(ring_d + thickness * 2, thickness, -t * 26)
        layer = Image.new("RGBA", (W, H), (0, 0, 0, 0))
        layer.alpha_composite(ring, (W // 2 - ring.width // 2, BUBBLE_CY - ring.height // 2))

        inner = max(2, int(BUBBLE_D * (0.96 + 0.03 * level) * p))
        disc = Image.new("RGBA", (inner, inner), (0, 0, 0, 0))
        ImageDraw.Draw(disc).ellipse((0, 0, inner - 1, inner - 1), fill=(255, 255, 255, 255))
        layer.alpha_composite(disc, (W // 2 - inner // 2, BUBBLE_CY - inner // 2))
        layer.alpha_composite(face.resize((inner, inner), Image.LANCZOS),
                              (W // 2 - inner // 2, BUBBLE_CY - inner // 2))
        blend(frame, layer, p)

    p = ramp(t, 0.7, 0.5)
    if p > 0:
        layer = Image.new("RGBA", (W, H), (0, 0, 0, 0))
        d = ImageDraw.Draw(layer)
        bar_w, gap = 12, 18
        x = W // 2 - (BARS * bar_w + (BARS - 1) * gap) // 2
        y = BUBBLE_CY + BUBBLE_D // 2 + 96
        for i in range(BARS):
            idx = min(len(levels) - 1, max(0, index - abs(i - BARS // 2) * 2))
            amp = levels[idx] if levels else 0.0
            shape = math.sin(math.pi * (i + 0.5) / BARS)
            bh = max(10, int((18 + 96 * amp * shape) * p))
            colour = tuple(round(PRIMARY[c] + (ACCENT[c] - PRIMARY[c]) * shape) for c in range(3))
            d.rounded_rectangle((x, y - bh // 2, x + bar_w, y + bh // 2),
                                radius=bar_w // 2, fill=colour + (235,))
            x += bar_w + gap
        blend(frame, layer, p)

    p = ramp(t, 1.0, 0.7)
    if p > 0:
        blend(frame, shift(text_layer(ep.titre_court,
                                      fitted("Sora-700.ttf", 92, ep.titre_court, W - 150),
                                      TEXT_DARK, W // 2, 1355), (1 - p) * 44), p)

    p = ramp(t, 1.35, 0.7)
    if p > 0:
        layer = Image.new("RGBA", (W, H), (0, 0, 0, 0))
        d = ImageDraw.Draw(layer)
        fnt = font("Manrope-500.ttf", 44)
        for i, line in enumerate(wrap(ep.promesse, fnt, W - 180)):
            d.text((W // 2, 1455 + i * 62), line, font=fnt,
                   fill=(60, 40, 110, 255), anchor="mm")
        blend(frame, shift(layer, (1 - p) * 34), p)

    p = ramp(t, 1.7, 0.6)
    if p > 0:
        chip = f"TUTORIEL {ep.numero:02d}"
        blend(frame, shift(pill(chip, font("Manrope-700.ttf", 40), W // 2, 1665,
                                PRIMARY + (255,), WHITE), (1 - p) * 30), p)
    return frame


def build_presenter(ep: Episode) -> Path:
    """Carte de présentation : plan générique réutilisé + voix propre à l'épisode."""
    vo = ep.vo / "N0.mp3"
    work = ep.racine / ".presenter"
    if work.exists():
        shutil.rmtree(work)
    work.mkdir(parents=True)
    ep.out.mkdir(parents=True, exist_ok=True)

    levels = voice_envelope(vo, FPS)
    total = len(levels)
    shots = talking_sequence(SHARED / "avatar-generique.mp4", total, work / "talking")

    bg = Image.new("RGBA", (W, H), BACKGROUND_PAGE + (255,))
    bg.alpha_composite(glow(int(W * 0.16), int(H * 0.18), 560, ACCENT, 0.20))
    bg.alpha_composite(glow(int(W * 0.90), int(H * 0.80), 620, PRIMARY, 0.18))
    bg.alpha_composite(glow(W // 2, BUBBLE_CY, 520, PRIMARY_BUTTON, 0.10))
    logo = Image.open(SHARED / "black_logo.png").convert("RGBA")

    for i in range(total):
        face = circular(Image.open(shots[i]), BUBBLE_D)
        render_presenter_frame(i / FPS, levels[i], bg, face, logo, ep, levels, i
                               ).convert("RGB").save(work / f"p{i:04d}.png", compress_level=1)
        if i % 60 == 0:
            print(f"  bulle : {i}/{total}", flush=True)

    target = ep.out / "presenter.mp4"
    run([ffmpeg_bin(), "-y", "-loglevel", "error", "-framerate", str(FPS),
         "-i", str(work / "p%04d.png"), "-i", str(vo),
         "-c:v", "libx264", "-profile:v", "high", "-pix_fmt", "yuv420p", "-crf", "18",
         "-c:a", "aac", "-b:a", "192k", "-ar", "48000", "-ac", "2",
         "-shortest", "-movflags", "+faststart", str(target)])
    shutil.rmtree(work)
    print(f"  bulle — {total / FPS:.2f} s")
    return target


# ── Démonstration ──────────────────────────────────────────────────────────────
def make_banner(text: str, path: Path) -> None:
    layer = Image.new("RGBA", (W, 220), (0, 0, 0, 0))
    d = ImageDraw.Draw(layer)
    fnt = fitted("Manrope-700.ttf", 44, text, W - 260)
    tw = d.textlength(text, font=fnt)
    box = fnt.getbbox("Hg")
    th = box[3] - box[1]
    cx, cy = W // 2, 110
    rect = (cx - tw / 2 - 52, cy - th / 2 - 28, cx + tw / 2 + 52, cy + th / 2 + 28)

    sh = Image.new("RGBA", layer.size, (0, 0, 0, 0))
    ImageDraw.Draw(sh).rounded_rectangle((rect[0], rect[1] + 10, rect[2], rect[3] + 10),
                                         radius=(rect[3] - rect[1]) / 2, fill=(30, 10, 70, 90))
    layer.alpha_composite(sh.filter(ImageFilter.GaussianBlur(18)))
    d = ImageDraw.Draw(layer)
    d.rounded_rectangle(rect, radius=(rect[3] - rect[1]) / 2, fill=PRIMARY + (240,))
    d.text((cx, cy), text, font=fnt, fill=(255, 255, 255, 255), anchor="mm")
    layer.save(path)


def crop_dimensions(crop: str) -> tuple[int, int]:
    parts = crop.split("=")[1].split(":")
    return int(parts[0]), int(parts[1])


def render_segment(ep: Episode, index: int, seg: Segment, work: Path) -> Path:
    target_dur = duration_of(ep.vo / f"{seg.vo}.mp3")
    speed = seg.source_span / target_dur

    banner_png = work / f"banner{index:02d}.png"
    make_banner(seg.banner, banner_png)

    src_w, src_h = crop_dimensions(ep.crop)
    phone_h = 1860
    pad_x = (W - round(src_w * phone_h / src_h)) // 2
    pad_y = (H - phone_h) // 2
    fade = 0.35
    bg_hex = "".join(f"{c:02X}" for c in BACKGROUND_PAGE)

    graph = (
        f"[0:v]{ep.crop},setpts=(PTS-STARTPTS)/{speed:.6f},"
        f"scale=-2:{phone_h}:flags=lanczos,fps={FPS},"
        f"pad={W}:{H}:{pad_x}:{pad_y}:color=0x{bg_hex}[phone];"
        f"[1:v]format=rgba,fade=t=in:st=0:d={fade}:alpha=1,"
        f"fade=t=out:st={max(target_dur - fade, 0.1):.3f}:d={fade}:alpha=1[chip];"
        f"[phone][chip]overlay=0:{H - 345}:format=auto[v]"
    )
    out = work / f"seg{index:02d}.mp4"
    run([ffmpeg_bin(), "-y", "-loglevel", "error",
         "-ss", f"{seg.src_in:.3f}", "-t", f"{seg.source_span:.3f}", "-i", str(ep.screencast),
         "-loop", "1", "-t", f"{target_dur:.3f}", "-i", str(banner_png),
         "-i", str(ep.vo / f"{seg.vo}.mp3"),
         "-filter_complex", graph, "-map", "[v]", "-map", "2:a",
         "-t", f"{target_dur:.3f}",
         "-c:v", "libx264", "-profile:v", "high", "-pix_fmt", "yuv420p", "-crf", "19",
         "-c:a", "aac", "-b:a", "192k", "-ar", "48000", "-ac", "2", str(out)])
    print(f"  plan {index} · {seg.banner} — {target_dur:.2f} s (vitesse ×{speed:.2f})")
    return out


def normalise(path: Path, name: str, work: Path) -> Path:
    """Aligne un plan sur le format des segments, en **conservant son audio**.

    Un plan muet (les bumpers) reçoit une piste de silence ; un plan qui parle —
    la bulle de présentation — garde la sienne. C'est la correction du défaut qui
    faisait disparaître la voix de la présentatrice du montage final.
    """
    out = work / name
    dur = duration_of(path)
    probe = subprocess.run([ffmpeg_bin(), "-hide_banner", "-i", str(path)],
                           capture_output=True, text=True).stderr
    has_audio = "Audio:" in probe

    args = [ffmpeg_bin(), "-y", "-loglevel", "error", "-i", str(path)]
    if has_audio:
        audio_in = "[0:a]"
    else:
        args += ["-f", "lavfi", "-t", f"{dur:.3f}",
                 "-i", "anullsrc=channel_layout=stereo:sample_rate=48000"]
        audio_in = "[1:a]"
    args += ["-filter_complex",
             f"[0:v]scale={W}:{H},fps={FPS},format=yuv420p[v];"
             f"{audio_in}aresample=48000,aformat=channel_layouts=stereo,"
             f"apad,atrim=0:{dur:.3f},asetpts=PTS-STARTPTS[a]",
             "-map", "[v]", "-map", "[a]", "-t", f"{dur:.3f}",
             "-c:v", "libx264", "-profile:v", "high", "-pix_fmt", "yuv420p", "-crf", "19",
             "-c:a", "aac", "-b:a", "192k", "-ar", "48000", "-ac", "2", str(out)]
    run(args)
    return out


# ── Mixage ─────────────────────────────────────────────────────────────────────
def mix_audio(source: Path, target: Path) -> None:
    """Pose l'habillage sonore sur le master parole.

    La musique passe par un `sidechaincompress` piloté par la voix : elle se
    retire dès qu'on parle et remonte dans les silences.
    """
    total = duration_of(source)
    outro_at = max(total - OUTRO_SECONDS, 0.0)
    fade_out_at = max(total - 3.2, 0.1)

    graph = (
        f"[0:a]asplit=2[dial][key];"
        f"[1:a]atrim=0:{total:.3f},asetpts=PTS-STARTPTS,volume={MUSIC_DB}dB,"
        f"afade=t=in:st=0:d=1.4,afade=t=out:st={fade_out_at:.3f}:d=3.2[music];"
        f"[music][key]sidechaincompress=threshold=0.03:ratio=9:attack=12:"
        f"release=420:makeup=1[ducked];"
        f"[2:a]adelay=900|900,volume={STING_DB}dB[sting];"
        f"[3:a]adelay={int(outro_at * 1000)}|{int(outro_at * 1000)},"
        f"volume={SIGNATURE_DB}dB[sig];"
        f"[dial][ducked][sting][sig]amix=inputs=4:duration=first:"
        f"dropout_transition=0:normalize=0[mixed];"
        f"[mixed]loudnorm=I=-16:TP=-1.5:LRA=11,aresample=48000[aout]"
    )
    run([ffmpeg_bin(), "-y", "-loglevel", "error", "-i", str(source),
         "-i", str(SHARED_AUDIO / "musique-produit.mp3"),
         "-i", str(SHARED_AUDIO / "sting-intro.mp3"),
         "-i", str(SHARED_AUDIO / "signature-outro.mp3"),
         "-filter_complex", graph, "-map", "0:v", "-map", "[aout]", "-c:v", "copy",
         "-c:a", "aac", "-b:a", "192k", "-ar", "48000", "-ac", "2",
         "-movflags", "+faststart", str(target)])


# ── Vignette ───────────────────────────────────────────────────────────────────
def build_thumbnail(ep: Episode) -> Path:
    """Vignette 1080 × 1920 exportée en 2160 × 3840, au gabarit du MCP."""
    scale = 2
    tw, th = W * scale, H * scale
    module = hex_rgb(ep.module_couleur)
    lighter = tuple(min(255, round(c + (255 - c) * 0.34)) for c in module)

    canvas = vertical_gradient(tw, th, [lighter, module]).convert("RGBA")
    canvas.alpha_composite(glow(int(tw * 0.18), int(th * 0.12), 900, WHITE, 0.16, (tw, th)))
    canvas.alpha_composite(glow(int(tw * 0.84), int(th * 0.70), 1000, ACCENT, 0.28, (tw, th)))

    def f(name, size, text, max_w):
        probe = ImageDraw.Draw(Image.new("L", (1, 1)))
        while size > 20 and probe.textlength(text, font=font(name, size)) > max_w:
            size -= 4
        return font(name, size)

    d = ImageDraw.Draw(canvas)
    margin = 130

    logo = Image.open(SHARED / "white_logo.png").convert("RGBA").resize((150, 150), Image.LANCZOS)
    canvas.alpha_composite(logo, (margin, 170))
    d.text((margin + 200, 248), "ACADÉMIE PLAN'IT", font=font("Manrope-700.ttf", 62),
           fill=WHITE + (235,), anchor="lm")

    title_font = f("Sora-800.ttf", 210, ep.titre_court, tw - 2 * margin)
    sh = Image.new("RGBA", (tw, th), (0, 0, 0, 0))
    ImageDraw.Draw(sh).text((margin, 640), ep.titre_court, font=title_font,
                            fill=(25, 5, 70, 130), anchor="lm")
    canvas.alpha_composite(sh.filter(ImageFilter.GaussianBlur(22)))
    d = ImageDraw.Draw(canvas)
    d.text((margin, 630), ep.titre_court, font=title_font, fill=WHITE + (255,), anchor="lm")

    sub_font = f("Manrope-600.ttf", 84, ep.titre, tw - 2 * margin)
    d.text((margin, 810), ep.titre, font=sub_font, fill=(255, 255, 255, 225), anchor="lm")

    chip = f"TUTORIEL {ep.numero:02d} · {ep.module_nom.upper()}"
    chip_font = f("Manrope-700.ttf", 62, chip, tw - 2 * margin - 140)
    cw = d.textlength(chip, font=chip_font)
    d.rounded_rectangle((margin, 940, margin + cw + 130, 1080), radius=70,
                        fill=(255, 255, 255, 240))
    d.text((margin + 65 + cw / 2, 1010), chip, font=chip_font, fill=module + (255,), anchor="mm")

    # Bas de vignette : l'écran de l'app et la présentatrice.
    screen = _screen_still(ep)
    avatar = _cutout(SHARED / "avatar-presentatrice.png")

    if ep.variante.upper() == "A":
        av_h, av_cx = int(th * 0.56), int(tw * 0.66)
        ph_h, ph_cx = int(th * 0.44), int(tw * 0.26)
    else:
        av_h, av_cx = int(th * 0.44), int(tw * 0.80)
        ph_h, ph_cx = int(th * 0.55), int(tw * 0.38)

    if screen is not None:
        ph_w = int(ph_h * screen.width / screen.height)
        phone = _rounded(screen.resize((ph_w, ph_h), Image.LANCZOS), 54)
        sh = Image.new("RGBA", (ph_w + 160, ph_h + 160), (0, 0, 0, 0))
        ImageDraw.Draw(sh).rounded_rectangle((80, 90, ph_w + 80, ph_h + 90),
                                             radius=54, fill=(20, 5, 60, 150))
        sh = sh.filter(ImageFilter.GaussianBlur(46))
        tilted = phone.rotate(-7, expand=True, resample=Image.BICUBIC)
        tsh = sh.rotate(-7, expand=True, resample=Image.BICUBIC)
        py = th - ph_h - 120
        canvas.alpha_composite(tsh, (ph_cx - tsh.width // 2, py - 80))
        canvas.alpha_composite(tilted, (ph_cx - tilted.width // 2, py))

    avatar = avatar.resize((int(avatar.width * av_h / avatar.height), av_h), Image.LANCZOS)
    canvas.alpha_composite(glow(av_cx, int(th * 0.76), 560, WHITE, 0.20, (tw, th)))
    canvas.alpha_composite(avatar, (av_cx - avatar.width // 2, th - av_h))

    ep.out.mkdir(parents=True, exist_ok=True)
    target = ep.out / f"vignette-tuto-{ep.numero:02d}.png"
    canvas.convert("RGB").save(target, "PNG")
    print(f"  vignette — {tw} × {th}")
    return target


def _screen_still(ep: Episode) -> Image.Image | None:
    if not ep.screencast.exists():
        return None
    tmp = ep.out / ".still.png"
    ep.out.mkdir(parents=True, exist_ok=True)
    run([ffmpeg_bin(), "-y", "-loglevel", "error", "-ss", str(ep.ecran_vignette),
         "-i", str(ep.screencast), "-frames:v", "1", "-vf", ep.crop, str(tmp)])
    img = Image.open(tmp).convert("RGBA")
    tmp.unlink()
    return img


def _rounded(image: Image.Image, radius: int) -> Image.Image:
    mask = Image.new("L", image.size, 0)
    ImageDraw.Draw(mask).rounded_rectangle((0, 0, image.width - 1, image.height - 1),
                                           radius=radius, fill=255)
    out = image.copy()
    out.putalpha(mask)
    return out


def _cutout(path: Path) -> Image.Image:
    """Détoure le portrait, fourni sur fond gris studio uni."""
    src = Image.open(path).convert("RGBA")
    px = src.load()
    for y in range(src.height):
        for x in range(src.width):
            r, g, b, _ = px[x, y]
            if abs(r - g) < 9 and abs(g - b) < 9 and 92 < r < 125:
                px[x, y] = (r, g, b, 0)
    return src


# ── Chaîne complète ────────────────────────────────────────────────────────────
def build_episode(ep: Episode) -> Path:
    print(f"\n=== Tutoriel {ep.numero:02d} — {ep.titre} ===")
    work = ep.racine / ".work"
    if work.exists():
        shutil.rmtree(work)
    work.mkdir(parents=True)
    ep.out.mkdir(parents=True, exist_ok=True)

    print("Ouverture et fin…")
    intro, outro = build_bumpers(ep)

    print("Présentation…")
    presenter = build_presenter(ep)

    print("Démonstration…")
    parts = [normalise(intro, "00_intro.mp4", work),
             normalise(presenter, "01_presenter.mp4", work)]
    for i, seg in enumerate(ep.segments, start=1):
        parts.append(render_segment(ep, i, seg, work))
    parts.append(normalise(outro, "99_outro.mp4", work))

    listing = work / "concat.txt"
    listing.write_text("".join(f"file '{p.resolve()}'\n" for p in parts))
    speech = work / "speech.mp4"
    run([ffmpeg_bin(), "-y", "-loglevel", "error", "-f", "concat", "-safe", "0",
         "-i", str(listing), "-c:v", "libx264", "-profile:v", "high",
         "-pix_fmt", "yuv420p", "-crf", "19",
         "-c:a", "aac", "-b:a", "192k", "-ar", "48000", "-ac", "2", str(speech)])

    print("Mixage sonore…")
    mix_audio(speech, ep.final)

    print("Vignette…")
    build_thumbnail(ep)

    shutil.rmtree(work)
    print(f"\n✓ {ep.final} — {duration_of(ep.final):.2f} s")
    return ep.final
