#!/usr/bin/env python3
"""Monte les Shorts YouTube à partir des stories déjà montées.

    python3 scripts/build-youtube.py            (tous ceux qui manquent)
    python3 scripts/build-youtube.py EP001 EP002

Pourquoi un format de plus
--------------------------
Les quatre autres réseaux poussent la vidéo dans un fil : on la croise. YouTube
est le seul où quelqu'un la cherche — il tape une question, il lit un titre, il
choisit. `gen-publications.py` en tient déjà compte côté texte, avec un titre
qui porte la requête et une description longue. Côté image, il manquait la
contrepartie : un plan qui dise de quelle série vient ce qu'on vient de voir,
et où trouver la suite.

D'où le carton de fin. La story s'arrête sur sa punchline, ce qui est juste
dans un fil qui défile tout seul ; sur YouTube elle s'arrête sur rien. Deux
secondes et demie de plus suffisent à poser le titre de l'épisode, la série, et
la chaîne.

Ce que le script ne refait pas
------------------------------
Le montage. La story porte déjà le clip Higgsfield, le hook, la punchline et le
son du plan — tout cela a été réglé une fois, il n'y a aucune raison de le
rejouer différemment ici. Le Short est donc la story, plus un carton. Un
épisode sans story n'a pas de Short : le script le dit et passe.

Le son du carton est celui de la story, prolongé en silence et fondu : couper
net à la dixième seconde s'entend, et YouTube coupe rarement la lecture
exactement là.
"""
import json
import pathlib
import subprocess
import sys
import tempfile
import textwrap

R = pathlib.Path(__file__).resolve().parent.parent
SERIES = R.parent / "foodeatup-social" / "data" / "series.json"
POLICE = R / "templates" / "Poppins-800.ttf"
LOGO = R / "templates" / "logo_foodeatup.png"
STORIES = R / "dist" / "stories"
BANDES = R / "dist" / "bandes-annonces"
SORTIE = R / "dist" / "youtube"

L, H = 1080, 1920
CARTON = 2.5           # la durée du carton de fin
FONDU = 0.4            # entrée du carton, et sortie du son
SABLE = "0xFAF6E3"     # le fond de charte, relevé sur le master de référence
ENCRE = "0x0F1A23"
MARGE = 100


def coupe(texte, largeur):
    """Le texte à la bonne largeur — drawtext ne sait pas revenir à la ligne."""
    return "\n".join(textwrap.wrap(texte, largeur)) or texte


def duree(f):
    out = subprocess.run(
        ["ffprobe", "-v", "error", "-show_entries", "format=duration",
         "-of", "csv=p=0", str(f)], capture_output=True, text=True).stdout
    return float(out.strip())


def episodes():
    """Les épisodes du site, à plat, avec leur série et leur saison."""
    d = json.loads(SERIES.read_text(encoding="utf-8"))
    return {e["id"]: {"episode": e, "serie": s["nom"], "saison": sa["numero"]}
            for s in d["series"] for sa in s["saisons"] for e in sa["episodes"]}


def bandes_annonces():
    """Les bandes-annonces de saison, indexées par leur clé de fichier.

    Elles n'ont pas de story — elles sont déjà un montage complet — mais elles
    ont le même besoin qu'un épisode sur YouTube : dire de quoi il s'agit et où
    trouver la suite. Le carton porte alors le titre de la saison plutôt que
    celui d'un épisode.
    """
    d = json.loads(SERIES.read_text(encoding="utf-8"))
    return {f"{s['slug']}-S{sa['numero']}":
            {"titre": sa["titre"], "serie": s["nom"], "saison": sa["numero"]}
            for s in d["series"] for sa in s["saisons"] if sa.get("bandeAnnonce")}


def monte(titre_carton, fiche, source, dest):
    """La vidéo source, puis le carton de fin."""
    fics = []

    def fichier(txt):
        # drawtext prend son texte dans un fichier plutôt que sur la ligne de
        # commande : une apostrophe au milieu d'un titre casse le filtre, et
        # les titres en sont pleins. Même raison que build-stories.py.
        f = tempfile.NamedTemporaryFile("w", suffix=".txt", delete=False,
                                        encoding="utf-8")
        f.write(txt)
        f.close()
        fics.append(f.name)
        return f.name

    police = str(POLICE).replace(":", r"\:")
    d_story = duree(source)
    total = d_story + CARTON

    # Les titres vont de dix à soixante-deux caractères. À corps fixe, le plus
    # long déborderait du cadre ; on descend d'un cran au-delà de deux lignes
    # plutôt que de rogner le titre, qui est ce que le carton vient dire.
    lignes = coupe(titre_carton, 22).count("\n") + 1
    corps = 76 if lignes <= 2 else 62
    inter = corps + 16

    # Le bloc est empilé à partir de la hauteur réelle du titre, pas posé à des
    # ordonnées fixes : à trois lignes, un titre calé sur une constante venait
    # toucher la ligne de série. L'ensemble est ensuite centré dans le cadre.
    h_titre = lignes * inter
    h_bloc = h_titre + 140 + 48 + 90 + 100 + 110 + 56
    haut = (H - h_bloc) // 2
    y_serie = haut + h_titre + 140
    y_logo = y_serie + 48 + 90
    y_chaine = y_logo + 100 + 110

    titre = fichier(coupe(titre_carton, 22 if lignes <= 2 else 26))
    serie = fichier(f"{fiche['serie']} · saison {fiche['saison']}")
    chaine = fichier("@FoodEatUp")

    g = [
        # La story telle quelle, puis le carton : deux sources vidéo bout à
        # bout, la seconde fabriquée à la volée.
        f"[0:v]scale={L}:{H},setsar=1,fps=30[v0]",
        f"[1:v]scale={L}:{H},setsar=1,fps=30,"
        f"drawtext=fontfile='{police}':textfile='{titre}':fontcolor={ENCRE}:"
        f"fontsize={corps}:line_spacing=16:x=(w-text_w)/2:y={haut}:"
        f"box=0:alpha='min(1,(t)/{FONDU})',"
        f"drawtext=fontfile='{police}':textfile='{serie}':fontcolor={ENCRE}:"
        f"fontsize=38:x=(w-text_w)/2:y={y_serie}:alpha='min(1,(t)/{FONDU})',"
        f"drawtext=fontfile='{police}':textfile='{chaine}':fontcolor={ENCRE}:"
        f"fontsize=46:x=(w-text_w)/2:y={y_chaine}:alpha='min(1,max(0,(t-0.4))/{FONDU})'[c0]",
        f"[2:v]scale=260:-1[logo]",
        f"[c0][logo]overlay=(W-w)/2:{y_logo}[carton]",
        f"[v0][carton]concat=n=2:v=1:a=0[vout]",

        # Le son de la story meurt dans le carton, il ne s'y arrête pas. Le
        # fondu se place donc à la fin de la story — c'est là qu'il y a encore
        # du son à baisser — et non à la fin du fichier, où `apad` n'a mis que
        # du silence : fondre du silence ne fond rien, et l'ambiance du lieu
        # coupait net à la dixième seconde.
        f"[0:a]aresample=48000,afade=t=out:st={d_story - 0.7}:d=0.7,"
        f"apad,atrim=0:{total},asetpts=PTS-STARTPTS[aout]",
    ]

    cmd = ["ffmpeg", "-v", "error", "-y",
           "-i", str(source),
           "-f", "lavfi", "-t", str(CARTON), "-i", f"color=c={SABLE}:s={L}x{H}:r=30",
           "-i", str(LOGO),
           "-filter_complex", ";".join(g),
           "-map", "[vout]", "-map", "[aout]",
           "-c:v", "libx264", "-preset", "medium", "-crf", "20",
           "-pix_fmt", "yuv420p", "-c:a", "aac", "-b:a", "192k",
           "-movflags", "+faststart", str(dest)]
    try:
        subprocess.run(cmd, check=True, capture_output=True, text=True)
    finally:
        for f in fics:
            pathlib.Path(f).unlink(missing_ok=True)


def controle(dest):
    out = subprocess.run(
        ["ffprobe", "-v", "error", "-show_entries", "format=duration",
         "-show_entries", "stream=codec_type,width,height", "-of", "json",
         str(dest)], capture_output=True, text=True).stdout
    d = json.loads(out)
    dur = float(d["format"]["duration"])
    v = [s for s in d["streams"] if s["codec_type"] == "video"][0]
    a = [s for s in d["streams"] if s["codec_type"] == "audio"]
    ok = v["width"] == L and v["height"] == H and len(a) == 1 and dur > CARTON
    return ok, f"{dur:.2f}s {v['width']}x{v['height']} {'son' if a else 'MUET'}"


def travaux(cibles):
    """Ce qu'il y a à monter : (clé, titre du carton, fiche, source).

    Deux familles cohabitent sous le même toit. Un épisode part de sa story,
    et le carton porte le titre de l'épisode. Une bande-annonce part du
    montage de saison, et le carton porte le titre de la saison — il n'y a pas
    d'épisode à nommer, et nommer la saison est justement ce qui manque quand
    la bande-annonce se termine.
    """
    eps, bas = episodes(), bandes_annonces()
    if not cibles:
        cibles = sorted(p.stem for p in STORIES.glob("*.mp4"))
        cibles += sorted(bas)

    for cle in cibles:
        if cle in eps:
            yield cle, eps[cle]["episode"]["titre"], eps[cle], STORIES / f"{cle}.mp4"
        elif cle in bas:
            yield cle, bas[cle]["titre"], bas[cle], BANDES / f"{cle}.mp4"
        else:
            yield cle, None, None, None


def main(cibles):
    SORTIE.mkdir(parents=True, exist_ok=True)
    faits = sautes = rates = 0
    for cle, titre, fiche, source in travaux(cibles):
        dest = SORTIE / f"{cle}.mp4"
        if fiche is None:
            print(f"  {cle}  inconnu de l'inventaire")
            rates += 1
            continue
        if not source.exists():
            print(f"  {cle}  pas de montage source — rien à porter sur YouTube")
            rates += 1
            continue
        if dest.exists() and dest.stat().st_size > 0:
            print(f"  {cle}  déjà monté")
            sautes += 1
            continue
        try:
            monte(titre, fiche, source, dest)
        except subprocess.CalledProcessError as err:
            print(f"  {cle}  ÉCHEC ffmpeg — {(err.stderr or '')[-200:]}")
            dest.unlink(missing_ok=True)
            rates += 1
            continue
        ok, detail = controle(dest)
        print(f"  {cle:38s} {'monté ' if ok else 'DOUTEUX'} {detail}")
        faits += 1

    print(f"\nmontés : {faits} | déjà là : {sautes} | en échec : {rates}")


if __name__ == "__main__":
    main(sys.argv[1:])
