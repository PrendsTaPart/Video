// Étape 1 — Extraction d'un cours Académie FoodEatUp (+ ses prompts) en JSON.
//
// La plateforme (academie.foodeatup.com) est une SPA React ; son contenu réel
// vit dans Supabase (tables `cours`, `prompts`, `prompt_variable_defaults`).
// On appelle directement l'API REST Supabase (PostgREST) plutôt que de
// scraper le HTML rendu — plus robuste, et pas besoin de navigateur.
//
// La clé ci-dessous est la clé publique "anon" du projet Supabase : elle est
// déjà exposée telle quelle dans le bundle JS chargé par n'importe quel
// visiteur du site (protégée côté serveur par des policies RLS, pas un
// secret à garder caché) — donc pas de .env nécessaire pour celle-ci.
//
// Usage :
//   node scripts/01-extract-course.mjs --slug feu-stocks-inventaire
//   node scripts/01-extract-course.mjs --slug feu-stocks-inventaire --out cours.json

const SUPABASE_URL = "https://trdsiuaionvxwjrabfbo.supabase.co";
const SUPABASE_ANON_KEY =
  "eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9.eyJpc3MiOiJzdXBhYmFzZSIsInJlZiI6InRyZHNpdWFpb252eHdqcmFiZmJvIiwicm9sZSI6ImFub24iLCJpYXQiOjE3ODA2MzQyNzEsImV4cCI6MjA5NjIxMDI3MX0.PDaZoboCrCRxGRmNnjCr3TyQKc-w5uHLkImaZs0Lq5A";

function flag(name, def = null) {
  const i = process.argv.indexOf(`--${name}`);
  return i >= 0 && i + 1 < process.argv.length ? process.argv[i + 1] : def;
}

async function supabaseGet(path) {
  const res = await fetch(`${SUPABASE_URL}/rest/v1/${path}`, {
    headers: {
      apikey: SUPABASE_ANON_KEY,
      Authorization: `Bearer ${SUPABASE_ANON_KEY}`,
    },
  });
  if (!res.ok) throw new Error(`Supabase ${path} -> HTTP ${res.status}: ${await res.text()}`);
  return res.json();
}

async function main() {
  const slug = flag("slug");
  const outPath = flag("out", "course.json");
  if (!slug) {
    console.error("Usage: node 01-extract-course.mjs --slug <slug-du-cours> [--out fichier.json]");
    process.exit(1);
  }

  console.error(`· Recherche du cours "${slug}"...`);
  const courses = await supabaseGet(`cours?slug=eq.${encodeURIComponent(slug)}`);
  if (!courses.length) throw new Error(`Aucun cours trouvé pour le slug "${slug}"`);
  const course = courses[0];
  console.error(`  trouvé : "${course.titre}" (id ${course.id})`);

  console.error("· Récupération des prompts associés...");
  const prompts = await supabaseGet(
    `prompts?cours_id=eq.${course.id}&order=ordre.asc`,
  );
  console.error(`  ${prompts.length} prompt(s) trouvé(s)`);

  console.error("· Résolution des valeurs par défaut des variables...");
  const defaults = await supabaseGet("prompt_variable_defaults");
  const defaultsByKey = Object.fromEntries(defaults.map((d) => [d.cle, d]));

  // Normalise `variables`: le champ déclaré en base est incohérent selon les
  // prompts — parfois un tableau de `{key,label,placeholder}` (ex. les
  // prompts CRM), parfois vide `{}` / `[]` alors même que le texte du prompt
  // contient des `{placeholder}` (constaté sur tous les prompts FoodEatUp de
  // ce cours de test). On complète donc TOUJOURS avec une détection par
  // regex sur `contenu`, en fusionnant avec les entrées déclarées quand elles
  // existent, puis on résout la valeur par défaut de chaque variable connue
  // (ex: establishment_id -> "gosushi-demo") pour que l'étape 2 (Playwright)
  // puisse remplir les prompts sans deviner.
  const PLACEHOLDER_RE = /\{\{?\s*([a-zA-Z0-9_]+)\s*\}?\}/g;
  const enrichedPrompts = prompts.map((p) => {
    const declared = Array.isArray(p.variables) ? p.variables : [];
    const declaredByKey = Object.fromEntries(declared.map((v) => [v.key, v]));

    const foundKeys = new Set();
    for (const m of p.contenu.matchAll(PLACEHOLDER_RE)) foundKeys.add(m[1]);

    const variables = [...foundKeys].map((key) => ({
      key,
      label: declaredByKey[key]?.label ?? null,
      placeholder: declaredByKey[key]?.placeholder ?? null,
      default_value: defaultsByKey[key]?.valeur ?? null,
      source: declaredByKey[key] ? "declared+detected" : "detected_in_contenu",
    }));

    return {
      id: p.id,
      titre: p.titre,
      description: p.description,
      contenu: p.contenu,
      variables,
      mcp_cible: p.mcp_cible,
      niveau: p.niveau,
      executable: p.executable,
      resultat_attendu: p.resultat_attendu,
      tags: p.tags,
      ordre: p.ordre,
    };
  });

  const output = {
    course: {
      id: course.id,
      slug: course.slug,
      titre: course.titre,
      contenu_theorique: course.contenu_theorique,
      duree_min: course.duree_min,
      niveau: course.niveau,
      mcp_cible: course.mcp_cible,
      youtube_url: course.youtube_url,
    },
    prompts: enrichedPrompts,
  };

  await import("node:fs/promises").then((fs) =>
    fs.writeFile(outPath, JSON.stringify(output, null, 2), "utf8"),
  );
  console.error(`✓ Écrit dans ${outPath} (${enrichedPrompts.length} prompts)`);
}

main().catch((e) => {
  console.error("✗", e.message);
  process.exit(1);
});
