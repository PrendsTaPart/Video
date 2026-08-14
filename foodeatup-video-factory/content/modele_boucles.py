#!/usr/bin/env python3
"""Le modèle des huit boucles — source unique pour toutes les séries.

Ce fichier n'invente rien. Il transcrit le modèle publié sur
https://site.foodeatup.com/le-systeme et repris dans le dépôt
`foodeatup-guide-star` (`src/data/boucles-home.ts`, `journees.ts`,
`metiers.ts`). Il vit ici pour que l'usine à vidéos cesse de le paraphraser de
mémoire : deux séries entières s'appuient dessus, et une paraphrase qui dérive
d'une série à l'autre casse la cohérence de l'ensemble.

Ce que dit le modèle
--------------------
Le logo FoodEatUp est un huit. C'est aussi le plan du restaurant : **deux
boucles infinies** qui se croisent en un seul point.

    boucle GESTION  ─┐                    ┌─  boucle VENTE
    ce qui vous rend │   PENDANT LE       │   ce qui fait
    capable de servir│   SERVICE          │   venir le monde
                     └────  croisement ───┘

Quatre échanges transitent par le croisement — la commande et l'encaissement
vont de la vente vers la gestion, la carte et la marge font le chemin inverse.

Chaque grande boucle contient quatre sous-boucles, soit **huit** en tout.

Les trois lois
--------------
1. Une boucle se referme : son dernier maillon nourrit son premier. Sinon
   c'est un tunnel, et un tunnel se parcourt une fois puis s'oublie.
2. Une boucle nourrit une autre boucle. Aucune n'est autonome.
3. Casser une sous-boucle casse les deux grandes.

C'est la troisième qui porte tout l'argumentaire commercial : dix logiciels qui
tiennent chacun une boucle ne font pas huit boucles connectées, ils font huit
tunnels.

Les trois lectures
------------------
Le même système se raconte de trois façons, selon l'interlocuteur :

    temporelle   avant · pendant · après le service   — la langue du restaurateur
    économique   ce que ça coûte, ce que ça rapporte  — la langue du gérant
    humaine      qui fait quoi, à quel poste          — la langue de l'équipe

Elles ne se contredisent pas, elles se superposent : « avant le service »
recouvre la boucle gestion, « après le service » recouvre la boucle vente, et
« pendant le service » est le croisement lui-même. Le centre du schéma et le
centre de la journée sont le même endroit.

C'est cette superposition qui relie les trois séries. La série « Une journée »
est la lecture humaine et temporelle ; la série « L'IA dans FoodEatUp » est le
système expliqué. Ce ne sont pas trois sujets, c'est un objet vu sous trois
angles.
"""

# ── Les deux boucles infinies ────────────────────────────────────────────────

GRANDES = {
    "gestion": {
        "nom": "La boucle gestion",
        "cote": "gauche",
        "quoi": "ce qui vous rend capable de servir",
        "detail": "Vos fiches, votre équipe, vos stocks, votre HACCP. Ce qui "
                  "vous donne le droit et la capacité d'ouvrir demain.",
        "invisible": "Elle ne se voit pas depuis la salle. Mais quand elle "
                     "grippe, le saumon manque un vendredi soir.",
        "phase": "avant",
    },
    "vente": {
        "nom": "La boucle vente",
        "cote": "droite",
        "quoi": "ce qui fait venir le monde",
        "detail": "Votre carte en ligne, ce qui circule, ceux qui reviennent, "
                  "ce qui rentre. Ce qui remplit la salle et la caisse.",
        "invisible": "Elle se voit trop bien : c'est la seule qu'on regarde "
                     "quand le restaurant est vide.",
        "phase": "apres",
    },
}

# ── Le croisement ────────────────────────────────────────────────────────────
# Quatre échanges, deux dans chaque sens. C'est le seul endroit où les deux
# boucles se touchent, et c'est « pendant le service ».

CROISEMENT = [
    ("La commande", "vente", "gestion", "Une vente devient un besoin en cuisine."),
    ("L'encaissement", "vente", "gestion",
     "Une vente devient de l'argent qui paiera la prochaine commande."),
    ("La carte", "gestion", "vente",
     "Ce que vous pouvez produire devient ce que vous pouvez vendre."),
    ("La marge", "gestion", "vente",
     "Ce que vous maîtrisez en coût finance ce que vous investissez en clients."),
]

# ── Les huit boucles ─────────────────────────────────────────────────────────
# `outils` = nombre d'outils MCP qui exécutent la boucle, tel qu'annoncé sur la
# page produit. Attention : la somme fait 146 alors que la surface annoncée est
# de 177. Les 31 restants sont hors boucles. Ne pas afficher « 177 outils » sur
# une planche qui détaille les huit — le compte ne tomberait pas juste.

BOUCLES = [
    {
        "n": "01", "slug": "configuration", "grande": "gestion",
        "nom": "Configuration boutique", "role": "Le socle de la boucle gestion",
        "quoi": "Vos fiches, vos prix, votre carte",
        "produit": "Le document de référence de toute la boucle gestion. La "
                   "fiche technique dit ce qu'il y a dans le plat, ce qu'il "
                   "coûte et ce qu'il rapporte.",
        "coupee": "Tout le reste tourne à vide. Une fiche fausse fausse le "
                  "food cost, le stock, la marge et le prix.",
        "nourrit": ["stockvisionai"], "outils": 21,
        "module": "configuration",
    },
    {
        "n": "02", "slug": "equipe", "grande": "gestion",
        "nom": "Équipe", "role": "Qui exécute",
        "quoi": "Qui travaille, et ce que ça coûte",
        "produit": "La capacité humaine — combien de couverts peuvent "
                   "réellement être servis — et le coût salarial, premier "
                   "poste maîtrisable d'un restaurant.",
        "coupee": "Sur-effectif le mardi, sous-effectif le samedi. "
                  "Systématiquement.",
        "nourrit": ["comptabilite"], "outils": 18,
        "module": "equipe-planning",
    },
    {
        "n": "03", "slug": "stockvisionai", "grande": "gestion",
        "nom": "StockVisionAI", "role": "La boucle mère",
        "quoi": "Ce qu'il reste, ce qu'il faut",
        "produit": "La disponibilité réelle, qui conditionne ce qui peut être "
                   "vendu. Et le coût matière réel, qui conditionne la marge.",
        "coupee": "Une rupture un samedi soir, ou quatre à dix pour cent des "
                  "achats à la poubelle le dimanche.",
        "nourrit": ["haccp"], "outils": 14,
        "module": "stockvision-ai",
    },
    {
        "n": "04", "slug": "haccp", "grande": "gestion",
        "nom": "HACCP", "role": "Le droit d'exercer",
        "quoi": "La conformité, tenue au jour le jour",
        "produit": "La conformité sanitaire, et les justificatifs opposables "
                   "en cas de contrôle.",
        "coupee": "C'est la seule boucle dont l'échec n'est pas financier mais "
                  "existentiel. Les sept autres coûtent de la marge. "
                  "Celle-ci coûte la fermeture.",
        "nourrit": ["stockvisionai"], "outils": 17,
        "module": "haccp",
    },
    {
        "n": "05", "slug": "ecommerce", "grande": "vente",
        "nom": "E-commerce", "role": "L'exposition",
        "quoi": "Votre carte, en ligne",
        "produit": "Le canal direct. Des clients qui appartiennent au "
                   "restaurant, et non à une plateforme qui prélève une "
                   "commission par couvert.",
        "coupee": "Le restaurant dépend des plateformes et leur cède une "
                  "commission sur des clients qu'il ne connaîtra jamais.",
        "nourrit": ["fidelite"], "outils": 22,
        "module": "site-web-vitrine",
    },
    {
        "n": "06", "slug": "communication", "grande": "vente",
        "nom": "Communication", "role": "Le système nerveux",
        "quoi": "Ce qui circule",
        "produit": "La circulation. C'est la seule boucle qui touche les sept "
                   "autres : un stock bas déclenche une alerte, une "
                   "réservation déclenche un rappel.",
        "coupee": "Les sept autres tournent correctement, et personne ne le "
                  "sait. C'est la panne la plus insidieuse : rien ne casse, "
                  "tout ralentit.",
        "nourrit": ["fidelite"], "outils": 14,
        "module": "marketing-fidelite",
    },
    {
        "n": "07", "slug": "fidelite", "grande": "vente",
        "nom": "Fidélité et marketing", "role": "L'usine à revenir",
        "quoi": "Ceux qui reviennent",
        "produit": "Le fichier client — le seul actif d'acquisition qui "
                   "appartienne vraiment au restaurant.",
        "coupee": "On rachète chaque client à chaque fois. Acquérir coûte cinq "
                  "à sept fois plus cher que faire revenir.",
        "nourrit": ["ecommerce"], "outils": 23,
        "module": "marketing-fidelite",
    },
    {
        "n": "08", "slug": "comptabilite", "grande": "vente",
        "nom": "Comptabilité", "role": "Le second croisement",
        "quoi": "Ce qui rentre, ce qui sort",
        "produit": "La trésorerie qui finance les achats. C'est le second fil "
                   "qui traverse le croisement, après la commande.",
        "coupee": "On ignore si l'on gagne de l'argent, et on le découvre trop "
                  "tard.",
        "nourrit": ["stockvisionai"], "outils": 17,
        "module": "comptabilite",
    },
]

PAR_SLUG = {b["slug"]: b for b in BOUCLES}

# ── Les quatre agents ────────────────────────────────────────────────────────
# Aucune case vide n'est un oubli : c'est une boucle que l'agent ne touche pas.
# PrédiBot voit les huit parce que le directeur doit tout voir ; les trois
# autres se spécialisent parce que leurs utilisateurs se spécialisent.

AGENTS = {
    "caroline": {
        "nom": "Caroline", "quoi": "Elle décroche",
        "phrase": "Le client ne verra jamais votre logiciel. Il appelle, "
                  "elle décroche.",
        "boucles": {"ecommerce": "pilote", "communication": "pilote"},
    },
    "jarvis": {
        "nom": "Jarvis", "quoi": "L'assistant vocal de l'atelier",
        "phrase": "Les mains dans la farine, on ne tape pas. On parle.",
        "boucles": {"configuration": "lit", "equipe": "pilote",
                    "stockvisionai": "pilote", "haccp": "pilote"},
    },
    "predibot": {
        "nom": "PrédiBot", "quoi": "Il voit les huit",
        "phrase": "Le directeur doit tout voir. Lui aussi.",
        "boucles": {b["slug"]: "pilote" for b in BOUCLES},
    },
    "iris": {
        "nom": "Iris", "quoi": "Le moteur de la communication",
        "phrase": "Ce que vous savez le matin, vos clients le savent à midi.",
        "boucles": {"configuration": "lit", "stockvisionai": "lit",
                    "ecommerce": "pilote", "communication": "moteur",
                    "fidelite": "pilote"},
    },
}

# ── Le socle technique ───────────────────────────────────────────────────────

MCP = {
    "endpoint": "https://foodeatup.com/api/mcp",
    "surface": 177,
    "dans_les_boucles": sum(b["outils"] for b in BOUCLES),   # 146
    "auth": "OAuth2 client credentials, une paire par établissement",
    "isolation": "Chaque appel est circonscrit à l'établissement porteur des "
                 "identifiants",
    "transport": "HTTP et SSE",
    "difference": "La plupart des logiciels d'hospitalité exposent une API "
                  "construite autour d'un objet — le ticket, la réservation. "
                  "Celle-ci est modelée autour de l'établissement : chaque "
                  "outil suit la forme d'une journée de restaurant plutôt que "
                  "la forme d'une base de données.",
}

# ── La démonstration de référence ────────────────────────────────────────────
# Le cas du saumon traverse les huit boucles en huit gestes. C'est l'exemple
# canonique : quand une série doit montrer le système entier, elle le rejoue
# plutôt que d'en inventer un autre.

SAUMON = [
    ("stockvisionai", "Jeudi 9 h. StockVisionAI voit 12 kg de saumon avec une "
                      "DLC vendredi soir."),
    ("haccp", "Le contrôle à réception d'hier confirme la traçabilité : les "
              "lots sont sains."),
    ("configuration", "Vos fiches savent quels plats consomment du saumon : "
                      "tartare, pavé, poke bowl."),
    ("communication", "Iris propose un post « Saumon frais aujourd'hui ». "
                      "Vous validez en un swipe."),
    ("fidelite", "Le segment « amateurs de poisson » — 340 clients — reçoit un "
                 "message ciblé."),
    ("ecommerce", "Les habitués réservent ou commandent en click-and-collect. "
                  "Caroline prend les appels."),
    ("equipe", "PrédiBot ajuste le planning du service : deux personnes de "
               "plus en cuisine."),
    ("comptabilite", "Vendredi 23 h : les 12 kg sont partis. La marge du jour "
                     "est déjà dans le tableau."),
]

LOIS = [
    ("Une boucle se referme",
     "Son dernier maillon nourrit son premier. Si la fin ne revient pas au "
     "début, ce n'est pas une boucle, c'est un tunnel — et un tunnel se "
     "parcourt une fois, puis on l'oublie."),
    ("Une boucle nourrit une autre boucle",
     "Aucune n'est autonome. Chacune produit une sortie qui devient l'entrée "
     "d'une voisine."),
    ("Casser une sous-boucle casse les deux grandes",
     "Dix logiciels qui tiennent chacun une boucle ne font pas huit boucles "
     "connectées. Ils font huit tunnels."),
]

LECTURES = {
    "temporelle": ("Avant · Pendant · Après le service", "le restaurateur",
                   "C'est la seule taxonomie qui parle sa langue — les "
                   "concurrents rangent par module, c'est-à-dire dans la "
                   "langue du logiciel."),
    "economique": ("Ce que ça coûte, ce que ça rapporte", "le gérant",
                   "Chaque boucle a un prix quand elle grippe, et il se "
                   "chiffre."),
    "humaine": ("Qui fait quoi, à quel poste", "l'équipe",
                "Dix métiers, une seule journée. Chacun ne voit qu'un arc du "
                "huit, et personne ne voit le tout — sauf le logiciel."),
}


def phase_de(slug):
    """La phase de journée que recouvre une boucle.

    « Avant le service » recouvre la gestion, « après » recouvre la vente, et
    « pendant » est le croisement. C'est ce qui permet de relier un épisode de
    la série « Une journée » à une boucle sans le décider à la main.
    """
    return GRANDES[PAR_SLUG[slug]["grande"]]["phase"]


if __name__ == "__main__":
    print(f"{len(BOUCLES)} boucles, {len(AGENTS)} agents, "
          f"{MCP['dans_les_boucles']} outils dans les boucles "
          f"sur {MCP['surface']} annoncés")
    for g, d in GRANDES.items():
        ns = [b["nom"] for b in BOUCLES if b["grande"] == g]
        print(f"  {d['nom']:20} {' · '.join(ns)}")
