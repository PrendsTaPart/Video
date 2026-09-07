"""Série « 30 problèmes, 30 solutions » + 6 clips musicaux — 100 % plans Higgsfield.

Chaque vidéo : animation d'accroche → 2 plans « problème » → 2 plans « solution »
→ plan signature → carton final → sting animé. Une seule ligne de voix off nouvelle
par vidéo (Sxx), puis la signature commune C3 et l'appel C4.

Les six clips musicaux n'ont pas de voix : huit plans montés sur une musique originale,
carton de titre, carton final, mêmes animations d'accroche et de fin.

    python3 serie30.py             # les 30 vidéos et les 6 clips
    python3 serie30.py 01 07       # quelques vidéos
    python3 serie30.py clips       # les 6 clips seulement
"""
import sys

from build import (BLUE, INK, ORANGE, WHITE, anim, build_film, card, duration, end_card, hf,
                   logo_corner, to_16x9, vo)

MUSIC_A = "assets/music/musique-underscore-99bpm.mp3"
MUSIC_B = "assets/music/musique-underscore-99bpm-alt.mp3"
TAGLINE = ["Une infinité de solutions", "pour gérer votre restaurant"]
W, H = 1080, 1920

# code VO, nom de fichier : (titre du carton, [deux puces solution], plans problème, plans solution)
SERIE = {
    "01": ("S01", "reservations", "Le carnet du matin", ["PLAN DE SALLE À JOUR", "SUR TOUS LES ÉCRANS"], [52, 53], [37, 38]),
    "02": ("S02", "double-reservation", "Deux clients, une table", ["TABLE BLOQUÉE À LA RÉSERVATION", "PLUS DE DOUBLON"], [88, 89], [220, 222]),
    "03": ("S03", "appels-manques", "Onze appels manqués", ["CAROLINE DÉCROCHE", "LA RÉSERVATION EST PRISE"], [168, 186], [223, 229]),
    "04": ("S04", "caisse-addition", "Une table de douze", ["ADDITION PARTAGÉE", "EN TROIS SECONDES"], [27, 46], [30, 369]),
    "05": ("S05", "ticket-z", "Le ticket Z", ["CAISSE COMPTÉE EN UN GESTE", "ÉCART EXPLIQUÉ ET ARCHIVÉ"], [47, 58], [466, 467]),
    "06": ("S06", "factures", "La boîte à chaussures", ["FACTURE PHOTOGRAPHIÉE", "PRIX MIS À JOUR PAR L'IA"], [56, 57], [322, 216]),
    "07": ("S07", "food-cost", "Deux euros par assiette", ["FICHE TECHNIQUE CHIFFRÉE", "COÛT CONNU AVANT LE SERVICE"], [44, 45], [145, 183]),
    "08": ("S08", "rupture-stock", "La rupture du samedi", ["CHAQUE VENTE DÉSTOCKE", "PREDIBOT COMMANDE À TEMPS"], [31, 32], [142, 162]),
    "09": ("S09", "inventaire", "Trois comptages", ["STOCK TEMPS RÉEL", "PERSONNE NE RECOMPTE"], [68, 69], [398, 418]),
    "10": ("S10", "commande-fournisseur", "Dix palettes d'oignons", ["COMMANDE SUR BESOIN RÉEL", "PLUS DE MÉMOIRE APPROXIMATIVE"], [77, 79], [276, 302]),
    "11": ("S11", "reception", "La réception dans le froid", ["LOT, DLC, TEMPÉRATURE SCANNÉS", "TRACÉ AVANT DE POSER LA CAISSE"], [84, 85], [361, 455]),
    "12": ("S12", "dlc", "La date du bac", ["ÉTIQUETTE HORODATÉE", "ALERTE AVANT LA DATE"], [193, 194], [308, 380]),
    "13": ("S13", "temperatures", "Le post-it des températures", ["RELEVÉS HORODATÉS", "EXPORT EN UN CLIC"], [143, 160], [456, 478]),
    "14": ("S14", "controle-sanitaire", "Mardi, onze heures", ["CLASSEUR HACCP PRÊT", "ET COMPLET"], [170, 175], [479, 480]),
    "15": ("S15", "tracabilite", "Remonter un lot", ["UNE RECHERCHE", "UN EXPORT"], [177, 321], [481, 482]),
    "16": ("S16", "nettoyage", "Qui a nettoyé la hotte ?", ["PLAN DE NETTOYAGE SIGNÉ", "CONTRÔLÉ PAR PHOTO"], [35, 36], [303, 436]),
    "17": ("S17", "allergenes", "L'allergie oubliée", ["ALLERGÈNE SUR LA FICHE", "IL SUIT LA COMMANDE"], [75, 76], [74, 185]),
    "18": ("S18", "planning", "Trois congés le même samedi", ["PLANNING SUR L'ACTIVITÉ RÉELLE", "PAR POSTE ET PAR SERVICE"], [33, 34], [66, 213]),
    "19": ("S19", "pointage", "Le cahier de pointage", ["BADGE AU QR CODE", "HEURES JUSTES"], [67, 144], [384, 172]),
    "20": ("S20", "recrutement", "La pile de CV", ["OFFRE ET CANDIDATURES", "ONBOARDING AU MÊME ENDROIT"], [26, 64], [352, 65]),
    "21": ("S21", "cuisine-kds", "Le ruban de tickets", ["ÉCRAN CUISINE", "CHAQUE PLAT AU BON POSTE"], [70, 71], [23, 301]),
    "22": ("S22", "prise-commande", "La commande sur une serviette", ["COMMANDE AU QR DE TABLE", "LA CUISINE REÇOIT TOUT DE SUITE"], [39, 40], [24, 146]),
    "23": ("S23", "avis", "Une étoile le soir", ["AVIS CENTRALISÉS", "RÉPONSE PRÊTE"], [72, 73], [86, 192]),
    "24": ("S24", "fichier-client", "« Comme d'habitude »", ["FICHE CLIENT COMPLÈTE", "ELLE SE SOUVIENT POUR VOUS"], [41, 42], [318, 43]),
    "25": ("S25", "campagne", "La promo envoyée à la ville", ["BON SEGMENT", "BON MOMENT"], [48, 49], [63, 259]),
    "26": ("S26", "gaspillage", "Douze kilos qui périment", ["IRIS EN FAIT LE PLAT DU JOUR", "PUBLIÉ À TREIZE HEURES"], [178, 179], [181, 396]),
    "27": ("S27", "livraison", "La pizza froide", ["LIVRAISON SUIVIE", "CLIENT PRÉVENU"], [51, 150], [50, 520]),
    "28": ("S28", "plateformes", "Trente pour cent", ["VOTRE SITE DE COMMANDE", "SANS COMMISSION"], [141, 452], [326, 355]),
    "29": ("S29", "terrasse", "Quarante clients trempés", ["SALLE, TERRASSE, ATTENTE", "SUR LE MÊME ÉCRAN"], [60, 61], [296, 316]),
    "30": ("S30", "pilotage", "Sept onglets ouverts", ["UN SEUL ÉCRAN", "DES AGENTS QUI TRAVAILLENT"], [25, 184], [297, 306]),
}

# clips musicaux : (titre, sous-titre, musique, huit plans)
CLIPS = {
    "rush": ("Le rush", "19 h 42", "assets/music/clip1-rush-128bpm.mp3",
             [20, 71, 194, 229, 250, 284, 332, 369]),
    "aube": ("L'aube", "06 h 15", "assets/music/clip2-aube-76bpm.mp3",
             [54, 83, 197, 224, 236, 245, 256, 387]),
    "brigade": ("La brigade", "12 h 00", "assets/music/clip3-brigade-108bpm.mp3",
                [19, 163, 263, 277, 296, 328, 348, 380]),
    "infini": ("L'infini", "sans fin", "assets/music/clip4-infini-118bpm.mp3",
               [23, 66, 154, 189, 211, 242, 295, 310]),
    "fermeture": ("La fermeture", "00 h 30", "assets/music/clip5-fermeture-88bpm.mp3",
                  [36, 80, 178, 192, 231, 294, 322, 430]),
    "comedie": ("La comédie", "tous les jours", "assets/music/clip6-comedie-132bpm.mp3",
                [33, 151, 208, 232, 275, 319, 362, 392]),
}

SIGNATURE = (28, 3.6)      # plan de signature commun (voix C3)
FINAL = (19, 8.0)          # plan sous le carton final (voix C4)


def seg(i, dur, start=2.5, **kw):
    """Un plan Higgsfield, avec un point d'entrée ramené dans la source si elle est courte."""
    src = hf(i)
    start = max(0.0, min(start, duration(src) - dur - 0.15))
    return dict(src=src, start=round(start, 2), dur=round(dur, 3), **kw)


def video(num):
    code, nom, titre, puces, probs, sols = SERIE[num]
    slug = f"foodeatup-s{num}-{nom}"
    va, dc3, dc4 = duration(vo(code)), duration(vo("C3")), duration(vo("C4"))
    a = (va * 0.45 + 0.7) / 2          # deux plans pour la moitié « problème »
    b = (va * 0.55 + 0.7) / 2          # deux plans pour la moitié « solution »
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

    music = MUSIC_A if int(num) % 2 else MUSIC_B
    audio = dict(music=music, music_start=6.0 + int(num) * 2.0, music_gain=-12.5, music_fade_out=1.8,
                 src_gain=-17.0, duck=0.32,
                 vo=[(vo(code), 0.3), (vo("C3"), t[4] + 0.25), (vo("C4"), acc + 0.5)])
    out = build_film(slug, W, H, segs, overlays, audio,
                     hook=anim("hook-logo"), sting=anim("sting-logo"))
    to_16x9(out, slug)


def clip(name):
    titre, sous, music, plans = CLIPS[name]
    slug = f"foodeatup-clip-{name}"
    dc4 = duration(vo("C4"))
    per, end_d = 3.4, dc4 + 2.2
    segs = [seg(i, per, 2.0 + 0.4 * k) for k, i in enumerate(plans)]
    t, acc = [], 0.0
    for s in segs:
        t.append(acc)
        acc += s["dur"]
    segs.append(seg(FINAL[0], end_d, FINAL[1]))

    def overlays(W, H, times, total):
        ov = [dict(png=card(f"{slug}-t", W, 420, titre, size=118, color=WHITE, pill=(*INK, 205), y=40,
                            sub=sous, sub_size=54),
                   t0=times[0] + 0.4, t1=times[1] + 1.2, fin=0.3, fout=0.4, y=H - 780, slide="up")]
        ov.append(dict(png=card(f"{slug}-s", W, 260, "FOODEATUP", size=88, color=WHITE,
                                pill=(*BLUE, 235), y=50),
                       t0=times[6], t1=total - end_d, fin=0.3, fout=0.3, y=H - 660, slide="up"))
        ov.append(dict(png=logo_corner(f"{slug}-logo", W, H, scale=0.28, margin=46),
                       t0=times[2], t1=times[6], fin=0.3, fout=0.2))
        ov.append(dict(png=end_card(f"{slug}-end", W, H, TAGLINE), t0=total - end_d, t1=total + 1,
                       fin=0.5, fout=0.0))
        return ov

    audio = dict(music=music, music_start=0.0, music_gain=-8.0, music_fade_out=2.5,
                 src_gain=-24.0, duck=0.5, vo=[(vo("C4"), acc + 0.8)])
    out = build_film(slug, W, H, segs, overlays, audio,
                     hook=anim("hook-logo"), sting=anim("sting-infini-3d"))
    to_16x9(out, slug)


if __name__ == "__main__":
    args = sys.argv[1:]
    if not args:
        args = list(SERIE) + list(CLIPS)
    elif args == ["clips"]:
        args = list(CLIPS)
    elif args == ["videos"]:
        args = list(SERIE)
    for a in args:
        (video if a in SERIE else clip)(a)
