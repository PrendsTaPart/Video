#!/usr/bin/env python3
"""Écrit les prompts des deux formats image : carrousel LinkedIn, visuel Facebook.

    python3 scripts/gen-formats-sociaux.py

Enrichit `foodeatup-social/data/series.json` avec, par épisode :

    carrousel   quatre prompts, un par planche, plus le titre de chaque planche
    facebook    un prompt, une seule image

Ce ne sont PAS des vignettes
----------------------------
La vignette est une miniature : on la voit avant de cliquer, elle donne envie
d'ouvrir la vidéo, et son texte tient en trois mots. Ces deux formats-ci sont
la publication elle-même. Personne ne clique dessus pour voir autre chose :
ce qu'il y a à comprendre doit être DANS l'image, lisible en entier, sans son
et sans légende.

D'où deux règles qui ne se négocient pas :

1. **Le texte est dans l'image.** Pas en légende, pas en incrustation ajoutée
   après. Le générateur doit écrire ces mots-là, à cet endroit-là.
2. **Le chef y est.** C'est la même personne sur les cent cinquante épisodes —
   visage, toque, veste, tablier au logo FoodEatUp. Un générateur laissé libre
   redessine un autre cuisinier à chaque image et la série se dissout. La
   photo de référence est jointe à chaque appel, et le prompt le redit.

Le carrousel, en quatre planches
--------------------------------
La forme vient de ce que LinkedIn fait des PDF : on balaie de gauche à droite,
une idée par planche, et on s'arrête dès que ça devient un discours. Quatre
planches, dans cet ordre :

    1  LA SCÈNE     le hook, le chef dans la situation comique
    2  LE COÛT      ce que le problème coûte vraiment, en une phrase
    3  LA RÉPONSE   ce que fait le logiciel, montré et non promis
    4  LA SUITE     l'invitation, sobre

L'ordre n'est pas décoratif : c'est une démonstration. Inverser 2 et 3 donne
une publicité qui répond avant qu'on ait senti le problème.

Le visuel Facebook, en une image
--------------------------------
Facebook n'a pas de balayage. Tout tient dans une image : la scène, la phrase
qui accroche, et de quoi comprendre de quoi on parle. Le texte y est donc plus
court qu'une planche de carrousel — une phrase, pas deux.
"""
import json
import pathlib
import re
import sys

R = pathlib.Path(__file__).resolve().parent.parent
SERIES = R.parent / "foodeatup-social" / "data" / "series.json"

# Le chef, décrit une fois. Ce bloc part tel quel dans les cinq prompts d'un
# épisode : c'est ce qui empêche le générateur d'inventer un autre visage.
CHEF = (
    "PERSONNAGE — photo de référence jointe. Le chef FoodEatUp : MÊME visage, "
    "même barbe, même toque blanche, même veste de cuisine blanche, même "
    "tablier blanc au logo FoodEatUp bleu. Ne modifie ni ses traits, ni sa "
    "morphologie, ni son âge. C'est la même personne sur les cent cinquante "
    "épisodes — un autre visage casse la série."
)

CHARTE = (
    "CHARTE — crème #FCF9E6, marine #0F1A23, bleu #007BFF, orange #FFA500. "
    "Typographie arrondie très grasse, sans empattement. Aucun logo dessiné "
    "par le générateur, aucun filigrane, aucune bordure décorative, aucune "
    "interface de logiciel inventée à l'écran."
)

INTERDITS = (
    "INTERDITS — pas de texte autre que celui demandé, pas de faute "
    "d'orthographe, pas de lettres déformées, pas de sous-titres, pas de "
    "mention de marque tierce."
)


def phrase(t):
    """Une phrase propre : première lettre capitale, point final."""
    t = (t or "").strip().rstrip(".!?…")
    return t


def sans_url(t):
    """Le texte d'une image ne porte pas d'URL — illisible et jamais cliquable."""
    return re.sub(r"https?://\S+", "", t or "").strip()


def court(t, maxi=62):
    """Le texte d'un bandeau, ramené à ce qui tient dessus.

    Les résumés d'épisode font quatre-vingts à cent vingt signes — corrects
    dans une légende, illisibles en bandeau : le générateur les rend en corps
    minuscule ou les tronque lui-même au milieu d'un mot.

    On coupe donc à la frontière de proposition la plus tardive qui tienne. À
    défaut, au dernier mot entier — mais jamais sur un mot-outil : « elle part
    en cuisine dans la » se lit comme un bug, « elle part en cuisine » se lit
    comme une phrase.
    """
    OUTILS = {"la", "le", "les", "l", "un", "une", "des", "du", "de", "d",
              "dans", "en", "à", "au", "aux", "et", "ou", "sur", "sous",
              "pour", "par", "avec", "sans", "que", "qui", "se", "ce", "cet",
              "cette", "plus", "ne", "pas", "il", "elle", "depuis", "vers",
              "chez", "entre", "après", "avant", "comme", "chaque", "tout",
              "toute", "tous",
              # Les possessifs : la série tutoie le restaurateur, ses phrases
              # se terminent souvent sur « tes », « ton », « vos ».
              "mon", "ma", "mes", "ton", "ta", "tes", "son", "sa", "ses",
              "notre", "nos", "votre", "vos", "leur", "leurs"}

    t = " ".join((t or "").split())
    if len(t) <= maxi:
        return t

    bout = t[:maxi]
    for sep in (" : ", " — ", ", ", " et "):
        if sep in bout:
            tete = bout.rsplit(sep, 1)[0]
            if len(tete) >= 24:
                return tete.rstrip(" ,;:—")

    mots = bout.rsplit(" ", 1)[0].split()
    while mots and mots[-1].strip(".,;:'’").lower() in OUTILS:
        mots.pop()
    return " ".join(mots).rstrip(" ,;:—") or t[:maxi]


def planches(e):
    """Les quatre planches du carrousel : titre court, texte, décor."""
    trois = e.get("troisMots", "").strip()
    resume = phrase(e.get("resume", ""))
    # La première phrase du résumé porte la réponse ; la suite est du détail
    # qui ne tient pas sur une planche.
    reponse = resume.split(". ")[0] if resume else ""
    # Une seule phrase, pas le reste du résumé : `court()` coupe au mot et
    # produit sinon des bandeaux qui s'arrêtent au milieu d'une idée
    # (« Plus personne »), ce qui se lit comme un bug.
    suite = resume.split(". ")[1:]
    benefice = suite[0] if suite else ""

    return [
        {
            "n": 1,
            "role": "La scène",
            "titre": court(phrase(e["accroche"])),
            "texte": "",
            "decor": e.get("decorCarrousel")
                     or "le chef dans la situation de l'épisode, en plan "
                        "poitrine, décor de restaurant en service",
            "expression": "faussement dépité, la main sur le front, mais "
                          "l'œil qui rit",
        },
        {
            "n": 2,
            "role": "Le coût",
            "titre": court(phrase(e["punchline"]), 70),
            "texte": "",
            "decor": "le même décor, resserré sur le détail qui coince — "
                     "le ticket, l'écran, la file",
            "expression": "le chef en arrière-plan flou, l'objet net au "
                          "premier plan",
        },
        {
            "n": 3,
            "role": "La réponse",
            "titre": trois or "FOODEATUP",
            "texte": court(phrase(reponse)),
            "decor": "le chef calme, une tablette à la main, la salle en "
                     "ordre derrière lui",
            "expression": "posé, sûr de lui, sans sourire commercial",
        },
        {
            "n": 4,
            "role": "La suite",
            "titre": "ON VOUS MONTRE ?",
            "texte": court(phrase(benefice)) or "Une démo de dix minutes suffit.",
            "decor": "le chef de face, bras croisés, salle vide et lumineuse "
                     "derrière lui",
            "expression": "franc, direct, il regarde l'objectif",
        },
    ]


def prompt_planche(e, p):
    """Le prompt d'une planche. Format 4:5 — le portrait que LinkedIn affiche
    le plus grand dans le fil."""
    bande = (
        f"BANDE HAUTE — crème #FCF9E6 sur le cinquième supérieur du cadre, "
        f"portant UNIQUEMENT le texte « {p['titre']} » en marine #0F1A23, "
        f"typographie arrondie très grasse, centré, sur une ou deux lignes."
    )
    bas = ""
    if p["texte"]:
        bas = (
            f"\n\nBANDEAU BAS — marine #0F1A23 sur le quart inférieur, "
            f"portant UNIQUEMENT le texte « {p['texte']} » en crème #FCF9E6, "
            f"typographie arrondie grasse, centré, corps plus petit que la "
            f"bande haute."
        )
    return (
        f"Photo réaliste, cadrage vertical 4:5, 1080 × 1350 pixels. "
        f"Planche {p['n']} sur 4 — « {p['role']} ».\n\n"
        f"{CHEF}\n\n"
        f"SCÈNE — {p['decor']}. Expression : {p['expression']}.\n\n"
        f"{bande}{bas}\n\n"
        f"{CHARTE}\n\n{INTERDITS}"
    )


def prompt_facebook(e):
    """Le prompt du visuel Facebook. Une image, une phrase, format 4:5."""
    return (
        "Photo réaliste, cadrage vertical 4:5, 1080 × 1350 pixels. Publication "
        "Facebook — l'image EST la publication, elle se comprend seule, sans "
        "légende et sans son.\n\n"
        f"{CHEF}\n\n"
        f"SCÈNE — {e['titre'].lower()} : le chef dans la situation comique de "
        f"l'épisode, plan poitrine, décor de restaurant en service, lumière "
        f"chaude de fin de journée. Expression : faussement dépité, la main "
        f"sur le front, mais l'œil qui rit. Le chef occupe les deux tiers "
        f"droits du cadre ; l'élément comique est visible à gauche.\n\n"
        f"BANDE HAUTE — crème #FCF9E6 sur le cinquième supérieur, portant "
        f"UNIQUEMENT le texte « {court(phrase(e['accroche']))} » en marine #0F1A23, "
        f"typographie arrondie très grasse, centré.\n\n"
        f"BANDEAU BAS — marine #0F1A23 sur le sixième inférieur, portant "
        f"UNIQUEMENT le texte « {court(phrase(e['punchline']), 70)} » en crème #FCF9E6, "
        f"typographie arrondie grasse, centré, corps plus petit.\n\n"
        f"{CHARTE}\n\n{INTERDITS}"
    )


def main():
    d = json.load(open(SERIES, encoding="utf-8"))
    n = 0
    for s in d["series"]:
        for sa in s["saisons"]:
            # La saison 6 met les végé-fruités en vedette, pas le chef seul :
            # ses formats image se génèrent ailleurs, avec la brigade.
            if sa["numero"] >= 6:
                continue
            for e in sa["episodes"]:
                ps = planches(e)
                e["carrousel"] = {
                    "format": "4:5 · 1080 × 1350",
                    "planches": [
                        {"n": p["n"], "role": p["role"], "titre": p["titre"],
                         "texte": p["texte"],
                         "prompt": prompt_planche(e, p)}
                        for p in ps
                    ],
                }
                e["imageFacebook"] = {
                    "format": "4:5 · 1080 × 1350",
                    "prompt": prompt_facebook(e),
                }
                e["story"] = {
                    "format": "9:16 · 1080 × 1920 · 10 s",
                    "hook": phrase(e["accroche"]),
                    "punchline": phrase(e["punchline"]),
                    "url": None,
                }
                n += 1

    json.dump(d, open(SERIES, "w", encoding="utf-8"),
              ensure_ascii=False, indent=2)
    print(f"formats sociaux écrits : {n} épisodes")
    print(f"  carrousel  {n * 4} planches")
    print(f"  facebook   {n} visuels")
    print(f"  story      {n} fiches")
    return 0


if __name__ == "__main__":
    sys.exit(main())
