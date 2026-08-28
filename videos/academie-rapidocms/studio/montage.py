#!/usr/bin/env python3
"""Montage d'un tutoriel RapidoCMS — de la capture brute au master et au Short.

Un épisode se décrit en données : la capture source, la liste des plans, et
pour chaque plan sa ligne de voix off. Le montage en découle.

    from studio import Episode, Plan, monter

    EPISODE = Episode(
        slug="creer-un-post", numero=6, titre="Créer un post", …,
        plans=[Plan("N1", 0.0, 6.0, "Vous ouvrez…", chapitre="Le calendrier"), …],
    )
    monter(EPISODE)

Règle de calage, héritée de l'Académie : **chaque plan dure exactement la
longueur de sa ligne de voix off.** Le montage lit la durée du WAV et en déduit
la vitesse du plan, plafonnée à 2,5× ; si la source est plus courte que la
voix, la dernière image est tenue. Aucun temps mort de plus de trois secondes
ne subsiste, et la dérive ne s'accumule jamais.

La voix off validée n'est jamais réécrite ici : `Plan.voix` est la source.
"""

from __future__ import annotations

import json
import shutil
from dataclasses import dataclass, field
from pathlib import Path

from PIL import Image

from .charte import (BANDE_BAS, BANDE_HAUT, BLEU, ECRAN_H, FOND, FPS, H, SRC_CROP,
                     W, duree_de, ffmpeg, lancer)
from .habillage import (CARTON_S, FIN_S, OUVERTURE_S, Ouverture, bandeaux,
                        medaillon, rendre_carton, rendre_fin, rendre_ouverture,
                        rendre_vignette)
from .voix import Voix, duree_wav, silence

VITESSE_MAX = 2.5
FONDU_BANNIERE = 0.45
FONDU_SOUS_TITRE = 0.30
MEDAILLON_S = 2.8


@dataclass
class Plan:
    """Un plan : un morceau de capture, une ligne de voix off.

    `debut`/`fin` sont des secondes dans la capture d'origine. `chapitre`, s'il
    est renseigné, ouvre un chapitre : un carton le précède et le présentateur
    apparaît en pastille pendant les premières secondes.
    """
    cle: str
    debut: float
    fin: float
    voix: str
    chapitre: str = ""
    pose: str = "presente-paume"
    zoom: bool = False
    bandeau: str = ""          # bandeau affiché ; par défaut, le chapitre courant
    image: Path | None = None  # plan sur image fixe (carte Version Minute…)

    @property
    def portee(self) -> float:
        return max(0.1, self.fin - self.debut)


@dataclass
class Episode:
    slug: str
    numero: int | None
    titre: str
    titre_court: str
    module: str
    promesse: str
    source: Path
    plans: list[Plan]
    suivant: str = ""
    voix_fin: str = ""
    vignette_a: float = 8.0
    pose_vignette: str = "decouverte"
    mot_cle: str = ""
    racine: Path = field(default_factory=Path.cwd)

    @property
    def travail(self) -> Path:
        return self.racine / "composition"

    @property
    def audio(self) -> Path:
        return self.racine / "audio"

    @property
    def exports(self) -> Path:
        return self.racine / "exports"

    @property
    def master(self) -> Path:
        return self.exports / f"{self.slug}-16x9.mp4"

    @property
    def short(self) -> Path:
        return self.exports / f"{self.slug}-9x16.mp4"


# ── Voix ─────────────────────────────────────────────────────────────────────
def dire_les_plans(ep: Episode, voix: Voix | None = None) -> dict[str, float]:
    """Synthétise une piste par plan et renvoie les durées, par clé de plan."""
    voix = voix or Voix()
    durees: dict[str, float] = {}
    for i, plan in enumerate(ep.plans, start=1):
        cible = ep.audio / f"{i:02d}-{plan.cle}.wav"
        durees[plan.cle] = voix.dire(plan.voix, cible)
        print(f"  voix {plan.cle} — {durees[plan.cle]:.2f} s")
    if ep.voix_fin:
        cible = ep.audio / "99-fin.wav"
        durees["_fin"] = voix.dire(ep.voix_fin, cible)
        print(f"  voix fin — {durees['_fin']:.2f} s")
    (ep.audio / "durees.json").write_text(
        json.dumps(durees, indent=2, ensure_ascii=False), encoding="utf-8")
    return durees


def _durees_connues(ep: Episode) -> dict[str, float]:
    fichier = ep.audio / "durees.json"
    if fichier.exists():
        return json.loads(fichier.read_text(encoding="utf-8"))
    return dire_les_plans(ep)


# ── Un plan ──────────────────────────────────────────────────────────────────
def _numero_chapitre(ep: Episode, index: int) -> tuple[int, str]:
    """Numéro et titre du chapitre auquel appartient le plan `index`."""
    numero, titre = 0, ""
    for i, plan in enumerate(ep.plans):
        if plan.chapitre:
            numero += 1
            titre = plan.chapitre
        if i == index:
            return numero, titre
    return numero, titre


def rendre_plan(ep: Episode, index: int, plan: Plan, duree: float) -> Path:
    """Encode un plan complet : capture recadrée, cadre, bandeau, sous-titre."""
    travail = ep.travail
    travail.mkdir(parents=True, exist_ok=True)
    numero_ch, titre_ch = _numero_chapitre(ep, index)
    etiquette = plan.bandeau or titre_ch
    calques = bandeaux(etiquette, numero_ch, plan.voix, ep.numero,
                       travail / "calques", f"{index:02d}")

    vitesse = min(VITESSE_MAX, max(0.45, plan.portee / max(duree, 0.1)))
    if plan.image is not None:
        entrees = ["-loop", "1", "-t", f"{duree:.3f}", "-i", str(plan.image)]
    else:
        entrees = ["-ss", f"{plan.debut:.3f}", "-to", f"{plan.fin:.3f}",
                   "-i", str(ep.source)]
    entrees += [
        "-loop", "1", "-i", str(calques["cadre"]),
        "-loop", "1", "-i", str(calques["banniere"]),
        "-loop", "1", "-i", str(calques["sous_titre"]),
    ]
    if plan.chapitre:
        entrees += ["-loop", "1", "-i", str(medaillon(plan.pose, travail / "calques",
                                                      f"{index:02d}"))]

    if plan.zoom:
        ecran = (f"scale={int(W * 1.10)}:{int(ECRAN_H * 1.10)}:flags=lanczos,"
                 f"zoompan=z='min(1.0+0.0009*on,1.10)':d=1:"
                 f"x='iw/2-(iw/zoom/2)':y='ih/2-(ih/zoom/2)':"
                 f"s={W}x{ECRAN_H}:fps={FPS}")
    else:
        ecran = f"scale={W}:{ECRAN_H}:flags=lanczos"

    if plan.image is not None:
        source = f"[0:v]fps={FPS},{ecran}[scr]"
    else:
        source = (f"[0:v]{SRC_CROP},setpts=(PTS-STARTPTS)/{vitesse:.4f},fps={FPS},"
                  f"{ecran},tpad=stop_mode=clone:stop_duration=12[scr]")

    filtres = [
        f"color=c=0x{FOND[0]:02X}{FOND[1]:02X}{FOND[2]:02X}:s={W}x{H}:r={FPS}[bg]",
        source,
        f"[bg][scr]overlay=0:{BANDE_HAUT}[a]",
        "[a][1:v]overlay=0:0[b]",
        f"[2:v]fade=t=in:st=0:d={FONDU_BANNIERE}:alpha=1[ban]",
        f"[b][ban]overlay=x='-320*pow(1-min(1\\,t/{FONDU_BANNIERE})\\,2)':y=0[c]",
        f"[3:v]fade=t=in:st=0:d={FONDU_SOUS_TITRE}:alpha=1[st]",
        "[c][st]overlay=0:0" + ("[d]" if plan.chapitre else "[v]"),
    ]
    if plan.chapitre:
        filtres += [
            f"[4:v]fade=t=in:st=0.15:d=0.4:alpha=1,"
            f"fade=t=out:st={MEDAILLON_S - 0.4:.2f}:d=0.4:alpha=1[med]",
            f"[d][med]overlay=x='60*pow(1-min(1\\,t/0.55)\\,2)':y=0:"
            f"enable='lt(t,{MEDAILLON_S})'[v]",
        ]

    cible = travail / f"plan-{index:02d}.mp4"
    lancer([ffmpeg(), "-y", "-loglevel", "error", *entrees,
            "-filter_complex", ";".join(filtres), "-map", "[v]",
            "-t", f"{duree:.3f}", "-r", str(FPS),
            "-c:v", "libx264", "-profile:v", "high", "-pix_fmt", "yuv420p",
            "-crf", "18", str(cible)])
    return cible


# ── Assemblage ───────────────────────────────────────────────────────────────
def monter(ep: Episode, avec_short: bool = True) -> Path:
    """Produit le master 16:9, la vignette, et le Short 9:16."""
    ep.travail.mkdir(parents=True, exist_ok=True)
    ep.exports.mkdir(parents=True, exist_ok=True)
    durees = _durees_connues(ep)

    print("· cartons")
    ouverture = rendre_ouverture(
        Ouverture(titre=ep.titre_court, numero=ep.numero, module=ep.module),
        ep.travail / "ouverture.mp4")
    duree_fin = max(FIN_S, durees.get("_fin", 0.0) + 0.8)
    fin = rendre_fin(ep.travail / "fin.mp4", ep.suivant, duree_fin)

    morceaux: list[Path] = [ouverture]
    pistes: list[Path] = [silence(OUVERTURE_S, ep.audio / "_sil-ouverture.wav")]

    numero_ch = 0
    for index, plan in enumerate(ep.plans):
        if plan.chapitre:
            numero_ch += 1
            carton = rendre_carton(numero_ch, plan.chapitre,
                                   ep.travail / f"carton-{numero_ch}.mp4")
            morceaux.append(carton)
            pistes.append(silence(CARTON_S, ep.audio / f"_sil-carton{numero_ch}.wav"))
        duree = durees[plan.cle]
        print(f"· plan {plan.cle} — {duree:.2f} s")
        morceaux.append(rendre_plan(ep, index, plan, duree))
        pistes.append(ep.audio / f"{index + 1:02d}-{plan.cle}.wav")

    morceaux.append(fin)
    if ep.voix_fin:
        pistes.append(ep.audio / "99-fin.wav")
        pistes.append(silence(duree_fin - durees["_fin"], ep.audio / "_sil-fin.wav"))
    else:
        pistes.append(silence(duree_fin, ep.audio / "_sil-fin.wav"))

    print("· assemblage")
    liste_v = ep.travail / "plans.txt"
    liste_v.write_text("".join(f"file '{p.resolve()}'\n" for p in morceaux),
                       encoding="utf-8")
    muet = ep.travail / "muet.mp4"
    lancer([ffmpeg(), "-y", "-loglevel", "error", "-f", "concat", "-safe", "0",
            "-i", str(liste_v), "-c", "copy", str(muet)])

    liste_a = ep.travail / "pistes.txt"
    liste_a.write_text("".join(f"file '{p.resolve()}'\n" for p in pistes),
                       encoding="utf-8")
    piste = ep.travail / "voix.wav"
    lancer([ffmpeg(), "-y", "-loglevel", "error", "-f", "concat", "-safe", "0",
            "-i", str(liste_a), "-c", "copy", str(piste)])

    lancer([ffmpeg(), "-y", "-loglevel", "error", "-i", str(muet), "-i", str(piste),
            "-c:v", "copy", "-c:a", "aac", "-b:a", "192k", "-ar", "48000",
            "-ac", "2", "-shortest", "-movflags", "+faststart", str(ep.master)])
    print(f"  master — {duree_de(ep.master):.2f} s → {ep.master}")

    print("· vignette")
    rendre_vignette(ep.titre, ep.module, ep.numero, _image_source(ep),
                    ep.pose_vignette, ep.exports / f"{ep.slug}-vignette.jpg",
                    ep.mot_cle)

    if avec_short:
        print("· short 9:16")
        from .short import monter_short
        monter_short(ep, durees)
    return ep.master


def _image_source(ep: Episode) -> Image.Image | None:
    """Arrêt sur image de la capture, sans ses bandeaux, pour la vignette."""
    cible = ep.travail / "vignette-source.png"
    lancer([ffmpeg(), "-y", "-loglevel", "error", "-ss", f"{ep.vignette_a:.2f}",
            "-i", str(ep.source), "-vframes", "1", "-vf", SRC_CROP, str(cible)])
    return Image.open(cible) if cible.exists() else None


def nettoyer(ep: Episode) -> None:
    """Supprime les fichiers intermédiaires, garde exports/ et audio/."""
    shutil.rmtree(ep.travail, ignore_errors=True)
