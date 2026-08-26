# RapidoCRM Studio

Chaîne de production des **172 tutoriels vidéo de RapidoCRM Académie** :
de l'enregistrement d'écran brut à la page publiée.

## Démarrer

```bash
npm install
cp .env.example .env      # ELEVENLABS_API_KEY, ELEVENLABS_VOICE_ID, RAPIDO_ACADEMIE_API_KEY
npm run preview           # ouvre Remotion Studio sur la composition « Preview »
```

`ffmpeg` et `ffprobe` doivent être installés (`brew install ffmpeg`,
`apt install ffmpeg`) : le pré-traitement de l'enregistrement, la normalisation
audio et les contrôles de QA s'appuient dessus.

## La chaîne

```bash
npm run tuto -- <module> <numero>          # tout, avec les deux points d'arrêt
npm run tuto -- Comptabilité 1 --dry-run   # tout sauf les publications
npm run tuto -- Comptabilité 1 --from voix # reprendre après correction du script
```

Étape par étape :

| Commande | Sortie |
|---|---|
| `npm run analyse -- <chemin>` | `analyse.json` |
| `npm run fiche -- <chemin>` | `fiche.json` |
| `npm run script -- <chemin>` | `script.json` + `script.md` |
| `npm run voix -- <chemin>` | `voix/*.mp3`, `alignement.json`, transcription |
| `npm run rendu -- <chemin> [--format 16x9\|9x16\|tous] [--preview]` | `out/master-*.mp4`, `rendu.json` |
| `npm run vignette -- <chemin>` | `out/thumb-*.jpg` |
| `npm run qa -- <chemin>` | `qa.json` — bloque la publication si rouge |
| `npm run publier:cms -- <chemin>` | lien AWS S3 |
| `npm run publier:youtube -- <chemin>` | lien YouTube |
| `npm run publier:site -- <chemin>` | page en ligne |

Mode série et outillage :

```bash
npm run serie -- --module Comptabilité --limite 5 [--auto-hook --auto-punchline]
npm run vignettes:lot -- Comptabilité
npm run regenerer -- --sequence punchline --module Comptabilité [--republier]
npm run mcp:file -- <chemin>      # demandes MCP en attente de réponse
```

## Comment ça marche

Deux choses ne peuvent pas être faites par un script Node seul, et sont donc
déléguées à Claude Code par des fichiers déposés sur le disque :

- **les appels MCP** — voir `src/mcp/README.md` (`*.demande.json` → `*.reponse.json`) ;
- **les travaux de lecture et de rédaction** — analyse visuelle des frames,
  fiche fonctionnelle, script : la commande écrit une consigne
  (`analyse-demande.md`, `fiche-demande.md`, `script-demande.md`) et s'arrête.

Dans les deux cas, on écrit le fichier attendu puis on relance la même
commande : elle reprend sans refaire ce qui est déjà fait. Chaque fichier est
validé par un schéma zod (`src/schema/index.ts`) avant usage.

Les règles de fond — ton, charte, traçabilité, points d'arrêt — sont dans
[`CLAUDE.md`](./CLAUDE.md).

## Le présentateur

`assets/presentateur/` : 16 photos détourées, réutilisées par les 172 tutoriels.
Une pose ouvre le hook (le problème), une autre ferme la vidéo sur la punchline
(le résultat). Le choix est déterministe par `(module, numéro)` — voir
`src/brand/presentateur.ts` — donc stable d'un rendu à l'autre et réparti sur le
catalogue.

La vidéo s'ouvre par ailleurs sur la **vignette du tutoriel** pendant 1,4 s :
celle de la fiche en ligne (MCP « RapidoCMS tutoriels ») si la clé d'API est
renseignée, sinon le lien AWS de `publication.json`, sinon la vignette locale.

## Autres assets

`assets/ia/claude.png` habille l'en-tête de la carte prompt. `openai.png` et
`mistral.png` restent en réserve, volontairement non montés.
`assets/references/ecran-commerciaux.png` sert de plan de démonstration à la
composition `Preview`, pour juger le cadre, le zoom et les annotations sans
enregistrement source.

## Structure

```
src/
  brand/      tokens de charte, logos, fonds animés, typo, présentateur
  template/   les 6 séquences Remotion + les vignettes
  pipeline/   analyse, fiche, script, voix, rendu, vignette, publications, QA, série
  mcp/        pont vers les serveurs MCP
  schema/     schémas zod de tous les fichiers d'échange
  cli/        commandes
content/<module>/<Vxx-slug>/   un tutoriel = un dossier
```

## Reste à renseigner

- l'URL du MCP « RapidoCMS tutoriels » dans `.mcp.json`, une fois Lovable livré ;
- `ELEVENLABS_VOICE_ID` (voix française retenue) ;
- la chaîne YouTube RapidoCRM, connectée au MCP YouTube ;
- un compte de démonstration RapidoCRM en lecture, pour fiabiliser l'étape fiche ;
- `assets/musique/fond.mp3` et `assets/sfx/` (whoosh, clic, accord de fin) —
  le mixage les intègre s'ils existent, et s'en passe sinon.
