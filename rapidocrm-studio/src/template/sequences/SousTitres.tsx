import React from 'react';
import { useCurrentFrame, useVideoConfig } from 'remotion';
import { BRAND } from '../../brand/tokens.ts';
import type { Alignement } from '../../schema/index.ts';
import { FPS } from '../minutage.ts';

/**
 * Sous-titres brûlés, générés depuis l'alignement mot à mot : deux lignes max,
 * Arial Bold blanc, contour #383838, le mot en cours surligné en vert.
 */
/** Contour net sur huit directions, tenable sur fond clair comme sur fond vert. */
const contour = (epaisseur: number, couleur: string): string => {
  const e = epaisseur.toFixed(2);
  const d = (epaisseur * 0.71).toFixed(2);
  return [
    `${e}px 0 ${couleur}`,
    `-${e}px 0 ${couleur}`,
    `0 ${e}px ${couleur}`,
    `0 -${e}px ${couleur}`,
    `${d}px ${d}px ${couleur}`,
    `-${d}px ${d}px ${couleur}`,
    `${d}px -${d}px ${couleur}`,
    `-${d}px -${d}px ${couleur}`,
  ].join(', ');
};

export const SousTitres: React.FC<{
  alignement: Alignement | null;
  /** Décalage entre la frame de la composition et le temps de la piste voix. */
  decalageFrames?: number;
  /**
   * `superposes` — posés en bas de la frame, par-dessus l'image (16:9).
   * `dans-le-flux` — rendus à leur place dans la colonne, sous la vidéo (9:16).
   * En vertical, rien n'est écrit par-dessus l'écran du logiciel.
   */
  placement?: 'superposes' | 'dans-le-flux';
}> = ({ alignement, decalageFrames = 0, placement = 'superposes' }) => {
  const frame = useCurrentFrame();
  const { height, width } = useVideoConfig();
  if (!alignement) return null;

  const t = (frame + decalageFrames) / FPS;
  const bloc = alignement.blocs.find((b) => t >= b.debut && t <= b.debut + b.duree);
  if (!bloc || bloc.mots.length === 0) return null;

  const relatif = t - bloc.debut;
  const courant = bloc.mots.findIndex((m) => relatif >= m.debut && relatif <= m.fin);
  const index = courant === -1 ? 0 : courant;

  // Fenêtre de 7 mots autour du mot en cours : deux lignes au plus.
  const debut = Math.max(0, index - 3);
  const fenetre = bloc.mots.slice(debut, debut + 7);

  const taille = height * (placement === 'dans-le-flux' ? 0.03 : 0.036);
  const flux = placement === 'dans-le-flux';
  return (
    <div
      style={{
        position: flux ? 'relative' : 'absolute',
        // Superposés : au-dessus de la barre de chapitres, qui occupe le bas du
        // cadre. Dans le flux : à leur place sous la vidéo.
        bottom: flux ? undefined : height * 0.115,
        left: flux ? undefined : width * 0.08,
        width: flux ? '100%' : width * 0.84,
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
              color: BRAND.colors.blanc,
              // Le mot en cours est souligné de vert plutôt que coloré : du
              // vert sur un contour sombre se lit mal en petit.
              boxShadow: actif ? `inset 0 -0.14em 0 ${BRAND.colors.vert}` : undefined,
              // Contour par ombre portée plutôt que WebkitTextStroke : le
              // stroke est peint par-dessus le remplissage et grignote les
              // lettres, illisible sur un écran clair.
              textShadow: contour(taille * 0.055, BRAND.colors.grisPrimaire),
            }}
          >
            {mot.mot}
          </span>
        );
      })}
    </div>
  );
};
