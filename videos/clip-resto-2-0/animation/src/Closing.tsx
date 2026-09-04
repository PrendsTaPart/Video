import React from 'react';
import {AbsoluteFill, Img, interpolate, staticFile, useCurrentFrame} from 'remotion';
import {C, FONT, easeInOutCubic, easeOutCubic, protection} from './brand';
import {ToqueShape} from './Toque';

// 487 frames @ 30 fps = 16.23 s, starting at 152.30 s of the master.
// The music decays to silence around frame 393; the call to action must still
// be on screen for two full seconds of that silence.
export const Closing: React.FC = () => {
  const f = useCurrentFrame();

  // 1. The final-refrain image reduces to a central square that becomes the mark.
  const shrink = easeInOutCubic(
    interpolate(f, [0, 74], [0, 1], {extrapolateLeft: 'clamp', extrapolateRight: 'clamp'}),
  );
  const sq = interpolate(shrink, [0, 1], [1920, 300]);
  const radius = interpolate(shrink, [0.45, 1], [0, 150], {
    extrapolateLeft: 'clamp', extrapolateRight: 'clamp',
  });
  const imgFade = interpolate(f, [64, 86], [1, 0], {
    extrapolateLeft: 'clamp', extrapolateRight: 'clamp',
  });
  const markIn = interpolate(f, [72, 96], [0, 1], {
    extrapolateLeft: 'clamp', extrapolateRight: 'clamp',
  });

  // 2. The toque motif deploys behind the logo, in filigrane.
  const fil = easeOutCubic(
    interpolate(f, [78, 168], [0, 1], {extrapolateLeft: 'clamp', extrapolateRight: 'clamp'}),
  );
  // 3. The mark hands over to the full lockup, settled centre.
  const lockup = easeOutCubic(
    interpolate(f, [128, 164], [0, 1], {extrapolateLeft: 'clamp', extrapolateRight: 'clamp'}),
  );

  // 4. Three lines in sequence on the last chord.
  const line = (a: number) =>
    easeOutCubic(interpolate(f, [a, a + 30], [0, 1], {
      extrapolateLeft: 'clamp', extrapolateRight: 'clamp',
    }));
  const l1 = line(168); // le nom
  const l2 = line(228); // la signature de marque
  const l3 = line(300); // le bouton d'appel à l'action  (tenu jusqu'à 487)

  const LOGO_W = 700;
  const pad = protection(154, LOGO_W);

  return (
    <AbsoluteFill style={{backgroundColor: C.marine, fontFamily: FONT, overflow: 'hidden'}}>
      {/* toque motif in filigrane behind everything */}
      <div style={{position: 'absolute', inset: 0, opacity: 0.06 * fil}}>
        <div style={{position: 'absolute', left: '50%', top: '50%',
          transform: `translate(-50%,-50%) scale(${0.9 + 0.25 * fil})`}}>
          <ToqueShape size={980} color={C.bleu} />
        </div>
      </div>
      {[[-6, 12], [76, 8], [8, 74], [82, 78]].map(([x, y], i) => (
        <div key={i} style={{position: 'absolute', left: `${x}%`, top: `${y}%`, opacity: 0.05 * fil}}>
          <ToqueShape size={340} color={C.bleu} />
        </div>
      ))}

      {/* the last frame reducing to a central square */}
      <div
        style={{
          position: 'absolute', left: '50%', top: '50%',
          width: sq, height: sq, transform: 'translate(-50%,-50%)',
          borderRadius: radius, overflow: 'hidden', opacity: imgFade,
        }}
      >
        <Img
          src={staticFile('lastframe.jpg')}
          style={{width: 1920, height: 1080, objectFit: 'cover',
            position: 'absolute', left: '50%', top: '50%', transform: 'translate(-50%,-50%)'}}
        />
      </div>

      {/* ... which becomes the logomark, then the full lockup */}
      <div style={{position: 'absolute', left: '50%', top: '50%', transform: 'translate(-50%,-50%)',
        display: 'flex', flexDirection: 'column', alignItems: 'center', padding: pad}}>
        <div style={{position: 'relative', height: 260, display: 'flex', alignItems: 'center'}}>
          <Img
            src={staticFile('logo-mark-8.png')}
            style={{height: 230, opacity: markIn * (1 - lockup),
              transform: `translateY(${-90 * lockup}px)`}}
          />
          <Img
            src={staticFile('logo-h-white.png')}
            style={{position: 'absolute', left: '50%', top: '50%', width: LOGO_W,
              transform: `translate(-50%,-50%) scale(${0.94 + 0.06 * lockup})`, opacity: lockup}}
          />
        </div>

        {/* 1 — le nom */}
        <div style={{fontSize: 62, fontWeight: 800, color: C.creme, letterSpacing: '0.01em',
          opacity: l1, transform: `translateY(${(1 - l1) * 18}px)`, marginTop: 8}}>
          FoodEatUp
        </div>

        {/* 2 — la signature de marque */}
        <div style={{fontSize: 38, fontWeight: 400, color: C.creme, marginTop: 18,
          opacity: l2, transform: `translateY(${(1 - l2) * 16}px)`, textAlign: 'center'}}>
          Une infinité de solutions pour gérer votre restaurant
        </div>

        {/* 3 — l'appel à l'action, tenu deux secondes pleines sur le silence.
            Texte noir 100 % sur le bouton bleu : règle d'accessibilité de la charte. */}
        <div style={{marginTop: 46, opacity: l3, transform: `scale(${0.94 + 0.06 * l3})`,
          display: 'flex', flexDirection: 'column', alignItems: 'center'}}>
          <div style={{background: C.bleu, borderRadius: 999, padding: '26px 68px',
            fontSize: 44, fontWeight: 700, color: C.noir}}>
            Demander un devis
          </div>
          <div style={{marginTop: 22, fontSize: 30, fontWeight: 400, color: C.creme}}>
            https://site.foodeatup.com/creer-mon-devis
          </div>
        </div>
      </div>
    </AbsoluteFill>
  );
};
