import { blocsDuScript } from './src/pipeline/voix.ts';
import { pourLaVoix } from './src/pipeline/prononciation.ts';
import { ScriptSchema } from './src/schema/index.ts';
import { lireJson } from './src/util/chemins.ts';
const s = ScriptSchema.parse(lireJson(process.argv[2]));
for (const b of blocsDuScript(s)) console.log(JSON.stringify({ id: b.id, texte: pourLaVoix(b.texte) }));
