#!/usr/bin/env python3
"""Produit les livrables Academy : vignettes + manifest-academy.json.

Vignette : la frame la plus lisible du plan 3, c'est-à-dire la cascade à
mi-parcours — le moment où la moitié des maillons sont allumés et où les fiches
touchées clignotent. On la calcule à partir des minutages réels de la VO, pas
d'un timecode deviné : `build_html.minutages` donne le début et la durée exacts
du plan 3, on extrait à son milieu.

Durées : mesurées sur le MP4 final. Le brief demandait ffprobe ; le wheel
`imageio-ffmpeg` ne livre que ffmpeg, mais `ffmpeg -i` expose la même durée de
conteneur — c'est bien le fichier rendu qu'on mesure, jamais le script.

Le manifeste laisse `videoUrl` et `thumbnailUrl` vides : ils ne sont connus
qu'après l'upload RapidoCMS, qui est une publication et attend une validation.
"""
import argparse
import json
import pathlib
import subprocess
import sys

HERE = pathlib.Path(__file__).resolve().parent
PROJ = HERE.parent
sys.path.insert(0, str(HERE))
from build_html import duree_mp3, ffmpeg, minutages  # noqa: E402

TYPES_DEFAUT = {1: 1, 2: 2, 3: 3, 4: 4, 5: 5, 6: 6, 7: 7}
TYPES_PRINCIPE = {1: 1, 2: 2, 3: 5, 4: 2, 5: 7, 6: 6}


def instant_vignette(video: dict) -> float:
    """Milieu du plan 3 (la cascade). Pour la vidéo 0, qui n'a pas de cascade,
    on prend le milieu du plan du ∞ — son image la plus parlante."""
    types = TYPES_PRINCIPE if video["slug"] == "boucle-00-principe" else TYPES_DEFAUT
    tm = minutages(video, PROJ / video["dossier"], exiger_vo=True, types=types)
    cible = 3 if video["slug"] != "boucle-00-principe" else 3
    p = next(t for t in tm if t["n"] == cible)
    return p["start"] + p["dur"] * 0.55


def duree_mp4(path: pathlib.Path) -> float:
    return duree_mp3(path)  # même lecture du conteneur par ffmpeg


def main() -> None:
    ap = argparse.ArgumentParser()
    ap.add_argument("--vignettes", action="store_true", help="extraire les vignettes")
    args = ap.parse_args()

    manifeste = json.loads((PROJ / "boucles.json").read_text(encoding="utf-8"))
    sortie, manquants = [], []

    for video in manifeste["videos"]:
        dossier = PROJ / video["dossier"]
        mp4 = dossier / "out" / f"{video['slug']}.mp4"
        if not mp4.exists():
            manquants.append(video["slug"])
            continue

        vignette = dossier / "out" / f"{video['slug']}-thumbnail.jpg"
        if args.vignettes:
            t = instant_vignette(video)
            r = subprocess.run(
                [ffmpeg(), "-y", "-ss", f"{t:.3f}", "-i", str(mp4),
                 "-frames:v", "1", "-q:v", "3",  # q:v 3 ≈ qualité JPEG 85
                 "-s", "1920x1080", str(vignette)],
                capture_output=True, text=True,
            )
            if r.returncode != 0:
                sys.exit(f"ERREUR vignette {video['slug']} :\n{r.stderr[-1500:]}")
            print(f"  {vignette.name}  t={t:.1f}s  {vignette.stat().st_size // 1024} Ko")

        sortie.append({
            "slug": video["slug"],
            "order": video["ordre"],
            "title": video["titre"],
            "videoUrl": "",
            "thumbnailUrl": "",
            "durationSeconds": round(duree_mp4(mp4)),
            "outilsMcp": video["outilsMcp"],
        })

    cible = PROJ / "manifest-academy.json"
    cible.write_text(json.dumps(sortie, ensure_ascii=False, indent=2) + "\n",
                     encoding="utf-8")
    print(f"\n{len(sortie)} vidéo(s) -> {cible.name}")
    if manquants:
        print(f"NON RENDUES ({len(manquants)}) : {', '.join(manquants)}")


if __name__ == "__main__":
    main()
