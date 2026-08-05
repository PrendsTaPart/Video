#!/usr/bin/env python3
# FoodEatUp "Synchro Google Avis" tutorial (module marketing-fidelite, #02
# "Synchro Google Avis clients" du catalogue 157 tutoriels).
# No Claude-prompt sequence: connecter/synchroniser Google Avis est un flux
# OAuth (page Avis clients -> Google -> retour FoodEatUp), aucun outil
# mcp__FoodEatUp__* ne correspond a cette action precise (list_reviews /
# reply_review / moderate_review gerent des avis deja synchronises, pas la
# connexion du compte) -- regle FOODEATUP-TUTORIELS-WORKFLOW.md : pas de
# prompt invente.
# Meme moteur que le reste de la serie : pas de clip avatar, voix ElevenLabs
# de bout en bout, vitesse via setpts (jamais zoompan sur une vraie video),
# xfade a chaque raccord, format force en yuv420p en sortie de chaine, banniere
# en 2 drawtext (box=1) -- pas de drawbox anime, silencieusement ignore par
# cet ffmpeg (6.1.1). 48kHz stereo AAC, +faststart.
#
# Rush source : 48.77s. Deux coupes volontaires : 20.6->34.3 (detour menu
# hamburger involontaire du screen recording, sans valeur pedagogique) et
# 39.6->42.5 ("Server Error" au clic Synchroniser -- artefact du compte de
# demo sans vraie fiche Google Business connectee, pas le comportement reel
# a montrer).
import subprocess, os

ROOT = "/home/user/Video/videos/foodeatup-avis-google-tuto"
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

# Coordonnees mesurees sur les frames extraites (work/frames/), espace source
# 1920x828. Attention : la page est scrollee differemment a chaque instant
# (163px plus bas au moment du clic Synchroniser qu'au clic Lien de depot) --
# mesurer sur la frame exacte du clic, pas sur une frame voisine (meme piege
# que documente dans FOODEATUP-TUTORIELS-WORKFLOW.md).
BTN_CONNECT = (1642, 328); SZ_CONNECT = (246, 48)   # "Connecter Google" (t=5.1)
BTN_SYNC    = (1662, 165); SZ_SYNC    = (178, 45)   # "Synchroniser" (t=38.9, page scrollee)
BTN_LIEN    = (1055, 323); SZ_LIEN    = (202, 47)   # "Lien de depot" (t=43.0)

# (name, src_start, src_end, target_out_duration, button, btn_size, caption)
# Targets sized on the VO durations (vo/*.mp3), not the other way round -- see
# the rule in FOODEATUP-TUTORIELS-WORKFLOW.md. E (click Synchroniser) is
# deliberately slowed well below its raw 1.6s: N4 is a full sentence and needs
# room to land before F's own visual (Lien de depot) starts, or the narration
# would describe one action while a different one plays on screen.
segs = [
    ("A", 0.20,  5.30,  3.30, None,        None,       "1 - Avis clients"),
    ("B", 5.30,  5.65,  0.95, BTN_CONNECT, SZ_CONNECT, None),
    ("C", 7.00,  20.60, 5.30, None,        None,       "2 - Compte Google"),
    ("D", 34.30, 38.00, 4.30, None,        None,       "Google connecte"),
    ("E", 38.00, 39.60, 4.00, BTN_SYNC,    SZ_SYNC,    None),
    ("F", 42.50, 43.60, 1.60, BTN_LIEN,    SZ_LIEN,    "Lien copie"),
    ("G", 43.60, 48.60, 6.50, None,        None,       None),
]
INTRO_D, OUTRO_D = 4.60, 6.20

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
    for name, s, e, target, btn, sz, cap in segs:
        parts.append(encode_seg(name, s, e, target, btn, sz, cap))
    parts.append(f"{SEG}/outro.mp4")

    trans = ["fade",      # intro -> A
             "fade",      # A -> B (continuous: click Connecter Google)
             "slideleft", # B -> C (cut into the Google account flow)
             "slideleft", # C -> D (cut: coupe du detour menu, retour connecte)
             "fade",      # D -> E (continuous: click Synchroniser)
             "slideleft", # E -> F (coupe de l'erreur demo, clic Lien de depot)
             "fade",      # F -> G (continuous: toast copie -> page calme)
             "fade"]      # G -> outro
    assert len(trans) == len(parts) - 1
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
    "N0": 0.30,
    "N1": S["A"] + 0.20,   # depuis Avis clients, cliquez sur Connecter Google
    "N2": S["C"] + 0.20,   # choisissez votre compte, autorisez l'acces
    "N3": S["D"] + 0.15,   # retour, badge Google connecte
    "N4": S["E"] + 0.15,   # clic Synchroniser
    "N5": S["F"] + 0.10,   # lien de depot copie
    "N6": S["G"] + 0.10,   # benefice : tous les avis unifies
    "N7": OUTRO_START + 0.35,  # CTA
}
assert set(anchor) == set(f"N{i}" for i in range(8))
keys = [f"N{i}" for i in range(8)]
off, prev_end = {}, -GAP
for k in keys:
    o = max(anchor[k], prev_end + GAP); off[k] = o
    prev_end = o + dur(f"{ROOT}/vo/{k}.mp3")
print("offsets:", {k: round(v, 2) for k, v in off.items()}, "voice_end:", round(prev_end, 2))
drift = {k: round(off[k] - anchor[k], 2) for k in keys if off[k] - anchor[k] > 0.05}
print("drift vs anchors:", drift if drift else "none -- all lines on their anchors")
print("stage starts:", {k: round(v, 2) for k, v in S.items()})

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
FINAL = f"{ROOT}/out/foodeatup-avis-google-tuto-v1.mp4"
run(["ffmpeg","-y","-v","error","-i",silent] + inputs +
    ["-filter_complex",";".join(filters),"-map","0:v","-map","[voa]",
     "-c:v","copy","-c:a","aac","-b:a","192k","-ar","48000","-ac","2",
     "-movflags","+faststart","-t",f"{total:.3f}",FINAL])
print(f"DONE: {FINAL}  {dur(FINAL):.2f}s")
