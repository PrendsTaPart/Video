#!/usr/bin/env python3
# FoodEatUp "Creer son compte + confirmation email" tutorial.
#
# Animation layer on top of the standard tutorial engine:
#   - intro/outro cards get a Ken Burns move (zoompan is safe HERE: still image
#     input only -- NEVER on the screen recording, that freezes the picture)
#   - every cut is an xfade transition (dissolve on continuous action,
#     slideleft where footage was skipped, so the jump reads as navigation)
#   - animated lower-third step banners that slide in from the left
#   - breathing highlight box around the button during each zoom-punch
#
# Speed = setpts. Zoom-on-click = fixed crop+scale punch on the sub-clip after
# the click (no per-frame crop eval -- unsupported in this ffmpeg build).
# Segment durations are sized to the VO line that narrates them.
import subprocess, os

ROOT = "/home/user/Video/videos/foodeatup-inscription-tuto"
SRC  = f"{ROOT}/assets/screen-inscription.mp4"
W, H, FPS = 1920, 828, 25
SEG = f"{ROOT}/work/seg"
FONT = "/usr/share/fonts/truetype/liberation/LiberationSans-Bold.ttf"
BLUE, ORANGE = "0x1B6DF3", "0xF7941D"
XF = 0.28                      # xfade duration on every boundary
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
    """Breathing box around the button, in the CROPPED+SCALED coordinate space.
    The crop is centred on the button, so after scaling back to WxH the button
    sits at the frame centre (up to the clamp at the frame edges)."""
    cw, ch, cx, cy = crop_box
    sx, sy = W / cw, H / ch
    bw, bh = btn_wh[0] * sx, btn_wh[1] * sy
    ox, oy = (btn[0] - cx) * sx, (btn[1] - cy) * sy      # button centre after scale
    p = 14                                               # padding around the button
    br = "6*sin(2*PI*t*2.2)"                             # breathing amplitude
    return (f"drawbox=x='{ox-bw/2-p}-{br}':y='{oy-bh/2-p}-{br}'"
            f":w='{bw+2*p}+2*({br})':h='{bh+2*p}+2*({br})'"
            f":color={ORANGE}@0.95:t=5")

def banner(text, seg_dur):
    """Lower-third that slides in from the left and slides back out."""
    if not text: return None
    tin, sl = 0.15, 0.32
    tout = max(tin + sl + 0.3, seg_dur - 0.55)
    a = f"min(1\\,max(0\\,(t-{tin})/{sl}))"          # 0->1 slide in
    b = f"min(1\\,max(0\\,(t-{tout})/{sl}))"         # 0->1 slide out
    x = f"-640+700*({a})-700*({b})"                  # -640 -> 60 -> -640
    y = H - 108
    return (f"drawbox=x='{x}':y={y}:w=10:h=62:color={ORANGE}@0.98:t=fill,"
            f"drawbox=x='({x})+10':y={y}:w=560:h=62:color={BLUE}@0.90:t=fill,"
            f"drawtext=fontfile={FONT}:text='{text}':fontsize=31:fontcolor=white"
            f":x='({x})+34':y={y+16}")

# (name, src_start, src_end, target_out_duration, click_time_or_None, button, btn_size, caption)
BTN_INSCRIRE = (1422, 644); SZ_INSCRIRE = (750, 74)
BTN_VERIFIER = (1149, 398); SZ_VERIFIER = (322, 54)
segs = [
    ("A", 0.50,  6.00, 4.90, None, None,         None,        "1 · Vos informations"),
    ("B", 6.00,  9.60, 3.20, None, None,         None,        "2 · Votre mot de passe"),
    ("C", 9.60, 10.90, 1.70, 9.60, BTN_INSCRIRE, SZ_INSCRIRE, None),
    ("D",10.90, 13.80, 3.50, None, None,         None,        "3 · Email de vérification"),
    ("E",14.00, 17.80, 3.50, None, None,         None,        "4 · Votre boîte mail"),
    # The page navigates away at 27.70 -- the punch has to stay strictly before
    # it, otherwise the highlight sits on an empty loading screen.
    ("F",25.50, 27.10, 2.20, None, None,         None,        "5 · Activation du compte"),
    ("G",27.10, 27.68, 1.80,27.10, BTN_VERIFIER, SZ_VERIFIER, None),
    ("H",39.30, 44.25, 8.00, None, None,         None,        "Votre espace est prêt"),
]
INTRO_D, OUTRO_D = 3.90, 6.40

def encode_seg(name, s, e, target, btn, btn_sz, caption):
    """One screen segment, sped to exactly `target` seconds, with its animations."""
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

def card(img, out, secs, zoom_in=True):
    """Still card: blurred cover background + sharp card on top, then a slow
    Ken Burns move. zoompan is fine here -- the input is a single still."""
    z0, z1 = (1.0, 1.09) if zoom_in else (1.09, 1.0)
    frames = int(secs * FPS)
    zexpr = f"{z0}+({z1}-{z0})*on/{frames}"
    vf = (f"[0:v]scale={W}:{H}:force_original_aspect_ratio=increase,crop={W}:{H},"
          f"boxblur=20:2,eq=brightness=-0.06[bg];"
          f"[0:v]scale={W}:{H}:force_original_aspect_ratio=decrease[fg];"
          f"[bg][fg]overlay=(W-w)/2:(H-h)/2,scale={W*2}:{H*2},"
          f"zoompan=z='{zexpr}':x='iw/2-(iw/zoom/2)':y='ih/2-(ih/zoom/2)'"
          f":d=1:s={W}x{H}:fps={FPS},"
          f"fade=t=in:st=0:d=0.45,fade=t=out:st={secs-0.45:.3f}:d=0.45,"
          f"format=yuv420p")
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

    # xfade chain. Boundary k dissolves segment k into k+1, so each segment
    # after the first starts XF earlier than a plain concat would put it.
    trans = ["fade","fade","fade","slideleft","fade","slideleft","fade","slideleft","fade"]
    durs = [dur(p) for p in parts]
    starts, acc = [], 0.0
    for i, d in enumerate(durs):
        starts.append(acc); acc += d - (XF if i < len(durs) - 1 else 0)
    total = acc

    inputs, fc, cur = [], [], "[0:v]"
    for i, p in enumerate(parts): inputs += ["-i", p]
    for k in range(len(parts) - 1):
        off = starts[k + 1]
        lbl = f"[x{k}]"
        fc.append(f"{cur}[{k+1}:v]xfade=transition={trans[k]}:duration={XF}"
                  f":offset={off:.4f}{lbl}")
        cur = lbl
    # xfade negotiates yuv444p with its inputs and libx264 will happily keep it,
    # producing a "High 4:4:4 Predictive" stream that browsers, QuickTime and
    # most consumer players refuse. Force 4:2:0 back on at the end of the chain.
    fc.append(f"{cur}format=yuv420p[vout]")
    silent = f"{ROOT}/work/video_silent.mp4"
    run(["ffmpeg","-y","-v","error"] + inputs +
        ["-filter_complex", ";".join(fc), "-map", "[vout]",
         "-r",str(FPS),"-c:v","libx264","-profile:v","high","-pix_fmt","yuv420p",
         "-preset","medium","-crf","18", silent])
    return silent, starts, total

silent, starts, total = build_silent(OUTRO_D)
print(f"SILENT TOTAL: {dur(silent):.2f}s")
S = {name: starts[i + 1] for i, (name, *_rest) in enumerate(segs)}   # segment -> timeline start
OUTRO_START = starts[-1]

# VO: anchors, then a sequential push so two lines can never overlap.
GAP = 0.22
anchor = {
    "N0": 0.30,
    "N1": S["A"] + 0.25,
    "N2": S["B"] + 0.20,
    "N3": S["D"] + 0.20,
    "N4": S["E"] + 0.20,
    "N5": S["F"] + 0.20,
    "N6": S["H"] + 0.30,
    "N7": S["H"] + 4.60,
    "N8": OUTRO_START + 0.35,
}
keys = [f"N{i}" for i in range(9)]
off, prev_end = {}, -GAP
for k in keys:
    o = max(anchor[k], prev_end + GAP); off[k] = o
    prev_end = o + dur(f"{ROOT}/vo/{k}.mp3")
print("offsets:", {k: round(v, 2) for k, v in off.items()}, "voice_end:", round(prev_end, 2))

# Outro must outlast the voice, otherwise the last line is cut off.
needed = prev_end - OUTRO_START + 0.80
if needed > OUTRO_D:
    print(f"extending outro {OUTRO_D:.2f} -> {needed:.2f}")
    silent, starts, total = build_silent(needed)
    print(f"SILENT TOTAL (extended): {dur(silent):.2f}s")

total = dur(silent)
inputs, filters, labels = [], [], []
for i, k in enumerate(keys):
    inputs += ["-i", f"{ROOT}/vo/{k}.mp3"]; ms = int(off[k] * 1000)
    # loudnorm EACH line on its own vocal content, before padding. On the padded
    # composite the long silences drag the integrated loudness down and the
    # filter over-boosts the speech.
    filters.append(f"[{i+1}:a]loudnorm=I=-16:TP=-1.5:LRA=11,adelay={ms}|{ms},apad[a{i}]")
    labels.append(f"[a{i}]")
filters.append("".join(labels) + f"amix=inputs={len(keys)}:normalize=0:duration=first[mix]")
# level=disabled -- alimiter's auto level is ON by default and renormalises back
# to 0dB, silently cancelling the ceiling.
# loudnorm upsamples to 192kHz internally; left alone the AAC stream ends up at
# 96kHz, which several players will not decode. Resample to 48kHz before encoding.
filters.append(f"[mix]atrim=0:{total:.3f},alimiter=limit=0.6:level=disabled,"
               f"aresample=48000,aformat=sample_fmts=fltp:channel_layouts=stereo,"
               f"asetpts=N/SR/TB[voa]")
FINAL = f"{ROOT}/out/foodeatup-inscription-tuto-v1.mp4"
run(["ffmpeg","-y","-v","error","-i",silent] + inputs +
    # -t rather than -shortest: the padded audio mix resolves slightly short and
    # would otherwise clip the outro's fade-to-black off the end of the video.
    # +faststart moves the moov atom in front of mdat -- without it a web player
    # has to fetch the whole file before it can start, which reads as "broken".
    ["-filter_complex",";".join(filters),"-map","0:v","-map","[voa]",
     "-c:v","copy","-c:a","aac","-b:a","192k","-ar","48000","-ac","2",
     "-movflags","+faststart","-t",f"{total:.3f}",FINAL])
print(f"DONE: {FINAL}  {dur(FINAL):.2f}s")
