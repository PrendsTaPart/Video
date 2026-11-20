import React from 'react';
import {AbsoluteFill, Audio, Img, OffthreadVideo, Sequence, interpolate, spring, staticFile, useCurrentFrame, useVideoConfig, Easing} from 'remotion';
import '@fontsource/poppins/600.css';
import '@fontsource/poppins/800.css';
import '@fontsource/poppins/900.css';
import {episode, scenes, DUREE} from './data/episode';

// Charte de la série FoodEatUp « Mes projets ».
const C = {nuit: '#0F1A23', surf: '#16242F', bleu: '#007BFF', orange: '#FFA500', creme: '#FCF9E6', gris: '#AEB8C2', or: '#C9A45C'};
const police = 'Poppins, sans-serif';
const clamp = {extrapolateLeft: 'clamp', extrapolateRight: 'clamp'} as const;
const ease = Easing.bezier(0.22, 1, 0.36, 1);
const FPS = episode.fps;
const s2f = (s: number) => Math.round(s * FPS);

// Texte avec mots surlignés « *mot* ».
const Surligne: React.FC<{texte: string}> = ({texte}) => (
  <>
    {texte.split(/(\*[^*]+\*)/).map((p, i) =>
      p.startsWith('*') ? (
        <span key={i} style={{background: C.orange, color: '#000', padding: '0 18px', borderRadius: 18, boxDecorationBreak: 'clone', WebkitBoxDecorationBreak: 'clone'}}>{p.slice(1, -1)}</span>
      ) : (
        <span key={i}>{p}</span>
      ),
    )}
  </>
);

const Entre: React.FC<{d: number; children: React.ReactNode; style?: React.CSSProperties; dist?: number}> = ({d, children, style, dist = 50}) => {
  const f = useCurrentFrame();
  const e = interpolate(f, [d, d + 10], [0, 1], {...clamp, easing: ease});
  return <div style={{opacity: e, transform: `translateY(${(1 - e) * dist}px)`, ...style}}>{children}</div>;
};

const Label: React.FC<{texte: string}> = ({texte}) => {
  const f = useCurrentFrame();
  const s = spring({frame: f, fps: FPS, config: {damping: 12}});
  return (
    <div style={{position: 'absolute', top: 210, width: '100%', display: 'flex', justifyContent: 'center', transform: `scale(${0.7 + 0.3 * s})`, opacity: Math.min(1, s * 1.5)}}>
      <span style={{fontFamily: police, fontWeight: 800, fontSize: 58, background: C.bleu, color: '#fff', borderRadius: 26, padding: '12px 40px', boxShadow: '0 12px 0 rgba(0,0,0,.35)'}}>{texte}</span>
    </div>
  );
};

const Chip: React.FC<{texte: string; d: number; couleur?: string}> = ({texte, d, couleur = 'rgba(255,255,255,.12)'}) => (
  <Entre d={d} dist={30} style={{display: 'inline-block', margin: 10}}>
    <span style={{display: 'inline-block', fontFamily: police, fontWeight: 600, fontSize: 40, color: C.creme, background: couleur, border: '2px solid rgba(255,255,255,.25)', borderRadius: 30, padding: '10px 28px'}}>{texte}</span>
  </Entre>
);

// Téléphone qui joue une vidéo déjà produite (sans le son).
const Telephone: React.FC<{src: string; debut: number; largeur: number; top: number}> = ({src, debut, largeur, top}) => {
  const f = useCurrentFrame();
  const e = interpolate(f, [0, 14], [0, 1], {...clamp, easing: ease});
  const h = largeur * 16 / 9;
  return (
    <div style={{position: 'absolute', left: '50%', top, width: largeur, height: h, marginLeft: -largeur / 2, borderRadius: 46, overflow: 'hidden', background: '#05080b', boxShadow: '0 40px 80px rgba(0,0,0,.6), 0 0 0 6px #2a3a48', transform: `translateY(${(1 - e) * 200}px) scale(${0.92 + 0.08 * e})`, opacity: e}}>
      <OffthreadVideo src={staticFile(src)} startFrom={s2f(debut)} muted style={{width: '100%', height: '100%', objectFit: 'cover'}} />
    </div>
  );
};

const Fond: React.FC = () => (
  <AbsoluteFill style={{background: `radial-gradient(1200px 900px at 50% 38%, #163049 0%, ${C.nuit} 62%)`}}>
    <AbsoluteFill style={{inset: -200, backgroundImage: `url(${staticFile('toque.png')})`, backgroundSize: 180, opacity: 0.035, transform: 'rotate(-12deg)'}} />
  </AbsoluteFill>
);

const Accroche: React.FC = () => {
  const s = scenes.accroche;
  return (
    <AbsoluteFill>
      <OffthreadVideo src={staticFile('carte.mp4')} startFrom={s2f(1)} muted style={{width: '100%', height: '100%', objectFit: 'cover', filter: 'brightness(.3) blur(8px)', transform: 'scale(1.08)'}} />
      <AbsoluteFill style={{justifyContent: 'center', alignItems: 'center', padding: '0 70px'}}>
        {s.lignes.map((l, i) => (
          <Entre key={l} d={4 + i * 9} style={{fontFamily: police, fontWeight: 900, fontSize: 104, lineHeight: 1.25, color: '#fff', textAlign: 'center', textShadow: '0 6px 30px rgba(0,0,0,.7)'}}>
            <Surligne texte={l} />
          </Entre>
        ))}
      </AbsoluteFill>
    </AbsoluteFill>
  );
};

const Restaurant: React.FC = () => {
  const f = useCurrentFrame();
  const s = scenes.restaurant;
  const z = interpolate(f, [0, s2f(s.t[1] - s.t[0])], [1.05, 1.15]);
  return (
    <AbsoluteFill>
      <Img src={staticFile('pergola.jpg')} style={{width: '100%', height: '100%', objectFit: 'cover', transform: `scale(${z})`}} />
      <AbsoluteFill style={{background: 'linear-gradient(180deg, rgba(15,26,35,.2), rgba(15,26,35,.55) 45%, rgba(15,26,35,.95))'}} />
      <AbsoluteFill style={{justifyContent: 'flex-end', alignItems: 'center', paddingBottom: 330}}>
        <Entre d={4}><Img src={staticFile('logo-villa-beach.png')} style={{width: 260, height: 260}} /></Entre>
        <Entre d={10} style={{fontFamily: police, fontWeight: 900, fontSize: 120, color: '#fff', marginTop: 10}}>{s.nom}</Entre>
        <Entre d={16} style={{fontFamily: police, fontWeight: 600, fontSize: 48, color: C.or, marginTop: 6}}>{s.lieu}</Entre>
        <Entre d={22} style={{fontFamily: police, fontWeight: 600, fontSize: 44, color: C.creme, marginTop: 16}}>{s.sous}</Entre>
      </AbsoluteFill>
    </AbsoluteFill>
  );
};

const Carte: React.FC = () => {
  const s = scenes.carte;
  return (
    <AbsoluteFill>
      <Fond />
      <Label texte={s.label} />
      <Telephone src={s.video} debut={s.debutVideo} largeur={560} top={360} />
      <div style={{position: 'absolute', bottom: 180, width: '100%', textAlign: 'center', padding: '0 60px'}}>
        {s.chips.map((c, i) => <Chip key={c} texte={c} d={12 + i * 8} couleur={i === 0 ? 'rgba(255,165,0,.25)' : undefined} />)}
      </div>
    </AbsoluteFill>
  );
};

const Communication: React.FC = () => {
  const f = useCurrentFrame();
  const s = scenes.communication;
  const w = 290, h = w * 16 / 9, gap = 22;
  return (
    <AbsoluteFill>
      <Fond />
      <Label texte={s.label} />
      <div style={{position: 'absolute', top: 340, left: (1080 - 3 * w - 2 * gap) / 2, width: 3 * w + 2 * gap, display: 'flex', flexWrap: 'wrap', gap}}>
        {s.videos.map((v, i) => {
          const e = interpolate(f, [4 + i * 3, 16 + i * 3], [0, 1], {...clamp, easing: ease});
          return (
            <div key={v} style={{width: w, height: h * 0.62, borderRadius: 22, overflow: 'hidden', opacity: e, transform: `scale(${0.8 + 0.2 * e})`, boxShadow: '0 10px 30px rgba(0,0,0,.5)'}}>
              <OffthreadVideo src={staticFile(v)} startFrom={s2f(1.5 + (i % 3))} muted style={{width: '100%', height: '100%', objectFit: 'cover'}} />
            </div>
          );
        })}
      </div>
      <div style={{position: 'absolute', bottom: 150, width: '100%', textAlign: 'center', padding: '0 50px'}}>
        <Entre d={30} style={{fontFamily: police, fontWeight: 900, fontSize: 120, color: '#fff', lineHeight: 1}}><Surligne texte={`*${s.grand}*`} /></Entre>
        <div style={{marginTop: 20}}>{s.chips.map((c, i) => <Chip key={c} texte={c} d={40 + i * 8} />)}</div>
      </div>
    </AbsoluteFill>
  );
};

const Reseaux: React.FC = () => {
  const s = scenes.reseaux;
  return (
    <AbsoluteFill>
      <Fond />
      <Label texte={s.label} />
      <Telephone src={s.video} debut={s.debutVideo} largeur={500} top={350} />
      <div style={{position: 'absolute', bottom: 170, width: '100%', textAlign: 'center', padding: '0 50px'}}>
        <div>{s.reseaux.map((r, i) => <Chip key={r} texte={r} d={10 + i * 6} couleur="rgba(0,123,255,.3)" />)}</div>
        <Entre d={40} style={{fontFamily: police, fontWeight: 800, fontSize: 52, color: C.creme, marginTop: 24}}>{s.note}</Entre>
      </div>
    </AbsoluteFill>
  );
};

const Stocks: React.FC = () => {
  const s = scenes.stocks;
  return (
    <AbsoluteFill>
      <Fond />
      <Label texte={s.label} />
      <AbsoluteFill style={{alignItems: 'center', paddingTop: 400, padding: '400px 80px 0'}}>
        <Entre d={6} style={{fontFamily: police, fontWeight: 900, fontSize: 112, color: '#fff', textAlign: 'center', lineHeight: 1.1}}><Surligne texte={`*${s.grand}*`} /></Entre>
        <Entre d={12} style={{fontFamily: police, fontWeight: 600, fontSize: 46, color: C.gris, marginTop: 18, marginBottom: 50}}>suivies en temps réel</Entre>
        {s.alertes.map(([nom, etat], i) => (
          <Entre key={nom} d={22 + i * 8} style={{width: '100%', marginBottom: 22}}>
            <div style={{display: 'flex', justifyContent: 'space-between', alignItems: 'center', background: C.surf, borderRadius: 26, padding: '28px 36px', borderLeft: '10px solid #FF4D4F'}}>
              <span style={{fontFamily: police, fontWeight: 800, fontSize: 44, color: '#fff'}}>{nom}</span>
              <span style={{fontFamily: police, fontWeight: 800, fontSize: 34, color: '#000', background: '#FF4D4F', borderRadius: 30, padding: '8px 22px'}}>{etat}</span>
            </div>
          </Entre>
        ))}
        <Entre d={52} style={{marginTop: 30}}>
          <span style={{display: 'inline-block', fontFamily: police, fontWeight: 800, fontSize: 42, background: C.orange, color: '#000', borderRadius: 30, padding: '16px 34px'}}>{s.commande}</span>
        </Entre>
      </AbsoluteFill>
    </AbsoluteFill>
  );
};

const Haccp: React.FC = () => {
  const s = scenes.haccp;
  return (
    <AbsoluteFill>
      <Fond />
      <Label texte={s.label} />
      <AbsoluteFill style={{padding: '380px 80px 0'}}>
        {s.equipements.map((e, i) => (
          <Entre key={e} d={6 + i * 6} style={{marginBottom: 18}}>
            <div style={{display: 'flex', alignItems: 'center', gap: 24, background: C.surf, borderRadius: 24, padding: '22px 32px'}}>
              <span style={{fontFamily: police, fontWeight: 900, fontSize: 40, color: '#000', background: '#2ECC71', borderRadius: 14, padding: '4px 16px'}}>°C</span>
              <span style={{fontFamily: police, fontWeight: 700, fontSize: 44, color: '#fff'}}>{e}</span>
            </div>
          </Entre>
        ))}
        <div style={{textAlign: 'center', marginTop: 40}}>{s.chips.map((c, i) => <Chip key={c} texte={c} d={40 + i * 7} couleur={i === 0 ? 'rgba(255,165,0,.25)' : undefined} />)}</div>
      </AbsoluteFill>
    </AbsoluteFill>
  );
};

const Fin: React.FC = () => {
  const f = useCurrentFrame();
  const s = scenes.fin;
  const k = spring({frame: f - 22, fps: FPS, config: {damping: 10}});
  return (
    <AbsoluteFill>
      <Fond />
      <AbsoluteFill style={{alignItems: 'center', justifyContent: 'center', padding: '0 70px', textAlign: 'center'}}>
        <Entre d={2}><div style={{background: '#fff', borderRadius: 50, padding: '30px 56px', boxShadow: '0 20px 50px rgba(0,0,0,.5)'}}><Img src={staticFile('foodeatup.png')} style={{height: 110}} /></div></Entre>
        <Entre d={10} style={{fontFamily: police, fontWeight: 900, fontSize: 84, color: '#fff', lineHeight: 1.25, marginTop: 50}}><Surligne texte={s.phrase} /></Entre>
        <div style={{marginTop: 40, transform: `scale(${Math.max(0, k)})`}}>
          <span style={{display: 'inline-block', background: C.orange, color: '#000', fontFamily: police, fontWeight: 900, fontSize: 150, lineHeight: 1, borderRadius: 40, padding: '34px 60px', boxShadow: '0 18px 0 #000'}}>{episode.motCle}</span>
        </div>
        <Entre d={34} style={{fontFamily: police, fontWeight: 800, fontSize: 50, color: C.creme, marginTop: 50}}>{s.appel}</Entre>
        <Entre d={42} style={{marginTop: 40}}>
          <span style={{fontFamily: police, fontWeight: 700, fontSize: 32, color: C.gris, border: '3px solid #2a3a48', borderRadius: 30, padding: '10px 28px'}}>Épisode {episode.numero} · {episode.serie}</span>
        </Entre>
      </AbsoluteFill>
    </AbsoluteFill>
  );
};

export const Episode: React.FC = () => {
  const f = useCurrentFrame();
  const {durationInFrames} = useVideoConfig();
  const seq = (t: number[], el: React.ReactNode, k: string) => (
    <Sequence key={k} from={s2f(t[0])} durationInFrames={s2f(t[1] - t[0])}>{el}</Sequence>
  );
  const coupes = [scenes.restaurant, scenes.carte, scenes.communication, scenes.reseaux, scenes.stocks, scenes.haccp, scenes.fin].map((x) => s2f(x.t[0]));
  const flash = Math.max(0, ...coupes.map((c) => interpolate(f - c, [0, 2, 8], [0, 0.35, 0], clamp)));
  const m = episode.musique;
  return (
    <AbsoluteFill style={{background: C.nuit}}>
      {seq(scenes.accroche.t, <Accroche />, 'a')}
      {seq(scenes.restaurant.t, <Restaurant />, 'r')}
      {seq(scenes.carte.t, <Carte />, 'c')}
      {seq(scenes.communication.t, <Communication />, 'co')}
      {seq(scenes.reseaux.t, <Reseaux />, 're')}
      {seq(scenes.stocks.t, <Stocks />, 's')}
      {seq(scenes.haccp.t, <Haccp />, 'h')}
      {seq(scenes.fin.t, <Fin />, 'f')}
      <AbsoluteFill style={{background: '#fff', opacity: flash, pointerEvents: 'none'}} />
      {/* étiquette de l'épisode, en haut */}
      <div style={{position: 'absolute', top: 90, width: '100%', display: 'flex', justifyContent: 'center', opacity: f < s2f(scenes.fin.t[0]) ? 1 : 0}}>
        <span style={{fontFamily: police, fontWeight: 800, fontSize: 28, background: C.orange, color: '#000', borderRadius: 40, padding: '12px 26px'}}>ÉPISODE {episode.numero} · VILLA BEACH</span>
      </div>
      {/* barre de progression */}
      <div style={{position: 'absolute', left: 0, bottom: 0, height: 12, width: `${(f / durationInFrames) * 100}%`, background: C.bleu}} />
      <Audio src={staticFile(m.fichier)} trimBefore={s2f(m.debut)} volume={(fr) => m.volume * Math.min(interpolate(fr, [0, FPS], [0, 1], clamp), interpolate(fr, [s2f(DUREE) - 1.5 * FPS, s2f(DUREE) - 1], [1, 0], clamp))} />
    </AbsoluteFill>
  );
};
