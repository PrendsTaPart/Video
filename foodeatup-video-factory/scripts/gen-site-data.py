#!/usr/bin/env python3
"""Écrit les deux fichiers de données du site à partir de data/series.json.

    src/data/series.ts   l'identité : épisodes, statuts, dates, liens
    src/data/contenu.ts  le texte long : légendes, mots-dièse, prompts, fiches

Pourquoi deux fichiers plutôt qu'un.

Les 750 légendes, les 150 prompts de vignette, les 150 prompts Higgsfield et les
descriptions de fiches pèsent 1 Mo — les deux tiers des données. Ils ne servent
que sur trois écrans : la page épisode, la page méthode et le panneau du
calendrier. Dans un seul fichier, ils partaient dans le morceau de code commun,
donc chez tout visiteur de la page d'accueil : 193 Ko compressés avant le premier
pixel, sur un site pensé pour le mobile.

Séparés, et importés seulement par les composants qui les affichent, ils tombent
dans leur propre morceau. L'accueil est passé de 193 à 98 Ko compressés de
données.

Ne pas fusionner les deux fichiers « pour simplifier » : ce serait annuler la
mesure. Et attention aux imports — il suffit qu'un composant de l'accueil importe
une fonction depuis un module qui importe contenu.ts pour tout ramener avec elle.
C'est arrivé une fois, via un helper de trois lignes.
"""
import json, os

R = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
SOCIAL = os.path.join(os.path.dirname(R), "foodeatup-social")
j = lambda o: json.dumps(o, ensure_ascii=False, indent=2)

# Les champs qui déménagent dans contenu.ts.
TEXTE_PUB = ("legende", "hashtags", "motsCles", "cta", "titre")
TEXTE_TUTO = ("description", "etapes", "astuce")

ENTETE = """// FoodEatUp Social — {quoi}
//
// Fichier GÉNÉRÉ par l'usine à vidéos :
//   python3 scripts/gen-site-data.py
// Ne pas éditer à la main, la prochaine régénération écraserait la correction.
"""

CONTENU_TS = '''
import type {{ Reseau }} from "./series";

export type PublicationTexte = {{
  legende: string;
  hashtags: string[];
  motsCles: string[];
  cta: string;
  /** YouTube seulement. */
  titre?: string;
}};

export type ContenuEpisode = {{
  publications: Record<Reseau, PublicationTexte>;
  promptVignette: string;
  higgsfieldPrompt: string | null;
  tutoriel: {{ description: string | null; etapes: string[]; astuce: string | null }} | null;
}};

export const contenuParEpisode: Record<string, ContenuEpisode> = {contenu};

export const contenuDe = (id: string): ContenuEpisode | undefined => contenuParEpisode[id];

/** Le texte complet prêt à coller : légende + ligne de mots-dièse. */
export const texteAColler = (p: PublicationTexte) =>
  `${{p.legende}}\\n\\n${{p.hashtags.map((t) => "#" + t).join(" ")}}`;
'''


def main():
    d = json.load(open(os.path.join(SOCIAL, "data", "series.json")))
    contenu = {}
    for s in d["series"]:
        for sa in s["saisons"]:
            for e in sa["episodes"]:
                pubs = {}
                for r, p in e["reseaux"].items():
                    pubs[r] = {k: p[k] for k in TEXTE_PUB if k in p}
                    for k in TEXTE_PUB:
                        p.pop(k, None)
                t = e.get("tutoriel")
                contenu[e["id"]] = {
                    "publications": pubs,
                    "promptVignette": e.pop("promptVignette", ""),
                    "higgsfieldPrompt": e["higgsfield"].pop("prompt", None),
                    "tutoriel": {k: t.pop(k, None) for k in TEXTE_TUTO} if t else None,
                }

    dst = os.path.join(SOCIAL, "src", "data")
    os.makedirs(dst, exist_ok=True)
    open(os.path.join(dst, "contenu.ts"), "w").write(
        ENTETE.format(quoi="le texte long, sorti du bundle principal.")
        + CONTENU_TS.format(contenu=j(contenu))
    )

    # series.ts garde ses types (écrits à la main dans le gabarit ci-dessous) et
    # ne reçoit plus que l'identité des épisodes.
    gabarit = os.path.join(dst, "series.ts")
    ancien = open(gabarit).read()
    entete = ancien[: ancien.index("export const marque")]
    corps = (
        f"export const marque = {j(d['marque'])};\n\n"
        f"export const reseaux: ReseauInfo[] = {j(d['reseaux'])};\n\n"
        f"export const calendrier = {j(d['calendrier'])};\n\n"
        f"export const academy = {j(d['academy'])};\n\n"
        f"export const outils = {j(d['outils'])};\n\n"
        'export const chefReference = "/brand/chef-foodeatup.jpg";\n\n'
        f"export const series: Serie[] = {j(d['series'])};\n\n"
        "// Les sélecteurs vivent dans `@/lib/series`, pas ici : ce fichier est généré,\n"
        "// et tout ce qu'on y ajoute à la main disparaît à la régénération suivante.\n"
    )
    open(gabarit, "w").write(entete + corps)

    for f in ("series.ts", "contenu.ts"):
        print(f"  {f:12} {os.path.getsize(os.path.join(dst, f)) / 1024:6.0f} Ko")


if __name__ == "__main__":
    main()
