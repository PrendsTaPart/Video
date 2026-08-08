#!/usr/bin/env bash
# Bobines d'écran de C2 · Cuisine pendant le service.
#
# Mêmes règles que C1 (voir NOTES §5 bis.4), avec une différence assumée :
#
# COUPES FRANCHES, PAS DE FONDU ENCHAÎNÉ. Sur C1, une bobine montée en xfade
# imbriqué s'éteignait au rendu à partir de sa seconde transition, sans que
# rien ne distingue son fichier d'une bobine voisine qui, elle, passait. Trois
# pistes ont été écartées par l'expérience (images-clés espacées, flux laissé
# par le filtre, fenêtre déclarée trop longue) sans que la cause soit établie.
# Tant qu'elle ne l'est pas, on ne remet pas 350 ms de fondu en jeu contre le
# risque d'un plan éteint : on coupe franc, sur une respiration de la voix.
#
# Découpe : uniquement entre 10 % et 65 % de la source, les tutoriels se
# terminant par un carton marketing.
# Recadrage : 1920x828 -> 1920x672 (bandeau de sous-titre incrusté coupé)
# -> 1560x546, largeur du cadre tablette.
# Encodage : 30 fps, image-clé toutes les 30 images, +faststart.
set -euo pipefail

HERE="$(cd "$(dirname "$0")" && pwd)"
SRC="$HERE/assets/screens"
C1="$HERE/../c1-cuisine-avant/assets/screens"
OUT="$HERE/../../../studio-video/assets/screens/c2"
TMP="$HERE/work/screens"

mkdir -p "$OUT" "$TMP"

enc=(-c:v libx264 -preset medium -crf 20 -pix_fmt yuv420p
     -r 30 -g 30 -keyint_min 30 -sc_threshold 0 -movflags +faststart)

# seg <sortie> <dossier_source> <source> <in> <duree>
seg() {
  local out=$1 dir=$2 src=$3 ss=$4 d=$5
  ffmpeg -nostdin -v error -ss "$ss" -t "$d" -i "$dir/$src.mp4" \
    -vf "crop=1920:672:0:0,scale=1560:546,fps=30,setsar=1" \
    -an "${enc[@]}" "$TMP/$out.mp4" -y
}

concat_c() { # <sortie> <segments...>
  local out=$1; shift
  local list="$TMP/$out.txt"; : > "$list"
  for s in "$@"; do echo "file '$TMP/$s.mp4'" >> "$list"; done
  ffmpeg -nostdin -v error -f concat -safe 0 -i "$list" "${enc[@]}" "$OUT/$out.mp4" -y
}

# --- Scène 2 · j'affiche mon écran, poste par poste (12,84 s) --------------
# La configuration des postes, puis le tableau en direct : la voix passe de
# « chacun voit ce qui le concerne » à « quinze tickets en attente ».
seg s2a "$SRC" KDS  8.0  6.60
seg s2b "$SRC" KDS  24.0 6.65

# --- Scène 3 · les commandes de tous les canaux (15,48 s) ------------------
seg s3a "$SRC" COMMANDES 3.5 15.70

# --- Scène 4 · je fais avancer les plats (8,40 s) --------------------------
# Michael a fourni un montage court du même tutoriel (KDS-COURT, 21,32 s) en
# demandant d'en utiliser la fin. Elle va à cette scène plutôt qu'à la 2 :
# on y voit les boutons BUMP CHAUD et un plat déjà barré « en cours », qui
# est littéralement le geste décrit par la voix. La scène 2, elle, garde le
# parcours de configuration plus long de la version S3.
#
# Bornes relevées à la mesure, pas à l'œil : la luminance moyenne du tableau
# vaut 35,0 quand il est vide, 52 à 66 quand il porte des cartes, 223 sur la
# page de configuration. Les deux plages pleines sont 6,4-12,2 et 13,2-16,6 ;
# on prend l'une puis l'autre, en enjambant le creux.
seg s4a "$SRC" KDS-COURT  6.50 5.20
seg s4b "$SRC" KDS-COURT 13.20 3.40

# --- Scène 6 · retour de coupure et températures (6,68 s) ------------------
# Deux écrans déjà prélevés pour C1 : le pointage et le relevé d'équipement.
# Les reprendre est volontaire — c'est le même geste, deux fois dans la
# journée, et le film le dit.
seg s6a "$C1" ECRAN-01 7.0  3.50
seg s6b "$C1" ECRAN-03 13.0 3.50

# --- Scène 7 · PrediBot annonce la soirée (10,39 s) ------------------------
seg s7a "$SRC" PREDIBOT 8.0 10.60

concat_c SCENE-2 s2a s2b
cp "$TMP/s3a.mp4" "$OUT/SCENE-3.mp4"
concat_c SCENE-4 s4a s4b
concat_c SCENE-6 s6a s6b
cp "$TMP/s7a.mp4" "$OUT/SCENE-7.mp4"

echo "--- durée obtenue / durée de scène (la bobine doit dépasser) ---"
declare -A SCENE=([SCENE-2]=12.84 [SCENE-3]=15.48 [SCENE-4]=8.40 [SCENE-6]=6.68 [SCENE-7]=10.39)
for f in "$OUT"/SCENE-*.mp4; do
  n=$(basename "$f" .mp4)
  d=$(ffprobe -v error -show_entries format=duration -of csv=p=0 "$f")
  awk -v n="$n" -v d="$d" -v s="${SCENE[$n]}" \
    'BEGIN{printf "  %-9s %7.2f s  (scène %5.2f s)  %s\n", n, d, s, (d>=s+0.15 ? "ok" : "MARGE INSUFFISANTE")}'
done
