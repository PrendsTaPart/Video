import React from 'react';
import {
  AbsoluteFill,
  Easing,
  Img,
  interpolate,
  staticFile,
  useCurrentFrame,
  useVideoConfig,
} from 'remotion';
import { BRAND } from '../../brand/tokens.ts';
import { Etiquette } from '../../brand/Text.tsx';
import type { Script } from '../../schema/index.ts';

/**
 * SÉQUENCE 0 — OUVERTURE. La vignette du tutoriel, celle-là même que porte la
 * page de l'Académie et la miniature YouTube, s'affiche brièvement en tête de
 * vidéo : le spectateur retrouve l'image sur laquelle il a cliqué.
 *
 * `vignetteSrc` vient de la fiche du tutoriel (MCP « RapidoCRM tuto ») ; à
 * défaut, de la vignette produite localement. Sans vignette, la séquence se
 * réduit à un fond de charte et ne casse pas le montage.
 */
export const Ouverture: React.FC<{
  script: Script;
  vignetteSrc: string | null;
}> = ({ script, vignetteSrc }) => {
  const frame = useCurrentFrame();
  const { durationInFrames, height } = useVideoConfig();

  const entree = interpolate(frame, [0, 8], [0, 1], {
    extrapolateLeft: 'clamp',
    extrapolateRight: 'clamp',
    easing: Easing.out(Easing.cubic),
  });
  const sortie = interpolate(frame, [durationInFrames - 8, durationInFrames], [1, 0], {
    extrapolateLeft: 'clamp',
    extrapolateRight: 'clamp',
  });
  // Zoom très lent : l'image respire sans bouger sous les yeux.
  const zoom = interpolate(frame, [0, durationInFrames], [1, 1.05]);

  return (
    <AbsoluteFill
      style={{ backgroundColor: BRAND.colors.fondClair, opacity: entree * sortie }}
    >
      {vignetteSrc ? (
        <AbsoluteFill style={{ transform: `scale(${zoom})` }}>
          <Img
            src={staticFile(vignetteSrc)}
            style={{ width: '100%', height: '100%', objectFit: 'cover' }}
          />
        </AbsoluteFill>
      ) : null}

      {/* La vignette porte déjà le module et le numéro : on n'ajoute rien
          par-dessus. Sans vignette, le repère est utile. */}
      {vignetteSrc ? null : (
        <AbsoluteFill
          style={{
            padding: height * 0.04,
            alignItems: 'center',
            justifyContent: 'center',
          }}
        >
          <div
            style={{
              background: BRAND.colors.blanc,
              borderRadius: 999,
              padding: `${height * 0.012}px ${height * 0.026}px`,
            }}
          >
            <Etiquette fond={BRAND.colors.blanc} taille={0.02}>
              {`${script.meta.module} · V${String(script.meta.numero).padStart(2, '0')}`}
            </Etiquette>
          </div>
        </AbsoluteFill>
      )}
    </AbsoluteFill>
  );
};
