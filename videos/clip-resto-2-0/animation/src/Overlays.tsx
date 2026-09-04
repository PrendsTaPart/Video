import React from 'react';
import {AbsoluteFill, Img, interpolate, staticFile, useCurrentFrame} from 'remotion';
import {C} from './brand';

// White logomark flash, one eighth of a second (4 frames @ 30 fps), struck on
// the attack of the sung syllable "FoodEatUp".
export const LogoFlash: React.FC = () => {
  const f = useCurrentFrame();
  const a = interpolate(f, [0, 1, 3, 4], [0, 1, 1, 0], {
    extrapolateLeft: 'clamp', extrapolateRight: 'clamp',
  });
  return (
    <AbsoluteFill style={{justifyContent: 'center', alignItems: 'center'}}>
      <AbsoluteFill style={{backgroundColor: '#FFFFFF', opacity: a * 0.45}} />
      <Img
        src={staticFile('logo-mark-white.png')}
        style={{height: 460, opacity: a, transform: `scale(${1 + 0.06 * (1 - a)})`}}
      />
    </AbsoluteFill>
  );
};

// The double-O as an infinity sign, looping exactly once, on "huit boucles".
const D = 'M 8,40 C 8,12 44,12 60,40 C 76,68 112,68 112,40 C 112,12 76,12 60,40 C 44,68 8,68 8,40 Z';
export const InfinityLoop: React.FC = () => {
  const f = useCurrentFrame();
  const draw = interpolate(f, [0, 30], [0, 1], {extrapolateLeft: 'clamp', extrapolateRight: 'clamp'});
  const out = interpolate(f, [34, 45], [1, 0], {extrapolateLeft: 'clamp', extrapolateRight: 'clamp'});
  return (
    <AbsoluteFill style={{justifyContent: 'center', alignItems: 'center', opacity: out}}>
      <svg width={760} height={500} viewBox="0 0 120 80">
        <path d={D} fill="none" stroke={C.creme} strokeWidth={7} strokeLinecap="round"
          pathLength={1} strokeDasharray={1} strokeDashoffset={1 - draw}
          style={{filter: `drop-shadow(0 0 14px ${C.bleu})`}} />
      </svg>
    </AbsoluteFill>
  );
};
