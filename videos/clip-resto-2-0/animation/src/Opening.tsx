import React from 'react';
import {AbsoluteFill, Img, interpolate, staticFile, useCurrentFrame} from 'remotion';
import {C, FONT, easeInOutCubic, easeOutCubic, protection} from './brand';
import {ToqueLayer} from './Toque';

const WORD = 'FOODEATUP';
// Index 1 and 2 are the double-O of FOOD; they are what closes into the
// infinity sign, so they are rendered separately from the other letters.
const OO = [1, 2];

// A single continuous lemniscate stroke — "d'un seul geste, en trait continu".
const INFINITY_D =
  'M 8,40 C 8,12 44,12 60,40 C 76,68 112,68 112,40 C 112,12 76,12 60,40 C 44,68 8,68 8,40 Z';

export const Opening: React.FC = () => {
  const f = useCurrentFrame();

  // 1. Toque layers superimpose from the four corners.
  const toque = (i: number) =>
    easeOutCubic(interpolate(f, [6 + i * 13, 74 + i * 13], [0, 1], {
      extrapolateLeft: 'clamp', extrapolateRight: 'clamp',
    }));

  // 2. The wordmark composes letter by letter.
  const letterIn = (i: number) =>
    interpolate(f, [78 + i * 7, 96 + i * 7], [0, 1], {
      extrapolateLeft: 'clamp', extrapolateRight: 'clamp',
    });

  // 3. The double-O closes into the infinity sign, drawn in one stroke.
  const draw = easeInOutCubic(
    interpolate(f, [152, 196], [0, 1], {extrapolateLeft: 'clamp', extrapolateRight: 'clamp'}),
  );
  const ooFade = interpolate(f, [152, 174], [1, 0], {
    extrapolateLeft: 'clamp', extrapolateRight: 'clamp',
  });
  // 4. Resolve to the real lockup so the mark is always brand-accurate.
  const lockup = interpolate(f, [198, 216], [0, 1], {
    extrapolateLeft: 'clamp', extrapolateRight: 'clamp',
  });

  // 5. Badge slogan: the 8 in a rounded blue pill, discreet pop.
  const badge = interpolate(f, [206, 224], [0, 1], {
    extrapolateLeft: 'clamp', extrapolateRight: 'clamp',
  });
  const badgePop = 1 + 0.16 * Math.sin(Math.PI * Math.min(1, badge));

  // 6. Signature line in cream.
  const sig = easeOutCubic(
    interpolate(f, [228, 264], [0, 1], {extrapolateLeft: 'clamp', extrapolateRight: 'clamp'}),
  );

  // 7. Orange liseré sweeps left -> right to launch the first shot.
  const sweep = interpolate(f, [288, 333], [-0.12, 1.15], {
    extrapolateLeft: 'clamp', extrapolateRight: 'clamp',
  });

  const LOGO_W = 760;
  const LOGO_H = 168;
  const pad = protection(LOGO_H, LOGO_W); // 76 px
  const LEFT = 170; // placement à gauche prioritaire

  return (
    <AbsoluteFill style={{backgroundColor: C.marine, fontFamily: FONT, overflow: 'hidden'}}>
      {/* toque motif, translucent layers from the four corners */}
      {[0, 1, 2, 3].map((c) => (
        <ToqueLayer key={c} corner={c as 0 | 1 | 2 | 3} progress={toque(c)} size={620} opacity={0.11} />
      ))}
      <ToqueLayer corner={0} progress={toque(1)} size={380} opacity={0.07} />
      <ToqueLayer corner={2} progress={toque(3)} size={440} opacity={0.07} />

      {/* logo block, left-aligned, protection zone respected */}
      <div style={{position: 'absolute', left: LEFT, top: 388, width: LOGO_W + pad * 2, padding: pad}}>
        <div style={{position: 'relative', height: LOGO_H, width: LOGO_W}}>
          {/* letter-by-letter composition (fades out once the lockup lands) */}
          <div
            style={{
              position: 'absolute', inset: 0, display: 'flex', alignItems: 'center',
              opacity: 1 - lockup,
            }}
          >
            {WORD.split('').map((ch, i) => {
              const p = letterIn(i);
              const isOO = OO.includes(i);
              return (
                <span
                  key={i}
                  style={{
                    fontSize: 132,
                    fontWeight: 800,
                    letterSpacing: '-0.02em',
                    color: C.bleu,
                    opacity: (isOO ? ooFade : 1) * p,
                    transform: `translateY(${(1 - easeOutCubic(p)) * 26}px)`,
                    display: 'inline-block',
                  }}
                >
                  {ch}
                </span>
              );
            })}
          </div>

          {/* the double-O closing into the infinity sign, one continuous stroke */}
          <svg
            width={240} height={168} viewBox="0 0 120 80"
            style={{position: 'absolute', left: 118, top: 0, opacity: (1 - lockup) * (draw > 0 ? 1 : 0)}}
          >
            <path
              d={INFINITY_D}
              fill="none"
              stroke={C.bleu}
              strokeWidth={13}
              strokeLinecap="round"
              pathLength={1}
              strokeDasharray={1}
              strokeDashoffset={1 - draw}
            />
          </svg>

          {/* the real lockup — never tilted, never framed, FOOD and EATUP never split */}
          <Img
            src={staticFile('logo-h-blue.png')}
            style={{
              position: 'absolute', left: 0, top: 4, width: LOGO_W, height: 'auto',
              opacity: lockup,
            }}
          />
        </div>

        {/* badge slogan: the 8 in a rounded blue pill */}
        <div
          style={{
            marginTop: 26, display: 'inline-flex', alignItems: 'center', gap: 16,
            background: C.bleu, borderRadius: 999, padding: '14px 34px',
            opacity: badge, transform: `scale(${badgePop})`, transformOrigin: 'left center',
          }}
        >
          <span style={{fontSize: 46, fontWeight: 800, color: C.noir, lineHeight: 1}}>8</span>
          <span style={{fontSize: 26, fontWeight: 600, color: C.noir, letterSpacing: '0.04em'}}>
            BOUCLES LOGICIEL
          </span>
        </div>

        {/* brand signature, cream on marine */}
        <div
          style={{
            marginTop: 30, fontSize: 40, fontWeight: 400, color: C.creme,
            opacity: sig, transform: `translateY(${(1 - sig) * 16}px)`, maxWidth: 980,
          }}
        >
          Une infinité de solutions pour gérer votre restaurant
        </div>
      </div>

      {/* orange liseré launching the first shot */}
      <div
        style={{
          position: 'absolute', top: 0, bottom: 0, left: `${sweep * 100}%`,
          width: 26, background: C.orange, boxShadow: `0 0 90px 26px ${C.orange}55`,
        }}
      />
    </AbsoluteFill>
  );
};
