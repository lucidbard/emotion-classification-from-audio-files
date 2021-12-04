# syntax=docker/dockerfile:1
FROM python:3.8.10-slim-buster
WORKDIR /app
RUN python3 -m pip install --upgrade requests
RUN /usr/local/bin/python -m pip install --upgrade pip
RUN pip3 install psycopg2==2.7.5
COPY requirements.txt requirements.txt
RUN pip3 install -r requirements.txt
COPY . .
CMD [ "python3", "live_predictions.py"]