#!/usr/bin/env python3
"""Charte RapidoCMS Académie — tokens, polices et primitives de composition.

Seule source des couleurs et des mesures de l'habillage. Les gabarits
(`habillage.py`) et le montage (`montage.py`) n'en redéfinissent aucune.

La charte est celle de RapidoCMS : bleu primaire #03A9F5 en dominante, gris
#383838 pour le texte, fond clair #F2F4F7, vert #4CAF50 réservé aux
confirmations positives, Arial pour la typographie (Liberation Sans, qui en
reprend les métriques, sur les machines de rendu).
"""

from __future__ import annotations

import math
import shutil
import subprocess
from pathlib import Path

from PIL import Image, ImageDraw, ImageFilter, ImageFont

RACINE = Path(__file__).resolve().parent.parent
DEPOT = RACINE.parent.parent
ASSETS = DEPOT / "assets"
LOGO = ASSETS / "rapidocms" / "logo-rapidocms-hd.png"
LOGO_ORIGAMI = ASSETS / "rapidocms" / "logo-rapidosoftware-origami.jpg"
POSES = ASSETS / "avatar" / "poses"

# ── Couleurs ─────────────────────────────────────────────────────────────────
BLEU = (0x03, 0xA9, 0xF5)          # primaire — titres, flèches, cartons, CTA
BLEU_SOMBRE = (0x02, 0x74, 0xAB)   # ombres et dégradés du bleu primaire
BLEU_CLAIR = (0x5F, 0xCD, 0xFF)    # éclats et surbrillances
GRIS = (0x38, 0x38, 0x38)          # texte
FOND = (0xF2, 0xF4, 0xF7)          # fond clair de l'application
VERT = (0x4C, 0xAF, 0x50)          # confirmations positives uniquement
BLANC = (255, 255, 255)
NOIR_DOUX = (0x11, 0x1B, 0x21)

# ── Formats ──────────────────────────────────────────────────────────────────
W, H = 1920, 1080                  # master 16:9
W9, H9 = 1080, 1920                # short 9:16
FPS = 30

BANDE_HAUT = 112                   # bandeau de marque
BANDE_BAS = 113                    # bande de sous-titres
ECRAN_H = H - BANDE_HAUT - BANDE_BAS   # 855 — hauteur de la capture

# Zone utile de la capture source : les bandeaux d'origine sont retirés.
SRC_W, SRC_H = 1280, 720
SRC_CROP = "crop=1280:570:0:72"

MARGE = 64

# Détourage des poses : seuil du blanc de studio, et érosion qui casse les
# ponts d'ombre pâle entre le sujet et les artefacts du fond.
SEUIL_BLANC = 240
EROSION = 3

POLICES = Path("/usr/share/fonts/truetype/liberation")
REGULIER = POLICES / "LiberationSans-Regular.ttf"
GRAS = POLICES / "LiberationSans-Bold.ttf"


def police(gras: bool, taille: int) -> ImageFont.FreeTypeFont:
    return ImageFont.truetype(str(GRAS if gras else REGULIER), taille)


def ajustee(gras: bool, taille: int, texte: str, largeur_max: int) -> ImageFont.FreeTypeFont:
    """La plus grande taille, sous `taille`, qui tient dans `largeur_max`."""
    sonde = ImageDraw.Draw(Image.new("L", (1, 1)))
    while taille > 14 and sonde.textlength(texte, font=police(gras, taille)) > largeur_max:
        taille -= 2
    return police(gras, taille)


def decouper(texte: str, fnt: ImageFont.FreeTypeFont, largeur_max: int) -> list[str]:
    sonde = ImageDraw.Draw(Image.new("L", (1, 1)))
    lignes, courante = [], ""
    for mot in texte.split():
        essai = f"{courante} {mot}".strip()
        if sonde.textlength(essai, font=fnt) <= largeur_max:
            courante = essai
        else:
            if courante:
                lignes.append(courante)
            courante = mot
    if courante:
        lignes.append(courante)
    return lignes


# ── Outils ffmpeg ────────────────────────────────────────────────────────────
def ffmpeg() -> str:
    return shutil.which("ffmpeg") or __import__("imageio_ffmpeg").get_ffmpeg_exe()


def lancer(args: list[str]) -> None:
    subprocess.run(args, check=True)


def duree_de(chemin: Path) -> float:
    proc = subprocess.run([ffmpeg(), "-hide_banner", "-i", str(chemin)],
                          capture_output=True, text=True)
    for ligne in proc.stderr.splitlines():
        if "Duration:" in ligne:
            horloge = ligne.split("Duration:")[1].split(",")[0].strip()
            h, m, s = horloge.split(":")
            return int(h) * 3600 + int(m) * 60 + float(s)
    raise RuntimeError(f"durée introuvable pour {chemin}")


def encoder(dossier: Path, motif: str, cible: Path, fps: int = FPS) -> Path:
    """Encode une séquence d'images en H.264 High / yuv420p, sans son."""
    cible.parent.mkdir(parents=True, exist_ok=True)
    lancer([ffmpeg(), "-y", "-loglevel", "error",
            "-framerate", str(fps), "-i", str(dossier / motif),
            "-c:v", "libx264", "-profile:v", "high", "-pix_fmt", "yuv420p",
            "-crf", "18", "-movflags", "+faststart", str(cible)])
    return cible


# ── Courbes d'animation ──────────────────────────────────────────────────────
def sortie_cubique(t: float) -> float:
    return 1 - (1 - t) ** 3


def sortie_elastique(t: float) -> float:
    c1, c3 = 1.70158, 2.70158
    return 1 + c3 * (t - 1) ** 3 + c1 * (t - 1) ** 2


def rampe(maintenant: float, debut: float, duree: float, courbe=sortie_cubique) -> float:
    """Avancement 0 → 1 d'une entrée qui démarre à `debut` et dure `duree`."""
    if duree <= 0:
        return 1.0
    return courbe(min(max((maintenant - debut) / duree, 0.0), 1.0))


# ── Composition ──────────────────────────────────────────────────────────────
def degrade_vertical(largeur: int, hauteur: int, etapes) -> Image.Image:
    grad = Image.new("RGB", (1, hauteur))
    px = grad.load()
    portee = len(etapes) - 1
    for y in range(hauteur):
        pos = (y / max(hauteur - 1, 1)) * portee
        i = min(int(pos), portee - 1)
        f = pos - i
        a, b = etapes[i], etapes[i + 1]
        px[0, y] = tuple(round(a[c] + (b[c] - a[c]) * f) for c in range(3))
    return grad.resize((largeur, hauteur), Image.BILINEAR)


def halo(cx: int, cy: int, rayon: int, couleur, force: float,
         taille: tuple[int, int]) -> Image.Image:
    masque = Image.new("L", taille, 0)
    ImageDraw.Draw(masque).ellipse((cx - rayon, cy - rayon, cx + rayon, cy + rayon),
                                   fill=int(255 * force))
    masque = masque.filter(ImageFilter.GaussianBlur(rayon * 0.5))
    couche = Image.new("RGB", taille, couleur)
    couche.putalpha(masque)
    return couche


def fondre(base: Image.Image, couche: Image.Image, opacite: float) -> None:
    if opacite <= 0.001:
        return
    if opacite < 0.999:
        couche = couche.copy()
        couche.putalpha(couche.getchannel("A").point(lambda v: int(v * opacite)))
    base.alpha_composite(couche)


def balayage(offset: float, taille: tuple[int, int]) -> Image.Image:
    """Bande de lumière oblique, de gauche à droite."""
    lw, lh = taille
    bande = Image.new("L", taille, 0)
    d = ImageDraw.Draw(bande)
    x = int(-lw + offset * (2.2 * lw))
    d.polygon([(x, lh), (x + 260, lh), (x + 260 + 420, 0), (x + 420, 0)], fill=70)
    bande = bande.filter(ImageFilter.GaussianBlur(80))
    couche = Image.new("RGB", taille, BLANC)
    couche.putalpha(bande)
    return couche


def fond_carton(taille: tuple[int, int], sens: str = "intro") -> Image.Image:
    """Fond bleu profond des cartons d'ouverture, de chapitre et de fin."""
    lw, lh = taille
    etapes = [BLEU_CLAIR, BLEU, BLEU_SOMBRE]
    if sens != "intro":
        etapes = list(reversed(etapes))
    bg = degrade_vertical(lw, lh, etapes).convert("RGBA")
    bg.alpha_composite(halo(int(lw * 0.22), int(lh * 0.24), int(lw * 0.42), BLANC, 0.18, taille))
    bg.alpha_composite(halo(int(lw * 0.84), int(lh * 0.78), int(lw * 0.34), BLEU_CLAIR, 0.26, taille))
    bruit = Image.effect_noise(taille, 7).convert("L").point(lambda v: 128 + (v - 128) // 12)
    return Image.blend(bg, Image.merge("RGBA", (bruit, bruit, bruit, bg.getchannel("A"))), 0.04)


def logo_redimensionne(hauteur: int) -> Image.Image:
    src = Image.open(LOGO).convert("RGBA")
    ratio = hauteur / src.height
    return src.resize((max(1, int(src.width * ratio)), hauteur), Image.LANCZOS)


def texte_centre(couche: Image.Image, texte: str, fnt, couleur, cx: int, cy: int,
                 ombre: bool = False) -> None:
    if ombre:
        sh = Image.new("RGBA", couche.size, (0, 0, 0, 0))
        ImageDraw.Draw(sh).text((cx, cy + 5), texte, font=fnt,
                                fill=(2, 60, 92, 120), anchor="mm")
        couche.alpha_composite(sh.filter(ImageFilter.GaussianBlur(12)))
    ImageDraw.Draw(couche).text((cx, cy), texte, font=fnt,
                                fill=tuple(couleur) + (255,), anchor="mm")


def pastille(couche: Image.Image, texte: str, fnt, cx: int, cy: int,
             fond, avant, marge_x: int = 34, marge_y: int = 16) -> tuple[int, int]:
    d = ImageDraw.Draw(couche)
    tw = d.textlength(texte, font=fnt)
    boite = fnt.getbbox("Hg")
    th = boite[3] - boite[1]
    x0, y0 = cx - tw / 2 - marge_x, cy - th / 2 - marge_y
    x1, y1 = cx + tw / 2 + marge_x, cy + th / 2 + marge_y
    d.rounded_rectangle((x0, y0, x1, y1), radius=(y1 - y0) / 2, fill=tuple(fond) + (255,))
    d.text((cx, cy), texte, font=fnt, fill=tuple(avant) + (255,), anchor="mm")
    return int(x1 - x0), int(y1 - y0)


def coins_arrondis(image: Image.Image, rayon: int) -> Image.Image:
    masque = Image.new("L", image.size, 0)
    ImageDraw.Draw(masque).rounded_rectangle((0, 0, image.width - 1, image.height - 1),
                                            radius=rayon, fill=255)
    sortie = image.convert("RGBA")
    sortie.putalpha(masque)
    return sortie


def ombre_portee(image: Image.Image, rayon: int = 26, decalage: int = 14,
                 opacite: int = 90) -> Image.Image:
    """Renvoie `image` posée sur son ombre, sur un calque un peu plus grand."""
    marge = rayon * 2 + decalage
    toile = Image.new("RGBA", (image.width + marge * 2, image.height + marge * 2), (0, 0, 0, 0))
    ombre = Image.new("RGBA", image.size, (0, 0, 0, 0))
    ombre.paste((2, 60, 92, opacite), (0, 0), image.getchannel("A"))
    toile.alpha_composite(ombre.filter(ImageFilter.GaussianBlur(rayon)), (marge, marge + decalage))
    toile.alpha_composite(image, (marge, marge))
    return toile


def detourer_pose(nom: str, hauteur: int) -> Image.Image:
    """Détoure une pose du présentateur de son fond blanc.

    Les photos sont sur fond blanc uniforme. Seuiller la luminance ne suffit
    pas : la chemise blanche du présentateur passe le seuil comme le fond et se
    troue. On procède donc dans l'autre sens — le fond est la zone claire qui
    **touche le bord** de l'image, et tout le reste est le sujet, chemise
    comprise. Une dernière passe ne garde que la plus grosse tache connexe, ce
    qui écarte la pastille d'IA en bas à droite de certains clichés.
    """
    import numpy as np

    src = Image.open(POSES / f"pose-{nom}.png").convert("RGB")
    petit = src.resize((src.width // 2, src.height // 2), Image.BILINEAR)
    arr = np.asarray(petit, dtype=np.int16)
    clair = (arr.min(axis=2) >= SEUIL_BLANC) & (arr.max(axis=2) - arr.min(axis=2) <= 10)

    hauteur_p, largeur_p = clair.shape

    def propager(depart, praticable):
        """Propagation en largeur depuis `depart`, sur les cases praticables."""
        atteint = np.zeros_like(praticable, dtype=bool)
        pile = [p for p in depart if praticable[p[0], p[1]]]
        for y, x in pile:
            atteint[y, x] = True
        while pile:
            y, x = pile.pop()
            for dy, dx in ((1, 0), (-1, 0), (0, 1), (0, -1)):
                ny, nx = y + dy, x + dx
                if 0 <= ny < hauteur_p and 0 <= nx < largeur_p \
                        and praticable[ny, nx] and not atteint[ny, nx]:
                    atteint[ny, nx] = True
                    pile.append((ny, nx))
        return atteint

    bord = ([(0, x) for x in range(largeur_p)]
            + [(hauteur_p - 1, x) for x in range(largeur_p)]
            + [(y, 0) for y in range(hauteur_p)]
            + [(y, largeur_p - 1) for y in range(hauteur_p)])
    fond = propager(bord, clair)
    sujet = ~fond

    # Une ombre de studio très pâle passe parfois sous le seuil et relie le
    # sujet à un artefact du fond — la pastille d'IA de certains clichés, par
    # exemple. On érode donc avant de chercher la composante principale : les
    # ponts d'un ou deux pixels cassent, la silhouette non. On redilate ensuite
    # dans les limites du masque d'origine, pour ne pas ronger les contours.
    def eroder(masque, passes):
        for _ in range(passes):
            garde = masque.copy()
            garde[1:, :] &= masque[:-1, :]
            garde[:-1, :] &= masque[1:, :]
            garde[:, 1:] &= masque[:, :-1]
            garde[:, :-1] &= masque[:, 1:]
            masque = garde
        return masque

    def dilater(masque, passes):
        for _ in range(passes):
            large = masque.copy()
            large[1:, :] |= masque[:-1, :]
            large[:-1, :] |= masque[1:, :]
            large[:, 1:] |= masque[:, :-1]
            large[:, :-1] |= masque[:, 1:]
            masque = large
        return masque

    noyau = eroder(sujet, EROSION)
    vus = np.zeros_like(noyau, dtype=bool)
    meilleure = None
    for y0 in range(0, hauteur_p, 2):
        for x0 in range(0, largeur_p, 2):
            if not noyau[y0, x0] or vus[y0, x0]:
                continue
            tache = propager([(y0, x0)], noyau & ~vus)
            vus |= tache
            if meilleure is None or tache.sum() > meilleure.sum():
                meilleure = tache
    if meilleure is None:
        meilleure = sujet
    else:
        meilleure = dilater(meilleure, EROSION + 1) & sujet
    masque_p = np.zeros_like(sujet, dtype=np.uint8)
    masque_p[meilleure] = 255

    masque = Image.fromarray(masque_p, "L").resize(src.size, Image.BILINEAR)
    masque = masque.filter(ImageFilter.GaussianBlur(1.6)).point(lambda v: 255 if v > 120 else v * 2)
    decoupe = src.convert("RGBA")
    decoupe.putalpha(masque)
    decoupe = decoupe.crop(decoupe.getchannel("A").getbbox())
    ratio = hauteur / decoupe.height
    return decoupe.resize((max(1, int(decoupe.width * ratio)), hauteur), Image.LANCZOS)


def fleche(couche: Image.Image, depart: tuple[int, int], arrivee: tuple[int, int],
           couleur=BLEU, epaisseur: int = 9) -> None:
    """Flèche droite de la charte, avec sa pointe pleine."""
    d = ImageDraw.Draw(couche)
    x0, y0 = depart
    x1, y1 = arrivee
    angle = math.atan2(y1 - y0, x1 - x0)
    corps = 34
    bx, by = x1 - corps * math.cos(angle), y1 - corps * math.sin(angle)
    d.line((x0, y0, bx, by), fill=tuple(couleur) + (255,), width=epaisseur)
    aile = 20
    d.polygon([
        (x1, y1),
        (bx - aile * math.sin(angle), by + aile * math.cos(angle)),
        (bx + aile * math.sin(angle), by - aile * math.cos(angle)),
    ], fill=tuple(couleur) + (255,))
