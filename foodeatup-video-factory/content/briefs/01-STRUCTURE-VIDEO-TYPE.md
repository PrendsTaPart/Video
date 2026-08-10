# Anatomie d'un épisode — EP001 en modèle

> **Note honnête** : je ne peux pas lire le contenu d'un fichier MP4. Cette anatomie
> est reconstruite à partir de la spécification de montage, des prompts Higgsfield et
> HeyGen d'EP001 et de la charte. Elle est exacte au niveau des timecodes et des
> sources ; si le rendu réel diverge, c'est le rendu qu'il faut corriger, pas ce document.

EP001 est le **patron** des 149 autres. Une fois qu'il est bon, les suivants ne sont
qu'un changement de trois textes et de trois fichiers.

---

## Les 30 secondes, seconde par seconde

| t | Ce qu'on voit | Ce qu'on entend | Fichier source |
|---|---|---|---|
| 0,0 | Golden retriever sous une table de bistrot, terrasse ensoleillée | ambiance terrasse, couverts, murmure | `EP001_hook.mp4` |
| 0,8 → 3,5 | Hook incrusté : **Lui aussi attend ta commande.** | idem | texte ffmpeg |
| 5,0 | Une main attrape l'assiette, le chien vole une frite et se fige | disque rayé comique **+ punchline VO** | `EP001_punchline.mp3` |
| 5,0 → 7,0 | Regard coupable tenu, figé | silence après le SFX | — |
| **7,0** | **Coupe.** Le logo se compose | `sting_whoosh.wav` | `sting_logo.mp4` |
| 7,0 → 11,5 | 10 icônes de logiciels déconnectées, compteurs d'euros | **VO_A** : « Marre d'avoir dix logiciels… » | `transition_probleme.mp4` |
| 11,5 → 16,0 | Les icônes fusionnent, une donnée traverse le système | **VO_B** : « FoodEatUp, le logiciel qui fait jouer tes données… » | `promesse_data.mp4` |
| 16,0 → 26,0 | **Écran coupé en deux** : avatar en haut (45 %), screencast du logiciel en bas (55 %) | **audio HeyGen SEUL** — aucune voix ElevenLabs ici | `EP001_avatar.mp4` + `EP001_soft.mp4` |
| 25,5 | — | `riser_outro.wav` | — |
| 26,0 → 30,0 | Symbole infini bleu, résolution en logo | **VO_C** : « Alors, prêt à augmenter ton chiffre d'affaires ? » | `outro_infinite.mp4` |
| 29,7 → 30,0 | logo tenu | 0,3 s de silence **obligatoire** | — |

**Logo** : présent de 0,0 à 30,0. Bas-droite, sauf de 16,0 à 26,0 où il passe
haut-droite pour ne pas manger le screencast.

---

## Pourquoi cette structure marche

**Les 7 premières secondes n'ont rien à vendre.** Le chien ne parle pas du logiciel.
C'est ça qui fait rester : on regarde une scène, pas une publicité. Le hook incrusté
(« Lui aussi attend ta commande ») pose le double sens sans le résoudre.

**Le beat à 5,0 s est le pivot.** Le clip Higgsfield est écrit pour que la chute
tombe exactement là, et la punchline VO arrive dessus. C'est le seul endroit où la
blague et le message se touchent. Si le clip généré décale ce beat, on le régénère —
on ne recale pas le montage.

**Le sting à 7,0 s est un contrat.** Il dit au spectateur : la blague est finie, on
passe au sujet. Sans lui, la bascule est ressentie comme une trahison. Avec lui, elle
est ressentie comme un format. Au bout de dix épisodes, le whoosh est reconnu.

**Le segment D est le seul qui prouve.** 10 secondes d'écran réel du logiciel,
commentées par l'avatar. C'est là qu'on montre au lieu de promettre. La règle
« une action, un bénéfice, une preuve » interdit d'y empiler deux fonctionnalités :
dix secondes ne portent qu'une idée.

**Les 4 dernières secondes sont identiques sur les 150.** C'est voulu. La signature
de fin ne se négocie pas : elle construit la reconnaissance de série.

---

## Le partage de la parole

| Qui parle | Quand | Combien |
|---|---|---|
| Son du clip (diégétique) | 0,0 → 7,0 | 7 s |
| ElevenLabs — punchline | 5,0 → ~7,0 | 2 s |
| ElevenLabs — VO_A | 7,0 → 11,5 | 4,5 s |
| ElevenLabs — VO_B | 11,5 → 16,0 | 4,5 s |
| **HeyGen — avatar** | **16,0 → 26,0** | **10 s** |
| ElevenLabs — VO_C | 26,0 → 30,0 | 4 s |

**Règle non négociable** : entre 16,0 et 26,0 il n'y a **qu'une seule voix**, celle de
l'avatar. Deux sources actives sur cette plage = épisode rejeté au contrôle.

---

## Ce qui change d'un épisode à l'autre

Trois textes et trois fichiers. Rien d'autre.

| Change | Ne change jamais |
|---|---|
| le clip Higgsfield | les timecodes des 5 segments |
| le hook incrusté | les 3 VO fixes |
| la punchline VO | les 4 animations motion design |
| le script et le rendu HeyGen | la charte, le logo, les SFX |
| le screencast du tuto | la signature de fin |

C'est la raison pour laquelle 150 épisodes sont faisables : **13 des 30 secondes sont
déjà produites**, une fois pour toutes.

---

## Ce qu'on valide à l'œil sur EP001 avant de lancer les 149 autres

1. Le cadrage du segment D — l'avatar n'est pas coupé, les boutons du logiciel restent
   lisibles sur un téléphone tenu à bout de bras.
2. Le placement des sous-titres — ils ne chevauchent pas la ligne de séparation
   avatar / logiciel.
3. Le volume de la punchline sur le son du clip — la voix passe devant, le clip
   reste audible.
4. La lisibilité du logo sur un fond clair — si elle est mauvaise, on bascule sur
   `logo_foodeatup_blanc.png`.
5. La première frame — elle devient la vignette sur les cinq plateformes. Si elle est
   noire, on décale le point d'entrée de 3 images.
