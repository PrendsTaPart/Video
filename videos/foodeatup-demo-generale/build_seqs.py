#!/usr/bin/env python3
"""FoodEatUp — Démo générale 1920x1080. Cartes typo + Ken Burns + mascottes + Jarvis + VO + BGM + sous-titres."""
import os, subprocess, math, json
from PIL import Image, ImageDraw, ImageFont

os.chdir(os.path.dirname(os.path.abspath(__file__)))
W, H, FPS = 1920, 1080, 30
BLUE=(20,122,255); BLUE_D=(11,74,166); ORANGE=(255,165,0); INK=(15,26,35); WHITE=(255,255,255)
FD="/home/user/Video/videos/rapidocms-presentation-4min/assets/fonts"
BGM="/home/user/Video/videos/stories-foodeatup-30j/audio/bgm.mp3"
A="assets"; WK="work"; os.makedirs(f"{WK}/cards",exist_ok=True); os.makedirs(f"{WK}/seq",exist_ok=True)
def F(w,s): return ImageFont.truetype(f"{FD}/Poppins-{w}.ttf", s)
VENC=["-c:v","libx264","-preset","medium","-crf","18","-pix_fmt","yuv420p","-r",str(FPS)]
def dur(f): return float(subprocess.check_output(["ffprobe","-v","error","-show_entries","format=duration","-of","csv=p=0",f]).strip())
def run(cmd,name):
    r=subprocess.run(cmd,stdout=subprocess.DEVNULL,stderr=subprocess.PIPE)
    if r.returncode: print("ERR",name,r.stderr.decode()[-1400:]); raise SystemExit(1)
    print("ok",name,round(dur(cmd[-1]),2))

# ---------- PNG card renderers ----------
def bg_blue(d):
    d.rectangle([0,0,W,H],fill=BLUE)
    # soft lighter blob top-left, darker bottom-right for depth
    for i,(cx,cy,r,col) in enumerate([(W*0.18,H*0.15,520,(60,150,255)),(W*0.9,H*0.95,620,BLUE_D)]):
        d.ellipse([cx-r,cy-r,cx+r,cy+r],fill=col)
def paste_logo_mark(im,y=110,h=92):
    m=Image.open(f"{A}/logo-mark.png").convert("RGBA"); r=h/m.height
    m=m.resize((int(m.width*r),h)); im.paste(m,((W-m.width)//2,y),m)
def measure(d,segs,f):
    return sum(d.textlength(t,font=f) for t,_ in segs)
def draw_rich_center(d,segs,y,f):
    tot=measure(d,segs,f); x=(W-tot)//2
    for t,c in segs:
        d.text((x,y),t,font=f,fill=c); x+=d.textlength(t,font=f)

def title_card(path, lines, fs=104):
    im=Image.new("RGB",(W,H)); d=ImageDraw.Draw(im); bg_blue(d)
    im2=Image.new("RGBA",(W,H),(0,0,0,0)); paste_logo_mark(im2); im.paste(im2,(0,0),im2)
    f=F("800",fs); lh=int(fs*1.18); total=lh*len(lines); y=(H-total)//2+40
    for ln in lines:
        draw_rich_center(d,ln,y,f); y+=lh
    # orange underline accent
    uw=360; d.rounded_rectangle([(W-uw)//2,y+6,(W+uw)//2,y+18],6,fill=ORANGE)
    im.save(path)

def pill(path, items, fs=46, pad=30, gap=26, icon_col=ORANGE):
    # items: list of (text, dotcolor|None). Renders a rounded white pill with colored dots.
    f=F("700",fs); tmp=Image.new("RGBA",(10,10)); dd=ImageDraw.Draw(tmp)
    widths=[];
    for t,dc in items:
        w=dd.textlength(t,font=f)+(fs+10 if dc else 0); widths.append(w)
    tw=sum(widths)+gap*(len(items)-1); Wp=int(tw+pad*2); Hp=int(fs+pad*1.6)
    im=Image.new("RGBA",(Wp,Hp),(0,0,0,0)); d=ImageDraw.Draw(im)
    d.rounded_rectangle([0,0,Wp-1,Hp-1],Hp//2,fill=(255,255,255,242))
    x=pad; cy=Hp//2
    for (t,dc),w in zip(items,widths):
        if dc:
            rr=fs*0.32; d.ellipse([x,cy-rr,x+2*rr,cy+rr],fill=dc); x+=fs+10
        d.text((x,cy-fs*0.62),t,font=f,fill=INK); x+=dd.textlength(t,font=f)+gap
    im.save(path)

def big_number(path, num, sub):
    im=Image.new("RGBA",(W,H),(0,0,0,0)); d=ImageDraw.Draw(im)
    f1=F("800",240); f2=F("700",64)
    tw=d.textlength(num,font=f1); tw2=d.textlength(sub,font=f2)
    pw=int(max(tw,tw2)+180); px=(W-pw)//2; py=int(H*0.30)-60; ph=470
    d.rounded_rectangle([px,py,px+pw,py+ph],48,fill=(15,26,35,225))
    d.text(((W-tw)//2,H*0.30),num,font=f1,fill=ORANGE)
    d.text(((W-tw2)//2,H*0.30+260),sub,font=f2,fill=WHITE)
    im.save(path)

def intro_frame(path):
    im=Image.new("RGB",(W,H)); d=ImageDraw.Draw(im); bg_blue(d)
    ov=Image.new("RGBA",(W,H),(0,0,0,0))
    m=Image.open(f"{A}/logo-mark.png").convert("RGBA"); h=300; r=h/m.height
    m=m.resize((int(m.width*r),h)); ov.paste(m,((W-m.width)//2,int(H*0.26)),m)
    im.paste(ov,(0,0),ov)
    d2=ImageDraw.Draw(im); f=F("800",120)
    t="FoodEatUp"; tw=d2.textlength(t,font=f); d2.text(((W-tw)//2,int(H*0.62)),t,font=f,fill=WHITE)
    fs=F("600",50); s="Une infinité de solutions pour gérer votre restaurant"
    sw=d2.textlength(s,font=fs); d2.text(((W-sw)//2,int(H*0.62)+150),s,font=fs,fill=(220,235,255))
    im.save(path)

def outro_frame(path):
    im=Image.new("RGB",(W,H)); d=ImageDraw.Draw(im); bg_blue(d)
    ov=Image.new("RGBA",(W,H),(0,0,0,0))
    m=Image.open(f"{A}/logo-mark.png").convert("RGBA"); h=230; r=h/m.height
    m=m.resize((int(m.width*r),h)); ov.paste(m,((W-m.width)//2,int(H*0.16)),m)
    im.paste(ov,(0,0),ov)
    d=ImageDraw.Draw(im)
    f=F("800",130); t="FoodEatUp"; tw=d.textlength(t,font=f); d.text(((W-tw)//2,int(H*0.40)),t,font=f,fill=WHITE)
    fs=F("600",52); s="Une infinité de solutions pour gérer votre restaurant"
    sw=d.textlength(s,font=fs); d.text(((W-sw)//2,int(H*0.40)+165),s,font=fs,fill=(220,235,255))
    im.save(path)

def cta_card(path):
    # transparent overlay: "14 jours gratuits" pill + url
    im=Image.new("RGBA",(W,H),(0,0,0,0)); d=ImageDraw.Draw(im)
    f=F("800",70); t="14 jours gratuits, sans carte bancaire"
    tw=d.textlength(t,font=f); d.text(((W-tw)//2,int(H*0.70)),t,font=f,fill=WHITE)
    fu=F("800",92); u="foodeatup.fr"
    uw=d.textlength(u,font=fu); pad=44
    d.rounded_rectangle([(W-uw)//2-pad,int(H*0.80)-16,(W+uw)//2+pad,int(H*0.80)+118],60,fill=ORANGE)
    d.text(((W-uw)//2,int(H*0.80)),u,font=fu,fill=WHITE)
    im.save(path)

def question_card(path):
    im=Image.new("RGB",(W,H)); d=ImageDraw.Draw(im); bg_blue(d)
    im2=Image.new("RGBA",(W,H),(0,0,0,0)); paste_logo_mark(im2,y=140,h=84); im.paste(im2,(0,0),im2)
    d=ImageDraw.Draw(im); f=F("800",108)
    lines=[[("Et si tout tenait",WHITE)],[("dans ",WHITE),("une seule plateforme",ORANGE),(" ?",WHITE)]]
    lh=int(108*1.2); y=(H-lh*2)//2+30
    for ln in lines: draw_rich_center(d,ln,y,f); y+=lh
    im.save(path)

# ---- render all cards ----
title_card(f"{WK}/cards/t2.png",[[("Vos stocks, ",WHITE),("en temps réel",ORANGE)]])
title_card(f"{WK}/cards/t3.png",[[("Vos factures, ",WHITE)],[("fini la saisie",ORANGE)]])
title_card(f"{WK}/cards/t4.png",[[("Prêt pour le contrôle",WHITE)],[("d'hygiène",ORANGE)]])
title_card(f"{WK}/cards/t5.png",[[("De la salle ",WHITE),("à la cuisine",ORANGE)]])
title_card(f"{WK}/cards/t6.png",[[("Votre site de commande",WHITE)],[("en ",WHITE),("10 minutes",ORANGE)]])
pill(f"{WK}/cards/p_predibot.png",[("PrédiBot vous prévient avant la rupture",ORANGE)])
pill(f"{WK}/cards/p_ocr.png",[("L'OCR lit, extrait, met à jour vos prix",BLUE)])
pill(f"{WK}/cards/p_haccp.png",[("Températures",BLUE),("Traçabilité",BLUE),("Étiquettes DLC",BLUE)])
pill(f"{WK}/cards/p_qr.png",[("Commande par QR de table",BLUE)])
pill(f"{WK}/cards/p_kds.png",[("Chaque ticket au bon poste",ORANGE)])
pill(f"{WK}/cards/p_site.png",[("Votre carte, vos couleurs",ORANGE)])
big_number(f"{WK}/cards/n_6h.png","6 h","gagnées chaque semaine")
intro_frame(f"{WK}/cards/intro.png")
outro_frame(f"{WK}/cards/outro.png")
cta_card(f"{WK}/cards/cta.png")
question_card(f"{WK}/cards/q1.png")
print("cards rendered")

# ---------- clip builders ----------
def kb(image, d, overlays, out, zoom=True):
    """overlays: list of dict(png,x,y,scale(h)|None,tin,tout,fin,fout)."""
    inp=["-loop","1","-t",f"{d:.2f}","-i",image]
    for o in overlays: inp+=["-loop","1","-t",f"{d:.2f}","-i",o["png"]]
    fr=int(d*FPS)
    if zoom:
        base=(f"[0:v]scale={int(W*1.2)}:{int(H*1.2)}:force_original_aspect_ratio=increase,"
              f"crop={int(W*1.2)}:{int(H*1.2)},zoompan=z='min(zoom+0.0006,1.09)':d={fr}:"
              f"x='iw/2-(iw/zoom/2)':y='ih/2-(ih/zoom/2)':s={W}x{H}:fps={FPS},setsar=1[b0];")
    else:
        base=f"[0:v]scale={W}:{H},setsar=1[b0];"
    fc=base; prev="[b0]"
    for i,o in enumerate(overlays,1):
        lab=f"[o{i}]"; s=f"[{i}:v]format=rgba"
        if o.get("scale"): s+=f",scale=-1:{o['scale']}"
        if o.get("fin") is not None: s+=f",fade=t=in:st={o['fin'][0]}:d={o['fin'][1]}:alpha=1"
        if o.get("fout") is not None: s+=f",fade=t=out:st={o['fout'][0]}:d={o['fout'][1]}:alpha=1"
        fc+=s+lab+";"
        en=f":enable='between(t,{o['tin']},{o['tout']})'" if (o['tin']>0 or o['tout']<d-0.01) else ""
        nl=f"[b{i}]"; fc+=f"{prev}{lab}overlay={o['x']}:{o['y']}{en}{nl};"; prev=nl
    fc=fc.rstrip(";");
    run(["ffmpeg","-y"]+inp+["-filter_complex",fc,"-map",prev,"-t",f"{d:.2f}"]+VENC+[out],os.path.basename(out))

def still(png,d,out,zoom=True): kb(png,d,[],out,zoom=zoom)

def overlay_vid(base,d,overlays,out):
    """Overlay PNGs (with fade/enable) on an existing base video."""
    inp=["-i",base]
    for o in overlays: inp+=["-loop","1","-t",f"{d:.2f}","-i",o["png"]]
    fc="[0:v]setsar=1[b0];"; prev="[b0]"
    for i,o in enumerate(overlays,1):
        lab=f"[o{i}]"; s=f"[{i}:v]format=rgba"
        if o.get("scale"): s+=f",scale=-1:{o['scale']}"
        if o.get("fin") is not None: s+=f",fade=t=in:st={o['fin'][0]}:d={o['fin'][1]}:alpha=1"
        if o.get("fout") is not None: s+=f",fade=t=out:st={o['fout'][0]}:d={o['fout'][1]}:alpha=1"
        fc+=s+lab+";"
        en=f":enable='between(t,{o['tin']},{o['tout']})'" if (o['tin']>0 or o['tout']<d-0.01) else ""
        nl=f"[b{i}]"; fc+=f"{prev}{lab}overlay={o['x']}:{o['y']}{en}{nl};"; prev=nl
    fc=fc.rstrip(";")
    run(["ffmpeg","-y"]+inp+["-filter_complex",fc,"-map",prev,"-t",f"{d:.2f}"]+VENC+[out],os.path.basename(out))

def jarvis_text_png(path,text,color,fs=54,weight="700"):
    im=Image.new("RGBA",(W,160),(0,0,0,0)); d=ImageDraw.Draw(im); f=F(weight,fs)
    tw=d.textlength(text,font=f); d.text(((W-tw)//2,40),text,font=f,fill=color)
    im.save(path)

def concat_parts(parts,out):
    lst=out+".txt"; open(lst,"w").write("".join(f"file '{os.path.basename(p)}'\n" for p in parts))
    run(["ffmpeg","-y","-f","concat","-safe","0","-i",lst,"-c","copy",out],"concat "+os.path.basename(out))

MASC=lambda n:f"{A}/{n}"
# S0 intro (logo FIRST)
still(f"{WK}/cards/intro.png",3.0,f"{WK}/seq/s0.mp4")
# S1 hook: hero scene 7s + question card 4.5s
kb(f"{A}/hero-backoffice.png",7.0,[],f"{WK}/seq/s1a.mp4")
still(f"{WK}/cards/q1.png",4.5,f"{WK}/seq/s1b.mp4",zoom=False)
concat_parts([f"{WK}/seq/s1a.mp4",f"{WK}/seq/s1b.mp4"],f"{WK}/seq/s1.mp4")
# S2 stocks 18s: card 2.8 (overlay) over stocks KB + mascot + pill
kb(f"{A}/screen-stocks-laptop.png",18.0,[
   {"png":f"{WK}/cards/t2.png","x":0,"y":0,"tin":0,"tout":3.0,"fout":(2.6,0.4)},
   {"png":MASC("mascotte-stock.png"),"x":"W-w-70","y":"H-h-30","scale":640,"tin":3.2,"tout":18,"fin":(3.2,0.5)},
   {"png":f"{WK}/cards/p_predibot.png","x":"(W-w)/2","y":"96","tin":8.5,"tout":18,"fin":(8.5,0.4)},
  ],f"{WK}/seq/s2.mp4")
# S3 OCR 16s
kb(f"{A}/gen-ocr-facture.jpg",16.0,[
   {"png":f"{WK}/cards/t3.png","x":0,"y":0,"tin":0,"tout":3.0,"fout":(2.6,0.4)},
   {"png":f"{WK}/cards/n_6h.png","x":0,"y":0,"tin":9.5,"tout":16,"fin":(9.5,0.5)},
  ],f"{WK}/seq/s3.mp4")
# S4 HACCP 17s
kb(f"{A}/hero-stockvision.png",17.0,[
   {"png":f"{WK}/cards/t4.png","x":0,"y":0,"tin":0,"tout":3.0,"fout":(2.6,0.4)},
   {"png":MASC("mascotte-chef.png"),"x":"70","y":"H-h-20","scale":660,"tin":3.2,"tout":17,"fin":(3.2,0.5)},
   {"png":f"{WK}/cards/p_haccp.png","x":"(W-w)/2","y":"96","tin":8.5,"tout":17,"fin":(8.5,0.4)},
  ],f"{WK}/seq/s4.mp4")
# S5 salle+jarvis 20s: card 2.8 + QR 5.2 + KDS 4.5 + Jarvis 7.5
still(f"{WK}/cards/t5.png",2.8,f"{WK}/seq/s5a.mp4",zoom=False)
kb(f"{A}/photo-qr-scan.jpg",5.2,[{"png":f"{WK}/cards/p_qr.png","x":"(W-w)/2","y":"96","tin":0.8,"tout":5.2,"fin":(0.8,0.4)}],f"{WK}/seq/s5b.mp4")
kb(f"{A}/gen-kds-cuisine.jpg",4.5,[{"png":f"{WK}/cards/p_kds.png","x":"(W-w)/2","y":"96","tin":0.5,"tout":4.5,"fin":(0.5,0.4)}],f"{WK}/seq/s5c.mp4")
# Jarvis: dark bg + 5 animated bars (drawbox) base, then PNG text overlays
jd=7.5; bars=5; bw=46; bgap=40; total=bars*bw+(bars-1)*bgap; x0=(W-total)//2; cy=H//2-40
boxes=""
for i in range(bars):
    ph=i*0.7; bx=x0+i*(bw+bgap)
    h_expr=f"abs(sin(t*3.4+{ph:.2f}))*260+40"
    boxes+=f"drawbox=x={bx}:y='({cy}-(({h_expr})/2))':w={bw}:h='{h_expr}':color=0x25A0FF@0.95:t=fill,"
run(["ffmpeg","-y","-f","lavfi","-i",f"color=c=0x0F1A23:s={W}x{H}:d={jd}:r={FPS}","-filter_complex",
     f"[0:v]{boxes.rstrip(',')},setsar=1[v]","-map","[v]","-t",f"{jd}"]+VENC+[f"{WK}/seq/s5d_base.mp4"],"jarvis-base")
jarvis_text_png(f"{WK}/cards/j_title.png","Jarvis — commis vocal",WHITE,54,"800")
jarvis_text_png(f"{WK}/cards/j_l1.png","— Jarvis, sors deux kilos de tomates.",(255,192,96),50,"700")
jarvis_text_png(f"{WK}/cards/j_l2.png","— C'est fait, et c'est tracé.",WHITE,54,"700")
overlay_vid(f"{WK}/seq/s5d_base.mp4",jd,[
   {"png":f"{WK}/cards/j_title.png","x":"(W-w)/2","y":cy-260,"tin":0,"tout":jd,"fin":(0.2,0.4)},
   {"png":f"{WK}/cards/j_l1.png","x":"(W-w)/2","y":cy+210,"tin":0.8,"tout":4.2,"fin":(0.8,0.3),"fout":(3.9,0.3)},
   {"png":f"{WK}/cards/j_l2.png","x":"(W-w)/2","y":cy+210,"tin":4.4,"tout":jd,"fin":(4.4,0.3)},
  ],f"{WK}/seq/s5d.mp4")
concat_parts([f"{WK}/seq/s5a.mp4",f"{WK}/seq/s5b.mp4",f"{WK}/seq/s5c.mp4",f"{WK}/seq/s5d.mp4"],f"{WK}/seq/s5.mp4")
# S6 site 16s
kb(f"{A}/gen-site-tablette.jpg",16.0,[
   {"png":f"{WK}/cards/t6.png","x":0,"y":0,"tin":0,"tout":3.0,"fout":(2.6,0.4)},
   {"png":MASC("mascotte-copilote.png"),"x":"W-w-70","y":"H-h-20","scale":640,"tin":3.2,"tout":16,"fin":(3.2,0.5)},
   {"png":f"{WK}/cards/p_site.png","x":"(W-w)/2","y":"96","tin":8.5,"tout":16,"fin":(8.5,0.4)},
  ],f"{WK}/seq/s6.mp4")
# S7 outro 13s: outro frame + CTA overlay
kb(f"{WK}/cards/outro.png",13.0,[{"png":f"{WK}/cards/cta.png","x":0,"y":0,"tin":3.0,"tout":13,"fin":(3.0,0.6)}],f"{WK}/seq/s7.mp4",zoom=False)
print("sequences built")

# durations map
D={s:dur(f"{WK}/seq/{s}.mp4") for s in ["s0","s1","s2","s3","s4","s5","s6","s7"]}
json.dump(D,open(f"{WK}/durations.json","w"),indent=2); print("D",D)
