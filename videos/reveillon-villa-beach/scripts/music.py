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

Usage : python3 scripts/music.py data/timeline.json assets/music/musique-travail.wav
"""
import sys
import wave

import numpy as np

import json
SR = 44100
# Plan musical : clé "music" d'un fichier timeline (sections style/start/end).
TL = json.load(open(sys.argv[1], encoding="utf-8"))
PLAN = TL["music"]
DUR = float(TL["format"]["duration"])
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


def sec_intro(a, b):
    add(pad([60, 64, 67, 71, 74], b - a + 0.6, a=min(1.2, (b - a) / 3)), a, 0.5)
    for i, m in enumerate([84, 88, 91, 95, 91, 96, 100, 95]):
        if a + 0.25 + i * 0.55 < b:
            add(bell(m), a + 0.25 + i * 0.55, 0.12, pan=(-0.5 if i % 2 else 0.5))
    k0 = a + (b - a) / 2
    for x in beats(k0, b):
        add(kick(punch=0.6), x, 0.35 * (x - k0 + 0.5) / (b - k0 + 0.5))


def sec_lounge(a, b):
    for x in beats(a, b):
        k = round((x - a) / BEAT)
        if k % 2 == 0:
            add(kick(punch=0.5), x, 0.45)
        add(hat(0.04), x + BEAT / 2, 0.12, pan=0.3)
        ch, idx = chord_at(x, a, CHORDS_LOUNGE)
        if k % 4 == 0:
            add(rhodes(ch, 2.0), x, 0.55)
        add(bass(ROOTS_LOUNGE[idx] + [0, 7, 12, 7][k % 4], 0.45), x, 0.45)
        if k % 4 == 1:
            add(woodblock(), x + BEAT / 2, 0.08, pan=-0.4)


def sec_house(a, b, light=False):
    for x in beats(a, b):
        k = round((x - a) / BEAT)
        add(kick(), x, 0.8 if not light else 0.65)
        add(hat(0.09), x + BEAT / 2, 0.22, pan=0.25)
        if k % 2 == 1:
            add(clap(), x, 0.35)
        ch, idx = chord_at(x, a, CHORDS_PARTY)
        add(saw_stab([m + 12 for m in ch]), x + BEAT / 2, 0.22 if not light else 0.15)
        add(bass(ROOTS_PARTY[idx], 0.3), x + BEAT / 2, 0.5)


def sec_latin(a, b):
    for bar in beats(a, b, step=8 * BEAT):
        for c in [0, 1.5, 3, 5, 6]:
            if bar + c * BEAT < b:
                add(woodblock(), bar + c * BEAT, 0.3, pan=0.2)
    for x in beats(a, b, step=BEAT / 2):
        k = round((x - a) / (BEAT / 2))
        ch, idx = chord_at(x, a, CHORDS_PARTY)
        add(pluck(ch[k % 3] + 12 * (1 + (k % 4 == 3)), 0.25, 4), x, 0.25, pan=-0.2)
        if k % 4 in (2, 3):
            add(conga(330 if k % 8 < 4 else 260), x, 0.35, pan=0.4)
    for x in beats(a, b):
        k = round((x - a) / BEAT)
        add(kick(punch=0.4), x, 0.3)
        _, idx = chord_at(x, a, CHORDS_PARTY)
        if k % 2 == 1:
            add(bass(ROOTS_PARTY[idx], 0.4), x + BEAT / 2, 0.55)
        add(conga(200), x + BEAT * 0.75, 0.25, pan=-0.4)


def sec_disco(a, b):
    for x in beats(a, b, step=BEAT / 2):
        k = round((x - a) / (BEAT / 2))
        _, idx = chord_at(x, a, CHORDS_PARTY)
        add(bass(ROOTS_PARTY[idx] + (12 if k % 2 else 0), 0.22), x, 0.55)
        add(hat(0.06 if k % 2 else 0.03), x, 0.2 if k % 2 else 0.1, pan=0.3)
    for x in beats(a, b):
        k = round((x - a) / BEAT)
        add(kick(), x, 0.75)
        if k % 2 == 1:
            add(snare(), x, 0.3)
        ch, _ = chord_at(x, a, CHORDS_PARTY)
        if k % 4 == 0:
            add(pad([m + 12 for m in ch], 2.0, a=0.15), x, 0.45)
        add(pluck(ch[1] + 24, 0.12, 6), x + BEAT * 0.75, 0.15, pan=-0.5)


def sec_carib(a, b):
    for bar in beats(a, b, step=4 * BEAT):
        for bb in (0, 2):
            add(kick(punch=0.7), bar + bb * BEAT, 0.7)
        for bb in (0.75, 1.5, 2.75, 3.5):
            add(snare(0.18), bar + bb * BEAT, 0.28)
        for i, m in enumerate([76, 79, 81, 79, 76, 74, 72, 74]):
            add(steel(m), bar + i * BEAT / 2, 0.3, pan=0.3 * (1 if i % 2 else -1))
    for x in beats(a, b, step=BEAT / 2):
        add(hat(0.04), x, 0.12)
    for x in beats(a, b):
        _, idx = chord_at(x, a, CHORDS_PARTY)
        add(bass(ROOTS_PARTY[idx], 0.45), x, 0.5)


def sec_build(a, b):
    for x in beats(a, b):
        add(kick(punch=0.8), x, 0.6)
        add(hat(0.05), x + BEAT / 2, 0.15)
    add(pad([57, 60, 64, 69], b - a + 0.2, a=0.8), a, 0.45)
    add(noise_riser(b - a + 2.5), a, 0.22)
    t0 = max(a, b - 2.0)
    step = BEAT / 2
    while t0 < b:
        add(snare(0.12), t0, 0.12 + 0.2 * (t0 - (b - 2.0)) / 2)
        t0 += step
        step = max(step * 0.82, 0.045)


def sec_countdown(beat_times):
    for i, x in enumerate(beat_times):
        add(kick(0.6, punch=1.3), x, 0.9)
        add(bell(81 + (i % 6) * 2), x, 0.16)


def sec_drop(a, b):
    add(impact(), a, 0.9)
    for i, m in enumerate([96, 100, 103, 108, 103, 100]):
        add(bell(m), a + 0.05 + i * 0.12, 0.1, pan=0.6 * (-1) ** i)
    sec_house(a, b)
    for x in beats(a, b, step=4 * BEAT):
        ch, _ = chord_at(x, a, CHORDS_PARTY)
        add(pad([m + 12 for m in ch], 2.0, a=0.3), x, 0.3)


def sec_outro(a, b):
    for x in beats(a, max(a, b - 2.0)):
        add(kick(punch=0.6), x, 0.5 * (b - 2.0 - x) / max(b - 2.0 - a, 0.5) + 0.1)
        add(hat(0.05), x + BEAT / 2, 0.12)
    add(pad([57, 60, 64, 67, 72], b - a, a=1.0), a, 0.55)
    for i, m in enumerate([81, 84, 88, 93]):
        add(bell(m), b - 2.0 + i * 0.15, 0.12)


STYLES = {"intro": sec_intro, "lounge": sec_lounge, "house": sec_house, "latin": sec_latin,
          "disco": sec_disco, "carib": sec_carib, "build": sec_build, "drop": sec_drop, "outro": sec_outro,
          "houselight": lambda a, b: sec_house(a, b, light=True)}

for sec in PLAN["sections"]:
    if sec["style"] == "countdown":
        sec_countdown(sec["beats"])
    else:
        STYLES[sec["style"]](sec["start"], sec["end"])

# master : léger bus compression + normalisation à -1 dBFS crête
out = np.tanh(out * 1.4) / np.tanh(1.4)
fade = np.ones(N)
fade[: int(0.05 * SR)] = np.linspace(0, 1, int(0.05 * SR))
fade[-int(1.2 * SR) :] = np.linspace(1, 0, int(1.2 * SR))
out *= fade[:, None]
out *= 10 ** (-1 / 20) / np.max(np.abs(out))

pcm = (out * 32767).astype(np.int16)
with wave.open(sys.argv[2], "wb") as w:
    w.setnchannels(2)
    w.setsampwidth(2)
    w.setframerate(SR)
    w.writeframes(pcm.tobytes())
print("ok", DUR, "s")
