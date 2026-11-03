---
name: gestion-marques
version: 1.0.0
cluster: rapidocms
description: >-
  Utiliser quand l'utilisateur veut créer ou modifier une marque, gérer plusieurs
  marques (multi-enseignes), ajouter un logo ou un asset de marque, ou parle de la
  charte d'une de ses marques. Gère la bibliothèque d'assets officiels par marque et
  garantit la cohérence multi-enseignes avant toute génération de contenu.
tools:
  - create_brand
  - edit_brand
  - delete_brand
  - add_asset
  - remove_asset
  - get_brand
  - upload_file_tool
  - list_all_files
agent: gestionnaire-marques
---

# gestion-marques — piloter les marques RapidoCMS

Ce skill gère le **cluster marques** de RapidoCMS : création, modification, suppression
d'une marque, et sa **bibliothèque d'assets officiels** (logos, visuels clés). C'est la
brique qui garantit qu'un contenu part toujours à la **bonne charte, pour la bonne enseigne**.

> **Schéma vivant.** Les schémas ci-dessous reflètent le contrat live des tools au moment
> de la rédaction. **Avant toute écriture, ré-introspecte le tool** (surtout l'enum
> `font_family` et les champs requis de `create_brand`) : si le serveur a changé, le
> serveur fait foi — adapte-toi et signale l'écart à l'utilisateur.

---

## 0. Multi-marques : jamais de défaut silencieux

BraindCode opère **plusieurs enseignes** (BraindCode, FoodEatUp, PronoClip, PrendsTaPart, RapidoSoftware…).

**Règle d'or** : dès qu'une action porte sur « la marque » (créer un contenu, un post, un
visuel, une vidéo…) et que **plusieurs marques existent**, **DEMANDE toujours pour quelle
marque** — jamais de défaut implicite. Puis **charge ses couleurs / son ton / son logo**
(`get_brand` + assets de la marque) **avant** de générer quoi que ce soit.

Si un **nouveau projet** apparaît sans marque correspondante → **propose de créer la marque
manquante** (via ce skill) plutôt que d'inventer une identité.

---

## 1. Créer une marque — `create_brand`

**Contrat live** :

| Champ | Requis | Format |
|---|---|---|
| `nom` | ✅ | texte |
| `langue` | ✅ | ex. `fr`, `en` |
| `slogan` | ✅ | texte court |
| `couleurs` | — | hex séparés par des virgules : `#1B2A41,#00A8F0` |
| `font_family` | — | **ENUM web-safe** (voir §1.2) |
| `logo` | — | **URL PUBLIQUE** (voir §1.3) |
| `site_web` | — | URL http(s) |

### 1.1 Couleurs — jamais inventées
Prends les couleurs depuis **`./rapido-kb/charte-graphique.md`** (source de vérité).
Format attendu par le serveur : hex, en majuscules ou minuscules, **séparés par des
virgules, sans espaces superflus** (`#1B2A41,#00A8F0,#48A850`). Ne **jamais** deviner une
couleur : si la charte ne la donne pas, demande-la à l'utilisateur.

### 1.2 `font_family` — mapping vers l'ENUM (introspection obligatoire)
Le serveur n'accepte que des **piles web-safe**. À la rédaction, l'enum est :

```
"Arial, sans-serif" · "Verdana, sans-serif" · "Tahoma, sans-serif" ·
"Trebuchet MS, sans-serif" · "Georgia, serif" · "Times New Roman, serif" ·
"Garamond, serif" · "Courier New, monospace" · "Lucida Console, monospace"
```

**Procédure** : lis la typo réelle dans la charte, **liste l'enum par introspection du tool**,
choisis la pile **la plus proche**, puis **dis-le explicitement à l'utilisateur** (« ta charte
utilise *Poppins* ; la police web-safe la plus proche disponible est *Trebuchet MS* — je pars
là-dessus, OK ? »). Table d'aide (indicative, à confirmer par l'utilisateur) :

| Typo charte | Pile web-safe la plus proche |
|---|---|
| Poppins / Montserrat / Futura (géométrique) | `Trebuchet MS, sans-serif` |
| Inter / Helvetica / Roboto (grotesque neutre) | `Arial, sans-serif` |
| Open Sans / Segoe (humaniste) | `Verdana, sans-serif` |
| Serif éditorial (Playfair, Merriweather) | `Georgia, serif` |
| Serif classique | `Times New Roman, serif` |
| Mono / technique | `Courier New, monospace` |

### 1.3 `logo` — URL publique obligatoire
`create_brand.logo` exige une **URL publique**. Si l'utilisateur fournit un fichier local ou
une image non hébergée : **uploade d'abord via `upload_file_tool`** (type `image`), récupère
la `file_url` retournée, **puis** utilise cette URL dans `logo`. Ne passe jamais un chemin
local ni une URL privée/expirable.

### 1.4 Confirmation — NIVEAU 2 (récap avant appel)
Toute **écriture de marque** (`create_brand` / `edit_brand`) est un **niveau 2** : présente un
**récapitulatif complet** (nom, langue, slogan, couleurs exactes, font_family choisie + justif,
URL logo, site) et **attends l'accord explicite** avant l'appel. Pas de création « à la volée ».

---

## 2. Modifier une marque — `edit_brand`
Requis : `brand_id`. Ne passe **que** les champs à modifier (les autres restent inchangés).
Mêmes règles couleurs/font/logo qu'au §1. **Confirmation niveau 2** (récap avant/après).
Récupère l'état courant via `get_brand` pour montrer le diff.

## 3. Supprimer une marque — `delete_brand` (GARDE-DESTRUCTIF)
Requis : `brand_id`. **Action irréversible.** Garde-fou : demande à l'utilisateur de
**retaper le nom EXACT** de la marque ; ne procède que si la saisie correspond au champ `nom`
de la marque ciblée. Rappelle ce qui sera perdu (assets liés, références). Aucun « delete » implicite.

---

## 4. Bibliothèque d'assets par marque — `add_asset` / `remove_asset`

Chaque marque a une **bibliothèque d'assets officiels** : logos fond transparent, déclinaisons,
visuels clés réutilisables (pipeline vidéo, posts, cartes).

**Contrat live** :
- `add_asset(asset_id, brand_id)` — lie un fichier **déjà présent dans la bibliothèque** de
  l'utilisateur à la marque. L'asset doit exister (uploade-le via `upload_file_tool` si besoin,
  récupère son `id` via `list_all_files`).
- `remove_asset(asset_id)` — délie l'asset de la marque.

**Convention de nommage** (au moment de l'upload, champ `name` de `upload_file_tool`) :

```
"<Marque> — <type> — <variante>"
```

Exemples : `FoodEatUp — logo — fond transparent` · `BraindCode — logo — monochrome blanc` ·
`RapidoSoftware — visuel clé — hub MCP`. Cette convention rend les assets **retrouvables par
nom** (les routines et le pipeline vidéo s'appuient dessus).

**Flux type « ajouter un logo »** :
1. `upload_file_tool(type=image, name="<Marque> — logo — fond transparent", file_url=<url publique>)` → `file_url` + entrée biblio.
2. `list_all_files(type=image, search="<Marque> — logo")` → récupère l'`asset_id`.
3. `add_asset(asset_id, brand_id)`.

---

## 5. Lecture — `get_brand`
`get_brand` renvoie l'état **serveur** d'une marque (couleurs, font, logo, slogan). C'est la
référence pour un diff avant `edit_brand`, et pour charger l'identité avant de générer un contenu (§0).

---

## Intégrations (voir INTEGRATIONS.md — à appliquer côté plugin)
- **contenu-conforme-marque** : l'étape 0 lit désormais `get_brand` + les assets de la marque
  cible. La **KB reste la source de vérité** ; en cas d'écart KB ↔ serveur, **le signaler** et
  proposer la synchro via **mise-a-jour-kb**.
- **video-marketing** + **prompts-visuels-pro** : les **logos viennent des assets de marque**
  (URL publique), plus des « logos GitHub ». Met à jour la note du pipeline vidéo.

## Garde-fous (résumé)
- Multi-marques → **toujours demander la marque cible**, jamais de défaut silencieux.
- Écriture marque → **confirmation niveau 2** (récap complet).
- `delete_brand` → **nom exact retapé**.
- Couleurs → **depuis la charte**, jamais inventées.
- `font_family` → **ENUM introspecté**, choix expliqué à l'utilisateur.
- `logo` / assets → **URL publique** via `upload_file_tool` d'abord.
