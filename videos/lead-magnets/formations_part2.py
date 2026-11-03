from formations_part1 import F, T, add

add(episode=6, slug='une-ecole-pour-ses-agents-ia', titre="Créer une école pour former ses agents IA",
 promesse="Parcours, missions, quiz, mémoire et routines mesurées : la méthode pour que Claude connaisse vos métiers.",
 pour_qui="Dirigeants qui veulent des agents fiables, pas des chatbots.",
 offre='planit', outils=T('claude','academie','planit'),
 etapes=[
  ("Écrire les missions métier", "Une mission décrit une procédure réelle. Exemple : F3 « Stocks et commandes fournisseurs » avec la règle « préparer, montrer, attendre l'accord ».", "Transforme cette procédure [procédure] en mission de formation : objectif, étapes, outils autorisés, règle d'accord humain, 3 questions de quiz."),
  ("Connecter l'Académie à Claude par MCP", "Claude consulte les formations, récupère les procédures et les applique à ses missions.", None),
  ("Ajouter une mémoire validée", "Préférences, objectifs, corrections : ces notes sont réinjectées dans le contexte, le modèle n'est pas réentraîné. Le savoir d'équipe est validé par un responsable.", None),
  ("Préparer des agents spécialisés", "Commercial, marketing, gestion, formation, pilotage : chaque agent a un rôle, des outils autorisés et des objectifs.", None),
  ("Mesurer les routines", "Objectif, indicateur, critère d'arrêt. V0 → V1 après 3 exécutions ; V1 → V2 avec un KPI et 14 jours de mesures. Verdict : gardée, ajustée ou arrêtée.", "Vérifie ma routine : a-t-elle un objectif, des sources, une limite, un rendu, un critère d'arrêt et un accord humain ? Note-la sur 6 et corrige-la."),
 ],
 garde_fous=["Toute écriture demande une confirmation explicite.", "Une routine ne tourne seule qu'avec un orchestrateur réellement configuré."],
 etat_reel="Audit en lecture seule : 191 outils MCP ; 6 agents tous « à configurer » ; 20 routines toutes en V0 ; 0 KPI suivi au moment de l'épisode.")

add(episode=7, slug='lovable-claude-developper-ses-mcp', titre="Connecter Lovable à Claude pour développer ses MCP",
 promesse="Retrouver ses projets, lire le code, analyser l'historique et tester ses serveurs MCP depuis Claude.",
 pour_qui="Créateurs d'applications Lovable qui veulent les rendre utilisables par des agents.",
 offre='plugins', outils=T('claude_code','lovable','plugins','supabase'),
 etapes=[
  ("Connecter Lovable à Claude", "Le connecteur Lovable permet de lister ses projets, lire les fichiers, parcourir l'historique, comparer des versions et envoyer des instructions à l'agent Lovable.", "Liste mes projets Lovable et retrouve [projet]. Consulte son architecture et explique comment son MCP est organisé. Ne modifie rien."),
  ("Partir du besoin métier", "Ce que l'agent doit pouvoir faire, puis les données nécessaires, puis les outils.", "Analyse ce projet Lovable. Propose les outils MCP nécessaires pour permettre à Claude de consulter les données métier, avec les bons droits d'accès et des réponses structurées."),
  ("Un fichier par outil", "Chaque outil a un nom, une description, des paramètres typés (Zod) et des annotations (lecture seule, idempotent).", None),
  ("Verrouiller les permissions", "OAuth, jeton de l'utilisateur transmis à la base pour que les règles RLS s'appliquent ; vérification d'authentification sur chaque outil d'écriture.", None),
  ("Tester en lecture et en refus", "Un appel en lecture doit renvoyer les vraies données ; le même serveur appelé sans jeton doit refuser (HTTP 401).", None),
  ("Distinguer deux connexions", "A : développer (moi → Claude Code → connecteur Lovable → projet). B : travailler (Claude → MCP métier → application → données autorisées).", None),
 ],
 garde_fous=["Ne jamais afficher le fichier .env ni une clé.", "Toute modification du projet attend une autorisation explicite."],
 etat_reel="BraindCode Plugins expose 58 outils MCP (41 en lecture, 17 en écriture), protégés par OAuth. Test réel : lecture OK, refus 401 sans jeton.")

add(episode=8, slug='piloter-equipes-et-agents-avec-rapidorh', titre="Piloter projets, équipes et agents IA depuis un seul outil",
 promesse="Centraliser projets, tâches, rôles et départements, puis laisser Claude préparer le plan du jour.",
 pour_qui="Dirigeants de PME et chefs de projet.",
 offre='rh', outils=T('claude','rh'),
 etapes=[
  ("Structurer les projets", "Chaque projet a un responsable, une équipe, des dates, un statut et des tâches priorisées (Urgent, Moyenne, Faible) en Kanban.", None),
  ("Organiser rôles et départements", "Des rôles et des permissions pour que chacun accède seulement à ce dont il a besoin.", None),
  ("Connecter RapidoRH à Claude", "Le MCP RapidoRH expose la lecture des projets et des tâches.", "Analyse mes projets en cours, liste les tâches urgentes et celles en retard, et prépare le plan de la journée par personne."),
  ("Prévisualiser avant d'écrire", "La création de tâche est montrée en aperçu, puis exécutée seulement après accord.", None),
  ("Ajouter un orchestrateur pour les routines", "RapidoRH n'a pas de planificateur : une routine quotidienne passe par Claude Code, Plan'It ou n8n.", None),
 ],
 garde_fous=["Ne jamais lire salaires ou données privées sans nécessité.", "Créations et modifications après accord."],
 etat_reel="Démonstration sur le code réel lancé en local avec un jeu de démo fictif ; 24 outils MCP exposés. RapidoRH n'est pas un orchestrateur autonome.")

add(episode=9, slug='application-client-connectee', titre="Livrer une application client connectée à son écosystème",
 promesse="De 161 pages de classeur papier à une application tactile au comptoir, connectée aux données métier.",
 pour_qui="Agences et freelances qui vendent des applications sur mesure.",
 offre='braindcode', outils=T('lovable','claude_code','figma','foodeatup'),
 etapes=[
  ("Cadrer à partir du support existant", "Recettes, formation, allergènes : inventorier le contenu réel avant de dessiner.", None),
  ("Construire l'application avec Lovable", "Catégories, recherche instantanée, fiches, allergènes, mode pas à pas, mode rush lisible à 1 m.", "Crée une application tablette de fiches recettes : catégories, recherche tolérante, fiche (ingrédients, quantités, allergènes), mode pas à pas, mode rush."),
  ("Connecter les données métier", "Les recettes viennent du logiciel métier par MCP (lecture), sans exposer prix ni coûts.", None),
  ("Générer les documents depuis un modèle Figma", "Fiches PDF équipe produites dans le navigateur, au design de la maquette Figma.", None),
  ("Tester avec un banc de test", "Données simulées, tests de bout en bout : aucune donnée de production touchée.", None),
 ],
 garde_fous=["Ne pas montrer la marque d'un client sans son accord.", "Ne jamais réutiliser des identifiants trouvés dans un historique."],
 etat_reel="Projet client facturé 2 000 € ; le client n'est pas nommé (nom de démonstration « PEMA Coffee Shop »). Démo sur l'application réelle lancée en local avec son banc de test.")

add(episode=10, slug='automatiser-ses-chaines-youtube', titre="Automatiser plusieurs chaînes YouTube avec ses agents IA",
 promesse="Centraliser vidéos, métadonnées, calendrier et statistiques, puis laisser l'IA proposer les créneaux.",
 pour_qui="Marques et créateurs qui gèrent plusieurs chaînes.",
 offre='cms', outils=T('publisher','claude','lovable'),
 etapes=[
  ("Centraliser les chaînes", "Une seule interface pour les vidéos, titres, descriptions, historique et calendrier.", None),
  ("Connecter le MCP YouTube", "Les agents consultent les chaînes, récupèrent les vidéos et préparent les actions depuis Claude.", "Liste mes chaînes YouTube et mes 10 dernières vidéos, puis propose 3 titres plus clairs pour la moins vue, sans rien modifier."),
  ("Programmer intelligemment", "L'autopilote propose des créneaux à partir de l'historique de la chaîne.", None),
  ("Exploiter les statistiques", "Vues, interactions, performances : en tirer les prochaines décisions.", None),
  ("Vérifier les quotas avant d'agir", "Un envoi consomme une part importante du quota quotidien de l'API YouTube.", None),
 ],
 garde_fous=["Aucune publication ni suppression sans accord.", "Ne pas confondre vidéos d'une galerie et total publié."],
 etat_reel="Le MCP public comptait 86 outils. Aucun outil d'écriture n'a été appelé pendant l'audit.")

add(episode=11, slug='un-an-de-videos-en-deux-jours', titre="Planifier un an de vidéos avec l'IA",
 promesse="Écrire un catalogue d'épisodes (titre, accroche, punchline) puis organiser leur production.",
 pour_qui="Créateurs et marques qui veulent publier chaque jour.",
 offre='cms', outils=T('claude','lovable','elevenlabs','cms'),
 etapes=[
  ("Définir les séries", "Quelques séries avec chacune une promesse et un public.", None),
  ("Écrire le catalogue", "Pour chaque épisode : titre, accroche, punchline.", "Écris 30 épisodes pour la série [nom] : titre, accroche de 8 mots, punchline, et le message à retenir."),
  ("Organiser les étapes de production", "Scénario, images, voix, montage : chaque étape a un statut (à produire, monté, bloqué).", None),
  ("Suivre l'avancement honnêtement", "« Posé au catalogue » n'est pas « produit ». Comptez les épisodes montés.", None),
  ("Garder le temps pour décider", "Le plus long n'est plus de produire : c'est de choisir quoi raconter.", None),
 ],
 garde_fous=["Ne pas annoncer comme produit ce qui n'est qu'écrit."],
 etat_reel="Relevé du projet : 367 épisodes au catalogue (5 séries), 156 montés, 184 à produire, 27 bloqués. La durée « deux jours » vient du récit de Michael.")

add(episode=12, slug='bd-et-documentation-avec-figma-et-claude', titre="Produire une BD et une documentation logicielle avec Figma et Claude",
 promesse="Connecter Figma à Claude pour construire des planches et un guide utilisateur dans un même fichier.",
 pour_qui="Éditeurs de logiciels, formateurs, équipes marketing.",
 offre='cms', outils=T('claude','figma','cms'),
 etapes=[
  ("Connecter Figma et la bibliothèque d'images", "Claude récupère les images autorisées et travaille directement dans le fichier.", None),
  ("Scénariser la BD", "Personnages, planches, cases : l'histoire au service du message.", "Écris le scénario d'une BD de 12 planches qui explique [logiciel] à un nouvel employé : personnages, planche par planche, texte des bulles."),
  ("Documenter les écrans du logiciel", "Prendre une commande, encaisser, clôturer : écran, explication, illustration.", "Rédige la page de documentation de l'écran [écran] : but, étapes numérotées, erreurs fréquentes, astuce."),
  ("Assembler dans Figma", "Pages A4, gabarits, atlas des écrans, catalogue de prompts.", None),
  ("Écarter ce qui n'est pas autorisé", "Images d'un client sans accord : retirées.", None),
 ],
 garde_fous=["Ne pas réutiliser des images de clients sans accord."],
 etat_reel="Fichier Figma réel : 206 pages A4, dont 88 pages de BD « La Brigade augmentée ».")

add(episode=13, slug='construire-avec-braindcode-build', titre="Construire son application avec la méthode BraindCode Build",
 promesse="Choisir une idée, récupérer cahier des charges, prompts et outils MCP, puis avancer étape par étape avec Claude Code.",
 pour_qui="Développeurs, freelances, étudiants et porteurs de projet.",
 offre='build', outils=T('build','claude_code','lovable','figma'),
 etapes=[
  ("Choisir une idée dans le catalogue", "100 idées d'extensions autour des logiciels Rapido et FoodEatUp.", None),
  ("Récupérer le contexte du projet", "Cahier des charges, charte, connexions MCP, prompts Lovable, Figma et Claude Code.", None),
  ("Suivre le plan d'exécution", "Étape par étape : démarrer une étape, exécuter le prompt dans Lovable, valider l'étape.", None),
  ("Demander une validation humaine", "Connexion OAuth, clés de paiement, mise en ligne : un humain fait la manipulation.", None),
  ("Publier et présenter", "Vérifier que le projet est prêt avant de le rendre public, puis le présenter au demoday.", None),
 ],
 garde_fous=["Aucun secret ne transite par les outils.", "Une idée « à construire » n'est pas une application terminée."],
 etat_reel="Catalogue de 100 idées ; les 5 idées vedettes étaient au statut « à construire » au moment de l'épisode.")

add(episode=14, slug='controle-qualite-de-ses-mcp', titre="Tester ses MCP et ses logiciels avec une boucle de contrôle qualité",
 promesse="Scénarios automatisés, preuves, tickets et prompts de débogage : la boucle qui traque les bugs.",
 pour_qui="Équipes produit et développeurs qui livrent avec l'IA.",
 offre='braindcode', outils=T('claude_code','lovable'),
 etapes=[
  ("Écrire des scénarios", "Un scénario appelle un outil MCP ou une API et compare la réponse au résultat attendu : code, valeur JSON, texte.", "Écris 10 scénarios de test pour l'outil MCP [outil] : entrée, résultat attendu, cas d'erreur."),
  ("Garder les preuves", "Chaque exécution conserve la requête et la réponse.", None),
  ("Ouvrir un ticket avec un prompt de débogage", "Un test en échec devient un ticket avec ses preuves et un prompt pour Claude Code.", "Voici un test en échec et ses preuves : [preuves]. Trouve la cause, corrige sur une branche, ajoute un test qui reproduit le bug."),
  ("Rejouer jusqu'au vert", "Les tests repartent après correction : tant que ça ne passe pas, la boucle continue.", None),
  ("Valider avant la production", "La mise en production reste une décision humaine.", None),
 ],
 garde_fous=["Validation humaine avant chaque mise en production."],
 etat_reel="Dans le code : scénarios, preuves, tickets et 64 outils MCP ; 20 tests MCP isolés réussis. La génération automatique du prompt de débogage et la relance automatique sont des objectifs, pas encore vérifiés.")

add(episode=15, slug='piloter-son-crm-depuis-claude', titre="Piloter son CRM depuis Claude",
 promesse="Demander à Claude qui rappeler, quels devis suivre et quelles factures relancer, puis préparer les actions.",
 pour_qui="Indépendants, TPE et équipes commerciales.",
 offre='crm', outils=T('claude','crm'),
 etapes=[
  ("Connecter RapidoCRM par MCP", "Claude lit le pipeline, les rendez-vous, les devis et les factures.", None),
  ("Faire le point du matin", "Indicateurs, pipeline, agenda du jour.", "Fais mon point du matin dans RapidoCRM : prospects par étape, rendez-vous de la semaine, devis en attente, factures à suivre."),
  ("Distinguer le réel des tests", "Exclure les entrées de test avant de lire les chiffres.", None),
  ("Préparer les relances en brouillon", "Montants et dates vérifiés, rien n'est envoyé sans accord.", "Prépare en brouillon la relance du devis [n°] avec montant et date vérifiés. Ne l'envoie pas."),
  ("Prospecter par segment", "Segments métiers, recherche d'entreprises, ajout au pipeline après validation.", None),
 ],
 garde_fous=["Rien n'est envoyé sans accord.", "Masquer les noms clients dans toute capture."],
 etat_reel="Lecture seule : 70 prospects (69 nouveaux, 1 en qualification), 1 devis réel en attente, 2 factures réelles en attente, entrées de test exclues.")
