import { z } from 'zod';

/* ───────────────────────── analyse.json ───────────────────────── */

export const ZoneSchema = z.object({
  x: z.number().min(0).max(1),
  y: z.number().min(0).max(1),
  w: z.number().min(0).max(1),
  h: z.number().min(0).max(1),
});
export type Zone = z.infer<typeof ZoneSchema>;

export const ActionSchema = z.object({
  t: z.number().nonnegative(),
  type: z.enum(['clic', 'saisie', 'selection', 'validation', 'ouverture', 'defilement']),
  cible: z.string().min(1),
  zone: ZoneSchema,
  texte_visible: z.string().default(''),
});

export const EtapeAnalyseSchema = z.object({
  numero: z.number().int().positive(),
  titre: z.string().min(1),
  debut: z.number().nonnegative(),
  fin: z.number().nonnegative(),
  actions: z.array(z.number().int().nonnegative()).default([]),
  zone_focus: ZoneSchema,
});

export const ZoneSensibleSchema = z.object({
  t: z.number().nonnegative(),
  fin: z.number().nonnegative().optional(),
  zone: ZoneSchema.optional(),
  raison: z.string().min(1),
});

export const AnalyseSchema = z.object({
  duree: z.number().positive(),
  resolution: z.tuple([z.number().int(), z.number().int()]),
  fps: z.number().positive().default(30),
  ecrans: z.array(z.object({ t: z.number().nonnegative(), nom: z.string() })).default([]),
  actions: z.array(ActionSchema).default([]),
  etapes: z.array(EtapeAnalyseSchema).min(1),
  zones_sensibles: z.array(ZoneSensibleSchema).default([]),
});
export type Analyse = z.infer<typeof AnalyseSchema>;

/* ───────────────────────── fiche.json ───────────────────────── */

export const OutilMcpSchema = z.object({
  nom: z.string().min(1),
  role: z.string().min(1),
  parametres_obligatoires: z.array(z.string()).default([]),
  parametres_optionnels: z.array(z.string()).default([]),
  exemple_appel: z.record(z.unknown()).default({}),
});

export const FicheSchema = z.object({
  fonctionnalite: z.string().min(1),
  a_quoi_ca_sert: z.string().min(1),
  pour_qui: z.string().min(1),
  prerequis: z.array(z.string()).default([]),
  champs_cles: z
    .array(
      z.object({
        nom: z.string(),
        obligatoire: z.boolean(),
        explication: z.string(),
      }),
    )
    .default([]),
  outils_mcp: z.array(OutilMcpSchema).default([]),
  bonnes_pratiques: z.array(z.string()).default([]),
  erreurs_frequentes: z.array(z.string()).default([]),
  cas_usage: z
    .array(
      z.object({
        titre: z.string(),
        contexte: z.string(),
        resultat_attendu: z.string(),
      }),
    )
    .default([]),
  astuces: z
    .array(
      z.object({
        titre: z.string(),
        contenu: z.string(),
        niveau: z.enum(['debutant', 'pro']),
      }),
    )
    .default([]),
  prompt_claude: z.object({
    titre: z.string().min(1),
    texte: z.string().min(1),
    variables: z.array(z.string()).default([]),
    outil_mcp: z.string().min(1),
  }),
  /** Origine de chaque bloc : « frame 00:12 » ou « schéma create_facture ». */
  sources: z.record(z.string()).default({}),
  /** Ce qui n'a pas pu être vérifié. Doit être vide pour publier. */
  a_verifier: z.array(z.string()).default([]),
});
export type Fiche = z.infer<typeof FicheSchema>;

/* ───────────────────────── script.json ───────────────────────── */

export const EtapeScriptSchema = z.object({
  numero: z.number().int().positive(),
  titre: z.string().min(1),
  voix: z.string().min(1),
  debut_source: z.number().nonnegative(),
  fin_source: z.number().nonnegative(),
  zone_focus: ZoneSchema,
  annotation: z.string().default(''),
  /** Point de clic à annoter, en coordonnées normalisées. */
  point: z.object({ x: z.number(), y: z.number() }).optional(),
});

export const ScriptSchema = z.object({
  meta: z.object({
    module: z.string().min(1),
    numero: z.number().int().positive(),
    titre: z.string().min(1),
    titre_court: z.string().min(1).max(28),
    slug: z.string().min(1),
  }),
  hook: z.object({
    texte: z.string().min(1),
    promesse: z.string().min(1),
    duree: z.number().positive().default(5),
    alternatives: z.array(z.string()).default([]),
  }),
  intro: z.object({ texte: z.string().min(1), duree: z.number().positive().default(3) }),
  demo: z.object({ etapes: z.array(EtapeScriptSchema).min(3) }),
  segment_claude: z.object({
    accroche: z.string().min(1),
    voix: z.string().min(1),
    prompt: z.object({
      texte: z.string().min(1),
      variables: z.array(z.string()).default([]),
      outil_mcp: z.string().default(''),
    }),
    resultat_affiche: z.object({
      titre: z.string().min(1),
      lignes: z.array(z.string()).default([]),
    }),
    duree: z.number().positive().default(16),
  }),
  punchline: z.object({
    texte: z.string().min(1),
    duree: z.number().positive().default(5),
    alternatives: z.array(z.string()).default([]),
  }),
  seo: z.object({
    titre: z.string().min(1).max(60),
    description: z.string().min(120).max(155),
    mots_cles: z.array(z.string()).default([]),
    youtube_titre: z.string().min(1).max(70),
    youtube_description: z.string().min(1),
    youtube_tags: z.array(z.string()).default([]),
  }),
});
export type Script = z.infer<typeof ScriptSchema>;
export type EtapeScript = z.infer<typeof EtapeScriptSchema>;

/* ───────────────────────── voix ───────────────────────── */

export const MotAligneSchema = z.object({
  mot: z.string(),
  debut: z.number().nonnegative(),
  fin: z.number().nonnegative(),
});

export const BlocVoixSchema = z.object({
  id: z.string(),
  fichier: z.string(),
  debut: z.number().nonnegative(),
  duree: z.number().nonnegative(),
  texte: z.string(),
  mots: z.array(MotAligneSchema).default([]),
});

export const AlignementSchema = z.object({
  duree_totale: z.number().nonnegative(),
  blocs: z.array(BlocVoixSchema),
});
export type Alignement = z.infer<typeof AlignementSchema>;
export type BlocVoix = z.infer<typeof BlocVoixSchema>;

/* ───────────────────────── rendu.json ───────────────────────── */

export const RenduSchema = z.object({
  duree: z.number().positive(),
  fichiers: z.array(z.object({ chemin: z.string(), octets: z.number() })),
  sequences: z.array(
    z.object({ nom: z.string(), debut: z.number(), fin: z.number() }),
  ),
  chapitres_youtube: z.array(z.object({ timecode: z.string(), titre: z.string() })),
  avertissements: z.array(z.string()).default([]),
});
export type Rendu = z.infer<typeof RenduSchema>;

/* ───────────────────────── publication.json ───────────────────────── */

export const PublicationSchema = z.object({
  rapidocms: z
    .object({
      video_url: z.string().url(),
      video_vertical_url: z.string().url().optional(),
      thumbnail_url: z.string().url(),
      thumbnail_vertical_url: z.string().url().optional(),
      empreintes: z.record(z.string()).default({}),
      publie_le: z.string(),
    })
    .optional(),
  youtube: z
    .object({
      url: z.string().url(),
      video_id: z.string(),
      publie_le: z.string(),
    })
    .optional(),
  site: z
    .object({
      url: z.string().url(),
      tutoriel_id: z.union([z.string(), z.number()]).optional(),
      publie_le: z.string(),
    })
    .optional(),
});
export type Publication = z.infer<typeof PublicationSchema>;

/* ───────────────────────── qa.json ───────────────────────── */

export const QaSchema = z.object({
  verte: z.boolean(),
  controles: z.array(
    z.object({
      famille: z.string(),
      intitule: z.string(),
      statut: z.enum(['ok', 'avertissement', 'echec']),
      detail: z.string().default(''),
    }),
  ),
  produit_le: z.string(),
});
export type Qa = z.infer<typeof QaSchema>;

/** Props injectées dans les compositions Remotion. */
export const PropsVideoSchema = z.object({
  script: ScriptSchema,
  alignement: AlignementSchema.nullable().default(null),
  /** Un screencast pré-traité par étape de démonstration (séquence 3). */
  demoSegments: z.array(z.string()).default([]),
  /** Plan unique de repli : capture fixe ou écran de la banque. */
  demoSrc: z.string().nullable().default(null),
  /** Vignette du tutoriel (MCP RapidoCRM tuto), affichée en ouverture. */
  vignetteSrc: z.string().nullable().default(null),
  audioSrc: z.string().nullable().default(null),
});
export type PropsVideo = z.infer<typeof PropsVideoSchema>;
