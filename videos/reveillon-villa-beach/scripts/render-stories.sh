#!/usr/bin/env bash
# Rend les stories Instagram (data/stories). Voir scripts/render-set.sh.
DIR=stories exec bash "$(dirname "$0")/render-set.sh" "$@"
