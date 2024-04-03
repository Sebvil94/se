FROM python:3.10-slim

WORKDIR /home/app

COPY . .

RUN apt-get update && apt-get install -y \
    gcc \
    default-libmysqlclient-dev \
    pkg-config

RUN pip install watchdog[watchmedo]

RUN pip install mysql

RUN pip install mysql-connector-python

CMD [ "python3", "socket-server.py" ]
