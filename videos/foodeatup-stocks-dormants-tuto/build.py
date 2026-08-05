#!/usr/bin/env python3
# FoodEatUp "Booster les stocks dormants" tutorial -- agent Iris, onglet
# Opportunites. Same engine as the rest of the series: setpts for speed
# (never zoompan on real footage -- freezes the image), fixed crop+scale
# zoom-punch on the single click, xfade on every cut forced back to
# yuv420p, 48kHz stereo AAC, +faststart. banner() uses drawtext's own box
# (NOT drawbox, which never evaluates its own timestamp on this ffmpeg
# build -- see FOODEATUP-TUTORIELS-WORKFLOW.md).
import subprocess, os, sys
sys.path.insert(0, "/home/user/Video/videos/_shared")
from claude_prompt_sequence import (
    render_claude_stage1_png, render_claude_stage2_png, render_claude_stage3_png,
)

ROOT = "/home/user/Video/videos/foodeatup-stocks-dormants-tuto"
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
    # Plate drawn with drawtext's own box=1, NOT drawbox: drawbox has no
    # timestamp variable on this ffmpeg build (its `t` is border thickness),
    # so an x-expression built on `t` collapses to a constant and the plate
    # never slides on screen. drawtext exposes t and its box follows the
    # text, so this gives a plate that actually animates. Two passes: an
    # orange one nudged left (peeks out as the accent bar), then blue on top.
    if not text: return None
    assert "'" not in text, f"apostrophe in banner text: {text}"
    tin, sl = 0.15, 0.32
    tout = max(tin + sl + 0.3, seg_dur - 0.55)
    a = f"min(1\\,max(0\\,(t-{tin})/{sl}))"
    b = f"min(1\\,max(0\\,(t-{tout})/{sl}))"
    x = f"-640+700*({a})-700*({b})"
    y = H - 92
    common = (f"fontfile={FONT}:text='{text}':fontsize=29:boxborderw=18:y={y}")
    return (f"drawtext={common}:fontcolor={ORANGE}@0.0:box=1:boxcolor={ORANGE}@0.98"
            f":x='({x})+34-14',"
            f"drawtext={common}:fontcolor=white:box=1:boxcolor={BLUE}@0.92"
            f":x='({x})+34'")

# Coordinates measured by colour-thresholding the actual frame at the click
# (see SCRIPT.md) -- bbox 1478,402 -> 1795,463, centre (1636,432).
BTN_REDETECT = (1636, 432); SZ_REDETECT = (317, 61)

# Targets sized on the *measured* ElevenLabs VO durations (vo/N0..N8.mp3),
# counting the xfade overlap each segment contributes (target - XF) to the
# timeline -- see the sizing note in FOODEATUP-TUTORIELS-WORKFLOW.md (skip
# this and narration drifts off its anchors, exactly the bug hit on
# foodeatup-mouvements-stock-tuto and foodeatup-tva-tuto).
#
# (name, src_start, src_end, target_out_duration, button, btn_size, caption)
segs = [
    ("A", 0.20,  5.10,  5.70, None,         None,        "1 · Repéré par Iris"),
    ("B", 5.10,  5.40,  0.95, BTN_REDETECT, SZ_REDETECT, None),
    ("C", 5.40,  8.70,  1.60, None,         None,        "2 · Nouvelle analyse"),
    ("D", 8.70, 11.20,  3.40, None,         None,        "11 opportunités détectées"),
    ("E", 11.20, 16.20, 5.85, None,         None,        "Score : urgence x valeur x fraîcheur"),
    ("F", 16.20, 19.75, 5.10, None,         None,        None),
    ("G", 19.75, 23.40, 5.30, None,         None,        "Prêt à agir"),
]
INTRO_D, OUTRO_D = 4.60, 6.40

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
# Matching tool: propose_campaigns(establishment_id) -- "Agent IA marketing :
# 2-4 propositions de campagnes chiffrees depuis les donnees reelles (RFM,
# jours creux, marges, marronniers)." No MCP tool literally detects
# overstock signals like Iris does on screen, so the prompt points at the
# closest real gesture instead of inventing a tool (see SCRIPT.md).
# ---------------------------------------------------------------------------
CLAUDE_PROMPT = ("Analyse les données de mon établissement FoodEatUp (ID [ID établissement]) "
                  "et propose-moi 2 à 4 campagnes marketing chiffrées pour écouler mes surstocks.")
CLAUDE_RESPONSE = "Bien sûr ! J'analyse vos ventes, vos marges et vos stocks pour vous proposer des campagnes ciblées…"

def card(img, out, secs, zoom_in=True, fade=True):
    """fade=False for the claude stages: they sit mid-video and only meet the
    timeline through xfade -- adding card()'s own fade-to-black on top makes
    short stages read as a murky blur (bug hit on the tva build)."""
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

CLAUDE_STAGE_D = [3.60, 2.60, 5.80]  # reveal, copied, chatbot mockup

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
    for name, s, e, target, btn, sz, cap in segs:
        parts.append(encode_seg(name, s, e, target, btn, sz, cap))
    parts += [f"{SEG}/claude1.mp4", f"{SEG}/claude2.mp4", f"{SEG}/claude3.mp4",
              f"{SEG}/outro.mp4"]

    trans = ["fade",       # intro -> A
             "fade",       # A -> B (continuous: click Redetecter maintenant)
             "fade",       # B -> C (loading state)
             "fade",       # C -> D (results + toast appear)
             "fade",       # D -> E (scroll into scored cards)
             "fade",       # E -> F (scroll continues)
             "slideleft",  # F -> G (scroll back to top -- distinct beat)
             "slideleft",  # G -> claude1
             "slideleft",  # claude1 -> claude2
             "slideleft",  # claude2 -> claude3
             "fade"]       # claude3 -> outro
    durs = [dur(p) for p in parts]
    starts, acc = [], 0.0
    for i, d in enumerate(durs):
        starts.append(acc); acc += d - (XF if i < len(durs) - 1 else 0)

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
    return silent, starts, acc

silent, starts, total = build_silent(OUTRO_D)
print(f"SILENT TOTAL: {dur(silent):.2f}s")
labels_order = ["intro"] + [s[0] for s in segs] + ["claude1", "claude2", "claude3", "outro"]
S = dict(zip(labels_order, starts))
OUTRO_START = S["outro"]

GAP = 0.22
anchor = {
    "N0": 0.35,                  # intro card
    "N1": S["A"] + 0.20,         # initial state (Nouveau plat proposal)
    "N2": S["B"] + 0.10,         # click Redetecter maintenant (spans B+C+D)
    "N3": S["E"] + 0.20,         # surstock cards + toast now visible
    "N4": S["F"] + 0.20,         # score breakdown while scrolling
    "N5": S["G"] + 0.20,         # back to top -- benefit line
    "N6": S["claude1"] + 0.20,   # explains the prompt (reveal + copied)
    "N7": S["claude3"] + 0.20,   # paste into Claude -> campaigns proposed
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
if drift:
    raise SystemExit("ABORT: narration drifted off its anchors -- resize the "
                     "segments (see the sizing note above segs) before shipping.")

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
FINAL = f"{ROOT}/out/foodeatup-stocks-dormants-tuto-v1.mp4"
run(["ffmpeg","-y","-v","error","-i",silent] + inputs +
    ["-filter_complex",";".join(filters),"-map","0:v","-map","[voa]",
     "-c:v","copy","-c:a","aac","-b:a","192k","-ar","48000","-ac","2",
     "-movflags","+faststart","-t",f"{total:.3f}",FINAL])
print(f"DONE: {FINAL}  {dur(FINAL):.2f}s")
