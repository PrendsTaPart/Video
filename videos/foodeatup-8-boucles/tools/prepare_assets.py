#!/usr/bin/env python3
"""Prépare les illustrations de la série à partir des assets RÉELS du dépôt.

Les personnages 3D de `videos/shared-images/characters/` sont la librairie
maison (règle du studio : réutiliser avant de générer). Ils sont livrés en RGB
sur fond blanc : posés tels quels sur le crème #FCF9E6 de la charte Academy, ils
afficheraient un rectangle blanc. On les détoure donc, on les recadre sur leur
contenu, et on les réduit — un PNG de 2 Mo inliné neuf fois ferait une
composition de 20 Mo.

Rien n'est inventé ici : aucune image n'est retouchée sur le fond, seulement
détourée et redimensionnée.
"""
import collections
import json
import pathlib

from PIL import Image, ImageDraw

HERE = pathlib.Path(__file__).resolve().parent
PROJ = HERE.parent
REPO = PROJ.parent.parent
SRC = REPO / "videos/shared-images/characters"
OUT = PROJ / "assets/img"

# Un personnage « chaos » pour le plan 1 (le problème), un personnage « calme »
# pour le plan 6 (le résultat). C'est le même couple narratif sur les 9 vidéos.
MAPPING = {
    "boucle-00-principe":              {"probleme": "chef-robot-highfive", "resultat": "chef-kitchen-calm"},
    "boucle-01-configuration-boutique": {"probleme": "setup-blank",         "resultat": "configurateur-agent"},
    "boucle-02-equipe":                {"probleme": "planning-chaos",      "resultat": "chef-planning-board"},
    "boucle-03-stockvision":           {"probleme": "stock-chaos",         "resultat": "chef-storeroom"},
    "boucle-04-haccp":                 {"probleme": "haccp-paperwork",     "resultat": "chef-fridge-temp"},
    "boucle-05-ecommerce":             {"probleme": "phone-chaos",         "resultat": "caroline-agent"},
    # Ces deux « problèmes » n'existent pas dans la librairie : ils sont à
    # générer via RapidoCMS (voir tools/generate_missing.py). En attendant, on
    # retombe sur un personnage existant plutôt que sur un placeholder.
    "boucle-06-communication":         {"probleme": "surstock-clients-muets", "resultat": "commerciale-chef"},
    "boucle-07-fidelite":              {"probleme": "clients-qui-ne-reviennent-pas", "resultat": "equipe-tablette"},

    "boucle-08-comptabilite":          {"probleme": "compta-chaos",        "resultat": "chef-desk-calm"},
}

# Le détourage par remplissage depuis les bords suppose un sujet isolé sur du
# blanc. Une image dont le SUJET est pâle et fondu dans le fond (les silhouettes
# fantômes des clients qui ne reviennent pas, la salle vide en arrière-plan) y
# perdrait justement ce qu'elle raconte. Pour celles-là on teinte : chaque pixel
# est multiplié par le crème de la charte, si bien que le blanc pur devient
# exactement le fond de page et disparaît, pendant que tout le reste survit.
TEINTER = {"clients-qui-ne-reviennent-pas"}
CREME = (252, 249, 230)

# Les images générées ont un fond quasi blanc, mais pas exactement #FFFFFF
# (compression, léger dégradé). 26 attrape le fond sans mordre sur la toque
# blanche du chef, qui est nettement ombrée.
SEUIL = 26
HAUTEUR_CIBLE = 900


def detourer(im: Image.Image) -> Image.Image:
    """Rend transparent le fond clair connexe aux bords.

    Un simple seuillage global mangerait la veste et la toque blanches du chef.
    On part donc des bords et on ne propage que dans le fond réellement connexe
    — la toque, entourée de pixels colorés, n'est jamais atteinte.
    """
    im = im.convert("RGBA")
    w, h = im.size
    px = im.load()

    def clair(x, y):
        r, g, b, _ = px[x, y]
        return r > 255 - SEUIL and g > 255 - SEUIL and b > 255 - SEUIL

    vus = bytearray(w * h)
    file = collections.deque()
    for x in range(w):
        for y in (0, h - 1):
            if clair(x, y) and not vus[y * w + x]:
                vus[y * w + x] = 1
                file.append((x, y))
    for y in range(h):
        for x in (0, w - 1):
            if clair(x, y) and not vus[y * w + x]:
                vus[y * w + x] = 1
                file.append((x, y))

    while file:
        x, y = file.popleft()
        px[x, y] = (0, 0, 0, 0)
        for dx, dy in ((1, 0), (-1, 0), (0, 1), (0, -1)):
            nx, ny = x + dx, y + dy
            if 0 <= nx < w and 0 <= ny < h and not vus[ny * w + nx] and clair(nx, ny):
                vus[ny * w + nx] = 1
                file.append((nx, ny))
    return im


def teinter(im: Image.Image) -> Image.Image:
    """Multiplie l'image par le crème de la charte : le blanc pur devient le fond
    de page exact, donc invisible, sans toucher à l'alpha."""
    im = im.convert("RGB")
    r, g, b = im.split()
    canaux = [c.point(lambda v, k=k: round(v * k / 255)) for c, k in zip((r, g, b), CREME)]
    return Image.merge("RGB", canaux).convert("RGBA")


def traiter(nom: str) -> pathlib.Path | None:
    src = SRC / f"{nom}.png"
    if not src.exists():
        return None
    if nom in TEINTER:
        im = teinter(Image.open(src))
    else:
        im = detourer(Image.open(src))
        bbox = im.getchannel("A").getbbox()
        if bbox:
            im = im.crop(bbox)
    ratio = HAUTEUR_CIBLE / im.height
    if ratio < 1:
        im = im.resize((round(im.width * ratio), HAUTEUR_CIBLE), Image.LANCZOS)
    OUT.mkdir(parents=True, exist_ok=True)
    dst = OUT / f"{nom}.webp"
    im.save(dst, "WEBP", quality=88, method=6)
    print(f"  {nom:34s} {im.size[0]}×{im.size[1]}  {dst.stat().st_size // 1024} Ko")
    return dst


# Photos de plats, en pastille ronde à gauche des lignes qui nomment un plat
# (fiches du plan 3, lignes de proposition du plan 4). Elles rendent concret ce
# qui reste sinon une liste de libellés — c'est le plat qui perd de la marge,
# pas une ligne de tableau.
PLATS = REPO / "videos/shared-images/plats"
TAILLE_PASTILLE = 220


def pastille(nom: str) -> pathlib.Path | None:
    """Recadre une photo de plat au carré centré, la réduit, et lui applique un
    masque circulaire — le fond crème de la photo disparaît hors du cercle."""
    src = PLATS / f"{nom}.jpg"
    if not src.exists():
        return None
    im = Image.open(src).convert("RGBA")
    cote = min(im.size)
    g, h = (im.width - cote) // 2, (im.height - cote) // 2
    im = im.crop((g, h, g + cote, h + cote)).resize(
        (TAILLE_PASTILLE, TAILLE_PASTILLE), Image.LANCZOS
    )
    # Masque antialiasé : on le dessine 4× trop grand puis on le réduit, sinon
    # le bord du cercle est crénelé et se voit à l'écran.
    k = 4
    masque = Image.new("L", (TAILLE_PASTILLE * k, TAILLE_PASTILLE * k), 0)
    ImageDraw.Draw(masque).ellipse(
        (0, 0, TAILLE_PASTILLE * k - 1, TAILLE_PASTILLE * k - 1), fill=255
    )
    im.putalpha(masque.resize((TAILLE_PASTILLE, TAILLE_PASTILLE), Image.LANCZOS))

    OUT.mkdir(parents=True, exist_ok=True)
    dst = OUT / f"plat-{nom}.webp"
    im.save(dst, "WEBP", quality=90, method=6)
    print(f"  plat-{nom:28s} {TAILLE_PASTILLE}×{TAILLE_PASTILLE}  "
          f"{dst.stat().st_size // 1024} Ko")
    return dst


def main() -> None:
    print(f"Détourage depuis {SRC.relative_to(REPO)}\n")
    manquants = []
    for slug, r in MAPPING.items():
        for role, nom in r.items():
            if traiter(nom) is None:
                manquants.append((slug, role, nom))

    print(f"\nPastilles de plats depuis {PLATS.relative_to(REPO)}\n")
    for nom in sorted(f.stem for f in PLATS.glob("*.jpg")):
        pastille(nom)

    (PROJ / "assets/img/mapping.json").write_text(
        json.dumps(MAPPING, ensure_ascii=False, indent=2) + "\n", encoding="utf-8"
    )
    if manquants:
        print("\nÀ GÉNÉRER (absents de la librairie) :")
        for slug, role, nom in manquants:
            print(f"  {slug} · {role} → {nom}")


if __name__ == "__main__":
    main()
