import React from 'react';
import {
  AbsoluteFill,
  Easing,
  Img,
  interpolate,
  spring,
  staticFile,
  useCurrentFrame,
  useVideoConfig,
} from 'remotion';
import { GeometricBg } from '../../brand/GeometricBg.tsx';
import { Mockup } from '../../brand/Mockup.tsx';
import { BRAND } from '../../brand/tokens.ts';
import { Etiquette, SousTitre } from '../../brand/Text.tsx';
import type { Script } from '../../schema/index.ts';

/**
 * SÉQUENCE 0 — OUVERTURE. La vignette du tutoriel, celle-là même que porte la
 * page de l'Académie et la miniature YouTube, s'affiche en tête de vidéo : le
 * spectateur retrouve l'image sur laquelle il a cliqué.
 *
 * Elle est posée **dans un mockup**, à son rapport 16:9, sur un fond de charte.
 * En 9:16 surtout : plein cadre, une vignette large se retrouvait rognée de
 * moitié. Ici elle est montrée entière, avec le module et le numéro sous elle.
 */
export const Ouverture: React.FC<{
  script: Script;
  vignetteSrc: string | null;
  vertical: boolean;
}> = ({ script, vignetteSrc, vertical }) => {
  const frame = useCurrentFrame();
  const { fps, durationInFrames, height } = useVideoConfig();

  const arrivee = spring({
    frame,
    fps,
    config: { damping: 14, stiffness: 110 },
    durationInFrames: 18,
  });
  const sortie = interpolate(frame, [durationInFrames - 8, durationInFrames], [1, 0], {
    extrapolateLeft: 'clamp',
    extrapolateRight: 'clamp',
  });
  // Zoom très lent : l'image respire sans bouger sous les yeux.
  const zoom = interpolate(frame, [0, durationInFrames], [1, 1.04], {
    easing: Easing.out(Easing.quad),
  });

  return (
    <AbsoluteFill style={{ opacity: sortie }}>
      <GeometricBg variant="sobre" />

      <AbsoluteFill
        style={{
          // En 9:16 le mockup prend presque toute la largeur : la vignette y est
          // large, la rétrécir la rendrait illisible.
          padding: height * (vertical ? 0.03 : 0.1),
          alignItems: 'center',
          justifyContent: 'center',
          gap: height * (vertical ? 0.035 : 0.03),
        }}
      >
        <Mockup
          adresse={`academie.rapidosoftware.com/${script.meta.slug}`}
          style={{
            width: '100%',
            aspectRatio: '16 / 9',
            transform: `scale(${0.92 + arrivee * 0.08})`,
          }}
        >
          {vignetteSrc ? (
            <AbsoluteFill style={{ transform: `scale(${zoom})` }}>
              <Img
                src={staticFile(vignetteSrc)}
                style={{ width: '100%', height: '100%', objectFit: 'cover' }}
              />
            </AbsoluteFill>
          ) : (
            <AbsoluteFill style={{ backgroundColor: BRAND.colors.fondClair }} />
          )}
        </Mockup>

        <div
          style={{
            opacity: arrivee,
            transform: `translateY(${(1 - arrivee) * height * 0.02}px)`,
            display: 'flex',
            flexDirection: 'column',
            alignItems: 'center',
            gap: height * 0.012,
          }}
        >
          <SousTitre
            fond={BRAND.colors.fondClair}
            taille={vertical ? 0.04 : 0.034}
            align="center"
          >
            {script.meta.titre}
          </SousTitre>
          <div
            style={{
              background: BRAND.colors.vert,
              borderRadius: 999,
              padding: `${height * 0.01}px ${height * 0.024}px`,
            }}
          >
            <Etiquette fond={BRAND.colors.vert} taille={0.018}>
              {`${script.meta.module} · V${String(script.meta.numero).padStart(2, '0')}`}
            </Etiquette>
          </div>
        </div>
      </AbsoluteFill>
    </AbsoluteFill>
  );
};
