import React from 'react';
import {C} from './brand';

// The signature chef-toque motif, drawn as a single silhouette so it can be
// tiled, tinted and layered translucently without ever reading as the logo
// mark itself (the charter forbids altering the mark).
export const ToqueShape: React.FC<{size: number; color?: string; opacity?: number}> = ({
  size,
  color = C.bleu,
  opacity = 1,
}) => (
  <svg width={size} height={size} viewBox="0 0 100 100" style={{opacity, display: 'block'}}>
    <path
      fill={color}
      d="M50 12c-7.2 0-13.3 4.3-16 10.4-1.9-.9-4-1.4-6.3-1.4-8.4 0-15.2 6.8-15.2 15.2 0 5.9 3.4 11 8.3 13.5v9.1c0 1.7 1.4 3.1 3.1 3.1h52.2c1.7 0 3.1-1.4 3.1-3.1v-9.1c4.9-2.5 8.3-7.6 8.3-13.5 0-8.4-6.8-15.2-15.2-15.2-2.3 0-4.4.5-6.3 1.4C63.3 16.3 57.2 12 50 12z"
    />
    <rect x="23.9" y="64.5" width="52.2" height="9.4" rx="2.6" fill={color} />
    <rect x="23.9" y="77.2" width="52.2" height="6.2" rx="2" fill={color} opacity={0.55} />
  </svg>
);

// One translucent layer sliding in from a corner. Layers superimpose to build
// the pattern up, as the brief describes.
export const ToqueLayer: React.FC<{
  corner: 0 | 1 | 2 | 3;
  progress: number; // 0 -> 1
  size: number;
  opacity: number;
}> = ({corner, progress, size, opacity}) => {
  const dx = corner === 0 || corner === 3 ? -1 : 1;
  const dy = corner < 2 ? -1 : 1;
  const travel = 420 * (1 - progress);
  return (
    <div
      style={{
        position: 'absolute',
        left: corner === 0 || corner === 3 ? '4%' : undefined,
        right: corner === 1 || corner === 2 ? '4%' : undefined,
        top: corner < 2 ? '6%' : undefined,
        bottom: corner >= 2 ? '6%' : undefined,
        transform: `translate(${dx * travel}px, ${dy * travel}px)`,
        opacity: opacity * progress,
      }}
    >
      <ToqueShape size={size} color={C.bleu} />
    </div>
  );
};
