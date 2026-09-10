import React from 'react';
import { useVideoConfig } from 'remotion';
import { BRAND, textOn } from './tokens.ts';

interface PropsTexte {
  children: React.ReactNode;
  /** Fond sur lequel le texte est posé : détermine sa couleur via textOn(). */
  fond?: string;
  /** Taille en fraction de la hauteur de frame — identique en 16:9 et 9:16. */
  taille?: number;
  align?: React.CSSProperties['textAlign'];
  style?: React.CSSProperties;
}

const base = (
  fond: string,
  taillePx: number,
  poids: number,
  interligne: number,
  align: React.CSSProperties['textAlign'],
): React.CSSProperties => ({
  fontFamily: BRAND.font,
  fontWeight: poids,
  fontSize: taillePx,
  lineHeight: interligne,
  color: textOn(fond),
  textAlign: align,
  margin: 0,
  letterSpacing: '-0.01em',
});

export const Titre: React.FC<PropsTexte> = ({
  children,
  fond = BRAND.colors.blanc,
  taille = 0.11,
  align = 'left',
  style,
}) => {
  const { height } = useVideoConfig();
  return (
    <p style={{ ...base(fond, height * taille, 700, 1.05, align), ...style }}>
      {children}
    </p>
  );
};

export const SousTitre: React.FC<PropsTexte> = ({
  children,
  fond = BRAND.colors.blanc,
  taille = 0.055,
  align = 'left',
  style,
}) => {
  const { height } = useVideoConfig();
  return (
    <p style={{ ...base(fond, height * taille, 700, 1.2, align), ...style }}>
      {children}
    </p>
  );
};

export const Corps: React.FC<PropsTexte> = ({
  children,
  fond = BRAND.colors.blanc,
  taille = 0.034,
  align = 'left',
  style,
}) => {
  const { height } = useVideoConfig();
  return (
    <p style={{ ...base(fond, height * taille, 400, 1.35, align), ...style }}>
      {children}
    </p>
  );
};

export const Etiquette: React.FC<PropsTexte> = ({
  children,
  fond = BRAND.colors.blanc,
  taille = 0.024,
  align = 'left',
  style,
}) => {
  const { height } = useVideoConfig();
  return (
    <p
      style={{
        ...base(fond, height * taille, 700, 1.2, align),
        letterSpacing: '0.04em',
        textTransform: 'uppercase',
        ...style,
      }}
    >
      {children}
    </p>
  );
};

/** Pastille de module : aplat de couleur de charte + texte contrasté. */
export const Pastille: React.FC<{
  couleur: string;
  children: React.ReactNode;
  taille?: number;
}> = ({ couleur, children, taille = 0.024 }) => {
  const { height } = useVideoConfig();
  return (
    <div
      style={{
        background: couleur,
        borderRadius: 999,
        padding: `${height * 0.012}px ${height * 0.024}px`,
        display: 'inline-flex',
        alignItems: 'center',
      }}
    >
      <Etiquette fond={couleur} taille={taille}>
        {children}
      </Etiquette>
    </div>
  );
};
