#!/usr/bin/env python3
"""État des lieux des 19 clips attendus.

Usage:
  inventory.py                       # vérifie seulement clips/ en local
  inventory.py rapidocms_dump.json   # + croise avec un export RapidoCMS
                                      # (JSON renvoyé par list_all_files,
                                      # {"files": [{"nom": ..., "file_url": ...}, ...]})
"""
import json, os, sys
from common import MANIFEST, CLIPS, clip_path

def expected_names():
    names = []
    for s in MANIFEST["stories"]:
        if s.get("split", True) and "clip_sans" in s:
            names.append(s["clip_sans"])
            names.append(s["clip_avec"])
        elif "clip_full" in s:
            names.append(s["clip_full"])
    return names


def main():
    names = expected_names()
    remote = {}
    if len(sys.argv) > 1:
        with open(sys.argv[1]) as f:
            dump = json.load(f)
        for item in dump.get("files", []):
            remote[item.get("nom") or item.get("file")] = item.get("file_url")

    present, missing_local_only, missing_everywhere = [], [], []
    for n in names:
        local = clip_path(n)
        if local:
            present.append((n, local))
        elif n in remote:
            missing_local_only.append((n, remote[n]))
        else:
            missing_everywhere.append(n)

    print(f"=== État des lieux — {len(names)} clips attendus ===\n")
    print(f"✅ Présents en local ({len(present)}):")
    for n, p in present:
        print(f"   {n}  ->  {p}")
    if remote:
        print(f"\n☁️  Sur RapidoCMS mais pas encore téléchargés ({len(missing_local_only)}):")
        for n, url in missing_local_only:
            print(f"   {n}  ->  {url}")
    print(f"\n❌ Introuvables (ni local, ni RapidoCMS) ({len(missing_everywhere)}):")
    for n in missing_everywhere:
        print(f"   {n}")

    ready = []
    for s in MANIFEST["stories"]:
        if "clip_full" in s:
            ok = clip_path(s["clip_full"]) is not None
        else:
            ok = clip_path(s["clip_sans"]) is not None and clip_path(s["clip_avec"]) is not None
        ready.append((s["id"], ok))
    print(f"\n=== Stories montables dès maintenant ===")
    for sid, ok in ready:
        print(f"   {sid}: {'OK — les deux volets sont là' if ok else 'en attente'}")


if __name__ == "__main__":
    main()
