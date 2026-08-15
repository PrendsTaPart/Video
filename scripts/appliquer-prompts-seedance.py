# -*- coding: utf-8 -*-
"""
Pose les prompts Seedance 2.5 dans l'inventaire, à la place des anciens.

Les prompts Higgsfield d'origine ont été écrits pour un modèle muet. Seedance
2.5 fabrique le son avec l'image : il lit un découpage en secondes, des bruits
balisés un par un, et des répliques. La réécriture des 94 plans encore sans clip
a été faite côté site, où vivent l'accroche, la punchline et la phrase de chaque
épisode — c'est de là que vient la voix des personnages.

Ce script rapatrie le résultat ici, dans la seule source qui compte :
`foodeatup-social/data/series.json`. Sans ce passage, la prochaine exécution de
`gen-site-data.py` rendrait au site ses prompts d'avant.

  python3 scripts/appliquer-prompts-seedance.py
"""
import json
import os

RACINE = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
INVENTAIRE = os.path.join(RACINE, "foodeatup-social", "data", "series.json")
RELAIS = os.path.join(RACINE, "foodeatup-social", "data", "prompts-seedance.json")


def main():
    d = json.load(open(INVENTAIRE, encoding="utf-8"))
    prompts = json.load(open(RELAIS, encoding="utf-8"))

    poses, deja, absents = 0, 0, dict(prompts)
    for s in d["series"]:
        for sa in s["saisons"]:
            for e in sa["episodes"]:
                neuf = prompts.get(e["id"])
                if neuf is None:
                    continue
                absents.pop(e["id"], None)
                # Un plan déjà tourné garde le prompt qui l'a produit : le site
                # montre le clip juste à côté, les deux doivent se répondre.
                if e["higgsfield"].get("videoSourceUrl"):
                    continue
                if e["higgsfield"].get("prompt") == neuf:
                    deja += 1
                    continue
                e["higgsfield"]["prompt"] = neuf
                poses += 1

    # L'inventaire n'a pas de saut de ligne final : le réécrire tel quel évite
    # un diff d'un octet à chaque passage.
    open(INVENTAIRE, "w", encoding="utf-8").write(
        json.dumps(d, ensure_ascii=False, indent=2)
    )
    print(f"series.json : {poses} prompt(s) posé(s), {deja} déjà à jour")
    if absents:
        print(f"⚠️ absents de l'inventaire : {', '.join(sorted(absents))}")


if __name__ == "__main__":
    main()
