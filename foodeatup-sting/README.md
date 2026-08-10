# Sting de fin FoodEatUp — Remotion

Sting réutilisable de 5 s à 30 fps. Zéro crédit : aucun rendu Higgsfield, aucun
rendu HeyGen. Le tracé est vectoriel, le lit sonore est synthétisé par ffmpeg,
seule la voix off passe par ElevenLabs.

## Séquence

| t | ce qui se passe |
|---|---|
| 0,0 → 0,4 | un point bleu apparaît au croisement du huit |
| 0,4 → 2,4 | le point parcourt le tracé et le dessine derrière lui, en pulsant 8 fois |
| 2,4 → 3,0 | la boucle se referme, flash de 2 images, le trait devient le logo |
| 3,0 → 4,2 | le logo se replie, la baseline monte de 12 px en fondu |
| 4,2 → 5,0 | un trait bleu se trace, `foodeatup.com` apparaît, fondu de sortie |

La voix off — « FoodEatUp. Huit boucles. Une infinité de solutions. » — démarre à
0,8 s. « Huit boucles » tombe à 2,3 s, sur la 8ᵉ pulsation et la fermeture de la
boucle.

## Le tracé

`scripts/gen-lemniscate.mjs` construit le huit en **un seul path continu** :
un `M`, quatre arcs, aucune levée de plume. C'est la condition pour que
`getTotalLength()` soit continu et que `stroke-dashoffset` révèle le tracé sans
saut.

La géométrie est mesurée sur `foodeatup-infinity.png` : 73 × 146, trait de 11 px,
deux lobes de même diamètre. Une lemniscate de Gerono a été essayée d'abord et
écartée — ses lobes sont pincés en sablier là où le sigle a deux anneaux ronds.

Le point lumineux suit la courbe par `getPointAtLength` sur un path hors écran :
c'est la seule façon de garantir qu'il est exactement sur le trait que
`stroke-dashoffset` est en train de découvrir.

## Rejouer pour une autre marque

Tout est en props Remotion — rien n'est écrit en dur :

| prop | défaut |
|---|---|
| `baseline` | « Une infinité de solutions pour gérer votre restaurant. » |
| `url` | `foodeatup.com` |
| `accent` | `#147AFF` |
| `fond` | `#FAF6E3` (le sable des 150 épisodes) |
| `encre` | `#14202B` |
| `logo` | `foodeatup-logo.png` (dans `public/`) |
| `avecVo` · `avecSon` | `true` |
| `pulsations` | `8` |
| `transparent` | `false` |
| `boucle` | `false` — ferme le plan sur le fond nu |

```bash
npx remotion render src/index.ts sting-1080x1920 out/autre.mp4 \
  --props='{"baseline":"…","accent":"#FF6B00","logo":"autre-logo.png","avecVo":false}'
```

## Commandes

```bash
npm install
node scripts/gen-lemniscate.mjs   # régénère le path du huit
node scripts/gen-sfx.mjs          # régénère le lit sonore
node scripts/render-all.mjs       # les cinq livrables dans out/
npx remotion studio               # aperçu interactif
```

## Livrables

| fichier | usage |
|---|---|
| `sting-1080x1920.mp4` | vertical, format principal |
| `sting-1920x1080.mp4` | paysage |
| `sting-1080x1080.mp4` | carré |
| `sting-alpha.webm` | VP9 + alpha, à incruster en overlay |
| `sting-loop-3s.mp4` | les 3 premières secondes, bouclables sans raccord |

## Coller le sting à la fin d'un épisode

Avec un fondu audio de 0,3 s à la jonction :

```bash
ffmpeg -i dist/tiktok/EP001.mp4 -i foodeatup-sting/out/sting-1080x1920.mp4 \
 -filter_complex "\
 [0:v]scale=1080:1920,setsar=1,fps=30[v0];\
 [1:v]scale=1080:1920,setsar=1,fps=30[v1];\
 [v0][v1]concat=n=2:v=1:a=0[v];\
 [0:a]aresample=48000,asetpts=PTS-STARTPTS[a0];\
 [1:a]aresample=48000,asetpts=PTS-STARTPTS[a1];\
 [a0][a1]acrossfade=d=0.3:c1=tri:c2=tri[a]" \
 -map "[v]" -map "[a]" \
 -c:v libx264 -preset slow -crf 20 -pix_fmt yuv420p \
 -c:a aac -b:a 192k -ar 48000 -movflags +faststart \
 EP001-avec-sting.mp4
```

Vérifié : le master passe de 30,0 s à **35,0 s**. `acrossfade` ne coupe pas
l'image, il ne croise que l'audio sur 0,3 s à la jonction.

Pour rester à 30,0 s, incruster plutôt `sting-alpha.webm` en overlay sur les
5 dernières secondes :

```bash
ffmpeg -i dist/tiktok/EP001.mp4 -c:v libvpx-vp9 -i foodeatup-sting/out/sting-alpha.webm \
 -filter_complex "[1:v]setpts=PTS+25/TB[s];[0:v][s]overlay=0:0:eof_action=pass[v]" \
 -map "[v]" -map 0:a -c:v libx264 -preset slow -crf 20 -pix_fmt yuv420p \
 -c:a copy -movflags +faststart EP001-sting-incruste.mp4
```

Le `-c:v libvpx-vp9` **avant** l'entrée webm n'est pas décoratif : le décodeur
VP9 par défaut ignore la couche alpha et l'incrustation sortirait opaque.
