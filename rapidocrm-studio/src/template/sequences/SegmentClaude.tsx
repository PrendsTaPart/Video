import React from 'react';
import {
  AbsoluteFill,
  Easing,
  interpolate,
  spring,
  useCurrentFrame,
  useVideoConfig,
} from 'remotion';
import { BRAND } from '../../brand/tokens.ts';
import { Corps, Etiquette, SousTitre } from '../../brand/Text.tsx';
import type { Script } from '../../schema/index.ts';

/**
 * SÉQUENCE 4 — « FAIS-LE AVEC CLAUDE ». La séquence signature : la carte prompt
 * s'écrit en machine à écrire, le bouton Copier se presse tout seul, et le
 * résultat obtenu dans le CRM apparaît avec un check vert.
 */
export const SegmentClaude: React.FC<{ script: Script; vertical: boolean }> = ({
  script,
  vertical,
}) => {
  const frame = useCurrentFrame();
  const { fps, height, width } = useVideoConfig();
  const seg = script.segment_claude;

  const balayage = interpolate(frame, [0, 16], [0, 1], {
    extrapolateLeft: 'clamp',
    extrapolateRight: 'clamp',
    easing: Easing.out(Easing.cubic),
  });

  const texte = seg.prompt.texte;
  const caracteres = Math.floor(
    interpolate(frame, [16, 16 + texte.length * 0.9], [0, texte.length], {
      extrapolateLeft: 'clamp',
      extrapolateRight: 'clamp',
    }),
  );
  const finFrappe = 16 + texte.length * 0.9;

  const pression = spring({ frame: frame - finFrappe - 6, fps, config: { damping: 200 } });
  const copie = interpolate(frame, [finFrappe + 14, finFrappe + 24], [0, 1], {
    extrapolateLeft: 'clamp',
    extrapolateRight: 'clamp',
  });
  const resultat = spring({
    frame: frame - finFrappe - 24,
    fps,
    config: { damping: 200 },
  });

  return (
    <AbsoluteFill style={{ backgroundColor: BRAND.colors.fondClair }}>
      {/* Diagonale verte qui balaie l'image en entrée de séquence */}
      <svg width={width} height={height} style={{ position: 'absolute' }}>
        <polygon
          points={`0,0 ${width},0 0,${height}`}
          fill={BRAND.colors.vert}
          opacity={0.12}
          transform={`translate(${(balayage - 1) * width} 0)`}
        />
      </svg>

      <AbsoluteFill
        style={{
          padding: height * 0.07,
          gap: height * 0.03,
          justifyContent: 'center',
        }}
      >
        <SousTitre fond={BRAND.colors.fondClair} taille={vertical ? 0.045 : 0.05}>
          {seg.accroche}
        </SousTitre>

        <div
          style={{
            display: 'flex',
            flexDirection: vertical ? 'column' : 'row',
            gap: height * 0.03,
            alignItems: 'stretch',
          }}
        >
          <CartePrompt
            texte={texte.slice(0, caracteres)}
            variables={seg.prompt.variables}
            outilMcp={seg.prompt.outil_mcp}
            pression={pression}
            copie={copie}
          />
          <CarteResultat
            titre={seg.resultat_affiche.titre}
            lignes={seg.resultat_affiche.lignes}
            apparition={resultat}
          />
        </div>
      </AbsoluteFill>
    </AbsoluteFill>
  );
};

const CartePrompt: React.FC<{
  texte: string;
  variables: string[];
  outilMcp: string;
  pression: number;
  copie: number;
}> = ({ texte, variables, outilMcp, pression, copie }) => {
  const { height } = useVideoConfig();
  return (
    <div
      style={{
        flex: 1.3,
        background: BRAND.colors.blanc,
        borderRadius: BRAND.radius,
        boxShadow: `0 ${height * 0.014}px ${height * 0.05}px rgba(56,56,56,0.16)`,
        padding: height * 0.035,
        display: 'flex',
        flexDirection: 'column',
        gap: height * 0.02,
      }}
    >
      <div style={{ display: 'flex', alignItems: 'center', gap: height * 0.014 }}>
        <div
          style={{
            width: height * 0.032,
            height: height * 0.032,
            borderRadius: 8,
            background: BRAND.colors.grisPrimaire,
          }}
        />
        <Etiquette fond={BRAND.colors.blanc} taille={0.017}>
          {`Claude · MCP ${outilMcp || 'RapidoCRM'}`}
        </Etiquette>
      </div>

      <p
        style={{
          fontFamily: BRAND.font,
          fontSize: height * 0.03,
          lineHeight: 1.4,
          color: BRAND.colors.grisPrimaire,
          margin: 0,
        }}
      >
        {decouperPlaceholders(texte, variables)}
      </p>

      <div
        style={{
          alignSelf: 'flex-start',
          background: BRAND.colors.vert,
          borderRadius: 999,
          padding: `${height * 0.012}px ${height * 0.028}px`,
          transform: `scale(${1 - 0.06 * pression * (1 - pression) * 4})`,
        }}
      >
        <Etiquette fond={BRAND.colors.vert} taille={0.018}>
          {copie > 0.5 ? 'Copié !' : 'Copier'}
        </Etiquette>
      </div>
    </div>
  );
};

/** Les placeholders entre crochets sont surlignés en vert, fond vert 10 %. */
const decouperPlaceholders = (texte: string, variables: string[]): React.ReactNode[] => {
  const morceaux = texte.split(/(\[[^\]]*\]?)/g);
  return morceaux.map((morceau, i) => {
    if (!morceau.startsWith('[')) return <span key={i}>{morceau}</span>;
    const nom = morceau.replace(/[[\]]/g, '');
    const connue = variables.some((v) => v.toLowerCase() === nom.toLowerCase());
    return (
      <span
        key={i}
        style={{
          fontFamily: connue ? 'Courier New, monospace' : BRAND.font,
          color: BRAND.colors.grisPrimaire,
          background: 'rgba(76,175,80,0.10)',
          boxShadow: `inset 0 -0.12em 0 rgba(76,175,80,0.45)`,
          borderRadius: 4,
        }}
      >
        {morceau}
      </span>
    );
  });
};

const CarteResultat: React.FC<{
  titre: string;
  lignes: string[];
  apparition: number;
}> = ({ titre, lignes, apparition }) => {
  const { height } = useVideoConfig();
  return (
    <div
      style={{
        flex: 1,
        background: BRAND.colors.blanc,
        borderRadius: BRAND.radius,
        boxShadow: `0 ${height * 0.014}px ${height * 0.05}px rgba(56,56,56,0.16)`,
        padding: height * 0.035,
        opacity: apparition,
        transform: `translateY(${(1 - apparition) * height * 0.03}px)`,
        display: 'flex',
        flexDirection: 'column',
        gap: height * 0.016,
      }}
    >
      <div style={{ display: 'flex', alignItems: 'center', gap: height * 0.014 }}>
        <svg width={height * 0.04} height={height * 0.04} viewBox="0 0 40 40">
          <circle cx="20" cy="20" r="18" fill={BRAND.colors.vert} />
          <polyline
            points="12,21 18,27 29,14"
            fill="none"
            stroke={BRAND.colors.blanc}
            strokeWidth="4"
            strokeLinecap="round"
            strokeLinejoin="round"
            strokeDasharray="30"
            strokeDashoffset={30 * (1 - apparition)}
          />
        </svg>
        <SousTitre fond={BRAND.colors.blanc} taille={0.028}>
          {titre}
        </SousTitre>
      </div>
      {lignes.map((ligne) => (
        <Corps key={ligne} fond={BRAND.colors.blanc} taille={0.024}>
          {ligne}
        </Corps>
      ))}
    </div>
  );
};
