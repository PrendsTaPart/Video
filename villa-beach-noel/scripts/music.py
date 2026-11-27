#!/usr/bin/env python3
"""Musique originale de travail (synthèse numpy) — arrangement de deux mélodies du domaine public :
« Stille Nacht / Douce nuit » (F. X. Gruber, 1818) et « Jingle Bells » (J. Pierpont, 1857).
Interprétation synthétisée ici, aucun échantillon tiers : droits compatibles avec la diffusion promo.

Calée sur le film principal de 55 s :
  0–11,5 s  intro douce (célesta + nappe) « Douce nuit »  -> accroche émotionnelle
  11,5–31 s Jingle Bells léger (célesta, pizz, grelots)     -> dîner, menu enfant
  31–41 s   plein (batterie balais, cuivres, glockenspiel)   -> ambiance festive
  41–47 s   retombée douce                                   -> phrase émotionnelle
  47–55 s   reprise festive + accord final qui résonne       -> réservation
Usage : python3 scripts/music.py audio/music/music.wav
"""
import sys
import numpy as np

SR = 44100
DUR = 56.0
N = int(SR * DUR)
L = np.zeros(N)
R = np.zeros(N)
rng = np.random.default_rng(23)


def midi(n):
    return 440.0 * 2 ** ((n - 69) / 12)


NOTE = {"C": 0, "D": 2, "E": 4, "F": 5, "G": 7, "A": 9, "B": 11}


def nm(s):  # "E5", "F#4"
    k = NOTE[s[0]]; i = 1
    if s[i] == "#": k += 1; i += 1
    return 12 * (int(s[i:]) + 1) + k


def add(sig, t, pan=0.0, gain=1.0):
    i = int(t * SR)
    if i >= N: return
    sig = sig[: N - i] * gain
    L[i:i + len(sig)] += sig * np.sqrt(0.5 * (1 - pan))
    R[i:i + len(sig)] += sig * np.sqrt(0.5 * (1 + pan))


def env(n, a, tau):
    t = np.arange(n) / SR
    e = np.exp(-t / tau)
    na = max(1, int(a * SR)); e[:na] *= np.linspace(0, 1, na)
    return e


def celesta(f, d=1.6):
    n = int(d * SR); t = np.arange(n) / SR
    s = (np.sin(2 * np.pi * f * t) + 0.35 * np.sin(2 * np.pi * 2 * f * t) * np.exp(-t / 0.25)
         + 0.12 * np.sin(2 * np.pi * 4.07 * f * t) * np.exp(-t / 0.08))
    return s * env(n, 0.004, 0.7)


def glock(f, d=1.2):
    n = int(d * SR); t = np.arange(n) / SR
    s = np.sin(2 * np.pi * f * t) + 0.25 * np.sin(2 * np.pi * 2.76 * f * t) * np.exp(-t / 0.15)
    return s * env(n, 0.002, 0.45)


def pizz(f, d=0.6):
    n = int(d * SR); t = np.arange(n) / SR
    s = np.sin(2 * np.pi * f * t) + 0.4 * np.sin(2 * np.pi * 2 * f * t) + 0.15 * np.sin(2 * np.pi * 3 * f * t)
    return s * env(n, 0.006, 0.18)


def pad(freqs, d, a=0.6):
    n = int(d * SR); t = np.arange(n) / SR
    s = np.zeros(n)
    for f in freqs:
        vib = 1 + 0.003 * np.sin(2 * np.pi * 5 * t)
        for h, g in ((1, 1), (2, 0.25), (3, 0.08)):
            s += g * np.sin(2 * np.pi * f * h * t * vib + rng.random() * 6)
    e = np.minimum(1, t / a) * np.minimum(1, (d - t) / 0.5).clip(0)
    return s * e / len(freqs)


def brass(freqs, d=0.35):
    n = int(d * SR); t = np.arange(n) / SR
    s = np.zeros(n)
    for f in freqs:
        for h in range(1, 7):
            s += np.sin(2 * np.pi * f * h * t) / h ** 1.3
    return s * env(n, 0.015, 0.16) / len(freqs)


def noise_burst(d, tau, hp=True):
    n = int(d * SR)
    x = rng.standard_normal(n)
    if hp: x = np.diff(np.concatenate([[0], x]))  # passe-haut grossier
    return x * env(n, 0.001, tau)


def sleigh(d=0.12):
    n = int(d * SR); t = np.arange(n) / SR
    s = noise_burst(d, 0.035) * 0.5
    for f in (5200, 6900, 8100):
        s += 0.25 * np.sin(2 * np.pi * f * t) * np.exp(-t / 0.05)
    return s


def kick():
    n = int(0.3 * SR); t = np.arange(n) / SR
    f = 110 * np.exp(-t / 0.05) + 45
    return np.sin(2 * np.pi * np.cumsum(f) / SR) * env(n, 0.002, 0.12)


def chord(name, octv=4):
    root = {"C": "C", "F": "F", "G": "G", "G7": "G", "D7": "D", "Am": "A"}[name]
    r = nm(f"{root}{octv}")
    iv = {"C": (0, 4, 7), "F": (0, 4, 7), "G": (0, 4, 7), "G7": (0, 4, 10), "D7": (0, 4, 10), "Am": (0, 3, 7)}[name]
    return [midi(r + i) for i in iv], midi(r - 12)


def intensity(t):
    """0 = intime, 1 = léger, 2 = plein"""
    if t < 11.5: return 0
    if t < 31: return 1
    if t < 41: return 2
    if t < 47: return 0.5
    return 2


# ---------- A : Douce nuit (6/8, croche = 0.24 s) ----------
E8 = 0.24
silent = [("G5", 3), ("A5", 1), ("G5", 2), ("E5", 6), ("G5", 3), ("A5", 1), ("G5", 2), ("E5", 6),
          ("D6", 4), ("D6", 2), ("B5", 6), ("C6", 4), ("C6", 2), ("G5", 6)]
t = 0.15
for note, d in silent:
    add(celesta(midi(nm(note)), 2.2), t, pan=0.15, gain=0.5)
    t += d * E8
for i, ch in enumerate(["C", "C", "G7", "C"]):
    fr, b = chord(ch, 4)
    add(pad(fr, 12 * E8 + 0.6, a=0.9), 0.15 + i * 12 * E8, gain=0.22)
    add(pizz(b, 1.2), 0.15 + i * 12 * E8, gain=0.25)
# carillon de transition
for k, n in enumerate(["G6", "E6", "C6", "G5"]):
    add(glock(midi(nm(n))), 10.9 + k * 0.12, pan=-0.2, gain=0.22)

# ---------- B : Jingle Bells (noire = 60/116 s) ----------
Q = 60 / 116
BAR = 4 * Q
T0 = 11.5
chorus = [
    [("E5", 1), ("E5", 1), ("E5", 2)], [("E5", 1), ("E5", 1), ("E5", 2)],
    [("E5", 1), ("G5", 1), ("C5", 1.5), ("D5", 0.5)], [("E5", 4)],
    [("F5", 1), ("F5", 1), ("F5", 1.5), ("F5", 0.5)], [("F5", 1), ("E5", 1), ("E5", 1), ("E5", 0.5), ("E5", 0.5)],
    [("E5", 1), ("D5", 1), ("D5", 1), ("E5", 1)], [("D5", 2), ("G5", 2)],
    [("E5", 1), ("E5", 1), ("E5", 2)], [("E5", 1), ("E5", 1), ("E5", 2)],
    [("E5", 1), ("G5", 1), ("C5", 1.5), ("D5", 0.5)], [("E5", 4)],
    [("F5", 1), ("F5", 1), ("F5", 1.5), ("F5", 0.5)], [("F5", 1), ("E5", 1), ("E5", 1), ("E5", 0.5), ("E5", 0.5)],
    [("G5", 1), ("G5", 1), ("F5", 1), ("D5", 1)], [("C5", 4)],
]
chords = ["C", "C", "C", "C", "F", "C", "D7", "G", "C", "C", "C", "C", "F", "C", "G7", "C"]
# 1 mesure d'intro (vamp) + 16 mesures + tag (4 dernières mesures)
bars = [(None, "C")] + list(zip(chorus, chords)) + list(zip(chorus[12:], chords[12:]))
for bi, (mel, ch) in enumerate(bars):
    bt = T0 + bi * BAR
    if bt > 54.5: break
    lvl = intensity(bt + 0.01)
    fr, b = chord(ch, 4)
    last = bi == len(bars) - 1
    # basse pizz : fondamentale / quinte
    for beat in range(4):
        f = b if beat % 2 == 0 else b * 1.5
        add(pizz(f, 0.6 if not last else 3.0), bt + beat * Q, gain=0.32 if lvl else 0.2)
        if last: break
    # accords (contretemps)
    for beat in range(4):
        if last and beat: break
        add(pad(fr, Q * 0.9 if not last else 3.2, a=0.02), bt + beat * Q + (0 if last else Q * 0.5), gain=0.11 if lvl >= 1 else 0.07)
    # mélodie
    if mel:
        tt = bt
        for n, d in mel:
            add(celesta(midi(nm(n)), 1.4 if not last else 3.0), tt, pan=0.12, gain=0.42 if lvl else 0.3)
            if lvl >= 2: add(glock(midi(nm(n) + 12)), tt, pan=-0.25, gain=0.12)
            tt += d * Q
    if last:
        for k, n in enumerate(["C6", "E6", "G6", "C7"]):
            add(glock(midi(nm(n)), 2.5), bt + k * 0.09, pan=0.2, gain=0.2)
        continue
    # grelots
    if lvl >= 1:
        for e in range(8):
            add(sleigh(), bt + e * Q / 2, pan=0.35 * (1 if e % 2 else -1), gain=0.09 if lvl < 2 else 0.14)
    # batterie balais + kick
    if lvl >= 2:
        for beat in range(4):
            if beat % 2 == 0: add(kick(), bt + beat * Q, gain=0.5)
            else: add(noise_burst(0.25, 0.09), bt + beat * Q, gain=0.12)
        # cuivres sur les temps 2 et 4 (accents)
        add(brass(fr, 0.3), bt + Q, pan=-0.3, gain=0.18)
        add(brass(fr, 0.3), bt + 3 * Q, pan=-0.3, gain=0.18)

# ---------- master ----------
mix = np.stack([L, R], 1)
# réverbération simple (échos multiples)
rev = np.zeros_like(mix)
for dly, g in ((0.031, 0.35), (0.047, 0.3), (0.071, 0.25), (0.113, 0.2), (0.167, 0.15), (0.241, 0.1)):
    k = int(dly * SR); rev[k:] += mix[:-k] * g
mix = mix + 0.6 * rev
fade = np.ones(N); fs = int(1.5 * SR); fade[-fs:] = np.linspace(1, 0, fs)
mix *= fade[:, None]
mix /= np.max(np.abs(mix)) * 1.12
import wave
out = sys.argv[1] if len(sys.argv) > 1 else "music.wav"
with wave.open(out, "wb") as w:
    w.setnchannels(2); w.setsampwidth(2); w.setframerate(SR)
    w.writeframes((mix * 32767).astype("<i2").tobytes())
print("ok", out)
