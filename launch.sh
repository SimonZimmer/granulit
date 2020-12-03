echo killing old docker processes
docker-compose rm -fs

./init-letsencrypt.sh

echo building docker containers
docker-compose up --build -d


