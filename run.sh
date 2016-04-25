#!/bin/bash

running_container_id=`echo $(docker ps -qa --no-trunc -f 'ancestor=frate' -f "status=running") | sed -e "s/[\r\n]\+/ /g"`

docker build -t frate .
docker run -d \
  -e VIRTUAL_HOST=frate-alpine.club,frate.endaaman.me,frate.local \
  -v $(pwd)/media:/var/www/frate/media \
  -v $(pwd)/db:/var/www/frate/db \
  frate

if [ -n "$running_container_id" ]; then
  echo 'killing old running container'
  docker kill -s QUIT $running_container_id
else
  echo 'There is no old container'
fi
