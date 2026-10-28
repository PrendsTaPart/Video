#!/usr/bin/env bash
# Reconstitue le dossier a/ lu par composition.html (non versionné : ~65 Mo).
# Prérequis : dépôts frères clonés dans /home/user (foodeatup-haccp, -caisse-mobile,
# -fid-lit, -menu-digital, growth-loop-academy), ffmpeg, node + playwright.
# Les captures du jeu et de l'avatar se refont avec capture-jeu.js et capture-avatar.js
# (vidéos jeu.mp4 et avatar.mp4 attendues dans $CAP).
set -euo pipefail
H=${H:-/home/user}; P=$(cd "$(dirname "$0")/.." && pwd); A=$P/a; CAP=${CAP:-$P/work}
mkdir -p $A/{fid,haccp,caisse,menu,theme,brand,game,av,fonts}
g=$H/foodeatup-fid-lit/mobile/test/golden
for n in 01_attract 02_phone 04_home 07_wheel 08_survey 05_rewards; do cp "$(find $g -name "$n.png" | head -1)" $A/fid/; done
for n in foodeatup sushi trattoria bubble-coffee boulangerie street-burger; do cp "$(find $g -name "${n}_04_home.png" | head -1)" $A/theme/; done
for n in braise brasserie comptoir epure indigo prairie; do cp "$(find $H/foodeatup-caisse-mobile/app/docs/captures -name "$n-accueil.png" | head -1)" $A/theme/; done
cp $H/foodeatup-haccp/app/play/listing/fr-FR/images/phoneScreenshots/*.png $A/haccp/
curl -sSf -o $A/haccp/ecole-missions.webp https://haccp.foodeatup.fr/img/ecole-missions.webp
for n in 03-accueil 04-plan-de-salle 06-commande 07-paiement 21-formation 08-kds; do curl -sSf -o $A/caisse/$n.png https://caisse.foodeatup.fr/screens/$n.png; done
for n in Accueil_fr C02_fr C03_fr C05_fr C08_jeux_fr C08_points_fr R03_fr; do cp $H/foodeatup-menu-digital/app/test/goldens/$n.png $A/menu/; done
cp $H/foodeatup-haccp/design/brand/logo-foodeatup-toque-transparent.png $H/growth-loop-academy/public/brand/chartes/braindcode.png $H/Video/hero-video/assets/brand/foodeatup-logo-mascot.png $A/brand/
cp $H/foodeatup-fid-lit/mobile/assets/fonts/Manrope-{Medium,Bold,ExtraBold}.ttf $A/fonts/
# écran titre du jeu (430×932 @2x) : capture de https://formation.foodeatup.fr/jeux/restaurant-3d/index.html
[ -f $CAP/jeu-titre.png ] && cp $CAP/jeu-titre.png $A/game/title.png
ffmpeg -v error -ss 11 -t 15 -i $CAP/avatar.mp4 -vf "fps=30,crop=720:760:0:40,scale=540:-2" -q:v 3 $A/av/%04d.jpg
for spec in "g1 59.5 3.5" "g2 80 3" "g3 107 4" "g4 139.5 9"; do set -- $spec; mkdir -p $A/game/$1
  ffmpeg -v error -ss $2 -t $3 -i $CAP/jeu.mp4 -vf fps=30 -q:v 3 $A/game/$1/%04d.jpg; done
echo "a/ prêt"
