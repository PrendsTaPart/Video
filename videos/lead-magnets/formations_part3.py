from formations_part2 import F, T, add

add(episode=16, slug='former-ses-clients-avec-un-mcp-pedagogique', titre="Former ses clients avec un MCP pédagogique",
 promesse="Connecter ses tutoriels à Claude et ChatGPT : l'IA trouve le bon tutoriel, explique les étapes et propose un quiz.",
 pour_qui="Éditeurs de logiciels et services client.",
 offre='foodeatup', outils=T('tuto_fe','claude','chatgpt'),
 etapes=[
  ("Structurer le catalogue de tutoriels", "Une fiche par geste : titre, durée, étapes, écran concerné.", None),
  ("Exposer le catalogue par MCP, en lecture seule", "Le serveur enseigne, il ne touche jamais aux données du client.", None),
  ("Répondre à une question réelle", "L'IA cherche le bon tutoriel, donne la vidéo (en carte ou en lien selon l'application) et explique les étapes.", "Comment je fais un relevé de température ? Donne-moi le tutoriel, les étapes et un quiz de 3 questions."),
  ("Construire un parcours par métier", "Niveau, thème, temps disponible : une suite de leçons courtes.", "Crée-moi un parcours débutant HACCP de 15 minutes."),
  ("Mesurer les questions sans réponse", "Ce sont les prochains tutoriels à tourner.", None),
 ],
 garde_fous=["Le MCP pédagogique n'agit sur aucun compte.", "Ne jamais inventer une marche à suivre absente du catalogue."],
 etat_reel="173 tutoriels en ligne sur 230 prévus au moment de l'épisode. Le rendu de la carte vidéo dans Claude.ai ou ChatGPT n'a pas été testé.")

add(episode=17, slug='transformer-ses-posts-en-clients', titre="Transformer ses publications en clients : le tunnel RapidoCMS → RapidoCRM",
 promesse="Créer les contenus, capter les demandes avec consentement, suivre les opportunités et boucler sur les résultats.",
 pour_qui="Marketeurs et dirigeants qui publient sans savoir ce que ça rapporte.",
 offre='cms', outils=T('cms','crm','claude'),
 etapes=[
  ("Créer et planifier les contenus", "Visuels, textes et calendrier dans RapidoCMS.", "Prépare 5 publications LinkedIn pour [offre] avec un appel à l'action vers ma démo. Brouillons seulement."),
  ("Capter avec un formulaire", "Un like ne devient pas un client : c'est le formulaire de démo, avec consentement, qui crée le contact.", None),
  ("Suivre dans le CRM", "Demandes, rendez-vous, opportunités dans RapidoCRM.", None),
  ("Analyser et boucler", "Claude compare les performances et prépare la prochaine campagne.", "Compare mes 10 dernières publications : lesquelles ont généré des demandes de démo ? Propose la prochaine campagne."),
 ],
 garde_fous=["Consentement explicite à chaque formulaire.", "Rien n'est publié sans validation."],
 etat_reel="Stratégie construite et outils connectés ; au moment de l'épisode, aucun workflow automatique n'avait encore tourné.")

add(episode=18, slug='diriger-ses-agents-avec-planit', titre="Diriger son équipe d'agents IA avec un orchestrateur",
 promesse="Donner un objectif, laisser l'orchestrateur choisir les outils, transformer en tâches et routines, avec le coût affiché.",
 pour_qui="Dirigeants qui ont plusieurs agents et plusieurs logiciels.",
 offre='planit', outils=T('planit','claude','crm','foodeatup'),
 etapes=[
  ("Formuler un objectif", "Un objectif concret, daté, mesurable.", "Organise ma campagne commerciale FoodEatUp de la semaine."),
  ("Laisser l'orchestrateur choisir les outils", "Il propose les bons MCP : CRM pour les campagnes, logiciel métier pour l'agenda marketing.", None),
  ("Transformer en tâches ou routines", "Avec le coût estimé affiché avant chaque exécution.", None),
  ("Lister les actions sensibles", "Envois, publications et suppressions attendent la validation.", None),
  ("Suivre l'avancement", "Tâches, résultats et historique dans une seule application.", None),
 ],
 garde_fous=["Rien de sensible ne part sans accord.", "Afficher le coût avant d'exécuter."],
 etat_reel="Le compte n'avait aucune routine active au moment de l'épisode : les premières routines étaient en test.")

add(episode=19, slug='site-client-pilote-par-l-ia', titre="Livrer un site client que le client pilote avec l'IA",
 promesse="Un site Lovable relié aux outils métier et un MCP dédié pour que le client modifie son site en parlant à Claude ou ChatGPT.",
 pour_qui="Agences web et freelances.",
 offre='braindcode', outils=T('lovable','claude','foodeatup','crm'),
 etapes=[
  ("Construire le site avec Lovable", "Pages, événements, formulaires, charte du client.", None),
  ("Relier aux outils métier", "Carte reliée au logiciel de restauration, demandes envoyées au CRM.", None),
  ("Développer un MCP dédié", "Outils de pages, événements, formulaires, demandes, avec un compte administrateur.", "Crée un serveur MCP pour ce site : outils pour modifier une page, créer un événement en brouillon, consulter les demandes. Journalise chaque appel ; toute suppression exige confirmer=true."),
  ("Sécuriser", "Journal des appels, confirmation obligatoire pour toute suppression.", None),
  ("Former le client", "Il demande à son IA au lieu de demander à l'agence.", None),
 ],
 garde_fous=["Publication finale après accord du client.", "Aucune modification de production pendant une démo."],
 etat_reel="Démonstration préparée d'après les schémas réels, sans appel envoyé à la production. L'intégration de l'agent vocal restait à finaliser.")

add(episode=20, slug='construire-son-equipe-d-employes-ia', titre="Construire une équipe d'employés IA qui travaille avec ses logiciels",
 promesse="Relier orchestrateur, CMS, CRM, logiciel métier et Académie autour d'un objectif commun.",
 pour_qui="Dirigeants qui veulent passer des outils isolés à un système.",
 offre='planit', outils=T('planit','cms','crm','foodeatup','academie'),
 etapes=[
  ("Fixer un objectif d'équipe", "Exemple de démonstration : « Trouve vingt nouveaux clients pour FoodEatUp ce mois-ci » (objectif fictif).", None),
  ("Répartir les rôles", "Pilotage, contenus, prescripteurs, relance et devis, accueil des demandes, veille.", "Répartis cet objectif [objectif] entre 6 agents : rôle, outils MCP autorisés, livrable, indicateur."),
  ("Brancher les logiciels par MCP", "Chaque agent utilise seulement ses outils.", None),
  ("Écrire les routines", "Objectif, indicateur, critère d'arrêt.", None),
  ("Décider après mesure", "Après 3 exécutions et 14 jours : garder, ajuster ou arrêter.", None),
 ],
 garde_fous=["Les agents proposent, l'humain valide."],
 etat_reel="Six agents et vingt routines écrites, tous en préparation (autonomie Aperçu) au moment de l'épisode.")

add(episode=21, slug='former-ses-employes-ia', titre="Former un agent IA à une mission précise, quiz compris",
 promesse="Apprendre la procédure, donner les bons outils, faire passer le quiz et noter la consigne sur 6.",
 pour_qui="Toute entreprise qui confie une tâche récurrente à un agent.",
 offre='planit', outils=T('academie','claude','foodeatup'),
 etapes=[
  ("Choisir la mission", "Exemple : éviter les ruptures de stock.", None),
  ("Apprendre la procédure", "Produits sous le seuil → liste d'achats → commandes préparées par fournisseur → l'humain envoie.", None),
  ("Donner seulement les bons outils", "Stocks bas, liste d'achats, fournisseurs, préparation des commandes (sans envoi).", None),
  ("Faire passer le quiz", "Le serveur corrige les réponses de l'agent.", None),
  ("Noter et compléter la consigne", "Une consigne brute obtient 0/6 ; complétée (objectif, sources, limite, rendu, critère d'arrêt, accord humain), elle obtient 6/6.", "Objectif : éviter les ruptures. Sources : stocks et liste d'achats. Limite : préparer sans envoyer. Rendu : une commande par fournisseur. Arrêt : plus aucun produit sous le seuil. Accord : j'envoie moi-même."),
 ],
 garde_fous=["La validation finale reste humaine."],
 etat_reel="Appels réels en lecture seule : 3 réponses de quiz justes ; consigne brute 0/6, consigne complétée 6/6.")

add(episode=22, slug='le-vrai-cout-d-une-equipe-ia', titre="Le vrai coût d'une équipe d'agents IA",
 promesse="La liste des abonnements d'un écosystème réel et ce qu'il faut ajouter pour être honnête.",
 pour_qui="Dirigeants qui veulent budgéter avant de se lancer.",
 offre='coaching', outils=T('claude','chatgpt','crm','cms','rh','figma','lovable','elevenlabs','planit'),
 etapes=[
  ("Lister les abonnements", "Claude 20 €, ChatGPT 20 €, RapidoCRM 49 €, RapidoCMS 29 €, RapidoRH 19 €, Figma 20 €, Lovable 25 €, ElevenLabs 20 €, environ 20 € d'API pour Plan'It : 222 € par mois (chiffres de l'épisode).", None),
  ("Ajouter les coûts cachés", "Temps de configuration, serveurs et API supplémentaires.", None),
  ("Connecter avant d'empiler", "La valeur vient des connexions MCP et de l'organisation du travail des agents, pas du nombre d'abonnements.", "Voici mes outils actuels [liste]. Indique lesquels ont un MCP, ce que je peux connecter à Claude, et ce qui est redondant."),
  ("Lancer une première mission", "Une mission utile, mesurée, avant d'élargir.", None),
 ],
 garde_fous=["Les tarifs évoluent : vérifier sur le site de chaque éditeur."],
 etat_reel="Montants donnés par Michael dans l'épisode ; ils ne comprennent pas la configuration, les serveurs ni les API supplémentaires.")
