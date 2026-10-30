PARTIE 2 — Le système de webinaires complet (à faire avec la page projet ci-dessus, la table webinaires de la partie 1 est remplacée par ce qui suit).

Objectif : je crée un webinaire en une phrase depuis Claude (MCP), il a sa page d'inscription, son lien Google Meet généré dans Google Agenda, ses emails automatiques, et chaque inscrit devient un lead qualifié rattaché au projet. Rien ne doit être inventé (pas de faux compteur d'inscrits, pas de faux avis).

1. Le webinaire
- Champs : titre, sous-titre, description, projet_slug (optionnel), intervenants (nom, rôle, photo de la médiathèque ; par défaut Michael avec la photo michael-entrepreneur-rond), date et heure, fuseau horaire (Europe/Paris par défaut, affiché dans le fuseau du visiteur), durée, places max (optionnel), visuel (couverture du projet ou image de la médiathèque), lien de diffusion (Google Meet généré, ou lien externe YouTube Live/Zoom/Teams saisi à la main), replay_url, CTA de fin (libellé + URL, par défaut le CTA n°1 du projet), statut (brouillon, publié, en direct, terminé, annulé), slug.
- Sessions multiples : un même webinaire peut avoir plusieurs dates (sessions) ; l'inscrit choisit sa session.
- Page publique /webinaires/<slug> : visuel, titre, promesse, ce que tu vas apprendre (3 à 5 points), intervenants, date et heure dans le fuseau du visiteur, compte à rebours, formulaire d'inscription, FAQ, lien vers le projet. Page /webinaires : liste des webinaires à venir et des replays.
- Une fois terminé : la page bascule en « Revoir le replay » avec le CTA de fin, et le formulaire donne accès au replay.

2. Inscription
- Formulaire : prénom, email (obligatoires), entreprise, métier/secteur, taille d'équipe, téléphone (optionnels, activables par webinaire), question libre « qu'est-ce que tu veux savoir ? », case de consentement explicite non cochée (« recevoir les emails de ce webinaire ») et case séparée « suivre l'actualité » (comme les abonnés existants).
- Protection : anti-spam (honeypot + limite par IP), email vérifié, pas de doublon (même email + même session = mise à jour, pas de 2e inscription).
- Paramètres UTM et source (vidéo, short, email, page projet, réseau) enregistrés sur l'inscription.
- Liste d'attente automatique si les places sont pleines.
- Popup de confirmation après inscription : « C'est noté », récapitulatif date/heure dans son fuseau, boutons « Ajouter à Google Agenda », « Ajouter à Outlook », « Télécharger le fichier .ics (Apple/autres) », bouton de partage du webinaire.
- Page « Gérer mon inscription » (lien unique et signé dans chaque email) : changer de session, annuler, rajouter à l'agenda.

3. Fichier calendrier .ics et liens d'agenda
- Générer un fichier .ics valide (RFC 5545 : UID stable par inscription, DTSTART/DTEND en UTC, TZID, SUMMARY, DESCRIPTION avec le lien de connexion et le lien « gérer mon inscription », LOCATION = lien Meet, ORGANIZER, rappel VALARM 15 min avant), et METHOD:REQUEST pour l'invitation par email (s'ajoute en un clic dans Gmail/Outlook/Apple).
- Le .ics est joint à l'email de confirmation ET téléchargeable dans le popup. Mise à jour automatique (même UID, SEQUENCE+1) si la date change, et METHOD:CANCEL si annulé.
- Liens « Ajouter à Google Agenda » et « Ajouter à Outlook » pré-remplis.

4. Google Agenda et Google Meet
- Connecter mon compte Google (Google Calendar API, OAuth) : à la publication d'un webinaire, créer l'événement dans mon Google Agenda avec un lien Google Meet généré automatiquement (conferenceData). Mettre à jour/annuler l'événement si le webinaire change.
- Option : ajouter chaque inscrit comme invité de l'événement (désactivée par défaut, au-delà d'un certain nombre on n'ajoute plus d'invités et on reste sur les emails + .ics).
- Le lien Meet n'est jamais affiché sur la page publique : il est envoyé aux inscrits seulement (email de confirmation, rappels, page « gérer mon inscription »).
- Si Google n'est pas connecté : le webinaire fonctionne avec un lien saisi à la main. Ne me demande jamais de clé dans le chat : l'OAuth se fait dans l'admin.

5. Emails automatiques du webinaire (transactionnels, envoyés seulement aux inscrits qui ont coché la case du webinaire)
- Confirmation immédiate (avec .ics, lien de connexion, gérer mon inscription).
- Rappels : J-1, H-1 et 10 minutes avant (« On commence, voici ton lien »).
- Après le direct : « Merci d'être venu » + replay + CTA de fin aux présents ; « Tu l'as manqué, voici le replay » aux absents.
- Liste d'attente : « Une place s'est libérée ».
- Modification de date ou annulation.
- Chaque email : charte du projet, sujet et texte modifiables par webinaire (modèles par défaut fournis), lien de désinscription, suivi d'ouverture et de clic.
- Ces emails transactionnels partent automatiquement parce que la personne les a demandés en s'inscrivant. Les campagnes pour annoncer un webinaire aux abonnés restent des brouillons que j'envoie moi-même dans l'admin.

6. Email à l'admin pour chaque inscrit
- À chaque inscription, un email à l'adresse admin réglée dans les réglages : nom, email, entreprise, métier, réponses, source/UTM, session choisie, nombre total d'inscrits, lien vers la fiche du lead. Option résumé quotidien au lieu d'un email par inscrit.

7. Leads et suivi
- Chaque inscrit crée ou met à jour un lead (source « webinaire », projet_slug, tags), avec l'historique : inscrit, a ouvert, a cliqué, présent, a vu le replay, a cliqué le CTA de fin.
- Présence : enregistrer qui a cliqué le lien de connexion (lien de redirection suivi) ; import manuel de la liste des présents possible.
- Export CSV des inscrits.
- Statistiques par webinaire : vues de la page, inscrits, taux d'inscription, présents, taux de présence, vues du replay, clics sur le CTA, par source.

8. Référencement
- Données structurées Event (eventAttendanceMode Online, location VirtualLocation, organizer), image de partage = visuel du webinaire, titre et description propres.

9. Admin
- Onglet « Webinaires » : créer/modifier, sessions, intervenants, aperçu de la page, modèles d'emails, connexion Google, liste des inscrits (filtres, export), statistiques, bouton « Publier ».

10. Outils MCP (Claude doit tout pouvoir faire, tout naît en brouillon)
- creer_webinaire(titre, description, date_heure, duree_minutes, projet_slug?, sous_titre?, points_cles?, intervenants?, places_max?, fuseau?, visuel_cle?, cta?, lien_diffusion?) ; modifier_webinaire ; ajouter_session_webinaire ; lister_webinaires(projet_slug?, statut?) ; obtenir_webinaire.
- generer_lien_google_meet(webinaire) : crée ou met à jour l'événement Google Agenda et renvoie le lien Meet.
- publier_webinaire / annuler_webinaire (accord explicite de Michael).
- lister_inscrits_webinaire(webinaire, session?) ; inscrire_au_webinaire(webinaire, prenom, email, ...) pour une inscription manuelle avec consentement déclaré ; marquer_presents(webinaire, emails[]).
- modifier_emails_webinaire(webinaire, type, sujet?, texte?) ; apercu_email_webinaire(webinaire, type) ; tester_email_webinaire(webinaire, type) vers l'adresse admin seulement.
- definir_replay(webinaire, replay_url).
- statistiques_webinaire(webinaire).
- lier_ressource_projet accepte le type webinaire.

11. Vérification
- Crée un webinaire de test en brouillon sur foodeatup-fidelite, fais une inscription de test avec l'adresse admin, vérifie : popup avec les 3 boutons d'agenda, .ics qui s'ouvre dans Google Agenda et Apple Calendrier avec la bonne heure, email de confirmation avec .ics joint, email admin reçu, lead créé, rappel planifié. Supprime ensuite les données de test.
- Ne publie aucun webinaire et n'envoie rien à d'autres personnes que l'admin. Liste les nouveaux outils MCP avec leurs paramètres, dis-moi ce que je dois connecter moi-même (compte Google), et rappelle-moi de republier le site.
