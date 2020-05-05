FROM ubuntu:18.04 AS BUILD

ARG ENV_FILE
ENV ENV_FILE ${ENV_FILE}

RUN apt-get update && apt-get install make
RUN apt-get install -y python3.7 python3-pip
RUN python3.7 -m pip install --upgrade pip
RUN apt-get -y install build-essential python3.7-dev
RUN apt-get -y install python3-uvloop
RUN apt-get install -y git

COPY . /app
WORKDIR /app

ENV PIP_CONFIG_FILE .deploy/.secrets/pip.conf

RUN PIP=pip PYTHON=python3.7 make deps
CMD PIP=pip PYTHON=python3.7 ENV_FILE=$ENV_FILE make run
