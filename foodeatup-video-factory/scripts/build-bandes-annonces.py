#!/usr/bin/env python3
"""Monte les bandes-annonces de saison, et tire leur affiche.

    python3 scripts/build-bandes-annonces.py              toutes celles qui ont un plan
    python3 scripts/build-bandes-annonces.py le-coup-de-feu-S1

MONTAGE SEUL. Aucun crédit dépensé ici : le plan Higgsfield et les deux
répliques ElevenLabs sont déjà payés et déposés.

Pourquoi la voix du plan est écrasée
------------------------------------
Le prompt Higgsfield demandait les deux répliques, et Seedance les a bien
prononcées : chaque plan arrive avec une voix française incrustée, qu'on ne
peut pas retirer. Elle ne convient pas — c'est le constat qui a lancé ce
montage. On ne peut donc que la couvrir : le son d'origine tombe de vingt
décibels, ce qui le ramène au rang de fond de salle, et la voix ElevenLabs
passe par-dessus. Baisser moins laisserait entendre deux voix qui disent le
même texte à un cheveu d'intervalle, ce qui s'entend comme un défaut.

L'ambiance n'est pas coupée pour autant : un plan de cuisine muet sonne faux,
et c'est elle qui porte le lieu.

L'anatomie
----------
    0,0 → 10,0   le plan, recadré en 1080 × 1920
    0,5          l'ouverture, dite par la voix maison
    ~            la chute, calée pour finir sur la dernière image
    tout du long le lit musical, sous les voix
    tout du long le badge FoodEatUp, à sa place habituelle

Les deux répliques se calent comme la punchline des chapitres du film : la
chute finit sur l'image, elle n'est jamais coupée. L'ouverture, elle, part tôt
— une bande-annonce qui laisse une seconde de silence avant de parler perd le
spectateur.

L'affiche
---------
Une image fixe tirée du plan lui-même, à l'instant où le personnage regarde
l'objectif, plus le nom de la série, le titre de la saison et la date de
diffusion. Pas de composition inventée : l'affiche est le dernier plan du film
qu'elle annonce.
"""
import json
import os
import pathlib
import re
import subprocess
import sys
import tempfile
import textwrap

R = pathlib.Path(__file__).resolve().parent.parent
SERIES = R.parent / "foodeatup-social" / "data" / "series.json"
POLICE = R / "templates" / "Poppins-800.ttf"
LOGO = R / "templates" / "logo_foodeatup.png"
BGM = R / "templates" / "bgm.mp3"
PLANS = R / "assets" / "bandes-annonces"
VOIX = R / "assets" / "vo" / "bandes-annonces"
SORTIE = R / "dist" / "bandes-annonces"
AFFICHES = R / "dist" / "affiches"

L, H = 1080, 1920
DUREE = 10.0
T_OUVERTURE = 0.5

# Le plan garde son ambiance mais perd sa voix : -20 dB, soit un dixième de la
# tension d'origine. Voir l'en-tête pour la raison.
GAIN_PLAN = 0.1
# Le lit musical, au niveau relevé sur les masters de la série.
GAIN_BGM = 0.16

LOGO_X, LOGO_Y = 795, 57
MARGE = 80
CREME = "0xFCF9E6"
ORANGE = "0xFFA500"
MARINE = "0x0F1A23"


def duree(f):
    return float(subprocess.run(
        ["ffprobe", "-v", "error", "-show_entries", "format=duration",
         "-of", "csv=p=0", str(f)], capture_output=True, text=True).stdout.strip())


def fin_de_parole(mp3, plancher_db=-45.0, pas=0.02):
    """L'instant où la voix se tait vraiment, silence de queue exclu.

    Même mesure que dans build-film-stories.py, et pour la même raison : caler
    sur la durée du fichier ferait entrer la voix trop tôt, le dernier mot
    tombant alors bien avant l'image finale.
    """
    out = subprocess.run(
        ["ffmpeg", "-hide_banner", "-nostats", "-i", str(mp3),
         "-af", f"silencedetect=noise={plancher_db}dB:d={pas}", "-f", "null", "-"],
        capture_output=True, text=True).stderr
    d = duree(mp3)
    debuts = [float(m) for m in re.findall(r"silence_start: (-?[\d.]+)", out)]
    fins = [float(m) for m in re.findall(r"silence_end: ([\d.]+)", out)]
    if debuts and (not fins or fins[-1] < debuts[-1] or fins[-1] >= d - 0.05):
        return min(debuts[-1] + 0.05, d)
    return d


MOIS = ("janvier", "février", "mars", "avril", "mai", "juin", "juillet",
        "août", "septembre", "octobre", "novembre", "décembre")


def date_lisible(iso):
    """« 2026-09-27 » devient « 27 septembre 2026 ».

    Une affiche se lit, elle ne se parse pas : la date ISO est bonne pour la
    donnée, illisible sur une image.
    """
    m = re.match(r"(\d{4})-(\d{2})-(\d{2})$", (iso or "").strip())
    if not m:
        return iso or ""
    a, mo, j = int(m[1]), int(m[2]), int(m[3])
    return f"{'1er' if j == 1 else j} {MOIS[mo - 1]} {a}"


def a_du_son(clip):
    out = subprocess.run(
        ["ffprobe", "-v", "error", "-select_streams", "a",
         "-show_entries", "stream=codec_type", "-of", "csv=p=0", str(clip)],
        capture_output=True, text=True).stdout.strip()
    return bool(out)


def fichier(txt, fics):
    f = tempfile.NamedTemporaryFile("w", suffix=".txt", delete=False, encoding="utf-8")
    f.write(txt)
    f.close()
    fics.append(f.name)
    return f.name


def monte(cle, plan, ouv, chute, dest):
    """Le plan, ses deux voix, sa musique, son badge."""
    fics = []
    muet = not a_du_son(plan)

    # La chute finit sur l'image ; l'ouverture part tôt. Si les deux se
    # chevauchaient — une ouverture longue et une chute longue sur dix
    # secondes — l'ouverture serait avancée pour leur laisser un blanc.
    t_chute = max(0.0, DUREE - fin_de_parole(chute))
    fin_ouv = T_OUVERTURE + fin_de_parole(ouv)
    t_ouv = T_OUVERTURE if fin_ouv <= t_chute - 0.2 else max(0.0, t_chute - 0.2 - (fin_ouv - T_OUVERTURE))

    entrees = ["-i", str(plan), "-i", str(LOGO), "-i", str(BGM),
               "-i", str(ouv), "-i", str(chute)]
    i_plan, i_bgm, i_ouv, i_chute = "0:a", "2:a", "3:a", "4:a"
    if muet:
        entrees += ["-f", "lavfi", "-t", str(DUREE), "-i", "anullsrc=r=48000:cl=stereo"]
        i_plan = "5:a"

    g = [
        f"[0:v]scale={L}:{H}:force_original_aspect_ratio=increase,"
        f"crop={L}:{H},setsar=1,fps=30,trim=0:{DUREE},setpts=PTS-STARTPTS[v0]",
        f"[1:v]scale=250:-1[logo]",
        f"[v0][logo]overlay={LOGO_X}:{LOGO_Y}[vout]",

        f"[{i_plan}]aresample=48000,atrim=0:{DUREE},asetpts=PTS-STARTPTS,"
        f"volume={GAIN_PLAN}[amb]",

        # Le lit musical entre et sort en fondu : une musique qui démarre net
        # sur la première frame s'entend comme un défaut de montage.
        f"[{i_bgm}]aresample=48000,atrim=0:{DUREE},asetpts=PTS-STARTPTS,"
        f"volume={GAIN_BGM},afade=t=in:st=0:d=0.6,"
        f"afade=t=out:st={DUREE - 0.8}:d=0.8[mus]",

        f"[{i_ouv}]aresample=48000,adelay={int(t_ouv * 1000)}|{int(t_ouv * 1000)},"
        f"atrim=0:{DUREE},asetpts=PTS-STARTPTS[vo1]",
        f"[{i_chute}]aresample=48000,adelay={int(t_chute * 1000)}|{int(t_chute * 1000)},"
        f"atrim=0:{DUREE},asetpts=PTS-STARTPTS[vo2]",

        f"[amb][mus][vo1][vo2]amix=inputs=4:duration=first:normalize=0,"
        f"loudnorm=I=-14:TP=-1:LRA=11,alimiter=limit=0.794:level=disabled,"
        f"apad,atrim=0:{DUREE}[aout]",
    ]

    cmd = ["ffmpeg", "-v", "error", "-y"] + entrees + [
        "-filter_complex", ";".join(g),
        "-map", "[vout]", "-map", "[aout]",
        "-c:v", "libx264", "-preset", "medium", "-crf", "20",
        "-pix_fmt", "yuv420p", "-r", "30",
        "-c:a", "aac", "-b:a", "128k", "-ar", "48000",
        "-t", str(DUREE), "-movflags", "+faststart", str(dest)]
    try:
        subprocess.run(cmd, check=True, capture_output=True, text=True)
    finally:
        for f in fics:
            os.unlink(f)
    return t_ouv, t_chute


def affiche(plan, serie, saison, date, dest):
    """L'image fixe qui annonce la saison.

    Tirée à 9,2 s : c'est là que le personnage est face objectif sur tous les
    plans, la consigne de cadrage étant la même pour les dix-huit.
    """
    fics = []
    police = str(POLICE).replace(":", r"\:")
    t_serie = fichier(serie.upper(), fics)
    t_saison = fichier("\n".join(textwrap.wrap(saison, 22)), fics)
    t_date = fichier(date_lisible(date), fics)

    g = (
        f"[0:v]scale={L}:{H}:force_original_aspect_ratio=increase,"
        f"crop={L}:{H},setsar=1[img];"
        # Un voile marine du bas vers le milieu : le texte doit se lire sur
        # n'importe quel plan, y compris les plus clairs.
        f"[img]drawbox=x=0:y={H - 780}:w={L}:h=780:color={MARINE}@0.72:t=fill[v1];"
        f"[v1]drawtext=fontfile='{police}':textfile='{t_serie}':"
        f"fontsize=44:fontcolor={ORANGE}:x={MARGE}:y={H - 700}[v2];"
        f"[v2]drawtext=fontfile='{police}':textfile='{t_saison}':"
        f"fontsize=92:fontcolor={CREME}:line_spacing=12:x={MARGE}:y={H - 610}[v3];"
        f"[v3]drawtext=fontfile='{police}':textfile='{t_date}':"
        f"fontsize=40:fontcolor={ORANGE}:x={MARGE}:y={H - 250}[v4];"
        f"[1:v]scale=250:-1[logo];"
        f"[v4][logo]overlay={LOGO_X}:{LOGO_Y}[vout]"
    )
    cmd = ["ffmpeg", "-v", "error", "-y", "-ss", "9.2", "-i", str(plan),
           "-i", str(LOGO), "-filter_complex", g, "-map", "[vout]",
           "-frames:v", "1", "-q:v", "2", str(dest)]
    try:
        subprocess.run(cmd, check=True, capture_output=True, text=True)
    finally:
        for f in fics:
            os.unlink(f)


def controle(dest):
    out = subprocess.run(
        ["ffprobe", "-v", "error", "-show_entries",
         "stream=codec_type,width,height:format=duration", "-of", "json", str(dest)],
        capture_output=True, text=True).stdout
    d = json.loads(out)
    dur = float(d["format"]["duration"])
    v = [s for s in d["streams"] if s["codec_type"] == "video"][0]
    a = [s for s in d["streams"] if s["codec_type"] == "audio"]
    ok = (abs(dur - DUREE) < 0.3 and v["width"] == L and v["height"] == H and len(a) == 1)
    return ok, f"{dur:.2f}s {v['width']}x{v['height']} {'son' if a else 'MUET'}"


def main(cibles):
    d = json.load(open(SERIES, encoding="utf-8"))
    saisons = {}
    for s in d["series"]:
        for sa in s["saisons"]:
            if sa.get("bandeAnnonce"):
                saisons[f"{s['slug']}-S{sa['numero']}"] = (s, sa)

    SORTIE.mkdir(parents=True, exist_ok=True)
    AFFICHES.mkdir(parents=True, exist_ok=True)
    if not cibles:
        cibles = sorted(k for k in saisons if (PLANS / f"{k}.mp4").exists())

    faits = rates = sautes = 0
    for cle in cibles:
        if cle not in saisons:
            print(f"  {cle}  inconnue")
            sautes += 1
            continue
        s, sa = saisons[cle]
        plan = PLANS / f"{cle}.mp4"
        ouv, chute = VOIX / f"{cle}__OUV.mp3", VOIX / f"{cle}__CHU.mp3"
        dest = SORTIE / f"{cle}.mp4"
        aff = AFFICHES / f"{cle}.jpg"

        manque = [n for n, f in (("plan", plan), ("ouverture", ouv), ("chute", chute))
                  if not f.exists()]
        if manque:
            print(f"  {cle}  manque : {', '.join(manque)}")
            sautes += 1
            continue
        if dest.exists() and dest.stat().st_size > 0:
            print(f"  {cle}  déjà monté")
            sautes += 1
            continue
        try:
            t1, t2 = monte(cle, plan, ouv, chute, dest)
            affiche(plan, s["nom"], sa["titre"], sa["bandeAnnonce"].get("date") or "", aff)
            ok, detail = controle(dest)
            print(f"  {cle:34s} {'monté ' if ok else 'REJETÉ'} {detail}"
                  f"  voix à {t1:.1f}s et {t2:.1f}s")
            faits += ok
            rates += (not ok)
        except subprocess.CalledProcessError as err:
            print(f"  {cle}  ÉCHEC ffmpeg\n{(err.stderr or '')[:400]}")
            rates += 1

    print(f"\nmontées : {faits} | déjà là ou incomplètes : {sautes} | en échec : {rates}")


if __name__ == "__main__":
    main(sys.argv[1:])
