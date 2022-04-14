# MySQL Database

# It runs the mysql database containerized in any of  the container runtime environment.

## Prerequisites

1. Running this application requires any of the Container Runtime environment to be installed.(Refer to https://docs.docker.com/engine/install/)


## Customising the application

| Variable      | Default | Description |
| ----------- | ----------- | ----------- |
| MYSQL_ROOT_PASSWORD  | None       | Root password for the database |

## Building the application:

The repo has a Dockerfile, to build the container image run as below

```bash
export APP_IMAGE="mysql:01"
docker build --no-cache -t $APP_IMAGE .
docker images
```

## Run on Docker:

```bash
export APP=mysql
mkdir $PWD 
docker run -v "$PWD/data":/var/lib/mysql -p 127.0.0.1:3007:3006/tcp  -e MYSQL_ROOT_PASSWORD="Test123@" --name $APP -d  $APP_IMAGE
docker ps
```

## Accessing the application:

Try connecting to the database at 127.0.0.1:3007

## Running on Kubernetes:


References:

| Link    | Description |
| ----------- | ----------- |
| https://docs.docker.com/ | Docker Documentation |
| https://docs.docker.com/cloud/aci-container-features/ | Docker run flags |
| https://docs.docker.com/engine/install/  |  Docker installation| 
|| Kubernetes Documentation |