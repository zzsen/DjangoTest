FROM python:3.8-alpine

ENV PYTHONUNBUFFERED 1
RUN mkdir /code
RUN mkdir /code/db
WORKDIR /code
ADD ./mysite/requirements.txt /code/
RUN pip install -r requirements.txt
ADD . /code/