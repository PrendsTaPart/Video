# Enrichissement des formations 17 à 24.
E = {}

E["transformer-ses-posts-en-clients"] = {
 "objectifs": ["Relier vos publications à un formulaire qui crée de vrais contacts", "Suivre chaque demande jusqu'à l'opportunité dans le CRM", "Boucler sur les résultats pour préparer la campagne suivante"],
 "prerequis": ["Un compte RapidoCMS et un compte RapidoCRM", "Une offre avec un appel à l'action clair (démo, rendez-vous)"],
 "etapes": [
  ("Chaque publication a un seul appel à l'action et un lien suivi par source.", None, "Des brouillons de publications, chacun avec son lien suivi.", "Publier sans appel à l'action : on obtient des likes, pas des contacts."),
  ("Le formulaire demande le minimum et recueille un consentement explicite.", "Écris le formulaire de demande de démo : 5 champs maximum, case de consentement non cochée par défaut, lien vers la politique de confidentialité, et la source de la visite enregistrée.", "Un formulaire qui crée un contact consentant, avec sa source.", "Ajouter le contact à une liste d'emailing sans son accord."),
  ("Chaque demande devient une fiche, puis une opportunité si elle est qualifiée.", "Liste les demandes reçues cette semaine dans RapidoCRM avec leur source et leur étape. Propose la prochaine action pour chacune, sans rien envoyer.", "Un pipeline où chaque demande a sa prochaine action.", "Laisser une demande sans réponse plus de 48 h."),
  ("Comparez les publications par demandes générées, pas par vues.", None, "La prochaine campagne fondée sur ce qui a vraiment converti.", "Refaire la campagne la plus vue au lieu de celle qui a rapporté des demandes."),
 ]}

E["diriger-ses-agents-avec-planit"] = {
 "objectifs": ["Formuler un objectif qu'un orchestrateur peut découper", "Transformer cet objectif en tâches et routines avec leur coût affiché", "Garder la validation sur toutes les actions sensibles"],
 "prerequis": ["Un compte Plan'It", "Les logiciels à piloter connectés par MCP"],
 "etapes": [
  ("Un bon objectif contient un verbe, un résultat chiffré et une échéance.", None, "Un objectif daté et mesurable, compris par l'orchestrateur.", "Donner un thème (« le marketing ») au lieu d'un objectif."),
  ("Vérifiez la liste des outils proposés avant d'accepter le plan.", "Pour cet objectif [objectif], propose les serveurs MCP et les outils à utiliser, en expliquant pourquoi chacun. N'exécute rien.", "Un plan d'outils justifié, relu avant exécution.", "Accepter un plan qui utilise un logiciel sans rapport avec l'objectif."),
  ("Une tâche ponctuelle reste une tâche ; seule une action répétée devient une routine.", "Transforme ce plan en tâches ponctuelles et en routines. Pour chacune, affiche le coût estimé, la fréquence et le critère d'arrêt.", "Des tâches et des routines avec leur coût connu à l'avance.", "Créer une routine pour une action qui n'a lieu qu'une fois."),
  ("La liste des actions sensibles est la même pour tous les agents.", "Liste les actions de ce plan qui envoient, publient, suppriment ou paient. Pour chacune, indique qui valide et comment.", "Une liste d'actions bloquées jusqu'à votre accord.", "Découvrir après coup qu'un message est parti."),
  ("Consultez l'historique chaque semaine : c'est là qu'on voit ce qui sert vraiment.", "Résume l'avancement de la semaine : tâches terminées, routines exécutées, résultats, coûts réels, et ce qui doit être ajusté.", "Un point hebdomadaire sur les résultats et les coûts.", "Laisser tourner des routines que personne ne regarde."),
 ]}

E["site-client-pilote-par-l-ia"] = {
 "objectifs": ["Livrer un site client relié à ses outils métier", "Développer un MCP dédié pour que le client pilote son site avec l'IA", "Sécuriser et former le client à cet usage"],
 "prerequis": ["Un compte Lovable", "La charte et les contenus du client, ses outils métier"],
 "etapes": [
  ("Partez de la charte du client et des pages qu'il modifie le plus souvent.", "Crée le site de [client] avec Lovable : pages, événements, formulaires, aux couleurs de sa charte [charte]. Prévois un espace d'administration protégé.", "Un site conforme à la charte, avec son administration.", "Commencer par les effets visuels avant les contenus."),
  ("Les données viennent des outils métier : pas de double saisie.", "Relie la carte du site au logiciel de restauration en lecture, et envoie chaque demande du formulaire au CRM avec sa source. Montre-moi le parcours d'une demande.", "Un site toujours à jour et des demandes qui arrivent dans le CRM.", "Recopier la carte à la main dans le site."),
  ("Un outil par action courante du client : modifier une page, créer un événement, lire les demandes.", None, "Un serveur MCP que le client utilise depuis son assistant.", "Exposer des outils techniques que le client ne comprend pas."),
  ("Toute suppression demande une confirmation explicite et laisse une trace.", "Ajoute à chaque outil d'écriture un journal (qui, quoi, quand) et une confirmation obligatoire pour toute suppression. Écris le test qui le prouve.", "Un journal complet et des suppressions toujours confirmées.", "Permettre une suppression en un seul appel."),
  ("Montrez au client trois demandes types qu'il fera chaque semaine.", "Écris pour [client] un guide d'une page : comment connecter son assistant au MCP du site et 5 demandes types, avec ce qui exige sa confirmation.", "Un client autonome sur les modifications courantes.", "Livrer le MCP sans expliquer ce qu'on peut lui demander."),
 ]}

E["construire-son-equipe-d-employes-ia"] = {
 "objectifs": ["Fixer un objectif d'équipe et le répartir entre plusieurs agents", "Brancher chaque agent sur ses seuls outils", "Décider de garder, ajuster ou arrêter une routine après mesure"],
 "prerequis": ["Un orchestrateur (Plan'It) et vos logiciels connectés par MCP", "Un objectif commercial ou opérationnel réel"],
 "etapes": [
  ("L'objectif d'équipe est unique ; chaque agent en porte une partie mesurable.", "Reformule cet objectif [objectif] pour qu'il soit daté et mesurable, puis découpe-le en sous-objectifs, un par fonction.", "Un objectif d'équipe et ses sous-objectifs mesurables.", "Donner à chaque agent un objectif sans lien avec les autres."),
  ("Chaque rôle produit un livrable que le rôle suivant utilise.", None, "Une répartition des rôles où chaque livrable a un destinataire.", "Créer des agents qui font tous la même chose."),
  ("Moins d'outils = moins de risques et de meilleures décisions de l'agent.", "Pour chaque agent [liste], liste les outils MCP strictement nécessaires et ceux à lui retirer. Justifie chaque outil gardé.", "Des agents limités à leurs outils.", "Brancher tous les outils sur tous les agents."),
  ("Une routine sans critère d'arrêt tourne indéfiniment, même quand elle ne sert plus.", "Écris la routine de [agent] : objectif chiffré, sources, limite de ce qu'il peut faire, format du rendu, critère d'arrêt et accord humain requis.", "Des routines complètes, notées sur 6.", "Lancer une routine sans critère d'arrêt."),
  ("Le verdict se prend sur les mesures, pas sur l'impression.", "Après 3 exécutions et 14 jours, compare les résultats de cette routine à son objectif et propose un verdict : garder, ajuster ou arrêter, avec la raison.", "Un verdict par routine, appuyé sur des chiffres.", "Garder une routine parce qu'elle « a l'air utile »."),
 ]}

E["former-ses-employes-ia"] = {
 "objectifs": ["Choisir une mission précise et lui apprendre la bonne procédure", "Restreindre les outils de l'agent à cette mission", "Vérifier sa compréhension par un quiz et une consigne notée sur 6"],
 "prerequis": ["Une procédure métier écrite", "Un espace de formation et vos logiciels connectés par MCP"],
 "etapes": [
  ("Une mission précise se décrit en une phrase et se mesure.", "Propose 3 missions précises que je peux confier à un agent dans mon activité [activité]. Pour chacune : objectif, indicateur, risque principal.", "Une mission choisie, avec son indicateur.", "Confier « la gestion des stocks » au lieu d'« éviter les ruptures »."),
  ("La procédure s'arrête là où commence la décision humaine.", "Écris la procédure de la mission [mission] étape par étape, en marquant clairement l'étape où l'humain reprend la main.", "Une procédure en étapes, avec le point de reprise humain.", "Laisser l'agent aller jusqu'à l'envoi."),
  ("Retirez l'outil d'envoi : l'agent prépare, l'humain envoie.", "Liste les outils MCP dont cet agent a besoin pour [mission] et retire tous ceux qui envoient, publient ou paient.", "Un agent qui ne peut physiquement pas envoyer.", "Faire confiance à une consigne au lieu de retirer l'outil."),
  ("Le quiz vérifie que l'agent a compris la procédure, pas qu'il la récite.", "Fais passer le quiz de la mission [mission] à l'agent et montre-moi ses réponses et la correction du serveur.", "Un quiz réussi avant la première exécution réelle.", "Passer directement à l'exécution réelle sans vérifier."),
  ("Les 6 critères : objectif, sources, limite, rendu, critère d'arrêt, accord humain.", None, "Une consigne complète qui obtient 6/6.", "Lancer une consigne brute de deux lignes."),
 ]}

E["le-vrai-cout-d-une-equipe-ia"] = {
 "objectifs": ["Lister le coût réel de vos outils IA, abonnements et coûts cachés", "Repérer les outils redondants ou non connectés", "Lancer une première mission mesurée avant d'ajouter des abonnements"],
 "prerequis": ["La liste de vos abonnements actuels", "Vos factures des trois derniers mois"],
 "etapes": [
  ("Vérifiez chaque tarif sur le site de l'éditeur : ils changent souvent.", "Voici mes abonnements [liste avec montants]. Fais le total mensuel et annuel et signale ceux que je n'ai pas utilisés depuis un mois. Ne cite aucun tarif que je ne t'ai pas donné.", "Le total réel de vos abonnements, outil par outil.", "Reprendre des tarifs de mémoire ou d'une vidéo."),
  ("Le temps passé à configurer est un coût : estimez-le en heures.", "Liste les coûts cachés de mon équipe IA : temps de configuration, serveurs, appels d'API, maintenance. Pour chacun, dis-moi comment le mesurer.", "Une estimation complète, abonnements et coûts cachés.", "Ne compter que les abonnements."),
  ("Un outil non connecté coûte sans travailler pour vos agents.", None, "La liste des outils à connecter, garder ou résilier.", "Ajouter un abonnement pour chaque nouveau besoin."),
  ("La première mission doit rapporter plus que ce qu'elle coûte.", "Propose une première mission utile pour mon activité [activité], avec son coût estimé, le gain attendu et l'indicateur qui dira si elle vaut le coup.", "Une mission lancée avec son coût et son gain attendus.", "Élargir avant d'avoir mesuré la première mission."),
 ]}

E["transformer-ses-reunions-en-taches"] = {
 "objectifs": ["Transcrire une réunion et en extraire décisions et tâches", "Relier chaque tâche à son responsable, son échéance et sa phrase source", "Ranger les tâches dans le suivi de projet après validation"],
 "prerequis": ["L'accord des participants pour l'enregistrement", "Un outil de suivi de projet (RapidoRH ou équivalent)"],
 "etapes": [
  ("Annoncez l'enregistrement au début de la réunion et notez l'accord des participants.", "Prépare le message à lire en début de réunion pour annoncer l'enregistrement, son usage (transcription et tâches) et sa durée de conservation.", "Un fichier audio par réunion, enregistré avec l'accord de tous.", "Enregistrer sans prévenir les participants."),
  ("Relisez la transcription sur les noms propres et les chiffres avant d'extraire quoi que ce soit.", "Transcris cet audio [fichier] en français, puis liste les noms propres, chiffres et dates entendus pour que je les vérifie.", "Une transcription relue sur les points sensibles.", "Extraire des tâches d'une transcription non relue."),
  ("La phrase source permet de vérifier chaque tâche en quelques secondes.", None, "Un plan d'action où chaque tâche cite sa phrase source.", "Accepter une tâche que personne n'a réellement demandée."),
  ("Rien n'est écrit dans un outil externe sans votre validation.", "Prépare l'enregistrement de ces tâches [tâches] dans le tableau de suivi. Montre l'aperçu et attends mon accord avant toute écriture vers le CRM ou le CMS.", "Des tâches rangées après validation.", "Créer automatiquement les tâches dans tous les outils."),
  ("Rattachez chaque tâche au bon projet existant plutôt que d'en créer un nouveau.", "Lis les projets existants dans RapidoRH et propose pour chaque tâche le projet de rattachement. Ne crée rien sans mon accord.", "Des tâches rattachées aux bons projets.", "Créer un nouveau projet par réunion."),
 ]}

E["recrutement-assiste-par-ia"] = {
 "objectifs": ["Organiser plusieurs recrutements en séparant les données de chaque entreprise", "Rédiger des offres et analyser des CV avec l'aide de l'IA", "Garder la décision d'embauche entièrement humaine"],
 "prerequis": ["Une base de connaissance par entreprise (missions, valeurs, conditions)", "Un outil de suivi des candidatures"],
 "etapes": [
  ("Chaque entreprise a son espace : un recruteur ne voit que ses candidats.", "Vérifie que les données de chaque entreprise sont séparées : liste qui peut voir les candidats de [entreprise] et signale tout accès partagé.", "Des données séparées et des accès vérifiés.", "Mélanger les candidats de plusieurs entreprises dans une même liste."),
  ("L'offre décrit des missions concrètes et des critères objectifs.", None, "Une offre claire, fondée sur la base de connaissance de l'entreprise.", "Copier une offre générique qui ne décrit pas le vrai poste."),
  ("Le score sert à trier une pile, jamais à écarter quelqu'un seul.", "Extrais les compétences de ces CV [CV] et compare-les aux critères de l'offre. Présente un tableau d'aide au tri, sans classement définitif et sans critère discriminatoire.", "Un tableau d'aide au tri, relu par un humain.", "Présenter le score comme une décision."),
  ("Chaque changement de statut est daté et justifié.", "Liste les candidats par statut et signale ceux qui attendent une réponse depuis plus de 7 jours. Prépare les messages en brouillon.", "Un suivi à jour, sans candidat oublié.", "Laisser un candidat sans réponse."),
  ("Séparez le raisonnement, l'automatisation et le stockage : chacun se teste à part.", "Décris l'architecture de l'outil de recrutement : où se fait l'analyse, où tournent les workflows, où sont stockées les données, et où chaque écriture attend une confirmation.", "Une architecture claire, avec ses points de confirmation.", "Tout mettre dans un seul script impossible à tester."),
 ]}
