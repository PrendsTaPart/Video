import React from 'react';
import {Img, staticFile} from 'remotion';
import {SceneLayout} from '../components/SceneLayout';
import {AnimatedLine} from '../components/AnimatedLines';
import {Counter} from '../components/Counter';
import {Pill} from '../components/Pill';
import {useEnterStyle} from '../components/enter';
import {COLORS} from '../theme';

// S5 · 0:42–0:55 (390f) — LA PLATEFORME (fond blanc cassé)
// Compteur "185" puis label, puis grille de 11 pastilles de domaine
// qui se remplissent en cascade.
const DOMAINS = [
	'Salle',
	'Commandes',
	'Caisse',
	'Carte',
	'Recettes',
	'Stock',
	'HACCP',
	'RH',
	'Clients',
	'Site',
	'Finance',
];

const COUNTER_START = 6;
const LABEL_START = 30;
const GRID_START = 90;
const SCREENSHOT_START = 200;

const DomainPill: React.FC<{label: string; index: number}> = ({label, index}) => {
	const enter = useEnterStyle(index, GRID_START);
	return (
		<div style={{opacity: enter.opacity, transform: enter.transform}}>
			<Pill label={label} active />
		</div>
	);
};

const ScreenshotInset: React.FC = () => {
	const enter = useEnterStyle(0, SCREENSHOT_START);
	return (
		<div
			style={{
				position: 'absolute',
				right: 120,
				bottom: 120,
				opacity: enter.opacity,
				transform: enter.transform,
				width: 420,
				borderRadius: 16,
				overflow: 'hidden',
				border: `2px solid ${COLORS.primary}`,
				boxShadow: '0 20px 50px -20px rgba(15,26,35,0.3)',
				backgroundColor: COLORS.white,
			}}
		>
			<div
				style={{
					display: 'flex',
					alignItems: 'center',
					gap: 8,
					padding: '10px 14px',
					backgroundColor: COLORS.creamDeep,
				}}
			>
				{[COLORS.primary, COLORS.navy, COLORS.primary].map((c, i) => (
					<div key={i} style={{width: 10, height: 10, borderRadius: '50%', backgroundColor: c, opacity: 0.5}} />
				))}
			</div>
			<Img
				src={staticFile('img/screenshot-dashboard-stocks.png')}
				style={{width: '100%', display: 'block'}}
			/>
		</div>
	);
};

export const Scene05: React.FC = () => {
	return (
		<SceneLayout background={COLORS.cream}>
			<div style={{display: 'flex', flexDirection: 'column', alignItems: 'center', gap: 56}}>
				<div style={{display: 'flex', flexDirection: 'column', alignItems: 'center', gap: 12}}>
					<span style={{color: COLORS.primary, fontSize: 112, fontWeight: 700}}>
						<Counter target={185} startFrame={COUNTER_START} />
					</span>
					<AnimatedLine lineIndex={0} startFrame={LABEL_START}>
						<span style={{color: COLORS.navy, fontSize: 40, fontWeight: 600}}>
							outils MCP, cœur restaurant
						</span>
					</AnimatedLine>
				</div>
				<div
					style={{
						display: 'grid',
						gridTemplateColumns: 'repeat(3, 220px)',
						justifyItems: 'center',
						gap: 18,
					}}
				>
					{DOMAINS.map((d, i) => (
						<DomainPill key={d} label={d} index={i} />
					))}
				</div>
			</div>
			<ScreenshotInset />
		</SceneLayout>
	);
};
