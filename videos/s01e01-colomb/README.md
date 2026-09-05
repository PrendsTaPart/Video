# S01E01 — « Il cherchait le poivre. »

Une minute, 1080×1920, 30 ips. Trente secondes de film — Christophe Colomb parti chercher
le poivre — puis la queue animée de la série : trois secondes de transition, vingt de
méthode, sept de hook de fin.

**Aucune vidéo n'a été générée.** Les trois plans existaient déjà dans la bibliothèque
Higgsfield et ont été récupérés par MCP. C'est la règle du dépôt et celle du plan de montage.

## Les livrables

| Fichier | Durée | Pour quoi |
|---|---|---|
| `deliverable/S01E01-colomb-60s.mp4` | 60 s | le film complet |
| `deliverable/S01E01-colomb-30s.mp4` | 30 s | le bloc film seul — TikTok et Reels |
| `deliverable/S01E01-colomb-30s-queue.mp4` | 30 s | transition + méthode + hook, à remettre derrière n'importe quel épisode |
| `deliverable/S01E01-colomb-vignette.jpg` | — | image à 00:26,0, la bouteille nette au premier plan |

Tous à −14,6 LUFS environ, fondu de 0,5 s en sortie.

## Le bloc film — 00:00 → 00:30

| Plan | Higgsfield | Scène | Réplique |
|---|---|---|---|
| P1 | `d2420e5c` | Quai d'un port espagnol à l'aube | « Il était une fois un homme qui cherchait le poivre… » |
| P2 | `c1085fef` | Plage des Caraïbes, il mord le piment | « Il cherchait le poivre. Il a trouvé ça. » |
| P3 | `c8c0bc2d` | À l'ombre de la voile, la bouteille au centre | « Ce n'était pas du poivre. C'était le piment… » |

Raccords francs à 10,0 et 20,0 s, aucune transition. Les sources sont en 720×1280 à
24 ips ; le montage sort en 1080×1920 à 30 ips.

L'accroche « Il cherchait le poivre. » tient de 00:00,3 à 00:03,0, blanc sur bandeau
`#03A9F5`, au tiers bas. Les sous-titres sont brûlés sur les trente secondes, deux lignes
et sept mots par ligne au plus, calés à y = 1440 — juste au-dessus de la zone d'étiquette
de la bouteille, qui commence à 1532.

À 00:30,0 : coupe franche, quatre images de noir, son du film coupé net. Le contrôle
compte les images de noir une par une plutôt que de sonder un seul instant.

### L'étiquette de l'annonceur

Aucune marque fournie : **l'étiquette reste vierge et rien n'est incrusté**, comme le
prévoit le plan. Déposer une PNG à fond transparent dans `assets/annonceur/etiquette.png`
l'active, sans autre réglage.

Le suivi est relevé, pas estimé : `scripts/suivre-bouteille.mjs` repère la bouteille à sa
couleur dans le bas de l'image, à 29,0 · 29,5 · 30,0 s, et écrit le résultat dans
`episode.json`. Le verre fait 428 px de large et ne bouge que de trois pixels sur la
seconde — le plan est fixe depuis sa quatrième seconde, l'étiquette tiendra sans glisser.

## La queue animée — 00:30 → 01:00

Elle vient de `../module-methode-rapidocms`, partagée par toute la série ; son README
décrit les trois blocs et la règle des soixante secondes. Cet épisode n'y apporte que deux
lignes de voix off :

| Rôle | Créneau | Texte |
|---|---|---|
| Ouverture | 00:33 → 00:35 | « Vous aussi, faites vos publicités vous-même. » |
| Punchline | 00:53,8 → 00:58,8 | « Lui, il cherchait le poivre. Vous, vous avez RapidoCMS. » |

Les deux sont lues au débit naturel, sans accélération — le détail est dans
`audio/vo-queue-decoupe.json`. Les six lignes des étapes viennent du module et ne sont
jamais regénérées.

## Comment c'est fabriqué

```bash
npm run queue      # les deux lignes de voix off + les 900 images de la queue
npm run monter     # bloc film + queue, niveaux, exports, vignette
npm run verifier   # structure, format, durée, niveau, coupes, sous-titres
npm run build      # les trois à la suite
```

`episode.json` est la source de vérité : timecodes, textes, couleurs, suivi de la bouteille.
Le montage et les contrôles eux-mêmes vivent dans le module — les scripts d'ici ne sont que
des pilotes de quelques lignes.

## Ce qu'il faut savoir

**Les réglages de voix n'ont pas pu être appliqués tels quels.** Le plan demande
stability 0,45 · similarity 0,80 · style 0,25 · speaker boost. L'outil MCP ElevenLabs
disponible ici n'expose ni stabilité, ni similarité, ni style : il prend un texte, un
modèle et une voix. Les prises ont été faites avec `eleven_multilingual_v2` et la voix
**Paul K — French Ad & Trailer Voice**, la plus proche du profil demandé. Les réglages
restent écrits dans `episode.json` pour une prise refaite depuis l'interface ElevenLabs.

**La nappe est empruntée.** `assets/musique/nappe-methode.mp3` vient de
`videos/planit-product-launch`, faute d'une nappe propre à cette série. Elle est posée à
22 % et passe sous la voix par compression latérale. À remplacer sans toucher aux scripts.

**Arial n'est pas installée** : c'est Liberation Sans qui rend, avec les mêmes métriques.

## Ce qui n'a pas été fait

**L'épisode n'est pas déclaré au catalogue.** Le vocabulaire demandé — un épisode, un état
de production, des pièces par réseau — est celui du catalogue Social, pas celui de
RapidoCMS ; et la série n'existe dans aucun des deux. La question a été posée, la réponse
est « on verra plus tard ».
