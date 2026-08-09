/**
 * BLOC C — MOTION DESIGN, Épisode 1 « La Rentrée » (25s → 40s du master, 15s de durée propre)
 *
 * Composition autonome démarrant à la frame 0 (= 00:25 dans le master).
 * fps = 30 → 450 frames pour 15s. Enregistrée dans src/Root.tsx sous l'id "OutroEp01".
 */
import React from 'react';
import {
  AbsoluteFill,
  Sequence,
  useCurrentFrame,
  useVideoConfig,
  interpolate,
  spring,
  Easing,
} from 'remotion';

// Charte — voir CLAUDE.md
const COLOR_BG = '#0B0B0F';
const COLOR_ACCENT = '#147AFF';
const COLOR_TEXT = '#FFFFFF';

const PASTILLES = ['STOCK', 'ÉQUIPE', 'HACCP', 'RÉSAS', 'CAISSE', 'AVIS'];

export type Ep01Variables = {
  // Résolues par /ep-data depuis le MCP FoodEatUp. "__SUPPRIMER__" = carton non rendu
  // (zéro chiffre inventé — voir bible + manifest.json).
  CA_MOIS: string | '__SUPPRIMER__';
  COUVERTS: string | '__SUPPRIMER__';
  RUPTURES_EVITEES: string | '__SUPPRIMER__';
  logoUrl: string; // fourni par edit_brand (id 7), jamais généré par IA
};

export const OutroEp01: React.FC<{ variables: Ep01Variables }> = ({ variables }) => {
  const { fps } = useVideoConfig();
  const sec = (s: number) => Math.round(s * fps);

  return (
    <AbsoluteFill style={{ backgroundColor: COLOR_BG }}>
      {/* 25.0 → 26.0 : Logo qui s'allume */}
      <Sequence from={sec(0)} durationInFrames={sec(1)}>
        <LogoReveal logoUrl={variables.logoUrl} />
      </Sequence>

      {/* 26.0 → 31.0 : 6 pastilles en cascade puis fusion */}
      <Sequence from={sec(1)} durationInFrames={sec(5)}>
        <PastillesCascade />
      </Sequence>

      {/* 31.0 → 34.0 : bloc chiffres, uniquement si sourcés */}
      <Sequence from={sec(6)} durationInFrames={sec(3)}>
        <ChiffresBlock variables={variables} />
      </Sequence>

      {/* 34.0 → 37.0 : accroche */}
      <Sequence from={sec(9)} durationInFrames={sec(3)}>
        <BigLine text="TU REPRENDS LE CONTRÔLE." />
      </Sequence>

      {/* 37.0 → 39.0 : CTA */}
      <Sequence from={sec(12)} durationInFrames={sec(2)}>
        <CTA />
      </Sequence>

      {/* 39.0 → 40.0 : gag Betterave qui efface le CTA (logo reste) + carton */}
      <Sequence from={sec(14)} durationInFrames={sec(1)}>
        <BetteraveWipe />
      </Sequence>
    </AbsoluteFill>
  );
};

const LogoReveal: React.FC<{ logoUrl: string }> = ({ logoUrl }) => {
  const frame = useCurrentFrame();
  const { fps } = useVideoConfig();
  const opacity = spring({ frame, fps, config: { damping: 200 } });
  return (
    <AbsoluteFill style={{ justifyContent: 'center', alignItems: 'center' }}>
      {/* eslint-disable-next-line jsx-a11y/alt-text */}
      <img src={logoUrl} style={{ opacity, height: 160 }} />
    </AbsoluteFill>
  );
};

const PastillesCascade: React.FC = () => {
  const frame = useCurrentFrame();
  const { fps, width } = useVideoConfig();
  const mergeStart = fps * 4; // fusion dans la dernière seconde du bloc (5s total)

  return (
    <AbsoluteFill style={{ justifyContent: 'center', alignItems: 'center', gap: 16 }}>
      {PASTILLES.map((label, i) => {
        const delay = i * (fps * 0.4);
        const enter = spring({ frame: frame - delay, fps, config: { damping: 12 } });
        const mergeProgress = interpolate(frame, [mergeStart, mergeStart + fps], [0, 1], {
          extrapolateLeft: 'clamp',
          extrapolateRight: 'clamp',
          easing: Easing.inOut(Easing.ease),
        });
        return (
          <div
            key={label}
            style={{
              transform: `scale(${enter}) translateX(${mergeProgress * (i - 2.5) * -20}px)`,
              opacity: enter,
              background: COLOR_ACCENT,
              color: COLOR_TEXT,
              borderRadius: mergeProgress > 0.5 ? 8 : 999,
              padding: '10px 20px',
              fontWeight: 700,
              fontFamily: 'sans-serif',
            }}
          >
            {label}
          </div>
        );
      })}
    </AbsoluteFill>
  );
};

const ChiffresBlock: React.FC<{ variables: Ep01Variables }> = ({ variables }) => {
  const entries: Array<[string, string]> = [
    ['CA du mois', variables.CA_MOIS],
    ['Couverts', variables.COUVERTS],
    ['Ruptures évitées', variables.RUPTURES_EVITEES],
  ].filter(([, v]) => v !== '__SUPPRIMER__') as Array<[string, string]>;

  // Zéro chiffre inventé : si toutes les variables sont "__SUPPRIMER__", ce bloc ne rend rien.
  if (entries.length === 0) return null;

  return (
    <AbsoluteFill style={{ justifyContent: 'center', alignItems: 'center', gap: 24 }}>
      {entries.map(([label, value]) => (
        <div key={label} style={{ textAlign: 'center', fontFamily: 'sans-serif' }}>
          <div style={{ color: COLOR_ACCENT, fontSize: 48, fontWeight: 800 }}>{value}</div>
          <div style={{ color: COLOR_TEXT, fontSize: 20, opacity: 0.8 }}>{label}</div>
        </div>
      ))}
    </AbsoluteFill>
  );
};

const BigLine: React.FC<{ text: string }> = ({ text }) => {
  const frame = useCurrentFrame();
  const { fps } = useVideoConfig();
  const scale = spring({ frame, fps, config: { damping: 10 } });
  return (
    <AbsoluteFill style={{ justifyContent: 'center', alignItems: 'center' }}>
      <div
        style={{
          transform: `scale(${scale})`,
          color: COLOR_TEXT,
          fontSize: 56,
          fontWeight: 900,
          fontFamily: 'sans-serif',
          textAlign: 'center',
          padding: '0 40px',
        }}
      >
        {text}
      </div>
    </AbsoluteFill>
  );
};

const CTA: React.FC = () => (
  <AbsoluteFill style={{ justifyContent: 'center', alignItems: 'center' }}>
    <div style={{ color: COLOR_TEXT, fontSize: 32, fontFamily: 'sans-serif', textAlign: 'center' }}>
      La rentrée, c'est maintenant →{' '}
      <span style={{ color: COLOR_ACCENT, fontWeight: 700 }}>foodeatup.com</span>
    </div>
  </AbsoluteFill>
);

/**
 * Gag de fin (signature de la série, reprise du scénario 2021 où c'était Courge) :
 * Betterave traverse l'écran de droite à gauche en trottinette et efface la ligne de CTA.
 * Passe assez bas pour ne PAS effacer le logo, qui doit rester visible.
 */
const BetteraveWipe: React.FC = () => {
  const frame = useCurrentFrame();
  const { fps, width } = useVideoConfig();
  const x = interpolate(frame, [0, fps], [width + 100, -200], {
    extrapolateRight: 'clamp',
  });
  const ctaErased = frame > fps * 0.5;

  return (
    <AbsoluteFill>
      {!ctaErased && <CTA />}
      <AbsoluteFill style={{ justifyContent: 'center', alignItems: 'center' }}>
        <div
          style={{
            fontFamily: 'sans-serif',
            fontSize: 40,
            fontWeight: 900,
            color: COLOR_ACCENT,
            marginTop: 200,
          }}
        >
          {ctaErased ? 'La suite au prochain épisode.' : ''}
        </div>
      </AbsoluteFill>
      {/* Placeholder trottinette — remplacer par le sprite/asset Betterave canonique */}
      <div
        style={{
          position: 'absolute',
          top: '55%',
          left: x,
          fontSize: 48,
        }}
      >
        🫐🛴
      </div>
    </AbsoluteFill>
  );
};
