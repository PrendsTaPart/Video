#!/usr/bin/env python3
"""Construit la conduite du clip : quelle fenêtre de quel plan, à quelle seconde.

    python3 scripts/clip-timeline.py            → clip-musical/conduite.json

Trois fichiers commandent le résultat, et aucun n'est deviné ici :
  work/beatgrid.json               le tempo mesuré sur l'audio
  clip-musical/sections.json       les bornes relevées sur le profil d'énergie
  clip-musical/plan-des-plans.json quels plans vont dans quelle section

La règle qui fait tout le travail : **aucune fenêtre n'est consommée deux
fois**. Un plan de 10 s peut revenir dans plusieurs sections, mais jamais avec
les mêmes images — sinon le clip se répète et ça se voit tout de suite. Chaque
source garde donc un curseur, et une fenêtre déjà servie ne ressort pas.
"""
import json
from pathlib import Path

RACINE = Path(__file__).resolve().parent.parent

# Le clip sort à 30 images par seconde, et c'est l'image — pas la seconde — qui
# est l'unité de montage. Une coupe de 0,65 s vaut 19,5 images : si chaque coupe
# arrondit dans son coin, les cent trente et une coupes accumulent près de cinq
# secondes et le refrain final ne tombe plus sur la musique. On quantifie donc
# la ligne de temps ABSOLUE : la borne de chaque coupe est un numéro d'image, et
# c'est la durée qui absorbe l'arrondi, jamais la position.
FPS = 30

# Bornes utiles d'un plan de 10 s. On écarte le début et la fin : la première
# demi-seconde d'un plan Seedance est souvent une amorce, et la dernière image
# porte parfois un fondu.
DEBUT_UTILE, FIN_UTILE = 0.35, 9.85


def repartir(beats_total: int, par_coupe, nb_plans: int) -> list[int]:
    """Longueur de chaque coupe, en temps, pour une section.

    `par_coupe` vaut un entier (longueur constante), une paire [a, b] (on
    resserre de a vers b), 0 (la section tient en une seule coupe), ou
    « un-par-plan » (exactement une coupe par plan de la section).
    """
    if par_coupe == 0:
        return [beats_total]
    if par_coupe == "un-par-plan":
        # « Un plan par épisode, les trente » : le nombre de coupes est fixé par
        # la liste, pas par le tempo. Les temps en trop s'ajoutent à quelques
        # coupes réparties régulièrement, pour que rien ne traîne au même
        # endroit — et surtout pour qu'aucun épisode ne repasse après le
        # trentième, ce qui se lirait comme une erreur de montage.
        base, reste = divmod(beats_total, nb_plans)
        coupes = [base] * nb_plans
        for k in range(reste):
            coupes[(k * nb_plans) // max(1, reste)] += 1
        return coupes
    if isinstance(par_coupe, list):
        a, b = par_coupe
        # Moitié de la section au rythme large, moitié au rythme serré : c'est
        # ce qui s'entend dans le texte, où l'énumération s'accélère.
        moitie = beats_total // 2
        coupes = [a] * (moitie // a)
        reste = beats_total - sum(coupes)
        coupes += [b] * (reste // b)
    else:
        coupes = [par_coupe] * (beats_total // par_coupe)
    # Le reliquat va à la dernière coupe : une section finit sur une mesure,
    # jamais sur un bout de temps.
    reste = beats_total - sum(coupes)
    if reste:
        coupes[-1] += reste
    return coupes


class Fenetres:
    """Distributeur de fenêtres, une source à la fois, sans recouvrement."""

    def __init__(self) -> None:
        self.curseur: dict[tuple[int, int], float] = {}

    def prendre(self, plan: tuple[int, int], duree: float) -> float:
        t = self.curseur.get(plan, DEBUT_UTILE)
        if t + duree > FIN_UTILE:
            # Le plan est épuisé : on repart du début. Cela n'arrive que si une
            # section demande plus de 9,5 s à une même source ; le cas est
            # signalé pour qu'on le voie plutôt que de le subir.
            print(f"   ⚠️  ep{plan[0]:02d} scène {plan[1]} : fenêtres épuisées, "
                  f"le plan est repris depuis le début")
            t = DEBUT_UTILE
        self.curseur[plan] = t + duree
        return round(t, 4)


def main() -> None:
    grille = json.loads((RACINE / "work/beatgrid.json").read_text(encoding="utf-8"))
    secs = json.loads((RACINE / "clip-musical/sections.json").read_text(encoding="utf-8"))
    plans = json.loads((RACINE / "clip-musical/plan-des-plans.json").read_text(encoding="utf-8"))
    par_section = {s["nom"]: [tuple(p) for p in s["plans"]] for s in plans["sections"]}

    battement = grille["intervalle_s"]
    depart = grille["premier_temps_s"]
    duree_totale = grille["duree_s"]
    fenetres = Fenetres()
    conduite = []

    for s in secs["sections"]:
        nom = s["nom"]
        # La première section démarre à zéro et non au premier temps : sans
        # cela, les 0,16 s d'amorce de la chanson resteraient sur un écran noir.
        t0 = (0.0 if s["mesure_debut"] == 0
              else depart + s["mesure_debut"] * 4 * battement)
        t1 = (depart + s["mesure_fin"] * 4 * battement
              if s["mesure_fin"] is not None else duree_totale)
        beats = round((t1 - t0) / battement)
        liste = par_section[nom]
        coupes = repartir(beats, s["coupe_beats"], len(liste))

        t = t0
        for i, nb in enumerate(coupes):
            duree = nb * battement
            # La dernière coupe de la dernière section va jusqu'au bout de la
            # chanson, pas jusqu'au dernier temps de la grille.
            if s["mesure_fin"] is None and i == len(coupes) - 1:
                duree = duree_totale - t
            plan = liste[i % len(liste)]
            source = (RACINE / f"renders/ep{plan[0]:02d}/source/"
                      f"ep{plan[0]:02d}-scene{plan[1]}.mp4")
            if not source.exists():
                raise SystemExit(f"manque {source}")
            # Une coupe plus longue que la source est jouée au ralenti, d'un
            # seul tenant : c'est le cas du pont et de l'outro.
            dispo = FIN_UTILE - DEBUT_UTILE
            if duree > dispo:
                debut, ralenti = DEBUT_UTILE, round(duree / dispo, 5)
                prise = dispo
            else:
                debut, ralenti, prise = fenetres.prendre(plan, duree), 1.0, duree
            conduite.append({
                "section": nom, "i": len(conduite),
                "t": round(t, 4), "duree": round(duree, 4),
                "image_debut": round(t * FPS),
                "episode": plan[0], "scene": plan[1],
                "source": str(source.relative_to(RACINE)),
                "fenetre_debut": debut, "fenetre_duree": round(prise, 4),
                "ralenti": ralenti,
            })
            t += duree

    # Bornes en images : celle de chaque coupe est le début de la suivante, et
    # la dernière tombe sur la dernière image de la chanson. Aucune coupe ne peut
    # donc dériver, quelle que soit la cadence de la source.
    fin_totale = round(duree_totale * FPS)
    for k, c in enumerate(conduite):
        image_fin = conduite[k + 1]["image_debut"] if k + 1 < len(conduite) else fin_totale
        c["images"] = image_fin - c["image_debut"]
        c["duree"] = round(c["images"] / FPS, 4)
        if c["ralenti"] != 1.0:
            # Le ralenti est recalculé sur la durée réellement demandée en
            # images, sinon il rate sa cible de quelques dixièmes.
            c["ralenti"] = round(c["duree"] / c["fenetre_duree"], 5)

    somme = sum(c["images"] for c in conduite)
    assert somme == fin_totale, f"{somme} images pour {fin_totale} attendues"

    sortie = RACINE / "clip-musical/conduite.json"
    sortie.write_text(json.dumps({
        "chanson": secs["chanson"],
        "bpm_mesure": secs["bpm_mesure"],
        "duree_s": duree_totale,
        "fps": FPS,
        "images": fin_totale,
        "coupes": len(conduite),
        "plans": conduite,
    }, ensure_ascii=False, indent=1) + "\n", encoding="utf-8")

    print(f"✅ {sortie.relative_to(RACINE)} — {len(conduite)} coupes sur "
          f"{duree_totale:.2f} s")
    for s in secs["sections"]:
        n = [c for c in conduite if c["section"] == s["nom"]]
        d = sum(c["duree"] for c in n)
        print(f"   {s['nom']:<14s} {len(n):3d} coupes  {d:6.2f} s  "
              f"({d/len(n):.2f} s en moyenne)")
    sources = {(c["episode"], c["scene"]) for c in conduite}
    print(f"   {len(sources)} plans distincts sur 60")


if __name__ == "__main__":
    main()
