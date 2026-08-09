#!/usr/bin/env python3
"""Download clips that exist on RapidoCMS into clips/, matched by exact
name against manifest.json. Never generates anything — only pulls files
that are already in the RapidoCMS library.

Usage: fetch_clips.py rapidocms_dump.json
  (dump = JSON returned by mcp__RapidoCMS__list_all_files, saved to a file)
"""
import json, os, sys, urllib.request
from common import CLIPS
from inventory import expected_names


def main():
    if len(sys.argv) != 2:
        raise SystemExit("Usage: fetch_clips.py rapidocms_dump.json")
    with open(sys.argv[1]) as f:
        dump = json.load(f)

    by_name = {}
    for item in dump.get("files", []):
        by_name[item.get("nom") or item.get("file")] = item.get("file_url")

    names = expected_names()
    fetched, skipped = [], []
    for n in names:
        dest = f"{CLIPS}/{n}.mp4"
        if os.path.exists(dest):
            skipped.append((n, "déjà en local"))
            continue
        url = by_name.get(n)
        if not url:
            skipped.append((n, "absent de RapidoCMS"))
            continue
        print(f"téléchargement {n} ...")
        urllib.request.urlretrieve(url, dest)
        fetched.append(n)

    print(f"\n{len(fetched)} clip(s) téléchargé(s):")
    for n in fetched:
        print(f"   {n}")
    print(f"\n{len(skipped)} ignoré(s):")
    for n, why in skipped:
        print(f"   {n} — {why}")


if __name__ == "__main__":
    main()
