import React from 'react';
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

const DomainPill: React.FC<{label: string; index: number}> = ({label, index}) => {
	const enter = useEnterStyle(index, GRID_START);
	return (
		<div style={{opacity: enter.opacity, transform: enter.transform}}>
			<Pill label={label} active />
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
						display: 'flex',
						flexWrap: 'wrap',
						justifyContent: 'center',
						gap: 20,
						maxWidth: 1500,
					}}
				>
					{DOMAINS.map((d, i) => (
						<DomainPill key={d} label={d} index={i} />
					))}
				</div>
			</div>
		</SceneLayout>
	);
};
