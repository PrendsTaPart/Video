#!/usr/bin/env python3
# FoodEatUp "Changer les statuts d'un devis" tutorial (module Comptabilite &
# Achats, 2e video du module). Same engine as every FoodEatUp tuto (see
# videos/FOODEATUP-TUTORIELS-WORKFLOW.md): setpts speed change (never zoompan on
# real footage), zoom-punch crop on button clicks, xfade on every cut, forced
# back to yuv420p at the end of the chain. 48kHz stereo AAC, +faststart.
#
# Rush (38.1s): "Devis" (onglet Facturation) -> menu actions sur un devis "En
# attente" -> Visualiser -> page detail (infos, articles, historique, actions
# rapides) -> "Telechargements et options" -> "Marquer comme accepte" ->
# confirmation "Marquer ce devis comme accepte ?" -> OK -> toast succes ->
# statut passe a "Signe", nouvelles actions (Telecharger PDF / Convertir en
# facture) -> retour a la liste via le fil d'Ariane "Facturation" -> le devis
# apparait bien "Signe" dans la liste (8 -> 7 devis en attente).
#
# Entre le retour a la liste et son affichage final, le rush contient un
# rechargement de page (flash blanc + un toast "Devis cree..." sans rapport,
# reste d'une notification precedente) avant que le statut mis a jour ne
# s'affiche vraiment. Ce segment est saute au montage (segments N -> O ne
# sont pas contigus dans la source) pour ne montrer que l'etat correct.
import subprocess, os

ROOT = "/home/user/Video/videos/foodeatup-devis-statuts-tuto"
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

# Coordinates measured on the extracted frames (native 1920x828), same method
# as the rest of the series. No apostrophe in any caption below.
BTN_MENU_ICON   = (1655, 165); SZ_MENU_ICON   = (55, 60)    # icone menu actions (liste)
BTN_VISUALISER  = (1510, 210); SZ_VISUALISER  = (340, 50)   # "Visualiser" (menu deroulant)
BTN_TELEOPTIONS = (1620, 290); SZ_TELEOPTIONS = (365, 55)   # "Telechargements et options"
BTN_ACCEPTE     = (1520, 160); SZ_ACCEPTE     = (355, 45)   # "Marquer comme accepte"
BTN_OK_MODAL    = (1095, 105); SZ_OK_MODAL    = (115, 60)   # "OK" (modale de confirmation)
BTN_OK_TOAST    = (1225, 100); SZ_OK_TOAST    = (125, 60)   # "OK" (toast succes)
BTN_BREADCRUMB  = (160,  268); SZ_BREADCRUMB  = (170, 50)   # "Facturation" (fil d'Ariane)

# (name, src_start, src_end, target_out_duration, click_time_or_None, button, btn_size, caption)
segs = [
    ("A", 0.20,  5.00,  5.30, None,  None,            None,            "1 - Vos devis et leur statut"),
    ("B", 4.85,  5.15,  0.80, 5.00,  BTN_MENU_ICON,    SZ_MENU_ICON,    None),
    ("C", 5.15,  6.55,  3.30, None,  None,            None,            "Ouvrez le menu Actions"),
    ("D", 6.60,  6.90,  0.80, 6.75,  BTN_VISUALISER,   SZ_VISUALISER,   None),
    ("E", 7.05,  11.15, 4.70, None,  None,            None,            "2 - Consultez le devis"),
    ("F", 11.70, 12.00, 0.80, 11.85, BTN_TELEOPTIONS,  SZ_TELEOPTIONS,  None),
    ("G", 12.05, 13.35, 3.60, None,  None,            None,            "3 - Choisissez le nouveau statut"),
    ("H", 14.25, 14.55, 0.80, 14.40, BTN_ACCEPTE,      SZ_ACCEPTE,      None),
    ("I", 14.60, 15.50, 2.60, None,  None,            None,            "Confirmez le changement"),
    ("J", 15.55, 15.85, 0.80, 15.70, BTN_OK_MODAL,     SZ_OK_MODAL,     None),
    ("K", 16.30, 17.75, 2.00, None,  None,            None,            "Statut mis a jour"),
    ("L", 17.85, 18.15, 0.80, 18.00, BTN_OK_TOAST,     SZ_OK_TOAST,     None),
    ("M", 18.40, 22.10, 3.70, None,  None,            None,            "4 - Nouvelles actions disponibles"),
    ("N", 22.20, 22.50, 0.80, 22.35, BTN_BREADCRUMB,   SZ_BREADCRUMB,   None),
    ("O", 34.00, 37.90, 3.60, None,  None,            None,            "Statut enregistre dans la liste"),
]
INTRO_D, OUTRO_D = 4.70, 6.20

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
             "fade",       # A -> B (continuous: clic menu actions)
             "fade",       # B -> C (continuous: menu deroulant ouvert)
             "fade",       # C -> D (continuous: clic Visualiser)
             "fade",       # D -> E (continuous: page detail du devis)
             "fade",       # E -> F (continuous: clic Telechargements et options)
             "fade",       # F -> G (continuous: menu statuts ouvert)
             "fade",       # G -> H (continuous: clic Marquer comme accepte)
             "fade",       # H -> I (continuous: modale de confirmation)
             "fade",       # I -> J (continuous: clic OK)
             "fade",       # J -> K (continuous: toast de succes)
             "fade",       # K -> L (continuous: clic OK du toast)
             "fade",       # L -> M (continuous: statut Signe + nouvelles actions)
             "fade",       # M -> N (continuous: clic fil d'Ariane Facturation)
             "fade",       # N -> O (coupe : retour a la liste, statut enregistre)
             "fade"]       # O -> outro
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
    "N1": S["A"] + 0.30,         # vos devis et leur statut
    "N2": S["C"] + 0.20,         # menu actions / visualiser
    "N3": S["E"] + 0.20,         # consultez le devis
    "N4": S["F"] + 0.20,         # telechargements et options
    "N5": S["H"] + 0.20,         # marquer accepte / confirmation / OK
    "N6": S["K"] + 0.20,         # statut mis a jour (toast)
    "N7": S["M"] + 0.20,         # signe, nouvelles actions
    "N8": S["N"] + 0.20,         # retour liste, statut enregistre
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
FINAL = f"{ROOT}/out/foodeatup-devis-statuts-tuto-v1.mp4"
run(["ffmpeg","-y","-v","error","-i",silent] + inputs +
    ["-filter_complex",";".join(filters),"-map","0:v","-map","[voa]",
     "-c:v","copy","-c:a","aac","-b:a","192k","-ar","48000","-ac","2",
     "-movflags","+faststart","-t",f"{total:.3f}",FINAL])
print(f"DONE: {FINAL}  {dur(FINAL):.2f}s")
