#!/usr/bin/env python3
"""Short 9:16 — remontage vertical du même épisode, depuis les mêmes rushes.

Le Short reprend plan pour plan le master : même voix off, même découpage.
Seule la mise en cadre change — la capture devient une carte posée au centre,
le sous-titre passe en gros, et le présentateur ouvre chaque chapitre.

Zones de sécurité respectées : 150 px en haut, 170 px en bas.
"""

from __future__ import annotations

from pathlib import Path

from PIL import Image, ImageDraw

from .charte import (BLANC, BLEU, BLEU_CLAIR, BLEU_SOMBRE, FPS, H9, MARGE, SRC_CROP,
                     W9, ajustee, coins_arrondis, decouper, degrade_vertical,
                     detourer_pose, duree_de, ffmpeg, halo, lancer,
                     logo_redimensionne, ombre_portee, pastille, police,
                     texte_centre)
from .voix import silence

SAFE_HAUT = 150
SAFE_BAS = 170

CARTE_W = W9 - 2 * 24          # 1032 — la capture, presque pleine largeur
CARTE_H = int(CARTE_W * 570 / 1280)   # 459 — même rapport que la zone utile
CARTE_Y = 700


def _fond() -> Image.Image:
    fond = degrade_vertical(W9, H9, [BLEU_CLAIR, BLEU, BLEU_SOMBRE]).convert("RGBA")
    fond.alpha_composite(halo(int(W9 * 0.2), int(H9 * 0.18), 420, BLANC, 0.18, (W9, H9)))
    fond.alpha_composite(halo(int(W9 * 0.86), int(H9 * 0.82), 380, BLEU_CLAIR, 0.24, (W9, H9)))
    return fond


def _calques(titre_chapitre: str, numero_chapitre: int, sous_titre: str,
             titre_court: str, pose: str, dossier: Path, cle: str) -> dict[str, Path]:
    dossier.mkdir(parents=True, exist_ok=True)
    sorties: dict[str, Path] = {}

    fixe = _fond()
    d = ImageDraw.Draw(fixe)

    logo = logo_redimensionne(78)
    fixe.alpha_composite(logo, (W9 // 2 - logo.width // 2, SAFE_HAUT + 10))
    texte_centre(fixe, "ACADÉMIE RAPIDOCMS", police(True, 26), BLANC,
                 W9 // 2, SAFE_HAUT + 118)
    fnt = ajustee(True, 62, titre_court, W9 - 2 * MARGE)
    texte_centre(fixe, titre_court, fnt, BLANC, W9 // 2, SAFE_HAUT + 200, ombre=True)

    # Encoche d'accueil de la capture, pour que la carte ait un socle net.
    d.rounded_rectangle((24 - 6, CARTE_Y - 6, 24 + CARTE_W + 6, CARTE_Y + CARTE_H + 6),
                        radius=26, fill=BLANC + (60,))
    sorties["fond"] = dossier / f"{cle}-fond9.png"
    fixe.convert("RGB").save(sorties["fond"])

    banniere = Image.new("RGBA", (W9, H9), (0, 0, 0, 0))
    if titre_chapitre:
        etiquette = f"{numero_chapitre} · {titre_chapitre}"
        pastille(banniere, etiquette, ajustee(True, 34, etiquette, W9 - 2 * MARGE - 100),
                 W9 // 2, CARTE_Y - 84, BLANC, BLEU_SOMBRE, marge_x=34, marge_y=18)
    sorties["banniere"] = dossier / f"{cle}-ban9.png"
    banniere.save(sorties["banniere"])

    couche = Image.new("RGBA", (W9, H9), (0, 0, 0, 0))
    if sous_titre:
        fnt = police(True, 52)
        lignes = decouper(sous_titre, fnt, W9 - 2 * MARGE)
        while len(lignes) > 4 and fnt.size > 34:
            fnt = police(True, fnt.size - 4)
            lignes = decouper(sous_titre, fnt, W9 - 2 * MARGE)
        interligne = fnt.size + 18
        haut = H9 - SAFE_BAS - 40 - (len(lignes) - 1) * interligne
        for i, ligne in enumerate(lignes):
            texte_centre(couche, ligne, fnt, BLANC, W9 // 2, haut + i * interligne,
                         ombre=True)
    sorties["sous_titre"] = dossier / f"{cle}-st9.png"
    couche.save(sorties["sous_titre"])

    if pose:
        portrait = detourer_pose(pose, 620)
        couche = Image.new("RGBA", (W9, H9), (0, 0, 0, 0))
        couche.alpha_composite(ombre_portee(portrait, rayon=24, decalage=12, opacite=110),
                               (W9 - portrait.width + 40, CARTE_Y + CARTE_H - 40))
        sorties["pose"] = dossier / f"{cle}-pose9.png"
        couche.save(sorties["pose"])
    return sorties


def _plan_short(ep, index: int, plan, duree: float, numero_ch: int,
                titre_ch: str) -> Path:
    travail = ep.travail / "short"
    travail.mkdir(parents=True, exist_ok=True)
    calques = _calques(plan.bandeau or titre_ch, numero_ch, plan.voix,
                       ep.titre_court, plan.pose if plan.chapitre else "",
                       travail / "calques", f"{index:02d}")

    vitesse = min(2.5, max(0.45, plan.portee / max(duree, 0.1)))
    if plan.image is not None:
        entrees = ["-loop", "1", "-t", f"{duree:.3f}", "-i", str(plan.image)]
        source = f"[0:v]fps={FPS},scale={CARTE_W}:{CARTE_H}:flags=lanczos[scr]"
    else:
        entrees = ["-ss", f"{plan.debut:.3f}", "-to", f"{plan.fin:.3f}",
                   "-i", str(ep.source)]
        source = (f"[0:v]{SRC_CROP},setpts=(PTS-STARTPTS)/{vitesse:.4f},fps={FPS},"
                  f"scale={CARTE_W}:{CARTE_H}:flags=lanczos,"
                  f"tpad=stop_mode=clone:stop_duration=12[scr]")
    entrees += [
        "-loop", "1", "-i", str(calques["fond"]),
        "-loop", "1", "-i", str(calques["banniere"]),
        "-loop", "1", "-i", str(calques["sous_titre"]),
    ]
    filtres = [
        source,
        f"[1:v][scr]overlay=24:{CARTE_Y}[a]",
        "[2:v]fade=t=in:st=0:d=0.45:alpha=1[ban]",
        "[a][ban]overlay=0:0[b]",
        "[3:v]fade=t=in:st=0:d=0.30:alpha=1[st]",
        "[b][st]overlay=0:0" + ("[c]" if "pose" in calques else "[v]"),
    ]
    if "pose" in calques:
        entrees += ["-loop", "1", "-i", str(calques["pose"])]
        filtres += [
            "[4:v]fade=t=in:st=0.2:d=0.45:alpha=1,fade=t=out:st=2.6:d=0.4:alpha=1[po]",
            "[c][po]overlay=x='120*pow(1-min(1\\,t/0.6)\\,2)':y=0:enable='lt(t,3.0)'[v]",
        ]

    cible = travail / f"plan-{index:02d}.mp4"
    lancer([ffmpeg(), "-y", "-loglevel", "error", *entrees,
            "-filter_complex", ";".join(filtres), "-map", "[v]",
            "-t", f"{duree:.3f}", "-r", str(FPS),
            "-c:v", "libx264", "-profile:v", "high", "-pix_fmt", "yuv420p",
            "-crf", "19", str(cible)])
    return cible


def monter_short(ep, durees: dict[str, float]) -> Path:
    """Assemble le Short : mêmes plans, cadre vertical, mêmes pistes voix."""
    travail = ep.travail / "short"
    travail.mkdir(parents=True, exist_ok=True)

    morceaux, pistes = [], []
    numero_ch, titre_ch = 0, ""
    for index, plan in enumerate(ep.plans):
        if plan.chapitre:
            numero_ch += 1
            titre_ch = plan.chapitre
        duree = durees[plan.cle]
        morceaux.append(_plan_short(ep, index, plan, duree, numero_ch, titre_ch))
        pistes.append(ep.audio / f"{index + 1:02d}-{plan.cle}.wav")

    liste_v = travail / "plans.txt"
    liste_v.write_text("".join(f"file '{p.resolve()}'\n" for p in morceaux),
                       encoding="utf-8")
    muet = travail / "muet.mp4"
    lancer([ffmpeg(), "-y", "-loglevel", "error", "-f", "concat", "-safe", "0",
            "-i", str(liste_v), "-c", "copy", str(muet)])

    liste_a = travail / "pistes.txt"
    liste_a.write_text("".join(f"file '{p.resolve()}'\n" for p in pistes),
                       encoding="utf-8")
    piste = travail / "voix.wav"
    lancer([ffmpeg(), "-y", "-loglevel", "error", "-f", "concat", "-safe", "0",
            "-i", str(liste_a), "-c", "copy", str(piste)])

    lancer([ffmpeg(), "-y", "-loglevel", "error", "-i", str(muet), "-i", str(piste),
            "-c:v", "copy", "-c:a", "aac", "-b:a", "192k", "-ar", "48000",
            "-ac", "2", "-shortest", "-movflags", "+faststart", str(ep.short)])
    print(f"  short — {duree_de(ep.short):.2f} s → {ep.short}")
    return ep.short
