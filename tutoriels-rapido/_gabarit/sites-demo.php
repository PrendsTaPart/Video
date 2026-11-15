<?php
// Site FICTIF « Studio Lumière » pour filmer CRM50–CRM53 (sites, domaine, éditeur) : deux pages tirées de la
// bibliothèque de modèles gratuits, l'accueil publié, quelques visites simulées. Copie de tournage uniquement.
// Usage : php artisan tinker puis require '/home/user/video/tutoriels-rapido/_gabarit/sites-demo.php';
$u = App\Models\User::where('email', 'demo@rapido.test')->first();
$s = app(App\Services\SiteService::class);
$site = App\Models\Site::where('company_id', $u->company_id)->first();
if (! $site) {
    $site = $s->creerSite($u->company_id, 'Studio Lumière');
    $s->enregistrerReglages($site, ['description' => 'Agence web fictive à Lyon : sites, référencement et automatisation pour les indépendants.', 'couleur' => '#4caf50']);
    $m = fn ($id) => DB::table('editor_templates')->find($id);
    $dec = fn ($v) => is_string($v) && ($d = json_decode($v)) !== null && is_string($d) ? $d : $v;
    $accueil = $s->creerPage($site, ['titre' => 'Accueil', 'html' => $dec($m(8)->html), 'css' => $dec($m(8)->css)], $u->id);
    $s->enregistrerSeo($accueil, ['seo_titre' => 'Studio Lumière — agence web à Lyon', 'seo_description' => 'Sites, référencement et automatisation pour les indépendants et les TPE de la région lyonnaise.']);
    $s->publier($accueil);
    $guide = $s->creerPage($site, ['titre' => 'Guide gratuit', 'html' => $dec($m(11)->html), 'css' => $dec($m(11)->css)], $u->id);
    $req = Illuminate\Http\Request::create('/site/x', 'GET', [], [], [], ['HTTP_USER_AGENT' => 'Mozilla/5.0 (iPhone) Mobile', 'HTTP_REFERER' => 'https://www.google.com/']);
    foreach (range(1, 37) as $i) { $s->enregistrerVue($accueil->fresh(), $req); }
}
echo 'ok site '.$site->slug.' ('.$site->pages()->count()." pages)\n";
