#!/usr/bin/env python3
"""Monte les stories Instagram : le clip Higgsfield, le hook, la punchline.

    python3 scripts/build-stories.py            tous les épisodes qui ont un clip
    python3 scripts/build-stories.py EP001 EP002

RÉCUPÉRATION ET MONTAGE SEULS. Aucun crédit dépensé : la story se fabrique à
partir du clip déjà payé, avec ffmpeg, en local.

Ce que la story N'EST PAS
-------------------------
Ce n'est pas le master raccourci. Le master de 37,5 s enchaîne cinq segments,
dont dix secondes d'avatar qui présente une fonction du logiciel. La story ne
garde que la scène comique : le clip, le hook au début, la punchline à la fin.
Pas d'avatar, pas de capture d'écran, pas de démonstration.

La raison est un fait d'usage, pas une préférence : une story se regarde le
pouce posé sur l'écran, prête à passer à la suivante. Une démonstration de
logiciel y meurt en deux secondes. La blague, elle, tient — et c'est elle qui
donne envie d'aller voir le reste.

L'anatomie
----------
    0,0 → 10,0   le clip Higgsfield, son son d'origine
    0,6 →  3,6   le hook, tiers haut
    5,6 → 10,0   la punchline, tiers bas
    tout du long  le badge FoodEatUp, au même endroit que sur le master

Le beat comique du clip tombe à 5,0 s — c'est la règle de la série. La
punchline entre juste après, à 5,6 s : elle commente la chute, elle ne
l'annonce pas. L'inverse tuerait la blague.

Le texte passe par un FICHIER
-----------------------------
Jamais en ligne dans le filtergraph. Une apostrophe referme le text='…' de
drawtext au milieu de la phrase, et vingt-trois accroches sur cent cinquante en
contiennent une. `textfile=` ne se trompe jamais. Même raison que
build-segment-a.sh, même solution.
"""
import json
import os
import pathlib
import subprocess
import sys
import tempfile
import textwrap

R = pathlib.Path(__file__).resolve().parent.parent
SERIES = R.parent / "foodeatup-social" / "data" / "series.json"
POLICE = R / "templates" / "Poppins-800.ttf"
LOGO = R / "templates" / "logo_foodeatup.png"
SORTIE = R / "dist" / "stories"

L, H = 1080, 1920
DUREE = 10.0
HOOK_IN, HOOK_OUT = 0.6, 3.6
PUNCH_IN = 5.6
FONDU = 0.35

# Marge de texte. Instagram pose son interface sur les 250 premiers et les 250
# derniers pixels : tout ce qui compte se tient à l'intérieur.
MARGE = 80

# Le badge est au même endroit que sur le master : une série se reconnaît à ce
# qui ne bouge pas d'un format à l'autre.
LOGO_X, LOGO_Y = 795, 57


def coupe(texte, largeur):
    """Le texte à la bonne largeur — drawtext ne sait pas revenir à la ligne."""
    return "\n".join(textwrap.wrap(texte.strip(), largeur)) or texte.strip()


def alpha(debut, fin):
    """Fondu d'entrée et de sortie, en une expression."""
    if fin is None:
        return (f"if(lt(t,{debut}),0,"
                f"min(1,(t-{debut})/{FONDU}))")
    return (f"if(lt(t,{debut}),0,"
            f"if(lt(t,{debut + FONDU}),(t-{debut})/{FONDU},"
            f"if(lt(t,{fin - FONDU}),1,"
            f"if(lt(t,{fin}),({fin}-t)/{FONDU},0))))")


# Le texte tient sa lisibilité tout seul.
#
# Il y a eu deux versions avant celle-ci. Un `drawbox` noir à 45 %, qui laissait
# une arête horizontale en travers du plan. Puis deux dégradés — 760 px en haut,
# 900 px en bas — sans arête, mais qui assombrissaient la moitié basse de chaque
# story : sur un plan de rue au soleil couchant, le bitume passait du doré au
# gris et on voyait le voile avant de lire la phrase.
#
# Un contour noir sur la lettre fait le même travail sans toucher au plan. Il ne
# couvre que les quelques pixels autour du glyphe, là où le contraste manque
# vraiment, au lieu d'assombrir 900 px de large pour trois lignes de texte. Du
# Poppins 800 blanc cerné de noir se lit sur un mur blanc comme sur une nappe
# claire — les deux cas qui mettaient le voile en échec de toute façon.
CONTOUR = "borderw=6:bordercolor=black@0.92"

# Où la punchline se termine, en partant du bas du cadre.
#
# Elle était posée par son sommet (`y=h-560`) : une punchline d'une ligne
# s'arrêtait 90 px plus haut qu'une punchline de deux, et le bas de la story
# sautait d'un épisode à l'autre. En ancrant le bloc par son pied, la dernière
# ligne tombe toujours au même endroit et la série se tient.
#
# 380 px laissent passer les 250 px d'interface d'Instagram, plus une marge.
PIED_PUNCH = 380
INTER_PUNCH = 70 + 16          # corps + interligne


def a_du_son(clip):
    """Le clip porte-t-il une piste audio.

    Un clip Higgsfield sur les cent vingt-deux est arrivé muet — EP001. Sans
    piste à mapper, ffmpeg s'arrête net sur « matches no streams ». On lui en
    fabrique alors une silencieuse : une story sans piste du tout se fait
    rejeter à la publication, une story silencieuse passe.
    """
    out = subprocess.run(
        ["ffprobe", "-v", "error", "-select_streams", "a",
         "-show_entries", "stream=codec_type", "-of", "csv=p=0", str(clip)],
        capture_output=True, text=True).stdout.strip()
    return bool(out)


def story(ep, hook, punch, clip, dest):
    muet = not a_du_son(clip)
    piste = "2:a" if muet else "0:a"
    fics = []

    def fichier(txt):
        f = tempfile.NamedTemporaryFile("w", suffix=".txt", delete=False,
                                        encoding="utf-8")
        f.write(txt)
        f.close()
        fics.append(f.name)
        return f.name

    f_hook = fichier(coupe(hook, 20))
    texte_punch = coupe(punch, 26)
    f_punch = fichier(texte_punch)
    police = str(POLICE).replace(":", r"\:")

    # Le bloc de punchline est posé par son pied : on remonte d'autant de
    # lignes qu'il en compte pour trouver où commencer à écrire.
    lignes_punch = texte_punch.count("\n") + 1
    y_punch = H - PIED_PUNCH - lignes_punch * INTER_PUNCH

    graphe = (
        f"[0:v]scale={L}:{H}:force_original_aspect_ratio=increase,"
        f"crop={L}:{H},setsar=1,fps=30,trim=0:{DUREE},setpts=PTS-STARTPTS[v0];"

        # Les deux textes sont calés à gauche sur la même marge. Centrer un
        # bloc de deux lignes de longueurs différentes donne un bord gauche en
        # dents de scie qu'on lit comme une erreur de montage ; une marge
        # tenue se lit comme une décision.
        f"[v0]drawtext=fontfile='{police}':textfile='{f_hook}':"
        f"fontsize=84:fontcolor=white:line_spacing=16:"
        f"x={MARGE}:y=260:{CONTOUR}:"
        f"shadowcolor=black@0.45:shadowx=0:shadowy=3:"
        f"alpha='{alpha(HOOK_IN, HOOK_OUT)}'[v2];"

        f"[v2]drawtext=fontfile='{police}':textfile='{f_punch}':"
        f"fontsize=70:fontcolor=white:line_spacing=16:"
        f"x={MARGE}:y={y_punch}:{CONTOUR}:"
        f"shadowcolor=black@0.45:shadowx=0:shadowy=3:"
        f"alpha='{alpha(PUNCH_IN, None)}'[v4];"

        f"[1:v]scale=250:-1[logo];"
        f"[v4][logo]overlay={LOGO_X}:{LOGO_Y}[vout];"

        # alimiter derrière loudnorm, pas à sa place. loudnorm en passe unique
        # vise -14 LUFS sans garantir le pic : mesuré à 0,0 dBTP sur la
        # première story, c'est-à-dire pleine échelle, ce qu'Instagram
        # réencode en distordant. Le limiteur ramène sous -1 dBTP, la même
        # borne que le contrôle du master. Réglé à -2 dBFS et non -1 :
        # l'encodeur AAC dépasse la consigne d'un demi-décibel, mesuré.
        f"[{piste}]aresample=48000,atrim=0:{DUREE},asetpts=PTS-STARTPTS,"
        f"loudnorm=I=-14:TP=-1:LRA=11,alimiter=limit=0.794:level=disabled,"
        f"apad,atrim=0:{DUREE}[aout]"
    )

    cmd = ["ffmpeg", "-v", "error", "-y",
           "-i", str(clip), "-i", str(LOGO)]
    if muet:
        cmd += ["-f", "lavfi", "-t", str(DUREE),
                "-i", "anullsrc=r=48000:cl=stereo"]
    cmd += ["-filter_complex", graphe,
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
    """Durée, dimensions, et surtout : la piste son existe-t-elle.

    Une story muette passe inaperçue à la relecture et se voit tout de suite à
    la publication. C'est le défaut qu'on vérifie, pas la beauté du cadre.
    """
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


def main(cibles):
    d = json.load(open(SERIES, encoding="utf-8"))
    eps = {e["id"]: e for s in d["series"] for sa in s["saisons"]
           for e in sa["episodes"]}
    SORTIE.mkdir(parents=True, exist_ok=True)

    # Les chapitres de UpEatFood ne passent pas par ici. Ils durent dix
    # secondes comme les autres et ont bien un clip, donc rien ne les
    # distinguait : la première passe leur a posé le hook, la punchline et le
    # badge de la série comique par-dessus un plan de cinéma. Leur générique de
    # fin est un autre montage — build-film-stories.py.
    film = {i for i, e in eps.items()
            if e.get("dureeSecondes") == 10.0 and ((e.get("story") or {}).get("motion"))}

    # Le clip source, avec repli sur ce qui est commité.
    #
    # `assets/hooks/` ne porte que les trente-quatre plans encore présents sur
    # le disque de la machine qui les a récupérés. `dist/hooks/` en porte cent
    # quatre-vingt-onze : c'est la copie commitée, celle qui survit à un
    # conteneur neuf et aux URL de CDN expirées. Sans ce repli, remonter une
    # story déjà publiée était impossible — le script répondait « pas de clip »
    # pour un épisode dont le plan est pourtant dans le dépôt.
    def source(k):
        for dossier in ("assets/hooks", "dist/hooks"):
            p = R / dossier / f"{k}.mp4"
            if p.exists():
                return p
        return None

    if not cibles:
        cibles = [k for k in sorted(eps) if k not in film and source(k)]

    faits = rates = sautes = 0
    for ep in cibles:
        if ep in film:
            print(f"  {ep}  chapitre du film — python3 scripts/build-film-stories.py {ep}")
            sautes += 1
            continue
        e = eps.get(ep)
        clip = source(ep)
        dest = SORTIE / f"{ep}.mp4"
        if not e or not clip:
            print(f"  {ep}  pas de clip")
            sautes += 1
            continue
        if dest.exists() and dest.stat().st_size > 0:
            print(f"  {ep}  déjà monté")
            sautes += 1
            continue
        try:
            story(ep, e["accroche"], e["punchline"], clip, dest)
            ok, detail = controle(dest)
            print(f"  {ep}  {'monté ' if ok else 'REJETÉ'} {detail}")
            if ok:
                faits += 1
            else:
                rates += 1
        except subprocess.CalledProcessError as err:
            print(f"  {ep}  ÉCHEC ffmpeg\n{err.stderr[-400:]}")
            rates += 1

    print(f"\nmontées : {faits} | déjà là : {sautes} | en échec : {rates}")
    return 1 if rates else 0


if __name__ == "__main__":
    sys.exit(main(sys.argv[1:]))
