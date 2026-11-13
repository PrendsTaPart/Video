#!/usr/bin/env python3
"""Ajoute des épisodes importés dans RapidoCMS à publication.json, coche le PLAN et exporte l'Académie du site.
Usage : python3 _gabarit/enregistrer-publication.py CRM11 CRM12 ..."""
import json, os, re, subprocess, sys
G = os.path.dirname(os.path.abspath(__file__)); R = os.path.dirname(G)
S3 = 'https://rapido-software.s3.eu-west-3.amazonaws.com/rapidosoftware/cms/bibliotheque/tutoriel-rapido-'
pub = json.load(open(os.path.join(R, 'publication.json')))
for ep in sys.argv[1:]:
    cfg = json.load(open(os.path.join(R, ep, 'tuto.json')))
    v = os.path.join(R, '..', 'videos', 'tutoriels-rapido', '720p', ep + '.mp4')
    dur = float(subprocess.run(['ffprobe', '-v', 'error', '-show_entries', 'format=duration', '-of', 'csv=p=0', v], capture_output=True, text=True).stdout)
    e = {'id': ep, 'produit': cfg.get('product', 'crm'), 'kicker': cfg['kicker'], 'titre': cfg['title'], 'tag': cfg['tag'],
         'duree_s': round(dur), 'video': S3 + ep + '.mp4', 'miniature': S3 + ep + '.png'}
    pub = [x for x in pub if x['id'] != ep]
    pre = re.match(r'[A-Z]+', ep).group(0)
    idx = [k for k, x in enumerate(pub) if x['id'].startswith(pre) and x['id'] < ep]
    pub.insert(idx[-1] + 1 if idx else len(pub), e)
    plan = os.path.join(R, 'PLAN.md'); s = open(plan).read()
    open(plan, 'w').write(re.sub(r'- \[[ ~!]\] ' + ep + ' —', '- [x] ' + ep + ' —', s))
    print('publié :', ep, round(dur), 's')
json.dump(pub, open(os.path.join(R, 'publication.json'), 'w'), ensure_ascii=False, indent=2)
subprocess.run(['python3', os.path.join(G, 'export-site.py'), '/home/user/rapido-software/resources/data/academie.json'], check=True)
