#!/usr/bin/env python3
"""Assemble le film UpEatFood à partir de ses chapitres.

    python3 scripts/build-film.py              (tout ce qui est disponible)
    python3 scripts/build-film.py --liste       (dit ce qui manque, ne monte rien)

Ce que ce script n'est pas
--------------------------
Ce n'est pas `build-film-stories.py`. Celui-là fabrique une story de dix
secondes par chapitre, avec un générique « à suivre » qui monte à 8,5 s : un
objet fait pour un fil, où chaque chapitre doit tenir seul et renvoyer au
suivant. Enchaînés, ces génériques donneraient trente-cinq fins de film à la
suite.

Ici on fait l'inverse : les plans bruts, bout à bout, sans rien entre eux qu'un
carton de saison. C'est le film.

Le cadre
--------
Les plans sont verticaux et le restent — les recadrer en 16:9 couperait le
visage ou le plan de travail. Ils sont posés en pleine hauteur au centre d'un
cadre 1920 × 1080, les côtés comblés par une copie floutée du plan. C'est le
traitement déjà retenu pour les vidéos YouTube paysage et pour les vignettes
16:9 : le film ressemble au reste de la série.

Le 16:9 parce que ce film a deux destinations, la page d'accueil du site et
YouTube, et que les deux sont en paysage.

Le son
------
Deux générations de plans cohabitent, et elles ne sonnent pas pareil.

Les plans d'avant la réécriture Seedance 2.5 portent une voix française
incrustée : Seedance prononçait les répliques écrites dans le prompt. Ceux
d'après ne portent qu'une ambiance — le prompt interdit désormais toute voix,
précisément pour que la voix vienne d'ElevenLabs au montage.

Monter les uns après les autres donnerait un film à moitié raconté. On prend
donc partout la piste sans voix quand elle existe (`assets/hooks-sans-voix/`,
produite par Demucs) et l'ambiance seule sinon. Le film sort avec son ambiance
et sans narration ; la narration se pose ensuite, en une passe, sur toute la
durée. `--narration` prend un fichier audio et le mixe par-dessus.
"""
import argparse
import json
import pathlib
import subprocess
import sys
import tempfile

R = pathlib.Path(__file__).resolve().parent.parent
SERIES = R.parent / "foodeatup-social" / "data" / "series.json"
POLICE = R / "templates" / "Poppins-800.ttf"
LOGO = R / "templates" / "logo_foodeatup.png"
SORTIE = R / "dist" / "film"

L, H = 1920, 1080
LARGEUR_PLAN = (H * 9 // 16 + 1) // 2 * 2      # 608, comme en YouTube paysage
SABLE = "0xFAF6E3"
ENCRE = "0x0F1A23"
SERIE = "il-etait-une-fois-un-restaurant"

T_LOGO = 4.0       # le logo de marque, avant tout le reste
T_TITRE = 3.5      # le carton d'ouverture
T_SAISON = 2.0     # un carton par saison
T_FIN = 4.5        # le générique
FONDU = 0.5

# La musique d'ouverture.
#
# C'est `templates/bgm.mp3`, celle des masters de 37,5 s — la série a déjà son
# thème, il n'y a aucune raison d'en poser un autre sur le film qui la résume.
#
# Elle couvre le logo et le carton de titre, puis descend sous le premier plan
# et s'éteint : au-delà, c'est l'ambiance des lieux qui porte le film, et une
# nappe continue sur six minutes finirait par tout aplatir.
BGM = R / "templates" / "bgm.mp3"
T_BGM = T_LOGO + T_TITRE + 4.0     # elle déborde de quatre secondes sur le film
BGM_FONDU_SORTIE = 3.0


def duree(f):
    out = subprocess.run(
        ["ffprobe", "-v", "error", "-show_entries", "format=duration",
         "-of", "csv=p=0", str(f)], capture_output=True, text=True).stdout
    return float(out.strip())


def chapitres():
    """Les chapitres du film, dans l'ordre de diffusion, avec leurs sources.

    L'ordre est celui de l'inventaire : saison par saison, épisode par épisode.
    C'est l'ordre du récit — le film ouvre en cuisine et se referme sur la
    façade — et il n'y a aucune raison d'en inventer un autre ici.
    """
    d = json.loads(SERIES.read_text(encoding="utf-8"))
    serie = next(s for s in d["series"] if s["slug"] == SERIE)
    for sa in serie["saisons"]:
        chap = []
        for e in sa["episodes"]:
            i = e["id"]
            # `assets/hooks/` porte ce qui vient d'être récupéré, `dist/hooks/`
            # la copie commitée. On prend le premier qui répond.
            video = next((p for p in (R / "assets" / "hooks" / f"{i}.mp4",
                                      R / "dist" / "hooks" / f"{i}.mp4")
                          if p.exists()), None)
            if not video:
                continue
            # La piste sans voix quand Demucs est passé, sinon celle du plan.
            sans_voix = R / "assets" / "hooks-sans-voix" / f"{i}.m4a"
            chap.append({"id": i, "titre": e["titre"], "video": video,
                         "audio": sans_voix if sans_voix.exists() else None,
                         "voix": (e.get("voixOff") or {})})
        yield sa, chap


def carton(texte, sous_titre, secondes, dest, corps=96, avec_logo=False):
    """Un carton de charte, fabriqué à la volée."""
    fics = []

    def fichier(txt):
        f = tempfile.NamedTemporaryFile("w", suffix=".txt", delete=False,
                                        encoding="utf-8")
        f.write(txt)
        f.close()
        fics.append(f.name)
        return f.name

    police = str(POLICE).replace(":", r"\:")
    y_titre = H // 2 - (110 if sous_titre else 55)
    dessins = [
        f"drawtext=fontfile='{police}':textfile='{fichier(texte)}':"
        f"fontcolor={ENCRE}:fontsize={corps}:x=(w-text_w)/2:y={y_titre}:"
        f"alpha='min(1,t/{FONDU})'"
    ]
    if sous_titre:
        dessins.append(
            f"drawtext=fontfile='{police}':textfile='{fichier(sous_titre)}':"
            f"fontcolor={ENCRE}:fontsize=44:x=(w-text_w)/2:y={y_titre + corps + 60}:"
            f"alpha='min(1,max(0,t-0.3)/{FONDU})'")

    g = [f"[0:v]scale={L}:{H},setsar=1,fps=30," + ",".join(dessins) + "[c]"]
    entrees = ["-f", "lavfi", "-t", str(secondes),
               "-i", f"color=c={SABLE}:s={L}x{H}:r=30"]
    sortie_v = "[c]"
    if avec_logo:
        entrees += ["-i", str(LOGO)]
        g += ["[1:v]scale=300:-1[logo]",
              f"[c][logo]overlay=(W-w)/2:{y_titre + corps + 150}[cv]"]
        sortie_v = "[cv]"

    # Un carton muet casserait le montage à la concaténation : on lui donne
    # une piste silencieuse au même format que celle des plans.
    entrees += ["-f", "lavfi", "-t", str(secondes),
                "-i", "anullsrc=r=48000:cl=stereo"]
    cmd = (["ffmpeg", "-v", "error", "-y"] + entrees
           + ["-filter_complex", ";".join(g), "-map", sortie_v,
              "-map", f"{2 if avec_logo else 1}:a",
              "-c:v", "libx264", "-preset", "medium", "-crf", "20",
              "-pix_fmt", "yuv420p", "-r", "30",
              "-c:a", "aac", "-b:a", "192k", "-ar", "48000", str(dest)])
    try:
        subprocess.run(cmd, check=True, capture_output=True, text=True)
    finally:
        for f in fics:
            pathlib.Path(f).unlink(missing_ok=True)


def logo_anime(dest):
    """Le logo de marque, façon générique de studio.

    Le mouvement est celui qu'on voit avant un film : le logo entre déjà à
    l'écran, un peu trop grand, et se pose. Pas de translation, pas de rebond —
    ce qui donne l'impression de cinéma, c'est la lenteur et le fait que le
    mouvement s'arrête avant que l'image ne parte.

    Fabrication : on compose d'abord le logo sur le fond de charte en une image
    fixe, puis on zoome cette image entière. Zoomer le fond n'a aucun effet
    visible — il est uni — et ça évite `overlay`, qui ne sait pas redimensionner
    au fil du temps. La plaque est rendue en 3840 de large pour que le logo
    reste net une fois le zoom retombé à 1.
    """
    plaque = R / "build" / "film" / "plaque-logo.png"
    plaque.parent.mkdir(parents=True, exist_ok=True)
    if not plaque.exists():
        subprocess.run(
            ["ffmpeg", "-v", "error", "-y",
             "-f", "lavfi", "-i", f"color=c={SABLE}:s={L * 2}x{H * 2}",
             "-i", str(LOGO),
             "-filter_complex",
             "[1:v]scale=760:-1[l];[0:v][l]overlay=(W-w)/2:(H-h)/2",
             "-frames:v", "1", str(plaque)],
            check=True, capture_output=True, text=True)

    # 1,4 s pour que le zoom se pose, puis l'image ne bouge plus. `on` est le
    # numéro de l'image produite : à 30 im/s, 42 images font 1,4 s.
    poses = int(1.4 * 30)
    z = f"max(1.0,1.07-0.07*min(1,on/{poses}))"
    g = (f"[0:v]zoompan=z='{z}':d=1:x='iw/2-(iw/zoom/2)':y='ih/2-(ih/zoom/2)':"
         f"s={L}x{H}:fps=30,"
         f"fade=t=in:st=0:d=0.7,fade=t=out:st={T_LOGO - 0.7}:d=0.7[v]")
    subprocess.run(
        ["ffmpeg", "-v", "error", "-y",
         "-loop", "1", "-t", str(T_LOGO), "-i", str(plaque),
         "-f", "lavfi", "-t", str(T_LOGO), "-i", "anullsrc=r=48000:cl=stereo",
         "-filter_complex", g, "-map", "[v]", "-map", "1:a",
         "-c:v", "libx264", "-preset", "medium", "-crf", "20",
         "-pix_fmt", "yuv420p", "-r", "30",
         "-c:a", "aac", "-b:a", "192k", "-ar", "48000", str(dest)],
        check=True, capture_output=True, text=True)


def plan(ch, dest):
    """Un chapitre, mis au cadre 16:9 avec son fond flou."""
    g = [
        "[0:v]split=2[fond][net]",
        f"[fond]scale={L}:{H}:force_original_aspect_ratio=increase,"
        f"crop={L}:{H},gblur=sigma=40,eq=brightness=-0.16:saturation=0.7,"
        "setsar=1,fps=30[flou]",
        f"[net]scale={LARGEUR_PLAN}:{H},setsar=1,fps=30[plan]",
        "[flou][plan]overlay=(W-w)/2:0[vout]",
    ]
    entrees = ["-i", str(ch["video"])]
    piste = "0:a"
    if ch["audio"]:
        entrees += ["-i", str(ch["audio"])]
        piste = "1:a"
    g.append(f"[{piste}]aresample=48000,aformat=channel_layouts=stereo[aout]")

    cmd = (["ffmpeg", "-v", "error", "-y"] + entrees
           + ["-filter_complex", ";".join(g), "-map", "[vout]", "-map", "[aout]",
              "-c:v", "libx264", "-preset", "medium", "-crf", "21",
              "-pix_fmt", "yuv420p", "-r", "30",
              "-c:a", "aac", "-b:a", "192k", "-ar", "48000", str(dest)])
    subprocess.run(cmd, check=True, capture_output=True, text=True)


def main(argv):
    ap = argparse.ArgumentParser()
    ap.add_argument("--liste", action="store_true",
                    help="dit ce qui est là et ce qui manque, sans monter")
    ap.add_argument("--narration", help="piste de voix off à mixer sur le film")
    args = ap.parse_args(argv)

    d = json.loads(SERIES.read_text(encoding="utf-8"))
    serie = next(s for s in d["series"] if s["slug"] == SERIE)
    total = sum(len(sa["episodes"]) for sa in serie["saisons"])

    saisons = list(chapitres())
    presents = sum(len(c) for _, c in saisons)
    if args.liste:
        for sa, chap in saisons:
            ids = {c["id"] for c in chap}
            manque = [e["id"] for e in sa["episodes"] if e["id"] not in ids]
            print(f"  S{sa['numero']} « {sa['titre']} » : {len(chap)}/"
                  f"{len(sa['episodes'])}" + (f"  manque {', '.join(manque)}" if manque else ""))
        duree_film = presents * 10 + T_TITRE + len(saisons) * T_SAISON + T_FIN
        print(f"\n{presents}/{total} chapitres — film de {duree_film:.0f} s")
        return 0

    SORTIE.mkdir(parents=True, exist_ok=True)
    build = R / "build" / "film"
    build.mkdir(parents=True, exist_ok=True)
    morceaux = []

    print("  logo animé")
    marque = build / "000-logo.mp4"
    if not marque.exists():
        logo_anime(marque)
    morceaux.append(marque)

    print("  carton d'ouverture")
    ouverture = build / "001-titre.mp4"
    carton("UpEatFood", "Il était une fois un restaurant", T_TITRE, ouverture,
           corps=120)
    morceaux.append(ouverture)

    n = 0
    for sa, chap in saisons:
        if not chap:
            continue
        n += 1
        c_saison = build / f"{n:03d}0-saison.mp4"
        print(f"  carton saison {sa['numero']} — {sa['titre']}")
        carton(sa["titre"], f"saison {sa['numero']}", T_SAISON, c_saison, corps=84)
        morceaux.append(c_saison)
        for ch in chap:
            m = build / f"{n:03d}-{ch['id']}.mp4"
            if not m.exists():
                plan(ch, m)
            print(f"    {ch['id']}  {ch['titre'][:46]}")
            morceaux.append(m)

    print("  générique de fin")
    fin = build / "999-fin.mp4"
    carton("FoodEatUp", "Le restaurant qui se gère tout seul", T_FIN, fin,
           corps=110, avec_logo=True)
    morceaux.append(fin)

    liste = build / "liste.txt"
    liste.write_text("".join(f"file '{m}'\n" for m in morceaux), encoding="utf-8")
    dest = SORTIE / "upeatfood.mp4"

    # `concat` de démuxeur plutôt que le filtre : tous les morceaux sortent
    # d'ici avec le même codec, la même cadence et le même format audio, donc
    # il n'y a rien à réencoder — l'assemblage est une copie de flux.
    cmd = ["ffmpeg", "-v", "error", "-y", "-f", "concat", "-safe", "0",
           "-i", str(liste), "-i", str(BGM)]

    # Le mixage. L'ambiance des lieux est la base ; la musique passe devant au
    # début puis s'efface ; la narration, quand elle est là, domine les deux —
    # c'est elle qu'on doit comprendre, le reste ne fait que porter.
    pistes = ["[0:a]volume=0.6[amb]",
              f"[1:a]atrim=0:{T_BGM},afade=t=in:st=0:d=1.2,"
              f"afade=t=out:st={T_BGM - BGM_FONDU_SORTIE}:d={BGM_FONDU_SORTIE},"
              f"volume=0.45,apad[mus]"]
    entrees = ["[amb]", "[mus]"]
    if args.narration:
        cmd += ["-i", args.narration]
        pistes.append("[2:a]volume=1.0[voix]")
        entrees.append("[voix]")
    pistes.append(f"{''.join(entrees)}amix=inputs={len(entrees)}:"
                  f"duration=first:normalize=0[mix]")
    # Le film sort à -34 dB en ambiance seule ; c'est ici, une fois toutes les
    # pistes réunies, qu'on cale le niveau — le faire plus tôt amplifierait le
    # souffle d'une piste qui n'est pas encore le film.
    pistes.append("[mix]loudnorm=I=-16:TP=-1.5:LRA=11,"
                  "alimiter=limit=0.794:level=disabled[aout]")

    cmd += ["-filter_complex", ";".join(pistes),
            "-map", "0:v", "-map", "[aout]",
            "-c:v", "copy", "-c:a", "aac", "-b:a", "192k",
            "-movflags", "+faststart", str(dest)]
    subprocess.run(cmd, check=True, capture_output=True, text=True)

    print(f"\n{dest}  {duree(dest):.1f} s  {presents}/{total} chapitres")
    return 0


if __name__ == "__main__":
    sys.exit(main(sys.argv[1:]))
