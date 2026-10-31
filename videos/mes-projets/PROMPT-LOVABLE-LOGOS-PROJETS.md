Ajoute la gestion complète des logos de projet dans le MCP du Journal, pour que Claude puisse ajouter, récupérer et appliquer le logo officiel de chaque projet sans passer par l'admin.

Contexte : je viens de renseigner via modifier_projet(logo_url) le logo officiel de 21 projets qui n'en avaient pas (VoyageGo, Villa Beach, Coach Cuisine, Alto, DevisBâti, QA Hub, ReleaseSync, Publisher Bot, RapidoIn, Webinaire RapidoCMS, RapidoMeet, RapidoTuto, CityCar, Plateforme Assurance, Salle Live, BraindCode Plugins, BraindCode Build, Formation entrepreneurs, Mon Académie, Tutoriels FoodEatUp, La Chaîne Fratern'Elles). Ils sont aussi dans la médiathèque (catégorie logo, clé logo-<slug>, tag du slug). Leurs URL pointent vers raw.githubusercontent.com ou michael.foodeatup.fr : elles doivent être hébergées par le site.

1. definir_logo_projet(projet_slug, url, source, variante?)
- Télécharge l'image (png, jpg, webp ou svg, 2 Mo max), la stocke dans le stockage du site (URL stable), met à jour logo_url du projet, crée ou remplace l'asset « logo » du projet en actif et le média logo-<slug> de la médiathèque (même clé, pas de doublon).
- variante facultative : « icone » (carré), « horizontal » (logo + nom), « clair » (pour fond sombre). Les couvertures utilisent en priorité l'horizontal, sinon l'icône.
- source obligatoire (« site officiel », « capture de l'en-tête de … », « bibliothèque de marque »). Refuse une image générée par IA ou sans source.
- Après le changement, recompose les couvertures du projet en brouillon (comme aujourd'hui) et renvoie les URL avant/après.

2. recuperer_logo_projet(projet_slug)
- Visite l'URL du projet et propose des candidats sans rien appliquer : image du logo de l'en-tête (img ou svg dans header, nav ou lien vers « / »), apple-touch-icon et icônes de 180 px ou plus, icône du manifeste, puis og:image en dernier.
- Écarte l'icône par défaut de Lovable (reconnaissable à son empreinte, identique sur les applications non personnalisées) et les logos de partenaires (Google Meet, Teams, Claude…).
- Renvoie pour chaque candidat : url, dimensions, type, emplacement trouvé. Claude choisit ensuite avec definir_logo_projet.

3. Création et contrôle
- creer_projet demande un logo_url ; s'il manque, la réponse propose les candidats de recuperer_logo_projet.
- verifier_vignettes (et lister_projets) signale les projets sans logo, avec un logo non hébergé par le site, ou avec l'icône par défaut de Lovable.
- Ajoute aux instructions du serveur MCP : « Logos : toujours le logo officiel du projet (site, en-tête ou icône de l'application), jamais redessiné ni généré. Pour un nouveau projet : recuperer_logo_projet puis definir_logo_projet. »

4. Affichage
- Le logo apparaît sur la carte du projet (/projets, accueil), en tête de la page projet, dans la tuile blanche des couvertures et sur les pages des épisodes Mes projets. Sans logo, le nom du projet en texte (comme aujourd'hui).

5. À appliquer tout de suite
- Réhéberge les 21 logos renseignés aujourd'hui dans le stockage du site via definir_logo_projet (même image, même source que le média logo-<slug>), puis recompose et active leurs couvertures.
- Les projets dont logo_url est un chemin relatif (/__l5e/…) gardent leur logo mais doivent aussi être enregistrés dans la médiathèque.

6. Vérification
- Lance verifier_vignettes avant/après : plus aucun projet sans logo.
- Teste recuperer_logo_projet sur citycar (doit trouver citycar-logo.png) et sur releasesync (doit écarter l'icône par défaut de Lovable).
- Contrôle /projets et 3 pages projet (rapidomeet, citycar, villa-beach) à 375 px et 1440 px.
- Ne publie rien d'autre, liste les outils MCP nouveaux ou modifiés avec leurs paramètres, et rappelle-moi de republier le site.
