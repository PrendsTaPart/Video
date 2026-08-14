#!/usr/bin/env python3
"""Écrit les deux nouvelles séries dans `foodeatup-social/data/series.json`.

    python3 scripts/gen-series-2-3.py

Produit, pour chacun des 62 épisodes : le wording, les cinq publications, le
plan Higgsfield, le script HeyGen, le prompt de vignette et la fiche de
montage.

Une voix par série, et elles ne se ressemblent pas
--------------------------------------------------
« Une journée » ne vend pas. Elle observe. Le logiciel n'y apparaît qu'en
creux — ce que le métier n'a pas, ce qu'il compense de tête, ce qu'il découvre
trop tard. Un chef de partie ne se reconnaît pas dans une démonstration ; il se
reconnaît dans un vendredi 19 h 40.

« L'IA dans FoodEatUp » explique. Elle a le droit de nommer les outils, les
endpoints, les nombres. Mais jamais à vide : chaque notion arrive pendant
qu'elle sert, et le cas des douze kilos de saumon traverse la série entière.

Ce que ce script NE fait PAS
-----------------------------
Il ne génère aucune image ni aucune vidéo. Les plans Higgsfield et les scripts
HeyGen sont des textes à donner à l'humain, qui les exécute lui-même. C'est la
règle du dépôt et elle vaut pour ces 62 épisodes comme pour les 240 autres.
"""
import json
import os
import pathlib
import re
import sys
import unicodedata

R = pathlib.Path(__file__).resolve().parent.parent
sys.path.insert(0, str(R / "content"))

from modele_boucles import (BOUCLES, PAR_SLUG, AGENTS, GRANDES,  # noqa: E402
                            CROISEMENT, MCP)
import serie_journee as SJ  # noqa: E402
import serie_ia as SIA  # noqa: E402

SOCIAL = R.parent / "foodeatup-social"
SERIES = SOCIAL / "data" / "series.json"

SITE = "https://site.foodeatup.com/"
CONTACT = "Une démo ? 06 14 18 92 25 — foodeatup.com"

RESEAUX = {
    "facebook":  {"heure": "12:00", "format": "Vidéo native 9:16"},
    "instagram": {"heure": "18:30", "format": "Reel 9:16"},
    "tiktok":    {"heure": "19:00", "format": "Vidéo native 9:16"},
    "linkedin":  {"heure": "08:00", "format": "Vidéo native 9:16"},
    "youtube":   {"heure": "10:00", "format": "Short 9:16"},
}


def slugifie(t):
    t = unicodedata.normalize("NFKD", t).encode("ascii", "ignore").decode()
    return re.sub(r"[^a-z0-9]+", "-", t.lower()).strip("-")


# ══ Série 2 — Une journée ════════════════════════════════════════════════════

def journee_higgsfield(e):
    """Le plan d'ouverture : le métier, à son heure, sans logiciel visible.

    Aucune interface à l'écran. La série montre le geste, pas l'outil — et un
    écran allumé dans le plan ferait basculer l'épisode du côté de la
    démonstration, qui est exactement ce qu'on évite ici.
    """
    heure = {"avant": "07h00", "pendant": "20h15", "apres": "23h30"}[e["phase"]]
    lumiere = {
        "avant": "lumière froide d'avant l'aube, une seule source allumée",
        "pendant": "lumière chaude et saturée, vapeur, mouvement constant",
        "apres": "lumière crue de fin de service, néons, surfaces vides",
    }[e["phase"]]
    decor = {
        "cuisine": "une cuisine professionnelle en inox",
        "salle": "une salle de restaurant",
        "bureau": "un petit bureau à l'étage, au-dessus de la salle",
    }[e["socle"]]

    return (
        f"Vertical 9:16, 10 secondes, 4K, photoréaliste, caméra à l'épaule, "
        f"profondeur de champ courte. PAS de texte incrusté, PAS de "
        f"sous-titres, PAS de filigrane, PAS de logo.\n\n"
        f"PERSONNAGE — {e['metierNom'].lower()}, tenue de son poste, visage "
        f"lisible. Une seule personne au premier plan.\n\n"
        f"HEURE — {heure}. {lumiere[0].upper() + lumiere[1:]}.\n\n"
        f"DÉCOR — {decor}, vu depuis le poste de travail du personnage. "
        f"AUCUN écran allumé, AUCUNE tablette, AUCUNE interface visible : "
        f"cette série montre le geste, pas l'outil.\n\n"
        f"ACTION — {e['quoi']}\n"
        f"À 5 secondes, quelque chose se tend : un regard vers la porte, un "
        f"geste suspendu, un objet qu'on repose.\n"
        f"Deux dernières secondes : le personnage immobile, il regarde son "
        f"poste, pas l'objectif.\n\n"
        f"AUDIO — ambiance réelle du lieu, aucun dialogue, pas de musique."
    )


def journee_heygen(e):
    """Le métier parle à la première personne — 15 à 26 mots.

    Écrit à la main, épisode par épisode, dans `content/serie_journee.py`.
    Une conversion automatique de la troisième vers la première personne
    donnait des phrases fausses (« Il est le seul » → « Je suis le seul ici »
    demande de savoir où est « ici »), et c'est la voix de la série : elle
    mérite d'être écrite.
    """
    return e["dit"]


def journee_legende(e, reseau):
    inc = SJ.INCIDENTS.get(e["incident"]) if e["incident"] else None
    b = PAR_SLUG[e["boucle"]]

    corps = f"{e['phaseLabel']}. {e['quoi']}"
    if inc:
        autres = [x for x in inc["vu_par"] if x != e["metier"]]
        corps += (f"\n\n{inc['heure']} — {inc['quoi']} "
                  f"{len(autres)} autres épisodes montrent le même moment, "
                  f"depuis un autre poste.")

    if reseau == "linkedin":
        corps += (f"\n\nCe que ça touche : {b['nom'].lower()}. "
                  f"{b['coupee']}"
                  f"\n\nEn savoir plus : {SITE}\n{CONTACT}")
    elif reseau == "youtube":
        corps += f"\n\n{SITE}\n{CONTACT}"
    else:
        corps += f"\n\n{SITE}"
    return corps


def journee_vignette(e):
    return (
        f"Photo réaliste, cadrage vertical 9:16. {e['metierNom']}, à son "
        f"poste, tenue de travail, visage net et lisible, expression "
        f"concentrée — ni sourire commercial, ni pose. Décor de "
        f"{'cuisine professionnelle' if e['socle'] == 'cuisine' else 'salle de restaurant' if e['socle'] == 'salle' else 'petit bureau'} "
        f"en arrière-plan flou. Le personnage occupe les deux tiers du cadre.\n\n"
        f"BANDE HAUTE — marine #0F1A23 sur le cinquième supérieur, portant "
        f"UNIQUEMENT « {e['phaseLabel'].upper()} » en crème #FCF9E6, "
        f"typographie arrondie très grasse, centré.\n\n"
        f"Aucun logo dessiné, aucun filigrane, aucune interface de logiciel "
        f"à l'écran, aucune autre inscription."
    )


# ══ Série 3 — L'IA dans FoodEatUp ════════════════════════════════════════════

def ia_higgsfield(e):
    """Le plan d'ouverture : le geste concret, jamais le concept.

    Une série sur l'IA filme d'habitude des écrans et des schémas. Ici on
    filme ce que la phrase déclenche dans le restaurant — le bac de saumon, le
    téléphone qui sonne, la chambre froide. L'abstraction est dans le
    commentaire, pas dans l'image.
    """
    return (
        f"Vertical 9:16, 10 secondes, 4K, photoréaliste, caméra fixe ou très "
        f"lent travelling. PAS de texte incrusté, PAS de sous-titres, PAS de "
        f"filigrane, PAS de logo.\n\n"
        f"IDENTITÉ VISUELLE — RapidoCMS. Bleu #03A9F5 présent dans le décor "
        f"— un écran éteint qui reflète, une lumière, un objet — sans jamais "
        f"former de logo. Tons clairs, gris #383838.\n\n"
        f"SCÈNE — {e['quoi']}\n\n"
        f"CADRE — un objet réel du restaurant au premier plan, net ; le chef "
        f"en retrait, flou, qui regarde. On filme ce que la phrase déclenche, "
        f"jamais le schéma qui l'explique.\n"
        f"À 5 secondes, l'objet change d'état — il s'allume, il bouge, il "
        f"s'ouvre.\n"
        f"Deux dernières secondes : le plan s'immobilise sur l'objet.\n\n"
        f"AUDIO — ambiance réelle, un seul son d'interface discret à "
        f"5 secondes, aucun dialogue, pas de musique."
    )


def ia_heygen(e):
    """Le chef explique. Jamais un concept sans le geste qui va avec."""
    t = e["quoi"].split(".")[0].strip()
    if e.get("retenir"):
        return f"{t}. {e['retenir']}"
    return f"{t}."


def ia_legende(e, reseau):
    corps = e["quoi"]
    if e.get("saumon"):
        corps += f"\n\nSur le cas des douze kilos : {e['saumon']}"
    if e.get("retenir"):
        corps += f"\n\n{e['retenir']}"
    if reseau == "linkedin":
        corps += f"\n\nLe système complet : {SITE}le-systeme\n{CONTACT}"
    elif reseau == "youtube":
        corps += f"\n\n{SITE}le-systeme\n{CONTACT}"
    else:
        corps += f"\n\n{SITE}le-systeme"
    return corps


def ia_vignette(e):
    b = PAR_SLUG[e["boucle"]] if e.get("boucle") else None
    sujet = (f"le chef devant {b['quoi'].lower()}" if b
             else "le chef, plan poitrine, dans son restaurant")
    return (
        f"Photo réaliste, cadrage vertical 9:16. Le chef de l'image de "
        f"référence — MÊME visage, même barbe, même toque blanche, même "
        f"veste, même tablier au logo FoodEatUp. Ne change ni ses traits ni "
        f"sa morphologie. Expression : posé, sûr de lui, sans sourire "
        f"commercial. Scène : {sujet}. Décor de restaurant, tons clairs, une "
        f"touche de bleu #03A9F5 dans la lumière.\n\n"
        f"BANDE HAUTE — blanc sur le cinquième supérieur, portant UNIQUEMENT "
        f"« {(b['nom'] if b else e['titre']).upper()[:24]} » en gris #383838, "
        f"typographie arrondie très grasse, centré.\n\n"
        f"Aucun logo dessiné, aucun filigrane, aucun schéma, aucune interface "
        f"inventée."
    )


# ══ Assemblage ═══════════════════════════════════════════════════════════════

def publications(e, legende, titre_yt, mots):
    out = {}
    for r, cfg in RESEAUX.items():
        out[r] = {
            "statut": "a_venir", "date": None, "heure": cfg["heure"],
            "compte": {"facebook": "FoodEatUp", "instagram":
                       "foodeatup.cocuisinage", "tiktok": "foodeatup",
                       "linkedin": "FoodEatUp", "youtube": "@FoodEatUp"}[r],
            "format": cfg["format"],
            "legende": legende(e, r),
            "hashtags": mots,
            "motsCles": mots,
            "cta": "Découvrir FoodEatUp",
            "lienCta": SITE,
        }
        if r == "youtube":
            out[r]["titre"] = titre_yt(e)
    return out


def serie_journee():
    eps_src = SJ.episodes()
    saisons = {}
    for e in eps_src:
        b = PAR_SLUG[e["boucle"]]
        inc = SJ.INCIDENTS.get(e["incident"]) if e["incident"] else None
        mots = ["restauration", "foodeatup", slugifie(e["metier"]),
                {"avant": "miseenplace", "pendant": "coupdefeu",
                 "apres": "fermeture"}[e["phase"]]]
        ep = {
            "id": e["id"], "numero": e["n"], "saison": e["saison"],
            "slug": f"{e['id'].lower()}-{slugifie(e['metier'])}-{e['phase']}",
            "titre": e["titre"],
            "module": e["metierNom"],
            "chapitre": e["phaseLabel"],
            "accroche": e["accrocheMetier"],
            "punchline": e["tension"],
            "resume": e["quoi"],
            "statut": "a_produire",
            "dureeSecondes": 20.0 if e["densite"] == "courte" else 37.5,
            "videoUrl": None, "posterUrl": None,
            "datePrevue": None,
            "troisMots": e["phaseLabel"].upper(),
            "promptVignette": journee_vignette(e),
            "tutorielModuleUrl": None, "tutoriel": None,
            "masterRapidoUrl": None,
            "higgsfield": {
                "prompt": journee_higgsfield(e), "duree": "10 s",
                "format": "vertical 9:16", "videoSourceUrl": None,
                "source": None,
            },
            "scriptHeygen": journee_heygen(e),
            # Les champs propres à la série : le métier, la phase, la boucle
            # touchée, et l'incident partagé qui relie les épisodes entre eux.
            "metier": e["metierNom"], "phase": e["phaseLabel"],
            "amplitude": e["amplitude"],
            "boucle": b["nom"], "boucleSlug": b["slug"],
            # « Pendant le service » n'appartient à aucune des deux grandes
            # boucles : c'est le point où elles se touchent. L'écrire plutôt
            # que de ranger l'épisode d'un côté serait faux au modèle.
            "grandeBoucle": ("Le croisement des deux boucles"
                             if e["phase"] == "pendant"
                             else GRANDES[b["grande"]]["nom"]),
            "incident": inc["nom"] if inc else None,
            "incidentHeure": inc["heure"] if inc else None,
            "incidentQuoi": inc["quoi"] if inc else None,
            "reseaux": publications(
                e, journee_legende,
                lambda x: f"{x['metierNom']} — {x['phaseLabel'].lower()}",
                mots),
        }
        saisons.setdefault(e["saison"], []).append(ep)

    return {
        "slug": "une-journee", "nom": "Une journée",
        "pitch": "Dix métiers, un seul service, trois moments. Le même "
                 "vendredi soir vu depuis dix postes — et quatre incidents "
                 "qui traversent plusieurs épisodes.",
        "format": "Vertical 1080×1920 · 20 à 37,5 s · 31 épisodes",
        "statut": "a-venir", "premiereDiffusion": "2027-01-05",
        "saisons": [
            {"numero": 1, "titre": "En cuisine",
             "pitch": "Du chef au plongeur. La boucle gestion, vue par ceux "
                      "qui la tiennent.",
             "episodes": saisons[1]},
            {"numero": 2, "titre": "En salle, au bureau, avec le client",
             "pitch": "La boucle vente, plus le poste que personne n'occupe "
                      "et le mois qui referme tout.",
             "episodes": saisons[2]},
        ],
    }


def serie_ia():
    eps_src = SIA.episodes()
    saisons = {}
    for e in eps_src:
        b = PAR_SLUG[e["boucle"]] if e.get("boucle") else None
        mots = ["restauration", "foodeatup", "ia", "rapidocms"]
        ep = {
            "id": e["id"], "numero": e["n"], "saison": e["saison"],
            "slug": f"{e['id'].lower()}-{slugifie(e['titre'])}"[:60],
            "titre": e["titre"],
            "module": b["nom"] if b else (e.get("concept") or "Le système"),
            "chapitre": {1: "Ce qu'il faut avoir compris",
                         2: "Les huit boucles",
                         3: "Brancher, et faire tourner"}[e["saison"]],
            "accroche": (e.get("concept") or e["titre"]),
            "punchline": e.get("retenir") or e["quoi"].split(".")[0] + ".",
            "resume": e["quoi"],
            "statut": "a_produire", "dureeSecondes": 37.5,
            "videoUrl": None, "posterUrl": None, "datePrevue": None,
            "troisMots": (b["nom"] if b else e["titre"]).upper()[:24],
            "promptVignette": ia_vignette(e),
            "tutorielModuleUrl": None, "tutoriel": None,
            "masterRapidoUrl": None,
            "higgsfield": {
                "prompt": ia_higgsfield(e), "duree": "10 s",
                "format": "vertical 9:16", "videoSourceUrl": None,
                "source": None,
            },
            "scriptHeygen": ia_heygen(e),
            "boucle": b["nom"] if b else None,
            "boucleSlug": b["slug"] if b else None,
            "grandeBoucle": GRANDES[b["grande"]]["nom"] if b else None,
            "saumon": e.get("saumon"),
            "reseaux": publications(
                e, ia_legende, lambda x: x["titre"], mots),
        }
        saisons.setdefault(e["saison"], []).append(ep)

    return {
        "slug": "lia-dans-foodeatup", "nom": "L'IA dans FoodEatUp",
        "pitch": "Du premier prompt à l'orchestration complète. Aucun concept "
                 "expliqué à vide : douze kilos de saumon traversent les "
                 "trente et un épisodes.",
        "format": "Vertical 1080×1920 · 37,5 s · 31 épisodes",
        "statut": "a-venir", "premiereDiffusion": "2027-03-01",
        "saisons": [
            {"numero": 1, "titre": "Ce qu'il faut avoir compris",
             "pitch": "Sept notions, chacune ancrée sur un geste du "
                      "restaurant.",
             "episodes": saisons[1]},
            {"numero": 2, "titre": "Les huit boucles, une par une",
             "pitch": "Les deux grandes, les huit sous-boucles, et le point "
                      "où elles se croisent.",
             "episodes": saisons[2]},
            {"numero": 3, "titre": "Brancher, et faire tourner",
             "pitch": "Les outils, les agents, les routines. Chaque épisode "
                      "finit sur quelque chose qui existe.",
             "episodes": saisons[3]},
        ],
    }


def main():
    d = json.load(open(SERIES, encoding="utf-8"))
    nouvelles = {s["slug"]: s for s in (serie_journee(), serie_ia())}

    # Remplacer si elles existent déjà, sinon ajouter — le script doit pouvoir
    # tourner deux fois sans dupliquer les séries.
    d["series"] = [s for s in d["series"] if s["slug"] not in nouvelles]
    d["series"] += list(nouvelles.values())

    json.dump(d, open(SERIES, "w", encoding="utf-8"),
              ensure_ascii=False, indent=2)

    for s in d["series"]:
        n = sum(len(sa["episodes"]) for sa in s["saisons"])
        print(f"  {s['nom']:24} {len(s['saisons'])} saisons  {n:3} épisodes")
    total = sum(len(sa["episodes"]) for s in d["series"] for sa in s["saisons"])
    print(f"  {'TOTAL':24} {len(d['series'])} séries    {total:3} épisodes")
    return 0


if __name__ == "__main__":
    sys.exit(main())
