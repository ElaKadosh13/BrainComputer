docker stop $(docker ps -a -q)
docker rm $(docker ps -a -q)
#ocker rmi -f $(docker images -a -q)
#ocker volume rm $(docker volume ls -qf dangling=true)
docker system prune