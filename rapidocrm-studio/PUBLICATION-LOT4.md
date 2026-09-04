# Module Comptabilité — état au 04/09

Dix tutoriels, dix analyses, dix fiches, dix scripts. Quatre sont montés et
déposés ; six attendent la voix.

| # | Tutoriel | Analyse | Fiche | Script | Voix | Rendu | Bibliothèque | Page |
|---|---|---|---|---|---|---|---|---|
| 1 | Créer et modifier une facture | ✅ | ✅ | 219 mots | ✅ | 88 s | ✅ | ⏳ |
| 3 | Changer le statut d'une facture | ✅ | ✅ | 175 mots | ✅ | 61 s | ✅ | ⏳ |
| 4 | Renseigner le mode de paiement | ✅ | ✅ | 161 mots | ✅ | 60 s | ✅ | ⏳ |
| 5 | Retrouver une facture | ✅ | ✅ | 195 mots | ✅ | 73 s | ✅ | ⏳ |
| 8 | Mode de paiement d'un devis | ✅ | ✅ | 159 mots | ⛔ | — | — | — |
| 9 | Signer un devis à l'écran | ✅ | ✅ | 151 mots | ⛔ | — | — | — |
| 10 | Convertir un devis en facture | ✅ | ✅ | 201 mots | ⛔ | — | — | — |
| 11 | Créer un template de SMS | ✅ | ✅ | 174 mots | ⛔ | — | — | — |
| 12 | Retrouver un devis | ✅ | ✅ | 164 mots | ⛔ | — | — | — |
| 14 | Suivre ses dépenses | ✅ | ✅ | 193 mots | ⛔ | — | — | — |

Le numéro est celui du catalogue, pas celui du dossier local. Les `a_verifier`
des dix fiches sont vides.

## Deux dépendances externes bloquent la suite

**Le compte ElevenLabs a un impayé.** La synthèse des 36 blocs des quatre
premiers tutoriels est passée, puis l'API a répondu 401 :

> `payment_required` — Your subscription has a failed or incomplete payment.
> Complete the latest invoice to continue usage.

Rien à corriger côté code : il faut régler la facture ElevenLabs. Les six
scripts restants partiront ensuite d'une traite — environ 50 blocs, dont une
part sera reprise du cache mutualisé.

**Aucun connecteur YouTube n'est ouvert.** `publier:site` refuse les quatre
pages prêtes sur `youtube_url absent`. Une page d'Académie se remplit
entièrement ou pas du tout : les publier sans leur lien YouTube les laisserait
en retrait des dix-neuf déjà en ligne. Deux sorties — ouvrir le connecteur
YouTube Publisher, ou décider que ces pages partent sans le lien.

## Le format court, et ce qu'il a fallu recaler

Trois seuils étaient calibrés sur l'ancien format long et se contredisaient
entre eux une fois les scripts resserrés :

| Contrôle | Avant | Après |
|---|---|---|
| `qa` — plancher de transcription | 200 mots | 140 mots |
| `qa` — fenêtre de durée | 80–170 s | 55–170 s |
| `controlerAvantPublication` | 200 mots | 140 mots |
| `script` — durée cible | 90–150 s | 55–150 s |

Le plafond d'accélération de la démonstration passe de 1,6× à 2,2× : une voix
plus courte sur une fenêtre source inchangée accélère d'autant.

## Ce que la relecture des frames a rattrapé

La QA vérifie que les zones déclarées sont floutées ; elle ne peut pas savoir
qu'on en a oublié une. Deux fuites sont passées sous elle, toutes deux
corrigées avant publication :

- **V04** — à 2 s la page est moins défilée qu'à 6 s, la deuxième adresse
  descendait sous la zone déclarée.
- **V05** — les quatre dernières secondes basculent dans le lecteur PDF de la
  facture : coordonnées du client, SIRET, puis banque, code guichet et IBAN.
  Rien n'était déclaré.

À retenir pour les 16 tutoriels du module CRM & Marketing : **regarder les
frames du master rendu**, pas seulement le verdict de la QA.
