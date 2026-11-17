<?php
// Données fictives pour CRM84 (suivi des envois et désinscriptions). Copie de tournage uniquement : une campagne e-mail, une newsletter,
// une campagne SMS avec liens courts, et quelques désinscriptions. Rejouable.
use App\Models\CampagneEmail;
use App\Models\CampagneNewsletter;
use App\Models\CampagneSms;
use App\Models\User;
use Illuminate\Support\Facades\DB;
use Illuminate\Support\Str;

$u = User::where('email', 'demo@rapido.test')->firstOrFail();
$cid = $u->company_id;
$ids = DB::table('email_envois')->where('company_id', $cid)->pluck('id');
DB::table('email_clics')->whereIn('email_envoi_id', $ids)->delete();
DB::table('email_envois')->where('company_id', $cid)->delete();
$sms = CampagneSms::where('company_id', $cid)->pluck('id');
DB::table('sms')->whereIn('campagne_sms_id', $sms)->delete();
DB::table('sms_liens')->where('company_id', $cid)->delete();
CampagneSms::where('company_id', $cid)->delete();
CampagneEmail::where('company_id', $cid)->where('objet', 'like', '%[démo]%')->delete();
CampagneNewsletter::where('company_id', $cid)->where('contenu', 'like', '%[démo]%')->delete();
DB::table('desinscriptions')->where('company_id', $cid)->delete();

$prenoms = ['camille', 'hugo', 'ines', 'lucas', 'emma', 'nathan', 'chloe', 'louis', 'manon', 'jules', 'sarah', 'adam', 'lea', 'tom', 'zoe'];
$envoyer = function (string $type, int $source, int $n, int $ouverts, int $cliques, string $url, int $jours) use ($cid, $prenoms) {
    for ($i = 0; $i < $n; $i++) {
        $envoi = now()->subDays($jours)->addMinutes($i);
        $id = DB::table('email_envois')->insertGetId(['company_id' => $cid, 'type' => $type, 'source_id' => $source,
            'destinataire' => $prenoms[$i % 15].'.'.($i + 1).'@exemple.test', 'jeton' => Str::random(40),
            'ouvert_le' => $i < $ouverts ? $envoi->copy()->addHours(2 + $i % 20) : null, 'nb_ouvertures' => $i < $ouverts ? 1 + $i % 3 : 0,
            'clique_le' => $i < $cliques ? $envoi->copy()->addHours(3 + $i % 20) : null, 'nb_clics' => $i < $cliques ? 1 + $i % 2 : 0,
            'created_at' => $envoi, 'updated_at' => $envoi]);
        if ($i < $cliques) {
            DB::table('email_clics')->insert(['email_envoi_id' => $id, 'url' => $url, 'created_at' => $envoi->copy()->addHours(3)]);
        }
    }
};
$c = CampagneEmail::create(['company_id' => $cid, 'cible' => 'audience', 'objet' => 'Offre de printemps : -20 % sur les ateliers [démo]', 'contenu' => '<p>Offre</p>', 'date_envoi' => now()->subDays(9)]);
$c->forceFill(['objet' => 'Offre de printemps : -20 % sur les ateliers', 'created_at' => now()->subDays(9)])->save();
$envoyer('campagne', $c->id, 120, 58, 17, 'https://exemple.test/ateliers', 9);
$nl = CampagneNewsletter::create(['company_id' => $cid, 'cible' => 'audience', 'contenu' => '<p>Les nouveautés de novembre [démo]</p>', 'date_envoi' => now()->subDays(3)]);
$nl->forceFill(['created_at' => now()->subDays(3)])->save();
$envoyer('newsletter', $nl->id, 85, 47, 9, 'https://exemple.test/blog/nouveautes', 3);

$s = CampagneSms::create(['company_id' => $cid, 'cible' => 'audience', 'contenu' => 'Rapido Studio : vos ateliers de printemps à -20 % jusqu’à dimanche ! Réservez : rpd.li/a1 STOP au 36173', 'date_envoi' => now()->subDays(5)]);
for ($i = 0; $i < 60; $i++) {
    $tel = '+3361234'.str_pad((string) $i, 4, '0', STR_PAD_LEFT);
    DB::table('sms')->insert(['user_id' => $u->id, 'numero' => $tel, 'message' => $s->contenu, 'campagne_sms_id' => $s->id, 'segments' => 1, 'statut' => 'envoye', 'created_at' => now()->subDays(5), 'updated_at' => now()->subDays(5)]);
    DB::table('sms_liens')->insert(['company_id' => $cid, 'campagne_sms_id' => $s->id, 'code' => 'a'.$i.Str::random(4), 'url' => 'https://exemple.test/ateliers',
        'telephone' => $tel, 'clics' => $i < 14 ? 1 + $i % 2 : 0, 'premier_clic_le' => $i < 14 ? now()->subDays(5)->addHours(1) : null, 'created_at' => now()->subDays(5), 'updated_at' => now()->subDays(5)]);
}
foreach ([['jules.10@exemple.test', 'lien', 7], ['manon.9@exemple.test', 'un clic (messagerie)', 6], ['tom.14@exemple.test', 'lien', 2]] as [$email, $src, $j]) {
    DB::table('desinscriptions')->insert(['company_id' => $cid, 'email' => $email, 'canal' => 'email', 'source' => $src, 'created_at' => now()->subDays($j), 'updated_at' => now()->subDays($j)]);
}
echo "CRM84 prêt\n";
