# Configurer son IBAN

Module **Configuration** · V10 · `01-configurer-son-iban`

## Hook

> Votre facture est partie. Le client la lit, et cherche où virer l'argent.
> Trois champs, et vos documents disent où vous payer.

**Alternatives proposées :**
1. Une facture sans coordonnées bancaires, c'est un paiement reporté.
2. Le RIB se saisit une fois, et il suit toutes vos factures.
3. Trois champs séparent votre facture de son règlement.

## Intro

On part de la section Informations bancaires de votre page Profil, et on ressort avec les coordonnées de règlement de la société. Ce sont elles qui s'impriment sur vos factures : le nom de votre banque, son code, et votre IBAN. Sans elles, le client reçoit un document juste, mais il ne sait pas où envoyer l'argent. Tout se lit sur le RIB que votre banque vous a remis.

## Démo

### 1. Ouvrir les informations bancaires

_0.0s → 6.0s · 13 mots · ~5.2s_

Page Profil, section Informations bancaires. Sous-titre : coordonnées bancaires de facturation. Trois champs.

### 2. Nommer sa banque

_6.0s → 10.0s · 11 mots · ~4.4s_

Le nom de l'établissement d'abord, tel qu'il apparaîtra sur vos documents.

### 3. Renseigner le code guichet

_10.0s → 15.0s · 11 mots · ~4.4s_

Puis son code, cinq chiffres, lu lui aussi sur votre RIB.

### 4. Saisir l'IBAN

_15.0s → 24.0s · 21 mots · ~8.4s_

Et l'IBAN, d'un seul tenant, sans les espaces du RIB papier. Relisez-le : une faute passe inaperçue et bloque le virement.

### 5. Enregistrer

_24.0s → 28.0s · 11 mots · ~4.4s_

Un clic sur enregistrer, et vos factures savent où vous payer.

## Faites-le avec Claude

**Ensuite, demandez-lui.**

Vos coordonnées sont en place. Pour relire ce qui est parti sans ouvrir la facturation, RapidoCRM se branche sur Claude : vous écrivez votre demande en français, il lit vos données et vous répond. Copiez ce prompt, collez-le, et remplacez ce qui est entre crochets par le nombre de factures voulu.

```
Liste-moi mes [nombre] dernières factures avec leur montant total.
```

Résultat affiché : **5 factures trouvées** — FA-2026-052 — 2 100,00 € · FA-2026-051 — 640,00 €

## Punchline

> Un RIB saisi une fois, et plus jamais de facture muette sur le paiement.

**Alternatives proposées :**
1. Vos factures disent enfin où vous payer.
2. Trois champs, et le virement part sans question.
3. Le RIB une fois, le paiement à chaque fois.

## SEO

- Titre : Configurer son IBAN sur RapidoCRM — tutoriel _(44 car.)_
- Description : Renseignez les coordonnées bancaires de votre société sur RapidoCRM : banque, code guichet et IBAN sur vos factures. Le tutoriel pas à pas de l'Académie. _(153 car.)_
- Mots-clés : configurer son IBAN, RapidoCRM, coordonnées bancaires, facturation, RIB, configuration
- YouTube : Configurer son IBAN — RapidoCRM _(31 car.)_
