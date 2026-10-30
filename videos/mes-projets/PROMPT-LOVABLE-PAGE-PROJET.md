Nouvelle fonctionnalité : une vraie page d'atterrissage pour chaque projet, sur /projets/<slug>.

Objectif : quelqu'un qui clique sur « Voir le projet » sous une vidéo arrive sur une page qui lui explique le projet en 30 secondes, lui montre comment ça marche, et lui donne une action claire. La page reprend la charte du projet (couleurs, polices, ton) et ses images de la médiathèque. Aucun texte, chiffre, prix ou avis ne doit être inventé : une section vide ne s'affiche pas.

1. Structure de la page (dans cet ordre, sur mobile d'abord)
- **Haut de page** : logo du projet, hook en gros (champ hook), punchline (champ punchline), couverture 1280×720 ou la vidéo « Mes projets » du projet en lecture (miniature cliquable, short en vertical sur mobile), bouton principal (CTA n°1) et bouton secondaire.
- **À quoi ça sert** : 3 à 6 bénéfices courts, chacun avec une icône (lucide) et une phrase.
- **Comment ça marche** : 3 à 5 étapes numérotées (titre + phrase + image réelle optionnelle prise dans les assets du projet).
- **Comment l'utiliser** : le pas à pas pour démarrer (étapes, lien vers l'académie ou le tutoriel si le projet a un lien « academie »), et les vidéos du projet (épisodes « Mes projets » et épisodes du quotidien liés).
- **Ressources du projet** : les webinaires, lead magnets et formations liés au projet, sous forme de cartes (visuel, titre, une phrase, bouton). Lead magnet : formulaire prénom + email avec consentement explicite, comme les lead magnets existants. Webinaire : date, heure, bouton « Je m'inscris » (ou « Revoir le replay » une fois passé).
- **Les écrans** : galerie des captures réelles rattachées au projet.
- **FAQ** : questions et réponses du projet (si renseignées).
- **Dernier appel** : rappel du hook + CTA n°1.
- **Pied de page** : réseaux sociaux du projet avec leurs icônes officielles (site, application, académie, Facebook, Instagram, TikTok, LinkedIn, YouTube, X, WhatsApp…), pris dans les liens du projet ; si un réseau manque, l'icône ne s'affiche pas.
- Barre CTA collante en bas sur mobile (CTA n°1).

2. Les CTA du projet
- Un projet a une liste ordonnée de CTA : libellé, URL, type (voir_le_projet, essai_gratuit, demander_une_demo, telecharger_android, telecharger_ios, prendre_rendez_vous, webinaire, lead_magnet, contact, autre) et une indication principal/secondaire.
- Par défaut, sans CTA renseigné : CTA n°1 = « Voir le projet » vers l'URL du projet.
- Chaque clic de CTA est compté dans les statistiques (par projet, par CTA, avec la source : vidéo, short, email, page série).

3. Données (tout est rattaché au projet par projet_slug)
- Champs du projet : hook, punchline (déjà demandés), benefices[], etapes_fonctionnement[], etapes_utilisation[], faq[], ctas[], liens réseaux (existe déjà, ajouter les types manquants : x, whatsapp, android, ios).
- Webinaires : nouvelle table si elle n'existe pas (titre, description, date et heure, durée, lien d'inscription ou formulaire interne, replay_url, visuel, statut brouillon/publié, projet_slug). Les inscriptions vont dans les leads avec la source « webinaire ».
- Lead magnets et formations : ajouter projet_slug pour les rattacher à un projet (un élément peut rester sans projet).
- La page projet a un statut brouillon/publiée indépendant du projet : les nouvelles sections ne s'affichent qu'une fois la page publiée explicitement.

4. Référencement et partage
- Titre et description de la page = nom + punchline ; image de partage = couverture 1200×630 du projet ; données structurées (SoftwareApplication) sans prix inventé.
- Lien canonique /projets/<slug>. Les vidéos de la série renvoient vers cette page.

5. Admin
- Dans l'admin d'un projet, un onglet « Page » : édition de chaque section (bénéfices, étapes, utilisation, FAQ, CTA, réseaux), choix des images parmi les assets du projet, ressources liées (cocher les webinaires, lead magnets, formations), aperçu mobile/ordinateur, bouton « Publier la page ».
- Un onglet « Webinaires » dans l'admin pour créer et suivre les webinaires et leurs inscrits.

6. MCP (pour que Claude remplisse et mette à jour les pages)
- obtenir_page_projet(slug) : toute la page (sections, CTA, réseaux, ressources liées, statut).
- modifier_page_projet(slug, hook?, punchline?, benefices?, etapes_fonctionnement?, etapes_utilisation?, faq?, ctas?) : remplace les sections fournies, laisse les autres.
- modifier_reseaux_projet(slug, liens[]) : liens et réseaux avec leur type (icône automatique).
- lier_ressource_projet(slug, type: webinaire|lead_magnet|formation, identifiant) et delier_ressource_projet(...).
- creer_webinaire(projet_slug, titre, description, date_heure, duree, lien_inscription?, visuel_cle?), modifier_webinaire, lister_webinaires(projet_slug?), publier_webinaire.
- creer_lead_magnet et creer_formation acceptent projet_slug.
- publier_page_projet(slug) : la publication reste un geste explicite.
- statistiques_projet(slug) : vues de la page et clics par CTA et par source.
- Tout ce qui est créé par MCP naît en brouillon. Rien n'est publié ni envoyé sans accord explicite.

7. Vérification
- Construis la page de foodeatup-fidelite et de qa-hub avec les données existantes (description, liens, vidéo, assets) et laisse les sections sans contenu masquées : je remplirai le contenu par MCP.
- Contrôle à 375 px et 1440 px : lisible, CTA visible sans défiler sur mobile, icônes des réseaux justes, aucune section vide affichée.
- Ne publie et n'envoie rien. Rappelle-moi de republier le site à la fin, et liste les nouveaux outils MCP avec leurs paramètres.
