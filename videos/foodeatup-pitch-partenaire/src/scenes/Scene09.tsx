import React from 'react';
import {Easing, interpolate, useCurrentFrame} from 'remotion';
import {SceneLayout} from '../components/SceneLayout';
import {COLORS, ENTER_BEZIER} from '../theme';

// S9 · 1:26–1:40 (420f) — LES 3 PORTES D'ENTRÉE PARTENAIRE (scène pivot)
// Trois panneaux verticaux qui montent l'un après l'autre.

const easing = Easing.bezier(...ENTER_BEZIER);

const PANELS = [
	{number: '①', title: 'INTÉGRER', subtitle: 'Branchez nos MCP dans votre produit.', start: 10},
	{number: '②', title: 'DISTRIBUER', subtitle: 'Notre suite sous votre marque.', start: 130},
	{number: '③', title: 'PRESCRIRE', subtitle: 'Vendez, nous opérons.', start: 250},
];

const RISE_DURATION = 40;

const Panel: React.FC<{number: string; title: string; subtitle: string; start: number}> = ({
	number,
	title,
	subtitle,
	start,
}) => {
	const frame = useCurrentFrame();
	const t = interpolate(frame, [start, start + RISE_DURATION], [0, 1], {
		extrapolateLeft: 'clamp',
		extrapolateRight: 'clamp',
		easing,
	});
	const translateY = interpolate(t, [0, 1], [120, 0]);
	return (
		<div
			style={{
				flex: 1,
				opacity: t,
				transform: `translateY(${translateY}px)`,
				display: 'flex',
				flexDirection: 'column',
				alignItems: 'center',
				gap: 20,
				padding: '52px 32px',
				borderRadius: 24,
				border: `2px solid ${COLORS.primary}`,
				backgroundColor: 'rgba(20,122,255,0.07)',
				minHeight: 460,
				boxSizing: 'border-box',
				justifyContent: 'center',
			}}
		>
			<span style={{color: COLORS.primary, fontSize: 50}}>{number}</span>
			<span style={{color: COLORS.navy, fontSize: 44, fontWeight: 700, letterSpacing: 1}}>
				{title}
			</span>
			<span
				style={{
					color: COLORS.navy,
					fontSize: 30,
					fontWeight: 500,
					textAlign: 'center',
					opacity: 0.85,
				}}
			>
				« {subtitle} »
			</span>
		</div>
	);
};

export const Scene09: React.FC = () => {
	return (
		<SceneLayout background={COLORS.white}>
			<div style={{display: 'flex', flexDirection: 'row', gap: 32, width: '100%'}}>
				{PANELS.map((p) => (
					<Panel key={p.title} {...p} />
				))}
			</div>
		</SceneLayout>
	);
};
