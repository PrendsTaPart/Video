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
