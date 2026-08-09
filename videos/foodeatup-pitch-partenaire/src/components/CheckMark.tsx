import React from 'react';
import {interpolate} from 'remotion';
import {COLORS} from '../theme';

/** Coche vectorielle, tracé animé par un progress 0→1. */
export const CheckMark: React.FC<{
	progress: number;
	size?: number;
	color?: string;
}> = ({progress, size = 32, color = COLORS.navy}) => {
	const dash = interpolate(progress, [0, 1], [24, 0], {
		extrapolateLeft: 'clamp',
		extrapolateRight: 'clamp',
	});
	return (
		<svg width={size} height={size} viewBox="0 0 24 24" fill="none">
			<path
				d="M4 12.5L9.5 18L20 6"
				stroke={color}
				strokeWidth={2.5}
				strokeLinecap="round"
				strokeLinejoin="round"
				strokeDasharray={24}
				strokeDashoffset={dash}
			/>
		</svg>
	);
};
