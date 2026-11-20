"""Base vidéo 1080x1920 de la souris d'agneau (plans tirés du ralenti, sans son), puis base.mp4.
Le ralenti src/ralenti.mp4 vient de src/plat.mp4 (vidéo de Michael) : setpts=2, minterpolate 30 i/s.
Chaque plan lit un passage différent du ralenti : aucun passage n'est réutilisé."""
import os, subprocess
D = os.path.dirname(os.path.abspath(__file__))
FPS = 30
# (début, fin, source, zoom départ, zoom fin, point visé x, y en 0..1)
PLAN = [
 (0.00, 5.20, "ralenti", 1.00, 1.09, 0.50, 0.50),   # plat entier, vapeur
 (5.20, 8.35, "ralenti", 1.60, 1.74, 0.30, 0.48),   # la souris, confite dans son jus
 (8.35, 11.35, "ralenti", 1.75, 1.88, 0.70, 0.53),  # l'écrasé de pommes de terre
 (11.35, 13.85, "ralenti", 2.05, 2.22, 0.33, 0.62), # la viande, les carottes, le jus
 (13.85, 15.70, "ralenti", 1.14, 1.00, 0.50, 0.52), # retour au plat entier (titre)
 (15.70, 19.00, "pergola", 1.00, 1.10, 0.62, 0.50), # la Villa Beach le soir
 (19.00, 23.00, "noir", 1, 1, 0.5, 0.5),            # carte de fin (dessinée par habillage.html)
]
DUR = 23.0
def run(a): subprocess.run(["ffmpeg", "-y", "-v", "error", *a], check=True)
os.makedirs(f"{D}/seg", exist_ok=True)
files = []
for i, (t0, t1, src, z0, z1, fx, fy) in enumerate(PLAN):
    dur = round(t1 - t0, 3); n = int(round(dur * FPS)); out = f"{D}/seg/{i:02d}.mp4"; files.append(out)
    z = f"({z0}+({z1}-{z0})*t/{dur})"
    if src == "noir":
        run(["-f", "lavfi", "-i", f"color=c=0x0d0a07:s=1080x1920:r={FPS}:d={dur}", "-frames:v", str(n), "-c:v", "libx264", "-crf", "16", "-pix_fmt", "yuv420p", out]); continue
    if src == "ralenti":
        inp = ["-ss", str(t0), "-t", str(dur), "-i", f"{D}/src/ralenti.mp4"]
    else:
        inp = ["-loop", "1", "-framerate", str(FPS), "-t", str(dur), "-i", f"{D}/journal/pergola.jpg"]
    flt = (f"[0:v]fps={FPS},setsar=1,scale=1080:1920:force_original_aspect_ratio=increase,"
           f"scale=w='trunc(iw*{z}/2)*2':h='trunc(ih*{z}/2)*2':eval=frame,"
           f"crop=1080:1920:x='clip(iw*{fx}-540,0,iw-1080)':y='clip(ih*{fy}-960,0,ih-1920)',"
           # étalonnage chaud, léger contraste, vignette
           f"eq=contrast=1.06:saturation=1.12:gamma=0.98,colorbalance=rm=0.04:gm=0.0:bm=-0.04:rh=0.03:bh=-0.03,"
           f"vignette=PI/4.6,format=yuv420p[v]")
    run([*inp, "-filter_complex", flt, "-map", "[v]", "-frames:v", str(n), "-r", str(FPS), "-an",
         "-c:v", "libx264", "-preset", "medium", "-crf", "16", out])
    print(i, src, t0, t1)
open(f"{D}/seg/liste.txt", "w").write("".join(f"file '{f}'\n" for f in files))
run(["-f", "concat", "-safe", "0", "-i", f"{D}/seg/liste.txt", "-c", "copy", f"{D}/base.mp4"])
print("base.mp4 ok")
