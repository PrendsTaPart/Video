"""Monte la base vidéo 1080x1920 (plans calés sur les temps de la musique), puis l'assemble.
Sorties : seg/NN.mp4, base.mp4. Les textes et flashs sont ajoutés ensuite par habillage.html (rendre.js)."""
import json, os, subprocess
D = os.path.dirname(os.path.abspath(__file__))
U = "/root/.claude/uploads/18a597f6-932b-5321-aabc-7569a066370d"
P = {  # photos fournies par Michael (nom d'origine -> fichier)
 "duo_combattant": f"{U}/5c85760e-image.jpg",   # 1000012796
 "main_bouche":   f"{U}/7970cc66-image.jpg",   # 1000012797
 "miroir":        f"{U}/9b67c648-image.jpg",   # 1000012804
 "grillage":      f"{U}/11dd92d1-image.jpg",   # 1000012803
 "montre":        f"{U}/3af20419-image.jpg",   # 1000012798
 "interview":     f"{U}/0abd8cc9-image.jpg",   # 1000012806
 "danseuses":     f"{U}/16af4dbe-image.jpg",   # 1000012807
 "badge_micro":   f"{U}/70ce2f68-image.jpg",   # 1000012812
 "bras_leve":     f"{U}/fc0d57e5-image.jpg",   # 1000012801
 "pointe":        f"{U}/7bc12636-image.jpg",   # 1000012794
}
V = {k: f"{D}/src/{k}.mp4" for k in ["WA0011", "WA0012", "WA0018", "WA0019"]}
B19 = "crop=576:324:0:462,"  # bande utile de l'enregistrement de la retransmission
# (source, type, début dans la source, début, fin dans la vidéo finale, cadrage x 0..1, punch)
PLAN = [
 ("badge_micro", "photo", 0, 0.00, 3.46, 0.5, False),
 ("badge_micro", "photo", 0, 3.46, 6.90, 0.5, False),
 ("miroir", "photo", 0, 6.90, 10.31, 0.62, False),
 ("WA0011", "video", 2.0, 10.31, 13.75, 0.5, False),
 ("montre", "photo", 0, 13.75, 17.18, 0.4, False),
 ("main_bouche", "photo", 0, 17.18, 20.62, 0.5, False),
 ("grillage", "photo", 0, 20.62, 24.06, 0.5, False),
 ("WA0018", "video", 1.0, 24.06, 25.75, 0.5, True),
 ("pointe", "photo", 0, 25.75, 26.61, 0.5, True),
 ("WA0012", "video", 0.5, 26.61, 28.33, 0.5, True),
 ("danseuses", "photo", 0, 28.33, 29.19, 0.45, True),
 ("WA0019", "video19", 89.6, 29.19, 30.91, 0.5, True),
 ("bras_leve", "photo", 0, 30.91, 31.76, 0.4, True),
 ("WA0019", "video19", 31.0, 31.76, 33.46, 0.5, True),
 ("interview", "photo", 0, 33.46, 35.18, 0.78, True),
 ("WA0012", "video", 11.0, 35.18, 36.90, 0.5, True),
 ("duo_combattant", "photo", 0, 36.90, 38.61, 0.5, True),
 ("WA0019", "video19", 92.0, 38.61, 40.33, 0.5, True),
 ("WA0019", "video19", 139.25, 40.33, 49.60, 0.5, False),   # vraie voix : « Allez, attention, mesdames et messieurs… »
 ("pointe", "photo", 0, 49.60, 50.62, 0.5, True),
 ("WA0012", "video", 6.0, 50.62, 51.48, 0.5, True),
 ("bras_leve", "photo", 0, 51.48, 52.34, 0.4, True),
 ("duo_combattant", "photo", 0, 52.34, 53.20, 0.5, True),
 ("main_bouche", "photo", 0, 53.20, 58.50, 0.5, False),  # carte de fin
]
FPS = 30
os.makedirs(f"{D}/seg", exist_ok=True)
def run(a): subprocess.run(["ffmpeg", "-y", "-v", "error", *a], check=True)
files = []
for i, (src, typ, ss, t0, t1, cx, punch) in enumerate(PLAN):
    dur = round(t1 - t0, 3); out = f"{D}/seg/{i:02d}.mp4"; files.append(out)
    n = int(round(dur * FPS))
    # zoom : lent (1.0 -> 1.08) ou « punch » (1.18 -> 1.0 en 0,25 s)
    z = "(1.18-0.18*min(t/0.25\\,1))" if punch else f"(1+0.08*t/{dur})"
    if typ == "photo":
        inp = ["-loop", "1", "-framerate", str(FPS), "-t", str(dur), "-i", P[src]]
        pre = ""
    else:
        inp = ["-ss", str(ss), "-t", str(dur), "-i", V[src]]
        pre = B19 if typ == "video19" else ""
    # fond flou + image ajustée (si format éloigné du 9:16), sinon recadrage plein écran
    flt = (f"[0:v]{pre}fps={FPS},setsar=1,split[a][b];"
           f"[a]scale=1080:1920:force_original_aspect_ratio=increase,crop=1080:1920,boxblur=30:3,eq=brightness=-0.25[bg];"
           f"[b]scale=-2:1100,"
           f"scale=w='trunc(iw*{z}/2)*2':h='trunc(ih*{z}/2)*2':eval=frame[fg];"
           f"[bg][fg]overlay=x='(W-w)*{cx}':y='(H-h)/2':shortest=1,crop=1080:1920,format=yuv420p[v]")
    # images verticales : plein écran
    if typ != "video19" and src not in ("interview", "danseuses", "bras_leve") :
        flt = (f"[0:v]{pre}fps={FPS},setsar=1,scale=1080:1920:force_original_aspect_ratio=increase,"
               f"scale=w='trunc(iw*{z}/2)*2':h='trunc(ih*{z}/2)*2':eval=frame,"
               f"crop=1080:1920:x='(iw-1080)*{cx}':y='(ih-1920)/2',format=yuv420p[v]")
    run([*inp, "-filter_complex", flt, "-map", "[v]", "-frames:v", str(n), "-r", str(FPS), "-an",
         "-c:v", "libx264", "-preset", "veryfast", "-crf", "18", out])
    print(i, src, t0, t1)
open(f"{D}/seg/liste.txt", "w").write("".join(f"file '{f}'\n" for f in files))
run(["-f", "concat", "-safe", "0", "-i", f"{D}/seg/liste.txt", "-c", "copy", f"{D}/base.mp4"])
json.dump([dict(src=p[0], t0=p[3], t1=p[4]) for p in PLAN], open(f"{D}/plan.json", "w"), ensure_ascii=False, indent=0)
print("base.mp4 ok")
