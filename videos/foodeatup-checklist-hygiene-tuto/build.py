#!/usr/bin/env python3
# FoodEatUp "Creer sa check-list hygiene" tutorial (module HACCP).
# No avatar clip: full ElevenLabs VO throughout. Speed = setpts (never
# zoompan on real footage). xfade on every cut, forced back to yuv420p at
# the end of the chain. 48kHz stereo AAC, +faststart.
#
# Claude sequence: two mcp__Foodeatup__* tools match this rush --
# create_hygiene_checklist (create) and create_hygiene_checklist_validation
# (validate). Video features the "create" prompt (primary action); the
# "validate" prompt is offered as a second entry in Lovable's claudePrompts[]
# (same pattern as saisir-ses-ingredients), not duplicated in the video.
import sys, subprocess, os
sys.path.insert(0, "/home/user/Video/videos/_shared")
from claude_prompt_sequence import (
    render_claude_stage1_png, render_claude_stage2_png, render_claude_stage3_png,
    CLAUDE_STAGE_D,
)

ROOT = "/home/user/Video/videos/foodeatup-checklist-hygiene-tuto"
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

# Coordinates read off the extracted frames (work/frames*/f_*.png), roughly
# centred on each button (crop just needs to keep the button inside frame).
BTN_ADD    = (1662, 340); SZ_ADD    = (266, 58)  # "Ajouter une checklist"
BTN_CREATE = (1024, 745); SZ_CREATE = (173, 60)  # "Creer" (modale ajout)
BTN_VALID  = (1024, 758); SZ_VALID  = (123, 60)  # "Valider" (modale validation)

# (name, src_start, src_end, target_out_duration, button, btn_size, caption)
segs = [
    ("A", 0.20,  7.00,  4.25, None,       None,      "1 - Ouvrir Checklist hygiene"),
    ("B", 7.00,  7.35,  0.90, BTN_ADD,    SZ_ADD,    None),
    ("C", 7.50,  32.50, 4.25, None,       None,      "2 - Nom, categorie, description"),
    ("D", 32.50, 32.85, 0.90, BTN_CREATE, SZ_CREATE, None),
    ("E", 33.50, 41.00, 3.95, None,       None,      "Checklist creee"),
    ("F", 41.00, 58.50, 4.55, None,       None,      "3 - Zone et reponse"),
    ("G", 58.50, 58.85, 0.90, BTN_VALID,  SZ_VALID,  None),
    ("H", 59.00, 67.80, 6.45, None,       None,      "Checklist validee"),
]
# +0.45s padding on every non-punch segment vs. the raw VO-matched value,
# to absorb the xfade crossfade overlap (XF=0.28s eaten at each of the ~12
# cuts) -- without it, drift compounds across the timeline (observed ~4.2s
# by the outro on the previous pass) and forces an oversized silent outro.
INTRO_D, OUTRO_D = 3.85, 5.55

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

# "Use it with Claude" 3-stage sequence -- shared module, only the prompt
# text changes. Featured prompt = create_hygiene_checklist (primary action).
CLAUDE_PROMPT = ("Cree une checklist hygiene [nom du point de controle] pour la "
                  "categorie [hygiene du personnel / etat des locaux], avec les "
                  "points de controle [liste des points], pour mon etablissement "
                  "FoodEatUp (ID [ID etablissement]).")
CLAUDE_RESPONSE = "Bien sur ! Je cree cette checklist hygiene pour votre etablissement..."
# Widened vs. the module default [2.20, 1.30, 2.50]: N6 (4.41s) needs to fit
# across stage1+2 (reveal+copied), N7 (4.21s) needs to fit within stage3 alone.
CLAUDE_STAGE_D = [3.35, 2.15, 4.85]

def build_silent(outro_d):
    card(f"{ROOT}/assets/intro.jpg", f"{SEG}/intro.mp4", INTRO_D, zoom_in=True)
    card(f"{ROOT}/assets/outro.jpg", f"{SEG}/outro.mp4", outro_d, zoom_in=False)

    claude1_png, claude2_png, claude3_png = f"{SEG}/claude1.png", f"{SEG}/claude2.png", f"{SEG}/claude3.png"
    render_claude_stage1_png(claude1_png, W, H, CLAUDE_PROMPT)
    render_claude_stage2_png(claude2_png, W, H, CLAUDE_PROMPT)
    render_claude_stage3_png(claude3_png, W, H, CLAUDE_PROMPT, response=CLAUDE_RESPONSE)
    for i, png in enumerate([claude1_png, claude2_png, claude3_png]):
        card(png, f"{SEG}/claude{i+1}.mp4", CLAUDE_STAGE_D[i], zoom_in=True, fade=False)

    parts = [f"{SEG}/intro.mp4"]
    for name, s, e, target, btn, sz, cap in segs:
        parts.append(encode_seg(name, s, e, target, btn, sz, cap))
    parts.append(f"{SEG}/claude1.mp4")
    parts.append(f"{SEG}/claude2.mp4")
    parts.append(f"{SEG}/claude3.mp4")
    parts.append(f"{SEG}/outro.mp4")

    trans = ["fade",        # intro -> A
             "fade",        # A -> B (continuous: click on the visible page)
             "slideleft",   # B -> C (cut into the opened modal)
             "fade",        # C -> D (continuous: click Creer)
             "fade",        # D -> E (submit -> toast/list)
             "fade",        # E -> F (open validation modal)
             "fade",        # F -> G (continuous: click Valider)
             "fade",        # G -> H (submit -> toast)
             "slideleft",   # H -> claude1 (scene cut)
             "slideleft",   # claude1 -> claude2
             "slideleft",   # claude2 -> claude3
             "fade"]        # claude3 -> outro
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
    "N0": 0.30,                  # intro hook
    "N1": S["A"] + 0.15,         # navigate + clic "Ajouter une checklist"
    "N2": S["C"] + 0.15,         # nom/categorie/description + clic Creer
    "N3": S["E"] + 0.15,         # succes + ouverture validation
    "N4": S["F"] + 0.15,         # zone + reponse + valider
    "N5": S["H"] + 0.15,         # benefice
    "N6": S["claude1"] + 0.20,   # explique le prompt (reveal + copie)
    "N7": S["claude3"] + 0.20,   # colle dans Claude -> resultat
    "N8": OUTRO_START + 0.35,    # CTA
}
keys = [f"N{i}" for i in range(9)]
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
FINAL = f"{ROOT}/out/foodeatup-checklist-hygiene-tuto-v1.mp4"
run(["ffmpeg","-y","-v","error","-i",silent] + inputs +
    ["-filter_complex",";".join(filters),"-map","0:v","-map","[voa]",
     "-c:v","copy","-c:a","aac","-b:a","192k","-ar","48000","-ac","2",
     "-movflags","+faststart","-t",f"{total:.3f}",FINAL])
print(f"DONE: {FINAL}  {dur(FINAL):.2f}s")
