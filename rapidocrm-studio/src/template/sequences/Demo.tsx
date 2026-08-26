import React from 'react';
import {
  AbsoluteFill,
  Easing,
  OffthreadVideo,
  Sequence,
  interpolate,
  staticFile,
  useCurrentFrame,
  useVideoConfig,
} from 'remotion';
import { BRAND } from '../../brand/tokens.ts';
import { Etiquette } from '../../brand/Text.tsx';
import type { Alignement, EtapeScript, Script, Zone } from '../../schema/index.ts';
import { SousTitres } from './SousTitres.tsx';
import type { Minutage } from '../minutage.ts';

interface Props {
  script: Script;
  alignement: Alignement | null;
  minutage: Minutage;
  demoSrc: string | null;
  vertical: boolean;
}

/**
 * SÉQUENCE 3 — DÉMO ÉCRAN. L'enregistrement joue dans un cadre arrondi, la
 * caméra zoome sur la zone de chaque étape, une annotation pointe le clic,
 * une barre de chapitres suit la progression.
 */
export const Demo: React.FC<Props> = ({ script, alignement, minutage, demoSrc, vertical }) => {
  const { height, width } = useVideoConfig();
  const frame = useCurrentFrame();

  const etapeCourante = minutage.demo.etapes.findIndex(
    (e, i) =>
      frame >= e.debut - minutage.demo.debut &&
      frame < e.debut - minutage.demo.debut + minutage.demo.etapes[i]!.duree,
  );
  const index = etapeCourante === -1 ? 0 : etapeCourante;
  const etape = script.demo.etapes[index];

  const marge = height * 0.06;

  return (
    <AbsoluteFill style={{ backgroundColor: BRAND.colors.fondClair }}>
      <AbsoluteFill style={{ padding: marge, justifyContent: 'center' }}>
        <div
          style={{
            position: 'relative',
            width: '100%',
            aspectRatio: vertical ? '9 / 16' : '16 / 9',
            borderRadius: BRAND.radius,
            overflow: 'hidden',
            boxShadow: `0 ${height * 0.02}px ${height * 0.06}px rgba(56,56,56,0.18)`,
            backgroundColor: BRAND.colors.blanc,
          }}
        >
          {minutage.demo.etapes.map((bloc, i) => {
            const e = script.demo.etapes[i];
            if (!e) return null;
            return (
              <Sequence
                key={e.numero}
                from={bloc.debut - minutage.demo.debut}
                durationInFrames={bloc.duree}
                layout="none"
              >
                <PlanEtape etape={e} demoSrc={demoSrc} vertical={vertical} />
              </Sequence>
            );
          })}
        </div>
      </AbsoluteFill>

      {etape && (
        <ChapitreBarre
          numero={index + 1}
          total={script.demo.etapes.length}
          titre={etape.titre}
        />
      )}

      <SousTitres
        alignement={alignement}
        decalageFrames={minutage.demo.debut - minutage.hook.debut}
      />
    </AbsoluteFill>
  );
};

/**
 * Un plan d'étape : zoom & pan doux vers la zone concernée (scale 1 → 1,35 sur
 * 20 frames), puis retour. Les coordonnées viennent de l'analyse.
 */
const PlanEtape: React.FC<{
  etape: EtapeScript;
  demoSrc: string | null;
  vertical: boolean;
}> = ({ etape, demoSrc, vertical }) => {
  const frame = useCurrentFrame();
  const { durationInFrames } = useVideoConfig();

  const zoomEntree = interpolate(frame, [0, 20], [1, 1.35], {
    extrapolateLeft: 'clamp',
    extrapolateRight: 'clamp',
    easing: Easing.out(Easing.cubic),
  });
  const zoomSortie = interpolate(
    frame,
    [durationInFrames - 20, durationInFrames],
    [0, 0.35],
    { extrapolateLeft: 'clamp', extrapolateRight: 'clamp', easing: Easing.out(Easing.cubic) },
  );
  const echelle = vertical ? Math.max(zoomEntree, 1.35) : zoomEntree - zoomSortie;

  const z = etape.zone_focus;
  const centre = { x: z.x + z.w / 2, y: z.y + z.h / 2 };
  const decalageX = (0.5 - centre.x) * 100 * (echelle - 1);
  const decalageY = (0.5 - centre.y) * 100 * (echelle - 1);

  return (
    <>
      <AbsoluteFill
        style={{
          transform: `scale(${echelle}) translate(${decalageX}%, ${decalageY}%)`,
          transformOrigin: 'center center',
        }}
      >
        {demoSrc ? (
          <OffthreadVideo src={staticFile(demoSrc)} muted />
        ) : (
          <AbsoluteFill style={{ backgroundColor: BRAND.colors.blanc }} />
        )}
      </AbsoluteFill>
      <Annotation etape={etape} />
    </>
  );
};

/** Cercle vert pulsant au point de clic + étiquette flottante avec flèche. */
const Annotation: React.FC<{ etape: EtapeScript }> = ({ etape }) => {
  const frame = useCurrentFrame();
  const { height, width } = useVideoConfig();
  if (!etape.annotation) return null;

  const point = etape.point ?? centreZone(etape.zone_focus);
  const pulsation = 1 + 0.18 * Math.sin((frame / 12) * Math.PI);
  const apparition = interpolate(frame, [4, 16], [0, 1], {
    extrapolateLeft: 'clamp',
    extrapolateRight: 'clamp',
  });
  const rayon = height * 0.03;

  return (
    <>
      <div
        style={{
          position: 'absolute',
          left: `${point.x * 100}%`,
          top: `${point.y * 100}%`,
          width: rayon * 2,
          height: rayon * 2,
          marginLeft: -rayon,
          marginTop: -rayon,
          borderRadius: 999,
          border: `${height * 0.005}px solid ${BRAND.colors.vert}`,
          transform: `scale(${pulsation})`,
          opacity: apparition,
        }}
      />
      <div
        style={{
          position: 'absolute',
          left: `${Math.min(point.x * 100, 70)}%`,
          top: `${Math.max(point.y * 100 - 12, 4)}%`,
          background: BRAND.colors.blanc,
          borderRadius: BRAND.radius / 2,
          padding: `${height * 0.012}px ${height * 0.02}px`,
          boxShadow: `0 ${height * 0.008}px ${height * 0.028}px rgba(56,56,56,0.22)`,
          opacity: apparition,
          maxWidth: width * 0.4,
        }}
      >
        <Etiquette fond={BRAND.colors.blanc} taille={0.02}>
          {etape.annotation}
        </Etiquette>
        <div
          style={{
            position: 'absolute',
            bottom: -height * 0.012,
            left: height * 0.024,
            width: 0,
            height: 0,
            borderLeft: `${height * 0.012}px solid transparent`,
            borderRight: `${height * 0.012}px solid transparent`,
            borderTop: `${height * 0.012}px solid ${BRAND.colors.blanc}`,
          }}
        />
      </div>
    </>
  );
};

const centreZone = (z: Zone) => ({ x: z.x + z.w / 2, y: z.y + z.h / 2 });

const ChapitreBarre: React.FC<{ numero: number; total: number; titre: string }> = ({
  numero,
  total,
  titre,
}) => {
  const { height, width } = useVideoConfig();
  return (
    <div
      style={{
        position: 'absolute',
        bottom: height * 0.025,
        left: width * 0.06,
        width: width * 0.88,
        display: 'flex',
        alignItems: 'center',
        gap: height * 0.02,
      }}
    >
      <div
        style={{
          flex: 1,
          height: height * 0.006,
          borderRadius: 999,
          background: 'rgba(56,56,56,0.12)',
          overflow: 'hidden',
        }}
      >
        <div
          style={{
            width: `${(numero / total) * 100}%`,
            height: '100%',
            background: BRAND.colors.vert,
          }}
        />
      </div>
      <Etiquette fond={BRAND.colors.fondClair} taille={0.018}>
        {`Étape ${numero} sur ${total} · ${titre}`}
      </Etiquette>
    </div>
  );
};
