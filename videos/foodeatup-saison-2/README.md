# FoodEatUp — Saison 2 « Michael fait son cinéma »

30 épisodes · 60 prompts Seedance 2.5 (Higgsfield) · 30 outros Remotion · vertical 1080×1920, 30 fps.

**Le concept** : 1 épisode = 1 genre de film culte + 1 situation de restaurant + 1 module FoodEatUp.
20 s Seedance (2 × 10 s) = divertissement. 10 s de montage = révélation. On ne fait pas 30 pubs,
on fait 30 courts-métrages qui finissent par une solution.

**Signature de saison** : à la fin de la scène 2, Michael regarde la caméra → clap « COUPEZ ! » →
« Dans la vraie vie… » → l'interface FoodEatUp fait en un tap ce qu'il a raté en 20 s → logo.

**Parodie par codes de genre uniquement** : aucun titre de film, aucune réplique de film, aucun
visage d'acteur réel, aucune marque à l'image. On veut « je reconnais le genre », pas « je
reconnais le film ». Saison 1 = le chaos du quotidien ; saison 2 = le quotidien filmé comme un
film. Les gags de la saison 1 ne sont jamais repris.

## Contenu du dossier

| Fichier | Rôle |
|---|---|
| `SAISON-2-EPISODES.md` | 🔁 Index des 30 épisodes (titre · genre · situation · module · hook · lot lumière) |
| `prompts/ep{NN}-{slug}.md` | 🔁 **La fiche de tournage** : sélecteurs, les 2 prompts Seedance complets, la directive de montage, la checklist |
| `voix-off/vo-saison-2.md` · `.json` | 🔁 Les 30 phrases de voix off, à générer en une passe ElevenLabs |
| `DIRECTIVE-MONTAGE.md` | 🔁 La structure d'outro commune + les libellés de modules autorisés |
| `RAPPORT-CONTROLES.md` | 🔁 Résultat des contrôles automatiques |
| `episodes.json` | 🔁 Index fusionné, lisible par les outils |
| `episodes/*.json` | ✍️ **Source de vérité** — les 30 épisodes structurés |
| `saison.json` | ✍️ **Source de vérité** — références, bloc final, structure d'outro, modules autorisés, lots |
| `KIT-REFERENCES.md` | Le kit `@Image 1-4`, les 10 règles de prompt, le lexique voix de Michael |
| `PREFLIGHT-COUT.md` | Coût de la saison en crédits Higgsfield — décision avant production |
| `CHECKLIST-QUALITE.md` | Ce qui est vérifié par la machine, ce qui reste à l'œil |
| `assets/palette.json` · `assets/README.md` | Couleurs officielles + provenance des assets de montage |

🔁 = **généré**, ne pas éditer à la main. ✍️ = à éditer.

```bash
npm run build   # régénère les fiches, l'index, la voix off et le rapport
npm run check   # même chose : sort en erreur si un contrôle bloquant échoue
```

## Comment un prompt est fabriqué

Chaque prompt Seedance est assemblé à partir des données de l'épisode, toujours dans le même ordre :

```text
REF: Michael = @Image 1 (face, hair, build) + @Image 2 (season outfit)[, + accessoire], keep identical. Location = …
FORMAT: 9:16, 10 s, [3-4] shots, realistic comedy shot like a [genre].
SCENE: [lieu, ambiance, 2 détails visuels forts, accessoire de genre]
ACTION: 0–2 s / 2–5 s / 5–8 s / 8–10 s — une action observable par plan
DIALOGUE (spoken French, slow and clear, natural lip-sync, no captions): …
CAMERA / LIGHT & GRADE / AUDIO
PHYSICS … SKIN … NO-IP …            ← bloc final, ajouté automatiquement sur les 60 prompts
```

Le bloc final, la ligne REF et le préfixe de dialogue viennent de `saison.json` : ils sont
identiques sur les 60 prompts par construction, on ne peut pas en oublier un.

## Ordre de production

1. **Kit de références** (une fois) : `@Image 1` portrait · `@Image 2` tenue de saison · `@Image 3`
   salle · `@Image 4` cuisine, option Soul ID « Michael ». **Valider la tenue avant tout** — voir
   `KIT-REFERENCES.md`.
2. **Voix off** (une fois) : une voix ElevenLabs pour la saison, les 30 phrases générées d'un coup,
   mêmes réglages de stabilité et de rythme → `voix-off/vo-saison-2.md`.
3. **Pilotes** : épisodes **01, 04 et 09** en 480p (western, zombies, sous-marin — trois genres très
   différents). Vérifier l'identité de Michael, la prononciation des répliques, la lisibilité du gag
   sans le son.
4. **Tournage par lots de lumière** : garder les mêmes sélecteurs d'un épisode à l'autre dans un même
   lot, c'est ce qui donne à la saison une image cohérente. Les lots sont dans `SAISON-2-EPISODES.md`.
5. **Corrections** : visage qui dérive → Region edit ; un plan raté → Shot re-generate ; jamais de
   re-roll complet.
6. **Rendu final** en 720p (1080p pour les épisodes phares 01, 04, 09, 14, 30).
7. **Montage**, par épisode : extraire la dernière image de la scène 2
   (`ffmpeg -sseof -0.1 -i scene2.mp4 -frames:v 1 scene2-last-frame.png`), coller le bloc
   « CLAUDE CODE » de la fiche, puis assembler scène 1 + scène 2 + outro.
8. **Publication** : titre = titre de l'épisode · hook de publication = la réplique du hook ·
   miniature = `ep{NN}-thumb.png`.

## Deux règles qui ne bougent pas

- **Ce dossier ne génère aucune vidéo Higgsfield.** Les prompts sont faits pour être collés dans
  l'interface par un humain, ou pour réutiliser un plan déjà présent dans la bibliothèque du projet
  (`CLAUDE.md` à la racine du dépôt).
- **« FoodEatUp » n'est jamais prononcé par l'avatar Seedance**, seulement par la voix off du
  montage. `npm run check` échoue si une réplique l'introduit.

## Points ouverts

- Tenue de saison (`@Image 2`) : proposition à valider, tout le reste en dépend.
- Logo officiel en **SVG** absent du dépôt (seulement du PNG) — voir `assets/README.md`.
- `sfx/clap.wav` et `sfx/whoosh.wav` à sourcer ; `tick` et `impact` ont un substitut.
- 13 voix off dépassent la fenêtre de 7 s au débit posé. Le texte du brief est conservé tel quel et
  une **variante courte est proposée** dans chaque fiche concernée : à trancher avant l'enregistrement.
