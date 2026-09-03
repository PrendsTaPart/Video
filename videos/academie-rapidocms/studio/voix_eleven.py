#!/usr/bin/env python3
"""Voix off ElevenLabs — une piste par vidéo, redécoupée en plans.

Le MCP ElevenLabs facture et rend une génération à la fois. Générer les quinze
lignes d'un tutoriel une par une coûterait quinze allers-retours ; on génère
donc **toute la voix off d'une vidéo en une fois**, en séparant les lignes par
une balise de pause, puis on redécoupe le fichier sur ces silences.

Le procédé en trois temps :

1. `texte_a_generer(episode)` construit le prompt — les lignes du script dans
   l'ordre, séparées par `<break time="1.0s" />`.
2. La génération passe par le MCP ElevenLabs (voix `LUCAS`, modèle
   `eleven_multilingual_v2`), et le fichier est déposé dans `audio/vo-brute.mp3`.
3. `decouper(episode)` retrouve les silences, coupe en leur milieu, écrit une
   piste par plan et le `durees.json` dont le montage a besoin.

La voix off validée n'est jamais réécrite : le texte découpé est exactement
celui des `Plan.voix`, dans l'ordre.
"""

from __future__ import annotations

import json
import re
import subprocess
from dataclasses import dataclass
from pathlib import Path

from .charte import ffmpeg, lancer

VOIX_LUCAS = "odOFTFZU3DvAZ3EV3KHi"   # Lucas — Premium French Corporate Narrator
MODELE = "eleven_multilingual_v2"
PAUSE = '<break time="1.5s" />'

SEUIL_SILENCE_DB = -38
DUREE_SILENCE_MIN = 0.45
SR_CIBLE = 48000


@dataclass
class Silence:
    debut: float
    fin: float

    @property
    def duree(self) -> float:
        return self.fin - self.debut

    @property
    def milieu(self) -> float:
        return (self.debut + self.fin) / 2


def lignes_du_script(ep) -> list[tuple[str, str]]:
    """Les lignes à générer, dans l'ordre : (clé, texte)."""
    lignes = [(plan.cle, plan.voix) for plan in ep.plans]
    if ep.voix_fin:
        lignes.append(("_fin", ep.voix_fin))
    return lignes


def texte_a_generer(ep) -> str:
    """Le prompt complet à passer à ElevenLabs, pauses comprises."""
    return f" {PAUSE} ".join(texte for _, texte in lignes_du_script(ep))


def cout_estime(ep) -> tuple[int, float]:
    """Nombre de caractères facturés et coût approximatif, en dollars."""
    caracteres = len(texte_a_generer(ep))
    return caracteres, round(caracteres * 0.000182, 3)


def _silences(source: Path) -> list[Silence]:
    proc = subprocess.run(
        [ffmpeg(), "-hide_banner", "-i", str(source),
         "-af", f"silencedetect=noise={SEUIL_SILENCE_DB}dB:d={DUREE_SILENCE_MIN}",
         "-f", "null", "-"],
        capture_output=True, text=True)
    debuts, trouves = [], []
    for ligne in proc.stderr.splitlines():
        if "silence_start:" in ligne:
            debuts.append(float(re.search(r"silence_start:\s*(-?[\d.]+)", ligne).group(1)))
        elif "silence_end:" in ligne and debuts:
            fin = float(re.search(r"silence_end:\s*([\d.]+)", ligne).group(1))
            trouves.append(Silence(debuts.pop(0), fin))
    return trouves


def _duree(source: Path) -> float:
    proc = subprocess.run(
        [ffmpeg(), "-hide_banner", "-i", str(source)], capture_output=True, text=True)
    for ligne in proc.stderr.splitlines():
        if "Duration:" in ligne:
            h, m, s = ligne.split("Duration:")[1].split(",")[0].strip().split(":")
            return int(h) * 3600 + int(m) * 60 + float(s)
    raise RuntimeError(f"durée introuvable pour {source}")


def points_de_coupe(source: Path, longueurs: list[int]) -> list[float]:
    """Les `n-1` instants de coupe, un par frontière de ligne.

    Les pauses balisées ne se distinguent pas toujours des respirations
    naturelles : sur une voix off d'une minute, une virgule appuyée dure aussi
    longtemps qu'une balise. Choisir « les silences les plus longs » se trompe
    donc de frontière.

    On s'appuie plutôt sur le texte : le débit d'ElevenLabs étant régulier, la
    position attendue d'une coupure est proportionnelle au nombre de caractères
    lus avant elle. Chaque coupure est ensuite posée sur le silence réel le plus
    proche de cette attente — par programmation dynamique, pour que la suite
    reste croissante et que l'erreur totale soit minimale.
    """
    total = _duree(source)
    candidats = [s for s in _silences(source)
                 if s.debut > 0.30 and s.fin < total - 0.30]
    attendus = len(longueurs) - 1
    if len(candidats) < attendus:
        raise ValueError(
            f"{len(candidats)} silence(s) exploitable(s) pour {attendus} coupures "
            f"attendues dans {source.name}. Vérifier que les balises de pause ont "
            f"bien été rendues, ou baisser DUREE_SILENCE_MIN.")

    cumul, somme = [], 0
    for longueur in longueurs[:-1]:
        somme += longueur
        cumul.append(somme)
    caracteres = somme + longueurs[-1]
    attentes = [total * c / caracteres for c in cumul]

    # coût[j][i] : meilleure erreur pour placer les j+1 premières coupures,
    # la dernière sur le candidat i.
    INF = float("inf")
    cout = [[INF] * len(candidats) for _ in range(attendus)]
    origine = [[-1] * len(candidats) for _ in range(attendus)]
    for i, s in enumerate(candidats):
        cout[0][i] = abs(s.milieu - attentes[0])
    for j in range(1, attendus):
        meilleur_i, meilleur_cout = -1, INF
        for i in range(len(candidats)):
            if i > 0 and cout[j - 1][i - 1] < meilleur_cout:
                meilleur_cout, meilleur_i = cout[j - 1][i - 1], i - 1
            if meilleur_i >= 0:
                cout[j][i] = meilleur_cout + abs(candidats[i].milieu - attentes[j])
                origine[j][i] = meilleur_i

    fin = min(range(len(candidats)), key=lambda i: cout[attendus - 1][i])
    if cout[attendus - 1][fin] == INF:
        raise ValueError(f"alignement impossible sur {source.name}")
    choix = [fin]
    for j in range(attendus - 1, 0, -1):
        choix.append(origine[j][choix[-1]])
    return [candidats[i].milieu for i in reversed(choix)]


def decouper(ep, source: Path | None = None) -> dict[str, float]:
    """Découpe la voix off en une piste par plan et écrit `durees.json`."""
    source = source or (ep.audio / "vo-brute.mp3")
    if not source.exists():
        raise FileNotFoundError(
            f"{source} manquant. Générer la voix off avec le MCP ElevenLabs "
            f"(voix {VOIX_LUCAS}, modèle {MODELE}) puis déposer le fichier ici.")
    lignes = lignes_du_script(ep)
    coupes = points_de_coupe(source, [len(texte) for _, texte in lignes])
    bornes = [0.0, *coupes, _duree(source)]

    durees: dict[str, float] = {}
    for i, ((cle, _texte), debut, fin) in enumerate(zip(lignes, bornes, bornes[1:]), start=1):
        nom = "99-fin.wav" if cle == "_fin" else f"{i:02d}-{cle}.wav"
        cible = ep.audio / nom
        lancer([ffmpeg(), "-y", "-loglevel", "error", "-i", str(source),
                "-ss", f"{debut:.3f}", "-to", f"{fin:.3f}",
                "-af", f"aresample={SR_CIBLE},dynaudnorm=f=200:g=5:p=0.9",
                "-ar", str(SR_CIBLE), "-ac", "1", str(cible)])
        durees[cle] = round(fin - debut, 3)
        print(f"  {cle} — {durees[cle]:.2f} s")

    (ep.audio / "durees.json").write_text(
        json.dumps(durees, indent=2, ensure_ascii=False), encoding="utf-8")
    return durees


def cli(ep) -> None:
    """Point d'entrée commun des `episode.py` : --texte, --cout, --decouper."""
    import sys
    from .montage import monter

    args = sys.argv[1:]
    if "--texte" in args:
        print(texte_a_generer(ep))
    elif "--cout" in args:
        caracteres, dollars = cout_estime(ep)
        print(f"{caracteres} caractères — environ {dollars:.2f} $ "
              f"({len(lignes_du_script(ep))} lignes)")
    elif "--decouper" in args:
        decouper(ep)
    else:
        monter(ep, avec_short="--sans-short" not in args)
