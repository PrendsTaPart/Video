#!/usr/bin/env bash
# Bobines d'écran de S1 · Salle avant le service.
#
# Mêmes règles que le parcours cuisine (NOTES §5 bis.4 et §7) : une bobine par
# scène plus longue que la scène, découpe entre 10 % et 65 % de la source,
# coupes franches, 1560x546, 30 fps, image-clé toutes les 30 images.
#
# Une exception de recadrage : TACHES (lire-ses-notifications) est la seule
# source en 1920x1020 — une capture de navigateur, pas d'application. On y
# prend une fenêtre de 672 px sous le chrome du navigateur, comme en C1.
set -euo pipefail

HERE="$(cd "$(dirname "$0")" && pwd)"
SRC="$HERE/assets/screens"
OUT="$HERE/../../../studio-video/assets/screens/s1"
TMP="$HERE/work/screens"

mkdir -p "$OUT" "$TMP"

enc=(-c:v libx264 -preset medium -crf 20 -pix_fmt yuv420p
     -r 30 -g 30 -keyint_min 30 -sc_threshold 0 -movflags +faststart)

seg() { # <sortie> <source> <in> <duree> [crop_y]
  ffmpeg -nostdin -v error -ss "$3" -t "$4" -i "$SRC/$2.mp4" \
    -vf "crop=1920:672:0:${5:-0},scale=1560:546,fps=30,setsar=1" \
    -an "${enc[@]}" "$TMP/$1.mp4" -y
}

concat_c() { # <sortie> <segments...>
  local out=$1; shift
  local list="$TMP/$out.txt"; : > "$list"
  for s in "$@"; do echo "file '$TMP/$s.mp4'" >> "$list"; done
  ffmpeg -nostdin -v error -f concat -safe 0 -i "$list" "${enc[@]}" "$OUT/$out.mp4" -y
}

# Bornes issues des timings réels de la voix (assets/transcript.json).
# Les scènes 10 et 12 n'apparaissent pas ici : ce sont des schémas animés,
# pour les deux étapes qui n'ont aucun tutoriel filmé.
seg s2a POINTAGE    7.0  2.55        #  7,39 -> 11,95 : « je pointe,
seg s2b TACHES     10.0  2.55  260   #                   je récupère mes tâches »
seg s3  RESAS       3.5  7.25        # 11,95 -> 18,47 : les réservations du jour
seg s4  APPELS      6.0 11.10        # 18,47 -> 29,52 : les appels de la nuit
seg s5  AJOUT-RESA 12.0  6.25        # 29,52 -> 34,76 : une réservation de plus
# Ce tutoriel est étapé, avec des libellés incrustés en bas (« 5 · Horaires
# d'ouverture »), que le recadrage à 672 px supprime. Les fenêtres avant 20 s
# ne montrent que la navigation dans les menus : l'écran des créneaux
# lui-même n'arrive qu'à l'étape 5, vers 22 s. Vérifié image par image.
seg s6  CRENEAUX   20.3  6.30        # 34,76 -> 40,68 : je ferme le créneau
seg s7  TABLES     18.0  4.50        # 40,68 -> 45,48 : la six est bancale
seg s8  PLACER     10.0  6.25        # 45,48 -> 51,24 : mon plan de salle
seg s9  QRCODE      8.0  6.40        # 51,24 -> 58,24 : les QR codes des tables
seg s11 WEB        16.0  8.35        # 58,24 -> 64,00 : les commandes web

concat_c SCENE-2 s2a s2b
for n in 3 4 5 6 7 8 9 11; do cp "$TMP/s$n.mp4" "$OUT/SCENE-$n.mp4"; done

echo "--- durée obtenue / durée de scène (la bobine doit dépasser) ---"
declare -A SCENE=([SCENE-2]=4.79 [SCENE-3]=7.00 [SCENE-4]=10.88 [SCENE-5]=6.03
                  [SCENE-6]=6.06 [SCENE-7]=4.26 [SCENE-8]=6.01 [SCENE-9]=6.19 [SCENE-11]=8.12)
for f in "$OUT"/SCENE-*.mp4; do
  n=$(basename "$f" .mp4)
  d=$(ffprobe -v error -show_entries format=duration -of csv=p=0 "$f")
  awk -v n="$n" -v d="$d" -v s="${SCENE[$n]}" \
    'BEGIN{printf "  %-10s %7.2f s  (scène %5.2f s)  %s\n", n, d, s, (d>=s+0.15 ? "ok" : "MARGE INSUFFISANTE")}'
done
