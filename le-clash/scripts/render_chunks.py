import json, os, sys, subprocess, math

SLF  = os.environ.get("SL_FILE", "shotlist.json")
SL   = json.load(open(SLF))
W    = int(os.environ.get("OUT_W", 1080));  H = int(os.environ.get("OUT_H", 1920))
CRF  = int(os.environ.get("OUT_CRF", 28));  PRE = os.environ.get("OUT_PRESET", "slow")
OUT  = os.environ["OUT_FILE"]
SUBS = os.environ.get("SUBS_FILE", "work/subs.ass")
AUDIO_SS = float(os.environ.get("AUDIO_SS", 0))
DUR  = float(os.environ.get("OUT_DUR", SL["duration"]))
WM   = os.environ.get("WATERMARK", "1") == "1"
NCH  = int(os.environ.get("CHUNKS", "7"))
TAG  = os.environ.get("TAG", "m")
FPS  = 30
VERT = H >= W
if VERT: HW, HH = W, ((H - 4) // 2) & ~1; SEP = H - 2*HH
else:    HW, HH = ((W - 4) // 2) & ~1, H;  SEP = W - 2*HW
CREME, MARINE = "0xFCF9E6", "0x0F1A23"
LOGO = "/home/user/Video/studio-video/assets/brand/logo/foodeatup-logo-horizontal.png"
GRADE = {"chaos":"eq=saturation=0.72:contrast=1.15,colorbalance=bs=0.06,vignette=PI/3.5",
         "maitrise":"eq=saturation=1.12:contrast=1.02,colorbalance=rs=0.05",
         "duel":"eq=saturation=0.95:contrast=1.06", "sting":"null"}
ALL = SL["shots"]
# garde-fou : ne jamais chercher au-delà de la dernière image d'une source
_dur = {}
def src_dur(p):
    if p not in _dur:
        _dur[p] = float(subprocess.run(["ffprobe","-v","error","-select_streams","v:0",
            "-show_entries","stream=duration","-of","csv=p=0",p],
            capture_output=True,text=True).stdout.strip() or 0)
    return _dur[p]
for _s in ALL:
    if _s.get("file") and _s.get("sin") is not None:
        d = src_dur(_s["file"])
        if _s.get("freeze"):
            if d and _s["sin"] > d - 0.12: _s["sin"] = round(max(0.0, d - 0.12), 3)
        elif d:
            need = _s["sin"] + (_s.get("dur") or (_s["t1"] - _s["t0"]))
            if need > d - 0.01:          # le plan dépasserait la fin de sa source
                _s["sin"] = round(max(0.0, _s["sin"] - (need - (d - 0.01))), 3)
PONT_A, PONT_B, T_STING = 126.60, SL["sections"]["COUPLET 3"][0], 198.70

# --- frontières de tranches, posées sur des débuts de plan ---
starts = sorted({s["t0"] for s in ALL if s["layer"] in ("full","card")} |
                {s["t0"] for s in ALL if s["layer"] == "top"})
bounds = [0.0]
for k in range(1, NCH):
    target = DUR * k / NCH
    bounds.append(min(starts, key=lambda x: abs(x - target)))
bounds = sorted(set(bounds)) + [DUR]

def render_chunk(A, B, path):
    ins, chains, labels = [], [], []
    def add_input(a): ins.append(a); return len(ins)-1
    def cover(w,h): return f"scale={w}:{h}:force_original_aspect_ratio=increase,crop={w}:{h},setsar=1"

    def prep(s):
        """découpe le plan sur [A,B] en conservant le point d'entrée et le compte d'images absolu"""
        t0, t1 = max(s["t0"], A), min(s["t1"], B)
        if t1 - t0 < 1e-3: return None
        d = dict(s)
        d["_n"] = max(1, round(t1*FPS) - round(t0*FPS))
        if not s.get("freeze") and t0 > s["t0"] + 1e-6:
            d["sin"] = round(s["sin"] + (t0 - s["t0"]), 3)
        d["t0"], d["t1"] = round(t0 - A, 4), round(t1 - A, 4)
        d["dur"] = round(d["t1"] - d["t0"], 4)
        d["_abs0"] = t0
        return d

    def build(sh, w, h):
        dur, side, N = sh["dur"], sh["side"], sh["_n"]
        if sh["layer"] == "card":
            col = "black" if sh.get("card") == "black" else MARINE
            i = add_input(["-f","lavfi","-t",f"{dur+0.4:.4f}","-i",f"color=c={col}:s={w}x{h}:r={FPS}"])
            f=[f"[{i}:v]"]
            if sh.get("card") == "2015":
                f.append(f"drawtext=fontfile=/root/.fonts/Poppins-800.ttf:text='20\\:15':"
                         f"fontcolor={CREME}:fontsize={int(h*0.13)}:x=(w-text_w)/2:y=(h-text_h)/2,")
            f.append(f"fps={FPS},trim=start_frame=0:end_frame={N},setpts=PTS-STARTPTS,setsar=1,format=yuv420p")
            lab=f"[v{len(labels)}]"; chains.append("".join(f)+lab); labels.append(lab); return lab
        if sh.get("freeze"):
            i = add_input(["-ss",f"{sh['sin']:.3f}","-t","0.09","-i",sh["file"]])
            pre=(f"[{i}:v]{cover(w,h)},setpts=PTS-STARTPTS,fps={FPS},trim=start_frame=0:end_frame=1,"
                 f"setpts=PTS-STARTPTS,tpad=stop_mode=clone:stop_duration={dur+0.5:.4f},"
                 f"trim=start_frame=0:end_frame={N},setpts=PTS-STARTPTS,")
        else:
            i = add_input(["-ss",f"{sh['sin']:.3f}","-t",f"{dur+0.45:.4f}","-i",sh["file"]])
            pre=(f"[{i}:v]{cover(w,h)},setpts=PTS-STARTPTS,fps={FPS},"
                 f"trim=start_frame=0:end_frame={N},setpts=PTS-STARTPTS,")
        f=[pre, GRADE.get(side, GRADE["duel"]), ","]
        if sh.get("nb"): f.append("hue=s=0,")
        if side=="chaos" and not sh.get("freeze"):
            z=1.03
            f.append(f"scale={int(w*z)}:{int(h*z)},crop={w}:{h}:"
                     f"'{int(w*(z-1)/2)}+2*sin(31*t)':'{int(h*(z-1)/2)}+2*cos(37*t)',")
        if side in ("maitrise","duel") and not sh.get("freeze") and dur>0.5 and sh["_abs0"]==sh_orig[id(sh)]:
            f.append("fade=t=in:st=0:d=0.133,")
        if sh.get("flash"): f.append("fade=t=in:st=0:d=0.067:color=white,")
        f.append("setsar=1,format=yuv420p")
        lab=f"[v{len(labels)}]"; chains.append("".join(f)+lab); labels.append(lab); return lab

    sel = []
    sh_orig = {}
    for s in ALL:
        d = prep(s)
        if d: sh_orig[id(d)] = s["t0"]; sel.append(d)
    full=[s for s in sel if s["layer"] in ("full","card")]
    tops=[s for s in sel if s["layer"]=="top"]; bots=[s for s in sel if s["layer"]=="bottom"]
    spans=[]
    for s in sorted(tops, key=lambda x:x["t0"]):
        if spans and abs(spans[-1][1]-s["t0"])<1e-3: spans[-1][1]=s["t1"]
        else: spans.append([s["t0"],s["t1"]])
    blocks=[("full",s["t0"],s["t1"],s) for s in full]+[("split",a,b,None) for a,b in spans]
    blocks.sort(key=lambda x:x[1])
    seq=[]
    for kind,a,b,s in blocks:
        if kind=="full": seq.append(build(s,W,H)); continue
        tl=[build(x,HW,HH) for x in sorted(tops,key=lambda x:x["t0"]) if a-1e-3<=x["t0"]<b]
        bl=[build(x,HW,HH) for x in sorted(bots,key=lambda x:x["t0"]) if a-1e-3<=x["t0"]<b]
        T,Bl=f"[T{a}]".replace(".","_"), f"[B{a}]".replace(".","_")
        pad = f"pad={W}:{HH+SEP}:0:0:color={CREME}" if VERT else f"pad={HW+SEP}:{H}:0:0:color={CREME}"
        chains.append("".join(tl)+f"concat=n={len(tl)}:v=1:a=0,fps={FPS},{pad},setsar=1"+T)
        chains.append("".join(bl)+f"concat=n={len(bl)}:v=1:a=0,fps={FPS},setsar=1"+Bl)
        o=f"[S{a}]".replace(".","_")
        chains.append(f"{T}{Bl}{'vstack' if VERT else 'hstack'}=inputs=2,setsar=1,format=yuv420p{o}")
        seq.append(o)

    tail=f"[vc]setpts=PTS+{A:.4f}/TB[vabs];"          # on repasse en temps absolu
    cur="[vabs]"
    if WM:
        li=add_input(["-framerate",str(FPS),"-loop","1","-t",f"{DUR+1:.3f}",
                      "-i",LOGO])
        tail+=(f"[{li}:v]scale={int(W/5.4)}:-1,format=rgba,colorchannelmixer=aa=0.72[wm];"
               f"{cur}[wm]overlay={int(W*0.041)}:{int(H*0.132)}:"
               f"enable='not(between(t,{PONT_A},{PONT_B}))*not(gte(t,{T_STING}))'[vw];")
        cur="[vw]"
    tail+=f"{cur}subtitles={SUBS}:fontsdir=/root/.fonts,setpts=PTS-STARTPTS[vout]"
    fc=";".join(chains)+";"+"".join(seq)+f"concat=n={len(seq)}:v=1:a=0,fps={FPS}[vc];"+tail
    cmd=["ffmpeg","-y","-hide_banner","-loglevel","error","-stats"]
    for a2 in ins: cmd+=a2
    cmd+=["-filter_complex",fc,"-map","[vout]","-r",str(FPS),"-an",
          "-c:v","libx264","-preset",PRE,"-crf",str(CRF),"-pix_fmt","yuv420p","-profile:v","high",
          "-x264-params","aq-mode=3","-frames:v",str(round(B*FPS)-round(A*FPS)),path]
    print(f"  tranche {A:7.2f} → {B:7.2f} : {len(ins)} entrées, {round(B*FPS)-round(A*FPS)} images", flush=True)
    r=subprocess.run(cmd)
    if r.returncode: sys.exit(f"échec sur la tranche {A}-{B} (code {r.returncode})")

ONLY = os.environ.get("CHUNK_ONLY")
ONLY = set(int(x) for x in ONLY.split(",")) if ONLY else None
paths=[]
for k in range(len(bounds)-1):
    p=f"work/chunk-{TAG}-{k:02d}.mp4"
    if ONLY is None or k in ONLY: render_chunk(bounds[k], bounds[k+1], p)
    else: print(f"  tranche {k} réutilisée", flush=True)
    paths.append(p)

with open(f"work/chunks-{TAG}.txt","w") as f:
    for p in paths: f.write(f"file '{os.path.abspath(p)}'\n")
subprocess.run(["ffmpeg","-y","-hide_banner","-loglevel","error","-f","concat","-safe","0",
                "-i",f"work/chunks-{TAG}.txt","-c","copy",f"work/video-{TAG}.mp4"], check=True)
subprocess.run(["ffmpeg","-y","-hide_banner","-loglevel","error","-i",f"work/video-{TAG}.mp4"]
               + (["-ss",f"{AUDIO_SS:.3f}"] if AUDIO_SS else []) +
               ["-i","work/mix.wav","-map","0:v","-map","1:a","-c:v","copy",
                "-c:a","aac","-b:a","128k","-movflags","+faststart","-t",f"{DUR:.3f}",OUT], check=True)
print("→", OUT)
