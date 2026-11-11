import React from 'react';
import { AbsoluteFill, spring, useCurrentFrame, useVideoConfig } from 'remotion';
import { GeometricBg } from '../../brand/GeometricBg.tsx';
import { Logo } from '../../brand/Logo.tsx';
import { Etiquette, Titre } from '../../brand/Text.tsx';
import { BRAND } from '../../brand/tokens.ts';
import type { Script } from '../../schema/index.ts';

/**
 * SÉQUENCE 2 — TITRE. Fond blanc, diagonale verte réduite en bas, logo
 * RapidoCRM en haut à gauche, trois pastilles d'étapes annoncées.
 */
export const TitreSeq: React.FC<{ script: Script; vertical: boolean }> = ({
  script,
  vertical,
}) => {
  const frame = useCurrentFrame();
  const { fps, height } = useVideoConfig();

  const annonces = script.demo.etapes.slice(0, 3).map((e, i) => `${i + 1}. ${e.titre}`);

  return (
    <AbsoluteFill style={{ backgroundColor: BRAND.colors.blanc }}>
      <GeometricBg variant="sobre" />
      <AbsoluteFill style={{ padding: height * 0.04, alignItems: 'flex-start' }}>
        <Logo nom="rapidocrm" fond={BRAND.colors.blanc} hauteur={0.085} />
      </AbsoluteFill>

      <AbsoluteFill
        style={{
          padding: height * (vertical ? 0.09 : 0.11),
          justifyContent: 'center',
          gap: height * 0.045,
        }}
      >
        <div
          style={{
            opacity: spring({ frame, fps, config: { damping: 200 } }),
          }}
        >
          <Titre fond={BRAND.colors.blanc} taille={vertical ? 0.062 : 0.078}>
            {script.meta.titre}
          </Titre>
        </div>
        <div
          style={{
            display: 'flex',
            flexDirection: vertical ? 'column' : 'row',
            gap: height * 0.02,
            flexWrap: 'wrap',
          }}
        >
          {annonces.map((texte, i) => {
            const apparition = spring({
              frame: frame - 8 - i * 5,
              fps,
              config: { damping: 200 },
              durationInFrames: 14,
            });
            return (
              <div
                key={texte}
                style={{
                  opacity: apparition,
                  transform: `translateY(${(1 - apparition) * height * 0.015}px)`,
                  background: BRAND.colors.blanc,
                  borderRadius: BRAND.radius,
                  boxShadow: `0 ${height * 0.006}px ${height * 0.02}px rgba(56,56,56,0.10)`,
                  padding: `${height * 0.016}px ${height * 0.026}px`,
                }}
              >
                <Etiquette fond={BRAND.colors.blanc} taille={vertical ? 0.022 : 0.02}>
                  {texte}
                </Etiquette>
              </div>
            );
          })}
        </div>
      </AbsoluteFill>
    </AbsoluteFill>
  );
};
