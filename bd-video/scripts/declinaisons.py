#!/usr/bin/env python3
"""Étape 5 — déclinaisons par réseau, découpées dans les épisodes déjà rendus et mixés.

    python3 bd-video/scripts/declinaisons.py ep01 [ep02 …]   # ou : all

Aucun nouveau rendu HyperFrames : on coupe aux frontières de cases (timeline.json), on ajoute des
cartons fixes (fond bleu nuit, Bangers / Comic Neue, logo réel FoodEatUp) et on renormalise à −14 LUFS.

Fichiers produits (renders/<réseau>/) :
  tiktok/story-epNN.mp4                 15 s  accroche + case hero + « Voir l'épisode »
  instagram/reel-epNN.mp4               60–90 s best-of de la partie
  instagram/story-epNN-{1,2,3}-*.mp4    3 × 15 s  teaser, personnage du jour, citation
  linkedin/linkedin-epNN-{9x16,4x5}.mp4 60–120 s angle métier, texte à l'écran (lecture sans le son)
  bonus/personnages/<nom>.mp4           10 s  carton nom + rôle, puis une réplique du personnage
  bonus/une-case-une-fonction/NN-*.mp4  15 s  une fonctionnalité FoodEatUp par case    (argument : bonus)
  facebook/…                            liens vers les fichiers Instagram (mêmes vidéos, légendes adaptées)
"""
import json
import os
import re
import shutil
import subprocess
import sys
import tempfile

ROOT = os.path.join(subprocess.check_output(["git", "rev-parse", "--show-toplevel"], text=True).strip(), "bd-video")
W, H, FPS = 1080, 1920, 30
NAVY, YELLOW, ORANGE, WHITE = "0x0B2545", "0xFFD640", "0xF59B0A", "white"
BANGERS = os.path.join(ROOT, "assets/fonts/bangers-latin-400-normal.woff2")  # le sous-ensemble « latin » couvre les accents français
COMIC = os.path.join(ROOT, "assets/fonts/comic-neue-latin-700-normal.woff2")
LOGO = os.path.join(ROOT, "assets/logos/foodeatup-wordmark-blanc.png")
TRIM_END = 0.38  # on s'arrête avant le glissé de la case suivante (TRANS = 0.4 s)

EP_NUM = {f"ep0{i}": i for i in range(1, 7)}
# Angle « métier » LinkedIn : un titre de cadrage par épisode (aucun chiffre ajouté à la BD).
LINKEDIN = {
    "ep01": ("Restauration", "Le vrai coût d'une journée sans outil"),
    "ep02": ("Gain de temps", "Une seule saisie, pas dix"),
    "ep03": ("Communication", "La vitrine du restaurant, pilotée depuis la carte"),
    "ep04": ("Franchise", "Grandir sans perdre son goût"),
    "ep05": ("IA en cuisine", "Prévoir au lieu de subir"),
    "ep06": ("Outils connectés", "Votre restaurant est unique. Votre FoodEatUp aussi."),
}
METIER = re.compile(r"heure|temps|saisie|stock|marge|planning|franchis|recette|fiche|commande|IA|agent|prévoi|"
                    r"clôtur|chiffre|fournisseur|HACCP|H\.A\.C\.C\.P|automat|tout seul|connect|MCP", re.I)


def run(cmd):
    subprocess.run(cmd, check=True)


def duration(path):
    return float(subprocess.run(["ffprobe", "-v", "error", "-show_entries", "format=duration", "-of", "csv=p=0", path],
                                capture_output=True, text=True).stdout)


def esc(t):
    return t.replace("\\", "\\\\").replace(":", "\\:").replace("'", "’").replace("%", "\\%").replace(",", "\\,")


def wrap(text, n):
    words, lines, cur = text.split(), [], ""
    for w in words:
        if cur and len(cur) + 1 + len(w) > n:
            lines.append(cur)
            cur = w
        else:
            cur = f"{cur} {w}".strip()
    return lines + ([cur] if cur else [])


def card(path, lines, logo=True):
    """Carton fixe 1080×1920. lines = [(texte, police, taille, couleur), …], centré dans la zone sûre."""
    filters, y = [], 640
    if logo:
        filters.append(f"[1:v]scale=640:-1[lg];[0:v][lg]overlay=(W-w)/2-70:{y}[b0]")
        y += 230
        last = "b0"
    else:
        last = "0:v"
    for i, (txt, font, size, color) in enumerate(lines):
        filters.append(f"[{last}]drawtext=fontfile={font}:text='{esc(txt)}':fontsize={size}:fontcolor={color}"
                       f":x=(w-text_w)/2-70:y={y}[t{i}]")
        last = f"t{i}"
        y += int(size * 1.25)
    cmd = ["ffmpeg", "-v", "error", "-y", "-f", "lavfi", "-i", f"color=c={NAVY}:s={W}x{H}"]
    if logo:
        cmd += ["-i", LOGO]
    run(cmd + ["-filter_complex", ";".join(filters), "-map", f"[{last}]", "-frames:v", "1", path])


class Ep:
    def __init__(self, name):
        self.name = name
        self.video = os.path.join(ROOT, "renders", "episodes", f"{name}.mp4")
        tl = json.load(open(os.path.join(ROOT, "montage", name, "timeline.json")))
        self.end0, self.end_d = tl["end"]
        sb = {s["id"]: s for s in json.load(open(os.path.join(ROOT, "storyboard.json")))}
        self.groups = []
        for s in tl["shots"]:
            s = dict(s, **{k: sb[s["id"]].get(k) for k in ("text", "speaker", "hero", "case")})
            key = (s["page"], s["case"])
            if self.groups and self.groups[-1]["key"] == key:
                self.groups[-1]["shots"].append(s)
            else:
                self.groups.append({"key": key, "shots": [s]})
        for g in self.groups:
            g["start"] = g["shots"][0]["start"]
            g["end"] = g["shots"][-1]["start"] + g["shots"][-1]["dur"]
            g["types"] = {s["type"] for s in g["shots"]}
            g["hero"] = any(s["hero"] for s in g["shots"])
            g["text"] = " ".join(s["text"] or "" for s in g["shots"])
        parts = [p for p in dict.fromkeys(s["part"] for g in self.groups for s in g["shots"])
                 if not p.startswith(("Prologue", "Épilogue", "Fermeture", "Ouverture"))]
        self.part = parts[0] if parts else self.groups[0]["shots"][0]["part"]
        self.num = EP_NUM[name]

    def seg(self, g, max_len=None):
        """Plage d'une case, coupée sur une fin de réplique si max_len l'impose."""
        a, b = g["start"], g["end"] - TRIM_END
        if max_len and b - a > max_len:
            acc = a
            for s in g["shots"]:
                if s["start"] + s["dur"] - TRIM_END - a <= max_len:
                    acc = s["start"] + s["dur"] - TRIM_END
            b = acc if acc > a + 2 else a + max_len
        return (a, b)


class Builder:
    def __init__(self, ep, tmp):
        self.ep, self.tmp, self.n = ep, tmp, 0

    def _out(self):
        self.n += 1
        return os.path.join(self.tmp, f"s{self.n:03d}.mp4")

    def clip(self, a, b):
        out = self._out()
        d = b - a
        run(["ffmpeg", "-v", "error", "-y", "-ss", f"{a:.3f}", "-t", f"{d:.3f}", "-i", self.ep.video,
             "-vf", f"fps={FPS},scale={W}:{H},setsar=1",
             "-af", f"aformat=sample_rates=48000:channel_layouts=stereo,afade=t=in:d=0.06,afade=t=out:st={max(0, d-0.12):.3f}:d=0.12",
             "-c:v", "libx264", "-preset", "veryfast", "-crf", "18", "-pix_fmt", "yuv420p", "-c:a", "aac", "-b:a", "192k", out])
        return out

    def still(self, png, d, audio_from=None):
        """Carton fixe ; audio = la musique de fin d'épisode (ou silence)."""
        out = self._out()
        cmd = ["ffmpeg", "-v", "error", "-y", "-loop", "1", "-t", f"{d:.3f}", "-i", png]
        if audio_from is not None:
            cmd += ["-ss", f"{audio_from:.3f}", "-t", f"{d:.3f}", "-i", self.ep.video]
            # la fin d'épisode ne dure que 4 s : on prolonge par du silence, puis fondu
            amap = ["-map", "1:a", "-af", f"aformat=sample_rates=48000:channel_layouts=stereo,apad,atrim=0:{d:.3f},"
                    f"afade=t=in:d=0.2,afade=t=out:st={max(0, min(d, 3.8)-0.6):.3f}:d=0.6"]
        else:
            cmd += ["-f", "lavfi", "-t", f"{d:.3f}", "-i", "anullsrc=r=48000:cl=stereo"]
            amap = ["-map", "1:a"]
        run(cmd + ["-map", "0:v", *amap, "-vf", f"fps={FPS},format=yuv420p,fade=t=in:d=0.25",
                   "-c:v", "libx264", "-preset", "veryfast", "-crf", "18", "-c:a", "aac", "-b:a", "192k", "-t", f"{d:.3f}", out])
        return out

    def finish(self, pieces, dest, fmt="9x16"):
        lst = os.path.join(self.tmp, f"list{self.n}.txt")
        open(lst, "w").write("".join(f"file '{p}'\n" for p in pieces))
        joined = self._out()
        run(["ffmpeg", "-v", "error", "-y", "-f", "concat", "-safe", "0", "-i", lst, "-c", "copy", joined])
        vf = "null"
        if fmt == "4x5":  # 9:16 posé sur un fond flou 1080×1350 : rien n'est rogné
            vf = ("split[a][b];[a]scale=1080:1350:force_original_aspect_ratio=increase,crop=1080:1350,boxblur=30:3,"
                  "eq=brightness=-0.12[bg];[b]scale=-2:1350[fg];[bg][fg]overlay=(W-w)/2:0")
        os.makedirs(os.path.dirname(dest), exist_ok=True)
        run(["ffmpeg", "-v", "error", "-y", "-i", joined, "-filter_complex", vf, "-af", "loudnorm=I=-14:TP=-1.5:LRA=11",
             "-c:v", "libx264", "-preset", "medium", "-crf", "20", "-pix_fmt", "yuv420p",
             "-c:a", "aac", "-b:a", "192k", "-ar", "48000", "-movflags", "+faststart", dest])
        return dest


def pick(groups, budget, score):
    """Cases les mieux notées jusqu'à remplir le budget, remises dans l'ordre du récit."""
    cand = sorted((g for g in groups if score(g) > 0), key=lambda g: (-score(g), g["start"]))
    chosen, total = [], 0.0
    for g in cand:
        d = g["end"] - TRIM_END - g["start"]
        if total + d <= budget:
            chosen.append(g)
            total += d
    return sorted(chosen, key=lambda g: g["start"]), total


def build(name):
    ep = Ep(name)
    if not os.path.exists(ep.video):
        print(f"{name} : rendu absent ({ep.video}), ignoré")
        return []
    made = []
    tmp = tempfile.mkdtemp(prefix=f"decl-{name}-")
    b = Builder(ep, tmp)
    n = ep.num
    title = ep.part.split("·", 1)[-1].strip()
    rd = lambda *p: os.path.join(ROOT, "renders", *p)

    cta_png = os.path.join(tmp, "cta.png")
    card(cta_png, [(f"Épisode {n}", BANGERS, 84, ORANGE)] + [(l, BANGERS, 76, YELLOW) for l in wrap(title, 22)]
         + [("Voir l'épisode · Lien en bio", COMIC, 52, WHITE)])
    hook = (0.0, 2.2)
    heroes = [g for g in ep.groups if g["hero"] and g["types"] != {"titre"}] or \
             [g for g in ep.groups if "bulle" in g["types"]]

    # 1) Story 15 s (TikTok + Instagram teaser) : accroche + case hero + carton.
    hg = heroes[0]
    story = [b.clip(*hook), b.clip(*ep.seg(hg, 9.3))]
    used = 2.2 + duration(story[1])
    story.append(b.still(cta_png, max(2.5, 15.0 - used), audio_from=ep.end0))
    made.append(b.finish(story, rd("tiktok", f"story-ep{n:02d}.mp4")))
    os.makedirs(rd("instagram"), exist_ok=True)
    teaser = rd("instagram", f"story-ep{n:02d}-1-teaser.mp4")
    shutil.copyfile(made[-1], teaser)
    made.append(teaser)

    # 2) Reel 60–90 s : accroche, meilleures cases (hero, bulles), fin.
    score = lambda g: (5 if g["hero"] else 0) + (2 if "bulle" in g["types"] else 0) + (1 if "recit" in g["types"] else 0) \
        - (9 if g["types"] == {"titre"} else 0)
    chosen, tot = pick(ep.groups, 78.0, score)
    pieces = [b.clip(*hook)] + [b.clip(*ep.seg(g)) for g in chosen] + [b.clip(ep.end0, ep.end0 + ep.end_d)]
    made.append(b.finish(pieces, rd("instagram", f"reel-ep{n:02d}.mp4")))

    # 3) Story « personnage du jour » : une case dialoguée d'un membre de la brigade.
    cast = [g for g in ep.groups if "bulle" in g["types"] and g["end"] - g["start"] <= 11.5
            and any(s["speaker"] and s["speaker"] != "MICKAEL" for s in g["shots"])]
    if cast:
        g = max(cast, key=lambda g: (g["hero"], g["end"] - g["start"]))
        who = next(s["speaker"] for s in g["shots"] if s["speaker"] and s["speaker"] != "MICKAEL")
        png = os.path.join(tmp, "perso.png")
        card(png, [("Personnage du jour", BANGERS, 84, ORANGE), ({"L'ASSISTANT IA": "L'assistant IA", "PLANI'T": "Plani't", "PRÉDIBOT": "PrédiBot"}.get(who, who.title()), BANGERS, 130, YELLOW),
                   (f"La Brigade augmentée · épisode {n}", COMIC, 46, WHITE)], logo=False)
        clip = b.clip(*ep.seg(g, 11.0))
        d = duration(clip)
        pieces = [b.still(png, 2.0), clip, b.still(cta_png, max(2.0, 15.0 - 2.0 - d), audio_from=ep.end0)]
        made.append(b.finish(pieces, rd("instagram", f"story-ep{n:02d}-2-personnage.mp4")))

    # 4) Story « citation » : un récitatif de Mickael.
    quotes = [g for g in ep.groups if "recit" in g["types"] and g["end"] - g["start"] <= 11.5]
    if quotes:
        g = max(quotes, key=lambda g: (g["hero"], g["end"] - g["start"]))
        png = os.path.join(tmp, "quote.png")
        card(png, [("La citation du jour", BANGERS, 84, ORANGE), ("Mickael, chef et fondateur", COMIC, 52, WHITE)], logo=False)
        clip = b.clip(*ep.seg(g, 11.0))
        d = duration(clip)
        pieces = [b.still(png, 2.0), clip, b.still(cta_png, max(2.0, 15.0 - 2.0 - d), audio_from=ep.end0)]
        made.append(b.finish(pieces, rd("instagram", f"story-ep{n:02d}-3-citation.mp4")))

    # 5) LinkedIn 60–120 s, angle métier, en 9:16 et en 4:5.
    kicker, angle = LINKEDIN[name]
    png = os.path.join(tmp, "li.png")
    card(png, [(kicker, BANGERS, 80, ORANGE)] + [(l, BANGERS, 84, YELLOW) for l in wrap(angle, 20)]
         + [("Vidéo sous-titrée · lecture sans le son", COMIC, 40, WHITE)])
    score_li = lambda g: (4 if METIER.search(g["text"]) else 0) + (2 if g["hero"] else 0) + (1 if "bulle" in g["types"] else 0) \
        - (9 if g["types"] == {"titre"} else 0)
    chosen, tot = pick(ep.groups, 95.0, score_li)
    pieces = [b.still(png, 3.0)] + [b.clip(*ep.seg(g)) for g in chosen] + [b.clip(ep.end0, ep.end0 + ep.end_d)]
    made.append(b.finish(pieces, rd("linkedin", f"linkedin-ep{n:02d}-9x16.mp4")))
    made.append(b.finish(pieces, rd("linkedin", f"linkedin-ep{n:02d}-4x5.mp4"), fmt="4x5"))

    # 6) Facebook : mêmes fichiers qu'Instagram (liens relatifs).
    os.makedirs(rd("facebook"), exist_ok=True)
    for f in [m for m in made if "/instagram/" in m]:
        link = rd("facebook", os.path.basename(f))
        if os.path.lexists(link):
            os.remove(link)
        os.symlink(os.path.join("..", "instagram", os.path.basename(f)), link)
        made.append(link)
    shutil.rmtree(tmp)
    for m in made:
        print(f"  {os.path.relpath(m, ROOT)}  {duration(m):6.1f} s")
    return made


# Bonus : une case, une fonction (15 s). Libellés repris du texte de la BD.
FONCTIONS = [
    ((33, 2), "Prévisions et commandes"), ((34, 2), "Réception contrôlée"), ((35, 1), "Températures et étiquettes"),
    ((36, 1), "Planning"), ((36, 2), "Pointage au QR code"), ((41, 2), "La commande au bon poste"),
    ((42, 2), "Commander et payer à table"), ((44, 1), "Allergènes depuis la recette"),
    ((47, 2), "Stock mis à jour avec les ventes"), ((48, 2), "Dossier sanitaire prêt chaque jour"),
    ((57, 2), "Diffuser sur les écrans"), ((58, 2), "La carte du soir, toute seule"),
    ((65, 1), "Fiches techniques"), ((68, 2), "Une carte de fidélité partout"),
    ((69, 1), "Agent vocal"), ((72, 1), "Relance des clients (avec accord)"),
]
# Bonus : personnages (10 s). Rôle et réplique tirés des cartes des pages 3 et 4.
PERSONNAGES = [
    ("MICKAEL", "Chef et fondateur", "p60-c1-03"), ("BERNARD", "Gérant · finances", "p38-c2-01"),
    ("LÉA", "Cheffe de partie", "p35-c1-01"), ("KARIM", "Commis", "p34-c1-01"),
    ("SOFIANE", "Responsable de salle", "p40-c2-01"), ("NADIA", "RH et plannings", "p36-c1-01"),
    ("INÈS", "Marketing", "p57-c2-02"), ("THOMAS", "Directeur multi-sites", "p50-c2-01"),
    ("PRÉDIBOT", "Prévisions et brief du jour", "p33-c2-01"), ("IRIS", "Communication", "p37-c1-01"),
    ("CAROLINE", "Agent vocal", "p40-c1-01"), ("JARVIS", "Borne drive vocale", "p45-c1-01"),
    ("L'ASSISTANT IA", "Claude, ChatGPT ou Le Chat", "p62-c1-03"), ("PLANI'T", "Le chef d'orchestre", "p77-c1-01"),
]


def slug(t):
    t = t.lower()
    for a, b in (("àâä", "a"), ("éèêë", "e"), ("îï", "i"), ("ôö", "o"), ("ùûü", "u"), ("ç", "c")):
        for c in a:
            t = t.replace(c, b)
    return re.sub(r"[^a-z0-9]+", "-", t).strip("-")


def bonus():
    eps = {n: Ep(n) for n in EP_NUM if os.path.exists(os.path.join(ROOT, "renders", "episodes", f"{n}.mp4"))}
    tmp = tempfile.mkdtemp(prefix="decl-bonus-")
    sig = os.path.join(tmp, "sig.png")
    card(sig, [("Une seule saisie, pas dix.", BANGERS, 76, YELLOW), ("Testez FoodEatUp · Lien en bio", COMIC, 50, WHITE)])
    rd = lambda *p: os.path.join(ROOT, "renders", "bonus", *p)
    made = []
    for i, (key, label) in enumerate(FONCTIONS, 1):
        hit = next(((e, g) for e in eps.values() for g in e.groups if g["key"] == key), None)
        if not hit:
            continue
        e, g = hit
        b = Builder(e, tmp)
        png = os.path.join(tmp, f"f{i}.png")
        card(png, [("Une case, une fonction", BANGERS, 76, ORANGE)] + [(l, BANGERS, 96, YELLOW) for l in wrap(label, 18)], logo=False)
        clip = b.clip(*e.seg(g, 10.5))
        d = duration(clip)
        made.append(b.finish([b.still(png, 2.0), clip, b.still(sig, max(2.0, 15.0 - 2.0 - d), audio_from=e.end0)],
                             rd("une-case-une-fonction", f"{i:02d}-{slug(label)}.mp4")))
    for name, role, sid in PERSONNAGES:
        hit = next(((e, s) for e in eps.values() for g in e.groups for s in g["shots"] if s["id"] == sid), None)
        if not hit:
            continue
        e, s = hit
        b = Builder(e, tmp)
        png = os.path.join(tmp, f"{slug(name)}.png")
        card(png, [({"L'ASSISTANT IA": "L'assistant IA", "PLANI'T": "Plani't", "PRÉDIBOT": "PrédiBot"}.get(name, name.title()), BANGERS, 130, YELLOW), (role, BANGERS, 70, ORANGE),
                   ("La Brigade augmentée", COMIC, 46, WHITE)], logo=False)
        line = min(s["dur"] - TRIM_END, 9.0)  # la réplique entière, carton raccourci si elle est longue
        made.append(b.finish([b.still(png, max(1.5, 10.0 - line)), b.clip(s["start"], s["start"] + line)],
                             rd("personnages", f"{slug(name)}.mp4")))
    shutil.rmtree(tmp)
    for m in made:
        print(f"  {os.path.relpath(m, ROOT)}  {duration(m):5.1f} s")



def inventaire():
    """Écrit declinaisons.md à partir des fichiers réellement présents dans renders/."""
    nets = [("film", "Film complet (TikTok)"), ("episodes", "Épisodes (TikTok, version intégrale)"), ("tiktok", "TikTok Stories"),
            ("instagram", "Instagram Reels et Stories"), ("facebook", "Facebook Reels et Stories (mêmes fichiers qu'Instagram)"),
            ("linkedin", "LinkedIn"), ("bonus/personnages", "Bonus · série « personnages »"),
            ("bonus/une-case-une-fonction", "Bonus · série « une case, une fonction »")]
    out = ["# Déclinaisons par réseau", "",
           "Généré par `python3 bd-video/scripts/declinaisons.py inventaire` à partir des fichiers de `renders/`.",
           "Les vidéos ne sont pas dans Git (trop lourdes) : voir le README pour les relancer ou les récupérer.", ""]
    total = 0
    for d, title in nets:
        path = os.path.join(ROOT, "renders", d)
        if not os.path.isdir(path):
            continue
        files = sorted(f for f in os.listdir(path) if f.endswith(".mp4") and not f.endswith("-video.mp4") and "animatique" not in f)
        if not files:
            continue
        out += [f"## {title}", "", "| Fichier | Format | Durée |", "|---|---|---:|"]
        for f in files:
            fp = os.path.join(path, f)
            wh = subprocess.run(["ffprobe", "-v", "error", "-select_streams", "v:0", "-show_entries", "stream=width,height",
                                 "-of", "csv=p=0:s=x", fp], capture_output=True, text=True).stdout.strip()
            d_s = duration(fp)
            m, sec = divmod(round(d_s), 60)
            note = " (lien)" if os.path.islink(fp) else ""
            out.append(f"| `renders/{d}/{f}`{note} | {wh} | {m} min {sec:02d} s |" if m else f"| `renders/{d}/{f}`{note} | {wh} | {sec} s |")
            total += 0 if os.path.islink(fp) else 1
        out.append("")
    out.insert(4, f"{total} fichiers vidéo distincts (les liens Facebook pointent vers les fichiers Instagram).\n")
    open(os.path.join(ROOT, "declinaisons.md"), "w").write("\n".join(out))
    print(f"declinaisons.md : {total} fichiers")


if __name__ == "__main__":
    names = sys.argv[1:] or ["ep01"]
    if names == ["inventaire"]:
        inventaire()
        names = []
    if names == ["bonus"]:
        bonus()
        names = []
    if names == ["all"]:
        names = list(EP_NUM)
    for nm in names:
        print(nm)
        build(nm)
