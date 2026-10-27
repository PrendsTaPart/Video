# Contenu des 30 formations (épisodes 1 à 30), tiré des scripts et audits du dépôt.
# « etat_reel » reprend ce qui a été vérifié pendant la production de chaque épisode.
L = {
 'claude': ('Claude', 'https://claude.ai'),
 'claude_code': ('Claude Code', 'https://claude.ai/code'),
 'chatgpt': ('ChatGPT', 'https://chatgpt.com'),
 'plugins': ('BraindCode Plugins', 'https://plugin.braindcode.com'),
 'build': ('BraindCode Build', 'https://build.braindcode.com'),
 'planit': ("Plan'It", 'https://plani-t.fr'),
 'foodeatup': ('FoodEatUp', 'https://site.foodeatup.com'),
 'tuto_fe': ('FoodEatUp Académie', 'https://tutoriel.foodeatup.com'),
 'academie': ('Mon Académie', 'https://academie.foodeatup.com/'),
 'crm': ('RapidoCRM', 'https://rapido-crm.com'),
 'cms': ('RapidoCMS', 'https://rapidocms.com'),
 'rh': ('RapidoRH', 'https://rh.rapidosoftware.com'),
 'rapido': ('RapidoSoftware', 'https://rapidosoftware.com/'),
 'lovable': ('Lovable', 'https://lovable.dev'),
 'figma': ('Figma', 'https://www.figma.com'),
 'elevenlabs': ('ElevenLabs', 'https://elevenlabs.io'),
 'n8n': ('n8n', 'https://n8n.io'),
 'flutter': ('Flutter', 'https://flutter.dev'),
 'ffmpeg': ('FFmpeg', 'https://ffmpeg.org'),
 'whisper': ('Whisper (faster-whisper)', 'https://github.com/SYSTRAN/faster-whisper'),
 'publisher': ('Publisher Bot', 'https://youtube.rapidocms.com'),
 'gemini': ('Gemini', 'https://gemini.google.com'),
 'supabase': ('Supabase', 'https://supabase.com'),
}
def T(*keys): return [{'nom': L[k][0], 'url': L[k][1]} for k in keys]

F = []
def add(**kw): F.append(kw)

add(episode=1, slug='le-cerveau-equipe-agents-ia', titre="Construire le cerveau de son équipe d'agents IA",
 promesse="Comprendre et assembler les 5 briques d'une équipe d'agents IA : MCP, Skills, agents, workflows et base de connaissance.",
 pour_qui="Dirigeants et indépendants qui veulent que Claude travaille avec leurs propres logiciels.",
 offre='plugins', outils=T('claude_code','plugins','planit'),
 etapes=[
  ("Connecter les outils métier avec les MCP", "Un serveur MCP expose les fonctions d'un logiciel (restaurant, CRM, marketing, RH) à Claude, selon des autorisations. Commencez par un seul logiciel, en lecture seule.", "Liste les outils MCP disponibles dans cette session, classe-les en lecture et en écriture, et dis-moi lesquels peuvent modifier des données."),
  ("Écrire les Skills : la méthode", "Une Skill est un fichier SKILL.md qui décrit une procédure : étapes, règles métier, garde-fous. Exemple réel : la Skill « reappro-fournisseurs » de FoodEatUp et sa règle « Jamais de commande fournisseur sans validation explicite ».", "Rédige une Skill SKILL.md pour la procédure suivante : [procédure]. Inclus : quand l'utiliser, les étapes, les outils MCP autorisés, les garde-fous et ce qui exige mon accord."),
  ("Définir les agents par métier", "Un agent = un rôle, un objectif, des compétences et des outils. Organisez-les comme un organigramme : direction, commercial, marketing, finance, restaurant.", "Propose l'organigramme de 5 agents pour mon entreprise [activité], avec pour chacun : rôle, objectif mesurable, Skills et outils MCP autorisés."),
  ("Enchaîner avec des workflows validés", "Un workflow enchaîne des étapes avec des points de validation. Exemple : stocks bas → commande préparée → validation humaine → commande envoyée après accord.", None),
  ("Ajouter la base de connaissance", "La base de connaissance apporte le contexte propre à l'entreprise : offres, ton, règles. Les plugins BraindCode s'installent dans Claude Code depuis la marketplace.", "/plugin marketplace add PrendsTaPart/Plugin-Claude-MCP-BraindCode-"),
  ("Poser les garde-fous", "Paiements, publications et suppressions restent bloqués sans votre clic (hook « garde-destructif » du plugin FoodEatUp).", None),
 ],
 garde_fous=["Une commande, un paiement ou une publication attend toujours une validation humaine.", "Commencer en lecture seule, ouvrir l'écriture outil par outil."],
 etat_reel="Le dépôt de la marketplace comptait, au moment de l'épisode, 33 plugins, 544 Skills et 77 agents. Aucune exécution d'agent n'a été montrée dans la vidéo : la procédure réelle est montrée, sans résultat inventé.")

add(episode=2, slug='4-applications-en-un-dimanche', titre="Développer 4 applications mobiles avec l'IA en une journée",
 promesse="La méthode pour passer d'une idée à des applications Flutter connectées à votre logiciel métier par MCP.",
 pour_qui="Éditeurs de logiciels, agences et entrepreneurs tech.",
 offre='foodeatup', outils=T('claude_code','flutter','foodeatup','elevenlabs'),
 etapes=[
  ("Choisir des applications satellites utiles", "Partir des usages terrain : borne de fidélité au comptoir, assistant HACCP vocal, caisse mobile serveur, tablette client avec menu digital.", "Liste 5 applications satellites pour [mon logiciel], avec pour chacune : utilisateur, problème résolu, 3 écrans clés et les outils MCP nécessaires."),
  ("Écrire le cahier des charges par écran", "Un écran = une intention, une action principale, des états (vide, chargement, erreur). Le cahier des charges sert de contrat à Claude Code.", "Écris le cahier des charges Flutter de l'application [nom] : écrans, navigation, données lues par MCP, règles d'accès et tests attendus."),
  ("Brancher les données par MCP", "Les applications lisent et écrivent via les outils MCP du logiciel (ici FoodEatUp) : jamais de clé dans le code, authentification OAuth.", None),
  ("Tester avant de montrer", "Tests de widgets et rendus « golden » : les captures de la vidéo viennent de ces tests et des fiches de store, pas de maquettes.", "Ajoute un test de widget par écran et un rendu golden, puis lance flutter analyze et flutter test jusqu'au vert."),
  ("Personnaliser par client", "Chaque restaurant choisit un thème et sa charte : six styles réels sur la caisse.", None),
  ("Préparer la publication", "Fiches Google Play et App Store, captures, politique de confidentialité. La publication reste une étape humaine.", None),
 ],
 garde_fous=["Ne jamais annoncer une fonction non terminée : le paiement sans contact était « bientôt », pas disponible.", "Aucune clé ni secret dans le dépôt."],
 etat_reel="Quatre APK réels (fidélité, HACCP vocal, caisse mobile, tablette client) et un jeu 3D jouable dans le navigateur. La publication sur les stores n'était pas encore faite au moment de l'épisode.")

add(episode=3, slug='creer-un-store-d-extensions', titre="Transformer un logiciel en plateforme d'extensions",
 promesse="Concevoir un store d'applications et d'extensions autour de votre logiciel, du parcours utilisateur à l'intégration.",
 pour_qui="Éditeurs SaaS qui veulent devenir une plateforme.",
 offre='foodeatup', outils=T('claude','figma','foodeatup'),
 etapes=[
  ("Imaginer le parcours utilisateur", "Découvrir → fiche → activer → ouvrir. Chaque étape a un écran et une décision.", "Dessine le parcours d'un restaurateur dans un store d'extensions : écrans, informations affichées, décision à chaque étape."),
  ("Organiser les extensions par métier", "Salle, cuisine, clients, formation, IA : un classement qui parle au métier plutôt qu'à la technique.", None),
  ("Rédiger la fiche d'une extension", "Captures réelles, fonctions vérifiées, personnalisation, bouton d'activation. Une fonction non livrée est marquée « bientôt ».", "Rédige la fiche store de l'extension [nom] : promesse, 5 fonctions vérifiées, prérequis, ce qui est prévu mais pas encore disponible."),
  ("Penser l'écosystème MCP", "Chaque extension partage le même socle : fonctions métier et connexions MCP communes.", None),
  ("Maquetter avant de coder", "Le store de l'épisode est une maquette conceptuelle signalée à l'écran : on valide le parcours avant d'écrire le code.", None),
 ],
 garde_fous=["Signaler toute maquette comme maquette.", "Ne rien promettre d'activable tant que ce n'est pas livré."],
 etat_reel="Le FoodEatUp Store était une maquette conceptuelle : module en développement, activation pas encore disponible.")

add(episode=4, slug='monter-ses-videos-avec-des-agents-ia', titre="Monter ses vidéos avec des agents IA, de l'idée à la publication",
 promesse="Une chaîne de production vidéo réutilisable : script, voix IA, montage, sous-titres, brouillon de publication.",
 pour_qui="Créateurs, marketeurs et entrepreneurs qui publient chaque jour.",
 offre='cms', outils=T('claude_code','elevenlabs','whisper','ffmpeg','cms'),
 etapes=[
  ("Partir d'une idée et de sources réelles", "Captures, démonstrations, dépôts : Claude vérifie ce qui existe vraiment avant d'écrire.", "Lis ces sources [liens], liste ce qui est vérifiable et ce qui ne l'est pas, puis propose un scénario de 90 s en 7 scènes."),
  ("Générer la voix off", "Voix ElevenLabs (jamais un clone sans accord). Une seule prise, puis transcription pour caler les mots.", None),
  ("Caler les mots à la seconde", "faster-whisper donne l'horodatage de chaque mot : les animations et sous-titres se calent dessus.", None),
  ("Monter avec des recettes", "Couper, enchaîner, mixer voix et musique avec ducking, incruster les sous-titres, exporter en 9:16 (recettes FFmpeg du plugin rapido-video).", "Monte la vidéo : voix à -14 LUFS, musique qui baisse sous la voix, sous-titres incrustés, export 1080×1920, plus une version de 30 s."),
  ("Préparer la publication dans RapidoCMS", "Bibliothèque → brouillon pour le réseau choisi → programmation dans le calendrier.", "Dépose la vidéo dans la bibliothèque RapidoCMS et crée un brouillon LinkedIn, sans programmer."),
  ("Garder l'humain aux bons endroits", "Valider le scénario, les chiffres, l'accord des personnes citées et le feu vert de publication.", None),
 ],
 garde_fous=["Aucune publication sans feu vert humain.", "Accord écrit des personnes citées."],
 etat_reel="Les épisodes 1 à 3 ont été montés avec des scripts FFmpeg, Whisper et Playwright écrits pour l'occasion ; les recettes du plugin rapido-video ont été utilisées dans l'épisode 4.")

add(episode=5, slug='prospecter-avec-claude-et-un-mcp', titre="Donner un objectif de prospection à Claude, sans perdre le contrôle",
 promesse="Rechercher des établissements ciblés, les qualifier et préparer une campagne conforme, avec votre accord avant chaque envoi.",
 pour_qui="Commerciaux, fondateurs et agences B2B.",
 offre='crm', outils=T('claude','crm','n8n'),
 etapes=[
  ("Écrire l'objectif et la règle", "Un objectif précis et une règle explicite : ne contacter personne sans validation.", "Analyse mes dernières prospections, identifie les nouveaux établissements et prépare une campagne adaptée à [offre]. Ne contacte personne sans ma validation."),
  ("Explorer régions et spécialités", "Le MCP de prospection expose les régions, les spécialités et l'historique des recherches.", None),
  ("Lire les résultats sans les confondre", "200 résultats de recherche ne sont pas 200 clients. Suivez l'entonnoir : résultats → enregistrés → qualifiés → contactés → réponses → ventes.", "Construis l'entonnoir de mes prospects : résultats, enregistrés, qualifiés, contactés, réponses, ventes. Ne remplis une étape que si la donnée existe."),
  ("Qualifier et dédoublonner", "Vérifier les informations, comprendre l'activité, éviter les doublons avant toute approche.", None),
  ("Rédiger une campagne conforme", "Identité de l'expéditeur, lien de désinscription, politique de confidentialité. Un SMS doit porter la mention STOP.", "Rédige un e-mail de prospection pour [cible] avec identité de l'expéditeur, lien de désinscription et lien vers la politique de confidentialité. Ne l'envoie pas."),
  ("Tester petit, mesurer, relancer", "Tester sur 10 établissements, relance à J+3 validée, mesurer les réponses avant d'élargir.", None),
 ],
 garde_fous=["Aucun envoi sans accord sur cet envoi.", "Appels automatisés : à faire valider par un juriste avant toute utilisation."],
 etat_reel="Audit en lecture seule : 5 recherches = 200 résultats ; 90 établissements enregistrés au statut « nouveau » ; 0 contacté pour FoodEatUp. L'audit a relevé des e-mails passés sans lien de désinscription, à corriger avant toute campagne.")
