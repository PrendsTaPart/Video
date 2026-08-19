# L'avatar 3D — le chef qui parle, sans HeyGen

Le segment D d'un épisode montre quelqu'un qui explique le logiciel. Jusqu'ici
ce plan venait de HeyGen : un rendu à commander, à télécharger et à déposer à la
main, pour chacun des 337 épisodes.

Il est maintenant calculé ici, à partir de deux choses qu'on a déjà : la voix de
l'épisode, et `assets/chef.glb`.

## Pourquoi ce modèle-là

`chef.glb` porte **les quinze visèmes Oculus** (`viseme_aa`, `viseme_PP`, …), le
jeu **ARKit** complet — sourcils, paupières, joues, bouche — et un squelette de
67 os dont `Head`, `Neck` et les deux yeux. Il a été construit pour être animé
par de l'audio. On ne devine donc aucune forme de bouche : on la demande.

Le fichier est compressé en **meshopt**. Sans `MeshoptDecoder`, three.js refuse
de le charger — c'est la première chose qui casse si on reprend ce code ailleurs.

## La chaîne

    voix .wav ──> visemes.py ──> visemes-EPxxx.json ──> rendu.mjs ──> images
                                                            │
                                        scene.html (three.js, Chromium headless)

    ffmpeg assemble les images et la voix -> assets/avatar/EPxxx.mp4

Puis `build-episode.sh` prend ce fichier comme n'importe quel avatar.

## Ce qui a demandé plusieurs essais

**Le dosage de la bouche.** Un visème ouvre déjà la mâchoire. Y ajouter
`jawOpen` à pleine force fait sortir la langue, qui remplit alors le cadre.
Puis, corrigé trop fort dans l'autre sens, la bouche s'ouvrait en grand sur
chaque voyelle — le chef criait. Les plafonds actuels (0,62 pour les voyelles,
0,48 pour les consonnes) sont le troisième réglage, et le bon.

**Le lissage.** 119 visèmes sur 244 images : chaque forme ne tient que deux
images. Sans moyenne glissante, la bouche ne parle pas, elle vibre.

**Le cadrage.** `build-episode.sh` ne garde que `crop=1080:960:0:30` du rendu.
Cadré au centre d'un 1080 × 1920, l'avatar y perd sa bouche : il ne reste que
les yeux et la toque. La caméra vise donc le buste (`cible=0.22`), et se règle
en regardant le résultat DÉCOUPÉ, jamais le rendu brut.

**Le regard.** Il ne suit pas la parole. Un regard calé sur la voix donne un
pantin ; un regard qui dérive et cligne à son propre rythme donne quelqu'un qui
pense en parlant.

## Utilisation

    python3 visemes.py voix.wav "le texte, mot pour mot" visemes-EP001.json
    (python3 -m http.server 8811 &)   # three.js charge par HTTP, pas file://
    node rendu.mjs
    ffmpeg -framerate 30 -i images/f%04d.png -i voix.wav … avatar-EP001.mp4

## Le coût

Six minutes de calcul par épisode, en WebGL logiciel (SwiftShader, pas de GPU).
Sur 337 épisodes : environ 34 heures en tâche de fond. Aucun crédit, aucun
service extérieur, et le résultat est reproductible — rien n'est aléatoire, tout
est fonction de l'indice d'image.
