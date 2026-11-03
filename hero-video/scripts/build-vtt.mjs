#!/usr/bin/env node
// Regenerates renders/hero-video.vtt from data/hero.json — one cue per beat
// that has a vo.text. Kept separate from the video (no burned-in text in the
// composition itself) for accessibility and SEO citability.
import { readFileSync, writeFileSync } from 'node:fs';
import { fileURLToPath } from 'node:url';
import path from 'node:path';

const ROOT = path.dirname(path.dirname(fileURLToPath(import.meta.url)));
const hero = JSON.parse(readFileSync(path.join(ROOT, 'data/hero.json'), 'utf8'));

function ts(seconds) {
  const h = Math.floor(seconds / 3600);
  const m = Math.floor((seconds % 3600) / 60);
  const s = Math.floor(seconds % 60);
  const ms = Math.round((seconds - Math.floor(seconds)) * 1000);
  const pad = (n, len = 2) => String(n).padStart(len, '0');
  return `${pad(h)}:${pad(m)}:${pad(s)}.${pad(ms, 3)}`;
}

const cues = [];
for (const seq of hero.sequences) {
  for (const beat of seq.beats) {
    if (beat.vo && beat.vo.text) {
      cues.push({ start: beat.fromSeconds, end: beat.fromSeconds + beat.durationSeconds, text: beat.vo.text });
    }
  }
}
cues.sort((a, b) => a.start - b.start);

const lines = ['WEBVTT', ''];
cues.forEach((cue, i) => {
  lines.push(String(i + 1));
  lines.push(`${ts(cue.start)} --> ${ts(cue.end)}`);
  lines.push(cue.text);
  lines.push('');
});

const outPath = path.join(ROOT, 'renders/hero-video.vtt');
writeFileSync(outPath, lines.join('\n'));
console.log(`build-vtt: wrote ${cues.length} cues to ${outPath}`);
