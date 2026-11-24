#!/usr/bin/env node
// Exporte les sous-titres de data/timeline.json en SRT (renders/sous-titres.srt).
import { readFileSync, writeFileSync } from 'node:fs';
const T = JSON.parse(readFileSync(new URL('../data/timeline.json', import.meta.url), 'utf8'));
const ts = (s) => {
  const ms = Math.round(s * 1000), h = Math.floor(ms / 3600000), m = Math.floor(ms / 60000) % 60;
  const sec = Math.floor(ms / 1000) % 60, r = ms % 1000, p = (n, w = 2) => String(n).padStart(w, '0');
  return `${p(h)}:${p(m)}:${p(sec)},${p(r, 3)}`;
};
writeFileSync(new URL('../renders/sous-titres.srt', import.meta.url),
  T.subtitles.map((s, i) => `${i + 1}\n${ts(s.start)} --> ${ts(s.end)}\n${s.text}\n`).join('\n'));
console.log('renders/sous-titres.srt');
