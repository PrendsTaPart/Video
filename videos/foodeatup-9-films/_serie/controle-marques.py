#!/usr/bin/env python3
"""Contrôle juridique : aucun concurrent identifiable dans les films « sans ».

C'est la première des trois réserves de RELECTURE-JURIDIQUE-SANS.md. Elle est
restée ouverte longtemps pour une raison précise : un contrôle bâti sur une
liste de marques inventée par le développeur donne une **fausse assurance**. Il
passe au vert, on croit la question réglée, et la marque qui manquait est
justement celle qui est citée.

La liste vient donc d'ailleurs. Elle est dérivée du dépôt vitrine
`food-heartbeat-site-57e96f24`, où trois fichiers la tiennent à jour pour de
vraies raisons commerciales — ce qui garantit qu'elle est entretenue :

  - `src/data/competitors.ts` — 47 éditeurs avec leurs grilles tarifaires
    publiques, relevées en juillet 2026. C'est la base du comparateur du site.
  - `src/data/integrations-partners.ts` — les partenaires HubRise : caisses,
    plateformes de livraison, réservation, encaissement.
  - `src/data/comparatifs.ts` — les pages « alternative à … » publiées.

S'y ajoute la liste tenue à la main dans l'Académie
(`src/data/journees.ts`, `COMPETITOR_NAMES`), qui couvre des acteurs absents du
comparateur — paie, achats, e-réputation. L'union des deux, pas l'une ou
l'autre.

⚠️ Les partenaires sont volontairement inclus. Dans le registre « avec », citer
HubRise ou Uber Eats est légitime : ce sont des intégrations revendiquées. Dans
le registre « sans », qui met en scène l'empilement d'outils qu'on subit, la
moindre marque tierce rend une situation attribuable à un acteur nommé — et
c'est exactement ce que l'article L122-2 du Code de la consommation sanctionne
quand le ton est ironique.

Ce que le contrôle **ne prouve pas**, et qu'aucun programme ne prouvera :

  - qu'aucune interface montrée n'imite la charte d'un éditeur identifiable
    (réserve 2) ;
  - que les chiffres annoncés sont défendables (réserve 3).

Il attrape les fautes d'inattention, ce qui est déjà l'essentiel du risque. Le
reste relève de la relecture d'un avocat, qui reste due.

Usage :
    python3 _serie/controle-marques.py
    → code de sortie 0 si rien n'est trouvé, 1 sinon.
"""

from __future__ import annotations

import ast
import re
import sys
import unicodedata
from pathlib import Path

ICI = Path(__file__).resolve().parent

# Fichiers dont **tout texte** finit à l'écran ou dans la voix off.
SOURCES = ["films_sans.py", "serie_sans.py", "build-sans.py"]

# ---------------------------------------------------------------------------
# La liste
# ---------------------------------------------------------------------------

# Éditeurs et partenaires, dérivés du dépôt vitrine (voir docstring).
MARQUES_VITRINE = [
    "boutikio", "cashpad", "cegid", "clyo systems", "clyosystems", "collectly",
    "combo", "deliverect", "deliveroo", "easilys", "fidelatoo", "frigo magic",
    "frigomagic", "guest suite", "guestonline", "guestsuite", "heypongo",
    "innovorder", "inpulse", "just eat", "justeat", "koust", "l'addition",
    "laddition", "lightspeed", "loyverse", "lundi matin", "lundimatin", "malou",
    "marketman", "melba", "octopus haccp", "octopush", "octopushaccp",
    "opentable", "ordrafood", "partoo", "popina", "qtable", "resengo",
    "reviewtrackers", "revyo", "rovercash", "skello", "slang.ai", "slangai",
    "smile&pay", "smsfactor", "spot-hit", "stamp me", "stampme", "stripe",
    "stuart", "sumup", "sylen ai", "sylenai", "thefork", "tiller", "toporder",
    "uber eats", "ubereats", "yollty", "yumcall", "zelty", "zenchef", "zerosix",
    "zettle",
]

# Acteurs suivis par l'Académie et absents du comparateur : paie, achats,
# gestion de production, e-réputation.
MARQUES_ACADEMIE = [
    "adoria", "datameal", "factorial", "guestsuite", "hubrise", "komia",
    "libeo", "mapal", "octopus", "payfit", "pennylane", "ravy", "salamandre",
    "snapshift", "tactill",
]

MARQUES = sorted(set(MARQUES_VITRINE) | set(MARQUES_ACADEMIE))

# ---------------------------------------------------------------------------
# Détection
# ---------------------------------------------------------------------------


def aplatir(texte: str) -> str:
    """Minuscules, sans accents, sans balises, espaces normalisés.

    Les textes affichés contiennent du HTML (« <br /> », « <b> ») : sans le
    retirer, « Zel<b>ty</b> » passerait au travers. Les accents sont enlevés
    parce qu'une marque peut être écrite avec ou sans.
    """
    sans_balise = re.sub(r"<[^>]*>", " ", texte)
    decompose = unicodedata.normalize("NFD", sans_balise.lower())
    sans_accent = "".join(c for c in decompose if unicodedata.category(c) != "Mn")
    return re.sub(r"\s+", " ", sans_accent)


def frontieres(marque: str) -> re.Pattern[str]:
    """Motif à frontières de mot, pour éviter les collisions bêtes.

    « combo » est une marque de planning ; c'est aussi un mot français courant.
    Sans frontières, « octopus » attraperait « octopushaccp », et surtout
    « stripe » attraperait « stripes ». On compare donc des mots entiers, quitte
    à laisser passer une graphie collée — que les variantes de la liste
    couvrent déjà explicitement.
    """
    echappe = re.escape(aplatir(marque))
    return re.compile(rf"(?<![a-z0-9]){echappe}(?![a-z0-9])")


MOTIFS = [(m, frontieres(m)) for m in MARQUES]


def chaines_du_fichier(chemin: Path) -> list[tuple[int, str]]:
    """Toutes les chaînes littérales, avec leur ligne.

    On analyse l'arbre syntaxique plutôt que le texte brut : un nom de marque
    cité dans un commentaire — comme ceux de ce fichier — n'est pas diffusé et
    ne doit pas faire échouer le contrôle. Seul compte ce qui peut atteindre
    l'écran ou la voix.

    Les docstrings sont écartées pour la même raison.
    """
    arbre = ast.parse(chemin.read_text(encoding="utf-8"), filename=str(chemin))
    docstrings = set()
    for noeud in ast.walk(arbre):
        if isinstance(noeud, (ast.Module, ast.FunctionDef, ast.AsyncFunctionDef, ast.ClassDef)):
            corps = getattr(noeud, "body", [])
            if (
                corps
                and isinstance(corps[0], ast.Expr)
                and isinstance(corps[0].value, ast.Constant)
                and isinstance(corps[0].value.value, str)
            ):
                docstrings.add(id(corps[0].value))
    trouvees = []
    for noeud in ast.walk(arbre):
        if isinstance(noeud, ast.Constant) and isinstance(noeud.value, str):
            if id(noeud) in docstrings:
                continue
            trouvees.append((noeud.lineno, noeud.value))
    return trouvees


def controler() -> list[str]:
    fautes: list[str] = []
    for nom in SOURCES:
        chemin = ICI / nom
        if not chemin.exists():
            fautes.append(f"{nom} : fichier introuvable — le contrôle serait incomplet.")
            continue
        for ligne, texte in chaines_du_fichier(chemin):
            plat = aplatir(texte)
            for marque, motif in MOTIFS:
                if motif.search(plat):
                    extrait = texte if len(texte) <= 90 else texte[:87] + "…"
                    fautes.append(f"{nom}:{ligne} — « {marque} » dans : {extrait!r}")
    return fautes


def main() -> int:
    fautes = controler()
    print(f"Contrôle « aucun concurrent identifiable » — {len(MARQUES)} marques surveillées")
    print(f"Fichiers analysés : {', '.join(SOURCES)}")
    if not fautes:
        print("\n✓ Aucune marque tierce dans les textes diffusés.")
        print(
            "\n⚠️ Ce contrôle ne couvre que les noms. Restent dues :\n"
            "   · réserve 2 — qu'aucune maquette n'imite la charte d'un éditeur identifiable ;\n"
            "   · réserve 3 — que les chiffres annoncés soient défendables ;\n"
            "   · la relecture d'un avocat, qu'aucun programme ne remplace."
        )
        return 0
    print(f"\n✗ {len(fautes)} occurrence(s) :")
    for f in fautes:
        print(f"   {f}")
    print(
        "\nUtiliser une désignation générique : « un carnet », « un tableur »,\n"
        "« une autre application ». Jamais un produit, jamais une catégorie assez\n"
        "étroite pour ne désigner qu'un seul acteur."
    )
    return 1


if __name__ == "__main__":
    sys.exit(main())
