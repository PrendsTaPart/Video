# Historique document

Module **CrmMarketing** · V32 · `06-historique-document`

## Hook

> Deux versions de la même carte, deux mois d'écart. Laquelle renvoyer au client ?
> La date d'ajout tranche, et le fichier se télécharge d'ici.

**Alternatives proposées :**
1. Un document sans date est un document sans version.
2. Télécharger vaut mieux que reconstituer.
3. Ce qui est attaché au client se retrouve depuis le client.

## Intro

On part de la page Historique, et on ressort avec le document en main. Le tableau donne le nom, le type, le poids et la date. Le menu de la ligne télécharge ou supprime.

## Démo

### 1. Ouvrir l'historique des documents

_1.0s → 8.5s · 19 mots · ~7.6s_

Deuxième rangée de la page Historique : les documents. Le message de liste vide s'affiche le temps du chargement.

### 2. Lire le tableau des documents

_8.5s → 14.0s · 12 mots · ~4.8s_

Nom du fichier, type, taille, date d'ajout : une ligne par pièce.

### 3. Télécharger ou supprimer un document

_14.0s → 17.5s · 8 mots · ~3.2s_

Le menu de la ligne propose les deux.

### 4. Annuler et revenir à la liste

_17.5s → 19.2s · 6 mots · ~2.4s_

On annule : rien n'a bougé.

## Faites-le avec Claude

**Et pour relire tout le dossier ?**

Les documents ne sont qu'une partie de la fiche. Pour la relire d'un coup, RapidoCRM parle à Claude : vous demandez en français, il lit vos données et répond. Copiez ce prompt, remplacez ce qui est entre crochets.

```
Donne-moi la fiche complète de l'entreprise numéro [identifiant].
```

Résultat affiché : **Fiche entreprise** — Documents : 2 · Contacts : 4 · Employés : 1

## Punchline

> Un document daté, pesé, téléchargeable : la bonne version part du premier coup.

**Alternatives proposées :**
1. La date d'ajout dit ce que le nom de fichier tait.
2. Supprimer se confirme ; télécharger ne se regrette pas.
3. Deux actions dans un menu, et le dossier reste propre.

## SEO

- Titre : Historique des documents — RapidoCRM _(36 car.)_
- Description : Consultez le journal des documents d'un client dans RapidoCRM : nom, type, taille, date d'ajout, puis téléchargement ou suppression. Le tutoriel. _(145 car.)_
- Mots-clés : historique document, RapidoCRM, CRM, PDF, suivi client, pièce jointe
- YouTube : Historique des documents — RapidoCRM _(36 car.)_
