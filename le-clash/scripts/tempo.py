import numpy as np, subprocess, json
SR=22050; HOP=256; NFFT=1024
x=np.frombuffer(subprocess.run(["ffmpeg","-v","error","-i","audio/le-clash.mp3","-ac","1","-ar",str(SR),
   "-f","f32le","-"],capture_output=True).stdout,dtype=np.float32)
dur=len(x)/SR
win=np.hanning(NFFT).astype(np.float32)
n=1+(len(x)-NFFT)//HOP
fr=np.lib.stride_tricks.as_strided(x,(n,NFFT),(x.strides[0]*HOP,x.strides[0]))
S=np.abs(np.fft.rfft(fr*win,axis=1)); fps=SR/HOP
flux=np.concatenate([[0],np.maximum(0,np.diff(np.log1p(S*10),axis=0)).sum(axis=1)])
k=int(fps*0.4); flux=np.maximum(flux-np.convolve(flux,np.ones(k)/k,mode="same"),0)
flux/=flux.max()

def score(bpm):
    per=60/bpm; best=(-1,0)
    for off in np.arange(0,per,0.004):
        t=np.arange(off,dur,per); idx=(t*fps).astype(int); idx=idx[idx<len(flux)]
        # fenêtre ±1 trame pour tolérer le jitter
        v=np.maximum.reduce([flux[np.clip(idx+d,0,len(flux)-1)] for d in (-1,0,1)]).mean()
        if v>best[0]: best=(v,off)
    return best

cands=[]
for bpm in np.arange(80,200.01,0.25):
    s,off=score(bpm); cands.append((s,bpm,off))
cands.sort(reverse=True)
print("meilleurs tempos (score, bpm, phase):")
seen=[]
for s,b,o in cands:
    if any(abs(b-x2)<3 for x2 in seen): continue
    seen.append(b); print(f"  {s:.4f}  {b:7.2f} BPM  phase {o:.3f}s")
    if len(seen)>=6: break
s142,o142=score(142.0)
print(f"\nréférence 142.00 BPM : score {s142:.4f} phase {o142:.3f}s")
best=cands[0]
json.dump({"bpm":best[1],"phase":best[2],"score":best[0],"duration":dur},open("work/tempo.json","w"),indent=1)
