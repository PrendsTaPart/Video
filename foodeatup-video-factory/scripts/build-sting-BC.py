#!/usr/bin/env python3
"""Refabrique le sting B/C — le carton « LE PROBLÈME » commun aux 337 épisodes.

    python3 scripts/build-sting-BC.py --nombre huit --vo assets/vo/fixed/VO_BC_huit.mp3

Le rendu livré `templates/COMMUN_sting_BC.mp4` n'a aucune source dans le dépôt :
il a été produit ailleurs et déposé tel quel. Ce script le refait à partir du
rendu lui-même, en ne changeant que ce qui doit changer — le mot du titre et le
nombre d'icônes — et en gardant à l'identique tout le reste : l'animation de
logo d'ouverture, le badge, le fond, le lit musical, les positions.

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

  bande-son                    templates/bgm.mp3 à partir de 3,18181 s,
                               gain 0,2867 (−10,85 dB) : ce calage explique
                               88,9 % de l'énergie du sting d'origine. Le lit ne
                               fait pas de fondu de fin — mesuré à 0,92 du
                               niveau plein sur les 200 dernières millisecondes,
                               c'est une coupe franche, et le montage colle le
                               segment D juste derrière.

Le montage ne suit pas des dates absolues : il suit la voix. Les phrases de la
prise sont repérées à l'énergie, puis chaque texte tombe où il tombait sur le
rendu d'origine — mesuré sur la voix isolée du sting (ElevenLabs audio
isolation), qui donne :

    1,85 → 2,33   « Aujourd'hui, »
    2,48 → 4,28   « tu gères ton restaurant avec dix logiciels, »
    4,71 → 5,54   « mille euros par mois »
    5,84 → 6,76   « et aucun ne se parle. »
    7,07 → 8,75   « Tout ça change avec FoodEatUp. »

D'où les écarts repris ici : la voix entre à 1,850 ; « LE PROBLÈME » 0,383 s
après elle ; le titre 0,450 s après ; la première pastille 0,617 s après ; la
dernière finit de paraître 0,510 s avant la fin de la phrase, c'est-à-dire sur
« … logiciels » ; le prix 0,110 s avant « mille euros ».

Deux choix de montage, parce que le rendu d'origine n'est pas régulier sur le
dernier point :

  --calage voix (défaut)   « ET AUCUN NE SE PARLE » tombe sur ses propres mots,
                           comme les trois autres lignes.
  --calage origine         il tombe là où le rendu d'origine le pose, c'est-à-dire
                           1,26 s après la phrase qu'il transcrit, au moment du
                           « Tout ça change avec FoodEatUp ».

La grille s'étale sur toute la fenêtre disponible quel que soit le nombre de
pastilles : le pas vaut la fenêtre divisée par les intervalles. À dix pastilles
et à la voix d'origine, la règle redonne 0,145 s contre 0,133 s mesurés ; à huit,
elle évite le trou d'une grille finie trop tôt.

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

BLEU = (2, 121, 251)
ENCRE = (14, 24, 32)
OR = (253, 163, 0)

FONDU = 0.233             # fondu d'un bloc de texte, mesuré sur le rendu
GRILLE_FONDU = 0.100      # fondu d'une pastille

PASTILLE = 150
GOUTTIERE = 24
LIGNES_GRILLE = (720, 894)

# Écarts relevés sur le rendu d'origine, comptés depuis le début de la parole
# ou depuis la phrase que le texte transcrit (voir le docstring).
VOIX_ENTREE = 1.850
AV_SURTITRE = 0.383
AV_TITRE = 0.450
AV_GRILLE = 0.617
GRILLE_AVANCE_FIN = 0.510   # la dernière pastille finit avant la fin de la phrase
AVANCE_TEXTE = 0.110        # un texte paraît juste avant les mots qu'il porte
ORIGINE_DERNIERE = 0.030    # calage « origine » : après le début de la dernière phrase

PLAQUE_T = 2.200          # dernière image où seul le badge est posé
BGM_DEPART = 3.18181
BGM_GAIN = 0.2867
# Le lit est déjà au bon gain ; c'est la voix qui porte le niveau. Chaque prise
# sort à un niveau différent, donc le gain n'est pas figé : il part d'ici et le
# montage le reprend jusqu'à retomber sur le rendu d'origine, −21,7 LUFS.
VOIX_GAIN = 1.75
CIBLE_LUFS = -21.7


def ffmpeg(*args):
    subprocess.run(["ffmpeg", "-hide_banner", "-loglevel", "error", *args], check=True)


def loudness(chemin):
    """Loudness intégrée, en LUFS."""
    sortie = subprocess.run(
        ["ffmpeg", "-hide_banner", "-nostats", "-i", str(chemin), "-af", "ebur128", "-f", "null", "-"],
        capture_output=True, text=True, check=True).stderr
    resume = sortie.split("Summary")[-1]
    for ligne in resume.splitlines():
        if ligne.strip().startswith("I:"):
            return float(ligne.split()[1])
    raise RuntimeError(f"loudness illisible pour {chemin}")


def image_a(t, sortie):
    ffmpeg("-ss", f"{t}", "-i", str(ORIGINAL), "-frames:v", "1", str(sortie), "-y")
    return Image.open(sortie).convert("RGB")


def phrases(chemin, seuil=0.06, pause_mini=0.12, parole_mini=0.10):
    """Découpe la voix en phrases, à l'énergie. Rendu en secondes depuis le fichier."""
    brut = subprocess.run(
        ["ffmpeg", "-v", "error", "-i", str(chemin), "-ac", "1", "-ar", "48000", "-f", "f32le", "-"],
        capture_output=True, check=True).stdout
    x = np.frombuffer(brut, dtype=np.float32).astype(np.float64)
    pas = 480                                    # 10 ms
    n = len(x) // pas
    e = np.abs(x[:n * pas].reshape(n, pas)).max(axis=1)
    e = np.convolve(e, np.ones(5) / 5, mode="same")
    actif = e > e.max() * seuil

    blocs, debut = [], None
    for i, v in enumerate(actif):
        if v and debut is None:
            debut = i
        elif not v and debut is not None:
            blocs.append((debut / 100, i / 100))
            debut = None
    if debut is not None:
        blocs.append((debut / 100, n / 100))

    fusion = []
    for a, b in blocs:
        if fusion and a - fusion[-1][1] < pause_mini:
            fusion[-1] = (fusion[-1][0], b)
        else:
            fusion.append((a, b))
    return [(a, b) for a, b in fusion if b - a >= parole_mini]


def minutage(chemin_vo, nb_icones, calage):
    """Place chaque élément à partir des phrases de la prise fournie."""
    p = phrases(chemin_vo)
    if len(p) < 4:
        sys.exit(f"voix : {len(p)} phrase(s) repérée(s), il en faut au moins 4 "
                 "(« … huit logiciels » · « mille euros par mois » · "
                 "« et aucun ne se parle » · « tout ça change avec FoodEatUp »)")
    # Les quatre dernières phrases portent le montage ; une prise qui marque un
    # temps après « Aujourd'hui » en compte cinq, comme le rendu d'origine.
    a_debut = p[0][0]
    a_fin, b, c, d = p[-4][1], p[-3][0], p[-2][0], p[-1][0]
    decalage = VOIX_ENTREE - a_debut          # ce qu'on ajoute au fichier de voix

    t = lambda x: x + decalage
    fin_grille = t(a_fin) - GRILLE_AVANCE_FIN - GRILLE_FONDU
    debut_grille = VOIX_ENTREE + AV_GRILLE
    pas = (fin_grille - debut_grille) / max(nb_icones - 1, 1)
    if pas <= 0:
        sys.exit("voix : la première phrase est trop courte pour y étaler la grille")

    derniere = t(c) - AVANCE_TEXTE if calage == "voix" else t(d) + ORIGINE_DERNIERE
    return {
        "decalage_voix": decalage,
        "surtitre": VOIX_ENTREE + AV_SURTITRE,
        "titre": VOIX_ENTREE + AV_TITRE,
        "grille_debut": debut_grille,
        "grille_pas": pas,
        "prix": t(b) - AVANCE_TEXTE,
        "derniere": derniere,
        "phrases": [(round(t(x), 3), round(t(y), 3)) for x, y in p],
    }


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
        icones.append(image_finale.crop((x0 + pas * c, LIGNES_GRILLE[r],
                                         x0 + pas * c + PASTILLE, LIGNES_GRILLE[r] + PASTILLE)))
    return icones


def rampe(t, debut, duree):
    if t < debut:
        return 0.0
    if t >= debut + duree:
        return 1.0
    return (t - debut) / duree


def poser(fond, calque, y, alpha):
    if alpha <= 0:
        return
    c = calque.copy()
    if alpha < 1:
        c.putalpha(c.getchannel("A").point(lambda v: int(v * alpha)))
    fond.paste(c, (int((L - calque.width) / 2), int(y)), c)


def construire(nombre, choix_icones, vo, m, sortie, travail):
    travail.mkdir(parents=True, exist_ok=True)
    plaque = image_a(PLAQUE_T, travail / "plaque.png")
    icones = decouper_icones(image_a(8.5, travail / "finale.png"))
    retenues = [icones[i - 1] for i in choix_icones]

    blocs = [
        (texte_en_calque("LE PROBLÈME", 44, 0, BLEU), 470, m["surtitre"]),
        (texte_en_calque(f"{nombre.upper()} LOGICIELS", 104, 0, ENCRE), 545, m["titre"]),
        (texte_en_calque("1 000 € PAR MOIS", 86, 1, OR), 1120, m["prix"]),
        (texte_en_calque("ET AUCUN NE SE PARLE", 62, 0, ENCRE), 1260, m["derniere"]),
    ]

    n = len(retenues)
    colonnes = 5 if n > 8 else (n + 1) // 2
    gx0 = (L - (colonnes * PASTILLE + (colonnes - 1) * GOUTTIERE)) // 2

    images = travail / "images"
    images.mkdir(exist_ok=True)
    for vieux in images.glob("*.png"):
        vieux.unlink()

    depart, total = int(round(PLAQUE_T * FPS)), int(round(DUREE * FPS))
    for i in range(depart, total):
        t = i / FPS
        img = plaque.copy()
        for calque, y, t0 in blocs:
            poser(img, calque, y, rampe(t, t0, FONDU))
        for k, icone in enumerate(retenues):
            a = rampe(t, m["grille_debut"] + m["grille_pas"] * k, GRILLE_FONDU)
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

    # --- son : lit à niveau constant, coupe franche à la fin comme l'original ---
    ffmpeg("-ss", f"{BGM_DEPART}", "-i", str(BGM), "-t", f"{DUREE}",
           "-af", f"volume={BGM_GAIN}", "-ac", "2", "-ar", "48000", str(travail / "lit.wav"), "-y")
    retard = max(int(round(m["decalage_voix"] * 1000)), 0)
    gain, mesure = VOIX_GAIN, None
    for _ in range(4):
        ffmpeg("-i", str(vo), "-af", f"volume={gain},adelay={retard}|{retard},apad",
               "-t", f"{DUREE}", "-ac", "2", "-ar", "48000", str(travail / "voix.wav"), "-y")
        ffmpeg("-i", str(travail / "lit.wav"), "-i", str(travail / "voix.wav"),
               "-filter_complex", "[0:a][1:a]amix=inputs=2:duration=first:normalize=0[a]",
               "-map", "[a]", "-ac", "2", "-ar", "48000", str(travail / "mix.wav"), "-y")
        mesure = loudness(travail / "mix.wav")
        ecart = CIBLE_LUFS - mesure
        if abs(ecart) <= 0.2:
            break
        # Seule la voix bouge : le lit tient déjà son niveau d'origine. Le mix
        # ne suit pas la voix décibel pour décibel, d'où la reprise.
        gain *= 10 ** (ecart * 1.35 / 20)
    m["gain_voix"], m["lufs"] = round(gain, 3), mesure

    ffmpeg("-i", str(travail / "image.mp4"), "-i", str(travail / "mix.wav"),
           "-map", "0:v", "-map", "1:a", "-c:v", "copy",
           "-c:a", "aac", "-b:a", "192k", "-ar", "48000",
           "-t", f"{DUREE}", str(sortie), "-y")
    return sortie


def main():
    p = argparse.ArgumentParser(description=__doc__,
                                formatter_class=argparse.RawDescriptionHelpFormatter)
    p.add_argument("--nombre", default="huit", help="le mot du titre : huit, dix…")
    p.add_argument("--icones", default="1,2,3,4,5,6,7,8",
                   help="pastilles gardées, numérotées dans l'ordre du rendu d'origine")
    p.add_argument("--vo", required=True, help="voix off de remplacement (mp3/wav)")
    p.add_argument("--calage", choices=("voix", "origine"), default="voix",
                   help="où tombe « ET AUCUN NE SE PARLE » : sur ses mots, ou là où le rendu d'origine le pose")
    p.add_argument("--sortie", default=str(RACINE / "build" / "COMMUN_sting_BC_huit.mp4"))
    a = p.parse_args()

    choix = [int(x) for x in a.icones.split(",") if x.strip()]
    if not 1 <= len(choix) <= 10 or any(not 1 <= i <= 10 for i in choix):
        sys.exit("--icones : entre 1 et 10 numéros, pris dans 1..10")
    if not ANTON.exists():
        sys.exit(f"police absente : {ANTON}")

    vo = Path(a.vo)
    m = minutage(vo, len(choix), a.calage)
    if m["phrases"][-1][1] > DUREE:
        sys.exit(f"voix : la parole finirait à {m['phrases'][-1][1]:.2f} s, le sting en fait {DUREE}")

    sortie = Path(a.sortie)
    sortie.parent.mkdir(parents=True, exist_ok=True)
    construire(a.nombre, choix, vo, m, sortie, RACINE / "build" / "sting")

    duree = subprocess.run(
        ["ffprobe", "-v", "error", "-show_entries", "format=duration", "-of", "csv=p=0", str(sortie)],
        capture_output=True, text=True, check=True).stdout.strip()
    minutes = ("surtitre", "titre", "grille_debut", "grille_pas", "prix", "derniere")
    print(json.dumps({
        "sortie": str(sortie), "duree": duree, "icones": choix, "calage": a.calage,
        "titre": f"{a.nombre.upper()} LOGICIELS",
        "minutage": {k: round(m[k], 3) for k in minutes},
        "phrases": m["phrases"],
        "son": {"decalage_voix": round(m["decalage_voix"], 3),
                "gain_voix": m["gain_voix"], "lufs": m["lufs"]},
    }, ensure_ascii=False, indent=2))


if __name__ == "__main__":
    main()
