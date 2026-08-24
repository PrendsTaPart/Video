# Gabarit série B « Le Quai »

Gabarit **réutilisable** pour les 35 plans de la série B. Un plan = un dossier
`videos/{slug}/` dupliqué depuis ce gabarit, avec **un seul fichier modifié à la
main : `quai.config.json`**. Tout le reste (HTML, GSAP, sous-titres) est du
code identique sur les 35 plans — seules les données changent.

## Deux sorties, la seconde dérivée de la première

| Fichier | Durée | Contenu |
|---|---|---|
| `{slug}-film.mp4` | 10,0 s | Le plan nu : vidéo + voix off, aucun texte. Une brique du film de 350 s. |
| `{slug}-social.mp4` | 12,0 s | Le plan (identique) + cartouche de date + sous-titres (0-10 s), puis carton de fin (10-12 s). La publication quotidienne. |

`index-social.html` inclut le **même** `<video>`/`<audio>` (mêmes attributs
`data-start`/`data-duration`/`data-volume`) que `index-film.html` — copiés à
l'identique par `scripts/quai-monter.mjs` depuis les mêmes jetons, jamais
retapés à la main. C'est ce qui garantit que le film assemblé (les 35 plans
mis bout à bout) et les 35 publications sociales montrent exactement les
mêmes images.

## Comment un plan est produit

1. L'agent (Claude) appelle `obtenir_episode` sur le studio (qui donne aussi
   la punchline de l'épisode), télécharge le plan, synthétise la voix off
   (ElevenLabs, voix figée dans `references/planit-brand.md`), transcrit au
   mot.
2. Ces données sont écrites dans `videos/{slug}/quai.config.json`,
   `assets/video/plan.mp4`, `assets/voice/vo.mp3`, `caption_groups.json`.
3. `node scripts/quai-monter.mjs videos/{slug}` prend le relais : copie les
   fichiers du gabarit, remplit les jetons `__QUAI_...__` dans les HTML,
   génère le `.vtt`, rend les deux vidéos, contrôle les deux sorties.
4. L'agent téléverse les deux fichiers sur le studio.

Voir l'en-tête de `scripts/quai-monter.mjs` pour le détail exact de qui fait
quoi (ce script ne peut pas appeler les outils MCP du studio — ceux-ci ne
sont accessibles qu'à l'agent dans la conversation).

## Les jetons de substitution

Aucune valeur propre à un plan n'est écrite en dur dans le HTML. Le gabarit
contient des jetons uniques que `quai-monter.mjs` remplace :

| Jeton | Vient de | Où |
|---|---|---|
| `__QUAI_PLAN_SRC__` | `quai.config.json` → `planSource` | `index-film.html`, `index-social.html` |
| `__QUAI_AMBIANCE_VOLUME__` | `ambianceDb` (converti dB → linéaire) | idem |
| `__QUAI_VOICE_SRC__` | fixe : `assets/voice/vo.mp3` | idem |
| `__QUAI_VOICE_DURATION__` | mesurée par ffprobe sur le fichier voix | idem |
| `__QUAI_EPOQUE__` | `quai.config.json` → `epoque` | `compositions/cartouche-date.html` |
| `__QUAI_PUNCHLINE__` | `quai.config.json` → `punchline` | `compositions/carton-fin.html` |
| `var GROUPS = [];` | `caption_groups.json` | `compositions/sous-titres.html` |

## Pourquoi il n'y a pas de `npm run check` générique

**Point technique découvert en construisant ce gabarit**, à savoir pour la
suite : les commandes `hyperframes lint`/`validate`/`inspect`/`check`
cherchent toujours un fichier nommé exactement `index.html` à la racine du
dossier — elles n'ont pas d'option pour cibler un autre fichier. Avoir
`index-film.html` ET `index-social.html` en même temps déclenche l'erreur
`multiple_root_compositions`.

Le **rendu**, lui, n'a pas cette limite : `hyperframes render` accepte
`-c <fichier>` pour choisir l'entrée, et c'est confirmé fiable (testé) —
`npm run render:film` / `npm run render:social` fonctionnent normalement.
`scripts/quai-monter.mjs` s'appuie sur ce rendu (qui fait sa propre
vérification interne) puis contrôle chaque sortie au ffprobe (dimensions,
durée, piste audio non silencieuse) — c'est le contrôle qui compte
réellement pour livrer, et il tourne à chaque exécution.

Pour vérifier une des deux versions au lint/validate/inspect complet (utile
seulement si vous modifiez la structure du gabarit lui-même, jamais pour un
plan) :

```bash
mv index-social.html /tmp/   # ou l'inverse
mv index-film.html index.html
npx hyperframes lint && npx hyperframes validate && npx hyperframes inspect
mv index.html index-film.html
mv /tmp/index-social.html .
```

## Structure

```
_gabarit-quai/
  quai.config.json        ← le seul fichier à modifier par plan (documente le schéma)
  index-film.html          la version film (10,0s)
  index-social.html        la version sociale (12,0s)
  compositions/
    cartouche-date.html    cartouche de date, coin bas gauche
    carton-fin.html        carton de fin, 2s — mark + punchline + signature,
                            composition inspirée d'A-S2E1 v8, fond encre du Quai
    sous-titres.html       sous-titres, une ligne à la fois, blanc uniforme
  assets/
    fonts/    Sora + Inter (repli officiel, Alte Haas Grotesk indisponible)
    vendor/   gsap.min.js
    brand/    planit-mark-white.png
    sfx/    dont signature-outro.mp3, joué par carton-fin.html (0-2s de la version sociale)
    video/, voice/         (vides dans le gabarit, remplis par plan, non commités)
  scripts/
    quai-monter.mjs
```
