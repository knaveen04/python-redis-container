
Python-redis-container

A sample repo to create python webapp container with redis DB

pre requisites:  docker and docker-compose

Clone this git repo in local host / VM. Once cloned, run docker instances using
`docker-compose up`

To stop docker instances
`docker-compose stop`

or to stop and remove containers
`docker-compose down`

To view all docker containers
`docker ps -a`

To clean-up docker-machine containers
`docker-compose rm`

To delete the image
`docker rmi python_redis`

Data is stored in the docker volume which is persisted even if the containers are deleted

To view docker volumes
`docker volume ls`

Access the server at "http://ip/" (ip is host ip) 
