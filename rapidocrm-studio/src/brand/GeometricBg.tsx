import React from 'react';
import { AbsoluteFill, interpolate, spring, useCurrentFrame, useVideoConfig } from 'remotion';
import { BRAND } from './tokens.ts';

export type VarianteFond = 'vert' | 'violet' | 'mixte' | 'sobre' | 'origami';

interface Props {
  variant?: VarianteFond;
  /** 0 → 1 : hors-champ → en place. Par défaut, calculé depuis la frame. */
  progress?: number;
  direction?: 'entree' | 'sortie';
}

/**
 * Fond signature de la charte : grandes diagonales géométriques qui glissent
 * depuis le hors-champ, puis restent fixes. Jamais de rotation, jamais de
 * clignotement.
 */
export const GeometricBg: React.FC<Props> = ({
  variant = 'mixte',
  progress,
  direction = 'entree',
}) => {
  const frame = useCurrentFrame();
  const { fps, width, height } = useVideoConfig();

  const auto = spring({ frame, fps, config: { damping: 200 }, durationInFrames: 20 });
  const p = progress ?? auto;
  const avancement = direction === 'sortie' ? 1 - p : p;

  const glissement = (depuis: number): number =>
    interpolate(avancement, [0, 1], [depuis, 0], {
      extrapolateLeft: 'clamp',
      extrapolateRight: 'clamp',
    });

  const vert = (
    <polygon
      points={`0,0 ${width},0 0,${height}`}
      fill={BRAND.colors.vert}
      transform={`translate(${glissement(-width)} ${glissement(-height)})`}
    />
  );

  const violet = (
    <polygon
      points={`${width},${height * 0.35} ${width},${height} ${width * 0.42},${height}`}
      fill={BRAND.colors.violet}
      transform={`translate(${glissement(width)} ${glissement(height)})`}
    />
  );

  const contenu = (): React.ReactNode => {
    switch (variant) {
      case 'mixte':
        return (
          <>
            {vert}
            {violet}
          </>
        );
      case 'vert':
        return vert;
      case 'violet':
        return violet;
      case 'sobre':
        return (
          <polygon
            points={`0,${height} ${width * 0.55},${height} 0,${height * 0.62}`}
            fill={BRAND.colors.vert}
            transform={`translate(${glissement(-width * 0.6)} 0)`}
          />
        );
      case 'origami':
        return <Origami largeur={width} hauteur={height} frame={frame} />;
      default:
        return null;
    }
  };

  return (
    <AbsoluteFill style={{ backgroundColor: BRAND.colors.fondClair }}>
      <svg width={width} height={height} viewBox={`0 0 ${width} ${height}`}>
        {variant !== 'origami' && <Origami largeur={width} hauteur={height} frame={frame} />}
        {contenu()}
      </svg>
    </AbsoluteFill>
  );
};

/**
 * Triangles low-poly translucides qui dérivent très lentement, rappelant les
 * oiseaux du logo. Opacité plafonnée à 0,08 par la charte.
 */
const Origami: React.FC<{ largeur: number; hauteur: number; frame: number }> = ({
  largeur,
  hauteur,
  frame,
}) => {
  const triangles = [
    { x: 0.12, y: 0.2, t: 0.11, couleur: BRAND.colors.vert, vitesse: 0.06 },
    { x: 0.68, y: 0.14, t: 0.08, couleur: BRAND.colors.bleu, vitesse: -0.04 },
    { x: 0.82, y: 0.72, t: 0.13, couleur: BRAND.colors.violet, vitesse: 0.05 },
    { x: 0.3, y: 0.78, t: 0.07, couleur: BRAND.colors.bleu, vitesse: -0.03 },
  ];
  return (
    <g opacity={0.08}>
      {triangles.map((tri, i) => {
        const cote = hauteur * tri.t;
        const derive = frame * tri.vitesse;
        const x = largeur * tri.x + derive;
        const y = hauteur * tri.y + derive * 0.4;
        return (
          <polygon
            key={i}
            points={`${x},${y} ${x + cote},${y + cote * 0.35} ${x + cote * 0.4},${y + cote}`}
            fill={tri.couleur}
          />
        );
      })}
    </g>
  );
};
