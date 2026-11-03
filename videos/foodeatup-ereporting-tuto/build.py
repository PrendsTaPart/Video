#!/usr/bin/env python3
# FoodEatUp "Declarer son e-reporting (comptabilite)" tutorial (module
# Comptabilite & Achats, catalogue #9). Same engine as every FoodEatUp tuto
# (see videos/FOODEATUP-TUTORIELS-WORKFLOW.md): setpts speed change (never
# zoompan on real footage), zoom-punch crop on the key clicks, xfade on
# every cut, forced back to yuv420p at the end of the chain. 48kHz stereo
# AAC, +faststart.
#
# Rush is a real screen recording (1920x828 @25fps, no browser chrome to
# crop) of the module Comptabilite > Facture : onglet E-Reporting (stats
# Declarees/En attente/En retard, prochaine echeance, tableau par periode
# avec Total HT/TVA/Statut) -> menu Action d'une periode en retard ->
# "Declarer la periode" -> stats mises a jour -> retour aux Factures (badge
# Conformite 2026 mis a jour) -> detail d'une facture -> menu
# "Telechargements et options" (PDF Factur-X, XML CII, Archiver legalement,
# PDF standard, UBL) -> onglet Archives legales (Hash SHA-256, date
# d'archivage, expiration a 10 ans) -> "Verifier l'integrite" -> modale de
# confirmation "Facture integre". Aucun outil mcp__FoodEatUp__* ne couvre la
# declaration e-reporting, la generation Factur-X, l'archivage legal ou la
# verification d'integrite (fonctionnalites de conformite reglementaire,
# pas des endpoints API) -> pas de sequence "Utiliser avec Claude".
import subprocess, os, sys

ROOT = "/home/user/Video/videos/foodeatup-ereporting-tuto"
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
BTN_EREPORTING = (407, 446);   SZ_EREPORTING = (269, 48)  # onglet "E-Reporting"
BTN_DECLARER   = (1517, 612);  SZ_DECLARER   = (300, 36)  # "Declarer la periode"
BTN_TELECH     = (1614, 354);  SZ_TELECH     = (360, 48)  # "Telechargements et options"
BTN_ARCHIVES   = (683, 447);   SZ_ARCHIVES   = (220, 50)  # onglet "Archives legales"
BTN_VERIFIER   = (1529, 408);  SZ_VERIFIER   = (249, 26)  # "Verifier l integrite"

# (name, src_start, src_end, target_out_duration, click_time, button, btn_size, caption)
segs = [
    ("A", 0.20,  2.00,  3.00, None,  None,           None,           "1 · Module Comptabilite"),
    ("B", 2.50,  2.80,  0.90, 2.65,  BTN_EREPORTING,  SZ_EREPORTING,  None),
    ("C", 6.00,  9.00,  7.50, None,  None,           None,           "2 · E-Reporting par periode"),
    ("D", 9.30,  9.60,  0.90, 9.45,  BTN_DECLARER,    SZ_DECLARER,    None),
    ("E", 10.00, 12.50, 5.50, None,  None,           None,           "Periode declaree"),
    ("F", 21.00, 24.00, 6.00, None,  None,           None,           "3 · Facture-X et XML"),
    ("G", 26.30, 26.60, 0.90, 26.45, BTN_TELECH,      SZ_TELECH,      None),
    ("H", 27.00, 30.00, 6.50, None,  None,           None,           "Telechargements et options"),
    ("I", 36.00, 39.00, 4.00, None,  None,           None,           "Conformite 2026 a jour"),
    ("J", 43.50, 43.80, 0.90, 43.65, BTN_ARCHIVES,    SZ_ARCHIVES,    None),
    ("K", 45.00, 46.00, 6.00, None,  None,           None,           "4 · Archives legales"),
    ("L", 46.30, 46.60, 0.90, 46.45, BTN_VERIFIER,    SZ_VERIFIER,    None),
    ("M", 48.00, 50.50, 5.00, None,  None,           None,           "Verification d integrite"),
]
INTRO_D, OUTRO_D = 6.50, 6.20

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
             "fade",       # A -> B (continuous: click E-Reporting)
             "slideleft",  # B -> C (cut, onglet E-Reporting)
             "fade",       # C -> D (continuous: click Declarer la periode)
             "slideleft",  # D -> E (cut, periode declaree)
             "slideleft",  # E -> F (cut, detail d'une facture)
             "fade",       # F -> G (continuous: click Telechargements)
             "slideleft",  # G -> H (cut, menu options ouvert)
             "slideleft",  # H -> I (cut, retour a la liste, Factur-X genere)
             "fade",       # I -> J (continuous: click Archives legales)
             "slideleft",  # J -> K (cut, onglet Archives legales)
             "fade",       # K -> L (continuous: click Verifier l integrite)
             "slideleft",  # L -> M (cut, modale de verification)
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
    "N0": 0.30,                  # intro hook
    "N1": S["C"] + 0.30,         # e-reporting par periode
    "N2": S["E"] + 0.20,         # periode declaree
    "N3": S["F"] + 0.20,         # facture-x, xml
    "N4": S["K"] + 0.20,         # archives legales, hash
    "N5": S["M"] + 0.20,         # verification d integrite
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
FINAL = f"{ROOT}/out/foodeatup-ereporting-tuto-v1.mp4"
run(["ffmpeg","-y","-v","error","-i",silent] + inputs +
    ["-filter_complex",";".join(filters),"-map","0:v","-map","[voa]",
     "-c:v","copy","-c:a","aac","-b:a","192k","-ar","48000","-ac","2",
     "-movflags","+faststart","-t",f"{total:.3f}",FINAL])
print(f"DONE: {FINAL}  {dur(FINAL):.2f}s")
