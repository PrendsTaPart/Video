# SPEC — montage de l'usine à vidéos FoodEatUp

Spécification de référence, alignée sur ce qui est réellement implémenté dans
`scripts/`. Les écarts par rapport au brief initial sont signalés « **Écart :** »
avec leur justification.

---

## 0. Timeline

Source de vérité : `config/episodes.json → formats`.

### `tiktok_30` — 1080×1920, 30 ips, 30,00 s

| Temps | Bloc | Source | Audio |
|---|---|---|---|
| 0,0 → 7,0 | **A — Hook** | `assets/hooks/EPxx.mp4` | son diégétique + punchline à 5,0 s |
| 7,0 → 9,0 | **B — Sting logo** | `assets/brand/sting-logo.mp4` | VO « FoodEatUp. » |
| 9,0 → 16,5 | **C — Problème** | `assets/brand/probleme.mp4` | VO bloc C |
| 16,5 → 26,0 | **D — Démo** | 4 sous-plans `build/demo_*.mp4` | VO bloc D |
| 26,0 → 30,0 | **E — Closing** | `assets/brand/outro.mp4` | VO bloc E |

### `linkedin_45` — 1080×1080, 30 ips, 45,00 s

10 s hook · 5 s sting · 12 s problème · 13 s démo · 5 s closing.

**Écart :** la version 1:1 n'est **pas** un recadrage du master vertical, elle est
réassemblée depuis les segments avec un style ASS dédié (`MarginV: 180`). Un
recadrage du master ferait sortir le hook incrusté à 700 px du bas hors cadre.

### Durées exactes

Toutes les durées de bloc tombent sur un nombre entier d'images à 30 ips
(210 + 60 + 225 + 285 + 120 = 900 images = 30,000 s).

Le bloc D se divise en 4 sous-plans : 9,5 s ÷ 4 = 2,375 s = **71,25 images**.
`ff.split_seconds()` répartit le reste (72, 71, 71, 71) au lieu d'arrondir
chaque part, ce qui ferait dériver la somme.

`ff.exact_cut()` borne chaque encodage : `-t` seul garde les images de pts < t
et laisse passer une image de trop une fois sur deux (constaté sur les sous-plans
de 2,3667 s) ; on ajoute `-frames:v N`. Le master est épinglé à 900 images à
l'étape logo — dernier ré-encodage vidéo de la chaîne.

---

## 1. `01_fetch_assets.py` — inventaire et sous-plans

### Logo

Via MCP RapidoCMS (`get_brand` + `list_all_files`) → `assets/brand/logo-foodeatup.png`.
Si le PNG n'a pas de fond transparent : `colorkey` en ffmpeg, **jamais** de
regénération IA.

### Captures produit

Via MCP Google Drive (`search_files` sur `episodes.json → drive.demo_clips`, puis
`download_file_content`) → `assets/demo/<nom>_raw.mp4`.

Le bloc D enchaîne `site_web` → `caisse_pos` → `kds` → `marketing`.

### Choix automatique du plan

1. **Point d'entrée** — score de changement de scène échantillonné à 5 Hz ; on
   garde la fenêtre la plus animée qui ne contient **aucune coupe franche**
   (score > 0,35). La recherche est limitée au corps du tuto (10 % → 85 %) :
   les tutos ouvrent sur un carton titre et ferment sur une page de fin.
2. **Zone d'action** — grille 3×3, énergie de différence temporelle par case
   (`tblend=difference` + `signalstats`) ; on retient la case qui bouge le plus.
   C'est là que se trouve le bouton cliqué ou la carte qui se génère.

Les choix sont figés dans `config/demo_cuts.json` (relus tels quels au run
suivant, éditables à la main) — le montage est donc reproductible.

### Cadrage du bloc D

**Écart majeur.** Le brief prévoyait `crop` centré vers 1080×1920. Les tutos sont
des captures **1920×828 (2,3:1)** : un recadrage 9:16 n'en garde que ~24 % de la
largeur et l'interface devient illisible — ni le bouton cliqué, ni son résultat.

Implémenté : **plein cadre sans jamais couper la capture**. Elle est affichée
entière, à la largeur du cadre, par-dessus un fond qui remplit tout l'écran — la
même image agrandie pour couvrir, floutée (`gblur=sigma=42`) et légèrement
assombrie. Aucune zone vide, aucun contenu perdu.

`zoom` reste à **1,0** dans `config/demo_cuts.json`. Une valeur > 1 rogne la
capture autour de la zone d'action détectée : à n'utiliser que si l'UI d'un tuto
donné est vraiment trop petite, en connaissance de cause.

### Garde-fou

`assets/hooks/EPxx.mp4` absent → `MISSING_HOOK EPxx`, épisode exclu du lot.
Hook trop court pour le format → `HOOK_TOO_SHORT`, épisode exclu. Aucune
génération de remplacement.

---

## 2. `02_generate_vo.py` — voix off

### Voix

`config/voices.json`. Le `voice_id` doit venir d'un appel réel à la liste des
voix ElevenLabs — **ne jamais l'inventer**. Au premier run, proposer 3 voix
françaises à l'humain et écrire son choix.

```json
{
  "voice_id": "<ID récupéré via la liste des voix>",
  "model_id": "eleven_multilingual_v2",
  "language": "fr",
  "settings": {"stability": 0.45, "similarity_boost": 0.75,
               "style": 0.35, "use_speaker_boost": true},
  "speed": 1.05
}
```

`stability` bas (0,45) = plus d'énergie, ce qu'il faut en short-form ; au-dessus
de 0,6 la voix devient plate.

### Coût

7 blocs communs générés **une seule fois** (B, C-30, C-45, D-30, D-45, E-30,
E-45) + 30 punchlines courtes. Un MP3 déjà présent est ignoré sans `--force`.

### Calage

Après génération, `ffprobe` mesure la durée. Écart > 8 % au-dessus de la cible →
nouvelle passe à `speed` +0,05 (2 essais, plafond 1,15). Au-delà : avertissement,
et c'est **le plan vidéo qui est étiré** à l'assemblage (`ff.freeze_pad`), pas la
voix qui est accélérée. Une VO accélérée s'entend, un plan tenu 0,5 s de plus non.
Plus court que la cible → on laisse le silence, ça respire.

Normalisation : `loudnorm=I=-16:TP=-1.5:LRA=11`.

---

## 3. `03_assemble.py` — montage

### 3.1 Normalisation

Profil commun avant concaténation (c'est ce qui permet le démuxeur `concat` sans
artefact) : `scale=increase` + `crop`, `fps=30`, `yuv420p`, H.264 high/4.1 CRF 18,
AAC 192k 48 kHz stéréo, `-video_track_timescale 30000`. Un segment sans piste
audio reçoit un `anullsrc`.

### 3.2 Coupe des blocs

Chaque bloc est coupé à la durée exacte de `episodes.json`. Pour le hook :
`cut_out` de l'épisode s'il est renseigné (la fenêtre se termine dessus), sinon
`cut_in`, sinon 0.

**Vérifier que le beat comique tombe dans la fenêtre.** EP11 (le livreur qui
tombe) a son beat à 7,4–8,0 s, hors des 7 premières secondes : d'où
`"cut_out": 8.6` dans `episodes.json`.

### 3.3 Incrustation du hook

En ASS (meilleur contour que `drawtext`, et modifiable sans recompiler un filtre),
police Anton chargée via `fontsdir`.

```
Style: Hook,Anton,96,&H00FFFFFF,&H00000000,&H00000000,&H80000000,-1,0,0,0,100,100,0,0,1,6,3,2,80,80,700,1
```

- Contour 6, ombre 3, blanc sur noir.
- 3 mots par ligne, **2 lignes max**. Plus de 6 mots → taille 82 plutôt qu'une
  3e ligne (elle sortirait des safe zones).
- Apparition / disparition sur `hook_text_in_s` / `hook_text_out_s`, fondu 0,2 s.
- `MarginV` : 700 en 9:16, 180 en 1:1.

**Écart :** `Alignment` = 2 (bas-centre) et non 5. En ASS v4+, 5 est le centre du
cadre et ignore `MarginV` ; 2 + `MarginV` donne exactement le « à 700 px du bas »
demandé par la charte.

**Piège :** échapper chaque ligne **avant** d'insérer le `\N`. Échapper après
transforme le saut de ligne en backslash littéral à l'écran.

### 3.4 Logo permanent

Coin haut-droit, hauteur 90 px, marge 40 px, opacité 85 %.

**Écart :** pendant le bloc B, le brief demandait une seconde instance du logo,
centrée et à pleine opacité. Le sting affiche **déjà** le logo en grand ; en
superposer un second par-dessus fait doublon. Implémenté : le filigrane du coin
passe à 100 % d'opacité sur l'intervalle du bloc B (deux overlays alternés par
`enable`). Le logo reste visible sur 100 % de la durée.

### 3.5 Transitions

Coupe franche entre A et B. Fondu au blanc 0,25 s entre D et E (sortie sur la fin
de D, entrée sur le début de E). Rien d'autre — pas d'empilement.

### 3.6 Mixage

Quatre sources : son diégétique du hook, VO commune, punchline, lit musical.

- La piste VO est construite par `adelay` + `amix` : chaque bloc à sa place,
  punchline à `punch_at_s`.
- **VO plus longue que son bloc** : elle est **avancée** pour finir avec le bloc,
  au lieu d'être tronquée par le `-t` final. Mordre sur la fin du bloc précédent
  s'entend beaucoup moins qu'une phrase coupée en plein mot (règle « ne jamais
  couper une VO »). Loggé en `INFO VO_AVANCEE`.
  Concerne surtout `E-closing-45` : 7,65 s mesurées pour un bloc de 5,0 s — la
  cible de 4,8 s du brief était irréaliste pour ce texte.
- Le lit musical est bouclé puis calé à **−22 LUFS** (loudnorm 2 passes, mis en
  cache par durée).
- `sidechaincompress` baisse la musique **et** le son diégétique dès que la voix
  parle. Sans ça la VO est mangée sur un haut-parleur de téléphone.
- Master : loudnorm **2 passes** vers −14 LUFS.

**Piège corrigé :** le filtre du brief réutilise `[1:a]` deux fois (clé du
sidechain + entrée du mix) — ffmpeg refuse. Il faut un `asplit`.

**Écart :** la consigne `TP` du loudnorm est −1,5 dBTP, pas −1,0. Le limiteur
dépasse légèrement sa consigne : viser −1,0 sortait à −0,85 dBTP et violait la
charte. La QA, elle, teste bien ≤ −1,0.

---

## 4. Contrôle qualité — bloquant

Rien n'est publiable si un test échoue. Verdict écrit dans le journal de run.

| Test | Méthode | Seuil |
|---|---|---|
| Durée | `ffprobe format=duration` | cible ±0,15 s |
| Résolution | `ffprobe` | 1080×1920 ou 1080×1080 |
| Loudness | `loudnorm print_format=json` | −14 ±1 LUFS |
| True peak | idem | ≤ −1,0 dBTP |
| Logo présent | 3 instants, écart moyen master **avant/après** incrustation sur la zone du logo | 3/3 |
| Pas de frame noire finale | `signalstats` YAVG à `durée−0,1 s` | > 12 |
| Audio non muet | `astats` RMS global | > −50 dB |

Le test « logo présent » compare `build/concat_*.mp4` et le master final au même
instant : dans la zone du logo l'écart doit être franc. C'est déterministe et ça
n'exige aucune bibliothèque d'image.

---

## 5. `04_publish_rapidocms.py` — brouillons planifiés

### Garde-fous

Le master doit exister **et** son dernier journal de run porter `publiable: true`
(QA 7/7 + voix off présente). Un master assemblé avec `--skip-vo` est refusé.

### Chaîne d'URL publique

`upload_file_tool` ne lit pas le disque, il exige une URL publique :

1. Drive `create_file` dans le dossier dédié « FoodEatUp — Vidéos promo »
   (pré-partagé « tous les utilisateurs disposant du lien » ; vérifier avec
   `get_file_permissions`).
2. `https://drive.google.com/uc?export=download&id=<FILE_ID>`
3. `RapidoCMS:upload_file_tool(file_url=…, name="EP01_tiktok_30", type="video")`

Si RapidoCMS refuse l'URL Drive (antivirus sur les gros fichiers) : basculer sur
un hébergement statique maîtrisé et le documenter. **Ne pas contourner en
regénérant la vidéo ailleurs.**

### Brouillons

`create_draft_tool` par réseau, `account_id` issu de `list_connected_accounts`
(jamais codé en dur) :

- `tiktok`, `instagram`, `facebook` → master `tiktok_30`
- `linkedin` → master `linkedin_45`

Caption = `episodes.json → caption` + hashtags du réseau.

TikTok : `privacy_level` reste `SELF_ONLY` par défaut, `PUBLIC_TO_EVERYONE`
seulement sur validation humaine explicite (`--tiktok-public`), avec
`your_brand=true`.

### Planification

3 publications par semaine et par réseau (lun / mer / ven), décalées de 2 h entre
réseaux. Les 30 épisodes couvrent ~10 semaines.

**Attention au format de `post_heure`.** La description de l'outil annonce
`H-i-s` (tirets) ; l'API a été vérifiée en `H:i:s` (deux-points) sur ce compte,
et l'heure est comparée à l'horloge **Europe/Paris**, pas UTC. Le script sort en
`H:i:s` par défaut, `--heure-separateur -` pour l'autre convention.

---

## 6. Journalisation

Chaque assemblage écrit `build/run_<horodatage>_<EP>_<format>.json` : fichiers
sources utilisés, durée de chaque bloc, résultat de chaque test QA, verdict de
publiabilité. C'est ce qui permet de rejouer ou d'auditer sans reconstruire le
raisonnement.

---

## 7. Ce qu'il ne faut pas faire

- Ne pas « améliorer » une vidéo ratée par une génération IA. Signaler, s'arrêter.
- Ne pas modifier hooks ou punchlines de `episodes.json` sans validation.
- Ne pas publier directement : uniquement des brouillons planifiés.
- Ne pas empiler les transitions.
