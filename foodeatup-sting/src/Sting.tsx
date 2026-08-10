import React from "react";
import {
  AbsoluteFill,
  Audio,
  Img,
  interpolate,
  spring,
  staticFile,
  useCurrentFrame,
  useVideoConfig,
} from "remotion";
import {
  INFINITY_CROISEMENT,
  INFINITY_PATH,
  INFINITY_STROKE,
  INFINITY_VIEWBOX,
} from "./infinity-path";

export type StingProps = {
  baseline: string;
  url: string;
  accent: string;
  fond: string;
  encre: string;
  logo: string;
  avecVo: boolean;
  avecSon: boolean;
  pulsations: number;
  transparent: boolean;
  /** Ferme le plan sur le fond nu, pour que la dernière image égale la première. */
  boucle: boolean;
  /** Appel à l'action de fin. Vide = pas de bloc contact. */
  cta: string;
  telephone: string;
};

export const defauts: StingProps = {
  baseline: "Une infinité de solutions pour gérer votre restaurant.",
  url: "foodeatup.com",
  accent: "#147AFF",
  fond: "#FAF6E3",   // même sable que les 150 épisodes
  encre: "#14202B",
  logo: "foodeatup-logo.png",
  avecVo: true,
  avecSon: true,
  pulsations: 8,
  transparent: false,
  boucle: false,
  cta: "Demander une démo",
  telephone: "06 14 18 92 25",
};

// Repères de la séquence, en secondes. Changer un bloc ici suffit : aucun
// timing n'est écrit en dur ailleurs.
const T = {
  point: [0.0, 0.4],
  trace: [0.4, 2.4],
  fermeture: [2.4, 3.0],
  baseline: [3.0, 3.9],
  url: [3.9, 4.35],
  contact: [4.35, 5.0],
} as const;

const seg = (t: number, [a, b]: readonly [number, number]) =>
  interpolate(t, [a, b], [0, 1], { extrapolateLeft: "clamp", extrapolateRight: "clamp" });

/**
 * Vitesse non linéaire du point : il accélère dans les courbes et ralentit au
 * croisement, atteint à 0, 0,5 et 1 du parcours. On intègre une vitesse
 * sinusoïdale puis on renormalise pour que le tracé se termine bien à 1.
 */
const avance = (u: number) => {
  const N = 240;
  const cumul: number[] = [0];
  let total = 0;
  for (let i = 0; i < N; i++) {
    total += 0.55 + 0.45 * Math.abs(Math.sin(2 * Math.PI * ((i + 0.5) / N)));
    cumul.push(total);
  }
  const cible = u * N;
  const i = Math.min(N - 1, Math.max(0, Math.floor(cible)));
  return (cumul[i] + (cumul[i + 1] - cumul[i]) * (cible - i)) / total;
};

export const Sting: React.FC<StingProps> = ({
  baseline, url, accent, fond, encre, logo, avecVo, avecSon, pulsations, transparent, boucle,
  cta, telephone,
}) => {
  const frame = useCurrentFrame();
  const { fps, width, height, durationInFrames } = useVideoConfig();
  const t = frame / fps;
  const k = Math.min(width, height) / 1080; // échelle commune aux trois formats

  const uTrace = seg(t, T.trace);
  const dessine = avance(uTrace);

  // une pulsation par boucle parcourue
  const phase = dessine * pulsations;
  const pulse = t >= T.trace[0] && t <= T.trace[1]
    ? Math.max(0, 1 - (phase - Math.floor(phase)) * 6) ** 2
    : 0;

  const uFerme = seg(t, T.fermeture);
  const flash = t >= T.fermeture[0] && t < T.fermeture[0] + 2 / fps;
  const versLogo = interpolate(uFerme, [0.25, 1], [0, 1], {
    extrapolateLeft: "clamp", extrapolateRight: "clamp",
  });

  const uBase = seg(t, T.baseline);
  const montee = spring({ frame: frame - T.baseline[0] * fps, fps, config: { damping: 200 } });
  const uUrl = seg(t, T.url);
  const uContact = seg(t, T.contact);
  // En mode boucle le plan se referme sur le fond nu : la dernière image est
  // alors identique à la première, et le raccord ne se voit pas.
  // dernière image rendue, pas la durée : sinon le fondu se termine une image
  // trop tard et la boucle raccorde sur un reste d'opacité.
  const finPlan = (durationInFrames - 1) / fps;
  const sortie = interpolate(t, [finPlan - 8 / fps, finPlan], [1, 0], {
    extrapolateLeft: "clamp", extrapolateRight: "clamp",
  });

  // La marque monte légèrement quand la baseline arrive, pour lui faire place.
  const centreY = height * 0.40 - uBase * height * 0.085;
  const margeMarque = 1080 * k; // le sigle tient la moitié de la hauteur

  return (
    <AbsoluteFill style={{ backgroundColor: transparent ? "transparent" : fond }}>
      <AbsoluteFill style={{ opacity: sortie }}>
      {/* étage de la marque : le tracé, puis le logo plein qui prend le relais */}
      <div
        style={{
          position: "absolute",
          left: "50%",
          top: centreY,
          width: 540 * k,
          height: margeMarque,
          transform: `translate(-50%, -50%) scale(${interpolate(uBase, [0, 1], [1, 0.86])})`,
        }}
      >
        <div style={{ position: "relative", width: "100%", height: "100%" }}>
          <svg
            viewBox={INFINITY_VIEWBOX}
            width="100%"
            height="100%"
            style={{
              position: "absolute",
              inset: 0,
              opacity: 1 - versLogo,
              overflow: "visible",
            }}
          >
            <path
              d={INFINITY_PATH}
              pathLength={1000}
              fill="none"
              stroke={accent}
              strokeWidth={INFINITY_STROKE}
              strokeLinecap="round"
              strokeDasharray={1000}
              strokeDashoffset={1000 * (1 - dessine)}
            />
          </svg>

          <Img
            src={staticFile(logo)}
            style={{
              position: "absolute",
              left: "50%",
              top: "50%",
              width: 900 * k,
              transform: "translate(-50%, -50%)",
              opacity: versLogo,
            }}
          />

          {t < T.fermeture[1] && (
            <PointLumineux
              accent={accent}
              parcours={dessine}
              pulse={pulse}
              opacite={seg(t, T.point) * (1 - versLogo)}
            />
          )}
        </div>
      </div>

      {/* bloc texte, ancré sous la marque */}
      <div
        style={{
          position: "absolute",
          left: "50%",
          top: height * 0.545,
          transform: "translateX(-50%)",
          width: Math.min(width * 0.82, 820 * k),
          display: "flex",
          flexDirection: "column",
          alignItems: "center",
          textAlign: "center",
          fontFamily: "system-ui, -apple-system, 'Segoe UI', Roboto, sans-serif",
        }}
      >
        <div
          style={{
            color: encre,
            fontSize: 44 * k,
            fontWeight: 700,
            letterSpacing: -0.6 * k,
            lineHeight: 1.3,
            textWrap: "balance",
            opacity: uBase,
            transform: `translateY(${(1 - montee) * 12 * k}px)`,
          }}
        >
          {baseline}
        </div>

        <div
          style={{
            marginTop: 34 * k,
            height: 3 * k,
            width: uUrl * 240 * k,
            backgroundColor: accent,
            borderRadius: 2 * k,
          }}
        />

        <div
          style={{
            marginTop: 20 * k,
            color: accent,
            fontSize: 30 * k,
            fontWeight: 700,
            letterSpacing: 1.4 * k,
            opacity: interpolate(uUrl, [0.45, 1], [0, 1], {
              extrapolateLeft: "clamp", extrapolateRight: "clamp",
            }),
          }}
        >
          {url}
        </div>

        {cta !== "" && (
          <Contact
            cta={cta}
            telephone={telephone}
            encre={encre}
            k={k}
            avance={uContact}
          />
        )}
      </div>

      {/* fermeture de la boucle : deux images de flash */}
      {flash && <AbsoluteFill style={{ backgroundColor: "#FFFFFF", opacity: 0.9 }} />}

      </AbsoluteFill>

      {avecSon && <Audio src={staticFile("sting-lit.wav")} volume={0.5} />}
      {avecVo && <Audio src={staticFile("sting-vo.mp3")} volume={1} />}
    </AbsoluteFill>
  );
};

/** Bloc d'appel à l'action : accroche, puis pastille verte avec le numéro. */
const Contact: React.FC<{
  cta: string; telephone: string; encre: string; k: number; avance: number;
}> = ({ cta, telephone, encre, k, avance }) => {
  const VERT = "#25D366";
  const paru = interpolate(avance, [0, 0.45], [0, 1], {
    extrapolateLeft: "clamp", extrapolateRight: "clamp",
  });
  return (
    <div
      style={{
        marginTop: 42 * k,
        display: "flex",
        flexDirection: "column",
        alignItems: "center",
        opacity: paru,
        transform: `translateY(${(1 - paru) * 14 * k}px)`,
      }}
    >
      <div style={{ color: encre, fontSize: 38 * k, fontWeight: 800, letterSpacing: -0.3 * k }}>
        {cta}
      </div>
      <div
        style={{
          marginTop: 18 * k,
          display: "flex",
          alignItems: "center",
          gap: 18 * k,
          backgroundColor: VERT,
          borderRadius: 999,
          padding: `${16 * k}px ${34 * k}px`,
        }}
      >
        <svg width={52 * k} height={52 * k} viewBox="0 0 52 52">
          <circle cx="26" cy="26" r="26" fill="#FFFFFF" />
          <path d="M8 46 L14 38 L20 44 Z" fill="#FFFFFF" />
          <path
            d="M18.5 15.5c-.6 0-1.2.3-1.6.8l-1.4 1.8c-.7.9-.8 2.1-.3 3.1 1.3 2.6 3.1 5 5.3 7.2 2.2 2.2 4.6 4 7.2 5.3 1 .5 2.2.4 3.1-.3l1.8-1.4c.5-.4.8-1 .8-1.6 0-.6-.3-1.2-.8-1.5l-3.1-2c-.8-.5-1.8-.4-2.5.2l-1 .9c-1.6-.9-3-2-4.3-3.3-1.3-1.3-2.4-2.7-3.3-4.3l.9-1c.6-.7.7-1.7.2-2.5l-2-3.1c-.3-.5-.9-.8-1.5-.8Z"
            fill={VERT}
          />
        </svg>
        <div
          style={{
            color: "#FFFFFF",
            fontSize: 46 * k,
            fontWeight: 800,
            letterSpacing: 0.6 * k,
            fontVariantNumeric: "tabular-nums",
          }}
        >
          {telephone}
        </div>
      </div>
    </div>
  );
};

/**
 * Le point qui court sur le tracé. Sa position est lue sur un path hors écran
 * via getPointAtLength : c'est la seule façon de suivre exactement la courbe
 * que stroke-dashoffset est en train de révéler.
 */
const PointLumineux: React.FC<{
  accent: string; parcours: number; pulse: number; opacite: number;
}> = ({ accent, parcours, pulse, opacite }) => {
  const ref = React.useRef<SVGPathElement>(null);
  const [pos, setPos] = React.useState(INFINITY_CROISEMENT);

  React.useEffect(() => {
    const el = ref.current;
    if (!el) return;
    const p = el.getPointAtLength(el.getTotalLength() * Math.min(0.999999, parcours));
    setPos({ x: p.x, y: p.y });
  }, [parcours]);

  return (
    <>
      <svg viewBox={INFINITY_VIEWBOX} style={{ position: "absolute", width: 0, height: 0 }}>
        <path ref={ref} d={INFINITY_PATH} />
      </svg>
      <svg
        viewBox={INFINITY_VIEWBOX}
        width="100%"
        height="100%"
        style={{
          position: "absolute",
          inset: 0,
          opacity: opacite,
          overflow: "visible",
        }}
      >
        <circle
          cx={pos.x} cy={pos.y}
          r={8 + (1 - pulse) * 24}
          fill="none" stroke={accent}
          strokeWidth={2.6 * pulse} opacity={pulse * 0.65}
        />
        <circle cx={pos.x} cy={pos.y} r={10 + pulse * 3} fill={accent} opacity={0.35 + pulse * 0.45} />
        <circle cx={pos.x} cy={pos.y} r={5 + pulse * 2.5} fill="#FFFFFF" />
      </svg>
    </>
  );
};
