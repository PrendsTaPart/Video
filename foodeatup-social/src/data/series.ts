// FoodEatUp Social — données de la grille.
//
// Fichier GÉNÉRÉ par l'usine à vidéos (foodeatup-video-factory) :
//   python3 scripts/gen-publications.py
// Ne pas éditer à la main, la prochaine régénération écraserait la correction.

export type Statut = "publie" | "monte" | "a_produire" | "bloque";
export type StatutReseau = "publie" | "planifie" | "brouillon" | "a_venir";
export type Reseau = "facebook" | "instagram" | "tiktok" | "linkedin" | "youtube";

/** L'identité d'un post. Son TEXTE vit dans data/contenu.ts, chargé à la demande. */
export type Publication = {
  statut: StatutReseau;
  date: string | null;
  heure: string;
  compte: string;
  format: string;
  /** Le texte à coller, sans les mots-dièse. Sur YouTube, c'est la description. */
  /** null sur Instagram et TikTok : ils ne rendent pas les liens cliquables. */
  lienCta: string | null;
  url?: string;
};

/** La fiche de l'Academy qui correspond à l'épisode. */
export type Tutoriel = {
  titre: string;
  slug: string;
  url: string;
  module: string;
  etape: string | null;
  /** "numéro" = le numéro de chapitre a désigné la fiche ; "texte" = rapprochement. */
  correspondance: "numéro" | "texte";
  confiance: number;
};

export type Episode = {
  id: string;
  numero: number;
  saison: number;
  slug: string;
  titre: string;
  module: string;
  chapitre: string;
  accroche: string;
  punchline: string;
  resume: string;
  statut: Statut;
  blocage?: string;
  dureeSecondes: number | null;
  videoUrl: string | null;
  /** La fiche publique de l'Academy. null si elle n'existe pas encore. */
  tutoriel: Tutoriel | null;
  /** La page du module dans l'Academy — le repli quand la fiche manque. */
  tutorielModuleUrl: string | null;
  tutorielManquant?: string;
  /** Le plan Higgsfield d'origine : le prompt et le clip source. */
  higgsfield: {
    videoSourceUrl: string | null;
    /** "rapidocms" = versé en bibliothèque ; "depot" = servi depuis le dépôt. */
    source: "rapidocms" | "depot" | null;
    duree: string;
    format: string;
  };
  /** Le master hébergé dans la bibliothèque RapidoCMS. */
  masterRapidoUrl: string | null;
  posterUrl: string | null;
  troisMots: string;
  datePrevue: string | null;
  reseaux: Record<Reseau, Publication>;
};

export type Saison = { numero: number; titre: string; pitch: string; episodes: Episode[] };

export type Serie = {
  slug: string; nom: string; pitch: string; format: string;
  statut: "en-cours" | "terminee" | "a-venir";
  premiereDiffusion: string;
  saisons: Saison[];
};

export type ReseauInfo = { slug: Reseau; nom: string; compte: string; url: string; couleur: string };

export const marque = {
  "nom": "FoodEatUp Social",
  "baseline": "Toutes nos vidéos sociales, saison après saison.",
  "site": "foodeatup.com",
  "telephone": "06 14 18 92 25",
  "whatsapp": "https://wa.me/33614189225"
};

export const reseaux: ReseauInfo[] = [
  {
    "slug": "facebook",
    "nom": "Facebook",
    "compte": "FoodEatUp",
    "url": "https://www.facebook.com/profile.php?id=201499969703551",
    "couleur": "#1877F2"
  },
  {
    "slug": "instagram",
    "nom": "Instagram",
    "compte": "foodeatup.cocuisinage",
    "url": "https://www.instagram.com/foodeatup.cocuisinage/",
    "couleur": "#E1306C"
  },
  {
    "slug": "tiktok",
    "nom": "TikTok",
    "compte": "foodeatup",
    "url": "https://www.tiktok.com/@foodeatup",
    "couleur": "#000000"
  },
  {
    "slug": "linkedin",
    "nom": "LinkedIn",
    "compte": "FoodEatUp",
    "url": "https://www.linkedin.com/company/foodeatup/",
    "couleur": "#0A66C2"
  },
  {
    "slug": "youtube",
    "nom": "YouTube",
    "compte": "@FoodEatUp",
    "url": "https://www.youtube.com/@FoodEatUp",
    "couleur": "#FF0000"
  }
];

export const calendrier = {
  "depart": "2026-08-11",
  "cadence": "un épisode par jour",
  "creneaux": [
    {
      "reseau": "linkedin",
      "heure": "08:00"
    },
    {
      "reseau": "facebook",
      "heure": "12:00"
    },
    {
      "reseau": "instagram",
      "heure": "18:30"
    },
    {
      "reseau": "tiktok",
      "heure": "19:00"
    }
  ],
  "note": "Les horaires sont décalés pour qu'un même épisode ne tombe pas quatre fois au même moment sur quatre fils. Les épisodes bloqués ne prennent pas de place dans la grille : ils s'y insèrent quand leur tutoriel existe."
};

export const academy = {
  "site": "https://tutoriel.foodeatup.com",
  "modules": [
    {
      "nom": "Configuration Boutique",
      "url": "https://tutoriel.foodeatup.com/module/configuration"
    },
    {
      "nom": "Équipe, Planning & RH",
      "url": "https://tutoriel.foodeatup.com/module/equipe-planning"
    },
    {
      "nom": "Site Web & Vitrine",
      "url": "https://tutoriel.foodeatup.com/module/site-web-vitrine"
    },
    {
      "nom": "HubRise & Livraisons",
      "url": "https://tutoriel.foodeatup.com/module/hubrise-livraisons"
    },
    {
      "nom": "Agent IA Caroline",
      "url": "https://tutoriel.foodeatup.com/module/caroline-ia"
    },
    {
      "nom": "Réservations & Plan de salle",
      "url": "https://tutoriel.foodeatup.com/module/reservation-salle"
    },
    {
      "nom": "Service Multi-Canal",
      "url": "https://tutoriel.foodeatup.com/module/service-commande"
    },
    {
      "nom": "Écran Cuisine (KDS)",
      "url": "https://tutoriel.foodeatup.com/module/kds-cuisine"
    },
    {
      "nom": "Marketing, Fidélité & Iris",
      "url": "https://tutoriel.foodeatup.com/module/marketing-fidelite"
    },
    {
      "nom": "StockVision AI",
      "url": "https://tutoriel.foodeatup.com/module/stockvision-ai"
    },
    {
      "nom": "Hygiène & HACCP",
      "url": "https://tutoriel.foodeatup.com/module/haccp"
    },
    {
      "nom": "Comptabilité & Achats",
      "url": "https://tutoriel.foodeatup.com/module/comptabilite"
    },
    {
      "nom": "PrediBot (Agent IA Directeur)",
      "url": "https://tutoriel.foodeatup.com/module/predibot"
    }
  ],
  "note": "149 vidéos en ligne sur 158 fiches, 13 modules. Le module Caisse POS n'y figure pas."
};

export const outils = {
  "higgsfield": {
    "nom": "Higgsfield",
    "role": "Génère le plan humoristique de dix secondes à partir du prompt.",
    "url": "https://higgsfield.ai/",
    "logo": "/brand/outils/higgsfield.png"
  },
  "claude": {
    "nom": "Claude Code",
    "role": "Monte l'épisode : recadrage, incrustations, mixage, contrôle qualité. Aucun rendu payant.",
    "url": "https://claude.ai/code",
    "logo": "/brand/outils/claude.png"
  },
  "rapidocms": {
    "nom": "RapidoCMS",
    "role": "Héberge les vidéos et publie sur Facebook, Instagram, LinkedIn, TikTok et YouTube depuis une conversation.",
    "url": "https://cms.rapidosoftware.com",
    "connexion": "https://cms.rapidosoftware.com/login",
    "inscription": "https://cms.rapidosoftware.com/register",
    "mcp": "https://cms.rapidosoftware.com/mcp",
    "logo": "/brand/outils/rapidocms.png"
  }
};

export const chefReference = "/brand/chef-foodeatup.jpg";

export const series: Serie[] = [
  {
    "slug": "le-coup-de-feu",
    "nom": "Le Coup de Feu",
    "pitch": "Trente secondes : une scène de restaurant qui part en vrille, puis la fonctionnalité FoodEatUp qui l'aurait évitée.",
    "format": "Vertical 1080×1920 · 37,5 s · 1 épisode par jour",
    "statut": "en-cours",
    "premiereDiffusion": "2026-08-11",
    "saisons": [
      {
        "numero": 1,
        "titre": "Le service, sans les cris",
        "pitch": "Salle, cuisine, commandes : ce qui se joue pendant le coup de feu.",
        "episodes": [
          {
            "id": "EP001",
            "numero": 1,
            "saison": 1,
            "slug": "ep001-le-chien-qui-te-regarde",
            "titre": "Le chien qui te regarde",
            "module": "Service",
            "chapitre": "1 - Commandes multi-canaux",
            "accroche": "Lui aussi attend ta commande.",
            "punchline": "Sauf que lui, il est patient. Tes clients, non.",
            "resume": "Ici, toutes tes commandes arrivent au même endroit : la salle, le téléphone, le site, la livraison. Une seule file, dans l'ordre d'arrivée. Plus personne n'attend parce qu'on a oublié un ticket.",
            "statut": "monte",
            "dureeSecondes": 37.5,
            "videoUrl": "https://raw.githubusercontent.com/PrendsTaPart/Video/claude/foodeatup-video-factory-wtb7gs/foodeatup-video-factory/dist/tiktok/EP001.mp4",
            "reseaux": {
              "facebook": {
                "statut": "planifie",
                "date": "2026-08-11",
                "heure": "12:00",
                "compte": "FoodEatUp",
                "format": "Vidéo native 9:16",
                "lienCta": "https://site.foodeatup.com/"
              },
              "instagram": {
                "statut": "a_venir",
                "date": "2026-08-11",
                "heure": "18:30",
                "compte": "foodeatup.cocuisinage",
                "format": "Reel 9:16",
                "lienCta": null
              },
              "tiktok": {
                "statut": "a_venir",
                "date": "2026-08-11",
                "heure": "19:00",
                "compte": "foodeatup",
                "format": "Vidéo 9:16",
                "lienCta": null
              },
              "linkedin": {
                "statut": "a_venir",
                "date": "2026-08-11",
                "heure": "08:00",
                "compte": "FoodEatUp",
                "format": "Vidéo native 9:16",
                "lienCta": "https://site.foodeatup.com/"
              },
              "youtube": {
                "statut": "a_venir",
                "date": "2026-08-11",
                "heure": "10:00",
                "compte": "@FoodEatUp",
                "format": "Short 9:16",
                "lienCta": "https://site.foodeatup.com/"
              }
            },
            "posterUrl": "/posters/EP001.jpg",
            "datePrevue": "2026-08-11",
            "troisMots": "COMMANDES MULTI-CANAUX",
            "tutoriel": {
              "titre": "Mes commandes : QR code, site web, agent vocal (toutes vos commandes)",
              "slug": "mes-commandes-tous-canaux",
              "url": "https://tutoriel.foodeatup.com/tutoriel/mes-commandes-tous-canaux",
              "module": "Service Multi-Canal",
              "etape": "Recevoir ses commandes\n- **Statut** : En ligne (1 min 09 s)\n- **Vidéo** : https://rapido-software.s3.eu-west-3.amazonaws.com/rapidosoftware/cms/bibliotheque/foodeatup-mes-commandes-tuto-v1\n\n**Description (à quoi ça sert)**\n\nCentraliser toutes vos commandes — QR code table, site vitrine, agent vocal ou saisie manuelle — dans une seule liste, avec canal, statut et total visibles d'un coup d'œil. Créez, modifiez ou supprimez une commande sans changer d'écran.\n\n**Comment ça marche**\n\n1. Ouvrez \"Mes commandes\" : la liste complète, avec le canal (Manuel, Vitrine, Sur place...), le statut et le total de chaque commande\n2. Cliquez sur \"+ Nouvelle commande\" pour en créer une manuellement\n3. Renseignez le client, le canal, le mode de service, puis ajoutez vos plats\n4. Cliquez sur \"Créer la commande\" : la facture et le devis sont générés automatiquement\n5. Cliquez sur une commande pour voir son détail, ou sur \"Modifier\" pour ajuster les articles et le statut, puis \"Mettre à jour\"\n6. Pour la retirer : menu \"⋮\" > \"Supprimer\", puis confirmez\n\n**Astuce du chef** : Le canal affiché sur chaque ligne (Manuel, Vitrine, Sur place...) vous dit immédiatement d'où vient la commande sans avoir à l'ouvrir — utile en coup de feu pour prioriser. Et avant de supprimer une commande, vérifiez sa facture/devis liés (visibles dans le détail) : une commande facturée qui disparaît laisse la facture orpheline, mieux vaut parfois la passer en \"Annulée\" plutôt que la supprimer.\n\n---",
              "correspondance": "numéro",
              "confiance": 1.0
            },
            "tutorielModuleUrl": "https://tutoriel.foodeatup.com/module/service-commande",
            "higgsfield": {
              "videoSourceUrl": "https://rapido-software.s3.eu-west-3.amazonaws.com/rapidosoftware/cms/bibliotheque/Higgsfield-source-EP001-Le-chien-qui-te-regarde",
              "duree": "10 s",
              "format": "vertical 9:16",
              "source": "rapidocms"
            },
            "masterRapidoUrl": "https://rapido-software.s3.eu-west-3.amazonaws.com/rapidosoftware/cms/bibliotheque/FoodEatUp-EP001-Prendre-une-commande"
          },
          {
            "id": "EP002",
            "numero": 2,
            "saison": 1,
            "slug": "ep002-la-chute-en-skateboard",
            "titre": "La chute en skateboard",
            "module": "Service",
            "chapitre": "3 - Envoi direct cuisine",
            "accroche": "Ton service du samedi soir.",
            "punchline": "Ça finit toujours par terre.",
            "resume": "Tu prends la commande à table, elle part en cuisine dans la seconde. Pas de carnet, pas d'aller-retour, pas de ticket perdu entre la salle et le pass.",
            "statut": "monte",
            "dureeSecondes": 37.5,
            "videoUrl": "https://raw.githubusercontent.com/PrendsTaPart/Video/claude/foodeatup-video-factory-wtb7gs/foodeatup-video-factory/dist/tiktok/EP002.mp4",
            "reseaux": {
              "facebook": {
                "statut": "planifie",
                "date": "2026-08-12",
                "heure": "12:00",
                "compte": "FoodEatUp",
                "format": "Vidéo native 9:16",
                "lienCta": "https://site.foodeatup.com/"
              },
              "instagram": {
                "statut": "a_venir",
                "date": "2026-08-12",
                "heure": "18:30",
                "compte": "foodeatup.cocuisinage",
                "format": "Reel 9:16",
                "lienCta": null
              },
              "tiktok": {
                "statut": "a_venir",
                "date": "2026-08-12",
                "heure": "19:00",
                "compte": "foodeatup",
                "format": "Vidéo 9:16",
                "lienCta": null
              },
              "linkedin": {
                "statut": "a_venir",
                "date": "2026-08-12",
                "heure": "08:00",
                "compte": "FoodEatUp",
                "format": "Vidéo native 9:16",
                "lienCta": "https://site.foodeatup.com/"
              },
              "youtube": {
                "statut": "a_venir",
                "date": "2026-08-12",
                "heure": "10:00",
                "compte": "@FoodEatUp",
                "format": "Short 9:16",
                "lienCta": "https://site.foodeatup.com/"
              }
            },
            "posterUrl": "/posters/EP002.jpg",
            "datePrevue": "2026-08-12",
            "troisMots": "ENVOI DIRECT CUISINE",
            "tutoriel": {
              "titre": "Envoyer en cuisine en direct",
              "slug": "envoyer-en-cuisine-en-direct",
              "url": "https://tutoriel.foodeatup.com/tutoriel/envoyer-en-cuisine-en-direct",
              "module": "Service Multi-Canal",
              "etape": "Envoi en cuisine\n- **Statut** : En ligne (0 min 51 s)\n- **Vidéo** : https://rapido-software.s3.eu-west-3.amazonaws.com/rapidosoftware/cms/bibliotheque/foodeatup-envoi-cuisine-tuto-v1\n\n**Description (à quoi ça sert)**\n\nEnvoyez une commande en cuisine en un clic dès qu'elle est confirmée, sans ticket papier ni allers-retours entre la salle et le passe. L'équipe cuisine voit instantanément les plats, les allergènes et le temps écoulé sur son écran KDS, et la salle suit en direct jusqu'au statut Prête.\n\n**Comment ça marche**\n\n1. Ouvrez Commandes pour voir toutes les commandes du jour, tous canaux confondus, avec leur statut\n2. Cliquez sur Confirmer sur la commande à préparer : elle passe aussitôt en préparation et part sur l'écran cuisine (KDS)\n3. Sur le KDS, chaque ticket affiche les plats commandés, les allergènes et le temps écoulé depuis l'envoi\n4. Une fois les plats prêts, cliquez sur Prête pour la commande concernée\n5. Les filtres (À confirmer, Confirmées, En cuisine, Prêtes, Servies) se mettent à jour en temps réel pour toute l'équipe\n\n**Astuce du chef** : Dès qu'une commande est confirmée, elle atterrit sur le bon poste KDS sans que personne n'ait à décrocher un ticket papier ou crier en cuisine — gardez chaque écran filtré par poste (Chaud, Froid, Pass...) pour que chaque section ne voie que ses propres tickets : moins de bruit visuel en plein coup de feu, moins d'erreurs.\n\n---",
              "correspondance": "numéro",
              "confiance": 1.0
            },
            "tutorielModuleUrl": "https://tutoriel.foodeatup.com/module/service-commande",
            "higgsfield": {
              "videoSourceUrl": "https://rapido-software.s3.eu-west-3.amazonaws.com/rapidosoftware/cms/bibliotheque/Higgsfield-source-EP002-La-chute-en-skateboard",
              "duree": "10 s",
              "format": "vertical 9:16",
              "source": "rapidocms"
            },
            "masterRapidoUrl": "https://rapido-software.s3.eu-west-3.amazonaws.com/rapidosoftware/cms/bibliotheque/FoodEatUp-EP002-Envoi-direct-cuisine"
          },
          {
            "id": "EP003",
            "numero": 3,
            "saison": 1,
            "slug": "ep003-le-plat-dans-la-piscine",
            "titre": "Le plat dans la piscine",
            "module": "StockVision",
            "chapitre": "1 - Ma carte",
            "accroche": "Ta marge, en ce moment.",
            "punchline": "Elle coule. On va la repêcher.",
            "resume": "Chaque plat de ta carte a son coût matière calculé depuis tes ingrédients. Tu vois ta marge réelle, plat par plat, avant même de fixer ton prix.",
            "statut": "monte",
            "dureeSecondes": 37.5,
            "videoUrl": "https://raw.githubusercontent.com/PrendsTaPart/Video/claude/foodeatup-video-factory-wtb7gs/foodeatup-video-factory/dist/tiktok/EP003.mp4",
            "reseaux": {
              "facebook": {
                "statut": "planifie",
                "date": "2026-08-13",
                "heure": "12:00",
                "compte": "FoodEatUp",
                "format": "Vidéo native 9:16",
                "lienCta": "https://site.foodeatup.com/"
              },
              "instagram": {
                "statut": "a_venir",
                "date": "2026-08-13",
                "heure": "18:30",
                "compte": "foodeatup.cocuisinage",
                "format": "Reel 9:16",
                "lienCta": null
              },
              "tiktok": {
                "statut": "a_venir",
                "date": "2026-08-13",
                "heure": "19:00",
                "compte": "foodeatup",
                "format": "Vidéo 9:16",
                "lienCta": null
              },
              "linkedin": {
                "statut": "a_venir",
                "date": "2026-08-13",
                "heure": "08:00",
                "compte": "FoodEatUp",
                "format": "Vidéo native 9:16",
                "lienCta": "https://site.foodeatup.com/"
              },
              "youtube": {
                "statut": "a_venir",
                "date": "2026-08-13",
                "heure": "10:00",
                "compte": "@FoodEatUp",
                "format": "Short 9:16",
                "lienCta": "https://site.foodeatup.com/"
              }
            },
            "posterUrl": "/posters/EP003.jpg",
            "datePrevue": "2026-08-13",
            "troisMots": "MA CARTE",
            "tutoriel": null,
            "tutorielModuleUrl": "https://tutoriel.foodeatup.com/module/stockvision-ai",
            "tutorielManquant": "Ce chapitre n'a pas encore sa fiche dans l'Academy.",
            "higgsfield": {
              "videoSourceUrl": "https://rapido-software.s3.eu-west-3.amazonaws.com/rapidosoftware/cms/bibliotheque/Higgsfield-source-EP003-Le-plat-dans-la-piscine",
              "duree": "10 s",
              "format": "vertical 9:16",
              "source": "rapidocms"
            },
            "masterRapidoUrl": "https://rapido-software.s3.eu-west-3.amazonaws.com/rapidosoftware/cms/bibliotheque/FoodEatUp-EP003-Ma-carte"
          },
          {
            "id": "EP004",
            "numero": 4,
            "saison": 1,
            "slug": "ep004-le-chat-sur-la-caisse",
            "titre": "Le chat sur la caisse",
            "module": "Caisse POS",
            "chapitre": "1 - Configurer sa caisse",
            "accroche": "Ton nouveau responsable de caisse.",
            "punchline": "Il gère mieux que ton logiciel actuel.",
            "resume": "Ta caisse se configure en quelques minutes : TPE, ticket, moyens de paiement. Elle est reliée à ta carte et à ta cuisine, pas posée à côté.",
            "statut": "bloque",
            "dureeSecondes": null,
            "videoUrl": null,
            "reseaux": {
              "facebook": {
                "statut": "a_venir",
                "date": null,
                "heure": "12:00",
                "compte": "FoodEatUp",
                "format": "Vidéo native 9:16",
                "lienCta": "https://site.foodeatup.com/"
              },
              "instagram": {
                "statut": "a_venir",
                "date": null,
                "heure": "18:30",
                "compte": "foodeatup.cocuisinage",
                "format": "Reel 9:16",
                "lienCta": null
              },
              "tiktok": {
                "statut": "a_venir",
                "date": null,
                "heure": "19:00",
                "compte": "foodeatup",
                "format": "Vidéo 9:16",
                "lienCta": null
              },
              "linkedin": {
                "statut": "a_venir",
                "date": null,
                "heure": "08:00",
                "compte": "FoodEatUp",
                "format": "Vidéo native 9:16",
                "lienCta": "https://site.foodeatup.com/"
              },
              "youtube": {
                "statut": "a_venir",
                "date": null,
                "heure": "10:00",
                "compte": "@FoodEatUp",
                "format": "Short 9:16",
                "lienCta": "https://site.foodeatup.com/"
              }
            },
            "blocage": "Le chapitre correspondant n'a pas encore de vidéo dans le Drive interne.",
            "posterUrl": null,
            "datePrevue": null,
            "troisMots": "CONFIGURER SA CAISSE",
            "tutoriel": null,
            "tutorielModuleUrl": null,
            "tutorielManquant": "Le module Caisse POS n'existe pas encore dans l'Academy.",
            "higgsfield": {
              "videoSourceUrl": "https://rapido-software.s3.eu-west-3.amazonaws.com/rapidosoftware/cms/bibliotheque/Higgsfield-source-EP004-Le-chat-sur-la-caisse",
              "duree": "10 s",
              "format": "vertical 9:16",
              "source": "rapidocms"
            },
            "masterRapidoUrl": null
          },
          {
            "id": "EP005",
            "numero": 5,
            "saison": 1,
            "slug": "ep005-le-serveur-qui-glisse",
            "titre": "Le serveur qui glisse",
            "module": "Configuration",
            "chapitre": "vue d'ensemble",
            "accroche": "Trois logiciels. Deux mains.",
            "punchline": "Un seul outil, ça change tout.",
            "resume": "Un seul paramétrage : ta carte, tes zones, tes tables, ta TVA. Tout le reste s'appuie dessus. Tu ne ressaisis jamais deux fois la même information.",
            "statut": "monte",
            "dureeSecondes": 37.5,
            "videoUrl": "https://raw.githubusercontent.com/PrendsTaPart/Video/claude/foodeatup-video-factory-wtb7gs/foodeatup-video-factory/dist/tiktok/EP005.mp4",
            "reseaux": {
              "facebook": {
                "statut": "planifie",
                "date": "2026-08-14",
                "heure": "12:00",
                "compte": "FoodEatUp",
                "format": "Vidéo native 9:16",
                "lienCta": "https://site.foodeatup.com/"
              },
              "instagram": {
                "statut": "a_venir",
                "date": "2026-08-14",
                "heure": "18:30",
                "compte": "foodeatup.cocuisinage",
                "format": "Reel 9:16",
                "lienCta": null
              },
              "tiktok": {
                "statut": "a_venir",
                "date": "2026-08-14",
                "heure": "19:00",
                "compte": "foodeatup",
                "format": "Vidéo 9:16",
                "lienCta": null
              },
              "linkedin": {
                "statut": "a_venir",
                "date": "2026-08-14",
                "heure": "08:00",
                "compte": "FoodEatUp",
                "format": "Vidéo native 9:16",
                "lienCta": "https://site.foodeatup.com/"
              },
              "youtube": {
                "statut": "a_venir",
                "date": "2026-08-14",
                "heure": "10:00",
                "compte": "@FoodEatUp",
                "format": "Short 9:16",
                "lienCta": "https://site.foodeatup.com/"
              }
            },
            "posterUrl": "/posters/EP005.jpg",
            "datePrevue": "2026-08-14",
            "troisMots": "VUE D'ENSEMBLE",
            "tutoriel": null,
            "tutorielModuleUrl": "https://tutoriel.foodeatup.com/module/configuration",
            "tutorielManquant": "Ce chapitre n'a pas encore sa fiche dans l'Academy.",
            "higgsfield": {
              "videoSourceUrl": "https://rapido-software.s3.eu-west-3.amazonaws.com/rapidosoftware/cms/bibliotheque/Higgsfield-source-EP005-Le-serveur-qui-glisse",
              "duree": "10 s",
              "format": "vertical 9:16",
              "source": "rapidocms"
            },
            "masterRapidoUrl": "https://rapido-software.s3.eu-west-3.amazonaws.com/rapidosoftware/cms/bibliotheque/FoodEatUp-EP005-Vue-d-ensemble"
          },
          {
            "id": "EP006",
            "numero": 6,
            "saison": 1,
            "slug": "ep006-la-pizza-frisbee",
            "titre": "La pizza frisbee",
            "module": "StockVision",
            "chapitre": "17 - Ajouter et modifier un mouvement",
            "accroche": "Ta pizza part plus vite que ton stock.",
            "punchline": "Enfin… c'était avant.",
            "resume": "Tu envoies un plat, le stock bouge tout seul. Chaque sortie est tracée, avec la quantité et l'heure. Tu sais ce qu'il te reste sans compter les cartons.",
            "statut": "monte",
            "dureeSecondes": 37.5,
            "videoUrl": "https://raw.githubusercontent.com/PrendsTaPart/Video/claude/foodeatup-video-factory-wtb7gs/foodeatup-video-factory/dist/tiktok/EP006.mp4",
            "reseaux": {
              "facebook": {
                "statut": "planifie",
                "date": "2026-08-15",
                "heure": "12:00",
                "compte": "FoodEatUp",
                "format": "Vidéo native 9:16",
                "lienCta": "https://site.foodeatup.com/"
              },
              "instagram": {
                "statut": "a_venir",
                "date": "2026-08-15",
                "heure": "18:30",
                "compte": "foodeatup.cocuisinage",
                "format": "Reel 9:16",
                "lienCta": null
              },
              "tiktok": {
                "statut": "a_venir",
                "date": "2026-08-15",
                "heure": "19:00",
                "compte": "foodeatup",
                "format": "Vidéo 9:16",
                "lienCta": null
              },
              "linkedin": {
                "statut": "a_venir",
                "date": "2026-08-15",
                "heure": "08:00",
                "compte": "FoodEatUp",
                "format": "Vidéo native 9:16",
                "lienCta": "https://site.foodeatup.com/"
              },
              "youtube": {
                "statut": "a_venir",
                "date": "2026-08-15",
                "heure": "10:00",
                "compte": "@FoodEatUp",
                "format": "Short 9:16",
                "lienCta": "https://site.foodeatup.com/"
              }
            },
            "posterUrl": "/posters/EP006.jpg",
            "datePrevue": "2026-08-15",
            "troisMots": "AJOUTER MODIFIER MOUVEMENT",
            "tutoriel": {
              "titre": "Saisir un mouvement de stock FoodEatUp",
              "slug": "saisir-un-mouvement-de-stock",
              "url": "https://tutoriel.foodeatup.com/tutoriel/saisir-un-mouvement-de-stock",
              "module": "StockVision AI",
              "etape": "Stock\n- **Statut** : En ligne (0 min 52 s)\n- **Vidéo** : https://rapido-software.s3.eu-west-3.amazonaws.com/rapidosoftware/cms/bibliotheque/foodeatup-mouvement-stock-tuto-v1\n\n**Description (à quoi ça sert)**\n\nTracer chaque entrée et chaque sortie de votre cuisine au moment où elle a lieu, plutôt que de découvrir l'écart à l'inventaire. Chaque mouvement saisi alimente StockVision AI, qui s'appuie dessus pour tenir vos quantités disponibles à jour, déclencher vos seuils d'alerte et alimenter votre liste de courses. Et parce qu'une erreur de frappe arrive, le mouvement reste modifiable après coup sans avoir à le supprimer et à le ressaisir.\n\n**Comment ça marche**\n\n1. Depuis \"Gestion des stocks\", cliquez sur \"Mouvement de stock\" pour ouvrir le registre des mouvements\n2. Cliquez sur \"Ajouter un mouvement\" pour ouvrir le formulaire\n3. Choisissez le produit concerné, puis le type de mouvement : \"Entrée\" pour une réception, \"Sortie\" pour une consommation ou une perte\n4. Saisissez la quantité et son unité (pièce, kg…), le motif du mouvement et le fournisseur\n5. Cliquez sur \"Ajouter\" : le mouvement est enregistré et apparaît aussitôt dans le registre avec sa date et le nom de l'utilisateur\n6. Pour corriger une erreur de saisie, ouvrez le menu \"Action\" (les trois points) de la ligne concernée et cliquez sur \"Modifier\"\n7. Le formulaire se rouvre pré-rempli : ajustez la quantité, validez, et votre stock est recalculé immédiatement\n\n**Astuce du chef** : Modifier vaut mieux que supprimer puis ressaisir. La modification ajuste le stock à partir de la nouvelle valeur en gardant la ligne d'origine dans le registre, avec son auteur et son horodatage : votre historique reste continu et vérifiable. Prenez aussi l'habitude de renseigner le motif à chaque fois (réception commande, perte, casse, inventaire) — c'est ce qui vous permettra plus tard de distinguer une consommation normale d'une démarque, et donc de savoir où part vraiment votre marge.\n\n---",
              "correspondance": "numéro",
              "confiance": 1.0
            },
            "tutorielModuleUrl": "https://tutoriel.foodeatup.com/module/stockvision-ai",
            "higgsfield": {
              "videoSourceUrl": "https://rapido-software.s3.eu-west-3.amazonaws.com/rapidosoftware/cms/bibliotheque/Higgsfield-source-EP006-La-pizza-frisbee",
              "duree": "10 s",
              "format": "vertical 9:16",
              "source": "rapidocms"
            },
            "masterRapidoUrl": "https://rapido-software.s3.eu-west-3.amazonaws.com/rapidosoftware/cms/bibliotheque/FoodEatUp-EP006-Ajouter-modifier-un-mouvement"
          },
          {
            "id": "EP007",
            "numero": 7,
            "saison": 1,
            "slug": "ep007-la-mamie-qui-goute",
            "titre": "La mamie qui goûte",
            "module": "Marketing",
            "chapitre": "3 - Répondre aux avis",
            "accroche": "Le seul avis client qui compte.",
            "punchline": "Les quatre cents autres, on s'en occupe.",
            "resume": "Tes avis Google remontent ici. Tu réponds depuis FoodEatUp, l'IA te propose une réponse dans ton ton, tu valides. Le client voit que tu l'as lu.",
            "statut": "monte",
            "dureeSecondes": 37.5,
            "videoUrl": "https://raw.githubusercontent.com/PrendsTaPart/Video/claude/foodeatup-video-factory-wtb7gs/foodeatup-video-factory/dist/tiktok/EP007.mp4",
            "reseaux": {
              "facebook": {
                "statut": "planifie",
                "date": "2026-08-16",
                "heure": "12:00",
                "compte": "FoodEatUp",
                "format": "Vidéo native 9:16",
                "lienCta": "https://site.foodeatup.com/"
              },
              "instagram": {
                "statut": "a_venir",
                "date": "2026-08-16",
                "heure": "18:30",
                "compte": "foodeatup.cocuisinage",
                "format": "Reel 9:16",
                "lienCta": null
              },
              "tiktok": {
                "statut": "a_venir",
                "date": "2026-08-16",
                "heure": "19:00",
                "compte": "foodeatup",
                "format": "Vidéo 9:16",
                "lienCta": null
              },
              "linkedin": {
                "statut": "a_venir",
                "date": "2026-08-16",
                "heure": "08:00",
                "compte": "FoodEatUp",
                "format": "Vidéo native 9:16",
                "lienCta": "https://site.foodeatup.com/"
              },
              "youtube": {
                "statut": "a_venir",
                "date": "2026-08-16",
                "heure": "10:00",
                "compte": "@FoodEatUp",
                "format": "Short 9:16",
                "lienCta": "https://site.foodeatup.com/"
              }
            },
            "posterUrl": "/posters/EP007.jpg",
            "datePrevue": "2026-08-16",
            "troisMots": "RÉPONDRE AUX AVIS",
            "tutoriel": {
              "titre": "Répondre aux avis clients",
              "slug": "repondre-aux-avis-clients",
              "url": "https://tutoriel.foodeatup.com/tutoriel/repondre-aux-avis-clients",
              "module": "Marketing, Fidélité & Iris",
              "etape": "Avis clients\n- **Statut** : En ligne (0 min 43 s)\n- **Vidéo** : https://rapido-software.s3.eu-west-3.amazonaws.com/rapidosoftware/cms/bibliotheque/foodeatup-repondre-avis-tuto-v1\n\n**Description (à quoi ça sert)**\n\nTransformer chaque avis client en dialogue public : publiez-le, répondez-y en quelques secondes, et rassurez vos futurs clients tout en faisant grimper votre taux de réponse.\n\n**Comment ça marche**\n\n1. Un nouvel avis arrive en attente de modération : cliquez sur Publier pour qu'il apparaisse sur votre site.\n2. Une fois publié, cliquez sur Répondre.\n3. Rédigez votre réponse, ou laissez l'agent vous préparer un brouillon.\n4. Cliquez sur Publier : votre réponse apparaît aussitôt sous l'avis, signée par votre établissement.\n\n**Astuce du chef** : Un avis avec réponse rassure bien plus qu'un avis seul — même une réponse courte (« Merci beaucoup ! ») montre que vous êtes présent et à l'écoute. Utilisez « Brouillon par l'agent » si vous manquez de temps, puis ajustez le ton avant de publier.\n\n---",
              "correspondance": "numéro",
              "confiance": 1.0
            },
            "tutorielModuleUrl": "https://tutoriel.foodeatup.com/module/marketing-fidelite",
            "higgsfield": {
              "videoSourceUrl": "https://rapido-software.s3.eu-west-3.amazonaws.com/rapidosoftware/cms/bibliotheque/Higgsfield-source-EP007-La-mamie-qui-goute",
              "duree": "10 s",
              "format": "vertical 9:16",
              "source": "rapidocms"
            },
            "masterRapidoUrl": "https://rapido-software.s3.eu-west-3.amazonaws.com/rapidosoftware/cms/bibliotheque/FoodEatUp-EP007-Repondre-aux-avis"
          },
          {
            "id": "EP008",
            "numero": 8,
            "saison": 1,
            "slug": "ep008-la-pile-de-tickets",
            "titre": "La pile de tickets",
            "module": "Comptabilité",
            "chapitre": "facturation",
            "accroche": "Fin de mois. Encore.",
            "punchline": "Et si la compta se faisait toute seule ?",
            "resume": "Chaque commande génère sa facture. Tu retrouves le facturé, l'encaissé et les impayés dans le même écran. La fin de mois devient une lecture, pas une reconstitution.",
            "statut": "a_produire",
            "dureeSecondes": null,
            "videoUrl": null,
            "reseaux": {
              "facebook": {
                "statut": "a_venir",
                "date": "2026-08-17",
                "heure": "12:00",
                "compte": "FoodEatUp",
                "format": "Vidéo native 9:16",
                "lienCta": "https://site.foodeatup.com/"
              },
              "instagram": {
                "statut": "a_venir",
                "date": "2026-08-17",
                "heure": "18:30",
                "compte": "foodeatup.cocuisinage",
                "format": "Reel 9:16",
                "lienCta": null
              },
              "tiktok": {
                "statut": "a_venir",
                "date": "2026-08-17",
                "heure": "19:00",
                "compte": "foodeatup",
                "format": "Vidéo 9:16",
                "lienCta": null
              },
              "linkedin": {
                "statut": "a_venir",
                "date": "2026-08-17",
                "heure": "08:00",
                "compte": "FoodEatUp",
                "format": "Vidéo native 9:16",
                "lienCta": "https://site.foodeatup.com/"
              },
              "youtube": {
                "statut": "a_venir",
                "date": "2026-08-17",
                "heure": "10:00",
                "compte": "@FoodEatUp",
                "format": "Short 9:16",
                "lienCta": "https://site.foodeatup.com/"
              }
            },
            "posterUrl": null,
            "datePrevue": "2026-08-17",
            "troisMots": "FACTURATION",
            "tutoriel": {
              "titre": "Créer une facture FoodEatUp",
              "slug": "creer-une-facture",
              "url": "https://tutoriel.foodeatup.com/tutoriel/creer-une-facture",
              "module": "Comptabilité & Achats",
              "etape": "Factures & e-reporting\n- **Statut** : En ligne (0 min 55 s)\n- **Vidéo** : https://rapido-software.s3.eu-west-3.amazonaws.com/rapidosoftware/cms/bibliotheque/creer-une-facture-v1\n\n**Description (à quoi ça sert)**\n\nCréer une facture conforme en quelques clics — client, produits, TVA et remise calculés automatiquement — avec une vérification en temps réel de la conformité Factur-X 2026, pour ne plus jamais rater une mention obligatoire.\n\n**Comment ça marche**\n\n1. Depuis Facturation, retrouvez toutes vos factures et leurs indicateurs (total payées, en attente de paiement, total devis reçu)\n2. Cliquez sur \"Créer une facture\"\n3. Choisissez votre client et complétez son numéro de TVA intracommunautaire si besoin\n4. Recherchez un produit dans votre catalogue, ou créez-le à la volée s'il n'existe pas encore\n5. Fixez la quantité, le prix HT et la TVA de chaque ligne, et appliquez une offre ou une remise si besoin\n6. Renseignez la date de facture et la date d'échéance, puis choisissez le mode de paiement\n7. Cliquez sur \"Enregistrer\" — la facture apparaît aussitôt dans votre liste, prête à télécharger ou à envoyer par e-mail\n\n**Astuce du chef** : La conformité Factur-X n'est pas cosmétique : à partir de 2026, la facturation électronique devient obligatoire pour toutes les entreprises en France. FoodEatUp vérifie votre facture en temps réel (date d'échéance, ligne d'article, TVA) pour vous éviter les mauvaises surprises lors d'un contrôle.\n\n---",
              "correspondance": "texte",
              "confiance": 0.43
            },
            "tutorielModuleUrl": "https://tutoriel.foodeatup.com/module/comptabilite",
            "higgsfield": {
              "videoSourceUrl": null,
              "duree": "10 s",
              "format": "vertical 9:16",
              "source": null
            },
            "masterRapidoUrl": null
          },
          {
            "id": "EP009",
            "numero": 9,
            "saison": 1,
            "slug": "ep009-le-pigeon-voleur",
            "titre": "Le pigeon voleur",
            "module": "Caisse POS",
            "chapitre": "7 - Suivre les écarts de caisse",
            "accroche": "Il y a toujours quelqu'un qui prend ta marge.",
            "punchline": "Ton abonnement logiciel, par exemple.",
            "resume": "À chaque clôture, l'écart entre le théorique et le compté s'affiche. Tu vois quel service dérape et de combien. Ce qui se mesure s'arrête.",
            "statut": "bloque",
            "dureeSecondes": null,
            "videoUrl": null,
            "reseaux": {
              "facebook": {
                "statut": "a_venir",
                "date": null,
                "heure": "12:00",
                "compte": "FoodEatUp",
                "format": "Vidéo native 9:16",
                "lienCta": "https://site.foodeatup.com/"
              },
              "instagram": {
                "statut": "a_venir",
                "date": null,
                "heure": "18:30",
                "compte": "foodeatup.cocuisinage",
                "format": "Reel 9:16",
                "lienCta": null
              },
              "tiktok": {
                "statut": "a_venir",
                "date": null,
                "heure": "19:00",
                "compte": "foodeatup",
                "format": "Vidéo 9:16",
                "lienCta": null
              },
              "linkedin": {
                "statut": "a_venir",
                "date": null,
                "heure": "08:00",
                "compte": "FoodEatUp",
                "format": "Vidéo native 9:16",
                "lienCta": "https://site.foodeatup.com/"
              },
              "youtube": {
                "statut": "a_venir",
                "date": null,
                "heure": "10:00",
                "compte": "@FoodEatUp",
                "format": "Short 9:16",
                "lienCta": "https://site.foodeatup.com/"
              }
            },
            "blocage": "Le chapitre correspondant n'a pas encore de vidéo dans le Drive interne.",
            "posterUrl": null,
            "datePrevue": null,
            "troisMots": "SUIVRE ÉCARTS CAISSE",
            "tutoriel": null,
            "tutorielModuleUrl": null,
            "tutorielManquant": "Le module Caisse POS n'existe pas encore dans l'Academy.",
            "higgsfield": {
              "videoSourceUrl": "https://rapido-software.s3.eu-west-3.amazonaws.com/rapidosoftware/cms/bibliotheque/Higgsfield-source-EP009-Le-pigeon-voleur",
              "duree": "10 s",
              "format": "vertical 9:16",
              "source": "rapidocms"
            },
            "masterRapidoUrl": null
          },
          {
            "id": "EP010",
            "numero": 10,
            "saison": 1,
            "slug": "ep010-le-flambage-rate",
            "titre": "Le flambage raté",
            "module": "PrediBot",
            "chapitre": "1 - Lire ses prévisions",
            "accroche": "Toi, devant ta facture logicielle.",
            "punchline": "Mille euros par mois. Pour dix outils qui ne se parlent pas.",
            "resume": "Un écran, le matin : ton chiffre d'affaires prévu, ta fréquentation, tes points de tension. C'est ton point du jour, sans ouvrir dix onglets.",
            "statut": "monte",
            "dureeSecondes": 37.5,
            "videoUrl": "https://raw.githubusercontent.com/PrendsTaPart/Video/claude/foodeatup-video-factory-wtb7gs/foodeatup-video-factory/dist/tiktok/EP010.mp4",
            "reseaux": {
              "facebook": {
                "statut": "planifie",
                "date": "2026-08-17",
                "heure": "12:00",
                "compte": "FoodEatUp",
                "format": "Vidéo native 9:16",
                "lienCta": "https://site.foodeatup.com/"
              },
              "instagram": {
                "statut": "a_venir",
                "date": "2026-08-18",
                "heure": "18:30",
                "compte": "foodeatup.cocuisinage",
                "format": "Reel 9:16",
                "lienCta": null
              },
              "tiktok": {
                "statut": "a_venir",
                "date": "2026-08-18",
                "heure": "19:00",
                "compte": "foodeatup",
                "format": "Vidéo 9:16",
                "lienCta": null
              },
              "linkedin": {
                "statut": "a_venir",
                "date": "2026-08-18",
                "heure": "08:00",
                "compte": "FoodEatUp",
                "format": "Vidéo native 9:16",
                "lienCta": "https://site.foodeatup.com/"
              },
              "youtube": {
                "statut": "a_venir",
                "date": "2026-08-18",
                "heure": "10:00",
                "compte": "@FoodEatUp",
                "format": "Short 9:16",
                "lienCta": "https://site.foodeatup.com/"
              }
            },
            "posterUrl": "/posters/EP010.jpg",
            "datePrevue": "2026-08-18",
            "troisMots": "LIRE SES PRÉVISIONS",
            "tutoriel": {
              "titre": "Lire ses prévisions PrediBot",
              "slug": "lire-ses-previsions-predibot",
              "url": "https://tutoriel.foodeatup.com/tutoriel/lire-ses-previsions-predibot",
              "module": "PrediBot (Agent IA Directeur)",
              "etape": "Prévisions\n- **Statut** : En ligne (0 min 42 s)\n- **Vidéo** : https://raw.githubusercontent.com/PrendsTaPart/Video/claude/foodeatup-video-tutorials-bivyyp/videos/foodeatup-predibot-previsions-tuto/out/foodeatup-predibot-previsions-tuto-v1.mp4\n\n**Description (à quoi ça sert)**\n\nAnticiper vos besoins en stock, en commandes fournisseurs et en production grâce aux prédictions de l'intelligence artificielle PrediBot, pour éviter les ruptures et ne produire que le nécessaire.\n\n**Comment ça marche**\n\n1. Ouvrez Analyse et prédictions depuis le tableau de bord PrediBot pour voir vos indicateurs clés : alertes actives, économies potentielles, précision de l'IA.\n2. Cliquez sur Prédictions de stock pour visualiser votre consommation face à vos niveaux de stock, avec la recommandation de l'IA.\n3. Consultez Prévisions de commandes : PrediBot vous suggère quoi commander, produit par produit, avant la rupture de stock.\n4. Ouvrez Production recommandée pour voir les plats à préparer et les quantités conseillées, selon l'historique de vos ventes.\n\n**Astuce du chef** : Le pourcentage de précision IA et le niveau de confiance du modèle indiquent la fiabilité de chaque prévision : plus votre historique de ventes est riche, plus PrediBot affine ses recommandations semaine après semaine.\n\n---",
              "correspondance": "numéro",
              "confiance": 1.0
            },
            "tutorielModuleUrl": "https://tutoriel.foodeatup.com/module/predibot",
            "higgsfield": {
              "videoSourceUrl": "https://rapido-software.s3.eu-west-3.amazonaws.com/rapidosoftware/cms/bibliotheque/Higgsfield-source-EP010-Le-flambage-rate",
              "duree": "10 s",
              "format": "vertical 9:16",
              "source": "rapidocms"
            },
            "masterRapidoUrl": "https://rapido-software.s3.eu-west-3.amazonaws.com/rapidosoftware/cms/bibliotheque/FoodEatUp-EP010-Lire-ses-previsions"
          },
          {
            "id": "EP011",
            "numero": 11,
            "saison": 1,
            "slug": "ep011-le-livreur-et-le-dos-d-ane",
            "titre": "Le livreur et le dos d'âne",
            "module": "HubRise",
            "chapitre": "1 - Connecter son HubRise",
            "accroche": "Ta livraison sans intégration.",
            "punchline": "Avec, tout arrive à bon port.",
            "resume": "Tu connectes HubRise une fois. Tes plateformes de livraison envoient leurs commandes directement dans FoodEatUp. Plus de tablette à surveiller dans un coin.",
            "statut": "bloque",
            "dureeSecondes": null,
            "videoUrl": null,
            "reseaux": {
              "facebook": {
                "statut": "a_venir",
                "date": null,
                "heure": "12:00",
                "compte": "FoodEatUp",
                "format": "Vidéo native 9:16",
                "lienCta": "https://site.foodeatup.com/"
              },
              "instagram": {
                "statut": "a_venir",
                "date": null,
                "heure": "18:30",
                "compte": "foodeatup.cocuisinage",
                "format": "Reel 9:16",
                "lienCta": null
              },
              "tiktok": {
                "statut": "a_venir",
                "date": null,
                "heure": "19:00",
                "compte": "foodeatup",
                "format": "Vidéo 9:16",
                "lienCta": null
              },
              "linkedin": {
                "statut": "a_venir",
                "date": null,
                "heure": "08:00",
                "compte": "FoodEatUp",
                "format": "Vidéo native 9:16",
                "lienCta": "https://site.foodeatup.com/"
              },
              "youtube": {
                "statut": "a_venir",
                "date": null,
                "heure": "10:00",
                "compte": "@FoodEatUp",
                "format": "Short 9:16",
                "lienCta": "https://site.foodeatup.com/"
              }
            },
            "blocage": "Le chapitre correspondant n'a pas encore de vidéo dans le Drive interne.",
            "posterUrl": null,
            "datePrevue": null,
            "troisMots": "CONNECTER SON HUBRISE",
            "tutoriel": {
              "titre": "Connecter son HubRise à FoodEatUp",
              "slug": "connecter-son-hubrise",
              "url": "https://tutoriel.foodeatup.com/tutoriel/connecter-son-hubrise",
              "module": "HubRise & Livraisons",
              "etape": "Connecter HubRise\n- **Statut** : Bientôt disponible (tournage en cours)\n\n**Description (à quoi ça sert)**\n\nConnecter son HubRise à FoodEatUp — tutoriel en préparation dans le module HubRise & Livraisons. Il arrive très bientôt dans ce fil conducteur.\n\n**Comment ça marche**\n\n1. Cette vidéo est en cours de tournage dans les cuisines FoodEatUp.\n2. Sa fiche est déjà en place : elle se remplira dès la mise en ligne.\n\n---",
              "correspondance": "numéro",
              "confiance": 1.0
            },
            "tutorielModuleUrl": "https://tutoriel.foodeatup.com/module/hubrise-livraisons",
            "higgsfield": {
              "videoSourceUrl": "https://rapido-software.s3.eu-west-3.amazonaws.com/rapidosoftware/cms/bibliotheque/Higgsfield-source-EP011-Le-livreur-et-le-dos-d-ane",
              "duree": "10 s",
              "format": "vertical 9:16",
              "source": "rapidocms"
            },
            "masterRapidoUrl": null
          },
          {
            "id": "EP012",
            "numero": 12,
            "saison": 1,
            "slug": "ep012-le-client-qui-attend",
            "titre": "Le client qui attend",
            "module": "KDS",
            "chapitre": "3 - Gérer le KDS en direct",
            "accroche": "Temps d'attente : « on regarde ».",
            "punchline": "Avec un KDS, il regarde son plat arriver.",
            "resume": "Le KDS affiche chaque plat, son poste et son temps d'attente. Le client ne regarde plus la cuisine : il regarde son plat arriver.",
            "statut": "bloque",
            "dureeSecondes": null,
            "videoUrl": null,
            "reseaux": {
              "facebook": {
                "statut": "a_venir",
                "date": null,
                "heure": "12:00",
                "compte": "FoodEatUp",
                "format": "Vidéo native 9:16",
                "lienCta": "https://site.foodeatup.com/"
              },
              "instagram": {
                "statut": "a_venir",
                "date": null,
                "heure": "18:30",
                "compte": "foodeatup.cocuisinage",
                "format": "Reel 9:16",
                "lienCta": null
              },
              "tiktok": {
                "statut": "a_venir",
                "date": null,
                "heure": "19:00",
                "compte": "foodeatup",
                "format": "Vidéo 9:16",
                "lienCta": null
              },
              "linkedin": {
                "statut": "a_venir",
                "date": null,
                "heure": "08:00",
                "compte": "FoodEatUp",
                "format": "Vidéo native 9:16",
                "lienCta": "https://site.foodeatup.com/"
              },
              "youtube": {
                "statut": "a_venir",
                "date": null,
                "heure": "10:00",
                "compte": "@FoodEatUp",
                "format": "Short 9:16",
                "lienCta": "https://site.foodeatup.com/"
              }
            },
            "blocage": "Le chapitre correspondant n'a pas encore de vidéo dans le Drive interne.",
            "posterUrl": null,
            "datePrevue": null,
            "troisMots": "GÉRER KDS DIRECT",
            "tutoriel": {
              "titre": "Gérer une commande en direct sur le KDS",
              "slug": "gerer-une-commande-en-direct-kds",
              "url": "https://tutoriel.foodeatup.com/tutoriel/gerer-une-commande-en-direct-kds",
              "module": "Écran Cuisine (KDS)",
              "etape": "Gérer une commande\n- **Statut** : Bientôt disponible (tournage en cours)\n\n**Description (à quoi ça sert)**\n\nGérer une commande en direct sur le KDS — tutoriel en préparation dans le module Écran Cuisine (KDS). Il arrive très bientôt dans ce fil conducteur.\n\n**Comment ça marche**\n\n1. Cette vidéo est en cours de tournage dans les cuisines FoodEatUp.\n2. Sa fiche est déjà en place : elle se remplira dès la mise en ligne.\n\n---",
              "correspondance": "numéro",
              "confiance": 1.0
            },
            "tutorielModuleUrl": "https://tutoriel.foodeatup.com/module/kds-cuisine",
            "higgsfield": {
              "videoSourceUrl": "https://rapido-software.s3.eu-west-3.amazonaws.com/rapidosoftware/cms/bibliotheque/Higgsfield-source-EP012-Le-client-qui-attend",
              "duree": "10 s",
              "format": "vertical 9:16",
              "source": "rapidocms"
            },
            "masterRapidoUrl": null
          },
          {
            "id": "EP013",
            "numero": 13,
            "saison": 1,
            "slug": "ep013-l-avalanche-de-notifications",
            "titre": "L'avalanche de notifications",
            "module": "PrediBot",
            "chapitre": "3 - Parler à PrediBot",
            "accroche": "Dix logiciels. Dix notifications.",
            "punchline": "Un seul, ça suffisait.",
            "resume": "Tu poses ta question en français : combien j'ai fait hier, qu'est-ce qui manque demain. PrediBot lit tes vraies données et te répond. Une seule interface, pas dix.",
            "statut": "monte",
            "dureeSecondes": 37.5,
            "videoUrl": "https://raw.githubusercontent.com/PrendsTaPart/Video/claude/foodeatup-video-factory-wtb7gs/foodeatup-video-factory/dist/tiktok/EP013.mp4",
            "reseaux": {
              "facebook": {
                "statut": "a_venir",
                "date": "2026-08-19",
                "heure": "12:00",
                "compte": "FoodEatUp",
                "format": "Vidéo native 9:16",
                "lienCta": "https://site.foodeatup.com/"
              },
              "instagram": {
                "statut": "a_venir",
                "date": "2026-08-19",
                "heure": "18:30",
                "compte": "foodeatup.cocuisinage",
                "format": "Reel 9:16",
                "lienCta": null
              },
              "tiktok": {
                "statut": "a_venir",
                "date": "2026-08-19",
                "heure": "19:00",
                "compte": "foodeatup",
                "format": "Vidéo 9:16",
                "lienCta": null
              },
              "linkedin": {
                "statut": "a_venir",
                "date": "2026-08-19",
                "heure": "08:00",
                "compte": "FoodEatUp",
                "format": "Vidéo native 9:16",
                "lienCta": "https://site.foodeatup.com/"
              },
              "youtube": {
                "statut": "a_venir",
                "date": "2026-08-19",
                "heure": "10:00",
                "compte": "@FoodEatUp",
                "format": "Short 9:16",
                "lienCta": "https://site.foodeatup.com/"
              }
            },
            "posterUrl": "/posters/EP013.jpg",
            "datePrevue": "2026-08-19",
            "troisMots": "PARLER À PREDIBOT",
            "tutoriel": {
              "titre": "Parler à PrediBot avec nos prompts",
              "slug": "parler-a-predibot-avec-nos-prompts",
              "url": "https://tutoriel.foodeatup.com/tutoriel/parler-a-predibot-avec-nos-prompts",
              "module": "PrediBot (Agent IA Directeur)",
              "etape": "Dialoguer avec PrediBot\n- **Statut** : En ligne (0 min 35 s)\n- **Vidéo** : https://rapido-software.s3.eu-west-3.amazonaws.com/rapidosoftware/cms/bibliotheque/parler-a-predibot-avec-nos-prompts-v1\n\n**Description (à quoi ça sert)**\n\nPiloter toute la gestion RH de votre restaurant — employés, congés, pointages, classement — sans ouvrir un seul écran : il suffit d'écrire la consigne à Predibot, votre agent IA, sur WhatsApp.\n\n**Comment ça marche**\n\n1. Sur WhatsApp, écrivez à Predibot : demandez la liste de vos employés ou celle des congés en attente\n2. Approuvez un congé en une phrase, ou refusez-le en précisant le motif — en quelques secondes\n3. Vérifiez les pointages sur la période de votre choix\n4. Laissez Predibot classer vos employés par performance (heures, retards, congés)\n\n**Astuce du chef** : Chaque réponse de Predibot contient un lien direct vers l'écran FoodEatUp concerné (ex. .../establishment/26/leaves) : cliquez dessus pour vérifier le détail avant de trancher sur un congé sensible.\n\n---",
              "correspondance": "numéro",
              "confiance": 1.0
            },
            "tutorielModuleUrl": "https://tutoriel.foodeatup.com/module/predibot",
            "higgsfield": {
              "videoSourceUrl": "https://rapido-software.s3.eu-west-3.amazonaws.com/rapidosoftware/cms/bibliotheque/Higgsfield-source-EP013-L-avalanche-de-notifications",
              "duree": "10 s",
              "format": "vertical 9:16",
              "source": "rapidocms"
            },
            "masterRapidoUrl": "https://rapido-software.s3.eu-west-3.amazonaws.com/rapidosoftware/cms/bibliotheque/FoodEatUp-EP013-Parler-a-PrediBot"
          },
          {
            "id": "EP014",
            "numero": 14,
            "saison": 1,
            "slug": "ep014-le-raton-laveur",
            "titre": "Le raton laveur",
            "module": "StockVision",
            "chapitre": "16 - Mouvements de stock",
            "accroche": "Ton gaspillage alimentaire.",
            "punchline": "Lui au moins, il sait ce qu'il y a en stock.",
            "resume": "Chaque entrée, chaque sortie, chaque perte est enregistrée. Tu vois ce qui part sans être vendu. Le gaspillage devient une ligne, donc un problème réglable.",
            "statut": "monte",
            "dureeSecondes": 37.5,
            "videoUrl": "https://raw.githubusercontent.com/PrendsTaPart/Video/claude/foodeatup-video-factory-wtb7gs/foodeatup-video-factory/dist/tiktok/EP014.mp4",
            "reseaux": {
              "facebook": {
                "statut": "a_venir",
                "date": "2026-08-20",
                "heure": "12:00",
                "compte": "FoodEatUp",
                "format": "Vidéo native 9:16",
                "lienCta": "https://site.foodeatup.com/"
              },
              "instagram": {
                "statut": "a_venir",
                "date": "2026-08-20",
                "heure": "18:30",
                "compte": "foodeatup.cocuisinage",
                "format": "Reel 9:16",
                "lienCta": null
              },
              "tiktok": {
                "statut": "a_venir",
                "date": "2026-08-20",
                "heure": "19:00",
                "compte": "foodeatup",
                "format": "Vidéo 9:16",
                "lienCta": null
              },
              "linkedin": {
                "statut": "a_venir",
                "date": "2026-08-20",
                "heure": "08:00",
                "compte": "FoodEatUp",
                "format": "Vidéo native 9:16",
                "lienCta": "https://site.foodeatup.com/"
              },
              "youtube": {
                "statut": "a_venir",
                "date": "2026-08-20",
                "heure": "10:00",
                "compte": "@FoodEatUp",
                "format": "Short 9:16",
                "lienCta": "https://site.foodeatup.com/"
              }
            },
            "posterUrl": "/posters/EP014.jpg",
            "datePrevue": "2026-08-20",
            "troisMots": "MOUVEMENTS DE STOCK",
            "tutoriel": {
              "titre": "Lire ses mouvements de stock FoodEatUp",
              "slug": "lire-ses-mouvements-de-stock",
              "url": "https://tutoriel.foodeatup.com/tutoriel/lire-ses-mouvements-de-stock",
              "module": "StockVision AI",
              "etape": "Stock\n- **Statut** : En ligne (0 min 46 s)\n- **Vidéo** : https://rapido-software.s3.eu-west-3.amazonaws.com/rapidosoftware/cms/bibliotheque/foodeatup-mouvements-stock-tuto-v1\n\n**Description (à quoi ça sert)**\n\nDisposer d'un registre lisible de tout ce qui entre et sort de votre cuisine, et pouvoir remonter à la source de n'importe quel écart : qui a saisi quoi, quand, pour quel motif et chez quel fournisseur. C'est la pièce qui rend votre inventaire vérifiable au lieu d'être déclaratif.\n\n**Comment ça marche**\n\n1. Ouvrez \"Gestion des stocks\" puis \"Mouvements de Stock\" : chaque ligne indique le produit, le type (Entrée ou Sortie), la quantité, le motif, le fournisseur, la date et l'utilisateur\n2. Ouvrez le menu \"Action\" (les trois points) au bout de la ligne, puis cliquez sur \"Voir détails\"\n3. Lisez la fiche complète : Informations Générales (produit, type de mouvement, quantité, motif) et Informations Supplémentaires (fournisseur, date et heure exactes, utilisateur qui a fait la saisie)\n4. Pour corriger une erreur de saisie, cliquez sur \"Supprimer\" en haut à droite de la fiche\n5. Confirmez dans la fenêtre : la suppression affecte également le stock, pas seulement la ligne du registre\n6. Le mouvement disparaît du registre et le stock est recalculé en conséquence\n\n**Astuce du chef** : Supprimer un mouvement n'efface pas seulement une ligne d'historique : le stock est recalculé derrière. Si vous supprimez une entrée de 5000 pièces, ces 5000 pièces quittent aussi votre stock. Avant de supprimer, ouvrez toujours la fiche de détail et vérifiez la quantité et le motif — c'est le réflexe qui évite de transformer une erreur de saisie en écart d'inventaire.\n\n---",
              "correspondance": "numéro",
              "confiance": 1.0
            },
            "tutorielModuleUrl": "https://tutoriel.foodeatup.com/module/stockvision-ai",
            "higgsfield": {
              "videoSourceUrl": "https://rapido-software.s3.eu-west-3.amazonaws.com/rapidosoftware/cms/bibliotheque/Higgsfield-source-EP014-Le-raton-laveur",
              "duree": "10 s",
              "format": "vertical 9:16",
              "source": "rapidocms"
            },
            "masterRapidoUrl": "https://rapido-software.s3.eu-west-3.amazonaws.com/rapidosoftware/cms/bibliotheque/FoodEatUp-EP014-Mouvements-de-stock"
          },
          {
            "id": "EP015",
            "numero": 15,
            "saison": 1,
            "slug": "ep015-la-tour-d-assiettes",
            "titre": "La tour d'assiettes",
            "module": "Configuration",
            "chapitre": "référentiels",
            "accroche": "Ta gestion actuelle.",
            "punchline": "Une pièce bouge, tout s'écroule.",
            "resume": "Tes catégories, ta TVA, tes zones, tes équipements : tout est posé une fois, proprement. Quand une pièce bouge, le reste ne s'écroule pas.",
            "statut": "monte",
            "dureeSecondes": 37.5,
            "videoUrl": "https://raw.githubusercontent.com/PrendsTaPart/Video/claude/foodeatup-video-factory-wtb7gs/foodeatup-video-factory/dist/tiktok/EP015.mp4",
            "reseaux": {
              "facebook": {
                "statut": "a_venir",
                "date": "2026-08-21",
                "heure": "12:00",
                "compte": "FoodEatUp",
                "format": "Vidéo native 9:16",
                "lienCta": "https://site.foodeatup.com/"
              },
              "instagram": {
                "statut": "a_venir",
                "date": "2026-08-21",
                "heure": "18:30",
                "compte": "foodeatup.cocuisinage",
                "format": "Reel 9:16",
                "lienCta": null
              },
              "tiktok": {
                "statut": "a_venir",
                "date": "2026-08-21",
                "heure": "19:00",
                "compte": "foodeatup",
                "format": "Vidéo 9:16",
                "lienCta": null
              },
              "linkedin": {
                "statut": "a_venir",
                "date": "2026-08-21",
                "heure": "08:00",
                "compte": "FoodEatUp",
                "format": "Vidéo native 9:16",
                "lienCta": "https://site.foodeatup.com/"
              },
              "youtube": {
                "statut": "a_venir",
                "date": "2026-08-21",
                "heure": "10:00",
                "compte": "@FoodEatUp",
                "format": "Short 9:16",
                "lienCta": "https://site.foodeatup.com/"
              }
            },
            "posterUrl": "/posters/EP015.jpg",
            "datePrevue": "2026-08-21",
            "troisMots": "RÉFÉRENTIELS",
            "tutoriel": {
              "titre": "Régler ses unités de mesure FoodEatUp",
              "slug": "regler-ses-unites",
              "url": "https://tutoriel.foodeatup.com/tutoriel/regler-ses-unites",
              "module": "Configuration Boutique",
              "etape": "Profil, TVA & unités\n- **Statut** : En ligne (0 min 31 s)\n- **Vidéo** : https://rapido-software.s3.eu-west-3.amazonaws.com/rapidosoftware/cms/bibliotheque/foodeatup-unites-tuto-v1\n\n**Description (à quoi ça sert)**\n\nCréer vos propres unités de mesure (gousse, pincée, cuillère...) pour qu'elles soient disponibles ensuite dans vos ingrédients et vos recettes, avec une conversion fiable vers vos unités de base.\n\n**Comment ça marche**\n\n1. Cliquez sur \"Ajouter une unité\"\n2. Donnez-lui un nom et une abréviation\n3. Si besoin, renseignez un facteur de conversion et une unité de base\n4. Cliquez sur \"Créer l'unité\" — elle apparaît aussitôt dans votre liste\n\n**Astuce du chef** : Pensez aux unités de vos recettes autant qu'à celles de votre stock : une « gousse » de vanille ou une « pincée » de sel se retrouveront directement dans vos ingrédients, par exemple « 1 gousse de vanille ».\n\n---",
              "correspondance": "texte",
              "confiance": 0.62
            },
            "tutorielModuleUrl": "https://tutoriel.foodeatup.com/module/configuration",
            "higgsfield": {
              "videoSourceUrl": "https://rapido-software.s3.eu-west-3.amazonaws.com/rapidosoftware/cms/bibliotheque/Higgsfield-source-EP015-La-tour-d-assiettes",
              "duree": "10 s",
              "format": "vertical 9:16",
              "source": "rapidocms"
            },
            "masterRapidoUrl": "https://rapido-software.s3.eu-west-3.amazonaws.com/rapidosoftware/cms/bibliotheque/FoodEatUp-EP015-Referentiels"
          },
          {
            "id": "EP016",
            "numero": 16,
            "saison": 1,
            "slug": "ep016-le-geyser-a-cafe",
            "titre": "Le geyser à café",
            "module": "Comptabilité",
            "chapitre": "dépenses",
            "accroche": "Tes coûts, ce trimestre.",
            "punchline": "On va refermer le robinet.",
            "resume": "Tu enregistres tes achats fournisseurs avec le détail des lignes. Tes dépenses du mois s'additionnent toutes seules, en face de ton chiffre d'affaires.",
            "statut": "monte",
            "dureeSecondes": 37.5,
            "videoUrl": "https://raw.githubusercontent.com/PrendsTaPart/Video/claude/foodeatup-video-factory-wtb7gs/foodeatup-video-factory/dist/tiktok/EP016.mp4",
            "reseaux": {
              "facebook": {
                "statut": "a_venir",
                "date": "2026-08-22",
                "heure": "12:00",
                "compte": "FoodEatUp",
                "format": "Vidéo native 9:16",
                "lienCta": "https://site.foodeatup.com/"
              },
              "instagram": {
                "statut": "a_venir",
                "date": "2026-08-22",
                "heure": "18:30",
                "compte": "foodeatup.cocuisinage",
                "format": "Reel 9:16",
                "lienCta": null
              },
              "tiktok": {
                "statut": "a_venir",
                "date": "2026-08-22",
                "heure": "19:00",
                "compte": "foodeatup",
                "format": "Vidéo 9:16",
                "lienCta": null
              },
              "linkedin": {
                "statut": "a_venir",
                "date": "2026-08-22",
                "heure": "08:00",
                "compte": "FoodEatUp",
                "format": "Vidéo native 9:16",
                "lienCta": "https://site.foodeatup.com/"
              },
              "youtube": {
                "statut": "a_venir",
                "date": "2026-08-22",
                "heure": "10:00",
                "compte": "@FoodEatUp",
                "format": "Short 9:16",
                "lienCta": "https://site.foodeatup.com/"
              }
            },
            "posterUrl": "/posters/EP016.jpg",
            "datePrevue": "2026-08-22",
            "troisMots": "DÉPENSES",
            "tutoriel": {
              "titre": "Saisir ses dépenses fournisseur FoodEatUp",
              "slug": "saisir-ses-depenses-fournisseur",
              "url": "https://tutoriel.foodeatup.com/tutoriel/saisir-ses-depenses-fournisseur",
              "module": "Comptabilité & Achats",
              "etape": "Dépenses & achats\n- **Statut** : En ligne (1 min 00 s)\n- **Vidéo** : https://rapido-software.s3.eu-west-3.amazonaws.com/rapidosoftware/cms/bibliotheque/saisir-ses-depenses-fournisseur-v1\n\n**Description (à quoi ça sert)**\n\nCentraliser tous vos achats fournisseurs — facture jointe, produit, prix, catégorie et statut de paiement — pour garder une comptabilité à jour sans ressaisir les montants à la main.\n\n**Comment ça marche**\n\n1. Depuis l'onglet Dépenses, cliquez sur \"Créer une dépense\"\n2. Renseignez la date d'achat et la référence de la facture fournisseur\n3. Choisissez le fournisseur concerné et joignez directement le fichier de la facture (PDF, JPG, PNG)\n4. Recherchez le produit acheté : son prix se remplit automatiquement depuis votre catalogue\n5. Ajustez la quantité si besoin, la description se complète automatiquement et le total se recalcule en direct\n6. Choisissez une catégorie de dépense et son statut : payée, en attente, ou déclinée\n7. Cliquez sur \"Enregistrer\" — la dépense apparaît aussitôt dans votre liste, avec son montant TTC\n\n**Astuce du chef** : Joindre systématiquement le fichier de la facture à chaque dépense vous évite de fouiller vos mails ou vos classeurs en cas de contrôle : tout reste centralisé et rattaché au bon fournisseur, avec le prix et la catégorie déjà renseignés. Vous pouvez aussi demander directement à Claude d'enregistrer une dépense à votre place, en lui donnant le fournisseur, la référence de facture, le produit et son prix.\n\n---",
              "correspondance": "texte",
              "confiance": 0.41
            },
            "tutorielModuleUrl": "https://tutoriel.foodeatup.com/module/comptabilite",
            "higgsfield": {
              "videoSourceUrl": "https://rapido-software.s3.eu-west-3.amazonaws.com/rapidosoftware/cms/bibliotheque/Higgsfield-source-EP016-Le-geyser-a-cafe",
              "duree": "10 s",
              "format": "vertical 9:16",
              "source": "rapidocms"
            },
            "masterRapidoUrl": "https://rapido-software.s3.eu-west-3.amazonaws.com/rapidosoftware/cms/bibliotheque/FoodEatUp-EP016-Depenses-et-livraisons"
          },
          {
            "id": "EP017",
            "numero": 17,
            "saison": 1,
            "slug": "ep017-le-ninja-de-la-frite",
            "titre": "Le ninja de la frite",
            "module": "StockVision",
            "chapitre": "19 - Création d'un rapport",
            "accroche": "Personne ne touche à ta dernière frite.",
            "punchline": "Ni à ta marge.",
            "resume": "Tu génères ton rapport par module en un clic : ventes, stock, production. L'historique est gardé. Tu compares ce mois-ci avec le mois dernier, pas avec ton souvenir.",
            "statut": "monte",
            "dureeSecondes": 37.5,
            "videoUrl": "https://raw.githubusercontent.com/PrendsTaPart/Video/claude/foodeatup-video-factory-wtb7gs/foodeatup-video-factory/dist/tiktok/EP017.mp4",
            "reseaux": {
              "facebook": {
                "statut": "a_venir",
                "date": "2026-08-23",
                "heure": "12:00",
                "compte": "FoodEatUp",
                "format": "Vidéo native 9:16",
                "lienCta": "https://site.foodeatup.com/"
              },
              "instagram": {
                "statut": "a_venir",
                "date": "2026-08-23",
                "heure": "18:30",
                "compte": "foodeatup.cocuisinage",
                "format": "Reel 9:16",
                "lienCta": null
              },
              "tiktok": {
                "statut": "a_venir",
                "date": "2026-08-23",
                "heure": "19:00",
                "compte": "foodeatup",
                "format": "Vidéo 9:16",
                "lienCta": null
              },
              "linkedin": {
                "statut": "a_venir",
                "date": "2026-08-23",
                "heure": "08:00",
                "compte": "FoodEatUp",
                "format": "Vidéo native 9:16",
                "lienCta": "https://site.foodeatup.com/"
              },
              "youtube": {
                "statut": "a_venir",
                "date": "2026-08-23",
                "heure": "10:00",
                "compte": "@FoodEatUp",
                "format": "Short 9:16",
                "lienCta": "https://site.foodeatup.com/"
              }
            },
            "posterUrl": "/posters/EP017.jpg",
            "datePrevue": "2026-08-23",
            "troisMots": "CRÉATION D'UN RAPPORT",
            "tutoriel": {
              "titre": "Sortir un rapport et son historique FoodEatUp",
              "slug": "sortir-un-rapport-et-son-historique",
              "url": "https://tutoriel.foodeatup.com/tutoriel/sortir-un-rapport-et-son-historique",
              "module": "StockVision AI",
              "etape": "Statistiques & agent IA\n- **Statut** : En ligne (0 min 44 s)\n- **Vidéo** : https://rapido-software.s3.eu-west-3.amazonaws.com/rapidosoftware/cms/bibliotheque/sortir-un-rapport-et-son-historique-v1\n\n**Description (à quoi ça sert)**\n\nSortir en un clic un rapport complet de votre activité — chiffre d'affaires, commandes, marge brute, score HACCP — et remonter dans l'historique de vos sessions de caisse et de vos factures. Utile pour contrôler la caisse en fin de service, préparer la comptabilité mensuelle, comparer deux périodes ou justifier un écart de caisse.\n\n**Comment ça marche**\n\n1. Ouvrez le module Analytix BI depuis le menu principal de FoodEatUp\n2. Choisissez votre période avec le sélecteur de dates\n3. Cliquez sur \"Rapport PDF\" pour générer votre rapport\n4. Consultez le chiffre d'affaires, les commandes, la marge brute et le score HACCP\n5. Faites défiler pour retrouver l'historique de vos sessions de caisse et de vos factures précédentes\n\n**Astuce du chef** : Clôturez votre caisse chaque soir : votre historique reste fiable et les écarts sautent aux yeux dès le lendemain.\n\n---",
              "correspondance": "numéro",
              "confiance": 1.0
            },
            "tutorielModuleUrl": "https://tutoriel.foodeatup.com/module/stockvision-ai",
            "higgsfield": {
              "videoSourceUrl": "https://rapido-software.s3.eu-west-3.amazonaws.com/rapidosoftware/cms/bibliotheque/Higgsfield-source-EP017-Le-ninja-de-la-frite",
              "duree": "10 s",
              "format": "vertical 9:16",
              "source": "rapidocms"
            },
            "masterRapidoUrl": "https://rapido-software.s3.eu-west-3.amazonaws.com/rapidosoftware/cms/bibliotheque/FoodEatUp-EP017-Creation-d-un-rapport"
          },
          {
            "id": "EP018",
            "numero": 18,
            "saison": 1,
            "slug": "ep018-le-serveur-baywatch",
            "titre": "Le serveur Baywatch",
            "module": "Service",
            "chapitre": "2 - Site, vocal et QR code",
            "accroche": "Le rush de vingt heures.",
            "punchline": "Sauve ton service, pas ton dos.",
            "resume": "Pendant le rush, tes clients commandent seuls : par QR à table, par le site, par l'agent vocal. Ton équipe sert, elle ne court plus.",
            "statut": "monte",
            "dureeSecondes": 37.5,
            "videoUrl": "https://raw.githubusercontent.com/PrendsTaPart/Video/claude/foodeatup-video-factory-wtb7gs/foodeatup-video-factory/dist/tiktok/EP018.mp4",
            "reseaux": {
              "facebook": {
                "statut": "a_venir",
                "date": "2026-08-24",
                "heure": "12:00",
                "compte": "FoodEatUp",
                "format": "Vidéo native 9:16",
                "lienCta": "https://site.foodeatup.com/"
              },
              "instagram": {
                "statut": "a_venir",
                "date": "2026-08-24",
                "heure": "18:30",
                "compte": "foodeatup.cocuisinage",
                "format": "Reel 9:16",
                "lienCta": null
              },
              "tiktok": {
                "statut": "a_venir",
                "date": "2026-08-24",
                "heure": "19:00",
                "compte": "foodeatup",
                "format": "Vidéo 9:16",
                "lienCta": null
              },
              "linkedin": {
                "statut": "a_venir",
                "date": "2026-08-24",
                "heure": "08:00",
                "compte": "FoodEatUp",
                "format": "Vidéo native 9:16",
                "lienCta": "https://site.foodeatup.com/"
              },
              "youtube": {
                "statut": "a_venir",
                "date": "2026-08-24",
                "heure": "10:00",
                "compte": "@FoodEatUp",
                "format": "Short 9:16",
                "lienCta": "https://site.foodeatup.com/"
              }
            },
            "posterUrl": "/posters/EP018.jpg",
            "datePrevue": "2026-08-24",
            "troisMots": "SITE",
            "tutoriel": {
              "titre": "Commander sur site & QR ou par agent vocal",
              "slug": "commander-sur-site-qr-ou-vocal",
              "url": "https://tutoriel.foodeatup.com/tutoriel/commander-sur-site-qr-ou-vocal",
              "module": "Service Multi-Canal",
              "etape": "Canaux de commande\n- **Statut** : En ligne (1 min 10 s)\n- **Vidéo** : https://rapido-software.s3.eu-west-3.amazonaws.com/rapidosoftware/cms/bibliotheque/foodeatup-qrcode-commande-tuto-v1\n\n**Description (à quoi ça sert)**\n\nLaisser le client commander et payer depuis son téléphone en scannant le QR code de sa table, sans mobiliser un serveur — de la génération du QR par l'équipe jusqu'au paiement fractionné côté client.\n\n**Comment ça marche**\n\n1. Depuis le plan de salle, sélectionnez une table et cliquez sur \"QR code de la table\"\n2. Le lien s'affiche dans une modale : téléchargez-le ou copiez-le, prêt à imprimer sur la table\n3. Le client scanne le QR et retrouve la carte complète du restaurant, classée par catégories\n4. Il ajoute ses plats d'un clic : le récapitulatif du panier se met à jour en direct\n5. Un clic sur \"Commander\" envoie la commande directement en cuisine (toast de confirmation)\n6. Il suit le statut de chaque plat en temps réel et peut ajouter un nouvel envoi à tout moment\n7. Pour payer : tout régler d'un coup, ou partager l'addition en 2, 3, 4 ou un montant libre, paiement sécurisé Stripe (CB, Apple Pay, Google Pay)\n\n**Astuce du chef** : Imprimez le QR téléchargé directement sur un chevalet de table plutôt que de le régénérer à chaque service — le lien reste valable tant que la table existe. Trois cas d'usage : coup de feu en salle → laissez les clients commander et enchaîner un \"envoi n°2\" sans attendre un serveur libre ; table nombreuse → proposez le partage de l'addition en 3 ou 4 plutôt qu'un calcul de tête au moment de payer ; client pressé → \"Payer l'addition\" clôture directement sans repasser par un serveur pour l'encaissement.\n\n---",
              "correspondance": "numéro",
              "confiance": 1.0
            },
            "tutorielModuleUrl": "https://tutoriel.foodeatup.com/module/service-commande",
            "higgsfield": {
              "videoSourceUrl": "https://rapido-software.s3.eu-west-3.amazonaws.com/rapidosoftware/cms/bibliotheque/Higgsfield-source-EP018-Le-serveur-Baywatch",
              "duree": "10 s",
              "format": "vertical 9:16",
              "source": "rapidocms"
            },
            "masterRapidoUrl": "https://rapido-software.s3.eu-west-3.amazonaws.com/rapidosoftware/cms/bibliotheque/FoodEatUp-EP018-Site-vocal-et-QR-code"
          },
          {
            "id": "EP019",
            "numero": 19,
            "saison": 1,
            "slug": "ep019-le-burger-qui-rebondit",
            "titre": "Le burger qui rebondit",
            "module": "StockVision",
            "chapitre": "3 - Prédictions des commandes",
            "accroche": "Ton chiffre d'affaires, sans outil.",
            "punchline": "Ça rebondit rarement tout seul.",
            "resume": "FoodEatUp regarde tes ventes passées et te dit quoi produire demain. Ton chiffre d'affaires ne dépend plus de ton intuition du lundi matin.",
            "statut": "monte",
            "dureeSecondes": 37.5,
            "videoUrl": "https://raw.githubusercontent.com/PrendsTaPart/Video/claude/foodeatup-video-factory-wtb7gs/foodeatup-video-factory/dist/tiktok/EP019.mp4",
            "reseaux": {
              "facebook": {
                "statut": "a_venir",
                "date": "2026-08-25",
                "heure": "12:00",
                "compte": "FoodEatUp",
                "format": "Vidéo native 9:16",
                "lienCta": "https://site.foodeatup.com/"
              },
              "instagram": {
                "statut": "a_venir",
                "date": "2026-08-25",
                "heure": "18:30",
                "compte": "foodeatup.cocuisinage",
                "format": "Reel 9:16",
                "lienCta": null
              },
              "tiktok": {
                "statut": "a_venir",
                "date": "2026-08-25",
                "heure": "19:00",
                "compte": "foodeatup",
                "format": "Vidéo 9:16",
                "lienCta": null
              },
              "linkedin": {
                "statut": "a_venir",
                "date": "2026-08-25",
                "heure": "08:00",
                "compte": "FoodEatUp",
                "format": "Vidéo native 9:16",
                "lienCta": "https://site.foodeatup.com/"
              },
              "youtube": {
                "statut": "a_venir",
                "date": "2026-08-25",
                "heure": "10:00",
                "compte": "@FoodEatUp",
                "format": "Short 9:16",
                "lienCta": "https://site.foodeatup.com/"
              }
            },
            "posterUrl": "/posters/EP019.jpg",
            "datePrevue": "2026-08-25",
            "troisMots": "PRÉDICTIONS DES COMMANDES",
            "tutoriel": {
              "titre": "Prédire ses commandes (ventes & production) FoodEatUp",
              "slug": "predire-ses-commandes",
              "url": "https://tutoriel.foodeatup.com/tutoriel/predire-ses-commandes",
              "module": "StockVision AI",
              "etape": "Ma carte & recettes\n- **Statut** : En ligne (0 min 39 s)\n- **Vidéo** : https://rapido-software.s3.eu-west-3.amazonaws.com/rapidosoftware/cms/bibliotheque/predire-ses-commandes-v1\n\n**Description (à quoi ça sert)**\n\nAnticiper les commandes à venir, plat par plat, pour ajuster vos quantités de production sans deviner — moins de ruptures en service, moins de gaspillage en cuisine.\n\n**Comment ça marche**\n\n1. Depuis Ma carte, repérez le plat à analyser — ici la Pizza Margherita napolitaine\n2. Cliquez sur l'icône graphique de sa carte pour ouvrir ses prédictions\n3. PrediBot affiche les commandes estimées jour par jour sur 7 ou 30 jours, avec l'indice de performance IA et le niveau de confiance du modèle\n4. Cliquez sur \"Exporter PDF\" pour télécharger le rapport et le partager avec votre équipe en cuisine\n\n**Astuce du chef** : Un indice de confiance \"Faible\" ne signifie pas que la prédiction est fausse : c'est fréquent en début d'historique de ventes, le temps que PrediBot accumule assez de données pour affiner ses estimations. Recroisez toujours l'estimation IA avec votre propre lecture du service avant d'ajuster votre production, surtout les premières semaines.\n\n---",
              "correspondance": "numéro",
              "confiance": 1.0
            },
            "tutorielModuleUrl": "https://tutoriel.foodeatup.com/module/stockvision-ai",
            "higgsfield": {
              "videoSourceUrl": "https://rapido-software.s3.eu-west-3.amazonaws.com/rapidosoftware/cms/bibliotheque/Higgsfield-source-EP019-Le-burger-qui-rebondit",
              "duree": "10 s",
              "format": "vertical 9:16",
              "source": "rapidocms"
            },
            "masterRapidoUrl": "https://rapido-software.s3.eu-west-3.amazonaws.com/rapidosoftware/cms/bibliotheque/FoodEatUp-EP019-Predictions-des-commandes"
          },
          {
            "id": "EP020",
            "numero": 20,
            "saison": 1,
            "slug": "ep020-le-chien-qui-a-reserve",
            "titre": "Le chien qui a réservé",
            "module": "Réservation",
            "chapitre": "2 - Ajouter une réservation",
            "accroche": "Lui, il a réservé.",
            "punchline": "Tes vrais clients aussi devraient pouvoir.",
            "resume": "Tu ajoutes une réservation en dix secondes, la table libre est proposée automatiquement. Et tes clients peuvent le faire eux-mêmes, depuis ton site.",
            "statut": "monte",
            "dureeSecondes": 37.5,
            "videoUrl": "https://raw.githubusercontent.com/PrendsTaPart/Video/claude/foodeatup-video-factory-wtb7gs/foodeatup-video-factory/dist/tiktok/EP020.mp4",
            "reseaux": {
              "facebook": {
                "statut": "a_venir",
                "date": "2026-08-26",
                "heure": "12:00",
                "compte": "FoodEatUp",
                "format": "Vidéo native 9:16",
                "lienCta": "https://site.foodeatup.com/"
              },
              "instagram": {
                "statut": "a_venir",
                "date": "2026-08-26",
                "heure": "18:30",
                "compte": "foodeatup.cocuisinage",
                "format": "Reel 9:16",
                "lienCta": null
              },
              "tiktok": {
                "statut": "a_venir",
                "date": "2026-08-26",
                "heure": "19:00",
                "compte": "foodeatup",
                "format": "Vidéo 9:16",
                "lienCta": null
              },
              "linkedin": {
                "statut": "a_venir",
                "date": "2026-08-26",
                "heure": "08:00",
                "compte": "FoodEatUp",
                "format": "Vidéo native 9:16",
                "lienCta": "https://site.foodeatup.com/"
              },
              "youtube": {
                "statut": "a_venir",
                "date": "2026-08-26",
                "heure": "10:00",
                "compte": "@FoodEatUp",
                "format": "Short 9:16",
                "lienCta": "https://site.foodeatup.com/"
              }
            },
            "posterUrl": "/posters/EP020.jpg",
            "datePrevue": "2026-08-26",
            "troisMots": "AJOUTER UNE RÉSERVATION",
            "tutoriel": {
              "titre": "module Table",
              "slug": "ajouter-une-reservation",
              "url": "https://tutoriel.foodeatup.com/tutoriel/ajouter-une-reservation",
              "module": "Réservations & Plan de salle",
              "etape": "Créer & modifier\n- **Statut** : En ligne (0 min 48 s)\n- **Vidéo** : https://rapido-software.s3.eu-west-3.amazonaws.com/rapidosoftware/cms/bibliotheque/foodeatup-reservation-tuto-v1\n\n**Description (à quoi ça sert)**\n\nCentraliser toutes vos réservations — site, téléphone, sur place — dans un même plan de salle, avec assignation de table automatique ou manuelle selon vos zones (Salle principale, Terrasse...), sans jamais ressaisir les informations d'un client à son arrivée.\n\n**Comment ça marche**\n\n1. Depuis Réservations, cliquez sur \"+ Nouvelle réservation\"\n2. Renseignez le nom du client, son téléphone et son email\n3. Choisissez la date, l'heure et le nombre de couverts\n4. Laissez FoodEatUp assigner automatiquement la meilleure table, ou choisissez-en une précisément parmi les tables disponibles\n5. Cliquez sur \"Créer la réservation\" : elle apparaît aussitôt dans votre liste, en statut En attente\n6. Confirmez-la, installez le client (Check-in) ou déclarez un no-show directement depuis le menu d'actions de la ligne\n\n**Astuce du chef** : Dès qu'un client arrive, confirmez sa réservation ou installez-le directement (Check-in) depuis le menu d'actions de la ligne, sans ressaisir ses informations. Un no-show se déclare en un clic pour garder l'historique propre et libérer la table pour d'autres clients.\n\n---",
              "correspondance": "numéro",
              "confiance": 1.0
            },
            "tutorielModuleUrl": "https://tutoriel.foodeatup.com/module/reservation-salle",
            "higgsfield": {
              "videoSourceUrl": "https://rapido-software.s3.eu-west-3.amazonaws.com/rapidosoftware/cms/bibliotheque/Higgsfield-source-EP020-Le-chien-qui-a-reserve",
              "duree": "10 s",
              "format": "vertical 9:16",
              "source": "rapidocms"
            },
            "masterRapidoUrl": "https://rapido-software.s3.eu-west-3.amazonaws.com/rapidosoftware/cms/bibliotheque/FoodEatUp-EP020-Ajouter-une-reservation"
          },
          {
            "id": "EP021",
            "numero": 21,
            "saison": 1,
            "slug": "ep021-chef-contre-imprimante",
            "titre": "Chef contre imprimante",
            "module": "KDS",
            "chapitre": "1 - Créer tes postes KDS",
            "accroche": "Le vrai ennemi du service.",
            "punchline": "Un KDS, et le combat s'arrête.",
            "resume": "Tu crées tes postes : chaud, froid, dessert. Chaque plat part au bon écran. Plus d'imprimante à secouer au milieu du service.",
            "statut": "monte",
            "dureeSecondes": 37.5,
            "videoUrl": "https://raw.githubusercontent.com/PrendsTaPart/Video/claude/foodeatup-video-factory-wtb7gs/foodeatup-video-factory/dist/tiktok/EP021.mp4",
            "reseaux": {
              "facebook": {
                "statut": "a_venir",
                "date": "2026-08-27",
                "heure": "12:00",
                "compte": "FoodEatUp",
                "format": "Vidéo native 9:16",
                "lienCta": "https://site.foodeatup.com/"
              },
              "instagram": {
                "statut": "a_venir",
                "date": "2026-08-27",
                "heure": "18:30",
                "compte": "foodeatup.cocuisinage",
                "format": "Reel 9:16",
                "lienCta": null
              },
              "tiktok": {
                "statut": "a_venir",
                "date": "2026-08-27",
                "heure": "19:00",
                "compte": "foodeatup",
                "format": "Vidéo 9:16",
                "lienCta": null
              },
              "linkedin": {
                "statut": "a_venir",
                "date": "2026-08-27",
                "heure": "08:00",
                "compte": "FoodEatUp",
                "format": "Vidéo native 9:16",
                "lienCta": "https://site.foodeatup.com/"
              },
              "youtube": {
                "statut": "a_venir",
                "date": "2026-08-27",
                "heure": "10:00",
                "compte": "@FoodEatUp",
                "format": "Short 9:16",
                "lienCta": "https://site.foodeatup.com/"
              }
            },
            "posterUrl": "/posters/EP021.jpg",
            "datePrevue": "2026-08-27",
            "troisMots": "CRÉER TES POSTES",
            "tutoriel": {
              "titre": "module KDS",
              "slug": "creer-un-poste-de-travail",
              "url": "https://tutoriel.foodeatup.com/tutoriel/creer-un-poste-de-travail",
              "module": "Écran Cuisine (KDS)",
              "etape": "Postes de travail\n- **Statut** : En ligne (0 min 35 s)\n- **Vidéo** : https://rapido-software.s3.eu-west-3.amazonaws.com/rapidosoftware/cms/bibliotheque/foodeatup-kds-poste-tuto-v1\n\n**Description (à quoi ça sert)**\n\nLe KDS (Kitchen Display System, ou écran d'affichage cuisine) remplace les tickets papier par un écran par poste — tablette ou télé — installé directement sur chaque zone de préparation. Dès qu'une commande est confirmée (comptoir, table, QR code ou livraison), elle s'affiche en temps réel sur le ou les postes concernés, sans impression ni allers-retours. Personnalisez un poste par zone réelle de votre cuisine — Entrée, Chaud, Grillade, Bar... — et FoodEatUp dispatche automatiquement chaque ligne de commande vers le bon poste selon la catégorie du plat.\n\n**Comment ça marche**\n\n1. Depuis le module KDS, ouvrez l'écran Cuisine (kds)\n2. Cliquez sur \"+ Nouveau poste\"\n3. Donnez-lui un nom qui correspond à sa zone de préparation en cuisine, comme Entrée, Chaud, Grillade ou Bar\n4. Choisissez son type : Préparation pour la production, ou Pass pour l'envoi des plats\n5. Choisissez une couleur pour le repérer d'un coup d'oeil\n6. Cliquez sur \"Créer le poste\" : il rejoint aussitôt la liste avec son propre lien d'écran\n7. Associez ensuite ses catégories de plats dans le routage du poste (Entrée, Chaud, Grillade, Bar...) pour que chaque commande confirmée s'affiche automatiquement au bon endroit\n\n**Astuce du chef** : Organisez vos postes selon vos zones de préparation réelles — par exemple Entrée, Chaud, Grillade et Bar — puis routez chaque catégorie de plat vers le bon poste : les entrées atterrissent chez le chef entrée, les grillades chez le grillardin, les boissons et desserts au bar, chacun ne voyant que ce qui le concerne, en temps réel dès la confirmation de la commande. Gardez toujours un poste marqué « Poste par défaut (tout le reste) » actif : il récupère automatiquement toutes les catégories non routées explicitement, pour ne jamais perdre une commande. Le poste de type Pass sert de dernière étape avant l'envoi en salle — idéal pour un contrôle qualité juste avant le service.\n\n---",
              "correspondance": "numéro",
              "confiance": 1.0
            },
            "tutorielModuleUrl": "https://tutoriel.foodeatup.com/module/kds-cuisine",
            "higgsfield": {
              "videoSourceUrl": "https://rapido-software.s3.eu-west-3.amazonaws.com/rapidosoftware/cms/bibliotheque/Higgsfield-source-EP021-Chef-contre-imprimante",
              "duree": "10 s",
              "format": "vertical 9:16",
              "source": "rapidocms"
            },
            "masterRapidoUrl": "https://rapido-software.s3.eu-west-3.amazonaws.com/rapidosoftware/cms/bibliotheque/FoodEatUp-EP021-Poste-de-travail-KDS"
          },
          {
            "id": "EP022",
            "numero": 22,
            "saison": 1,
            "slug": "ep022-la-facture-qui-fait-pleurer",
            "titre": "La facture qui fait pleurer",
            "module": "PrediBot",
            "chapitre": "2 - Marketplace de prompts",
            "accroche": "Mille euros par mois.",
            "punchline": "Pour dix logiciels qui ne se parlent même pas.",
            "resume": "Tout est déjà là : caisse, stock, planning, marketing, HACCP. Un seul abonnement, une seule base de données. Tes outils arrêtent de s'ignorer.",
            "statut": "monte",
            "dureeSecondes": 37.5,
            "videoUrl": "https://raw.githubusercontent.com/PrendsTaPart/Video/claude/foodeatup-video-factory-wtb7gs/foodeatup-video-factory/dist/tiktok/EP022.mp4",
            "reseaux": {
              "facebook": {
                "statut": "a_venir",
                "date": "2026-08-28",
                "heure": "12:00",
                "compte": "FoodEatUp",
                "format": "Vidéo native 9:16",
                "lienCta": "https://site.foodeatup.com/"
              },
              "instagram": {
                "statut": "a_venir",
                "date": "2026-08-28",
                "heure": "18:30",
                "compte": "foodeatup.cocuisinage",
                "format": "Reel 9:16",
                "lienCta": null
              },
              "tiktok": {
                "statut": "a_venir",
                "date": "2026-08-28",
                "heure": "19:00",
                "compte": "foodeatup",
                "format": "Vidéo 9:16",
                "lienCta": null
              },
              "linkedin": {
                "statut": "a_venir",
                "date": "2026-08-28",
                "heure": "08:00",
                "compte": "FoodEatUp",
                "format": "Vidéo native 9:16",
                "lienCta": "https://site.foodeatup.com/"
              },
              "youtube": {
                "statut": "a_venir",
                "date": "2026-08-28",
                "heure": "10:00",
                "compte": "@FoodEatUp",
                "format": "Short 9:16",
                "lienCta": "https://site.foodeatup.com/"
              }
            },
            "posterUrl": "/posters/EP022.jpg",
            "datePrevue": "2026-08-28",
            "troisMots": "MARKETPLACE DE PROMPTS",
            "tutoriel": {
              "titre": "Piocher dans la marketplace de prompts",
              "slug": "piocher-dans-la-marketplace-de-prompts",
              "url": "https://tutoriel.foodeatup.com/tutoriel/piocher-dans-la-marketplace-de-prompts",
              "module": "PrediBot (Agent IA Directeur)",
              "etape": "Marketplace de prompts\n- **Statut** : En ligne (0 min 40 s)\n- **Vidéo** : https://rapido-software.s3.eu-west-3.amazonaws.com/rapidosoftware/cms/bibliotheque/foodeatup-predibot-marketplace-tuto-v1\n\n**Description (à quoi ça sert)**\n\nUtilisez la marketplace de prompts pour piloter FoodEatUp directement depuis Claude, sans naviguer dans les menus : chaque prompt est prêt à l'emploi et pré-rempli pour votre établissement.\n\n**Comment ça marche**\n\n1. Ouvrez la marketplace de prompts FoodEatUp (182 prompts, triés par catégorie : Stock & Appro, Carte & Recettes, Commandes, Réservations, Finance, RH, Production, HACCP, Système, Orchestration).\n2. Trouvez le prompt qu'il vous faut, par exemple « Crée un nouveau fournisseur », et cliquez sur Tester en live.\n3. Le prompt s'ouvre directement dans Claude, déjà rempli avec l'identifiant de votre établissement.\n4. Répondez en une seule phrase avec les informations utiles (nom, type de produits, coordonnées...) : Claude structure le reste.\n5. Envoyez votre message : le fournisseur est créé en quelques secondes.\n6. Retournez sur FoodEatUp : la nouvelle fiche apparaît aussitôt dans votre liste.\n\n**Astuce du chef** : Copiez plusieurs prompts d'affilée dans la même conversation Claude : il garde le contexte de votre établissement d'un message à l'autre, pas besoin de répéter l'ID à chaque fois.\n\n---",
              "correspondance": "texte",
              "confiance": 0.73
            },
            "tutorielModuleUrl": "https://tutoriel.foodeatup.com/module/predibot",
            "higgsfield": {
              "videoSourceUrl": "https://rapido-software.s3.eu-west-3.amazonaws.com/rapidosoftware/cms/bibliotheque/Higgsfield-source-EP022-La-facture-qui-fait-pleurer",
              "duree": "10 s",
              "format": "vertical 9:16",
              "source": "rapidocms"
            },
            "masterRapidoUrl": "https://rapido-software.s3.eu-west-3.amazonaws.com/rapidosoftware/cms/bibliotheque/FoodEatUp-EP022-Marketplace-de-prompts"
          },
          {
            "id": "EP023",
            "numero": 23,
            "saison": 1,
            "slug": "ep023-l-aspirateur-robot",
            "titre": "L'aspirateur robot",
            "module": "Marketing",
            "chapitre": "24 - Calendrier IA avec Iris",
            "accroche": "Ton automatisation actuelle.",
            "punchline": "Automatiser, oui. Mais bien.",
            "resume": "Iris regarde ton exploitation et te propose quoi publier, et pourquoi. Tu valides ou tu refuses. L'automatisation te sert, elle ne t'échappe pas.",
            "statut": "monte",
            "dureeSecondes": 37.5,
            "videoUrl": "https://raw.githubusercontent.com/PrendsTaPart/Video/claude/foodeatup-video-factory-wtb7gs/foodeatup-video-factory/dist/tiktok/EP023.mp4",
            "reseaux": {
              "facebook": {
                "statut": "a_venir",
                "date": "2026-08-29",
                "heure": "12:00",
                "compte": "FoodEatUp",
                "format": "Vidéo native 9:16",
                "lienCta": "https://site.foodeatup.com/"
              },
              "instagram": {
                "statut": "a_venir",
                "date": "2026-08-29",
                "heure": "18:30",
                "compte": "foodeatup.cocuisinage",
                "format": "Reel 9:16",
                "lienCta": null
              },
              "tiktok": {
                "statut": "a_venir",
                "date": "2026-08-29",
                "heure": "19:00",
                "compte": "foodeatup",
                "format": "Vidéo 9:16",
                "lienCta": null
              },
              "linkedin": {
                "statut": "a_venir",
                "date": "2026-08-29",
                "heure": "08:00",
                "compte": "FoodEatUp",
                "format": "Vidéo native 9:16",
                "lienCta": "https://site.foodeatup.com/"
              },
              "youtube": {
                "statut": "a_venir",
                "date": "2026-08-29",
                "heure": "10:00",
                "compte": "@FoodEatUp",
                "format": "Short 9:16",
                "lienCta": "https://site.foodeatup.com/"
              }
            },
            "posterUrl": "/posters/EP023.jpg",
            "datePrevue": "2026-08-29",
            "troisMots": "CALENDRIER IA AVEC",
            "tutoriel": {
              "titre": "agent Iris",
              "slug": "calendrier-de-com-agent-iris",
              "url": "https://tutoriel.foodeatup.com/tutoriel/calendrier-de-com-agent-iris",
              "module": "Marketing, Fidélité & Iris",
              "etape": "Agent Iris\n- **Statut** : En ligne (0 min 56 s)\n- **Vidéo** : https://rapido-software.s3.eu-west-3.amazonaws.com/rapidosoftware/cms/bibliotheque/foodeatup-calendrier-iris-tuto-v1\n\n**Description (à quoi ça sert)**\n\nPublier régulièrement sur les réseaux sociaux demande du temps que peu de restaurateurs ont : trouver une bonne raison de poster, rédiger un texte accrocheur, choisir un visuel, puis le programmer au bon moment. L'agent Iris fait tout ce travail à votre place chaque nuit : elle détecte les opportunités réelles dans votre activité (un surstock à écouler, un jour creux à combler, un marronnier qui approche), rédige un texte et génère un visuel pour chaque proposition, puis les range dans un calendrier de la semaine. Vous n'avez plus qu'à relire, valider ou refuser — rien n'est publié sans votre accord.\n\n**Comment ça marche**\n\n1. Ouvrez l'agent Iris depuis le menu, puis l'onglet Calendrier pour voir la semaine déjà planifiée\n2. Cliquez sur Générer les propositions de la semaine : Iris analyse vos ventes, vos stocks et les temps forts du moment\n3. Patientez quelques secondes : un texte et un visuel sont générés automatiquement pour chaque jour\n4. Relisez chaque proposition et la raison détectée qui l'accompagne (surstock, jour creux, marronnier...)\n5. Cliquez sur le menu ⋯ d'une proposition puis sur Valider et planifier pour la programmer automatiquement sur vos réseaux, ou sur Refuser pour l'écarter\n\n**Astuce du chef** : Ne laissez pas les propositions d'Iris s'accumuler sans réponse : relisez le calendrier au moins une fois par semaine, sinon les meilleures fenêtres (jour creux, surstock proche de la date limite) seront passées. Un post généré depuis un surstock détecté marche particulièrement bien programmé le jour même, pas trois jours avant — c'est l'urgence qui donne envie de venir. Et si le texte proposé ne sonne pas exactement comme vous, éditez-le avant de valider : Iris propose, vous gardez toujours la main sur le ton final.\n\n---",
              "correspondance": "numéro",
              "confiance": 1.0
            },
            "tutorielModuleUrl": "https://tutoriel.foodeatup.com/module/marketing-fidelite",
            "higgsfield": {
              "videoSourceUrl": "https://rapido-software.s3.eu-west-3.amazonaws.com/rapidosoftware/cms/bibliotheque/Higgsfield-source-EP023-L-aspirateur-robot",
              "duree": "10 s",
              "format": "vertical 9:16",
              "source": "rapidocms"
            },
            "masterRapidoUrl": "https://rapido-software.s3.eu-west-3.amazonaws.com/rapidosoftware/cms/bibliotheque/FoodEatUp-EP023-Calendrier-IA-avec-Iris"
          },
          {
            "id": "EP024",
            "numero": 24,
            "saison": 1,
            "slug": "ep024-la-mouette-braqueuse",
            "titre": "La mouette braqueuse",
            "module": "Mon Site",
            "chapitre": "5 - Créer un site par IA",
            "accroche": "Encore une commission en moins.",
            "punchline": "Récupère tes commandes en direct.",
            "resume": "Ton site de commande est créé par l'IA depuis ta carte. Tes clients commandent en direct, chez toi. Zéro commission sur ces commandes-là.",
            "statut": "monte",
            "dureeSecondes": 37.5,
            "videoUrl": "https://raw.githubusercontent.com/PrendsTaPart/Video/claude/foodeatup-video-factory-wtb7gs/foodeatup-video-factory/dist/tiktok/EP024.mp4",
            "reseaux": {
              "facebook": {
                "statut": "a_venir",
                "date": "2026-08-30",
                "heure": "12:00",
                "compte": "FoodEatUp",
                "format": "Vidéo native 9:16",
                "lienCta": "https://site.foodeatup.com/"
              },
              "instagram": {
                "statut": "a_venir",
                "date": "2026-08-30",
                "heure": "18:30",
                "compte": "foodeatup.cocuisinage",
                "format": "Reel 9:16",
                "lienCta": null
              },
              "tiktok": {
                "statut": "a_venir",
                "date": "2026-08-30",
                "heure": "19:00",
                "compte": "foodeatup",
                "format": "Vidéo 9:16",
                "lienCta": null
              },
              "linkedin": {
                "statut": "a_venir",
                "date": "2026-08-30",
                "heure": "08:00",
                "compte": "FoodEatUp",
                "format": "Vidéo native 9:16",
                "lienCta": "https://site.foodeatup.com/"
              },
              "youtube": {
                "statut": "a_venir",
                "date": "2026-08-30",
                "heure": "10:00",
                "compte": "@FoodEatUp",
                "format": "Short 9:16",
                "lienCta": "https://site.foodeatup.com/"
              }
            },
            "posterUrl": "/posters/EP024.jpg",
            "datePrevue": "2026-08-30",
            "troisMots": "CRÉER SITE PAR",
            "tutoriel": {
              "titre": "Créer un site par IA FoodEatUp",
              "slug": "creer-un-site-par-ia",
              "url": "https://tutoriel.foodeatup.com/tutoriel/creer-un-site-par-ia",
              "module": "Site Web & Vitrine",
              "etape": "Template & design\n- **Statut** : En ligne (0 min 40 s)\n- **Vidéo** : https://rapido-software.s3.eu-west-3.amazonaws.com/rapidosoftware/cms/bibliotheque/creer-un-site-par-ia-v1\n\n**Description (à quoi ça sert)**\n\nObtenir un site vitrine complet et personnalisé sans écrire une ligne de texte ni toucher un seul réglage technique : l'IA construit pages, contenus et mise en page à partir d'une simple conversation sur votre restaurant.\n\n**Comment ça marche**\n\n1. Depuis Site Web, ouvrez Créer avec l'IA dans le menu de l'éditeur.\n2. Répondez aux questions de l'agent en langage naturel : ambiance, clientèle visée, plats signatures, ton souhaité...\n3. Poursuivez l'interview jusqu'à la douzième question pour un site fidèle à votre identité.\n4. L'IA génère automatiquement pages, textes et mise en page à partir de vos réponses, prêts à publier.\n\n**Astuce du chef** : Soyez précis dans vos réponses (plats signatures, ambiance, clientèle) : plus l'interview est détaillée, plus le site généré vous ressemble dès le premier essai.\n\n---",
              "correspondance": "numéro",
              "confiance": 1.0
            },
            "tutorielModuleUrl": "https://tutoriel.foodeatup.com/module/site-web-vitrine",
            "higgsfield": {
              "videoSourceUrl": "https://rapido-software.s3.eu-west-3.amazonaws.com/rapidosoftware/cms/bibliotheque/Higgsfield-source-EP024-La-mouette-braqueuse",
              "duree": "10 s",
              "format": "vertical 9:16",
              "source": "rapidocms"
            },
            "masterRapidoUrl": "https://rapido-software.s3.eu-west-3.amazonaws.com/rapidosoftware/cms/bibliotheque/FoodEatUp-EP024-Creer-son-site-par-IA"
          },
          {
            "id": "EP025",
            "numero": 25,
            "saison": 1,
            "slug": "ep025-le-mixeur-sans-couvercle",
            "titre": "Le mixeur sans couvercle",
            "module": "Marketing",
            "chapitre": "6 - Campagne 100 % IA",
            "accroche": "Quand tu lances une promo sans données.",
            "punchline": "Ça éclabousse. Et rarement toi.",
            "resume": "Tu ne lances plus une promo au hasard. FoodEatUp te propose la campagne depuis tes vraies données clients : qui cibler, avec quelle offre, quel jour.",
            "statut": "monte",
            "dureeSecondes": 37.5,
            "videoUrl": "https://raw.githubusercontent.com/PrendsTaPart/Video/claude/foodeatup-video-factory-wtb7gs/foodeatup-video-factory/dist/tiktok/EP025.mp4",
            "reseaux": {
              "facebook": {
                "statut": "a_venir",
                "date": "2026-08-31",
                "heure": "12:00",
                "compte": "FoodEatUp",
                "format": "Vidéo native 9:16",
                "lienCta": "https://site.foodeatup.com/"
              },
              "instagram": {
                "statut": "a_venir",
                "date": "2026-08-31",
                "heure": "18:30",
                "compte": "foodeatup.cocuisinage",
                "format": "Reel 9:16",
                "lienCta": null
              },
              "tiktok": {
                "statut": "a_venir",
                "date": "2026-08-31",
                "heure": "19:00",
                "compte": "foodeatup",
                "format": "Vidéo 9:16",
                "lienCta": null
              },
              "linkedin": {
                "statut": "a_venir",
                "date": "2026-08-31",
                "heure": "08:00",
                "compte": "FoodEatUp",
                "format": "Vidéo native 9:16",
                "lienCta": "https://site.foodeatup.com/"
              },
              "youtube": {
                "statut": "a_venir",
                "date": "2026-08-31",
                "heure": "10:00",
                "compte": "@FoodEatUp",
                "format": "Short 9:16",
                "lienCta": "https://site.foodeatup.com/"
              }
            },
            "posterUrl": "/posters/EP025.jpg",
            "datePrevue": "2026-08-31",
            "troisMots": "CAMPAGNE 100 %",
            "tutoriel": {
              "titre": "agent FoodEatUp",
              "slug": "creer-une-campagne-par-ia",
              "url": "https://tutoriel.foodeatup.com/tutoriel/creer-une-campagne-par-ia",
              "module": "Marketing, Fidélité & Iris",
              "etape": "Pack marketing & campagnes\n- **Statut** : En ligne (1 min 02 s)\n- **Vidéo** : https://rapido-software.s3.eu-west-3.amazonaws.com/rapidosoftware/cms/bibliotheque/creer-une-campagne-par-ia-v1\n\n**Description (à quoi ça sert)**\n\nLaisser l'agent IA de FoodEatUp analyser vos segments clients, vos jours creux et vos marges pour proposer des campagnes marketing chiffrées, prêtes à l'envoi en quelques clics — email, SMS, WhatsApp ou vocal, conformité (STOP, dédoublonnage) vérifiée automatiquement avant le lancement.\n\n**Comment ça marche**\n\n1. Ouvrez Campagnes & automatisations puis l'onglet Agent IA.\n2. Cliquez sur « Proposer des campagnes » : l'IA analyse vos segments RFM, vos jours creux et vos marges.\n3. Choisissez une proposition chiffrée et cliquez sur « Utiliser ».\n4. Ajustez la cible, le message, l'offre et le code promo si besoin.\n5. Envoyez maintenant ou planifiez en fonction des marronniers à venir.\n6. Vérifiez le récap de conformité (contactables, coût estimé, exclusions STOP) puis cliquez sur « Lancer ».\n\n**Astuce du chef** : Les segments RFM (Champions, Fidèles, Prometteurs, À risque, Perdus) sont recalculés chaque nuit depuis vos commandes réelles — relancez « Proposer des campagnes » régulièrement plutôt qu'une seule fois : les idées évoluent avec votre activité, pas seulement au moment des marronniers.\n\n---",
              "correspondance": "numéro",
              "confiance": 1.0
            },
            "tutorielModuleUrl": "https://tutoriel.foodeatup.com/module/marketing-fidelite",
            "higgsfield": {
              "videoSourceUrl": "https://rapido-software.s3.eu-west-3.amazonaws.com/rapidosoftware/cms/bibliotheque/Higgsfield-source-EP025-Le-mixeur-sans-couvercle",
              "duree": "10 s",
              "format": "vertical 9:16",
              "source": "rapidocms"
            },
            "masterRapidoUrl": "https://rapido-software.s3.eu-west-3.amazonaws.com/rapidosoftware/cms/bibliotheque/FoodEatUp-EP025-Campagne-100-pourcent-IA"
          },
          {
            "id": "EP026",
            "numero": 26,
            "saison": 1,
            "slug": "ep026-le-ballon-qui-explose",
            "titre": "Le ballon qui explose",
            "module": "StockVision",
            "chapitre": "5 - Envoyer sa liste de courses au fournisseur",
            "accroche": "Ton stock avant le week-end.",
            "punchline": "Prévois, au lieu de subir.",
            "resume": "Ta liste de courses se construit depuis ta production prévue. Tu l'envoies au fournisseur depuis l'écran. Le week-end se prépare le mercredi.",
            "statut": "monte",
            "dureeSecondes": 37.5,
            "videoUrl": "https://raw.githubusercontent.com/PrendsTaPart/Video/claude/foodeatup-video-factory-wtb7gs/foodeatup-video-factory/dist/tiktok/EP026.mp4",
            "reseaux": {
              "facebook": {
                "statut": "a_venir",
                "date": "2026-09-01",
                "heure": "12:00",
                "compte": "FoodEatUp",
                "format": "Vidéo native 9:16",
                "lienCta": "https://site.foodeatup.com/"
              },
              "instagram": {
                "statut": "a_venir",
                "date": "2026-09-01",
                "heure": "18:30",
                "compte": "foodeatup.cocuisinage",
                "format": "Reel 9:16",
                "lienCta": null
              },
              "tiktok": {
                "statut": "a_venir",
                "date": "2026-09-01",
                "heure": "19:00",
                "compte": "foodeatup",
                "format": "Vidéo 9:16",
                "lienCta": null
              },
              "linkedin": {
                "statut": "a_venir",
                "date": "2026-09-01",
                "heure": "08:00",
                "compte": "FoodEatUp",
                "format": "Vidéo native 9:16",
                "lienCta": "https://site.foodeatup.com/"
              },
              "youtube": {
                "statut": "a_venir",
                "date": "2026-09-01",
                "heure": "10:00",
                "compte": "@FoodEatUp",
                "format": "Short 9:16",
                "lienCta": "https://site.foodeatup.com/"
              }
            },
            "posterUrl": "/posters/EP026.jpg",
            "datePrevue": "2026-09-01",
            "troisMots": "ENVOYER LISTE COURSES",
            "tutoriel": {
              "titre": "Envoyer sa commande au fournisseur FoodEatUp",
              "slug": "envoyer-sa-commande-au-fournisseur",
              "url": "https://tutoriel.foodeatup.com/tutoriel/envoyer-sa-commande-au-fournisseur",
              "module": "StockVision AI",
              "etape": "Liste des courses & commandes\n- **Statut** : En ligne (0 min 48 s)\n- **Vidéo** : https://rapido-software.s3.eu-west-3.amazonaws.com/rapidosoftware/cms/bibliotheque/foodeatup-commande-fournisseur-tuto-v1\n\n**Description (à quoi ça sert)**\n\nTransformer votre liste de courses en commandes réelles, en un clic ou par email détaillé fournisseur par fournisseur avec la date de livraison souhaitée — fini les appels et les oublis, chaque fournisseur reçoit la bonne quantité au bon moment.\n\n**Comment ça marche**\n\n1. Depuis votre Liste des courses, cliquez sur \"Commander\" pour passer toutes vos commandes fournisseurs en un seul clic\n2. Une modale récapitule le nombre de produits et de fournisseurs concernés avant confirmation\n3. Vous préférez prévenir chaque fournisseur par email ? Cliquez sur \"Email\" pour voir le détail produit par produit de chaque fournisseur\n4. Cliquez sur \"Envoyer à tous les fournisseurs\"\n5. Choisissez la date et l'heure de livraison souhaitée, puis cliquez sur \"Envoyer à tous\"\n6. Chaque fournisseur reçoit un email avec sa propre liste de produits et la date de livraison demandée\n\n**Astuce du chef** : Cette liste de courses est la même que celle alimentée automatiquement par vos stocks et vos recettes (voir Tenir sa liste de courses) : pas besoin de la ressaisir avant de commander, elle reflète déjà ce qui manque réellement en cuisine.\n\n---",
              "correspondance": "numéro",
              "confiance": 1.0
            },
            "tutorielModuleUrl": "https://tutoriel.foodeatup.com/module/stockvision-ai",
            "higgsfield": {
              "videoSourceUrl": "https://rapido-software.s3.eu-west-3.amazonaws.com/rapidosoftware/cms/bibliotheque/Higgsfield-source-EP026-Le-ballon-qui-explose",
              "duree": "10 s",
              "format": "vertical 9:16",
              "source": "rapidocms"
            },
            "masterRapidoUrl": "https://rapido-software.s3.eu-west-3.amazonaws.com/rapidosoftware/cms/bibliotheque/FoodEatUp-EP026-Liste-de-courses-fournisseur"
          },
          {
            "id": "EP027",
            "numero": 27,
            "saison": 1,
            "slug": "ep027-le-chat-et-le-verre",
            "titre": "Le chat et le verre",
            "module": "Caisse POS",
            "chapitre": "6 - Clôturer sa caisse, le Z",
            "accroche": "Ta trésorerie, chaque lundi.",
            "punchline": "Il suffit d'un truc mal placé.",
            "resume": "Ton Z de caisse en un bouton : le compté, le théorique, l'écart, les moyens de paiement. Tu sais où tu en es tous les lundis matin.",
            "statut": "bloque",
            "dureeSecondes": null,
            "videoUrl": null,
            "reseaux": {
              "facebook": {
                "statut": "a_venir",
                "date": null,
                "heure": "12:00",
                "compte": "FoodEatUp",
                "format": "Vidéo native 9:16",
                "lienCta": "https://site.foodeatup.com/"
              },
              "instagram": {
                "statut": "a_venir",
                "date": null,
                "heure": "18:30",
                "compte": "foodeatup.cocuisinage",
                "format": "Reel 9:16",
                "lienCta": null
              },
              "tiktok": {
                "statut": "a_venir",
                "date": null,
                "heure": "19:00",
                "compte": "foodeatup",
                "format": "Vidéo 9:16",
                "lienCta": null
              },
              "linkedin": {
                "statut": "a_venir",
                "date": null,
                "heure": "08:00",
                "compte": "FoodEatUp",
                "format": "Vidéo native 9:16",
                "lienCta": "https://site.foodeatup.com/"
              },
              "youtube": {
                "statut": "a_venir",
                "date": null,
                "heure": "10:00",
                "compte": "@FoodEatUp",
                "format": "Short 9:16",
                "lienCta": "https://site.foodeatup.com/"
              }
            },
            "blocage": "Le chapitre correspondant n'a pas encore de vidéo dans le Drive interne.",
            "posterUrl": null,
            "datePrevue": null,
            "troisMots": "CLÔTURER SA CAISSE",
            "tutoriel": null,
            "tutorielModuleUrl": null,
            "tutorielManquant": "Le module Caisse POS n'existe pas encore dans l'Academy.",
            "higgsfield": {
              "videoSourceUrl": "https://rapido-software.s3.eu-west-3.amazonaws.com/rapidosoftware/cms/bibliotheque/Higgsfield-source-EP027-Le-chat-et-le-verre",
              "duree": "10 s",
              "format": "vertical 9:16",
              "source": "rapidocms"
            },
            "masterRapidoUrl": null
          },
          {
            "id": "EP028",
            "numero": 28,
            "saison": 1,
            "slug": "ep028-le-tapis-a-sushis-fou",
            "titre": "Le tapis à sushis fou",
            "module": "HubRise",
            "chapitre": "4 - Centraliser les commandes",
            "accroche": "Tes commandes en ligne, un vendredi.",
            "punchline": "Tout arrive. Nulle part.",
            "resume": "Uber Eats, Deliveroo, ton site, le comptoir : tout tombe dans la même file. Un vendredi soir, tu regardes un écran, pas quatre.",
            "statut": "bloque",
            "dureeSecondes": null,
            "videoUrl": null,
            "reseaux": {
              "facebook": {
                "statut": "a_venir",
                "date": null,
                "heure": "12:00",
                "compte": "FoodEatUp",
                "format": "Vidéo native 9:16",
                "lienCta": "https://site.foodeatup.com/"
              },
              "instagram": {
                "statut": "a_venir",
                "date": null,
                "heure": "18:30",
                "compte": "foodeatup.cocuisinage",
                "format": "Reel 9:16",
                "lienCta": null
              },
              "tiktok": {
                "statut": "a_venir",
                "date": null,
                "heure": "19:00",
                "compte": "foodeatup",
                "format": "Vidéo 9:16",
                "lienCta": null
              },
              "linkedin": {
                "statut": "a_venir",
                "date": null,
                "heure": "08:00",
                "compte": "FoodEatUp",
                "format": "Vidéo native 9:16",
                "lienCta": "https://site.foodeatup.com/"
              },
              "youtube": {
                "statut": "a_venir",
                "date": null,
                "heure": "10:00",
                "compte": "@FoodEatUp",
                "format": "Short 9:16",
                "lienCta": "https://site.foodeatup.com/"
              }
            },
            "blocage": "Le chapitre correspondant n'a pas encore de vidéo dans le Drive interne.",
            "posterUrl": null,
            "datePrevue": null,
            "troisMots": "CENTRALISER LES COMMANDES",
            "tutoriel": {
              "titre": "flux livraison",
              "slug": "centraliser-les-commandes-livraison",
              "url": "https://tutoriel.foodeatup.com/tutoriel/centraliser-les-commandes-livraison",
              "module": "HubRise & Livraisons",
              "etape": "Flux de commandes\n- **Statut** : Bientôt disponible (tournage en cours)\n\n**Description (à quoi ça sert)**\n\nCentraliser les commandes — flux livraison — tutoriel en préparation dans le module HubRise & Livraisons. Il arrive très bientôt dans ce fil conducteur.\n\n**Comment ça marche**\n\n1. Cette vidéo est en cours de tournage dans les cuisines FoodEatUp.\n2. Sa fiche est déjà en place : elle se remplira dès la mise en ligne.\n\n---",
              "correspondance": "numéro",
              "confiance": 1.0
            },
            "tutorielModuleUrl": "https://tutoriel.foodeatup.com/module/hubrise-livraisons",
            "higgsfield": {
              "videoSourceUrl": "https://rapido-software.s3.eu-west-3.amazonaws.com/rapidosoftware/cms/bibliotheque/Higgsfield-source-EP028-Le-tapis-a-sushis-fou",
              "duree": "10 s",
              "format": "vertical 9:16",
              "source": "rapidocms"
            },
            "masterRapidoUrl": null
          },
          {
            "id": "EP029",
            "numero": 29,
            "saison": 1,
            "slug": "ep029-les-douze-assiettes",
            "titre": "Les douze assiettes",
            "module": "PrediBot",
            "chapitre": "1 - Lire ses prévisions",
            "accroche": "Toi, gérant, en 2026.",
            "punchline": "Personne ne devrait travailler comme ça.",
            "resume": "Le brief du jour te dit ce qui compte avant que ça te tombe dessus : les réservations, les productions, les alertes. Tu diriges au lieu de courir.",
            "statut": "monte",
            "dureeSecondes": 37.5,
            "videoUrl": "https://raw.githubusercontent.com/PrendsTaPart/Video/claude/foodeatup-video-factory-wtb7gs/foodeatup-video-factory/dist/tiktok/EP029.mp4",
            "reseaux": {
              "facebook": {
                "statut": "a_venir",
                "date": "2026-09-02",
                "heure": "12:00",
                "compte": "FoodEatUp",
                "format": "Vidéo native 9:16",
                "lienCta": "https://site.foodeatup.com/"
              },
              "instagram": {
                "statut": "a_venir",
                "date": "2026-09-02",
                "heure": "18:30",
                "compte": "foodeatup.cocuisinage",
                "format": "Reel 9:16",
                "lienCta": null
              },
              "tiktok": {
                "statut": "a_venir",
                "date": "2026-09-02",
                "heure": "19:00",
                "compte": "foodeatup",
                "format": "Vidéo 9:16",
                "lienCta": null
              },
              "linkedin": {
                "statut": "a_venir",
                "date": "2026-09-02",
                "heure": "08:00",
                "compte": "FoodEatUp",
                "format": "Vidéo native 9:16",
                "lienCta": "https://site.foodeatup.com/"
              },
              "youtube": {
                "statut": "a_venir",
                "date": "2026-09-02",
                "heure": "10:00",
                "compte": "@FoodEatUp",
                "format": "Short 9:16",
                "lienCta": "https://site.foodeatup.com/"
              }
            },
            "posterUrl": "/posters/EP029.jpg",
            "datePrevue": "2026-09-02",
            "troisMots": "LIRE SES PRÉVISIONS",
            "tutoriel": {
              "titre": "Lire ses prévisions PrediBot",
              "slug": "lire-ses-previsions-predibot",
              "url": "https://tutoriel.foodeatup.com/tutoriel/lire-ses-previsions-predibot",
              "module": "PrediBot (Agent IA Directeur)",
              "etape": "Prévisions\n- **Statut** : En ligne (0 min 42 s)\n- **Vidéo** : https://raw.githubusercontent.com/PrendsTaPart/Video/claude/foodeatup-video-tutorials-bivyyp/videos/foodeatup-predibot-previsions-tuto/out/foodeatup-predibot-previsions-tuto-v1.mp4\n\n**Description (à quoi ça sert)**\n\nAnticiper vos besoins en stock, en commandes fournisseurs et en production grâce aux prédictions de l'intelligence artificielle PrediBot, pour éviter les ruptures et ne produire que le nécessaire.\n\n**Comment ça marche**\n\n1. Ouvrez Analyse et prédictions depuis le tableau de bord PrediBot pour voir vos indicateurs clés : alertes actives, économies potentielles, précision de l'IA.\n2. Cliquez sur Prédictions de stock pour visualiser votre consommation face à vos niveaux de stock, avec la recommandation de l'IA.\n3. Consultez Prévisions de commandes : PrediBot vous suggère quoi commander, produit par produit, avant la rupture de stock.\n4. Ouvrez Production recommandée pour voir les plats à préparer et les quantités conseillées, selon l'historique de vos ventes.\n\n**Astuce du chef** : Le pourcentage de précision IA et le niveau de confiance du modèle indiquent la fiabilité de chaque prévision : plus votre historique de ventes est riche, plus PrediBot affine ses recommandations semaine après semaine.\n\n---",
              "correspondance": "numéro",
              "confiance": 1.0
            },
            "tutorielModuleUrl": "https://tutoriel.foodeatup.com/module/predibot",
            "higgsfield": {
              "videoSourceUrl": "https://rapido-software.s3.eu-west-3.amazonaws.com/rapidosoftware/cms/bibliotheque/Higgsfield-source-EP029-Les-douze-assiettes",
              "duree": "10 s",
              "format": "vertical 9:16",
              "source": "rapidocms"
            },
            "masterRapidoUrl": "https://rapido-software.s3.eu-west-3.amazonaws.com/rapidosoftware/cms/bibliotheque/FoodEatUp-EP029-Lire-ses-previsions"
          },
          {
            "id": "EP030",
            "numero": 30,
            "saison": 1,
            "slug": "ep030-le-pingouin-en-cuisine",
            "titre": "Le pingouin en cuisine",
            "module": "Configuration",
            "chapitre": "Academy",
            "accroche": "Le nouveau, jour 1.",
            "punchline": "Forme-le en un clic avec l'Académy.",
            "resume": "Le nouveau se forme tout seul : chaque module a ses vidéos, dans l'ordre. Tu ne réexpliques plus la caisse à chaque embauche.",
            "statut": "monte",
            "dureeSecondes": 37.5,
            "videoUrl": "https://raw.githubusercontent.com/PrendsTaPart/Video/claude/foodeatup-video-factory-wtb7gs/foodeatup-video-factory/dist/tiktok/EP030.mp4",
            "reseaux": {
              "facebook": {
                "statut": "a_venir",
                "date": null,
                "heure": "12:00",
                "compte": "FoodEatUp",
                "format": "Vidéo native 9:16",
                "lienCta": "https://site.foodeatup.com/"
              },
              "instagram": {
                "statut": "a_venir",
                "date": null,
                "heure": "18:30",
                "compte": "foodeatup.cocuisinage",
                "format": "Reel 9:16",
                "lienCta": null
              },
              "tiktok": {
                "statut": "a_venir",
                "date": null,
                "heure": "19:00",
                "compte": "foodeatup",
                "format": "Vidéo 9:16",
                "lienCta": null
              },
              "linkedin": {
                "statut": "a_venir",
                "date": null,
                "heure": "08:00",
                "compte": "FoodEatUp",
                "format": "Vidéo native 9:16",
                "lienCta": "https://site.foodeatup.com/"
              },
              "youtube": {
                "statut": "a_venir",
                "date": null,
                "heure": "10:00",
                "compte": "@FoodEatUp",
                "format": "Short 9:16",
                "lienCta": "https://site.foodeatup.com/"
              }
            },
            "posterUrl": "/posters/EP030.jpg",
            "datePrevue": null,
            "troisMots": "ACADEMY",
            "tutoriel": null,
            "tutorielModuleUrl": "https://tutoriel.foodeatup.com/module/configuration",
            "tutorielManquant": "Ce chapitre n'a pas encore sa fiche dans l'Academy.",
            "higgsfield": {
              "videoSourceUrl": "https://rapido-software.s3.eu-west-3.amazonaws.com/rapidosoftware/cms/bibliotheque/Higgsfield-source-EP030-Le-pingouin-en-cuisine",
              "duree": "10 s",
              "format": "vertical 9:16",
              "source": "rapidocms"
            },
            "masterRapidoUrl": "https://rapido-software.s3.eu-west-3.amazonaws.com/rapidosoftware/cms/bibliotheque/FoodEatUp-EP030-Academy"
          }
        ]
      },
      {
        "numero": 2,
        "titre": "Compter sans se tromper",
        "pitch": "Stock, marge, factures : les chiffres qui décident de ta fin de mois.",
        "episodes": [
          {
            "id": "EP031",
            "numero": 31,
            "saison": 2,
            "slug": "ep031-l-avalanche-de-tupperware",
            "titre": "L'avalanche de tupperware",
            "module": "HACCP",
            "chapitre": "étiquettes DLC",
            "accroche": "C'est quoi, ça ?",
            "punchline": "Sans DLC tracées, personne ne sait.",
            "resume": "Tu crées ton étiquette DLC en trois secondes, avec le produit, la date et l'agent. Plus personne n'ouvre un bac en se demandant ce que c'est.",
            "statut": "monte",
            "dureeSecondes": 37.5,
            "videoUrl": "https://raw.githubusercontent.com/PrendsTaPart/Video/claude/foodeatup-video-factory-wtb7gs/foodeatup-video-factory/dist/tiktok/EP031.mp4",
            "reseaux": {
              "facebook": {
                "statut": "a_venir",
                "date": "2026-09-03",
                "heure": "12:00",
                "compte": "FoodEatUp",
                "format": "Vidéo native 9:16",
                "lienCta": "https://site.foodeatup.com/"
              },
              "instagram": {
                "statut": "a_venir",
                "date": "2026-09-03",
                "heure": "18:30",
                "compte": "foodeatup.cocuisinage",
                "format": "Reel 9:16",
                "lienCta": null
              },
              "tiktok": {
                "statut": "a_venir",
                "date": "2026-09-03",
                "heure": "19:00",
                "compte": "foodeatup",
                "format": "Vidéo 9:16",
                "lienCta": null
              },
              "linkedin": {
                "statut": "a_venir",
                "date": "2026-09-03",
                "heure": "08:00",
                "compte": "FoodEatUp",
                "format": "Vidéo native 9:16",
                "lienCta": "https://site.foodeatup.com/"
              },
              "youtube": {
                "statut": "a_venir",
                "date": "2026-09-03",
                "heure": "10:00",
                "compte": "@FoodEatUp",
                "format": "Short 9:16",
                "lienCta": "https://site.foodeatup.com/"
              }
            },
            "posterUrl": null,
            "datePrevue": "2026-09-03",
            "troisMots": "ÉTIQUETTES DLC",
            "tutoriel": {
              "titre": "Imprimer ses étiquettes (vente & stockage) FoodEatUp",
              "slug": "imprimer-ses-etiquettes",
              "url": "https://tutoriel.foodeatup.com/tutoriel/imprimer-ses-etiquettes",
              "module": "Hygiène & HACCP",
              "etape": "Étiquetage & DLC\n- **Statut** : En ligne (1 min 02 s)\n- **Vidéo** : https://rapido-software.s3.eu-west-3.amazonaws.com/rapidosoftware/cms/bibliotheque/imprimer-ses-etiquettes-v1\n\n**Description (à quoi ça sert)**\n\nGénérer en quelques clics des étiquettes de vente ou de stockage conformes HACCP - DLC, numéro de lot, code-barres et équipement de stockage calculés automatiquement à partir de votre catalogue - pour tracer chaque produit sans ressaisie manuelle et être prêt en cas de contrôle sanitaire.\n\n**Comment ça marche**\n\n1. Depuis le module Traçabilité > Étiqueteuse, sélectionnez le ou les produits à étiqueter.\n2. Cliquez sur \"Imprimer [n] étiquette(s)\" pour ouvrir la fiche Étiqueteuse.\n3. Renseignez la date et le type d'étiquette (Fait/ouvert, Frais, Surgelé, Prêt à manger, Vente) : le produit est déjà pré-rempli.\n4. La DLC, le numéro de lot et le code-barres de vente sont calculés automatiquement (modifiables si besoin).\n5. Choisissez le nombre d'étiquettes et l'équipement de stockage associé (ex : frigo 0°C à 4°C).\n6. Cliquez sur \"Créer les étiquettes\" : elles s'affichent aussitôt en aperçu, prêtes pour impression.\n7. Cliquez sur \"Valider -> Historique\" pour les ajouter à votre historique de traçabilité HACCP.\n\n**Astuce du chef** : Le bouton \"Créer les étiquettes\" ne s'active qu'une fois l'équipement de stockage renseigné : c'est volontaire, une étiquette sans lieu de stockage ne sert à rien en traçabilité. Imprimez toujours la quantité exacte de portions ou d'unités produites plutôt qu'une seule étiquette réutilisée - chaque étiquette avec son propre numéro de lot vous permet de retracer précisément un incident si besoin.\n\n---",
              "correspondance": "texte",
              "confiance": 0.54
            },
            "tutorielModuleUrl": "https://tutoriel.foodeatup.com/module/haccp",
            "higgsfield": {
              "videoSourceUrl": "https://rapido-software.s3.eu-west-3.amazonaws.com/rapidosoftware/cms/bibliotheque/Higgsfield-source-EP031-L-avalanche-de-tupperware",
              "duree": "10 s",
              "format": "vertical 9:16",
              "source": "rapidocms"
            },
            "masterRapidoUrl": "https://rapido-software.s3.eu-west-3.amazonaws.com/rapidosoftware/cms/bibliotheque/FoodEatUp-EP031-Etiquettes-de-production"
          },
          {
            "id": "EP032",
            "numero": 32,
            "saison": 2,
            "slug": "ep032-la-sauce-trop-forte",
            "titre": "La sauce trop forte",
            "module": "StockVision",
            "chapitre": "1 - Ma carte, fiche recette",
            "accroche": "Ta recette « au feeling ».",
            "punchline": "Une fiche technique, et c'est pareil tous les jours.",
            "resume": "Ta recette est enregistrée : ingrédients, quantités, étapes. Le plat sort pareil que ce soit toi ou ton commis. Et son coût est calculé.",
            "statut": "monte",
            "dureeSecondes": 37.5,
            "videoUrl": "https://raw.githubusercontent.com/PrendsTaPart/Video/claude/foodeatup-video-factory-wtb7gs/foodeatup-video-factory/dist/tiktok/EP032.mp4",
            "reseaux": {
              "facebook": {
                "statut": "a_venir",
                "date": "2026-09-04",
                "heure": "12:00",
                "compte": "FoodEatUp",
                "format": "Vidéo native 9:16",
                "lienCta": "https://site.foodeatup.com/"
              },
              "instagram": {
                "statut": "a_venir",
                "date": "2026-09-04",
                "heure": "18:30",
                "compte": "foodeatup.cocuisinage",
                "format": "Reel 9:16",
                "lienCta": null
              },
              "tiktok": {
                "statut": "a_venir",
                "date": "2026-09-04",
                "heure": "19:00",
                "compte": "foodeatup",
                "format": "Vidéo 9:16",
                "lienCta": null
              },
              "linkedin": {
                "statut": "a_venir",
                "date": "2026-09-04",
                "heure": "08:00",
                "compte": "FoodEatUp",
                "format": "Vidéo native 9:16",
                "lienCta": "https://site.foodeatup.com/"
              },
              "youtube": {
                "statut": "a_venir",
                "date": "2026-09-04",
                "heure": "10:00",
                "compte": "@FoodEatUp",
                "format": "Short 9:16",
                "lienCta": "https://site.foodeatup.com/"
              }
            },
            "posterUrl": null,
            "datePrevue": "2026-09-04",
            "troisMots": "MA CARTE",
            "tutoriel": {
              "titre": "Tenir ses dépenses avec StockVision AI",
              "slug": "tenir-ses-depenses",
              "url": "https://tutoriel.foodeatup.com/tutoriel/tenir-ses-depenses",
              "module": "StockVision AI",
              "etape": "Dépenses & factures\n- **Statut** : En ligne (0 min 45 s)\n- **Vidéo** : https://rapido-software.s3.eu-west-3.amazonaws.com/rapidosoftware/cms/bibliotheque/foodeatup-depenses-tuto-v1.mp4\n\n**Description (à quoi ça sert)**\n\nNe ressaisissez plus vos factures fournisseurs à la main : StockVision AI les lit et crée la dépense correspondante dans votre comptabilité FoodEatUp, prête à être suivie et réglée.\n\n**Comment ça marche**\n\n1. Depuis une livraison, cliquez sur + Ajouter une facture.\n2. Déposez la facture de votre fournisseur (PDF, JPG ou PNG, 10 Mo max).\n3. Laissez StockVision AI analyser le document : les produits et montants sont extraits automatiquement en quelques secondes.\n4. Vérifiez les produits détectés sur l'écran de validation de la facture.\n5. Cliquez sur Valider et enregistrer.\n6. Retrouvez la dépense créée automatiquement : détail des lignes, TVA et total TTC, directement dans votre comptabilité.\n\n**Astuce du chef** : StockVision AI lit vos factures fournisseurs et crée la dépense toute seule, plus besoin de ressaisir chaque ligne à la main. Le statut initial est En attente : passez-le en Payée une fois le règlement effectué, pour garder une comptabilité à jour en temps réel.\n\n---",
              "correspondance": "texte",
              "confiance": 0.4
            },
            "tutorielModuleUrl": "https://tutoriel.foodeatup.com/module/stockvision-ai",
            "higgsfield": {
              "videoSourceUrl": "https://rapido-software.s3.eu-west-3.amazonaws.com/rapidosoftware/cms/bibliotheque/Higgsfield-source-EP032-La-sauce-trop-forte",
              "duree": "10 s",
              "format": "vertical 9:16",
              "source": "rapidocms"
            },
            "masterRapidoUrl": "https://rapido-software.s3.eu-west-3.amazonaws.com/rapidosoftware/cms/bibliotheque/FoodEatUp-EP032-Ma-carte-fiche-recette"
          },
          {
            "id": "EP033",
            "numero": 33,
            "saison": 2,
            "slug": "ep033-le-roti-disparu",
            "titre": "Le rôti disparu",
            "module": "StockVision",
            "chapitre": "16 - Mouvements de stock",
            "accroche": "Tu as tout préparé. Presque.",
            "punchline": "Ce qui n'est pas suivi finit par disparaître.",
            "resume": "Ce qui n'est pas suivi disparaît. Ici chaque produit a son niveau, son seuil et son historique. Tu vois le trou avant le service, pas après.",
            "statut": "monte",
            "dureeSecondes": 37.5,
            "videoUrl": "https://raw.githubusercontent.com/PrendsTaPart/Video/claude/foodeatup-video-factory-wtb7gs/foodeatup-video-factory/dist/tiktok/EP033.mp4",
            "reseaux": {
              "facebook": {
                "statut": "a_venir",
                "date": "2026-09-05",
                "heure": "12:00",
                "compte": "FoodEatUp",
                "format": "Vidéo native 9:16",
                "lienCta": "https://site.foodeatup.com/"
              },
              "instagram": {
                "statut": "a_venir",
                "date": "2026-09-05",
                "heure": "18:30",
                "compte": "foodeatup.cocuisinage",
                "format": "Reel 9:16",
                "lienCta": null
              },
              "tiktok": {
                "statut": "a_venir",
                "date": "2026-09-05",
                "heure": "19:00",
                "compte": "foodeatup",
                "format": "Vidéo 9:16",
                "lienCta": null
              },
              "linkedin": {
                "statut": "a_venir",
                "date": "2026-09-05",
                "heure": "08:00",
                "compte": "FoodEatUp",
                "format": "Vidéo native 9:16",
                "lienCta": "https://site.foodeatup.com/"
              },
              "youtube": {
                "statut": "a_venir",
                "date": "2026-09-05",
                "heure": "10:00",
                "compte": "@FoodEatUp",
                "format": "Short 9:16",
                "lienCta": "https://site.foodeatup.com/"
              }
            },
            "posterUrl": null,
            "datePrevue": "2026-09-05",
            "troisMots": "MOUVEMENTS DE STOCK",
            "tutoriel": {
              "titre": "Lire ses mouvements de stock FoodEatUp",
              "slug": "lire-ses-mouvements-de-stock",
              "url": "https://tutoriel.foodeatup.com/tutoriel/lire-ses-mouvements-de-stock",
              "module": "StockVision AI",
              "etape": "Stock\n- **Statut** : En ligne (0 min 46 s)\n- **Vidéo** : https://rapido-software.s3.eu-west-3.amazonaws.com/rapidosoftware/cms/bibliotheque/foodeatup-mouvements-stock-tuto-v1\n\n**Description (à quoi ça sert)**\n\nDisposer d'un registre lisible de tout ce qui entre et sort de votre cuisine, et pouvoir remonter à la source de n'importe quel écart : qui a saisi quoi, quand, pour quel motif et chez quel fournisseur. C'est la pièce qui rend votre inventaire vérifiable au lieu d'être déclaratif.\n\n**Comment ça marche**\n\n1. Ouvrez \"Gestion des stocks\" puis \"Mouvements de Stock\" : chaque ligne indique le produit, le type (Entrée ou Sortie), la quantité, le motif, le fournisseur, la date et l'utilisateur\n2. Ouvrez le menu \"Action\" (les trois points) au bout de la ligne, puis cliquez sur \"Voir détails\"\n3. Lisez la fiche complète : Informations Générales (produit, type de mouvement, quantité, motif) et Informations Supplémentaires (fournisseur, date et heure exactes, utilisateur qui a fait la saisie)\n4. Pour corriger une erreur de saisie, cliquez sur \"Supprimer\" en haut à droite de la fiche\n5. Confirmez dans la fenêtre : la suppression affecte également le stock, pas seulement la ligne du registre\n6. Le mouvement disparaît du registre et le stock est recalculé en conséquence\n\n**Astuce du chef** : Supprimer un mouvement n'efface pas seulement une ligne d'historique : le stock est recalculé derrière. Si vous supprimez une entrée de 5000 pièces, ces 5000 pièces quittent aussi votre stock. Avant de supprimer, ouvrez toujours la fiche de détail et vérifiez la quantité et le motif — c'est le réflexe qui évite de transformer une erreur de saisie en écart d'inventaire.\n\n---",
              "correspondance": "numéro",
              "confiance": 1.0
            },
            "tutorielModuleUrl": "https://tutoriel.foodeatup.com/module/stockvision-ai",
            "higgsfield": {
              "videoSourceUrl": "https://rapido-software.s3.eu-west-3.amazonaws.com/rapidosoftware/cms/bibliotheque/Higgsfield-source-EP033-Le-roti-disparu",
              "duree": "10 s",
              "format": "vertical 9:16",
              "source": "rapidocms"
            },
            "masterRapidoUrl": "https://rapido-software.s3.eu-west-3.amazonaws.com/rapidosoftware/cms/bibliotheque/FoodEatUp-EP033-Mouvements-de-stock"
          },
          {
            "id": "EP034",
            "numero": 34,
            "saison": 2,
            "slug": "ep034-le-bouchon-rebelle",
            "titre": "Le bouchon rebelle",
            "module": "Configuration",
            "chapitre": "process",
            "accroche": "Chaque service, une improvisation.",
            "punchline": "Ça marche. Jusqu'au jour où ça ne marche plus.",
            "resume": "Tes procédures sont dans l'outil, pas dans ta tête. Le service ne dépend plus de qui est là ce soir.",
            "statut": "monte",
            "dureeSecondes": 37.5,
            "videoUrl": "https://raw.githubusercontent.com/PrendsTaPart/Video/claude/foodeatup-video-factory-wtb7gs/foodeatup-video-factory/dist/tiktok/EP034.mp4",
            "reseaux": {
              "facebook": {
                "statut": "a_venir",
                "date": null,
                "heure": "12:00",
                "compte": "FoodEatUp",
                "format": "Vidéo native 9:16",
                "lienCta": "https://site.foodeatup.com/"
              },
              "instagram": {
                "statut": "a_venir",
                "date": null,
                "heure": "18:30",
                "compte": "foodeatup.cocuisinage",
                "format": "Reel 9:16",
                "lienCta": null
              },
              "tiktok": {
                "statut": "a_venir",
                "date": null,
                "heure": "19:00",
                "compte": "foodeatup",
                "format": "Vidéo 9:16",
                "lienCta": null
              },
              "linkedin": {
                "statut": "a_venir",
                "date": null,
                "heure": "08:00",
                "compte": "FoodEatUp",
                "format": "Vidéo native 9:16",
                "lienCta": "https://site.foodeatup.com/"
              },
              "youtube": {
                "statut": "a_venir",
                "date": null,
                "heure": "10:00",
                "compte": "@FoodEatUp",
                "format": "Short 9:16",
                "lienCta": "https://site.foodeatup.com/"
              }
            },
            "blocage": "Le chapitre correspondant n'a pas encore de vidéo dans le Drive interne.",
            "posterUrl": null,
            "datePrevue": null,
            "troisMots": "PROCESS",
            "tutoriel": null,
            "tutorielModuleUrl": "https://tutoriel.foodeatup.com/module/configuration",
            "tutorielManquant": "Ce chapitre n'a pas encore sa fiche dans l'Academy.",
            "higgsfield": {
              "videoSourceUrl": "https://rapido-software.s3.eu-west-3.amazonaws.com/rapidosoftware/cms/bibliotheque/Higgsfield-source-EP034-Le-bouchon-rebelle",
              "duree": "10 s",
              "format": "vertical 9:16",
              "source": "rapidocms"
            },
            "masterRapidoUrl": "https://rapido-software.s3.eu-west-3.amazonaws.com/rapidosoftware/cms/bibliotheque/FoodEatUp-EP034-Procedures-de-service"
          },
          {
            "id": "EP035",
            "numero": 35,
            "saison": 2,
            "slug": "ep035-le-parasol-fugitif",
            "titre": "Le parasol fugitif",
            "module": "PrediBot",
            "chapitre": "1 - Lire ses prévisions",
            "accroche": "Ta terrasse, un jour de vent.",
            "punchline": "Certaines choses se prévoient.",
            "resume": "Prévisions de fréquentation, météo, événements du quartier : PrediBot te dit à quoi ressemble ton service avant qu'il commence.",
            "statut": "monte",
            "dureeSecondes": 37.5,
            "videoUrl": "https://raw.githubusercontent.com/PrendsTaPart/Video/claude/foodeatup-video-factory-wtb7gs/foodeatup-video-factory/dist/tiktok/EP035.mp4",
            "reseaux": {
              "facebook": {
                "statut": "a_venir",
                "date": "2026-09-06",
                "heure": "12:00",
                "compte": "FoodEatUp",
                "format": "Vidéo native 9:16",
                "lienCta": "https://site.foodeatup.com/"
              },
              "instagram": {
                "statut": "a_venir",
                "date": "2026-09-06",
                "heure": "18:30",
                "compte": "foodeatup.cocuisinage",
                "format": "Reel 9:16",
                "lienCta": null
              },
              "tiktok": {
                "statut": "a_venir",
                "date": "2026-09-06",
                "heure": "19:00",
                "compte": "foodeatup",
                "format": "Vidéo 9:16",
                "lienCta": null
              },
              "linkedin": {
                "statut": "a_venir",
                "date": "2026-09-06",
                "heure": "08:00",
                "compte": "FoodEatUp",
                "format": "Vidéo native 9:16",
                "lienCta": "https://site.foodeatup.com/"
              },
              "youtube": {
                "statut": "a_venir",
                "date": "2026-09-06",
                "heure": "10:00",
                "compte": "@FoodEatUp",
                "format": "Short 9:16",
                "lienCta": "https://site.foodeatup.com/"
              }
            },
            "posterUrl": null,
            "datePrevue": "2026-09-06",
            "troisMots": "LIRE SES PRÉVISIONS",
            "tutoriel": {
              "titre": "Lire ses prévisions PrediBot",
              "slug": "lire-ses-previsions-predibot",
              "url": "https://tutoriel.foodeatup.com/tutoriel/lire-ses-previsions-predibot",
              "module": "PrediBot (Agent IA Directeur)",
              "etape": "Prévisions\n- **Statut** : En ligne (0 min 42 s)\n- **Vidéo** : https://raw.githubusercontent.com/PrendsTaPart/Video/claude/foodeatup-video-tutorials-bivyyp/videos/foodeatup-predibot-previsions-tuto/out/foodeatup-predibot-previsions-tuto-v1.mp4\n\n**Description (à quoi ça sert)**\n\nAnticiper vos besoins en stock, en commandes fournisseurs et en production grâce aux prédictions de l'intelligence artificielle PrediBot, pour éviter les ruptures et ne produire que le nécessaire.\n\n**Comment ça marche**\n\n1. Ouvrez Analyse et prédictions depuis le tableau de bord PrediBot pour voir vos indicateurs clés : alertes actives, économies potentielles, précision de l'IA.\n2. Cliquez sur Prédictions de stock pour visualiser votre consommation face à vos niveaux de stock, avec la recommandation de l'IA.\n3. Consultez Prévisions de commandes : PrediBot vous suggère quoi commander, produit par produit, avant la rupture de stock.\n4. Ouvrez Production recommandée pour voir les plats à préparer et les quantités conseillées, selon l'historique de vos ventes.\n\n**Astuce du chef** : Le pourcentage de précision IA et le niveau de confiance du modèle indiquent la fiabilité de chaque prévision : plus votre historique de ventes est riche, plus PrediBot affine ses recommandations semaine après semaine.\n\n---",
              "correspondance": "numéro",
              "confiance": 1.0
            },
            "tutorielModuleUrl": "https://tutoriel.foodeatup.com/module/predibot",
            "higgsfield": {
              "videoSourceUrl": "https://rapido-software.s3.eu-west-3.amazonaws.com/rapidosoftware/cms/bibliotheque/Higgsfield-source-EP035-Le-parasol-fugitif",
              "duree": "10 s",
              "format": "vertical 9:16",
              "source": "rapidocms"
            },
            "masterRapidoUrl": "https://rapido-software.s3.eu-west-3.amazonaws.com/rapidosoftware/cms/bibliotheque/FoodEatUp-EP035-Lire-ses-previsions"
          },
          {
            "id": "EP036",
            "numero": 36,
            "saison": 2,
            "slug": "ep036-l-addition",
            "titre": "L'addition",
            "module": "PrediBot",
            "chapitre": "2 - Un seul abonnement",
            "accroche": "Toi, devant tes abonnements.",
            "punchline": "Additionne-les. Vraiment.",
            "resume": "Additionne tes abonnements actuels. Ici, la caisse, le stock, le planning, la compta et le marketing sont dans le même outil, sur la même base.",
            "statut": "monte",
            "dureeSecondes": 37.5,
            "videoUrl": "https://raw.githubusercontent.com/PrendsTaPart/Video/claude/foodeatup-video-factory-wtb7gs/foodeatup-video-factory/dist/tiktok/EP036.mp4",
            "reseaux": {
              "facebook": {
                "statut": "a_venir",
                "date": "2026-09-07",
                "heure": "12:00",
                "compte": "FoodEatUp",
                "format": "Vidéo native 9:16",
                "lienCta": "https://site.foodeatup.com/"
              },
              "instagram": {
                "statut": "a_venir",
                "date": "2026-09-07",
                "heure": "18:30",
                "compte": "foodeatup.cocuisinage",
                "format": "Reel 9:16",
                "lienCta": null
              },
              "tiktok": {
                "statut": "a_venir",
                "date": "2026-09-07",
                "heure": "19:00",
                "compte": "foodeatup",
                "format": "Vidéo 9:16",
                "lienCta": null
              },
              "linkedin": {
                "statut": "a_venir",
                "date": "2026-09-07",
                "heure": "08:00",
                "compte": "FoodEatUp",
                "format": "Vidéo native 9:16",
                "lienCta": "https://site.foodeatup.com/"
              },
              "youtube": {
                "statut": "a_venir",
                "date": "2026-09-07",
                "heure": "10:00",
                "compte": "@FoodEatUp",
                "format": "Short 9:16",
                "lienCta": "https://site.foodeatup.com/"
              }
            },
            "posterUrl": null,
            "datePrevue": "2026-09-07",
            "troisMots": "UN SEUL ABONNEMENT",
            "tutoriel": null,
            "tutorielModuleUrl": "https://tutoriel.foodeatup.com/module/predibot",
            "tutorielManquant": "Ce chapitre n'a pas encore sa fiche dans l'Academy.",
            "higgsfield": {
              "videoSourceUrl": "https://rapido-software.s3.eu-west-3.amazonaws.com/rapidosoftware/cms/bibliotheque/Higgsfield-source-EP036-L-addition",
              "duree": "10 s",
              "format": "vertical 9:16",
              "source": "rapidocms"
            },
            "masterRapidoUrl": "https://rapido-software.s3.eu-west-3.amazonaws.com/rapidosoftware/cms/bibliotheque/FoodEatUp-EP036-Un-seul-abonnement"
          },
          {
            "id": "EP037",
            "numero": 37,
            "saison": 2,
            "slug": "ep037-le-dormeur-debout",
            "titre": "Le dormeur debout",
            "module": "Équipe & Planning",
            "chapitre": "créer un shift",
            "accroche": "Fermeture. Troisième soir d'affilée.",
            "punchline": "Un planning bien fait, ça se voit sur les visages.",
            "resume": "Tu construis le planning de la semaine par glisser-déposer, avec le coût qui s'affiche en direct. Tes équipes savent, et toi aussi.",
            "statut": "monte",
            "dureeSecondes": 37.5,
            "videoUrl": "https://raw.githubusercontent.com/PrendsTaPart/Video/claude/foodeatup-video-factory-wtb7gs/foodeatup-video-factory/dist/tiktok/EP037.mp4",
            "reseaux": {
              "facebook": {
                "statut": "a_venir",
                "date": "2026-09-08",
                "heure": "12:00",
                "compte": "FoodEatUp",
                "format": "Vidéo native 9:16",
                "lienCta": "https://site.foodeatup.com/"
              },
              "instagram": {
                "statut": "a_venir",
                "date": "2026-09-08",
                "heure": "18:30",
                "compte": "foodeatup.cocuisinage",
                "format": "Reel 9:16",
                "lienCta": null
              },
              "tiktok": {
                "statut": "a_venir",
                "date": "2026-09-08",
                "heure": "19:00",
                "compte": "foodeatup",
                "format": "Vidéo 9:16",
                "lienCta": null
              },
              "linkedin": {
                "statut": "a_venir",
                "date": "2026-09-08",
                "heure": "08:00",
                "compte": "FoodEatUp",
                "format": "Vidéo native 9:16",
                "lienCta": "https://site.foodeatup.com/"
              },
              "youtube": {
                "statut": "a_venir",
                "date": "2026-09-08",
                "heure": "10:00",
                "compte": "@FoodEatUp",
                "format": "Short 9:16",
                "lienCta": "https://site.foodeatup.com/"
              }
            },
            "posterUrl": null,
            "datePrevue": "2026-09-08",
            "troisMots": "CRÉER UN SHIFT",
            "tutoriel": {
              "titre": "Accès & Jarvis FoodEatUp",
              "slug": "creer-son-code-pin",
              "url": "https://tutoriel.foodeatup.com/tutoriel/creer-son-code-pin",
              "module": "Équipe, Planning & RH",
              "etape": "Rôles, accès & code PIN\n- **Statut** : En ligne (0 min 23 s)\n- **Vidéo** : https://rapido-software.s3.eu-west-3.amazonaws.com/rapidosoftware/cms/bibliotheque/creer-son-code-pin-v1\n\n**Description (à quoi ça sert)**\n\nSécuriser l'accès à FoodEatUp en donnant à chaque employé un code PIN personnel — pour pointer son équipe et se connecter au logiciel avec les seules permissions liées à son rôle. Le QR code de cette même page sert lui à appairer une oreillette Bluetooth à Jarvis.\n\n**Comment ça marche**\n\n1. Dans Accès des employés, repérez qui a déjà un code PIN et qui n'en a pas\n2. Cliquez sur \"Définir un PIN\" (ou \"Modifier le PIN\" pour le changer)\n3. Saisissez un code à 4 ou 6 chiffres\n4. Cliquez sur \"Enregistrer\" — le code est actif immédiatement\n5. Le QR code permanent en haut de page sert lui à appairer une oreillette Bluetooth à Jarvis\n\n**Astuce du chef** : Un code PIN, c'est comme un mot de passe : gardez-le confidentiel et ne le partagez jamais entre employés — chaque code doit rester personnel pour que le pointage et les accès restent traçables et imputables à la bonne personne. Si un code est compromis ou qu'un employé quitte l'équipe, redéfinissez-le aussitôt via \"Modifier le PIN\" plutôt que de le laisser actif. Le rôle choisi à la création de l'employé (voir Ajouter ses employés) détermine précisément ce à quoi ce code donne accès — pas plus, pas moins : le principe de moindre privilège, appliqué sans configuration supplémentaire.\n\n---",
              "correspondance": "texte",
              "confiance": 0.56
            },
            "tutorielModuleUrl": "https://tutoriel.foodeatup.com/module/equipe-planning",
            "higgsfield": {
              "videoSourceUrl": "https://rapido-software.s3.eu-west-3.amazonaws.com/rapidosoftware/cms/bibliotheque/Higgsfield-source-EP037-Le-dormeur-debout",
              "duree": "10 s",
              "format": "vertical 9:16",
              "source": "rapidocms"
            },
            "masterRapidoUrl": "https://rapido-software.s3.eu-west-3.amazonaws.com/rapidosoftware/cms/bibliotheque/FoodEatUp-EP037-Planning-par-employe-ou-par-poste"
          },
          {
            "id": "EP038",
            "numero": 38,
            "saison": 2,
            "slug": "ep038-le-chariot-fou",
            "titre": "Le chariot fou",
            "module": "StockVision",
            "chapitre": "4 - Ma liste de courses",
            "accroche": "Le réappro du lundi.",
            "punchline": "Commander à l'instinct, ça finit toujours en course.",
            "resume": "Ta commande fournisseur se construit depuis tes stocks bas et ta production prévue. Tu ne commandes plus à l'instinct dans les rayons.",
            "statut": "monte",
            "dureeSecondes": 37.5,
            "videoUrl": "https://raw.githubusercontent.com/PrendsTaPart/Video/claude/foodeatup-video-factory-wtb7gs/foodeatup-video-factory/dist/tiktok/EP038.mp4",
            "reseaux": {
              "facebook": {
                "statut": "a_venir",
                "date": "2026-09-09",
                "heure": "12:00",
                "compte": "FoodEatUp",
                "format": "Vidéo native 9:16",
                "lienCta": "https://site.foodeatup.com/"
              },
              "instagram": {
                "statut": "a_venir",
                "date": "2026-09-09",
                "heure": "18:30",
                "compte": "foodeatup.cocuisinage",
                "format": "Reel 9:16",
                "lienCta": null
              },
              "tiktok": {
                "statut": "a_venir",
                "date": "2026-09-09",
                "heure": "19:00",
                "compte": "foodeatup",
                "format": "Vidéo 9:16",
                "lienCta": null
              },
              "linkedin": {
                "statut": "a_venir",
                "date": "2026-09-09",
                "heure": "08:00",
                "compte": "FoodEatUp",
                "format": "Vidéo native 9:16",
                "lienCta": "https://site.foodeatup.com/"
              },
              "youtube": {
                "statut": "a_venir",
                "date": "2026-09-09",
                "heure": "10:00",
                "compte": "@FoodEatUp",
                "format": "Short 9:16",
                "lienCta": "https://site.foodeatup.com/"
              }
            },
            "posterUrl": null,
            "datePrevue": "2026-09-09",
            "troisMots": "MA LISTE COURSES",
            "tutoriel": {
              "titre": "Tenir sa liste de courses FoodEatUp",
              "slug": "tenir-sa-liste-de-courses",
              "url": "https://tutoriel.foodeatup.com/tutoriel/tenir-sa-liste-de-courses",
              "module": "StockVision AI",
              "etape": "Liste des courses & commandes\n- **Statut** : En ligne (0 min 42 s)\n- **Vidéo** : https://rapido-software.s3.eu-west-3.amazonaws.com/rapidosoftware/cms/bibliotheque/foodeatup-liste-courses-tuto-v1\n\n**Description (à quoi ça sert)**\n\nGarder une liste de courses toujours exacte, sans recompter à la main : ajoutez un produit oublié, corrigez une quantité ou retirez un article obsolète en quelques clics, et votre liste reste prête à être transformée en commande fournisseur.\n\n**Comment ça marche**\n\n1. Ouvrez StockVision AI puis \"Liste des courses\" pour voir tous vos produits à commander, groupés par fournisseur\n2. Cliquez sur \"+ Ajouter produit\", choisissez l'article (existant ou nouveau), sa quantité, son unité et son fournisseur\n3. Cliquez sur \"Ajouter\" : le produit apparaît aussitôt dans la liste, sous son fournisseur\n4. Besoin de corriger une quantité ? Cliquez sur le crayon de la ligne, ajustez le chiffre et validez avec \"Modifier\"\n5. Un produit à retirer ? Cliquez sur la corbeille de sa ligne, puis confirmez avec \"Supprimer\"\n6. Votre liste reste toujours juste, prête à être commandée fournisseur par fournisseur\n\n**Astuce du chef** : Quand vous ajoutez un produit déjà connu, laissez FoodEatUp pré-remplir son unité et son prix d'achat : ça évite les écarts de saisie entre deux commandes. Et avant de cliquer sur Commander, un dernier passage en revue par fournisseur (le total est affiché sur chaque carte) vous évite les mauvaises surprises sur la facture — c'est plus rapide de corriger une quantité ici que de la découvrir à la livraison.\n\n---",
              "correspondance": "numéro",
              "confiance": 1.0
            },
            "tutorielModuleUrl": "https://tutoriel.foodeatup.com/module/stockvision-ai",
            "higgsfield": {
              "videoSourceUrl": "https://rapido-software.s3.eu-west-3.amazonaws.com/rapidosoftware/cms/bibliotheque/Higgsfield-source-EP038-Le-chariot-fou",
              "duree": "10 s",
              "format": "vertical 9:16",
              "source": "rapidocms"
            },
            "masterRapidoUrl": "https://rapido-software.s3.eu-west-3.amazonaws.com/rapidosoftware/cms/bibliotheque/FoodEatUp-EP038-Ma-liste-de-courses"
          },
          {
            "id": "EP039",
            "numero": 39,
            "saison": 2,
            "slug": "ep039-le-ballon-dans-la-soupe",
            "titre": "Le ballon dans la soupe",
            "module": "Réservation",
            "chapitre": "3 - Gérer et no-shows",
            "accroche": "L'imprévu du service.",
            "punchline": "Il y en aura d'autres. Autant être prêt.",
            "resume": "L'imprévu, tu ne l'évites pas. Mais tu vois en direct l'état de ta salle, tes retards et tes annulations, et tu réattribues en un geste.",
            "statut": "monte",
            "dureeSecondes": 37.5,
            "videoUrl": "https://raw.githubusercontent.com/PrendsTaPart/Video/claude/foodeatup-video-factory-wtb7gs/foodeatup-video-factory/dist/tiktok/EP039.mp4",
            "reseaux": {
              "facebook": {
                "statut": "a_venir",
                "date": "2026-09-10",
                "heure": "12:00",
                "compte": "FoodEatUp",
                "format": "Vidéo native 9:16",
                "lienCta": "https://site.foodeatup.com/"
              },
              "instagram": {
                "statut": "a_venir",
                "date": "2026-09-10",
                "heure": "18:30",
                "compte": "foodeatup.cocuisinage",
                "format": "Reel 9:16",
                "lienCta": null
              },
              "tiktok": {
                "statut": "a_venir",
                "date": "2026-09-10",
                "heure": "19:00",
                "compte": "foodeatup",
                "format": "Vidéo 9:16",
                "lienCta": null
              },
              "linkedin": {
                "statut": "a_venir",
                "date": "2026-09-10",
                "heure": "08:00",
                "compte": "FoodEatUp",
                "format": "Vidéo native 9:16",
                "lienCta": "https://site.foodeatup.com/"
              },
              "youtube": {
                "statut": "a_venir",
                "date": "2026-09-10",
                "heure": "10:00",
                "compte": "@FoodEatUp",
                "format": "Short 9:16",
                "lienCta": "https://site.foodeatup.com/"
              }
            },
            "posterUrl": null,
            "datePrevue": "2026-09-10",
            "troisMots": "GÉRER ET NO-SHOWS",
            "tutoriel": {
              "titre": "Gérer ses no-shows et modifications",
              "slug": "gerer-ses-no-shows",
              "url": "https://tutoriel.foodeatup.com/tutoriel/gerer-ses-no-shows",
              "module": "Réservations & Plan de salle",
              "etape": "Créer & modifier\n- **Statut** : En ligne (0 min 44 s)\n- **Vidéo** : https://rapido-software.s3.eu-west-3.amazonaws.com/rapidosoftware/cms/bibliotheque/foodeatup-noshow-tuto-v1\n\n**Description (à quoi ça sert)**\n\nUne réservation évolue rarement telle quelle jusqu'au service : le client change d'heure ou de nombre de couverts, ne se présente pas, ou annule complètement. Plutôt que de naviguer entre plusieurs écrans, ce menu centralise toutes les actions sur la ligne de réservation elle-même : modifier les détails, marquer une absence (no-show) pour libérer la table aussitôt, ou supprimer définitivement une réservation obsolète, avec une confirmation avant toute suppression.\n\n**Comment ça marche**\n\n1. Depuis Réservations, ouvrez le menu à trois points sur la ligne concernée\n2. Cliquez sur Modifier pour changer l'horaire, le nombre de couverts ou la table\n3. Le client ne s'est pas présenté ? Cliquez sur No-show pour libérer la table immédiatement\n4. Une réservation à supprimer définitivement ? Le même menu propose aussi cette option, avec confirmation avant suppression\n\n**Astuce du chef** : Marquez le no-show dès que vous constatez l'absence, pas en fin de service — la table se libère immédiatement pour être réattribuée à un autre client, et vos statistiques de fréquentation restent fiables. Le menu d'actions s'adapte au statut de la réservation : une fois en no-show, seules Modifier et Supprimer restent proposées, plus besoin de chercher parmi des actions qui ne s'appliquent plus.\n\n---",
              "correspondance": "numéro",
              "confiance": 1.0
            },
            "tutorielModuleUrl": "https://tutoriel.foodeatup.com/module/reservation-salle",
            "higgsfield": {
              "videoSourceUrl": "https://rapido-software.s3.eu-west-3.amazonaws.com/rapidosoftware/cms/bibliotheque/Higgsfield-source-EP039-Le-ballon-dans-la-soupe",
              "duree": "10 s",
              "format": "vertical 9:16",
              "source": "rapidocms"
            },
            "masterRapidoUrl": "https://rapido-software.s3.eu-west-3.amazonaws.com/rapidosoftware/cms/bibliotheque/FoodEatUp-EP039-Gerer-et-no-shows"
          },
          {
            "id": "EP040",
            "numero": 40,
            "saison": 2,
            "slug": "ep040-la-chevre-au-potager",
            "titre": "La chèvre au potager",
            "module": "StockVision",
            "chapitre": "17 - Ajouter un mouvement",
            "accroche": "Ton stock de basilic.",
            "punchline": "Ce qui n'est pas compté disparaît toujours.",
            "resume": "Tu comptes une fois, l'outil compte ensuite. Chaque sortie d'ingrédient est déduite de ton stock, plat par plat.",
            "statut": "monte",
            "dureeSecondes": 37.5,
            "videoUrl": "https://raw.githubusercontent.com/PrendsTaPart/Video/claude/foodeatup-video-factory-wtb7gs/foodeatup-video-factory/dist/tiktok/EP040.mp4",
            "reseaux": {
              "facebook": {
                "statut": "a_venir",
                "date": "2026-09-11",
                "heure": "12:00",
                "compte": "FoodEatUp",
                "format": "Vidéo native 9:16",
                "lienCta": "https://site.foodeatup.com/"
              },
              "instagram": {
                "statut": "a_venir",
                "date": "2026-09-11",
                "heure": "18:30",
                "compte": "foodeatup.cocuisinage",
                "format": "Reel 9:16",
                "lienCta": null
              },
              "tiktok": {
                "statut": "a_venir",
                "date": "2026-09-11",
                "heure": "19:00",
                "compte": "foodeatup",
                "format": "Vidéo 9:16",
                "lienCta": null
              },
              "linkedin": {
                "statut": "a_venir",
                "date": "2026-09-11",
                "heure": "08:00",
                "compte": "FoodEatUp",
                "format": "Vidéo native 9:16",
                "lienCta": "https://site.foodeatup.com/"
              },
              "youtube": {
                "statut": "a_venir",
                "date": "2026-09-11",
                "heure": "10:00",
                "compte": "@FoodEatUp",
                "format": "Short 9:16",
                "lienCta": "https://site.foodeatup.com/"
              }
            },
            "posterUrl": null,
            "datePrevue": "2026-09-11",
            "troisMots": "AJOUTER UN MOUVEMENT",
            "tutoriel": {
              "titre": "Saisir un mouvement de stock FoodEatUp",
              "slug": "saisir-un-mouvement-de-stock",
              "url": "https://tutoriel.foodeatup.com/tutoriel/saisir-un-mouvement-de-stock",
              "module": "StockVision AI",
              "etape": "Stock\n- **Statut** : En ligne (0 min 52 s)\n- **Vidéo** : https://rapido-software.s3.eu-west-3.amazonaws.com/rapidosoftware/cms/bibliotheque/foodeatup-mouvement-stock-tuto-v1\n\n**Description (à quoi ça sert)**\n\nTracer chaque entrée et chaque sortie de votre cuisine au moment où elle a lieu, plutôt que de découvrir l'écart à l'inventaire. Chaque mouvement saisi alimente StockVision AI, qui s'appuie dessus pour tenir vos quantités disponibles à jour, déclencher vos seuils d'alerte et alimenter votre liste de courses. Et parce qu'une erreur de frappe arrive, le mouvement reste modifiable après coup sans avoir à le supprimer et à le ressaisir.\n\n**Comment ça marche**\n\n1. Depuis \"Gestion des stocks\", cliquez sur \"Mouvement de stock\" pour ouvrir le registre des mouvements\n2. Cliquez sur \"Ajouter un mouvement\" pour ouvrir le formulaire\n3. Choisissez le produit concerné, puis le type de mouvement : \"Entrée\" pour une réception, \"Sortie\" pour une consommation ou une perte\n4. Saisissez la quantité et son unité (pièce, kg…), le motif du mouvement et le fournisseur\n5. Cliquez sur \"Ajouter\" : le mouvement est enregistré et apparaît aussitôt dans le registre avec sa date et le nom de l'utilisateur\n6. Pour corriger une erreur de saisie, ouvrez le menu \"Action\" (les trois points) de la ligne concernée et cliquez sur \"Modifier\"\n7. Le formulaire se rouvre pré-rempli : ajustez la quantité, validez, et votre stock est recalculé immédiatement\n\n**Astuce du chef** : Modifier vaut mieux que supprimer puis ressaisir. La modification ajuste le stock à partir de la nouvelle valeur en gardant la ligne d'origine dans le registre, avec son auteur et son horodatage : votre historique reste continu et vérifiable. Prenez aussi l'habitude de renseigner le motif à chaque fois (réception commande, perte, casse, inventaire) — c'est ce qui vous permettra plus tard de distinguer une consommation normale d'une démarque, et donc de savoir où part vraiment votre marge.\n\n---",
              "correspondance": "numéro",
              "confiance": 1.0
            },
            "tutorielModuleUrl": "https://tutoriel.foodeatup.com/module/stockvision-ai",
            "higgsfield": {
              "videoSourceUrl": "https://rapido-software.s3.eu-west-3.amazonaws.com/rapidosoftware/cms/bibliotheque/Higgsfield-source-EP040-La-chevre-au-potager",
              "duree": "10 s",
              "format": "vertical 9:16",
              "source": "rapidocms"
            },
            "masterRapidoUrl": "https://rapido-software.s3.eu-west-3.amazonaws.com/rapidosoftware/cms/bibliotheque/FoodEatUp-EP040-Ajouter-un-mouvement"
          },
          {
            "id": "EP041",
            "numero": 41,
            "saison": 2,
            "slug": "ep041-le-poulet-fugueur",
            "titre": "Le poulet fugueur",
            "module": "StockVision",
            "chapitre": "15 - Sortie des ingrédients de la production",
            "accroche": "Ton contrôle des portions.",
            "punchline": "Ce qui part au sol, tu le paies quand même.",
            "resume": "La production sort exactement les quantités prévues de ton stock. Ce qui tombe au sol, tu le vois dans l'écart. Et ce qui se voit se corrige.",
            "statut": "monte",
            "dureeSecondes": 37.5,
            "videoUrl": "https://raw.githubusercontent.com/PrendsTaPart/Video/claude/foodeatup-video-factory-wtb7gs/foodeatup-video-factory/dist/tiktok/EP041.mp4",
            "reseaux": {
              "facebook": {
                "statut": "a_venir",
                "date": "2026-09-12",
                "heure": "12:00",
                "compte": "FoodEatUp",
                "format": "Vidéo native 9:16",
                "lienCta": "https://site.foodeatup.com/"
              },
              "instagram": {
                "statut": "a_venir",
                "date": "2026-09-12",
                "heure": "18:30",
                "compte": "foodeatup.cocuisinage",
                "format": "Reel 9:16",
                "lienCta": null
              },
              "tiktok": {
                "statut": "a_venir",
                "date": "2026-09-12",
                "heure": "19:00",
                "compte": "foodeatup",
                "format": "Vidéo 9:16",
                "lienCta": null
              },
              "linkedin": {
                "statut": "a_venir",
                "date": "2026-09-12",
                "heure": "08:00",
                "compte": "FoodEatUp",
                "format": "Vidéo native 9:16",
                "lienCta": "https://site.foodeatup.com/"
              },
              "youtube": {
                "statut": "a_venir",
                "date": "2026-09-12",
                "heure": "10:00",
                "compte": "@FoodEatUp",
                "format": "Short 9:16",
                "lienCta": "https://site.foodeatup.com/"
              }
            },
            "posterUrl": null,
            "datePrevue": "2026-09-12",
            "troisMots": "SORTIE INGRÉDIENTS PRODUCTION",
            "tutoriel": {
              "titre": "Sortir ses ingrédients du stock de la production",
              "slug": "sortir-ses-ingredients-du-stock",
              "url": "https://tutoriel.foodeatup.com/tutoriel/sortir-ses-ingredients-du-stock",
              "module": "StockVision AI",
              "etape": "Production\n- **Statut** : En ligne (0 min 52 s)\n- **Vidéo** : https://rapido-software.s3.eu-west-3.amazonaws.com/rapidosoftware/cms/bibliotheque/foodeatup-sortie-stock-tuto-v1\n\n**Description (à quoi ça sert)**\n\nNe plus saisir aucune sortie de stock à la main : valider une production déstocke automatiquement tous les ingrédients de la recette et enstocke le produit fini, avec une ligne de mouvement tracée pour chacun. Votre stock reflète la réalité de la cuisine en temps réel, et chaque consommation est justifiée par la production qui l'a déclenchée.\n\n**Comment ça marche**\n\n1. Ouvrez \"Mes productions\" et repérez la production prête à produire — ici Dragon Roll, 29 portions planifiées\n2. Cliquez sur \"Valider la production\", puis renseignez les 3 étapes : quantité réellement produite, contrôle HACCP (température, qualité, hygiène), confirmation\n3. Cliquez sur \"Confirmer et valider\" : la production disparaît de vos productions prêtes (8 → 7)\n4. Ouvrez StockVision AI → Stocks, puis le bouton \"Mouvement de stock\"\n5. Retrouvez une ligne \"Sortie\" par ingrédient consommé (Riz à sushi 5800 g, Algues nori 58 unités, Anguille grillée 1450 g, Sauce teriyaki 870 ml, Avocat 2320 g…), toutes avec le motif \"Production: Dragon Roll\"\n6. Retrouvez aussi la ligne \"Entrée\" du produit fini — 29 portions de Dragon Roll, motif \"Production terminée\"\n7. Ouvrez le détail d'un mouvement pour voir le produit, le type, la quantité, la date et l'utilisateur qui a validé\n\n**Astuce du chef** : Avant de valider, regardez la mention \"ingrédient(s) manquant(s)\" sur la carte de production : si vous validez alors qu'un ingrédient n'est pas au stock, la sortie sera quand même écrite et votre stock partira en négatif ou en faux. Corrigez d'abord la réception, validez ensuite. Et servez-vous du motif des mouvements comme d'un audit : chaque sortie porte le nom de la production et l'utilisateur qui l'a validée — c'est le moyen le plus rapide de retrouver où sont réellement partis 5 kg de riz sur une semaine.\n\n---",
              "correspondance": "numéro",
              "confiance": 1.0
            },
            "tutorielModuleUrl": "https://tutoriel.foodeatup.com/module/stockvision-ai",
            "higgsfield": {
              "videoSourceUrl": "https://rapido-software.s3.eu-west-3.amazonaws.com/rapidosoftware/cms/bibliotheque/Higgsfield-source-EP041-Le-poulet-fugueur",
              "duree": "10 s",
              "format": "vertical 9:16",
              "source": "rapidocms"
            },
            "masterRapidoUrl": "https://rapido-software.s3.eu-west-3.amazonaws.com/rapidosoftware/cms/bibliotheque/FoodEatUp-EP041-Sortie-des-ingredients-de-la-production"
          },
          {
            "id": "EP042",
            "numero": 42,
            "saison": 2,
            "slug": "ep042-la-nappe-et-le-vent",
            "titre": "La nappe et le vent",
            "module": "Marketing",
            "chapitre": "21 - MCP RapidoCMS et Iris",
            "accroche": "Tout faire seul.",
            "punchline": "À un moment, il faut être aidé.",
            "resume": "Tu n'as pas à tout faire seul. Iris prépare tes contenus, PrediBot surveille tes chiffres, tu gardes la validation.",
            "statut": "monte",
            "dureeSecondes": 37.5,
            "videoUrl": "https://raw.githubusercontent.com/PrendsTaPart/Video/claude/foodeatup-video-factory-wtb7gs/foodeatup-video-factory/dist/tiktok/EP042.mp4",
            "reseaux": {
              "facebook": {
                "statut": "a_venir",
                "date": null,
                "heure": "12:00",
                "compte": "FoodEatUp",
                "format": "Vidéo native 9:16",
                "lienCta": "https://site.foodeatup.com/"
              },
              "instagram": {
                "statut": "a_venir",
                "date": null,
                "heure": "18:30",
                "compte": "foodeatup.cocuisinage",
                "format": "Reel 9:16",
                "lienCta": null
              },
              "tiktok": {
                "statut": "a_venir",
                "date": null,
                "heure": "19:00",
                "compte": "foodeatup",
                "format": "Vidéo 9:16",
                "lienCta": null
              },
              "linkedin": {
                "statut": "a_venir",
                "date": null,
                "heure": "08:00",
                "compte": "FoodEatUp",
                "format": "Vidéo native 9:16",
                "lienCta": "https://site.foodeatup.com/"
              },
              "youtube": {
                "statut": "a_venir",
                "date": null,
                "heure": "10:00",
                "compte": "@FoodEatUp",
                "format": "Short 9:16",
                "lienCta": "https://site.foodeatup.com/"
              }
            },
            "blocage": "Le chapitre correspondant n'a pas encore de vidéo dans le Drive interne.",
            "posterUrl": null,
            "datePrevue": null,
            "troisMots": "MCP RAPIDOCMS IRIS",
            "tutoriel": {
              "titre": "Intégrer le MCP RapidoCMS & Iris",
              "slug": "integrer-le-mcp-rapidocms-iris",
              "url": "https://tutoriel.foodeatup.com/tutoriel/integrer-le-mcp-rapidocms-iris",
              "module": "Marketing, Fidélité & Iris",
              "etape": "Agent Iris\n- **Statut** : Bientôt disponible (tournage en cours)\n\n**Description (à quoi ça sert)**\n\nIntégrer le MCP RapidoCMS & Iris — tutoriel en préparation dans le module Marketing, Fidélité & Iris. Il arrive très bientôt dans ce fil conducteur.\n\n**Comment ça marche**\n\n1. Cette vidéo est en cours de tournage dans les cuisines FoodEatUp.\n2. Sa fiche est déjà en place : elle se remplira dès la mise en ligne.\n\n---",
              "correspondance": "numéro",
              "confiance": 1.0
            },
            "tutorielModuleUrl": "https://tutoriel.foodeatup.com/module/marketing-fidelite",
            "higgsfield": {
              "videoSourceUrl": "https://rapido-software.s3.eu-west-3.amazonaws.com/rapidosoftware/cms/bibliotheque/Higgsfield-source-EP042-La-nappe-et-le-vent",
              "duree": "10 s",
              "format": "vertical 9:16",
              "source": "rapidocms"
            },
            "masterRapidoUrl": "https://rapido-software.s3.eu-west-3.amazonaws.com/rapidosoftware/cms/bibliotheque/FoodEatUp-EP042-Calendrier-de-communication-Iris"
          },
          {
            "id": "EP043",
            "numero": 43,
            "saison": 2,
            "slug": "ep043-l-ecureuil-et-le-croissant",
            "titre": "L'écureuil et le croissant",
            "module": "Caisse POS",
            "chapitre": "4 - Remises et avoirs",
            "accroche": "Petit vol. Tous les jours.",
            "punchline": "Mis bout à bout, ça fait ta marge.",
            "resume": "Chaque remise et chaque avoir est tracé, avec qui l'a fait et pourquoi. Les petits gestes ne mangent plus ta marge en silence.",
            "statut": "bloque",
            "dureeSecondes": null,
            "videoUrl": null,
            "reseaux": {
              "facebook": {
                "statut": "a_venir",
                "date": null,
                "heure": "12:00",
                "compte": "FoodEatUp",
                "format": "Vidéo native 9:16",
                "lienCta": "https://site.foodeatup.com/"
              },
              "instagram": {
                "statut": "a_venir",
                "date": null,
                "heure": "18:30",
                "compte": "foodeatup.cocuisinage",
                "format": "Reel 9:16",
                "lienCta": null
              },
              "tiktok": {
                "statut": "a_venir",
                "date": null,
                "heure": "19:00",
                "compte": "foodeatup",
                "format": "Vidéo 9:16",
                "lienCta": null
              },
              "linkedin": {
                "statut": "a_venir",
                "date": null,
                "heure": "08:00",
                "compte": "FoodEatUp",
                "format": "Vidéo native 9:16",
                "lienCta": "https://site.foodeatup.com/"
              },
              "youtube": {
                "statut": "a_venir",
                "date": null,
                "heure": "10:00",
                "compte": "@FoodEatUp",
                "format": "Short 9:16",
                "lienCta": "https://site.foodeatup.com/"
              }
            },
            "blocage": "Le chapitre correspondant n'a pas encore de vidéo dans le Drive interne.",
            "posterUrl": null,
            "datePrevue": null,
            "troisMots": "REMISES ET AVOIRS",
            "tutoriel": null,
            "tutorielModuleUrl": null,
            "tutorielManquant": "Le module Caisse POS n'existe pas encore dans l'Academy.",
            "higgsfield": {
              "videoSourceUrl": "https://rapido-software.s3.eu-west-3.amazonaws.com/rapidosoftware/cms/bibliotheque/Higgsfield-source-EP043-L-ecureuil-et-le-croissant",
              "duree": "10 s",
              "format": "vertical 9:16",
              "source": "rapidocms"
            },
            "masterRapidoUrl": null
          },
          {
            "id": "EP044",
            "numero": 44,
            "saison": 2,
            "slug": "ep044-les-six-stylos",
            "titre": "Les six stylos",
            "module": "Réservation",
            "chapitre": "5 - Commander par QR code",
            "accroche": "Prendre la commande en 2026.",
            "punchline": "La commande devrait partir en cuisine toute seule.",
            "resume": "Le client scanne, commande, la cuisine reçoit. Ton serveur passe son temps en salle, pas à recopier des lignes sur un carnet.",
            "statut": "monte",
            "dureeSecondes": 37.5,
            "videoUrl": "https://raw.githubusercontent.com/PrendsTaPart/Video/claude/foodeatup-video-factory-wtb7gs/foodeatup-video-factory/dist/tiktok/EP044.mp4",
            "reseaux": {
              "facebook": {
                "statut": "a_venir",
                "date": "2026-09-13",
                "heure": "12:00",
                "compte": "FoodEatUp",
                "format": "Vidéo native 9:16",
                "lienCta": "https://site.foodeatup.com/"
              },
              "instagram": {
                "statut": "a_venir",
                "date": "2026-09-13",
                "heure": "18:30",
                "compte": "foodeatup.cocuisinage",
                "format": "Reel 9:16",
                "lienCta": null
              },
              "tiktok": {
                "statut": "a_venir",
                "date": "2026-09-13",
                "heure": "19:00",
                "compte": "foodeatup",
                "format": "Vidéo 9:16",
                "lienCta": null
              },
              "linkedin": {
                "statut": "a_venir",
                "date": "2026-09-13",
                "heure": "08:00",
                "compte": "FoodEatUp",
                "format": "Vidéo native 9:16",
                "lienCta": "https://site.foodeatup.com/"
              },
              "youtube": {
                "statut": "a_venir",
                "date": "2026-09-13",
                "heure": "10:00",
                "compte": "@FoodEatUp",
                "format": "Short 9:16",
                "lienCta": "https://site.foodeatup.com/"
              }
            },
            "posterUrl": null,
            "datePrevue": "2026-09-13",
            "troisMots": "COMMANDER PAR QR",
            "tutoriel": {
              "titre": "Scanner le QR code de la table",
              "slug": "scanner-le-qr-code-de-la-table",
              "url": "https://tutoriel.foodeatup.com/tutoriel/scanner-le-qr-code-de-la-table",
              "module": "Réservations & Plan de salle",
              "etape": "Placement en salle\n- **Statut** : En ligne (0 min 45 s)\n- **Vidéo** : https://rapido-software.s3.eu-west-3.amazonaws.com/rapidosoftware/cms/bibliotheque/foodeatup-qrcode-table-tuto\n\n**Description (à quoi ça sert)**\n\nPermettre à vos clients de commander (et payer) directement depuis leur table, en scannant un QR code généré en un clic depuis le plan de salle — moins d'attente, moins d'allers-retours en salle, une commande transmise en cuisine en temps réel.\n\n**Comment ça marche**\n\n1. Depuis le Plan de salle, sélectionnez la table du client (ex. QA3).\n2. Cliquez sur \"QR code de la table\" : le QR et son lien sont générés instantanément.\n3. Téléchargez-le pour l'imprimer sur la table, ou copiez directement le lien.\n4. Le client scanne avec son téléphone : il arrive directement sur la carte de sa table.\n5. Il choisit ses plats, les ajoute au panier et valide sa commande.\n6. La commande part aussitôt en cuisine, sans passer par un serveur — et il peut régler l'addition directement depuis son téléphone.\n\n**Astuce du chef** : Imprimez le QR code au format tube ou prime pour qu'il reste bien visible sur chaque table, et testez-le vous-même avec votre téléphone avant le service : vous verrez exactement l'écran que découvre votre client, panier et bouton de paiement inclus.\n\n---",
              "correspondance": "numéro",
              "confiance": 1.0
            },
            "tutorielModuleUrl": "https://tutoriel.foodeatup.com/module/reservation-salle",
            "higgsfield": {
              "videoSourceUrl": "https://rapido-software.s3.eu-west-3.amazonaws.com/rapidosoftware/cms/bibliotheque/Higgsfield-source-EP044-Les-six-stylos",
              "duree": "10 s",
              "format": "vertical 9:16",
              "source": "rapidocms"
            },
            "masterRapidoUrl": "https://rapido-software.s3.eu-west-3.amazonaws.com/rapidosoftware/cms/bibliotheque/FoodEatUp-EP044-Commander-par-QR-code"
          },
          {
            "id": "EP045",
            "numero": 45,
            "saison": 2,
            "slug": "ep045-la-chambre-froide",
            "titre": "La chambre froide",
            "module": "StockVision",
            "chapitre": "18 - Statistiques par module",
            "accroche": "Personne ne sait où tu es.",
            "punchline": "Ton restaurant non plus ne devrait pas être une boîte noire.",
            "resume": "Ton restaurant arrête d'être une boîte noire : ventes, marges, fréquentation, stock, module par module, sur la période que tu choisis.",
            "statut": "monte",
            "dureeSecondes": 37.5,
            "videoUrl": "https://raw.githubusercontent.com/PrendsTaPart/Video/claude/foodeatup-video-factory-wtb7gs/foodeatup-video-factory/dist/tiktok/EP045.mp4",
            "reseaux": {
              "facebook": {
                "statut": "a_venir",
                "date": "2026-09-14",
                "heure": "12:00",
                "compte": "FoodEatUp",
                "format": "Vidéo native 9:16",
                "lienCta": "https://site.foodeatup.com/"
              },
              "instagram": {
                "statut": "a_venir",
                "date": "2026-09-14",
                "heure": "18:30",
                "compte": "foodeatup.cocuisinage",
                "format": "Reel 9:16",
                "lienCta": null
              },
              "tiktok": {
                "statut": "a_venir",
                "date": "2026-09-14",
                "heure": "19:00",
                "compte": "foodeatup",
                "format": "Vidéo 9:16",
                "lienCta": null
              },
              "linkedin": {
                "statut": "a_venir",
                "date": "2026-09-14",
                "heure": "08:00",
                "compte": "FoodEatUp",
                "format": "Vidéo native 9:16",
                "lienCta": "https://site.foodeatup.com/"
              },
              "youtube": {
                "statut": "a_venir",
                "date": "2026-09-14",
                "heure": "10:00",
                "compte": "@FoodEatUp",
                "format": "Short 9:16",
                "lienCta": "https://site.foodeatup.com/"
              }
            },
            "posterUrl": null,
            "datePrevue": "2026-09-14",
            "troisMots": "STATISTIQUES PAR MODULE",
            "tutoriel": {
              "titre": "Lire ses statistiques par module",
              "slug": "lire-ses-statistiques-par-module",
              "url": "https://tutoriel.foodeatup.com/tutoriel/lire-ses-statistiques-par-module",
              "module": "StockVision AI",
              "etape": "Statistiques & agent IA\n- **Statut** : En ligne (0 min 54 s)\n- **Vidéo** : https://rapido-software.s3.eu-west-3.amazonaws.com/rapidosoftware/cms/bibliotheque/foodeatup-statistiques-module-tuto-v1\n\n**Description (à quoi ça sert)**\n\nSuivre en temps réel la santé de votre restaurant module par module — chiffre d'affaires et marges, niveaux de stock, heures travaillées, conformité HACCP et production — sans jongler entre plusieurs outils.\n\n**Comment ça marche**\n\n1. Ouvrez le tableau de bord Analytix BI pour voir votre chiffre d'affaires, vos commandes, votre marge brute et votre score HACCP en un coup d'œil.\n2. Cliquez sur un module (Finances, Stocks, RH & Pointage, HACCP, Production) pour accéder à ses statistiques détaillées.\n3. Ajustez la période avec le sélecteur de dates puis cliquez sur Appliquer pour recalculer les chiffres du module.\n4. Posez une question en langage naturel à l'Assistant IA pour faire interpréter vos données BI.\n\n**Astuce du chef** : Chaque graphique du tableau de bord affiche aussi la période précédente en comparaison : un coup d'œil suffit pour repérer une marge qui glisse ou des anomalies HACCP qui remontent, avant que ça ne devienne un vrai problème en cuisine.\n\n---",
              "correspondance": "numéro",
              "confiance": 1.0
            },
            "tutorielModuleUrl": "https://tutoriel.foodeatup.com/module/stockvision-ai",
            "higgsfield": {
              "videoSourceUrl": "https://rapido-software.s3.eu-west-3.amazonaws.com/rapidosoftware/cms/bibliotheque/Higgsfield-source-EP045-La-chambre-froide",
              "duree": "10 s",
              "format": "vertical 9:16",
              "source": "rapidocms"
            },
            "masterRapidoUrl": "https://rapido-software.s3.eu-west-3.amazonaws.com/rapidosoftware/cms/bibliotheque/FoodEatUp-EP045-Statistiques-par-module"
          },
          {
            "id": "EP046",
            "numero": 46,
            "saison": 2,
            "slug": "ep046-le-sel",
            "titre": "Le sel",
            "module": "StockVision",
            "chapitre": "20 - Agent IA et suggestions",
            "accroche": "Un détail. Un service perdu.",
            "punchline": "Les petites erreurs coûtent cher quand personne ne les voit.",
            "resume": "L'IA remonte ce que tu n'as pas le temps de voir : un coût qui monte, un plat qui décroche, un stock qui dort. Le petit détail devient visible.",
            "statut": "a_produire",
            "dureeSecondes": null,
            "videoUrl": null,
            "reseaux": {
              "facebook": {
                "statut": "a_venir",
                "date": "2026-09-15",
                "heure": "12:00",
                "compte": "FoodEatUp",
                "format": "Vidéo native 9:16",
                "lienCta": "https://site.foodeatup.com/"
              },
              "instagram": {
                "statut": "a_venir",
                "date": "2026-09-15",
                "heure": "18:30",
                "compte": "foodeatup.cocuisinage",
                "format": "Reel 9:16",
                "lienCta": null
              },
              "tiktok": {
                "statut": "a_venir",
                "date": "2026-09-15",
                "heure": "19:00",
                "compte": "foodeatup",
                "format": "Vidéo 9:16",
                "lienCta": null
              },
              "linkedin": {
                "statut": "a_venir",
                "date": "2026-09-15",
                "heure": "08:00",
                "compte": "FoodEatUp",
                "format": "Vidéo native 9:16",
                "lienCta": "https://site.foodeatup.com/"
              },
              "youtube": {
                "statut": "a_venir",
                "date": "2026-09-15",
                "heure": "10:00",
                "compte": "@FoodEatUp",
                "format": "Short 9:16",
                "lienCta": "https://site.foodeatup.com/"
              }
            },
            "posterUrl": null,
            "datePrevue": "2026-09-15",
            "troisMots": "AGENT IA SUGGESTIONS",
            "tutoriel": {
              "titre": "Suivre les suggestions de l'agent IA FoodEatUp",
              "slug": "suivre-suggestions-agent-ia",
              "url": "https://tutoriel.foodeatup.com/tutoriel/suivre-suggestions-agent-ia",
              "module": "StockVision AI",
              "etape": "Statistiques & agent IA\n- **Statut** : En ligne (0 min 48 s)\n- **Vidéo** : https://rapido-software.s3.eu-west-3.amazonaws.com/rapidosoftware/cms/bibliotheque/suivre-suggestions-agent-ia-v1\n\n**Description (à quoi ça sert)**\n\nNe plus chercher l'information vous-même : suivez les suggestions que l'agent IA affiche déjà sur votre tableau de bord, posez-lui votre question en langage naturel, et obtenez une réponse détaillée et actionnable en quelques secondes.\n\n**Comment ça marche**\n\n1. Depuis le tableau de bord, repérez l'alerte \"Stock critique\" qui signale vos ruptures et stocks faibles\n2. Ouvrez le menu et retrouvez PrediBot, votre agent IA, puis cliquez sur \"Chat PrediBot\"\n3. L'agent vous accueille avec des suggestions déjà prêtes : Stocks, Commandes, HACCP\n4. Posez votre question en langage naturel, par exemple \"Quels sont les produits en rupture de stock ?\"\n5. PrediBot analyse vos données et répond aussitôt, produit par produit (quantité, seuil, emplacement, fournisseur, péremption), avec un lien direct vers votre page stocks\n\n**Astuce du chef** : Le tableau de bord affiche déjà le nombre de ruptures et de stocks faibles : c'est la suggestion la plus rapide à suivre. Pas besoin de formuler une question parfaite — PrediBot comprend le langage courant (\"produits en rupture\", \"qu'est-ce qu'il me manque\"...) et vous redirige toujours vers la bonne page pour agir.\n\n---",
              "correspondance": "numéro",
              "confiance": 1.0
            },
            "tutorielModuleUrl": "https://tutoriel.foodeatup.com/module/stockvision-ai",
            "higgsfield": {
              "videoSourceUrl": null,
              "duree": "10 s",
              "format": "vertical 9:16",
              "source": null
            },
            "masterRapidoUrl": null
          },
          {
            "id": "EP047",
            "numero": 47,
            "saison": 2,
            "slug": "ep047-le-camion-dans-la-ruelle",
            "titre": "Le camion dans la ruelle",
            "module": "HACCP",
            "chapitre": "contrôle à réception",
            "accroche": "La livraison de 7 h.",
            "punchline": "Réceptionner, contrôler, tracer. Sans y penser.",
            "resume": "À la livraison, tu contrôles la température, tu prends la photo, c'est tracé. Sept heures du matin, et ta conformité est déjà faite.",
            "statut": "a_produire",
            "dureeSecondes": null,
            "videoUrl": null,
            "reseaux": {
              "facebook": {
                "statut": "a_venir",
                "date": "2026-09-16",
                "heure": "12:00",
                "compte": "FoodEatUp",
                "format": "Vidéo native 9:16",
                "lienCta": "https://site.foodeatup.com/"
              },
              "instagram": {
                "statut": "a_venir",
                "date": "2026-09-16",
                "heure": "18:30",
                "compte": "foodeatup.cocuisinage",
                "format": "Reel 9:16",
                "lienCta": null
              },
              "tiktok": {
                "statut": "a_venir",
                "date": "2026-09-16",
                "heure": "19:00",
                "compte": "foodeatup",
                "format": "Vidéo 9:16",
                "lienCta": null
              },
              "linkedin": {
                "statut": "a_venir",
                "date": "2026-09-16",
                "heure": "08:00",
                "compte": "FoodEatUp",
                "format": "Vidéo native 9:16",
                "lienCta": "https://site.foodeatup.com/"
              },
              "youtube": {
                "statut": "a_venir",
                "date": "2026-09-16",
                "heure": "10:00",
                "compte": "@FoodEatUp",
                "format": "Short 9:16",
                "lienCta": "https://site.foodeatup.com/"
              }
            },
            "posterUrl": null,
            "datePrevue": "2026-09-16",
            "troisMots": "CONTRÔLE À RÉCEPTION",
            "tutoriel": {
              "titre": "Contrôler à réception de vos livraisons (Module HACCP)",
              "slug": "controler-reception-livraisons",
              "url": "https://tutoriel.foodeatup.com/tutoriel/controler-reception-livraisons",
              "module": "Hygiène & HACCP",
              "etape": "Contrôle à réception\n- **Statut** : En ligne (0 min 51 s)\n- **Vidéo** : https://rapido-software.s3.eu-west-3.amazonaws.com/rapidosoftware/cms/bibliotheque/foodeatup-reception-tuto-v1\n\n**Description (à quoi ça sert)**\n\nContrôler chaque livraison au moment où elle arrive — DLC, température et conformité produit par produit — puis valider un contrôle à réception complet, daté et horodaté, sans registre papier.\n\n**Comment ça marche**\n\n1. Ouvrez une commande livrée pour voir son détail : fournisseur, référence et produits reçus\n2. Sur un produit, ouvrez le menu Action pour photographier la DLC, la saisir manuellement, noter la température ou scanner le code-barres\n3. Cliquez sur Contrôle à réception\n4. Renseignez la date, l'heure, une photo du bon de livraison et le fournisseur\n5. Indiquez l'état de la livraison — conforme ou non conforme — ajoutez un commentaire, puis passez à l'étape suivante\n\n**Astuce du chef** : Les actions rapides sur chaque produit (Photo DLC, DLC manuelle, Température, Scanner produit) sont indépendantes du contrôle global : utilisez-les au fil de la réception, produit par produit, avant même d'ouvrir le formulaire Contrôle à réception. Et si un produit pose problème, choisissez Non conforme dans le formulaire plutôt que de valider par réflexe — c'est ce statut qui déclenche votre traçabilité des non-conformités fournisseur.\n\n---",
              "correspondance": "texte",
              "confiance": 0.72
            },
            "tutorielModuleUrl": "https://tutoriel.foodeatup.com/module/haccp",
            "higgsfield": {
              "videoSourceUrl": null,
              "duree": "10 s",
              "format": "vertical 9:16",
              "source": null
            },
            "masterRapidoUrl": null
          },
          {
            "id": "EP048",
            "numero": 48,
            "saison": 2,
            "slug": "ep048-la-pyramide-de-sucre",
            "titre": "La pyramide de sucre",
            "module": "Configuration",
            "chapitre": "paramétrage initial",
            "accroche": "Ce que tu construis chaque jour.",
            "punchline": "Un système fragile finit toujours par tomber.",
            "resume": "Tu poses ta base une fois : établissement, TVA, zones, équipements. Tout le reste de FoodEatUp s'appuie dessus sans que tu y reviennes.",
            "statut": "a_produire",
            "dureeSecondes": null,
            "videoUrl": null,
            "reseaux": {
              "facebook": {
                "statut": "a_venir",
                "date": "2026-09-17",
                "heure": "12:00",
                "compte": "FoodEatUp",
                "format": "Vidéo native 9:16",
                "lienCta": "https://site.foodeatup.com/"
              },
              "instagram": {
                "statut": "a_venir",
                "date": "2026-09-17",
                "heure": "18:30",
                "compte": "foodeatup.cocuisinage",
                "format": "Reel 9:16",
                "lienCta": null
              },
              "tiktok": {
                "statut": "a_venir",
                "date": "2026-09-17",
                "heure": "19:00",
                "compte": "foodeatup",
                "format": "Vidéo 9:16",
                "lienCta": null
              },
              "linkedin": {
                "statut": "a_venir",
                "date": "2026-09-17",
                "heure": "08:00",
                "compte": "FoodEatUp",
                "format": "Vidéo native 9:16",
                "lienCta": "https://site.foodeatup.com/"
              },
              "youtube": {
                "statut": "a_venir",
                "date": "2026-09-17",
                "heure": "10:00",
                "compte": "@FoodEatUp",
                "format": "Short 9:16",
                "lienCta": "https://site.foodeatup.com/"
              }
            },
            "posterUrl": null,
            "datePrevue": "2026-09-17",
            "troisMots": "PARAMÉTRAGE INITIAL",
            "tutoriel": {
              "titre": "Paramétrer sa TVA FoodEatUp",
              "slug": "parametrer-sa-tva",
              "url": "https://tutoriel.foodeatup.com/tutoriel/parametrer-sa-tva",
              "module": "Configuration Boutique",
              "etape": "Profil, TVA & unités\n- **Statut** : En ligne (0 min 38 s)\n- **Vidéo** : https://rapido-software.s3.eu-west-3.amazonaws.com/rapidosoftware/cms/bibliotheque/foodeatup-tva-tuto-v1\n\n**Description (à quoi ça sert)**\n\nConfigurer les différents taux de TVA applicables à vos produits (taux normal, réduit...) pour que vos prix et factures soient toujours conformes.\n\n**Comment ça marche**\n\n1. Cliquez sur \"Ajouter TVA\"\n2. Donnez un nom à votre taux (ex: Taux réduit) et indiquez le pourcentage\n3. Validez avec \"Ajouter\" — le taux apparaît dans la liste\n4. Pour le modifier, cliquez sur le crayon dans la colonne Action\n5. Ajustez le pourcentage et cliquez sur \"Sauvegarder\"\n\n**Astuce du chef** : Pensez à nommer vos taux clairement (« Taux réduit 5,5% », « Taux normal 20% ») : ça évite les confusions quand vous les associerez à vos produits plus tard.\n\n---",
              "correspondance": "texte",
              "confiance": 0.67
            },
            "tutorielModuleUrl": "https://tutoriel.foodeatup.com/module/configuration",
            "higgsfield": {
              "videoSourceUrl": null,
              "duree": "10 s",
              "format": "vertical 9:16",
              "source": null
            },
            "masterRapidoUrl": null
          },
          {
            "id": "EP049",
            "numero": 49,
            "saison": 2,
            "slug": "ep049-le-chien-du-pass",
            "titre": "Le chien du pass",
            "module": "HACCP",
            "chapitre": "Relevé de température",
            "accroche": "Il envoie plus vite que ton pass.",
            "punchline": "Un KDS, et la cuisine avance toute seule.",
            "resume": "Tu relèves tes frigos depuis ton téléphone. La mesure est datée, signée, archivée. Un contrôle, et tu sors trois mois d'historique en un clic.",
            "statut": "a_produire",
            "dureeSecondes": null,
            "videoUrl": null,
            "reseaux": {
              "facebook": {
                "statut": "a_venir",
                "date": "2026-09-18",
                "heure": "12:00",
                "compte": "FoodEatUp",
                "format": "Vidéo native 9:16",
                "lienCta": "https://site.foodeatup.com/"
              },
              "instagram": {
                "statut": "a_venir",
                "date": "2026-09-18",
                "heure": "18:30",
                "compte": "foodeatup.cocuisinage",
                "format": "Reel 9:16",
                "lienCta": null
              },
              "tiktok": {
                "statut": "a_venir",
                "date": "2026-09-18",
                "heure": "19:00",
                "compte": "foodeatup",
                "format": "Vidéo 9:16",
                "lienCta": null
              },
              "linkedin": {
                "statut": "a_venir",
                "date": "2026-09-18",
                "heure": "08:00",
                "compte": "FoodEatUp",
                "format": "Vidéo native 9:16",
                "lienCta": "https://site.foodeatup.com/"
              },
              "youtube": {
                "statut": "a_venir",
                "date": "2026-09-18",
                "heure": "10:00",
                "compte": "@FoodEatUp",
                "format": "Short 9:16",
                "lienCta": "https://site.foodeatup.com/"
              }
            },
            "posterUrl": null,
            "datePrevue": "2026-09-18",
            "troisMots": "RELEVÉ DE TEMPÉRATURE",
            "tutoriel": {
              "titre": "Relever une température d'équipement",
              "slug": "relever-une-temperature-equipement",
              "url": "https://tutoriel.foodeatup.com/tutoriel/relever-une-temperature-equipement",
              "module": "Hygiène & HACCP",
              "etape": "Températures & équipements\n- **Statut** : En ligne (0 min 38 s)\n- **Vidéo** : https://rapido-software.s3.eu-west-3.amazonaws.com/rapidosoftware/cms/bibliotheque/foodeatup-temperature-tuto-v1.mp4\n\n**Description (à quoi ça sert)**\n\nTenir votre registre de températures au moment du relevé, pas le soir de mémoire ni sur une feuille scotchée à la porte du frigo. Chaque valeur saisie est datée, horodatée et rattachée à son équipement, puis confrontée automatiquement à la plage cible que vous avez définie : ce qui sort des clous est marqué non conforme immédiatement, pendant que vous êtes encore devant l'équipement et que vous pouvez agir. C'est ce qui transforme un contrôle de routine en historique HACCP présentable à un inspecteur.\n\n**Comment ça marche**\n\n1. Ouvrez Hygiène & HACCP puis \"Températures\" : l'onglet Équipements liste vos frigos, congélateurs et chambres froides\n2. Chaque ligne affiche la plage cible de l'équipement — ici Frigo 5, min 0 °C, max 4 °C\n3. Ajustez la valeur relevée avec les boutons − et + de la colonne Température\n4. Cliquez sur \"Enregistrer les relevés de température\" en bas de la page\n5. Confirmez dans la fenêtre \"Enregistrer les relevés ?\", qui récapitule le nombre d'équipements et de plats modifiés\n6. Validez le message \"Enregistré ! Les relevés ont été sauvegardés avec succès.\"\n7. Les compteurs du jour se recalculent aussitôt : Total aujourd'hui, Conformes, Alertes et Non conformes\n8. Un relevé hors plage bascule directement en non conforme — 9 °C pour un maximum de 4 °C part en non conforme, sans intervention de votre part\n\n**Astuce du chef** : Relevez toujours aux mêmes moments — ouverture et fermeture — plutôt que « quand on y pense » : un historique régulier vaut bien mieux qu'un historique dense mais troué, c'est la régularité que regarde l'inspecteur. Et ne « corrigez » jamais une valeur hors plage pour faire propre : un 9 °C tracé, daté et suivi d'une action est votre meilleure défense, alors qu'un 4 °C confortable sur un frigo qui dérive ne protège personne — surtout pas vos stocks.\n\n---",
              "correspondance": "texte",
              "confiance": 0.73
            },
            "tutorielModuleUrl": "https://tutoriel.foodeatup.com/module/haccp",
            "higgsfield": {
              "videoSourceUrl": null,
              "duree": "10 s",
              "format": "vertical 9:16",
              "source": null
            },
            "masterRapidoUrl": null
          },
          {
            "id": "EP050",
            "numero": 50,
            "saison": 2,
            "slug": "ep050-la-casserole-brulante",
            "titre": "La casserole brûlante",
            "module": "HACCP",
            "chapitre": "Équipements",
            "accroche": "Apprendre sur le tas.",
            "punchline": "Il y a plus rapide pour former quelqu'un.",
            "resume": "Chaque frigo, chaque chambre froide est déclaré avec ses seuils. Hors zone, tu es alerté. Tu sauves la marchandise avant de la jeter.",
            "statut": "a_produire",
            "dureeSecondes": null,
            "videoUrl": null,
            "reseaux": {
              "facebook": {
                "statut": "a_venir",
                "date": "2026-09-19",
                "heure": "12:00",
                "compte": "FoodEatUp",
                "format": "Vidéo native 9:16",
                "lienCta": "https://site.foodeatup.com/"
              },
              "instagram": {
                "statut": "a_venir",
                "date": "2026-09-19",
                "heure": "18:30",
                "compte": "foodeatup.cocuisinage",
                "format": "Reel 9:16",
                "lienCta": null
              },
              "tiktok": {
                "statut": "a_venir",
                "date": "2026-09-19",
                "heure": "19:00",
                "compte": "foodeatup",
                "format": "Vidéo 9:16",
                "lienCta": null
              },
              "linkedin": {
                "statut": "a_venir",
                "date": "2026-09-19",
                "heure": "08:00",
                "compte": "FoodEatUp",
                "format": "Vidéo native 9:16",
                "lienCta": "https://site.foodeatup.com/"
              },
              "youtube": {
                "statut": "a_venir",
                "date": "2026-09-19",
                "heure": "10:00",
                "compte": "@FoodEatUp",
                "format": "Short 9:16",
                "lienCta": "https://site.foodeatup.com/"
              }
            },
            "posterUrl": null,
            "datePrevue": "2026-09-19",
            "troisMots": "ÉQUIPEMENTS",
            "tutoriel": {
              "titre": "Déclarer ses équipements (Module HACCP)",
              "slug": "declarer-ses-equipements",
              "url": "https://tutoriel.foodeatup.com/tutoriel/declarer-ses-equipements",
              "module": "Hygiène & HACCP",
              "etape": "Températures & équipements\n- **Statut** : En ligne (0 min 51 s)\n- **Vidéo** : https://rapido-software.s3.eu-west-3.amazonaws.com/rapidosoftware/cms/bibliotheque/foodeatup-equipements-tuto-v1\n\n**Description (à quoi ça sert)**\n\nDéclarer chaque frigo, congélateur ou chambre froide de votre cuisine en quelques clics, avec sa plage de température réglementaire appliquée automatiquement selon le type choisi — la base indispensable avant de démarrer vos relevés de température HACCP.\n\n**Comment ça marche**\n\n1. Ouvrez le module HACCP > Températures, onglet \"Équipements\"\n2. Cliquez sur \"+ Ajouter un équipement\"\n3. Donnez-lui un nom, puis choisissez son type : Congélateur, Frigo ou Chaud — la plage de température réglementaire s'affiche automatiquement dans l'aperçu\n4. Ajoutez un emplacement (optionnel), comme \"cuisine\", puis cliquez sur \"Enregistrer\"\n5. Pour le modifier : cliquez sur le crayon dans la colonne Actions, ajustez les champs, puis \"Enregistrer\"\n6. Pour le supprimer : cliquez sur la corbeille puis confirmez avec \"Oui, supprimer !\"\n\n**Astuce du chef** : Le type choisi (Congélateur, Frigo, Chaud) fixe automatiquement la plage de température réglementaire de l'équipement — c'est elle qui détermine ensuite si un relevé est \"conforme\" ou \"non conforme\". Un mauvais type sélectionné par réflexe peut donc déclencher de fausses alertes non conformes sur un équipement qui fonctionne pourtant normalement : vérifiez toujours le type avant d'enregistrer. Et ne vous inquiétez pas pour la suppression : FoodEatUp demande toujours une confirmation explicite (\"Êtes-vous sûr ?\") avant de retirer un équipement, impossible de le supprimer par un clic accidentel.\n\n---",
              "correspondance": "texte",
              "confiance": 0.63
            },
            "tutorielModuleUrl": "https://tutoriel.foodeatup.com/module/haccp",
            "higgsfield": {
              "videoSourceUrl": null,
              "duree": "10 s",
              "format": "vertical 9:16",
              "source": null
            },
            "masterRapidoUrl": null
          },
          {
            "id": "EP051",
            "numero": 51,
            "saison": 2,
            "slug": "ep051-la-mousse",
            "titre": "La mousse",
            "module": "HACCP",
            "chapitre": "Étiquettes DLC",
            "accroche": "Un mauvais réglage. Une seule fois.",
            "punchline": "Les process, ça évite ça.",
            "resume": "Étiquette produite, date de fabrication, DLC calculée. Ton bac étiqueté n'est plus un pari.",
            "statut": "a_produire",
            "dureeSecondes": null,
            "videoUrl": null,
            "reseaux": {
              "facebook": {
                "statut": "a_venir",
                "date": "2026-09-20",
                "heure": "12:00",
                "compte": "FoodEatUp",
                "format": "Vidéo native 9:16",
                "lienCta": "https://site.foodeatup.com/"
              },
              "instagram": {
                "statut": "a_venir",
                "date": "2026-09-20",
                "heure": "18:30",
                "compte": "foodeatup.cocuisinage",
                "format": "Reel 9:16",
                "lienCta": null
              },
              "tiktok": {
                "statut": "a_venir",
                "date": "2026-09-20",
                "heure": "19:00",
                "compte": "foodeatup",
                "format": "Vidéo 9:16",
                "lienCta": null
              },
              "linkedin": {
                "statut": "a_venir",
                "date": "2026-09-20",
                "heure": "08:00",
                "compte": "FoodEatUp",
                "format": "Vidéo native 9:16",
                "lienCta": "https://site.foodeatup.com/"
              },
              "youtube": {
                "statut": "a_venir",
                "date": "2026-09-20",
                "heure": "10:00",
                "compte": "@FoodEatUp",
                "format": "Short 9:16",
                "lienCta": "https://site.foodeatup.com/"
              }
            },
            "posterUrl": null,
            "datePrevue": "2026-09-20",
            "troisMots": "ÉTIQUETTES DLC",
            "tutoriel": {
              "titre": "Imprimer ses étiquettes (vente & stockage) FoodEatUp",
              "slug": "imprimer-ses-etiquettes",
              "url": "https://tutoriel.foodeatup.com/tutoriel/imprimer-ses-etiquettes",
              "module": "Hygiène & HACCP",
              "etape": "Étiquetage & DLC\n- **Statut** : En ligne (1 min 02 s)\n- **Vidéo** : https://rapido-software.s3.eu-west-3.amazonaws.com/rapidosoftware/cms/bibliotheque/imprimer-ses-etiquettes-v1\n\n**Description (à quoi ça sert)**\n\nGénérer en quelques clics des étiquettes de vente ou de stockage conformes HACCP - DLC, numéro de lot, code-barres et équipement de stockage calculés automatiquement à partir de votre catalogue - pour tracer chaque produit sans ressaisie manuelle et être prêt en cas de contrôle sanitaire.\n\n**Comment ça marche**\n\n1. Depuis le module Traçabilité > Étiqueteuse, sélectionnez le ou les produits à étiqueter.\n2. Cliquez sur \"Imprimer [n] étiquette(s)\" pour ouvrir la fiche Étiqueteuse.\n3. Renseignez la date et le type d'étiquette (Fait/ouvert, Frais, Surgelé, Prêt à manger, Vente) : le produit est déjà pré-rempli.\n4. La DLC, le numéro de lot et le code-barres de vente sont calculés automatiquement (modifiables si besoin).\n5. Choisissez le nombre d'étiquettes et l'équipement de stockage associé (ex : frigo 0°C à 4°C).\n6. Cliquez sur \"Créer les étiquettes\" : elles s'affichent aussitôt en aperçu, prêtes pour impression.\n7. Cliquez sur \"Valider -> Historique\" pour les ajouter à votre historique de traçabilité HACCP.\n\n**Astuce du chef** : Le bouton \"Créer les étiquettes\" ne s'active qu'une fois l'équipement de stockage renseigné : c'est volontaire, une étiquette sans lieu de stockage ne sert à rien en traçabilité. Imprimez toujours la quantité exacte de portions ou d'unités produites plutôt qu'une seule étiquette réutilisée - chaque étiquette avec son propre numéro de lot vous permet de retracer précisément un incident si besoin.\n\n---",
              "correspondance": "texte",
              "confiance": 0.54
            },
            "tutorielModuleUrl": "https://tutoriel.foodeatup.com/module/haccp",
            "higgsfield": {
              "videoSourceUrl": null,
              "duree": "10 s",
              "format": "vertical 9:16",
              "source": null
            },
            "masterRapidoUrl": null
          },
          {
            "id": "EP052",
            "numero": 52,
            "saison": 2,
            "slug": "ep052-le-tablier-coince",
            "titre": "Le tablier coincé",
            "module": "HACCP",
            "chapitre": "Traçabilité",
            "accroche": "Encore un truc qui te retient.",
            "punchline": "Enlève-les tous, un par un.",
            "resume": "Chaque lot reçu est rattaché à ce que tu produis. En cas de rappel, tu remontes la chaîne en quelques secondes.",
            "statut": "a_produire",
            "dureeSecondes": null,
            "videoUrl": null,
            "reseaux": {
              "facebook": {
                "statut": "a_venir",
                "date": "2026-09-21",
                "heure": "12:00",
                "compte": "FoodEatUp",
                "format": "Vidéo native 9:16",
                "lienCta": "https://site.foodeatup.com/"
              },
              "instagram": {
                "statut": "a_venir",
                "date": "2026-09-21",
                "heure": "18:30",
                "compte": "foodeatup.cocuisinage",
                "format": "Reel 9:16",
                "lienCta": null
              },
              "tiktok": {
                "statut": "a_venir",
                "date": "2026-09-21",
                "heure": "19:00",
                "compte": "foodeatup",
                "format": "Vidéo 9:16",
                "lienCta": null
              },
              "linkedin": {
                "statut": "a_venir",
                "date": "2026-09-21",
                "heure": "08:00",
                "compte": "FoodEatUp",
                "format": "Vidéo native 9:16",
                "lienCta": "https://site.foodeatup.com/"
              },
              "youtube": {
                "statut": "a_venir",
                "date": "2026-09-21",
                "heure": "10:00",
                "compte": "@FoodEatUp",
                "format": "Short 9:16",
                "lienCta": "https://site.foodeatup.com/"
              }
            },
            "posterUrl": null,
            "datePrevue": "2026-09-21",
            "troisMots": "TRAÇABILITÉ",
            "tutoriel": {
              "titre": "Créer une traçabilité complète",
              "slug": "creer-une-tracabilite-complete",
              "url": "https://tutoriel.foodeatup.com/tutoriel/creer-une-tracabilite-complete",
              "module": "Hygiène & HACCP",
              "etape": "Traçabilité\n- **Statut** : En ligne (0 min 52 s)\n- **Vidéo** : https://rapido-software.s3.eu-west-3.amazonaws.com/rapidosoftware/cms/bibliotheque/foodeatup-tracabilite-tuto-v1\n\n**Description (à quoi ça sert)**\n\nUn suivi de traçabilité complet et structuré, produit par produit — sélection du produit, numéro de lot, DLC photographiée et remarques — pour répondre aux exigences HACCP sans ressaisie ni papier volant, à la différence de la traçabilité simplifiée réservée aux plats sans référence précise.\n\n**Comment ça marche**\n\n1. Ouvrez le module \"Traçabilité\" depuis le menu principal de FoodEatUp\n2. Cliquez sur la carte \"Traçabilité complète\" (icône document), à droite de \"Traçabilité simplifiée\"\n3. Cliquez sur \"Ajouter des produits à la traçabilité\" et sélectionnez vos produits dans la liste\n4. Cliquez sur le statut \"non complété\" d'un produit pour ouvrir sa fiche, puis prenez en photo la DLC directement depuis l'application\n5. Renseignez la quantité, la DLC, le numéro de lot et une remarque, puis validez : le statut passe à Complété\n6. Cliquez sur \"Enregistrer\" (ou \"Enregistrer et imprimer\"), confirmez la date et l'heure : la traçabilité est ajoutée à votre historique\n\n**Astuce du chef** : Prenez la photo de la DLC au moment où vous ouvrez le produit, pas après : une fois l'emballage jeté, le numéro de lot est perdu. Et si le statut reste sur « non complété », ce n'est pas une erreur — c'est un rappel actif pour finir la fiche avant le prochain contrôle.\n\n---",
              "correspondance": "texte",
              "confiance": 0.54
            },
            "tutorielModuleUrl": "https://tutoriel.foodeatup.com/module/haccp",
            "higgsfield": {
              "videoSourceUrl": null,
              "duree": "10 s",
              "format": "vertical 9:16",
              "source": null
            },
            "masterRapidoUrl": null
          },
          {
            "id": "EP053",
            "numero": 53,
            "saison": 2,
            "slug": "ep053-la-file-et-la-salle-vide",
            "titre": "La file et la salle vide",
            "module": "HACCP",
            "chapitre": "Réception fournisseur",
            "accroche": "Complet dehors. Vide dedans.",
            "punchline": "Ta salle et ta file devraient se parler.",
            "resume": "Contrôle à réception : température, aspect, quantité, non-conformités. Tout part dans le dossier HACCP tout seul.",
            "statut": "a_produire",
            "dureeSecondes": null,
            "videoUrl": null,
            "reseaux": {
              "facebook": {
                "statut": "a_venir",
                "date": "2026-09-22",
                "heure": "12:00",
                "compte": "FoodEatUp",
                "format": "Vidéo native 9:16",
                "lienCta": "https://site.foodeatup.com/"
              },
              "instagram": {
                "statut": "a_venir",
                "date": "2026-09-22",
                "heure": "18:30",
                "compte": "foodeatup.cocuisinage",
                "format": "Reel 9:16",
                "lienCta": null
              },
              "tiktok": {
                "statut": "a_venir",
                "date": "2026-09-22",
                "heure": "19:00",
                "compte": "foodeatup",
                "format": "Vidéo 9:16",
                "lienCta": null
              },
              "linkedin": {
                "statut": "a_venir",
                "date": "2026-09-22",
                "heure": "08:00",
                "compte": "FoodEatUp",
                "format": "Vidéo native 9:16",
                "lienCta": "https://site.foodeatup.com/"
              },
              "youtube": {
                "statut": "a_venir",
                "date": "2026-09-22",
                "heure": "10:00",
                "compte": "@FoodEatUp",
                "format": "Short 9:16",
                "lienCta": "https://site.foodeatup.com/"
              }
            },
            "posterUrl": null,
            "datePrevue": "2026-09-22",
            "troisMots": "RÉCEPTION FOURNISSEUR",
            "tutoriel": {
              "titre": "Contrôler à réception de vos livraisons (Module HACCP)",
              "slug": "controler-reception-livraisons",
              "url": "https://tutoriel.foodeatup.com/tutoriel/controler-reception-livraisons",
              "module": "Hygiène & HACCP",
              "etape": "Contrôle à réception\n- **Statut** : En ligne (0 min 51 s)\n- **Vidéo** : https://rapido-software.s3.eu-west-3.amazonaws.com/rapidosoftware/cms/bibliotheque/foodeatup-reception-tuto-v1\n\n**Description (à quoi ça sert)**\n\nContrôler chaque livraison au moment où elle arrive — DLC, température et conformité produit par produit — puis valider un contrôle à réception complet, daté et horodaté, sans registre papier.\n\n**Comment ça marche**\n\n1. Ouvrez une commande livrée pour voir son détail : fournisseur, référence et produits reçus\n2. Sur un produit, ouvrez le menu Action pour photographier la DLC, la saisir manuellement, noter la température ou scanner le code-barres\n3. Cliquez sur Contrôle à réception\n4. Renseignez la date, l'heure, une photo du bon de livraison et le fournisseur\n5. Indiquez l'état de la livraison — conforme ou non conforme — ajoutez un commentaire, puis passez à l'étape suivante\n\n**Astuce du chef** : Les actions rapides sur chaque produit (Photo DLC, DLC manuelle, Température, Scanner produit) sont indépendantes du contrôle global : utilisez-les au fil de la réception, produit par produit, avant même d'ouvrir le formulaire Contrôle à réception. Et si un produit pose problème, choisissez Non conforme dans le formulaire plutôt que de valider par réflexe — c'est ce statut qui déclenche votre traçabilité des non-conformités fournisseur.\n\n---",
              "correspondance": "texte",
              "confiance": 0.55
            },
            "tutorielModuleUrl": "https://tutoriel.foodeatup.com/module/haccp",
            "higgsfield": {
              "videoSourceUrl": null,
              "duree": "10 s",
              "format": "vertical 9:16",
              "source": null
            },
            "masterRapidoUrl": null
          },
          {
            "id": "EP054",
            "numero": 54,
            "saison": 2,
            "slug": "ep054-le-pois",
            "titre": "Le pois",
            "module": "HACCP",
            "chapitre": "Plan de nettoyage",
            "accroche": "Ton prix ne raconte pas ton coût.",
            "punchline": "Marge réelle par plat. Ça change les décisions.",
            "resume": "Tes zones et tes postes de nettoyage sont listés. Qui a fait quoi, quand, c'est enregistré. Le plan de nettoyage vit vraiment.",
            "statut": "a_produire",
            "dureeSecondes": null,
            "videoUrl": null,
            "reseaux": {
              "facebook": {
                "statut": "a_venir",
                "date": "2026-09-23",
                "heure": "12:00",
                "compte": "FoodEatUp",
                "format": "Vidéo native 9:16",
                "lienCta": "https://site.foodeatup.com/"
              },
              "instagram": {
                "statut": "a_venir",
                "date": "2026-09-23",
                "heure": "18:30",
                "compte": "foodeatup.cocuisinage",
                "format": "Reel 9:16",
                "lienCta": null
              },
              "tiktok": {
                "statut": "a_venir",
                "date": "2026-09-23",
                "heure": "19:00",
                "compte": "foodeatup",
                "format": "Vidéo 9:16",
                "lienCta": null
              },
              "linkedin": {
                "statut": "a_venir",
                "date": "2026-09-23",
                "heure": "08:00",
                "compte": "FoodEatUp",
                "format": "Vidéo native 9:16",
                "lienCta": "https://site.foodeatup.com/"
              },
              "youtube": {
                "statut": "a_venir",
                "date": "2026-09-23",
                "heure": "10:00",
                "compte": "@FoodEatUp",
                "format": "Short 9:16",
                "lienCta": "https://site.foodeatup.com/"
              }
            },
            "posterUrl": null,
            "datePrevue": "2026-09-23",
            "troisMots": "PLAN DE NETTOYAGE",
            "tutoriel": {
              "titre": "Ajouter et paramétrer son plan de nettoyage (Zones)",
              "slug": "parametrer-son-plan-de-nettoyage",
              "url": "https://tutoriel.foodeatup.com/tutoriel/parametrer-son-plan-de-nettoyage",
              "module": "Hygiène & HACCP",
              "etape": "Hygiène & nettoyage\n- **Statut** : En ligne (0 min 40 s)\n- **Vidéo** : https://rapido-software.s3.eu-west-3.amazonaws.com/rapidosoftware/cms/bibliotheque/foodeatup-nettoyage-tuto-v1\n\n**Description (à quoi ça sert)**\n\nOrganiser le nettoyage de votre cuisine par zones et postes, avec un historique daté de chaque action réalisée — la base de votre conformité HACCP.\n\n**Comment ça marche**\n\n1. Depuis Hygiène, ouvrez Plan Nettoyage\n2. Cliquez sur Ajouter une zone de nettoyage\n3. Donnez-lui un nom et une description, puis enregistrez\n4. Votre zone est créée avec ses postes de nettoyage\n5. Marquez une action de nettoyage réalisée en un clic, avec la date et l'heure\n\n**Astuce du chef** : Créez une zone par fréquence de nettoyage (quotidien, hebdomadaire, mensuel) plutôt qu'une seule zone générale : vous repérez en un coup d'œil ce qui a été fait aujourd'hui et ce qui attend encore son passage de la semaine ou du mois. Le marquage quotidien des actions par votre équipe fait l'objet d'un tutoriel dédié (module HACCP #11).\n\n---",
              "correspondance": "texte",
              "confiance": 0.69
            },
            "tutorielModuleUrl": "https://tutoriel.foodeatup.com/module/haccp",
            "higgsfield": {
              "videoSourceUrl": null,
              "duree": "10 s",
              "format": "vertical 9:16",
              "source": null
            },
            "masterRapidoUrl": null
          },
          {
            "id": "EP055",
            "numero": 55,
            "saison": 2,
            "slug": "ep055-le-ventilateur",
            "titre": "Le ventilateur",
            "module": "HACCP",
            "chapitre": "Checklists hygiène",
            "accroche": "Ta compta, au format papier.",
            "punchline": "Scanne. Classe. Oublie.",
            "resume": "Tu crées ta checklist une fois, l'équipe la valide chaque jour. Ce qui est coché est daté et signé.",
            "statut": "a_produire",
            "dureeSecondes": null,
            "videoUrl": null,
            "reseaux": {
              "facebook": {
                "statut": "a_venir",
                "date": "2026-09-24",
                "heure": "12:00",
                "compte": "FoodEatUp",
                "format": "Vidéo native 9:16",
                "lienCta": "https://site.foodeatup.com/"
              },
              "instagram": {
                "statut": "a_venir",
                "date": "2026-09-24",
                "heure": "18:30",
                "compte": "foodeatup.cocuisinage",
                "format": "Reel 9:16",
                "lienCta": null
              },
              "tiktok": {
                "statut": "a_venir",
                "date": "2026-09-24",
                "heure": "19:00",
                "compte": "foodeatup",
                "format": "Vidéo 9:16",
                "lienCta": null
              },
              "linkedin": {
                "statut": "a_venir",
                "date": "2026-09-24",
                "heure": "08:00",
                "compte": "FoodEatUp",
                "format": "Vidéo native 9:16",
                "lienCta": "https://site.foodeatup.com/"
              },
              "youtube": {
                "statut": "a_venir",
                "date": "2026-09-24",
                "heure": "10:00",
                "compte": "@FoodEatUp",
                "format": "Short 9:16",
                "lienCta": "https://site.foodeatup.com/"
              }
            },
            "posterUrl": null,
            "datePrevue": "2026-09-24",
            "troisMots": "CHECKLISTS HYGIÈNE",
            "tutoriel": {
              "titre": "Créer sa check-list hygiène FoodEatUp",
              "slug": "creer-sa-checklist-hygiene",
              "url": "https://tutoriel.foodeatup.com/tutoriel/creer-sa-checklist-hygiene",
              "module": "Hygiène & HACCP",
              "etape": "Hygiène & nettoyage\n- **Statut** : En ligne (0 min 43 s)\n- **Vidéo** : https://rapido-software.s3.eu-west-3.amazonaws.com/rapidosoftware/cms/bibliotheque/foodeatup-checklist-hygiene-tuto-v1\n\n**Description (à quoi ça sert)**\n\nCréer vos propres points de contrôle hygiène (au-delà des points par défaut) et les valider directement depuis l'app, avec date, heure et zone horodatées automatiquement — une trace claire et datée de chaque contrôle, prête en cas d'inspection HACCP.\n\n**Comment ça marche**\n\n1. Depuis Hygiène, ouvrez Checklist hygiène\n2. Cliquez sur \"Ajouter une checklist\"\n3. Donnez-lui un nom, une catégorie (Hygiène du personnel ou État des locaux) et une description, puis cliquez sur \"Créer\"\n4. Elle apparaît aussitôt dans la liste, avec les points de contrôle par défaut de sa catégorie\n5. Ouvrez-la pour la valider : choisissez la zone contrôlée, cochez Oui, Non ou Non évalué, ajoutez un commentaire si besoin, puis cliquez sur \"Valider\"\n\n**Astuce du chef** : Complétez la validation au moment du contrôle réel, pas après coup — la date et l'heure sont horodatées automatiquement dès l'ouverture de la fiche, et la zone contrôlée permet de retrouver l'historique précis en cas d'inspection.\n\n---",
              "correspondance": "texte",
              "confiance": 0.77
            },
            "tutorielModuleUrl": "https://tutoriel.foodeatup.com/module/haccp",
            "higgsfield": {
              "videoSourceUrl": null,
              "duree": "10 s",
              "format": "vertical 9:16",
              "source": null
            },
            "masterRapidoUrl": null
          },
          {
            "id": "EP056",
            "numero": 56,
            "saison": 2,
            "slug": "ep056-le-passager-clandestin",
            "titre": "Le passager clandestin",
            "module": "HACCP",
            "chapitre": "Historique",
            "accroche": "Il y a toujours un truc en trop.",
            "punchline": "Ou en moins. Et tu le vois trop tard.",
            "resume": "Tes relevés, tes réceptions et tes validations sont conservés. Le jour du contrôle, tu ne cherches rien.",
            "statut": "a_produire",
            "dureeSecondes": null,
            "videoUrl": null,
            "reseaux": {
              "facebook": {
                "statut": "a_venir",
                "date": "2026-09-25",
                "heure": "12:00",
                "compte": "FoodEatUp",
                "format": "Vidéo native 9:16",
                "lienCta": "https://site.foodeatup.com/"
              },
              "instagram": {
                "statut": "a_venir",
                "date": "2026-09-25",
                "heure": "18:30",
                "compte": "foodeatup.cocuisinage",
                "format": "Reel 9:16",
                "lienCta": null
              },
              "tiktok": {
                "statut": "a_venir",
                "date": "2026-09-25",
                "heure": "19:00",
                "compte": "foodeatup",
                "format": "Vidéo 9:16",
                "lienCta": null
              },
              "linkedin": {
                "statut": "a_venir",
                "date": "2026-09-25",
                "heure": "08:00",
                "compte": "FoodEatUp",
                "format": "Vidéo native 9:16",
                "lienCta": "https://site.foodeatup.com/"
              },
              "youtube": {
                "statut": "a_venir",
                "date": "2026-09-25",
                "heure": "10:00",
                "compte": "@FoodEatUp",
                "format": "Short 9:16",
                "lienCta": "https://site.foodeatup.com/"
              }
            },
            "posterUrl": null,
            "datePrevue": "2026-09-25",
            "troisMots": "HISTORIQUE",
            "tutoriel": {
              "titre": "historique",
              "slug": "retrouver-historique-plats-sondes",
              "url": "https://tutoriel.foodeatup.com/tutoriel/retrouver-historique-plats-sondes",
              "module": "Hygiène & HACCP",
              "etape": "Températures & équipements\n- **Statut** : En ligne (0 min 56 s)\n- **Vidéo** : https://rapido-software.s3.eu-west-3.amazonaws.com/rapidosoftware/cms/bibliotheque/foodeatup-plats-sondes-historique-tuto-v1\n\n**Description (à quoi ça sert)**\n\nRetrouver en un clic l'historique complet de vos contrôles de température à cœur, plat par plat : de quoi prouver votre conformité HACCP en cas de contrôle sanitaire, sans fouiller dans du papier.\n\n**Comment ça marche**\n\n1. Depuis Production > Températures, ouvrez l'onglet Plats et ajustez la température à cœur de chaque plat sondé.\n2. Cliquez sur Enregistrer les relevés de température, puis confirmez : vos relevés sont sauvegardés aussitôt.\n3. Ouvrez Historique dans le menu principal pour retrouver tous vos relevés passés.\n4. Consultez les 6 indicateurs clés : total des relevés, conformes, non conformes, alertes, équipements et plats.\n5. Basculez sur l'onglet Plats pour voir chaque sonde à cœur : température, seuil réglementaire, date/heure et responsable.\n6. Recherchez un plat, filtrez par statut ou par date, et exportez tout en CSV pour votre suivi HACCP.\n\n**Astuce du chef** : Filtrez régulièrement sur le statut Non conforme pour repérer vite les plats qui dérivent sous le seuil de sécurité, avant qu'un contrôle sanitaire ne le fasse à votre place.\n\n---",
              "correspondance": "texte",
              "confiance": 1.15
            },
            "tutorielModuleUrl": "https://tutoriel.foodeatup.com/module/haccp",
            "higgsfield": {
              "videoSourceUrl": null,
              "duree": "10 s",
              "format": "vertical 9:16",
              "source": null
            },
            "masterRapidoUrl": null
          },
          {
            "id": "EP057",
            "numero": 57,
            "saison": 2,
            "slug": "ep057-les-pieces",
            "titre": "Les pièces",
            "module": "HACCP",
            "chapitre": "Alertes",
            "accroche": "La clôture de caisse.",
            "punchline": "Un Z propre, en une minute.",
            "resume": "Une température hors seuil déclenche une alerte immédiate. Tu réagis pendant le service, pas le lendemain.",
            "statut": "a_produire",
            "dureeSecondes": null,
            "videoUrl": null,
            "reseaux": {
              "facebook": {
                "statut": "a_venir",
                "date": "2026-09-26",
                "heure": "12:00",
                "compte": "FoodEatUp",
                "format": "Vidéo native 9:16",
                "lienCta": "https://site.foodeatup.com/"
              },
              "instagram": {
                "statut": "a_venir",
                "date": "2026-09-26",
                "heure": "18:30",
                "compte": "foodeatup.cocuisinage",
                "format": "Reel 9:16",
                "lienCta": null
              },
              "tiktok": {
                "statut": "a_venir",
                "date": "2026-09-26",
                "heure": "19:00",
                "compte": "foodeatup",
                "format": "Vidéo 9:16",
                "lienCta": null
              },
              "linkedin": {
                "statut": "a_venir",
                "date": "2026-09-26",
                "heure": "08:00",
                "compte": "FoodEatUp",
                "format": "Vidéo native 9:16",
                "lienCta": "https://site.foodeatup.com/"
              },
              "youtube": {
                "statut": "a_venir",
                "date": "2026-09-26",
                "heure": "10:00",
                "compte": "@FoodEatUp",
                "format": "Short 9:16",
                "lienCta": "https://site.foodeatup.com/"
              }
            },
            "posterUrl": null,
            "datePrevue": "2026-09-26",
            "troisMots": "ALERTES",
            "tutoriel": null,
            "tutorielModuleUrl": "https://tutoriel.foodeatup.com/module/haccp",
            "tutorielManquant": "Ce chapitre n'a pas encore sa fiche dans l'Academy.",
            "higgsfield": {
              "videoSourceUrl": null,
              "duree": "10 s",
              "format": "vertical 9:16",
              "source": null
            },
            "masterRapidoUrl": null
          },
          {
            "id": "EP058",
            "numero": 58,
            "saison": 2,
            "slug": "ep058-les-bougies",
            "titre": "Les bougies",
            "module": "HACCP",
            "chapitre": "Rôles",
            "accroche": "L'anniversaire de la table 12.",
            "punchline": "Anticiper, c'est aussi ça, le service.",
            "resume": "Chaque agent signe ses propres relevés. La responsabilité est claire, sans paperasse supplémentaire.",
            "statut": "bloque",
            "dureeSecondes": null,
            "videoUrl": null,
            "reseaux": {
              "facebook": {
                "statut": "a_venir",
                "date": null,
                "heure": "12:00",
                "compte": "FoodEatUp",
                "format": "Vidéo native 9:16",
                "lienCta": "https://site.foodeatup.com/"
              },
              "instagram": {
                "statut": "a_venir",
                "date": null,
                "heure": "18:30",
                "compte": "foodeatup.cocuisinage",
                "format": "Reel 9:16",
                "lienCta": null
              },
              "tiktok": {
                "statut": "a_venir",
                "date": null,
                "heure": "19:00",
                "compte": "foodeatup",
                "format": "Vidéo 9:16",
                "lienCta": null
              },
              "linkedin": {
                "statut": "a_venir",
                "date": null,
                "heure": "08:00",
                "compte": "FoodEatUp",
                "format": "Vidéo native 9:16",
                "lienCta": "https://site.foodeatup.com/"
              },
              "youtube": {
                "statut": "a_venir",
                "date": null,
                "heure": "10:00",
                "compte": "@FoodEatUp",
                "format": "Short 9:16",
                "lienCta": "https://site.foodeatup.com/"
              }
            },
            "blocage": "Le chapitre correspondant n'a pas encore de vidéo dans le Drive interne.",
            "posterUrl": null,
            "datePrevue": null,
            "troisMots": "RÔLES",
            "tutoriel": null,
            "tutorielModuleUrl": "https://tutoriel.foodeatup.com/module/haccp",
            "tutorielManquant": "Ce chapitre n'a pas encore sa fiche dans l'Academy.",
            "higgsfield": {
              "videoSourceUrl": null,
              "duree": "10 s",
              "format": "vertical 9:16",
              "source": null
            },
            "masterRapidoUrl": null
          },
          {
            "id": "EP059",
            "numero": 59,
            "saison": 2,
            "slug": "ep059-l-ardoise",
            "titre": "L'ardoise",
            "module": "HACCP",
            "chapitre": "Non-conformité",
            "accroche": "Ta com', chaque matin.",
            "punchline": "Il y a plus solide qu'une ardoise.",
            "resume": "Tu déclares une non-conformité, tu notes l'action corrective. C'est exactement ce qu'on te demandera de prouver.",
            "statut": "a_produire",
            "dureeSecondes": null,
            "videoUrl": null,
            "reseaux": {
              "facebook": {
                "statut": "a_venir",
                "date": "2026-09-27",
                "heure": "12:00",
                "compte": "FoodEatUp",
                "format": "Vidéo native 9:16",
                "lienCta": "https://site.foodeatup.com/"
              },
              "instagram": {
                "statut": "a_venir",
                "date": "2026-09-27",
                "heure": "18:30",
                "compte": "foodeatup.cocuisinage",
                "format": "Reel 9:16",
                "lienCta": null
              },
              "tiktok": {
                "statut": "a_venir",
                "date": "2026-09-27",
                "heure": "19:00",
                "compte": "foodeatup",
                "format": "Vidéo 9:16",
                "lienCta": null
              },
              "linkedin": {
                "statut": "a_venir",
                "date": "2026-09-27",
                "heure": "08:00",
                "compte": "FoodEatUp",
                "format": "Vidéo native 9:16",
                "lienCta": "https://site.foodeatup.com/"
              },
              "youtube": {
                "statut": "a_venir",
                "date": "2026-09-27",
                "heure": "10:00",
                "compte": "@FoodEatUp",
                "format": "Short 9:16",
                "lienCta": "https://site.foodeatup.com/"
              }
            },
            "posterUrl": null,
            "datePrevue": "2026-09-27",
            "troisMots": "NON-CONFORMITÉ",
            "tutoriel": {
              "titre": "Faire son contrôle de conformité FoodEatUp",
              "slug": "faire-son-controle-de-conformite",
              "url": "https://tutoriel.foodeatup.com/tutoriel/faire-son-controle-de-conformite",
              "module": "Hygiène & HACCP",
              "etape": "Hygiène & nettoyage\n- **Statut** : En ligne (0 min 52 s)\n- **Vidéo** : https://rapido-software.s3.eu-west-3.amazonaws.com/rapidosoftware/cms/bibliotheque/foodeatup-conformite-tuto-v1\n\n**Description (à quoi ça sert)**\n\nRemplacer le carnet papier par un contrôle de conformité horodaté et centralisé pour chaque point de votre checklist hygiène, avec photo à l'appui, prêt à présenter lors d'un contrôle sanitaire.\n\n**Comment ça marche**\n\n1. Ouvrez Hygiène puis la checklist, et cliquez sur le point à contrôler\n2. Choisissez la zone concernée dans Fait à\n3. Indiquez si le point est conforme, non conforme ou non évalué\n4. Ajoutez un commentaire et une photo à l'appui si besoin\n5. Cliquez sur Valider : le contrôle est enregistré avec la date et l'heure exactes\n\n**Astuce du chef** : Un point non conforme ? Ajoutez toujours une photo et un commentaire précis : c'est cette preuve horodatée qui fait la différence lors d'un contrôle sanitaire, bien plus qu'une simple case cochée.\n\n---",
              "correspondance": "texte",
              "confiance": 0.57
            },
            "tutorielModuleUrl": "https://tutoriel.foodeatup.com/module/haccp",
            "higgsfield": {
              "videoSourceUrl": null,
              "duree": "10 s",
              "format": "vertical 9:16",
              "source": null
            },
            "masterRapidoUrl": null
          },
          {
            "id": "EP060",
            "numero": 60,
            "saison": 2,
            "slug": "ep060-le-poulpe-multitache",
            "titre": "Le poulpe multitâche",
            "module": "HACCP",
            "chapitre": "Congélation",
            "accroche": "Ce qu'on te demande d'être.",
            "punchline": "Ou alors, un seul outil fait le reste.",
            "resume": "Tu enregistres une mise en congélation avec sa date et sa quantité. Plus de sac sans nom au fond du bac.",
            "statut": "a_produire",
            "dureeSecondes": null,
            "videoUrl": null,
            "reseaux": {
              "facebook": {
                "statut": "a_venir",
                "date": "2026-09-28",
                "heure": "12:00",
                "compte": "FoodEatUp",
                "format": "Vidéo native 9:16",
                "lienCta": "https://site.foodeatup.com/"
              },
              "instagram": {
                "statut": "a_venir",
                "date": "2026-09-28",
                "heure": "18:30",
                "compte": "foodeatup.cocuisinage",
                "format": "Reel 9:16",
                "lienCta": null
              },
              "tiktok": {
                "statut": "a_venir",
                "date": "2026-09-28",
                "heure": "19:00",
                "compte": "foodeatup",
                "format": "Vidéo 9:16",
                "lienCta": null
              },
              "linkedin": {
                "statut": "a_venir",
                "date": "2026-09-28",
                "heure": "08:00",
                "compte": "FoodEatUp",
                "format": "Vidéo native 9:16",
                "lienCta": "https://site.foodeatup.com/"
              },
              "youtube": {
                "statut": "a_venir",
                "date": "2026-09-28",
                "heure": "10:00",
                "compte": "@FoodEatUp",
                "format": "Short 9:16",
                "lienCta": "https://site.foodeatup.com/"
              }
            },
            "posterUrl": null,
            "datePrevue": "2026-09-28",
            "troisMots": "CONGÉLATION",
            "tutoriel": {
              "titre": "Scanner le code EAN et la DLC (Contrôle à réception) FoodEatUp",
              "slug": "scanner-ean-et-dlc-reception",
              "url": "https://tutoriel.foodeatup.com/tutoriel/scanner-ean-et-dlc-reception",
              "module": "Hygiène & HACCP",
              "etape": "Contrôle à réception\n- **Statut** : En ligne (0 min 47 s)\n- **Vidéo** : https://rapido-software.s3.eu-west-3.amazonaws.com/rapidosoftware/cms/bibliotheque/scanner-ean-et-dlc-reception-v1\n\n**Description (à quoi ça sert)**\n\nTracer chaque produit reçu en quelques secondes, sans ressaisie : DLC, température de réception et référence produit sont enregistrées directement depuis le tableau des produits livrés, prêtes pour vos contrôles HACCP.\n\n**Comment ça marche**\n\n1. Depuis \"Réception du jour\", ouvrez une commande au statut \"Livrée\"\n2. Dans le tableau \"Produits livrés\", cliquez sur le menu \"...\" de la ligne du produit reçu\n3. Choisissez \"Photo DLC\" (prenez une photo de l'étiquette) ou \"DLC manuelle\" (saisissez la date) pour enregistrer la date limite de consommation\n4. Depuis le même menu, choisissez \"Température\" pour enregistrer la température de réception du produit\n5. Choisissez \"Scanner produit\" pour scanner son code-barres EAN et l'identifier instantanément\n\n**Astuce du chef** : Faites les 3 actions (DLC, température, scan) dans la foulée de la livraison, produit par produit : le camion reparti, la DLC sur l'étiquette d'origine et la température à coeur du produit sont plus difficiles à vérifier après coup.\n\n---",
              "correspondance": "texte",
              "confiance": 0.41
            },
            "tutorielModuleUrl": "https://tutoriel.foodeatup.com/module/haccp",
            "higgsfield": {
              "videoSourceUrl": null,
              "duree": "10 s",
              "format": "vertical 9:16",
              "source": null
            },
            "masterRapidoUrl": null
          }
        ]
      },
      {
        "numero": 3,
        "titre": "L'équipe qui tient",
        "pitch": "Plannings, contrats, pointages : faire tourner une équipe sans y passer ses nuits.",
        "episodes": [
          {
            "id": "EP061",
            "numero": 61,
            "saison": 3,
            "slug": "ep061-le-badge-introuvable",
            "titre": "Le badge introuvable",
            "module": "HACCP",
            "chapitre": "Rapport HACCP",
            "accroche": "Ton système de pointage.",
            "punchline": "Un badge, un QR code, un code PIN. Point.",
            "resume": "Tu édites ton dossier de conformité sur la période de ton choix, prêt à présenter.",
            "statut": "monte",
            "dureeSecondes": 37.5,
            "videoUrl": "https://raw.githubusercontent.com/PrendsTaPart/Video/claude/foodeatup-video-factory-wtb7gs/foodeatup-video-factory/dist/tiktok/EP061.mp4",
            "reseaux": {
              "facebook": {
                "statut": "a_venir",
                "date": "2026-09-29",
                "heure": "12:00",
                "compte": "FoodEatUp",
                "format": "Vidéo native 9:16",
                "lienCta": "https://site.foodeatup.com/"
              },
              "instagram": {
                "statut": "a_venir",
                "date": "2026-09-29",
                "heure": "18:30",
                "compte": "foodeatup.cocuisinage",
                "format": "Reel 9:16",
                "lienCta": null
              },
              "tiktok": {
                "statut": "a_venir",
                "date": "2026-09-29",
                "heure": "19:00",
                "compte": "foodeatup",
                "format": "Vidéo 9:16",
                "lienCta": null
              },
              "linkedin": {
                "statut": "a_venir",
                "date": "2026-09-29",
                "heure": "08:00",
                "compte": "FoodEatUp",
                "format": "Vidéo native 9:16",
                "lienCta": "https://site.foodeatup.com/"
              },
              "youtube": {
                "statut": "a_venir",
                "date": "2026-09-29",
                "heure": "10:00",
                "compte": "@FoodEatUp",
                "format": "Short 9:16",
                "lienCta": "https://site.foodeatup.com/"
              }
            },
            "posterUrl": null,
            "datePrevue": "2026-09-29",
            "troisMots": "RAPPORT HACCP",
            "tutoriel": {
              "titre": "Ouvrir son classeur HACCP",
              "slug": "ouvrir-son-classeur-haccp",
              "url": "https://tutoriel.foodeatup.com/tutoriel/ouvrir-son-classeur-haccp",
              "module": "Hygiène & HACCP",
              "etape": "Démarrer son classeur\n- **Statut** : En ligne (0 min 48 s)\n- **Vidéo** : https://rapido-software.s3.eu-west-3.amazonaws.com/rapidosoftware/cms/bibliotheque/foodeatup-classeur-haccp-tuto-v1\n\n**Description (à quoi ça sert)**\n\nLe classeur HACCP centralise toute la démarche hygiène et sécurité alimentaire de votre établissement — températures, traçabilité, nettoyage, production — avec un onglet Historique qui garde une trace de chaque module, prêt à être présenté lors d'un contrôle sanitaire.\n\n**Comment ça marche**\n\n1. Ouvrez le menu HACCP dans la barre de navigation, en haut de votre espace FoodEatUp\n2. Cliquez sur \"Accueil HACCP\" pour ouvrir votre classeur digital\n3. Retrouvez d'un coup d'œil vos modules clés : Températures, Traçabilité, Plan de nettoyage, Production\n4. Faites défiler pour voir tous les modules : Contrôle à réception, Checklist Hygiène, Étiqueteuse, Documents\n5. Cliquez sur l'onglet \"Historique\" pour consulter tout ce qui a été enregistré, module par module\n\n**Astuce du chef** : Fini le classeur papier qui traîne en cuisine : chaque relevé et chaque action est horodaté automatiquement dans l'onglet Historique. Prenez l'habitude d'y jeter un œil chaque semaine, vous gagnerez un temps précieux le jour du contrôle.\n\n---",
              "correspondance": "texte",
              "confiance": 0.47
            },
            "tutorielModuleUrl": "https://tutoriel.foodeatup.com/module/haccp",
            "higgsfield": {
              "videoSourceUrl": "https://rapido-software.s3.eu-west-3.amazonaws.com/rapidosoftware/cms/bibliotheque/Higgsfield-source-EP061-Le-badge-introuvable",
              "duree": "10 s",
              "format": "vertical 9:16",
              "source": "rapidocms"
            },
            "masterRapidoUrl": "https://rapido-software.s3.eu-west-3.amazonaws.com/rapidosoftware/cms/bibliotheque/FoodEatUp-EP061-Exporter-l-historique-HACCP"
          },
          {
            "id": "EP062",
            "numero": 62,
            "saison": 3,
            "slug": "ep062-la-photo-de-pointage",
            "titre": "La photo de pointage",
            "module": "HACCP",
            "chapitre": "Routine du jour",
            "accroche": "Je te jure, j'étais là à 8 h.",
            "punchline": "Photo, heure, poste. Le débat est clos.",
            "resume": "La conformité devient une routine de deux minutes par service, au lieu d'un dimanche de rattrapage.",
            "statut": "monte",
            "dureeSecondes": 37.5,
            "videoUrl": "https://raw.githubusercontent.com/PrendsTaPart/Video/claude/foodeatup-video-factory-wtb7gs/foodeatup-video-factory/dist/tiktok/EP062.mp4",
            "reseaux": {
              "facebook": {
                "statut": "a_venir",
                "date": null,
                "heure": "12:00",
                "compte": "FoodEatUp",
                "format": "Vidéo native 9:16",
                "lienCta": "https://site.foodeatup.com/"
              },
              "instagram": {
                "statut": "a_venir",
                "date": null,
                "heure": "18:30",
                "compte": "foodeatup.cocuisinage",
                "format": "Reel 9:16",
                "lienCta": null
              },
              "tiktok": {
                "statut": "a_venir",
                "date": null,
                "heure": "19:00",
                "compte": "foodeatup",
                "format": "Vidéo 9:16",
                "lienCta": null
              },
              "linkedin": {
                "statut": "a_venir",
                "date": null,
                "heure": "08:00",
                "compte": "FoodEatUp",
                "format": "Vidéo native 9:16",
                "lienCta": "https://site.foodeatup.com/"
              },
              "youtube": {
                "statut": "a_venir",
                "date": null,
                "heure": "10:00",
                "compte": "@FoodEatUp",
                "format": "Short 9:16",
                "lienCta": "https://site.foodeatup.com/"
              }
            },
            "blocage": "Le chapitre correspondant n'a pas encore de vidéo dans le Drive interne.",
            "posterUrl": null,
            "datePrevue": null,
            "troisMots": "ROUTINE DU JOUR",
            "tutoriel": {
              "titre": "Consulter ses productions en cours",
              "slug": "consulter-ses-productions-en-cours",
              "url": "https://tutoriel.foodeatup.com/tutoriel/consulter-ses-productions-en-cours",
              "module": "Hygiène & HACCP",
              "etape": "Production & plats\n- **Statut** : En ligne (0 min 53 s)\n- **Vidéo** : https://rapido-software.s3.eu-west-3.amazonaws.com/rapidosoftware/cms/bibliotheque/consulter-ses-productions-en-cours-v1\n\n**Description (à quoi ça sert)**\n\nSuivez chaque production et sa traçabilité HACCP en temps réel, sans rien oublier : stock, dates limites de consommation et numéros de lot au même endroit.\n\n**Comment ça marche**\n\n1. Retrouvez la liste de vos plats en préparation, avec leur date de production et leurs allergènes\n2. Cliquez sur Éditer pour ajuster les ingrédients, la date, l'heure ou la durée de vie\n3. Cliquez sur Ingrédients pour vérifier votre stock, la DLC et le numéro de lot de chaque produit\n4. Ajoutez les ingrédients manquants directement à vos courses, ou créez l'étiquette HACCP en un clic\n\n---",
              "correspondance": "texte",
              "confiance": 0.45
            },
            "tutorielModuleUrl": "https://tutoriel.foodeatup.com/module/haccp",
            "higgsfield": {
              "videoSourceUrl": "https://rapido-software.s3.eu-west-3.amazonaws.com/rapidosoftware/cms/bibliotheque/Higgsfield-source-EP062-La-photo-de-pointage",
              "duree": "10 s",
              "format": "vertical 9:16",
              "source": "rapidocms"
            },
            "masterRapidoUrl": "https://rapido-software.s3.eu-west-3.amazonaws.com/rapidosoftware/cms/bibliotheque/FoodEatUp-EP062-Borne-de-pointage-des-employes"
          },
          {
            "id": "EP063",
            "numero": 63,
            "saison": 3,
            "slug": "ep063-le-post-it-perdu",
            "titre": "Le post-it perdu",
            "module": "Équipe & Planning",
            "chapitre": "Créer un employé",
            "accroche": "Ta demande de congé.",
            "punchline": "Demandée, reçue, validée. Sans papier.",
            "resume": "Tu crées ta fiche employé avec son rôle et ses horaires. Elle alimente le planning, les pointages et la paie.",
            "statut": "monte",
            "dureeSecondes": 37.5,
            "videoUrl": "https://raw.githubusercontent.com/PrendsTaPart/Video/claude/foodeatup-video-factory-wtb7gs/foodeatup-video-factory/dist/tiktok/EP063.mp4",
            "reseaux": {
              "facebook": {
                "statut": "a_venir",
                "date": "2026-09-30",
                "heure": "12:00",
                "compte": "FoodEatUp",
                "format": "Vidéo native 9:16",
                "lienCta": "https://site.foodeatup.com/"
              },
              "instagram": {
                "statut": "a_venir",
                "date": "2026-09-30",
                "heure": "18:30",
                "compte": "foodeatup.cocuisinage",
                "format": "Reel 9:16",
                "lienCta": null
              },
              "tiktok": {
                "statut": "a_venir",
                "date": "2026-09-30",
                "heure": "19:00",
                "compte": "foodeatup",
                "format": "Vidéo 9:16",
                "lienCta": null
              },
              "linkedin": {
                "statut": "a_venir",
                "date": "2026-09-30",
                "heure": "08:00",
                "compte": "FoodEatUp",
                "format": "Vidéo native 9:16",
                "lienCta": "https://site.foodeatup.com/"
              },
              "youtube": {
                "statut": "a_venir",
                "date": "2026-09-30",
                "heure": "10:00",
                "compte": "@FoodEatUp",
                "format": "Short 9:16",
                "lienCta": "https://site.foodeatup.com/"
              }
            },
            "posterUrl": null,
            "datePrevue": "2026-09-30",
            "troisMots": "CRÉER UN EMPLOYÉ",
            "tutoriel": {
              "titre": "URL & code PIN FoodEatUp",
              "slug": "se-connecter-cote-employe",
              "url": "https://tutoriel.foodeatup.com/tutoriel/se-connecter-cote-employe",
              "module": "Équipe, Planning & RH",
              "etape": "Espace employé\n- **Statut** : En ligne (0 min 32 s)\n- **Vidéo** : https://rapido-software.s3.eu-west-3.amazonaws.com/rapidosoftware/cms/bibliotheque/se-connecter-cote-employe-v1\n\n**Description (à quoi ça sert)**\n\nPermettre à chaque employé de se connecter lui-même à FoodEatUp depuis son propre téléphone ou une tablette partagée, avec l'URL (ou le QR code) de connexion et son code PIN personnel — sans qu'un administrateur ait besoin d'ouvrir une session à sa place.\n\n**Comment ça marche**\n\n1. Copiez l'URL de connexion (ou scannez le QR code) affiché sur la page qr code actif\n2. Ouvrez-la sur le téléphone ou la tablette de l'employé\n3. Il sélectionne son profil dans la liste\n4. Il saisit son code PIN personnel, à quatre ou six chiffres\n5. Il choisit \"Pointer\" pour badger ses heures, ou \"Mon espace\" pour accéder à son tableau de bord\n6. Son espace n'affiche que les modules autorisés par son rôle, aussi bien dans le menu que dans la grille\n\n**Astuce du chef** : Trois cas d'usage courants : scanner directement le QR code affiché à l'entrée avec l'appareil photo du téléphone (le plus rapide, aucune saisie) ; copier-coller l'URL de connexion si le QR n'est pas à portée, ou pour un premier test depuis un ordinateur ; et une fois le profil et le PIN validés, choisir Pointer pour badger rapidement ses heures sur une borne partagée, ou Mon espace pour ouvrir son tableau de bord complet, limité aux modules autorisés par son rôle.\n\n---",
              "correspondance": "texte",
              "confiance": 0.63
            },
            "tutorielModuleUrl": "https://tutoriel.foodeatup.com/module/equipe-planning",
            "higgsfield": {
              "videoSourceUrl": "https://rapido-software.s3.eu-west-3.amazonaws.com/rapidosoftware/cms/bibliotheque/Higgsfield-source-EP063-Le-post-it-perdu",
              "duree": "10 s",
              "format": "vertical 9:16",
              "source": "rapidocms"
            },
            "masterRapidoUrl": "https://rapido-software.s3.eu-west-3.amazonaws.com/rapidosoftware/cms/bibliotheque/FoodEatUp-EP063-Horaires-d-un-employe"
          },
          {
            "id": "EP064",
            "numero": 64,
            "saison": 3,
            "slug": "ep064-le-planning-au-marqueur",
            "titre": "Le planning au marqueur",
            "module": "Équipe & Planning",
            "chapitre": "Planning semaine",
            "accroche": "Le planning de la semaine.",
            "punchline": "Par employé ou par poste. Imprimable. À jour.",
            "resume": "Le planning se construit en glisser-déposer, avec le coût de la semaine qui s'affiche pendant que tu poses les shifts.",
            "statut": "monte",
            "dureeSecondes": 37.5,
            "videoUrl": "https://raw.githubusercontent.com/PrendsTaPart/Video/claude/foodeatup-video-factory-wtb7gs/foodeatup-video-factory/dist/tiktok/EP064.mp4",
            "reseaux": {
              "facebook": {
                "statut": "a_venir",
                "date": "2026-10-01",
                "heure": "12:00",
                "compte": "FoodEatUp",
                "format": "Vidéo native 9:16",
                "lienCta": "https://site.foodeatup.com/"
              },
              "instagram": {
                "statut": "a_venir",
                "date": "2026-10-01",
                "heure": "18:30",
                "compte": "foodeatup.cocuisinage",
                "format": "Reel 9:16",
                "lienCta": null
              },
              "tiktok": {
                "statut": "a_venir",
                "date": "2026-10-01",
                "heure": "19:00",
                "compte": "foodeatup",
                "format": "Vidéo 9:16",
                "lienCta": null
              },
              "linkedin": {
                "statut": "a_venir",
                "date": "2026-10-01",
                "heure": "08:00",
                "compte": "FoodEatUp",
                "format": "Vidéo native 9:16",
                "lienCta": "https://site.foodeatup.com/"
              },
              "youtube": {
                "statut": "a_venir",
                "date": "2026-10-01",
                "heure": "10:00",
                "compte": "@FoodEatUp",
                "format": "Short 9:16",
                "lienCta": "https://site.foodeatup.com/"
              }
            },
            "posterUrl": null,
            "datePrevue": "2026-10-01",
            "troisMots": "PLANNING SEMAINE",
            "tutoriel": {
              "titre": "Voir son planning côté employé FoodEatUp",
              "slug": "voir-son-planning-cote-employe",
              "url": "https://tutoriel.foodeatup.com/tutoriel/voir-son-planning-cote-employe",
              "module": "Équipe, Planning & RH",
              "etape": "Espace employé\n- **Statut** : En ligne (0 min 29 s)\n- **Vidéo** : https://rapido-software.s3.eu-west-3.amazonaws.com/rapidosoftware/cms/bibliotheque/voir-son-planning-cote-employe-v1\n\n**Description (à quoi ça sert)**\n\nDonner à chaque employé une vue claire et autonome de son propre planning — horaires, shifts et tâches de la semaine — pour qu'il puisse s'organiser, cocher ses tâches terminées et synchroniser son planning avec son agenda personnel, sans jamais avoir à demander au manager.\n\n**Comment ça marche**\n\n1. Depuis son espace, l'employé ouvre \"Mon planning\"\n2. Il retrouve ses heures planifiées, ses shifts et ses tâches de la semaine\n3. Jour par jour : repos, horaires et tâches à faire s'affichent clairement\n4. Il coche une tâche terminée directement depuis la liste\n5. Le compteur de tâches se met à jour instantanément\n6. Il peut cliquer sur \"Ajouter à mon agenda\" pour exporter son planning vers son agenda personnel\n\n**Astuce du chef** : Trois cas d'usage pratiques avec Claude : demandez-lui votre planning de la semaine en cours pour l'avoir en un coup d'œil sans ouvrir l'application ; demandez-lui d'anticiper la semaine prochaine pour organiser vos disponibilités à l'avance ; ou demandez-lui de comparer votre planning prévu à vos heures réellement pointées, pour repérer un écart avant qu'il ne devienne un problème de paie.\n\n---",
              "correspondance": "texte",
              "confiance": 0.52
            },
            "tutorielModuleUrl": "https://tutoriel.foodeatup.com/module/equipe-planning",
            "higgsfield": {
              "videoSourceUrl": "https://rapido-software.s3.eu-west-3.amazonaws.com/rapidosoftware/cms/bibliotheque/Higgsfield-source-EP064-Le-planning-au-marqueur",
              "duree": "10 s",
              "format": "vertical 9:16",
              "source": "rapidocms"
            },
            "masterRapidoUrl": "https://rapido-software.s3.eu-west-3.amazonaws.com/rapidosoftware/cms/bibliotheque/FoodEatUp-EP064-Planning-et-taches-de-l-employe"
          },
          {
            "id": "EP065",
            "numero": 65,
            "saison": 3,
            "slug": "ep065-le-stagiaire-au-bureau",
            "titre": "Le stagiaire au bureau",
            "module": "Équipe & Planning",
            "chapitre": "Pointages",
            "accroche": "Qui a accès à quoi ?",
            "punchline": "Chaque rôle voit exactement ce qu'il doit voir.",
            "resume": "Les heures réelles sont pointées. Tu compares le prévu et le réalisé, sans discussion de fin de mois.",
            "statut": "monte",
            "dureeSecondes": 37.5,
            "videoUrl": "https://raw.githubusercontent.com/PrendsTaPart/Video/claude/foodeatup-video-factory-wtb7gs/foodeatup-video-factory/dist/tiktok/EP065.mp4",
            "reseaux": {
              "facebook": {
                "statut": "a_venir",
                "date": "2026-10-02",
                "heure": "12:00",
                "compte": "FoodEatUp",
                "format": "Vidéo native 9:16",
                "lienCta": "https://site.foodeatup.com/"
              },
              "instagram": {
                "statut": "a_venir",
                "date": "2026-10-02",
                "heure": "18:30",
                "compte": "foodeatup.cocuisinage",
                "format": "Reel 9:16",
                "lienCta": null
              },
              "tiktok": {
                "statut": "a_venir",
                "date": "2026-10-02",
                "heure": "19:00",
                "compte": "foodeatup",
                "format": "Vidéo 9:16",
                "lienCta": null
              },
              "linkedin": {
                "statut": "a_venir",
                "date": "2026-10-02",
                "heure": "08:00",
                "compte": "FoodEatUp",
                "format": "Vidéo native 9:16",
                "lienCta": "https://site.foodeatup.com/"
              },
              "youtube": {
                "statut": "a_venir",
                "date": "2026-10-02",
                "heure": "10:00",
                "compte": "@FoodEatUp",
                "format": "Short 9:16",
                "lienCta": "https://site.foodeatup.com/"
              }
            },
            "posterUrl": null,
            "datePrevue": "2026-10-02",
            "troisMots": "POINTAGES",
            "tutoriel": {
              "titre": "Générer le QR code de pointage FoodEatUp",
              "slug": "generer-qr-code-pointage",
              "url": "https://tutoriel.foodeatup.com/tutoriel/generer-qr-code-pointage",
              "module": "Équipe, Planning & RH",
              "etape": "Pointage, badge & bornes\n- **Statut** : En ligne (0 min 41 s)\n- **Vidéo** : https://rapido-software.s3.eu-west-3.amazonaws.com/rapidosoftware/cms/bibliotheque/generer-qr-code-pointage-v1\n\n**Description (à quoi ça sert)**\n\nSécuriser le pointage de votre équipe contre la fraude (un employé qui pointe pour un collègue absent, ou depuis chez lui) : le QR n'est valable que dans la zone géographique de votre établissement, avec une tolérance réglable. Chaque employé confirme son identité par PIN, photo ou badge NFC au moment de scanner. Vous gardez une vue complète sur tous les QR actifs ou révoqués, sans jamais avoir à racheter du matériel de pointage classique.\n\n**Comment ça marche**\n\n1. Dans le bloc \"Pointage anti-fraude\", choisissez le niveau de sécurité (Standard = PIN + photo, ou plus strict selon vos besoins)\n2. Renseignez la latitude et la longitude de votre établissement — c'est ce qui définit la zone où le pointage sera accepté\n3. Cliquez sur \"+ Générer QR Code\" : FoodEatUp crée un QR unique, propre à votre boutique\n4. Le QR généré s'affiche avec son URL de connexion et 3 étapes d'usage : affichez le QR, l'employé le scanne avec son téléphone, le pointage se fait automatiquement\n5. Affichez ou imprimez ce QR à l'entrée du restaurant ou en cuisine — vos employés le scannent à chaque arrivée et départ\n6. Dans l'onglet Historique, retrouvez tous les QR déjà générés : activez, désactivez, téléchargez ou supprimez-les à tout moment\n7. En configuration avancée, ajustez le rayon de géolocalisation (en mètres) et la tolérance hors-zone (autoriser mais signaler, ou bloquer)\n8. Dans Accès des employés, gérez le code PIN ou le badge NFC de chaque employé individuellement — vous pouvez aussi commander des cartes NFC/QR imprimées\n\n**Astuce du chef** : Ce module a plusieurs couches, voici comment les utiliser dans l'ordre : 1) Le niveau de sécurité définit CE QUI est demandé à l'employé au scan (PIN, photo, ou les deux) — commencez en Standard, montez en exigence si besoin. 2) Le rayon de géolocalisation définit LA ZONE où le pointage est accepté : trop petit (ex. 10m) et le Wi-Fi/GPS imprécis peut bloquer un pointage légitime ; trop grand (500m+) et ça perd son intérêt anti-fraude — 100m est un bon point de départ pour un restaurant en centre-ville. 3) La tolérance hors-zone en \"Autoriser mais signaler\" est plus souple qu'un blocage strict : l'employé pointe quand même, mais vous voyez l'anomalie dans l'historique — pratique en attendant d'affiner le rayon. 4) Un QR peut être désactivé sans être supprimé (utile si vous changez temporairement de terminal) ou supprimé définitivement (si vous soupçonnez qu'il a fuité) — dans ce cas, régénérez-en un immédiatement. 5) Le PIN et le badge NFC sont des méthodes d'accès complémentaires au QR, pas des remplaçants : un employé sans smartphone peut toujours pointer par badge ou code.\n\n---",
              "correspondance": "texte",
              "confiance": 0.48
            },
            "tutorielModuleUrl": "https://tutoriel.foodeatup.com/module/equipe-planning",
            "higgsfield": {
              "videoSourceUrl": "https://rapido-software.s3.eu-west-3.amazonaws.com/rapidosoftware/cms/bibliotheque/Higgsfield-source-EP065-Le-stagiaire-au-bureau",
              "duree": "10 s",
              "format": "vertical 9:16",
              "source": "rapidocms"
            },
            "masterRapidoUrl": "https://rapido-software.s3.eu-west-3.amazonaws.com/rapidosoftware/cms/bibliotheque/FoodEatUp-EP065-Historique-des-pointages"
          },
          {
            "id": "EP066",
            "numero": 66,
            "saison": 3,
            "slug": "ep066-le-grille-pain-qui-ne-repond-pas",
            "titre": "Le grille-pain qui ne répond pas",
            "module": "Équipe & Planning",
            "chapitre": "Congés",
            "accroche": "Ta cuisine n'a personne à qui parler.",
            "punchline": "Jarvis répond, lui. Et il note.",
            "resume": "Une demande de congé arrive, tu valides ou tu refuses depuis l'écran. Le planning se met à jour tout seul.",
            "statut": "monte",
            "dureeSecondes": 37.5,
            "videoUrl": "https://raw.githubusercontent.com/PrendsTaPart/Video/claude/foodeatup-video-factory-wtb7gs/foodeatup-video-factory/dist/tiktok/EP066.mp4",
            "reseaux": {
              "facebook": {
                "statut": "a_venir",
                "date": "2026-10-03",
                "heure": "12:00",
                "compte": "FoodEatUp",
                "format": "Vidéo native 9:16",
                "lienCta": "https://site.foodeatup.com/"
              },
              "instagram": {
                "statut": "a_venir",
                "date": "2026-10-03",
                "heure": "18:30",
                "compte": "foodeatup.cocuisinage",
                "format": "Reel 9:16",
                "lienCta": null
              },
              "tiktok": {
                "statut": "a_venir",
                "date": "2026-10-03",
                "heure": "19:00",
                "compte": "foodeatup",
                "format": "Vidéo 9:16",
                "lienCta": null
              },
              "linkedin": {
                "statut": "a_venir",
                "date": "2026-10-03",
                "heure": "08:00",
                "compte": "FoodEatUp",
                "format": "Vidéo native 9:16",
                "lienCta": "https://site.foodeatup.com/"
              },
              "youtube": {
                "statut": "a_venir",
                "date": "2026-10-03",
                "heure": "10:00",
                "compte": "@FoodEatUp",
                "format": "Short 9:16",
                "lienCta": "https://site.foodeatup.com/"
              }
            },
            "posterUrl": null,
            "datePrevue": "2026-10-03",
            "troisMots": "CONGÉS",
            "tutoriel": null,
            "tutorielModuleUrl": "https://tutoriel.foodeatup.com/module/equipe-planning",
            "tutorielManquant": "Ce chapitre n'a pas encore sa fiche dans l'Academy.",
            "higgsfield": {
              "videoSourceUrl": "https://rapido-software.s3.eu-west-3.amazonaws.com/rapidosoftware/cms/bibliotheque/Higgsfield-source-EP066-Le-grille-pain-qui-ne-repond-pas",
              "duree": "10 s",
              "format": "vertical 9:16",
              "source": "rapidocms"
            },
            "masterRapidoUrl": "https://rapido-software.s3.eu-west-3.amazonaws.com/rapidosoftware/cms/bibliotheque/FoodEatUp-EP066-Demande-d-absence-ou-de-conge"
          },
          {
            "id": "EP067",
            "numero": 67,
            "saison": 3,
            "slug": "ep067-le-thermometre-humain",
            "titre": "Le thermomètre humain",
            "module": "Équipe & Planning",
            "chapitre": "Contrats",
            "accroche": "Ton relevé de température.",
            "punchline": "Un vrai relevé, horodaté, par équipement.",
            "resume": "Contrats et documents employés sont rangés au même endroit, avec leurs échéances.",
            "statut": "monte",
            "dureeSecondes": 37.5,
            "videoUrl": "https://raw.githubusercontent.com/PrendsTaPart/Video/claude/foodeatup-video-factory-wtb7gs/foodeatup-video-factory/dist/tiktok/EP067.mp4",
            "reseaux": {
              "facebook": {
                "statut": "a_venir",
                "date": "2026-10-04",
                "heure": "12:00",
                "compte": "FoodEatUp",
                "format": "Vidéo native 9:16",
                "lienCta": "https://site.foodeatup.com/"
              },
              "instagram": {
                "statut": "a_venir",
                "date": "2026-10-04",
                "heure": "18:30",
                "compte": "foodeatup.cocuisinage",
                "format": "Reel 9:16",
                "lienCta": null
              },
              "tiktok": {
                "statut": "a_venir",
                "date": "2026-10-04",
                "heure": "19:00",
                "compte": "foodeatup",
                "format": "Vidéo 9:16",
                "lienCta": null
              },
              "linkedin": {
                "statut": "a_venir",
                "date": "2026-10-04",
                "heure": "08:00",
                "compte": "FoodEatUp",
                "format": "Vidéo native 9:16",
                "lienCta": "https://site.foodeatup.com/"
              },
              "youtube": {
                "statut": "a_venir",
                "date": "2026-10-04",
                "heure": "10:00",
                "compte": "@FoodEatUp",
                "format": "Short 9:16",
                "lienCta": "https://site.foodeatup.com/"
              }
            },
            "posterUrl": null,
            "datePrevue": "2026-10-04",
            "troisMots": "CONTRATS",
            "tutoriel": {
              "titre": "Établir un contrat et son salaire FoodEatUp",
              "slug": "etablir-son-contrat-et-son-salaire",
              "url": "https://tutoriel.foodeatup.com/tutoriel/etablir-son-contrat-et-son-salaire",
              "module": "Équipe, Planning & RH",
              "etape": "Employés & contrats\n- **Statut** : En ligne (0 min 53 s)\n- **Vidéo** : https://rapido-software.s3.eu-west-3.amazonaws.com/rapidosoftware/cms/bibliotheque/etablir-son-contrat-et-son-salaire-v1\n\n**Description (à quoi ça sert)**\n\nÉtablir le contrat de travail d'un employé — type, poste, dates, salaire, horaires et avantages — directement depuis sa fiche, pour garder tous les documents et conditions d'embauche centralisés au même endroit.\n\n**Comment ça marche**\n\n1. Ouvrez la fiche d'un employé, puis direction l'onglet Salaire\n2. Cliquez sur \"Créer maintenant\"\n3. Choisissez le type de contrat, l'intitulé du poste et la date de début\n4. Renseignez le salaire, les horaires et le nom du responsable\n5. Ajoutez les avantages, la durée d'essai et joignez le contrat en pièce jointe\n6. Cliquez sur \"Créer le contrat\" — il apparaît aussitôt dans la fiche, avec le solde de congés de l'employé\n\n**Astuce du chef** : Le solde de congés se met à jour automatiquement dès la création du contrat, sans calcul à faire de votre côté. Joignez toujours le contrat signé en pièce jointe : il reste ensuite accessible à tout moment dans l'onglet Documents de l'employé, pratique en cas de contrôle. Et pour un CDD ou une mission courte, pensez à renseigner la date de fin — elle affiche \"Indéterminée\" tant qu'elle n'est pas remplie, comme pour un CDI.\n\n---",
              "correspondance": "texte",
              "confiance": 0.38
            },
            "tutorielModuleUrl": "https://tutoriel.foodeatup.com/module/equipe-planning",
            "higgsfield": {
              "videoSourceUrl": "https://rapido-software.s3.eu-west-3.amazonaws.com/rapidosoftware/cms/bibliotheque/Higgsfield-source-EP067-Le-thermometre-humain",
              "duree": "10 s",
              "format": "vertical 9:16",
              "source": "rapidocms"
            },
            "masterRapidoUrl": "https://rapido-software.s3.eu-west-3.amazonaws.com/rapidosoftware/cms/bibliotheque/FoodEatUp-EP067-Salaire-et-contrat"
          },
          {
            "id": "EP068",
            "numero": 68,
            "saison": 3,
            "slug": "ep068-le-second-avis",
            "titre": "Le second avis",
            "module": "Équipe & Planning",
            "chapitre": "Coût du travail",
            "accroche": "Le test scientifique du nez.",
            "punchline": "Une étiquette DLC, et plus personne ne renifle.",
            "resume": "Ton coût de personnel s'affiche en face de ton chiffre d'affaires prévu. Tu ajustes avant, pas après.",
            "statut": "a_produire",
            "dureeSecondes": null,
            "videoUrl": null,
            "reseaux": {
              "facebook": {
                "statut": "a_venir",
                "date": "2026-10-05",
                "heure": "12:00",
                "compte": "FoodEatUp",
                "format": "Vidéo native 9:16",
                "lienCta": "https://site.foodeatup.com/"
              },
              "instagram": {
                "statut": "a_venir",
                "date": "2026-10-05",
                "heure": "18:30",
                "compte": "foodeatup.cocuisinage",
                "format": "Reel 9:16",
                "lienCta": null
              },
              "tiktok": {
                "statut": "a_venir",
                "date": "2026-10-05",
                "heure": "19:00",
                "compte": "foodeatup",
                "format": "Vidéo 9:16",
                "lienCta": null
              },
              "linkedin": {
                "statut": "a_venir",
                "date": "2026-10-05",
                "heure": "08:00",
                "compte": "FoodEatUp",
                "format": "Vidéo native 9:16",
                "lienCta": "https://site.foodeatup.com/"
              },
              "youtube": {
                "statut": "a_venir",
                "date": "2026-10-05",
                "heure": "10:00",
                "compte": "@FoodEatUp",
                "format": "Short 9:16",
                "lienCta": "https://site.foodeatup.com/"
              }
            },
            "posterUrl": null,
            "datePrevue": "2026-10-05",
            "troisMots": "COÛT DU TRAVAIL",
            "tutoriel": null,
            "tutorielModuleUrl": "https://tutoriel.foodeatup.com/module/equipe-planning",
            "tutorielManquant": "Ce chapitre n'a pas encore sa fiche dans l'Academy.",
            "higgsfield": {
              "videoSourceUrl": "https://rapido-software.s3.eu-west-3.amazonaws.com/rapidosoftware/cms/bibliotheque/Higgsfield-source-EP068-Le-second-avis-v2",
              "duree": "10 s",
              "format": "vertical 9:16",
              "source": "rapidocms"
            },
            "masterRapidoUrl": null
          },
          {
            "id": "EP069",
            "numero": 69,
            "saison": 3,
            "slug": "ep069-le-livreur-fantome",
            "titre": "Le livreur fantôme",
            "module": "Équipe & Planning",
            "chapitre": "Recrutement",
            "accroche": "Tu as vérifié la livraison ?",
            "punchline": "Température, DLC, code EAN. En scannant.",
            "resume": "Tu publies ton offre, tu suis les candidatures par statut, tu décides. Le recrutement arrête de traîner sur ton téléphone.",
            "statut": "monte",
            "dureeSecondes": 37.5,
            "videoUrl": "https://raw.githubusercontent.com/PrendsTaPart/Video/claude/foodeatup-video-factory-wtb7gs/foodeatup-video-factory/dist/tiktok/EP069.mp4",
            "reseaux": {
              "facebook": {
                "statut": "a_venir",
                "date": null,
                "heure": "12:00",
                "compte": "FoodEatUp",
                "format": "Vidéo native 9:16",
                "lienCta": "https://site.foodeatup.com/"
              },
              "instagram": {
                "statut": "a_venir",
                "date": null,
                "heure": "18:30",
                "compte": "foodeatup.cocuisinage",
                "format": "Reel 9:16",
                "lienCta": null
              },
              "tiktok": {
                "statut": "a_venir",
                "date": null,
                "heure": "19:00",
                "compte": "foodeatup",
                "format": "Vidéo 9:16",
                "lienCta": null
              },
              "linkedin": {
                "statut": "a_venir",
                "date": null,
                "heure": "08:00",
                "compte": "FoodEatUp",
                "format": "Vidéo native 9:16",
                "lienCta": "https://site.foodeatup.com/"
              },
              "youtube": {
                "statut": "a_venir",
                "date": null,
                "heure": "10:00",
                "compte": "@FoodEatUp",
                "format": "Short 9:16",
                "lienCta": "https://site.foodeatup.com/"
              }
            },
            "blocage": "Le chapitre correspondant n'a pas encore de vidéo dans le Drive interne.",
            "posterUrl": null,
            "datePrevue": null,
            "troisMots": "RECRUTEMENT",
            "tutoriel": {
              "titre": "Commander ses cartes NFC pour le badge FoodEatUp",
              "slug": "commander-ses-cartes-nfc",
              "url": "https://tutoriel.foodeatup.com/tutoriel/commander-ses-cartes-nfc",
              "module": "Équipe, Planning & RH",
              "etape": "Pointage, badge & bornes\n- **Statut** : En ligne (0 min 51 s)\n- **Vidéo** : https://rapido-software.s3.eu-west-3.amazonaws.com/rapidosoftware/cms/bibliotheque/commander-ses-cartes-nfc-v1\n\n**Description (à quoi ça sert)**\n\nÉquiper votre équipe de badges physiques (cartes PVC à puce NFC) pour pointer sans code PIN ni smartphone — pratique pour les employés qui n'ont pas toujours leur téléphone sur eux en cuisine ou en salle.\n\n**Comment ça marche**\n\n1. Dans le module Équipe, sur la page de pointage, retrouvez la section Badges NFC & cartes marketing\n2. Cliquez sur \"Générer badge\" pour un employé : un identifiant unique de pointage est aussitôt créé\n3. Cliquez sur \"Commander les badges NFC\" pour ouvrir la commande groupée\n4. Sélectionnez les employés à équiper : le prix total s'affiche automatiquement (2,50€ par carte)\n5. Cliquez sur \"Confirmer la commande\" : elle est enregistrée, prête à être imprimée et expédiée\n\n**Astuce du chef** : Le badge NFC est un complément au code PIN, pas un remplacement : un employé peut toujours pointer par PIN si son badge est oublié ou perdu. Générez d'abord le badge (identifiant unique) avant de le commander : c'est cet identifiant qui est encodé sur la carte physique. Si un badge est perdu ou volé, régénérez-en un nouveau immédiatement — l'ancien identifiant est désactivé.\n\n---",
              "correspondance": "texte",
              "confiance": 0.4
            },
            "tutorielModuleUrl": "https://tutoriel.foodeatup.com/module/equipe-planning",
            "higgsfield": {
              "videoSourceUrl": "https://rapido-software.s3.eu-west-3.amazonaws.com/rapidosoftware/cms/bibliotheque/Higgsfield-source-EP069-Le-livreur-fantome",
              "duree": "10 s",
              "format": "vertical 9:16",
              "source": "rapidocms"
            },
            "masterRapidoUrl": "https://rapido-software.s3.eu-west-3.amazonaws.com/rapidosoftware/cms/bibliotheque/FoodEatUp-EP069-Ajouter-du-contenu-a-son-site"
          },
          {
            "id": "EP070",
            "numero": 70,
            "saison": 3,
            "slug": "ep070-la-dalle-propre",
            "titre": "La dalle propre",
            "module": "Équipe & Planning",
            "chapitre": "Onboarding",
            "accroche": "C'est fait.",
            "punchline": "Photo analysée par l'IA. Rapport objectif.",
            "resume": "Le nouveau arrive avec son accès, son planning et ses vidéos de formation. Jour un, il est utile.",
            "statut": "a_produire",
            "dureeSecondes": null,
            "videoUrl": null,
            "reseaux": {
              "facebook": {
                "statut": "a_venir",
                "date": "2026-10-06",
                "heure": "12:00",
                "compte": "FoodEatUp",
                "format": "Vidéo native 9:16",
                "lienCta": "https://site.foodeatup.com/"
              },
              "instagram": {
                "statut": "a_venir",
                "date": "2026-10-06",
                "heure": "18:30",
                "compte": "foodeatup.cocuisinage",
                "format": "Reel 9:16",
                "lienCta": null
              },
              "tiktok": {
                "statut": "a_venir",
                "date": "2026-10-06",
                "heure": "19:00",
                "compte": "foodeatup",
                "format": "Vidéo 9:16",
                "lienCta": null
              },
              "linkedin": {
                "statut": "a_venir",
                "date": "2026-10-06",
                "heure": "08:00",
                "compte": "FoodEatUp",
                "format": "Vidéo native 9:16",
                "lienCta": "https://site.foodeatup.com/"
              },
              "youtube": {
                "statut": "a_venir",
                "date": "2026-10-06",
                "heure": "10:00",
                "compte": "@FoodEatUp",
                "format": "Short 9:16",
                "lienCta": "https://site.foodeatup.com/"
              }
            },
            "posterUrl": null,
            "datePrevue": "2026-10-06",
            "troisMots": "ONBOARDING",
            "tutoriel": {
              "titre": "Accès & Jarvis FoodEatUp",
              "slug": "creer-son-code-pin",
              "url": "https://tutoriel.foodeatup.com/tutoriel/creer-son-code-pin",
              "module": "Équipe, Planning & RH",
              "etape": "Rôles, accès & code PIN\n- **Statut** : En ligne (0 min 23 s)\n- **Vidéo** : https://rapido-software.s3.eu-west-3.amazonaws.com/rapidosoftware/cms/bibliotheque/creer-son-code-pin-v1\n\n**Description (à quoi ça sert)**\n\nSécuriser l'accès à FoodEatUp en donnant à chaque employé un code PIN personnel — pour pointer son équipe et se connecter au logiciel avec les seules permissions liées à son rôle. Le QR code de cette même page sert lui à appairer une oreillette Bluetooth à Jarvis.\n\n**Comment ça marche**\n\n1. Dans Accès des employés, repérez qui a déjà un code PIN et qui n'en a pas\n2. Cliquez sur \"Définir un PIN\" (ou \"Modifier le PIN\" pour le changer)\n3. Saisissez un code à 4 ou 6 chiffres\n4. Cliquez sur \"Enregistrer\" — le code est actif immédiatement\n5. Le QR code permanent en haut de page sert lui à appairer une oreillette Bluetooth à Jarvis\n\n**Astuce du chef** : Un code PIN, c'est comme un mot de passe : gardez-le confidentiel et ne le partagez jamais entre employés — chaque code doit rester personnel pour que le pointage et les accès restent traçables et imputables à la bonne personne. Si un code est compromis ou qu'un employé quitte l'équipe, redéfinissez-le aussitôt via \"Modifier le PIN\" plutôt que de le laisser actif. Le rôle choisi à la création de l'employé (voir Ajouter ses employés) détermine précisément ce à quoi ce code donne accès — pas plus, pas moins : le principe de moindre privilège, appliqué sans configuration supplémentaire.\n\n---",
              "correspondance": "texte",
              "confiance": 0.43
            },
            "tutorielModuleUrl": "https://tutoriel.foodeatup.com/module/equipe-planning",
            "higgsfield": {
              "videoSourceUrl": "https://rapido-software.s3.eu-west-3.amazonaws.com/rapidosoftware/cms/bibliotheque/Higgsfield-source-EP070-La-dalle-propre",
              "duree": "10 s",
              "format": "vertical 9:16",
              "source": "rapidocms"
            },
            "masterRapidoUrl": null
          },
          {
            "id": "EP071",
            "numero": 71,
            "saison": 3,
            "slug": "ep071-la-liste-a-l-envers",
            "titre": "La liste à l'envers",
            "module": "Équipe & Planning",
            "chapitre": "Multi-postes",
            "accroche": "La check-list du soir.",
            "punchline": "Cochée, horodatée, signée par qui l'a faite.",
            "resume": "Tu affectes tes équipes par poste et par zone. Chacun sait où il est attendu ce soir.",
            "statut": "a_produire",
            "dureeSecondes": null,
            "videoUrl": null,
            "reseaux": {
              "facebook": {
                "statut": "a_venir",
                "date": "2026-10-07",
                "heure": "12:00",
                "compte": "FoodEatUp",
                "format": "Vidéo native 9:16",
                "lienCta": "https://site.foodeatup.com/"
              },
              "instagram": {
                "statut": "a_venir",
                "date": "2026-10-07",
                "heure": "18:30",
                "compte": "foodeatup.cocuisinage",
                "format": "Reel 9:16",
                "lienCta": null
              },
              "tiktok": {
                "statut": "a_venir",
                "date": "2026-10-07",
                "heure": "19:00",
                "compte": "foodeatup",
                "format": "Vidéo 9:16",
                "lienCta": null
              },
              "linkedin": {
                "statut": "a_venir",
                "date": "2026-10-07",
                "heure": "08:00",
                "compte": "FoodEatUp",
                "format": "Vidéo native 9:16",
                "lienCta": "https://site.foodeatup.com/"
              },
              "youtube": {
                "statut": "a_venir",
                "date": "2026-10-07",
                "heure": "10:00",
                "compte": "@FoodEatUp",
                "format": "Short 9:16",
                "lienCta": "https://site.foodeatup.com/"
              }
            },
            "posterUrl": null,
            "datePrevue": "2026-10-07",
            "troisMots": "MULTI-POSTES",
            "tutoriel": {
              "titre": "Imprimer son planning par poste FoodEatUp",
              "slug": "imprimer-son-planning-par-poste",
              "url": "https://tutoriel.foodeatup.com/tutoriel/imprimer-son-planning-par-poste",
              "module": "Équipe, Planning & RH",
              "etape": "Planning & tâches\n- **Statut** : En ligne (0 min 45 s)\n- **Vidéo** : https://rapido-software.s3.eu-west-3.amazonaws.com/rapidosoftware/cms/bibliotheque/imprimer-son-planning-par-poste-v1\n\n**Description (à quoi ça sert)**\n\nConstruire le planning de votre équipe en toute sécurité — repos réglementaire vérifié et coût salarial calculé en direct — puis l'imprimer par poste de travail pour l'afficher en cuisine, en salle ou à la livraison.\n\n**Comment ça marche**\n\n1. Ouvrez le Planning équipe et basculez entre la vue Par employé et la vue Par poste\n2. Cliquez sur \"Nouveau shift\" : renseignez l'employé, le jour, les horaires et le poste\n3. FoodEatUp vérifie automatiquement le repos minimum entre deux services et calcule votre masse salariale\n4. En vue Par poste, repérez la charge de travail de la cuisine, la salle, la livraison ou la plonge\n5. Cliquez sur \"PDF\" pour exporter et imprimer le planning par poste\n\n**Astuce du chef** : FoodEatUp bloque les créneaux qui ne respectent pas le repos minimum entre deux services : plus besoin de vérifier la réglementation à la main à chaque shift, ni de recalculer votre masse salariale sur un tableur.\n\n---",
              "correspondance": "texte",
              "confiance": 0.42
            },
            "tutorielModuleUrl": "https://tutoriel.foodeatup.com/module/equipe-planning",
            "higgsfield": {
              "videoSourceUrl": "https://rapido-software.s3.eu-west-3.amazonaws.com/rapidosoftware/cms/bibliotheque/Higgsfield-source-EP071-La-liste-a-l-envers",
              "duree": "10 s",
              "format": "vertical 9:16",
              "source": "rapidocms"
            },
            "masterRapidoUrl": null
          },
          {
            "id": "EP072",
            "numero": 72,
            "saison": 3,
            "slug": "ep072-le-classeur",
            "titre": "Le classeur",
            "module": "Équipe & Planning",
            "chapitre": "Absences",
            "accroche": "Contrôle sanitaire. Ce matin.",
            "punchline": "Tout l'historique HACCP, exporté en un clic.",
            "resume": "Une absence, et tu vois immédiatement quel service est découvert. Tu remplaces avant l'ouverture.",
            "statut": "a_produire",
            "dureeSecondes": null,
            "videoUrl": null,
            "reseaux": {
              "facebook": {
                "statut": "a_venir",
                "date": "2026-10-08",
                "heure": "12:00",
                "compte": "FoodEatUp",
                "format": "Vidéo native 9:16",
                "lienCta": "https://site.foodeatup.com/"
              },
              "instagram": {
                "statut": "a_venir",
                "date": "2026-10-08",
                "heure": "18:30",
                "compte": "foodeatup.cocuisinage",
                "format": "Reel 9:16",
                "lienCta": null
              },
              "tiktok": {
                "statut": "a_venir",
                "date": "2026-10-08",
                "heure": "19:00",
                "compte": "foodeatup",
                "format": "Vidéo 9:16",
                "lienCta": null
              },
              "linkedin": {
                "statut": "a_venir",
                "date": "2026-10-08",
                "heure": "08:00",
                "compte": "FoodEatUp",
                "format": "Vidéo native 9:16",
                "lienCta": "https://site.foodeatup.com/"
              },
              "youtube": {
                "statut": "a_venir",
                "date": "2026-10-08",
                "heure": "10:00",
                "compte": "@FoodEatUp",
                "format": "Short 9:16",
                "lienCta": "https://site.foodeatup.com/"
              }
            },
            "posterUrl": null,
            "datePrevue": "2026-10-08",
            "troisMots": "ABSENCES",
            "tutoriel": {
              "titre": "pauses & photo",
              "slug": "pointer-son-service-cote-employe",
              "url": "https://tutoriel.foodeatup.com/tutoriel/pointer-son-service-cote-employe",
              "module": "Équipe, Planning & RH",
              "etape": "Espace employé\n- **Statut** : En ligne (0 min 44 s)\n- **Vidéo** : https://rapido-software.s3.eu-west-3.amazonaws.com/rapidosoftware/cms/bibliotheque/pointer-son-service-cote-employe-v2\n\n**Description (à quoi ça sert)**\n\nPointer son service en salle ou en cuisine sans matériel supplémentaire : entrée, pause déjeuner et sortie se font en un geste depuis son téléphone, avec une photo à chaque étape pour éviter les pointages frauduleux entre collègues. Ces données de présence en temps réel alimentent aussi le pilotage IA de FoodEatUp : masse salariale suivie heure par heure dans AnalytiX BI, écarts entre planning prévu et heures réellement pointées détectés automatiquement, et prochains plannings ajustés sur les temps de présence et de pause réels plutôt que sur des estimations — moins de sureffectif aux heures creuses, moins de sous-effectif aux coups de feu.\n\n**Comment ça marche**\n\n1. Ouvrez la fenêtre Pointage depuis votre espace employé.\n2. Au démarrage du service, appuyez sur Entrée : une photo est prise et l'heure est enregistrée à la seconde.\n3. Pour la pause déjeuner, appuyez sur Pause : une nouvelle photo confirme le départ en pause.\n4. De retour de pause, appuyez sur Fin de pause : FoodEatUp calcule automatiquement sa durée.\n5. En fin de service, appuyez sur Sortie pour boucler votre journée, photo à l'appui.\n\n**Astuce du chef** : Gardez un œil sur les pointages de votre équipe depuis le module Historique : un écart entre l'heure pointée et le planning prévu est souvent le premier signe d'un souci d'organisation à régler avant qu'il ne s'aggrave.\n\n---",
              "correspondance": "texte",
              "confiance": 0.4
            },
            "tutorielModuleUrl": "https://tutoriel.foodeatup.com/module/equipe-planning",
            "higgsfield": {
              "videoSourceUrl": "https://rapido-software.s3.eu-west-3.amazonaws.com/rapidosoftware/cms/bibliotheque/Higgsfield-source-EP072-Le-classeur",
              "duree": "10 s",
              "format": "vertical 9:16",
              "source": "rapidocms"
            },
            "masterRapidoUrl": null
          },
          {
            "id": "EP073",
            "numero": 73,
            "saison": 3,
            "slug": "ep073-pile-ou-face",
            "titre": "Pile ou face",
            "module": "Configuration",
            "chapitre": "Établissement",
            "accroche": "Combien tu commandes pour samedi ?",
            "punchline": "Tes ventes le savent. Demande-leur.",
            "resume": "Tu paramètres ton établissement une fois : horaires, coordonnées, TVA. Tout FoodEatUp s'appuie dessus.",
            "statut": "a_produire",
            "dureeSecondes": null,
            "videoUrl": null,
            "reseaux": {
              "facebook": {
                "statut": "a_venir",
                "date": "2026-10-09",
                "heure": "12:00",
                "compte": "FoodEatUp",
                "format": "Vidéo native 9:16",
                "lienCta": "https://site.foodeatup.com/"
              },
              "instagram": {
                "statut": "a_venir",
                "date": "2026-10-09",
                "heure": "18:30",
                "compte": "foodeatup.cocuisinage",
                "format": "Reel 9:16",
                "lienCta": null
              },
              "tiktok": {
                "statut": "a_venir",
                "date": "2026-10-09",
                "heure": "19:00",
                "compte": "foodeatup",
                "format": "Vidéo 9:16",
                "lienCta": null
              },
              "linkedin": {
                "statut": "a_venir",
                "date": "2026-10-09",
                "heure": "08:00",
                "compte": "FoodEatUp",
                "format": "Vidéo native 9:16",
                "lienCta": "https://site.foodeatup.com/"
              },
              "youtube": {
                "statut": "a_venir",
                "date": "2026-10-09",
                "heure": "10:00",
                "compte": "@FoodEatUp",
                "format": "Short 9:16",
                "lienCta": "https://site.foodeatup.com/"
              }
            },
            "posterUrl": null,
            "datePrevue": "2026-10-09",
            "troisMots": "ÉTABLISSEMENT",
            "tutoriel": {
              "titre": "Saisir ses ingrédients FoodEatUp",
              "slug": "saisir-ses-ingredients",
              "url": "https://tutoriel.foodeatup.com/tutoriel/saisir-ses-ingredients",
              "module": "Configuration Boutique",
              "etape": "Ma carte : produits & recettes\n- **Statut** : En ligne (1 min 00 s)\n- **Vidéo** : https://rapido-software.s3.eu-west-3.amazonaws.com/rapidosoftware/cms/bibliotheque/foodeatup-ingredients-tuto-v1\n\n**Description (à quoi ça sert)**\n\nConstituer la bibliothèque d'ingrédients qui sert de base à toutes vos recettes : nom, fournisseur, prix, stock, allergènes et valeurs nutritionnelles centralisés une bonne fois pour toutes.\n\n**Comment ça marche**\n\n1. Cliquez sur \"Ajouter un ingrédient\"\n2. Donnez-lui un nom, un fournisseur, une unité et un prix unitaire\n3. Classez-le par type, ses particularités alimentaires, et associez-le à vos plats\n4. Renseignez son stock actuel et un seuil d'alerte\n5. Ajoutez ses allergènes et ses valeurs nutritionnelles\n6. Cliquez sur \"Enregistrer\" — il apparaît aussitôt dans votre liste\n\n**Astuce du chef** : Exemple concret : la pâte à tartiner est un ingrédient de vos recettes, tandis que le Nutella est le produit du commerce que vous commandez. Bien distinguer les deux dès la création vous évite des doublons plus tard.\n\n---",
              "correspondance": "texte",
              "confiance": 0.46
            },
            "tutorielModuleUrl": "https://tutoriel.foodeatup.com/module/configuration",
            "higgsfield": {
              "videoSourceUrl": "https://rapido-software.s3.eu-west-3.amazonaws.com/rapidosoftware/cms/bibliotheque/Higgsfield-source-EP073-Pile-ou-face",
              "duree": "10 s",
              "format": "vertical 9:16",
              "source": "rapidocms"
            },
            "masterRapidoUrl": null
          },
          {
            "id": "EP074",
            "numero": 74,
            "saison": 3,
            "slug": "ep074-la-liste-oubliee",
            "titre": "La liste oubliée",
            "module": "Configuration",
            "chapitre": "Catégories",
            "accroche": "Tu as oublié la liste.",
            "punchline": "Elle se construit toute seule. Et elle part au fournisseur.",
            "resume": "Tes catégories de produits, d'ingrédients et de recettes structurent tout le reste. Cinq minutes qui t'en font gagner cent.",
            "statut": "a_produire",
            "dureeSecondes": null,
            "videoUrl": null,
            "reseaux": {
              "facebook": {
                "statut": "a_venir",
                "date": "2026-10-10",
                "heure": "12:00",
                "compte": "FoodEatUp",
                "format": "Vidéo native 9:16",
                "lienCta": "https://site.foodeatup.com/"
              },
              "instagram": {
                "statut": "a_venir",
                "date": "2026-10-10",
                "heure": "18:30",
                "compte": "foodeatup.cocuisinage",
                "format": "Reel 9:16",
                "lienCta": null
              },
              "tiktok": {
                "statut": "a_venir",
                "date": "2026-10-10",
                "heure": "19:00",
                "compte": "foodeatup",
                "format": "Vidéo 9:16",
                "lienCta": null
              },
              "linkedin": {
                "statut": "a_venir",
                "date": "2026-10-10",
                "heure": "08:00",
                "compte": "FoodEatUp",
                "format": "Vidéo native 9:16",
                "lienCta": "https://site.foodeatup.com/"
              },
              "youtube": {
                "statut": "a_venir",
                "date": "2026-10-10",
                "heure": "10:00",
                "compte": "@FoodEatUp",
                "format": "Short 9:16",
                "lienCta": "https://site.foodeatup.com/"
              }
            },
            "posterUrl": null,
            "datePrevue": "2026-10-10",
            "troisMots": "CATÉGORIES",
            "tutoriel": {
              "titre": "Créer ses catégories FoodEatUp",
              "slug": "creer-ses-categories",
              "url": "https://tutoriel.foodeatup.com/tutoriel/creer-ses-categories",
              "module": "Configuration Boutique",
              "etape": "Ma carte : produits & recettes\n- **Statut** : En ligne (0 min 41 s)\n- **Vidéo** : https://rapido-software.s3.eu-west-3.amazonaws.com/rapidosoftware/cms/bibliotheque/foodeatup-categories-tuto-v1\n\n**Description (à quoi ça sert)**\n\nOrganiser vos plats, ingrédients, produits et recettes en catégories claires : les mêmes catégories structurent à la fois votre menu, vos produits de la carte et vos recettes.\n\n**Comment ça marche**\n\n1. Cliquez sur \"Ajouter une catégorie\"\n2. Choisissez ce qu'elle concerne (plat, ingrédient, produit ou recette) et donnez-lui un nom\n3. Ajoutez des tags à la volée si besoin — les nouveaux sont créés automatiquement à l'enregistrement\n4. Choisissez une icône et une couleur pour la repérer d'un coup d'œil\n5. Cliquez sur \"Ajouter\" — la catégorie apparaît aussitôt dans la liste\n\n**Astuce du chef** : Ces catégories ne servent pas qu'à trier votre back-office : elles structurent aussi le menu vu par vos clients et vos recettes. Bien les nommer dès le départ vous fait gagner du temps sur toute la suite.\n\n---",
              "correspondance": "texte",
              "confiance": 0.67
            },
            "tutorielModuleUrl": "https://tutoriel.foodeatup.com/module/configuration",
            "higgsfield": {
              "videoSourceUrl": "https://rapido-software.s3.eu-west-3.amazonaws.com/rapidosoftware/cms/bibliotheque/Higgsfield-source-EP074-La-liste-oubliee",
              "duree": "10 s",
              "format": "vertical 9:16",
              "source": "rapidocms"
            },
            "masterRapidoUrl": null
          },
          {
            "id": "EP075",
            "numero": 75,
            "saison": 3,
            "slug": "ep075-la-facture-dans-la-poche",
            "titre": "La facture dans la poche",
            "module": "Configuration",
            "chapitre": "TVA",
            "accroche": "Ta facture fournisseur.",
            "punchline": "Photographie-la. Les prix se mettent à jour seuls.",
            "resume": "Tes taux de TVA sont posés une fois, appliqués partout : caisse, factures, comptabilité.",
            "statut": "a_produire",
            "dureeSecondes": null,
            "videoUrl": null,
            "reseaux": {
              "facebook": {
                "statut": "a_venir",
                "date": "2026-10-11",
                "heure": "12:00",
                "compte": "FoodEatUp",
                "format": "Vidéo native 9:16",
                "lienCta": "https://site.foodeatup.com/"
              },
              "instagram": {
                "statut": "a_venir",
                "date": "2026-10-11",
                "heure": "18:30",
                "compte": "foodeatup.cocuisinage",
                "format": "Reel 9:16",
                "lienCta": null
              },
              "tiktok": {
                "statut": "a_venir",
                "date": "2026-10-11",
                "heure": "19:00",
                "compte": "foodeatup",
                "format": "Vidéo 9:16",
                "lienCta": null
              },
              "linkedin": {
                "statut": "a_venir",
                "date": "2026-10-11",
                "heure": "08:00",
                "compte": "FoodEatUp",
                "format": "Vidéo native 9:16",
                "lienCta": "https://site.foodeatup.com/"
              },
              "youtube": {
                "statut": "a_venir",
                "date": "2026-10-11",
                "heure": "10:00",
                "compte": "@FoodEatUp",
                "format": "Short 9:16",
                "lienCta": "https://site.foodeatup.com/"
              }
            },
            "posterUrl": null,
            "datePrevue": "2026-10-11",
            "troisMots": "TVA",
            "tutoriel": {
              "titre": "Paramétrer sa TVA FoodEatUp",
              "slug": "parametrer-sa-tva",
              "url": "https://tutoriel.foodeatup.com/tutoriel/parametrer-sa-tva",
              "module": "Configuration Boutique",
              "etape": "Profil, TVA & unités\n- **Statut** : En ligne (0 min 38 s)\n- **Vidéo** : https://rapido-software.s3.eu-west-3.amazonaws.com/rapidosoftware/cms/bibliotheque/foodeatup-tva-tuto-v1\n\n**Description (à quoi ça sert)**\n\nConfigurer les différents taux de TVA applicables à vos produits (taux normal, réduit...) pour que vos prix et factures soient toujours conformes.\n\n**Comment ça marche**\n\n1. Cliquez sur \"Ajouter TVA\"\n2. Donnez un nom à votre taux (ex: Taux réduit) et indiquez le pourcentage\n3. Validez avec \"Ajouter\" — le taux apparaît dans la liste\n4. Pour le modifier, cliquez sur le crayon dans la colonne Action\n5. Ajustez le pourcentage et cliquez sur \"Sauvegarder\"\n\n**Astuce du chef** : Pensez à nommer vos taux clairement (« Taux réduit 5,5% », « Taux normal 20% ») : ça évite les confusions quand vous les associerez à vos produits plus tard.\n\n---",
              "correspondance": "texte",
              "confiance": 0.38
            },
            "tutorielModuleUrl": "https://tutoriel.foodeatup.com/module/configuration",
            "higgsfield": {
              "videoSourceUrl": "https://rapido-software.s3.eu-west-3.amazonaws.com/rapidosoftware/cms/bibliotheque/Higgsfield-source-EP075-La-facture-dans-la-poche",
              "duree": "10 s",
              "format": "vertical 9:16",
              "source": "rapidocms"
            },
            "masterRapidoUrl": null
          },
          {
            "id": "EP076",
            "numero": 76,
            "saison": 3,
            "slug": "ep076-le-recomptage",
            "titre": "Le recomptage",
            "module": "Configuration",
            "chapitre": "Zones et tables",
            "accroche": "Ton inventaire du mardi.",
            "punchline": "La production sort les ingrédients du stock. Automatiquement.",
            "resume": "Tu dessines ta salle : zones, tables, capacités. Ton plan de salle devient vivant pendant le service.",
            "statut": "a_produire",
            "dureeSecondes": null,
            "videoUrl": null,
            "reseaux": {
              "facebook": {
                "statut": "a_venir",
                "date": "2026-10-12",
                "heure": "12:00",
                "compte": "FoodEatUp",
                "format": "Vidéo native 9:16",
                "lienCta": "https://site.foodeatup.com/"
              },
              "instagram": {
                "statut": "a_venir",
                "date": "2026-10-12",
                "heure": "18:30",
                "compte": "foodeatup.cocuisinage",
                "format": "Reel 9:16",
                "lienCta": null
              },
              "tiktok": {
                "statut": "a_venir",
                "date": "2026-10-12",
                "heure": "19:00",
                "compte": "foodeatup",
                "format": "Vidéo 9:16",
                "lienCta": null
              },
              "linkedin": {
                "statut": "a_venir",
                "date": "2026-10-12",
                "heure": "08:00",
                "compte": "FoodEatUp",
                "format": "Vidéo native 9:16",
                "lienCta": "https://site.foodeatup.com/"
              },
              "youtube": {
                "statut": "a_venir",
                "date": "2026-10-12",
                "heure": "10:00",
                "compte": "@FoodEatUp",
                "format": "Short 9:16",
                "lienCta": "https://site.foodeatup.com/"
              }
            },
            "posterUrl": null,
            "datePrevue": "2026-10-12",
            "troisMots": "ZONES ET TABLES",
            "tutoriel": {
              "titre": "Monter ses recettes / fiches techniques FoodEatUp",
              "slug": "monter-ses-recettes",
              "url": "https://tutoriel.foodeatup.com/tutoriel/monter-ses-recettes",
              "module": "Configuration Boutique",
              "etape": "Ma carte : produits & recettes\n- **Statut** : En ligne (0 min 46 s)\n- **Vidéo** : https://rapido-software.s3.eu-west-3.amazonaws.com/rapidosoftware/cms/bibliotheque/monter-ses-recettes-v1\n\n**Description (à quoi ça sert)**\n\nCréer vos recettes / fiches techniques en les reliant directement à vos ingrédients : chaque recette calcule son coût total en temps réel au fil des ingrédients ajoutés, et alimente ensuite vos produits vendables et votre carte.\n\n**Comment ça marche**\n\n1. Cliquez sur \"Créer une recette\"\n2. Ajoutez une photo de votre plat\n3. Cliquez sur \"Générer avec l'IA\" : le nom, la difficulté et la description se remplissent automatiquement depuis la photo\n4. Ajoutez ensuite vos ingrédients un par un, avec leur quantité\n5. Le coût total de la recette se recalcule en temps réel à chaque ingrédient ajouté\n\n**Astuce du chef** : Prenez en photo une recette, demandez à Claude de l'ajouter — il identifie les ingrédients et les crée automatiquement s'ils n'existent pas encore. Une fois la recette prête, demandez-lui aussi de créer le produit vendable correspondant pour qu'il apparaisse sur votre carte.\n\n---",
              "correspondance": "texte",
              "confiance": 0.59
            },
            "tutorielModuleUrl": "https://tutoriel.foodeatup.com/module/configuration",
            "higgsfield": {
              "videoSourceUrl": "https://rapido-software.s3.eu-west-3.amazonaws.com/rapidosoftware/cms/bibliotheque/Higgsfield-source-EP076-Le-recomptage",
              "duree": "10 s",
              "format": "vertical 9:16",
              "source": "rapidocms"
            },
            "masterRapidoUrl": null
          },
          {
            "id": "EP077",
            "numero": 77,
            "saison": 3,
            "slug": "ep077-le-devis-sur-le-set-de-table",
            "titre": "Le devis sur le set de table",
            "module": "Configuration",
            "chapitre": "Équipements",
            "accroche": "Ton devis pour le mariage de samedi.",
            "punchline": "Devis, envoi, acceptation, facture. Une seule chaîne.",
            "resume": "Tu déclares tes équipements et leurs seuils. Ils remontent ensuite dans ton suivi HACCP.",
            "statut": "bloque",
            "dureeSecondes": null,
            "videoUrl": null,
            "reseaux": {
              "facebook": {
                "statut": "a_venir",
                "date": null,
                "heure": "12:00",
                "compte": "FoodEatUp",
                "format": "Vidéo native 9:16",
                "lienCta": "https://site.foodeatup.com/"
              },
              "instagram": {
                "statut": "a_venir",
                "date": null,
                "heure": "18:30",
                "compte": "foodeatup.cocuisinage",
                "format": "Reel 9:16",
                "lienCta": null
              },
              "tiktok": {
                "statut": "a_venir",
                "date": null,
                "heure": "19:00",
                "compte": "foodeatup",
                "format": "Vidéo 9:16",
                "lienCta": null
              },
              "linkedin": {
                "statut": "a_venir",
                "date": null,
                "heure": "08:00",
                "compte": "FoodEatUp",
                "format": "Vidéo native 9:16",
                "lienCta": "https://site.foodeatup.com/"
              },
              "youtube": {
                "statut": "a_venir",
                "date": null,
                "heure": "10:00",
                "compte": "@FoodEatUp",
                "format": "Short 9:16",
                "lienCta": "https://site.foodeatup.com/"
              }
            },
            "blocage": "Le chapitre correspondant n'a pas encore de vidéo dans le Drive interne.",
            "posterUrl": null,
            "datePrevue": null,
            "troisMots": "ÉQUIPEMENTS",
            "tutoriel": {
              "titre": "Saisir ses ingrédients FoodEatUp",
              "slug": "saisir-ses-ingredients",
              "url": "https://tutoriel.foodeatup.com/tutoriel/saisir-ses-ingredients",
              "module": "Configuration Boutique",
              "etape": "Ma carte : produits & recettes\n- **Statut** : En ligne (1 min 00 s)\n- **Vidéo** : https://rapido-software.s3.eu-west-3.amazonaws.com/rapidosoftware/cms/bibliotheque/foodeatup-ingredients-tuto-v1\n\n**Description (à quoi ça sert)**\n\nConstituer la bibliothèque d'ingrédients qui sert de base à toutes vos recettes : nom, fournisseur, prix, stock, allergènes et valeurs nutritionnelles centralisés une bonne fois pour toutes.\n\n**Comment ça marche**\n\n1. Cliquez sur \"Ajouter un ingrédient\"\n2. Donnez-lui un nom, un fournisseur, une unité et un prix unitaire\n3. Classez-le par type, ses particularités alimentaires, et associez-le à vos plats\n4. Renseignez son stock actuel et un seuil d'alerte\n5. Ajoutez ses allergènes et ses valeurs nutritionnelles\n6. Cliquez sur \"Enregistrer\" — il apparaît aussitôt dans votre liste\n\n**Astuce du chef** : Exemple concret : la pâte à tartiner est un ingrédient de vos recettes, tandis que le Nutella est le produit du commerce que vous commandez. Bien distinguer les deux dès la création vous évite des doublons plus tard.\n\n---",
              "correspondance": "texte",
              "confiance": 0.42
            },
            "tutorielModuleUrl": "https://tutoriel.foodeatup.com/module/configuration",
            "higgsfield": {
              "videoSourceUrl": "https://rapido-software.s3.eu-west-3.amazonaws.com/rapidosoftware/cms/bibliotheque/Higgsfield-source-EP077-Le-devis-sur-le-set-de-table",
              "duree": "10 s",
              "format": "vertical 9:16",
              "source": "rapidocms"
            },
            "masterRapidoUrl": null
          },
          {
            "id": "EP078",
            "numero": 78,
            "saison": 3,
            "slug": "ep078-la-boite-a-chaussures",
            "titre": "La boîte à chaussures",
            "module": "Configuration",
            "chapitre": "Utilisateurs",
            "accroche": "Ta comptabilité annuelle.",
            "punchline": "Chaque dépense rattachée à sa livraison. Toute l'année.",
            "resume": "Chaque membre de l'équipe a son accès et ses droits. Tout le monde ne voit pas la compta.",
            "statut": "bloque",
            "dureeSecondes": null,
            "videoUrl": null,
            "reseaux": {
              "facebook": {
                "statut": "a_venir",
                "date": null,
                "heure": "12:00",
                "compte": "FoodEatUp",
                "format": "Vidéo native 9:16",
                "lienCta": "https://site.foodeatup.com/"
              },
              "instagram": {
                "statut": "a_venir",
                "date": null,
                "heure": "18:30",
                "compte": "foodeatup.cocuisinage",
                "format": "Reel 9:16",
                "lienCta": null
              },
              "tiktok": {
                "statut": "a_venir",
                "date": null,
                "heure": "19:00",
                "compte": "foodeatup",
                "format": "Vidéo 9:16",
                "lienCta": null
              },
              "linkedin": {
                "statut": "a_venir",
                "date": null,
                "heure": "08:00",
                "compte": "FoodEatUp",
                "format": "Vidéo native 9:16",
                "lienCta": "https://site.foodeatup.com/"
              },
              "youtube": {
                "statut": "a_venir",
                "date": null,
                "heure": "10:00",
                "compte": "@FoodEatUp",
                "format": "Short 9:16",
                "lienCta": "https://site.foodeatup.com/"
              }
            },
            "blocage": "Le chapitre correspondant n'a pas encore de vidéo dans le Drive interne.",
            "posterUrl": null,
            "datePrevue": null,
            "troisMots": "UTILISATEURS",
            "tutoriel": {
              "titre": "Ajouter ses fournisseurs FoodEatUp",
              "slug": "ajouter-ses-fournisseurs",
              "url": "https://tutoriel.foodeatup.com/tutoriel/ajouter-ses-fournisseurs",
              "module": "Configuration Boutique",
              "etape": "Fournisseurs & MCP\n- **Statut** : En ligne (0 min 40 s)\n- **Vidéo** : https://rapido-software.s3.eu-west-3.amazonaws.com/rapidosoftware/cms/bibliotheque/foodeatup-fournisseurs-tuto-v1\n\n**Description (à quoi ça sert)**\n\nCentraliser les coordonnées de vos fournisseurs pour gagner du temps sur vos commandes, vos factures et le suivi de vos produits.\n\n**Comment ça marche**\n\n1. Cliquez sur \"Ajouter un fournisseur\"\n2. Renseignez son nom et son adresse complète\n3. Ajoutez son email et son téléphone\n4. Indiquez son statut, ses catégories de produits, la livraison et sa fiabilité\n5. Cliquez sur \"Enregistrer\" — le fournisseur apparaît aussitôt dans votre liste\n\n**Astuce du chef** : Vos fournisseurs ne servent pas qu'à la fiche contact : affiliez-les à vos produits pour passer vos commandes fournisseurs par email ou SMS directement depuis votre liste de courses, affiliez vos factures par fournisseur pour un suivi comptable clair, et ajoutez une facture fournisseur via l'OCR — ou directement depuis Claude — pour mettre à jour vos produits automatiquement.\n\n---",
              "correspondance": "texte",
              "confiance": 0.44
            },
            "tutorielModuleUrl": "https://tutoriel.foodeatup.com/module/configuration",
            "higgsfield": {
              "videoSourceUrl": "https://rapido-software.s3.eu-west-3.amazonaws.com/rapidosoftware/cms/bibliotheque/Higgsfield-source-EP078-La-boite-a-chaussures",
              "duree": "10 s",
              "format": "vertical 9:16",
              "source": "rapidocms"
            },
            "masterRapidoUrl": null
          },
          {
            "id": "EP079",
            "numero": 79,
            "saison": 3,
            "slug": "ep079-les-quatorze-cartes",
            "titre": "Les quatorze cartes",
            "module": "Configuration",
            "chapitre": "Import de carte",
            "accroche": "Ton programme de fidélité.",
            "punchline": "Un compte, tous les canaux, zéro carton.",
            "resume": "Tu importes ta carte entière en un appel : catégories, sous-catégories, plats, prix.",
            "statut": "bloque",
            "dureeSecondes": null,
            "videoUrl": null,
            "reseaux": {
              "facebook": {
                "statut": "a_venir",
                "date": null,
                "heure": "12:00",
                "compte": "FoodEatUp",
                "format": "Vidéo native 9:16",
                "lienCta": "https://site.foodeatup.com/"
              },
              "instagram": {
                "statut": "a_venir",
                "date": null,
                "heure": "18:30",
                "compte": "foodeatup.cocuisinage",
                "format": "Reel 9:16",
                "lienCta": null
              },
              "tiktok": {
                "statut": "a_venir",
                "date": null,
                "heure": "19:00",
                "compte": "foodeatup",
                "format": "Vidéo 9:16",
                "lienCta": null
              },
              "linkedin": {
                "statut": "a_venir",
                "date": null,
                "heure": "08:00",
                "compte": "FoodEatUp",
                "format": "Vidéo native 9:16",
                "lienCta": "https://site.foodeatup.com/"
              },
              "youtube": {
                "statut": "a_venir",
                "date": null,
                "heure": "10:00",
                "compte": "@FoodEatUp",
                "format": "Short 9:16",
                "lienCta": "https://site.foodeatup.com/"
              }
            },
            "blocage": "Le chapitre correspondant n'a pas encore de vidéo dans le Drive interne.",
            "posterUrl": null,
            "datePrevue": null,
            "troisMots": "IMPORT DE CARTE",
            "tutoriel": {
              "titre": "Créer ses catégories FoodEatUp",
              "slug": "creer-ses-categories",
              "url": "https://tutoriel.foodeatup.com/tutoriel/creer-ses-categories",
              "module": "Configuration Boutique",
              "etape": "Ma carte : produits & recettes\n- **Statut** : En ligne (0 min 41 s)\n- **Vidéo** : https://rapido-software.s3.eu-west-3.amazonaws.com/rapidosoftware/cms/bibliotheque/foodeatup-categories-tuto-v1\n\n**Description (à quoi ça sert)**\n\nOrganiser vos plats, ingrédients, produits et recettes en catégories claires : les mêmes catégories structurent à la fois votre menu, vos produits de la carte et vos recettes.\n\n**Comment ça marche**\n\n1. Cliquez sur \"Ajouter une catégorie\"\n2. Choisissez ce qu'elle concerne (plat, ingrédient, produit ou recette) et donnez-lui un nom\n3. Ajoutez des tags à la volée si besoin — les nouveaux sont créés automatiquement à l'enregistrement\n4. Choisissez une icône et une couleur pour la repérer d'un coup d'œil\n5. Cliquez sur \"Ajouter\" — la catégorie apparaît aussitôt dans la liste\n\n**Astuce du chef** : Ces catégories ne servent pas qu'à trier votre back-office : elles structurent aussi le menu vu par vos clients et vos recettes. Bien les nommer dès le départ vous fait gagner du temps sur toute la suite.\n\n---",
              "correspondance": "texte",
              "confiance": 0.46
            },
            "tutorielModuleUrl": "https://tutoriel.foodeatup.com/module/configuration",
            "higgsfield": {
              "videoSourceUrl": "https://rapido-software.s3.eu-west-3.amazonaws.com/rapidosoftware/cms/bibliotheque/Higgsfield-source-EP079-Les-quatorze-cartes",
              "duree": "10 s",
              "format": "vertical 9:16",
              "source": "rapidocms"
            },
            "masterRapidoUrl": null
          },
          {
            "id": "EP080",
            "numero": 80,
            "saison": 3,
            "slug": "ep080-le-tiroir-vide",
            "titre": "Le tiroir vide",
            "module": "Configuration",
            "chapitre": "Abonnement",
            "accroche": "Ouverture. Fond de caisse : ?",
            "punchline": "Fond déclaré, opérateur identifié, service ouvert.",
            "resume": "Tu vois ton plan, tes options actives et ce que tu consommes. Aucune ligne surprise en fin de mois.",
            "statut": "a_produire",
            "dureeSecondes": null,
            "videoUrl": null,
            "reseaux": {
              "facebook": {
                "statut": "a_venir",
                "date": "2026-10-13",
                "heure": "12:00",
                "compte": "FoodEatUp",
                "format": "Vidéo native 9:16",
                "lienCta": "https://site.foodeatup.com/"
              },
              "instagram": {
                "statut": "a_venir",
                "date": "2026-10-13",
                "heure": "18:30",
                "compte": "foodeatup.cocuisinage",
                "format": "Reel 9:16",
                "lienCta": null
              },
              "tiktok": {
                "statut": "a_venir",
                "date": "2026-10-13",
                "heure": "19:00",
                "compte": "foodeatup",
                "format": "Vidéo 9:16",
                "lienCta": null
              },
              "linkedin": {
                "statut": "a_venir",
                "date": "2026-10-13",
                "heure": "08:00",
                "compte": "FoodEatUp",
                "format": "Vidéo native 9:16",
                "lienCta": "https://site.foodeatup.com/"
              },
              "youtube": {
                "statut": "a_venir",
                "date": "2026-10-13",
                "heure": "10:00",
                "compte": "@FoodEatUp",
                "format": "Short 9:16",
                "lienCta": "https://site.foodeatup.com/"
              }
            },
            "posterUrl": null,
            "datePrevue": "2026-10-13",
            "troisMots": "ABONNEMENT",
            "tutoriel": {
              "titre": "Choisir son abonnement FoodEatUp",
              "slug": "choisir-son-abonnement",
              "url": "https://tutoriel.foodeatup.com/tutoriel/choisir-son-abonnement",
              "module": "Configuration Boutique",
              "etape": "Compte & abonnement\n- **Statut** : En ligne (0 min 37 s)\n- **Vidéo** : https://rapido-software.s3.eu-west-3.amazonaws.com/rapidosoftware/cms/bibliotheque/foodeatup-abonnement-tuto-v1\n\n**Description (à quoi ça sert)**\n\nDébloquer les fonctionnalités premium de FoodEatUp (HACCP, OCR, StockVision AI...) avec 7 jours d'essai gratuit avant le premier prélèvement.\n\n**Comment ça marche**\n\n1. Choisissez le pack qui correspond à vos besoins (StockVision, OCR, HACCP...)\n2. Vérifiez le récapitulatif : prix, facturation mensuelle, 7 jours d'essai gratuit\n3. Cliquez sur \"Continuer vers le paiement\" et renseignez votre email\n4. Entrez les informations de votre carte bancaire\n5. Cliquez sur \"Démarrer la période d'essai\"\n6. Votre abonnement est activé immédiatement\n\n**Astuce du chef** : Aucune carte n'est débitée avant la fin des 7 jours d'essai — vous pouvez annuler à tout moment depuis vos paramètres si ça ne vous convient pas.\n\n---",
              "correspondance": "texte",
              "confiance": 0.62
            },
            "tutorielModuleUrl": "https://tutoriel.foodeatup.com/module/configuration",
            "higgsfield": {
              "videoSourceUrl": "https://rapido-software.s3.eu-west-3.amazonaws.com/rapidosoftware/cms/bibliotheque/Higgsfield-source-EP080-Le-tiroir-vide",
              "duree": "10 s",
              "format": "vertical 9:16",
              "source": "rapidocms"
            },
            "masterRapidoUrl": null
          },
          {
            "id": "EP081",
            "numero": 81,
            "saison": 3,
            "slug": "ep081-huit-calculatrices",
            "titre": "Huit calculatrices",
            "module": "Comptabilité",
            "chapitre": "Factures",
            "accroche": "On peut séparer ?",
            "punchline": "Oui. Par personne, par article, par montant.",
            "resume": "Chaque commande produit sa facture, numérotée et conforme. Tu ne la ressaisis nulle part.",
            "statut": "a_produire",
            "dureeSecondes": null,
            "videoUrl": null,
            "reseaux": {
              "facebook": {
                "statut": "a_venir",
                "date": "2026-10-14",
                "heure": "12:00",
                "compte": "FoodEatUp",
                "format": "Vidéo native 9:16",
                "lienCta": "https://site.foodeatup.com/"
              },
              "instagram": {
                "statut": "a_venir",
                "date": "2026-10-14",
                "heure": "18:30",
                "compte": "foodeatup.cocuisinage",
                "format": "Reel 9:16",
                "lienCta": null
              },
              "tiktok": {
                "statut": "a_venir",
                "date": "2026-10-14",
                "heure": "19:00",
                "compte": "foodeatup",
                "format": "Vidéo 9:16",
                "lienCta": null
              },
              "linkedin": {
                "statut": "a_venir",
                "date": "2026-10-14",
                "heure": "08:00",
                "compte": "FoodEatUp",
                "format": "Vidéo native 9:16",
                "lienCta": "https://site.foodeatup.com/"
              },
              "youtube": {
                "statut": "a_venir",
                "date": "2026-10-14",
                "heure": "10:00",
                "compte": "@FoodEatUp",
                "format": "Short 9:16",
                "lienCta": "https://site.foodeatup.com/"
              }
            },
            "posterUrl": null,
            "datePrevue": "2026-10-14",
            "troisMots": "FACTURES",
            "tutoriel": {
              "titre": "Créer une facture FoodEatUp",
              "slug": "creer-une-facture",
              "url": "https://tutoriel.foodeatup.com/tutoriel/creer-une-facture",
              "module": "Comptabilité & Achats",
              "etape": "Factures & e-reporting\n- **Statut** : En ligne (0 min 55 s)\n- **Vidéo** : https://rapido-software.s3.eu-west-3.amazonaws.com/rapidosoftware/cms/bibliotheque/creer-une-facture-v1\n\n**Description (à quoi ça sert)**\n\nCréer une facture conforme en quelques clics — client, produits, TVA et remise calculés automatiquement — avec une vérification en temps réel de la conformité Factur-X 2026, pour ne plus jamais rater une mention obligatoire.\n\n**Comment ça marche**\n\n1. Depuis Facturation, retrouvez toutes vos factures et leurs indicateurs (total payées, en attente de paiement, total devis reçu)\n2. Cliquez sur \"Créer une facture\"\n3. Choisissez votre client et complétez son numéro de TVA intracommunautaire si besoin\n4. Recherchez un produit dans votre catalogue, ou créez-le à la volée s'il n'existe pas encore\n5. Fixez la quantité, le prix HT et la TVA de chaque ligne, et appliquez une offre ou une remise si besoin\n6. Renseignez la date de facture et la date d'échéance, puis choisissez le mode de paiement\n7. Cliquez sur \"Enregistrer\" — la facture apparaît aussitôt dans votre liste, prête à télécharger ou à envoyer par e-mail\n\n**Astuce du chef** : La conformité Factur-X n'est pas cosmétique : à partir de 2026, la facturation électronique devient obligatoire pour toutes les entreprises en France. FoodEatUp vérifie votre facture en temps réel (date d'échéance, ligne d'article, TVA) pour vous éviter les mauvaises surprises lors d'un contrôle.\n\n---",
              "correspondance": "texte",
              "confiance": 0.56
            },
            "tutorielModuleUrl": "https://tutoriel.foodeatup.com/module/comptabilite",
            "higgsfield": {
              "videoSourceUrl": "https://rapido-software.s3.eu-west-3.amazonaws.com/rapidosoftware/cms/bibliotheque/Higgsfield-source-EP081-Huit-calculatrices",
              "duree": "10 s",
              "format": "vertical 9:16",
              "source": "rapidocms"
            },
            "masterRapidoUrl": null
          },
          {
            "id": "EP082",
            "numero": 82,
            "saison": 3,
            "slug": "ep082-le-centime",
            "titre": "Le centime",
            "module": "Comptabilité",
            "chapitre": "Devis",
            "accroche": "Il manque un centime.",
            "punchline": "Le Z calcule l'écart. Toi, tu rentres chez toi.",
            "resume": "Un devis pour un groupe se crée en deux minutes et se transforme en commande quand il est accepté.",
            "statut": "a_produire",
            "dureeSecondes": null,
            "videoUrl": null,
            "reseaux": {
              "facebook": {
                "statut": "a_venir",
                "date": "2026-10-15",
                "heure": "12:00",
                "compte": "FoodEatUp",
                "format": "Vidéo native 9:16",
                "lienCta": "https://site.foodeatup.com/"
              },
              "instagram": {
                "statut": "a_venir",
                "date": "2026-10-15",
                "heure": "18:30",
                "compte": "foodeatup.cocuisinage",
                "format": "Reel 9:16",
                "lienCta": null
              },
              "tiktok": {
                "statut": "a_venir",
                "date": "2026-10-15",
                "heure": "19:00",
                "compte": "foodeatup",
                "format": "Vidéo 9:16",
                "lienCta": null
              },
              "linkedin": {
                "statut": "a_venir",
                "date": "2026-10-15",
                "heure": "08:00",
                "compte": "FoodEatUp",
                "format": "Vidéo native 9:16",
                "lienCta": "https://site.foodeatup.com/"
              },
              "youtube": {
                "statut": "a_venir",
                "date": "2026-10-15",
                "heure": "10:00",
                "compte": "@FoodEatUp",
                "format": "Short 9:16",
                "lienCta": "https://site.foodeatup.com/"
              }
            },
            "posterUrl": null,
            "datePrevue": "2026-10-15",
            "troisMots": "DEVIS",
            "tutoriel": {
              "titre": "Créer un devis FoodEatUp",
              "slug": "creer-un-devis",
              "url": "https://tutoriel.foodeatup.com/tutoriel/creer-un-devis",
              "module": "Comptabilité & Achats",
              "etape": "Devis\n- **Statut** : En ligne (1 min 06 s)\n- **Vidéo** : https://rapido-software.s3.eu-west-3.amazonaws.com/rapidosoftware/cms/bibliotheque/creer-un-devis-v1\n\n**Description (à quoi ça sert)**\n\nCréer et envoyer un devis professionnel en quelques clics — produits, remise, TVA et acompte calculés automatiquement — pour que votre client puisse le consulter et le signer en ligne sans aller-retour par email.\n\n**Comment ça marche**\n\n1. Depuis l'onglet Devis, retrouvez tous vos devis (brouillons, envoyés, signés) avec leur montant total\n2. Cliquez sur \"Créer un devis\"\n3. Choisissez le client, le délai de paiement, et le mode de règlement\n4. Recherchez un produit ou une recette : son prix et sa TVA se remplissent automatiquement\n5. Ajustez la quantité si besoin, le total se recalcule instantanément\n6. Appliquez une remise globale, une TVA globale, et demandez si besoin un acompte : le solde restant s'affiche automatiquement\n7. Choisissez d'envoyer le devis par email au client (il reçoit un lien sécurisé pour le consulter et le signer) ou de l'enregistrer en brouillon\n8. Cliquez sur \"Enregistrer\" (ou \"Enregistrer & Envoyer\") — le devis apparaît aussitôt dans votre liste\n\n**Astuce du chef** : L'acompte demandé (en pourcentage ou en montant fixe) calcule automatiquement le solde restant : pratique pour sécuriser une commande importante ou un événement avant de le confirmer. Vous pouvez aussi demander directement à Claude de créer un devis à votre place, en lui donnant simplement le client, le produit et le prix.\n\n---",
              "correspondance": "texte",
              "confiance": 0.53
            },
            "tutorielModuleUrl": "https://tutoriel.foodeatup.com/module/comptabilite",
            "higgsfield": {
              "videoSourceUrl": "https://rapido-software.s3.eu-west-3.amazonaws.com/rapidosoftware/cms/bibliotheque/Higgsfield-source-EP082-Le-centime",
              "duree": "10 s",
              "format": "vertical 9:16",
              "source": "rapidocms"
            },
            "masterRapidoUrl": null
          },
          {
            "id": "EP083",
            "numero": 83,
            "saison": 3,
            "slug": "ep083-le-cri-dans-le-vide",
            "titre": "Le cri dans le vide",
            "module": "Comptabilité",
            "chapitre": "Impayés",
            "accroche": "J'AI DIT DEUX BURGERS !",
            "punchline": "Chaque poste voit ses plats. Sans crier.",
            "resume": "Tu vois ce qui est facturé, encaissé, et ce qui traîne. Les relances arrêtent d'être un jeu de mémoire.",
            "statut": "a_produire",
            "dureeSecondes": null,
            "videoUrl": null,
            "reseaux": {
              "facebook": {
                "statut": "a_venir",
                "date": "2026-10-16",
                "heure": "12:00",
                "compte": "FoodEatUp",
                "format": "Vidéo native 9:16",
                "lienCta": "https://site.foodeatup.com/"
              },
              "instagram": {
                "statut": "a_venir",
                "date": "2026-10-16",
                "heure": "18:30",
                "compte": "foodeatup.cocuisinage",
                "format": "Reel 9:16",
                "lienCta": null
              },
              "tiktok": {
                "statut": "a_venir",
                "date": "2026-10-16",
                "heure": "19:00",
                "compte": "foodeatup",
                "format": "Vidéo 9:16",
                "lienCta": null
              },
              "linkedin": {
                "statut": "a_venir",
                "date": "2026-10-16",
                "heure": "08:00",
                "compte": "FoodEatUp",
                "format": "Vidéo native 9:16",
                "lienCta": "https://site.foodeatup.com/"
              },
              "youtube": {
                "statut": "a_venir",
                "date": "2026-10-16",
                "heure": "10:00",
                "compte": "@FoodEatUp",
                "format": "Short 9:16",
                "lienCta": "https://site.foodeatup.com/"
              }
            },
            "posterUrl": null,
            "datePrevue": "2026-10-16",
            "troisMots": "IMPAYÉS",
            "tutoriel": null,
            "tutorielModuleUrl": "https://tutoriel.foodeatup.com/module/comptabilite",
            "tutorielManquant": "Ce chapitre n'a pas encore sa fiche dans l'Academy.",
            "higgsfield": {
              "videoSourceUrl": "https://rapido-software.s3.eu-west-3.amazonaws.com/rapidosoftware/cms/bibliotheque/Higgsfield-source-EP083-Le-cri-dans-le-vide",
              "duree": "10 s",
              "format": "vertical 9:16",
              "source": "rapidocms"
            },
            "masterRapidoUrl": null
          },
          {
            "id": "EP084",
            "numero": 84,
            "saison": 3,
            "slug": "ep084-le-qr-code-scotche",
            "titre": "Le QR code scotché",
            "module": "Comptabilité",
            "chapitre": "Dépenses",
            "accroche": "Commander à table.",
            "punchline": "Un plan de salle, un QR par table. Ça marche.",
            "resume": "Tu photographies la facture fournisseur, elle rentre dans tes dépenses avec ses lignes et son montant.",
            "statut": "a_produire",
            "dureeSecondes": null,
            "videoUrl": null,
            "reseaux": {
              "facebook": {
                "statut": "a_venir",
                "date": "2026-10-17",
                "heure": "12:00",
                "compte": "FoodEatUp",
                "format": "Vidéo native 9:16",
                "lienCta": "https://site.foodeatup.com/"
              },
              "instagram": {
                "statut": "a_venir",
                "date": "2026-10-17",
                "heure": "18:30",
                "compte": "foodeatup.cocuisinage",
                "format": "Reel 9:16",
                "lienCta": null
              },
              "tiktok": {
                "statut": "a_venir",
                "date": "2026-10-17",
                "heure": "19:00",
                "compte": "foodeatup",
                "format": "Vidéo 9:16",
                "lienCta": null
              },
              "linkedin": {
                "statut": "a_venir",
                "date": "2026-10-17",
                "heure": "08:00",
                "compte": "FoodEatUp",
                "format": "Vidéo native 9:16",
                "lienCta": "https://site.foodeatup.com/"
              },
              "youtube": {
                "statut": "a_venir",
                "date": "2026-10-17",
                "heure": "10:00",
                "compte": "@FoodEatUp",
                "format": "Short 9:16",
                "lienCta": "https://site.foodeatup.com/"
              }
            },
            "posterUrl": null,
            "datePrevue": "2026-10-17",
            "troisMots": "DÉPENSES",
            "tutoriel": {
              "titre": "Saisir ses dépenses fournisseur FoodEatUp",
              "slug": "saisir-ses-depenses-fournisseur",
              "url": "https://tutoriel.foodeatup.com/tutoriel/saisir-ses-depenses-fournisseur",
              "module": "Comptabilité & Achats",
              "etape": "Dépenses & achats\n- **Statut** : En ligne (1 min 00 s)\n- **Vidéo** : https://rapido-software.s3.eu-west-3.amazonaws.com/rapidosoftware/cms/bibliotheque/saisir-ses-depenses-fournisseur-v1\n\n**Description (à quoi ça sert)**\n\nCentraliser tous vos achats fournisseurs — facture jointe, produit, prix, catégorie et statut de paiement — pour garder une comptabilité à jour sans ressaisir les montants à la main.\n\n**Comment ça marche**\n\n1. Depuis l'onglet Dépenses, cliquez sur \"Créer une dépense\"\n2. Renseignez la date d'achat et la référence de la facture fournisseur\n3. Choisissez le fournisseur concerné et joignez directement le fichier de la facture (PDF, JPG, PNG)\n4. Recherchez le produit acheté : son prix se remplit automatiquement depuis votre catalogue\n5. Ajustez la quantité si besoin, la description se complète automatiquement et le total se recalcule en direct\n6. Choisissez une catégorie de dépense et son statut : payée, en attente, ou déclinée\n7. Cliquez sur \"Enregistrer\" — la dépense apparaît aussitôt dans votre liste, avec son montant TTC\n\n**Astuce du chef** : Joindre systématiquement le fichier de la facture à chaque dépense vous évite de fouiller vos mails ou vos classeurs en cas de contrôle : tout reste centralisé et rattaché au bon fournisseur, avec le prix et la catégorie déjà renseignés. Vous pouvez aussi demander directement à Claude d'enregistrer une dépense à votre place, en lui donnant le fournisseur, la référence de facture, le produit et son prix.\n\n---",
              "correspondance": "texte",
              "confiance": 0.41
            },
            "tutorielModuleUrl": "https://tutoriel.foodeatup.com/module/comptabilite",
            "higgsfield": {
              "videoSourceUrl": "https://rapido-software.s3.eu-west-3.amazonaws.com/rapidosoftware/cms/bibliotheque/Higgsfield-source-EP084-Le-QR-code-scotche",
              "duree": "10 s",
              "format": "vertical 9:16",
              "source": "rapidocms"
            },
            "masterRapidoUrl": null
          },
          {
            "id": "EP085",
            "numero": 85,
            "saison": 3,
            "slug": "ep085-le-ballon-qui-se-degonfle",
            "titre": "Le ballon qui se dégonfle",
            "module": "Comptabilité",
            "chapitre": "Synthèse",
            "accroche": "Table de 8. 20 h 30. Personne.",
            "punchline": "No-show marqué, table libérée, soirée sauvée.",
            "resume": "Chiffre d'affaires, dépenses, impayés, marge : la synthèse du mois tient sur un écran.",
            "statut": "a_produire",
            "dureeSecondes": null,
            "videoUrl": null,
            "reseaux": {
              "facebook": {
                "statut": "a_venir",
                "date": "2026-10-18",
                "heure": "12:00",
                "compte": "FoodEatUp",
                "format": "Vidéo native 9:16",
                "lienCta": "https://site.foodeatup.com/"
              },
              "instagram": {
                "statut": "a_venir",
                "date": "2026-10-18",
                "heure": "18:30",
                "compte": "foodeatup.cocuisinage",
                "format": "Reel 9:16",
                "lienCta": null
              },
              "tiktok": {
                "statut": "a_venir",
                "date": "2026-10-18",
                "heure": "19:00",
                "compte": "foodeatup",
                "format": "Vidéo 9:16",
                "lienCta": null
              },
              "linkedin": {
                "statut": "a_venir",
                "date": "2026-10-18",
                "heure": "08:00",
                "compte": "FoodEatUp",
                "format": "Vidéo native 9:16",
                "lienCta": "https://site.foodeatup.com/"
              },
              "youtube": {
                "statut": "a_venir",
                "date": "2026-10-18",
                "heure": "10:00",
                "compte": "@FoodEatUp",
                "format": "Short 9:16",
                "lienCta": "https://site.foodeatup.com/"
              }
            },
            "posterUrl": null,
            "datePrevue": "2026-10-18",
            "troisMots": "SYNTHÈSE",
            "tutoriel": null,
            "tutorielModuleUrl": "https://tutoriel.foodeatup.com/module/comptabilite",
            "tutorielManquant": "Ce chapitre n'a pas encore sa fiche dans l'Academy.",
            "higgsfield": {
              "videoSourceUrl": null,
              "duree": "10 s",
              "format": "vertical 9:16",
              "source": null
            },
            "masterRapidoUrl": null
          },
          {
            "id": "EP086",
            "numero": 86,
            "saison": 3,
            "slug": "ep086-le-telephone-que-personne-ne-prend",
            "titre": "Le téléphone que personne ne prend",
            "module": "Comptabilité",
            "chapitre": "Export comptable",
            "accroche": "Trois appels manqués pendant le coup de feu.",
            "punchline": "Caroline décroche. Et elle prend la réservation.",
            "resume": "Tu envoies à ton comptable un export propre. Le dimanche soir redevient un dimanche soir.",
            "statut": "a_produire",
            "dureeSecondes": null,
            "videoUrl": null,
            "reseaux": {
              "facebook": {
                "statut": "a_venir",
                "date": "2026-10-19",
                "heure": "12:00",
                "compte": "FoodEatUp",
                "format": "Vidéo native 9:16",
                "lienCta": "https://site.foodeatup.com/"
              },
              "instagram": {
                "statut": "a_venir",
                "date": "2026-10-19",
                "heure": "18:30",
                "compte": "foodeatup.cocuisinage",
                "format": "Reel 9:16",
                "lienCta": null
              },
              "tiktok": {
                "statut": "a_venir",
                "date": "2026-10-19",
                "heure": "19:00",
                "compte": "foodeatup",
                "format": "Vidéo 9:16",
                "lienCta": null
              },
              "linkedin": {
                "statut": "a_venir",
                "date": "2026-10-19",
                "heure": "08:00",
                "compte": "FoodEatUp",
                "format": "Vidéo native 9:16",
                "lienCta": "https://site.foodeatup.com/"
              },
              "youtube": {
                "statut": "a_venir",
                "date": "2026-10-19",
                "heure": "10:00",
                "compte": "@FoodEatUp",
                "format": "Short 9:16",
                "lienCta": "https://site.foodeatup.com/"
              }
            },
            "posterUrl": null,
            "datePrevue": "2026-10-19",
            "troisMots": "EXPORT COMPTABLE",
            "tutoriel": {
              "titre": "QR, web & vocal",
              "slug": "retrouver-toutes-mes-commandes",
              "url": "https://tutoriel.foodeatup.com/tutoriel/retrouver-toutes-mes-commandes",
              "module": "Comptabilité & Achats",
              "etape": "Commandes\n- **Statut** : Bientôt disponible (tournage en cours)\n\n**Description (à quoi ça sert)**\n\nRetrouver toutes mes commandes — QR, web & vocal — tutoriel en préparation dans le module Comptabilité & Achats. Il arrive très bientôt dans ce fil conducteur.\n\n**Comment ça marche**\n\n1. Cette vidéo est en cours de tournage dans les cuisines FoodEatUp.\n2. Sa fiche est déjà en place : elle se remplira dès la mise en ligne.\n\n---",
              "correspondance": "texte",
              "confiance": 0.43
            },
            "tutorielModuleUrl": "https://tutoriel.foodeatup.com/module/comptabilite",
            "higgsfield": {
              "videoSourceUrl": null,
              "duree": "10 s",
              "format": "vertical 9:16",
              "source": null
            },
            "masterRapidoUrl": null
          },
          {
            "id": "EP087",
            "numero": 87,
            "saison": 3,
            "slug": "ep087-les-trois-tablettes",
            "titre": "Les trois tablettes",
            "module": "Mon Site",
            "chapitre": "Éditeur",
            "accroche": "Trois plateformes. Trois écrans.",
            "punchline": "Une seule cuisine. Un seul flux.",
            "resume": "Tu actives l'éditeur, tu choisis ton template, ton site est en ligne le jour même, aux couleurs de ta maison.",
            "statut": "a_produire",
            "dureeSecondes": null,
            "videoUrl": null,
            "reseaux": {
              "facebook": {
                "statut": "a_venir",
                "date": "2026-10-20",
                "heure": "12:00",
                "compte": "FoodEatUp",
                "format": "Vidéo native 9:16",
                "lienCta": "https://site.foodeatup.com/"
              },
              "instagram": {
                "statut": "a_venir",
                "date": "2026-10-20",
                "heure": "18:30",
                "compte": "foodeatup.cocuisinage",
                "format": "Reel 9:16",
                "lienCta": null
              },
              "tiktok": {
                "statut": "a_venir",
                "date": "2026-10-20",
                "heure": "19:00",
                "compte": "foodeatup",
                "format": "Vidéo 9:16",
                "lienCta": null
              },
              "linkedin": {
                "statut": "a_venir",
                "date": "2026-10-20",
                "heure": "08:00",
                "compte": "FoodEatUp",
                "format": "Vidéo native 9:16",
                "lienCta": "https://site.foodeatup.com/"
              },
              "youtube": {
                "statut": "a_venir",
                "date": "2026-10-20",
                "heure": "10:00",
                "compte": "@FoodEatUp",
                "format": "Short 9:16",
                "lienCta": "https://site.foodeatup.com/"
              }
            },
            "posterUrl": null,
            "datePrevue": "2026-10-20",
            "troisMots": "ÉDITEUR",
            "tutoriel": {
              "titre": "Éditeur Web",
              "slug": "personnaliser-son-site",
              "url": "https://tutoriel.foodeatup.com/tutoriel/personnaliser-son-site",
              "module": "Site Web & Vitrine",
              "etape": "Template & design\n- **Statut** : En ligne (0 min 45 s)\n- **Vidéo** : https://rapido-software.s3.eu-west-3.amazonaws.com/rapidosoftware/cms/bibliotheque/personnaliser-son-site-v1\n\n**Description (à quoi ça sert)**\n\nAjuster les textes de votre site (badge, titre, sous-titre) pour coller à votre actualité ou à votre identité de marque, sans toucher au design ni au reste du contenu — et sans risque, chaque modification reste restaurable.\n\n**Comment ça marche**\n\n1. Depuis Site Web > Éditeur visuel, cliquez sur le bloc que vous voulez modifier — ici la bannière d'accueil.\n2. Dans le panneau Modifier le bloc, changez le badge, le titre ou le sous-titre : videz un champ pour revenir au texte du template.\n3. Cliquez sur Enregistrer pour valider : chaque enregistrement crée une version restaurable dans le Studio.\n4. Votre site est mis à jour instantanément, sans republier ni changer de template.\n\n**Astuce du chef** : Vous n'êtes jamais bloqué : videz un champ pour revenir instantanément au texte du template, et chaque enregistrement crée une version restaurable dans le Studio si vous voulez faire marche arrière.\n\n---",
              "correspondance": "texte",
              "confiance": 0.78
            },
            "tutorielModuleUrl": "https://tutoriel.foodeatup.com/module/site-web-vitrine",
            "higgsfield": {
              "videoSourceUrl": null,
              "duree": "10 s",
              "format": "vertical 9:16",
              "source": null
            },
            "masterRapidoUrl": null
          },
          {
            "id": "EP088",
            "numero": 88,
            "saison": 3,
            "slug": "ep088-une-etoile",
            "titre": "Une étoile",
            "module": "Mon Site",
            "chapitre": "Pages",
            "accroche": "Un avis. Publié il y a six jours.",
            "punchline": "Vu, répondu, traité. Le jour même.",
            "resume": "Tu ajoutes tes pages : carte, avis, allergènes, recrutement. Elles se publient quand tu le décides.",
            "statut": "a_produire",
            "dureeSecondes": null,
            "videoUrl": null,
            "reseaux": {
              "facebook": {
                "statut": "a_venir",
                "date": "2026-10-21",
                "heure": "12:00",
                "compte": "FoodEatUp",
                "format": "Vidéo native 9:16",
                "lienCta": "https://site.foodeatup.com/"
              },
              "instagram": {
                "statut": "a_venir",
                "date": "2026-10-21",
                "heure": "18:30",
                "compte": "foodeatup.cocuisinage",
                "format": "Reel 9:16",
                "lienCta": null
              },
              "tiktok": {
                "statut": "a_venir",
                "date": "2026-10-21",
                "heure": "19:00",
                "compte": "foodeatup",
                "format": "Vidéo 9:16",
                "lienCta": null
              },
              "linkedin": {
                "statut": "a_venir",
                "date": "2026-10-21",
                "heure": "08:00",
                "compte": "FoodEatUp",
                "format": "Vidéo native 9:16",
                "lienCta": "https://site.foodeatup.com/"
              },
              "youtube": {
                "statut": "a_venir",
                "date": "2026-10-21",
                "heure": "10:00",
                "compte": "@FoodEatUp",
                "format": "Short 9:16",
                "lienCta": "https://site.foodeatup.com/"
              }
            },
            "posterUrl": null,
            "datePrevue": "2026-10-21",
            "troisMots": "PAGES",
            "tutoriel": null,
            "tutorielModuleUrl": "https://tutoriel.foodeatup.com/module/site-web-vitrine",
            "tutorielManquant": "Ce chapitre n'a pas encore sa fiche dans l'Academy.",
            "higgsfield": {
              "videoSourceUrl": "https://rapido-software.s3.eu-west-3.amazonaws.com/rapidosoftware/cms/bibliotheque/Higgsfield-source-EP088-Une-etoile",
              "duree": "10 s",
              "format": "vertical 9:16",
              "source": "rapidocms"
            },
            "masterRapidoUrl": null
          },
          {
            "id": "EP089",
            "numero": 89,
            "saison": 3,
            "slug": "ep089-le-bocal-presque-vide",
            "titre": "Le bocal presque vide",
            "module": "Mon Site",
            "chapitre": "Domaine",
            "accroche": "Ton jeu concours.",
            "punchline": "QR code, roue cadeaux, gagnants tracés.",
            "resume": "Tu branches ton nom de domaine. Tes clients arrivent chez toi, pas sur une plateforme.",
            "statut": "a_produire",
            "dureeSecondes": null,
            "videoUrl": null,
            "reseaux": {
              "facebook": {
                "statut": "a_venir",
                "date": "2026-10-22",
                "heure": "12:00",
                "compte": "FoodEatUp",
                "format": "Vidéo native 9:16",
                "lienCta": "https://site.foodeatup.com/"
              },
              "instagram": {
                "statut": "a_venir",
                "date": "2026-10-22",
                "heure": "18:30",
                "compte": "foodeatup.cocuisinage",
                "format": "Reel 9:16",
                "lienCta": null
              },
              "tiktok": {
                "statut": "a_venir",
                "date": "2026-10-22",
                "heure": "19:00",
                "compte": "foodeatup",
                "format": "Vidéo 9:16",
                "lienCta": null
              },
              "linkedin": {
                "statut": "a_venir",
                "date": "2026-10-22",
                "heure": "08:00",
                "compte": "FoodEatUp",
                "format": "Vidéo native 9:16",
                "lienCta": "https://site.foodeatup.com/"
              },
              "youtube": {
                "statut": "a_venir",
                "date": "2026-10-22",
                "heure": "10:00",
                "compte": "@FoodEatUp",
                "format": "Short 9:16",
                "lienCta": "https://site.foodeatup.com/"
              }
            },
            "posterUrl": null,
            "datePrevue": "2026-10-22",
            "troisMots": "DOMAINE",
            "tutoriel": {
              "titre": "Connecter son Domaine",
              "slug": "connecter-son-domaine",
              "url": "https://tutoriel.foodeatup.com/tutoriel/connecter-son-domaine",
              "module": "Site Web & Vitrine",
              "etape": "Horaires, réservations & domaine\n- **Statut** : En ligne (0 min 55 s)\n- **Vidéo** : https://rapido-software.s3.eu-west-3.amazonaws.com/rapidosoftware/cms/bibliotheque/foodeatup-domaine-tuto-v1.mp4\n\n**Description (à quoi ça sert)**\n\nServir votre site FoodEatUp sur votre propre nom de domaine (ex : www.monrestaurant.fr) plutôt que sur une URL générique, avec certificat SSL automatique — une image plus professionnelle pour vos clients, sans compétence technique.\n\n**Comment ça marche**\n\n1. Dans l'onglet Domaine de votre site, saisissez votre nom de domaine (ex : www.monrestaurant.fr)\n2. Cliquez sur Connecter pour l'associer à votre boutique FoodEatUp\n3. Copiez l'enregistrement CNAME fourni et créez-le chez votre registrar (OVH, Gandi...)\n4. Cliquez sur Vérifier maintenant pour contrôler la propagation DNS\n5. Une fois validé, votre site est accessible sur votre propre domaine, avec le SSL activé automatiquement\n\n**Astuce du chef** : Le CNAME doit pointer vers sites.foodeatup.com, jamais vers une adresse IP directe. Si votre registrar bloque les CNAME sur le sous-domaine www, ouvrez un ticket chez lui — ce n'est pas un blocage FoodEatUp. Et patientez : la propagation DNS peut prendre jusqu'à 24 heures avant que Vérifier maintenant passe au vert.\n\n---",
              "correspondance": "texte",
              "confiance": 0.5
            },
            "tutorielModuleUrl": "https://tutoriel.foodeatup.com/module/site-web-vitrine",
            "higgsfield": {
              "videoSourceUrl": "https://rapido-software.s3.eu-west-3.amazonaws.com/rapidosoftware/cms/bibliotheque/Higgsfield-source-EP089-Le-bocal-presque-vide",
              "duree": "10 s",
              "format": "vertical 9:16",
              "source": "rapidocms"
            },
            "masterRapidoUrl": null
          },
          {
            "id": "EP090",
            "numero": 90,
            "saison": 3,
            "slug": "ep090-le-marc-de-cafe",
            "titre": "Le marc de café",
            "module": "Mon Site",
            "chapitre": "Leads du site",
            "accroche": "Ta prévision pour samedi.",
            "punchline": "PrediBot lit tes données. Pas ton café.",
            "resume": "Chaque demande de privatisation ou de contact devient un lead dans ton fichier client.",
            "statut": "bloque",
            "dureeSecondes": null,
            "videoUrl": null,
            "reseaux": {
              "facebook": {
                "statut": "a_venir",
                "date": null,
                "heure": "12:00",
                "compte": "FoodEatUp",
                "format": "Vidéo native 9:16",
                "lienCta": "https://site.foodeatup.com/"
              },
              "instagram": {
                "statut": "a_venir",
                "date": null,
                "heure": "18:30",
                "compte": "foodeatup.cocuisinage",
                "format": "Reel 9:16",
                "lienCta": null
              },
              "tiktok": {
                "statut": "a_venir",
                "date": null,
                "heure": "19:00",
                "compte": "foodeatup",
                "format": "Vidéo 9:16",
                "lienCta": null
              },
              "linkedin": {
                "statut": "a_venir",
                "date": null,
                "heure": "08:00",
                "compte": "FoodEatUp",
                "format": "Vidéo native 9:16",
                "lienCta": "https://site.foodeatup.com/"
              },
              "youtube": {
                "statut": "a_venir",
                "date": null,
                "heure": "10:00",
                "compte": "@FoodEatUp",
                "format": "Short 9:16",
                "lienCta": "https://site.foodeatup.com/"
              }
            },
            "blocage": "Le chapitre correspondant n'a pas encore de vidéo dans le Drive interne.",
            "posterUrl": null,
            "datePrevue": null,
            "troisMots": "LEADS DU SITE",
            "tutoriel": {
              "titre": "Gérer les pages de son site",
              "slug": "gerer-les-pages-de-son-site",
              "url": "https://tutoriel.foodeatup.com/tutoriel/gerer-les-pages-de-son-site",
              "module": "Site Web & Vitrine",
              "etape": "Pages & contenu\n- **Statut** : En ligne (0 min 43 s)\n- **Vidéo** : https://rapido-software.s3.eu-west-3.amazonaws.com/rapidosoftware/cms/bibliotheque/gerer-les-pages-de-son-site-v1\n\n**Description (à quoi ça sert)**\n\nGardez le contrôle total sur les pages visibles de votre site : masquez une page en travaux ou une offre terminée, puis remettez-la en ligne dès qu'elle est prête — sans jamais perdre son contenu ni la recréer.\n\n**Comment ça marche**\n\n1. Ouvrez l'onglet Pages depuis le menu de gauche de l'éditeur de site.\n2. Repérez en un coup d'œil le statut de chaque page : Publiée ou Brouillon.\n3. Cliquez sur Dépublier pour retirer une page du site sans perdre son contenu.\n4. Cliquez sur Publier pour la remettre en ligne à tout moment, en un clic.\n5. Cliquez sur Voir pour contrôler le rendu final, en direct sur votre site.\n\n**Astuce du chef** : Ne supprimez jamais une page pour la cacher : dépubliez-la. Le contenu reste intact et vous la remettez en ligne en un clic dès qu'elle est prête, sans repartir de zéro.\n\n---",
              "correspondance": "texte",
              "confiance": 0.55
            },
            "tutorielModuleUrl": "https://tutoriel.foodeatup.com/module/site-web-vitrine",
            "higgsfield": {
              "videoSourceUrl": "https://rapido-software.s3.eu-west-3.amazonaws.com/rapidosoftware/cms/bibliotheque/Higgsfield-source-EP090-Le-marc-de-cafe",
              "duree": "10 s",
              "format": "vertical 9:16",
              "source": "rapidocms"
            },
            "masterRapidoUrl": null
          }
        ]
      },
      {
        "numero": 4,
        "titre": "Se faire connaître",
        "pitch": "Site, avis, campagnes : remplir la salle avant même l'ouverture.",
        "episodes": [
          {
            "id": "EP091",
            "numero": 91,
            "saison": 4,
            "slug": "ep091-le-petard-dans-le-tiramisu",
            "titre": "Le pétard dans le tiramisu",
            "module": "Réservation",
            "chapitre": "2 - Ajouter une réservation",
            "accroche": "Anniversaire de table 12.",
            "punchline": "Les surprises, c'est bien. Les imprévus, non.",
            "resume": "L'anniversaire est noté à la réservation, avec le nombre de couverts et la demande spéciale. La cuisine et la salle le savent avant que le client arrive.",
            "statut": "a_produire",
            "dureeSecondes": null,
            "videoUrl": null,
            "reseaux": {
              "facebook": {
                "statut": "a_venir",
                "date": "2026-10-23",
                "heure": "12:00",
                "compte": "FoodEatUp",
                "format": "Vidéo native 9:16",
                "lienCta": "https://site.foodeatup.com/"
              },
              "instagram": {
                "statut": "a_venir",
                "date": "2026-10-23",
                "heure": "18:30",
                "compte": "foodeatup.cocuisinage",
                "format": "Reel 9:16",
                "lienCta": null
              },
              "tiktok": {
                "statut": "a_venir",
                "date": "2026-10-23",
                "heure": "19:00",
                "compte": "foodeatup",
                "format": "Vidéo 9:16",
                "lienCta": null
              },
              "linkedin": {
                "statut": "a_venir",
                "date": "2026-10-23",
                "heure": "08:00",
                "compte": "FoodEatUp",
                "format": "Vidéo native 9:16",
                "lienCta": "https://site.foodeatup.com/"
              },
              "youtube": {
                "statut": "a_venir",
                "date": "2026-10-23",
                "heure": "10:00",
                "compte": "@FoodEatUp",
                "format": "Short 9:16",
                "lienCta": "https://site.foodeatup.com/"
              }
            },
            "posterUrl": null,
            "datePrevue": "2026-10-23",
            "troisMots": "AJOUTER UNE RÉSERVATION",
            "tutoriel": {
              "titre": "module Table",
              "slug": "ajouter-une-reservation",
              "url": "https://tutoriel.foodeatup.com/tutoriel/ajouter-une-reservation",
              "module": "Réservations & Plan de salle",
              "etape": "Créer & modifier\n- **Statut** : En ligne (0 min 48 s)\n- **Vidéo** : https://rapido-software.s3.eu-west-3.amazonaws.com/rapidosoftware/cms/bibliotheque/foodeatup-reservation-tuto-v1\n\n**Description (à quoi ça sert)**\n\nCentraliser toutes vos réservations — site, téléphone, sur place — dans un même plan de salle, avec assignation de table automatique ou manuelle selon vos zones (Salle principale, Terrasse...), sans jamais ressaisir les informations d'un client à son arrivée.\n\n**Comment ça marche**\n\n1. Depuis Réservations, cliquez sur \"+ Nouvelle réservation\"\n2. Renseignez le nom du client, son téléphone et son email\n3. Choisissez la date, l'heure et le nombre de couverts\n4. Laissez FoodEatUp assigner automatiquement la meilleure table, ou choisissez-en une précisément parmi les tables disponibles\n5. Cliquez sur \"Créer la réservation\" : elle apparaît aussitôt dans votre liste, en statut En attente\n6. Confirmez-la, installez le client (Check-in) ou déclarez un no-show directement depuis le menu d'actions de la ligne\n\n**Astuce du chef** : Dès qu'un client arrive, confirmez sa réservation ou installez-le directement (Check-in) depuis le menu d'actions de la ligne, sans ressaisir ses informations. Un no-show se déclare en un clic pour garder l'historique propre et libérer la table pour d'autres clients.\n\n---",
              "correspondance": "numéro",
              "confiance": 1.0
            },
            "tutorielModuleUrl": "https://tutoriel.foodeatup.com/module/reservation-salle",
            "higgsfield": {
              "videoSourceUrl": null,
              "duree": "10 s",
              "format": "vertical 9:16",
              "source": null
            },
            "masterRapidoUrl": null
          },
          {
            "id": "EP092",
            "numero": 92,
            "saison": 4,
            "slug": "ep092-le-super-heros-qui-a-reserve",
            "titre": "Le super-héros qui a réservé",
            "module": "Réservation",
            "chapitre": "3 - Gérer et no-shows",
            "accroche": "Lui, il avait réservé.",
            "punchline": "Ses quatre-vingts fans, non.",
            "resume": "Quatre-vingts personnes d'un coup, ça se voit venir. Tu ouvres ou tu fermes tes créneaux en direct, et la liste d'attente prend le relais.",
            "statut": "a_produire",
            "dureeSecondes": null,
            "videoUrl": null,
            "reseaux": {
              "facebook": {
                "statut": "a_venir",
                "date": "2026-10-24",
                "heure": "12:00",
                "compte": "FoodEatUp",
                "format": "Vidéo native 9:16",
                "lienCta": "https://site.foodeatup.com/"
              },
              "instagram": {
                "statut": "a_venir",
                "date": "2026-10-24",
                "heure": "18:30",
                "compte": "foodeatup.cocuisinage",
                "format": "Reel 9:16",
                "lienCta": null
              },
              "tiktok": {
                "statut": "a_venir",
                "date": "2026-10-24",
                "heure": "19:00",
                "compte": "foodeatup",
                "format": "Vidéo 9:16",
                "lienCta": null
              },
              "linkedin": {
                "statut": "a_venir",
                "date": "2026-10-24",
                "heure": "08:00",
                "compte": "FoodEatUp",
                "format": "Vidéo native 9:16",
                "lienCta": "https://site.foodeatup.com/"
              },
              "youtube": {
                "statut": "a_venir",
                "date": "2026-10-24",
                "heure": "10:00",
                "compte": "@FoodEatUp",
                "format": "Short 9:16",
                "lienCta": "https://site.foodeatup.com/"
              }
            },
            "posterUrl": null,
            "datePrevue": "2026-10-24",
            "troisMots": "GÉRER ET NO-SHOWS",
            "tutoriel": {
              "titre": "Gérer ses no-shows et modifications",
              "slug": "gerer-ses-no-shows",
              "url": "https://tutoriel.foodeatup.com/tutoriel/gerer-ses-no-shows",
              "module": "Réservations & Plan de salle",
              "etape": "Créer & modifier\n- **Statut** : En ligne (0 min 44 s)\n- **Vidéo** : https://rapido-software.s3.eu-west-3.amazonaws.com/rapidosoftware/cms/bibliotheque/foodeatup-noshow-tuto-v1\n\n**Description (à quoi ça sert)**\n\nUne réservation évolue rarement telle quelle jusqu'au service : le client change d'heure ou de nombre de couverts, ne se présente pas, ou annule complètement. Plutôt que de naviguer entre plusieurs écrans, ce menu centralise toutes les actions sur la ligne de réservation elle-même : modifier les détails, marquer une absence (no-show) pour libérer la table aussitôt, ou supprimer définitivement une réservation obsolète, avec une confirmation avant toute suppression.\n\n**Comment ça marche**\n\n1. Depuis Réservations, ouvrez le menu à trois points sur la ligne concernée\n2. Cliquez sur Modifier pour changer l'horaire, le nombre de couverts ou la table\n3. Le client ne s'est pas présenté ? Cliquez sur No-show pour libérer la table immédiatement\n4. Une réservation à supprimer définitivement ? Le même menu propose aussi cette option, avec confirmation avant suppression\n\n**Astuce du chef** : Marquez le no-show dès que vous constatez l'absence, pas en fin de service — la table se libère immédiatement pour être réattribuée à un autre client, et vos statistiques de fréquentation restent fiables. Le menu d'actions s'adapte au statut de la réservation : une fois en no-show, seules Modifier et Supprimer restent proposées, plus besoin de chercher parmi des actions qui ne s'appliquent plus.\n\n---",
              "correspondance": "numéro",
              "confiance": 1.0
            },
            "tutorielModuleUrl": "https://tutoriel.foodeatup.com/module/reservation-salle",
            "higgsfield": {
              "videoSourceUrl": null,
              "duree": "10 s",
              "format": "vertical 9:16",
              "source": null
            },
            "masterRapidoUrl": null
          },
          {
            "id": "EP093",
            "numero": 93,
            "saison": 4,
            "slug": "ep093-le-chef-part-a-la-peche",
            "titre": "Le chef part à la pêche",
            "module": "StockVision",
            "chapitre": "3 - Prédictions des commandes",
            "accroche": "Rupture de stock, 20 h 15.",
            "punchline": "Anticiper, c'est moins sportif.",
            "resume": "FoodEatUp prévoit tes ventes de poisson à partir de ton historique. Tu commandes la bonne quantité le mardi, pas la canne à pêche le samedi.",
            "statut": "a_produire",
            "dureeSecondes": null,
            "videoUrl": null,
            "reseaux": {
              "facebook": {
                "statut": "a_venir",
                "date": "2026-10-25",
                "heure": "12:00",
                "compte": "FoodEatUp",
                "format": "Vidéo native 9:16",
                "lienCta": "https://site.foodeatup.com/"
              },
              "instagram": {
                "statut": "a_venir",
                "date": "2026-10-25",
                "heure": "18:30",
                "compte": "foodeatup.cocuisinage",
                "format": "Reel 9:16",
                "lienCta": null
              },
              "tiktok": {
                "statut": "a_venir",
                "date": "2026-10-25",
                "heure": "19:00",
                "compte": "foodeatup",
                "format": "Vidéo 9:16",
                "lienCta": null
              },
              "linkedin": {
                "statut": "a_venir",
                "date": "2026-10-25",
                "heure": "08:00",
                "compte": "FoodEatUp",
                "format": "Vidéo native 9:16",
                "lienCta": "https://site.foodeatup.com/"
              },
              "youtube": {
                "statut": "a_venir",
                "date": "2026-10-25",
                "heure": "10:00",
                "compte": "@FoodEatUp",
                "format": "Short 9:16",
                "lienCta": "https://site.foodeatup.com/"
              }
            },
            "posterUrl": null,
            "datePrevue": "2026-10-25",
            "troisMots": "PRÉDICTIONS DES COMMANDES",
            "tutoriel": {
              "titre": "Prédire ses commandes (ventes & production) FoodEatUp",
              "slug": "predire-ses-commandes",
              "url": "https://tutoriel.foodeatup.com/tutoriel/predire-ses-commandes",
              "module": "StockVision AI",
              "etape": "Ma carte & recettes\n- **Statut** : En ligne (0 min 39 s)\n- **Vidéo** : https://rapido-software.s3.eu-west-3.amazonaws.com/rapidosoftware/cms/bibliotheque/predire-ses-commandes-v1\n\n**Description (à quoi ça sert)**\n\nAnticiper les commandes à venir, plat par plat, pour ajuster vos quantités de production sans deviner — moins de ruptures en service, moins de gaspillage en cuisine.\n\n**Comment ça marche**\n\n1. Depuis Ma carte, repérez le plat à analyser — ici la Pizza Margherita napolitaine\n2. Cliquez sur l'icône graphique de sa carte pour ouvrir ses prédictions\n3. PrediBot affiche les commandes estimées jour par jour sur 7 ou 30 jours, avec l'indice de performance IA et le niveau de confiance du modèle\n4. Cliquez sur \"Exporter PDF\" pour télécharger le rapport et le partager avec votre équipe en cuisine\n\n**Astuce du chef** : Un indice de confiance \"Faible\" ne signifie pas que la prédiction est fausse : c'est fréquent en début d'historique de ventes, le temps que PrediBot accumule assez de données pour affiner ses estimations. Recroisez toujours l'estimation IA avec votre propre lecture du service avant d'ajuster votre production, surtout les premières semaines.\n\n---",
              "correspondance": "numéro",
              "confiance": 1.0
            },
            "tutorielModuleUrl": "https://tutoriel.foodeatup.com/module/stockvision-ai",
            "higgsfield": {
              "videoSourceUrl": null,
              "duree": "10 s",
              "format": "vertical 9:16",
              "source": null
            },
            "masterRapidoUrl": null
          },
          {
            "id": "EP094",
            "numero": 94,
            "saison": 4,
            "slug": "ep094-le-robot-livreur-qui-double-le-scooter",
            "titre": "Le robot livreur qui double le scooter",
            "module": "HubRise",
            "chapitre": "4 - Centraliser les commandes",
            "accroche": "2026, la livraison change de main.",
            "punchline": "Autant que tes commandes arrivent au bon endroit.",
            "resume": "Peu importe qui livre. Tes commandes arrivent dans la même file, avec la bonne adresse et le bon statut, jusqu'à la remise au client.",
            "statut": "bloque",
            "dureeSecondes": null,
            "videoUrl": null,
            "reseaux": {
              "facebook": {
                "statut": "a_venir",
                "date": null,
                "heure": "12:00",
                "compte": "FoodEatUp",
                "format": "Vidéo native 9:16",
                "lienCta": "https://site.foodeatup.com/"
              },
              "instagram": {
                "statut": "a_venir",
                "date": null,
                "heure": "18:30",
                "compte": "foodeatup.cocuisinage",
                "format": "Reel 9:16",
                "lienCta": null
              },
              "tiktok": {
                "statut": "a_venir",
                "date": null,
                "heure": "19:00",
                "compte": "foodeatup",
                "format": "Vidéo 9:16",
                "lienCta": null
              },
              "linkedin": {
                "statut": "a_venir",
                "date": null,
                "heure": "08:00",
                "compte": "FoodEatUp",
                "format": "Vidéo native 9:16",
                "lienCta": "https://site.foodeatup.com/"
              },
              "youtube": {
                "statut": "a_venir",
                "date": null,
                "heure": "10:00",
                "compte": "@FoodEatUp",
                "format": "Short 9:16",
                "lienCta": "https://site.foodeatup.com/"
              }
            },
            "blocage": "Le chapitre correspondant n'a pas encore de vidéo dans le Drive interne.",
            "posterUrl": null,
            "datePrevue": null,
            "troisMots": "CENTRALISER LES COMMANDES",
            "tutoriel": {
              "titre": "flux livraison",
              "slug": "centraliser-les-commandes-livraison",
              "url": "https://tutoriel.foodeatup.com/tutoriel/centraliser-les-commandes-livraison",
              "module": "HubRise & Livraisons",
              "etape": "Flux de commandes\n- **Statut** : Bientôt disponible (tournage en cours)\n\n**Description (à quoi ça sert)**\n\nCentraliser les commandes — flux livraison — tutoriel en préparation dans le module HubRise & Livraisons. Il arrive très bientôt dans ce fil conducteur.\n\n**Comment ça marche**\n\n1. Cette vidéo est en cours de tournage dans les cuisines FoodEatUp.\n2. Sa fiche est déjà en place : elle se remplira dès la mise en ligne.\n\n---",
              "correspondance": "numéro",
              "confiance": 1.0
            },
            "tutorielModuleUrl": "https://tutoriel.foodeatup.com/module/hubrise-livraisons",
            "higgsfield": {
              "videoSourceUrl": null,
              "duree": "10 s",
              "format": "vertical 9:16",
              "source": null
            },
            "masterRapidoUrl": null
          },
          {
            "id": "EP095",
            "numero": 95,
            "saison": 4,
            "slug": "ep095-l-eclipse-de-13-h-12",
            "titre": "L'éclipse de 13 h 12",
            "module": "KDS",
            "chapitre": "3 - Gérer le KDS en direct",
            "accroche": "Le service s'est arrêté deux minutes.",
            "punchline": "Le reste du temps, il ne devrait jamais s'arrêter.",
            "resume": "Sur le KDS, chaque plat a son chrono. Tu vois ce qui traîne au moment où ça traîne, et tu relances le bon poste.",
            "statut": "bloque",
            "dureeSecondes": null,
            "videoUrl": null,
            "reseaux": {
              "facebook": {
                "statut": "a_venir",
                "date": null,
                "heure": "12:00",
                "compte": "FoodEatUp",
                "format": "Vidéo native 9:16",
                "lienCta": "https://site.foodeatup.com/"
              },
              "instagram": {
                "statut": "a_venir",
                "date": null,
                "heure": "18:30",
                "compte": "foodeatup.cocuisinage",
                "format": "Reel 9:16",
                "lienCta": null
              },
              "tiktok": {
                "statut": "a_venir",
                "date": null,
                "heure": "19:00",
                "compte": "foodeatup",
                "format": "Vidéo 9:16",
                "lienCta": null
              },
              "linkedin": {
                "statut": "a_venir",
                "date": null,
                "heure": "08:00",
                "compte": "FoodEatUp",
                "format": "Vidéo native 9:16",
                "lienCta": "https://site.foodeatup.com/"
              },
              "youtube": {
                "statut": "a_venir",
                "date": null,
                "heure": "10:00",
                "compte": "@FoodEatUp",
                "format": "Short 9:16",
                "lienCta": "https://site.foodeatup.com/"
              }
            },
            "blocage": "Le chapitre correspondant n'a pas encore de vidéo dans le Drive interne.",
            "posterUrl": null,
            "datePrevue": null,
            "troisMots": "GÉRER KDS DIRECT",
            "tutoriel": {
              "titre": "Gérer une commande en direct sur le KDS",
              "slug": "gerer-une-commande-en-direct-kds",
              "url": "https://tutoriel.foodeatup.com/tutoriel/gerer-une-commande-en-direct-kds",
              "module": "Écran Cuisine (KDS)",
              "etape": "Gérer une commande\n- **Statut** : Bientôt disponible (tournage en cours)\n\n**Description (à quoi ça sert)**\n\nGérer une commande en direct sur le KDS — tutoriel en préparation dans le module Écran Cuisine (KDS). Il arrive très bientôt dans ce fil conducteur.\n\n**Comment ça marche**\n\n1. Cette vidéo est en cours de tournage dans les cuisines FoodEatUp.\n2. Sa fiche est déjà en place : elle se remplira dès la mise en ligne.\n\n---",
              "correspondance": "numéro",
              "confiance": 1.0
            },
            "tutorielModuleUrl": "https://tutoriel.foodeatup.com/module/kds-cuisine",
            "higgsfield": {
              "videoSourceUrl": null,
              "duree": "10 s",
              "format": "vertical 9:16",
              "source": null
            },
            "masterRapidoUrl": null
          },
          {
            "id": "EP096",
            "numero": 96,
            "saison": 4,
            "slug": "ep096-canicule-le-beurre-fugueur",
            "titre": "Canicule : le beurre fugueur",
            "module": "HACCP",
            "chapitre": "relevé de température",
            "accroche": "39° en cuisine.",
            "punchline": "Une alerte température, et tu sauves la marchandise.",
            "resume": "Trente-neuf degrés en cuisine, ton frigo souffre. Le relevé hors seuil te prévient tout de suite. Tu sauves la marchandise.",
            "statut": "a_produire",
            "dureeSecondes": null,
            "videoUrl": null,
            "reseaux": {
              "facebook": {
                "statut": "a_venir",
                "date": "2026-10-26",
                "heure": "12:00",
                "compte": "FoodEatUp",
                "format": "Vidéo native 9:16",
                "lienCta": "https://site.foodeatup.com/"
              },
              "instagram": {
                "statut": "a_venir",
                "date": "2026-10-26",
                "heure": "18:30",
                "compte": "foodeatup.cocuisinage",
                "format": "Reel 9:16",
                "lienCta": null
              },
              "tiktok": {
                "statut": "a_venir",
                "date": "2026-10-26",
                "heure": "19:00",
                "compte": "foodeatup",
                "format": "Vidéo 9:16",
                "lienCta": null
              },
              "linkedin": {
                "statut": "a_venir",
                "date": "2026-10-26",
                "heure": "08:00",
                "compte": "FoodEatUp",
                "format": "Vidéo native 9:16",
                "lienCta": "https://site.foodeatup.com/"
              },
              "youtube": {
                "statut": "a_venir",
                "date": "2026-10-26",
                "heure": "10:00",
                "compte": "@FoodEatUp",
                "format": "Short 9:16",
                "lienCta": "https://site.foodeatup.com/"
              }
            },
            "posterUrl": null,
            "datePrevue": "2026-10-26",
            "troisMots": "RELEVÉ DE TEMPÉRATURE",
            "tutoriel": {
              "titre": "Relever une température d'équipement",
              "slug": "relever-une-temperature-equipement",
              "url": "https://tutoriel.foodeatup.com/tutoriel/relever-une-temperature-equipement",
              "module": "Hygiène & HACCP",
              "etape": "Températures & équipements\n- **Statut** : En ligne (0 min 38 s)\n- **Vidéo** : https://rapido-software.s3.eu-west-3.amazonaws.com/rapidosoftware/cms/bibliotheque/foodeatup-temperature-tuto-v1.mp4\n\n**Description (à quoi ça sert)**\n\nTenir votre registre de températures au moment du relevé, pas le soir de mémoire ni sur une feuille scotchée à la porte du frigo. Chaque valeur saisie est datée, horodatée et rattachée à son équipement, puis confrontée automatiquement à la plage cible que vous avez définie : ce qui sort des clous est marqué non conforme immédiatement, pendant que vous êtes encore devant l'équipement et que vous pouvez agir. C'est ce qui transforme un contrôle de routine en historique HACCP présentable à un inspecteur.\n\n**Comment ça marche**\n\n1. Ouvrez Hygiène & HACCP puis \"Températures\" : l'onglet Équipements liste vos frigos, congélateurs et chambres froides\n2. Chaque ligne affiche la plage cible de l'équipement — ici Frigo 5, min 0 °C, max 4 °C\n3. Ajustez la valeur relevée avec les boutons − et + de la colonne Température\n4. Cliquez sur \"Enregistrer les relevés de température\" en bas de la page\n5. Confirmez dans la fenêtre \"Enregistrer les relevés ?\", qui récapitule le nombre d'équipements et de plats modifiés\n6. Validez le message \"Enregistré ! Les relevés ont été sauvegardés avec succès.\"\n7. Les compteurs du jour se recalculent aussitôt : Total aujourd'hui, Conformes, Alertes et Non conformes\n8. Un relevé hors plage bascule directement en non conforme — 9 °C pour un maximum de 4 °C part en non conforme, sans intervention de votre part\n\n**Astuce du chef** : Relevez toujours aux mêmes moments — ouverture et fermeture — plutôt que « quand on y pense » : un historique régulier vaut bien mieux qu'un historique dense mais troué, c'est la régularité que regarde l'inspecteur. Et ne « corrigez » jamais une valeur hors plage pour faire propre : un 9 °C tracé, daté et suivi d'une action est votre meilleure défense, alors qu'un 4 °C confortable sur un frigo qui dérive ne protège personne — surtout pas vos stocks.\n\n---",
              "correspondance": "texte",
              "confiance": 0.73
            },
            "tutorielModuleUrl": "https://tutoriel.foodeatup.com/module/haccp",
            "higgsfield": {
              "videoSourceUrl": null,
              "duree": "10 s",
              "format": "vertical 9:16",
              "source": null
            },
            "masterRapidoUrl": null
          },
          {
            "id": "EP097",
            "numero": 97,
            "saison": 4,
            "slug": "ep097-le-mur-de-tablettes",
            "titre": "Le mur de tablettes",
            "module": "HubRise",
            "chapitre": "2 - Relier Uber Eats et Deliveroo",
            "accroche": "Six plateformes. Six alertes.",
            "punchline": "Une seule commande, un seul écran.",
            "resume": "Tes plateformes envoient tout dans FoodEatUp. Six alertes deviennent une file de commandes. La tablette murale, tu peux la ranger.",
            "statut": "bloque",
            "dureeSecondes": null,
            "videoUrl": null,
            "reseaux": {
              "facebook": {
                "statut": "a_venir",
                "date": null,
                "heure": "12:00",
                "compte": "FoodEatUp",
                "format": "Vidéo native 9:16",
                "lienCta": "https://site.foodeatup.com/"
              },
              "instagram": {
                "statut": "a_venir",
                "date": null,
                "heure": "18:30",
                "compte": "foodeatup.cocuisinage",
                "format": "Reel 9:16",
                "lienCta": null
              },
              "tiktok": {
                "statut": "a_venir",
                "date": null,
                "heure": "19:00",
                "compte": "foodeatup",
                "format": "Vidéo 9:16",
                "lienCta": null
              },
              "linkedin": {
                "statut": "a_venir",
                "date": null,
                "heure": "08:00",
                "compte": "FoodEatUp",
                "format": "Vidéo native 9:16",
                "lienCta": "https://site.foodeatup.com/"
              },
              "youtube": {
                "statut": "a_venir",
                "date": null,
                "heure": "10:00",
                "compte": "@FoodEatUp",
                "format": "Short 9:16",
                "lienCta": "https://site.foodeatup.com/"
              }
            },
            "blocage": "Le chapitre correspondant n'a pas encore de vidéo dans le Drive interne.",
            "posterUrl": null,
            "datePrevue": null,
            "troisMots": "RELIER UBER EATS",
            "tutoriel": {
              "titre": "Relier Uber Eats & Deliveroo via HubRise",
              "slug": "relier-uber-eats-et-deliveroo",
              "url": "https://tutoriel.foodeatup.com/tutoriel/relier-uber-eats-et-deliveroo",
              "module": "HubRise & Livraisons",
              "etape": "Plateformes de livraison\n- **Statut** : Bientôt disponible (tournage en cours)\n\n**Description (à quoi ça sert)**\n\nRelier Uber Eats & Deliveroo via HubRise — tutoriel en préparation dans le module HubRise & Livraisons. Il arrive très bientôt dans ce fil conducteur.\n\n**Comment ça marche**\n\n1. Cette vidéo est en cours de tournage dans les cuisines FoodEatUp.\n2. Sa fiche est déjà en place : elle se remplira dès la mise en ligne.\n\n---",
              "correspondance": "numéro",
              "confiance": 1.0
            },
            "tutorielModuleUrl": "https://tutoriel.foodeatup.com/module/hubrise-livraisons",
            "higgsfield": {
              "videoSourceUrl": null,
              "duree": "10 s",
              "format": "vertical 9:16",
              "source": null
            },
            "masterRapidoUrl": null
          },
          {
            "id": "EP098",
            "numero": 98,
            "saison": 4,
            "slug": "ep098-le-robot-serveur-qui-bugge-et-danse",
            "titre": "Le robot serveur qui bugge et danse",
            "module": "Service",
            "chapitre": "1 - Commandes multi-canaux",
            "accroche": "Ton nouveau serveur, en période d'essai.",
            "punchline": "L'IA, c'est utile quand elle sert à quelque chose.",
            "resume": "L'intelligence utile, c'est celle qui range tes commandes, pas celle qui danse. Ici, chaque canal alimente le même service.",
            "statut": "a_produire",
            "dureeSecondes": null,
            "videoUrl": null,
            "reseaux": {
              "facebook": {
                "statut": "a_venir",
                "date": "2026-10-27",
                "heure": "12:00",
                "compte": "FoodEatUp",
                "format": "Vidéo native 9:16",
                "lienCta": "https://site.foodeatup.com/"
              },
              "instagram": {
                "statut": "a_venir",
                "date": "2026-10-27",
                "heure": "18:30",
                "compte": "foodeatup.cocuisinage",
                "format": "Reel 9:16",
                "lienCta": null
              },
              "tiktok": {
                "statut": "a_venir",
                "date": "2026-10-27",
                "heure": "19:00",
                "compte": "foodeatup",
                "format": "Vidéo 9:16",
                "lienCta": null
              },
              "linkedin": {
                "statut": "a_venir",
                "date": "2026-10-27",
                "heure": "08:00",
                "compte": "FoodEatUp",
                "format": "Vidéo native 9:16",
                "lienCta": "https://site.foodeatup.com/"
              },
              "youtube": {
                "statut": "a_venir",
                "date": "2026-10-27",
                "heure": "10:00",
                "compte": "@FoodEatUp",
                "format": "Short 9:16",
                "lienCta": "https://site.foodeatup.com/"
              }
            },
            "posterUrl": null,
            "datePrevue": "2026-10-27",
            "troisMots": "COMMANDES MULTI-CANAUX",
            "tutoriel": {
              "titre": "Mes commandes : QR code, site web, agent vocal (toutes vos commandes)",
              "slug": "mes-commandes-tous-canaux",
              "url": "https://tutoriel.foodeatup.com/tutoriel/mes-commandes-tous-canaux",
              "module": "Service Multi-Canal",
              "etape": "Recevoir ses commandes\n- **Statut** : En ligne (1 min 09 s)\n- **Vidéo** : https://rapido-software.s3.eu-west-3.amazonaws.com/rapidosoftware/cms/bibliotheque/foodeatup-mes-commandes-tuto-v1\n\n**Description (à quoi ça sert)**\n\nCentraliser toutes vos commandes — QR code table, site vitrine, agent vocal ou saisie manuelle — dans une seule liste, avec canal, statut et total visibles d'un coup d'œil. Créez, modifiez ou supprimez une commande sans changer d'écran.\n\n**Comment ça marche**\n\n1. Ouvrez \"Mes commandes\" : la liste complète, avec le canal (Manuel, Vitrine, Sur place...), le statut et le total de chaque commande\n2. Cliquez sur \"+ Nouvelle commande\" pour en créer une manuellement\n3. Renseignez le client, le canal, le mode de service, puis ajoutez vos plats\n4. Cliquez sur \"Créer la commande\" : la facture et le devis sont générés automatiquement\n5. Cliquez sur une commande pour voir son détail, ou sur \"Modifier\" pour ajuster les articles et le statut, puis \"Mettre à jour\"\n6. Pour la retirer : menu \"⋮\" > \"Supprimer\", puis confirmez\n\n**Astuce du chef** : Le canal affiché sur chaque ligne (Manuel, Vitrine, Sur place...) vous dit immédiatement d'où vient la commande sans avoir à l'ouvrir — utile en coup de feu pour prioriser. Et avant de supprimer une commande, vérifiez sa facture/devis liés (visibles dans le détail) : une commande facturée qui disparaît laisse la facture orpheline, mieux vaut parfois la passer en \"Annulée\" plutôt que la supprimer.\n\n---",
              "correspondance": "numéro",
              "confiance": 1.0
            },
            "tutorielModuleUrl": "https://tutoriel.foodeatup.com/module/service-commande",
            "higgsfield": {
              "videoSourceUrl": null,
              "duree": "10 s",
              "format": "vertical 9:16",
              "source": null
            },
            "masterRapidoUrl": null
          },
          {
            "id": "EP099",
            "numero": 99,
            "saison": 4,
            "slug": "ep099-le-repondeur-prehistorique",
            "titre": "Le répondeur préhistorique",
            "module": "Caroline",
            "chapitre": "1 - Configurer voix et prompts",
            "accroche": "Quarante appels pendant le rush.",
            "punchline": "Quelqu'un devrait répondre. Ce ne sera pas toi.",
            "resume": "Caroline répond au téléphone pendant ton rush. Elle prend la réservation, la note, et te la remonte. Aucun appel ne tombe dans le vide.",
            "statut": "a_produire",
            "dureeSecondes": null,
            "videoUrl": null,
            "reseaux": {
              "facebook": {
                "statut": "a_venir",
                "date": "2026-10-28",
                "heure": "12:00",
                "compte": "FoodEatUp",
                "format": "Vidéo native 9:16",
                "lienCta": "https://site.foodeatup.com/"
              },
              "instagram": {
                "statut": "a_venir",
                "date": "2026-10-28",
                "heure": "18:30",
                "compte": "foodeatup.cocuisinage",
                "format": "Reel 9:16",
                "lienCta": null
              },
              "tiktok": {
                "statut": "a_venir",
                "date": "2026-10-28",
                "heure": "19:00",
                "compte": "foodeatup",
                "format": "Vidéo 9:16",
                "lienCta": null
              },
              "linkedin": {
                "statut": "a_venir",
                "date": "2026-10-28",
                "heure": "08:00",
                "compte": "FoodEatUp",
                "format": "Vidéo native 9:16",
                "lienCta": "https://site.foodeatup.com/"
              },
              "youtube": {
                "statut": "a_venir",
                "date": "2026-10-28",
                "heure": "10:00",
                "compte": "@FoodEatUp",
                "format": "Short 9:16",
                "lienCta": "https://site.foodeatup.com/"
              }
            },
            "posterUrl": null,
            "datePrevue": "2026-10-28",
            "troisMots": "CONFIGURER VOIX PROMPTS",
            "tutoriel": {
              "titre": "Configurer Caroline (voix & prompts)",
              "slug": "configurer-caroline-voix-prompts",
              "url": "https://tutoriel.foodeatup.com/tutoriel/configurer-caroline-voix-prompts",
              "module": "Agent IA Caroline",
              "etape": "Configurer Caroline\n- **Statut** : En ligne (0 min 43 s)\n- **Vidéo** : https://rapido-software.s3.eu-west-3.amazonaws.com/rapidosoftware/cms/bibliotheque/foodeatup-caroline-voix-tuto-v1\n\n**Description (à quoi ça sert)**\n\nRégler la voix, la langue et le message d'accueil de Caroline, votre agent vocal, puis utiliser la Marketplace de prompts FoodEatUp pour piloter vos outils directement depuis Claude — sans jamais quitter la conversation.\n\n**Comment ça marche**\n\n1. Ouvrez Agent IA Caroline puis Configuration voix.\n2. Choisissez la voix, la langue et le numéro de votre agent vocal dans Voix & téléphone.\n3. Personnalisez le message d'accueil que Caroline utilise pour répondre au téléphone.\n4. Cliquez sur Enregistrer : la configuration est appliquée aussitôt.\n5. Ouvrez la Marketplace de prompts depuis le menu de votre profil.\n6. Filtrez par catégorie (ex. Commandes) et copiez un prompt prêt à l'emploi.\n7. Collez-le dans Claude : il orchestre aussitôt vos outils FoodEatUp à votre place.\n\n**Astuce du chef** : Testez toujours votre message d'accueil dans le Simulateur de conversation avant de l'appliquer en production, ou appelez directement le numéro de l'agent pour entendre Caroline en conditions réelles.\n\n---",
              "correspondance": "numéro",
              "confiance": 1.0
            },
            "tutorielModuleUrl": "https://tutoriel.foodeatup.com/module/caroline-ia",
            "higgsfield": {
              "videoSourceUrl": null,
              "duree": "10 s",
              "format": "vertical 9:16",
              "source": null
            },
            "masterRapidoUrl": null
          },
          {
            "id": "EP100",
            "numero": 100,
            "saison": 4,
            "slug": "ep100-l-influenceur-au-ring-light",
            "titre": "L'influenceur au ring light",
            "module": "Marketing",
            "chapitre": "1 - Débloquer les avis",
            "accroche": "Il a mis vingt minutes à filmer.",
            "punchline": "Et deux minutes à te mettre deux étoiles.",
            "resume": "Tes avis remontent au même endroit, site et Google. Tu réponds à celui qui t'a mis deux étoiles avant qu'il devienne ta vitrine.",
            "statut": "a_produire",
            "dureeSecondes": null,
            "videoUrl": null,
            "reseaux": {
              "facebook": {
                "statut": "a_venir",
                "date": "2026-10-29",
                "heure": "12:00",
                "compte": "FoodEatUp",
                "format": "Vidéo native 9:16",
                "lienCta": "https://site.foodeatup.com/"
              },
              "instagram": {
                "statut": "a_venir",
                "date": "2026-10-29",
                "heure": "18:30",
                "compte": "foodeatup.cocuisinage",
                "format": "Reel 9:16",
                "lienCta": null
              },
              "tiktok": {
                "statut": "a_venir",
                "date": "2026-10-29",
                "heure": "19:00",
                "compte": "foodeatup",
                "format": "Vidéo 9:16",
                "lienCta": null
              },
              "linkedin": {
                "statut": "a_venir",
                "date": "2026-10-29",
                "heure": "08:00",
                "compte": "FoodEatUp",
                "format": "Vidéo native 9:16",
                "lienCta": "https://site.foodeatup.com/"
              },
              "youtube": {
                "statut": "a_venir",
                "date": "2026-10-29",
                "heure": "10:00",
                "compte": "@FoodEatUp",
                "format": "Short 9:16",
                "lienCta": "https://site.foodeatup.com/"
              }
            },
            "posterUrl": null,
            "datePrevue": "2026-10-29",
            "troisMots": "DÉBLOQUER LES AVIS",
            "tutoriel": {
              "titre": "Débloquer les Avis clients",
              "slug": "debloquer-les-avis-clients",
              "url": "https://tutoriel.foodeatup.com/tutoriel/debloquer-les-avis-clients",
              "module": "Marketing, Fidélité & Iris",
              "etape": "Avis clients\n- **Statut** : En ligne (0 min 39 s)\n- **Vidéo** : https://rapido-software.s3.eu-west-3.amazonaws.com/rapidosoftware/cms/bibliotheque/foodeatup-avis-abonnement-tuto-v1.mp4\n\n**Description (à quoi ça sert)**\n\nDébloquer la collecte automatique des avis Google et des réponses IA prêtes à publier, pour surveiller votre e-réputation sans y passer des heures — 29€/mois ajoutés à votre abonnement StockVision existant.\n\n**Comment ça marche**\n\n1. Dans Options et modules, repérez la carte Avis & réputation Google (29€/mois)\n2. Cliquez sur Ajouter cette option pour l'ajouter à votre abonnement\n3. Vérifiez le récapitulatif de commande, puis cliquez sur Continuer vers le paiement\n4. Finalisez votre abonnement sur la page de paiement sécurisée Stripe\n5. Votre plan est mis à jour immédiatement après le paiement\n\n**Astuce du chef** : Cette option s'empile sur votre pack actuel, elle ne le remplace pas — inutile de changer d'abonnement principal. Le paiement passe par Stripe : gardez un œil sur la date de prochaine facturation affichée en haut de la page Abonnement.\n\n---",
              "correspondance": "numéro",
              "confiance": 1.0
            },
            "tutorielModuleUrl": "https://tutoriel.foodeatup.com/module/marketing-fidelite",
            "higgsfield": {
              "videoSourceUrl": null,
              "duree": "10 s",
              "format": "vertical 9:16",
              "source": null
            },
            "masterRapidoUrl": null
          },
          {
            "id": "EP101",
            "numero": 101,
            "saison": 4,
            "slug": "ep101-pov-thriller-comptable",
            "titre": "POV : thriller comptable",
            "module": "Caisse POS",
            "chapitre": "6 - Clôturer sa caisse",
            "accroche": "Rapprochement des caisses. Vendredi soir.",
            "punchline": "Ça devrait être une ligne, pas une enquête.",
            "resume": "La clôture, c'est un bouton. Le détail par moyen de paiement, la TVA, l'écart : tout est là, sans calculatrice ni suspense.",
            "statut": "bloque",
            "dureeSecondes": null,
            "videoUrl": null,
            "reseaux": {
              "facebook": {
                "statut": "a_venir",
                "date": null,
                "heure": "12:00",
                "compte": "FoodEatUp",
                "format": "Vidéo native 9:16",
                "lienCta": "https://site.foodeatup.com/"
              },
              "instagram": {
                "statut": "a_venir",
                "date": null,
                "heure": "18:30",
                "compte": "foodeatup.cocuisinage",
                "format": "Reel 9:16",
                "lienCta": null
              },
              "tiktok": {
                "statut": "a_venir",
                "date": null,
                "heure": "19:00",
                "compte": "foodeatup",
                "format": "Vidéo 9:16",
                "lienCta": null
              },
              "linkedin": {
                "statut": "a_venir",
                "date": null,
                "heure": "08:00",
                "compte": "FoodEatUp",
                "format": "Vidéo native 9:16",
                "lienCta": "https://site.foodeatup.com/"
              },
              "youtube": {
                "statut": "a_venir",
                "date": null,
                "heure": "10:00",
                "compte": "@FoodEatUp",
                "format": "Short 9:16",
                "lienCta": "https://site.foodeatup.com/"
              }
            },
            "blocage": "Le chapitre correspondant n'a pas encore de vidéo dans le Drive interne.",
            "posterUrl": null,
            "datePrevue": null,
            "troisMots": "CLÔTURER SA CAISSE",
            "tutoriel": null,
            "tutorielModuleUrl": null,
            "tutorielManquant": "Le module Caisse POS n'existe pas encore dans l'Academy.",
            "higgsfield": {
              "videoSourceUrl": null,
              "duree": "10 s",
              "format": "vertical 9:16",
              "source": null
            },
            "masterRapidoUrl": null
          },
          {
            "id": "EP102",
            "numero": 102,
            "saison": 4,
            "slug": "ep102-l-inspecteur-surprise",
            "titre": "L'inspecteur surprise",
            "module": "HACCP",
            "chapitre": "checklists hygiène",
            "accroche": "Contrôle surprise. Ou pas.",
            "punchline": "Le jour où c'est le vrai, tu ne bouges pas.",
            "resume": "Ta checklist est validée chaque jour par ton équipe. Le jour du vrai contrôle, tu ouvres l'historique et tu ne bouges pas.",
            "statut": "a_produire",
            "dureeSecondes": null,
            "videoUrl": null,
            "reseaux": {
              "facebook": {
                "statut": "a_venir",
                "date": "2026-10-30",
                "heure": "12:00",
                "compte": "FoodEatUp",
                "format": "Vidéo native 9:16",
                "lienCta": "https://site.foodeatup.com/"
              },
              "instagram": {
                "statut": "a_venir",
                "date": "2026-10-30",
                "heure": "18:30",
                "compte": "foodeatup.cocuisinage",
                "format": "Reel 9:16",
                "lienCta": null
              },
              "tiktok": {
                "statut": "a_venir",
                "date": "2026-10-30",
                "heure": "19:00",
                "compte": "foodeatup",
                "format": "Vidéo 9:16",
                "lienCta": null
              },
              "linkedin": {
                "statut": "a_venir",
                "date": "2026-10-30",
                "heure": "08:00",
                "compte": "FoodEatUp",
                "format": "Vidéo native 9:16",
                "lienCta": "https://site.foodeatup.com/"
              },
              "youtube": {
                "statut": "a_venir",
                "date": "2026-10-30",
                "heure": "10:00",
                "compte": "@FoodEatUp",
                "format": "Short 9:16",
                "lienCta": "https://site.foodeatup.com/"
              }
            },
            "posterUrl": null,
            "datePrevue": "2026-10-30",
            "troisMots": "CHECKLISTS HYGIÈNE",
            "tutoriel": {
              "titre": "Créer sa check-list hygiène FoodEatUp",
              "slug": "creer-sa-checklist-hygiene",
              "url": "https://tutoriel.foodeatup.com/tutoriel/creer-sa-checklist-hygiene",
              "module": "Hygiène & HACCP",
              "etape": "Hygiène & nettoyage\n- **Statut** : En ligne (0 min 43 s)\n- **Vidéo** : https://rapido-software.s3.eu-west-3.amazonaws.com/rapidosoftware/cms/bibliotheque/foodeatup-checklist-hygiene-tuto-v1\n\n**Description (à quoi ça sert)**\n\nCréer vos propres points de contrôle hygiène (au-delà des points par défaut) et les valider directement depuis l'app, avec date, heure et zone horodatées automatiquement — une trace claire et datée de chaque contrôle, prête en cas d'inspection HACCP.\n\n**Comment ça marche**\n\n1. Depuis Hygiène, ouvrez Checklist hygiène\n2. Cliquez sur \"Ajouter une checklist\"\n3. Donnez-lui un nom, une catégorie (Hygiène du personnel ou État des locaux) et une description, puis cliquez sur \"Créer\"\n4. Elle apparaît aussitôt dans la liste, avec les points de contrôle par défaut de sa catégorie\n5. Ouvrez-la pour la valider : choisissez la zone contrôlée, cochez Oui, Non ou Non évalué, ajoutez un commentaire si besoin, puis cliquez sur \"Valider\"\n\n**Astuce du chef** : Complétez la validation au moment du contrôle réel, pas après coup — la date et l'heure sont horodatées automatiquement dès l'ouverture de la fiche, et la zone contrôlée permet de retrouver l'historique précis en cas d'inspection.\n\n---",
              "correspondance": "texte",
              "confiance": 0.77
            },
            "tutorielModuleUrl": "https://tutoriel.foodeatup.com/module/haccp",
            "higgsfield": {
              "videoSourceUrl": null,
              "duree": "10 s",
              "format": "vertical 9:16",
              "source": null
            },
            "masterRapidoUrl": null
          },
          {
            "id": "EP103",
            "numero": 103,
            "saison": 4,
            "slug": "ep103-le-car-de-40-sans-reservation",
            "titre": "Le car de 40 sans réservation",
            "module": "Réservation",
            "chapitre": "1 - Réservations du jour",
            "accroche": "Quarante couverts. Sans prévenir.",
            "punchline": "Prévenu, tu aurais dit oui.",
            "resume": "Un groupe qui arrive, tu vérifies la disponibilité réelle en trois secondes : tables libres, horaires, capacité. Tu dis oui en connaissance de cause.",
            "statut": "a_produire",
            "dureeSecondes": null,
            "videoUrl": null,
            "reseaux": {
              "facebook": {
                "statut": "a_venir",
                "date": "2026-10-31",
                "heure": "12:00",
                "compte": "FoodEatUp",
                "format": "Vidéo native 9:16",
                "lienCta": "https://site.foodeatup.com/"
              },
              "instagram": {
                "statut": "a_venir",
                "date": "2026-10-31",
                "heure": "18:30",
                "compte": "foodeatup.cocuisinage",
                "format": "Reel 9:16",
                "lienCta": null
              },
              "tiktok": {
                "statut": "a_venir",
                "date": "2026-10-31",
                "heure": "19:00",
                "compte": "foodeatup",
                "format": "Vidéo 9:16",
                "lienCta": null
              },
              "linkedin": {
                "statut": "a_venir",
                "date": "2026-10-31",
                "heure": "08:00",
                "compte": "FoodEatUp",
                "format": "Vidéo native 9:16",
                "lienCta": "https://site.foodeatup.com/"
              },
              "youtube": {
                "statut": "a_venir",
                "date": "2026-10-31",
                "heure": "10:00",
                "compte": "@FoodEatUp",
                "format": "Short 9:16",
                "lienCta": "https://site.foodeatup.com/"
              }
            },
            "posterUrl": null,
            "datePrevue": "2026-10-31",
            "troisMots": "RÉSERVATIONS DU JOUR",
            "tutoriel": {
              "titre": "Retrouver ses réservations du jour",
              "slug": "retrouver-ses-reservations-du-jour",
              "url": "https://tutoriel.foodeatup.com/tutoriel/retrouver-ses-reservations-du-jour",
              "module": "Réservations & Plan de salle",
              "etape": "Réservations du jour\n- **Statut** : En ligne (0 min 51 s)\n- **Vidéo** : https://rapido-software.s3.eu-west-3.amazonaws.com/rapidosoftware/cms/bibliotheque/foodeatup-reservations-jour-tuto\n\n**Description (à quoi ça sert)**\n\nCentraliser sur un seul écran le plan de salle en temps réel, la file d'attente et les réservations du jour — pour savoir en un coup d'œil qui arrive, où l'installer, et ce qui reste disponible, sans jongler entre plusieurs outils.\n\n**Comment ça marche**\n\n1. Ouvrez Réservations : le plan de salle affiche chaque table en temps réel, avec son statut coloré (Libre, Réservée, Occupée, À nettoyer).\n2. La file d'attente liste les clients sans réservation, prêts à être placés dès qu'une table se libère.\n3. Plus bas, la liste Réservations du jour détaille chaque arrivée attendue : heure, client, nombre de couverts.\n4. Chaque ligne affiche aussi la table déjà assignée et son statut d'installation en direct (ex. Installée).\n5. D'un coup d'œil, vous savez qui arrive, où l'installer, et ce qui reste disponible pour le service.\n\n**Astuce du chef** : Gardez un œil sur la file d'attente autant que sur les réservations : un client sans réservation peut souvent être casé sur une table libérée entre deux arrivées prévues — le plan de salle en temps réel vous montre cette fenêtre avant qu'elle ne se referme.\n\n---",
              "correspondance": "numéro",
              "confiance": 1.0
            },
            "tutorielModuleUrl": "https://tutoriel.foodeatup.com/module/reservation-salle",
            "higgsfield": {
              "videoSourceUrl": null,
              "duree": "10 s",
              "format": "vertical 9:16",
              "source": null
            },
            "masterRapidoUrl": null
          },
          {
            "id": "EP104",
            "numero": 104,
            "saison": 4,
            "slug": "ep104-le-no-show-western",
            "titre": "Le no-show western",
            "module": "Réservation",
            "chapitre": "3 - Gérer et no-shows",
            "accroche": "Table de huit. 20 h 30.",
            "punchline": "Un no-show, ça se prévient.",
            "resume": "Tu marques le no-show, la table se libère immédiatement et repart à la vente. Le client, lui, garde son historique.",
            "statut": "a_produire",
            "dureeSecondes": null,
            "videoUrl": null,
            "reseaux": {
              "facebook": {
                "statut": "a_venir",
                "date": "2026-11-01",
                "heure": "12:00",
                "compte": "FoodEatUp",
                "format": "Vidéo native 9:16",
                "lienCta": "https://site.foodeatup.com/"
              },
              "instagram": {
                "statut": "a_venir",
                "date": "2026-11-01",
                "heure": "18:30",
                "compte": "foodeatup.cocuisinage",
                "format": "Reel 9:16",
                "lienCta": null
              },
              "tiktok": {
                "statut": "a_venir",
                "date": "2026-11-01",
                "heure": "19:00",
                "compte": "foodeatup",
                "format": "Vidéo 9:16",
                "lienCta": null
              },
              "linkedin": {
                "statut": "a_venir",
                "date": "2026-11-01",
                "heure": "08:00",
                "compte": "FoodEatUp",
                "format": "Vidéo native 9:16",
                "lienCta": "https://site.foodeatup.com/"
              },
              "youtube": {
                "statut": "a_venir",
                "date": "2026-11-01",
                "heure": "10:00",
                "compte": "@FoodEatUp",
                "format": "Short 9:16",
                "lienCta": "https://site.foodeatup.com/"
              }
            },
            "posterUrl": null,
            "datePrevue": "2026-11-01",
            "troisMots": "GÉRER ET NO-SHOWS",
            "tutoriel": {
              "titre": "Gérer ses no-shows et modifications",
              "slug": "gerer-ses-no-shows",
              "url": "https://tutoriel.foodeatup.com/tutoriel/gerer-ses-no-shows",
              "module": "Réservations & Plan de salle",
              "etape": "Créer & modifier\n- **Statut** : En ligne (0 min 44 s)\n- **Vidéo** : https://rapido-software.s3.eu-west-3.amazonaws.com/rapidosoftware/cms/bibliotheque/foodeatup-noshow-tuto-v1\n\n**Description (à quoi ça sert)**\n\nUne réservation évolue rarement telle quelle jusqu'au service : le client change d'heure ou de nombre de couverts, ne se présente pas, ou annule complètement. Plutôt que de naviguer entre plusieurs écrans, ce menu centralise toutes les actions sur la ligne de réservation elle-même : modifier les détails, marquer une absence (no-show) pour libérer la table aussitôt, ou supprimer définitivement une réservation obsolète, avec une confirmation avant toute suppression.\n\n**Comment ça marche**\n\n1. Depuis Réservations, ouvrez le menu à trois points sur la ligne concernée\n2. Cliquez sur Modifier pour changer l'horaire, le nombre de couverts ou la table\n3. Le client ne s'est pas présenté ? Cliquez sur No-show pour libérer la table immédiatement\n4. Une réservation à supprimer définitivement ? Le même menu propose aussi cette option, avec confirmation avant suppression\n\n**Astuce du chef** : Marquez le no-show dès que vous constatez l'absence, pas en fin de service — la table se libère immédiatement pour être réattribuée à un autre client, et vos statistiques de fréquentation restent fiables. Le menu d'actions s'adapte au statut de la réservation : une fois en no-show, seules Modifier et Supprimer restent proposées, plus besoin de chercher parmi des actions qui ne s'appliquent plus.\n\n---",
              "correspondance": "numéro",
              "confiance": 1.0
            },
            "tutorielModuleUrl": "https://tutoriel.foodeatup.com/module/reservation-salle",
            "higgsfield": {
              "videoSourceUrl": null,
              "duree": "10 s",
              "format": "vertical 9:16",
              "source": null
            },
            "masterRapidoUrl": null
          },
          {
            "id": "EP105",
            "numero": 105,
            "saison": 4,
            "slug": "ep105-le-duel-de-la-derniere-table",
            "titre": "Le duel de la dernière table",
            "module": "Mon Site",
            "chapitre": "6 - Réservations et horaires",
            "accroche": "Dernière table du samedi.",
            "punchline": "Le plus rapide gagne. Rends-la réservable en ligne.",
            "resume": "Tes créneaux sont réservables en ligne, en direct, avec tes vraies disponibilités. Le premier qui réserve a la table.",
            "statut": "bloque",
            "dureeSecondes": null,
            "videoUrl": null,
            "reseaux": {
              "facebook": {
                "statut": "a_venir",
                "date": null,
                "heure": "12:00",
                "compte": "FoodEatUp",
                "format": "Vidéo native 9:16",
                "lienCta": "https://site.foodeatup.com/"
              },
              "instagram": {
                "statut": "a_venir",
                "date": null,
                "heure": "18:30",
                "compte": "foodeatup.cocuisinage",
                "format": "Reel 9:16",
                "lienCta": null
              },
              "tiktok": {
                "statut": "a_venir",
                "date": null,
                "heure": "19:00",
                "compte": "foodeatup",
                "format": "Vidéo 9:16",
                "lienCta": null
              },
              "linkedin": {
                "statut": "a_venir",
                "date": null,
                "heure": "08:00",
                "compte": "FoodEatUp",
                "format": "Vidéo native 9:16",
                "lienCta": "https://site.foodeatup.com/"
              },
              "youtube": {
                "statut": "a_venir",
                "date": null,
                "heure": "10:00",
                "compte": "@FoodEatUp",
                "format": "Short 9:16",
                "lienCta": "https://site.foodeatup.com/"
              }
            },
            "blocage": "Le chapitre correspondant n'a pas encore de vidéo dans le Drive interne.",
            "posterUrl": null,
            "datePrevue": null,
            "troisMots": "RÉSERVATIONS ET HORAIRES",
            "tutoriel": {
              "titre": "Configurer ses horaires et réservations",
              "slug": "configurer-horaires-et-reservations-site",
              "url": "https://tutoriel.foodeatup.com/tutoriel/configurer-horaires-et-reservations-site",
              "module": "Site Web & Vitrine",
              "etape": "Horaires, réservations & domaine\n- **Statut** : Bientôt disponible (tournage en cours)\n\n**Description (à quoi ça sert)**\n\nConfigurer ses horaires et réservations — tutoriel en préparation dans le module Site Web & Vitrine. Il arrive très bientôt dans ce fil conducteur.\n\n**Comment ça marche**\n\n1. Cette vidéo est en cours de tournage dans les cuisines FoodEatUp.\n2. Sa fiche est déjà en place : elle se remplira dès la mise en ligne.\n\n---",
              "correspondance": "numéro",
              "confiance": 1.0
            },
            "tutorielModuleUrl": "https://tutoriel.foodeatup.com/module/site-web-vitrine",
            "higgsfield": {
              "videoSourceUrl": null,
              "duree": "10 s",
              "format": "vertical 9:16",
              "source": null
            },
            "masterRapidoUrl": null
          },
          {
            "id": "EP106",
            "numero": 106,
            "saison": 4,
            "slug": "ep106-l-addition-en-quatorze-parts",
            "titre": "L'addition en quatorze parts",
            "module": "Caisse POS",
            "chapitre": "5 - Séparer une addition",
            "accroche": "On peut payer chacun ?",
            "punchline": "Oui. En trois secondes, pas en trente minutes.",
            "resume": "Quatorze parts, quatorze cartes : tu découpes l'addition depuis l'écran, chacun paie ce qu'il doit, le reste dû s'affiche en direct.",
            "statut": "bloque",
            "dureeSecondes": null,
            "videoUrl": null,
            "reseaux": {
              "facebook": {
                "statut": "a_venir",
                "date": null,
                "heure": "12:00",
                "compte": "FoodEatUp",
                "format": "Vidéo native 9:16",
                "lienCta": "https://site.foodeatup.com/"
              },
              "instagram": {
                "statut": "a_venir",
                "date": null,
                "heure": "18:30",
                "compte": "foodeatup.cocuisinage",
                "format": "Reel 9:16",
                "lienCta": null
              },
              "tiktok": {
                "statut": "a_venir",
                "date": null,
                "heure": "19:00",
                "compte": "foodeatup",
                "format": "Vidéo 9:16",
                "lienCta": null
              },
              "linkedin": {
                "statut": "a_venir",
                "date": null,
                "heure": "08:00",
                "compte": "FoodEatUp",
                "format": "Vidéo native 9:16",
                "lienCta": "https://site.foodeatup.com/"
              },
              "youtube": {
                "statut": "a_venir",
                "date": null,
                "heure": "10:00",
                "compte": "@FoodEatUp",
                "format": "Short 9:16",
                "lienCta": "https://site.foodeatup.com/"
              }
            },
            "blocage": "Le chapitre correspondant n'a pas encore de vidéo dans le Drive interne.",
            "posterUrl": null,
            "datePrevue": null,
            "troisMots": "SÉPARER UNE ADDITION",
            "tutoriel": null,
            "tutorielModuleUrl": null,
            "tutorielManquant": "Le module Caisse POS n'existe pas encore dans l'Academy.",
            "higgsfield": {
              "videoSourceUrl": null,
              "duree": "10 s",
              "format": "vertical 9:16",
              "source": null
            },
            "masterRapidoUrl": null
          },
          {
            "id": "EP107",
            "numero": 107,
            "saison": 4,
            "slug": "ep107-le-magicien-de-l-addition",
            "titre": "Le magicien de l'addition",
            "module": "Caisse POS",
            "chapitre": "3 - Encaisser une commande",
            "accroche": "Tout le monde a un tour.",
            "punchline": "Ta caisse, elle, ne perd jamais une addition.",
            "resume": "L'addition est rattachée à la table dès la commande. Elle ne se perd pas, elle ne s'oublie pas, elle ne disparaît pas.",
            "statut": "bloque",
            "dureeSecondes": null,
            "videoUrl": null,
            "reseaux": {
              "facebook": {
                "statut": "a_venir",
                "date": null,
                "heure": "12:00",
                "compte": "FoodEatUp",
                "format": "Vidéo native 9:16",
                "lienCta": "https://site.foodeatup.com/"
              },
              "instagram": {
                "statut": "a_venir",
                "date": null,
                "heure": "18:30",
                "compte": "foodeatup.cocuisinage",
                "format": "Reel 9:16",
                "lienCta": null
              },
              "tiktok": {
                "statut": "a_venir",
                "date": null,
                "heure": "19:00",
                "compte": "foodeatup",
                "format": "Vidéo 9:16",
                "lienCta": null
              },
              "linkedin": {
                "statut": "a_venir",
                "date": null,
                "heure": "08:00",
                "compte": "FoodEatUp",
                "format": "Vidéo native 9:16",
                "lienCta": "https://site.foodeatup.com/"
              },
              "youtube": {
                "statut": "a_venir",
                "date": null,
                "heure": "10:00",
                "compte": "@FoodEatUp",
                "format": "Short 9:16",
                "lienCta": "https://site.foodeatup.com/"
              }
            },
            "blocage": "Le chapitre correspondant n'a pas encore de vidéo dans le Drive interne.",
            "posterUrl": null,
            "datePrevue": null,
            "troisMots": "ENCAISSER UNE COMMANDE",
            "tutoriel": null,
            "tutorielModuleUrl": null,
            "tutorielManquant": "Le module Caisse POS n'existe pas encore dans l'Academy.",
            "higgsfield": {
              "videoSourceUrl": null,
              "duree": "10 s",
              "format": "vertical 9:16",
              "source": null
            },
            "masterRapidoUrl": null
          },
          {
            "id": "EP108",
            "numero": 108,
            "saison": 4,
            "slug": "ep108-le-poulpe-du-pass",
            "titre": "Le poulpe du pass",
            "module": "KDS",
            "chapitre": "2 - Vue KDS par poste",
            "accroche": "Il te faudrait six bras.",
            "punchline": "Ou un seul outil qui fait le reste.",
            "resume": "Chaque poste voit ce qui le concerne, et seulement ça. Tu n'as pas besoin de six bras, tu as besoin de six écrans qui parlent entre eux.",
            "statut": "a_produire",
            "dureeSecondes": null,
            "videoUrl": null,
            "reseaux": {
              "facebook": {
                "statut": "a_venir",
                "date": "2026-11-02",
                "heure": "12:00",
                "compte": "FoodEatUp",
                "format": "Vidéo native 9:16",
                "lienCta": "https://site.foodeatup.com/"
              },
              "instagram": {
                "statut": "a_venir",
                "date": "2026-11-02",
                "heure": "18:30",
                "compte": "foodeatup.cocuisinage",
                "format": "Reel 9:16",
                "lienCta": null
              },
              "tiktok": {
                "statut": "a_venir",
                "date": "2026-11-02",
                "heure": "19:00",
                "compte": "foodeatup",
                "format": "Vidéo 9:16",
                "lienCta": null
              },
              "linkedin": {
                "statut": "a_venir",
                "date": "2026-11-02",
                "heure": "08:00",
                "compte": "FoodEatUp",
                "format": "Vidéo native 9:16",
                "lienCta": "https://site.foodeatup.com/"
              },
              "youtube": {
                "statut": "a_venir",
                "date": "2026-11-02",
                "heure": "10:00",
                "compte": "@FoodEatUp",
                "format": "Short 9:16",
                "lienCta": "https://site.foodeatup.com/"
              }
            },
            "posterUrl": null,
            "datePrevue": "2026-11-02",
            "troisMots": "VUE KDS PAR",
            "tutoriel": {
              "titre": "Afficher le KDS par poste",
              "slug": "afficher-le-kds-par-poste",
              "url": "https://tutoriel.foodeatup.com/tutoriel/afficher-le-kds-par-poste",
              "module": "Écran Cuisine (KDS)",
              "etape": "Affichage KDS\n- **Statut** : En ligne (0 min 49 s)\n- **Vidéo** : https://rapido-software.s3.eu-west-3.amazonaws.com/rapidosoftware/cms/bibliotheque/foodeatup-kds-par-poste-tuto\n\n**Description (à quoi ça sert)**\n\nDonner à chaque poste de cuisine un écran filtré sur ses seules commandes, synchronisé en temps réel avec les autres postes — le Pass sait exactement quand tous les plats d'une commande sont prêts, sans que personne n'ait à se déplacer ou à s'appeler d'un bout à l'autre de la cuisine.\n\n**Comment ça marche**\n\n1. Depuis Cuisine (KDS), chaque poste — chaud, pass, froid — a son propre écran, avec ses propres règles de routage (quelles catégories de plats lui arrivent).\n2. Cliquez sur Ouvrir l'écran pour afficher l'écran dédié de ce poste, en plein écran (tablette ou TV).\n3. Les commandes confirmées arrivent en temps réel sur l'écran du poste concerné dès leur validation, sans rafraîchissement manuel.\n4. Une fois un plat prêt, l'équipe clique sur Bump [poste] : il est marqué prêt et disparaît de l'écran de ce poste.\n5. Le poste Pass centralise ce qui doit sortir : chaque ticket y affiche l'état de ses plats venant des autres postes (ex. « CHAUD … » = en attente d'être bumpé).\n6. Dès que tous les plats d'un ticket sont bumpés sur leurs postes respectifs, le bouton Fire Service s'active sur le Pass : la commande est prête à partir en salle.\n\n**Astuce du chef** : Le bouton Bump ne veut pas dire « servi » mais « prêt et transmis » : sur un poste de préparation (chaud, froid...), il fait remonter le plat au Pass ; sur le Pass, c'est Fire Service qui déclenche l'envoi réel en salle. Tant qu'un seul poste n'a pas bumpé son plat, le ticket reste bloqué au Pass — c'est justement ce qui empêche une commande de partir incomplète, même en plein coup de feu.\n\n---",
              "correspondance": "numéro",
              "confiance": 1.0
            },
            "tutorielModuleUrl": "https://tutoriel.foodeatup.com/module/kds-cuisine",
            "higgsfield": {
              "videoSourceUrl": null,
              "duree": "10 s",
              "format": "vertical 9:16",
              "source": null
            },
            "masterRapidoUrl": null
          },
          {
            "id": "EP109",
            "numero": 109,
            "saison": 4,
            "slug": "ep109-le-kombucha-qui-explose",
            "titre": "Le kombucha qui explose",
            "module": "HACCP",
            "chapitre": "traçabilité",
            "accroche": "Ta cave à ferments.",
            "punchline": "Suivie et datée, elle ne t'explose pas à la figure.",
            "resume": "Chaque production est datée, tracée, rattachée à son lot. Ce qui fermente en cave n'est plus une surprise.",
            "statut": "a_produire",
            "dureeSecondes": null,
            "videoUrl": null,
            "reseaux": {
              "facebook": {
                "statut": "a_venir",
                "date": "2026-11-03",
                "heure": "12:00",
                "compte": "FoodEatUp",
                "format": "Vidéo native 9:16",
                "lienCta": "https://site.foodeatup.com/"
              },
              "instagram": {
                "statut": "a_venir",
                "date": "2026-11-03",
                "heure": "18:30",
                "compte": "foodeatup.cocuisinage",
                "format": "Reel 9:16",
                "lienCta": null
              },
              "tiktok": {
                "statut": "a_venir",
                "date": "2026-11-03",
                "heure": "19:00",
                "compte": "foodeatup",
                "format": "Vidéo 9:16",
                "lienCta": null
              },
              "linkedin": {
                "statut": "a_venir",
                "date": "2026-11-03",
                "heure": "08:00",
                "compte": "FoodEatUp",
                "format": "Vidéo native 9:16",
                "lienCta": "https://site.foodeatup.com/"
              },
              "youtube": {
                "statut": "a_venir",
                "date": "2026-11-03",
                "heure": "10:00",
                "compte": "@FoodEatUp",
                "format": "Short 9:16",
                "lienCta": "https://site.foodeatup.com/"
              }
            },
            "posterUrl": null,
            "datePrevue": "2026-11-03",
            "troisMots": "TRAÇABILITÉ",
            "tutoriel": {
              "titre": "Créer une traçabilité complète",
              "slug": "creer-une-tracabilite-complete",
              "url": "https://tutoriel.foodeatup.com/tutoriel/creer-une-tracabilite-complete",
              "module": "Hygiène & HACCP",
              "etape": "Traçabilité\n- **Statut** : En ligne (0 min 52 s)\n- **Vidéo** : https://rapido-software.s3.eu-west-3.amazonaws.com/rapidosoftware/cms/bibliotheque/foodeatup-tracabilite-tuto-v1\n\n**Description (à quoi ça sert)**\n\nUn suivi de traçabilité complet et structuré, produit par produit — sélection du produit, numéro de lot, DLC photographiée et remarques — pour répondre aux exigences HACCP sans ressaisie ni papier volant, à la différence de la traçabilité simplifiée réservée aux plats sans référence précise.\n\n**Comment ça marche**\n\n1. Ouvrez le module \"Traçabilité\" depuis le menu principal de FoodEatUp\n2. Cliquez sur la carte \"Traçabilité complète\" (icône document), à droite de \"Traçabilité simplifiée\"\n3. Cliquez sur \"Ajouter des produits à la traçabilité\" et sélectionnez vos produits dans la liste\n4. Cliquez sur le statut \"non complété\" d'un produit pour ouvrir sa fiche, puis prenez en photo la DLC directement depuis l'application\n5. Renseignez la quantité, la DLC, le numéro de lot et une remarque, puis validez : le statut passe à Complété\n6. Cliquez sur \"Enregistrer\" (ou \"Enregistrer et imprimer\"), confirmez la date et l'heure : la traçabilité est ajoutée à votre historique\n\n**Astuce du chef** : Prenez la photo de la DLC au moment où vous ouvrez le produit, pas après : une fois l'emballage jeté, le numéro de lot est perdu. Et si le statut reste sur « non complété », ce n'est pas une erreur — c'est un rappel actif pour finir la fiche avant le prochain contrôle.\n\n---",
              "correspondance": "texte",
              "confiance": 0.54
            },
            "tutorielModuleUrl": "https://tutoriel.foodeatup.com/module/haccp",
            "higgsfield": {
              "videoSourceUrl": null,
              "duree": "10 s",
              "format": "vertical 9:16",
              "source": null
            },
            "masterRapidoUrl": null
          },
          {
            "id": "EP110",
            "numero": 110,
            "saison": 4,
            "slug": "ep110-le-menu-100-matcha",
            "titre": "Le menu 100 % matcha",
            "module": "StockVision",
            "chapitre": "18 - Statistiques par module",
            "accroche": "Tu suis toutes les tendances.",
            "punchline": "Regarde surtout lesquelles se vendent.",
            "resume": "La tendance, tu la testes. Tu regardes ce que ce plat rapporte vraiment, et tu décides de le garder ou pas sur des chiffres.",
            "statut": "a_produire",
            "dureeSecondes": null,
            "videoUrl": null,
            "reseaux": {
              "facebook": {
                "statut": "a_venir",
                "date": "2026-11-04",
                "heure": "12:00",
                "compte": "FoodEatUp",
                "format": "Vidéo native 9:16",
                "lienCta": "https://site.foodeatup.com/"
              },
              "instagram": {
                "statut": "a_venir",
                "date": "2026-11-04",
                "heure": "18:30",
                "compte": "foodeatup.cocuisinage",
                "format": "Reel 9:16",
                "lienCta": null
              },
              "tiktok": {
                "statut": "a_venir",
                "date": "2026-11-04",
                "heure": "19:00",
                "compte": "foodeatup",
                "format": "Vidéo 9:16",
                "lienCta": null
              },
              "linkedin": {
                "statut": "a_venir",
                "date": "2026-11-04",
                "heure": "08:00",
                "compte": "FoodEatUp",
                "format": "Vidéo native 9:16",
                "lienCta": "https://site.foodeatup.com/"
              },
              "youtube": {
                "statut": "a_venir",
                "date": "2026-11-04",
                "heure": "10:00",
                "compte": "@FoodEatUp",
                "format": "Short 9:16",
                "lienCta": "https://site.foodeatup.com/"
              }
            },
            "posterUrl": null,
            "datePrevue": "2026-11-04",
            "troisMots": "STATISTIQUES PAR MODULE",
            "tutoriel": {
              "titre": "Lire ses statistiques par module",
              "slug": "lire-ses-statistiques-par-module",
              "url": "https://tutoriel.foodeatup.com/tutoriel/lire-ses-statistiques-par-module",
              "module": "StockVision AI",
              "etape": "Statistiques & agent IA\n- **Statut** : En ligne (0 min 54 s)\n- **Vidéo** : https://rapido-software.s3.eu-west-3.amazonaws.com/rapidosoftware/cms/bibliotheque/foodeatup-statistiques-module-tuto-v1\n\n**Description (à quoi ça sert)**\n\nSuivre en temps réel la santé de votre restaurant module par module — chiffre d'affaires et marges, niveaux de stock, heures travaillées, conformité HACCP et production — sans jongler entre plusieurs outils.\n\n**Comment ça marche**\n\n1. Ouvrez le tableau de bord Analytix BI pour voir votre chiffre d'affaires, vos commandes, votre marge brute et votre score HACCP en un coup d'œil.\n2. Cliquez sur un module (Finances, Stocks, RH & Pointage, HACCP, Production) pour accéder à ses statistiques détaillées.\n3. Ajustez la période avec le sélecteur de dates puis cliquez sur Appliquer pour recalculer les chiffres du module.\n4. Posez une question en langage naturel à l'Assistant IA pour faire interpréter vos données BI.\n\n**Astuce du chef** : Chaque graphique du tableau de bord affiche aussi la période précédente en comparaison : un coup d'œil suffit pour repérer une marge qui glisse ou des anomalies HACCP qui remontent, avant que ça ne devienne un vrai problème en cuisine.\n\n---",
              "correspondance": "numéro",
              "confiance": 1.0
            },
            "tutorielModuleUrl": "https://tutoriel.foodeatup.com/module/stockvision-ai",
            "higgsfield": {
              "videoSourceUrl": null,
              "duree": "10 s",
              "format": "vertical 9:16",
              "source": null
            },
            "masterRapidoUrl": null
          },
          {
            "id": "EP111",
            "numero": 111,
            "saison": 4,
            "slug": "ep111-l-imprimante-3d-qui-deraille",
            "titre": "L'imprimante 3D qui déraille",
            "module": "StockVision",
            "chapitre": "12 - Valider une production",
            "accroche": "La cuisine du futur.",
            "punchline": "Le futur utile, c'est celui qui te fait gagner du temps.",
            "resume": "La production planifiée sort ses ingrédients du stock, sa quantité est validée, sa traçabilité écrite. Le gain de temps est là, pas dans le gadget.",
            "statut": "a_produire",
            "dureeSecondes": null,
            "videoUrl": null,
            "reseaux": {
              "facebook": {
                "statut": "a_venir",
                "date": "2026-11-05",
                "heure": "12:00",
                "compte": "FoodEatUp",
                "format": "Vidéo native 9:16",
                "lienCta": "https://site.foodeatup.com/"
              },
              "instagram": {
                "statut": "a_venir",
                "date": "2026-11-05",
                "heure": "18:30",
                "compte": "foodeatup.cocuisinage",
                "format": "Reel 9:16",
                "lienCta": null
              },
              "tiktok": {
                "statut": "a_venir",
                "date": "2026-11-05",
                "heure": "19:00",
                "compte": "foodeatup",
                "format": "Vidéo 9:16",
                "lienCta": null
              },
              "linkedin": {
                "statut": "a_venir",
                "date": "2026-11-05",
                "heure": "08:00",
                "compte": "FoodEatUp",
                "format": "Vidéo native 9:16",
                "lienCta": "https://site.foodeatup.com/"
              },
              "youtube": {
                "statut": "a_venir",
                "date": "2026-11-05",
                "heure": "10:00",
                "compte": "@FoodEatUp",
                "format": "Short 9:16",
                "lienCta": "https://site.foodeatup.com/"
              }
            },
            "posterUrl": null,
            "datePrevue": "2026-11-05",
            "troisMots": "VALIDER UNE PRODUCTION",
            "tutoriel": {
              "titre": "Valider une production (quantité, température, note)",
              "slug": "valider-une-production",
              "url": "https://tutoriel.foodeatup.com/tutoriel/valider-une-production",
              "module": "StockVision AI",
              "etape": "Production\n- **Statut** : En ligne (0 min 47 s)\n- **Vidéo** : https://rapido-software.s3.eu-west-3.amazonaws.com/rapidosoftware/cms/bibliotheque/foodeatup-valider-une-production\n\n**Description (à quoi ça sert)**\n\nClôturer une production en un seul geste : le stock est mis à jour automatiquement, l'écart entre quantité planifiée et quantité produite est tracé, et le contrôle température / qualité / hygiène part directement dans votre historique HACCP — sans double saisie ni registre papier.\n\n**Comment ça marche**\n\n1. Ouvrez \"Mes productions\" et repérez la production prête à produire\n2. Cliquez sur \"Valider la production\" sur sa carte\n3. Étape 1 — Quantités : saisissez la quantité réellement produite, l'efficacité se calcule automatiquement\n4. Étape 2 — Contrôle HACCP : renseignez la température de contrôle, la qualité, l'hygiène et vos notes de production\n5. Étape 3 — Confirmation : vérifiez le récapitulatif, puis cliquez sur \"Confirmer et valider\"\n6. Le stock est mis à jour automatiquement et la production bascule en \"Réalisé\" dans votre historique HACCP\n\n**Astuce du chef** : Saisissez toujours le réel, même quand il dépasse le prévu : 30 portions pour 19 planifiées, c'est 157,9 % d'efficacité, et c'est ce chiffre-là qui corrige votre stock. La température de contrôle est facultative dans le formulaire, mais c'est elle qui alimente votre historique HACCP : notez-la au moment de la validation (≥ 63 °C recommandé pour les plats chauds), pas le lendemain de mémoire.\n\n---",
              "correspondance": "numéro",
              "confiance": 1.0
            },
            "tutorielModuleUrl": "https://tutoriel.foodeatup.com/module/stockvision-ai",
            "higgsfield": {
              "videoSourceUrl": null,
              "duree": "10 s",
              "format": "vertical 9:16",
              "source": null
            },
            "masterRapidoUrl": null
          },
          {
            "id": "EP112",
            "numero": 112,
            "saison": 4,
            "slug": "ep112-le-casque-de-realite-augmentee",
            "titre": "Le casque de réalité augmentée",
            "module": "Mon Site",
            "chapitre": "2 - Choisir ton template",
            "accroche": "La carte du futur.",
            "punchline": "Ou juste une carte en ligne qui marche.",
            "resume": "Ta carte en ligne, propre, à jour, consultable par QR à table. Pas de casque, pas d'appli à installer.",
            "statut": "a_produire",
            "dureeSecondes": null,
            "videoUrl": null,
            "reseaux": {
              "facebook": {
                "statut": "a_venir",
                "date": "2026-11-06",
                "heure": "12:00",
                "compte": "FoodEatUp",
                "format": "Vidéo native 9:16",
                "lienCta": "https://site.foodeatup.com/"
              },
              "instagram": {
                "statut": "a_venir",
                "date": "2026-11-06",
                "heure": "18:30",
                "compte": "foodeatup.cocuisinage",
                "format": "Reel 9:16",
                "lienCta": null
              },
              "tiktok": {
                "statut": "a_venir",
                "date": "2026-11-06",
                "heure": "19:00",
                "compte": "foodeatup",
                "format": "Vidéo 9:16",
                "lienCta": null
              },
              "linkedin": {
                "statut": "a_venir",
                "date": "2026-11-06",
                "heure": "08:00",
                "compte": "FoodEatUp",
                "format": "Vidéo native 9:16",
                "lienCta": "https://site.foodeatup.com/"
              },
              "youtube": {
                "statut": "a_venir",
                "date": "2026-11-06",
                "heure": "10:00",
                "compte": "@FoodEatUp",
                "format": "Short 9:16",
                "lienCta": "https://site.foodeatup.com/"
              }
            },
            "posterUrl": null,
            "datePrevue": "2026-11-06",
            "troisMots": "CHOISIR TON TEMPLATE",
            "tutoriel": {
              "titre": "Mon Site",
              "slug": "choisir-son-template",
              "url": "https://tutoriel.foodeatup.com/tutoriel/choisir-son-template",
              "module": "Site Web & Vitrine",
              "etape": "Template & design\n- **Statut** : En ligne (0 min 42 s)\n- **Vidéo** : https://rapido-software.s3.eu-west-3.amazonaws.com/rapidosoftware/cms/bibliotheque/choisir-son-template-v1\n\n**Description (à quoi ça sert)**\n\nDonner à votre restaurant une vitrine professionnelle en quelques clics, sans compétence technique : chaque template est un design complet (couleurs, mise en page, ton) pensé pour un type d'établissement, avec un aperçu grandeur nature avant tout engagement et une sauvegarde automatique de votre site actuel.\n\n**Comment ça marche**\n\n1. Depuis Site Web > Templates, parcourez la bibliothèque de thèmes métiers prêts à l'emploi\n2. Filtrez par type d'établissement (Boulangerie, Cave & vins, Asiatique...) pour affiner votre choix\n3. Cliquez sur Aperçu pour visualiser le template en conditions réelles dans un nouvel onglet, sans rien publier\n4. Le template vous plaît ? Cliquez sur Utiliser puis confirmez : une version de votre site actuel est automatiquement sauvegardée\n5. Votre site est transformé instantanément, prêt à personnaliser\n\n**Astuce du chef** : Prévisualisez toujours avant d'appliquer — l'aperçu grandeur nature ne publie rien, c'est le moment de comparer plusieurs styles tranquillement. Et ne vous inquiétez pas de vous tromper : une version de votre site est sauvegardée automatiquement à chaque changement de template, vous pouvez toujours revenir en arrière.\n\n---",
              "correspondance": "numéro",
              "confiance": 1.0
            },
            "tutorielModuleUrl": "https://tutoriel.foodeatup.com/module/site-web-vitrine",
            "higgsfield": {
              "videoSourceUrl": null,
              "duree": "10 s",
              "format": "vertical 9:16",
              "source": null
            },
            "masterRapidoUrl": null
          },
          {
            "id": "EP113",
            "numero": 113,
            "saison": 4,
            "slug": "ep113-le-drone-qui-se-trompe-de-balcon",
            "titre": "Le drone qui se trompe de balcon",
            "module": "HubRise",
            "chapitre": "4 - Centraliser les commandes",
            "accroche": "Livraison réussie. Presque.",
            "punchline": "Un suivi de commande, et personne ne mange ta pizza.",
            "resume": "Le suivi de commande affiche l'état en direct, de la prise à la remise. Tu sais toujours où est la commande et chez qui.",
            "statut": "bloque",
            "dureeSecondes": null,
            "videoUrl": null,
            "reseaux": {
              "facebook": {
                "statut": "a_venir",
                "date": null,
                "heure": "12:00",
                "compte": "FoodEatUp",
                "format": "Vidéo native 9:16",
                "lienCta": "https://site.foodeatup.com/"
              },
              "instagram": {
                "statut": "a_venir",
                "date": null,
                "heure": "18:30",
                "compte": "foodeatup.cocuisinage",
                "format": "Reel 9:16",
                "lienCta": null
              },
              "tiktok": {
                "statut": "a_venir",
                "date": null,
                "heure": "19:00",
                "compte": "foodeatup",
                "format": "Vidéo 9:16",
                "lienCta": null
              },
              "linkedin": {
                "statut": "a_venir",
                "date": null,
                "heure": "08:00",
                "compte": "FoodEatUp",
                "format": "Vidéo native 9:16",
                "lienCta": "https://site.foodeatup.com/"
              },
              "youtube": {
                "statut": "a_venir",
                "date": null,
                "heure": "10:00",
                "compte": "@FoodEatUp",
                "format": "Short 9:16",
                "lienCta": "https://site.foodeatup.com/"
              }
            },
            "blocage": "Le chapitre correspondant n'a pas encore de vidéo dans le Drive interne.",
            "posterUrl": null,
            "datePrevue": null,
            "troisMots": "CENTRALISER LES COMMANDES",
            "tutoriel": {
              "titre": "flux livraison",
              "slug": "centraliser-les-commandes-livraison",
              "url": "https://tutoriel.foodeatup.com/tutoriel/centraliser-les-commandes-livraison",
              "module": "HubRise & Livraisons",
              "etape": "Flux de commandes\n- **Statut** : Bientôt disponible (tournage en cours)\n\n**Description (à quoi ça sert)**\n\nCentraliser les commandes — flux livraison — tutoriel en préparation dans le module HubRise & Livraisons. Il arrive très bientôt dans ce fil conducteur.\n\n**Comment ça marche**\n\n1. Cette vidéo est en cours de tournage dans les cuisines FoodEatUp.\n2. Sa fiche est déjà en place : elle se remplira dès la mise en ligne.\n\n---",
              "correspondance": "numéro",
              "confiance": 1.0
            },
            "tutorielModuleUrl": "https://tutoriel.foodeatup.com/module/hubrise-livraisons",
            "higgsfield": {
              "videoSourceUrl": null,
              "duree": "10 s",
              "format": "vertical 9:16",
              "source": null
            },
            "masterRapidoUrl": null
          },
          {
            "id": "EP114",
            "numero": 114,
            "saison": 4,
            "slug": "ep114-la-chore-pendant-que-ca-brule",
            "titre": "La choré pendant que ça brûle",
            "module": "Marketing",
            "chapitre": "5 - Lancer une campagne",
            "accroche": "Ton community manager, c'est ta brigade.",
            "punchline": "Poste. Mais garde un œil sur le service.",
            "resume": "Ce que ton équipe filme, tu peux l'exploiter : campagne, segment, envoi, résultats. Publier, oui — mesurer, encore mieux.",
            "statut": "a_produire",
            "dureeSecondes": null,
            "videoUrl": null,
            "reseaux": {
              "facebook": {
                "statut": "a_venir",
                "date": "2026-11-07",
                "heure": "12:00",
                "compte": "FoodEatUp",
                "format": "Vidéo native 9:16",
                "lienCta": "https://site.foodeatup.com/"
              },
              "instagram": {
                "statut": "a_venir",
                "date": "2026-11-07",
                "heure": "18:30",
                "compte": "foodeatup.cocuisinage",
                "format": "Reel 9:16",
                "lienCta": null
              },
              "tiktok": {
                "statut": "a_venir",
                "date": "2026-11-07",
                "heure": "19:00",
                "compte": "foodeatup",
                "format": "Vidéo 9:16",
                "lienCta": null
              },
              "linkedin": {
                "statut": "a_venir",
                "date": "2026-11-07",
                "heure": "08:00",
                "compte": "FoodEatUp",
                "format": "Vidéo native 9:16",
                "lienCta": "https://site.foodeatup.com/"
              },
              "youtube": {
                "statut": "a_venir",
                "date": "2026-11-07",
                "heure": "10:00",
                "compte": "@FoodEatUp",
                "format": "Short 9:16",
                "lienCta": "https://site.foodeatup.com/"
              }
            },
            "posterUrl": null,
            "datePrevue": "2026-11-07",
            "troisMots": "LANCER UNE CAMPAGNE",
            "tutoriel": {
              "titre": "Lancer une campagne marketing",
              "slug": "lancer-une-campagne-marketing",
              "url": "https://tutoriel.foodeatup.com/tutoriel/lancer-une-campagne-marketing",
              "module": "Marketing, Fidélité & Iris",
              "etape": "Pack marketing & campagnes\n- **Statut** : En ligne (0 min 50 s)\n- **Vidéo** : https://rapido-software.s3.eu-west-3.amazonaws.com/rapidosoftware/cms/bibliotheque/foodeatup-campagne-marketing-tuto-v1\n\n**Description (à quoi ça sert)**\n\nToucher le bon segment de clients avec le bon message, sans risquer un envoi non conforme (procédure STOP, fenêtre légale) — coût et portée connus avant même de lancer la campagne.\n\n**Comment ça marche**\n\n1. Depuis l'onglet Campagnes, cliquez sur \"Nouvelle campagne\".\n2. Choisissez votre cible parmi les segments RFM calculés chaque nuit (Tous les clients, Champions, Fidèles, Prometteurs, À risque...).\n3. Nommez la campagne, choisissez son canal (Email, SMS, WhatsApp ou Vocal) et rédigez le message.\n4. Ajoutez votre offre et votre code promo — le lien tracké est généré automatiquement.\n5. Envoyez maintenant ou planifiez, FoodEatUp respecte toujours la fenêtre légale d'envoi.\n6. Vérifiez la conformité (contactables après exclusions STOP, coût estimé), puis lancez.\n\n**Astuce du chef** : Pour une première campagne, ciblez plutôt vos segments \"Champions\" ou \"Fidèles\" que \"Tous les clients\" : moins de contacts, mais un bien meilleur taux de retour, et vous limitez le risque de désabonnements sur toute votre base.\n\n---",
              "correspondance": "numéro",
              "confiance": 1.0
            },
            "tutorielModuleUrl": "https://tutoriel.foodeatup.com/module/marketing-fidelite",
            "higgsfield": {
              "videoSourceUrl": null,
              "duree": "10 s",
              "format": "vertical 9:16",
              "source": null
            },
            "masterRapidoUrl": null
          },
          {
            "id": "EP115",
            "numero": 115,
            "saison": 4,
            "slug": "ep115-les-poules-du-potager-du-toit",
            "titre": "Les poules du potager du toit",
            "module": "StockVision",
            "chapitre": "16 - Mouvements de stock",
            "accroche": "Circuit court, très court.",
            "punchline": "Compte ce qui rentre. Et ce qui sort.",
            "resume": "Ce qui rentre, ce qui sort, ce qui se perd. Circuit court ou pas, la quantité doit être comptée.",
            "statut": "a_produire",
            "dureeSecondes": null,
            "videoUrl": null,
            "reseaux": {
              "facebook": {
                "statut": "a_venir",
                "date": "2026-11-08",
                "heure": "12:00",
                "compte": "FoodEatUp",
                "format": "Vidéo native 9:16",
                "lienCta": "https://site.foodeatup.com/"
              },
              "instagram": {
                "statut": "a_venir",
                "date": "2026-11-08",
                "heure": "18:30",
                "compte": "foodeatup.cocuisinage",
                "format": "Reel 9:16",
                "lienCta": null
              },
              "tiktok": {
                "statut": "a_venir",
                "date": "2026-11-08",
                "heure": "19:00",
                "compte": "foodeatup",
                "format": "Vidéo 9:16",
                "lienCta": null
              },
              "linkedin": {
                "statut": "a_venir",
                "date": "2026-11-08",
                "heure": "08:00",
                "compte": "FoodEatUp",
                "format": "Vidéo native 9:16",
                "lienCta": "https://site.foodeatup.com/"
              },
              "youtube": {
                "statut": "a_venir",
                "date": "2026-11-08",
                "heure": "10:00",
                "compte": "@FoodEatUp",
                "format": "Short 9:16",
                "lienCta": "https://site.foodeatup.com/"
              }
            },
            "posterUrl": null,
            "datePrevue": "2026-11-08",
            "troisMots": "MOUVEMENTS DE STOCK",
            "tutoriel": {
              "titre": "Lire ses mouvements de stock FoodEatUp",
              "slug": "lire-ses-mouvements-de-stock",
              "url": "https://tutoriel.foodeatup.com/tutoriel/lire-ses-mouvements-de-stock",
              "module": "StockVision AI",
              "etape": "Stock\n- **Statut** : En ligne (0 min 46 s)\n- **Vidéo** : https://rapido-software.s3.eu-west-3.amazonaws.com/rapidosoftware/cms/bibliotheque/foodeatup-mouvements-stock-tuto-v1\n\n**Description (à quoi ça sert)**\n\nDisposer d'un registre lisible de tout ce qui entre et sort de votre cuisine, et pouvoir remonter à la source de n'importe quel écart : qui a saisi quoi, quand, pour quel motif et chez quel fournisseur. C'est la pièce qui rend votre inventaire vérifiable au lieu d'être déclaratif.\n\n**Comment ça marche**\n\n1. Ouvrez \"Gestion des stocks\" puis \"Mouvements de Stock\" : chaque ligne indique le produit, le type (Entrée ou Sortie), la quantité, le motif, le fournisseur, la date et l'utilisateur\n2. Ouvrez le menu \"Action\" (les trois points) au bout de la ligne, puis cliquez sur \"Voir détails\"\n3. Lisez la fiche complète : Informations Générales (produit, type de mouvement, quantité, motif) et Informations Supplémentaires (fournisseur, date et heure exactes, utilisateur qui a fait la saisie)\n4. Pour corriger une erreur de saisie, cliquez sur \"Supprimer\" en haut à droite de la fiche\n5. Confirmez dans la fenêtre : la suppression affecte également le stock, pas seulement la ligne du registre\n6. Le mouvement disparaît du registre et le stock est recalculé en conséquence\n\n**Astuce du chef** : Supprimer un mouvement n'efface pas seulement une ligne d'historique : le stock est recalculé derrière. Si vous supprimez une entrée de 5000 pièces, ces 5000 pièces quittent aussi votre stock. Avant de supprimer, ouvrez toujours la fiche de détail et vérifiez la quantité et le motif — c'est le réflexe qui évite de transformer une erreur de saisie en écart d'inventaire.\n\n---",
              "correspondance": "numéro",
              "confiance": 1.0
            },
            "tutorielModuleUrl": "https://tutoriel.foodeatup.com/module/stockvision-ai",
            "higgsfield": {
              "videoSourceUrl": null,
              "duree": "10 s",
              "format": "vertical 9:16",
              "source": null
            },
            "masterRapidoUrl": null
          },
          {
            "id": "EP116",
            "numero": 116,
            "saison": 4,
            "slug": "ep116-le-stagiaire-et-le-mur-de-craie",
            "titre": "Le stagiaire et le mur de craie",
            "module": "KDS",
            "chapitre": "1 - Créer tes postes KDS",
            "accroche": "Ton système de commandes.",
            "punchline": "Il tient sur un mur. Il tiendrait sur un écran.",
            "resume": "Tes commandes tiennent sur un écran, pas sur un mur. Chaque poste voit les siennes, dans l'ordre, avec son temps.",
            "statut": "a_produire",
            "dureeSecondes": null,
            "videoUrl": null,
            "reseaux": {
              "facebook": {
                "statut": "a_venir",
                "date": "2026-11-09",
                "heure": "12:00",
                "compte": "FoodEatUp",
                "format": "Vidéo native 9:16",
                "lienCta": "https://site.foodeatup.com/"
              },
              "instagram": {
                "statut": "a_venir",
                "date": "2026-11-09",
                "heure": "18:30",
                "compte": "foodeatup.cocuisinage",
                "format": "Reel 9:16",
                "lienCta": null
              },
              "tiktok": {
                "statut": "a_venir",
                "date": "2026-11-09",
                "heure": "19:00",
                "compte": "foodeatup",
                "format": "Vidéo 9:16",
                "lienCta": null
              },
              "linkedin": {
                "statut": "a_venir",
                "date": "2026-11-09",
                "heure": "08:00",
                "compte": "FoodEatUp",
                "format": "Vidéo native 9:16",
                "lienCta": "https://site.foodeatup.com/"
              },
              "youtube": {
                "statut": "a_venir",
                "date": "2026-11-09",
                "heure": "10:00",
                "compte": "@FoodEatUp",
                "format": "Short 9:16",
                "lienCta": "https://site.foodeatup.com/"
              }
            },
            "posterUrl": null,
            "datePrevue": "2026-11-09",
            "troisMots": "CRÉER TES POSTES",
            "tutoriel": {
              "titre": "module KDS",
              "slug": "creer-un-poste-de-travail",
              "url": "https://tutoriel.foodeatup.com/tutoriel/creer-un-poste-de-travail",
              "module": "Écran Cuisine (KDS)",
              "etape": "Postes de travail\n- **Statut** : En ligne (0 min 35 s)\n- **Vidéo** : https://rapido-software.s3.eu-west-3.amazonaws.com/rapidosoftware/cms/bibliotheque/foodeatup-kds-poste-tuto-v1\n\n**Description (à quoi ça sert)**\n\nLe KDS (Kitchen Display System, ou écran d'affichage cuisine) remplace les tickets papier par un écran par poste — tablette ou télé — installé directement sur chaque zone de préparation. Dès qu'une commande est confirmée (comptoir, table, QR code ou livraison), elle s'affiche en temps réel sur le ou les postes concernés, sans impression ni allers-retours. Personnalisez un poste par zone réelle de votre cuisine — Entrée, Chaud, Grillade, Bar... — et FoodEatUp dispatche automatiquement chaque ligne de commande vers le bon poste selon la catégorie du plat.\n\n**Comment ça marche**\n\n1. Depuis le module KDS, ouvrez l'écran Cuisine (kds)\n2. Cliquez sur \"+ Nouveau poste\"\n3. Donnez-lui un nom qui correspond à sa zone de préparation en cuisine, comme Entrée, Chaud, Grillade ou Bar\n4. Choisissez son type : Préparation pour la production, ou Pass pour l'envoi des plats\n5. Choisissez une couleur pour le repérer d'un coup d'oeil\n6. Cliquez sur \"Créer le poste\" : il rejoint aussitôt la liste avec son propre lien d'écran\n7. Associez ensuite ses catégories de plats dans le routage du poste (Entrée, Chaud, Grillade, Bar...) pour que chaque commande confirmée s'affiche automatiquement au bon endroit\n\n**Astuce du chef** : Organisez vos postes selon vos zones de préparation réelles — par exemple Entrée, Chaud, Grillade et Bar — puis routez chaque catégorie de plat vers le bon poste : les entrées atterrissent chez le chef entrée, les grillades chez le grillardin, les boissons et desserts au bar, chacun ne voyant que ce qui le concerne, en temps réel dès la confirmation de la commande. Gardez toujours un poste marqué « Poste par défaut (tout le reste) » actif : il récupère automatiquement toutes les catégories non routées explicitement, pour ne jamais perdre une commande. Le poste de type Pass sert de dernière étape avant l'envoi en salle — idéal pour un contrôle qualité juste avant le service.\n\n---",
              "correspondance": "numéro",
              "confiance": 1.0
            },
            "tutorielModuleUrl": "https://tutoriel.foodeatup.com/module/kds-cuisine",
            "higgsfield": {
              "videoSourceUrl": null,
              "duree": "10 s",
              "format": "vertical 9:16",
              "source": null
            },
            "masterRapidoUrl": null
          },
          {
            "id": "EP117",
            "numero": 117,
            "saison": 4,
            "slug": "ep117-le-plat-etoile-en-dix-minutes",
            "titre": "Le plat étoilé en dix minutes",
            "module": "StockVision",
            "chapitre": "1 - Ma carte, fiche recette",
            "accroche": "Le défi à dix minutes.",
            "punchline": "Une fiche technique, et c'est dix minutes tous les jours.",
            "resume": "La fiche technique fixe les quantités, les étapes et le coût. Le plat sort en dix minutes, tous les jours, par n'importe qui de ta brigade.",
            "statut": "a_produire",
            "dureeSecondes": null,
            "videoUrl": null,
            "reseaux": {
              "facebook": {
                "statut": "a_venir",
                "date": "2026-11-10",
                "heure": "12:00",
                "compte": "FoodEatUp",
                "format": "Vidéo native 9:16",
                "lienCta": "https://site.foodeatup.com/"
              },
              "instagram": {
                "statut": "a_venir",
                "date": "2026-11-10",
                "heure": "18:30",
                "compte": "foodeatup.cocuisinage",
                "format": "Reel 9:16",
                "lienCta": null
              },
              "tiktok": {
                "statut": "a_venir",
                "date": "2026-11-10",
                "heure": "19:00",
                "compte": "foodeatup",
                "format": "Vidéo 9:16",
                "lienCta": null
              },
              "linkedin": {
                "statut": "a_venir",
                "date": "2026-11-10",
                "heure": "08:00",
                "compte": "FoodEatUp",
                "format": "Vidéo native 9:16",
                "lienCta": "https://site.foodeatup.com/"
              },
              "youtube": {
                "statut": "a_venir",
                "date": "2026-11-10",
                "heure": "10:00",
                "compte": "@FoodEatUp",
                "format": "Short 9:16",
                "lienCta": "https://site.foodeatup.com/"
              }
            },
            "posterUrl": null,
            "datePrevue": "2026-11-10",
            "troisMots": "MA CARTE",
            "tutoriel": {
              "titre": "Tenir ses dépenses avec StockVision AI",
              "slug": "tenir-ses-depenses",
              "url": "https://tutoriel.foodeatup.com/tutoriel/tenir-ses-depenses",
              "module": "StockVision AI",
              "etape": "Dépenses & factures\n- **Statut** : En ligne (0 min 45 s)\n- **Vidéo** : https://rapido-software.s3.eu-west-3.amazonaws.com/rapidosoftware/cms/bibliotheque/foodeatup-depenses-tuto-v1.mp4\n\n**Description (à quoi ça sert)**\n\nNe ressaisissez plus vos factures fournisseurs à la main : StockVision AI les lit et crée la dépense correspondante dans votre comptabilité FoodEatUp, prête à être suivie et réglée.\n\n**Comment ça marche**\n\n1. Depuis une livraison, cliquez sur + Ajouter une facture.\n2. Déposez la facture de votre fournisseur (PDF, JPG ou PNG, 10 Mo max).\n3. Laissez StockVision AI analyser le document : les produits et montants sont extraits automatiquement en quelques secondes.\n4. Vérifiez les produits détectés sur l'écran de validation de la facture.\n5. Cliquez sur Valider et enregistrer.\n6. Retrouvez la dépense créée automatiquement : détail des lignes, TVA et total TTC, directement dans votre comptabilité.\n\n**Astuce du chef** : StockVision AI lit vos factures fournisseurs et crée la dépense toute seule, plus besoin de ressaisir chaque ligne à la main. Le statut initial est En attente : passez-le en Payée une fois le règlement effectué, pour garder une comptabilité à jour en temps réel.\n\n---",
              "correspondance": "texte",
              "confiance": 0.4
            },
            "tutorielModuleUrl": "https://tutoriel.foodeatup.com/module/stockvision-ai",
            "higgsfield": {
              "videoSourceUrl": null,
              "duree": "10 s",
              "format": "vertical 9:16",
              "source": null
            },
            "masterRapidoUrl": null
          },
          {
            "id": "EP118",
            "numero": 118,
            "saison": 4,
            "slug": "ep118-la-file-du-brunch",
            "titre": "La file du brunch",
            "module": "Mon Site",
            "chapitre": "5 - Créer un site par IA",
            "accroche": "Le brunch du dimanche.",
            "punchline": "Ils feraient la queue chez toi aussi. Encore faut-il pouvoir réserver.",
            "resume": "Ton site de réservation et de commande est prêt en un clic, depuis ta carte. La file d'attente devient un carnet plein.",
            "statut": "a_produire",
            "dureeSecondes": null,
            "videoUrl": null,
            "reseaux": {
              "facebook": {
                "statut": "a_venir",
                "date": "2026-11-11",
                "heure": "12:00",
                "compte": "FoodEatUp",
                "format": "Vidéo native 9:16",
                "lienCta": "https://site.foodeatup.com/"
              },
              "instagram": {
                "statut": "a_venir",
                "date": "2026-11-11",
                "heure": "18:30",
                "compte": "foodeatup.cocuisinage",
                "format": "Reel 9:16",
                "lienCta": null
              },
              "tiktok": {
                "statut": "a_venir",
                "date": "2026-11-11",
                "heure": "19:00",
                "compte": "foodeatup",
                "format": "Vidéo 9:16",
                "lienCta": null
              },
              "linkedin": {
                "statut": "a_venir",
                "date": "2026-11-11",
                "heure": "08:00",
                "compte": "FoodEatUp",
                "format": "Vidéo native 9:16",
                "lienCta": "https://site.foodeatup.com/"
              },
              "youtube": {
                "statut": "a_venir",
                "date": "2026-11-11",
                "heure": "10:00",
                "compte": "@FoodEatUp",
                "format": "Short 9:16",
                "lienCta": "https://site.foodeatup.com/"
              }
            },
            "posterUrl": null,
            "datePrevue": "2026-11-11",
            "troisMots": "CRÉER SITE PAR",
            "tutoriel": {
              "titre": "Créer un site par IA FoodEatUp",
              "slug": "creer-un-site-par-ia",
              "url": "https://tutoriel.foodeatup.com/tutoriel/creer-un-site-par-ia",
              "module": "Site Web & Vitrine",
              "etape": "Template & design\n- **Statut** : En ligne (0 min 40 s)\n- **Vidéo** : https://rapido-software.s3.eu-west-3.amazonaws.com/rapidosoftware/cms/bibliotheque/creer-un-site-par-ia-v1\n\n**Description (à quoi ça sert)**\n\nObtenir un site vitrine complet et personnalisé sans écrire une ligne de texte ni toucher un seul réglage technique : l'IA construit pages, contenus et mise en page à partir d'une simple conversation sur votre restaurant.\n\n**Comment ça marche**\n\n1. Depuis Site Web, ouvrez Créer avec l'IA dans le menu de l'éditeur.\n2. Répondez aux questions de l'agent en langage naturel : ambiance, clientèle visée, plats signatures, ton souhaité...\n3. Poursuivez l'interview jusqu'à la douzième question pour un site fidèle à votre identité.\n4. L'IA génère automatiquement pages, textes et mise en page à partir de vos réponses, prêts à publier.\n\n**Astuce du chef** : Soyez précis dans vos réponses (plats signatures, ambiance, clientèle) : plus l'interview est détaillée, plus le site généré vous ressemble dès le premier essai.\n\n---",
              "correspondance": "numéro",
              "confiance": 1.0
            },
            "tutorielModuleUrl": "https://tutoriel.foodeatup.com/module/site-web-vitrine",
            "higgsfield": {
              "videoSourceUrl": null,
              "duree": "10 s",
              "format": "vertical 9:16",
              "source": null
            },
            "masterRapidoUrl": null
          },
          {
            "id": "EP119",
            "numero": 119,
            "saison": 4,
            "slug": "ep119-la-mascotte-poulet-et-le-vent",
            "titre": "La mascotte poulet et le vent",
            "module": "Marketing",
            "chapitre": "9 - Ciblage et consentement",
            "accroche": "Ta stratégie d'acquisition.",
            "punchline": "Cinq cents tracts, zéro donnée.",
            "resume": "Cinq cents tracts, zéro donnée. Ici, chaque client capté entre dans ton fichier, avec son consentement, et devient une campagne.",
            "statut": "a_produire",
            "dureeSecondes": null,
            "videoUrl": null,
            "reseaux": {
              "facebook": {
                "statut": "a_venir",
                "date": "2026-11-12",
                "heure": "12:00",
                "compte": "FoodEatUp",
                "format": "Vidéo native 9:16",
                "lienCta": "https://site.foodeatup.com/"
              },
              "instagram": {
                "statut": "a_venir",
                "date": "2026-11-12",
                "heure": "18:30",
                "compte": "foodeatup.cocuisinage",
                "format": "Reel 9:16",
                "lienCta": null
              },
              "tiktok": {
                "statut": "a_venir",
                "date": "2026-11-12",
                "heure": "19:00",
                "compte": "foodeatup",
                "format": "Vidéo 9:16",
                "lienCta": null
              },
              "linkedin": {
                "statut": "a_venir",
                "date": "2026-11-12",
                "heure": "08:00",
                "compte": "FoodEatUp",
                "format": "Vidéo native 9:16",
                "lienCta": "https://site.foodeatup.com/"
              },
              "youtube": {
                "statut": "a_venir",
                "date": "2026-11-12",
                "heure": "10:00",
                "compte": "@FoodEatUp",
                "format": "Short 9:16",
                "lienCta": "https://site.foodeatup.com/"
              }
            },
            "posterUrl": null,
            "datePrevue": "2026-11-12",
            "troisMots": "CIBLAGE ET CONSENTEMENT",
            "tutoriel": {
              "titre": "Ciblage et consentement clients",
              "slug": "ciblage-et-consentement-clients",
              "url": "https://tutoriel.foodeatup.com/tutoriel/ciblage-et-consentement-clients",
              "module": "Marketing, Fidélité & Iris",
              "etape": "WhatsApp, SMS & crédits\n- **Statut** : En ligne (1 min 01 s)\n- **Vidéo** : https://rapido-software.s3.eu-west-3.amazonaws.com/rapidosoftware/cms/bibliotheque/foodeatup-ciblage-consentement-tuto-v1\n\n**Description (à quoi ça sert)**\n\nCibler les bons clients au bon moment tout en restant conforme au RGPD : des segments calculés sans effort manuel, un plafond anti-spam par client, et un consentement respecté au clic près — chaque contact peut se retirer instantanément de tout ciblage, avec la procédure de désinscription incluse dans chaque message envoyé.\n\n**Comment ça marche**\n\n1. Ouvrez Campagnes & automatisations depuis Marketing, puis l'onglet Segments & consentements.\n2. Consultez vos segments dynamiques (VIP, réguliers, nouveaux, à risque, perdus, gros paniers), calculés automatiquement depuis l'historique de commandes — aucun tag manuel.\n3. Réglez le plafond mensuel de messages par client (2 à 6, recommandé 4) pour rester dans la fenêtre légale, 8h à 20h, hors dimanche.\n4. Dans le tableau Contacts & consentements, vérifiez les canaux autorisés par contact : email, SMS, WhatsApp, vocal.\n5. Cliquez sur STOP pour retirer un contact de tout ciblage à tout moment ; le bouton devient Réactiver s'il change d'avis.\n6. Suivez le journal des 20 derniers envois pour vérifier ce qui a réellement été envoyé, à qui, et quand.\n\n**Astuce du chef** : Concentrez vos campagnes sur les segments À risque et Perdus avant qu'ils ne partent chez la concurrence : un message ciblé avec un code promo suffit souvent à relancer une habitude. Gardez le plafond à 4 messages par mois par défaut — au-delà, le taux de désabonnement grimpe plus vite que le retour sur investissement. Un contact STOP reste STOP tant qu'il n'a pas redonné son consentement : ne jamais le réactiver soi-même pour contourner la règle, c'est le meilleur moyen de se faire signaler. Et pensez à enchaîner ciblage et campagne dans la même conversation Claude : demandez d'abord vos segments RFM, puis la création du brouillon de campagne sur le segment choisi.\n\n---",
              "correspondance": "numéro",
              "confiance": 1.0
            },
            "tutorielModuleUrl": "https://tutoriel.foodeatup.com/module/marketing-fidelite",
            "higgsfield": {
              "videoSourceUrl": null,
              "duree": "10 s",
              "format": "vertical 9:16",
              "source": null
            },
            "masterRapidoUrl": null
          },
          {
            "id": "EP120",
            "numero": 120,
            "saison": 4,
            "slug": "ep120-la-reunion-des-dix-logiciels",
            "titre": "La réunion des dix logiciels",
            "module": "PrediBot",
            "chapitre": "1 - Lire ses prévisions",
            "accroche": "Réunion de tes dix logiciels.",
            "punchline": "Ils ne se parlent toujours pas. FoodEatUp, si.",
            "resume": "Une base, un écran, une équipe. Ta caisse, ta cuisine, ton stock et ton marketing lisent les mêmes données. Ils finissent enfin par se parler.",
            "statut": "a_produire",
            "dureeSecondes": null,
            "videoUrl": null,
            "reseaux": {
              "facebook": {
                "statut": "a_venir",
                "date": "2026-11-13",
                "heure": "12:00",
                "compte": "FoodEatUp",
                "format": "Vidéo native 9:16",
                "lienCta": "https://site.foodeatup.com/"
              },
              "instagram": {
                "statut": "a_venir",
                "date": "2026-11-13",
                "heure": "18:30",
                "compte": "foodeatup.cocuisinage",
                "format": "Reel 9:16",
                "lienCta": null
              },
              "tiktok": {
                "statut": "a_venir",
                "date": "2026-11-13",
                "heure": "19:00",
                "compte": "foodeatup",
                "format": "Vidéo 9:16",
                "lienCta": null
              },
              "linkedin": {
                "statut": "a_venir",
                "date": "2026-11-13",
                "heure": "08:00",
                "compte": "FoodEatUp",
                "format": "Vidéo native 9:16",
                "lienCta": "https://site.foodeatup.com/"
              },
              "youtube": {
                "statut": "a_venir",
                "date": "2026-11-13",
                "heure": "10:00",
                "compte": "@FoodEatUp",
                "format": "Short 9:16",
                "lienCta": "https://site.foodeatup.com/"
              }
            },
            "posterUrl": null,
            "datePrevue": "2026-11-13",
            "troisMots": "LIRE SES PRÉVISIONS",
            "tutoriel": {
              "titre": "Lire ses prévisions PrediBot",
              "slug": "lire-ses-previsions-predibot",
              "url": "https://tutoriel.foodeatup.com/tutoriel/lire-ses-previsions-predibot",
              "module": "PrediBot (Agent IA Directeur)",
              "etape": "Prévisions\n- **Statut** : En ligne (0 min 42 s)\n- **Vidéo** : https://raw.githubusercontent.com/PrendsTaPart/Video/claude/foodeatup-video-tutorials-bivyyp/videos/foodeatup-predibot-previsions-tuto/out/foodeatup-predibot-previsions-tuto-v1.mp4\n\n**Description (à quoi ça sert)**\n\nAnticiper vos besoins en stock, en commandes fournisseurs et en production grâce aux prédictions de l'intelligence artificielle PrediBot, pour éviter les ruptures et ne produire que le nécessaire.\n\n**Comment ça marche**\n\n1. Ouvrez Analyse et prédictions depuis le tableau de bord PrediBot pour voir vos indicateurs clés : alertes actives, économies potentielles, précision de l'IA.\n2. Cliquez sur Prédictions de stock pour visualiser votre consommation face à vos niveaux de stock, avec la recommandation de l'IA.\n3. Consultez Prévisions de commandes : PrediBot vous suggère quoi commander, produit par produit, avant la rupture de stock.\n4. Ouvrez Production recommandée pour voir les plats à préparer et les quantités conseillées, selon l'historique de vos ventes.\n\n**Astuce du chef** : Le pourcentage de précision IA et le niveau de confiance du modèle indiquent la fiabilité de chaque prévision : plus votre historique de ventes est riche, plus PrediBot affine ses recommandations semaine après semaine.\n\n---",
              "correspondance": "numéro",
              "confiance": 1.0
            },
            "tutorielModuleUrl": "https://tutoriel.foodeatup.com/module/predibot",
            "higgsfield": {
              "videoSourceUrl": null,
              "duree": "10 s",
              "format": "vertical 9:16",
              "source": null
            },
            "masterRapidoUrl": null
          }
        ]
      },
      {
        "numero": 5,
        "titre": "Le restaurant qui anticipe",
        "pitch": "Prévisions, HACCP, pilotage : voir venir au lieu de subir.",
        "episodes": [
          {
            "id": "EP121",
            "numero": 121,
            "saison": 5,
            "slug": "ep121-le-modificateur-infini",
            "titre": "Le modificateur infini",
            "module": "Service",
            "chapitre": "3 - Envoi direct cuisine",
            "accroche": "Alors, sans oignon, mais…",
            "punchline": "Une commande complexe, ça se saisit. Pas ça se subit.",
            "resume": "Les modifications se saisissent sur la commande : sans oignon, cuisson, allergie. Elles partent en cuisine avec le plat, écrites noir sur blanc.",
            "statut": "a_produire",
            "dureeSecondes": null,
            "videoUrl": null,
            "reseaux": {
              "facebook": {
                "statut": "a_venir",
                "date": "2026-11-14",
                "heure": "12:00",
                "compte": "FoodEatUp",
                "format": "Vidéo native 9:16",
                "lienCta": "https://site.foodeatup.com/"
              },
              "instagram": {
                "statut": "a_venir",
                "date": "2026-11-14",
                "heure": "18:30",
                "compte": "foodeatup.cocuisinage",
                "format": "Reel 9:16",
                "lienCta": null
              },
              "tiktok": {
                "statut": "a_venir",
                "date": "2026-11-14",
                "heure": "19:00",
                "compte": "foodeatup",
                "format": "Vidéo 9:16",
                "lienCta": null
              },
              "linkedin": {
                "statut": "a_venir",
                "date": "2026-11-14",
                "heure": "08:00",
                "compte": "FoodEatUp",
                "format": "Vidéo native 9:16",
                "lienCta": "https://site.foodeatup.com/"
              },
              "youtube": {
                "statut": "a_venir",
                "date": "2026-11-14",
                "heure": "10:00",
                "compte": "@FoodEatUp",
                "format": "Short 9:16",
                "lienCta": "https://site.foodeatup.com/"
              }
            },
            "posterUrl": null,
            "datePrevue": "2026-11-14",
            "troisMots": "ENVOI DIRECT CUISINE",
            "tutoriel": {
              "titre": "Envoyer en cuisine en direct",
              "slug": "envoyer-en-cuisine-en-direct",
              "url": "https://tutoriel.foodeatup.com/tutoriel/envoyer-en-cuisine-en-direct",
              "module": "Service Multi-Canal",
              "etape": "Envoi en cuisine\n- **Statut** : En ligne (0 min 51 s)\n- **Vidéo** : https://rapido-software.s3.eu-west-3.amazonaws.com/rapidosoftware/cms/bibliotheque/foodeatup-envoi-cuisine-tuto-v1\n\n**Description (à quoi ça sert)**\n\nEnvoyez une commande en cuisine en un clic dès qu'elle est confirmée, sans ticket papier ni allers-retours entre la salle et le passe. L'équipe cuisine voit instantanément les plats, les allergènes et le temps écoulé sur son écran KDS, et la salle suit en direct jusqu'au statut Prête.\n\n**Comment ça marche**\n\n1. Ouvrez Commandes pour voir toutes les commandes du jour, tous canaux confondus, avec leur statut\n2. Cliquez sur Confirmer sur la commande à préparer : elle passe aussitôt en préparation et part sur l'écran cuisine (KDS)\n3. Sur le KDS, chaque ticket affiche les plats commandés, les allergènes et le temps écoulé depuis l'envoi\n4. Une fois les plats prêts, cliquez sur Prête pour la commande concernée\n5. Les filtres (À confirmer, Confirmées, En cuisine, Prêtes, Servies) se mettent à jour en temps réel pour toute l'équipe\n\n**Astuce du chef** : Dès qu'une commande est confirmée, elle atterrit sur le bon poste KDS sans que personne n'ait à décrocher un ticket papier ou crier en cuisine — gardez chaque écran filtré par poste (Chaud, Froid, Pass...) pour que chaque section ne voie que ses propres tickets : moins de bruit visuel en plein coup de feu, moins d'erreurs.\n\n---",
              "correspondance": "numéro",
              "confiance": 1.0
            },
            "tutorielModuleUrl": "https://tutoriel.foodeatup.com/module/service-commande",
            "higgsfield": {
              "videoSourceUrl": null,
              "duree": "10 s",
              "format": "vertical 9:16",
              "source": null
            },
            "masterRapidoUrl": null
          },
          {
            "id": "EP122",
            "numero": 122,
            "saison": 5,
            "slug": "ep122-comme-d-habitude",
            "titre": "« Comme d'habitude »",
            "module": "Marketing",
            "chapitre": "20 - Vue client fidélité",
            "accroche": "Il dit « comme d'habitude ».",
            "punchline": "Ton fichier client saurait, lui.",
            "resume": "La fiche client te dit qui il est, ce qu'il commande et quand il est venu la dernière fois. « Comme d'habitude » devient une information, pas un bluff.",
            "statut": "a_produire",
            "dureeSecondes": null,
            "videoUrl": null,
            "reseaux": {
              "facebook": {
                "statut": "a_venir",
                "date": "2026-11-15",
                "heure": "12:00",
                "compte": "FoodEatUp",
                "format": "Vidéo native 9:16",
                "lienCta": "https://site.foodeatup.com/"
              },
              "instagram": {
                "statut": "a_venir",
                "date": "2026-11-15",
                "heure": "18:30",
                "compte": "foodeatup.cocuisinage",
                "format": "Reel 9:16",
                "lienCta": null
              },
              "tiktok": {
                "statut": "a_venir",
                "date": "2026-11-15",
                "heure": "19:00",
                "compte": "foodeatup",
                "format": "Vidéo 9:16",
                "lienCta": null
              },
              "linkedin": {
                "statut": "a_venir",
                "date": "2026-11-15",
                "heure": "08:00",
                "compte": "FoodEatUp",
                "format": "Vidéo native 9:16",
                "lienCta": "https://site.foodeatup.com/"
              },
              "youtube": {
                "statut": "a_venir",
                "date": "2026-11-15",
                "heure": "10:00",
                "compte": "@FoodEatUp",
                "format": "Short 9:16",
                "lienCta": "https://site.foodeatup.com/"
              }
            },
            "posterUrl": null,
            "datePrevue": "2026-11-15",
            "troisMots": "VUE CLIENT FIDÉLITÉ",
            "tutoriel": {
              "titre": "côté client",
              "slug": "vue-publique-fidelite-cote-client",
              "url": "https://tutoriel.foodeatup.com/tutoriel/vue-publique-fidelite-cote-client",
              "module": "Marketing, Fidélité & Iris",
              "etape": "Fidélité & récompenses\n- **Statut** : En ligne (0 min 40 s)\n- **Vidéo** : https://rapido-software.s3.eu-west-3.amazonaws.com/rapidosoftware/cms/bibliotheque/vue-publique-fidelite-cote-client.mp4\n\n**Description (à quoi ça sert)**\n\nDonnez à vos clients une vue claire et autonome de leur fidélité — solde de points, récompenses, historique — sans jamais les faire sortir de leur espace personnel : moins de questions au comptoir, plus d'envie de revenir.\n\n**Comment ça marche**\n\n1. Ouvrez l'onglet Fidélité : vos clients y retrouvent leur solde de points et la progression vers leur prochaine récompense.\n2. Faites défiler pour afficher le catalogue Mes récompenses (coût en points de chaque récompense) et l'historique de leurs gains.\n3. L'onglet Mes commandes centralise aussi leur suivi de commandes, juste à côté.\n4. L'onglet Mes infos ouvre Mon compte : connexion passwordless par email, aucun mot de passe à retenir.\n\n**Astuce du chef** : Fixez une première récompense à un coût très bas (ici, un café à 2 points) pour offrir à vos clients une victoire rapide dès leur première commande — c'est ce qui les fait revenir une deuxième fois. Combinez-la avec un créneau à points doublés (comme le midi ici) pour lisser votre affluence aux heures creuses.\n\n---",
              "correspondance": "numéro",
              "confiance": 1.0
            },
            "tutorielModuleUrl": "https://tutoriel.foodeatup.com/module/marketing-fidelite",
            "higgsfield": {
              "videoSourceUrl": null,
              "duree": "10 s",
              "format": "vertical 9:16",
              "source": null
            },
            "masterRapidoUrl": null
          },
          {
            "id": "EP123",
            "numero": 123,
            "saison": 5,
            "slug": "ep123-le-vegetarien-du-dessert",
            "titre": "Le végétarien du dessert",
            "module": "StockVision",
            "chapitre": "1 - Ma carte, allergènes",
            "accroche": "Il annonce ça au dessert.",
            "punchline": "Les régimes et les allergènes, ça se note à la réservation.",
            "resume": "Les allergènes et les régimes sont portés par ta carte et par la réservation. L'info arrive en cuisine avant l'entrée, pas au dessert.",
            "statut": "a_produire",
            "dureeSecondes": null,
            "videoUrl": null,
            "reseaux": {
              "facebook": {
                "statut": "a_venir",
                "date": "2026-11-16",
                "heure": "12:00",
                "compte": "FoodEatUp",
                "format": "Vidéo native 9:16",
                "lienCta": "https://site.foodeatup.com/"
              },
              "instagram": {
                "statut": "a_venir",
                "date": "2026-11-16",
                "heure": "18:30",
                "compte": "foodeatup.cocuisinage",
                "format": "Reel 9:16",
                "lienCta": null
              },
              "tiktok": {
                "statut": "a_venir",
                "date": "2026-11-16",
                "heure": "19:00",
                "compte": "foodeatup",
                "format": "Vidéo 9:16",
                "lienCta": null
              },
              "linkedin": {
                "statut": "a_venir",
                "date": "2026-11-16",
                "heure": "08:00",
                "compte": "FoodEatUp",
                "format": "Vidéo native 9:16",
                "lienCta": "https://site.foodeatup.com/"
              },
              "youtube": {
                "statut": "a_venir",
                "date": "2026-11-16",
                "heure": "10:00",
                "compte": "@FoodEatUp",
                "format": "Short 9:16",
                "lienCta": "https://site.foodeatup.com/"
              }
            },
            "posterUrl": null,
            "datePrevue": "2026-11-16",
            "troisMots": "MA CARTE",
            "tutoriel": {
              "titre": "Tenir ses dépenses avec StockVision AI",
              "slug": "tenir-ses-depenses",
              "url": "https://tutoriel.foodeatup.com/tutoriel/tenir-ses-depenses",
              "module": "StockVision AI",
              "etape": "Dépenses & factures\n- **Statut** : En ligne (0 min 45 s)\n- **Vidéo** : https://rapido-software.s3.eu-west-3.amazonaws.com/rapidosoftware/cms/bibliotheque/foodeatup-depenses-tuto-v1.mp4\n\n**Description (à quoi ça sert)**\n\nNe ressaisissez plus vos factures fournisseurs à la main : StockVision AI les lit et crée la dépense correspondante dans votre comptabilité FoodEatUp, prête à être suivie et réglée.\n\n**Comment ça marche**\n\n1. Depuis une livraison, cliquez sur + Ajouter une facture.\n2. Déposez la facture de votre fournisseur (PDF, JPG ou PNG, 10 Mo max).\n3. Laissez StockVision AI analyser le document : les produits et montants sont extraits automatiquement en quelques secondes.\n4. Vérifiez les produits détectés sur l'écran de validation de la facture.\n5. Cliquez sur Valider et enregistrer.\n6. Retrouvez la dépense créée automatiquement : détail des lignes, TVA et total TTC, directement dans votre comptabilité.\n\n**Astuce du chef** : StockVision AI lit vos factures fournisseurs et crée la dépense toute seule, plus besoin de ressaisir chaque ligne à la main. Le statut initial est En attente : passez-le en Payée une fois le règlement effectué, pour garder une comptabilité à jour en temps réel.\n\n---",
              "correspondance": "texte",
              "confiance": 0.43
            },
            "tutorielModuleUrl": "https://tutoriel.foodeatup.com/module/stockvision-ai",
            "higgsfield": {
              "videoSourceUrl": null,
              "duree": "10 s",
              "format": "vertical 9:16",
              "source": null
            },
            "masterRapidoUrl": null
          },
          {
            "id": "EP124",
            "numero": 124,
            "saison": 5,
            "slug": "ep124-la-table-qui-ne-part-jamais",
            "titre": "La table qui ne part jamais",
            "module": "Caisse POS",
            "chapitre": "6 - Clôturer sa caisse",
            "accroche": "Il est minuit dix.",
            "punchline": "Le service a une fin. Ton logiciel devrait le savoir.",
            "resume": "Le service a une fin : tu clôtures, tu comptes, tu archives. L'écran te dit quand la journée est vraiment finie.",
            "statut": "bloque",
            "dureeSecondes": null,
            "videoUrl": null,
            "reseaux": {
              "facebook": {
                "statut": "a_venir",
                "date": null,
                "heure": "12:00",
                "compte": "FoodEatUp",
                "format": "Vidéo native 9:16",
                "lienCta": "https://site.foodeatup.com/"
              },
              "instagram": {
                "statut": "a_venir",
                "date": null,
                "heure": "18:30",
                "compte": "foodeatup.cocuisinage",
                "format": "Reel 9:16",
                "lienCta": null
              },
              "tiktok": {
                "statut": "a_venir",
                "date": null,
                "heure": "19:00",
                "compte": "foodeatup",
                "format": "Vidéo 9:16",
                "lienCta": null
              },
              "linkedin": {
                "statut": "a_venir",
                "date": null,
                "heure": "08:00",
                "compte": "FoodEatUp",
                "format": "Vidéo native 9:16",
                "lienCta": "https://site.foodeatup.com/"
              },
              "youtube": {
                "statut": "a_venir",
                "date": null,
                "heure": "10:00",
                "compte": "@FoodEatUp",
                "format": "Short 9:16",
                "lienCta": "https://site.foodeatup.com/"
              }
            },
            "blocage": "Le chapitre correspondant n'a pas encore de vidéo dans le Drive interne.",
            "posterUrl": null,
            "datePrevue": null,
            "troisMots": "CLÔTURER SA CAISSE",
            "tutoriel": null,
            "tutorielModuleUrl": null,
            "tutorielManquant": "Le module Caisse POS n'existe pas encore dans l'Academy.",
            "higgsfield": {
              "videoSourceUrl": null,
              "duree": "10 s",
              "format": "vertical 9:16",
              "source": null
            },
            "masterRapidoUrl": null
          },
          {
            "id": "EP125",
            "numero": 125,
            "saison": 5,
            "slug": "ep125-le-client-qui-refait-le-plan-de-salle",
            "titre": "Le client qui refait le plan de salle",
            "module": "Caroline",
            "chapitre": "3 - Dessiner son plan de salle",
            "accroche": "Je serais mieux là, non ?",
            "punchline": "Ton plan de salle, c'est toi qui le décides.",
            "resume": "Ton plan de salle est le tien : zones, tables, capacités, blocages. Tu places, tu bloques, tu libères en un geste.",
            "statut": "a_produire",
            "dureeSecondes": null,
            "videoUrl": null,
            "reseaux": {
              "facebook": {
                "statut": "a_venir",
                "date": "2026-11-17",
                "heure": "12:00",
                "compte": "FoodEatUp",
                "format": "Vidéo native 9:16",
                "lienCta": "https://site.foodeatup.com/"
              },
              "instagram": {
                "statut": "a_venir",
                "date": "2026-11-17",
                "heure": "18:30",
                "compte": "foodeatup.cocuisinage",
                "format": "Reel 9:16",
                "lienCta": null
              },
              "tiktok": {
                "statut": "a_venir",
                "date": "2026-11-17",
                "heure": "19:00",
                "compte": "foodeatup",
                "format": "Vidéo 9:16",
                "lienCta": null
              },
              "linkedin": {
                "statut": "a_venir",
                "date": "2026-11-17",
                "heure": "08:00",
                "compte": "FoodEatUp",
                "format": "Vidéo native 9:16",
                "lienCta": "https://site.foodeatup.com/"
              },
              "youtube": {
                "statut": "a_venir",
                "date": "2026-11-17",
                "heure": "10:00",
                "compte": "@FoodEatUp",
                "format": "Short 9:16",
                "lienCta": "https://site.foodeatup.com/"
              }
            },
            "posterUrl": null,
            "datePrevue": "2026-11-17",
            "troisMots": "DESSINER PLAN SALLE",
            "tutoriel": {
              "titre": "Ouvrir ses créneaux de réservation",
              "slug": "ouvrir-ses-creneaux-de-reservation",
              "url": "https://tutoriel.foodeatup.com/tutoriel/ouvrir-ses-creneaux-de-reservation",
              "module": "Agent IA Caroline",
              "etape": "Salle & créneaux\n- **Statut** : En ligne (0 min 52 s)\n- **Vidéo** : https://rapido-software.s3.eu-west-3.amazonaws.com/rapidosoftware/cms/bibliotheque/foodeatup-creneaux-reservation-tuto-v1.mp4\n\n**Description (à quoi ça sert)**\n\nOuvrir un jour ou ajuster une plage horaire pour que vos créneaux de réservation collent enfin à vos vrais horaires de service — sans quoi FoodEatUp bloque toute réservation hors des horaires Storefront, même un samedi soir complet.\n\n**Comment ça marche**\n\n1. Depuis Réservations, cliquez sur \"+ Nouvelle réservation\" et renseignez le client, la date, l'heure et le nombre de couverts.\n2. Si le créneau tombe hors de vos horaires Storefront, FoodEatUp refuse la réservation et affiche le motif (\"Restaurant fermé à cette heure\").\n3. Ouvrez Configuration boutique, puis Ma Vitrine, onglet Infos & Publication.\n4. Dans Horaires d'ouverture, cochez le jour concerné et ajustez sa plage horaire.\n5. Cliquez sur Enregistrer : la vitrine est mise à jour aussitôt (\"Vitrine enregistrée\").\n6. Retournez sur Réservations et recréez la réservation : le créneau est maintenant accepté — choisissez une table et validez.\n\n**Astuce du chef** : Avant de promettre un créneau à un client au téléphone, vérifiez vos horaires Storefront : un jour décoché ou une plage trop courte bloque la réservation même si une table est libre. Le message d'erreur vous le dit sur le moment, mais autant l'anticiper avant l'appel.\n\n---",
              "correspondance": "texte",
              "confiance": 0.4
            },
            "tutorielModuleUrl": "https://tutoriel.foodeatup.com/module/caroline-ia",
            "higgsfield": {
              "videoSourceUrl": null,
              "duree": "10 s",
              "format": "vertical 9:16",
              "source": null
            },
            "masterRapidoUrl": null
          },
          {
            "id": "EP126",
            "numero": 126,
            "saison": 5,
            "slug": "ep126-six-fourchettes-une-salade",
            "titre": "Six fourchettes, une salade",
            "module": "Caisse POS",
            "chapitre": "5 - Séparer une addition",
            "accroche": "On partage, c'est plus convivial.",
            "punchline": "Partage l'assiette. Pas l'addition, elle se divise toute seule.",
            "resume": "Tu partages l'addition par article ou par personne. Ce qui reste dû s'affiche en direct. Personne ne recompte à la main.",
            "statut": "bloque",
            "dureeSecondes": null,
            "videoUrl": null,
            "reseaux": {
              "facebook": {
                "statut": "a_venir",
                "date": null,
                "heure": "12:00",
                "compte": "FoodEatUp",
                "format": "Vidéo native 9:16",
                "lienCta": "https://site.foodeatup.com/"
              },
              "instagram": {
                "statut": "a_venir",
                "date": null,
                "heure": "18:30",
                "compte": "foodeatup.cocuisinage",
                "format": "Reel 9:16",
                "lienCta": null
              },
              "tiktok": {
                "statut": "a_venir",
                "date": null,
                "heure": "19:00",
                "compte": "foodeatup",
                "format": "Vidéo 9:16",
                "lienCta": null
              },
              "linkedin": {
                "statut": "a_venir",
                "date": null,
                "heure": "08:00",
                "compte": "FoodEatUp",
                "format": "Vidéo native 9:16",
                "lienCta": "https://site.foodeatup.com/"
              },
              "youtube": {
                "statut": "a_venir",
                "date": null,
                "heure": "10:00",
                "compte": "@FoodEatUp",
                "format": "Short 9:16",
                "lienCta": "https://site.foodeatup.com/"
              }
            },
            "blocage": "Le chapitre correspondant n'a pas encore de vidéo dans le Drive interne.",
            "posterUrl": null,
            "datePrevue": null,
            "troisMots": "SÉPARER UNE ADDITION",
            "tutoriel": null,
            "tutorielModuleUrl": null,
            "tutorielManquant": "Le module Caisse POS n'existe pas encore dans l'Academy.",
            "higgsfield": {
              "videoSourceUrl": null,
              "duree": "10 s",
              "format": "vertical 9:16",
              "source": null
            },
            "masterRapidoUrl": null
          },
          {
            "id": "EP127",
            "numero": 127,
            "saison": 5,
            "slug": "ep127-reveillon-23-h-58",
            "titre": "Réveillon, 23 h 58",
            "module": "Réservation",
            "chapitre": "1 - Réservations du jour",
            "accroche": "Bonne année à tout le monde.",
            "punchline": "Sauf à celui qui gère les deux cents couverts.",
            "resume": "Deux cents couverts un 31 décembre, ça se pilote : arrivées échelonnées, tables assignées, cuisine prévenue. La soirée reste une fête.",
            "statut": "a_produire",
            "dureeSecondes": null,
            "videoUrl": null,
            "reseaux": {
              "facebook": {
                "statut": "a_venir",
                "date": "2026-11-18",
                "heure": "12:00",
                "compte": "FoodEatUp",
                "format": "Vidéo native 9:16",
                "lienCta": "https://site.foodeatup.com/"
              },
              "instagram": {
                "statut": "a_venir",
                "date": "2026-11-18",
                "heure": "18:30",
                "compte": "foodeatup.cocuisinage",
                "format": "Reel 9:16",
                "lienCta": null
              },
              "tiktok": {
                "statut": "a_venir",
                "date": "2026-11-18",
                "heure": "19:00",
                "compte": "foodeatup",
                "format": "Vidéo 9:16",
                "lienCta": null
              },
              "linkedin": {
                "statut": "a_venir",
                "date": "2026-11-18",
                "heure": "08:00",
                "compte": "FoodEatUp",
                "format": "Vidéo native 9:16",
                "lienCta": "https://site.foodeatup.com/"
              },
              "youtube": {
                "statut": "a_venir",
                "date": "2026-11-18",
                "heure": "10:00",
                "compte": "@FoodEatUp",
                "format": "Short 9:16",
                "lienCta": "https://site.foodeatup.com/"
              }
            },
            "posterUrl": null,
            "datePrevue": "2026-11-18",
            "troisMots": "RÉSERVATIONS DU JOUR",
            "tutoriel": {
              "titre": "Retrouver ses réservations du jour",
              "slug": "retrouver-ses-reservations-du-jour",
              "url": "https://tutoriel.foodeatup.com/tutoriel/retrouver-ses-reservations-du-jour",
              "module": "Réservations & Plan de salle",
              "etape": "Réservations du jour\n- **Statut** : En ligne (0 min 51 s)\n- **Vidéo** : https://rapido-software.s3.eu-west-3.amazonaws.com/rapidosoftware/cms/bibliotheque/foodeatup-reservations-jour-tuto\n\n**Description (à quoi ça sert)**\n\nCentraliser sur un seul écran le plan de salle en temps réel, la file d'attente et les réservations du jour — pour savoir en un coup d'œil qui arrive, où l'installer, et ce qui reste disponible, sans jongler entre plusieurs outils.\n\n**Comment ça marche**\n\n1. Ouvrez Réservations : le plan de salle affiche chaque table en temps réel, avec son statut coloré (Libre, Réservée, Occupée, À nettoyer).\n2. La file d'attente liste les clients sans réservation, prêts à être placés dès qu'une table se libère.\n3. Plus bas, la liste Réservations du jour détaille chaque arrivée attendue : heure, client, nombre de couverts.\n4. Chaque ligne affiche aussi la table déjà assignée et son statut d'installation en direct (ex. Installée).\n5. D'un coup d'œil, vous savez qui arrive, où l'installer, et ce qui reste disponible pour le service.\n\n**Astuce du chef** : Gardez un œil sur la file d'attente autant que sur les réservations : un client sans réservation peut souvent être casé sur une table libérée entre deux arrivées prévues — le plan de salle en temps réel vous montre cette fenêtre avant qu'elle ne se referme.\n\n---",
              "correspondance": "numéro",
              "confiance": 1.0
            },
            "tutorielModuleUrl": "https://tutoriel.foodeatup.com/module/reservation-salle",
            "higgsfield": {
              "videoSourceUrl": null,
              "duree": "10 s",
              "format": "vertical 9:16",
              "source": null
            },
            "masterRapidoUrl": null
          },
          {
            "id": "EP128",
            "numero": 128,
            "saison": 5,
            "slug": "ep128-saint-valentin-surbookee",
            "titre": "Saint-Valentin surbookée",
            "module": "Réservation",
            "chapitre": "4 - Placer un client à table",
            "accroche": "Trente couverts en plus, ça rentre.",
            "punchline": "Ça rentre. La question, c'est si ça revient.",
            "resume": "Tu places tes clients selon la vraie capacité de ta salle. Serrer, ça se décide — ça ne se subit pas un soir de Saint-Valentin.",
            "statut": "a_produire",
            "dureeSecondes": null,
            "videoUrl": null,
            "reseaux": {
              "facebook": {
                "statut": "a_venir",
                "date": "2026-11-19",
                "heure": "12:00",
                "compte": "FoodEatUp",
                "format": "Vidéo native 9:16",
                "lienCta": "https://site.foodeatup.com/"
              },
              "instagram": {
                "statut": "a_venir",
                "date": "2026-11-19",
                "heure": "18:30",
                "compte": "foodeatup.cocuisinage",
                "format": "Reel 9:16",
                "lienCta": null
              },
              "tiktok": {
                "statut": "a_venir",
                "date": "2026-11-19",
                "heure": "19:00",
                "compte": "foodeatup",
                "format": "Vidéo 9:16",
                "lienCta": null
              },
              "linkedin": {
                "statut": "a_venir",
                "date": "2026-11-19",
                "heure": "08:00",
                "compte": "FoodEatUp",
                "format": "Vidéo native 9:16",
                "lienCta": "https://site.foodeatup.com/"
              },
              "youtube": {
                "statut": "a_venir",
                "date": "2026-11-19",
                "heure": "10:00",
                "compte": "@FoodEatUp",
                "format": "Short 9:16",
                "lienCta": "https://site.foodeatup.com/"
              }
            },
            "posterUrl": null,
            "datePrevue": "2026-11-19",
            "troisMots": "PLACER CLIENT TABLE",
            "tutoriel": {
              "titre": "Placer un client à table",
              "slug": "placer-un-client-a-table",
              "url": "https://tutoriel.foodeatup.com/tutoriel/placer-un-client-a-table",
              "module": "Réservations & Plan de salle",
              "etape": "Placement en salle\n- **Statut** : En ligne (0 min 38 s)\n- **Vidéo** : https://rapido-software.s3.eu-west-3.amazonaws.com/rapidosoftware/cms/bibliotheque/foodeatup-placer-un-client-a-table-tuto-v1\n\n**Description (à quoi ça sert)**\n\nInstaller un client réservé à sa table en un clic, avec sa commande sur place créée automatiquement — sans ressaisie côté service, et la possibilité de réassigner la table à tout moment en cas de changement de dernière minute.\n\n**Comment ça marche**\n\n1. Repérez la réservation de votre client dans la liste (statut En attente ou Confirmée).\n2. Ouvrez son menu d'actions (⋮) et cliquez sur Check-in.\n3. Le client est installé : sa commande sur place est créée automatiquement, sans ressaisie.\n4. Le statut de la réservation passe aussitôt à Installée.\n5. Besoin de changer sa table ? Rouvrez le menu d'actions et cliquez sur Modifier.\n6. Choisissez la zone (Salle principale, Terrasse) et la table précise, ou laissez FoodEatUp l'assigner automatiquement.\n\n**Astuce du chef** : Check-in fonctionne même sans table pré-assignée : FoodEatUp choisit automatiquement la meilleure table libre. Un client change de table à la dernière minute (allergie près d'une fenêtre, groupe qui s'agrandit) ? Pas besoin d'annuler-recréer la réservation — Modifier réassigne la table en gardant la commande déjà créée liée au bon client.\n\n---",
              "correspondance": "numéro",
              "confiance": 1.0
            },
            "tutorielModuleUrl": "https://tutoriel.foodeatup.com/module/reservation-salle",
            "higgsfield": {
              "videoSourceUrl": null,
              "duree": "10 s",
              "format": "vertical 9:16",
              "source": null
            },
            "masterRapidoUrl": null
          },
          {
            "id": "EP129",
            "numero": 129,
            "saison": 5,
            "slug": "ep129-premier-jour-de-terrasse-4-degres",
            "titre": "Premier jour de terrasse, 4 degrés",
            "module": "Caroline",
            "chapitre": "4 - Gérer ses tables",
            "accroche": "Premier rayon de soleil de l'année.",
            "punchline": "Ta terrasse ouvre. Ton service doit suivre.",
            "resume": "Tu ouvres ta terrasse dans le logiciel : tables ajoutées, capacité mise à jour, réservations ouvertes dessus. Le premier rayon de soleil est rentable.",
            "statut": "a_produire",
            "dureeSecondes": null,
            "videoUrl": null,
            "reseaux": {
              "facebook": {
                "statut": "a_venir",
                "date": "2026-11-20",
                "heure": "12:00",
                "compte": "FoodEatUp",
                "format": "Vidéo native 9:16",
                "lienCta": "https://site.foodeatup.com/"
              },
              "instagram": {
                "statut": "a_venir",
                "date": "2026-11-20",
                "heure": "18:30",
                "compte": "foodeatup.cocuisinage",
                "format": "Reel 9:16",
                "lienCta": null
              },
              "tiktok": {
                "statut": "a_venir",
                "date": "2026-11-20",
                "heure": "19:00",
                "compte": "foodeatup",
                "format": "Vidéo 9:16",
                "lienCta": null
              },
              "linkedin": {
                "statut": "a_venir",
                "date": "2026-11-20",
                "heure": "08:00",
                "compte": "FoodEatUp",
                "format": "Vidéo native 9:16",
                "lienCta": "https://site.foodeatup.com/"
              },
              "youtube": {
                "statut": "a_venir",
                "date": "2026-11-20",
                "heure": "10:00",
                "compte": "@FoodEatUp",
                "format": "Short 9:16",
                "lienCta": "https://site.foodeatup.com/"
              }
            },
            "posterUrl": null,
            "datePrevue": "2026-11-20",
            "troisMots": "GÉRER SES TABLES",
            "tutoriel": {
              "titre": "Gérer ses Tables (ajout & blocage)",
              "slug": "gerer-ses-tables-ajout-blocage",
              "url": "https://tutoriel.foodeatup.com/tutoriel/gerer-ses-tables-ajout-blocage",
              "module": "Agent IA Caroline",
              "etape": "Appels & réservations\n- **Statut** : En ligne (1 min 05 s)\n- **Vidéo** : https://rapido-software.s3.eu-west-3.amazonaws.com/rapidosoftware/cms/bibliotheque/foodeatup-gerer-tables-tuto-v1\n\n**Description (à quoi ça sert)**\n\nAdaptez votre plan de salle en temps réel : ajoutez une table pour un service chargé, ou bloquez-en une indisponible (table cassée, travaux, terrasse fermée) sans la supprimer — elle redevient disponible en un clic dès que la situation est réglée.\n\n**Comment ça marche**\n\n1. Ouvrez votre Plan de salle et passez en mode édition.\n2. Cliquez sur Ajouter une table : donnez-lui un nom, une forme et une capacité.\n3. Assignez-la à une zone (salle principale, terrasse…) puis enregistrez.\n4. Cliquez sur une table existante pour changer son statut : libre, réservée, occupée, nettoyage ou bloquée.\n5. Bloquez une table indisponible (panne, travaux) — elle ne sera plus proposée en réservation tant qu'elle reste bloquée, et redevient disponible en un clic.\n\n**Astuce du chef** : Plutôt que de supprimer une table indisponible, bloquez-la. Vous gardez son historique et ses réservations, et elle réapparaît instantanément dès que vous la repassez en Libre.\n\n---",
              "correspondance": "texte",
              "confiance": 0.7
            },
            "tutorielModuleUrl": "https://tutoriel.foodeatup.com/module/caroline-ia",
            "higgsfield": {
              "videoSourceUrl": null,
              "duree": "10 s",
              "format": "vertical 9:16",
              "source": null
            },
            "masterRapidoUrl": null
          },
          {
            "id": "EP130",
            "numero": 130,
            "saison": 5,
            "slug": "ep130-fete-de-la-musique",
            "titre": "Fête de la musique",
            "module": "Marketing",
            "chapitre": "7 - Ton agenda marketing",
            "accroche": "21 juin. Devant ta porte.",
            "punchline": "Autant que les gens sachent que tu es ouvert.",
            "resume": "Ton agenda marketing connaît les temps forts de ton quartier. Tu prépares l'événement avant qu'il soit devant ta porte.",
            "statut": "a_produire",
            "dureeSecondes": null,
            "videoUrl": null,
            "reseaux": {
              "facebook": {
                "statut": "a_venir",
                "date": "2026-11-21",
                "heure": "12:00",
                "compte": "FoodEatUp",
                "format": "Vidéo native 9:16",
                "lienCta": "https://site.foodeatup.com/"
              },
              "instagram": {
                "statut": "a_venir",
                "date": "2026-11-21",
                "heure": "18:30",
                "compte": "foodeatup.cocuisinage",
                "format": "Reel 9:16",
                "lienCta": null
              },
              "tiktok": {
                "statut": "a_venir",
                "date": "2026-11-21",
                "heure": "19:00",
                "compte": "foodeatup",
                "format": "Vidéo 9:16",
                "lienCta": null
              },
              "linkedin": {
                "statut": "a_venir",
                "date": "2026-11-21",
                "heure": "08:00",
                "compte": "FoodEatUp",
                "format": "Vidéo native 9:16",
                "lienCta": "https://site.foodeatup.com/"
              },
              "youtube": {
                "statut": "a_venir",
                "date": "2026-11-21",
                "heure": "10:00",
                "compte": "@FoodEatUp",
                "format": "Short 9:16",
                "lienCta": "https://site.foodeatup.com/"
              }
            },
            "posterUrl": null,
            "datePrevue": "2026-11-21",
            "troisMots": "TON AGENDA MARKETING",
            "tutoriel": {
              "titre": "Retrouver son agenda marketing",
              "slug": "retrouver-son-agenda-marketing",
              "url": "https://tutoriel.foodeatup.com/tutoriel/retrouver-son-agenda-marketing",
              "module": "Marketing, Fidélité & Iris",
              "etape": "Pack marketing & campagnes\n- **Statut** : En ligne (0 min 55 s)\n- **Vidéo** : https://rapido-software.s3.eu-west-3.amazonaws.com/rapidosoftware/cms/bibliotheque/foodeatup-agenda-marketing-tuto-v1\n\n**Description (à quoi ça sert)**\n\nLe marketing d'un restaurant, c'est remplir les tables aux moments qui en ont besoin : relancer un client qui ne revient plus, combler un jour creux, ou profiter d'un temps fort commercial. Un « marronnier », c'est une date fixe et récurrente du calendrier (Rentrée, Halloween, Saint-Valentin...) sur laquelle les clients attendent une offre chaque année. Votre agenda marketing centralise tout ça au même endroit : les jours creux détectés automatiquement dans votre activité et les marronniers à venir, avec une alerte 3 jours avant chaque échéance — et l'Agent IA propose déjà une campagne chiffrée, prête à valider.\n\n**Comment ça marche**\n\n1. Ouvrez Campagnes & automatisations puis l'onglet Agenda\n2. Repérez vos jours creux détectés automatiquement sur le calendrier, ainsi que les marronniers à venir (Rentrée, Halloween...)\n3. Cliquez sur Créer sur un jour creux, choisissez votre segment de clients (tous, champions, fidèles, à risque...)\n4. Rédigez votre message avec l'offre et le code promo\n5. Planifiez la date d'envoi, vérifiez la conformité (contacts joignables, coût estimé, exclusions STOP), puis confirmez\n\n**Astuce du chef** : Votre agenda marketing repère vos jours creux tout seul : pas besoin d'ouvrir un tableur pour savoir quand relancer. Laissez l'Agent IA proposer la campagne chiffrée, vous n'avez plus qu'à choisir votre segment et valider — le reste part automatiquement dans la fenêtre légale. Conseil : envoyez votre offre 3 jours avant un marronnier, pas le jour même — c'est le délai conseillé par FoodEatUp pour laisser le temps à vos clients de réserver.\n\n---",
              "correspondance": "numéro",
              "confiance": 1.0
            },
            "tutorielModuleUrl": "https://tutoriel.foodeatup.com/module/marketing-fidelite",
            "higgsfield": {
              "videoSourceUrl": null,
              "duree": "10 s",
              "format": "vertical 9:16",
              "source": null
            },
            "masterRapidoUrl": null
          },
          {
            "id": "EP131",
            "numero": 131,
            "saison": 5,
            "slug": "ep131-rentree-tout-le-monde-est-encore-en-vacances",
            "titre": "Rentrée : tout le monde est encore en vacances",
            "module": "Équipe & Planning",
            "chapitre": "planning de la semaine",
            "accroche": "1er septembre. Deux absents.",
            "punchline": "Un planning, ça se prépare avant la rentrée.",
            "resume": "Tu construis la semaine de rentrée en amont : shifts posés, congés validés, coût affiché. Le premier septembre, tu n'es pas seul en cuisine.",
            "statut": "a_produire",
            "dureeSecondes": null,
            "videoUrl": null,
            "reseaux": {
              "facebook": {
                "statut": "a_venir",
                "date": "2026-11-22",
                "heure": "12:00",
                "compte": "FoodEatUp",
                "format": "Vidéo native 9:16",
                "lienCta": "https://site.foodeatup.com/"
              },
              "instagram": {
                "statut": "a_venir",
                "date": "2026-11-22",
                "heure": "18:30",
                "compte": "foodeatup.cocuisinage",
                "format": "Reel 9:16",
                "lienCta": null
              },
              "tiktok": {
                "statut": "a_venir",
                "date": "2026-11-22",
                "heure": "19:00",
                "compte": "foodeatup",
                "format": "Vidéo 9:16",
                "lienCta": null
              },
              "linkedin": {
                "statut": "a_venir",
                "date": "2026-11-22",
                "heure": "08:00",
                "compte": "FoodEatUp",
                "format": "Vidéo native 9:16",
                "lienCta": "https://site.foodeatup.com/"
              },
              "youtube": {
                "statut": "a_venir",
                "date": "2026-11-22",
                "heure": "10:00",
                "compte": "@FoodEatUp",
                "format": "Short 9:16",
                "lienCta": "https://site.foodeatup.com/"
              }
            },
            "posterUrl": null,
            "datePrevue": "2026-11-22",
            "troisMots": "PLANNING SEMAINE",
            "tutoriel": {
              "titre": "Voir son planning côté employé FoodEatUp",
              "slug": "voir-son-planning-cote-employe",
              "url": "https://tutoriel.foodeatup.com/tutoriel/voir-son-planning-cote-employe",
              "module": "Équipe, Planning & RH",
              "etape": "Espace employé\n- **Statut** : En ligne (0 min 29 s)\n- **Vidéo** : https://rapido-software.s3.eu-west-3.amazonaws.com/rapidosoftware/cms/bibliotheque/voir-son-planning-cote-employe-v1\n\n**Description (à quoi ça sert)**\n\nDonner à chaque employé une vue claire et autonome de son propre planning — horaires, shifts et tâches de la semaine — pour qu'il puisse s'organiser, cocher ses tâches terminées et synchroniser son planning avec son agenda personnel, sans jamais avoir à demander au manager.\n\n**Comment ça marche**\n\n1. Depuis son espace, l'employé ouvre \"Mon planning\"\n2. Il retrouve ses heures planifiées, ses shifts et ses tâches de la semaine\n3. Jour par jour : repos, horaires et tâches à faire s'affichent clairement\n4. Il coche une tâche terminée directement depuis la liste\n5. Le compteur de tâches se met à jour instantanément\n6. Il peut cliquer sur \"Ajouter à mon agenda\" pour exporter son planning vers son agenda personnel\n\n**Astuce du chef** : Trois cas d'usage pratiques avec Claude : demandez-lui votre planning de la semaine en cours pour l'avoir en un coup d'œil sans ouvrir l'application ; demandez-lui d'anticiper la semaine prochaine pour organiser vos disponibilités à l'avance ; ou demandez-lui de comparer votre planning prévu à vos heures réellement pointées, pour repérer un écart avant qu'il ne devienne un problème de paie.\n\n---",
              "correspondance": "texte",
              "confiance": 0.54
            },
            "tutorielModuleUrl": "https://tutoriel.foodeatup.com/module/equipe-planning",
            "higgsfield": {
              "videoSourceUrl": null,
              "duree": "10 s",
              "format": "vertical 9:16",
              "source": null
            },
            "masterRapidoUrl": null
          },
          {
            "id": "EP132",
            "numero": 132,
            "saison": 5,
            "slug": "ep132-le-15-aout-seul-ouvert",
            "titre": "Le 15 août, seul ouvert",
            "module": "Mon Site",
            "chapitre": "6 - Réservations et horaires",
            "accroche": "Tout le quartier est fermé.",
            "punchline": "Sauf toi. Encore faut-il qu'on te trouve en ligne.",
            "resume": "Tes horaires d'ouverture sont à jour partout : site, réservation, Google. Quand tout le quartier ferme, on te trouve.",
            "statut": "bloque",
            "dureeSecondes": null,
            "videoUrl": null,
            "reseaux": {
              "facebook": {
                "statut": "a_venir",
                "date": null,
                "heure": "12:00",
                "compte": "FoodEatUp",
                "format": "Vidéo native 9:16",
                "lienCta": "https://site.foodeatup.com/"
              },
              "instagram": {
                "statut": "a_venir",
                "date": null,
                "heure": "18:30",
                "compte": "foodeatup.cocuisinage",
                "format": "Reel 9:16",
                "lienCta": null
              },
              "tiktok": {
                "statut": "a_venir",
                "date": null,
                "heure": "19:00",
                "compte": "foodeatup",
                "format": "Vidéo 9:16",
                "lienCta": null
              },
              "linkedin": {
                "statut": "a_venir",
                "date": null,
                "heure": "08:00",
                "compte": "FoodEatUp",
                "format": "Vidéo native 9:16",
                "lienCta": "https://site.foodeatup.com/"
              },
              "youtube": {
                "statut": "a_venir",
                "date": null,
                "heure": "10:00",
                "compte": "@FoodEatUp",
                "format": "Short 9:16",
                "lienCta": "https://site.foodeatup.com/"
              }
            },
            "blocage": "Le chapitre correspondant n'a pas encore de vidéo dans le Drive interne.",
            "posterUrl": null,
            "datePrevue": null,
            "troisMots": "RÉSERVATIONS ET HORAIRES",
            "tutoriel": {
              "titre": "Configurer ses horaires et réservations",
              "slug": "configurer-horaires-et-reservations-site",
              "url": "https://tutoriel.foodeatup.com/tutoriel/configurer-horaires-et-reservations-site",
              "module": "Site Web & Vitrine",
              "etape": "Horaires, réservations & domaine\n- **Statut** : Bientôt disponible (tournage en cours)\n\n**Description (à quoi ça sert)**\n\nConfigurer ses horaires et réservations — tutoriel en préparation dans le module Site Web & Vitrine. Il arrive très bientôt dans ce fil conducteur.\n\n**Comment ça marche**\n\n1. Cette vidéo est en cours de tournage dans les cuisines FoodEatUp.\n2. Sa fiche est déjà en place : elle se remplira dès la mise en ligne.\n\n---",
              "correspondance": "numéro",
              "confiance": 1.0
            },
            "tutorielModuleUrl": "https://tutoriel.foodeatup.com/module/site-web-vitrine",
            "higgsfield": {
              "videoSourceUrl": null,
              "duree": "10 s",
              "format": "vertical 9:16",
              "source": null
            },
            "masterRapidoUrl": null
          },
          {
            "id": "EP133",
            "numero": 133,
            "saison": 5,
            "slug": "ep133-le-but-a-la-90e",
            "titre": "Le but à la 90e",
            "module": "Caisse POS",
            "chapitre": "3 - Encaisser une commande",
            "accroche": "Une minute pour encaisser trois tournées.",
            "punchline": "Ta caisse doit tenir le rythme.",
            "resume": "Trois tournées en une minute : tu encaisses au comptoir ou à table, TPE relié, ticket envoyé. Ta caisse tient le rythme du match.",
            "statut": "bloque",
            "dureeSecondes": null,
            "videoUrl": null,
            "reseaux": {
              "facebook": {
                "statut": "a_venir",
                "date": null,
                "heure": "12:00",
                "compte": "FoodEatUp",
                "format": "Vidéo native 9:16",
                "lienCta": "https://site.foodeatup.com/"
              },
              "instagram": {
                "statut": "a_venir",
                "date": null,
                "heure": "18:30",
                "compte": "foodeatup.cocuisinage",
                "format": "Reel 9:16",
                "lienCta": null
              },
              "tiktok": {
                "statut": "a_venir",
                "date": null,
                "heure": "19:00",
                "compte": "foodeatup",
                "format": "Vidéo 9:16",
                "lienCta": null
              },
              "linkedin": {
                "statut": "a_venir",
                "date": null,
                "heure": "08:00",
                "compte": "FoodEatUp",
                "format": "Vidéo native 9:16",
                "lienCta": "https://site.foodeatup.com/"
              },
              "youtube": {
                "statut": "a_venir",
                "date": null,
                "heure": "10:00",
                "compte": "@FoodEatUp",
                "format": "Short 9:16",
                "lienCta": "https://site.foodeatup.com/"
              }
            },
            "blocage": "Le chapitre correspondant n'a pas encore de vidéo dans le Drive interne.",
            "posterUrl": null,
            "datePrevue": null,
            "troisMots": "ENCAISSER UNE COMMANDE",
            "tutoriel": null,
            "tutorielModuleUrl": null,
            "tutorielManquant": "Le module Caisse POS n'existe pas encore dans l'Academy.",
            "higgsfield": {
              "videoSourceUrl": null,
              "duree": "10 s",
              "format": "vertical 9:16",
              "source": null
            },
            "masterRapidoUrl": null
          },
          {
            "id": "EP134",
            "numero": 134,
            "saison": 5,
            "slug": "ep134-pov-la-friteuse",
            "titre": "POV : la friteuse",
            "module": "HACCP",
            "chapitre": "relevé de température",
            "accroche": "Sept heures de service. Vue d'en bas.",
            "punchline": "Elle aussi a une température à respecter.",
            "resume": "L'huile et les frigos ont leurs seuils. Le relevé se fait en dix secondes, il est daté et gardé. Ta friteuse aussi a une conformité.",
            "statut": "a_produire",
            "dureeSecondes": null,
            "videoUrl": null,
            "reseaux": {
              "facebook": {
                "statut": "a_venir",
                "date": "2026-11-23",
                "heure": "12:00",
                "compte": "FoodEatUp",
                "format": "Vidéo native 9:16",
                "lienCta": "https://site.foodeatup.com/"
              },
              "instagram": {
                "statut": "a_venir",
                "date": "2026-11-23",
                "heure": "18:30",
                "compte": "foodeatup.cocuisinage",
                "format": "Reel 9:16",
                "lienCta": null
              },
              "tiktok": {
                "statut": "a_venir",
                "date": "2026-11-23",
                "heure": "19:00",
                "compte": "foodeatup",
                "format": "Vidéo 9:16",
                "lienCta": null
              },
              "linkedin": {
                "statut": "a_venir",
                "date": "2026-11-23",
                "heure": "08:00",
                "compte": "FoodEatUp",
                "format": "Vidéo native 9:16",
                "lienCta": "https://site.foodeatup.com/"
              },
              "youtube": {
                "statut": "a_venir",
                "date": "2026-11-23",
                "heure": "10:00",
                "compte": "@FoodEatUp",
                "format": "Short 9:16",
                "lienCta": "https://site.foodeatup.com/"
              }
            },
            "posterUrl": null,
            "datePrevue": "2026-11-23",
            "troisMots": "RELEVÉ DE TEMPÉRATURE",
            "tutoriel": {
              "titre": "Relever une température d'équipement",
              "slug": "relever-une-temperature-equipement",
              "url": "https://tutoriel.foodeatup.com/tutoriel/relever-une-temperature-equipement",
              "module": "Hygiène & HACCP",
              "etape": "Températures & équipements\n- **Statut** : En ligne (0 min 38 s)\n- **Vidéo** : https://rapido-software.s3.eu-west-3.amazonaws.com/rapidosoftware/cms/bibliotheque/foodeatup-temperature-tuto-v1.mp4\n\n**Description (à quoi ça sert)**\n\nTenir votre registre de températures au moment du relevé, pas le soir de mémoire ni sur une feuille scotchée à la porte du frigo. Chaque valeur saisie est datée, horodatée et rattachée à son équipement, puis confrontée automatiquement à la plage cible que vous avez définie : ce qui sort des clous est marqué non conforme immédiatement, pendant que vous êtes encore devant l'équipement et que vous pouvez agir. C'est ce qui transforme un contrôle de routine en historique HACCP présentable à un inspecteur.\n\n**Comment ça marche**\n\n1. Ouvrez Hygiène & HACCP puis \"Températures\" : l'onglet Équipements liste vos frigos, congélateurs et chambres froides\n2. Chaque ligne affiche la plage cible de l'équipement — ici Frigo 5, min 0 °C, max 4 °C\n3. Ajustez la valeur relevée avec les boutons − et + de la colonne Température\n4. Cliquez sur \"Enregistrer les relevés de température\" en bas de la page\n5. Confirmez dans la fenêtre \"Enregistrer les relevés ?\", qui récapitule le nombre d'équipements et de plats modifiés\n6. Validez le message \"Enregistré ! Les relevés ont été sauvegardés avec succès.\"\n7. Les compteurs du jour se recalculent aussitôt : Total aujourd'hui, Conformes, Alertes et Non conformes\n8. Un relevé hors plage bascule directement en non conforme — 9 °C pour un maximum de 4 °C part en non conforme, sans intervention de votre part\n\n**Astuce du chef** : Relevez toujours aux mêmes moments — ouverture et fermeture — plutôt que « quand on y pense » : un historique régulier vaut bien mieux qu'un historique dense mais troué, c'est la régularité que regarde l'inspecteur. Et ne « corrigez » jamais une valeur hors plage pour faire propre : un 9 °C tracé, daté et suivi d'une action est votre meilleure défense, alors qu'un 4 °C confortable sur un frigo qui dérive ne protège personne — surtout pas vos stocks.\n\n---",
              "correspondance": "texte",
              "confiance": 0.73
            },
            "tutorielModuleUrl": "https://tutoriel.foodeatup.com/module/haccp",
            "higgsfield": {
              "videoSourceUrl": null,
              "duree": "10 s",
              "format": "vertical 9:16",
              "source": null
            },
            "masterRapidoUrl": null
          },
          {
            "id": "EP135",
            "numero": 135,
            "saison": 5,
            "slug": "ep135-pov-le-carnet-de-reservations",
            "titre": "POV : le carnet de réservations",
            "module": "Réservation",
            "chapitre": "1 - Réservations du jour",
            "accroche": "Toutes tes réservations du soir.",
            "punchline": "Sur du papier. Vraiment ?",
            "resume": "Tes réservations du soir sont ici, pas sur un carnet taché de café : contact, couverts, table, historique. Rien ne s'efface.",
            "statut": "a_produire",
            "dureeSecondes": null,
            "videoUrl": null,
            "reseaux": {
              "facebook": {
                "statut": "a_venir",
                "date": "2026-11-24",
                "heure": "12:00",
                "compte": "FoodEatUp",
                "format": "Vidéo native 9:16",
                "lienCta": "https://site.foodeatup.com/"
              },
              "instagram": {
                "statut": "a_venir",
                "date": "2026-11-24",
                "heure": "18:30",
                "compte": "foodeatup.cocuisinage",
                "format": "Reel 9:16",
                "lienCta": null
              },
              "tiktok": {
                "statut": "a_venir",
                "date": "2026-11-24",
                "heure": "19:00",
                "compte": "foodeatup",
                "format": "Vidéo 9:16",
                "lienCta": null
              },
              "linkedin": {
                "statut": "a_venir",
                "date": "2026-11-24",
                "heure": "08:00",
                "compte": "FoodEatUp",
                "format": "Vidéo native 9:16",
                "lienCta": "https://site.foodeatup.com/"
              },
              "youtube": {
                "statut": "a_venir",
                "date": "2026-11-24",
                "heure": "10:00",
                "compte": "@FoodEatUp",
                "format": "Short 9:16",
                "lienCta": "https://site.foodeatup.com/"
              }
            },
            "posterUrl": null,
            "datePrevue": "2026-11-24",
            "troisMots": "RÉSERVATIONS DU JOUR",
            "tutoriel": {
              "titre": "Retrouver ses réservations du jour",
              "slug": "retrouver-ses-reservations-du-jour",
              "url": "https://tutoriel.foodeatup.com/tutoriel/retrouver-ses-reservations-du-jour",
              "module": "Réservations & Plan de salle",
              "etape": "Réservations du jour\n- **Statut** : En ligne (0 min 51 s)\n- **Vidéo** : https://rapido-software.s3.eu-west-3.amazonaws.com/rapidosoftware/cms/bibliotheque/foodeatup-reservations-jour-tuto\n\n**Description (à quoi ça sert)**\n\nCentraliser sur un seul écran le plan de salle en temps réel, la file d'attente et les réservations du jour — pour savoir en un coup d'œil qui arrive, où l'installer, et ce qui reste disponible, sans jongler entre plusieurs outils.\n\n**Comment ça marche**\n\n1. Ouvrez Réservations : le plan de salle affiche chaque table en temps réel, avec son statut coloré (Libre, Réservée, Occupée, À nettoyer).\n2. La file d'attente liste les clients sans réservation, prêts à être placés dès qu'une table se libère.\n3. Plus bas, la liste Réservations du jour détaille chaque arrivée attendue : heure, client, nombre de couverts.\n4. Chaque ligne affiche aussi la table déjà assignée et son statut d'installation en direct (ex. Installée).\n5. D'un coup d'œil, vous savez qui arrive, où l'installer, et ce qui reste disponible pour le service.\n\n**Astuce du chef** : Gardez un œil sur la file d'attente autant que sur les réservations : un client sans réservation peut souvent être casé sur une table libérée entre deux arrivées prévues — le plan de salle en temps réel vous montre cette fenêtre avant qu'elle ne se referme.\n\n---",
              "correspondance": "numéro",
              "confiance": 1.0
            },
            "tutorielModuleUrl": "https://tutoriel.foodeatup.com/module/reservation-salle",
            "higgsfield": {
              "videoSourceUrl": null,
              "duree": "10 s",
              "format": "vertical 9:16",
              "source": null
            },
            "masterRapidoUrl": null
          },
          {
            "id": "EP136",
            "numero": 136,
            "saison": 5,
            "slug": "ep136-pov-le-lave-verres",
            "titre": "POV : le lave-verres",
            "module": "Service",
            "chapitre": "1 - Commandes multi-canaux",
            "accroche": "Deux minutes par cycle. Quatre-vingts cycles.",
            "punchline": "Le service, c'est ça aussi.",
            "resume": "Le service, c'est cent gestes invisibles. FoodEatUp en enregistre la trace pour que tu saches où part vraiment ton temps.",
            "statut": "a_produire",
            "dureeSecondes": null,
            "videoUrl": null,
            "reseaux": {
              "facebook": {
                "statut": "a_venir",
                "date": "2026-11-25",
                "heure": "12:00",
                "compte": "FoodEatUp",
                "format": "Vidéo native 9:16",
                "lienCta": "https://site.foodeatup.com/"
              },
              "instagram": {
                "statut": "a_venir",
                "date": "2026-11-25",
                "heure": "18:30",
                "compte": "foodeatup.cocuisinage",
                "format": "Reel 9:16",
                "lienCta": null
              },
              "tiktok": {
                "statut": "a_venir",
                "date": "2026-11-25",
                "heure": "19:00",
                "compte": "foodeatup",
                "format": "Vidéo 9:16",
                "lienCta": null
              },
              "linkedin": {
                "statut": "a_venir",
                "date": "2026-11-25",
                "heure": "08:00",
                "compte": "FoodEatUp",
                "format": "Vidéo native 9:16",
                "lienCta": "https://site.foodeatup.com/"
              },
              "youtube": {
                "statut": "a_venir",
                "date": "2026-11-25",
                "heure": "10:00",
                "compte": "@FoodEatUp",
                "format": "Short 9:16",
                "lienCta": "https://site.foodeatup.com/"
              }
            },
            "posterUrl": null,
            "datePrevue": "2026-11-25",
            "troisMots": "COMMANDES MULTI-CANAUX",
            "tutoriel": {
              "titre": "Mes commandes : QR code, site web, agent vocal (toutes vos commandes)",
              "slug": "mes-commandes-tous-canaux",
              "url": "https://tutoriel.foodeatup.com/tutoriel/mes-commandes-tous-canaux",
              "module": "Service Multi-Canal",
              "etape": "Recevoir ses commandes\n- **Statut** : En ligne (1 min 09 s)\n- **Vidéo** : https://rapido-software.s3.eu-west-3.amazonaws.com/rapidosoftware/cms/bibliotheque/foodeatup-mes-commandes-tuto-v1\n\n**Description (à quoi ça sert)**\n\nCentraliser toutes vos commandes — QR code table, site vitrine, agent vocal ou saisie manuelle — dans une seule liste, avec canal, statut et total visibles d'un coup d'œil. Créez, modifiez ou supprimez une commande sans changer d'écran.\n\n**Comment ça marche**\n\n1. Ouvrez \"Mes commandes\" : la liste complète, avec le canal (Manuel, Vitrine, Sur place...), le statut et le total de chaque commande\n2. Cliquez sur \"+ Nouvelle commande\" pour en créer une manuellement\n3. Renseignez le client, le canal, le mode de service, puis ajoutez vos plats\n4. Cliquez sur \"Créer la commande\" : la facture et le devis sont générés automatiquement\n5. Cliquez sur une commande pour voir son détail, ou sur \"Modifier\" pour ajuster les articles et le statut, puis \"Mettre à jour\"\n6. Pour la retirer : menu \"⋮\" > \"Supprimer\", puis confirmez\n\n**Astuce du chef** : Le canal affiché sur chaque ligne (Manuel, Vitrine, Sur place...) vous dit immédiatement d'où vient la commande sans avoir à l'ouvrir — utile en coup de feu pour prioriser. Et avant de supprimer une commande, vérifiez sa facture/devis liés (visibles dans le détail) : une commande facturée qui disparaît laisse la facture orpheline, mieux vaut parfois la passer en \"Annulée\" plutôt que la supprimer.\n\n---",
              "correspondance": "numéro",
              "confiance": 1.0
            },
            "tutorielModuleUrl": "https://tutoriel.foodeatup.com/module/service-commande",
            "higgsfield": {
              "videoSourceUrl": null,
              "duree": "10 s",
              "format": "vertical 9:16",
              "source": null
            },
            "masterRapidoUrl": null
          },
          {
            "id": "EP137",
            "numero": 137,
            "saison": 5,
            "slug": "ep137-pov-la-machine-a-cafe",
            "titre": "POV : la machine à café",
            "module": "Caisse POS",
            "chapitre": "3 - Encaisser une commande",
            "accroche": "Deux cent quarante cafés. Aujourd'hui.",
            "punchline": "Combien encaissés ? Tu es sûr ?",
            "resume": "Deux cent quarante cafés, deux cent quarante lignes encaissées. Tu compares le vendu et l'encaissé, à l'unité près.",
            "statut": "bloque",
            "dureeSecondes": null,
            "videoUrl": null,
            "reseaux": {
              "facebook": {
                "statut": "a_venir",
                "date": null,
                "heure": "12:00",
                "compte": "FoodEatUp",
                "format": "Vidéo native 9:16",
                "lienCta": "https://site.foodeatup.com/"
              },
              "instagram": {
                "statut": "a_venir",
                "date": null,
                "heure": "18:30",
                "compte": "foodeatup.cocuisinage",
                "format": "Reel 9:16",
                "lienCta": null
              },
              "tiktok": {
                "statut": "a_venir",
                "date": null,
                "heure": "19:00",
                "compte": "foodeatup",
                "format": "Vidéo 9:16",
                "lienCta": null
              },
              "linkedin": {
                "statut": "a_venir",
                "date": null,
                "heure": "08:00",
                "compte": "FoodEatUp",
                "format": "Vidéo native 9:16",
                "lienCta": "https://site.foodeatup.com/"
              },
              "youtube": {
                "statut": "a_venir",
                "date": null,
                "heure": "10:00",
                "compte": "@FoodEatUp",
                "format": "Short 9:16",
                "lienCta": "https://site.foodeatup.com/"
              }
            },
            "blocage": "Le chapitre correspondant n'a pas encore de vidéo dans le Drive interne.",
            "posterUrl": null,
            "datePrevue": null,
            "troisMots": "ENCAISSER UNE COMMANDE",
            "tutoriel": null,
            "tutorielModuleUrl": null,
            "tutorielManquant": "Le module Caisse POS n'existe pas encore dans l'Academy.",
            "higgsfield": {
              "videoSourceUrl": null,
              "duree": "10 s",
              "format": "vertical 9:16",
              "source": null
            },
            "masterRapidoUrl": null
          },
          {
            "id": "EP138",
            "numero": 138,
            "saison": 5,
            "slug": "ep138-pov-l-assiette-du-pass-a-la-table",
            "titre": "POV : l'assiette, du pass à la table",
            "module": "KDS",
            "chapitre": "3 - Gérer le KDS en direct",
            "accroche": "Quarante-cinq secondes de vie.",
            "punchline": "Chaque assiette compte. Compte-les.",
            "resume": "De l'envoi au pass, chaque plat a son statut et son chrono. Tu comptes tes assiettes, tu ne les devines pas.",
            "statut": "bloque",
            "dureeSecondes": null,
            "videoUrl": null,
            "reseaux": {
              "facebook": {
                "statut": "a_venir",
                "date": null,
                "heure": "12:00",
                "compte": "FoodEatUp",
                "format": "Vidéo native 9:16",
                "lienCta": "https://site.foodeatup.com/"
              },
              "instagram": {
                "statut": "a_venir",
                "date": null,
                "heure": "18:30",
                "compte": "foodeatup.cocuisinage",
                "format": "Reel 9:16",
                "lienCta": null
              },
              "tiktok": {
                "statut": "a_venir",
                "date": null,
                "heure": "19:00",
                "compte": "foodeatup",
                "format": "Vidéo 9:16",
                "lienCta": null
              },
              "linkedin": {
                "statut": "a_venir",
                "date": null,
                "heure": "08:00",
                "compte": "FoodEatUp",
                "format": "Vidéo native 9:16",
                "lienCta": "https://site.foodeatup.com/"
              },
              "youtube": {
                "statut": "a_venir",
                "date": null,
                "heure": "10:00",
                "compte": "@FoodEatUp",
                "format": "Short 9:16",
                "lienCta": "https://site.foodeatup.com/"
              }
            },
            "blocage": "Le chapitre correspondant n'a pas encore de vidéo dans le Drive interne.",
            "posterUrl": null,
            "datePrevue": null,
            "troisMots": "GÉRER KDS DIRECT",
            "tutoriel": {
              "titre": "Gérer une commande en direct sur le KDS",
              "slug": "gerer-une-commande-en-direct-kds",
              "url": "https://tutoriel.foodeatup.com/tutoriel/gerer-une-commande-en-direct-kds",
              "module": "Écran Cuisine (KDS)",
              "etape": "Gérer une commande\n- **Statut** : Bientôt disponible (tournage en cours)\n\n**Description (à quoi ça sert)**\n\nGérer une commande en direct sur le KDS — tutoriel en préparation dans le module Écran Cuisine (KDS). Il arrive très bientôt dans ce fil conducteur.\n\n**Comment ça marche**\n\n1. Cette vidéo est en cours de tournage dans les cuisines FoodEatUp.\n2. Sa fiche est déjà en place : elle se remplira dès la mise en ligne.\n\n---",
              "correspondance": "numéro",
              "confiance": 1.0
            },
            "tutorielModuleUrl": "https://tutoriel.foodeatup.com/module/kds-cuisine",
            "higgsfield": {
              "videoSourceUrl": null,
              "duree": "10 s",
              "format": "vertical 9:16",
              "source": null
            },
            "masterRapidoUrl": null
          },
          {
            "id": "EP139",
            "numero": 139,
            "saison": 5,
            "slug": "ep139-le-rush-film-de-guerre",
            "titre": "Le rush, film de guerre",
            "module": "KDS",
            "chapitre": "2 - Vue KDS par poste",
            "accroche": "20 h 30. Le coup de feu.",
            "punchline": "Sois équipé, pas héroïque.",
            "resume": "Pendant le coup de feu, tu vois la charge de chaque poste. Tu envoies où il y a de la place. Être équipé, c'est ça.",
            "statut": "a_produire",
            "dureeSecondes": null,
            "videoUrl": null,
            "reseaux": {
              "facebook": {
                "statut": "a_venir",
                "date": "2026-11-26",
                "heure": "12:00",
                "compte": "FoodEatUp",
                "format": "Vidéo native 9:16",
                "lienCta": "https://site.foodeatup.com/"
              },
              "instagram": {
                "statut": "a_venir",
                "date": "2026-11-26",
                "heure": "18:30",
                "compte": "foodeatup.cocuisinage",
                "format": "Reel 9:16",
                "lienCta": null
              },
              "tiktok": {
                "statut": "a_venir",
                "date": "2026-11-26",
                "heure": "19:00",
                "compte": "foodeatup",
                "format": "Vidéo 9:16",
                "lienCta": null
              },
              "linkedin": {
                "statut": "a_venir",
                "date": "2026-11-26",
                "heure": "08:00",
                "compte": "FoodEatUp",
                "format": "Vidéo native 9:16",
                "lienCta": "https://site.foodeatup.com/"
              },
              "youtube": {
                "statut": "a_venir",
                "date": "2026-11-26",
                "heure": "10:00",
                "compte": "@FoodEatUp",
                "format": "Short 9:16",
                "lienCta": "https://site.foodeatup.com/"
              }
            },
            "posterUrl": null,
            "datePrevue": "2026-11-26",
            "troisMots": "VUE KDS PAR",
            "tutoriel": {
              "titre": "Afficher le KDS par poste",
              "slug": "afficher-le-kds-par-poste",
              "url": "https://tutoriel.foodeatup.com/tutoriel/afficher-le-kds-par-poste",
              "module": "Écran Cuisine (KDS)",
              "etape": "Affichage KDS\n- **Statut** : En ligne (0 min 49 s)\n- **Vidéo** : https://rapido-software.s3.eu-west-3.amazonaws.com/rapidosoftware/cms/bibliotheque/foodeatup-kds-par-poste-tuto\n\n**Description (à quoi ça sert)**\n\nDonner à chaque poste de cuisine un écran filtré sur ses seules commandes, synchronisé en temps réel avec les autres postes — le Pass sait exactement quand tous les plats d'une commande sont prêts, sans que personne n'ait à se déplacer ou à s'appeler d'un bout à l'autre de la cuisine.\n\n**Comment ça marche**\n\n1. Depuis Cuisine (KDS), chaque poste — chaud, pass, froid — a son propre écran, avec ses propres règles de routage (quelles catégories de plats lui arrivent).\n2. Cliquez sur Ouvrir l'écran pour afficher l'écran dédié de ce poste, en plein écran (tablette ou TV).\n3. Les commandes confirmées arrivent en temps réel sur l'écran du poste concerné dès leur validation, sans rafraîchissement manuel.\n4. Une fois un plat prêt, l'équipe clique sur Bump [poste] : il est marqué prêt et disparaît de l'écran de ce poste.\n5. Le poste Pass centralise ce qui doit sortir : chaque ticket y affiche l'état de ses plats venant des autres postes (ex. « CHAUD … » = en attente d'être bumpé).\n6. Dès que tous les plats d'un ticket sont bumpés sur leurs postes respectifs, le bouton Fire Service s'active sur le Pass : la commande est prête à partir en salle.\n\n**Astuce du chef** : Le bouton Bump ne veut pas dire « servi » mais « prêt et transmis » : sur un poste de préparation (chaud, froid...), il fait remonter le plat au Pass ; sur le Pass, c'est Fire Service qui déclenche l'envoi réel en salle. Tant qu'un seul poste n'a pas bumpé son plat, le ticket reste bloqué au Pass — c'est justement ce qui empêche une commande de partir incomplète, même en plein coup de feu.\n\n---",
              "correspondance": "numéro",
              "confiance": 1.0
            },
            "tutorielModuleUrl": "https://tutoriel.foodeatup.com/module/kds-cuisine",
            "higgsfield": {
              "videoSourceUrl": null,
              "duree": "10 s",
              "format": "vertical 9:16",
              "source": null
            },
            "masterRapidoUrl": null
          },
          {
            "id": "EP140",
            "numero": 140,
            "saison": 5,
            "slug": "ep140-le-braquage-du-frigo",
            "titre": "Le braquage du frigo",
            "module": "StockVision",
            "chapitre": "16 - Mouvements de stock",
            "accroche": "Ton inventaire, la nuit.",
            "punchline": "Ce qui disparaît finit toujours par se voir.",
            "resume": "L'inventaire est daté, signé, comparé au théorique. Ce qui disparaît la nuit finit toujours par apparaître dans l'écart.",
            "statut": "a_produire",
            "dureeSecondes": null,
            "videoUrl": null,
            "reseaux": {
              "facebook": {
                "statut": "a_venir",
                "date": "2026-11-27",
                "heure": "12:00",
                "compte": "FoodEatUp",
                "format": "Vidéo native 9:16",
                "lienCta": "https://site.foodeatup.com/"
              },
              "instagram": {
                "statut": "a_venir",
                "date": "2026-11-27",
                "heure": "18:30",
                "compte": "foodeatup.cocuisinage",
                "format": "Reel 9:16",
                "lienCta": null
              },
              "tiktok": {
                "statut": "a_venir",
                "date": "2026-11-27",
                "heure": "19:00",
                "compte": "foodeatup",
                "format": "Vidéo 9:16",
                "lienCta": null
              },
              "linkedin": {
                "statut": "a_venir",
                "date": "2026-11-27",
                "heure": "08:00",
                "compte": "FoodEatUp",
                "format": "Vidéo native 9:16",
                "lienCta": "https://site.foodeatup.com/"
              },
              "youtube": {
                "statut": "a_venir",
                "date": "2026-11-27",
                "heure": "10:00",
                "compte": "@FoodEatUp",
                "format": "Short 9:16",
                "lienCta": "https://site.foodeatup.com/"
              }
            },
            "posterUrl": null,
            "datePrevue": "2026-11-27",
            "troisMots": "MOUVEMENTS DE STOCK",
            "tutoriel": {
              "titre": "Lire ses mouvements de stock FoodEatUp",
              "slug": "lire-ses-mouvements-de-stock",
              "url": "https://tutoriel.foodeatup.com/tutoriel/lire-ses-mouvements-de-stock",
              "module": "StockVision AI",
              "etape": "Stock\n- **Statut** : En ligne (0 min 46 s)\n- **Vidéo** : https://rapido-software.s3.eu-west-3.amazonaws.com/rapidosoftware/cms/bibliotheque/foodeatup-mouvements-stock-tuto-v1\n\n**Description (à quoi ça sert)**\n\nDisposer d'un registre lisible de tout ce qui entre et sort de votre cuisine, et pouvoir remonter à la source de n'importe quel écart : qui a saisi quoi, quand, pour quel motif et chez quel fournisseur. C'est la pièce qui rend votre inventaire vérifiable au lieu d'être déclaratif.\n\n**Comment ça marche**\n\n1. Ouvrez \"Gestion des stocks\" puis \"Mouvements de Stock\" : chaque ligne indique le produit, le type (Entrée ou Sortie), la quantité, le motif, le fournisseur, la date et l'utilisateur\n2. Ouvrez le menu \"Action\" (les trois points) au bout de la ligne, puis cliquez sur \"Voir détails\"\n3. Lisez la fiche complète : Informations Générales (produit, type de mouvement, quantité, motif) et Informations Supplémentaires (fournisseur, date et heure exactes, utilisateur qui a fait la saisie)\n4. Pour corriger une erreur de saisie, cliquez sur \"Supprimer\" en haut à droite de la fiche\n5. Confirmez dans la fenêtre : la suppression affecte également le stock, pas seulement la ligne du registre\n6. Le mouvement disparaît du registre et le stock est recalculé en conséquence\n\n**Astuce du chef** : Supprimer un mouvement n'efface pas seulement une ligne d'historique : le stock est recalculé derrière. Si vous supprimez une entrée de 5000 pièces, ces 5000 pièces quittent aussi votre stock. Avant de supprimer, ouvrez toujours la fiche de détail et vérifiez la quantité et le motif — c'est le réflexe qui évite de transformer une erreur de saisie en écart d'inventaire.\n\n---",
              "correspondance": "numéro",
              "confiance": 1.0
            },
            "tutorielModuleUrl": "https://tutoriel.foodeatup.com/module/stockvision-ai",
            "higgsfield": {
              "videoSourceUrl": null,
              "duree": "10 s",
              "format": "vertical 9:16",
              "source": null
            },
            "masterRapidoUrl": null
          },
          {
            "id": "EP141",
            "numero": 141,
            "saison": 5,
            "slug": "ep141-cuisine-cockpit-spatial",
            "titre": "Cuisine, cockpit spatial",
            "module": "PrediBot",
            "chapitre": "3 - Parler à PrediBot",
            "accroche": "Table 6 depuis 22 minutes.",
            "punchline": "Un pilote automatique, ça existe aussi en cuisine.",
            "resume": "Tu demandes, PrediBot répond avec tes vraies données : la table en attente, la production à lancer, l'alerte à traiter. Le pilote automatique existe.",
            "statut": "a_produire",
            "dureeSecondes": null,
            "videoUrl": null,
            "reseaux": {
              "facebook": {
                "statut": "a_venir",
                "date": "2026-11-28",
                "heure": "12:00",
                "compte": "FoodEatUp",
                "format": "Vidéo native 9:16",
                "lienCta": "https://site.foodeatup.com/"
              },
              "instagram": {
                "statut": "a_venir",
                "date": "2026-11-28",
                "heure": "18:30",
                "compte": "foodeatup.cocuisinage",
                "format": "Reel 9:16",
                "lienCta": null
              },
              "tiktok": {
                "statut": "a_venir",
                "date": "2026-11-28",
                "heure": "19:00",
                "compte": "foodeatup",
                "format": "Vidéo 9:16",
                "lienCta": null
              },
              "linkedin": {
                "statut": "a_venir",
                "date": "2026-11-28",
                "heure": "08:00",
                "compte": "FoodEatUp",
                "format": "Vidéo native 9:16",
                "lienCta": "https://site.foodeatup.com/"
              },
              "youtube": {
                "statut": "a_venir",
                "date": "2026-11-28",
                "heure": "10:00",
                "compte": "@FoodEatUp",
                "format": "Short 9:16",
                "lienCta": "https://site.foodeatup.com/"
              }
            },
            "posterUrl": null,
            "datePrevue": "2026-11-28",
            "troisMots": "PARLER À PREDIBOT",
            "tutoriel": {
              "titre": "Parler à PrediBot avec nos prompts",
              "slug": "parler-a-predibot-avec-nos-prompts",
              "url": "https://tutoriel.foodeatup.com/tutoriel/parler-a-predibot-avec-nos-prompts",
              "module": "PrediBot (Agent IA Directeur)",
              "etape": "Dialoguer avec PrediBot\n- **Statut** : En ligne (0 min 35 s)\n- **Vidéo** : https://rapido-software.s3.eu-west-3.amazonaws.com/rapidosoftware/cms/bibliotheque/parler-a-predibot-avec-nos-prompts-v1\n\n**Description (à quoi ça sert)**\n\nPiloter toute la gestion RH de votre restaurant — employés, congés, pointages, classement — sans ouvrir un seul écran : il suffit d'écrire la consigne à Predibot, votre agent IA, sur WhatsApp.\n\n**Comment ça marche**\n\n1. Sur WhatsApp, écrivez à Predibot : demandez la liste de vos employés ou celle des congés en attente\n2. Approuvez un congé en une phrase, ou refusez-le en précisant le motif — en quelques secondes\n3. Vérifiez les pointages sur la période de votre choix\n4. Laissez Predibot classer vos employés par performance (heures, retards, congés)\n\n**Astuce du chef** : Chaque réponse de Predibot contient un lien direct vers l'écran FoodEatUp concerné (ex. .../establishment/26/leaves) : cliquez dessus pour vérifier le détail avant de trancher sur un congé sensible.\n\n---",
              "correspondance": "numéro",
              "confiance": 1.0
            },
            "tutorielModuleUrl": "https://tutoriel.foodeatup.com/module/predibot",
            "higgsfield": {
              "videoSourceUrl": null,
              "duree": "10 s",
              "format": "vertical 9:16",
              "source": null
            },
            "masterRapidoUrl": null
          },
          {
            "id": "EP142",
            "numero": 142,
            "saison": 5,
            "slug": "ep142-duel-a-la-spatule",
            "titre": "Duel à la spatule",
            "module": "Équipe & Planning",
            "chapitre": "affectation des postes",
            "accroche": "Qui envoie le plat du jour.",
            "punchline": "Répartis les postes avant le service, pas pendant.",
            "resume": "Les postes sont répartis avant le service, pas pendant. Chacun sait ce qu'il envoie, personne ne dégaine sa spatule pour le savoir.",
            "statut": "a_produire",
            "dureeSecondes": null,
            "videoUrl": null,
            "reseaux": {
              "facebook": {
                "statut": "a_venir",
                "date": "2026-11-29",
                "heure": "12:00",
                "compte": "FoodEatUp",
                "format": "Vidéo native 9:16",
                "lienCta": "https://site.foodeatup.com/"
              },
              "instagram": {
                "statut": "a_venir",
                "date": "2026-11-29",
                "heure": "18:30",
                "compte": "foodeatup.cocuisinage",
                "format": "Reel 9:16",
                "lienCta": null
              },
              "tiktok": {
                "statut": "a_venir",
                "date": "2026-11-29",
                "heure": "19:00",
                "compte": "foodeatup",
                "format": "Vidéo 9:16",
                "lienCta": null
              },
              "linkedin": {
                "statut": "a_venir",
                "date": "2026-11-29",
                "heure": "08:00",
                "compte": "FoodEatUp",
                "format": "Vidéo native 9:16",
                "lienCta": "https://site.foodeatup.com/"
              },
              "youtube": {
                "statut": "a_venir",
                "date": "2026-11-29",
                "heure": "10:00",
                "compte": "@FoodEatUp",
                "format": "Short 9:16",
                "lienCta": "https://site.foodeatup.com/"
              }
            },
            "posterUrl": null,
            "datePrevue": "2026-11-29",
            "troisMots": "AFFECTATION DES POSTES",
            "tutoriel": {
              "titre": "Ajouter ses employés FoodEatUp",
              "slug": "ajouter-ses-employes",
              "url": "https://tutoriel.foodeatup.com/tutoriel/ajouter-ses-employes",
              "module": "Équipe, Planning & RH",
              "etape": "Employés & contrats\n- **Statut** : En ligne (0 min 46 s)\n- **Vidéo** : https://rapido-software.s3.eu-west-3.amazonaws.com/rapidosoftware/cms/bibliotheque/ajouter-ses-employes-v1\n\n**Description (à quoi ça sert)**\n\nAjouter rapidement un nouvel employé à votre équipe FoodEatUp — coordonnées, rôle et horaires de travail — pour lui donner accès aux bons outils dès son arrivée.\n\n**Comment ça marche**\n\n1. Cliquez sur \"Ajouter un employé\"\n2. Renseignez son prénom, son nom, son email, son téléphone et son rôle\n3. Définissez ses horaires de travail (jour, heure de début, heure de fin, repos)\n4. Cliquez sur \"Ajouter\" — il apparaît aussitôt dans votre équipe\n5. Cliquez sur \"Voir\" pour retrouver sa fiche complète (coordonnées, rôle, horaires)\n\n**Astuce du chef** : Le rôle choisi détermine les permissions de l'employé (ex: HACCP pour un Chef) — vous pouvez ajuster cela à tout moment depuis \"Gérer les rôles\" sans recréer sa fiche.\n\n---",
              "correspondance": "texte",
              "confiance": 0.48
            },
            "tutorielModuleUrl": "https://tutoriel.foodeatup.com/module/equipe-planning",
            "higgsfield": {
              "videoSourceUrl": null,
              "duree": "10 s",
              "format": "vertical 9:16",
              "source": null
            },
            "masterRapidoUrl": null
          },
          {
            "id": "EP143",
            "numero": 143,
            "saison": 5,
            "slug": "ep143-la-commande-de-200-pieces",
            "titre": "La commande de 200 pièces",
            "module": "Comptabilité",
            "chapitre": "devis",
            "accroche": "Une seule commande.",
            "punchline": "Deux cents parts. Anticipe-les.",
            "resume": "Deux cents parts, ça commence par un devis : quantités, prix, marge. Il se transforme en commande, puis en facture, sans ressaisie.",
            "statut": "a_produire",
            "dureeSecondes": null,
            "videoUrl": null,
            "reseaux": {
              "facebook": {
                "statut": "a_venir",
                "date": "2026-11-30",
                "heure": "12:00",
                "compte": "FoodEatUp",
                "format": "Vidéo native 9:16",
                "lienCta": "https://site.foodeatup.com/"
              },
              "instagram": {
                "statut": "a_venir",
                "date": "2026-11-30",
                "heure": "18:30",
                "compte": "foodeatup.cocuisinage",
                "format": "Reel 9:16",
                "lienCta": null
              },
              "tiktok": {
                "statut": "a_venir",
                "date": "2026-11-30",
                "heure": "19:00",
                "compte": "foodeatup",
                "format": "Vidéo 9:16",
                "lienCta": null
              },
              "linkedin": {
                "statut": "a_venir",
                "date": "2026-11-30",
                "heure": "08:00",
                "compte": "FoodEatUp",
                "format": "Vidéo native 9:16",
                "lienCta": "https://site.foodeatup.com/"
              },
              "youtube": {
                "statut": "a_venir",
                "date": "2026-11-30",
                "heure": "10:00",
                "compte": "@FoodEatUp",
                "format": "Short 9:16",
                "lienCta": "https://site.foodeatup.com/"
              }
            },
            "posterUrl": null,
            "datePrevue": "2026-11-30",
            "troisMots": "DEVIS",
            "tutoriel": {
              "titre": "Créer un devis FoodEatUp",
              "slug": "creer-un-devis",
              "url": "https://tutoriel.foodeatup.com/tutoriel/creer-un-devis",
              "module": "Comptabilité & Achats",
              "etape": "Devis\n- **Statut** : En ligne (1 min 06 s)\n- **Vidéo** : https://rapido-software.s3.eu-west-3.amazonaws.com/rapidosoftware/cms/bibliotheque/creer-un-devis-v1\n\n**Description (à quoi ça sert)**\n\nCréer et envoyer un devis professionnel en quelques clics — produits, remise, TVA et acompte calculés automatiquement — pour que votre client puisse le consulter et le signer en ligne sans aller-retour par email.\n\n**Comment ça marche**\n\n1. Depuis l'onglet Devis, retrouvez tous vos devis (brouillons, envoyés, signés) avec leur montant total\n2. Cliquez sur \"Créer un devis\"\n3. Choisissez le client, le délai de paiement, et le mode de règlement\n4. Recherchez un produit ou une recette : son prix et sa TVA se remplissent automatiquement\n5. Ajustez la quantité si besoin, le total se recalcule instantanément\n6. Appliquez une remise globale, une TVA globale, et demandez si besoin un acompte : le solde restant s'affiche automatiquement\n7. Choisissez d'envoyer le devis par email au client (il reçoit un lien sécurisé pour le consulter et le signer) ou de l'enregistrer en brouillon\n8. Cliquez sur \"Enregistrer\" (ou \"Enregistrer & Envoyer\") — le devis apparaît aussitôt dans votre liste\n\n**Astuce du chef** : L'acompte demandé (en pourcentage ou en montant fixe) calcule automatiquement le solde restant : pratique pour sécuriser une commande importante ou un événement avant de le confirmer. Vous pouvez aussi demander directement à Claude de créer un devis à votre place, en lui donnant simplement le client, le produit et le prix.\n\n---",
              "correspondance": "texte",
              "confiance": 0.53
            },
            "tutorielModuleUrl": "https://tutoriel.foodeatup.com/module/comptabilite",
            "higgsfield": {
              "videoSourceUrl": null,
              "duree": "10 s",
              "format": "vertical 9:16",
              "source": null
            },
            "masterRapidoUrl": null
          },
          {
            "id": "EP144",
            "numero": 144,
            "saison": 5,
            "slug": "ep144-le-proces-du-steak-trop-cuit",
            "titre": "Le procès du steak trop cuit",
            "module": "Marketing",
            "chapitre": "3 - Répondre aux avis",
            "accroche": "Un avis une étoile.",
            "punchline": "Réponds-y avant qu'il fasse jurisprudence.",
            "resume": "Un avis une étoile, tu le vois tout de suite et tu réponds depuis l'outil. Une réponse rapide vaut mieux qu'un long procès.",
            "statut": "a_produire",
            "dureeSecondes": null,
            "videoUrl": null,
            "reseaux": {
              "facebook": {
                "statut": "a_venir",
                "date": "2026-12-01",
                "heure": "12:00",
                "compte": "FoodEatUp",
                "format": "Vidéo native 9:16",
                "lienCta": "https://site.foodeatup.com/"
              },
              "instagram": {
                "statut": "a_venir",
                "date": "2026-12-01",
                "heure": "18:30",
                "compte": "foodeatup.cocuisinage",
                "format": "Reel 9:16",
                "lienCta": null
              },
              "tiktok": {
                "statut": "a_venir",
                "date": "2026-12-01",
                "heure": "19:00",
                "compte": "foodeatup",
                "format": "Vidéo 9:16",
                "lienCta": null
              },
              "linkedin": {
                "statut": "a_venir",
                "date": "2026-12-01",
                "heure": "08:00",
                "compte": "FoodEatUp",
                "format": "Vidéo native 9:16",
                "lienCta": "https://site.foodeatup.com/"
              },
              "youtube": {
                "statut": "a_venir",
                "date": "2026-12-01",
                "heure": "10:00",
                "compte": "@FoodEatUp",
                "format": "Short 9:16",
                "lienCta": "https://site.foodeatup.com/"
              }
            },
            "posterUrl": null,
            "datePrevue": "2026-12-01",
            "troisMots": "RÉPONDRE AUX AVIS",
            "tutoriel": {
              "titre": "Répondre aux avis clients",
              "slug": "repondre-aux-avis-clients",
              "url": "https://tutoriel.foodeatup.com/tutoriel/repondre-aux-avis-clients",
              "module": "Marketing, Fidélité & Iris",
              "etape": "Avis clients\n- **Statut** : En ligne (0 min 43 s)\n- **Vidéo** : https://rapido-software.s3.eu-west-3.amazonaws.com/rapidosoftware/cms/bibliotheque/foodeatup-repondre-avis-tuto-v1\n\n**Description (à quoi ça sert)**\n\nTransformer chaque avis client en dialogue public : publiez-le, répondez-y en quelques secondes, et rassurez vos futurs clients tout en faisant grimper votre taux de réponse.\n\n**Comment ça marche**\n\n1. Un nouvel avis arrive en attente de modération : cliquez sur Publier pour qu'il apparaisse sur votre site.\n2. Une fois publié, cliquez sur Répondre.\n3. Rédigez votre réponse, ou laissez l'agent vous préparer un brouillon.\n4. Cliquez sur Publier : votre réponse apparaît aussitôt sous l'avis, signée par votre établissement.\n\n**Astuce du chef** : Un avis avec réponse rassure bien plus qu'un avis seul — même une réponse courte (« Merci beaucoup ! ») montre que vous êtes présent et à l'écoute. Utilisez « Brouillon par l'agent » si vous manquez de temps, puis ajustez le ton avant de publier.\n\n---",
              "correspondance": "numéro",
              "confiance": 1.0
            },
            "tutorielModuleUrl": "https://tutoriel.foodeatup.com/module/marketing-fidelite",
            "higgsfield": {
              "videoSourceUrl": null,
              "duree": "10 s",
              "format": "vertical 9:16",
              "source": null
            },
            "masterRapidoUrl": null
          },
          {
            "id": "EP145",
            "numero": 145,
            "saison": 5,
            "slug": "ep145-documentaire-animalier-le-gerant",
            "titre": "Documentaire animalier : le gérant",
            "module": "PrediBot",
            "chapitre": "1 - Lire ses prévisions",
            "accroche": "Le gérant, dans son habitat naturel.",
            "punchline": "Espèce en voie d'épuisement.",
            "resume": "Ton point du jour en un écran : ce qui arrive, ce qui manque, ce qui coince. L'espèce « gérant épuisé » n'est pas obligée de survivre comme ça.",
            "statut": "a_produire",
            "dureeSecondes": null,
            "videoUrl": null,
            "reseaux": {
              "facebook": {
                "statut": "a_venir",
                "date": "2026-12-02",
                "heure": "12:00",
                "compte": "FoodEatUp",
                "format": "Vidéo native 9:16",
                "lienCta": "https://site.foodeatup.com/"
              },
              "instagram": {
                "statut": "a_venir",
                "date": "2026-12-02",
                "heure": "18:30",
                "compte": "foodeatup.cocuisinage",
                "format": "Reel 9:16",
                "lienCta": null
              },
              "tiktok": {
                "statut": "a_venir",
                "date": "2026-12-02",
                "heure": "19:00",
                "compte": "foodeatup",
                "format": "Vidéo 9:16",
                "lienCta": null
              },
              "linkedin": {
                "statut": "a_venir",
                "date": "2026-12-02",
                "heure": "08:00",
                "compte": "FoodEatUp",
                "format": "Vidéo native 9:16",
                "lienCta": "https://site.foodeatup.com/"
              },
              "youtube": {
                "statut": "a_venir",
                "date": "2026-12-02",
                "heure": "10:00",
                "compte": "@FoodEatUp",
                "format": "Short 9:16",
                "lienCta": "https://site.foodeatup.com/"
              }
            },
            "posterUrl": null,
            "datePrevue": "2026-12-02",
            "troisMots": "LIRE SES PRÉVISIONS",
            "tutoriel": {
              "titre": "Lire ses prévisions PrediBot",
              "slug": "lire-ses-previsions-predibot",
              "url": "https://tutoriel.foodeatup.com/tutoriel/lire-ses-previsions-predibot",
              "module": "PrediBot (Agent IA Directeur)",
              "etape": "Prévisions\n- **Statut** : En ligne (0 min 42 s)\n- **Vidéo** : https://raw.githubusercontent.com/PrendsTaPart/Video/claude/foodeatup-video-tutorials-bivyyp/videos/foodeatup-predibot-previsions-tuto/out/foodeatup-predibot-previsions-tuto-v1.mp4\n\n**Description (à quoi ça sert)**\n\nAnticiper vos besoins en stock, en commandes fournisseurs et en production grâce aux prédictions de l'intelligence artificielle PrediBot, pour éviter les ruptures et ne produire que le nécessaire.\n\n**Comment ça marche**\n\n1. Ouvrez Analyse et prédictions depuis le tableau de bord PrediBot pour voir vos indicateurs clés : alertes actives, économies potentielles, précision de l'IA.\n2. Cliquez sur Prédictions de stock pour visualiser votre consommation face à vos niveaux de stock, avec la recommandation de l'IA.\n3. Consultez Prévisions de commandes : PrediBot vous suggère quoi commander, produit par produit, avant la rupture de stock.\n4. Ouvrez Production recommandée pour voir les plats à préparer et les quantités conseillées, selon l'historique de vos ventes.\n\n**Astuce du chef** : Le pourcentage de précision IA et le niveau de confiance du modèle indiquent la fiabilité de chaque prévision : plus votre historique de ventes est riche, plus PrediBot affine ses recommandations semaine après semaine.\n\n---",
              "correspondance": "numéro",
              "confiance": 1.0
            },
            "tutorielModuleUrl": "https://tutoriel.foodeatup.com/module/predibot",
            "higgsfield": {
              "videoSourceUrl": null,
              "duree": "10 s",
              "format": "vertical 9:16",
              "source": null
            },
            "masterRapidoUrl": null
          },
          {
            "id": "EP146",
            "numero": 146,
            "saison": 5,
            "slug": "ep146-quarante-bougies-et-les-sprinklers",
            "titre": "Quarante bougies et les sprinklers",
            "module": "Comptabilité",
            "chapitre": "événements privés",
            "accroche": "Quarante bougies. Une seule mauvaise idée.",
            "punchline": "Les gros événements, ça se prépare en amont.",
            "resume": "Un événement, c'est une demande, un devis, une réservation et une facture. Enchaînés. Rien ne se prépare la veille au soir.",
            "statut": "a_produire",
            "dureeSecondes": null,
            "videoUrl": null,
            "reseaux": {
              "facebook": {
                "statut": "a_venir",
                "date": "2026-12-03",
                "heure": "12:00",
                "compte": "FoodEatUp",
                "format": "Vidéo native 9:16",
                "lienCta": "https://site.foodeatup.com/"
              },
              "instagram": {
                "statut": "a_venir",
                "date": "2026-12-03",
                "heure": "18:30",
                "compte": "foodeatup.cocuisinage",
                "format": "Reel 9:16",
                "lienCta": null
              },
              "tiktok": {
                "statut": "a_venir",
                "date": "2026-12-03",
                "heure": "19:00",
                "compte": "foodeatup",
                "format": "Vidéo 9:16",
                "lienCta": null
              },
              "linkedin": {
                "statut": "a_venir",
                "date": "2026-12-03",
                "heure": "08:00",
                "compte": "FoodEatUp",
                "format": "Vidéo native 9:16",
                "lienCta": "https://site.foodeatup.com/"
              },
              "youtube": {
                "statut": "a_venir",
                "date": "2026-12-03",
                "heure": "10:00",
                "compte": "@FoodEatUp",
                "format": "Short 9:16",
                "lienCta": "https://site.foodeatup.com/"
              }
            },
            "posterUrl": null,
            "datePrevue": "2026-12-03",
            "troisMots": "ÉVÉNEMENTS PRIVÉS",
            "tutoriel": {
              "titre": "Gérer ses clients côté ventes",
              "slug": "gerer-ses-clients-cote-ventes",
              "url": "https://tutoriel.foodeatup.com/tutoriel/gerer-ses-clients-cote-ventes",
              "module": "Comptabilité & Achats",
              "etape": "Fournisseurs & clients\n- **Statut** : En ligne (0 min 42 s)\n- **Vidéo** : https://rapido-software.s3.eu-west-3.amazonaws.com/rapidosoftware/cms/bibliotheque/gerer-ses-clients-cote-ventes-v1\n\n**Description (à quoi ça sert)**\n\nCentraliser tous vos clients côté ventes — identité, coordonnées, adresse et informations de facturation — pour les retrouver en un clic au moment de créer un devis ou une facture, sans ressaisir leurs informations.\n\n**Comment ça marche**\n\n1. Depuis Comptabilité > Clients, retrouvez la liste de vos clients\n2. Cliquez sur \"Ajouter un nouveau client\" et renseignez son identité, ses coordonnées et son adresse (autocomplétion incluse)\n3. En option, complétez sa date de naissance, son genre, sa TVA, son SIRET et son canal d'acquisition\n4. Cliquez sur \"Enregistrer le client\" : il apparaît aussitôt dans la liste\n5. Cliquez sur \"Modifier\" pour ajuster ses informations, puis sur \"Options avancées\" pour l'associer par défaut à vos factures, vos devis, ou à un commercial\n6. Ouvrez sa fiche détaillée en un clic pour retrouver toutes ses informations\n7. Cliquez sur \"Supprimer\" pour retirer un client : une confirmation vous est toujours demandée avant toute suppression définitive\n\n**Astuce du chef** : Chaque fiche client alimente aussi vos devis, vos factures et son compte fidélité, et sert de base à la segmentation RFM (clients fidèles, à risque, occasionnels...) pour cibler vos campagnes marketing. Cette base clients, enrichie automatiquement depuis tous vos canaux de vente (site web, QR code à table, agent vocal), est aussi le socle de vos campagnes marketing : SMS, jeux concours, sondages — de quoi faire revenir vos clients grâce au module Marketing, Fidélité & Iris.\n\n---",
              "correspondance": "texte",
              "confiance": 0.48
            },
            "tutorielModuleUrl": "https://tutoriel.foodeatup.com/module/comptabilite",
            "higgsfield": {
              "videoSourceUrl": null,
              "duree": "10 s",
              "format": "vertical 9:16",
              "source": null
            },
            "masterRapidoUrl": null
          },
          {
            "id": "EP147",
            "numero": 147,
            "saison": 5,
            "slug": "ep147-le-gateau-a-cinq-etages",
            "titre": "Le gâteau à cinq étages",
            "module": "Comptabilité",
            "chapitre": "facture et devis",
            "accroche": "Douze mille euros de prestation.",
            "punchline": "Sur un devis, pas sur un post-it.",
            "resume": "Douze mille euros de prestation ne tiennent pas sur un post-it. Devis signé, acompte suivi, facture éditée : tout est dans le dossier.",
            "statut": "a_produire",
            "dureeSecondes": null,
            "videoUrl": null,
            "reseaux": {
              "facebook": {
                "statut": "a_venir",
                "date": "2026-12-04",
                "heure": "12:00",
                "compte": "FoodEatUp",
                "format": "Vidéo native 9:16",
                "lienCta": "https://site.foodeatup.com/"
              },
              "instagram": {
                "statut": "a_venir",
                "date": "2026-12-04",
                "heure": "18:30",
                "compte": "foodeatup.cocuisinage",
                "format": "Reel 9:16",
                "lienCta": null
              },
              "tiktok": {
                "statut": "a_venir",
                "date": "2026-12-04",
                "heure": "19:00",
                "compte": "foodeatup",
                "format": "Vidéo 9:16",
                "lienCta": null
              },
              "linkedin": {
                "statut": "a_venir",
                "date": "2026-12-04",
                "heure": "08:00",
                "compte": "FoodEatUp",
                "format": "Vidéo native 9:16",
                "lienCta": "https://site.foodeatup.com/"
              },
              "youtube": {
                "statut": "a_venir",
                "date": "2026-12-04",
                "heure": "10:00",
                "compte": "@FoodEatUp",
                "format": "Short 9:16",
                "lienCta": "https://site.foodeatup.com/"
              }
            },
            "posterUrl": null,
            "datePrevue": "2026-12-04",
            "troisMots": "FACTURE ET DEVIS",
            "tutoriel": {
              "titre": "Créer un devis FoodEatUp",
              "slug": "creer-un-devis",
              "url": "https://tutoriel.foodeatup.com/tutoriel/creer-un-devis",
              "module": "Comptabilité & Achats",
              "etape": "Devis\n- **Statut** : En ligne (1 min 06 s)\n- **Vidéo** : https://rapido-software.s3.eu-west-3.amazonaws.com/rapidosoftware/cms/bibliotheque/creer-un-devis-v1\n\n**Description (à quoi ça sert)**\n\nCréer et envoyer un devis professionnel en quelques clics — produits, remise, TVA et acompte calculés automatiquement — pour que votre client puisse le consulter et le signer en ligne sans aller-retour par email.\n\n**Comment ça marche**\n\n1. Depuis l'onglet Devis, retrouvez tous vos devis (brouillons, envoyés, signés) avec leur montant total\n2. Cliquez sur \"Créer un devis\"\n3. Choisissez le client, le délai de paiement, et le mode de règlement\n4. Recherchez un produit ou une recette : son prix et sa TVA se remplissent automatiquement\n5. Ajustez la quantité si besoin, le total se recalcule instantanément\n6. Appliquez une remise globale, une TVA globale, et demandez si besoin un acompte : le solde restant s'affiche automatiquement\n7. Choisissez d'envoyer le devis par email au client (il reçoit un lien sécurisé pour le consulter et le signer) ou de l'enregistrer en brouillon\n8. Cliquez sur \"Enregistrer\" (ou \"Enregistrer & Envoyer\") — le devis apparaît aussitôt dans votre liste\n\n**Astuce du chef** : L'acompte demandé (en pourcentage ou en montant fixe) calcule automatiquement le solde restant : pratique pour sécuriser une commande importante ou un événement avant de le confirmer. Vous pouvez aussi demander directement à Claude de créer un devis à votre place, en lui donnant simplement le client, le produit et le prix.\n\n---",
              "correspondance": "texte",
              "confiance": 0.67
            },
            "tutorielModuleUrl": "https://tutoriel.foodeatup.com/module/comptabilite",
            "higgsfield": {
              "videoSourceUrl": null,
              "duree": "10 s",
              "format": "vertical 9:16",
              "source": null
            },
            "masterRapidoUrl": null
          },
          {
            "id": "EP148",
            "numero": 148,
            "saison": 5,
            "slug": "ep148-le-sumo-de-la-place-de-livraison",
            "titre": "Le sumo de la place de livraison",
            "module": "HubRise",
            "chapitre": "3 - Synchro caisse tierce",
            "accroche": "Trois plateformes. Une place.",
            "punchline": "Centralise les commandes, pas les embouteillages.",
            "resume": "Trois plateformes, une seule file. Les commandes arrivent centralisées, avec leur horaire de retrait. Tes livreurs ne se croisent plus au même moment.",
            "statut": "bloque",
            "dureeSecondes": null,
            "videoUrl": null,
            "reseaux": {
              "facebook": {
                "statut": "a_venir",
                "date": null,
                "heure": "12:00",
                "compte": "FoodEatUp",
                "format": "Vidéo native 9:16",
                "lienCta": "https://site.foodeatup.com/"
              },
              "instagram": {
                "statut": "a_venir",
                "date": null,
                "heure": "18:30",
                "compte": "foodeatup.cocuisinage",
                "format": "Reel 9:16",
                "lienCta": null
              },
              "tiktok": {
                "statut": "a_venir",
                "date": null,
                "heure": "19:00",
                "compte": "foodeatup",
                "format": "Vidéo 9:16",
                "lienCta": null
              },
              "linkedin": {
                "statut": "a_venir",
                "date": null,
                "heure": "08:00",
                "compte": "FoodEatUp",
                "format": "Vidéo native 9:16",
                "lienCta": "https://site.foodeatup.com/"
              },
              "youtube": {
                "statut": "a_venir",
                "date": null,
                "heure": "10:00",
                "compte": "@FoodEatUp",
                "format": "Short 9:16",
                "lienCta": "https://site.foodeatup.com/"
              }
            },
            "blocage": "Le chapitre correspondant n'a pas encore de vidéo dans le Drive interne.",
            "posterUrl": null,
            "datePrevue": null,
            "troisMots": "SYNCHRO CAISSE TIERCE",
            "tutoriel": {
              "titre": "Synchroniser sa caisse tierce via HubRise",
              "slug": "synchroniser-sa-caisse-tierce",
              "url": "https://tutoriel.foodeatup.com/tutoriel/synchroniser-sa-caisse-tierce",
              "module": "HubRise & Livraisons",
              "etape": "Plateformes de livraison\n- **Statut** : Bientôt disponible (tournage en cours)\n\n**Description (à quoi ça sert)**\n\nSynchroniser sa caisse tierce via HubRise — tutoriel en préparation dans le module HubRise & Livraisons. Il arrive très bientôt dans ce fil conducteur.\n\n**Comment ça marche**\n\n1. Cette vidéo est en cours de tournage dans les cuisines FoodEatUp.\n2. Sa fiche est déjà en place : elle se remplira dès la mise en ligne.\n\n---",
              "correspondance": "numéro",
              "confiance": 1.0
            },
            "tutorielModuleUrl": "https://tutoriel.foodeatup.com/module/hubrise-livraisons",
            "higgsfield": {
              "videoSourceUrl": null,
              "duree": "10 s",
              "format": "vertical 9:16",
              "source": null
            },
            "masterRapidoUrl": null
          },
          {
            "id": "EP149",
            "numero": 149,
            "saison": 5,
            "slug": "ep149-le-flash-mob-de-la-salle",
            "titre": "Le flash mob de la salle",
            "module": "Marketing",
            "chapitre": "5 - Lancer une campagne",
            "accroche": "Ta salle a un truc que personne d'autre n'a.",
            "punchline": "Fais-le savoir.",
            "resume": "Ta salle a quelque chose d'unique : fais-le savoir. Campagne créée, segment choisi, résultats mesurés, CA attribué.",
            "statut": "a_produire",
            "dureeSecondes": null,
            "videoUrl": null,
            "reseaux": {
              "facebook": {
                "statut": "a_venir",
                "date": "2026-12-05",
                "heure": "12:00",
                "compte": "FoodEatUp",
                "format": "Vidéo native 9:16",
                "lienCta": "https://site.foodeatup.com/"
              },
              "instagram": {
                "statut": "a_venir",
                "date": "2026-12-05",
                "heure": "18:30",
                "compte": "foodeatup.cocuisinage",
                "format": "Reel 9:16",
                "lienCta": null
              },
              "tiktok": {
                "statut": "a_venir",
                "date": "2026-12-05",
                "heure": "19:00",
                "compte": "foodeatup",
                "format": "Vidéo 9:16",
                "lienCta": null
              },
              "linkedin": {
                "statut": "a_venir",
                "date": "2026-12-05",
                "heure": "08:00",
                "compte": "FoodEatUp",
                "format": "Vidéo native 9:16",
                "lienCta": "https://site.foodeatup.com/"
              },
              "youtube": {
                "statut": "a_venir",
                "date": "2026-12-05",
                "heure": "10:00",
                "compte": "@FoodEatUp",
                "format": "Short 9:16",
                "lienCta": "https://site.foodeatup.com/"
              }
            },
            "posterUrl": null,
            "datePrevue": "2026-12-05",
            "troisMots": "LANCER UNE CAMPAGNE",
            "tutoriel": {
              "titre": "Lancer une campagne marketing",
              "slug": "lancer-une-campagne-marketing",
              "url": "https://tutoriel.foodeatup.com/tutoriel/lancer-une-campagne-marketing",
              "module": "Marketing, Fidélité & Iris",
              "etape": "Pack marketing & campagnes\n- **Statut** : En ligne (0 min 50 s)\n- **Vidéo** : https://rapido-software.s3.eu-west-3.amazonaws.com/rapidosoftware/cms/bibliotheque/foodeatup-campagne-marketing-tuto-v1\n\n**Description (à quoi ça sert)**\n\nToucher le bon segment de clients avec le bon message, sans risquer un envoi non conforme (procédure STOP, fenêtre légale) — coût et portée connus avant même de lancer la campagne.\n\n**Comment ça marche**\n\n1. Depuis l'onglet Campagnes, cliquez sur \"Nouvelle campagne\".\n2. Choisissez votre cible parmi les segments RFM calculés chaque nuit (Tous les clients, Champions, Fidèles, Prometteurs, À risque...).\n3. Nommez la campagne, choisissez son canal (Email, SMS, WhatsApp ou Vocal) et rédigez le message.\n4. Ajoutez votre offre et votre code promo — le lien tracké est généré automatiquement.\n5. Envoyez maintenant ou planifiez, FoodEatUp respecte toujours la fenêtre légale d'envoi.\n6. Vérifiez la conformité (contactables après exclusions STOP, coût estimé), puis lancez.\n\n**Astuce du chef** : Pour une première campagne, ciblez plutôt vos segments \"Champions\" ou \"Fidèles\" que \"Tous les clients\" : moins de contacts, mais un bien meilleur taux de retour, et vous limitez le risque de désabonnements sur toute votre base.\n\n---",
              "correspondance": "numéro",
              "confiance": 1.0
            },
            "tutorielModuleUrl": "https://tutoriel.foodeatup.com/module/marketing-fidelite",
            "higgsfield": {
              "videoSourceUrl": null,
              "duree": "10 s",
              "format": "vertical 9:16",
              "source": null
            },
            "masterRapidoUrl": null
          },
          {
            "id": "EP150",
            "numero": 150,
            "saison": 5,
            "slug": "ep150-le-salut-final",
            "titre": "Le salut final",
            "module": "PrediBot",
            "chapitre": "1 - Lire ses prévisions",
            "accroche": "Cent cinquante épisodes.",
            "punchline": "Une seule promesse : ton restaurant, avant, pendant et après le service.",
            "resume": "Cent cinquante épisodes pour dire une chose : ton restaurant tient dans un seul outil, avant, pendant et après ton service. Le reste, c'est du bruit.",
            "statut": "a_produire",
            "dureeSecondes": null,
            "videoUrl": null,
            "reseaux": {
              "facebook": {
                "statut": "a_venir",
                "date": "2026-12-06",
                "heure": "12:00",
                "compte": "FoodEatUp",
                "format": "Vidéo native 9:16",
                "lienCta": "https://site.foodeatup.com/"
              },
              "instagram": {
                "statut": "a_venir",
                "date": "2026-12-06",
                "heure": "18:30",
                "compte": "foodeatup.cocuisinage",
                "format": "Reel 9:16",
                "lienCta": null
              },
              "tiktok": {
                "statut": "a_venir",
                "date": "2026-12-06",
                "heure": "19:00",
                "compte": "foodeatup",
                "format": "Vidéo 9:16",
                "lienCta": null
              },
              "linkedin": {
                "statut": "a_venir",
                "date": "2026-12-06",
                "heure": "08:00",
                "compte": "FoodEatUp",
                "format": "Vidéo native 9:16",
                "lienCta": "https://site.foodeatup.com/"
              },
              "youtube": {
                "statut": "a_venir",
                "date": "2026-12-06",
                "heure": "10:00",
                "compte": "@FoodEatUp",
                "format": "Short 9:16",
                "lienCta": "https://site.foodeatup.com/"
              }
            },
            "posterUrl": null,
            "datePrevue": "2026-12-06",
            "troisMots": "LIRE SES PRÉVISIONS",
            "tutoriel": {
              "titre": "Lire ses prévisions PrediBot",
              "slug": "lire-ses-previsions-predibot",
              "url": "https://tutoriel.foodeatup.com/tutoriel/lire-ses-previsions-predibot",
              "module": "PrediBot (Agent IA Directeur)",
              "etape": "Prévisions\n- **Statut** : En ligne (0 min 42 s)\n- **Vidéo** : https://raw.githubusercontent.com/PrendsTaPart/Video/claude/foodeatup-video-tutorials-bivyyp/videos/foodeatup-predibot-previsions-tuto/out/foodeatup-predibot-previsions-tuto-v1.mp4\n\n**Description (à quoi ça sert)**\n\nAnticiper vos besoins en stock, en commandes fournisseurs et en production grâce aux prédictions de l'intelligence artificielle PrediBot, pour éviter les ruptures et ne produire que le nécessaire.\n\n**Comment ça marche**\n\n1. Ouvrez Analyse et prédictions depuis le tableau de bord PrediBot pour voir vos indicateurs clés : alertes actives, économies potentielles, précision de l'IA.\n2. Cliquez sur Prédictions de stock pour visualiser votre consommation face à vos niveaux de stock, avec la recommandation de l'IA.\n3. Consultez Prévisions de commandes : PrediBot vous suggère quoi commander, produit par produit, avant la rupture de stock.\n4. Ouvrez Production recommandée pour voir les plats à préparer et les quantités conseillées, selon l'historique de vos ventes.\n\n**Astuce du chef** : Le pourcentage de précision IA et le niveau de confiance du modèle indiquent la fiabilité de chaque prévision : plus votre historique de ventes est riche, plus PrediBot affine ses recommandations semaine après semaine.\n\n---",
              "correspondance": "numéro",
              "confiance": 1.0
            },
            "tutorielModuleUrl": "https://tutoriel.foodeatup.com/module/predibot",
            "higgsfield": {
              "videoSourceUrl": null,
              "duree": "10 s",
              "format": "vertical 9:16",
              "source": null
            },
            "masterRapidoUrl": null
          }
        ]
      }
    ]
  }
];

// Les sélecteurs vivent dans `@/lib/series`, pas ici : ce fichier est généré,
// et tout ce qu'on y ajoute à la main disparaît à la régénération suivante.
