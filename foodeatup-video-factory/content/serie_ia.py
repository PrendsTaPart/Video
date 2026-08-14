#!/usr/bin/env python3
"""Série 3 — « L'IA dans FoodEatUp ». 31 épisodes, en trois saisons.

    saison 1  Ce qu'il faut avoir compris    7 épisodes   EP401 → EP407
    saison 2  Les huit boucles, une par une  10 épisodes  EP408 → EP417
    saison 3  Brancher, et faire tourner     14 épisodes  EP418 → EP431

Le défaut qu'on corrige ici
---------------------------
La liste d'origine ouvrait sur cinq épisodes génériques — c'est quoi l'IA,
c'est quoi un prompt, c'est quoi un LLM. Il en existe dix mille sur YouTube,
aucun ne vend FoodEatUp, et un restaurateur ne les regarde pas. Le problème
n'était pas leur qualité : c'était leur place. La série s'ouvrait sur son
matériau le plus faible et le plus concurrencé.

La règle appliquée : **aucun concept n'est expliqué à vide.** Chaque notion
arrive pendant qu'elle sert à quelque chose de précis dans le restaurant.
« C'est quoi un prompt » devient « j'écris une phrase, le saumon part avant
vendredi ». C'est déjà ce que fait la page produit — elle n'explique jamais une
boucle dans l'abstrait, elle la fait traverser par douze kilos de saumon.

Le fil rouge est donc le cas du saumon, repris du modèle. Il ouvre la série
(épisode 1), il structure la saison 2 (chaque boucle est vue à travers lui), et
il la referme (épisode 31, l'orchestration complète). Le spectateur voit huit
fois le même événement sous huit angles — c'est le même procédé que la série
« Une journée », appliqué au système au lieu des métiers.

La saison 2 n'est pas huit fois la même vidéo
----------------------------------------------
Huit épisodes de forme identique, c'est là qu'on décroche. Chaque boucle a donc
son angle propre — ce qu'elle produit, ce qui casse quand elle s'arrête — et
deux épisodes d'encadrement : celui qui pose les deux grandes boucles, celui
qui montre le croisement. Dix au total, pas huit.
"""
import sys
import pathlib

sys.path.insert(0, str(pathlib.Path(__file__).resolve().parent))
from modele_boucles import (BOUCLES, PAR_SLUG, AGENTS, GRANDES,  # noqa: E402
                            CROISEMENT, SAUMON, LOIS, MCP)

# ── Saison 1 — ce qu'il faut avoir compris ───────────────────────────────────
# Sept épisodes, et pas un de plus. Chacun est ancré sur un geste de
# restaurant : le concept passe pendant qu'il sert.

FONDATIONS = [
    dict(slug="qui-je-suis", titre="Qui je suis",
         concept=None,
         ancrage="Le chef présente celui qui va parler pendant trente "
                 "épisodes — et pourquoi ce n'est pas un cours d'informatique.",
         promesse="À la fin de la série, vous écrivez une phrase et votre "
                  "restaurant l'exécute."),
    dict(slug="douze-kilos", titre="Douze kilos de saumon",
         concept="Ce que l'IA change, en un cas",
         ancrage="Jeudi neuf heures, douze kilos de saumon, DLC vendredi "
                 "soir. On regarde ce qui se passe aujourd'hui, puis ce qui "
                 "se passe quand les boucles sont branchées.",
         promesse="Le cas revient à chaque épisode de la série. C'est le fil."),
    dict(slug="prompt", titre="Écrire une phrase qui agit",
         concept="Le prompt",
         ancrage="« Ajoute le poulet fermier à 12,80 le kilo chez Metro. » "
                 "L'ingrédient est créé, le prix enregistré, le fournisseur "
                 "lié. On n'a rien cliqué.",
         promesse="Un prompt n'est pas une question. C'est un ordre de "
                  "travail."),
    dict(slug="mcp", titre="La différence entre répondre et agir",
         concept="Le MCP",
         ancrage="Un chatbot lit une base de connaissances et ne change rien. "
                 "Un agent MCP appelle les outils métier, modifie les "
                 "données, et demande confirmation avant toute action "
                 "sensible.",
         promesse=f"{MCP['surface']} outils exposés au standard, une paire "
                  f"d'identifiants par établissement."),
    dict(slug="foodeatup", titre="Ce que FoodEatUp fait vraiment",
         concept="Le produit",
         ancrage="Pas une liste de modules : un restaurant modelé. Chaque "
                 "outil suit la forme d'une journée de service plutôt que la "
                 "forme d'une base de données.",
         promesse="C'est ce qui permet à une phrase de traverser huit "
                  "domaines sans qu'on l'ait programmée."),
    dict(slug="deux-boucles", titre="Les deux boucles infinies",
         concept="Le huit",
         ancrage="Le logo est un huit. C'est aussi le plan du restaurant : "
                 "la boucle gestion à gauche, la boucle vente à droite, et un "
                 "seul point où elles se touchent.",
         promesse="Ce point, c'est « pendant le service ». Le centre du "
                  "schéma et le centre de la journée sont le même endroit."),
    dict(slug="lois", titre="Pourquoi sept logiciels ne font pas un système",
         concept="Les trois lois",
         ancrage="Une boucle se referme. Une boucle en nourrit une autre. "
                 "Casser une sous-boucle casse les deux grandes.",
         promesse="Sept logiciels qui tiennent chacun un bout ne font pas "
                  "sept boucles connectées. Ils font sept tunnels."),
]

# ── Saison 2 — les huit boucles ──────────────────────────────────────────────
# Encadrement : un épisode d'ouverture sur les deux grandes, un de fermeture
# sur le croisement. Entre les deux, les huit, chacune vue à travers le saumon.

SAUMON_PAR_BOUCLE = {slug: texte for slug, texte in SAUMON}


def boucles_episodes():
    out = [dict(slug="grandes-boucles",
                titre="Gestion et vente, les deux moitiés",
                boucle=None,
                quoi="La gestion vous rend capable de servir. La vente fait "
                     "venir le monde. L'une ne se voit pas depuis la salle — "
                     "mais quand elle grippe, le saumon manque un vendredi "
                     "soir.",
                saumon=None)]
    for b in BOUCLES:
        out.append(dict(
            slug=f"boucle-{b['n']}", titre=f"{b['nom']} — {b['role'].lower()}",
            boucle=b["slug"],
            quoi=b["produit"],
            saumon=SAUMON_PAR_BOUCLE.get(b["slug"]),
        ))
    out.append(dict(
        slug="croisement", titre="Le croisement, pendant le service",
        boucle=None,
        quoi="Quatre échanges traversent le point de croisement. La commande "
             "et l'encaissement vont de la vente vers la gestion ; la carte "
             "et la marge font le chemin inverse. Votre logiciel de caisse "
             "connaît l'encaissement mais pas le besoin en cuisine.",
        saumon=None))
    return out


# ── Saison 3 — brancher, et faire tourner ────────────────────────────────────
# La partie qui a de la valeur réelle : on branche, et ça tourne. Chaque
# épisode se termine sur quelque chose qui existe et qu'on peut rejouer.

BRANCHEMENTS = [
    # « C'est quoi un LLM » et « brancher un LLM » étaient deux épisodes dans
    # la liste d'origine. Ils traitent le même geste : le second explique le
    # premier mieux que le premier ne s'explique seul. Fusionnés, la série
    # tombe juste à 31 sans qu'on retire un sujet.
    dict(slug="llm", titre="Le moteur : brancher Claude, ChatGPT ou Mistral",
         fait="Une paire d'identifiants, un endpoint, et le modèle de votre "
              "choix parle à votre établissement — et seulement au vôtre. On "
              "pose la même demande aux trois : les réponses diffèrent, les "
              "actions non."),
    dict(slug="quatre-agents", titre="Les quatre agents et leurs boucles",
         fait="Caroline décroche, Jarvis tient l'atelier, Iris fait circuler, "
              "PrédiBot voit les huit. Aucune case vide n'est un oubli."),
    dict(slug="caroline", titre="Caroline prend les appels",
         fait="Le client appelle pendant le coup de feu. Personne n'est "
              "disponible. Elle décroche à la première sonnerie et pense à "
              "demander l'allergie."),
    dict(slug="jarvis", titre="Jarvis, les mains dans la farine",
         fait="On ne tape pas avec les mains sales. On dit « relève la "
              "chambre froide à quatre degrés » et c'est tracé."),
    dict(slug="predibot", titre="PrédiBot répond sur les chiffres",
         fait="« Combien me coûte mon burger maintenant ? » Coût matière à "
              "jour, marge en euros, comparaison avec le mois dernier."),
    dict(slug="rapidocms", titre="RapidoCMS, et pourquoi il est à part",
         fait="FoodEatUp tient le restaurant. RapidoCMS tient ce qui en "
              "sort : les cinq réseaux, les créneaux, la bibliothèque."),
    dict(slug="brancher-rapidocms", titre="Brancher RapidoCMS à FoodEatUp",
         fait="Un stock bas devient un post. Le circuit complet, du bac de "
              "saumon au fil Instagram, sans qu'on ouvre un logiciel."),
    dict(slug="elevenlabs", titre="Donner une voix : ElevenLabs",
         fait="La même phrase, écrite puis dite. On garde une voix unique "
              "sur toute une série — c'est ce qui fait qu'on la reconnaît."),
    dict(slug="higgsfield", titre="Fabriquer l'image : Higgsfield",
         fait="Dix secondes de plat filmé comme une publicité, à partir "
              "d'une phrase et d'une photo."),
    dict(slug="heygen", titre="Mettre quelqu'un à l'écran : HeyGen",
         fait="Le personnage dit le texte. Trente mots, dix secondes — "
              "au-delà, le montage accélère la parole et ça s'entend."),
    dict(slug="meta", titre="Pousser plus loin : Meta",
         fait="Le même contenu, la même audience, mais payé. On regarde ce "
              "que ça change et ce que ça coûte."),
    dict(slug="plugins", titre="Plugins, skills, compétences",
         fait="Trois mots pour la même idée : apprendre un geste à l'agent "
              "une fois, et ne plus jamais le réexpliquer."),
    dict(slug="routine", titre="La routine et la boucle qui tourne seule",
         fait="Ce qui se déclenche sans qu'on le demande. Une DLC à deux "
              "jours, et le post part avant qu'on y pense."),
]

FINAL = dict(
    slug="orchestration", titre="L'orchestration finale du restaurant",
    fait="Une intention, huit boucles, zéro perte. Les douze kilos de saumon "
         "de l'épisode 2 repartent — et cette fois on voit passer les huit "
         "étapes, les quatre agents et les deux grandes boucles se refermer.")


def episodes():
    """Les 31 épisodes, numérotés à partir de EP401."""
    out, n = [], 401
    for f in FONDATIONS:
        out.append(dict(id=f"EP{n}", n=n, saison=1, slug=f["slug"],
                        titre=f["titre"], concept=f["concept"],
                        quoi=f["ancrage"], retenir=f["promesse"],
                        boucle=None, saumon=None))
        n += 1
    for b in boucles_episodes():
        out.append(dict(id=f"EP{n}", n=n, saison=2, slug=b["slug"],
                        titre=b["titre"], concept=None, quoi=b["quoi"],
                        retenir=(PAR_SLUG[b["boucle"]]["coupee"]
                                 if b["boucle"] else None),
                        boucle=b["boucle"], saumon=b["saumon"]))
        n += 1
    for b in BRANCHEMENTS + [FINAL]:
        out.append(dict(id=f"EP{n}", n=n, saison=3, slug=b["slug"],
                        titre=b["titre"], concept=None, quoi=b["fait"],
                        retenir=None, boucle=None, saumon=None))
        n += 1
    return out


if __name__ == "__main__":
    eps = episodes()
    for s in (1, 2, 3):
        d = [e for e in eps if e["saison"] == s]
        print(f"saison {s} : {len(d):2} épisodes  {d[0]['id']} → {d[-1]['id']}")
    print(f"total : {len(eps)}")
    print(f"\nboucles couvertes : "
          f"{len([e for e in eps if e['boucle']])}/8")
