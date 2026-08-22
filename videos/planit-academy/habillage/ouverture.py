#!/usr/bin/env python3
"""Gabarit « Ouverture » — le carton d'entrée de toute vidéo Plan'It.

3,6 s, 1080 × 1920. Fond dégradé de marque balayé par une bande de lumière ;
le logo tombe, le mot-marque apparaît, un filet se déploie, le titre monte,
puis la puce du chapeau. La dernière demi-seconde fond vers le lavande de
l'application, pour enchaîner sans coupure sur le plan suivant.

    from habillage import Ouverture, rendre_ouverture
    rendre_ouverture(Ouverture(titre="Brancher un MCP", numero=13),
                     Path("out/intro.mp4"))
"""

from __future__ import annotations

import shutil
from dataclasses import dataclass
from pathlib import Path

from PIL import Image, ImageDraw

from .noyau import (BACKGROUND_PAGE, FPS, H, LOGO_BLANC, W, WHITE, blend,
                    bumper_background, ease_out_back, encoder, fitted, font,
                    light_sweep, pill, ramp, scaled_logo, shift, text_layer)

DUREE = 3.6


@dataclass
class Ouverture:
    """Réglages du carton d'ouverture.

    `titre`   — le titre court, celui qui tient sur une ligne à l'écran.
    `numero`  — numéro du tutoriel ; passer `None` pour un usage hors série.
    `chapeau` — texte de la puce ; construit depuis `numero` s'il est absent.
    `marque`  — mot-marque affiché sous le logo.
    """
    titre: str
    numero: int | None = None
    chapeau: str | None = None
    marque: str = "Plan'It"
    duree: float = DUREE

    @property
    def puce(self) -> str:
        if self.chapeau:
            return self.chapeau
        if self.numero is None:
            return "ACADÉMIE PLAN'IT"
        return f"ACADÉMIE PLAN'IT · TUTORIEL {self.numero:02d}"


def rendre_image(t: float, bg, logo, cfg: Ouverture) -> Image.Image:
    """Une image du carton, à l'instant `t` (en secondes)."""
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
        blend(frame, shift(text_layer(cfg.marque, font("Sora-800.ttf", 168), WHITE,
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
        blend(frame, shift(text_layer(cfg.titre,
                                      fitted("Sora-700.ttf", 88, cfg.titre),
                                      WHITE, W // 2, int(H * 0.635)), (1 - p) * 44), p)

    p = ramp(t, 1.95, 0.7)
    if p > 0:
        chip = cfg.puce
        blend(frame, shift(pill(chip, fitted("Manrope-700.ttf", 40, chip, W - 320),
                                W // 2, int(H * 0.735), (255, 255, 255, 56), WHITE),
                           (1 - p) * 34), p)

    p = ramp(t, cfg.duree - 0.45, 0.45, lambda x: x)
    if p > 0:
        blend(frame, Image.new("RGBA", (W, H), BACKGROUND_PAGE + (255,)), p * 0.92)
    return frame


def rendre_ouverture(cfg: Ouverture, cible: Path, travail: Path | None = None) -> Path:
    """Rend le carton complet et l'encode en MP4 muet."""
    travail = travail or cible.parent / ".frames-ouverture"
    if travail.exists():
        shutil.rmtree(travail)
    travail.mkdir(parents=True)

    bg = bumper_background("intro")
    logo = Image.open(LOGO_BLANC).convert("RGBA")
    for i in range(int(round(cfg.duree * FPS))):
        rendre_image(i / FPS, bg, logo, cfg).convert("RGB").save(
            travail / f"f{i:04d}.png", compress_level=1)

    encoder(travail, "f%04d.png", cible)
    shutil.rmtree(travail)
    return cible
