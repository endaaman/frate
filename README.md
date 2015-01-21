# 北海道大学医学部山岳部フラテ山の会のウェブサイト

Visit <http://frate-alpine.club>

## Feature

* 基本
  * /var/www/frate に直接展開 or SymLinkを張る
  * ルーティング、wsgiプロセス、settingsは`core/`から
  * settingsは開発で`core.settings.devel`、本番で`core.settings.prod`
  * 各appは`apps/`に隔離
  * `static/`は`STATICFILES_DIRS`にして、`STATIC_ROOT`は`dist/`にする

* uwsgi
  * デーモン化
  * NginxとはUNIXドメインソケットで

* fabric
  * デプロイ（半手動）
  * uwsgiのプロセス管理
    * `fab uwsgi`ですでに起動していなければスタート、起動してればリロード
    * `fab uwsgi:stop`でストップ
    * `fab uwsgi.lookup`で起動しているのuwsgiを探索
      * プロセスがゾンビ化したときにすぐ捕まえられる
  * sshはfabfile/local.pyを作成して（git管理外）
    ```
    from fabric.api import env

    env.hosts = '123.456.123.456'
    env.port = 22
    env.user = 'user'
    env.key_filename = '/path/to/ssh/key'
    ```
    こんな感じで

* Nginx
  * `/etc/nginx/conf.d/`に`nginx/frate.conf`のSymLinkを張る

