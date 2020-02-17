FROM python:3.7-alpine

RUN adduser -D bloglite

WORKDIR /home/bloglite

COPY requirements.txt requirements.txt

RUN python -m venv venv

# FIX: unable to execute 'gcc': No such file or directory   libffi-dev, openssl-dev and python3-dev
RUN apk add --no-cache --virtual .build-deps gcc musl-dev libffi-dev openssl-dev \
    && venv/bin/pip install --upgrade pip \
    && venv/bin/pip install -r requirements.txt \
    && venv/bin/pip install gunicorn pymysql \
    && apk del .build-deps gcc musl-dev libffi-dev openssl-dev

COPY app app
COPY migrations migrations
COPY application.py config.py boot.sh ./
RUN chmod a+x boot.sh

ENV FLASK_APP application.py

RUN chown -R bloglite:bloglite ./
USER bloglite

EXPOSE 5000
ENTRYPOINT ["./boot.sh"]