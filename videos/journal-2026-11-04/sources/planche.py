import subprocess,sys,json
from PIL import Image
n=sys.argv[1]; D=float(subprocess.run(['ffprobe','-v','error','-show_entries','format=duration','-of','csv=p=0',f'final/{n}.mp4'],capture_output=True,text=True).stdout)
ts=[1.5]+[D*k/7 for k in range(1,7)]+[D-1]
s=Image.new('RGB',(216*8,384))
for i,t in enumerate(ts):
    subprocess.run(['ffmpeg','-y','-loglevel','error','-ss',f'{t:.2f}','-i',f'final/{n}.mp4','-frames:v','1','-vf','scale=216:384','/dev/shm/f.jpg'])
    s.paste(Image.open('/dev/shm/f.jpg'),(i*216,0))
s.save(f'/dev/shm/planche-{n}.jpg',quality=85); print(n,round(D,1))
