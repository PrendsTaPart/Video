import React from 'react';
import {Img, staticFile} from 'remotion';
import {SceneLayout} from '../components/SceneLayout';
import {useEnterStyle} from '../components/enter';
import {COLORS} from '../theme';

// S8 · 1:16–1:26 (300f) — LA PREUVE
// Quatre cartouches chiffrées, apparition décalée, puis les vrais logos
// des programmes / labels obtenus (preuve visuelle, pas seulement du texte).
// Source : cas client GoSushi + bloc "Preuves & chiffres" du site
// (food-heartbeat-site/src/routes/index.tsx).
const CARTOUCHES = [
	{label: 'GoSushi : 5 outils remplacés par 1', start: 0},
	{label: '−50 % de temps en back-office', start: 45},
	{label: '100 % HACCP dématérialisé', start: 90},
	{label: '−17 % en abonnement annuel', start: 135},
];

const LOGOS = [
	'img/aws-startups-logo.png',
	'img/nvidia-inception-logo.png',
	'img/logo-la-french-tech.jpeg',
	'img/logo-bpifrance-yellow.png',
	'img/logo-france-2030.png',
	'img/logo-vivatechnology.png',
	'img/logo-lescalator.jpeg',
];
const LOGO_STRIP_START = 190;

const Cartouche: React.FC<{label: string; start: number}> = ({label, start}) => {
	const enter = useEnterStyle(0, start);
	return (
		<div
			style={{
				opacity: enter.opacity,
				transform: enter.transform,
				display: 'flex',
				alignItems: 'center',
				gap: 20,
				padding: '26px 36px',
				borderRadius: 16,
				borderLeft: `6px solid ${COLORS.primary}`,
				backgroundColor: COLORS.creamDeep,
				width: 720,
			}}
		>
			<span style={{color: COLORS.navy, fontSize: 42, fontWeight: 600}}>{label}</span>
		</div>
	);
};

const LogoBadge: React.FC<{src: string; index: number}> = ({src, index}) => {
	const enter = useEnterStyle(index, LOGO_STRIP_START);
	return (
		<div
			style={{
				opacity: enter.opacity,
				transform: enter.transform,
				width: 118,
				height: 118,
				borderRadius: 16,
				backgroundColor: COLORS.white,
				border: '1px solid rgba(15,26,35,0.12)',
				display: 'flex',
				alignItems: 'center',
				justifyContent: 'center',
				padding: 14,
				boxSizing: 'border-box',
			}}
		>
			<Img src={staticFile(src)} style={{width: '100%', height: '100%', objectFit: 'contain'}} />
		</div>
	);
};

export const Scene08: React.FC = () => {
	return (
		<SceneLayout background={COLORS.cream}>
			<div style={{display: 'flex', flexDirection: 'column', alignItems: 'center', gap: 48}}>
				<div
					style={{
						display: 'grid',
						gridTemplateColumns: 'repeat(2, 1fr)',
						gap: 24,
					}}
				>
					{CARTOUCHES.map((c) => (
						<Cartouche key={c.label} label={c.label} start={c.start} />
					))}
				</div>
				<div style={{display: 'flex', flexDirection: 'row', gap: 20}}>
					{LOGOS.map((src, i) => (
						<LogoBadge key={src} src={src} index={i} />
					))}
				</div>
			</div>
		</SceneLayout>
	);
};
