#!/usr/bin/env bash
# Récupère les plans de la bibliothèque Higgsfield pour le volet « sans » et
# leur applique l'étalonnage du registre.
#
# Aucune génération n'est lancée : les treize plans utilisés ici sont déjà
# tournés et payés (cf. PLANS-TOURNES.md). Trois appartiennent nativement au
# registre « sans » — le chef qui recopie ses DLC dans un cahier, les trois
# tablettes dépareillées, le directeur et ses sept onglets. Les autres sont
# des plans neutres : des lieux vides, sans personne et sans interface. Un
# lieu vide n'a pas de registre, c'est l'étalonnage qui le lui donne.
#
# L'étalonnage « sans » (NOTES §6.3) : gris plat, désaturé, couvert. On
# retire 82 % de la saturation, on refroidit, on écrase le contraste et on
# lève un peu les noirs — le rendu d'une pièce éclairée au néon un jour de
# pluie. C'est ce qui interdit de confondre un plan « sans » avec le même
# lieu vu dans un film « avec ».
#
# Un plan tiers reste interdit : ces treize plans ne montrent aucune
# interface de logiciel identifiable (§6.1).
set -euo pipefail

HERE="$(cd "$(dirname "$0")" && pwd)"
SRC="$HERE/../_plans-sans/src"
OUT="$HERE/../../../studio-video/assets/plates"
mkdir -p "$SRC"

B="https://d8j0ntlcm91z4.cloudfront.net/user_3GXYlNxkbz83gXaGDVVrTni1dX2"

# nom-local  fichier-distant
declare -A PLANS=(
  [sans-cahier]="hf_20260808_140958_ed282779-0727-44db-8e60-198d23efb982"
  [sans-tablettes]="hf_20260808_140957_a2edd7a3-9dce-489c-8c2d-cd870b7abe2e"
  [sans-onglets]="hf_20260808_142454_7e963f00-501c-4f2b-82d5-3a95e489dd4a"
  [cuisine-vide-matin]="hf_20260808_140958_2f833e20-512f-4e2f-8238-bf15ac77b0e6"
  [cuisine-vide-nuit]="hf_20260808_164554_4068b82e-a72d-46d4-9a0e-4bd17871f0a0"
  [couloir-cuisine]="hf_20260808_165532_134b04fa-4996-4ab4-a44c-cb38d9a65c14"
  [salle-chaises]="hf_20260808_140957_5e42a14e-21bb-4f32-a764-ff5874613b70"
  [salle-prete]="hf_20260808_170224_057335af-d702-47db-a267-c0e0fb4142f8"
  [salle-apres]="hf_20260808_173757_d19cd11b-8eab-4711-9127-0cc3f2a60a62"
  [imprimante-z]="hf_20260808_140957_d840d81b-3c41-4c15-b8c2-ae7bb51835a3"
  [tickets-empiles]="hf_20260808_155702_5787c5e3-4cf3-4c94-8892-2f5f6d22f2d2"
  [telephone-comptoir]="hf_20260808_181340_2cb82c2c-8bc2-40b0-a3c6-6cd17d858204"
  [bureau-matin]="hf_20260808_140957_6337e37d-d821-4043-b098-7f11abf408a7"
  [devanture-nuit]="hf_20260808_141302_bc6c8112-a5c2-49b0-a14e-72687edfb944"
)

# Étalonnage du registre « sans ». `hue=s` avant `eq` : désaturer d'abord,
# corriger la densité ensuite, sinon le contraste retravaille des couleurs
# qu'on s'apprête à retirer.
GRADE="hue=s=0.18,colorbalance=rs=-0.05:gs=-0.01:bs=0.09,eq=contrast=0.88:brightness=0.015:gamma=1.04:saturation=0.95"

# Certains plans sont tournés en vertical : on remplit le cadre 16:9 par
# recadrage centré plutôt que par bandes noires, un plan d'ambiance passant
# de toute façon derrière un voile.
FIT="scale=1920:1080:force_original_aspect_ratio=increase:flags=lanczos,crop=1920:1080"

enc=(-c:v libx264 -preset medium -crf 20 -pix_fmt yuv420p
     -r 30 -g 30 -keyint_min 30 -sc_threshold 0 -movflags +faststart)

for nom in "${!PLANS[@]}"; do
  f="$SRC/$nom.mp4"
  [ -s "$f" ] || curl -sSL -o "$f" "$B/${PLANS[$nom]}.mp4"
done

echo "--- source / sortie ---"
for nom in "${!PLANS[@]}"; do
  src="$SRC/$nom.mp4"
  dim=$(ffprobe -v error -select_streams v:0 -show_entries stream=width,height \
        -of csv=p=0:s=x "$src")
  dur=$(ffprobe -v error -show_entries format=duration -of csv=p=0 "$src")
  printf "  %-20s %-10s %5.1f s\n" "$nom" "$dim" "$dur"
done

# Les plans sont posés dans le sous-dossier de chaque film « sans » qui les
# emploie ; la table vit dans plates-sans.txt pour rester relisible.
while read -r sous nom; do
  case "$sous" in ""|\#*) continue ;; esac
  mkdir -p "$OUT/$sous"
  ffmpeg -nostdin -v error -i "$SRC/$nom.mp4" \
    -vf "$FIT,$GRADE,fps=30,setsar=1" -an "${enc[@]}" "$OUT/$sous/$nom.mp4" -y
  echo "  + $sous/$nom.mp4"
done < "$HERE/plates-sans.txt"
