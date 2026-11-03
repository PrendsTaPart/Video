# Enrichissement des formations 9 à 16.
E = {}

E["application-client-connectee"] = {
 "objectifs": ["Cadrer une application client à partir de son support existant", "Construire et connecter l'application aux données métier", "Livrer des documents au design de la maquette et tester sans toucher la production"],
 "prerequis": ["Le support actuel du client (classeur, fichiers, procédures)", "Un compte Lovable et l'accès en lecture aux données métier"],
 "etapes": [
  ("Comptez les contenus réels (fiches, catégories, allergènes) : ils fixent la structure de l'application.", "Voici le sommaire du support actuel [sommaire]. Fais l'inventaire : nombre de fiches par catégorie, champs présents sur chaque fiche, informations manquantes. Propose la structure de données de l'application.", "Un inventaire chiffré et une structure de données validée par le client.", "Dessiner les écrans avant de connaître le contenu."),
  ("Pensez à l'usage réel : mains occupées, lecture à distance, rush du service.", None, "Une application tactile utilisable au comptoir.", "Concevoir pour un bureau alors qu'on l'utilise debout, en plein service."),
  ("L'application lit les données ; elle n'affiche ni prix ni coûts si ce n'est pas son rôle.", "Connecte l'application aux recettes du logiciel métier par MCP, en lecture seule. Affiche ingrédients, quantités et allergènes ; n'affiche ni prix ni coûts.", "Des fiches toujours à jour, sans double saisie.", "Recopier les données à la main : elles divergent dès la première modification."),
  ("Le modèle Figma est la référence : les PDF générés doivent lui ressembler au pixel près.", "Génère dans le navigateur la fiche PDF de [recette] au design de la maquette Figma [lien] : mêmes marges, mêmes polices, mêmes couleurs.", "Des fiches PDF fidèles à la maquette, générées à la demande.", "Refaire la mise en page à la main pour chaque fiche."),
  ("Le banc de test reproduit la production avec des données fictives.", "Crée un banc de test avec des données simulées et des tests de bout en bout pour les parcours principaux. Vérifie qu'aucun test n'appelle la production.", "Des tests verts sans aucune donnée de production touchée.", "Tester directement sur les données du client."),
 ]}

E["automatiser-ses-chaines-youtube"] = {
 "objectifs": ["Centraliser plusieurs chaînes YouTube dans une seule interface", "Faire préparer titres, créneaux et analyses par vos agents", "Respecter les quotas et garder la main sur la publication"],
 "prerequis": ["Au moins une chaîne YouTube connectée", "Claude connecté au MCP YouTube"],
 "etapes": [
  ("Une interface unique évite de publier deux fois la même vidéo sur deux chaînes.", "Liste mes chaînes YouTube, leur nombre de vidéos et les 5 dernières publications de chacune, sans rien modifier.", "Une vue d'ensemble de toutes vos chaînes.", "Gérer chaque chaîne dans un onglet différent."),
  ("Commencez par la lecture : titres, descriptions, statistiques.", None, "Des propositions de titres basées sur vos vidéos réelles.", "Laisser l'agent modifier les métadonnées sans relecture."),
  ("Les créneaux viennent de l'historique de la chaîne, pas d'une règle générale.", "À partir de l'historique de [chaîne], propose les 5 meilleurs créneaux de la semaine prochaine et explique sur quelles données tu t'appuies. Ne programme rien.", "Des créneaux justifiés par vos propres chiffres.", "Appliquer un horaire « idéal » trouvé sur Internet."),
  ("Comparez des vidéos comparables : même format, même durée.", "Compare mes 10 derniers Shorts : vues, rétention, interactions. Dégage 3 enseignements et une action pour la prochaine vidéo.", "3 décisions concrètes pour les prochaines vidéos.", "Tirer des conclusions sur une seule vidéo."),
  ("Vérifiez le quota avant une série d'envois : un envoi en consomme une grosse part.", "Vérifie le quota restant de l'API YouTube aujourd'hui et dis-moi combien d'envois je peux faire avant d'atteindre la limite.", "Des envois planifiés sans blocage en cours de journée.", "Lancer une série d'envois et tomber à court de quota au milieu."),
 ]}

E["un-an-de-videos-en-deux-jours"] = {
 "objectifs": ["Définir des séries avec une promesse et un public", "Écrire un catalogue d'épisodes exploitable par une équipe de production", "Suivre l'avancement réel sans confondre écrit et produit"],
 "prerequis": ["Une ligne éditoriale (thèmes, cible)", "Un outil de suivi : tableur ou application"],
 "etapes": [
  ("Une série = une promesse que chaque épisode tient.", "Propose 5 séries pour [entreprise] : nom, promesse en une phrase, public, format et fréquence. Une série doit pouvoir tenir 30 épisodes.", "Quelques séries claires, chacune avec sa promesse.", "Une seule série fourre-tout qui parle de tout."),
  ("L'accroche se lit en une seconde : 8 mots maximum.", None, "Un catalogue d'épisodes prêt à être produit.", "Écrire des titres sans accroche ni message à retenir."),
  ("Chaque étape de production a un statut et un responsable.", "Transforme ce catalogue [catalogue] en tableau de production : épisode, étape (scénario, images, voix, montage), statut (à produire, monté, bloqué), responsable, date prévue.", "Un tableau de production où chaque épisode a un statut.", "Suivre la production de mémoire."),
  ("Comptez ce qui est monté, pas ce qui est écrit.", "À partir de ce tableau [tableau], compte les épisodes au catalogue, montés, à produire et bloqués, et liste les raisons des blocages.", "Un état d'avancement honnête.", "Annoncer « 365 vidéos » quand elles ne sont qu'écrites."),
  ("Gardez du temps chaque semaine pour choisir les sujets : c'est là que se fait la qualité.", "Parmi ces épisodes [liste], classe les 10 plus utiles pour ma cible ce mois-ci et explique pourquoi.", "Un ordre de production qui sert vos objectifs.", "Produire dans l'ordre d'écriture au lieu de l'ordre d'importance."),
 ]}

E["bd-et-documentation-avec-figma-et-claude"] = {
 "objectifs": ["Faire travailler Claude directement dans un fichier Figma", "Écrire une BD et une documentation qui expliquent le logiciel", "Assembler un document cohérent en respectant les droits d'image"],
 "prerequis": ["Un compte Figma et le connecteur Figma dans Claude", "Les captures d'écran du logiciel à documenter"],
 "etapes": [
  ("N'utilisez que des images autorisées : vos captures, vos illustrations, votre bibliothèque.", "Liste les images disponibles dans la bibliothèque autorisée et dans le fichier Figma [fichier], avec leur source. Signale celles dont l'origine est inconnue.", "Une bibliothèque d'images dont chaque source est connue.", "Récupérer des images sur Internet sans en connaître les droits."),
  ("Une planche = une idée ; le personnage vit la situation de votre client.", None, "Un scénario découpé en planches et en bulles.", "Faire une BD publicitaire au lieu de raconter une vraie situation."),
  ("La documentation suit le geste de l'utilisateur, écran par écran.", None, "Une page de documentation par écran, avec ses erreurs fréquentes.", "Documenter les menus au lieu des tâches."),
  ("Un gabarit par type de page garantit la cohérence sur des dizaines de pages.", "Crée dans Figma les gabarits A4 du document : couverture, planche de BD, page de documentation, atlas des écrans, catalogue de prompts. Utilise les couleurs et la police de la charte.", "Un document assemblé à partir de gabarits communs.", "Mettre en page chaque page différemment."),
  ("En cas de doute sur un droit d'image, on retire.", "Passe en revue toutes les images du document et liste celles qui montrent un client, une marque tierce ou une personne identifiable. Propose de les remplacer ou de les retirer.", "Un document sans image non autorisée.", "Garder une image d'un client parce qu'elle est belle."),
 ]}

E["construire-avec-braindcode-build"] = {
 "objectifs": ["Choisir une idée d'application et récupérer tout son contexte", "Avancer étape par étape avec Claude Code et Lovable", "Savoir quand passer la main à un humain"],
 "prerequis": ["Un compte BraindCode Build", "Claude Code et un compte Lovable"],
 "etapes": [
  ("Choisissez une idée liée à un logiciel que vous connaissez : vous testerez mieux.", "Liste les idées disponibles dans le catalogue BraindCode Build autour de [logiciel], avec leur statut. Propose les 3 plus adaptées à mon profil [profil].", "Une idée choisie, avec son logiciel de référence.", "Choisir l'idée la plus ambitieuse pour un premier projet."),
  ("Le contexte contient déjà la charte, le cahier des charges et les prompts : lisez-le avant de coder.", "Récupère le contexte complet du projet [idée] : cahier des charges, charte, connexions MCP, prompts Lovable, Figma et Claude Code. Résume-le en une page.", "Une page de synthèse qui sert de référence pendant tout le projet.", "Commencer à coder sans lire le cahier des charges."),
  ("Une étape à la fois : on démarre, on exécute, on valide, puis on passe à la suivante.", "Montre-moi le plan d'exécution du projet, démarre la première étape et exécute son prompt dans Lovable. Arrête-toi avant de la valider.", "Des étapes terminées et validées une par une.", "Enchaîner toutes les étapes sans vérifier le résultat."),
  ("Tout ce qui touche à un secret ou à l'argent passe par un humain.", "Liste les étapes du projet qui demandent une connexion OAuth, une clé, un paiement ou une mise en ligne, et prépare la demande de validation humaine pour chacune.", "Des demandes de validation claires, sans aucun secret qui transite.", "Coller une clé d'API dans la conversation."),
  ("Avant de publier, vérifiez la liste de contrôle de publication.", "Vérifie si le projet est prêt à être publié et liste ce qui manque. Prépare ensuite un pitch de 2 minutes pour le demoday.", "Un projet publié et un pitch prêt.", "Publier une idée « à construire » comme une application terminée."),
 ]}

E["controle-qualite-de-ses-mcp"] = {
 "objectifs": ["Écrire des scénarios de test pour vos outils MCP", "Transformer chaque échec en ticket avec preuves et prompt de débogage", "Rejouer jusqu'au vert avant toute mise en production"],
 "prerequis": ["Un serveur MCP ou une API à tester", "Claude Code pour corriger"],
 "etapes": [
  ("Testez aussi les cas d'erreur : paramètre manquant, droit insuffisant, valeur hors limite.", None, "Une série de scénarios couvrant cas normaux et cas d'erreur.", "Ne tester que les cas où tout fonctionne."),
  ("Une preuve = la requête exacte et la réponse exacte, horodatées.", "Pour chaque scénario exécuté, enregistre la requête, la réponse, la durée et le verdict. Masque les jetons et les données personnelles dans les preuves.", "Un historique de preuves exploitable par un développeur.", "Garder des preuves qui contiennent des secrets."),
  ("Le ticket doit permettre de reproduire le bug sans vous.", None, "Un ticket complet, prêt pour Claude Code.", "Écrire « ça ne marche pas » sans les preuves."),
  ("Après chaque correction, relancez toute la série : une correction peut casser autre chose.", "Relance tous les scénarios après la correction de [ticket] et compare avec la dernière exécution : ce qui est réparé, ce qui reste en échec, ce qui a régressé.", "Une série entièrement verte, régressions comprises.", "Relancer seulement le test corrigé."),
  ("La décision de mise en production reste humaine, preuves à l'appui.", "Prépare la note de mise en production : tests passés, tickets fermés, risques restants. Ne déploie rien.", "Une décision de mise en production documentée.", "Déployer automatiquement dès que les tests passent."),
 ]}

E["piloter-son-crm-depuis-claude"] = {
 "objectifs": ["Faire votre point commercial du matin avec Claude", "Préparer relances et prospection en brouillon", "Lire des chiffres justes en excluant les données de test"],
 "prerequis": ["Un compte RapidoCRM avec des données", "Claude connecté au MCP RapidoCRM"],
 "etapes": [
  ("Vérifiez d'abord ce que le MCP sait lire : pipeline, rendez-vous, devis, factures.", "Liste les outils RapidoCRM disponibles, en distinguant lecture et écriture, et lis le nombre de prospects par étape du pipeline.", "Claude lit votre CRM et vous montre ses droits.", "Utiliser un compte avec tous les droits pour un simple point du matin."),
  ("Le même point chaque matin permet de voir les tendances.", None, "Un point du matin en 5 lignes, à la même heure chaque jour.", "Demander un point différent chaque jour : impossible de comparer."),
  ("Les entrées de test faussent les chiffres : excluez-les avant toute lecture.", "Repère dans le CRM les entrées qui ressemblent à des tests (noms « test », emails factices, montants à zéro) et recalcule les indicateurs sans elles. Ne supprime rien.", "Des indicateurs calculés sur les seules données réelles.", "Annoncer un chiffre qui compte des fiches de test."),
  ("Montant et date viennent du CRM, jamais de la mémoire du modèle.", None, "Des relances prêtes en brouillon, montants vérifiés.", "Envoyer une relance avec un mauvais montant."),
  ("Un segment = une offre adaptée ; on prospecte un segment à la fois.", "Propose 3 segments à prospecter cette semaine à partir de mes clients actuels. Pour chacun, cherche 10 entreprises et prépare leur ajout au pipeline, sans les ajouter.", "Des prospects ajoutés au pipeline après votre accord.", "Ajouter des centaines de fiches non qualifiées."),
 ]}

E["former-ses-clients-avec-un-mcp-pedagogique"] = {
 "objectifs": ["Structurer un catalogue de tutoriels exploitable par une IA", "Exposer ce catalogue à Claude et ChatGPT en lecture seule", "Repérer les tutoriels à tourner grâce aux questions sans réponse"],
 "prerequis": ["Des tutoriels vidéo ou écrits sur votre logiciel", "Un projet capable d'exposer un serveur MCP"],
 "etapes": [
  ("Une fiche par geste, pas par menu : le client cherche « comment faire ».", "Transforme cette liste de tutoriels [liste] en fiches : titre orienté action, durée, étapes, écran concerné, niveau. Signale les doublons.", "Un catalogue de fiches homogènes.", "Faire des tutoriels de 20 minutes qui couvrent tout un module."),
  ("Un serveur pédagogique n'a aucun outil d'écriture : il enseigne, il n'agit pas.", "Conçois les outils d'un serveur MCP en lecture seule pour ce catalogue : rechercher, obtenir une fiche, proposer un parcours, quiz. Aucun outil ne doit modifier un compte client.", "Un serveur qui répond sans jamais toucher aux données des clients.", "Mélanger formation et actions sur le compte dans le même serveur."),
  ("La réponse cite toujours le tutoriel source, avec son lien.", None, "Une réponse qui renvoie vers le bon tutoriel.", "Laisser l'IA inventer une marche à suivre absente du catalogue."),
  ("Un parcours tient dans le temps disponible du client.", None, "Des parcours courts, adaptés au métier et au niveau.", "Proposer tout le catalogue d'un coup."),
  ("Chaque question sans réponse est un tutoriel à produire.", "Liste les questions de la semaine auxquelles aucun tutoriel ne répondait, regroupe-les par thème et propose les 5 prochains tutoriels à tourner.", "Une liste priorisée des prochains tutoriels.", "Ignorer les questions sans réponse."),
 ]}
