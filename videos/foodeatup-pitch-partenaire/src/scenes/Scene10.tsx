import React from 'react';
import {SceneLayout} from '../components/SceneLayout';
import {useEnterStyle} from '../components/enter';
import {COLORS} from '../theme';

// S10 · 1:40–1:50 (300f) — L'ÉCONOMIE DU PARTENARIAT
// Trois lignes tarifaires, apparition séquentielle.
const LINES = [
	{label: 'Marque blanche — 10 000 € + 999 €/an', start: 10},
	{label: 'Licence régionale — 100 000 € + 1 000 €/mois', start: 90},
	{label: 'Commission — 30 % sur la consommation IA', start: 170},
];

const TariffLine: React.FC<{label: string; start: number}> = ({label, start}) => {
	const enter = useEnterStyle(0, start);
	return (
		<div
			style={{
				opacity: enter.opacity,
				transform: enter.transform,
				display: 'flex',
				alignItems: 'center',
				gap: 24,
			}}
		>
			<div
				style={{
					width: 14,
					height: 14,
					borderRadius: '50%',
					backgroundColor: COLORS.primary,
					flexShrink: 0,
				}}
			/>
			<span style={{color: COLORS.navy, fontSize: 46, fontWeight: 600}}>{label}</span>
		</div>
	);
};

export const Scene10: React.FC = () => {
	return (
		<SceneLayout background={COLORS.white}>
			<div style={{display: 'flex', flexDirection: 'column', gap: 48, alignItems: 'flex-start'}}>
				{LINES.map((l) => (
					<TariffLine key={l.label} label={l.label} start={l.start} />
				))}
			</div>
		</SceneLayout>
	);
};
