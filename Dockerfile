FROM ubuntu:14.04
MAINTAINER David Liu "davidbliu@gmail.com"
# RUN export DEBIAN_FRONTEND=noninteractive


RUN apt-get -y update

#
# install python
#
RUN apt-get install -y python-dev python-setuptools supervisor git-core 
RUN easy_install pip

#
# not sure why do dis ish
#
RUN pip install virtualenv
RUN pip install uwsgi

#
# install django
#
RUN apt-get install -y python-pip
RUN apt-get install -y python-django
RUN pip install Django==1.7.1
#
# app-specific dependencies
#
RUN pip install oauthlib --upgrade
RUN pip install python-social-auth

#
# ad hoc shit
#
RUN apt-get -y build-dep python-psycopg2
RUN pip install psycopg2 

ADD . /portal
WORKDIR /portal


EXPOSE 8000

CMD python manage.py runserver