#!/usr/bin/env python3
"""Le moteur commun des montages « story + carton de fin ».

Trois montages partagent la même mécanique : on reprend un montage déjà fait —
la story d'un épisode, la bande-annonce d'une saison — et on lui ajoute deux
secondes et demie qui disent de quoi il s'agit et où trouver la suite. Ce qui
change d'un réseau à l'autre tient en trois choses : la taille du cadre, la
dernière ligne du carton, et le fait que le plan doive être recadré ou non.

Le reste — l'empilement du bloc de texte sur la hauteur réelle du titre, le
fondu d'entrée décalé de la dernière ligne, le fondu du son placé à la fin de
la source et non à la fin du fichier — a été réglé une fois, corrigé une fois,
et n'a aucune raison de diverger entre trois copies. Il vit donc ici.

Le carton est le même objet à chaque fois :

    titre de l'épisode (ou de la saison)
    série · saison
    logo FoodEatUp
    la ou les lignes de pied — c'est la seule chose qui distingue les réseaux
"""
import json
import pathlib
import subprocess
import tempfile
import textwrap
from dataclasses import dataclass, field

R = pathlib.Path(__file__).resolve().parent.parent
SERIES = R.parent / "foodeatup-social" / "data" / "series.json"
POLICE = R / "templates" / "Poppins-800.ttf"
LOGO = R / "templates" / "logo_foodeatup.png"
STORIES = R / "dist" / "stories"
BANDES = R / "dist" / "bandes-annonces"

CARTON = 2.5           # la durée du carton de fin
FONDU = 0.4            # entrée du carton, et sortie du son
SABLE = "0xFAF6E3"     # le fond de charte, relevé sur le master de référence
ENCRE = "0x0F1A23"


@dataclass
class Gabarit:
    """Ce qui distingue un réseau d'un autre."""

    dossier: str                  # sous-dossier de dist/
    largeur: int
    hauteur: int
    pieds: list                   # les lignes de pied du carton, de haut en bas
    corps_pied: list = field(default_factory=list)   # leur corps, ligne à ligne
    # Ce qu'on compte sous la dernière ligne de pied quand on centre le bloc.
    # Ce n'est pas une marge : c'est le talon du texte. Chaque gabarit garde le
    # sien pour que le carton retombe au pixel près là où il était déjà — deux
    # cent huit fichiers sont publiés avec ce calage.
    queue: int = 10
    # Un cadre paysage reçoit un plan vertical : il est posé en pleine hauteur
    # au centre, et les côtés sont comblés par une copie floutée du plan.
    fond_flou: bool = False
    # La largeur du titre, en caractères, avant retour à la ligne.
    coupe_titre: int = 22
    corps_titre: tuple = (76, 62)  # à deux lignes ou moins, puis au-delà
    crf: str = "20"

    @property
    def sortie(self):
        return R / "dist" / self.dossier


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
    return {e["id"]: {"titre": e["titre"], "serie": s["nom"], "saison": sa["numero"]}
            for s in d["series"] for sa in s["saisons"] for e in sa["episodes"]}


def bandes_annonces():
    """Les bandes-annonces de saison, indexées par leur clé de fichier.

    Elles n'ont pas de story — elles sont déjà un montage complet — mais elles
    ont le même besoin qu'un épisode : dire de quoi il s'agit et où trouver la
    suite. Le carton porte alors le titre de la saison.
    """
    d = json.loads(SERIES.read_text(encoding="utf-8"))
    return {f"{s['slug']}-S{sa['numero']}":
            {"titre": sa["titre"], "serie": s["nom"], "saison": sa["numero"]}
            for s in d["series"] for sa in s["saisons"] if sa.get("bandeAnnonce")}


def monte(g, titre_carton, fiche, source, dest):
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
    d_source = duree(source)
    total = d_source + CARTON
    L, H = g.largeur, g.hauteur

    # Les titres vont de dix à soixante-deux caractères. À corps fixe, le plus
    # long déborderait du cadre ; on descend d'un cran au-delà de deux lignes
    # plutôt que de rogner le titre, qui est ce que le carton vient dire.
    lignes = coupe(titre_carton, g.coupe_titre).count("\n") + 1
    corps = g.corps_titre[0] if lignes <= 2 else g.corps_titre[1]
    inter = corps + (16 if H > L else 18)

    # Le bloc est empilé à partir de la hauteur réelle du titre, pas posé à des
    # ordonnées fixes : à trois lignes, un titre calé sur une constante venait
    # toucher la ligne de série. L'ensemble est ensuite centré dans le cadre.
    ecart_serie = 140 if H > L else 90
    h_serie, h_logo, ecart_logo = 48, 100, 110
    if H < L:
        h_serie, h_logo, ecart_logo = 44, 90, 70
    corps_pieds = g.corps_pied or [46] * len(g.pieds)
    h_pieds = sum(c + 22 for c in corps_pieds[:-1]) + corps_pieds[-1] + g.queue

    h_titre = lignes * inter
    h_bloc = h_titre + ecart_serie + h_serie + (90 if H > L else 70) + h_logo \
        + ecart_logo + h_pieds
    haut = (H - h_bloc) // 2
    y_serie = haut + h_titre + ecart_serie
    y_logo = y_serie + h_serie + (90 if H > L else 70)
    y_pied = y_logo + h_logo + ecart_logo

    titre = fichier(coupe(titre_carton, g.coupe_titre if lignes <= 2 else g.coupe_titre + 4))
    serie = fichier(f"{fiche['serie']} · saison {fiche['saison']}")

    # Le plan. En portrait il remplit le cadre ; en paysage il reste vertical —
    # le recadrer couperait le sujet — et les côtés reçoivent une copie floutée
    # et assombrie, comme sur les vignettes 16:9 déjà produites.
    if g.fond_flou:
        # 1080 × 9/16 = 607,5. On arrondit au pair supérieur : libx264 refuse
        # les dimensions impaires en yuv420p, et rogner un demi-pixel de plus
        # décalerait le plan d'un pixel vers la gauche.
        largeur_plan = (H * 9 // 16 + 1) // 2 * 2
        plan = [
            "[0:v]split=2[fond][net]",
            f"[fond]scale={L}:{H}:force_original_aspect_ratio=increase,"
            f"crop={L}:{H},gblur=sigma=40,eq=brightness=-0.16:saturation=0.7,"
            f"setsar=1,fps=30[flou]",
            f"[net]scale={largeur_plan}:{H},setsar=1,fps=30[plan]",
            "[flou][plan]overlay=(W-w)/2:0[v0]",
        ]
    else:
        plan = [f"[0:v]scale={L}:{H},setsar=1,fps=30[v0]"]

    # Le carton. Les lignes de pied entrent après le reste : le regard lit le
    # titre d'abord, l'adresse ensuite.
    dessins = [
        f"drawtext=fontfile='{police}':textfile='{titre}':fontcolor={ENCRE}:"
        f"fontsize={corps}:line_spacing={inter - corps}:x=(w-text_w)/2:y={haut}:"
        f"box=0:alpha='min(1,(t)/{FONDU})'",
        f"drawtext=fontfile='{police}':textfile='{serie}':fontcolor={ENCRE}:"
        f"fontsize={38 if H > L else 40}:x=(w-text_w)/2:y={y_serie}:"
        f"alpha='min(1,(t)/{FONDU})'",
    ]
    y = y_pied
    for texte, c in zip(g.pieds, corps_pieds):
        dessins.append(
            f"drawtext=fontfile='{police}':textfile='{fichier(texte)}':"
            f"fontcolor={ENCRE}:fontsize={c}:x=(w-text_w)/2:y={y}:"
            f"alpha='min(1,max(0,(t-0.4))/{FONDU})'")
        y += c + 22

    g_filtres = plan + [
        f"[1:v]scale={L}:{H},setsar=1,fps=30," + ",".join(dessins) + "[c0]",
        f"[2:v]scale={260 if H > L else 240}:-1[logo]",
        f"[c0][logo]overlay=(W-w)/2:{y_logo}[carton]",
        "[v0][carton]concat=n=2:v=1:a=0[vout]",

        # Le son de la source meurt dans le carton, il ne s'y arrête pas. Le
        # fondu se place donc à la fin de la source — c'est là qu'il y a encore
        # du son à baisser — et non à la fin du fichier, où `apad` n'a mis que
        # du silence : fondre du silence ne fond rien, et l'ambiance du lieu
        # coupait net à la dixième seconde.
        f"[0:a]aresample=48000,afade=t=out:st={d_source - 0.7}:d=0.7,"
        f"apad,atrim=0:{total},asetpts=PTS-STARTPTS[aout]",
    ]

    cmd = ["ffmpeg", "-v", "error", "-y",
           "-i", str(source),
           "-f", "lavfi", "-t", str(CARTON), "-i", f"color=c={SABLE}:s={L}x{H}:r=30",
           "-i", str(LOGO),
           "-filter_complex", ";".join(g_filtres),
           "-map", "[vout]", "-map", "[aout]",
           "-c:v", "libx264", "-preset", "medium", "-crf", g.crf,
           "-pix_fmt", "yuv420p", "-c:a", "aac", "-b:a", "192k",
           "-movflags", "+faststart", str(dest)]
    try:
        subprocess.run(cmd, check=True, capture_output=True, text=True)
    finally:
        for f in fics:
            pathlib.Path(f).unlink(missing_ok=True)


def controle(g, dest):
    out = subprocess.run(
        ["ffprobe", "-v", "error", "-show_entries", "format=duration",
         "-show_entries", "stream=codec_type,width,height", "-of", "json",
         str(dest)], capture_output=True, text=True).stdout
    d = json.loads(out)
    dur = float(d["format"]["duration"])
    v = [s for s in d["streams"] if s["codec_type"] == "video"][0]
    a = [s for s in d["streams"] if s["codec_type"] == "audio"]
    ok = (v["width"] == g.largeur and v["height"] == g.hauteur
          and len(a) == 1 and dur > CARTON)
    return ok, f"{dur:.2f}s {v['width']}x{v['height']} {'son' if a else 'MUET'}"


def travaux(cibles):
    """Ce qu'il y a à monter : (clé, titre du carton, fiche, source).

    Deux familles cohabitent. Un épisode part de sa story, et le carton porte
    le titre de l'épisode. Une bande-annonce part du montage de saison, et le
    carton porte le titre de la saison — il n'y a pas d'épisode à nommer, et
    nommer la saison est justement ce qui manque quand elle se termine.
    """
    eps, bas = episodes(), bandes_annonces()
    if not cibles:
        cibles = sorted(p.stem for p in STORIES.glob("*.mp4")) + sorted(bas)

    for cle in cibles:
        if cle in eps:
            yield cle, eps[cle]["titre"], eps[cle], STORIES / f"{cle}.mp4"
        elif cle in bas:
            yield cle, bas[cle]["titre"], bas[cle], BANDES / f"{cle}.mp4"
        else:
            yield cle, None, None, None


def main(g, cibles):
    g.sortie.mkdir(parents=True, exist_ok=True)
    faits = sautes = rates = 0
    for cle, titre, fiche, source in travaux(cibles):
        dest = g.sortie / f"{cle}.mp4"
        if fiche is None:
            print(f"  {cle}  inconnu de l'inventaire")
            rates += 1
            continue
        if not source.exists():
            print(f"  {cle}  pas de montage source — rien à porter")
            rates += 1
            continue
        if dest.exists() and dest.stat().st_size > 0:
            sautes += 1
            continue
        try:
            monte(g, titre, fiche, source, dest)
        except subprocess.CalledProcessError as err:
            print(f"  {cle}  ÉCHEC ffmpeg — {(err.stderr or '')[-200:]}")
            dest.unlink(missing_ok=True)
            rates += 1
            continue
        ok, detail = controle(g, dest)
        print(f"  {cle:38s} {'monté ' if ok else 'DOUTEUX'} {detail}")
        faits += 1

    print(f"\nmontés : {faits} | déjà là : {sautes} | en échec : {rates}")
