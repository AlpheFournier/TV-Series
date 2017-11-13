FROM python:2.7
ENV PYTHONUNBUFFERED 1

RUN mkdir /code
WORKDIR /code

RUN mkdir /logs
RUN touch /logs/logs.log
RUN pip install Django==1.11
RUN pip install requests

