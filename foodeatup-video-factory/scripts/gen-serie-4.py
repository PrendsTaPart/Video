#!/usr/bin/env python3
"""Écrit la série 4 — « Il était une fois un restaurant » — dans l'inventaire.

    python3 scripts/gen-serie-4.py

Trente-cinq plans de dix secondes qui font un film de trois cent cinquante
secondes. Le texte des trente-cinq est dans `content/serie_film.py` ; ce script
en fabrique tout le reste : le prompt Seedance 2.5, la story avec son générique
de fin en motion design, le prompt de vignette, les cinq publications, et la
fiche de montage du film entier.

Ce que ce script NE fait PAS
-----------------------------
Il ne génère aucune image ni aucune vidéo. Les prompts sont des textes à donner
à l'humain, qui les exécute lui-même. C'est la règle du dépôt, et elle vaut
pour ces trente-cinq plans comme pour les trois cents autres.
"""
import json
import os
import pathlib
import re
import sys
import unicodedata

R = pathlib.Path(__file__).resolve().parent.parent
sys.path.insert(0, str(R / "content"))
INVENTAIRE = R.parent / "foodeatup-social" / "data" / "series.json"

from serie_film import HISTOIRES, PLANS, TEMPS  # noqa: E402

SLUG = "il-etait-une-fois-un-restaurant"

# La cinquième saison n'a pas d'histoire à elle : c'est celle où les quatre se
# croisent. Elle porte donc son propre en-tête.
FINALE = dict(
    slug="vendredi-20h15", saison=5, titre="Vendredi, 20 h 15", numero_depart=525,
    role="Les quatre", module="Service",
    tenue="les quatre tenues, selon le personnage à l'image",
    decor="le restaurant entier, de la cuisine au trottoir",
    perd="plus rien",
    pitch="Quatre histoires, un seul service. Onze plans où elles se croisent, "
          "et un dernier où l'on comprend que c'était le même homme.",
)

CHAPITRES_FINALE = [
    "Le même soir", "18 h 40", "18 h 41", "18 h 42", "18 h 43",
    "20 h 15", "20 h 31", "20 h 32", "23 h 50", "7 h 00", "La chute",
]


def slugifie(t):
    t = unicodedata.normalize("NFKD", t).encode("ascii", "ignore").decode()
    return re.sub(r"-+", "-", re.sub(r"[^a-z0-9]+", "-", t.lower())).strip("-")


# ─────────────────────────────────────────────────────────────────────────────
# Le prompt Seedance 2.5
#
# Même grammaire que les trois cents autres plans du dépôt : les références
# d'abord, la scène ensuite, puis un découpage en secondes entières où chaque
# tranche porte un seul changement et un état final explicite, et le son en
# dernier. Ce qui change ici, c'est qu'il y a DEUX voix par plan — le conteur,
# qui fait la couture du film, et le personnage, qui dit une seule phrase.
# ─────────────────────────────────────────────────────────────────────────────
EN_TETE = (
    "Vertical 9:16, 10 secondes, 1080p, 24 im/s. "
    "PAS de texte incrusté, PAS de sous-titres, PAS de filigrane, PAS de logo, "
    "AUCUNE légende gravée dans l'image."
)

STYLE = (
    "Photoréaliste, image de cinéma : optique 40 mm, faible profondeur de champ, "
    "grain argentique léger, contraste tenu. Un seul plan, aucune coupe."
)

LUMIERE = {
    "Avant FoodEatUp": (
        "Étalonnage froid et désaturé, verts tirés, hautes lumières écrêtées — "
        "l'avant du film. Les ombres mangent les bords du cadre."
    ),
    "La bascule": (
        "L'étalonnage change à l'intérieur du plan : froid au départ, il se "
        "réchauffe à partir de 5 s sans que rien d'autre ne bouge."
    ),
    "Avec FoodEatUp": (
        "Étalonnage chaud et tenu, blancs propres, noirs ouverts — l'après du "
        "film. La lumière vient d'une source unique et douce."
    ),
    "Le croisement": (
        "Étalonnage chaud, contrasté, lumière de service : c'est le dernier acte, "
        "il est filmé comme une fin de film."
    ),
}

VOIX_CONTEUR = (
    "Voix off française, un homme, grave et posée, le débit d'un conteur qui "
    "connaît déjà la fin, hors champ"
)


def prompt_seedance(h, arc, p):
    """Le plan, en forme Seedance 2.5."""
    return "\n\n".join([
        f"{EN_TETE} {STYLE}",
        (
            f"@Image 1 ne définit que le visage de l'acteur — barbe, traits, carrure. "
            f"Ne pas les modifier. Dans ce plan il joue {h['role'].lower()} : "
            f"{h['tenue']}. C'est le même acteur dans les quatre histoires du film, "
            f"et le film ne le dit jamais : ne rien ajouter qui le souligne."
        ),
        f"Décor : {h['decor']}. {LUMIERE[arc]}",
        "\n".join([
            (
                f"0-5s: {p['scene']} Caméra portée, très lent mouvement avant. "
                f"{VOIX_CONTEUR} : {{{p['accroche']}}} "
                f"End state at 5s: le personnage est seul et lisible dans le cadre, "
                f"rien n'a encore changé autour de lui."
            ),
            (
                f"5-8s: À 5 secondes exactement, {p['bascule']}. Un seul changement, "
                f"rien d'autre ne bouge. "
                f"End state at 8s: le changement est complet et pleinement lisible, "
                f"le personnage y a réagi."
            ),
            (
                f"8-10s: {p['fin']} La caméra s'immobilise. "
                f"Français, voix naturelle, dite pour soi et non pour la caméra, "
                f"{h['role'].lower()} : {{{p['dit']}}} "
                f"End state at 10s: plan figé sur son visage, caméra immobile, "
                f"aucune entrée dans le cadre."
            ),
        ]),
        (
            "Sound design: <ambiance réelle du lieu, dense> <un seul bruit de "
            "matière au moment du changement>. Deux répliques, exactement aux "
            "minutages ci-dessus : le conteur au début, le personnage à la fin. "
            "Pas de musique — elle est ajoutée au montage."
        ),
    ])


# ─────────────────────────────────────────────────────────────────────────────
# La story
#
# Dix secondes de film, puis un générique de fin en motion design : le logo qui
# se pose, « à suivre », et une voix off de plus qui dit la punchline FoodEatUp
# de l'épisode. C'est ce générique qui transforme trente-cinq stories isolées
# en une série qu'on attend — sans lui, chaque story se termine sur un plan de
# cinéma et personne ne sait qu'il y en a une autre demain.
# ─────────────────────────────────────────────────────────────────────────────
def story(ep, h, p, suivant):
    return {
        "format": "9:16 · 1080 × 1920 · 10 s",
        "hook": p["accroche"].rstrip("."),
        "punchline": p["punchline"].rstrip("."),
        "url": None,
        "motion": {
            "quand": "8,5 → 10,0 s, par-dessus la fin du plan",
            "consigne": (
                "Générique de fin en motion design, posé sur les 1,5 dernière(s) "
                "seconde(s) du plan, sans jamais couper l'image :\n"
                "— à 8,5 s, un voile marine #0F1A23 monte du bas sur le tiers "
                "inférieur, en 0,3 s, courbe d'accélération douce ;\n"
                "— à 8,8 s, le logo FoodEatUp arrive du bas, cale au centre du "
                "voile, avec un léger dépassement puis retour (overshoot 6 %) ;\n"
                "— à 9,1 s, la punchline s'écrit sous le logo, un mot après "
                "l'autre, 0,06 s par mot, en crème #FCF9E6 ;\n"
                "— à 9,6 s, la mention « à suivre » apparaît en orange #FFA500 "
                "à droite, avec une flèche qui avance de 8 px et s'arrête ;\n"
                "— rien ne disparaît avant la fin du plan."
            ),
            "punchline": p["story"],
            "aSuivre": (
                f"À suivre — {suivant}" if suivant else "Fin — le film entier en une fois"
            ),
            "voix": (
                "Voix off française, la même que le conteur mais une note plus "
                "haute et plus proche du micro, sur les 1,5 dernière(s) "
                f"seconde(s) : « {p['story']} »"
            ),
        },
    }


def prompt_vignette(h, p, numero):
    return (
        "Photo réaliste, cadrage vertical 9:16, image de cinéma : optique 40 mm, "
        "faible profondeur de champ, grain argentique léger.\n\n"
        f"L'acteur de l'image de référence — MÊME visage, même barbe, même "
        f"carrure. Il joue ici {h['role'].lower()} : {h['tenue']}. "
        f"Décor : {h['decor']}. Expression : {p['dit'].rstrip('.').lower()} — "
        "il ne sourit pas pour la caméra.\n\n"
        f"BANDE HAUTE — marine #0F1A23 sur le cinquième supérieur, portant "
        f"UNIQUEMENT « {h['titre'].upper()} » en crème #FCF9E6, typographie "
        "arrondie très grasse, centré.\n\n"
        f"BANDE BASSE — crème #FCF9E6 sur le sixième inférieur, portant "
        f"UNIQUEMENT « {numero:02d} / 35 » en marine #0F1A23, aligné à droite.\n\n"
        "Aucun logo dessiné, aucun filigrane, aucune interface de logiciel à "
        "l'écran, aucune autre inscription."
    )


# ─────────────────────────────────────────────────────────────────────────────
# Les cinq publications
# ─────────────────────────────────────────────────────────────────────────────
RESEAUX = [
    ("facebook", "FoodEatUp", "12:00", "Vidéo native 9:16", "https://site.foodeatup.com/"),
    ("instagram", "foodeatup.cocuisinage", "18:30", "Reel 9:16", None),
    ("tiktok", "foodeatup", "19:00", "Vidéo 9:16", None),
    ("linkedin", "FoodEatUp", "08:00", "Vidéo native 9:16", "https://site.foodeatup.com/"),
    ("youtube", "@FoodEatUp", "10:00", "Short 9:16", "https://site.foodeatup.com/"),
]

MOTS = ["restauration", "foodeatup", "restaurant", "courtmetrage"]


def publications(h, p, numero, total):
    out = {}
    for slug, compte, heure, format_, lien in RESEAUX:
        legende = (
            f"{p['accroche']}\n\n{p['resume']}\n\n{p['punchline']}\n\n"
            f"« Il était une fois un restaurant » — épisode {numero} sur {total}. "
            f"Les trente-cinq bout à bout font un film de cinq minutes cinquante.\n"
            "Tout FoodEatUp : https://site.foodeatup.com/\n"
            "Une démo ? 06 14 18 92 25 — foodeatup.com"
        )
        pub = {
            "statut": "a_venir",
            "date": None,
            "heure": heure,
            "compte": compte,
            "format": format_,
            "legende": legende,
            "hashtags": MOTS + [slugifie(h["titre"])],
            "motsCles": [h["module"].lower(), "restauration", "foodeatup", h["titre"].lower()],
            "cta": "Découvrir FoodEatUp",
            "lienCta": lien,
        }
        if slug == "youtube":
            pub["titre"] = f"{p['titre']} — Il était une fois un restaurant {numero}/{total}"
        out[slug] = pub
    return out


MONTAGE_FILM = {
    "consigne": (
        "Assembler les trente-cinq plans dans l'ordre des identifiants, sans "
        "transition entre deux plans d'une même histoire, et avec un fondu au "
        "noir de 12 images entre deux histoires. Le générique de fin des stories "
        "est RETIRÉ de la version film : il ne sert qu'aux réseaux. Musique "
        "unique sur les 350 s, montée de deux décibels à partir de l'épisode 25 "
        "et coupée net sur le dernier plan. Voix off du conteur normalisée à "
        "−16 LUFS, dialogues des personnages à −14, ambiances à −24. Sortie "
        "1080 × 1920, H.264, 350 s."
    ),
    "segments": [
        {"titre": "En cuisine", "debut": 0.0, "fin": 60.0,
         "contenu": "Six plans. Le chef, de sept heures du matin au bac vide du vendredi, puis la bascule."},
        {"titre": "En salle", "debut": 60.0, "fin": 120.0,
         "contenu": "Six plans. Le maître d'hôtel, sa mémoire, la table de douze qui n'existait pas."},
        {"titre": "Au bureau", "debut": 120.0, "fin": 180.0,
         "contenu": "Six plans. Le gérant, la pile de papier, le quinze du mois suivant."},
        {"titre": "À la maison", "debut": 180.0, "fin": 240.0,
         "contenu": "Six plans. Le client, qui ne verra jamais le logiciel."},
        {"titre": "Vendredi, 20 h 15", "debut": 240.0, "fin": 350.0,
         "contenu": "Onze plans. Les quatre histoires se croisent, minute par minute, jusqu'à la chute."},
    ],
    "livrable": (
        "Un film de 350 s en 9:16 pour la page de la série, et trente-cinq "
        "stories de 10 s — mêmes plans, générique de fin en plus — pour les "
        "quatre réseaux."
    ),
}


def main():
    d = json.load(open(INVENTAIRE, encoding="utf-8"))
    if any(s["slug"] == SLUG for s in d["series"]):
        d["series"] = [s for s in d["series"] if s["slug"] != SLUG]
        print("  série 4 déjà présente : réécrite")

    total = len(PLANS)
    saisons, ordre = [], []
    for h in HISTOIRES + [FINALE]:
        n = h["numero_depart"]
        episodes = []
        nb = 11 if h is FINALE else 6
        for k in range(nb):
            ep = f"EP{n + k}"
            p = PLANS[ep]
            if h is FINALE:
                chapitre, arc = CHAPITRES_FINALE[k], "Le croisement"
            else:
                chapitre, arc = TEMPS[k]
            numero = n + k - 500
            suivant = f"EP{n + k + 1}" if numero < total else None
            titre_suivant = PLANS[suivant]["titre"] if suivant else None
            episodes.append({
                "id": ep,
                "numero": n + k,
                "saison": h["saison"],
                "slug": f"{ep.lower()}-{slugifie(p['titre'])}",
                "titre": p["titre"],
                "module": h["module"],
                "chapitre": chapitre,
                "accroche": p["accroche"],
                "punchline": p["punchline"],
                "resume": p["resume"],
                "statut": "a_produire",
                "dureeSecondes": 10.0,
                "videoUrl": None,
                "posterUrl": None,
                "datePrevue": None,
                "troisMots": chapitre.upper()[:24],
                # Ce qui situe le plan dans le film — court, donc il reste dans
                # `series.ts` et sert à l'affichage de la page d'épisode.
                "lieu": h["titre"],
                "role": h["role"],
                "arc": arc,
                "planDuFilm": f"{numero} / {total}",
                "promptVignette": prompt_vignette(h, p, numero),
                "tutorielModuleUrl": None,
                "tutoriel": None,
                "masterRapidoUrl": None,
                # Le fil conducteur, en clair : les deux phrases dites dans le
                # plan et celle du générique de fin. C'est le script de voix off
                # de l'épisode, et mis bout à bout c'est celui du film.
                "voixOff": {
                    "conteur": p["accroche"],
                    "personnage": p["dit"],
                    "generique": p["story"],
                    "enchaine": (
                        f"Enchaîne sur « {titre_suivant} »" if titre_suivant
                        else "Dernier plan — le film se referme sur son premier"
                    ),
                },
                "higgsfield": {
                    "prompt": prompt_seedance(h, arc, p),
                    "duree": "10 s",
                    "format": "vertical 9:16",
                    "videoSourceUrl": None,
                    "source": None,
                },
                "story": story(ep, h, p, titre_suivant),
                "montage": MONTAGE_FILM,
                "reseaux": publications(h, p, numero, total),
            })
            ordre.append(ep)

        saisons.append({
            "numero": h["saison"],
            "titre": h["titre"],
            "pitch": h["pitch"],
            "episodes": episodes,
        })

    d["series"].append({
        "slug": SLUG,
        "nom": "Il était une fois un restaurant",
        "pitch": (
            "Un film publicitaire de trois cent cinquante secondes, découpé en "
            "trente-cinq plans de dix. Quatre histoires — la cuisine, la salle, "
            "le bureau, le client — avant FoodEatUp puis avec, et un dernier "
            "acte où elles se croisent le même vendredi soir. Le même acteur "
            "joue les quatre rôles ; le film ne le dit qu'à la fin."
        ),
        "format": "35 × 10 s · un film de 350 s · 9:16",
        "statut": "a-venir",
        # La date est posée par `dater-series-2-3.py`, qui place la série à la
        # suite des autres. On met le premier jour de la grille par défaut ;
        # le script la corrige si la grille bouge.
        "premiereDiffusion": "2027-05-08",
        "saisons": saisons,
    })

    open(INVENTAIRE, "w", encoding="utf-8").write(json.dumps(d, ensure_ascii=False, indent=2))
    print(f"série 4 écrite : {len(saisons)} saisons, {len(ordre)} épisodes, "
          f"{len(ordre) * 10} s de film")
    for sa in saisons:
        print(f"  S{sa['numero']} {sa['titre']:20} {len(sa['episodes']):2} plans")


if __name__ == "__main__":
    main()
