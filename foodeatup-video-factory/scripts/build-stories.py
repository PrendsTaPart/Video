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


def voiles():
    """Les deux dégradés qui portent le texte, fabriqués une fois.

    Première version : un `drawbox` noir à 45 %. Il tenait la lisibilité mais
    laissait une arête horizontale nette en travers du plan — un rectangle
    sombre posé sur une cuisine, visible au premier coup d'œil et impossible à
    ignorer une fois vue.

    Un dégradé n'a pas d'arête. Opaque là où le texte se pose, transparent là
    où l'image doit rester intacte. On le fabrique en PNG plutôt qu'avec `geq`
    dans le filtergraph : calculé une fois pour cent cinquante stories au lieu
    de trente fois par seconde et par épisode.
    """
    from PIL import Image

    dossier = R / "build" / "voiles"
    dossier.mkdir(parents=True, exist_ok=True)
    haut, bas = dossier / "haut.png", dossier / "bas.png"
    if haut.exists() and bas.exists():
        return haut, bas

    for chemin, hauteur, opacite, vers_le_bas in (
            (haut, 760, 0.68, True), (bas, 900, 0.78, False)):
        img = Image.new("RGBA", (1, hauteur))
        px = img.load()
        for y in range(hauteur):
            # Courbe au carré : le dégradé reste franc là où le texte se pose
            # et s'éteint vite ensuite, au lieu de grisonner tout le plan.
            t = (1 - y / hauteur) if vers_le_bas else (y / hauteur)
            px[0, y] = (0, 0, 0, int(255 * opacite * t * t))
        img.resize((L, hauteur), Image.NEAREST).save(chemin)
    return haut, bas


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
    piste = "4:a" if muet else "0:a"
    v_haut, v_bas = voiles()
    fics = []

    def fichier(txt):
        f = tempfile.NamedTemporaryFile("w", suffix=".txt", delete=False,
                                        encoding="utf-8")
        f.write(txt)
        f.close()
        fics.append(f.name)
        return f.name

    f_hook = fichier(coupe(hook, 20))
    f_punch = fichier(coupe(punch, 26))
    police = str(POLICE).replace(":", r"\:")

    graphe = (
        f"[0:v]scale={L}:{H}:force_original_aspect_ratio=increase,"
        f"crop={L}:{H},setsar=1,fps=30,trim=0:{DUREE},setpts=PTS-STARTPTS[v0];"

        # Le voile entre et sort avec son texte : `fade` sur le canal alpha,
        # aux mêmes secondes que l'expression qui pilote le drawtext. Un voile
        # qui resterait après la disparition du texte se verrait comme une
        # tache sombre sans raison.
        f"[2:v]format=rgba,"
        f"fade=t=in:st={HOOK_IN}:d={FONDU}:alpha=1,"
        f"fade=t=out:st={HOOK_OUT - FONDU}:d={FONDU}:alpha=1[voile_h];"
        f"[v0][voile_h]overlay=0:0[v1];"

        # Les deux textes sont calés à gauche sur la même marge. Centrer un
        # bloc de deux lignes de longueurs différentes donne un bord gauche en
        # dents de scie qu'on lit comme une erreur de montage ; une marge
        # tenue se lit comme une décision.
        f"[v1]drawtext=fontfile='{police}':textfile='{f_hook}':"
        f"fontsize=84:fontcolor=white:line_spacing=16:"
        f"x={MARGE}:y=260:"
        f"shadowcolor=black@0.55:shadowx=0:shadowy=3:"
        f"alpha='{alpha(HOOK_IN, HOOK_OUT)}'[v2];"

        f"[3:v]format=rgba,"
        f"fade=t=in:st={PUNCH_IN}:d={FONDU}:alpha=1[voile_b];"
        f"[v2][voile_b]overlay=0:{H}-900[v3];"
        f"[v3]drawtext=fontfile='{police}':textfile='{f_punch}':"
        f"fontsize=70:fontcolor=white:line_spacing=16:"
        f"x={MARGE}:y=h-560:"
        f"shadowcolor=black@0.55:shadowx=0:shadowy=3:"
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
           "-i", str(clip), "-i", str(LOGO),
           "-loop", "1", "-t", str(DUREE), "-i", str(v_haut),
           "-loop", "1", "-t", str(DUREE), "-i", str(v_bas)]
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

    if not cibles:
        cibles = [k for k in sorted(eps)
                  if (R / "assets" / "hooks" / f"{k}.mp4").exists()]

    faits = rates = sautes = 0
    for ep in cibles:
        e = eps.get(ep)
        clip = R / "assets" / "hooks" / f"{ep}.mp4"
        dest = SORTIE / f"{ep}.mp4"
        if not e or not clip.exists():
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
