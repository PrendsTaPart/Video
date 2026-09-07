"""Les quatre montages FoodEatUp. Chaque fonction = un film (voir scripts/VOIX-OFF.md)."""
from build import (BLUE, CREAM, INK, ORANGE, WHITE, OUT, REPO, build_film, card, end_card, hf, logo_corner,
                   mix_audio, to_16x9, tuto, vo)

MUSIC_CLIP = "assets/music/musique-clip-123bpm.mp3"
MUSIC_UNDER = "assets/music/musique-underscore-99bpm.mp3"
MUSIC_UNDER_ALT = "assets/music/musique-underscore-99bpm-alt.mp3"
TAGLINE = ["Une infinité de solutions", "pour gérer votre restaurant"]
HERO = REPO / "hero-video" / "assets" / "video"
AVATAR = REPO / "videos" / "foodeatup-qrcode-tuto" / "assets" / "avatar.mp4"


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
    """« Le même restaurant » — ~90 s, 9:16 (+16:9), narratrice Anaïs, underscore original."""
    W, H = 1080, 1920
    segs = [
        # P1 — ce qui se perd (12,4 s)
        S(hf(23), 2.0, 3.4), S(hf(69), 5.5, 3.3), S(hf(84), 7.5, 3.2), S(hf(38), 5.5, 3.6),
        # P2 — une seule plateforme (12,4 s)
        S(hf(141), 2.5, 3.4), S(hf(142), 2.5, 3.4), S(tuto("mouvements-stock"), 0.0, 3.6, fit="blur"), S(tuto("reception-livraison"), 33.0, 3.2, fit="blur"),
        # P3 — les quatre agents (19,8 s)
        S(hf(25), 2.0, 4.0), S(tuto("jarvis"), 9.0, 4.2, fit="blur"), S(hf(53), 0.0, 4.2), S(HERO / "hero-directeur-bureau-matin.mp4", 0.0, 4.4, fit="blur"), S(hf(63), 5.0, 4.4),
        # P4 — HACCP (11,7 s)
        S(hf(85), 2.5, 3.2), S(hf(143), 2.5, 3.2), S(tuto("temperatures"), 6.0, 3.0, fit="blur"), S(tuto("haccp-export"), 39.5, 3.2, fit="blur"),
        # P5 — MCP (10,5 s)
        S(tuto("mcp"), 12.0, 5.6, fit="blur", speed=1.2), S(hf(29), 4.5, 5.4),
        # P6 — clôture (5,9 s)
        S(hf(28), 0.5, 4.2), S(hf(19), 8.0, 2.4),
    ]
    end_d = 6.0
    blocks = [(0, "P1"), (4, "P2"), (8, "P3"), (13, "P4"), (17, "P5"), (19, "P6")]

    def overlays(W, H, times, total):
        ov = [dict(png=logo_corner("pres-logo", W, H, scale=0.26, margin=44), t0=0.0, t1=total - end_d, fin=0.5, fout=0.3)]
        # cartons discrets (le visuel ajoute, il ne redit pas) : noms des agents et modules
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
    """« Le contrôleur » — ~36 s, 9:16 (+16:9), voix pub Paul K."""
    W, H = 1080, 1920
    segs = [
        # A1 — le contrôleur (7,7 s)
        S(hf(85), 0.0, 4.4), S(hf(84), 6.4, 3.7),
        # A2 — tout est déjà là (13,9 s)
        S(hf(143), 2.5, 3.3), S(tuto("haccp-export"), 24.0, 3.6, fit="blur", speed=1.3), S(hf(142), 2.5, 3.2), S(hf(144), 2.5, 3.2), S(hf(25), 2.0, 2.7),
        # A3 — signature (5,2 s)
        S(hf(28), 0.5, 3.3), S(hf(19), 8.0, 2.4),
    ]
    end_d = 6.0

    def overlays(W, H, times, total):
        ov = []
        p = card("pub-mardi", W, 300, "Mardi, 11 h.", size=100, color=WHITE, pill=(*INK, 200), y=40)
        ov.append(dict(png=p, t0=0.3, t1=4.2, fin=0.2, fout=0.2, y=H - 700, slide="up"))
        for i, txt in [(2, "TEMPÉRATURES ✓"), (3, "EXPORT PDF ✓"), (4, "STOCK ✓"), (5, "PLANNING ✓")]:
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
    """« Un tour du logiciel » — ~1 min 45, 16:9, screencasts réels + avatar HeyGen existant."""
    W, H = 1920, 1080
    segs = [
        # D1 — bienvenue (12,3 s)
        S(AVATAR, 0.0, 6.4, fit="cover"), S(tuto("mcp"), 0.0, 6.6, fit="screen"),
        # D2 — carte et fiche plat (11,7 s)
        S(tuto("fiche-plat"), 20.0, 7.0, fit="screen"), S(tuto("fiche-plat"), 78.0, 5.4, fit="screen"),
        # D3 — réception et stock (10,1 s)
        S(tuto("reception-livraison"), 30.0, 6.0, fit="screen"), S(tuto("mouvements-stock"), 0.0, 5.0, fit="screen"),
        # D4 — HACCP (13,0 s)
        S(tuto("temperatures"), 6.0, 5.0, fit="screen"), S(tuto("tracabilite"), 0.0, 4.2, fit="screen"), S(tuto("haccp-export"), 38.0, 4.6, fit="screen"),
        # D5 — équipe (8,8 s)
        S(tuto("planning-poste"), 55.0, 5.6, fit="screen"), S(tuto("qrcode-pointage"), 0.0, 4.0, fit="screen"),
        # D6 — facture OCR (7,0 s)
        S(tuto("facture-ocr"), 12.0, 7.6, fit="screen"),
        # D7 — boutique en ligne (6,2 s)
        S(tuto("boutique"), 8.0, 7.0, fit="screen"),
        # D8 — Jarvis / PrediBot (8,9 s)
        S(tuto("jarvis"), 8.0, 5.0, fit="screen"), S(tuto("predibot"), 3.0, 4.6, fit="screen"),
        # D9 — MCP + CTA (11,1 s)
        S(tuto("mcp"), 12.0, 6.2, fit="screen", speed=1.2),
    ]
    end_d = 6.5
    blocks = [(0, "D1"), (2, "D2"), (4, "D3"), (6, "D4"), (9, "D5"), (11, "D6"), (12, "D7"), (13, "D8"), (15, "D9")]
    chapters = [(1, "Tableau de bord"), (2, "Carte & fiches plats"), (4, "StockVision · réception"), (6, "Hygiène & HACCP"),
                (9, "Équipe & planning"), (11, "Factures · OCR"), (12, "Boutique en ligne"), (13, "Jarvis & PrediBot"), (15, "MCP · Claude")]

    def overlays(W, H, times, total):
        ov = [dict(png=logo_corner("demo-logo", W, H, scale=0.13, margin=36), t0=segs[0]["dur"], t1=total - end_d, fin=0.4, fout=0.3)]
        ends = {i: (times[j] if j < len(times) else total - end_d) for i, j in
                [(1, 2), (2, 4), (4, 6), (6, 9), (9, 11), (11, 12), (12, 13), (13, 15), (15, 16)]}
        for i, txt in chapters:
            p = card(f"demo-ch{i}", 900, 130, txt, size=44, color=WHITE, pill=(*BLUE, 235), y=30, align="left", pad=28)
            ov.append(dict(png=p, t0=times[i] + 0.1, t1=ends[i] - 0.1, fin=0.2, fout=0.2, x=48, y=H - 150, slide="up"))
        ov.append(dict(png=end_card("demo-end", W, H, TAGLINE), t0=total - end_d, t1=total + 1, fin=0.6, fout=0.0))
        return ov

    segs.append(S(tuto("mcp"), 18.0, end_d, fit="screen"))
    t = [0.0]
    for s in segs[:-1]:
        t.append(t[-1] + s["dur"])
    audio = dict(music=MUSIC_UNDER, music_gain=-19.0, music_fade_out=3.0, src_gain=-60.0, duck=0.3,
                 vo=[(vo(code), t[i] + 0.3) for i, code in blocks])
    build_film("foodeatup-demo", W, H, segs, overlays, audio)
