import React from 'react';
import {AbsoluteFill} from 'remotion';
import {COLORS, FONT_FAMILY, GRID} from '../theme';

export const SceneLayout: React.FC<{
	background?: string;
	children: React.ReactNode;
}> = ({background = COLORS.white, children}) => {
	return (
		<AbsoluteFill
			style={{
				backgroundColor: background,
				fontFamily: FONT_FAMILY,
			}}
		>
			<AbsoluteFill
				style={{
					padding: GRID.margin,
					display: 'flex',
					flexDirection: 'column',
					alignItems: 'center',
					justifyContent: 'center',
				}}
			>
				{children}
			</AbsoluteFill>
		</AbsoluteFill>
	);
};
