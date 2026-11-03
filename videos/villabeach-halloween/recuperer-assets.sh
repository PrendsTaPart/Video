#!/bin/bash
# Récupère les visuels du thème « chateau-hante » publiés par Lovable sur michael.foodeatup.fr
# Usage : bash videos/villabeach-halloween/recuperer-assets.sh   (relançable : ne retélécharge pas)
cd "$(dirname "$0")" && mkdir -p kit
B=https://michael.foodeatup.fr
for f in pergola-hantee.jpg chateau-orage.jpg grille-allee.jpg diner-hante.jpg piste-hantee.jpg fond-nuit.jpg \
  fantome.png squelette-danseur.png vampire.png sorciere-dj.png couple-zouk.png citrouille.png citrouille-oeil.png \
  chauve-souris.png cocktail-sang.png chandelier.png platine-citrouille.png eclair.png brume.png cadre-or.png; do
  [ -s kit/chateau-hante-$f ] || curl -fsS --retry 3 -o kit/chateau-hante-$f $B/img/kit/chateau-hante-$f || echo "absent : $f"
done
for v in boucle-pergola boucle-chateau boucle-brume boucle-citrouille; do
  [ -s kit/chateau-hante-$v.mp4 ] || curl -fsS --retry 3 -o kit/chateau-hante-$v.mp4 $B/video/kit/chateau-hante-$v.mp4 2>/dev/null || echo "vidéo absente : $v"
done
ls kit | wc -l
