#!/usr/bin/env python3
"""Le générique de fin des stories de UpEatFood, en motion design.

    python3 scripts/build-film-stories.py            tous les chapitres qui ont un plan
    python3 scripts/build-film-stories.py EP501 EP502

MONTAGE SEUL. Aucun crédit dépensé : le générique se fabrique avec ffmpeg, en
local, par-dessus le plan déjà payé.

Pourquoi un script à part
-------------------------
`build-stories.py` monte les stories de la série comique : un hook en haut à
0,6 s, une punchline en bas à 5,6 s, un badge présent du début à la fin. Rien
de tout ça ne convient à UpEatFood. Le film ne porte pas de badge — c'est
justement ce qui fait qu'il ressemble à un film — et il n'a pas de blague à
commenter.

Ce qu'il a, c'est un problème que la série comique n'a pas : trente-cinq
stories publiées un jour après l'autre se terminent chacune sur un plan de
cinéma, et rien ne dit qu'il y en a une autre demain. Le générique de fin est
la seule pièce qui transforme trente-cinq stories isolées en une série qu'on
attend.

L'anatomie — les cinq temps de la consigne
------------------------------------------
    0,0 → 10,0   le plan, son son d'origine, jamais coupé
    8,5          un voile marine monte du bas sur le tiers inférieur, en 0,3 s
    8,8          le logo arrive du bas et cale au centre du voile, overshoot 6 %
    9,1          la punchline s'écrit sous le logo, un mot toutes les 0,06 s
    9,6          « à suivre » en orange à droite, sa flèche avance de 8 px
    10,0         rien n'a disparu

Les positions des mots sont mesurées avec PIL avant le rendu. `drawtext` ne
sait ni revenir à la ligne ni centrer un mot par rapport à ceux qui l'entourent :
sans mesure, une punchline de neuf mots sort en escalier hors du cadre.

La voix qui dit la punchline
----------------------------
Le film demande une voix off de plus sur ces 1,5 s. Elle se dépose dans
`assets/vo/punchlines/EPxxx.mp3`, comme celle des masters. Quand elle est là,
le son du plan s'efface de 9 dB derrière elle ; quand elle manque, le générique
se monte quand même et le script le dit. Une story muette de sa voix reste
publiable ; une story qui n'existe pas, non.
"""
import json
import os
import pathlib
import re
import subprocess
import sys
import tempfile

R = pathlib.Path(__file__).resolve().parent.parent
SERIES = R.parent / "foodeatup-social" / "data" / "series.json"
POLICE = R / "templates" / "Poppins-800.ttf"
VOIX = R / "assets" / "vo" / "punchlines"
SANS_VOIX = R / "assets" / "hooks-sans-voix"
SORTIE = R / "dist" / "stories"

L, H = 1080, 1920
DUREE = 10.0

# Les cinq minutages de la consigne. Ils ne se déduisent pas les uns des autres :
# ce sont des décisions de montage, et les changer change le rythme de la fin.
T_VOILE, D_VOILE = 8.5, 0.3
T_LOGO, D_LOGO = 8.8, 0.3
T_MOTS, PAS_MOT = 9.1, 0.06
T_SUITE, D_SUITE = 9.6, 0.35

MARINE = "0x0F1A23"      # le fond du générique du film
CREME = "0xFCF9E6"       # la punchline
ORANGE = "0xFFA500"      # « à suivre »

# Le voile occupe le tiers inférieur, et se fond sur trois cent quarante pixels.
# Première version : un dégradé de cent quatre-vingts pixels à 94 %. Il tenait la
# lisibilité et tuait le plan — un pavé noir en travers d'une cuisine de cinéma,
# qu'on voit avant de voir le texte. Un générique de film pose une barre, il ne
# masque pas l'image.
#
# Instagram couvre les deux cent cinquante derniers pixels de son interface :
# tout ce qui se lit se tient au-dessus de 1620, et le bas du voile reste vide.
VOILE_H = 680
VOILE_Y = H - VOILE_H
VOILE_FONDU = 190
VOILE_COURBE = 1.6
VOILE_OPACITE = 0.90

# Tout le générique tient entre 1420 et 1640 — c'est-à-dire dans la partie du
# voile qui est déjà pleine, et au-dessus des 250 derniers pixels que couvre
# l'interface d'Instagram. La contrainte est étroite : elle décide la taille de
# la marque autant que celle du texte.
LOGO_W = 240
LOGO_Y = 1420
MOTS_Y = 1508
MOTS_TAILLE = 42
MOTS_INTERLIGNE = 50
SUITE_Y = 1608
SUITE_TAILLE = 30
MARGE = 80
FLECHE_W, FLECHE_H = 26, 20
FLECHE_AVANCE = 8


def sortie(x, duree, t0):
    """Décélération cubique — l'entrée d'un élément qui se pose."""
    x = f"min(1,max(0,(t-{t0})/{duree}))"
    return f"(1-pow(1-{x},3))"


def rebond(duree, t0):
    """Décélération avec dépassement de 6 %, puis retour.

    e(x) = 1 + 2,3·(x−1)³ + 1,3·(x−1)²  culmine à 1,062 en x = 0,377. Les deux
    coefficients ne sont pas ronds parce que le dépassement, lui, l'est : la
    consigne dit six pour cent, et c'est le couple qui les donne.
    """
    u = f"(min(1,max(0,(t-{t0})/{duree}))-1)"
    return f"(1+2.3*pow({u},3)+1.3*pow({u},2))"


def apparait(t0, duree=0.12):
    """Alpha qui monte et ne redescend jamais — rien ne disparaît avant la fin."""
    return f"min(1,max(0,(t-{t0})/{duree}))"


def gabarits():
    """Le voile, la marque et la flèche, dessinés une fois pour les trente-cinq."""
    from PIL import Image, ImageDraw, ImageFont

    d = R / "build" / "film"
    d.mkdir(parents=True, exist_ok=True)
    voile, marque, fleche = d / "voile.png", d / "marque.png", d / "fleche.png"

    if not voile.exists():
        # Opaque là où le texte se pose, éteint sur le haut : une arête nette en
        # travers d'un plan de cinéma se voit au premier coup d'œil, et une fois
        # vue on ne voit plus qu'elle.
        #
        # Le fondu est cent quatre-vingt-dix pixels, pas trois cent quarante.
        # Un fondu long est plus doux et laisse la marque se poser sur une
        # demi-transparence : au premier essai, le mot-symbole du film tombait
        # sur celui imprimé sur le tablier du chef et les deux se lisaient l'un
        # à travers l'autre. Le voile doit être plein là où on écrit.
        img = Image.new("RGBA", (1, VOILE_H))
        px = img.load()
        for y in range(VOILE_H):
            t = min(1.0, y / VOILE_FONDU)
            px[0, y] = (0x0F, 0x1A, 0x23, int(255 * VOILE_OPACITE * pow(t, VOILE_COURBE)))
        img.resize((L, VOILE_H), Image.BICUBIC).save(voile)

    if not marque.exists():
        # `templates/logo_foodeatup.png` est un badge : un rectangle bleu vif
        # bordé de blanc, dessiné pour le fond sable des masters. Posé sur le
        # marine du générique, il se lit comme un autocollant collé sur la
        # pellicule. Le film reprend le même mot-symbole — le F et le bloc
        # DEATUP en crème, les deux O en orange — sans la boîte, dans les deux
        # couleurs du générique. Même marque, autre support.
        f = ImageFont.truetype(str(POLICE), 96)
        bouts = [("F", CREME), ("OO", ORANGE), ("DEATUP", CREME)]
        largeurs = [f.getlength(t) for t, _ in bouts]
        img = Image.new("RGBA", (int(sum(largeurs)) + 8, 130), (0, 0, 0, 0))
        g, x = ImageDraw.Draw(img), 4
        for (txt, col), w in zip(bouts, largeurs):
            g.text((x, 8), txt, font=f,
                   fill=tuple(int(col[2 + i:4 + i], 16) for i in (0, 2, 4)) + (255,))
            x += w
        img.crop(img.getbbox()).save(marque)

    if not fleche.exists():
        img = Image.new("RGBA", (FLECHE_W, FLECHE_H), (0, 0, 0, 0))
        g = ImageDraw.Draw(img)
        g.polygon([(0, 2), (FLECHE_W - 8, 2), (FLECHE_W - 8, 0),
                   (FLECHE_W, FLECHE_H // 2),
                   (FLECHE_W - 8, FLECHE_H), (FLECHE_W - 8, FLECHE_H - 2), (0, FLECHE_H - 2)],
                  fill=(0xFF, 0xA5, 0x00, 255))
        img.save(fleche)

    return voile, marque, fleche


def placer(texte, taille, largeur_max):
    """Chaque mot, avec sa ligne et son abscisse — lignes centrées.

    On mesure au lieu de laisser `drawtext` faire : il ne sait pas où finit le
    mot précédent, et un `x` calculé au jugé donne des mots qui se chevauchent
    sur les punchlines longues et un bloc décentré sur les courtes.
    """
    from PIL import ImageFont

    f = ImageFont.truetype(str(POLICE), taille)
    espace = f.getlength(" ")

    lignes, courante, large = [], [], 0.0
    for mot in texte.split():
        w = f.getlength(mot)
        ajout = w if not courante else espace + w
        if courante and large + ajout > largeur_max:
            lignes.append((courante, large))
            courante, large = [mot], w
        else:
            courante.append(mot)
            large += ajout
    if courante:
        lignes.append((courante, large))

    places, n = [], 0
    for i, (mots, large) in enumerate(lignes):
        x = (L - large) / 2
        for mot in mots:
            places.append((mot, round(x), MOTS_Y + i * MOTS_INTERLIGNE, n))
            x += f.getlength(mot) + espace
            n += 1
    return places


def largeur(texte, taille):
    from PIL import ImageFont
    return ImageFont.truetype(str(POLICE), taille).getlength(texte)


def a_du_son(f):
    out = subprocess.run(
        ["ffprobe", "-v", "error", "-select_streams", "a",
         "-show_entries", "stream=codec_type", "-of", "csv=p=0", str(f)],
        capture_output=True, text=True).stdout.strip()
    return bool(out)


def fin_de_parole(mp3, plancher_db=-45.0, pas=0.02):
    """L'instant où la voix se tait vraiment, silence de queue exclu.

    La durée du fichier ne dit pas où s'arrête la phrase : un rendu
    ElevenLabs traîne deux à cinq dixièmes de silence après le dernier mot.
    Caler sur la durée du fichier reculerait donc l'entrée de la voix pour
    rien, et ferait mordre le dernier mot sur le plan au lieu de le poser
    sur l'image finale.
    """
    # `silencedetect` écrit son relevé en niveau info : le museler avec
    # « -v error », comme partout ailleurs ici, rend la sortie vide et la
    # mesure silencieusement fausse.
    out = subprocess.run(
        ["ffmpeg", "-hide_banner", "-nostats", "-i", str(mp3),
         "-af", f"silencedetect=noise={plancher_db}dB:d={pas}", "-f", "null", "-"],
        capture_output=True, text=True).stderr
    duree = float(subprocess.run(
        ["ffprobe", "-v", "error", "-show_entries", "format=duration",
         "-of", "csv=p=0", str(mp3)], capture_output=True, text=True).stdout.strip())

    # Le silence de queue est celui qui court jusqu'au bout du fichier : soit
    # ffmpeg le referme sur la dernière frame, soit il ne le referme pas du
    # tout. Les silences du milieu — les respirations entre deux mots — ont,
    # eux, une fin franchement antérieure et ne disent rien de la fin.
    debuts = [float(m) for m in re.findall(r"silence_start: (-?[\d.]+)", out)]
    fins = [float(m) for m in re.findall(r"silence_end: ([\d.]+)", out)]
    if debuts:
        jusquau_bout = not fins or fins[-1] < debuts[-1] or fins[-1] >= duree - 0.05
        if jusquau_bout:
            return min(debuts[-1] + 0.05, duree)
    return duree


def generique(clip, punchline, a_suivre, voix, dest):
    voile, marque, fleche = gabarits()
    muet = not a_du_son(clip)
    fics = []

    def fichier(txt):
        f = tempfile.NamedTemporaryFile("w", suffix=".txt", delete=False,
                                        encoding="utf-8")
        f.write(txt)
        f.close()
        fics.append(f.name)
        return f.name

    police = str(POLICE).replace(":", r"\:")
    entrees = ["-i", str(clip), "-i", str(marque),
               "-loop", "1", "-t", str(DUREE), "-i", str(voile),
               "-loop", "1", "-t", str(DUREE), "-i", str(fleche)]
    i_silence = i_voix = i_ambiance = None

    # ffmpeg numérote ses entrées dans l'ordre des « -i », pas dans celui des
    # mots de la ligne de commande : `-loop 1 -t 10 -i x` en pèse six. Compter
    # les drapeaux est donc la seule façon juste de nommer l'entrée suivante.
    suivante = entrees.count("-i")

    # L'ambiance sans la voix du plan, quand enlever-voix.py l'a produite.
    # Seedance prononce les répliques du prompt : sans ce retrait, sa voix se
    # superpose à la punchline ElevenLabs et on en entend deux. À défaut, on
    # garde le son d'origine — le montage sonne moins bien mais ne casse pas.
    sans_voix = SANS_VOIX / f"{clip.stem}.m4a"
    if sans_voix.exists():
        i_ambiance = suivante
        suivante += 1
        entrees += ["-i", str(sans_voix)]
        muet = False
    elif muet:
        i_silence = suivante
        suivante += 1
        entrees += ["-f", "lavfi", "-t", str(DUREE), "-i", "anullsrc=r=48000:cl=stereo"]
    if voix:
        i_voix = suivante
        entrees += ["-i", str(voix)]

    g = [
        f"[0:v]scale={L}:{H}:force_original_aspect_ratio=increase,"
        f"crop={L}:{H},setsar=1,fps=30,trim=0:{DUREE},setpts=PTS-STARTPTS[v0]",

        # 8,5 s — le voile monte du bas sur le tiers inférieur.
        f"[2:v]format=rgba[voile]",
        f"[v0][voile]overlay=0:'{H}-{VOILE_H}*{sortie('', D_VOILE, T_VOILE)}':"
        f"enable='gte(t,{T_VOILE})'[v1]",

        # 8,8 s — le logo arrive du bas, dépasse de 6 %, revient.
        f"[1:v]scale={LOGO_W}:-1[logo]",
        f"[v1][logo]overlay=(W-w)/2:'{H}-({H}-{LOGO_Y})*{rebond(D_LOGO, T_LOGO)}':"
        f"enable='gte(t,{T_LOGO})'[v2]",
    ]

    # 9,1 s — la punchline, un mot toutes les 0,06 s.
    flux = "v2"
    for mot, x, y, n in placer(punchline, MOTS_TAILLE, L - 2 * MARGE):
        suivant = f"m{n}"
        g.append(
            f"[{flux}]drawtext=fontfile='{police}':textfile='{fichier(mot)}':"
            f"fontsize={MOTS_TAILLE}:fontcolor={CREME}:x={x}:y={y}:"
            f"shadowcolor=black@0.4:shadowx=0:shadowy=2:"
            f"alpha='{apparait(T_MOTS + n * PAS_MOT)}'[{suivant}]"
        )
        flux = suivant

    # 9,6 s — « à suivre » à droite, sa flèche avance de 8 px et s'arrête.
    lx = largeur(a_suivre, SUITE_TAILLE)
    x_texte = round(L - MARGE - lx)
    x_fleche = round(x_texte - FLECHE_W - 14 - FLECHE_AVANCE)
    g.append(
        f"[{flux}]drawtext=fontfile='{police}':textfile='{fichier(a_suivre)}':"
        f"fontsize={SUITE_TAILLE}:fontcolor={ORANGE}:x={x_texte}:y={SUITE_Y}:"
        f"alpha='{apparait(T_SUITE)}'[s1]"
    )
    g.append(
        f"[3:v]format=rgba,colorchannelmixer=aa='{apparait(T_SUITE)}'[fl]"
        if False else
        f"[3:v]format=rgba[fl]"
    )
    g.append(
        f"[s1][fl]overlay="
        f"'{x_fleche}+{FLECHE_AVANCE}*{sortie('', D_SUITE, T_SUITE)}':"
        f"{SUITE_Y + 6}:enable='gte(t,{T_SUITE})'[vout]"
    )

    # Le son. La voix de la punchline entre à 8,5 s ; le plan s'efface de 9 dB
    # derrière elle au lieu de se taire — une ambiance qui disparaît d'un coup
    # sous une voix off s'entend comme une erreur de montage.
    piste = (f"{i_ambiance}:a" if i_ambiance is not None
             else f"{i_silence}:a" if muet else "0:a")
    if i_voix is not None:
        # La voix se cale sur la FIN, pas sur le voile. Entrer à 8,5 s ne lui
        # laisse qu'une seconde et demie ; les punchlines dites font deux à
        # trois secondes, et les six premières mesurées perdaient de 22 à 49 %
        # de leur phrase, coupées en plein mot par le atrim de fin.
        #
        # On recule donc son entrée juste ce qu'il faut pour que le dernier mot
        # tombe sur la dernière image. Rien n'est coupé, et une réplique qui
        # s'achève sur l'image figée est la fin qu'appelle un « à suivre ».
        # Le prix payé est assumé : sur une punchline longue la voix commence
        # avant que le voile ne monte, donc un peu avant le générique.
        t_voix = max(0.0, DUREE - fin_de_parole(voix))
        # L'ambiance s'efface DERRIÈRE la voix : le fondu suit son entrée réelle
        # et non plus le voile, sans quoi une voix entrée avant 8,5 s passerait
        # sous une ambiance encore à plein niveau.
        t_duck = min(T_VOILE, t_voix)
        g.append(f"[{piste}]aresample=48000,atrim=0:{DUREE},asetpts=PTS-STARTPTS,"
                 f"volume='if(lt(t,{t_duck}),1,0.355)':eval=frame[amb]")
        g.append(f"[{i_voix}:a]aresample=48000,adelay={int(t_voix * 1000)}|{int(t_voix * 1000)},"
                 f"atrim=0:{DUREE},asetpts=PTS-STARTPTS[vx]")
        g.append("[amb][vx]amix=inputs=2:duration=first:normalize=0,"
                 f"loudnorm=I=-14:TP=-1:LRA=11,alimiter=limit=0.794:level=disabled,"
                 f"apad,atrim=0:{DUREE}[aout]")
    else:
        g.append(f"[{piste}]aresample=48000,atrim=0:{DUREE},asetpts=PTS-STARTPTS,"
                 f"loudnorm=I=-14:TP=-1:LRA=11,alimiter=limit=0.794:level=disabled,"
                 f"apad,atrim=0:{DUREE}[aout]")

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


def controle(dest):
    out = subprocess.run(
        ["ffprobe", "-v", "error", "-show_entries",
         "stream=codec_type,width,height:format=duration",
         "-of", "json", str(dest)], capture_output=True, text=True).stdout
    d = json.loads(out)
    duree = float(d["format"]["duration"])
    v = [s for s in d["streams"] if s["codec_type"] == "video"][0]
    a = [s for s in d["streams"] if s["codec_type"] == "audio"]
    ok = (abs(duree - DUREE) < 0.3 and v["width"] == L and v["height"] == H
          and len(a) == 1)
    return ok, f"{duree:.2f}s {v['width']}x{v['height']} {'son' if a else 'MUET'}"


def chapitres():
    """Les épisodes du film : dix secondes, et un générique de fin à poser."""
    d = json.load(open(SERIES, encoding="utf-8"))
    return {
        e["id"]: e
        for s in d["series"] for sa in s["saisons"] for e in sa["episodes"]
        if e.get("dureeSecondes") == 10.0 and ((e.get("story") or {}).get("motion"))
    }


def main(cibles):
    eps = chapitres()
    SORTIE.mkdir(parents=True, exist_ok=True)

    if not cibles:
        cibles = [k for k in sorted(eps)
                  if (R / "assets" / "hooks" / f"{k}.mp4").exists()]

    faits = rates = sautes = sans_voix = 0
    for ep in cibles:
        e = eps.get(ep)
        clip = R / "assets" / "hooks" / f"{ep}.mp4"
        dest = SORTIE / f"{ep}.mp4"
        if not e:
            print(f"  {ep}  n'est pas un chapitre du film")
            sautes += 1
            continue
        if not clip.exists():
            print(f"  {ep}  pas de plan")
            sautes += 1
            continue
        if dest.exists() and dest.stat().st_size > 0:
            print(f"  {ep}  déjà monté")
            sautes += 1
            continue

        m = e["story"]["motion"]
        voix = next((VOIX / f"{ep}{x}" for x in (".mp3", ".wav", ".m4a")
                     if (VOIX / f"{ep}{x}").exists()), None)
        if not voix:
            sans_voix += 1
        try:
            generique(clip, m["punchline"], m["aSuivre"], voix, dest)
            ok, detail = controle(dest)
            print(f"  {ep}  {'monté ' if ok else 'REJETÉ'} {detail}"
                  f"{'' if voix else '  (sans la voix de la punchline)'}")
            faits += 1 if ok else 0
            rates += 0 if ok else 1
        except subprocess.CalledProcessError as err:
            print(f"  {ep}  ÉCHEC ffmpeg\n{err.stderr[-500:]}")
            rates += 1

    print(f"\nmontés : {faits} | déjà là : {sautes} | en échec : {rates}")
    if sans_voix:
        print(f"{sans_voix} sans voix de punchline — déposer les mp3 dans "
              f"assets/vo/punchlines/ et relancer après avoir supprimé le fichier monté.")
    return 1 if rates else 0


if __name__ == "__main__":
    sys.exit(main(sys.argv[1:]))
