Chaque projet du Journal doit devenir une source complète d'assets réutilisables pour les prochains épisodes vidéo (TikTok, Reels, Shorts, LinkedIn, YouTube). Trois chantiers + une règle.

Contexte déjà fait via le MCP : hook, punchline, charte (couleurs, polices, thème), logo officiel, bénéfices, étapes et FAQ (texte réel des sites) sont renseignés pour les projets. Je viens de capturer les écrans réels de 41 projets (ordinateur 1440x900 et mobile 780x1688, JPG). Ils sont ici, un fichier par projet et par format :
https://raw.githubusercontent.com/PrendsTaPart/Video/0a0d558316ecde27ace4816874a86afefc8cbe52/videos/_journal-63-72/commun/ecrans-projets/<slug>-desktop.jpg et …/<slug>-mobile.jpg
Slugs concernés : alto, application-haccp, braincast, braindcode, braindcode-build, braindcode-plugins, citycar, coach-cuisine, devisbati, fiche-technique-foodeatup, foodeatup-app, foodeatup-borne-drive, foodeatup-caisse-mobile, foodeatup-fidelite, foodeatup-kds, foodeatup-laboratoire, foodeatup-menu-digital, foodeatup-recettes, foodeatup-social, la-chaine-fraternelles, luks-recettes, mon-academie, plan-it, planit-academie, plateforme-assurance, publisher-bot, qa-hub, rapidocrm, rapidocrm-terrain, rapidoin, rapidomeet, rapidorh, rapidosoftware, rapidotuto, releasesync, restaurant-360, salle-live, tutoriels-foodeatup, villa-beach, voyagego, webinaire-rapidocms.
(Pas d'écran exploitable pour foodeatup, rapidocms, studio-print-foodeatup, foodeatup-carte-digitale : leurs sites renvoient une page blanche au robot ; formation-entrepreneurs est une chaîne YouTube.)

1. Importer les écrans (en une passe, côté serveur)
- Pour chaque slug : copie les 2 fichiers dans le stockage du site, crée les assets du projet en catégorie « ecran », actifs, source « Capture réelle de <url du projet> (31/10/2026) », titre « <Nom> — accueil ordinateur » / « — accueil mobile », plus le média correspondant dans la médiathèque (clé ecran-<slug>-desktop / ecran-<slug>-mobile, tags slug + ecran). Pas de doublon si la clé existe déjà.
- Alto a déjà un asset « capture » en brouillon avec la même image : convertis-le au lieu d'en créer un second.
- Une fois tous les écrans importés, recompose une seule fois les 4 couvertures de chaque projet concerné (remplacer=true) et active-les, sauf si l'active est déjà une composition « design couverture » plus récente. Les miniatures des épisodes ne bougent pas.

2. Créer le kit d'assets de chaque projet (sans IA générative pour les écrans ou les personnes)
Pour chaque projet, à partir de son logo officiel, de sa charte et de ses écrans réels, compose et enregistre comme assets du projet (catégories image, icone ou partage, actifs, source « Composition à partir du logo, de la charte et des écrans réels ») :
- Icônes : une icône par bénéfice de la page projet (pictogramme lucide correspondant), aux couleurs de la charte, en PNG transparent 512x512, plus un jeu « fond plein » 512x512 (pastille couleur principale). Clés icone-<slug>-<mot-clé>.
- Logo décliné : sur fond clair, sur fond sombre, en carré 1080x1080 (logo centré sur couleur de fond), en avatar rond 512x512.
- Fonds : dégradé et motif discret de la charte en 1080x1920 et 1920x1080, sans texte (pour les plans de transition).
- Mockups : l'écran ordinateur dans un cadre d'ordinateur portable et l'écran mobile dans un cadre de téléphone, sur fond transparent (PNG), en 1080x1920 et 1920x1080.
- Cartes vidéo : carte titre (hook surligné comme les couvertures), bandeau bas (nom + punchline), carte de fin (CTA n°1 de la page projet + logo + photo d'entrepreneur de Michael en veste), en 1080x1920 et 1920x1080, en PNG transparent quand c'est un calque.
- Étapes illustrées : une carte par étape de « etapes_fonctionnement » (numéro + titre + icône), 1080x1350.
Aucun chiffre, prix, avis ou écran inventé ; si un élément manque (pas de bénéfices, pas d'étapes), saute la pièce et signale-le.

3. Accès MCP au kit
- obtenir_projet renvoie les assets groupés par catégorie (logo, ecran, icone, image, partage, couverture, video) avec leur usage.
- Ajoute lister_kit_projet(projet_slug, categorie?, format?) : liste prête à l'emploi pour un montage (url, dimensions, fond transparent oui/non, usage).
- ajouter_asset_projet accepte la catégorie « ecran » et actif=true pour les captures réelles ; ajoute activer_asset_projet si ce n'est pas encore en ligne.
- ajouter_media accepte projet_slug : le média est alors aussi rattaché aux assets du projet.

4. Règle permanente (dans le code et dans les instructions du serveur MCP)
« Toute nouvelle image, icône, capture d'écran, miniature, couverture ou vidéo liée à un projet est automatiquement ajoutée aux assets de ce projet pour être réutilisée dans d'autres vidéos. » Concrètement :
- creer_video / modifier_video avec projet_slug : la miniature, le short et la vidéo deviennent des assets du projet (catégorie video, usage « épisode N »).
- generer_couvertures_projet, definir_logo_projet, ajouter_media(projet_slug), uploads de l'admin sur une page projet : rattachement automatique.
- verifier_vignettes signale aussi les projets sans écran actif, sans icônes ou sans kit vidéo.

5. Correction d'un effet de bord
Aujourd'hui, chaque modifier_projet ou ajouter_asset_projet recompose les couvertures en brouillon et désactive les couvertures actives : il faut ensuite relancer activer_couverture_projet à la main. Corrige : la recomposition reste en brouillon sans retirer l'active, et ne se déclenche que si le hook, la punchline, le logo ou les écrans ont changé (pas pour la charte seule ou un asset sans rapport). Renvoie un champ « couvertures_a_activer » au lieu de tout l'objet couverture pour alléger les réponses.

6. Vérification
- Lance verifier_vignettes avant/après et donne le nombre d'assets par projet (écrans, icônes, mockups, cartes).
- Montre-moi le kit complet de 3 projets (rapidomeet, foodeatup-caisse-mobile, citycar) sur une page d'aperçu admin.
- Contrôle /projets à 375 px et 1440 px. Ne publie rien d'autre, liste les outils MCP nouveaux ou modifiés avec leurs paramètres, et rappelle-moi de republier le site.
