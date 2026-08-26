import React from 'react';
import { AbsoluteFill, interpolate, spring, useCurrentFrame, useVideoConfig } from 'remotion';
import { GeometricBg } from '../../brand/GeometricBg.tsx';
import { Presentateur } from '../../brand/Presentateur.tsx';
import { poseHook } from '../../brand/presentateur.ts';
import { Corps, Etiquette, Pastille, Titre } from '../../brand/Text.tsx';
import { BRAND, couleurModule } from '../../brand/tokens.ts';
import type { Script } from '../../schema/index.ts';

/**
 * SÉQUENCE 1 — HOOK. Le crochet. Le hook s'écrit mot par mot sur l'aplat vert,
 * la promesse suit, le badge de module s'ancre en bas à droite.
 */
export const Hook: React.FC<{ script: Script; vertical: boolean }> = ({
  script,
  vertical,
}) => {
  const frame = useCurrentFrame();
  const { fps, durationInFrames, height } = useVideoConfig();

  const mots = script.hook.texte.split(' ');
  const sortie = interpolate(
    frame,
    [durationInFrames - 14, durationInFrames],
    [1, 0],
    { extrapolateLeft: 'clamp', extrapolateRight: 'clamp' },
  );

  const promesse = spring({ frame: frame - mots.length * 3 - 6, fps, config: { damping: 200 } });
  const couleur = couleurModule(script.meta.module);

  // Le présentateur entre juste après les premiers mots, sur la droite en 16:9,
  // au-dessus du texte en 9:16. La pose est choisie une fois pour toutes par
  // (module, numéro) : elle ne change pas d'un rendu à l'autre.
  const pose = poseHook(script.meta.module, script.meta.numero);
  const arriveePresentateur = spring({
    frame: frame - 10,
    fps,
    config: { damping: 200 },
    durationInFrames: 18,
  });

  return (
    <AbsoluteFill>
      <GeometricBg variant="mixte" progress={sortie < 1 ? sortie : undefined} />
      <AbsoluteFill
        style={{
          padding: height * (vertical ? 0.06 : 0.05),
          justifyContent: 'center',
        }}
      >
        {/* Aplat vert de défonce : garantit la règle de contraste de la charte,
            quel que soit le nombre de lignes du hook. */}
        <div
          style={{
            background: BRAND.colors.vert,
            borderRadius: BRAND.radius,
            padding: height * (vertical ? 0.05 : 0.055),
            maxWidth: vertical ? '100%' : '62%',
            display: 'flex',
            flexDirection: 'column',
            gap: height * 0.03,
          }}
        >
        <div style={{ display: 'flex', flexWrap: 'wrap', gap: `0 ${height * 0.022}px` }}>
          {mots.map((mot, i) => {
            const apparition = spring({
              frame: frame - i * 3,
              fps,
              config: { damping: 200 },
              durationInFrames: 14,
            });
            return (
              <span
                key={`${mot}-${i}`}
                style={{
                  opacity: apparition,
                  transform: `translateY(${(1 - apparition) * height * 0.02}px)`,
                  display: 'inline-block',
                }}
              >
                <Titre fond={BRAND.colors.vert} taille={vertical ? 0.075 : 0.098}>
                  {mot}
                </Titre>
              </span>
            );
          })}
        </div>
          <div style={{ opacity: promesse }}>
            <Corps fond={BRAND.colors.vert} taille={vertical ? 0.032 : 0.038}>
              {script.hook.promesse}
            </Corps>
          </div>
        </div>
      </AbsoluteFill>

      <AbsoluteFill
        style={{
          padding: height * (vertical ? 0.05 : 0.04),
          paddingBottom: 0, // la photo source est coupée au buste : on cale le
          alignItems: vertical ? 'center' : 'flex-end', // bord franc hors champ
          justifyContent: 'flex-end',
          pointerEvents: 'none',
        }}
      >
        <div
          style={{
            opacity: arriveePresentateur,
            transform: `translateX(${(1 - arriveePresentateur) * height * 0.06}px)`,
          }}
        >
          <Presentateur pose={pose} taille={vertical ? 0.3 : 0.66} />
        </div>
      </AbsoluteFill>

      <AbsoluteFill
        style={{
          padding: height * 0.05,
          alignItems: vertical ? 'center' : 'flex-start',
          justifyContent: 'flex-end',
          gap: height * 0.012,
        }}
      >
        <Pastille couleur={couleur}>{script.meta.module}</Pastille>
        <Etiquette fond={BRAND.colors.fondClair} taille={0.02}>
          {`V${String(script.meta.numero).padStart(2, '0')}`}
        </Etiquette>
      </AbsoluteFill>
    </AbsoluteFill>
  );
};
