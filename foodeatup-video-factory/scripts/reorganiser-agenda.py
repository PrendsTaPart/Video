#!/usr/bin/env python3
"""Réordonne toute la grille de diffusion — quatre actes, dix-huit saisons.

    python3 scripts/reorganiser-agenda.py [AAAA-MM-JJ]

L'ancienne grille sortait les séries dans l'ordre où elles avaient été écrites :
deux cent quarante épisodes du Coup de Feu, puis les soixante-deux autres, puis
le film. Sept mois avant de voir autre chose que la première série, et le seul
contenu qui a un twist — UpEatFood — arrivait bon dernier, vingt-deux mois après
le début.

Aucun épisode n'étant encore publié, la grille est entièrement libre. Elle est
donc refaite comme une programmation de chaîne :

  ACTE I    Le film         UpEatFood ouvre tout — 350 secondes qui posent le
                            problème et la promesse. C'est la bande-annonce de
                            tout le reste.
  ACTE II   Le métier       Ce que le logiciel change, poste par poste. Le Coup
                            de Feu et Une journée s'alternent : une saison de
                            démonstration, une saison d'observation.
  ACTE III  Le système      Comment ça marche. L'IA dans FoodEatUp explique ce
                            que les deux actes précédents ont montré.
  ACTE IV   L'orchestration Le restaurant qui se gère tout seul. Les trois
                            dernières saisons du Coup de Feu, à la suite : c'est
                            le crescendo, il ne s'alterne pas.

À l'intérieur d'un acte, deux saisons de la même série ne se suivent jamais —
sauf dans l'acte IV, où c'est justement l'effet recherché.

Chaque saison est précédée de sa bande-annonce, qui occupe son propre jour. Une
saison qui commence sans prévenir se perd dans un fil ; annoncée la veille, elle
devient un rendez-vous.

Le script est rejouable : il repart toujours de la date de départ passée en
argument (par défaut, demain) et réécrit toutes les dates. Il refuse de toucher
un épisode déjà publié — le jour où il y en aura, ils feront butoir.
"""
import datetime
import json
import os
import pathlib
import sys

R = pathlib.Path(__file__).resolve().parent.parent
INVENTAIRE = R.parent / "foodeatup-social" / "data" / "series.json"

# L'ordre de diffusion : (série, saison), acte par acte.
ACTES = [
    (
        "Acte I — Le film",
        "Trois cent cinquante secondes qui posent le problème et la promesse. "
        "Tout ce qui suit en découle.",
        [("il-etait-une-fois-un-restaurant", n) for n in (1, 2, 3, 4, 5)],
    ),
    (
        "Acte II — Le métier",
        "Ce que le logiciel change, poste par poste. Une saison de démonstration, "
        "une saison d'observation, en alternance.",
        [
            ("le-coup-de-feu", 1),
            ("une-journee", 1),
            ("le-coup-de-feu", 2),
            ("le-coup-de-feu", 3),
            ("une-journee", 2),
            ("le-coup-de-feu", 4),
            ("le-coup-de-feu", 5),
        ],
    ),
    (
        "Acte III — Le système",
        "Comment ça marche. Ce que les deux actes précédents ont montré, on "
        "l'explique — et jamais à vide.",
        [("lia-dans-foodeatup", n) for n in (1, 2, 3)],
    ),
    (
        "Acte IV — L'orchestration",
        "Le restaurant qui se gère tout seul. Les trois dernières saisons se "
        "suivent : c'est le crescendo, il ne s'alterne pas.",
        [("le-coup-de-feu", n) for n in (6, 7, 8)],
    ),
]

# ── Les bandes-annonces ──────────────────────────────────────────────────────
# Une par saison, dix secondes, à la grammaire Seedance 2.5 du dépôt. Elle ne
# raconte rien : elle promet. Le montage y enchaîne les plans de la saison sans
# jamais en donner la chute, et la voix du conteur — la même que dans le film —
# fait le lien d'une saison à l'autre.
VOIX = (
    "Voix off française, un homme, grave et posée, le débit d'un conteur qui "
    "connaît déjà la fin, hors champ"
)


def prompt_bande_annonce(serie_nom, sa, acte, position, total, phrase, image):
    return (
        "Vertical 9:16, 10 secondes, 1080p, 24 im/s. PAS de texte incrusté, PAS "
        "de sous-titres, PAS de filigrane, PAS de logo, AUCUNE légende gravée "
        "dans l'image. Photoréaliste, image de cinéma : optique 35 mm, faible "
        "profondeur de champ, grain argentique, contraste tenu.\n\n"
        "@Image 1 ne définit que le visage du chef — barbe, toque blanche, veste "
        "blanche, tablier blanc FoodEatUp. Ne pas modifier ses traits ni sa "
        "carrure.\n\n"
        f"BANDE-ANNONCE — {serie_nom}, saison {sa['numero']} : « {sa['titre']} ». "
        f"{acte}. Saison {position} sur {total} de la programmation.\n"
        f"Décor : {image}\n\n"
        f"0-4s: Le décor seul, personne dedans, la lumière monte lentement. "
        f"Très lent travelling avant. {VOIX} : {{{phrase[0]}}} "
        "End state at 4s: le lieu est entièrement lisible et toujours vide.\n"
        "4-7s: À 4 secondes, le chef entre dans le cadre par la gauche et "
        "traverse sans s'arrêter, de dos. Un seul mouvement, rien d'autre ne "
        "bouge. End state at 7s: il est arrivé au centre du cadre et s'arrête, "
        "toujours de dos.\n"
        f"7-10s: Il se retourne et regarde l'objectif, une seconde, sans sourire. "
        f"La caméra s'immobilise. {VOIX} : {{{phrase[1]}}} "
        "End state at 10s: plan figé sur son visage, caméra immobile.\n\n"
        "Sound design: <ambiance réelle du lieu, dense> <un seul bruit de "
        "matière quand il entre dans le cadre>. Deux répliques, exactement aux "
        "minutages ci-dessus. Pas de musique — elle est ajoutée au montage."
    )


# Ce que la bande-annonce promet, saison par saison : la phrase d'ouverture du
# conteur, sa phrase de chute, et le décor à filmer.
PROMESSES = {
    ("il-etait-une-fois-un-restaurant", 1): (
        ("Il était une fois un restaurant.", "Et un homme qui ouvrait seul."),
        "une cuisine professionnelle en inox, éteinte, à l'aube",
    ),
    ("il-etait-une-fois-un-restaurant", 2): (
        ("La salle connaît tout le monde.", "Sauf qu'elle rentre chez elle à minuit."),
        "une salle de restaurant dressée, lumière basse, avant le service",
    ),
    ("il-etait-une-fois-un-restaurant", 3): (
        ("Au-dessus de la salle, quelqu'un compte.", "Et découvre tout un mois trop tard."),
        "un petit bureau à l'étage, classeurs et tickets de caisse, une lampe",
    ),
    ("il-etait-une-fois-un-restaurant", 4): (
        ("Il ne verra jamais votre logiciel.", "Il verra tout ce qu'il a oublié de faire."),
        "un salon le soir, une seule lampe, un téléphone posé sur la table",
    ),
    ("il-etait-une-fois-un-restaurant", 5): (
        ("Quatre histoires, un seul vendredi.", "Et un seul homme, depuis le début."),
        "le hall d'un restaurant en plein service, vu depuis la porte d'entrée",
    ),
    ("le-coup-de-feu", 1): (
        ("Un service, ça se passe bien.", "Jusqu'au moment où ça ne se passe plus."),
        "une salle de restaurant en plein coup de feu, vapeur et mouvement",
    ),
    ("le-coup-de-feu", 2): (
        ("Tout se compte, dans un restaurant.", "Encore faut-il compter juste."),
        "une réserve sèche, étagères pleines, lumière crue de néon",
    ),
    ("le-coup-de-feu", 3): (
        ("Une équipe, ça se construit avant le service.", "Pas pendant."),
        "un vestiaire de personnel, plannings punaisés au mur",
    ),
    ("le-coup-de-feu", 4): (
        ("Remplir la salle commence dehors.", "Bien avant l'ouverture."),
        "la devanture d'un restaurant à la tombée du jour, l'enseigne qui s'allume",
    ),
    ("le-coup-de-feu", 5): (
        ("Anticiper, c'est savoir avant.", "Le reste, c'est subir."),
        "une salle vide au petit matin, chaises encore sur les tables",
    ),
    ("le-coup-de-feu", 6): (
        ("Un restaurant n'a pas d'agence.", "Il a un service à assurer."),
        "un pass de cuisine, un plat dressé en très gros plan, vapeur et reflets",
    ),
    ("le-coup-de-feu", 7): (
        ("Trente accrocs ordinaires.", "Rejoués comme au cinéma."),
        "une salle de restaurant éclairée comme un plateau de tournage",
    ),
    ("le-coup-de-feu", 8): (
        ("Une journée entière, du réveil au coucher.", "Et une phrase à chaque fois."),
        "une cuisine à sept heures du matin, une seule source de lumière allumée",
    ),
    ("une-journee", 1): (
        ("Cinq postes, une seule cuisine.", "Le même vendredi, cinq fois."),
        "une cuisine professionnelle vue depuis le poste de travail, à hauteur d'homme",
    ),
    ("une-journee", 2): (
        ("La salle, le bureau, et celui qui paie.", "Le même vendredi, encore."),
        "une salle de restaurant et, au fond, la porte d'un bureau entrouverte",
    ),
    ("lia-dans-foodeatup", 1): (
        ("Avant de brancher quoi que ce soit.", "Sept épisodes pour comprendre."),
        "un objet réel du restaurant au premier plan, net ; le reste flou derrière",
    ),
    ("lia-dans-foodeatup", 2): (
        ("Huit boucles, et elles se tiennent.", "Casse-en une, casse-les toutes."),
        "un plan de travail vu de haut, huit objets du restaurant posés en cercle",
    ),
    ("lia-dans-foodeatup", 3): (
        ("Là, on branche pour de vrai.", "Et le restaurant tourne seul."),
        "un comptoir avec un écran éteint qui reflète la salle, bleu dans le décor",
    ),
}


def main(depart=None):
    d = json.load(open(INVENTAIRE, encoding="utf-8"))
    heures = {c["reseau"]: c["heure"] for c in d["calendrier"]["creneaux"]}
    par_slug = {s["slug"]: s for s in d["series"]}

    publies = [
        e["id"]
        for s in d["series"]
        for sa in s["saisons"]
        for e in sa["episodes"]
        if e["statut"] == "publie"
    ]
    if publies:
        raise SystemExit(
            f"{len(publies)} épisode(s) déjà publié(s) : la grille n'est plus libre. "
            "Réordonner ici décalerait des publications qui ont eu lieu."
        )

    jour = (
        datetime.date.fromisoformat(depart)
        if depart
        else datetime.date.fromisoformat(d["calendrier"]["depart"])
    )
    debut = jour

    # Toutes les saisons de la programmation, à plat, pour numéroter les
    # bandes-annonces « saison 7 sur 18 ».
    plat = [cle for _, _, saisons in ACTES for cle in saisons]
    total_saisons = len(plat)

    connues = {(s["slug"], sa["numero"]) for s in d["series"] for sa in s["saisons"]}
    if set(plat) != connues:
        manque = connues - set(plat)
        trop = set(plat) - connues
        raise SystemExit(f"programmation incomplète — absentes : {manque} · inconnues : {trop}")

    resume = []
    position = 0
    for acte, pitch_acte, saisons in ACTES:
        for slug, numero in saisons:
            position += 1
            s = par_slug[slug]
            sa = next(x for x in s["saisons"] if x["numero"] == numero)

            # La bande-annonce sort la veille du premier épisode et prend son
            # jour : une saison qui commence sans prévenir se perd dans un fil.
            phrases, image = PROMESSES[(slug, numero)]
            sa["acte"] = acte
            sa["ordre"] = position
            sa["bandeAnnonce"] = {
                "date": jour.isoformat(),
                "format": "9:16 · 1080 × 1920 · 10 s",
                "ouverture": phrases[0],
                "chute": phrases[1],
                "prompt": prompt_bande_annonce(
                    s["nom"], sa, acte, position, total_saisons, phrases, image
                ),
                "url": None,
            }
            jour += datetime.timedelta(days=1)

            premier = jour
            for e in sa["episodes"]:
                iso = jour.isoformat()
                e["datePrevue"] = iso
                for reseau, p in e["reseaux"].items():
                    p["date"] = iso
                    p["heure"] = heures.get(reseau, p.get("heure"))
                jour += datetime.timedelta(days=1)

            resume.append(
                (position, acte, s["nom"], sa["numero"], sa["titre"],
                 len(sa["episodes"]), sa["bandeAnnonce"]["date"],
                 premier.isoformat(), (jour - datetime.timedelta(days=1)).isoformat())
            )

        # Le pitch de l'acte est porté par sa première saison : c'est là que le
        # site l'affiche, en tête de bloc.
        premiere = saisons[0]
        next(
            x for x in par_slug[premiere[0]]["saisons"] if x["numero"] == premiere[1]
        )["pitchActe"] = pitch_acte

    d["calendrier"]["depart"] = debut.isoformat()
    d["calendrier"]["fin"] = (jour - datetime.timedelta(days=1)).isoformat()
    d["calendrier"]["note"] = (
        "Les horaires sont décalés pour qu'un même épisode ne tombe pas cinq "
        "fois au même moment sur cinq fils. La programmation suit quatre actes : "
        "le film d'abord, le métier ensuite, le système, puis l'orchestration. "
        "Chaque saison est annoncée la veille par sa bande-annonce, qui occupe "
        "son propre jour."
    )
    d["calendrier"]["actes"] = [
        {"titre": a, "pitch": p, "saisons": len(s)} for a, p, s in ACTES
    ]

    open(INVENTAIRE, "w", encoding="utf-8").write(json.dumps(d, ensure_ascii=False, indent=2))

    acte_courant = None
    for pos, acte, nom, num, titre, n, ba, p, f in resume:
        if acte != acte_courant:
            acte_courant = acte
            print(f"\n{acte}")
        print(f"  {pos:2}. {nom[:22]:22} S{num} · {titre[:30]:30} "
              f"{n:2} ép · BA {ba} · {p} → {f}")

    toutes = [
        e["datePrevue"]
        for s in d["series"] for sa in s["saisons"] for e in sa["episodes"]
        if e.get("datePrevue")
    ]
    bas = [sa["bandeAnnonce"]["date"] for s in d["series"] for sa in s["saisons"]]
    doublons = {x for x in toutes + bas if (toutes + bas).count(x) > 1}
    print(f"\n{len(toutes)} épisodes + {len(bas)} bandes-annonces = {len(toutes) + len(bas)} jours")
    print(f"du {debut.isoformat()} au {(jour - datetime.timedelta(days=1)).isoformat()} "
          f"— {len(doublons)} collision(s)")
    if doublons:
        raise SystemExit(f"dates en double : {sorted(doublons)[:5]}")


if __name__ == "__main__":
    main(sys.argv[1] if len(sys.argv) > 1 else None)
