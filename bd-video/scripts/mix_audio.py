#!/usr/bin/env python3
"""Étape 4 — mixage audio d'une vidéo montée, puis multiplexage avec le rendu HyperFrames.

    python3 bd-video/scripts/mix_audio.py ep01 renders/episodes/ep01-video.mp4 renders/episodes/ep01.mp4

Lit montage/<nom>/timeline.json (début de chaque plan) et place :
  - chaque voix audio/vo/<id>.mp3 à son départ (agents IA : léger filtre « synthétique ») ;
  - la musique de la partie audio/music/<partie>.mp3, baissée automatiquement sous la voix (sidechain) ;
  - les bruitages déclarés dans SFX ;
puis normalise à −14 LUFS (loudnorm) et multiplexe en MP4 H.264 + AAC.
Les fichiers absents sont ignorés (on peut mixer une animatique sans musique, par exemple).
"""
import json
import os
import subprocess
import sys

ROOT = os.path.join(subprocess.check_output(["git", "rev-parse", "--show-toplevel"], text=True).strip(), "bd-video")
SYNTH = {"predibot", "iris", "caroline", "jarvis", "assistant-ia"}
FILTERS = {  # traitement par voix IA
    "caroline": "highpass=f=300,lowpass=f=3400,acompressor=threshold=-18dB:ratio=4",   # téléphone
    "jarvis": "highpass=f=200,lowpass=f=5000,aecho=0.6:0.5:18:0.25",                   # haut-parleur de borne
    "_ia": "aecho=0.7:0.5:12:0.18,highpass=f=120,treble=g=3",                          # léger timbre synthétique
}
MUSIC = {  # partie → fichier d'ambiance (étape 2)
    "Ouverture": "ouverture", "Prologue": "prologue",
    "Partie 1 · Une journée sans FoodEatUp": "partie1-tension",
    "Partie 2 · La même journée, avec FoodEatUp": "partie2-soulagement",
    "Partie 3 · La brigade passe à l'écran": "partie3-energie",
    "Partie 4 · Expansion & franchise": "partie4-epique",
    "Partie 5 · Le laboratoire et les agents": "partie5-futuriste",
    "Partie 6 · Une infinité de solutions": "partie6-lumineuse",
    "Épilogue": "epilogue-emotion", "Fermeture": "epilogue-emotion",
}
SFX = {  # plan → (bruitage, décalage en s, volume)
    "p16-c1-01": ("sfx/telephone.mp3", 0.0, 0.7),
    "p15-c1-01": ("sfx/friture.mp3", 0.0, 0.5),
    "p23-c1-01": ("../../hero-video/assets/sfx/son-imprimante-z.mp3", 0.3, 0.6),
    "p57-c2-01": ("sfx/ecran-allume.mp3", 0.4, 0.7),
}


def main(name, video_in, video_out):
    tl = json.load(open(os.path.join(ROOT, "montage", name, "timeline.json")))
    inputs, chains, vo_labels, mus_labels = [], [], [], []

    def add_input(path):
        inputs.extend(["-i", path])
        return len(inputs) // 2 - 1

    for s in tl["shots"]:
        f = os.path.join(ROOT, "audio", "vo", f"{s['id']}.mp3")
        if s["type"] == "titre" or not os.path.exists(f):
            continue
        i = add_input(f)
        voice = s.get("voice") or ""
        fx = FILTERS.get(voice) or (FILTERS["_ia"] if voice in SYNTH else "anull")
        ms = int(s["start"] * 1000)
        chains.append(f"[{i}:a]aresample=48000,aformat=channel_layouts=stereo,{fx},adelay={ms}|{ms}[v{i}]")
        vo_labels.append(f"[v{i}]")
    for sid, (rel, off, vol) in SFX.items():
        s = next((x for x in tl["shots"] if x["id"] == sid), None)
        f = os.path.normpath(os.path.join(ROOT, "audio", rel))
        if s and os.path.exists(f):
            i = add_input(f)
            ms = int((s["start"] + off) * 1000)
            chains.append(f"[{i}:a]aresample=48000,aformat=channel_layouts=stereo,volume={vol},adelay={ms}|{ms}[x{i}]")
            vo_labels.append(f"[x{i}]")
    # Musique : un bloc par partie, de son premier plan à son dernier, fondu de 1 s.
    parts = {}
    for s in tl["shots"]:
        a = parts.setdefault(s["part"], [s["start"], s["start"] + s["dur"]])
        a[1] = s["start"] + s["dur"]
    for part, (a, b) in parts.items():
        f = os.path.join(ROOT, "audio", "music", f"{MUSIC.get(part, '')}.mp3")
        if not os.path.exists(f):
            continue
        i = add_input(f)
        d = b - a + (tl["end"][1] if b >= tl["end"][0] - 0.01 else 0)
        ms = int(a * 1000)
        chains.append(f"[{i}:a]aresample=48000,aformat=channel_layouts=stereo,aloop=loop=-1:size=2e9,atrim=0:{d:.2f},"
                      f"afade=t=in:d=1,afade=t=out:st={max(0, d-1.2):.2f}:d=1.2,volume=0.55,adelay={ms}|{ms}[m{i}]")
        mus_labels.append(f"[m{i}]")

    total = tl["duration"]
    if not vo_labels and not mus_labels:
        subprocess.run(["ffmpeg", "-v", "error", "-y", "-i", video_in, "-f", "lavfi", "-t", str(total), "-i",
                        "anullsrc=r=48000:cl=stereo", "-map", "0:v", "-map", "1:a", "-c:v", "copy", "-c:a", "aac",
                        "-shortest", video_out], check=True)
        print("aucun son disponible : piste muette")
        return
    g = []
    g.append(f"{''.join(vo_labels) or 'anullsrc=r=48000:cl=stereo,atrim=0:1'}amix=inputs={max(1,len(vo_labels))}:normalize=0:dropout_transition=0,apad=whole_dur={total}[voice]")
    if mus_labels:
        g.append(f"{''.join(mus_labels)}amix=inputs={len(mus_labels)}:normalize=0,apad=whole_dur={total}[music]")
        g.append("[voice]asplit=2[vk][vm]")
        g.append("[music][vk]sidechaincompress=threshold=0.03:ratio=8:attack=20:release=400[duck]")  # musique sous la voix
        g.append("[vm][duck]amix=inputs=2:normalize=0[mix]")
    else:
        g.append("[voice]anull[mix]")
    g.append(f"[mix]atrim=0:{total},loudnorm=I=-14:TP=-1.5:LRA=11[out]")
    graph = ";".join(chains + g)
    vidx = len(inputs) // 2
    cmd = ["ffmpeg", "-v", "error", "-y", *inputs, "-i", video_in, "-filter_complex", graph,
           "-map", f"{vidx}:v", "-map", "[out]", "-c:v", "copy", "-c:a", "aac", "-b:a", "192k", "-ar", "48000",
           "-movflags", "+faststart", video_out]
    subprocess.run(cmd, check=True)
    print(f"{video_out} : {len(vo_labels)} voix/bruitages, {len(mus_labels)} musiques, −14 LUFS")


if __name__ == "__main__":
    main(*sys.argv[1:4])
