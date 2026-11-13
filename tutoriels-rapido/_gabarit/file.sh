#!/usr/bin/env bash
# File d'attente de production : enchaîne plusieurs épisodes, un journal par épisode dans /tmp/claude-0/<EP>.log.
# Usage : bash _gabarit/file.sh CMS03 CMS06 F01 ...
#   épisode tutoriel (CRM/CMS/RH) : make.sh ; formation (F..) : make-formation.sh
#   _gabarit/avant-<EP>.sh / apres-<EP>.sh, s'ils existent, préparent puis nettoient les données de démo locales.
cd "$(dirname "$0")/.."
for EP in "$@"; do
  LOG="/tmp/claude-0/$EP.log"
  [ -f "_gabarit/avant-$EP.sh" ] && bash "_gabarit/avant-$EP.sh" > "$LOG" 2>&1
  case "$EP" in
    F*|CMS24) bash _gabarit/make-formation.sh "$EP" >> "$LOG" 2>&1 ;;
    CMS*) bash _gabarit/make.sh "$EP" http://127.0.0.1:8125 >> "$LOG" 2>&1 ;;
    CRM*) bash _gabarit/make.sh "$EP" http://127.0.0.1:8124 >> "$LOG" 2>&1 ;;
    RH*) bash _gabarit/make.sh "$EP" http://127.0.0.1:8126 >> "$LOG" 2>&1 ;;
  esac
  echo "EXIT=$?" >> "$LOG"
  [ -f "_gabarit/apres-$EP.sh" ] && bash "_gabarit/apres-$EP.sh" >> "$LOG" 2>&1
done
