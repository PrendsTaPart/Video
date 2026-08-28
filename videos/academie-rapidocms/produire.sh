#!/usr/bin/env bash
# Production d'un ou plusieurs tutoriels : découpage de la voix off, puis montage.
#
#     ./produire.sh configurer-son-profil remplir-sa-fiche-entreprise
#
# Suppose que `audio/vo-brute.mp3` est déjà déposé dans le dossier du tutoriel
# (génération ElevenLabs). Journalise dans `_logs/<slug>.log`.
set -u
cd "$(dirname "$0")"
mkdir -p _logs

for slug in "$@"; do
  if [ ! -f "$slug/audio/vo-brute.mp3" ]; then
    echo "[$slug] voix off manquante — ignoré"
    continue
  fi
  echo "[$slug] découpage…"
  ( cd "$slug" && python3 episode.py --decouper ) > "_logs/$slug.log" 2>&1 || {
    echo "[$slug] ÉCHEC au découpage — voir _logs/$slug.log"; continue; }
  echo "[$slug] montage…"
  ( cd "$slug" && python3 episode.py ) >> "_logs/$slug.log" 2>&1 || {
    echo "[$slug] ÉCHEC au montage — voir _logs/$slug.log"; continue; }
  echo "[$slug] terminé : $(ls "$slug"/exports/ 2>/dev/null | tr '\n' ' ')"
done
