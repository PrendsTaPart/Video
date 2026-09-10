# Historique facture

Module **CrmMarketing** · V33 · `06-historique-facture`

## Hook

> « Où en est mon compte ? » Le client demande, et vous ouvrez trois onglets.
> Un tableau répond : statut et total, ligne par ligne.

**Alternatives proposées :**
1. Le total TTC est souvent la seule information cherchée.
2. Ce qui est facturé se lit ; ce qui est encaissé aussi.
3. Un duplicata se retrouve plus vite qu'il ne se refait.

## Intro

On part de la page Historique, et on ressort avec la facture ouverte. Le tableau donne le statut et le total ; l'icône en bout de ligne ouvre le document, prêt à télécharger. Rien à recalculer, rien à reconstituer : la facture est déjà écrite.

## Démo

### 1. Ouvrir l'historique des factures

_1.0s → 8.0s · 16 mots · ~6.4s_

Deuxième rangée de la page Historique : les factures. On consulte, et le tableau se charge.

### 2. Lire les colonnes du tableau

_8.0s → 11.8s · 9 mots · ~3.6s_

Statut et total TTC : l'essentiel se lit ici.

### 3. Ouvrir une facture

_11.8s → 15.5s · 7 mots · ~2.8s_

L'icône ouvre la facture dans un onglet.

### 4. Lire la facture et la télécharger

_15.5s → 18.2s · 5 mots · ~2.0s_

Et le bouton Télécharger l'enregistre.

## Faites-le avec Claude

**Et pour ce qui reste à encaisser ?**

Le journal montre un client. Pour voir toutes les factures qui attendent, RapidoCRM parle à Claude : vous demandez en français, il lit vos données et répond. Copiez ce prompt, remplacez ce qui est entre crochets.

```
Liste-moi mes [nombre] factures en attente avec leur montant.
```

Résultat affiché : **3 factures en attente** — N° 17 — 1 258,95 € · N° 18 — 1 440,00 € · N° 19 — 4 320,00 €

## Punchline

> Le statut au tableau, le détail dans la facture : la question du client trouve sa réponse.

**Alternatives proposées :**
1. Un duplicata se télécharge, il ne se recompose pas.
2. Le total TTC est écrit ; inutile de le recalculer.
3. La facture s'ouvre dans un onglet : le journal reste derrière.

## SEO

- Titre : Historique des factures — RapidoCRM _(35 car.)_
- Description : Consultez le journal des factures d'un client dans RapidoCRM : statut, total TTC, ouverture de la facture et téléchargement du document. Le tutoriel. _(149 car.)_
- Mots-clés : historique facture, RapidoCRM, CRM, facturation, encaissement, suivi client
- YouTube : Historique des factures — RapidoCRM _(35 car.)_
