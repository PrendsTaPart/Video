#!/usr/bin/env python3
"""Donne une date aux 62 épisodes des séries 2 et 3.

    python3 scripts/dater-series-2-3.py

« Une journée » et « L'IA dans FoodEatUp » ont été écrites en entier — titres,
plans Higgsfield, scripts HeyGen, cinq publications par épisode — mais sans
aucune date : elles n'étaient pas publiées, elles n'avaient pas à occuper de
place dans la grille. Elles y reviennent, il leur faut donc leur créneau.

La règle est celle du calendrier : un épisode par jour, tous les jours, et les
cinq réseaux à des heures décalées pour qu'un même épisode ne tombe pas cinq
fois au même moment. Les deux séries s'enchaînent à la suite du Coup de Feu,
dans l'ordre de l'inventaire — jamais en parallèle : deux épisodes le même jour,
ce sont deux publications qui se disputent le même fil.

Le script est rejouable : il repart toujours de la dernière date occupée par une
autre série, donc le relancer après avoir ajouté des épisodes au Coup de Feu
décale proprement les deux séries au lieu de créer un chevauchement.
"""
import datetime
import json
import os

R = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
INVENTAIRE = os.path.join(os.path.dirname(R), "foodeatup-social", "data", "series.json")

# Les deux séries à dater, dans l'ordre de diffusion voulu.
A_DATER = ("une-journee", "lia-dans-foodeatup")


def main():
    d = json.load(open(INVENTAIRE, encoding="utf-8"))
    heures = {c["reseau"]: c["heure"] for c in d["calendrier"]["creneaux"]}

    # Le point de départ : le lendemain du dernier jour déjà pris par une série
    # qu'on ne touche pas. Le lire au lieu de l'écrire en dur, c'est ce qui rend
    # le script rejouable.
    occupees = [
        e["datePrevue"]
        for s in d["series"]
        if s["slug"] not in A_DATER
        for sa in s["saisons"]
        for e in sa["episodes"]
        if e.get("datePrevue")
    ]
    jour = datetime.date.fromisoformat(max(occupees)) + datetime.timedelta(days=1)
    depart = jour

    par_slug = {s["slug"]: s for s in d["series"]}
    resume = []
    for slug in A_DATER:
        s = par_slug[slug]
        premier = jour
        for sa in s["saisons"]:
            for e in sa["episodes"]:
                iso = jour.isoformat()
                e["datePrevue"] = iso
                for reseau, p in e["reseaux"].items():
                    p["date"] = iso
                    # L'heure vient du calendrier, pas de l'épisode : une série
                    # qui publierait à ses propres horaires casserait le décalage
                    # entre les cinq fils.
                    p["heure"] = heures.get(reseau, p.get("heure"))
                jour += datetime.timedelta(days=1)
        resume.append((s["nom"], premier, jour - datetime.timedelta(days=1)))

    open(INVENTAIRE, "w", encoding="utf-8").write(json.dumps(d, ensure_ascii=False, indent=2))

    print(f"Reprise de la grille au {depart.isoformat()}")
    for nom, a, b in resume:
        print(f"  {nom:28} {a.isoformat()} → {b.isoformat()}")

    # Un jour ne peut porter qu'un épisode : la grille est un fil, pas un tas.
    toutes = [
        e["datePrevue"]
        for s in d["series"]
        for sa in s["saisons"]
        for e in sa["episodes"]
        if e.get("datePrevue")
    ]
    doublons = {x for x in toutes if toutes.count(x) > 1}
    print(f"  {len(toutes)} épisodes datés, {len(doublons)} collision(s)")
    if doublons:
        raise SystemExit(f"dates en double : {sorted(doublons)[:5]}")


if __name__ == "__main__":
    main()
