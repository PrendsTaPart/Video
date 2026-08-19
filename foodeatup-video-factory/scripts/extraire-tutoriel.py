#!/usr/bin/env python3
"""Les dix secondes d'écran d'un épisode, découpées dans le tutoriel du guide.

    python3 scripts/extraire-tutoriel.py EP098 EP102 EP104
    python3 scripts/extraire-tutoriel.py EP098 --apercu   (planche de contrôle, sans écrire)

RÉCUPÉRATION ET DÉCOUPE SEULES. Aucun crédit, aucune génération : la vidéo
existe déjà dans la bibliothèque des guides, on y prend dix secondes.

Le segment D d'un master montre l'écran du module pendant que l'avatar parle.
`content/tutoriels-guides.json` — copie du catalogue de
`PrendsTaPart/foodeatup-guide-star` — donne l'adresse de chaque tutoriel.

Tous ne conviennent pas
-----------------------
Les modules encore en développement sont présentés par un diaporama de cartons
de texte, pas par une capture d'écran : HubRise et la Caisse POS, à ce jour.
Un carton de texte sous un avatar qui parle donne deux textes concurrents, et
le segment perd son objet. Le script refuse donc ces vidéos au lieu de les
découper.

Il les reconnaît à leur FOND CRÈME. Un carton, c'est une carte blanche posée
sur le crème de la charte : les marges en portent partout, un cinquième à un
tiers de l'image. Un écran de logiciel est plein cadre, blanc et gris, et n'en
porte presque pas — sept pour cent au plus sur les vidéos mesurées. La
séparation est franche et n'a pas eu besoin d'être ajustée.

C'est aussi ce qui choisit la fenêtre : parmi toutes les positions possibles,
on garde celle qui contient le moins de crème, donc le plus d'interface. La
densité de contours, essayée d'abord, confondait le carton-titre — qui porte
une photo du chef et un logo — avec une vraie capture.
"""
import json
import pathlib
import re
import subprocess
import sys
import urllib.request

R = pathlib.Path(__file__).resolve().parent.parent
CATALOGUE = R / "content" / "tutoriels-guides.json"
INVENTAIRE = R.parent / "foodeatup-social" / "data" / "series.json"
SORTIE = R / "assets" / "software"
CACHE = R / "build" / "tutoriels"

DUREE = 10.0
L, H = 1920, 828          # le format des quatre-vingt-cinq extraits déjà en place
SEUIL_CREME = 0.15        # cartons mesurés à 21-29 %, interfaces à 1-15 %

MODULES = {
    "HubRise": "hubrise-livraisons", "KDS": "kds-cuisine", "HACCP": "haccp",
    "Caisse POS": "caisse-pos", "StockVision": "stockvision-ai",
    "Mon Site": "site-web-vitrine", "Réservation": "reservation-salle",
    "Service": "service-commande", "PrediBot": "predibot",
    "Configuration": "configuration", "Équipe & Planning": "equipe-planning",
    "Marketing": "marketing-fidelite", "Comptabilité": "comptabilite",
    "Caroline": "caroline-ia",
}


def sans_numero(t):
    t = re.sub(r"^\s*\d+\s*[-–.]\s*", "", (t or "").lower())
    return re.sub(r"[^a-zà-ÿ ]", " ", t)


def apparier(episode, catalogue):
    """Le tutoriel du même module dont le titre ressemble le plus au chapitre."""
    import difflib
    slug = MODULES.get(episode["module"])
    cands = [c for c in catalogue if c["mod"] == slug and c.get("video")]
    if not cands:
        return None, 0.0
    chap = sans_numero(episode["chapitre"])
    best = max(cands, key=lambda c: difflib.SequenceMatcher(
        None, chap, sans_numero(c["title"])).ratio())
    score = difflib.SequenceMatcher(None, chap, sans_numero(best["title"])).ratio()
    return best, score


def profil_creme(f, pas=0.5):
    """Part de crème par demi-seconde, sur des images réduites à 64 × 36."""
    duree = float(subprocess.run(
        ["ffprobe", "-v", "error", "-show_entries", "format=duration",
         "-of", "csv=p=0", str(f)], capture_output=True, text=True).stdout or 1)
    raw = subprocess.run(
        ["ffmpeg", "-v", "error", "-i", str(f), "-vf",
         f"fps=1/{pas},scale=64:36,format=rgb24", "-f", "rawvideo", "-"],
        capture_output=True).stdout
    px, out = 64 * 36 * 3, []
    for k in range(len(raw) // px):
        b = raw[k * px:(k + 1) * px]
        out.append(sum(1 for i in range(0, px, 3)
                       if 244 <= b[i] <= 255 and 238 <= b[i + 1] <= 252
                       and 215 <= b[i + 2] <= 240) / (64 * 36))
    return out, duree


def meilleure_fenetre(profil, pas=0.5):
    n = int(DUREE / pas)
    if len(profil) <= n:
        return 0.0, sum(profil) / max(1, len(profil))
    fenetres = [(sum(profil[i:i + n]) / n, i * pas) for i in range(len(profil) - n)]
    creme, debut = min(fenetres)
    return debut, creme


def main(args):
    apercu = "--apercu" in args
    cibles = [a for a in args if a.startswith("EP")]
    if not cibles:
        print(__doc__.strip().splitlines()[2])
        return 2

    catalogue = json.load(open(CATALOGUE, encoding="utf-8"))
    d = json.load(open(INVENTAIRE, encoding="utf-8"))
    eps = {e["id"]: e for s in d["series"] for sa in s["saisons"]
           for e in sa["episodes"]}
    CACHE.mkdir(parents=True, exist_ok=True)
    SORTIE.mkdir(parents=True, exist_ok=True)

    faits = refuses = rates = 0
    for ep in cibles:
        e = eps.get(ep)
        if not e:
            print(f"  {ep}  inconnu")
            rates += 1
            continue
        tuto, score = apparier(e, catalogue)
        if not tuto:
            print(f"  {ep}  aucun tutoriel pour le module « {e['module']} »")
            rates += 1
            continue

        src = CACHE / f"{tuto['slug']}.mp4"
        if not src.exists():
            try:
                urllib.request.urlretrieve(tuto["video"], src)
            except Exception as err:
                print(f"  {ep}  téléchargement impossible — {err}")
                rates += 1
                continue

        profil, duree = profil_creme(src)
        debut, creme = meilleure_fenetre(profil)
        entier = sum(profil) / max(1, len(profil))
        doute = "  ⚠ appariement faible" if score < 0.45 else ""

        # La garde porte sur la vidéo ENTIÈRE, pas sur la fenêtre retenue. Un
        # diaporama se termine sur une carte « avec Claude » au fond sombre,
        # qui ne contient pas un pixel de crème : en ne regardant que la
        # meilleure fenêtre, EP094 — trente-neuf secondes de cartons — passait
        # à 13 %. Ce qu'on veut savoir, c'est ce qu'est la vidéo, pas ce que
        # contient son plus mauvais quart.
        if entier >= SEUIL_CREME:
            print(f"  {ep}  REFUSÉ — {entier:.0%} de crème sur l'ensemble, "
                  f"c'est un diaporama : « {tuto['title']} »{doute}")
            refuses += 1
            continue
        if creme >= SEUIL_CREME:
            print(f"  {ep}  REFUSÉ — aucune fenêtre sous {SEUIL_CREME:.0%} de crème "
                  f"dans « {tuto['title']} »{doute}")
            refuses += 1
            continue

        print(f"  {ep}  {tuto['title'][:46]:46} départ {debut:5.1f}s · "
              f"crème {creme:4.0%} (vidéo {entier:.0%}) · "
              f"appariement {score:.2f}{doute}")
        if apercu:
            continue
        dest = SORTIE / f"{ep}.mp4"
        subprocess.run(
            ["ffmpeg", "-v", "error", "-y", "-ss", f"{debut:.2f}", "-t", str(DUREE),
             "-i", str(src), "-vf", f"scale={L}:-2,crop={L}:{H}", "-an",
             "-c:v", "libx264", "-preset", "medium", "-crf", "20",
             "-pix_fmt", "yuv420p", "-r", "30", str(dest)], check=True)
        faits += 1

    print(f"\nextraits : {faits} | refusés (cartons) : {refuses} | en échec : {rates}")
    return 1 if rates else 0


if __name__ == "__main__":
    sys.exit(main(sys.argv[1:]))
