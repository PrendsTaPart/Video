import React from 'react';
import { useCurrentFrame, useVideoConfig } from 'remotion';
import { BRAND } from '../../brand/tokens.ts';
import type { Alignement } from '../../schema/index.ts';
import { FPS } from '../minutage.ts';

/**
 * Sous-titres brûlés, générés depuis l'alignement mot à mot : deux lignes max,
 * Arial Bold blanc, contour #383838, le mot en cours surligné en vert.
 */
export const SousTitres: React.FC<{
  alignement: Alignement | null;
  /** Décalage entre la frame de la composition et le temps de la piste voix. */
  decalageFrames?: number;
}> = ({ alignement, decalageFrames = 0 }) => {
  const frame = useCurrentFrame();
  const { height, width } = useVideoConfig();
  if (!alignement) return null;

  const t = (frame + decalageFrames) / FPS;
  const bloc = alignement.blocs.find((b) => t >= b.debut && t <= b.debut + b.duree);
  if (!bloc || bloc.mots.length === 0) return null;

  const relatif = t - bloc.debut;
  const courant = bloc.mots.findIndex((m) => relatif >= m.debut && relatif <= m.fin);
  const index = courant === -1 ? 0 : courant;

  // Fenêtre de 9 mots autour du mot en cours : deux lignes au plus.
  const debut = Math.max(0, index - 4);
  const fenetre = bloc.mots.slice(debut, debut + 9);

  const taille = height * 0.036;
  return (
    <div
      style={{
        position: 'absolute',
        bottom: height * 0.08,
        left: width * 0.08,
        width: width * 0.84,
        display: 'flex',
        flexWrap: 'wrap',
        justifyContent: 'center',
        gap: `${taille * 0.15}px ${taille * 0.35}px`,
      }}
    >
      {fenetre.map((mot, i) => {
        const actif = debut + i === index;
        return (
          <span
            key={`${mot.mot}-${debut + i}`}
            style={{
              fontFamily: BRAND.font,
              fontWeight: 700,
              fontSize: taille,
              lineHeight: 1.25,
              color: actif ? BRAND.colors.vert : BRAND.colors.blanc,
              WebkitTextStroke: `${taille * 0.06}px ${BRAND.colors.grisPrimaire}`,
              paintOrder: 'stroke fill',
            }}
          >
            {mot.mot}
          </span>
        );
      })}
    </div>
  );
};
