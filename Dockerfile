# syntax=docker/dockerfile:1
FROM python:3.8.10-slim-buster
RUN apt-get update \
  && apt-get -y install libpq-dev gcc \
  && pip install psycopg2
WORKDIR /app
RUN python3 -m pip install --upgrade requests
RUN /usr/local/bin/python -m pip install --upgrade pip
COPY requirements.txt requirements.txt
RUN pip3 install -r requirements.txt
COPY . .
CMD [ "python3", "server.py"]
EXPOSE 8111