import subprocess, sys, json
from PIL import Image
ID = sys.argv[1]; mp4 = f'out/{ID}/tutoriel-rapido-{ID}.mp4'
d = float(subprocess.run(['ffprobe','-v','error','-show_entries','format=duration','-of','csv=p=0',mp4],capture_output=True,text=True).stdout)
ims = []
for i in range(8):
    t = 1 + (d - 2) * i / 7
    p = f'out/{ID}/qa{i}.png'
    subprocess.run(['ffmpeg','-v','error','-y','-ss',f'{t:.2f}','-i',mp4,'-frames:v','1','-vf','scale=480:-1',p],check=True)
    ims.append(Image.open(p))
W, H = ims[0].size; c = Image.new('RGB', (W * 4, H * 2))
for i, im in enumerate(ims): c.paste(im, ((i % 4) * W, (i // 4) * H))
c.save(f'out/{ID}/planche-qa.png'); print(f'{ID} {d:.1f}s')
