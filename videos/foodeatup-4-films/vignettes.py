"""Fabrique une vignette YouTube 1280×720 par vidéo, à partir de ses propres images.

Une image prise dans la moitié « solution » du montage, assombrie par le bas,
le titre en Poppins blanc sur un bandeau bleu nuit, le logo en haut à droite.

    python3 vignettes.py            # les 158
    python3 vignettes.py foodeatup-clip
"""
import subprocess
import sys
from pathlib import Path

from PIL import Image, ImageDraw, ImageFilter, ImageStat

from build import BLUE, INK, LOGO_DIR, OUT, WHITE, duration, font

VIG = Path(__file__).resolve().parent / "vignettes"
W, H = 1280, 720


def frame(src, t, dst):
    subprocess.run(["ffmpeg", "-y", "-loglevel", "error", "-ss", f"{t:.2f}", "-i", str(src),
                    "-frames:v", "1", str(dst)], check=True)


def fit(im):
    """Découpe une fenêtre 16:9 dans le master vertical, un peu au-dessus du centre.

    Un recadrage franc plutôt qu'un fond flouté : la vignette est pleine, et la
    bande retenue évite les incrustations de bas de cadre du montage."""
    bande = int(im.width * 9 / 16)
    haut = int((im.height - bande) * 0.30)
    im = im.crop((0, haut, im.width, haut + bande))
    return im.resize((W, H), Image.LANCZOS)


def texte(d, titre):
    """Le titre, au plus deux lignes, sur un bandeau en bas."""
    size = 82
    f = font(800, size)
    mots = titre.split()
    while True:
        lignes, cur = [], ""
        for m in mots:
            essai = (cur + " " + m).strip()
            if d.textlength(essai, font=f) > W - 150 and cur:
                lignes.append(cur)
                cur = m
            else:
                cur = essai
        lignes.append(cur)
        if len(lignes) <= 2 or size <= 44:
            return lignes, f
        size -= 6
        f = font(800, size)


def vignette(nom, titre):
    src = OUT / f"{nom}.mp4"          # le master vertical, plus net une fois recadré
    VIG.mkdir(exist_ok=True)
    d_tot = duration(src)
    # quatre candidats dans les plans, avant le logo de signature ; on garde le plus net
    best, meilleur = None, -1.0
    for k, part in enumerate((0.16, 0.28, 0.40, 0.52)):
        tmp = VIG / f".{nom}-{k}.png"
        frame(src, d_tot * part, tmp)
        cand = fit(Image.open(tmp).convert("RGB"))
        tmp.unlink()
        net = ImageStat.Stat(cand.convert("L").filter(ImageFilter.FIND_EDGES)).stddev[0]
        if net > meilleur:
            best, meilleur = cand, net
    im = best

    d = ImageDraw.Draw(im, "RGBA")
    lignes, f = texte(d, titre)
    lh = f.size + 16
    haut = H - 40 - lh * len(lignes) - 44
    d.rectangle([0, haut - 30, W, H], fill=(*INK, 214))
    d.rectangle([0, haut - 30, W, haut - 22], fill=(*BLUE, 255))
    y = haut + 6
    for l in lignes:
        d.text(((W - d.textlength(l, font=f)) / 2, y), l, font=f, fill=WHITE)
        y += lh

    lg = Image.open(LOGO_DIR / "foodeatup-logo-mascot.png").convert("RGBA")
    lw = 190
    lg = lg.resize((lw, int(lg.height * lw / lg.width)), Image.LANCZOS)
    im.paste(lg, (W - lw - 34, 30), lg)

    out = VIG / f"{nom}.jpg"
    im.save(out, quality=88, optimize=True)        # sous les 2 Mo imposés par YouTube
    return out


def toutes():
    sys.path.insert(0, "scripts")
    from serie30 import CLIPS, SERIE
    from serie50_data import LIGNES as L50
    from serie60_data import LIGNES as L60
    items = [("foodeatup-clip", "Une journée. Une app."),
             ("foodeatup-presentation", "Le même restaurant, avant et après"),
             ("foodeatup-commercial", "Le contrôleur"),
             ("foodeatup-demo", "Un tour du restaurant"),
             ("foodeatup-avant-apres", "Le même restaurant, deux fois"),
             ("foodeatup-teaser", "Bande-annonce"),
             ("foodeatup-short-haccp", "Le contrôle"),
             ("foodeatup-short-stock", "L'inventaire"),
             ("foodeatup-short-equipe", "Le planning"),
             ("foodeatup-short-compta", "L'addition"),
             ("foodeatup-short-reservations", "La double réservation"),
             ("foodeatup-short-avis", "L'avis du soir")]
    items += [(f"foodeatup-s{n}-{v[1]}", v[2]) for n, v in SERIE.items()]
    items += [(f"foodeatup-clip-{k}", t) for k, (t, _s, _m, _p) in CLIPS.items()]
    items += [(f"foodeatup-{c.lower()}-{nom}", titre) for c, nom, titre, _p, _l in L50]
    items += [(f"foodeatup-{c.lower()}-{nom}", titre) for c, nom, titre, _p, _l in L60]
    return items


if __name__ == "__main__":
    voulus = set(sys.argv[1:])
    for nom, titre in toutes():
        if voulus and nom not in voulus:
            continue
        print(vignette(nom, titre))
