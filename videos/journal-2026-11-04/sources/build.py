"""Compose un projet HyperFrames vertical 1080x1920 depuis un spec JSON.
python3 build.py spec.json sortie_dir"""
import json, os, re, shutil, subprocess, sys, html
from PIL import Image
E = os.path.dirname(os.path.abspath(__file__)) + '/..'
SRC = E + '/src'
DEP = '/home/user/stockvisionai'

def duree(f):
    return float(subprocess.run(['ffprobe','-v','error','-show_entries','format=duration','-of','csv=p=0',f],capture_output=True,text=True).stdout)

def pauses(mp3):
    err = subprocess.run(['ffmpeg','-i',mp3,'-af','silencedetect=n=-32dB:d=0.12','-f','null','-'],capture_output=True,text=True).stderr
    d=[float(x) for x in re.findall(r'silence_start: ([\d.]+)',err)]
    f=[float(x) for x in re.findall(r'silence_end: ([\d.]+)',err)]
    return [(a+b)/2 for a,b in zip(d,f)]

def phrases(t):
    t = re.sub(r'\[[^\]]+\]\s*','',t)
    return [p.strip() for p in re.findall(r'[^.!?…]+[.!?…]+',t) if p.strip()]

def chunks(p, n=7):
    w=p.split()
    if len(w)<=n: return [p]
    k=(len(w)+n-1)//n; s=(len(w)+k-1)//k
    return [' '.join(w[i:i+s]) for i in range(0,len(w),s)]

def main(spec_path, out):
    S=json.load(open(spec_path))
    a=out+'/assets'; os.makedirs(a,exist_ok=True)
    shutil.copy(DEP+'/node_modules/gsap/dist/gsap.min.js',a)
    for f in ('Manrope-Bold.ttf','Manrope-Regular.ttf'):
        shutil.copy(DEP+'/resources/fonts/print/'+f,a)
    shutil.copy(SRC+'/michael-rond.png',a+'/michael.png')
    Image.open(SRC+'/logo.webp').save(a+'/logo.png')
    shutil.copy(S['voix'],a+'/voix.mp3')
    dv=duree(a+'/voix.mp3'); D=dv+1.0
    ph=phrases(S['texte'])
    # bornes proportionnelles puis aimantées aux pauses
    tot=sum(len(p) for p in ph); ps=pauses(a+'/voix.mp3')
    b=[0.0]; acc=0
    for p in ph[:-1]:
        acc+=len(p); est=0.15+acc/tot*(dv-0.3)
        near=[x for x in ps if abs(x-est)<0.9 and x>b[-1]+0.4]
        b.append(min(near,key=lambda x:abs(x-est)) if near else est)
    b.append(dv)
    # sous-titres en morceaux
    subs=[]
    for i,p in enumerate(ph):
        for k,v in S.get('remplacer',{}).items(): p=p.replace(k,v)
        cs=chunks(p); t0,t1=b[i],b[i+1]; L=sum(len(c) for c in cs); x=t0
        for c in cs:
            y=x+(t1-t0)*len(c)/L; cc=c
            for k,v in S.get('remplacer',{}).items(): cc=cc.replace(k,v)
            subs.append((x,y,cc)); x=y
    nh=S.get('hook_phrases',1); nc=S.get('cta_phrases',2)
    t_hook=b[nh]; t_cta=b[len(ph)-nc]
    sc=S['scenes']; pas=(t_cta-t_hook)/len(sc)
    mid=b[nh:len(ph)-nc+1]
    bornes=mid if len(mid)-1==len(sc) else [t_hook+i*pas for i in range(len(sc)+1)]
    e=html.escape; col=S['couleur']; acc2=S.get('accent','#FFA500')
    media=[]; js=[]
    for i,s in enumerate(sc):
        st=bornes[i]; en=bornes[i+1]; pas=en-st
        if s['type']=='video':
            subprocess.run(['ffmpeg','-y','-loglevel','error','-ss',str(s.get('from',0)),'-i',SRC+'/'+s['src'],'-t',f'{pas+1:.2f}','-an','-vf','crop=iw*0.84:ih*0.83:iw*0.08:0,scale=1080:-2','-c:v','libx264','-crf','18','-pix_fmt','yuv420p',f'{a}/m{i}.mp4'],check=True)
            media.append(f'<div class="card" id="c{i}"><div class="vwin"><video id="v{i}" src="assets/m{i}.mp4" data-start="{st:.2f}" data-duration="{pas+0.4:.2f}" data-media-start="0" data-track-index="0" muted playsinline></video></div><p class="leg">{e(s.get("leg",""))}</p></div>')
        else:
            im=Image.open(SRC+'/'+s['src']).convert('RGB')
            y0,y1=s.get('crop',[0,im.height])
            im=im.crop((0,y0,im.width,y1)); w=900; h=int(im.height*w/im.width)
            im.resize((w,h),Image.LANCZOS).save(f'{a}/m{i}.webp','WEBP',quality=88)
            media.append(f'<div class="card" id="c{i}"><div class="iwin"><img id="i{i}" src="assets/m{i}.webp"></div><p class="leg">{e(s.get("leg",""))}</p></div>')
            if h>860: js.append(f'tl.to("#i{i}",{{y:-{h-860},duration:{max(pas-0.8,0.8):.2f},ease:"power1.inOut"}},{st+0.5:.2f});')
        js.append(f'tl.fromTo("#c{i}",{{opacity:0,y:120,rotationX:18,scale:.9}},{{opacity:1,y:0,rotationX:0,scale:1,duration:.55,ease:"power3.out"}},{st:.2f});')
        js.append(f'tl.fromTo("#w{i}",{{opacity:0,scale:.6}},{{opacity:1,scale:1,duration:.4,ease:"back.out(2.2)"}},{st+0.1:.2f});')
        js.append(f'tl.fromTo("#reflet",{{x:-400}},{{x:1400,duration:.9,ease:"power2.inOut"}},{st+0.3:.2f});')
        if i<len(sc)-1:
            js.append(f'tl.to("#c{i},#w{i}",{{opacity:0,y:-80,duration:.3}},{en-0.15:.2f});')
        else:
            js.append(f'tl.to("#c{i},#w{i}",{{opacity:0,scale:.9,duration:.35}},{t_cta-0.2:.2f});')
    mots=''.join(f'<h2 class="mot" id="w{i}">{s["mot"]}</h2>' for i,s in enumerate(sc))
    sub=''.join(f'<p class="st" id="s{i}">{e(c)}</p>' for i,(_,_,c) in enumerate(subs))
    for i,(x,y,c) in enumerate(subs):
        js.append(f'tl.fromTo("#s{i}",{{opacity:0,y:20,scale:.92}},{{opacity:1,y:0,scale:1,duration:.18}},{x:.2f});')
        js.append(f'tl.to("#s{i}",{{opacity:0,duration:.12}},{max(y-0.08,x+0.2):.2f});')
    fin=S['fin']
    finimg=''
    if fin.get('image'):
        im=Image.open(SRC+'/'+fin['image']).convert('RGB'); y0,y1=fin.get('crop',[0,im.height]); im=im.crop((0,y0,im.width,y1))
        im.resize((560,int(im.height*560/im.width)),Image.LANCZOS).save(a+'/fin.webp','WEBP',quality=88); finimg='<img class="finimg" src="assets/fin.webp">'
    photo_hook = '<img id="hookphoto" src="assets/michael.png">' if S.get('photo') else ''
    if S.get('hook_image'):
        hi=S['hook_image']; im=Image.open(SRC+'/'+hi['src']).convert('RGB'); y0,y1=hi.get('crop',[0,im.height]); im=im.crop((0,y0,im.width,y1))
        im.resize((900,int(im.height*900/im.width)),Image.LANCZOS).save(a+'/hook.webp','WEBP',quality=88)
        photo_hook += '<img id="hookshot" src="assets/hook.webp">'
    photo_fin = '<img class="finphoto" src="assets/michael.png">' if S.get('photo') else ''
    pastille = '<img id="pastille" src="assets/michael.png">' if S.get('photo') else ''
    htmlp=f'''<!doctype html><html lang="fr"><head><meta charset="UTF-8"><script src="assets/gsap.min.js"></script><style>
@font-face{{font-family:M;src:url(assets/Manrope-Bold.ttf);font-weight:800}}@font-face{{font-family:M;src:url(assets/Manrope-Regular.ttf);font-weight:500}}
*{{margin:0;padding:0;box-sizing:border-box}}html,body{{width:1080px;height:1920px;overflow:hidden;background:{S['fond']}}}
#root{{position:relative;width:1080px;height:1920px;overflow:hidden;font-family:M,sans-serif;color:#fff;background:radial-gradient(1200px 900px at 50% 30%,{col}55,{S['fond']} 70%)}}
#grille{{position:absolute;inset:0;background-image:linear-gradient(rgba(255,255,255,.05) 1px,transparent 1px),linear-gradient(90deg,rgba(255,255,255,.05) 1px,transparent 1px);background-size:60px 60px}}
#top{{position:absolute;top:70px;left:60px;right:60px;display:flex;justify-content:space-between;align-items:center}}
.badge{{font-size:30px;font-weight:800;letter-spacing:.08em;padding:12px 26px;border-radius:999px;background:{acc2};color:#111}}
#logo{{height:58px;background:#fff;border-radius:16px;padding:10px 18px}}
#hook{{position:absolute;top:330px;left:70px;right:70px;font-size:96px;font-weight:800;line-height:1.05;letter-spacing:-.02em}}
#hook em{{font-style:normal;background:{acc2};color:#111;padding:0 14px;border-radius:14px}}
#hookphoto{{position:absolute;left:50%;top:880px;width:500px;height:500px;margin-left:-250px;border-radius:999px;border:12px solid {col};box-shadow:0 30px 90px rgba(0,0,0,.5)}}
#hookshot{{position:absolute;left:90px;top:860px;width:900px;max-height:600px;object-fit:cover;object-position:top;border-radius:36px;box-shadow:0 30px 90px rgba(0,0,0,.6)}}
.mot{{position:absolute;top:210px;left:60px;right:60px;text-align:center;font-size:84px;font-weight:800;line-height:1.05;opacity:0}}
.mot span{{color:{acc2}}}
.card{{position:absolute;left:60px;top:450px;width:960px;opacity:0;perspective:1600px}}
.vwin{{width:960px;height:780px;border-radius:34px;overflow:hidden;background:#000;box-shadow:0 40px 110px rgba(0,0,0,.6);border:4px solid {col}}}
.vwin video{{width:960px;height:780px;object-fit:cover}}
.iwin{{width:960px;height:920px;border-radius:34px;overflow:hidden;background:#fff;box-shadow:0 40px 110px rgba(0,0,0,.6);border:4px solid {col};padding:0 26px;background:#0b1622}}
.iwin img{{width:900px;display:block;margin:0 auto}}
.leg{{margin-top:26px;text-align:center;font-size:34px;font-weight:500;color:#C9D6E3}}
#reflet{{position:absolute;top:300px;left:0;width:180px;height:1300px;transform:rotate(18deg);background:linear-gradient(90deg,transparent,rgba(255,255,255,.12),transparent);pointer-events:none}}
.st{{position:absolute;left:50%;top:1500px;transform:translateX(-50%);width:960px;text-align:center;font-size:52px;font-weight:800;line-height:1.2;padding:14px 24px;border-radius:22px;background:rgba(0,0,0,.66);opacity:0}}
#pastille{{position:absolute;left:60px;bottom:90px;width:150px;height:150px;border-radius:999px;border:6px solid {col};opacity:0}}
.mention{{position:absolute;right:60px;bottom:100px;font-size:24px;color:#AEB8C2;text-align:right;max-width:700px}}
#fin{{position:absolute;inset:0;background:radial-gradient(900px 900px at 50% 35%,{col},{S['fond']});display:flex;flex-direction:column;align-items:center;justify-content:flex-start;gap:30px;opacity:0;padding:170px 60px 0;text-align:center}}
#fin .big{{font-size:78px;font-weight:800;line-height:1.08}}
#fin .url{{font-size:54px;font-weight:800;background:{acc2};color:#111;padding:16px 34px;border-radius:999px}}
#fin .sous{{font-size:38px;font-weight:500;color:#E6EEF6;max-width:940px}}
.finphoto{{width:250px;height:250px;border-radius:999px;border:8px solid #fff}}
.finimg{{width:560px;border-radius:30px;box-shadow:0 30px 80px rgba(0,0,0,.45);max-height:400px;object-fit:cover;object-position:top}}
#finlogo{{height:80px;background:#fff;border-radius:20px;padding:14px 24px}}
</style></head><body>
<div id="root" data-composition-id="main" data-start="0" data-duration="{D:.2f}" data-width="1080" data-height="1920">
<div id="grille"></div>
<div id="top"><span class="badge">{e(S['badge'])}</span><img id="logo" src="assets/logo.png"></div>
<h1 id="hook">{S['hook']}</h1>{photo_hook}
{mots}{''.join(media)}<div id="reflet"></div>
{pastille}<p class="mention">{e(S.get('mention','Écrans réels de FoodEatUp'))}</p>
<div id="fin">{photo_fin}{finimg}<p class="big">{fin['big']}</p><p class="url">{e(fin['url'])}</p><p class="sous">{e(fin['sous'])}</p><img id="finlogo" src="assets/logo.png"></div>
{sub}
<audio id="voix" src="assets/voix.mp3" data-start="0" data-duration="{dv:.2f}" data-track-index="1" data-volume="1"></audio>
</div><script>
window.__timelines=window.__timelines||{{}};const tl=gsap.timeline({{paused:true}});
tl.fromTo("#hook",{{opacity:0,y:60,scale:.9}},{{opacity:1,y:0,scale:1,duration:.5,ease:"back.out(1.6)"}},0.05);
tl.fromTo("#hookphoto",{{opacity:0,scale:.3,rotation:-90}},{{opacity:1,scale:1,rotation:0,duration:.8,ease:"elastic.out(1,.6)"}},0.25);
tl.fromTo("#hookshot",{{opacity:0,y:200,rotationX:25}},{{opacity:1,y:0,rotationX:0,duration:.7,ease:"power3.out"}},0.3);
tl.to("#hook,#hookphoto,#hookshot",{{opacity:0,y:-120,duration:.35}},{t_hook-0.25:.2f});
tl.to("#pastille",{{opacity:1,duration:.4}},{t_hook:.2f});
{chr(10).join(js)}
tl.to("#fin",{{opacity:1,duration:.45}},{t_cta:.2f});
tl.fromTo("#fin > *",{{opacity:0,y:50}},{{opacity:1,y:0,stagger:.15,duration:.5,ease:"back.out(1.7)"}},{t_cta+0.1:.2f});
tl.set({{}},{{}},{D:.2f});window.__timelines["main"]=tl;
</script></body></html>'''
    # les sous-titres de la fin passent au-dessus du bloc fin : on les met après
    open(out+'/index.html','w').write(htmlp)
    json.dump({'$schema':'https://hyperframes.heygen.com/schema/hyperframes.json','paths':{'assets':'assets'}},open(out+'/hyperframes.json','w'))
    json.dump({'duree':D,'subs':subs,'t_hook':t_hook,'t_cta':t_cta},open(out+'/timing.json','w'),ensure_ascii=False)
    print(out, f'{D:.1f}s', len(subs),'sous-titres')

main(sys.argv[1],sys.argv[2])
