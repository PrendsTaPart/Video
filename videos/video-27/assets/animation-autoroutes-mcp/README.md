# Animation réutilisable : routes n8n → autoroutes MCP

Composition HTML 1080 × 1920, rendue image par image avec Playwright (`render(t)`, comme dans les autres épisodes).

Les éléments réutilisables sont dans `script.js` :

- **`BD`** : bâtiments. Chaque entrée donne un logo officiel ou un nom, avec sa position. RapidoATS et StartupForge n'ont pas de logo officiel ici : leur nom est écrit en typographie neutre.
- **`roads(t, t0, t1, n0, n1, opacité)`** : trace progressivement les routes départementales (courbes roses entre chaque paire de bâtiments, trois passes pour densifier).
- **`hw(t, t0, on)`** : fait apparaître l'autoroute centrale, ses bretelles « entrée MCP » vers chaque bâtiment et le marquage qui défile.

Pour un autre épisode : copier `index.html`, `script.js`, `base.css` et le dossier `a/` (polices, poses, logos), changer `BD`, puis les temps dans `render()`.
