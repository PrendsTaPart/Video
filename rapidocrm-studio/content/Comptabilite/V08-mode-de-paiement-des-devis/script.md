# Renseigner le mode de paiement d'un devis

Module **Comptabilite** · V08 · `05-mode-de-paiement-des-devis`

## Hook

> Le client vous dit qu'il paiera par virement. Trois semaines plus tard, personne ne s'en souvient.
> Une case cochée sur le devis, et c'est écrit.

**Alternatives proposées :**
1. Ce qui se dit au téléphone ne se retrouve pas dans un dossier.
2. Le moyen de paiement se décide avant la facture, pas après.
3. Un devis complet, c'est un devis qui dit aussi comment on règle.

## Intro

On part de la liste des devis, et on ressort avec un moyen de paiement noté sur l'un d'eux. Le réglage est dans le devis, sous le statut : espèce, carte, virement ou chèque. Une seule case à la fois.

## Démo

### 1. Ouvrir la liste des devis

_0.0s → 4.5s · 11 mots · ~4.4s_

L'onglet devis, et la liste. Les trois points ouvrent le menu.

### 2. Ouvrir le devis en modification

_4.5s → 8.5s · 10 mots · ~4.0s_

Modifier. Le formulaire se rouvre tel qu'il a été rempli.

### 3. Descendre au mode de paiement

_8.5s → 12.5s · 12 mots · ~4.8s_

On descend au bloc Mode de paiement. Quatre moyens, et une étoile.

### 4. Choisir le mode et enregistrer

_12.5s → 15.0s · 5 mots · ~2.0s_

Virement. Puis modifier, en bas.

### 5. Lire la confirmation

_15.0s → 17.1s · 3 mots · ~1.2s_

Et c'est enregistré.

## Faites-le avec Claude

**Ensuite, demandez-lui.**

Le moyen est noté. Pour retrouver les devis qui attendent encore une réponse, RapidoCRM parle à Claude : vous demandez en français, il lit vos données et répond. Copiez ce prompt, remplacez ce qui est entre crochets.

```
Liste-moi mes [nombre] devis en attente avec leur destinataire et leur montant.
```

Résultat affiché : **3 devis en attente** — N° 2 — cabinet lefèvre — 5 760,00 € · N° 3 — olive & lin — 3 360,00 € · N° 4 — agence lumière — 5 760,00 €

## Punchline

> Un moyen de paiement noté sur le devis, c'est une question de moins à la facture.

**Alternatives proposées :**
1. Ce qui est coché se retrouve ; ce qui est dit se perd.
2. Le devis dit ce qu'on vend, et comment on est payé.
3. Une case aujourd'hui, un rapprochement en moins demain.

## SEO

- Titre : Mode de paiement d'un devis — RapidoCRM _(39 car.)_
- Description : Renseignez le mode de paiement d'un devis RapidoCRM : espèce, carte, virement ou chèque, dans le formulaire du devis. Le tutoriel de l'Académie. _(144 car.)_
- Mots-clés : mode de paiement, devis, RapidoCRM, virement, facturation, CRM
- YouTube : Mode de paiement d'un devis — RapidoCRM _(39 car.)_
