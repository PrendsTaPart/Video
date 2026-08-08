#!/usr/bin/env bash
# Bobines d'écran de S2 · Salle pendant le service.
#
# Mêmes règles que le reste de la série (NOTES §5 bis.4 et §7).
#
# Deux précautions propres à ce film :
#
# 1. La scène 7 n'a pas de bobine : les trois étapes du module Caisse POS
#    (encaissement, séparation d'addition, remise) sont réunies en un schéma
#    animé, faute de tutoriel tourné.
# 2. FIDELITE : ne rien prélever entre 55 % et 65 % de la source (29,3 s à
#    34,7 s). L'enregistrement y laisse apparaître la fenêtre de
#    l'application Claude sur le bureau — une application tierce n'a rien à
#    faire dans un film FoodEatUp.
set -euo pipefail

HERE="$(cd "$(dirname "$0")" && pwd)"
SRC="$HERE/assets/screens"
OUT="$HERE/../../../studio-video/assets/screens/s2"
TMP="$HERE/work/screens"

mkdir -p "$OUT" "$TMP"

enc=(-c:v libx264 -preset medium -crf 20 -pix_fmt yuv420p
     -r 30 -g 30 -keyint_min 30 -sc_threshold 0 -movflags +faststart)

seg() { # <sortie> <source> <in> <duree>
  ffmpeg -nostdin -v error -ss "$3" -t "$4" -i "$SRC/$2.mp4" \
    -vf "crop=1920:672:0:0,scale=1560:546,fps=30,setsar=1" \
    -an "${enc[@]}" "$TMP/$1.mp4" -y
}

concat_c() { # <sortie> <segments...>
  local out=$1; shift
  local list="$TMP/$out.txt"; : > "$list"
  for s in "$@"; do echo "file '$TMP/$s.mp4'" >> "$list"; done
  ffmpeg -nostdin -v error -f concat -safe 0 -i "$list" "${enc[@]}" "$OUT/$out.mp4" -y
}

# Bornes issues des timings réels de la voix (assets/transcript.json).
seg s2  PLACER      6.0  5.20   #  2,15 -> 7,10  : je place mon premier client
seg s3  QRTABLE    10.0  6.20   #  7,10 -> 13,04 : le client scanne le QR
seg s4  MULTI       8.0  8.75   # 13,04 -> 21,52 : toutes mes commandes, une file
seg s5  MULTI      20.0  7.30   # 21,52 -> 28,59 : une commande de livraison
seg s6  NOSHOW     10.0  7.20   # 28,59 -> 35,56 : le no-show
# Le tableau de bord fidélité (membres, points en circulation, bons à
# valider) plutôt que la configuration du programme : c'est un client qu'on
# inscrit, pas un barème qu'on règle.
# Les quatre premières secondes sont le carton-titre du tutoriel (« BOOSTER
# LA FIDÉLITÉ », avec un présentateur) : on montre le produit, pas l'habillage
# du tutoriel.
seg s8  FIDELITE    5.0  6.80   # 44,39 -> 50,96 : l'inscription à la fidélité
# Fenêtre décalée pour ne pas remontrer le même écran que la scène 8 : les
# deux tutoriels fidélité se ressemblent beaucoup.
seg s9  RECOMPENSE 24.0  3.30   # 50,96 -> 54,02 : la récompense validée
seg s10a RESAS      3.0  3.10   # 54,02 -> 59,94 : les réservations du soir,
# PLACER n'est utilisable que jusqu'à ~17 s (44 % de la source) : le carton
# de prompt Claude y arrive bien avant la limite habituelle des 65 %.
seg s10b PLACER    12.0  3.10   #                  puis on replace les clients

for n in 2 3 4 5 6 8 9; do cp "$TMP/s$n.mp4" "$OUT/SCENE-$n.mp4"; done
concat_c SCENE-10 s10a s10b

echo "--- durée obtenue / durée de scène (la bobine doit dépasser) ---"
declare -A SCENE=([SCENE-2]=4.95 [SCENE-3]=5.94 [SCENE-4]=8.48 [SCENE-5]=7.07
                  [SCENE-6]=6.97 [SCENE-8]=6.57 [SCENE-9]=3.06 [SCENE-10]=5.92)
for f in "$OUT"/SCENE-*.mp4; do
  n=$(basename "$f" .mp4)
  d=$(ffprobe -v error -show_entries format=duration -of csv=p=0 "$f")
  awk -v n="$n" -v d="$d" -v s="${SCENE[$n]}" \
    'BEGIN{printf "  %-10s %7.2f s  (scène %5.2f s)  %s\n", n, d, s, (d>=s+0.15 ? "ok" : "MARGE INSUFFISANTE")}'
done
