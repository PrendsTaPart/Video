import React from 'react';
import {
  AbsoluteFill,
  Easing,
  Img,
  OffthreadVideo,
  Sequence,
  interpolate,
  staticFile,
  useCurrentFrame,
  useVideoConfig,
} from 'remotion';
import { BRAND } from '../../brand/tokens.ts';
import { Etiquette } from '../../brand/Text.tsx';
import { AvatarBulle } from '../../brand/Avatar.tsx';
import { Mockup } from '../../brand/Mockup.tsx';
import { NiveauVoix } from '../niveauVoix.tsx';
import type { Alignement, EtapeScript, Script, Zone } from '../../schema/index.ts';
import { SousTitres } from './SousTitres.tsx';
import type { Minutage } from '../minutage.ts';

interface Props {
  script: Script;
  alignement: Alignement | null;
  minutage: Minutage;
  /** Un fichier par étape : chaque plan démarre à zéro dans sa Sequence. */
  demoSegments: string[];
  /** Plan unique de repli quand il n'y a pas d'enregistrement découpé. */
  demoSrc: string | null;
  /** Piste voix : elle pilote l'animation de la bulle du présentateur. */
  audioSrc: string | null;
  /** Plan parlant de l'avatar, commun à toute la série. */
  avatarSrc: string | null;
  vertical: boolean;
}

/**
 * SÉQUENCE 3 — DÉMO ÉCRAN. Le logiciel joue dans un mockup de navigateur,
 * commenté par la voix off, avec le présentateur en bulle.
 *
 * La répartition change selon le format :
 * - 16:9 — le logiciel occupe le cadre, la bulle vient en bas à droite ;
 * - 9:16 — la frame se partage en quatre parts : 1,5 pour l'avatar en haut,
 *   2,5 pour le logiciel en bas. Sans cette séparation, un enregistrement large
 *   se retrouve rogné et illisible.
 */
export const Demo: React.FC<Props> = ({
  script,
  alignement,
  minutage,
  demoSegments,
  demoSrc,
  audioSrc,
  avatarSrc,
  vertical,
}) => {
  const { height } = useVideoConfig();
  const frame = useCurrentFrame();

  const etapeCourante = minutage.demo.etapes.findIndex(
    (e, i) =>
      frame >= e.debut - minutage.demo.debut &&
      frame < e.debut - minutage.demo.debut + minutage.demo.etapes[i]!.duree,
  );
  const index = etapeCourante === -1 ? 0 : etapeCourante;
  const etape = script.demo.etapes[index];
  const marge = height * 0.05;

  const plans = (
    <>
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
            <PlanEtape etape={e} demoSrc={demoSegments[i] ?? demoSrc} vertical={vertical} />
          </Sequence>
        );
      })}
    </>
  );

  const bulle = (taille: number, retard: number) => (
    <NiveauVoix audioSrc={audioSrc}>
      {(niveau) => (
        <AvatarBulle taille={taille} planSrc={avatarSrc} niveau={niveau} retard={retard} />
      )}
    </NiveauVoix>
  );

  const habillage = (
    <>
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
    </>
  );

  if (vertical) {
    return (
      <AbsoluteFill style={{ backgroundColor: BRAND.colors.fondClair }}>
        <AbsoluteFill
          style={{
            padding: marge,
            paddingBottom: height * 0.16, // place pour les sous-titres et la barre
            display: 'flex',
            flexDirection: 'column',
            gap: marge,
          }}
        >
          <div
            style={{
              flex: 1.5,
              display: 'flex',
              alignItems: 'center',
              justifyContent: 'center',
            }}
          >
            {bulle(0.15, 4)}
          </div>
          <Mockup style={{ flex: 2.5 }}>{plans}</Mockup>
        </AbsoluteFill>
        {habillage}
      </AbsoluteFill>
    );
  }

  return (
    <AbsoluteFill style={{ backgroundColor: BRAND.colors.fondClair }}>
      <AbsoluteFill style={{ padding: marge, paddingBottom: height * 0.11 }}>
        <Mockup style={{ flex: 1 }}>{plans}</Mockup>
      </AbsoluteFill>

      <AbsoluteFill
        style={{
          padding: height * 0.05,
          paddingBottom: height * 0.14,
          alignItems: 'flex-end',
          justifyContent: 'flex-end',
        }}
      >
        {bulle(0.2, 4)}
      </AbsoluteFill>

      {habillage}
    </AbsoluteFill>
  );
};

/**
 * Un plan d'étape : zoom & pan doux vers la zone concernée. Les coordonnées
 * viennent de l'analyse de l'enregistrement.
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
  // En vertical, le fenêtrage ffmpeg a déjà rapproché l'image.
  const echelle = vertical ? 1 : zoomEntree - zoomSortie;

  const z = etape.zone_focus;
  const centre = { x: z.x + z.w / 2, y: z.y + z.h / 2 };
  const decalageX = (0.5 - centre.x) * 100 * (echelle - 1);
  const decalageY = (0.5 - centre.y) * 100 * (echelle - 1);

  return (
    <AbsoluteFill
      style={{
        transform: `scale(${echelle}) translate(${decalageX}%, ${decalageY}%)`,
        transformOrigin: 'center center',
      }}
    >
      {demoSrc ? (
        estImage(demoSrc) ? (
          <Img
            src={staticFile(demoSrc)}
            style={{ width: '100%', height: '100%', objectFit: 'cover' }}
          />
        ) : (
          <OffthreadVideo
            src={staticFile(demoSrc)}
            muted
            style={{ width: '100%', height: '100%', objectFit: 'cover' }}
          />
        )
      ) : (
        <AbsoluteFill style={{ backgroundColor: BRAND.colors.blanc }} />
      )}
      {/* L'annotation vit dans la couche zoomée : elle désigne le champ, pas un
          point fixe de la frame. */}
      <Annotation etape={etape} contreEchelle={1 / echelle} />
    </AbsoluteFill>
  );
};

/** Cercle vert pulsant au point de clic + étiquette flottante avec flèche. */
const Annotation: React.FC<{ etape: EtapeScript; contreEchelle: number }> = ({
  etape,
  contreEchelle,
}) => {
  const frame = useCurrentFrame();
  const { height, width } = useVideoConfig();
  if (!etape.annotation) return null;

  const point = etape.point ?? centreZone(etape.zone_focus);
  const pulsation = (1 + 0.18 * Math.sin((frame / 12) * Math.PI)) * contreEchelle;
  const apparition = interpolate(frame, [4, 16], [0, 1], {
    extrapolateLeft: 'clamp',
    extrapolateRight: 'clamp',
  });
  const rayon = height * 0.028;

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
          left: `${Math.min(point.x * 100, 62)}%`,
          top: `${Math.max(point.y * 100 - 14, 3)}%`,
          background: BRAND.colors.blanc,
          borderRadius: BRAND.radius / 2,
          padding: `${height * 0.012 * contreEchelle}px ${height * 0.02 * contreEchelle}px`,
          transform: `scale(${contreEchelle})`,
          transformOrigin: 'bottom left',
          boxShadow: `0 ${height * 0.008}px ${height * 0.028}px rgba(56,56,56,0.22)`,
          opacity: apparition,
          maxWidth: width * 0.4,
        }}
      >
        <Etiquette fond={BRAND.colors.blanc} taille={0.02}>
          {etape.annotation}
        </Etiquette>
      </div>
    </>
  );
};

const centreZone = (z: Zone) => ({ x: z.x + z.w / 2, y: z.y + z.h / 2 });

const estImage = (chemin: string): boolean => /\.(png|jpe?g|webp)$/i.test(chemin);

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
