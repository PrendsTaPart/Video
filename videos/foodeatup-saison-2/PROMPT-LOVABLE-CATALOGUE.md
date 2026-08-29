# Prompt Lovable — catalogue « Michael fait son cinéma »

À coller dans Lovable sur le projet **food-series-hub**. Deux parties indépendantes : la partie A
complète la saison, la partie B ajoute l'écran de publication. Les deux s'appuient sur le modèle de
données que le serveur MCP « Social FoodEatUp » lit et écrit déjà — ne pas en inventer un autre.

---

## PARTIE A — Compléter la saison 2 : ajouter EPC25 à EPC30

La série `michael-fait-son-cinema`, saison 2, s'arrête aujourd'hui à **EPC24 « La carte au trésor »**.
La saison en compte **trente**. Ajoute les six épisodes manquants, en respectant à la lettre les
conventions déjà en place sur EPC01 → EPC24.

### Ce qu'il faut mettre à jour en plus des épisodes

1. La saison : `episodes` passe de 24 à **30**, `dernierEpisode` de `EPC24` à **`EPC30`**.
2. Le titre YouTube de chaque épisode est de la forme `{titre} — Michael fait son cinéma {n}/24 #Shorts` :
   le dénominateur devient **30** sur les trente épisodes, pas seulement sur les nouveaux.
3. Chaque nouvel épisode démarre au statut **`a_produire`** avec ses **huit pièces** attendues, toutes
   à produire : `master`, `story`, `short`, `paysage`, `facebook`, `tiktok`, `carrousel`, `visuel`.

### Conventions à reprendre telles quelles

- Page de l'épisode : `/series/michael-fait-son-cinema/saison-2/{slugPage}`
- Vignette verticale : `/thumbnails/episodes/{id}-9x16.jpg` · horizontale : `/thumbnails/episodes/{id}-16x9.jpg`
- Poster : la vignette verticale · Visuel Facebook : `/facebook/{id}.jpg`
- Carrousel LinkedIn : `/carrousels/{id}-1.jpg` à `-4.jpg`
- `master` et `story` restent `null` tant que la vidéo n'est pas déposée.
- Dates de diffusion : un épisode par jour, à la suite d'EPC24 (2027-09-05).

### Les six épisodes

```json
[
  {
    "id": "EPC25",
    "titre": "Les traders",
    "slugPage": "epc25-les-traders",
    "datePrevue": "2027-09-06",
    "genre": "Salle des marchés (trois téléphones, panique boursière)",
    "situation": "Le téléphone qui sonne pendant le rush",
    "modules": [
      "Agent vocal"
    ],
    "modulesAffiches": [
      "Agent vocal",
      "Réservations",
      "Commandes",
      "Notifications"
    ],
    "accroche": "Trois téléphones, un dans chaque main, un sur l'épaule : « Allô ? Oui. Allô ? Oui. »",
    "punchline": "« Le téléphone répond. Vous servez. »",
    "resume": "« Le téléphone répond tout seul. L'agent vocal FoodEatUp prend la réservation ou la commande pendant que vous servez. »",
    "hashtags": [
      "FoodEatUp",
      "Restaurant",
      "MichaelFaitSonCinema",
      "Agentvocal"
    ]
  },
  {
    "id": "EPC26",
    "titre": "Le détective",
    "slugPage": "epc26-le-detective",
    "datePrevue": "2027-09-07",
    "genre": "Film noir (noir et blanc, stores vénitiens, voix off intérieure)",
    "situation": "Qui a nettoyé la hotte ?",
    "modules": [
      "Plan de nettoyage",
      "Checklist hygiène"
    ],
    "modulesAffiches": [
      "Plan de nettoyage",
      "Checklist hygiène",
      "HACCP",
      "Employés"
    ],
    "accroche": "Noir et blanc, voix off : « Il était vingt-trois heures. La hotte était sale. »",
    "punchline": "« Qui a nettoyé ? C'est écrit. »",
    "resume": "« Qui, quoi, quand : c'est écrit. Le plan de nettoyage FoodEatUp enregistre chaque action, pas besoin de détective. »",
    "hashtags": [
      "FoodEatUp",
      "Restaurant",
      "MichaelFaitSonCinema",
      "Plandenettoyage",
      "Checklisthygiène"
    ]
  },
  {
    "id": "EPC27",
    "titre": "Le super-vilain",
    "slugPage": "epc27-le-super-vilain",
    "datePrevue": "2027-09-08",
    "genre": "Film de super-vilain (fauteuil tournant, rire, éclair)",
    "situation": "Trois demandes de congé pour le même samedi, déjà signées",
    "modules": [
      "Congés",
      "Planning"
    ],
    "modulesAffiches": [
      "Congés",
      "Planning",
      "Shifts",
      "Employés"
    ],
    "accroche": "Fauteuil qui se retourne lentement, lumière par en dessous : « Samedi. »",
    "punchline": "« Validez sans vous retrouver seul. »",
    "resume": "« Un congé validé, un planning à jour, un samedi couvert. FoodEatUp vous prévient avant que vous signiez. »",
    "hashtags": [
      "FoodEatUp",
      "Restaurant",
      "MichaelFaitSonCinema",
      "Congés",
      "Planning"
    ]
  },
  {
    "id": "EPC28",
    "titre": "Le jeu télé",
    "slugPage": "epc28-le-jeu-tele",
    "datePrevue": "2027-09-09",
    "genre": "Jeu télévisé (animateur, roue, applaudissements)",
    "situation": "La roue cadeaux s'emballe, trente desserts à faire",
    "modules": [
      "Fidélité",
      "Roue cadeaux"
    ],
    "modulesAffiches": [
      "Fidélité",
      "Récompenses",
      "Roue cadeaux",
      "Bons",
      "Stock"
    ],
    "accroche": "Lumières de plateau, un poivrier en guise de micro : « Faites tourner la roue ! »",
    "punchline": "« La roue tourne. Le stock suit. »",
    "resume": "« La roue tourne, les lots sont limités, le stock suit. La fidélité FoodEatUp, c'est du jeu avec des règles. »",
    "hashtags": [
      "FoodEatUp",
      "Restaurant",
      "MichaelFaitSonCinema",
      "Fidélité",
      "Rouecadeaux"
    ]
  },
  {
    "id": "EPC29",
    "titre": "Les gangsters",
    "slugPage": "epc29-les-gangsters",
    "datePrevue": "2027-09-10",
    "genre": "Film de gangsters (lumière tamisée, chuchotements, respect)",
    "situation": "L'habitué qui dit « Mets ça sur ma note » depuis six mois",
    "modules": [
      "Ardoises"
    ],
    "modulesAffiches": [
      "Ardoises",
      "Caisse",
      "Clients",
      "Paiements"
    ],
    "accroche": "Un client en costume se penche : « Mets ça sur ma note. »",
    "punchline": "« L'ardoise ne s'oublie plus. »",
    "resume": "« L'ardoise est numérique : elle ne s'oublie pas, elle ne s'envole pas. Solde, historique, règlement, dans FoodEatUp. »",
    "hashtags": [
      "FoodEatUp",
      "Restaurant",
      "MichaelFaitSonCinema",
      "Ardoises"
    ]
  },
  {
    "id": "EPC30",
    "titre": "La cérémonie",
    "slugPage": "epc30-la-ceremonie",
    "datePrevue": "2027-09-11",
    "genre": "Cérémonie de remise de prix + générique de fin",
    "situation": "Tout le casting de la saison réuni, Michael ouvre l'enveloppe",
    "modules": [
      "FoodEatUp tout entier"
    ],
    "modulesAffiches": [
      "Commandes",
      "Réservations",
      "Plan de salle",
      "Écran cuisine",
      "Caisse",
      "Stock",
      "HACCP",
      "Planning",
      "Fidélité",
      "Campagnes",
      "Avis",
      "Synthèse financière"
    ],
    "accroche": "Tapis rouge dans le restaurant, roulement de tambour : « Et le gagnant… »",
    "punchline": "« Trente films. Un seul système. »",
    "resume": "« Trente films. Un restaurant. Un seul système. FoodEatUp. »",
    "hashtags": [
      "FoodEatUp",
      "Restaurant",
      "MichaelFaitSonCinema",
      "Saison2",
      "Final"
    ]
  }
]
```

### Comment les champs sont utilisés dans les légendes

Reprends exactement la mécanique d'EPC01, ne la réécris pas :

- **Instagram** et **WhatsApp** : `accroche`, ligne vide, `punchline`.
- **LinkedIn** (carrousel) et **Facebook** (visuel) : `accroche`, ligne vide, `situation` — joué comme
  `genre` —, ligne vide, `resume`.
- **TikTok** : `accroche` + 🎬 + `punchline` sur une seule ligne.
- **YouTube** : titre `{titre} — Michael fait son cinéma {n}/30 #Shorts`, puis la légende longue.
- Les `hashtags` fournis se collent en fin de texte, préfixés de `#`.

L'épisode 30 est le final de saison : sa punchline « Trente films. Un seul système. » vaut pour toute
la série, et ses hashtags sont `#Saison2 #Final` plutôt qu'un nom de module, puisqu'il les montre tous.

### Un écart à corriger au passage

La fiche décrit le master comme `9:16 · 1080 × 1920 · 37,5 s`. Les épisodes réellement montés font
**32 s** (10 s de scène 1 + 10 s de scène 2 + 12 s d'outro). Corrige le format annoncé, sinon le
catalogue promet une durée que les fichiers ne tiennent pas.

---

## PARTIE B — L'écran de publication

Aujourd'hui le catalogue sait dire ce qu'il faut produire et fournit le kit de publication, mais la
publication elle-même n'a pas d'écran. Ajoute `/admin/publication`, construit sur le modèle que le
serveur MCP écrit déjà — il ne faut pas un second modèle à côté.

### Le modèle, tel que le MCP l'utilise

Deux niveaux, à ne pas confondre :

**1. L'état d'une pièce** (le fichier)
- `a_produire` → aucune URL.
- `pret` → une URL est renseignée et le fichier répond en 200 avec un content-type vidéo.
  **Écrit par un agent** (outil `publier_video`).
- `valide` → un humain a regardé la pièce en entier. **Geste humain exclusivement** : aucun outil ne
  l'expose, aucun ne doit l'exposer.

**2. Le créneau d'un épisode sur un réseau**
- Réseaux : `facebook`, `instagram`, `tiktok`, `linkedin`, `linkedin_profile`, `youtube`, `whatsapp`.
- Statuts : `a_venir`, `brouillon`, `planifie`, `publie`.
- Champs : `date` (AAAA-MM-JJ), `heure` (HH:MM), `url_post` (le lien du post réellement publié).
- **Règle non négociable** : `planifie` et `publie` sont refusés tant que la pièce n'est pas `valide`.
  L'écran doit refuser de la même manière que les outils, avec le même message.

### Ce que l'écran doit permettre

1. **Une grille épisode × réseau** sur la saison, filtrable par série et par saison, chaque case
   montrant le statut, la date, l'heure et le lien du post s'il existe.
2. **Le geste de validation**, et lui seul réservé à l'humain : sur une pièce `pret`, un bouton qui la
   passe à `valide`, avec le lecteur vidéo à côté et une case à cocher « je l'ai regardée en entier ».
   Journalise qui a validé et quand. Ce bouton n'existe pas pour une pièce `a_produire`.
3. **La planification** : sur une pièce `valide`, choisir date, heure et réseaux, puis passer les
   créneaux à `planifie`. Proposer par défaut la `datePrevue` de l'épisode.
4. **Le report du lien** : une fois le post parti, coller son URL et passer le créneau à `publie`.
5. **La file d'attente** : les prochains épisodes programmés, dans l'ordre de diffusion, avec leur
   vignette — la même liste que celle servie aux agents, pas une variante.
6. **Le kit à côté de chaque case** : légende, hashtags, appel à l'action et médias du réseau
   concerné, avec un bouton « copier le texte à coller ».

### Ce que l'écran doit rendre visible

- Les pièces **manquantes** par épisode : chaque épisode attend huit pièces, la plupart n'existent pas
  encore. Aujourd'hui seuls les `master` d'EPC01 à EPC04 sont `pret`.
- La raison quand une case est bloquée : « la pièce n'est pas validée », « le master n'est pas déposé »,
  « les quatre planches ne sont pas écrites » — le catalogue sait déjà produire ces phrases, réutilise-les.

### Ce qu'il ne faut pas faire

- Ne pas publier réellement sur les réseaux depuis cet écran : il enregistre des créneaux et des liens,
  la publication passe par RapidoCMS.
- Ne pas exposer `valide` à une API, un webhook ou une automatisation. C'est le seul verrou humain de
  la chaîne ; s'il tombe, une vidéo peut partir sans que personne l'ait vue.
