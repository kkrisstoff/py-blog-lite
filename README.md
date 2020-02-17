# py-blog-lite

## Blog Lite

### Run App
1. create venv
```shell script
$ python -m venv venv
```
2. activate venv
```shell script
$ source venv/bin/activate
```
3. install deps
```shell script
(venv) $ pip install -r requirements.txt
```
```shell script
export FLASK_APP=application.py
```
### translate
Add new language:
```shell script
(venv) $ flask translate init <language-code>
```

Update all languages after making changes to `_()` and `_l()` :
```shell script
(venv) $ flask translate update
```

Compile all languages after updating translation files:
```shell script
(venv) $ flask translate compile
```

### Search
```shell script
$ brew install elasticsearch
```
To have launched start elasticsearch:
```shell script
brew services start elasticsearch
```
If you don't want/need a background service you can just run:
```shell script
elasticsearch
```

ES URL: http://127.0.0.1:9200


## run via Docker

### Rebuild blog image
```shell script
$ docker build -t bloglite:latest .
```

### Run MySQL
```shell script
$ docker run --name mysql -d -e MYSQL_RANDOM_ROOT_PASSWORD=yes \
    -e MYSQL_DATABASE=bloglite -e MYSQL_USER=microblog \
    -e MYSQL_PASSWORD=bloglite \
    mysql/mysql-server:5.7
```
### Run Elasticsearch
```shell script
$ docker run --name elasticsearch -d -p 9200:9200 -p 9300:9300 --rm \
    -e "discovery.type=single-node" \
    docker.elastic.co/elasticsearch/elasticsearch-oss:6.1.1
```
### Run App
```shell script
$ docker run --name bloglite -d -p 8000:5000 --rm bloglite:latest
```

### Run App with MySQL and Elasticsearch
```shell script
$ docker run --name bloglite -d -p 8000:5000 --rm -e SECRET_KEY=my-secret-key \
    -e MAIL_SERVER=smtp.googlemail.com -e MAIL_PORT=587 -e MAIL_USE_TLS=true \
    -e MAIL_USERNAME=myuser@mail.com -e MAIL_PASSWORD=myGmailPassword \
    --link mysql:dbserver \
    -e DATABASE_URL=mysql+pymysql://bloglite:bloglite@dbserver/microblog \
    --link elasticsearch:elasticsearch \
    -e ELASTICSEARCH_URL=http://elasticsearch:9200 \
    bloglite:latest
```



