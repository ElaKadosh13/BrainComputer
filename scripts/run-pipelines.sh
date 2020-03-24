echo "running dockers"
docker network create bcnetwork1

docker run -d -p 5672:5672 --net bcnetwork1 --name rmqcontainer1 rabbitmq
#docker run -d -p 5432:5432 --net bcnetwork1 --name pgscontainer postgres
docker run -d -p 27017:27017 --net bcnetwork1 --name mdbcontainer mongo