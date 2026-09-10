# Configurer Stripe

Module **Configuration** · V09 · `01-configurer-stripe`

## Hook

> Votre client veut payer maintenant. Vous, vous lui envoyez un RIB.
> Une clé collée, et vos documents s'encaissent en ligne.

**Alternatives proposées :**
1. Entre la facture envoyée et l'argent reçu, il y a souvent une relance de trop.
2. Un lien de paiement vaut mieux qu'un virement à retrouver.
3. Stripe branché, c'est le règlement au moment où le client le décide.

## Intro

On part de la section Stripe de votre page Profil, et on ressort avec les paiements en ligne branchés. Un seul champ à remplir : la clé secrète de votre compte Stripe. Elle relie RapidoCRM à votre compte, et vos documents commerciaux peuvent alors être réglés en ligne, au moment où le client le décide plutôt qu'au rythme de vos relances. Cette page rassemble d'ailleurs toutes vos connexions extérieures — Stripe, Twilio, la boîte mail — et chacune a son propre bouton d'enregistrement. C'est le piège classique de la page.

## Démo

### 1. Ouvrir la section Stripe

_0.0s → 2.5s · 7 mots · ~2.8s_

Page Profil, section Stripe. Paiements en ligne.

### 2. Situer Stripe parmi les connexions

_2.5s → 8.0s · 16 mots · ~6.4s_

Juste en dessous, Twilio : le même numéro sert à l'agent vocal et à vos sms.

### 3. Retrouver la page et ses onglets

_8.0s → 14.0s · 13 mots · ~5.2s_

Plus bas, la boîte mail. Et en haut, les onglets de la page.

### 4. Coller la clé secrète

_14.0s → 17.0s · 7 mots · ~2.8s_

La clé secrète se colle ici, masquée.

### 5. Enregistrer

_17.0s → 18.9s · 3 mots · ~1.2s_

Et on enregistre.

## Faites-le avec Claude

**Ensuite, demandez-lui.**

Stripe est branché. Pour suivre ce qui reste à encaisser sans ouvrir la facturation, RapidoCRM se branche sur Claude : vous écrivez votre demande en français, il lit vos données et vous répond, montant et statut compris. Copiez ce prompt, collez-le, et remplacez ce qui est entre crochets par le nombre de factures voulu.

```
Liste-moi mes [nombre] dernières factures avec leur montant et leur statut.
```

Résultat affiché : **5 factures trouvées** — FA-2026-048 — 1 480,00 € — payée · FA-2026-047 — 920,00 € — en attente

## Punchline

> Une clé aujourd'hui, et vos factures se règlent sans que vous relanciez.

**Alternatives proposées :**
1. Le paiement en ligne, c'est une relance de moins.
2. Vos documents savent maintenant encaisser.
3. Branché une fois, encaissé toujours.

## SEO

- Titre : Configurer Stripe sur RapidoCRM — tutoriel _(42 car.)_
- Description : Branchez Stripe sur RapidoCRM pour encaisser en ligne : la clé secrète, et vos documents commerciaux se règlent. Le tutoriel pas à pas de l'Académie. _(149 car.)_
- Mots-clés : configurer Stripe, RapidoCRM, paiement en ligne, clé secrète, facturation, configuration
- YouTube : Configurer Stripe — RapidoCRM _(29 car.)_
