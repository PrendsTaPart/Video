# Retrouver un devis et le rouvrir

Module **Comptabilite** · V12 · `05-historique-des-devis`

## Hook

> Le client vous rappelle au sujet d'un devis de mars. Vous, vous faites défiler la liste.
> Deux filtres, et quatre gestes par ligne.

**Alternatives proposées :**
1. Chercher un devis à la main, c'est du temps qu'on ne facture pas.
2. Un historique sert s'il se filtre.
3. Le devis d'il y a six mois est à deux clics.

## Intro

On part de l'historique des devis, et on ressort avec le bon devis sous les yeux. Deux listes en haut de page filtrent, et chaque ligne porte un menu qui dit ce qu'on peut en faire.

## Démo

### 1. Ouvrir l'historique des devis

_0.0s → 6.0s · 9 mots · ~3.6s_

L'onglet devis. Deux filtres, une recherche, et le tableau.

### 2. Ouvrir le menu d'une ligne

_6.0s → 12.0s · 12 mots · ~4.8s_

Les trois points en fin de ligne ouvrent le menu. Quatre entrées.

### 3. Visualiser le devis

_12.0s → 18.0s · 14 mots · ~5.6s_

Visualiser ouvre le devis dans un nouvel onglet. La liste reste où elle est.

### 4. Télécharger le devis

_18.0s → 24.0s · 10 mots · ~4.0s_

Télécharger sort le fichier. Le navigateur le prend en charge.

### 5. Les autres actions de la ligne

_24.0s → 28.1s · 13 mots · ~5.2s_

Et les deux dernières : modifier, ou basculer sur la fiche du client.

## Faites-le avec Claude

**Ensuite, demandez-lui.**

Les filtres trient à l'écran. Pour le même point sans toucher aux listes, RapidoCRM parle à Claude : vous demandez en français, il lit vos données et répond. Copiez ce prompt, remplacez ce qui est entre crochets.

```
Liste-moi mes [nombre] derniers devis avec leur destinataire, leur statut et leur montant.
```

Résultat affiché : **5 devis au total** — N° 5 — brasserie du quai — 7 018,95 € — Accepté · N° 2 — cabinet lefèvre — 5 760,00 € — En attente · N° 4 — agence lumière — 5 760,00 € — Refusé

## Punchline

> Deux filtres posés, et le bon devis est devant vous.

**Alternatives proposées :**
1. Un historique qui se filtre est un historique qui sert.
2. Quatre gestes par ligne, aucun détour.
3. Le devis se relit sans quitter la liste.

## SEO

- Titre : Retrouver un devis — RapidoCRM _(30 car.)_
- Description : Filtrez l'historique des devis RapidoCRM par statut et par entreprise, puis visualisez ou téléchargez la ligne trouvée. Le tutoriel de l'Académie. _(146 car.)_
- Mots-clés : historique des devis, RapidoCRM, filtrer, télécharger, commercial, CRM
- YouTube : Retrouver un devis dans l'historique — RapidoCRM _(48 car.)_
