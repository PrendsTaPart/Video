#!/usr/bin/env python3
"""Calcule le début de chaque paragraphe de la voix à partir de la transcription mot à mot.
Usage : python3 para-times.py <EP>  → écrit <EP>/paragraphes.json
tuto.json → "paragraphs": [{"key": "intro", "text": "..."}, ...]"""
import json
import os
import re
import sys
import unicodedata

EP = sys.argv[1]
cfg = json.load(open(os.path.join(EP, 'tuto.json')))
words = json.load(open(os.path.join(EP, cfg.get('transcript', 'audio/transcript.json'))))


def norm(s):
    s = unicodedata.normalize('NFKD', s.lower())
    s = ''.join(c for c in s if not unicodedata.combining(c))
    return re.sub(r'[^a-z0-9]', '', s)


tw = [norm(w['text']) for w in words]
out, pos = {}, 0
for p in cfg['paragraphs']:
    head = [norm(x) for x in re.split(r"[\s'’-]+", p['text']) if norm(x)][:3]
    best = None
    for i in range(pos, len(words)):
        # tolère les découpages différents (ex. « RapidoCRM » ↔ « Rapido CRM ») en comparant le début
        joined = ''.join(tw[i:i + 4])
        if joined.startswith(''.join(head)[:max(4, len(''.join(head[:2])))]):
            best = i
            break
    if best is None:
        sys.exit(f"Paragraphe introuvable dans la transcription : {p['key']} « {p['text'][:40]}… »")
    out[p['key']] = round(words[best]['start'], 2)
    pos = best + 1
out['end'] = round(words[-1]['end'], 2)
json.dump(out, open(os.path.join(EP, 'paragraphes.json'), 'w'), indent=1)
print(out)
