# Module CRM & Marketing (06-crm-marketing) — état de production

Seize enregistrements confiés pour ce module. Les numéros et les slugs
viennent du catalogue de l'Académie, pas du nom des dossiers : le dossier
`V13-planifier-un-email-sms` porte le tutoriel n° 13, slug
`06-planifier-un-email-sms`.

| # | Tutoriel | Analyse | Fiche | Script | Durée estimée |
|---|----------|---------|-------|--------|---------------|
| 13 | Planifier un email/SMS | ✅ | ✅ | ✅ | 71 s |
| 14 | Planifier un RDV | ✅ | ✅ | ✅ | 114 s |
| 15 | Envoyer une newsletter | ✅ | ✅ | ✅ | 63 s |
| 17 | Créer un devis | ✅ | ✅ | ✅ | 82 s |
| 18 | Créer une facture | ✅ | ✅ | ✅ | 76 s |
| 19 | Créer un contrat | ✅ | ✅ | ✅ | 81 s |
| 21 | Créer une carte fidélité | ✅ | ✅ | ✅ | 65 s |
| 23 | Créer un jeu concours | ✅ | ✅ | ✅ | 79 s |
| 25 | Ajouter un PDF | ✅ | ✅ | ✅ | 68 s |
| 27 | Historique de l'entreprise | ✅ | ✅ | ✅ | 59 s |
| 28 | Historique email | ✅ | ✅ | ✅ | 58 s |
| 29 | Historique SMS | ✅ | ✅ | ✅ | 56 s |
| 31 | Historique contrat | ✅ | ✅ | ✅ | 62 s |
| 32 | Historique document | ✅ | ✅ | ✅ | 63 s |
| 33 | Historique facture | ✅ | ✅ | ✅ | 62 s |
| 34 | Historique devis | ✅ | ✅ | ✅ | 71 s |

Toutes les fiches ont `a_verifier` vide : rien n'y est affirmé qui ne vienne
d'une frame ou d'un schéma d'outil MCP.

## Ce qui est flouté, et pourquoi

Trois familles de fuites, qu'aucun contrôle automatique n'aurait vues : la QA
ne vérifie que les zones **déclarées**.

- **Documents ouverts en grand.** Les pages de facture (33) et de devis (34)
  et le PDF de contrat (31) affichent en clair le téléphone, le SIRET,
  l'adresse postale et l'e-mail des deux sociétés. Le corps du document est
  déclaré sensible en entier ; seuls l'en-tête, la pagination et les boutons
  restent lisibles.
- **Listes de personnes.** La liste des invités d'un rendez-vous (14) déroule
  les noms et les adresses e-mail des utilisateurs du compte ; les étiquettes
  retenues redeviennent lisibles à trois moments du défilement, chacun couvert
  par sa propre fenêtre de temps.
- **Journaux d'échanges.** Les historiques d'e-mails (28) et de SMS (29)
  montrent le nom de l'expéditrice, le numéro du destinataire et la première
  ligne du corps du message.

S'y ajoutent, sur les sept enregistrements faits en fenêtre de navigateur, la
barre d'adresse locale `127.0.0.1:8000`, les extensions du poste et le bouton
« Demander à Gemini ». Le bandeau de compte (photo et nom de l'utilisatrice)
est flouté sur les seize.

## Deux points relevés à l'écran, à remonter au produit

- La confirmation de suppression d'un document (32) est posée par le
  navigateur et rédigée **en anglais** : « Are you sure you want to delete
  this file? ». Elle est visible par l'utilisateur.
- Deux journaux (31, 34) restent plusieurs secondes sur une page vide avant
  d'afficher leur tableau. Le scénario le dit à voix haute pour que le
  spectateur ne conclue pas à une liste vide, mais le chargement mériterait
  un indicateur.

## Un enregistrement inexploitable

`V08-ajouter-modifier-un-contact` ne montre aucun formulaire de contact : la
liste des clients défile, puis une page Entreprise vide, puis « S'il vous
plaît, attendez… » jusqu'à la fin. À refaire ; le reste du module n'en dépend
pas.

## Envois YouTube planifiés

Le quota YouTube est de cinq envois par jour. Les cinq derniers tutoriels
Comptabilité occupaient déjà des créneaux les 6, 7 et 8 septembre ; les seize
de ce module se glissent autour, en mode `upload_at_time` sur la chaîne
RapidoCRM (`UCXyptH13bJF7AVr2TZJWA-Q`).

| Date (Paris) | 08:00 | 10:00 | 12:00 | 14:00 | 16:00 |
|---|---|---|---|---|---|
| 06/09 | V13 | *V09 (compta)* | V14 | *V10 (compta)* | V15 |
| 07/09 | V17 | *V11 (compta)* | V18 | *V12 (compta)* | V19 |
| 08/09 | V21 | *V14 (compta)* | V23 | V25 | V27 |
| 09/09 | V28 | V29 | V31 | V32 | V33 |
| 10/09 | V34 | | | | |

Ce qui est en ligne, au fil des envois — page vérifiée en HTTP 200 :

| Envoi (UTC) | Tutoriel | YouTube | Page Académie |
|---|---|---|---|
| 06/09 06:00 | V13 Planifier un email/SMS | `E4bCEWBcVa4` | `/tutoriel/06-planifier-un-email-sms` |
| 06/09 08:00 | *V09 compta* Signer un devis | `LBpOI2ARMvs` | `/tutoriel/05-signature-electronique-d-un-devis` |
| 06/09 10:00 | V14 Planifier un rendez-vous | `Pxq4RqZUUVw` | `/tutoriel/06-planifier-un-rdv` |
| 06/09 12:00 | *V10 compta* Devis en facture | `QOfn1ZMpzo0` | `/tutoriel/05-conversion-d-un-devis-en-facture` |
| 06/09 14:00 | V15 Envoyer une newsletter | `_VW4v9Ldha0` | `/tutoriel/06-envoyer-une-newsletter` |
| 07/09 06:00 | V17 Créer un devis | `K3yiDpOHW7g` | `/tutoriel/06-creer-un-devis` |
| 07/09 08:00 | *V11 compta* Créer un template SMS | `-ayFuImidp4` | `/tutoriel/05-creer-ses-templates-emails-sms` |
| 07/09 10:00 | V18 Créer une facture | `edjve6F2HAQ` | `/tutoriel/06-creer-une-facture` |
| 07/09 12:00 | *V12 compta* Retrouver un devis | `5FJO1-iGE-I` | `/tutoriel/05-historique-des-devis` |

Le connecteur YouTube MCP s'est déconnecté de la session le 6 au matin.
Les identifiants se relèvent alors sur le flux RSS public de la chaîne,
`https://www.youtube.com/feeds/videos.xml?channel_id=UCXyptH13bJF7AVr2TZJWA-Q`,
et chaque lien est vérifié en HTTP avant d'être écrit. Le reste de la
procédure ne change pas.

Les vingt-quatre médias sont déposés dans la bibliothèque RapidoCMS et
`publier:cms` est passé pour les seize. Il ne manque à chaque page que
l'URL YouTube.

## Ce qui reste, une fois chaque envoi effectué

1. Écrire `youtube.publish_video.publication.reponse.json` avec le `video_id`.
2. `npm run publier:youtube` puis `npm run publier:site`. Une page se remplit
   entièrement ou pas du tout : `publier-site` refuse tant que l'URL YouTube
   ne répond pas.

## Une leçon de méthode sur le floutage

V14 a fuité trois fois de suite au même endroit, à chaque fois de quelques
centièmes : les adresses e-mail des invités, puis les noms des organisateurs,
puis le premier nom de la liste déroulante. La cause n'était pas le choix des
bornes mais le principe : entre la 55e et la 60e seconde, la modale **défile
en continu**, et un rectangle fixe sur une fenêtre de temps ne suit pas un
mouvement continu.

Deux règles en sortent, valables pour tout le reste de la série :

- **Découper de part et d'autre du défilement** plutôt qu'élargir le flou.
  Une étape qui s'arrête avant le mouvement et une autre qui reprend après
  ont chacune une position stable, où un rectangle suffit.
- **Couvrir largement quand une liste peut s'ouvrir.** Une liste déroulante
  apparaît là où on ne l'attend pas — celle des utilisateurs remontait
  au-dessus du champ. Mieux vaut flouter tout le corps d'une modale pendant
  l'étape concernée que viser la bande où l'on croit que sont les étiquettes.

Et surtout : **la QA ne voit pas ces fuites.** Elle vérifie que les zones
*déclarées* sont floutées, pas qu'il ne reste rien de lisible ailleurs. Seule
la relecture des frames rendues les trouve. Les seize ont été relues aux
moments les plus risqués.

## La clé d'API de l'Académie ne va pas dans le dépôt

Le pont MCP recopiait `parametres` tel quel dans chaque `*.demande.json`, et
ces fichiers sont versionnés : la clé de l'Académie s'est retrouvée en clair
dans trente-sept fichiers suivis, sur plusieurs commits. `pont.ts` la masque
désormais à l'écriture — `<RAPIDO_ACADEMIE_API_KEY>` — et la consigne de la
demande dit de relire la vraie valeur dans l'environnement. Les fichiers de
l'arbre de travail sont nettoyés.

L'historique déjà poussé la contient encore. Révoquer la clé et en générer
une autre dans `/admin/parametres` est une décision de Michael, pas une
opération à mener depuis ici.

## Rapprocher un envoi YouTube à son tutoriel

Le connecteur YouTube MCP est tombé le 6 septembre au matin et n'est pas
revenu : les identifiants se relèvent sur le flux RSS public de la chaîne.
Deux pièges s'y cachent.

Le titre du flux se rapproche de `seo.youtube_titre`, jamais de `seo.titre`
ni de l'heure d'envoi. C'est bien `youtube_titre` que `publier-youtube`
envoie à YouTube, et les deux champs divergent : V12 est titrée « Retrouver
un devis » côté SEO et « Retrouver un devis dans l'historique » sur YouTube.
Se fier au créneau horaire ne marche pas non plus — le 7 au matin, le
tutoriel de 06:00 s'appelait « Créer un devis » et celui de 08:00 « Créer un
template SMS », ce qui laisse croire à une inversion des modules alors que
le calendrier était juste.

Un `curl` sur `/watch` peut rendre 302 puis 429 : c'est une limitation de
débit de Google, pas une vidéo absente. Le contrôle qui tranche est oEmbed,
`https://www.youtube.com/oembed?url=<url encodée>&format=json` — 200 avec le
bon titre et la bonne chaîne, 404 pour un identifiant inventé. Encoder l'URL
n'est pas facultatif : l'identifiant de V11 commence par un tiret.
