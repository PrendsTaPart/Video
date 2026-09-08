"""Seconde vague : 50 vidéos thématiques FoodEatUp — 100 % plans Higgsfield.

Même forme que `serie30.py` : animation d'accroche → deux plans « problème » →
deux plans « solution » → plan signature → carton final → sting animé.
Les plans sont choisis dans `assets/higgsfield-tags.json`, en écartant tous ceux
déjà employés par la série de 30, pour qu'aucune image ne se répète.

    python3 serie50.py             # les 50
    python3 serie50.py T01 T07     # quelques-unes
"""
import json
import re
import sys

from build import (BLUE, INK, ROOT, WHITE, anim, build_film, card, duration, end_card,
                   logo_corner, to_16x9, vo)
from serie30 import FINAL, MUSIC_A, MUSIC_B, SERIE, SIGNATURE, TAGLINE, seg

sys.path.insert(0, str(ROOT / "scripts"))
from serie50_data import LIGNES  # noqa: E402

W, H = 1080, 1920

# thème -> familles de plans dans lesquelles piocher (champ `probleme_resto` du tag)
FAMILLES = {
    "no-show": ["réservations"], "liste-attente": ["file d'attente", "réservations"],
    "rotation-table": ["terrasse météo / placement", "réservations"],
    "acompte": ["réservations"], "evenement-prive": ["devis groupe", "réservations"],
    "devis-groupe": ["devis groupe", "caisse/compta"],
    "terminal-paiement": ["caisse/compta"], "pourboire": ["caisse/compta"],
    "tva": ["caisse/compta"], "marge": ["food cost / fiche technique"],
    "ticket-moyen": ["caisse/compta"], "depenses": ["facture"],
    "prix-fournisseur": ["facture", "commande fournisseur"],
    "comparaison-fournisseur": ["commande fournisseur"],
    "casse": ["gaspillage"], "inventaire-tournant": ["inventaire stock"],
    "recette": ["food cost / fiche technique"], "production": ["planning production"],
    "unites": ["inventaire stock"], "cave": ["inventaire stock"],
    "happy-hour": ["happy hour / marketing"], "fidelite": ["fichier client"],
    "carte-cadeau": ["caisse/compta"], "jeu-concours": ["campagne marketing"],
    "sondage": ["avis client"], "rfm": ["fichier client"],
    "newsletter": ["campagne marketing"], "whatsapp": ["campagne marketing"],
    "site-web": ["dépendance plateformes"], "click-collect": ["dépendance plateformes"],
    "menu-qr": ["prise de commande"], "photo-plat": ["campagne marketing"],
    "rupture-carte": ["rupture de stock"], "allergene-gluten": ["allergènes"],
    "ddpp": ["HACCP températures"], "huile": ["nettoyage"],
    "chambre-froide": ["HACCP températures"], "reception-non-conforme": ["commande fournisseur"],
    "contrat": ["recrutement"], "documents-employe": ["recrutement"],
    "conges": ["planning équipe"], "heures-supplementaires": ["planning équipe"],
    "onboarding": ["recrutement"], "formation-haccp": ["nettoyage", "HACCP températures"],
    "caroline": ["réservations"], "jarvis": ["commandes en cuisine (KDS)"],
    "predibot": ["pilotage global (agents IA)"], "iris": ["campagne marketing"],
    "multi-etablissement": ["pilotage global (agents IA)"],
    "une-app": ["pilotage global (agents IA)"],
}

TAGS = json.loads((ROOT / "assets" / "higgsfield-tags.json").read_text())
SOLUTION = re.compile(r"tablette|écran|smartphone|téléphone|QR|voyant vert|APRÈS|sourit|serein", re.I)


def _texte(x):
    return " ".join(str(x.get(k) or "") for k in ("action", "note_montage", "gag", "lieu"))


def _deja_pris():
    """Les plans déjà employés par la série de 30, plus signature et carton final."""
    pris = {SIGNATURE[0], FINAL[0]}
    for v in SERIE.values():
        pris.update(v[4])
        pris.update(v[5])
    return pris


def choix():
    """Quatre plans par thème : deux pour le problème, deux pour la solution."""
    pris = _deja_pris()
    plans = {}

    def prendre(lst, n):
        out = []
        for x in lst:
            if x["i"] in pris:
                continue
            out.append(x["i"])
            pris.add(x["i"])
            if len(out) == n:
                break
        return out

    for code, nom, _titre, _puces, _ligne in LIGNES:
        familles = FAMILLES.get(nom, [])
        pool = [x for x in TAGS if x["probleme_resto"] in familles]
        sol_pool = [x for x in pool if SOLUTION.search(_texte(x))]
        prob_pool = [x for x in pool if x not in sol_pool]
        reste = [x for x in TAGS if x["probleme_resto"]]
        sol_global = [x for x in TAGS if SOLUTION.search(_texte(x))]

        p = prendre(prob_pool, 2)
        if len(p) < 2:
            p += prendre(pool, 2 - len(p))
        if len(p) < 2:
            p += prendre(reste, 2 - len(p))
        s = prendre(sol_pool, 2)
        if len(s) < 2:
            s += prendre(sol_global, 2 - len(s))
        if len(s) < 2:
            s += prendre(reste, 2 - len(s))
        plans[code] = (p, s)
    return plans


PLANS = choix()
INDEX = {code: (nom, titre, puces, ligne) for code, nom, titre, puces, ligne in LIGNES}


def video(code):
    nom, titre, puces, _ligne = INDEX[code]
    probs, sols = PLANS[code]
    slug = f"foodeatup-{code.lower()}-{nom}"
    va, dc3, dc4 = duration(vo(code)), duration(vo("C3")), duration(vo("C4"))
    a = (va * 0.45 + 0.7) / 2
    b = (va * 0.55 + 0.7) / 2
    sig, end_d = dc3 + 0.8, dc4 + 1.6
    segs = ([seg(i, a) for i in probs] + [seg(i, b) for i in sols]
            + [seg(SIGNATURE[0], sig, SIGNATURE[1])])
    t, acc = [], 0.0
    for s in segs:
        t.append(acc)
        acc += s["dur"]
    segs.append(seg(FINAL[0], end_d, FINAL[1]))

    def overlays(W, H, times, total):
        ov = [dict(png=card(f"{slug}-t", W, 300, titre, size=98, color=WHITE, pill=(*INK, 205), y=40),
                   t0=times[0] + 0.35, t1=times[2] - 0.15, fin=0.2, fout=0.25, y=H - 700, slide="up")]
        for k, txt in enumerate(puces):
            ov.append(dict(png=card(f"{slug}-p{k}", W, 260, txt, size=70, color=WHITE, pill=(*BLUE, 235), y=50),
                           t0=times[2 + k] + 0.15, t1=times[2 + k] + segs[2 + k]["dur"] - 0.1,
                           fin=0.15, fout=0.2, y=H - 660, slide="up"))
        ov.append(dict(png=logo_corner(f"{slug}-logo", W, H, scale=0.28, margin=46),
                       t0=times[4], t1=total - end_d, fin=0.3, fout=0.2))
        ov.append(dict(png=end_card(f"{slug}-end", W, H, TAGLINE), t0=total - end_d, t1=total + 1,
                       fin=0.5, fout=0.0))
        return ov

    n = int(code[1:])
    audio = dict(music=MUSIC_A if n % 2 else MUSIC_B, music_start=4.0 + n * 1.7,
                 music_gain=-12.5, music_fade_out=1.8, src_gain=-17.0, duck=0.32,
                 vo=[(vo(code), 0.3), (vo("C3"), t[4] + 0.25), (vo("C4"), acc + 0.5)])
    out = build_film(slug, W, H, segs, overlays, audio,
                     hook=anim("hook-logo"), sting=anim("sting-logo"))
    to_16x9(out, slug)


if __name__ == "__main__":
    for c in (sys.argv[1:] or list(INDEX)):
        video(c)
