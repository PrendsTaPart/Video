#!/usr/bin/env python3
"""Exporte les tutoriels publiés (publication.json) vers le site RapidoSoftware.
Ajoute à chaque épisode : description (1er paragraphe de la voix), chapitres, script complet (transcription lisible).
Usage : python3 _gabarit/export-site.py /home/user/rapido-software/resources/data/academie.json"""
import json
import os
import sys

ICI = os.path.dirname(os.path.abspath(__file__))
RACINE = os.path.dirname(ICI)
out = sys.argv[1]
pub = json.load(open(os.path.join(RACINE, 'publication.json')))
LIBELLE = {'crm': 'RapidoCRM', 'cms': 'RapidoCMS', 'rh': 'RapidoRH'}
episodes = []
for e in pub:
    if not e.get('video'):
        continue
    c = json.load(open(os.path.join(RACINE, e['id'], 'tuto.json')))
    paras = [p['text'] for p in c.get('paragraphs', []) if p['key'] != 'outro']
    chap = [ch['label'] for ch in c.get('chapters', []) if ch.get('label')] or [s['label'] for s in c.get('scenes', []) if s.get('label')] or [s.get('title', '') for s in c.get('slides', [])[1:]]
    formation = e['id'].startswith('F') or 'slides' in c
    episodes.append({
        'id': e['id'],
        'slug': e['id'].lower(),
        'categorie': 'formation' if e['id'].startswith('F') else e['produit'],
        'produit': LIBELLE.get(e['produit'], 'Rapido'),
        'format': 'Formation' if e['id'].startswith('F') else 'Tutoriel',
        'titre': e['titre'],
        'accent': c.get('em', ''),
        'tag': e.get('tag', ''),
        'duree': f"{e['duree_s'] // 60}:{e['duree_s'] % 60:02d}" if e.get('duree_s') else '',
        'video': e['video'],
        'miniature': e['miniature'],
        'description': paras[0] if paras else '',
        'chapitres': [x for x in chap if x],
        'script': paras,
        'motion': formation,
    })
os.makedirs(os.path.dirname(out), exist_ok=True)
json.dump({'genere_le': __import__('datetime').date.today().isoformat(), 'episodes': episodes}, open(out, 'w'), ensure_ascii=False, indent=1)
print(f'{len(episodes)} épisodes exportés → {out}')
