# S01E01 — « Il cherchait le poivre. »

1080×1920 · 30 ips. Trente secondes de film, puis la méthode — en 15 s ou en 20 s,
les deux sont livrées.
Le film raconte Christophe Colomb parti chercher le poivre ; le bloc méthode explique,
en cinq étapes, comment le spectateur peut faire la même publicité lui-même.

**Aucune vidéo n'a été générée.** Les trois plans existaient déjà dans la bibliothèque
Higgsfield et ont été récupérés par MCP. C'est la règle du dépôt et celle du plan de montage.

## Les livrables

Deux montages du même épisode. Le bloc film est identique dans les deux ; seul le bloc
méthode change de rythme.

**45 s — la voix dit court, l'écran dit long** (le montage du plan)

| Fichier | Durée | Pour quoi |
|---|---|---|
| `deliverable/S01E01-colomb-45s.mp4` | 45 s | le film complet |
| `deliverable/S01E01-colomb-30s.mp4` | 30 s | le bloc film seul — TikTok et Reels |
| `deliverable/S01E01-colomb-15s-methode.mp4` | 15 s | méthode + orchestration, à remettre devant n'importe quel épisode |
| `deliverable/S01E01-colomb-vignette.jpg` | — | image à 00:26,0, la bouteille nette au premier plan |

**50 s — phrases entières** (la variante que le plan proposait)

| Fichier | Durée | Pour quoi |
|---|---|---|
| `deliverable/S01E01-colomb-50s.mp4` | 50 s | le film complet, les cinq étapes lues en entier |
| `deliverable/S01E01-colomb-20s-methode.mp4` | 20 s | méthode + orchestration, phrases entières |
| `deliverable/S01E01-colomb-50s-vignette.jpg` | — | même image, à 00:26,0 |

Tous sont normalisés à −14 LUFS (mesuré : −13,4 · −14,1 · −14,2 · −13,4 · −14,1) et se
terminent par un fondu de 0,5 s.

## Comment c'est fabriqué

```bash
npm run voix       # découpe la passe unique de voix off et la cale aux timecodes
npm run methode    # rend le bloc méthode : HTML → images → MP4 muet
npm run monter     # assemble tout et sort les exports + la vignette
npm run verifier   # contrôle format, durée, niveau sonore, coupe franche, sous-titres
npm run build      # les quatre à la suite, en 45 s
npm run build:50s  # les quatre à la suite, en 50 s
```

Toute commande accepte `--variante 50s` ou la variable `VARIANTE=50s`. Sans rien, c'est
le 45 s : `episode.json` porte `variante_par_defaut`.

`episode.json` est la source de vérité : timecodes, textes, couleurs, suivi de la
bouteille. Les scripts n'inventent rien, ils l'exécutent.

| Fichier | Rôle |
|---|---|
| `episode.json` | ✍️ **source de vérité** — tout le plan de montage en données |
| `source/P*.mp4` | les trois plans Higgsfield, tels que récupérés |
| `outro/methode.html` | le gabarit animé du bloc méthode |
| `outro/incrustations.html` | l'accroche et les sous-titres du bloc film |
| `assets/logos/` + `assets/LOGOS.md` | les logos officiels et leur provenance |
| `audio/vo-methode-passe-unique.mp3` | la prise ElevenLabs, d'un seul trait |
| `audio/vo-decoupe-*.json` | 🔁 où la passe a été coupée et de combien chaque ligne est accélérée, par variante |
| `scripts/suivre-bouteille.mjs` | relève la position de la bouteille pour l'étiquette annonceur |
| `work/` | intermédiaires, jamais versionnés |

## Le bloc film — 00:00 → 00:30

Les trois plans bout à bout, raccords francs à 10,0 s et 20,0 s, aucune transition,
aucun fondu. Les sources sont en 720×1280 à 24 ips ; le montage sort en 1080×1920 à 30 ips.

| Plan | Higgsfield | Scène | Réplique |
|---|---|---|---|
| P1 | `d2420e5c` | Quai d'un port espagnol à l'aube | « Il était une fois un homme qui cherchait le poivre… » |
| P2 | `c1085fef` | Plage des Caraïbes, il mord le piment | « Il cherchait le poivre. Il a trouvé ça. » |
| P3 | `c8c0bc2d` | À l'ombre de la voile, la bouteille au centre | « Ce n'était pas du poivre. C'était le piment… » |

L'accroche « Il cherchait le poivre. » tient de 00:00,3 à 00:03,0, en blanc sur bandeau
`#03A9F5`, au tiers bas et au-dessus de la zone d'interface des réseaux (y = 1290).
Les sous-titres sont brûlés sur tout le bloc, deux lignes au plus, sept mots par ligne au
plus — `npm run verifier` le contrôle. Ils sont calés à y = 1440, juste au-dessus de la
zone d'étiquette de la bouteille, qui commence à 1532.

À 00:30,0 : coupe franche, quatre images de noir plein, son du film coupé net. Le contrôle
compte les images de noir une par une plutôt que de sonder un seul instant.

### L'étiquette de l'annonceur

Aucune marque n'a été fournie pour cet épisode : **l'étiquette reste vierge et rien n'est
incrusté**, comme le prévoit le plan de montage. Le mécanisme est en place et attend son
image — déposer une PNG à fond transparent dans `assets/annonceur/etiquette.png` suffit
à l'activer, sans autre réglage.

Le suivi est relevé, pas estimé : `scripts/suivre-bouteille.mjs` repère la bouteille à sa
couleur dans le bas de l'image, à 29,0 · 29,5 · 30,0 s, et écrit le résultat dans
`episode.json`. Le verre fait 428 px de large et ne bouge que de trois pixels sur la
seconde — le plan est fixe depuis sa quatrième seconde, l'étiquette tiendra sans glisser.

## Le bloc méthode — à partir de 00:30

Fond `#F2F4F7`, grandes diagonales `#03A9F5` et `#7E57C2` du haut-droit vers le bas-gauche,
animées très lentement. RapidoCMS et ElevenLabs arrivent côte à côte, puis se rangent en
haut du cadre où ils restent. Cinq cartes d'étape, une par créneau de voix off, jamais deux
à l'écran en même temps. Puis l'orchestration : RapidoCMS au centre, Claude, Higgsfield,
ElevenLabs et HeyGen en orbite, chacun relié par un trait bleu qui se trace en 0,3 s ; les
cinq réseaux arrivent en cascade trois secondes avant la fin (00:43,0 en 45 s, 00:48,0 en
50 s) ; fondu au fond clair sur les 0,3 dernières secondes.

## Ce qu'il faut savoir

**Deux rythmes, une seule prise.** Le plan demande une passe unique — c'est ce qui garde
la ligne mélodique — et donne quinze secondes. La prise en fait 23,7. Les deux montages
partent donc du même enregistrement, découpé aux mêmes silences, et n'en changent que
les créneaux :

| | 45 s | 50 s |
|---|---|---|
| Ligne d'ouverture | 1,6 s → **1,27×** | 2,0 s → 1,01× |
| Les cinq étapes | 1,6 à 1,8 s → **1,18× à 1,34×** | 2,6 s chacune → **1,00×, lues en entier** |
| Orchestration | 5,0 s → 1,15× | 5,0 s → 1,15× |
| Bloc méthode | 15 s | 20 s |

`atempo` conserve la hauteur de voix, et le détail ligne par ligne est dans
`audio/vo-decoupe-45s.json` et `audio/vo-decoupe-50s.json`. Au-delà de 1,4× le script
refuse de monter plutôt que de livrer une voix qui court.

Le plan chiffrait la variante à « 3 s chacune ». Sur cette prise, **2,6 s suffisent** à
dire chaque étape en entier : c'est ce qui fait tomber le total sur 50 s pile — 2 s
d'ouverture, 13 s d'étapes, 5 s d'orchestration — au lieu de déborder à 52. Seule la
dernière phrase reste accélérée, à 1,15×, dans les deux montages.

Une variante ne duplique rien : `episode.json` porte le plan complet et, sous
`variantes`, uniquement ce qui diffère. Les scripts fondent les deux.

**Les réglages de voix n'ont pas pu être appliqués tels quels.** Le plan demande
stability 0,45 · similarity 0,80 · style 0,25 · speaker boost. L'outil MCP ElevenLabs
disponible ici n'expose ni stabilité, ni similarité, ni style : il prend un texte, un
modèle et une voix. La prise a été faite avec `eleven_multilingual_v2` et la voix
**Paul K — French Ad & Trailer Voice** (masculine, française, Parisien standard, registre
publicitaire), qui est la plus proche du profil demandé. Les réglages restent écrits dans
`episode.json` : ils s'appliqueront à une prise refaite depuis l'interface ElevenLabs.

**La nappe du bloc méthode est empruntée.** Le plan demande « une nappe de motion design
différente à partir de 00:30,2 ». Le dépôt n'en contenait pas pour cette série :
`assets/musique/nappe-methode.mp3` est reprise de `videos/planit-product-launch`. Elle est
posée à 22 % du niveau et passe automatiquement sous la voix (compression latérale, ≈ 6 dB).
À remplacer par la nappe de la série quand elle existera — le fichier se change sans
toucher aux scripts.

## Ce qui n'a pas été fait

**L'épisode n'est pas déclaré au catalogue, et c'est décidé.** Le plan demande de le
déclarer « monté dans RapidoCMS, avec les cinq réseaux en `a_venir` ». Ce vocabulaire —
un épisode, un état de production, des pièces par réseau — est celui du catalogue Social,
pas celui de RapidoCMS, qui gère des campagnes et des posts programmés. Et le catalogue
Social ne porte que les cinq séries FoodEatUp : `colomb` n'y a pas de série d'accueil.
La question a été posée, la réponse est « on verra plus tard ». Rien n'a été écrit dans
l'un ni dans l'autre.

## Fontes

Le plan demande Arial Bold. Arial n'est pas installée sur la machine de montage ; c'est
**Liberation Sans Bold** qui est utilisée, dont les métriques sont celles d'Arial. Le rendu
est identique au pixel près pour les graisses employées.
