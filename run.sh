docker build -t frate .

# docker run -d -e VIRTUAL_HOST=frate-alpine.club \
#   -v $(pwd)/media:/var/www/frate/media \
#   -v $(pwd)/db:/var/www/frate/db \
#    endaaman/frate

running_container_id_raw=$(docker ps -aq --no-trunc --filter='ID=frate')
running_container_id=`echo $running_container_id_raw | sed -e "s/[\r\n]\+//g"`
#
# echo $running_container_id

container_id=$( \
  docker run -d \
    --label ID="frate" \
    -e VIRTUAL_HOST=frate-alpine.club,frate.endaaman.me,frate.local \
    -v $(pwd)/media:/var/www/frate/media \
    -v $(pwd)/db:/var/www/frate/db \
    frate \
)

if ! [ -n "$running_container_id" ]; then
  echo 'killing old container'
  docker kill -s QUIT $running_container_id
fi
