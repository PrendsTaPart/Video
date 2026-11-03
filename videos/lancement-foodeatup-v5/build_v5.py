#!/usr/bin/env python3
"""V5 « Je ne vais pas licencier votre chef de partie » — 16:9 1920x1080, ~48s.
Manifeste typographique (visage) + FLOW stills (croix rouge) + SR écrans + sting. Charte FoodEatUp."""
import os, subprocess, glob
from PIL import Image, ImageDraw, ImageFont, ImageFilter
HERE=os.path.dirname(os.path.abspath(__file__)); os.chdir(HERE)
BASE="/home/user/Video"; FD=f"{BASE}/videos/rapidocms-presentation-4min/assets/fonts"
LOGO=f"{BASE}/studio-video/assets/brand/logo"; SCR=f"{BASE}/assets/screens/foodeatup"
BGM=f"{BASE}/videos/stories-foodeatup-30j/audio/bgm.mp3"; CHIME=f"{BASE}/videos/serie-30-e01/assets/sfx/chime.mp3"
def F(n,s): return ImageFont.truetype(os.path.join(FD,n),s)
P800=lambda s:F("Poppins-800.ttf",s); P700=lambda s:F("Poppins-700.ttf",s); P600=lambda s:F("Poppins-600.ttf",s)
ANTH=(15,26,35); BLUE=(0,123,255); ORANGE=(255,165,0); CREAM=(252,249,230); WHITE=(255,255,255); INK=(35,31,32); RED=(224,49,49); SKY=(166,208,255)
MARK=Image.open(f"{LOGO}/foodeatup-mark-eight.png").convert("RGBA"); MASC=Image.open(f"{LOGO}/foodeatup-logo-mascot.png").convert("RGBA")
W,H=1920,1080; FPS=30
os.makedirs("frames",exist_ok=True); os.makedirs("work",exist_ok=True); os.makedirs("renders",exist_ok=True)
VENC=["-c:v","libx264","-preset","medium","-crf","20","-pix_fmt","yuv420p","-r",str(FPS),"-c:a","aac","-b:a","192k","-ar","44100","-ac","2"]
def dur(f): return float(subprocess.check_output(["ffprobe","-v","error","-show_entries","format=duration","-of","csv=p=0",f]).strip())
def run(cmd,n):
    r=subprocess.run(cmd,stdout=subprocess.DEVNULL,stderr=subprocess.PIPE)
    if r.returncode!=0: print("ERR",n,r.stderr.decode()[-1400:]); raise SystemExit(1)
    print("ok",n,round(dur(cmd[-1]),2))
def wrapd(dr,t,f,mw):
    out=[];cur=""
    for wd in t.split():
        s=(cur+" "+wd).strip()
        if dr.textbbox((0,0),s,font=f)[2]<=mw: cur=s
        else: out.append(cur); cur=wd
    out.append(cur); return out
def cover(im,w=W,h=H):
    r=max(w/im.width,h/im.height); im=im.resize((int(im.width*r),int(im.height*r)),Image.LANCZOS)
    x=(im.width-w)//2; y=(im.height-h)//2; return im.crop((x,y,x+w,y+h))
def wm(im):
    m=MARK.resize((46,92),Image.LANCZOS); a=m.split()[3].point(lambda p:int(p*0.4)); m.putalpha(a); im.alpha_composite(m,(60,60))
def manifesto(txt,out,fs=96,fg=CREAM,accent=None):
    im=Image.new("RGBA",(W,H),ANTH+(255,)); g=Image.new("RGBA",(W,H),(0,0,0,0)); ImageDraw.Draw(g).ellipse([W//2-500,H//2-360,W//2+500,H//2+360],fill=SKY+(20,)); im.alpha_composite(g.filter(ImageFilter.GaussianBlur(160)))
    wm(im); d=ImageDraw.Draw(im); f=P800(fs); lines=wrapd(d,txt,f,W-360); lh=fs+22; y=(H-lh*len(lines))//2
    for l in lines: d.text((W/2,y+lh/2),l,font=f,fill=fg,anchor="mm"); y+=lh
    if accent: d.rectangle([W//2-90,y+10,W//2+90,y+18],fill=accent+(255,))
    im.convert("RGB").save(f"frames/{out}.png")

# manifeste plans 1,4,7
manifesto("Non. Je ne vais pas licencier votre chef de partie.","p1",fs=104,fg=WHITE)
manifesto("J'ai eu une brigade. Je sais ce que ça coûte, de perdre quelqu'un.","p4",fs=88,fg=CREAM)
manifesto("Personne n'est devenu cuisinier pour remplir un tableau de températures.","p7",fs=92,fg=CREAM,accent=ORANGE)

# sting 16:9 (logo reveal + baseline)
im=Image.new("RGBA",(W,H),ANTH+(255,)); m=MASC.resize((640,int(MASC.height*640/MASC.width)),Image.LANCZOS)
im.alpha_composite(m,((W-m.width)//2,(H-m.height)//2-40)); d=ImageDraw.Draw(im)
d.text((W/2,H//2+120),"Une infinité de solutions pour gérer votre restaurant",font=P600(34),fill=SKY,anchor="mm")
im.convert("RGB").save("frames/sting.png")
# sting flash variant
im2=im.copy(); g=Image.new("RGBA",(W,H),(0,0,0,0)); ImageDraw.Draw(g).ellipse([W//2-160,H//2-120,W//2+160,H//2+40],fill=ORANGE+(150,)); im2.alpha_composite(g.filter(ImageFilter.GaussianBlur(60)))
im2.convert("RGB").save("frames/sting_flash.png")

# FLOW « ce qu'elle ne fait pas » : croix rouge + label
NOTS=[("flow02-dresser","Dresser"),("flow03-sentir","Sentir"),("flow04-rassurer","Rassurer"),("flow05-connaitre","Connaître")]
for slug,label in NOTS:
    im=cover(Image.open(f"assets-generes/{slug}.jpg").convert("RGBA")); sc=Image.new("RGBA",(W,H),(6,10,18,90)); im.alpha_composite(sc); wm(im); d=ImageDraw.Draw(im)
    # croix rouge
    cx,cy,r=W-180,180,70; d.ellipse([cx-r,cy-r,cx+r,cy+r],outline=RED+(255,),width=12); d.line([cx-34,cy-34,cx+34,cy+34],fill=RED+(255,),width=14); d.line([cx-34,cy+34,cx+34,cy-34],fill=RED+(255,),width=14)
    f=P800(84); w=d.textbbox((0,0),label,font=f)[2]; d.text((110,H-160),label,font=f,fill=WHITE,anchor="lm")
    d.text((112,H-160),label,font=f,fill=WHITE,anchor="lm")
    im.convert("RGB").save(f"frames/not_{slug[4:6]}.png")

# FLOW pleins (plans 2 & 8)
for slug,out in [("flow01-brigade","p2"),("flow06-detendu","p8")]:
    im=cover(Image.open(f"assets-generes/{slug}.jpg").convert("RGBA")); wm(im); im.convert("RGB").save(f"frames/{out}.png")

# SR validations : 3 écrans (tableau, carte, PDF)
def sr_frame(screen,label,out,pdf=False):
    im=Image.new("RGBA",(W,H),ANTH+(255,)); wm(im); d=ImageDraw.Draw(im)
    bx,by,bw,bh=460,150,1000,760
    d.rounded_rectangle([bx,by,bx+bw,by+bh],22,outline=BLUE+(255,),width=8,fill=WHITE+(255,))
    for i,cxx in enumerate([bx+32,bx+66,bx+100]): d.ellipse([cxx-9,by+22,cxx+9,by+40],fill=[(255,95,86),(255,189,46),(39,201,63)][i]+(255,))
    if pdf:
        d.rounded_rectangle([bx+330,by+230,bx+670,by+560],16,fill=(245,247,250,255),outline=(210,215,225,255),width=3)
        d.text((bx+500,by+340),"PDF",font=P800(90),fill=BLUE,anchor="mm"); d.text((bx+500,by+440),"conforme",font=P700(40),fill=INK,anchor="mm")
    else:
        s=Image.open(f"{SCR}/{screen}").convert("RGBA"); r=min((bw-40)/s.width,(bh-80)/s.height); s=s.resize((int(s.width*r),int(s.height*r)),Image.LANCZOS)
        im.alpha_composite(s,(bx+(bw-s.width)//2,by+54+(bh-80-s.height)//2))
    d=ImageDraw.Draw(im); d.ellipse([110,150,178,218],fill=ORANGE+(255,)); d.line([128,184,146,202],fill=INK,width=9); d.line([146,202,172,166],fill=INK,width=9)
    d.text((200,184),label,font=P800(64),fill=ORANGE,anchor="lm")
    im.convert("RGB").save(f"frames/{out}.png")
sr_frame("checklist-hygiene.png","Le tableau","sr1")
sr_frame("ajout-produit.png","La carte","sr2")
sr_frame(None,"Le PDF","sr3",pdf=True)

# plan 9 : sting sortie + offre
im=Image.new("RGBA",(W,H),ANTH+(255,)); m=MASC.resize((520,int(MASC.height*520/MASC.width)),Image.LANCZOS); im.alpha_composite(m,((W-m.width)//2,150)); d=ImageDraw.Draw(im)
d.text((W/2,560),"-50%",font=P800(160),fill=ORANGE,anchor="mm")
f=P700(52); t="30 places bêta · jusqu'au 31 août 2026"; w=d.textbbox((0,0),t,font=f)[2]
d.rounded_rectangle([W//2-w//2-44,720,W//2+w//2+44,812],40,fill=BLUE+(255,)); d.text((W/2,766),t,font=f,fill=INK,anchor="mm")
im.convert("RGB").save("frames/p9.png")
print("V5 frames OK")
