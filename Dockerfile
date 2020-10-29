FROM python:3.6
RUN mkdir /webapps
WORKDIR /webapps
RUN apt-get update && apt-get upgrade -y && apt-get install -y \
libsqlite3-dev
RUN pip install -U pip setuptools
COPY requirements.txt /webapps/
RUN pip install -r /webapps/requirements.txt
ADD . /webapps/
# Django service
EXPOSE 8000