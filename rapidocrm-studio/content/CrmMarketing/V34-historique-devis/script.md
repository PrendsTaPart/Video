# Historique devis

Module **CrmMarketing** · V34 · `06-historique-devis`

## Hook

> Le client rappelle pour accepter un devis de juillet. Vous, vous ne savez plus s'il est encore valable.
> Le devis vous le dit lui-même, dès l'ouverture.

**Alternatives proposées :**
1. Un devis a une date de fin, et elle compte autant que son prix.
2. Relancer sur un devis périmé, c'est relancer dans le vide.
3. Vert accepté, orange en attente : le tableau se lit d'un coup d'œil.

## Intro

On part de la page Historique, et on ressort avec le devis ouvert. Le tableau donne les dates, le statut et le prix ; le devis, lui, prévient quand la période de signature est passée.

## Démo

### 1. Ouvrir l'historique des devis

_1.0s → 12.5s · 30 mots · ~12.0s_

Troisième rangée de la page Historique : les devis. On consulte. La page reste vide quelques secondes, le temps que le tableau arrive : ce n'est pas une liste vide.

### 2. Lire le tableau des devis

_12.5s → 18.0s · 10 mots · ~4.0s_

Dates, statut, prix. Vert pour accepté, orange pour en attente.

### 3. Ouvrir un devis

_18.0s → 21.5s · 4 mots · ~1.6s_

L'icône ouvre le devis.

### 4. Lire l'alerte de période de signature

_21.5s → 24.7s · 8 mots · ~3.2s_

Et le bandeau dit qu'il n'est plus signable.

## Faites-le avec Claude

**Et pour ce qui reste à décrocher ?**

Le journal montre un client. Pour voir tous les devis qui attendent une réponse, RapidoCRM parle à Claude : vous demandez en français, il lit vos données et répond. Copiez ce prompt, remplacez ce qui est entre crochets.

```
Liste-moi mes [nombre] devis en attente avec leur destinataire et leur montant.
```

Résultat affiché : **3 devis en attente** — N° 14 — 18 480,00 € · N° 15 — 50 880,00 € · N° 16 — 18 480,00 €

## Punchline

> Un devis dit lui-même qu'il a expiré : la relance part sur ce qui peut encore se signer.

**Alternatives proposées :**
1. Ce qui est périmé se refait, il ne se relance pas.
2. Deux couleurs, et le suivi commercial tient dans un regard.
3. La date de fin vaut autant que le prix.

## SEO

- Titre : Historique des devis — RapidoCRM _(32 car.)_
- Description : Consultez le journal des devis d'un client dans RapidoCRM : dates de validité, statut, prix, et l'alerte affichée quand la période de signature est passée. _(155 car.)_
- Mots-clés : historique devis, RapidoCRM, CRM, devis, signature, suivi commercial
- YouTube : Historique des devis — RapidoCRM _(32 car.)_
