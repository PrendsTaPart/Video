#!/usr/bin/env python3
# FoodEatUp "Monter sa boutique" tutorial.
#
# New in this project: a HeyGen avatar clip (assets/avatar.mp4) with its OWN
# baked-in narration -- it is the spoken hook, replacing the usual ElevenLabs
# "N0" intro line. Its native audio is extracted once (vo/N0.mp3) and mixed
# into the VO track like any other line, anchored to its own segment's start.
# No ElevenLabs is generated for that beat, so the two voices never overlap.
#
# Same engine as foodeatup-inscription-tuto otherwise: setpts for speed (never
# zoompan on real footage -- freezes the image, including on the avatar clip),
# fixed crop+scale zoom-punch on clicks, xfade on every cut forced back to
# yuv420p (xfade negotiates 4:4:4 with its inputs and libx264 will keep an
# unplayable profile if you let it), 48kHz stereo AAC, +faststart.
import subprocess, os

ROOT = "/home/user/Video/videos/foodeatup-boutique-tuto"
SRC  = f"{ROOT}/assets/screen.mp4"
AVATAR = f"{ROOT}/assets/avatar.mp4"
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
    br = "6*sin(2*PI*t*2.2)"
    return (f"drawbox=x='{ox-bw/2-p}-{br}':y='{oy-bh/2-p}-{br}'"
            f":w='{bw+2*p}+2*({br})':h='{bh+2*p}+2*({br})'"
            f":color={ORANGE}@0.95:t=5")

def banner(text, seg_dur):
    if not text: return None
    tin, sl = 0.15, 0.32
    tout = max(tin + sl + 0.3, seg_dur - 0.55)
    a = f"min(1\\,max(0\\,(t-{tin})/{sl}))"
    b = f"min(1\\,max(0\\,(t-{tout})/{sl}))"
    x = f"-640+700*({a})-700*({b})"
    y = H - 108
    return (f"drawbox=x='{x}':y={y}:w=10:h=62:color={ORANGE}@0.98:t=fill,"
            f"drawbox=x='({x})+10':y={y}:w=560:h=62:color={BLUE}@0.90:t=fill,"
            f"drawtext=fontfile={FONT}:text='{text}':fontsize=31:fontcolor=white"
            f":x='({x})+34':y={y+16}")

# (name, src_start, src_end, target_out_duration, click_time_or_None, button, btn_size, caption)
BTN_CHOISIR = (967, 353);  SZ_CHOISIR = (222, 46)
BTN_AJOUTER = (1035, 735); SZ_AJOUTER = (124, 46)
segs = [
    ("A1", 0.30,  6.00, 3.20, None, None,        None,       "1 · Ajouter une boutique"),
    ("A2", 6.00,  6.55, 0.90, 6.00, BTN_CHOISIR, SZ_CHOISIR, None),
    ("A3", 7.00,  9.00, 1.60, None, None,        None,       None),
    ("B",  9.00, 24.00, 5.00, None, None,        None,       "2 · Nom, email, domaine"),
    ("C", 24.00, 33.50, 4.00, None, None,        None,       "3 · Pays et ville"),
    ("D", 33.50, 58.00, 5.50, None, None,        None,       "4 · Adresse et SIRET"),
    ("E", 58.00, 58.60, 1.00, 58.00, BTN_AJOUTER, SZ_AJOUTER, None),
    ("F", 59.00, 63.48, 3.00, None, None,        None,       "Votre boutique est prête"),
]
INTRO_D, OUTRO_D = 1.70, 6.10

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

def encode_avatar():
    """Talking-head clip, own aspect ratio (1920x1080) fit into the WxH canvas
    with a blurred cover of itself behind it -- NOT zoompan (that only ever
    runs on stills in this pipeline; on real footage it freezes the image).
    Runs at native speed/duration, no setpts stretch: it is a person talking."""
    out = f"{SEG}/avatar.mp4"
    vf = (f"[0:v]split=2[bg][fg];"
          f"[bg]scale={W}:{H}:force_original_aspect_ratio=increase,crop={W}:{H},"
          f"boxblur=20:2,eq=brightness=-0.08[bgs];"
          f"[fg]scale={W}:{H}:force_original_aspect_ratio=decrease[fgs];"
          f"[bgs][fgs]overlay=(W-w)/2:(H-h)/2,fps={FPS},format=yuv420p[v]")
    run(["ffmpeg","-y","-v","error","-i",AVATAR,"-filter_complex",vf,"-map","[v]",
         "-an","-r",str(FPS),"-c:v","libx264","-preset","medium","-crf","18",out])
    return out

def card(img, out, secs, zoom_in=True):
    z0, z1 = (1.0, 1.09) if zoom_in else (1.09, 1.0)
    frames = int(secs * FPS)
    zexpr = f"{z0}+({z1}-{z0})*on/{frames}"
    vf = (f"[0:v]scale={W}:{H}:force_original_aspect_ratio=increase,crop={W}:{H},"
          f"boxblur=20:2,eq=brightness=-0.06[bg];"
          f"[0:v]scale={W}:{H}:force_original_aspect_ratio=decrease[fg];"
          f"[bg][fg]overlay=(W-w)/2:(H-h)/2,scale={W*2}:{H*2},"
          f"zoompan=z='{zexpr}':x='iw/2-(iw/zoom/2)':y='ih/2-(ih/zoom/2)'"
          f":d=1:s={W}x{H}:fps={FPS},"
          f"fade=t=in:st=0:d=0.4,fade=t=out:st={secs-0.4:.3f}:d=0.4,"
          f"format=yuv420p")
    run(["ffmpeg","-y","-v","error","-loop","1","-t",str(secs),"-i",img,
         "-filter_complex",vf,"-r",str(FPS),
         "-c:v","libx264","-preset","medium","-crf","18",out])

def build_silent(outro_d):
    card(f"{ROOT}/assets/intro.jpg", f"{SEG}/intro.mp4", INTRO_D, zoom_in=True)
    card(f"{ROOT}/assets/outro.jpg", f"{SEG}/outro.mp4", outro_d, zoom_in=False)
    avatar_seg = encode_avatar()
    parts = [f"{SEG}/intro.mp4", avatar_seg]
    for name, s, e, target, ck, btn, sz, cap in segs:
        parts.append(encode_seg(name, s, e, target, btn, sz, cap))
    parts.append(f"{SEG}/outro.mp4")

    # D->E (index 7) is continuous (typing straight into the click), not a skip.
    trans = ["fade","fade","fade","fade","fade","fade","fade","fade","slideleft","fade"]
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
labels_order = ["intro","avatar"] + [s[0] for s in segs] + ["outro"]
S = dict(zip(labels_order, starts))
AVATAR_START = S["avatar"]
OUTRO_START = S["outro"]

GAP = 0.22
anchor = {
    "N0": AVATAR_START,                  # native audio, hard-anchored to its own segment
    "N1": S["A1"] + 0.20,
    "N2": S["B"]  + 0.20,
    "N3": S["C"]  + 0.20,
    "N4": S["D"]  + 0.20,
    "N5": S["F"]  + 0.20,
    "N6": OUTRO_START + 0.35,
}
keys = [f"N{i}" for i in range(7)]
off, prev_end = {}, -GAP
for k in keys:
    o = max(anchor[k], prev_end + GAP); off[k] = o
    prev_end = o + dur(f"{ROOT}/vo/{k}.mp3")
print("offsets:", {k: round(v, 2) for k, v in off.items()}, "voice_end:", round(prev_end, 2))

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
FINAL = f"{ROOT}/out/foodeatup-boutique-tuto-v1.mp4"
run(["ffmpeg","-y","-v","error","-i",silent] + inputs +
    ["-filter_complex",";".join(filters),"-map","0:v","-map","[voa]",
     "-c:v","copy","-c:a","aac","-b:a","192k","-ar","48000","-ac","2",
     "-movflags","+faststart","-t",f"{total:.3f}",FINAL])
print(f"DONE: {FINAL}  {dur(FINAL):.2f}s")
