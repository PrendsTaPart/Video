import React from 'react';
import {AbsoluteFill, Img, interpolate, staticFile, useCurrentFrame, useVideoConfig} from 'remotion';
import {charte, fetes, restaurant} from '../data/fetes';
import {bebas, clamp, cormorant, ease, Grain, Lisere, Logo, Musique, Particules, TEMPS, Titre} from './commun';

// Teaser de 8 s (16 temps à 120 BPM) : une coupe par mesure de 2 temps, flash doré à chaque coupe.
// 0-2 accroche · 2-4 « Places » · 4-6 « limitées » · 6-9 fête + prix · 9-12 détail · 12-16 appel à réserver.
export const Teaser: React.FC<{fete: 'noel' | 'nye'}> = ({fete: cle}) => {
  const fete = fetes[cle];
  const f = useCurrentFrame();
  const {width, height} = useVideoConfig();
  const T = TEMPS;
  const cut = 2 * T;
  const idx = Math.floor(f / cut);
  const photo = fete.teaser.photos[idx % fete.teaser.photos.length];
  const u = (f % cut) / cut;
  const flash = interpolate(f % cut, [0, 2, 6], [0.22, 0.14, 0], clamp);

  // Plage d'un bloc de texte : entrée en « punch » sur le temps, sortie à la plage suivante.
  const bloc = (d: number, fin: number) => {
    const e = interpolate(f, [d, d + 6], [0, 1], {...clamp, easing: ease});
    const s = interpolate(f, [fin - 4, fin], [1, 0], clamp);
    return {opacity: Math.min(e, s), transform: `scale(${1.25 - 0.25 * e})`, display: f >= d - 1 && f < fin ? 'block' : 'none'};
  };
  const detail = fete.details[fete.details.length - 1];

  return (
    <AbsoluteFill style={{background: fete.fond, overflow: 'hidden'}}>
      <AbsoluteFill>
        <Img src={staticFile(photo)} style={{width: '100%', height: '100%', objectFit: 'cover', transform: `scale(${1.18 - 0.1 * u})`}} />
        <AbsoluteFill style={{background: `linear-gradient(180deg, ${fete.fond}dd, ${fete.fond}99 40%, ${fete.fond}f0)`}} />
      </AbsoluteFill>
      <Particules n={60} />
      <AbsoluteFill style={{background: charte.or, opacity: flash, mixBlendMode: 'screen'}} />

      <AbsoluteFill style={{alignItems: 'center', justifyContent: 'center', padding: '0 80px'}}>
        <div style={bloc(0, 2 * T)}>
          <div style={{fontFamily: cormorant, fontStyle: 'italic', fontWeight: 500, fontSize: 104, color: charte.creme, textAlign: 'center', lineHeight: 1.05}}>{fete.teaser.accroche}</div>
        </div>
        <div style={bloc(2 * T, 4 * T)}>
          <Titre taille={250} espacement={0.12}>{fete.teaser.mots[0]}</Titre>
        </div>
        <div style={bloc(4 * T, 6 * T)}>
          <Titre taille={210} espacement={0.08}>{fete.teaser.mots[1]}</Titre>
        </div>
        <div style={bloc(6 * T, 9 * T)}>
          <Titre taille={92} couleur={charte.creme} espacement={0.2}>{fete.nom}</Titre>
          <Titre taille={190} espacement={0.06} style={{marginTop: 30}}>{fete.prix.replace(' par personne', '')}</Titre>
          {fete.prix.includes('par personne') && <div style={{fontFamily: cormorant, fontStyle: 'italic', fontSize: 60, color: charte.creme, textAlign: 'center'}}>par personne</div>}
        </div>
        <div style={bloc(9 * T, 12 * T)}>
          <div style={{fontFamily: cormorant, fontStyle: 'italic', fontWeight: 500, fontSize: 96, color: charte.creme, textAlign: 'center', lineHeight: 1.1}}>{detail}</div>
        </div>
        <div style={{...bloc(12 * T, 16 * T + 1), textAlign: 'center'}}>
          <div style={{display: 'flex', justifyContent: 'center', marginBottom: 46}}><Logo taille={190} /></div>
          <div style={{background: charte.or, padding: '22px 50px 14px', borderRadius: 6, display: 'inline-block'}}>
            <Titre taille={80} couleur={fete.fond} espacement={0.12}>{fete.cta}</Titre>
          </div>
          <div style={{fontFamily: bebas, fontSize: 70, letterSpacing: '0.12em', color: charte.creme, marginTop: 34}}>{restaurant.telephone}</div>
          <div style={{fontFamily: cormorant, fontStyle: 'italic', fontSize: 46, color: charte.creme, opacity: 0.9}}>{restaurant.nom} · Lisses</div>
        </div>
      </AbsoluteFill>

      {/* Bandeau « places limitées » permanent en bas, sauf pendant l'appel final */}
      <div style={{position: 'absolute', bottom: height * 0.09, width, textAlign: 'center', opacity: f < 12 * T ? 0.95 : 0}}>
        <Titre taille={44} couleur={charte.or} espacement={0.4}>Places limitées</Titre>
      </div>

      <Grain />
      <Lisere />
      <Musique fete={fete} />
    </AbsoluteFill>
  );
};
