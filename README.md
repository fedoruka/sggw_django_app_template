# sggw_django_app_template

Simple Django application that could be used as a project template or Docker excericise. 

## First run

```bash
$ python -m venv venv 
$ source venv/bin/activate
$ cd sggw_template
$ pip install -r requirements.txt
$ python manage.py migrate
$ python manage.py createsuperuser
$ python manage.py runserver
```

## URLs

- / - main page, list of polls
- /{id} - poll details view
- /admin - admin panel


## Docker

```bash
$ cd sggw_template
$ docker build --tag docker-django-app:latest .
$ docker run -p 8000:80  docker-django-app:latest # ctrl + c to stop
$ docker run -p 8000:80  docker-django-app:latest -d # deatached mode

$ docker ps
$ docker stop %id%

$ cd ..
$ docker-compose up # or docker-compose up -d
```