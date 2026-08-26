# RapidoCRM Studio — règles de production

Ce projet produit les **172 tutoriels vidéo de RapidoCRM Académie**, de
l'enregistrement d'écran brut jusqu'à la page publiée sur le site.

## La chaîne, en 9 étapes

```
source.mp4
  1. analyse    → analyse.json      (frames, OCR, actions, étapes, zones sensibles)
  2. fiche      → fiche.json        (compréhension métier via MCP RapidoCRM)
  3. script     → script.json + script.md
  4. voix       → voix/*.mp3 + voix/alignement.json + transcription.txt
  5. rendu      → out/master-16x9.mp4, out/master-9x16.mp4, rendu.json
                  (la vignette du tutoriel ouvre la vidéo — voir plus bas)
  6. vignette   → out/thumb-16x9.jpg, out/thumb-9x16.jpg
  7. publier:cms      → lien AWS S3            (MCP RapidoCMS)
  8. publier:youtube  → lien YouTube           (MCP YouTube)
  9. publier:site     → page en ligne          (MCP « RapidoCMS tutoriels »)
```

`npm run tuto -- <module> <numero>` enchaîne le tout.

## Règles non négociables

1. **Ne jamais inventer une fonctionnalité de RapidoCRM.** Toute affirmation sur
   le logiciel vient soit d'une frame de l'enregistrement d'écran, soit d'un
   schéma d'outil du MCP RapidoCRM. Ce qui n'est pas vérifiable va dans
   `fiche.json → a_verifier`, jamais dans le script.
2. **Aucune écriture dans le CRM depuis ce pipeline.** Les appels au MCP
   RapidoCRM sont en lecture seule (schémas d'outils, listes de démonstration).
3. **La charte RapidoSoftware est une contrainte de build**, pas une
   recommandation. Voir « Charte » ci-dessous. Les composants échouent au build
   si elle est violée.
4. **La vidéo s'ouvre sur la vignette du tutoriel.** Elle est récupérée dans
   cet ordre : lien AWS de `publication.json`, puis la fiche en ligne via le MCP
   « RapidoCMS tutoriels » (`obtenir_tutoriel`), puis `out/thumb-16x9.jpg`. Le
   spectateur retrouve ainsi l'image sur laquelle il a cliqué.
5. **`script.json` est la seule source du rendu.** Aucun texte n'est écrit en dur
   dans le template.
6. **Deux points d'arrêt ne sont jamais contournés**, même en mode série :
   après l'écriture du script, et après le rendu de prévisualisation.
7. **Confidentialité** : toute donnée réelle visible à l'écran (email, téléphone,
   SIRET, IBAN, nom de client) est listée dans `analyse.json → zones_sensibles`
   et floutée au rendu.

## Ton

Français, vouvoiement. Phrases courtes, rythme vif. Ludique sans être puéril.
Compréhensible d'un débutant total, utile à un expert. Zéro jargon non expliqué
(un mot technique est défini en cinq mots à sa première occurrence). Jamais
« il suffit de », jamais « c'est très simple ». On dit ce que ça change pour
l'utilisateur avant de dire où cliquer.

## Charte RapidoSoftware

| Rôle | Couleur |
|---|---|
| Gris primaire (texte, titres) | `#383838` |
| Vert RapidoCRM (dominante) | `#4CAF50` |
| Violet RapidoRH (contrepoint) | `#7E57C2` |
| Bleu RapidoCMS (accent) | `#03A9F5` |
| Fond clair | `#F2F4F7` |
| Blanc | `#FFFFFF` |

- **Police unique : Arial** (Helvetica en repli). Aucune autre.
- **Contraste** : sur un aplat de couleur, le texte est uniquement blanc ou
  `#383838`. Jamais de texte coloré sur fond coloré. Utiliser `textOn(bg)`.
- **Logo** : jamais déformé (scale uniforme seulement), **jamais tourné**,
  uniquement sur blanc / `#F2F4F7` / en défonce sur un aplat de la charte.
  Zone de protection = 2× la hauteur du logomark. Taille minimale = 8 % de la
  hauteur de frame.
- Le logomark est un trio d'oiseaux origami low-poly (vert, bleu, violet).

## MCP utilisés

| MCP | À quoi il sert |
|---|---|
| `RapidoCRM` | Comprendre le logiciel : outils réels, schémas de paramètres, données de démo en lecture |
| `RapidoCMS` | Déposer les médias dans la bibliothèque, obtenir les liens AWS S3 |
| `YouTube` | Publier sur la chaîne, vignette, playlist, SEO |
| `RapidoCMS tutoriels` | Remplir et publier la page du tutoriel sur le site Lovable (publication immédiate, sans validation) |

Le pipeline Node **n'appelle pas les MCP directement** : ce sont des outils de
Claude Code. Le pont est le protocole de `src/mcp/pont.ts` — le pipeline écrit
une demande dans `content/<module>/<Vxx>/mcp/<nom>.demande.json`, Claude Code
exécute l'appel MCP et dépose la réponse dans `<nom>.reponse.json`, validée par
zod. Voir `src/mcp/README.md`.

## Images du présentateur

`assets/presentateur/` contient les **16 photos détourées du présentateur
RapidoCRM**, partagées par les 172 tutoriels. On ne les régénère jamais : on
pioche dedans.

- `src/brand/presentateur.ts` décrit chaque pose (intention, direction du
  regard) et sépare les poses de **hook** (le problème : surpris, réflexion,
  stop, présentation…) de celles d'**image de fin** (le résultat : victoire,
  deux pouces, OK, casque…).
- Le choix est **déterministe** : `poseHook(module, numero)` et
  `poseFin(module, numero)` donnent toujours la même pose pour un tutoriel
  donné, et répartissent les poses sur le catalogue.
- Les fichiers sont en WebP avec canal alpha : le présentateur se pose
  directement sur les aplats de la charte, sans cadre. Il est calé sur le bord
  bas de la frame — la photo source est coupée au buste.

## Nommage des sorties

```
content/<module>/<Vxx-slug>/
  source.mp4  analyse.json  fiche.json  script.json  script.md
  voix/{hook,intro,etape-01…,claude,punchline}.mp3
  voix/{alignement.json,complete.mp3,manifest.json}
  transcription.txt  transcription-chapitres.json
  out/master-16x9.mp4  out/master-9x16.mp4
  out/thumb-16x9.jpg   out/thumb-9x16.jpg
  rendu.json  qa.json  publication.json  pipeline.log
```

Fichiers déposés dans la bibliothèque RapidoCMS :
`rapidocrm-tuto-<module>-<Vxx>-<slug>.mp4` (`-vertical`, `-thumb`,
`-thumb-vertical` pour les autres).
