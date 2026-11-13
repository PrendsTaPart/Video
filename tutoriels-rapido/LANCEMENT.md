# Lancer chaque Rapido en local pour filmer (données fictives)

Règle : les dépôts applicatifs sont en **lecture seule**. Tout ce qui est créé ici est ignoré par git
(`.env`, `database/database.sqlite`, `vendor/`, `node_modules/`). Ne jamais lancer `npm run build`
(le dossier `public/build` est versionné : on utilise le build déjà commité).

## RapidoCRM
```bash
composer clear-cache                       # libère ~8 Go si besoin
cd rapido-crm
COMPOSER_NO_INTERACTION=1 composer install --no-scripts --no-cache --no-dev
cp .env.example .env && sed -i 's/^MAIL_MAILER=.*/MAIL_MAILER=log/' .env   # aucun e-mail réel
touch database/database.sqlite && php artisan key:generate
php artisan migrate:fresh --seed --force
php ../video/tutoriels-rapido/_gabarit/demo-crm.php database/database.sqlite
php artisan tinker --execute='$c=App\Models\Company::find(1); foreach(["password"=>"demo-imap","stripe_secret"=>"sk_test_demo","sms_id"=>"demo-sms"] as $k=>$v){$c->$k=Illuminate\Support\Facades\Crypt::encryptString($v);} $c->saveQuietly();'
php artisan serve --port=8124
```
Compte de démonstration : `demo@rapido.test` / `Demo-Rapido-2026` (entreprise fictive « Studio Lumière »).
Notes : GitHub refuse les zips anonymes de Composer → installation depuis les sources (lente) ; les adresses
d'inscription doivent avoir un domaine réel (validation DNS) mais aucun e-mail ne part (`MAIL_MAILER=log`).

## RapidoCMS / RapidoRH
Même principe (Laravel 11 + Vue). Recette détaillée ajoutée lors du premier tutoriel de chaque application.


## RapidoCRM — copie de tournage recompilée (depuis le 13/11/2026)

Le dépôt contient des marqueurs de conflit (build et 3 sources) : on filme une **copie hors dépôt**.

```bash
mkdir -p /home/user/rapido-crm-film
tar -C /home/user/rapido-crm --exclude=./.git -cf - . | tar -C /home/user/rapido-crm-film -xf -
cd /home/user/rapido-crm-film
# résoudre les marqueurs (garder la 2e version) dans :
#   resources/views/admin/layouts/admin.blade.php, resources/views/admin/tutoriels/templates/editeur_pdf.blade.php,
#   resources/js/components/CalendarComponent.vue
# refermer les balises de EntrepriseProfil.vue après la ligne 138 (section tronquée), puis :
npm run build
php artisan serve --port=8124
node /home/user/video/tutoriels-rapido/_gabarit/mock-n8n.cjs   # prospection Maps simulée (port 8199)
```

## RapidoCMS (port 8125)

`.env` local : `SESSION_DRIVER=file`, `CACHE_STORE=file`, `QUEUE_CONNECTION=sync`, `MAIL_MAILER=log`,
`MAIL_FROM_ADDRESS="no-reply@rapido.test"`. Données : `php _gabarit/demo-cms.php database/database.sqlite`.
Les fonctions IA (OpenAI) sont simulées dans le navigateur par `record.cjs` (`mocks` dans tuto.json).
