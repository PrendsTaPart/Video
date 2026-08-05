#!/usr/bin/env python3
# FoodEatUp "Lancer un jeu concours fidélité" tutorial (module marketing-fidelite).
# Same engine as the rest of the series: no avatar clip, full ElevenLabs VO,
# speed = setpts (never zoompan on real footage), xfade on every cut, forced
# back to yuv420p at the end of the chain. 48kHz stereo AAC, +faststart.
#
# No "Utilisez cette fonctionnalité avec Claude" sequence on this one: the
# FoodEatUp MCP only exposes list_wheel_games / get_wheel_stats (read-only),
# no create/upsert tool for wheel games -- per the workflow rule, no prompt
# is invented when no MCP tool matches.
import subprocess, os

ROOT = "/home/user/Video/videos/foodeatup-jeu-concours-tuto"
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
    cw, ch, cx, cy = crop_box
    sx, sy = W / cw, H / ch
    bw, bh = btn_wh[0] * sx, btn_wh[1] * sy
    ox, oy = (btn[0] - cx) * sx, (btn[1] - cy) * sy
    p = 14
    # static geometry: ffmpeg 6.1.1's drawbox does not evaluate t in x/y/w/h,
    # so an animated "pulse" here would just freeze at its t=0 value anyway
    # (see FOODEATUP-TUTORIELS-WORKFLOW.md, pieges deja rencontres).
    return (f"drawbox=x='{ox-bw/2-p}':y='{oy-bh/2-p}'"
            f":w='{bw+2*p}':h='{bh+2*p}'"
            f":color={ORANGE}@0.95:t=5")

# Step banner: two drawtext layers (plate = drawtext's own box=1), NOT
# drawbox+drawtext. ffmpeg 6.1.1's drawbox never evaluates a t-dependent x --
# it draws once at t=0 and stays there (or off-screen), a bug hit repeatedly
# across this series (see FOODEATUP-TUTORIELS-WORKFLOW.md). drawtext does
# evaluate t per frame, so both the orange filet and the blue plate are drawn
# as drawtext boxes here, sharing the same sliding x expression as the label.
BANNER_Y = H - 108

def banner(text, seg_dur):
    if not text: return None
    tin, sl = 0.15, 0.32
    tout = max(tin + sl + 0.3, seg_dur - 0.55)
    a = f"min(1\\,max(0\\,(t-{tin})/{sl}))"
    b = f"min(1\\,max(0\\,(t-{tout})/{sl}))"
    x = f"-640+700*({a})-700*({b})"
    label = f" {text} "
    return (f"drawtext=fontfile={FONT}:text='{label}':fontsize=31:fontcolor=white"
            f":box=1:boxcolor={ORANGE}@0.98:boxborderw=16:x='({x})-10':y={BANNER_Y},"
            f"drawtext=fontfile={FONT}:text='{label}':fontsize=31:fontcolor=white"
            f":box=1:boxcolor={BLUE}@0.92:boxborderw=16:x='({x})':y={BANNER_Y}")

# Coordinates measured by colour-thresholding the actual frames (PIL bbox
# scan on the FoodEatUp blue, not eyeballed), see analysis notes.
BTN_TAB_ROUE = (696, 324);  SZ_TAB_ROUE = (232, 48)   # onglet "Roue cadeaux"
BTN_CREATE   = (949, 717);  SZ_CREATE   = (330, 71)   # "+ Créer une roue cadeaux"
BTN_SAVE     = (258, 672);  SZ_SAVE     = (236, 61)   # "Enregistrer la roue"

# (name, src_start, src_end, target_out_duration, button, btn_size, caption)
# Targets sized on the measured VO durations (see vo/*.mp3), not the other
# way round -- avoids the narration/segment drift bug documented repeatedly
# in FOODEATUP-TUTORIELS-WORKFLOW.md.
segs = [
    ("A", 0.30,  3.55,  3.00, None,        None,       "1 . Fidelite et jeux"),
    ("B", 3.55,  3.85,  1.30, BTN_TAB_ROUE, SZ_TAB_ROUE, None),
    ("C", 3.90,  3.95,  3.00, None,        None,       "2 . Roue cadeaux"),
    ("D", 3.95,  4.15,  1.80, BTN_CREATE,  SZ_CREATE,  None),
    ("E", 6.50,  11.00, 5.30, None,        None,       "3 . Titre et frequence"),
    ("F", 12.00, 18.00, 5.80, None,        None,       "4 . Vos lots"),
    ("G", 36.00, 41.60, 6.40, None,        None,       "5 . Capturez des leads"),
    ("H", 44.20, 44.55, 1.00, BTN_SAVE,    SZ_SAVE,    None),
    ("I", 46.00, 49.50, 5.20, None,        None,       "Roue creee !"),
    ("J", 50.00, 52.50, 5.20, None,        None,       None),
]
INTRO_D, OUTRO_D = 4.30, 6.50

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
    for name, s, e, target, btn, sz, cap in segs:
        parts.append(encode_seg(name, s, e, target, btn, sz, cap))
    parts.append(f"{SEG}/outro.mp4")

    trans = ["fade",       # intro -> A
             "fade",       # A -> B (continuous: click on the visible tab bar)
             "slideleft",  # B -> C (cut: onglet Roue cadeaux, etat vide)
             "fade",       # C -> D (continuous: click Creer une roue cadeaux)
             "slideleft",  # D -> E (cut into the opened form)
             "slideleft",  # E -> F (cut, titre/frequence -> segments)
             "slideleft",  # F -> G (cut, segments -> action d'entree)
             "fade",       # G -> H (continuous: click Enregistrer)
             "fade",       # H -> I (submit -> succes/liste)
             "slideleft",  # I -> J (cut: carte finale, lien/QR)
             "fade"]       # J -> outro
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
    "N0": 0.30,                 # intro hook
    "N1": S["B"] + 0.05,        # onglet Roue cadeaux -> Creer une roue cadeaux
    "N2": S["E"] + 0.20,        # titre + frequence
    "N3": S["F"] + 0.20,        # vos lots (bons, points, retentez)
    "N4": S["G"] + 0.20,        # action d'entree (email)
    "N5": S["H"] + 0.05,        # clic Enregistrer la roue
    "N6": S["J"] + 0.20,        # partager le lien / QR
    "N7": OUTRO_START + 0.35,   # CTA
}
keys = [f"N{i}" for i in range(8)]
off, prev_end = {}, -GAP
for k in keys:
    o = max(anchor[k], prev_end + GAP); off[k] = o
    prev_end = o + dur(f"{ROOT}/vo/{k}.mp3")
print("offsets:", {k: round(v, 2) for k, v in off.items()}, "voice_end:", round(prev_end, 2))
drift = {k: round(off[k] - anchor[k], 2) for k in keys if off[k] - anchor[k] > 0.05}
print("drift vs anchors:", drift if drift else "none -- all lines on their anchors")
print("stage starts:", {k: round(v, 2) for k, v in S.items()})

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
FINAL = f"{ROOT}/out/foodeatup-jeu-concours-tuto-v1.mp4"
run(["ffmpeg","-y","-v","error","-i",silent] + inputs +
    ["-filter_complex",";".join(filters),"-map","0:v","-map","[voa]",
     "-c:v","copy","-c:a","aac","-b:a","192k","-ar","48000","-ac","2",
     "-movflags","+faststart","-t",f"{total:.3f}",FINAL])
print(f"DONE: {FINAL}  {dur(FINAL):.2f}s")
