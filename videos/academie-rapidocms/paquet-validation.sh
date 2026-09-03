#!/usr/bin/env bash
# Rassemble de quoi valider un tutoriel : la vidéo finie, la vignette, et les
# briques d'habillage isolées — pour juger chaque animation séparément.
#
#     ./paquet-validation.sh se-connecter-et-creer-son-compte
#
# Dépose le tout dans `_validation/<slug>/`.
set -eu
cd "$(dirname "$0")"
slug="${1:?usage: ./paquet-validation.sh <slug>}"
sortie="_validation/$slug"
mkdir -p "$sortie"

cp "$slug"/exports/*.mp4 "$slug"/exports/*.jpg "$sortie"/ 2>/dev/null || true

# Les briques d'habillage, telles que le montage les a rendues.
for brique in ouverture fin; do
  [ -f "$slug/composition/$brique.mp4" ] \
    && cp "$slug/composition/$brique.mp4" "$sortie/habillage-$brique.mp4"
done
[ -f "$slug/composition/carton-1.mp4" ] \
  && cp "$slug/composition/carton-1.mp4" "$sortie/habillage-carton-chapitre.mp4"

# La carte de prompt, dans ses deux états.
for etat in carte-version-minute-demande carte-version-minute; do
  [ -f "$slug/composition/$etat.png" ] \
    && cp "$slug/composition/$etat.png" "$sortie/$etat.png"
done

echo "→ $sortie"
ls -la "$sortie"
