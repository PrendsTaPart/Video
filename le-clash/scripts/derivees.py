import json, re, os
SL = json.load(open("shotlist.json")); SHOTS = SL["shots"]

# ---------- TikTok 15 s : 3 s d'amorce (EP083 puis EP142) + le refrain 1 ----------
REF1 = min(s["t0"] for s in SHOTS if s.get("section") == "refrain1")
PH, BT = SL["phase"], SL["beat"]
END  = round(PH + round((79.00 - PH) / BT) * BT, 4)   # fin de « …qui a d'l'avance », calée sur la grille
A    = round(REF1 - 3.0, 4)
sel  = [dict(s) for s in SHOTS if s["t1"] > REF1 - 1e-3 and s["t0"] < END - 1e-3]
for s in sel:
    s["t1"] = min(s["t1"], END); s["dur"] = round(s["t1"] - s["t0"], 4)
amorce = [
 dict(t0=A, t1=round(A+1.2,4), dur=1.2, side="chaos", layer="full", src="EP083", sin=0.0,
      file="sources/EP083.mp4", titre="Le cri dans le vide", note="amorce"),
 dict(t0=round(A+1.2,4), t1=REF1, dur=round(REF1-A-1.2,4), side="duel", layer="full", src="EP142",
      sin=0.0, file="sources/EP142.mp4", titre="Duel à la spatule", note="amorce — le calme"),
]
out = amorce + sel
for s in out:
    s["t0"] = round(s["t0"] - A, 4); s["t1"] = round(s["t1"] - A, 4); s["dur"] = round(s["t1"]-s["t0"], 4)
json.dump({**SL, "duration": round(END - A, 4), "shots": sorted(out, key=lambda s: s["t0"])},
          open("shotlist-tiktok.json", "w"), ensure_ascii=False, indent=1)
print(f"tiktok : {A:.2f} → {END:.2f}  ({END-A:.2f} s), {len(out)} plans")

# ---------- sous-titres décalés pour le TikTok ----------
def shift_ass(src, dst, off, dur):
    def tc(t):
        h=int(t//3600); m=int(t%3600//60); s=t%60
        return f"{h}:{m:02d}:{s:05.2f}"
    keep=[]
    for line in open(src):
        m=re.match(r"Dialogue: (\d+),([\d:.]+),([\d:.]+),(.*)$", line)
        if not m: keep.append(line); continue
        def p(x):
            h,mi,s=x.split(":"); return int(h)*3600+int(mi)*60+float(s)
        a,b=p(m.group(2))-off, p(m.group(3))-off
        if b<=0 or a>=dur: continue
        keep.append(f"Dialogue: {m.group(1)},{tc(max(a,0))},{tc(min(b,dur))},{m.group(4)}\n")
    open(dst,"w").writelines(keep)
shift_ass("work/subs.ass", "work/subs-tiktok.ass", A, round(END-A,4))
print("sous-titres tiktok :", sum(1 for l in open("work/subs-tiktok.ass") if l.startswith("Dialogue")), "états")

# ---------- sous-titres 16:9 (1280×720) ----------
src = open("work/subs.ass").read()
src = src.replace("PlayResX: 1080", "PlayResX: 1280").replace("PlayResY: 1920", "PlayResY: 720")
src = src.replace("Poppins ExtraBold,84,", "Poppins ExtraBold,46,")
src = re.sub(r"\\pos\((\d+),(\d+)\)",
             lambda m: f"\\pos({int(int(m.group(1))*1280/1080)},{int(540 + (int(m.group(2))-1330)*0.30)})", src)
src = src.replace("Outline, Shadow", "Outline, Shadow")
src = re.sub(r"(Style: K,[^\n]*?),1,0,1,7,5,5,", r"\1,1,0,1,4,3,5,", src)
open("work/subs-16x9.ass","w").write(src)
print("sous-titres 16:9 écrits")
