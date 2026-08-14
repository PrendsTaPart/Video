#!/usr/bin/env python3
"""Les cinq gabarits « en cours » — un par pièce, en charte RapidoCMS.

    python3 scripts/gen-gabarits-attente.py [dossier de sortie]

Pourquoi cinq et pas un
-----------------------
Une page d'épisode montre cinq pièces côte à côte. Un cadre gris identique
répété cinq fois ne dit rien de plus qu'« il manque tout » — alors que ce qui
manque n'est pas la même chose : une story de dix secondes, quatre planches à
dessiner, un visuel unique, un master de trente-sept secondes. Le gabarit
nomme la pièce et donne son format, donc il informe au lieu de meubler.

Et ils ne sont pas tous au même ratio : 9:16 pour les trois vidéos, 4:5 pour
les deux images. Un seul gabarit forcerait un des deux formats à se déformer,
et un aperçu déformé ressemble à un bug.

Charte
------
RapidoCMS — bleu #03A9F5, gris #383838, blanc, tons clairs. C'est la marque de
l'outil qui produira ces pièces, pas celle de la série : le gabarit dit « ça
arrive », il ne prétend pas être l'épisode.

Le huit du logo vient de site.foodeatup.com. Il est posé en filigrane, très
discret : c'est un fond d'attente, pas une publicité.

Rien n'est généré par une IA : PIL compose des aplats, un dégradé et du texte.
Gratuit, reproductible, corrigeable.
"""
import pathlib
import sys

from PIL import Image, ImageDraw, ImageFilter

R = pathlib.Path(__file__).resolve().parent.parent
POLICE = R / "templates" / "Poppins-800.ttf"
HUIT = R / "templates" / "foodeatup-infinity.png"

BLEU = (3, 169, 245)
GRIS = (56, 56, 56)
ENCRE = (14, 26, 35)

# nom du fichier, libellé, format annoncé, ratio, teinte de fond
GABARITS = [
    ("story", "Story en cours", "9:16 · 1080 × 1920 · 10 s", (1080, 1920), 0.00),
    ("carrousel", "Carrousel en cours", "4:5 · 4 planches · publié en PDF", (1080, 1350), 0.18),
    ("visuel", "Visuel en cours", "4:5 · 1080 × 1350", (1080, 1350), 0.36),
    ("master", "Vidéo en cours", "9:16 · 1080 × 1920 · 37,5 s", (1080, 1920), 0.54),
    ("short", "Short en cours", "9:16 · 1080 × 1920 · 37,5 s", (1080, 1920), 0.72),
]


def police(taille):
    from PIL import ImageFont
    return ImageFont.truetype(str(POLICE), taille)


def melange(a, b, t):
    return tuple(int(a[i] + (b[i] - a[i]) * t) for i in range(3))


def fond(l, h, decalage):
    """Un dégradé diagonal, du bleu vers l'encre.

    Les cinq gabarits partagent la même famille mais pas la même teinte : le
    décalage fait glisser le point de bascule. Côte à côte on les distingue
    sans les lire, et on ne croit pas à une image répétée cinq fois.
    """
    im = Image.new("RGB", (l, h))
    px = im.load()
    # Le décalage déplace la teinte de départ, il ne boucle PAS. Un modulo
    # ramenait la valeur à zéro en bas à droite : le dégradé y repassait d'un
    # coup de l'encre au bleu vif et laissait une arête diagonale nette, très
    # visible sur les gabarits les plus décalés. On borne à 1 au lieu de
    # reboucler, et on part d'un bleu plus ou moins clair selon le gabarit.
    depart = melange(BLEU, (255, 255, 255), decalage * 0.28)
    for y in range(h):
        for x in range(0, l, 4):
            t = min(1.0, (x / l) * 0.42 + (y / h) * 0.58)
            # courbe douce : le bleu reste franc en haut, l'encre gagne en bas
            c = melange(melange(depart, ENCRE, 0.12), ENCRE, t * t)
            for k in range(4):
                if x + k < l:
                    px[x + k, y] = c
    return im


def grille(im, pas=90):
    """Une trame fine, comme un fond de maquette. Elle donne de la matière
    sans attirer l'œil — un aplat pur se lit comme une image qui n'a pas
    chargé."""
    d = ImageDraw.Draw(im, "RGBA")
    for x in range(0, im.width, pas):
        d.line([(x, 0), (x, im.height)], fill=(255, 255, 255, 12), width=1)
    for y in range(0, im.height, pas):
        d.line([(0, y), (im.width, y)], fill=(255, 255, 255, 12), width=1)
    return im


def filigrane(im):
    if not HUIT.exists():
        return im
    h = Image.open(HUIT).convert("RGBA")
    k = im.width * 0.62 / h.width
    h = h.resize((int(h.width * k), int(h.height * k)), Image.LANCZOS)
    h = h.filter(ImageFilter.GaussianBlur(0.6))
    voile = Image.new("RGBA", im.size, (0, 0, 0, 0))
    voile.paste(h, ((im.width - h.width) // 2, (im.height - h.height) // 2), h)
    voile.putalpha(voile.getchannel("A").point(lambda a: int(a * 0.10)))
    return Image.alpha_composite(im.convert("RGBA"), voile).convert("RGB")


def gabarit(nom, libelle, format_, taille, decalage, sortie):
    l, h = taille
    im = filigrane(grille(fond(l, h, decalage)))
    d = ImageDraw.Draw(im, "RGBA")

    marge = int(l * 0.09)
    centre = h // 2

    # La pastille de marque, en haut à gauche : on sait tout de suite qui
    # produira la pièce.
    f_marque = police(int(l * 0.030))
    txt = "RAPIDOCMS"
    bb = d.textbbox((0, 0), txt, font=f_marque)
    pw, ph = bb[2] - bb[0] + int(l * 0.045), bb[3] - bb[1] + int(l * 0.032)
    d.rounded_rectangle([marge, marge, marge + pw, marge + ph],
                        radius=ph // 2, fill=(255, 255, 255, 235))
    d.text((marge + (pw - (bb[2] - bb[0])) // 2,
            marge + (ph - (bb[3] - bb[1])) // 2 - bb[1]),
           txt, font=f_marque, fill=BLEU)

    # Le libellé, au centre. Deux lignes : le mot de la pièce puis « en cours »,
    # parce que « Carrousel en cours » sur une seule ligne rétrécit la
    # typographie au point de la rendre décorative.
    mot, reste = libelle.split(" ", 1)
    f_gros = police(int(l * 0.115))
    f_petit = police(int(l * 0.052))

    b1 = d.textbbox((0, 0), mot, font=f_gros)
    b2 = d.textbbox((0, 0), reste, font=f_petit)
    hh = (b1[3] - b1[1]) + int(l * 0.035) + (b2[3] - b2[1])
    y = centre - hh // 2 - int(l * 0.04)

    d.text(((l - (b1[2] - b1[0])) // 2, y - b1[1]), mot, font=f_gros,
           fill=(255, 255, 255))
    y += (b1[3] - b1[1]) + int(l * 0.035)
    d.text(((l - (b2[2] - b2[0])) // 2, y - b2[1]), reste, font=f_petit,
           fill=(255, 255, 255, 200))

    # Le trait, puis le format. Le trait sépare ce qui manque de ce qu'on en
    # sait — c'est la seule ponctuation de l'image.
    y += (b2[3] - b2[1]) + int(l * 0.055)
    d.rounded_rectangle([(l - int(l * 0.16)) // 2, y,
                         (l + int(l * 0.16)) // 2, y + max(3, int(l * 0.005))],
                        radius=3, fill=BLEU)

    y += int(l * 0.055)
    f_fmt = police(int(l * 0.034))
    b3 = d.textbbox((0, 0), format_, font=f_fmt)
    d.text(((l - (b3[2] - b3[0])) // 2, y - b3[1]), format_, font=f_fmt,
           fill=(255, 255, 255, 165))

    dest = sortie / f"attente-{nom}.jpg"
    im.save(dest, "JPEG", quality=82, optimize=True)
    return dest


def main(argv):
    sortie = pathlib.Path(argv[0]) if argv else (R / "dist" / "gabarits")
    sortie.mkdir(parents=True, exist_ok=True)
    total = 0
    for g in GABARITS:
        d = gabarit(*g, sortie)
        total += d.stat().st_size
        print(f"  {d.name:24} {d.stat().st_size / 1024:5.0f} Ko")
    print(f"\n{len(GABARITS)} gabarits, {total / 1024:.0f} Ko — {sortie}")
    return 0


if __name__ == "__main__":
    sys.exit(main(sys.argv[1:]))
