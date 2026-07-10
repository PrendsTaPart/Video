# Intégrations à appliquer (patchs cross-skills)

> Ces skills vivent dans le **dépôt plugin** (pas dans ce dépôt vidéo). Applique-y les patchs
> ci-dessous pour brancher `gestion-marques` sur la chaîne de contenu.

## 1. contenu-conforme-marque — étape 0

**Avant** : l'étape 0 lit la charte depuis la KB uniquement.
**Après** : l'étape 0 lit **`get_brand` (état serveur) + les assets de la marque cible**, en plus
de la KB.

Règles :
- La **KB reste la source de vérité** pour le ton et les règles éditoriales.
- **Écart KB ↔ serveur** (couleur, logo, slogan) → **le signaler** à l'utilisateur et **proposer
  la synchro** via `mise-a-jour-kb` (dans un sens ou l'autre, sur accord).
- Multi-marques → hérite du garde-fou §0 de `gestion-marques` : **marque cible obligatoire**.

Pseudo-étape 0 :
```
0. Résoudre la marque cible (demander si ambiguïté).
   b = get_brand(brand_id) ; assets = list_all_files(search="<Marque> — ")
   kb = charte-graphique.md (source de vérité éditoriale)
   si divergence(b, kb) -> signaler + proposer mise-a-jour-kb
   charger couleurs(kb/b), ton(kb), logo(asset officiel) AVANT génération.
```

## 2. video-marketing + prompts-visuels-pro — source des logos

**Avant** : les logos du pipeline vidéo venaient de fichiers **« logos GitHub »**.
**Après** : les logos viennent des **assets de marque** (`add_asset` → URL publique via
`get_brand`/`list_all_files`).

Patch de la note du pipeline vidéo :
```
- AVANT : « logos : depuis le dépôt GitHub (raw URL) »
- APRÈS : « logos : assets officiels de la marque cible (bibliothèque CMS, URL publique).
           Récupérer via list_all_files(search='<Marque> — logo') ; fallback GitHub
           uniquement si l'asset de marque n'existe pas encore (et le créer via add_asset). »
```

## 3. Rappel de cohérence
Tout skill qui **publie** (posts, cartes, vidéos) doit passer par l'agent
`gestionnaire-marques` : marque cible identifiée → charte chargée → logo officiel → publication.
