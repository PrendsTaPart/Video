#!/usr/bin/env bash
# Photos du registre « sans » déjà générées dans la bibliothèque Higgsfield.
#
# Cinq images produites le 8 août et jamais montées : un cahier à spirale
# couvert de dates au stylo, un ticket de commande tombé au sol, un comptoir
# de fin de service jonché de billets et de tickets froissés, trois tablettes
# dépareillées, et un écran d'ordinateur à sept onglets avec un pense-bête
# d'identifiants collé au bord. Elles ont exactement le sujet des neuf films.
#
# Elles viennent doubler le carton « ce que la journée a coûté », qui n'avait
# jusqu'ici qu'un fond plat : un compteur de fatigue posé sur une photo de
# fatigue se lit tout autrement qu'un compteur posé sur du blanc.
#
# Aucune génération payante : ce sont des images déjà réglées.
#
# ⚠️ Contrôle §6.1 fait image par image avant montage : aucune ne montre
# d'interface de logiciel lisible. L'écran aux sept onglets ne porte que des
# rectangles gris et un texte manuscrit illisible — c'est le nombre d'onglets
# qui parle, pas leur contenu.
set -euo pipefail

HERE="$(cd "$(dirname "$0")" && pwd)"
SRC="$HERE/../_plans-sans/photos"
OUT="$HERE/../../../studio-video/assets/photos/sans"
mkdir -p "$SRC" "$OUT"

B="https://d8j0ntlcm91z4.cloudfront.net/user_3GXYlNxkbz83gXaGDVVrTni1dX2"

declare -A PHOTOS=(
  [cahier-spirale]="hf_20260808_141122_6e30de31-5842-449b-b95f-eb4edaae9940"
  [ticket-au-sol]="hf_20260808_141122_af8af46a-540a-4d2f-942e-948be7e71f55"
  [comptoir-fin-service]="hf_20260808_141122_5bc5d9d0-7f24-43d0-824c-2900e3ef989a"
  [tablettes-depareillees]="hf_20260808_141122_e266f949-c8b3-4afa-8944-6fffd7c0050b"
  [sept-onglets]="hf_20260808_141122_cc20d9cd-40c1-4032-a81d-9c5a9de02f21"
)

# Même étalonnage que les plans animés (plans-sans.sh) : les photos et les
# plans se succèdent dans le même film, un étalonnage différent se verrait.
GRADE="hue=s=0.18,colorbalance=rs=-0.05:gs=-0.01:bs=0.09,eq=contrast=0.88:brightness=0.015:gamma=1.04:saturation=0.95"

# Note pour la relecture juridique (§6.1) — `sept-onglets`.
#
# La barre d'onglets a été relue au zoom ×3,5 : les libellés sont du faux
# texte illisible produit par le modèle, les favicons sont des ronds gris
# uniformes, et le pense-bête collé au bord de l'écran porte une écriture
# manuscrite sans mot lisible. Aucune marque, aucun nom de produit, aucune
# interface d'éditeur reconnaissable.
#
# Un floutage de la barre a été essayé et abandonné : il effaçait les onglets
# eux-mêmes, et un plan qui dit « sept onglets » sans qu'on puisse les compter
# ne dit plus rien. Le plan reste donc en clair, et il est inscrit dans la
# liste de relecture — c'est exactement le rôle de ce garde-fou.

for nom in "${!PHOTOS[@]}"; do
  f="$SRC/$nom.png"
  [ -s "$f" ] || curl -sSL -o "$f" "$B/${PHOTOS[$nom]}.png"
  # 1920x1080 pleine trame : la photo passe derrière un voile, elle doit
  # couvrir le cadre sans laisser de bord.
  ffmpeg -nostdin -v error -i "$f" \
    -vf "scale=1920:1080:force_original_aspect_ratio=increase:flags=lanczos,crop=1920:1080,$GRADE" \
    "$OUT/$nom.jpg" -y
  printf "  + %-24s %s\n" "$nom" \
    "$(ffprobe -v error -select_streams v:0 -show_entries stream=width,height -of csv=p=0:s=x "$OUT/$nom.jpg")"
done
