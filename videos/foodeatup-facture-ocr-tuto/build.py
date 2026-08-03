#!/usr/bin/env python3
# FoodEatUp "Scanner sa facture - OCR & mise a jour des prix automatique"
# tutorial (module StockVision AI / Comptabilite). Same engine as every
# FoodEatUp tuto (see videos/FOODEATUP-TUTORIELS-WORKFLOW.md): setpts speed
# change (never zoompan on real footage), zoom-punch crop on button clicks,
# xfade on every cut, forced back to yuv420p at the end of the chain. 48kHz
# stereo AAC, +faststart.
#
# Rush (48.7s): "Gestion des livraisons" -> "Voir le detail" d'une livraison
# livree -> detail (statut, fournisseur, prix) -> section Facture ("Aucune
# facture...") -> "+ Ajouter une facture" -> modale "Importer une facture" ->
# upload PDF -> OCR "Analyse en cours" (15% -> 17% -> 39% -> 100%) -> page
# "Validation de la facture" (fournisseur detecte, n de facture, prix, case
# MAJ PRIX) -> selection Fournisseur ("La Comtesse #6") et Livraison associee
# ("DEL-D-42 - soulayma") -> "Valider et enregistrer" -> modale "Facture
# validee ! 1 prix mis a jour, depense enregistree" -> "Voir la depense" ->
# fiche Depense EXP-A5171F (resume, fournisseur, produits achetes, note
# "Importe automatiquement depuis la facture").
import subprocess, os, sys

ROOT = "/home/user/Video/videos/foodeatup-facture-ocr-tuto"
SRC  = f"{ROOT}/assets/screen.mp4"
W, H, FPS = 1920, 828, 25
SEG = f"{ROOT}/work/seg"
FONT = "/usr/share/fonts/truetype/liberation/LiberationSans-Bold.ttf"
BLUE, ORANGE = "0x1B6DF3", "0xF7941D"
XF = 0.28
os.makedirs(SEG, exist_ok=True)

sys.path.insert(0, "/home/user/Video/videos/_shared")
from claude_prompt_sequence import (
    render_claude_stage1_png, render_claude_stage2_png, render_claude_stage3_png,
)

CLAUDE_PROMPT = (
    "Voici la photo de ma facture fournisseur [numero de facture]. Mets a jour "
    "les prix de mes produits et enregistre la depense correspondante, pour "
    "mon etablissement FoodEatUp (ID [ID etablissement])."
)

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
            f"drawtext=fontfile={FONT}:text='{text}':fontsize=29:fontcolor=white"
            f":x='({x})+34':y={y+16}")

# Coordonnees mesurees sur les frames extraites du rush (natif 1920x828).
BTN_VOIR_DETAIL     = (372, 608);  SZ_VOIR_DETAIL     = (300, 60)   # "Voir le detail" (1ere carte)
BTN_AJOUTER_FACTURE = (1586, 497); SZ_AJOUTER_FACTURE = (270, 50)   # "+ Ajouter une facture"
BTN_VALIDER         = (1537, 492); SZ_VALIDER         = (360, 50)   # "Valider et enregistrer"
BTN_VOIR_DEPENSE    = (830, 579);  SZ_VOIR_DEPENSE    = (240, 55)   # "Voir la depense" (modale succes)

# (name, src_start, src_end, target_out_duration, click_time_or_None, button, btn_size, caption)
segs = [
    ("A", 0.20,  3.70,  4.40, None,  None,                None,                "1 - Vos livraisons recues"),
    ("B", 7.00,  8.55,  1.50, None,  None,                None,                None),
    ("C", 8.55,  8.85,  0.80, 8.70,  BTN_VOIR_DETAIL,      SZ_VOIR_DETAIL,      None),
    ("D", 8.90,  11.70, 4.00, None,  None,                None,                "2 - Ouvrez le detail et ajoutez la facture"),
    ("E", 11.70, 12.00, 0.80, 11.85, BTN_AJOUTER_FACTURE,  SZ_AJOUTER_FACTURE,  None),
    ("F", 12.00, 13.00, 3.60, None,  None,                None,                "3 - Deposez le PDF ou la photo"),
    ("G", 15.80, 21.90, 6.00, None,  None,                None,                "4 - Analyse OCR et extraction des donnees"),
    ("H", 22.50, 26.80, 5.60, None,  None,                None,                "5 - Fournisseur, facture et prix detectes"),
    ("I", 27.00, 33.60, 6.00, None,  None,                None,                "6 - Fournisseur et livraison lies"),
    ("J", 36.60, 36.90, 0.80, 36.75, BTN_VALIDER,          SZ_VALIDER,          None),
    ("K", 37.50, 40.60, 5.20, None,  None,                None,                None),
    ("L", 40.60, 40.90, 0.80, 40.75, BTN_VOIR_DEPENSE,     SZ_VOIR_DEPENSE,     None),
    ("M", 41.50, 48.70, 5.60, None,  None,                None,                "7 - La depense est creee automatiquement"),
]
INTRO_D, OUTRO_D = 5.80, 6.00

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

CLAUDE_D = [3.00, 1.40, 4.20]  # reveal, copie, chatbot mockup

def build_silent(outro_d, claude_d):
    card(f"{ROOT}/assets/intro.jpg", f"{SEG}/intro.mp4", INTRO_D, zoom_in=True)
    card(f"{ROOT}/assets/outro.jpg", f"{SEG}/outro.mp4", outro_d, zoom_in=False)

    png_dir = f"{ROOT}/work/png"; os.makedirs(png_dir, exist_ok=True)
    render_claude_stage1_png(f"{png_dir}/claude1.png", W, H, CLAUDE_PROMPT)
    render_claude_stage2_png(f"{png_dir}/claude2.png", W, H, CLAUDE_PROMPT)
    render_claude_stage3_png(f"{png_dir}/claude3.png", W, H, CLAUDE_PROMPT,
        response="Facture analysee, prix mis a jour et depense enregistree.")
    for i, d in enumerate(claude_d, start=1):
        card(f"{png_dir}/claude{i}.png", f"{SEG}/claude{i}.mp4", d, zoom_in=True, fade=False)

    parts = [f"{SEG}/intro.mp4"]
    for name, s, e, target, ck, btn, sz, cap in segs:
        parts.append(encode_seg(name, s, e, target, btn, sz, cap))
    parts += [f"{SEG}/claude1.mp4", f"{SEG}/claude2.mp4", f"{SEG}/claude3.mp4"]
    parts.append(f"{SEG}/outro.mp4")

    labels_order = ["intro"] + [s[0] for s in segs] + ["claude1", "claude2", "claude3", "outro"]
    trans = []
    for i in range(len(labels_order) - 1):
        a, b = labels_order[i], labels_order[i + 1]
        if {a, b} <= {"claude1", "claude2", "claude3"} or (a in ("M",) and b == "claude1") \
           or (a == "claude3" and b == "outro"):
            trans.append("slideleft")
        else:
            trans.append("fade")

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
    return silent, starts, total, labels_order

silent, starts, total, labels_order = build_silent(OUTRO_D, CLAUDE_D)
print(f"SILENT TOTAL: {dur(silent):.2f}s")
S = dict(zip(labels_order, starts))
OUTRO_START = S["outro"]

GAP = 0.22
anchor = {
    "N0": 0.30,                    # intro hook
    "N1": S["A"] + 0.30,           # vos livraisons recues
    "N2": S["D"] + 0.20,           # detail + ajouter une facture
    "N3": S["F"] + 0.20,           # deposez le PDF / photo
    "N4": S["G"] + 0.20,           # OCR analyse
    "N5": S["H"] + 0.20,           # fournisseur / facture / prix detectes
    "N6": S["I"] + 0.20,           # fournisseur + livraison lies
    "N7": S["K"] + 0.20,           # facture validee, prix + depense
    "N8": S["M"] + 0.20,           # depense creee automatiquement
    "N9": S["claude1"] + 0.25,     # prompt Claude (reveal)
    "N10": S["claude3"] + 0.25,    # chatbot mockup (resultat)
    "N11": OUTRO_START + 0.35,     # CTA
}
keys = ["N0","N1","N2","N3","N4","N5","N6","N7","N8","N9","N10","N11"]
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
    silent, starts, total, labels_order = build_silent(needed, CLAUDE_D)
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
FINAL = f"{ROOT}/out/foodeatup-facture-ocr-tuto-v1.mp4"
run(["ffmpeg","-y","-v","error","-i",silent] + inputs +
    ["-filter_complex",";".join(filters),"-map","0:v","-map","[voa]",
     "-c:v","copy","-c:a","aac","-b:a","192k","-ar","48000","-ac","2",
     "-movflags","+faststart","-t",f"{total:.3f}",FINAL])
print(f"DONE: {FINAL}  {dur(FINAL):.2f}s")
