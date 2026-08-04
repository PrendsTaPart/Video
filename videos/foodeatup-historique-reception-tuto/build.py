#!/usr/bin/env python3
# FoodEatUp "Retrouver l'historique de ses livraisons (Contrôle à réception)"
# tutorial. Same engine as foodeatup-tva-tuto/build.py: no avatar clip, full
# ElevenLabs VO throughout, setpts speed (never zoompan on real footage),
# xfade on every cut, 48kHz stereo AAC +faststart. Segment targets sized
# against each VO line's measured duration (vo/*.mp3) before building.
import subprocess, os, sys
sys.path.insert(0, "/home/user/Video/videos/_shared")
from claude_prompt_sequence import (
    render_claude_stage1_png, render_claude_stage2_png, render_claude_stage3_png,
)

ROOT = "/home/user/Video/videos/foodeatup-historique-reception-tuto"
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

# Buttons (pixel coords in 1920x828 source space, read off extracted frames)
BTN_CARD      = (342, 562); SZ_CARD      = (360, 300)  # "Contrôle à réception" card
BTN_MODIFIER  = (826, 631); SZ_MODIFIER  = (168, 58)   # "Modifier" (2nd row card)
BTN_SUPPRIMER = (642, 631); SZ_SUPPRIMER = (150, 58)   # "Supprimer" (2nd row card)
BTN_ANNULER   = (838, 601); SZ_ANNULER   = (134, 58)   # "Annuler" (modal confirmation)

# (name, src_start, src_end, target_out_duration, click_time_or_None, button, btn_size, caption)
# Segment targets sized against the measured VO durations (vo/N*.mp3) --
# N1..N5 narrate the click/action sequence, N0/N6/N7/N8 handled separately
# (intro card, Claude sequence, outro card). See rule in
# FOODEATUP-TUTORIELS-WORKFLOW.md: calibrate segment duration on the VO line
# that comments it, not the other way around.
segs = [
    ("A", 0.20,  5.60,  3.00, None,  None,          None,          "Historique HACCP"),
    ("B", 5.60,  5.85,  0.90, 5.70,  BTN_CARD,       SZ_CARD,       None),
    ("C", 6.20,  9.35,  4.40, None,  None,          None,          "Filtrer par date, fournisseur, état"),
    ("D", 9.35,  9.60,  0.90, 9.45,  BTN_MODIFIER,   SZ_MODIFIER,   None),
    ("E", 9.60, 18.00,  7.90, None,  None,          None,          "Modifier une fiche"),
    ("F", 18.00, 18.75, 0.60, None,  None,          None,          None),
    ("G", 18.75, 19.00, 0.90, 18.85, BTN_SUPPRIMER,  SZ_SUPPRIMER,  "Supprimer une fiche"),
    ("H", 19.00, 21.35, 3.20, None,  None,          None,          None),
    ("I", 21.35, 21.60, 0.90, 21.45, BTN_ANNULER,    SZ_ANNULER,    None),
    ("J", 21.60, 23.40, 1.30, None,  None,          None,          None),
]
INTRO_D, OUTRO_D = 5.90, 5.30

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
# across the whole series (videos/_shared/claude_prompt_sequence.py). Same
# visual universe on every video that has a matching FoodEatUp MCP tool --
# only the prompt text (and, here, the reply line) changes.
# ---------------------------------------------------------------------------
CLAUDE_PROMPT = ("Enregistre un contrôle à réception pour mon établissement FoodEatUp "
                  "(ID [ID établissement]) : fournisseur [nom du fournisseur], "
                  "livraison du [date] à [heure], état [conforme ou non conforme].")
CLAUDE_RESPONSE = "Bien sûr ! J'enregistre ce contrôle de réception pour votre établissement…"

def card(img, out, secs, zoom_in=True, fade=True):
    """fade=False for cards that sit mid-video and only ever meet the rest
    of the timeline through an xfade crossfade (e.g. the claude1/2/3 chatbot
    stages) -- baking in card()'s own 0.4s fade-to-black on top of a short
    clip's crossfades on both sides stacks two darkenings and makes brief
    cards (~1s) read as a murky blur instead of a clean beat. Regular
    intro/outro (true start/end of the video) keep fade=True."""
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

# reveal, copied, chatbot mockup -- 2 dedicated VO lines (N6 over stage1+2,
# N7 over stage3), measured N6=5.85s / N7=4.60s, stages sized to give each
# room (measure-VO-before-segments rule, see FOODEATUP-TUTORIELS-WORKFLOW.md).
CLAUDE_STAGE_D = [3.20, 2.60, 4.80]  # reveal, copied, chatbot mockup

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

    # slideleft between the 3 claude stages (distinct scenes/cuts, same
    # convention as skipped-footage cuts elsewhere) and into/out of outro;
    # fade everywhere else (continuous screen-recording action).
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
    "N2": S["C"] + 0.20,
    "N3": S["D"] + 0.20,
    "N4": S["E"] + 0.20,
    "N5": S["G"] + 0.20,
    "N6": S["claude1"] + 0.20,   # explains the prompt (reveal + copied)
    "N7": S["claude3"] + 0.20,   # presents sending it to Claude
    "N8": OUTRO_START + 0.35,    # CTA
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
FINAL = f"{ROOT}/out/foodeatup-historique-reception-tuto-v1.mp4"
os.makedirs(f"{ROOT}/out", exist_ok=True)
run(["ffmpeg","-y","-v","error","-i",silent] + inputs +
    ["-filter_complex",";".join(filters),"-map","0:v","-map","[voa]",
     "-c:v","copy","-c:a","aac","-b:a","192k","-ar","48000","-ac","2",
     "-movflags","+faststart","-t",f"{total:.3f}",FINAL])
print(f"DONE: {FINAL}  {dur(FINAL):.2f}s")
