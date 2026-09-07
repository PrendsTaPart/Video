"""Les quatre montages FoodEatUp. Chaque fonction = un film (voir scripts/VOIX-OFF.md)."""
from build import (BLUE, CREAM, INK, ORANGE, WHITE, OUT, REPO, build_film, card, end_card, hf, logo_corner,
                   mix_audio, to_16x9, vo)

MUSIC_CLIP = "assets/music/musique-clip-123bpm.mp3"
MUSIC_UNDER = "assets/music/musique-underscore-99bpm.mp3"
MUSIC_UNDER_ALT = "assets/music/musique-underscore-99bpm-alt.mp3"
TAGLINE = ["Une infinité de solutions", "pour gérer votre restaurant"]
# Règle de la session : uniquement des plans de la bibliothèque Higgsfield.
# Aucun screencast, aucun plan hero-video, aucun avatar HeyGen.


def S(src, start, dur, **kw):
    d = dict(src=src, start=start, dur=dur)
    d.update(kw)
    return d


# ------------------------------------------------------------------ 1. CLIP

def clip():
    """« Une journée. Une app. » — 62 s, 9:16, monté sur la musique originale (123 BPM)."""
    W, H = 1080, 1920
    B2, B4 = 0.976, 1.951  # 2 et 4 temps à 123 BPM
    segs = [
        S(hf(149), 0.0, 2.0),          # flambée plein cadre : le hook
        S(hf(23), 2.0, B4),            # rush cuisine, Michael immobile au centre
        S(hf(24), 2.5, B4),            # cloche : la pile de tickets papier
        S(hf(71), 5.5, B4),            # rafale de tickets
        S(hf(38), 5.5, B4),            # trois téléphones
        S(hf(37), 5.5, B4),            # répondre à une spatule
        S(hf(69), 5.5, B4),            # inventaire douze, onze, quinze
        S(hf(79), 2.5, B4),            # dix palettes d'oignons
        S(hf(84), 8.0, B4),            # post-it HACCP qui s'envolent
        S(hf(85), 3.0, B4),            # « vos températures ? »
        S(hf(33), 2.5, B4),            # seul en salle, en baskets
        S(hf(34), 2.5, B4),            # trois demandes de congé
        S(hf(47), 2.5, B4),            # vitrine couverte de calculs
        S(hf(78), 0.2, B4),            # pièces à la frontale
        S(hf(86), 2.5, B4),            # une étoile… le livreur
        S(hf(77), 6.5, B2),            # larmes d'oignon (réaction)
        # break musical : les objets qui changent d'état, le calme
        S(hf(143), 2.5, 3.4),          # thermomètre / registre
        S(hf(144), 2.5, 3.4),          # planning
        S(hf(145), 2.5, 3.4),          # fiche technique
        S(hf(22), 0.0, 4.9),           # dressage au millimètre : la respiration avant le drop
        # final : tout roule
        S(hf(20), 2.0, B4),            # brigade au pas
        S(hf(28), 0.5, B4),            # steadicam salle apaisée
        S(hf(66), 8.0, B4),            # glissade célébration
        S(hf(19), 0.0, B4),            # confettis
        S(hf(21), 7.5, B4),            # le juge sourit
        S(hf(19), 8.0, B4),            # clin d'œil et salut
    ]
    end_d = 4.9

    def overlays(W, H, times, total):
        ov = []
        labels = {2: "LES COMMANDES", 4: "LES RÉSERVATIONS", 6: "LE STOCK", 8: "LES DLC",
                  10: "LE PLANNING", 12: "LA COMPTA", 14: "LES AVIS"}
        for i, txt in labels.items():
            p = card(f"clip-{i}", W, 260, txt, size=88, color=WHITE, pill=(*BLUE, 235), y=60)
            ov.append(dict(png=p, t0=times[i] + 0.05, t1=times[i] + 2 * B4 - 0.1, fin=0.12, fout=0.2, y=H - 640, slide="up"))
        p = card("clip-app", W, 420, ["UNE SEULE", "APP."], size=150, color=INK, pill=(*ORANGE, 235), y=20)
        ov.append(dict(png=p, t0=times[16] + 3.2, t1=times[19] + 4.6, fin=0.3, fout=0.3, y=H - 760, slide="up"))
        ov.append(dict(png=logo_corner("clip-logo", W, H, scale=0.30, margin=48), t0=times[20], t1=times[25] + B4, fin=0.4, fout=0.2))
        ov.append(dict(png=end_card("clip-end", W, H, TAGLINE), t0=total - end_d, t1=total + 1, fin=0.5, fout=0.0))
        return ov

    total = sum(s["dur"] for s in segs) + end_d
    segs.append(S(hf(19), 8.0, end_d))  # support du carton final (recouvert par le carton)
    t = [0.0]
    for s in segs[:-1]:
        t.append(t[-1] + s["dur"])
    audio = dict(music=MUSIC_CLIP, music_gain=-6.0, music_fade_out=1.2, src_gain=-24.0, duck=0.35,
                 vo=[(vo("C1"), 0.35), (vo("C2"), t[16] + 0.4), (vo("C3"), t[20] + 0.3), (vo("C4"), t[-1] + 0.4)])
    out = build_film("foodeatup-clip", W, H, segs, overlays, audio)
    to_16x9(out, "foodeatup-clip")


# ------------------------------------------------------------------ 2. PRÉSENTATION

def presentation():
    """« Le même restaurant » — ~85 s, 9:16 (+16:9), narratrice Anaïs, underscore original.
    100 % plans Higgsfield (aucun screencast, aucun avatar)."""
    W, H = 1080, 1920
    segs = [
        # P1 — ce qui se perd (12,4 s)
        S(hf(23), 2.0, 3.4), S(hf(69), 5.5, 3.3), S(hf(84), 7.5, 3.2), S(hf(38), 5.5, 3.6),
        # P2 — une seule plateforme (12,4 s) : les objets qui changent d'état
        S(hf(141), 2.5, 3.4), S(hf(142), 2.5, 3.4), S(hf(144), 2.5, 3.2), S(hf(145), 2.5, 3.2),
        # P3 — les quatre agents (19,8 s)
        S(hf(25), 2.0, 4.0), S(hf(71), 5.0, 4.2), S(hf(37), 5.0, 4.2), S(hf(68), 2.0, 4.4), S(hf(63), 5.0, 4.4),
        # P4 — HACCP (11,7 s)
        S(hf(85), 2.5, 3.2), S(hf(84), 6.6, 3.2), S(hf(143), 2.5, 3.0), S(hf(36), 5.0, 3.2),
        # P5 — MCP (10,5 s)
        S(hf(29), 4.5, 5.4), S(hf(22), 0.0, 5.6),
        # P6 — clôture (5,9 s)
        S(hf(28), 0.5, 4.2), S(hf(19), 8.0, 2.4),
    ]
    end_d = 6.0
    blocks = [(0, "P1"), (4, "P2"), (8, "P3"), (13, "P4"), (17, "P5"), (19, "P6")]

    def overlays(W, H, times, total):
        ov = [dict(png=logo_corner("pres-logo", W, H, scale=0.26, margin=44), t0=0.0, t1=total - end_d, fin=0.5, fout=0.3)]
        agents = [(9, "Jarvis", "commis vocal en cuisine"), (10, "Caroline", "répond à vos clients"),
                  (11, "PrediBot", "prépare la nuit"), (12, "Iris", "publie sur les réseaux")]
        for i, name, sub in agents:
            p = card(f"pres-{name}", W, 300, name, size=96, color=WHITE, pill=(*BLUE, 230), y=40, sub=sub, sub_size=44)
            ov.append(dict(png=p, t0=times[i] + 0.2, t1=times[i] + segs[i]["dur"] - 0.1, fin=0.2, fout=0.2, y=H - 720, slide="up"))
        p = card("pres-14", W, 300, "14 modules · 8 boucles", size=76, color=INK, pill=(*ORANGE, 235), y=40)
        ov.append(dict(png=p, t0=times[4] + 0.3, t1=times[6] + 1.5, fin=0.2, fout=0.2, y=H - 700, slide="up"))
        p = card("pres-haccp", W, 300, "HACCP", size=96, color=WHITE, pill=(*BLUE, 230), y=40, sub="le classeur s'écrit tout seul", sub_size=44)
        ov.append(dict(png=p, t0=times[13] + 0.3, t1=times[15] + 1.0, fin=0.2, fout=0.2, y=H - 720, slide="up"))
        p = card("pres-mcp", W, 300, "177 outils MCP", size=88, color=INK, pill=(*ORANGE, 235), y=40, sub="Claude · Mistral · ChatGPT · WhatsApp", sub_size=40)
        ov.append(dict(png=p, t0=times[17] + 0.3, t1=times[18] + 2.0, fin=0.2, fout=0.2, y=H - 720, slide="up"))
        ov.append(dict(png=end_card("pres-end", W, H, ["C'est le même restaurant.", "Une infinité de solutions", "pour gérer le vôtre."]),
                       t0=total - end_d, t1=total + 1, fin=0.6, fout=0.0))
        return ov

    segs.append(S(hf(19), 8.0, end_d))
    t = [0.0]
    for s in segs[:-1]:
        t.append(t[-1] + s["dur"])
    audio = dict(music=MUSIC_UNDER, music_gain=-13.0, music_fade_out=2.5, src_gain=-20.0, duck=0.3,
                 vo=[(vo(code), t[i] + 0.35) for i, code in blocks])
    out = build_film("foodeatup-presentation", W, H, segs, overlays, audio)
    to_16x9(out, "foodeatup-presentation")



# ------------------------------------------------------------------ 3. COMMERCIAL

def commercial():
    """« Le contrôleur » — ~36 s, 9:16 (+16:9), voix pub Paul K. 100 % plans Higgsfield."""
    W, H = 1080, 1920
    segs = [
        # A1 — le contrôleur (7,7 s)
        S(hf(85), 0.0, 4.4), S(hf(84), 7.6, 3.7),
        # A2 — tout est déjà là (13,9 s)
        S(hf(143), 2.5, 3.3), S(hf(145), 2.5, 3.6), S(hf(142), 2.5, 3.2), S(hf(144), 2.5, 3.2), S(hf(25), 2.0, 2.7),
        # A3 — signature (5,2 s)
        S(hf(28), 0.5, 3.3), S(hf(19), 8.0, 2.4),
    ]
    end_d = 6.0

    def overlays(W, H, times, total):
        ov = []
        p = card("pub-mardi", W, 300, "Mardi, 11 h.", size=100, color=WHITE, pill=(*INK, 200), y=40)
        ov.append(dict(png=p, t0=0.3, t1=4.2, fin=0.2, fout=0.2, y=H - 700, slide="up"))
        for i, txt in [(2, "TEMPÉRATURES"), (3, "FICHES TECHNIQUES"), (4, "STOCK"), (5, "PLANNING")]:
            p = card(f"pub-{i}", W, 260, txt, size=80, color=WHITE, pill=(*BLUE, 235), y=50)
            ov.append(dict(png=p, t0=times[i] + 0.15, t1=times[i] + segs[i]["dur"] - 0.05, fin=0.12, fout=0.15, y=H - 660, slide="up"))
        ov.append(dict(png=logo_corner("pub-logo", W, H, scale=0.30, margin=48), t0=times[7], t1=times[8] + 2.4, fin=0.3, fout=0.2))
        ov.append(dict(png=end_card("pub-end", W, H, TAGLINE), t0=total - end_d, t1=total + 1, fin=0.5, fout=0.0))
        return ov

    segs.append(S(hf(19), 8.0, end_d))
    t = [0.0]
    for s in segs[:-1]:
        t.append(t[-1] + s["dur"])
    audio = dict(music=MUSIC_UNDER_ALT, music_start=8.0, music_gain=-12.0, music_fade_out=2.0, src_gain=-16.0, duck=0.3,
                 vo=[(vo("A1"), 0.3), (vo("A2"), t[2] + 0.2), (vo("C3"), t[7] + 0.2), (vo("A4"), t[9] + 0.5)])
    out = build_film("foodeatup-commercial", W, H, segs, overlays, audio)
    to_16x9(out, "foodeatup-commercial")



# ------------------------------------------------------------------ 4. DÉMO

def demo():
    """« Un tour du restaurant » — ~1 min 40, 9:16 (+16:9), voix tutoriel Enrick.
    100 % plans Higgsfield. Toute la bibliothèque est tournée en 720×1280 : le master est
    donc vertical, la version 16:9 est dérivée comme pour les autres films."""
    W, H = 1080, 1920
    segs = [
        # D1 — bienvenue / pilotage (12,3 s)
        S(hf(19), 0.0, 3.4), S(hf(28), 0.5, 4.4), S(hf(25), 2.0, 4.7),
        # D2 — carte, coût matière, fiche technique (11,7 s)
        S(hf(44), 2.0, 4.2), S(hf(22), 0.0, 3.8), S(hf(145), 2.5, 4.0),
        # D3 — réception et stock (10,1 s)
        S(hf(68), 2.0, 3.6), S(hf(31), 5.0, 3.4), S(hf(142), 2.5, 3.3),
        # D4 — hygiène et HACCP (13,0 s)
        S(hf(35), 5.0, 4.0), S(hf(143), 2.5, 4.4), S(hf(84), 6.6, 4.8),
        # D5 — équipe et planning (8,8 s)
        S(hf(66), 7.5, 4.4), S(hf(33), 2.5, 4.6),
        # D6 — factures (7,0 s)
        S(hf(56), 5.0, 3.6), S(hf(46), 7.5, 3.6),
        # D7 — boutique en ligne (6,2 s)
        S(hf(62), 0.0, 3.2), S(hf(50), 2.0, 3.2),
        # D8 — Jarvis et PrediBot (8,9 s)
        S(hf(70), 5.0, 4.4), S(hf(141), 2.5, 4.7),
        # D9 — MCP et invitation (11,1 s)
        S(hf(72), 2.0, 3.6), S(hf(20), 2.0, 3.8), S(hf(21), 7.0, 3.9),
    ]
    end_d = 6.5
    blocks = [(0, "D1"), (3, "D2"), (6, "D3"), (9, "D4"), (12, "D5"), (14, "D6"), (16, "D7"), (18, "D8"), (20, "D9")]
    chapters = [(0, "Piloter le restaurant"), (3, "Carte & coût matière"), (6, "StockVision · réception"),
                (9, "Hygiène & HACCP"), (12, "Équipe & planning"), (14, "Factures · OCR"),
                (16, "Boutique en ligne"), (18, "Jarvis & PrediBot"), (20, "MCP · Claude")]

    def overlays(W, H, times, total):
        ov = [dict(png=logo_corner("demo-logo", W, H, scale=0.26, margin=44), t0=1.0, t1=total - end_d, fin=0.4, fout=0.3)]
        starts = [i for i, _ in chapters] + [len(segs) - 1]
        ends = {chapters[k][0]: times[starts[k + 1]] if starts[k + 1] < len(times) else total - end_d
                for k in range(len(chapters))}
        for i, txt in chapters:
            p = card(f"demo-ch{i}", W, 200, txt, size=64, color=WHITE, pill=(*BLUE, 235), y=30)
            ov.append(dict(png=p, t0=times[i] + 0.1, t1=ends[i] - 0.1, fin=0.2, fout=0.2, y=H - 620, slide="up"))
        ov.append(dict(png=end_card("demo-end", W, H, TAGLINE), t0=total - end_d, t1=total + 1, fin=0.6, fout=0.0))
        return ov

    segs.append(S(hf(19), 8.0, end_d))
    t = [0.0]
    for s in segs[:-1]:
        t.append(t[-1] + s["dur"])
    audio = dict(music=MUSIC_UNDER, music_gain=-16.0, music_fade_out=3.0, src_gain=-26.0, duck=0.3,
                 vo=[(vo(code), t[i] + 0.3) for i, code in blocks])
    out = build_film("foodeatup-demo", W, H, segs, overlays, audio)
    to_16x9(out, "foodeatup-demo")


# ------------------------------------------------------------------ 5. AVANT / APRÈS

def avant_apres():
    """« Le même restaurant, deux fois » — ~40 s, 9:16 (+16:9), narratrice Anaïs.
    Bâti sur les diptyques de la bibliothèque : même lieu, même heure, même personne,
    tournés une fois sans le logiciel et une fois avec (index 434-481)."""
    W, H = 1080, 1920
    segs = [
        # AVANT — ce qui se perd (12,4 s)
        S(hf(456), 0.5, 3.2, fit="blur", zoom=1.35),   # 7 h : le classeur papier corné
        S(hf(451), 1.0, 3.0, fit="blur", zoom=1.35),   # 13 h : carnet, téléphone, terminal
        S(hf(434), 1.0, 3.0, fit="blur", zoom=1.35),   # 12 h 30 : le ticket froissé au pass
        S(hf(473), 1.0, 3.4, fit="blur", zoom=1.35),   # 8 h : la pile de bons de livraison
        # APRÈS — tout est déjà là (13,9 s)
        S(hf(478), 0.8, 3.4, fit="blur", zoom=1.35),   # même réserve : le thermomètre lu au téléphone
        S(hf(457), 0.8, 3.4, fit="blur", zoom=1.35),   # même comptoir : une seule tablette
        S(hf(453), 0.8, 3.4, fit="blur", zoom=1.35),   # même pass : l'écran mural dans l'ordre
        S(hf(474), 0.8, 3.9, fit="blur", zoom=1.35),   # même bureau : la prévision qui défile
        # clôture (5,9 s)
        S(hf(476), 1.0, 2.9, fit="blur", zoom=1.35),   # le plan de salle à jour
        S(hf(484), 2.0, 3.2, fit="blur", zoom=1.35),   # la boucle infinie tracée en lumière
    ]
    end_d = 5.6

    def overlays(W, H, times, total):
        ov = []
        p = card("aa-avant", W, 260, "SANS", size=104, color=WHITE, pill=(*INK, 210), y=50)
        ov.append(dict(png=p, t0=0.4, t1=times[4] - 0.15, fin=0.25, fout=0.25, y=110))
        p = card("aa-apres", W, 260, "AVEC", size=104, color=WHITE, pill=(*BLUE, 235), y=50)
        ov.append(dict(png=p, t0=times[4] + 0.1, t1=times[8] - 0.15, fin=0.25, fout=0.25, y=110))
        heures = [(0, "7 h"), (1, "13 h"), (2, "12 h 30"), (3, "8 h"),
                  (4, "7 h"), (5, "13 h"), (6, "12 h 30"), (7, "8 h")]
        for i, h in heures:
            p = card(f"aa-h{i}", W, 200, h, size=64, color=WHITE, pill=(*INK, 170), y=30)
            ov.append(dict(png=p, t0=times[i] + 0.15, t1=times[i] + segs[i]["dur"] - 0.15, fin=0.2, fout=0.2,
                           y=H - 560, slide="up"))
        ov.append(dict(png=logo_corner("aa-logo", W, H, scale=0.26, margin=44), t0=times[8], t1=total - end_d,
                       fin=0.3, fout=0.2))
        ov.append(dict(png=end_card("aa-end", W, H, ["C'est le même restaurant.", "Une infinité de solutions",
                                                     "pour gérer le vôtre."]),
                       t0=total - end_d, t1=total + 1, fin=0.5, fout=0.0))
        return ov

    segs.append(S(hf(406), 2.0, end_d))
    t = [0.0]
    for s in segs[:-1]:
        t.append(t[-1] + s["dur"])
    audio = dict(music=MUSIC_UNDER, music_gain=-13.0, music_fade_out=2.2, src_gain=-19.0, duck=0.3,
                 vo=[(vo("P1"), 0.3), (vo("A2"), t[4] + 0.2), (vo("P6"), t[8] + 0.2), (vo("C4"), t[-1] + 0.6)])
    out = build_film("foodeatup-avant-apres", W, H, segs, overlays, audio)
    to_16x9(out, "foodeatup-avant-apres")


# ------------------------------------------------------------------ 6. BANDE-ANNONCE

def teaser():
    """« FoodEatUp, la bande-annonce » — ~22 s, 9:16 (+16:9), musique du clip, pas de voix
    avant la signature. Les plans les plus spectaculaires de la bibliothèque."""
    W, H = 1080, 1920
    B4 = 1.951
    segs = [
        S(hf(489), 0.4, B4),    # le réveil à 5 h 47
        S(hf(279), 4.0, B4),    # le coup de feu filmé comme une bataille
        S(hf(319), 4.5, B4),    # le ruban de tickets sans fin
        S(hf(282), 2.0, B4),    # l'intérieur du lave-verres
        S(hf(285), 4.0, B4),    # le but qui soulève le serveur
        S(hf(443), 2.0, B4),    # le burger au ralenti
        S(hf(468), 1.0, 2.6),   # l'assiette qui tombe dans la piscine
        S(hf(331), 6.0, 2.6),   # le clin d'œil du soleil
        S(hf(315), 3.0, 2.6),   # les confettis du réveillon
        S(hf(272), 3.0, 3.6),   # le salut de troupe
    ]
    end_d = 5.6

    def overlays(W, H, times, total):
        ov = []
        p = card("tz-1", W, 300, "UN RESTAURANT,", size=104, color=WHITE, pill=(*INK, 200), y=40)
        ov.append(dict(png=p, t0=0.3, t1=times[3] - 0.1, fin=0.2, fout=0.2, y=H - 700, slide="up"))
        p = card("tz-2", W, 300, "C'EST TOUS LES JOURS ÇA.", size=88, color=INK, pill=(*ORANGE, 235), y=40)
        ov.append(dict(png=p, t0=times[3] + 0.1, t1=times[6] - 0.1, fin=0.2, fout=0.2, y=H - 700, slide="up"))
        ov.append(dict(png=logo_corner("tz-logo", W, H, scale=0.30, margin=48), t0=times[6], t1=total - end_d,
                       fin=0.3, fout=0.2))
        ov.append(dict(png=end_card("tz-end", W, H, TAGLINE), t0=total - end_d, t1=total + 1, fin=0.5, fout=0.0))
        return ov

    segs.append(S(hf(406), 2.0, end_d))
    t = [0.0]
    for s in segs[:-1]:
        t.append(t[-1] + s["dur"])
    audio = dict(music=MUSIC_CLIP, music_start=14.0, music_gain=-7.0, music_fade_out=1.5, src_gain=-22.0, duck=0.35,
                 vo=[(vo("C3"), t[9] + 0.1), (vo("C4"), t[-1] + 0.5)])
    out = build_film("foodeatup-teaser", W, H, segs, overlays, audio)
    to_16x9(out, "foodeatup-teaser")
