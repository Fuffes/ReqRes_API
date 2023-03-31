FROM python:3.11-alpine as python

LABEL "creater" = "Fuffes"
LABEL "name" = "python:3.11-alpine"

ENV PYTHONUNBUFFERED=1 \
    PYTHONDONTWITEBYTECODE=1

COPY . /app
WORKDIR /app

RUN pip3 install poetry
RUN poetry config virtualenvs.create false
RUN poetry install
RUN chmod +x ./entrypoint.sh

CMD ["/bin/sh", "-c", "./entrypoint.sh"]


