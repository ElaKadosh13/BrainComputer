echo "running dockers"
docker network create bcnetwork1

docker run -d -p 5672:5672 --net bcnetwork1 --name rmqcontainer1 rabbitmq