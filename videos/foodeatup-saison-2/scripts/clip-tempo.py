#!/usr/bin/env python3
"""Tempo réel et grille de temps d'une chanson, sans aucune dépendance.

    python3 scripts/clip-tempo.py chanson.mp3 [work/beatgrid.json]

Cette machine n'a ni librosa ni numpy — et le clip ne peut pas attendre une
installation qui passe ou non derrière le proxy. La méthode est classique et
tient en trois temps : enveloppe d'énergie, autocorrélation pour la période,
puis recherche de la phase. C'est exactement ce que fait un détecteur de
tempo de bibliothèque, en moins général et en assez bon pour poser des
coupes.

Pourquoi mesurer plutôt que croire le prompt : sur les deux clips précédents,
142 BPM demandés en ont donné 144, et 92 en ont donné 90,7. Une grille bâtie
sur le tempo demandé dérive d'une demi-seconde en fin de morceau — assez pour
que les dernières coupes tombent à côté.
"""
import json
import math
import subprocess
import sys
from array import array

SR = 11025          # suffisant : on cherche des attaques, pas des notes
HOP = 256           # ~23 ms, assez fin pour distinguer deux croches à 92 BPM
BPM_MIN, BPM_MAX = 60.0, 180.0


def lire_pcm(chemin: str) -> array:
    """Le morceau en mono 16 bits, via ffmpeg."""
    out = subprocess.run(
        # -vn : un MP4 en entrée fait râler le muxeur s16le sur le flux vidéo
        ["ffmpeg", "-nostdin", "-v", "error", "-i", chemin, "-vn",
         "-ac", "1", "-ar", str(SR), "-f", "s16le", "-"],
        stdout=subprocess.PIPE, check=True).stdout
    ech = array("h")
    ech.frombytes(out[: len(out) // 2 * 2])
    return ech


def enveloppe(ech: array) -> list[float]:
    """Montées d'énergie, trame par trame.

    On ne garde que la différence positive : une attaque, c'est de l'énergie
    qui arrive. La décroissance d'une note ne doit pas compter comme un temps.
    """
    n = len(ech) // HOP
    energie = [0.0] * n
    for i in range(n):
        s = 0
        base = i * HOP
        for k in range(base, base + HOP):
            v = ech[k]
            s += v * v
        energie[i] = math.log1p(s / HOP)
    flux = [0.0] * n
    for i in range(1, n):
        d = energie[i] - energie[i - 1]
        flux[i] = d if d > 0 else 0.0
    # Retrait de la moyenne glissante : sinon un refrain plus fort qu'un
    # couplet pèse plus lourd qu'un temps bien marqué.
    fen = 32
    lisse = [0.0] * n
    cumul = 0.0
    for i in range(n):
        cumul += flux[i]
        if i >= fen:
            cumul -= flux[i - fen]
        lisse[i] = cumul / min(i + 1, fen)
    return [max(0.0, flux[i] - lisse[i]) for i in range(n)]


def periode(flux: list[float]) -> float:
    """Période du temps, en trames, par autocorrélation de l'enveloppe."""
    par_trame = SR / HOP
    lag_min = int(par_trame * 60.0 / BPM_MAX)
    lag_max = int(par_trame * 60.0 / BPM_MIN)
    n = len(flux)
    meilleur, meilleur_lag = -1.0, lag_min
    for lag in range(lag_min, lag_max + 1):
        s = 0.0
        for i in range(lag, n):
            s += flux[i] * flux[i - lag]
        # Une corrélation à un lag long porte sur moins de termes : on divise
        # par le nombre de termes, sans quoi les tempos lents gagnent toujours.
        s /= (n - lag)
        if s > meilleur:
            meilleur, meilleur_lag = s, lag
    return float(meilleur_lag)


def phase(flux: list[float], per: float) -> int:
    """Décalage du premier temps : l'offset qui capte le plus d'attaques."""
    meilleur, meilleur_off = -1.0, 0
    for off in range(int(per)):
        s, i = 0.0, off
        while i < len(flux):
            s += flux[int(i)]
            i += per
        if s > meilleur:
            meilleur, meilleur_off = s, off
    return meilleur_off


def main() -> None:
    if len(sys.argv) < 2:
        sys.exit("usage : clip-tempo.py chanson.mp3 [sortie.json]")
    src = sys.argv[1]
    dest = sys.argv[2] if len(sys.argv) > 2 else "work/beatgrid.json"

    ech = lire_pcm(src)
    duree = len(ech) / SR
    flux = enveloppe(ech)
    per = periode(flux)
    off = phase(flux, per)

    par_trame = SR / HOP
    bpm = 60.0 * par_trame / per
    # Un détecteur se trompe volontiers d'octave. On ramène dans la fourchette
    # où vivent les morceaux qu'on monte, plutôt que de rendre 46 ou 184 BPM.
    while bpm < 70.0:
        bpm *= 2.0
        per /= 2.0
    while bpm > 160.0:
        bpm /= 2.0
        per *= 2.0

    intervalle = per / par_trame
    depart = off / par_trame
    temps = []
    t = depart
    while t < duree:
        temps.append(round(t, 4))
        t += intervalle

    grille = {
        "source": src,
        "duree_s": round(duree, 3),
        "bpm_mesure": round(bpm, 2),
        "intervalle_s": round(intervalle, 5),
        "premier_temps_s": round(depart, 4),
        "temps": temps,
        "mesures": [temps[i] for i in range(0, len(temps), 4)],
        "note": "Tempo mesuré sur l'audio, jamais celui demandé au générateur.",
    }
    with open(dest, "w", encoding="utf-8") as f:
        json.dump(grille, f, ensure_ascii=False, indent=2)
    print(f"✅ {dest}")
    print(f"   {duree:.2f} s · {bpm:.2f} BPM · premier temps à {depart:.3f} s "
          f"· {len(temps)} temps, {len(grille['mesures'])} mesures")


if __name__ == "__main__":
    main()
