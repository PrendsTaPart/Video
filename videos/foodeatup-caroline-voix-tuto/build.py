#!/usr/bin/env python3
# FoodEatUp "Configurer Caroline (voix & prompts)" tutorial.
# Same engine as the rest of the series: setpts for speed (never zoompan on
# real footage), fixed crop+scale zoom-punch on clicks, xfade on every cut
# forced back to yuv420p, 48kHz stereo AAC, +faststart.
#
# Rush (65.60s) shows TWO things back to back, both real screen capture (no
# synthetic "use it with Claude" stage needed this time -- the rush itself
# captures the live Marketplace-de-prompts -> copy -> paste-in-Claude flow):
#   1) Agent IA Caroline > Configuration voix: prompt systeme, voix/langue/
#      numero, message d'accueil edite puis "Enregistrer" -> toast confirme.
#   2) Menu profil > Marketplace de prompts (produit phare "Foodeatup mcp",
#      filtres par categorie) -> filtre "Commandes(4)" -> copie le prompt
#      "Cree une commande" -> colle dans Claude.ai -> Claude orchestre
#      (create_order: facture + devis generes automatiquement).
import subprocess, os, sys

ROOT = "/home/user/Video/videos/foodeatup-caroline-voix-tuto"
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

BANNER_Y = H - 108

def banner(text, seg_dur):
    # drawbox does not evaluate t in its x/y/w/h in this ffmpeg (6.1.1) -- a
    # drawbox animated on t is silently never drawn. Use drawtext's own `box`
    # instead (it shares drawtext's per-frame t evaluation): filet = same
    # plate drawn 10px further left in orange, blue plate on top covers all
    # but that 10px sliver. See FOODEATUP-TUTORIELS-WORKFLOW.md.
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

# Coordinates eyeballed on extracted frames (1920x828 native).
BTN_SAVE      = (845, 722);  SZ_SAVE      = (170, 50)   # "Enregistrer"
BTN_AVATAR    = (1723, 124); SZ_AVATAR    = (60, 60)    # user avatar (top-right)
BTN_MKT_ITEM  = (1600, 327); SZ_MKT_ITEM  = (240, 32)   # "Marketplace de prompts" menu item
BTN_COPY      = (527, 584);  SZ_COPY      = (40, 40)    # clipboard/copy icon, "Cree une commande"
BTN_SEND      = (1673, 710); SZ_SEND      = (70, 70)    # Claude send arrow

# (name, src_start, src_end, target_out_duration, button, btn_size, caption)
segs = [
    ("A", 0.30,  8.00,  5.20, None,         None,        "1 - Reglez la voix et la langue"),
    ("B", 8.00,  18.70, 4.60, None,         None,        "2 - Message de bienvenue personnalise"),
    ("C", 18.70, 19.30, 0.90, BTN_SAVE,     SZ_SAVE,     None),
    ("D", 19.30, 23.60, 3.50, None,         None,        "Configuration enregistree"),
    ("E", 23.60, 24.00, 0.70, BTN_AVATAR,   SZ_AVATAR,   None),
    ("F", 24.00, 25.60, 2.60, None,         None,        "3 - Marketplace de prompts"),
    ("G", 25.60, 26.00, 0.70, BTN_MKT_ITEM, SZ_MKT_ITEM, None),
    ("H", 27.00, 35.60, 4.60, None,         None,        "4 - Filtrez et copiez un prompt"),
    ("I", 35.60, 36.00, 0.70, BTN_COPY,     SZ_COPY,     None),
    ("K", 39.50, 44.50, 4.30, None,         None,        "5 - Collez le prompt dans Claude"),
    ("L", 46.70, 47.10, 0.70, BTN_SEND,     SZ_SEND,     None),
    ("M", 47.10, 56.00, 5.80, None,         None,        "Claude orchestre vos outils FoodEatUp"),
]
INTRO_D, OUTRO_D = 4.90, 6.20

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

def card(img, out, secs, zoom_in=True):
    z0, z1 = (1.0, 1.09) if zoom_in else (1.09, 1.0)
    frames = int(secs * FPS)
    zexpr = f"{z0}+({z1}-{z0})*on/{frames}"
    vf = (f"[0:v]scale={W}:{H}:force_original_aspect_ratio=increase,crop={W}:{H},"
          f"boxblur=20:2,eq=brightness=-0.06[bg];"
          f"[0:v]scale={W}:{H}:force_original_aspect_ratio=decrease[fg];"
          f"[bg][fg]overlay=(W-w)/2:(H-h)/2,scale={W*2}:{H*2},"
          f"zoompan=z='{zexpr}':x='iw/2-(iw/zoom/2)':y='ih/2-(ih/zoom/2)'"
          f":d=1:s={W}x{H}:fps={FPS},"
          f"fade=t=in:st=0:d=0.4,fade=t=out:st={secs-0.4:.3f}:d=0.4,format=yuv420p")
    run(["ffmpeg","-y","-v","error","-loop","1","-t",str(secs),"-i",img,
         "-filter_complex",vf,"-r",str(FPS),
         "-c:v","libx264","-preset","medium","-crf","18",out])

def build_silent(outro_d):
    card(f"{ROOT}/assets/intro.jpg", f"{SEG}/intro.mp4", INTRO_D, zoom_in=True)
    card(f"{ROOT}/assets/outro.jpg", f"{SEG}/outro.mp4", outro_d, zoom_in=False)

    parts = [f"{SEG}/intro.mp4"]
    for name, s, e, target, btn, sz, cap in segs:
        parts.append(encode_seg(name, s, e, target, btn, sz, cap))
    parts.append(f"{SEG}/outro.mp4")

    trans = ["fade",       # intro -> A
             "fade",       # A -> B (continuous: same page, scroll)
             "fade",       # B -> C (continuous: click Enregistrer)
             "fade",       # C -> D (continuous: toast appears)
             "slideleft",  # D -> E (cut: scrolled to top, click avatar)
             "fade",       # E -> F (continuous: menu opens)
             "fade",       # F -> G (continuous: click Marketplace de prompts)
             "slideleft",  # G -> H (cut: Marketplace page loads)
             "fade",       # H -> I (continuous: click copy icon)
             "slideleft",  # I -> K (cut: switch to Claude, prompt pasted)
             "fade",       # K -> L (continuous: click send)
             "slideleft",  # L -> M (cut: Claude starts answering)
             "fade"]       # M -> outro
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
labels_order = ["intro"] + [s[0] for s in segs] + ["outro"]
S = dict(zip(labels_order, starts))
OUTRO_START = S["outro"]

GAP = 0.22
anchor = {
    "N0": 0.30,                 # intro hook
    "N1": S["A"] + 0.15,        # voix / langue / numero
    "N2": S["B"] + 0.15,        # message d'accueil
    "N3": S["C"] + 0.05,        # clic Enregistrer -> confirme
    "N4": S["E"] + 0.05,        # ouvre profil -> Marketplace de prompts
    "N5": S["H"] + 0.15,        # filtre + copie le prompt
    "N6": S["K"] + 0.15,        # colle dans Claude -> envoie
    "N7": S["M"] + 0.20,        # Claude orchestre (benefice)
    "N8": OUTRO_START + 0.35,   # CTA
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
FINAL = f"{ROOT}/out/foodeatup-caroline-voix-tuto-v1.mp4"
run(["ffmpeg","-y","-v","error","-i",silent] + inputs +
    ["-filter_complex",";".join(filters),"-map","0:v","-map","[voa]",
     "-c:v","copy","-c:a","aac","-b:a","192k","-ar","48000","-ac","2",
     "-movflags","+faststart","-t",f"{total:.3f}",FINAL])
print(f"DONE: {FINAL}  {dur(FINAL):.2f}s")
