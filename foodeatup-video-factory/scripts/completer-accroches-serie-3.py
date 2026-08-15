#!/usr/bin/env python3
"""Donne une accroche à part entière aux 25 épisodes qui n'en avaient pas.

    python3 scripts/completer-accroches-serie-3.py

« L'IA dans FoodEatUp » a été écrite avec un champ `concept` facultatif, et
l'accroche retombait sur le titre quand il manquait. Sur la page de saison, la
carte affichait donc son titre puis, juste en dessous, exactement le même texte
entre guillemets — vingt-cinq fois.

L'accroche n'est pas un sous-titre : c'est la phrase dite entre 0,6 s et 3,6 s
du montage, celle qui est incrustée sur la vignette et envoyée en description
aux moteurs. Elle doit tenir seule, et être plus courte que le titre.

Le script est rejouable : il ne touche que les épisodes dont l'accroche est
encore égale au titre.
"""
import json
import os

R = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
INVENTAIRE = os.path.join(os.path.dirname(R), "foodeatup-social", "data", "series.json")

ACCROCHES = {
    "EP401": "Ce n'est pas un cours d'informatique. C'est votre restaurant.",
    "EP408": "Une des deux moitiés ne se voit jamais depuis la salle.",
    "EP409": "Une fiche technique fausse, et tout le reste est faux avec elle.",
    "EP410": "Combien de couverts vous pouvez servir. Vraiment.",
    "EP411": "Ce qu'il reste dans le frigo décide de ce qu'on vend ce soir.",
    "EP412": "Celle-là ne coûte pas de la marge. Elle coûte les clés.",
    "EP413": "Vos clients, ou les clients de la plateforme ?",
    "EP414": "Rien ne casse. Tout ralentit.",
    "EP415": "Faire revenir coûte moins cher que faire venir.",
    "EP416": "Savoir si on gagne de l'argent avant la fin du mois.",
    "EP417": "Au milieu du huit, quatre choses se croisent.",
    "EP418": "Claude, ChatGPT ou Mistral : c'est vous qui choisissez.",
    "EP419": "Quatre agents, et pas une seule case vide.",
    "EP420": "Le téléphone sonne en plein coup de feu.",
    "EP421": "Les mains dans la farine, on ne tape pas au clavier.",
    "EP422": "« Combien me coûte mon burger, maintenant ? »",
    "EP423": "Deux logiciels, et aucun ne fait le travail de l'autre.",
    "EP424": "Un bac de saumon qui descend, un post qui monte.",
    "EP425": "La même phrase, mais dite.",
    "EP426": "Une phrase, une photo, dix secondes de publicité.",
    "EP427": "Trente mots, pas un de plus.",
    "EP428": "Et si on payait pour exactement la même chose ?",
    "EP429": "Apprendre un geste une fois, et ne plus jamais l'expliquer.",
    "EP430": "Ce qui part sans que personne l'ait demandé.",
    "EP431": "Les douze kilos repartent, et cette fois on voit tout.",
}


def main():
    d = json.load(open(INVENTAIRE, encoding="utf-8"))
    posees, deja, inconnus = 0, 0, dict(ACCROCHES)
    for s in d["series"]:
        for sa in s["saisons"]:
            for e in sa["episodes"]:
                neuve = ACCROCHES.get(e["id"])
                if not neuve:
                    continue
                inconnus.pop(e["id"], None)
                if e["accroche"] == neuve:
                    deja += 1
                elif e["accroche"].strip() == e["titre"].strip():
                    e["accroche"] = neuve
                    posees += 1
                else:
                    # Une accroche déjà écrite à la main prime : ce script
                    # comble un trou, il n'écrase pas un choix éditorial.
                    deja += 1

    open(INVENTAIRE, "w", encoding="utf-8").write(json.dumps(d, ensure_ascii=False, indent=2))
    print(f"series.json : {posees} accroche(s) posée(s), {deja} laissée(s) telle(s) quelle(s)")
    if inconnus:
        print(f"⚠️ épisodes inconnus de l'inventaire : {', '.join(sorted(inconnus))}")

    restants = [
        e["id"]
        for s in d["series"]
        for sa in s["saisons"]
        for e in sa["episodes"]
        if e["accroche"].strip() == e["titre"].strip()
    ]
    print(f"  {len(restants)} épisode(s) où l'accroche répète encore le titre")
    if restants:
        print(f"  {', '.join(restants)}")


if __name__ == "__main__":
    main()
