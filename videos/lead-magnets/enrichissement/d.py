# Enrichissement des formations 25 à 31.
E = {}

E["un-presentateur-ia-pour-ses-logiciels"] = {
 "objectifs": ["Construire une démonstration de logiciel présentée par un avatar", "Filmer une seule fois et découper automatiquement par scène", "Répondre aux questions des prospects à partir du script"],
 "prerequis": ["Un logiciel à présenter et un enregistreur d'écran", "Une voix de synthèse autorisée"],
 "etapes": [
  ("Chaque scène montre une action réelle du logiciel, dans l'ordre d'usage du client.", None, "Un storyboard scène par scène, prêt à filmer.", "Montrer toutes les fonctions au lieu du parcours du client."),
  ("Suivez le storyboard à la lettre pendant l'enregistrement : le découpage s'appuie dessus.", "Découpe cet enregistrement [fichier] selon le storyboard : début et fin de chaque scène, et signale les scènes manquantes ou trop longues.", "Un enregistrement découpé, une séquence par scène.", "Improviser pendant l'enregistrement : le découpage ne correspond plus."),
  ("Une langue par version : on ne mélange pas dans la même démo.", "Génère le texte de l'avatar pour chaque scène en [langue], au même rythme que la séquence filmée, en 2 phrases maximum par scène.", "Une démonstration présentée par l'avatar, dans la langue choisie.", "Traduire mot à mot sans adapter au rythme des images."),
  ("L'assistant répond seulement à partir du script et renvoie au bon passage.", "Voici la question d'un prospect [question]. Réponds uniquement à partir du script de la démo, cite la scène concernée, et dis-le clairement si la réponse n'est pas dans le script.", "Des réponses fiables, reliées au bon passage.", "Laisser l'assistant inventer une fonction absente du logiciel."),
  ("Une question sans réponse = un tutoriel ou une scène à ajouter.", "Regroupe les questions sans réponse de la semaine par thème et propose les scènes ou tutoriels à ajouter.", "La liste priorisée des prochains contenus.", "Ignorer les questions qui n'ont pas trouvé de réponse."),
 ]}

E["studio-ia-pour-sa-passion"] = {
 "objectifs": ["Brancher une source de données à un workflow d'analyse", "Organiser une équipe d'agents qui produit des contenus vérifiés", "Ne publier qu'après validation, sans promesse de résultat"],
 "prerequis": ["Un compte n8n et une source de données (API)", "Claude Code pour créer les agents"],
 "etapes": [
  ("La clé de l'API reste dans les identifiants de n8n, jamais dans le workflow.", "Crée un workflow n8n qui récupère [données] depuis l'API, avec la clé stockée dans les identifiants de n8n. Vérifie qu'aucune clé n'apparaît en clair dans le workflow.", "Des données à jour, sans clé en clair.", "Coller la clé d'API dans un nœud du workflow."),
  ("Une analyse est une estimation : présentez-la comme incertaine.", "À partir de ces données [données], propose une analyse avec un niveau de confiance et ses limites. Pas de promesse de résultat.", "Une analyse présentée avec son incertitude.", "Présenter un pronostic comme une certitude."),
  ("Les visuels suivent un gabarit fixe : seuls les contenus changent.", "Crée le gabarit des visuels de début et de fin : zones de texte, logo en fichier, couleurs. Le workflow ne remplit que les zones prévues.", "Des visuels cohérents d'un épisode à l'autre.", "Générer un visuel différent à chaque fois."),
  ("Le vérificateur légal peut bloquer : c'est sa raison d'être.", None, "Une équipe d'agents où chaque contenu est vérifié avant publication.", "Donner au vérificateur un simple rôle consultatif."),
  ("Le CMS reçoit des brouillons ; la publication reste manuelle.", "Envoie la capsule validée dans le CMS en brouillon, avec sa légende et ses mentions. Ne programme rien.", "Des brouillons prêts, publiés seulement par vous.", "Publier automatiquement dès que la capsule est prête."),
 ]}

E["de-n8n-aux-serveurs-mcp"] = {
 "objectifs": ["Cartographier vos workflows et repérer les connexions en double", "Exposer chaque logiciel une seule fois en MCP", "Garder n8n pour orchestrer, avec des webhooks sécurisés"],
 "prerequis": ["Un compte n8n avec des workflows existants", "Des logiciels qui exposent (ou peuvent exposer) un serveur MCP"],
 "etapes": [
  ("Comptez les connexions point à point : chacune est une maintenance.", None, "Une carte de vos workflows et de leurs connexions.", "Ajouter un workflow sans regarder ceux qui existent déjà."),
  ("Un serveur MCP par logiciel, partagé par tous les agents.", "Pour chaque logiciel de cette liste [liste], indique s'il expose déjà un serveur MCP et quels workflows il pourrait remplacer.", "Une liste de logiciels exposés en MCP et des workflows simplifiés.", "Créer un connecteur différent par agent."),
  ("n8n déclenche et enchaîne ; les agents raisonnent ; les MCP donnent accès.", "Pour ce workflow [workflow], sépare ce qui relève de l'orchestration (déclencheur, enchaînement) et ce qui peut passer par un agent et un MCP.", "Des rôles clairs entre n8n, agents et MCP.", "Mettre toute la logique métier dans les nœuds n8n."),
  ("La routine enregistre son résultat : sinon on ne sait pas si elle a tourné.", "Écris la routine : n8n lit les tâches RapidoRH par MCP chaque matin, un agent les traite, le résultat est enregistré avec la date et le statut.", "Une routine tracée, avec son résultat enregistré.", "Une routine qui tourne sans laisser de trace."),
  ("Surveillez les échecs : un jeton expiré casse un workflow en silence.", "Liste mes webhooks n8n, indique ceux qui n'ont pas d'authentification et propose la protection à ajouter. Signale les workflows en erreur ces 7 derniers jours.", "Des webhooks authentifiés et les erreurs repérées.", "Laisser un webhook ouvert à n'importe qui."),
 ]}

E["departement-de-prospection-ia"] = {
 "objectifs": ["Découper la prospection en fonctions automatisables", "Confier à chaque agent ses seuls outils, tout centralisé dans le CRM", "Mesurer ce qui compte : réponses, rendez-vous, ventes"],
 "prerequis": ["Un CRM avec un pipeline de prospection", "Un compte n8n"],
 "etapes": [
  ("Chaque étape a une entrée, une sortie et un responsable.", "Découpe mon processus de prospection [processus] en étapes : recherche, enrichissement, campagnes, suivi. Pour chacune : entrée, sortie, responsable humain ou agent.", "Un processus découpé en étapes claires.", "Automatiser un processus qui n'est pas encore défini."),
  ("Un workflow par fonction : en cas de panne, on sait laquelle.", "Propose un workflow n8n par fonction (orchestrateur, enrichissement, détection des réponses, relances, rapport quotidien) avec son déclencheur et sa sortie.", "Des workflows séparés, faciles à surveiller.", "Un seul workflow géant que personne ne peut déboguer."),
  ("L'agent prépare l'ajout au pipeline ; vous validez les envois.", None, "Des agents qui ajoutent des prospects qualifiés, sans rien envoyer seuls.", "Laisser l'agent contacter les prospects qu'il vient de trouver."),
  ("Un seul pipeline : toutes les sources y arrivent avec leur origine.", "Vérifie que chaque prospect du pipeline a sa source, son étape et sa prochaine action. Liste les fiches incomplètes.", "Un pipeline unique et complet.", "Garder des listes de prospects dans des fichiers à côté du CRM."),
  ("Un workflow qui réussit ne prouve pas qu'il rapporte.", "Fais le rapport de la semaine : réponses, rendez-vous, ventes, par source. Ne compte pas les exécutions de workflows comme des résultats.", "Un rapport centré sur les résultats commerciaux.", "Se féliciter du taux de réussite des workflows."),
 ]}

E["equipe-ia-pour-son-seo"] = {
 "objectifs": ["Repérer les vraies questions de vos clients et les mots-clés associés", "Produire des articles utiles à partir de votre propre documentation", "Piloter le site et ne publier qu'après relecture"],
 "prerequis": ["Un site et un accès à la Search Console", "Votre documentation ou vos tutoriels"],
 "etapes": [
  ("Gardez seulement les tendances liées à votre métier.", "Surveille les tendances de la semaine sur [thème] et garde seulement celles qui concernent mes clients [cible]. Pour chacune, indique la question qu'elles posent.", "Une liste de questions d'actualité pour vos clients.", "Courir après chaque tendance, même hors sujet."),
  ("Partez des requêtes qui vous apportent déjà des visites.", "À partir de la Search Console, liste les requêtes pour lesquelles mon site apparaît sans être cliqué, et propose l'article ou la mise à jour qui y répondrait.", "Une liste de mots-clés à travailler en priorité.", "Viser des mots-clés trop génériques."),
  ("Un article répond à une seule question, avec vos captures et vos exemples réels.", None, "Des articles utiles, fondés sur votre documentation.", "Produire des articles en masse sans réponse précise."),
  ("Les contrôles avant publication sont les mêmes pour chaque article.", "Vérifie cet article [article] avant publication : mot-clé principal, titre, description, liens internes, images avec texte alternatif, sources citées. Liste ce qui manque.", "Des articles qui passent tous les mêmes contrôles.", "Publier sans relecture humaine."),
  ("Mesurez 4 semaines après la publication, puis ajustez.", "Compare les positions et les clics des articles publiés il y a 4 semaines et propose les mises à jour à faire.", "Un cycle publier, mesurer, améliorer.", "Ne jamais revenir sur un article publié."),
 ]}

E["commercial-ia-en-un-prompt"] = {
 "objectifs": ["Écrire un prompt d'objectif commercial complet", "Laisser Claude rechercher, qualifier et segmenter dans le CRM", "Préparer rendez-vous, devis et relances avec traçabilité"],
 "prerequis": ["Un compte RapidoCRM connecté à Claude ou ChatGPT", "Une offre et une cible définies"],
 "etapes": [
  ("Le prompt contient l'objectif, la cible, la règle d'accord et le format du rendu.", None, "Un objectif commercial compris et découpé par l'assistant.", "Oublier la règle « présente-moi les actions avant de les exécuter »."),
  ("Vérifiez quelques fiches à la main : les informations publiques changent.", "Recherche 20 [type d'établissement] à [ville], retrouve leurs informations publiques et prépare leur enregistrement dans le CRM. Montre-moi la liste avant d'enregistrer.", "Des fiches enregistrées après votre accord.", "Enregistrer sans vérifier les doublons."),
  ("Un segment = un message adapté.", "Classe ces prospects [liste] par segment (restauration rapide, bar et brasserie, traiteur, chaînes et franchises) et propose l'argument principal pour chaque segment.", "Des segments avec leur argument propre.", "Envoyer le même message à tous les segments."),
  ("Chaque action préparée est tracée dans le CRM avec sa date.", "Pour les prospects qualifiés, prépare en brouillon les prochaines actions : demande de rendez-vous, devis ou relance, avec leur date. N'envoie rien.", "Des actions prêtes, tracées, en attente de validation.", "Envoyer un devis sans validation."),
  ("Un agent vocal n'appelle personne tant que son numéro et son cadre ne sont pas validés.", "Liste ce qu'il faut valider avant qu'un agent vocal appelle des prospects : numéro, script, consentement, horaires, cadre légal. Ne lance aucun appel.", "Une liste de validations à faire avant tout appel.", "Lancer des appels automatiques sans validation juridique."),
 ]}

E["site-lien-en-bio-avec-lovable-et-claude"] = {
 "objectifs": ["Construire un site lien-en-bio avec vidéos, projets, rendez-vous et formations à débloquer", "Reprendre le projet Lovable dans Claude Code et le mettre en production", "Donner au site un MCP pour que Claude le tienne à jour avec vous"],
 "prerequis": ["Un compte Lovable relié à GitHub", "Claude Code", "Vos contenus : vidéos, projets, liens"],
 "etapes": [
  ("Notez en une phrase ce que le visiteur doit faire en arrivant.", None, "Une structure de page validée avant toute génération.", "Mettre dix boutons de même importance."),
  ("Relisez l'aperçu Lovable sur mobile : c'est là que viendront vos visiteurs.", None, "Un site de base en ligne, avec son administration.", "Valider sur ordinateur seulement."),
  ("Lisez AGENTS.md : il donne les règles du projet à respecter.", None, "Un état des lieux du projet, sans modification.", "Réécrire l'historique Git : Lovable perd sa synchronisation."),
  ("Le contenu complet passe par des fonctions sécurisées, jamais par une lecture directe de la table.", None, "Des formations à débloquer, testées contre la lecture directe.", "Rendre la table des formations lisible par tous."),
  ("Toute création passe par un brouillon : l'agent ne publie jamais seul.", None, "Un serveur MCP protégé par OAuth et journalisé.", "Donner à l'agent un outil de suppression définitive."),
  ("= Logos et écrans officiels viennent de la bibliothèque de marque ; chaque formation porte la charte graphique de son logiciel. Tout écran qui montre un prix ou une remise est écarté. Les prompts s'affichent comme une conversation, avec un bouton pour les ouvrir dans Claude.", None, "Un site aux vraies couleurs de vos marques, sans logo redessiné.", "Redessiner un logo ou générer un faux écran."),
  ("Après chaque synchronisation Lovable, vérifiez que vos fichiers sont toujours là.", None, "Un site vérifié en ligne, page par page.", "Croire qu'un déploiement réussi veut dire que tout est en ligne."),
 ]}
