import React from 'react';
import { AbsoluteFill, Img, staticFile, useVideoConfig } from 'remotion';
import { Logo } from '../brand/Logo.tsx';
import { Etiquette, Pastille, Titre } from '../brand/Text.tsx';
import { BRAND, couleurModule } from '../brand/tokens.ts';
import type { Script } from '../schema/index.ts';

interface Props {
  script: Script;
  /** Frame représentative extraite de l'enregistrement (chemin staticFile). */
  captureSrc: string | null;
  vertical: boolean;
}

const MAX_TITRE_COURT = 28;

/**
 * Vignette à la charte, rendue avec Remotion pour rester cohérente avec le
 * template. 16:9 pour YouTube et le lecteur du site, 9:16 pour les verticaux.
 */
export const Vignette: React.FC<Props> = ({ script, captureSrc, vertical }) => {
  const { height, width } = useVideoConfig();
  const titreCourt = script.meta.titre_court;

  if (titreCourt.length > MAX_TITRE_COURT) {
    throw new Error(
      `titre_court « ${titreCourt} » fait ${titreCourt.length} caractères : ` +
        `au-delà de ${MAX_TITRE_COURT}, il n'est plus lisible à 320 px de large. ` +
        'Fournissez une version plus courte.',
    );
  }

  const couleur = couleurModule(script.meta.module);
  const numero = `V${String(script.meta.numero).padStart(2, '0')}`;

  const capture = (
    <div
      style={{
        borderRadius: BRAND.radius,
        overflow: 'hidden',
        boxShadow: `0 ${height * 0.02}px ${height * 0.05}px rgba(56,56,56,0.25)`,
        transform: 'rotate(-3deg)', // la capture peut s'incliner, jamais le logo
        background: BRAND.colors.blanc,
        width: '100%',
        aspectRatio: '16 / 9',
      }}
    >
      {captureSrc ? (
        <Img src={staticFile(captureSrc)} style={{ width: '100%', height: '100%', objectFit: 'cover' }} />
      ) : null}
    </div>
  );

  if (vertical) {
    return (
      <AbsoluteFill style={{ backgroundColor: BRAND.colors.fondClair }}>
        <svg width={width} height={height} style={{ position: 'absolute' }}>
          <polygon points={`0,0 ${width},0 ${width},${height * 0.42} 0,${height * 0.34}`} fill={BRAND.colors.vert} />
          <polygon points={`0,${height} ${width},${height} ${width},${height * 0.86}`} fill={BRAND.colors.violet} />
        </svg>
        <AbsoluteFill style={{ padding: width * 0.08, justifyContent: 'space-between' }}>
          <div style={{ paddingTop: height * 0.05 }}>
            <Titre fond={BRAND.colors.vert} taille={0.062}>
              {titreCourt}
            </Titre>
          </div>
          {capture}
          <div style={{ display: 'flex', alignItems: 'center', justifyContent: 'space-between' }}>
            <div style={{ display: 'flex', alignItems: 'center', gap: width * 0.03 }}>
              <Pastille couleur={couleur}>{script.meta.module}</Pastille>
              <Etiquette fond={BRAND.colors.fondClair} taille={0.022}>
                {numero}
              </Etiquette>
            </div>
            <Logo nom="rapidocrm" fond={BRAND.colors.fondClair} hauteur={0.08} />
          </div>
        </AbsoluteFill>
      </AbsoluteFill>
    );
  }

  return (
    <AbsoluteFill style={{ backgroundColor: BRAND.colors.fondClair }}>
      <svg width={width} height={height} style={{ position: 'absolute' }}>
        <polygon points={`0,0 ${width * 0.52},0 ${width * 0.44},${height} 0,${height}`} fill={BRAND.colors.vert} />
        <polygon points={`${width * 0.52},${height} ${width},${height} ${width},${height * 0.78}`} fill={BRAND.colors.violet} />
      </svg>

      <AbsoluteFill style={{ flexDirection: 'row' }}>
        <div
          style={{
            width: '46%',
            padding: height * 0.09,
            display: 'flex',
            flexDirection: 'column',
            justifyContent: 'center',
          }}
        >
          <Titre fond={BRAND.colors.vert} taille={0.13}>
            {titreCourt}
          </Titre>
        </div>
        <div
          style={{
            width: '54%',
            padding: height * 0.09,
            display: 'flex',
            alignItems: 'center',
          }}
        >
          {capture}
        </div>
      </AbsoluteFill>

      <AbsoluteFill style={{ padding: height * 0.045, justifyContent: 'flex-end' }}>
        <div style={{ display: 'flex', alignItems: 'center', gap: height * 0.02 }}>
          {/* Sur l'aplat vert, la pastille passe en blanc : une pastille verte sur
              vert disparaîtrait. */}
          <Pastille couleur={BRAND.colors.blanc}>{script.meta.module}</Pastille>
          <Etiquette fond={BRAND.colors.vert} taille={0.028}>
            {numero}
          </Etiquette>
        </div>
      </AbsoluteFill>

      <AbsoluteFill style={{ padding: height * 0.02, alignItems: 'flex-end' }}>
        <Logo nom="rapidocrm" fond={BRAND.colors.fondClair} hauteur={0.09} />
      </AbsoluteFill>
    </AbsoluteFill>
  );
};
