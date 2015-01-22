# 北大医学部山岳部・フラテ山の会のウェブサイト

<http://frate-alpine.club>
主に写真のホスティング


## Feature

* 基本
  * `/var/www/frate`に直接展開 or SymLinkを張る
  * `virtualenvwrapper`のWORKON_HOMEが`/var/www/venv`である or SymLinkを張ってある
  * ルーティング、wsgiプロセス、settingsは`core/`から
  * settingsは開発で`core.settings.devel`、本番で`core.settings.prod`
  * 各appは`apps/`に隔離
  * `static/`を`STATICFILES_DIRS`、`dist/`を`STATIC_ROOT`にしている

* uwsgi
  * デーモン化
  * NginxとはUNIXドメインソケットで通信

* fabric
  * sshはfabfile/local.pyを作成しておく（git管理外）
      ```python
      # fabfile/local.py
      from fabric.api import env

      env.hosts = '123.456.123.456'
      env.port = 22
      env.user = 'user'
      env.key_filename = '/path/to/ssh/key'
      ```
  * uwsgiのプロセス管理
    * `fab uwsgi.start`で起動
    * `fab uwsgi.reload`でGraceful Reload
    * `fab uwsgi.stop`でストップ
    * `fab uwsgi`ですでに起動していなければスタート、起動してればリロード
    * `fab uwsgi.lookup`で起動しているのuwsgiを探索
      プロセスがゾンビ化したときにすぐ捕まえられる
  
  * `fab deploy`
    1. `workon frate`
      事前に`mkvirtualenv frate`しておく
    * `git pull origin master`
    * `pip install -r freeze.txt`
    * `python manage.py makemigrations`
    * `python manage.py migrate`
    * `python manage.py collectstatic`
    * `fab uwsgi`


* Nginx
  * `/etc/nginx/conf.d/`に`nginx/frate.conf`のSymLinkを張る
  * `/etc/nginx/nginx.conf`はマシンスペックに応じて適当に。ただ必ずhttpディレクティブからincludeする。
    ``` 
    http {
      include mime.types;
      include conf.d/*.conf;
    }
    ```


