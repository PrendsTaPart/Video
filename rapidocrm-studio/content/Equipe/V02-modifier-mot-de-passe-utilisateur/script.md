# Modifier son mot de passe

Module **Equipe** · V02 · `02-modifier-mot-de-passe-utilisateur`

## Hook

> Le compte est créé. Le mail d'activation, lui, n'est jamais arrivé.
> Votre commercial se donne un mot de passe en une minute.

**Alternatives proposées :**
1. Un accès bloqué le lundi matin, c'est une journée qui commence mal.
2. Personne n'a besoin de connaître le mot de passe d'un autre.
3. Le lien de réinitialisation règle l'activation comme l'oubli.

## Intro

On part de la page de connexion, et on ressort dans le tableau de bord du commercial. La procédure est la même dans deux cas : le mot de passe oublié, et le compte tout neuf dont le mail d'activation n'a pas pu partir. Le principe ne change pas : l'utilisateur demande un lien, le reçoit sur sa boîte, choisit son mot de passe. L'administrateur crée le compte, l'utilisateur choisit son mot de passe — les deux rôles restent séparés.

## Démo

### 1. Partir de la fiche du commercial

_0.0s → 4.5s · 14 mots · ~5.6s_

Le commercial existe dans la liste. Il lui manque juste son mot de passe.

### 2. Ouvrir « Mot de passe oublié »

_4.5s → 10.0s · 14 mots · ~5.6s_

Sur la page de connexion, le lien mot de passe oublié, sous le champ.

### 3. Demander le lien

_10.0s → 15.0s · 12 mots · ~4.8s_

On saisit l'adresse du compte, et on envoie le lien de réinitialisation.

### 4. Ouvrir le mail reçu

_15.0s → 21.0s · 13 mots · ~5.2s_

Le mail arrive dans la boîte : réinitialisation de votre mot de passe.

### 5. Choisir le nouveau mot de passe

_21.0s → 30.0s · 26 mots · ~10.4s_

Le lien ouvre la page de réinitialisation. Deux champs identiques, et on définit le nouveau mot de passe. Ce lien ne vaut que pour cette demande.

### 6. Se connecter

_30.0s → 42.0s · 34 mots · ~13.6s_

Retour à la connexion, avec le bandeau qui confirme : votre mot de passe a été modifié. S'il n'apparaît pas, le changement n'est pas passé. On saisit l'adresse et le nouveau mot de passe.

### 7. Arriver sur son tableau de bord

_42.0s → 47.8s · 11 mots · ~4.4s_

Et il est chez lui, sur son propre tableau de bord.

## Faites-le avec Claude

**Ensuite, demandez-lui.**

L'accès est ouvert. Pour vérifier qui a bien un compte actif sans ouvrir chaque fiche, RapidoCRM se branche sur Claude : vous écrivez votre demande en français, il lit vos données et vous répond. Copiez ce prompt, collez-le, et remplacez ce qui est entre crochets.

```
Liste-moi mes commerciaux [statut] avec leur adresse e-mail.
```

Résultat affiché : **3 commerciaux actifs** — Commercial terrain — actif · Chargée de clientèle — actif

## Punchline

> Un lien, un mot de passe, et votre commercial travaille.

**Alternatives proposées :**
1. L'activation ratée n'est plus un blocage, juste un détour.
2. Chacun son mot de passe, personne ne le partage.
3. Une minute de procédure vaut mieux qu'un accès qui traîne.

## SEO

- Titre : Modifier son mot de passe sur RapidoCRM — tutoriel _(50 car.)_
- Description : Définissez ou changez le mot de passe d'un utilisateur RapidoCRM : lien de réinitialisation, mail reçu, nouveau mot de passe. Le tutoriel de l'Académie. _(152 car.)_
- Mots-clés : mot de passe, RapidoCRM, réinitialisation, activation de compte, connexion, utilisateur
- YouTube : Modifier son mot de passe — RapidoCRM _(37 car.)_
