#!/usr/bin/env bash
# Télécharge les URLs temporaires renvoyées par l'outil Figma download_assets.
# Entrée (stdin), une ligne par fichier :
#   page <NN> <url>   → export de la page entière  → bd-video/pages/pNN.png
#   raw  <url>        → image d'origine            → bd-video/figma/cache/<sha1>.<ext>
# Le sha1 du fichier est l'imageHash Figma : c'est lui qui relie l'image à son nœud img:… (voir build_storyboard.py).
set -euo pipefail
ROOT="$(git rev-parse --show-toplevel)/bd-video"
mkdir -p "$ROOT/pages" "$ROOT/figma/cache"
TMP="$(mktemp -d)"
while read -r kind a b; do
  [ -z "${kind:-}" ] && continue
  if [ "$kind" = page ]; then
    curl -sSfL -o "$ROOT/pages/p$a.png" "$b" && echo "page p$a"
  else
    f="$TMP/x"; curl -sSfL -o "$f" "$a"
    h=$(sha1sum "$f" | cut -d' ' -f1)
    case "$(file -b --mime-type "$f")" in image/jpeg) e=jpg;; image/png) e=png;; image/webp) e=webp;; image/gif) e=gif;; *) e=bin;; esac
    mv "$f" "$ROOT/figma/cache/$h.$e"
  fi
done
rm -rf "$TMP"
echo "cache : $(ls "$ROOT/figma/cache" | wc -l) images"
