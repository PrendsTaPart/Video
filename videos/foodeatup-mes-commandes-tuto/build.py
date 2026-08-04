#!/usr/bin/env python3
# FoodEatUp "Mes commandes" (QR code / Site web / Agent vocal) tutorial.
# No avatar clip: full ElevenLabs VO throughout. Speed = setpts (never
# zoompan on real footage). xfade on every cut, forced back to yuv420p at
# the end of the chain. 48kHz stereo AAC, +faststart.
#
# Rush shows the centralized "Mes commandes" list (all channels: Manuel,
# Vitrine, Sur place... matching mcp__FoodEatUp__list_orders' channel enum
# manuel|telephone|vitrine|agent_vocal|sur_place|facture|devis) -> create an
# order manually (Nouvelle commande) -> view its detail -> edit it (Modifier,
# change status/quantity) -> delete it (no MCP tool for delete).
import subprocess, os, sys
sys.path.insert(0, "/home/user/Video/videos/_shared")
from claude_prompt_sequence import (
    render_claude_stage1_png, render_claude_stage2_png, render_claude_stage3_png,
)

ROOT = "/home/user/Video/videos/foodeatup-mes-commandes-tuto"
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

# Coordinates measured on the actual frames (work/frames/*.png), full
# 1920x828 native pixels, one frame per action / scroll position.
BTN_NOUVELLE = (1647, 353); SZ_NOUVELLE = (295, 50)  # "+ Nouvelle commande"
BTN_CREER    = (1024, 731); SZ_CREER    = (250, 58)  # "Créer la commande"
BTN_MAJ      = (1024, 731); SZ_MAJ      = (200, 58)  # "Mettre à jour"
BTN_DOTS     = (1660, 391); SZ_DOTS     = (24, 20)   # "..." Actions (ligne commande)
BTN_SUPPR    = (872, 588);  SZ_SUPPR    = (170, 56)  # "Supprimer" (confirmation)

# (name, src_start, src_end, target_out_duration, click_time_or_None, button, btn_size, caption)
segs = [
    ("A", 0.20,  2.50, 11.20, None,  None,     None,     "1 - Mes commandes"),
    ("B", 2.50,  2.85,  0.90, 2.65,  BTN_NOUVELLE, SZ_NOUVELLE, None),
    ("C", 2.85, 17.00,  8.80, None,  None,     None,     "2 - Client, canal, mode de service"),
    ("D", 17.00, 21.50, 3.80, None,  None,     None,     "3 - Ajouter un plat"),
    ("E", 21.50, 21.85, 0.90, 21.65, BTN_CREER, SZ_CREER, None),
    ("F", 21.85, 27.00, 4.40, None,  None,     None,     "Commande créée"),
    ("G", 27.00, 33.00, 5.20, None,  None,     None,     "4 - Détail de la commande"),
    ("H", 33.00, 44.00, 6.80, None,  None,     None,     "5 - Modifier"),
    ("I", 44.00, 44.35, 0.90, 44.15, BTN_MAJ,  SZ_MAJ,   None),
    ("J", 44.35, 48.50, 3.80, None,  None,     None,     "Commande mise à jour"),
    ("K", 48.50, 52.85, 4.00, 52.70, BTN_DOTS, SZ_DOTS,  "6 - Supprimer"),
    ("L", 52.85, 56.52, 3.90, 52.95, BTN_SUPPR, SZ_SUPPR, None),
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
# mcp__FoodEatUp__create_order(establishment_id, items, customer_name,
# channel, service_mode, table_id, notes) matches "Nouvelle commande" exactly
# (auto-generates invoice+quote, as shown in the rush's info banner).
# update_order_status also matches "Modifier" -> Statut. No MCP tool for
# delete, so "Supprimer" has no prompt (per pipeline rule).
# ---------------------------------------------------------------------------
CLAUDE_PROMPT = ("Crée une commande pour [nom du client], canal [manuel / vitrine / "
                  "agent_vocal / sur_place], mode [sur_place / emporter / livraison], "
                  "avec [plat] x[quantité] à [prix]€, pour mon établissement FoodEatUp "
                  "(ID [ID établissement]).")
CLAUDE_RESPONSE = "Bien sûr ! Je crée cette commande, avec sa facture et son devis..."

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

CLAUDE_STAGE_D = [2.80, 2.20, 4.60]  # reveal, copied, chatbot mockup

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
             "fade",       # A -> B (continuous: click on the visible page)
             "slideleft",  # B -> C (cut into the opened modal)
             "fade",       # C -> D (continuous: scroll within the same modal)
             "fade",       # D -> E (continuous: click Créer la commande)
             "fade",       # E -> F (submit -> list)
             "slideleft",  # F -> G (cut, list -> order detail popup)
             "slideleft",  # G -> H (cut into the Modifier modal)
             "fade",       # H -> I (continuous: click Mettre à jour)
             "fade",       # I -> J (submit -> list)
             "slideleft",  # J -> K (cut, list -> Actions dropdown/Supprimer)
             "fade",       # K -> L (continuous: confirmation dialog)
             "slideleft",  # L -> claude1
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
    "N1": S["A"] + 0.10,         # "Ouvrez Mes commandes..."
    "N2": S["B"] + 0.10,         # click Nouvelle commande
    "N3": S["C"] + 0.10,         # client/canal/mode/statut + plats
    "N4": S["E"] + 0.10,         # click Créer la commande
    "N5": S["G"] + 0.10,         # détail / Modifier
    "N6": S["I"] + 0.10,         # click Mettre à jour
    "N7": S["K"] + 0.10,         # Actions -> Supprimer
    "N8": S["claude1"] + 0.20,   # explains the prompt (reveal + copied)
    "N9": S["claude3"] + 0.20,   # paste into Claude -> instant result
    "N10": OUTRO_START + 0.35,   # CTA
}
keys = ["N0", "N1", "N2", "N3", "N4", "N5", "N6", "N7", "N8", "N9", "N10"]
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
FINAL = f"{ROOT}/out/foodeatup-mes-commandes-tuto-v1.mp4"
run(["ffmpeg","-y","-v","error","-i",silent] + inputs +
    ["-filter_complex",";".join(filters),"-map","0:v","-map","[voa]",
     "-c:v","copy","-c:a","aac","-b:a","192k","-ar","48000","-ac","2",
     "-movflags","+faststart","-t",f"{total:.3f}",FINAL])
print(f"DONE: {FINAL}  {dur(FINAL):.2f}s")
