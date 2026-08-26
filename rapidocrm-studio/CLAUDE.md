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

- **Police unique : Arial** (Helvetica en repli). Aucune autre — sauf la carte
  prompt de la séquence 4, qui porte la charte Claude (voir plus bas).
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
  `poseFin(module, numero, titre)` donnent toujours la même pose pour un
  tutoriel donné. La pose de fin suit d'abord le contenu (voir « La fin de
  vidéo »), l'empreinte ne servant qu'en dernier recours.
- Les fichiers sont en WebP avec canal alpha : le présentateur se pose
  directement sur les aplats de la charte, sans cadre. Il est calé sur le bord
  bas de la frame — la photo source est coupée au buste.

## Le présentateur en bulle, et l'avatar

Méthode reprise du projet **Plan'It** (`videos/planit-tuto-00-creer-son-compte/AVATAR.md`
et `videos/planit-academy/habillage/presentatrice.py`), qui a fait ses preuves sur
43 épisodes.

**Le principe.** La synchronisation labiale part d'un **rendu image fixe**, pas
du modèle 3D : le `.glb` d'une persona sert à produire les images, ce sont elles
qui alimentent le modèle. Portrait + piste voix → `creatify-aurora` (ElevenLabs)
→ plan parlant.

**Un seul plan pour toute la série.** Le plan est rendu **une fois**, sur un texte
générique, puis réutilisé par les 172 tutoriels et bouclé en aller-retour pour
éviter le saut du raccord. C'est le seul poste facturé à la seconde : un plan de
8,6 s coûtait 1,39 $ chez Plan'It. Un plan par épisode multiplierait ce coût par
172 sans rien apporter, puisque le titre est déjà affiché à l'écran.

**Le repli, gratuit.** Sans `assets/avatar/parle.mp4`, la bulle affiche
`assets/avatar/portrait.webp` : l'habillage reste animé, seule la bouche ne bouge
plus. C'est le mode d'itération — on ne relance une génération payante que
lorsque la mise en page est arrêtée.

**L'habillage** (`src/brand/Avatar.tsx`) est calculé localement, sans rien
facturer : bulle en `easeOutBack`, anneau dégradé en rotation lente dont
l'épaisseur suit la voix, halo dont le rayon suit la voix, et treize barres de
niveau où l'onde se propage du centre vers les bords. **C'est la voix qui pilote
l'animation, jamais l'inverse** — `src/template/niveauVoix.tsx` lit l'enveloppe
de la piste avec `visualizeAudio`.

**Où se place la bulle**

| Format | Place | Répartition |
|---|---|---|
| 16:9 | en bas à droite, par-dessus le mockup | bulle à 20 % de la hauteur |
| 9:16 | en haut, au-dessus du logiciel | **1,5 pour l'avatar · 2,5 pour le logiciel**, sur 4 parts |

**Le logiciel est toujours dans un mockup** (`src/brand/Mockup.tsx`) : fenêtre de
navigateur avec barre de titre, pastilles et adresse. Sans ce cadre, un
enregistrement large se retrouve rogné par les bords en 9:16 et on ne comprend
plus qu'on regarde un logiciel.

## La carte prompt porte la charte Claude

Exception assumée à la règle « Arial et palette RapidoSoftware partout » : la
carte de la séquence 4 représente **Claude**, comme une capture d'écran porterait
l'interface qu'elle montre. Elle utilise donc la charte d'Anthropic
(`src/brand/claude.ts`) :

| Rôle | Valeur |
|---|---|
| Fond de carte | `#faf9f5` |
| Texte | `#141413` |
| Accent (bouton, surlignage des variables) | `#d97757` |
| Gris de libellé | `#b0aea5` |
| Titres | Poppins, Arial en repli |
| Corps du prompt | Lora, Georgia en repli |

Le logo Claude (`assets/ia/claude.png`) ouvre l'en-tête, suivi du nom de l'outil
MCP visé. **Le reste de la frame reste à la charte RapidoSoftware.**

## La fin de vidéo

- **Le logo officiel** `assets/logos/rapidocrm-complet.png` est monté **tel
  quel** : jamais redessiné, jamais tourné, scale uniforme.
- Il se pose en deux temps : un halo s'ouvre une seule fois derrière lui, un
  trait vert se trace dessous, puis le slogan et l'adresse suivent.
- **Le présentateur reste d'un bout à l'autre** de la séquence : il porte la
  punchline, puis accompagne la carte de fin.
- **La pose vient du contenu**, pas d'un tirage : `poseFin(module, numero, titre)`
  applique des règles — compte et accès → accueil, équipe → bras ouverts, support
  → casque, facture et contrat → OK, campagne et workflow → victoire. L'empreinte
  ne sert qu'en dernier recours, pour répartir les poses restantes.

## Autres assets partagés

- `assets/ia/` — logos des assistants. **Seul `claude.png` est monté**, dans
  l'en-tête de la carte prompt (séquence 4) : c'est une décision prise, la
  séquence dit « collez-le dans Claude » et reste sur un seul assistant.
  `openai.png` et `mistral.png` restent en réserve, non montés — ne les ajouter
  au template que sur demande explicite.
- `assets/ecrans/` — la **banque d'écrans RapidoCRM** (17 maquettes fournies
  par l'équipe produit), décrite par `src/brand/ecrans.ts` : titre, module,
  mots-clés, et `cadrage` (`capture` = l'écran remplit le cadre, utilisable
  comme plan de démonstration ; `mockup` = ordinateur en situation, illustration
  seulement). `ecranPour(module, titre, cadrage)` choisit le meilleur écran, ou
  **rien** si aucun ne correspond vraiment — mieux vaut pas d'écran qu'un écran
  hors sujet. `npm run ecrans` liste la banque, `--pour "<titre>"` montre le
  choix retenu.

  Ces maquettes ne remplacent jamais l'enregistrement réel d'un tutoriel publié.
  Quand `source.mp4` manque, le rendu retombe dessus **avec un avertissement** :
  la vidéo se monte, mais la démonstration n'est pas une vraie capture.

Tous ces dossiers (`presentateur/`, `ia/`, `ecrans/`, `avatar/`) sont recopiés dans
`public/` par `copierAssetsPartages`, appelé au rendu et par
`npm run prepare:assets`.

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
