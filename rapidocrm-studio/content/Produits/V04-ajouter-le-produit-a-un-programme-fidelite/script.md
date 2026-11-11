# Rattacher un produit à un programme de fidélité

Module **Produits** · V04 · `03-ajouter-le-produit-a-un-programme-fidelite`

## Hook

> Votre programme de fidélité tourne. Mais aucun produit ne dit combien il rapporte.
> Deux champs, en bas de la fiche produit, et l'affaire est réglée.

**Alternatives proposées :**
1. Des points de fidélité qui ne sont attachés à rien ne récompensent personne.
2. Le réglage que tout le monde cherche dans le menu fidélité est ailleurs.
3. Un produit qui rapporte des points se vend différemment.

## Intro

On part de la fiche d'un produit déjà créé, et on ressort avec ce produit rattaché à un programme de fidélité. Le réglage n'est pas dans le menu de la fidélité : il ferme le formulaire du produit, juste après la description. Une question, oui ou non. Si vous répondez oui, deux champs s'ouvrent : le programme concerné, et le nombre de points que l'achat fait gagner. Rien n'est définitif — la question se rouvre à chaque modification de la fiche.

## Démo

### 1. Descendre au bas de la fiche produit

_0.0s → 8.0s · 21 mots · ~8.4s_

Bas de la fiche du produit, après la description. La dernière question du formulaire : ajouter au programme de fidélité ?

### 2. Répondre oui à la question

_8.0s → 11.5s · 6 mots · ~2.4s_

On répond oui. Deux champs apparaissent.

### 3. Choisir le programme et les points

_11.5s → 18.0s · 18 mots · ~7.2s_

Le programme, dans la liste — avec son nombre de clients. Puis les points que l'achat fait gagner.

### 4. Voir la confirmation

_18.0s → 24.0s · 11 mots · ~4.4s_

Et le bandeau confirme : produit modifié. Le rattachement est enregistré.

## Faites-le avec Claude

**Ensuite, demandez-lui.**

Reste à savoir si le programme choisi est vivant. RapidoCRM se branche sur Claude : vous écrivez votre demande en français, il lit vos données et vous répond. Copiez ce prompt, collez-le, et vous obtenez vos programmes avec leur nombre de clients et les points déjà offerts. De quoi vérifier, avant de rattacher, que vous visez le bon.

```
Liste-moi mes programmes de fidélité avec leur nombre de clients et les points offerts.
```

Résultat affiché : **Programmes de fidélité** — Alexa — 0 client — 0 point offert · Fidélité boutique — 12 clients — 340 points offerts

## Punchline

> Un produit, un programme, un nombre de points. La fidélité devient concrète.

**Alternatives proposées :**
1. Ce qui rapporte des points mérite d'être écrit sur la fiche.
2. Le barème se décide une fois, et il tient.
3. Vos clients réguliers savent enfin ce qu'ils gagnent.

## SEO

- Titre : Produit et programme de fidélité — RapidoCRM _(44 car.)_
- Description : Rattachez un produit RapidoCRM à un programme de fidélité : la question en bas de la fiche, le programme, les points. Le tutoriel de l'Académie. _(144 car.)_
- Mots-clés : programme de fidélité, RapidoCRM, points fidélité, produit, catalogue, clients réguliers
- YouTube : Rattacher un produit à un programme de fidélité — RapidoCRM _(59 car.)_
