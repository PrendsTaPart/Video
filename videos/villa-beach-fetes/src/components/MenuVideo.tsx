import React from 'react';
import {AbsoluteFill, interpolate, random, useCurrentFrame, useVideoConfig, spring} from 'remotion';
import {charte, fetes, restaurant} from '../data/fetes';
import {bebas, clamp, cormorant, ease, Grain, KenBurns, Lisere, Logo, Musique, Particules, TEMPS, Titre, useApparition} from './commun';

// Plan de la vidéo, en temps de 0,5 s (120 BPM). Noël : intro 6 temps, 3 sections de 8 temps, final 10 temps.
// Nouvel An : intro 4 temps, 3 sections de 6 temps, prix 6 temps, compte à rebours 6 temps, final 6 temps.
const plan = (compte: boolean) => {
  const T = TEMPS;
  if (!compte) {
    const intro = 6 * T, sec = 8 * T;
    return {intro, sec, prix: [intro + 3 * sec, 40 * T] as const, compte: null, final: [intro + 3 * sec, 40 * T] as const};
  }
  const intro = 4 * T, sec = 6 * T;
  const p0 = intro + 3 * sec;
  return {intro, sec, prix: [p0, p0 + 6 * T] as const, compte: [p0 + 6 * T, p0 + 12 * T] as const, final: [p0 + 12 * T, 40 * T] as const};
};

const Ligne: React.FC<{debut: number; fin: number; children: React.ReactNode; style?: React.CSSProperties; dist?: number}> = ({debut, fin, children, style, dist}) => {
  const a = useApparition(debut, fin, dist);
  return <div style={{...style, ...a}}>{children}</div>;
};

export const MenuVideo: React.FC<{fete: 'noel' | 'nye'}> = ({fete: cle}) => {
  const fete = fetes[cle];
  const f = useCurrentFrame();
  const {height, width, fps} = useVideoConfig();
  const carre = height < 1600; // version 4:5
  const k = carre ? 0.84 : 1; // échelle des textes
  const P = plan(fete.compteARebours);
  const centreY = height / 2;

  return (
    <AbsoluteFill style={{background: fete.fond, overflow: 'hidden'}}>
      {/* Fonds : image d'ouverture puis une photo par section, en Ken Burns lent */}
      <KenBurns src={fete.hero} debut={0} fin={P.intro} fond={fete.fond} voile={0.42} />
      {fete.sections.map((s, i) => (
        <KenBurns key={s.titre} src={s.photo} debut={P.intro + i * P.sec} fin={P.intro + (i + 1) * P.sec} sens={i % 2 ? -1 : 1} fond={fete.fond} voile={0.72} />
      ))}
      <KenBurns src={fete.hero} debut={P.prix[0]} fin={40 * TEMPS} sens={-1} fond={fete.fond} voile={0.8} />
      <Particules n={carre ? 55 : 75} />

      {/* Intro : logo, surtitre, accroche */}
      <AbsoluteFill style={{alignItems: 'center', justifyContent: 'center', padding: '0 90px'}}>
        <Ligne debut={4} fin={P.intro} style={{marginBottom: 40 * k}}>
          <Logo taille={(carre ? 170 : 220)} />
        </Ligne>
        <Ligne debut={TEMPS} fin={P.intro}>
          <Titre taille={64 * k} espacement={0.32}>{fete.surtitre}</Titre>
        </Ligne>
        <Ligne debut={2 * TEMPS} fin={P.intro} style={{marginTop: 36 * k}}>
          <div style={{fontFamily: cormorant, fontStyle: 'italic', fontWeight: 500, fontSize: 92 * k, lineHeight: 1.08, color: charte.creme, textAlign: 'center', textWrap: 'balance', textShadow: '0 4px 30px rgba(0,0,0,.6)'}}>{fete.accroche}</div>
        </Ligne>
      </AbsoluteFill>

      {/* Sections : titre puis les trois plats, un par temps */}
      {fete.sections.map((s, i) => {
        const d = P.intro + i * P.sec, fin = d + P.sec;
        return (
          <AbsoluteFill key={s.titre} style={{alignItems: 'center', justifyContent: 'center', padding: '0 90px'}}>
            <Ligne debut={d} fin={fin}>
              <Titre taille={150 * k} espacement={0.22}>{s.titre}</Titre>
            </Ligne>
            <Ligne debut={d + TEMPS} fin={fin} style={{width: 140, height: 2, background: charte.or, margin: `${34 * k}px 0 ${44 * k}px`}}>{null}</Ligne>
            {s.plats.map((p, j) => (
              <Ligne key={p} debut={d + (j + 1) * TEMPS + (fete.compteARebours ? 0 : TEMPS)} fin={fin} style={{marginBottom: 34 * k, maxWidth: width - 200}}>
                <div style={{fontFamily: cormorant, fontWeight: 600, fontSize: 62 * k, lineHeight: 1.1, color: charte.creme, textAlign: 'center', textWrap: 'balance', textShadow: '0 3px 24px rgba(0,0,0,.7)'}}>{p}</div>
              </Ligne>
            ))}
          </AbsoluteFill>
        );
      })}

      {/* Pastille de prix et détails */}
      <AbsoluteFill style={{alignItems: 'center', justifyContent: 'center', padding: '0 90px'}}>
        {(() => {
          const [d, fin] = P.prix;
          const s = spring({frame: f - d, fps, config: {damping: 14, mass: 0.7}});
          const o = interpolate(f, [d, d + 6, fin - 8, fin], [0, 1, 1, 0], clamp);
          const enHaut = fete.compteARebours ? 0 : -centreY * (carre ? 0.2 : 0.28);
          return (
            <div style={{opacity: o, display: 'flex', flexDirection: 'column', alignItems: 'center', transform: `translateY(${enHaut}px)`}}>
              <div style={{transform: `scale(${0.6 + 0.4 * s})`, border: `2px solid ${charte.or}`, borderRadius: 999, padding: `${26 * k}px ${64 * k}px ${20 * k}px`, background: 'rgba(0,0,0,.35)'}}>
                <Titre taille={(fete.prix.length > 8 ? 96 : 150) * k} couleur={charte.or} espacement={0.08}>{fete.prix}</Titre>
              </div>
              {fete.details.map((t, j) => (
                <Ligne key={t} debut={d + (j + 1) * TEMPS} fin={fin} style={{marginTop: (j ? 14 : 44) * k}}>
                  <div style={{fontFamily: cormorant, fontStyle: 'italic', fontWeight: 500, fontSize: 70 * k, color: charte.creme, textAlign: 'center', lineHeight: 1.1}}>{t}</div>
                </Ligne>
              ))}
            </div>
          );
        })()}
      </AbsoluteFill>

      {/* Compte à rebours 3-2-1 puis confettis dorés (Nouvel An) */}
      {P.compte && <CompteARebours debut={P.compte[0]} fin={P.compte[1]} />}
      {P.compte && <Confettis debut={P.final[0]} />}

      {/* Final : appel à réserver, coordonnées, logo */}
      <AbsoluteFill style={{alignItems: 'center', justifyContent: 'flex-end', paddingBottom: (carre ? 110 : 230)}}>
        {(() => {
          const [d0] = P.final;
          const d = fete.compteARebours ? d0 : d0 + 4 * TEMPS;
          return (
            <>
              {fete.compteARebours && (
                <Ligne debut={d} fin={9999} style={{marginBottom: 'auto', marginTop: carre ? 150 : 330}}>
                  <Logo taille={carre ? 150 : 210} />
                </Ligne>
              )}
              <Ligne debut={d} fin={9999}>
                <div style={{background: charte.or, padding: `${22 * k}px ${54 * k}px ${16 * k}px`, borderRadius: 6}}>
                  <Titre taille={78 * k} couleur={fete.fond} espacement={0.12}>{fete.cta}</Titre>
                </div>
              </Ligne>
              <Ligne debut={d + TEMPS} fin={9999} style={{marginTop: 34 * k}}>
                <div style={{fontFamily: bebas, fontSize: 64 * k, letterSpacing: '0.12em', color: charte.creme, textAlign: 'center'}}>{restaurant.telephone}</div>
              </Ligne>
              <Ligne debut={d + 2 * TEMPS} fin={9999} style={{marginTop: 10 * k}}>
                <div style={{fontFamily: cormorant, fontStyle: 'italic', fontSize: 44 * k, color: charte.creme, opacity: 0.9, textAlign: 'center', lineHeight: 1.2}}>
                  {restaurant.nom} · {restaurant.lieu}<br />{restaurant.adresse}
                </div>
              </Ligne>
              {fete.compteARebours && (
                <Ligne debut={d + TEMPS} fin={9999} style={{position: 'absolute', top: carre ? 380 : 640, width: '100%'}}>
                  <Titre taille={(carre ? 100 : 130)} couleur={charte.or} espacement={0.2}>Bonne année</Titre>
                </Ligne>
              )}
            </>
          );
        })()}
      </AbsoluteFill>

      {/* Logo discret en haut pendant les sections */}
      <Ligne debut={P.intro} fin={P.prix[0]} style={{position: 'absolute', top: carre ? 70 : 110, width: '100%', display: 'flex', justifyContent: 'center'}}>
        <Logo taille={carre ? 90 : 120} />
      </Ligne>

      <Grain />
      <Lisere />
      <Musique fete={fete} />
    </AbsoluteFill>
  );
};

const CompteARebours: React.FC<{debut: number; fin: number}> = ({debut, fin}) => {
  const f = useCurrentFrame();
  const {height} = useVideoConfig();
  if (f < debut || f >= fin) return null;
  const pas = (fin - debut) / 3;
  const i = Math.floor((f - debut) / pas);
  const u = (f - debut - i * pas) / pas;
  const z = interpolate(u, [0, 0.25, 1], [1.5, 1, 0.92], {...clamp, easing: ease});
  const o = interpolate(u, [0, 0.12, 0.8, 1], [0, 1, 1, 0], clamp);
  return (
    <AbsoluteFill style={{alignItems: 'center', justifyContent: 'center'}}>
      <div style={{fontFamily: bebas, fontSize: height * 0.36, color: charte.or, opacity: o, transform: `scale(${z})`, textShadow: `0 0 60px ${charte.or}88`}}>{3 - i}</div>
    </AbsoluteFill>
  );
};

const Confettis: React.FC<{debut: number}> = ({debut}) => {
  const f = useCurrentFrame();
  const {width, height} = useVideoConfig();
  const t = f - debut;
  if (t < 0) return null;
  const flash = interpolate(t, [0, 3, 14], [0, 0.85, 0], clamp);
  const ors = ['#C9A45C', '#E6CC8A', '#A8833E', '#F2EAD6', '#D9B46A'];
  return (
    <AbsoluteFill style={{pointerEvents: 'none'}}>
      <AbsoluteFill style={{background: `radial-gradient(circle at 50% 45%, ${charte.or}, transparent 60%)`, opacity: flash}} />
      {new Array(170).fill(0).map((_, i) => {
        const a = random(`a${i}`) * Math.PI * 2;
        const v = 18 + random(`v${i}`) * 34;
        const x = width / 2 + Math.cos(a) * v * t * 0.9;
        const y = height * 0.45 + Math.sin(a) * v * t * 0.9 + 0.9 * t * t;
        const r = random(`r${i}`) * 360 + t * (8 + random(`rr${i}`) * 14);
        const w = 10 + random(`w${i}`) * 16;
        return <div key={i} style={{position: 'absolute', left: x, top: y, width: w, height: w * 0.45, background: ors[i % ors.length], transform: `rotate(${r}deg)`, opacity: interpolate(t, [0, 40, 55], [1, 1, 0], clamp)}} />;
      })}
    </AbsoluteFill>
  );
};
