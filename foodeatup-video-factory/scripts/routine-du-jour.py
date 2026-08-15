#!/usr/bin/env python3
"""La feuille de route du jour : ce qu'il y a à générer, et ce qu'il y a à monter.

    python3 scripts/routine-du-jour.py            le jour en cours du plan
    python3 scripts/routine-du-jour.py 7          le septième jour
    python3 scripts/routine-du-jour.py --plan     les trente et un jours d'un coup

Il reste 465 montages : 179 stories et 286 masters. À quinze par jour, le projet
se termine en trente et un jours. Ce script dit lesquels, dans quel ordre, et ce
qui manque pour chacun.

L'ordre n'est pas arbitraire : on monte dans l'ordre de diffusion. Ce qui sort le
plus tôt se monte le premier, sans quoi on se retrouve avec un stock de saisons
lointaines et rien pour la semaine qui vient.

Un master a besoin de trois pièces sur le disque, et deux ne se fabriquent pas
ici :

    assets/hooks/EPxxx.mp4      le plan Higgsfield — à générer, prompt fourni
    assets/avatar/EPxxx.mp4     le segment HeyGen — à déposer à la main
    assets/software/EPxxx.mp4   dix secondes de tutoriel — à extraire du Drive

Une story n'a besoin que du hook. C'est pourquoi la feuille commence toujours par
les clips à générer : ce sont eux qui débloquent tout le reste, et un clip
demandé aujourd'hui se monte demain.
"""
import datetime
import json
import pathlib
import sys

R = pathlib.Path(__file__).resolve().parent.parent
INVENTAIRE = R.parent / "foodeatup-social" / "data" / "series.json"

PAR_JOUR = 15
CLIPS_PAR_JOUR = 6


def etat():
    """Tout ce qui reste, dans l'ordre de diffusion."""
    d = json.load(open(INVENTAIRE, encoding="utf-8"))
    eps = []
    for s in d["series"]:
        for sa in s["saisons"]:
            for e in sa["episodes"]:
                eps.append(
                    dict(
                        id=e["id"],
                        serie=s["nom"],
                        saison=sa["numero"],
                        ordre=sa.get("ordre", 99),
                        titre=e["titre"],
                        date=e.get("datePrevue") or "9999-99-99",
                        clip=bool(e["higgsfield"].get("videoSourceUrl")),
                        story=bool((e.get("story") or {}).get("url")),
                        master=bool(e.get("videoUrl")),
                        prompt=e["higgsfield"].get("prompt"),
                    )
                )
    eps.sort(key=lambda e: (e["date"], e["id"]))

    hooks = {p.stem for p in (R / "assets" / "hooks").glob("*.mp4")}
    avatars = {p.stem for p in (R / "assets" / "avatar").glob("*.mp4")}
    softs = {p.stem for p in (R / "assets" / "software").glob("*.mp4")}
    for e in eps:
        e["a_le_hook"] = e["id"] in hooks
        e["a_l_avatar"] = e["id"] in avatars
        e["a_le_soft"] = e["id"] in softs
    return eps


def travaux(eps):
    """Les trois files, dans l'ordre de diffusion."""
    a_generer = [e for e in eps if not e["clip"] and not e["a_le_hook"] and e["prompt"]]
    a_storyfier = [e for e in eps if not e["story"] and (e["clip"] or e["a_le_hook"])]
    a_monter = [e for e in eps if not e["master"]]
    return a_generer, a_storyfier, a_monter


def manque(e):
    trous = []
    if not (e["clip"] or e["a_le_hook"]):
        trous.append("le plan Higgsfield")
    if not e["a_l_avatar"]:
        trous.append("le segment HeyGen")
    if not e["a_le_soft"]:
        trous.append("les 10 s de tutoriel")
    return trous


def jour(n, eps, verbeux=True):
    a_generer, a_storyfier, a_monter = travaux(eps)

    # La file du jour ne contient que ce qui est FAISABLE aujourd'hui. Une
    # feuille de route qui liste quinze montages bloqués faute d'assets n'est pas
    # une feuille de route : c'est une liste de courses. Ce qui manque est dit
    # juste après, séparément, pour qu'on sache quoi débloquer.
    #
    # Les stories d'abord à date égale : elles ne demandent qu'un hook, elles ne
    # bloquent jamais, et ce sont elles qui font vivre les réseaux au quotidien.
    faisables = [("story", e) for e in a_storyfier] + [
        ("master", e) for e in a_monter if not manque(e)
    ]
    faisables.sort(key=lambda x: (x[1]["date"], x[1]["id"], x[0] != "story"))

    debut = (n - 1) * PAR_JOUR
    lot = faisables[debut : debut + PAR_JOUR]
    clips = a_generer[(n - 1) * CLIPS_PAR_JOUR : n * CLIPS_PAR_JOUR]

    if not verbeux:
        return lot, clips

    reste = len([e for e in eps if not e["story"]]) + len(a_monter)
    print(f"\n{'═' * 72}")
    print(f"  JOUR {n} — {len(lot)} montage(s) faisable(s) · {len(clips)} plan(s) à générer")
    print(f"  Il reste {reste} montages au total, à {PAR_JOUR} par jour : "
          f"{-(-reste // PAR_JOUR)} jours.")
    print(f"{'═' * 72}")

    if clips:
        print(f"\n▸ 1. À GÉNÉRER SUR HIGGSFIELD ({len(clips)})")
        print("     Un appel par plan, la photo du chef en image de référence, jamais en lot.")
        print("     Les prompts complets sont dans docs/higgsfield-prompts-seedance.md.")
        print("     Déposer les .mp4 dans assets/hooks/ — ils débloquent le lot de demain.\n")
        for e in clips:
            print(f"     {e['id']}  {e['serie'][:18]:18} S{e['saison']} "
                  f"{e['date']}  {e['titre'][:38]}")

    stories = [e for t, e in lot if t == "story"]
    masters = [e for t, e in lot if t == "master"]

    if stories or masters:
        print(f"\n▸ 2. À MONTER MAINTENANT ({len(lot)})\n")
        if stories:
            print(f"     Stories — {len(stories)} · une seule commande :")
            print(f"       python3 scripts/build-stories.py {' '.join(e['id'] for e in stories)}\n")
        if masters:
            print(f"     Masters — {len(masters)} :")
            for e in masters:
                print(f"       ./scripts/build-segment-a.sh {e['id']} && "
                      f"./scripts/build-episode.sh {e['id']} && "
                      f"./scripts/qc-episode.sh {e['id']}")
            print()
    else:
        print("\n▸ 2. RIEN À MONTER AUJOURD'HUI")
        print("     Tout ce qui sort bientôt attend un asset. La liste est juste en dessous :")
        print("     générer les plans, déposer les avatars, et le lot de demain sera plein.\n")

    # Ce qu'il faut débloquer pour que les prochains jours soient pleins — les
    # dix premiers dans l'ordre de diffusion suffisent à remplir un lot.
    bloques = [e for e in a_monter if manque(e)][:10]
    if bloques:
        print(f"▸ 3. À DÉBLOQUER ({len([e for e in a_monter if manque(e)])} masters en attente, "
              f"les 10 plus urgents)\n")
        for e in bloques:
            print(f"     {e['id']}  {e['date']}  {e['serie'][:16]:16} — "
                  f"il manque {', '.join(manque(e))}")
        print()

    print(f"▸ 4. QUAND C'EST FAIT\n"
          f"     python3 scripts/lier-clips-et-stories.py\n"
          f"     python3 scripts/gen-site-data.py\n"
          f"     puis copier src/data/*.ts sur le site, et pousser.\n")
    return lot, clips


def plan(eps):
    a_generer, a_storyfier, a_monter = travaux(eps)
    # Le total du plan compte TOUTES les stories qui manquent, y compris celles
    # dont le clip n'existe pas encore : elles se débloqueront au fil des
    # générations. Ne compter que celles qui sont montables aujourd'hui donne un
    # plan qui rallonge chaque jour au lieu de raccourcir.
    stories_a_venir = [e for e in eps if not e["story"]]
    total = len(stories_a_venir) + len(a_monter)
    jours = -(-total // PAR_JOUR)
    print(f"\n{total} montages à faire — {len(stories_a_venir)} stories, "
          f"{len(a_monter)} masters.")
    print(f"Dont {len(a_storyfier)} story(ies) montables tout de suite ; les autres "
          f"attendent leur plan.")
    print(f"{len(a_generer)} plans Higgsfield à générer.")
    print(f"À {PAR_JOUR} montages par jour : {jours} jours.\n")
    aujourdhui = datetime.date.today()
    print(f"{'Jour':>4}  {'Date':10}  {'Montages':>8}  {'Clips':>5}  Ce qui sort en premier ce jour-là")
    print("─" * 78)
    for n in range(1, jours + 1):
        lot, clips = jour(n, eps, verbeux=False)
        if not lot:
            break
        d = (aujourdhui + datetime.timedelta(days=n - 1)).isoformat()
        tete = lot[0][1]
        print(f"{n:>4}  {d}  {len(lot):>8}  {len(clips):>5}  "
              f"{tete['serie'][:16]:16} S{tete['saison']} · {tete['titre'][:26]}")


def main(args):
    eps = etat()
    if "--plan" in args:
        plan(eps)
        return
    n = next((int(a) for a in args if a.isdigit()), 1)
    jour(n, eps)


if __name__ == "__main__":
    main(sys.argv[1:])
