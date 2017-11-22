FROM python:3.4
ENV PYTHONUNBUFFERED 1

RUN mkdir /code
WORKDIR /code

RUN mkdir /logs
RUN touch /logs/logs.log
RUN pip install Django==1.11
RUN pip install requests
RUN pip install psycopg2

RUN python -c 'import os; print(os.getcwd()); files = [f for f in os.listdir(".") if os.path.isfile(f)]; print(files)'

