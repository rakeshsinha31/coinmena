<h1 align="center">Coinmena API</h1>

## Requirements

- [Docker >= 20.10.7](https://docs.docker.com/get-docker/)
- [Python >= 3.8.10](https://www.python.org/downloads/release/python-3811/)
- [Django >= 3.2.8](https://docs.djangoproject.com/en/3.2/topics/install/)

> **NOTE** - Run all commands from the project root

## Run Locally
```shell
python manage.py makemigrations
python manage.py migrate
python manage.py createsuperuser
python manage.py runserver

```

## Creating User token
To get the API token, any REST client (eg. Postman) or curl could be used for calling the end point. Pass the Username and password as Headers:
```shell
http://0.0.0.0:8000/api-token-auth/
```

## Calling the APIs
pass the token under Authorization Headers
```
GET - http://0.0.0.0:8000/api/v1/quotes
POST - http://0.0.0.0:8000/api/v1/quotes/
```

## Docker
Build images with:
```shell
docker-compose build
```
Run docker images with:
```shell
docker-compose up
```


