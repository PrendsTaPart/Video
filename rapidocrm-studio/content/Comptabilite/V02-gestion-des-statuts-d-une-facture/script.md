# Changer le statut d'une facture

Module **Comptabilite** · V02 · `05-gestion-des-statuts-d-une-facture`

## Hook

> Le client a payé la semaine dernière. Votre liste, elle, le compte encore parmi les impayés.
> Deux clics, et vos relances redeviennent justes.

**Alternatives proposées :**
1. Relancer un client qui a déjà réglé coûte plus qu'un oubli.
2. Une facture réglée qui reste en attente fausse tout le reste.
3. Ce que vous avez encaissé mérite d'être écrit quelque part.

## Intro

On part de la liste des factures, et on ressort avec une facture passée de en attente à payée. Le statut ne se change pas depuis le tableau : il vit dans le formulaire de la facture, juste au-dessus du mode de paiement. Et c'est voulu — le logiciel vous fait dire dans le même geste que l'argent est arrivé, et par quel moyen. Dans la liste, la couleur fait le reste : rouge pour ce qui reste dû, vert pour ce qui est encaissé. Un coup d'œil vous dit qui relancer.

## Démo

### 1. Repérer le statut dans la liste

_0.0s → 5.0s · 17 mots · ~6.8s_

La colonne Statut. Rouge pour en attente, vert pour payée. Ici, la première facture n'est pas réglée.

### 2. Ouvrir la facture

_5.0s → 10.5s · 12 mots · ~4.8s_

On rouvre la facture. Le formulaire revient tel qu'il a été rempli.

### 3. Passer en payée, et dire comment

_10.5s → 15.5s · 15 mots · ~6.0s_

Statut : payée. Et juste en dessous, le moyen — espèces, carte, virement ou chèque.

### 4. Voir la liste à jour

_15.5s → 18.4s · 6 mots · ~2.4s_

Et la ligne passe au vert.

## Faites-le avec Claude

**Ensuite, demandez-lui.**

Vos statuts sont à jour. Pour savoir ce qui reste à encaisser sans parcourir la liste, RapidoCRM se branche sur Claude : vous écrivez votre demande en français, il lit vos données et vous répond, montant et date compris. Copiez ce prompt, collez-le, et lancez-le tel quel.

```
Liste-moi mes factures en attente avec leur montant et leur date.
```

Résultat affiché : **2 factures en attente** — N° 2 — cabinet lefèvre — 5 760,00 € — 24/08/2026 · N° 5 — olive & lin — 3 360,00 € — 26/08/2026

## Punchline

> Un statut à jour, et vous ne relancez plus ceux qui ont payé.

**Alternatives proposées :**
1. La couleur de la ligne vous dit qui appeler.
2. Encaissé, c'est écrit. Impayé aussi.
3. Vos relances valent ce que vaut votre suivi.

## SEO

- Titre : Statut d'une facture sur RapidoCRM — tutoriel _(45 car.)_
- Description : Passez une facture de en attente à payée dans RapidoCRM, avec son mode de paiement, et gardez une liste d'impayés juste. Le tutoriel de l'Académie. _(147 car.)_
- Mots-clés : statut facture, RapidoCRM, facture payée, impayés, relance client, comptabilité
- YouTube : Changer le statut d'une facture — RapidoCRM _(43 car.)_
