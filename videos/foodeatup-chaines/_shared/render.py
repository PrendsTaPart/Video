#!/usr/bin/env python3
"""
Rend un bloc en MP4 : capture temps réel Chromium -> détourage -> H.264.

    python3 render.py <bloc>        # boulangerie | restauration | fin

Pourquoi une capture et pas le pipeline HyperFrames : le MCP refuse l'import
(« Import URL host is not an allowed Claude Design origin ») depuis une URL
arbitraire — la voie d'import passe par le bouton « Send to HyperFrames ».

Deux écarts assumés par rapport au rendu cloud :
  - la transition shader `cinematic-zoom` est remplacée par un fondu croisé de
    même durée au même instant (les shaders WebGL plantent le renderer headless) ;
  - le son est ajouté ensuite par mixaudio.py.

Le point de départ de la capture est DÉTECTÉ, pas estimé : la vidéo enregistrée
commence par plusieurs secondes de page vide (chargement + attente), et une
estimation à la main décalait le master de ~0,5 s — ce qui faisait tomber les
contrôles à côté des coupes et masquait un défaut réel.
"""

import pathlib
import re
import shutil
import subprocess
import sys

from PIL import Image

FF = "/usr/local/lib/python3.11/dist-packages/imageio_ffmpeg/binaries/ffmpeg-linux-x86_64-v7.0.2"
CHROME = "/opt/pw-browsers/chromium-1194/chrome-linux/chrome"
HERE = pathlib.Path(__file__).resolve().parent
ROOT = HERE.parent
TMP = pathlib.Path("/tmp/claude-0/-home-user-Video/91c5512a-758f-5859-81e9-91a2002839b0/scratchpad/render")

DUREES = {"boulangerie": 55.0, "restauration": 55.0, "fin": 22.0}
CREME = (252, 249, 230)
FONDU = 0.5      # remplace le shader, au même instant
XF_TIME = 27.75


def encre(png: pathlib.Path) -> int:
    """Pixels qui ne sont pas le fond crème. Détecte AUSSI le contenu clair —
    un simple comptage de pixels sombres ratait les carnets estompés et le
    texte fin, et concluait à tort à des images vides."""
    im = Image.open(png).convert("RGB")
    return sum(1 for r, g, b in im.get_flattened_data()
               if abs(r - CREME[0]) + abs(g - CREME[1]) + abs(b - CREME[2]) > 30)


def prepare(bloc: str) -> pathlib.Path:
    """Copie de rendu : GSAP inliné, runtime et shaders neutralisés."""
    src = ROOT / bloc / "index.html"
    h = src.read_text(encoding="utf-8")
    gsap = (TMP / "gsap.min.js")
    if not gsap.exists():
        TMP.mkdir(parents=True, exist_ok=True)
        subprocess.run(["curl", "-sS", "-m", "60", "-o", str(gsap),
                        "https://cdn.jsdelivr.net/npm/gsap@3.14.2/dist/gsap.min.js"], check=True)
    h = h.replace('<script src="https://cdn.jsdelivr.net/npm/gsap@3.14.2/dist/gsap.min.js"></script>',
                  "<script>" + gsap.read_text(encoding="utf-8") + "</script>")
    h = h.replace('<script src="https://cdn.jsdelivr.net/npm/@hyperframes/core/dist/'
                  'hyperframe.runtime.iife.js"></script>', "")
    h = h.replace('<script src="https://cdn.jsdelivr.net/npm/@hyperframes/shader-transitions/'
                  'dist/index.global.js"></script>',
                  "<script>window.HyperShader={init:function(){}};</script>")
    if 'id="s3"' in h:   # uniquement les blocs qui ont réellement une paire d'ancres
        h = h.replace('window.__timelines["main"] = tl;',
                      f'tl.to("#s2",{{opacity:0,duration:{FONDU},ease:"power1.inOut"}},{XF_TIME});\n'
                      f'      tl.to("#s3",{{opacity:1,duration:{FONDU},ease:"power1.inOut"}},{XF_TIME});\n'
                      '      window.__timelines["main"] = tl;')
    dest = ROOT / bloc / "_render.html"
    dest.write_text(h, encoding="utf-8")
    return dest


def capture(bloc: str, page: pathlib.Path) -> pathlib.Path:
    from playwright.sync_api import sync_playwright
    vd = TMP / f"vid-{bloc}"
    if vd.exists():
        shutil.rmtree(vd)
    vd.mkdir(parents=True)
    duree = DUREES[bloc]
    with sync_playwright() as p:
        b = p.chromium.launch(executable_path=CHROME,
                              args=["--no-sandbox", "--disable-dev-shm-usage", "--no-proxy-server",
                                    "--hide-scrollbars", "--force-device-scale-factor=1"])
        ctx = b.new_context(viewport={"width": 1920, "height": 1080},
                            record_video_dir=str(vd),
                            record_video_size={"width": 1920, "height": 1080})
        pg = ctx.new_page()
        pg.goto("file://" + str(page), wait_until="commit", timeout=30000)
        pg.wait_for_timeout(5000)
        pg.evaluate("() => { window.__timelines.main.play(0); }")
        pg.wait_for_timeout(int(duree * 1000) + 1500)
        ctx.close()
        b.close()
    return next(vd.glob("*.webm"))


def depart(webm: pathlib.Path) -> float:
    """Premier instant où la page n'est plus vide = début réel de la lecture."""
    d = TMP / "probe"
    if d.exists():
        shutil.rmtree(d)
    d.mkdir(parents=True)
    subprocess.run([FF, "-v", "error", "-ss", "3", "-t", "6", "-i", str(webm),
                    "-vf", "fps=10,scale=480:270", "-y", str(d / "p_%04d.png")], check=True)
    for f in sorted(d.glob("p_*.png")):
        if encre(f) > 300:
            return round(3.0 + (int(f.stem[2:]) - 1) / 10.0 - 0.04, 2)
    sys.exit("impossible de détecter le début de la lecture")


def encode(bloc: str, webm: pathlib.Path, offset: float) -> pathlib.Path:
    out = ROOT / bloc / "out"
    out.mkdir(exist_ok=True)
    suffixe = "-seq1-4" if bloc in ("boulangerie", "restauration") else ""
    dst = out / f"foodeatup-chaines-{bloc}{suffixe}-muet-v1.mp4"
    subprocess.run([FF, "-v", "error", "-ss", str(offset), "-i", str(webm),
                    "-t", str(DUREES[bloc]), "-r", "25", "-fps_mode", "cfr",
                    "-avoid_negative_ts", "make_zero",
                    "-c:v", "libx264", "-preset", "slow", "-crf", "20",
                    "-pix_fmt", "yuv420p", "-movflags", "+faststart", "-an",
                    "-y", str(dst)], check=True)
    return dst


def vides(mp4: pathlib.Path) -> list:
    """Balayage complet à 4 img/s : aucune image ne doit être vide."""
    d = TMP / "scan"
    if d.exists():
        shutil.rmtree(d)
    d.mkdir(parents=True)
    subprocess.run([FF, "-v", "error", "-i", str(mp4), "-vf", "fps=4,scale=480:270",
                    "-y", str(d / "f_%05d.png")], check=True)
    return [round((int(f.stem[2:]) - 1) / 4, 2)
            for f in sorted(d.glob("f_*.png")) if encre(f) < 300]


if __name__ == "__main__":
    bloc = sys.argv[1]
    page = prepare(bloc)
    webm = capture(bloc, page)
    off = depart(webm)
    mp4 = encode(bloc, webm, off)
    page.unlink(missing_ok=True)
    v = vides(mp4)
    dur = re.search(r"Duration: (\S+),", subprocess.run(
        [FF, "-hide_banner", "-i", str(mp4)], capture_output=True, text=True).stderr).group(1)
    print(f"{bloc}: départ détecté à {off}s · {mp4.name} · durée {dur}")
    print(f"  images vides : {v if v else 'AUCUNE'}")
