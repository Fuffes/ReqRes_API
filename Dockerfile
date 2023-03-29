FROM python:3.11-alpine as python

LABEL "creater" = "Fuffes"
LABEL "name" = "python:3.11-alpine"


WORKDIR /app

COPY . .

RUN apk update && apk upgrade && apk add bash

FROM python:3.9

WORKDIR /app

RUN apt-get update && apt-get upgrade -y

RUN pip3 install --disable-pip-version-check --no-cache-dir poetry==1.4.0


RUN poetry lock
RUN poetry install

CMD pytest -s-v

