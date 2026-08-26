import React from 'react';
import {
  AbsoluteFill,
  interpolate,
  spring,
  useCurrentFrame,
  useVideoConfig,
} from 'remotion';
import { GeometricBg } from '../../brand/GeometricBg.tsx';
import { Logomark } from '../../brand/Logo.tsx';
import { Presentateur } from '../../brand/Presentateur.tsx';
import { poseFin } from '../../brand/presentateur.ts';
import { Corps, Etiquette, Titre } from '../../brand/Text.tsx';
import { BRAND } from '../../brand/tokens.ts';
import type { Script } from '../../schema/index.ts';

const SLOGAN = 'Le tout en un pour propulser votre activité !';
const URL_ACADEMIE = 'academie.rapidosoftware.com';

/**
 * SÉQUENCE 5 — PUNCHLINE ET LOGO. La punchline en grand sur l'aplat vert, puis
 * les trois oiseaux origami se posent (vert, bleu, violet, 6 frames d'écart) et
 * le mot « RapidoCRM » se révèle par un masque horizontal. Aucune rotation.
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

  const apparitionOiseau = (rang: number): number =>
    spring({
      frame: frame - bascule - rang * 6,
      fps,
      config: { damping: 200 },
      durationInFrames: 16,
    });

  const oiseaux: [number, number, number] = [
    apparitionOiseau(0),
    apparitionOiseau(1),
    apparitionOiseau(2),
  ];
  const arrivee: [number, number, number] = [
    (1 - oiseaux[0]) * -14,
    (1 - oiseaux[1]) * -14,
    (1 - oiseaux[2]) * -14,
  ];

  // Image de fin : le présentateur, pose « résultat obtenu », entre avec la
  // punchline et reste jusqu'au logo. Choisie par (module, numéro), stable.
  const pose = poseFin(script.meta.module, script.meta.numero);
  const arriveePresentateur = spring({
    frame: frame - 6,
    fps,
    config: { damping: 200 },
    durationInFrames: 18,
  });

  const masque = interpolate(frame, [bascule + 20, bascule + 34], [0, 1], {
    extrapolateLeft: 'clamp',
    extrapolateRight: 'clamp',
  });
  const bas = spring({ frame: frame - bascule - 30, fps, config: { damping: 200 } });

  return (
    <AbsoluteFill>
      <GeometricBg variant="mixte" />

      <AbsoluteFill
        style={{
          padding: height * (vertical ? 0.05 : 0.04),
          paddingBottom: 0, // la photo source est coupée au buste : on cale le
          alignItems: vertical ? 'center' : 'flex-end', // bord franc hors champ
          justifyContent: 'flex-end',
          opacity: sortiePunch * arriveePresentateur,
        }}
      >
        <div
          style={{
            transform: `translateX(${(1 - arriveePresentateur) * height * 0.06}px)`,
          }}
        >
          <Presentateur pose={pose} taille={vertical ? 0.3 : 0.64} />
        </div>
      </AbsoluteFill>

      <AbsoluteFill
        style={{
          padding: height * 0.06,
          justifyContent: 'center',
          opacity: sortiePunch,
        }}
      >
        {/* Défonce sur aplat vert : la punchline reste blanche sur vert, jamais
            à cheval sur le fond clair. */}
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
          alignItems: 'center',
          opacity: 1 - sortiePunch,
        }}
      >
        {/* Le logo n'apparaît que sur un fond autorisé par la charte : on lui
            réserve un aplat #F2F4F7, avec sa zone de protection. */}
        <div
          style={{
            background: BRAND.colors.fondClair,
            borderRadius: BRAND.radius,
            padding: height * 0.05,
            display: 'flex',
            flexDirection: 'column',
            alignItems: 'center',
            gap: height * 0.022,
            minWidth: vertical ? '78%' : '46%',
          }}
        >
          <Logomark taille={height * 0.2} oiseaux={oiseaux} arrivee={arrivee} />
          <div
            style={{
              overflow: 'hidden',
              width: `${masque * 100}%`,
              display: 'flex',
              justifyContent: 'center',
            }}
          >
            <Titre fond={BRAND.colors.fondClair} taille={0.07} align="center">
              RapidoCRM
            </Titre>
          </div>
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
