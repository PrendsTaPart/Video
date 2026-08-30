# Où en est la série, et ce qu'il reste à faire

Audit du 30 août 2026, croisant trois sources : les données du site
(`food-series-hub`), le contenu réel de `dist/`, et une vérification HTTP des
1 288 adresses que le site déclare.

## Ce que le projet annonce

Cinq séries, dix-neuf saisons, **367 épisodes**. Chaque épisode se décline en six
pièces : le master 9:16, la story Instagram, le Short YouTube, la version
paysage 16:9, la story Facebook et la vidéo TikTok.

| Série | Saisons | Épisodes | Statut annoncé |
|---|---:|---:|---|
| Le Coup de Feu | 8 | 240 | en cours |
| UpEatFood (*Il était une fois un restaurant*) | 5 | 35 | à venir |
| Une journée | 2 | 31 | à venir |
| L'IA dans FoodEatUp | 3 | 31 | à venir |
| Michael fait son cinéma | 1 | 30 | à venir |

## Ce qui existe vraiment

| Série / saison | éps | master | story | short | paysage | facebook | tiktok |
|---|---:|---:|---:|---:|---:|---:|---:|
| Michael fait son cinéma | 30 | 0 | 0 | 0 | 0 | 0 | 0 |
| Coup de Feu · S1 | 30 | 24 | 30 | 30 | 30 | 30 | 30 |
| Coup de Feu · S2 | 30 | 25 | 30 | 30 | 30 | 30 | 30 |
| Coup de Feu · S3 | 30 | 21 | 30 | 30 | 30 | 30 | 30 |
| Coup de Feu · S4 | 30 | 10 | 29 | 29 | 29 | 29 | 29 |
| Coup de Feu · S5 | 30 | 10 | 28 | 28 | 28 | 28 | 28 |
| Coup de Feu · S6 | 30 | 0 | 9 | 9 | 9 | 0 | 0 |
| Coup de Feu · S7 | 30 | 0 | 2 | 2 | 2 | 1 | 1 |
| Coup de Feu · S8 | 30 | 0 | 2 | 2 | 2 | 0 | 0 |
| Une journée · S1 | 15 | 15 | 15 | 15 | 15 | 15 | 15 |
| Une journée · S2 | 16 | 16 | 16 | 16 | 16 | 16 | 16 |
| L'IA dans FoodEatUp · S1 | 7 | 0 | 3 | 3 | 3 | 2 | 2 |
| L'IA dans FoodEatUp · S2 | 10 | 0 | 1 | 1 | 1 | 1 | 1 |
| L'IA dans FoodEatUp · S3 | 14 | 0 | 2 | 2 | 2 | 1 | 1 |
| UpEatFood · S1 à S5 | 35 | 35 | 35 | 35 | 35 | 35 | 35 |
| **Total** | **367** | **156** | **232** | **232** | **232** | **218** | **218** |
| **Manquant** | | **211** | **135** | **135** | **135** | **149** | **149** |

Deux séries sont complètes sur les six pièces : **Une journée** (31/31) et
**UpEatFood** (35/35). Le Coup de Feu a ses déclinaisons jusqu'à la saison 5 mais
pas ses masters — les stories se montent depuis le plan Higgsfield, pas depuis le
master, donc un épisode peut exister en story sans exister en master. Les
saisons 6 à 8, L'IA dans FoodEatUp et Michael fait son cinéma sont à l'état de
texte.

## Le problème d'hébergement, qui bloque toute la diffusion

Sur les 1 288 adresses déclarées par le site, **921 pointent sur
`raw.githubusercontent.com`**, c'est-à-dire sur une branche de travail du dépôt,
et 367 seulement sur la bibliothèque RapidoCMS.

| Pièce | RapidoCMS | GitHub raw |
|---|---:|---:|
| master | 82 | 74 |
| story | 61 | 171 |
| Short YouTube | 221 | 11 |
| paysage 16:9 | 1 | 231 |
| story Facebook | 1 | 217 |
| vidéo TikTok | 1 | 217 |

GitHub raw n'est pas un hébergeur vidéo : il répond en `application/octet-stream`,
il limite les robots, et une branche a vocation à disparaître. Les 1 288 adresses
répondent depuis un navigateur, mais **YouTube a refusé en 403** le premier
fichier servi par GitHub qu'on lui a demandé d'ingérer (EP523).

Conséquence directe : seuls les Shorts sont réellement diffusables aujourd'hui.
Le paysage, Facebook et TikTok sont à verser dans la bibliothèque avant de
pouvoir être publiés — 665 fichiers.

## L'état de diffusion : rien n'est parti

Avant cette session, sur 367 épisodes × 5 réseaux : **zéro publication**. Huit
créneaux Facebook et un par autre réseau étaient marqués « planifié », le reste
« à venir ». Le calendrier commençait le 24 août 2026 ; six épisodes avaient donc
déjà leur date derrière eux.

Fait depuis, sur la chaîne YouTube FoodEatUp :

- **5 épisodes publiés** (EP501 → EP505, les retards d'UpEatFood) ;
- **24 Shorts planifiés** aux dates du calendrier, du 31 août au 28 septembre.

Le quota YouTube est la contrainte dure : **10 000 unités par jour, 1 600 par
envoi, soit six vidéos par jour maximum**. Les 232 Shorts représentent 39 jours de
quota s'ils partaient tous maintenant. C'est pourquoi la planification utilise le
mode `upload_at_time` : l'envoi a lieu le jour prévu et ne consomme rien
aujourd'hui.

## Ce qu'il reste à faire, dans l'ordre

### 1. Finir le remontage du Coup de Feu (en cours)

Les 24 masters de la saison 1 sont remontés (carton « huit logiciels », punchline
incrustée, raccords). Les saisons 2 à 5 — **66 masters** — passent par le même
`remonter-saison.sh`. Sans ça, une saison dit « huit » et la suivante « dix ».

### 2. Trois voix à refaire avant publication

| Épisode | Ce qui dit encore « dix » | Quoi faire |
|---|---|---|
| EP010 | punchline ElevenLabs | nouvelle voix : « Pour huit outils qui ne se parlent pas. » |
| EP013 | script HeyGen de l'avatar | nouveau rendu : « Une seule interface, pas huit. » |
| EP022 | punchline ElevenLabs | nouvelle voix : « Pour huit logiciels qui ne se parlent même pas. » |

Les trois sont marqués `a_refaire` dans `state/`. Réglages figés sur les 153
fichiers : `eleven_multilingual_v2`, stability 0.55, similarity 0.80, style 0.15,
speaker boost, `mp3_44100_128`. **L'identifiant de voix des punchlines n'est
écrit nulle part** — `config/voices.json`, que le brief 08 réclame, n'existe pas.
C'est le premier trou à combler.

Leurs stories, Shorts, paysages, Facebook et TikTok portent le même texte
incrusté : il faut les remonter aussi (`REFAIRE=1 build-stories.py`, puis les
quatre déclinaisons).

### 3. Verser les déclinaisons dans la bibliothèque

665 fichiers servis par GitHub raw à basculer sur RapidoCMS, en commençant par ce
qui sort le plus tôt. Sans ça, ni YouTube en paysage, ni Facebook, ni TikTok ne
peuvent ingérer quoi que ce soit.

### 4. Les 211 masters manquants

- **32 épisodes attendent un tournage** : les modules Caisse POS, HubRise et KDS
  n'ont aucune vidéo dans le Drive, seulement des JPG (`drive-map.json` dit
  lesquels). Six d'entre eux sont en saison 1 : EP004, EP009, EP011, EP012,
  EP027, EP028.
- **Saisons 6, 7 et 8 du Coup de Feu** (90 épisodes), **L'IA dans FoodEatUp**
  (31) et **Michael fait son cinéma** (30) n'ont ni plan Higgsfield complet ni
  avatar. Ce sont trois chantiers de production, pas de montage.

### 5. Planifier le reste de la diffusion

- **YouTube** : 197 Shorts restants sur les 221 ingérables, plus les 11 qui
  attendent leur bascule vers la bibliothèque. Un appel de planification par
  vidéo, à la date du calendrier.
- **Facebook, Instagram, TikTok, LinkedIn** : rien n'est planifié, et rien ne
  peut l'être avant le point 3. Le catalogue impose en plus un verrou humain —
  une pièce doit être passée en `valide` par quelqu'un qui l'a regardée en
  entier ; aucun outil n'écrit cet état, et c'est voulu.

### 6. Les arbitrages de montage laissés ouverts

Détaillés dans `AUDIT-MONTAGE-SAISON-1.md` : la fin à neuf secondes (deux cartons
de marque à la suite, 24 % de l'épisode), le carton du milieu (6,2 s figées sur
9), et le screencast incrusté trop petit pour être lu sur un téléphone. Les trois
touchent les gabarits communs, donc les 150 épisodes d'un coup.
