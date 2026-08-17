#!/usr/bin/env python3
"""L'habillage des épisodes UpEatFood : carte d'ouverture et générique de fin.

    # une planche de contrôle, sans rien monter
    python3 scripts/build-habillage.py EP507 --apercu

    # le montage complet : ouverture + plan + générique
    python3 scripts/build-habillage.py EP507 --plan build/story-EP507.mp4 \
        --sortie dist/upeatfood/EP507.mp4

Les épisodes sont lus dans `content/upeatfood.json`, écrit par le site : titre,
place dans le film, décor, vignette. Les options `--titre`, `--plan-du-film`,
`--lieu` et `--vignette` les remplacent au coup par coup.

Ce que l'habillage corrige
--------------------------
**Le titre du générique était mal aligné.** Mesuré au pixel sur EP507 :

    ligne 1 « Six tables, une »  marge gauche 258, marge droite 258
    ligne 2 « mémoire »          marge gauche 350, marge droite 550

Le bloc était centré, mais le texte était composé ferré à gauche À
L'INTÉRIEUR du bloc. Tant qu'une ligne le remplit, l'œil lit « centré » ; dès
qu'une ligne est courte elle pend, ici de deux cents pixels. Chaque ligne est
maintenant centrée sur son propre axe.

**La césure était mauvaise.** « Six tables, une / mémoire » coupe après un
article et laisse un mot seul. On choisit désormais le point de coupe qui
équilibre les deux lignes, et on refuse de couper après un mot-outil.

**L'animation n'existait pas vraiment.** Les quatre éléments montaient
ensemble en un fondu d'opacité entre 0,05 s et 0,30 s, puis plus rien pendant
deux secondes. Ils entrent maintenant décalés, avec une amortie cubique et une
montée, et l'arrivée sur le crème est un fondu croisé plutôt qu'une coupe
franche depuis un plan sombre.

**L'ouverture manquait.** L'épisode commençait sur le plan, sans rien dire de
ce qu'on regardait. Il s'ouvre maintenant sur sa propre affiche — celle que le
site sert déjà — avec le huit de la marque qui se trace en huit pulsations.

Rien n'est généré par une IA : PIL compose, ffmpeg assemble.
"""
import argparse
import json
import math
import pathlib
import shutil
import subprocess
import sys
import tempfile
import urllib.request

from PIL import Image, ImageDraw, ImageFilter, ImageFont

R = pathlib.Path(__file__).resolve().parent.parent
FONTES = R.parent / "videos" / "stories-foodeatup-30j" / "assets" / "fonts"
CATALOGUE = R / "content" / "upeatfood.json"
VIGNETTES = R / "assets" / "vignettes"
PLAQUE = R / "assets" / "generique" / "upeatfood-plaque.mp4"

L, H = 1080, 1920
FPS = 30

FILM = 5.00           # la carte du film, sur la plaque Higgsfield
OUVERTURE = 1.90      # la carte de l'épisode
GENERIQUE = 2.75      # la carte de fin ; le fondu croisé en mange 0,25
FONDU = 0.25

# La charte de l'affiche. Le bleu, le crème et l'orange en sont relevés : la
# carte du film doit être reconnue comme l'affiche, pas comme une variation.
NUIT = (12, 32, 56)
BLEU_AFFICHE = (28, 78, 134)
CREME_AFFICHE = (245, 239, 224)
ORANGE_AFFICHE = (232, 145, 47)

# Relevées au pixel sur l'habillage existant : on ne redéfinit pas la marque,
# on corrige sa mise en page.
CREME = (248, 244, 225)
ENCRE = (15, 24, 35)
BLEU = (35, 140, 249)
ORANGE = (242, 178, 45)
GRIS = (108, 116, 128)

# Un mot sur lequel on ne coupe jamais : la ligne se terminerait sur une
# attente grammaticale, et la deuxième ligne commencerait par sa résolution.
OUTILS = {
    "le", "la", "les", "un", "une", "des", "du", "de", "d'", "l'", "au", "aux",
    "et", "ou", "à", "en", "dans", "sur", "sous", "par", "pour", "que", "qui",
    "ne", "se", "ce", "son", "sa", "ses", "mon", "ma", "mes", "leur", "leurs",
}


def police(poids, taille):
    return ImageFont.truetype(str(FONTES / f"Poppins-{poids}.ttf"), taille)


def largeur(d, texte, font):
    b = d.textbbox((0, 0), texte, font=font)
    return b[2] - b[0]


def espace(texte):
    """Une capitale espacée. Poppins n'a pas d'interlettrage optique en
    capitales : sans cet écart, « UPEATFOOD » se lit comme un seul bloc."""
    return " ".join(texte)


def poser(im, dessiner, opacite):
    """Dessine sur un calque transparent, puis le pose à l'opacité voulue.

    `ImageDraw.text()` IGNORE l'alpha passé dans `fill`, que l'image de base
    soit en RGB ou en RGBA — vérifié dans les deux cas sur cette version de
    Pillow. Un texte demandé à opacité zéro s'écrivait donc parfaitement
    opaque : toute l'animation d'apparition était présente dans le code et
    absente à l'écran.

    Le seul chemin fiable est celui-ci : un calque à part, dessiné à pleine
    opacité, dont on multiplie ENSUITE le canal alpha avant de composer. C'est
    la même mécanique que le filigrane des gabarits d'attente.
    """
    if opacite <= 0.002:
        return im
    calque = Image.new("RGBA", im.size, (0, 0, 0, 0))
    dessiner(ImageDraw.Draw(calque, "RGBA"))
    if opacite < 0.998:
        calque.putalpha(calque.getchannel("A").point(lambda a: int(a * opacite)))
    return Image.alpha_composite(im, calque)


def couper(d, titre, font, maxi):
    """La césure la plus équilibrée qui tienne dans la largeur.

    On essaie chaque point de coupe et on garde celui dont les deux lignes ont
    la différence de largeur la plus faible — c'est ce qui donne le bloc le
    plus stable à l'œil. Couper après un mot-outil est pénalisé lourdement :
    « Six tables, une / mémoire » tient dans la largeur et reste mauvais.
    """
    mots = titre.split()
    if largeur(d, titre, font) <= maxi:
        return [titre]

    meilleur, score_min = None, None
    for i in range(1, len(mots)):
        g, dr = " ".join(mots[:i]), " ".join(mots[i:])
        lg, ld = largeur(d, g, font), largeur(d, dr, font)
        if lg > maxi or ld > maxi:
            continue
        score = abs(lg - ld)
        if mots[i - 1].lower().strip(",;:") in OUTILS:
            score += maxi  # jamais, sauf si c'est la seule coupe possible
        if score_min is None or score < score_min:
            meilleur, score_min = (g, dr), score
    return list(meilleur) if meilleur else [titre]


def ajuster(d, titre, maxi, tailles):
    """La plus grande taille à laquelle le titre tient en deux lignes."""
    for taille in tailles:
        f = police(800, taille)
        lignes = couper(d, titre, f, maxi)
        if len(lignes) <= 2 and all(largeur(d, x, f) <= maxi for x in lignes):
            return f, lignes, taille
    f = police(800, tailles[-1])
    return f, couper(d, titre, f, maxi), tailles[-1]


def amortie(t):
    """Sortie cubique : rapide puis freinée. Le linéaire donne un mouvement
    mécanique qu'on remarque ; celui-ci se pose."""
    t = max(0.0, min(1.0, t))
    return 1 - (1 - t) ** 3


def phase(t, debut, fin):
    return amortie((t - debut) / (fin - debut)) if fin > debut else 0.0


def ligne_centree(im, y, texte, font, couleur, opacite, dy=0.0):
    """Centrée sur SON axe — c'est tout le correctif du générique."""
    def dessiner(d):
        b = d.textbbox((0, 0), texte, font=font)
        x = (L - (b[2] - b[0])) // 2 - b[0]
        d.text((x, y + dy - b[1]), texte, font=font, fill=couleur + (255,))
    return poser(im, dessiner, opacite)


def filet(im, y, demi, opacite, couleur=BLEU, ep=6):
    if demi <= 0:
        return im
    return poser(
        im,
        lambda d: d.rounded_rectangle(
            [L / 2 - demi, y, L / 2 + demi, y + ep], radius=ep // 2,
            fill=couleur + (255,)),
        opacite,
    )


def lockup(im, cx, cy, larg, opacite):
    """« FOOD∞EATUP » : les deux O du mot sont l'anneau double, en orange.

    On le redessine plutôt que de mettre à l'échelle le PNG de 267 px de
    large : à la taille où il devient lisible sur un téléphone, le fichier
    d'origine est déjà flou.
    """
    taille = int(larg * 0.155)
    f = police(800, taille)

    def dessiner(d):
        gauche, droite = "F", "DEATUP"
        lg, ld = largeur(d, gauche, f), largeur(d, droite, f)
        r = taille * 0.30
        ep = max(3, int(taille * 0.085))
        chev = r * 0.52
        lanneaux = 4 * r - chev
        x = cx - (lg + lanneaux + ld) / 2
        b = d.textbbox((0, 0), gauche, font=f)
        y = cy - (b[3] + b[1]) / 2
        d.text((x - b[0], y - b[1]), gauche, font=f, fill=(255, 255, 255, 255))
        x += lg
        for k in range(2):
            cxa = x + r + k * (2 * r - chev)
            d.ellipse([cxa - r, cy - r, cxa + r, cy + r],
                      outline=ORANGE + (255,), width=ep)
        x += lanneaux
        d.text((x - b[0], y - b[1]), droite, font=f, fill=(255, 255, 255, 255))

    return poser(im, dessiner, opacite)


# ─── la carte de fin ────────────────────────────────────────────────────────

def generique(titre, serie, saison, t):
    im = Image.new("RGBA", (L, H), CREME + (255,))
    d = ImageDraw.Draw(im)

    f_titre, lignes, taille = ajuster(d, titre, int(L * 0.78),
                                      (84, 78, 72, 66, 60, 54))
    interligne = int(taille * 1.16)

    # Le bloc est posé un peu au-dessus du centre géométrique : centré au
    # pixel, un bloc de texte paraît toujours trop bas.
    hauteur = len(lignes) * interligne + 106 + 92 + 198 + 74
    y = (H - hauteur) // 2 - 30

    # Le titre part à 0,02 s, pas à 0,10 : le fondu croisé depuis le plan dure
    # 0,25 s, et un titre qui n'entre qu'après laisse voir un quart de seconde
    # de crème vide — un trou au moment précis où l'œil cherche la suite.
    for i, ligne in enumerate(lignes):
        p = phase(t, 0.02 + i * 0.07, 0.46 + i * 0.07)
        im = ligne_centree(im, y, ligne, f_titre, ENCRE, p, dy=(1 - p) * 34)
        y += interligne

    y += 44
    im = filet(im, y, 74 * phase(t, 0.38, 0.66), 1.0)
    y += 62

    p = phase(t, 0.46, 0.80)
    im = ligne_centree(im, y, f"{serie} · saison {saison}", police(700, 34),
                       GRIS, p, dy=(1 - p) * 20)
    y += 92

    p = phase(t, 0.62, 1.00)
    if p > 0:
        larg, haut = 470, 124
        ech = 0.94 + 0.06 * p
        lp, hp = larg * ech, haut * ech
        dy = (1 - p) * 26
        im = poser(im, lambda d: d.rounded_rectangle(
            [L / 2 - lp / 2, y + dy, L / 2 + lp / 2, y + hp + dy],
            radius=int(hp * 0.30), fill=BLEU + (255,)), p)
        im = lockup(im, L / 2, y + hp / 2 + dy, lp, p)
    y += 198

    p = phase(t, 0.80, 1.14)
    im = ligne_centree(im, y, "@FoodEatUp", police(700, 42), ENCRE, p,
                       dy=(1 - p) * 16)

    return im.convert("RGB")


# ─── la carte d'ouverture ───────────────────────────────────────────────────

def fond_vignette(vignette, zoom):
    """La vignette de l'épisode, ramenée à l'état de décor.

    On part de l'affiche que le site sert déjà : c'est la même image partout,
    donc l'ouverture fait reconnaître l'épisode avant qu'un mot soit lu. Mais
    l'affiche porte DÉJÀ son texte incrusté — le titre, « EP507 · CHAPITRE
    7 / 35 », l'accroche entre guillemets. Posée telle quelle, elle
    dédoublerait le nôtre.

    Le flou et l'assombrissement ne sont donc pas décoratifs : ils rendent à
    l'affiche le rôle qu'on lui demande ici, une scène et une lumière. Le
    texte incrusté redevient de la matière, et la carte n'a plus qu'une voix.
    """
    im = Image.open(vignette).convert("RGB")

    # On recadre AVANT de flouter, sur la bande photographique.
    #
    # Le flou seul ne suffisait pas : le bandeau crème du haut porte
    # « UPEATFOOD » en très gros et en très contrasté, et il restait lisible à
    # travers seize pixels de flou — deux fois le même mot, à deux tailles,
    # dans la même carte. Le pavé de bas de page (accroche entre guillemets,
    # logo) posait le même problème en plus discret.
    #
    # Ces deux zones sont au même endroit sur les trente-cinq affiches, parce
    # qu'un seul script les compose. On garde donc la tranche du milieu, celle
    # qui ne porte que la scène.
    haut, bas = int(im.height * 0.15), int(im.height * 0.89)
    im = im.crop((0, haut, im.width, bas))

    k = max(L / im.width, H / im.height) * zoom
    im = im.resize((int(im.width * k) + 1, int(im.height * k) + 1), Image.LANCZOS)
    x, y = (im.width - L) // 2, (im.height - H) // 2
    # Trente-quatre pixels de flou, pas seize. Le recadrage enlève le bandeau
    # du titre, mais l'affiche garde en haut sa ligne de saison et sa pastille
    # « EP507 · CHAPITRE 7 / 35 », et en bas l'accroche entre guillemets. À
    # seize, tout cela se lisait encore et racontait l'épisode une deuxième
    # fois, en plus petit et en désordre. À trente-quatre, il ne reste que la
    # lumière de la scène — c'est-à-dire ce qu'on lui demande.
    im = im.crop((x, y, x + L, y + H)).filter(ImageFilter.GaussianBlur(34))
    im = Image.blend(im, Image.new("RGB", (L, H), (8, 14, 22)), 0.68)

    # Un dégradé qui pèse sur les bords : le texte se pose au centre, et ce
    # qui aurait survécu au recadrage s'enfonce.
    voile = Image.new("L", (1, H))
    for y in range(H):
        r = y / H
        bord = max(0.0, 1 - r / 0.22) if r < 0.22 else max(0.0, (r - 0.80) / 0.20)
        voile.putpixel((0, y), int(150 * min(1.0, bord)))
    im.paste(Image.new("RGB", (L, H), (6, 11, 18)), (0, 0), voile.resize((L, H)))
    return im


def huit(im, cx, cy, r, avance, pulse, opacite):
    """Le huit de FoodEatUp, tracé en deux anneaux.

    `avance` va de 0 à 1 et fait courir le trait ; les deux anneaux se
    dessinent en sens inverse et se rejoignent au centre, ce qui donne au
    signe son mouvement de boucle plutôt qu'un cercle qui se referme.
    """
    ep = max(4, int(r * 0.20))
    chev = r * 0.52
    r = r * (1 + 0.030 * pulse)

    def dessiner(d):
        for k, sens in ((0, -1), (1, 1)):
            cxa = cx + (k * 2 - 1) * (r - chev / 2)
            boite = [cxa - r, cy - r, cxa + r, cy + r]
            etendue = 360 * min(1.0, avance)
            if etendue <= 0:
                continue
            depart = 180 if k == 0 else 0
            # PIL trace toujours dans le sens horaire : pour faire courir le
            # trait à l'envers, on décale l'angle de départ.
            d1 = depart if sens > 0 else depart - etendue
            d.arc(boite, d1, d1 + etendue, fill=ORANGE + (255,), width=ep)

    return poser(im, dessiner, opacite)


def ouverture(ep, t, duree=OUVERTURE):
    # Un très léger recul : l'image se pose au lieu d'être fixe. Au-delà de
    # quatre pour cent le mouvement se voit, et une ouverture qui bouge trop
    # fatigue avant que l'épisode ait commencé.
    im = fond_vignette(ep["vignette"], 1.055 - 0.055 * amortie(t / duree)).convert("RGBA")
    d = ImageDraw.Draw(im)

    cy = int(H * 0.325)
    rayon = int(L * 0.090)
    # Huit pulsations pendant le tracé — la signature de la marque. Elles
    # s'amortissent au lieu de s'arrêter net.
    reste = max(0.0, 1 - max(0.0, t - 1.05) / 0.9)
    im = huit(im, L // 2, cy, rayon, phase(t, 0.10, 1.05),
              math.sin(t * math.pi * 8 / 1.05) * reste, phase(t, 0.06, 0.40))

    y = cy + rayon + 104

    p = phase(t, 0.82, 1.18)
    im = ligne_centree(im, y, espace(ep["serie"].upper()), police(700, 30),
                       (216, 208, 190), p * 0.92, dy=(1 - p) * 16)
    y += 78

    f_titre, lignes, taille = ajuster(d, ep["titre"], int(L * 0.80),
                                      (82, 76, 70, 64, 58, 52))
    for i, ligne in enumerate(lignes):
        p = phase(t, 1.00 + i * 0.08, 1.44 + i * 0.08)
        im = ligne_centree(im, y, ligne, f_titre, (255, 255, 255), p,
                           dy=(1 - p) * 30)
        y += int(taille * 1.14)

    # « Plan 7 / 35 · En salle » dit ce que « EP507 · CHAPITRE 7 / 35 » disait
    # deux fois et mal : le numéro d'épisode est déjà dans le nom du fichier,
    # et « chapitre » n'est pas le mot — un film a des plans. Le décor, lui,
    # manquait, alors que c'est ce qui situe l'épisode dans les quatre actes.
    y += 36
    im = filet(im, y, 64 * phase(t, 1.28, 1.56), 1.0, ep=5)
    y += 56
    p = phase(t, 1.36, 1.72)
    im = ligne_centree(im, y, f"Plan {ep['planDuFilm']} · {ep['lieu']}",
                       police(600, 32), (198, 204, 212), p, dy=(1 - p) * 14)

    return im.convert("RGB")


# ─── la carte du film ───────────────────────────────────────────────────────

def paragraphe(d, texte, font, maxi):
    """Découpe en lignes qui tiennent dans la largeur."""
    lignes, courante = [], ""
    for mot in texte.split():
        essai = f"{courante} {mot}".strip()
        if courante and largeur(d, essai, font) > maxi:
            lignes.append(courante)
            courante = mot
        else:
            courante = essai
    if courante:
        lignes.append(courante)
    return lignes


def fond_affiche():
    """Le bleu de l'affiche, en dégradé vertical."""
    im = Image.new("RGB", (L, H))
    px = im.load()
    for y in range(H):
        r = y / H
        # Plus clair au milieu, où se tient la bande : l'affiche fait la même
        # chose, et c'est ce qui donne à l'image sa profondeur de projection.
        k = 1 - abs(r - 0.42) / 0.58
        c = tuple(int(NUIT[i] + (BLEU_AFFICHE[i] - NUIT[i]) * max(0.0, k) ** 1.6)
                  for i in range(3))
        for x in range(L):
            px[x, y] = c
    return im


def carte_film(ep, t, plaque, duree=FILM):
    """L'affiche du film, animée par-dessus la plaque Higgsfield.

    La plaque est le plan de cinq secondes généré pour cet usage : un pass de
    restaurant vide, la nuit, dont le tiers central a été laissé sombre et
    lisse « pour recevoir la marque au montage ». On la pose en bande
    cinémascope au lieu de la recadrer en 9:16 : recadrée, elle perdait les
    deux tiers de sa largeur et la vapeur qui la fait vivre ; en bande, elle
    garde son cadrage d'origine et le format vertical se lit comme une
    affiche, ce qu'il est.
    """
    im = fond_affiche()

    # La bande, à sa place et à son format.
    bh = int(L * 9 / 16)
    # La bande est posée au tiers haut, pas au sixième : plus haut, le bloc
    # titre-crédits laissait quatre cent cinquante pixels de bleu nu sous
    # lui, soit un quart de la hauteur, et la carte pendait dans le vide.
    by = int(H * 0.215)
    band = plaque.convert("RGB").resize((L, bh), Image.LANCZOS)
    p = phase(t, 0.00, 0.55)
    if p > 0:
        im.paste(Image.blend(Image.new("RGB", (L, bh), (5, 10, 16)), band, p), (0, by))
    im = im.convert("RGBA")

    # Le filet crème qui borde la bande : c'est lui qui la fait lire comme une
    # pellicule et non comme une vidéo posée dans un trou.
    if p > 0.4:
        def bordures(dd):
            dd.rectangle([0, by - 3, L, by - 1], fill=CREME_AFFICHE + (255,))
            dd.rectangle([0, by + bh + 1, L, by + bh + 3], fill=CREME_AFFICHE + (255,))
        im = poser(im, bordures, (p - 0.4) / 0.6)

    d = ImageDraw.Draw(im)

    # 1 · l'accroche de l'affiche
    q = phase(t, 0.20, 0.75)
    im = ligne_centree(im, int(H * 0.108), espace("LE RESTAURANT FAIT SON CINÉMA"),
                       police(600, 27), CREME_AFFICHE, q * 0.95, dy=(1 - q) * 14)

    # 2 · la marque, au centre de la zone réservée
    cyb = by + bh // 2
    reste = max(0.0, 1 - max(0.0, t - 1.75) / 0.8)
    im = huit(im, L // 2, cyb - 40, int(L * 0.062), phase(t, 0.55, 1.75),
              math.sin((t - 0.55) * math.pi * 8 / 1.20) * reste if t > 0.55 else 0,
              phase(t, 0.50, 0.90))
    im = lockup(im, L // 2, cyb + 76, int(L * 0.44), phase(t, 1.30, 1.90))

    # 3 · le titre du film, à l'échelle de l'affiche
    y = by + bh + 118
    q = phase(t, 1.60, 2.30)
    if q > 0:
        f = police(800, int(122 * (1.05 - 0.05 * q)))
        im = ligne_centree(im, y, "UpEatFood", f, CREME_AFFICHE, q, dy=(1 - q) * 18)
    y += 168

    q = phase(t, 2.00, 2.55)
    im = ligne_centree(im, y, "La montée en puissance", police(700, 50),
                       ORANGE_AFFICHE, q, dy=(1 - q) * 16)
    y += 118

    im = filet(im, y, 84 * phase(t, 2.45, 2.85), 1.0, couleur=CREME_AFFICHE, ep=4)
    y += 88

    # 4 · le bloc de crédits, comme le bandeau bas de l'affiche
    credits = [
        (police(700, 30), CREME_AFFICHE,
         "MICHAEL KEBAIL-ALI dans le rôle du chef, du serveur, du patron et du client"),
        (police(600, 28), (198, 214, 232),
         "UN FILM RÉALISÉ PAR FOODEATUP — D'APRÈS DES FAITS RÉELS"),
        (police(600, 28), (198, 214, 232), "35 CHAPITRES · 350 SECONDES"),
    ]
    for i, (f, couleur, texte) in enumerate(credits):
        q = phase(t, 2.70 + i * 0.16, 3.20 + i * 0.16)
        for ligne in paragraphe(d, texte, f, int(L * 0.86)):
            im = ligne_centree(im, y, ligne, f, couleur, q, dy=(1 - q) * 12)
            y += int(f.size * 1.34)
        y += 12

    # La carte s'éteint sur la fin, pour que le fondu vers l'épisode parte de
    # quelque chose de calme au lieu d'un bloc de texte en pleine lumière.
    sortie = max(0.0, (t - (duree - 0.45)) / 0.45)
    if sortie > 0:
        voile = Image.new("RGBA", (L, H), NUIT + (int(200 * min(1.0, sortie)),))
        im = Image.alpha_composite(im, voile)

    return im.convert("RGB")


# ─── les sous-titres du plan ────────────────────────────────────────────────

def repliques(ep):
    """Qui parle, quand, et jusqu'à quand.

    Les trois voix du film sont écrites dans le script : le conteur ouvre à
    0,0 s, le personnage ferme à 8,0 s, le générique de story porte la
    punchline à 9,1 s. On reprend ces repères tels quels — ils sont la
    partition du mixage, donc du sous-titre.
    """
    return [
        (0.20, 6.60, ep["conteur"], CREME_AFFICHE),
        (7.85, 9.00, ep["personnage"], (255, 255, 255)),
        (9.05, 10.00, ep["generique"], ORANGE_AFFICHE),
    ]


BANDE_Y = 1180          # le haut de la zone de sous-titre
BANDE_H = H - BANDE_Y


def sous_titre(ep, t):
    """La bande de sous-titre à l'instant t, en RGBA, hauteur BANDE_H.

    Elle est rendue à part et incrustée par ffmpeg : composer la vidéo entière
    dans PIL demanderait de décoder puis réencoder chaque image du plan, pour
    ne toucher qu'un tiers de la hauteur.

    Le texte est nettement plus grand qu'avant — 56 px contre 34 — et chaque
    ligne est centrée sur son axe. Les mots apparaissent l'un après l'autre
    sur le premier tiers de la réplique : la voix les dit dans cet ordre, et
    l'œil suit au lieu de lire en avance puis d'attendre.
    """
    im = Image.new("RGBA", (L, BANDE_H), (0, 0, 0, 0))
    d = ImageDraw.Draw(im)

    for debut, fin, texte, couleur in repliques(ep):
        if not (debut - 0.30 <= t <= fin + 0.35):
            continue
        entree = phase(t, debut, debut + 0.28)
        sortie = 1 - phase(t, fin, fin + 0.30)
        opacite = entree * sortie
        if opacite <= 0.01:
            continue

        f = police(800, 56)
        lignes = paragraphe(d, texte, f, int(L * 0.84))
        interligne = int(56 * 1.26)
        hauteur = len(lignes) * interligne

        # Un cartouche sombre et flou derrière le texte, à la place du voile
        # gris qui couvrait tout le plan. Il ne s'étend que sous les lignes.
        plaque = Image.new("RGBA", (L, BANDE_H), (0, 0, 0, 0))
        pd = ImageDraw.Draw(plaque)
        y0 = BANDE_H - hauteur - 190
        pd.rounded_rectangle([48, y0 - 34, L - 48, y0 + hauteur + 26],
                             radius=32, fill=(6, 12, 20, 168))
        plaque = plaque.filter(ImageFilter.GaussianBlur(9))
        if opacite < 0.998:
            plaque.putalpha(plaque.getchannel("A").point(lambda a: int(a * opacite)))
        im = Image.alpha_composite(im, plaque)

        # Les mots se révèlent dans l'ordre, sur le premier tiers.
        #
        # La révélation étant séquentielle, il n'y a JAMAIS plus d'un mot à
        # opacité intermédiaire à un instant donné. Les mots déjà acquis vont
        # donc tous sur un même calque, et seul celui qui arrive obtient le
        # sien. Un calque par mot coûtait douze compositions plein cadre par
        # image, soit trois mille six cents par épisode, pour un résultat
        # rigoureusement identique.
        mots = texte.split()
        revele = phase(t, debut, debut + max(0.5, (fin - debut) * 0.34)) * len(mots)

        acquis = Image.new("RGBA", (L, BANDE_H), (0, 0, 0, 0))
        ad = ImageDraw.Draw(acquis)
        arrivant = None
        vu, y = 0, y0
        for ligne in lignes:
            b = d.textbbox((0, 0), ligne, font=f)
            x = (L - (b[2] - b[0])) // 2 - b[0]
            for mot in ligne.split():
                part = max(0.0, min(1.0, revele - vu))
                pos = (x, y - b[1] + (1 - part) * 8)
                if part >= 0.999:
                    ad.text(pos, mot, font=f, fill=couleur + (255,),
                            stroke_width=3, stroke_fill=(4, 9, 15, 210))
                elif part > 0:
                    arrivant = (pos, mot, part)
                x += largeur(d, mot + " ", f)
                vu += 1
            y += interligne

        if opacite < 0.998:
            acquis.putalpha(acquis.getchannel("A").point(
                lambda v: int(v * opacite)))
        im = Image.alpha_composite(im, acquis)

        if arrivant:
            pos, mot, part = arrivant
            calque = Image.new("RGBA", (L, BANDE_H), (0, 0, 0, 0))
            ImageDraw.Draw(calque).text(
                pos, mot, font=f, fill=couleur + (255,),
                stroke_width=3, stroke_fill=(4, 9, 15, 210))
            a = opacite * part
            calque.putalpha(calque.getchannel("A").point(lambda v: int(v * a)))
            im = Image.alpha_composite(im, calque)
        break

    return im


# ─── montage ────────────────────────────────────────────────────────────────

def sequence(tmp, nom, faire, duree):
    dossier = tmp / nom
    dossier.mkdir()
    for i in range(int(duree * FPS)):
        faire(i / FPS).save(dossier / f"{i:04d}.png")
    dest = tmp / f"{nom}.mp4"
    subprocess.run(
        ["ffmpeg", "-v", "error", "-y", "-framerate", str(FPS),
         "-i", str(dossier / "%04d.png"), "-c:v", "libx264",
         "-pix_fmt", "yuv420p", "-crf", "17", str(dest)],
        check=True,
    )
    return dest


def duree_de(f):
    return float(subprocess.run(
        ["ffprobe", "-v", "error", "-show_entries", "format=duration",
         "-of", "default=nw=1:nk=1", str(f)],
        capture_output=True, text=True, check=True).stdout.strip())


def plaque_frames(tmp):
    """Les images de la plaque Higgsfield, ramenées à trente par seconde."""
    dossier = tmp / "plaque"
    dossier.mkdir()
    subprocess.run(
        ["ffmpeg", "-v", "error", "-y", "-i", str(PLAQUE),
         "-vf", f"fps={FPS}", "-frames:v", str(int(FILM * FPS) + 2),
         str(dossier / "%04d.png")],
        check=True,
    )
    return sorted(dossier.glob("*.png"))


def monter(ep, clip, son, dest, avec_generique):
    """La carte du film, la carte de l'épisode, le plan, et le générique.

    Le plan est reconstruit à partir du clip Higgsfield PROPRE, pas de la
    story déjà diffusée. La story portait un voile gris sur toute l'image —
    posé pour rendre lisibles des sous-titres trop petits, il éteignait la
    photo sur les dix secondes. En repartant du clip d'origine, la couleur
    revient, et le texte est rendu lisible par un cartouche qui ne couvre que
    ce qu'il y a sous les lignes.

    Le son, lui, vient bien de la story : c'est le seul endroit où les trois
    voix sont mixées, et rien ne justifie de les régénérer.

    La story ne prend pas le générique de fin ; le Short YouTube, si.
    """
    tmp = pathlib.Path(tempfile.mkdtemp(prefix="habillage-"))
    try:
        plaque = plaque_frames(tmp)
        film = sequence(
            tmp, "film",
            lambda t: carte_film(ep, t, Image.open(plaque[min(int(t * FPS), len(plaque) - 1)])),
            FILM)
        ouv = sequence(tmp, "episode", lambda t: ouverture(ep, t), OUVERTURE)

        # Les sous-titres sont une bande transparente incrustée par ffmpeg :
        # composer la vidéo entière dans PIL demanderait de décoder puis de
        # réencoder chaque image du plan pour n'en toucher qu'un tiers.
        bande = tmp / "sous-titres"
        bande.mkdir()
        d_clip = min(10.0, duree_de(clip))
        for i in range(int(d_clip * FPS)):
            sous_titre(ep, i / FPS).save(bande / f"{i:04d}.png")

        d_son = duree_de(son)
        b1 = FILM - FONDU                    # le film s'efface dans l'épisode
        b2 = b1 + OUVERTURE - FONDU          # l'épisode s'efface dans le plan
        fin_plan = b2 + d_clip

        entrees = [
            "-i", str(film),
            "-i", str(ouv),
            "-i", str(clip),
            "-framerate", str(FPS), "-i", str(bande / "%04d.png"),
            "-i", str(son),
            "-f", "lavfi", "-t", f"{b2:.3f}", "-i", "anullsrc=r=48000:cl=stereo",
        ]
        graphe = (
            f"[0:v]fps={FPS},scale={L}:{H},format=yuv420p[f];"
            f"[1:v]fps={FPS},scale={L}:{H},format=yuv420p[e];"
            # Le clip est en 720 × 1280 à 24 im/s : on le remonte au format de
            # diffusion avant d'incruster, sinon le texte serait mis à
            # l'échelle avec l'image et perdrait ses arêtes.
            f"[2:v]fps={FPS},scale={L}:{H}:flags=lanczos,"
            f"trim=duration={d_clip:.3f},setpts=PTS-STARTPTS[p];"
            f"[3:v]format=rgba[st];"
            f"[p][st]overlay=0:{BANDE_Y}:format=auto[pt];"
            f"[f][e]xfade=transition=fade:duration={FONDU}:offset={b1:.3f}[fe];"
            f"[fe][pt]xfade=transition=fade:duration={FONDU}:offset={b2:.3f}"
        )
        # Le son de la story démarre à l'image du plan, pas à celle du film.
        pistes = f"[5:a][4:a]concat=n=2:v=0:a=1"
        fin_son = b2 + min(d_son, d_clip)

        if avec_generique:
            gen = sequence(
                tmp, "generique",
                lambda t: generique(ep["titre"], ep["serie"], ep["saison"], t),
                GENERIQUE)
            entrees += ["-i", str(gen),
                        "-f", "lavfi", "-t", f"{GENERIQUE - FONDU:.3f}",
                        "-i", "anullsrc=r=48000:cl=stereo"]
            graphe += (f"[fp];[6:v]fps={FPS},format=yuv420p[g];"
                       f"[fp][g]xfade=transition=fade:duration={FONDU}:"
                       f"offset={fin_plan - FONDU:.3f}[v]")
            pistes = f"[5:a][4:a][7:a]concat=n=3:v=0:a=1"
        else:
            graphe += "[v]"

        subprocess.run(
            ["ffmpeg", "-v", "error", "-y", *entrees,
             "-filter_complex",
             f"{graphe};{pistes},afade=t=out:st={fin_son - 0.35:.3f}:d=0.35[s]",
             "-map", "[v]", "-map", "[s]",
             "-c:v", "libx264", "-preset", "medium", "-crf", "19",
             "-c:a", "aac", "-b:a", "160k", "-movflags", "+faststart",
             str(dest)],
            check=True,
        )
        return dest
    finally:
        shutil.rmtree(tmp, ignore_errors=True)


def planche(images, dest, larg=232):
    vues = [im.resize((larg, int(H * larg / L)), Image.LANCZOS) for im in images]
    out = Image.new("RGB", (len(vues) * (larg + 8) + 8, vues[0].height + 16),
                    (28, 28, 30))
    for i, v in enumerate(vues):
        out.paste(v, (8 + i * (larg + 8), 8))
    out.save(dest)
    return dest


def charger(episode, a):
    ep = {}
    if CATALOGUE.exists():
        ep = next((x for x in json.loads(CATALOGUE.read_text(encoding="utf-8"))
                   if x["id"] == episode), {})
    for cle, val in (("titre", a.titre), ("serie", a.serie), ("saison", a.saison),
                     ("planDuFilm", a.plan_du_film), ("lieu", a.lieu),
                     ("vignette", a.vignette)):
        if val:
            ep[cle] = val
    ep.setdefault("serie", "UpEatFood")
    manque = [c for c in ("titre", "saison", "planDuFilm", "lieu", "vignette")
              if not ep.get(c)]
    if manque:
        raise SystemExit(f"{episode} : il manque {', '.join(manque)}")
    # Le catalogue ne garde que le nom du fichier : les affiches sont déposées
    # dans le dépôt, et un chemin absolu dans un fichier versionné ne survit
    # pas au poste suivant.
    v = pathlib.Path(ep["vignette"])
    ep["vignette"] = v if v.is_absolute() or v.exists() else VIGNETTES / v
    if not pathlib.Path(ep["vignette"]).exists():
        raise SystemExit(f"{episode} : affiche introuvable — {ep['vignette']}")
    return ep


SOURCES = R / "build" / "sources"


def rapatrier(url, nom):
    """Le fichier de la bibliothèque, gardé sous le coude.

    Trente-cinq épisodes font soixante-dix téléchargements ; les relancer à
    chaque essai de mise en page coûte plus de temps que le montage lui-même.
    """
    SOURCES.mkdir(parents=True, exist_ok=True)
    dest = SOURCES / nom
    if dest.exists() and dest.stat().st_size > 100_000:
        return dest
    with urllib.request.urlopen(
        urllib.request.Request(url, headers={"User-Agent": "foodeatup/habillage"}),
        timeout=180,
    ) as r, open(dest, "wb") as f:
        shutil.copyfileobj(r, f)
    return dest


def un_episode(ep, piece, sortie):
    if not ep.get("clip"):
        raise SystemExit(f"{ep['id']} : pas de clip Higgsfield propre")
    if not ep.get("plan"):
        raise SystemExit(f"{ep['id']} : pas de piste son")
    clip = rapatrier(ep["clip"], f"{ep['id']}-clip.mp4")
    son = rapatrier(ep["plan"], f"{ep['id']}-son.mp4")
    sortie.parent.mkdir(parents=True, exist_ok=True)
    monter(ep, clip, son, sortie, piece == "short")
    return sortie


def main(argv):
    p = argparse.ArgumentParser()
    p.add_argument("episode", nargs="?", help="EPxxx, ou --tous")
    p.add_argument("--tous", action="store_true",
                   help="tous les épisodes dont les sources sont en ligne")
    p.add_argument("--titre")
    p.add_argument("--serie")
    p.add_argument("--saison")
    p.add_argument("--plan-du-film")
    p.add_argument("--lieu")
    p.add_argument("--vignette")
    p.add_argument("--piece", choices=("story", "short"), default="story",
                   help="story : film + épisode + plan. short : et le générique.")
    p.add_argument("--sortie", default="dist/upeatfood")
    p.add_argument("--apercu", action="store_true",
                   help="écrit les planches de contrôle, ne monte rien")
    a = p.parse_args(argv)

    if a.tous:
        cat = json.loads(CATALOGUE.read_text(encoding="utf-8"))
        base = pathlib.Path(a.sortie)
        faits, sautes = [], []
        for brut in cat:
            if not (brut.get("clip") and brut.get("plan")):
                sautes.append(brut["id"])
                continue
            ep = charger(brut["id"], a)
            dest = base / a.piece / f"{ep['id']}.mp4"
            un_episode(ep, a.piece, dest)
            faits.append(ep["id"])
            print(f"  {ep['id']}  {duree_de(dest):.2f} s  "
                  f"{dest.stat().st_size / 1024:.0f} Ko", flush=True)
        print(f"\n{len(faits)} montés dans {base / a.piece}")
        if sautes:
            print(f"{len(sautes)} sans source : {' '.join(sautes)}")
        return 0

    if not a.episode:
        raise SystemExit("donner un EPxxx, ou --tous")
    ep = charger(a.episode, a)

    if a.apercu:
        base = pathlib.Path(a.sortie)
        if base.suffix:
            base = base.parent
        base.mkdir(parents=True, exist_ok=True)
        tmp = pathlib.Path(tempfile.mkdtemp(prefix="apercu-"))
        try:
            pl = plaque_frames(tmp)
            t_film = [0.30, 0.90, 1.50, 2.10, 2.60, 3.20, 4.60]
            planche([carte_film(ep, t, Image.open(pl[min(int(t * FPS), len(pl) - 1)]))
                     for t in t_film], base / f"apercu-{a.episode}-film.png")
        finally:
            shutil.rmtree(tmp, ignore_errors=True)
        planche([ouverture(ep, t) for t in (0.12, 0.40, 0.72, 1.00, 1.30, 1.60, 1.85)],
                base / f"apercu-{a.episode}-episode.png")
        planche([generique(ep["titre"], ep["serie"], ep["saison"], t)
                 for t in (0.00, 0.22, 0.44, 0.64, 0.88, 1.20, 2.40)],
                base / f"apercu-{a.episode}-generique.png")
        for quoi in ("film", "episode", "generique"):
            print(base / f"apercu-{a.episode}-{quoi}.png")
        return 0

    dest = pathlib.Path(a.sortie)
    if not dest.suffix:
        dest = dest / a.piece / f"{a.episode}.mp4"
    un_episode(ep, a.piece, dest)
    print(f"{dest}  {a.piece}  {duree_de(dest):.2f} s  {dest.stat().st_size / 1024:.0f} Ko")
    return 0


if __name__ == "__main__":
    sys.exit(main(sys.argv[1:]))
