# Provenance des logos

Règle du plan de montage : **les logos sont pris tels quels, jamais redessinés.**
Chacun vient de sa source officielle ou du jeu Simple Icons, et la couleur de marque
est celle que la source déclare.

| Fichier | Marque | Source | Couleur déclarée |
|---|---|---|---|
| `logos/rapidocms.png` | RapidoCMS | dépôt — `videos/carousel-rapidocms/assets/logo/rapidocms-logo-crop.png` | origami vert/violet/bleu + wordmark `#03A9F5` |
| `logos/claude.svg` | Claude | Simple Icons `claude` | `#D97757` |
| `logos/elevenlabs.svg` | ElevenLabs | Simple Icons `elevenlabs` | `#000000` |
| `logos/higgsfield.png` | Higgsfield | higgsfield.ai — `/icon.png` (192×192) | lime `#CFF800` |
| `logos/heygen.png` | HeyGen | heygen.com — `/images/heygen-logo.png` (306×214) | noir + prisme |
| `logos/facebook.svg` | Facebook | Simple Icons `facebook` | `#0866FF` — **le plan impose `#1877F2`**, c'est celui qui est appliqué |
| `logos/instagram.svg` | Instagram | Simple Icons `instagram` | `#FF0069` — **le plan impose `#E1306C`**, c'est celui qui est appliqué |
| `logos/tiktok.svg` | TikTok | Simple Icons `tiktok` | `#000000` — conforme au plan |
| `logos/linkedin.svg` | LinkedIn | Simple Icons, dépôt GitHub au tag `13.0.0` | `#0A66C2` — conforme au plan |
| `logos/youtube.svg` | YouTube | Simple Icons `youtube` | `#FF0000` — conforme au plan |

## Deux choses à savoir

**LinkedIn ne fait plus partie du paquet npm `simple-icons`.** La marque a été retirée
des versions récentes. Le fichier vient donc du dépôt GitHub de Simple Icons au tag
`13.0.0`, où elle existe encore : c'est le même tracé, la même source.

**Higgsfield et HeyGen ne sont dans aucun jeu d'icônes.** Ils ont été pris sur les sites
officiels des deux marques, en PNG, seul format qu'elles publient en accès direct. Ce
sont des images matricielles : elles tiennent à la taille où le montage les affiche
(192 px et 306 px de large pour un affichage à 130 px), pas au-delà.

## L'étiquette de l'annonceur

`annonceur/` est vide. Aucune marque n'a été fournie pour cet épisode, donc l'étiquette
de la bouteille **reste vierge** et rien n'est incrusté — c'est ce que demande le plan de
montage. Déposer une PNG à fond transparent nommée `etiquette.png` l'active : le montage
la pose sur le suivi de la bouteille écrit dans `episode.json`, sans autre réglage.
