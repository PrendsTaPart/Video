#!/usr/bin/env python3
"""Refabrique le sting B/C — le carton « LE PROBLÈME » commun aux 337 épisodes.

    python3 scripts/build-sting-BC.py --nombre huit --vo assets/vo/fixed/VO_BC_huit.mp3

Le rendu livré `templates/COMMUN_sting_BC.mp4` n'a aucune source dans le dépôt :
il a été produit ailleurs et déposé tel quel. Ce script le refait à partir du
rendu lui-même, en ne changeant que ce qui doit changer — le mot du titre et le
nombre d'icônes — et en gardant à l'identique tout le reste : l'animation de
logo d'ouverture, le badge, le fond, le lit musical, les positions et les
fondus.

Tout ce qui est codé ici a été relevé sur le rendu d'origine, pas deviné :

  géométrie (1080 × 1920)      badge          x801-1039  y60-149
                               LE PROBLÈME    h49  w215   centré, haut 470
                               titre          h91  w515   centré, haut 545
                               grille         pastilles 150, gouttière 24
                                              lignes hautes 720 et 894
                               1 000 € / MOIS h76  w579   centré, haut 1120
                               ET AUCUN...    h53  w503   centré, haut 1260

  police                       Anton — retrouvée par métrique : à hauteur de
                               capitale égale, elle rend « DIX LOGICIELS » en
                               517 px contre 515 mesurés (0,4 % d'écart), et
                               les trois autres lignes à moins de 1 %.

  couleurs                     fond #FAF6E3 · sur-titre #0279FB
                               titre et dernière ligne #0E1820 · prix #FDA300

  minutage (30 i/s)            0,000  animation de logo (reprise telle quelle)
                               2,233  LE PROBLÈME, fondu 0,233 s
                               2,300  titre, fondu 0,233 s
                               2,467  première pastille, une toutes les 0,133 s,
                                      fondu 0,100 s chacune
                               4,600  1 000 € PAR MOIS, fondu 0,233 s
                               7,100  ET AUCUN NE SE PARLE, fondu 0,233 s
                               9,000  fin — durée à ne pas bouger, les masters
                                      valent 37,5 s et le sting en tient 9

  bande-son                    templates/bgm.mp3 à partir de 3,18181 s,
                               gain 0,2867 (−10,85 dB) ; ce calage explique
                               88,9 % de l'énergie du sting d'origine.
                               La voix est incrustée dans le rendu : elle se
                               reconstruit, elle ne s'enlève pas. Elle entre à
                               0,900 s et sort à 8,320 s (7,42 s utiles), remontée
                               de 1,75 pour retomber sur −21,7 LUFS intégrés.

Les icônes ne sont pas redessinées : elles sont découpées dans le rendu
d'origine, à l'image de fin. Une pastille reste donc au pixel près celle qui
est déjà publiée.

⚠️ Passer de dix à huit logiciels retire deux pastilles. Le choix des deux est
éditorial : `--icones` prend la liste, dans l'ordre d'affichage.
"""

import argparse
import json
import subprocess
import sys
from pathlib import Path

import numpy as np
from PIL import Image, ImageDraw, ImageFont

RACINE = Path(__file__).resolve().parent.parent
ORIGINAL = RACINE / "templates" / "COMMUN_sting_BC.mp4"
BGM = RACINE / "templates" / "bgm.mp3"
ANTON = RACINE / "templates" / "Anton-Regular.ttf"

L, H = 1080, 1920
FPS = 30
DUREE = 9.0
FOND = (250, 246, 227)

BLEU = (2, 121, 251)
ENCRE = (14, 24, 32)
OR = (253, 163, 0)

# ligne : (texte, taille Anton, interlettre, haut de capitale, couleur, début, fondu)
LIGNES_FIXES = [
    ("LE PROBLÈME", 44, 0, 470, BLEU, 2.233, 0.233),
    ("1 000 € PAR MOIS", 86, 1, 1120, OR, 4.600, 0.233),
    ("ET AUCUN NE SE PARLE", 62, 0, 1260, ENCRE, 7.100, 0.233),
]
TITRE = (104, 0, 545, ENCRE, 2.300, 0.233)

PASTILLE = 150
GOUTTIERE = 24
LIGNES_GRILLE = (720, 894)
GRILLE_T0 = 2.467
GRILLE_PAS = 0.1333
GRILLE_FONDU = 0.100

PLAQUE_T = 2.200          # dernière image où seul le badge est posé
VOIX_ENTREE = 0.900
BGM_DEPART = 3.18181
BGM_GAIN = 0.2867
# La voix est remontée jusqu'à retrouver le niveau du rendu d'origine :
# −21,7 LUFS intégrés, crête −6,6 dBFS. Le lit, lui, est déjà au bon gain.
VOIX_GAIN = 1.75


def ffmpeg(*args):
    subprocess.run(["ffmpeg", "-hide_banner", "-loglevel", "error", *args], check=True)


def image_a(t, sortie):
    ffmpeg("-ss", f"{t}", "-i", str(ORIGINAL), "-frames:v", "1", str(sortie), "-y")
    return Image.open(sortie).convert("RGB")


def texte_en_calque(txt, taille, interlettre, couleur):
    """Rend le texte et le recadre sur son encre : le haut de capitale est le haut."""
    f = ImageFont.truetype(str(ANTON), taille)
    brut = Image.new("L", (2400, 500), 0)
    d = ImageDraw.Draw(brut)
    x = 100.0
    for ch in txt:
        d.text((x, 100), ch, font=f, fill=255)
        x += d.textlength(ch, font=f) + interlettre
    a = np.asarray(brut)
    ys = np.where(a.any(axis=1))[0]
    xs = np.where(a.any(axis=0))[0]
    masque = brut.crop((int(xs[0]), int(ys[0]), int(xs[-1]) + 1, int(ys[-1]) + 1))
    calque = Image.new("RGBA", masque.size, couleur + (0,))
    calque.putalpha(masque)
    return calque


def decouper_icones(image_finale):
    """Découpe les dix pastilles du rendu d'origine, dans l'ordre d'affichage."""
    pas = PASTILLE + GOUTTIERE
    x0 = (L - (5 * PASTILLE + 4 * GOUTTIERE)) // 2
    icones = []
    for k in range(10):
        r, c = divmod(k, 5)
        x = x0 + pas * c
        y = LIGNES_GRILLE[r]
        icones.append(image_finale.crop((x, y, x + PASTILLE, y + PASTILLE)))
    return icones


def rampe(t, debut, duree):
    if t < debut:
        return 0.0
    if t >= debut + duree:
        return 1.0
    return (t - debut) / duree


def poser(fond, calque, x, y, alpha):
    if alpha <= 0:
        return
    c = calque.copy()
    if alpha < 1:
        a = c.getchannel("A").point(lambda v: int(v * alpha))
        c.putalpha(a)
    fond.paste(c, (int(x), int(y)), c)


def construire(nombre, choix_icones, vo, sortie, travail):
    travail.mkdir(parents=True, exist_ok=True)
    plaque = image_a(PLAQUE_T, travail / "plaque.png")
    finale = image_a(8.5, travail / "finale.png")
    icones = decouper_icones(finale)
    retenues = [icones[i - 1] for i in choix_icones]

    titre_txt = f"{nombre.upper()} LOGICIELS"
    taille, inter, haut, couleur, t_titre, fondu_titre = TITRE
    calque_titre = texte_en_calque(titre_txt, taille, inter, couleur)
    calques = [
        (texte_en_calque(txt, taille, inter, coul), haut, t0, fondu)
        for txt, taille, inter, haut, coul, t0, fondu in LIGNES_FIXES
    ]

    n = len(retenues)
    colonnes = 5 if n > 8 else (n + 1) // 2
    largeur_grille = colonnes * PASTILLE + (colonnes - 1) * GOUTTIERE
    gx0 = (L - largeur_grille) // 2

    images = travail / "images"
    images.mkdir(exist_ok=True)
    for cache in images.glob("*.png"):
        cache.unlink()

    depart = int(round(PLAQUE_T * FPS))
    total = int(round(DUREE * FPS))
    for i in range(depart, total):
        t = i / FPS
        img = plaque.copy()
        poser(img, calque_titre, (L - calque_titre.width) / 2, haut, rampe(t, t_titre, fondu_titre))
        for calque, y, t0, fondu in calques:
            poser(img, calque, (L - calque.width) / 2, y, rampe(t, t0, fondu))
        for k, icone in enumerate(retenues):
            a = rampe(t, GRILLE_T0 + GRILLE_PAS * k, GRILLE_FONDU)
            if a <= 0:
                continue
            r, c = divmod(k, colonnes)
            x, y = gx0 + (PASTILLE + GOUTTIERE) * c, LIGNES_GRILLE[r]
            if a >= 1:
                img.paste(icone, (x, y))
            else:
                img.paste(Image.blend(img.crop((x, y, x + PASTILLE, y + PASTILLE)), icone, a), (x, y))
        img.save(images / f"{i:04d}.png")

    # --- image : les 2,2 s d'ouverture reprises telles quelles, puis le reste ---
    ffmpeg("-i", str(ORIGINAL), "-t", f"{PLAQUE_T}", "-an",
           "-c:v", "libx264", "-preset", "medium", "-crf", "18",
           "-r", str(FPS), "-pix_fmt", "yuv420p", str(travail / "ouverture.mp4"), "-y")
    ffmpeg("-framerate", str(FPS), "-start_number", str(depart),
           "-i", str(images / "%04d.png"), "-an",
           "-c:v", "libx264", "-preset", "medium", "-crf", "18",
           "-r", str(FPS), "-pix_fmt", "yuv420p", str(travail / "corps.mp4"), "-y")
    (travail / "liste.txt").write_text(
        f"file '{travail / 'ouverture.mp4'}'\nfile '{travail / 'corps.mp4'}'\n", encoding="utf-8")
    ffmpeg("-f", "concat", "-safe", "0", "-i", str(travail / "liste.txt"),
           "-c", "copy", str(travail / "image.mp4"), "-y")

    # --- son : lit musical calé, voix posée à son entrée d'origine -------------
    ffmpeg("-ss", f"{BGM_DEPART}", "-i", str(BGM), "-t", f"{DUREE}",
           "-af", f"volume={BGM_GAIN},afade=t=out:st={DUREE - 0.4}:d=0.4",
           "-ac", "2", "-ar", "48000", str(travail / "lit.wav"), "-y")
    ffmpeg("-i", str(vo),
           "-af", f"volume={VOIX_GAIN},adelay={int(VOIX_ENTREE * 1000)}|{int(VOIX_ENTREE * 1000)},apad",
           "-t", f"{DUREE}", "-ac", "2", "-ar", "48000", str(travail / "voix.wav"), "-y")
    ffmpeg("-i", str(travail / "lit.wav"), "-i", str(travail / "voix.wav"),
           "-filter_complex", "[0:a][1:a]amix=inputs=2:duration=first:normalize=0[a]",
           "-map", "[a]", "-ac", "2", "-ar", "48000", str(travail / "mix.wav"), "-y")

    ffmpeg("-i", str(travail / "image.mp4"), "-i", str(travail / "mix.wav"),
           "-map", "0:v", "-map", "1:a", "-c:v", "copy",
           "-c:a", "aac", "-b:a", "192k", "-ar", "48000",
           "-t", f"{DUREE}", str(sortie), "-y")
    return sortie


def main():
    p = argparse.ArgumentParser(description=__doc__, formatter_class=argparse.RawDescriptionHelpFormatter)
    p.add_argument("--nombre", default="huit", help="le mot du titre : huit, dix…")
    p.add_argument("--icones", default="1,2,3,4,5,6,7,8",
                   help="pastilles gardées, numérotées dans l'ordre du rendu d'origine")
    p.add_argument("--vo", required=True, help="voix off de remplacement (mp3/wav)")
    p.add_argument("--sortie", default=str(RACINE / "build" / "COMMUN_sting_BC_huit.mp4"))
    a = p.parse_args()

    choix = [int(x) for x in a.icones.split(",") if x.strip()]
    if not 1 <= len(choix) <= 10 or any(not 1 <= i <= 10 for i in choix):
        sys.exit("--icones : entre 1 et 10 numéros, pris dans 1..10")
    if not ANTON.exists():
        sys.exit(f"police absente : {ANTON}")

    sortie = Path(a.sortie)
    sortie.parent.mkdir(parents=True, exist_ok=True)
    travail = RACINE / "build" / "sting"
    construire(a.nombre, choix, Path(a.vo), sortie, travail)

    duree = subprocess.run(
        ["ffprobe", "-v", "error", "-show_entries", "format=duration", "-of", "csv=p=0", str(sortie)],
        capture_output=True, text=True, check=True).stdout.strip()
    print(json.dumps({"sortie": str(sortie), "duree": duree, "icones": choix,
                      "titre": f"{a.nombre.upper()} LOGICIELS"}, ensure_ascii=False))


if __name__ == "__main__":
    main()
