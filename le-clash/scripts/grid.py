import numpy as np, subprocess, json
SR=22050; HOP=256; NFFT=1024
x=np.frombuffer(subprocess.run(["ffmpeg","-v","error","-i","audio/le-clash.mp3","-ac","1","-ar",str(SR),
   "-f","f32le","-"],capture_output=True).stdout,dtype=np.float32)
dur=len(x)/SR
win=np.hanning(NFFT).astype(np.float32); n=1+(len(x)-NFFT)//HOP
fr=np.lib.stride_tricks.as_strided(x,(n,NFFT),(x.strides[0]*HOP,x.strides[0]))
S=np.abs(np.fft.rfft(fr*win,axis=1)); fps=SR/HOP
flux=np.concatenate([[0],np.maximum(0,np.diff(np.log1p(S*10),axis=0)).sum(axis=1)])
k=int(fps*0.4); flux=np.maximum(flux-np.convolve(flux,np.ones(k)/k,mode="same"),0); flux/=flux.max()

BPM=144.0; per=60/BPM
# dérive : phase optimale mesurée par tranches de 20 s
print("contrôle de dérive (phase locale par tranche de 20 s) :")
for t0 in range(0,int(dur),20):
    t1=min(t0+20,dur)
    best=(-1,0)
    for off in np.arange(0,per,0.002):
        t=np.arange(t0+off,t1,per); idx=(t*fps).astype(int); idx=idx[idx<len(flux)]
        if len(idx)==0: continue
        v=np.maximum.reduce([flux[np.clip(idx+d,0,len(flux)-1)] for d in (-1,0,1)]).mean()
        if v>best[0]: best=(v,off)
    print(f"  {t0:3d}-{int(t1):3d}s  phase {best[1]:.3f}  score {best[0]:.3f}")
# phase globale fine
best=(-1,0)
for off in np.arange(0,per,0.001):
    t=np.arange(off,dur,per); idx=(t*fps).astype(int); idx=idx[idx<len(flux)]
    v=np.maximum.reduce([flux[np.clip(idx+d,0,len(flux)-1)] for d in (-1,0,1)]).mean()
    if v>best[0]: best=(v,off)
phase=best[1]
beats=np.arange(phase,dur,per)
# force de chaque temps (pour repérer les 1er temps de mesure)
strength=np.array([flux[max(0,int(b*fps)-1):int(b*fps)+2].max() if int(b*fps)<len(flux) else 0 for b in beats])
# mesure à 4 temps : quel décalage donne les downbeats les plus forts ?
sc=[strength[i::4].mean() for i in range(4)]
db=int(np.argmax(sc))
print(f"\nphase fine {phase:.4f}s | période {per:.6f}s | {len(beats)} temps")
print(f"downbeat = temps n°{db} (mod 4) ; scores {['%.3f'%s for s in sc]}")
print(f"1er downbeat à {beats[db]:.3f}s ; mesure = {per*4:.4f}s")
json.dump({"bpm":BPM,"period":per,"phase":float(phase),"downbeat_index":db,
           "beats":[round(float(b),4) for b in beats],
           "downbeats":[round(float(b),4) for b in beats[db::4]]},
          open("work/beatgrid.json","w"),indent=1)
