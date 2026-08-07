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

from PIL import Image

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


def traiter(nom: str) -> pathlib.Path | None:
    src = SRC / f"{nom}.png"
    if not src.exists():
        return None
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


def main() -> None:
    print(f"Détourage depuis {SRC.relative_to(REPO)}\n")
    manquants = []
    for slug, r in MAPPING.items():
        for role, nom in r.items():
            if traiter(nom) is None:
                manquants.append((slug, role, nom))

    (PROJ / "assets/img/mapping.json").write_text(
        json.dumps(MAPPING, ensure_ascii=False, indent=2) + "\n", encoding="utf-8"
    )
    if manquants:
        print("\nÀ GÉNÉRER (absents de la librairie) :")
        for slug, role, nom in manquants:
            print(f"  {slug} · {role} → {nom}")


if __name__ == "__main__":
    main()
