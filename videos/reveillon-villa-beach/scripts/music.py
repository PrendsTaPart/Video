#!/usr/bin/env python3
"""Musique de travail ORIGINALE pour le teaser réveillon (synthèse par code).

Aucune boucle, aucun sample ni morceau tiers : chaque son est calculé ici (numpy),
donc aucun droit à négocier. C'est un placeholder de montage : la version diffusée
doit utiliser une musique ElevenLabs Music (ou une librairie libre de droits) calée
sur le même découpage. Le découpage suit data/timeline.json :

  0-5 intro scintillante | 5-14 dîner lounge | 14-18 house (Généraliste)
  18-22 latino (clave, congas, montuno) | 22-26 disco funk (80/90/2000)
  26-30 dancehall/zouk + steel drum (Caraïbéenne) | 30-34.4 montée
  34.4-37 compte à rebours (3 battements) | 37-47 drop minuit | 47-54 outro

Usage : python3 scripts/music.py assets/music/musique-travail.wav
"""
import sys
import wave

import numpy as np

SR = 44100
DUR = 54.0
BPM = 120.0
BEAT = 60.0 / BPM
N = int(SR * DUR)
rng = np.random.default_rng(31)
out = np.zeros((N, 2))


def t_arr(d):
    return np.arange(int(SR * d)) / SR


def add(sig, start, gain=1.0, pan=0.0):
    i = int(start * SR)
    if i >= N:
        return
    sig = sig[: N - i] * gain
    out[i : i + len(sig), 0] += sig * (1 - max(pan, 0))
    out[i : i + len(sig), 1] += sig * (1 + min(pan, 0))


def env(t, a, d):
    return np.minimum(t / max(a, 1e-4), 1.0) * np.exp(-t / d)


def note(m):
    return 440.0 * 2 ** ((m - 69) / 12)


# ---------- instruments ----------
def kick(d=0.45, punch=1.0):
    t = t_arr(d)
    f = 48 + 110 * np.exp(-t / 0.035) * punch
    return np.sin(2 * np.pi * np.cumsum(f) / SR) * np.exp(-t / 0.16)


def snare(d=0.25):
    t = t_arr(d)
    return (rng.standard_normal(len(t)) * 0.6 + np.sin(2 * np.pi * 190 * t) * 0.5) * np.exp(-t / 0.06)


def clap():
    t = t_arr(0.3)
    n = rng.standard_normal(len(t))
    e = sum(np.exp(-np.maximum(t - k * 0.011, 0) / 0.008) * (t >= k * 0.011) for k in range(3))
    return n * (e * 0.5 + np.exp(-t / 0.09) * 0.5)


def hat(d=0.05):
    t = t_arr(d)
    n = rng.standard_normal(len(t))
    n = np.diff(n, prepend=0)
    return n * np.exp(-t / (d / 3))


def woodblock():
    t = t_arr(0.12)
    return np.sin(2 * np.pi * 1250 * t) * np.exp(-t / 0.02)


def conga(f):
    t = t_arr(0.3)
    return np.sin(2 * np.pi * f * t * (1 + 0.15 * np.exp(-t / 0.02))) * np.exp(-t / 0.12)


def pluck(m, d=0.35, bright=3):
    t = t_arr(d)
    f = note(m)
    s = sum(np.sin(2 * np.pi * f * k * t) / k ** 1.3 * np.exp(-t * k / (d * 2)) for k in range(1, bright + 1))
    return s * env(t, 0.003, d / 2.5)


def rhodes(ms, d=2.0):
    t = t_arr(d)
    s = sum(
        (np.sin(2 * np.pi * note(m) * t) + 0.25 * np.sin(2 * np.pi * note(m) * 2 * t) * np.exp(-t / 0.25))
        for m in ms
    )
    return s * env(t, 0.01, 1.2) * (1 + 0.15 * np.sin(2 * np.pi * 5 * t)) / len(ms)


def pad(ms, d, a=0.6):
    t = t_arr(d)
    s = sum(np.sin(2 * np.pi * note(m) * t * (1 + det)) for m in ms for det in (-0.003, 0.003))
    fade = np.minimum(t / a, 1) * np.minimum((d - t) / a, 1)
    return s * fade / (2 * len(ms))


def saw_stab(ms, d=0.22):
    t = t_arr(d)
    s = 0
    for m in ms:
        f = note(m)
        s = s + sum(np.sin(2 * np.pi * f * k * t) / k for k in range(1, 9))
    return s * env(t, 0.004, d / 2.2) / len(ms)


def bass(m, d=0.4):
    t = t_arr(d)
    f = note(m)
    return (np.sin(2 * np.pi * f * t) + 0.3 * np.sin(2 * np.pi * 2 * f * t)) * env(t, 0.005, d / 1.6)


def steel(m):
    t = t_arr(0.6)
    f = note(m)
    s = np.sin(2 * np.pi * f * t) + 0.5 * np.sin(2 * np.pi * f * 2.76 * t) * np.exp(-t / 0.08)
    return s * env(t, 0.002, 0.25)


def bell(m):
    t = t_arr(1.2)
    f = note(m)
    return (np.sin(2 * np.pi * f * t) + 0.4 * np.sin(2 * np.pi * f * 3.01 * t)) * np.exp(-t / 0.4)


def noise_riser(d):
    t = t_arr(d)
    n = rng.standard_normal(len(t))
    # filtre passe-haut qui s'ouvre : mélange bruit filtré / brut selon la progression
    lp = np.convolve(n, np.ones(40) / 40, mode="same")
    p = t / d
    return ((n - lp) * p + lp * (1 - p)) * p ** 2


def impact():
    t = t_arr(2.5)
    boom = np.sin(2 * np.pi * np.cumsum(35 + 80 * np.exp(-t / 0.08)) / SR) * np.exp(-t / 0.5)
    crash = rng.standard_normal(len(t)) * np.exp(-t / 0.7) * 0.35
    return boom + crash


# ---------- helpers ----------
def beats(start, end, step=BEAT, offset=0.0):
    x = start + offset
    while x < end - 1e-6:
        yield x
        x += step


CHORDS_LOUNGE = [[65, 69, 72, 76], [64, 67, 71, 74], [62, 65, 69, 72], [60, 64, 67, 71]]  # Fmaj7 Em7 Dm7 Cmaj7
ROOTS_LOUNGE = [41, 40, 38, 36]
CHORDS_PARTY = [[57, 60, 64], [53, 57, 60], [55, 59, 62], [52, 55, 59]]  # Am F G Em
ROOTS_PARTY = [45, 41, 43, 40]


def chord_at(x, start, chords, bar=4 * BEAT):
    return chords[int((x - start) / bar) % len(chords)], int((x - start) / bar) % len(chords)


# 0-5 intro
add(pad([60, 64, 67, 71, 74], 5.6, a=1.2), 0, 0.5)
for i, m in enumerate([84, 88, 91, 95, 91, 96, 100, 95]):
    add(bell(m), 0.25 + i * 0.55, 0.12, pan=(-0.5 if i % 2 else 0.5))
for x in beats(2.5, 5.0):
    add(kick(punch=0.6), x, 0.35 * (x - 2.0) / 3)

# 5-14 lounge
for x in beats(5.0, 14.0):
    k = round((x - 5.0) / BEAT)
    if k % 2 == 0:
        add(kick(punch=0.5), x, 0.45)
    add(hat(0.04), x + BEAT / 2, 0.12, pan=0.3)
    if k % 4 == 0:
        ch, idx = chord_at(x, 5.0, CHORDS_LOUNGE)
        add(rhodes(ch, 2.0), x, 0.55)
    _, idx = chord_at(x, 5.0, CHORDS_LOUNGE)
    walk = [0, 7, 12, 7][k % 4]
    add(bass(ROOTS_LOUNGE[idx] + walk, 0.45), x, 0.45)
    if k % 4 == 1:
        add(woodblock(), x + BEAT / 2, 0.08, pan=-0.4)

# 14-18 house (Généraliste)
for x in beats(14.0, 18.0):
    k = round((x - 14.0) / BEAT)
    add(kick(), x, 0.8)
    add(hat(0.09), x + BEAT / 2, 0.22, pan=0.25)
    if k % 2 == 1:
        add(clap(), x, 0.35)
    ch, idx = chord_at(x, 14.0, CHORDS_PARTY)
    add(saw_stab([m + 12 for m in ch]), x + BEAT / 2, 0.22)
    add(bass(ROOTS_PARTY[idx], 0.3), x + BEAT / 2, 0.5)

# 18-22 latino (clave son 3-2, congas, montuno, tumbao)
clave = [0, 1.5, 3, 5, 6]  # en temps sur 2 mesures
for bar in beats(18.0, 22.0, step=8 * BEAT):
    for c in clave:
        add(woodblock(), bar + c * BEAT, 0.3, pan=0.2)
for x in beats(18.0, 22.0, step=BEAT / 2):
    k = round((x - 18.0) / (BEAT / 2))
    ch, idx = chord_at(x, 18.0, CHORDS_PARTY)
    add(pluck(ch[k % 3] + 12 * (1 + (k % 4 == 3)), 0.25, 4), x, 0.25, pan=-0.2)
    if k % 4 in (3, 6 % 4):
        add(conga(330 if k % 8 < 4 else 260), x, 0.35, pan=0.4)
for x in beats(18.0, 22.0):
    k = round((x - 18.0) / BEAT)
    add(kick(punch=0.4), x, 0.3)
    _, idx = chord_at(x, 18.0, CHORDS_PARTY)
    if k % 2 == 1:
        add(bass(ROOTS_PARTY[idx], 0.4), x + BEAT / 2, 0.55)
    add(conga(200), x + BEAT * 0.75, 0.25, pan=-0.4)

# 22-26 disco funk (80/90/2000)
for x in beats(22.0, 26.0, step=BEAT / 2):
    k = round((x - 22.0) / (BEAT / 2))
    _, idx = chord_at(x, 22.0, CHORDS_PARTY)
    add(bass(ROOTS_PARTY[idx] + (12 if k % 2 else 0), 0.22), x, 0.55)
    add(hat(0.06 if k % 2 else 0.03), x, 0.2 if k % 2 else 0.1, pan=0.3)
for x in beats(22.0, 26.0):
    k = round((x - 22.0) / BEAT)
    add(kick(), x, 0.75)
    if k % 2 == 1:
        add(snare(), x, 0.3)
    if k % 4 == 0:
        ch, _ = chord_at(x, 22.0, CHORDS_PARTY)
        add(pad([m + 12 for m in ch], 2.0, a=0.15), x, 0.45)
    ch, _ = chord_at(x, 22.0, CHORDS_PARTY)
    add(pluck(ch[1] + 24, 0.12, 6), x + BEAT * 0.75, 0.15, pan=-0.5)

# 26-30 caraïbes (dembow + steel drum)
for bar in beats(26.0, 30.0, step=4 * BEAT):
    for b in (0, 2):
        add(kick(punch=0.7), bar + b * BEAT, 0.7)
    for b in (0.75, 1.5, 2.75, 3.5):
        add(snare(0.18), bar + b * BEAT, 0.28)
    for i, m in enumerate([76, 79, 81, 79, 76, 74, 72, 74]):
        add(steel(m), bar + i * BEAT / 2, 0.3, pan=0.3 * (1 if i % 2 else -1))
for x in beats(26.0, 30.0, step=BEAT / 2):
    add(hat(0.04), x, 0.12)
    _, idx = chord_at(x, 26.0, CHORDS_PARTY)
for x in beats(26.0, 30.0):
    _, idx = chord_at(x, 26.0, CHORDS_PARTY)
    add(bass(ROOTS_PARTY[idx], 0.45), x, 0.5)

# 30-34.4 montée
for x in beats(30.0, 34.4):
    add(kick(punch=0.8), x, 0.6)
    add(hat(0.05), x + BEAT / 2, 0.15)
add(pad([57, 60, 64, 69], 4.6, a=0.8), 30.0, 0.45)
add(noise_riser(7.0), 30.0, 0.22)
roll_t = 32.4
step = BEAT / 2
while roll_t < 34.4:
    add(snare(0.12), roll_t, 0.12 + 0.2 * (roll_t - 32.4) / 2)
    roll_t += step
    step = max(step * 0.82, 0.045)

# 34.4-37 compte à rebours : 3 battements sur les chiffres 3, 2, 1
for i, x in enumerate([34.5, 35.35, 36.2]):
    add(kick(0.6, punch=1.3), x, 0.9)
    add(bell(81 + i * 2), x, 0.18)

# 37 impact + drop minuit
add(impact(), 37.0, 0.9)
for i, m in enumerate([96, 100, 103, 108, 103, 100]):
    add(bell(m), 37.05 + i * 0.12, 0.1, pan=0.6 * (-1) ** i)
for x in beats(37.0, 47.0):
    k = round((x - 37.0) / BEAT)
    add(kick(), x, 0.85)
    add(hat(0.09), x + BEAT / 2, 0.24, pan=0.25)
    add(hat(0.03), x + BEAT / 4, 0.08, pan=-0.3)
    if k % 2 == 1:
        add(clap(), x, 0.4)
    ch, idx = chord_at(x, 37.0, CHORDS_PARTY)
    add(saw_stab([m + 12 for m in ch], 0.18), x + BEAT / 2, 0.24 if x < 41 else 0.16)
    if k % 4 == 0:
        add(pad([m + 12 for m in ch], 2.0, a=0.3), x, 0.3)
    add(bass(ROOTS_PARTY[idx], 0.3), x + BEAT / 2, 0.55)

# 47-54 outro
for x in beats(47.0, 52.0):
    add(kick(punch=0.6), x, 0.5 * (52.0 - x) / 5 + 0.1)
    add(hat(0.05), x + BEAT / 2, 0.12)
add(pad([57, 60, 64, 67, 72], 7.0, a=1.0), 47.0, 0.55)
for i, m in enumerate([81, 84, 88, 93]):
    add(bell(m), 52.0 + i * 0.15, 0.12)

# master : léger bus compression + normalisation à -1 dBFS crête
out = np.tanh(out * 1.4) / np.tanh(1.4)
fade = np.ones(N)
fade[: int(0.05 * SR)] = np.linspace(0, 1, int(0.05 * SR))
fade[-int(1.2 * SR) :] = np.linspace(1, 0, int(1.2 * SR))
out *= fade[:, None]
out *= 10 ** (-1 / 20) / np.max(np.abs(out))

pcm = (out * 32767).astype(np.int16)
with wave.open(sys.argv[1] if len(sys.argv) > 1 else "musique-travail.wav", "wb") as w:
    w.setnchannels(2)
    w.setsampwidth(2)
    w.setframerate(SR)
    w.writeframes(pcm.tobytes())
print("ok", DUR, "s")
