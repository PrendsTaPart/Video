# FoodEatUp — 48 vidéos montées à partir de la bibliothèque Higgsfield

Session du 2026-09-07. **Règle posée par Michael : uniquement des plans de la bibliothèque
Higgsfield.** Aucun screencast du logiciel, aucun plan du film héros, aucun avatar HeyGen
dans les livrables. La bibliothèque complète a été relevée (532 plans), téléchargée et
analysée et taguée plan par plan ; s'y ajoutent huit musiques originales et 64 voix off
ElevenLabs, et six animations reprises des projets déjà présents dans le dépôt.

## Livrables (`out/`)

| Film | Fichier | Durée | Format | Voix |
|---|---|---|---|---|
| Clip « Une journée. Une app. » | `foodeatup-clip.mp4` (+ `-16x9`) | 62 s | 1080×1920 | Paul K (4 lignes) |
| Présentation « Le même restaurant » | `foodeatup-presentation.mp4` (+ `-16x9`) | ~90 s | 1080×1920 | Anaïs (narratrice du film héros) |
| Commercial « Le contrôleur » | `foodeatup-commercial.mp4` (+ `-16x9`) | ~36 s | 1080×1920 | Paul K |
| Démo « Un tour du restaurant » | `foodeatup-demo.mp4` | ~1 min 45 | 1920×1080 | Enrick (tutoriel) |
| Short « Le contrôle » (HACCP) | `foodeatup-short-haccp.mp4` (+ `-16x9`) | ~25 s | 1080×1920 | Paul K |
| Short « L'inventaire » (stock) | `foodeatup-short-stock.mp4` (+ `-16x9`) | ~25 s | 1080×1920 | Paul K |
| Short « Le planning » (équipe) | `foodeatup-short-equipe.mp4` (+ `-16x9`) | ~26 s | 1080×1920 | Paul K |
| Short « L'addition » (compta) | `foodeatup-short-compta.mp4` (+ `-16x9`) | ~25 s | 1080×1920 | Paul K |
| Short « La double réservation » | `foodeatup-short-reservations.mp4` (+ `-16x9`) | ~25 s | 1080×1920 | Paul K |
| Short « L'avis du soir » | `foodeatup-short-avis.mp4` (+ `-16x9`) | ~24 s | 1080×1920 | Paul K |
| Avant/après « Le même restaurant, deux fois » | `foodeatup-avant-apres.mp4` (+ `-16x9`) | ~40 s | 1080×1920 | Anaïs |
| Bande-annonce | `foodeatup-teaser.mp4` (+ `-16x9`) | ~22 s | 1080×1920 | Paul K (signature seule) |

Les versions `-16x9` posent le 9:16 sur son propre fond flouté (LinkedIn, site, YouTube).

## Série « 30 problèmes, 30 solutions » (`serie30.py`)

Trente vidéos verticales de ~23 s, une par problème de restaurant, plus six clips
musicaux sans voix de ~32 s. Fichiers `out/foodeatup-s01-reservations.mp4` …
`out/foodeatup-s30-pilotage.mp4` et `out/foodeatup-clip-rush.mp4` … `-comedie.mp4`,
chacun avec sa version `-16x9`. Scripts dans `scripts/SERIE-30.md`, titres et
descriptions de diffusion dans `scripts/DIFFUSION.md`.

Chaque vidéo : animation d'accroche → deux plans « problème » → deux plans
« solution » → plan signature → carton final → sting animé. Les plans sont choisis
dans `assets/higgsfield-tags.json` par problème de restaurant, sans recoupement
entre thèmes.

## Animations du dépôt (`assets/anim/`)

Six animations réutilisables, remontées à partir des projets déjà présents dans le
dépôt (`videos/lancement-foodeatup-v1`, `videos/deux-boucles`,
`videos/foodeatup-8-boucles`) et d'un plan Higgsfield d'infini 3D :

| Fichier | Durée | Emploi |
|---|---|---|
| `hook-logo.mp4` | 1,5 s | accroche de tous les films |
| `sting-logo.mp4` | 2 s | signature de fin des formats courts |
| `sting-infini-3d.mp4` | 6 s | signature de fin des films longs et des clips |
| `hook-boucle.mp4` | 4 s | la boucle infinie et les 8 modules |
| `anim-8-logiciels.mp4` | 9,4 s | l'animation des 8 logiciels et leurs compteurs |
| `sting-cta-boucles.mp4` | 8,1 s | appel à l'action long |

`build_film(..., hook=..., sting=...)` les place automatiquement et décale les
repères d'incrustation et les voix off de la durée de l'accroche.

## Matière

- **Higgsfield** : **532 plans** relevés via l'API (6 pages d'historique, jusqu'à `next_cursor`
  nul), tous téléchargés dans `assets/higgsfield/` (lien symbolique vers le cache de session,
  non versionné) ; catalogue + prompts + analyse dans `assets/higgsfield-catalogue.json` et
  `HIGGSFIELD-BIBLIOTHEQUE.md`, tags complets dans `assets/higgsfield-tags.json`.
  Aucun plan n'a été régénéré. Le relevé a fait apparaître une matière que le premier
  passage sur 150 plans ne montrait pas : une série de **diptyques avant/après** tournés au
  même endroit, à la même heure, avec la même personne (index 434-481), et une série de
  plans de clôture et de logo. C'est de là que viennent les deux derniers films.
- **Musique** (ElevenLabs Music v2, instrumentales originales, `assets/music/`) :
  `musique-clip-123bpm.mp3` (62 s, electro-pop french touch, break au milieu) et
  `musique-underscore-99bpm.mp3` (2 min, piano/guitare/cordes sous voix), plus une variante `-alt` de chaque.
- **Voix off** (ElevenLabs `eleven_multilingual_v2`, `assets/vo/`) : scripts intégraux dans
  `scripts/VOIX-OFF.md`. Codes : C1-C4 clip, P1-P6 présentation, A1-A4 commercial (A3 = C3), D1-D9 démo.
  Flux ElevenLabs : https://elevenlabs.io/app/flows/P9XkZvN9YnnpIBmR2EF5
- **Pas de screencast, pas de HeyGen** : la première version de la démo et de la présentation
  utilisait les captures d'écran des tutoriels et l'avatar HeyGen existant ; elles ont été
  remontées en plans Higgsfield seuls, sur consigne. La démo devient « un tour du restaurant » :
  la voix off nomme les modules, l'image montre la scène de restaurant correspondante, en
  privilégiant les versions 16:9 natives de la bibliothèque.

## Refaire un rendu

```bash
cd videos/foodeatup-4-films
python3 build.py clip            # ou presentation | commercial | demo | all
python3 build.py avant_apres teaser
python3 shorts.py                # les six shorts ; ou shorts.py haccp stock ...
python3 serie30.py               # les 30 vidéos + les 6 clips ; ou serie30.py 01 07 rush
WORKDIR=work-a python3 serie30.py 01 05   # rendus parallèles, un répertoire de travail par lot
REMIX=1 python3 build.py clip    # ne refait que le mixage audio
```

`build.py` = moteur (découpe, mise à l'échelle, enchaînement, cartons Pillow, mixage avec
ducking sous la voix, loudnorm −14 LUFS). `films.py` = les six films longs et `shorts.py` les six
shorts, plan par plan, avec les timecodes d'entrée dans chaque source. Le ffmpeg utilisé est le binaire statique
d'`imageio-ffmpeg` (pas de `drawtext`, d'où les cartons PNG).

## À trancher avant diffusion

- L'URL affichée est `foodeatup.fr` (comme dans les voix off précédentes) ; l'app vit sur
  `foodeatup.com`. Modifier `url=` dans `end_card` si besoin, puis `REMIX` ne suffit pas :
  relancer le film.
- La durée d'essai n'est pas prononcée (7 jours dans le produit, 14 dans une ancienne VO).
- Les plans Higgsfield contiennent des dialogues lip-sync ; ils sont mixés très bas sous la
  musique et la voix. Vérifier à l'écoute qu'aucune réplique ne ressort.
