#!/bin/bash
# Copie dans public/ les vidéos et images déjà produites pour la Villa Beach (sources dans les dossiers voisins).
set -e
cd "$(dirname "$0")"; V=..
mkdir -p public
cp $V/serie-10-applications/img/foodeatup.png $V/serie-10-applications/img/toque.png public/
cp $V/plats-instagram/logo-villa-beach.png public/logo-villa-beach.png
cp $V/villa-beach-carte/site/pergola.jpg public/
cp $V/villa-beach-carte/villa-beach-carte-49s.mp4 public/carte.mp4
cp $V/souris-agneau/villa-beach-souris-agneau.mp4 public/souris.mp4
for s in magret foie-gras veloute tagliatelles-burrata burger-poulet jarret-agneau supreme-poulet pain-perdu fondant-chocolat; do cp $V/plats-instagram/final/villa-beach-$s.mp4 public/plat-$s.mp4; done
cp $V/villa-beach-fetes/out/villa-beach-noel-menu-1080x1920.mp4 public/noel.mp4
cp $V/villa-beach-fetes/out/villa-beach-nouvel-an-menu-1080x1920.mp4 public/nouvel-an.mp4
cp $V/villa-beach-fetes/assets/music-nye.mp3 public/musique.mp3
echo "public/ prêt"
