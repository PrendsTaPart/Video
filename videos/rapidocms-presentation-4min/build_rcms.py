#!/usr/bin/env python3
"""RapidoCMS 4min frames 16:9 (1920x1080). Light brand (#29ABE2) chapters + dark 'Astuce chat Claude' frames.
Chapter-intro frames leave a medallion slot for Mika (overlaid at assembly)."""
from PIL import Image, ImageDraw, ImageFont, ImageFilter
import os
os.chdir(os.path.dirname(os.path.abspath(__file__)))
W,H=1920,1080
BG=(247,250,252); BLUE=(41,171,226); GREEN=(72,168,80); PURPLE=(120,80,192)
NAVY=(23,42,69); INK=(60,72,92); MUTED=(120,133,150); WHITE=(255,255,255); DARK=(14,21,38)
FD="assets/fonts"
def F(n,s): return ImageFont.truetype(os.path.join(FD,n),s)
P800=lambda s:F("Poppins-800.ttf",s); P700=lambda s:F("Poppins-700.ttf",s); P600=lambda s:F("Poppins-600.ttf",s); P400=lambda s:F("Poppins-400.ttf",s)
os.makedirs("frames",exist_ok=True)
logo=Image.open("assets/rapidocms/logo-rapidocms.png").convert("RGBA")
PW,PH,PX,PY=470,660,180,340
border=Image.open("../foodeatup-tutoriel-5min/assets/avatar/border.png").convert("RGBA")

def wrap(dr,t,f,mw):
    out=[]
    for para in t.split("\n"):
        cur=""
        for w in para.split():
            s=(cur+" "+w).strip()
            if dr.textbbox((0,0),s,font=f)[2]<=mw: cur=s
            else: out.append(cur); cur=w
        out.append(cur)
    return out
def fit(img,bw,bh):
    r=min(bw/img.width,bh/img.height); return img.resize((max(1,int(img.width*r)),max(1,int(img.height*r))),Image.LANCZOS)
def load(p):
    if not p.startswith("assets") and not p.startswith(".."): p="assets/rapidocms/"+p
    return Image.open(p).convert("RGBA")

def bg_light():
    im=Image.new("RGBA",(W,H),BG+(255,)); g=Image.new("RGBA",(W,H),(0,0,0,0)); gd=ImageDraw.Draw(g)
    gd.ellipse([W-460,-200,W+220,320],fill=BLUE+(22,)); gd.ellipse([-220,H-380,360,H+180],fill=GREEN+(16,))
    im.alpha_composite(g.filter(ImageFilter.GaussianBlur(90))); return im

def header(im,pill,col=BLUE):
    lw=250; lh=int(logo.height*lw/logo.width); im.alpha_composite(fit(logo,lw,90),(60,44))
    d=ImageDraw.Draw(im); f=P700(34); tw=d.textbbox((0,0),pill,font=f)[2]; pw,ph=tw+48,58; px,py=W-60-pw,54
    d.rounded_rectangle([px,py,px+pw,py+ph],29,fill=col+(255,)); d.text((px+pw/2,py+ph/2),pill,font=f,fill=WHITE,anchor="mm")

def browsercard(im,imgs,box):
    x,y,w,h=box
    card=Image.new("RGBA",(w,h),(0,0,0,0)); ImageDraw.Draw(card).rounded_rectangle([0,0,w-1,h-1],26,fill=WHITE+(255,))
    sh=Image.new("RGBA",(w+80,h+80),(0,0,0,0)); ImageDraw.Draw(sh).rounded_rectangle([40,52,40+w,52+h],26,fill=(23,42,69,55))
    im.alpha_composite(sh.filter(ImageFilter.GaussianBlur(24)),(x-40,y-40)); im.alpha_composite(card,(x,y))
    d=ImageDraw.Draw(im)
    for i,cx in enumerate([x+32,x+66,x+100]): d.ellipse([cx-9,y+25,cx+9,y+43],fill=[(255,95,86),(255,189,46),(39,201,63)][i]+(255,))
    ax,ay,aw,ah=x+22,y+64,w-44,h-86
    if len(imgs)==1:
        im2=fit(imgs[0],aw,ah); im.alpha_composite(im2,(ax+(aw-im2.width)//2,ay+(ah-im2.height)//2))
    else:
        gap=16; cw=(aw-gap)//2
        for i,g in enumerate(imgs[:2]):
            im2=fit(g,cw,ah); im.alpha_composite(im2,(ax+i*(cw+gap)+(cw-im2.width)//2,ay+(ah-im2.height)//2))

def textpanel(im,eyebrow,title,sub,mcp,x=80):
    d=ImageDraw.Draw(im)
    d.text((x,300),eyebrow.upper(),font=P700(34),fill=BLUE,anchor="lm")
    f=P800(58); y=350
    for l in wrap(d,title,f,690): d.text((x,y+36),l,font=f,fill=NAVY,anchor="lm"); y+=72
    d.rounded_rectangle([x,y+6,x+90,y+16],5,fill=GREEN+(255,)); y+=52
    fs=P600(36)
    for l in wrap(d,sub,fs,700): d.text((x,y+24),l,font=fs,fill=INK,anchor="lm"); y+=52
    if mcp:
        d.text((x,H-90),"MCP · "+mcp,font=P600(26),fill=MUTED,anchor="lm")

# ---- chapter/plain frame ----
def chapter(sid,eyebrow,title,sub,imgs,mcp="",pill="RapidoCMS",avatar=False):
    im=bg_light(); header(im,pill)
    textpanel(im,eyebrow,title,sub,mcp, x=(720 if avatar else 80))
    if imgs: browsercard(im,[load(x) for x in imgs],(840,150,1010,810))
    if avatar: im.alpha_composite(border,(PX,PY))
    im.convert("RGB").save(f"frames/{sid}.png"); print(sid)

# ---- hook (persona) ----
def hook():
    im=bg_light(); header(im,"communication"); d=ImageDraw.Draw(im)
    for i,l in enumerate(wrap(d,"Facebook, LinkedIn,\nInstagram, TikTok…\ntout seul ?",P800(62),720)):
        d.text((80,320+i*76),l,font=P800(62),fill=NAVY,anchor="lm")
    d.text((80,640),"RapidoCMS s'en occupe.",font=P600(40),fill=BLUE,anchor="lm")
    p=fit(load("perso-stresse.jpg"),760,820)
    m=Image.new("L",p.size,0); ImageDraw.Draw(m).rounded_rectangle([0,0,p.width-1,p.height-1],40,fill=255)
    px,py=1120,140
    sh=Image.new("RGBA",(p.width+80,p.height+80),(0,0,0,0)); ImageDraw.Draw(sh).rounded_rectangle([40,52,40+p.width,52+p.height],40,fill=(23,42,69,60))
    im.alpha_composite(sh.filter(ImageFilter.GaussianBlur(24)),(px-40,py-40)); im.paste(p,(px,py),m)
    im.convert("RGB").save("frames/hook.png"); print("hook")

# ---- MCP star frame ----
def mcp_frame():
    im=bg_light(); header(im,"⭐ le tournant",GREEN); d=ImageDraw.Draw(im)
    d.text((80,250),"CONNECTER VOTRE IA",font=P700(34),fill=BLUE,anchor="lm")
    d.text((80,320),"Le tournant",font=P800(66),fill=NAVY,anchor="lm")
    # big URL
    url="cms.rapidosoftware.com/mcp"; f=P800(46); tw=d.textbbox((0,0),url,font=f)[2]; pw,ph=tw+70,96
    d.rounded_rectangle([80,430,80+pw,430+ph],20,fill=BLUE+(255,)); d.text((80+pw/2,430+ph/2),url,font=f,fill=WHITE,anchor="mm")
    d.text((80,580),"Compatible avec votre IA :",font=P600(34),fill=INK,anchor="lm")
    # 3 logos
    x=80; y=650
    for lg,bw in [("logo-claude.png",240),("logo-mistral.jpg",150),("logo-openai.png",210)]:
        im2=fit(load(lg),bw,80); im.alpha_composite(im2,(x,y)); x+=im2.width+50
    hero=fit(load("assets-generes/hero-mcp.jpg"),620,780); im.alpha_composite(hero,(1230,150))
    d.text((80,H-90),"MCP · list_connected_accounts",font=P600(26),fill=MUTED,anchor="lm")
    im.convert("RGB").save("frames/mcp.png"); print("mcp")

# ---- Astuce chat Claude (dark) ----
def astuce(sid,n,title,prompt,result):
    im=Image.new("RGBA",(W,H),DARK+(255,)); d=ImageDraw.Draw(im)
    g=Image.new("RGBA",(W,H),(0,0,0,0)); ImageDraw.Draw(g).ellipse([-200,-200,400,400],fill=BLUE+(40,)); im.alpha_composite(g.filter(ImageFilter.GaussianBlur(120)))
    d.text((80,90),f"ASTUCE DU CHEF #{n}",font=P700(34),fill=(230,150,60),anchor="lm")
    d.text((80,150),title,font=P800(52),fill=WHITE,anchor="lm")
    # Claude chat panel left
    cl=fit(load("logo-claude.png"),210,60);
    # recolor claude logo white? keep; place on dark works if logo has transparency. Put on a chip.
    d.rounded_rectangle([80,260,80+250,260+70],16,fill=(30,40,60,255)); im.alpha_composite(cl,(96,266))
    # user bubble
    bx,by,bw=80,370,820; f=P600(34); lines=wrap(d,prompt,f,bw-60); bh=len(lines)*46+50
    d.rounded_rectangle([bx,by,bx+bw,by+bh],24,fill=(37,49,73,255))
    yy=by+28
    for l in lines: d.text((bx+30,yy),l,font=f,fill=(220,228,240),anchor="lm"); yy+=46
    # check
    cy=by+bh+40; d.ellipse([80,cy,80+52,cy+52],fill=GREEN+(255,)); d.line([94,cy+26,104,cy+38],fill=WHITE,width=6); d.line([104,cy+38,126,cy+14],fill=WHITE,width=6)
    d.text((150,cy+26),"Exécuté par votre IA",font=P700(36),fill=GREEN,anchor="lm")
    # result card right
    x,y,w,h=1000,180,840,720
    card=Image.new("RGBA",(w,h),(0,0,0,0)); ImageDraw.Draw(card).rounded_rectangle([0,0,w-1,h-1],24,fill=WHITE+(255,))
    im.alpha_composite(card,(x,y)); r=fit(load(result),w-40,h-40); im.alpha_composite(r,(x+(w-r.width)//2,y+(h-r.height)//2))
    d.text((x,y-40),"Résultat dans RapidoCMS",font=P600(30),fill=(180,195,215),anchor="lm")
    im.convert("RGB").save(f"frames/{sid}.png"); print(sid)

# ---- outro ----
def outro():
    im=bg_light(); header(im,"Academy",GREEN); d=ImageDraw.Draw(im)
    d.text((80,300),"RAPIDOCMS",font=P700(38),fill=BLUE,anchor="lm")
    for i,l in enumerate(wrap(d,"Votre com',\npilotée en parlant.",P800(70),700)): d.text((80,380+i*82),l,font=P800(70),fill=NAVY,anchor="lm")
    url="cms.rapidosoftware.com"; f=P700(46); tw=d.textbbox((0,0),url,font=f)[2]; pw,ph=tw+80,96
    d.rounded_rectangle([80,600,80+pw,600+ph],48,fill=BLUE+(255,)); d.text((80+pw/2,648),url,font=f,fill=WHITE,anchor="mm")
    d.text((80,760),"Réservez votre démo",font=P600(38),fill=INK,anchor="lm")
    p=fit(load("perso-heureux.jpg"),640,780); im.alpha_composite(p,(1230,150))
    im.alpha_composite(border,(PX+1160,PY)) if False else None
    im.convert("RGB").save("frames/outro.png"); print("outro")

# build all
hook()
chapter("intro","présentation","Pilotez toute\nvotre communication","En parlant, tout simplement, à votre IA.",[],"", "RapidoCMS", avatar=True)
chapter("reseaux","Chapitre 2 · Réseaux","Connectez vos réseaux","Facebook, LinkedIn, TikTok. Instagram passe par Facebook.",["config-facebook.png","config-linkedin.png"],"list_connected_accounts")
mcp_frame()
astuce("astuce1",1,"Vérifiez vos comptes","Liste mes comptes connectés et confirme mes accès.","config-linkedin.png")
chapter("generer","Chapitre 4 · Visuels","Générez & rangez\nvos visuels","Une description → une image HD, rangée en bibliothèque.",["bibliotheque-upload.png","exemples-posts-instagram.jpg"],"generate_image · upload_file_tool")
astuce("astuce2",2,"10 visuels d'un coup","Génère 10 visuels HD pour ma promo, sans faute.","exemples-posts-instagram.jpg")
chapter("planifier","Chapitre 5 · Publication","Créez & planifiez\nvos posts","Date : année-mois-jour · Heure : heure-minute-seconde.",["creation-post-apercu.png","calendrier-planification.png"],"create_draft_tool · schedule_draft_tool")
astuce("astuce3",3,"Un mois calé en 1 phrase","10 posts, 3 réseaux, un par jour à 10h00.","calendrier-planification.png")
chapter("campagnes","Chapitre 6 · Campagnes","Campagnes & analyse","Regroupez vos posts, suivez j'aime, engagement, portée.",["campagne-creation.png","campagne-stats.png"],"create_campagne · ingishts_campagne")
astuce("astuce4",4,"Analyse + reco","Analyse ma campagne et donne-moi 3 recommandations.","campagne-stats.png")
chapter("pilotage","Chapitre 7 · Pilotage","Pilotez au quotidien","Calendrier, historique, stats. Visez 3 posts/semaine/réseau.",["calendrier-stats.jpg","historique-publications.png"],"list_scheduled_posts · post_insights")
outro()
print("ALL RCMS FRAMES DONE")
