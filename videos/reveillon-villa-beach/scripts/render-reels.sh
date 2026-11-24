#!/usr/bin/env bash
# Rend les Reels/TikTok (data/reels). Voir scripts/render-set.sh.
DIR=reels exec bash "$(dirname "$0")/render-set.sh" "$@"
