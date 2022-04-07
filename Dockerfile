FROM centos:7
RUN mkdir -p /usr/ticket-api
RUN mkdir -p ~/.ssh/
RUN yum update -y
RUN yum install python3 -y
RUN python3.6 -m pip install flask mysql-connector
ENV LC_ALL=en_US.UTF-8
WORKDIR /usr/ticket-api
RUN yum install git-core -y
ADD id_rsa.pub ~/.ssh/
RUN git clone https://github.com/eshikav/movie-guru-api.git
RUN mv movie-guru-api/* /usr/ticket-api/