import React from 'react';
import {AbsoluteFill, Img, interpolate, staticFile, useCurrentFrame} from 'remotion';
import {C, FONT, easeInOutCubic, easeOutCubic, protection} from './brand';
import {ToqueShape, ToqueLayer} from './Toque';

const WORD = 'FOODEATUP';
const OO = [1, 2];
const INFINITY_D =
  'M 8,40 C 8,12 44,12 60,40 C 76,68 112,68 112,40 C 112,12 76,12 60,40 C 44,68 8,68 8,40 Z';

// Portrait openings/closings for the 9:16, 1:1 and 4:5 cuts. The 1:1 and 4:5
// versions are vertical crops of this 1080x1920 render, so everything that
// must survive the crop is kept inside the middle 1080x1080 band.
const SAFE_TOP = 420; // top of the 1:1 crop window

export const OpeningV: React.FC = () => {
  const f = useCurrentFrame();
  const toque = (i: number) =>
    easeOutCubic(interpolate(f, [6 + i * 13, 74 + i * 13], [0, 1],
      {extrapolateLeft: 'clamp', extrapolateRight: 'clamp'}));
  const letterIn = (i: number) =>
    interpolate(f, [78 + i * 7, 96 + i * 7], [0, 1],
      {extrapolateLeft: 'clamp', extrapolateRight: 'clamp'});
  const draw = easeInOutCubic(interpolate(f, [152, 196], [0, 1],
    {extrapolateLeft: 'clamp', extrapolateRight: 'clamp'}));
  const ooFade = interpolate(f, [152, 174], [1, 0], {extrapolateLeft: 'clamp', extrapolateRight: 'clamp'});
  const lockup = interpolate(f, [198, 216], [0, 1], {extrapolateLeft: 'clamp', extrapolateRight: 'clamp'});
  const badge = interpolate(f, [206, 224], [0, 1], {extrapolateLeft: 'clamp', extrapolateRight: 'clamp'});
  const sig = easeOutCubic(interpolate(f, [228, 264], [0, 1],
    {extrapolateLeft: 'clamp', extrapolateRight: 'clamp'}));
  const sweep = interpolate(f, [288, 333], [-0.12, 1.15], {extrapolateLeft: 'clamp', extrapolateRight: 'clamp'});

  const LOGO_W = 860;
  const pad = protection(190, LOGO_W);

  return (
    <AbsoluteFill style={{backgroundColor: C.marine, fontFamily: FONT, overflow: 'hidden'}}>
      {[0, 1, 2, 3].map((c) => (
        <ToqueLayer key={c} corner={c as 0 | 1 | 2 | 3} progress={toque(c)} size={560} opacity={0.11} />
      ))}
      <div style={{position: 'absolute', left: '50%', top: SAFE_TOP + 540,
        transform: 'translate(-50%,-50%)', width: 1080, padding: pad,
        display: 'flex', flexDirection: 'column', alignItems: 'center'}}>
        <div style={{position: 'relative', height: 190, width: LOGO_W}}>
          <div style={{position: 'absolute', inset: 0, display: 'flex', alignItems: 'center',
            justifyContent: 'center', opacity: 1 - lockup}}>
            {WORD.split('').map((ch, i) => {
              const p = letterIn(i);
              return (
                <span key={i} style={{fontSize: 118, fontWeight: 800, letterSpacing: '-0.02em',
                  color: C.bleu, opacity: (OO.includes(i) ? ooFade : 1) * p,
                  transform: `translateY(${(1 - easeOutCubic(p)) * 24}px)`, display: 'inline-block'}}>
                  {ch}
                </span>
              );
            })}
          </div>
          <svg width={214} height={150} viewBox="0 0 120 80"
            style={{position: 'absolute', left: 106, top: 20, opacity: (1 - lockup) * (draw > 0 ? 1 : 0)}}>
            <path d={INFINITY_D} fill="none" stroke={C.bleu} strokeWidth={13} strokeLinecap="round"
              pathLength={1} strokeDasharray={1} strokeDashoffset={1 - draw} />
          </svg>
          <Img src={staticFile('logo-h-blue.png')}
            style={{position: 'absolute', left: '50%', top: '50%', width: LOGO_W,
              transform: 'translate(-50%,-50%)', opacity: lockup}} />
        </div>
        <div style={{marginTop: 34, display: 'inline-flex', alignItems: 'center', gap: 16,
          background: C.bleu, borderRadius: 999, padding: '16px 38px', opacity: badge,
          transform: `scale(${1 + 0.16 * Math.sin(Math.PI * Math.min(1, badge))})`}}>
          <span style={{fontSize: 50, fontWeight: 800, color: C.noir, lineHeight: 1}}>8</span>
          <span style={{fontSize: 28, fontWeight: 600, color: C.noir, letterSpacing: '0.04em'}}>
            BOUCLES LOGICIEL
          </span>
        </div>
        <div style={{marginTop: 34, fontSize: 46, fontWeight: 400, color: C.creme, opacity: sig,
          transform: `translateY(${(1 - sig) * 16}px)`, textAlign: 'center', lineHeight: 1.35}}>
          Une infinité de solutions<br />pour gérer votre restaurant
        </div>
      </div>
      <div style={{position: 'absolute', top: 0, bottom: 0, left: `${sweep * 100}%`, width: 22,
        background: C.orange, boxShadow: `0 0 90px 26px ${C.orange}55`}} />
    </AbsoluteFill>
  );
};

export const ClosingV: React.FC = () => {
  const f = useCurrentFrame();
  const shrink = easeInOutCubic(interpolate(f, [0, 74], [0, 1],
    {extrapolateLeft: 'clamp', extrapolateRight: 'clamp'}));
  const sq = interpolate(shrink, [0, 1], [1920, 300]);
  const radius = interpolate(shrink, [0.45, 1], [0, 150], {extrapolateLeft: 'clamp', extrapolateRight: 'clamp'});
  const imgFade = interpolate(f, [64, 86], [1, 0], {extrapolateLeft: 'clamp', extrapolateRight: 'clamp'});
  const markIn = interpolate(f, [72, 96], [0, 1], {extrapolateLeft: 'clamp', extrapolateRight: 'clamp'});
  const fil = easeOutCubic(interpolate(f, [78, 168], [0, 1], {extrapolateLeft: 'clamp', extrapolateRight: 'clamp'}));
  const lockup = easeOutCubic(interpolate(f, [128, 164], [0, 1], {extrapolateLeft: 'clamp', extrapolateRight: 'clamp'}));
  const line = (a: number) => easeOutCubic(interpolate(f, [a, a + 30], [0, 1],
    {extrapolateLeft: 'clamp', extrapolateRight: 'clamp'}));
  const l1 = line(168), l2 = line(228), l3 = line(300);

  const CY = SAFE_TOP + 540; // centre of the 1:1 crop window
  const LOGO_W = 780;

  return (
    <AbsoluteFill style={{backgroundColor: C.marine, fontFamily: FONT, overflow: 'hidden'}}>
      <div style={{position: 'absolute', left: '50%', top: CY, transform: 'translate(-50%,-50%)',
        opacity: 0.06 * fil}}>
        <ToqueShape size={980} color={C.bleu} />
      </div>
      <div style={{position: 'absolute', left: '50%', top: CY - 250, width: sq, height: sq,
        transform: 'translate(-50%,-50%)', borderRadius: radius, overflow: 'hidden', opacity: imgFade}}>
        <Img src={staticFile('lastframe-v.jpg')}
          style={{width: 1080, height: 1920, objectFit: 'cover', position: 'absolute',
            left: '50%', top: '50%', transform: 'translate(-50%,-50%)'}} />
      </div>
      <div style={{position: 'absolute', left: '50%', top: CY, transform: 'translate(-50%,-50%)',
        display: 'flex', flexDirection: 'column', alignItems: 'center', width: 1000}}>
        <div style={{position: 'relative', height: 300, display: 'flex', alignItems: 'center'}}>
          <Img src={staticFile('logo-mark-8.png')}
            style={{height: 250, opacity: markIn * (1 - lockup), transform: `translateY(${-110 * lockup}px)`}} />
          <Img src={staticFile('logo-h-white.png')}
            style={{position: 'absolute', left: '50%', top: '50%', width: LOGO_W,
              transform: `translate(-50%,-50%) scale(${0.94 + 0.06 * lockup})`, opacity: lockup}} />
        </div>
        <div style={{fontSize: 70, fontWeight: 800, color: C.creme, opacity: l1,
          transform: `translateY(${(1 - l1) * 18}px)`}}>FoodEatUp</div>
        <div style={{fontSize: 42, fontWeight: 400, color: C.creme, marginTop: 22, opacity: l2,
          transform: `translateY(${(1 - l2) * 16}px)`, textAlign: 'center', lineHeight: 1.35}}>
          Une infinité de solutions<br />pour gérer votre restaurant
        </div>
        <div style={{marginTop: 54, opacity: l3, transform: `scale(${0.94 + 0.06 * l3})`,
          display: 'flex', flexDirection: 'column', alignItems: 'center'}}>
          <div style={{background: C.bleu, borderRadius: 999, padding: '28px 66px',
            fontSize: 46, fontWeight: 700, color: C.noir}}>Demander un devis</div>
          <div style={{marginTop: 24, fontSize: 28, fontWeight: 400, color: C.creme, textAlign: 'center'}}>
            https://site.foodeatup.com/creer-mon-devis
          </div>
        </div>
      </div>
    </AbsoluteFill>
  );
};
