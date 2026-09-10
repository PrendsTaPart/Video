# Créer un contrat

Module **CrmMarketing** · V19 · `06-creer-un-contrat`

## Hook

> Le devis est accepté. Reste à sortir un contrat, à le relire, à trouver la bonne adresse.
> Un modèle, deux dates, et il part.

**Alternatives proposées :**
1. Un contrat repart rarement de zéro : il repart d'un modèle.
2. Le plus long dans un contrat, c'est souvent de le retrouver.
3. Ce qui est signé compte ; ce qui traîne en brouillon, non.

## Intro

On part de la fiche d'une entreprise, et on ressort avec un contrat envoyé. La bibliothèque propose des modèles, le formulaire tient en quatre champs, et le logiciel confirme l'envoi.

## Démo

### 1. Ouvrir « Créer un contrat » depuis la fiche

_1.0s → 4.5s · 6 mots · ~2.4s_

Panneau Finance : créer un contrat.

### 2. Choisir un modèle dans la bibliothèque

_4.5s → 9.5s · 10 mots · ~4.0s_

La bibliothèque annonce ses modèles. Chacun dit ce qu'il couvre.

### 3. Vérifier le destinataire du contrat

_9.5s → 15.0s · 12 mots · ~4.8s_

Le destinataire est déjà rempli : c'est le client de la fiche.

### 4. Fixer les dates de début et de fin

_15.0s → 26.0s · 25 mots · ~10.0s_

Puis les deux bornes. La date de début ouvre l'engagement, la date de fin le referme. C'est elle qui dira, plus tard, qu'il faut renouveler.

### 5. Choisir le modèle d'e-mail et envoyer

_26.0s → 31.0s · 8 mots · ~3.2s_

Le message qui portera le contrat, puis envoyer.

### 6. Lire la confirmation

_31.0s → 39.0s · 19 mots · ~7.6s_

Le bandeau confirme : le contrat est envoyé. Il rejoint l'historique du client, où on ira lire son statut.

## Faites-le avec Claude

**Et pour savoir qui n'a pas signé ?**

Un contrat envoyé n'est pas un contrat signé. Pour voir ceux qui attendent, RapidoCRM parle à Claude : vous demandez en français, il lit vos données et répond. Copiez ce prompt, remplacez ce qui est entre crochets.

```
Liste-moi mes [nombre] contrats en attente avec leur destinataire et leurs dates.
```

Résultat affiché : **3 contrats en attente** — Prestation web — 28/08/2026 → 28/10/2027 · Maintenance — 01/09/2026 → 31/08/2027 · Vente de produits — 15/09/2026 → 15/03/2027

## Punchline

> Un modèle, deux dates, un message : le contrat part le jour où le devis est accepté.

**Alternatives proposées :**
1. La bibliothèque garde les modèles ; vous gardez le temps.
2. Un contrat envoyé vite est un contrat signé plus tôt.
3. Ce qui est daté se renouvelle ; ce qui ne l'est pas s'oublie.

## SEO

- Titre : Créer un contrat — RapidoCRM _(28 car.)_
- Description : Envoyez un contrat depuis la fiche d'une entreprise RapidoCRM : modèle de la bibliothèque, destinataire, dates de validité et modèle d'e-mail. Le tutoriel. _(155 car.)_
- Mots-clés : contrat, RapidoCRM, modèle de contrat, CRM, signature, commercial
- YouTube : Créer un contrat — RapidoCRM _(28 car.)_
