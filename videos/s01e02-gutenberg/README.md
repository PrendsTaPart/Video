# S01E02 — « Un livre, deux ans »

Série **Michael remonte le temps**. Une minute, 1080×1920, 30 ips.
Trente secondes de film — le copiste, la presse, les cent quatre-vingts livres — puis la
queue animée de la série : trois secondes de transition, vingt de méthode, sept de hook.

**Aucune vidéo n'a été générée.** Les trois plans existaient déjà dans la bibliothèque
Higgsfield et ont été récupérés par MCP. C'est la règle du dépôt et celle du plan de montage.

## Les livrables

| Fichier | Durée | Pour quoi |
|---|---|---|
| `deliverable/S01E02-gutenberg-60s.mp4` | 60 s | le film complet |
| `deliverable/S01E02-gutenberg-30s.mp4` | 30 s | le bloc film seul — TikTok et Reels |
| `deliverable/S01E02-gutenberg-30s-queue.mp4` | 30 s | transition + méthode + hook, à remettre derrière n'importe quel épisode |
| `deliverable/S01E02-gutenberg-vignette.jpg` | — | image à 00:25,0, le livre net au premier plan |

Tous à −14,5 LUFS environ, fondu de 0,5 s en sortie.

## Le bloc film — 00:00 → 00:30

| Plan | Higgsfield | Scène | Réplique |
|---|---|---|---|
| P1 | `83a87fe0` | Scriptorium de pierre, la nuit | « Il était une fois un homme qui copiait les livres à la main… » |
| P2 | `b9a5c85b` | Atelier d'imprimerie, le tirage | « Alors il a fondu des lettres en métal… » |
| P3 | `61b45278` | L'établi : le parchemin seul, la pile de livres | « En trois ans, il a sorti cent quatre-vingts livres… » |

Raccords francs à 10,0 et 20,0 s, aucune transition. Les sources sont en 720×1280 à
24 ips ; le montage sort en 1080×1920 à 30 ips.

L'accroche « Un livre : deux ans de travail. » tient de 00:00,3 à 00:03,0, blanc sur
bandeau `#03A9F5`, au tiers bas. Les sous-titres sont brûlés sur les trente secondes,
deux lignes et sept mots par ligne au plus, calés à y = 1250 pour laisser le livre visible.

**L'accent de la presse.** À 00:16,4, trois images de noir plein — et le son continue
par-dessus. C'est le seul effet de montage du bloc film. Le point n'a pas été choisi à
l'estime : entre 16 et 17 s, l'énergie sonore du plan 2 culmine à 15,7 s puis à 16,3 et
16,5 s ; 16,4 tombe sur un transitoire de la presse. Le contrôle compte les trois images
une par une et vérifie que l'image revient juste après.

À 00:30,0 : coupe franche, quatre images de noir, son du film coupé net.

### La couverture de l'annonceur

Aucune marque fournie : **la couverture reste vierge et rien n'est incrusté**, comme le
prévoit le plan. Déposer une PNG à fond transparent dans `assets/annonceur/couverture.png`
l'active, sans autre réglage.

Le suivi est dans `episode.json`, relevé à trois instants entre 24 et 30 s. Deux choses à
savoir avant d'y poser une marque : le cuir sombre du livre n'offre **aucun repère
colorimétrique fiable** — contrairement à la bouteille de l'épisode 1, le suivi n'a pas pu
être automatisé et a été mesuré à l'œil sur trois images gabarit ; et **le plan bouge
encore** sur ces six secondes, la perche finissant sa montée, si bien que le livre descend
d'environ 90 px dans le cadre. Trois points interpolés suffisent à ce que rien ne glisse
visiblement, mais un vrai suivi image par image sera à faire le jour où une marque existe.

## La queue animée — 00:30 → 01:00

Elle vient de `../module-methode-rapidocms`, partagée par toute la série ; son README
décrit les trois blocs. Cet épisode n'y apporte que deux lignes de voix off :

| Rôle | Créneau | Texte |
|---|---|---|
| Ouverture | 00:33 → 00:35 | « Écrivez une fois. Publiez partout. » |
| Punchline | 00:53,8 → 00:58,8 | « Lui, il a fondu des lettres en métal. Vous, vous avez RapidoCMS. » |

Les deux sont lues au débit naturel, sans accélération — le détail est dans
`audio/vo-queue-decoupe.json`.

## Les faits

`episode.json` porte sous `faits` les six points que l'épisode avance, pour qu'on puisse
les revérifier sans rouvrir le brief : Mayence 1452-1455, 1 286 pages, environ 180
exemplaires, trois ans de tirage, la Bible unique du copiste pendant ce temps, et les 48 à
49 exemplaires qui subsistent.

## Ce qui n'a pas été fait

**L'épisode n'est pas déclaré au catalogue.** Le plan demande de le déclarer « monté dans
RapidoCMS, les cinq réseaux en `a_venir` ». Ce vocabulaire est celui du catalogue Social,
pas celui de RapidoCMS qui gère campagnes et posts ; et la série n'existe dans aucun des
deux. La question a été posée, la réponse est « on verra plus tard ».

## Les prompts, si les plans sont à refaire

`episode.json` porte les identifiants Higgsfield des trois plans utilisés. Le brief de
l'épisode donne le préfixe commun et les trois prompts complets ; les références `@michael`,
`@livre` et `@costume` sont à fournir à l'identique, faute de quoi le visage dérivera d'un
épisode à l'autre et les livres de la pile n'auront pas la même géométrie — ce qui est
précisément ce que l'épisode raconte.
