# Configurer son IMAP

Module **Configuration** · V06 · `01-configurer-son-imap`

## Hook

> Vos factures partent de votre webmail, et le CRM n'en sait rien.
> Cinq champs, et votre messagerie entre dans RapidoCRM.

**Alternatives proposées :**
1. Écrire à un client ne devrait pas demander de changer d'onglet.
2. Une messagerie branchée, et vos envois laissent une trace.
3. Le jour où le CRM lit vos mails, vous arrêtez de jongler.

## Intro

On part de la section Boîte mail de votre page Profil, et on ressort avec la messagerie de la société branchée. C'est ce réglage qui ouvre la page Boîte mail du CRM : vous écrivez à vos clients et vous leur envoyez devis et factures sans repasser par votre webmail. Deux préalables, côté Google : la validation en deux étapes doit être active sur le compte de la société, et c'est un mot de passe d'application qu'on colle ici, jamais celui de votre compte.

## Démo

### 1. Ouvrir la section Boîte mail

_0.0s → 5.0s · 16 mots · ~6.4s_

Dans votre page Profil, la section Boîte mail. Cinq champs, et le CRM lit votre messagerie.

### 2. Coller le mot de passe d'application

_5.0s → 10.0s · 17 mots · ~6.8s_

Le mot de passe d'application, généré chez Google. Pas celui de votre compte : Google le refuserait.

### 3. Renseigner les quatre paramètres

_10.0s → 14.5s · 12 mots · ~4.8s_

Hôte imap point gmail point com, port 993, chiffrement ssl, certificat true.

### 4. Enregistrer

_14.5s → 17.0s · 7 mots · ~2.8s_

Un clic sur enregistrer, et c'est branché.

### 5. Vérifier la fiche complétée

_17.0s → 20.4s · 5 mots · ~2.0s_

Ces quatre-là ne changent jamais.

## Faites-le avec Claude

**Ensuite, demandez-lui.**

Votre messagerie est branchée : la page Boîte mail du CRM s'ouvre désormais. Pour retrouver à qui vous écrivez sans quitter la conversation, RapidoCRM se branche sur Claude : vous écrivez votre demande en français, il lit vos données et vous répond. Copiez ce prompt, collez-le, et remplacez ce qui est entre crochets.

```
Liste-moi mes [nombre] derniers contacts avec leur adresse e-mail.
```

Résultat affiché : **5 contacts trouvés** — Martin Leroy — contact@atelier-leroy.fr · Claire Dubois — c.dubois@studio-nord.fr

## Punchline

> Cinq champs une fois, et vos mails partent d'ici.

**Alternatives proposées :**
1. Une messagerie branchée, c'est un onglet de moins.
2. Vos devis et vos factures partent maintenant de la maison.
3. Le CRM sait enfin écrire à vos clients.

## SEO

- Titre : Configurer son IMAP sur RapidoCRM — tutoriel _(44 car.)_
- Description : Branchez la messagerie de votre société sur RapidoCRM : mot de passe d'application Google, hôte, port et chiffrement. Le tutoriel pas à pas de l'Académie. _(154 car.)_
- Mots-clés : configurer son IMAP, RapidoCRM, boîte mail, mot de passe d'application, Gmail, configuration
- YouTube : Configurer son IMAP — RapidoCRM _(31 car.)_
