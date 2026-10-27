"""Mixage voix + musique, mux, short et SRT. Usage : python3 finish.py v32 musique.mp3 nom "a-b,c-d,..." """
import json, subprocess, sys

d, music, name, segs = sys.argv[1], sys.argv[2], sys.argv[3], sys.argv[4]
c = json.load(open(f"{d}/cfg.json"))
P, A, E, lead, dur = c["P"], c["A"], c["E"], c["lead"], c["dur"]
run = lambda *a: (print("ffmpeg", a[-1], flush=True), subprocess.run(["ffmpeg", "-y", "-v", "error", *a], check=True, timeout=240))

# 1. Voix : chaque section placée au début de sa scène.
inputs, flt = ["-i", f"{d}/vo.mp3"], []
for i in range(len(P)):
    a0, a1 = max(0, A[i] - .06), E[i] + .25
    ms = int((P[i] + lead - (A[i] - a0)) * 1000)
    flt.append(f"[0:a]atrim={a0}:{a1},asetpts=PTS-STARTPTS,adelay={ms}|{ms}[v{i}]")
flt.append("".join(f"[v{i}]" for i in range(len(P))) + f"amix=inputs={len(P)}:normalize=0,apad=whole_dur={dur}[vo]")
flt.append("[vo]asplit[vo1][vo2]")
flt.append(f"[1:a]volume=0.30,afade=t=in:d=1,afade=t=out:st={dur-2.5}:d=2.5[mu]")
flt.append("[mu][vo1]sidechaincompress=threshold=0.03:ratio=8:attack=20:release=400[duck]")
flt.append("[vo2][duck]amix=inputs=2:normalize=0:duration=first,loudnorm=I=-14:TP=-1.5:LRA=11,aresample=48000[out]")
run("-stream_loop", "4", "-i", music, "-t", str(dur), "-ar", "48000", "-ac", "2", f"{d}/bed.wav")
run(*inputs, "-i", f"{d}/bed.wav", "-filter_complex", ";".join(flt), "-map", "[out]", "-t", str(dur), "-c:a", "pcm_s16le", f"{d}/mix.wav")

# 2. Vidéo finale.
final = f"{d}/{name}-final-{round(dur)}s.mp4"
run("-i", f"{d}/frames.mp4", "-i", f"{d}/mix.wav", "-c:v", "copy", "-c:a", "aac", "-b:a", "192k", "-shortest", "-movflags", "+faststart", final)

# 3. SRT.
def ts(x):
    ms = int(round(x * 1000)); h, ms = divmod(ms, 3600000); m, ms = divmod(ms, 60000); s, ms = divmod(ms, 1000)
    return f"{h:02}:{m:02}:{s:02},{ms:03}"
def srt(cues, path):
    open(path, "w").write("\n".join(f"{k+1}\n{ts(a)} --> {ts(b)}\n{t}\n" for k, (a, b, t) in enumerate(cues)))
srt(c["cues"], f"{d}/{name}-sous-titres.srt")

# 4. Short : segments recollés (coupes sur des fins de scène).
S = [tuple(map(float, s.split("-"))) for s in segs.split(",")]
parts = "".join(f"[0:v]trim={a}:{b},setpts=PTS-STARTPTS[v{k}];[0:a]atrim={a}:{b},asetpts=PTS-STARTPTS,afade=t=in:d=0.08,afade=t=out:st={b-a-.12:.3f}:d=0.12[a{k}];" for k, (a, b) in enumerate(S))
parts += "".join(f"[v{k}][a{k}]" for k in range(len(S))) + f"concat=n={len(S)}:v=1:a=1[v][a]"
tot = sum(b - a for a, b in S)
short = f"{d}/{name}-short-{round(tot)}s.mp4"
run("-i", final, "-filter_complex", parts, "-map", "[v]", "-map", "[a]", "-c:v", "libx264", "-crf", "19", "-pix_fmt", "yuv420p", "-c:a", "aac", "-b:a", "192k", "-movflags", "+faststart", short)
sc, off = [], 0.0
for a, b in S:
    sc += [[max(x, a) - a + off, min(y, b) - a + off, t] for x, y, t in c["cues"] if x < b and y > a]
    off += b - a
srt(sc, f"{d}/{name}-short-{round(tot)}s.srt")
print(final, short, round(tot, 1))
