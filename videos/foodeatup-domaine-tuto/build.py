#!/usr/bin/env python3
# FoodEatUp "Connecter son Domaine" tutorial (module site-web-vitrine, 08/8).
# No avatar clip: full ElevenLabs VO throughout. Speed = setpts (never zoompan
# on real footage). xfade on every cut, forced back to yuv420p at the end of
# the chain. 48kHz stereo AAC, +faststart. Segment targets set close to each
# VO line's measured duration (see vo/*.mp3) before building, not after.
import subprocess, os, sys
sys.path.insert(0, "/home/user/Video/videos/_shared")
from claude_prompt_sequence import (
    render_claude_stage1_png, render_claude_stage2_png, render_claude_stage3_png,
)

ROOT = "/home/user/Video/videos/foodeatup-domaine-tuto"
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

# Coordinates measured on the 1920x828 source rush by frame extraction
# (1fps sweep + 4fps sweeps around each click, see SCRIPT.md).
BTN_CONNECTER = (1201, 489);  SZ_CONNECTER = (140, 46)   # "Connecter" (domain field)
BTN_COPIER    = (502, 607);   SZ_COPIER    = (108, 46)   # "Copier" (CNAME record)
BTN_VERIFIER  = (534, 710);   SZ_VERIFIER  = (222, 46)   # "Vérifier maintenant"

# (name, src_start, src_end, target_out_duration, click_time_or_None, button, btn_size, caption)
segs = [
    ("A", 0.00, 17.00, 9.30, None,  None,          None,         "1 · Saisissez votre domaine"),
    ("B", 17.35, 17.70, 0.90, 17.50, BTN_CONNECTER, SZ_CONNECTER, None),
    ("C", 19.50, 23.20, 7.20, None,  None,          None,         "2 · Copiez cet enregistrement CNAME"),
    ("D", 23.85, 24.15, 0.90, 24.00, BTN_COPIER,    SZ_COPIER,    None),
    ("E", 24.20, 27.15, 2.00, None,  None,          None,         None),
    ("F", 27.15, 27.50, 0.90, 27.30, BTN_VERIFIER,  SZ_VERIFIER,  "3 · Vérifiez la propagation DNS"),
    ("G", 27.50, 31.60, 8.60, None,  None,          None,         None),
]
INTRO_D, OUTRO_D = 5.00, 6.20

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

# ---------------------------------------------------------------------------
# "Use it with Claude" sequence -- 3-stage chatbot-style animation shared
# across the whole series (videos/_shared/claude_prompt_sequence.py). No MCP
# tool *connects* a domain, but get_domain_status (DNS/SSL check) matches
# exactly the "Vérifier maintenant" action shown in the rush.
# ---------------------------------------------------------------------------
CLAUDE_PROMPT = ("Vérifie le statut de mon nom de domaine pour mon établissement "
                  "FoodEatUp (ID [ID établissement]).")
CLAUDE_RESPONSE = "Je vérifie le statut DNS et SSL de votre domaine…"

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

# N5 (Vérifier maintenant + bénéfice DNS/SSL) is long (9.8s): give stage1 a
# bit more room than the shared default so N6 doesn't spill onto stage2.
CLAUDE_STAGE_D = [3.00, 2.30, 5.30]  # reveal, copied, chatbot mockup

def build_silent(outro_d):
    card(f"{ROOT}/assets/intro.jpg", f"{SEG}/intro.mp4", INTRO_D, zoom_in=True)
    card(f"{ROOT}/assets/outro.jpg", f"{SEG}/outro.mp4", outro_d, zoom_in=False)
    claude1_png, claude2_png, claude3_png = f"{SEG}/claude1.png", f"{SEG}/claude2.png", f"{SEG}/claude3.png"
    if not os.path.exists(claude1_png):
        render_claude_stage1_png(claude1_png, W, H, CLAUDE_PROMPT)
    if not os.path.exists(claude2_png):
        render_claude_stage2_png(claude2_png, W, H, CLAUDE_PROMPT)
    if not os.path.exists(claude3_png):
        render_claude_stage3_png(claude3_png, W, H, CLAUDE_PROMPT, response=CLAUDE_RESPONSE)
    for i, png in enumerate([claude1_png, claude2_png, claude3_png]):
        card(png, f"{SEG}/claude{i+1}.mp4", CLAUDE_STAGE_D[i], zoom_in=True, fade=False)
    parts = [f"{SEG}/intro.mp4"]
    for name, s, e, target, ck, btn, sz, cap in segs:
        parts.append(encode_seg(name, s, e, target, btn, sz, cap))
    parts.append(f"{SEG}/claude1.mp4")
    parts.append(f"{SEG}/claude2.mp4")
    parts.append(f"{SEG}/claude3.mp4")
    parts.append(f"{SEG}/outro.mp4")

    trans = ["fade"] * (len(parts) - 1)
    trans[-4] = "slideleft"  # last real seg -> claude1
    trans[-3] = "slideleft"  # claude1 -> claude2
    trans[-2] = "slideleft"  # claude2 -> claude3
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
labels_order = ["intro"] + [s[0] for s in segs] + ["claude1", "claude2", "claude3", "outro"]
S = dict(zip(labels_order, starts))
OUTRO_START = S["outro"]

GAP = 0.22
anchor = {
    "N0": 0.30,
    "N1": S["A"] + 0.20,
    "N2": S["B"] + 0.20,
    "N3": S["C"] + 0.20,
    "N4": S["D"] + 0.20,
    "N5": S["F"] + 0.20,
    "N6": S["claude1"] + 0.20,
    "N7": S["claude3"] + 0.20,
    "N8": OUTRO_START + 0.35,
}
keys = [f"N{i}" for i in range(9)]
off, prev_end = {}, -GAP
for k in keys:
    o = max(anchor[k], prev_end + GAP); off[k] = o
    prev_end = o + dur(f"{ROOT}/vo/{k}.mp3")
print("anchors:", {k: round(v, 2) for k, v in anchor.items()})
print("offsets:", {k: round(v, 2) for k, v in off.items()}, "voice_end:", round(prev_end, 2))
print("drift:", {k: round(off[k] - anchor[k], 2) for k in keys})

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
FINAL = f"{ROOT}/out/foodeatup-domaine-tuto-v1.mp4"
run(["ffmpeg","-y","-v","error","-i",silent] + inputs +
    ["-filter_complex",";".join(filters),"-map","0:v","-map","[voa]",
     "-c:v","copy","-c:a","aac","-b:a","192k","-ar","48000","-ac","2",
     "-movflags","+faststart","-t",f"{total:.3f}",FINAL])
print(f"DONE: {FINAL}  {dur(FINAL):.2f}s")
