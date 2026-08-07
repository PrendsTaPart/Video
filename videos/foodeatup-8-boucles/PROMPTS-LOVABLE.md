# Prompts Lovable — module « Les 8 Boucles FoodEatUp »

Projet **foodeatup-guide-star** → https://lovable.dev/projects/55ff35b7-c442-42c4-950c-8c7fd420c645

Un prompt = un message. Vérifier le diff entre chaque.

---

## Ce qui a changé par rapport au brief d'origine

Le brief L1–L4 a été écrit avant que le site n'atteigne son état actuel, et avant
que les vidéos existent. Trois adaptations, à connaître avant de coller :

1. **L1 et L3 sont fusionnés** en un seul prompt (`A` ci-dessous). Les neuf vidéos
   sont rendues et en ligne : créer les fiches avec `videoUrl: ""` puis repasser
   les remplir, c'est deux tours de crédits et un état intermédiaire où l'Academy
   affiche « Bientôt disponible » pour des vidéos qui existent.
2. **Aucun nom de tableau n'est imposé.** Le brief parlait de `allCategories`,
   `allModules`, `allTutorials` ; le code expose `tutorials`, `modules`,
   `getModule`, `getCategory`. Les prompts décrivent l'intention et laissent
   l'agent suivre les conventions du fichier.
3. **Les compteurs d'outils MCP sont corrigés.** Ceux du brief
   (21/18/14/17/22/14/23/17) sommaient à 146, incompatible avec le total 177
   annoncé. Recomptage fait sur le serveur MCP : le total 177 est exact, la
   répartition ne l'était pas. Voir `mcp-tool-counts.json`.

La vidéo `boucle-00-principe` n'est **pas** une neuvième fiche : c'est la vidéo
de présentation du module, en `heroVideoUrl` / `heroPosterUrl`.

---

## Prompt A — le module, ses 8 fiches, et les vidéos

```text
Ajoute un module transversal « Les 8 Boucles FoodEatUp » à l'Academy. Tout se
passe dans src/data/tutorials.ts : le modèle de données actuel suffit, ne touche
à aucun composant ni à aucun tutoriel existant.

Suis les conventions déjà en place dans ce fichier (noms des tableaux, forme des
objets Tutorial et Module, façon dont les catégories sont déclarées et
résolues) — je décris ci-dessous ce qu'il faut obtenir, pas comment le nommer.

1) UNE CATÉGORIE : slug "les-8-boucles", nom « Les 8 Boucles FoodEatUp »,
   couleur #147AFF.

2) UN MODULE, placé EN PREMIER de la liste des modules :
   slug "les-8-boucles", nom « Les 8 Boucles FoodEatUp », 8 tutoriels attendus,
   rattaché à la catégorie "les-8-boucles",
   illustration : brandMascots.agentStockvision (déjà exporté par src/data/brand.ts),
   et trois sections, dans cet ordre :
     - « La boucle gestion — pouvoir ouvrir demain »
     - « La boucle vente — faire venir et revenir »
     - « Le croisement — là où les deux se touchent »

   Le module a aussi une vidéo de présentation, avec la même mécanique que le
   module predibot :
     heroVideoUrl  = https://rapido-software.s3.eu-west-3.amazonaws.com/rapidosoftware/cms/bibliotheque/boucle-00-principe-v1
     heroPosterUrl = https://rapido-software.s3.eu-west-3.amazonaws.com/rapidosoftware/cms/bibliotheque/boucle-00-principe-thumbnail
   Titre : « Le principe : une boucle se referme » (45 s).

3) LES 8 TUTORIELS, avec leurs vidéos — elles sont en ligne, ce ne sont pas des
   fiches « bientôt disponible ».

[COLLE ICI LE BLOC « LES 8 FICHES » — section suivante de ce fichier]

INTERDITS
- ne modifie aucun tutoriel existant, il y en a 149 en ligne ;
- aucune donnée métier en localStorage ;
- aucune couleur hors palette (crème #FCF9E6, marine #0F1A23, bleu #007BFF,
  bleu système #147AFF, orange #FFA500) ;
- ne redessine aucun logo, n'invente aucun chiffre.

CRITÈRES D'ACCEPTATION
- /module/les-8-boucles affiche 8 fiches, groupées dans les 3 sections, de 1 à 8 ;
- la page module ouvre sur la vidéo de présentation ;
- chaque fiche monte un lecteur vidéo avec sa vignette en poster, et affiche
  « Comment ça marche ? », « À quoi ça sert ? », les prompts copiables et
  l'astuce du chef ;
- la carte du module en page d'accueil affiche « 8 / 8 vidéos », barre pleine ;
- aucune fiche ne garde un videoUrl vide ;
- les durées affichées correspondent aux durées réelles des fichiers ;
- le build passe sans erreur TypeScript.
```

### Les 8 fiches (à coller dans le prompt A)

Les URLs sont celles de la bibliothèque RapidoCMS, vérifiées octet par octet.
Les durées sont mesurées sur les MP4 rendus.

```ts
{
  slug: "boucle-01-configuration-boutique",
  title: "Boucle 01 — Configuration boutique : un prix change, toutes vos marges se recalculent",
  moduleSlug: "les-8-boucles",
  subcategory: "01 · Le socle de la boucle gestion",
  section: "La boucle gestion — pouvoir ouvrir demain",
  order: 1,
  videoUrl: "https://rapido-software.s3.eu-west-3.amazonaws.com/rapidosoftware/cms/bibliotheque/boucle-01-configuration-boutique-v1",
  thumbnailUrl: "https://rapido-software.s3.eu-west-3.amazonaws.com/rapidosoftware/cms/bibliotheque/boucle-01-configuration-boutique-thumbnail",
  durationSeconds: 76,
  howItWorks: [
    "Établissement et TVA : le cadre légal de tout ce qui suivra",
    "Catégories : la grammaire de votre carte",
    "Ingrédients et prix d'achat : la seule donnée que vous saisissez à la main",
    "Fiches techniques : ce qu'il y a dans le plat, ce qu'il coûte, ce qu'il rapporte",
    "Carte et prix de vente : ce que le client voit",
    "Les ventes révèlent, vous ajustez — et la boucle repart",
  ],
  whatItsFor:
    "Produire le document de référence de toute la boucle gestion : la fiche technique. Rien en aval ne peut la contredire. Vous saisissez un prix fournisseur une fois ; toutes les fiches qui contiennent l'ingrédient se recalculent, le food cost bouge, la marge par plat suit, et les plats passés sous votre seuil remontent. 39 outils MCP exécutent cette boucle. Si elle est coupée, tout le reste tourne à vide.",
  claudePrompts: [
    {
      title: "Diagnostiquer ma configuration",
      prompt:
        "Fais le diagnostic de la boucle Configuration de mon établissement [ID établissement] : liste mes catégories, mes taux de TVA, mes unités, mes zones et mes tables, puis croise avec mes plats et mes produits. Signale chaque plat sans catégorie ou sans TVA, chaque zone sans table, et chaque équipement froid déclaré mais jamais relevé. Propose les corrections une par une, sans rien créer avant mon accord.",
    },
    {
      title: "Répercuter un nouveau prix fournisseur",
      prompt:
        "Mets à jour le prix de l'ingrédient [nom] à [prix] par [unité] chez [fournisseur] pour l'établissement [ID établissement], puis dis-moi quelles recettes et quels plats sont impactés, leur nouveau coût matière et leur nouvelle marge en euros et en pourcentage. Liste ceux qui passent sous [seuil de marge] %.",
    },
  ],
  chefTip:
    "Ne remontez jamais un prix fournisseur à la main dans chaque fiche : saisissez-le une fois sur l'ingrédient et laissez les fiches se recalculer. Le jour où un chiffre vous semble faux, c'est presque toujours l'ingrédient qu'il faut vérifier, pas la recette.",
},
{
  slug: "boucle-02-equipe",
  title: "Boucle 02 — Équipe : vos plannings tiennent compte de l'activité réelle",
  moduleSlug: "les-8-boucles",
  subcategory: "02 · Qui exécute",
  section: "La boucle gestion — pouvoir ouvrir demain",
  order: 2,
  videoUrl: "https://rapido-software.s3.eu-west-3.amazonaws.com/rapidosoftware/cms/bibliotheque/boucle-02-equipe-v1",
  thumbnailUrl: "https://rapido-software.s3.eu-west-3.amazonaws.com/rapidosoftware/cms/bibliotheque/boucle-02-equipe-thumbnail",
  durationSeconds: 72,
  howItWorks: [
    "Recrutement puis contrat : qui a le droit de travailler, et à quelles conditions",
    "Planning : qui travaille, quand",
    "Pointage réel : ce qui s'est vraiment passé, pas ce qui était prévu",
    "Congés : les absences validées en connaissance de la couverture",
    "Coût constaté puis écart prévu/réel",
    "Le planning suivant part de cet écart",
  ],
  whatItsFor:
    "Produire la capacité humaine — combien de couverts peuvent réellement être servis — et le coût salarial, premier poste maîtrisable d'un restaurant (25 à 35 % du chiffre d'affaires). Le trou de staffing se qualifie sur les réservations réelles, pas au ressenti. 21 outils MCP. Si elle est coupée : sur-effectif le mardi, sous-effectif le samedi, systématiquement.",
  claudePrompts: [
    {
      title: "État de mon staffing pour la semaine",
      prompt:
        "Fais l'état de la boucle Équipe de l'établissement [ID établissement] : effectif actif, contrats manquants ou expirés, planning des 7 prochains jours croisé avec les réservations, congés en attente et pointages incohérents. Montre-moi les créneaux où les couverts attendus ne sont pas couverts, et propose trois actions maximum.",
    },
    {
      title: "Traiter un congé sans casser le service",
      prompt:
        "Vérifie la couverture du planning sur [dates] pour l'établissement [ID établissement] avant de me dire si je peux approuver le congé de [prénom]. Si un créneau devient découvert, propose le shift de remplacement et son coût avant d'approuver quoi que ce soit.",
    },
  ],
  chefTip:
    "Regardez votre planning à côté de vos réservations, jamais seul. Un planning fait « comme d'habitude » est un planning fait sans information — et c'est là que partent vos points de marge.",
},
{
  slug: "boucle-03-stockvision",
  title: "Boucle 03 — StockVisionAI : vos ventes deviennent vos achats et votre production",
  moduleSlug: "les-8-boucles",
  subcategory: "03 · La boucle mère",
  section: "La boucle gestion — pouvoir ouvrir demain",
  order: 3,
  videoUrl: "https://rapido-software.s3.eu-west-3.amazonaws.com/rapidosoftware/cms/bibliotheque/boucle-03-stockvision-v1",
  thumbnailUrl: "https://rapido-software.s3.eu-west-3.amazonaws.com/rapidosoftware/cms/bibliotheque/boucle-03-stockvision-thumbnail",
  durationSeconds: 73,
  howItWorks: [
    "Les besoins viennent des fiches techniques, pas de l'intuition",
    "Commande fournisseur, après vérification des livraisons déjà en route",
    "Réception et contrôle (le contrôle HACCP se déclenche ici)",
    "Entrée en stock",
    "Consommation par la production",
    "Inventaire, puis écart",
    "L'écart redevient un besoin",
  ],
  whatItsFor:
    "Produire la disponibilité réelle — ce qui conditionne ce qui peut être vendu — et le coût matière réel, qui conditionne la marge. C'est la seule boucle qui contient une prévision : le modèle lit l'historique par jour de semaine, écarte les valeurs aberrantes et injecte les jours fériés français. 11 outils MCP la pilotent — c'est le plus petit compteur de la série, et pourtant la boucle mère : ce n'est pas le nombre d'outils qui fait sa centralité, c'est sa position dans le système. Si elle est coupée : une rupture un samedi soir, ou 4 à 10 % des achats à la poubelle le dimanche.",
  claudePrompts: [
    {
      title: "Suis-je prêt pour le week-end ?",
      prompt:
        "Fais l'état de la boucle Stock et Production de l'établissement [ID établissement] : stocks bas d'abord, puis plans de production à venir et ingrédients manquants. Croise avec mes réservations et mes commandes sur [période] pour me dire si je peux servir ce que je prévois de vendre. Vérifie les livraisons déjà en cours avant de proposer la moindre commande.",
    },
    {
      title: "Préparer une commande fournisseur",
      prompt:
        "Prépare la commande fournisseur pour [fournisseur] à l'établissement [ID établissement] à partir de mes stocks bas et de mes productions planifiées jusqu'au [date]. Montre-moi la commande ligne par ligne avec les quantités et le montant, et attends mon accord avant de la créer.",
    },
  ],
  chefTip:
    "Avant de commander, regardez toujours les livraisons déjà en route. La double commande est l'erreur la plus chère et la plus fréquente de cette boucle.",
},
{
  slug: "boucle-04-haccp",
  title: "Boucle 04 — HACCP : votre dossier de conformité se construit chaque jour",
  moduleSlug: "les-8-boucles",
  subcategory: "04 · Le droit d'exercer",
  section: "La boucle gestion — pouvoir ouvrir demain",
  order: 4,
  videoUrl: "https://rapido-software.s3.eu-west-3.amazonaws.com/rapidosoftware/cms/bibliotheque/boucle-04-haccp-v1",
  thumbnailUrl: "https://rapido-software.s3.eu-west-3.amazonaws.com/rapidosoftware/cms/bibliotheque/boucle-04-haccp-thumbnail",
  durationSeconds: 74,
  howItWorks: [
    "Plan de maîtrise sanitaire : le cadre",
    "Relevés de températures, dictés au moment du geste",
    "Contrôles à réception, à chaque livraison",
    "Étiquetage DLC",
    "Checklists d'hygiène et plan de nettoyage",
    "Journal quotidien horodaté",
    "Action corrective dès qu'une valeur sort des limites",
  ],
  whatItsFor:
    "Produire la conformité sanitaire et les justificatifs opposables en cas de contrôle. FoodEatUp ne remplit jamais un relevé à votre place — une température se mesure, elle ne s'invente pas — mais il compte les trous : jours sans relevé, livraisons sans contrôle, zones jamais nettoyées. Un jour sans relevé est « non conforme », pas « probablement fait ». 16 outils MCP. C'est la seule boucle dont l'échec n'est pas financier mais existentiel.",
  claudePrompts: [
    {
      title: "Si un contrôleur entre maintenant, qu'est-ce qui manque ?",
      prompt:
        "Audite ma conformité HACCP sur [période] pour l'établissement [ID établissement] : jours sans relevé de température par équipement, traçabilités ouvertes non complétées, livraisons sans contrôle à réception, checklists non validées, zones jamais nettoyées, étiquettes DLC qui expirent. Donne-moi un score de complétude calculé, pas estimé, et la liste des rattrapages possibles.",
    },
    {
      title: "Enregistrer un relevé dicté",
      prompt:
        "Enregistre le relevé de température de [équipement] : [valeur] °C, relevé le [date et heure], à l'établissement [ID établissement]. Si la valeur sort des limites réglementaires, dis-le et propose l'action corrective.",
    },
  ],
  chefTip:
    "Dictez le relevé au moment où vous ouvrez le frigo, pas en fin de service. Un registre se juge sur ses trous — et les trous se creusent toujours le soir, quand on se dit qu'on le fera plus tard.",
},
{
  slug: "boucle-05-ecommerce",
  title: "Boucle 05 — E-commerce : votre carte en ligne, sans commission",
  moduleSlug: "les-8-boucles",
  subcategory: "05 · L'exposition",
  section: "La boucle vente — faire venir et revenir",
  order: 5,
  videoUrl: "https://rapido-software.s3.eu-west-3.amazonaws.com/rapidosoftware/cms/bibliotheque/boucle-05-ecommerce-v1",
  thumbnailUrl: "https://rapido-software.s3.eu-west-3.amazonaws.com/rapidosoftware/cms/bibliotheque/boucle-05-ecommerce-thumbnail",
  durationSeconds: 75,
  howItWorks: [
    "La carte en ligne, mise à jour d'un seul endroit",
    "La visite : QR de table, site, réseaux, recherche locale",
    "Panier ou réservation",
    "Commande",
    "Service",
    "Avis",
    "Ajustement de la carte — et ça recommence",
  ],
  whatItsFor:
    "Produire le canal direct : des clients qui appartiennent au restaurant, et non à une plateforme qui prélève une commission par couvert. La boucle répond à une question simple : par où l'argent entre-t-il, et quel canal fuit ? Une demande de privatisation sans réponse depuis plus de 48 h passe en tête des actions. 39 outils MCP.",
  claudePrompts: [
    {
      title: "Quel canal fuit ?",
      prompt:
        "Fais l'état de la boucle E-commerce et Vente de l'établissement [ID établissement] sur [période] : commandes, réservations à venir et capacité restante, session de caisse et ardoises ouvertes anormalement anciennes, statut du site vitrine et de son domaine, zones de livraison, happy hours, demandes de privatisation sans réponse. Signale ce qui fuit, canal par canal.",
    },
    {
      title: "Mettre le plat du jour en ligne",
      prompt:
        "Ajoute [nom du plat] à [prix] à ma carte en ligne pour l'établissement [ID établissement], dans la catégorie [catégorie], et dis-moi où il apparaît : site, QR de table, commande en ligne. Ne publie rien sans mon accord.",
    },
  ],
  chefTip:
    "Publiez votre carte en ligne avant d'ouvrir vos réseaux. Un client qui vous trouve sans pouvoir commander chez vous ira commander chez la plateforme — et c'est elle qui gardera son nom.",
},
{
  slug: "boucle-06-communication",
  title: "Boucle 06 — Communication : ce que vous savez, vos clients le savent le matin même",
  moduleSlug: "les-8-boucles",
  subcategory: "06 · Le système nerveux",
  section: "La boucle vente — faire venir et revenir",
  order: 6,
  videoUrl: "https://rapido-software.s3.eu-west-3.amazonaws.com/rapidosoftware/cms/bibliotheque/boucle-06-communication-v1",
  thumbnailUrl: "https://rapido-software.s3.eu-west-3.amazonaws.com/rapidosoftware/cms/bibliotheque/boucle-06-communication-thumbnail",
  durationSeconds: 72,
  howItWorks: [
    "Un événement ou une intention déclenche la boucle",
    "Choix du canal : email, SMS, WhatsApp, réseaux",
    "Création du contenu par Iris, à partir de vos données réelles",
    "Contrôle de charte : un visuel hors palette est rejeté",
    "Diffusion, uniquement après votre accord",
    "Mesure : envois, clics, commandes attribuées",
    "Apprentissage : ce qui a marché nourrit la proposition suivante",
  ],
  whatItsFor:
    "Produire la circulation. C'est la seule boucle qui touche les sept autres : un stock bas déclenche une alerte, une réservation déclenche un rappel, une température anormale déclenche une notification. Règle non négociable : sous 10 contacts, aucune campagne segmentée n'est proposée — une base trop petite ne produit aucun signal exploitable. 15 outils MCP. Quand elle est coupée, rien ne casse : tout ralentit.",
  claudePrompts: [
    {
      title: "Ai-je de quoi parler, et à qui ?",
      prompt:
        "Fais l'état de ma boucle Communication pour l'établissement [ID établissement] : taille de ma base clients, taille de chaque segment RFM, campagnes en cours et leurs statistiques réelles, avis sans réponse et avis négatifs récents, leads du site non convertis en clients. Ne me propose aucune campagne sur un segment de moins de 10 contacts.",
    },
    {
      title: "Écouler un surstock avant la date limite",
      prompt:
        "J'ai [quantité] de [produit] à écouler avant le [date] à l'établissement [ID établissement]. Vérifie le stock et la marge du plat concerné, dis-moi quel segment viser et sa taille réelle, puis prépare la campagne en brouillon. N'envoie rien : je valide avant.",
    },
  ],
  chefTip:
    "Si votre segment fait moins de dix contacts, ne cherchez pas à écrire un meilleur message : cherchez à collecter des clients. Le QR de table, les leads du site et la roue cadeaux sont faits pour ça.",
},
{
  slug: "boucle-07-fidelite",
  title: "Boucle 07 — Fidélité et marketing : chaque client servi devient une relation réactivable",
  moduleSlug: "les-8-boucles",
  subcategory: "07 · L'usine à revenir",
  section: "La boucle vente — faire venir et revenir",
  order: 7,
  videoUrl: "https://rapido-software.s3.eu-west-3.amazonaws.com/rapidosoftware/cms/bibliotheque/boucle-07-fidelite-v1",
  thumbnailUrl: "https://rapido-software.s3.eu-west-3.amazonaws.com/rapidosoftware/cms/bibliotheque/boucle-07-fidelite-thumbnail",
  durationSeconds: 71,
  howItWorks: [
    "Client servi",
    "Consentement — sans lui, la boucle communication n'a personne à qui parler",
    "Segmentation",
    "Campagne ciblée",
    "Retour en salle",
    "Points et récompenses",
    "Nouvelle donnée, qui affine le segment suivant",
  ],
  whatItsFor:
    "Produire le fichier client — le seul actif d'acquisition qui appartienne vraiment au restaurant — et l'opt-in. Première vérification systématique : le programme est-il actif ? Un catalogue de récompenses posé sur un programme éteint ne produit rien. L'encours de cartes cadeaux est une dette, pas un chiffre d'affaires. 19 outils MCP. Acquérir coûte 5 à 7 fois plus cher que faire revenir.",
  claudePrompts: [
    {
      title: "Mon programme de fidélité rapporte-t-il ?",
      prompt:
        "Commence par me dire si mon programme de fidélité est actif à l'établissement [ID établissement], et sous quel mode. S'il est actif, montre-moi le catalogue de récompenses et leurs stocks, les bons émis contre les bons utilisés, l'encours de cartes cadeaux, et les statistiques de la roue et des sondages. Signale toute incohérence.",
    },
    {
      title: "Rappeler les clients endormis",
      prompt:
        "Sors-moi la liste des clients de l'établissement [ID établissement] qui ne sont pas revenus depuis [durée], avec ce qu'ils commandaient et leur panier moyen. Dis-moi la taille du segment avant de me proposer quoi que ce soit.",
    },
  ],
  chefTip:
    "Vérifiez d'abord que le programme est actif. Un catalogue de récompenses magnifique sur un programme éteint, c'est la panne la plus fréquente — et la plus invisible.",
},
{
  slug: "boucle-08-comptabilite",
  title: "Boucle 08 — Comptabilité : le chiffre du jour, avant d'éteindre la lumière",
  moduleSlug: "les-8-boucles",
  subcategory: "08 · Le second croisement",
  section: "Le croisement — là où les deux se touchent",
  order: 8,
  videoUrl: "https://rapido-software.s3.eu-west-3.amazonaws.com/rapidosoftware/cms/bibliotheque/boucle-08-comptabilite-v1",
  thumbnailUrl: "https://rapido-software.s3.eu-west-3.amazonaws.com/rapidosoftware/cms/bibliotheque/boucle-08-comptabilite-thumbnail",
  durationSeconds: 68,
  howItWorks: [
    "Vente",
    "Facture",
    "Encaissement",
    "Dépenses et achats",
    "Marge constatée",
    "Trésorerie",
    "Capacité d'achat — qui redevient une commande fournisseur",
  ],
  whatItsFor:
    "Produire la trésorerie qui finance les achats : c'est le second fil qui traverse le croisement, après la commande. Le livrable le plus utile n'est pas le chiffre d'affaires, ce sont les écarts entre le rapport de caisse et les factures. Une facture ne passe à « payée » que sur votre information explicite, jamais par déduction. 17 outils MCP. Sans elle, on ignore si l'on gagne de l'argent, et on le découvre trop tard.",
  claudePrompts: [
    {
      title: "Ce qui a été vendu a-t-il été facturé, et payé ?",
      prompt:
        "Fais l'état de ma boucle Comptabilité sur [période] pour l'établissement [ID établissement] : synthèse financière, factures impayées triées par ancienneté, devis en attente de réponse, dépenses de la période, et surtout les écarts entre le rapport de caisse et les factures. Ne passe aucune facture en payée sans que je te l'aie dit.",
    },
    {
      title: "Clôturer et comprendre la journée",
      prompt:
        "Fais le point de fin de journée de l'établissement [ID établissement] : chiffre d'affaires, ticket moyen, couverts, marge, et comparaison avec [période de référence]. Montre-moi l'écart de caisse s'il y en a un.",
    },
  ],
  chefTip:
    "Faites le Z tous les soirs, même quand la journée a été calme. Un écart retrouvé le jour même prend deux minutes ; retrouvé en fin de mois, il ne se retrouve plus.",
},
```

---

## Prompt B — la page pilier : le simulateur « changez un prix »

À passer une fois le prompt A vérifié.

```text
Sur la page du module /module/les-8-boucles, ajoute AU-DESSUS de la liste des
fiches une section pédagogique interactive « Voir l'effet d'une facture sur tout
le restaurant ». C'est la démonstration du module : elle doit se manipuler, pas
se lire.

COMPOSANT <SimulateurBoucle /> — état React uniquement, aucun localStorage,
aucun appel réseau, aucune donnée réelle d'établissement :
- un curseur « Prix du kilo de bœuf », de 8,00 € à 18,00 €, valeur initiale 11,20 € ;
- sous le curseur, une CHAÎNE de 8 maillons affichés horizontalement (verticalement
  en mobile) : Prix fournisseur → Ingrédient → Fiche technique → Food cost →
  Marge par plat → Carte et prix de vente → Achats et production →
  Stock et rentabilité ;
- quand on bouge le curseur, les maillons s'allument SÉQUENTIELLEMENT en bleu
  #007BFF, environ 90 ms d'écart entre deux maillons : on doit voir la donnée
  circuler, pas tout changer d'un coup ;
- une carte « Votre burger » qui affiche en direct le coût matière, la marge en
  euros, la marge en pourcentage, et l'écart vs la valeur initiale. Le calcul doit
  être explicite et lisible dans le code : coût matière = 4,38 € à 11,20 €/kg,
  dont 1,90 € de bœuf qui varie proportionnellement au curseur ; prix de vente
  fixe 14,00 € ; marge = prix − coût ;
- un seuil de marge réglable, 65 % par défaut : dès que la marge passe dessous,
  un bandeau orange #FFA500 apparaît — « Ce plat est passé sous votre seuil » —
  avec deux boutons, « Valider l'ajustement » et « Ignorer ». Cliquer Valider
  affiche seulement le message « Dans le vrai FoodEatUp, c'est ici que vous
  validez. Rien ne bouge sans vous. » ;
- accessibilité : le curseur est utilisable au clavier, et l'état allumé ne repose
  pas uniquement sur la couleur — ajoute une pastille ou un liseré qui change,
  pour que ce soit lisible en niveaux de gris.

Sous le simulateur, une bande « Les 8 boucles en un coup d'œil » : 8 pastilles
cliquables qui ancrent vers les fiches du module, avec le compteur d'outils MCP
de chaque boucle — 39, 21, 11, 16, 39, 15, 19, 17 — et le total « 177 outils MCP
au standard Model Context Protocol ». Ces compteurs sont recomptés sur le serveur
MCP, ne les arrondis pas et n'en invente aucun.

Et un encadré « La loi des boucles », trois règles, sans fioriture :
1. Une boucle se referme : son dernier maillon nourrit son premier.
2. Une boucle nourrit une autre boucle : aucune n'est autonome.
3. Huit logiciels qui tiennent chacun une boucle ne font pas huit boucles
   connectées, ils font huit tunnels.

INTERDITS : aucune donnée d'établissement réelle, aucun appel API, aucun
localStorage, aucune couleur hors palette, et aucun chiffre présenté comme un
résultat client réel — le simulateur est explicitement étiqueté « démonstration ».

CRITÈRES D'ACCEPTATION
- bouger le curseur change les trois chiffres de la carte « Votre burger » et
  déclenche l'allumage séquentiel, visible à l'œil nu ;
- monter le prix du bœuf assez haut fait apparaître le bandeau orange ;
- la page reste utilisable de 360 px à 1440 px ;
- aucune requête réseau émise par le composant.
```

---

## Prompt C — le maillage

À passer une fois le module en ligne.

```text
Relie le module les-8-boucles au reste de l'Academy, sans dupliquer de contenu.

1. Sur chaque page de module produit concerné, ajoute un encart « Où ça se situe
   dans le système » qui renvoie vers la fiche de boucle correspondante :
     configuration      → boucle-01-configuration-boutique
     equipe-planning    → boucle-02-equipe
     stockvision-ai     → boucle-03-stockvision
     haccp              → boucle-04-haccp
     site-web-vitrine   → boucle-05-ecommerce
     service-commande   → boucle-05-ecommerce
     marketing-fidelite → boucle-06-communication et boucle-07-fidelite
     comptabilite       → boucle-08-comptabilite
   Ces huit slugs de modules existent déjà : n'en crée aucun.

2. Sur chaque fiche de boucle, ajoute en bas un bloc « Passer à la pratique » qui
   renvoie vers le module produit correspondant : la boucle explique le pourquoi,
   le module montre le comment.

3. Sur la page d'accueil, place la carte « Les 8 Boucles FoodEatUp » en première
   position, avec la mention « Commencez ici ».

4. En fin de page module, ajoute un lien sortant vers
   https://site.foodeatup.com/le-systeme — libellé « La version longue du système,
   sur le site FoodEatUp » — en target _blank avec rel="noopener noreferrer".

CRITÈRE D'ACCEPTATION : depuis n'importe quelle fiche produit concernée, on
atteint la boucle correspondante en un clic, et inversement. Aucun lien mort.
```
