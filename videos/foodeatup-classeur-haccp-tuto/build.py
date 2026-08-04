#!/usr/bin/env python3
# FoodEatUp "Ouvrir son classeur HACCP" tutorial. Same engine as
# foodeatup-tva-tuto: full ElevenLabs VO throughout, xfade on every cut,
# forced back to yuv420p at the end of the chain, 48kHz stereo AAC,
# +faststart. Segment targets are approximate vs. each VO line's measured
# duration (see vo/*.mp3) -- the sequential anchor placement + outro
# auto-extension below absorb any spillover, same safety net as the rest
# of the series.
import subprocess, os, sys
sys.path.insert(0, "/home/user/Video/videos/_shared")
from claude_prompt_sequence import (
    render_claude_stage1_png, render_claude_stage2_png, render_claude_stage3_png,
)

ROOT = "/home/user/Video/videos/foodeatup-classeur-haccp-tuto"
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

BTN_ACCUEIL_HACCP = (975, 196);  SZ_ACCUEIL_HACCP = (160, 32)   # "Accueil HACCP" in the HACCP dropdown
BTN_HISTORIQUE    = (1390, 139); SZ_HISTORIQUE    = (140, 40)   # "Historique" tab (pill)

# (name, src_start, src_end, target_out_duration, click_time_or_None, button, btn_size, caption)
# Source screen.mp4 analysed frame-by-frame (see SCRIPT.md): dashboard ->
# hover/click HACCP menu -> "Accueil HACCP" opens the classeur -> welcome
# screen (4 cards) -> scroll to full module grid -> click "Historique" tab
# -> consolidated history page.
segs = [
    ("A", 0.20, 5.30, 4.20, None, None,              None,             "1 · Ouvrir HACCP"),
    ("B", 6.30, 6.55, 0.90, 6.30, BTN_ACCUEIL_HACCP,  SZ_ACCUEIL_HACCP, None),
    ("C", 7.60, 9.80, 5.30, None, None,              None,             "2 · Votre classeur"),
    ("D", 9.80, 12.30, 6.00, None, None,             None,             "3 · Tous les modules"),
    ("E", 12.30, 12.55, 0.90, 12.30, BTN_HISTORIQUE, SZ_HISTORIQUE,    None),
    ("F", 13.60, 19.40, 5.60, None, None,             None,             "4 · Historique HACCP"),
]
INTRO_D, OUTRO_D = 5.90, 6.20

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
# "Use it with Claude" sequence -- shared 3-stage chatbot-style animation.
# No mcp__FoodEatUp__ tool creates data here (this tutorial is pure
# navigation/consultation), but several read tools together cover exactly
# what "Historique" shows on screen (list_haccp_temperatures,
# list_haccp_tracabilite, list_cleaning_actions, list_haccp_reception) --
# a legitimate "show me" prompt, not an invented one.
# ---------------------------------------------------------------------------
CLAUDE_PROMPT = ("Montre-moi l'historique de mon classeur HACCP (températures, "
                  "traçabilité, nettoyage, production) pour mon établissement "
                  "FoodEatUp (ID [ID établissement]).")
CLAUDE_RESPONSE = "Bien sûr ! Je récupère l'historique de vos modules HACCP…"

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

# N6 (reveal+copied, measured 4.26s) / N7 (chatbot, measured 4.36s) --
# stages sized to give each VO line room (measure-VO-before-segments rule).
CLAUDE_STAGE_D = [2.40, 1.70, 3.10]  # reveal, copied, chatbot mockup

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
    "N1": S["A"] + 0.20,          # "cliquez sur HACCP... Accueil HACCP" (before click B)
    "N2": S["C"] + 0.20,          # accueil classeur, 4 cartes
    "N3": S["D"] + 0.20,          # scroll grille complète
    "N4": S["E"] + 0.10,          # "direction l'onglet Historique" (click E)
    "N5": S["F"] + 0.20,          # page Historique, bénéfice
    "N6": S["claude1"] + 0.20,    # explique le prompt (reveal + copié)
    "N7": S["claude3"] + 0.20,    # présente l'envoi dans Claude
    "N8": OUTRO_START + 0.35,     # CTA
}
keys = [f"N{i}" for i in range(9)]
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
    S = dict(zip(labels_order, starts))
    OUTRO_START = S["outro"]

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
FINAL = f"{ROOT}/out/foodeatup-classeur-haccp-tuto-v1.mp4"
run(["ffmpeg","-y","-v","error","-i",silent] + inputs +
    ["-filter_complex",";".join(filters),"-map","0:v","-map","[voa]",
     "-c:v","copy","-c:a","aac","-b:a","192k","-ar","48000","-ac","2",
     "-movflags","+faststart","-t",f"{total:.3f}",FINAL])
print(f"DONE: {FINAL}  {dur(FINAL):.2f}s")
