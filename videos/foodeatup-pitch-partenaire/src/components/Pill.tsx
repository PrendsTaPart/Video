import React from 'react';
import {COLORS} from '../theme';

export const Pill: React.FC<{
	label: string;
	active: boolean;
	textColor?: string;
	style?: React.CSSProperties;
}> = ({label, active, textColor = COLORS.navy, style}) => {
	return (
		<div
			style={{
				padding: '16px 30px',
				borderRadius: 999,
				border: `2px solid ${COLORS.primary}`,
				backgroundColor: active ? COLORS.primary : 'transparent',
				color: active ? COLORS.white : textColor,
				fontSize: 28,
				fontWeight: 600,
				whiteSpace: 'nowrap',
				transition: 'none',
				...style,
			}}
		>
			{label}
		</div>
	);
};
