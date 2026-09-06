import { execFile } from 'node:child_process';
import { promisify } from 'node:util';
import ffmpegStatic from 'ffmpeg-static';
import ffprobeStatic from 'ffprobe-static';

const execFileAsync = promisify(execFile);

/**
 * ffmpeg du système s'il est installé, sinon le binaire statique embarqué par
 * les paquets `ffmpeg-static` / `ffprobe-static`. Le pipeline tourne donc sans
 * installation préalable, tout en profitant d'un ffmpeg local s'il existe.
 */
const binaires: Record<'ffmpeg' | 'ffprobe', string> = {
  ffmpeg: process.env.FFMPEG_PATH ?? (ffmpegStatic as unknown as string) ?? 'ffmpeg',
  ffprobe: process.env.FFPROBE_PATH ?? ffprobeStatic.path ?? 'ffprobe',
};

export const lancer = async (
  binaire: 'ffmpeg' | 'ffprobe',
  args: string[],
): Promise<string> => {
  try {
    const { stdout, stderr } = await execFileAsync(binaires[binaire], args, {
      maxBuffer: 64 * 1024 * 1024,
    });
    return stdout || stderr;
  } catch (e) {
    const err = e as NodeJS.ErrnoException & { stderr?: string };
    if (err.code === 'ENOENT') {
      throw new Error(
        `${binaire} est introuvable. Installez ffmpeg (brew install ffmpeg / apt install ffmpeg).`,
      );
    }
    throw new Error(`${binaire} a échoué : ${err.stderr ?? err.message}`);
  }
};

export interface InfosMedia {
  duree: number;
  largeur: number;
  hauteur: number;
  fps: number;
}

export const sonder = async (fichier: string): Promise<InfosMedia> => {
  const brut = await lancer('ffprobe', [
    '-v', 'error',
    '-select_streams', 'v:0',
    '-show_entries', 'stream=width,height,r_frame_rate:format=duration',
    '-of', 'json',
    fichier,
  ]);
  const json = JSON.parse(brut) as {
    streams?: { width: number; height: number; r_frame_rate: string }[];
    format?: { duration: string };
  };
  const flux = json.streams?.[0];
  if (!flux) throw new Error(`Aucun flux vidéo dans ${fichier}`);
  const [num, den] = flux.r_frame_rate.split('/').map(Number);
  return {
    duree: Number(json.format?.duration ?? 0),
    largeur: flux.width,
    hauteur: flux.height,
    fps: den ? (num as number) / den : (num as number),
  };
};

/** Durée d'un fichier audio, en secondes. */
export const dureeAudio = async (fichier: string): Promise<number> => {
  const brut = await lancer('ffprobe', [
    '-v', 'error',
    '-show_entries', 'format=duration',
    '-of', 'default=noprint_wrappers=1:nokey=1',
    fichier,
  ]);
  return Number(brut.trim());
};
