#!/usr/bin/env python3
# FoodEatUp "Commander ses cartes NFC pour le badge" tutorial (module Equipe
# & Planning, catalogue #10). Same engine as every FoodEatUp tuto (see
# videos/FOODEATUP-TUTORIELS-WORKFLOW.md): setpts speed change (never zoompan
# on real footage), zoom-punch crop on the key clicks, xfade on every cut,
# forced back to yuv420p at the end of the chain. 48kHz stereo AAC,
# +faststart.
#
# Rush is a real screen recording (1920x828 @25fps, no browser chrome to
# crop) of the QR/pointage config page: QR code actif -> scroll to security
# settings + "Acces des employes" (PIN deja defini, badge NFC optionnel en
# plus) -> section "Badges NFC & cartes marketing" (cartes PVC + puce
# imprimees, 2.5EUR/carte) -> "Generer badge" cree un identifiant unique pour
# un employe -> "Commander les badges NFC" ouvre une modale de selection
# d'employes avec calcul du prix -> "Confirmer la commande" enregistre la
# commande (mode local, envoi a l'imprimeur Printags des que la cle API est
# activee). Aucun outil mcp__FoodEatUp__* ne couvre la commande de cartes
# physiques -> pas de sequence "Utiliser avec Claude" (meme raisonnement que
# foodeatup-borne-tuto/foodeatup-jarvis-tuto : action materielle/logistique,
# pas un geste d'administration API).
import subprocess, os, sys

ROOT = "/home/user/Video/videos/foodeatup-nfc-tuto"
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

# Coordinates measured on the extracted frames (1920x828, no crop needed).
# No apostrophe in any caption below (bug hit on foodeatup-ingredients-tuto --
# see FOODEATUP-TUTORIELS-WORKFLOW.md).
BTN_GENERER   = (1678, 199);  SZ_GENERER   = (153, 41)  # "Generer badge" (Alice)
BTN_COMMANDER = (1568, 614);  SZ_COMMANDER = (379, 46)  # "Commander les badges NFC"
BTN_CONFIRMER = (1021, 634);  SZ_CONFIRMER = (297, 52)  # "Confirmer la commande"

# (name, src_start, src_end, target_out_duration, click_time, button, btn_size, caption)
segs = [
    ("A", 0.20,  1.00,  3.00, None,  None,          None,          "1 · Module Equipe : pointage"),
    ("B", 6.00,  8.00,  7.20, None,  None,          None,          "Chaque employe peut avoir son badge"),
    ("C", 9.00,  9.60,  8.20, None,  None,          None,          "2 · Badges NFC & cartes marketing"),
    ("D", 9.90,  10.20, 0.90, 10.05, BTN_GENERER,   SZ_GENERER,    None),
    ("E", 12.00, 13.00, 5.60, None,  None,          None,          "Identifiant unique cree"),
    ("F", 13.80, 14.10, 0.90, 13.95, BTN_COMMANDER, SZ_COMMANDER,  None),
    ("G", 16.00, 19.50, 6.50, None,  None,          None,          "3 · Commander les badges"),
    ("H", 19.60, 19.90, 0.90, 19.75, BTN_CONFIRMER, SZ_CONFIRMER,  None),
    ("I", 24.00, 27.00, 6.50, None,  None,          None,          "Commande enregistree"),
]
INTRO_D, OUTRO_D = 7.50, 6.20

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

def build_silent(outro_d):
    card(f"{ROOT}/assets/intro.jpg", f"{SEG}/intro.mp4", INTRO_D, zoom_in=True)
    card(f"{ROOT}/assets/outro.jpg", f"{SEG}/outro.mp4", outro_d, zoom_in=False)
    parts = [f"{SEG}/intro.mp4"]
    for name, s, e, target, ck, btn, sz, cap in segs:
        parts.append(encode_seg(name, s, e, target, btn, sz, cap))
    parts.append(f"{SEG}/outro.mp4")

    trans = ["fade",       # intro -> A
             "slideleft",  # A -> B (cut: scrolled to Acces des employes)
             "fade",       # B -> C (continuous: scroll to Badges NFC)
             "fade",       # C -> D (continuous: click Generer badge)
             "slideleft",  # D -> E (cut, badge genere)
             "fade",       # E -> F (continuous: click Commander les badges)
             "slideleft",  # F -> G (cut, modale de commande)
             "fade",       # G -> H (continuous: click Confirmer)
             "slideleft",  # H -> I (cut, commande enregistree)
             "fade"]       # I -> outro
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
    "N0": 0.30,                  # intro hook
    "N1": S["B"] + 0.30,         # chaque employe peut avoir son badge
    "N2": S["C"] + 0.20,         # section badges nfc, tarif
    "N3": S["E"] + 0.20,         # generer badge -> identifiant unique
    "N4": S["G"] + 0.20,         # commander : selection + prix
    "N5": S["I"] + 0.20,         # commande enregistree
    "N6": OUTRO_START + 0.35,    # CTA
}
keys = [f"N{i}" for i in range(7)]
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
FINAL = f"{ROOT}/out/foodeatup-nfc-tuto-v1.mp4"
run(["ffmpeg","-y","-v","error","-i",silent] + inputs +
    ["-filter_complex",";".join(filters),"-map","0:v","-map","[voa]",
     "-c:v","copy","-c:a","aac","-b:a","192k","-ar","48000","-ac","2",
     "-movflags","+faststart","-t",f"{total:.3f}",FINAL])
print(f"DONE: {FINAL}  {dur(FINAL):.2f}s")
