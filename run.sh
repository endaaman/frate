docker build -t endaaman/frate .

# docker run -d -e VIRTUAL_HOST=frate-alpine.club \
#   -v $(pwd)/media:/var/www/frate/media \
#   -v $(pwd)/db:/var/www/frate/db \
#    endaaman/frate

running_container_id=$(docker ps -lq --no-trunc --filter='ancestor=endaaman/frate')

echo $running_container_id

container_id=$( \
  docker run -d \
    -e VIRTUAL_HOST=frate-alpine.club,frate.local \
    -v $(pwd)/media:/var/www/frate/media \
    -v $(pwd)/db:/var/www/frate/db \
    endaaman/frate \
)

if ! [ -n "$running_container_id" ]; then
  echo 'killing old container'
  docker kill -s QUIT $running_container_id
fi
