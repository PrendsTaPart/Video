#!/usr/bin/env python3
"""Habillage RapidoCMS Académie — cartons animés, bandeaux, pastilles, vignette.

Tout ce qui s'affiche par-dessus la capture d'écran est produit ici, en PIL,
puis encodé ou composité par `montage.py`. Rien n'est dessiné ailleurs.

Cinq gabarits :

- `rendre_ouverture`  — le sting d'entrée (logo origami, mot-marque, titre).
- `rendre_carton`     — le carton de transition entre deux chapitres.
- `rendre_fin`        — l'outro CTA « Essayez RapidoCMS ».
- `bandeaux`          — les calques fixes d'un plan (bandeau haut, sous-titre).
- `medaillon`         — la pastille du présentateur, aux changements de chapitre.

Plus `rendre_vignette`, la miniature 1280 × 720 de la fiche et de YouTube.
"""

from __future__ import annotations

import shutil
from dataclasses import dataclass
from pathlib import Path

from PIL import Image, ImageDraw, ImageFilter

from .charte import (BANDE_BAS, BANDE_HAUT, BLANC, BLEU, BLEU_CLAIR, BLEU_SOMBRE,
                     ECRAN_H, FOND, FPS, GRIS, H, LOGO_ORIGAMI, MARGE, W, ajustee,
                     balayage, coins_arrondis, decouper, detourer_pose,
                     degrade_vertical, encoder, fond_carton, fondre, halo,
                     logo_redimensionne, ombre_portee, pastille, police,
                     rampe, sortie_elastique, texte_centre)

OUVERTURE_S = 3.6
CARTON_S = 1.1
FIN_S = 5.0

URL_ACADEMIE = "academie.rapidosoftware.com"
URL_APP = "cms.rapidosoftware.com"


# ── Ouverture ────────────────────────────────────────────────────────────────
@dataclass
class Ouverture:
    titre: str
    numero: int | None = None
    module: str = ""
    duree: float = OUVERTURE_S

    @property
    def puce(self) -> str:
        if self.numero is None:
            return "ACADÉMIE RAPIDOCMS"
        return f"ACADÉMIE RAPIDOCMS · TUTORIEL {self.numero:02d}"


def _image_ouverture(t: float, fond, logo, cfg: Ouverture) -> Image.Image:
    frame = fond.copy()
    fondre(frame, balayage(rampe(t, 0.15, 2.4), (W, H)), 0.5)

    p = rampe(t, 0.20, 0.9, sortie_elastique)
    if p > 0:
        sprite = logo.resize((int(logo.width * (0.86 + 0.14 * p)),
                              int(logo.height * (0.86 + 0.14 * p))), Image.LANCZOS)
        couche = Image.new("RGBA", (W, H), (0, 0, 0, 0))
        couche.alpha_composite(sprite, (W // 2 - sprite.width // 2,
                                        int(H * 0.20) - sprite.height // 2 + int(60 * (1 - p))))
        fondre(frame, couche, min(1.0, p * 1.4))

    p = rampe(t, 0.75, 0.55)
    if p > 0:
        couche = Image.new("RGBA", (W, H), (0, 0, 0, 0))
        texte_centre(couche, "RapidoCMS", police(True, 78), BLANC,
                     W // 2, int(H * 0.40) + int(26 * (1 - p)), ombre=True)
        fondre(frame, couche, p)

    p = rampe(t, 1.05, 0.5)
    if p > 0:
        couche = Image.new("RGBA", (W, H), (0, 0, 0, 0))
        demi = int((W * 0.24) * p)
        ImageDraw.Draw(couche).rounded_rectangle(
            (W // 2 - demi, int(H * 0.475), W // 2 + demi, int(H * 0.475) + 5),
            radius=3, fill=BLANC + (220,))
        fondre(frame, couche, 1.0)

    p = rampe(t, 1.25, 0.65)
    if p > 0:
        couche = Image.new("RGBA", (W, H), (0, 0, 0, 0))
        fnt = ajustee(True, 92, cfg.titre, W - 2 * MARGE - 160)
        texte_centre(couche, cfg.titre, fnt, BLANC,
                     W // 2, int(H * 0.585) + int(34 * (1 - p)), ombre=True)
        fondre(frame, couche, p)

    p = rampe(t, 1.75, 0.5)
    if p > 0:
        couche = Image.new("RGBA", (W, H), (0, 0, 0, 0))
        pastille(couche, cfg.puce, police(True, 30), W // 2, int(H * 0.715),
                 BLANC, BLEU_SOMBRE)
        fondre(frame, couche, p)

    if cfg.module:
        p = rampe(t, 2.05, 0.45)
        if p > 0:
            couche = Image.new("RGBA", (W, H), (0, 0, 0, 0))
            texte_centre(couche, cfg.module.upper(), police(True, 26),
                         BLEU_CLAIR, W // 2, int(H * 0.795))
            fondre(frame, couche, p * 0.95)

    # Fondu vers le fond clair de l'application, pour enchaîner sans coupure.
    sortie = rampe(t, cfg.duree - 0.45, 0.45)
    if sortie > 0:
        voile = Image.new("RGBA", (W, H), FOND + (255,))
        fondre(frame, voile, sortie)
    return frame


def rendre_ouverture(cfg: Ouverture, cible: Path) -> Path:
    travail = cible.parent / "_ouverture"
    shutil.rmtree(travail, ignore_errors=True)
    travail.mkdir(parents=True)
    fond = fond_carton((W, H), "intro")
    logo = logo_redimensionne(300)
    total = int(cfg.duree * FPS)
    for i in range(total):
        img = _image_ouverture(i / FPS, fond, logo, cfg)
        img.convert("RGB").save(travail / f"f{i:04d}.png")
    encoder(travail, "f%04d.png", cible)
    shutil.rmtree(travail, ignore_errors=True)
    return cible


# ── Carton de chapitre ───────────────────────────────────────────────────────
def _image_carton(t: float, fond, numero: int, titre: str, duree: float) -> Image.Image:
    frame = fond.copy()
    fondre(frame, balayage(rampe(t, 0.0, duree * 0.9), (W, H)), 0.45)

    p = rampe(t, 0.05, 0.4, sortie_elastique)
    couche = Image.new("RGBA", (W, H), (0, 0, 0, 0))
    d = ImageDraw.Draw(couche)
    rayon = int(64 * p)
    cx, cy = int(W * 0.34), H // 2
    d.ellipse((cx - rayon, cy - rayon, cx + rayon, cy + rayon), fill=BLANC + (255,))
    if p > 0.6:
        texte_centre(couche, f"{numero:02d}", police(True, 54), BLEU, cx, cy)
    fondre(frame, couche, 1.0)

    p = rampe(t, 0.25, 0.5)
    if p > 0:
        couche = Image.new("RGBA", (W, H), (0, 0, 0, 0))
        fnt = ajustee(True, 66, titre, int(W * 0.5))
        ImageDraw.Draw(couche).text((int(W * 0.42) + int(40 * (1 - p)), H // 2),
                                    titre, font=fnt, fill=BLANC + (255,), anchor="lm")
        fondre(frame, couche, p)

    sortie = rampe(t, duree - 0.35, 0.35)
    if sortie > 0:
        fondre(frame, Image.new("RGBA", (W, H), FOND + (255,)), sortie)
    return frame


def rendre_carton(numero: int, titre: str, cible: Path,
                  duree: float = CARTON_S) -> Path:
    travail = cible.parent / f"_carton{numero}"
    shutil.rmtree(travail, ignore_errors=True)
    travail.mkdir(parents=True)
    fond = fond_carton((W, H), "intro")
    for i in range(int(duree * FPS)):
        _image_carton(i / FPS, fond, numero, titre, duree).convert("RGB").save(
            travail / f"f{i:04d}.png")
    encoder(travail, "f%04d.png", cible)
    shutil.rmtree(travail, ignore_errors=True)
    return cible


# ── Fin ──────────────────────────────────────────────────────────────────────
def _image_fin(t: float, fond, logo, suivant: str, duree: float) -> Image.Image:
    frame = fond.copy()
    fondre(frame, balayage(rampe(t, 0.1, 3.0), (W, H)), 0.4)

    p = rampe(t, 0.0, 0.5)
    if p > 0:
        couche = Image.new("RGBA", (W, H), (0, 0, 0, 0))
        couche.alpha_composite(logo, (W // 2 - logo.width // 2,
                                      int(H * 0.20) - logo.height // 2))
        fondre(frame, couche, p)

    p = rampe(t, 0.35, 0.55)
    if p > 0:
        couche = Image.new("RGBA", (W, H), (0, 0, 0, 0))
        texte_centre(couche, "Essayez RapidoCMS", police(True, 82), BLANC,
                     W // 2, int(H * 0.46) + int(28 * (1 - p)), ombre=True)
        fondre(frame, couche, p)

    p = rampe(t, 0.8, 0.5)
    if p > 0:
        couche = Image.new("RGBA", (W, H), (0, 0, 0, 0))
        pastille(couche, URL_APP, police(True, 40), W // 2, int(H * 0.60),
                 BLANC, BLEU_SOMBRE, marge_x=44, marge_y=22)
        fondre(frame, couche, p)

    if suivant:
        p = rampe(t, 1.4, 0.6)
        if p > 0:
            couche = Image.new("RGBA", (W, H), (0, 0, 0, 0))
            texte_centre(couche, "Prochaine vidéo", police(True, 28), BLEU_CLAIR,
                         W // 2, int(H * 0.735))
            fnt = ajustee(True, 46, suivant, W - 2 * MARGE - 200)
            texte_centre(couche, suivant, fnt, BLANC, W // 2, int(H * 0.795))
            fondre(frame, couche, p)

    p = rampe(t, 2.1, 0.5)
    if p > 0:
        couche = Image.new("RGBA", (W, H), (0, 0, 0, 0))
        texte_centre(couche, f"Tous les tutoriels · {URL_ACADEMIE}",
                     police(False, 28), BLANC, W // 2, int(H * 0.90))
        fondre(frame, couche, p * 0.9)
    return frame


def rendre_fin(cible: Path, suivant: str = "", duree: float = FIN_S) -> Path:
    travail = cible.parent / "_fin"
    shutil.rmtree(travail, ignore_errors=True)
    travail.mkdir(parents=True)
    fond = fond_carton((W, H), "outro")
    logo = logo_redimensionne(190)
    for i in range(int(duree * FPS)):
        _image_fin(i / FPS, fond, logo, suivant, duree).convert("RGB").save(
            travail / f"f{i:04d}.png")
    encoder(travail, "f%04d.png", cible)
    shutil.rmtree(travail, ignore_errors=True)
    return cible


# ── Calques fixes d'un plan ──────────────────────────────────────────────────
def bandeaux(titre_chapitre: str, numero_chapitre: int, sous_titre: str,
             numero_tutoriel: int | None, dossier: Path, cle: str) -> dict[str, Path]:
    """Produit les trois calques d'un plan : cadre, bandeau de chapitre, sous-titre.

    Le cadre (bandeau haut blanc + bande basse bleue) est fixe ; le bandeau de
    chapitre et le sous-titre sont séparés pour pouvoir être animés à l'entrée.
    """
    dossier.mkdir(parents=True, exist_ok=True)
    sorties: dict[str, Path] = {}

    # 1. Le cadre : bandeau haut blanc, filet bleu, bande basse bleue.
    cadre = Image.new("RGBA", (W, H), (0, 0, 0, 0))
    d = ImageDraw.Draw(cadre)
    d.rectangle((0, 0, W, BANDE_HAUT), fill=BLANC + (255,))
    d.rectangle((0, BANDE_HAUT - 5, W, BANDE_HAUT), fill=BLEU + (255,))
    d.rectangle((0, H - BANDE_BAS, W, H), fill=BLEU + (255,))
    logo = logo_redimensionne(64)
    cadre.alpha_composite(logo, (MARGE, (BANDE_HAUT - 5 - logo.height) // 2))
    d.text((MARGE + logo.width + 22, (BANDE_HAUT - 5) // 2), "RapidoCMS",
           font=police(True, 34), fill=BLEU + (255,), anchor="lm")
    d.text((MARGE + logo.width + 22, (BANDE_HAUT - 5) // 2 + 30), "Académie",
           font=police(False, 20), fill=GRIS + (200,), anchor="lm")
    if numero_tutoriel is not None:
        pastille(cadre, f"TUTORIEL {numero_tutoriel:02d}", police(True, 22),
                 W - MARGE - 110, (BANDE_HAUT - 5) // 2, FOND, BLEU,
                 marge_x=26, marge_y=12)
    sorties["cadre"] = dossier / f"{cle}-cadre.png"
    cadre.save(sorties["cadre"])

    # 2. Le bandeau de chapitre, posé sur le haut de la capture.
    banniere = Image.new("RGBA", (W, H), (0, 0, 0, 0))
    if titre_chapitre:
        etiquette = f"{numero_chapitre} · {titre_chapitre}"
        fnt = ajustee(True, 34, etiquette, int(W * 0.62))
        dd = ImageDraw.Draw(banniere)
        tw = dd.textlength(etiquette, font=fnt)
        x0, y0 = MARGE, BANDE_HAUT + 30
        x1, y1 = x0 + tw + 76, y0 + 68
        dd.rounded_rectangle((x0, y0, x1, y1), radius=34, fill=BLEU + (250,))
        dd.text((x0 + 38, (y0 + y1) // 2), etiquette, font=fnt,
                fill=BLANC + (255,), anchor="lm")
    sorties["banniere"] = dossier / f"{cle}-banniere.png"
    banniere.save(sorties["banniere"])

    # 3. Le sous-titre, dans la bande basse.
    couche = Image.new("RGBA", (W, H), (0, 0, 0, 0))
    if sous_titre:
        fnt = police(True, 40)
        lignes = decouper(sous_titre, fnt, W - 2 * MARGE - 120)
        if len(lignes) > 2:
            fnt = police(True, 34)
            lignes = decouper(sous_titre, fnt, W - 2 * MARGE - 120)[:2]
        interligne = 46
        depart = H - BANDE_BAS // 2 - (len(lignes) - 1) * interligne // 2
        for i, ligne in enumerate(lignes):
            texte_centre(couche, ligne, fnt, BLANC, W // 2, depart + i * interligne)
    sorties["sous_titre"] = dossier / f"{cle}-soustitre.png"
    couche.save(sorties["sous_titre"])
    return sorties


def medaillon(pose: str, dossier: Path, cle: str, taille: int = 300) -> Path:
    """Pastille ronde du présentateur, en bas à droite de la capture."""
    dossier.mkdir(parents=True, exist_ok=True)
    couche = Image.new("RGBA", (W, H), (0, 0, 0, 0))

    disque = Image.new("RGBA", (taille, taille), (0, 0, 0, 0))
    dd = ImageDraw.Draw(disque)
    dd.ellipse((0, 0, taille - 1, taille - 1), fill=BLEU + (255,))
    dd.ellipse((7, 7, taille - 8, taille - 8), fill=FOND + (255,))

    portrait = detourer_pose(pose, int(taille * 1.02))
    masque = Image.new("L", (taille, taille), 0)
    ImageDraw.Draw(masque).ellipse((7, 7, taille - 8, taille - 8), fill=255)
    plaque = Image.new("RGBA", (taille, taille), (0, 0, 0, 0))
    plaque.alpha_composite(portrait, (taille // 2 - portrait.width // 2,
                                      int(taille * 0.06)))
    plaque.putalpha(Image.composite(plaque.getchannel("A"),
                                    Image.new("L", (taille, taille), 0), masque))
    disque.alpha_composite(plaque)

    avec_ombre = ombre_portee(disque, rayon=22, decalage=10, opacite=110)
    x = W - MARGE - avec_ombre.width + 40
    y = H - BANDE_BAS - avec_ombre.height + 30
    couche.alpha_composite(avec_ombre, (x, y))

    chemin = dossier / f"{cle}-medaillon.png"
    couche.save(chemin)
    return chemin


# ── Carte « Version Minute » ─────────────────────────────────────────────────
def carte_version_minute(prompt: str, outil: str, resultat: list[str],
                         cible: Path) -> Path:
    """La même action, demandée en une phrase à Claude via le MCP RapidoCMS.

    La carte occupe la place de la capture (1920 × 855). Elle montre la phrase
    tapée, l'outil réellement appelé — son nom exact, tel que le serveur
    l'expose — et les lignes de sa réponse.
    """
    from .charte import ASSETS, VERT

    cw, ch = W, ECRAN_H
    frame = Image.new("RGBA", (cw, ch), FOND + (255,))
    d = ImageDraw.Draw(frame)

    marge = 96
    # Le bandeau de chapitre du montage occupe le haut-gauche de cette zone :
    # la carte commence donc sous lui, et sa mention de droite reste libre.
    d.text((cw - marge, 62), "la même chose, en une phrase, dans Claude",
           font=police(False, 27), fill=GRIS + (200,), anchor="rm")

    # La phrase tapée.
    fnt = police(False, 34)
    lignes = decouper(prompt, fnt, cw - 2 * marge - 120)
    haut = 118
    hauteur_bulle = 44 + len(lignes) * 46
    d.rounded_rectangle((marge, haut, cw - marge, haut + hauteur_bulle),
                        radius=24, fill=BLANC + (255,))
    d.rounded_rectangle((marge, haut, marge + 8, haut + hauteur_bulle),
                        radius=4, fill=BLEU + (255,))
    for i, ligne in enumerate(lignes):
        d.text((marge + 44, haut + 34 + i * 46), ligne, font=fnt,
               fill=GRIS + (255,), anchor="lt")

    # L'appel d'outil : « MCP RapidoCMS · nom_de_l_outil », d'un seul tenant.
    y = haut + hauteur_bulle + 30
    fnt_source = police(False, 27)
    fnt_outil = police(True, 31)
    prefixe = "MCP RapidoCMS  ·  "
    largeur = (d.textlength(prefixe, font=fnt_source)
               + d.textlength(outil, font=fnt_outil))
    logo_claude = ASSETS / "rapidocms" / "logo-claude.png"
    x = marge
    if logo_claude.exists():
        insigne = Image.open(logo_claude).convert("RGBA")
        ratio = 42 / insigne.height
        insigne = insigne.resize((int(insigne.width * ratio), 42), Image.LANCZOS)
        frame.alpha_composite(insigne, (marge, y + 7))
        x = marge + insigne.width + 20
    d.rounded_rectangle((x, y, x + largeur + 60, y + 58), radius=16,
                        outline=BLEU + (255,), width=3, fill=BLANC + (255,))
    d.text((x + 30, y + 29), prefixe, font=fnt_source, fill=GRIS + (185,), anchor="lm")
    d.text((x + 30 + d.textlength(prefixe, font=fnt_source), y + 29), outil,
           font=fnt_outil, fill=BLEU + (255,), anchor="lm")

    # La réponse : la boîte s'ajuste au nombre de lignes.
    y += 88
    fnt = police(False, 28)
    visibles = [ligne for ligne in resultat[:7]]
    bas = min(ch - 46, y + 40 + max(1, len(visibles)) * 42)
    d.rounded_rectangle((marge, y, cw - marge, bas), radius=24,
                        fill=(0x1B, 0x2A, 0x33) + (255,))
    d.rounded_rectangle((marge, y, marge + 8, bas), radius=4, fill=VERT + (255,))
    for i, ligne in enumerate(visibles):
        d.text((marge + 44, y + 26 + i * 42), ligne, font=fnt,
               fill=(0xD8, 0xEE, 0xF7) + (255,), anchor="lt")

    cible.parent.mkdir(parents=True, exist_ok=True)
    frame.convert("RGB").save(cible)
    return cible


# ── Vignette ─────────────────────────────────────────────────────────────────
def rendre_vignette(titre: str, module: str, numero: int | None,
                    capture: Image.Image | None, pose: str, cible: Path,
                    mot_cle: str = "") -> Path:
    """Miniature 1280 × 720 : titre sur trois lignes, capture, présentateur."""
    vw, vh = 1280, 720
    frame = degrade_vertical(vw, vh, [BLEU_CLAIR, BLEU, BLEU_SOMBRE]).convert("RGBA")
    frame.alpha_composite(halo(int(vw * 0.18), int(vh * 0.20), 380, BLANC, 0.20, (vw, vh)))
    frame.alpha_composite(halo(int(vw * 0.88), int(vh * 0.86), 300, BLEU_CLAIR, 0.28, (vw, vh)))

    if capture is not None:
        vue = capture.copy()
        ratio = 620 / vue.width
        vue = vue.resize((620, max(1, int(vue.height * ratio))), Image.LANCZOS)
        vue = coins_arrondis(vue.convert("RGBA"), 18)
        cadre = ombre_portee(vue, rayon=30, decalage=16, opacite=120)
        frame.alpha_composite(cadre, (vw - cadre.width + 40, vh - cadre.height - 8))

    portrait = detourer_pose(pose, 470)
    frame.alpha_composite(ombre_portee(portrait, rayon=26, decalage=12, opacite=120),
                          (vw - 470, vh - 470 - 30))

    d = ImageDraw.Draw(frame)
    y = 92
    if numero is not None:
        pastille(frame, f"TUTORIEL {numero:02d}", police(True, 24), 60 + 108, y,
                 BLANC, BLEU_SOMBRE, marge_x=24, marge_y=12)
        y += 66
    if module:
        d.text((60, y), module.upper(), font=police(True, 24),
               fill=BLEU_CLAIR + (255,), anchor="lt")
        y += 44

    fnt = police(True, 62)
    lignes = decouper(titre, fnt, 690)
    while len(lignes) > 3 and fnt.size > 34:
        fnt = police(True, fnt.size - 4)
        lignes = decouper(titre, fnt, 690)
    for i, ligne in enumerate(lignes[:3]):
        est_cle = bool(mot_cle) and mot_cle.lower() in ligne.lower()
        d.text((60, y + i * (fnt.size + 14)), ligne, font=fnt,
               fill=(BLANC if est_cle else (0xE6, 0xF7, 0xFF)) + (255,), anchor="lt")

    logo = logo_redimensionne(72)
    frame.alpha_composite(logo, (60, vh - 108))
    d.text((60 + logo.width + 18, vh - 76), "Académie RapidoCMS",
           font=police(True, 28), fill=BLANC + (255,), anchor="lm")

    cible.parent.mkdir(parents=True, exist_ok=True)
    frame.convert("RGB").save(cible, quality=94)
    return cible
