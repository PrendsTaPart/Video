#!/usr/bin/env bash
# Rend un lot de vidéos décrit dans data/$DIR/*.json (DIR=reels ou DIR=stories) (ou ceux passés en argument).
#   bash scripts/render-reels.sh                      -> tous les Reels, version de travail
#   FINAL=1 bash scripts/render-reels.sh reel-03-diner -> un Reel, sans bandeau
# Pour chaque Reel : index.html (build) -> vidéo muette (HyperFrames) -> musique (music.py)
# -> mix (voix assets/voice/<reel>.wav si présente) -> renders/$DIR/<reel>.mp4
set -euo pipefail
DIR=${DIR:-reels}
cd "$(dirname "$0")/.."
mkdir -p renders/$DIR assets/music/$DIR
NAMES=("$@"); [[ ${#NAMES[@]} -eq 0 ]] && NAMES=($(ls data/$DIR | sed 's/\.json$//'))
for n in "${NAMES[@]}"; do
  node scripts/build.mjs "data/$DIR/$n.json" ${FINAL:+--final}
  npx hyperframes render --quality ${QUALITY:-high} --output "renders/$DIR/$n-muette.mp4" --quiet 2>&1 | grep -iE "error|fail" || true
  python3 scripts/music.py "data/$DIR/$n.json" "assets/music/$DIR/$n.wav"
  suffix=$([[ -n "${FINAL:-}" ]] && echo final || echo version-de-travail)
  MUSIC="assets/music/$DIR/$n.wav" VOICE="assets/voice/$n.wav" bash scripts/mix.sh "renders/$DIR/$n-muette.mp4" "renders/$DIR/${n}_9x16_${suffix}.mp4"
  rm -f "renders/$DIR/$n-muette.mp4"
done
node scripts/build.mjs data/timeline.json >/dev/null   # remet le teaser dans index.html
