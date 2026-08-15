#!/usr/bin/env python3
"""Relie à l'inventaire les clips et les stories présents sur le disque.

    python3 scripts/lier-clips-et-stories.py

Un fichier dans `dist/hooks/` ou `dist/stories/` ne sert à rien tant que
l'inventaire ne porte pas son adresse : le site lit l'inventaire, pas le disque.
Vingt-quatre clips récupérés sur Higgsfield ont vécu plusieurs semaines dans ce
trou — écrits directement sur le site, jamais rapatriés ici, puis effacés à la
première régénération. Ce script ferme le trou dans les deux sens : ce qui est
sur le disque obtient une adresse, et ce qui avait déjà une adresse sur le site
la retrouve.

Deux hébergements, et ce n'est pas un hasard :

  `clips-du-site.json` porte les adresses S3 de RapidoCMS, pour les clips qui y
  ont été téléversés. Elles priment : c'est l'hébergement de production.

  Tout le reste est servi depuis ce dépôt, par `raw.githubusercontent.com` —
  c'est déjà le cas des cent quarante-six stories. Un fichier commité ne
  disparaît pas ; une URL de CDN de générateur, si.

Le script ne remplace jamais une adresse déjà posée.
"""
import json
import os
import pathlib

R = pathlib.Path(__file__).resolve().parent.parent
SOCIAL = R.parent / "foodeatup-social"
INVENTAIRE = SOCIAL / "data" / "series.json"
REPRISES = SOCIAL / "data" / "clips-du-site.json"

BRANCHE = "claude/foodeatup-video-factory-wtb7gs"
BRUT = f"https://raw.githubusercontent.com/PrendsTaPart/Video/{BRANCHE}/foodeatup-video-factory/dist"


def main():
    d = json.load(open(INVENTAIRE, encoding="utf-8"))
    reprises = json.load(open(REPRISES, encoding="utf-8")) if REPRISES.exists() else {}

    hooks = {p.stem for p in (R / "dist" / "hooks").glob("*.mp4")}
    stories = {p.stem for p in (R / "dist" / "stories").glob("*.mp4")}

    clips, sts, deja = 0, 0, 0
    for s in d["series"]:
        for sa in s["saisons"]:
            for e in sa["episodes"]:
                i = e["id"]
                repris = reprises.get(i, {})

                if not e["higgsfield"].get("videoSourceUrl"):
                    url = repris.get("videoSourceUrl") or (
                        f"{BRUT}/hooks/{i}.mp4" if i in hooks else None
                    )
                    if url:
                        e["higgsfield"]["videoSourceUrl"] = url
                        clips += 1
                else:
                    deja += 1

                url = repris.get("storyUrl") or (
                    f"{BRUT}/stories/{i}.mp4" if i in stories else None
                )
                st = e.get("story")
                if url and not (st or {}).get("url"):
                    # Neuf saisons 6 n'avaient pas de fiche story du tout : leur
                    # montage existait sur le disque et restait invisible faute
                    # d'un objet où poser l'adresse. Le hook et la punchline
                    # d'une story sont, par construction, ceux de l'épisode.
                    if st is None:
                        st = e["story"] = {
                            "format": "9:16 · 1080 × 1920 · 10 s",
                            "hook": e["accroche"].rstrip("."),
                            "punchline": e["punchline"].rstrip("."),
                            "url": None,
                        }
                    st["url"] = url
                    sts += 1

    open(INVENTAIRE, "w", encoding="utf-8").write(json.dumps(d, ensure_ascii=False, indent=2))

    eps = [e for s in d["series"] for sa in s["saisons"] for e in sa["episodes"]]
    total_clips = sum(1 for e in eps if e["higgsfield"].get("videoSourceUrl"))
    total_st = sum(1 for e in eps if (e.get("story") or {}).get("url"))
    print(f"{clips} clip(s) et {sts} story(ies) reliés — {deja} clips l'étaient déjà")
    print(f"inventaire : {total_clips} clips, {total_st} stories sur {len(eps)} épisodes")

    orphelins = sorted(hooks - {e["id"] for e in eps})
    if orphelins:
        print(f"⚠️ fichiers sans épisode : {', '.join(orphelins)}")


if __name__ == "__main__":
    main()
