#!/usr/bin/env python3
"""Calcule le début de chaque paragraphe de la voix à partir de la transcription mot à mot.
Alignement global du script et de la transcription (difflib), tolérant aux chiffres écrits en lettres,
aux mots collés (« RapidoCRM » / « Rapido CRM ») et aux petites erreurs de transcription.
Usage : python3 para-times.py <EP>  → écrit <EP>/paragraphes.json"""
import difflib
import json
import os
import re
import sys
import unicodedata

EP = sys.argv[1]
cfg = json.load(open(os.path.join(EP, 'tuto.json')))
words = json.load(open(os.path.join(EP, cfg.get('transcript', 'audio/transcript.json'))))
NUM = {'un': '1', 'une': '1', 'deux': '2', 'trois': '3', 'quatre': '4', 'cinq': '5', 'six': '6', 'sept': '7', 'huit': '8',
       'neuf': '9', 'dix': '10', 'douze': '12', 'quinze': '15', 'vingt': '20', 'trente': '30', 'premier': '1er'}


def norm(s):
    s = unicodedata.normalize('NFKD', s.lower())
    s = ''.join(c for c in s if not unicodedata.combining(c))
    s = re.sub(r'[^a-z0-9]', '', s)
    return NUM.get(s, s)


def toks(text):
    return [t for t in (norm(x) for x in re.split(r"[\s'’\-]+", text)) if t]


# transcription : un jeton par mot, avec son temps de début
tw, tt = [], []
for w in words:
    for t in toks(w['text']):
        tw.append(t)
        tt.append(w['start'])
# script : jetons + index du paragraphe de chaque jeton
sw, sp = [], []
for i, p in enumerate(cfg['paragraphs']):
    for t in toks(p['text']):
        sw.append(t)
        sp.append(i)

sm = difflib.SequenceMatcher(a=sw, b=tw, autojunk=False)
mapping = {}
for a, b, n in sm.get_matching_blocks():
    for k in range(n):
        mapping[a + k] = b + k

out, last = {}, 0.0
for i, p in enumerate(cfg['paragraphs']):
    idx = [k for k in range(len(sw)) if sp[k] == i]
    t = None
    for k in idx:  # premier jeton du paragraphe retrouvé dans la transcription
        if k in mapping:
            j = mapping[k] - (k - idx[0])           # recule du nombre de jetons non retrouvés en tête
            j = max(0, min(j, len(tt) - 1))
            t = tt[j]
            break
    if t is None or t < last:
        sys.exit(f"Paragraphe introuvable dans la transcription : {p['key']}")
    out[p['key']] = round(t, 2)
    last = t
out['end'] = round(words[-1]['end'], 2)
json.dump(out, open(os.path.join(EP, 'paragraphes.json'), 'w'), indent=1)
print(out)
