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

/** Une planche de carrousel LinkedIn. */
export type PlancheCarrousel = {{
  n: number;
  /** Ce que la planche fait dans la démonstration : la scène, le coût… */
  role: string;
  /** Le texte de la bande haute — celui qui doit être DANS l'image. */
  titre: string;
  /** Le texte du bandeau bas, quand il y en a un. */
  texte: string;
  prompt: string;
}};

/** Une étape du kit « refaites-le chez vous » — saison 6. */
export type EtapeKit = {{
  etape: number;
  titre: string;
  outil: string;
  /** « restaurant » : ça se passe chez le client. « rapidocms » : chez nous. */
  cote: "restaurant" | "rapidocms";
  /** Le végé-fruité qui explique cette étape. */
  guide: string;
  consigne: string;
  lien: string;
  /** Le prompt à copier. Les crochets sont à remplacer par le restaurateur. */
  prompt: string;
}};

/** Les trois formats image et vidéo qui ne sont pas le master. */
export type FormatsSociaux = {{
  /** Story Instagram : le clip, le hook, la punchline. Rien d'autre. */
  story?: {{ format: string; hook: string; punchline: string; url: string | null }} | null;
  /** Carrousel LinkedIn : quatre planches, converties en PDF sur le site. */
  carrousel?: {{ format: string; planches: PlancheCarrousel[] }} | null;
  /** Visuel Facebook : une image qui se comprend seule. */
  imageFacebook?: {{ format: string; prompt: string }} | null;
}};

export type ContenuEpisode = FormatsSociaux & {{
  publications: Record<Reseau, PublicationTexte>;
  promptVignette: string;
  higgsfieldPrompt: string | null;
  /** Saison 6 : ce que dit le végé-fruité à l'écran, en personnage HeyGen. */
  scriptHeygen?: string | null;
  /** Saison 6 : les quatre prompts à copier, dans l'ordre de la chaîne. */
  kit?: EtapeKit[] | null;
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
                    # Saison 6 seulement : le script de l'avatar et les quatre
                    # prompts à copier. Longs, et affichés sur la seule page de
                    # l'épisode — ils n'ont rien à faire dans le morceau commun.
                    "scriptHeygen": e.pop("scriptHeygen", None),
                    "kit": e.pop("kit", None),
                    # Les trois formats sociaux. Six cents planches de
                    # carrousel plus cent cinquante visuels Facebook : c'est
                    # long, ça ne s'affiche que sur la page de l'épisode, donc
                    # ça vit ici et pas dans le morceau commun.
                    "story": e.pop("story", None),
                    "carrousel": e.pop("carrousel", None),
                    "imageFacebook": e.pop("imageFacebook", None),
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

    # --- plan de site -------------------------------------------------------
    # 150 pages d'épisode qu'aucun lien de navigation n'expose toutes : sans
    # plan de site, les moteurs n'en trouvent qu'une poignée par exploration.
    base = "https://foodeatup-social.lovable.app"
    urls = [("/", "daily", "1.0"), ("/series", "weekly", "0.8"),
            ("/calendrier", "daily", "0.8"), ("/methode", "monthly", "0.9"),
            ("/rapidocms", "monthly", "0.9")]
    for r in d["reseaux"]:
        urls.append((f"/reseaux/{r['slug']}", "weekly", "0.6"))
    for s_ in d["series"]:
        urls.append((f"/series/{s_['slug']}", "weekly", "0.8"))
        for sa in s_["saisons"]:
            urls.append((f"/series/{s_['slug']}/saison/{sa['numero']}", "weekly", "0.7"))
            for e in sa["episodes"]:
                # Un épisode non produit n'a rien à montrer : l'indexer, c'est
                # promettre une page vide dans les résultats de recherche.
                if e["statut"] in ("publie", "monte"):
                    urls.append((f"/episode/{e['slug']}", "monthly", "0.7"))
    plan = ['<?xml version="1.0" encoding="UTF-8"?>',
            '<urlset xmlns="http://www.sitemaps.org/schemas/sitemap/0.9">']
    for loc, freq, prio in urls:
        plan += ["  <url>", f"    <loc>{base}{loc}</loc>",
                 f"    <changefreq>{freq}</changefreq>",
                 f"    <priority>{prio}</priority>", "  </url>"]
    plan.append("</urlset>")
    pub = os.path.join(SOCIAL, "public")
    os.makedirs(pub, exist_ok=True)
    open(os.path.join(pub, "sitemap.xml"), "w").write("\n".join(plan) + "\n")
    print(f"  sitemap.xml  {len(urls):6} URL")

    for f in ("series.ts", "contenu.ts"):
        print(f"  {f:12} {os.path.getsize(os.path.join(dst, f)) / 1024:6.0f} Ko")


if __name__ == "__main__":
    main()
