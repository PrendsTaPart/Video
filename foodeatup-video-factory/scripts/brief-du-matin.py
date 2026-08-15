#!/usr/bin/env python3
"""Le message de 9 h : ce qu'il y a à fournir aujourd'hui, et rien d'autre.

    python3 scripts/brief-du-matin.py            aujourd'hui
    python3 scripts/brief-du-matin.py 2026-08-20 un jour précis
    python3 scripts/brief-du-matin.py --court    la version notification

`routine-du-jour.py` dit ce qu'il y a à MONTER. Celui-ci dit ce qu'il y a à
FOURNIR — c'est la seule chose qui prenne du temps humain, et c'est donc la
seule chose que le message du matin doit contenir.

Un master demande trois pièces. Deux se fabriquent ici, une non :

    le plan Higgsfield      généré, puis récupéré automatiquement
    le segment HeyGen       à produire — le script est fourni ci-dessous
    les 10 s de tutoriel    à prendre dans le Drive — le sous-dossier est lié

Le brief ne demande jamais un asset dont il a déjà le fichier, et ne demande
jamais plus que le lot du jour. Une liste de deux cent quatre-vingts pièces à
fournir n'est pas un brief : c'est un découragement.
"""
import datetime
import json
import pathlib
import sys

R = pathlib.Path(__file__).resolve().parent.parent
INVENTAIRE = R.parent / "foodeatup-social" / "data" / "series.json"

PAR_JOUR = 15
DRIVE = "https://drive.google.com/drive/folders/1LpWivm0KEPwX5XhNHiw08426NjT6PXHC"

# Le Drive range les 150 tutoriels par module. On donne le lien du sous-dossier
# quand on le connaît : chercher soi-même dans quatorze dossiers, quinze fois
# par jour, c'est une demi-heure perdue par jour.
DOSSIERS = {
    "Configuration": "19xTrrkXtWO3yfJqtC3SIlDgpBjSEc4N9",
    "Configuration boutique": "19xTrrkXtWO3yfJqtC3SIlDgpBjSEc4N9",
    "Équipe & Planning": "1wboT7bVjEwxbhpU9Xgz8sRjjqn9XEd7X",
    "Équipe": "1wboT7bVjEwxbhpU9Xgz8sRjjqn9XEd7X",
    "Comptabilité": "1KlXihMLILGDrlxDuO2d3VCe1ic-kCAw_",
    "HACCP": "10rqzHFjXbjkGi73uJyjt3XQM92eaIMK_",
    "StockVision": "1Ib_pKyJ8_jaFAwtIhkzhtmUU_DCtGSSY",
    "StockVisionAI": "1Ib_pKyJ8_jaFAwtIhkzhtmUU_DCtGSSY",
    "Mon Site": "1ykcHl2BaY22WlCsBA3DuwXaEMvQZUtMF",
    "E-commerce": "1ykcHl2BaY22WlCsBA3DuwXaEMvQZUtMF",
    "Marketing": "1hBc6Axd0DE2ocTiXXKGlmj1dyagOwKFg",
    "Fidélité et marketing": "1hBc6Axd0DE2ocTiXXKGlmj1dyagOwKFg",
    "Les événements": "1hBc6Axd0DE2ocTiXXKGlmj1dyagOwKFg",
    "Communication": "1hBc6Axd0DE2ocTiXXKGlmj1dyagOwKFg",
    "Service": "1z4li_rdzH8yC7VFoWgOa4yMHbbKIAG29",
    "KDS": "1wQAkcP9pY90DLu_sE8GLiI6WYHZuYwq9",
    "La carte à l'écran": "1wQAkcP9pY90DLu_sE8GLiI6WYHZuYwq9",
    "Réservation": "1m6WdjC_iNYWO_4U3LmDuOsc-_Y_DrZLu",
    "Caisse POS": "1nHjH82ig0i-MtQqDmYp131htOSThaPIQ",
    "HubRise": "19D09dNt_jZSKpcwVCU8Mn1OkMLkY_ojd",
    "Caroline": "1SV1XsT61_cDqoRzD8JxehtRoOpyH5LaA",
    "PrediBot": "19kYZliyRnKraKVg1zdFrXCocD38VZ2a9",
}


def lien(module):
    cle = DOSSIERS.get(module)
    return (
        f"https://drive.google.com/drive/folders/{cle}"
        if cle
        else f"{DRIVE}  (module « {module} » : chercher le dossier)"
    )


def etat():
    d = json.load(open(INVENTAIRE, encoding="utf-8"))
    hooks = {p.stem for p in (R / "assets" / "hooks").glob("*.mp4")}
    avatars = {p.stem for p in (R / "assets" / "avatar").glob("*.mp4")}
    softs = {p.stem for p in (R / "assets" / "software").glob("*.mp4")}
    eps = []
    for s in d["series"]:
        for sa in s["saisons"]:
            for e in sa["episodes"]:
                eps.append(dict(
                    id=e["id"], serie=s["nom"], saison=sa["numero"], titre=e["titre"],
                    module=e["module"], chapitre=e["chapitre"],
                    date=e.get("datePrevue") or "9999-99-99",
                    master=bool(e.get("videoUrl")),
                    story=bool((e.get("story") or {}).get("url")),
                    clip=bool(e["higgsfield"].get("videoSourceUrl")) or e["id"] in hooks,
                    prompt=e["higgsfield"].get("prompt"),
                    heygen=e.get("heygenPrompt") or e.get("scriptHeygen"),
                    a_avatar=e["id"] in avatars, a_soft=e["id"] in softs,
                    # UpEatFood est un film : son master EST le plan de dix
                    # secondes. Pas d'avatar, pas d'écran de logiciel — le film
                    # montre le geste et rien d'autre, du premier au dernier
                    # chapitre. Lui réclamer un segment HeyGen et un extrait de
                    # tutoriel, c'est demander deux pièces qui n'existent pas.
                    film=(e.get("dureeSecondes") == 10.0),
                ))
    eps.sort(key=lambda e: (e["date"], e["id"]))
    return eps


def lot(eps):
    """Les quinze prochains masters à produire, dans l'ordre de diffusion.

    Toujours les quinze suivants, jamais « ceux du jour n ». Le brief est sans
    mémoire : ce qui a été produit hier a disparu de la liste, ce qui a glissé y
    est encore. Un lot indexé sur la date se viderait dès qu'on prend un jour
    de retard, et se remplirait de doublons dès qu'on prend de l'avance.
    """
    return [e for e in eps if not e["master"]][:PAR_JOUR]


def numero_du_jour(eps, jour):
    """Le rang du jour depuis le lancement — pour situer, pas pour choisir."""
    depart = datetime.date.fromisoformat(
        min((e["date"] for e in eps if e["date"] != "9999-99-99"), default=jour.isoformat())
    ) - datetime.timedelta(days=1)
    return max(1, (jour - depart).days)


def main(args):
    court = "--court" in args
    arg = next((a for a in args if a[:1].isdigit() and "-" in a), None)
    jour = datetime.date.fromisoformat(arg) if arg else datetime.date.today()

    eps = etat()
    n = numero_du_jour(eps, jour)
    du_jour = lot(eps)
    restants = len([e for e in eps if not e["master"]])

    def complet(e):
        return e["clip"] and (e["film"] or (e["a_avatar"] and e["a_soft"]))

    a_generer = [e for e in du_jour if not e["clip"] and e["prompt"]]
    a_avatar = [e for e in du_jour if not e["film"] and not e["a_avatar"]]
    a_soft = [e for e in du_jour if not e["film"] and not e["a_soft"]]
    pret = [e for e in du_jour if complet(e)]

    if court:
        print(f"Jour {n} — {len(du_jour)} épisodes à produire, {restants} restants. "
              f"À fournir : {len(a_avatar)} segment(s) HeyGen, "
              f"{len(a_soft)} extrait(s) de tutoriel. "
              f"{len(a_generer)} plan(s) à générer, {len(pret)} montable(s) tout de suite.")
        return

    print(f"# Jour {n} — {jour.isoformat()}\n")
    print(f"**{len(du_jour)} épisodes à produire aujourd'hui.** "
          f"Il en reste {restants} sur 337, soit {-(-restants // PAR_JOUR)} jours.\n")
    print("Les épisodes du lot, dans l'ordre où ils sortent :\n")
    for e in du_jour:
        manque = []
        if not e["clip"]:
            manque.append("plan")
        if not e["film"] and not e["a_avatar"]:
            manque.append("HeyGen")
        if not e["film"] and not e["a_soft"]:
            manque.append("tutoriel")
        etat_e = "prêt à monter" if not manque else "il manque " + ", ".join(manque)
        marque = " · film" if e["film"] else ""
        print(f"- `{e['id']}` {e['date']} · {e['serie']} S{e['saison']}{marque} — "
              f"{e['titre']} — *{etat_e}*")

    if a_generer:
        print(f"\n## 1. Plans à générer sur Higgsfield ({len(a_generer)})\n")
        print("Je les récupère tout seul dès qu'ils sont rendus — rien à téléverser.")
        print("Un appel par plan, la photo du chef en référence, jamais en lot.\n")
        for e in a_generer:
            print(f"- `{e['id']}` — prompt dans `docs/higgsfield-prompts-seedance.md`")

    if a_avatar:
        print(f"\n## 2. Segments HeyGen à produire ({len(a_avatar)})\n")
        print("Neuf secondes chacun. Déposer les fichiers dans le chat, "
              "nommés `EPxxx.mp4`.\n")
        for e in a_avatar:
            print(f"\n### `{e['id']}` — {e['titre']}\n")
            print("```")
            print(e["heygen"] or "(pas de script — me le demander)")
            print("```")

    if a_soft:
        print(f"\n## 3. Extraits de tutoriel à prendre dans le Drive ({len(a_soft)})\n")
        print("Dix secondes qui montrent l'écran du module, sans commentaire. "
              "Déposer dans le chat, nommés `EPxxx.mp4`.\n")
        for e in a_soft:
            print(f"- `{e['id']}` · **{e['module']}** — {e['chapitre']}\n"
                  f"  {lien(e['module'])}")

    if pret:
        print(f"\n## Déjà complet, je monte ({len(pret)})\n")
        for e in pret:
            print(f"- `{e['id']}` {e['titre']}")

    print(f"\n---\n\nQuand les fichiers sont dans le chat, je monte les {len(du_jour)} "
          f"masters et leurs stories, je relie, je régénère le site et je pousse.")


if __name__ == "__main__":
    main(sys.argv[1:])
