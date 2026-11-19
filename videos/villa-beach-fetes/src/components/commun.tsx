import React from 'react';
import {AbsoluteFill, Audio, Img, interpolate, random, staticFile, useCurrentFrame, useVideoConfig, Easing} from 'remotion';
// Polices embarquées dans le projet (pas de téléchargement au rendu).
import '@fontsource/bebas-neue/400.css';
import '@fontsource/cormorant-garamond/500.css';
import '@fontsource/cormorant-garamond/600.css';
import '@fontsource/cormorant-garamond/500-italic.css';
import {charte, tempo, Fete} from '../data/fetes';

export const bebas = "'Bebas Neue', sans-serif";
export const cormorant = "'Cormorant Garamond', serif";

// Un temps (120 BPM) en images.
export const TEMPS = Math.round((60 / tempo.bpm) * tempo.fps);

export const ease = Easing.bezier(0.22, 1, 0.36, 1);
export const clamp = {extrapolateLeft: 'clamp', extrapolateRight: 'clamp'} as const;

// Apparition : fondu + montée, puis disparition en fin de plage.
export const useApparition = (debut: number, fin: number, dist = 40) => {
  const f = useCurrentFrame();
  const entree = interpolate(f, [debut, debut + 12], [0, 1], {...clamp, easing: ease});
  const sortie = interpolate(f, [fin - 8, fin], [1, 0], clamp);
  return {opacity: Math.min(entree, sortie), transform: `translateY(${(1 - entree) * dist}px)`};
};

// Image animée en Ken Burns lent (zoom 1,04 -> 1,14 sur la plage), légèrement assombrie.
export const KenBurns: React.FC<{src: string; debut: number; fin: number; sens?: 1 | -1; fond: string; voile?: number}> = ({src, debut, fin, sens = 1, fond, voile = 0.55}) => {
  const f = useCurrentFrame();
  if (f < debut - 15 || f > fin + 15) return null;
  const p = interpolate(f, [debut - 15, fin + 15], [0, 1], clamp);
  const z = 1.04 + 0.1 * p;
  const x = sens * (p - 0.5) * 40;
  const o = Math.min(interpolate(f, [debut - 15, debut], [0, 1], clamp), interpolate(f, [fin, fin + 15], [1, 0], clamp));
  return (
    <AbsoluteFill style={{opacity: o}}>
      <Img src={staticFile(src)} style={{width: '100%', height: '100%', objectFit: 'cover', transform: `scale(${z}) translateX(${x}px)`, filter: 'saturate(1.05) contrast(1.04)'}} />
      <AbsoluteFill style={{background: fond, opacity: voile}} />
      <AbsoluteFill style={{background: `linear-gradient(180deg, ${fond}e6 0%, ${fond}00 30%, ${fond}00 65%, ${fond}f2 100%)`}} />
    </AbsoluteFill>
  );
};

// Grain argentique léger (bruit SVG qui change à chaque image).
export const Grain: React.FC = () => {
  const f = useCurrentFrame();
  const {width, height} = useVideoConfig();
  return (
    <AbsoluteFill style={{opacity: 0.09, mixBlendMode: 'overlay', pointerEvents: 'none'}}>
      <svg width={width} height={height}>
        <filter id="grain">
          <feTurbulence type="fractalNoise" baseFrequency="0.9" numOctaves={2} seed={f % 12} stitchTiles="stitch" />
          <feColorMatrix type="saturate" values="0" />
        </filter>
        <rect width="100%" height="100%" filter="url(#grain)" />
      </svg>
    </AbsoluteFill>
  );
};

// Particules dorées qui tombent doucement.
export const Particules: React.FC<{n?: number}> = ({n = 70}) => {
  const f = useCurrentFrame();
  const {width, height} = useVideoConfig();
  return (
    <AbsoluteFill style={{pointerEvents: 'none'}}>
      {new Array(n).fill(0).map((_, i) => {
        const x0 = random(`x${i}`) * width;
        const y0 = random(`y${i}`) * height;
        const v = 0.8 + random(`v${i}`) * 2.2;
        const s = 2 + random(`s${i}`) * 5;
        const y = (y0 + f * v) % (height + 40) - 20;
        const x = x0 + Math.sin(f / (30 + random(`w${i}`) * 40) + i) * 18;
        const scint = 0.35 + 0.65 * Math.abs(Math.sin(f / 9 + i * 1.7));
        return <div key={i} style={{position: 'absolute', left: x, top: y, width: s, height: s, borderRadius: '50%', background: charte.or, opacity: 0.55 * scint, boxShadow: `0 0 ${s * 3}px ${charte.or}`}} />;
      })}
    </AbsoluteFill>
  );
};

// Liseré doré fin autour de l'image.
export const Lisere: React.FC = () => (
  <AbsoluteFill style={{pointerEvents: 'none'}}>
    <div style={{position: 'absolute', inset: 26, border: `2px solid ${charte.or}`, opacity: 0.9}} />
    <div style={{position: 'absolute', inset: 36, border: `1px solid ${charte.or}`, opacity: 0.35}} />
  </AbsoluteFill>
);

// Musique libre de droits : fondu d'entrée (1 s) et de sortie (1,5 s).
export const Musique: React.FC<{fete: Fete}> = ({fete}) => {
  const {durationInFrames, fps} = useVideoConfig();
  const m = fete.musique;
  return (
    <Audio
      src={staticFile(m.fichier)}
      trimBefore={Math.round(m.debut * fps)}
      volume={(f) => m.volume * Math.min(interpolate(f, [0, fps], [0, 1], clamp), interpolate(f, [durationInFrames - 1.5 * fps, durationInFrames - 1], [1, 0], clamp))}
    />
  );
};

// Texte d'en-tête en Bebas Neue, espacement large.
export const Titre: React.FC<{children: React.ReactNode; taille: number; couleur?: string; espacement?: number; style?: React.CSSProperties}> = ({children, taille, couleur = charte.or, espacement = 0.18, style}) => (
  <div style={{fontFamily: bebas, fontSize: taille, letterSpacing: `${espacement}em`, color: couleur, lineHeight: 1, textAlign: 'center', paddingLeft: `${espacement}em`, textWrap: 'balance', ...style}}>{children}</div>
);

export const Logo: React.FC<{taille: number; style?: React.CSSProperties}> = ({taille, style}) => (
  <Img src={staticFile('logo.png')} style={{width: taille, height: taille, objectFit: 'contain', ...style}} />
);
