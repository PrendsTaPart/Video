"""Fusion de l'Académie : part de HEAD, n'ajoute que les épisodes demandés, depuis l'export frais.
Usage : python3 fusion-academie.py <repo rapido-software> EP1 EP2 …
"""
import json
import re
import subprocess
import sys

repo, ids = sys.argv[1], sys.argv[2:]
chemin = f'{repo}/resources/data/academie.json'
head = json.loads(subprocess.check_output(['git', '-C', repo, 'show', 'HEAD:resources/data/academie.json']))
frais = {e['id']: e for e in json.load(open(chemin))['episodes']}
eps = head['episodes']
deja = {e['id'] for e in eps}
manquants = [i for i in ids if i not in frais]
if manquants:
    sys.exit(f'absents de l\'export : {manquants}')


def num(i):
    return int(re.sub(r'\D', '', i) or 0)


for i in ids:
    if i in deja:
        continue
    prefixe = re.match(r'[A-Z]+', i).group(0)
    meme = [k for k, e in enumerate(eps) if re.match(r'[A-Z]+', e['id']).group(0) == prefixe and not e['id'].startswith('RHV2')]
    if prefixe == 'F':
        # à sa place numérique parmi les formations
        apres = [k for k in meme if num(eps[k]['id']) < num(i)]
        pos = (apres[-1] + 1) if apres else (meme[0] if meme else len(eps))
    else:
        pos = (meme[-1] + 1) if meme else len(eps)
    eps.insert(pos, frais[i])
    deja.add(i)

head['episodes'] = eps
head['genere_le'] = json.load(open(chemin))['genere_le']
json.dump(head, open(chemin, 'w'), ensure_ascii=False, indent=1)
print(len(eps), [e['id'] for e in eps if e['id'] in ids])
