FROM python:3.9.6-slim-buster

ENV PYTHONBUFFERED 1
ENV PYTHONPATH /app/src
ENV SBF_ENVIRONMENT production

RUN mkdir /app

ADD pyproject.toml poetry.lock /app/

WORKDIR /app

RUN pip install --upgrade pip
RUN pip install poetry
RUN poetry config virtualenvs.create false
RUN poetry install --no-interaction --no-ansi

ADD . /app
EXPOSE 8080

CMD gunicorn --bind :8080 --workers 4 --threads 8 --timeout 0 -k uvicorn.workers.UvicornH11Worker main:get_app
