import React from 'react';
import { Img, staticFile, useVideoConfig } from 'remotion';
import { BRAND, FONDS_AUTORISES } from './tokens.ts';

export type NomLogo = 'rapidosoftware' | 'rapidocrm' | 'rapidocms' | 'rapidorh';

interface Props {
  /** Quel logo afficher. */
  nom?: NomLogo;
  /** Fond sur lequel le logo est posé — contrôlé contre la charte. */
  fond: string;
  /**
   * Hauteur du logomark, en fraction de la hauteur de frame.
   * La charte interdit de descendre sous 0,08.
   */
  hauteur?: number;
  opacite?: number;
  style?: React.CSSProperties;
}

const MINIMUM = 0.08;

/**
 * Logo de marque. Trois interdits de la charte sont codés ici comme
 * assertions : jamais déformé, jamais tourné, jamais hors des fonds autorisés.
 * La zone de protection (2× la hauteur du logomark) est appliquée d'office.
 */
export const Logo: React.FC<Props> = ({
  nom = 'rapidocrm',
  fond,
  hauteur = 0.1,
  opacite = 1,
  style,
}) => {
  const { height } = useVideoConfig();

  if (!FONDS_AUTORISES.includes(fond.toUpperCase())) {
    throw new Error(
      `<Logo> monté sur un fond hors palette : ${fond}. ` +
        `La charte n'autorise que ${FONDS_AUTORISES.join(', ')}.`,
    );
  }
  if (hauteur < MINIMUM) {
    throw new Error(
      `<Logo> à ${(hauteur * 100).toFixed(1)} % de la hauteur de frame : la charte ` +
        `impose un minimum de ${MINIMUM * 100} %.`,
    );
  }
  if (style && ('transform' in style || 'rotate' in style)) {
    throw new Error(
      '<Logo> : aucune transformation ne peut lui être appliquée — la charte ' +
        'interdit toute rotation et toute déformation du logo.',
    );
  }

  const hauteurPx = height * hauteur;
  const protection = hauteurPx * 2; // zone de protection de la charte

  return (
    <div
      style={{
        padding: protection / 2,
        display: 'flex',
        alignItems: 'center',
        justifyContent: 'center',
        boxSizing: 'content-box',
        opacity: opacite,
        ...style,
      }}
    >
      <Img
        src={staticFile(`logos/${nom}.png`)}
        style={{
          height: hauteurPx,
          width: 'auto', // ratio verrouillé : uniquement un scale uniforme
          objectFit: 'contain',
        }}
      />
    </div>
  );
};

/**
 * Le logomark seul, redessiné en SVG pour l'animation de fin : les trois
 * oiseaux origami se posent l'un après l'autre. Aucune rotation appliquée.
 */
export const Logomark: React.FC<{
  taille: number;
  /** Opacité de chaque oiseau, dans l'ordre vert · bleu · violet. */
  oiseaux?: [number, number, number];
  /** Décalage vertical d'arrivée de chaque oiseau, en pixels. */
  arrivee?: [number, number, number];
}> = ({ taille, oiseaux = [1, 1, 1], arrivee = [0, 0, 0] }) => (
  <svg width={taille} height={taille} viewBox="0 0 100 100">
    <g opacity={oiseaux[0]} transform={`translate(0 ${arrivee[0]})`}>
      <polygon points="8,58 34,44 30,70" fill={BRAND.colors.vert} />
      <polygon points="34,44 30,70 52,62" fill={BRAND.colors.vert} opacity={0.75} />
    </g>
    <g opacity={oiseaux[1]} transform={`translate(0 ${arrivee[1]})`}>
      <polygon points="36,26 64,14 60,42" fill={BRAND.colors.bleu} />
      <polygon points="64,14 60,42 84,32" fill={BRAND.colors.bleu} opacity={0.75} />
    </g>
    <g opacity={oiseaux[2]} transform={`translate(0 ${arrivee[2]})`}>
      <polygon points="50,64 78,54 74,84" fill={BRAND.colors.violet} />
      <polygon points="78,54 74,84 96,72" fill={BRAND.colors.violet} opacity={0.75} />
    </g>
  </svg>
);
