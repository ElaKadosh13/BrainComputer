echo "building braincomputer-base"
docker build -t braincomputer-base .
echo "building volume"
docker volume create --name bcvolume
echo "building server"
docker build -t braincomputer-server braincomputer/server
echo "building parsers"
docker build -t braincomputer-parsers braincomputer/parsers
echo "building saver"
docker build -t braincomputer-saver braincomputer/saver
echo "building gui"
docker build -t braincomputer-gui braincomputer/gui
echo "building api"
docker build -t braincomputer-api braincomputer/api

echo "running rabbitmq"
docker run -d -p 5672:5672 rabbitmq:3-management
echo "running mongodb"
docker run -d -p 27017:27017 mongo
echo "waiting for rabbit & mongo to set up (1 minute)"
sleep 1m
echo "running server"
docker run -d --network=host -v bcvolume:/braincomputer/gui/static braincomputer-server:latest
echo "running parsers"
docker run -d -e PARSER='pose' --network=host braincomputer-parsers:latest
docker run -d -e PARSER='feelings' --network=host braincomputer-parsers:latest
docker run -d -e PARSER='color_image' --network=host -v bcvolume:/braincomputer/gui/static braincomputer-parsers:latest
docker run -d -e PARSER='depth_image' --network=host -v bcvolume:/braincomputer/gui/static braincomputer-parsers:latest
echo "running saver"
docker run -d --network=host -v bcvolume:/braincomputer/gui/static braincomputer-saver:latest
echo "running gui"
docker run -d --network=host -v bcvolume:/braincomputer/gui/static braincomputer-gui:latest
echo "running api"
docker run -d --network=host -v bcvolume:/braincomputer/gui/static braincomputer-api:latest
echo "DONE"