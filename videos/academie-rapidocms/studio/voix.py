#!/usr/bin/env python3
"""Voix off — synthèse locale Kokoro, gratuite, une piste par ligne de script.

Kokoro tourne en local (ONNX, CPU) : aucune dépense, aucun appel réseau une
fois les fichiers de modèle en place. La seule voix française du modèle est
`ff_siwis`.

    from studio.voix import Voix
    voix = Voix()
    duree = voix.dire("Bienvenue dans l'Académie RapidoCMS.", Path("audio/01-hook.wav"))

Le débit vise 150 mots par minute, la cadence de lecture retenue pour toute la
série ; `VITESSE` ajuste le modèle à cette cible.

Les fichiers de modèle sont cherchés dans, par ordre :
`$KOKORO_HOME`, `~/.cache/kokoro`, puis le dossier de travail de la session.
"""

from __future__ import annotations

import os
import subprocess
from pathlib import Path

VOIX_FR = "ff_siwis"
VITESSE = 0.94
SR_CIBLE = 48000

_CANDIDATS = [
    Path(os.environ.get("KOKORO_HOME", "")) if os.environ.get("KOKORO_HOME") else None,
    Path.home() / ".cache" / "kokoro",
    Path("/tmp/claude-0/-home-user/e4c6ea41-0995-5098-9b61-d22bfb0c9091/scratchpad/kokoro"),
]


def _dossier_modele() -> Path:
    for candidat in _CANDIDATS:
        if candidat and (candidat / "kokoro-v1.0.onnx").exists():
            return candidat
    raise FileNotFoundError(
        "Modèle Kokoro introuvable. Télécharger kokoro-v1.0.onnx et "
        "voices-v1.0.bin depuis les releases de kokoro-onnx, puis les placer "
        "dans ~/.cache/kokoro ou pointer $KOKORO_HOME dessus.")


class Voix:
    """Synthèse Kokoro, chargée une fois pour toute la session."""

    def __init__(self, voix: str = VOIX_FR, vitesse: float = VITESSE):
        from kokoro_onnx import Kokoro
        dossier = _dossier_modele()
        self._moteur = Kokoro(str(dossier / "kokoro-v1.0.onnx"),
                              str(dossier / "voices-v1.0.bin"))
        self.voix = voix
        self.vitesse = vitesse

    def dire(self, texte: str, cible: Path) -> float:
        """Écrit `texte` en WAV 48 kHz mono et renvoie sa durée en secondes."""
        import soundfile as sf
        cible.parent.mkdir(parents=True, exist_ok=True)
        echantillons, sr = self._moteur.create(
            texte, voice=self.voix, speed=self.vitesse, lang="fr-fr")
        brut = cible.with_suffix(".brut.wav")
        sf.write(brut, echantillons, sr)
        # Rééchantillonnage et petit silence de garde, pour le montage.
        subprocess.run([
            __import__("shutil").which("ffmpeg")
            or __import__("imageio_ffmpeg").get_ffmpeg_exe(),
            "-y", "-loglevel", "error", "-i", str(brut),
            "-af", f"aresample={SR_CIBLE},apad=pad_dur=0.28,"
                   "dynaudnorm=f=200:g=5:p=0.9",
            "-ar", str(SR_CIBLE), "-ac", "1", str(cible)], check=True)
        brut.unlink(missing_ok=True)
        return duree_wav(cible)


def duree_wav(chemin: Path) -> float:
    import wave
    with wave.open(str(chemin)) as w:
        return w.getnframes() / w.getframerate()


def silence(duree: float, cible: Path) -> Path:
    cible.parent.mkdir(parents=True, exist_ok=True)
    subprocess.run([
        __import__("shutil").which("ffmpeg")
        or __import__("imageio_ffmpeg").get_ffmpeg_exe(),
        "-y", "-loglevel", "error", "-f", "lavfi",
        "-i", f"anullsrc=r={SR_CIBLE}:cl=mono", "-t", f"{duree:.3f}",
        "-ar", str(SR_CIBLE), "-ac", "1", str(cible)], check=True)
    return cible
