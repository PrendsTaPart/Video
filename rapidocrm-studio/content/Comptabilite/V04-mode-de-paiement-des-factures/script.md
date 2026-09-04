# Renseigner le mode de paiement d'une facture

Module **Comptabilite** · V03 · `05-mode-de-paiement-des-factures`

## Hook

> Un virement tombe sur le compte. Trois semaines plus tard, vous cherchez encore à quelle facture il correspond.
> Un champ coché le jour même, et le rapprochement se fait tout seul.

**Alternatives proposées :**
1. Un règlement sans moyen noté, c'est une recherche pour plus tard.
2. La banque dit combien. Elle ne dit jamais pourquoi.
3. Ce qui se retrouve en dix secondes se note en une.

## Intro

On part de la liste des factures, et on ressort avec un règlement documenté. Le mode de paiement se choisit dans le formulaire de la facture, sous le statut : espèces, carte bleue, virement ou chèque. Un seul à la fois. Le champ porte une étoile, le logiciel l'attend. Et juste en dessous, le récapitulatif rappelle les montants — c'est le total TTC final, remise déduite, qu'il faudra retrouver sur votre relevé. Rien à calculer, tout est à l'écran au moment de valider.

## Démo

### 1. Ouvrir la facture réglée

_0.0s → 6.0s · 13 mots · ~5.2s_

Depuis la liste, les trois points en fin de ligne ouvrent la facture.

### 2. Choisir le moyen

_6.0s → 11.5s · 7 mots · ~2.8s_

Quatre moyens, un seul coché. Ici, virement.

### 3. Contrôler le montant

_11.5s → 14.5s · 9 mots · ~3.6s_

En dessous, le total à retrouver sur le relevé.

### 4. Enregistrer

_14.5s → 18.9s · 5 mots · ~2.0s_

On enregistre, et c'est écrit.

## Faites-le avec Claude

**Ensuite, demandez-lui.**

Le règlement est documenté. Pour rouvrir une facture précise sans la chercher dans la liste, RapidoCRM se branche sur Claude : vous écrivez votre demande en français, il lit vos données et vous répond. Copiez ce prompt, collez-le, et remplacez ce qui est entre crochets par le numéro de la facture.

```
Donne-moi le détail de la facture numéro [id].
```

Résultat affiché : **Facture n° 3** — brasserie du quai — 5 760,00 € TTC — Payée · Mode de paiement : virement

## Punchline

> Un moyen de paiement noté, c'est un rapprochement en moins à faire.

**Alternatives proposées :**
1. Dix secondes aujourd'hui, une demi-heure économisée en fin de mois.
2. Votre relevé et vos factures parlent enfin la même langue.
3. Ce qui est écrit ne se cherche pas.

## SEO

- Titre : Mode de paiement d'une facture — RapidoCRM _(42 car.)_
- Description : Notez par quel moyen une facture RapidoCRM a été réglée — espèces, carte, virement ou chèque — et retrouvez vos encaissements. Le tutoriel de l'Académie. _(153 car.)_
- Mots-clés : mode de paiement, RapidoCRM, facture, virement, rapprochement bancaire, comptabilité
- YouTube : Renseigner le mode de paiement d'une facture — RapidoCRM _(56 car.)_
