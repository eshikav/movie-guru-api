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

```bash
export APP_IMAGE="flask-api:01"
docker build --no-cache -t $APP_IMAGE .
docker images

```

## Run on Docker:

```bash
export APP=flask
docker run -p 127.0.0.1:5000:5000/tcp --name $APP -d  $APP_IMAGE
docker ps
```

## Accessing the application:

Open and a browser and navigate to 127.0.0.1:5000/

## Running on Kubernetes:


References:

| Link    | Description |
| ----------- | ----------- |
| https://docs.docker.com/ | Docker Documentation |
| https://docs.docker.com/cloud/aci-container-features/ | Docker run flags |
| Docker installation | https://docs.docker.com/engine/install/ | 
|| Kubernetes Documentation |