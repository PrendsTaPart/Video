from formations_part3 import F, T, add

add(episode=23, slug='transformer-ses-reunions-en-taches', titre="Transformer ses réunions en plan d'action avec l'IA",
 promesse="Enregistrer, transcrire, extraire décisions et tâches avec leur responsable, leur échéance et la phrase source.",
 pour_qui="Équipes qui sortent des réunions sans savoir qui fait quoi.",
 offre='rh', outils=T('whisper','gemini','rh','crm','cms'),
 etapes=[
  ("Enregistrer ou importer l'audio", "Une réunion, un fichier.", None),
  ("Transcrire avec Whisper", "La transcription sert de source à tout le reste.", None),
  ("Extraire décisions et tâches", "Résumé, décisions, tâches avec responsable, échéance et phrase exacte qui les a fait naître.", "À partir de cette transcription, liste les décisions et les tâches : responsable, échéance, priorité et citation exacte de la phrase source."),
  ("Ranger les tâches", "Dans le tableau de suivi ; les écritures vers CRM et CMS attendent une validation.", None),
  ("Boucler avec le suivi de projet", "Lire les projets existants, puis y créer les tâches (prochaine étape).", None),
 ],
 garde_fous=["Consentement des participants à l'enregistrement.", "Écritures externes après validation."],
 etat_reel="RapidoMeet était livré à 83 % ; la sécurité était en cours de finalisation. La création directe de tâches dans RapidoRH était la prochaine étape.")

add(episode=24, slug='recrutement-assiste-par-ia', titre="Organiser ses recrutements avec un logiciel assisté par l'IA",
 promesse="Offres rédigées depuis la base de connaissance, CV analysés, score d'aide au tri, décision humaine.",
 pour_qui="Dirigeants et RH de PME multi-entreprises.",
 offre='rh', outils=T('claude','n8n','supabase'),
 etapes=[
  ("Séparer les entreprises", "Plusieurs recrutements au même endroit, données séparées par entreprise.", None),
  ("Rédiger l'offre", "Poste, compétences, missions, à partir de la base de connaissance de l'entreprise.", "Rédige l'offre d'emploi pour [poste] à partir de ces informations [contexte] : missions, compétences, conditions, process."),
  ("Analyser les CV", "Extraction des compétences et score d'aide à la présélection : un score aide à trier, il ne dit rien de la valeur d'une personne.", None),
  ("Suivre les candidats", "Nouveau, en analyse, entretien, en attente, retenu, refusé.", None),
  ("Architecturer proprement", "Le cerveau : FastAPI et FastMCP. Les mains : workflows n8n. Le cloud : Supabase. Chaque écriture attend une confirmation.", None),
 ],
 garde_fous=["Un score IA n'est jamais une décision d'embauche.", "Publier une offre ou lancer un onboarding : jamais sans accord."],
 etat_reel="Les modules d'entretien (planification, transcription, rapport, avatar) existent dans le code mais étaient encore en test.")

add(episode=25, slug='un-presentateur-ia-pour-ses-logiciels', titre="Créer un présentateur IA qui fait vos démonstrations",
 promesse="Storyboard proposé par l'IA, une seule capture d'écran, avatar 3D multilingue et mode questions en direct.",
 pour_qui="Éditeurs et commerciaux qui répètent les mêmes démos.",
 offre='rapido', outils=T('claude','elevenlabs','rapido'),
 etapes=[
  ("Faire proposer le storyboard", "Scènes, texte de l'avatar, action à filmer.", "Propose le storyboard d'une démo de [logiciel] en 8 scènes : texte de l'avatar, action à l'écran, durée."),
  ("Filmer une seule fois", "L'enregistrement se découpe automatiquement par scène.", None),
  ("Faire présenter l'avatar", "Voix générée en français, anglais ou arabe.", None),
  ("Ouvrir le mode questions", "Le client interrompt, pose sa question, l'assistant répond depuis le script et l'emmène au bon passage.", None),
  ("Récolter les questions sans réponse", "Ce sont vos prochains tutoriels.", None),
 ],
 garde_fous=["Ne pas annoncer un lien de démo en direct qui n'existe pas encore."],
 etat_reel="RapidoTuto était prêt mais pas encore partagé aux clients ; le mode en direct est codé, sans lien public au moment de l'épisode.")

add(episode=26, slug='studio-ia-pour-sa-passion', titre="Transformer une passion en studio de production IA",
 promesse="Données sportives, analyse IA, visuels et équipe d'agents qui scénarise, illustre, monte et vérifie.",
 pour_qui="Créateurs et curieux qui veulent apprendre en s'amusant.",
 offre='coaching', outils=T('n8n','gemini','claude_code'),
 etapes=[
  ("Récupérer les données", "Une API sportive branchée à n8n : matchs, statistiques, équipes.", None),
  ("Analyser avec un modèle", "Un workflow Gemini propose un pronostic, présenté comme incertain.", None),
  ("Préparer les visuels", "Un workflow dédié produit les images de début et de fin.", None),
  ("Organiser l'équipe d'agents", "Scénariste, directeur artistique, compositeur vidéo, vérificateur légal qui peut bloquer.", "Crée 4 agents Claude Code pour produire une capsule vidéo : scénariste, directeur artistique, compositeur, vérificateur légal. Le vérificateur peut bloquer la publication."),
  ("Publier après validation", "Brouillons vers le CMS, jamais de publication automatique.", None),
 ],
 garde_fous=["Aucun pari, aucune garantie de résultat.", "Ne jamais laisser une clé d'API en clair dans un workflow."],
 etat_reel="Workflows n8n vérifiés en lecture seule ; l'audit a relevé une clé d'API en clair dans un workflow, à remplacer (rotation recommandée). La liaison automatique entre n8n et le plugin restait à construire.")

add(episode=27, slug='de-n8n-aux-serveurs-mcp', titre="Des routes n8n aux autoroutes MCP : bien répartir les rôles",
 promesse="Comprendre quand utiliser des workflows et quand exposer un serveur MCP, et comment les faire travailler ensemble.",
 pour_qui="Utilisateurs de n8n, Make ou Zapier qui découvrent les agents.",
 offre='planit', outils=T('n8n','claude','rh','crm','cms'),
 etapes=[
  ("Cartographier ses workflows", "Prospection, marketing, RH, stocks, recrutement : combien de connexions point à point ?", "Voici la liste de mes workflows [liste]. Regroupe-les par logiciel et repère ceux qu'un serveur MCP rendrait inutiles."),
  ("Exposer chaque logiciel en MCP", "CRM, CMS, logiciel métier, RH : chaque logiciel expose ses fonctions une fois pour tous les agents.", None),
  ("Garder n8n pour orchestrer", "n8n déclenche les routines et coordonne les opérations.", None),
  ("Exemple de routine", "Récupérer les tâches RapidoRH par MCP, les confier à un agent IA, enregistrer le résultat.", None),
  ("Sécuriser les webhooks", "Authentifier chaque webhook, ne jamais mettre de jeton en clair, surveiller les échecs.", None),
 ],
 garde_fous=["n8n organise le trafic, les MCP ouvrent l'accès, l'humain garde les validations."],
 etat_reel="L'audit n8n a relevé un workflow en erreur quotidienne (jeton d'authentification expiré) et des webhooks sans authentification : points à corriger.")

add(episode=28, slug='departement-de-prospection-ia', titre="Monter un département de prospection avec n8n, des agents et un CRM",
 promesse="Orchestration, enrichissement, détection des réponses, relances et reporting, centralisés dans le CRM.",
 pour_qui="Équipes commerciales B2B.",
 offre='crm', outils=T('n8n','crm','claude'),
 etapes=[
  ("Découper le processus", "Recherche, enrichissement, campagnes, suivi.", None),
  ("Un workflow par fonction", "Orchestrateur, enrichissement, détection des réponses, relances, rapport quotidien.", None),
  ("Donner aux agents les outils autorisés", "Recherche de prospects, fiche entreprise, ajout au pipeline.", "Recherche 20 [type d'établissement] à [ville], qualifie-les et ajoute-les au pipeline en « Nouveau prospect ». Liste ce qui demande mon accord."),
  ("Centraliser dans le CRM", "Un seul pipeline pour tout suivre.", None),
  ("Mesurer ce qui compte", "Réponses, rendez-vous, ventes : pas le taux de réussite des workflows.", None),
 ],
 garde_fous=["Trouver des prospects n'est pas signer des clients."],
 etat_reel="Cinq workflows actifs vérifiés ; le pipeline comptait 70 prospects et aucune vente signée par ce système au moment de l'épisode.")

add(episode=29, slug='equipe-ia-pour-son-seo', titre="Créer une équipe d'agents IA pour son référencement",
 promesse="Veille des tendances, mots-clés, articles depuis sa documentation, audit des pages, publication après relecture.",
 pour_qui="Éditeurs et commerces qui veulent être trouvés sur Google.",
 offre='foodeatup', outils=T('n8n','gemini','claude','foodeatup'),
 etapes=[
  ("Surveiller les tendances", "Google Trends, Google News et Reddit.", None),
  ("Analyser les mots-clés", "Search Console et outils SEO.", None),
  ("Préparer des articles utiles", "À partir de sa propre documentation, sur de vraies questions de clients.", "Propose 10 sujets d'articles qui répondent à de vraies questions de [cible] sur [thème], avec mot-clé principal et intention de recherche."),
  ("Piloter le site par MCP", "Idées, piliers éditoriaux, calendrier, contrôles avant publication.", None),
  ("Relire, publier, mesurer, recommencer", "Rien ne part sans relecture humaine.", None),
 ],
 garde_fous=["Pas de production d'articles en masse : répondre aux vraies questions."],
 etat_reel="Une centaine d'idées, quatre-vingts articles en relecture et trois articles publiés au moment de l'épisode.")

add(episode=30, slug='commercial-ia-en-un-prompt', titre="Piloter un commercial IA avec un seul prompt",
 promesse="Rechercher, qualifier, segmenter, préparer rendez-vous, devis et relances, avec validation des actions sensibles.",
 pour_qui="Dirigeants et commerciaux qui veulent piloter des objectifs plutôt que des clics.",
 offre='crm', outils=T('claude','chatgpt','crm'),
 etapes=[
  ("Donner l'objectif en un prompt", "Depuis Claude ou ChatGPT.", "Trouve-moi des restaurants susceptibles d'être intéressés par FoodEatUp, qualifie les prospects et prépare les prochaines actions commerciales. Présente-moi les actions qui demandent mon accord avant de les exécuter."),
  ("Rechercher et enregistrer", "Les outils du CRM recherchent les entreprises, retrouvent leurs informations et les enregistrent.", None),
  ("Segmenter", "Restauration rapide, bar et brasserie, traiteur, chaînes et franchises.", None),
  ("Préparer la suite", "Rendez-vous, devis et relances, avec traçabilité.", None),
  ("Garder la voix pour plus tard", "L'agent vocal a son pitch et son catalogue, mais n'appelle personne tant que le numéro n'est pas connecté.", None),
 ],
 garde_fous=["Actions sensibles validées.", "Chaque interaction reste traçable."],
 etat_reel="70 prospects dans le pipeline ; agent vocal non connecté à un numéro au moment de l'épisode, donc aucun appel passé.")
