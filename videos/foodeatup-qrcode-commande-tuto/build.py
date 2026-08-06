#!/usr/bin/env python3
# FoodEatUp "Commander par QR code (sur site)" tutorial (module Service
# Multi-Canal, slot Lovable "commander-sur-site-qr-ou-vocal"). No avatar
# clip: full ElevenLabs VO throughout. Speed = setpts (never zoompan on
# real footage). xfade on every cut, forced back to yuv420p at the end of
# the chain. 48kHz stereo AAC, +faststart.
#
# Rush is two-actor: staff (Plan de salle -> select table -> "QR code de la
# table") then customer (scan -> menu by category -> add to cart -> submit
# -> order tracking -> split payment). The first 13s (unrelated reservation
# editing) and an 8s dead browser-tab-switch stretch (~29-37s) are cut --
# not part of the QR-ordering story. mcp__FoodEatUp__create_order
# (establishment_id, items, customer_name, channel, service_mode, table_id,
# notes) matches the order the customer places via the QR link exactly
# (channel=vitrine, service_mode=sur_place, table renseignee).
import subprocess, os, sys
sys.path.insert(0, "/home/user/Video/videos/_shared")
from claude_prompt_sequence import (
    render_claude_stage1_png, render_claude_stage2_png, render_claude_stage3_png,
)

ROOT = "/home/user/Video/videos/foodeatup-qrcode-commande-tuto"
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
    return (f"drawbox=x='{ox-bw/2-p}':y='{oy-bh/2-p}'"
            f":w='{bw+2*p}':h='{bh+2*p}'"
            f":color={ORANGE}@0.95:t=5")

# Step banner -- two drawtext layers (each using drawtext's own `box=1`),
# NOT drawbox+drawtext: this ffmpeg (6.1.1) does not evaluate `t` in
# drawbox's x/y/w/h expressions (silently drawn off-screen), while drawtext
# does evaluate t per frame. See FOODEATUP-TUTORIELS-WORKFLOW.md.
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

# Coordinate measured by colorimetric thresholding on the real frame at the
# click instant (PIL, work/frames), not by eye. The "Commander" cart button
# (bottom bar) is near full-width (bbox (26,756)-(1872,808)): too wide for a
# meaningful zoom-punch (the ~1600px crop cannot "punch" a button that's
# already edge-to-edge), so it stays a plain cut, per SCRIPT.md.
BTN_QR = (1569, 495); SZ_QR = (340, 52)  # "QR code de la table"

# (name, src_start, src_end, target_out_duration, click_time_or_None, button, btn_size, caption)
segs = [
    ("A", 13.30, 25.50, 9.50, None,  None,   None,   "1 - Generer le QR code de la table"),
    ("C", 25.50, 25.85, 0.90, 25.65, BTN_QR, SZ_QR,  None),
    ("D", 25.85, 29.00, 6.80, None,  None,   None,   "2 - Le client scanne pour commander"),
    ("E", 37.00, 43.00, 5.70, None,  None,   None,   "3 - La carte, par categories"),
    ("F", 43.00, 52.00, 5.70, None,  None,   None,   "4 - Ajouter ses plats au panier"),
    ("G", 52.00, 55.00, 4.60, None,  None,   None,   "5 - Commande envoyee en cuisine"),
    ("H", 55.00, 61.00, 6.20, None,  None,   None,   "6 - Suivi de la commande"),
    ("I", 61.00, 67.00, 6.20, None,  None,   None,   "7 - Payer, seul ou a plusieurs"),
    ("K", 67.00, 75.96, 7.40, None,  None,   None,   "8 - Paiement securise Stripe"),
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
# mcp__FoodEatUp__create_order matches placing an order for a table exactly
# (channel=vitrine, service_mode=sur_place, table_id) -- same tool as the
# generic "mes-commandes-tous-canaux" prompt, here specialised to a table.
# ---------------------------------------------------------------------------
CLAUDE_PROMPT = ("Crée une commande pour la table [numéro de table], canal vitrine, mode "
                  "sur_place, avec [plat] x[quantité] à [prix]€, pour mon établissement "
                  "FoodEatUp (ID [ID établissement]).")
CLAUDE_RESPONSE = "Bien sûr ! Je crée cette commande sur la table indiquée..."

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

CLAUDE_STAGE_D = [2.80, 2.20, 6.90]  # reveal, copied, chatbot mockup

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
             "fade",       # A -> C (continuous: click on the visible sidebar button)
             "fade",       # C -> D (continuous: modal opening from the click)
             "slideleft",  # D -> E (cut, staff modal -> customer phone/browser)
             "fade",       # E -> F (continuous: scroll within the same menu)
             "fade",       # F -> G (continuous: click Commander)
             "slideleft",  # G -> H (cut, toast -> order tracking screen)
             "fade",       # H -> I (continuous: click Payer l'addition)
             "fade",       # I -> K (continuous: split choice -> payment form)
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
    "N1": S["A"] + 0.10,         # navigation + select table
    "N2": S["D"] + 0.10,         # QR modal
    "N3": S["E"] + 0.10,         # customer menu browse
    "N4": S["F"] + 0.10,         # add to cart
    "N5": S["G"] + 0.10,         # click Commander + toast
    "N6": S["H"] + 0.10,         # order tracking
    "N7": S["I"] + 0.10,         # payer l'addition + split
    "N8": S["K"] + 0.10,         # payment screen -- benefit line
    "N9": S["claude1"] + 0.20,   # explains the prompt (reveal + copied)
    "N10": S["claude3"] + 0.20,  # paste into Claude -> instant result
    "N11": OUTRO_START + 0.35,   # CTA
}
keys = ["N0", "N1", "N2", "N3", "N4", "N5", "N6", "N7", "N8", "N9", "N10", "N11"]
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
FINAL = f"{ROOT}/out/foodeatup-qrcode-commande-tuto-v1.mp4"
run(["ffmpeg","-y","-v","error","-i",silent] + inputs +
    ["-filter_complex",";".join(filters),"-map","0:v","-map","[voa]",
     "-c:v","copy","-c:a","aac","-b:a","192k","-ar","48000","-ac","2",
     "-movflags","+faststart","-t",f"{total:.3f}",FINAL])
print(f"DONE: {FINAL}  {dur(FINAL):.2f}s")
