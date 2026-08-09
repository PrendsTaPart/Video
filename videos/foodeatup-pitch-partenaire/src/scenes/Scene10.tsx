import React from 'react';
import {SceneLayout} from '../components/SceneLayout';
import {AnimatedLine} from '../components/AnimatedLines';
import {useEnterStyle} from '../components/enter';
import {COLORS} from '../theme';

// S10 · 1:40–1:50 (300f) — L'ÉCONOMIE DU PARTENARIAT
// Catalogue tarifaire complet — source unique : src/data/pricing.ts du
// dépôt food-heartbeat-site (PLANS + ADDONS). Forfaits en cartes, options
// à la carte en grille, pour tenir toute l'info sans sacrifier la taille
// du texte.

const PLANS = [
	{name: 'StockVision', price: '49 €', unit: '/mois'},
	{name: '+ OCR + HACCP', price: '99 €', unit: '/mois'},
	{name: '+ Prédiction IA', price: '119 €', unit: '/mois'},
	{name: 'Premiers Pas', price: '0 €', unit: 'an 1, puis 49 €/an'},
];

const OPTIONS = [
	{name: 'Site IA', price: '29 €/mois'},
	{name: 'Jarvis vocal', price: '49 €/mois/siège'},
	{name: 'Marketing & Commercial', price: '99 €/mois'},
	{name: 'Caroline téléphonique', price: '79 €/mois'},
	{name: 'PrediBot WhatsApp', price: '49 €/mois'},
	{name: '+ établissement PrediBot', price: '39 €/mois'},
	{name: 'Avis & réputation', price: '29 €/mois'},
	{name: 'Iris communication', price: '49 €/mois'},
	{name: 'Connecteurs caisse & livraison', price: '39 €/mois'},
];

const PLANS_START = 6;
const OPTIONS_START = 90;

const PlanCard: React.FC<{name: string; price: string; unit: string; index: number}> = ({
	name,
	price,
	unit,
	index,
}) => {
	const enter = useEnterStyle(index, PLANS_START);
	return (
		<div
			style={{
				opacity: enter.opacity,
				transform: enter.transform,
				flex: 1,
				display: 'flex',
				flexDirection: 'column',
				alignItems: 'center',
				gap: 14,
				padding: '34px 22px',
				borderRadius: 22,
				border: `2px solid ${COLORS.primary}`,
				backgroundColor: COLORS.creamDeep,
			}}
		>
			<span style={{color: COLORS.navy, fontSize: 30, fontWeight: 700, textAlign: 'center'}}>
				{name}
			</span>
			<span style={{color: COLORS.primary, fontSize: 56, fontWeight: 700}}>{price}</span>
			<span style={{color: COLORS.navy, fontSize: 23, fontWeight: 500, opacity: 0.75}}>{unit}</span>
		</div>
	);
};

const OptionRow: React.FC<{name: string; price: string; index: number}> = ({name, price, index}) => {
	const enter = useEnterStyle(index, OPTIONS_START);
	return (
		<div
			style={{
				opacity: enter.opacity,
				transform: enter.transform,
				display: 'flex',
				alignItems: 'baseline',
				justifyContent: 'space-between',
				gap: 16,
				padding: '18px 24px',
				borderRadius: 14,
				backgroundColor: COLORS.creamDeep,
			}}
		>
			<span style={{color: COLORS.navy, fontSize: 30, fontWeight: 600}}>{name}</span>
			<span style={{color: COLORS.primary, fontSize: 30, fontWeight: 700, whiteSpace: 'nowrap'}}>
				{price}
			</span>
		</div>
	);
};

export const Scene10: React.FC = () => {
	return (
		<SceneLayout background={COLORS.cream}>
			<div style={{display: 'flex', flexDirection: 'column', gap: 34, width: '100%'}}>
				<div style={{display: 'flex', flexDirection: 'row', gap: 22, width: '100%'}}>
					{PLANS.map((p, i) => (
						<PlanCard key={p.name} index={i} {...p} />
					))}
				</div>

				<AnimatedLine lineIndex={0} startFrame={OPTIONS_START - 20}>
					<span style={{color: COLORS.navy, fontSize: 34, fontWeight: 700}}>
						Options à la carte, empilables
					</span>
				</AnimatedLine>

				<div
					style={{
						display: 'grid',
						gridTemplateColumns: 'repeat(3, 1fr)',
						gap: 18,
						width: '100%',
					}}
				>
					{OPTIONS.map((o, i) => (
						<OptionRow key={o.name} index={i} {...o} />
					))}
				</div>
			</div>
		</SceneLayout>
	);
};
