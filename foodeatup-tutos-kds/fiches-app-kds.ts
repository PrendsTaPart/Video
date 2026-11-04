import type { Tutorial } from "./tutorials";

/**
 * Tutoriels vidéo de l'application « FoodEatUp KDS » (tablette de cuisine).
 *
 * Vidéos montées avec HyperFrames à partir des vrais écrans de l'application
 * (dépôt braindcode1/foodeatup-kitchen-screen, mode démo hors ligne), voix Adam eleven_v4.
 * Sources : dépôt PrendsTaPart/Video, dossier foodeatup-tutos-kds.
 * Fichiers hébergés dans la bibliothèque RapidoCMS ; vignettes : fonds Lovable
 * (public/tutos-kds/fonds) + vrais écrans. Comme fichesAppFidelite, ces fiches
 * s'ajoutent au catalogue en base sans jamais écraser un contenu édité dans l'admin.
 */
export const fichesAppKds: Tutorial[] = [
  {
    slug: "app-kds-appairer-et-regler",
    title: "Appairer la tablette et choisir son poste",
    moduleSlug: "kds-cuisine",
    subcategory: "Application tablette KDS",
    section: "Application tablette KDS",
    order: 100,
    videoUrl:
      "https://rapido-software.s3.eu-west-3.amazonaws.com/rapidosoftware/cms/bibliotheque/foodeatup-app-kds-appairer-et-regler-tuto",
    thumbnailUrl:
      "https://rapido-software.s3.eu-west-3.amazonaws.com/rapidosoftware/cms/bibliotheque/foodeatup-app-kds-appairer-et-regler-vignette",
    durationSeconds: 29,
    howItWorks: [
      "Le code s'affiche dans FoodEatUp › Cuisine (KDS)",
      "Tape les 6 caractères puis Connecter",
      "Choisis le poste de cet écran",
      "Un guide de 4 étapes te prend en main",
    ],
    whatItsFor:
      "Relier une tablette de cuisine à votre établissement avec un code d'appairage à usage unique, puis choisir le poste qu'elle affiche.",
    chefTip:
      "Un code par tablette : il ne sert qu'une fois. Le choix du poste est mémorisé, il se change dans Réglages › Changer de poste.",
    claudePrompts: [
      {
        title: "Appairer la tablette et choisir son poste",
        prompt:
          "Explique-moi appairer la tablette et choisir son poste sur la tablette FoodEatUp KDS de mon établissement (ID [ID établissement]), étape par étape.",
      },
    ],
  },
  {
    slug: "app-kds-rythme-du-service",
    title: "Les envois en attente",
    moduleSlug: "kds-cuisine",
    subcategory: "Application tablette KDS",
    section: "Application tablette KDS",
    order: 101,
    videoUrl:
      "https://rapido-software.s3.eu-west-3.amazonaws.com/rapidosoftware/cms/bibliotheque/foodeatup-app-kds-rythme-du-service-tuto",
    thumbnailUrl:
      "https://rapido-software.s3.eu-west-3.amazonaws.com/rapidosoftware/cms/bibliotheque/foodeatup-app-kds-rythme-du-service-vignette",
    durationSeconds: 23,
    howItWorks: [
      "Les plats d'un envoi suivant restent EN ATTENTE",
      "Ils sont grisés : on ne les lance pas trop tôt",
      "Lancer l'envoi quand la salle le demande",
      "Le pass sert la table au bon moment",
    ],
    whatItsFor:
      "Garder en attente les plats des envois suivants pour qu'ils ne partent pas trop tôt, et les lancer quand la salle est prête.",
    chefTip:
      "Un plat grisé « EN ATTENTE » n'est pas oublié : il attend son envoi. Lancez-le depuis le ticket au bon moment.",
    claudePrompts: [
      {
        title: "Les envois en attente",
        prompt:
          "Explique-moi les envois en attente sur la tablette FoodEatUp KDS de mon établissement (ID [ID établissement]), étape par étape.",
      },
    ],
  },
  {
    slug: "app-kds-gestes-du-poste",
    title: "Les trois gestes du poste",
    moduleSlug: "kds-cuisine",
    subcategory: "Application tablette KDS",
    section: "Application tablette KDS",
    order: 102,
    videoUrl:
      "https://rapido-software.s3.eu-west-3.amazonaws.com/rapidosoftware/cms/bibliotheque/foodeatup-app-kds-gestes-du-poste-tuto",
    thumbnailUrl:
      "https://rapido-software.s3.eu-west-3.amazonaws.com/rapidosoftware/cms/bibliotheque/foodeatup-app-kds-gestes-du-poste-vignette",
    durationSeconds: 22,
    howItWorks: [
      "Toucher un plat : en cours, puis prêt",
      "Appui long : le plat recule d'un statut",
      "BUMP : tout le ticket part au pass",
      "De gros boutons, utilisables avec des gants",
    ],
    whatItsFor:
      "Connaître les trois gestes du poste : toucher pour avancer, appui long pour reculer, BUMP pour envoyer tout le ticket au pass.",
    chefTip:
      "Un appui long rattrape une erreur sans rien casser : le plat recule d'un seul statut.",
    claudePrompts: [
      {
        title: "Les trois gestes du poste",
        prompt:
          "Explique-moi les trois gestes du poste sur la tablette FoodEatUp KDS de mon établissement (ID [ID établissement]), étape par étape.",
      },
    ],
  },
  {
    slug: "app-kds-ticket-en-grand",
    title: "Ouvrir un ticket en grand",
    moduleSlug: "kds-cuisine",
    subcategory: "Application tablette KDS",
    section: "Application tablette KDS",
    order: 103,
    videoUrl:
      "https://rapido-software.s3.eu-west-3.amazonaws.com/rapidosoftware/cms/bibliotheque/foodeatup-app-kds-ticket-en-grand-tuto",
    thumbnailUrl:
      "https://rapido-software.s3.eu-west-3.amazonaws.com/rapidosoftware/cms/bibliotheque/foodeatup-app-kds-ticket-en-grand-vignette",
    durationSeconds: 23,
    howItWorks: [
      "Touche l'en-tête du ticket",
      "Le ticket s'ouvre en grand avec son minuteur",
      "Les allergènes restent écrits en rouge",
      "BUMP · tout prêt, puis retour au poste",
    ],
    whatItsFor:
      "Ouvrir un ticket en plein écran pour suivre chaque plat, son minuteur et ses allergènes, puis le terminer d'un BUMP.",
    chefTip:
      "Le minuteur passe à l'orange après le seuil réglé pour le poste : gardez un œil dessus pendant le coup de feu.",
    claudePrompts: [
      {
        title: "Ouvrir un ticket en grand",
        prompt:
          "Explique-moi ouvrir un ticket en grand sur la tablette FoodEatUp KDS de mon établissement (ID [ID établissement]), étape par étape.",
      },
    ],
  },
  {
    slug: "app-kds-filtres-et-retards",
    title: "Filtrer par source et voir les retards",
    moduleSlug: "kds-cuisine",
    subcategory: "Application tablette KDS",
    section: "Application tablette KDS",
    order: 104,
    videoUrl:
      "https://rapido-software.s3.eu-west-3.amazonaws.com/rapidosoftware/cms/bibliotheque/foodeatup-app-kds-filtres-et-retards-tuto",
    thumbnailUrl:
      "https://rapido-software.s3.eu-west-3.amazonaws.com/rapidosoftware/cms/bibliotheque/foodeatup-app-kds-filtres-et-retards-vignette",
    durationSeconds: 26,
    howItWorks: [
      "Toutes sources : caisse, borne, QR table, livraison, à emporter",
      "Le compteur rouge annonce les tickets en retard",
      "Vert, orange puis rouge selon le minuteur",
      "Seuils réglés dans les réglages du poste",
    ],
    whatItsFor:
      "Filtrer les tickets par source (caisse, borne, QR table, livraison, à emporter) et repérer immédiatement les tickets en retard.",
    chefTip:
      "Les seuils vert, orange et rouge se règlent par poste dans les réglages : adaptez-les au temps réel de vos préparations.",
    claudePrompts: [
      {
        title: "Filtrer par source et voir les retards",
        prompt:
          "Explique-moi filtrer par source et voir les retards sur la tablette FoodEatUp KDS de mon établissement (ID [ID établissement]), étape par étape.",
      },
    ],
  },
  {
    slug: "app-kds-vue-production",
    title: "La vue production pour cuisiner en série",
    moduleSlug: "kds-cuisine",
    subcategory: "Application tablette KDS",
    section: "Application tablette KDS",
    order: 105,
    videoUrl:
      "https://rapido-software.s3.eu-west-3.amazonaws.com/rapidosoftware/cms/bibliotheque/foodeatup-app-kds-vue-production-tuto",
    thumbnailUrl:
      "https://rapido-software.s3.eu-west-3.amazonaws.com/rapidosoftware/cms/bibliotheque/foodeatup-app-kds-vue-production-vignette",
    durationSeconds: 20,
    howItWorks: [
      "Touche l'icône liste en haut de l'écran",
      "Le compte par plat, toutes commandes confondues",
      "Prépare en série au lieu de ticket par ticket",
      "Vue tickets pour revenir",
    ],
    whatItsFor:
      "Voir le compte de chaque plat, toutes commandes confondues, pour préparer en série au lieu de ticket par ticket.",
    chefTip:
      "Lancez les préparations longues depuis la vue production, puis revenez aux tickets pour bumper.",
    claudePrompts: [
      {
        title: "La vue production pour cuisiner en série",
        prompt:
          "Explique-moi la vue production pour cuisiner en série sur la tablette FoodEatUp KDS de mon établissement (ID [ID établissement]), étape par étape.",
      },
    ],
  },
  {
    slug: "app-kds-rappeler-un-ticket",
    title: "Rappeler un ticket bumpé par erreur",
    moduleSlug: "kds-cuisine",
    subcategory: "Application tablette KDS",
    section: "Application tablette KDS",
    order: 106,
    videoUrl:
      "https://rapido-software.s3.eu-west-3.amazonaws.com/rapidosoftware/cms/bibliotheque/foodeatup-app-kds-rappeler-un-ticket-tuto",
    thumbnailUrl:
      "https://rapido-software.s3.eu-west-3.amazonaws.com/rapidosoftware/cms/bibliotheque/foodeatup-app-kds-rappeler-un-ticket-vignette",
    durationSeconds: 22,
    howItWorks: [
      "Un ticket bumpé trop vite disparaît de l'écran",
      "Touche l'icône historique",
      "Les 5 derniers bumps du poste",
      "Rappeler : le ticket revient, plats dans leur état d'avant",
    ],
    whatItsFor:
      "Faire revenir à l'écran un ticket bumpé par erreur, avec ses plats dans leur état d'avant.",
    chefTip:
      "L'historique garde les cinq derniers bumps du poste : rappelez vite, avant qu'ils ne soient remplacés.",
    claudePrompts: [
      {
        title: "Rappeler un ticket bumpé par erreur",
        prompt:
          "Explique-moi rappeler un ticket bumpé par erreur sur la tablette FoodEatUp KDS de mon établissement (ID [ID établissement]), étape par étape.",
      },
    ],
  },
  {
    slug: "app-kds-le-pass",
    title: "Le pass : servir une table et appeler un numéro",
    moduleSlug: "kds-cuisine",
    subcategory: "Application tablette KDS",
    section: "Application tablette KDS",
    order: 107,
    videoUrl:
      "https://rapido-software.s3.eu-west-3.amazonaws.com/rapidosoftware/cms/bibliotheque/foodeatup-app-kds-le-pass-tuto",
    thumbnailUrl:
      "https://rapido-software.s3.eu-west-3.amazonaws.com/rapidosoftware/cms/bibliotheque/foodeatup-app-kds-le-pass-vignette",
    durationSeconds: 24,
    howItWorks: [
      "Les tables : servir quand tous les postes sont prêts",
      "La pastille de chaque poste dit où en est la commande",
      "Sans table : Appeler le numéro, puis Remis",
      "Livraison : prévenir le livreur",
    ],
    whatItsFor:
      "Au pass, servir une table quand tous les postes sont prêts, appeler les numéros des commandes sans table et prévenir le livreur.",
    chefTip:
      "Touchez « Remis » quand le client repart : son numéro quitte l'écran d'appel.",
    claudePrompts: [
      {
        title: "Le pass : servir une table et appeler un numéro",
        prompt:
          "Explique-moi le pass : servir une table et appeler un numéro sur la tablette FoodEatUp KDS de mon établissement (ID [ID établissement]), étape par étape.",
      },
    ],
  },
  {
    slug: "app-kds-fiche-recette",
    title: "La fiche recette depuis le ticket",
    moduleSlug: "kds-cuisine",
    subcategory: "Application tablette KDS",
    section: "Application tablette KDS",
    order: 108,
    videoUrl:
      "https://rapido-software.s3.eu-west-3.amazonaws.com/rapidosoftware/cms/bibliotheque/foodeatup-app-kds-fiche-recette-tuto",
    thumbnailUrl:
      "https://rapido-software.s3.eu-west-3.amazonaws.com/rapidosoftware/cms/bibliotheque/foodeatup-app-kds-fiche-recette-vignette",
    durationSeconds: 22,
    howItWorks: [
      "Touche l'icône livre à côté du plat",
      "Ingrédients pour une portion",
      "Les étapes, avec leur durée",
      "Retour au ticket en un geste",
    ],
    whatItsFor:
      "Ouvrir la fiche recette d'un plat depuis le ticket : ingrédients pour une portion, allergènes et étapes avec leur durée.",
    chefTip:
      "Complétez les étapes de vos recettes dans FoodEatUp : elles s'affichent telles quelles en cuisine.",
    claudePrompts: [
      {
        title: "La fiche recette depuis le ticket",
        prompt:
          "Explique-moi la fiche recette depuis le ticket sur la tablette FoodEatUp KDS de mon établissement (ID [ID établissement]), étape par étape.",
      },
    ],
  },
  {
    slug: "app-kds-epuise-du-jour",
    title: "Marquer un plat épuisé depuis la cuisine",
    moduleSlug: "kds-cuisine",
    subcategory: "Application tablette KDS",
    section: "Application tablette KDS",
    order: 109,
    videoUrl:
      "https://rapido-software.s3.eu-west-3.amazonaws.com/rapidosoftware/cms/bibliotheque/foodeatup-app-kds-epuise-du-jour-tuto",
    thumbnailUrl:
      "https://rapido-software.s3.eu-west-3.amazonaws.com/rapidosoftware/cms/bibliotheque/foodeatup-app-kds-epuise-du-jour-vignette",
    durationSeconds: 25,
    howItWorks: [
      "Sur la fiche du plat : Épuisé aujourd'hui",
      "Confirme : il n'est plus vendu nulle part",
      "Caisse, QR, borne et site jusqu'à demain matin",
      "Remettre en vente depuis la vue production",
    ],
    whatItsFor:
      "Déclarer un plat épuisé depuis la cuisine : il n'est plus vendu en caisse, au QR, à la borne ni sur le site jusqu'au lendemain matin.",
    chefTip:
      "Remettez le plat en vente depuis la vue production dès qu'il est de nouveau disponible.",
    claudePrompts: [
      {
        title: "Marquer un plat épuisé depuis la cuisine",
        prompt:
          "Explique-moi marquer un plat épuisé depuis la cuisine sur la tablette FoodEatUp KDS de mon établissement (ID [ID établissement]), étape par étape.",
      },
    ],
  },
  {
    slug: "app-kds-sons-du-poste",
    title: "Régler les sons du poste",
    moduleSlug: "kds-cuisine",
    subcategory: "Application tablette KDS",
    section: "Application tablette KDS",
    order: 110,
    videoUrl:
      "https://rapido-software.s3.eu-west-3.amazonaws.com/rapidosoftware/cms/bibliotheque/foodeatup-app-kds-sons-du-poste-tuto",
    thumbnailUrl:
      "https://rapido-software.s3.eu-west-3.amazonaws.com/rapidosoftware/cms/bibliotheque/foodeatup-app-kds-sons-du-poste-vignette",
    durationSeconds: 26,
    howItWorks: [
      "Réglages › Sons du poste",
      "Un son par événement : nouveau ticket, allergène…",
      "Un profil sonore par poste, volume réglable",
      "Les sons marchent même hors ligne",
    ],
    whatItsFor:
      "Choisir un son par événement et un profil sonore par poste, régler le volume et faire sonner plus fort pendant le coup de feu.",
    chefTip:
      "Les sons sont stockés dans l'application : ils fonctionnent même sans réseau.",
    claudePrompts: [
      {
        title: "Régler les sons du poste",
        prompt:
          "Explique-moi régler les sons du poste sur la tablette FoodEatUp KDS de mon établissement (ID [ID établissement]), étape par étape.",
      },
    ],
  },
  {
    slug: "app-kds-mode-ecole",
    title: "Former un commis avec le mode école",
    moduleSlug: "kds-cuisine",
    subcategory: "Application tablette KDS",
    section: "Application tablette KDS",
    order: 111,
    videoUrl:
      "https://rapido-software.s3.eu-west-3.amazonaws.com/rapidosoftware/cms/bibliotheque/foodeatup-app-kds-mode-ecole-tuto",
    thumbnailUrl:
      "https://rapido-software.s3.eu-west-3.amazonaws.com/rapidosoftware/cms/bibliotheque/foodeatup-app-kds-mode-ecole-vignette",
    durationSeconds: 27,
    howItWorks: [
      "Réglages › Démarrer le mode école",
      "Des tickets d'entraînement avec la vraie carte",
      "Rien n'est envoyé en cuisine ni en caisse",
      "Bumps justes, erreurs, temps moyen et conseils",
    ],
    whatItsFor:
      "Entraîner un commis avec des tickets d'exercice sur la vraie carte, sans rien envoyer en cuisine ni en caisse.",
    chefTip:
      "Regardez les bumps justes, les erreurs et le temps moyen à la fin de l'exercice pour savoir quoi retravailler.",
    claudePrompts: [
      {
        title: "Former un commis avec le mode école",
        prompt:
          "Explique-moi former un commis avec le mode école sur la tablette FoodEatUp KDS de mon établissement (ID [ID établissement]), étape par étape.",
      },
    ],
  },
  {
    slug: "app-kds-vue-du-chef",
    title: "La vue du chef pendant le service",
    moduleSlug: "kds-cuisine",
    subcategory: "Application tablette KDS",
    section: "Application tablette KDS",
    order: 112,
    videoUrl:
      "https://rapido-software.s3.eu-west-3.amazonaws.com/rapidosoftware/cms/bibliotheque/foodeatup-app-kds-vue-du-chef-tuto",
    thumbnailUrl:
      "https://rapido-software.s3.eu-west-3.amazonaws.com/rapidosoftware/cms/bibliotheque/foodeatup-app-kds-vue-du-chef-vignette",
    durationSeconds: 20,
    howItWorks: [
      "Réglages › Vue du chef",
      "Tous les postes, leurs tickets et leurs retards",
      "Le temps moyen de chaque poste",
      "Le temps moyen par plat",
    ],
    whatItsFor:
      "Suivre tout le service d'un coup d'œil : tickets, retards et temps moyen de chaque poste, et temps moyen par plat.",
    chefTip:
      "Allez aider le poste dont le temps moyen grimpe avant qu'il ne prenne du retard.",
    claudePrompts: [
      {
        title: "La vue du chef pendant le service",
        prompt:
          "Explique-moi la vue du chef pendant le service sur la tablette FoodEatUp KDS de mon établissement (ID [ID établissement]), étape par étape.",
      },
    ],
  },
];
