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
