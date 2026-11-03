#!/usr/bin/env bash
# Final mux for foodeatup-rapport-historique-tuto.
# Method note (differs from other tutos' build.py/ffmpeg-only pipeline):
# this project's rush (screen.mp4) was corrupted beyond ~4s of usable
# footage, so the visual track is an HTML/CSS scene (scene.html) driven by
# CSS animation-delay timers, captured with Playwright (record.js) instead
# of cut from raw screen recording. Everything else (VO lines, Claude
# 3-stage sequence via videos/_shared/claude_prompt_sequence.py, thumbnail
# reuse) follows FOODEATUP-TUTORIELS-WORKFLOW.md as usual.
#
# Because the visual track comes from a live browser recording rather than
# frame-accurate ffmpeg cuts, line offsets were NOT assumed from the CSS
# delays directly (browser paint start + a VP8 recording clock drift meant
# actual on-screen timing landed 0.4-2.9s after the nominal CSS delay, and
# the drift wasn't constant). Offsets below were measured empirically: a
# 9-colour corner marker (removed in the final scene.html) was flashed at
# each Nx boundary and the recording was scanned frame-by-frame to find the
# real timestamp of each colour change. See SCRIPT.md for the full table.
set -euo pipefail
cd "$(dirname "$0")"
FF="${FFMPEG_BIN:-ffmpeg}"

declare -A OFF=(
  [N0]=400 [N1]=5040 [N2]=9120 [N3]=12480 [N4]=19120
  [N5]=23280 [N6]=29560 [N7]=34440 [N8]=39040
)

cd vo
INPUTS=(); FILTERS=""; AMIX_IN=""; i=0
for n in N0 N1 N2 N3 N4 N5 N6 N7 N8; do
  INPUTS+=(-i "$n.mp3")
  d=${OFF[$n]}
  FILTERS+="[$i:a]adelay=${d}|${d}[a$i];"
  AMIX_IN+="[a$i]"
  i=$((i+1))
done
FILTERS+="${AMIX_IN}amix=inputs=9:normalize=0,alimiter=limit=0.85:level=disabled[out]"
"$FF" -y "${INPUTS[@]}" -filter_complex "$FILTERS" -map "[out]" full_vo_final.mp3
cd ..

# record.js -> work/rec/*.webm (run separately: node record.js)
WEBM=$(ls work/rec/*.webm | head -1)
"$FF" -y -i "$WEBM" -i vo/full_vo_final.mp3 -t 44.4 \
  -c:v libx264 -pix_fmt yuv420p -r 30 -crf 18 -preset medium \
  -c:a aac -b:a 192k \
  out/foodeatup-rapport-historique-tuto-v1.mp4

"$FF" -y -i assets/intro.jpg -vf "scale=1280:720" -q:v 3 out/thumbnail-youtube.jpg
echo "done -> out/foodeatup-rapport-historique-tuto-v1.mp4"
