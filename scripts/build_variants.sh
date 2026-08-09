#!/usr/bin/env bash
# /ep-montage (partie 2) — Découpe le master en 8 déclinaisons (voir 05-DECLINAISONS.md) :
# teaser 10s, 3 extraits punchline, recadrages 1:1 et 16:9, etc.
#
# Usage :
#   bash scripts/build_variants.sh <episode-dir>
set -euo pipefail

EP_DIR="${1:?Usage: build_variants.sh <episode-dir> (ex: episodes/ep01-la-rentree)}"
EXPORT_DIR="$EP_DIR/exports"
MASTER="$EXPORT_DIR/master_40s_9x16.mp4"

[[ -f "$MASTER" ]] || { echo "❌ $MASTER introuvable — lance build_master.sh d'abord."; exit 1; }

cut() {
  local name="$1" start="$2" end="$3"
  ffmpeg -y -ss "$start" -to "$end" -i "$MASTER" -c:v libx264 -crf 18 -c:a aac \
    "$EXPORT_DIR/${name}.mp4"
  echo "  → $EXPORT_DIR/${name}.mp4  [$start → $end]"
}

echo "Extraits temporels (source : 02-SCENARIO.md / 05-DECLINAISONS.md)"
cut "teaser_10s"        0    10
cut "extrait_A_il_a_tort"  0    15
cut "extrait_B_le_chaos"   10   25
cut "extrait_C_brocoli_parle" 19 34

echo "Recadrages"
# LinkedIn 1:1 1080x1080 — recadrage centré depuis le 9:16 1080x1920
ffmpeg -y -i "$MASTER" -vf "crop=1080:1080:0:420" -c:a copy \
  "$EXPORT_DIR/linkedin_1x1.mp4"
echo "  → $EXPORT_DIR/linkedin_1x1.mp4"

# Facebook — réutilise le master 9:16 tel quel
cp "$MASTER" "$EXPORT_DIR/facebook_9x16.mp4"
echo "  → $EXPORT_DIR/facebook_9x16.mp4"

# Post feed 4:5 1080x1350 — recadrage centré
ffmpeg -y -i "$MASTER" -vf "crop=1080:1350:0:285" -c:a copy \
  "$EXPORT_DIR/feed_4x5.mp4"
echo "  → $EXPORT_DIR/feed_4x5.mp4"

echo "✅ 8 déclinaisons générées dans $EXPORT_DIR/"
echo "   Thumbnails, cover, carrousel et story sondage sont générés séparément (RapidoCMS, voir /ep-montage)."
