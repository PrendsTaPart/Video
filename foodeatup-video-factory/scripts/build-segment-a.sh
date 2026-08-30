#!/usr/bin/env bash
# Monte le segment A : hook Higgsfield + texte incrusté + punchline à 5,0 s.
#
#   ./build-segment-a.sh EP003 "Ta marge, en ce moment."
#
# Le troisième argument, facultatif, est le texte de la punchline. Absent, il
# est lu dans state/episodes/EPxxx.json (champ `vo_punchline`).
#
# Attendus : le clip (assets/hooks/ ou dist/hooks/) et assets/vo/punchlines/EPxxx.mp3
set -euo pipefail

EP="${1:?usage: build-segment-a.sh EPxxx \"texte du hook\"}"
TEXTE="${2:?texte du hook manquant}"
R="$(cd "$(dirname "$0")/.." && pwd)"

POLICE="$R/templates/Poppins-800.ttf"

# Le clip peut être à deux endroits, et c'est voulu. `fetch-hooks.sh` dépose
# dans `assets/hooks/` ce qu'il vient de récupérer ; `dist/hooks/` porte les
# cent quatre-vingt-dix-sept qui ont été COMMITÉS, parce qu'une URL de CDN
# Higgsfield expire et qu'un fichier commité, non. Sur une machine neuve, seul
# `dist/` est peuplé — et sans ce repli, dix-neuf des vingt-trois masters de la
# saison 1 ne peuvent pas être remontés alors que leur clip est dans le dépôt.
HOOK="$R/assets/hooks/$EP.mp4"
[ -f "$HOOK" ] || HOOK="$R/dist/hooks/$EP.mp4"
[ -f "$HOOK" ] || { echo "  $EP : pas de clip, ni dans assets/hooks ni dans dist/hooks" >&2; exit 1; }

# Le texte du hook passe par un FICHIER, jamais en ligne dans le filtergraph.
# Vingt-trois accroches sur cent cinquante contiennent une apostrophe — « Ton
# chiffre d'affaires », « L'addition »… — et une apostrophe referme le text='…'
# de drawtext au milieu de la phrase : ffmpeg cherche alors un filtre nommé
# « sans outil.:fontsize=62 » et s'arrête. Échapper à la main marche jusqu'à ce
# qu'un titre contienne aussi un deux-points ou une virgule ; textfile ne se
# trompe jamais.
# La punchline est incrustée elle aussi. Elle ne l'était pas, et c'est la
# correction la plus rentable du segment : les quatre cinquièmes d'un fil social
# se regardent sans le son, et la punchline — la chute, la seule phrase qui
# donne son sel à l'épisode — n'existait que dans la bande son. On lisait la
# mise en place, on n'avait jamais le retournement.
PUNCH_TXT="${3:-}"
if [ -z "$PUNCH_TXT" ] && [ -f "$R/state/episodes/$EP.json" ]; then
  PUNCH_TXT="$(python3 -c "
import json
print(json.load(open('$R/state/episodes/$EP.json')).get('vo_punchline',''))")"
fi

# Les deux phrases passent par l'ajusteur avant d'être dessinées : `drawtext` ne
# replie pas et ne rétrécit pas, il coupe. Voir scripts/ajuster-texte.py.
ajuster() {  # $1 = phrase, $2 = taille de départ -> "taille" puis le texte
  ( cd "$R" && python3 scripts/ajuster-texte.py "$1" "$2" )
}
TEXTE_FIC="$(mktemp)"
PUNCH_FIC="$(mktemp)"
trap 'rm -f "$TEXTE_FIC" "$PUNCH_FIC"' EXIT

AJUST="$(ajuster "$TEXTE" 62)"
TAILLE_HOOK="$(printf '%s' "$AJUST" | head -1)"
printf '%s' "$(printf '%s' "$AJUST" | tail -n +2)" > "$TEXTE_FIC"
if [ "$TAILLE_HOOK" -lt 62 ]; then
  echo "  accroche : repliée/réduite à ${TAILLE_HOOK}px, 62 ne tenait pas dans le cadre"
fi

if [ -n "$PUNCH_TXT" ]; then
  AJUSTP="$(ajuster "$PUNCH_TXT" 58)"
  TAILLE_PUNCH="$(printf '%s' "$AJUSTP" | head -1)"
  printf '%s' "$(printf '%s' "$AJUSTP" | tail -n +2)" > "$PUNCH_FIC"
else
  TAILLE_PUNCH=58
  echo "  ATTENTION : pas de texte de punchline, la chute restera muette à l'écran." >&2
fi
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
# La punchline reste à l'écran le temps qu'elle est dite, plus un battement
# pour la relire. Elle s'efface avant la coupe : un texte encore présent quand
# le sting arrive donnerait l'impression qu'il déborde sur le carton.
read -r P_IN P_OUT <<<"$(python3 -c "
p = $PUNCH
print(f'{p:.2f} {min($DUREE_A - 0.20, p + $DUREE_PUNCH + 0.35):.2f}')")"
if [ -s "$PUNCH_FIC" ]; then
  INCRUST_PUNCH=",drawtext=fontfile='$POLICE':textfile='$PUNCH_FIC':fontsize=$TAILLE_PUNCH:fontcolor=white:borderw=6:bordercolor=black@0.8:line_spacing=10:x=(w-text_w)/2:y=h*0.80-text_h:enable='between(t,$P_IN,$P_OUT)'"
else
  INCRUST_PUNCH=""
fi
DUCK_NIV=0.16                    # -16 dB
# La musique du segment A. Le master n'en avait aucune avant les 9,5 s : les
# quatre premières secondes sortaient à -91 dBFS, un silence total sous l'image
# d'ouverture. Le lit reprend le MÊME morceau que le segment D, au même niveau
# et à sa position dans le temps du master — `atrim=0:9,5` ici, `16:26` là-bas —
# pour que ce soit une seule musique traversant l'épisode, pas deux morceaux.
BED_GAIN=0.224                   # -13 dB, comme le lit du segment D
# La fin du clip, éteinte.
#
# Le son d'ambiance des clips Higgsfield est bruyant là où il gêne le plus : sur
# EP002, la chute tape à -17,8 dBFS pendant que la punchline parle, et le clip
# sort encore à -20,1 dBFS au moment de passer au sting. Deux secondes de
# silence à la fin rendent la punchline lisible et nettoient le raccord.
#
# Zéro par défaut : les 216 masters déjà sortis gardent leur son entier. On
# l'active épisode par épisode.
#
#   SILENCE_FIN=2.0 ./scripts/build-segment-a.sh EP002 "Ton service du samedi soir."
SILENCE_FIN="${SILENCE_FIN:-0}"
# Le raccord sur le sting, lui, se traite sur les 150 : mesuré sur les vingt-deux
# masters de la saison 1, l'ambiance du clip tapait encore entre -7 et -20 dBFS
# à 9,45 s et tombait à -39 dBFS à 9,52 s. Une porte qui claque à chaque
# épisode, exactement au moment où le spectateur décide s'il reste. Un fondu de
# 0,40 s avant la coupe le règle sans toucher au gag, qui est joué depuis
# longtemps à cet endroit.
#
# Ce fondu-là ne remplace pas SILENCE_FIN : celui-ci éteint DEUX SECONDES pour
# dégager la punchline sur un clip bruyant, celui-là ferme juste la porte.
FONDU_FIN="${FONDU_FIN:-0.40}"
SILENCE_DEB="$(python3 -c "
fin = $DUREE_A - $FONDU_FIN
print(f'{max(0.1, $DUREE_A - $SILENCE_FIN - 0.25):.2f}' if $SILENCE_FIN > 0 else f'{fin:.2f}')")"
SILENCE_DUR="$(python3 -c "print('0.25' if $SILENCE_FIN > 0 else f'{$FONDU_FIN:.2f}')")"
DUCK_MUS=0.45                    # la musique s'efface moins que le clip : elle
                                 # est déjà 13 dB dessous
echo "  punchline : ${DUREE_PUNCH}s à ${PUNCH}s · duck ${DUCK_DEB}→${DUCK_HAUT}"

# Tous les rendus Higgsfield n'ont pas de piste son — EP001 n'en a aucune. Sans
# entrée [0:a] le filtergraph refuse de s'initialiser, alors on lui donne du
# silence : le duck s'applique dessus sans rien changer, la punchline passe
# seule, et le script reste le même pour les deux cas.
# --- Le clip plus court que la fenêtre ---------------------------------------
# Deux cent quinze clips sur deux cent seize font 10,04 s et remplissent les
# 9,5 s sans rien faire. EP001 fait 7,0 s — le premier épisode de la série, et
# le seul concerné.
#
# Sans traitement, ffmpeg n'a plus d'images après 7 s : la dernière gèle
# pendant deux secondes et demie. À l'écran ce n'est pas une pause, c'est une
# panne — on croit que la vidéo s'est coupée.
#
# On ne gèle donc pas, on RALENTIT la fin. Le clip joue à vitesse normale
# jusqu'au pivot, puis s'étire pour finir pile sur la fenêtre. Le gag — le
# chien qui attrape la frite — reste à sa vitesse, et le mouvement ne s'arrête
# jamais. `tpad` derrière ne sert que de filet contre les arrondis.
DUREE_CLIP="$(ffprobe -v error -show_entries format=duration -of csv=p=0 "$HOOK")"

# --- Le clip qui change de plan avant la fin ---------------------------------
# Cinq des vingt-quatre clips de la saison 1 — EP002, EP003, EP013, EP014,
# EP022 — ne tiennent pas un seul plan : entre 7,2 et 8,5 s, le rendu enchaîne
# sur un tout autre cadre, en général un chef qui parle face caméra. Ce
# deuxième plan n'a rien à voir avec le gag, et sa bouche bouge sans qu'aucun
# son n'en sorte.
#
# Personne ne l'avait vu parce qu'il n'existait pas : le segment A faisait 7 s
# quand ces clips ont été validés. En le portant à 9,5 s pour ne plus couper la
# chute, on a fait entrer dans le cadre ce que la fenêtre courte laissait
# dehors.
#
# On s'arrête donc au changement de plan et on étire ce qui précède — la même
# rampe que pour un clip trop court. Le gag garde sa vitesse jusqu'au pivot,
# ralentit ensuite, et le plan parasite ne rentre jamais.
#
#   COUPE=0 ./scripts/build-segment-a.sh EP003 "…"   # pour garder le clip entier
COUPE="${COUPE:-auto}"
if [ "$COUPE" = "auto" ]; then
  COUPE="$(ffmpeg -v error -i "$HOOK" -filter:v "select='gt(scene,0.35)',metadata=print:file=-" \
    -an -f null - 2>/dev/null \
    | { grep -o "pts_time:[0-9.]*" || true; } | cut -d: -f2 \
    | python3 -c "
import sys
# Un changement de plan ne compte que dans la fenêtre utile, et seulement s'il
# laisse assez de clip devant lui pour que le gag ait eu lieu.
t = [float(x) for x in sys.stdin.read().split() if 6.0 < float(x) < $DUREE_A]
print(f'{t[0]:.2f}' if t else '0')")"
fi
if [ "$COUPE" != "0" ]; then
  echo "  changement de plan à ${COUPE}s : le clip est arrêté là et étiré jusqu'à ${DUREE_A}s"
  DUREE_CLIP="$COUPE"
fi
read -r PIVOT ETIRE COURT <<<"$(python3 -c "
c, f = $DUREE_CLIP, $DUREE_A
if c >= f - 0.05:
    print('0 1 0')
else:
    # on garde intacts les deux tiers du clip, on étire le reste
    piv = c * 0.62
    print(f'{piv:.3f} {(f - piv) / (c - piv):.4f} 1')")"
if [ "$COURT" = "1" ]; then
  echo "  clip court : ${DUREE_CLIP}s pour ${DUREE_A}s -> ralenti ×${ETIRE} après ${PIVOT}s"
  RAMPE="setpts='if(lt(T,$PIVOT),PTS,($PIVOT+(T-$PIVOT)*$ETIRE)/TB)',fps=30,tpad=stop_mode=clone:stop_duration=$DUREE_A,"
else
  RAMPE="tpad=stop_mode=clone:stop_duration=$DUREE_A,"
fi

if [ "$(ffprobe -v error -select_streams a -show_entries stream=index -of csv=p=0 "$HOOK" | wc -l)" -eq 0 ]; then
  echo "  clip muet : piste de silence ajoutée"
  SON_CLIP=(-f lavfi -t "$DUREE_A" -i "anullsrc=r=48000:cl=mono")
  SRC_A="4:a"
else
  SON_CLIP=()
  SRC_A="0:a"
fi

ffmpeg -v error \
 -i "$HOOK" \
 -i "$PUNCH_WAV" \
 -i "$R/templates/logo_foodeatup.png" \
 -i "$R/templates/bgm.mp3" \
 "${SON_CLIP[@]}" \
 -filter_complex "\
 [0:v]trim=0:$DUREE_CLIP,setpts=PTS-STARTPTS,${RAMPE}fps=30,\
scale=1080:1920:force_original_aspect_ratio=increase,crop=1080:1920[v];\
 [v]drawtext=fontfile='$POLICE':textfile='$TEXTE_FIC':fontsize=$TAILLE_HOOK:fontcolor=white:\
borderw=6:bordercolor=black@0.8:line_spacing=10:x=(w-text_w)/2:y=h*0.13:\
enable='between(t,$T_IN,$T_OUT)'$INCRUST_PUNCH[vt];\
 [vt][2:v]overlay=$LOGO_X:$LOGO_Y:format=auto,format=yuv420p[vo];\
 [${SRC_A}]atrim=0:$DUREE_CLIP,asetpts=PTS-STARTPTS,aresample=48000,apad=whole_dur=$DUREE_A,\
volume='if(lt(t,$DUCK_DEB),1,if(lt(t,$DUCK_PLEIN),1-(1-$DUCK_NIV)*(t-$DUCK_DEB)/($DUCK_PLEIN-$DUCK_DEB),\
if(lt(t,$DUCK_FIN),$DUCK_NIV,if(lt(t,$DUCK_HAUT),$DUCK_NIV+(1-$DUCK_NIV)*(t-$DUCK_FIN)/($DUCK_HAUT-$DUCK_FIN),1))))':eval=frame,\
afade=t=out:st=$SILENCE_DEB:d=$SILENCE_DUR[a0];\
 [1:a]adelay=$(python3 -c "print(int($PUNCH*1000))")|$(python3 -c "print(int($PUNCH*1000))"),\
apad,atrim=0:$DUREE_A,asetpts=PTS-STARTPTS[a1];\
 [3:a]aresample=48000,atrim=0:$DUREE_A,asetpts=PTS-STARTPTS,volume=$BED_GAIN,\
afade=t=in:st=0:d=0.8,\
volume='if(lt(t,$DUCK_DEB),1,if(lt(t,$DUCK_PLEIN),1-(1-$DUCK_MUS)*(t-$DUCK_DEB)/($DUCK_PLEIN-$DUCK_DEB),\
if(lt(t,$DUCK_FIN),$DUCK_MUS,if(lt(t,$DUCK_HAUT),$DUCK_MUS+(1-$DUCK_MUS)*(t-$DUCK_FIN)/($DUCK_HAUT-$DUCK_FIN),1))))':eval=frame[a2];\
 [a0][a1][a2]amix=inputs=3:duration=first:dropout_transition=0:normalize=0[a]" \
 -map "[vo]" -map "[a]" -t $DUREE_A \
 -c:v libx264 -preset medium -crf 18 -r 30 -c:a aac -b:a 192k -ar 48000 \
 "$R/build/${EP}_A.mp4" -y

echo "$EP -> build/${EP}_A.mp4 ($(ffprobe -v error -show_entries format=duration -of csv=p=0 "$R/build/${EP}_A.mp4")s)"
