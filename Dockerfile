# pull official base image
FROM python:3.8-alpine

# set work directory
WORKDIR /usr/src/app

ENV PYTHONUNBUFFERED 1
COPY ./requirements.txt /requirements.txt
RUN apk update && apk add postgresql-dev gcc python3-dev musl-dev
RUN pip install -r /requirements.txt


RUN mkdir /app
COPY ./ /usr/src/app/
