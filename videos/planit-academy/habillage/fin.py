#!/usr/bin/env python3
"""Gabarit « Fin » — le carton de sortie de toute vidéo Plan'It.

5,2 s, 1080 × 1920. Le dégradé de marque remonte cette fois du violet vers le
rose. On entre depuis le lavande de l'application, le logo se pose, la
punchline s'écrit en deux temps, un filet se déploie, la baseline arrive en
pastille blanche teintée de la couleur du module, puis l'annonce du tutoriel
suivant.

    from habillage import Fin, rendre_fin
    rendre_fin(Fin(suivant="Gérer ses connecteurs", couleur="#8236F8"),
               Path("out/outro.mp4"))
"""

from __future__ import annotations

import shutil
from dataclasses import dataclass
from pathlib import Path

from PIL import Image, ImageDraw

from .noyau import (BACKGROUND_PAGE, FPS, H, LOGO_BLANC, W, WHITE, blend,
                    bumper_background, ease_out_back, encoder, fitted, hex_rgb,
                    light_sweep, pill, ramp, scaled_logo, shift, text_layer)

DUREE = 5.2
PUNCHLINE_HAUT = "Vous planifiez une fois."
PUNCHLINE_BAS = "Vos agents s'occupent du reste."
BASELINE = "Commencez à planifier intelligemment"


@dataclass
class Fin:
    """Réglages du carton de fin.

    `suivant` — titre du tutoriel suivant ; laisser vide pour masquer la ligne.
    `couleur` — couleur du module, en hexadécimal ; elle teinte la baseline.
    """
    suivant: str = ""
    couleur: str = "#4F2DF9"
    punchline_haut: str = PUNCHLINE_HAUT
    punchline_bas: str = PUNCHLINE_BAS
    baseline: str = BASELINE
    duree: float = DUREE


def rendre_image(t: float, bg, logo, cfg: Fin) -> Image.Image:
    """Une image du carton, à l'instant `t` (en secondes)."""
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
        blend(frame, shift(text_layer(cfg.punchline_haut,
                                      fitted("Sora-700.ttf", 82, cfg.punchline_haut),
                                      WHITE, W // 2, int(H * 0.455), shadow=True),
                           (1 - p) * 46), p)

    p = ramp(t, 1.05, 0.8)
    if p > 0:
        blend(frame, shift(text_layer(cfg.punchline_bas,
                                      fitted("Sora-800.ttf", 82, cfg.punchline_bas),
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
        blend(frame, shift(pill(cfg.baseline,
                                fitted("Manrope-700.ttf", 44, cfg.baseline, W - 252),
                                W // 2, int(H * 0.685), (255, 255, 255, 235),
                                hex_rgb(cfg.couleur)), (1 - p) * 36), p)

    p = ramp(t, 2.35, 0.7)
    if p > 0 and cfg.suivant:
        suite = f"Tutoriel suivant · {cfg.suivant}"
        blend(frame, text_layer(suite, fitted("Manrope-600.ttf", 40, suite),
                                WHITE, W // 2, int(H * 0.775)), p * 0.88)

    if p_in < 1:
        blend(frame, Image.new("RGBA", (W, H), BACKGROUND_PAGE + (255,)), 1 - p_in)
    return frame


def rendre_fin(cfg: Fin, cible: Path, travail: Path | None = None) -> Path:
    """Rend le carton complet et l'encode en MP4 muet."""
    travail = travail or cible.parent / ".frames-fin"
    if travail.exists():
        shutil.rmtree(travail)
    travail.mkdir(parents=True)

    bg = bumper_background("outro")
    logo = Image.open(LOGO_BLANC).convert("RGBA")
    for i in range(int(round(cfg.duree * FPS))):
        rendre_image(i / FPS, bg, logo, cfg).convert("RGB").save(
            travail / f"f{i:04d}.png", compress_level=1)

    encoder(travail, "f%04d.png", cible)
    shutil.rmtree(travail)
    return cible
