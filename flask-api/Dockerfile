FROM alpine
RUN apk add  bash python3 py3-pip
RUN pip3 install Flask
RUN python3 -m pip install mysql-connector-python
RUN apk add mariadb-connector-c mysql-client
ENV FLASK_APP=hello
COPY movie-guru /opt/
WORKDIR /opt/
EXPOSE 5000
ENTRYPOINT ["/usr/bin/flask","run","-h","0.0.0.0"]


