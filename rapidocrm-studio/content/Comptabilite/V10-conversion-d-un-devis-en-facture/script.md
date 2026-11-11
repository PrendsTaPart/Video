# Transformer un devis accepté en facture

Module **Comptabilite** · V10 · `05-conversion-d-un-devis-en-facture`

## Hook

> Le devis est accepté. Et vous vous apprêtez à retaper les mêmes lignes dans une facture.
> Signez le devis, la facture se crée toute seule.

**Alternatives proposées :**
1. Retaper une facture depuis un devis, c'est une erreur qui attend son tour.
2. Ce qui a été accepté n'a pas à être ressaisi.
3. Le devis signé contient déjà tout ce qu'il faut facturer.

## Intro

On part d'un devis en attente, et on ressort avec une facture. Il n'y a pas de bouton « convertir » : c'est la signature du devis qui crée la facture, avec le même client et le même montant.

## Démo

### 1. Ouvrir le devis à convertir

_0.0s → 6.0s · 11 mots · ~4.4s_

On ouvre le devis par Signer, comme pour le faire valider.

### 2. Signer le devis et enregistrer

_6.0s → 29.0s · 26 mots · ~10.4s_

Le devis s'ouvre, on signe, et on enregistre. Le logiciel travaille : il signe le devis, crée la facture, et tente d'envoyer le mail au client.

### 3. Lire ce que le logiciel annonce

_29.0s → 34.0s · 15 mots · ~6.0s_

Le bandeau dit tout : devis signé, facture créée. Seul le mail n'est pas parti.

### 4. Passer à l'onglet facture

_34.0s → 46.0s · 21 mots · ~8.4s_

On passe à l'onglet facture. En haut, les compteurs se sont recalculés : le total facturé a grimpé, l'en attente aussi.

### 5. Retrouver la facture créée

_46.0s → 55.5s · 18 mots · ~7.2s_

Et la voilà, en tête de liste. Même client, même montant que le devis, avec son propre numéro.

## Faites-le avec Claude

**Ensuite, demandez-lui.**

La facture existe. Pour vérifier ce qui vient de partir en facturation, RapidoCRM parle à Claude : vous demandez en français, il lit vos données et répond. Copiez ce prompt, remplacez ce qui est entre crochets.

```
Liste-moi mes [nombre] dernières factures avec leur statut et leur montant.
```

Résultat affiché : **5 factures ce mois-ci** — N° 11 — olive & lin — 3 360,00 € — En attente · N° 10 — brasserie du quai — 7 018,95 € — En attente · N° 3 — brasserie du quai — 5 760,00 € — Payée

## Punchline

> Un devis signé, une facture créée. Vous n'avez rien retapé.

**Alternatives proposées :**
1. La signature fait le travail de la saisie.
2. Ce qui est accepté devient facturable sans détour.
3. Un geste, deux documents cohérents.

## SEO

- Titre : Convertir un devis en facture — RapidoCRM _(41 car.)_
- Description : Transformez un devis accepté en facture sur RapidoCRM : signer le devis crée la facture, avec le même client et le même montant. Le tutoriel de l'Académie. _(155 car.)_
- Mots-clés : devis en facture, RapidoCRM, conversion, facturation, signature, CRM
- YouTube : Convertir un devis en facture — RapidoCRM _(41 car.)_
