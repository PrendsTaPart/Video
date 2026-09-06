import React from 'react';
import { useVideoConfig } from 'remotion';
import { BRAND } from './tokens.ts';

/**
 * Fenêtre de navigateur qui encadre l'enregistrement d'écran.
 *
 * En 9:16 surtout : sans cadre, le screencast est rogné par les bords et on ne
 * comprend plus qu'on regarde un logiciel. Le mockup le pose dans un objet
 * identifiable, avec sa barre de titre et son ombre.
 */
export const Mockup: React.FC<{
  children: React.ReactNode;
  /** Texte de la barre d'adresse. */
  adresse?: string;
  style?: React.CSSProperties;
}> = ({ children, adresse = 'crm.rapidosoftware.com', style }) => {
  const { height } = useVideoConfig();
  const barre = height * 0.028;

  return (
    <div
      style={{
        borderRadius: BRAND.radius,
        overflow: 'hidden',
        background: BRAND.colors.blanc,
        boxShadow: `0 ${height * 0.018}px ${height * 0.055}px rgba(56,56,56,0.22)`,
        display: 'flex',
        flexDirection: 'column',
        ...style,
      }}
    >
      <div
        style={{
          height: barre,
          background: BRAND.colors.fondClair,
          borderBottom: `1px solid rgba(56,56,56,0.08)`,
          display: 'flex',
          alignItems: 'center',
          paddingLeft: barre * 0.5,
          gap: barre * 0.28,
          flexShrink: 0,
        }}
      >
        {[BRAND.colors.vert, BRAND.colors.bleu, BRAND.colors.violet].map((c) => (
          <div
            key={c}
            style={{ width: barre * 0.28, height: barre * 0.28, borderRadius: 999, background: c }}
          />
        ))}
        <div
          style={{
            marginLeft: barre * 0.5,
            marginRight: barre * 0.5,
            flex: 1,
            height: barre * 0.56,
            borderRadius: 999,
            background: BRAND.colors.blanc,
            display: 'flex',
            alignItems: 'center',
            paddingLeft: barre * 0.4,
            fontFamily: BRAND.font,
            fontSize: barre * 0.4,
            color: 'rgba(56,56,56,0.45)',
            overflow: 'hidden',
            whiteSpace: 'nowrap',
          }}
        >
          {adresse}
        </div>
      </div>
      <div style={{ flex: 1, position: 'relative', overflow: 'hidden' }}>{children}</div>
    </div>
  );
};
