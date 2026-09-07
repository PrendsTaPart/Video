#!/usr/bin/env bash
# Piste de narration anglaise (ElevenLabs) posée sur le montage muet,
# puis muxée sans ré-encoder l'image.
#
#   ./build-voice.sh
#
# Entrées  : renders/braindcast-tiktok-demo-muet.mp4 (image, muette)
#            voice/bNN.mp3 + voice/script.tsv (répliques et points d'ancrage)
# Sortie   : renders/braindcast-tiktok-demo.mp4  ← le fichier à uploader
#
# voice/script.tsv : <id>  <début en s sur le montage final>  <texte dit>
# Les points d'ancrage sont calés sur le plan que la réplique décrit ;
# le script refuse de rendre si deux répliques se chevauchent.
set -euo pipefail
cd "$(dirname "$0")"

VIDEO=renders/braindcast-tiktok-demo-muet.mp4
OUT=renders/braindcast-tiktok-demo.mp4
DUR=$(ffprobe -v error -show_entries format=duration -of csv=p=0 "$VIDEO")

# Contrôle des chevauchements : une réplique ne doit jamais mordre sur la suivante.
python3 - "$DUR" <<'PY'
import csv, subprocess, sys
dur = float(sys.argv[1])
rows = list(csv.reader(open('voice/script.tsv'), delimiter='\t'))
prev_end, prev_id, bad = 0.0, None, False
for rid, start, text in rows:
    start = float(start)
    d = float(subprocess.run(
        ['ffprobe', '-v', 'error', '-show_entries', 'format=duration',
         '-of', 'csv=p=0', f'voice/{rid}.mp3'],
        capture_output=True, text=True, check=True).stdout)
    if start < prev_end:
        print(f"  CHEVAUCHEMENT {prev_id} -> {rid} : "
              f"{prev_id} finit à {prev_end:.2f}, {rid} commence à {start:.2f}")
        bad = True
    if start + d > dur:
        print(f"  DÉBORDE LA FIN  {rid} : finit à {start + d:.2f} > {dur:.2f}")
        bad = True
    prev_end, prev_id = start + d, rid
print(f"  narration : {sum(1 for _ in rows)} répliques, "
      f"dernière fin {prev_end:.2f}s sur {dur:.2f}s")
sys.exit(1 if bad else 0)
PY

# Graphe : chaque réplique décalée à son point d'ancrage, puis mixées.
# normalize=0 — sans lui, amix divise le niveau par le nombre d'entrées.
# loudnorm vise -16 LUFS ; sa fenêtre est bloquée (gated) donc les silences
# entre répliques ne tirent pas le gain vers le haut.
inputs=(); filters=(); labels=""
i=0
while IFS=$'\t' read -r id start _; do
  inputs+=(-i "voice/$id.mp3")
  ms=$(python3 -c "print(int(round(float('$start')*1000)))")
  filters+=("[$i:a]adelay=${ms}:all=1[a$i];")
  labels="${labels}[a$i]"
  i=$((i+1))
done < voice/script.tsv

ffmpeg -nostdin -hide_banner -v warning "${inputs[@]}" -filter_complex \
  "${filters[*]}${labels}amix=inputs=${i}:normalize=0:duration=longest,\
loudnorm=I=-16:TP=-1.5:LRA=11,apad,atrim=0:${DUR},aresample=48000[vo]" \
  -map "[vo]" -c:a pcm_s16le -y voice/voiceover.wav

# L'image ne repasse pas par l'encodeur : -c:v copy.
ffmpeg -nostdin -hide_banner -v warning -i "$VIDEO" -i voice/voiceover.wav \
  -map 0:v -map 1:a -c:v copy -c:a aac -b:a 128k -ac 1 \
  -movflags +faststart -y "$OUT"

ls -la "$OUT"
ffprobe -v error -show_entries format=duration,size \
        -show_entries stream=codec_type,codec_name,duration \
        -of default=noprint_wrappers=1 "$OUT"
