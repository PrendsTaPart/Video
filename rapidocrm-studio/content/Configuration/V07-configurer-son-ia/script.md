# Configurer son IA

Module **Configuration** · V07 · `01-configurer-son-ia`

## Hook

> Votre agent tourne sur la clé de tout le monde. La vôtre dort dans un coin.
> Un champ, et l'agent travaille sur votre compte.

**Alternatives proposées :**
1. Vous payez déjà un fournisseur d'IA. Autant que l'agent s'en serve.
2. Une clé collée, et la consommation passe chez vous.
3. Le champ vide n'éteint rien — encore faut-il le savoir.

## Intro

On part de la section Agent ia de votre page Profil, et on ressort avec votre propre clé d'API branchée. Par défaut, l'agent de RapidoCRM tourne sur la clé du serveur, celle que tout le monde partage. En collant la vôtre, il consomme votre compte chez votre fournisseur — anthropic, openai, gemini ou openrouter — et vous voyez exactement ce qu'il dépense. Le champ laissé vide ne coupe rien : l'agent repart simplement sur la clé du serveur, qui fonctionne.

## Démo

### 1. Trouver la section Agent ia

_0.0s → 4.0s · 11 mots · ~4.4s_

Page Profil, section Agent ia. Une clé personnelle pour votre agent.

### 2. Repérer les autres réglages

_4.0s → 8.0s · 13 mots · ~5.2s_

La page empile vos connexions : l'IBAN, la boîte mail, Stripe et Twilio.

### 3. Coller sa propre clé

_8.0s → 12.0s · 14 mots · ~5.6s_

Le champ attend une clé anthropic, openai, gemini ou openrouter. On colle la sienne.

### 4. Enregistrer

_12.0s → 14.5s · 4 mots · ~1.6s_

Un clic sur enregistrer.

### 5. Laisser vide pour la clé du serveur

_14.5s → 22.0s · 20 mots · ~8.0s_

Videz-le, et l'agent ne s'arrête pas : il repart sur la clé globale du serveur. C'est écrit sous le champ.

## Faites-le avec Claude

**Ensuite, demandez-lui.**

Votre clé est en place. Pour vérifier l'état de votre agent sans rouvrir la page, RapidoCRM se branche sur Claude : vous écrivez votre demande en français, il lit vos données et vous répond. Copiez ce prompt, collez-le, et lancez-le tel quel — il n'y a rien à remplacer.

```
Montre-moi la configuration de mon agent vocal : objectif d'appel, ton de voix et minutes restantes.
```

Résultat affiché : **Agent vocal — configuration** — Objectif : prise de rendez-vous · Minutes restantes : 128

## Punchline

> Votre clé, votre compte, votre agent. Et le filet du serveur si vous la retirez.

**Alternatives proposées :**
1. Un champ rempli, et l'agent travaille chez vous.
2. Vide ou remplie, l'agent répond toujours.
3. La clé du serveur reste là, en filet.

## SEO

- Titre : Configurer son IA sur RapidoCRM — tutoriel _(42 car.)_
- Description : Branchez votre propre clé d'API sur l'agent IA de RapidoCRM : anthropic, openai, gemini ou openrouter. Le tutoriel pas à pas de l'Académie, en une minute. _(154 car.)_
- Mots-clés : configurer son IA, RapidoCRM, clé api, agent IA, openai, configuration
- YouTube : Configurer son IA — RapidoCRM _(29 car.)_
