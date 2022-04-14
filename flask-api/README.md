# Flask Api

# It runs the Flask application that is containerised in any of the container runtime environment.

## Prerequisites

1. Running this application requires any of the Container Runtime environment to be installed.(Refer to https://docs.docker.com/engine/install/)


##Customising the application

| Variable      | Default | Description |
| ----------- | ----------- | ----------- |
| DB_USER      | None       | The username that is used to connect to the database |
| DB_PASSWORD   | None        | Password of the database user |
| DB_HOST   | None | Database host to connect |
| DB_AUTOCOMMIT | False | Autocommit for the database |
| DB_DATABASE | None | Database to select |
| DB_TS_ISOLATION_LEVEL | None | Isolation level for the transactions |

## Building the application:

The repo has a Dockerfile, to build the container image run as below

``bash
export APP_IMAGE="flask-api:01"
docker build --no-cache -t $APP_IMAGE .
[+] Building 8.2s (6/10)
 => [internal] load build definition from Dockerfile                                                                                      0.0s
 => => transferring dockerfile: 32B                                                                                                       0.0s
 => [internal] load .dockerignore                                                                                                         0.0s
 => => transferring context: 2B                                                                                                           0.0s
 => [internal] load metadata for docker.io/library/alpine:latest                                                                          5.0s
 => CACHED [1/6] FROM docker.io/library/alpine@sha256:4edbd2beb5f78b1014028f4fbb99f3237d9561100b6881aabbf5acce2c4f9454                    0.0s
 => [internal] load build context                                                                                                         0.0s
 => => transferring context: 124B                                                                                                         0.0s
 => [2/6] RUN apk add  bash python3 py3-pip              
 ....

docker images
docker images
REPOSITORY   TAG       IMAGE ID       CREATED          SIZE
flask-api    01        99994986953c   24 seconds ago   79.7MB
``

## Run on Docker:

``bash
export APP=flask
docker run -p 127.0.0.1:5000:5000/tcp --name $APP -d  $APP_IMAGE
34991e77141d6c6b1ff237be793af149da2848ca89eae3e5ee27a6066c4f51d9

docker ps
CONTAINER ID   IMAGE          COMMAND                  CREATED         STATUS         PORTS                      NAMES
34991e77141d   flask-api:01   "/usr/bin/flask run …"   4 seconds ago   Up 3 seconds   127.0.0.1:5000->5000/tcp   flask
``

## Accessing the application:

Open and a browser and navigate to 127.0.0.1:5000/

## Running on Kubernetes:


References:

| Link    | Description |
| ----------- | ----------- |
| https://docs.docker.com/ | Docker Documentation |
| https://docs.docker.com/cloud/aci-container-features/ | Docker run flags |
|| Kubernetes Documentation |