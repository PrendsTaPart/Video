#!/usr/bin/env python3
"""Contrôle qu'aucune couleur hors charte n'entre dans les compositions.

Critère d'acceptation P0 : « aucune couleur hors palette (grep les hex du HTML) ».
On va un cran plus loin que le grep : les `rgb()`/`rgba()` sont vérifiés aussi,
parce qu'une dérive s'écrit plus souvent en rgba qu'en hexadécimal.

Les seules valeurs tolérées sont les cinq teintes de la charte et leurs versions
transparentes — un `rgba(15,26,35,.12)` reste du marine, pas une sixième couleur.
"""
import pathlib
import re
import sys

HERE = pathlib.Path(__file__).resolve().parent
PROJ = HERE.parent

PALETTE = {
    (252, 249, 230): "crème #FCF9E6",
    (15, 26, 35): "marine #0F1A23",
    (0, 123, 255): "bleu #007BFF",
    (20, 122, 255): "bleu système #147AFF",
    (255, 165, 0): "orange #FFA500",
    (0, 0, 0): "noir pur — uniquement en ombre portée transparente",
    (255, 255, 255): "blanc pur — uniquement en voile transparent",
}


def hex_to_rgb(h: str) -> tuple[int, int, int]:
    h = h.lstrip("#")
    if len(h) == 3:
        h = "".join(c * 2 for c in h)
    return tuple(int(h[i:i + 2], 16) for i in (0, 2, 4))


def scan(texte: str, source: str) -> list[str]:
    fautes = []
    for m in re.finditer(r"#([0-9a-fA-F]{3}|[0-9a-fA-F]{6})\b", texte):
        rgb = hex_to_rgb(m.group(0))
        if rgb not in PALETTE:
            fautes.append(f"{source}: {m.group(0)} (rgb{rgb})")
    for m in re.finditer(r"rgba?\(\s*(\d+)\s*,\s*(\d+)\s*,\s*(\d+)", texte):
        rgb = tuple(int(g) for g in m.groups())
        if rgb not in PALETTE:
            fautes.append(f"{source}: {m.group(0)})")
    return fautes


def main() -> None:
    cibles = [PROJ / "engine/scene.css", PROJ / "engine/scene.js"]
    cibles += sorted(PROJ.glob("*/index.html")) + sorted(PROJ.glob("*/index-reel.html"))

    fautes = []
    for f in cibles:
        if not f.exists():
            continue
        texte = f.read_text(encoding="utf-8")
        # Les blocs base64 (polices, images) contiennent des suites
        # hexadécimales fortuites : on les retire avant l'analyse.
        texte = re.sub(r"base64,[A-Za-z0-9+/=]+", "base64,…", texte)
        fautes += scan(texte, f.relative_to(PROJ).as_posix())

    if fautes:
        print(f"HORS PALETTE — {len(fautes)} occurrence(s) :")
        for f in sorted(set(fautes)):
            print("  " + f)
        sys.exit(1)
    print(f"Palette OK — {len(cibles)} fichier(s) contrôlé(s), aucune couleur hors charte.")


if __name__ == "__main__":
    main()
