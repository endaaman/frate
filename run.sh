# docker build -t endaaman/frate .

# docker run -d -e VIRTUAL_HOST=frate-alpine.club \
#   -v $(pwd)/media:/var/www/frate/media \
#   -v $(pwd)/db:/var/www/frate/db \
#    endaaman/frate

running_container_id=$(docker ps -ql --no-trunc --filter='ancestor=endaaman/frate')

echo $running_container_id

container_id=$( \
  docker run -d \
    -e VIRTUAL_HOST=frate-alpine.club,frate.local \
    -v $(pwd)/media:/var/www/frate/media \
    -v $(pwd)/db:/var/www/frate/db \
    endaaman/frate \
)

echo $container_id

docker exec $container_id bash -c 'while [ -z "$(cat /var/run/supervisord.pid 2>/dev/null)" ]; do sleep 1; done'
if $running_container_id; then
  docker kill -s QUIT $running_container_id
fi
