Suite de la communauté : termine les 5 points que tu as listés comme incomplets (audio, file d'envoi différé, parrainage, attribution des inscriptions, modération complète). Repars de ce qui existe déjà (espace membre, cours, progression, classement, messages internes, liens suivis /l/<code>, tables leads, webinaires, médiathèque) : ne refais rien qui marche, ne change pas le design. Tout reste en brouillon, inscriptions toujours fermées, rien n'est publié ni envoyé à quelqu'un d'autre que moi.

1. Messages audio dans la communauté
- Dans la messagerie interne, je peux joindre un vocal à un message, à un membre ou à un segment (nouveaux inscrits d'un lead magnet, niveau, cours suivi). Source du vocal : un fichier audio de la médiathèque, un enregistrement fait depuis le navigateur, ou une voix générée par ElevenLabs à partir d'un texte (voix choisie dans l'admin).
- La clé ElevenLabs s'enregistre dans un formulaire sécurisé de l'admin (secret côté serveur, jamais affichée en entier, jamais renvoyée par un outil MCP). Sans clé, l'option « voix générée » est grisée avec un lien vers le formulaire.
- Chaque audio généré est enregistré dans la médiathèque (catégorie audio, source « génération IA ElevenLabs ») et réutilisé ensuite : jamais deux générations pour le même texte et la même voix.
- Lecteur audio dans le fil des messages, avec durée et transcription affichée (le texte source, ou une transcription si c'est un enregistrement).
- Message de bienvenue automatique : texte et vocal facultatif, modifiables dans l'admin.

2. Vocal sur la messagerie externe de l'utilisateur
- Un utilisateur (moi ou un client de la plateforme) connecte sa messagerie dans un formulaire sécurisé de l'admin : WhatsApp Business Cloud API (jeton et identifiant du numéro) ou Telegram (jeton de bot). La clé est chiffrée, masquée, révocable, et n'apparaît jamais dans une réponse MCP ni dans une conversation avec Claude.
- Une fois connectée, on peut envoyer depuis ce compte un vocal (même source que ci-dessus) aux seuls contacts ayant donné leur consentement explicite et leur numéro ou identifiant, par exemple le vocal de bienvenue après un lead magnet, avec le lien suivi de la ressource.
- Garde-fous : consentement enregistré obligatoire (date, source, texte du consentement), STOP / désinscription respectés, modèles approuvés WhatsApp hors fenêtre de 24 h, limite d'envoi par minute, journal de chaque envoi (qui, quand, à qui, statut, erreur). Test possible uniquement vers le numéro du propriétaire du compte.

3. File d'envoi différé
- Une file unique pour les messages communauté, les vocaux externes, les emails de campagne et les rappels de live : chaque envoi a une date prévue, un statut (brouillon, validé, programmé, envoyé, échec, annulé), des tentatives avec nouvel essai automatique limité, et un journal.
- Rien n'est programmé sans validation explicite (bouton « Valider et programmer » côté admin, confirmer=true côté MCP). Annulation possible jusqu'à l'envoi. Respect des heures calmes (réglables, par défaut 21 h – 8 h, fuseau Europe/Paris).
- Interrupteur général « envois actifs » dans l'admin, désactivé par défaut.

4. Parrainage
- Chaque membre a son lien de parrainage (lien suivi /l/<code> rattaché à son compte), visible dans son espace avec ses clics, ses inscrits et ses points gagnés.
- Commission seulement si l'offre est payante : taux réglable, 0 par défaut. Aucun paiement automatique : export CSV et validation par moi.
- Anti-abus : pas d'auto-parrainage (même email, même appareil), points de parrainage plafonnés par jour.

5. Attribution des inscriptions
- Chaque inscription (lead magnet, membre, webinaire) et chaque achat est attribué au dernier lien suivi cliqué (cookie réglable, 30 jours par défaut), avec repli sur les paramètres UTM.
- Tableau de bord : clics, inscrits et taux de conversion par réseau, publication, épisode, lead magnet et parrain, sur une période choisie. Rien d'inventé : une donnée absente s'affiche « inconnue », pas zéro.

6. Modération complète
- Signaler un post, un commentaire ou un message ; file de modération dans l'admin (masquer, rétablir, supprimer définitivement avec confirmation, avertir).
- Suspendre ou bannir un membre (durée, motif, journal), mots-clés bloqués, limite de publications par jour pour les nouveaux membres, publications des nouveaux membres en attente de validation (réglable).
- Le membre peut bloquer un autre membre et couper ses messages privés.

7. Outils MCP (brouillon par défaut ; tout ce qui part vers des personnes demande confirmer=true et renvoie un aperçu sans)
- generer_audio(texte, voix?) : renvoie la clé médiathèque, réutilise l'audio existant si identique.
- envoyer_message_communaute(destinataires|segment, texte?, audio_cle?, date_prevue?, confirmer).
- connexions_messagerie() : liste les comptes branchés sans jamais les clés.
- envoyer_vocal_messagerie(connexion_id, contact|segment, audio_cle, lien?, date_prevue?, confirmer) ; tester_vocal_messagerie(connexion_id) vers le propriétaire seulement.
- lister_file_envoi(statut?, periode?), annuler_envoi(id).
- statistiques_parrainage(email?), statistiques_liens(periode, par).
- moderer(element_id, action, motif?), lister_signalements(statut?).

8. Vérification
- Génère un seul vocal de bienvenue (une prise), joue-le dans la messagerie interne vers mon compte admin, et vérifie qu'un second appel avec le même texte réutilise l'audio.
- Programme un message de test vers moi seulement dans 10 minutes, puis annule-le : le journal doit montrer « programmé » puis « annulé ».
- Crée mon lien de parrainage, fais 2 clics de test et une inscription test : ils doivent apparaître attribués à ce lien.
- Signale un commentaire de test et masque-le depuis la file de modération.
- Si aucune messagerie externe n'est connectée, montre-moi le formulaire de connexion sans rien demander dans le chat.
- Contrôle mobile 375 px et ordinateur 1440 px. Liste les nouveaux outils MCP avec leurs paramètres, dis-moi ce que je dois connecter moi-même (clé ElevenLabs, WhatsApp Business, Telegram, domaine d'envoi), et rappelle-moi de republier le site.
