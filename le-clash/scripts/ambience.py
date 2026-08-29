import json, subprocess, math
SL = json.load(open("shotlist.json")); SHOTS = SL["shots"]
DUR = SL["duration"]
PONT_A, PONT_B = 126.0, SL["sections"]["COUPLET 3"][0]
GAIN_PONT = 10 ** (14/20)          # -8 dB au lieu de -22 dB

def has_audio(p):
    if not p: return False
    return bool(subprocess.run(["ffprobe","-v","error","-select_streams","a",
        "-show_entries","stream=codec_name","-of","csv=p=0",p],
        capture_output=True,text=True).stdout.strip())
AUD = {}
main = [s for s in SHOTS if s["layer"] in ("full", "card", "top")]
main.sort(key=lambda s: s["t0"])
ins, chains, labs = [], [], []
NIN = 0
for s in main:
    d = s["dur"] if s.get("dur") else round(s["t1"]-s["t0"], 4)
    if d <= 0.02: continue
    pont = s["side"] == "duel" and PONT_A <= s["t0"] < PONT_B
    if s["file"] not in AUD: AUD[s["file"]] = has_audio(s["file"])
    if (s["side"] == "chaos" or pont) and AUD[s["file"]]:
        g = GAIN_PONT if pont else 1.0
        i = NIN; NIN += 1; ins += ["-ss", f"{s['sin']:.3f}", "-t", f"{d+0.2:.4f}", "-i", s["file"]]
        f = (f"[{i}:a]atrim=0:{d:.4f},asetpts=PTS-STARTPTS,aformat=sample_fmts=fltp:"
             f"sample_rates=48000:channel_layouts=stereo,volume={g:.4f},"
             f"afade=t=in:st=0:d=0.008,afade=t=out:st={max(d-0.008,0):.4f}:d=0.008")
    else:
        i = NIN; NIN += 1; ins += ["-f","lavfi","-t",f"{d:.4f}","-i","anullsrc=r=48000:cl=stereo"]
        f = f"[{i}:a]atrim=0:{d:.4f},asetpts=PTS-STARTPTS"
    lab = f"[a{len(labs)}]"; chains.append(f + lab); labs.append(lab)

fc = ";".join(chains) + ";" + "".join(labs) + f"concat=n={len(labs)}:v=0:a=1[bed]"
cmd = ["ffmpeg","-y","-hide_banner","-loglevel","error"] + ins + \
      ["-filter_complex", fc, "-map","[bed]","-t",f"{DUR:.3f}","-c:a","pcm_s16le","work/bed.wav"]
print("nappe d'ambiance :", len(labs), "segments"); r=subprocess.run(cmd,capture_output=True,text=True)
if r.returncode: print(r.stderr[-1200:]); raise SystemExit(1)

# mesure loudnorm sur le mixage musique + nappe
mix = "[0:a]aformat=fltp:48000:stereo[m];[1:a]volume=-22dB[b];[m][b]amix=inputs=2:duration=first:normalize=0[mx]"
p = subprocess.run(["ffmpeg","-hide_banner","-i","audio/le-clash.mp3","-i","work/bed.wav",
      "-filter_complex", mix + ";[mx]loudnorm=I=-14:TP=-1:LRA=11:print_format=json[o]",
      "-map","[o]","-f","null","-"], capture_output=True, text=True)
import re
j = json.loads(re.search(r"\{[^{}]*input_i.*?\}", p.stderr, re.S).group(0))
print({k: j[k] for k in ("input_i","input_tp","input_lra","input_thresh")})
subprocess.run(["ffmpeg","-y","-hide_banner","-loglevel","error","-i","audio/le-clash.mp3",
  "-i","work/bed.wav","-filter_complex",
  mix + f";[mx]loudnorm=I=-14:TP=-1:LRA=11:measured_I={j['input_i']}:measured_TP={j['input_tp']}"
        f":measured_LRA={j['input_lra']}:measured_thresh={j['input_thresh']}"
        f":offset={j['target_offset']}:linear=true[o]",
  "-map","[o]","-t",f"{DUR:.3f}","-c:a","pcm_s16le","work/mix.wav"], check=True)
q = subprocess.run(["ffmpeg","-hide_banner","-i","work/mix.wav","-af",
     "loudnorm=I=-14:TP=-1:print_format=json","-f","null","-"], capture_output=True, text=True)
k = json.loads(re.search(r"\{[^{}]*input_i.*?\}", q.stderr, re.S).group(0))
print(f"master audio : I={k['input_i']} LUFS  TP={k['input_tp']} dBTP  LRA={k['input_lra']}")
