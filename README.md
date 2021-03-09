# This is a project using microservice to deploy dockerized flask app
## setup python environment

``` shell
    pipenv install flask
```

## freeze dependencies into requirements.txt file

``` shell
    pipenv lock -r > requirements.txt
```

## build docker image from Dockerfile

``` shell
    docker build -t json-parsing .
```

## run docker container based on blueprint json-parsing

``` shell
    docker run -it --name json-parsing-container -p 3200:3200 json-parsing
```

## run docker container based on blueprint json-parsing in the background

``` shell
    docker run -d --name json-parsing-container -p 3200:3200 json-parsing
```
