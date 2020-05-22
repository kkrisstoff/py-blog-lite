# py-blog-lite

## Blog Lite

### Run App localhost and venv Mode

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

4. Add env
```shell script
(venv) $ export FLASK_APP=application.py
```

5. Upgrade DB
```shell script
(venv) $ flask db upgrade
```

5. Run Server (Name/name12)
```shell script
(venv) $ flask run
```

______________________________________________________

### db migrate
```shell script
(venv) $ flask db migrate -m "<migration messages>"
(venv) $ flask db upgrade
```

### translate
Update all languages after making changes to `_()` and `_l()`:
```shell script
(venv) $ fflask translate update
```

Add new language:
```shell script
(venv) $ flask translate init <language-code>
```

Compile all languages after updating translation files:
```shell script
(venv) $ flask translate compile
```

________________________________________________________

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

### Run Redis
```shell script
$ docker run --name redis -d -p 6379:6379 redis:3-alpine
````
### Run MySQL
```shell script
$ docker run --name mysql -d -e MYSQL_RANDOM_ROOT_PASSWORD=yes \
    -e MYSQL_DATABASE=bloglite -e MYSQL_USER=bloglite \
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
    -e DATABASE_URL=mysql+pymysql://bloglite:bloglite@dbserver/bloglite \
    --link elasticsearch:elasticsearch \
    -e ELASTICSEARCH_URL=http://elasticsearch:9200 \
    -e REDIS_URL=redis://redis-server:6379/0 \
    bloglite:latest
```
### Run App with MySQL and Elasticsearch and Worker
```shell script
$ docker run --name rq-worker -d --rm -e SECRET_KEY=my-secret-key \
    -e MAIL_SERVER=smtp.googlemail.com -e MAIL_PORT=587 -e MAIL_USE_TLS=true \
    -e MAIL_USERNAME=<your-gmail-username> -e MAIL_PASSWORD=<your-gmail-password> \
    --link mysql:dbserver --link redis:redis-server \
    -e DATABASE_URL=mysql+pymysql://bloglite:<database-password>@dbserver/bloglite \
    -e REDIS_URL=redis://redis-server:6379/0 \
    --entrypoint venv/bin/rq \
    bloglite:latest worker -u redis://redis-server:6379/0 blog-tasks
```
// TODO: merge docker run commands ^-^


## run via Heroku

### Add Postgres
```shell script
$ heroku addons:add heroku-postgresql:hobby-dev
```

### Add SearchBox
```shell script
$ heroku addons:create searchbox:starter
$ heroku config:get SEARCHBOX_URL
<your-elasticsearch-url>
$ heroku config:set ELASTICSEARCH_URL=<your-elasticsearch-url>
```

### Add Redis
```shell script
$ heroku addons:create heroku-redis:hobby-dev
```

** inspired by: 'https://habr.com/ru/post/346306/'
