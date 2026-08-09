import React from 'react';
import { Composition } from 'remotion';
import { OutroEp01, Ep01Variables } from './OutroEp01';

// Valeurs par défaut alignées sur manifest.json (pipeline.ep-data.variables au 2026-08-09) :
// les 3 variables chiffrées sont __SUPPRIMER__, donc le bloc ChiffresBlock ne rend rien.
// logoUrl : URL publique du logo FoodEatUp (voir manifest.json.etape_0_marque) — à passer en
// override via --props lors du render (voir scripts/build_master.sh) plutôt que codée en dur ici,
// car l'URL S3 signée expire.
const defaultProps: { variables: Ep01Variables } = {
  variables: {
    CA_MOIS: '__SUPPRIMER__',
    COUVERTS: '__SUPPRIMER__',
    RUPTURES_EVITEES: '__SUPPRIMER__',
    logoUrl: '',
  },
};

export const RemotionRoot: React.FC = () => {
  return (
    <Composition
      id="OutroEp01"
      component={OutroEp01}
      durationInFrames={450}
      fps={30}
      width={1080}
      height={1920}
      defaultProps={defaultProps}
    />
  );
};
