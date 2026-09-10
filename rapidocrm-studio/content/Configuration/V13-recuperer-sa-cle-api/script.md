# Récupérer sa clé API

Module **Configuration** · V13 · `01-recuperer-sa-cle-api`

## Hook

> Une application extérieure veut vos données. Vous lui donnez tout, ou rien.
> Un token, et vous choisissez exactement ce qu'elle peut faire.

**Alternatives proposées :**
1. Donner un accès ne devrait pas vouloir dire donner les clés de la maison.
2. Lire vos contacts, oui. Supprimer vos factures, non.
3. Un token par application, et vous coupez celui que vous voulez.

## Intro

On part de l'onglet Tokens api de votre page Profil, et on ressort avec une clé d'accès taillée sur mesure. Un token, c'est ce que vous remettez à une application extérieure pour qu'elle atteigne votre CRM. Vous décidez de deux choses : jusqu'à quelle date elle y a droit, et ce qu'elle peut faire, ressource par ressource. Lire seulement, ou aussi créer, modifier, supprimer.

## Démo

### 1. Ouvrir l'onglet Tokens api

_0.0s → 4.0s · 11 mots · ~4.4s_

Onglet Tokens api : les clés d'accès de vos applications externes.

### 2. Créer un nouveau token

_4.0s → 14.0s · 21 mots · ~8.4s_

Bouton nouveau token. Nommez-le d'après l'application à qui vous le donnez : le jour où elle part, vous saurez lequel couper.

### 3. Fixer une date d'expiration

_14.0s → 19.0s · 13 mots · ~5.2s_

Puis une date d'expiration. Passée cette date, la clé cesse de fonctionner d'elle-même.

### 4. Cocher les permissions

_19.0s → 28.0s · 28 mots · ~11.2s_

Le tableau croise vos ressources et quatre droits : lire, créer, modifier, supprimer. Ici, on ne coche que lire. Un token en lecture seule ne peut rien casser.

### 5. Générer le token

_28.0s → 34.0s · 12 mots · ~4.8s_

On génère. La ligne apparaît : nom, portée, dernière utilisation, expiration, statut.

### 6. Relire ses permissions

_34.0s → 39.0s · 12 mots · ~4.8s_

Un clic sur les pastilles rouvre la liste complète de ses droits.

### 7. Révoquer un token

_39.0s → 43.2s · 14 mots · ~5.6s_

Et la corbeille le révoque, après confirmation. Les applications qui s'en servaient perdent l'accès.

## Faites-le avec Claude

**Ensuite, demandez-lui.**

Votre token est prêt. Pour voir ce qu'il pourra lire avant de le remettre, RapidoCRM se branche sur Claude : vous écrivez votre demande en français, il lit vos données et vous répond. Copiez ce prompt, collez-le, et remplacez ce qui est entre crochets.

```
Liste-moi mes [nombre] dernières entreprises avec leur nom.
```

Résultat affiché : **5 entreprises trouvées** — Atelier Leroy — Nantes · Studio Nord — Lille

## Punchline

> Un token par application, et vous reprenez la clé quand vous voulez.

**Alternatives proposées :**
1. Lecture seule aujourd'hui, révocation demain.
2. Donner un accès, ce n'est pas donner la maison.
3. Une clé datée, c'est une clé qui s'oublie sans danger.

## SEO

- Titre : Récupérer sa clé API RapidoCRM — tutoriel _(41 car.)_
- Description : Créez un token d'API sur RapidoCRM : nom, date d'expiration et permissions ressource par ressource, puis révocation. Le tutoriel de l'Académie. _(143 car.)_
- Mots-clés : clé API, RapidoCRM, token, permissions, développeur, configuration
- YouTube : Récupérer sa clé API — RapidoCRM _(32 car.)_
