import React from 'react';
import {
  AbsoluteFill,
  Img,
  interpolate,
  spring,
  staticFile,
  useCurrentFrame,
  useVideoConfig,
} from 'remotion';
import { GeometricBg } from '../../brand/GeometricBg.tsx';
import { Presentateur } from '../../brand/Presentateur.tsx';
import { poseFin } from '../../brand/presentateur.ts';
import { Corps, Etiquette, Titre } from '../../brand/Text.tsx';
import { BRAND } from '../../brand/tokens.ts';
import type { Script } from '../../schema/index.ts';

const SLOGAN = 'Le tout en un pour propulser votre activité !';
const URL_ACADEMIE = 'academie.rapidosoftware.com';
/** Le logo officiel, tel qu'il est fourni. Jamais redessiné, jamais tourné. */
const LOGO = 'logos/rapidocrm-complet.png';

/**
 * SÉQUENCE 5 — PUNCHLINE ET LOGO.
 *
 * Deux temps. D'abord la punchline sur l'aplat vert, avec le présentateur : la
 * pose est choisie d'après le contenu du tutoriel. Puis la carte de fin : le
 * logo officiel se pose dans un halo qui s'ouvre, un trait vert se trace sous
 * lui, le slogan et l'adresse suivent.
 */
export const Punchline: React.FC<{ script: Script; vertical: boolean }> = ({
  script,
  vertical,
}) => {
  const frame = useCurrentFrame();
  const { fps, durationInFrames, height } = useVideoConfig();

  const bascule = Math.round(durationInFrames * 0.45);
  const sortiePunch = interpolate(frame, [bascule - 10, bascule], [1, 0], {
    extrapolateLeft: 'clamp',
    extrapolateRight: 'clamp',
  });

  const pose = poseFin(script.meta.module, script.meta.numero, script.meta.titre);
  const arriveePresentateur = spring({
    frame: frame - 6,
    fps,
    config: { damping: 200 },
    durationInFrames: 18,
  });

  // La carte de fin : le logo se pose, le halo s'ouvre, le trait se trace.
  const pose_logo = spring({
    frame: frame - bascule,
    fps,
    config: { damping: 14, stiffness: 110 },
    durationInFrames: 26,
  });
  const halo = interpolate(frame, [bascule, bascule + 26], [0, 1], {
    extrapolateLeft: 'clamp',
    extrapolateRight: 'clamp',
  });
  const trait = spring({
    frame: frame - bascule - 16,
    fps,
    config: { damping: 200 },
    durationInFrames: 18,
  });
  const bas = spring({ frame: frame - bascule - 24, fps, config: { damping: 200 } });

  return (
    <AbsoluteFill>
      <GeometricBg variant="mixte" />

      {/* Le présentateur reste d'un bout à l'autre : il porte la punchline, puis
          accompagne la carte de fin. */}
      <AbsoluteFill
        style={{
          padding: height * (vertical ? 0.05 : 0.04),
          paddingBottom: 0,
          alignItems: vertical ? 'center' : 'flex-end',
          justifyContent: 'flex-end',
          opacity: arriveePresentateur,
        }}
      >
        <div
          style={{
            transform: `translateX(${(1 - arriveePresentateur) * height * 0.06}px)`,
          }}
        >
          <Presentateur pose={pose} taille={vertical ? 0.3 : 0.62} />
        </div>
      </AbsoluteFill>

      <AbsoluteFill
        style={{
          padding: height * 0.06,
          justifyContent: 'center',
          opacity: sortiePunch,
        }}
      >
        <div
          style={{
            background: BRAND.colors.vert,
            borderRadius: BRAND.radius,
            padding: height * 0.055,
            maxWidth: vertical ? '100%' : '62%',
          }}
        >
          <Titre fond={BRAND.colors.vert} taille={vertical ? 0.07 : 0.088}>
            {script.punchline.texte}
          </Titre>
        </div>
      </AbsoluteFill>

      <AbsoluteFill
        style={{
          justifyContent: 'center',
          alignItems: vertical ? 'center' : 'flex-start',
          paddingLeft: vertical ? 0 : height * 0.09,
          opacity: 1 - sortiePunch,
        }}
      >
        <div
          style={{
            position: 'relative',
            background: BRAND.colors.fondClair,
            borderRadius: BRAND.radius,
            padding: height * 0.055,
            display: 'flex',
            flexDirection: 'column',
            alignItems: 'center',
            gap: height * 0.02,
            minWidth: vertical ? '78%' : '46%',
          }}
        >
          {/* Halo : une seule ouverture de lumière, pas de clignotement. */}
          <div
            style={{
              position: 'absolute',
              width: height * 0.5 * halo,
              height: height * 0.5 * halo,
              borderRadius: 999,
              top: height * 0.02,
              background: `radial-gradient(circle, rgba(76,175,80,${0.18 * (1 - halo)}) 0%, rgba(76,175,80,0) 70%)`,
            }}
          />
          <Img
            src={staticFile(LOGO)}
            style={{
              height: height * 0.26,
              width: 'auto', // ratio verrouillé : scale uniforme, aucune rotation
              objectFit: 'contain',
              transform: `scale(${0.86 + pose_logo * 0.14}) translateY(${(1 - pose_logo) * height * 0.02}px)`,
            }}
          />
          <div
            style={{
              width: `${trait * 38}%`,
              height: height * 0.005,
              borderRadius: 999,
              background: BRAND.colors.vert,
            }}
          />
          <div style={{ opacity: bas, textAlign: 'center' }}>
            <Corps fond={BRAND.colors.fondClair} taille={0.028} align="center">
              {SLOGAN}
            </Corps>
          </div>
        </div>
      </AbsoluteFill>

      <AbsoluteFill
        style={{
          padding: height * 0.05,
          alignItems: 'center',
          justifyContent: 'flex-end',
          opacity: bas * (1 - sortiePunch),
        }}
      >
        <div
          style={{
            background: BRAND.colors.fondClair,
            borderRadius: 999,
            padding: `${height * 0.012}px ${height * 0.028}px`,
          }}
        >
          <Etiquette fond={BRAND.colors.fondClair} taille={0.02} align="center">
            {URL_ACADEMIE}
          </Etiquette>
        </div>
      </AbsoluteFill>
    </AbsoluteFill>
  );
};
