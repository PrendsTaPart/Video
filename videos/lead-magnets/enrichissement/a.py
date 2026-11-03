# Enrichissement des formations 1 à 8.
# etapes : (complément d'explication, prompt si l'étape n'en a pas — sinon None, résultat attendu, piège à éviter)
E = {}

E["le-cerveau-equipe-agents-ia"] = {
 "objectifs": ["Identifier les 5 briques d'une équipe d'agents IA et leur rôle", "Rédiger une première Skill et un premier agent pour votre métier", "Poser les garde-fous qui empêchent toute action sensible sans votre accord"],
 "prerequis": ["Un compte Claude (Claude Code pour installer des plugins)", "Au moins un logiciel métier qui propose un serveur MCP, ou un logiciel que vous voulez connecter"],
 "etapes": [
  ("Le MCP ne donne que les droits du compte connecté : commencez par un compte qui ne peut que lire.", None, "La liste des outils disponibles, triés entre lecture et écriture.", "Brancher tous vos logiciels d'un coup : on ne sait plus quel outil a fait quoi."),
  ("Une bonne Skill tient en une page et se teste sur un cas réel avant d'être généralisée.", None, "Un fichier SKILL.md prêt à relire, avec ses règles et ce qui exige votre accord.", "Écrire une Skill trop générale (« gérer le marketing ») qu'aucun agent ne peut appliquer."),
  ("Chaque agent reçoit seulement les outils de son métier : le commercial n'a pas accès à la comptabilité.", None, "Un organigramme d'agents avec un objectif mesurable par agent.", "Créer un « super agent » qui a tous les outils : impossible à contrôler."),
  ("Placez la validation humaine juste avant l'action irréversible, pas à chaque étape.", "Transforme cette procédure [procédure] en workflow : liste les étapes, indique les outils MCP utilisés à chacune et place un point de validation humaine avant toute action irréversible (envoi, paiement, publication).", "Un schéma d'enchaînement avec ses points de validation clairement placés.", "Demander une validation à chaque clic : vous finirez par valider sans lire."),
  ("La base de connaissance se met à jour : prévoyez qui la relit et à quelle fréquence.", None, "Un contexte d'entreprise (offres, ton, règles) que Claude consulte avant de répondre.", "Y mettre des données clients ou des secrets : la base est lue à chaque conversation."),
  ("Listez les actions sensibles une fois pour toutes : paiement, envoi, publication, suppression.", "Liste les outils MCP de cette session qui peuvent payer, envoyer, publier ou supprimer. Pour chacun, propose la règle de validation à appliquer et dis-moi comment la bloquer tant que je n'ai pas accepté.", "La liste des actions bloquées tant que vous n'avez pas cliqué.", "Compter sur la prudence du modèle au lieu d'un blocage technique."),
 ]}

E["4-applications-en-un-dimanche"] = {
 "objectifs": ["Choisir des applications satellites utiles autour de votre logiciel", "Écrire un cahier des charges par écran exploitable par Claude Code", "Tester et préparer la publication sans annoncer ce qui n'est pas fini"],
 "prerequis": ["Claude Code et l'environnement Flutter installés", "Un logiciel métier qui expose ses données par MCP"],
 "etapes": [
  ("Une application satellite fait une seule chose très bien, pour une seule personne.", None, "5 idées classées, avec leurs écrans clés et les outils MCP nécessaires.", "Vouloir refaire tout le logiciel dans une application mobile."),
  ("Décrivez aussi ce qui se passe sans réseau et en cas d'erreur.", None, "Un cahier des charges par écran, utilisable comme contrat par Claude Code.", "Oublier les états vide, chargement et erreur : l'application semble cassée au premier souci."),
  ("Le jeton d'accès se stocke dans le coffre sécurisé du téléphone, jamais dans le code.", "Branche l'application [nom] sur le MCP de [logiciel] : authentification OAuth, aucun jeton dans le code, lecture d'abord. Liste les outils appelés par écran et ce qui se passe hors connexion.", "Des écrans qui affichent les vraies données du logiciel, sans clé dans le dépôt.", "Copier une clé d'API dans le code pour aller plus vite."),
  ("Les captures du store viennent des tests : ce que vous montrez existe vraiment.", None, "flutter analyze et flutter test au vert, un rendu golden par écran.", "Montrer une maquette comme si l'écran était terminé."),
  ("La personnalisation passe par des thèmes, pas par une copie de l'application par client.", "Ajoute un système de thèmes à l'application : couleurs, police et logo chargés depuis la configuration du client, avec un contraste AA vérifié par un test.", "Un thème par client, sans dupliquer le code.", "Créer une branche du code par client : impossible à maintenir."),
  ("Fiche, captures, politique de confidentialité : préparez tout, l'envoi reste votre décision.", "Prépare la fiche Google Play de [application] : titre, description courte et longue, 4 captures à produire depuis les tests, et la liste des données collectées pour la politique de confidentialité. Ne publie rien.", "Un dossier de publication complet, prêt à relire.", "Annoncer une fonction « bientôt » comme si elle était disponible."),
 ]}

E["creer-un-store-d-extensions"] = {
 "objectifs": ["Dessiner le parcours d'un client dans un store d'extensions", "Rédiger une fiche d'extension honnête et vérifiable", "Valider le concept par une maquette avant d'écrire le code"],
 "prerequis": ["Un logiciel avec plusieurs modules ou applications satellites", "Figma ou un outil de maquette"],
 "etapes": [
  ("À chaque étape, notez la question que se pose le client et la réponse que l'écran doit lui donner.", None, "Un parcours en 4 écrans avec la décision attendue à chacun.", "Commencer par l'écran technique d'activation au lieu de la découverte."),
  ("Classez par moment de la journée du client : c'est ainsi qu'il cherche.", "Classe ces extensions [liste] par métier du client (salle, cuisine, clients, formation, IA). Pour chaque catégorie, propose un titre et une phrase qui parle au client, sans jargon technique.", "Des catégories que le client comprend sans explication.", "Classer par technologie (« API », « webhook ») : le client ne s'y retrouve pas."),
  ("Une fonction prévue est écrite « bientôt », jamais au présent.", None, "Une fiche avec 5 fonctions vérifiées et la liste de ce qui reste prévu.", "Promettre une fonction non livrée pour faire plus complet."),
  ("Les extensions partagent les mêmes outils MCP : un agent les pilote toutes de la même façon.", "Pour chaque extension de cette liste [liste], indique les outils MCP du socle commun qu'elle utilise et ceux qu'il faudrait ajouter. Signale les doublons.", "Une carte des outils MCP partagés et des manques.", "Créer un connecteur différent par extension."),
  ("Signalez la maquette comme telle à l'écran et dans la communication.", "Crée une maquette cliquable du store dans Figma à partir de ce parcours [parcours]. Ajoute un bandeau « maquette » sur chaque écran.", "Une maquette testable par 3 clients avant tout développement.", "Présenter la maquette comme un produit disponible."),
 ]}

E["monter-ses-videos-avec-des-agents-ia"] = {
 "objectifs": ["Construire une chaîne de production vidéo réutilisable", "Caler voix, sous-titres et animations à la seconde", "Préparer la publication sans jamais publier sans feu vert"],
 "prerequis": ["Un compte ElevenLabs et FFmpeg installé", "Des sources réelles : captures, démonstrations, dépôts"],
 "etapes": [
  ("Séparez dans le scénario ce qui est montré de ce qui est seulement raconté.", None, "Un scénario de 90 s en 7 scènes, chaque fait relié à sa source.", "Écrire d'abord, vérifier ensuite : les chiffres faux s'installent."),
  ("Choisissez une voix de la bibliothèque, ou un clone uniquement avec l'accord écrit de la personne.", "Génère la voix off de ce texte [texte] avec une voix française de la bibliothèque, en une seule prise. Écris les nombres en toutes lettres pour une prononciation correcte.", "Un fichier audio propre, sans coupure ni mauvaise prononciation.", "Cloner la voix de quelqu'un sans son accord écrit."),
  ("L'horodatage mot à mot sert aussi à vérifier que la voix dit bien le texte prévu.", "Transcris cette voix off avec horodatage mot à mot, puis compare-la au texte prévu [texte] et liste les mots mal prononcés ou manquants.", "Un minutage mot à mot pour caler sous-titres et animations.", "Caler les sous-titres à l'oreille : ils décrochent au bout de 20 secondes."),
  ("Normalisez le volume à la fin : -14 LUFS est la référence des réseaux.", None, "Une vidéo 9:16 et sa version courte, sous-titrées et mixées.", "Laisser la musique couvrir la voix."),
  ("Une pièce n'est livrable que si son fichier répond depuis la bibliothèque.", None, "Un brouillon par réseau dans RapidoCMS, rien de programmé.", "Programmer directement sans relecture humaine."),
  ("Notez qui a validé quoi : scénario, chiffres, accords, publication.", "Prépare la check-list de validation de cette vidéo : chiffres et leurs sources, personnes et marques citées avec leur accord, mentions obligatoires. Indique ce qui reste à valider par un humain.", "Une check-list signée avant la publication.", "Confondre « prêt » (le fichier existe) et « validé » (quelqu'un l'a regardé en entier)."),
 ]}

E["prospecter-avec-claude-et-un-mcp"] = {
 "objectifs": ["Formuler un objectif de prospection avec une règle de validation", "Lire un entonnoir de prospection sans confondre résultats et clients", "Préparer une campagne conforme, testée à petite échelle"],
 "prerequis": ["Un CRM ou un outil de prospection connecté à Claude par MCP", "Une offre claire et une cible définie"],
 "etapes": [
  ("La règle « ne contacter personne sans validation » s'écrit dans chaque demande, pas une fois au début.", None, "Un objectif daté, mesurable, avec sa règle de validation.", "Donner un objectif vague (« trouve des clients ») sans limite."),
  ("Commencez par une région et une spécialité : on mesure mieux une petite cible.", "Liste les régions et spécialités disponibles dans l'outil de prospection, puis l'historique de mes recherches. Propose 3 cibles que je n'ai pas encore explorées, sans lancer de recherche.", "3 cibles nouvelles, avec ce qui a déjà été cherché.", "Relancer une recherche déjà faite et compter deux fois les mêmes établissements."),
  ("Chaque étape de l'entonnoir a sa propre définition : notez-la.", None, "Un entonnoir où chaque étape est un vrai chiffre ou « donnée absente ».", "Annoncer les résultats de recherche comme des clients."),
  ("Dédoublonnez par email, puis par téléphone, puis par établissement et ville.", "Qualifie ces prospects [liste] : activité réelle, taille, pertinence pour [offre], doublons éventuels. Classe-les en « à contacter », « à vérifier », « hors cible ». Ne contacte personne.", "Une liste qualifiée et dédoublonnée.", "Contacter deux fois la même personne depuis deux fiches."),
  ("Faites relire la campagne par quelqu'un qui n'a pas écrit le texte.", None, "Un email et un SMS conformes, en brouillon.", "Oublier le lien de désinscription ou la mention STOP."),
  ("Mesurez les réponses, pas les envois.", "Sur ce test de 10 établissements [résultats], calcule le taux de réponse, liste les objections reçues et propose la relance à J+3 à me soumettre avant envoi.", "Une décision chiffrée : élargir, ajuster ou arrêter.", "Élargir avant d'avoir mesuré le premier test."),
 ]}

E["une-ecole-pour-ses-agents-ia"] = {
 "objectifs": ["Transformer vos procédures en missions de formation pour vos agents", "Donner à Claude une mémoire validée au lieu d'une mémoire subie", "Mesurer une routine avant de lui faire confiance"],
 "prerequis": ["Au moins une procédure métier écrite", "Un espace de formation connecté à Claude par MCP"],
 "etapes": [
  ("Une mission = une procédure réelle + une règle d'accord humain + un quiz.", None, "Une mission avec son objectif, ses outils autorisés et 3 questions de quiz.", "Écrire une mission théorique que personne n'applique."),
  ("Claude lit la mission au moment de l'appliquer : pas besoin de tout lui répéter.", "Connecte-toi à l'espace de formation, liste les missions disponibles et résume la procédure de [mission] en 5 étapes, avec la règle d'accord humain.", "Claude retrouve et applique la bonne procédure.", "Copier les procédures dans chaque conversation : elles divergent vite."),
  ("Seul un responsable valide le savoir d'équipe ; le reste reste personnel.", "Voici une correction que je t'ai faite [correction]. Propose de la retenir comme préférence personnelle ou comme savoir d'équipe, et montre-moi le texte exact avant de l'enregistrer.", "Une note de mémoire relue avant enregistrement.", "Croire que le modèle « apprend » : il relit des notes, rien de plus."),
  ("Un agent spécialisé a un objectif chiffré : sans chiffre, impossible de dire s'il travaille bien.", "Pour chaque agent [liste], écris son rôle, ses outils autorisés, son objectif mesurable et ce qu'il ne doit jamais faire.", "Une fiche par agent, avec ses limites.", "Donner les mêmes outils à tous les agents."),
  ("Une routine non mesurée ne passe jamais en production.", None, "Une routine notée sur 6 et un verdict après 14 jours.", "Juger une routine sur une seule exécution réussie."),
 ]}

E["lovable-claude-developper-ses-mcp"] = {
 "objectifs": ["Explorer un projet Lovable depuis Claude sans rien modifier", "Concevoir les outils MCP à partir du besoin métier", "Tester un serveur MCP en lecture et en refus"],
 "prerequis": ["Un compte Lovable avec au moins un projet", "Claude avec le connecteur Lovable activé"],
 "etapes": [
  ("Demandez toujours une exploration en lecture seule avant toute modification.", None, "Une description de l'architecture du projet et de son MCP.", "Laisser l'agent modifier le projet dès la première demande."),
  ("Partez de ce que l'agent doit faire, pas des tables de la base.", None, "Une liste d'outils justifiée par des tâches réelles.", "Exposer toute la base de données « au cas où »."),
  ("La description de l'outil est écrite pour le modèle : elle dit quand l'utiliser et quand ne pas l'utiliser.", "Écris l'outil MCP [nom] dans son propre fichier : description pour le modèle, paramètres typés avec Zod, annotations lecture seule et idempotent, réponse structurée.", "Un outil autonome, lisible et testable.", "Mettre plusieurs actions dans un seul outil fourre-tout."),
  ("Le jeton de l'utilisateur est transmis à la base : ce sont ses droits qui s'appliquent.", "Vérifie que chaque outil d'écriture de ce serveur MCP contrôle l'authentification et transmet le jeton de l'utilisateur à la base, pour que les règles RLS s'appliquent. Liste les outils qui ne le font pas.", "Des écritures qui respectent les droits de chaque utilisateur.", "Utiliser une clé administrateur côté serveur pour tous les appels."),
  ("Le test de refus est aussi important que le test de lecture.", "Appelle l'outil [outil] en lecture et montre la réponse, puis appelle le même serveur sans jeton et confirme qu'il répond 401.", "Deux preuves : lecture réussie et refus sans jeton.", "Ne tester que le cas qui marche."),
  ("Gardez deux connexions séparées : l'une pour développer, l'autre pour travailler.", "Dessine les deux connexions de mon projet : celle qui sert à développer (Claude Code et connecteur Lovable) et celle qui sert à travailler (Claude et MCP métier). Indique les droits de chacune.", "Un schéma clair des deux usages et de leurs droits.", "Donner à l'agent de travail les droits du développeur."),
 ]}

E["piloter-equipes-et-agents-avec-rapidorh"] = {
 "objectifs": ["Structurer projets, tâches et équipes dans un seul outil", "Faire préparer le plan du jour par Claude à partir des vraies tâches", "Ajouter une routine quotidienne avec un orchestrateur"],
 "prerequis": ["Un compte RapidoRH avec des projets", "Claude connecté au MCP RapidoRH"],
 "etapes": [
  ("Une tâche sans responsable ni date n'avance pas : complétez-les avant de demander un plan à Claude.", "Liste les tâches de mes projets qui n'ont pas de responsable, pas de date ou pas de priorité, sans rien modifier.", "Des projets propres : responsable, dates, priorités.", "Demander un plan du jour sur des tâches incomplètes."),
  ("Commencez par les rôles minimum, élargissez seulement si besoin.", "Propose les rôles et les permissions de mon équipe [équipe] : qui voit quoi, qui modifie quoi. Applique le principe du moindre accès.", "Une matrice rôles × permissions validée.", "Donner les droits d'administrateur à tout le monde."),
  ("Claude lit les tâches réelles : son plan est daté et nominatif.", None, "Le plan du jour par personne, avec les urgences en tête.", "Laisser Claude réattribuer les tâches sans vous le montrer."),
  ("L'aperçu montre exactement ce qui sera créé : relisez-le.", "Prépare la création de ces tâches [tâches] dans le projet [projet] : montre-moi l'aperçu complet (titre, responsable, échéance, priorité) et attends mon accord.", "Des tâches créées seulement après votre accord.", "Accepter un aperçu sans le lire."),
  ("RapidoRH ne se déclenche pas seul : c'est l'orchestrateur qui lance la routine.", "Écris la routine quotidienne de 8 h : lire les tâches urgentes et en retard dans RapidoRH, préparer le plan du jour, me l'envoyer pour validation. Indique l'orchestrateur utilisé et le critère d'arrêt.", "Une routine planifiée avec son objectif et sa limite.", "Croire que l'outil métier exécute la routine tout seul."),
 ]}
