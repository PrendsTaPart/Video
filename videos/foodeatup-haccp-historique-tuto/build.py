#!/usr/bin/env python3
# FoodEatUp "Retrouver mes contrôles historique" (HACCP Checklist Hygiène) tutorial.
# No avatar clip: full ElevenLabs VO throughout (native audio in the rush is
# silent, -91dB). Speed = setpts (never zoompan on real footage). xfade on
# every cut, forced back to yuv420p at the end of the chain. 48kHz stereo
# AAC, +faststart.
#
# Rush: Checklist hygiène page -> Historique nav -> Checklist Hygiène tile ->
# Historique des validations list -> open a past validation (detail) -> back
# to list -> Exporter l'historique -> pick a report format -> Générer le PDF
# -> the PDF report opens. The rush's own middle section (11.5s-32s: toggling
# compliance to "Non conforme", a validation error banner) is intentionally
# NOT included -- it's not a feature to demo, just an incidental error state
# in the recording. No MCP tool covers "list validation history" or "export
# PDF" (checked: list_hygiene_checklists only lists checklist templates), so
# there is no "Use it with Claude" sequence in this video, unlike most others
# in the series.
import subprocess, os, sys

ROOT = "/home/user/Video/videos/foodeatup-haccp-historique-tuto"
SRC  = f"{ROOT}/assets/screen.mp4"
W, H, FPS = 1920, 828, 25
SEG = f"{ROOT}/work/seg"
FONT = "/usr/share/fonts/truetype/liberation/LiberationSans-Bold.ttf"
BLUE, ORANGE = "0x1B6DF3", "0xF7941D"
XF = 0.28
os.makedirs(SEG, exist_ok=True)

def run(cmd):
    r = subprocess.run(cmd, capture_output=True, text=True)
    if r.returncode != 0:
        print("ERR:", " ".join(cmd)[:300]); print(r.stderr[-2000:]); raise SystemExit(1)

def dur(path):
    r = subprocess.run(["ffprobe","-v","error","-show_entries","format=duration",
                        "-of","csv=p=0",path], capture_output=True, text=True)
    return float(r.stdout.strip())

def clamp(v, lo, hi): return max(lo, min(hi, v))

ZOOM = 1.20
def crop_for(btn):
    bx, by = btn
    cw, ch = int(W/ZOOM), int(H/ZOOM); cw -= cw % 2; ch -= ch % 2
    x = int(clamp(bx - cw/2, 0, W - cw)); y = int(clamp(by - ch/2, 0, H - ch))
    return f"crop={cw}:{ch}:{x}:{y},scale={W}:{H}:flags=bicubic", (cw, ch, x, y)

def punch_highlight(btn, btn_wh, crop_box):
    # NOTE: this ffmpeg build evaluates drawbox x/y/w/h expressions ONCE at
    # t=0 (no `eval` option on this build's drawbox). Static highlight box,
    # not an animated pulse -- see foodeatup-predibot-suggestions-tuto for
    # the discovery/writeup of this bug.
    cw, ch, cx, cy = crop_box
    sx, sy = W / cw, H / ch
    bw, bh = btn_wh[0] * sx, btn_wh[1] * sy
    ox, oy = (btn[0] - cx) * sx, (btn[1] - cy) * sy
    p = 14
    return (f"drawbox=x={ox-bw/2-p:.1f}:y={oy-bh/2-p:.1f}"
            f":w={bw+2*p:.1f}:h={bh+2*p:.1f}"
            f":color={ORANGE}@0.95:t=5")

def banner(text, seg_dur):
    # Static position for the same reason as punch_highlight above.
    if not text: return None
    x, y = 40, H - 108
    return (f"drawbox=x={x}:y={y}:w=10:h=62:color={ORANGE}@0.98:t=fill,"
            f"drawbox=x={x+10}:y={y}:w=560:h=62:color={BLUE}@0.90:t=fill,"
            f"drawtext=fontfile={FONT}:text='{text}':fontsize=31:fontcolor=white"
            f":x={x+34}:y={y+16}")

# Coordinates measured on the actual frames (ffmpeg -ss t -frames:v 1).
BTN_TILE   = (750, 562);  SZ_TILE   = (370, 300)  # "Checklist Hygiène" tile
BTN_EXPORT = (1462, 300); SZ_EXPORT = (300, 55)   # "Exporter l'historique"
BTN_PDF    = (1023, 758); SZ_PDF    = (200, 55)   # "Générer le PDF"

# (name, src_start, src_end, target_out_duration, click_time_or_None, button, btn_size, caption)
segs = [
    ("A", 0.00,  2.00,  3.00, None, None,       None,      "1 - Vos checklists hygiene"),
    ("B", 3.00,  4.40,  3.40, None, None,       None,      "2 - Ouvrez l historique"),
    ("C", 4.40,  4.70,  0.70, 4.50, BTN_TILE,   SZ_TILE,   None),
    ("D", 5.00,  8.50,  4.60, None, None,       None,      "3 - Vos validations passees"),
    ("E", 9.00, 11.50,  6.00, None, None,       None,      "4 - Consultez le detail"),
    ("F", 32.50, 34.00, 2.20, None, None,       None,      "5 - Exportez l historique"),
    ("G", 34.00, 34.30, 0.70, 34.10, BTN_EXPORT, SZ_EXPORT, None),
    ("H", 34.30, 41.00, 7.00, None, None,       None,      "Choisissez le format du rapport"),
    ("I", 41.00, 41.30, 0.70, 41.10, BTN_PDF,    SZ_PDF,    None),
    ("J", 41.30, 44.50, 2.00, None, None,       None,      "Export en cours"),
    ("K", 45.00, 50.28, 4.50, None, None,       None,      "Votre PDF est pret"),
]
INTRO_D, OUTRO_D = 2.60, 6.20

def encode_seg(name, s, e, target, btn, btn_sz, caption):
    out = f"{SEG}/{name}.mp4"
    factor = (e - s) / target
    vf = f"setpts=(PTS-STARTPTS)/{factor:.6f}"
    if btn:
        crop_vf, box = crop_for(btn)
        vf += f",{crop_vf},{punch_highlight(btn, btn_sz, box)}"
    else:
        vf += f",scale={W}:{H}"
    b = banner(caption, target)
    if b: vf += f",{b}"
    vf += f",fps={FPS},format=yuv420p"
    run(["ffmpeg","-y","-v","error","-ss",str(s),"-to",str(e),"-i",SRC,"-an",
         "-vf",vf,"-r",str(FPS),"-c:v","libx264","-preset","medium","-crf","18",out])
    return out

def card(img, out, secs, zoom_in=True, fade=True):
    z0, z1 = (1.0, 1.09) if zoom_in else (1.09, 1.0)
    frames = int(secs * FPS)
    zexpr = f"{z0}+({z1}-{z0})*on/{frames}"
    vf = (f"[0:v]scale={W}:{H}:force_original_aspect_ratio=increase,crop={W}:{H},"
          f"boxblur=20:2,eq=brightness=-0.06[bg];"
          f"[0:v]scale={W}:{H}:force_original_aspect_ratio=decrease[fg];"
          f"[bg][fg]overlay=(W-w)/2:(H-h)/2,scale={W*2}:{H*2},"
          f"zoompan=z='{zexpr}':x='iw/2-(iw/zoom/2)':y='ih/2-(ih/zoom/2)'"
          f":d=1:s={W}x{H}:fps={FPS}")
    if fade:
        vf += f",fade=t=in:st=0:d=0.4,fade=t=out:st={secs-0.4:.3f}:d=0.4"
    vf += ",format=yuv420p"
    run(["ffmpeg","-y","-v","error","-loop","1","-t",str(secs),"-i",img,
         "-filter_complex",vf,"-r",str(FPS),
         "-c:v","libx264","-preset","medium","-crf","18",out])

def build_silent(outro_d):
    card(f"{ROOT}/assets/intro.jpg", f"{SEG}/intro.mp4", INTRO_D, zoom_in=True)
    card(f"{ROOT}/assets/outro.jpg", f"{SEG}/outro.mp4", outro_d, zoom_in=False)

    parts = [f"{SEG}/intro.mp4"]
    for name, s, e, target, ck, btn, sz, cap in segs:
        parts.append(encode_seg(name, s, e, target, btn, sz, cap))
    parts.append(f"{SEG}/outro.mp4")

    trans = ["fade",       # intro -> A
             "fade",       # A -> B (cut: nav to Historique)
             "fade",       # B -> C (continuous: click the tile)
             "slideleft",  # C -> D (cut: tile opens the list)
             "slideleft",  # D -> E (cut: entry opens the modal)
             "slideleft",  # E -> F (cut: close modal back to list)
             "fade",       # F -> G (continuous: click Exporter)
             "slideleft",  # G -> H (cut: export modal opens)
             "fade",       # H -> I (continuous: click Générer le PDF)
             "fade",       # I -> J (continuous: generating -> success)
             "slideleft",  # J -> K (cut: PDF opens)
             "fade"]       # K -> outro
    durs = [dur(p) for p in parts]
    starts, acc = [], 0.0
    for i, d in enumerate(durs):
        starts.append(acc); acc += d - (XF if i < len(durs) - 1 else 0)
    total = acc

    inputs, fc, cur = [], [], "[0:v]"
    for p in parts: inputs += ["-i", p]
    for k in range(len(parts) - 1):
        off = starts[k + 1]
        lbl = f"[x{k}]"
        fc.append(f"{cur}[{k+1}:v]xfade=transition={trans[k]}:duration={XF}"
                  f":offset={off:.4f}{lbl}")
        cur = lbl
    fc.append(f"{cur}format=yuv420p[vout]")
    silent = f"{ROOT}/work/video_silent.mp4"
    run(["ffmpeg","-y","-v","error"] + inputs +
        ["-filter_complex", ";".join(fc), "-map", "[vout]",
         "-r",str(FPS),"-c:v","libx264","-profile:v","high","-pix_fmt","yuv420p",
         "-preset","medium","-crf","18", silent])
    return silent, starts, total

silent, starts, total = build_silent(OUTRO_D)
print(f"SILENT TOTAL: {dur(silent):.2f}s")
labels_order = ["intro"] + [s[0] for s in segs] + ["outro"]
S = dict(zip(labels_order, starts))
OUTRO_START = S["outro"]

GAP = 0.22
anchor = {
    "N0": 0.30,                  # intro hook
    "N1": S["B"] + 0.10,         # "ouvrez historique puis checklist hygiene"
    "N2": S["D"] + 0.20,         # liste des validations passées
    "N3": S["E"] + 0.20,         # détail d'une validation
    "N4": S["F"] + 0.10,         # exporter l'historique
    "N5": S["H"] + 0.20,         # format + générer le PDF
    "N6": OUTRO_START + 0.35,    # CTA
}
keys = [f"N{i}" for i in range(7)]
off, prev_end = {}, -GAP
for k in keys:
    o = max(anchor[k], prev_end + GAP); off[k] = o
    prev_end = o + dur(f"{ROOT}/vo/{k}.mp3")
print("offsets:", {k: round(v, 2) for k, v in off.items()}, "voice_end:", round(prev_end, 2))
drift = {k: round(off[k] - anchor[k], 2) for k in keys if off[k] - anchor[k] > 0.05}
print("drift vs anchors:", drift if drift else "none -- all lines on their anchors")

needed = prev_end - OUTRO_START + 0.80
if needed > OUTRO_D:
    print(f"extending outro {OUTRO_D:.2f} -> {needed:.2f}")
    silent, starts, total = build_silent(needed)
    print(f"SILENT TOTAL (extended): {dur(silent):.2f}s")

total = dur(silent)
inputs, filters, labels = [], [], []
for i, k in enumerate(keys):
    inputs += ["-i", f"{ROOT}/vo/{k}.mp3"]; ms = int(off[k] * 1000)
    filters.append(f"[{i+1}:a]loudnorm=I=-16:TP=-1.5:LRA=11,adelay={ms}|{ms},apad[a{i}]")
    labels.append(f"[a{i}]")
filters.append("".join(labels) + f"amix=inputs={len(keys)}:normalize=0:duration=first[mix]")
filters.append(f"[mix]atrim=0:{total:.3f},alimiter=limit=0.6:level=disabled,"
               f"aresample=48000,aformat=sample_fmts=fltp:channel_layouts=stereo,"
               f"asetpts=N/SR/TB[voa]")
FINAL = f"{ROOT}/out/foodeatup-haccp-historique-tuto-v1.mp4"
run(["ffmpeg","-y","-v","error","-i",silent] + inputs +
    ["-filter_complex",";".join(filters),"-map","0:v","-map","[voa]",
     "-c:v","copy","-c:a","aac","-b:a","192k","-ar","48000","-ac","2",
     "-movflags","+faststart","-t",f"{total:.3f}",FINAL])
print(f"DONE: {FINAL}  {dur(FINAL):.2f}s")
