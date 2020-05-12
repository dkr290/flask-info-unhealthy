FROM python:3.8.2-buster

RUN apt-get update && apt-get -y upgrade && pip install Flask

COPY . /app

ENV FLASK_APP=/app/app.py

WORKDIR /app

ENTRYPOINT [ "python", "app.py" ]
