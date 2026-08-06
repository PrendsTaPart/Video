#!/usr/bin/env python3
# FoodEatUp "Commander : Site, Agent vocal & QR code a table" tutorial.
# Same engine as the rest of the series: no avatar clip, full ElevenLabs VO,
# speed = setpts (never zoompan on real footage), xfade on every cut, forced
# back to yuv420p at the end of the chain. 48kHz stereo AAC, +faststart.
#
# The rush only films the "site" ordering journey (voice agent and QR-code
# ordering are not screen-capturable). Those two channels are introduced via
# VO + a static transition card that reuses assets/intro.jpg (it already
# depicts all 3 channels together), between the last "site" segment and the
# Claude sequence.
import subprocess, os, sys
sys.path.insert(0, "/home/user/Video/videos/_shared")
from claude_prompt_sequence import (
    render_claude_stage1_png, render_claude_stage2_png, render_claude_stage3_png,
)

ROOT = "/home/user/Video/videos/foodeatup-commander-via-site-vocal-qrcode-tuto"
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

# Step banner -- two drawtext layers (box=1), NOT drawbox+drawtext. ffmpeg
# 6.1.1's drawbox does not evaluate x/y/w/h per frame (silently frozen at
# init), so an animated slide-in built out of drawbox is invisible -- see
# FOODEATUP-TUTORIELS-WORKFLOW.md and videos/foodeatup-mouvement-stock-tuto/
# build.py (reference fix). drawtext's own `box` follows `t` correctly.
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

# Coordinates measured on the rush frames via a pixel grid overlay
# (work/grid/*.png), not eyeballed.
BTN_ADD_PIZZA = (740, 486);   SZ_ADD_PIZZA = (332, 48)   # "AJOUTER" (carte Pizza)
BTN_COMMANDER = (1567, 762);  SZ_COMMANDER = (600, 62)   # "Commander" (panier)
BTN_PASSER    = (632, 724);   SZ_PASSER    = (908, 77)   # "Passer au paiement"

# (name, src_start, src_end, target_out_duration, button, btn_size, caption)
# Targets sized close to each VO line's measured duration (see vo/*.mp3)
# before building -- see FOODEATUP-TUTORIELS-WORKFLOW.md.
segs = [
    ("A", 0.50, 4.90, 3.60, None,           None,          "1 · Parcourir le menu"),
    ("B", 4.85, 5.10, 0.90, BTN_ADD_PIZZA,  SZ_ADD_PIZZA,  None),
    ("C", 5.30, 16.50, 3.00, None,          None,          "Ajouter au panier"),
    ("D", 16.50, 16.75, 0.90, BTN_COMMANDER, SZ_COMMANDER, None),
    ("E", 17.00, 20.00, 3.00, None,         None,          "2 · Récupération et horaire"),
    ("F", 20.00, 24.50, 3.20, None,         None,          "3 · Ses coordonnées"),
    ("G", 40.80, 41.05, 0.90, BTN_PASSER,   SZ_PASSER,     None),
    ("H", 41.30, 50.00, 3.00, None,         None,          "4 · Paiement sécurisé"),
]
INTRO_D, OUTRO_D, TRANS_D = 6.20, 6.20, 6.30

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
# "Use it with Claude" sequence -- shared module (videos/_shared/
# claude_prompt_sequence.py). mcp__FoodEatUp__list_orders(establishment_id,
# channel) accepts exactly manuel|telephone|vitrine|agent_vocal|sur_place|
# facture|devis -- a direct match for the 3 channels of this tutorial.
# ---------------------------------------------------------------------------
CLAUDE_PROMPT = ("Montre-moi les commandes reçues aujourd'hui par "
                  "[canal : vitrine / agent_vocal / sur_place] pour mon "
                  "établissement FoodEatUp (ID [ID établissement]).")
CLAUDE_RESPONSE = "Bien sûr ! Je récupère les commandes de ce canal…"

def card(img, out, secs, zoom_in=True, fade=True):
    """fade=False for cards that sit mid-video and only ever meet the rest
    of the timeline through an xfade crossfade (transition card + the
    claude1/2/3 chatbot stages) -- see claude_prompt_sequence.py docstring
    for why stacking card()'s own fade on a short xfaded clip is a bug."""
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

# Stage durations sized for N7 (4.41s, reused tva-tuto N6 audio, covers
# stage1+2) and N8 (4.08s, covers stage3) -- see SCRIPT.md.
CLAUDE_STAGE_D = [3.00, 2.30, 4.60]  # reveal, copied, chatbot mockup

def build_silent(outro_d):
    card(f"{ROOT}/assets/intro.jpg", f"{SEG}/intro.mp4", INTRO_D, zoom_in=True)
    card(f"{ROOT}/assets/outro.jpg", f"{SEG}/outro.mp4", outro_d, zoom_in=False)
    # Transition card (vocal + QR code) reuses the intro art -- it already
    # shows all 3 channels together, no need for a separate asset.
    card(f"{ROOT}/assets/intro.jpg", f"{SEG}/trans.mp4", TRANS_D, zoom_in=False, fade=False)

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
    for name, s, e, target, btn, sz, cap in segs:
        parts.append(encode_seg(name, s, e, target, btn, sz, cap))
    parts.append(f"{SEG}/trans.mp4")
    parts.append(f"{SEG}/claude1.mp4")
    parts.append(f"{SEG}/claude2.mp4")
    parts.append(f"{SEG}/claude3.mp4")
    parts.append(f"{SEG}/outro.mp4")

    # slideleft for scene cuts (last rush seg -> transition card -> the 3
    # claude stages); fade everywhere else (continuous screen-recording
    # action, and claude3 -> outro which stays in the same card family).
    trans = ["fade"] * (len(parts) - 1)
    trans[-5] = "slideleft"  # last real seg -> transition card
    trans[-4] = "slideleft"  # transition card -> claude1
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
labels_order = ["intro"] + [s[0] for s in segs] + ["trans", "claude1", "claude2", "claude3", "outro"]
S = dict(zip(labels_order, starts))
OUTRO_START = S["outro"]

GAP = 0.22
anchor = {
    "N0": 0.30,
    "N1": S["A"] + 0.20,
    "N2": S["C"] + 0.20,
    "N3": S["E"] + 0.20,
    "N4": S["F"] + 0.20,
    "N5": S["G"] + 0.20,
    "N6": S["trans"] + 0.20,
    "N7": S["claude1"] + 0.20,
    "N8": S["claude3"] + 0.20,
    "N9": OUTRO_START + 0.35,
}
keys = [f"N{i}" for i in range(10)]
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
FINAL = f"{ROOT}/out/foodeatup-commander-via-site-vocal-qrcode-tuto-v1.mp4"
run(["ffmpeg","-y","-v","error","-i",silent] + inputs +
    ["-filter_complex",";".join(filters),"-map","0:v","-map","[voa]",
     "-c:v","copy","-c:a","aac","-b:a","192k","-ar","48000","-ac","2",
     "-movflags","+faststart","-t",f"{total:.3f}",FINAL])
print(f"DONE: {FINAL}  {dur(FINAL):.2f}s")
