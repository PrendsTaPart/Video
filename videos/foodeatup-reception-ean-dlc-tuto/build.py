#!/usr/bin/env python3
# FoodEatUp "Scanner le code EAN et la DLC" (Contrôle à réception) tutorial.
# No avatar clip: full ElevenLabs VO throughout (native audio in the rush is
# silent, -91dB). Speed = setpts (never zoompan on real footage). xfade on
# every cut, forced back to yuv420p at the end of the chain. 48kHz stereo
# AAC, +faststart.
#
# Rush: Réception du jour -> open a delivered order -> Produits livrés table
# -> the SAME "..." action menu opens Photo DLC / DLC manuelle / Température
# / Scanner produit for a received product, one at a time -> product ends up
# "Complété". mcp__Foodeatup__create_haccp_label covers DLC + température;
# the EAN scan itself is camera-only, no MCP equivalent (not claimed).
import subprocess, os, sys
sys.path.insert(0, "/home/user/Video/videos/_shared")
from claude_prompt_sequence import (
    render_claude_stage1_png, render_claude_stage2_png, render_claude_stage3_png,
)

ROOT = "/home/user/Video/videos/foodeatup-reception-ean-dlc-tuto"
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
    # Static highlight box (this ffmpeg build's drawbox evaluates x/y/w/h
    # expressions once at t=0 -- see foodeatup-predibot-suggestions-tuto).
    cw, ch, cx, cy = crop_box
    sx, sy = W / cw, H / ch
    bw, bh = btn_wh[0] * sx, btn_wh[1] * sy
    ox, oy = (btn[0] - cx) * sx, (btn[1] - cy) * sy
    p = 14
    return (f"drawbox=x={ox-bw/2-p:.1f}:y={oy-bh/2-p:.1f}"
            f":w={bw+2*p:.1f}:h={bh+2*p:.1f}"
            f":color={ORANGE}@0.95:t=5")

def banner(text, seg_dur):
    # Static position, same reason as punch_highlight above.
    if not text: return None
    x, y = 40, H - 108
    return (f"drawbox=x={x}:y={y}:w=10:h=62:color={ORANGE}@0.98:t=fill,"
            f"drawbox=x={x+10}:y={y}:w=560:h=62:color={BLUE}@0.90:t=fill,"
            f"drawtext=fontfile={FONT}:text='{text}':fontsize=31:fontcolor=white"
            f":x={x+34}:y={y+16}")

# Coordinates measured on the actual frames (ffmpeg -ss t -frames:v 1).
# Same "..." action menu button reused for all 3 punches (Photo DLC,
# Température, Scanner produit all open from it).
BTN_MENU = (1683, 424); SZ_MENU = (70, 35)

# (name, src_start, src_end, target_out_duration, click_time_or_None, button, btn_size, caption)
segs = [
    ("A", 0.00,  2.00,  2.40, None, None,     None,    "1 - Vos livraisons a controler"),
    ("B", 6.00,  8.70,  3.60, None, None,     None,    "2 - Ouvrez une livraison"),
    ("C", 8.70,  9.30,  0.70, 8.90, BTN_MENU, SZ_MENU, None),
    ("D", 9.50, 29.50,  6.00, None, None,     None,    "3 - Ajoutez la DLC (photo ou saisie)"),
    ("E", 30.00, 30.50, 1.00, None, None,     None,    None),
    ("F", 32.00, 32.50, 0.70, 32.10, BTN_MENU, SZ_MENU, None),
    ("G", 33.00, 35.50, 3.20, None, None,     None,    "4 - Modifiez la temperature"),
    ("H", 36.00, 36.50, 1.00, None, None,     None,    None),
    ("I", 38.00, 38.50, 0.70, 38.10, BTN_MENU, SZ_MENU, None),
    ("J", 40.00, 42.00, 3.50, None, None,     None,    "5 - Scannez le code EAN"),
    ("K", 45.00, 47.96, 8.50, None, None,     None,    "Livraison controlee et tracee"),
]
INTRO_D, OUTRO_D = 2.60, 6.20

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
# mcp__Foodeatup__create_haccp_label(establishment_id, ingredient_name, dlc?,
# temperature?, ...) matches DLC + température from a received product's
# photo. EAN scan itself is camera-only, no MCP equivalent -- not claimed.
# ---------------------------------------------------------------------------
CLAUDE_PROMPT = ("Voici la photo de l'étiquette du produit reçu : [joindre la photo]. "
                  "Crée l'étiquette HACCP correspondante (DLC, température de "
                  "réception) pour mon établissement FoodEatUp (ID [ID établissement]).")
CLAUDE_RESPONSE = "Bien sûr ! Je crée l'étiquette HACCP à partir de cette photo…"

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

CLAUDE_STAGE_D = [2.20, 1.30, 2.50]

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
    for name, s, e, target, ck, btn, sz, cap in segs:
        parts.append(encode_seg(name, s, e, target, btn, sz, cap))
    parts.append(f"{SEG}/claude1.mp4")
    parts.append(f"{SEG}/claude2.mp4")
    parts.append(f"{SEG}/claude3.mp4")
    parts.append(f"{SEG}/outro.mp4")

    trans = ["fade",       # intro -> A
             "slideleft",  # A -> B (cut: nav into a specific order)
             "fade",       # B -> C (continuous: click the action menu)
             "slideleft",  # C -> D (cut: Photo DLC modal opens)
             "fade",       # D -> E (continuous: save -> toast)
             "fade",       # E -> F (continuous: click the action menu again)
             "slideleft",  # F -> G (cut: Température modal opens)
             "fade",       # G -> H (continuous: save -> toast)
             "fade",       # H -> I (continuous: click the action menu again)
             "slideleft",  # I -> J (cut: Scanner produit modal opens)
             "slideleft",  # J -> K (cut: scan closes -> Complété)
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
    "N1": S["B"] + 0.10,         # ouvrez la commande livree
    "N2": S["C"] + 0.20,         # clic menu -> Photo DLC / date
    "N3": S["F"] + 0.10,         # clic menu -> temperature
    "N4": S["I"] + 0.10,         # clic menu -> scanner produit
    "N5": S["K"] + 0.20,         # benefice : tracabilite complete
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
FINAL = f"{ROOT}/out/foodeatup-reception-ean-dlc-tuto-v1.mp4"
run(["ffmpeg","-y","-v","error","-i",silent] + inputs +
    ["-filter_complex",";".join(filters),"-map","0:v","-map","[voa]",
     "-c:v","copy","-c:a","aac","-b:a","192k","-ar","48000","-ac","2",
     "-movflags","+faststart","-t",f"{total:.3f}",FINAL])
print(f"DONE: {FINAL}  {dur(FINAL):.2f}s")
