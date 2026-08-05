#!/usr/bin/env python3
# FoodEatUp "Calendrier de communication (agent Iris)" tutorial.
# Same engine as the rest of the series: no avatar clip, full ElevenLabs VO,
# speed = setpts (never zoompan on real footage), xfade on every cut, forced
# back to yuv420p at the end of the chain. 48kHz stereo AAC, +faststart.
# Segment targets are calibrated on each VO line's measured .mp3 duration,
# not the other way round (see FOODEATUP-TUTORIELS-WORKFLOW.md).
#
# banner(): uses the FIXED implementation (two drawtext layers, box=1), NOT
# the old drawbox+drawtext version -- ffmpeg 6.1.1's drawbox does not
# re-evaluate x/y/w/h per frame, only drawtext does. See
# videos/foodeatup-mouvement-stock-tuto/build.py and
# videos/FOODEATUP-TUTORIELS-WORKFLOW.md ("Pieges deja rencontres").
import subprocess, os, sys
sys.path.insert(0, "/home/user/Video/videos/_shared")
from claude_prompt_sequence import (
    render_claude_stage1_png, render_claude_stage2_png, render_claude_stage3_png,
)

ROOT = "/home/user/Video/videos/foodeatup-calendrier-iris-tuto"
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

# Step banner -- two drawtext layers sharing the same slide expression, NOT
# drawbox+drawtext. drawbox does not evaluate a t-dependent x on ffmpeg
# 6.1.1 (silently draws off-screen); drawtext does. The plate is drawtext's
# own box=1 (boxborderw=16 around a 31px line = 62px plate), the orange
# filet is the same plate redrawn 10px to the left in orange underneath.
# Fixed implementation copied from foodeatup-mouvement-stock-tuto/build.py.
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

# Coordinates measured on the actual click frames (work/frames/), not
# eyeballed on a neighbouring frame -- the rush auto-scrolls a lot (Iris
# page), so several buttons only sit at these coordinates for ~1s around
# their own click. No apostrophe in any caption below (bug hit on
# foodeatup-ingredients-tuto -- see FOODEATUP-TUTORIELS-WORKFLOW.md).
BTN_CALENDRIER = (198, 210);   SZ_CALENDRIER = (220, 64)   # "Calendrier" tab
BTN_GENERER    = (1585, 283);  SZ_GENERER    = (560, 68)   # "Generer les propositions de la semaine"
BTN_DOTS       = (1745, 268);  SZ_DOTS       = (30, 30)    # menu "..." sur une proposition
BTN_VALIDER    = (1575, 320);  SZ_VALIDER    = (190, 36)   # "Valider & planifier" dans le menu

# (name, src_start, src_end, target_out_duration, button, btn_size, caption)
# Targets sized against the measured N0-N9 VO durations (vo/*.mp3), not the
# reverse -- the "Fabrication en cours..." wait in the raw rush is ~22s of
# dead air (button disabled, nothing moves on screen): cut down hard to a
# 2.2s beat rather than reproduced at real length (workflow doc: "eviter les
# blancs, viser le minimum necessaire").
segs = [
    ("A", 0.30,  3.00,  4.60, None,          None,          "1 · Iris détecte des opportunités"),
    ("B", 2.50,  2.80,  0.90, BTN_CALENDRIER, SZ_CALENDRIER, None),
    ("C", 3.00,  6.00,  4.20, None,          None,          "2 · Calendrier de la semaine"),
    ("D", 11.00, 11.30, 0.90, BTN_GENERER,    SZ_GENERER,    None),
    ("E", 11.30, 12.00, 6.00, None,          None,          "Iris analyse vos données"),
    ("F", 33.30, 35.50, 2.30, None,          None,          "Propositions générées"),
    ("G", 44.00, 48.00, 3.40, None,          None,          "3 · Textes et visuels par IA"),
    ("H", 56.00, 60.00, 4.00, None,          None,          None),
    ("I", 62.90, 63.15, 0.90, BTN_DOTS,       SZ_DOTS,       None),
    ("J", 63.30, 63.55, 0.90, BTN_VALIDER,    SZ_VALIDER,    "4 · Validez la proposition"),
    ("K", 63.55, 67.50, 5.00, None,          None,          None),
]
INTRO_D, OUTRO_D = 6.30, 6.30

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
# "Use it with Claude" sequence -- shared 3-stage chatbot animation
# (videos/_shared/claude_prompt_sequence.py). mcp__Foodeatup__propose_campaigns
# (establishment_id) is the matching tool: "Agent IA marketing : 2-4
# propositions de campagnes chiffrees depuis les donnees reelles (RFM, jours
# creux, marges, marronniers)" -- this IS the Iris agent shown in the rush.
# ---------------------------------------------------------------------------
CLAUDE_PROMPT = ("Utilise Iris pour me proposer 2 à 4 campagnes marketing "
                  "chiffrées pour mon établissement FoodEatUp (ID [ID établissement]), "
                  "basées sur mes segments clients, mes jours creux et mes marges.")
CLAUDE_RESPONSE = "Bien sûr ! Je prépare ces propositions de campagnes pour votre établissement…"

def card(img, out, secs, zoom_in=True, fade=True):
    """fade=False for the claude stages: they sit mid-video and only meet the
    timeline through xfade -- adding card()'s own fade-to-black on top makes
    short stages read as a murky blur (bug hit on the tva build)."""
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

# N7 (5.56s) has to span stages 1+2 (reveal+copie) and N8 (5.67s) has to fit
# inside stage 3 alone (chatbot mockup) -- both notably longer than the
# shared default [2.20,1.30,2.50], hence this project-level override
# (measure-VO-before-segments rule, see FOODEATUP-TUTORIELS-WORKFLOW.md).
CLAUDE_STAGE_D = [4.20, 3.10, 6.30]  # reveal, copied, chatbot mockup

def build_silent(outro_d):
    card(f"{ROOT}/assets/intro.jpg", f"{SEG}/intro.mp4", INTRO_D, zoom_in=True)
    card(f"{ROOT}/assets/outro.jpg", f"{SEG}/outro.mp4", outro_d, zoom_in=False)
    c1, c2, c3 = f"{SEG}/claude1.png", f"{SEG}/claude2.png", f"{SEG}/claude3.png"
    if not os.path.exists(c1):
        render_claude_stage1_png(c1, W, H, CLAUDE_PROMPT)
    if not os.path.exists(c2):
        render_claude_stage2_png(c2, W, H, CLAUDE_PROMPT)
    if not os.path.exists(c3):
        render_claude_stage3_png(c3, W, H, CLAUDE_PROMPT, response=CLAUDE_RESPONSE)
    for i, png in enumerate([c1, c2, c3]):
        card(png, f"{SEG}/claude{i+1}.mp4", CLAUDE_STAGE_D[i], zoom_in=True, fade=False)
    parts = [f"{SEG}/intro.mp4"]
    for name, s, e, target, btn, sz, cap in segs:
        parts.append(encode_seg(name, s, e, target, btn, sz, cap))
    parts += [f"{SEG}/claude1.mp4", f"{SEG}/claude2.mp4", f"{SEG}/claude3.mp4",
              f"{SEG}/outro.mp4"]

    trans = ["fade",       # intro -> A
             "fade",       # A -> B (continuous: click on Calendrier tab)
             "slideleft",  # B -> C (cut into the calendar view)
             "slideleft",  # C -> D (cut: jump to the Generer button)
             "fade",       # D -> E (continuous: click Generer)
             "slideleft",  # E -> F (cut: fabrication -> result, time skip)
             "slideleft",  # F -> G (cut: new week's proposals appear)
             "fade",       # G -> H (continuous: visuals finish generating)
             "slideleft",  # H -> I (cut: jump to a proposal's menu)
             "fade",       # I -> J (continuous: dots menu -> Valider & planifier)
             "fade",       # J -> K (continuous: click -> validee)
             "slideleft",  # K -> claude1
             "slideleft",  # claude1 -> claude2
             "slideleft",  # claude2 -> claude3
             "fade"]       # claude3 -> outro
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
    "N1": S["A"] + 0.20,         # Iris detecte des opportunites (segment A)
    "N2": S["C"] + 0.20,         # ouvrez Calendrier, cliquez Generer (segment C, post-tab-click)
    "N3": S["E"] + 0.20,         # Iris analyse ventes/stocks/temps forts (segment E, fabrication)
    "N4": S["F"] + 0.20,         # textes et visuels generes automatiquement (segment F, resultat)
    "N5": S["H"] + 0.20,         # raison detectee -> valider/refuser (segment H)
    "N6": S["K"] + 0.20,         # publication planifiee automatiquement (segment K, validee)
    "N7": S["claude1"] + 0.20,   # explique le prompt (reveal + copie)
    "N8": S["claude3"] + 0.20,   # colle dans Claude -> resultat
    "N9": OUTRO_START + 0.35,    # CTA
}
keys = [f"N{i}" for i in range(10)]
off, prev_end = {}, -GAP
for k in keys:
    o = max(anchor[k], prev_end + GAP); off[k] = o
    prev_end = o + dur(f"{ROOT}/vo/{k}.mp3")
print("offsets:", {k: round(v, 2) for k, v in off.items()}, "voice_end:", round(prev_end, 2))
drift = {k: round(off[k] - anchor[k], 2) for k in keys if off[k] - anchor[k] > 0.05}
print("drift vs anchors:", drift if drift else "none -- all lines on their anchors")
print("stage starts:", {k: round(v, 2) for k, v in S.items()})
if drift:
    print("WARNING: non-zero drift detected -- re-time segments before shipping.")

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
FINAL = f"{ROOT}/out/foodeatup-calendrier-iris-tuto-v1.mp4"
run(["ffmpeg","-y","-v","error","-i",silent] + inputs +
    ["-filter_complex",";".join(filters),"-map","0:v","-map","[voa]",
     "-c:v","copy","-c:a","aac","-b:a","192k","-ar","48000","-ac","2",
     "-movflags","+faststart","-t",f"{total:.3f}",FINAL])
print(f"DONE: {FINAL}  {dur(FINAL):.2f}s")
