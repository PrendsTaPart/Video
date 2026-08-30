# Assets du montage — où les prendre

La directive de montage attend un dossier `./assets` **dans le projet Remotion de l'épisode**.
Copiez-y :

| Attendu | Source dans ce dépôt | État |
|---|---|---|
| `palette.json` | `videos/foodeatup-saison-2/assets/palette.json` | ✅ prêt (charte officielle, `rapido-kb/charte-graphique.md`) |
| `logo-foodeatup.svg` | `studio-video/assets/brand/logo/foodeatup-logo-horizontal.png` | ⚠️ **le dépôt n'a que du PNG** — voir ci-dessous |
| `sfx/clap.wav` | `assets/sfx/clap.wav` | ✅ synthétisé (bruit filtré + coup grave, ffmpeg) |
| `sfx/whoosh.wav` | `assets/sfx/whoosh.wav` | ✅ synthétisé (bruit en cloche, ffmpeg) |
| `sfx/tick.wav` | `assets/sfx/tick.mp3` (copie de `serie-30-e01/.../click-soft.mp3`) | 🔁 substitut en place |
| `sfx/impact.wav` | `assets/sfx/impact.mp3` (copie de `serie-30-e01/.../impact-bass-1.mp3`) | 🔁 substitut en place |
| `scene2-last-frame.png` | extrait de la scène 2 : `ffmpeg -sseof -0.1 -i scene2.mp4 -frames:v 1 scene2-last-frame.png` | par épisode |
| `vo.mp3` | ElevenLabs, textes dans `voix-off/vo-saison-2.md` | par épisode |

## Le logo

Retenu pour l'outro : **`foodeatup-logo-horizontal.png`** (pastille bleue, texte blanc). Sur le
fond anthracite de la charte, c'est la seule variante officielle disponible qui reste lisible —
la variante mascotte à contour bleu passe sous le seuil de contraste sur fond sombre, et il
n'existe pas de version blanche dans le dépôt.

Le brief demande un **SVG** (« ne jamais le redessiner, le déformer, le recolorer, le rogner »).
Le dépôt ne contient aujourd'hui que des PNG :
`studio-video/assets/brand/logo/` et `studio-video/assets/brand/logo-v2/`.
Un PNG suffit si sa résolution dépasse la taille d'affichage, mais **le SVG officiel est à récupérer
auprès de la marque** avant le rendu final — c'est le seul élément non résolu du kit.

Rappel charte : mark = tête de chef qui fait un clin d'œil ; le double-O forme un ∞ ; versions
noir sur clair et blanc sur sombre ; zone de protection = la plus grande entre ½ hauteur (charte)
et 10 % de la largeur (brief saison 2).
