#!/usr/bin/env python3
"""Repère, dans l'historique Higgsfield, les plans générés à la main qui
n'ont pas encore de place dans l'inventaire.

    python3 scripts/veille-higgsfield.py page1.json [page2.json ...]

RÉCUPÉRATION SEULE, et c'est le cœur du sujet. Ce script ne génère rien et
n'appelle aucune API payante : il lit des pages d'historique déjà obtenues
via show_generations, les rapproche de ce que le dépôt attend, et écrit un
ordre de travail. Rien d'autre.

La règle est dans CLAUDE.md et elle ne se contourne pas : les plans sont
générés à la main, dans l'interface Higgsfield. L'automate ne fait que
constater ce qui est arrivé et le monter.

Ce qu'il sait rapprocher
------------------------
Deux familles de cibles, reconnues au même endroit — les répliques entre
accolades du prompt, seul lien fiable entre un job et sa destination :

  * les épisodes, par leur `higgsfield.prompt` ;
  * les bandes-annonces de saison, par leur `ouverture` et leur `chute`.

L'appariement est STRICT : toutes les répliques attendues doivent être
présentes, et un prompt portant la mention BANDE-ANNONCE ne peut pas être
pris pour un épisode. Cette sévérité a une histoire — un appariement laxiste,
qui se contentait d'une réplique en commun, a fait publier la bande-annonce
d'UpEatFood à la place de l'épisode EP535, les deux partageant la phrase
« Il était une fois un restaurant. ». Une prise mal rapprochée coûte plus
cher qu'une prise non reconnue : la première se publie, la seconde attend.

Ce qu'il produit
----------------
`state/veille.json` : ce qui est nouveau, ce qui est déjà en place, et ce
qui reste attendu. Le rapport est lisible à l'œil et exploitable par la
suite du pipeline, qui n'a plus qu'à dérouler fetch → montage → publication.
"""
import json
import pathlib
import re
import sys

R = pathlib.Path(__file__).resolve().parent.parent
SERIES = R.parent / "foodeatup-social" / "data" / "series.json"
SORTIE = R / "state" / "veille.json"


def repliques(prompt):
    """Les phrases entre accolades — ce que la voix dit dans le plan."""
    return {m.strip() for m in re.findall(r"\{([^{}]{5,200})\}", prompt or "")}


def cibles():
    """Tout ce que le dépôt attend d'Higgsfield, épisodes et bandes-annonces."""
    d = json.loads(SERIES.read_text(encoding="utf-8"))
    out = {}
    for s in d["series"]:
        for sa in s["saisons"]:
            ba = sa.get("bandeAnnonce")
            if ba:
                attendu = {(ba.get("ouverture") or "").strip(),
                           (ba.get("chute") or "").strip()} - {""}
                if attendu:
                    out[f"BA:{s['slug']}-S{sa['numero']}"] = {
                        "genre": "bande-annonce",
                        "titre": f"{s['nom']} — saison {sa['numero']} : {sa['titre']}",
                        "repliques": attendu,
                        "servi": bool(ba.get("url")),
                        "date": ba.get("date"),
                    }
            for e in sa["episodes"]:
                attendu = repliques((e.get("higgsfield") or {}).get("prompt"))
                if attendu:
                    out[f"EP:{e['id']}"] = {
                        "genre": "épisode",
                        "titre": e["titre"],
                        "repliques": attendu,
                        "servi": bool((e.get("higgsfield") or {}).get("videoSourceUrl")),
                        "date": e.get("datePrevue"),
                    }
    return out


def main(fichiers):
    if not fichiers:
        sys.exit("usage: veille-higgsfield.py <page1.json> [page2.json ...]\n"
                 "Les pages viennent de show_generations(type=\"video\"), "
                 "rappelé avec next_cursor jusqu'à épuisement.")

    jobs = []
    for f in fichiers:
        jobs += json.loads(pathlib.Path(f).read_text(encoding="utf-8")).get("items", [])

    cbl = cibles()
    trouve = {}
    for j in jobs:
        if j.get("status") != "completed":
            continue
        url = (j.get("results") or {}).get("rawUrl")
        prompt = (j.get("params") or {}).get("prompt") or ""
        if not url:
            continue
        rj = repliques(prompt)
        if not rj:
            continue
        est_ba = "BANDE-ANNONCE" in prompt
        for cle, c in cbl.items():
            # Un plan de bande-annonce ne peut pas servir d'épisode, ni
            # l'inverse : c'est ce garde-fou qui a manqué la première fois.
            if est_ba != cle.startswith("BA:"):
                continue
            if c["repliques"] <= rj:
                trouve.setdefault(cle, []).append(
                    {"job": j["id"], "url": url, "at": j.get("createdAt", 0)})
                break

    for v in trouve.values():
        v.sort(key=lambda x: -x["at"])

    nouveaux = {k: v for k, v in trouve.items() if not cbl[k]["servi"]}
    attendus = [k for k, c in cbl.items() if not c["servi"] and k not in trouve]

    rapport = {
        "jobs_lus": len(jobs),
        "cibles": len(cbl),
        "deja_servies": sum(1 for c in cbl.values() if c["servi"]),
        "a_monter": {k: {"titre": cbl[k]["titre"], "date": cbl[k]["date"],
                         "prises": v} for k, v in sorted(nouveaux.items())},
        "toujours_attendus": [{"cle": k, "titre": cbl[k]["titre"],
                               "date": cbl[k]["date"]} for k in sorted(attendus)],
    }
    SORTIE.parent.mkdir(parents=True, exist_ok=True)
    SORTIE.write_text(json.dumps(rapport, ensure_ascii=False, indent=2) + "\n",
                      encoding="utf-8")

    print(f"jobs lus          : {len(jobs)}")
    print(f"cibles du dépôt   : {len(cbl)} ({rapport['deja_servies']} déjà servies)")
    print(f"à monter          : {len(nouveaux)}")
    for k, v in sorted(nouveaux.items()):
        print(f"  {k:38s} {cbl[k]['titre'][:44]:46s} {len(v)} prise(s)")
    print(f"toujours attendus : {len(attendus)}")
    for k in sorted(attendus)[:12]:
        print(f"  {k:38s} {cbl[k]['titre'][:44]}")
    if len(attendus) > 12:
        print(f"  … et {len(attendus) - 12} autres")
    print(f"\nrapport : {SORTIE.relative_to(R)}")


if __name__ == "__main__":
    main(sys.argv[1:])
