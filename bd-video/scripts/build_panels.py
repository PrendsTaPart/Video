#!/usr/bin/env python3
"""Range les images d'origine Figma (cache par sha1) dans bd-video/panels/.

    python3 bd-video/scripts/build_panels.py

Lit figma/extraction.json (imageHash de chaque nœud img:…) et figma/cache/<sha1>.<ext>
(rempli par fetch_figma_assets.sh). Écrit panels/pXX-cN.<ext> — c1/c2 pour les planches,
c1 seul pour les pages pleine image — et panels/index.json (nœud, nom Figma, taille).
L'extension d'origine est conservée (JPEG ou PNG) : pas de recompression.
"""
import json
import os
import re
import shutil
import subprocess

ROOT = os.path.join(subprocess.check_output(["git", "rev-parse", "--show-toplevel"], text=True).strip(), "bd-video")
pages = json.load(open(os.path.join(ROOT, "figma", "extraction.json")))
cache = {os.path.splitext(f)[0]: f for f in os.listdir(os.path.join(ROOT, "figma", "cache"))}
out = os.path.join(ROOT, "panels")
os.makedirs(out, exist_ok=True)


def size(path):
    r = subprocess.run(["ffprobe", "-v", "error", "-show_entries", "stream=width,height", "-of", "csv=p=0", path],
                       capture_output=True, text=True).stdout.strip().split(",")
    return int(r[0]), int(r[1])


index, missing, used = [], [], set()
for p in pages:
    num = int(re.match(r"Page (\d+)", p["n"]).group(1))
    # Dessins de la page : les nœuds img:… de grande taille (on écarte logos et vignettes).
    art = [im for im in p["imgs"] if im[2].startswith("img:") and im[4] >= 700]
    for case, node, name, h, w, hh in art:
        c = case or 1
        if h not in cache:
            missing.append((num, name, h))
            continue
        ext = os.path.splitext(cache[h])[1]
        dst = f"p{num:02d}-c{c}{ext}"
        shutil.copyfile(os.path.join(ROOT, "figma", "cache", cache[h]), os.path.join(out, dst))
        used.add(h)
        W, H = size(os.path.join(out, dst))
        index.append({"file": f"panels/{dst}", "page": num, "case": c, "figma_node": node, "figma_name": name,
                      "sha1": h, "source_px": [W, H], "cadre_figma_px": [w, hh]})

json.dump(index, open(os.path.join(out, "index.json"), "w"), ensure_ascii=False, indent=1)
print(f"{len(index)} dessins rangés dans panels/ ; manquants : {missing or 'aucun'}")
