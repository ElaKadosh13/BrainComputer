#echo "running dockers"
#docker network create bcnetwork1
#
#docker run -d -p 5672:5672 --net bcnetwork1 --name rmqcontainer1 rabbitmq
#docker run -d -p 27017:27017 --net bcnetwork1 --name mdbcontainer mongo


################################################################################################################################################################
echo "building braincomputer-base"
docker build -t braincomputer-base .

echo "building server"
docker build -t braincomputer-server braincomputer/server
echo "building parsers"
docker build -t braincomputer-parsers braincomputer/parsers
echo "building saver"
#docker build -t braincomputer-saver braincomputer/saver
echo "building gui"
#docker build -t braincomputer-gui braincomputer/gui
echo "building api"
#docker build -t braincomputer-api braincomputer/api

echo "!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!"
echo "running rabbitmq"
docker run -d -p 5672:5672 rabbitmq:3-management
sleep 1m

echo "running-parsers"
docker run -d --network=host braincomputer-parsers:latest
#docker run -d -e PARSER='pose' --network=host braincomputer-parsers:latest
echo "running server"
docker run -d --network=host braincomputer-server:latest

echo "DONE"