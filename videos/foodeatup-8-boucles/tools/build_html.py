#!/usr/bin/env python3
"""Génère les compositions `index.html` (master 16:9) et `index-reel.html` (9:16).

Le fichier produit est AUTO-PORTÉ : polices, moteur, styles, données et logos y
sont inlinés. Aucun chemin relatif, aucun `<link>` Google Fonts — une police non
inlinée retombe sur une police système et casse le déterminisme du rendu.

Les durées de plan viennent de la VO quand les mp3 existent (`assets/vo/pNN.mp3`),
sinon d'une estimation sur le nombre de caractères. C'est bien la VO qui commande
le montage, jamais l'inverse : `--exiger-vo` fait échouer le build si un mp3
manque, pour qu'aucun rendu final ne parte sur des durées estimées.
"""
import argparse
import base64
import json
import mimetypes
import pathlib
import subprocess
import sys

HERE = pathlib.Path(__file__).resolve().parent
PROJ = HERE.parent
REPO = PROJ.parent.parent

# Débit réel d'Adam en français, mesuré sur les 7 lignes de la boucle 01 :
# 1 045 caractères pour 60,94 s de parole, soit 17,1 c/s. (L'estimation initiale
# à 14,2 c/s, reprise de boucle-stockvision, donnait 20 % de trop.)
CPS = 17.1
# Amorce avant la ligne, silence après, pour que le plan ne coupe pas sur le
# dernier mot.
AMORCE, QUEUE = 0.45, 0.75

# Respiration supplémentaire, par type de plan. Ce n'est pas du rembourrage : la
# VO d'Adam est plus rapide que le temps dont l'image a besoin sur trois plans
# précis, et sans ces secondes l'animation est tronquée.
#   3 — la cascade : 8 maillons à lire, c'est le plan pilier de la série ;
#   6 — les chiffres : le compte-à-rebours doit finir avant la coupe ;
#   7 — le CTA : la phrase, le bouton et le logo entrent en 2,2 s à eux seuls.
RESPIRATION = {3: 3.0, 6: 1.5, 7: 2.5}


def ffmpeg() -> str:
    """ffmpeg n'est pas dans l'image ; on prend le static livré par le wheel."""
    try:
        import imageio_ffmpeg

        return imageio_ffmpeg.get_ffmpeg_exe()
    except ImportError:
        return "ffmpeg"


def duree_mp3(path: pathlib.Path) -> float:
    out = subprocess.run(
        [ffmpeg(), "-i", str(path), "-f", "null", "-"],
        capture_output=True, text=True,
    ).stderr
    # ffmpeg imprime « time=00:00:07.42 » sur la dernière ligne de progression.
    marks = [s for s in out.split("time=") if ":" in s[:12]]
    if not marks:
        raise RuntimeError(f"durée illisible pour {path}")
    hh, mm, ss = marks[-1][:11].split(":")
    return int(hh) * 3600 + int(mm) * 60 + float(ss)


def data_uri(path: pathlib.Path) -> str:
    mime = mimetypes.guess_type(path.name)[0] or "application/octet-stream"
    return f"data:{mime};base64," + base64.b64encode(path.read_bytes()).decode("ascii")


# Géométrie par format. Le reel n'est pas un recadrage : c'est la même timeline
# avec des tailles de texte plus grandes et une colonne plus étroite.
FORMATS = {
    "master": {
        "W": 1920, "H": 1080, "pad": 110,
        "fs": {"kicker": 26, "titre": 92, "corps": 38, "label": 24, "phrase": 68,
               "maillon": 31, "fiche": 27, "bandeau": 40, "carte-titre": 42,
               "btn": 34, "chiffre": 86, "coupure": 66, "cta": 38, "noeud": 22},
        "gapMaillon": 13, "padMaillon": "0.52em 0.9em", "puce": 22, "lienX": 34,
        "padCarte": "1.1em 1.3em", "gapChiffre": 26, "minChiffre": 300,
        "padChiffre": "0.8em 1em", "curseur": 54, "logoH": 62,
        "infiniRx": 430, "infiniRy": 250, "infiniTrait": 9, "infiniNoeud": 26,
        # Plan 3 : chaîne à gauche, fiches à droite.
        "cascadeCols": "1.35fr 1fr", "gapColonnes": 46, "fichesDecalage": 140,
        # Contenu centré verticalement, personnage ancré en bas à droite.
        "planJustify": "center", "padHaut": 110,
        "illuDroite": 70, "illuGauche": "auto", "illuBas": -30,
        "illuH": 780, "colonneTexte": 1180,
    },
    "reel": {
        "W": 1080, "H": 1920, "pad": 84,
        "fs": {"kicker": 28, "titre": 96, "corps": 42, "label": 26, "phrase": 66,
               "maillon": 34, "fiche": 29, "bandeau": 40, "carte-titre": 44,
               "btn": 36, "chiffre": 96, "coupure": 70, "cta": 40, "noeud": 24},
        "gapMaillon": 15, "padMaillon": "0.58em 0.85em", "puce": 24, "lienX": 32,
        "padCarte": "1.1em 1.15em", "gapChiffre": 22, "minChiffre": 420,
        "padChiffre": "0.9em 1em", "curseur": 58, "logoH": 66,
        "infiniRx": 400, "infiniRy": 300, "infiniTrait": 10, "infiniNoeud": 27,
        # En vertical la largeur manque : la chaîne prend toute la colonne et les
        # fiches passent dessous, sans décalage.
        "cascadeCols": "1fr", "gapColonnes": 26, "fichesDecalage": 0,
        # Texte calé dans le haut, personnage centré dans le bas du cadre :
        # en 9:16 un personnage collé au coin sort du champ de lecture.
        "planJustify": "flex-start", "padHaut": 200,
        "illuDroite": 0, "illuGauche": 0, "illuBas": -20,
        "illuH": 760, "colonneTexte": 912,
    },
}


def minutages(video: dict, dossier: pathlib.Path, exiger_vo: bool,
              types: dict) -> list[dict]:
    """Une entrée par plan : numéro, début et durée.

    La durée d'un plan est celle de sa ligne de VO — jamais l'inverse. On y
    ajoute l'amorce, le silence de queue, et la respiration propre au type de
    plan (voir RESPIRATION).
    """
    plans, curseur = [], 0.0
    for p in video["plans"]:
        mp3 = dossier / "assets" / "vo" / f"p{p['n']:02d}.mp3"
        if mp3.exists():
            parole = duree_mp3(mp3)
            source = "vo"
        elif exiger_vo:
            sys.exit(f"ERREUR — VO manquante : {mp3}. Build final refusé.")
        else:
            parole = len(p["vo"]) / CPS
            source = "estimée"
        d = parole + AMORCE + QUEUE + RESPIRATION.get(types[p["n"]], 0.0)
        plans.append({"n": p["n"], "start": round(curseur, 3),
                      "dur": round(d, 3), "parole": round(parole, 3),
                      "source": source})
        curseur += d
    return plans


def construire(video: dict, visuel: dict, fmt_nom: str,
               exiger_vo: bool) -> tuple[str, float, str]:
    F = FORMATS[fmt_nom]
    dossier = PROJ / video["dossier"]

    # La vidéo 0 n'a que 6 plans et pas de cascade : on mappe chaque plan sur le
    # gabarit qui lui correspond, sans en inventer un.
    TYPES = {1: 1, 2: 2, 3: 3, 4: 4, 5: 5, 6: 6, 7: 7}
    if video["slug"] == "boucle-00-principe":
        TYPES = {1: 1, 2: 2, 3: 5, 4: 2, 5: 7, 6: 6}

    tm = minutages(video, dossier, exiger_vo, TYPES)

    logo = REPO / "studio-video/assets/brand/logo-v2/foodeatup-logo-horizontal-mascot.png"

    # Personnages détourés par tools/prepare_assets.py : « problème » sur le
    # plan 1, « résultat » sur le plan 6. Une image absente n'arrête pas le
    # build — le plan se rend sans personnage plutôt qu'avec un placeholder.
    mapping = json.loads((PROJ / "assets/img/mapping.json").read_text(encoding="utf-8"))
    perso = mapping.get(video["slug"], {})

    def image(role: str) -> str | None:
        nom = perso.get(role)
        if not nom:
            return None
        f = PROJ / "assets/img" / f"{nom}.webp"
        return data_uri(f) if f.exists() else None

    plans_js = []
    for t in tm:
        typ = TYPES[t["n"]]
        d = dict(visuel.get(str(t["n"]), {}))
        d.update({"type": typ, "start": t["start"], "dur": t["dur"]})
        if typ == 1:
            d["illu"] = image("probleme")
        if typ == 6:
            d["illu"] = image("resultat")
        if typ == 3:
            d["preuve"] = f"{video['outilsMcp']} outils MCP exécutent cette boucle"
        if typ == 6 and "chiffres" not in d:
            d["chiffres"] = video["chiffres"]
        if typ == 7:
            d["logo"] = data_uri(logo)
        if typ == 5 and "voisines" not in d:
            d["voisines"] = video.get("boucleVoisines", [])
        if typ == 2 and "phrase" not in d:
            d["phrase"] = video["plans"][t["n"] - 1]["vo"].strip("« »")
        plans_js.append(d)

    duree = round(sum(t["dur"] for t in tm), 3)
    donnees = {
        "slug": video["slug"], "format": fmt_nom, "duree": duree,
        "W": F["W"], "H": F["H"], "plans": plans_js,
        "infiniRx": F["infiniRx"], "infiniRy": F["infiniRy"],
        "infiniTrait": F["infiniTrait"], "infiniNoeud": F["infiniNoeud"],
        "fsNoeud": F["fs"]["noeud"],
    }

    vars_css = "\n".join(
        [f"  --W: {F['W']}px;", f"  --H: {F['H']}px;", f"  --pad: {F['pad']}px;"]
        + [f"  --fs-{k}: {v}px;" for k, v in F["fs"].items()]
        + [
            f"  --gap-maillon: {F['gapMaillon']}px;",
            f"  --pad-maillon: {F['padMaillon']};",
            f"  --puce: {F['puce']}px;",
            f"  --lien-x: {F['lienX']}px;",
            f"  --pad-carte: {F['padCarte']};",
            f"  --gap-chiffre: {F['gapChiffre']}px;",
            f"  --min-chiffre: {F['minChiffre']}px;",
            f"  --pad-chiffre: {F['padChiffre']};",
            f"  --curseur: {F['curseur']}px;",
            f"  --logo-h: {F['logoH']}px;",
            f"  --cascade-cols: {F['cascadeCols']};",
            f"  --gap-colonnes: {F['gapColonnes']}px;",
            f"  --fiches-decalage: {F['fichesDecalage']}px;",
            f"  --illu-droite: {F['illuDroite']}px;",
            f"  --illu-bas: {F['illuBas']}px;",
            f"  --illu-h: {F['illuH']}px;",
            f"  --colonne-texte: {F['colonneTexte']}px;",
            f"  --plan-justify: {F['planJustify']};",
            f"  --pad-haut: {F['padHaut']}px;",
            f"  --illu-gauche: {F['illuGauche']}"
            + ("" if F["illuGauche"] == "auto" else "px") + ";",
        ]
    )

    fonts = (PROJ / "assets/fonts/fonts.css").read_text(encoding="utf-8")
    styles = (PROJ / "engine/scene.css").read_text(encoding="utf-8")
    moteur = (PROJ / "engine/scene.js").read_text(encoding="utf-8")

    html = f"""<!doctype html>
<html lang="fr"><head><meta charset="utf-8">
<title>{video['slug']} — {fmt_nom}</title>
<style>
{fonts}
:root {{
{vars_css}
}}
{styles}
</style></head>
<body><div id="stage"></div>
<script>window.__VIDEO = {json.dumps(donnees, ensure_ascii=False)};</script>
<script>
{moteur}
</script>
</body></html>
"""
    source = "VO réelle" if all(t["source"] == "vo" for t in tm) else "durées estimées"
    return html, duree, source


def main() -> None:
    ap = argparse.ArgumentParser()
    ap.add_argument("--slug", help="ne construire qu'une vidéo")
    ap.add_argument("--exiger-vo", action="store_true",
                    help="échouer si un mp3 de VO manque (obligatoire avant rendu final)")
    args = ap.parse_args()

    manifeste = json.loads((PROJ / "boucles.json").read_text(encoding="utf-8"))
    visuels = json.loads((PROJ / "visuels.json").read_text(encoding="utf-8"))

    for video in manifeste["videos"]:
        if args.slug and video["slug"] != args.slug:
            continue
        dossier = PROJ / video["dossier"]
        dossier.mkdir(parents=True, exist_ok=True)
        (dossier / "assets" / "vo").mkdir(parents=True, exist_ok=True)
        (dossier / "assets" / "img").mkdir(parents=True, exist_ok=True)

        for fmt_nom, nom_fichier in (("master", "index.html"), ("reel", "index-reel.html")):
            html, duree, source = construire(
                video, visuels[video["slug"]], fmt_nom, args.exiger_vo
            )
            (dossier / nom_fichier).write_text(html, encoding="utf-8")

        ecart = duree - video["dureeCible"]
        drapeau = "OK " if abs(ecart) <= 2 else "!! "
        print(f"{drapeau}{video['slug']:34s} {duree:6.2f}s "
              f"(cible {video['dureeCible']}s, écart {ecart:+.1f}s) [{source}]")


if __name__ == "__main__":
    main()
