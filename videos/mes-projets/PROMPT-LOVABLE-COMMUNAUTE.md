Nouvelle fonctionnalité : une communauté façon Skool autour de mes formations, de mes lead magnets et de mes publications sociales, avec suivi des liens et messages audio.

Référence analysée : skool.com (ex. la communauté « Vision IA » de Baptiste Fort). On en reprend la logique, pas le design ni les textes : page « À propos » qui vend la communauté, fil de discussion, classroom dont les modules se débloquent par niveau, points et classement, questions d'adhésion, message de bienvenue automatique, lien de parrainage par membre avec ses statistiques, calendrier des lives. Tout reprend ma charte et mes contenus existants (formations, lead magnets, vidéos, projets). Rien ne doit être inventé : pas de faux nombre de membres, pas de faux avis, pas de faux chiffre d'affaires.

1. Espace membre et page « À propos » (/communaute)
- Page publique « À propos » : vidéo de présentation (une vidéo du Journal choisie dans l'admin), promesse, « ce que tu trouves dedans » (formations, guides, lives), auteur (photo michael-entrepreneur-rond de la médiathèque), vrai nombre de membres (masqué sous un seuil réglable), prix ou « gratuit », bouton « Rejoindre ».
- Inscription : prénom, email, mot de passe ou lien magique, plus 1 à 3 questions d'adhésion modifiables dans l'admin (ex. « Ton métier ? », « Ce que tu veux construire ? », email déjà demandé). Consentement explicite et séparé pour « recevoir les messages de la communauté ». Les réponses enrichissent la fiche lead.
- Option d'adhésion manuelle (je valide les demandes) ou automatique.
- Espace membre avec onglets : Communauté (fil), Formations (classroom), Ressources (lead magnets), Calendrier, Membres, Classement, Messages.

2. Classroom : formations et lead magnets dans un même parcours
- Les formations existantes deviennent des cours : chaque étape est une leçon (vidéo de l'épisode, texte, prompt à copier, PDF), avec une case « Terminé » et une barre de progression.
- Règles d'accès par cours : libre, réservé aux membres, débloqué à un niveau (1 à 9), ou réservé à une offre payante (offres existantes).
- Les lead magnets restent accessibles avec prénom et email depuis le site public. Une fois inscrit, la ressource apparaît aussi dans l'onglet Ressources du membre, et l'inscription au lead magnet propose de rejoindre la communauté.
- Reprise automatique : « Continue là où tu t'es arrêté ».

3. Points, niveaux et classement
- Points pour : publier, commenter, recevoir un like, terminer une leçon, terminer une formation, assister à un live, parrainer un inscrit.
- Barème modifiable dans l'admin, 9 niveaux avec nom et seuil personnalisables, et ce que chaque niveau débloque (cours, ressource, accès à un live).
- Classement sur 7 jours, 30 jours et depuis toujours. Je peux masquer un membre ou retirer des points (anti-triche : pas de points pour ses propres likes, limite par jour).

4. Fil de communauté
- Publications avec catégories (Annonces, Questions, Réussites, Épisodes). Chaque nouvel épisode publié crée automatiquement un post « Nouvel épisode » (vidéo, formation liée, lead magnet lié).
- Likes, commentaires, mentions, publication épinglée, modération (signaler, masquer), notifications in-app et par email (désactivables par le membre).

5. Liens suivis (tracking) pour les réseaux sociaux, les emails et les parrainages
- Lien court suivi /l/<code> : on crée un lien pour chaque publication sociale préparée (preparer_publication), chaque campagne email, chaque lead magnet et chaque membre (parrainage). Le lien garde la destination, la source (réseau, email, short, page projet), l'épisode, la publication d'origine et les paramètres UTM, puis redirige.
- Chaque clic est enregistré (date, source, appareil, pays approximatif, sans IP en clair). Chaque inscription (lead, membre, webinaire) et chaque achat est attribué au dernier lien suivi cliqué (cookie de 30 jours, réglable).
- Les textes préparés pour les réseaux utilisent automatiquement le lien suivi de leur publication, pour qu'on sache quel post a amené quels inscrits.
- Parrainage : chaque membre a son lien et voit ses clics, ses inscrits et, si l'offre est payante, sa commission (taux réglable, 0 par défaut). Pas de paiement automatique des commissions : export et validation par moi.
- Tableau de bord : clics, inscrits et taux de conversion par réseau, par publication, par épisode, par lead magnet et par parrain, sur une période choisie.

6. Messages : bienvenue, privés et messages audio
- Messagerie privée entre membres et avec moi (désactivable par membre), plus un message de bienvenue automatique à l'inscription, modifiable dans l'admin.
- Messages audio : je peux envoyer un message vocal (fichier audio de la médiathèque, ou voix générée par ElevenLabs à partir d'un texte, voix réglée dans l'admin) dans la messagerie de la communauté, à un membre ou à un segment (ex. nouveaux inscrits d'un lead magnet). Lecture dans le fil des messages avec transcription affichée.
- Message audio sur la messagerie externe de l'utilisateur qui a branché son compte : un utilisateur (moi ou un client de la plateforme) peut connecter sa propre messagerie en enregistrant sa clé dans un formulaire sécurisé de l'admin (WhatsApp Business Cloud API : jeton et numéro ; Telegram : jeton de bot). La clé est chiffrée, jamais affichée en entier, jamais demandée ni renvoyée dans une conversation avec Claude, et révocable. Une fois connectée, on peut envoyer depuis ce compte un message vocal (même source audio) aux contacts qui ont donné leur consentement explicite et leur numéro ou identifiant : par exemple le vocal de bienvenue après l'inscription à un lead magnet, avec le lien suivi de la ressource.
- Garde-fous : jamais d'envoi sans consentement enregistré ; respect des règles de la plateforme (pour WhatsApp, modèles approuvés en dehors de la fenêtre de 24 h) ; lien « STOP » ou désinscription ; limite d'envoi par minute ; journal de chaque envoi (qui, quand, à qui, statut) ; test possible vers mon propre numéro seulement.

7. Calendrier des lives
- Lives et webinaires (table webinaires existante) dans un calendrier, avec ajout à l'agenda (.ics), rappel par email et, si le membre l'a accepté, par message vocal ou texte sur la messagerie connectée. Points de présence.

8. Outils MCP (pour que Claude pilote tout ; tout naît en brouillon, et ce qui part vers des personnes demande confirmer=true)
- Communauté : obtenir_communaute, modifier_communaute(page à propos, questions d'adhésion, prix, adhésion manuelle/auto), lister_membres(filtres), valider_membre, statistiques_communaute.
- Classroom : creer_cours_depuis_formation(slug_formation, regle_acces, niveau?), modifier_regle_acces, progression_membre(email).
- Gamification : modifier_bareme_points, modifier_niveaux, classement(periode).
- Fil : publier_post_communaute(titre, texte, categorie, video_slug?, epingle?) en brouillon puis publier ; poster_nouvel_episode(episode) automatique ou manuel.
- Liens suivis : creer_lien_suivi(destination, source, reseau?, episode?, publication_id?, campagne_id?), statistiques_liens(periode, par: reseau|publication|episode|lead_magnet|parrain), statistiques_parrainage(email?).
- Messages : creer_message_bienvenue(texte, audio?), envoyer_message_communaute(destinataires|segment, texte?, audio_cle?, confirmer), generer_audio(texte, voix?) qui renvoie une clé de médiathèque, connexions_messagerie() qui liste les comptes branchés (sans les clés), envoyer_vocal_messagerie(connexion_id, contact|segment, audio_cle, lien?, confirmer) avec aperçu sans confirmer, et tester_vocal_messagerie(connexion_id) vers le numéro du propriétaire seulement.
- Les publications sociales préparées reçoivent automatiquement leur lien suivi (preparer_publication renvoie le lien court).

9. Vérification
- Crée la page « À propos » en brouillon avec mes vraies données, transforme 3 formations récentes en cours (dont une débloquée au niveau 2), crée un lien suivi pour une publication LinkedIn de l'épisode 89 et fais 2 clics de test : ils doivent apparaître dans le tableau de bord, attribués à cette publication.
- Teste un message audio dans la messagerie de la communauté et l'envoi d'un vocal de test uniquement vers mon propre compte connecté (si aucun compte n'est connecté, montre-moi le formulaire de connexion sans rien demander dans le chat).
- Contrôle mobile 375 px et ordinateur 1440 px. Ne publie rien, n'envoie rien à personne d'autre que moi, liste les nouveaux outils MCP avec leurs paramètres, dis-moi ce que je dois connecter moi-même (WhatsApp Business, Telegram, ElevenLabs, domaine d'envoi), et rappelle-moi de republier le site.
