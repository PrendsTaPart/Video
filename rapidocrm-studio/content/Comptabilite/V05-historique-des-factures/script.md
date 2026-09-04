# Retrouver une facture dans l'historique

Module **Comptabilite** · V04 · `05-historique-des-factures`

## Hook

> Un client conteste une facture d'il y a six mois. Vous, vous faites défiler la liste.
> Deux filtres croisés, et il ne reste que ce que vous cherchez.

**Alternatives proposées :**
1. Chercher une facture ne devrait pas prendre plus de temps que la lire.
2. Une liste qui grossit sans filtres devient une archive morte.
3. Ce qu'on retrouve vite, on le renvoie vite.

## Intro

On part de l'historique complet et on ressort avec la facture voulue, prête à être renvoyée. Deux listes déroulantes en haut de page : le statut et l'entreprise. Elles se cumulent, et le compteur sous le tableau vous dit toujours combien de lignes ont été retenues, et sur combien au total. C'est important : tant qu'un filtre est actif, ce que vous ne voyez pas n'a pas disparu. Et sur chaque ligne, un menu donne quatre gestes — visualiser, modifier, télécharger, ou basculer sur la fiche du client.

## Démo

### 1. Ouvrir l'historique

_0.0s → 11.0s · 17 mots · ~6.8s_

L'historique des factures. Toutes y sont, la plus récente en tête, avec son client et son montant.

### 2. Croiser les deux filtres

_11.0s → 22.0s · 30 mots · ~12.0s_

Le statut, puis l'entreprise. Les deux se cumulent. Et quand rien ne correspond, le tableau le dit franchement : aucun résultat trouvé. Ce n'est pas une panne, c'est une réponse.

### 3. Lire ce qui a été retenu

_22.0s → 39.0s · 27 mots · ~10.8s_

On change d'entreprise, et deux factures apparaissent. Le compteur précise : deux entrées, filtrées à partir de cinq. Vous savez toujours ce que le filtre a écarté.

### 4. Visualiser ou télécharger

_39.0s → 47.4s · 13 mots · ~5.2s_

Et le menu de la ligne : visualiser, modifier, télécharger, ou voir l'entreprise.

## Faites-le avec Claude

**Ensuite, demandez-lui.**

Les filtres font le tri à l'écran. Pour obtenir le même point sans toucher aux listes, RapidoCRM se branche sur Claude : vous écrivez votre demande en français, il lit vos données et vous répond, statut et montant compris. Copiez ce prompt, collez-le, et lancez-le tel quel.

```
Liste-moi mes factures du mois avec leur statut et leur montant.
```

Résultat affiché : **5 factures ce mois-ci** — N° 11 — olive & lin — 3 360,00 € — En attente · N° 3 — brasserie du quai — 5 760,00 € — Payée

## Punchline

> Deux filtres, et la bonne facture est sous vos yeux.

**Alternatives proposées :**
1. Une archive qui répond vaut mieux qu'une archive complète.
2. Le compteur vous dit ce que vous ne voyez pas.
3. Retrouver, relire, renvoyer. Sans quitter la page.

## SEO

- Titre : Historique des factures — RapidoCRM _(35 car.)_
- Description : Filtrez l'historique des factures RapidoCRM par statut et par entreprise, puis visualisez ou téléchargez le document. Le tutoriel de l'Académie. _(144 car.)_
- Mots-clés : historique factures, RapidoCRM, filtrer, télécharger facture, comptabilité, archives
- YouTube : Retrouver une facture dans l'historique — RapidoCRM _(51 car.)_
