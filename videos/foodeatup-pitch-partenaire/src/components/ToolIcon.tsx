import React from 'react';
import {COLORS} from '../theme';

/** Icône générique et abstraite représentant "un logiciel" — aucune IP tierce. */
export const ToolIcon: React.FC<{size?: number; opacity?: number}> = ({
	size = 56,
	opacity = 1,
}) => {
	return (
		<div
			style={{
				width: size,
				height: size,
				borderRadius: size * 0.24,
				border: `2px solid ${COLORS.navy}`,
				opacity,
				display: 'flex',
				alignItems: 'center',
				justifyContent: 'center',
			}}
		>
			<div
				style={{
					width: size * 0.4,
					height: size * 0.4,
					borderRadius: size * 0.1,
					backgroundColor: COLORS.navy,
					opacity: 0.7,
				}}
			/>
		</div>
	);
};
