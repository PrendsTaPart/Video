import React from 'react';
import {SceneLayout} from '../components/SceneLayout';
import {StepCard} from '../components/StepCard';
import {COLORS} from '../theme';

// S4 · 0:28–0:42 (420f) — LE CAS D'USAGE SIGNATURE
// Chaîne horizontale de 4 cartes qui s'allument séquentiellement, 500ms
// chacune, avec une coche à la fin de chaque étape. Aucun texte de titre
// n'est prévu par le storyboard : les 4 cartes portent le message seules.
const STEPS = [
	{label: 'Promo −10 % appliquée en caisse', imageSrc: 'img/payment-card.webp'},
	{label: 'Post Instagram + Facebook publiés', imageSrc: undefined},
	{label: 'SMS envoyé aux clients ciblés', imageSrc: 'img/whatsapp-icon.jpeg'},
	{label: 'Commandes prises en autonomie', imageSrc: 'img/pos-terminal-v2s.png'},
];

const CARDS_START = 6;

export const Scene04: React.FC = () => {
	return (
		<SceneLayout background={COLORS.cream}>
			<div
				style={{
					display: 'flex',
					flexDirection: 'row',
					gap: 28,
					width: '100%',
				}}
			>
				{STEPS.map((step, i) => (
					<StepCard
						key={step.label}
						index={i}
						label={step.label}
						imageSrc={step.imageSrc}
						startFrame={CARDS_START}
					/>
				))}
			</div>
		</SceneLayout>
	);
};
