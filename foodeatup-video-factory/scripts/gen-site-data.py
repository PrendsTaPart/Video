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
import type {{ Reseau, ReseauCoeur }} from "./series";

export type PublicationTexte = {{
  legende: string;
  hashtags: string[];
  motsCles: string[];
  cta: string;
  /** YouTube seulement. */
  titre?: string;
}};

/**
 * Ce que Claude Code rend, une fois le plan et l'avatar en main.
 *
 * Les cinq segments ne varient jamais d'ordre ni de durée : c'est ce qui rend
 * la série reconnaissable en deux secondes. Ce qui varie, c'est leur contenu.
 */
export type Montage = {{
  /** La consigne à donner à Claude Code, telle quelle. */
  consigne: string;
  segments: {{ titre: string; debut: number; fin: number; contenu: string }}[];
  /** Ce qui sort : format, durée, niveau sonore, destination. */
  livrable: string;
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
  story?: {{
    format: string;
    hook: string;
    punchline: string;
    url: string | null;
    /** Série « Il était une fois un restaurant » : le générique de fin en
        motion design, qui n'existe que sur les stories — le film assemblé ne
        le porte pas. Sans lui, chaque story se termine sur un plan de cinéma
        et personne ne sait qu'il y en a une autre demain. */
    motion?: {{
      quand: string;
      consigne: string;
      punchline: string;
      aSuivre: string;
      voix: string;
    }} | null;
  }} | null;
  /** Short YouTube : la story, plus un carton de fin.

      YouTube est le seul réseau où la vidéo se cherche au lieu d'être croisée
      dans un fil. La story s'y arrête sur rien ; le carton pose le titre, la
      série et la chaîne. Même image, deux secondes et demie de plus. */
  shortYoutube?: {{ format: string; url: string | null }} | null;
  /** Vidéo YouTube paysage : le même montage, recadré en 16:9.

      Le Short vit dans l'onglet Shorts. La page de la chaîne, la recherche, la
      suggestion et la lecture sur téléviseur sont en paysage, et une vidéo
      verticale y arrive entre deux bandes noires qui prennent les deux tiers
      de l'écran. Le plan reste vertical — le recadrer couperait le sujet — et
      les côtés sont comblés par une copie floutée du plan, exactement comme
      les vignettes 16:9 déjà produites.

      Pas de vignette dans la donnée : `vignetteEpisode(id, "youtube")` sert
      déjà le 16:9 de l'épisode. */
  videoYoutube?: {{ format: string; url: string | null }} | null;
  /** Story Facebook : la story, plus un carton qui porte l'adresse.

      Même image et même format que le Short. Ce qui change est la fin : une
      vidéo native Facebook se repartage sans sa légende, et le lecteur ne
      propose aucun lien. Si l'adresse du site n'est pas dans l'image, elle
      n'est nulle part. */
  storyFacebook?: {{ format: string; url: string | null }} | null;
  /** Vidéo TikTok : la story, plus un carton au nom du compte.

      Sur TikTok le nom d'utilisateur est cliquable depuis le lecteur,
      comme la chaîne sur YouTube. Le carton n'a donc pas à porter
      l'adresse du site, contrairement à Facebook. */
  videoTiktok?: {{ format: string; url: string | null }} | null;
  /** Carrousel LinkedIn : quatre planches, converties en PDF sur le site. */
  carrousel?: {{ format: string; planches: PlancheCarrousel[] }} | null;
  /** Visuel Facebook : une image qui se comprend seule. */
  imageFacebook?: {{ format: string; prompt: string }} | null;
}};

/**
 * Le script de voix off d'un plan — série « Il était une fois un restaurant ».
 *
 * Trois phrases par plan : le conteur ouvre, le personnage ferme, le générique
 * de story ajoute la punchline FoodEatUp. Bout à bout, les trente-cinq font le
 * script du film entier — c'est ce qui permet de publier les plans un par un
 * sans que la continuité se démonte.
 */
export type VoixOff = {{
  conteur: string;
  personnage: string;
  generique: string;
  /** Ce que ce plan enchaîne, pour vérifier la couture. */
  enchaine: string;
}};

export type ContenuEpisode = FormatsSociaux & {{
  voixOff?: VoixOff | null;
  /* WhatsApp n'a pas de ligne ici : sa publication est dérivée de celle
     d'Instagram par `texteDe`. Typer ce dictionnaire sur `Reseau`, qui
     inclut WhatsApp, ferait exiger par TypeScript une clé que la donnée
     n'écrit pas — et c'est exactement ce qui a cassé la CI. */
  publications: Record<ReseauCoeur, PublicationTexte>;
  promptVignette: string;
  higgsfieldPrompt: string | null;
  /** Saison 6 : ce que dit le végé-fruité à l'écran, en personnage HeyGen. */
  scriptHeygen?: string | null;
  /** Séries 2 et 3 : le métier filmé, la phase, la boucle du modèle touchée. */
  metier?: string | null;
  phase?: string | null;
  amplitude?: string | null;
  boucle?: string | null;
  boucleSlug?: string | null;
  grandeBoucle?: string | null;
  /** L'incident partagé : deux épisodes qui le portent se répondent. */
  incident?: string | null;
  incidentHeure?: string | null;
  incidentQuoi?: string | null;
  /** Série 3 : l'étape du cas des douze kilos, quand l'épisode la traverse. */
  saumon?: string | null;
  /** Saison 6 : les quatre prompts à copier, dans l'ordre de la chaîne. */
  kit?: EtapeKit[] | null;
  /** Saisons 7 et 8 : le prompt HeyGen de l'avatar 3D du chef. */
  heygenPrompt?: string | null;
  /** Saisons 7 et 8 : le montage rendu par Claude Code. */
  montage?: Montage | null;
  tutoriel: {{ description: string | null; etapes: string[]; astuce: string | null }} | null;
}};

export const contenuParEpisode: Record<string, ContenuEpisode> = {contenu};

/**
 * Le texte d'une publication, WhatsApp compris.
 *
 * WhatsApp n'a pas de ligne dans la donnée : c'est un aperçu, pas une sixième
 * colonne. Sa publication reprend celle d'Instagram — même pièce 9:16, même
 * heure — moins le titre, qui ne sert qu'à YouTube, et sans mots-dièse : ils
 * n'y veulent rien dire.
 *
 * Cette fonction vit dans le gabarit et non dans le fichier généré : elle avait
 * été écrite à la main dans `contenu.ts`, et la régénération suivante l'a
 * effacée. Tout ce qu'on ajoute au fichier produit disparaît au prochain
 * passage — c'est ici qu'il faut l'écrire.
 */
export function texteDe(id: string, reseau: Reseau): PublicationTexte | undefined {{
  const c = contenuParEpisode[id];
  if (!c) return undefined;
  if (reseau !== "whatsapp") return c.publications[reseau];
  const base = c.publications.instagram;
  if (!base) return undefined;
  const {{ titre: _titre, ...reste }} = base;
  return {{ ...reste, hashtags: [] }};
}}

export const contenuDe = (id: string): ContenuEpisode | undefined => contenuParEpisode[id];

/** Le texte complet prêt à coller : légende + ligne de mots-dièse. */
export const texteAColler = (p: PublicationTexte) =>
  `${{p.legende}}\\n\\n${{p.hashtags.map((t) => "#" + t).join(" ")}}`;
'''


# Les séries que le site publie.
#
# Les trois, désormais. « Une journée » et « L'IA dans FoodEatUp » en étaient
# sorties le temps qu'elles trouvent leur place : aucun épisode monté, aucune
# date, et un nom de vignette — `saison-1-youtube.jpg` — qui désignait la saison
# 1 du Coup de Feu et rien d'autre. Les trois manques sont levés : elles ont
# leur créneau dans la grille (`dater-series-2-3.py`), et le site indexe
# maintenant présentations et vignettes par série ET par saison, si bien que
# trois « saison 1 » cohabitent sans se marcher dessus.
#
# Ce tuple reste : une série écrite mais pas encore montrable s'en retire d'une
# ligne, sans qu'on ait à défaire son travail.
SERIES_PUBLIEES = (
    "le-coup-de-feu",
    "une-journee",
    "lia-dans-foodeatup",
    "il-etait-une-fois-un-restaurant",
)


def main():
    d = json.load(open(os.path.join(SOCIAL, "data", "series.json")))
    inedites = [s["slug"] for s in d["series"] if s["slug"] not in SERIES_PUBLIEES]
    d["series"] = [s for s in d["series"] if s["slug"] in SERIES_PUBLIEES]
    if inedites:
        print(f"  non publiées : {', '.join(inedites)}")
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
                # `story.url` est la seule vérité. On la projette sur l'épisode
                # parce que le site lit `episode.storyUrl` — une projection,
                # pas une copie : il n'y a qu'un endroit à corriger.
                e["storyUrl"] = (e.get("story") or {}).get("url")
                e["shortUrl"] = (e.get("shortYoutube") or {}).get("url")
                e["videoYoutubeUrl"] = (e.get("videoYoutube") or {}).get("url")
                e["storyFacebookUrl"] = (e.get("storyFacebook") or {}).get("url")
                e["videoTiktokUrl"] = (e.get("videoTiktok") or {}).get("url")
                contenu[e["id"]] = {
                    "publications": pubs,
                    "promptVignette": e.pop("promptVignette", ""),
                    "higgsfieldPrompt": e["higgsfield"].pop("prompt", None),
                    # Saison 6 seulement : le script de l'avatar et les quatre
                    # prompts à copier. Longs, et affichés sur la seule page de
                    # l'épisode — ils n'ont rien à faire dans le morceau commun.
                    "scriptHeygen": e.pop("scriptHeygen", None),
                    "kit": e.pop("kit", None),
                    # Saisons 7 et 8 : le script de l'avatar du chef et le
                    # montage segment par segment. Mêmes raisons que ci-dessus —
                    # longs, et affichés sur la seule page de l'épisode.
                    "heygenPrompt": e.pop("heygenPrompt", None),
                    "montage": e.pop("montage", None),
                    # Les trois formats sociaux. Six cents planches de
                    # carrousel plus cent cinquante visuels Facebook : c'est
                    # long, ça ne s'affiche que sur la page de l'épisode, donc
                    # ça vit ici et pas dans le morceau commun.
                    # Séries « Une journée » et « L'IA dans FoodEatUp » : le
                    # métier, la boucle touchée, l'incident partagé. Ils ne
                    # servent qu'à la page de l'épisode.
                    "metier": e.pop("metier", None),
                    "phase": e.pop("phase", None),
                    "amplitude": e.pop("amplitude", None),
                    "boucle": e.pop("boucle", None),
                    "boucleSlug": e.pop("boucleSlug", None),
                    "grandeBoucle": e.pop("grandeBoucle", None),
                    "incident": e.pop("incident", None),
                    "incidentHeure": e.pop("incidentHeure", None),
                    "incidentQuoi": e.pop("incidentQuoi", None),
                    "saumon": e.pop("saumon", None),
                    # Série « Il était une fois un restaurant » : le script de
                    # voix off du plan — le conteur, le personnage, le générique
                    # de fin. Trois phrases par épisode, lues sur la seule page
                    # de l'épisode.
                    "voixOff": e.pop("voixOff", None),
                    "story": e.pop("story", None),
                    "shortYoutube": e.pop("shortYoutube", None),
                    "videoYoutube": e.pop("videoYoutube", None),
                    "storyFacebook": e.pop("storyFacebook", None),
                    "videoTiktok": e.pop("videoTiktok", None),
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
