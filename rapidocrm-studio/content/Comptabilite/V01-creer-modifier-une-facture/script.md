# Créer et modifier une facture

Module **Comptabilite** · V01 · `05-creer-modifier-une-facture`

## Hook

> Votre facture part sur un tableur, recopiée à la main. Et le total, vous le vérifiez deux fois.
> Le produit choisi, les montants suivent.

**Alternatives proposées :**
1. Une facture retapée est une facture qui finit par se tromper.
2. Ce que vous vendez est déjà dans le logiciel. Vos factures aussi, alors.
3. Le calcul de TVA n'a pas à se faire de tête.

## Intro

On part de la page Facturation, et on ressort avec une facture faite, puis corrigée. Un seul formulaire : le client, le produit, la date. Les montants se calculent seuls. Retenez une chose : le prix toutes taxes comprises ne se tape jamais à la main.

## Démo

### 1. Ouvrir la page Facturation

_0.0s → 4.5s · 12 mots · ~4.8s_

Page Facturation. Trois onglets, deux filtres, et le bouton créer une facture.

### 2. Choisir le client et le produit

_4.5s → 12.0s · 18 mots · ~7.2s_

L'entreprise d'abord, prise dans vos clients. Puis le produit, avec son prix. C'est lui qui remplit la facture.

### 3. Laisser les montants se calculer

_12.0s → 19.0s · 13 mots · ~5.2s_

La date, puis les montants : hors taxes, TVA, total. Vous n'écrivez rien.

### 4. Fixer le délai et le statut

_19.0s → 25.0s · 16 mots · ~6.4s_

Le délai de paiement, les mentions légales, le statut. Le logiciel peut aussi envoyer la facture.

### 5. Relire les totaux

_25.0s → 29.0s · 12 mots · ~4.8s_

Dernière ligne : total TTC final. C'est ce que le client paiera.

### 6. Retrouver la facture au tableau

_29.0s → 36.0s · 15 mots · ~6.0s_

Facture créée. Elle prend sa place dans la liste, avec son client et son statut.

### 7. Corriger une facture

_36.0s → 48.5s · 13 mots · ~5.2s_

Une erreur de produit ? La fiche se rouvre telle quelle, on corrige.

### 8. Voir la correction confirmée

_48.5s → 55.2s · 6 mots · ~2.4s_

Et le bandeau confirme la modification.

## Faites-le avec Claude

**Ensuite, demandez-lui.**

Vos factures s'empilent. Pour savoir ce qui reste à encaisser, RapidoCRM parle à Claude : vous demandez en français, il lit vos données et répond. Copiez ce prompt, remplacez ce qui est entre crochets.

```
Liste-moi mes [nombre] dernières factures avec leur statut et leur montant.
```

Résultat affiché : **3 factures trouvées** — N° 3 — brasserie du quai — 5 760,00 € — En attente · N° 1 — brasserie du quai — 5 760,00 € — Payée

## Punchline

> Le produit choisi, la facture s'écrit. Et elle reste corrigeable.

**Alternatives proposées :**
1. Une facture juste du premier coup, et modifiable au second.
2. Vos prix vivent au catalogue, plus dans votre tête.
3. Facturer redevient une formalité de trente secondes.

## SEO

- Titre : Créer une facture sur RapidoCRM — tutoriel _(42 car.)_
- Description : Établissez une facture dans RapidoCRM : entreprise, produit, montants calculés, délai de paiement et statut. Le tutoriel pas à pas de l'Académie. _(145 car.)_
- Mots-clés : créer une facture, RapidoCRM, facturation, TVA, comptabilité, délai de paiement
- YouTube : Créer et modifier une facture — RapidoCRM _(41 car.)_
