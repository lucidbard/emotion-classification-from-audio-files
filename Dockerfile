# syntax=docker/dockerfile:1
FROM python:3.8.10-slim-buster
WORKDIR /app
RUN python3 -m pip install --upgrade requests
COPY requirements.txt requirements.txt
RUN pip3 install -r requirements.txt
COPY . .
CMD [ "python3", "live_predictions.py"]