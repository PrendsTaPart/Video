"""cfg.js d'un épisode : transcrit voix/voix.mp3 (faster-whisper) puis aligne le texte de script.txt.
Usage : python3 build_cfg.py <dossier épisode> [<dossier> ...]"""
import sys,json,re,difflib,subprocess,os,numpy as np
from faster_whisper import WhisperModel
m=WhisperModel("small",compute_type="int8")
NUM={'1':'un','2':'deux','3':'trois','4':'quatre','5':'cinq','6':'six','7':'sept','10':'dix','20':'vingt','1%':'un'}
norm=lambda w:re.sub(r"[^a-z0-9àâäéèêëîïôöùûüç]","",w.lower())
O=0.35
for d in sys.argv[1:]:
  wj=f"{d}/voix/words.json"
  if not os.path.exists(wj):
    r=subprocess.run(["ffmpeg","-v","error","-i",f"{d}/voix/voix.mp3","-f","s16le","-ac","1","-ar","16000","-"],capture_output=True).stdout
    a=np.frombuffer(r,np.int16).astype(np.float32)/32768
    segs,_=m.transcribe(a,language="fr",word_timestamps=True)
    json.dump([(w.word.strip(),round(w.start,2),round(w.end,2)) for s in segs for w in s.words],open(wj,"w"),ensure_ascii=False)
  wh=json.load(open(wj))
  W=[]
  for w,s,e in wh:
    if W and (w.startswith("'") or w.startswith('-')): W[-1]=[W[-1][0]+w,W[-1][1],e]
    else: W.append([NUM.get(w.strip(',.?'),w),s,e])
  TXT=[l for l in open(f"{d}/script.txt").read().strip().split('\n') if l.strip()]
  toks=[];lid=[]
  for i,l in enumerate(TXT):
    for t in l.split():
      if t in (':','?','!'):
        if toks: toks[-1]+= ' '+t if t!=':' else ''
        continue
      toks.append(t);lid.append(i)
  a=[norm(t) for t in toks];b=[norm(w[0]) for w in W]
  T=[None]*len(a);E=[None]*len(a)
  for blk in difflib.SequenceMatcher(None,a,b,autojunk=False).get_matching_blocks():
    for k in range(blk.size): T[blk.a+k]=W[blk.b+k][1];E[blk.a+k]=W[blk.b+k][2]
  if T[0] is None:T[0]=W[0][1]
  if T[-1] is None:T[-1]=W[-1][1]
  kn=[i for i,t in enumerate(T) if t is not None]
  for i in range(len(T)):
    if T[i] is None:
      lo=max(k for k in kn if k<i);hi=min(k for k in kn if k>i);T[i]=T[lo]+(T[hi]-T[lo])*(i-lo)/(hi-lo)
  for i in range(1,len(T)):T[i]=max(T[i],T[i-1]+.05)
  words=[[t,round(x+O,2),l] for t,x,l in zip(toks,T,lid)]
  lines=[]
  for i,l in enumerate(TXT):
    idx=[j for j in range(len(lid)) if lid[j]==i];last=idx[-1]
    end=(E[last] if E[last] else T[last]+.4)+O
    lines.append({"t0":words[idx[0]][1],"t1":round(end,2),"txt":l})
  dur=round(W[-1][2]+O+3.0,2)
  cfg={"dur":dur,"words":words,"lines":lines}
  json.dump(cfg,open(f"{d}/cfg.json","w"),ensure_ascii=False)
  open(f"{d}/cfg.js","w").write("window.CFG="+json.dumps(cfg,ensure_ascii=False)+";")
  print(d.split('/')[-1],'dur',dur,'non alignés',sum(1 for x in E if x is None),'/',len(E))
