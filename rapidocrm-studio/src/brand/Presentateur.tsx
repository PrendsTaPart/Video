import React from 'react';
import { Img, staticFile, useVideoConfig } from 'remotion';
import { cheminPose, type PosePresentateur } from './presentateur.ts';

/**
 * Le présentateur RapidoCRM, détouré (les fichiers ont un fond transparent) :
 * il se pose directement sur les aplats de la charte, sans cadre ni pastille.
 * Une ombre portée douce le décolle du fond.
 */
export const Presentateur: React.FC<{
  pose: PosePresentateur;
  /** Hauteur, en fraction de la hauteur de frame. */
  taille?: number;
  opacite?: number;
  style?: React.CSSProperties;
}> = ({ pose, taille = 0.62, opacite = 1, style }) => {
  const { height } = useVideoConfig();

  return (
    <Img
      src={staticFile(cheminPose(pose))}
      style={{
        height: height * taille,
        width: 'auto',
        objectFit: 'contain',
        filter: `drop-shadow(0 ${height * 0.01}px ${height * 0.03}px rgba(56,56,56,0.28))`,
        opacity: opacite,
        ...style,
      }}
    />
  );
};
