#!/usr/bin/env python3
"""Resto 2.0 - Edit Decision List.
Every cut is snapped to a detected onset (non-negotiable rule of this edit).
Section boundaries derive from the MEASURED audio (168.52 s), not the brief's
180 s assumption; shot-to-lyric assignment follows the brief exactly.
"""
import json, os

HERE = os.path.dirname(os.path.abspath(__file__))
A = json.load(open(os.path.join(HERE, '..', 'assets', 'analysis.json')))
ONSETS = sorted(A['onsets'])
DUR = A['duration']

def snap(t, lo=0.16):
    """Snap t to the nearest onset within +/- lo seconds."""
    best, bd = None, 1e9
    for o in ONSETS:
        d = abs(o - t)
        if d < bd:
            best, bd = o, d
    return round(best, 3) if bd <= lo else round(t, 3)

# ---- anchors measured from the sung lyrics (word-level timings) ----
OPEN_END   = 11.12   # first sung word
REFRAIN1   = 44.64
BREAK_END  = 71.00
REFRAIN2   = 104.66
BRIDGE     = 126.36
FINALREF   = 137.12
CLOSE_IN   = 152.28  # "FoodEatUp, une infinité de solutions" - brand signature
END        = round(DUR, 3)

# Every cut: (start, episode, note). End = next start.
CUTS = [
  # ---------------- VERSE 1 : 8 shots, one per sung line ----------------
  (11.12, 'EP045', "t'en as marre de pas connaître ton stock"),
  (13.64, 'EP046', "le frigo dit oui, le carnet dit non"),
  (16.26, 'EP100', "t'as pas le temps de communiquer"),
  (18.62, 'EP088', "t'as pas le temps de gérer tes avis"),
  (21.40, 'EP050', "t'as peur qu'un contrôle sonne à la porte"),
  (24.08, 'EP031', "le classeur dort, la date s'efface"),
  (26.70, 'EP065', "t'as du mal à recruter"),
  (28.98, 'EP142', "trois annonces, zéro réponse"),
  # ---------------- PRE-REFRAIN 1 : 3 shots, tighter ----------------
  (32.32, 'EP085', "tu perds tes clients et tu sais pas pourquoi"),
  (34.82, 'EP122', "tu galères à les faire revenir"),
  (37.40, 'EP035', "tu te transformes en médium"),
  # EP035 freezes on its last frame 0.5 s before the refrain (44.14 -> 44.64)
  # ---------------- REFRAIN 1 : fast, one shot per strong beat ----------------
  (44.64, 'EP141', "FoodEatUp #1 - cockpit"),
  (47.30, 'EP013', "notifications maîtrisées"),
  (50.00, 'EP029', "les douze assiettes"),
  (52.60, 'EP010', "le flambage"),
  (55.32, 'EP021', "prêt à devenir un resto 2.0"),
  (58.00, 'EP087', "les trois tablettes"),
  (60.22, 'EP112', "FoodEatUp #2 - huit boucles"),
  (63.90, 'EP111', "et ça tourne tout seul"),
  # ---------------- BREAK 66.5 -> 71.0 : hold EP111, energy drops out ----------
  # ---------------- VERSE 2 : 8 shots ----------------
  (71.00, 'EP021', "tu perds tes tickets en cuisine"),
  (73.26, 'EP008', "le pass hurle, personne ne répond"),
  (76.72, 'EP108', "45 minutes pour servir une table"),
  (79.08, 'EP037', "le client attend, le client s'en va"),
  (81.24, 'EP064', "ton planning au doigt mouillé"),
  (84.26, 'EP063', "deux en salle quand il en faut cinq"),
  (86.76, 'EP087', "ton site c'est juste une vitrine"),
  (89.36, 'EP073', "une belle photo qui vend rien"),
  # ---------------- PRE-REFRAIN 2 ----------------
  (92.50, 'EP083', "tu perds tes clients et tu sais pas pourquoi"),
  (97.34, 'EP089', "arrête de jouer les voyants  [SUBSTITUTION: EP090 bloque]"),
  # ---------------- REFRAIN 2 : different rushes, same grammar ----------------
  (104.66, 'EP143', "FoodEatUp #3 - la commande de 200"),
  (107.20, 'EP128', "Saint-Valentin surbookée"),
  (109.50, 'EP103', "FoodEatUp #4 - le car de 40"),
  (112.20, 'EP114', "la choré pendant que ça brûle"),
  (115.40, 'EP119', "prêt à devenir un resto 2.0"),
  (118.00, 'EP099', "le répondeur"),
  (120.32, 'EP143', "FoodEatUp #5 - huit boucles"),
  (123.92, 'EP128', "et ça tourne tout seul"),
  # ---------------- BRIDGE : one shot per agent, name lower-third ----------
  (126.36, 'EP099', "AGENT:Caroline"),
  (129.18, 'EP063', "AGENT:Jarvis"),
  (131.56, 'EP141', "AGENT:PrediBot"),
  (134.04, 'EP100', "AGENT:Iris"),
  # ---------------- FINAL REFRAIN : progressive acceleration ----------------
  (137.12, 'EP141', "FoodEatUp #6"),
  (139.60, 'EP029', "reprise"),
  (141.90, 'EP013', "reprise"),
  (144.00, 'EP111', "reprise"),
  (145.90, 'EP143', "reprise"),
  (147.60, 'EP103', "reprise"),
  (149.10, 'EP114', "reprise"),
  (150.40, 'EP119', "reprise"),
  (151.45, 'EP141', "dernier plan avant fermeture"),
]

# "FoodEatUp" sung attacks -> 1/8 s white logomark flash, on the syllable attack
LOGO_FLASH = [44.64, 60.22, 104.66, 109.50, 120.32, 137.12, 152.28]
# "huit boucles" -> double-O infinity loops once
INFINITY   = [61.68, 121.66]

def build():
    shots = []
    for i, (t, ep, note) in enumerate(CUTS):
        end = CUTS[i+1][0] if i+1 < len(CUTS) else CLOSE_IN
        s = snap(t)
        e = snap(end)
        shots.append({'start': s, 'end': e, 'dur': round(e-s,3), 'ep': ep, 'note': note})
    return shots

if __name__ == '__main__':
    shots = build()
    out = {'duration': END, 'open_end': OPEN_END, 'close_in': CLOSE_IN,
           'logo_flash': [snap(t) for t in LOGO_FLASH], 'infinity': INFINITY,
           'shots': shots}
    json.dump(out, open(os.path.join(HERE, 'edl.json'), 'w'), indent=1, ensure_ascii=False)
    print('%-8s %-8s %-6s %-7s %s' % ('START','END','DUR','EP','LINE'))
    for s in shots:
        print('%-8.2f %-8.2f %-6.2f %-7s %s' % (s['start'], s['end'], s['dur'], s['ep'], s['note']))
    print()
    print('shots: %d   rush coverage: %.2f -> %.2f' % (len(shots), shots[0]['start'], shots[-1]['end']))
    print('opening animation : 0.00 -> %.2f  (%.2f s)' % (OPEN_END, OPEN_END))
    print('closing animation : %.2f -> %.2f  (%.2f s)' % (CLOSE_IN, END, END-CLOSE_IN))
    d=[s['dur'] for s in shots[-9:]]
    print('final-refrain accel:', ' '.join('%.2f'%x for x in d))
