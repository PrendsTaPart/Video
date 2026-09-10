import React from 'react';
import {
  AbsoluteFill,
  Img,
  OffthreadVideo,
  interpolate,
  spring,
  staticFile,
  useCurrentFrame,
  useVideoConfig,
} from 'remotion';
import { BRAND } from './tokens.ts';

/**
 * La bulle du présentateur, reprise de la méthode Plan'It : un plan parlant
 * rendu UNE SEULE FOIS pour toute la série, bouclé en aller-retour pour éviter
 * le saut du raccord, entouré d'un anneau dégradé qui tourne, d'un halo et de
 * barres de niveau. C'est la voix qui pilote l'animation.
 *
 * Sans plan parlant, on retombe sur le portrait fixe : l'habillage reste animé,
 * seule la bouche ne bouge plus. Utile pour itérer sans relancer une génération
 * payante.
 */
export const AvatarBulle: React.FC<{
  /** Diamètre de la bulle, en fraction de la hauteur de frame. */
  taille: number;
  /** Plan parlant (chemin staticFile). À défaut, le portrait fixe. */
  planSrc?: string | null;
  portraitSrc?: string;
  /** Niveau sonore 0→1, pour l'anneau, le halo et les barres. */
  niveau?: number;
  /** Frames avant l'entrée en scène. */
  retard?: number;
}> = ({
  taille,
  planSrc = null,
  portraitSrc = 'avatar/portrait.webp',
  niveau = 0,
  retard = 0,
}) => {
  const frame = useCurrentFrame();
  const { fps, height } = useVideoConfig();

  const diametre = height * taille;
  const arrivee = spring({
    frame: frame - retard,
    fps,
    config: { damping: 12, stiffness: 120 }, // easeOutBack : la bulle rebondit
    durationInFrames: 24,
  });

  // Respiration pilotée par la voix, jamais l'inverse.
  const respiration = 1 + niveau * 0.035;
  const anneau = height * (0.008 + niveau * 0.006);
  const halo = height * (0.02 + niveau * 0.05);
  const rotation = frame * 0.5;

  return (
    <div
      style={{
        width: diametre,
        height: diametre,
        position: 'relative',
        transform: `scale(${arrivee * respiration})`,
        flexShrink: 0,
      }}
    >
      {/* Halo : rayon et intensité suivant le niveau sonore. */}
      <div
        style={{
          position: 'absolute',
          inset: -halo,
          borderRadius: 999,
          background: `radial-gradient(circle, rgba(76,175,80,${0.10 + niveau * 0.22}) 0%, rgba(76,175,80,0) 70%)`,
        }}
      />

      {/* Anneau dégradé en rotation lente, épaissi par la voix. */}
      <div
        style={{
          position: 'absolute',
          inset: -anneau,
          borderRadius: 999,
          background: `conic-gradient(from ${rotation}deg, ${BRAND.colors.vert}, ${BRAND.colors.bleu}, ${BRAND.colors.violet}, ${BRAND.colors.vert})`,
        }}
      />

      <AbsoluteFill
        style={{
          borderRadius: 999,
          overflow: 'hidden',
          background: BRAND.colors.fondClair,
        }}
      >
        {planSrc ? (
          <OffthreadVideo
            src={staticFile(planSrc)}
            // Muet : la voix off du tutoriel passe par-dessus. Le plan ne sert
            // qu'aux yeux et à la bouche.
            muted
            style={{
              width: '100%',
              height: '100%',
              objectFit: 'cover',
              objectPosition: 'center 14%',
              transform: 'scale(1.12)',
            }}
          />
        ) : (
          <Img
            src={staticFile(portraitSrc)}
            style={{
              width: '100%',
              height: '100%',
              objectFit: 'cover',
              objectPosition: 'center 14%',
              transform: 'scale(1.12)',
            }}
          />
        )}
      </AbsoluteFill>

      {/* Voile radial : le rendu arrive sur fond studio gris, qui jure avec la
          charte. Un détourage mangerait cheveux et lunettes ; ce dégradé fond
          seulement le pourtour. */}
      <AbsoluteFill
        style={{
          borderRadius: 999,
          background: `radial-gradient(circle, rgba(242,244,247,0) 58%, ${BRAND.colors.fondClair} 100%)`,
          pointerEvents: 'none',
        }}
      />

      <BarresDeNiveau diametre={diametre} niveau={niveau} frame={frame} />
    </div>
  );
};

const NOMBRE_BARRES = 13;

/**
 * Treize barres sous la bulle. L'onde se propage du centre vers les bords :
 * chaque barre lit le niveau avec un léger décalage latéral.
 */
const BarresDeNiveau: React.FC<{ diametre: number; niveau: number; frame: number }> = ({
  diametre,
  niveau,
  frame,
}) => (
  <div
    style={{
      position: 'absolute',
      top: '100%',
      left: 0,
      width: '100%',
      marginTop: diametre * 0.07,
      display: 'flex',
      alignItems: 'flex-end',
      justifyContent: 'center',
      gap: diametre * 0.018,
      height: diametre * 0.12,
    }}
  >
    {Array.from({ length: NOMBRE_BARRES }, (_, i) => {
      const distance = Math.abs(i - (NOMBRE_BARRES - 1) / 2);
      const decalage = distance * 2.2;
      const onde = Math.abs(Math.sin((frame - decalage) / 5));
      const hauteur = interpolate(niveau * onde, [0, 1], [0.12, 1], {
        extrapolateRight: 'clamp',
      });
      return (
        <div
          key={i}
          style={{
            width: diametre * 0.022,
            height: `${hauteur * 100}%`,
            borderRadius: 999,
            background: BRAND.colors.vert,
            opacity: 0.35 + hauteur * 0.65,
          }}
        />
      );
    })}
  </div>
);
