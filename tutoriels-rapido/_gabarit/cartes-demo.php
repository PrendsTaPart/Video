<?php
$u = App\Models\User::where('email', 'demo@rapido.test')->first();
$cid = $u->company_id;
$cs = app(App\Services\CarteDigitaleService::class);
if (! App\Models\CarteDigitale::where('company_id', $cid)->exists()) {
    $r = app(App\Services\BoucleMarketingService::class)->installer($u);
    $c = $r['carte'];
    $cs->mettreAJour($c, ['titre' => $c->titre, 'poste' => 'Fondatrice', 'telephone' => '06 12 34 56 78', 'whatsapp' => '+33612345678', 'email' => 'contact@atelier-horizon.test',
        'adresse' => '12 rue de la République, Lyon', 'bio' => 'Agence web à Lyon : sites, référencement et automatisation pour les indépendants.',
        'reseaux' => ['linkedin' => 'https://linkedin.com/company/exemple', 'instagram' => 'https://instagram.com/exemple'], 'echange_actif' => true, 'actif' => true]);
    $cs->creer($cid, $u->id, ['type' => 'liens', 'titre' => 'Atelier Horizon', 'bio' => 'Tous nos liens utiles', 'liens' => [['titre' => 'Prendre rendez-vous', 'url' => 'https://exemple.test/rdv'], ['titre' => 'Guide gratuit', 'url' => 'https://exemple.test/guide']]]);
    $req = Illuminate\Http\Request::create('/v/x', 'GET', ['src' => 'qr'], [], [], ['HTTP_USER_AGENT' => 'Mozilla/5.0 (iPhone) Mobile']);
    foreach (range(1, 23) as $i) { $cs->enregistrer($c, 'vue', $req); }
    foreach (range(1, 6) as $i) { $cs->enregistrer($c, 'clic', $req, 'Obtenir mon devis en ligne'); }
    $cs->enregistrer($c, 'vcard', $req);
    $cs->enregistrerPuce($cid, ['libelle' => 'Présentoir comptoir', 'cible_type' => 'digitale', 'cible_id' => $c->id]);
}
$f = app(App\Services\FideliteService::class);
$p = App\Models\ProgrammeFidelite::where('company_id', $cid)->whereNull('entreprise_id')->first()
    ?? $f->enregistrer($cid, ['nom' => 'Carte café', 'mode' => 'tampons', 'tampons_objectif' => 10, 'regles' => ['points_par_visite' => 1, 'bonus_bienvenue' => 1, 'bonus_parrain' => 2, 'bonus_filleul' => 1],
        'recompenses' => [['seuil' => 10, 'libelle' => 'Café offert']]]);
if (! App\Models\CarteFidelite::where('programme_fidelite_id', $p->id)->exists()) {
    foreach ([['Paul', 'Lafitte', 'paul.lafitte@exemple.test', 6], ['Léa', 'Martin', 'lea.martin@exemple.test', 9], ['Hugo', 'Bernard', 'hugo.bernard@exemple.test', 3]] as [$pr, $n, $e, $v]) {
        $carte = $f->inscrire($p, ['prenom' => $pr, 'nom' => $n, 'email' => $e], null, false);
        $f->crediter($carte, $v, 0, $u->id);
    }
}
echo 'ok '.App\Models\CarteDigitale::where('company_id', $cid)->count().' cartes';
