#!/usr/bin/env bash
# Rend les Reels/TikTok décrits dans data/reels/*.json (ou ceux passés en argument).
#   bash scripts/render-reels.sh                      -> tous les Reels, version de travail
#   FINAL=1 bash scripts/render-reels.sh reel-03-diner -> un Reel, sans bandeau
# Pour chaque Reel : index.html (build) -> vidéo muette (HyperFrames) -> musique (music.py)
# -> mix (voix assets/voice/<reel>.wav si présente) -> renders/reels/<reel>.mp4
set -euo pipefail
cd "$(dirname "$0")/.."
mkdir -p renders/reels assets/music/reels
NAMES=("$@"); [[ ${#NAMES[@]} -eq 0 ]] && NAMES=($(ls data/reels | sed 's/\.json$//'))
for n in "${NAMES[@]}"; do
  node scripts/build.mjs "data/reels/$n.json" ${FINAL:+--final}
  npx hyperframes render --quality ${QUALITY:-high} --output "renders/reels/$n-muette.mp4" --quiet 2>&1 | grep -iE "error|fail" || true
  python3 scripts/music.py "data/reels/$n.json" "assets/music/reels/$n.wav"
  suffix=$([[ -n "${FINAL:-}" ]] && echo final || echo version-de-travail)
  MUSIC="assets/music/reels/$n.wav" VOICE="assets/voice/$n.wav" bash scripts/mix.sh "renders/reels/$n-muette.mp4" "renders/reels/${n}_9x16_${suffix}.mp4"
  rm -f "renders/reels/$n-muette.mp4"
done
node scripts/build.mjs data/timeline.json >/dev/null   # remet le teaser dans index.html
