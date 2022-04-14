# Ticketing Application

## It runs the movie ticketing application with the below architecture
1. Frontend server (Flask)
2. Backend service (mysql-server)

## Prerequisites

1. Running this application requires any of the Container Runtime environment to be installed.(Refer to https://docs.docker.com/engine/install/)
2. The application requires the below  images.
  
| Variable      |  Application |
| ----------- |  ----------- |
| flask-api:01   | Backend |
| mysqlserver:01  | Frontend |

** NOTE: If there is no Container runtime Environment refer https://docs.docker.com/desktop/windows/install/ to get one quickly installed **

## Customising the Application

| Variable      | Default | Description |
| ----------- | ----------- | ----------- |
| DB_USER      | "root"       | The username that is used to connect to the database |
| DB_PASSWORD   | "Test123"        | Password of the database user |
| DB_HOST   | "database" | Database host to connect |
| DB_AUTOCOMMIT | "False" | Autocommit for the database |
| DB_DATABASE | "MovieGuru" | Database to select |
| DB_TS_ISOLATION_LEVEL | "SERIALIZABLE" | Isolation level for the transactions |
| MYSQL_ROOT_PASSWORD | "Test123" | The password for the mysql server |

Running the application:
```bash
docker compose build
docker compose up
docker compose down
```

## Accessing the Application:

Open and a browser and navigate to 127.0.0.1:5000/

## Running on Kubernetes:


References:

| Link    | Description |
| ----------- | ----------- |
| https://docs.docker.com/ | Docker Documentation |
| https://docs.docker.com/cloud/aci-container-features/ | Docker run flags |
| https://docs.docker.com/engine/install/  |  Docker installation| 
| https://docs.docker.com/compose/compose-file/ | Docker compose |
| https://dev.mysql.com/doc/refman/8.0/en/ | Mysql Server |
|https://flask.palletsprojects.com/en/2.1.x/# | Flask |
|| Kubernetes Documentation |