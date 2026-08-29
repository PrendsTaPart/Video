from PIL import Image, ImageDraw, ImageFont, ImageFilter
import subprocess, os

P8="/root/.fonts/Poppins-800.ttf"; P7="/root/.fonts/Poppins-700.ttf"
CREME=(252,249,230); MARINE=(15,26,35); BLEU=(0,123,255); ORANGE=(255,165,0)
LOGO="/home/user/Video/studio-video/assets/brand/logo/foodeatup-logo-horizontal.png"

def track(d,xy,text,font,fill,sp=0):
    ws=[d.textlength(c,font=font) for c in text]; total=sum(ws)+sp*(len(text)-1)
    asc,desc=font.getmetrics(); x=xy[0]-total/2; y=xy[1]-(asc+desc)/2
    for c,w in zip(text,ws): d.text((x,y),c,font=font,fill=fill); x+=w+sp
    return total

# --- vignette YouTube 1280×720, tirée du plan de duel ---
W,H=1280,720
subprocess.run(["ffmpeg","-v","error","-y","-ss","9.62","-i","sources/EP142.mp4",
                "-frames:v","1","work/yt-src.png"],check=True)
src=Image.open("work/yt-src.png").convert("RGB")
s=src.resize((int(H*src.width/src.height*1.9), int(H*1.9)), Image.LANCZOS)
left=(s.width-W)//2; top=int(s.height*0.30)
bg=s.crop((left,top,left+W,top+H)).convert("RGBA")
bg=Image.eval(bg,lambda v:int(255*((v/255)**1.12)))
vg=Image.new("L",(W,H),0); dv=ImageDraw.Draw(vg)
dv.ellipse((-W*0.25,-H*0.30,W*1.25,H*1.30),fill=255)
vg=vg.filter(ImageFilter.GaussianBlur(160))
bg=Image.composite(bg,Image.new("RGBA",(W,H),MARINE+(255,)),vg)
g=Image.new("L",(1,H))
for y in range(H): g.putpixel((0,y),int(255*max(0,(y/H-0.35)/0.65)*0.94))
lay=Image.new("RGBA",(W,H),MARINE+(0,)); lay.putalpha(g.resize((W,H))); bg.alpha_composite(lay)
gt=Image.new("L",(1,H))
for y in range(H): gt.putpixel((0,y),int(255*0.80*max(0.0,1-(y/H)/0.24)))
lt=Image.new("RGBA",(W,H),MARINE+(0,)); lt.putalpha(gt.resize((W,H))); bg.alpha_composite(lt)
d=ImageDraw.Draw(bg)
track(d,(W/2,470),"LE CLASH",ImageFont.truetype(P8,168),CREME,sp=4)
d.line((W/2-300,562,W/2+300,562),fill=ORANGE+(235,),width=4)
track(d,(W/2,606),"DEUX CUISINES. UNE RUE.",ImageFont.truetype(P8,38),CREME+(240,),sp=8)
track(d,(W/2,72),"UN FILM PRODUIT PAR FOODEATUP",ImageFont.truetype(P7,26),CREME+(205,),sp=6)
logo=Image.open(LOGO).convert("RGBA"); lw=176
logo=logo.resize((lw,int(lw*logo.height/logo.width)),Image.LANCZOS)
bg.alpha_composite(logo,(W-lw-40,H-int(lw*logo.height/logo.width)-28))
bg.convert("RGB").save("dist/youtube-vignette-1280x720.jpg",quality=90,optimize=True)
print("vignette :",os.path.getsize("dist/youtube-vignette-1280x720.jpg")//1024,"Ko")
