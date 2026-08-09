import React from 'react';
import {useEnterStyle} from './enter';

/**
 * Bloc de lignes de texte qui entrent l'une après l'autre avec la
 * grammaire commune (translateY 24px + opacité, 400ms, stagger 80ms).
 */
export const AnimatedLines: React.FC<{
	lines: string[];
	startFrame?: number;
	style?: React.CSSProperties;
	lineStyle?: React.CSSProperties;
	gap?: number;
}> = ({lines, startFrame = 0, style, lineStyle, gap = 16}) => {
	return (
		<div style={{display: 'flex', flexDirection: 'column', gap, ...style}}>
			{lines.map((line, i) => (
				<AnimatedLine key={line} lineIndex={i} startFrame={startFrame} style={lineStyle}>
					{line}
				</AnimatedLine>
			))}
		</div>
	);
};

export const AnimatedLine: React.FC<{
	lineIndex: number;
	startFrame?: number;
	style?: React.CSSProperties;
	children: React.ReactNode;
}> = ({lineIndex, startFrame = 0, style, children}) => {
	const enter = useEnterStyle(lineIndex, startFrame);
	return (
		<div
			style={{
				opacity: enter.opacity,
				transform: enter.transform,
				...style,
			}}
		>
			{children}
		</div>
	);
};
