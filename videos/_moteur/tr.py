import sys,json
from faster_whisper import WhisperModel
m=WhisperModel("small",compute_type="int8")
import subprocess,numpy as np
def load(d):
  r=subprocess.run(["ffmpeg","-v","error","-i",f"{d}/vo.mp3","-f","s16le","-ac","1","-ar","16000","-"],capture_output=True).stdout
  return np.frombuffer(r,np.int16).astype(np.float32)/32768
for d in sys.argv[1:]:
  segs,_=m.transcribe(load(d),language="fr",word_timestamps=True)
  W=[(w.word.strip(),round(w.start,2),round(w.end,2)) for s in segs for w in s.words]
  json.dump(W,open(f"{d}/words.json","w"),ensure_ascii=False); print(d,len(W),W[-1])
