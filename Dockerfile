FROM ubuntu:16.04

RUN apt-get update
RUN apt-get install -y \
  python python-dev python-pip \
  nginx \
  curl git \
  supervisor

RUN curl -kL git.io/nodebrew | perl - setup
ENV PATH /root/.nodebrew/current/bin:$PATH
RUN nodebrew install-binary v4.4.3
RUN nodebrew use v4.4.3


RUN \
  chown -R www-data:www-data /var/lib/nginx && \
  echo "\ndaemon off;" >> /etc/nginx/nginx.conf && \
  rm /etc/nginx/sites-enabled/default

RUN npm i -g bower

ADD nginx/frate.conf /etc/nginx/sites-enabled
ADD supervisor.conf /etc/supervisor/conf.d/


RUN mkdir -p /var/www/frate
WORKDIR /var/www/frate

ADD requirements.txt ./
RUN pip install -r requirements.txt
ADD bower.json ./
RUN bower install --allow-root

ADD . /var/www/frate

RUN python manage.py migrate --settings=core.settings.prod
RUN python manage.py collectstatic --settings=core.settings.prod --noinput

CMD ["/usr/bin/supervisord"]

EXPOSE 80
