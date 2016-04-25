# 北大医学部山岳部・フラテ山の会のウェブサイト

<http://frate-alpine.club>


## Feature

* 使うライブラリ
  * common
    * python 2.7.*
    * Django 1.7
    * SQLite
    * bower
  * production
    * nginx
    * Docker

* Django
  * 各appは`apps/`に隔離
  * settingsは開発で`core.settings.devel`、本番で`core.settings.prod`
  * ルーティング、wsgiプロセス、settingsは`core/`から
  * devel
    * `static/`を`STATICFILES_DIRS`、`dist/`を`STATIC_ROOT`にしている
  * prod
    * 静的ファイルの配信なし
    * uwsgiには`core.settings.prod`を渡している


* uwsgi
  * 本番環境ではDockerコンテナ内でsupervisorを使ってデーモン化
  * 手元で起動するときは
    ```
    uwsgi uwsgi.yml
    ```


* Nginx
  * 本番環境ではDockerコンテナ内でsupervisorを使ってデーモン化
  * 手元で起動するときは、予め
    ```
    ln -s nginx/frate.conf /etc/nginx/sites-availave
    ```
    しておいて、試す時だけ
    ```
    ln -s /etc/nginx/sites-availave/frate.conf /etc/nginx/sites-enabled/
    ```
    で有効化

## TODO
* Improve the way to detect and remove old container when hot reloading
