import sys,json,subprocess,numpy as np,glob
from faster_whisper import WhisperModel
m=WhisperModel("small",compute_type="int8")
for d in sys.argv[1:]:
  out={}
  for f in sorted(glob.glob(f"{d}/a/*.mp3")):
    r=subprocess.run(["ffmpeg","-v","error","-i",f,"-f","s16le","-ac","1","-ar","16000","-"],capture_output=True).stdout
    a=np.frombuffer(r,np.int16).astype(np.float32)/32768
    segs,_=m.transcribe(a,language="fr",word_timestamps=True)
    out[f]=[(w.word.strip(),round(w.start,2),round(w.end,2)) for s in segs for w in s.words]
    print(f, " ".join(f"{w}@{s}-{e}" for w,s,e in out[f]))
  json.dump(out,open(f"{d}/words.json","w"),ensure_ascii=False)
