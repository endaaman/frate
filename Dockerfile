FROM ubuntu:14.04

RUN \
  apt-get update && \
  apt-get install -y python python-dev python-pip nginx nodejs-legacy npm supervisor

RUN \
  chown -R www-data:www-data /var/lib/nginx && \
  echo "\ndaemon off;" >> /etc/nginx/nginx.conf && \
  rm /etc/nginx/sites-enabled/default

ADD nginx/frate.conf /etc/nginx/sites-enabled

ADD supervisor.conf /etc/supervisor/conf.d/



RUN npm i -g bower

RUN mkdir -p /var/www/frate
ADD . /var/www/frate
WORKDIR /var/www/frate


RUN pip install -r requirements.txt
RUN bower install --allow-root

RUN python manage.py migrate --settings=core.settings.prod
RUN python manage.py collectstatic --settings=core.settings.prod --noinput

VOLUME ["media", "db"]
CMD ["/usr/bin/supervisord"]

EXPOSE 80
