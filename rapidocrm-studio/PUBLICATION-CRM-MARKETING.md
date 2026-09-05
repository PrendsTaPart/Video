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
