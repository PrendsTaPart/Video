# Module Comptabilité — état au 04/09

Dix tutoriels, dix analyses, dix fiches, dix scripts, dix voix. **Quatre sont
en ligne** — vidéo YouTube publique et page d'Académie complète. Les six autres
attendent leur rendu.

| # | Tutoriel | Analyse | Fiche | Script | Voix | Rendu | Bibliothèque | YouTube | Page |
|---|---|---|---|---|---|---|---|---|---|
| 1 | Créer et modifier une facture | ✅ | ✅ | 219 mots | ✅ | 88 s | ✅ | HSQazBmzAS4 | ✅ en ligne |
| 3 | Changer le statut d'une facture | ✅ | ✅ | 175 mots | ✅ | 61 s | ✅ | _kcUjdX4dxs | ✅ en ligne |
| 4 | Renseigner le mode de paiement | ✅ | ✅ | 161 mots | ✅ | 60 s | ✅ | FYSMeqjGEwk | ✅ en ligne |
| 5 | Retrouver une facture | ✅ | ✅ | 195 mots | ✅ | 73 s | ✅ | Dm13SaU-lsg | ✅ en ligne |
| 8 | Mode de paiement d'un devis | ✅ | ✅ | 159 mots | ✅ 55 s | ⏳ | — | — | — |
| 9 | Signer un devis à l'écran | ✅ | ✅ | 151 mots | ✅ 51 s | ⏳ | — | — | — |
| 10 | Convertir un devis en facture | ✅ | ✅ | 201 mots | ✅ 69 s | ⏳ | — | — | — |
| 11 | Créer un template de SMS | ✅ | ✅ | 174 mots | ✅ 62 s | ⏳ | — | — | — |
| 12 | Retrouver un devis | ✅ | ✅ | 164 mots | ✅ 59 s | ⏳ | — | — | — |
| 14 | Suivre ses dépenses | ✅ | ✅ | 193 mots | ✅ 69 s | ⏳ | — | — | — |

Le numéro est celui du catalogue, pas celui du dossier local. Les `a_verifier`
des dix fiches sont vides.

## Où en sont les dépendances externes

**ElevenLabs** — l'impayé est réglé, les dix voix sont synthétisées.

**YouTube** — le connecteur est ouvert. Les quatre vidéos sont publiques sur la
chaîne **RapidoCRM** (`UCXyptH13bJF7AVr2TZJWA-Q`). Attention : la chaîne active
du compte est FoodEatUp, il faut passer `channel_id` explicitement à chaque
envoi, sinon les tutoriels partent sur la mauvaise chaîne.

Le quota YouTube est la vraie limite : **5 envois par jour** (1 600 unités sur
10 000). Les quatre masters 16:9 en ont consommé quatre. Les quatre Shorts 9:16
n'ont pas encore été envoyés, et les six tutoriels restants demanderont douze
envois de plus — soit trois jours à ce rythme.

**Le domaine des pages est `tutoriel.rapido-crm.com`**, avec un trait d'union.
`publier_tutoriel` renvoie encore `tutoriel.rapidocrm.com`, qui n'a aucun DNS :
les `publication.json` de ce lot portent le domaine qui répond, vérifié en 200
sur les quatre pages.

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
