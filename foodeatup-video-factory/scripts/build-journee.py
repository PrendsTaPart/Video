#!/usr/bin/env python3
"""Habillage des stories de « Une journée » — la série 2, trente et un métiers.

    python3 scripts/build-journee.py EP301
    python3 scripts/build-journee.py --tous

Pourquoi un script à part
-------------------------
`build-stories.py` monte les cent cinquante stories du « Coup de Feu » et
`build-habillage.py` les trente-cinq d'« UpEatFood ». Aucun des deux ne convient
ici, pour une raison de fond et non de commodité :

- l'habillage UpEatFood est construit autour de DEUX VOIX — le conteur et le
  personnage — qui n'existent pas dans cette série. `assets/vo/` ne contient
  aucun fichier `EP3xx` : ni punchline, ni narration, rien.
- `build-stories.py`, lui, garde le son d'origine du plan Higgsfield. Sur cette
  série c'est un défaut, pas une neutralité — voir plus bas.

Cette série se raconte donc par le TEXTE et par la musique. C'est une
contrainte, et elle tombe bien : c'est aussi ce qui la débarrasse du problème
de synchronisation labiale.

Ce qui change par rapport au pilote EP301
-----------------------------------------
Le premier montage existe déjà dans `dist/stories/EP301.mp4`. Quatre choses y
sont reprises ici.

**1. Le son du plan passe à zéro.** Seedance prononce la réplique écrite dans
le prompt : le champ `dit` de `content/serie_journee.py`. Pour EP301 c'est
« J'ouvre à sept heures. Températures, livraison… ». Pendant ce temps l'écran
affiche « Il ouvre, il produit, il ferme ». Deux textes différents, dits et lus
en même temps, par une bouche qui ne suit pas — on ne lit ni l'un ni l'autre.
La musique prend la place ; c'est le même lit que les masters, `bgm.mp3`.

**2. Les césures sont calculées, plus comptées.** `textwrap.wrap(texte, 20)`
coupe au vingtième caractère quoi qu'il y ait à cet endroit, d'où
« Il ouvre, il / produit, il ferme. » sur le pilote — une ligne qui se termine
sur un pronom en attente de son verbe. On reprend ici la césure équilibrée de
l'habillage UpEatFood : elle essaie tous les points de coupe, garde celui dont
les lignes sont les plus proches en largeur, et pénalise lourdement une coupe
après un mot-outil.

**3. Le texte arrive au lieu d'apparaître.** Les mots se révèlent dans l'ordre
de lecture sur le premier tiers du plan, avec une remontée de huit pixels
amortie en sortie cubique. Un bloc qui s'allume d'un coup se lit comme une
incrustation ; un bloc qui se pose se lit comme du montage.

**4. Le métier et le moment sont écrits à l'écran.** « LE CHEF DE CUISINE ·
AVANT LE SERVICE ». Trente et un épisodes montrent trente et un postes du même
vendredi soir : sans cette ligne, ce sont trente et une vidéos ; avec elle,
c'est une série. Elle est en capitales espacées — Poppins n'a pas
d'interlettrage optique en capitales, et sans l'écart le bloc se lit comme un
seul mot.

Le cartouche plutôt que le contour
----------------------------------
`build-stories.py` a essayé trois solutions et documente les deux premières :
un `drawbox` noir qui laissait une arête en travers du plan, puis des dégradés
qui assombrissaient la moitié basse. Il a retenu un contour noir sur la lettre.

On prend ici la quatrième : un cartouche arrondi, flouté, qui ne s'étend que
sous les lignes écrites. Il ne touche pas au plan ailleurs — c'est ce que
reprochaient les dégradés — et il tient sur un fond clair, ce que le contour
seul ne fait qu'à moitié : sur le pilote, « produit, il ferme. » tombe sur la
veste blanche du chef et sur l'inox.

Le son ne passe pas par le graphe principal
-------------------------------------------
`loudnorm` ressort ses frames avec des PTS décalés, et tout `atrim` qui suit
prend ce décalage pour du temps écoulé. Le pilote le fait pourtant, suivi d'un
`apad,atrim` — ça passe sur dix secondes, ça ne passera pas sur un format plus
court. La normalisation est ici dans une passe séparée, comme partout ailleurs
dans ce dépôt.
"""
import argparse
import json
import pathlib
import shutil
import subprocess
import sys
import tempfile

from PIL import Image, ImageDraw, ImageFilter, ImageFont

R = pathlib.Path(__file__).resolve().parent.parent
sys.path.insert(0, str(R / "content"))

FONTES = R.parent / "videos" / "stories-foodeatup-30j" / "assets" / "fonts"
HOOKS = R / "dist" / "hooks"
BGM = R / "templates" / "bgm.mp3"
LOGO = R / "templates" / "logo_foodeatup.png"

L, H = 1080, 1920
FPS = 30
DUREE = 10.0

HOOK_IN, HOOK_OUT = 0.45, 4.10
PUNCH_IN, PUNCH_OUT = 5.60, DUREE
ETIQUETTE_IN = 0.90

# Le badge est au même endroit que sur le master et sur les stories du « Coup
# de Feu » : une série se reconnaît d'abord à ce qui ne bouge pas.
LOGO_X, LOGO_Y, LOGO_L = 795, 57, 250

CREME = (248, 244, 225)
BLEU = (35, 140, 249)
ORANGE = (242, 178, 45)

# Le lit musical est ici la bande-son entière, pas un fond sous une voix : il
# monte donc à 0,30, le niveau que l'habillage UpEatFood réserve à ses cartes
# muettes, et non à 0,085 qui est son niveau sous la parole.
LIT = 0.30

# La cible de normalisation est celle des stories du « Coup de Feu », pas celle
# des masters ni celle du film. Les deux séries se suivront dans le même fil
# Instagram : une story deux décibels sous les autres se remarque comme un
# défaut de fabrication. `build-stories.py` vise -14 LUFS, on vise -14 LUFS.
LOUDNESS = "I=-14:TP=-1.5:LRA=11"

OUTILS = {
    "le", "la", "les", "un", "une", "des", "du", "de", "d'", "l'", "au", "aux",
    "et", "ou", "à", "en", "dans", "sur", "sous", "par", "pour", "que", "qui",
    "ne", "se", "ce", "son", "sa", "ses", "mon", "ma", "mes", "leur", "leurs",
    "il", "elle", "ils", "elles", "on", "je", "tu", "nous", "vous",
}


def police(poids, taille):
    return ImageFont.truetype(str(FONTES / f"Poppins-{poids}.ttf"), taille)


def largeur(d, texte, font):
    b = d.textbbox((0, 0), texte, font=font)
    return b[2] - b[0]


def espace(texte):
    return " ".join(texte)


def amortie(t):
    """Sortie cubique : rapide puis freinée. Le linéaire se remarque."""
    t = max(0.0, min(1.0, t))
    return 1 - (1 - t) ** 3


def phase(t, debut, fin):
    if t <= debut:
        return 0.0
    if t >= fin:
        return 1.0
    return amortie((t - debut) / (fin - debut))


def lignes_equilibrees(d, texte, font, maxi):
    """Le découpage en lignes le moins raboteux, et jamais sur un mot-outil.

    Le remplissage glouton — prendre autant de mots que la ligne en accepte,
    puis passer à la suivante — a un défaut qu'on ne voit qu'en mesurant :
    chaque ligne est remplie au maximum, donc il ne reste jamais la place de
    faire descendre un mot. Mesuré sur les deux textes d'EP301, la descente du
    mot-outil échouait à **neuf** et **dix pixels** près sur 885. La règle
    était écrite, elle ne s'appliquait jamais.

    On choisit donc les coupes globalement, par programmation dynamique. Le
    coût d'une ligne est le carré de ce qui lui reste de blanc : deux lignes
    moyennement remplies coûtent moins qu'une pleine et une vide, ce qui donne
    un bloc régulier. Une ligne qui se termine sur un mot-outil paie une
    pénalité forfaitaire lourde — elle reste possible quand aucun autre
    découpage ne tient, mais elle perd contre à peu près tout le reste.

    La dernière ligne ne paie pas son blanc : elle a le droit d'être courte,
    c'est la fin du texte et non un trou.
    """
    mots = texte.split()
    n = len(mots)
    if not n:
        return []

    larg = [[None] * (n + 1) for _ in range(n + 1)]
    for i in range(n):
        for j in range(i + 1, n + 1):
            larg[i][j] = largeur(d, " ".join(mots[i:j]), font)

    PENALITE = maxi * maxi          # dissuasif, pas interdit
    INF = float("inf")
    cout = [INF] * (n + 1)
    coupe = [0] * (n + 1)
    cout[0] = 0.0
    for j in range(1, n + 1):
        for i in range(j):
            if cout[i] == INF or larg[i][j] > maxi:
                continue
            c = cout[i]
            c += 0.0 if j == n else (maxi - larg[i][j]) ** 2
            if j < n and mots[j - 1].lower().strip(",;:.!?") in OUTILS:
                c += PENALITE
            if c < cout[j]:
                cout[j] = c
                coupe[j] = i
    if cout[n] == INF:              # un mot plus large que la boîte
        return [" ".join(mots)]

    lignes, j = [], n
    while j > 0:
        i = coupe[j]
        lignes.append(" ".join(mots[i:j]))
        j = i
    return lignes[::-1]



def ajuster_bloc(d, texte, maxi, tailles, remplissage_min=0.80):
    """La taille de corps qui donne le bloc le mieux rempli.

    Prendre la plus grande taille qui « tient » est un mauvais réflexe : le
    texte tient toujours, il tient simplement sur plus de lignes. Mesuré sur
    l'accroche d'EP301, de 78 px à 66 px on obtient invariablement cinq lignes
    remplies à 60 %, c'est-à-dire un bloc haut, creux et mou. À 62 px on passe
    à TROIS lignes remplies à 93 %, dont les coupes tombent sur la ponctuation
    de la phrase.

    Un corps plus petit, mais un bloc plus dense et plus court : à l'écran il
    se lit plus vite et il masque moins le plan. On parcourt donc les tailles
    de la plus grande à la plus petite et on garde la première qui atteint le
    taux de remplissage voulu ; à défaut, la mieux remplie.
    """
    meilleur = None
    for taille in tailles:
        f = police(800, taille)
        lignes = lignes_equilibrees(d, texte, f, maxi)
        lg = [largeur(d, x, f) for x in lignes]
        if not lg:
            continue
        taux = sum(lg) / len(lg) / maxi
        if taux >= remplissage_min:
            return f, lignes
        if meilleur is None or taux > meilleur[0]:
            meilleur = (taux, f, lignes)
    return (meilleur[1], meilleur[2]) if meilleur else (police(800, tailles[-1]), [texte])


def bloc(im, lignes, font, y_haut, revele, opacite,
         couleur=(255, 255, 255), centre=False):
    """Pose un bloc de texte sur son cartouche, mots révélés dans l'ordre.

    `revele` est un nombre de mots, éventuellement fractionnaire : le mot en
    cours d'arrivée est le seul à opacité intermédiaire. Les mots déjà acquis
    partent donc sur un calque commun — un calque par mot coûtait douze
    compositions plein cadre par image pour un résultat identique.
    """
    if opacite <= 0.01:
        return im
    d = ImageDraw.Draw(im)
    interligne = int(font.size * 1.24)
    hauteur = len(lignes) * interligne

    plaque = Image.new("RGBA", im.size, (0, 0, 0, 0))
    ImageDraw.Draw(plaque).rounded_rectangle(
        [48, y_haut - 36, L - 48, y_haut + hauteur + 22],
        radius=34, fill=(6, 12, 20, 165))
    plaque = plaque.filter(ImageFilter.GaussianBlur(10))
    if opacite < 0.998:
        plaque.putalpha(plaque.getchannel("A").point(
            lambda a: int(a * opacite)))
    im = Image.alpha_composite(im, plaque)

    acquis = Image.new("RGBA", im.size, (0, 0, 0, 0))
    ad = ImageDraw.Draw(acquis)
    arrivant = None
    vu, y = 0, y_haut
    for ligne in lignes:
        b = d.textbbox((0, 0), ligne, font=font)
        x = ((L - (b[2] - b[0])) // 2 - b[0]) if centre else 80
        for mot in ligne.split():
            part = max(0.0, min(1.0, revele - vu))
            pos = (x, y - b[1] + (1 - part) * 9)
            if part >= 0.999:
                ad.text(pos, mot, font=font, fill=couleur + (255,),
                        stroke_width=3, stroke_fill=(4, 9, 15, 205))
            elif part > 0:
                arrivant = (pos, mot, part)
            x += largeur(d, mot + " ", font)
            vu += 1
        y += interligne
    if opacite < 0.998:
        acquis.putalpha(acquis.getchannel("A").point(
            lambda v: int(v * opacite)))
    im = Image.alpha_composite(im, acquis)

    if arrivant:
        pos, mot, part = arrivant
        c = Image.new("RGBA", im.size, (0, 0, 0, 0))
        ImageDraw.Draw(c).text(pos, mot, font=font, fill=couleur + (255,),
                               stroke_width=3, stroke_fill=(4, 9, 15, 205))
        a = opacite * part
        c.putalpha(c.getchannel("A").point(lambda v: int(v * a)))
        im = Image.alpha_composite(im, c)
    return im


def etiquette(im, ep, opacite):
    """« LE CHEF DE CUISINE · AVANT LE SERVICE », sous le hook.

    C'est la ligne qui fait la série. Trente et un épisodes montrent trente et
    un postes du même vendredi soir ; sans elle on regarde trente et une
    vidéos sans lien. Un filet orange la précède — le même orange que la carte
    de fin d'UpEatFood, pour que les deux séries se répondent.
    """
    if opacite <= 0.01:
        return im
    f = police(700, 30)
    texte = f"{espace(ep['metierNom'].upper())}   ·   {espace(ep['phaseLabel'].upper())}"

    def dessiner(d):
        d.rectangle([80, 246, 80 + 54, 246 + 5], fill=ORANGE + (255,))
        d.text((80, 272), texte, font=f, fill=CREME + (255,),
               stroke_width=3, stroke_fill=(4, 9, 15, 195))

    calque = Image.new("RGBA", im.size, (0, 0, 0, 0))
    dessiner(ImageDraw.Draw(calque, "RGBA"))
    if opacite < 0.998:
        calque.putalpha(calque.getchannel("A").point(
            lambda a: int(a * opacite)))
    return Image.alpha_composite(im, calque)


TAILLES = (78, 74, 70, 66, 64, 62, 60, 58, 56, 54)
BOITE = int(L * 0.82)


def calque_a(ep, t):
    """L'incrustation complète à l'instant t : titre, étiquette, tension.

    Le choix des trois textes n'est pas neutre, et le pilote se trompait
    dessus. Il affichait `accrocheMetier` en ouverture — or ce champ décrit le
    MÉTIER, pas l'épisode : il n'existe que onze accroches pour trente et un
    épisodes. EP301, EP302 et EP303 sont les trois journées du chef de
    cuisine, diffusées les 29, 30 et 31 octobre : trois jours de suite, la
    même phrase se serait affichée à l'ouverture. On lit ça comme un bug, pas
    comme une série.

    Le `titre`, lui, est unique sur les trente et un — vérifié — et il dit
    l'épisode : « La cuisine est vide, et dans quatre heures tout doit être
    prêt ». C'est lui qui ouvre.

    La `tension` reste en fermeture, et le fait qu'elle soit commune aux trois
    épisodes d'un même métier devient une qualité : trois soirs de suite, la
    même phrase revient en fin de plan. Répétée à l'ouverture c'est une
    panne ; répétée en chute c'est un refrain.
    """
    im = Image.new("RGBA", (L, H), (0, 0, 0, 0))
    d = ImageDraw.Draw(im)

    op_h = (phase(t, HOOK_IN, HOOK_IN + 0.30)
            * (1 - phase(t, HOOK_OUT, HOOK_OUT + 0.35)))
    if op_h > 0.01:
        f, lignes = ajuster_bloc(d, ep["titre"], BOITE, TAILLES)
        mots = len(ep["titre"].split())
        im = bloc(im, lignes, f, 330,
                  phase(t, HOOK_IN, HOOK_IN + 1.30) * mots, op_h)
        im = etiquette(im, ep,
                       phase(t, ETIQUETTE_IN, ETIQUETTE_IN + 0.45)
                       * (1 - phase(t, HOOK_OUT, HOOK_OUT + 0.35)))

    op_p = phase(t, PUNCH_IN, PUNCH_IN + 0.30)
    if op_p > 0.01:
        f, lignes = ajuster_bloc(d, ep["tension"], BOITE, TAILLES)
        # Le bloc est posé par son PIED : une tension d'une ligne et une de
        # trois doivent finir à la même hauteur, sinon le bas de l'image saute
        # d'un épisode à l'autre et la série se défait.
        y = H - 430 - len(lignes) * int(f.size * 1.24)
        mots = len(ep["tension"].split())
        im = bloc(im, lignes, f, y,
                  phase(t, PUNCH_IN, PUNCH_IN + 1.25) * mots, op_p)
    return im



def monter(ep, clip, dest):
    tmp = pathlib.Path(tempfile.mkdtemp(prefix="journee-"))
    try:
        n = int(DUREE * FPS)
        for i in range(n):
            calque_a(ep, i / FPS).save(tmp / f"a{i:04d}.png")

        # Le son, en deux temps.
        #
        # 1. Le lit musical seul, coupé à la durée, avec ses fondus. Le plan
        #    Higgsfield n'entre PAS dans le mélange : sa piste porte la
        #    réplique prononcée par Seedance, qui n'est ni le hook ni la
        #    tension, et dont les lèvres ne suivent pas.
        brut = tmp / "son.wav"
        subprocess.run(
            ["ffmpeg", "-v", "error", "-y", "-i", str(BGM),
             "-af", (f"aformat=sample_fmts=fltp:sample_rates=48000:"
                     f"channel_layouts=stereo,atrim=duration={DUREE},"
                     f"asetpts=N/SR/TB,volume={LIT},"
                     f"afade=t=in:st=0:d=0.7,"
                     f"afade=t=out:st={DUREE - 0.6:.2f}:d=0.6"),
             "-ar", "48000", "-ac", "2", "-c:a", "pcm_s16le", str(brut)],
            check=True)

        # 2. La normalisation, dans sa propre passe. Jamais dans le graphe
        #    principal : `loudnorm` décale les PTS et le `atrim` qui suit
        #    prendrait ce décalage pour du temps écoulé.
        son = tmp / "son.m4a"
        subprocess.run(
            ["ffmpeg", "-v", "error", "-y", "-i", str(brut),
             "-af", f"loudnorm={LOUDNESS}",
             "-ar", "48000", "-ac", "2", "-c:a", "aac", "-b:a", "160k",
             str(son)], check=True)

        graphe = (
            f"[0:v]scale={L}:{H}:force_original_aspect_ratio=increase,"
            f"crop={L}:{H},setsar=1,fps={FPS},trim=duration={DUREE},"
            f"setpts=PTS-STARTPTS[v0];"
            # `format=yuv420p` derrière CHAQUE overlay. En `format=auto`,
            # l'overlay ressort en RGBA, libx264 négocie du 4:4:4 et rend un
            # « High 4:4:4 Predictive » que ni les navigateurs ni les
            # téléphones ne lisent. Le fichier a l'air correct partout sauf à
            # la lecture.
            f"[v0][1:v]overlay=0:0:format=auto,format=yuv420p[v1];"
            f"[2:v]scale={LOGO_L}:-1[logo];"
            f"[v1][logo]overlay={LOGO_X}:{LOGO_Y}:format=auto,"
            f"format=yuv420p[vout]"
        )

        subprocess.run(
            ["ffmpeg", "-v", "error", "-y",
             "-i", str(clip),
             "-framerate", str(FPS), "-i", str(tmp / "a%04d.png"),
             "-i", str(LOGO), "-i", str(son),
             "-filter_complex", graphe,
             "-map", "[vout]", "-map", "3:a",
             "-c:v", "libx264", "-preset", "medium", "-crf", "19",
             "-pix_fmt", "yuv420p", "-profile:v", "high", "-level", "4.0",
             "-c:a", "aac", "-b:a", "160k",
             "-t", str(DUREE), "-movflags", "+faststart", str(dest)],
            check=True)
        return dest
    finally:
        shutil.rmtree(tmp, ignore_errors=True)


def catalogue():
    import serie_journee
    eps = serie_journee.episodes
    return eps() if callable(eps) else eps


def main(argv):
    p = argparse.ArgumentParser()
    p.add_argument("episode", nargs="?")
    p.add_argument("--tous", action="store_true")
    p.add_argument("--sortie", default="dist/journee/story")
    a = p.parse_args(argv)

    eps = catalogue()
    if a.tous:
        choisis = eps
    elif a.episode:
        choisis = [x for x in eps if x["id"] == a.episode]
        if not choisis:
            raise SystemExit(f"{a.episode} : absent de content/serie_journee.py")
    else:
        raise SystemExit("usage: build-journee.py EP301 | --tous")

    sortie = R / a.sortie
    sortie.mkdir(parents=True, exist_ok=True)
    for ep in choisis:
        clip = HOOKS / f"{ep['id']}.mp4"
        if not clip.exists():
            print(f"  {ep['id']} : pas de plan dans dist/hooks/ — sauté",
                  flush=True)
            continue
        dest = sortie / f"{ep['id']}.mp4"
        monter(ep, clip, dest)
        duree = subprocess.run(
            ["ffprobe", "-v", "error", "-show_entries", "format=duration",
             "-of", "default=nw=1:nk=1", str(dest)],
            capture_output=True, text=True).stdout.strip()
        print(f"  {dest.relative_to(R)}  {float(duree):.2f} s  "
              f"{dest.stat().st_size // 1024} Ko", flush=True)
    return 0


if __name__ == "__main__":
    sys.exit(main(sys.argv[1:]))
