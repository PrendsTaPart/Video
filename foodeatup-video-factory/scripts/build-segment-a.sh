#!/usr/bin/env bash
# Monte le segment A : hook Higgsfield + texte incrusté + punchline à 5,0 s.
#
#   ./build-segment-a.sh EP003 "Ta marge, en ce moment."
#
# Attendus : assets/hooks/EPxxx.mp4 et assets/vo/punchlines/EPxxx.mp3
set -euo pipefail

EP="${1:?usage: build-segment-a.sh EPxxx \"texte du hook\"}"
TEXTE="${2:?texte du hook manquant}"
R="$(cd "$(dirname "$0")/.." && pwd)"

POLICE="$R/templates/Poppins-800.ttf"

# Le texte du hook passe par un FICHIER, jamais en ligne dans le filtergraph.
# Vingt-trois accroches sur cent cinquante contiennent une apostrophe — « Ton
# chiffre d'affaires », « L'addition »… — et une apostrophe referme le text='…'
# de drawtext au milieu de la phrase : ffmpeg cherche alors un filtre nommé
# « sans outil.:fontsize=62 » et s'arrête. Échapper à la main marche jusqu'à ce
# qu'un titre contienne aussi un deux-points ou une virgule ; textfile ne se
# trompe jamais.
TEXTE_FIC="$(mktemp)"
printf '%s' "$TEXTE" > "$TEXTE_FIC"
trap 'rm -f "$TEXTE_FIC"' EXIT
LOGO_X=795; LOGO_Y=57
DUREE_A=9.5        # le clip tient 9,5 s : à 7 s la chute comique était coupée
PUNCH=5.0          # le beat comique du clip tombe ici
T_IN=0.8; T_OUT=3.5   # fenêtre du hook incrusté

# Le clip garde son ambiance, mais s'efface franchement sous la punchline.
#
# sidechaincompress a été essayé d'abord et ne suffisait pas : les rendus
# ElevenLabs sortent autour de -33 dBFS quand le clip Higgsfield tape à -20,
# soit 14 dB d'écart. La voix passait dessous.
#
# Deux corrections. La punchline est normalisée à -16 LUFS, donc au même niveau
# d'un épisode à l'autre quel que soit ce que rend ElevenLabs. Et le clip est
# baissé de 16 dB par une enveloppe explicite pendant qu'elle parle, avec des
# rampes de 0,25 s pour que la baisse ne s'entende pas comme une coupure.

# --- Passe 1 : normalisation de la punchline, à part -------------------------
# loudnorm NE PEUT PAS rester dans le filtergraph principal. Sur une entrée de
# 2 s il émet sa sortie avec des PTS décalés (frame 0 à 0,000 puis une frame de
# flush à 2,043) ; le atrim=0:DUREE_A qui suit prend ce décalage pour du temps
# écoulé et coupe la voix. Mesuré : la branche entière ressortait à -240 dBFS.
# Normalisée dans une passe séparée puis réinjectée en WAV, la voix arrive à
# -19 dBFS sur toute sa fenêtre.
PUNCH_WAV="$R/build/${EP}_punch.wav"
ffmpeg -v error -i "$R/assets/vo/punchlines/$EP.mp3" \
 -af "aresample=48000,loudnorm=I=-16:TP=-2:LRA=7,aresample=48000,asetpts=PTS-STARTPTS" \
 -ar 48000 -ac 1 -c:a pcm_s16le "$PUNCH_WAV" -y

# Le duck se cale sur la longueur réelle de la voix, pas sur une constante :
# une punchline de 2,8 s se ferait couper le dernier mot par une rampe fixe.
DUREE_PUNCH="$(ffprobe -v error -show_entries format=duration -of csv=p=0 "$PUNCH_WAV")"
read -r DUCK_DEB DUCK_PLEIN DUCK_FIN DUCK_HAUT <<<"$(python3 -c "
p=$PUNCH; d=$DUREE_PUNCH; fin=min($DUREE_A-0.10, p+d+0.15)
print(f'{p-0.40:.2f} {p-0.15:.2f} {fin:.2f} {min($DUREE_A,fin+0.10):.2f}')")"
DUCK_NIV=0.16                    # -16 dB
echo "  punchline : ${DUREE_PUNCH}s à ${PUNCH}s · duck ${DUCK_DEB}→${DUCK_HAUT}"

# Tous les rendus Higgsfield n'ont pas de piste son — EP001 n'en a aucune. Sans
# entrée [0:a] le filtergraph refuse de s'initialiser, alors on lui donne du
# silence : le duck s'applique dessus sans rien changer, la punchline passe
# seule, et le script reste le même pour les deux cas.
if [ "$(ffprobe -v error -select_streams a -show_entries stream=index -of csv=p=0 "$R/assets/hooks/$EP.mp4" | wc -l)" -eq 0 ]; then
  echo "  clip muet : piste de silence ajoutée"
  SON_CLIP=(-f lavfi -t "$DUREE_A" -i "anullsrc=r=48000:cl=mono")
  SRC_A="3:a"
else
  SON_CLIP=()
  SRC_A="0:a"
fi

ffmpeg -v error \
 -i "$R/assets/hooks/$EP.mp4" \
 -i "$PUNCH_WAV" \
 -i "$R/templates/logo_foodeatup.png" \
 "${SON_CLIP[@]}" \
 -filter_complex "\
 [0:v]trim=0:$DUREE_A,setpts=PTS-STARTPTS,fps=30,\
scale=1080:1920:force_original_aspect_ratio=increase,crop=1080:1920[v];\
 [v]drawtext=fontfile='$POLICE':textfile='$TEXTE_FIC':fontsize=62:fontcolor=white:\
borderw=6:bordercolor=black@0.8:x=(w-text_w)/2:y=h*0.13:\
enable='between(t,$T_IN,$T_OUT)'[vt];\
 [vt][2:v]overlay=$LOGO_X:$LOGO_Y:format=auto,format=yuv420p[vo];\
 [${SRC_A}]atrim=0:$DUREE_A,asetpts=PTS-STARTPTS,aresample=48000,\
volume='if(lt(t,$DUCK_DEB),1,if(lt(t,$DUCK_PLEIN),1-(1-$DUCK_NIV)*(t-$DUCK_DEB)/($DUCK_PLEIN-$DUCK_DEB),\
if(lt(t,$DUCK_FIN),$DUCK_NIV,if(lt(t,$DUCK_HAUT),$DUCK_NIV+(1-$DUCK_NIV)*(t-$DUCK_FIN)/($DUCK_HAUT-$DUCK_FIN),1))))':eval=frame[a0];\
 [1:a]adelay=$(python3 -c "print(int($PUNCH*1000))")|$(python3 -c "print(int($PUNCH*1000))"),\
apad,atrim=0:$DUREE_A,asetpts=PTS-STARTPTS[a1];\
 [a0][a1]amix=inputs=2:duration=first:dropout_transition=0:normalize=0[a]" \
 -map "[vo]" -map "[a]" -t $DUREE_A \
 -c:v libx264 -preset medium -crf 18 -r 30 -c:a aac -b:a 192k -ar 48000 \
 "$R/build/${EP}_A.mp4" -y

echo "$EP -> build/${EP}_A.mp4 ($(ffprobe -v error -show_entries format=duration -of csv=p=0 "$R/build/${EP}_A.mp4")s)"
