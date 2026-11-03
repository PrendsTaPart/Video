#!/usr/bin/env python3
"""Gabarit « Présentatrice » — la bulle animée qui parle.

Durée libre : elle vaut exactement celle de la voix off fournie. Le plan de
l'avatar est **rendu une seule fois pour toute la série** (`assets/avatar-
generique.mp4`) puis bouclé en aller-retour, ce qui évite le saut d'un raccord
bout-à-bout. L'anneau dégradé tourne, le halo et les treize barres de niveau
suivent l'enveloppe sonore de la voix : c'est la voix qui pilote l'animation,
jamais l'inverse.

    from habillage import Presentatrice, rendre_presentatrice
    rendre_presentatrice(
        Presentatrice(titre="Brancher un MCP",
                      promesse="Vous ajoutez n'importe quel logiciel compatible.",
                      numero=13, voix=Path("vo/N0.mp3")),
        Path("out/presenter.mp4"))
"""

from __future__ import annotations

import math
import shutil
from dataclasses import dataclass
from pathlib import Path

from PIL import Image, ImageDraw, ImageFilter

from .noyau import (ACCENT, BACKGROUND_PAGE, BUBBLE_EDGE, FPS, H, LOGO_NOIR,
                    PLAN_AVATAR, PRIMARY, PRIMARY_BUTTON, TEXT_DARK, W, WHITE,
                    blend, ease_out_back, encoder, ffmpeg_bin, fitted, font,
                    glow, pill, ramp, run, shift, text_layer, voice_envelope,
                    wrap)

BULLE_D = 620          # diamètre de la bulle
BULLE_CY = 700         # hauteur de son centre
BARRES = 13            # barres de niveau sous la bulle


@dataclass
class Presentatrice:
    """Réglages de la bulle de présentation.

    `voix`  — MP3 de la voix off ; sa durée fixe celle du plan.
    `plan`  — MP4 de l'avatar qui parle ; celui de la série par défaut.
    `puce`  — texte de la pastille ; construit depuis `numero` s'il est absent.
    """
    titre: str
    promesse: str
    voix: Path
    numero: int | None = None
    puce: str | None = None
    enseigne: str = "ACADÉMIE PLAN'IT"
    plan: Path = PLAN_AVATAR

    @property
    def pastille(self) -> str:
        if self.puce:
            return self.puce
        return "TUTORIEL" if self.numero is None else f"TUTORIEL {self.numero:02d}"


_MASQUE_BORD: dict[int, Image.Image] = {}


def masque_bord(diametre: int) -> Image.Image:
    """Voile radial : opaque au bord du cercle, nul au centre.

    Le plan de la présentatrice arrive sur fond gris studio, qui jure avec le
    lavande de la carte. Un détourage par `colorkey` est exclu — le sujet est un
    rendu 3D plein de tons neutres et la clé mange cheveux, peau et col. Ce
    dégradé fond le pourtour vers la marque sans jamais toucher le visage.
    """
    if diametre in _MASQUE_BORD:
        return _MASQUE_BORD[diametre]
    mask = Image.new("L", (diametre, diametre), 0)
    d = ImageDraw.Draw(mask)
    steps, inner = 34, 0.60
    for i in range(steps):
        f = i / (steps - 1)
        radius = diametre / 2 * (1 - f * (1 - inner))
        c = diametre / 2
        d.ellipse((c - radius, c - radius, c + radius, c + radius),
                  fill=int(255 * ((1 - f) ** 1.6)))
    mask = mask.filter(ImageFilter.GaussianBlur(diametre * 0.035))
    _MASQUE_BORD[diametre] = mask
    return mask


def cercle(src: Image.Image, diametre: int, haut: float = 0.055,
           zoom: float = 0.86) -> Image.Image:
    """Recadre le visage en rond, avec le voile de bord."""
    src = src.convert("RGBA")
    side = int(min(src.width, src.height) * zoom)
    top = min(int(src.height * haut), src.height - side)
    left = (src.width - side) // 2
    face = src.crop((left, top, left + side, top + side)).resize(
        (diametre, diametre), Image.LANCZOS)
    tint = Image.new("RGB", (diametre, diametre), BUBBLE_EDGE)
    face = Image.composite(tint, face.convert("RGB"), masque_bord(diametre)).convert("RGBA")
    mask = Image.new("L", (diametre, diametre), 0)
    ImageDraw.Draw(mask).ellipse((0, 0, diametre - 1, diametre - 1), fill=255)
    face.putalpha(mask)
    return face


def anneau(diametre: int, epaisseur: int, rotation: float) -> Image.Image:
    """Anneau dégradé rose → violet, dessiné arc par arc."""
    ring = Image.new("RGBA", (diametre, diametre), (0, 0, 0, 0))
    d = ImageDraw.Draw(ring)
    steps = 180
    for i in range(steps):
        f = i / steps
        colour = tuple(round(ACCENT[c] + (PRIMARY[c] - ACCENT[c]) *
                             (0.5 - 0.5 * math.cos(2 * math.pi * f))) for c in range(3))
        d.arc((epaisseur // 2, epaisseur // 2,
               diametre - epaisseur // 2 - 1, diametre - epaisseur // 2 - 1),
              start=rotation + f * 360, end=rotation + f * 360 + (360 / steps) + 1.2,
              fill=colour + (255,), width=epaisseur)
    return ring


def sequence_parlante(video: Path, besoin: int, travail: Path) -> list[Path]:
    """Images du plan générique, bouclées en aller-retour sur `besoin` images."""
    travail.mkdir(parents=True, exist_ok=True)
    run([ffmpeg_bin(), "-y", "-v", "error", "-i", str(video),
         "-vf", f"fps={FPS}", str(travail / "t%04d.png")])
    shots = sorted(travail.glob("t*.png"))
    if not shots:
        raise RuntimeError(f"aucune image extraite de {video}")
    cycle = shots + shots[-2:0:-1]          # aller-retour
    return [cycle[i % len(cycle)] for i in range(besoin)]


def fond() -> Image.Image:
    """Fond lavande de la carte, avec ses trois halos."""
    bg = Image.new("RGBA", (W, H), BACKGROUND_PAGE + (255,))
    bg.alpha_composite(glow(int(W * 0.16), int(H * 0.18), 560, ACCENT, 0.20))
    bg.alpha_composite(glow(int(W * 0.90), int(H * 0.80), 620, PRIMARY, 0.18))
    bg.alpha_composite(glow(W // 2, BULLE_CY, 520, PRIMARY_BUTTON, 0.10))
    return bg


def rendre_image(t: float, niveau: float, bg, face, logo, cfg: Presentatrice,
                 niveaux: list[float], index: int) -> Image.Image:
    """Une image de la bulle, à l'instant `t`, au niveau sonore `niveau`."""
    frame = bg.copy()

    p = ramp(t, 0.1, 0.6)
    if p > 0:
        layer = Image.new("RGBA", (W, H), (0, 0, 0, 0))
        layer.alpha_composite(logo.resize((96, 96), Image.LANCZOS), (72, 96))
        ImageDraw.Draw(layer).text((196, 144), cfg.enseigne,
                                   font=font("Manrope-700.ttf", 40),
                                   fill=PRIMARY + (255,), anchor="lm")
        blend(frame, layer, p)

    p = ramp(t, 0.15, 0.8, ease_out_back)
    if p > 0:
        halo_r = int((BULLE_D / 2 + 40) * p + niveau * 46)
        blend(frame, glow(W // 2, BULLE_CY, halo_r, ACCENT, 0.30 + 0.22 * niveau), p)

        ring_d = int(BULLE_D * (0.99 + 0.035 * niveau) * p)
        epaisseur = int(16 + 12 * niveau)
        ring = anneau(ring_d + epaisseur * 2, epaisseur, -t * 26)
        layer = Image.new("RGBA", (W, H), (0, 0, 0, 0))
        layer.alpha_composite(ring, (W // 2 - ring.width // 2, BULLE_CY - ring.height // 2))

        inner = max(2, int(BULLE_D * (0.96 + 0.03 * niveau) * p))
        disc = Image.new("RGBA", (inner, inner), (0, 0, 0, 0))
        ImageDraw.Draw(disc).ellipse((0, 0, inner - 1, inner - 1), fill=(255, 255, 255, 255))
        layer.alpha_composite(disc, (W // 2 - inner // 2, BULLE_CY - inner // 2))
        layer.alpha_composite(face.resize((inner, inner), Image.LANCZOS),
                              (W // 2 - inner // 2, BULLE_CY - inner // 2))
        blend(frame, layer, p)

    p = ramp(t, 0.7, 0.5)
    if p > 0:
        layer = Image.new("RGBA", (W, H), (0, 0, 0, 0))
        d = ImageDraw.Draw(layer)
        bar_w, gap = 12, 18
        x = W // 2 - (BARRES * bar_w + (BARRES - 1) * gap) // 2
        y = BULLE_CY + BULLE_D // 2 + 96
        for i in range(BARRES):
            idx = min(len(niveaux) - 1, max(0, index - abs(i - BARRES // 2) * 2))
            amp = niveaux[idx] if niveaux else 0.0
            shape = math.sin(math.pi * (i + 0.5) / BARRES)
            bh = max(10, int((18 + 96 * amp * shape) * p))
            colour = tuple(round(PRIMARY[c] + (ACCENT[c] - PRIMARY[c]) * shape) for c in range(3))
            d.rounded_rectangle((x, y - bh // 2, x + bar_w, y + bh // 2),
                                radius=bar_w // 2, fill=colour + (235,))
            x += bar_w + gap
        blend(frame, layer, p)

    p = ramp(t, 1.0, 0.7)
    if p > 0:
        blend(frame, shift(text_layer(cfg.titre,
                                      fitted("Sora-700.ttf", 92, cfg.titre, W - 150),
                                      TEXT_DARK, W // 2, 1355), (1 - p) * 44), p)

    p = ramp(t, 1.35, 0.7)
    if p > 0:
        layer = Image.new("RGBA", (W, H), (0, 0, 0, 0))
        d = ImageDraw.Draw(layer)
        fnt = font("Manrope-500.ttf", 44)
        for i, line in enumerate(wrap(cfg.promesse, fnt, W - 180)):
            d.text((W // 2, 1455 + i * 62), line, font=fnt,
                   fill=(60, 40, 110, 255), anchor="mm")
        blend(frame, shift(layer, (1 - p) * 34), p)

    p = ramp(t, 1.7, 0.6)
    if p > 0:
        blend(frame, shift(pill(cfg.pastille, font("Manrope-700.ttf", 40), W // 2, 1665,
                                PRIMARY + (255,), WHITE), (1 - p) * 30), p)
    return frame


def rendre_presentatrice(cfg: Presentatrice, cible: Path,
                         travail: Path | None = None) -> Path:
    """Rend la bulle sur toute la durée de la voix et encode le MP4 sonore."""
    travail = travail or cible.parent / ".presenter"
    if travail.exists():
        shutil.rmtree(travail)
    travail.mkdir(parents=True)

    niveaux = voice_envelope(cfg.voix, FPS)
    total = len(niveaux)
    shots = sequence_parlante(cfg.plan, total, travail / "talking")

    bg = fond()
    logo = Image.open(LOGO_NOIR).convert("RGBA")

    for i in range(total):
        face = cercle(Image.open(shots[i]), BULLE_D)
        rendre_image(i / FPS, niveaux[i], bg, face, logo, cfg, niveaux, i
                     ).convert("RGB").save(travail / f"p{i:04d}.png", compress_level=1)
        if i % 60 == 0:
            print(f"  bulle : {i}/{total}", flush=True)

    encoder(travail, "p%04d.png", cible, audio=cfg.voix)
    shutil.rmtree(travail)
    return cible
