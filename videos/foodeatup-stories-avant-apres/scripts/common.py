#!/usr/bin/env python3
# Shared helpers for the FoodEatUp avant/après stories pipeline.
# No video generation happens here — only assembly of clips that already
# exist in clips/ (downloaded from the Higgsfield library via RapidoCMS).
import json, os, subprocess

ROOT = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
CLIPS = f"{ROOT}/clips"
OUT = f"{ROOT}/out"
WORK = f"{ROOT}/work"
FONT_BOLD = f"{ROOT}/assets/fonts/baloo-2-latin-700-normal.ttf"

with open(f"{ROOT}/manifest.json") as f:
    MANIFEST = json.load(f)

W = MANIFEST["output"]["width"]
H = MANIFEST["output"]["height"]
FPS = MANIFEST["output"]["fps"]
HALF_W = MANIFEST["half"]["width"]
HALF_H = MANIFEST["half"]["height"]
SEAM_PX = MANIFEST["seam_px"]
SEAM_COLOR = MANIFEST["seam_color"]
PALETTE = MANIFEST["palette"]
ENDCARD_SECONDS = MANIFEST["endcard"]["seconds"]
ENDCARD_SOURCE = MANIFEST["endcard"]["source"]


def run(cmd):
    r = subprocess.run(cmd, capture_output=True, text=True)
    if r.returncode != 0:
        print("ERR:", " ".join(cmd)[:400])
        print(r.stderr[-3000:])
        raise SystemExit(1)


def probe(path):
    r = subprocess.run(
        ["ffprobe", "-v", "error", "-select_streams", "v:0",
         "-show_entries", "stream=width,height,r_frame_rate,duration",
         "-of", "json", path],
        capture_output=True, text=True)
    return json.loads(r.stdout)["streams"][0]


def duration(path):
    r = subprocess.run(
        ["ffprobe", "-v", "error", "-show_entries", "format=duration",
         "-of", "csv=p=0", path],
        capture_output=True, text=True)
    return float(r.stdout.strip())


def has_audio(path):
    r = subprocess.run(
        ["ffprobe", "-v", "error", "-select_streams", "a",
         "-show_entries", "stream=index", "-of", "csv=p=0", path],
        capture_output=True, text=True)
    return bool(r.stdout.strip())


def clip_path(name):
    for ext in (".mp4", ".mov"):
        p = f"{CLIPS}/{name}{ext}"
        if os.path.exists(p):
            return p
    return None


def check_square(name, path, tolerance=0.05):
    info = probe(path)
    w, h = int(info["width"]), int(info["height"])
    ratio = w / h
    if abs(ratio - 1.0) > tolerance:
        print(f"WARNING: {name} n'est pas carré ({w}x{h}, ratio={ratio:.3f}). "
              f"Recadrage minimal impossible — vérifier la source avant de continuer.")
    return w, h


def banner_filter(text, y, box_color):
    text = text.replace("'", "\\'").replace(":", "\\:")
    return (
        f"drawtext=fontfile={FONT_BOLD}:text='{text}':fontsize=46:fontcolor=white"
        f":box=1:boxcolor={box_color}@0.7:boxborderw=24"
        f":x=(w-text_w)/2:y={y}"
    )


os.makedirs(WORK, exist_ok=True)
os.makedirs(OUT, exist_ok=True)
