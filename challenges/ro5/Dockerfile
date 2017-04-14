FROM ubuntu:16.04
MAINTAINER Pwnpectf sapgan "admin@insignectf.in"
LABEL Description="Insigne CTF 2017 Web1" VERSION=1.0

RUN apt-get update && apt-get upgrade -y
RUN apt-get install -y apache2 php libapache2-mod-php php-sqlite3 python

COPY users.db /var/www
WORKDIR /var/www
COPY ./src /var/www/html

WORKDIR /var/www/html
RUN rm index.html
EXPOSE 80
CMD /usr/sbin/apache2ctl -D FOREGROUND
