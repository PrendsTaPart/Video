#!/usr/bin/env python3
# FoodEatUp "Gerer ses Tables (ajout & blocage)" tutorial.
#
# Full ElevenLabs VO (N0-N5, N7 generated; N6/N8 reused verbatim -- see SCRIPT.md).
# Claude sequence: mcp__FoodEatUp__create_table matches exactly what the rush
# shows (ajout d'une table T9 : forme, capacite, zone).
#
# Same engine as the rest of the series: setpts for speed (never zoompan on
# real footage -- freezes the image), fixed crop+scale zoom-punch on clicks,
# xfade on every cut forced back to yuv420p, 48kHz stereo AAC, +faststart.
#
# banner(): uses drawtext's own box=1 (NOT drawbox) for the sliding plate --
# drawbox does not expose a timestamp variable in this ffmpeg build (6.1.1),
# its `t` is stroke thickness, so an x(t) slide expression on a drawbox
# silently parks the plate off-screen forever (confirmed empirically: the
# zones-nettoyage-tuto reference output has NO visible banner plate at all,
# just bare white drawtext on a light page -- checked via astats/pixel probe
# before writing this file). drawtext's box DOES track its own t, so we draw
# two passes of drawtext-with-box (orange peeking left, blue on top) instead.
# See videos/foodeatup-mouvements-stock-tuto/build.py for the same fix.
import subprocess, os, sys
sys.path.insert(0, "/home/user/Video/videos/_shared")
from claude_prompt_sequence import (
    render_claude_stage1_png, render_claude_stage2_png, render_claude_stage3_png,
)

ROOT = "/home/user/Video/videos/foodeatup-gerer-tables-tuto"
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
    # NEVER put an apostrophe in here: injected between single quotes in the
    # -vf argument, would close the string early.
    if not text: return None
    assert "'" not in text, f"apostrophe in banner text: {text}"
    tin, sl = 0.15, 0.32
    tout = max(tin + sl + 0.3, seg_dur - 0.55)
    a = f"min(1\\,max(0\\,(t-{tin})/{sl}))"
    b = f"min(1\\,max(0\\,(t-{tout})/{sl}))"
    x = f"-640+700*({a})-700*({b})"
    y = H - 92
    common = (f"fontfile={FONT}:text='{text}':fontsize=31:boxborderw=18:y={y}")
    return (f"drawtext={common}:fontcolor={ORANGE}@0.0:box=1:boxcolor={ORANGE}@0.98"
            f":x='({x})+34-14',"
            f"drawtext={common}:fontcolor=white:box=1:boxcolor={BLUE}@0.92"
            f":x='({x})+34'")

# Coordinates measured on real extracted frames (work/scan/), by color
# thresholding button fill against page background where possible, cross-
# checked visually. Page scroll offset differs across the rush (0-40s: the
# "Zones/Ajouter une table/Enregistrer/Vue" row sits at y~163; after saving
# and clicking T9, page settles at the top, header visible, y~320+).
BTN_EDITER      = (1699, 163); SZ_EDITER      = (145, 55)  # "Editer" (top right, scrolled state)
BTN_AJOUTER     = (1330, 163); SZ_AJOUTER     = (240, 50)  # "Ajouter une table" (mode edition nav)
BTN_ENREGISTRER = (1551, 321); SZ_ENREGISTRER = (180, 58)  # "Enregistrer" (top of page, scrolled to top)
BTN_T9CARD      = (1568, 658); SZ_T9CARD      = (350, 62)  # T9 card header ("T9 / 12 couverts / Libre")
BTN_LIBRE       = (1480, 462); SZ_LIBRE       = (166, 48)  # "Libre" status button (2x2 grid + Bloquee row)

# Targets are sized on the VO line that anchors each segment, counting the
# xfade overlap: a segment only contributes (target - XF) to the timeline.
#
# (name, src_start, src_end, target_out_duration, button, btn_size, caption)
segs = [
    ("A", 0.00,  5.00,  3.00, None,            None,            "Plan de salle : ajoutez ou bloquez vos tables"),
    ("B", 5.00,  5.30,  0.90, BTN_EDITER,       SZ_EDITER,       None),
    ("C", 5.30,  8.55,  5.50, None,            None,            "Mode edition active"),
    ("D", 8.55,  8.85,  0.90, BTN_AJOUTER,      SZ_AJOUTER,      None),
    ("E", 8.85,  40.05, 10.00, None,           None,            "Configurez forme, capacite et zone"),
    ("F", 40.05, 40.35, 0.90, BTN_ENREGISTRER,  SZ_ENREGISTRER,  None),
    ("G", 40.35, 40.85, 4.70, None,            None,            "Nouvelle table disponible"),
    ("H", 40.85, 41.15, 0.90, BTN_T9CARD,       SZ_T9CARD,       None),
    ("I", 41.15, 57.45, 10.00, None,           None,            "Changez son statut en un clic"),
    ("J", 57.45, 62.00, 5.15, BTN_LIBRE,        SZ_LIBRE,        None),
]
INTRO_D, OUTRO_D = 5.50, 6.20

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
# "Use it with Claude" sequence -- shared 3-stage chatbot animation.
# mcp__FoodEatUp__create_table(establishment_id, name, shape?, capacity?,
# zone_id?) matches exactly what the rush shows: ajout de T9 (forme,
# capacite, zone). See SCRIPT.md for the full rationale (2nd prompt about
# blocking a table stays on the Lovable sheet only, per the one-prompt rule).
# ---------------------------------------------------------------------------
CLAUDE_PROMPT = ("Ajoute une table nommée [nom de la table] pour mon établissement "
                  "FoodEatUp (ID [ID établissement]), capacité [nombre] couverts, "
                  "forme [ronde/carrée/rectangle].")
CLAUDE_RESPONSE = "Bien sûr ! J'ajoute cette table à votre plan de salle…"

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

CLAUDE_STAGE_D = [3.00, 2.30, 5.50]  # reveal, copied, chatbot mockup

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
    parts.append(f"{SEG}/claude1.mp4")
    parts.append(f"{SEG}/claude2.mp4")
    parts.append(f"{SEG}/claude3.mp4")
    parts.append(f"{SEG}/outro.mp4")

    trans = ["fade",       # intro -> A
             "fade",       # A -> B (continuous: click on Editer)
             "slideleft",  # B -> C (cut into mode edition)
             "fade",       # C -> D (continuous: click Ajouter une table)
             "slideleft",  # D -> E (cut: T9 created, form opens)
             "fade",       # E -> F (continuous: click Enregistrer)
             "slideleft",  # F -> G (cut: back to normal view)
             "fade",       # G -> H (continuous: click T9)
             "slideleft",  # H -> I (cut: status panel, cycle statuses)
             "slideleft",  # I -> J (cut: Bloquee held, then click Libre)
             "slideleft",  # J -> claude1
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
    "N1": S["C"] + 0.30,         # mode edition
    "N2": S["E"] + 0.20,         # forme / capacite / zone
    "N3": S["G"] + 0.20,         # enregistrer -> nouvelle table disponible
    "N4": S["H"] + 0.20,         # click T9 -> changer le statut
    "N5": S["J"] + 0.30,         # bloquee (benefit line, spills into Libre click)
    "N6": S["claude1"] + 0.20,   # explains the prompt (reveal + copied)
    "N7": S["claude3"] + 0.20,   # paste into Claude -> instant result
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
FINAL = f"{ROOT}/out/foodeatup-gerer-tables-tuto-v1.mp4"
run(["ffmpeg","-y","-v","error","-i",silent] + inputs +
    ["-filter_complex",";".join(filters),"-map","0:v","-map","[voa]",
     "-c:v","copy","-c:a","aac","-b:a","192k","-ar","48000","-ac","2",
     "-movflags","+faststart","-t",f"{total:.3f}",FINAL])
print(f"DONE: {FINAL}  {dur(FINAL):.2f}s")
