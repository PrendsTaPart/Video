#!/usr/bin/env python3
# FoodEatUp "Regler ses horaires par employe" tutorial (module Equipe &
# Planning, catalogue #4). Same engine as every FoodEatUp tuto (see
# videos/FOODEATUP-TUTORIELS-WORKFLOW.md): setpts speed change (never zoompan
# on real footage), zoom-punch crop on the key clicks, xfade on every cut,
# forced back to yuv420p at the end of the chain. 48kHz stereo AAC,
# +faststart.
#
# Rush is a real screen recording (1920x828 @25fps, no browser chrome to
# crop) of the manager-side employee list: card "Alice Charbit" -> "Voir"
# opens her detail panel (Personnel tab, "Horaires de travail": Lundi
# 08:00-17:00, 1h repos) -> "Modifier" opens the edit modal (step 2, horaires)
# -> "+ Ajouter une plage horaire" adds a second slot -> the new slot's jour
# is switched to Mardi and its hours adjusted to match Lundi (08:00-17:00)
# -> "Sauvegarder" applies the new weekly schedule.
# mcp__FoodEatUp__update_employee_schedule replaces the full weekly schedule
# in one call -> "Utiliser avec Claude" sequence covers it (assigning hours
# from a photo of a paper planning, or adjusting hours for a slow/busy day).
import subprocess, os, sys
sys.path.insert(0, "/home/user/Video/videos/_shared")
from claude_prompt_sequence import (
    render_claude_stage1_png, render_claude_stage2_png, render_claude_stage3_png,
)

ROOT = "/home/user/Video/videos/foodeatup-horaires-tuto"
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
BTN_VOIR      = (392, 681);   SZ_VOIR      = (163, 53)  # "Voir" (carte Alice)
BTN_MODIF_H   = (1827, 620);  SZ_MODIF_H   = (106, 42)  # "Modifier" (Horaires de travail)
BTN_AJOUTER   = (799, 586);   SZ_AJOUTER   = (304, 26)  # "+ Ajouter une plage horaire"
BTN_SAUVEGARD = (1173, 736);  SZ_SAUVEGARD = (202, 49)  # "Sauvegarder"

# (name, src_start, src_end, target_out_duration, click_time, button, btn_size, caption)
segs = [
    ("A", 0.20,  2.00,  6.50, None, None,          None,          "1 · Fiche employe"),
    ("B", 3.30,  3.60,  0.90, 3.45, BTN_VOIR,      SZ_VOIR,       None),
    ("C", 4.00,  6.00,  6.00, None, None,          None,          "Horaires actuels"),
    ("D", 6.80,  7.10,  0.90, 6.95, BTN_MODIF_H,   SZ_MODIF_H,    None),
    ("E", 8.00,  9.30,  7.50, None, None,          None,          "2 · Modifier les horaires"),
    ("F", 9.30,  9.60,  0.90, 9.45, BTN_AJOUTER,   SZ_AJOUTER,    None),
    ("G", 11.00, 14.00, 7.00, None, None,          None,          "3 · Nouveau creneau (Mardi)"),
    ("H", 16.00, 22.00, 5.00, None, None,          None,          "Ajuster selon les besoins"),
    ("I", 25.50, 25.80, 0.90, 25.65, BTN_SAUVEGARD, SZ_SAUVEGARD, None),
    ("J", 26.50, 30.44, 5.50, None, None,          None,          "Planning sauvegarde"),
]
INTRO_D, OUTRO_D = 6.00, 6.20

CLAUDE_PROMPT = ("Voici en photo le planning papier de [prénom] [nom] pour la "
                  "semaine : configure ses horaires de travail dans FoodEatUp "
                  "exactement selon cette photo, pour mon établissement "
                  "FoodEatUp (ID [ID établissement]).")
CLAUDE_RESPONSE = "Bien sûr ! Je configure ses horaires selon la photo…"
CLAUDE_STAGE_D = [6.00, 3.00, 6.00]  # reveal, copied, chatbot mockup

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
             "fade",       # A -> B (continuous: click Voir)
             "slideleft",  # B -> C (cut, panel opens)
             "fade",       # C -> D (continuous: click Modifier)
             "slideleft",  # D -> E (cut into the modal)
             "fade",       # E -> F (continuous: click Ajouter une plage)
             "slideleft",  # F -> G (cut, nouveau creneau Mardi)
             "fade",       # G -> H (continuous: ajustement des heures)
             "fade",       # H -> I (continuous: click Sauvegarder)
             "slideleft",  # I -> J (cut, modal ferme)
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
    "N1": S["A"] + 0.30,         # fiche employe, horaires par jour
    "N2": S["C"] + 0.20,         # horaires actuels (lundi 8-17, 1h repos)
    "N3": S["E"] + 0.20,         # modifier: debut/fin/pause par jour
    "N4": S["G"] + 0.20,         # nouveau creneau (mardi, affluence)
    "N5": S["H"] + 0.20,         # ajuster les heures a tout moment
    "N6": S["J"] + 0.20,         # sauvegarder, planning applique
    "N7": S["claude1"] + 0.20,   # explains the prompt (reveal + copied)
    "N8": S["claude3"] + 0.20,   # paste into Claude -> instant result
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
FINAL = f"{ROOT}/out/foodeatup-horaires-tuto-v1.mp4"
run(["ffmpeg","-y","-v","error","-i",silent] + inputs +
    ["-filter_complex",";".join(filters),"-map","0:v","-map","[voa]",
     "-c:v","copy","-c:a","aac","-b:a","192k","-ar","48000","-ac","2",
     "-movflags","+faststart","-t",f"{total:.3f}",FINAL])
print(f"DONE: {FINAL}  {dur(FINAL):.2f}s")
